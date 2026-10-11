from pathlib import Path
import base64,gzip,hashlib,json
r=Path(__file__).resolve().parent
for name,row in json.loads((r/"logs-manifest.json").read_text()).items():
 data=gzip.decompress(base64.b64decode((r/(name+".gz.b64")).read_text()))
 assert len(data)==row["bytes"] and hashlib.sha256(data).hexdigest()==row["sha256"]
 (r/name).write_bytes(data)
 print(name,"EXACT_LOG_READBACK",len(data))
