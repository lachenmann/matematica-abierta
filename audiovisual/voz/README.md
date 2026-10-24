# MA-VOICE v1.0

Voz institucional aprobada por el autor el 24 de octubre de 2026:
identidad sintética originada con Qwen3-TTS 1.7B VoiceDesign;
producción mediante **Qwen3-TTS 1.7B Base y la referencia exacta aprobada**.

- [Perfil cerrado](perfiles/MA-VOICE-v1.0/perfil.json)
- [Huellas de insumos protegidos](perfiles/MA-VOICE-v1.0/SHA256SUMS.json)
- [Protocolo técnico y comandos](PROTOCOLO_TECNICO.md)
- [QA de la integración](QA_INTEGRACION.md)

Desde la raíz del repositorio:

```powershell
.\audiovisual\manim\narrar.ps1 -Command verify
.\audiovisual\manim\narrar.ps1 -Command plan -Script audiovisual\voz\ejemplos\guion.json
.\audiovisual\manim\narrar.ps1 -Command generate -Script mi-video\guion.json -Output mi-video\voz-v001
```

La entrada MA Video usa Base por defecto; Kokoro queda como previsualización
explícita. Los proyectos existentes conservan voz, timing y masters originales.
La elección de identidad está aprobada; la calidad de cada guion, animación y
lectura futura sigue requiriendo QA independiente.
