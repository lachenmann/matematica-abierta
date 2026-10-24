import pathlib,json,html
import numpy as np,soundfile as sf
R=pathlib.Path(__file__).resolve().parent
cfg=json.loads((R/'evidencia/modelos.json').read_text()); profile=json.loads((R/'VOICE_PROFILE.json').read_text(encoding='utf8'))
script=json.loads((R/'guion.json').read_text(encoding='utf8'))['segmentos']; levels=json.loads((R/'evidencia/sonoridad.json').read_text())
prompt_config=json.loads((R/'referencia/prompt_config.json').read_text(encoding='utf8'))
rows=[]
demo_status=('Se generó `demo/MA_VOICE_003_DEMO.mp4` con Base, en una copia de EXP003 a 1920×1080 y 60 fps.' if (R/'demo/MA_VOICE_003_DEMO.mp4').exists() else 'La copia de EXP003 queda preparada en `demo/`; todavía no hay un MP4 final generado.')
for mode in ['clone','direct']:
    clips=[json.loads(p.read_text(encoding='utf8')) for p in sorted((R/'raw'/mode).glob('*.json'))]
    load=json.loads((R/'evidencia'/f'load_{mode}.json').read_text());duration=levels[mode]['duration']; generation=sum(x['generation_seconds'] for x in clips);cpu=sum(x['cpu_seconds'] for x in clips)
    peak=max(load['peak_rss'],max(x['peak_rss'] for x in clips));available=min(load['min_available'],min(x['min_available'] for x in clips))
    if mode=='clone' and (R/'evidencia/load_clone_preliminar.json').exists():
        cold=json.loads((R/'evidencia/load_clone_preliminar.json').read_text());peak=max(peak,cold['peak_rss']);available=min(available,cold['min_available'])
    rows.append({'mode':mode,'duration':duration,'speech':sum(x['seconds'] for x in clips),'generation':generation,'load':load['seconds'],'rtf_speech':generation/sum(x['seconds'] for x in clips),'cpu_percent':cpu/generation/6*100,'peak_gib':peak/2**30,'available_min_gib':available/2**30,'lufs':levels[mode]['measured']['input_i'],'tp':levels[mode]['measured']['input_tp']})
