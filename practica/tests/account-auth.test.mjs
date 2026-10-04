import test from 'node:test';
import assert from 'node:assert/strict';
import {
  getAccountIdentity, startAnonymousAccount, linkEmailToAccount, signOutAccount
} from '../account-auth.mjs';

test('Identidad local cuando no existe usuario Supabase', async () => {
  const client = { auth: { getUser: async () => ({ data: { user: null }, error: null }) } };
  assert.deepEqual(await getAccountIdentity(client), { state: 'local', userId: null, email: null });
});

test('Inicio anónimo conserva el user_id retornado por Supabase', async () => {
  const client = {
    auth: {
      signInAnonymously: async () => ({
        data: { user: { id: 'u-1', is_anonymous: true, email: null } },
        error: null
      })
    }
  };
  assert.deepEqual(await startAnonymousAccount(client), { state: 'anonymous', userId: 'u-1', email: null });
});

test('Vincular correo usa updateUser sobre la identidad existente', async () => {
  let attributes;
  const client = {
    auth: {
      updateUser: async value => {
        attributes = value;
        return {
          data: { user: { id: 'u-1', is_anonymous: true, email: value.email } },
          error: null
        };
      }
    }
  };
  const result = await linkEmailToAccount(client, ' alumno@example.org ');
  assert.deepEqual(attributes, { email: 'alumno@example.org' });
  assert.equal(result.userId, 'u-1');
  assert.equal(result.state, 'anonymous-pending-verification');
  await assert.rejects(() => linkEmailToAccount(client, 'mal'), /Correo inválido/);
});

test('Cerrar sesión propaga errores y confirma éxito', async () => {
  const ok = { auth: { signOut: async () => ({ error: null }) } };
  assert.equal(await signOutAccount(ok), true);
  const bad = { auth: { signOut: async () => ({ error: { message: 'falló' } }) } };
  await assert.rejects(() => signOutAccount(bad), /falló/);
});
