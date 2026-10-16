(() => {
  const section = document.querySelector('.comments');
  if (!section) return;
  const theme = () => document.documentElement.dataset.theme === 'dark' ? 'dark_dimmed' : 'light';
  const script = document.createElement('script');
  script.src = 'https://giscus.app/client.js';
  script.async = true;
  script.crossOrigin = 'anonymous';
  const settings = {
    repo: section.dataset.repo,
    'repo-id': section.dataset.repoId,
    category: section.dataset.category,
    'category-id': section.dataset.categoryId,
    mapping: 'specific',
    term: section.dataset.term,
    strict: '1',
    'reactions-enabled': '1',
    'emit-metadata': '0',
    'input-position': 'top',
    theme: theme(),
    lang: 'pt',
    loading: 'lazy',
  };
  Object.entries(settings).forEach(([key, value]) => script.setAttribute(`data-${key}`, value));
  section.querySelector('.giscus').appendChild(script);
  new MutationObserver(() => {
    document.querySelector('iframe.giscus-frame')?.contentWindow.postMessage(
      { giscus: { setConfig: { theme: theme() } } }, 'https://giscus.app'
    );
  }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
})();
