---
title: Capítulo 3 — Notas históricas y control de fuentes
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
source-id: EDC-C03-NOTAS-HISTORICAS
source-sha256: 7363a5c6fe9f019dd5a0a05ba2a26ce04045196eae02cddeb8e3923fa3311343
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-03.html) · [Ejercicios](capitulo-03-ejercicios.html) · [Soluciones](capitulo-03-soluciones.html) · [Notas históricas](capitulo-03-notas.html)

Las notas acompañan [el capítulo 3](capitulo-03.html) sin convertirse en premisas de sus demostraciones. Distinguen **una reconstrucción matemática contemporánea**, las investigaciones históricas secundarias efectivamente consultadas y la disponibilidad de documentos primarios que aún no se han cotejado en su texto. Un título localizado no equivale a una lectura; una noticia biográfica no avala una atribución de prioridad absoluta.

## H1. Fermat: un problema anterior a la derivada moderna

La búsqueda de máximos y mínimos mediante operaciones algebraicas tiene en Pierre de Fermat un antecedente decisivo. El procedimiento que se describe habitualmente como **adigualdad** o *adequality* comparaba expresiones asociadas con una incógnita y su incremento, simplificaba y eliminaba términos dependientes del incremento. En notación y reconstrucción modernas puede recordar operaciones que preceden al cociente incremental, pero **no** debe presentarse como una prueba original del teorema de Fermat formulado sobre funciones continuas y derivables en un intervalo real.

**Fuente secundaria localizada y consultada por su contenido público:** Kenneth M. Monks, «Fermat’s Method for Finding Maxima and Minima: A Mini-Primary Source Project for Calculus 1 Students», *Convergence*, Mathematical Association of America, febrero de 2023, DOI `10.4169/convergence20230201`, https://old.maa.org/press/periodicals/convergence/fermat-s-method-for-finding-maxima-and-minima-a-mini-primary-source-project-for-calculus-1-students . La ficha presenta un proyecto de lectura sobre Fermat y su desacuerdo con Descartes. El texto visible contiene una traducción de una comunicación de Fermat enviada a Descartes por mediación de Mersenne en 1638, con localizador atribuido a una edición de escritos de Fermat de 1636–1642, pp. 133–134. **No** se ha cotejado dicha edición primaria, por lo que la localización de páginas se conserva sólo como referencia de la fuente secundaria.


## H2. Michel Rolle: teoría algebraica de ecuaciones y resistencia a infinitésimos

La biografía de MacTutor sitúa el resultado asociado a Rolle en su obra *Démonstration d'une Méthode pour resoudre les Egalitez de tous les degrez* (1691), vinculada con un método de «cascadas» de ecuaciones polinómicas. Señala que el nombre posterior «teorema de Rolle» fue empleado por Giusto Bellavitis en 1846. El contexto **no** era todavía el teorema general moderno para toda función continua en $[a,b]$ y derivable en $(a,b)$ que se demuestra en §3.3.

MacTutor documenta asimismo la crítica de Rolle al cálculo de infinitesimales y su controversia con Pierre Varignon. Por ello sería históricamente equivocado afirmar que Rolle formuló nuestra prueba moderna como parte de una defensa del cálculo infinitesimal.

**Fuente secundaria efectivamente leída:** J. J. O'Connor y E. F. Robertson, «Michel Rolle», *MacTutor History of Mathematics*, https://mathshistory.st-andrews.ac.uk/Biographies/Rolle/ , sección **Biography**, párrafos «cascades», publicación de 1691, denominación de Bellavitis y controversia Rolle–Varignon. El artículo fue actualizado en diciembre de 2008 según su propia ficha.


## H3. Valor medio: Lagrange, Cauchy y el problema de la rigurosidad

La denominación **valor medio de Lagrange** es matemática y editorialmente habitual, pero no se debe convertir en un relato simple de invención por un solo autor. La tradición de estudiar incrementos finitos, desigualdades derivativas y propiedades de raíces se desarrolló por etapas. La formulación y las demostraciones rigurosas de Augustin-Louis Cauchy constituyen hitos del siglo XIX; sus argumentos históricos deben estudiarse en relación con trabajos anteriores de Lagrange y otros autores.

**Fuentes consultadas:** «Cauchy's Calculus», MacTutor, https://mathshistory.st-andrews.ac.uk/Extras/Cauchy_Calculus/ , párrafos sobre el *Cours d'Analyse* de 1821, derivada y versión histórica del valor medio; y «Earliest Uses of Symbols of Calculus», https://mathshistory.st-andrews.ac.uk/Miller/mathsym/calculus/ , apartado sobre el primer uso de $\varepsilon$ y $\delta$ y los argumentos de Cauchy en sus lecciones de 1823. El segundo registro recoge observaciones atribuidas a Judith V. Grabiner sobre el contexto de la prueba, no una colación independiente del texto original por EDC.

La exposición de §3.4 es una demostración moderna mediante la función auxiliar que resta la recta secante. No se afirma que Cauchy escribiera exactamente esa fórmula con nuestras hipótesis y nuestra notación.


## H4. Darboux: las derivadas y una propiedad que no equivale a continuidad

