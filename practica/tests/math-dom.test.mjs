import test from 'node:test';
import assert from 'node:assert/strict';
import { setMath, typesetMath, mathElement } from '../math-dom.mjs';

function node() {
  return { textContent: '', dataset: {}, isConnected: true, className: '' };
}
function root(...nodes) {
  return { isConnected: true, dataset: {}, querySelectorAll: () => nodes };
}

test('Sin MathJax externo el enunciado legible se conserva intacto', async () => {
  const previous = globalThis.window;
  globalThis.window = {};
  try {
    const sample = node();
    setMath(sample, 'Calcula 1/2 + 1/3.');
    await typesetMath(root(sample));
    assert.equal(sample.textContent, 'Calcula 1/2 + 1/3.');
    assert.equal(sample.dataset.mathPending, 'true');
  } finally { globalThis.window = previous; }
});

test('El texto de reserva traduce TeX editorial a una expresión comprensible', async () => {
  const previous = globalThis.window;
  globalThis.window = {};
  try {
    const sample = node();
    setMath(sample, String.raw`Resuelve \(\frac{x+1}{x-3}=2\), con \(x\ne3\).`);
    await typesetMath(root(sample));
    assert.equal(sample.textContent, 'Resuelve (x+1)/(x-3)=2, con x≠3.');
  } finally { globalThis.window = previous; }
});

test('Una caída de MathJax restaura el texto de reserva y permite reintentar', async () => {
  const previous = globalThis.window;
  let calls = 0;
  globalThis.window = { MathJax: { startup: { promise: Promise.resolve() },
    typesetClear: () => {}, typesetPromise: async () => { calls++; throw new Error('fallo simulado'); } } };
  try {
    const sample = node();
    setMath(sample, String.raw`\(\frac{x-1}{3}=2\)`);
    const container = root(sample);
    await typesetMath(container);
    assert.equal(sample.textContent, '(x-1)/3=2');
    assert.equal(sample.dataset.mathPending, 'true');
    await typesetMath(container);
    assert.equal(calls, 2);
  } finally { globalThis.window = previous; }
});

test('Una inicialización de MathJax suspendida vence y no bloquea renders posteriores', async () => {
  const previous = globalThis.window;
  globalThis.window = { MathJax: { startup: { promise: new Promise(() => {}) },
    typesetClear: () => {}, typesetPromise: async () => {} } };
  try {
    const sample = node();
    setMath(sample, String.raw`\(x\ne3\)`);
    await typesetMath(root(sample), { timeoutMs: 10 });
    assert.equal(sample.textContent, 'x≠3');
    assert.equal(sample.dataset.mathPending, 'true');
  } finally { globalThis.window = previous; }
});

test('Al cargar MathJax, compone la fórmula de una actualización dinámica una sola vez', async () => {
  const previous = globalThis.window;
  let calls = 0;
  globalThis.window = { MathJax: { startup: { promise: Promise.resolve() },
    typesetPromise: async () => { calls++; }, typesetClear: () => {} } };
  try {
    const sample = node();
    setMath(sample, 'Calcula 1/2 + 1/3.');
    const container = root(sample);
    await typesetMath(container);
    assert.equal(sample.textContent, String.raw`Calcula \(\frac12+\frac13\).`);
    assert.equal(calls, 1);
    await typesetMath(container);
    assert.equal(calls, 1);
  } finally { globalThis.window = previous; }
});

test('La explicación siguiente invalida la ecuación anterior antes de componer', async () => {
  const previous = globalThis.window;
  let cleared = 0;
  let rendered = 0;
  globalThis.window = { MathJax: { startup: { promise: Promise.resolve() },
    typesetClear: () => { cleared++; }, typesetPromise: async () => { rendered++; } } };
  try {
    const sample = node();
    setMath(sample, 'x = −1');
    const container = root(sample);
    await typesetMath(container);
    setMath(sample, 'x = 11');
    await typesetMath(container);
    assert.equal(sample.textContent, String.raw`\(x=11\)`);
    assert.equal(rendered, 2);
    assert.equal(cleared, 2);
    assert.equal(sample.dataset.mathSource, 'x = 11');
  } finally { globalThis.window = previous; }
});

test('Un contenedor retirado no dispara una composición tardía', async () => {
  const previous = globalThis.window;
  let calls = 0;
  globalThis.window = { MathJax: { startup: { promise: Promise.resolve() },
    typesetPromise: async () => { calls++; }, typesetClear: () => {} } };
  try {
    const sample = node();
    setMath(sample, 'n²');
    const container = root(sample);
    container.isConnected = false;
    await typesetMath(container);
    assert.equal(calls, 0);
    assert.equal(sample.textContent, 'n²');
  } finally { globalThis.window = previous; }
});

test('Los nodos de MathJax se crean como texto, nunca como HTML inyectado', () => {
  const previousWindow = globalThis.window;
  const previousDocument = globalThis.document;
  globalThis.window = {};
  globalThis.document = { createElement: () => node() };
  try {
    const element = mathElement('span', '<img src=x onerror=alert(1)> 1/2', 'test');
    assert.equal(element.textContent, '<img src=x onerror=alert(1)> 1/2');
    assert.equal(element.className, 'test');
    assert.equal(element.dataset.mathPending, 'true');
  } finally { globalThis.window = previousWindow; globalThis.document = previousDocument; }
});
