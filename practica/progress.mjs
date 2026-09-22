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
          typeof move.expected === 'string');
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

/** Función pura: el mismo ejercicio solo puede puntuarse una vez por estado local. */
export function finishProgress(progress, session, item, finishedAt) {
  const outcome = sessionResult(session, item);
  const next = normalizeProgress(progress);
  let delta = null;
  let ratingBefore = null;
  let ratingAfter = null;
  if (session.mode === 'challenge' && !next.ratedIds.includes(item.id)) {
    ratingBefore = next.ratings[item.area] ?? INITIAL_RATING;
    const calculation = eloUpdate(ratingBefore, item.provisionalRating, outcome.flawless ? 1 : 0);
    delta = calculation.delta;
    ratingAfter = calculation.next;
    next.ratings[item.area] = ratingAfter;
    next.ratedIds = [...next.ratedIds, item.id];
  }
  const record = {
    id: item.id, title: item.title, area: item.area, mode: session.mode,
    correct: outcome.correct, total: outcome.total, trace: session.trace,
    finishedAt, delta, ratingBefore, ratingAfter
  };
  next.history = [record, ...next.history].slice(0, HISTORY_LIMIT);
  return { progress: next, record };
}
