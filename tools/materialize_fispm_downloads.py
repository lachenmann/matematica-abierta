#!/usr/bin/env python3
"""Reassemble the exact v04 Overleaf archive for Quarto's public resources.

The checked source stores eight small binary parts to support connector upload
limits. This is lossless packaging: each part and the assembled archive are
verified against SHA-256 before the public download is installed atomically.
"""
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    manifest = json.loads((ROOT / 'data/fispm-download-parts/v04.json').read_text())
    output = ROOT / manifest['output']
    if output.is_file() and output.stat().st_size == manifest['bytes'] and digest(output) == manifest['sha256']:
        print('FISPM v04 Overleaf download: SHA-256 verified')
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_name(output.name + '.tmp')
    try:
        with temp.open('wb') as dest:
            for part in manifest['parts']:
                path = ROOT / part['path']
                if path.stat().st_size != part['bytes'] or digest(path) != part['sha256']:
                    raise ValueError(f'Invalid archive part: {part["path"]}')
                with path.open('rb') as src:
                    for chunk in iter(lambda: src.read(1024 * 1024), b''):
                        dest.write(chunk)
        if temp.stat().st_size != manifest['bytes'] or digest(temp) != manifest['sha256']:
            raise ValueError('Assembled v04 archive does not match the approved deliverable')
        os.replace(temp, output)
        print('FISPM v04 Overleaf download: rebuilt and SHA-256 verified')
    finally:
        temp.unlink(missing_ok=True)

if __name__ == '__main__':
    main()
