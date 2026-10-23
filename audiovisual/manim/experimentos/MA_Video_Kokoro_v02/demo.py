"""MA Video Kokoro v0.2 — guion → voz española local → tiempos → Manim → MP4.

Todo es experimental y aislado. No modifica los WAV ni Reaper de las clases.
La TTS local es Kokoro ONNX, disponible mediante `uv run --with`.
"""
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


def build_timeline(guion: dict, clips: list[Path | None], mode: str) -> dict:
    segs = guion["segmentos"]
    if [s["visual"] for s in segs] != VISUALS or len(segs) != 4 or len(clips) != 4:
        raise ValueError("Se requieren cuatro escenas canónicas en orden: " + ", ".join(VISUALS))
    cursor = 0.0
    items = []
    for seg, audio in zip(segs, clips):
        seconds = audio_seconds(audio) if audio else 0.0
        dur = max(float(seg["duracion_previsualizacion"]), seconds + 1.2)
        items.append({"id": seg["id"], "visual": seg["visual"], "texto": seg["texto"],
                      "inicio": round(cursor, 4), "duracion": round(dur, 4),
                      "duracion_audio": round(seconds, 4),
                      "audio": str(audio.resolve()) if audio else None})
        cursor += dur
    return {"video_id": guion["video_id"], "modo_voz": mode, "version": "0.2",
            "qa": "PROTOTIPO_NO_AUDITADO", "segmentos": items,
            "duracion_total": round(cursor, 4)}


def write_subtitles(timeline: dict) -> None:
    blocks = []
    for i, s in enumerate(timeline["segmentos"], 1):
        end = s["inicio"] + (s["duracion_audio"] or s["duracion"] - 0.4)
        blocks.append(f"{i}\n{srt_time(s['inicio'])} --> {srt_time(end)}\n{s['texto']}\n")
    (GENERADOS / "subtitulos.srt").write_text("\n".join(blocks), encoding="utf-8")


def make_audio_only(timeline: dict, dest: Path) -> None:
    """Ensamblar el audio con silencios de sincronía usando FFmpeg."""
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg es necesario para producir la pista completa.")
    audios = [seg["audio"] for seg in timeline["segmentos"]]
    if any(p is None for p in audios):
        raise ValueError("Se requiere voz para crear un WAV ensamblado.")
    import struct
    # Construir PCM mono 24k con FFmpeg, cada WAV resampleado al vuelo.
    args = ["ffmpeg", "-y", "-v", "error"]
    filters = []
    for idx, seg in enumerate(timeline["segmentos"]):
        args.extend(["-i", seg["audio"]])
        delay_ms = round(seg["inicio"] * 1000)
        filters.append(f"[{idx}:a]aformat=channel_layouts=mono,aresample=24000,adelay={delay_ms}:all=1[a{idx}]")
    parts = "".join(f"[a{i}]" for i in range(len(audios)))
    filters.append(f"{parts}amix=inputs={len(audios)}:normalize=0:duration=longest,apad,atrim=0:{timeline['duracion_total']:.3f}[out]")
    args.extend(["-filter_complex", ";".join(filters), "-map", "[out]", "-ar", "24000",
                 "-ac", "1", "-c:a", "pcm_s16le", str(dest)])
    subprocess.run(args, check=True)


