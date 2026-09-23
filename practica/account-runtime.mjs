/** Orquestación del modo sincronizado de MA-Práctica. GPL-3.0-or-later. */
import { buildLocalImportSnapshot } from './account-sync.mjs';
import { getAccountIdentity, startAnonymousAccount } from './account-auth.mjs';
import { createAccountProgressStore } from './account-progress-store.mjs';
import { buildSessionRecord } from './progress.mjs';

export async function activateAccountSync(client, localProgress, createdAt = new Date().toISOString()) {
  let identity = await getAccountIdentity(client);
  const store = createAccountProgressStore(client);
  let imported = null;

  if (identity.state === 'local') {
    identity = await startAnonymousAccount(client);
    imported = await store.importLocal(buildLocalImportSnapshot(localProgress, createdAt));
  }

  const loaded = await store.load();
  return {
    store,
    identity: loaded.identity ?? identity,
    progress: loaded.progress,
    imported
  };
}

export async function resumeAccountSync(client) {
  const identity = await getAccountIdentity(client);
  if (identity.state === 'local') {
    return { store: null, identity, progress: null };
  }
  const store = createAccountProgressStore(client);
  const loaded = await store.load();
  return { store, identity: loaded.identity, progress: loaded.progress };
}

export async function finishAccountSession(store, session, item, finishedAt) {
  if (!store) throw new Error('No hay almacén remoto activo');

  let ratingEvent = {
    applied: false,
    ratingBefore: null,
    ratingAfter: null,
    delta: null
  };

  const baseRecord = buildSessionRecord(session, item, finishedAt);

  if (session.mode === 'challenge') {
    ratingEvent = await store.recordRatedExercise({
      exerciseId: item.id,
      area: item.area,
      exerciseRating: item.provisionalRating,
      outcome: baseRecord.solved ? 1 : 0,
      ratingPolicy: 'first-attempt-v03'
    });
  }

  const record = buildSessionRecord(session, item, finishedAt, ratingEvent);
  await store.saveSession(record);
  const loaded = await store.load();

  return {
    progress: loaded.progress,
    identity: loaded.identity,
    record,
    ratingEvent
  };
}
