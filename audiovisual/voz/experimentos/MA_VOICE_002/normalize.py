"""EBU R128 measurement and constant gain, preserving speech dynamics."""
import pathlib,json,subprocess,re,hashlib
R=pathlib.Path(__file__).resolve().parent
def measure(p):
    r=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','loudnorm=I=-24:TP=-2:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
    measured=json.loads(re.findall(r'\{[^{}]*\}',r.stderr,re.S)[-1])
    return {k:measured[k] for k in ['input_i','input_tp','input_lra','input_thresh']}
rows=[]
for p in sorted((R/'raw').glob('*.wav')):
    if p.name.startswith('part_'): continue
    a=measure(p); dest=R/'escucha'/p.name
    gain=-24-float(a['input_i'])
    assert float(a['input_tp'])+gain < -2, 'Insufficient peak headroom for constant gain'
    f=f'volume={gain:.6f}dB'
    subprocess.run(['ffmpeg','-v','error','-y','-i',str(p),'-af',f,'-ar','48000','-ac','1','-c:a','pcm_s24le',str(dest)],check=True)
    b=measure(dest)
    assert abs(float(b['input_i'])+24)<.05 and float(b['input_tp'])<=-2
    rows.append({'file':dest.name,'method':'constant_gain','gain_db':gain,'target_lufs':-24,'raw':a,'normalized':b,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(R/'evidencia/sonoridad.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print([(r['file'],r['normalized']['input_i'],r['normalized']['input_tp']) for r in rows])
