#!/usr/bin/env python3
"""Reconstruye únicamente el derivado QMD verificado; no edita el maestro de Drive."""
import base64
import bz2
import hashlib
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
DEST = Path('problemas/colecciones/spivak-calculus/capitulo-01.qmd')
EXPECTED = 'e6032555ef420580be6e8efa63d6831442592a519526d7125764d3db65580e1e'
parts = sorted(BASE.glob('fragmento-*.b64'))
assert len(parts) == 16, f'Fragmentos incompletos: {len(parts)}/16'
encoded = ''.join(p.read_text('ascii').strip() for p in parts)
data = bz2.decompress(base64.b64decode(encoded, validate=True))
actual = hashlib.sha256(data).hexdigest()
assert actual == EXPECTED, f'Hash inesperado: {actual}'
assert data.startswith(b'---\ntitle: "Spivak, Calculus')
text = data.decode('utf-8')
ids = re.findall(r'^## (SPV4-C01-E\d{3})\b', text, re.M)
assert ids == [f'SPV4-C01-E{i:03d}' for i in range(1, 26)]
assert len(re.findall(r'^### ', text, re.M)) == 202
assert '$el de $k=0$$' not in text
assert '$se comprueba separadamente' not in text
assert len(re.findall(r'^\|', text, re.M)) > 50
DEST.parent.mkdir(parents=True, exist_ok=True)
DEST.write_bytes(data)
print(f'PASS: {DEST} | {len(data)} bytes | SHA256 {actual} | 25 ejercicios | 202 subsecciones')
