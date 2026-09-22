import test from 'node:test';
import assert from 'node:assert/strict';
import { EXERCISES } from '../exercises.mjs';
import { startSession, submitAnswer, advance } from '../engine.mjs';
import { emptyProgress, finishProgress } from '../progress.mjs';
import { reviewStep, canAct } from '../view-model.mjs';

const calculus = EXERCISES.find(ex => ex.area === 'calculo');
function answerStep(session, choice) {
  return submitAnswer(session, calculus, choice);
}

test('No se consulta un paso futuro ni uno aún no respondido', () => {
  const session = startSession(calculus);
  for (const index of [-1, 0, 1, NaN, 0.5, '0']) assert.throws(() => reviewStep(session, calculus, index));
  const answered = answerStep(session, 0);
  assert.throws(() => reviewStep(answered, calculus, 1));
  assert.throws(() => reviewStep(answered, EXERCISES[0], 0));
});

test('La consulta reproduce la elección equivocada, la corrección y la justificación', () => {
  const session = answerStep(startSession(calculus, 'challenge'), 0);
  const reviewed = reviewStep(session, calculus, 0);
  assert.deepEqual(reviewed, {
    ordinal: 1,
    question: calculus.steps[0].question,
    notation: calculus.steps[0].notation,
    chosen: 'Regla del producto',
    expected: 'Regla de la cadena',
    correct: false,
    explanation: calculus.steps[0].explanation
  });
});

test('Consultas repetidas no mutan la sesión original', () => {
  let session = answerStep(startSession(calculus), 0);
  session = advance(session, calculus);
  session = answerStep(session, calculus.steps[1].correctIndex);
  const before = structuredClone(session);
  for (const index of [0, 1, 0, 1]) reviewStep(session, calculus, index);
  assert.deepEqual(session, before);
  assert.equal(session.trace[0].chosen, 'Regla del producto');
  assert.equal(session.index, 1);
});

test('Proyección no comparte objetos con la traza y no permite reescribir el primer intento', () => {
  const session = answerStep(startSession(calculus), 0);
  const reviewed = reviewStep(session, calculus, 0);
  reviewed.chosen = 'Alteración local';
  assert.equal(session.trace[0].chosen, 'Regla del producto');
  assert.throws(() => answerStep(session, 1));
});

test('La consulta bloquea el envío y el avance hasta volver al paso actual', () => {
  let session = startSession(calculus);
  assert.equal(canAct(session, null), true);
  session = answerStep(session, 0);
  assert.equal(canAct(session, 0), false);
  assert.equal(canAct(session, null), true);
  session = advance(session, calculus);
  assert.equal(canAct(session, 0), false);
  assert.equal(canAct(session, null), true);
});

test('El paso revisado conserva su explicación al completar el ejercicio', () => {
  let session = startSession(calculus, 'training');
  for (const step of calculus.steps) {
    session = answerStep(session, step.correctIndex);
    session = advance(session, calculus);
  }
  assert.equal(session.completed, true);
  assert.equal(canAct(session, null), false);
  assert.equal(canAct(session, 0), false);
  assert.equal(reviewStep(session, calculus, 0).explanation, calculus.steps[0].explanation);
  assert.throws(() => reviewStep(session, calculus, session.trace.length));
});

test('Revisar la planilla no cambia Elo ni datos del progreso ya puntuado', () => {
  let session = startSession(calculus, 'challenge');
  for (const step of calculus.steps) {
    session = answerStep(session, step.correctIndex);
    session = advance(session, calculus);
  }
  const result = finishProgress(emptyProgress(), session, calculus, '2026-09-22T00:00:00Z');
  const before = structuredClone(result.progress);
  for (let i = 0; i < session.trace.length; i++) reviewStep(session, calculus, i);
  assert.deepEqual(result.progress, before);
  const repeated = finishProgress(result.progress, session, calculus, '2026-09-22T00:00:01Z');
  assert.equal(repeated.record.delta, null);
  assert.equal(repeated.progress.ratings.calculo, result.progress.ratings.calculo);
});

test('La traza inconsistente se rechaza al inspeccionar', () => {
  const session = answerStep(startSession(calculus), 0);
  const damaged = {...session, trace: [{...session.trace[0],ordinal:3}]};
  assert.throws(() => reviewStep(damaged, calculus, 0));
});
