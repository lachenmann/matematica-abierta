"""Validate real official Base model + approved prompt, without synthesizing variants."""
import threading
import time
import psutil
from ma_voice.core import ROOT, profile, write_json
from ma_voice.backends import QwenBase, model_path


def main():
    p = profile()
    process = psutil.Process()
    rows, stop = [], threading.Event()
    start = time.perf_counter()
    def monitor():
        while not stop.is_set():
            rows.append({'seconds': time.perf_counter()-start, 'rss': process.memory_info().rss,
                         'available': psutil.virtual_memory().available, 'cpu_seconds': sum(process.cpu_times()[:2])})
            stop.wait(.25)
    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()
    try:
        worker = QwenBase(p, model_path(p))
        prompt = worker.prompt[0]
        result = {'device': str(worker.model.model.device), 'dtype': str(worker.model.model.dtype),
                  'icl_mode': prompt.icl_mode, 'x_vector_only_mode': prompt.x_vector_only_mode,
                  'ref_text': prompt.ref_text, 'ref_code_shape': list(prompt.ref_code.shape),
                  'embedding_shape': list(prompt.ref_spk_embedding.shape), 'new_synthesis_calls': 0,
                  'load_seconds': time.perf_counter()-start}
    finally:
        stop.set()
        thread.join()
    result.update({'peak_rss_bytes': max(r['rss'] for r in rows), 'minimum_available_bytes': min(r['available'] for r in rows),
                   'cpu_seconds': rows[-1]['cpu_seconds']-rows[0]['cpu_seconds'], 'samples': rows})
    write_json(ROOT/'evidencia/real_backend_smoke.json', result)
    print({k: v for k, v in result.items() if k != 'samples'})


if __name__ == '__main__':
    main()
