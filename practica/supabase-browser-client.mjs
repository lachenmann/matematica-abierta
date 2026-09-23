/** Cliente mínimo para Supabase en MA-Práctica.
 * Sin dependencias externas: Auth + Data API + RPC sobre fetch.
 * Código original GPL-3.0-or-later.
 */

export const ACCOUNT_SESSION_KEY = 'ma-practica-supabase-session-v01';

function normalizeUrl(value) {
  const url = typeof value === 'string' ? value.trim().replace(/\/+$/, '') : '';
  if (!/^https:\/\/[a-z0-9-]+\.supabase\.co$/i.test(url)) {
    throw new Error('URL de Supabase inválida');
  }
  return url;
}

function normalizeKey(value) {
  const key = typeof value === 'string' ? value.trim() : '';
  if (!key) throw new Error('Falta la clave publicable de Supabase');
  return key;
}

function readJson(text) {
  if (!text) return null;
  try { return JSON.parse(text); } catch { return text; }
}

function messageFrom(body, fallback) {
  return body?.message || body?.msg || body?.error_description || body?.error || fallback;
}

export function hasStoredAccountSession(storage) {
  try {
    const raw = storage?.getItem(ACCOUNT_SESSION_KEY);
    if (!raw) return false;
    const session = JSON.parse(raw);
    return typeof session?.access_token === 'string' && typeof session?.refresh_token === 'string';
  } catch {
    return false;
  }
}

class RestQuery {
  constructor(client, table) {
    this.client = client;
    this.table = table;
    this.method = 'GET';
    this.params = new URLSearchParams();
    this.body = undefined;
    this.prefer = undefined;
  }

  select(columns = '*') {
    this.params.set('select', columns);
    return this;
  }

  order(column, { ascending = true } = {}) {
    this.params.set('order', column + '.' + (ascending ? 'asc' : 'desc'));
    return this;
  }

  limit(value) {
    this.params.set('limit', String(value));
    return this;
  }

  insert(row) {
    this.method = 'POST';
    this.body = row;
    this.prefer = 'return=minimal';
    return this;
  }

  delete() {
    this.method = 'DELETE';
    this.prefer = 'return=minimal';
    return this;
  }

  eq(column, value) {
    this.params.set(column, 'eq.' + String(value));
    return this;
  }

  execute() {
    const query = this.params.toString();
    const path = '/rest/v1/' + encodeURIComponent(this.table) + (query ? '?' + query : '');
    return this.client._dataRequest(path, {
      method: this.method,
      body: this.body,
      prefer: this.prefer
    });
  }

  then(resolve, reject) {
    return this.execute().then(resolve, reject);
  }
}

export class BrowserSupabaseClient {
  constructor({ projectUrl, publishableKey, storage = globalThis.localStorage, fetchImpl = globalThis.fetch } = {}) {
    this.projectUrl = normalizeUrl(projectUrl);
    this.publishableKey = normalizeKey(publishableKey);
    this.storage = storage;
    if (typeof fetchImpl !== 'function') throw new Error('fetch no está disponible');
    this.fetchImpl = fetchImpl;

    this.auth = {
      getUser: () => this._getUser(),
      signInAnonymously: options => this._signInAnonymously(options),
      updateUser: attributes => this._updateUser(attributes),
      signOut: () => this._signOut()
    };
  }

