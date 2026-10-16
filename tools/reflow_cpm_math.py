"""Recompose measured wide prose displays, retaining mathematical tokens."""
from pathlib import Path
import argparse,json,re,textwrap
p=argparse.ArgumentParser();p.add_argument('project',type=Path);p.add_argument('measurements',type=Path);a=p.parse_args()
def endbrace(s,start):
 d=1;i=start+1
 while i<len(s) and d:
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):d+=1
  elif s[i]=='}' and s[i-1]!='\\':d-=1
  i+=1
 return i
def wrap_text(s):
 out='';i=0
 while i<len(s):
  if s.startswith('\\text{',i):
   j=endbrace(s,i+5);body=s[i+6:j-1]
   if len(body)>60 and '\\' not in body:
    chunks=textwrap.wrap(body,56,break_long_words=False,break_on_hyphens=False)
    if all(c.count('$')%2==0 for c in chunks):
     out+='\\begin{gathered}'+'\\\\'.join('\\text{'+c+'}' for c in chunks)+'\\end{gathered}'
    else:out+=s[i:j]
   else:out+=s[i:j]
   i=j
  else:out+=s[i];i+=1
 return out
op=re.compile(r'\\(?:longrightarrow|Longrightarrow|longleftrightarrow|Longleftrightarrow|iff|to|neq|qquad|quad)\b')
def rows(s):
 # The single-column array is only a layout container.
 if s.startswith('\\begin{array}{c}') and s.endswith('\\end{array}') and s.count('\\begin{array}')==1:
  s=s[len('\\begin{array}{c}'):-len('\\end{array}')]
 out=[];start=0;depth=0;env=0;i=0
 while i<len(s):
  if s.startswith('\\begin{',i):env+=1
  if s.startswith('\\end{',i):env-=1
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  elif s[i]=='}' and s[i-1]!='\\':depth-=1
  m=op.match(s,i)
  if m and depth==0 and env==0:
   if s[start:i].strip():out.append(s[start:i].strip())
   start=i
  i+=1
 if s[start:].strip():out.append(s[start:].strip())
 return out
def normalized(s):
 s=re.sub(r'\\(?:begin|end)\{gathered\}','',s)
 s=re.sub(r'\\begin\{array\}\{c\}|\\end\{array\}','',s)
 s=s.replace('\\\\','');s=re.sub(r'\\text\{','{',s)
 return re.sub(r'\s|[{}]','',s)
manual={
 (1,794):r'\boxed{\begin{gathered}\text{la longitud de la diagonal de un cuadrado de lado }1\\\text{ no puede representarse mediante un número racional}.\end{gathered}}',
 (4,72):r'\boxed{\begin{gathered}\text{solo estudiaremos el límite de }f\\\text{ cuando el punto de aproximación}\\\text{ sea punto de acumulación de su dominio.}\end{gathered}}',
 (4,506):r'\boxed{\begin{gathered}\text{las dos paredes exteriores entran en la banda }(L-\varepsilon,L+\varepsilon),\\\text{ y la función intermedia queda obligada a entrar con ellas.}\end{gathered}}',
 (5,227):r'\boxed{\begin{gathered}\text{si una función es continua en todos los puntos de un}\\\text{intervalo,}\\\text{ ¿puede saltarse un valor situado entre dos valores que}\\\text{sí toma?}\end{gathered}}',
 (5,550):r'\boxed{\begin{gathered}\text{infinitos puntos pueden estar organizados de tal manera}\\\text{ que toda cobertura abierta se reduzca a finitos testigos.}\end{gathered}}',
 (5,558):r'\boxed{\begin{gathered}\text{la completitud debe producir una frontera de cobertura}\\+\text{la apertura debe impedir que esa frontera se detenga}\\\text{antes del extremo}.\end{gathered}}',
 (5,862):r'\boxed{\begin{gathered}\text{si la función original es además continua sobre un}\\\text{intervalo,}\\\text{ entonces la inversa no solo conserva el orden: también}\\\text{es continua.}\end{gathered}}'
}
records=json.loads((a.project/'layout-transforms.json').read_text()) if (a.project/'layout-transforms.json').exists() else []
for d in json.loads(a.measurements.read_text()):
 path=a.project/'chapters'/f"c{d['chapter']:02}.tex";s=path.read_text();idx=d['index']
 pattern=re.compile(r'(\\begin\{cpmath\}\{'+str(idx)+r'\}\n)([\s\S]*?)(\n\\end\{cpmath\})')
 m=pattern.search(s);assert m,(path,idx)
 old=m[2].strip();boxed=old.startswith('\\boxed{') and endbrace(old,6)==len(old)
 body=old[7:-1].strip() if boxed else old
 body=wrap_text(body);parts=rows(body)
 new='\\begin{gathered}\n'+'\\\\[3pt]\n'.join(parts)+'\n\\end{gathered}'
 if boxed:new='\\boxed{'+new+'}'
 new=manual.get((d['chapter'],idx),new)
 # Only layout commands and whitespace may differ.
 assert normalized(old)==normalized(new.replace('[3pt]','')),(path,idx)
 s=s[:m.start(2)]+new+s[m.end(2):];path.write_text(s)
 previous=next((x for x in records if x['chapter']==d['chapter'] and x['index']==idx),None)
 if previous:previous['after']=new
 else:records.append({'chapter':d['chapter'],'index':idx,'before':old,'after':new,'token_conservation':True})
(a.project/'layout-transforms.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print('Recomposed',len(records),'wide displays; token conservation verified.')
