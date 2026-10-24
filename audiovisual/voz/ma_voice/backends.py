"""CPU-only, lazy imports: load one backend per worker process."""
import json
import os
from pathlib import Path
from .core import ROOT, PROFILE_DIR, digest


def model_path(profile, override=None):
    if override:
        return Path(override).resolve()
    canonical = ROOT/'models/base17'
    return canonical if (canonical/'config.json').exists() else (PROFILE_DIR/profile['base_model']['local']).resolve()


def verify_model(location):
    import hashlib
    entries = json.loads((PROFILE_DIR/'verificacion_modelos_original.json').read_text(encoding='utf8'))
    for entry in entries:
        if entry['mode'] != 'clone':
            continue
        path = Path(location)/entry['file']
        if entry['algorithm'] == 'sha256':
            actual = digest(path)
        elif entry['algorithm'] == 'git-blob-sha1':
            actual = hashlib.sha1(b'blob '+str(path.stat().st_size).encode()+b'\0'+path.read_bytes()).hexdigest()
        else:
            raise ValueError(f'Algoritmo desconocido: {entry["algorithm"]}')
        if actual != entry['expected']:
            raise ValueError(f'Pesos/configuración alterados: {path}')


def runtime_fingerprint():
    from importlib.metadata import version
    expected = {'qwen-tts': '0.1.1', 'transformers': '4.57.3', 'torch': '2.14.1'}
    actual = {name: version(name) for name in expected}
    for name, wanted in expected.items():
        if actual[name].split('+')[0] != wanted:
            raise ValueError(f'Runtime distinto al aprobado: {name}={actual[name]} (esperado {wanted})')
    return actual


class QwenBase:
    def __init__(self, profile, location):
        os.environ['OMP_NUM_THREADS'] = str(profile['threads'])
        os.environ['MKL_NUM_THREADS'] = str(profile['threads'])
        os.environ['HF_HUB_OFFLINE'] = '1'
        import psutil
        if psutil.virtual_memory().available < 10.5 * 2**30:
            raise RuntimeError('Se requieren 10.5 GiB libres antes de cargar Base')
        verify_model(location)
        runtime_fingerprint()
        import torch
        from qwen_tts import Qwen3TTSModel
        from safetensors.torch import load_file
        from qwen_tts.inference.qwen3_tts_model import VoiceClonePromptItem
        self.torch, self.profile = torch, profile
        torch.set_num_threads(profile['threads'])
        torch.set_num_interop_threads(1)
        torch.manual_seed(profile['seed'])
        self.model = Qwen3TTSModel.from_pretrained(str(location), device_map='cpu', dtype=torch.float32,
            attn_implementation='eager', low_cpu_mem_usage=True, offload_state_dict=True)
        data = load_file(str(PROFILE_DIR/profile['prompt_cache']))
        config = json.loads((PROFILE_DIR/profile['prompt_config']).read_text(encoding='utf8'))
        if config['reference_sha256'] != profile['reference_sha256'] or config['ref_text'] != profile['reference_text']:
            raise ValueError('Prompt no corresponde a referencia aprobada')
        self.prompt = [VoiceClonePromptItem(ref_code=data['0_ref_code'], ref_spk_embedding=data['0_ref_spk_embedding'],
            x_vector_only_mode=False, icl_mode=True, ref_text=config['ref_text'])]

    def generate(self, text):
        self.torch.manual_seed(self.profile['seed'])
        waves, sr = self.model.generate_voice_clone(text=[text], language=self.profile['language'],
            voice_clone_prompt=self.prompt, max_new_tokens=self.profile['max_new_tokens_per_cue'])
        return waves[0], sr


class KokoroPreview:
    def __init__(self, model, voices):
        from kokoro_onnx import Kokoro
        self.model = Kokoro(str(model), str(voices))

    def generate(self, text):
        return self.model.create(text, voice='em_alex', speed=1.0, lang='es')
