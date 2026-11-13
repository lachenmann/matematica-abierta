/* MA-ART-0026 · Laboratorio de integración. JavaScript sin dependencias.
 * Los ínfimos y supremos se calculan analíticamente, no por muestreo.
 * No se simula la función de Dirichlet mediante aritmética de coma flotante.
 */
(() => {
  'use strict';
  const NS = 'http://www.w3.org/2000/svg';
  const PI2 = 2 * Math.PI;
  const EPS = 1e-11;
  const fmt = new Intl.NumberFormat('es-CL', { maximumFractionDigits: 5 });
  const $ = id => document.getElementById(id);
  const state = { fn: 'cuadrado', n: 8, c: 0.43, partition: 'uniforme', tags: 'medio', display: 'ambos', epsilon: 0.10, seed: 17, customTags: {} };
  const labels = {
    cuadrado: 'f(x) = x²', seno: 'f(x) = sen(2πx)',
    escalon: 'h(x) = 1 si x ≥ c', dirichlet: 'q(x) = 1 si x ∈ ℚ'
  };
  const normalTagOptions = [
    ['izquierda', 'Extremos izquierdos'], ['medio', 'Puntos medios'],
    ['derecha', 'Extremos derechos'], ['alternas', 'Alternadas'],
    ['aleatorias', 'Aleatorias reproducibles'], ['personalizadas', 'Personalizadas (gráfico)']
  ];
  const rationalTagOptions = [['racionales', 'Todas racionales'], ['irracionales', 'Todas irracionales']];

  function bounded(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
  function num(v) { return Math.abs(v) < 1e-12 ? '0' : fmt.format(v); }
  function exactValue(fn, c) {
    switch (fn) { case 'cuadrado': return 1 / 3; case 'seno': return 0; case 'escalon': return 1 - c; default: return null; }
  }
  function valueAt(fn, x, c) {
    switch (fn) {
      case 'cuadrado': return x * x;
      case 'seno': return Math.sin(PI2 * x);
      case 'escalon': return x >= c ? 1 : 0;
      default: return NaN;
    }
  }
  /* Definiciones exactas para los cuatro ejemplos, con el carácter cerrado de I_i. */
  function extrema(fn, a, b, c) {
    if (fn === 'cuadrado') return [a * a, b * b];
    if (fn === 'dirichlet') return [0, 1];
    if (fn === 'escalon') return [a < c ? 0 : 1, b >= c ? 1 : 0];
    // La función seno tiene críticos interiores en x=1/4 y x=3/4.
    const vs = [Math.sin(PI2 * a), Math.sin(PI2 * b)];
    if (a <= 0.25 && 0.25 <= b) vs.push(1);
    if (a <= 0.75 && 0.75 <= b) vs.push(-1);
    return [Math.min(...vs), Math.max(...vs)];
  }
  function makeRng(seed) {
    let x = seed >>> 0;
    return () => {
      x = (x + 0x6D2B79F5) >>> 0;
      let z = Math.imul(x ^ (x >>> 15), 1 | x);
      z ^= z + Math.imul(z ^ (z >>> 7), 61 | z);
      return ((z ^ (z >>> 14)) >>> 0) / 4294967296;
    };
  }
  function partition(n, mode, seed) {
    if (mode === 'uniforme') {
      const p = Array.from({ length: n + 1 }, (_, i) => i / n);
      p[n] = 1;
      return p;
    }
    const rand = makeRng(seed);
    const w = Array.from({ length: n }, () => 0.40 + rand() * 1.2);
    const total = w.reduce((a, b) => a + b, 0);
    const p = [0]; let sum = 0;
    for (let i = 0; i < n - 1; i++) { sum += w[i] / total; p.push(sum); }
    p.push(1);
    return p;
  }
  function tagFraction(i, mode, n, seed, custom) {
    if (mode === 'personalizadas') return Object.prototype.hasOwnProperty.call(custom, i) ? custom[i] : 0.5;
    if (mode === 'izquierda') return 0;
    if (mode === 'derecha') return 1;
    if (mode === 'alternas') return i % 2 === 0 ? 0 : 1;
    if (mode === 'aleatorias') return makeRng((seed * 151 + n * 31 + i * 8191) >>> 0)();
    return 0.5;
  }
  function sums(fn, p, tags, seed, c, custom = {}) {
    const details = [];
    let L = 0, S = 0, U = 0, maxMesh = 0;
    for (let i = 0; i < p.length - 1; i++) {
      const a = p[i], b = p[i + 1], dx = b - a;
      const [mi, ma] = extrema(fn, a, b, c);
      const r = tagFraction(i, tags, p.length - 1, seed, custom);
      const xi = a + r * dx;
      const yi = fn === 'dirichlet' ? (tags === 'irracionales' ? 0 : 1) : valueAt(fn, xi, c);
      L += mi * dx; S += yi * dx; U += ma * dx;
      maxMesh = Math.max(maxMesh, dx);
      details.push({ a, b, dx, mi, ma, xi, yi, i });
    }
    if (L > S + EPS || S > U + EPS) throw new Error(`Cálculo incoherente: L=${L}, S=${S}, U=${U}`);
    return { L, S, U, gap: Math.max(0, U - L), maxMesh, details };
  }
  function svgNode(tag, attrs = {}, textValue = null) {
    const el = document.createElementNS(NS, tag);
    for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, String(v));
    if (textValue !== null) el.textContent = textValue;
    return el;
  }
  function add(svg, tag, attrs = {}, text = null) {
    const node = svgNode(tag, attrs, text);
    svg.appendChild(node); return node;
  }
  function clear(svg) { while (svg.firstChild) svg.removeChild(svg.firstChild); }
  function line(svg, x1, y1, x2, y2, attrs = {}) { return add(svg, 'line', { x1, y1, x2, y2, ...attrs }); }
  function textAt(svg, x, y, str, more = {}) { return add(svg, 'text', { x, y, class: 'svg-text', ...more }, str); }

  function mainPlot(res, p) {
    const svg = $('grafico-principal'); clear(svg);
    const left = 68, right = 960, top = 27, bottom = 369, w = right - left;
    const range = state.fn === 'seno' ? [-1.16, 1.16] : [-0.14, 1.17];
    const [low, high] = range;
    const X = x => left + w * x;
    const Y = y => bottom - (y - low) / (high - low) * (bottom - top);
    const zero = Y(0);
    add(svg, 'rect', { x: left, y: top, width: right - left, height: bottom - top, fill: '#fbfdfc' });
    const yTicks = state.fn === 'seno' ? [-1, -.5, 0, .5, 1] : [0, .25, .5, .75, 1];
    for (const val of yTicks) {
      const y = Y(val);
      line(svg, left, y, right, y, { class: val === 0 ? 'svg-axis' : 'svg-grid' });
      textAt(svg, left - 14, y + 5, num(val), { class: 'svg-tick', 'text-anchor': 'end' });
    }
    for (let k = 0; k <= 4; k++) {
      const xx = X(k / 4);
      line(svg, xx, top, xx, bottom, { class: 'svg-grid' });
      textAt(svg, xx, bottom + 24, num(k / 4), { class: 'svg-tick', 'text-anchor': 'middle' });
    }
    textAt(svg, right - 1, bottom + 43, 'x', { class: 'svg-label', 'text-anchor': 'end' });
    textAt(svg, left - 24, top + 3, 'y', { class: 'svg-label', 'text-anchor': 'middle' });

    const showS = state.display !== 'darboux';
    const showLU = state.display !== 'riemann';
    for (const d of res.details) {
      const x0 = X(d.a), x1 = X(d.b), bw = Math.max(0, x1 - x0), xPad = 0.55;
      if (showLU) {
        const yMa = Y(d.ma), yMi = Y(d.mi);
        add(svg, 'rect', { x: x0 + xPad, y: yMa, width: Math.max(0, bw - xPad * 2), height: Math.max(0, yMi - yMa), fill: '#a793b6', opacity: '.33' });
        if (state.display === 'darboux') {
          for (const [val, color] of [[d.ma, '#b77f83'], [d.mi, '#4b91a5']]) {
            const yy = Y(val);
            add(svg, 'rect', { x: x0 + xPad, y: Math.min(yy, zero), width: Math.max(0, bw - 2 * xPad), height: Math.abs(zero - yy), fill: color, opacity: '.12' });
          }
        }
        if (bw >= 4) {
          line(svg, x0, yMa, x1, yMa, { stroke: '#ad7081', 'stroke-width': 2.2, opacity: .91 });
          line(svg, x0, yMi, x1, yMi, { stroke: '#418ca4', 'stroke-width': 2.2, opacity: .91 });
        }
      }
      if (showS) {
        const yy = Y(d.yi);
        add(svg, 'rect', { x: x0 + xPad, y: Math.min(yy, zero), width: Math.max(0, bw - 2 * xPad), height: Math.abs(yy - zero), fill: '#c17a5f', opacity: state.display === 'ambos' ? .41 : .51 });
        if (state.fn !== 'dirichlet' && bw >= 8) {
          add(svg, 'circle', { cx: X(d.xi), cy: yy, r: state.n <= 30 ? 4.4 : 2.8, fill: '#9c5b44', stroke: '#fff', 'stroke-width': 1.5 });
        }
      }
      if (bw >= 3) line(svg, x0, top, x0, bottom, { stroke: '#d9e3e3', 'stroke-width': 1, opacity: .9 });
    }
    line(svg, right, top, right, bottom, { stroke: '#d9e3e3', 'stroke-width': 1 });

    if (state.fn === 'cuadrado' || state.fn === 'seno') {
      const d = Array.from({ length: 501 }, (_, i) => `${i ? 'L' : 'M'}${X(i / 500).toFixed(2)} ${Y(valueAt(state.fn, i / 500, state.c)).toFixed(2)}`).join(' ');
      add(svg, 'path', { d, class: 'svg-curve' });
    } else if (state.fn === 'escalon') {
      const x = X(state.c);
      add(svg, 'path', { d: `M${X(0)} ${Y(0)} H${x} M${x} ${Y(1)} H${X(1)}`, class: 'svg-curve' });
      line(svg, x, Y(0), x, Y(1), { stroke: '#aebdc0', 'stroke-dasharray': '5 6', 'stroke-width': 1.5 });
      add(svg, 'circle', { cx: x, cy: Y(0), r: 5, fill: '#fff', stroke: '#275f72', 'stroke-width': 2.5 });
      add(svg, 'circle', { cx: x, cy: Y(1), r: 5, fill: '#275f72', stroke: '#fff', 'stroke-width': 1.4 });
      textAt(svg, x + 9, Y(1) - 12, `c = ${num(state.c)}`, { class: 'svg-label' });
    } else {
      add(svg, 'rect', { x: left + 150, y: top + 32, width: 588, height: 67, rx: 9, fill: '#ffffff', opacity: .96, stroke: '#e3e8e7' });
      textAt(svg, (left + right) / 2, top + 60, 'No dibujamos una curva de Dirichlet', { class: 'svg-label', 'text-anchor': 'middle', 'font-weight': 750 });
      textAt(svg, (left + right) / 2, top + 82, 'En cada tramo: ínfimo 0 y supremo 1', { class: 'svg-tick', 'text-anchor': 'middle' });
    }
    if (state.fn !== 'dirichlet') {
      for (const d of res.details) {
        const x0 = X(d.a), bw = X(d.b) - x0;
        const hit = add(svg, 'rect', { x: x0, y: top, width: bw, height: bottom - top, class: 'svg-control-hit', tabindex: 0, role: 'button', 'data-interval-index': d.i, 'aria-label': `Cambiar etiqueta del tramo ${d.i + 1}` });
        const title = add(hit, 'title'); title.textContent = `Tramo ${d.i + 1}: [${num(d.a)}, ${num(d.b)}], ínfimo ${num(d.mi)}, supremo ${num(d.ma)}. Pulsa para colocar una etiqueta.`;
      }
    }
    textAt(svg, (left + right) / 2, 420, state.fn === 'dirichlet' ? 'Las etiquetas se eligen por tipo (racionales o irracionales), no por aproximación decimal.' : 'Pulsa sobre una franja vertical para situar allí una etiqueta.', { class: 'svg-tick', 'text-anchor': 'middle' });
  }

  function seriesData() {
    const output = [];
    for (let n = 2; n <= 100; n++) {
      const mode = state.tags === 'personalizadas' ? 'medio' : state.tags;
      const r = sums(state.fn, partition(n, 'uniforme', 0), mode, state.seed, state.c);
      output.push({ n, L: r.L, S: r.S, U: r.U, gap: r.gap });
    }
    return output;
  }
  function convergencePlot(data) {
    const svg = $('grafico-convergencia'); clear(svg);
    const left = 73, right = 960, top = 25, bottom = 368;
    const X = n => left + (n - 2) / 98 * (right - left);
    const exact = exactValue(state.fn, state.c);
    const values = data.flatMap(d => [d.L, d.S, d.U]);
    if (exact !== null) values.push(exact);
    let mini = Math.min(...values), maxi = Math.max(...values);
    let span = maxi - mini;
    if (span < 0.02) span = 0.2;
    mini -= span * 0.09; maxi += span * 0.09;
    const Y = val => bottom - ((val - mini) / (maxi - mini)) * (bottom - top);
    add(svg, 'rect', { x: left, y: top, width: right - left, height: bottom - top, fill: '#fbfdfc' });
    for (let i = 0; i <= 4; i++) {
      const val = mini + i / 4 * (maxi - mini);
      const y = Y(val);
      line(svg, left, y, right, y, { class: 'svg-grid' });
      textAt(svg, left - 13, y + 5, num(val), { class: 'svg-tick', 'text-anchor': 'end' });
    }
    [2, 20, 40, 60, 80, 100].forEach(n => {
      line(svg, X(n), top, X(n), bottom, { class: 'svg-grid' });
      textAt(svg, X(n), bottom + 25, String(n), { class: 'svg-tick', 'text-anchor': 'middle' });
    });
    if (exact !== null) line(svg, left, Y(exact), right, Y(exact), { stroke: '#70967e', 'stroke-width': 2, 'stroke-dasharray': '8 5' });
    for (const [key, color] of [['L', '#448ea6'], ['S', '#bd785c'], ['U', '#b27b89']]) {
      const path = data.map((d, i) => `${i ? 'L' : 'M'}${X(d.n).toFixed(2)} ${Y(d[key]).toFixed(2)}`).join(' ');
      add(svg, 'path', { d: path, fill: 'none', stroke: color, 'stroke-width': key === 'S' ? 2.5 : 3, 'stroke-linejoin': 'round' });
    }
    const current = data[state.n - 2];
    line(svg, X(state.n), top, X(state.n), bottom, { stroke: '#49677d', 'stroke-dasharray': '5 7', 'stroke-width': 1.7 });
    for (const [key, color] of [['L', '#448ea6'], ['S', '#bd785c'], ['U', '#b27b89']]) {
      add(svg, 'circle', { cx: X(state.n), cy: Y(current[key]), r: 5.2, fill: color, stroke: '#fff', 'stroke-width': 2 });
    }
    textAt(svg, X(state.n), top - 7, `n = ${state.n}`, { class: 'svg-label', 'text-anchor': 'middle', 'font-weight': '700' });
    textAt(svg, right, bottom + 45, 'n (tramos)', { class: 'svg-label', 'text-anchor': 'end' });
    add(svg, 'rect', { x: left, y: top, width: right - left, height: bottom - top, fill: 'transparent', role: 'button', tabindex: 0, 'aria-label': 'Pulsa para seleccionar un número de tramos entre 2 y 100', id: 'seleccionar-n-en-grafico', cursor: 'crosshair' });
    return current;
  }
  const STAR = [0, 0.20, 0.45, 0.77, 1];
  function refinedUnion(a, b) {
    const vals = [...a, ...b].sort((x, y) => x - y);
    const output = [];
    for (const x of vals) if (output.length === 0 || Math.abs(x - output[output.length - 1]) > 1e-10) output.push(x);
    output[0] = 0; output[output.length - 1] = 1;
    return output;
  }
  function refinementPlot(q, r, affected) {
    const svg = $('grafico-refinacion'); clear(svg);
    const left = 150, right = 950, dx = right - left;
    const X = x => left + dx * x;
    const lines = [
      { key: 'P*', p: STAR, y: 68, color: '#c58c68', note: 'Partición fija' },
      { key: 'Q', p: q, y: 151, color: '#5195a4', note: 'Partición libre' },
      { key: 'R', p: r, y: 233, color: '#6a8b75', note: 'Unión ordenada' }
    ];
    lines.forEach(({ key, p, y, color, note }) => {
      textAt(svg, 20, y - 5, key, { class: 'svg-label', 'font-weight': 800, 'font-size': 24 });
      textAt(svg, 20, y + 17, note, { class: 'svg-tick' });
      if (key === 'Q') affected.forEach(i => {
        add(svg, 'rect', { x: X(p[i]), y: y - 18, width: X(p[i + 1]) - X(p[i]), height: 36, fill: '#e6c7a7', opacity: .72, rx: 2 });
      });
      line(svg, left, y, right, y, { stroke: color, 'stroke-width': 4, 'stroke-linecap': 'round' });
      p.forEach((v, i) => {
        const extra = (i === 0 || i === p.length - 1) ? 15 : 11;
        line(svg, X(v), y - extra, X(v), y + extra, { stroke: color, 'stroke-width': 2.6 });
        if (key === 'P*' && i > 0 && i < p.length - 1) {
          textAt(svg, X(v), y - 24, `t${i}`, { class: 'svg-tick', 'text-anchor': 'middle' });
        }
      });
    });
    textAt(svg, left, 286, '0', { class: 'svg-tick', 'text-anchor': 'middle' });
    textAt(svg, right, 286, '1', { class: 'svg-tick', 'text-anchor': 'middle' });
  }

  function update() {
    const p = partition(state.n, state.partition, state.seed);
    const res = sums(state.fn, p, state.tags, state.seed, state.c, state.customTags);
    $('n').value = String(state.n); $('n-valor').textContent = String(state.n);
    $('salto').value = String(state.c); $('salto-valor').textContent = num(state.c);
    $('jump-control').hidden = state.fn !== 'escalon';
    $('redistribuir').disabled = state.partition !== 'irregular';
    $('funcion-titulo').textContent = labels[state.fn];
    $('particion-detalle').textContent = `${state.n} tramos · partición ${state.partition} · ‖P‖ = ${num(res.maxMesh)}`;
    $('valor-l').textContent = num(res.L);
    $('valor-s').textContent = num(res.S);
    $('valor-u').textContent = num(res.U);
    $('valor-gap').textContent = num(res.gap);
    mainPlot(res, p);

    const exact = exactValue(state.fn, state.c);
    const conclusion = $('conclusion');
    conclusion.classList.toggle('warning', state.fn === 'dirichlet');
    if (state.fn === 'dirichlet') {
      conclusion.innerHTML = '<strong>La brecha nunca se cierra.</strong> Todos los subintervalos de longitud positiva contienen racionales e irracionales: L = 0 y U = 1 para toda partición. No existe integral de Riemann. La elección de etiquetas es conceptual, no una prueba con números decimales.';
    } else {
      const textValue = state.fn === 'cuadrado' && state.partition === 'uniforme' ? ` Para x², con partición uniforme, la brecha exacta es 1/n = ${num(1 / state.n)}.` : '';
      const tail = state.fn === 'seno' ? ' La suma puede acumular contribuciones positivas y negativas.' : state.fn === 'escalon' ? ' La separación procede del tramo que alcanza el punto de salto.' : '';
      conclusion.innerHTML = `<strong>Encierro verificado:</strong> L ≤ S ≤ U. La integral existe y vale <strong>${num(exact)}</strong>; el error de la suma etiquetada es <strong>${num(Math.abs(res.S - exact))}</strong> y nunca supera U − L.${textValue}${tail}`;
    }
    const goal = $('reto-estado');
    const passed = res.gap < state.epsilon - 1e-12;
    goal.classList.toggle('unsolved', !passed);
    if (state.fn === 'dirichlet') goal.textContent = 'Imposible para ε < 1: U − L = 1';
    else goal.textContent = passed ? '✓ Conseguido: U − L < ε' : 'Todavía no: ajusta n o la partición';

    const series = seriesData();
    convergencePlot(series);
    $('convergencia-titulo').textContent = `Sumas para ${labels[state.fn]}`;
    const conv = $('convergencia-lectura');
    conv.classList.toggle('warning', state.fn === 'dirichlet');
    if (state.fn === 'dirichlet') conv.innerHTML = '<strong>No hay convergencia de las cotas:</strong> L permanece en 0 y U permanece en 1, aunque n crezca. Una elección de etiquetas racionales o irracionales genera sumas constantes distintas; ninguna elección aislada demuestra integrabilidad.';
    else if (state.fn === 'cuadrado') conv.innerHTML = `<strong>Convergencia comprobable:</strong> para particiones uniformes de x², U − L = 1/n. Cuando n = ${state.n}, la brecha es ${num(1 / state.n)} y ambas cotas se acercan a 1/3.`;
    else if (state.fn === 'escalon') conv.innerHTML = `<strong>Una discontinuidad aislada:</strong> la brecha está controlada por la malla; en las particiones uniformes vale a lo sumo 1/n. La integral es ${num(exact)}.`;
    else conv.innerHTML = '<strong>Área con signo:</strong> las contribuciones por encima y debajo del eje se compensan. Para esta función senoidal, la integral en [0,1] es 0. La brecha de Darboux tiende a 0 al refinar.';
    document.querySelectorAll('[data-n]').forEach(btn => btn.classList.toggle('current', Number(btn.dataset.n) === state.n));

    const r = refinedUnion(STAR, p);
    const affected = [];
    for (let i = 0; i < p.length - 1; i++) if (STAR.slice(1, -1).some(t => t > p[i] + 1e-11 && t < p[i + 1] - 1e-11)) affected.push(i);
    refinementPlot(p, r, affected);
    const fixed = sums(state.fn, STAR, state.fn === 'dirichlet' ? 'racionales' : 'medio', state.seed, state.c);
    const joined = sums(state.fn, r, state.tags, state.seed, state.c);
    const M = 1, k = STAR.length - 1, bound = fixed.gap + 4 * M * (k - 1) * res.maxMesh;
    $('brecha-p').textContent = num(fixed.gap);
    $('brecha-q').textContent = num(res.gap);
    $('brecha-r').textContent = num(joined.gap);
    $('afectados-q').textContent = String(affected.length);
    $('prueba-lectura').textContent = `Con M = ${M}, k = ${k} y ‖Q‖ = ${num(res.maxMesh)}, la cota del lado derecho vale ${num(bound)}. La brecha real de Q es ${num(res.gap)}. ${res.gap <= bound + 1e-8 ? 'La desigualdad se verifica.' : 'Advertencia: comprobar el cálculo.'} Al refinar, la brecha no puede aumentar: aquí pasa de ${num(res.gap)} en Q a ${num(joined.gap)} en R.`;
  }

  function loadTagOptions(dirichlet) {
    const select = $('etiquetas');
    const vals = dirichlet ? rationalTagOptions : normalTagOptions;
    select.replaceChildren(...vals.map(([v, label]) => {
      const opt = document.createElement('option'); opt.value = v; opt.textContent = label; return opt;
    }));
    state.tags = dirichlet ? 'racionales' : 'medio'; select.value = state.tags;
    $('etiquetas-ayuda').textContent = dirichlet
      ? 'No se infiere la racionalidad de decimales: se comparan familias de etiquetas elegidas matemáticamente.'
      : 'También puedes pulsar cada tramo del gráfico para mover su etiqueta.';
  }
  function installEvents() {
    const controls = { fn: 'funcion', n: 'n', c: 'salto', partition: 'particion', tags: 'etiquetas', display: 'visualizacion', epsilon: 'epsilon' };
    for (const [prop, id] of Object.entries(controls)) {
      $(id).addEventListener(id === 'n' || id === 'salto' ? 'input' : 'change', ev => {
        if (prop === 'fn') {
          state.fn = ev.target.value;
          state.customTags = {};
          loadTagOptions(state.fn === 'dirichlet');
        } else {
          state[prop] = prop === 'n' ? Number(ev.target.value) : prop === 'c' || prop === 'epsilon' ? Number(ev.target.value) : ev.target.value;
          if (prop === 'n' || prop === 'partition') { state.customTags = {}; if (state.tags === 'personalizadas') { state.tags = 'medio'; $('etiquetas').value = 'medio'; } }
        }
        update();
      });
    }
    $('redistribuir').addEventListener('click', () => { state.seed += 1; state.customTags = {}; update(); });
    $('restablecer').addEventListener('click', () => {
      Object.assign(state, { fn: 'cuadrado', n: 8, c: 0.43, partition: 'uniforme', tags: 'medio', display: 'ambos', epsilon: 0.1, seed: 17, customTags: {} });
      $('funcion').value = state.fn; $('particion').value = state.partition; $('visualizacion').value = state.display; $('epsilon').value = String(state.epsilon);
      loadTagOptions(false); update();
    });
    $('grafico-principal').addEventListener('click', ev => {
      const hit = ev.target.closest('[data-interval-index]');
      if (!hit || state.fn === 'dirichlet') return;
      const i = Number(hit.dataset.intervalIndex);
      const svg = $('grafico-principal');
      const pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY;
      const local = pt.matrixTransform(svg.getScreenCTM().inverse());
      const p = partition(state.n, state.partition, state.seed);
      const xi = bounded((local.x - 68) / (960 - 68), p[i], p[i + 1]);
      state.customTags[i] = bounded((xi - p[i]) / (p[i + 1] - p[i]), 0, 1);
      state.tags = 'personalizadas'; $('etiquetas').value = 'personalizadas'; update();
    });
    $('grafico-principal').addEventListener('keydown', ev => {
      const hit = ev.target.closest('[data-interval-index]');
      if (!hit || (ev.key !== 'Enter' && ev.key !== ' ')) return;
      ev.preventDefault();
      const i = Number(hit.dataset.intervalIndex);
      const prev = state.customTags[i] === undefined ? 0.2 : state.customTags[i];
      state.customTags[i] = prev < 0.25 ? 0.5 : prev < 0.55 ? 0.8 : 0.2;
      state.tags = 'personalizadas'; $('etiquetas').value = 'personalizadas';
      update();
      const reHit = document.querySelector(`#grafico-principal [data-interval-index="${i}"]`);
      if (reHit) reHit.focus();
    });
    const convSelect = ev => {
      const svg = $('grafico-convergencia');
      const pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY;
      const local = pt.matrixTransform(svg.getScreenCTM().inverse());
      state.n = bounded(Math.round(2 + ((local.x - 73) / (960 - 73)) * 98), 2, 100);
      state.customTags = {};
      if (state.tags === 'personalizadas') { state.tags = 'medio'; $('etiquetas').value = 'medio'; }
      update();
    };
    $('grafico-convergencia').addEventListener('click', ev => { if (ev.target.id === 'seleccionar-n-en-grafico') convSelect(ev); });
    $('grafico-convergencia').addEventListener('keydown', ev => {
      if (ev.target.id === 'seleccionar-n-en-grafico' && (ev.key === 'ArrowRight' || ev.key === 'ArrowLeft')) {
        ev.preventDefault(); state.n = bounded(state.n + (ev.key === 'ArrowRight' ? 1 : -1), 2, 100); update();
        $('seleccionar-n-en-grafico').focus();
      }
    });
    document.querySelectorAll('[data-n]').forEach(btn => btn.addEventListener('click', () => { state.n = Number(btn.dataset.n); state.customTags = {}; if (state.tags === 'personalizadas') { state.tags = 'medio'; $('etiquetas').value = 'medio'; } update(); }));
    const tabs = Array.from(document.querySelectorAll('[role=tab]'));
    function chooseTab(tab, focus = false) {
      for (const t of tabs) {
        const selected = t === tab;
        t.classList.toggle('active', selected);
        t.setAttribute('aria-selected', String(selected));
        t.tabIndex = selected ? 0 : -1;
        $(t.getAttribute('aria-controls')).hidden = !selected;
      }
      if (focus) tab.focus();
    }
    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => chooseTab(tab));
      tab.addEventListener('keydown', e => {
        const move = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!move && e.key !== 'Home' && e.key !== 'End') return;
        e.preventDefault();
        const next = e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : (i + move + tabs.length) % tabs.length;
        chooseTab(tabs[next], true);
      });
    });
    $('exportar-csv').addEventListener('click', () => {
      const data = seriesData();
      const f = val => val.toFixed(8).replace('.', ',');
      const rows = ['n;L(f,P_n);S(f,P_n,xi);U(f,P_n);U-L', ...data.map(d => `${d.n};${f(d.L)};${f(d.S)};${f(d.U)};${f(d.gap)}`)];
      const blob = new Blob(['\ufeff' + rows.join('\r\n')], { type: 'text/csv;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a'); a.href = url; a.download = `MA-ART-0026-${state.fn}-sumas.csv`;
      document.body.append(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    });
  }
  function initialize() {
    installEvents(); loadTagOptions(false); update();
    // Solo para pruebas automatizadas locales; no realiza solicitudes ni guarda datos.
    if (location.hostname === 'localhost' || location.hostname === '127.0.0.1' || location.protocol === 'file:') {
      window.__MA_lab_test = { state, partition, extrema, sums, exactValue, refinedUnion, seriesData };
    }
  }
  initialize();
})();
