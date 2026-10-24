# MA-VOICE-003 — voz institucional candidata

Este experimento consolida la muestra sintética elegida por el autor en MA-VOICE-002. La identidad se define por el WAV exacto y su hash, no por volver a inventar una voz desde una descripción.

Entregables producidos:

- `ESCUCHA.html`: referencia elegida, dos narraciones completas y comparación por segmentos.
- `escucha/NARRACION_clone.wav`: Qwen 1.7B Base, condicionado por la referencia sintética aprobada.
- `escucha/NARRACION_direct.wav`: Qwen 1.7B VoiceDesign, control con la descripción original.
- `VOICE_PROFILE.json`: perfil candidato, con aprobación auditiva pendiente.
- `referencia/`: copias exactas del WAV elegido y su original, procedencia y prompt reutilizable en safetensors.
- `guion.json` y `GUION.md`: mismo texto matemático de EXP003, en 18 segmentos.
- `INFORME_TECNICO.md`, `QA_FINAL.md` y `evidencia/`: configuración, recursos, transcripciones y verificaciones.
- `demo/MA_VOICE_003_DEMO.mp4`: demostración cuando la revisión técnica permita integrarla; no constituye aprobación de publicación.

Ejecutar `reproducir.ps1` desde este directorio dentro del repositorio. Requiere uv, FFmpeg, red para recuperar pesos fijados y espacio local. `-RenderDemo` utiliza el entorno Manim existente de EXP003 como intérprete, sin instalar paquetes ni modificar sus fuentes. Las salidas se escriben en esta copia. Los modelos se cargan secuencialmente en CPU.

La síntesis se reanuda por hashes de tomas completas. Los lotes de dos textos registran su tiempo total y el coste amortizado; no se presenta ese coste como una medición aislada de cada frase. Los pesos y entornos no se incluyen en Git ni en el ZIP.

La selección definitiva de voz, acento, naturalidad, timbre, expresividad y ritmo queda pendiente de escucha y aprobación del autor. No se utiliza ninguna grabación humana para la referencia.
