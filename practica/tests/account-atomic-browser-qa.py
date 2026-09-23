"""QA de entrega atómica en navegador real; API controlada, sin usuarios Supabase reales.
No se sustituye window.fetch. El SQL transaccional se prueba por separado.
"""
# SPDX-License-Identifier: GPL-3.0-or-later
import copy
import json
import math
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import expect, sync_playwright

BASE = 'http://127.0.0.1:8765/practica/index.html'
HOST = 'ma-atomic-fixture.supabase.co'
KEY = 'ma-practica-demo-v01'
AUTH = 'ma-practica-supabase-session-v01'
USER = {'id': '00000000-0000-4000-8000-000000000001', 'is_anonymous': True, 'email': None}
OUT = Path('practica/browser-qa-artifacts')


class Backend:
    def __init__(self, context):
        self.signups = 0
        self.imports = 0
        self.attempts = 0
        self.replays = 0
        self.imported = False
        self.ratings = {}
        self.rated = {}
        self.sessions = []
        self.receipts = {}
        self.fail = None
        self.reject_auth = False
        self.lose_import = False
        self.unexpected = []
        context.route('**/*', self.route)

    def reply(self, route, body, status=200):
        route.fulfill(status=status, content_type='application/json', body=json.dumps(body), headers={
            'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'apikey,authorization,content-type,prefer',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'})

    def route(self, route):
        request = route.request
        u = urlparse(request.url)
        if u.hostname == '127.0.0.1':
            if u.path.endswith('/supabase-config.local.mjs'):
                route.fulfill(content_type='application/javascript', body=(
                    f'export const projectUrl="https://{HOST}"; export const publishableKey="sb_publishable_fixture";'))
            else:
                route.continue_()
            return
        if u.hostname != HOST:
            self.unexpected.append(request.url)
            route.abort()
            return
        if request.method == 'OPTIONS':
            self.reply(route, {})
            return
        if u.path.startswith('/auth/v1/') and self.reject_auth:
            self.reply(route, {'message': 'Auth offline fixture'}, 503)
            return
        if u.path == '/auth/v1/signup':
            self.signups += 1
            self.reply(route, {'access_token': 'fixture-access', 'refresh_token': 'fixture-refresh', 'expires_in': 3600, 'user': USER})
            return
        if u.path == '/auth/v1/token':
            self.reply(route, {'access_token': 'fixture-renewed', 'refresh_token': 'fixture-renewed-refresh', 'expires_in': 3600, 'user': USER})
            return
        if request.headers.get('authorization') not in ('Bearer fixture-access', 'Bearer fixture-renewed'):
            self.reply(route, {'message': 'Wrong fixture token'}, 401)
            return
        if u.path == '/auth/v1/user':
            self.reply(route, USER)
        elif u.path == '/rest/v1/rpc/ma_import_local_progress':
            if self.imported:
                self.reply(route, {'message': 'remote progress is not empty'}, 400)
                return
            self.imports += 1
            self.imported = True
            snap = request.post_data_json['p_snapshot']
            self.ratings = copy.deepcopy(snap['ratings'])
            self.rated = {eid: None for eid in snap['ratedIds']}
            self.sessions = [{'payload': r, 'created_at': r['finishedAt']} for r in snap['history']]
            if self.lose_import:
                self.lose_import = False
                route.abort()
            else:
                self.reply(route, [{'imported_ratings': len(self.ratings), 'imported_rated_ids': len(self.rated), 'imported_sessions': len(self.sessions)}])
        elif u.path == '/rest/v1/user_ratings':
            self.reply(route, [{'area': a, 'rating': r} for a, r in self.ratings.items()])
        elif u.path == '/rest/v1/rated_exercises':
            self.reply(route, [{'exercise_id': eid} for eid in self.rated])
        elif u.path == '/rest/v1/practice_sessions' and request.method == 'GET':
            self.reply(route, self.sessions[:20])
        elif u.path == '/rest/v1/rpc/ma_finish_practice_session':
            self.attempts += 1
            if self.fail in ('before', 'replay-blocked'):
                self.reply(route, {'message': 'Finalization offline fixture'}, 503)
                return
            body = request.post_data_json
            sid = body['p_session_id']
            fingerprint = json.dumps(body, sort_keys=True)
            if sid in self.receipts:
                saved_hash, result = self.receipts[sid]
                assert saved_hash == fingerprint, 'El cliente cambió el cuerpo de un reintento'
                result = {**result, 'replayed': True}
                self.replays += 1
            else:
                record = copy.deepcopy(body['p_record'])
                applied = record['mode'] == 'challenge' and not record['partial'] and record['id'] not in self.rated
                before = after = delta = None
                if applied:
                    before = self.ratings.get(record['area'], 1200)
                    expected = 1 / (1 + 10 ** ((body['p_exercise_rating'] - before) / 400))
                    outcome = int(record['correct'] == record['total'])
                    delta = math.floor(24 * (outcome - expected) + .5)
                    after = before + delta
                    self.ratings[record['area']] = after
                    self.rated[record['id']] = delta
                record.update(clientSessionId=sid, delta=delta, ratingBefore=before, ratingAfter=after,
                              ratingPolicy='first-attempt-v03' if applied else None)
                self.sessions.insert(0, {'payload': record, 'created_at': record['finishedAt']})
                result = {'sessionId': sid, 'replayed': False, 'ratingApplied': applied, 'ratingBefore': before,
                          'ratingAfter': after, 'delta': delta, 'record': record, 'historyDeleted': False}
                self.receipts[sid] = (fingerprint, result)
            if self.fail == 'after':
                self.fail = 'replay-blocked'
                route.abort()
            else:
                self.reply(route, result)
        else:
            self.unexpected.append(request.method + ' ' + u.path)
            self.reply(route, {'message': 'Unexpected request'}, 500)


