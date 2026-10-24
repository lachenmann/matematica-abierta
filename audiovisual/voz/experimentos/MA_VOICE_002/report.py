import pathlib,json,html,soundfile as sf,re,unicodedata,difflib
R=pathlib.Path(__file__).resolve().parent
expected=(R/'fragmento.txt').read_text(encoding='utf-8')
labels={'kokoro_em_alex':'Kokoro · em_alex (referencia)','supertonic3_M1':'Supertonic 3 · M1','supertonic3_M2':'Supertonic 3 · M2','supertonic3_M3':'Supertonic 3 · M3','qwen06_Ryan':'Qwen 0.6B · Ryan','qwen06_Aiden':'Qwen 0.6B · Aiden','qwen17_VoiceDesign_BREVE':'Qwen 1.7B · VoiceDesign (prueba breve)'}
levels={x['file']:x for x in json.loads((R/'evidencia/sonoridad.json').read_text())}
lines=['# MA-VOICE-002 — informe técnico y recomendación provisional','',
'Experimento local independiente de Manim. Rama `codex/ma-voice-002`. Fecha: 23 de octubre de 2026. No se han publicado audios ni modificado los MP4, las tomas originales o la instalación canónica de Manim.','',
'## Equipo y método','',
'Windows 11 Pro, Intel Core i5-9400 (6 núcleos/6 hilos), 31,85 GiB físicos, Intel UHD 630. Inferencia CPU, seis hilos, float32 en Qwen, ONNX Runtime en Supertonic. No se usa CUDA. La memoria disponible inicial era aproximadamente 13 GiB porque el equipo tenía otras aplicaciones abiertas.','',
'Se utilizan cuatro intervenciones consecutivas del Experimento 003: `cuenta`, `frontera`, `siguiente`, `salto`. Kokoro conserva las tomas em_alex ya producidas a velocidad 0,94. Cada motor recibe exactamente el mismo texto hablado por intervención; se añaden 0,45 s entre intervenciones y al final. Esta segmentación hace comparable el texto y permite observar cambios de timbre entre frases. El ritmo interno de cada voz se conserva.','',
'> '+expected,'',
'Supertonic: voces masculinas predefinidas M1, M2, M3, idioma `es`, 16 pasos, velocidad 1,0. Qwen 0.6B: Ryan y Aiden, idioma `Spanish`, parámetros de muestreo oficiales y semilla inicial 20261023; máximo 512 tokens por intervención. Sus perfiles originales están descritos como voces inglesas por el proveedor; aquí se prueba su síntesis cruzada al español. No admite instrucciones de estilo en el modelo 0.6B: no se añadió una instrucción que el motor ignoraría. No se proporciona ningún audio de referencia a los nuevos motores.','',
'Sonoridad: medición EBU R128 y ganancia constante por archivo, objetivo −24 LUFS; WAV mono 48 kHz PCM de 24 bits en `escucha/`. Se verifican los LUFS y los picos de cada copia. Este nivel deja al menos 2 dB de margen de pico verdadero en todas las voces y permite conservar la dinámica sin compresión ni limitación. Una prueba previa a −20 LUFS podía activar limitación sobre Kokoro y fue descartada. Los originales se conservan en `raw/`. No se igualan duraciones ni se modifica la altura.','',
'Los tiempos son observaciones de este equipo en uso, no un benchmark de laboratorio. El proceso se muestrea cada 0,25 s; RAM es el máximo RSS observado durante síntesis, no la memoria del archivo de pesos ni el pico durante carga. CPU % se expresa sobre los seis núcleos: segundos de CPU / segundos de generación / 6 × 100. No incluye el coste de normalización ni ASR.','',
'## Resultados medidos','',
'| Voz | WAV (s) | Generación (s) | RTF | Carga (s) | RAM síntesis (GiB) | CPU media equipo | LUFS | dBTP |',
'|---|---:|---:|---:|---:|---:|---:|---:|---:|']
cards=[]; missing=[]
for key,label in labels.items():
    p=R/'escucha'/f'{key}.wav'
    if not p.exists(): missing.append(label); continue
    inf=sf.info(p); dur=inf.duration; level=levels[p.name]['normalized']; m=R/'evidencia'/f'{key}.json'
    if m.exists():
        x=json.loads(m.read_text()); t=x['generation_seconds']; vals=f"{t:.1f} | {t/dur:.2f} | {x['model_load_seconds']:.1f} | {x['peak_process_rss_bytes']/2**30:.2f} | {100*x['process_cpu_seconds']/t/6:.1f}%"
    else: vals='no medido¹ | — | — | — | —'
    lines.append(f"| {label} | {dur:.2f} | {vals} | {level['input_i']} | {level['input_tp']} |")
    cards.append(f'<section><h2>{html.escape(label)}</h2><audio controls preload="none" src="escucha/{key}.wav"></audio><p>{dur:.2f} s · {level["input_i"]} LUFS · <a href="escucha/{key}.wav" download>Descargar WAV</a></p></section>')
