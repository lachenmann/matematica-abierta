"""Adapt the audited canonical tome to the website, preserving public routes."""
import argparse, hashlib, json, re, shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('canonical', type=Path)
parser.add_argument('--figures', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root/'data/cpm-tome-i-manifest.json').read_text())
rows = manifest['chapters']
labels = json.loads((root/'data/cpm-tome-i-reference-labels.json').read_text())
sources = {r['chapter']: (args.canonical/(r['chapter']+'.md')).read_text() for r in rows}
owners = {}
for row in rows:
    for anchor in re.findall(r'\{#([\w-]+)', sources[row['chapter']]):
        assert anchor not in owners, anchor
        owners[anchor] = row
for row in rows:
    source = sources[row['chapter']]
    assert hashlib.sha256(source.encode()).hexdigest() == row['source_sha256']
    body = re.sub(r'\A---\n.*?\n---\n', '', source, count=1, flags=re.S).strip()
    def reference(match):
        anchor = match[1]
        target = owners[anchor]
        label = labels[anchor].replace('[', r'\[').replace(']', r'\]')
        url = ('' if target == row else Path(target['path']).name) + '#'+anchor
        return '['+label+']('+url+')'
    body = re.sub(r'(?<![\w])@((?:sec|def|thm|lem|prp|cor|exm|exr|sol|fig|eq|tbl)-[\w-]+)', reference, body)
    body = body.replace('../90 - Assets/figures/', '../../assets/books/cpm-tomo-i/')
    i = row['visible']-1
    nav = ['[Índice del Tomo I](../para-matematicos/calculo-para-matematicos.md)']
    if i: nav.insert(0, '[← Capítulo '+str(i)+']('+Path(rows[i-1]['path']).name+')')
    if i < 19: nav.append('[Capítulo '+str(i+2)+' →]('+Path(rows[i+1]['path']).name+')')
    nav = ' · '.join(nav)
    title = json.dumps(row['title'], ensure_ascii=False)
    prereqs = '\n'.join('  - '+r['content_id'] for r in rows[:i]) or '  []'
    metadata = f'''---
title: {title}
description: "Capítulo {i+1} de Cálculo para matemáticos, Tomo I; 40 ejercicios con soluciones."
content-id: {row['content_id']}
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas: [calculo, analisis]
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: {row['date_created']}
date-modified: 2026-09-30
prerequisites:
{prereqs}
number-sections: true
number-depth: 2
number-offset: [{i}]
crossref:
  chapters: true
format:
  html:
    css: calculo-para-matematicos.css
    html-math-method:
      method: mathjax
      url: https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js
---

'''
    first_end = body.index('\n', body.index('# '))
    body = body[:first_end]+'\n\n'+nav+body[first_end:]
    (root/row['path']).write_text(metadata+body+'\n\n---\n\n'+nav+'\n')
asset_dir = root/'assets/books/cpm-tomo-i'
asset_dir.mkdir(parents=True, exist_ok=True)
figure_source=args.figures or next((p for p in [args.canonical.parent/'90 - Assets/figures',args.canonical.parent/'book/90 - Assets/figures'] if p.is_dir()),None)
assert figure_source is not None, 'pass --figures with the canonical PNG directory'
assert len(list(figure_source.glob('*.png')))==56
for image in figure_source.glob('*.png'):
    shutil.copyfile(image, asset_dir/image.name)
print('Adapted', len(rows), 'chapters; copied', len(list(asset_dir.glob('*.png'))), 'figures')
