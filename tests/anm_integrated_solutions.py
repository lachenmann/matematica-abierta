"""Check per-question disclosures against the edition's audited activity counts."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'data/anm-edition-v01-manifest.json').read_text())
totals = {'exercise': 0, 'microcontrol': 0}
for c in range(manifest['chapter_count']):
    page = next(row for row in manifest['pages'] if row['source'] == f'ANM-C{c:02d}.md')
    text = (root / page['path']).read_text()
    assert '<details class="anm-solution" open' not in text
    disclosures = re.findall(r'<details class="anm-solution">\s*<summary>(.*?)</summary>\s*(.*?)\s*</details>', text, re.S)
    expected = {'exercise': 0, 'microcontrol': 0}
    for label, body in disclosures:
        key = 'microcontrol' if 'microcontrol' in label else 'exercise'
        assert body.strip(), (c, label, 'empty answer')
        expected[key] += 1
    for key, prefix in [('exercise', 'MA-EX-'), ('microcontrol', 'MA-MIC-')]:
        ids = re.findall(r'\[\]\{#(' + prefix + r'[^}]+)\}', text)
        assert len(ids) == len(set(ids)) == expected[key], (c, key)
        totals[key] += len(ids)
    assert text.count('<details class="anm-solution">') == text.count('</details>')
    assert not re.search(r'\n{3,}|\t|\f', text)
index = (root / 'libros/para-matematicos/analisis-para-matematicos.md').read_text()
chapter_index = index.split('## Capítulos disponibles', 1)[1].split('## Referencias', 1)[0]
assert len(re.findall(r'^\d+\. ', chapter_index, re.M)) == 32
assert not re.search(r'-(ejercicios|soluciones|microcontroles)\.html|MA-BCH-', chapter_index)
assert totals['exercise'] == manifest['exercise_pairs']
assert totals['microcontrol'] == manifest['microcheck_pairs']
print('PASS: 32 chapter entries;', totals, 'paired, closed disclosures')
