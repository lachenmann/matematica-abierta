# CPM-YT-C01-V01 — Preview local

Este paquete reemplaza la previsualización v01 rechazada.

## Flujo canónico

1. Actualizar el repositorio local:

```powershell
cd D:\MatematicaAbierta-Main
git pull
```

2. Renderizar desde el entorno Manim local:

```powershell
cd D:\MatematicaAbierta-Main\audiovisual\manim
.\render-cpm-yt-c01-v01-preview.ps1
```

Equivalente directo:

```powershell
uv run manim -pql --disable_caching .\clases\cpm_yt_c01_v01_preview.py CPMYTC01V01Preview
```

Para alta calidad:

```powershell
uv run manim -pqh --disable_caching .\clases\cpm_yt_c01_v01_preview.py CPMYTC01V01Preview
```

## Estándar visual

- Fondo: `#0F1117`.
- Todo rótulo visible comienza con mayúscula.
- Fórmulas y símbolos: `MathTex`.
- Rótulos y texto técnico: `Tex`.
- No usar `Text` como sustituto de LaTeX.
- No rasterizar fórmulas.
- Un único cambio matemático sustantivo por transición.
- Asociatividad, conmutatividad, neutros e inversos deben verse como transformaciones distintas.
- Hipótesis como `a\neq0` permanecen visibles mientras justifican un paso.
- El preview no fija todavía la sincronía definitiva con el audio.

No grabar el audio definitivo hasta aprobar el render local.


## Render sincronizado con la voz definitiva

La toma continua de Reaper se conserva localmente, fuera de Git:

```text
cpm_yt_c01_v01\voice-reference\CPM-YT-C01-V01-reference.rpp
cpm_yt_c01_v01\voice-reference\audio\CPM-YT-C01-V01-reference.wav
```

Los tiempos canónicos extraídos de los 39 marcadores se guardan en:

```text
cpm_yt_c01_v01\voice-reference\voice-reference-timing.json
```

El render de producción se genera con:

```powershell
cd D:\MatematicaAbierta-Main\audiovisual\manim
.\render-cpm-yt-c01-v01-production.ps1
```

El script vuelve a analizar el `.rpp` antes de renderizar y usa la clase
`CPMYTC01V01Production`. El preview mudo permanece separado como referencia
visual aprobada.
