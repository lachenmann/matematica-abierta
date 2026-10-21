#!/usr/bin/env python3
"""Read-only desktop/phone QA for complete APM Tomo II."""
from pathlib import Path
from functools import partial
import http.server,socketserver,threading,json,os
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];os.chdir(ROOT)
m=json.loads((ROOT/'data/apm-tome-ii-manifest.json').read_text());out=ROOT/'.ma-build/apm-ii-visual';out.mkdir(parents=True,exist_ok=True)
class Server(socketserver.TCPServer):allow_reuse_address=True
server=Server(('127.0.0.1',8792),partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT/'_site')));threading.Thread(target=server.serve_forever,daemon=True).start();checks=[]
with sync_playwright() as p:
 browser=p.chromium.launch();contexts={w:browser.new_context(viewport={'width':w,'height':1000}) for w in [375,1440]}
 for row in m['chapters']:
  for width,ctx in contexts.items():
   page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   response=page.goto('http://127.0.0.1:8792/'+row['path'].replace('.md','.html'),wait_until='networkidle',timeout=120000);page.wait_for_function('!!window.MathJax?.startup?.promise',timeout=120000)
   page.evaluate('''async()=>{await MathJax.startup.promise;await document.fonts.ready;await Promise.all([...document.images].map(async i=>{i.loading='eager';try{await i.decode()}catch{}}))}''')
   d=page.evaluate('''(expected)=>{const m=document.querySelector('main.content'),ids=[...m.querySelectorAll('[id]')].map(x=>x.id);return {pageWidth:document.documentElement.scrollWidth,math:m.querySelectorAll('mjx-container').length,sourceMath:m.querySelectorAll('.math').length,mathErrors:m.querySelectorAll('mjx-merror,merror,[data-mjx-error]').length,missingIds:expected.filter(x=>!document.getElementById(x)),duplicateIds:ids.filter((x,i)=>ids.indexOf(x)!==i),failedImages:[...m.querySelectorAll('img')].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),missingAlt:[...m.querySelectorAll('img')].filter(i=>!i.alt.trim()).length,brokenFragments:[...m.querySelectorAll('a[href^="#"]')].filter(a=>a.hash.length>1&&!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash)}}''',row['ids'])
   d.update(chapter=row['chapter'],width=width,status=response.status,errors=list(errors));d['pass']=response.status==200 and d['pageWidth']<=width+2 and d['math']>0 and d['math']==d['sourceMath'] and not any(d[k] for k in ['mathErrors','missingIds','duplicateIds','failedImages','missingAlt','brokenFragments','errors']);checks.append(d)
   for label,target in [('theory',page.locator('main.content h2').first),('exercise',page.locator('[id="'+row['exercise_ids'][0]+'"]')),('solution',page.locator('[id="'+row['solution_ids'][0]+'"]')),('end',page.locator('[id="'+row['solution_ids'][-1]+'"]'))]:
    if target.count():target.scroll_into_view_if_needed();page.screenshot(path=str(out/f'c{row["chapter"]:02}-{width}-{label}.png'))
   page.close();(out/'results.json').write_text(json.dumps({'complete':len(checks)==40,'checks':checks},ensure_ascii=False,indent=2));print(json.dumps({'chapter':row['chapter'],'width':width,'pass':d['pass']}),flush=True)
 browser.close()
server.shutdown();assert len(checks)==40 and all(x['pass'] for x in checks),json.dumps([x for x in checks if not x['pass']],ensure_ascii=False)
print('APM Tomo II: 40/40 desktop/phone checks PASS')
