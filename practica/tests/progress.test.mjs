import test from 'node:test';
import assert from 'node:assert/strict';
import { EXERCISES } from '../exercises.mjs';
import { startSession, submitAnswer, advance } from '../engine.mjs';
import {
  STORAGE_KEY, HISTORY_LIMIT, emptyProgress, normalizeProgress, loadProgress,
  saveProgress, archivePartial, finishProgress
} from '../progress.mjs';

const arithmetic = EXERCISES.find(ex => ex.area === 'aritmetica');
const calculus = EXERCISES.find(ex => ex.area === 'calculo');

function storage() {
  const contents = new Map();
  return {
    getItem: key => contents.get(key) ?? null,
    setItem: (key, value) => contents.set(key, value)
  };
}
function solved(item, mode = 'challenge', firstWrong = false) {
  let session = startSession(item, mode);
  for (let i = 0; i < item.steps.length; i++) {
    const correct = item.steps[i].correctIndex;
    const answer = i === 0 && firstWrong ? (correct + 1) % item.steps[i].options.length : correct;
    session = advance(submitAnswer(session, item, answer), item);
  }
  return session;
}

test('La lectura inicial y el borrado devuelven estados independientes y vacíos', () => {
  const disk = storage();
  const first = loadProgress(disk);
  assert.equal(first.persistent, true);
  assert.deepEqual(first.progress, emptyProgress());
  first.progress.ratedIds.push(arithmetic.id);
  assert.deepEqual(emptyProgress().ratedIds, []);
  assert.equal(saveProgress(disk, emptyProgress()), true);
  assert.deepEqual(loadProgress(disk).progress, emptyProgress());
});

test('La carga filtra ratings y registros corruptos y elimina IDs puntuados repetidos', () => {
  const disk = storage();
  disk.setItem(STORAGE_KEY, JSON.stringify({
    ratings: { aritmetica: '9999', calculo: 1220, algebra: -50, geometria: 900 },
    ratedIds: [calculus.id, calculus.id, null, 'otra-cosa'],
    history: [null, { id: 'inventado', trace: [] }]
  }));
  assert.deepEqual(loadProgress(disk).progress, { ratings: { calculo: 1220 }, ratedIds: [calculus.id], history: [] });
  assert.deepEqual(normalizeProgress([]), emptyProgress());
  disk.setItem(STORAGE_KEY, '{mal JSON');
  assert.deepEqual(loadProgress(disk), { progress: emptyProgress(), persistent: false });
});

test('Sin permisos de almacenamiento no se bloquea el entrenamiento', () => {
  const blocked = { getItem() { throw Error('bloqueado'); }, setItem() { throw Error('bloqueado'); } };
  assert.deepEqual(loadProgress(blocked), { progress: emptyProgress(), persistent: false });
  assert.equal(saveProgress(blocked, emptyProgress()), false);
  assert.equal(saveProgress(null, emptyProgress()), false);
});

test('Entrenamiento no puntúa; un desafío correcto suma Elo una sola vez', () => {
  let progress = emptyProgress();
  const training = finishProgress(progress, solved(calculus, 'training'), calculus, 'fecha-1');
  assert.equal(training.record.delta, null);
  assert.deepEqual(training.progress.ratings, {});
  assert.deepEqual(training.progress.ratedIds, []);
  progress = finishProgress(training.progress, solved(calculus), calculus, 'fecha-2').progress;
  assert.equal(progress.ratings.calculo, 1214);
  assert.deepEqual(progress.ratedIds, [calculus.id]);
  const repeated = finishProgress(progress, solved(calculus), calculus, 'fecha-3');
  assert.equal(repeated.record.delta, null);
  assert.equal(repeated.progress.ratings.calculo, 1214);
  assert.equal(repeated.progress.history.length, 3);
  assert.deepEqual(training.progress.ratings, {}); // Las funciones no mutan su entrada.
});

test('Reiniciar la página no permite puntuar otra vez el mismo ejercicio', () => {
  const disk = storage();
  const first = finishProgress(emptyProgress(), solved(calculus), calculus, 'fecha-1');
  assert.equal(saveProgress(disk, first.progress), true);
  const reloaded = loadProgress(disk);
  assert.equal(reloaded.progress.history[0].correct, calculus.steps.length);
  const duplicate = finishProgress(reloaded.progress, solved(calculus), calculus, 'fecha-2');
  assert.equal(duplicate.record.delta, null);
  assert.deepEqual(duplicate.progress.ratedIds, [calculus.id]);
  assert.equal(duplicate.progress.ratings.calculo, 1214);
});

test('Un error en el primer intento produce fallo puntuable, aunque se termine guiado', () => {
  const result = finishProgress(emptyProgress(), solved(calculus, 'challenge', true), calculus, 'fecha-1');
  assert.ok(result.record.delta < 0);
  assert.equal(result.record.correct, calculus.steps.length - 1);
  assert.equal(result.record.trace[0].correct, false);
  assert.equal(result.record.trace[0].expected, 'Regla de la cadena');
});

test('El Elo es independiente entre aritmética y cálculo', () => {
  const first = finishProgress(emptyProgress(), solved(arithmetic), arithmetic, 'fecha-1');
  const second = finishProgress(first.progress, solved(calculus), calculus, 'fecha-2');
  assert.equal(second.progress.ratings.aritmetica, first.progress.ratings.aritmetica);
  assert.equal(second.progress.ratings.calculo, 1214);
  assert.equal(second.progress.ratedIds.length, 2);
});

test('El historial parcial conserva elecciones sin puntuar y se limita a veinte registros', () => {
  let partial = submitAnswer(startSession(calculus, 'challenge'), calculus, 0);
  let progress = archivePartial(emptyProgress(), partial, calculus, 'fecha-0');
  assert.equal(progress.history[0].partial, true);
  assert.equal(progress.history[0].trace[0].chosen, 'Regla del producto');
  assert.equal(progress.history[0].delta, null);
  assert.deepEqual(progress.ratings, {});
  for (let i = 1; i <= HISTORY_LIMIT + 5; i++) {
    progress = archivePartial(progress, partial, calculus, `fecha-${i}`);
  }
  assert.equal(progress.history.length, HISTORY_LIMIT);
  assert.equal(progress.history[0].finishedAt, `fecha-${HISTORY_LIMIT + 5}`);
  assert.equal(archivePartial(progress, startSession(calculus), calculus, 'sin pasos'), progress);
});

test('Después de borrar el almacenamiento desaparecen historial y rating experimental', () => {
  const disk = storage();
  const completed = finishProgress(emptyProgress(), solved(calculus), calculus, 'fecha-1');
  saveProgress(disk, completed.progress);
  assert.equal(loadProgress(disk).progress.history.length, 1);
  saveProgress(disk, emptyProgress());
  assert.deepEqual(loadProgress(disk).progress, emptyProgress());
});
