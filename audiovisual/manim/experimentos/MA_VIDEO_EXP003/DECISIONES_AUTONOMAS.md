# Decisiones autónomas — EXP003

## Del texto a la película

El trabajo comenzó leyendo el pasaje fuente, antes de escribir el guion. La sección desarrolla una dificultad de información: un prefijo finito puede compartir distintas continuaciones. Se eligió la pregunta «¿qué podemos afirmar sobre lo que ocurre después?» como hilo conductor. La idea constitutiva del cierre es estudiar todos los términos suficientemente tardíos; no se introduce todavía una definición formal de límite.

La lectura inicial produjo GUION_PROPUESTO.md. Un agente matemático independiente señaló la distinción entre observar datos y conocer las reglas completas. La pareja concreta se distingue en n=10^6+1; una muestra que incluya ese índice sí la separa. Esta precisión gobierna el guion definitivo, sin convertir la imposibilidad de extrapolar en una imposibilidad de distinguir cualquier pareja.

Se sustituyeron lecturas poco naturales de números grandes por «la suma de un millón y uno/dos». También «uno dividido por ene más uno» por «uno dividido por la suma de ene y uno», para explicitar el alcance del denominador al oído. La formulación del conteo separa el millón de términos del término de índice cero. No se cambiaron valores ni hipótesis.

La dirección visual propuso una ventana local y una tabla exacta en la frontera: permite leer 1/(10^6+1) y 1/(10^6+2) sin fingir que un valor próximo a cero es cero. El gráfico inicial contiene puntos discretos; el avance del selector representa la inspección, no valores entre índices. El tramo omitido se rotula expresamente.

La generalización extiende un esquema de índices con extremo finito N. La imagen conserva una continuación después de cada extremo. Así el movimiento representa el razonamiento de elegir un prefijo más largo, sin sugerir una comprobación de infinitos términos.

## Funciones y separación

- Pedagogía: subagente independiente, estudio de fuente y guion original.
- Matemática: subagente independiente, auditoría del texto y validador racional exacto.
- Dirección visual: subagente independiente, storyboard original y riesgos de escala.
- Programación: subagente independiente, escena Manim nueva; agente principal integra y ejecuta la producción.
- Narración: subagente independiente, Kokoro local y alineación auxiliar por palabra.
- Auditoría audiovisual: función independiente sobre el MP4; agente principal aplica correcciones y consolida evidencia.

No se reutilizan guiones, storyboards ni animaciones matemáticas de los experimentos anteriores. Se reutilizan el motor de síntesis, las utilidades de ensamblado/QA y la intro institucional de 7 s con música acreditada. Los motivos de la intro pertenecen a la marca; el desarrollo matemático procede exclusivamente del pasaje.

Azul identifica a; violeta identifica b. La estabilidad de estos colores ayuda a seguir su identidad durante la comparación. Verde expresa el intervalo común; naranja, la pregunta o el corte. Esta asignación se documenta como adaptación pedagógica de la paleta canónica.

## Autonomía y validación

El usuario proporcionó fuente, objetivo, restricciones y criterios; no proporcionó guion ni escenas. Las decisiones narrativas y visuales fueron generadas por los agentes. La infraestructura realiza síntesis, sincronización, render, ensamblado, extracción y pruebas; esa automatización técnica se distingue de las decisiones editoriales anteriores.

No se requirió aprobación humana intermedia para decisiones de realización. La escucha humana crítica queda como validación editorial posterior, según la solicitud. Los tiempos, renders y defectos efectivamente encontrados se completan en QA_FINAL.md y generados/renders.json; no se convierten controles automáticos en aprobación editorial.

## Hallazgo del MP4 y revisión de dirección

La primera película completa hizo visible un fallo que el código no hacía evidente: `set_opacity(.18)` aumentaba el relleno del rectángulo de prefijo desde .045 a .18. En el cierre el comienzo se volvía más visible al hablar de términos tardíos. El agente principal y el auditor independiente identificaron ese mismo MAJOR. Se modificaron separadamente opacidad de trazo y relleno, y sólo los puntos del prefijo se atenúan. Los puntos posteriores, la flecha y el subrayado se destacan simultáneamente con la frase final. La nueva película preliminar fue reinspeccionada a12fps y en detalle nativo; el auditor confirmó el cierre de AV-001. Esta corrección es una decisión de foco pedagógico surgida de inspeccionar el video, no sólo una reparación de compilación.

También se corrigió un problema de cuantización de la intro a30fps y una carrera de lectura de guion que afectó dos tomas; las firmas de caché permitieron regenerar únicamente esos fragmentos. Los registros originales y definitivos se conservan separados. No se detectaron errores matemáticos sustantivos en el guion; las precisiones sobre datos/reglas y denominadores previnieron ambigüedades.

## Refinamiento de subtítulos

La prueba real con el SRT activado reveló otra colisión: el párrafo completo del cierre ocupaba cuatro líneas y cubría la conclusión. Se dividió todo el texto canónico en42 segmentos de hasta dos líneas de42 caracteres, sin resumir ni cambiar palabras. Los límites usan la alineación de los WAV definitivos y, sólo donde falta correspondencia léxica ASR, interpolación entre palabras vecinas. El inicio de cada bloque registra su método en timing_subtitulos.json. La vista corregida de177s deja la conclusión libre. Se conserva la animación y la voz; el cambio sólo requiere reensamblar la pista de subtítulos. La apariencia de una pista seleccionable depende también de las preferencias del reproductor.
