import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
audio=json.loads((R/'evidencia/audio_qa.json').read_text(encoding='utf8'))
reading=json.loads((R/'evidencia/revision_lectura.json').read_text(encoding='utf8'))
protection=json.loads((R/'evidencia/proteccion.json').read_text())
models=json.loads((R/'evidencia/verificacion_modelos.json').read_text())
lines=['# MA-VOICE-003 — QA final de la propuesta candidata','',
'La aprobación auditiva institucional permanece pendiente del autor. Este informe separa las verificaciones técnicas, los indicios de lectura y la inspección visual del MP4.','',
'## Integridad y procedencia','',
f'- {len(models)} archivos de los modelos cotejados con los identificadores de sus revisiones oficiales: '+('coinciden todos.' if all(x['match'] for x in models) else 'hay discrepancias.'),
f'- {len(protection)} verificaciones de originales y copias de referencia: '+('sin cambios.' if all(x['unchanged'] for x in protection) else 'hay cambios que revisar.'),
'- El prompt persistido está ligado por SHA256 al WAV sintético exacto elegido. No se produce una referencia nueva desde la descripción.','',
'## Audios completos','',
'| Modalidad | Duración (s) | Formato | Escala completa | Palabras/min de voz | Pausas añadidas (s) |','|---|---:|---|---:|---:|---:|']
for mode,x in audio.items():lines.append(f"| {mode} | {x['duration']:.3f} | {x['sample_rate']} Hz, mono, {x['subtype']} | {x['samples_at_full_scale']} | {x['spoken_wpm']:.1f} | {x['added_pause_seconds']:.3f} |")
lines+=['','Ambos WAV se decodificaron completos. Sonoridad igualada mediante ganancia constante de cada narración completa, sin compresión, limitación o cambio de velocidad. Las pausas internas detectadas entre palabras se conservan en `evidencia/audio_qa.json`; son puntos de escucha, no defectos confirmados.','',
'## Lectura matemática','',
'Las 36 tomas se transcribieron por separado con Whisper small int8 local. Se conserva el texto reconocido íntegro, los tiempos por palabra y la comparación con el guion. La puntuación y las variantes n/ene o b/be se normalizan para comparar texto; no se reescribe el audio. Las discrepancias siguientes son indicios ASR y requieren comprobarse por escucha, especialmente si afectan números u operadores.','']
for mode in ['clone','direct']:
    group=[x for x in reading if x['mode']==mode]
    lines+=['### '+mode,'']
    for x in group:
        if x['differences']:lines.append('- `'+x['id']+'`: '+json.dumps(x['differences'],ensure_ascii=False)+'.')
    if not any(x['differences'] for x in group):lines+=['No aparecen diferencias tras la normalización textual documentada. Esto no garantiza una pronunciación o entonación perceptualmente satisfactoria.']
lines+=['','## Demostración audiovisual','']
movie=R/'demo/MA_VOICE_003_DEMO.mp4';extr=R/'demo/qa/extraccion.json';inspection=R/'demo/qa/inspeccion_manual.json'
if movie.exists():
    lines+=['Se generó una copia de EXP003 con la ruta Base y el mismo guion. Las animaciones originales se conservan; las adaptaciones temporales de la copia y los marcadores se documentan en `demo/` y `evidencia/`.','',
    'MP4 SHA256: `'+hashlib.sha256(movie.read_bytes()).hexdigest()+'`.','']
    if extr.exists():
        e=json.loads(extr.read_text());lines+=[f"El MP4 se decodificó completo. Se verificó 1920×1080, 60 fps y audio 48 kHz. Se extrajeron {e['chronology_frames']} fotogramas a 4 fps, {len(e['full_resolution'])} estados a resolución completa y vecindades de los eventos temporales.",'']
    mux=R/'demo/qa/audio_mux_checks.json'
    if mux.exists():
        m=json.loads(mux.read_text());lines+=['Se comparó el AAC decodificado del MP4 con el WAV de mezcla en tres ventanas distribuidas por la película. Desplazamientos medidos: '+', '.join(f"{x['lag_seconds']*1000:.3f} ms" for x in m['windows'])+'. Correlaciones: '+', '.join(f"{x['correlation']:.5f}" for x in m['windows'])+'.','']
    if inspection.exists():
        x=json.loads(inspection.read_text(encoding='utf8'))
        if x.get('movie_sha256')==hashlib.sha256(movie.read_bytes()).hexdigest():lines+=['Registro de inspección realmente realizada sobre este MP4:','','```json',json.dumps(x,ensure_ascii=False,indent=2),'```','']
        else:lines+=['Existe un registro visual de otra versión; no se considera inspeccionado este nuevo hash de MP4.','']
    else:lines+=['La extracción está disponible, pero no hay una inspección visual manual registrada todavía; no se declara superado ese gate.','']
else:lines+=['No se incluye MP4 final en este estado de ejecución. Las narraciones y sus fuentes son independientes de la viabilidad de esa integración.','']
lines+=['## Alcance y aprobación','',
'El coseno de embeddings se usa exclusivamente como proxy de identidad y variación. No decide naturalidad, expresividad, acento latinoamericano ni superioridad sonora. La referencia breve limita esa inferencia.','',
'La evaluación perceptual de ambas narraciones completas y del ritmo audiovisual sigue pendiente del autor. La propuesta no se marca como voz institucional definitiva, `PRODUCTION_READY` o lista para publicación. Usar `APROBACION_AUDITIVA.md` y `ESCUCHA.html` para registrar la decisión.']
(R/'QA_FINAL.md').write_text('\n'.join(lines),encoding='utf8')
print('QA actualizado; aprobación auditiva pendiente')
