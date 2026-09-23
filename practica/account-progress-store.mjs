/** Persistencia remota opcional para MA-Accounts v0.1. GPL-3.0-or-later. */
import { HISTORY_LIMIT, normalizeProgress } from './progress.mjs';
import { validateImportSnapshot } from './account-sync.mjs';
import { getAccountIdentity } from './account-auth.mjs';

function unwrap(result, fallback) {
  if (result?.error) throw new Error(result.error.message || String(result.error));
  if (!result) throw new Error(fallback);
  return result.data;
}

function firstRow(data) {
  if (Array.isArray(data)) return data[0] ?? null;
  return data ?? null;
}

export class AccountProgressStore {
  constructor(client) {
    if (!client?.from || !client?.rpc || !client?.auth) throw new Error('Cliente Supabase inválido');
    this.client = client;
    this.kind = 'account';
  }

  async identity() {
    return getAccountIdentity(this.client);
  }

  async isAvailable() {
    try {
      return (await this.identity()).state !== 'local';
    } catch {
      return false;
    }
  }

  async load() {
    const identity = await this.identity();
    if (identity.state === 'local') throw new Error('No hay identidad remota activa');

    const ratingsQuery = this.client.from('user_ratings').select('area,rating');
    const ratedQuery = this.client.from('rated_exercises').select('exercise_id');
    const sessionsQuery = this.client
      .from('practice_sessions')
      .select('payload,created_at')
      .order('created_at', { ascending: false })
      .limit(HISTORY_LIMIT);

    const [ratingsResult, ratedResult, sessionsResult] = await Promise.all([
      ratingsQuery, ratedQuery, sessionsQuery
    ]);

    const ratingsRows = unwrap(ratingsResult, 'No se pudieron cargar ratings') ?? [];
    const ratedRows = unwrap(ratedResult, 'No se pudieron cargar ejercicios puntuados') ?? [];
    const sessionRows = unwrap(sessionsResult, 'No se pudo cargar el historial') ?? [];

    const ratings = {};
    for (const row of ratingsRows) {
      if (typeof row?.area === 'string' && Number.isInteger(row?.rating)) ratings[row.area] = row.rating;
    }

    const raw = {
      ratings,
      ratedIds: ratedRows.map(row => row?.exercise_id).filter(Boolean),
      history: sessionRows.map(row => row?.payload).filter(Boolean)
    };

    return {
      progress: normalizeProgress(raw),
      persistent: true,
      identity
    };
  }

  async recordRatedExercise({ exerciseId, area, exerciseRating, outcome, ratingPolicy = 'first-attempt-v03' }) {
    const data = unwrap(await this.client.rpc('ma_record_rated_exercise', {
      p_exercise_id: exerciseId,
      p_area: area,
      p_exercise_rating: exerciseRating,
      p_outcome: outcome,
      p_rating_policy: ratingPolicy
    }), 'No se pudo registrar el movimiento Elo');

    const row = firstRow(data);
    if (!row || typeof row.applied !== 'boolean') throw new Error('Respuesta Elo remota inválida');
    return {
      applied: row.applied,
      ratingBefore: row.rating_before ?? null,
      ratingAfter: row.rating_after ?? null,
      delta: row.delta ?? null
    };
  }

  async saveSession(record) {
    if (!record || typeof record !== 'object') throw new Error('Registro de sesión inválido');
    const identity = await this.identity();
    if (identity.state === 'local') throw new Error('No hay identidad remota activa');

    const row = {
      user_id: identity.userId,
      exercise_id: record.id,
      area: record.area,
      mode: record.mode,
      payload: record,
      finished_at: typeof record.finishedAt === 'string' ? record.finishedAt : null
    };

    unwrap(await this.client.from('practice_sessions').insert(row), 'No se pudo guardar la sesión');
    return true;
  }

  async importLocal(snapshot) {
    const safe = validateImportSnapshot(snapshot);
    const data = unwrap(await this.client.rpc('ma_import_local_progress', {
      p_snapshot: safe
    }), 'No se pudo importar el progreso local');

    const row = firstRow(data);
    if (!row) throw new Error('Respuesta de importación inválida');
    return {
      importedRatings: row.imported_ratings ?? 0,
      importedRatedIds: row.imported_rated_ids ?? 0,
      importedSessions: row.imported_sessions ?? 0
    };
  }

  async clearHistory() {
    const identity = await this.identity();
    if (identity.state === 'local') throw new Error('No hay identidad remota activa');
    unwrap(
      await this.client.from('practice_sessions').delete().eq('user_id', identity.userId),
      'No se pudo borrar el historial remoto'
    );
    return true;
  }
}

export function createAccountProgressStore(client) {
  return new AccountProgressStore(client);
}
