"""Check the EDC edition's identifiers, coverage, rendered links and local assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import argparse,re,json,collections,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
folder=root/'libros/otros/elementos-del-calculo'
parser=argparse.ArgumentParser();parser.add_argument('--site-dir',type=Path);args=parser.parse_args()
files=list(folder.glob('*.md'))+list(folder.glob('*.qmd'));assert len(files)==56
exc=sol=0;ids=[]
for f in files:
 text=f.read_text();assert '[[' not in text and 'drive.google.com' not in text
 assert 'license: GFDL-1.3-or-later' in text
 ids+=re.findall(r'^content-id: (MA-\S+)',text,re.M)
 if f.name.endswith('-ejercicios.md'):
  chapter=f.name[9:11];a=set(re.findall(r'EDC-C'+chapter+r'-EXR-\d{3}',text))
  b=set(re.findall(r'EDC-C'+chapter+r'-SOL-\d{3}',(folder/f'capitulo-{chapter}-soluciones.md').read_text()))
  assert {x.replace('-EXR-','-SOL-') for x in a}==b,(f,a,b);exc+=len(a);sol+=len(b)
assert exc==sol==338,(exc,sol)
assert len(ids)==len(set(ids))==13
assert 'MA-BOK-0015' in ids and all(f'MA-BCH-{i:04d}' in ids for i in range(331,343))
historical_count=0
for chapter in range(12):
 text=(folder/f'capitulo-{chapter:02}.md').read_text()
 expected=2 if chapter in [2,3,4,8] else 1
 actual=text.count('title="Historia — ')
 assert actual==expected,(chapter,actual,expected)
 assert text.count('*Lectura opcional.*')==expected
 historical_count+=actual
assert historical_count==16
svg=list((root/'assets/books/elementos-del-calculo').glob('*.svg'));assert len(svg)==7
for figure in svg:
 assert len(figure.read_bytes())>1000
 assert ET.fromstring(figure.read_bytes()).tag.endswith('svg')
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag in ['a','img','script','link']:
   key='href' if tag in ['a','link'] else 'src'
   if key in a:self.links.append(a[key])
if args.site_dir:
 site=args.site_dir.resolve();cached={};count=0
 for f in files:
  page=site/f.relative_to(root).with_suffix('.html');assert page.is_file(),page
  parsed=Links();parsed.feed(page.read_text())
  if re.fullmatch(r'capitulo-\d\d.md',f.name):
   html=page.read_text()
   assert 'Lectura opcional.' in html and 'Historia — ' in html,page
   assert 'data-bs-toggle="collapse"' in html,page
  content_ids=[x for x in parsed.ids if x not in ['quarto-text-highlighting-styles','quarto-bootstrap']]
  assert len(content_ids)==len(set(content_ids)),page
  for link in parsed.links:
   url=urlsplit(link)
   if url.scheme or url.netloc:continue
   target=(site/unquote(url.path).lstrip('/') if url.path.startswith('/') else page.parent/unquote(url.path)).resolve() if url.path else page
   if target.is_dir():target=target/'index.html'
   # Global navigation can point outside the targeted QA render.
   if str(target).startswith(str(site/'libros/otros/elementos-del-calculo')) or '/assets/' in str(target) or target.name=='COPYING.FDL':
    assert target.is_file(),(page,link)
    if url.fragment and target.suffix=='.html':
     if target not in cached:
      p=Links();p.feed(target.read_text());cached[target]=p.ids
     assert unquote(url.fragment) in cached[target],(page,link)
    count+=1
 for landing in ['libros/index.html','libros/otros/index.html']:
  p=site/landing
  if p.is_file():assert 'elementos-del-calculo/index.html' in p.read_text(),p
 print('EDC rendered routes/assets/fragments:',count,'PASS')
 import sys
 sys.path.insert(0,str(root))
 from tools.check_ma_fig_html import verify_html_figure
 for manifest in (root/'data/ma-fig-manifests').glob('edc-*.json'):
  errors=verify_html_figure(site,root,json.loads(manifest.read_text()))
  assert not errors,errors
 print('EDC C9: 14 figure placements, captions, alt and SHA-256 PASS')
print('EDC structure: 56 pages, 12 chapters, 338 exercise/solution pairs, 7 SVG, 13 IDs PASS')
