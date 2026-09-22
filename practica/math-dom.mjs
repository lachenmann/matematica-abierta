import { toMathText } from './math-tex.mjs';

const authoredTeX = text => /\\\(|\\\[/.test(text);
const plainFallback = text => text.replace(/\\\(|\\\)|\\\[|\\\]/g, '');

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
export function typesetMath(root) {
  const mj = window.MathJax;
  if (typeof mj?.typesetPromise !== 'function') return previous;
  previous = previous.catch(() => {}).then(async () => {
    await mj.startup.promise;
    if (!root.isConnected) return;
    const nodes = [root, ...root.querySelectorAll('[data-math-pending]')]
      .filter(node => node.dataset?.mathPending === 'true' && node.isConnected);
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
    if (found) await mj.typesetPromise([root]);
  }).catch(error => console.warn('MA-Práctica: no se pudo componer una expresión matemática.', error));
  return previous;
}
