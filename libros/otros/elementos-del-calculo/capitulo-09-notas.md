---
title: Capítulo 9 — Notas históricas y control de fuentes
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
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C09-NOTAS-HISTORICAS
source-sha256: c29a610e13cb9e406817af000899061148a82d98916fb2ee5daa03c2f39ef629
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-09.html) · [Ejercicios](capitulo-09-ejercicios.html) · [Soluciones](capitulo-09-soluciones.html) · [Notas históricas](capitulo-09-notas.html)

Las afirmaciones históricas de [C09](capitulo-09.html) se separan de las demostraciones matemáticas. Las primeras describen tradiciones documentadas; las segundas son **reconstrucciones originales modernas**, formuladas con intervalos reales, límites, derivadas y el Teorema Fundamental construido en C00–C08. No atribuimos retrospectivamente a un autor de los siglos XVII o XVIII un «resto de Lagrange» con las hipótesis precisas de nuestro Teorema 9.4, ni damos por sentada la coincidencia de una función $C^\infty$ con una serie de potencias.

## H1. El binomio generalizado y Newton

La identidad finita para potencias enteras no debe confundirse con el problema de elevar una expresión a un exponente fraccionario o negativo y obtener una **suma infinita**. La bibliografía matemática contemporánea vincula el desarrollo binomial generalizado de Newton con los años **1664–1665**, mientras otras reconstrucciones sitúan la circulación documental de sus métodos en comunicaciones y manuscritos posteriores. Una fecha atribuida a un descubrimiento no es la fecha de primera publicación del mismo resultado.

