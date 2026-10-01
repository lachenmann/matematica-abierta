# Protocolo de grabación — voz de referencia

## Objetivo

Obtener una pista de referencia suficientemente estable para sincronizar Manim. **No es todavía el máster de audio**.

## Formato

- un archivo por segmento;
- WAV PCM preferido;
- 48 kHz;
- mono;
- 24 bit si el grabador lo permite; 16 bit también sirve para referencia;
- no normalizar, comprimir ni aplicar reducción de ruido destructiva antes de medir.

## Archivos

1. `01-opening.wav`
2. `02-block-1.wav`
3. `03-bridge-1.wav`
4. `04-block-2.wav`
5. `05-bridge-2.wav`
6. `06-block-3.wav`
7. `07-closing.wav`

Los archivos deben guardarse localmente en:

`audiovisual/manim/ma_cls_c13_p01/voice-reference/audio/`

La carpeta `audio/` queda ignorada por Git: una voz de referencia no debe entrar accidentalmente en el repositorio.

## Criterio de lectura

- leer el texto de `spoken-script.md` literalmente;
- conservar pausas naturales en comas, dos puntos y fórmulas;
- no intentar alcanzar exactamente el tiempo objetivo;
- no acelerar una fórmula para “entrar” en el cue;
- dejar aproximadamente 100–250 ms de silencio al comienzo y al final de cada archivo;
- si hay un error, repetir el segmento completo en vez de hacer un empalme.

## Después de grabar

Desde `audiovisual/manim/ma_cls_c13_p01`:

```powershell
uv run python analyze_voice_reference.py voice-reference/audio
```

El analizador crea:

`voice-reference/voice-reference-timing.json`

con las duraciones reales, los tiempos acumulados y la desviación frente al modelo de 115 palabras/minuto.

## Regla MA-M06

**La voz gobierna la permanencia; la matemática gobierna el momento de aparición.**

La locución real puede cambiar cuánto permanece visible un estado, pero no puede adelantar una fórmula antes de que sus componentes conceptuales hayan sido presentados.
