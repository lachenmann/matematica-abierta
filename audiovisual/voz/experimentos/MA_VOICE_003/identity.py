"""Speaker-embedding consistency proxy; never a naturalness/accent score."""
import os
os.environ['OMP_NUM_THREADS']='6'
import pathlib,json
import numpy as np,soundfile as sf,torch,librosa
from safetensors import safe_open
from qwen_tts.core.models.configuration_qwen3_tts import Qwen3TTSSpeakerEncoderConfig
from qwen_tts.core.models.modeling_qwen3_tts import Qwen3TTSSpeakerEncoder,mel_spectrogram
R=pathlib.Path(__file__).resolve().parent
torch.set_num_threads(6)
config=json.loads((R/'models/base17/config.json').read_text())
encoder=Qwen3TTSSpeakerEncoder(Qwen3TTSSpeakerEncoderConfig(**config['speaker_encoder_config'])).float().eval()
with safe_open(str(R/'models/base17/model.safetensors'),framework='pt',device='cpu') as f:
    state={k.removeprefix('speaker_encoder.'):f.get_tensor(k).float() for k in f.keys() if k.startswith('speaker_encoder.')}
encoder.load_state_dict(state,strict=True)
@torch.inference_mode()
def emb(p):
    y,sr=sf.read(p,dtype='float32')
    if sr!=24000: y=librosa.resample(y,orig_sr=sr,target_sr=24000)
    mel=mel_spectrogram(torch.from_numpy(y).unsqueeze(0),n_fft=1024,num_mels=128,sampling_rate=24000,hop_size=256,win_size=1024,fmin=0,fmax=12000).transpose(1,2)
    e=encoder(mel)[0].numpy(); return e/np.linalg.norm(e)
reference=emb(R/'referencia/elegida_escucha.wav')
from safetensors.torch import load_file
cached=load_file(str(R/'referencia/voice_clone_prompt.safetensors'))['0_ref_spk_embedding'].numpy().reshape(-1).copy();cached/=np.linalg.norm(cached)
out={'method':'official Qwen ECAPA-TDNN speaker encoder, cosine; proxy only, not a perceptual verdict','reference_seconds':4.45,'reference_reextraction_cosine_vs_official_prompt':float(reference@cached),'modes':{}}
for mode in ['clone','direct']:
    files=sorted((R/'raw'/mode).glob('*.wav')); vectors=np.stack([emb(p) for p in files]); center=vectors.mean(0); center/=np.linalg.norm(center)
    scores=vectors@reference; consistency=vectors@center
    out['modes'][mode]={'mean_reference_cosine':float(scores.mean()),'min_reference_cosine':float(scores.min()),'mean_centroid_cosine':float(consistency.mean()),'std_reference_cosine':float(scores.std()),'clips':[{'id':p.stem,'reference_cosine':float(a),'centroid_cosine':float(b)} for p,a,b in zip(files,scores,consistency)]}
(R/'evidencia/identidad_proxy.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out),flush=True)
