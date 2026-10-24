"""Copy EXP003 source and replace only voice timings/alignment in the copy."""
import pathlib,json,shutil,hashlib,subprocess,textwrap,re
import numpy as np,soundfile as sf
R=pathlib.Path(__file__).resolve().parent; S=R.parents[2]/'manim/experimentos/MA_VIDEO_EXP003'; D=R/'demo'
(D/'generados').mkdir(exist_ok=True)
shutil.copyfile(S/'escena.py',D/'escena.py'); shutil.copytree(S/'recursos',D/'recursos',dirs_exist_ok=True)
scene=D/'escena.py';scene_code=scene.read_text(encoding='utf8')
scene_code=scene_code.replace("('regla_a', .3): ('a sub', 0),", "('regla_a', .3): ('Asubn', 0),")
scene_code=scene_code.replace("first=self.mx('0',30,MUTED).move_to([-5,-.3,0])", "first=self.mx('0',30,MUTED).move_to([-5,-.7,0])")
scene.write_text(scene_code,encoding='utf8')
intro=D/'recursos/intro_canal.py'; code=intro.read_text(encoding='utf8')
code=re.sub(r'INTRO_MUSIC_FILE = \(.*?\)\nINTRO_MUSIC_GAIN_DB', 'INTRO_MUSIC_FILE = Path(__file__).with_name("intro-musica.wav")\nINTRO_MUSIC_GAIN_DB',code,flags=re.S)
intro.write_text(code,encoding='utf8')
t=json.loads((R/'evidencia/timing_clone.json').read_text(encoding='utf8'))
for c in t['cues']:
    for key in ['inicio','fin_voz','fin']: c[key]+=7
t['duracion_total']+=7; t['guion_sha256']=hashlib.sha256((R/'guion.json').read_bytes()).hexdigest()
(D/'generados/timing_produccion.json').write_text(json.dumps(t,ensure_ascii=False,indent=2),encoding='utf8')
a=json.loads((R/'evidencia/alineacion_clone.json').read_text(encoding='utf8')); a['guion_sha256']=t['guion_sha256']
(D/'generados/alineacion_clips.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
y,sr=sf.read(R/'escucha/NARRACION_clone.wav'); sf.write(D/'narracion_con_intro.wav',np.concatenate([np.zeros(7*sr),y]),sr,subtype='PCM_24')
subprocess.run(['ffmpeg','-v','error','-y','-i',str(D/'narracion_con_intro.wav'),'-i',str(D/'recursos/intro-musica.wav'),'-filter_complex','[1:a]volume=-18dB[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[out]','-map','[out]','-ar','48000','-ac','1','-c:a','pcm_s24le',str(D/'DEMO_AUDIO.wav')],check=True)
# The existing subtitle builder is reused through a small local adapter.
shutil.copyfile(S/'subtitulos.py',D/'subtitulos.py')
subtitles=D/'subtitulos.py'
subtitles.write_text(subtitles.read_text(encoding='utf8').replace("'b':'be'", "'b':'be','asubn':'a'"),encoding='utf8')
(D/'motor_voz.py').write_text('from pathlib import Path\nROOT=Path(__file__).resolve().parent\nEXPORTS=ROOT\nGENERADOS=ROOT/"generados"\ndef srt_time(t):\n m=round(t*1000);h,m=divmod(m,3600000);mi,m=divmod(m,60000);s,m=divmod(m,1000);return f"{h:02d}:{mi:02d}:{s:02d},{m:03d}"\n',encoding='utf8')
import sys
sys.path.insert(0,str(D)); from subtitulos import build
build(t)
(R/'evidencia/integracion_fuentes.json').write_text(json.dumps({'source_scene':str(S/'escena.py'),'source_sha256':hashlib.sha256((S/'escena.py').read_bytes()).hexdigest(),'copy_sha256':hashlib.sha256((D/'escena.py').read_bytes()).hexdigest(),'animations':'same geometry and animation definitions; new timing and word alignments','timing_adaptations':[{'cue':'regla_a','original_anchor':'a sub','asr_anchor':'Asubn','selected_word':0,'local_onset_seconds':2.46,'reason':'ASR merges a sub ene as a single word; avoids fractional anticipation'}],'intro_path_patch':'local protected copy of original music','original_mp4_sha256':hashlib.sha256((S/'EXP003_FINAL.mp4').read_bytes()).hexdigest()},indent=2),encoding='utf8')
manifest=R/'evidencia/integracion_fuentes.json';record=json.loads(manifest.read_text())
record['spatial_adaptations']=[{'object':'index zero label in finite-prefix diagram','from':[-5,-.3,0],'to':[-5,-.7,0],'reason':'original rectangle bottom crossed label zero; align with N baseline without changing animation timing'}]
record['animations']='original animation sequence and composition; one index label position corrected'
record['caption_adaptations']=[{'asr':'Asubn','canonical_start':'a','reason':'use real compound-word onset for a sub ene caption; retain canonical text'}]
manifest.write_text(json.dumps(record,indent=2),encoding='utf8')
print('Copia preparada para render',t['duracion_total'],flush=True)
