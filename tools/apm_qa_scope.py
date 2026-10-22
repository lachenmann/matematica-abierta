"""Run the Tomo I browser battery when its chapters or shared presentation change."""
from pathlib import Path
import subprocess,json,argparse,re

COMMON={"_brand.yml","styles.scss","paper.scss","brand.scss","libros/_metadata.yml",
 "assets/books/reader.css","tools/smart_render.py","tests/apm_tome_browser.py",
 "data/apm-tome-i-manifest.json"}

def only_unrelated_resource_additions(old_config,new_config):
 """Keep every old resource and every presentation setting byte-for-byte."""
 if old_config==new_config:return True
 def parts(text):
  lines=text.splitlines(keepends=True)
  try:project=next(i for i,line in enumerate(lines) if line.rstrip()=='project:')
  except StopIteration:return None
  end=next((i for i in range(project+1,len(lines)) if lines[i].strip() and not lines[i][0].isspace()),len(lines))
  resource=next((i for i in range(project+1,end) if lines[i].rstrip()=='  resources:'),None)
  if resource is None:return None
  stop=resource+1
  while stop<len(lines) and (not lines[stop].strip() or lines[stop].startswith('    ')):stop+=1
  return lines[:resource+1],lines[resource+1:stop],lines[stop:]
 old,new=parts(old_config),parts(new_config)
 if old is None or new is None or old[0]!=new[0] or old[2]!=new[2]:return False
 index=0
 for line in new[1]:
  if index<len(old[1]) and line==old[1][index]:index+=1;continue
  if line=='    - "COPYING.FDL"\n':continue
  entry=re.fullmatch(r"    - ([\"']?)assets/books/([a-z0-9_-]+)/\*\*\1\s*",line)
  if not entry or entry[2] in {'apm','apm-tomo-i'}:return False
 return index==len(old[1])

def required(changed,chapter_paths,old_config,new_config):
 for name in changed:
  # Tomo II has a complete independent browser battery, including both indexes.
  # Neither its chapter pages nor the shared landing change Tomo I composition.
  if name.startswith(("libros/capitulos/algebra-para-matematicos-tomo-ii",
                      "libros/para-matematicos/algebra-para-matematicos-tomo-ii")):
   continue
  if name == "libros/para-matematicos/algebra-para-matematicos.md":
   continue
  if name in COMMON or name in chapter_paths:return True
  if name.startswith(('assets/books/apm-tomo-i/','assets/includes/','assets/brand/')):return True
  if name.startswith('libros/capitulos/algebra-para-matematicos'):return True
  if name.startswith('libros/para-matematicos/algebra-para-matematicos'):return True
  if name=='_quarto.yml':
   # New downloads belonging to another book do not change Tomo I composition.
   if not only_unrelated_resource_additions(old_config,new_config):return True
 return False

def main():
 p=argparse.ArgumentParser();p.add_argument('--base',required=True);a=p.parse_args()
 root=Path(__file__).resolve().parents[1]
 def git(*args):return subprocess.check_output(['git',*args],cwd=root,text=True)
 paths={row['path'] for row in json.loads((root/'data/apm-tome-i-manifest.json').read_text())['chapters']}
 changed=git('diff','--name-only',a.base,'HEAD').splitlines()
 decision=required(changed,paths,git('show',a.base+':_quarto.yml'),git('show','HEAD:_quarto.yml'))
 print('required='+str(decision).lower())
if __name__=='__main__':main()
