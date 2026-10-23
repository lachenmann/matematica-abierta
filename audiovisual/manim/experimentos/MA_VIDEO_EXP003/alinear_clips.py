"""Alineación auxiliar local de los clips completos: no modifica la voz."""
import json
import time
from faster_whisper import WhisperModel
from motor_voz import ROOT, GENERADOS, GUION, sha256_file


def main():
    start = time.time()
    synthesis = json.loads((GENERADOS / "tomas_definitivas.json").read_text(encoding="utf8"))
    script = json.loads(GUION.read_text(encoding="utf8"))
    assert synthesis["guion_sha256"] == sha256_file(GUION)
    model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4)
    rows = []
    for expected, clip in zip(script["segmentos"], synthesis["clips"]):
        path = ROOT / clip["path"]
        assert sha256_file(path) == clip["sha256"]
        segments, _ = model.transcribe(str(path), language="es", beam_size=5,
                                        word_timestamps=True)
        parts = [dict(start=s.start, end=s.end, text=s.text,
                      words=[dict(word=w.word, start=w.start, end=w.end,
                                  probability=w.probability) for w in s.words])
                 for s in segments]
        row = dict(id=expected["id"], inicio=0, sha256=clip["sha256"],
                   texto_esperado=expected["texto"],
                   texto_reconocido=" ".join(s["text"].strip() for s in parts),
                   segmentos=parts, words=[w for s in parts for w in s["words"]])
        rows.append(row)
        print(expected["id"], row["texto_reconocido"], flush=True)
    result = dict(modelo="Whisper small, CPU int8, 4 threads", idioma="es",
                  guion_sha256=sha256_file(GUION), segundos_ejecucion=time.time()-start,
                  alcance="ASR auxiliar; sus tiempos requieren contraste matemático y visual",
                  clips=rows)
    (GENERADOS / "alineacion_clips.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf8")


if __name__ == "__main__":
    main()
