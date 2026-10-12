---
title: Capítulo 10 — Notas históricas y control de fuentes
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
source-id: EDC-C10-NOTAS-HISTORICAS
source-sha256: cabbc9e2cb6c16fef4926b6259538c0956b22b7919e4ecbf7aaa8cdea9140db6
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-10.html) · [Ejercicios](capitulo-10-ejercicios.html) · [Soluciones](capitulo-10-soluciones.html) · [Notas históricas](capitulo-10-notas.html)

Estas notas acompañan [el capítulo 10](capitulo-10.html). Se distinguen tres niveles: **historia documentada**, **reconstrucción matemática contemporánea** y **modelos físicos o biológicos idealizados**. Las demostraciones y condiciones de regularidad del capítulo pertenecen a EDC y no se atribuyen literalmente a autores antiguos. Una ficha de un original no cuenta como colación de su contenido; un resultado matemático moderno no acredita por sí mismo una prioridad histórica.

## H1. El problema inverso de tangentes y las ecuaciones diferenciales

Las preguntas por curvas determinadas mediante tangentes, velocidades u otras relaciones diferenciales surgieron alrededor del desarrollo del cálculo en el siglo XVII. Es legítimo relacionar estas preguntas con las tradiciones de Newton y Leibniz, pero no es correcto afirmar que ya dispusieran de nuestra formulación sobre $F:D\subseteq\mathbb R^2\to\mathbb R$, problemas de valor inicial y prueba de unicidad Lipschitz. La conexión entre ecuaciones en *fluxiones* e investigaciones de las décadas de 1670–1690 ha sido estudiada por historiadores de las matemáticas.

