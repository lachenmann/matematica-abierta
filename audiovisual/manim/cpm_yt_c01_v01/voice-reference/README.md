# CPM-YT-C01-V01 — referencia de voz

Archivos locales esperados:

- `CPM-YT-C01-V01-reference.rpp`
- `audio/CPM-YT-C01-V01-reference.wav`

El WAV y el proyecto de Reaper son material local y no se versionan.
`voice-reference-timing.json` sí es canónico y contiene los tiempos extraídos de los marcadores Reaper.

Para regenerarlo:

```powershell
cd D:\MatematicaAbierta-Main\audiovisual\manim\cpm_yt_c01_v01
uv run python .\analyze_voice_reference.py
```
