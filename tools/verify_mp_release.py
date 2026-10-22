#!/usr/bin/env python3
"""Verify the complete MP edition, public downloads, and SVG import."""
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
def main():
 manifest=json.loads((ROOT/'data/mp-web-v1-manifest.json').read_text())
 assert len(manifest['units'])==28
 for u in manifest['units']:
  page=(ROOT/u['path']).read_text()
  assert u['source_sha256'] in page
  assert u['content_id'] in page
 for a in manifest['assets']:
  data=(ROOT/a['path']).read_bytes()
  assert len(data)==a['bytes'],a['path']
  assert hashlib.sha256(data).hexdigest()==a['sha256'],a['path']
 figures=list((ROOT/'data/ma-fig-manifests').glob('mp-*.json'))
 assert len(figures)==77
 for p in figures:
  f=json.loads(p.read_text());src=(ROOT/f['source_repository']).read_text()
  expected=re.sub(r'<!DOCTYPE[^>]*>\s*','',src,flags=re.S)
  assert expected==(ROOT/f['outputs']['web_svg']).read_text(),p
 print('MP release: PASS — 28 units, 77 original figures, 3 exact downloads')
def check_site(site):
 from html.parser import HTMLParser
 from urllib.parse import urlsplit,unquote
 class Page(HTMLParser):
  def __init__(self,text):
   super().__init__();self.ids=set();self.links=[];self.images=[];self.main=False;self.feed(text)
  def handle_starttag(self,tag,attrs):
   a=dict(attrs)
   if tag=='main':self.main=True
   if 'id' in a:self.ids.add(a['id'])
   if tag=='a' and 'href' in a:self.links.append(a['href'])
   if tag=='img':self.images.append(a)
 folder=site/'libros/otros/matematica-preuniversitaria'
 pages={p.resolve():Page(p.read_text()) for p in folder.glob('*.html')}
 assert len(pages)==30, f'MP: expected 30 pages, found {len(pages)}'
 proofs=0;images=set()
 for path,page in pages.items():
  assert page.main, f'MP: empty or incomplete page {path}'
  for href in page.links:
   u=urlsplit(href)
   if u.scheme or u.netloc:continue
   target=(site/u.path.lstrip('/') if u.path.startswith('/') else path.parent/unquote(u.path) if u.path else path).resolve()
   # Global navigation is validated by the existing site checks.
   if target.parent!=folder.resolve():continue
   assert target.is_file(), (path,href)
   if u.fragment:
    assert unquote(u.fragment) in pages[target].ids,(path,href)
    if target.stem=='apendice':proofs+=1
  for image in page.images:
   src=unquote(urlsplit(image.get('src','')).path)
   if '/assets/books/mp/' not in src:continue
   target=site/src.lstrip('/') if src.startswith('/') else path.parent/src
   assert target.is_file(), (path,src)
   assert image.get('alt','').strip(), (path,src,'missing alt')
   images.add(target.resolve())
 assert len(images)==77,len(images)
 assert proofs>=155,proofs
 print(f'MP HTML: PASS — 30 pages, {proofs} proof links, 77 described figures')
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--site-dir',type=Path);args=parser.parse_args()
 main()
 if args.site_dir:check_site(args.site_dir.resolve())
