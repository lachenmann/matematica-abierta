"""Síntesis local por fragmentos del guion original de EXP003."""
import importlib.metadata
import hashlib
import json
import time
from motor_voz import (GUION, ROOT, GENERADOS, MODELS, generate_kokoro_clips,
                       audio_seconds, sha256_file)


def main():
    start = time.time()
    script_bytes = GUION.read_bytes()
    data = json.loads(script_bytes)
    script_sha = hashlib.sha256(script_bytes).hexdigest()
    expected = json.loads((ROOT / "modelos.json").read_text(encoding="utf8"))["archivos"]
    model, voices = MODELS / "kokoro-v1.0.onnx", MODELS / "voices-v1.0.bin"
    for path in (model, voices):
        assert sha256_file(path) == expected[path.name]
    parts = [{"id": f"cue-{i:02d}-{seg['id']}", "texto": seg["texto"]}
             for i, seg in enumerate(data["segmentos"])]
    clips = generate_kokoro_clips(parts, voice="em_alex", speed=.94, refresh=False,
                                  model=model, voices=voices)
    report = dict(voz="em_alex", idioma="es", velocidad=.94,
                  guion_sha256=script_sha, segundos_ejecucion=time.time()-start,
                  modelos={p.name: sha256_file(p) for p in (model, voices)},
                  versiones={name: importlib.metadata.version(name) for name in
                             ("kokoro-onnx", "onnxruntime", "soundfile")},
                  clips=[dict(id=s["id"], path=str(p.relative_to(ROOT)),
                              segundos=audio_seconds(p), sha256=sha256_file(p))
                         for s, p in zip(parts, clips)])
    report["segundos_voz"] = sum(p["segundos"] for p in report["clips"])
    GENERADOS.mkdir(exist_ok=True)
    target = GENERADOS / ("tomas_definitivas.json" if (GENERADOS / "sintesis_inicial.json").exists()
                           else "sintesis_inicial.json")
    target.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
