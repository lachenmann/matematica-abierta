/** Coordinación opt-in, cola local y reanudación. GPL-3.0-or-later. */
import { AccountOutbox, makeSubmission, withPendingSessions } from './account-outbox.mjs';
import { createAccountProgressStore } from './account-progress-store.mjs';
import { getAccountIdentity, startAnonymousAccount } from './account-auth.mjs';
import { buildLocalImportSnapshot } from './account-sync.mjs';
import { normalizeProgress } from './progress.mjs';
import { storedAccountIdentity, hasStoredAccountSession } from './supabase-browser-client.mjs';

const IMPORT_PREFIX = 'ma-practica-import-pending-v01:';
function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort().map(k => [k, stable(value[k])]));
  return value;
}
function signature(progress) {
  const p = normalizeProgress(progress);
  return JSON.stringify(stable({ ratings: p.ratings, ratedIds: p.ratedIds.slice().sort(),
    history: p.history.map(r => JSON.stringify(stable(r))).sort() }));
}

export class AccountCoordinator {
  constructor({ storage, loadClient, getProgress, acceptProgress, onChange = () => {} }) {
    this.storage = storage;
    this.loadClient = loadClient;
    this.getProgress = getProgress;
    this.acceptProgress = acceptProgress;
    this.onChange = onChange;
    this.outbox = new AccountOutbox(storage);
    this.identity = storedAccountIdentity(storage);
    this.wanted = hasStoredAccountSession(storage);
    this.store = null;
    this.error = null;
    this.confirmed = false;
    this.flight = null;
    this.importSnapshot = null;
  }

  state() {
    let pending = 0;
    let blocked = false;
    let error = this.error;
    try { if (this.identity) pending = this.outbox.list(this.identity.userId).length; }
    catch (failure) { blocked = true; error = failure.message; }
    return { wanted: this.wanted, identity: this.identity, busy: Boolean(this.flight),
      pending, blocked, error, confirmed: this.confirmed, persistent: this.outbox.persistent };
  }
  notify() { this.onChange(this.state()); }
  view(progress = this.getProgress()) {
    return this.identity ? withPendingSessions(progress, this.outbox.list(this.identity.userId)) : progress;
  }
  apply(remote) {
    if (remote.identity.userId !== this.identity.userId) throw new Error('La identidad remota cambió');
    this.acceptProgress(this.view(remote.progress));
  }

  enqueue(record, exerciseRating, sessionId) {
    if (!this.wanted) return false;
    if (!this.identity) throw new Error('No se conoce la identidad remota: no se puede enviar esta sesión');
    this.outbox.enqueue(makeSubmission(this.identity.userId, sessionId, record, exerciseRating));
    this.acceptProgress(this.view());
    this.notify();
    // No esperar a la red para continuar la práctica.
    void this.sync();
    return true;
  }

  sync({ activate = false } = {}) {
    if (this.flight) return this.flight;
    if (!this.wanted && !activate) return Promise.resolve(false);
    this.error = null;
    this.flight = Promise.resolve().then(() => this._sync(activate)).then(() => true).catch(error => {
      this.error = error?.message || 'No se pudo confirmar la sincronización';
      this.confirmed = false;
      return false;
    }).finally(() => {
      this.flight = null;
      this.notify();
      // Una sesión pudo sellarse mientras terminaba la última lectura remota.
      const state = this.state();
      if (!state.error && !state.blocked && state.pending) queueMicrotask(() => { void this.sync(); });
    });
    this.notify();
    return this.flight;
  }

  async _sync(activate) {
    const client = await this.loadClient();
    let identity = await getAccountIdentity(client);
    if (identity.state === 'local') {
      if (this.wanted || !activate) throw new Error('La sesión guardada no está disponible. No se creará otra identidad automáticamente');
      identity = await startAnonymousAccount(client);
      this.identity = identity;
      this.wanted = true;
      this.importSnapshot = buildLocalImportSnapshot(this.getProgress());
      try {
        if (!this.storage) throw new Error('Sin almacenamiento');
        this.storage.setItem(IMPORT_PREFIX + identity.userId, JSON.stringify(this.importSnapshot));
      } catch { this.outbox.persistent = false; }
    } else if (this.identity && this.identity.userId !== identity.userId) {
      throw new Error('La cuenta cambió; los pendientes de la cuenta anterior no se enviarán');
    }
    this.identity = identity;
    this.wanted = true;
    this.store = createAccountProgressStore(client);
    if (!this.importSnapshot) {
      const raw = this.storage?.getItem(IMPORT_PREFIX + identity.userId);
      if (raw) {
        try { this.importSnapshot = JSON.parse(raw); }
        catch { throw new Error('El respaldo de importación está dañado; se conserva sin sobrescribir'); }
      }
    }
    if (this.importSnapshot) {
      try { await this.store.importLocal(this.importSnapshot); }
      catch (error) {
        if (!error.message.includes('remote progress is not empty')) throw error;
        // Respuesta perdida tras importar: reconocer solo la copia exacta, nunca
        // fusionar por suma ratings de dos progresos distintos.
      }
      const imported = await this.store.load();
      if (signature(imported.progress) !== signature(this.importSnapshot)) {
        throw new Error('El remoto no coincide con la importación pendiente; se conserva el respaldo local');
      }
      this.apply(imported);
      this.storage?.removeItem(IMPORT_PREFIX + identity.userId);
      this.importSnapshot = null;
    }
    await this.outbox.flush(this.store, identity.userId, remote => this.apply(remote));
    const loaded = await this.store.load();
    this.apply(loaded);
    this.confirmed = true;
  }

  async clearHistory() {
    const state = this.state();
    if (state.busy || state.pending || state.blocked || !this.store || !state.confirmed) {
      throw new Error('Confirma los envíos pendientes antes de borrar el historial sincronizado');
    }
    await this.store.clearHistory();
    this.apply(await this.store.load());
    this.notify();
  }
}
