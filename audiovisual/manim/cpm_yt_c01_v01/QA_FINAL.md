# CPM-YT-C01-V01 — Auditoría audiovisual final

Fecha: 2026-10-03. Rama de entrega: `prototype/ma-cls-c13`.

## Alcance y método

- Master local: `exports/CPM-YT-C01-V01-production.mp4`.
- Fuente: `clases/cpm_yt_c01_v01_production.py`.
- Inspección visual cronológica de todo el metraje mediante fotogramas del MP4,
  conservando las transiciones y muestras de las pausas; revisión adicional de
  movimientos, cambios de encabezado, paneles y tiempos fijos.
- Comparación de entradas visuales con transcripción auxiliar local de la toma
  continua, con tiempos de palabra. La transcripción no sustituye ni modifica
  el guion, el WAV, el proyecto Reaper o sus marcadores.
- Render integrado mediante `render-cpm-yt-c01-v01-production.ps1`.
- Los masters, fotogramas y transcripción auxiliar permanecen en `exports/`,
  fuera de Git. La inspección final se registra abajo después del render.

## Hallazgos del master inicial y correcciones

| Severidad | Tramo | Problema | Corrección |
|---|---|---|---|
| MAJOR | 00:25–00:36 | La solución de la ecuación aparece antes de su frase | Escritura de suma, producto y ecuación por separado; solución posterior |
| MAJOR | 01:04–01:47 | Cadena y ampliación a los racionales entran completas demasiado pronto | Aparición por sistema numérico y espera antes de la ampliación |
| MAJOR | 03:27 / 04:26 | Paréntesis atraviesan operandos al reagrupar | Carriles superior e inferior para los paréntesis |
| MAJOR | 04:15 / 05:22 | Las letras que intercambian posiciones comparten trayectoria | Semicírculos opuestos; verificación de separación durante el recorrido |
| MAJOR | Igualdades y encabezados | Fundidos simultáneos superponen textos incompatibles | Salida de la expresión anterior antes de la entrada de la nueva |
| MAJOR | 05:38–05:59 | Copias de factores cruzan los sumandos y se superponen al reunirse | Traslado de las copias por un carril superior; retirada antes de reponer los paréntesis |
| MAJOR | 06:06–06:47 | Definición y caso trivial muestran resultados antes de su explicación | Construcción por conjunto, operaciones, elementos y condición; operaciones triviales separadas |
| MAJOR | 07:16–07:40 | Recapitulaciones anticipan las propiedades individuales | Encabezados en los tiempos fijos y filas según las palabras de la voz |
| MAJOR | 08:33–09:49 | Resultados de F₂ e inverso aparecen antes de mencionarse; atención estática | Resultado de suma y pasos de producto/inverso separados; énfasis al retomar el ejemplo |
| MAJOR | 09:56–10:38 | Fracciones del intervalo no siguen la enumeración de propiedades pendientes | Entradas vinculadas a frases concretas, incluida resta/división |
| MAJOR | 11:07–11:34 | Fórmulas de la suma desbordan su tarjeta; evaluación adelantada | Dos filas para la suma, ajuste al marco y entradas sincronizadas |
| MAJOR | 11:35–11:49 | Ecuación completa y solución del inverso de dos adelantadas | Ecuación en 11:41 y solución en 11:46 |
| MAJOR | 12:15–13:15 | Conceptos de orden y preguntas finales entran en bloque o antes de su frase | Rótulos, ejemplos y preguntas revelados por separado |
| MINOR | Tablas de axiomas | Columnas variables y colores inconsistentes en igualdades | Columnas alineadas; variables aisladas con colores estables y operadores neutros |

## Tiempos fijos del autor

| Tiempo del video | Acción |
|---|---|
| 05:06.000 | Énfasis de `a≠0`; la hipótesis permanece visible desde su definición verbal |
| 07:16.000 | Entrada del encabezado de estructura aditiva |
| 07:29.000 | Entrada del encabezado de estructura multiplicativa |
| 07:40.000 | Entrada del encabezado de distributividad |
| 12:15.000 | Entrada de «Lo que todavía no hemos supuesto» |

Los paneles anteriores salen antes de cada cambio; el contenido nuevo no entra
antes del tiempo fijado. Las animaciones de entrada comienzan en ese tiempo y
alcanzan su opacidad completa después.

## Segunda pasada

La primera exportación corregida se inspeccionó de principio a fin y no se
aprobó: todavía superponía ecuación y solución en 01:42 y 11:46, y etiquetas
de pertenencia en sus cambios. Además, dejaba símbolos aislados al introducir
los inversos y conservaba F₂ cuando la voz retomaba el inventario de axiomas.
La segunda pasada separa esas salidas y entradas, usa un compañero «?» antes
de nombrar el inverso, recupera el inventario en 09:37 y añade la pregunta
de resta/división en 13:18 sin anticipar sus definiciones.

## Insumos protegidos

SHA-256 de los originales, comprobados antes de las correcciones:

- WAV: `7815b285c543ee1a04542702fda1d4a6423afcca95c00c73d497be2f312a48c7`.
- RPP: `fdcd38c74d65d286ca8c2de05fc262a2470c7804b02ca882e754344cc7cc3f74`.

## Validación final

Resultado de la segunda exportación: **0 BLOCKER y 0 MAJOR abiertos**.

- Exportación realizada con el script oficial: 1920×1080, H.264, 60 fps,
  audio AAC estéreo a 48 kHz; duración 821,120 s (13:41,120).
- Inspección cronológica de principio a fin: extracción a 4 fps de todo el MP4,
  1020 fotogramas seleccionados por cambio visual y muestras de las pausas,
  examinados en las 43 láminas `exports/audit-render-2/sheet-00.jpg` a
  `sheet-42.jpg`. Este método es revisión por fotogramas, no una afirmación de
  reproducción continua a velocidad normal.
- Revisión adicional de siete secuencias a 12 fps: soluciones en 01:42 y
  11:46, pertenencia en 11:50, conmutatividad de suma y producto, expansión
  distributiva y factorización. Sin colisiones de operandos ni fundidos de
  fórmulas incompatibles.
- Verificación a resolución completa de las tarjetas de enteros, inventario
  de axiomas y cierre; último fotograma inspeccionado en 821,05 s.
- Los cinco hitos coinciden con el tiempo de la escena a 60 fps y se revisaron
  también en fotogramas a −0,10 / +0,10 / +0,45 / +1,30 s de cada hito.
- Las tres comprobaciones de `verify_production_layout.py` pasan; comprobación
  de sintaxis y `git diff --check` sin errores. Render: 400 animaciones,
  sin avisos `SYNC WARN`.
- WAV y RPP conservan los SHA-256 anteriores. La voz decodificada del master
  se comparó con el WAV en ventanas de cinco segundos en 30, 120, 210, 300,
  450, 600, 735 y 800 s: correlaciones 0,9965–0,9983, desplazamiento uniforme
  de decodificación de +21,3125 ms respecto de la entrada nominal a 7 s,
  sin deriva entre el inicio y el final. No se modificó la voz ni el guion.

SHA-256 del MP4 final:
`a0d57a41781c0f56fa47a9c4585d6349c7f68d9d70be328fea4eeb3fbadd460d`.

Las evidencias locales quedan en `exports/audit-render-2/`, incluidas
`fixed-cues.jpg`, `metadata.json` y `audio-verification.json`. El master y las
evidencias se mantienen fuera de Git conforme a las exclusiones del proyecto.
