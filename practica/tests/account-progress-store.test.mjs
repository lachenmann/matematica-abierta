import test from 'node:test';
import assert from 'node:assert/strict';
import { createAccountProgressStore } from '../account-progress-store.mjs';

function query(result) {
  const promise = Promise.resolve(result);
  promise.select = () => promise;
  promise.order = () => promise;
  promise.limit = () => promise;
  promise.insert = () => promise;
  promise.delete = () => {
    const chain = { eq: async () => result };
    return chain;
  };
  return promise;
}

function clientFixture() {
  const calls = [];
  const client = {
    auth: {
      getUser: async () => ({
        data: { user: { id: 'u-1', is_anonymous: true, email: null } },
        error: null
      })
    },
    from(name) {
      if (name === 'user_ratings') {
        return { select: () => query({ data: [{ area: 'algebra', rating: 1310 }], error: null }) };
      }
      if (name === 'rated_exercises') {
        return { select: () => query({ data: [{ exercise_id: 'MAP-DEMO-005' }], error: null }) };
      }
      if (name === 'practice_sessions') {
        return {
          select: () => query({ data: [{
            payload: {
              id: 'MAP-DEMO-005', title: 'x', area: 'algebra', mode: 'training',
              correct: 1, total: 1, trace: [], finishedAt: '2026-09-23T00:00:00.000Z'
            },
            created_at: '2026-09-23T00:00:00.000Z'
          }], error: null }),
          insert: async row => { calls.push(['insert', row]); return { data: null, error: null }; },
          delete: () => ({ eq: async (...args) => { calls.push(['delete', ...args]); return { data: null, error: null }; } })
        };
      }
      throw new Error('tabla inesperada');
    },
    async rpc(name, args) {
      calls.push(['rpc', name, args]);
      if (name === 'ma_record_rated_exercise') {
        return { data: [{ applied: true, rating_before: 1200, rating_after: 1214, delta: 14 }], error: null };
      }
      if (name === 'ma_import_local_progress') {
        return { data: [{ imported_ratings: 1, imported_rated_ids: 1, imported_sessions: 0 }], error: null };
      }
      throw new Error('rpc inesperada');
    }
  };
  return { client, calls };
}

test('AccountProgressStore reconstruye progreso normalizado desde tablas remotas', async () => {
  const { client } = clientFixture();
  const store = createAccountProgressStore(client);
  const loaded = await store.load();
  assert.equal(store.kind, 'account');
  assert.equal(loaded.persistent, true);
  assert.equal(loaded.identity.state, 'anonymous');
  assert.deepEqual(loaded.progress.ratings, { algebra: 1310 });
  assert.deepEqual(loaded.progress.ratedIds, ['MAP-DEMO-005']);
});

test('El movimiento Elo usa exclusivamente la RPC canónica', async () => {
  const { client, calls } = clientFixture();
  const store = createAccountProgressStore(client);
  const result = await store.recordRatedExercise({
    exerciseId: 'MAP-DEMO-005', area: 'algebra', exerciseRating: 1250, outcome: 1
  });
  assert.deepEqual(result, { applied: true, ratingBefore: 1200, ratingAfter: 1214, delta: 14 });
  assert.equal(calls[0][1], 'ma_record_rated_exercise');
});

test('Importación local usa RPC y no recalcula Elo en el cliente', async () => {
  const { client, calls } = clientFixture();
  const store = createAccountProgressStore(client);
  const result = await store.importLocal({
    version: 1,
    createdAt: '2026-09-23T00:00:00.000Z',
    ratings: { algebra: 1310 },
    ratedIds: ['MAP-DEMO-005'],
    history: []
  });
  assert.deepEqual(result, { importedRatings: 1, importedRatedIds: 1, importedSessions: 0 });
  assert.equal(calls[0][1], 'ma_import_local_progress');
});

test('Sesiones e historial remoto quedan restringidos al usuario activo', async () => {
  const { client, calls } = clientFixture();
  const store = createAccountProgressStore(client);
  const record = {
    id: 'MAP-DEMO-005', area: 'algebra', mode: 'training',
    finishedAt: '2026-09-23T00:00:00.000Z'
  };
  assert.equal(await store.saveSession(record), true);
  assert.equal(calls[0][1].user_id, 'u-1');
  assert.equal(await store.clearHistory(), true);
  assert.deepEqual(calls[1], ['delete', 'user_id', 'u-1']);
});
