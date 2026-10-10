"""Normalize the seven M04 diagrams' desktop and mobile SVGs for MA-FIG-PIPE.

Removes only the XML external DTD from local, self-contained Matplotlib output;
keeps mathematical paths, labels, viewBoxes, and SVG accessibility text.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'tools' / 'figures' / 'MA-ART-0017 - Integrales - assets'
OUTPUT = ROOT / 'assets' / 'articles' / 'ma-art-0017'
OUTPUT.mkdir(parents=True, exist_ok=True)
for original in sorted(SOURCE.glob('MA-ART-0017-F*.svg')):
    text = original.read_text(encoding='utf-8')
    cleaned, count = re.subn(r'<!DOCTYPE[\s\S]*?>\n?', '', text, count=1, flags=re.I)
    if count not in (0, 1):
        raise RuntimeError(f'Unexpected DTD count in {original.name}')
    ET.fromstring(cleaned)
    (OUTPUT / original.name).write_text(cleaned, encoding='utf-8')
print('Prepared', len(list(OUTPUT.glob('MA-ART-0017-F*.svg'))), 'SVG variants')
