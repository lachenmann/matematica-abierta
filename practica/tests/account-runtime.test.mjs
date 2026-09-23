import test from 'node:test';
import assert from 'node:assert/strict';
import { activateAccountSync, resumeAccountSync, finishAccountSession } from '../account-runtime.mjs';

const UID = '00000000-0000-4000-8000-000000000001';
const SID = '00000000-0000-4000-8000-000000000002';
function remoteClientFixture({ hasUser = false } = {}) {
  const calls = [];
  let user = hasUser ? { id: UID, is_anonymous: true, email: null } : null;
  const client = {
    auth: {
      getUser: async () => ({ data: { user }, error: null }),
      signInAnonymously: async () => {
        user = { id: UID, is_anonymous: true, email: null };
        calls.push(['signInAnonymously']);
        return { data: { user }, error: null };
      }
    },
    from(name) {
      const data = name === 'user_ratings' ? [{ area: 'algebra', rating: 1212 }] :
        name === 'rated_exercises' ? [{ exercise_id: 'MAP-DEMO-005' }] : [];
      return { select() {
        const p = Promise.resolve({ data, error: null });
        p.order = () => p; p.limit = () => p; return p;
      }, insert() { throw new Error('No insertar historial separado de Elo'); } };
    },
    async rpc(name, args) {
      calls.push(['rpc', name, args]);
      if (name === 'ma_import_local_progress') return { data: [{ imported_ratings: 1, imported_rated_ids: 0, imported_sessions: 0 }], error: null };
      if (name === 'ma_finish_practice_session') return { data: {
        sessionId: args.p_session_id, replayed: false, ratingApplied: true,
        ratingBefore: 1200, ratingAfter: 1212, delta: 12, historyDeleted: false,
        record: { ...args.p_record, clientSessionId: args.p_session_id,
          delta: 12, ratingBefore: 1200, ratingAfter: 1212, ratingPolicy: 'first-attempt-v03' }
      }, error: null };
      throw new Error('RPC no atómica: ' + name);
    }
  };
  return { client, calls };
}
const item = { id: 'MAP-DEMO-005', title: 'Prueba', area: 'algebra', provisionalRating: 1200,
  steps: [{ question: 'q1', options: ['a','b'], correctIndex: 0 }, { question: 'q2', options: ['c','d'], correctIndex: 1 }] };
const session = { id: item.id, mode: 'challenge', index: 2, completed: true,
  trace: [
    { ordinal: 1, question: 'q1', notation: 'x', explanation: 'e1', correct: true, chosen: 'a', expected: 'a' },
    { ordinal: 2, question: 'q2', notation: 'y', explanation: 'e2', correct: true, chosen: 'd', expected: 'd' }
  ] };

test('activar sincronización crea identidad anónima e importa explícitamente el local', async () => {
  const { client, calls } = remoteClientFixture();
  const result = await activateAccountSync(client, { ratings: { algebra: 1275 }, ratedIds: [], history: [] }, '2026-09-23T00:00:00.000Z');
  assert.equal(result.identity.state, 'anonymous');
  assert.equal(result.progress.ratings.algebra, 1212);
  assert.ok(calls.some(call => call[0] === 'signInAnonymously'));
  assert.equal(calls.find(call => call[1] === 'ma_import_local_progress')[2].p_snapshot.ratings.algebra, 1275);
});
test('reanudar una identidad existente no vuelve a importar progreso local', async () => {
  const { client, calls } = remoteClientFixture({ hasUser: true });
  const result = await resumeAccountSync(client);
  assert.equal(result.identity.userId, UID);
  assert.equal(result.progress.ratings.algebra, 1212);
  assert.equal(calls.some(call => call[1] === 'ma_import_local_progress'), false);
});
test('finalizar usa una sola RPC para Elo e historial y conserva el identificador suministrado', async () => {
  const { client, calls } = remoteClientFixture({ hasUser: true });
  const resumed = await resumeAccountSync(client);
  const result = await finishAccountSession(resumed.store, session, item, '2026-09-23T00:00:00.000Z', SID);
  assert.equal(result.ratingEvent.applied, true);
  assert.equal(result.record.delta, 12);
  assert.equal(result.record.ratingBefore, 1200);
  assert.equal(result.record.ratingAfter, 1212);
  assert.equal(calls.length, 1);
  assert.equal(calls[0][1], 'ma_finish_practice_session');
  assert.equal(calls[0][2].p_session_id, SID);
});
test('el helper rechaza un envío sin identificador estable antes de escribir', async () => {
  const { client, calls } = remoteClientFixture({ hasUser: true });
  const resumed = await resumeAccountSync(client);
  await assert.rejects(finishAccountSession(resumed.store, session, item, '2026-09-23T00:00:00.000Z'), /inválida/);
  assert.equal(calls.length, 0);
});
