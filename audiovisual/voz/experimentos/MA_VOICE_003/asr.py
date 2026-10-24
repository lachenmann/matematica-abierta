import pathlib,json,truststore,hashlib,time
truststore.inject_into_ssl()
from huggingface_hub import snapshot_download
from faster_whisper import WhisperModel
R=pathlib.Path(__file__).resolve().parent
path=snapshot_download('Systran/faster-whisper-small',revision='536b0662742c02347bc0e980a01041f333bce120',allow_patterns=['config.json','preprocessor_config.json','model.bin','tokenizer.json','vocabulary.*'])
model=WhisperModel(path,device='cpu',compute_type='int8',cpu_threads=4)
for mode in ['clone','direct']:
    clips=[]
    for p in sorted((R/'raw'/mode).glob('*.wav')):
        dest=R/'evidencia'/f'asr_{mode}_{p.stem}.json'; digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if dest.exists() and json.loads(dest.read_text())['sha256']==digest: rec=json.loads(dest.read_text(encoding='utf8'))
        else:
            segments,_=model.transcribe(str(p),language='es',beam_size=5,word_timestamps=True)
            segments=list(segments)
            rec={'id':p.stem[3:],'sha256':digest,'text':' '.join(s.text.strip() for s in segments),'words':[{'word':w.word,'start':w.start,'end':w.end,'probability':w.probability} for s in segments for w in s.words]}
            dest.write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf8')
        clips.append(rec); print(mode,rec['id'],rec['text'],flush=True)
    (R/'evidencia'/f'alineacion_{mode}.json').write_text(json.dumps({'clips':clips},ensure_ascii=False,indent=2),encoding='utf8')
