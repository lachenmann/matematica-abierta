import pathlib,json,hashlib,truststore,shutil
truststore.inject_into_ssl()
from huggingface_hub import HfApi
R=pathlib.Path(__file__).resolve().parent; cfg=json.loads((R/'evidencia/modelos.json').read_text()); rows=[]
def hashfile(p,alg='sha256'):
    h=hashlib.new(alg)
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
    return h.hexdigest()
for name,x in cfg.items():
    local=pathlib.Path(x['local']); local=local if local.is_absolute() else R/local
    info=HfApi().model_info(x['repo'],revision=x['revision'],files_metadata=True)
    for f in info.siblings:
        p=local/f.rfilename
        if not p.is_file():continue
        if f.lfs: expected=f.lfs.sha256; actual=hashfile(p); alg='sha256'
        else:
            b=p.read_bytes();actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();expected=f.blob_id;alg='git-blob-sha1'
        rows.append({'mode':name,'file':f.rfilename,'expected':expected,'actual':actual,'match':expected==actual,'algorithm':alg})
(R/'evidencia/verificacion_modelos.json').write_text(json.dumps(rows,indent=2));assert all(x['match'] for x in rows)
previous=R.parent/'MA_VOICE_002'; original=R.parents[2]/'manim/experimentos/MA_VIDEO_EXP003'
protection=[]
for folder in ['escucha','raw']:
    src=previous/folder/'qwen17_VoiceDesign_BREVE.wav';copy=R/'referencia'/f'elegida_{folder}.wav'
    protection.append({'source':str(src),'copy':str(copy),'unchanged':hashfile(src)==hashfile(copy),'sha256':hashfile(src)})
for name,expected in {'EXP003_FINAL.mp4':'3f92a9bf67dff433edb74af421278178dd89cedbe72df435adcd9e9118d3c014','guion.json':'c0ec7c04dabe0f75826276fe0ca7a77de8033bb1576f49f958723f74416c0b36','EXP003_AUDIO.wav':'fdd6da5f3e0ef103428419c9d04b1f52a4e162e642e6bc88d822259bc4efe7c0'}.items():
    actual=hashfile(original/name);protection.append({'source':str(original/name),'expected':expected,'sha256':actual,'unchanged':actual==expected})
(R/'evidencia/proteccion.json').write_text(json.dumps(protection,indent=2));assert all(x['unchanged'] for x in protection)
(R/'licencias').mkdir(exist_ok=True)
shutil.copyfile(R/'models/base17/README.md',R/'licencias/QWEN_BASE_MODEL_CARD.md')
direct=pathlib.Path(cfg['direct']['local']);direct=direct if direct.is_absolute() else R/direct
shutil.copyfile(direct/'README.md',R/'licencias/QWEN_VOICEDESIGN_MODEL_CARD.md')
shutil.copyfile(previous/'QWEN_LICENSE.txt',R/'licencias/QWEN_APACHE_2.txt')
print('Verificados',len(rows),'archivos de modelos y originales protegidos')
