---
title: Capítulo 1 — Notas históricas y control de fuentes
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
css: /assets/books/elementos-del-calculo/edc-source-notes.css
provenance:
  type: original
  sources:
    - role: idea
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C01-NOTAS-HISTORICAS
source-sha256: f32d0eab3cbf76e5b3e4142e2cf67236a8e20a665c4d1b7e8c93b17baa7b3834
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-01.html) · [Ejercicios](capitulo-01-ejercicios.html) · [Soluciones](capitulo-01-soluciones.html) · [Notas históricas](capitulo-01-notas.html)

Estas notas acompañan [el capítulo 1](capitulo-01.html) sin incorporarse a sus demostraciones. No equiparan el vocabulario de los siglos XVI–XVII con límites $\varepsilon$–$\delta$ ni con la definición moderna de función. Una afirmación respaldada por una síntesis historiográfica secundaria no se convierte por ello en lectura directa de la fuente primaria correspondiente.

## H1. Galileo, movimiento y tiempo cuadrático

**Afirmación controlada.** La relación entre distancia recorrida desde el reposo en movimiento uniformemente acelerado y cuadrado del tiempo está documentada para Galileo. En notación moderna puede modelarse como $s(t)=ct^2$, con la elección de origen y condiciones pertinentes; esto es una **reformulación contemporánea**, no la notación original del autor.

**Fuentes consultadas:**

