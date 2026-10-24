# MA-VOICE-002 — QA final

Estado: siete muestras producidas y verificadas técnicamente; selección institucional pendiente de escucha perceptual.

- Tres voces masculinas predefinidas Supertonic 3, dos Qwen CustomVoice y referencia Kokoro: mismo fragmento hablado. VoiceDesign: extracto breve adicional, claramente identificado.
- Textos matemáticos escritos como se pronuncian: «ene», «un millón más uno», «uno dividido por la suma de un millón y dos». No se envían fórmulas LaTeX al motor.
- Los 64 archivos descargados coinciden con sus hashes de revisiones oficiales. Licencias, versiones, código y mediciones conservados.
- Los siete originales y las siete copias de escucha se decodifican completos, sin valores no finitos ni muestras a escala completa.
- Copias de escucha: 48 kHz, mono, PCM de 24 bits, −24 LUFS mediante ganancia constante. Se conserva la dinámica; no se comprime, limita, acelera ni cambia el tono.
- El MP4, el audio maestro y el guion del Experimento 003 coinciden con sus hashes anteriores. También se verificaron las cuatro tomas originales utilizadas.

## Lectura y matemática

Se revisaron las siete transcripciones completas. Conservan el contenido numérico y las relaciones del fragmento: el tramo tiene un millón de términos más el índice cero; en la frontera el denominador es un millón más uno; en el índice siguiente pasa a un millón más dos; la segunda sucesión toma el valor uno. No se observaron omisiones o repeticiones del contenido en las transcripciones. Esto es evidencia auxiliar de inteligibilidad, no una garantía auditiva.

Whisper representa la palabra «ene» como «n», «en e», «en n» o «en evale». Estos pasajes deben escucharse: la segmentación escrita no demuestra que la voz se equivoque. Los tiempos son relativos a cada WAV completo.

| Archivo | Desde (s) | Texto reconocido |
|---|---:|---|
| kokoro_em_alex.wav | 17.28 | ahora n vale un millón más uno, la primera sucesión vale uno |
| qwen06_Aiden.wav | 21.60 | Ahora en e vale un millón más uno. |
| qwen06_Ryan.wav | 26.06 | Ahora en e vale un millón más uno. |
| qwen17_VoiceDesign_BREVE.wav | 1.64 | Ahora n vale un millón más uno. |
| supertonic3_M1.wav | 21.18 | Ahora en n vale un millón más uno. |
| supertonic3_M2.wav | 20.54 | Ahora en evale un millón más uno. |
| supertonic3_M3.wav | 17.50 | Ahora n vale un millón más uno. |

Sonoridad medida: de -24.01 a -23.99 LUFS; diferencia máxima 0.02 LUFS. Pico verdadero máximo: -2.42 dBTP.

## Límites de la evaluación

Naturalidad, expresividad, preferencia de acento latinoamericano, claridad perceptual de «ene», estabilidad subjetiva del timbre y adecuación pedagógica de las pausas quedan sin puntuación hasta escuchar. No se declara ninguna voz superior a Kokoro por arquitectura, tamaño o métricas.

Recomendación provisional de operación: comenzar la selección auditiva con Supertonic M1/M2/M3 por su ejecución ágil en este CPU y compararlas con Kokoro, Ryan y Aiden. La muestra VoiceDesign demuestra viabilidad de una prueba breve, no sustituye la prueba completa ni representa una voz predefinida.

Consultar `INFORME_TECNICO.md`, `PROTOCOLO_ESCUCHA.md` y las evidencias JSON.