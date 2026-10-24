# MA-VOICE v1.0 — protocolo institucional

Decisión del autor: 24 de octubre de 2026. Rama de integración: `codex/ma-voice-v1`.
Ámbito: narración de nuevos videos automatizados de Matemática Abierta.

La identidad sintética aprobada se originó en **Qwen3-TTS 1.7B VoiceDesign**.
El motor predeterminado es **Qwen3-TTS 1.7B Base**, mediante *Voice Design then Clone*,
condicionado siempre por la referencia aprobada. La aprobación de identidad vocal
está cerrada; cada guion, animación y master conserva su auditoría editorial independiente.
No equivale a aprobar automáticamente futuras lecturas ni videos.

## Insumos cerrados

`perfiles/MA-VOICE-v1.0/perfil.json` registra la decisión y las dos preferencias.
`SHA256SUMS.json` protege 17 archivos, recuperados del commit `2fd216ae` de
`codex/ma-voice-003`, más la extracción exacta de la alternativa.
`config.json` fija también las huellas del perfil y de ese manifiesto.

| Insumo | SHA-256 |
|---|---|
| Referencia sintética exacta `referencia.wav` | `f724ed8b1f3c80e9731d2ea6bf2c480b9f7eef9108f22b04da3d3be895be0c2d` |
| Narración Base aprobada `NARRACION_Base_aprobada.wav` | `87acdafe6e5ef954017af57b9c6c246b2a7db34edcf1623d4ba4692c979a0586` |
| Prompt acústico `voice_clone_prompt.safetensors` | `5c4483ad677cbcc8c564e55a536134864ff5123e0f254f75ed3d2295545bb35b` |

El WAV de referencia es el que escuchó el autor, mono, 48 kHz, PCM24, 4,45 s,
incluido el silencio final original. También se conserva el WAV raw original.
Texto: «Avancemos un índice. Ahora ene vale un millón más uno.»
No recortar, normalizar ni reemplazar ese WAV para crear la identidad.
El prompt contiene embedding **y códigos acústicos**; `icl_mode=True`,
`x_vector_only_mode=False`. No se sustituye por un embedding aislado.

La alternativa positiva es exclusivamente la voz inicial del control directo.
Se conserva el primer cue completo: **[0,000; 11,520) s**, muestras **[0; 552960)**
a 48 kHz de `MA_VOICE_003/escucha/NARRACION_direct.wav`, en
`alternativa_inicial_direct_exact.wav`. Sus muestras PCM coinciden exactamente
con ese intervalo. El límite corresponde al primer segmento del guion, no a una
medición perceptual de un cambio de voz. No se afirma que todo el segmento ni toda
la narración directa mantengan una sola identidad. El clip normalizado por separado
se guarda además como `alternativa_inicial_direct.wav`: difiere mínimamente en la
cola del remuestreo y no es la extracción exacta del audio completo escuchado.
Esta alternativa no participa en la síntesis predeterminada.

## Entorno y modelos

Windows 11, CPU Intel i5-9400, seis núcleos/hilos, 32 GB nominales; CUDA no utilizada.
Python 3.11.16, qwen-tts 0.1.1, torch 2.14.1 CPU, transformers 4.57.3.
Se conserva el freeze completo en `requirements-original.txt`, los scripts originales,
tarjetas de modelos y licencias Apache-2.0. No se instalan paquetes en Manim.

| Papel | Repositorio oficial | Revisión |
|---|---|---|
| Producción Base | Qwen/Qwen3-TTS-12Hz-1.7B-Base | `fd4b254389122332181a7c3db7f27e918eec64e3` |
| Origen histórico VoiceDesign | Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign | `5ecdb67327fd37bb2e042aab12ff7391903235d3` |

