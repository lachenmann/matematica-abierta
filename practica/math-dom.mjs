import { toMathText } from './math-tex.mjs';

const authoredTeX = text => /\\\(|\\\[/.test(text);
const fallbackTerm = term => /^-?[\p{L}\p{N}.]+$/u.test(term) ? term : `(${term})`;
const plainFallback = text => text
  .replace(/\\frac\{([^{}]*)\}\{([^{}]*)\}/g, (_, numerator, denominator) =>
    `${fallbackTerm(numerator)}/${fallbackTerm(denominator)}`)
  .replace(/\\mathbb\{R\}/g, 'ℝ')
  .replace(/\\varnothing/g, '∅')
  .replace(/\\infty/g, '∞')
  .replace(/\\ne/g, '≠')
  .replace(/\\pm/g, '±')
  .replace(/\\gcd/g, 'mcd')
  .replace(/\\iff/g, '⇔')
  .replace(/\\(?:left|right)/g, '')
  .replace(/\\\{/g, '{')
  .replace(/\\\}/g, '}')
  .replace(/\^\{([^{}]*)\}/g, '^$1')
  .replace(/\\\(|\\\)|\\\[|\\\]/g, '');

const timeout = (promise, milliseconds) => new Promise((resolve, reject) => {
  const timer = setTimeout(() => reject(new Error(`MathJax no respondió en ${milliseconds} ms.`)), milliseconds);
  Promise.resolve(promise).then(
    value => { clearTimeout(timer); resolve(value); },
    error => { clearTimeout(timer); reject(error); },
  );
});

/** Texto seguro: los delimitadores TeX editoriales se ocultan si MathJax no carga. Sin innerHTML. */
export function setMath(node, source) {
  clearMath(node);
  node.textContent = authoredTeX(source) ? plainFallback(source) : source;
  node.dataset.mathSource = source;
  node.dataset.mathPending = 'true';
  return node;
}

export function mathElement(tag, source, className = '') {
  const node = document.createElement(tag);
  if (className) node.className = className;
  return setMath(node, source);
}

/** Desregistra ecuaciones antes de reemplazar sus nodos (API oficial de MathJax). */
export function clearMath(node) {
  if (typeof window.MathJax?.typesetClear === 'function') window.MathJax.typesetClear([node]);
}

let previous = Promise.resolve();
/** Serializa los renders y evita reescribir un TeX editorial con sustituciones dentro de sus delimitadores. */
export function typesetMath(root, { timeoutMs = 4000 } = {}) {
  const mj = window.MathJax;
  if (typeof mj?.typesetPromise !== 'function') return previous;
  previous = previous.then(async () => {
    if (!root.isConnected) return;
    const nodes = [root, ...root.querySelectorAll('[data-math-pending]')]
      .filter(node => node.dataset?.mathPending === 'true' && node.isConnected);
    if (!nodes.length) return;
    try {
      await timeout(mj.startup.promise, timeoutMs);
      let found = false;
      for (const node of nodes) {
        const source = node.dataset.mathSource;
        // El TeX explícito ya está delimitado. Convertir sus fragmentos de nuevo rompería MathJax.
        const math = authoredTeX(source) ? source : toMathText(source);
        if (math !== node.textContent || authoredTeX(source)) {
          node.textContent = math;
          found = true;
        }
        delete node.dataset.mathPending;
      }
      if (found) await timeout(mj.typesetPromise([root]), timeoutMs);
    } catch (error) {
      if (typeof mj.typesetClear === 'function') mj.typesetClear([root]);
      for (const node of nodes) {
        if (!node.isConnected) continue;
        node.textContent = authoredTeX(node.dataset.mathSource)
          ? plainFallback(node.dataset.mathSource)
          : node.dataset.mathSource;
        node.dataset.mathPending = 'true';
      }
      console.warn('MA-Práctica: no se pudo componer una expresión matemática.', error);
    }
  });
  return previous;
}
