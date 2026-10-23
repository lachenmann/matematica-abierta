# Protocolo canónico de producción audiovisual
## Cálculo para matemáticos — Matemática Abierta

**Versión:** 2.0 — 5 de octubre de 2026
**Referentes:** V01 como identidad visual; V02 cerrado y publicado por confirmación del autor el 5 de octubre de 2026.
**Principio rector:** el guion gobierna la animación; el render final gobierna el QA.

---

## 1. Estados del video

Cada video avanza por estos estados:

```text
SCRIPT_DRAFT → SCRIPT_LOCKED
→ VOICE_LOCKED
→ SEMANTIC_TIMING_READY
→ REPRESENTATIVE_SAMPLE
→ ANIMATION_DRAFT
→ ANIMATION_REFINEMENT
→ AUDIOVISUAL_QA
→ ANIMATION_LOCKED
→ FINAL_EDIT
→ FINAL_MASTER_QA
→ PRODUCTION_READY
→ PUBLISHED_CLOSED
```

No pasar a `PRODUCTION_READY` por compilación correcta ni por existencia del MP4.
El último gate es siempre una auditoría audiovisual del render final.

---

## 2. Fuentes y artefactos

Para cada video deben existir, como mínimo:

- guion canónico;
- plan visual;
- fuente Manim de producción;
- WAV definitivo;
- proyecto Reaper o fuente equivalente, cuando exista; no exigirlo si el WAV definitivo basta;
- archivo de timing/marcadores;
- script de render de producción;
- master MP4;
- informe `QA_FINAL.md`.

El WAV y el proyecto de edición de voz se consideran **insumos protegidos** una vez
cerrados. Antes del QA final se registran sus SHA-256.

---

## 3. Regla audiovisual fundamental

La pantalla sigue la semántica de la voz.

Si la voz dice:

```text
A → B → C
```

la pantalla debe acompañar cada idea en su momento. Puede conservar el contexto,
transformarlo o sustituirlo; no acumular automáticamente A, B y C en pantalla.

No debe mostrar información antes de que sea pronunciada.

Esto se aplica a:

- fórmulas;
- listas;
- axiomas;
- propiedades;
- tablas;
- definiciones;
- hipótesis;
- ejemplos;
- consecuencias;
- preguntas.

Una escena estática mientras la voz desarrolla varias ideas es un defecto de
ritmo salvo que la inmovilidad tenga una función deliberada.

---

## 4. Principios de animación matemática

### 4.1 Transformaciones

- Un cambio matemático sustantivo por transición.
- Evitar recorridos que atraviesen otros operandos.
- Para intercambios de posición, usar trayectorias separadas.
- Para reagrupar paréntesis, usar carriles que no crucen los símbolos.
- Para distribuir o factorizar, mover copias por rutas externas a la expresión.
- No dejar copias residuales, dobles objetos ni símbolos huérfanos.

### 4.2 Entrada y salida

No fundir simultáneamente dos fórmulas incompatibles sobre la misma zona.

Patrón preferido:

```text
salida de fórmula A
→ breve separación
→ entrada de fórmula B
```

### 4.3 Tiempo de lectura

Después de una transformación importante, la expresión final debe permanecer
lo suficiente para ser leída.

No fijar una pausa universal: ajustarla según densidad matemática y locución.

### 4.4 Hipótesis

Las hipótesis necesarias, por ejemplo `a\neq0`, permanecen visibles mientras
justifican el paso correspondiente.

### 4.5 Tipografía

- Matemática: `MathTex`.
- Rótulos: `Tex`.
- Evitar rasterizar matemática.
- Mantener escalas y alineaciones consistentes.
- Verificar legibilidad real en 1920×1080.

---

## 4.6 Refinamiento audiovisual en Work

El caso piloto mostró que la inspección del **render real** permite mejorar
sustancialmente animaciones que parecen correctas al leer el código.

Por tanto, antes de declarar `ANIMATION_LOCKED`, los videos deben pasar por una
fase explícita de `ANIMATION_REFINEMENT` en Work cuando esté disponible el
entorno local.

Work debe recibir acceso al repositorio local y a un render completo, y ejecutar
iterativamente:

```text
ver render
→ detectar problemas de movimiento/composición/ritmo
→ corregir Manim
→ renderizar
→ volver a inspeccionar
```

Esta fase no es sólo corrección de errores. También puede mejorar:

