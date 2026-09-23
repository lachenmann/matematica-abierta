// SPDX-License-Identifier: GPL-3.0-or-later
import test from 'node:test';
import assert from 'node:assert/strict';
import { createBrowserSupabaseClient } from '../supabase-browser-client.mjs';

const config = {
  projectUrl: 'https://ma-fetch-regression.supabase.co',
  publishableKey: 'sb_publishable_fixture'
};
const response = body => ({ ok: true, status: 200, text: async () => JSON.stringify(body) });
const session = () => ({
  access_token: 'fixture-access', refresh_token: 'fixture-refresh', expires_in: 3600,
  user: { id: '00000000-0000-4000-8000-000000000001', is_anonymous: true }
});
function memoryStorage() {
  const values = new Map();
  return {
    getItem: key => values.get(key) ?? null,
    setItem: (key, value) => values.set(key, value),
    removeItem: key => values.delete(key)
  };
}

test('Fetch conserva globalThis como receptor en Auth, Data API y RPC', async () => {
  const calls = [];
  // No usar una arrow: ocultaría el fallo de receptor del fetch nativo de Window.
  async function fetchImpl(url, options) {
    assert.equal(this, globalThis, 'fetch no debe recibir el cliente como this');
    calls.push([url, options]);
    if (url.endsWith('/auth/v1/signup')) return response(session());
    if (url.endsWith('/auth/v1/user')) return response(session().user);
    if (url.includes('/rest/v1/user_ratings?')) return response([]);
    if (url.endsWith('/rest/v1/rpc/ma_import_local_progress')) return response([{ imported_ratings: 0 }]);
    throw new Error('Solicitud inesperada');
  }
  const client = createBrowserSupabaseClient(config, memoryStorage(), fetchImpl);
  assert.equal(calls.length, 0, 'Construir el cliente no debe iniciar tráfico');
  assert.equal((await client.auth.signInAnonymously()).error, null);
  assert.equal((await client.auth.getUser()).error, null);
  assert.equal((await client.from('user_ratings').select('area,rating')).error, null);
  assert.equal((await client.rpc('ma_import_local_progress', { p_snapshot: {} })).error, null);
  assert.equal(calls.length, 4);
  assert.equal(calls[0][1].headers.Authorization, undefined);
  assert.equal(calls[3][1].headers.Authorization, 'Bearer fixture-access');
});

test('Una implementación fetch ya enlazada conserva su receptor propio', async () => {
  const owner = {};
  let count = 0;
  async function customFetch() {
    assert.equal(this, owner);
    count += 1;
    return response(session());
  }
  const client = createBrowserSupabaseClient(config, memoryStorage(), customFetch.bind(owner));
  assert.equal((await client.auth.signInAnonymously()).error, null);
  assert.equal(count, 1);
});
