import json,pathlib,hashlib,importlib.metadata as m,shutil,platform,psutil
R=pathlib.Path(__file__).resolve().parent
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
    return h.hexdigest()
rows=[]
for p in sorted((R/'models').rglob('*')):
    if p.is_file() and '.cache' not in p.parts:
        rows.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
(R/'evidencia/modelos_sha256.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
lic=R/'licencias'; lic.mkdir(exist_ok=True)
for model in ['supertonic3','qwen06','qwen17']:
    for name in ['LICENSE','README.md']:
        p=R/'models'/model/name
        if p.exists(): shutil.copyfile(p,lic/f'{model}_{name}')
deps=[]
for name in ['supertonic','qwen-tts','torch','torchaudio','onnxruntime','faster-whisper']:
    d=m.distribution(name); deps.append({'name':name,'version':d.version,'license':d.metadata.get('License'),'license_expression':d.metadata.get('License-Expression'),'home':d.metadata.get('Home-page'),'project_urls':d.metadata.get_all('Project-URL')})
    for f in d.files or []:
        if 'license' in str(f).lower() and pathlib.Path(str(f)).name.lower().startswith('license'):
            dest=lic/(name+'_'+pathlib.Path(str(f)).name)
            if not dest.exists(): shutil.copyfile(d.locate_file(f),dest)
(R/'evidencia/dependencias.json').write_text(json.dumps(deps,indent=2),encoding='utf-8')
(R/'evidencia/sistema.json').write_text(json.dumps({'platform':platform.platform(),'python':platform.python_version(),'ram_total':psutil.virtual_memory().total,'ram_available_at_inventory':psutil.virtual_memory().available},indent=2),encoding='utf-8')
print(len(rows),'archivos de modelos inventariados')
