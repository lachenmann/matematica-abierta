"""Validate the controlled public derivative before and after HTML rendering."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,sys
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/'libros/otros/tratado-funciones'
manifest=json.loads((BOOK/'source-manifest.json').read_text())
pages=list(BOOK.glob('*.qmd'))
assert len(pages)==35, len(pages)
assert len(list(BOOK.glob('capitulo-*.qmd')))==18
assert manifest['status']=='publication-candidate-ci-pending'
for catalog,target in [('libros/index.qmd','otros/tratado-funciones/index.html'),('libros/otros/index.qmd','tratado-funciones/index.qmd')]:
 assert (ROOT/catalog).read_text().count(target)>=1, catalog
anchors={}
for page in pages:
 text=page.read_text()
 assert '[[' not in text and 'drive.google.com' not in text,page
 assert re.search(r'^draft: false$',text,re.M) and re.search(r'^status: published$',text,re.M),page
 assert '## Edición en preparación' not in text,page
 assert not re.search(r'(no redactado|reservado pero no redactado|la introducción general sigue pendiente|La introducción general .*continúa pendiente)',text),page
 found=re.findall(r'<a id="([^"]+)"></a>',text)
 assert len(found)==len(set(found)),page
 anchors[page.name]=set(found)
mathids=[x for values in anchors.values() for x in values if re.fullmatch(r'TF-(?:AX|DEF|THM|EXA|CEX)-\d{5}',x)]
assert len(mathids)==len(set(mathids))==269
for kind,count in {'AX':9,'DEF':73,'THM':133,'EXA':32,'CEX':22}.items():
 assert sum(x.startswith('TF-'+kind+'-') for x in mathids)==count,kind
for n in (17,18):assert not anchors[f'capitulo-{n}.qmd']
for page in pages:
 for target,anchor in re.findall(r'\]\(([^\s()]+\.qmd)(?:#([^\s()]+))?\)',page.read_text()):
  assert (page.parent/target).is_file(),(page.name,target)
  if anchor:assert anchor in anchors[Path(target).name],(page.name,target,anchor)
assert len(manifest['sources'])==34
assert all(re.fullmatch('[0-9a-f]{64}',s['sha256']) for s in manifest['sources'])
for source in manifest['sources']:
 text=(BOOK/source['derived']).read_text()
 version_line=next(line for line in text.splitlines() if line.startswith('source-version:'))
 assert version_line.split(':',1)[1].strip().strip('"').strip("'")==source['version'], source['derived']
tfkeys=re.findall(r'@\w+\{(tf-[^,]+),',(ROOT/'references.bib').read_text())
assert len(tfkeys)==len(set(tfkeys))==37, 'TF bibliography keys'
assert next(s for s in manifest['sources'] if s['document_id']=='TF-CAT-009')['version']=='1.0.4'
assert next(s for s in manifest['sources'] if s['document_id']=='TF-BIB-PUBLIC-0001')['version']=='1.0.0'
print('35 pages; 18 chapters; 269 unique anchors; local destinations and source versions valid; 37 unique TF bibliography keys')

if '--html' in sys.argv:
 class Parse(HTMLParser):
  def __init__(self):super().__init__();self.ids=[];self.links=[];self.styles=[]
  def handle_starttag(self,tag,attrs):
   a=dict(attrs)
   if 'id' in a:
    # Quarto reuses these two stylesheet IDs for light/dark variants.
    # Only link elements with those IDs are excluded from content anchor QA.
    if tag=='link' and a.get('rel')=='stylesheet' and a['id'] in {'quarto-bootstrap','quarto-text-highlighting-styles'}:self.styles.append(a['id'])
    else:self.ids.append(a['id'])
   if tag=='a' and 'href' in a:self.links.append(a['href'])
 dest=ROOT/'_site/libros/otros/tratado-funciones'
 parsed={}
 for page in pages:
  h=dest/(page.stem+'.html');assert h.is_file(),h
  parser=Parse();parser.feed(h.read_text());parsed[h.name]=parser
  duplicates={id:count for id,count in Counter(parser.ids).items() if count>1}
  assert not duplicates,(h,duplicates)
  assert anchors[page.name].issubset(set(parser.ids)),h
  assert 'drive.google.com' not in h.read_text(),h
 for name,p in parsed.items():
  for url in p.links:
   path,_,fragment=url.partition('#')
   if path in parsed and fragment:assert fragment in parsed[path].ids,(name,url)
 print('35 rendered pages; all result anchors retained; no private Drive URLs')
