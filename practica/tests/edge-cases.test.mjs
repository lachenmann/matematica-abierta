import test from 'node:test';
import assert from 'node:assert/strict';
import { EXERCISES } from '../exercises.mjs';
import { validateBank, startSession, submitAnswer, advance, sessionResult, eloUpdate } from '../engine.mjs';

const derivative = EXERCISES.find(ex => ex.area === 'calculo');

function cloneWith(patch) {
  return { ...derivative, id: 'MAP-DEMO-999', ...patch };
}

test('Se rechazan bancos vacíos, IDs mal formados y áreas no reconocidas', () => {
  assert.throws(() => validateBank([]));
  assert.throws(() => validateBank(null));
  assert.throws(() => validateBank([cloneWith({ id: 'MA-PRB-0001' })]));
  assert.throws(() => validateBank([cloneWith({ area: 'geometria' })]));
});

test('Se rechazan niveles, ratings y respuestas correctas fuera de rango', () => {
  assert.throws(() => validateBank([cloneWith({ difficulty: 0 })]));
  assert.throws(() => validateBank([cloneWith({ difficulty: 6 })]));
  assert.throws(() => validateBank([cloneWith({ provisionalRating: 2501 })]));
  assert.throws(() => validateBank([cloneWith({ steps: [{ ...derivative.steps[0], correctIndex: 99 }, derivative.steps[1]] })]));
  assert.throws(() => validateBank([cloneWith({ steps: [derivative.steps[0]] })]));
});

test('Inicio rechaza ejercicio o modalidad inválidos', () => {
  assert.throws(() => startSession(null));
  assert.throws(() => startSession(derivative, 'ranked'));
  assert.equal(startSession(derivative).mode, 'training');
});

test('Una respuesta no admite índices negativos, fraccionarios, NaN o ejercicios distintos', () => {
  const start = startSession(derivative);
  for (const value of [-1, 1.5, NaN, Infinity, derivative.steps[0].options.length]) {
    assert.throws(() => submitAnswer(start, derivative, value));
  }
  assert.throws(() => submitAnswer(start, EXERCISES[0], 0));
  assert.throws(() => advance(start, EXERCISES[0]));
});

test('La traza preserva el estado previo y la primera elección aunque se avance', () => {
  const original = startSession(derivative);
  const answered = submitAnswer(original, derivative, 0);
  assert.equal(original.trace.length, 0);
  assert.equal(answered.trace.length, 1);
  assert.equal(answered.trace[0].chosen, 'Regla del producto');
  assert.equal(answered.trace[0].expected, 'Regla de la cadena');
  const advanced = advance(answered, derivative);
  assert.equal(answered.index, 0);
  assert.equal(advanced.index, 1);
  assert.deepEqual(advanced.trace, answered.trace);
  assert.throws(() => advance(advanced, derivative));
});

test('Los cuatro ejercicios se completan y no aceptan nuevas acciones tras terminar', () => {
  for (const exercise of EXERCISES) {
    let session = startSession(exercise, 'challenge');
    assert.throws(() => sessionResult(session, exercise));
    for (const step of exercise.steps) {
      session = submitAnswer(session, exercise, step.correctIndex);
      session = advance(session, exercise);
    }
    assert.equal(session.completed, true, exercise.id);
    assert.deepEqual(sessionResult(session, exercise), { correct: exercise.steps.length, total: exercise.steps.length, flawless: true });
    assert.throws(() => advance(session, exercise));
    assert.throws(() => submitAnswer(session, exercise, 0));
  }
});

test('Elo es simétrico para ratings iguales y rechaza parámetros inválidos', () => {
  assert.equal(eloUpdate(1200, 1200, 1).delta, 12);
  assert.equal(eloUpdate(1200, 1200, 0).delta, -12);
  for (const invalid of [NaN, Infinity]) assert.throws(() => eloUpdate(invalid, 1200, 1));
  for (const result of [-1, 0.5, 2]) assert.throws(() => eloUpdate(1200, 1200, result));
  assert.throws(() => eloUpdate(1200, 1200, 1, 0));
});

test('Aritmética: la opción de suma equivalente es única', () => {
  const exercise = EXERCISES.find(ex => ex.area === 'aritmetica');
  const fractionValue = expression => expression.split('+').reduce((total, part) => {
    const [numerator, denominator] = part.trim().split('/').map(Number);
    return total + numerator / denominator;
  }, 0);
  const options = exercise.steps[1].options;
  assert.equal(options.filter(option => Math.abs(fractionValue(option) - 5 / 6) < 1e-12).length, 1);
  assert.equal(fractionValue(options[exercise.steps[1].correctIndex]), 5 / 6);
});

test('Álgebra: la solución seleccionada satisface ambos miembros', () => {
  const exercise = EXERCISES.find(ex => ex.area === 'algebra');
  assert.equal(exercise.steps[2].options[exercise.steps[2].correctIndex], 'x = 11');
  const x = 11;
  assert.equal(2 * (x - 3), x + 5);
  assert.notEqual(2 * (-1 - 3), -1 + 5);
  assert.notEqual(2 * (5 - 3), 5 + 5);
});

test('Cálculo: derivada seleccionada coincide con cocientes incrementales de muestra', () => {
  const f = x => (x * x + 1) ** 3;
  const derivativeFormula = x => 6 * x * (x * x + 1) ** 2;
  assert.equal(derivative.steps[3].options[derivative.steps[3].correctIndex], '6x(x² + 1)²');
  for (const x of [-3, -2, -1, 0, 1, 2, 3]) {
    const h = 1e-5;
    const estimate = (f(x + h) - f(x - h)) / (2 * h);
    assert.ok(Math.abs(estimate - derivativeFormula(x)) < 1e-5, `Derivada en x=${x}`);
  }
});

test('Demostración: la contraposición es consistente para enteros positivos y negativos de muestra', () => {
  const exercise = EXERCISES.find(ex => ex.area === 'demostraciones');
  assert.equal(exercise.steps[0].correctIndex, 0);
  for (let n = -100; n <= 100; n++) {
    const even = n % 2 === 0;
    assert.ok(!even || n * n % 2 === 0);
    assert.ok(n * n % 2 !== 1 || n % 2 !== 0);
  }
});
