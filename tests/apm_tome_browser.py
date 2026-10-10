"""QA of actual Quarto composition: all APM chapters, desktop and phone."""
import json,os,threading,http.server,functools
from pathlib import Path
from playwright.sync_api import sync_playwright
out=Path('.ma-build/apm-visual');out.mkdir(parents=True,exist_ok=True)
manifest=json.loads(Path('data/apm-tome-i-manifest.json').read_text())
handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory='_site')
server=http.server.ThreadingHTTPServer(('127.0.0.1',8791),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
base=os.environ.get('APM_QA_URL','http://127.0.0.1:8791')
checks=[]
with sync_playwright() as p:
 browser=p.chromium.launch()
 for row in manifest['chapters']:
  for width in [375,1440]:
   page=browser.new_page(viewport={'width':width,'height':1000},device_scale_factor=1)
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   response=page.goto(base+'/'+row['path'].replace('.md','.html'),wait_until='networkidle',timeout=120000)
   page.wait_for_function('!!window.MathJax?.startup?.promise',timeout=120000)
   page.evaluate('async()=>{await MathJax.startup.promise;await document.fonts.ready}')
   data=page.evaluate('''()=>{
    const main=document.querySelector('main.content');const ids=[...main.querySelectorAll('[id]')].map(x=>x.id);
    return {width:innerWidth,pageWidth:document.documentElement.scrollWidth,
     math:main.querySelectorAll('mjx-container').length,sourceMath:main.querySelectorAll('.math').length,
     mathErrors:main.querySelectorAll('mjx-merror,merror,[data-mjx-error]').length,
     undefinedCommands:[...main.querySelectorAll('mjx-container')].filter(e=>e.querySelector('[mathcolor="red"]')||[...e.querySelectorAll('mjx-mtext')].some(n=>n.style.color==='red')).map(e=>e.textContent),
     failedImages:[...main.querySelectorAll('img')].filter(e=>!e.complete||!e.naturalWidth).map(e=>e.src),
     missingAlt:main.querySelectorAll('img:not([alt]),img[alt=""]').length,
     missingAnchors:[...main.querySelectorAll('a[href^="#"]')].filter(e=>e.hash.length>1&&!document.getElementById(decodeURIComponent(e.hash.slice(1)))).map(e=>e.hash),
     duplicateIds:ids.filter((x,i)=>ids.indexOf(x)!==i),
     privateIds:/MA-(EX|SOL)-APM|INTERNAL EDITORIAL|SOURCE_PACKET_ID|PRCM_v04/.test(main.innerText)};
   }''')
   data.update(chapter=row['chapter'],status=response.status,errors=list(errors))
   data['pass']=response.status==200 and data['math']>0 and data['math']==data['sourceMath'] and data['pageWidth']<=width+2 and not any(data[k] for k in ['mathErrors','undefinedCommands','failedImages','missingAlt','missingAnchors','duplicateIds','privateIds','errors'])
   checks.append(data)
   main=page.locator('main.content')
   for label,locator in [('theory',main.locator('h2').first),('exercises',main.locator('h1,h2,h3,h4').filter(has_text='Ejercicios').first),('solutions',main.locator('h1,h2,h3,h4').filter(has_text='Soluciones').last),('end',main.locator('h1,h2,h3,h4').last)]:
    if locator.count():
     locator.scroll_into_view_if_needed();page.screenshot(path=str(out/f"c{row['chapter']:02d}-{width}-{label}.png"))
   if row['chapter']==26:
    for i,img in enumerate(main.locator('img').all(),1):
     img.scroll_into_view_if_needed();page.screenshot(path=str(out/f'c26-{width}-fig{i}.png'))
   page.close();print(json.dumps({k:data[k] for k in ['chapter','width','math','pass']}),flush=True)
   (out/'results.json').write_text(json.dumps({'complete':len(checks)==52,'checks':checks},ensure_ascii=False,indent=2))
 browser.close()
server.shutdown()
assert len(checks)==52 and all(x['pass'] for x in checks),json.dumps([x for x in checks if not x['pass']],ensure_ascii=False)
print('APM: 52/52 desktop and phone compositions PASS')
