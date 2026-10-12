---
title: Capítulo 8 — Notas históricas y control de fuentes
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
source-id: EDC-C08-NOTAS-HISTORICAS
source-sha256: 75364a48700e6cc941bcadbe6359912baa6ab23ffcb468fab7ac40040d92ad7c
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-08.html) · [Ejercicios](capitulo-08-ejercicios.html) · [Soluciones](capitulo-08-soluciones.html) · [Notas históricas](capitulo-08-notas.html)

Estas notas acompañan [el capítulo 8](capitulo-08.html) y separan la genealogía de los procedimientos infinitos de la **demostración moderna** de las propiedades de series. En particular, nuestras pruebas mediante límites de sucesiones reales, completitud, radio de convergencia y cotas cuantificadas se han escrito para EDC y no se atribuyen literalmente a autores de épocas anteriores. El material efectivamente leído en web se diferencia de una referencia bibliográfica meramente localizada o de un facsímil no cotejado.

## H1. La armónica y Nicole Oresme

La demostración por agrupaciones sucesivas en bloques crecientes proporciona una manera elemental de apreciar cómo términos que tienden a cero pueden originar sumas parciales no acotadas. La historiografía vincula el conocimiento de la divergencia de la serie armónica con Nicole Oresme en el siglo XIV. Ello no justifica afirmar que su demostración tuviera el formalismo $\varepsilon$–$N$ o que escribiera $\sum1/n$ en notación actual.

**Fuente historiográfica y pedagógica localizada y con texto accesible:** Jeff Babb, «Mathematical Concepts and Proofs from Nicole Oresme: Using the History of Calculus to Teach Mathematics», *Science & Education* **14** (2005), 443–456, DOI [10.1007/s11191-004-7937-y](https://doi.org/10.1007/s11191-004-7937-y). El registro abierto en [ResearchGate](https://www.researchgate.net/publication/260263038_Mathematical_Concepts_and_Proofs_from_Nicole_Oresme_Using_the_History_of_Calculus_to_Teach_Mathematics) incluye título, resumen y un pasaje sobre la divergencia de la armónica, con reconstrucción pedagógica por bloques. La edición primaria de Oresme no fue cotejada.


## H2. Series en el cálculo de Newton y Leibniz

Durante los siglos XVII y XVIII, las expansiones infinitas se utilizaron para obtener cuadraturas, aproximaciones y representaciones de funciones. El tránsito entre expresiones algebraicas finitas y procedimientos infinitos no obedecía aún a una teoría única de convergencia; en particular, sería anacrónico atribuir a Newton el Teorema 8.9 formulado mediante una cota uniforme local de restos.

**Historiografía leída:** J. J. O'Connor y E. F. Robertson, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), *MacTutor History of Mathematics*, secciones que discuten *De analysi* (manuscrito de 1669), las series empleadas por Newton para seno y coseno y la distinción entre fechas de redacción y publicación. La exposición sobre Leibniz y la notación $\int$ contextualiza el carácter operatorio del cálculo; no prueba por sí sola afirmaciones sobre la prioridad de cada serie.

**Reserva:** los manuscritos de Newton y Leibniz y sus ediciones críticas no se han colacionado para este capítulo; no se inventan páginas ni se transcriben fórmulas como testimonios del original.


## H3. La arctangente y la llamada fórmula de Gregory–Leibniz

La identidad $\pi/4=1-1/3+1/5-\cdots$ se suele asociar a la tradición de Gregory y Leibniz. Conviene distinguir el uso histórico de esa representación de la **prueba concreta** de C08: integrar sobre $[0,1]$ una identidad geométrica finita y estimar su resto en $1/(2N+3)$. Que el resultado tenga un nombre histórico no acredita que la técnica con integral de Riemann–Darboux haya sido empleada por sus autores.

**Contexto:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), síntesis general sobre el surgimiento de métodos de series. Para atribuciones exactas de manuscritos, cronologías y primeras apariciones de la expansión de arctangente se necesitaría una investigación especializada adicional; la fuente consultada aquí no basta para resolver por sí sola ese problema de prioridad.


## H4. Cauchy: la convergencia exige condiciones

Una diferencia importante entre manipular una fórmula y demostrar una identidad infinita es precisar **el límite de las sumas parciales** y controlar las colas. Este énfasis tiene una referencia histórica particularmente pertinente en el *Cours d'analyse* de Augustin-Louis Cauchy, publicado en **1821**. La síntesis MacTutor reproduce en traducción su definición de suma convergente mediante $S_n\to S$, la condición necesaria $u_n\to0$ y su formulación de la necesidad de controlar colas de una cantidad arbitraria de términos. También indica que su programa de rigor no eliminó todos los errores en las operaciones con series de funciones.

