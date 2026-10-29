(function () {
  var root = document.documentElement;
  var KEY_LANG = 'cc-chart-legal.lang', KEY_MODE = 'cc-chart-legal.mode';
  function save(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  function setLang(lang) {
    root.setAttribute('data-lang', lang);
    root.lang = lang;
    var t = document.querySelector('title[data-en]');
    if (t) document.title = t.getAttribute('data-' + lang);
    document.querySelectorAll('[data-set-lang]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-set-lang') === lang));
    });
  }
  function setMode(mode) {
    root.setAttribute('data-mode', mode);
    var btn = document.querySelector('[data-toggle-mode]');
    if (btn) {
      var en = mode === 'dark' ? 'Switch to light theme' : 'Switch to dark theme';
      var vi = mode === 'dark' ? 'Chuyển sang giao diện sáng' : 'Chuyển sang giao diện tối';
      btn.setAttribute('aria-label', root.getAttribute('data-lang') === 'vi' ? vi : en);
    }
    window.dispatchEvent(new Event('cc-mode'));
  }

  document.querySelectorAll('[data-set-lang]').forEach(function (b) {
    b.addEventListener('click', function () {
      var l = b.getAttribute('data-set-lang');
      setLang(l); save(KEY_LANG, l);
      setMode(root.getAttribute('data-mode') || 'dark');
    });
  });
  var modeBtn = document.querySelector('[data-toggle-mode]');
  if (modeBtn) modeBtn.addEventListener('click', function () {
    var m = root.getAttribute('data-mode') === 'light' ? 'dark' : 'light';
    setMode(m); save(KEY_MODE, m);
  });

  setLang(root.getAttribute('data-lang') === 'vi' ? 'vi' : 'en');
  setMode(root.getAttribute('data-mode') === 'light' ? 'light' : 'dark');
})();
