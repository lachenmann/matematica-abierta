import test from 'node:test';
import assert from 'node:assert/strict';
import { ALGEBRA_PILOT } from '../algebra-pilot.mjs';
import { EXERCISES } from '../exercises.mjs';
import { validateBank, startSession, eloUpdate } from '../engine.mjs';
import { startFlow, answerFlow } from '../attempt-flow.mjs';
import { emptyProgress, finishProgress } from '../progress.mjs';
import { setMath, typesetMath } from '../math-dom.mjs';

// Oráculo editorial separado de correctIndex para detectar cambios accidentales en las claves.
const KEYS = {
  'MAP-DEMO-005': [0, 1, 2, 1], 'MAP-DEMO-006': [1, 0, 2],
  'MAP-DEMO-007': [2, 0, 1], 'MAP-DEMO-008': [1, 2, 0],
  'MAP-DEMO-009': [0, 1, 2], 'MAP-DEMO-010': [1, 2, 0],
  'MAP-DEMO-011': [2, 0, 1], 'MAP-DEMO-012': [1, 0, 2, 1],
  'MAP-DEMO-013': [1, 0, 2], 'MAP-DEMO-014': [2, 0, 1]
};

test('Banco: diez problemas originales y 14 IDs distintos conservando los cuatro históricos', () => {
  assert.equal(ALGEBRA_PILOT.length, 10);
  assert.equal(EXERCISES.length, 14);
  assert.deepEqual(EXERCISES.slice(0, 4).map(e => e.id), ['MAP-DEMO-001','MAP-DEMO-002','MAP-DEMO-003','MAP-DEMO-004']);
  assert.equal(validateBank(EXERCISES), true);
  assert.deepEqual(ALGEBRA_PILOT.map(e => e.id), Object.keys(KEYS));
  for (const item of ALGEBRA_PILOT) {
    assert.equal(item.area, 'algebra');
    assert.equal(item.steps.length, KEYS[item.id].length);
    assert.deepEqual(item.steps.map(s => s.correctIndex), KEYS[item.id]);
    for (const step of item.steps) {
      assert.equal(new Set(step.options).size, step.options.length, `${item.id}: distractor duplicado`);
      assert.ok(step.explanation.length > 40, `${item.id}: falta justificación`);
      assert.ok(step.notation.length > 0);
      assert.ok(step.options.every(option => option.trim()));
    }
  }
});

test('Los diez problemas completan el flujo con primeros intentos impecables', () => {
  for (const item of ALGEBRA_PILOT) {
    let flow = startFlow(startSession(item, 'challenge'));
    for (const key of KEYS[item.id]) {
      flow = answerFlow(flow, item, key);
      assert.equal(flow.status, 'ask');
    }
    assert.equal(flow.session.completed, true, item.id);
    assert.equal(flow.session.trace.length, item.steps.length);
    assert.ok(flow.session.trace.every(move => move.correct && move.attempts.length === 1), item.id);
  }
});

test('El primer desafío correcto gana Elo; repetir el mismo ID no puntúa', () => {
  const item = ALGEBRA_PILOT[0];
  let flow = startFlow(startSession(item, 'challenge'));
  for (const key of KEYS[item.id]) flow = answerFlow(flow, item, key);
  const completed = { ...flow.session, finishedAt: '2026-09-22T21:00:00.000Z' };
  const first = finishProgress(emptyProgress(), completed, item, completed.finishedAt);
  assert.ok(first.progress.ratings.algebra > 1200);
  assert.ok(first.progress.history[0].delta > 0);
  const again = finishProgress(first.progress, { ...completed, finishedAt: '2026-09-22T21:01:00.000Z' }, item, '2026-09-22T21:01:00.000Z');
  assert.equal(again.progress.ratings.algebra, first.progress.ratings.algebra);
  assert.equal(again.progress.history[0].delta, null);
  assert.ok(eloUpdate(1200, item.provisionalRating, 0).delta < 0);
});

test('Control algebraico independiente de resultados y condiciones de dominio', () => {
  const eq005 = x => (x - 1) / 3 + (x + 2) / 2;
  assert.equal(eq005(4), 4);
  for (const x of [-6, -1, 0, 6]) assert.notEqual(eq005(x), 4);
  for (const x of [-11, 0, 13]) assert.equal(3 * (x + 2) - 3 * x, 6);
  for (const x of [-5, 0, 10]) assert.equal(2 * x + 5 - 2 * (x + 1), 3);
  for (const x of [-3, 0, 1, 5]) {
    assert.equal(3*x*(2*x-3), 6*x*x-9*x);
    assert.equal((x-5)*(x+5), x*x-25);
  }
  assert.deepEqual([-5, 2].map(x => (x-2)*(x+5)), [0, 0]);
  for (const x of [-2, 0, 1.9, 2, 3]) assert.equal(-3*x+6>0, x<2);
  assert.ok(Number.isNaN((3+1)/(3-3)) === false); // La división JS da Infinity: se exige exclusión editorial.
  assert.equal((7+1)/(7-3), 2);
  assert.deepEqual([4+3, 4-3], [7, 1]);
  assert.equal(3**2, 9); assert.equal((-3)**2, 9);
});

test('MathJax representa TeX explícito del nuevo banco sin anidarlo en otra fórmula', async () => {
  const original = globalThis.window;
  let count = 0;
  globalThis.window = { MathJax: { startup: { promise: Promise.resolve() }, typesetClear() {}, async typesetPromise() { count++; } } };
  try {
    const source = ALGEBRA_PILOT[0].prompt;
    const sample = { textContent:'', dataset:{}, isConnected:true };
    const parent = { dataset:{}, isConnected:true, querySelectorAll:() => [sample] };
    setMath(sample, source);
    assert.ok(sample.textContent.includes('frac'));
    await typesetMath(parent);
    assert.equal(sample.textContent, source);
    assert.equal(count, 1);
  } finally { globalThis.window = original; }
});
