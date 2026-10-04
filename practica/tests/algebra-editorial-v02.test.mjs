import test from 'node:test';
import assert from 'node:assert/strict';
import { ALGEBRA_PILOT } from '../algebra-pilot.mjs';

// Fuente editorial aprobada: MAP-BANK-ALG-LOTE01 v0.2, mismo ID de Drive.
// https://drive.google.com/file/d/1Rdtc6o65pSrDXtyUyRbi45DrT0myMf74/view
const byId = id => {
  const problem = ALGEBRA_PILOT.find(item => item.id === id);
  assert.ok(problem, `Falta el problema ${id}`);
  return problem;
};

test('V0.2 canónica: 008 explicita la convención entera positiva', () => {
  const step = byId('MAP-DEMO-008').steps[0];
  assert.equal(step.question, '¿Cuál es el máximo factor monomial común tomando coeficientes enteros positivos?');
  assert.deepEqual(step.options, [String.raw`\(3\)`, String.raw`\(3x\)`, String.raw`\(x^2\)`]);
  assert.equal(step.correctIndex, 1);
  assert.match(step.explanation, /\\gcd\(6,9\)=3/);
  assert.match(step.explanation, /menor potencia de/);
  assert.match(step.explanation, /reales arbitrarios sin normalización/);
  assert.equal(byId('MAP-DEMO-008').steps[1].correctIndex, 2);
  assert.equal(byId('MAP-DEMO-008').steps[2].correctIndex, 0);
});

test('V0.2 canónica: 014 prueba necesidad y suficiencia sin cambiar distractores', () => {
  const step = byId('MAP-DEMO-014').steps[2];
  assert.deepEqual(step.options, [
    String.raw`\(S=\{3\}\)`, String.raw`\(S=\{-3,3\}\)`, String.raw`\(S=\{-9,9\}\)`
  ]);
  assert.equal(step.correctIndex, 1);
  assert.match(step.explanation, /x\^2=9 \\iff x\^2-9=0 \\iff \(x-3\)\(x\+3\)=0/);
  assert.match(step.explanation, /propiedad del producto nulo/);
  assert.match(step.explanation, /Recíprocamente/);
  assert.match(step.explanation, /no hay otras soluciones reales/);
  assert.equal(byId('MAP-DEMO-014').steps[0].correctIndex, 2);
  assert.equal(byId('MAP-DEMO-014').steps[1].correctIndex, 0);
});

test('Ningún ID, clave o rating cambia al sincronizar la versión editorial', () => {
  assert.deepEqual(ALGEBRA_PILOT.map(item => [item.id, item.provisionalRating, item.steps.map(step => step.correctIndex)]), [
    ['MAP-DEMO-005', 1000, [0, 1, 2, 1]],
    ['MAP-DEMO-006', 900, [1, 0, 2]],
    ['MAP-DEMO-007', 950, [2, 0, 1]],
    ['MAP-DEMO-008', 1050, [1, 2, 0]],
    ['MAP-DEMO-009', 1050, [0, 1, 2]],
    ['MAP-DEMO-010', 1100, [1, 2, 0]],
    ['MAP-DEMO-011', 1100, [2, 0, 1]],
    ['MAP-DEMO-012', 1200, [1, 0, 2, 1]],
    ['MAP-DEMO-013', 1100, [1, 0, 2]],
    ['MAP-DEMO-014', 1050, [2, 0, 1]]
  ]);
});

test('La presentación TeX de todas las fichas conserva delimitadores y llaves agrupadoras', () => {
  for (const item of ALGEBRA_PILOT) {
    for (const step of item.steps) {
      for (const field of [item.prompt, step.question, ...step.options, step.notation, step.explanation]) {
        const starts = [...field.matchAll(/\\\(/g)].length;
        const ends = [...field.matchAll(/\\\)/g)].length;
        assert.equal(starts, ends, `${item.id}: delimitadores desequilibrados: ${field}`);
        for (const match of field.matchAll(/\\\((.*?)\\\)/gs)) {
          let depth = 0;
          const math = match[1];
          for (let i = 0; i < math.length; i++) {
            if (math[i] === '\\' && '{}'.includes(math[i + 1] ?? '')) { i++; continue; }
            if (math[i] === '{') depth++;
            if (math[i] === '}') depth--;
            assert.ok(depth >= 0, `${item.id}: llave sobrante en ${math}`);
          }
          assert.equal(depth, 0, `${item.id}: llave de agrupación abierta en ${math}`);
        }
      }
    }
  }
});