lines+=['','¹ Kokoro es una referencia conservada; no se inventa un tiempo nuevo de generación. RTF menor que uno significa generación más rápida que la duración del audio. Las cargas iniciales pueden incluir importaciones y calentamiento de bibliotecas.','',
'## Verificación de lectura','',
'Whisper small int8 local, español, beam size 5, sirve como revisión auxiliar. A continuación se conservan las transcripciones completas. Una discrepancia ASR es un indicio para escuchar, no prueba concluyente de un error de la voz. La estabilidad perceptual del timbre, la naturalidad, la expresividad y el acento latinoamericano requieren escucha humana y no se califican a partir de estas cifras.','']
design=R/'evidencia/voicedesign_prompt.json'
if design.exists():
    prompt=json.loads(design.read_text(encoding='utf-8'))
    lines+=['### Alcance de VoiceDesign','',
    'Prueba breve adicional, realizada por separado después de liberar CustomVoice. El umbral previo fue 12 GiB disponibles; se registra en `voicedesign_recursos_previos.json`. VoiceDesign crea un timbre a partir de una descripción, por lo que esta muestra no es una voz predefinida y no pertenece a la comparación completa. No se clona ninguna voz.','',
    'Texto: «'+prompt['text']+'»','',
    'Descripción: `'+prompt['instruction']+'`','']
    loadfile=R/'evidencia/voicedesign_carga.json'
    if loadfile.exists():
        d=json.loads(loadfile.read_text())
        lines+=[f"Durante su carga se observaron {d['peak_rss_bytes']/2**30:.2f} GiB de RSS y al menos {d['min_available_bytes']/2**30:.2f} GiB disponibles en el sistema. El pico de síntesis se informa por separado en la tabla.",'']
for key,label in labels.items():
    p=R/'evidencia'/f'asr_{key}.json'
    if not p.exists(): continue
    x=json.loads(p.read_text(encoding='utf-8')); transcript=' '.join(s['text'].strip() for s in x['segments'])
    lines+=['### '+label,'',transcript,'']
lines+=['## Licencias y procedencia','',
'Pesos Supertonic 3: OpenRAIL-M; código del SDK: MIT. Qwen3-TTS: Apache 2.0. Kokoro: referencia de la producción anterior, pesos Apache 2.0. Las licencias y fichas recuperadas se guardan en `licencias/` y en los archivos de procedencia; `evidencia/dependencias.json` identifica las bibliotecas.','',
'Fuentes oficiales: [Supertonic archivado](https://github.com/supertone-oss-archive/supertonic), [pesos Supertonic 3](https://huggingface.co/Supertone/supertonic-3), [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS), [CustomVoice 0.6B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice), [VoiceDesign 1.7B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign).','',
'Las revisiones exactas están fijadas en `evidencia/revisiones.json` y `voicedesign_revision.json`. `verificacion_oficial.json` compara cada archivo descargado con el SHA256 LFS o el identificador Git de la revisión oficial. `modelos_sha256.json` registra además tamaños y SHA256 locales. Los modelos y el entorno permanecen disponibles localmente, excluidos de Git.','',
'## Incidencias y límites','',
'Se resolvió un fallo de certificado HTTPS usando el almacén de confianza de Windows mediante truststore; no se deshabilitó la validación TLS. La primera importación de PyTorch fue lenta. Se interrumpió una prueba de Qwen con decodificación greedy antes de completar muestras y se adoptó el muestreo recomendado por el SDK oficial; su log se conserva. Los resultados entregados corresponden al muestreo oficial. El aviso de FlashAttention es esperable en CPU; no se instala. El SDK avisa que no encuentra el ejecutable SoX; la ruta de síntesis utilizada produce WAV mediante soundfile, sin llamar ese ejecutable.','',
'La semilla y las versiones están fijadas; no se promete identidad binaria entre otras versiones de CPU o bibliotecas. No se realizó una escucha perceptual humana de estas muestras. Acento, naturalidad, expresividad, calidad subjetiva de la pronunciación y estabilidad perceptual quedan pendientes de esa evaluación. Usar `PROTOCOLO_ESCUCHA.md` antes de seleccionar una voz institucional.','',
'## Recomendación provisional','',
'Priorizar la escucha de las tres voces de Supertonic junto con Kokoro para el flujo automatizado en este CPU: el coste observado de Supertonic permite iterar con comodidad. Incluir Ryan y Aiden en la decisión por su resultado audible, aceptando su mayor coste de ejecución. Esta es una recomendación operativa; no establece superioridad sonora ni sustituye la elección después de escuchar.','',
'## Reproducción','',
'Ejecutar `reproducir.ps1` desde este directorio. Requiere uv, FFmpeg y conexión para recuperar dependencias y revisiones oficiales. VoiceDesign es una prueba opcional y se activa por separado tras verificar RAM disponible. Los MP4 y la infraestructura de Manim no participan de la ejecución.','']
if missing: lines+=['Muestras aún no disponibles: '+', '.join(missing)+'.','']
(R/'INFORME_TECNICO.md').write_text('\n'.join(lines),encoding='utf-8')
page='''<!doctype html><html lang="es"><meta charset="utf-8"><title>MA-VOICE-002 · escucha</title><style>body{font:18px system-ui;max-width:900px;margin:40px auto;padding:0 22px;background:#101724;color:#edf2f7}section{padding:18px 0;border-bottom:1px solid #40536b}h2{font-size:22px}audio{width:100%}a{color:#8cddff}p{line-height:1.6}</style><h1>Matemática Abierta · comparación de voces</h1><p>Mismo fragmento, sonoridad igualada. Mantén el volumen del sistema. Evalúa naturalidad, acento, matemática, timbre y ritmo. No hay una voz ganadora preseleccionada.</p><p>'''+html.escape(expected)+'</p>'+''.join(cards)+'<p><a href="INFORME_TECNICO.md">Informe técnico</a> · <a href="PROTOCOLO_ESCUCHA.md">Guía de evaluación</a></p></html>'
(R/'ESCUCHA.html').write_text(page,encoding='utf-8')
print('Informe y página de escucha actualizados')
