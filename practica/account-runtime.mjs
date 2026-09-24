/** Helpers de cuenta; la interfaz usa AccountCoordinator para reintentos durables. GPL-3.0-or-later. */
import { buildLocalImportSnapshot } from './account-sync.mjs';
import { getAccountIdentity, startAnonymousAccount } from './account-auth.mjs';
import { createAccountProgressStore } from './account-progress-store.mjs';
import { buildSessionRecord } from './progress.mjs';
import { makeSubmission } from './account-outbox.mjs';

export async function activateAccountSync(client, localProgress, createdAt = new Date().toISOString()) {
  let identity = await getAccountIdentity(client);
  const store = createAccountProgressStore(client);
  let imported = null;
  if (identity.state === 'local') {
    identity = await startAnonymousAccount(client);
    imported = await store.importLocal(buildLocalImportSnapshot(localProgress, createdAt));
  }
  const loaded = await store.load();
  return { store, identity: loaded.identity ?? identity, progress: loaded.progress, imported };
}

export async function resumeAccountSync(client) {
  const identity = await getAccountIdentity(client);
  if (identity.state === 'local') return { store: null, identity, progress: null };
  const store = createAccountProgressStore(client);
  const loaded = await store.load();
  return { store, identity: loaded.identity, progress: loaded.progress };
}

/** El llamante conserva sessionId y finishedAt entre reintentos. No genera IDs al enviar. */
export async function finishAccountSession(store, session, item, finishedAt, sessionId) {
  if (!store) throw new Error('No hay almacén remoto activo');
  const identity = await store.identity();
  const submission = makeSubmission(identity.userId, sessionId,
    buildSessionRecord(session, item, finishedAt), item.provisionalRating);
  const receipt = await store.finalizeSession(submission);
  const loaded = await store.load();
  return { progress: loaded.progress, identity: loaded.identity, record: receipt.record,
    ratingEvent: { applied: receipt.ratingApplied, ratingBefore: receipt.ratingBefore,
      ratingAfter: receipt.ratingAfter, delta: receipt.delta }, replayed: receipt.replayed };
}
