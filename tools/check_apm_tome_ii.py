#!/usr/bin/env python3
"""Validate the complete approved Tomo II source and its Quarto output."""
from pathlib import Path
from html.parser import HTMLParser
import argparse,hashlib,json,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
def reading_text(s):
 s=re.sub(r'\A---\n.*?\n---\n','',s,flags=re.S).strip()
 s=re.sub(r'^# Capítulo \d+\. [^\n]+\n','',s,count=1).strip()
 s=re.sub(r'<figure\b.*?</figure>','',s,flags=re.S)
 s=re.sub(r'<span\b[^>]*class="apm-anchor"[^>]*></span>','',s)
 s=re.sub(r'<!--\s*ID:.*?-->','',s,flags=re.S)
 s='\n'.join(l for l in s.splitlines() if not '[Índice del tomo II]' in l)
 s=re.sub(r'\n---\s*$','',s)
 return ' '.join(s.split())
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.images=[];self.hrefs=[];self.math=0;self.captions={};self.figure=None;self.in_caption=False
 def handle_starttag(self,t,a):
  a=dict(a)
  if a.get('id'):self.ids.append(a['id'])
  if t=='figure':self.figure=a.get('id');self.captions[self.figure]=''
  if t=='figcaption':self.in_caption=True
  if t=='img':self.images.append(a)
  if t=='a' and a.get('href'):self.hrefs.append(a['href'])
  if 'math' in a.get('class','').split():self.math+=1

 def handle_endtag(self,t):
  if t=='figcaption':self.in_caption=False
 def handle_data(self,s):
  if self.in_caption:self.captions[self.figure]+=s

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--site-dir',type=Path);ap.add_argument('--caption-roundtrip',action='store_true');args=ap.parse_args()
 m=json.loads((ROOT/'data/apm-tome-ii-manifest.json').read_text());assert len(m['chapters'])==20
 allids=[];ex=sol=0
 for row in m['chapters']:
  p=ROOT/row['path'];s=p.read_text();ids=re.findall(r'<span id="([^"]+)" class="apm-anchor"></span>',s)
  assert ids==row['ids'],row['path'];allids+=ids
  assert hashlib.sha256(reading_text(s).encode()).hexdigest()==row['approved_reading_sha256'],row['path']
  ex+=len(row['exercise_ids']);sol+=len(row['solution_ids']);assert len(row['exercise_ids'])==len(row['solution_ids'])
  assert 'status: published\n' in s and 'draft: false\n' in s and 'solution-status: complete\n' in s
  assert 'SOURCE_PACKET' not in s and '[[' not in s
  for ref in re.findall(r'\]\((/[^)]+\.md)\)',s):assert (ROOT/ref.lstrip('/')).is_file(),ref
  if args.caption_roundtrip:
   h=subprocess.check_output(['quarto','pandoc',str(p),'--to=html','--mathjax'],text=True);page=Page();page.feed(h)
   for f in m['figures']:
    if f['chapter']!=row['chapter']:continue
    manifest=json.loads((ROOT/f['manifest']).read_text())
    assert ' '.join(manifest['caption'].split()) in ' '.join(page.captions[manifest['figure_label']].split()),manifest['figure_id']
  if args.site_dir:
   h=(args.site_dir/Path(row['path']).with_suffix('.html')).read_text();page=Page();page.feed(h)
   assert set(ids)<=set(page.ids),row['path'];assert len(page.ids)==len(set(page.ids)),row['path'];assert page.math>0
   assert len([im for im in page.images if '/apm-tomo-ii/' in im.get('src','')])==sum(f['chapter']==row['chapter'] for f in m['figures'])
 assert len(allids)==1901 and len(set(allids))==1901 and ex==808 and sol==808
 assert len(m['figures'])==78
 for f in m['figures']:assert hashlib.sha256((ROOT/f['output']).read_bytes()).hexdigest()==f['sha256']
 print('APM Tomo II: 20 capítulos, 808 ejercicios, 808 soluciones, 1901 IDs y 78 figuras: PASS')
if __name__=='__main__':main()
