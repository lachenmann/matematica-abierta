---
title: Capítulo 6 — Notas históricas y control de fuentes
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
source-id: EDC-C06-NOTAS-HISTORICAS
source-sha256: c4d35997cb177a3574f131eac74d5b3ab94bd8d5c13dba7b40e52df2af9c3c4a
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-06.html) · [Ejercicios](capitulo-06-ejercicios.html) · [Soluciones](capitulo-06-soluciones.html) · [Notas históricas](capitulo-06-notas.html)

Estas notas acompañan [el capítulo 6](capitulo-06.html) y conservan la diferencia entre las **pruebas actuales**, la **historiografía efectivamente consultada** y las **fuentes primarias localizadas pero todavía no colacionadas**. Las demostraciones de EDC pertenecen a un sistema moderno de funciones reales, derivadas por límite e integral Riemann–Darboux. No atribuimos ese sistema retrospectivamente a autores de los siglos XVII o XVIII.

## H1. Un resultado con más de una genealogía

El vínculo entre tangentes, cuadraturas y magnitudes variables se desarrolló mediante varias tradiciones europeas del siglo XVII. Torricelli, James Gregory, Isaac Barrow, Isaac Newton y Gottfried Wilhelm Leibniz aparecen en la bibliografía histórica con contribuciones distintas. No es correcto identificar sin examen «primera intuición de operaciones inversas», «demostración geométrica de un caso», «expresión analítica», «notación general» y «enunciado actual del Teorema Fundamental».

**Fuente secundaria efectivamente leída:** John J. O'Connor y Edmund F. Robertson, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), MacTutor History of Mathematics, párrafos sobre Torricelli, Barrow, Newton y Leibniz (texto web abierto y leído en este macrotramo). Allí se describe el paso de métodos particulares a interpretaciones de inversión entre velocidad y desplazamiento, y se discuten las distintas concepciones de Newton y Leibniz.

**Reserva:** esa misma síntesis afirma que Barrow se aproximó al resultado, pero «nunca lo enunció explícitamente». Otra historiografía interpreta una de sus proposiciones geométricas como una versión del teorema. No disimulamos la diferencia entre criterios de atribución.

**Estado:** `SECONDARY_WEB_READ / DEFINITION_OF_FIRST_STATEMENT_CONTESTED / NO_PRIMARY_COLLATION`.

## H2. Barrow y el lenguaje geométrico

Las *Lectiones Geometricae* de Isaac Barrow circularon impresas en 1670 según MacTutor y el catálogo de ediciones. La obra contiene relaciones entre tangentes, curvas asociadas a áreas y segmentos de referencia. Una traducción e interpretación historiográfica importante sitúa en la **Lección X, proposición 11** una relación que puede reconstruirse en notación moderna como derivada de una función de área. Esta lectura no significa que Barrow formulara una integral de Riemann ni el par de afirmaciones de nuestros Teoremas 6.2 y 6.5 con hipótesis de continuidad en $[a,b]$.

**Localizadores de contraste:** MacTutor, [biografía de Isaac Barrow](https://mathshistory.st-andrews.ac.uk/Biographies/Barrow/), sección acerca de la publicación de *Lectiones Geometricae* (1670); [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), párrafos sobre el triángulo diferencial y las cuadraturas; Frank J. Swetz y Victor J. Katz, [«Mathematical Treasures — Isaac Barrow's Geometrical Lectures»](https://old.maa.org/press/periodicals/convergence/mathematical-treasures-isaac-barrows-geometrical-lectures), ficha indexada que presenta esa obra como poseedora de una de las primeras demostraciones del resultado moderno. La ficha MAA se identificó por resultado web; su lectura integral en el servidor antiguo queda **pendiente**.

**Facsímil localizado sin colación:** [*Lectiones geometricae* (1670), reproducción en Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lectiones_geometricae-_..._1670_(IA_bim_early-english-books-1641-1700_lectiones-geometricae-_barrow-isaac_1670).pdf), ficha y metadata pública. El acceso a la ficha **no** equivale a una lectura paleográfica del libro ni a la identificación personal de páginas internas.

**Estado:** `MACTUTOR_READ / MAA_INDEX_ONLY / FACSIMILE_LOCATED_NOT_COLLATED`.

## H3. Newton y las cantidades fluyentes

MacTutor sitúa en manuscritos de la década de 1660 el trabajo de Newton sobre fluxiones, fluentes, tangentes y áreas. En la presentación de esa historiografía, encontrar una magnitud a partir de su fluxión constituye un problema inverso estrechamente vinculado con las cuadraturas; algunas exposiciones lo describen como un antecedente explícito del Teorema Fundamental. El orden de escritura, circulación manuscrita y publicación posterior impide equiparar fecha de descubrimiento con primera edición pública.

**Fuente secundaria leída:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), párrafos sobre manuscrito de fluxiones de 1666, *De analysi*, publicación tardía y diferencias con la notación leibniziana.