En 1875, Gaston Darboux publicó *Mémoire sur les fonctions discontinues*. La *Encyclopedia of Mathematics* relaciona ese año con la demostración de que las derivadas finitas poseen la propiedad de los valores intermedios y con ejemplos de derivadas discontinuas. Esto explica la importancia de distinguir el Teorema 3.8 de una afirmación falsa: no estamos diciendo que $f'$ deba ser continua.

**Fuente secundaria consultada:** «Darboux property», *Encyclopedia of Mathematics*, https://encyclopediaofmath.org/wiki/Darboux_property , entrada relativa a la propiedad de valor intermedio y a la investigación histórica de 1875.

**Ficha bibliográfica primaria verificada, texto no cotejado:** G. Darboux, «Mémoire sur les fonctions discontinues», *Annales scientifiques de l'École Normale Supérieure*, 2.ª serie, tomo 4 (1875), pp. 57–112, DOI `10.24033/asens.122`; registro en https://archive.numdam.org/item/ASENS_1875_2_4__57_0/ . La existencia de la edición y sus páginas se confirmaron en la ficha, **sin afirmar lectura del artículo entero ni de su facsímil**.


## H5. Extremos clásicos y problemas de optimización

La optimización no se agota en el cálculo de una derivada. Los problemas geométricos de máximos y mínimos tienen una tradición anterior a la teoría moderna: el modo en que se elegía el objeto, se expresaba una restricción y se justificaba una respuesta varió a través de épocas y disciplinas. El tratamiento de rectángulos, cilindros y funciones con decaimiento en C03 es una **selección contemporánea de problemas modelo**, sin atribuir a un personaje histórico concreto la solución actual con estas variables.

**Fuente secundaria consultada:** Gabriela R. Sanchis, «Historical Activities for Calculus — Module 3: Optimization Problems Then and Now», MAA *Convergence* (junio de 2014), https://old.maa.org/press/periodicals/convergence/historical-activities-for-calculus-module-3-optimization-problems-then-and-now . El módulo relaciona problemas de Herón, Snell, Regiomontano, Galileo y otros; sus ejemplos sirven para el diseño de futuras investigaciones históricas, **no** para afirmar que el enunciado exacto del cilindro cerrado de nuestro Ejercicio 3.27 proceda de una fuente antigua.


## H6. Genealogía de Toth y frontera de proyectos

*Elements of Mathematics* de Gabor Toth ya introduce nociones de derivabilidad, puntos críticos y principio de Fermat en su capítulo 4. El propósito de C03 no es reclamar prioridad temática frente a Toth, sino articular con detalle una teoría propia de Rolle y del valor medio, las desigualdades globales de incremento, la convexidad y la optimización, manteniendo una cadena demostrativa independiente. El resultado previo de Toth constituye una **inspiración intelectual**, no una autorización para reproducir su redacción o sus problemas.

*Cálculo para matemáticos* contiene tratamientos afines de Rolle, valor medio, monotonía y convexidad. No se han copiado de ese corpus las demostraciones, figuras o ejercicios; se mantiene la separación documental, de identificadores y de licencias. Véase la [nota editorial sobre autonomía y fuentes](edicion.html).

## Matriz de fuentes y reservas

| Entrada | Tipo | Consultado en M04 | Alcance permitido |
|---|---|---|---|
| Monks, MAA *Convergence*, Fermat (2023) | Secundaria que incorpora traducción histórica | Contenido público de la ficha/resultados, no la edición primaria | Adecuación algebraica y contexto Fermat–Descartes, con reservas |
| MacTutor, Michel Rolle | Síntesis histórica | Sección biográfica y párrafos sobre 1691 y controversia | Origen algebraico del resultado asociado con su nombre |
| MacTutor, Cauchy's Calculus | Síntesis histórica | Apartados sobre rigor, límites, derivadas y valor medio | Contextualización de las formas rigurosas posteriores |
| MacTutor, símbolos de cálculo | Historia de notación | Pasaje relevante sobre valor medio y criterios del siglo XIX | Advertencia sobre lectura retrospectiva |
| Encyclopedia of Mathematics, Darboux property | Enciclopedia | Entrada pública consultada | Contexto de 1875 y derivada con propiedad intermedia |
| Darboux (1875), Numdam | Fuente primaria | Sólo ficha de metadatos, no facsímil | Registro bibliográfico, **no** cita textual |
| Sanchis, MAA (2014) | Didáctica historiográfica | Página pública consultada | Inventario de situaciones históricas de optimización |
| Toth 2021 | Antecedente bibliográfico | Control EDC-M00, sin nueva lectura integral | Genealogía, no copia |
| CPM | Obra propia independiente | Control EDC-M00, sin traslado | Frontera de compatibilidad, no importación |

**Reserva bibliográfica no bloqueante:** una futura edición histórica ampliada necesitará cotejar las obras originales de Fermat, Rolle y Cauchy y las páginas pertinentes del tratado de Darboux; no hay citas de página inventadas ni se confunde la comprobación de una ficha con la lectura de un texto. Las demostraciones del capítulo no dependen de esas atribuciones.
