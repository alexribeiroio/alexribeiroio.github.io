(function () {
  const STORAGE_KEY = 'ph_consent';
  const config = window.__PH_CONFIG__;
  if (!config || !config.apiKey) return;

  const banner = document.getElementById('cookies');
  const acceptBtn = document.getElementById('ph-consent-accept');
  const denyBtn = document.getElementById('ph-consent-deny');
  const manageLinks = document.querySelectorAll('[data-ph-manage-cookies]');

  let loading = false;

  function getConsent() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch {
      return null;
    }
  }

  function setConsent(value) {
    try {
      localStorage.setItem(STORAGE_KEY, value);
    } catch {
      /* ignore quota / private mode */
    }
  }

  function showBanner() {
    if (!banner) return;
    banner.hidden = false;
    banner.setAttribute('aria-hidden', 'false');
  }

  function hideBanner() {
    if (!banner) return;
    banner.hidden = true;
    banner.setAttribute('aria-hidden', 'true');
  }

  function notifyReady() {
    document.dispatchEvent(new CustomEvent('ph:ready'));
    const queue = window.__PH_ON_READY__;
    if (Array.isArray(queue)) {
      while (queue.length) {
        try {
          queue.shift()();
        } catch {
          /* ignore listener errors */
        }
      }
    }
  }

  function loadPostHog() {
    if (loading || (window.posthog && window.posthog.__loaded)) {
      if (window.posthog && typeof window.posthog.opt_in_capturing === 'function') {
        window.posthog.opt_in_capturing();
      }
      notifyReady();
      return;
    }
    loading = true;

    !(function (t, e) {
      var o, n, p, r;
      e.__SV ||
        (window.posthog && window.posthog.__loaded) ||
        ((window.posthog = e),
        (e._i = []),
        (e.init = function (i, s, a) {
          function g(t, e) {
            var o = e.split('.');
            2 == o.length && ((t = t[o[0]]), (e = o[1]));
            t[e] = function () {
              t.push([e].concat(Array.prototype.slice.call(arguments, 0)));
            };
          }
          (p = t.createElement('script')),
            (p.type = 'text/javascript'),
            (p.crossOrigin = 'anonymous'),
            (p.async = !0),
            (p.src =
              s.api_host.replace('.i.posthog.com', '-assets.i.posthog.com') +
              '/static/array.js'),
            (r = t.getElementsByTagName('script')[0]),
            r.parentNode.insertBefore(p, r);
          var u = e;
          for (
            void 0 !== a ? (u = e[a] = []) : (a = 'posthog'),
              u.people = u.people || [],
              Object.defineProperty(u, 'toString', {
                configurable: !0,
                enumerable: !0,
                writable: !0,
                value: function (t) {
                  var e = 'posthog';
                  return (
                    'posthog' !== a && (e += '.' + a), t || (e += ' (stub)'), e
                  );
                },
              }),
              Object.defineProperty(u.people, 'toString', {
                configurable: !0,
                enumerable: !0,
                writable: !0,
                value: function () {
                  return u.toString(1) + '.people (stub)';
                },
              }),
              (o =
                'vu pu gu mu init Gu Qu Hu Wu Xu il Vu Yu ju oc ac lc uc cc hc capture getExtension Zu hu gc calculateEventProperties vc register register_once register_for_session unregister unregister_for_session zu mc getFeatureFlag getFeatureFlagPayload getFeatureFlagResult getAllFeatureFlags isFeatureEnabled reloadFeatureFlags updateFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSurveysLoaded onSessionId getSurveys getActiveMatchingSurveys onActiveMatchingSurveysChanged renderSurvey displaySurvey cancelPendingSurvey canRenderSurvey canRenderSurveyAsync wc identify setPersonProperties unsetPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset kc shutdown setIdentity clearIdentity get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException addExceptionStep captureLog startExceptionAutocapture stopExceptionAutocapture loadToolbar get_property getSessionProperty yc nc createPersonProfile setInternalOrTestUser bc xu ku opt_in_capturing opt_out_capturing Su has_opted_in_capturing has_opted_out_capturing get_explicit_consent_status is_capturing clear_opt_in_out_capturing tc debug nl Os getPageViewId captureTraceFeedback captureTraceMetric Du'.split(
                  ' '
                )),
              (n = 0);
            n < o.length;
            n++
          )
            g(u, o[n]);
          e._i.push([i, s, a]);
        }),
        (e.__SV = 1));
    })(document, window.posthog || []);

    const page = window.__PH_PAGE__ || {};
    const register = { site: 'alexribeiro.io' };
    if (page.section) register.section = page.section;
    if (page.kind) register.kind = page.kind;
    if (page.postId) register.postId = page.postId;
    if (page.slug) register.slug = page.slug;
    if (page.categorias) register.categorias = page.categorias;
    if (page.tags) register.tags = page.tags;

    window.posthog.init(config.apiKey, {
      api_host: config.apiHost,
      defaults: config.defaults || '2026-05-30',
      person_profiles: 'identified_only',
      capture_pageview: true,
      autocapture: false,
      disable_session_recording: true,
      loaded: function (ph) {
        ph.register(register);
        notifyReady();
      },
    });
  }

  function accept() {
    setConsent('granted');
    hideBanner();
    loadPostHog();
  }

  function deny() {
    setConsent('denied');
    hideBanner();
    if (window.posthog && typeof window.posthog.opt_out_capturing === 'function') {
      window.posthog.opt_out_capturing();
    }
  }

  function manage(event) {
    if (event) {
      event.preventDefault();
      event.stopPropagation();
    }
    showBanner();
    const acceptControl = acceptBtn || banner;
    if (acceptControl && typeof acceptControl.focus === 'function') {
      acceptControl.focus();
    }
  }

  acceptBtn?.addEventListener('click', accept);
  denyBtn?.addEventListener('click', deny);
  manageLinks.forEach((el) => el.addEventListener('click', manage));

  const consent = getConsent();
  if (consent === 'granted') {
    loadPostHog();
  }

  if (location.hash === '#cookies') {
    showBanner();
  } else if (consent === 'granted' || consent === 'denied') {
    hideBanner();
  } else {
    showBanner();
  }
})();
