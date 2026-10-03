#!/usr/bin/env python3
from __future__ import annotations
import json, shlex, wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VOICE = ROOT / "voice-reference"
AUDIO = VOICE / "audio" / "CPM-YT-C01-V01-reference.wav"
RPP = VOICE / "CPM-YT-C01-V01-reference.rpp"
OUT = VOICE / "voice-reference-timing.json"

CANONICAL = [
"c01v01-00-start","c01v01-01-aritmetica","c01v01-02-cadena",
"c01v01-03-naturales-suma","c01v01-04-naturales-resta","c01v01-05-enteros",
"c01v01-06-racionales","c01v01-07-spoiler-supremo","c01v01-08-cuerpo",
"c01v01-09-conjunto-f","c01v01-10-clausura","c01v01-11-operaciones-primitivas",
"c01v01-12-asoc-suma","c01v01-13-neutro-suma","c01v01-14-inverso-suma",
"c01v01-15-conmut-suma","c01v01-16-asoc-producto","c01v01-17-neutro-producto",
"c01v01-18-inverso-producto","c01v01-19-cero-sin-inverso","c01v01-20-conmut-producto",
"c01v01-21-distributividad","c01v01-22-factor-comun","c01v01-23-def-cuerpo",
"c01v01-24-cuerpo-trivial","c01v01-25-trivial-operaciones","c01v01-26-excluir-trivial",
"c01v01-27-tabla-axiomas","c01v01-28-f2","c01v01-29-f2-tablas",
"c01v01-30-f2-suma","c01v01-31-f2-producto","c01v01-32-consecuencias-pendientes",
"c01v01-33-enteros-ejemplo","c01v01-34-enteros-inverso","c01v01-35-medio-no-entero",
"c01v01-36-racionales-reales","c01v01-37-cierre-siguiente-clase","c01v01-38-end",
]

def wav_duration(path: Path):
    with wave.open(str(path), "rb") as w:
        return w.getnframes()/w.getframerate(), w.getframerate(), w.getnchannels(), w.getsampwidth()*8

def parse_markers(path: Path):
    found={}
    duplicates=[]
    for raw in path.read_text(encoding="utf-8",errors="replace").splitlines():
        line=raw.strip()
        if not line.startswith("MARKER "):
            continue
        parts=shlex.split(line)
        if len(parts)>=4:
            name=parts[3].strip()
            if name in found:
                duplicates.append(name)
            found[name]=float(parts[2])
    if duplicates:
        raise SystemExit(
            "Marcadores duplicados: " + ", ".join(sorted(set(duplicates)))
        )
    return found

def main():
    found=parse_markers(RPP)
    missing=[x for x in CANONICAL if x not in found]
    if missing:
        raise SystemExit("Faltan marcadores: "+", ".join(missing))
    times=[found[x] for x in CANONICAL]
    if any(b<=a for a,b in zip(times,times[1:])):
        raise SystemExit("Marcadores fuera de orden.")
    duration,rate,channels,bits=wav_duration(AUDIO)
    if times[-1] > duration + 0.05:
        raise SystemExit("El marcador final queda fuera del WAV.")
    result={
      "id":"CPM-YT-C01-V01",
      "marker_revision":1,
      "scheme":"CPM_REAPER_SYNC_V1",
      "audio_file":"audio/"+AUDIO.name,
      "reaper_project":RPP.name,
      "audio_format":{"sample_rate_hz":rate,"channels":channels,"bit_depth":bits,"encoding":"PCM"},
      "audio_duration_seconds":round(duration,6),
      "markers":[{"name":n,"time_seconds":round(found[n],6)} for n in CANONICAL],
    }
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
