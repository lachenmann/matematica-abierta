"""Auxiliary reading check. ASR is not a perceptual listening evaluation."""
import pathlib,json,time
import truststore
truststore.inject_into_ssl()
from faster_whisper import WhisperModel
R=pathlib.Path(__file__).resolve().parent
pin=R/'evidencia/asr_model_revision.json'
source='small'
if pin.exists():
    from huggingface_hub import snapshot_download
    x=json.loads(pin.read_text())
    source=snapshot_download(x['repo'],revision=x['revision'],allow_patterns=['config.json','preprocessor_config.json','model.bin','tokenizer.json','vocabulary.*'])
model=WhisperModel(source,device='cpu',compute_type='int8',cpu_threads=4)
for p in sorted((R/'raw').glob('*.wav')):
    if p.name.startswith('part_'): continue
    dest=R/'evidencia'/('asr_'+p.stem+'.json')
    if dest.exists(): continue
    t=time.perf_counter()
    seg,info=model.transcribe(str(p),language='es',beam_size=5,word_timestamps=True)
    rows=[{'start':s.start,'end':s.end,'text':s.text,'words':[{'word':w.word,'start':w.start,'end':w.end,'p':w.probability} for w in s.words]} for s in seg]
    dest.write_text(json.dumps({'file':p.name,'segments':rows,'seconds':time.perf_counter()-t},ensure_ascii=False,indent=2),encoding='utf-8')
    print(p.name,' '.join(s['text'] for s in rows),flush=True)
