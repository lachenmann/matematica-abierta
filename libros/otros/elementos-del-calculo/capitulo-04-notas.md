---
title: Capítulo 4 — Notas históricas y control de fuentes
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
source-id: EDC-C04-NOTAS-HISTORICAS
source-sha256: a88924171be4f985e750e90086b0a1d0eba0b2f1b428657956c76d7873e6af2b
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-04.html) · [Ejercicios](capitulo-04-ejercicios.html) · [Soluciones](capitulo-04-soluciones.html) · [Notas históricas](capitulo-04-notas.html)

Estas notas acompañan [el capítulo 4](capitulo-04.html) y documentan sus referencias. La distinción fundamental es triple: (i) **fuentes históricas traducidas o reproducidas que pudieron leerse en línea**; (ii) **historiografía secundaria efectivamente consultada**; (iii) **archivos y fichas sólo localizados**. Una coincidencia matemática entre notación actual y resultado antiguo no acredita que el procedimiento o la demostración moderna se encontrara en un texto histórico. Las pruebas del capítulo son construcciones contemporáneas propias.

## H1. Euclides X.1, Eudoxo y el agotamiento

La proposición 1 del libro X de los *Elementos* explica, en forma de relaciones entre magnitudes, que una disminución reiterada de más de la mitad del resto acaba por dejar una magnitud menor que otra previamente especificada. Este razonamiento se relaciona con el método de agotamiento, utilizado en problemas geométricos de área y volumen. **No** es la fórmula moderna $R_n\to0$ escrita mediante límites: el Lema 4.1 traduce una estructura lógica semejante a aritmética de números reales.

**Texto en traducción localizada:** *Euclid’s Elements*, Book X, Proposition 1, edición digital «Euclid’s Elements» de D. E. Joyce y colaboradores, [proposición X.1](https://www.euclids-elements.org/elements/books/bookX/propositions/propX1/), primer enunciado, demostración y notas «Use of this proposition». También se localizó una traducción atribuida a T. L. Heath en [Perseus, Book X, Proposition 1](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0086%3Abook%3D10); la lectura de esta última página íntegra no pudo completarse en la consulta actual, aunque el pasaje apareció en el índice de búsqueda.

**Historiografía leída:** O'Connor y Robertson, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), MacTutor, líneas/primeros párrafos dedicados a Eudoxo, agotamiento y Arquímedes. Su atribución a Eudoxo hacia 370 a. C. se registra como información de síntesis, no como descubrimiento de un manuscrito suyo cotejado aquí.


## H2. Arquímedes, la cuadratura parabólica y la Proposición 24

El resultado de un segmento parabólico equivalente a **cuatro tercios** de un triángulo de igual base y altura constituye el eje del capítulo. La fuente antigua es *La cuadratura de la parábola*, dirigida a Dositeo; el texto conservado incluye procedimientos mecánicos y una demostración geométrica por agotamiento. Nuestro Teorema 4.2, formulado para el gráfico de una función cuadrática con sumas de triángulos y paralelogramos de error, es una **demostración moderna independiente**, no una traducción ni un facsímil de la Proposición 24.

**Testimonio primario mediado por traducción inglesa, efectivamente leído:** MacTutor, [«Archimedes: Quadrature of the parabola»](https://mathshistory.st-andrews.ac.uk/Extras/Archimedes_parabola/), prefacio reproducido, pasajes iniciales de la carta a Dositeo y mención del descubrimiento mecánico seguido de la demostración geométrica. El texto es una traducción accesible con aclaraciones editoriales entre corchetes; **no** se cotejó con el original griego ni con un facsímil.

**Historiografía secundaria leída:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), párrafos sobre la cuadratura del segmento parabólico, polígonos inscritos y razón geométrica $1/4$.

**Referencia adicional localizada pero no íntegramente leída por indisponibilidad del sitio al abrirlo:** Andrew Leahy, «A Translation of Evangelista Torricelli's Quadratura Parabolae — Archimedes' Quadrature of the Parabola», *MAA Convergence*, [ficha enlazada](https://old.maa.org/press/periodicals/convergence/a-translation-of-evangelista-torricellis-quadratura-parabolae-archimedes-quadrature-of-the-parabola). El resultado indexado del buscador identifica la **Proposición 24**, la formulación $4/3$ y una remisión a Heath, p. 251; la página completa devolvió error de acceso. **No** se atribuye consulta integral ni se cita Heath por página como si hubiéramos examinado ese libro en M05.

**Referencia complementaria identificada, no colacionada:** Thomas L. Heath, *The Works of Archimedes*, reproducción Cambridge Library Collection. Figura como candidato a cotejo filológico si se prepara una edición de imprenta.


## H3. La singularidad del método de agotamiento

El agotamiento no se reduce a «sumar infinitos triángulos» como si existiera de antemano una suma infinita general. En la práctica probatoria antigua, una aproximación finita y un procedimiento para hacer el resto menor que una magnitud dada podían conducir a una doble demostración por reducción al absurdo. Nuestro argumento numérico utiliza límites y la completitud de $\mathbb R$, mientras la historiografía examinada distingue esa reconstrucción de la presentación geométrica original.

**Fuente historiográfica leída:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), sección de Arquímedes y sucesión de triángulos. **Fuente parcial contextual:** ficha MAA Convergence de Leahy citada en H2, cuyo fragmento indexado describe la diferencia entre la fórmula moderna de suma geométrica y el agotamiento sin paso explícito al límite moderno; la imposibilidad de abrir su texto íntegro se mantiene anotada.

La reconstrucción de §4.4 no tiene como misión decidir cómo concebía Arquímedes el infinito ni reconstruir palabra por palabra su demostración. La afirmación matemática y la interpretación histórica reciben controles separados.


## H4. Cavalieri, la geometría de indivisibles y su recepción

Bonaventura Cavalieri publicó la *Geometria indivisibilibus continuorum nova quadam ratione promota* en 1635, aunque su manuscrito había sido redactado antes. El método de indivisibles compara figuras mediante familias de segmentos y planos paralelos. La discusión histórica incluye críticas sobre si una línea puede funcionar como constituyente de una superficie y hasta qué punto el nuevo método aceptaba un infinito actual o potencial. No se debe reinterpretar sin pruebas su procedimiento como teoría de medida, integración de Riemann o de Lebesgue, ni confundirlo automáticamente con la posterior formulación rigurosa del principio de Cavalieri.

**Fuente secundaria leída:** O'Connor y Robertson, [«Bonaventura Francesco Cavalieri»](https://mathshistory.st-andrews.ac.uk/Biographies/Cavalieri/), MacTutor, párrafos de la obra de 1635 y la explicación sobre indivisibles, secciones paralelas, críticas de Paul Guldin y las *Exercitationes geometricae sex* de 1647. La página incluye citas de Howard Eves y de bibliografía especializada; estas citas fueron leídas **en reproducción secundaria**, no en los libros originales.

**Contexto secundario adicional leído:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), párrafos sobre Cavalieri, Roberval y el desarrollo de cuadraturas mediante potencias. El nombre «fórmula de Cavalieri» para integrales de potencias debe tratarse como una etiqueta retrospectiva: el argumento de C04 por el teorema del valor medio no se presenta como obra de Cavalieri.


