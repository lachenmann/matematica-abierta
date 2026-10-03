import test from 'node:test';
import assert from 'node:assert/strict';
import { EXERCISES } from '../exercises.mjs';
import { startSession } from '../engine.mjs';
import { startFlow, answerFlow, retryFlow, surrenderFlow, continueFlow, partialFlowSession } from '../attempt-flow.mjs';
import { emptyProgress, finishProgress, auditFirstAttempts } from '../progress.mjs';
import { reviewStep } from '../view-model.mjs';

const fractions = EXERCISES.find(item => item.area === 'aritmetica');
const wrongAt = step => (step.correctIndex + 1) % step.options.length;
function allCorrect(item = fractions) {
  let flow = startFlow(startSession(item, 'challenge'));
  for (const step of item.steps) flow = answerFlow(flow, item, step.correctIndex);
  return flow;
}

test('Respuesta correcta avanza sin botón intermedio y conserva explicación del paso anterior', () => {
  const first = startFlow(startSession(fractions, 'training'));
  const flow = answerFlow(first, fractions, fractions.steps[0].correctIndex);
  assert.equal(flow.status, 'ask');
  assert.equal(flow.session.index, 1);
  assert.equal(flow.session.trace.length, 1);
  assert.equal(flow.session.trace[0].correct, true);
  assert.equal(flow.notice.kind, 'correct');
  assert.equal(flow.notice.explanation, fractions.steps[0].explanation);
  assert.equal(first.session.index, 0);
});

test('Error no avanza ni revela la respuesta; reintentar conserva el fallo inicial', () => {
  let flow = startFlow(startSession(fractions, 'challenge'));
  const wrong = wrongAt(fractions.steps[0]);
  flow = answerFlow(flow, fractions, wrong);
  assert.equal(flow.status, 'wrong');
  assert.equal(flow.session.index, 0);
  assert.equal(flow.session.trace.length, 0);
  assert.equal(flow.notice.expected, undefined);
  assert.throws(() => answerFlow(flow, fractions, fractions.steps[0].correctIndex));
  flow = retryFlow(flow, fractions);
  assert.throws(() => answerFlow(flow, fractions, wrong));
  flow = answerFlow(flow, fractions, fractions.steps[0].correctIndex);
  assert.equal(flow.session.index, 1);
  assert.equal(flow.session.trace[0].chosen, fractions.steps[0].options[wrong]);
  assert.equal(flow.session.trace[0].correct, false);
  assert.equal(flow.session.trace[0].resolved, true);
  assert.equal(flow.session.trace[0].surrendered, false);
  assert.deepEqual(flow.session.trace[0].attempts, [fractions.steps[0].options[wrong], fractions.steps[0].options[fractions.steps[0].correctIndex]]);
  const review = reviewStep(flow.session, fractions, 0);
  review.attempts.push('no altera');
  assert.equal(flow.session.trace[0].attempts.length, 2);
});

test('Rendirse enseña solución antes de continuar y conserva elección fallida', () => {
  const wrong = wrongAt(fractions.steps[0]);
  let flow = answerFlow(startFlow(startSession(fractions)), fractions, wrong);
  flow = surrenderFlow(flow, fractions);
  assert.equal(flow.status, 'solution');
  assert.equal(flow.session.index, 0);
  assert.equal(flow.session.trace.length, 1);
  assert.equal(flow.notice.expected, fractions.steps[0].options[fractions.steps[0].correctIndex]);
  assert.equal(flow.session.trace[0].surrendered, true);
  assert.throws(() => answerFlow(flow, fractions, fractions.steps[0].correctIndex));
  flow = continueFlow(flow, fractions);
  assert.equal(flow.session.index, 1);
  assert.equal(flow.status, 'ask');
});

test('REGRESIÓN: fracciones correctas 6, 3/6 + 2/6 y 5/6 jamás restan Elo', () => {
  const expected = ['6', '3/6 + 2/6', '5/6'];
  assert.deepEqual(fractions.steps.map(step => step.options[step.correctIndex]), expected);
  const flow = allCorrect();
  assert.equal(flow.session.completed, true);
  assert.deepEqual(auditFirstAttempts(flow.session, fractions), {
    firstCorrect: 3, total: 3, wrongOrdinals: [], flawless: true
  });
  const scored = finishProgress(emptyProgress(), flow.session, fractions, 'fecha');
  assert.ok(scored.record.delta >= 0);
  assert.ok(scored.record.ratingAfter >= scored.record.ratingBefore);
  assert.equal(scored.record.correct, 3);
  assert.equal(scored.record.solved, true);
  assert.equal(scored.record.ratingPolicy, 'first-attempt-v03');
});

