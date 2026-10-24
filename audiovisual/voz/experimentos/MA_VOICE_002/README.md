# MA-VOICE-002

Abrir **ESCUCHA.html** en un navegador para alternar las siete muestras locales. Todos los WAV comparativos están en **escucha/** y tienen −24 LUFS mediante ganancia constante, sin compresión ni cambio de velocidad. Ajustar el volumen del sistema una sola vez.

- [Informe técnico](INFORME_TECNICO.md): tiempos, recursos, licencias y recomendación operativa provisional.
- [QA final](QA_FINAL.md): verificaciones realizadas, límites y segundos concretos para escuchar «ene».
- [Pauta de escucha](PROTOCOLO_ESCUCHA.md): evaluación perceptual y selección pendiente.
- `raw/`: salidas sin normalizar y tomas parciales de Qwen.
- `evidencia/`: métricas, transcripciones, procedencia y hashes.
- `reproducir.ps1`: reconstrucción desde este directorio dentro del repositorio, con Python 3.11.16, uv y FFmpeg. Lee las tomas de EXP003 para reconstruir la referencia; no las modifica.
- `models/` y `.venv/`: pesos y entorno local conservados, excluidos de Git y del ZIP.

El ZIP incluye WAV, código, documentación y evidencias; los pesos se recuperan mediante las revisiones fijadas. VoiceDesign es una prueba breve adicional de timbre diseñado, sin clonación, y no una voz predefinida. No hay una ganadora sonora declarada antes de la escucha.
