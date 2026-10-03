/** Cola de sesiones: un archivo lógico por envío, sin truncar a 20. GPL-3.0-or-later. */
import { normalizeProgress, HISTORY_LIMIT } from './progress.mjs';

export const OUTBOX_PREFIX = 'ma-practica-outbox-v01:';
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map(key => [key, stable(value[key])]));
  }
  return value;
}
const serialize = value => JSON.stringify(stable(value));

export function makeSubmission(userId, sessionId, record, exerciseRating) {
  if (!UUID.test(userId) || !UUID.test(sessionId)) throw new Error('Identidad o sesión de envío inválida');
  if (!Number.isInteger(exerciseRating) || exerciseRating < 500 || exerciseRating > 2500) {
    throw new Error('Dificultad del envío inválida');
  }
  const clean = structuredClone(record);
  if (!clean || typeof clean !== 'object') throw new Error('Registro de envío inválido');
  delete clean.pendingSync;
  delete clean.syncError;
  clean.clientSessionId = sessionId;
  clean.partial = clean.partial === true;
  clean.delta = null;
  clean.ratingBefore = null;
  clean.ratingAfter = null;
  clean.ratingPolicy = null;
  if (normalizeProgress({ history: [clean] }).history.length !== 1 ||
      !clean.trace.length || (!clean.partial && clean.trace.length !== clean.total) ||
      typeof clean.finishedAt !== 'string' || !Number.isFinite(Date.parse(clean.finishedAt))) {
    throw new Error('Registro incompleto o fecha de envío inválida');
  }
  if (new TextEncoder().encode(serialize(clean)).length > 131072) throw new Error('Sesión demasiado grande');
  return { version: 1, userId, sessionId, exerciseRating, record: clean };
}

function validate(entry) {
  if (entry?.version !== 1) throw new Error('Versión de envío pendiente inválida');
  const safe = makeSubmission(entry.userId, entry.sessionId, entry.record, entry.exerciseRating);
  if (serialize(entry) !== serialize(safe)) throw new Error('Envío pendiente alterado; se conserva sin enviar');
  return safe;
}

export class AccountOutbox {
  constructor(storage) {
    this.storage = storage;
    this.memory = new Map();
    this.persistent = Boolean(storage);
    this.flight = null;
  }

  key(entry) { return OUTBOX_PREFIX + entry.userId + ':' + entry.sessionId; }

  enqueue(entry) {
    const safe = validate(entry);
    const key = this.key(safe);
    const text = serialize(safe);
    let previous = this.memory.get(key);
    try { previous = this.storage?.getItem(key) ?? previous; }
    catch { this.persistent = false; }
    if (previous && previous !== text) throw new Error('Un identificador pendiente no puede cambiar de contenido');
    // Memoria conserva el envío si localStorage está bloqueado o sin espacio.
    this.memory.set(key, text);
    try {
      if (!this.storage) throw new Error('Sin almacenamiento');
      this.storage.setItem(key, text);
      if (this.storage.getItem(key) !== text) throw new Error('Escritura no confirmada');
    } catch { this.persistent = false; }
    return structuredClone(safe);
  }

  list(userId) {
    if (!UUID.test(userId)) throw new Error('Propietario de cola inválido');
    const prefix = OUTBOX_PREFIX + userId + ':';
    const raw = new Map([...this.memory].filter(([key]) => key.startsWith(prefix)));
    try {
      if (this.storage) {
        if (typeof this.storage.key !== 'function' || !Number.isInteger(this.storage.length)) throw new Error('Almacenamiento no enumerable');
        for (let i = 0; i < this.storage.length; i++) {
          const key = this.storage.key(i);
          if (key?.startsWith(prefix)) {
            const text = this.storage.getItem(key);
            if (text !== null) raw.set(key, text);
          }
        }
      }
    } catch { this.persistent = false; }
    const result = [];
    for (const [key, text] of raw) {
      let entry;
      try { entry = validate(JSON.parse(text)); }
      catch { throw new Error('Hay un envío local dañado. No se ha borrado ni enviado'); }
      if (this.key(entry) !== key || entry.userId !== userId) throw new Error('Propietario de envío inconsistente');
      result.push(entry);
    }
    return result.sort((a, b) => a.record.finishedAt.localeCompare(b.record.finishedAt) || a.sessionId.localeCompare(b.sessionId));
  }

  acknowledge(entry) {
    const key = this.key(entry);
    const expected = serialize(entry);
    try {
      const current = this.storage?.getItem(key);
      if (current && current !== expected) throw new Error('El envío cambió durante la confirmación');
      this.storage?.removeItem(key);
      if (this.storage?.getItem(key)) throw new Error('No se pudo confirmar la retirada de la cola');
    } catch (error) {
      this.persistent = false;
      throw error;
    }
    this.memory.delete(key);
  }

  // Una sola descarga de la cola por instancia. Varias pestañas pueden reenviar;
  // la identidad y los recibos del servidor son la garantía definitiva.
  flush(store, userId, onRemote) {
    if (this.flight) return this.flight;
    this.flight = this._flush(store, userId, onRemote).finally(() => { this.flight = null; });
    return this.flight;
  }

  async _flush(store, userId, onRemote) {
    let delivered = 0;
    while (true) {
      const entry = this.list(userId)[0];
      if (!entry) return delivered;
      await store.finalizeSession(entry);
      const remote = await store.load();
      if (remote.identity.userId !== userId) throw new Error('La identidad cambió; no se confirma el envío');
      // Si se pierde la respuesta o falla la lectura posterior, no se retira la
      // entrada: el próximo envío tendrá exactamente el mismo ID y contenido.
      await onRemote(remote);
      this.acknowledge(entry);
      delivered++;
    }
  }
}

export function withPendingSessions(progress, entries) {
  const result = normalizeProgress(progress);
  const confirmed = result.history.filter(record => record.pendingSync !== true);
  const ids = new Set(confirmed.map(record => record.clientSessionId).filter(Boolean));
  const pending = entries.filter(entry => !ids.has(entry.sessionId)).map(entry => ({
    ...structuredClone(entry.record), pendingSync: true
  }));
  result.history = [...pending, ...confirmed].sort((a, b) =>
    String(b.finishedAt ?? '').localeCompare(String(a.finishedAt ?? ''))
  ).slice(0, HISTORY_LIMIT);
  return result;
}
