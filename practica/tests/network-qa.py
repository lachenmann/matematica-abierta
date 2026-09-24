"""Auditoría observable del tráfico del prototipo con MathJax servido por el mismo origen."""
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8765/practica/index.html'
MATHJAX = 'http://127.0.0.1:8765/practica/vendor/mathjax/tex-chtml.js'


def audit(browser):
    context = browser.new_context(viewport={'width': 320, 'height': 850}, locale='es-CL')
    page = context.new_page()
    requests = []
    try:
        def record(request):
            parsed = urlparse(request.url)
            if parsed.scheme in ('http', 'https'):
                requests.append(request)

        page.on('request', record)
        page.goto(BASE, wait_until='load', timeout=60000)
        page.locator('#prompt mjx-container').first.wait_for(timeout=45000)

        disclosure = page.locator('.privacy-disclosure')
        assert disclosure.is_visible(), 'Falta aviso de privacidad visible'
        text = disclosure.inner_text()
        assert 'no los transmite' in text
        assert 'misma copia de la aplicación' in text
        assert 'CDN' in text

        page.locator('#question input[name="answer"]').first.check()
        page.locator('#submit').click()
        page.locator('#history-toggle').click()
        assert page.locator('#history-panel').is_visible()

        assert any(request.url == MATHJAX for request in requests), 'No se observó el MathJax local preparado'
        external = [request.url for request in requests
                    if urlparse(request.url).hostname != '127.0.0.1']
        assert not external, f'La aplicación realizó solicitudes HTTP(S) externas: {external}'
        assert all('MAP-DEMO-' not in request.url and 'ma-practica-demo-v01' not in request.url
                   for request in requests), 'Una URL contiene datos del ejercicio o del almacenamiento'

        hosts = sorted({urlparse(request.url).hostname for request in requests})
        print(f'PASS tráfico Chromium: {len(requests)} solicitudes HTTP(S), hosts={hosts}; sin tráfico externo')
    finally:
        context.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            audit(browser)
        finally:
            browser.close()
