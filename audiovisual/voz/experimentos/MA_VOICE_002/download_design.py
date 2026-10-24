import pathlib,json,truststore
truststore.inject_into_ssl()
from huggingface_hub import snapshot_download
R=pathlib.Path(__file__).resolve().parent
repo='Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign'
rev='5ecdb67327fd37bb2e042aab12ff7391903235d3'
snapshot_download(repo,revision=rev,local_dir=R/'models/qwen17')
(R/'evidencia/voicedesign_revision.json').write_text(json.dumps({'repo':repo,'revision':rev}),encoding='utf-8')