**Fuente historiográfica localizada por índice de búsqueda, no integralmente abierta:** Omar A. Hernandez Rodriguez y Jorge M. Lopez Fernandez, [«Teaching the Fundamental Theorem of Calculus: A Historical Reflection — Newton's Proof of the FTC»](https://old.maa.org/press/periodicals/convergence/teaching-the-fundamental-theorem-of-calculus-a-historical-reflection-newtons-proof-of-the-ftc), *MAA Convergence*, enero de 2012, DOI **10.4169/loci003803**. La ficha indexada remite a la prueba de *De analysi* (1669), reproduce un argumento de rectángulos y enlaza con Guicciardini. El servidor antiguo devolvió error al abrir el texto íntegro; por tanto sólo se conserva como fuente **localizada** y no como colación directa.

**Estado:** `SECONDARY_WEB_READ / MAA_INDEX_ONLY / NEWTON_PRIMARY_NOT_COLLATED`.

## H4. Leibniz: notación e inversión de procesos

Los símbolos $d$ e $\int$ tienen una historia documental asociada a Leibniz, cuyos manuscritos y publicaciones del último tercio del siglo XVII contribuyeron a que la diferenciación y la integración pudieran manipularse como operaciones de un cálculo. La estabilidad de una notación no implica que el autor trabajara con nuestra definición de función continua, nuestra integral de Darboux ni nuestra demostración con $\varepsilon$ y $\delta$.

**Fuente secundaria leída:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), párrafos sobre el desarrollo leibniziano de $dx$, $dy$ y $\int$, manuscritos de 1675 y publicaciones posteriores.

