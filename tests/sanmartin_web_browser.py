"""Full IC2021 browser QA in CI: desktop/phone, MathJax, image loading and navigation."""
import functools, http.server, json, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT=Path('.ma-build/ic2021-visual');OUT.mkdir(parents=True,exist_ok=True)
handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory='_site')
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
origin=f'http://127.0.0.1:{server.server_port}'
root='/libros/otros/introduccion-al-calculo/'
names=['index',*[f'capitulo-{n:02}' for n in range(1,19)],'apendices']
results=[]
try:
 with sync_playwright() as pw:
  browser=pw.chromium.launch()
  for width in (390,768,1440):
   context=browser.new_context(viewport={'width':width,'height':900},color_scheme='light')
   page=context.new_page()
   for i,name in enumerate(names):
    response=page.goto(origin+root+name+'.html',wait_until='networkidle')
    assert response.status==200,(name,response.status)
    if name.startswith('capitulo') or name=='apendices':
     page.wait_for_function('window.MathJax?.startup?.promise',timeout=90000)
     page.evaluate('async()=>{await MathJax.startup.promise;await document.fonts.ready;}')
    data=page.evaluate('''()=>({math:document.querySelectorAll('main mjx-container').length,errors:[...document.querySelectorAll('main mjx-merror,main [data-mjx-error]')].map(x=>x.textContent),missingImages:[...document.querySelectorAll('main img')].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src),figures:document.querySelectorAll('main figure').length,altMissing:[...document.querySelectorAll('main img')].filter(x=>!x.alt).length,overflow:document.documentElement.scrollWidth>innerWidth+2,nav:[...document.querySelectorAll('.page-navigation a')].map(x=>new URL(x.href).pathname),readerStyles:[...document.querySelectorAll('link[rel=stylesheet]')].filter(x=>x.href.includes('/assets/books/reader.css')).length})''')
    results.append({'width':width,'page':name,**data})
    assert not data['errors'] and not data['missingImages'] and not data['altMissing'],(name,width,data)
    assert not data['overflow'] and data['readerStyles']==1,(name,width,data)
    if name.startswith('capitulo'):assert data['math']>0,(name,'no math')
    expected=[root+names[j]+'.html' for j in [i-1,i+1] if 0<=j<len(names)]
    normalized=[root+'index.html' if x==root else x for x in data['nav']]
    assert normalized==expected,(name,'navigation',normalized,expected)
    if name in ('index','capitulo-03','capitulo-13','capitulo-18'):
     page.screenshot(path=str(OUT/f'{name}-{width}.png'))
     if page.locator('main figure').count():
      page.locator('main figure').first.scroll_into_view_if_needed()
      page.screenshot(path=str(OUT/f'{name}-{width}-figure.png'))
   context.close()
  browser.close()
finally:
 (OUT/'report.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
 server.shutdown()
print('IC2021 browser PASS:',len(results),'page/viewport pairs')
