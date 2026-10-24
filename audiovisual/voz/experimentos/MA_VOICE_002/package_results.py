import pathlib,json,hashlib,zipfile
R=pathlib.Path(__file__).resolve().parent
required=['kokoro_em_alex','supertonic3_M1','supertonic3_M2','supertonic3_M3','qwen06_Ryan','qwen06_Aiden']
for name in required:
    assert (R/'raw'/f'{name}.wav').is_file(), name
    assert (R/'escucha'/f'{name}.wav').is_file(), name
    assert (R/'evidencia'/f'asr_{name}.json').is_file(), name
files=[p for p in R.rglob('*') if p.is_file() and not any(x in p.relative_to(R).parts for x in ['.venv','models','__pycache__']) and p.suffix!='.zip' and p.name!='entrega_sha256.json']
rows=[{'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]
manifest=R/'evidencia/entrega_sha256.json'; manifest.write_text(json.dumps(rows,indent=2),encoding='utf-8'); files.append(manifest)
archive=R/'MA_VOICE_002_ESCUCHA_Y_FUENTES.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files): z.write(p,p.relative_to(R))
with zipfile.ZipFile(archive) as z: assert z.testzip() is None
print(str(archive),archive.stat().st_size,hashlib.sha256(archive.read_bytes()).hexdigest())
