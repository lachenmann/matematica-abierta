#!/usr/bin/env python3
"""Reassemble the verified IC2021 Quarto source ZIP from versioned Git blobs.

The distributed pieces are ordinary binary files committed to the repository.
No authenticated downloads or network access are required by Quarto or CI.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'assets/books/san-martin/IC2021_master_y_figuras.zip'
PARTS = ROOT / 'assets/books/san-martin/parts'
EXPECTED_SHA256 = '0c27bae1aeb06250c52aeb73d1e0019c75d15790eda8e8c61bf89df2a34c9e9e'
PART_COUNT = 11


def sha256(path: Path) -> str:
    d = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            d.update(chunk)
    return d.hexdigest()


def ensure_archive() -> Path:
    if ARCHIVE.is_file() and sha256(ARCHIVE) == EXPECTED_SHA256:
        return ARCHIVE
    names = [PARTS / f'part_{i:02d}.bin' for i in range(PART_COUNT)]
    missing = [str(p) for p in names if not p.is_file()]
    if missing:
        raise FileNotFoundError('Faltan componentes de la edición IC2021: ' + ', '.join(missing))
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    temp = ARCHIVE.with_name(ARCHIVE.name + '.building')
    try:
        with temp.open('wb') as dst:
            for name in names:
                with name.open('rb') as src:
                    for block in iter(lambda: src.read(1 << 20), b''):
                        dst.write(block)
        if sha256(temp) != EXPECTED_SHA256:
            raise ValueError('La reconstrucción binaria del ZIP no coincide con su SHA-256 canónico')
        os.replace(temp, ARCHIVE)
    finally:
        temp.unlink(missing_ok=True)
    return ARCHIVE


if __name__ == '__main__':
    p = ensure_archive()
    print(f'IC2021 ZIP fuente: PASS — {p.stat().st_size} bytes, SHA-256 {EXPECTED_SHA256}')
