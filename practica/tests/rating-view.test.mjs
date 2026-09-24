import test from 'node:test';
import assert from 'node:assert/strict';
import { EXERCISES } from '../exercises.mjs';
import { startSession, submitAnswer, advance } from '../engine.mjs';
import { emptyProgress, finishProgress, normalizeProgress } from '../progress.mjs';
import { AREA_NAMES, ratingSnapshot, signedDelta } from '../rating-view.mjs';

const item = EXERCISES.find(exercise => exercise.area === 'calculo');
const byArea = (snapshot, area) => snapshot.find(row => row.area === area);
function complete(mode, wrongFirst = false) {
  let session = startSession(item, mode);
  item.steps.forEach((step, index) => {
    const choice = wrongFirst && index === 0 ? (step.correctIndex + 1) % step.options.length : step.correctIndex;
    session = submitAnswer(session, item, choice);
    session = advance(session, item);
  });
  return session;
}

test('Marcador inicial: cuatro áreas independientes y sin variaciones inventadas', () => {
  const rows = ratingSnapshot(emptyProgress());
  assert.equal(rows.length, 4);
  assert.deepEqual(rows.map(row => row.name), Object.values(AREA_NAMES));
  rows.forEach(row => {
    assert.equal(row.current, 1200);
    assert.equal(row.latestDelta, null);
    assert.deepEqual(row.events, []);
  });
  assert.equal(signedDelta(null), '—');
  assert.equal(signedDelta(0), '0');
  assert.equal(signedDelta(11), '+11');
  assert.equal(signedDelta(-11), '-11');
});

test('Un desafío correcto produce un único movimiento con valores verificables', () => {
  const outcome = finishProgress(emptyProgress(), complete('challenge'), item, '2026-09-22T12:00:00Z');
  const row = byArea(ratingSnapshot(outcome.progress), 'calculo');
  assert.equal(row.current, outcome.record.ratingAfter);
  assert.equal(row.latestDelta, outcome.record.delta);
  assert.deepEqual(row.events.map(event => [event.before, event.after, event.delta]), [
    [outcome.record.ratingBefore, outcome.record.ratingAfter, outcome.record.delta]
  ]);
  assert.equal(byArea(ratingSnapshot(outcome.progress), 'aritmetica').current, 1200);
});

test('Entrenamiento y desafío repetido no generan movimientos Elo nuevos', () => {
  const first = finishProgress(emptyProgress(), complete('challenge'), item, '2026-09-22T12:00:00Z');
  const training = finishProgress(first.progress, complete('training'), item, '2026-09-22T12:01:00Z');
  const repeated = finishProgress(training.progress, complete('challenge'), item, '2026-09-22T12:02:00Z');
  assert.equal(repeated.record.delta, null);
  const row = byArea(ratingSnapshot(repeated.progress), 'calculo');
  assert.equal(row.events.length, 1);
  assert.equal(row.current, first.record.ratingAfter);
});

test('Registro cronológico y última variación corresponden al área seleccionada', () => {
  const progress = {
    ratings: { calculo: 1210, algebra: 1190 }, ratedIds: [],
    history: [
      { area: 'calculo', mode: 'challenge', title: 'Segundo', ratingBefore: 1215, ratingAfter: 1210, delta: -5 },
      { area: 'algebra', mode: 'challenge', title: 'Álgebra', ratingBefore: 1200, ratingAfter: 1190, delta: -10 },
      { area: 'calculo', mode: 'challenge', title: 'Primero', ratingBefore: 1200, ratingAfter: 1215, delta: 15 }
    ]
  };
  const rows = ratingSnapshot(progress);
  assert.deepEqual(byArea(rows, 'calculo').events.map(event => event.title), ['Primero', 'Segundo']);
  assert.equal(byArea(rows, 'calculo').latestDelta, -5);
  assert.equal(byArea(rows, 'algebra').latestDelta, -10);
});

test('Registros incompletos, entrenamiento, datos inválidos y discrepancias no falsifican variaciones', () => {
  const progress = { ratings: { calculo: 1250 }, history: [
    { area: 'calculo', mode: 'challenge', title: 'Incompleto', partial: true, ratingBefore: 1200, ratingAfter: 1250, delta: 50 },
    { area: 'calculo', mode: 'training', title: 'Entrenamiento', ratingBefore: 1200, ratingAfter: 1250, delta: 50 },
    { area: 'calculo', mode: 'challenge', title: 'No cuadra', ratingBefore: 1200, ratingAfter: 1250, delta: 12 },
    { area: 'calculo', mode: 'challenge', title: 'Dato defectuoso', ratingBefore: '1200', ratingAfter: 1250, delta: 50 },
    { area: 'calculo', mode: 'challenge', title: 'Válido antiguo', ratingBefore: 1200, ratingAfter: 1210, delta: 10 }
  ] };
  const row = byArea(ratingSnapshot(progress), 'calculo');
  assert.deepEqual(row.events.map(event => event.title), ['Válido antiguo']);
  assert.equal(row.current, 1250);
  assert.equal(row.latestDelta, null);
  assert.equal(ratingSnapshot(normalizeProgress({ratings: {calculo: 'bad'}})).find(r => r.area === 'calculo').current, 1200);
});

test('Consultar el marcador no modifica progreso, intentos ni Elo', () => {
  const first = finishProgress(emptyProgress(), complete('challenge', true), item, '2026-09-22T12:00:00Z');
  const before = structuredClone(first.progress);
  const rows = ratingSnapshot(first.progress);
  rows[2].events[0].title = 'Solo cambia la proyección';
  assert.deepEqual(first.progress, before);
  assert.equal(byArea(ratingSnapshot(first.progress), 'calculo').current, first.record.ratingAfter);
});
