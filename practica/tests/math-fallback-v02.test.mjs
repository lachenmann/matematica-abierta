import test from 'node:test';
import assert from 'node:assert/strict';
import { ALGEBRA_PILOT } from '../algebra-pilot.mjs';
import { setMath } from '../math-dom.mjs';

test('La reserva del lote editorial no muestra comandos TeX ante fallo de CDN', () => {
  const previous = globalThis.window;
  globalThis.window = {};
  try {
    for (const problem of ALGEBRA_PILOT) {
      const fields = [problem.prompt];
      for (const step of problem.steps) fields.push(step.question, ...step.options, step.notation, step.explanation);
      for (const source of fields) {
        const node = { textContent: '', dataset: {} };
        setMath(node, source);
        assert.doesNotMatch(node.textContent, /\\[a-zA-Z]+/, `${problem.id}: macro sin traducir en reserva: ${node.textContent}`);
      }
    }
  } finally { globalThis.window = previous; }
});

test('La justificación del factor común y la exhaustividad son legibles sin CDN', () => {
  const previous = globalThis.window;
  globalThis.window = {};
  try {
    const factor = { textContent: '', dataset: {} };
    const roots = { textContent: '', dataset: {} };
    setMath(factor, ALGEBRA_PILOT.find(p => p.id === 'MAP-DEMO-008').steps[0].explanation);
    setMath(roots, ALGEBRA_PILOT.find(p => p.id === 'MAP-DEMO-014').steps[2].explanation);
    assert.match(factor.textContent, /mcd\(6,9\)=3/);
    assert.match(roots.textContent, /x\^2=9 ⇔ x\^2-9=0 ⇔ \(x-3\)\(x\+3\)=0/);
    assert.match(roots.textContent, /ℝ/);
  } finally { globalThis.window = previous; }
});
