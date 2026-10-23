"""Comprobación local de inteligibilidad; nunca declara escucha perceptual."""
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from faster_whisper import WhisperModel
from demo import ROOT, GUION, EXPORTS, sha256_file

master = EXPORTS / "MA-VIZ-SECANTE-001-kokoro-alta.mp4"
model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(str(master), language="es", beam_size=5, word_timestamps=True)
rows = [{"start": s.start, "end": s.end, "text": s.text,
         "words": [{"word": w.word, "start": w.start, "end": w.end,
                    "probability": w.probability} for w in s.words]} for s in segments]
expected = " ".join(s["texto"] for s in json.loads(GUION.read_text(encoding="utf8"))["segmentos"])
actual = " ".join(s["text"].strip() for s in rows)


def tokens(text):
    words = re.findall(r"[\wáéíóúñ]+", text.lower())
    mapping = {"x": "equis", "1": "uno", "2": "dos", "hache": "h"}
    return [mapping.get(w, w) for w in words]


matcher = SequenceMatcher(None, tokens(expected), tokens(actual), autojunk=False)
diff = [{"op": op, "esperado": tokens(expected)[i:j], "reconocido": tokens(actual)[k:l]}
        for op, i, j, k, l in matcher.get_opcodes() if op != "equal"]
dest = EXPORTS / "qa-final"
dest.mkdir(exist_ok=True)
report = {"master_sha256": sha256_file(master), "modelo": "Whisper small, int8, CPU",
          "texto_esperado": expected, "texto_reconocido": actual,
          "diferencias_normalizadas": diff, "segmentos": rows,
          "alcance": "Reconocimiento automático del sonido decodificado; no escucha humana"}
(dest / "transcripcion-asr.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
print(actual)
print("Diferencias:", diff)
