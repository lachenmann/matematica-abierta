/** Progreso local de MA-Práctica. Datos experimentales, no fiables entre dispositivos. */
import { AREAS, INITIAL_RATING, eloUpdate, sessionResult } from './engine.mjs';

export const STORAGE_KEY = 'ma-practica-demo-v01';
export const HISTORY_LIMIT = 20;

export function emptyProgress() {
  return { ratings: {}, ratedIds: [], history: [] };
}

/** Aísla y depura datos que vienen de localStorage, sin confiar en su estructura. */
export function normalizeProgress(raw) {
  const result = emptyProgress();
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) return result;
  for (const area of AREAS) {
    const rating = raw.ratings && raw.ratings[area];
    if (Number.isInteger(rating) && rating >= 0 && rating <= 4000) result.ratings[area] = rating;
  }
  if (Array.isArray(raw.ratedIds)) {
    result.ratedIds = [...new Set(raw.ratedIds.filter(id => typeof id === 'string' && /^MAP-DEMO-\d{3}$/.test(id)))];
  }
  if (Array.isArray(raw.history)) {
    result.history = raw.history.filter(record => {
      return record && typeof record === 'object' && /^MAP-DEMO-\d{3}$/.test(record.id) &&
        AREAS.includes(record.area) && ['training', 'challenge'].includes(record.mode) &&
        typeof record.title === 'string' && Number.isInteger(record.total) && record.total > 0 &&
        Number.isInteger(record.correct) && record.correct >= 0 && record.correct <= record.total &&
        Array.isArray(record.trace) && record.trace.length <= record.total &&
        record.trace.every(move => move && Number.isInteger(move.ordinal) &&
          typeof move.notation === 'string' && typeof move.explanation === 'string' &&
          typeof move.correct === 'boolean' && typeof move.chosen === 'string' &&
          typeof move.expected === 'string' &&
          (move.resolved === undefined || typeof move.resolved === 'boolean') &&
          (move.surrendered === undefined || typeof move.surrendered === 'boolean') &&
          (move.attempts === undefined || (Array.isArray(move.attempts) && move.attempts.length > 0 &&
            move.attempts.length <= 64 && move.attempts.every(choice => typeof choice === 'string'))));
    }).slice(0, HISTORY_LIMIT);
  }
  return result;
}

export function loadProgress(storage) {
  try {
    const text = storage.getItem(STORAGE_KEY);
    return { progress: normalizeProgress(text ? JSON.parse(text) : null), persistent: true };
  } catch {
    return { progress: emptyProgress(), persistent: false };
  }
}

export function saveProgress(storage, progress) {
  try {
    storage.setItem(STORAGE_KEY, JSON.stringify(normalizeProgress(progress)));
    return true;
  } catch {
    return false;
  }
}

export function archivePartial(progress, session, item, finishedAt) {
  if (!session || session.completed || !session.trace.length) return progress;
  const record = {
    id: item.id, title: item.title, area: item.area, mode: session.mode,
    correct: session.trace.filter(move => move.correct).length, total: item.steps.length,
    trace: session.trace, finishedAt, partial: true, delta: null
  };
  return { ...progress, history: [record, ...progress.history].slice(0, HISTORY_LIMIT) };
}

/**
 * Auditoría previa a cualquier cambio Elo. Verifica contra la clave del ejercicio
 * que el primer intento, su indicador de acierto y la corrección concuerdan.
 * Ante contradicción, lanza un error en lugar de descontar silenciosamente.
 */
export function auditFirstAttempts(session, item) {
  const result = sessionResult(session, item);
  const wrongOrdinals = [];
  for (const [index, move] of session.trace.entries()) {
    const step = item.steps[index];
    const expected = step.options[step.correctIndex];
    if (move.ordinal !== index + 1 || move.question !== step.question ||
        move.expected !== expected || !step.options.includes(move.chosen) ||
        move.correct !== (move.chosen === expected)) {
      throw new Error(`Inconsistencia de corrección en el paso ${index + 1}: no se ha modificado el Elo`);
    }
    if (Array.isArray(move.attempts)) {
      if (!move.attempts.length || move.attempts[0] !== move.chosen ||
          new Set(move.attempts).size !== move.attempts.length ||
          move.attempts.some(option => !step.options.includes(option)) ||
          (move.resolved === true && move.attempts.at(-1) !== expected) ||
          (move.surrendered === true && (move.resolved === true || move.attempts.includes(expected)))) {
        throw new Error(`Inconsistencia de intentos en el paso ${index + 1}: no se ha modificado el Elo`);
      }
    }
    if (!move.correct) wrongOrdinals.push(index + 1);
  }
  if (result.correct !== result.total - wrongOrdinals.length) throw new Error('Recuento inconsistente: no se ha modificado el Elo');
  return { firstCorrect: result.correct, total: result.total, wrongOrdinals, flawless: wrongOrdinals.length === 0 };
}

/** Política: cualquier respuesta inicial incorrecta cuenta como fallo; reintentar no borra ese dato. */
export function finishProgress(progress, session, item, finishedAt) {
  const audit = auditFirstAttempts(session, item);
  const next = normalizeProgress(progress);
  let delta = null;
  let ratingBefore = null;
  let ratingAfter = null;
  if (session.mode === 'challenge' && !next.ratedIds.includes(item.id)) {
    ratingBefore = next.ratings[item.area] ?? INITIAL_RATING;
    const calculation = eloUpdate(ratingBefore, item.provisionalRating, audit.flawless ? 1 : 0);
    delta = calculation.delta;
    ratingAfter = calculation.next;
    if (audit.flawless && delta < 0) throw new Error('Inconsistencia Elo: éxito con puntuación negativa; no se guardó el resultado');
    next.ratings[item.area] = ratingAfter;
    next.ratedIds = [...next.ratedIds, item.id];
  }
  const record = {
    id: item.id, title: item.title, area: item.area, mode: session.mode,
    correct: audit.firstCorrect, total: audit.total, wrongOrdinals: audit.wrongOrdinals,
    resolved: session.trace.filter(move => move.correct || move.resolved === true).length,
    solved: audit.flawless, trace: session.trace,
    finishedAt, delta, ratingBefore, ratingAfter,
    ratingPolicy: delta === null ? null : 'first-attempt-v03'
  };
  next.history = [record, ...next.history].slice(0, HISTORY_LIMIT);
  return { progress: next, record };
}