- trayectorias de objetos;
- separación espacial de operandos;
- movimiento de paréntesis;
- ritmo de entrada y salida;
- permanencia de estados finales;
- jerarquía visual;
- progresión semántica de fórmulas y listas;
- composición de tarjetas y tablas;
- continuidad entre escenas.

La calidad del movimiento debe juzgarse por el video resultante, no por la
elegancia aparente del código.

El diseño parte del WAV definitivo y del texto canónico. El autor no necesita
escribir instrucciones de animación frase por frase. El realizador segmenta por
microtramos semánticos y diseña el apoyo visual con libertad dentro del protocolo.

El chat de diseño/redacción puede producir la primera implementación, pero
`ANIMATION_LOCKED` sólo se alcanza después de inspección visual del render y
refinamiento suficiente.

## 5. Sincronización

La voz definitiva se sincroniza mediante marcadores canónicos.

Los tiempos absolutos fijados por el autor tienen precedencia sobre
interpolaciones aproximadas.

Toda entrada visual importante debe corresponder a:

- marcador canónico, o
- cue absoluto documentado.

El código no debe anticipar la locución sólo porque exista tiempo libre antes
del siguiente marcador.

---

## 6. Render de producción

El script de producción debe:

1. validar WAV y proyecto de voz si está disponible;
2. validar marcadores y rechazar duplicados;
3. regenerar assets derivados cuando corresponda;
4. comprobar sintaxis Python;
5. renderizar sin caché obsoleta;
6. producir el master estable en `exports/`;
7. generar SHA-256 del master.

Estándar actual:

- 1920×1080;
- 60 fps;
- H.264;
- audio AAC 48 kHz.

---

## 7. QA audiovisual autónoma

El QA final se realiza sobre el MP4, no sólo sobre el código.

### Pasada A — cronológica

Inspeccionar todo el metraje mediante extracción suficiente para conservar:

- cambios visuales;
- pausas;
- estados persistentes;
- transiciones.

El caso piloto usó extracción base a 4 fps y láminas de contacto.

### Pasada B — secuencias críticas

Revisar a mayor densidad temporal las animaciones con riesgo de colisión:

- `Transform`;
- `TransformMatchingTex`;
- intercambios de operandos;
- paréntesis;
- distribución/factorización;
- pertenencia a conjuntos;
- solución de ecuaciones;
- cambios de encabezado.

El caso piloto usó 12 fps para secuencias críticas.

### Pasada C — resolución completa

Comprobar a resolución completa:

- tarjetas;
- tablas;
- títulos;
- márgenes;
- textos densos;
- objetos próximos al borde;
- superposiciones;
- alineaciones.

### Pasada D — cues fijos

Para cada tiempo fijado por el autor revisar, como mínimo, fotogramas alrededor de:

```text
t − 0,10 s
t + 0,10 s
t + 0,45 s
t + 1,30 s
```

Esto verifica que:

- la pantalla anterior haya salido;
- la nueva no entre antes;
- la animación comience en el cue;
- el estado resultante sea legible.

---

## 8. Clasificación de defectos

### BLOCKER

Impide publicación:

- error matemático;
- audio ausente o incorrecto;
- render roto;
- fórmula ilegible;
- desincronización grave;
- contenido faltante.

### MAJOR

No impide reproducir el archivo, pero exige corrección antes de publicar:

- anticipación semántica;
- colisiones de símbolos;
- superposición de fórmulas incompatibles;
- ritmo claramente incorrecto;
- escenas extensamente estáticas contra la narración;
- contenido relevante fuera del marco;
- transformación visualmente falsa o confusa.

### MINOR

Defecto perceptible que no altera el razonamiento:

- alineación secundaria;
- espaciado;
- escala ligeramente inconsistente;
- color no uniforme.

### COSMETIC

Preferencia estética sin impacto pedagógico.

**Gate de publicación: 0 BLOCKER y 0 MAJOR.**

---

## 9. Ciclo correctivo obligatorio

```text
render
→ inspección
→ registro de defectos
→ corrección de código
→ validación estática
→ nuevo render
→ reinspección
```

Repetir hasta alcanzar el gate.

Nunca asumir que una corrección no produjo un defecto secundario.

---

## 10. Validación técnica final

Antes de cerrar:

- `python -m py_compile`;
- `git diff --check`;
- verificadores específicos de layout si existen;
- ausencia de `SYNC WARN` significativos;
- SHA-256 de WAV igual al inicial y de RPP si se ha recibido;
- verificación de audio del master contra el WAV en varios puntos de la línea temporal;
- comprobación de ausencia de deriva;
- SHA-256 del MP4 final.

---

