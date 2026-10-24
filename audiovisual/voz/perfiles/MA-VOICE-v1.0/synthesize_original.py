"""Sequential CPU worker. Resumable, exact synthetic reference; no human cloning."""
import os
os.environ['OMP_NUM_THREADS']='6'; os.environ['MKL_NUM_THREADS']='6'
import sys,time,json,pathlib,threading,hashlib
import numpy as np,soundfile as sf,psutil
R=pathlib.Path(__file__).resolve().parent
mode=sys.argv[1]; assert mode in ['clone','direct']
P=psutil.Process(); samples=[]; finished=False
def monitor():
    while not finished:
        row={'t':time.time(),'rss':P.memory_info().rss,'cpu_s':sum(P.cpu_times()[:2]),'available':psutil.virtual_memory().available}
        samples.append(row)
        if len(samples)%40==0: (R/'evidencia'/f'live_{mode}.json').write_text(json.dumps(row))
        time.sleep(.25)
threading.Thread(target=monitor,daemon=True).start()
start=time.perf_counter()
if psutil.virtual_memory().available<10.5*2**30: raise RuntimeError('Se requieren 10.5 GiB libres antes de cargar con memoria optimizada')
import torch
torch.set_num_threads(6); torch.set_num_interop_threads(1); torch.manual_seed(20261023)
from qwen_tts import Qwen3TTSModel
config=json.loads((R/'evidencia/modelos.json').read_text())
location=pathlib.Path(config[mode]['local']); location=location if location.is_absolute() else R/location
model=Qwen3TTSModel.from_pretrained(str(location),device_map='cpu',dtype=torch.float32,attn_implementation='eager',low_cpu_mem_usage=True,offload_state_dict=True)
load={'seconds':time.perf_counter()-start,'peak_rss':max(s['rss'] for s in samples),'min_available':min(s['available'] for s in samples)}
load['actual_model_dtype']=str(model.model.dtype)
load['actual_device']=str(model.model.device)
(R/'evidencia'/f'load_{mode}.json').write_text(json.dumps(load,indent=2))
reference=json.loads((R/'referencia/procedencia.json').read_text(encoding='utf8'))
if mode=='clone':
    t=time.perf_counter()
    cache=R/'referencia/voice_clone_prompt.safetensors'
    if cache.exists():
        from safetensors.torch import load_file
        from qwen_tts.inference.qwen3_tts_model import VoiceClonePromptItem
        pc=json.loads((R/'referencia/prompt_config.json').read_text(encoding='utf8'))
        assert pc['reference_sha256']==hashlib.sha256((R/'referencia/elegida_escucha.wav').read_bytes()).hexdigest()
        profile=R/'VOICE_PROFILE.json'
        if profile.exists():
            expected_cache=json.loads(profile.read_text(encoding='utf8')).get('prompt_cache_sha256')
            if expected_cache: assert hashlib.sha256(cache.read_bytes()).hexdigest()==expected_cache, 'El prompt de identidad protegido cambió'
        data=load_file(str(cache)); prompt=[VoiceClonePromptItem(ref_code=data['0_ref_code'],ref_spk_embedding=data['0_ref_spk_embedding'],x_vector_only_mode=False,icl_mode=True,ref_text=pc['ref_text'])]
    else:
        prompt=model.create_voice_clone_prompt(ref_audio=str(R/'referencia/elegida_escucha.wav'),ref_text=reference['reference_text']['text'],x_vector_only_mode=False)
    from safetensors.torch import save_file
    tensors={}
    for i,p in enumerate(prompt):
        tensors[f'{i}_ref_spk_embedding']=p.ref_spk_embedding.cpu().contiguous()
        if p.ref_code is not None: tensors[f'{i}_ref_code']=p.ref_code.cpu().contiguous()
    if not cache.exists():
        save_file(tensors,str(cache))
        (R/'referencia/prompt_config.json').write_text(json.dumps({'x_vector_only_mode':False,'icl_mode':True,'ref_text':reference['reference_text']['text'],'create_seconds':time.perf_counter()-t,'reference_sha256':hashlib.sha256((R/'referencia/elegida_escucha.wav').read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf8')
cues=json.loads((R/'guion.json').read_text(encoding='utf8'))['segmentos']
groups=[[0]]+[list(range(i,min(i+2,len(cues)))) for i in range(1,len(cues),2)]
def reusable(p,index):
    if not p.exists() or not p.with_suffix('.json').exists(): return False
    old=json.loads(p.with_suffix('.json').read_text(encoding='utf8'))
    return (old.get('text')==cues[index]['texto'] and old.get('model_revision')==config[mode]['revision']
        and old.get('reference_sha256')==(reference['reference_files'][0]['sha256'] if mode=='clone' else None)
        and old.get('seed')==20261023 and old.get('parameters',{}).get('max_new_tokens')==768
        and hashlib.sha256(p.read_bytes()).hexdigest()==old.get('sha256'))
for group in groups:
    outputs=[R/'raw'/mode/f'{i:02d}_{cues[i]["id"]}.wav' for i in group]
    if all(reusable(p,i) for p,i in zip(outputs,group)):
        print('REUSE',mode,group,flush=True); continue
    samples.clear(); t=time.perf_counter(); cpu0=sum(P.cpu_times()[:2]); torch.manual_seed(20261023)
    texts=[cues[i]['texto'] for i in group]
    if mode=='clone':
        wavs,sr=model.generate_voice_clone(text=texts,language='Spanish',voice_clone_prompt=prompt,max_new_tokens=768)
    else:
        wavs,sr=model.generate_voice_design(text=texts,language='Spanish',instruct=reference['reference_text']['instruction'],max_new_tokens=768)
    elapsed=time.perf_counter()-t; cpu=sum(P.cpu_times()[:2])-cpu0
    for i,output,wav in zip(group,outputs,wavs):
        cue=cues[i]; y=np.asarray(wav); assert np.isfinite(y).all() and len(y)>0
        sf.write(output,y,sr,subtype='FLOAT')
        rec={'id':cue['id'],'text':cue['texto'],'mode':mode,'seed':20261023,'seconds':len(y)/sr,'generation_seconds':elapsed/len(group),'cpu_seconds':cpu/len(group),'batch_generation_seconds':elapsed,'batch_ids':group,'timing_basis':'amortized batch time; first cue single','peak_rss':max(s['rss'] for s in samples),'min_available':min(s['available'] for s in samples),'sample_rate':sr,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'parameters':{'max_new_tokens':768,'language':'Spanish','sampling':'official defaults','dtype':'float32','attention':'eager','threads':6}}
        rec.update({'model_repo':config[mode]['repo'],'model_revision':config[mode]['revision'],'reference_sha256':reference['reference_files'][0]['sha256'] if mode=='clone' else None})
        output.with_suffix('.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf8')
        print(json.dumps(rec,ensure_ascii=True),flush=True)
finished=True
print('COMPLETE',mode,flush=True)
