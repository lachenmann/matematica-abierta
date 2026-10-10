---
title: "La construcción de los reales: existencia, unicidad y dos caminos de demostración"
description: "Una guía para estudiar la construcción de los números reales, comparar sus demostraciones y leer la monografía complementaria de Análisis real para matemáticos."
content-id: MA-ART-0016
content-type: article
status: published
date-created: 2026-10-09
date-modified: 2026-10-09
areas: [analisis]
level: universitario
topics: [numeros-reales, cortaduras-de-dedekind, completitud, isomorfismos]
prerequisites: []
related: [MA-BOK-0010, MA-BCH-0175, MA-BOK-0013, MA-ART-0002]
provenance:
  type: original
  sources:
    - "La construcción de los reales, edición de estudio M18 v05."
    - "Análisis real para matemáticos, capítulo 0."
    - "Divergence is Divergence, cuatro clases de Real Analysis; enlaces al final."
license: GFDL-1.3-or-later
---

Al escribir $\mathbb R$ solemos disponer de una imagen: una recta en la que podemos sumar, comparar y medir distancias. Pero esa imagen deja abiertas dos preguntas. ¿Existe un sistema que reúna todas las propiedades que usamos? Si lo construimos de otra manera, ¿obtendremos una estructura diferente?

La monografía **La construcción de los reales** desarrolla ambas preguntas y continúa hasta la desigualdad triangular y el control de errores. Reúne cuatro capítulos, tres apéndices y 78 ejercicios con soluciones desarrolladas. Se ofrece como lectura complementaria de [*Análisis real para matemáticos*](../libros/para-matematicos/analisis-para-matematicos.md), cuyo capítulo inicial ya construye los reales y demuestra su unicidad.

[**Leer o descargar el libro completo en PDF**](../assets/books/cdr/la-construccion-de-los-reales-estudio.pdf){.btn .btn-primary}

[Consultar la ficha y la guía de lectura de la monografía](../libros/otros/la-construccion-de-los-reales.md).

## La especificación y el objeto que la cumple

Un cuerpo ordenado completo permite operar con las leyes de un cuerpo, comparar sus elementos mediante un orden compatible y obtener el supremo de cada subconjunto no vacío y acotado superiormente. Esa descripción fija lo que buscamos. Para demostrar existencia, todavía debemos proporcionar un objeto y verificar las tres exigencias.

Los racionales ofrecen la aritmética y el orden. El obstáculo aparece al considerar, por ejemplo, $S=\{q\in\mathbb Q:q\ge0,\ q^2<2\}$. El conjunto tiene elementos y cotas superiores racionales, pero carece de supremo en $\mathbb Q$. Podemos demostrarlo trabajando exclusivamente con racionales: ningún racional tiene cuadrado igual a dos; si un candidato positivo tiene cuadrado menor que dos, lo podemos superar dentro de $S$; si tiene cuadrado mayor, podemos reducirlo conservando una cota superior.

Esta prueba localiza la insuficiencia antes de introducir $\sqrt2$ como número real. Así evita usar como premisa el objeto que la construcción pretende justificar.

Una cortadura de Dedekind codifica una posición mediante su lado racional izquierdo. Es un subconjunto no vacío y propio de $\mathbb Q$, cerrado hacia abajo y sin máximo. La colección de todas esas cortaduras será el nuevo dominio. El orden surge de la inclusión; el racional $r$ queda representado por $C_r=\{q\in\mathbb Q:q<r\}$.

Ahora comienza el trabajo algebraico. Hay que definir suma, opuesto, producto e inverso, comprobar que producen cortaduras y demostrar sus leyes. Sólo después tendremos un cuerpo ordenado. Finalmente, la unión de una familia no vacía de cortaduras acotada superiormente proporciona su supremo y cierra la prueba de existencia.

## Dos caminos para demostrar la unicidad

Sean $F$ y $G$ dos cuerpos ordenados completos. Cada uno contiene una copia canónica de los racionales. Escribamos $q_F$ y $q_G$ para distinguir sus imágenes.

La candidata a identificar ambos cuerpos es

$$
\varphi(x)=\sup_G\{q_G:q\in\mathbb Q,\ q_F<x\}.
$$

Antes de usar la fórmula debemos verificar que el conjunto es no vacío y está acotado en $G$. Después debemos demostrar que la aplicación conserva orden, suma, producto y unidad, y que es biyectiva. La unicidad exige además probar que cualquier otro isomorfismo ordenado coincide con ella.

ANM y CDR utilizan esta candidata, pero organizan de manera distinta las verificaciones.

En el [capítulo 0 de ANM](../libros/capitulos/analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md), el hilo conductor es la **traza racional** $A_x=\{q\in\mathbb Q:q_F<x\}$. Primero se demuestra que esa información determina al elemento. Después se comprueba que el transporte conserva las trazas. La construcción simétrica produce la inversa; las caracterizaciones racionales de suma y producto permiten demostrar que también se conserva la aritmética.

