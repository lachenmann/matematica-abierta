/** Contrato de importación local -> cuenta. No recalcula Elo. GPL-3.0-or-later. */
import { normalizeProgress } from './progress.mjs';

export const ACCOUNT_SYNC_VERSION = 1;

export function buildLocalImportSnapshot(progress, createdAt = new Date().toISOString()) {
  const normalized = normalizeProgress(progress);
  return Object.freeze({
    version: ACCOUNT_SYNC_VERSION,
    createdAt,
    ratings: { ...normalized.ratings },
    ratedIds: [...normalized.ratedIds],
    history: normalized.history.map(record => structuredClone(record))
  });
}

export function validateImportSnapshot(snapshot) {
  if (!snapshot || snapshot.version !== ACCOUNT_SYNC_VERSION || typeof snapshot.createdAt !== 'string') {
    throw new Error('Snapshot de importación inválido');
  }
  const progress = normalizeProgress(snapshot);
  return {
    version: ACCOUNT_SYNC_VERSION,
    createdAt: snapshot.createdAt,
    ratings: progress.ratings,
    ratedIds: progress.ratedIds,
    history: progress.history
  };
}
