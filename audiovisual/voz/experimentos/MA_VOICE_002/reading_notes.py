import pathlib,json
R=pathlib.Path(__file__).resolve().parent
rows=[]
for p in sorted((R/'evidencia').glob('asr_*.json')):
    x=json.loads(p.read_text(encoding='utf-8'))
    if 'segments' not in x: continue
    words=[w for s in x['segments'] for w in s['words']]
    for i,w in enumerate(words):
        if 'ahora' in w['word'].lower():
            context=[]
            for following in words[i:i+12]:
                context.append(following['word'].strip())
                if following['word'].rstrip().endswith('.'): break
            rows.append({'file':x['file'],'start':w['start'],'recognized_context':' '.join(context),'expected':'Ahora ene vale un millón más uno.','status':'Variación de transcripción de ene; comprobar por escucha, no error confirmado'})
(R/'evidencia/puntos_escucha.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# MA-VOICE-002 — QA final','',
'Estado: siete muestras producidas y verificadas técnicamente; selección institucional pendiente de escucha perceptual.','',
'- Tres voces masculinas predefinidas Supertonic 3, dos Qwen CustomVoice y referencia Kokoro: mismo fragmento hablado. VoiceDesign: extracto breve adicional, claramente identificado.','- Textos matemáticos escritos como se pronuncian: «ene», «un millón más uno», «uno dividido por la suma de un millón y dos». No se envían fórmulas LaTeX al motor.','- Los 64 archivos descargados coinciden con sus hashes de revisiones oficiales. Licencias, versiones, código y mediciones conservados.','- Los siete originales y las siete copias de escucha se decodifican completos, sin valores no finitos ni muestras a escala completa.','- Copias de escucha: 48 kHz, mono, PCM de 24 bits, −24 LUFS mediante ganancia constante. Se conserva la dinámica; no se comprime, limita, acelera ni cambia el tono.','- El MP4, el audio maestro y el guion del Experimento 003 coinciden con sus hashes anteriores. También se verificaron las cuatro tomas originales utilizadas.','',
'## Lectura y matemática','',
'Se revisaron las siete transcripciones completas. Conservan el contenido numérico y las relaciones del fragmento: el tramo tiene un millón de términos más el índice cero; en la frontera el denominador es un millón más uno; en el índice siguiente pasa a un millón más dos; la segunda sucesión toma el valor uno. No se observaron omisiones o repeticiones del contenido en las transcripciones. Esto es evidencia auxiliar de inteligibilidad, no una garantía auditiva.','',
'Whisper representa la palabra «ene» como «n», «en e», «en n» o «en evale». Estos pasajes deben escucharse: la segmentación escrita no demuestra que la voz se equivoque. Los tiempos son relativos a cada WAV completo.','',
'| Archivo | Desde (s) | Texto reconocido |','|---|---:|---|']
for row in rows: lines.append(f"| {row['file']} | {row['start']:.2f} | {row['recognized_context']} |")
levels=json.loads((R/'evidencia/sonoridad.json').read_text())
values=[float(x['normalized']['input_i']) for x in levels]
peaks=[float(x['normalized']['input_tp']) for x in levels]
lines+=['',f'Sonoridad medida: de {min(values):.2f} a {max(values):.2f} LUFS; diferencia máxima {max(values)-min(values):.2f} LUFS. Pico verdadero máximo: {max(peaks):.2f} dBTP.','',
'## Límites de la evaluación','',
'Naturalidad, expresividad, preferencia de acento latinoamericano, claridad perceptual de «ene», estabilidad subjetiva del timbre y adecuación pedagógica de las pausas quedan sin puntuación hasta escuchar. No se declara ninguna voz superior a Kokoro por arquitectura, tamaño o métricas.','',
'Recomendación provisional de operación: comenzar la selección auditiva con Supertonic M1/M2/M3 por su ejecución ágil en este CPU y compararlas con Kokoro, Ryan y Aiden. La muestra VoiceDesign demuestra viabilidad de una prueba breve, no sustituye la prueba completa ni representa una voz predefinida.','',
'Consultar `INFORME_TECNICO.md`, `PROTOCOLO_ESCUCHA.md` y las evidencias JSON.']
(R/'QA_FINAL.md').write_text('\n'.join(lines),encoding='utf-8')
print('QA y puntos de escucha registrados')
