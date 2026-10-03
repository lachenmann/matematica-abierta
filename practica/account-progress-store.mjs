/** Persistencia remota opcional para MA-Accounts v0.1. GPL-3.0-or-later. */
import { HISTORY_LIMIT, normalizeProgress } from './progress.mjs';
import { validateImportSnapshot } from './account-sync.mjs';
import { getAccountIdentity } from './account-auth.mjs';

function unwrap(result, fallback) {
  if (result?.error) throw Object.assign(new Error(result.error.message || String(result.error)), {
    status: result.error.status, code: result.error.code
  });
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

  async identity() { return getAccountIdentity(this.client); }

  async isAvailable() {
    try { return (await this.identity()).state !== 'local'; }
    catch { return false; }
  }

  async load() {
    const identity = await this.identity();
    if (identity.state === 'local') throw new Error('No hay identidad remota activa');
    const ratingsQuery = this.client.from('user_ratings').select('area,rating');
    const ratedQuery = this.client.from('rated_exercises').select('exercise_id');
    const sessionsQuery = this.client.from('practice_sessions')
      .select('payload,created_at').order('created_at', { ascending: false }).limit(HISTORY_LIMIT);
    const [ratingsResult, ratedResult, sessionsResult] = await Promise.all([ratingsQuery, ratedQuery, sessionsQuery]);
    const ratingsRows = unwrap(ratingsResult, 'No se pudieron cargar ratings') ?? [];
    const ratedRows = unwrap(ratedResult, 'No se pudieron cargar ejercicios puntuados') ?? [];
    const sessionRows = unwrap(sessionsResult, 'No se pudo cargar el historial') ?? [];
    if ((await this.identity()).userId !== identity.userId) throw new Error('La identidad cambió durante la carga');
    const ratings = {};
    for (const row of ratingsRows) {
      if (typeof row?.area === 'string' && Number.isInteger(row?.rating)) ratings[row.area] = row.rating;
    }
    return {
      progress: normalizeProgress({ ratings,
        ratedIds: ratedRows.map(row => row?.exercise_id).filter(Boolean),
        history: sessionRows.map(row => row?.payload).filter(Boolean)
      }),
      persistent: true, identity
    };
  }

  /** Única operación de escritura para sesiones nuevas, completas o parciales. */
  async finalizeSession(submission) {
    const identity = await this.identity();
    if (!identity.userId || identity.userId !== submission.userId) {
      throw new Error('El envío pendiente pertenece a otra identidad');
    }
    const result = unwrap(await this.client.rpc('ma_finish_practice_session', {
      p_session_id: submission.sessionId,
      p_record: submission.record,
      p_exercise_rating: submission.exerciseRating
    }, { expectedUserId: submission.userId }), 'No se pudo confirmar la sesión');
    if (!result || result.sessionId !== submission.sessionId ||
        typeof result.replayed !== 'boolean' || typeof result.ratingApplied !== 'boolean' ||
        typeof result.historyDeleted !== 'boolean') throw new Error('Recibo de sesión inválido');
    if (result.ratingApplied) {
      if (![result.ratingBefore, result.ratingAfter, result.delta].every(Number.isInteger) ||
          result.ratingAfter - result.ratingBefore !== result.delta) throw new Error('Recibo Elo inconsistente');
    } else if (result.delta !== null || result.ratingBefore !== null || result.ratingAfter !== null) {
      throw new Error('Una sesión no puntuada recibió un movimiento histórico');
    }
    if (result.historyDeleted) {
      if (result.record !== null || !result.replayed) throw new Error('Recibo de historial borrado inválido');
    } else if (result.record?.clientSessionId !== submission.sessionId ||
               result.record?.id !== submission.record.id ||
               normalizeProgress({ history: [result.record] }).history.length !== 1) {
      throw new Error('El recibo no contiene la sesión esperada');
    }
    return result;
  }

  // Compatibilidad v0.1: no se usa para finalizar sesiones en la interfaz nueva.
  async recordRatedExercise({ exerciseId, area, exerciseRating, outcome, ratingPolicy = 'first-attempt-v03' }) {
    const row = firstRow(unwrap(await this.client.rpc('ma_record_rated_exercise', {
      p_exercise_id: exerciseId, p_area: area, p_exercise_rating: exerciseRating,
      p_outcome: outcome, p_rating_policy: ratingPolicy
    }), 'No se pudo registrar el movimiento Elo'));
    if (!row || typeof row.applied !== 'boolean') throw new Error('Respuesta Elo remota inválida');
    return { applied: row.applied, ratingBefore: row.rating_before ?? null,
      ratingAfter: row.rating_after ?? null, delta: row.delta ?? null };
  }

  async saveSession(record) {
    if (!record || typeof record !== 'object') throw new Error('Registro de sesión inválido');
    const identity = await this.identity();
    if (identity.state === 'local') throw new Error('No hay identidad remota activa');
    unwrap(await this.client.from('practice_sessions').insert({
      user_id: identity.userId, exercise_id: record.id, area: record.area, mode: record.mode,
      payload: record, finished_at: typeof record.finishedAt === 'string' ? record.finishedAt : null
    }), 'No se pudo guardar la sesión');
    return true;
  }

  async importLocal(snapshot) {
    const safe = validateImportSnapshot(snapshot);
    const row = firstRow(unwrap(await this.client.rpc('ma_import_local_progress', { p_snapshot: safe }),
      'No se pudo importar el progreso local'));
    if (!row) throw new Error('Respuesta de importación inválida');
    return { importedRatings: row.imported_ratings ?? 0, importedRatedIds: row.imported_rated_ids ?? 0,
      importedSessions: row.imported_sessions ?? 0 };
  }

  async clearHistory() {
    const identity = await this.identity();
    if (identity.state === 'local') throw new Error('No hay identidad remota activa');
    unwrap(await this.client.from('practice_sessions').delete().eq('user_id', identity.userId),
      'No se pudo borrar el historial remoto');
    return true;
  }
}

export function createAccountProgressStore(client) { return new AccountProgressStore(client); }
