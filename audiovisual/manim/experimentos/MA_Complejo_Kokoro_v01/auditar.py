"""Evidencia técnica y extracción del MP4 real; no sustituye la inspección."""
import argparse
import json
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw
import numpy as np
import soundfile as sf
from motor_voz import ROOT, EXPORTS, GENERADOS, sha256_file


def run(args):
    return subprocess.run([str(a) for a in args], check=True, capture_output=True)


def sheet(frames, dest, cols=5, rows=4):
    for offset in range(0, len(frames), cols*rows):
        page = Image.new("RGB", (cols*384, rows*240), "#151923")
        draw = ImageDraw.Draw(page)
        for k, (path, seconds) in enumerate(frames[offset:offset+cols*rows]):
            im = Image.open(path).convert("RGB").resize((384, 216))
            x, y = k % cols * 384, k // cols * 240
            page.paste(im, (x, y))
            draw.text((x+7, y+220), f"{seconds:06.2f} s", fill="white")
        page.save(dest / f"lamina-{offset//(cols*rows)+1:02d}.jpg", quality=94)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--calidad", default="alta")
    p.add_argument("--fps", type=int, default=4)
    p.add_argument("--nombre", default="final")
    a = p.parse_args()
    master = EXPORTS / f"MA-COMPLEJO-001-kokoro-{a.calidad}.mp4"
    dest = EXPORTS / ("qa-"+a.nombre)
    dest.mkdir(exist_ok=True)
    timeline = json.loads((GENERADOS / "timing_produccion.json").read_text(encoding="utf8"))
    probe = json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", master]).stdout)
    (dest / "ffprobe.json").write_text(json.dumps(probe, indent=2), encoding="utf8")
    video = next(s for s in probe["streams"] if s["codec_type"] == "video")
    if a.calidad == "alta":
        assert (video["width"], video["height"], video["r_frame_rate"]) == (1920, 1080, "60/1")
    run(["ffmpeg", "-v", "error", "-y", "-i", master, "-vf", f"fps={a.fps},scale=640:-1", dest / "base-%04d.jpg"])
    sheet([(f, i/a.fps) for i, f in enumerate(sorted(dest.glob("base-*.jpg")))], dest)
    # Cuatro observaciones alrededor de cada cue; además de la pasada cronológica.
    cue_dir = dest / "cues"
    cue_dir.mkdir(exist_ok=True)
    frames = []
    for cue in timeline["cues"] + timeline.get("marcadores_visuales", []):
        for i, delta in enumerate((-.10, .10, .45, 1.30)):
            t = cue["inicio"] + delta
            file = cue_dir / f"{cue['id']}-{i}.png"
            run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.5f}", "-i", master, "-frames:v", "1", file])
            frames.append((file, t))
    sheet(frames, cue_dir, cols=4, rows=4)
    run(["ffmpeg", "-v", "error", "-y", "-i", master, "-ss", "33.8", "-vf",
         "subtitles=exports/MA-COMPLEJO-001.srt:force_style='Fontsize=18,MarginV=12'",
         "-frames:v", "1", dest / "subtitulos-33s.png"])
    cues = {c['id']: c for c in timeline['cues']}
    for name in ('deformacion','giro','local','critico'):
        region = dest / name
        region.mkdir(exist_ok=True)
        start = cues[name]['inicio']
        end = min(cues[name]['fin'], start+5)
        run(['ffmpeg','-v','error','-y','-ss',start,'-i',master,'-t',end-start,
             '-vf','fps=12,scale=640:-1',region/'crit-%04d.jpg'])
        sheet([(f,start+i/12) for i,f in enumerate(sorted(region.glob('crit-*.jpg')))],region)
    # Decodificar TODO el master; una miniatura o ffprobe no detecta corrupción.
    run(["ffmpeg", "-v", "error", "-i", master, "-f", "null", "-"])
    decoded = dest / "audio-master.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", master, "-vn", "-ac", "1", "-ar", "48000", decoded])
    reference, sr = sf.read(EXPORTS / "MA-COMPLEJO-001-narracion.wav")
    actual, _ = sf.read(decoded)
    correlations = []
    for cue in timeline["cues"]:
        start = round((cue["inicio"]+.15)*sr)
        stop = min(round(cue["fin_voz"]*sr), start+sr)
        x, y = reference[start:stop], actual[start:stop]
        # Retardo estimado de ±10 ms; permite comprobar deriva al final del video.
        from scipy.signal import correlate, correlation_lags
        cx = correlate(y, x, mode="full", method="fft")
        lags = correlation_lags(len(y), len(x), mode="full")
        mask = abs(lags) <= 480
        lag = int(lags[mask][np.argmax(cx[mask])])
        correlations.append({"cue":cue["id"], "t":start/sr,
                             "correlacion": float(np.corrcoef(x,y)[0,1]), "retardo_muestras":lag})
    result = {"master":str(master), "sha256":sha256_file(master),
              "wav_sha256":sha256_file(EXPORTS / "MA-COMPLEJO-001-narracion.wav"),
              "duracion_wav":len(reference)/sr, "duracion_audio_aac":len(actual)/sr,
              "pico_wav_dbfs":float(20*np.log10(np.max(abs(reference)))),
              "muestras_clipping":int(np.sum(abs(reference)>=.9999)),
              "audio_correlaciones":correlations, "decodificacion_completa":"OK"}
    assert result["wav_sha256"] == timeline["audio_sha256"]
    if timeline.get("audio_fuente_sha256"):
        assert sha256_file(EXPORTS / "MA-COMPLEJO-001-kokoro-voz.wav") == timeline["audio_fuente_sha256"]
    assert all(c["correlacion"]>.98 and abs(c["retardo_muestras"])<48 for c in correlations)
    (dest / "validacion.json").write_text(json.dumps(result, indent=2), encoding="utf8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
