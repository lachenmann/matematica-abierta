# Protocolo canónico de producción audiovisual
## Cálculo para matemáticos — Matemática Abierta

**Versión:** 1.0  
**Caso piloto validado:** `CPM-YT-C01-V01 — Los axiomas de cuerpo`  
**Principio rector:** el guion gobierna la animación; el render final gobierna el QA.

---

## 1. Estados del video

Cada video avanza por estos estados:

```text
SCRIPT_DRAFT
→ SCRIPT_LOCKED
→ ANIMATION_DRAFT
→ ANIMATION_REFINEMENT
→ ANIMATION_LOCKED
→ VOICE_LOCKED
→ FINAL_EDIT
→ AUDIOVISUAL_QA
→ PRODUCTION_READY
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
- proyecto Reaper o fuente equivalente;
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

la pantalla debe construir:

```text
A
→ A + B
→ A + B + C
```

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

1. validar WAV/proyecto de voz;
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
- SHA-256 de WAV/RPP igual al inicial;
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
