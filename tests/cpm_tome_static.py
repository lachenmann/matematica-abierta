"""Validate the complete CPM web release, including preserved public identities."""
from pathlib import Path
import hashlib, json, re

root = Path(__file__).resolve().parents[1]
rows = json.loads((root/'data/cpm-tome-i-manifest.json').read_text())['chapters']
assert len(rows) == 20
owners = {}
exercise_ids, solution_ids = [], []
images = set()
all_ids = []
for path in list(root.rglob('*.md')) + list(root.rglob('*.qmd')):
    if '.git' not in path.parts and not any(p.startswith('_site') for p in path.parts):
        all_ids += re.findall(r'^content-id: (MA-\w+-\d+)', path.read_text(), re.M)
assert len(all_ids) == len(set(all_ids)), 'duplicate public content ID'
for row in rows:
    path = root/row['path']
    source = path.read_text()
    assert re.search(r'^content-id: '+row['content_id']+'$', source, re.M)
    assert not re.search(r'(?<![\w])@(?:sec|def|thm|lem|prp|cor|exm|exr|sol|fig)-', source)
    assert not any(x in source for x in ['sediment://', 'sandbox:', '../90 - Assets/'])
    anchors = re.findall(r'\{#([\w-]+)', source)
    for anchor in anchors:
        assert anchor not in owners, anchor
        owners[anchor] = path
    ex = re.findall(r'\{#exr-t1-(\d+)', source)
    sol = re.findall(r'\{#sol-t1-(\d+)', source)
    assert len(ex) == len(sol) == 40 and ex == sol
    exercise_ids += ex
    solution_ids += sol
    for image in re.findall(r'../../assets/books/cpm-tomo-i/([^>\s)]+\.png)', source):
        assert (root/'assets/books/cpm-tomo-i'/image).is_file()
        images.add(image)
assert len(owners) == 2446
assert sorted(map(int, exercise_ids)) == list(range(36, 836))
assert exercise_ids == solution_ids and len(images) == 64
for row in rows:
    source = (root/row['path']).read_text()
    for file, anchor in re.findall(r'\]\(([^)#]*)#([\w-]+)\)', source):
        assert anchor in owners, anchor
        expected = (root/row['path']).parent/file if file else root/row['path']
        assert expected == owners[anchor], (row['chapter'], anchor)
hub = (root/'libros/para-matematicos/calculo-para-matematicos.md').read_text()
assert 'Publicación progresiva' not in hub
assert all('../capitulos/'+Path(r['path']).name in hub for r in rows)
print('PASS: 20 chapters, 800 matched pairs, 2446 anchors, 64 images, all reference destinations, unique public IDs')
