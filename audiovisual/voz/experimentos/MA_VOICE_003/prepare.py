import pathlib,json,hashlib,shutil,truststore
truststore.inject_into_ssl()
from huggingface_hub import HfApi,snapshot_download
R=pathlib.Path(__file__).resolve().parent; PREV=R.parent/'MA_VOICE_002'; EXP=R.parents[2]/'manim/experimentos/MA_VIDEO_EXP003'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for d in ['referencia','evidencia','models','raw/direct','raw/clone','escucha','demo']: (R/d).mkdir(exist_ok=True,parents=True)
records=[]
for folder in ['escucha','raw']:
    source=PREV/folder/'qwen17_VoiceDesign_BREVE.wav'; target=R/'referencia'/f'elegida_{folder}.wav'
    shutil.copyfile(source,target); assert sha(source)==sha(target)
    records.append({'source':str(source),'copy':str(target),'sha256':sha(target),'purpose':'exact auditioned identity reference' if folder=='escucha' else 'original unnormalized backup'})
for name in ['voicedesign_prompt.json','voicedesign_revision.json','qwen17_VoiceDesign_BREVE.json']:
    shutil.copyfile(PREV/'evidencia'/name,R/'referencia'/name)
shutil.copyfile(PREV/'generate.py',R/'referencia/MA_VOICE_002_generate_original.py')
shutil.copyfile(EXP/'guion.json',R/'guion.json')
shutil.copyfile(EXP/'generados/timing_produccion.json',R/'evidencia/timing_original.json')
info={'reference_files':records,'reference_text':json.loads((R/'referencia/voicedesign_prompt.json').read_text(encoding='utf8')),'seed':20261023,'package':'qwen-tts==0.1.1','torch':'2.14.1+cpu','dtype':'float32','attention':'eager','threads':6,'language':'Spanish','original_max_new_tokens':192,'original_sampling':'official defaults; seed set before model loading','reference_includes_trailing_silence_seconds':.45,'primary_reference':'referencia/elegida_escucha.wav','guion_sha256':sha(R/'guion.json')}
(R/'referencia/procedencia.json').write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf8')
pin=R/'evidencia/modelos.json'
if pin.exists(): models=json.loads(pin.read_text())
else:
    repo='Qwen/Qwen3-TTS-12Hz-1.7B-Base'; rev=HfApi().model_info(repo).sha
    models={'clone':{'repo':repo,'revision':rev,'local':'models/base17'},'direct':{'repo':'Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign','revision':json.loads((PREV/'evidencia/voicedesign_revision.json').read_text())['revision'],'local':'../MA_VOICE_002/models/qwen17'}}
    pin.write_text(json.dumps(models,indent=2),encoding='utf8')
snapshot_download(models['clone']['repo'],revision=models['clone']['revision'],local_dir=R/'models/base17')
direct_path=pathlib.Path(models['direct']['local']); direct_path=direct_path if direct_path.is_absolute() else R/direct_path
if not (direct_path/'model.safetensors').exists():
    models['direct']['local']='models/design17'
    snapshot_download(models['direct']['repo'],revision=models['direct']['revision'],local_dir=R/'models/design17')
    pin.write_text(json.dumps(models,indent=2),encoding='utf8')
print('Referencia exacta preservada y Base descargado',flush=True)
