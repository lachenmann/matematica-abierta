# QA de canonización MA-VOICE v1.0

Fecha: 24 de octubre de 2026. Rama: `codex/ma-voice-v1`.
Fuente aprobada: `codex/ma-voice-003`, commit `2fd216ae`.

## Decisión incorporada

El autor aprobó la identidad sintética originada con Qwen3-TTS 1.7B VoiceDesign,
y específicamente **Base · Identidad desde la referencia elegida**,
`NARRACION_clone.wav`, como realización institucional principal. El workflow
predeterminado es Voice Design then Clone mediante Qwen3-TTS 1.7B Base y el WAV
exacto aprobado. La alternativa positiva es únicamente la voz inicial del control
directo. La decisión vocal está aprobada; no queda pendiente una nueva elección
de voz. La auditoría editorial y audiovisual continúa por producción.

## Cambios

- Perfil cerrado `perfiles/MA-VOICE-v1.0`: WAV de referencia, backup raw, narración
  Base aprobada, prompt acústico, configuración, versiones, procedencia y licencias.
- Los 16 insumos copiados se contrastaron byte a byte con el commit aprobado.
  Un archivo adicional conserva una extracción exacta de la alternativa.
  SHA-256 de los 17 archivos, del perfil y del manifiesto protegidos.
- La alternativa exacta cubre [0,000; 11,520) s del audio directo escuchado,
  muestras [0; 552960) a 48 kHz. La coincidencia de muestras PCM se verificó.
  El fin es un límite del primer cue; no se afirma continuidad de identidad vocal
  en todo el segmento ni en el resto de la narración.
- Entrada `audiovisual/manim/narrar.ps1`, defaults MA Video y documentación enlazada.
  Base por defecto; Kokoro `em_alex` como preview explícito.
- Generación local por fragmento, caché con identidad/configuración en su clave,
  rechazo de corrupción, bloqueo de workers simultáneos sobre una misma caché,
  salida nueva por construcción, métricas y manifiesto reproducible `build.json`.
- Diccionario matemático configurable y validación conservadora. No se infiere
  una lectura algebraica ambigua ni se modifica el texto canónico de entrada.
- Ensamblado con pausas sobre fotogramas, WAV, timing, subtítulos de borrador y
  adaptador Manim sin dependencias TTS. Marcadores vinculados al hash del WAV;
  los anclajes semánticos carecen de fallback estimado.

## Verificaciones realizadas

1. **21 pruebas automáticas pasaron**, evidencia `evidencia/tests.txt`:
   índices, exponentes, símbolos, expresiones, nombres, diccionario configurable,
   preservación de texto, IDs y pausas, claves de caché, corrupción, finitud,
   saturación, ensamblado, offset, marcadores, API Base y alternativa exacta.
2. **Modelo real cargado en CPU**, con los pesos oficiales fijados verificados:
   float32, prompt completo ICL, códigos [56,16], embedding [2048], texto de
   referencia correcto. Carga 50,075 s; pico RSS **10,735 GiB**; mínimo libre
   **4,048 GiB**; CPU acumulada 35,969 s de hilos durante el muestreo.
   Cero llamadas nuevas de síntesis. `evidencia/real_backend_smoke.json`.
3. **Integración real desde caché**: importación controlada del primer fragmento
   aprobado, un hit verificado, ensamblado de 11,2667 s, PCM24 mono 24 kHz,
   offset de video exactamente 7 s. WAV, timing, subtítulos y manifiesto de
   construcción producidos por el CLI. `evidencia/integracion_cache.json`.
   No se atribuyen sus tiempos a síntesis nueva.
4. **Entrada PowerShell MA Video ejecutada**: verify, plan y generate desde la
   raíz; el plan del ejemplo está en `evidencia/plan_ejemplo.json`.
5. **Adaptador importado con el Python del entorno Manim existente**: lectura de
   WAV/timing y offset correctos, sin importar Torch. Sin instalación de paquetes
   ni cambio del entorno Manim.
6. **Freeze comprobado con `uv pip sync --dry-run --torch-backend cpu`** contra el
   entorno aprobado: 95 paquetes resueltos, no haría cambios. No se reinstaló el
   runtime ni se afirma una instalación limpia en otro equipo.
7. `compileall` de módulos, pruebas y utilidades pasó. Comprobación de diferencias
   Git realizada antes del commit, sin incluir cambios ajenos a esta intervención.
8. MA-VOICE-002 y MA-VOICE-003 no presentan diferencias respecto del commit fuente.
   Se verificaron por SHA-256 las dos narraciones completas y la referencia original;
   el master original EXP003 conserva su huella previa. El MP4 demo previo también
   conserva una huella registrada en la evidencia. Sin nuevos renders ni alteración
   de WAV, marcadores, guiones, manuscritos o videos anteriores.

## Hallazgos y correcciones durante la integración

- Una prueba detectó que el segmento directo procesado por separado difiere en
  11 de las 552.960 muestras de la extracción del audio completo, en la cola de
  remuestreo. Se conservó el clip anterior y se añadió la extracción PCM exacta,
  sin normalización, fundidos ni regeneración de voz.
- Se endureció la validación para rechazar llaves incompletas en índices/exponentes.
- Se añadió rechazo de entradas de caché incompletas y escritura atómica de archivos.
- Un bloqueo transitorio de limpieza de un directorio temporal en Windows se
  resolvió con reintentos limitados del fixture; la ejecución final pasó completa.
- El SDK advierte ausencia de SoX y flash-attn. La carga CPU eager con prompt
  serializado pasó; no requiere atención CUDA ni extracción nueva de referencia.

## Alcance y límites

No se generaron variantes, no se rediseñó la identidad y no se ejecutó una nueva
narración completa: se preserva la que ya aprobó auditivamente el autor. La llamada
de síntesis del adaptador está cubierta por prueba de contrato y por la carga real
del modelo/prompt; el end-to-end de esta canonización usó caché, deliberadamente.
Kokoro no se volvió a sintetizar ni a evaluar auditivamente en esta intervención.

No se produjo ni se inspeccionó un MP4 nuevo: ésta es una integración de motor.
Los futuros videos deben pasar escucha, revisión de marcadores, auditoría editorial
y QA sobre su master real conforme al protocolo audiovisual. Los subtítulos por
cue son borradores y requieren cortes de lectura. El diccionario no valida
automáticamente la verdad matemática ni detecta todos los nombres propios.
No se declara `PRODUCTION_READY` para ningún video nuevo.

Estado: **MA-VOICE v1.0 integrado y preparado para nuevos experimentos**.
Sin publicación, servicios de pago ni cambios remotos. Los cambios ajenos que ya
existían en el árbol de trabajo se conservaron fuera del commit de integración.