  _readSession() {
    try {
      const raw = this.storage?.getItem(ACCOUNT_SESSION_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  }

  _saveSession(payload) {
    const session = {
      access_token: payload.access_token,
      refresh_token: payload.refresh_token,
      expires_at: Number(payload.expires_at) || Math.floor(Date.now() / 1000) + Number(payload.expires_in || 3600),
      user: payload.user ?? null
    };
    if (!session.access_token || !session.refresh_token) throw new Error('Sesión Supabase incompleta');
    try { this.storage?.setItem(ACCOUNT_SESSION_KEY, JSON.stringify(session)); } catch { /* sesión de memoria solamente */ }
    return session;
  }

  _clearSession() {
    try { this.storage?.removeItem(ACCOUNT_SESSION_KEY); } catch { /* sin almacenamiento */ }
  }

  async _raw(path, { method = 'GET', body, token, prefer } = {}) {
    const headers = {
      apikey: this.publishableKey,
      Accept: 'application/json'
    };
    if (token) headers.Authorization = 'Bearer ' + token;
    if (body !== undefined) headers['Content-Type'] = 'application/json';
    if (prefer) headers.Prefer = prefer;

    let response;
    try {
      response = await this.fetchImpl(this.projectUrl + path, {
        method,
        headers,
        body: body === undefined ? undefined : JSON.stringify(body)
      });
    } catch (error) {
      return { ok: false, status: 0, body: null, error: { message: error?.message || 'Error de red' } };
    }

    const text = await response.text();
    const parsed = readJson(text);
    if (!response.ok) {
      return {
        ok: false,
        status: response.status,
        body: parsed,
        error: { message: messageFrom(parsed, 'Solicitud Supabase fallida') }
      };
    }
    return { ok: true, status: response.status, body: parsed, error: null };
  }

  async _refreshSession(session) {
    if (!session?.refresh_token) return null;
    const result = await this._raw('/auth/v1/token?grant_type=refresh_token', {
      method: 'POST',
      body: { refresh_token: session.refresh_token }
    });
    if (!result.ok || !result.body?.access_token) {
      this._clearSession();
      return null;
    }
    return this._saveSession(result.body);
  }

  async _session({ refreshEarly = true } = {}) {
    let session = this._readSession();
    if (!session) return null;
    const now = Math.floor(Date.now() / 1000);
    if (refreshEarly && Number(session.expires_at || 0) <= now + 60) {
      session = await this._refreshSession(session);
    }
    return session;
  }

  async _authorized(path, options = {}) {
    let session = await this._session();
    if (!session) return { data: null, error: { message: 'No hay sesión remota activa' } };

    let result = await this._raw(path, { ...options, token: session.access_token });
    if (!result.ok && result.status === 401) {
      session = await this._refreshSession(session);
      if (session) result = await this._raw(path, { ...options, token: session.access_token });
    }
    if (!result.ok) return { data: null, error: result.error };
    return { data: result.body, error: null };
  }

  async _signInAnonymously(options = undefined) {
    const data = options?.options?.data ?? options?.data ?? {};
    const result = await this._raw('/auth/v1/signup', { method: 'POST', body: { data } });
    if (!result.ok) return { data: null, error: result.error };
    const session = this._saveSession(result.body);
    return { data: { user: result.body.user ?? session.user, session }, error: null };
  }

  async _getUser() {
    const session = await this._session();
    if (!session) return { data: { user: null }, error: null };
    const result = await this._authorized('/auth/v1/user');
    if (result.error) return result;
    if (result.data?.id) {
      const current = this._readSession();
      if (current) {
        current.user = result.data;
        try { this.storage?.setItem(ACCOUNT_SESSION_KEY, JSON.stringify(current)); } catch { /* opcional */ }
      }
    }
    return { data: { user: result.data ?? null }, error: null };
  }

  async _updateUser(attributes) {
    return this._authorized('/auth/v1/user', { method: 'PUT', body: attributes });
  }

  async _signOut() {
    const session = await this._session({ refreshEarly: false });
    if (!session) return { error: null };
    const result = await this._raw('/auth/v1/logout', { method: 'POST', token: session.access_token });
    this._clearSession();
    return { error: result.ok ? null : result.error };
  }

  from(table) {
    if (!/^[a-z_][a-z0-9_]*$/i.test(table)) throw new Error('Tabla inválida');
    return new RestQuery(this, table);
  }

  rpc(name, args = {}) {
    if (!/^[a-z_][a-z0-9_]*$/i.test(name)) {
      return Promise.resolve({ data: null, error: { message: 'RPC inválida' } });
    }
    return this._authorized('/rest/v1/rpc/' + encodeURIComponent(name), {
      method: 'POST',
      body: args
    });
  }

  _dataRequest(path, options) {
    return this._authorized(path, options);
  }
}

export function createBrowserSupabaseClient(config = {}, storage = globalThis.localStorage, fetchImpl = globalThis.fetch) {
  return new BrowserSupabaseClient({
    projectUrl: config.projectUrl,
    publishableKey: config.publishableKey,
    storage,
    fetchImpl
  });
}
