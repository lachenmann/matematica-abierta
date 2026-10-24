import pathlib,json,hashlib,truststore
truststore.inject_into_ssl()
from huggingface_hub import HfApi
R=pathlib.Path(__file__).resolve().parent
models=json.loads((R/'evidencia/revisiones.json').read_text())
extra=R/'evidencia/voicedesign_revision.json'
if extra.exists(): models['qwen17']=json.loads(extra.read_text())
rows=[]
for name,x in models.items():
    info=HfApi().model_info(x['repo'],revision=x['revision'],files_metadata=True)
    for s in info.siblings:
        p=R/'models'/name/s.rfilename
        if not p.exists(): continue
        if s.lfs:
            expected=s.lfs.sha256; h=hashlib.sha256()
            with p.open('rb') as f:
                for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
            actual=h.hexdigest(); kind='LFS SHA256'
        else:
            data=p.read_bytes(); expected=s.blob_id
            actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(); kind='Git blob SHA1'
        rows.append({'model':name,'file':s.rfilename,'algorithm':kind,'expected':expected,'actual':actual,'match':expected==actual})
(R/'evidencia/verificacion_oficial.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
assert all(r['match'] for r in rows), 'Hash mismatch'
print(len(rows),'hashes coinciden con las revisiones oficiales')
