"""Same-build Android-width online/file:// reader comparison (not device QA).

Run with a Python environment containing playwright and its Chromium browser:
python tests/offline_parity_browser.py --site _site --output /tmp/parity-qa
"""
import argparse
import functools
import http.server
import json
from pathlib import Path
import threading
import time

from playwright.sync_api import sync_playwright


PROBE = """() => {
  const main = document.querySelector('main');
  const nodes = [...main.querySelectorAll('h1,h2,h3,p,li,td,th,table,.callout,mjx-container')];
  return {mathVersion: window.MathJax?.version,
    mathMetrics: [...window.MathJax.startup.document.math].filter(m=>main.contains(m.start.node)).slice(0,3).map(m=>m.metrics),
    fonts: [...document.fonts].map(f=>({family:f.family,weight:f.weight,style:f.style,status:f.status})),
    outputOptions: JSON.stringify(window.MathJax.startup.document.outputJax.options),
    mathCount: main.querySelectorAll('mjx-container').length,
    errors: main.querySelectorAll('mjx-merror,[data-mjx-error]').length,
    clippedMath: [...main.querySelectorAll('mjx-container[display="true"]')].flatMap((el,index)=>{
      const math=el.querySelector('mjx-math'); if(!math)return [];
      const box=math.getBoundingClientRect();
      for(let parent=el;parent && parent!==main;parent=parent.parentElement){
        if(['hidden','auto','scroll','clip'].includes(getComputedStyle(parent).overflowY)){
          const bounds=parent.getBoundingClientRect();
          if(box.top < bounds.top-1 || box.bottom > bounds.bottom+1) return [{index,top:box.top-bounds.top,bottom:box.bottom-bounds.bottom}];
        }
      } return [];
    }),
    verticalOverflow: [...main.querySelectorAll('mjx-container[display=\"true\"]')].map((el,index)=>({index,client:el.clientHeight,scroll:el.scrollHeight})).filter(x=>x.scroll>x.client+1),
    fcp: performance.getEntriesByName('first-contentful-paint')[0]?.startTime,
    ready: window.__mathReady,
    metrics: nodes.map(el => {
      const r=el.getBoundingClientRect(), s=getComputedStyle(el);
      return {tag:el.tagName, text:el.textContent.slice(0,60), x:r.x, y:r.y+scrollY, width:r.width, height:r.height,
        font:s.fontFamily, size:s.fontSize, line:s.lineHeight, color:s.color};
    })};
}"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', type=Path, default=Path('_site'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--width', type=int, action='append')
    parser.add_argument('--chapter', action='append')
    args = parser.parse_args()
    site = args.site.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    package = site / 'app/offline/MA-BOK-0005'
    manifest = json.loads((package / 'manifest-v1.json').read_text())
    css = (Path(__file__).resolve().parents[1] / 'tools/offline-reader.css').read_text()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(site))
    class Server(http.server.ThreadingHTTPServer):
        # Quarto starts many parallel asset requests on a cold browser context.
        request_queue_size = 128

    server = Server(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    origin = f'http://127.0.0.1:{server.server_port}'
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in (args.width or [390, 430]):
            for chapter in manifest['contents']:
                if args.chapter and chapter['contentId'] not in args.chapter:
                    continue
                pair = {}
                for mode in ['online', 'offline']:
                    context = browser.new_context(viewport={'width': width, 'height': 844},
                                                  color_scheme='dark', device_scale_factor=1)
                    page = context.new_page()
                    errors, failed, external, responses = [], [], [], []
                    page.on('response', lambda r: responses.append({'url': r.url, 'status': r.status}) if r.status >= 400 else None)
                    page.on('pageerror', lambda e: (errors.append(str(e)), print('page error', str(e), flush=True)))
                    page.on('requestfailed', lambda r: failed.append(r.url))
                    if mode == 'online':
                        def reader(route):
                            response = route.fetch()
                            text = response.text().replace('</head>', '<style>'+css+'</style></head>')
                            route.fulfill(response=response, body=text)
                        page.route(origin + chapter['canonicalPath'], reader)
                        url = origin + chapter['canonicalPath']
                    else:
                        def no_network(route):
                            external.append(route.request.url)
                            route.abort()
                        context.route('http://**/*', no_network)
                        context.route('https://**/*', no_network)
                        url = (package / chapter['localPath']).as_uri()
                    page.add_init_script("""document.addEventListener('DOMContentLoaded',()=>{
                      const spans=[...document.querySelectorAll('main .math')];
                      const expected=spans.length;
                      window.__mathSamples={};
                      for(const [name,token] of Object.entries({fraction:String.fromCharCode(92)+'frac',root:String.fromCharCode(92)+'sqrt',sum:String.fromCharCode(92)+'sum',power:'^',prime:"'"})) {
                        const index=spans.findIndex(el=>el.textContent.includes(token));
                        if(index>=0) window.__mathSamples[name]=index;
                      }
                      const first=spans.findIndex(el=>el.classList.contains('inline'));
                      if(first>=0) window.__mathSamples.inline=first;
                      const check=()=>{if(document.querySelectorAll('main mjx-container').length>=expected && expected>0){
                        document.fonts.ready.then(()=>{window.__mathReady=performance.now()});
                        observer.disconnect();
                      }};
                      const observer=new MutationObserver(check);
                      observer.observe(document.body,{childList:true,subtree:true}); check();
                    });""")
                    print('loading', mode, width, chapter['contentId'], flush=True)
                    page.on('console', lambda m: print('browser', m.type, m.text[:300], flush=True) if m.type == 'error' else None)
                    page.goto(url, wait_until='domcontentloaded', timeout=60000)
                    print('DOM ready', mode, flush=True)
                    deadline = time.monotonic() + 60
                    while not page.evaluate('() => Boolean(window.__mathReady) && document.fonts.status === "loaded"'):
                        if time.monotonic() > deadline:
                            print('startup failure', errors, failed, page.evaluate('() => ({version:window.MathJax?.version, count:document.querySelectorAll("mjx-container").length, ready:window.__mathReady})'), flush=True)
                            raise RuntimeError('math/font readiness timeout')
                        page.wait_for_timeout(50)
                    print('math ready', mode, flush=True)
                    page.wait_for_timeout(300)
                    pair[mode] = {**page.evaluate(PROBE), 'pageErrors': errors,
                                  'failedRequests': failed, 'externalRequests': external, 'httpErrors': responses}
                    cdp = context.new_cdp_session(page)
                    cdp.send('DOM.enable')
                    cdp.send('CSS.enable')
                    root = cdp.send('DOM.getDocument')
                    node = cdp.send('DOM.querySelector', {'nodeId':root['root']['nodeId'], 'selector':'main.content'})
                    pair[mode]['renderedFonts'] = cdp.send('CSS.getPlatformFontsForNode', {'nodeId':node['nodeId']})['fonts']
                    cdp.detach()
                    page.screenshot(path=str(args.output / f'{chapter["contentId"]}-{width}-{mode}.png'),
                                    full_page=False)
                    samples = page.evaluate(r'''() => {
                      const spans=[...document.querySelectorAll('main .math')]; const samples={};
                      for(const [name,token] of Object.entries({fraction:'\\frac',root:'\\sqrt',sum:'\\sum',power:'^',prime:'\\prime'})) {
                        const index=spans.findIndex(el=>(el.querySelector('mjx-math')?.dataset.latex||'').includes(token));
                        if(index>=0)samples[name]=index;
                      }
                      if(samples.prime===undefined){const i=spans.findIndex(el=>(el.querySelector('mjx-math')?.dataset.latex||'').includes("'"));if(i>=0)samples.prime=i;}
                      const inline=spans.findIndex(el=>el.classList.contains('inline'));if(inline>=0)samples.inline=inline;
                      return samples;
                    }''')
                    pair[mode]['samples'] = samples
                    for name, index in samples.items():
                        page.locator('main .math').nth(index).scroll_into_view_if_needed()
                        page.screenshot(path=str(args.output / f'{chapter["contentId"]}-{width}-{mode}-{name}.png'))
                    fragment = page.locator('main a[href^="#"]').first
                    if fragment.count():
                        href = fragment.get_attribute('href')
                        fragment.evaluate('(el)=>el.click()')
                        pair[mode]['fragmentNavigation'] = page.evaluate('() => location.hash') == href
                    context.close()
                online, offline = pair['online'], pair['offline']
                differences = []
                if len(online['metrics']) != len(offline['metrics']):
                    differences.append({'nodeCount': [len(online['metrics']),len(offline['metrics'])]})
                for index, (a,b) in enumerate(zip(online['metrics'],offline['metrics'])):
                    changes = {key:[a[key],b[key]] for key in a if
                               (abs(a[key]-b[key]) > 1 if isinstance(a[key],(int,float)) else a[key]!=b[key])}
                    if changes:
                        differences.append({'node': index, 'changes': changes})
                pair['differences'] = differences
                pair['chapter'] = chapter['contentId']
                pair['width'] = width
                results.append(pair)
                (args.output / 'report.json').write_text(json.dumps(results,indent=2))
                print(chapter['contentId'], width, 'differences',len(differences),
                      'math ms', online['ready'],offline['ready'], flush=True)
        browser.close()
    server.shutdown()
    if any(r['differences'] or r['offline']['errors'] or r['offline']['pageErrors'] or
           r['offline']['failedRequests'] or r['offline']['externalRequests'] or r['offline']['clippedMath'] or
           r['online']['httpErrors'] or r['offline']['httpErrors'] or
           r['online']['errors'] or r['online']['failedRequests'] or r['online']['pageErrors'] or
           not r['offline'].get('fragmentNavigation', True) for r in results):
        raise SystemExit('PARITY FAILED: inspect report.json')


if __name__ == '__main__':
    main()
