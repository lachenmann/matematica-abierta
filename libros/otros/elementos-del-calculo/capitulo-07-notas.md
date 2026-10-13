---
title: Capítulo 7 — Notas históricas y control de fuentes
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
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
source-id: EDC-C07-NOTAS-HISTORICAS
source-sha256: 96dab74d0f7f676af1ea5584e6362bdec120d5d307cad5bf4b6661767185cc18
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-07.html) · [Ejercicios](capitulo-07-ejercicios.html) · [Soluciones](capitulo-07-soluciones.html) · [Notas históricas](capitulo-07-notas.html)

Estas notas acompañan [el capítulo 7](capitulo-07.html) y distinguen los antecedentes históricos de los **teoremas formulados hoy**. La técnica moderna de sustitución se justifica en EDC desde la regla de la cadena y el Teorema Fundamental; la integración por partes, desde la regla del producto; las fracciones parciales, desde identidades de polinomios. Ninguna prueba moderna del capítulo se presenta como transcripción de un texto de los siglos XVII–XIX. La exposición no ha importado pasajes del libro de Gabor Toth ni del proyecto independiente *Cálculo para matemáticos*.

## H1. La búsqueda histórica de cuadraturas y primitivas

El problema de encontrar áreas bajo curvas, volúmenes y otros valores acumulados es anterior a una definición general de integral. Los argumentos de agotamiento de la Antigüedad, los métodos de indivisibles y las cuadraturas de potencias de los siglos XVI–XVII pertenecen a tradiciones que no comparten todavía el aparato de Riemann–Darboux. Una descripción historiográfica moderna reúne estas contribuciones, pero hay que distinguir sus técnicas originales de una traducción retrospectiva a la notación $\int_a^b f(x)dx$.

**Fuente secundaria efectivamente leída:** J. J. O'Connor y E. F. Robertson, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), MacTutor History of Mathematics, párrafos iniciales sobre Eudoxo y Arquímedes y apartados posteriores sobre Cavalieri, Roberval y Fermat. Se consultó la página íntegra en este macrotramo. La ficha describe la continuidad temática entre cuadraturas y reglas de cálculo, no una equivalencia literal de demostraciones.

**Estado:** `SECONDARY_WEB_READ / ANCIENT_AND_EARLY_MODERN_PRIMARIES_NOT_COLLATED`.

## H2. Newton, Leibniz y el carácter operatorio del cálculo

MacTutor contrasta el enfoque newtoniano de fluentes y fluxiones con el tratamiento leibniziano de diferencias y sumaciones. La notación $\int$ y el uso de $dx$, vinculados con los trabajos de Leibniz, ayudaron a organizar procedimientos de cálculo. Pero presentar el símbolo $du$ como si constituyera ya una magnitud independiente con la que se pueden cancelar factores sin demostrar nada sería confundir la utilidad de una notación histórica con un argumento matemático.

**Fuente secundaria leída:** O'Connor–Robertson, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), sección de Newton y Leibniz, especialmente los párrafos sobre la diferencia conceptual entre fluxiones y sumas y sobre la notación de Leibniz hacia 1675. El texto también indica que la denominación *calculus integralis* fue propuesta en el entorno de Jakob Bernoulli hacia 1690; esto se consigna sólo como dato de la síntesis historiográfica, no como verificación de un manuscrito del siglo XVII.

**Reserva editorial:** ni el Teorema 7.1 formulado para $f$ continua y $\phi\in C^1$, ni la integral de Darboux usada en su prueba, se atribuyen a Newton o Leibniz. Un estudio de primeras apariciones de fórmulas de sustitución o partes exigiría reconstruir la cronología a partir de ediciones primarias, no de semejanzas simbólicas.

**Estado:** `SECONDARY_WEB_READ / PRIMARY_NOT_COLLATED`.

## H3. Sustitución y el papel de la orientación

