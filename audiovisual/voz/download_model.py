"""Explicit setup only. No model download during production synthesis."""
from ma_voice.core import profile, ROOT
from ma_voice.backends import model_path, verify_model
import truststore
truststore.inject_into_ssl()
from huggingface_hub import snapshot_download

p = profile()
location = ROOT/'models/base17'
snapshot_download(p['base_model']['repo'], revision=p['base_model']['revision'], local_dir=location)
verify_model(location)
print(location)
