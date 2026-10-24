import pathlib,json,math,subprocess,re,hashlib,shutil
import numpy as np,soundfile as sf
R=pathlib.Path(__file__).resolve().parent
def run(args): return subprocess.run([str(a) for a in args],check=True,capture_output=True,text=True)
def measure(p):
    s=run(['ffmpeg','-hide_banner','-i',p,'-af','loudnorm=I=-24:TP=-2:LRA=11:print_format=json','-f','null','-']).stderr
    x=json.loads(re.findall(r'\{[^{}]*\}',s,re.S)[-1]); return {k:x[k] for k in ['input_i','input_tp','input_lra']}
script=json.loads((R/'guion.json').read_text(encoding='utf8')); levels={}
for mode in ['clone','direct']:
    audio=[]; cursor=0.; cues=[]
    for i,s in enumerate(script['segmentos']):
        p=R/'raw'/mode/f'{i:02d}_{s["id"]}.wav'; y,sr=sf.read(p); assert sr==24000
        length=len(y)/sr; total=math.ceil((length+s.get('pausa',1))*60)/60
        cues.append({'id':s['id'],'texto':s['texto'],'inicio':cursor,'fin_voz':cursor+length,'fin':cursor+total,'audio':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
        audio.extend([y,np.zeros(round(total*sr)-len(y))]); cursor+=total
    raw=R/'raw'/f'NARRACION_{mode}.wav'; sf.write(raw,np.concatenate(audio),sr,subtype='FLOAT')
    level=measure(raw); gain=-24-float(level['input_i'])
    # Choose one common target below all source true-peak limits later if needed.
    levels[mode]={'raw':level,'gain_db':gain,'predicted_tp':float(level['input_tp'])+gain,'raw_path':str(raw),'duration':cursor}
    (R/'evidencia'/f'timing_{mode}.json').write_text(json.dumps({'mode':mode,'duracion_total':cursor,'cues':cues},ensure_ascii=False,indent=2),encoding='utf8')
target=min(-24.,min(-2-(float(v['raw']['input_tp'])-float(v['raw']['input_i'])) for v in levels.values()))-.1
for mode,x in levels.items():
    gain=target-float(x['raw']['input_i']); dest=R/'escucha'/f'NARRACION_{mode}.wav'
    run(['ffmpeg','-y','-v','error','-i',x['raw_path'],'-af',f'volume={gain}dB','-ar','48000','-c:a','pcm_s24le',dest])
    x.update({'target_lufs':target,'gain_db':gain,'predicted_tp':float(x['raw']['input_tp'])+gain,'measured':measure(dest),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
    segment_dir=R/'escucha/segmentos'/mode; segment_dir.mkdir(parents=True,exist_ok=True)
    for p in sorted((R/'raw'/mode).glob('*.wav')):
        run(['ffmpeg','-y','-v','error','-i',p,'-af',f'volume={gain}dB','-ar','48000','-c:a','pcm_s24le',segment_dir/p.name])
(R/'evidencia/sonoridad.json').write_text(json.dumps(levels,indent=2),encoding='utf8')
print(json.dumps(levels),flush=True)
