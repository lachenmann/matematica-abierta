---
title: Capítulo 5 — Historia y control de fuentes
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
license: GFDL-1.3-or-later
areas:
- calculo
- analisis
- fundamentos
level: intermedio
topics:
- calculo-de-una-variable
- historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
  - role: idea
    note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra
      independiente.'
source-id: EDC-C05-NOTAS-HISTORICAS
source-sha256: 6ba7c163ea97a807b6fd6ac706bbb88bb7c45066a00e9640db195d3c9d331c8d
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-05.html) · [Ejercicios](capitulo-05-ejercicios.html) · [Soluciones](capitulo-05-soluciones.html) · [Notas históricas](capitulo-05-notas.html)

Este expediente acompaña [el capítulo 5](capitulo-05.html), pero no sustituye ni justifica sus teoremas matemáticos. Se distinguen (i) testimonio primario efectivamente consultado; (ii) catálogos y registros de ediciones que **localizan** un documento pero no constituyen lectura de su contenido; (iii) historiografía secundaria realmente consultada; y (iv) pruebas modernas redactadas en EDC. Los símbolos $\varepsilon$, supremos sobre particiones, sumas de Darboux y el formalismo de funciones acotadas pertenecen a nuestra reconstrucción, no se atribuyen indiscriminadamente a todos los autores nombrados.

## H1. De las cuadraturas al problema de la integración de funciones

El capítulo 4 partió de áreas geométricas, triángulos y aproximaciones por agotamiento; el capítulo 5 da un nuevo paso al admitir **funciones acotadas arbitrarias** como objetos de examen, incluidas funciones con discontinuidades. Este paso no corresponde a una sola invención súbita de todas las propiedades modernas de la integral.

