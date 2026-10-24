# MA-VOICE-003 — QA final de la propuesta candidata

La aprobación auditiva institucional permanece pendiente del autor. Este informe separa las verificaciones técnicas, los indicios de lectura y la inspección visual del MP4.

## Integridad y procedencia

- 26 archivos de los modelos cotejados con los identificadores de sus revisiones oficiales: coinciden todos.
- 5 verificaciones de originales y copias de referencia: sin cambios.
- El prompt persistido está ligado por SHA256 al WAV sintético exacto elegido. No se produce una referencia nueva desde la descripción.

## Audios completos

| Modalidad | Duración (s) | Formato | Escala completa | Palabras/min de voz | Pausas añadidas (s) |
|---|---:|---|---:|---:|---:|
| clone | 177.717 | 48000 Hz, mono, PCM_24 | 0 | 157.6 | 29.957 |
| direct | 205.050 | 48000 Hz, mono, PCM_24 | 0 | 132.9 | 29.930 |

Ambos WAV se decodificaron completos. Sonoridad igualada mediante ganancia constante de cada narración completa, sin compresión, limitación o cambio de velocidad. Las pausas internas detectadas entre palabras se conservan en `evidencia/audio_qa.json`; son puntos de escucha, no defectos confirmados.

## Lectura matemática

Las 36 tomas se transcribieron por separado con Whisper small int8 local. Se conserva el texto reconocido íntegro, los tiempos por palabra y la comparación con el guion. La puntuación y las variantes n/ene o b/be se normalizan para comparar texto; no se reescribe el audio. Las discrepancias siguientes son indicios ASR y requieren comprobarse por escucha, especialmente si afectan números u operadores.

### clone

- `regla_a`: [{"op": "replace", "expected": "a sub ene", "asr": "asubn"}].
- `siguiente`: [{"op": "replace", "expected": "un", "asr": "uno"}, {"op": "replace", "expected": "un", "asr": "uno"}].
### direct

- `regla_a`: [{"op": "replace", "expected": "sub ene", "asr": "su vn"}].
- `regla_b`: [{"op": "insert", "expected": "", "asr": "a"}].
- `comunes`: [{"op": "replace", "expected": "recorramos", "asr": "recordamos"}].
- `despues`: [{"op": "replace", "expected": "de a", "asr": "dea"}, {"op": "replace", "expected": "de be", "asr": "deb"}].

## Demostración audiovisual

Se generó una copia de EXP003 con la ruta Base y el mismo guion. Las animaciones originales se conservan; las adaptaciones temporales de la copia y los marcadores se documentan en `demo/` y `evidencia/`.

MP4 SHA256: `7e249e571f2b4212242b97e1e1d9086e5902102e4a3d9a5fbb69fc24c7877720`.

El MP4 se decodificó completo. Se verificó 1920×1080, 60 fps y audio 48 kHz. Se extrajeron 739 fotogramas a 4 fps, 18 estados a resolución completa y vecindades de los eventos temporales.

Se comparó el AAC decodificado del MP4 con el WAV de mezcla en tres ventanas distribuidas por la película. Desplazamientos medidos: 0.000 ms, 0.000 ms, 0.000 ms. Correlaciones: 1.00000, 1.00000, 1.00000.

Registro de inspección realmente realizada sobre este MP4:

```json
{
  "movie_sha256": "7e249e571f2b4212242b97e1e1d9086e5902102e4a3d9a5fbb69fc24c7877720",
  "reviewer": "assistant visual inspection of actual extracted video frames",
  "initial_pass": {
    "chronology": "all 24 contact sheets, 739 frames at 4 fps",
    "key_states": "all 18 states in 5 readable montages",
    "critical_sequences": "all 7 contact sheets at 12 fps",
    "native_resolution": "piecewise definition after completion, boundary table, finite-prefix diagram and final tail"
  },
  "corrective_pass": {
    "defect": "MINOR inherited: green rectangle lower border crossed label zero",
    "change": "zero moved from y=-0.3 to y=-0.7 in copied scene only",
    "final_review": "chronology sheets 18 to 23 (144s to end), full generalization and final states, critical rules-after-N and tail sequences",
    "unchanged_prefix": "584 of 584 final 4fps frames before 146s byte-identical to the already inspected first render",
    "timing": "all event and word-anchor records unchanged after spatial correction"
  },
  "semantic_sync_correction": "a sub ene / Asubn onset mapped to 2.46s in its cue before first master; subtitles anchored to the same onset",
  "observations": [
    "No new spatial collisions or clipping observed within inspected scope",
    "Boundary values 1/(10^6+1), next a value 1/(10^6+2), b value 1 preserved",
    "Zero now separated from green border and aligned with N baseline",
    "187 animations retained; narration and identity-reference hashes unchanged"
  ],
  "perceptual_audio_listening": "not performed by assistant; final author listening and approval pending",
  "publication_status": "demonstration only; no publication approval"
}
```

## Alcance y aprobación

El coseno de embeddings se usa exclusivamente como proxy de identidad y variación. No decide naturalidad, expresividad, acento latinoamericano ni superioridad sonora. La referencia breve limita esa inferencia.

La evaluación perceptual de ambas narraciones completas y del ritmo audiovisual sigue pendiente del autor. La propuesta no se marca como voz institucional definitiva, `PRODUCTION_READY` o lista para publicación. Usar `APROBACION_AUDITIVA.md` y `ESCUCHA.html` para registrar la decisión.