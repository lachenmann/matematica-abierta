"""Auditoría observable del tráfico del prototipo; no sustituye revisión de privacidad del proveedor.
Ejecutar con servidor local en 127.0.0.1:8765 y Playwright + Chromium.
"""
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8765/practica/index.html'
EXPECTED = {'127.0.0.1', 'cdn.jsdelivr.net'}
MATHJAX = 'https://cdn.jsdelivr.net/npm/mathjax@4.0.0/tex-chtml.js'


def audit(browser):
    context = browser.new_context(viewport={'width': 320, 'height': 850}, locale='es-CL')
    page = context.new_page()
    outbound = []
    requests = []
    try:
        def record(request):
            parsed = urlparse(request.url)
            if parsed.scheme not in ('http', 'https'):
                return
            requests.append(request)
            if parsed.hostname not in EXPECTED:
                outbound.append(request.url)
        page.on('request', record)
        page.goto(BASE, wait_until='load', timeout=60000)
        page.locator('#prompt mjx-container').first.wait_for(timeout=45000)
        assert page.locator('.privacy-disclosure').is_visible(), 'Falta aviso de privacidad visible'
        assert 'datos técnicos de conexión' in page.locator('.privacy-disclosure').inner_text()
        link = page.locator('.privacy-disclosure a')
        assert link.get_attribute('href') == 'https://www.jsdelivr.com/terms/privacy-policy'
        assert link.get_attribute('target') == '_blank'
        assert {'noopener', 'noreferrer'} <= set(link.get_attribute('rel').split())
        page.locator('#question input[name="answer"]').first.check()
        page.locator('#submit').click()
        page.locator('#history-toggle').click()
        assert page.locator('#history-panel').is_visible()
        assert not outbound, f'Solicitudes a dominios no inventariados: {outbound}'
        external = [request for request in requests if urlparse(request.url).hostname != '127.0.0.1']
        assert external and any(request.url == MATHJAX for request in external), 'No se observó el recurso CDN declarado'
        assert all(request.method == 'GET' for request in external), 'Hubo envíos no GET a proveedor externo'
        assert all('MAP-DEMO-' not in request.url and 'ma-practica-demo-v01' not in request.url
                   for request in external), 'Un recurso externo contiene datos del ejercicio o almacenamiento en URL'
        initial = next(request for request in external if request.url == MATHJAX)
        assert not initial.all_headers().get('referer'), 'El script inicial filtra la URL referente'
        hosts = sorted({urlparse(request.url).hostname for request in requests})
        print(f'PASS tráfico Chromium: {len(requests)} solicitudes HTTP(S), hosts={hosts}; jsDelivr GET y sin referente inicial')
    finally:
        context.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            audit(browser)
        finally:
            browser.close()
