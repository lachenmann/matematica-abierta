/* Generador de ternas pitagóricas — Matemática Abierta.
 * Incluir una sola vez desde la plantilla web (no dentro del Markdown):
 * <script src="/js/diofanto-triples.js" defer></script>
 * No utiliza dependencias externas ni document.currentScript.
 */
(() => {
  'use strict';

  const selector = '[data-diofanto-widget]';
  const gcd = (a, b) => {
    while (b !== 0) [a, b] = [b, a % b];
    return a;
  };
  const integerInRange = (value, min, max, fallback) => {
    const number = Number(value);
    return Number.isFinite(number) ? Math.min(max, Math.max(min, Math.trunc(number))) : fallback;
  };

  function initialize(root) {
    if (root.dataset.diofantoInitialized === 'true') return;

    const get = (key) => root.querySelector(`[data-${key}]`);
    const pSlider = get('p');
    const qSlider = get('q');
    const outputKeys = ['p-value', 'q-value', 'identity', 'slope', 'point', 'gcd',
      'status', 'polygon', 'right-angle', 'label-a', 'label-b', 'label-c',
      'triangle', 'announcement', 'fallback'];
    if (!pSlider || !qSlider || outputKeys.some((key) => !get(key))) return;

    function update() {
      const p = integerInRange(pSlider.value, 2, 20, 2);
      pSlider.value = String(p);
      qSlider.max = String(p - 1);
      const q = integerInRange(qSlider.value, 1, p - 1, 1);
      qSlider.value = String(q);

      const a = 2 * p * q;
      const b = p * p - q * q;
      const c = p * p + q * q;
      const primitive = gcd(p, q) === 1 && (p - q) % 2 !== 0;
      const tripleGcd = gcd(gcd(a, b), c);
      const setText = (key, value) => { get(key).textContent = String(value); };
      const fraction = (numerator, denominator) => {
        const common = gcd(numerator, denominator);
        return `${numerator / common}/${denominator / common}`;
      };

      setText('p-value', p);
      setText('q-value', q);
      setText('identity', `${a}² + ${b}² = ${c}²`);
      setText('slope', `m = ${fraction(p, q)}`);
      setText('point', `(${fraction(a, c)}, ${fraction(b, c)})`);
      setText('gcd', gcd(p, q));
      setText('status', primitive ? 'Terna primitiva' : `Terna no primitiva (mcd de la terna: ${tripleGcd})`);
      setText('announcement', `Parámetros ${p} y ${q}. Terna ${a}, ${b}, ${c}. ${primitive ? 'Primitiva' : 'No primitiva'}.`);

      const scale = 150 / Math.max(a, b);
      const width = a * scale;
      const height = b * scale;
      const x = (260 - width) / 2;
      const y = 210;
      const marker = Math.min(12, width / 4, height / 4);

      get('polygon').setAttribute('points', `${x},${y} ${x + width},${y} ${x},${y - height}`);
      get('right-angle').setAttribute('points', `${x},${y - marker} ${x + marker},${y - marker} ${x + marker},${y}`);
      get('triangle').setAttribute('aria-label', `Triángulo rectángulo de catetos ${a} y ${b} e hipotenusa ${c}`);

      const position = (key, xx, yy, value) => {
        const node = get(`label-${key}`);
        node.setAttribute('x', String(xx));
        node.setAttribute('y', String(yy));
        node.textContent = String(value);
      };
      position('a', x + width / 2, y + 21, a);
      position('b', x - 17, y - height / 2, b);
      position('c', x + width / 2 + 13, y - height / 2 - 9, c);
    }

    pSlider.addEventListener('input', update);
    qSlider.addEventListener('input', update);
    root.dataset.diofantoInitialized = 'true';
    get('fallback').hidden = true;
    update();
  }

  function initializeAll() {
    document.querySelectorAll(selector).forEach(initialize);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeAll, { once: true });
  } else {
    initializeAll();
  }
  // Los motores SPA pueden reemplazar el contenido Markdown sin recargar el JS.
  ['astro:page-load', 'turbo:load', 'swup:contentReplaced', 'pageshow'].forEach(
    (eventName) => document.addEventListener(eventName, initializeAll)
  );
})();
