#!/usr/bin/env python3
"""Verify the revised canonical edition, exact downloads and the v04 archive."""
import argparse,collections,hashlib,json,re,subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.images=[];self.styles=[];self.math=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag=='img':self.images.append(a)
  if tag=='link' and a.get('rel')=='stylesheet':self.styles.append(a.get('href',''))
  if 'math' in a.get('class','').split():self.math+=1

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--site-dir',type=Path);args=parser.parse_args()
 data=json.loads((ROOT/'data/fispm-tome-i-manifest.json').read_text());rows=data['chapters']
 assert data['canonical'] is True and data['edition']=='r20261021'
 assert [r['chapter'] for r in rows]==list(range(28))
 assert len(set(r['content_id'] for r in rows))==28
 assert sum(r['exercises'] for r in rows)==565 and sum(r['figures'] for r in rows)==200
 for r in rows:
  p=ROOT/r['path'];s=p.read_text();assert digest(p)==r['web_sha256']
  assert 'content-id: '+r['content_id'] in s and 'source-id: '+r['source_id'] in s
  assert 'canonical-edition: true' in s and 'archive: true' not in s
  assert '[[' not in s and '[!' not in s
  en,sol=s.split('## Soluciones',1)
  eh=re.findall(r'^### (\d+)\. (.*?) \{#ejercicio-\d+-\d+\}',en,re.M)
  sh=re.findall(r'^### (\d+)\. (.*?) \{#solucion-\d+-\d+\}',sol,re.M)
  assert eh==sh and len(eh)==r['exercises'] and 18<=len(eh)<=27,(p,'exercise pairs')
  assert len(re.findall(r'!\[',s))==r['figures']
  if r['chapter']>0:assert Path(rows[r['chapter']-1]['path']).name in s
  if r['chapter']<27:assert Path(rows[r['chapter']+1]['path']).name in s
 for f in data['figures']:assert digest(ROOT/f['path'])==f['sha256']
 for d in data['downloads']:
  p=ROOT/d['output'];assert p.is_file() and p.stat().st_size==d['bytes'] and digest(p)==d['sha256']
 archive=data['archive'];assert 'archive: true' in (ROOT/archive['landing']).read_text()
 for r in archive['chapters']:
  s=(ROOT/r['path']).read_text();assert 'archive: true' in s
  # Only metadata and an explicit archival notice precede the original body.
  assert hashlib.sha256(s.split(':::\n',1)[1].replace('../para-matematicos/fisica-para-matematicos-v04-archivo.md','../para-matematicos/fisica-para-matematicos.md').encode()).hexdigest()==r['sha256_cuerpo_original'],r['path']
 catalog=json.loads((ROOT/'app/catalog-v1.json').read_text())
 current=[x for x in catalog['items'] if x.get('parentId')=='MA-BOK-0005']
 assert {x['id'] for x in current}=={r['content_id'] for r in rows}
 assert not any(x['path']==('/'+Path(r['path']).with_suffix('.html').as_posix()) for x in current for r in archive['chapters'])
 if args.site_dir:
  site=args.site_dir.resolve();pages={}
  for r in rows:
   p=site/Path(r['path']).with_suffix('.html');assert p.is_file(),p
   parsed=Page();parsed.feed(p.read_text());pages[p.resolve()]=parsed
   assert not [x for x,n in collections.Counter(parsed.ids).items() if n>1 and x not in {'quarto-bootstrap','quarto-text-highlighting-styles'}],p
   assert parsed.math>50,(p,'math missing')
   assert sum(x.endswith('assets/books/reader.css') for x in parsed.styles)==1,(p,'reader CSS')
   assert sum('/assets/books/fispm/r20261021/' in im.get('src','') for im in parsed.images)==r['figures']
   for im in parsed.images:
    assert im.get('alt','').strip(),(p,'alt')
    u=urlsplit(im['src'])
    if not u.scheme:
     target=site/unquote(u.path).lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)
     assert target.is_file(),(p,im['src'])
  for p,page in pages.items():
   for href in page.links:
    u=urlsplit(href)
    if u.scheme or u.netloc:continue
    target=(site/u.path.lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)).resolve() if u.path else p
    if target in pages and u.fragment:assert unquote(u.fragment) in pages[target].ids,(p.name,href)
  for d in data['downloads']:assert digest(site/d['output'])==d['sha256']
  landing=site/'libros/para-matematicos/fisica-para-matematicos.html';s=landing.read_text()
  assert 'Edición canónica revisada' in s and '532 páginas' in s
  for r in rows:assert Path(r['path']).with_suffix('.html').name in s
  assert (site/Path(archive['landing']).with_suffix('.html')).is_file()
 legacy=['python3',str(ROOT/'tools/check_fispm_v04_archive.py')]
 if args.site_dir:legacy+=['--site-dir',str(args.site_dir)]
 subprocess.run(legacy,cwd=ROOT,check=True)
 print('FISPM canonical edition: PASS — 28 chapters, 565 solved pairs, 200 figures, exact downloads, preserved v04 archive'+('; rendered HTML and resources verified' if args.site_dir else ''))
if __name__=='__main__':main()
