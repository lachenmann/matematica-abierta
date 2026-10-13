---
title: Capítulo 0 — Notas históricas y de fuentes
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
source-id: EDC-C00-NOTAS-HISTORICAS
source-sha256: 38c3f231be2a627ad4fe1f9bb6d04d942aa086a70855fe2bfcb39f2ca6f958d7
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-00.html) · [Ejercicios](capitulo-00-ejercicios.html) · [Soluciones](capitulo-00-soluciones.html) · [Notas históricas](capitulo-00-notas.html)

Estas notas acompañan el [capítulo 0](capitulo-00.html). Su función es **documentar afirmaciones y advertir sobre anacronismos**, no suministrar por autoridad histórica pruebas de las proposiciones matemáticas, que se ofrecen dentro de la exposición. Cada entrada indica el tipo de fuente, el pasaje consultado y el límite de la afirmación.

## H1 — Cuadraturas antiguas y Arquímedes

El problema de determinar áreas delimitadas por curvas es anterior al cálculo moderno. El ejemplo de la cuadratura del segmento parabólico de Arquímedes y el papel de la aproximación geométrica están documentados en la historia de la disciplina.

**Control consultado:** MacTutor History of Mathematics, «A history of the calculus», párrafos iniciales sobre el método de agotamiento, Eudoxo y Arquímedes (https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/). En particular, la página describe la razón $4/3$ respecto de un triángulo asociado al segmento parabólico. **Apoyo adicional localizado:** William Dunham, «Historically Speaking: 1. The Quadrature of the Parabola», *MAA Convergence* (https://old.maa.org/press/periodicals/convergence/historically-speaking-1-the-quadrature-of-the-parabola); su ficha de búsqueda describe un comentario a la reconstrucción moderna de Carl Boyer y Phillip S. Jones, pero la página completa no se pudo abrir en esta consulta. No se atribuye aquí un número de página al original antiguo.

**Límite:** presentar una suma $\sum k^2/n^3$ como lo que «hizo Arquímedes» sería incorrecto. Las sumas del capítulo 0 son **construcciones modernas ilustrativas**, no transcripciones ni equivalentes literales de su técnica geométrica. El análisis directo de una edición primaria de Arquímedes se reserva para C04.

## H2 — Métodos para tangentes, acumulación y cambio en los siglos XVI y XVII

Los procedimientos para tangentes, máximos/mínimos y cuadraturas no surgieron en un único paso ni bajo un vocabulario unificado. Entre los nombres que aparecen al reconstruir este proceso se cuentan Fermat, Cavalieri, Torricelli, Barrow, Newton y Leibniz.

**Control consultado:** MacTutor History of Mathematics, «A history of the calculus», apartados que presentan a Fermat/Descartes, Cavalieri, Torricelli/Barrow, fluxiones de Newton y diferenciales de Leibniz (https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/). Se trata de una síntesis secundaria, útil para fijar una orientación y una cronología general, no de una edición crítica de los manuscritos de los autores.

**Límite:** el cociente $[f(a+h)-f(a)]/h$ tratado con $\varepsilon$–$\delta$ en EDC pertenece al lenguaje moderno. No atribuir tal definición precisa a Fermat, Galileo, Barrow, Newton o Leibniz sin comprobar textos originales y el significado de sus términos. Tampoco emplear «descubridor del cálculo» en sentido exclusivo sin matizar tradiciones y problemas distintos.

## H3 — Historia conceptual y orden pedagógico

La sucesión didáctica «límites → derivadas → integrales → series» no debe confundirse con el orden cronológico efectivo de los problemas históricos. La exposición formal moderna es el resultado de desarrollos posteriores; en particular, el estudio del siglo XIX contribuyó decisivamente a fijar las formas de rigor que hoy se enseñan.

**Control consultado:** David M. Bressoud, presentación de *Calculus Reordered: A History of the Big Ideas*, *Mathematical Association of America*, 1 de julio de 2019 (https://maa.org/math-values/launchings201906-z45y4/), y ficha editorial/JSTOR del libro (https://www.jstor.org/stable/j.ctvc778s8), Princeton University Press, 2019.

**Límite:** Bressoud constituye una fuente secundaria de interpretación histórica y pedagógica. No se afirma haber leído el PDF completo localizado en Drive ni se proporcionan páginas interiores no verificadas. EDC puede escoger un orden de exposición moderno distinto del orden de desarrollo histórico, siempre que mantenga visible esa diferencia.

## H4 — Genealogía intelectual del proyecto

La lectura previa o paralela de Gabor Toth, *Elements of Mathematics: A Problem-Centered Approach to History and Foundations*, Springer, 2021, es recomendada expresamente en el [prefacio de EDC](prefacio.html). Esa genealogía explica la decisión de partir de problemas y llegar a demostraciones, pero **no convierte los pasajes de Toth en fuentes primarias de historia** ni atribuye a su autor participación en esta obra.

**Registros internos contrastados en EDC-M00:** `TOTH-EOM/PROJECT_STATUS.md`, `TOTH_CLOSURE_AUDIT.md` y `TOTH-C04-S03` (diferenciabilidad); todos mantienen independencia editorial. Los ejemplos y demostraciones del capítulo 0 son reconstrucciones autónomas. No se trasladan ejercicios, ilustraciones ni prosa de Toth o *Cálculo para matemáticos*.

## H5 — Cauchy: límite, incrementos y condiciones de las fórmulas

**Fuente primaria leída en esta revisión:** Augustin-Louis Cauchy, *Cours d’analyse de l’École royale polytechnique*, première partie: Analyse algébrique (1821), transcripción de Wikisource, https://fr.wikisource.org/wiki/Cours_d’analyse_de_l’école_royale_polytechnique/Texte_entier.

**Localizadores efectivos:** introducción, párrafos sobre el propósito de escribir el curso para los alumnos y sobre las condiciones de validez de las fórmulas; preliminares, párrafos de definición de cantidad variable, límite y cantidad infinitamente pequeña; capítulo II, §II, «De la continuité des fonctions», párrafos iniciales que relacionan el incremento del argumento con el incremento de la función. Consultados el 13-10-2026 UTC / 12-10-2026 en Santiago. Se leyó la transcripción de esos pasajes, no se efectuó colación con las imágenes de todas las páginas de la edición.

**Resultado para el recuadro publicable:** se conserva el episodio de 1821 y se reemplaza la apertura genérica de aproximaciones por dos ejemplos presentes en los preliminares: fracciones que aproximan un irracional y polígonos inscritos que aproximan el área de un círculo. La conexión entre esas formulaciones y nuestras tolerancias se presenta como lectura pedagógica actual, sin atribuir a Cauchy la definición exacta de EDC. La mención del incremento infinitamente pequeño pertenece al vocabulario de la fuente; no introduce un infinitesimal como número real en la teoría del capítulo.

**Límite:** cotejo de pasajes concretos, no historia exhaustiva del rigor decimonónico ni afirmación de prioridad exclusiva. No se añaden citas literales ni paginación impresa no verificada.

## Registro bibliográfico local de C00

| Código | Fuente | Estado documental | Utilización en C00 |
|---|---|---|---|
| C00-H1 | MacTutor, «A history of the calculus» | Texto web consultado el 10-10-2026 | Cuadratura antigua, antecedentes de tangentes, Newton/Leibniz; síntesis secundaria |
| C00-H2 | MAA, Dunham, «Historically Speaking: 1. The Quadrature of the Parabola» | Ficha de búsqueda consultada; lectura web íntegra no obtenida | Apoyo a existencia del ejemplo de Arquímedes; no hay cita de página |
| C00-H3 | Bressoud, presentación de *Calculus Reordered*, MAA (2019) | Presentación web consultada el 10-10-2026 | Diferencia entre orden histórico y orden de exposición |
| C00-H4 | Toth, *Elements of Mathematics* (2021) | Obra localizada en Drive; lectura/traducción anterior registrada en TOTH-EOM | Deuda intelectual; no prueba de hechos históricos específicos |
| C00-H5 | Bressoud, *Calculus Reordered* (2019) | PDF localizado por metadatos en Drive; sin lectura completa en M01 | Bibliografía futura para C04/C11 |
| C00-H6 | Cauchy, *Cours d’analyse* (1821) | Pasajes de introducción, preliminares y II §II leídos en transcripción web durante RLI-R01; facsímil no colacionado | Control del recuadro «Cauchy y el arte de acercarse» |

**Pendientes legítimos para capítulos futuros:** cotejo de fuentes primarias de Arquímedes, Fermat, Newton y Leibniz, así como discusión historiográfica de tradiciones no europeas. Ninguno es necesario para la validez de los ocho teoremas y las proposiciones demostradas en C00.
