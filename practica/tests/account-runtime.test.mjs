import test from 'node:test';
import assert from 'node:assert/strict';
import { activateAccountSync, resumeAccountSync, finishAccountSession } from '../account-runtime.mjs';

function remoteClientFixture({ hasUser = false } = {}) {
  const calls = [];
  let user = hasUser ? { id: 'u-1', is_anonymous: true, email: null } : null;
  const client = {
    auth: {
      getUser: async () => ({ data: { user }, error: null }),
      signInAnonymously: async () => {
        user = { id: 'u-1', is_anonymous: true, email: null };
        calls.push(['signInAnonymously']);
        return { data: { user }, error: null };
      }
    },
    from(name) {
      if (name === 'user_ratings') {
        return { select: () => Promise.resolve({ data: [{ area: 'algebra', rating: 1212 }], error: null }) };
      }
      if (name === 'rated_exercises') {
        return { select: () => Promise.resolve({ data: [{ exercise_id: 'MAP-DEMO-005' }], error: null }) };
      }
      if (name === 'practice_sessions') {
        return {
          select: () => {
            const p = Promise.resolve({ data: [], error: null });
            p.order = () => p;
            p.limit = () => p;
            return p;
          },
          insert: async row => {
            calls.push(['insert', row]);
            return { data: null, error: null };
          }
        };
      }
      throw new Error('tabla inesperada');
    },
    async rpc(name, args) {
      calls.push(['rpc', name, args]);
      if (name === 'ma_import_local_progress') {
        return { data: [{ imported_ratings: 1, imported_rated_ids: 0, imported_sessions: 0 }], error: null };
      }
      if (name === 'ma_record_rated_exercise') {
        return { data: [{ applied: true, rating_before: 1200, rating_after: 1212, delta: 12 }], error: null };
      }
      throw new Error('rpc inesperada');
    }
  };
  return { client, calls };
}

const item = {
  id: 'MAP-DEMO-005',
  title: 'Prueba',
  area: 'algebra',
  provisionalRating: 1200,
  steps: [
    { question: 'q1', options: ['a', 'b'], correctIndex: 0 },
    { question: 'q2', options: ['c', 'd'], correctIndex: 1 }
  ]
};

const session = {
  id: 'MAP-DEMO-005',
  mode: 'challenge',
  index: 2,
  completed: true,
  trace: [
    {
      ordinal: 1,
      question: 'q1',
      notation: 'x',
      explanation: 'e1',
      correct: true,
      chosen: 'a',
      expected: 'a'
    },
    {
      ordinal: 2,
      question: 'q2',
      notation: 'y',
      explanation: 'e2',
      correct: true,
      chosen: 'd',
      expected: 'd'
    }
  ]
};

test('activar sincronización crea identidad anónima e importa explícitamente el local', async () => {
  const { client, calls } = remoteClientFixture();
  const local = { ratings: { algebra: 1275 }, ratedIds: [], history: [] };
  const result = await activateAccountSync(client, local, '2026-09-23T00:00:00.000Z');

  assert.equal(result.identity.state, 'anonymous');
  assert.equal(result.progress.ratings.algebra, 1212);
  assert.ok(calls.some(call => call[0] === 'signInAnonymously'));
  const imported = calls.find(call => call[0] === 'rpc' && call[1] === 'ma_import_local_progress');
  assert.equal(imported[2].p_snapshot.ratings.algebra, 1275);
});

test('reanudar una identidad existente no vuelve a importar progreso local', async () => {
  const { client, calls } = remoteClientFixture({ hasUser: true });
  const result = await resumeAccountSync(client);
  assert.equal(result.identity.userId, 'u-1');
  assert.equal(result.progress.ratings.algebra, 1212);
  assert.equal(calls.some(call => call[1] === 'ma_import_local_progress'), false);
});

test('finalizar desafío remoto registra Elo del servidor y luego guarda la sesión', async () => {
  const { client, calls } = remoteClientFixture({ hasUser: true });
  const resumed = await resumeAccountSync(client);
  const result = await finishAccountSession(
    resumed.store,
    session,
    item,
    '2026-09-23T00:00:00.000Z'
  );

  assert.equal(result.ratingEvent.applied, true);
  assert.equal(result.record.delta, 12);
  assert.equal(result.record.ratingBefore, 1200);
  assert.equal(result.record.ratingAfter, 1212);
  const insert = calls.find(call => call[0] === 'insert');
  assert.equal(insert[1].payload.delta, 12);
});
