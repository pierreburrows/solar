(function () {
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* announcement bar */
  var ann = d.querySelector('.announce');
  try { if (ann && sessionStorage.getItem('ev-ann') === '0') ann.classList.add('hide'); } catch (e) {}
  var annX = d.querySelector('.announce .x');
  if (annX) annX.addEventListener('click', function () {
    ann.classList.add('hide');
    try { sessionStorage.setItem('ev-ann', '0'); } catch (e) {}
  });

  /* nav state on scroll */
  var onScroll = function () { root.classList.toggle('scrolled', window.scrollY > 40); };
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  /* mega menu */
  var trig = d.querySelector('[data-mega]'), mega = d.querySelector('.mega'), t;
  function setMega(open) {
    if (!mega) return;
    mega.classList.toggle('open', open);
    trig.setAttribute('aria-expanded', open ? 'true' : 'false');
    var v = mega.querySelector('video');
    if (v) { open ? v.play().catch(function(){}) : v.pause(); }
  }
  if (trig && mega) {
    trig.addEventListener('click', function () { setMega(!mega.classList.contains('open')); });
    [trig, mega].forEach(function (el) {
      el.addEventListener('mouseenter', function () { clearTimeout(t); setMega(true); });
      el.addEventListener('mouseleave', function () { t = setTimeout(function () { setMega(false); }, 180); });
    });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMega(false); });
    d.addEventListener('click', function (e) { if (!e.target.closest('.navbar')) setMega(false); });
  }

  /* mobile sheet */
  var sheet = d.querySelector('.sheet');
  d.querySelectorAll('[data-sheet]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = !sheet.classList.contains('open');
      sheet.classList.toggle('open', open);
      d.body.style.overflow = open ? 'hidden' : '';
    });
  });

  /* hero film sequencer: plug-in -> aerial -> logo, crossfaded */
  var hero = d.querySelector('.hero');
  if (hero) {
    var vids = [].slice.call(hero.querySelectorAll('.hero-media video'));
    var poster = hero.querySelector('.hero-media img');
    var chaps = [].slice.call(hero.querySelectorAll('.chapter'));
    var cur = -1, FADE = 0.9;
    function show(i) {
      if (i === cur) return;
      var next = vids[i];
      try { next.currentTime = 0; } catch (e) {}
      var p = next.play();
      var go = function () {
        vids.forEach(function (v, k) { v.classList.toggle('on', k === i); });
        if (poster) poster.classList.remove('on');
        hero.classList.toggle('logo-moment', i === vids.length - 1);
        chaps.forEach(function (c, k) { c.classList.toggle('active', k === i); if (k !== i) c.style.setProperty('--p', k < i ? '100%' : '0%'); });
        var prev = vids[cur]; cur = i;
        if (prev) setTimeout(function () { prev.pause(); }, 1200);
      };
      if (p && p.then) p.then(go).catch(function () { /* autoplay blocked: keep poster */ });
      else go();
    }
    vids.forEach(function (v, i) {
      v.addEventListener('timeupdate', function () {
        if (i !== cur || !v.duration) return;
        var pct = Math.min(100, v.currentTime / v.duration * 100);
        if (chaps[i]) chaps[i].style.setProperty('--p', pct + '%');
        // the last clip (logo) is held a little longer before looping
        var lead = i === vids.length - 1 ? 0.15 : FADE;
        if (v.duration - v.currentTime < lead) show((i + 1) % vids.length);
      });
      v.addEventListener('ended', function () { if (i === cur) show((i + 1) % vids.length); });
    });
    chaps.forEach(function (c, i) { c.addEventListener('click', function () { show(i); }); });
    if (!reduce && vids.length) {
      if (vids[0].readyState >= 2) show(0); else vids[0].addEventListener('canplay', function h() { vids[0].removeEventListener('canplay', h); show(0); });
    }
  }

  /* play looping videos only while on screen */
  var lazyVids = d.querySelectorAll('video[data-inview]');
  if ('IntersectionObserver' in window) {
    var vio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) {
          if (!v.src && v.dataset.src) v.src = v.dataset.src;
          if (!reduce) v.play().catch(function () {});
        } else v.pause();
      });
    }, { rootMargin: '200px 0px' });
    lazyVids.forEach(function (v) { vio.observe(v); });

    var rio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); rio.unobserve(e.target); } });
    }, { threshold: .12 });
    d.querySelectorAll('.rv').forEach(function (el) { rio.observe(el); });

    /* animated counters */
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, end = +el.dataset.count, pre = el.dataset.pre || '', t0 = null;
        cio.unobserve(el);
        if (reduce) { el.textContent = pre + end.toLocaleString('en-GB'); return; }
        requestAnimationFrame(function step(ts) {
          if (!t0) t0 = ts;
          var k = Math.min(1, (ts - t0) / 1400), ease = 1 - Math.pow(1 - k, 3);
          el.textContent = pre + Math.round(end * ease).toLocaleString('en-GB');
          if (k < 1) requestAnimationFrame(step);
        });
      });
    }, { threshold: .5 });
    d.querySelectorAll('[data-count]').forEach(function (el) { cio.observe(el); });
  } else {
    d.querySelectorAll('.rv').forEach(function (el) { el.classList.add('in'); });
  }

  var y = d.getElementById('year'); if (y) y.textContent = new Date().getFullYear();

  /* quote form */
  d.querySelectorAll('form.quote').forEach(function (form) {
    var params = new URLSearchParams(location.search), svc = params.get('service');
    if (svc && form.service) for (var i = 0; i < form.service.options.length; i++) if (form.service.options[i].value === svc) form.service.selectedIndex = i;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = new FormData(form), endpoint = form.getAttribute('data-endpoint'), ok = form.querySelector('.form-success');
      if (endpoint) {
        fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (r) { if (!r.ok) throw 0; form.reset(); ok.style.display = 'block'; })
          .catch(function () { mailto(form, data); });
      } else mailto(form, data);
    });
  });
  function mailto(form, data) {
    var lines = [];
    data.forEach(function (v, k) { if (v) lines.push(k.charAt(0).toUpperCase() + k.slice(1) + ': ' + v); });
    location.href = 'mailto:' + form.getAttribute('data-email') + '?subject=' + encodeURIComponent('Quote request – ' + (data.get('service') || 'General enquiry')) + '&body=' + encodeURIComponent(lines.join('\n'));
  }
})();
