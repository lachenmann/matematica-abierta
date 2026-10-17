# Informe de la segunda pasada editorial — candidata v04

**Física para matemáticos — Tomo I: Fundamentos y mecánica** · A. Peña · Matemática Abierta.

Esta pasada responde a los títulos sin contenido, las diferencias de escala y la insuficiencia visual señalados en la candidata v03. El resultado es un proyecto AMSBook autocontenido y dos PDF compilados. La edición sigue siendo candidata: no se ha canonizado ni publicado y no se han modificado la web, GitHub ni los manuscritos de la bóveda.

## Encabezados

Se retiraron **27 epígrafes realmente vacíos**: diez en el capítulo 2, seis en el 3 y once al final de los capítulos 8–10 y 15–22. Entre ellos estaban «Notas y referencias». Se conservaron sus anclas, las notas al pie y las bibliografías con contenido. No se inventó texto para llenar esos rótulos.

Se protegieron **83 cadenas de encabezados consecutivos**, reservando espacio para el título, su subtítulo y el comienzo del contenido. La primera prueba de carta confirmó un caso real en la sección «Incertidumbre relativa y comparación de escalas»; la compilación final lo mantiene unido a su desarrollo. Se distinguieron de ese defecto los epígrafes corridos, como «Conclusión» o «Precisar», cuyo texto comienza en la misma línea.

El cotejo final encuentra 2246 de 2263 títulos por cadena en A4 y 2249 en carta, sin candidatos de título aislado al pie de página. Los títulos no reconocidos por cadena incluyen rótulos de una letra, símbolos matemáticos o expansiones formales. Sus páginas se incluyeron en las pruebas visuales; la cifra de coincidencias no se presenta como prueba de lectura integral. Se conserva el registro de los epígrafes retirados y de las cadenas protegidas.

También se corrigieron erratas inequívocas como «capítulo capítulo», «hacial capítulo» y «paral capítulo», y tres frases de estado de producción que ya no correspondían a un libro compuesto.

## Densidad y escala de las figuras

Se añadieron **61 figuras pedagógicas**, elevando el total de 115 a **176**: 155 figuras nuevas con fuente TikZ editable y 21 originales preservadas. Los seis primeros capítulos pasan de tres figuras cada uno a 9, 9, 8, 8, 8 y 7, respectivamente. Los capítulos 7–13 reciben dos más cada uno y los capítulos 14–29 una más cada uno. El capítulo 30 conserva sus veinte ilustraciones.

Las adiciones tratan unidades y escalamiento, incertidumbre y transformaciones no lineales, proyecciones y cambios de marco, regularidad de curvas, límites no uniformes y cotas, reconstrucción cinemática, alcance y altura del proyectil, sistemas y fuerzas externas, contacto unilateral, fricción, Atwood, trabajo firmado, dominios perforados, colisiones, brazos de torque, cáscaras esféricas, retornos radiales, focos orbitales, dispersión, Coriolis, rodadura, precesión, desfase, intercambio modal, trabajo virtual, coordenadas acopladas, simetrías y variables canónicas.

La escala se asigna **por figura**, con anchuras y alturas registradas en puntos. Los esquemas estrechos y pequeños reciben ampliación moderada; las láminas originales se compactan manteniendo rótulos legibles. Las figuras nuevas tienen límite de 200 pt de alto y las originales de 270 pt; ninguna imagen necesita una página completa. La anchura queda dentro de la mancha de ambos formatos. La legibilidad se contrastó en página, no sólo en archivos de figura aislados.

La lámina F18 del capítulo 30 se recompuso horizontalmente en TikZ: mismas tres soluciones, mismo dato inicial y misma ventana temporal. Se cotejaron sus 603 puntos con la fórmula original, con error máximo de redondeo inferior a 3,2×10⁻⁷ en el radio. Se conservaron intactos tanto el PDF como el SVG originales. El inventario distingue la fuente histórica de la copia de composición.

