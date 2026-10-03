import test from 'node:test';
import assert from 'node:assert/strict';
import {
  ACCOUNT_SESSION_KEY,
  createBrowserSupabaseClient,
  hasStoredAccountSession
} from '../supabase-browser-client.mjs';

function memoryStorage() {
  const map = new Map();
  return {
    getItem: key => map.has(key) ? map.get(key) : null,
    setItem: (key, value) => map.set(key, String(value)),
    removeItem: key => map.delete(key)
  };
}

function response(status, body = null) {
  return {
    ok: status >= 200 && status < 300,
    status,
    text: async () => body == null ? '' : JSON.stringify(body)
  };
}

test('signInAnonymously guarda una sesión y getUser usa el token activo', async () => {
  const storage = memoryStorage();
  const calls = [];
  const fetchImpl = async (url, options) => {
    calls.push([url, options]);
    if (url.endsWith('/auth/v1/signup')) {
      return response(200, {
        access_token: 'access-1',
        refresh_token: 'refresh-1',
        expires_in: 3600,
        user: { id: 'u-1', is_anonymous: true }
      });
    }
    if (url.endsWith('/auth/v1/user')) {
      assert.equal(options.headers.Authorization, 'Bearer access-1');
      return response(200, { id: 'u-1', is_anonymous: true });
    }
    throw new Error('URL inesperada: ' + url);
  };

  const client = createBrowserSupabaseClient({
    projectUrl: 'https://demo.supabase.co',
    publishableKey: 'sb_publishable_test'
  }, storage, fetchImpl);

  const signed = await client.auth.signInAnonymously();
  assert.equal(signed.data.user.id, 'u-1');
  assert.equal(hasStoredAccountSession(storage), true);

  const current = await client.auth.getUser();
  assert.equal(current.data.user.id, 'u-1');
  assert.equal(calls.length, 2);
});

test('Data API y RPC usan Authorization y construyen filtros canónicos', async () => {
  const storage = memoryStorage();
  storage.setItem(ACCOUNT_SESSION_KEY, JSON.stringify({
    access_token: 'access-2',
    refresh_token: 'refresh-2',
    expires_at: Math.floor(Date.now() / 1000) + 3600,
    user: { id: 'u-2' }
  }));

  const seen = [];
  const fetchImpl = async (url, options) => {
    seen.push([url, options]);
    if (url.includes('/rest/v1/user_ratings')) return response(200, [{ area: 'algebra', rating: 1200 }]);
    if (url.includes('/rest/v1/rpc/ma_record_rated_exercise')) return response(200, [{ applied: false }]);
    throw new Error('URL inesperada: ' + url);
  };

  const client = createBrowserSupabaseClient({
    projectUrl: 'https://demo.supabase.co',
    publishableKey: 'sb_publishable_test'
  }, storage, fetchImpl);

  const ratings = await client.from('user_ratings').select('area,rating').order('area').limit(20);
  assert.equal(ratings.error, null);
  assert.equal(ratings.data[0].rating, 1200);
  assert.match(seen[0][0], /select=area%2Crating/);
  assert.match(seen[0][0], /order=area\.asc/);
  assert.equal(seen[0][1].headers.Authorization, 'Bearer access-2');

  const rpc = await client.rpc('ma_record_rated_exercise', { p_exercise_id: 'MAP-DEMO-005' });
  assert.equal(rpc.data[0].applied, false);
  assert.equal(JSON.parse(seen[1][1].body).p_exercise_id, 'MAP-DEMO-005');
});

test('token vencido se renueva antes de consultar la API', async () => {
  const storage = memoryStorage();
  storage.setItem(ACCOUNT_SESSION_KEY, JSON.stringify({
    access_token: 'old',
    refresh_token: 'refresh-3',
    expires_at: Math.floor(Date.now() / 1000) - 1,
    user: { id: 'u-3' }
  }));

  const fetchImpl = async (url, options) => {
    if (url.includes('/auth/v1/token?grant_type=refresh_token')) {
      return response(200, {
        access_token: 'new',
        refresh_token: 'refresh-4',
        expires_in: 3600,
        user: { id: 'u-3', is_anonymous: true }
      });
    }
    if (url.endsWith('/auth/v1/user')) {
      assert.equal(options.headers.Authorization, 'Bearer new');
      return response(200, { id: 'u-3', is_anonymous: true });
    }
    throw new Error('URL inesperada: ' + url);
  };

  const client = createBrowserSupabaseClient({
    projectUrl: 'https://demo.supabase.co',
    publishableKey: 'sb_publishable_test'
  }, storage, fetchImpl);

  const current = await client.auth.getUser();
  assert.equal(current.data.user.id, 'u-3');
  assert.match(storage.getItem(ACCOUNT_SESSION_KEY), /"access_token":"new"/);
});
