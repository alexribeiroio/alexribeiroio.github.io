(function () {
  function capture(event, properties) {
    const ph = window.posthog;
    if (!ph || typeof ph.capture !== 'function') return;
    if (typeof ph.has_opted_out_capturing === 'function' && ph.has_opted_out_capturing()) {
      return;
    }
    ph.capture(event, properties);
  }

  function placementFor(el) {
    if (el.closest('.header')) return 'header';
    if (el.closest('.home-info')) return 'home';
    if (el.closest('.footer')) return 'footer';
    if (el.closest('.post-content') || el.closest('.post-single')) return 'sobre';
    return 'other';
  }

  function destinationFor(anchor) {
    const named = anchor.getAttribute('data-ph-outbound');
    if (named) return named;
    try {
      const host = new URL(anchor.href, window.location.origin).hostname.replace(/^www\./, '');
      if (host.includes('github')) return 'github';
      if (host.includes('instagram')) return 'instagram';
      if (host.includes('linkedin')) return 'linkedin';
      if (anchor.getAttribute('href')?.includes('index.xml') || host === location.hostname) {
        if (anchor.getAttribute('href')?.includes('.xml')) return 'rss';
      }
      return host || 'external';
    } catch {
      return 'external';
    }
  }

  function bindThemeToggle() {
    const toggle = document.getElementById('theme-toggle');
    if (!toggle || toggle.dataset.phBound) return;
    toggle.dataset.phBound = '1';
    toggle.addEventListener('click', () => {
      const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      capture('theme_toggled', { theme });
    });
  }

  function bindClicks() {
    document.addEventListener('click', (event) => {
      const target = event.target instanceof Element ? event.target : null;
      if (!target) return;

      const cta = target.closest('[data-ph-cta]');
      if (cta) {
        capture('cta_clicked', {
          cta_id: cta.getAttribute('data-ph-cta'),
          href: cta.getAttribute('href') || undefined,
        });
        return;
      }

      const outbound = target.closest('a[data-ph-outbound], a.rss-link, a.feed-link');
      if (outbound) {
        const href = outbound.getAttribute('href') || '';
        const isExternal =
          outbound.hasAttribute('data-ph-outbound') ||
          outbound.classList.contains('rss-link') ||
          outbound.classList.contains('feed-link') ||
          /^https?:\/\//i.test(href);
        if (!isExternal) return;
        capture('outbound_click', {
          destination: destinationFor(outbound),
          placement: outbound.getAttribute('data-ph-placement') || placementFor(outbound),
        });
        return;
      }

      const result = target.closest('#searchResults a');
      if (result) {
        const links = Array.from(document.querySelectorAll('#searchResults a'));
        capture('search_result_clicked', { position: links.indexOf(result) });
      }
    });
  }

  function bindSearch() {
    window.__phSearch = function (queryLength) {
      if (typeof queryLength !== 'number' || queryLength < 2) return;
      capture('search_submitted', { query_length: queryLength });
    };
  }

  function bindScrollDepth() {
    const content = document.querySelector('.post-content');
    const page = window.__PH_PAGE__ || {};
    if (!content || page.section !== 'posts' || page.kind !== 'page') return;

    const marks = [25, 50, 75, 100];
    const seen = new Set();

    function check() {
      const rect = content.getBoundingClientRect();
      const viewBottom = window.innerHeight;
      const total = content.offsetHeight;
      if (total <= 0) return;
      const scrolled = Math.min(Math.max(viewBottom - rect.top, 0), total);
      const percent = Math.round((scrolled / total) * 100);
      for (const mark of marks) {
        if (percent >= mark && !seen.has(mark)) {
          seen.add(mark);
          capture('post_scroll_depth', {
            percent: mark,
            postId: page.postId,
            slug: page.slug,
          });
        }
      }
    }

    let ticking = false;
    window.addEventListener(
      'scroll',
      () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => {
          ticking = false;
          check();
        });
      },
      { passive: true }
    );
    check();
  }

  function init() {
    bindThemeToggle();
    bindClicks();
    bindSearch();
    bindScrollDepth();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