**Historiografía secundaria efectivamente leída:** *Grande Encyclopédie Larousse*, voz «analyse», subsección «Intégrales définies» (<https://www.larousse.fr/archives/grande-encyclopedie/page/683>, líneas textuales bajo ese encabezado). Distingue las aproximaciones por sumas asociadas a Cauchy desde 1823 y las ampliaciones atribuidas a Riemann y Darboux. La periodización constituye una síntesis editorial de la enciclopedia, no una colación por nosotros de cada obra original.


## H2. Augustin-Louis Cauchy y el papel de las sumas finitas (1823)

En el *Résumé des leçons données à l'École royale polytechnique sur le calcul infinitésimal* (1823), Cauchy dedicó una parte de sus lecciones a las integrales definidas. La fuente historiográfica de H1 describe su uso de sumas ponderadas por longitudes de subintervalo para funciones continuas; no debe identificarse esta formulación sin examen con nuestra definición por supremos/ínfimos de Darboux para toda función acotada.

**Referencia primaria localizada con identificación editorial, pero no colacionada frase por frase:** Augustin-Louis Cauchy, *Résumé des leçons données à l'École royale polytechnique sur le calcul infinitésimal*, París, Imprimerie royale, 1823. Ficha de edición digital en [Google Books](https://books.google.com/books/about/R%C3%A9sum%C3%A9_des_le%C3%A7ons_donn%C3%A9es_%C3%A0_l_Ecole.html?id=hABDXdTdEvoC) y [tabla de contenido en Wikisource](https://fr.wikisource.org/wiki/R%C3%A9sum%C3%A9_des_le%C3%A7ons_donn%C3%A9es_%C3%A0_l%E2%80%99%C3%A9cole_polytechnique_sur_le_calcul_infinit%C3%A9simal), donde se identifican las lecciones XXI–XXIII dedicadas a integrales definidas y su descomposición. Estos índices permiten localizar la materia, pero no acreditan que para esta edición se haya leído el desarrollo original completo.


## H3. Bernhard Riemann y el problema de las funciones discontinuas

El trabajo de habilitación de Riemann sobre la representación de funciones mediante series trigonométricas, fechado en 1854, se asocia en la historiografía con una formulación más general de la integral y una discusión de las condiciones de integrabilidad. Debemos distinguir **fecha de elaboración** y **fecha de circulación impresa**: la pieza fue publicada después de la muerte de Riemann y hay catálogos que sitúan el volumen editorial en 1867 o 1868. En un libro histórico no conviene escribir simplemente «Riemann publicó en 1854 su definición».

**Catálogos consultados:**

- Trinity College Dublin, [«Ueber die Darstellbarkeit einer Function durch eine trigonometrische Reihe»](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Trig/), ficha que identifica la *Habilitationsschrift* y señala publicación por Richard Dedekind, después de la muerte de Riemann, en las *Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen*, vol. 13 (ficha: 1867).
- Catálogo archivístico Kalliope, [manuscrito «Cod. Ms. B. Riemann 8»](https://kalliope.staatsbibliothek-berlin.de/de/ead?ead.id=DE-611-HS-3204968), identificación del original manuscrito de 1854 y remisión a las obras completas, segunda edición, Leipzig 1892, pp. 227–271. **Este localizador es bibliográfico; no indica que hayamos leído esas páginas.**
- Xavier University, [ficha de la traducción inglesa](https://www.exhibit.xavier.edu/oresme_2014Feb/2/), con traducción publicada en *Collected Papers* (2004), cap. XII, pp. 219–256; el acceso al documento derivó a otra página, por lo que no se afirma lectura íntegra.
- *MAA Reviews*, [reseña de *Bernhard Riemann, 1826–1866*](https://old.maa.org/node/107984), pasaje sobre la habilitación de 1854 y publicación póstuma.


## H4. Gaston Darboux, 1875: sumas superiores e inferiores

La conexión histórica más directa con la estructura del capítulo es el trabajo de **Gaston Darboux**, *Mémoire sur les fonctions discontinues*, publicado en 1875. La presentación por sumas inferiores y superiores y su convergencia común ofrece el criterio que hoy llamamos de Riemann–Darboux. El nombre doble reconoce una genealogía, no la afirmación de que Riemann y Darboux redactaron la misma prueba en el mismo lenguaje.

**Registro bibliográfico directamente verificado:** Darboux, Gaston, «Mémoire sur les fonctions discontinues», *Annales scientifiques de l'École Normale Supérieure*, segunda serie, tomo 4 (1875), pp. 57–112, DOI [10.24033/asens.122](https://doi.org/10.24033/asens.122). La ficha de [Numdam](https://archive.numdam.org/item/ASENS_1875_2_4__57_0/) y [EuDML](https://eudml.org/doc/80798) permite verificar autor, fecha, revista y paginación. El intento de abrir la ficha Numdam íntegra produjo un tiempo de espera agotado; se **localizó** el artículo, sin declarar que cada línea del original fue colacionada.

**Evidencia secundaria:** MacTutor, [«Gaston Darboux»](https://mathshistory.st-andrews.ac.uk/Biographies/Darboux/), resultado de índice consultado que atribuye a su trabajo de 1875 la presentación mediante sumas superior e inferior. **Fuente retrospectiva efectivamente leída:** William Henry Young, [«Twentieth Century Pure Mathematical Research»](https://mathshistory.st-andrews.ac.uk/Extras/Young_research/), discurso de 1924, sección 12: Young caracteriza las aproximaciones superior e inferior de Darboux como una clarificación del trabajo de Riemann. Este testimonio secundario, procedente de otro matemático y momento, no sustituye la lectura del texto francés de 1875.


## H5. Por qué la prueba matemática actual no es un calco de la historia

La versión desarrollada en C05 introduce explícitamente: (a) supremos e ínfimos de las funciones acotadas en subintervalos cerrados; (b) supremo global de sumas inferiores e ínfimo de superiores; (c) refinamiento común y criterio de error; (d) un lema cuantitativo que compara **cualquier** partición suficientemente fina con una partición fija; (e) equivalencia entre la forma de Darboux y la formulación por sumas etiquetadas. La elección de ese recorrido obedece a necesidades lógicas y didácticas modernas.

Ni la progresión de sumas de Cauchy ni la obra de Riemann ni el memorando de Darboux deben tratarse como si hubiesen sido escritos con nuestras definiciones de formalismo de libro de texto. Tampoco debe presentarse esta integral como la más general posible. Ejemplos de funciones fuera de su dominio de integrabilidad, junto con desarrollos posteriores de integración, llevaron a otras teorías.

**Fuentes de contraste realmente consultadas:** *Larousse*, «analyse», «Intégrales définies», y W. H. Young (1924), sección 12. **No se ha realizado colación literal de facsímiles de Cauchy, Riemann o Darboux** para esta edición.

## H6. Lecturas disponibles y por verificar

Entre las referencias complementarias se encuentran Spivak, Apostol, Courant–John, Bressoud y Gabor Toth. Su mención bibliográfica no equivale a un cotejo de esas obras; sólo se proporcionan localizadores específicos cuando han sido comprobados.

**Prioridades de una futura colación historiográfica:** Cauchy 1823, lecciones XXI–XXIII; Riemann 1854, apartado original sobre integral; Darboux 1875, texto publicado pp. 57–112, especialmente su formulación y pruebas del límite de sumas. La preparación matemática de C06 no depende de que esas tareas filológicas estén cerradas, porque las pruebas de C05 son autosuficientes.

## Registro y dictamen

| Fuente | Tipo | Comprobación de este tramo | Límite declarado |
|---|---|---|---|
| Larousse, «analyse», «Intégrales définies» | Historia secundaria | Texto web leído | No fuente primaria |
| Cauchy 1823, *Résumé des leçons…* | Original histórico | Ficha y tabla de materias identificadas | No cotejo textual |
| Riemann 1854, habilitación | Original histórico | Catálogos y manuscrito identificados | No lectura completa |
| Darboux, *Mémoire*, 1875 | Original histórico | Datos de Numdam/EuDML confirmados | No colación francesa |
| W. H. Young, discurso de 1924, §12 | Testimonio retrospectivo | Texto accesible leído | Visión posterior, no prueba de fecha original |
| MacTutor, biografía Darboux | Historiografía secundaria | Resultado indexado | Página íntegra no recuperada |
| Toth / CPM | Precedentes de proyecto | Frontera fijada en EDC-M00 | No traslado de textos ni ejercicios |

**Dictamen:** los hechos históricos de C05 se formulan dentro del nivel de lectura efectivamente disponible; los resultados matemáticos son construcciones originales y están sujetos a QA propio. No se equiparan intuiciones de cuadratura antigua con una definición de Riemann desarrollada en el siglo XIX.


## Complemento de control bibliográfico — EDC-M13-A03 (11 de octubre de 2026)

**Cauchy 1823: edición original distinguida de 1821.** La [ETH-Bibliothek, e-rara](https://www.e-rara.ch/zut/content/titleinfo/8350182) identifica *Résumé des leçons données à l’École Royale Polytechnique sur le calcul infinitésimal*, tomo I, París, Imprimerie Royale / Debure frères, **1823**, signatura Rar 10369 y DOI `10.3931/e-rara-25962`. Es un testimonio catalogado distinto del *Cours d’analyse* de **1821**; no se han colacionado las lecciones completas ni sus definiciones, y no se afirma que el autor haya utilizado nuestra definición de integral por Darboux. **Estado:** `ARCHIVAL_CATALOG_VERIFIED / FRENCH_CONTENT_NOT_COLLATED`.

**Riemann 1854 y edición de 1867.** El [catálogo de manuscritos Kalliope](https://kalliope.staatsbibliothek-berlin.de/de/ead?ead.id=DE-611-HS-3204968) identifica la *Habilitationsschrift* de **1854** en el legado de Göttingen (`Cod. Ms. B. Riemann 8`); el [catálogo de ETH-Bibliothek](https://www.e-rara.ch/zut/content/titleinfo/13665454) identifica la edición impresa de **1867** (*Ueber die Darstellbarkeit einer Function durch eine trigonometrische Reihe*, 47 pp.). El [índice del Göttinger Digitalisierungszentrum](https://gdz.sub.uni-goettingen.de/id/PPN309770033) señala expresamente el §4 sobre la definición de una integral definida. Manuscrito, edición y argumento moderno de C05 son tres niveles distintos. **Estado:** `ARCHIVAL_AND_PRINTED_EDITION_METADATA_READ / §4_CATALOGUED_NOT_TEXTUALLY_COLLATED`.

**Darboux 1875.** El registro de [Numdam](https://www.numdam.org/item/ASENS_1875_2_4__57_0/) confirma *Mémoire sur les fonctions discontinues*, *Annales scientifiques de l’École Normale Supérieure*, segunda serie, tomo 4 (**1875**), 57–112, DOI `10.24033/asens.122`. Verificar esos metadatos no equivale a demostrar qué formulación empleó Darboux en cada página ni a haber colacionado íntegramente el artículo. **Estado:** `PRIMARY_JOURNAL_METADATA_VERIFIED / FULL_ARTICLE_UNCOLLATED`.

**Control de método:** esta actualización aporta trazabilidad documental puntual; **no** modifica las pruebas de Riemann–Darboux que hemos reconstruido matemáticamente en C05.
