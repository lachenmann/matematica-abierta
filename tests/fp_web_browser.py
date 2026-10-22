"""QA C de la edición web de Física preuniversitaria: fórmulas, figuras y navegación."""
import functools
import http.server
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright

OUTPUT = Path('.ma-build/fp-visual')
OUTPUT.mkdir(parents=True, exist_ok=True)
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory='_site')
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
origin = f'http://127.0.0.1:{server.server_port}'
root = '/libros/otros/fisica-preuniversitaria/'
results = []
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for width in (390, 1440):
            context = browser.new_context(viewport={'width': width, 'height': 900}, color_scheme='light')
            page = context.new_page()
            for name in ['index', *[f'capitulo-{n:02}' for n in range(1, 24)]]:
                response = page.goto(origin + root + name + '.html', wait_until='networkidle')
                assert response.status == 200, (name, response.status)
                if name != 'index':
                    page.wait_for_function('window.MathJax && window.MathJax.startup && window.MathJax.startup.promise', timeout=60000)
                    page.evaluate('async () => { await MathJax.startup.promise; await document.fonts.ready; }')
                    page.wait_for_selector('main mjx-container', timeout=60000)
                data = page.evaluate('''() => {
                    const main = document.querySelector('main');
                    return {
                        math: main.querySelectorAll('mjx-container').length,
                        mathErrors: [...main.querySelectorAll('mjx-merror,[data-mjx-error]')].map(x=>x.textContent),
                        missingImages: [...main.querySelectorAll('img')].filter(x=>!x.complete || x.naturalWidth===0).map(x=>x.src),
                        images: main.querySelectorAll('img').length,
                        readerStyles: [...document.querySelectorAll('link[rel="stylesheet"]')].filter(x=>x.href.includes('/assets/books/reader.css')).length,
                        overflow: document.documentElement.scrollWidth > innerWidth + 2,
                        navigation: [...main.querySelectorAll('a')].filter(x=>x.textContent.includes('Índice del libro')).length
                    };
                }''')
                results.append({'width': width, 'page': name, **data})
                assert not data['mathErrors'], (name, width, data['mathErrors'])
                assert not data['missingImages'], (name, width, data['missingImages'])
                assert not data['overflow'], (name, width, 'page overflow')
                assert data['readerStyles'] == 1, (name, data)
                if name != 'index':
                    assert data['math'] > 0 and data['navigation'] == 2, (name, data)
                if name in ('index', 'capitulo-01', 'capitulo-06', 'capitulo-15', 'capitulo-20', 'capitulo-23'):
                    page.screenshot(path=str(OUTPUT / f'{name}-{width}-top.png'))
                    image = page.locator('main img').first
                    if image.count():
                        image.scroll_into_view_if_needed()
                        page.screenshot(path=str(OUTPUT / f'{name}-{width}-figure.png'))
            context.close()
        browser.close()
finally:
    (OUTPUT / 'report.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf8')
    server.shutdown()
print(f'FP web QA PASS: {len(results)} páginas/vistas')
