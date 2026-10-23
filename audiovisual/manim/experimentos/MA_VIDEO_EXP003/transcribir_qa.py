"""Comprobación local de inteligibilidad; nunca declara escucha perceptual."""
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from faster_whisper import WhisperModel
from motor_voz import ROOT, GUION, EXPORTS, sha256_file

import sys
master = (EXPORTS / "EXP003_NARRACION.wav" if "--voz" in sys.argv else ROOT / "EXP003_FINAL.mp4")
model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4)
segments, info = model.transcribe(str(master), language="es", beam_size=5, word_timestamps=True)
rows = [{"start": s.start, "end": s.end, "text": s.text,
         "words": [{"word": w.word, "start": w.start, "end": w.end,
                    "probability": w.probability} for w in s.words]} for s in segments]
expected = " ".join(s["texto"] for s in json.loads(GUION.read_text(encoding="utf8"))["segmentos"])
actual = " ".join(s["text"].strip() for s in rows)


def tokens(text):
    text = re.sub(r'\b(uno más|dos) y\b', r'\1 i', text.lower())
    text = text.replace('pre imágenes', 'preimágenes')
    text = re.sub(r"\bdoble u\b", "dobleu", text.lower())
    words = re.findall(r"[\wáéíóúñ]+", text.lower())
    mapping = {"x": "equis", "0": "cero", "1": "uno", "2": "dos", "hache": "h", "z": "zeta", "w": "dobleu", "i": "i"}
    return [mapping.get(w, w) for w in words]


matcher = SequenceMatcher(None, tokens(expected), tokens(actual), autojunk=False)
diff = [{"op": op, "esperado": tokens(expected)[i:j], "reconocido": tokens(actual)[k:l]}
        for op, i, j, k, l in matcher.get_opcodes() if op != "equal"]
dest = EXPORTS / ("qa-voz" if "--voz" in sys.argv else "qa-final")
dest.mkdir(exist_ok=True)
report = {"master_sha256": sha256_file(master), "modelo": "Whisper small, int8, CPU",
          "normalizaciones": "z/zeta, x/equis, dígitos; homofonía i/y sólo en uno más i y dos i; pre imágenes/preimágenes",
          "texto_esperado": expected, "texto_reconocido": actual,
          "diferencias_normalizadas": diff, "segmentos": rows,
          "alcance": "Reconocimiento automático del sonido decodificado; no escucha humana"}
(dest / "transcripcion-asr.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
print(actual)
print("Diferencias:", diff)