def pending(page):
    return page.evaluate("Object.keys(localStorage).filter(k=>k.startsWith('ma-practica-outbox-v01:')).length")


def start(browser, width=375):
    context = browser.new_context(viewport={'width': width, 'height': 900}, service_workers='block')
    backend = Backend(context)
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(BASE, wait_until='load')
    assert backend.signups == 0
    assert page.evaluate("Function.prototype.toString.call(window.fetch).includes('[native code]')")
    page.locator('#account-save').click()
    expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=20000)
    return context, backend, page, errors


def choose_arithmetic(page):
    page.locator('#settings-panel > summary').click()
    page.locator('#area').select_option('aritmetica')
    page.locator('#mode').select_option('challenge')
    expect(page.locator('#title')).to_have_text('Sumar fracciones')


def solve(page):
    for key in (1, 0, 2):
        page.locator('#question input[name=answer]').nth(key).check()
        page.locator('#submit').click()
    expect(page.locator('#another')).to_be_visible()


def failure_and_reload(browser, phase, width):
    context, backend, page, errors = start(browser, width)
    try:
        choose_arithmetic(page)
        backend.fail = phase
        solve(page)
        expect(page.locator('#account-status')).to_contain_text('No se pudo confirmar', timeout=20000)
        expect(page.locator('#question')).to_contain_text('pendiente de sincronización')
        assert pending(page) == 1
        cached = page.evaluate('(key)=>JSON.parse(localStorage.getItem(key))', KEY)
        assert cached['ratings'].get('aritmetica', 1200) == 1200
        assert len(backend.receipts) == (0 if phase == 'before' else 1)
        page.reload(wait_until='load')
        expect(page.locator('#account-status')).to_contain_text('No se pudo confirmar', timeout=20000)
        assert pending(page) == 1 and backend.signups == 1
        backend.fail = None
        page.evaluate("window.dispatchEvent(new Event('online'))")
        expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=20000)
        expect(page.locator('#rating-current')).to_contain_text('1202')
        assert pending(page) == 0 and len(backend.receipts) == 1 and len(backend.sessions) == 1
        assert backend.ratings['aritmetica'] == 1202
        if phase == 'after':
            assert backend.replays >= 1
        page.reload(wait_until='load')
        expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=20000)
        expect(page.locator('#rating-current')).to_contain_text('1202')
        assert backend.signups == 1 and backend.imports == 1
        # Repetición distinta: nuevo ID de sesión, pero ningún segundo +2.
        choose_arithmetic(page)
        solve(page)
        expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=20000)
        assert len(backend.receipts) == 2 and len(backend.sessions) == 2
        assert backend.sessions[0]['payload']['delta'] is None
        expect(page.locator('#question')).to_contain_text('Esta repetición no modificó el Elo')
        assert not errors and not backend.unexpected
        assert page.evaluate('Math.max(document.documentElement.scrollWidth,document.body.scrollWidth)<=innerWidth+1')
        OUT.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(OUT / f'atomic-{phase}-{width}.png'), full_page=True)
        print(f'PASS atomic {phase} {width}px: cola durable, recarga, un movimiento, historial sin duplicados y repetición independiente')
    finally:
        context.close()


def expired_offline(browser):
    context, backend, page, errors = start(browser)
    try:
        page.evaluate('(key)=>{const s=JSON.parse(localStorage.getItem(key));s.expires_at=1;localStorage.setItem(key,JSON.stringify(s));}', AUTH)
        before = page.evaluate('(key)=>localStorage.getItem(key)', AUTH)
        backend.reject_auth = True
        page.reload(wait_until='load')
        expect(page.locator('#account-status')).to_contain_text('Auth offline fixture', timeout=20000)
        assert page.evaluate('(key)=>localStorage.getItem(key)', AUTH) == before
        choose_arithmetic(page)
        solve(page)
        expect(page.locator('#question')).to_contain_text('pendiente de sincronización')
        expect(page.locator('#account-status')).to_contain_text('Auth offline fixture', timeout=20000)
        assert pending(page) == 1 and backend.signups == 1
        backend.reject_auth = False
        page.evaluate("window.dispatchEvent(new Event('online'))")
        expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=20000)
        assert backend.signups == 1 and pending(page) == 0 and backend.ratings['aritmetica'] == 1202
        assert not errors and not backend.unexpected
        print('PASS token vencido + offline: identidad y pendientes conservados; renovación sin crear otra cuenta')
    finally:
        context.close()


def import_reply_lost(browser):
    context = browser.new_context(service_workers='block')
    backend = Backend(context)
    backend.lose_import = True
    page = context.new_page()
    try:
        page.goto(BASE, wait_until='load')
        page.locator('#account-save').click()
        expect(page.locator('#account-status')).to_contain_text('No se pudo confirmar', timeout=20000)
        page.reload(wait_until='load')
        expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=20000)
        assert backend.signups == 1 and backend.imports == 1
        assert not backend.unexpected
        print('PASS respuesta de importación perdida: reconoce la copia exacta sin sustituir la identidad')
    finally:
        context.close()


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            for width in (320, 375, 430, 1280):
                for phase in ('before', 'after'):
                    failure_and_reload(browser, phase, width)
            expired_offline(browser)
            import_reply_lost(browser)
        finally:
            browser.close()
    print('PASS entrega atómica UI: API simulada; cero escrituras en el Supabase real del autor')