## H5. Torricelli y la continuidad del problema parabólico

La cuadratura de la parábola fue objeto de nuevas demostraciones en el siglo XVII, especialmente en la tradición de Torricelli. Una ficha accesible por resultados indexados de la *Mathematical Association of America* presenta la traducción de su *Quadratura Parabolae* y la contrasta con procedimientos de Arquímedes y Cavalieri. Esta referencia ayuda a no reducir la historia a un único episodio antiguo seguido inmediatamente por Newton y Leibniz.

**Referencia localizada mediante índice de búsqueda (texto completo no abierto):** Andrew Leahy, «A Translation of Evangelista Torricelli's Quadratura Parabolae — Torricelli's Quadrature of the Parabola (One Version)», [MAA Convergence](https://old.maa.org/press/periodicals/convergence/a-translation-of-evangelista-torricellis-quadratura-parabolae-torricellis-quadrature-of-the-parabola). El resultado indexado describe procedimientos de indivisibles y una comparación con Arquímedes; el sitio devolvió error al solicitar la página completa. No se cita una página ni una proposición particular del tratado de Torricelli como si hubiese sido examinada directamente.


## H6. La diferencia entre sumas finitas y una integral moderna

El estudio de sumas de cuadrados y potencias ilustra un puente conceptual que es legítimo para nuestro lector **actual**. Al escribir $\sum f(\xi_i)\Delta_i$ y considerar una finura $\|P\|\to0$, no atribuimos una definición de Riemann a matemáticos anteriores al siglo XIX. Las reconstrucciones modernas son útiles para explicar por qué pudo surgir el cálculo integral, pero los textos históricos no siempre usan nuestros dominios, funciones, particiones, cuantificadores ni criterios de convergencia.

**Fuentes de contraste leídas:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), párrafos sobre Roberval, Cavalieri y Newton/Leibniz. Las fórmulas de C04 pertenecen al sistema moderno del libro y se prueban desde C00–C03; no se importó una exposición del proyecto independiente *Cálculo para matemáticos* ni de la traducción de Toth.


## Inventario de control para uso editorial

| Identificador | Objeto | Disponibilidad | Lectura efectiva en M05 | Uso de las afirmaciones |
|---|---|---|---|---|
| H-EUC-X1 | Euclides X.1 | Web pública | Proposición y comentario digital leídos | Agotamiento, distinción con límite moderno |
| H-ARC-PREF | Prefacio de Arquímedes a Dositeo | Traducción reproducida en MacTutor | Leído | Descubrimiento mecánico y prueba geométrica, con cautela de traducción |
| H-ARC-QP24 | Proposición 24 / ficha Leahy–MAA | Resultado web indexado | Texto íntegro no disponible | Sólo localización de resultado, no cotejo primario |
| H-ARC-HEATH | Heath, *The Works of Archimedes* | PDF localizado en Drive | No leído | Candidato a colación posterior |
| H-CAV | MacTutor Cavalieri | Web pública | Leído | Publicación 1635, indivisibles y controversias |
| H-TOR | Leahy, traducción de Torricelli | Resultado web indexado | Página íntegra no disponible | Contexto de segunda tradición, no citas directas |
| H-HIST | MacTutor historia del cálculo | Web pública | Leído | Marco comparativo, no fuente primaria para cada atribución |

## Dictamen historiográfico

Las proposiciones cronológicas e históricas del capítulo son deliberadamente limitadas, y sus fuentes se enumeran arriba. No se atribuyen a los autores antiguos razonamientos $\varepsilon$–$\delta$, integrales de Riemann, funciones en notación actual ni series infinitas en el sentido moderno. La historia se mantiene separada de las pruebas publicables y quedan marcadas las necesidades de colación primaria de una eventual edición crítica.
