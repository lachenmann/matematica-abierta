"""Final local table composition, without altering the source's rational values."""
from pathlib import Path
import argparse,json,re
p=argparse.ArgumentParser();p.add_argument('project',type=Path);a=p.parse_args()
path=a.project/'chapters/c05.tex';s=path.read_text();edits=[]
def table(m):
 old=m[0]
 if 'intervalo conservado' not in old:return old
 new=re.sub(r'(\d+)/(\d+)',lambda z:r'\dfrac{'+z[1]+'}{'+z[2]+'}',old)
 normalize=lambda t:re.sub(r'\\dfrac\{(\d+)\}\{(\d+)\}',r'\1/\2',t)
 assert normalize(new)==normalize(old)
 edits.append({'chapter':5,'table':'Bisección; primeros ocho cortes','before':old,'after':new,'rational_values_preserved':True})
 return new
s=re.sub(r'\\begin\{longtable\}[\s\S]*?\\end\{longtable\}',table,s);assert len(edits)==1
path.write_text(s)
if not (a.project/'table-transforms.json').exists():(a.project/'table-transforms.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2))
bookmarks={
 'sec-t1-c02-05':'Completitud: la propiedad que falta en ℚ',
 'sec-t1-c04-02':'Tan cerca como queramos, desde algún momento: la definición ε–N',
 'sec-t1-c04-04':'El álgebra de límites: cuándo podemos calcular sin volver a ε',
 'sec-t1-c05-02':'De la cola al entorno perforado: la definición ε–δ',
 'sec-t1-c06-08':'Una sola δ para todo el intervalo: continuidad uniforme',
 'sec-t1-c19-09':'Funciones racionales III: cuadráticos irreducibles y la aparición de arctan',
 'sec-t1-c20-06':"Longitud de la gráfica: de polígonos a ∫√(1+(f′)²)"
}
def brace_end(t,start):
 depth=1;i=start+1
 while depth:
  if t[i]=='{' and t[i-1]!='\\':depth+=1
  elif t[i]=='}' and t[i-1]!='\\':depth-=1
  i+=1
 return i
for path in (a.project/'chapters').glob('*.tex'):
 s=path.read_text()
 s=re.sub(r'\\Needspace\{8\\baselineskip\}(\n\\hypertarget\{[^}]+\}\{%\n\\subsection\{Soluciones)',lambda m:'\\Needspace{12\\baselineskip}'+m[1],s)
 for ident,title in bookmarks.items():
  start=s.find('\\hypertarget{'+ident+'}')
  if start<0:continue
  command=s.index('\\texorpdfstring{',start);first=command+len('\\texorpdfstring');second=brace_end(s,first);assert s[second]=='{';end=brace_end(s,second)
  s=s[:second+1]+title+s[end-1:]
 path.write_text(s)
(a.project/'bookmark-transforms.json').write_text(json.dumps(bookmarks,ensure_ascii=False,indent=2))
print('Bisection table recomposed; all rational values preserved.')
