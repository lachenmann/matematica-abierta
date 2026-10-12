"""Run the full APM browser battery when APM or its shared presentation changes."""
from pathlib import Path
import subprocess,json,argparse

COMMON={"_brand.yml","styles.scss","paper.scss","brand.scss","libros/_metadata.yml",
 "assets/books/reader.css","tools/smart_render.py","tests/apm_tome_browser.py",
 "data/apm-tome-i-manifest.json","libros/para-matematicos/algebra-para-matematicos.md"}

def required(changed,chapter_paths,old_config,new_config):
 for name in changed:
  if name in COMMON or name in chapter_paths:return True
  if name.startswith(('assets/books/apm-tomo-i/','assets/includes/','assets/brand/')):return True
  if name.startswith('libros/capitulos/algebra-para-matematicos'):return True
  if name.startswith('libros/para-matematicos/algebra-para-matematicos'):return True
  if name=='_quarto.yml':
   # A verbatim extra licence resource does not change existing page composition.
   if new_config.replace('    - "COPYING.FDL"\n','')!=old_config:return True
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