Se revisaron y corrigieron rótulos superpuestos. Se muestran extremos abiertos a ambos lados de la discontinuidad del campo de una cáscara ideal. Dos adiciones inicialmente redundantes se diferenciaron antes de cerrar la edición: el proyectil muestra ahora altura y alcance; el esquema de dos cuerpos muestra el balance de fuerzas internas y externas. Las flechas de fuerza, velocidad, aceleración y variación virtual conservan su interpretación explícita en el epígrafe.

## Conservación y controles científicos

- 30 capítulos y **900 ejercicios con 900 soluciones** conservados. Los 900 identificadores se localizaron en cada PDF.
- **222 notas al pie** conservadas. Las fuentes originales de cotejo y los 42 archivos gráficos originales PDF/SVG permanecen idénticos byte a byte.
- La secuencia matemática del cuerpo de cada capítulo coincide con v03, excluyendo únicamente las figuras y sus epígrafes. Se incluyen los treinta diffs v03→v04.
- Se repitieron los 52 controles analíticos/numéricos del programa visual previo y las reproducciones independientes del mapa estándar y del péndulo forzado.
- Las 61 adiciones tienen controles analíticos, numéricos, geométricos o de alcance conceptual según su contenido. Los diagramas cualitativos se declaran como tales; las barras de medición no reciben una interpretación estadística injustificada.

Estos controles no sustituyen una nueva auditoría matemática completa de cada demostración del tomo.

## Compilación y auditoría final

Se conservan `amsbook`, 11 pt, Computer Modern Unicode, New Computer Modern Math, XeLaTeX y las optimizaciones de párrafo y ecuaciones en línea de v02. Se realizaron tres pasadas completas de XeLaTeX por formato y la conversión final con `xdvipdfmx`, comprobando el cierre de auxiliares y las 176 etiquetas de figura.

| Control | A4 | Carta |
|---|---:|---:|
| Páginas | 1140 | 1230 |
| Capítulos en navegación PDF | 30 | 30 |
| Epígrafes de figura | 176 | 176 |
| Errores de compilación | 0 | 0 |
| Referencias o citas indefinidas | 0 | 0 |
| Glifos faltantes | 0 | 0 |
| Desbordamientos horizontales | 0 | 0 |
| Texto fuera del margen físico seguro de 33 pt | 0 | 0 |
| Destinos internos fuera del PDF | 0 | 0 |
| Páginas en blanco | 0 | 15 |
| Avisos verticales leves | 4 | 12 |
| Mayor aviso vertical | 2.362 pt | 4.055 pt |

Las páginas en blanco de carta se cotejaron con el inicio en recto del capítulo siguiente. Los avisos verticales se registran y sus páginas se incluyen en las pruebas; no se ocultan ni se califican como errores eliminados. Las fuentes están incrustadas y el expediente incluye las salidas reales de `pdffonts`.

Se revisaron 33 hojas de contacto: 241 páginas de A4 y 261 de carta, con ampliaciones selectivas. Incluyen todas las páginas ilustradas y todos los comienzos y finales de capítulo. El control automático de márgenes y enlaces recorrió todas las páginas. Esta revisión de composición no equivale a una lectura visual línea por línea del texto completo.

## Entrega y límites

El ZIP incluye ambos PDF, los treinta capítulos, las fuentes TikZ y SVG, las copias históricas intactas, las pruebas visuales, los registros y los scripts de compilación y control. `main.tex` abre A4; `main_Carta_Impresion.tex` abre la edición carta a doble cara. No se distribuyen archivos de fuentes tipográficas.

La compilación fue local; no se ejecutó una sesión real en Overleaf. No se revalidaron en línea todos los enlaces bibliográficos externos. El manifiesto externo registra las huellas del ZIP y de los dos PDF; el manifiesto interno permite comprobar el contenido del proyecto.

**Estado: candidata v04 para revisión del autor, sin canonización ni publicación.**
