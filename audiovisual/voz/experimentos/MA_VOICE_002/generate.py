"""Local CPU synthesis; no reference audio is passed to either model."""
import os
os.environ['OMP_NUM_THREADS']='6'
os.environ['MKL_NUM_THREADS']='6'
import pathlib,json,time,threading,psutil,numpy as np,soundfile as sf,sys
R=pathlib.Path(__file__).resolve().parent
cues=json.loads((R/'fragmento.json').read_text(encoding='utf-8'))
proc=psutil.Process(); stop=False; samples=[]
def monitor():
    while not stop:
        samples.append({'t':time.time(),'rss':proc.memory_info().rss,'cpu_s':sum(proc.cpu_times()[:2]),'available':psutil.virtual_memory().available})
        if len(samples)%120==0:
            (R/'evidencia/live_resources.json').write_text(json.dumps(samples[-1]),encoding='utf-8')
        time.sleep(.25)
threading.Thread(target=monitor,daemon=True).start()
def save(name,start,load,parts,sr):
    y=np.concatenate([x for p in parts for x in (np.asarray(p).reshape(-1),np.zeros(round(.45*sr)))])
    sf.write(R/f'raw/{name}.wav',y,sr,subtype='PCM_16')
    rec={'voice':name,'generation_seconds':time.perf_counter()-start,'model_load_seconds':load,'audio_seconds':len(y)/sr,'sample_rate':sr,'peak_process_rss_bytes':max(s['rss'] for s in samples),'min_system_available_bytes':min(s['available'] for s in samples),'process_cpu_seconds':samples[-1]['cpu_s']-samples[0]['cpu_s'],'sample_interval_seconds':.25}
    (R/f'evidencia/{name}.json').write_text(json.dumps(rec,indent=2),encoding='utf-8'); print(rec,flush=True)
    (R/f'evidencia/{name}_resources.json').write_text(json.dumps(samples),encoding='utf-8')
mode=sys.argv[1]; t=time.perf_counter()
if mode=='supertonic':
    from supertonic import TTS
    model=TTS(model='supertonic-3',model_dir=R/'models/supertonic3',auto_download=False,intra_op_num_threads=6,inter_op_num_threads=1)
    load=time.perf_counter()-t
    for voice in ['M1','M2','M3']:
        samples.clear(); start=time.perf_counter(); parts=[]
        np.random.seed(20261023)
        for cue in cues:
            wav,duration=model.synthesize(cue['texto'],voice_style=model.get_voice_style(voice_name=voice),lang='es',total_steps=16,speed=1.0)
            parts.append(wav)
        save('supertonic3_'+voice,start,load,parts,model.sample_rate)
elif mode=='qwen':
    import torch
    torch.set_num_threads(6); torch.set_num_interop_threads(1); torch.manual_seed(20261023)
    from qwen_tts import Qwen3TTSModel
    model=Qwen3TTSModel.from_pretrained(str(R/'models/qwen06'),device_map='cpu',dtype=torch.float32,attn_implementation='eager')
    load=time.perf_counter()-t
    for voice in ['Ryan','Aiden']:
        samples.clear(); start=time.perf_counter(); parts=[]
        for cue in cues:
            wavs,sr=model.generate_custom_voice(text=cue['texto'],language='Spanish',speaker=voice,max_new_tokens=512)
            sf.write(R/f'raw/part_{voice}_{cue["id"]}.wav',wavs[0],sr,subtype='PCM_16')
            parts.append(wavs[0]); print(voice,cue['id'],len(wavs[0])/sr,flush=True)
        save('qwen06_'+voice,start,load,parts,sr)
else:
    available=psutil.virtual_memory().available
    (R/'evidencia/voicedesign_recursos_previos.json').write_text(json.dumps({'available_bytes':available,'minimum_available_bytes':12*2**30,'planned_dtype':'float32','max_new_tokens':192}),encoding='utf-8')
    if available < 12*2**30:
        print('VoiceDesign omitido: menos de 12 GiB disponibles para carga float32 y margen de trabajo',flush=True)
        sys.exit(0)
    import torch
    torch.set_num_threads(6); torch.set_num_interop_threads(1); torch.manual_seed(20261023)
    from qwen_tts import Qwen3TTSModel
    model=Qwen3TTSModel.from_pretrained(str(R/'models/qwen17'),device_map='cpu',dtype=torch.float32,attn_implementation='eager')
    load=time.perf_counter()-t
    (R/'evidencia/voicedesign_carga.json').write_text(json.dumps({'load_seconds':load,'peak_rss_bytes':max(s['rss'] for s in samples),'min_available_bytes':min(s['available'] for s in samples)}),encoding='utf-8')
    if psutil.virtual_memory().available < 2*2**30:
        print('VoiceDesign omitido después de cargar: margen disponible inferior a 2 GiB',flush=True)
        sys.exit(0)
    start=time.perf_counter(); samples.clear()
    text='Avancemos un índice. Ahora ene vale un millón más uno.'
    instruction='A male educational narrator, warm and calm, clear Latin American Spanish pronunciation, measured pace and neutral intonation.'
    wavs,sr=model.generate_voice_design(text=text,language='Spanish',instruct=instruction,max_new_tokens=192)
    (R/'evidencia/voicedesign_prompt.json').write_text(json.dumps({'text':text,'instruction':instruction},ensure_ascii=False,indent=2),encoding='utf-8')
    save('qwen17_VoiceDesign_BREVE',start,load,wavs,sr)
stop=True