**Fuente especializada consultada:** Tom Archibald e Ivor Grattan-Guinness, «The History of Differential Equations, 1670–1950», *Oberwolfach Reports* (2005), [registro y resumen de EMS Press](https://ems.press/journals/owr/articles/765). El resumen sitúa las ecuaciones fluxionales de Newton en la década de 1670 y la emergencia de las ecuaciones diferenciales en la tradición de Leibniz y los Bernoulli a partir de la década de 1680. **Consulta efectiva:** registro/resumen público, no lectura integral de todas las contribuciones de la reunión.

**Historiografía secundaria:** O'Connor y Robertson, [«Calculus history»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), *MacTutor*, contexto sobre Newton, Leibniz y la expansión del cálculo. **Estado:** `SPECIALIST_ABSTRACT_READ / MACTUTOR_SECONDARY_READ / SEVENTEENTH_CENTURY_PRIMARY_NOT_COLLATED`.

## H2. Los Bernoulli y la clasificación de ecuaciones

La **ecuación de Bernoulli**, en la clasificación moderna, es una EDO de primer orden $y'+p(t)y=q(t)y^\alpha$ con $\alpha\notin\{0,1\}$. Se transforma, en una rama donde $y$ tenga el signo y regularidad necesarios, mediante $z=y^{1-\alpha}$ a una ecuación lineal. El nombre histórico **no** significa que las condiciones de existencia, continuidad y signo de nuestro capítulo fueran expresadas de esa forma en el siglo XVII. El modelo logístico de C10 es un caso algebraicamente relacionado con $\alpha=2$, aunque aquí lo resolvemos y estudiamos como modelo separado.

**Referencia moderna consultada:** [*Encyclopedia of Mathematics*, «Bernoulli equation»](https://encyclopediaofmath.org/wiki/Bernoulli_equation), definición y transformación, con referencia bibliográfica a Johann Bernoulli, *Acta Eruditorum* (1695), pp. 59–67 y 537–557. Estas páginas son **localizadores bibliográficos proporcionados por la enciclopedia**, no páginas primarias cotejadas personalmente; la edición latina de 1695 no fue colacionada. **Estado:** `MODERN_MATH_REFERENCE_READ / LATIN_PRIMARY_CATALOGUED_NOT_COLLATED`.

## H3. Euler, factores integrantes y métodos operatorios

La biografía de Leonhard Euler en MacTutor documenta que el siglo XVIII amplió decisivamente la investigación de ecuaciones diferenciales, incluyendo **factores integrantes, ecuaciones lineales y métodos de aproximación**. En C10 reconstruimos el factor integrante $\mu=e^{\int p}$ desde una regla del producto y el Teorema Fundamental de C06, una prueba moderna que no se presenta como transcripción de Euler. El nombre «variación de la constante» designa también una idea operatoria con genealogía histórica compleja y no debe convertirse en una atribución exclusiva sin examen de originales.

**Fuente secundaria efectivamente leída:** [MacTutor, «Leonhard Euler»](https://mathshistory.st-andrews.ac.uk/Biographies/Euler/), secciones sobre ecuaciones diferenciales, factores integrantes, mecánica y cálculo integral. **Contraste matemático moderno:** [*Encyclopedia of Mathematics*, «Differential equation, ordinary»](https://encyclopediaofmath.org/wiki/Differential_equation%2C_ordinary), formulación de problemas iniciales y de unicidad. No se han colacionado los tratados de Euler *Institutiones calculi integralis* ni sus manuscritos particulares. **Estado:** `MACTUTOR_SECONDARY_READ / MODERN_REFERENCE_READ / EULER_PRIMARY_NOT_COLLATED`.

## H4. El crecimiento logístico y Pierre-François Verhulst

La ecuación logística surge de intentar representar **un crecimiento que se desacelera al acercarse a una capacidad limitada**. La historiografía atribuye a Pierre-François Verhulst una propuesta poblacional en 1838 y una exposición influyente en 1845; las fechas de conferencia, publicación, cambio de terminología y redescubrimientos posteriores deben distinguirse. La constante $K$ en nuestro Teorema 10.7 representa un parámetro supuesto, no un hecho universal sobre poblaciones reales.

**Biografía secundaria leída:** [MacTutor, «Pierre François Verhulst»](https://mathshistory.st-andrews.ac.uk/Biographies/Verhulst/), pasajes sobre 1838, comunicaciones de 1844 y publicación de 1845. **Registro primario localizado y parcialmente visible:** P.-F. Verhulst, «Recherches mathématiques sur la loi d'accroissement de la population», *Nouveaux mémoires de l'Académie royale des sciences et belles-lettres de Bruxelles* **18** (1845), pp. 1–40, DOI [10.3406/marb.1845.3438](https://doi.org/10.3406/marb.1845.3438), [Persée](https://www.persee.fr/doc/marb_0770-8157_1845_num_18_1_3438). El registro muestra el título y páginas de la edición, **no acredita una colación matemática página a página de la memoria francesa**.

**Estudio historiográfico especializado (resumen consultado):** [«The early origins of the logit model»](https://doi.org/10.1016/j.shpsc.2004.09.003), *Studies in History and Philosophy of Science Part C* **35** (2004), 613–626, sobre Verhulst y la historia posterior del modelo. **Estado:** `SECONDARY_BIOGRAPHY_READ / PRIMARY_RECORD_PARTIALLY_VISIBLE / SPECIALIST_ABSTRACT_ONLY`.

## H5. Newton, la medición del calor y el enfriamiento

La llamada «ley del enfriamiento de Newton» tiene una genealogía histórica vinculada a la medición experimental de temperaturas y el trabajo de Newton sobre escalas de calor. Una aplicación actual de la EDO $T'=-k(T-T_a)$ presupone **ambiente constante y un coeficiente proporcional efectivo**, no equivale sin mediaciones a la metodología experimental de Newton. El resultado matemático del capítulo describe las consecuencias de aceptar ese modelo idealizado, no demuestra su validez física irrestricta.

**Investigación histórica leída en resumen y extractos:** J. Simón Calero (2021), [«La *Scala graduum caloris* de Newton. Una simulación numérica»](https://doi.org/10.3989/asclepio.2021.16), *Asclepio* **73** (1), p350. El artículo sitúa *Scala graduum caloris* en *Philosophical Transactions* **22** (1700–1701), pp. 824–829, como publicación anónima de 1701. **Corroboración histórico-documental:** [The Newton Project, capítulo XXV](https://newtonproject.ox.ac.uk/view/texts/normalized/OTHE00086), texto normalizado de una biografía posterior que describe la comunicación de mayo de 1701 y la publicación. **Reserva:** ese capítulo biográfico no es la reproducción diplomática del artículo científico original; el latín de 1701 no fue colacionado íntegramente para EDC-C10.


## H6. Mecánica, vibración y el oscilador armónico

El oscilador armónico $x''+\omega^2x=0$ se presenta aquí como consecuencia de una **ley restitutiva proporcional** en un modelo unidimensional, no como reproducción de un problema de ondas, una cuerda vibrante ni una ecuación diferencial parcial. La demostración de unicidad mediante $E=(x')^2+\omega^2x^2$ utiliza un invariante matemático verificable por producto y derivada; no presupone que toda vibración natural sea exactamente armónica.

**Contexto secundario:** [MacTutor, «Leonhard Euler»](https://mathshistory.st-andrews.ac.uk/Biographies/Euler/), contribuciones a mecánica, acústica, membranas vibrantes y métodos diferenciales; [MacTutor, «Lagrange Analytical Mechanics»](https://mathshistory.st-andrews.ac.uk/Extras/Lagrange_Analytical_Mechanics/), desarrollo histórico de las ecuaciones del movimiento. Son panoramas históricos, **no referencias que documenten nuestra prueba concreta de energía para este PVI**. **Estado:** `SECONDARY_CONTEXT_READ / NO_HISTORICAL_PROOF_ATTRIBUTED`.

## H7. Existencia, unicidad y condiciones de regularidad

Para el siglo XIX, la cuestión no era sólo encontrar antiderivadas o fórmulas especiales, sino decidir **bajo qué hipótesis una ley y un dato determinan una trayectoria**. El resultado moderno frecuentemente llamado de Picard–Lindelöf o Cauchy–Lipschitz exige hipótesis apropiadas y prueba tanto existencia local como unicidad. En C10 deliberadamente **no** demostramos ese teorema general: el Teorema 10.6 sólo garantiza **unicidad de dos soluciones que ya existen** bajo una desigualdad Lipschitz en un rectángulo, mientras que los teoremas 10.1–10.3 construyen soluciones para clases concretas.

**Contraste matemático efectivamente consultado:** [*Encyclopedia of Mathematics*, «Differential equation, ordinary»](https://encyclopediaofmath.org/wiki/Differential_equation%2C_ordinary), secciones de problema de Cauchy y de condiciones de unicidad. La genealogía y prioridades precisas de Cauchy, Lipschitz, Picard y Lindelöf requieren fuentes históricas especializadas y originales que **no** fueron cotejados aquí. **Estado:** `MODERN_MATH_REFERENCE_READ / SPECIFIC_HISTORICAL_PRIORITY_NOT_CLAIMED`.

## H8. El llamado método de Euler y los errores de aproximación

El paso explícito $y_{n+1}=y_n+hF(t_n,y_n)$ recibe hoy el nombre «método de Euler». En C10 se ha demostrado **sólo** la cota del error local de un paso iniciado desde un punto exacto cuando existe segunda derivada acotada; no se ha demostrado convergencia global del método numérico para cualquier campo $F$. El epónimo moderno no permite identificar sin trabajo histórico adicional una publicación precisa de Euler que contenga nuestro enunciado de Taylor–Lagrange y nuestra notación.

**Referencia secundaria de contexto:** [MacTutor, «Leonhard Euler»](https://mathshistory.st-andrews.ac.uk/Biographies/Euler/), su trabajo sobre aproximaciones y ecuaciones diferenciales. **Contraste pedagógico moderno localizado:** [UC Davis, notas de ecuaciones de primer orden](https://www.math.ucdavis.edu/~tracy/courses/math22B/22BBook.pdf), manual matemático; **no se realizó una colación por páginas de ese PDF en EDC-M11**. **Estado:** `SECONDARY_CONTEXT_READ / MODERN_PEDAGOGICAL_PDF_INDEX_ONLY`.

## Registro consolidado de procedencia

| Obra o documento | Estado efectivo de consulta | Uso autorizado y reserva |
|---|---|---|
| Archibald y Grattan-Guinness, *Oberwolfach Reports* | Resumen editorial abierto | Panorama de siglos XVII–XX; no atribución literal de pruebas |
| MacTutor: historia del cálculo, Euler, Verhulst y mecánica de Lagrange | Páginas secundarias consultadas | Contexto de problemas, publicaciones y métodos |
| *Encyclopedia of Mathematics*: Bernoulli y EDO ordinaria | Entradas matemáticas consultadas | Definiciones y contraste moderno; no páginas primarias |
| Verhulst, *Recherches mathématiques...* (1845), Persée | Registro y portada parcial visibles; original sin colación integral | Año, título, volumen y localizador bibliográfico |
| Simón Calero (2021), *Asclepio*; Newton Project | Resumen/extractos y biografía normalizada consultados | Historia de *Scala graduum caloris* con reserva documental |
| *The early origins of the logit model* (2004) | Resumen abierto | Evolución histórica del nombre «logístico», no artículo completo |
| Originales de Newton, Bernoulli, Euler, Verhulst y los historiadores de existencia | Algunos localizados; sin cotejo sistemático | Pendientes para la auditoría histórica transversal de C11 |

**Dictamen:** los modelos y demostraciones son parte de *Elementos del cálculo*, no reproducciones de escritos históricos. Las notas exponen los límites reales de lectura y colación. Los originales no examinados no se citan con páginas de contenido inventadas ni se les atribuyen nuestras condiciones de regularidad actuales.