**Testimonio primario localizado por ficha bibliográfica/reproducción, no colacionado directamente:** Frank J. Swetz, [«Mathematical Treasure: Leibniz's Papers on Calculus — Integral Calculus»](https://old.maa.org/press/periodicals/convergence/mathematical-treasure-leibnizs-papers-on-calculus-integral-calculus), *MAA Convergence*, ficha indexada que identifica el artículo latino «De geometria recondita et analysi indivisibilium atque infinitorum» en *Acta Eruditorum*, junio de **1686**, pp. 292–300, y una demostración de una forma del vínculo entre procedimientos. El artículo original **no** fue leído línea a línea en este macrotramo.

**Estado:** `MACTUTOR_READ / LEIBNIZ_PRIMARY_LOCATED_NOT_COLLATED`.

## H5. Gregory y el problema de la primera formulación

Las biografías generales suelen simplificar el relato con una sucesión Barrow–Newton–Leibniz. La historiografía más especializada atribuye también a **James Gregory** demostraciones geométricas relacionadas con curvas de áreas. Esta diferencia justifica evitar frases tajantes como «Newton fue el primero en probar el Teorema Fundamental», salvo que antes se precise cuál enunciado, qué fuente y qué criterio de equivalencia se está usando.

**Lecturas y localizadores:** MacTutor, [«A history of the calculus»](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/), síntesis de antecedentes y Newton; artículo de Hernandez Rodriguez y Lopez Fernandez, [«Integration from Cavalieri to Darboux»](https://old.maa.org/press/periodicals/convergence/teaching-the-fundamental-theorem-of-calculus-a-historical-reflection-integration-from-cavalieri-to), *MAA Convergence*, localizado mediante índice de búsqueda (no abierto completo), cuyo resumen adjudica a Barrow una formulación publicada y menciona Gregory entre los demostradores. Se mantiene esa divergencia interpretativa señalada en H1.

**Estado:** `GENERAL_SECONDARY_READ / SPECIALIST_TEXT_INDEX_ONLY / GREGORY_PRIMARY_NOT_COLLATED`.

## H6. La formalización moderna y una advertencia pedagógica

El capítulo 5 definió la integral sin invocar primitivas. Sólo ahora, en C06, se demuestra la fórmula $\int_a^b f=G(b)-G(a)$. Una enseñanza que presenta directamente la diferencia $G(b)-G(a)$ **como definición** de la integral y después la anuncia como teorema corre el riesgo de circularidad conceptual. Esto no convierte nuestra elección expositiva en una reproducción de un procedimiento de Newton o de Leibniz: es una arquitectura de rigor moderno.

**Fuente matemática actual consultada:** [*Encyclopedia of Mathematics*, «Newton–Leibniz formula»](https://encyclopediaofmath.org/wiki/Newton-Leibniz_formula), fórmula de evaluación y comentario histórico inicial. Esa entrada también menciona extensiones en el marco de Lebesgue: las extensiones **no** se incorporan a EDC-C06 y no se invocan en ninguna prueba.

**Nota didáctica localizada por índice, no abierta íntegramente:** Hernandez Rodriguez y Lopez Fernandez, [«Teaching the Fundamental Theorem of Calculus: A Historical Reflection — Introduction»](https://old.maa.org/press/periodicals/convergence/teaching-the-fundamental-theorem-of-calculus-a-historical-reflection-introduction), *MAA Convergence* (2012), cuyo resumen destaca el riesgo de vaciar de contenido el teorema cuando la integral ya fue definida por la antiderivación.

**Estado:** `EOM_READ / MAA_INDEX_ONLY / MODERN_EDC_PROOFS_INDEPENDENT`.

## Registro consolidado y tareas historiográficas diferidas

| Fuente | Condición de acceso constatada | Empleo en C06 |
|---|---|---|
| MacTutor, O'Connor–Robertson, *A history of the calculus* | Página íntegra abierta y leída | Contexto histórico general; contraste Newton–Leibniz–Barrow |
| MacTutor, biografía de Barrow | Resultado localizado; extractos legibles | Fecha editorial y trayectoria de *Lectiones Geometricae* |
| *Encyclopedia of Mathematics*, «Newton–Leibniz formula» | Resultado y entrada consultados | Convención moderna; no extiende hipótesis del libro |
| MAA, Hernandez Rodriguez–Lopez Fernandez, artículo de 2012 | Fichas indexadas; error al abrir página completa | Pistas para colación posterior; no citas directas de pasajes inaccesibles |
| MAA, Swetz/Katz y Swetz sobre Barrow/Leibniz | Fichas indexadas | Testimonios y localizadores tentativos; no lectura de los facsímiles |
| Facsímil Barrow 1670 en Commons | Metadata localizada | Fuente primaria pendiente de lectura y transcripción |
| Ediciones críticas de Newton y Leibniz | No consultadas aquí | Requerirán elección de edición, localizador y cotejo en una revisión historiográfica de fondo |

**Dictamen:** el texto principal usa atribuciones deliberadamente generales y proporcionadas a las fuentes efectivamente consultadas. Las notas documentan contradicciones historiográficas y lagunas de colación sin presentarlas como hechos demostrados. En la edición privada de C06 no se inserta ilustración tomada de un sitio comercial ni se copia un facsímil sin expediente de procedencia y derechos.


## Complemento documental — revisión literaria R07 (13 de octubre de 2026)

Se abrió la [ficha editorial de Thiago Dourado, *Cálculo Integral de Gottfried Wilhelm von Leibniz*, RBHM 22(45), 1–20 (2022)](https://www.rbhm.org.br/index.php/RBHM/article/view/379), DOI 10.47976/RBHM2022v22n4501-20. El PDF servido por la revista devolvió errores de acceso. La [copia del artículo en ResearchGate](https://www.researchgate.net/publication/363329426_Calculo_Integral_de_Gottfried_Wilhelm_von_Leibniz) permitió leer texto extraído de la traducción portuguesa: p. 2, interlocución con Craig; pp. 5–6, método inverso de tangentes y reciprocidad de sumas y diferencias. El recuadro utiliza esos pasajes. Estado: PRIMARY_IN_PORTUGUESE_TRANSLATION_SELECTED_EXTRACTED_TEXT_READ.

No se cotejó visualmente el PDF ni se colacionaron las imágenes del latín. La lectura de una traducción publicada complementa H4, pero no equivale a revisar el original. Los metadatos editoriales se comprobaron en la revista; las afirmaciones sobre el pasaje se apoyan en el texto de la traducción, no sólo en su resumen. No se adoptan como dictamen de prioridad las atribuciones generales del traductor sobre el primer descubrimiento o la primera publicación.

La ficha de Swetz sobre el artículo integral de Leibniz (MAA) reapareció en el resultado de búsqueda, pero la apertura directa del servidor antiguo volvió a fallar. Se conserva como localizador y no se declara inspección de sus facsímiles. En este tramo no se amplió el cotejo primario de Barrow, Newton o Gregory. H1–H6 y el registro anterior permanecen como historia de los controles efectuados.
