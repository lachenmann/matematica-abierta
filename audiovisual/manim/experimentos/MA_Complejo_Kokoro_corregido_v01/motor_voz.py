"""Motor Kokoro reutilizado del prototipo v0.2, sin modificar su carpeta."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import wave

ROOT = Path(__file__).resolve().parent
GUION = ROOT / "guion.json"
GENERADOS = ROOT / "generados"
AUDIOS = GENERADOS / "audio"
EXPORTS = ROOT / "exports"
MODELS = ROOT / "models"
if not all((MODELS / f).is_file() for f in ("kokoro-v1.0.onnx", "voices-v1.0.bin")):
    shared_models = ROOT.parent / "MA_Video_Kokoro_v02" / "models"
    if all((shared_models / f).is_file() for f in ("kokoro-v1.0.onnx", "voices-v1.0.bin")):
        MODELS = shared_models
VOICES = {"em_alex", "em_santa", "ef_dora"}
VISUALS = ["curva", "secante", "aproximacion", "tangente"]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def audio_seconds(path: Path) -> float:
    if path.suffix.lower() == ".wav":
        with wave.open(str(path), "rb") as w:
            return w.getnframes() / w.getframerate()
    if shutil.which("ffprobe") is None:
        raise RuntimeError("Necesitas FFmpeg/ffprobe para archivos mp3 y m4a.")
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
                       check=True, text=True, capture_output=True)
    return float(p.stdout.strip())


def voice_signature(text: str, voice: str, speed: float, model: Path) -> str:
    payload = {"text": text, "voice": voice, "speed": speed,
               "model_size": model.stat().st_size, "model_name": model.name,
               "backend": "kokoro-onnx 0.6.1", "lang": "es"}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def check_kokoro_models(model: Path, voices: Path) -> None:
    if not model.is_file() or not voices.is_file():
        raise FileNotFoundError(
            "Faltan los pesos de Kokoro. Ejecuta primero .\\setup-kokoro.ps1 "
            "desde PowerShell; descargarás los modelos una sola vez."
        )
    if model.stat().st_size < 80_000_000 or voices.stat().st_size < 20_000_000:
        raise ValueError("Archivos de Kokoro demasiado pequeños: descarga incompleta.")


def generate_kokoro_clips(segments: list[dict], *, voice: str, speed: float,
                          refresh: bool, model: Path, voices: Path) -> list[Path]:
    check_kokoro_models(model, voices)
    try:
        from kokoro_onnx import Kokoro
        import soundfile as sf
    except ImportError as exc:
        raise RuntimeError(
            "Falta kokoro-onnx / soundfile. Ejecuta la maqueta con .\\producir-kokoro.ps1 "
            "o usa: uv run --with kokoro-onnx==0.6.1 --with soundfile python demo.py --voz kokoro"
        ) from exc
    AUDIOS.mkdir(parents=True, exist_ok=True)
    ready = []
    tasks = []
    for seg in segments:
        wav = AUDIOS / f"{seg['id']}-{voice}.wav"
        meta = AUDIOS / f"{seg['id']}-{voice}.json"
        sig = voice_signature(seg["texto"], voice, speed, model)
        if not refresh and wav.exists() and meta.exists():
            try:
                cached = json.loads(meta.read_text(encoding="utf-8"))
                if cached.get("signature") == sig and cached.get("sha256") == sha256_file(wav):
                    ready.append(wav)
                    continue
            except (ValueError, OSError):
                pass
        ready.append(wav)
        tasks.append((seg, wav, meta, sig))
    if not tasks:
        print("[CACHE] Voz Kokoro ya generada; se reutilizan los WAV.")
        return ready
    print("[KOKORO] Cargando modelo local. Voz:", voice, "idioma: es")
    engine = Kokoro(str(model), str(voices))
    try:
        for seg, wav, meta, sig in tasks:
            print("[KOKORO]", seg["id"], "->", wav.name, flush=True)
            samples, sr = engine.create(seg["texto"], voice=voice, speed=speed, lang="es")
            if sr <= 0 or len(samples) == 0:
                raise RuntimeError("Kokoro devolvió audio vacío para " + seg["id"])
            tmp = wav.with_name(wav.stem + ".partial.wav")
            sf.write(str(tmp), samples, sr, subtype="PCM_16")
            tmp.replace(wav)
            meta.write_text(json.dumps({"signature": sig, "voice": voice, "lang": "es",
                                       "speed": speed, "duration": audio_seconds(wav),
                                       "sha256": sha256_file(wav)}, indent=2), encoding="utf-8")
    finally:
        # La API de Kokoro usa un archivo NPZ abierto en algunas versiones.
        close = getattr(getattr(engine, "voices", None), "close", None)
        if callable(close):
            close()
    return ready


def srt_time(value: float) -> str:
    ms = round(max(0.0, value) * 1000)
    hh, rem = divmod(ms, 3_600_000)
    mm, rem = divmod(rem, 60_000)
    ss, mmm = divmod(rem, 1000)
    return f"{hh:02d}:{mm:02d}:{ss:02d},{mmm:03d}"