**Historiografía y extractos traducidos efectivamente leídos:** MacTutor, [«Cauchy's Calculus»](https://mathshistory.st-andrews.ac.uk/Extras/Cauchy_Calculus/), párrafos «Cauchy's definition of convergence and sum of a series» y «Cauchy's errors». No se ha cotejado el francés del *Cours d'analyse* en la edición original. Las citas de MacTutor se utilizan para caracterizar una tradición histórica, **no** para sustituir la prueba de nuestro Teorema 8.1.


## H5. Abel, el problema de las fronteras y la continuidad

El comportamiento de una serie de potencias en los puntos $c\pm R$ no queda decidido por su convergencia interior. Los ejemplos del §8.7 separan convergencia absoluta, condicional y divergencia sobre la frontera; el ejemplo del §8.11 ilustra una prueba de borde **particular** mediante resto integrado, sin adoptar el teorema general de Abel como premisa.

**Fuente de control matemática moderna consultada:** [*Encyclopedia of Mathematics*, «Power series»](https://encyclopediaofmath.org/wiki/Power_series), descripción del radio, convergencia interior y posibles comportamientos sobre la circunferencia de convergencia. La entrada trata funciones complejas y resultados de analiticidad que no se importan como fundamentos de nuestro argumento de una variable real.

**Fuente historiográfica de contexto localizada:** [MacTutor, «Konrad Knopp: Texts»](https://mathshistory.st-andrews.ac.uk/Extras/Knopp_texts/), índice descriptivo de capítulos sobre el desarrollo de la teoría de convergencia y teoremas de Abel; esto **no** equivale a leer una demostración primaria de Abel. La memoria original de Abel de 1826 y su correspondencia se reservan para eventual cotejo en el capítulo C09.


## H6. Convergencia absoluta, reordenaciones y operaciones legítimas

La regla de que una serie de números absolutamente convergente conserva su valor bajo reordenaciones, y de que el producto de Cauchy de dos de esas series suma el producto de sus valores, es una afirmación matemática moderna con hipótesis precisas. El comportamiento de una serie condicionalmente convergente es diferente: la reordenación puede alterar el resultado. Las pruebas de C08 se formularon directamente con colas y sumas finitas, evitando la invocación de integrales de Lebesgue o teoremas generales de series múltiples.

**Control matemático consultado:** *Encyclopedia of Mathematics*, [«Absolutely convergent series»](https://encyclopediaofmath.org/wiki/Absolutely_convergent_series) — resultados de convergencia absoluta, reordenación y producto. [«Conditional convergence»](https://encyclopediaofmath.org/wiki/Conditional_convergence) — distinción con series no absolutamente convergentes. Ambas son fuentes modernas, no evidencia primaria acerca de fechas de descubrimiento.


## H7. La convergencia local y Weierstrass

El uso de una cota que sirva simultáneamente para todos los puntos de un intervalo cerrado estrictamente interior al radio es esencial para la justificación de derivadas e integrales de series de potencias. En la historiografía del análisis, la noción de convergencia uniforme se asocia a las reconstrucciones rigurosas del siglo XIX, incluidas contribuciones de Weierstrass. Nuestro Teorema 8.8 contiene una **estimación local particular**, no desarrolla la teoría general de convergencia uniforme de familias arbitrarias.

**Fuente secundaria localizada:** MacTutor, [«Karl Weierstrass»](https://mathshistory.st-andrews.ac.uk/Biographies/Weierstrass/), semblanza que recoge sus aportes a convergencia uniforme y funciones definidas por productos infinitos. **Fuente matemática leída:** *Encyclopedia of Mathematics*, [«Power series»](https://encyclopediaofmath.org/wiki/Power_series), convergencia local interior y operaciones. Ninguna de estas fuentes autoriza afirmar que Weierstrass utilizara exactamente nuestra demostración de C08.


## Registro consolidado de procedencia

| Fuente | Estado de consulta en EDC-M09 | Utilización permitida |
|---|---|---|
| Jeff Babb, *Science & Education* 14 (2005) | Registro y texto accesible consultados; texto original de Oresme no cotejado | Marco Oresme y armónica, sin atribuir símbolos modernos |
| MacTutor, O'Connor–Robertson, «A history of the calculus» | Página web abierta y consultada | Antecedentes de series y cálculo Newton–Leibniz |
| MacTutor, «Cauchy's Calculus» | Página completa leída con extractos traducidos | Formulación histórica de sumas parciales y colas |
| MacTutor, «Konrad Knopp: Texts» | Descripción de contenidos y capítulos leída | Localización bibliográfica; no fuente primaria de Abel |
| MacTutor, Weierstrass | Síntesis secundaria localizable | Contexto para convergencia uniforme |
| *Encyclopedia of Mathematics*, «Power series» | Entrada abierta y consultada | Contraste moderno de radio y fronteras |
| *Encyclopedia of Mathematics*, «Absolutely convergent series» y «Conditional convergence» | Entradas web consultadas | Contraste matemático de reordenaciones y productos |
| Cauchy 1821; Abel 1826; manuscritos de Newton y Leibniz | Referencias históricas, originales no colacionados | Pendiente para revisión crítica del volumen |

**Dictamen historiográfico:** ningún teorema del capítulo se atribuye a un documento primario no examinado. El uso del nombre de un autor en una identidad o criterio no reemplaza una investigación de su formulación original. Las demostraciones de `EDC-C08` son contemporáneas y están conectadas exclusivamente con los resultados ya disponibles en el libro.
