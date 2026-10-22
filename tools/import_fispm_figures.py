#!/usr/bin/env python3
"""Import audited editable SVG without changing any graphical XML node."""
from pathlib import Path
import hashlib,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def main():
 count=0
 for p in (ROOT/'data/ma-fig-manifests').glob('fpm-r20261021-*.json'):
  m=json.loads(p.read_text());raw=(ROOT/m['source_repository']).read_bytes()
  assert hashlib.sha256(raw).hexdigest()==m['source_sha256']
  out=re.sub(br'<!DOCTYPE\s+svg\s+PUBLIC\s+"[^"]*"\s+"[^"]*"\s*>\s*',b'',raw)
  assert ET.tostring(ET.fromstring(raw))==ET.tostring(ET.fromstring(out))
  assert hashlib.sha256(out).hexdigest()==m['output_sha256']['web_svg']
  (ROOT/m['outputs']['web_svg']).write_bytes(out);count+=1
 assert count==200,count
 print('FISPM SVG import: 200 figures; graphical XML preserved')
if __name__=='__main__':main()
