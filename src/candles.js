(function () {
  var cv = document.getElementById('candles');
  if (!cv) return;
  var ctx = cv.getContext('2d');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var seed = 7;
  function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }

  var N = 44, bars = [], p = 100;
  for (var i = 0; i < N; i++) {
    var drift = Math.sin(i / 7) * 0.6 + 0.25;
    var o = p, c = o + (rnd() - 0.45 + drift * 0.4) * 2.4;
    var h = Math.max(o, c) + rnd() * 1.4, l = Math.min(o, c) - rnd() * 1.4;
    bars.push({ o: o, h: h, l: l, c: c });
    p = c;
  }

  function css(name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }
  var shown = reduce ? N : 0, start = null;

  function draw() {
    var dpr = window.devicePixelRatio || 1;
    var w = cv.clientWidth, h = cv.clientHeight;
    if (cv.width !== Math.round(w * dpr) || cv.height !== Math.round(h * dpr)) {
      cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    var up = css('--accent'), down = css('--down'), grid = css('--line'), ma = css('--ma');
    var lo = Infinity, hi = -Infinity;
    bars.forEach(function (b) { lo = Math.min(lo, b.l); hi = Math.max(hi, b.h); });
    var padT = 16, padB = 16, padX = 12;
    function y(v) { return padT + (hi - v) / (hi - lo) * (h - padT - padB); }

    ctx.strokeStyle = grid; ctx.lineWidth = 1; ctx.setLineDash([2, 4]);
    for (var g = 1; g < 4; g++) {
      var gy = Math.round(padT + g * (h - padT - padB) / 4) + 0.5;
      ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(w, gy); ctx.stroke();
    }
    ctx.setLineDash([]);

    var step = (w - padX * 2) / N, bw = Math.max(2, step * 0.62);
    for (var i = 0; i < Math.floor(shown); i++) {
      var b = bars[i], x = padX + i * step + step / 2, col = b.c >= b.o ? up : down;
      ctx.strokeStyle = col; ctx.fillStyle = col;
      ctx.beginPath(); ctx.moveTo(Math.round(x) + 0.5, y(b.h)); ctx.lineTo(Math.round(x) + 0.5, y(b.l)); ctx.stroke();
      var top = y(Math.max(b.o, b.c)), bh = Math.max(1, Math.abs(y(b.o) - y(b.c)));
      ctx.fillRect(x - bw / 2, top, bw, bh);
    }

    ctx.strokeStyle = ma; ctx.lineWidth = 1.5; ctx.beginPath();
    var started = false;
    for (var j = 6; j < Math.floor(shown); j++) {
      var s = 0; for (var k = j - 6; k <= j; k++) s += bars[k].c;
      var mx = padX + j * step + step / 2, my = y(s / 7);
      if (!started) { ctx.moveTo(mx, my); started = true; } else ctx.lineTo(mx, my);
    }
    ctx.stroke();

    if (shown >= N) {
      var last = bars[N - 1], ly = Math.round(y(last.c)) + 0.5, lc = last.c >= last.o ? up : down;
      ctx.strokeStyle = lc; ctx.setLineDash([3, 3]); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(0, ly); ctx.lineTo(w, ly); ctx.stroke(); ctx.setLineDash([]);
    }
  }

  function intro(t) {
    if (start === null) start = t;
    shown = Math.min(N, (t - start) / 900 * N);
    draw();
    if (shown < N) requestAnimationFrame(intro);
  }

  function tick() {
    var b = bars[N - 1];
    b.c += (rnd() - 0.5) * 0.9;
    b.h = Math.max(b.h, b.c); b.l = Math.min(b.l, b.c);
    draw();
  }

  if (reduce) draw(); else requestAnimationFrame(intro);
  if (!reduce) setInterval(function () { if (shown >= N && !document.hidden) tick(); }, 1400);
  window.addEventListener('cc-mode', draw);
  if (window.ResizeObserver) new ResizeObserver(draw).observe(cv); else window.addEventListener('resize', draw);
})();
