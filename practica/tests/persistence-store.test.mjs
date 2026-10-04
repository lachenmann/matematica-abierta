import test from 'node:test';
import assert from 'node:assert/strict';
import { emptyProgress } from '../progress.mjs';
import { LocalProgressStore, createLocalProgressStore } from '../persistence-store.mjs';

function memoryStorage() {
  const data = new Map();
  return {
    getItem: key => data.get(key) ?? null,
    setItem: (key, value) => data.set(key, value)
  };
}

test('LocalProgressStore conserva el contrato del MVP', () => {
  const store = createLocalProgressStore(memoryStorage());
  assert.equal(store.kind, 'local');
  assert.equal(store.isAvailable(), true);
  assert.deepEqual(store.load().progress, emptyProgress());
  assert.equal(store.save({ ratings: { algebra: 1234 }, ratedIds: [], history: [] }), true);
  assert.equal(store.load().progress.ratings.algebra, 1234);
  assert.equal(store.clear(), true);
  assert.deepEqual(store.load().progress, emptyProgress());
});

test('LocalProgressStore degrada sin lanzar cuando localStorage está bloqueado', () => {
  const blocked = {
    getItem() { throw new Error('bloqueado'); },
    setItem() { throw new Error('bloqueado'); }
  };
  const store = new LocalProgressStore(blocked);
  assert.equal(store.isAvailable(), false);
  assert.equal(store.save(emptyProgress()), false);
  assert.equal(store.clear(), false);
});
