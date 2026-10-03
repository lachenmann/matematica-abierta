# Protocolo de grabación — Reaper / toma continua

## Decisión de flujo

La locución se graba como **una sola toma continua** en Reaper. No se divide en archivos por tramo.

Los siete bloques siguen existiendo únicamente como **marcadores temporales** para sincronizar Manim.

## Grabación

- una pista de voz continua;
- WAV PCM preferido para el render de referencia;
- 48 kHz;
- mono;
- 24 bit si está disponible;
- no es necesario cortar los bloques ni exportarlos individualmente.

Puedes editar respiraciones, errores o silencios dentro de Reaper como lo haces normalmente. Lo importante es que, después de editar, los marcadores queden en las posiciones definitivas.

## Marcadores canónicos

Coloca un marcador de Reaper al **comienzo** de cada unidad con estos nombres exactos:

1. `opening`
2. `block-1`
3. `bridge-1`
4. `block-2`
5. `bridge-2`
6. `block-3`
7. `closing`

Opcionalmente añade `end` al final exacto de la locución. Si no existe, el analizador usa el final del archivo de audio.

En Reaper basta con situar el cursor y pulsar **M** para crear un marcador; después asigna uno de esos nombres.

## Archivos necesarios

Sólo necesitamos dos archivos de trabajo:

- el render continuo, por ejemplo `MA-CLS-C13-P01-reference.wav`;
- tu proyecto de Reaper, por ejemplo `MA-CLS-C13-P01-reference.rpp`.

No hace falta exportar CSV ni regiones, y tampoco separar la voz en clips.

## Análisis

Desde `audiovisual/manim/ma_cls_c13_p01`:

```powershell
uv run python analyze_voice_reference.py `
  --audio "RUTA\MA-CLS-C13-P01-reference.wav" `
  --rpp "RUTA\MA-CLS-C13-P01-reference.rpp"
```

El script lee los marcadores directamente del archivo `.rpp` y crea:

`voice-reference/voice-reference-timing.json`

con:

- duración real de cada unidad;
- tiempos absolutos de inicio y término;
- duración total;
- desviación respecto del modelo de 185 s.

## Guion

Lee `spoken-script.md` como una locución continua. Los encabezados 01–07 son sólo referencias editoriales; **no se pronuncian**.

## Regla MA-M06

**La voz gobierna la permanencia; la matemática gobierna el momento de aparición.**

La grabación continua puede tener el ritmo natural que necesites. Manim se ajustará después a la voz; no debes forzar tu lectura para coincidir con los tiempos estimados.