**Fuente matemática efectivamente consultada:** [*Encyclopedia of Mathematics*, «Binomial series»](https://encyclopediaofmath.org/wiki/Binomial_series), definición de $\binom\alpha n$, casos de terminación, radio unitario cuando el exponente no es entero no negativo y nota histórica acerca de Newton y Abel. La fuente expone además casos de frontera que **C09 no utiliza sin prueba**, y trata variables complejas fuera de la jurisdicción del libro.

**Testimonio primario en edición digital localizado y parcialmente leído:** [The Newton Project, «History of the Method of Fluxions»](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00356), transcripción diplomática del manuscrito Cambridge University Library MS Add. 3968, ff. 146r–171r. La página permite constatar que Newton revisó retrospectivamente la cronología de su método y citó sus cartas de 1676. **Reserva:** no se ha colacionado el manuscrito completo ni demostrado que este pasaje específico corresponda al primer enunciado del binomio. No se emplea como prueba de una prioridad exclusiva.


## H2. Brook Taylor y la obra impresa de 1715

**Brook Taylor** publicó *Methodus incrementorum directa et inversa* en **1715**. La obra pertenece a un ambiente matemático donde se estudiaban series, diferencias, procedimientos de resolución de ecuaciones y problemas mecánicos. La historiografía secundaria consultada señala versiones de una regla de expansión vinculadas con la correspondencia de Taylor con John Machin en **1712**, e identifica distintas motivaciones de pasajes del libro de 1715.

**Fuente secundaria íntegramente abierta:** J. J. O'Connor y E. F. Robertson, [«Brook Taylor»](https://mathshistory.st-andrews.ac.uk/Biographies/Taylor/), *MacTutor History of Mathematics*, especialmente los párrafos sobre *Methodus*, la carta de 26 de julio de 1712, la Proposición 11 y el corolario de la Proposición 7. La misma biografía advierte expresamente que variantes anteriores se asocian a **James Gregory, Newton, Leibniz, Johann Bernoulli y Abraham de Moivre**. No sería correcto inferir «primer descubridor absoluto» a partir del uso posterior del epónimo.

**Verificación bibliográfica de la edición:** [Folger Shakespeare Library, registro de *Methodus incrementorum directa & inversa*](https://catalog.folger.edu/record/749251), con impresor, Londres, 1715 y colación [6], 118, [2] páginas. [Google Books, ficha de la edición de 1715](https://books.google.com/books/about/Methodus_incrementorum_directa_inversa.html?id=wjYO0gEACAAJ) consigna también el año y una extensión de 118 páginas. **Ninguna de estas fichas equivale a lectura completa del texto latino**.


## H3. La diferencia entre una regla antigua y el resto moderno

El nombre «Taylor» designa en la enseñanza contemporánea tanto un polinomio como una serie infinita y varias fórmulas para la diferencia restante. Son objetos matemáticos que deben distinguirse incluso cuando se estudian conjuntamente. La fórmula de Lagrange que demostramos en C09 utiliza hipótesis explícitas de continuidad de derivadas hasta orden $n$ en un compacto y existencia de la derivada siguiente en el interior; su prueba por Rolle pertenece a una formulación moderna.

**Referencia matemática consultada:** [*Encyclopedia of Mathematics*, «Taylor formula»](https://encyclopediaofmath.org/wiki/Taylor_formula). La entrada distingue restos de **Peano, Lagrange, Cauchy** e **integral**; fue consultado su contenido de fórmulas, aunque una recuperación adicional del enlace falló. Por ello se invoca sólo como **control matemático de formas**, no como documento primario acerca de quién publicó primero cada una.

**Referencia secundaria verificada de terminología:** [*Encyclopedia of Mathematics*, «Taylor series»](https://encyclopediaofmath.org/wiki/Taylor_series), definición por derivadas y discusión de representabilidad; ficha y contenido accesibles en los resultados consultados. **Reserva:** las fórmulas matemáticas en estas fuentes no permiten inferir que Taylor demostrara exactamente el Teorema 9.4 que usamos.


## H4. Gregory, Bernoulli y la dificultad de una historia por «primeros»

La atribución de un desarrollo general a un solo autor oscurece que **series particulares, leyes de formación de coeficientes y fórmulas derivativas generales** fueron problemas matemáticos relacionados pero distintos. La biografía de Taylor en MacTutor menciona antecedentes de Gregory y Johann Bernoulli; la entrada de la *Encyclopedia of Mathematics* sobre Taylor indica asimismo una expansión relacionada publicada por Johann I Bernoulli en **1694**. Se trata de informaciones provenientes de historiografía y referencias matemáticas modernas, no de una comparación personal de las ediciones latinas de todos los textos.

**Fuente historiográfica efectivamente leída:** [MacTutor, «Brook Taylor»](https://mathshistory.st-andrews.ac.uk/Biographies/Taylor/), apartados sobre Gregory, Newton, Bernoulli y la denominación tardía de la serie. El mismo artículo enumera como estudio especializado: A. Malet, «James Gregorie on tangents and the 'Taylor' rule for series expansions», *Archive for History of Exact Sciences* **46** (1993), 97–137. Esta referencia es **bibliografía localizada**, no un artículo leído integralmente en EDC-M10.


## H5. Maclaurin y Lagrange: nombres, programas y fechas

El desarrollo centrado en cero se denomina «de Maclaurin» en la terminología actual, pero es un **caso particular** de la construcción de Taylor, no un teorema de fundamento diferente. La obra de **Colin Maclaurin**, *A Treatise of Fluxions*, se publicó en **1742**. La publicación de **Joseph-Louis Lagrange**, *Théorie des fonctions analytiques*, data de **1797**. La historiografía acerca del programa de Lagrange muestra que su ambición de fundamentar el cálculo a través de expansiones no se identifica sin reservas con nuestra teoría actual de funciones reales y de restos.

**Fuentes consultadas:** [*Encyclopedia of Mathematics*, «MacLaurin series»](https://encyclopediaofmath.org/wiki/MacLaurin_series), definición moderna y referencia a los dos volúmenes de 1742; [MacTutor, «Colin Maclaurin's A Treatise of Fluxions — Introduction»](https://mathshistory.st-andrews.ac.uk/Extras/Maclaurin_introduction/), texto modernizado según puntuación de una edición posterior; [Craig G. Fraser, «Joseph Louis Lagrange's algebraic vision of the calculus»](https://www.sciencedirect.com/science/article/pii/0315086087900024), *Historia Mathematica* **14** (1987), 38–53, resumen bibliográfico abierto; y [*Landmark Writings in Western Mathematics*, capítulo sobre la primera edición de 1797](https://www.sciencedirect.com/science/chapter/edited-volume/abs/pii/B9780444508713501005), ficha y resumen consultados.

**Reserva:** no se ha cotejado el libro de Maclaurin de 1742 ni el francés de la edición de Lagrange de 1797; la lectura del resumen de Fraser **no** equivale a verificar todo su argumento historiográfico. No se asigna automáticamente a Lagrange nuestra demostración con $\Phi(t)$ y Rolle ni a Maclaurin la primera idea de expansión en cero.


## H6. El siglo XIX y el problema de las series representativas

La transformación del cálculo en análisis riguroso exigió separar la manipulación de expresiones infinitas de su validez como límites. EDC-C08 introdujo precisamente sumas parciales y estimaciones de colas; EDC-C09 distingue además un resto **para orden fijo** de la exigencia de que ese resto tienda a cero cuando el orden crece. Un programa histórico que definiera toda función mediante una expansión infinita debe evaluarse bajo criterios que no estaban formulados de manera idéntica en todos los períodos.

**Fuente secundaria accesible:** J. J. O'Connor y E. F. Robertson, [«Cauchy's Calculus»](https://mathshistory.st-andrews.ac.uk/Extras/Cauchy_Calculus/), lectura ya controlada en EDC-C08 para el contexto de convergencia y errores históricos; no se afirma una nueva colación del francés original aquí. **Fuente historiográfica adicional localizada:** [Craig G. Fraser, «The Development of Lagrange's Ideas on the Calculus: 1754–1797»](https://www.cambridge.org/core/books/abs/historian-looks-back/development-of-lagranges-ideas-on-the-calculus-17541797/6CF9485AAC1CF906C8A1E8AD8A68C5F9), ficha/resumen consultados, con reserva de acceso al capítulo completo.

El contraejemplo matemático $e^{-1/x^2}$ prolongado por cero **no es una cita histórica de Cauchy ni una reconstrucción de un texto de Taylor**: se incluye como prueba moderna autónoma. El control moderno de esta distinción aparece, por ejemplo, en material docente de Stony Brook, [«Foundations of Numerical Methods — Taylor Series and Taylor Polynomials»](https://www.ams.stonybrook.edu/~jiao/teaching/ams527/lectures/04_TaylorSeries.pdf), **localizado mediante índice web, no inspeccionado por páginas**; por tanto no se presenta como facsímil analizado ni se reproducen sus ilustraciones.


## H7. Newton–Raphson: una misma etiqueta para tradiciones distintas

El §9.11 aprovecha una **fórmula moderna de error cuadrático** deducida del resto de Taylor de orden uno. El nombre «método de Newton» no acredita que Newton usara en sus manuscritos la demostración precisa con $C^2$, $|f'|\ge m$ y $|f''|\le M$. La historiografía atribuye a **Joseph Raphson** una publicación de **1690** y distingue los escritos de Newton sobre resolución de ecuaciones, redactados y publicados en momentos diferentes. También advierte que el formato de los algoritmos antiguos no siempre coincide con la recurrencia moderna $x_{k+1}=x_k-f(x_k)/f'(x_k)$.

**Fuente secundaria abierta por resultados de consulta:** [MacTutor, «Joseph Raphson»](https://mathshistory.st-andrews.ac.uk/Biographies/Raphson/), relato sobre *Analysis aequationum universalis* (1690), su recepción en la Royal Society y la cronología de Newton. [MacTutor, «Raphson books»](https://mathshistory.st-andrews.ac.uk/Extras/Raphson_books/), ficha con reproducciones editadas de reseñas inglesas de época. Los textos latinos originales no se han colacionado para C09.


## Registro historiográfico consolidado

| Tema / fuente | Estado efectivo | Uso y reserva |
|---|---|---|
| *Encyclopedia of Mathematics*, «Binomial series», «Taylor formula», «Taylor series», «MacLaurin series» | Fórmulas, definiciones y metadatos consultados | Control moderno, no prioridad documental primaria |
| MacTutor, «Brook Taylor» | Página íntegra abierta y leída | Fecha editorial 1715, antecedentes y cautela sobre epónimos |
| Folger Library / Google Books, *Methodus* | Fichas catalográficas examinadas | Comprobación bibliográfica; sin colación latina |
| The Newton Project, NATP00356 | Transcripción diplomática parcialmente leída | Testimonio sobre historia de fluxiones, sin adjudicar prioridad binomial |
| MacTutor, Maclaurin (Introducción) | Texto editorial normalizado localizado | Contexto; no edición original cotejada |
| Fraser (1987), Cambridge, ScienceDirect | Resúmenes y fichas consultados | Programa histórico de Lagrange, sin lectura íntegra del capítulo |
| MacTutor, Raphson y reseñas de 1690 | Resultados y extractos consultados | Cronología del método numérico, sin equivalencia literal con teorema actual |
| Originales de Newton, Taylor, Maclaurin, Lagrange y Raphson | No colacionados integralmente | Pendientes de eventual auditoría filológica con facsímiles |

**Dictamen:** se pueden atribuir con cautela los hitos **Newton–binomio**, **Taylor–1715**, **Maclaurin–1742**, **Lagrange–1797** y **Raphson–1690** a las fuentes secundarias o fichas consultadas. No se debe confundir esa atribución con autoría de nuestras pruebas modernas, con una edición crítica terminada ni con certificación de primacía histórica. Las fórmulas, contraejemplos y estimaciones del texto de C09 pertenecen al manuscrito independiente de *Elementos del cálculo*.


## Complemento bibliográfico — EDC-M13-A03 (11 de octubre de 2026)

**Dos testimonios editoriales, una obra.** La ficha de la [Folger Shakespeare Library](https://catalog.folger.edu/record/749251) registra *Methodus incrementorum directa & inversa* de Brook Taylor, impresa en Londres en **1715**, con paginación `[6],118,[2]` y hoja final de correcciones. La [National Library of Australia](https://catalogue.nla.gov.au/catalog/3275233) registra una emisión de **1717** y la describe con cautela como **probable reedición de los pliegos de 1715**, con las primeras hojas preliminares recompuestas. Esta distinción impide identificar indiscriminadamente cualquier ejemplar de 1717 con una primera edición nueva o tomar la fecha de un catálogo como certificación de una fórmula concreta.

**Estado de evidencia:** `1715_AND_1717_LIBRARY_CATALOGS_READ / EXPLICIT_PROBABLE_REISSUE / LATIN_TEXT_NOT_COLLATED`. La denominación contemporánea «serie de Taylor» conserva el carácter de epónimo histórico, **no** una tesis de prioridad exclusiva ni una transcripción de la notación de nuestro Teorema 9.