## 11. Informe QA_FINAL

Cada video debe cerrar con:

```text
<directorio-del-video>/QA_FINAL.md
```

Debe registrar:

- fecha;
- rama;
- master auditado;
- fuente Manim;
- método de inspección;
- hallazgos y correcciones;
- tiempos fijos;
- número de renders;
- insumos protegidos y hashes;
- validaciones técnicas;
- defectos abiertos por severidad;
- duración, resolución y fps;
- SHA-256 del master final;
- ubicación de evidencias locales.

---

## 12. Evidencia local

Los siguientes artefactos pueden quedar fuera de Git:

- MP4 final;
- fotogramas;
- láminas de contacto;
- transcripción auxiliar;
- metadatos de inspección;
- verificaciones de audio.

Guardar bajo `exports/` o subdirectorios equivalentes.

El informe `QA_FINAL.md` sí se versiona.

---

## 13. Regla para Work

Para QA final, Work debe trabajar con acceso local al repositorio y al MP4.

Prompt mínimo recomendado:

> Aplica `AUDIOVISUAL_PRODUCTION_PROTOCOL.md` al video actual. Mira el master,
> corrige autónomamente los problemas BLOCKER/MAJOR, renderiza, vuelve a
> inspeccionar el nuevo MP4 y repite hasta cerrar el gate. No cambies guion ni voz.

Work no debe cerrar la tarea sólo porque Manim renderice correctamente.

---

## 14. Lecciones del caso piloto

El primer video demostró que los defectos más frecuentes no eran matemáticos
sino temporales y espaciales:

- soluciones mostradas antes de ser pronunciadas;
- listas completas mostradas antes de su enumeración;
- símbolos que compartían trayectoria;
- paréntesis atravesando operandos;
- fórmulas incompatibles solapadas durante fundidos;
- escenas estáticas durante locuciones largas;
- contenido correcto pero demasiado rápido para ser leído.

Por tanto, el QA de futuros videos debe tratar **ritmo y semántica temporal**
como propiedades de corrección, no sólo como decisiones estéticas.


## 15. Flujo operativo desde V03

Aplicar conjuntamente este documento y [PROTOCOLO_VISUAL_CANAL.md](PROTOCOLO_VISUAL_CANAL.md). El primero gobierna producción y evidencia; el segundo, el lenguaje visual. Para empezar V03, consultar [cpm_yt_c01_v03/PRODUCTION_BRIEF.md](cpm_yt_c01_v03/PRODUCTION_BRIEF.md).

- Recibir WAV definitivo y localizar el texto canónico en Obsidian/repositorio. Registrar fuentes, duración, silencios, huellas y offset de intro de 7 s. No inventar tiempos ni contenido cuando falta el audio.
- Preparar un único mapa de microtramos con tiempos de voz/video, anclaje oral, hipótesis, objeto activo, transformación, énfasis y permanencia. Mantener contenido/timing separados del motor de animación.
- Revisar una muestra representativa de 2–3 minutos antes de extender el diseño. Reutilizar V01 y las decisiones cerradas de V02; no someter cada escena rutinaria a aprobación.
- Render de revisión completo a 720p30, revisión con audio y correcciones; producción a 1080p60 sólo después. Revisar inicio y último minuto como bloques completos, además de demostraciones y transiciones.
- Usar una sola orden de construcción reproducible por video y un registro acumulado de correcciones. Evitar una cadena de scripts de parches que dependa de masters intermedios. Para correcciones locales, documentar intervalos, base, huellas y uniones; verificar duración, fotogramas y audio.
- Registrar el alcance real del QA: muestreo visual, revisión audiovisual de intervalos o visionado continuo. Las láminas no prueban sincronización semántica ni escucha continua. Asociar evidencia al master vigente.
- Entregar master, miniatura, textos de YouTube y capítulos derivados del timing real. Publicación sólo cuando la autorice o confirme el autor; registrar URL si la proporciona.

## 16. Cierre y continuidad

V02 quedó **PUBLISHED_CLOSED** por confirmación del autor el 5 de octubre de 2026. Su master local y huella constan en cpm_yt_c01_v02/QA_PRODUCTION_FINAL.md. No se verificó una URL pública y no se exige para registrar esta confirmación. No rerenderizar ni modificar V02 para preparar V03; reutilizar sus componentes mediante importación o extracción a módulos compartidos, conservando la fuente publicada.

Mantener separadas la aprobación editorial del autor y la evidencia técnica del QA. El cierre no transforma un muestreo previo en revisión continua.
