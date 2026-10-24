import json, hashlib, pathlib, shutil, urllib.request
import truststore
truststore.inject_into_ssl()
ROOT=pathlib.Path(__file__).resolve().parent
SOURCE=ROOT.parents[2]/'manim/experimentos/MA_VIDEO_EXP003'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if __name__=='__main__':
    for d in ['raw','escucha','evidencia','models']: (ROOT/d).mkdir(exist_ok=True)
    script=json.loads((SOURCE/'guion.json').read_text(encoding='utf-8'))
    # Four consecutive cues, about thirty seconds in the existing recording.
    ids=['cuenta','frontera','siguiente','salto']
    cues=[s for s in script['segmentos'] if s['id'] in ids]
    (ROOT/'fragmento.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'fragmento.txt').write_text(' '.join(s['texto'] for s in cues),encoding='utf-8')
    import soundfile as sf, numpy as np
    manifest=json.loads((SOURCE/'generados/tomas_definitivas.json').read_text(encoding='utf-8'))
    chunks=[]; originals=[]
    for clip in manifest['clips']:
        if any(clip['id'].endswith('-'+i) for i in ids):
            p=SOURCE/clip['path']; y,sr=sf.read(p); chunks.extend([y,np.zeros(int(sr*.45))]); originals.append({'path':str(p),'sha256':sha(p)})
    sf.write(ROOT/'raw/kokoro_em_alex.wav',np.concatenate(chunks),sr,subtype='PCM_16')
    (ROOT/'evidencia/originales.json').write_text(json.dumps(originals,indent=2),encoding='utf-8')
    from huggingface_hub import HfApi,snapshot_download
    revisions=ROOT/'evidencia/revisiones.json'
    result=json.loads(revisions.read_text()) if revisions.exists() else {}
    for repo,name in [('Supertone/supertonic-3','supertonic3'),('Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice','qwen06')]:
        if name not in result:
            info=HfApi().model_info(repo,files_metadata=True)
            result[name]={'repo':repo,'revision':info.sha}
        (ROOT/'evidencia/revisiones.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
        snapshot_download(repo,revision=result[name]['revision'],local_dir=ROOT/'models'/name)
    print(result,flush=True)
