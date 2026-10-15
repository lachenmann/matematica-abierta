from pathlib import Path
import base64,zipfile,json,hashlib,re,fitz
from PIL import Image,ImageDraw
r=Path('apm-pdf-build');out=r/'delivery';out.mkdir(exist_ok=True);temp=r/'package';temp.mkdir(exist_ok=True)
with zipfile.ZipFile(__import__('io').BytesIO(base64.b64decode((r/'input.b64').read_bytes()))) as z:z.extractall(temp)
for p in (r/'output').glob('T1*.pdf'):(temp/'figures'/p.name).write_bytes(p.read_bytes())
readme='''Álgebra para matemáticos — Tomo I
A. Peña — Matemática Abierta
Fuentes derivadas de los 26 capítulos revisados y ampliados de Obsidian.

Overleaf: importe este ZIP, seleccione pdfLaTeX y main.tex (A4 digital) o main-carta.tex (Carta para impresión).
Local: latexmk -pdf main.tex ; latexmk -pdf main-carta.tex
Incluye las cinco figuras vectoriales PDF; no requiere shell escape.
AMSBook, 11 pt, Latin Modern. Las dos ediciones contienen ejercicios y soluciones completos.
26 capítulos, 2352 pares de ejercicios y soluciones, 43521 expresiones matemáticas y 99 tablas.
La licencia GNU FDL 1.3 completa está incorporada como apéndice de ambos PDF.
Los Markdown canónicos originales permanecen en Obsidian; no fueron modificados.
Esta entrega verifica conversión y maquetación, no vuelve a demostrar todos los resultados del libro.
Edición: 15 de octubre de 2026.
'''
(temp/'README.txt').write_text(readme,encoding='utf8')
with zipfile.ZipFile(out/'APM_Tomo_I_LaTeX_Overleaf_v01.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(temp.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(temp))
reports=[]
for stem,filename in [('main','APM_Tomo_I_Lectura_Digital_A4_v01.pdf'),('main-carta','APM_Tomo_I_Impresion_Carta_v01.pdf')]:
 p=r/'output'/f'{stem}.pdf';(out/filename).write_bytes(p.read_bytes());doc=fitz.open(p)
 qa=out/stem;qa.mkdir(exist_ok=True);toc=doc.get_toc();chapters=[x for x in toc if x[0]==1 and x[1].startswith('Capítulo ')]
 selected={1,2,3,len(doc)}|{c[2] for c in chapters}|{c[2]-1 for c in chapters[1:]}
 offset=chapters[0][2]-1
 log=(r/'output'/f'{stem}.log').read_text(errors='replace')
 tables=[int(x)+offset for x in re.findall(r'APMTABLE:page=(\d+)',log)]
 for n in tables:selected.update([n,min(n+1,len(doc))])
 flags=[];figures=[];blank=[];links=0
 sheet=None;thumbs=[]
 for i,page in enumerate(doc):
  txt=page.get_text()
  if not txt.strip():blank.append(i+1)
  if '##' in txt or 'SOURCE_PACKET' in txt or re.search(r'\boindent\b',txt):flags.append({'page':i+1,'kind':'residue'})
  if re.search(r'Figura 26\.[1-5]',txt):figures.append(i+1);selected.add(i+1)
  bad=[w for w in page.get_text('words') if w[1]>65 and w[3]<page.rect.height-65 and (w[0]<75 or w[2]>page.rect.width-75)]
  if bad:flags.append({'page':i+1,'kind':'margin','words':[w[4] for w in bad]});selected.add(i+1)
  for l in page.get_links():
   links+=1
   if l['kind']==fitz.LINK_GOTO and not 0<=l['page']<len(doc):flags.append({'page':i+1,'kind':'bad link'})
  pix=page.get_pixmap(matrix=fitz.Matrix(.35,.35),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);thumbs.append(im)
 for start in range(0,len(thumbs),40):
  sheet=Image.new('RGB',(1200,1824),'#ddd');draw=ImageDraw.Draw(sheet)
  for j,im in enumerate(thumbs[start:start+40]):
   im.thumbnail((230,205));x=j%5*240+(240-im.width)//2;y=j//5*228+20;sheet.paste(im,(x,y));draw.text((j%5*240+8,j//5*228+3),str(start+j+1),fill='black')
  sheet.save(qa/f'survey-{start//40:02d}.jpg',quality=72)
 for n in sorted(selected):
  page=doc[n-1];pix=page.get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False);pix.save(qa/f'read-{n:04d}.png')
 report={'file':filename,'pages':len(doc),'paper_points':list(doc[0].rect),'chapters':chapters,'table_pages':tables,'figure_pages':figures,'review_pages':sorted(selected),'flags':flags,'blank_pages':blank,'links':links,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 (qa/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));reports.append(report)
(out/'manifest.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2))
