/** Auth + Data API + RPC para MA-Práctica, sin CDN. GPL-3.0-or-later. */
export const ACCOUNT_SESSION_KEY = 'ma-practica-supabase-session-v01';

function normalizeUrl(value) {
  const url = typeof value === 'string' ? value.trim().replace(/\/+$/, '') : '';
  if (!/^https:\/\/[a-z0-9-]+\.supabase\.co$/i.test(url)) throw new Error('URL de Supabase inválida');
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
    const session = JSON.parse(storage?.getItem(ACCOUNT_SESSION_KEY) || 'null');
    return typeof session?.access_token === 'string' && typeof session?.refresh_token === 'string';
  } catch { return false; }
}
/** Solo selecciona la cola local; NO autentica ni autoriza operaciones remotas. */
export function storedAccountIdentity(storage) {
  try {
    if (!hasStoredAccountSession(storage)) return null;
    const user = JSON.parse(storage.getItem(ACCOUNT_SESSION_KEY)).user;
    if (!user?.id) return null;
    return { userId: user.id, state: user.is_anonymous ? 'anonymous' : 'recoverable', email: user.email ?? null };
  } catch { return null; }
}

class RestQuery {
  constructor(client, table) {
    this.client = client; this.table = table; this.method = 'GET';
    this.params = new URLSearchParams(); this.body = undefined; this.prefer = undefined;
  }
  select(columns = '*') { this.params.set('select', columns); return this; }
  order(column, { ascending = true } = {}) {
    this.params.set('order', column + '.' + (ascending ? 'asc' : 'desc')); return this;
  }
  limit(value) { this.params.set('limit', String(value)); return this; }
  insert(row) { this.method = 'POST'; this.body = row; this.prefer = 'return=minimal'; return this; }
  delete() { this.method = 'DELETE'; this.prefer = 'return=minimal'; return this; }
  eq(column, value) { this.params.set(column, 'eq.' + String(value)); return this; }
  execute() {
    const query = this.params.toString();
    return this.client._dataRequest('/rest/v1/' + encodeURIComponent(this.table) + (query ? '?' + query : ''), {
      method: this.method, body: this.body, prefer: this.prefer
    });
  }
  then(resolve, reject) { return this.execute().then(resolve, reject); }
}

