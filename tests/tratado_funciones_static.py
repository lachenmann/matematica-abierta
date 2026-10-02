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
assert manifest['status']=='published'
for catalog,target in [('libros/index.qmd','otros/tratado-funciones/index.html'),('libros/tratados/index.qmd','../otros/tratado-funciones/index.html')]:
 catalog_text=(ROOT/catalog).read_text()
 assert catalog_text.count(target)>=1, catalog
 assert 'dieciocho capítulos, ejercicios' not in catalog_text.lower(), catalog
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

# Formal-treatise policy: chapters may contain examples and counterexamples, but no exercise blocks.
for n in range(1,19):
 text=(BOOK/f'capitulo-{n:02d}.qmd').read_text()
 assert not re.search(r'(?im)^(?:#{1,6}\s+.*\bejercicios?\b|\*\*Ejercicios?\b)',text), f'embedded exercise in chapter {n}'

# Appendix C is part of the treatise as worked examples, not as exercises or a problem-bank collection.
appendix_c=(BOOK/'apendice-c.qmd').read_text()
appendix_c_body=appendix_c.split('---',2)[-1]
assert 'title: Apéndice C. Ejemplos desarrollados' in appendix_c
assert len(re.findall(r'^### Ejemplo C\.\d+\.',appendix_c,re.M))==41
assert not re.search(r'(?i)\bejercicios?\b|\bsoluciones?\b',appendix_c_body)
assert '**Enunciado.**' not in appendix_c and '**Pista.**' not in appendix_c and '**Solución.**' not in appendix_c
assert not (ROOT/'problemas/colecciones/tratado-funciones/index.qmd').exists()
assert '[Apéndice C — Ejemplos desarrollados](apendice-c.qmd)' in (BOOK/'index.qmd').read_text()

# Final editorial closure: no stale publication/pedagogy language may remain.
book_text='\n'.join(page.read_text() for page in pages)
assert 'banco de problemas' not in book_text.lower()
assert 'sin publicación web' not in book_text.lower()
assert 'preguntas para verificar comprensión' not in book_text.lower()
assert 'pendiente técnico:' not in book_text.lower()
assert '### 18.6.3. Cierre editorial y continuidad formal' in (BOOK/'capitulo-18.qmd').read_text()
assert '[Apéndice C](apendice-c.qmd)' in (BOOK/'indice-ejemplos.qmd').read_text()

# Linear reading navigation must remain complete and reciprocal.
reading_order=[
 'prefacio.qmd','introduccion.qmd','convenciones.qmd','matriz-hipotesis.qmd',
 *[f'capitulo-{n:02d}.qmd' for n in range(1,19)],
 'apendice-a.qmd','apendice-b.qmd','apendice-c.qmd','apendice-d.qmd',
 'bibliografia.qmd','glosario.qmd','indice-conceptos.qmd','indice-notacion.qmd',
 'indice-resultados.qmd','indice-ejemplos.qmd','indice-contraejemplos.qmd','indice-fundamentos.qmd'
]
for i,name in enumerate(reading_order):
 text=(BOOK/name).read_text()
 navs=re.findall(r'::: \{\.tf-navigation\}([\s\S]*?):::',text)
 assert navs,name
 nav=navs[-1]
 prev='index.qmd' if i==0 else reading_order[i-1]
 nxt='index.qmd' if i==len(reading_order)-1 else reading_order[i+1]
 assert f'[← Anterior]({prev})' in nav,(name,'previous',prev)
 assert '[Índice del tratado](index.qmd)' in nav,name
 assert f'[Siguiente →]({nxt})' in nav,(name,'next',nxt)

# Reconstruct the declared dependency graph from result comments.
node_owner={anchor:page.name for page in pages for anchor in anchors[page.name] if re.fullmatch(r'TF-(?:AX|DEF|THM|EXA|CEX)-\d{5}',anchor)}
edges=[]
theorems={}
for n in range(1,17):
 page=BOOK/f'capitulo-{n:02d}.qmd'
 text=page.read_text()
 for line in text.splitlines():
  m=re.search(r'result-id:\s*(TF-(?:AX|DEF|THM|EXA|CEX)-\d{5});\s*depends-on:\s*(.*?)\s*-->',line)
  if m:
   raw=m.group(2).strip()
   deps=[] if raw=='[]' else [x.strip() for x in raw.split(',') if x.strip()]
   for dep in deps: edges.append((dep,m.group(1)))
  m=re.match(r'^\*\*Teorema\s+([0-9]+\.[0-9]+\.[0-9]+)\s+—\s+(.+?)\*\*\s*<!--\s*result-id:\s*(TF-THM-\d{5});\s*depends-on:\s*(.*?)\s*-->',line)
  if m:
   raw=m.group(4).strip()
   deps=[] if raw=='[]' else [x.strip() for x in raw.split(',') if x.strip()]
   theorems[m.group(3)]={'locator':m.group(1),'title':m.group(2),'deps':deps,'page':page.name}
assert len(theorems)==133
assert len(edges)==len(set(edges))==800, len(edges)
assert all(a in node_owner and b in node_owner for a,b in edges)
assert all(a!=b for a,b in edges)

# DAG check.
adj={x:[] for x in node_owner}
indeg={x:0 for x in node_owner}
for a,b in edges:
 adj[a].append(b);indeg[b]+=1
queue=[x for x,d in indeg.items() if d==0];seen=0
while queue:
 v=queue.pop();seen+=1
 for w in adj[v]:
  indeg[w]-=1
  if indeg[w]==0:queue.append(w)
assert seen==len(node_owner),'dependency graph contains a cycle'

# Appendix B must be a mechanically synchronized theorem atlas.
atlas=(BOOK/'apendice-b.qmd').read_text()
atlas_rows={}
for line in atlas.splitlines():
 m=re.match(r'^\| \[(TF-THM-\d{5})\]\([^)]+\) \| \[([0-9]+\.[0-9]+\.[0-9]+)\]\([^)]+\) \| (.*?) \| (.*?) \|$',line)
 if m:
  atlas_rows[m.group(1)]={
   'locator':m.group(2),
   'title':m.group(3),
   'deps':re.findall(r'\[(TF-(?:AX|DEF|THM|EXA|CEX)-\d{5})\]\(',m.group(4))
  }
assert len(atlas_rows)==133
for id,meta in theorems.items():
 assert id in atlas_rows,id
 assert atlas_rows[id]['locator']==meta['locator'],id
 assert atlas_rows[id]['title']==meta['title'],id
 assert atlas_rows[id]['deps']==meta['deps'],id
assert '269 nodos' in atlas and '800 aristas únicas' in atlas

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
print('35 pages; 18 chapters; 269 unique anchors; 800-edge DAG; 133 synchronized theorem-atlas rows; local destinations and source versions valid; 37 unique TF bibliography keys')

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
