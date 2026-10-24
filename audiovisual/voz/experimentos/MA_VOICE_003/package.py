import pathlib,json,hashlib,zipfile
R=pathlib.Path(__file__).resolve().parent
for name in ['clone','direct']:
    assert (R/'escucha'/f'NARRACION_{name}.wav').is_file()
    assert len(list((R/'raw'/name).glob('*.json')))==18
def excluded(p):
    parts=p.relative_to(R).parts
    return any(x in parts for x in ['.venv','models','__pycache__','media','frames4','critical_frames','qa_previa']) or p.suffix=='.zip' or p.name in ['entrega_sha256.json','audio_mp4_decodificado.wav'] or p.name.startswith('MA_VOICE_003_DEMO_anterior_')
files=sorted(p for p in R.rglob('*') if p.is_file() and not excluded(p))
rows=[]
for p in files:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
    rows.append({'file':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':h.hexdigest()})
manifest=R/'evidencia/entrega_sha256.json';manifest.write_text(json.dumps(rows,indent=2));files.append(manifest)
out=R/'MA_VOICE_003_PROPUESTA_REPRODUCIBLE.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for p in files:z.write(p,p.relative_to(R))
with zipfile.ZipFile(out) as z: assert z.testzip() is None
print(str(out),out.stat().st_size,flush=True)