export class BrowserSupabaseClient {
  constructor({ projectUrl, publishableKey, storage = globalThis.localStorage,
    fetchImpl = globalThis.fetch, timeoutMs = 12000 } = {}) {
    this.projectUrl = normalizeUrl(projectUrl);
    this.publishableKey = normalizeKey(publishableKey);
    this.storage = storage;
    if (typeof fetchImpl !== 'function') throw new Error('fetch no está disponible');
    this.fetchImpl = fetchImpl.bind(globalThis);
    if (!Number.isFinite(timeoutMs) || timeoutMs <= 0) throw new Error('Tiempo de espera inválido');
    this.timeoutMs = timeoutMs;
    this.memorySession = null;
    this.refreshFlight = null;
    this.auth = {
      getUser: () => this._getUser(), signInAnonymously: options => this._signInAnonymously(options),
      updateUser: attributes => this._updateUser(attributes), signOut: () => this._signOut()
    };
  }
  _readSession() {
    try {
      if (!this.storage) return this.memorySession;
      const raw = this.storage.getItem(ACCOUNT_SESSION_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch { return this.memorySession; }
  }
  _saveSession(payload) {
    const session = {
      access_token: payload.access_token, refresh_token: payload.refresh_token,
      expires_at: Number(payload.expires_at) || Math.floor(Date.now() / 1000) + Number(payload.expires_in || 3600),
      user: payload.user ?? null
    };
    if (!session.access_token || !session.refresh_token) throw new Error('Sesión Supabase incompleta');
    this.memorySession = session;
    try { this.storage?.setItem(ACCOUNT_SESSION_KEY, JSON.stringify(session)); } catch { /* memoria, no durabilidad */ }
    return session;
  }
  _clearSession() {
    this.memorySession = null;
    try { this.storage?.removeItem(ACCOUNT_SESSION_KEY); } catch { /* sin almacenamiento */ }
  }
  async _raw(path, { method = 'GET', body, token, prefer } = {}) {
    const headers = { apikey: this.publishableKey, Accept: 'application/json' };
    if (token) headers.Authorization = 'Bearer ' + token;
    if (body !== undefined) headers['Content-Type'] = 'application/json';
    if (prefer) headers.Prefer = prefer;
    const abort = new AbortController();
    const timer = setTimeout(() => abort.abort(), this.timeoutMs);
    try {
      const response = await this.fetchImpl(this.projectUrl + path, {
        method, headers, signal: abort.signal, credentials: 'omit',
        body: body === undefined ? undefined : JSON.stringify(body)
      });
      const parsed = readJson(await response.text());
      if (!response.ok) return { ok: false, status: response.status, body: parsed, error: {
        message: messageFrom(parsed, 'Solicitud Supabase fallida'), status: response.status,
        code: parsed?.code ?? parsed?.error_code
      } };
      return { ok: true, status: response.status, body: parsed, error: null };
    } catch (error) {
      return { ok: false, status: 0, body: null, error: {
        message: abort.signal.aborted ? 'La conexión agotó el tiempo de espera' : error?.message || 'Error de red',
        status: 0, code: abort.signal.aborted ? 'TIMEOUT' : 'NETWORK_ERROR'
      } };
    } finally { clearTimeout(timer); }
  }
  _refreshSession(session) {
    if (this.refreshFlight) return this.refreshFlight;
    const refresh = async () => {
      const current = this._readSession();
      if (!current || current.user?.id !== session.user?.id) throw new Error('La identidad cambió durante la renovación');
      // Otra pestaña o petición ya renovó la sesión mientras esperábamos el lock.
      if (current.access_token !== session.access_token) return current;
      const result = await this._raw('/auth/v1/token?grant_type=refresh_token', {
        method: 'POST', body: { refresh_token: current.refresh_token }
      });
      if (!result.ok || !result.body?.access_token) {
        // Un error de red NO equivale a cerrar la cuenta anónima.
        throw Object.assign(new Error(result.error?.message || 'No se pudo renovar la sesión'), result.error);
      }
      if (this._readSession()?.user?.id !== current.user?.id || result.body.user?.id !== current.user?.id) {
        throw new Error('La renovación no corresponde a la identidad activa');
      }
      return this._saveSession(result.body);
    };
    const locks = globalThis.navigator?.locks;
    const operation = locks?.request
      ? locks.request('ma-practica-auth-refresh:' + this.projectUrl, refresh)
      : refresh();
    this.refreshFlight = Promise.resolve(operation).finally(() => { this.refreshFlight = null; });
    return this.refreshFlight;
  }
  async _session({ refreshEarly = true } = {}) {
    const session = this._readSession();
    if (!session) return null;
    if (refreshEarly && Number(session.expires_at || 0) <= Math.floor(Date.now() / 1000) + 60) {
      return this._refreshSession(session);
    }
    return session;
  }
  async _authorized(path, options = {}) {
    try {
      let session = await this._session();
      if (!session) throw new Error('No hay sesión remota activa');
      const checkOwner = () => {
        if (options.expectedUserId && session.user?.id !== options.expectedUserId) {
          throw new Error('El envío pendiente pertenece a otra identidad');
        }
      };
      checkOwner();
      let result = await this._raw(path, { ...options, token: session.access_token });
      if (!result.ok && result.status === 401) {
        session = await this._refreshSession(session);
        checkOwner();
        result = await this._raw(path, { ...options, token: session.access_token });
      }
      return result.ok ? { data: result.body, error: null } : { data: null, error: result.error };
    } catch (error) { return { data: null, error: { message: error.message, status: error.status, code: error.code } }; }
  }
  async _signInAnonymously(options = undefined) {
    const data = options?.options?.data ?? options?.data ?? {};
    const result = await this._raw('/auth/v1/signup', { method: 'POST', body: { data } });
    if (!result.ok) return { data: null, error: result.error };
    const session = this._saveSession(result.body);
    return { data: { user: result.body.user ?? session.user, session }, error: null };
  }
  async _getUser() {
    try {
      if (!await this._session()) return { data: { user: null }, error: null };
      const result = await this._authorized('/auth/v1/user');
      if (result.error) return result;
      const current = this._readSession();
      if (current && result.data?.id === current.user?.id) this._saveSession({ ...current, user: result.data });
      return { data: { user: result.data ?? null }, error: null };
    } catch (error) { return { data: null, error: { message: error.message, code: error.code, status: error.status } }; }
  }
  async _updateUser(attributes) {
    const result = await this._authorized('/auth/v1/user', { method: 'PUT', body: attributes });
    return result.error ? result : { data: { user: result.data ?? null }, error: null };
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
  rpc(name, args = {}, options = {}) {
    if (!/^[a-z_][a-z0-9_]*$/i.test(name)) return Promise.resolve({ data: null, error: { message: 'RPC inválida' } });
    return this._authorized('/rest/v1/rpc/' + encodeURIComponent(name), {
      method: 'POST', body: args, expectedUserId: options.expectedUserId
    });
  }
  _dataRequest(path, options) { return this._authorized(path, options); }
}
export function createBrowserSupabaseClient(config = {}, storage = globalThis.localStorage, fetchImpl = globalThis.fetch) {
  return new BrowserSupabaseClient({ projectUrl: config.projectUrl, publishableKey: config.publishableKey,
    storage, fetchImpl, timeoutMs: config.timeoutMs ?? 12000 });
}
