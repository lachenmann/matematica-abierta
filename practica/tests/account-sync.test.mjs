import test from 'node:test';
import assert from 'node:assert/strict';
import { buildLocalImportSnapshot, validateImportSnapshot } from '../account-sync.mjs';

test('La importación conserva ratings e IDs sin recalcular Elo', () => {
  const progress = {
    ratings: { algebra: 1288 },
    ratedIds: ['MAP-DEMO-005', 'MAP-DEMO-006'],
    history: []
  };
  const snapshot = buildLocalImportSnapshot(progress, '2026-09-23T00:00:00.000Z');
  assert.deepEqual(snapshot.ratings, { algebra: 1288 });
  assert.deepEqual(snapshot.ratedIds, ['MAP-DEMO-005', 'MAP-DEMO-006']);
  assert.equal(snapshot.createdAt, '2026-09-23T00:00:00.000Z');
  assert.deepEqual(validateImportSnapshot(snapshot).ratings, { algebra: 1288 });
});

test('La importación filtra estructura inválida con las mismas reglas del progreso local', () => {
  const snapshot = validateImportSnapshot({
    version: 1,
    createdAt: 'fecha',
    ratings: { algebra: 99999, calculo: 1300 },
    ratedIds: ['MAP-DEMO-005', 'MAP-DEMO-005', 'invalido'],
    history: []
  });
  assert.deepEqual(snapshot.ratings, { calculo: 1300 });
  assert.deepEqual(snapshot.ratedIds, ['MAP-DEMO-005']);
});

test('Snapshot incompatible se rechaza explícitamente', () => {
  assert.throws(() => validateImportSnapshot({ version: 99 }), /inválido/);
});
