"""Regresión de fetch nativo y del botón de cuenta en Chromium.

La API Supabase se intercepta con Playwright: no se crean usuarios reales ni
se utiliza la configuración local del desarrollador. window.fetch NO se sustituye.
Ejecutar desde la raíz con servidor HTTP en 127.0.0.1:8765.
"""
# SPDX-License-Identifier: GPL-3.0-or-later
import json
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import expect, sync_playwright

BASE = 'http://127.0.0.1:8765/practica/index.html'
API_HOST = 'ma-fetch-regression.supabase.co'
API_ORIGIN = 'https://' + API_HOST
PROGRESS_KEY = 'ma-practica-demo-v01'
SESSION_KEY = 'ma-practica-supabase-session-v01'
LOCAL = {'ratings': {'algebra': 1333}, 'ratedIds': ['MAP-DEMO-006'], 'history': []}
USER = {'id': '00000000-0000-4000-8000-000000000001', 'is_anonymous': True, 'email': None}
OUT = Path('practica/browser-qa-artifacts')


class Fixture:
    def __init__(self, context, *, unbound=False, reject_signup=False):
        self.calls = []
        self.signups = 0
        self.imports = 0
        self.config_reads = 0
        self.unexpected = []
        self.snapshot = None
        self.reject_signup = reject_signup
        self.original_client = None
        if unbound:
            source = Path('practica/supabase-browser-client.mjs').read_text(encoding='utf-8')
            fixed = 'this.fetchImpl = fetchImpl.bind(globalThis);'
            assert fixed in source, 'Falta el punto de control del parche fetch'
            self.original_client = source.replace(fixed, 'this.fetchImpl = fetchImpl;', 1)
        context.route('**/*', self.route)
        context.add_init_script(
            'if (!localStorage.getItem(' + json.dumps(PROGRESS_KEY) + ')) {'
            'localStorage.setItem(' + json.dumps(PROGRESS_KEY) + ',' + json.dumps(json.dumps(LOCAL)) + ');}'
        )

    def reply(self, route, body, status=200):
        route.fulfill(status=status, content_type='application/json', body=json.dumps(body), headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'apikey,authorization,content-type,prefer',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
        })

    def route(self, route):
        request = route.request
        url = urlparse(request.url)
        if url.hostname == '127.0.0.1':
            if url.path.endswith('/supabase-config.local.mjs'):
                self.config_reads += 1
                route.fulfill(content_type='application/javascript', body=(
                    'export const projectUrl = ' + json.dumps(API_ORIGIN) + ';'
                    'export const publishableKey = "sb_publishable_fixture";'
                ))
            elif self.original_client and url.path.endswith('/supabase-browser-client.mjs'):
                route.fulfill(content_type='application/javascript', body=self.original_client)
            else:
                route.continue_()
            return
        if url.hostname != API_HOST:
            self.unexpected.append(request.url)
            route.abort()
            return
        if request.method == 'OPTIONS':
            self.reply(route, {})
            return
        self.calls.append((request.method, url.path))
        if url.path == '/auth/v1/signup' and request.method == 'POST':
            if self.reject_signup:
                self.reply(route, {'message': 'Servicio de prueba no disponible'}, 503)
            else:
                self.signups += 1
                self.reply(route, {'access_token': 'fixture-access', 'refresh_token': 'fixture-refresh',
                                   'expires_in': 3600, 'user': USER})
            return
        if request.headers.get('authorization') != 'Bearer fixture-access':
            self.reply(route, {'message': 'Token de prueba incorrecto'}, 401)
            return
        if url.path == '/auth/v1/user' and request.method == 'GET':
            self.reply(route, USER)
        elif url.path == '/rest/v1/rpc/ma_import_local_progress' and request.method == 'POST':
            self.imports += 1
            self.snapshot = request.post_data_json['p_snapshot']
            self.reply(route, [{'imported_ratings': 1, 'imported_rated_ids': 1, 'imported_sessions': 0}])
        elif url.path == '/rest/v1/user_ratings' and request.method == 'GET':
            self.reply(route, [{'area': 'algebra', 'rating': 1333}])
        elif url.path == '/rest/v1/rated_exercises' and request.method == 'GET':
            self.reply(route, [{'exercise_id': 'MAP-DEMO-006'}])
        elif url.path == '/rest/v1/practice_sessions' and request.method == 'GET':
            self.reply(route, [])
        else:
            self.unexpected.append(request.method + ' ' + url.path)
            self.reply(route, {'message': 'Solicitud no prevista por la prueba'}, 500)