test('Un fallo inicial resta Elo aun si se resuelve después por reintento', () => {
  let flow = answerFlow(startFlow(startSession(fractions, 'challenge')), fractions, wrongAt(fractions.steps[0]));
  flow = retryFlow(flow, fractions);
  flow = answerFlow(flow, fractions, fractions.steps[0].correctIndex);
  for (const step of fractions.steps.slice(1)) flow = answerFlow(flow, fractions, step.correctIndex);
  assert.equal(flow.session.completed, true);
  assert.deepEqual(auditFirstAttempts(flow.session, fractions).wrongOrdinals, [1]);
  const scored = finishProgress(emptyProgress(), flow.session, fractions, 'fecha');
  assert.ok(scored.record.delta < 0);
  assert.equal(scored.record.correct, fractions.steps.length - 1);
  assert.equal(scored.record.resolved, fractions.steps.length);
  assert.equal(scored.record.solved, false);
  assert.equal(finishProgress(scored.progress, flow.session, fractions, 'fecha-2').record.delta, null);
});

test('Rendirse registra un fallo y muestra resultado sin aprobación ficticia', () => {
  let flow = answerFlow(startFlow(startSession(fractions, 'challenge')), fractions, wrongAt(fractions.steps[0]));
  flow = continueFlow(surrenderFlow(flow, fractions), fractions);
  for (const step of fractions.steps.slice(1)) flow = answerFlow(flow, fractions, step.correctIndex);
  assert.equal(flow.session.completed, true);
  const result = finishProgress(emptyProgress(), flow.session, fractions, 'fecha');
  assert.ok(result.record.delta < 0);
  assert.deepEqual(result.record.wrongOrdinals, [1]);
  assert.equal(result.record.resolved, fractions.steps.length - 1);
});

test('Auditoría impide descontar si la opción correcta fue marcada incorrectamente', () => {
  const perfect = allCorrect();
  const damaged = { ...perfect.session, trace: perfect.session.trace.map((move, index) => index ? move : { ...move, correct: false }) };
  assert.throws(() => auditFirstAttempts(damaged, fractions), /Inconsistencia de corrección/);
  assert.throws(() => finishProgress(emptyProgress(), damaged, fractions, 'fecha'), /no se ha modificado el Elo/);
  const wrongKey = { ...fractions, steps: fractions.steps.map((step, index) => index ? step : { ...step, correctIndex: 0 }) };
  assert.throws(() => finishProgress(emptyProgress(), perfect.session, wrongKey, 'fecha'), /Inconsistencia de corrección/);
});

test('Repetir correctamente no cambia el Elo negativo histórico ni lo muestra como nuevo', () => {
  const perfect = allCorrect();
  const oldProgress = {
    ratings: { aritmetica: 1178 }, ratedIds: [fractions.id],
    history: [{ id: fractions.id, area: fractions.area, title: fractions.title, mode: 'challenge', correct: 2, total: 3, trace: perfect.session.trace, finishedAt: 'anterior', delta: -22, ratingBefore: 1200, ratingAfter: 1178 }]
  };
  const result = finishProgress(oldProgress, perfect.session, fractions, 'hoy');
  assert.equal(result.record.delta, null);
  assert.equal(result.progress.ratings.aritmetica, 1178);
  assert.equal(result.progress.history[1].delta, -22);
  assert.equal(result.record.correct, 3);
  assert.ok(finishProgress(emptyProgress(), perfect.session, fractions, 'hoy').record.delta >= 0);
});

test('Salir tras error conserva intento parcial, sin rendición ni Elo', () => {
  const wrong = wrongAt(fractions.steps[0]);
  const flow = answerFlow(startFlow(startSession(fractions, 'challenge')), fractions, wrong);
  const snapshot = partialFlowSession(flow, fractions);
  assert.equal(snapshot.trace.length, 1);
  assert.equal(snapshot.trace[0].chosen, fractions.steps[0].options[wrong]);
  assert.equal(snapshot.trace[0].resolved, false);
  assert.equal(snapshot.trace[0].surrendered, false);
  assert.equal(flow.session.trace.length, 0);
  assert.equal(partialFlowSession(startFlow(startSession(fractions)), fractions).trace.length, 0);
});

test('No se permiten acciones tras completar o con ejercicio distinto', () => {
  const completed = allCorrect();
  assert.throws(() => answerFlow(completed, fractions, 0));
  assert.throws(() => surrenderFlow(completed, fractions));
  assert.throws(() => answerFlow(startFlow(startSession(fractions)), EXERCISES[1], 0));
});