def main() -> None:
    p = argparse.ArgumentParser(description="MA Video Kokoro: secante → tangente")
    p.add_argument("--voz", choices=["kokoro", "silencio", "propia"], default="kokoro")
    p.add_argument("--timbre", choices=sorted(VOICES), default="em_alex")
    p.add_argument("--velocidad", type=float, default=0.94)
    p.add_argument("--modelo", type=Path, default=MODELS / "kokoro-v1.0.onnx")
    p.add_argument("--voces", type=Path, default=MODELS / "voices-v1.0.bin")
    p.add_argument("--calidad", choices=["baja", "media", "alta"], default="media")
    p.add_argument("--solo-plan", action="store_true")
    p.add_argument("--solo-voz", action="store_true", help="WAV completo y SRT, sin render Manim")
    p.add_argument("--regenerar-voz", action="store_true")
    a = p.parse_args()
    if not 0.75 <= a.velocidad <= 1.20:
        p.error("La velocidad recomendada está entre 0.75 y 1.20.")
    if a.solo_plan and a.voz == "kokoro":
        p.error("Para un plan sin síntesis utiliza --voz silencio --solo-plan.")
    if a.solo_voz and a.voz == "silencio":
        p.error("--solo-voz necesita un modo de narración.")
    guion = json.loads(GUION.read_text(encoding="utf-8"))
    segs = guion["segmentos"]
    clips: list[Path | None]
    if a.voz == "kokoro":
        clips = generate_kokoro_clips(segs, voice=a.timbre, speed=a.velocidad,
                                     refresh=a.regenerar_voz,
                                     model=a.modelo.resolve(), voices=a.voces.resolve())
    elif a.voz == "propia":
        clips = []
        for seg in segs:
            found = next((ROOT / "voz-propia" / (seg["id"] + ext)
                          for ext in (".wav", ".mp3", ".m4a")
                          if (ROOT / "voz-propia" / (seg["id"] + ext)).exists()), None)
            if found is None:
                raise FileNotFoundError("Se necesita voz-propia/" + seg["id"] + ".wav")
            clips.append(found)
    else:
        clips = [None] * 4
    timeline = build_timeline(guion, clips, a.voz)
    GENERADOS.mkdir(parents=True, exist_ok=True)
    (GENERADOS / "timeline.json").write_text(json.dumps(timeline, indent=2,
                                                         ensure_ascii=False), encoding="utf-8")
    write_subtitles(timeline)
    print("[OK] Timeline:", timeline["duracion_total"], "segundos")
    if a.solo_plan:
        return
    EXPORTS.mkdir(parents=True, exist_ok=True)
    if a.voz != "silencio":
        make_audio_only(timeline, EXPORTS / f"{guion['video_id']}-{a.voz}-voz.wav")
    if a.solo_voz:
        print("[OK] Voz completa y subtítulos disponibles en exports/ y generados/.")
        return
    if not shutil.which("ffmpeg"):
        raise RuntimeError("Falta FFmpeg en PATH.")
    render_flag = {"baja": "-ql", "media": "-qm", "alta": "-qh"}[a.calidad]
    env = dict(os.environ, MA_VIDEO_TIMELINE=str((GENERADOS / "timeline.json").resolve()))
    command = [sys.executable, "-m", "manim", render_flag, "--disable_caching",
               "escena.py", "MAVIZSecanteTangente"]
    print("$", " ".join(command), flush=True)
    subprocess.run(command, check=True, cwd=ROOT, env=env)
    candidates = sorted((ROOT / "media").rglob("MAVIZSecanteTangente.mp4"),
                        key=lambda f: f.stat().st_mtime, reverse=True)
    if not candidates:
        raise RuntimeError("Manim terminó pero falta el MP4 en media/.")
    mp4 = EXPORTS / f"{guion['video_id']}-{a.voz}-{a.calidad}.mp4"
    shutil.copy2(candidates[0], mp4)
    digest = sha256_file(mp4)
    (EXPORTS / (mp4.name + ".sha256")).write_text(digest + "  " + mp4.name + "\n")
    report = {"video_id": guion["video_id"], "master": str(mp4), "sha256": digest,
              "voice": a.voz, "voice_name": a.timbre if a.voz == "kokoro" else "",
              "duration": timeline["duracion_total"],
              "state": "PROTOTIPO_GENERADO - auditoría audiovisual pendiente"}
    (GENERADOS / "informe.json").write_text(json.dumps(report, indent=2,
                                                        ensure_ascii=False), encoding="utf-8")
    print("[OK] Master:", mp4)
    print("[QA] Revisar video completo antes de aprobar; aún no es PRODUCTION_READY.")


if __name__ == "__main__":
    main()
