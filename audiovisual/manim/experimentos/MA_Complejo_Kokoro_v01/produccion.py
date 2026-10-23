"""Construcción reproducible del prototipo existente: Kokoro → cues → Manim.

El guion canónico permanece en guion.json. Las cláusulas conservan exactamente
su contenido y fijan anclajes a partir de WAV reales, sin estimar palabras/s.
"""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import math
import os
import re
from pathlib import Path
import py_compile
import subprocess
import sys
import textwrap

from motor_voz import (ROOT, GUION, MODELS, EXPORTS, GENERADOS, generate_kokoro_clips,
                  audio_seconds, sha256_file, srt_time)

CLAUSES = [(s["id"], s["texto"]) for s in json.loads(GUION.read_text(encoding="utf8"))["segmentos"]]


def run(args, **kwargs):
    subprocess.run([str(a) for a in args], check=True, **kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--calidad", choices=["media", "alta"], default="alta")
    parser.add_argument("--solo-voz", action="store_true")
    parser.add_argument("--regenerar-voz", action="store_true")
    parser.add_argument("--solo-ensamblar", action="store_true",
                        help="Reusar el render visual de la calidad elegida; sólo si la escena no cambió")
    args = parser.parse_args()
    guion = json.loads(GUION.read_text(encoding="utf-8"))
    canonical = " ".join(s["texto"] for s in guion["segmentos"])
    assert canonical == " ".join(t for _, t in CLAUSES), "Se ha alterado el guion"
    EXPORTS.mkdir(exist_ok=True)
    GENERADOS.mkdir(exist_ok=True)
    for src in ("produccion.py", "escena.py", "motor_voz.py"):
        py_compile.compile(str(ROOT / src), doraise=True)
    model = MODELS / "kokoro-v1.0.onnx"
    voices = MODELS / "voices-v1.0.bin"
    expected = json.loads((ROOT / "modelos.json").read_text(encoding="utf8"))["archivos"]
    for path in (model, voices):
        assert sha256_file(path) == expected[path.name], f"Modelo distinto: {path.name}"
    parts = [{"id": f"cue-{i:02d}-{cue}", "texto": text}
             for i, (cue, text) in enumerate(CLAUSES)]
    clips = generate_kokoro_clips(parts, voice="em_alex", speed=0.94,
                                  refresh=args.regenerar_voz, model=model, voices=voices)
    import numpy as np
    import soundfile as sf
    # Cues en múltiplos de 1/30: misma posición en revisión 30 fps y master 60 fps.
    sr = 24000
    chunks = [np.zeros(sr, dtype=np.float32)]
    cursor = 1.0
    cues = []
    for (cue, text), clip in zip(CLAUSES, clips):
        samples, rate = sf.read(clip, dtype="float32")
        assert rate == sr and samples.ndim == 1 and len(samples) > 0
        length = len(samples) / sr
        duration = math.ceil((length + 0.32) * 30) / 30
        if cue == "cierre_global":
            duration += 1.5
        cues.append({"id": cue, "texto": text, "inicio": cursor,
                     "fin_voz": cursor + length, "fin": cursor + duration,
                     "audio": str(clip.relative_to(ROOT)), "sha256": sha256_file(clip)})
        chunks.extend([samples, np.zeros(round(duration * sr) - len(samples), dtype=np.float32)])
        cursor = round(cursor + duration, 8)
    assert len({c["id"] for c in cues}) == len(cues)
    samples = np.concatenate(chunks)
    raw = GENERADOS / "voz-24k.wav"
    sf.write(raw, samples, sr, subtype="PCM_16")
    wav = EXPORTS / "MA-COMPLEJO-001-kokoro-voz.wav"
    # No compresión dinámica: sólo resampleo sinc a 48k; no cambia la duración.
    candidate = GENERADOS / "voz-48k-candidata.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-af", "aresample=48000:resampler=soxr",
         "-c:a", "pcm_s16le", candidate])
    if wav.exists():
        assert sha256_file(wav) == sha256_file(candidate), "El WAV está protegido; conservar la toma y revisar la síntesis candidata"
    else:
        candidate.replace(wav)
    protected = sha256_file(wav)
    # El WAV sintetizado se conserva protegido. El master sonoro es un derivado
    # de dos pasadas EBU R128; se fija por hash sin alterar la toma de Kokoro.
    mastered = EXPORTS / "MA-COMPLEJO-001-narracion.wav"
    if not mastered.exists():
        measurement = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af",
            "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
            check=True, capture_output=True, text=True)
        stats = json.loads(re.findall(r"\{[^{}]+\}", measurement.stderr)[-1])
        filt = ("loudnorm=I=-16:TP=-1.5:LRA=11:linear=false:"
                f"measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:"
                f"measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:"
                f"offset={stats['target_offset']}:print_format=json")
        run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", filt,
             "-ar", "48000", "-c:a", "pcm_s16le", mastered])
        (GENERADOS / "normalizacion.json").write_text(json.dumps(stats, indent=2), encoding="utf8")
    mastered_hash = sha256_file(mastered)
    assert abs(audio_seconds(mastered)-audio_seconds(wav)) < 1/48000, "La normalización cambió la duración"
    prior_timing = GENERADOS / "timing_produccion.json"
    if prior_timing.exists():
        prior = json.loads(prior_timing.read_text(encoding="utf8"))
        if prior.get("audio_fuente_sha256"):
            assert mastered_hash == prior["audio_sha256"], "La narración final está protegida"
    timeline = {"video_id": guion["video_id"], "duracion_total": len(samples) / sr,
                "voz": "em_alex", "velocidad": 0.94, "audio_sha256": mastered_hash,
                "audio_fuente_sha256": protected,
                "guion_sha256": sha256_file(GUION), "cues": cues,
                "modelos": {p.name: sha256_file(p) for p in (model, voices)},
                "versiones": {p: importlib.metadata.version(p) for p in
                              ("manim", "kokoro-onnx", "onnxruntime", "soundfile", "numpy")}}
    visual_plan = json.loads((ROOT / "plan_visual.json").read_text(encoding="utf-8"))
    assert visual_plan.get("wav_sha256", protected) == protected, "El audio cambió: revisar los microanclajes"
    visual_cues = visual_plan["marcadores"]
    assert len({c["id"] for c in cues+visual_cues}) == len(cues+visual_cues), "Cues duplicados"
    assert all(0 <= c["inicio"] < timeline["duracion_total"] for c in visual_cues)
    timeline["marcadores_visuales"] = visual_cues
    (GENERADOS / "timing_produccion.json").write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding="utf-8")
    subtitle_cues = cues
    assert " ".join(c["texto"] for c in subtitle_cues) == canonical
    srt = "\n".join(f"{i}\n{srt_time(c['inicio'])} --> {srt_time(c['fin_voz'])}\n{textwrap.fill(c['texto'], width=52)}\n"
                    for i, c in enumerate(subtitle_cues, 1))
    (EXPORTS / "MA-COMPLEJO-001.srt").write_text(srt, encoding="utf-8")
    print("VOICE_LOCKED", protected, "duración", timeline["duracion_total"], flush=True)
    if args.solo_voz:
        return
    high = args.calidad == "alta"
    fps, resolution = (60, "1920,1080") if high else (30, "1280,720")
    if not args.solo_ensamblar:
        run([sys.executable, "-m", "manim", "-r", resolution, "--fps", fps,
             "--disable_caching", "escena.py", "MAComplejoCuadrado"], cwd=ROOT)
    rendered = ROOT / f"media/videos/escena/{1080 if high else 720}p{fps}/MAComplejoCuadrado.mp4"
    master = EXPORTS / f"MA-COMPLEJO-001-kokoro-{args.calidad}.mp4"
    # Conservar un master anterior antes de reemplazarlo en otro ciclo correctivo.
    if master.exists():
        import shutil
        shutil.copy2(master, master.with_name(master.stem + "-anterior.mp4"))
    run(["ffmpeg", "-v", "error", "-nostdin", "-y", "-i", rendered, "-i", mastered,
         "-i", EXPORTS / "MA-COMPLEJO-001.srt", "-map", "0:v", "-map", "1:a", "-map", "2:0",
         "-c:v", "copy", "-c:a", "aac", "-aac_coder", "fast", "-b:a", "192k", "-ar", "48000", "-c:s", "mov_text",
         "-metadata:s:s:0", "language=spa", "-metadata:s:a:0", "language=spa",
         "-disposition:s:0", "0",
         "-movflags", "+faststart", master])
    assert sha256_file(wav) == protected, "Se modificó el WAV protegido"
    assert sha256_file(mastered) == mastered_hash, "Se modificó la narración final"
    digest = sha256_file(master)
    master.with_suffix(".mp4.sha256").write_text(f"{digest}  {master.name}\n", encoding="ascii")
    print("MASTER", master, digest, flush=True)


if __name__ == "__main__":
    main()
