import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
S=R.parents[2]/'manim/experimentos/MA_VIDEO_EXP003'
expected={'EXP003_FINAL.mp4':'3f92a9bf67dff433edb74af421278178dd89cedbe72df435adcd9e9118d3c014','EXP003_AUDIO.wav':'fdd6da5f3e0ef103428419c9d04b1f52a4e162e642e6bc88d822259bc4efe7c0','guion.json':'c0ec7c04dabe0f75826276fe0ca7a77de8033bb1576f49f958723f74416c0b36'}
rows=[]
for name,wanted in expected.items():
    p=S/name; h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
    rows.append({'path':str(p),'original_expected':wanted,'current':h.hexdigest(),'unchanged':h.hexdigest()==wanted})
for row in json.loads((R/'evidencia/originales.json').read_text()):
    h=hashlib.sha256(pathlib.Path(row['path']).read_bytes()).hexdigest()
    rows.append({'path':row['path'],'original_expected':row['sha256'],'current':h,'unchanged':h==row['sha256']})
(R/'evidencia/proteccion.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
assert all(x['unchanged'] for x in rows)
print('Originales comprobados:',len(rows))