def open_page(context):
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(BASE, wait_until='load', timeout=60000)
    expect(page.locator('#account-save')).to_be_visible()
    # Route intercepta HTTP, pero la función sigue siendo la nativa de Chromium.
    assert page.evaluate("Function.prototype.toString.call(window.fetch).includes('[native code]')")
    return page, errors


def local_progress(page):
    return page.evaluate('(key) => JSON.parse(localStorage.getItem(key))', PROGRESS_KEY)


def negative_control(browser):
    context = browser.new_context(viewport={'width': 375, 'height': 850}, service_workers='block')
    fixture = Fixture(context, unbound=True)
    try:
        page, errors = open_page(context)
        page.locator('#account-save').click()
        expect(page.locator('#account-status')).to_contain_text('Illegal invocation')
        assert fixture.calls == [], 'El fallo de receptor debe ocurrir antes de cualquier petición remota'
        assert local_progress(page) == LOCAL
        assert not errors and not fixture.unexpected
        print('PASS control negativo: llamada antigua reproduce Illegal invocation antes de la red')
    finally:
        context.close()


def opt_in(browser, width):
    context = browser.new_context(viewport={'width': width, 'height': 850}, service_workers='block')
    fixture = Fixture(context)
    try:
        page, errors = open_page(context)
        assert fixture.calls == [] and fixture.config_reads == 0
        assert local_progress(page) == LOCAL
        page.locator('#account-save').click()
        expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=15000)
        expect(page.locator('#account-save')).to_be_hidden()
        assert fixture.signups == 1 and fixture.imports == 1
        assert fixture.snapshot['version'] == 1
        for field, value in LOCAL.items():
            assert fixture.snapshot[field] == value
        assert local_progress(page) == LOCAL
        stored_id = page.evaluate('(key) => JSON.parse(localStorage.getItem(key)).user.id', SESSION_KEY)
        assert stored_id == USER['id']
        page.reload(wait_until='load')
        expect(page.locator('#account-badge')).to_have_text('Sincronización activa', timeout=15000)
        assert fixture.signups == 1 and fixture.imports == 1, 'Recargar no debe crear ni importar otra identidad'
        assert local_progress(page) == LOCAL
        assert not errors and not fixture.unexpected
        assert page.evaluate('Math.max(document.documentElement.scrollWidth, document.body.scrollWidth) <= innerWidth + 1')
        OUT.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(OUT / f'accounts-fetch-{width}.png'), full_page=True)
        print(f'PASS opt-in {width}px: fetch nativo, importación conservada y recarga sin duplicados; API simulada')
    finally:
        context.close()


def rejected_signup(browser):
    context = browser.new_context(viewport={'width': 375, 'height': 850}, service_workers='block')
    fixture = Fixture(context, reject_signup=True)
    try:
        page, errors = open_page(context)
        page.locator('#account-save').click()
        expect(page.locator('#account-status')).to_contain_text('Servicio de prueba no disponible')
        expect(page.locator('#account-save')).to_be_enabled()
        assert local_progress(page) == LOCAL and fixture.imports == 0
        assert page.evaluate('(key) => localStorage.getItem(key)', SESSION_KEY) is None
        assert not errors and not fixture.unexpected
        print('PASS HTTP 503: mensaje visible, progreso local intacto y ninguna importación')
    finally:
        context.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            negative_control(browser)
            for width in (320, 375, 430, 1280):
                opt_in(browser, width)
            rejected_signup(browser)
        finally:
            browser.close()
    print('PASS regresión opt-in: Chromium nativo; cero usuarios o escrituras en Supabase real')
