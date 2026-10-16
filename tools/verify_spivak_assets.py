"""Verifica los bytes de las figuras originales importadas del solucionario."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1];n=0
for p in (root/'data/ma-fig-manifests').glob('spv4-*.json'):
 d=json.loads(p.read_text())
 for key,name in d['outputs'].items():
  assert hashlib.sha256((root/name).read_bytes()).hexdigest()==d['output_sha256'][key],name
 n+=1
print(f'Spivak: {n} figuras, integridad exacta.')