El procedimiento de sustituir variables está asociado en la enseñanza actual a la «regla de la cadena en sentido inverso». En nuestro Teorema 7.1, la sustitución integra la expresión $f(\phi(t))\phi'(t)$ y conserva los extremos orientados $\phi(\alpha)$ y $\phi(\beta)$. No se exige monotonía global de $\phi$. Esta es una afirmación contemporánea dentro de la teoría de una variable, no una transcripción del razonamiento con infinitésimos de un autor histórico.

**Fuente matemática moderna consultada:** [*Encyclopedia of Mathematics*, «Integration by substitution»](https://encyclopediaofmath.org/wiki/Integration_by_substitution), encabezado «Integration by substitution», fórmula de cambio de variable con integrando continuo y transformación continuamente derivable y párrafo sobre primitivas por composición. La versión consultada presenta condiciones suficientes e indica que pueden debilitarse. Nuestro enunciado y demostración son propios y especifican un intervalo abierto $J$ que contiene la imagen compacta para garantizar existencia global de una primitiva.

**Estado:** `MODERN_MATHEMATICAL_ENTRY_READ / MODERN_EDC_PROOF_INDEPENDENT`.

## H4. Integración por partes y el producto derivado

La identidad de integración por partes conserva una relación algebraica exacta con la regla del producto. El lector puede comprobar que, una vez construida una integral y probado el Teorema Fundamental, aplicar el teorema a $(uv)'=u'v+uv'$ produce directamente la fórmula sin necesidad de un nuevo concepto de infinitésimo. La versión del capítulo adopta la condición sencilla $u,v\in C^1([a,b])$; las posibles extensiones a funciones con menor regularidad no forman parte del núcleo de EDC.

**Fuente matemática moderna leída:** [*Encyclopedia of Mathematics*, «Integration by parts»](https://encyclopediaofmath.org/wiki/Integration_by_parts), definición inicial, fórmula de integración definida y explicación derivada de la regla de Leibniz (producto). La entrada menciona extensiones para Lebesgue que **no** se utilizan en C07.

**Estado:** `MODERN_MATHEMATICAL_ENTRY_READ / NO_HISTORICAL_FIRST_INVENTOR_ASSIGNED`.

## H5. Las fracciones parciales: algoritmo algebraico, no teorema de integración

Antes de que se elija una primitiva de una función racional, es necesario reconocer un cociente de polinomios y descomponerlo algebraicamente. El Teorema 7.3 demuestra una descomposición para **raíces reales simples**, por evaluación en esas raíces y comparación de grados; casos de factores repetidos y cuadráticos se justifican por identidades concretas. No se atribuye esta prueba a ningún matemático antiguo por el hecho de que haya aparecido con frecuencia en tablas históricas de integración.

Las técnicas de racionalización y factorización poseen genealogías diferentes de la construcción rigurosa de la integral. El capítulo distingue cuidadosamente la justificación *algebraica* de una identidad de fracciones de la justificación *analítica* para integrar cada término sobre un intervalo que evite los polos. La denominación moderna «fracciones parciales» es una herramienta expositiva, no una afirmación filológica sobre un tratado específico.

**Fuente contextual moderna localizada:** [*Encyclopedia of Mathematics*, «Integral calculus»](https://encyclopediaofmath.org/wiki/Integral_calculus), apartados que enumeran sustitución y partes entre las técnicas de cálculo. Las fracciones parciales son demostradas en EDC de manera independiente. Los libros de cálculo de Apostol, Spivak y Courant–John fueron identificados en el inventario de Drive de EDC-M00; **no se afirma aquí una lectura nueva de sus páginas**.

**Estado:** `MODERN_MATH_CONTEXT / PRIMARY_HISTORICAL_ATTRIBUTION_NOT_ATTEMPTED`.

## H6. La distinción entre existencia de primitivas y representación elemental

Si una función es continua en un intervalo cerrado, la primera parte del Teorema Fundamental asegura una primitiva expresable como función de acumulación. Ello no implica que el lector haya recibido una receta finita para reescribir esa función mediante una lista previa de funciones especiales. En C07 se presenta $H(x)=\int_0^xe^{-t^2}dt$ como **ejemplo constructivo de primitiva definida por acumulación**, sin intentar demostrar el teorema más avanzado de no elementalidad de una antiderivada de la gaussiana.

**Fuente matemática moderna leída:** [*Encyclopedia of Mathematics*, «Integral»](https://encyclopediaofmath.org/wiki/Integral), distinción introductoria entre problemas de recuperación de funciones desde tasas y cálculo de acumulaciones, más el pasaje de la fórmula Newton–Leibniz para integrandos continuos. La entrada presenta otros tipos de integrales que no forman parte del capítulo.

**Estado:** `MODERN_REFERENCE_READ / ADVANCED_NON_ELEMENTARITY_RESULT_NOT_CLAIMED`.

## Registro bibliográfico y límites efectivos

| Fuente | Disponibilidad | Lectura en M08 | Uso declarado |
|---|---|---|---|
| MacTutor, O'Connor–Robertson, *A history of the calculus* | Web pública | Abierta y leída | Contexto histórico de cuadraturas, Newton, Leibniz y notación |
| *Encyclopedia of Mathematics*, «Integration by substitution» | Web pública | Ficha y fórmula consultadas | Contraste de condiciones suficientes de sustitución |
| *Encyclopedia of Mathematics*, «Integration by parts» | Web pública | Ficha y fórmula consultadas | Regla del producto y condiciones de partes |
| *Encyclopedia of Mathematics*, «Integral» | Web pública | Entrada consultada | Existencia, primitivas y definiciones históricas |
| Apostol I, Spivak, Courant–John I | PDFs localizados en Drive desde M00 | No releídos íntegramente en M08 | Referencias bibliográficas para una revisión posterior |
| Manuscritos originales de Newton, Leibniz y Bernoulli | No colacionados | No | Prohibido atribuir formulaciones literales o páginas no vistas |

**Dictamen historiográfico:** las referencias sostienen un marco general y matemático pertinente, no una historia exhaustiva de la «primera invención» de cada técnica. Cualquier edición histórica más extensa debe cotejar testimonios primarios, publicaciones y localizadores precisos antes de presentar dataciones o atribuciones prioritarias.


## Complemento documental — revisión literaria R08 (13 de octubre de 2026)

El recuadro utiliza la traducción portuguesa de Thiago Dourado, *Cálculo Integral de Gottfried Wilhelm von Leibniz*, RBHM 22(45), 1–20 (2022), DOI 10.47976/RBHM2022v22n4501-20. La [ficha editorial](https://www.rbhm.org.br/index.php/RBHM/article/view/379) y el [texto extraído de la copia en ResearchGate](https://www.researchgate.net/publication/363329426_Calculo_Integral_de_Gottfried_Wilhelm_von_Leibniz) se consultaron en R07. Se reutilizan los pasajes efectivamente leídos: pp. 6–7, preferencia por la escritura diferencial y reciprocidad; p. 9, advertencia sobre conservar la generalidad de los avances de la variable. No se atribuye al documento la fórmula moderna del Teorema 7.1 ni una primera invención de la integración por partes.

Estado: PRIMARY_IN_PORTUGUESE_TRANSLATION_SELECTED_EXTRACTED_TEXT_READ_IN_R07 / REUSED_WITH_LOCATORS_IN_R08. No se declara una nueva lectura íntegra en R08, cotejo visual del PDF ni colación del latín. Las ecuaciones históricas con extracción defectuosa no se transcriben. El ejemplo afín y su interpretación mediante la cadena son una explicación matemática del capítulo, no una traducción de un ejemplo de Leibniz. H1–H6 y el registro anterior se conservan; el complemento amplía el nivel documental del recuadro sin reescribir retroactivamente esos controles.
