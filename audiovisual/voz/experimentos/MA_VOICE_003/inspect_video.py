import pathlib,json,subprocess,math
from PIL import Image,ImageDraw
import numpy as np,soundfile as sf
from scipy.signal import correlate
R=pathlib.Path(__file__).resolve().parent;D=R/'demo';movie=D/'MA_VOICE_003_DEMO.mp4';Q=D/'qa'
Q.mkdir(exist_ok=True)
def run(args):return subprocess.run([str(a) for a in args],check=True,capture_output=True,text=True)
info=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',movie]).stdout)
(Q/'ffprobe.json').write_text(json.dumps(info,indent=2),encoding='utf8')
video=next(s for s in info['streams'] if s['codec_type']=='video'); audio=next(s for s in info['streams'] if s['codec_type']=='audio')
assert video['width']==1920 and video['height']==1080 and video['r_frame_rate']=='60/1' and audio['sample_rate']=='48000'
run(['ffmpeg','-v','error','-i',movie,'-f','null','-'])
run(['ffmpeg','-v','error','-y','-i',movie,'-vn','-ac','1','-ar','48000','-c:a','pcm_f32le',Q/'audio_mp4_decodificado.wav'])
reference,sr=sf.read(D/'DEMO_AUDIO.wav');decoded,_=sf.read(Q/'audio_mp4_decodificado.wav');checks=[]
for seconds in [10,90,max(10,len(reference)/sr-8)]:
    start=round(seconds*sr);size=5*sr;margin=round(.1*sr)
    a=reference[start:start+size];b=decoded[start-margin:start+size+margin]
    a=a-a.mean();b=b-b.mean();offset=int(np.argmax(correlate(b,a,mode='valid',method='fft')))-margin
    aligned=b[margin+offset:margin+offset+len(a)]
    coefficient=float(np.dot(a,aligned)/(np.linalg.norm(a)*np.linalg.norm(aligned)))
    checks.append({'window_start':seconds,'lag_seconds':offset/sr,'correlation':coefficient})
assert all(abs(x['lag_seconds'])<=1/60 and x['correlation']>.95 for x in checks)
(Q/'audio_mux_checks.json').write_text(json.dumps({'wav_duration':len(reference)/sr,'decoded_aac_duration':len(decoded)/sr,'windows':checks},indent=2),encoding='utf8')
frames=Q/'frames4';frames.mkdir(exist_ok=True)
run(['ffmpeg','-v','error','-y','-i',movie,'-vf','fps=4','-q:v','3',frames/'%05d.jpg'])
files=sorted(frames.glob('*.jpg')); sheets=[]
for start in range(0,len(files),32):
    canvas=Image.new('RGB',(2560,800),'#18202b');draw=ImageDraw.Draw(canvas)
    for j,p in enumerate(files[start:start+32]):
        x=j%8*320;y=j//8*200
        with Image.open(p) as image: canvas.paste(image.resize((320,180)),(x,y))
        draw.text((x+4,y+182),f'{(start+j)/4:.2f}s',fill='white')
    dest=Q/f'cronologia_{start//32:03d}.jpg';canvas.save(dest,quality=90);sheets.append(str(dest))
timeline=json.loads((D/'generados/timing_produccion.json').read_text(encoding='utf8'))
key=[]
for i,c in enumerate(timeline['cues']):
    t=min(c['fin_voz']-.1,c['inicio']+(c['fin_voz']-c['inicio'])*.7)
    dest=Q/f'full_{i:02d}_{c["id"]}.png';run(['ffmpeg','-v','error','-y','-ss',t,'-i',movie,'-frames:v','1',dest]);key.append({'id':c['id'],'time':t,'path':str(dest)})
events=json.loads((D/'generados/eventos_visuales.json').read_text(encoding='utf8'))
critical=[]
for e in events:
    if e['id'] not in ['formula_a','condicion_posterior','indice_siguiente','valor_a_siguiente','valor_b_salto','reglas_despues_de_N','foco_cola']:continue
    start=max(0,e['inicio']-.1); folder=Q/'critical_frames'/e['id'];folder.mkdir(parents=True,exist_ok=True)
    run(['ffmpeg','-v','error','-y','-ss',start,'-i',movie,'-t','2','-vf','fps=12','-q:v','3',folder/'%04d.jpg'])
    group=sorted(folder.glob('*.jpg'));canvas=Image.new('RGB',(1920,800),'#18202b');draw=ImageDraw.Draw(canvas)
    for j,p in enumerate(group[:24]):
        x=j%6*320;y=j//6*200
        with Image.open(p) as image:canvas.paste(image.resize((320,180)),(x,y))
        draw.text((x+4,y+182),f'{start+j/12:.3f}s',fill='white')
    dest=Q/f'critico_{e["id"]}.jpg';canvas.save(dest,quality=92)
    critical.append({'id':e['id'],'start':start,'fps':12,'frames':len(group),'sheet':str(dest)})
# Explicit cue-neighborhood evidence; review can select the critical events at full resolution.
neighbors=[]
for i,e in enumerate(events):
    for offset in [-.1,.1,.45,1.3]:
        t=max(0,min(timeline['duracion_total']-.05,e['inicio']+offset))
        dest=Q/f'cue_{i:02d}_{offset:+.2f}.jpg';run(['ffmpeg','-v','error','-y','-ss',t,'-i',movie,'-frames:v','1','-q:v','3',dest]);neighbors.append({'event':e['id'],'time':t,'path':str(dest)})
(Q/'extraccion.json').write_text(json.dumps({'complete_decode':'OK','fps_base':4,'chronology_frames':len(files),'sheets':sheets,'full_resolution':key,'critical_sequences':critical,'event_neighborhoods':neighbors,'inspection_status':'extracted, manual visual inspection must be recorded separately'},indent=2),encoding='utf8')
print('MP4 decodificado completo; hojas y fotogramas preparados',len(files),len(sheets),flush=True)
