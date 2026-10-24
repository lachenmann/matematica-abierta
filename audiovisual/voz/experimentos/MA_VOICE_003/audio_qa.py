import pathlib,json,subprocess
import numpy as np,soundfile as sf
R=pathlib.Path(__file__).resolve().parent; result={}
script=json.loads((R/'guion.json').read_text(encoding='utf8'))['segmentos']
for mode in ['clone','direct']:
    wav=R/'escucha'/f'NARRACION_{mode}.wav'; y,sr=sf.read(wav);info=sf.info(wav)
    assert sr==48000 and info.channels==1 and info.subtype=='PCM_24' and np.isfinite(y).all()
    subprocess.run(['ffmpeg','-v','error','-i',str(wav),'-f','null','-'],check=True)
    timeline=json.loads((R/'evidencia'/f'timing_{mode}.json').read_text(encoding='utf8'))
    assert abs(len(y)/sr-timeline['duracion_total'])<1/sr
    alignment=json.loads((R/'evidencia'/f'alineacion_{mode}.json').read_text(encoding='utf8'))
    assert len(alignment['clips'])==len(script)==18
    gaps=[]
    for cue in alignment['clips']:
        for a,b in zip(cue['words'],cue['words'][1:]):
            if b['start']-a['end']>.35:gaps.append({'id':cue['id'],'from':a['end'],'to':b['start'],'gap':b['start']-a['end'],'before':a['word'],'after':b['word']})
    speech=sum(json.loads(p.read_text(encoding='utf8'))['seconds'] for p in (R/'raw'/mode).glob('*.json'))
    result[mode]={'complete_decode':'OK','sample_rate':sr,'channels':info.channels,'subtype':info.subtype,'duration':len(y)/sr,'peak':float(np.abs(y).max()),'samples_at_full_scale':int(np.sum(np.abs(y)>=1-2**-23)),'script_word_count':sum(len(s['texto'].split()) for s in script),'spoken_wpm':60*sum(len(s['texto'].split()) for s in script)/speech,'added_pause_seconds':len(y)/sr-speech,'word_gaps_over_350ms':gaps}
    assert result[mode]['samples_at_full_scale']==0
(R/'evidencia/audio_qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=True),flush=True)