(R/'evidencia/resumen.json').write_text(json.dumps(rows,indent=2))
lines=['# MA-VOICE-003 — propuesta de voz institucional candidata','',
'Estado: candidata técnica para aprobación auditiva del autor. La aprobación de la muestra breve en MA-VOICE-002 no se extiende automáticamente a las narraciones largas.','',
'## Identidad preservada','',
'Se conserva byte por byte el WAV elegido en MA-VOICE-002 (`referencia/elegida_escucha.wav`), su versión original sin normalizar y el código que lo produjo. La referencia es enteramente sintética; no se utiliza ni se clona ninguna grabación humana del autor.','',
'SHA256 del WAV de identidad: `'+profile['reference_sha256']+'`.','',
'Texto de la referencia: «'+profile['reference_text']+'». Duración del archivo: 4,45 s, incluyendo 0,45 s de silencio añadido al final.','',
'Descripción original: `A male educational narrator, warm and calm, clear Latin American Spanish pronunciation, measured pace and neutral intonation.`','',
'Modelo original: Qwen3-TTS-12Hz-1.7B-VoiceDesign, revisión `'+cfg['direct']['revision']+'`; qwen-tts 0.1.1, PyTorch 2.14.1+cpu, semilla 20261023 fijada antes de cargar, float32, eager, seis hilos, idioma Spanish, máximo 192 tokens y muestreo oficial. La descripción y la semilla son procedencia, no un sustituto del WAV elegido.','',
'## Procedimiento oficial y modalidades','',
'Se aplica [Voice Design then Clone de Qwen](https://github.com/QwenLM/Qwen3-TTS#voice-design-then-clone): la muestra sintética ya aprobada pasa a `create_voice_clone_prompt`, y el prompt reutilizable se utiliza en `generate_voice_clone` del modelo 1.7B Base.','',
f"**Base con referencia (`clone`)** usa el archivo exacto elegido, su transcripción, el embedding de hablante y los códigos acústicos de referencia: `x_vector_only_mode=False`, `icl_mode=True`. El prompt se conserva en safetensors, con configuración JSON y hash del WAV vinculado. La extracción inicial tardó {prompt_config['create_seconds']:.2f} s; después se vuelve a cargar sin extraer rasgos en cada frase.",'',
'**VoiceDesign directo (`direct`)** usa la descripción original y genera el mismo texto con semilla documentada. Es el control experimental: esa API no recibe la referencia elegida y no garantiza recuperar su identidad. No sustituye a la voz seleccionada.','',
'Base oficial: `'+cfg['clone']['repo']+'`, revisión `'+cfg['clone']['revision']+'`. Ambos modelos están bajo Apache 2.0; se conservan fichas, licencia y comparación de hashes de archivos contra las revisiones oficiales.','',
'## Texto, CPU y reproducción','',
'Se reutiliza íntegro el guion matemático del Experimento 003: 18 microtramos y unos tres minutos de contenido, con expresiones normalizadas para lectura. La copia `guion.json` tiene el mismo hash que la fuente original. Las pausas pedagógicas se conservan y cada toma tiene texto, hash, semilla y parámetros.','',
'Equipo: Windows 11, Intel Core i5-9400, 6 núcleos/6 hilos, 32 GB de RAM; sin CUDA. Nuevo entorno aislado en MA_VOICE_003, sin instalar ni modificar paquetes de Manim. Modelos 1.7B float32, atención eager, seis hilos, carga con `low_cpu_mem_usage` y `offload_state_dict`. Los dos modelos completos nunca permanecen cargados simultáneamente.','',
'La primera toma es individual. El resto usa el batch oficial de dos textos por llamada, conservando el orden del guion. Se reinicia la semilla 20261023 antes de cada grupo, máximo 768 tokens por texto, parámetros de muestreo oficiales. Los registros distinguen tiempo total del lote y tiempo amortizado por toma. Una prueba serial previa se interrumpió para aplicar batch; su primera toma terminada se conserva y reutiliza. Los tiempos exitosos no incluyen el trabajo incompleto de esa transición.','',
'Las tomas, la referencia y el prompt entregados se preservan por hash. La configuración y las semillas permiten repetir el procedimiento, pero no se promete identidad binaria de una nueva síntesis en otro hardware o con otras bibliotecas numéricas.','',
'El monitor registra RSS del proceso, segundos CPU y memoria disponible cada 0,25 s. Son mediciones de un equipo en uso, no un benchmark de laboratorio. El porcentaje de CPU está referido a los seis núcleos. RTF se calcula contra duración de voz sin las pausas añadidas. La columna de carga incluye importaciones del runtime y apertura del modelo; la de síntesis corresponde al tiempo transcurrido de las llamadas exitosas, no a segundos CPU acumulados.','',
'| Modalidad | Narración con pausas (s) | Voz (s) | Síntesis exitosa (s) | Carga (s) | RTF voz | CPU | Pico observado (GiB) | Mínimo disponible (GiB) | LUFS | dBTP |',
'|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
for x in rows: lines.append(f"| {x['mode']} | {x['duration']:.2f} | {x['speech']:.2f} | {x['generation']:.1f} | {x['load']:.1f} | {x['rtf_speech']:.2f} | {x['cpu_percent']:.1f}% | {x['peak_gib']:.2f} | {x['available_min_gib']:.2f} | {x['lufs']} | {x['tp']} |")
lines+=['',
'Las copias de escucha usan el mismo objetivo LUFS y ganancia constante por narración completa, sin compresión, limitación, cambio de tono o aceleración. No se normaliza cada segmento por separado: las diferencias internas de nivel quedan disponibles para la evaluación. Los extractos usan la misma ganancia global de su narración.','',
'## Verificación y límites','',
'La revisión automática usa Whisper small int8 local, con revisión fijada, transcripciones por toma y palabras temporizadas. Sus discrepancias se documentan como indicios para escuchar; no se sustituyen automáticamente palabras del audio ni se considera el ASR una audición. Las pausas, entonación, expresividad, preferencia de acento latinoamericano y naturalidad requieren evaluación perceptual.','',
'El análisis de identidad usa únicamente el encoder de hablante ECAPA-TDNN oficial de Base. Sus similitudes coseno son una ayuda para detectar variación, no una escala de calidad sonora ni una prueba de acento. Es el mismo encoder que condiciona Base, por lo que la métrica está ligada al procedimiento y no constituye una validación independiente. La muestra breve contiene pocos fonemas y limita lo que puede inferirse sobre estabilidad durante tres minutos.','']
identity=R/'evidencia/identidad_proxy.json'
if identity.exists():
    x=json.loads(identity.read_text())
    lines+=['| Modalidad | Coseno medio con referencia | Mínimo | Desviación | Coseno medio con centro propio |','|---|---:|---:|---:|---:|']
    for mode,d in x['modes'].items():lines.append(f"| {mode} | {d['mean_reference_cosine']:.4f} | {d['min_reference_cosine']:.4f} | {d['std_reference_cosine']:.4f} | {d['mean_centroid_cosine']:.4f} |")
lines+=['','## Propuesta y demostración','',
'Se propone `MA-QWEN-VD-001-candidata`, definida por el hash de referencia y el prompt Base persistido. La ruta con referencia es la que conserva explícitamente el anclaje de identidad; VoiceDesign directo queda como control. La elección definitiva permanece pendiente de aprobación auditiva del autor.','',
demo_status+' Se conserva la secuencia de animaciones y la composición originales. Se adaptan los tiempos y el anclaje ASR de «a sub ene», y se separa el rótulo «0» del borde verde en la copia. No se alteran los MP4 originales. La demostración no implica estado de publicación ni aprobación perceptual. Consultar `QA_FINAL.md` para las verificaciones realmente realizadas.','',
'Reproducir mediante `reproducir.ps1`. Los pesos y entornos están excluidos del ZIP y de Git; sus revisiones se fijan en `evidencia/modelos.json`. Las fuentes de animación copiadas, marcadores, alineaciones y subtítulos quedan en `demo/`.']
(R/'INFORME_TECNICO.md').write_text('\n'.join(lines),encoding='utf8')
cards=[]
for mode,label in [('clone','Base · identidad desde la referencia elegida'),('direct','VoiceDesign directo · control por descripción')]:
    cards.append(f'<section><h2>{label}</h2><audio controls preload="none" src="escucha/NARRACION_{mode}.wav"></audio><p><a href="escucha/NARRACION_{mode}.wav" download>WAV completo</a></p></section>')
segments=[]
for i,s in enumerate(script):
    clips=''.join(f'<p>{mode}<audio controls preload="none" src="escucha/segmentos/{mode}/{i:02d}_{s["id"]}.wav"></audio></p>' for mode in ['clone','direct'])
    segments.append(f'<details><summary>{i+1}. {s["id"]}</summary><p>{html.escape(s["texto"])}</p>{clips}</details>')
page='<!doctype html><html lang="es"><meta charset="utf-8"><title>MA-VOICE-003</title><style>body{font:18px system-ui;max-width:960px;margin:40px auto;padding:0 20px;background:#0F1117;color:#F5F7FA}audio,video{width:100%}a{color:#4EA1FF}section,details{padding:15px 0;border-bottom:1px solid #555}p{line-height:1.6}</style><h1>Voz institucional candidata · MA-VOICE-003</h1><p>Referencia exacta elegida por el autor. La aprobación de las narraciones completas sigue pendiente. Mantén un mismo volumen del sistema y compara los mismos pasajes.</p><audio controls src="referencia/elegida_escucha.wav"></audio>'+''.join(cards)+'<h2>Comparación por segmento</h2>'+''.join(segments)+'<h2>Demostración</h2><video controls preload="none" src="demo/MA_VOICE_003_DEMO.mp4"></video><p><a href="INFORME_TECNICO.md">Informe técnico</a> · <a href="QA_FINAL.md">QA</a></p></html>'
page=page.replace('</html>','<script>const players=[...document.querySelectorAll("audio,video")];players.forEach(p=>p.addEventListener("play",()=>players.forEach(q=>{if(q!==p)q.pause()})));</script></html>')
(R/'ESCUCHA.html').write_text(page,encoding='utf8')
print(json.dumps(rows),flush=True)
