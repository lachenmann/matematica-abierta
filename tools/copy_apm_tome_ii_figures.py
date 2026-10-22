#!/usr/bin/env python3
"""Derive standalone web SVG from canonical SVG; preserve drawing elements."""
from pathlib import Path
import re,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1]
for p in (r/'data/apm-tome-ii-figure-sources').glob('*.svg'):
 raw=p.read_bytes();clean=re.sub(rb'<!DOCTYPE[^>]*>\s*',b'',raw,flags=re.S)
 assert ET.tostring(ET.fromstring(raw))==ET.tostring(ET.fromstring(clean)),p.name
 out=r/'assets/books/apm-tomo-ii'/p.name;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(clean)
