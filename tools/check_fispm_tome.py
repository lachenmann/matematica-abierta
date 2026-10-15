"""Check the FISPM source contract and the actual thirty rendered chapters."""
import argparse,collections,json,re
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

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--site-dir',type=Path);args=parser.parse_args()
 data=json.loads((ROOT/'data/fispm-tome-i-manifest.json').read_text(encoding='utf-8'));rows=data['chapters'];assert len(rows)==30
 assert len({r['content_id'] for r in rows})==30
 assert rows[0]['content_id']=='MA-BCH-0009' and rows[1]['content_id']=='MA-BCH-0031'
 sources={r['chapter']:(ROOT/r['path']).read_text(encoding='utf-8') for r in rows}
 for r in rows:
  s=sources[r['chapter']]
  assert 'content-id: '+r['content_id'] in s and 'source-id: '+r['source_id'] in s
  assert '[[' not in s and '[!' not in s
  assert not re.search(r'PRIVATE|QA_PASS|EDITORIAL_PROVISIONAL_CLOSE|MASTER_CANONICO',s)
  if r['chapter']>1:assert Path(rows[r['chapter']-2]['path']).name in s
  if r['chapter']<30:assert Path(rows[r['chapter']]['path']).name in s
 if args.site_dir:
  site=args.site_dir.resolve();pages={}
  for r in rows:
   p=site/Path(r['path']).with_suffix('.html');assert p.is_file(),p
   parsed=Page();parsed.feed(p.read_text(encoding='utf-8'));pages[p.resolve()]=parsed
   duplicates=[x for x,n in collections.Counter(parsed.ids).items() if n>1 and x not in {'quarto-bootstrap','quarto-text-highlighting-styles'}]
   assert not duplicates,(p,duplicates)
   assert parsed.math>100,(p,parsed.math)
   assert any(x.endswith('assets/books/reader.css') for x in parsed.styles),(p,'missing canonical reader CSS')
   for im in parsed.images:
    assert im.get('alt','').strip(),(p,'missing alt')
    u=urlsplit(im['src'])
    if not u.scheme:assert (p.parent/unquote(u.path)).is_file(),(p,im['src'])
  for p,page in pages.items():
   for href in page.links:
    u=urlsplit(href)
    if u.scheme or u.netloc:continue
    target=(site/u.path.lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)).resolve() if u.path else p
    if target in pages and u.fragment:assert unquote(u.fragment) in pages[target].ids,(p.name,href)
  assert sum(sum('/assets/books/fispm/' in im.get('src','') for im in p.images) for p in pages.values())==data['figure_count']
 print('FISPM Tome I: PASS — 30 sources'+(' and 30 rendered chapters, declared figures, local links and canonical CSS' if args.site_dir else ''))
if __name__=='__main__':main()