Procedimiento oficial: [Qwen — Voice Design then Clone](https://github.com/QwenLM/Qwen3-TTS#voice-design-then-clone).
La fase de diseño ya ocurrió: la producción normal sólo carga Base y el prompt
cerrado. No llama a `generate_voice_design` ni vuelve a diseñar la voz por descripción.
Los pesos existentes de MA-VOICE-003 se reutilizan en lectura. Si se descargan,
se guardan en `audiovisual/voz/models/base17`, sin escribir en experimentos anteriores.
Se verifican todos los archivos de Base contra hashes oficiales archivados,
incluidos pesos SHA-256 y configuración mediante Git blob SHA-1.

Desde la raíz del repositorio:

```powershell
# Ya operativo: reutiliza en lectura el entorno aislado de MA-VOICE-003.
.\audiovisual\manim\narrar.ps1 -Command verify

# Instalación separada en un equipo nuevo; requiere uv y acceso a pesos públicos.
.\audiovisual\voz\setup.ps1 -DownloadModel

# Validar/verbalizar y ver claves de caché; no sintetiza.
.\audiovisual\manim\narrar.ps1 -Command plan -Script ruta\guion.json

# Construcción: especificar una carpeta de salida que todavía no exista.
.\audiovisual\manim\narrar.ps1 -Command generate -Script ruta\guion.json -Output ruta\voz-v001 -Offset 7
```

`setup.ps1` crea `audiovisual/voz/.venv` sólo si no existe y sincroniza el freeze
con backend CPU. No se ejecutó una reinstalación durante esta canonización:
se validó el runtime ya operativo del experimento aprobado. El CLI admite `--model`
para una copia local; exige exactamente los mismos pesos/configuración.
Las llamadas de producción son offline. Una descarga es una operación explícita.

Float32, atención eager, seis hilos intra-op, uno inter-op, seed 20261023 antes de
cargar y antes de cada fragmento, idioma Spanish, máximo 768 tokens nuevos.
Sampling: defaults originales de la revisión fijada, conservados en
`generation_config_original.json` (temperature 0.9, top_k 50, top_p 1,
repetition_penalty 1.05 y parámetros del subtalker).
Para futuros fragmentos el batch es **uno**, con semilla reiniciada por fragmento:
permite editar uno sin alterar los demás. MA-VOICE-003 utilizó primer cue individual
y luego parejas; sus WAV aprobados se conservan y no se presentan como regenerados
bit a bit con el nuevo agrupamiento. Reproducibilidad computacional no garantiza
identidad binaria entre otras CPU, versiones o librerías; conservar la caché y sus hashes.

Se exige al menos 10,5 GiB libres antes de cargar. El worker usa un lock por caché;
ejecutar un único proceso de voz a la vez, sin ASR u otro modelo pesado en paralelo.
Tras una interrupción, comprobar que el proceso terminó antes de retirar un lock
residual. No hay fallback automático a otra voz por falta de RAM o por un error.

## Fragmentos y pronunciación

Entrada JSON compatible con la estructura existente: `segmentos`, cada uno con
`id`, `texto`, `pausa`. `texto` conserva la versión canónica destinada a pantalla;
`hablado`, opcional, permite una lectura editorial explícita. La normalización sólo
actúa sobre el texto enviado al motor; nunca modifica el guion de entrada.
IDs únicos y seguros, pausas finitas no negativas, hasta 65 palabras por fragmento.
Dividir por ideas y cláusulas; no cortar una expresión o hipótesis entre cues.

`pronunciacion/es.json` contiene expresiones, símbolos, letras, números y nombres
propios. `-Dictionary ruta\diccionario.json` selecciona una copia por proyecto.
Las expresiones se marcan con `$...$` o `\(...\)`:

| Entrada | Lectura |
|---|---|
| `$a_n$` | a sub ene |
| `$a_{n+1}$` | a sub ene más uno |
| `$x^2$` | equis al cuadrado |
| `$x^n$` | equis elevado a ene |
| `$1/(n+1)$` | uno dividido por la suma de ene y uno |
| `$≠$` | es distinto de |

Las expresiones algebraicas complejas requieren una entrada exacta; no se adivina
precedencia. Por ejemplo `$a_{n+2}$` se rechaza hasta documentar su lectura.
Los nombres pueden declararse en `nombres` dentro del cue: cada uno debe existir
en el diccionario y en el texto hablado. Las pronunciaciones de nombres son
configurables y requieren revisión editorial. No se detectan automáticamente todos
los nombres propios del lenguaje natural.
Se rechazan cifras y notación residual, TeX crudo, índices/exponentes no resueltos
y expresiones desconocidas. La validación formal no prueba corrección matemática.

## Caché e integridad

Clave SHA-256: texto hablado normalizado, perfil completo, referencia, diccionario,
motor, modelo/revisión, versiones del backend, semilla, tokens y tamaño de batch.
Cada entrada tiene WAV raw y JSON con hash y procedencia. Un hit se verifica contra
sus bytes antes de reutilizarlo. La corrupción bloquea, no dispara una regeneración
silenciosa. Los fragmentos no afectados mantienen su clave al editar otro cue.
Cambiar el diccionario completo invalida conservadoramente las claves, aunque una
entrada concreta no intervenga en el texto. No sobrescribir masters cerrados:
cada construcción exige una carpeta de salida nueva.

`import-approved` sólo admite el primer fragmento exacto de MA-VOICE-003,
que fue generado individualmente con la misma política. Se usa para la prueba real
de integración sin producir variantes. No reetiqueta las parejas originales como
generaciones individuales. `metrics.json` registra hits, tiempo, RAM y CPU; un hit
no se cuenta como síntesis. La caché se debe respaldar junto con los proyectos.

## Sincronización con Manim

Se generan `narracion.wav` PCM24 mono, `timing.json` y
`subtitulos_borrador.srt`. Se preserva la frecuencia de origen (Base: 24 kHz),
sin time-stretch, normalización ni modificación de timbre. Las pausas se redondean
a fotogramas de 1/60 s. El WAV comienza en el tiempo de voz cero; el offset de intro
se aplica al video, los subtítulos y los marcadores, no como silencio duplicado.
La mezcla/master posterior debe exportar audio 48 kHz y registrar sus nuevas huellas.

El timing fija inicio/fin por cue y duración real de habla. Esto **no sustituye**
los anclajes semánticos por palabra. Crear un `marcadores.json` después de escuchar
el WAV, o de revisar una alineación ASR local. Formato:

```json
{
  "audio_sha256": "SHA256 exacto de narracion.wav",
  "markers": [
    {"id": "regla_pronunciada", "cue_id": "potencia", "voice_seconds": 4.25,
     "basis": "reviewed_word_alignment"}
  ]
}
```

Los tiempos son segundos absolutos en el WAV de voz. El ejemplo 4.25 es ilustrativo,
no un marcador medido. `basis` permite `author` o `reviewed_word_alignment`.
`VoiceTimeline` comprueba el hash del WAV, cues, límites y duplicados; rechaza
marcadores sin fuente revisada. `semantic_time()` no ofrece fallback si falta un
marcador. `wait_until()` avisa mediante error si la escena ya pasó el cue.
`ejemplos/escena.py` muestra la integración y requiere marcadores medidos antes de
renderizar. El adaptador usa sólo biblioteca estándar y puede importarse desde Manim
sin importar Torch, Qwen, NumPy ni el entorno de voz. No se ejecutó ese ejemplo de
animación con tiempos ficticios ni se alteró una escena canónica.

Los SRT por cue son borradores: revisar cortes de lectura, longitud, fórmulas,
hipótesis y sincronización, y subdividirlos por palabras antes de un master final.
Los marcadores del autor prevalecen sobre cualquier alineación automática.

## Kokoro para pruebas

`-Engine kokoro-preview` es una elección explícita, voz `em_alex`, idioma `es`,
velocidad 1.0. Requiere `-Python` apuntando a un entorno Kokoro existente y rutas
`-KokoroModel`, `-KokoroVoices`. No instala nada en ese entorno.
Modelo y voces se incluyen por SHA-256 en la clave de caché. No mezclar su timing
con el de Base. La revisión definitiva se realiza con Base y el WAV definitivo.

## QA y continuidad

Antes de `VOICE_LOCKED`: verificar perfil/modelo, revisar lectura matemática,
ausencia de omisiones/repeticiones, timbre, pausas, acento y expresividad por escucha.
Verificar finitud, ausencia de saturación y duración; medir LUFS/true peak de la
mezcla y ajustar el nivel global de manera documentada si hace falta.
La identidad aprobada no autoriza a ignorar un fallo de dicción de una toma nueva.

Antes de `SEMANTIC_TIMING_READY`: vincular marcadores al hash del WAV y revisar
las entradas importantes contra el habla real. Antes de `PRODUCTION_READY`:
aplicar además `audiovisual/manim/AUDIOVISUAL_PRODUCTION_PROTOCOL.md` al MP4 final,
incluyendo inspección cronológica, transiciones críticas, resolución completa,
audio y deriva. La auditoría editorial sigue siendo independiente.

Pruebas:

```powershell
Push-Location audiovisual\voz
.\experimentos\MA_VOICE_003\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\experimentos\MA_VOICE_003\.venv\Scripts\python.exe smoke_backend.py
Pop-Location
```

La segunda prueba carga el modelo real y el prompt aprobado en CPU, sin sintetizar
una variante. Las pruebas unitarias cubren integridad, normalización, caché corrupta,
ensamblado, offset, marcadores, llamada Base y límites exactos de la alternativa.
No confundir estas pruebas con una auditoría pedagógica o audiovisual del master.

Se conservan íntegros los WAV, marcadores, audios y videos anteriores. Los perfiles
cerrados cambian creando otra versión con decisión explícita del autor; no editar
v1.0 para cambiar de referencia. Este protocolo no habilita publicación remota.
