"""Rebuild only the approved ANM SVG web derivatives; never generates figures."""
from pathlib import Path
import json, re, hashlib
root=Path(__file__).resolve().parents[1]
for path in (root/'data/ma-fig-manifests').glob('*.json'):
    doc=json.loads(path.read_text())
    if 'revision-20261016' not in doc.get('source_repository',''): continue
    source=root/doc['source_repository']; raw=source.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==doc['source_sha256'], source
    data=re.sub(rb'<!DOCTYPE[^>]*(?:\[[\s\S]*?\]\s*)?>',b'',raw)
    output=root/doc['outputs']['web_svg']
    assert hashlib.sha256(data).hexdigest()==doc['output_sha256']['web_svg'], output
    output.parent.mkdir(parents=True,exist_ok=True); output.write_bytes(data)
print('ANM: approved SVG derivatives rebuilt with exact expected hashes')
