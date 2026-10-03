#!/usr/bin/env python3
"""Analiza una locución continua de Reaper para MA-CLS-C13-P01."""

from __future__ import annotations

import argparse
import json
import math
import shlex
import tempfile
import wave
from pathlib import Path

import av

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "voice-reference" / "segments.json"
DEFAULT_OUTPUT = ROOT / "voice-reference" / "voice-reference-timing.json"

CANONICAL_IDS = [
    "opening",
    "block-1",
    "bridge-1",
    "block-2",
    "bridge-2",
    "block-3",
    "closing",
]


def duration_seconds(path: Path) -> float:
    with av.open(str(path)) as container:
        if container.duration is not None:
            return float(container.duration / av.time_base)

        durations = []
        for stream in container.streams.audio:
            if stream.duration is not None and stream.time_base is not None:
                durations.append(float(stream.duration * stream.time_base))
        if durations:
            return max(durations)

    raise RuntimeError(f"No se pudo determinar la duración de {path}")


def parse_reaper_markers(rpp_path: Path) -> dict[str, float]:
    """Lee marcadores MARKER del .rpp y devuelve nombre -> segundos."""
    markers: dict[str, float] = {}

    for raw in rpp_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line.startswith("MARKER "):
            continue

        try:
            parts = shlex.split(line)
        except ValueError:
            continue

        if len(parts) < 4:
            continue

        try:
            position = float(parts[2])
        except ValueError:
            continue

        name = parts[3].strip()
        if name:
            markers[name] = position

    return markers


def normalize_markers(markers: dict[str, float]) -> dict[str, float]:
    missing = [name for name in CANONICAL_IDS if name not in markers]
    if missing:
        raise ValueError(
            "Faltan marcadores canónicos en Reaper: " + ", ".join(missing)
        )

    ordered = {name: float(markers[name]) for name in CANONICAL_IDS}
    positions = list(ordered.values())

    if any(b <= a for a, b in zip(positions, positions[1:])):
        raise ValueError("Los marcadores de Reaper no están en orden temporal estricto.")

    if "end" in markers:
        ordered["end"] = float(markers["end"])
        if ordered["end"] <= ordered["closing"]:
            raise ValueError("El marcador 'end' debe estar después de 'closing'.")

    return ordered


def analyze_continuous(audio_path: Path, rpp_path: Path, output: Path) -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    markers = normalize_markers(parse_reaper_markers(rpp_path))
    audio_duration = duration_seconds(audio_path)

    if markers["opening"] < 0:
        raise ValueError("El marcador 'opening' no puede ser negativo.")

    last_boundary = markers.get("end", audio_duration)
    if last_boundary > audio_duration + 0.05:
        raise ValueError("El último marcador queda fuera de la duración del audio.")

    target_by_id = {
        item["id"]: float(item["target_seconds"])
        for item in manifest["segments"]
    }

    rows = []
    for index, segment_id in enumerate(CANONICAL_IDS):
        start = markers[segment_id]
        if index + 1 < len(CANONICAL_IDS):
            end = markers[CANONICAL_IDS[index + 1]]
        else:
            end = last_boundary

        actual = end - start
        target = target_by_id[segment_id]

        rows.append(
            {
                "id": segment_id,
                "target_seconds": round(target, 3),
                "actual_seconds": round(actual, 3),
                "delta_seconds": round(actual - target, 3),
                "start_seconds": round(start, 3),
                "end_seconds": round(end, 3),
            }
        )

    final_hold = float(manifest["segments"][-1].get("final_hold_seconds", 0.0))
    speech_total = rows[-1]["end_seconds"] - rows[0]["start_seconds"]
    total_with_hold = speech_total + final_hold
    target_speech = sum(target_by_id.values())
    target_total = target_speech + final_hold

    result = {
        "id": manifest["id"],
        "source": "reaper-continuous-reference-voice",
        "audio_file": audio_path.name,
        "reaper_project": rpp_path.name,
        "audio_duration_seconds": round(audio_duration, 3),
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
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        audio = tmp / "reference.wav"
        rpp = tmp / "reference.rpp"
        output = tmp / "timing.json"

        write_silent_wav(audio, 7.9)

        marker_lines = []
        positions = [0.2, 1.2, 2.2, 3.2, 4.2, 5.2, 6.2]
        for i, (name, pos) in enumerate(zip(CANONICAL_IDS, positions), start=1):
            marker_lines.append(f'MARKER {i} {pos:.3f} "{name}" 0 0 1 B')
        marker_lines.append('MARKER 8 7.200 "end" 0 0 1 B')
        rpp.write_text("\n".join(marker_lines) + "\n", encoding="utf-8")

        result = analyze_continuous(audio, rpp, output)
        measured = [row["actual_seconds"] for row in result["segments"]]

        for got in measured:
            if not math.isclose(got, 1.0, abs_tol=0.002):
                raise AssertionError(got)

        if not output.exists():
            raise AssertionError("No se creó el archivo de salida")

    print("[PASS] analyze_voice_reference.py — Reaper continuous take")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Mide una toma continua de Reaper usando marcadores del .rpp."
    )
    parser.add_argument(
        "--audio",
        type=Path,
        help="Render continuo de la locución.",
    )
    parser.add_argument(
        "--rpp",
        type=Path,
        help="Proyecto .rpp de Reaper con los marcadores canónicos.",
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

    if args.audio is None or args.rpp is None:
        parser.error("--audio y --rpp son obligatorios salvo con --self-test")

    result = analyze_continuous(args.audio, args.rpp, args.output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
