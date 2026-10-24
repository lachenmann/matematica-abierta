import pathlib,json,numpy as np,soundfile as sf,subprocess
R=pathlib.Path(__file__).resolve().parent
rows=[]
for folder in ['raw','escucha']:
    for p in sorted((R/folder).glob('*.wav')):
        if p.name.startswith('part_'): continue
        y,sr=sf.read(p); info=sf.info(p)
        assert np.isfinite(y).all() and len(y)>0
        subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
        threshold=32767/32768 if info.subtype=='PCM_16' else 1-2**-23
        rows.append({'file':p.relative_to(R).as_posix(),'seconds':len(y)/sr,'sample_rate':sr,'channels':info.channels,'subtype':info.subtype,'peak_amplitude':float(np.abs(y).max()),'samples_at_full_scale':int(np.sum(np.abs(y)>=threshold)),'silence_below_minus60_percent':float(100*np.mean(np.abs(y)<.001)),'complete_decode':'OK'})
(R/'evidencia/audio_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print([(x['file'],x['samples_at_full_scale']) for x in rows])