1. Museo Galileo, «[Galileo's law of falling bodies](https://catalogue.museogalileo.it/indepth/GalileosLawFallingBodies.html)», ficha de profundidad (*In-depth*), párrafo explicativo bajo ese título. Expone la proporcionalidad cuadrática y la secuencia de incrementos impares.
2. Michael Fowler, Universidad de Virginia, «[Galileo on Uniform and Uniformly Accelerated Motion](https://galileo.phys.virginia.edu/classes/109N/tns153.htm)», presentación de extractos de *Two New Sciences*, **Third Day**, sección de movimiento naturalmente acelerado. Es un acceso mediado a un texto histórico, no una colación de la impresión de 1638.
3. *Stanford Encyclopedia of Philosophy*, «[Galileo Galilei](https://plato.stanford.edu/entries/galileo/)», pasaje sobre la ley de caída y los planos inclinados.

**Precaución.** El capítulo toma la ley cuadrática como problema de variación y no atribuye a Galileo una operación de límite bilateral ni la fórmula simbólica $s'(t)$.

## H2. Fermat, extremos y tangentes

**Afirmación controlada.** Fermat desarrolló métodos de máximos, mínimos y tangentes que se reconocen retrospectivamente como antecedentes de la diferenciación. Su método de *adigualdad* (*adequality*) no debe identificarse sin matices con un algoritmo $\varepsilon$–$\delta$ ni reducirse a la mera sustitución de un incremento por cero.

**Fuentes consultadas:**

1. J. J. O'Connor y E. F. Robertson, «[Pierre de Fermat](https://mathshistory.st-andrews.ac.uk/Biographies/Fermat/)», MacTutor, sección **Biography**, pasajes sobre la correspondencia de 1636 con Mersenne y el envío del método sobre máximos, mínimos y tangentes, y la controversia con Descartes.
2. O'Connor y Robertson, «[A history of the calculus](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/)», MacTutor, pasajes relativos a Fermat y Descartes.
3. Roberto Cardil, «[Kepler: The Volume of a Wine Barrel — Derivatives, Tangents, and Slopes](https://old.maa.org/press/periodicals/convergence/kepler-the-volume-of-a-wine-barrel-derivatives-tangents-and-slopes-conclusion)», *MAA Convergence*, apartado **Derivatives, Tangents, and Slopes**. Útil como interpretación didáctica, no como reemplazo de textos de Fermat.
4. Mikhail G. Katz y colaboradores, «[Pierre de Fermat](https://u.math.biu.ac.il/~katzmik/fermat.html)», portal de publicaciones de investigación que describe debates interpretativos sobre *adequality*. La página de índice se consultó, **no** los artículos íntegros vinculados; por ello se registra como pista de contraste sin adscribir a esos artículos afirmaciones leídas en detalle.

**Precaución.** La disputa historiográfica sobre las prioridades y el alcance técnico de la adigualdad requiere lectura de ediciones críticas antes de atribuir a Fermat un enunciado matemático exacto presentado en el capítulo moderno.

## H3. Barrow, tangentes y cuadraturas

**Afirmación controlada.** Isaac Barrow presentó métodos geométricos de tangencia y cuadratura en sus *Lectiones Geometricae*, y hay evidencia histórica de su percepción de una relación recíproca entre esos problemas. Esa relación anticipa, sin constituir literalmente, las versiones modernas del Teorema Fundamental del Cálculo que EDC demostrará en C06.

**Fuentes consultadas:**

1. P. N. Ruane, reseña de «[The Geometrical Lectures of Isaac Barrow](https://old.maa.org/press/maa-reviews/the-geometrical-lectures-of-isaac-barrow)», *Mathematical Association of America*, **MAA Review**, fechada el 7 de noviembre de 2006. La reseña describe las lecciones de 1663–1667 publicadas en 1670, las tangentes, el triángulo diferencial y los problemas de cuadratura.
2. *Stanford Encyclopedia of Philosophy*, «[Continuity and Infinitesimals](https://plato.stanford.edu/entries/continuity/)», apartado **4. The Continuum and the Infinitesimal in the Seventeenth and Eighteenth Centuries**, pasaje sobre Barrow y la relación entre tangencia y cuadratura.
3. MacTutor, «[A history of the calculus](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/)», pasaje relativo a Torricelli y Barrow.

**Precaución.** La reseña de la MAA reproduce una afirmación fuerte de J. M. Child sobre Barrow como «primer inventor». Se registra como **tesis de Child**, no como veredicto historiográfico de EDC. No se ha colacionado un ejemplar de la edición de 1670.

## H4. Newton: cantidades fluyentes, fluxiones y fuentes polémicas

**Afirmación controlada.** El trabajo de Newton con magnitudes variables y *fluxiones* se relaciona históricamente con el problema de obtener razones de cambio y con el problema inverso de reconstruir magnitudes. Las reconstrucciones de fechas de descubrimiento, difusión manuscrita y prioridad requieren separar testimonios, publicación y evaluación historiográfica posterior.

**Fuentes consultadas:**

1. MacTutor, «[A history of the calculus](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/)», pasajes **Newton / fluxions / publicación**, después de la discusión de Barrow. Distingue trabajos de la década de 1660 y difusión posterior.
2. *The Newton Project*, «[History of the Method of Fluxions (Normalized)](https://newtonproject.ox.ac.uk/view/texts/normalized/NATP00356)», documento `NATP00356`, en especial los pasajes sobre el método de las fluxiones, las cartas de 1672–1676 y la publicación diferencial de 1684. Es **fuente primaria en contexto de disputa**, no reconstrucción neutral; se utilizó para confirmar que Newton argumentaba retrospectivamente sobre la cronología y la prioridad, no para dar por probadas todas sus imputaciones a Leibniz.

**Precaución.** El hecho de que el Newton Project transcriba una afirmación de Newton sólo demuestra que esa afirmación consta en el documento. C01 no reproduce sus acusaciones como hechos históricos independientes.

### Control adicional del recuadro Newton — EDC-RLI-R02

Se releyó la fuente primaria normalizada NATP00356 el 13-10-2026. Localizadores: f. 146v, párrafo que comienza «In the above mentiond Analysis», sobre áreas como fluentes, ordenadas como fluxiones y abscisa común que aumenta uniformemente como tiempo; f. 154v, párrafo sobre el uso del símbolo de fluxión para representar un momento, que distingue fluxiones o velocidades finitas de momentos infinitamente pequeños. Estos dos pasajes sostienen la conexión concreta entre geometría y movimiento en el recuadro revisado. La imagen inicial del punto que recorre una curva es una explicación pedagógica actual, no una cita del documento.

El recuadro conserva la diferencia entre este vocabulario y nuestro cociente incremental. No se introducen fechas nuevas de descubrimiento ni un veredicto de prioridad. La naturaleza polémica del manuscrito permanece registrada en H4. Se leyó la transcripción normalizada de pasajes concretos; no se colacionaron todas las imágenes del manuscrito. Fuente y folios verificados: https://newtonproject.ox.ac.uk/view/texts/normalized/NATP00356.

## H5. Leibniz: diferencias, cálculo y publicación

**Afirmación controlada.** En las últimas décadas del siglo XVII Leibniz desarrolló un cálculo diferencial con conceptualización y notación distintas de las fluxiones newtonianas. La publicación de su «Nova methodus pro maximis et minimis, itemque tangentibus...» en *Acta Eruditorum* (1684) constituye un hito documental, sin resolver por sí sola las disputas historiográficas sobre los manuscritos y los descubrimientos anteriores.

**Fuentes consultadas:**

1. MacTutor, «[A history of the calculus](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/)», pasajes **Leibniz / diferencias / notación $dx,dy$ / publicación**.
2. *The Newton Project*, `NATP00356` (enlace en H4), que menciona la publicación en *Acta Eruditorum* de octubre de 1684; su tratamiento es adversarial y no puede sustituir historiografía crítica.
3. P. N. Ruane, reseña MAA de Barrow (enlace en H3), párrafos sobre la publicación de las lecciones y la aparición posterior del término *calculus*.

**Precaución.** No se utilizó una imagen del artículo original ni una edición crítica de Leibniz para transcribir fórmulas o asignar localizadores de página. La valoración de la independencia de los descubrimientos se aplaza a C11 con fuentes primarias colacionadas.

## Registro de lectura y reutilización

| Tipo de fuente | Estado en EDC-M02 | Alcance |
|---|---|---|
| MacTutor — historia general y biografía de Fermat | `WEB_TEXTO_CONSULTADO` | Contexto secundario; pasajes identificados |
| Museo Galileo y Universidad de Virginia | `WEB_TEXTO_CONSULTADO` | Caída cuadrática y mediación de *Two New Sciences* |
| MAA — Barrow; MAA Convergence — Fermat | `WEB_TEXTO_CONSULTADO` | Historia matemática secundaria, no fuente primaria directamente colacionada |
| Stanford Encyclopedia — continuidad/infinitesimales | `WEB_TEXTO_CONSULTADO` | Marco historiográfico y precisión conceptual |
| Newton Project, `NATP00356` | `FUENTE_PRIMARIA_WEB_CONSULTADA_CON_RESERVA` | Testimonio polémico, no certificación de prioridad |
| PDF de Toth y bibliografía de cálculo/historia localizada en Drive en EDC-M00 | `LOCALIZADA_PREVIAMENTE; NO_RELEÍDA_EN_M02` | No se inventan páginas ni se asume revisión de texto completo |

Ninguna prueba matemática de C01 depende de la exactitud de una atribución histórica. Las lecturas web indicadas fueron consultadas el **10 de octubre de 2026**. El estado documental se limita a las páginas citadas, no a una revisión integral de sus bibliografías.
