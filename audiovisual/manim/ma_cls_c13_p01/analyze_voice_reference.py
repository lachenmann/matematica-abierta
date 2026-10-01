#!/usr/bin/env python3
"""Mide la voz de referencia de MA-CLS-C13-P01 y genera cues reales."""

from __future__ import annotations

import argparse
import json
import math
import tempfile
import wave
from pathlib import Path

import av

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "voice-reference" / "segments.json"
DEFAULT_OUTPUT = ROOT / "voice-reference" / "voice-reference-timing.json"


def duration_seconds(path: Path) -> float:
    with av.open(str(path)) as container:
        if container.duration is not None:
            # PyAV expresa container.duration en unidades de av.time_base.
            return float(container.duration / av.time_base)

        durations = []
        for stream in container.streams.audio:
            if stream.duration is not None and stream.time_base is not None:
                durations.append(float(stream.duration * stream.time_base))
        if durations:
            return max(durations)

    raise RuntimeError(f"No se pudo determinar la duración de {path}")


def locate_file(audio_dir: Path, preferred_name: str) -> Path:
    preferred = audio_dir / preferred_name
    if preferred.exists():
        return preferred

    stem = Path(preferred_name).stem
    candidates = []
    for ext in (".wav", ".flac", ".m4a", ".mp3", ".ogg"):
        p = audio_dir / f"{stem}{ext}"
        if p.exists():
            candidates.append(p)

    if len(candidates) == 1:
        return candidates[0]
    if not candidates:
        raise FileNotFoundError(
            f"Falta {preferred_name} (también se aceptan FLAC, M4A, MP3 u OGG con el mismo nombre base)."
        )
    raise RuntimeError(f"Hay múltiples archivos para {stem}: {candidates}")


def analyze(audio_dir: Path, output: Path) -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = []
    cursor = 0.0

    for item in manifest["segments"]:
        path = locate_file(audio_dir, item["filename"])
        actual = duration_seconds(path)
        target = float(item["target_seconds"])
        start = cursor
        end = start + actual
        delta = actual - target

        row = {
            "id": item["id"],
            "file": path.name,
            "target_seconds": round(target, 3),
            "actual_seconds": round(actual, 3),
            "delta_seconds": round(delta, 3),
            "start_seconds": round(start, 3),
            "end_seconds": round(end, 3),
        }
        if "final_hold_seconds" in item:
            row["final_hold_seconds"] = float(item["final_hold_seconds"])
        rows.append(row)
        cursor = end

    final_hold = float(manifest["segments"][-1].get("final_hold_seconds", 0.0))
    speech_total = cursor
    total_with_hold = speech_total + final_hold
    target_speech = sum(float(x["target_seconds"]) for x in manifest["segments"])
    target_total = target_speech + final_hold

    result = {
        "id": manifest["id"],
        "source": "recorded-reference-voice",
        "segments": rows,
        "speech_total_seconds": round(speech_total, 3),
        "final_hold_seconds": round(final_hold, 3),
        "total_seconds": round(total_with_hold, 3),
        "target_total_seconds": round(target_total, 3),
        "delta_total_seconds": round(total_with_hold - target_total, 3),
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return result


def write_silent_wav(path: Path, seconds: float, rate: int = 8000) -> None:
    frames = max(1, round(seconds * rate))
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(rate)
        wav.writeframes(b"\x00\x00" * frames)


def self_test() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        audio_dir = Path(tmp) / "audio"
        audio_dir.mkdir()
        expected = []
        for index, item in enumerate(manifest["segments"], start=1):
            seconds = 0.25 + index * 0.01
            expected.append(seconds)
            write_silent_wav(audio_dir / item["filename"], seconds)

        output = Path(tmp) / "timing.json"
        result = analyze(audio_dir, output)

        measured = [x["actual_seconds"] for x in result["segments"]]
        for got, want in zip(measured, expected):
            if not math.isclose(got, want, abs_tol=0.002):
                raise AssertionError((got, want))
        if not output.exists():
            raise AssertionError("No se creó el archivo de salida")

    print("[PASS] analyze_voice_reference.py")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "audio_dir",
        nargs="?",
        type=Path,
        help="Carpeta que contiene los siete archivos de voz.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="JSON de salida.",
    )
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    if args.audio_dir is None:
        parser.error("audio_dir es obligatorio salvo con --self-test")

    result = analyze(args.audio_dir, args.output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