CDR desarrolla una ruta mediante **operaciones con conjuntos y supremos**. Para la suma, relaciona el corte de una suma con las sumas de sus cortes y demuestra el correspondiente resultado sobre supremos. Para el producto, trabaja primero con partes positivas, controla los supremos anidados y compara productos exactos con racionales estrictamente inferiores a esos productos. El cero y los demás signos se incorporan después.

La diferencia es instructiva. En una ruta seguimos la información racional que caracteriza cada elemento. En la otra seguimos cómo se transforman conjuntos y cómo sus supremos responden a esas operaciones. Compararlas obliga a reconocer qué lema autoriza cada paso, aunque la fórmula inicial y la conclusión sean las mismas.

## Dos maneras de definir operaciones sobre cortaduras

También podemos comparar las operaciones de la construcción por cortaduras. Una definición de suma toma los valores exactos $a+b$, con $a\in A$ y $b\in B$. Otra toma todos los racionales estrictamente inferiores a alguna de esas sumas. Ambas dan el mismo conjunto, pero la equivalencia debe probarse.

Si $q<a+b$, el racional $a'=q-b$ satisface $a'<a$, pertenece a $A$ por descenso y cumple $q=a'+b$. En la otra dirección, si $q=a+b$, la ausencia de máximo proporciona $a'>a$ en $A$; entonces $q<a'+b$. Estas dos observaciones justifican la igualdad de las definiciones.

Los apéndices de CDR estudian otra variante: definir operaciones mediante **recintos racionales**, usando extremos inferiores y superiores para controlar sus resultados. El problema adicional consiste en justificar que los recintos pueden estrecharse cuanto sea necesario y que los controles racionales permiten transferir las identidades algebraicas.

El teorema que compara la construcción por recintos con la construcción por testigos aparece después de completar ambas. Ese orden es esencial: la comparación no puede suplir las verificaciones de las que depende.

## Cómo leer el libro junto con ANM

| Objetivo | Lectura sugerida |
|---|---|
| Construir los reales por primera vez | Capítulo 0 de ANM; después, capítulos I–II de CDR para contrastar la exposición. |
| Comprender otra demostración de unicidad | §0.9–§0.10 de ANM y capítulo III de CDR. |
| Comparar operaciones y controlar circularidad | Apéndices de CDR, después de estudiar la construcción principal. |
| Pasar de la estructura al control de errores | Capítulo IV de CDR y capítulos de ANM sobre distancia y sucesiones. |
| Trabajar por cuenta propia | Ejercicios al final de cada capítulo de CDR; intentar la resolución antes de leer la solución. |

CDR conserva su propio recorrido y puede estudiarse sin seguir ANM. Quien llegue desde ANM ya habrá resuelto las preguntas de existencia y unicidad; podrá dedicar la segunda lectura a las variantes, los casos delicados y las estrategias demostrativas.

El capítulo IV explica por qué la desigualdad triangular permite controlar una suma de errores. Incluye además dos ejemplos al retirar ese axioma: en uno falla la estabilidad de la suma de límites; en otro se conserva gracias a una comparación con una norma conocida. Esa distinción invita a estudiar las hipótesis por el trabajo que realizan dentro de una prueba.

## Procedencia y alcance de esta edición

El punto de partida son cuatro clases del curso *Real Analysis* de **Divergence is Divergence**:

- [The Real Number System](https://www.youtube.com/watch?v=w26JekhZEUU).
- [The Existence of Real Numbers](https://www.youtube.com/watch?v=RfAxW_UD_94).
- [The Uniqueness of Real Numbers](https://www.youtube.com/watch?v=TUGvSs7Tr-g).
- [The Triangle Inequality](https://www.youtube.com/watch?v=nv4jtXJVppE).

La monografía ofrece una elaboración editorial autónoma: desarrolla comprobaciones, corrige formulaciones y añade demostraciones, comparaciones y ejercicios. Esas intervenciones son responsabilidad de esta edición. Los resultados clásicos no se presentan como nuevos y el texto no se ofrece como transcripción literal de las grabaciones.

El PDF corresponde a la **edición de estudio M18 v05**, preparada para distribución. Continúan pendientes la revisión matemática externa y el cotejo audiovisual integral de las cuatro fuentes. Esta indicación permite estudiar y discutir el manuscrito conociendo el alcance de su revisión.

Para [comunicar una errata](https://github.com/lachenmann/matematica-abierta/issues/new), indica capítulo, sección o ejercicio, el pasaje y la corrección propuesta.

[**Abrir el libro completo**](../assets/books/cdr/la-construccion-de-los-reales-estudio.pdf) · [Volver a ANM](../libros/para-matematicos/analisis-para-matematicos.md)
