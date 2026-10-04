/** Autenticación opcional para MA-Accounts v0.1. GPL-3.0-or-later. */

function fail(error, fallback) {
  if (error) throw new Error(error.message || String(error));
  throw new Error(fallback);
}

function requireClient(client) {
  if (!client?.auth) throw new Error('Cliente Supabase inválido');
  return client;
}

export async function getAccountIdentity(client) {
  requireClient(client);
  const { data, error } = await client.auth.getUser();
  if (error) fail(error, 'No se pudo consultar la identidad');
  const user = data?.user ?? null;
  if (!user) return { state: 'local', userId: null, email: null };
  return {
    state: user.is_anonymous ? 'anonymous' : 'recoverable',
    userId: user.id,
    email: user.email ?? null
  };
}

export async function startAnonymousAccount(client, options = undefined) {
  requireClient(client);
  const { data, error } = await client.auth.signInAnonymously(options);
  if (error) fail(error, 'No se pudo crear la identidad anónima');
  const user = data?.user ?? data?.session?.user ?? null;
  if (!user?.id) throw new Error('Supabase no devolvió un usuario anónimo');
  return {
    state: 'anonymous',
    userId: user.id,
    email: user.email ?? null
  };
}

export async function linkEmailToAccount(client, email) {
  requireClient(client);
  const normalized = typeof email === 'string' ? email.trim() : '';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(normalized)) {
    throw new Error('Correo inválido');
  }
  const { data, error } = await client.auth.updateUser({ email: normalized });
  if (error) fail(error, 'No se pudo vincular el correo');
  const user = data?.user ?? null;
  if (!user?.id) throw new Error('Supabase no devolvió el usuario actualizado');
  return {
    state: user.is_anonymous ? 'anonymous-pending-verification' : 'recoverable',
    userId: user.id,
    email: user.email ?? normalized
  };
}

export async function signOutAccount(client) {
  requireClient(client);
  const { error } = await client.auth.signOut();
  if (error) fail(error, 'No se pudo cerrar la sesión');
  return true;
}
