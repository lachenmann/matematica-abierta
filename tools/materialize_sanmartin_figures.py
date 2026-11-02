#!/usr/bin/env python3
"""Materialize verified IC2021 figures from the tracked source bundle.

For Quarto website pre-render: safe, idempotent and entirely offline.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import sys
import zipfile
from sanmartin_archive import ensure_archive

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'assets/books/san-martin/IC2021_master_y_figuras.zip'
TARGET = ROOT / 'libros/otros/introduccion-al-calculo-san-martin'


def check_member(name: str):
    p=pathlib.PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or p.parts[0]!='figuras' or p.suffix.lower()!='.png':
        raise ValueError(f'Ruta insegura de figura: {name}')


def run():
    with zipfile.ZipFile(ensure_archive()) as z:
        meta=json.loads(z.read('MANIFEST.json'))
        if meta.get('schema')!=1 or len(meta.get('figures',{}))!=175:
            raise ValueError('Se esperaban 175 figuras verificadas')
        done=0
        for name,detail in sorted(meta['figures'].items()):
            check_member(name)
            payload=z.read(name)
            if hashlib.sha256(payload).hexdigest()!=detail['sha256'] or len(payload)!=detail['size']:
                raise ValueError('Falla de integridad de figura '+name)
            to=TARGET/name
            if to.exists() and hashlib.sha256(to.read_bytes()).hexdigest()==detail['sha256']:
                done+=1
                continue
            to.parent.mkdir(parents=True,exist_ok=True)
            to.write_bytes(payload)
            done+=1
    print(f'IC2021 figuras: PASS — {done} PNG disponibles para Quarto')


if __name__=='__main__':
    try:run()
    except Exception as e:
        print(f'IC2021 figuras: FAIL — {e}',file=sys.stderr);sys.exit(1)
