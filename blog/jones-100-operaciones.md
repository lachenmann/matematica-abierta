---
title: "¿Puede cualquier teorema demostrarse con 100 operaciones? Lo que realmente dice James P. Jones"
description: "La cota publicada por Jones, su alcance documental y el certificado reproducible de la construcción independiente S126."
content-id: MA-ART-0013
content-type: article
status: published
draft: false
date-created: 2026-10-03
date-modified: 2026-10-06
areas:
  - fundamentos
  - teoria-de-numeros
topics:
  - ecuaciones-diofanticas
  - computabilidad
  - demostrabilidad
level: avanzado
prerequisites: []
related: []
provenance:
  type: synthesis
  note: "Adaptación web de JONES_100_ARTICLE_v1.2.md; Apéndice A: S126-REPRO v1.0."
license: GFDL-1.3-or-later
toc: true
toc-depth: 2
resources:
  - ../assets/articles/ma-art-0013/S126_REPRO_v1.0.zip
format:
  html:
    include-after-body:
      - ../assets/articles/ma-art-0013/responsive.html
---

**Nota de versión — v1.2 — 6 oct 2026.** Derivada del máster canónico v1.1 mediante la actualización de los estados de OUC G2 y G3 en §14 y un bloque sobre la investigación en curso. Se conservan intactos el interludio sobre publicación, peer review y reproducibilidad, la nota posterior a RED TEAM R1 y S126-REPRO v1.0 en el Apéndice A. La atribución Pascal–Kline es provisional; la referencia a Matiyasevich 1993 conserva el alcance documental del cotejo disponible.

Cien operaciones aritméticas no son cien pasos de demostración. Este artículo distingue la cota publicada por Jones, su alcance documental y una construcción independiente cuyo certificado puede reproducirse operación por operación.

Hay afirmaciones matemáticas que parecen demasiado sorprendentes para ser ciertas. Que cualquier teorema demostrable pueda tener una prueba de apenas cien operaciones es una de ellas. ¿Cómo podría caber en tan pocos cálculos una demostración que ocupa muchas páginas o exige años de trabajo? Comprender esa afirmación requiere detenerse en qué significa aquí «probar» y qué estamos contando como una «operación».

Este artículo nació de una convicción que orienta Matemática Abierta: procurar que el lector pueda seguir el razonamiento sin que sus pasos decisivos queden ocultos. Al leer el trabajo de James P. Jones de 1980, recurrimos a un modelo de lenguaje para explicar el argumento y reconstruir sus pasos. Pero aquella tarea, inicialmente pedagógica, fue convirtiéndose en una investigación: cuanto más intentábamos hacer explícito el recorrido hasta las cien operaciones, más difícil resultaba establecer cómo se obtenía exactamente ese recuento. Encontramos antecedentes, referencias y una cota publicada, pero no una exposición que nos permitiera reproducir las cien operaciones una por una.

De esa dificultad surgieron las preguntas que guían estas páginas: ¿qué afirma realmente Jones?, ¿qué podemos reconstruir a partir de sus textos?, ¿cómo presentar una comprobación aritmética que el lector pueda verificar por sí mismo? El recorrido nos llevará de las demostraciones formales a las ecuaciones diofánticas y a una construcción explícita de 126 operaciones. Mantendremos separados el resultado publicado por Jones, nuestra reconstrucción y las cuestiones que permanecen abiertas.

## Contenido {#contenido}

1. [¿Puede cualquier teorema demostrarse con 100 operaciones?](#seccion-01)
2. [De una teoría axiomatizable a un conjunto c.e.](#seccion-02)
3. [De un conjunto c.e. a una representación diofántica](#seccion-03)
4. [Cómo se mide una ecuación diofántica: variables, grado y operaciones](#seccion-04)
5. [El antecedente de 243 operaciones](#seccion-05)
6. [El eslabón perdido de 149](#seccion-06)
7. [El teorema de las 100 operaciones](#seccion-07)
   - [7.1. Publicación, peer review y reproducibilidad](#seccion-07-1)
8. [¿Podemos construir nosotros un certificado completamente verificable?](#seccion-08)
9. [La arquitectura de S126](#seccion-09)
10. [Cómo se cuentan exactamente 126 operaciones](#seccion-10)
11. [Qué demuestra S126 y qué no demuestra](#seccion-11)
12. [Optimizar una representación universal](#seccion-12)
13. [Qué aprendimos intentando bajar de 126](#seccion-13)
14. [El problema que permanece abierto](#seccion-14)
15. [Entonces, ¿puede cualquier teorema demostrarse con 100 operaciones?](#seccion-15)
16. [Conclusión](#seccion-16)

[Apéndice A — Certificado reproducible](#apendice-a) · [Bibliografía](#bibliografia)

## 1. ¿Puede cualquier teorema demostrarse con 100 operaciones? {#seccion-01}

**«100 operaciones» no significa «100 pasos de demostración».** El resultado de James P. Jones se refiere a una forma de certificación aritmética de la demostrabilidad. Para entenderlo hay que distinguir el razonamiento formal, su codificación mediante números y la comprobación de un certificado.

Usaremos **[P]** para resultados publicados; **[R]** para nuestra reconstrucción del argumento; **[I]** para interpretaciones pedagógicas; y **[A]** para cuestiones abiertas. La etiqueta [R] no implica una afirmación de novedad.

**[P]** En el Teorema 5 de *Undecidable Diophantine Equations* (1980), Jones afirma, en paráfrasis:

> Si una proposición es demostrable en una teoría axiomatizable, admite una prueba consistente en 100 sumas y multiplicaciones de enteros. (Jones 1980, p. 862, Teorema 5).

**[R]** La expresión «otra prueba» requiere explicación. No se afirma que una deducción extensa pueda sustituirse por cien aplicaciones de las reglas de inferencia de la misma teoría. El procedimiento cambia la forma de presentar la evidencia: traduce la existencia de una demostración formal a la existencia de una solución de ciertas ecuaciones diofánticas. Una solución concreta proporciona entonces un **testigo aritmético de demostrabilidad**.

**[I]** Imaginemos que alguien entrega una colección de enteros y asegura que certifican un teorema. Para comprobar esa afirmación necesitamos dos cosas: verificar las relaciones aritméticas correspondientes y conocer la justificación matemática de que esas relaciones representan correctamente la demostrabilidad. Las operaciones numéricas constituyen la comprobación del testigo; el puente entre esa comprobación y el teorema pertenece a la construcción metamatemática.

**[P]** Jones introduce la medida $o$ como el número de sumas, restas y multiplicaciones necesarias para comprobar una solución propuesta. El enunciado del Teorema 5 habla de sumas y multiplicaciones de enteros. También señala que la deducción formal puede recuperarse efectivamente de la solución. (Jones 1980, p. 862).

**[R]** Conviene separar cuatro objetos:

| Objeto | Qué es | Qué función cumple |
|---|---|---|
| **Prueba formal** | Una derivación finita conforme a los axiomas y reglas de una teoría. | Establecer que $T\vdash\sigma$. |
| **Código de Gödel** | Un número que codifica una expresión o una derivación. | Permitir que la sintaxis se trate mediante procedimientos aritméticos. |
| **Testigo diofántico** | Una tupla de números que satisface las ecuaciones asociadas al enunciado. | Certificar la condición existencial que representa su demostrabilidad. |
| **Verificación aritmética** | La evaluación de las expresiones y la comprobación de las igualdades. | Determinar si la tupla presentada es una solución. |

El código de un enunciado no es su demostración. Tampoco debemos identificar sin más el código de una prueba con el testigo diofántico: la representación puede necesitar numerosos datos auxiliares.

**[I]** Una multiplicación de enteros cuenta como una operación en esta medida, aunque sus operandos tengan millones de cifras. Por eso, una cota sobre el número de operaciones no proporciona por sí sola una cota comparable sobre el tiempo de cálculo, la memoria necesaria o el tamaño del certificado. Tampoco incluye el trabajo de encontrar los números adecuados.

## 2. De una teoría axiomatizable a un conjunto c.e. {#seccion-02}

**[R]** Fijemos una teoría $T$ formulada en un lenguaje efectivo, con reglas de inferencia comprobables mediante un algoritmo. Aquí «axiomatizable» se entiende en sentido **efectivo**: sus axiomas pueden enumerarse algorítmicamente. Tener una descripción informal de ciertos principios no basta para obtener el resultado.

Una numeración de Gödel asigna códigos naturales a las expresiones del lenguaje. Escribiremos

$$
\ulcorner\sigma\urcorner
$$

para el código del enunciado $\sigma$, y definiremos el conjunto numérico de los teoremas de $T$ por

$$
\operatorname{Th}(T)
=
\bigl\{
\ulcorner\sigma\urcorner:
T\vdash\sigma
\bigr\}.
$$

Esta notación se refiere a **lo demostrable en $T$**. No presupone que hayamos identificado todas las verdades acerca de los objetos que la teoría pretende describir.

**[P]** Un conjunto es *computablemente enumerable*, abreviado **c.e.**, si existe un procedimiento que enumera sus elementos. La denominación histórica *recursivamente enumerable*, abreviada **r.e.**, designa la misma noción. El conjunto de teoremas de una teoría efectivamente axiomatizable es computablemente enumerable. (Schwarz, cap. 5).

**[R]** Podemos reconstruir la razón mediante una enumeración por etapas. En cada etapa hacemos avanzar el procedimiento que enumera los axiomas y examinamos una cantidad finita creciente de posibles derivaciones a partir de los axiomas ya aparecidos.

Toda prueba auténtica es finita. Utiliza un número finito de axiomas, y cada uno aparecerá en alguna etapa de la enumeración. Por tanto, llegará una etapa en la que estarán disponibles todos los axiomas empleados y se examinará aquella derivación. Su conclusión será incorporada a la lista de teoremas.

Ningún teorema queda fuera y ninguna expresión se incorpora sin una derivación válida. Así obtenemos

$$
T\text{ efectivamente axiomatizable}
\quad\Longrightarrow\quad
\operatorname{Th}(T)\text{ es c.e.}
$$

La hipótesis sobre $T$ es la que garantiza esta propiedad del conjunto entero. La afirmación particular $T\vdash\sigma$ nos dice, además, que

$$
\ulcorner\sigma\urcorner\in\operatorname{Th}(T).
$$

**[R]** Hay una sutileza cuando los axiomas son enumerables pero su pertenencia no es decidible. En ese caso, no podemos suponer que una inspección aislada resuelva siempre si una fórmula es un axioma. Podemos acompañar cada uso de un axioma con un registro finito de su aparición en la enumeración. De este modo se obtiene una relación de comprobación efectiva

$$
\operatorname{Prf}_T(p,n),
$$

donde $p$ codifica una derivación con sus justificaciones auxiliares y $n$ codifica su conclusión. Entonces

$$
n\in\operatorname{Th}(T)
\quad\Longleftrightarrow\quad
\exists p\in\mathbb N\;
\operatorname{Prf}_T(p,n).
$$

**[I]** Enumerar no equivale a decidir. Si buscamos una demostración de $\sigma$, la enumeración acabará encontrándola cuando exista. Si no existe, la búsqueda puede continuar indefinidamente. La ausencia de una prueba entre las examinadas hasta cierto momento no certifica su inexistencia.

## 3. De un conjunto c.e. a una representación diofántica {#seccion-03}

**[P]** El teorema de Davis–Putnam–Robinson–Matiyasevich, conocido como **DPRM**, establece que todo conjunto computablemente enumerable es diofántico. Con la convención $\mathbb N=\{0,1,2,\ldots\}$, esto significa que, para cada conjunto c.e. $W\subseteq\mathbb N$, existe un polinomio de coeficientes enteros

$$
P_W(n,x_1,\ldots,x_m)
$$

tal que

$$
\boxed{
n\in W
\quad\Longleftrightarrow\quad
\exists x_1,\ldots,x_m\in\mathbb N\;
P_W(n,x_1,\ldots,x_m)=0.
}
$$

El trabajo de Matiyasevich completó el resultado apoyándose en las contribuciones anteriores de Davis, Putnam y Robinson. (Matiyasevich 1971).

**[I]** Una representación diofántica transforma una condición de pertenencia en una pregunta sobre soluciones. Como ejemplo elemental, pertenecer al conjunto de cuadrados naturales equivale a satisfacer

$$
n\in\{0,1,4,9,\ldots\}
\quad\Longleftrightarrow\quad
\exists x\in\mathbb N\;(n-x^2=0).
$$

DPRM extiende esta posibilidad a cualquier conjunto c.e., incluso cuando su enumeración procede de cálculos o deducciones mucho más complejos.

**[R]** Apliquemos el teorema a $\operatorname{Th}(T)$. Obtenemos un polinomio $P_T$, fijo una vez elegidas la teoría y la codificación, para el cual

$$
\boxed{
T\vdash\sigma
\quad\Longleftrightarrow\quad
\exists\mathbf x\in\mathbb N^m\;
P_T(\ulcorner\sigma\urcorner,\mathbf x)=0.
}
$$

Esta equivalencia tiene dos direcciones igualmente necesarias. Si existe una prueba formal, debe existir una solución. Si existe una solución, el enunciado debe ser demostrable en $T$. La segunda dirección impide que aparezcan certificados de proposiciones que la teoría no demuestra.

La cadena conceptual puede escribirse ahora sin confundir sus niveles:

$$
\begin{gathered}
T\text{ efectivamente axiomatizable}
\;\Longrightarrow\;
\operatorname{Th}(T)\text{ c.e.}
\;\Longrightarrow\;
\operatorname{Th}(T)\text{ diofántico},
\\[4pt]
T\vdash\sigma
\;\Longleftrightarrow\;
\ulcorner\sigma\urcorner\in\operatorname{Th}(T)
\;\Longleftrightarrow\;
\exists\mathbf x\;
P_T(\ulcorner\sigma\urcorner,\mathbf x)=0.
\end{gathered}
$$

**[R]** No debemos leer la última igualdad como una traducción directa del contenido matemático de $\sigma$. Si $\sigma$ habla de triángulos, las variables auxiliares no tienen por qué representar lados o ángulos. La ecuación representa **su pertenencia al conjunto de teoremas de $T$**.

En una construcción efectiva podemos buscar una solución a partir de un enunciado demostrado, enumerando las tuplas hasta encontrar una que satisfaga la ecuación. Recíprocamente, una solución válida garantiza que la enumeración de pruebas terminará encontrando una demostración. Esta observación asegura una recuperación efectiva por búsqueda; no asegura rapidez ni identifica la prueba recuperada con una determinada prueba original.

**[I]** Comprobar una tupla concreta y determinar si existe alguna tupla son tareas distintas. La primera consiste en efectuar cálculos finitos. La segunda exige afrontar una búsqueda sin límite previo de tamaño.

**[R]** Es en la primera tarea donde entra la medida de operaciones. Incluso para una expresión elemental, la escritura influye en el cálculo. Evaluar

$$
a^2+2ab+b^2
$$

mediante sus términos separados requiere más operaciones que calcular primero $a+b$ y luego multiplicar el resultado por sí mismo. La identidad

$$
a^2+2ab+b^2=(a+b)^2
$$

permite una evaluación con una suma y una multiplicación.

Por ello, al introducir un presupuesto de operaciones hay que especificar las expresiones que se evalúan, el orden de cálculo y los resultados intermedios que se reutilizan. La existencia de una representación diofántica, por sí sola, no fija ese presupuesto. DPRM proporciona el puente entre enumerabilidad y ecuaciones; obtener una cota uniforme pequeña exige una construcción cuantitativa adicional.

## 4. Cómo se mide una ecuación diofántica: variables, grado y operaciones {#seccion-04}

**[P]** En los trabajos de Jones aparecen tres medidas diferentes de complejidad:

$$
v=\text{número de incógnitas},\qquad
\delta=\text{grado},\qquad
o=\text{número de operaciones aritméticas}.
$$

Cada una describe un aspecto de la representación. Para distinguirlas, consideremos una ecuación universal escrita esquemáticamente como

$$
U(n,x,z_1,\ldots,z_v)=0.
$$

El parámetro $n$ selecciona un conjunto computablemente enumerable; $x$ es el número cuya pertenencia se quiere representar; las incógnitas $z_1,\ldots,z_v$ constituyen el testigo existencial. En la convención expuesta por Jones, los parámetros se tratan como coeficientes al calcular el grado respecto de las incógnitas: no se suman a $v$ ni contribuyen a ese grado. Esta distinción aparece explícitamente en Jones 1978, p. 337.

| Medida | Qué cuenta | Qué deja sin determinar |
|---|---|---|
| $v$ | Las incógnitas existenciales de la representación. | El tamaño de sus valores y la dificultad de encontrarlos. |
| $\delta$ | El grado total respecto de las incógnitas; para un sistema, el máximo de los grados de sus ecuaciones. | El número de operaciones de una evaluación concreta. |
| $o$ | Las operaciones aritméticas necesarias para comprobar una solución propuesta. | El tamaño de los operandos y el coste de buscar la solución. |

**[P]** Jones define $o$ en 1980, p. 862, mediante el **número total de sumas, restas y multiplicaciones necesarias para evaluar o determinar la corrección de una solución propuesta**. En 1978 y 1982 explica, además, que considera la resta como una forma de suma con signo.

**[R]** Esta es la convención histórica que debemos conservar. No incluye la división, la extracción de raíces o la exponenciación como operaciones elementales independientes. Una potencia escrita de manera compacta exige explicar cómo se evalúa mediante las operaciones admitidas. Tampoco se debe trasladar automáticamente al coste $o$ la convención que trata los parámetros como coeficientes para calcular $\delta$: excluirlos del grado no equivale a declarar gratuitos todos los cálculos entre ellos.

**[I]** Las tres medidas pueden variar en direcciones opuestas. Por ejemplo, la condición

$$
y=x^8
$$

puede sustituirse por

$$
u=x^2,\qquad v=u^2,\qquad y=v^2.
$$

El grado máximo desciende de ocho a dos, pero aparecen dos incógnitas adicionales. Las tres multiplicaciones sucesivas también permiten evaluar $x^8$ directamente, de modo que la reducción de grado no implica por sí sola una reducción del trabajo aritmético.

**[P]** Jones estudia precisamente estos intercambios entre grado e incógnitas. Sus tablas de pares universales $(v,\delta)$ registran posibilidades simultáneas de representación, no una clasificación por número de operaciones.

**[R]** También importa distinguir un sistema de ecuaciones de la ecuación única obtenida al combinarlo. Aunque ambos expresen la misma condición existencial, pueden tener grados y costes operacionales diferentes. El antecedente de 1978 permite comprobarlo con cifras publicadas.

## 5. El antecedente de 243 operaciones {#seccion-05}

**[P]** En *Three Universal Representations of Recursively Enumerable Sets* (1978), el Teorema 3 presenta explícitamente el sistema numerado **(1.3)**. Para enteros positivos $x,n$, su propiedad es

$$
x\in W_n
\quad\Longleftrightarrow\quad
\text{el sistema (1.3) tiene una solución en enteros no negativos}.
$$

Aquí $(W_n)$ es una enumeración efectiva de los conjuntos recursivamente enumerables de enteros positivos. Al variar $n$, el mismo sistema representa cualquiera de esos conjuntos.

El sistema consta de **36 ecuaciones y 67 incógnitas**, sin contar los parámetros $n,x$; el grado máximo de sus ecuaciones es **38**. Jones lo imprime en p. 337 y describe estas características en p. 338. En esta última página le atribuye un coste de **243 operaciones**, contando la resta como suma con signo.

**[R]** Lo que se verifica es una solución propuesta del sistema completo. Se fijan $n,x$, se proporcionan valores para las 67 incógnitas y se evalúan las expresiones de las 36 igualdades. La cifra 243 corresponde a esa comprobación aritmética; no cuenta 243 intentos de búsqueda, 243 incógnitas ni 243 inferencias formales.

La construcción publicada permite seguir mucho más que el enunciado final. Su organización puede reconstruirse así:

| Tramo de Jones 1978 | Función en la construcción |
|---|---|
| §3, lemas 3.1–3.2, pp. 345–346 | Enumerar los conjuntos diofánticos y codificar secuencias finitas de valores que respetan sumas y productos. |
| Lema 3.4, pp. 347–348 | Expresar la pertenencia mediante condiciones iniciales y una condición universal acotada. |
| Lema 3.5, p. 348, apoyado en el lema 2.3 | Aplicar la eliminación del cuantificador acotado mediante condiciones aritméticas auxiliares. |
| Lemas de §2 y ensamblaje de p. 349 | Convertir las condiciones auxiliares en ecuaciones polinómicas y especificar sustituciones, eliminaciones y cambios de letras. |
| Teorema 3, sistema (1.3), pp. 337–338 | Presentar el sistema universal resultante y declarar su coste operacional. |

**[P]** La fuente documenta incluso decisiones locales de economía. En p. 345 Jones explica que el lema 2.10 permite una formulación con menos operaciones que el lema 2.9: introduce una expresión para combinar condiciones, elimina variables por sustitución y obtiene las relaciones $Q_1$–$Q_4$. En la aplicación puede omitir una de ellas porque otra condición ya la garantiza. El ensamblaje de p. 349 explica cómo esas piezas desembocan en (1.3).

**[R]** Por eso el estado documental de 243 es sólido: disponemos del sistema, de la construcción que lo justifica y del total que Jones le asigna. Su reconstrucción tiene un objeto explícito sobre el cual trabajar. Esto debe distinguirse de afirmar que una tabla moderna de operaciones, registro por registro, estuviera impresa en el artículo.

Una comprobación especialmente clara aparece al pasar del sistema a una sola ecuación.

**[P]** Jones señala que, al trasladar los términos y sumar los cuadrados de los 36 residuos, se obtiene una ecuación universal de grado 76. Su coste pasa de 243 a **350 operaciones**.

**[R]** Si las ecuaciones se escriben como $E_i=F_i$, la combinación es

$$
\sum_{i=1}^{36}(E_i-F_i)^2=0.
$$

La diferencia entre ambos totales se reconstruye exactamente:

$$
\underbrace{243}_{\text{evaluación del sistema}}
+
\underbrace{36}_{\text{restas}}
+
\underbrace{36}_{\text{cuadrados}}
+
\underbrace{35}_{\text{sumas}}
=
350.
$$

Este cálculo explica el incremento publicado; no sustituye el recuento completo del sistema inicial. También muestra por qué no debemos atribuir indistintamente el coste 243 al sistema y a su ecuación combinada.

**[P]** El antecedente es directo también en su interpretación lógica. El Corolario 1 de 1978 formula, con 243 operaciones, la misma clase de afirmación sobre demostraciones que reaparecerá con 100. Jones 1980 remite expresamente a ese resultado anterior.

## 6. El eslabón perdido de 149 {#seccion-06}

**[P]** Inmediatamente después del Corolario 1, en p. 338 del artículo de 1978, Jones escribe:

> “In a future paper we will show that this number, 243, may be further reduced, to 149.”

El pasaje promete mostrar en un trabajo futuro una reducción del coste que acaba de presentar. Su alcance documental es preciso:

$$
\boxed{243\to149\text{ está anunciado, no reconstruido.}}
$$

**[R]** Hay tres situaciones que conviene separar:

| Situación | Evidencia necesaria | Estado del escalón 149 |
|---|---|---|
| **Existencia anunciada de una reducción** | Una afirmación del autor que comunique la mejora. | Documentada en Jones 1978, p. 338. |
| **Publicación de una construcción** | Las ecuaciones, transformaciones y justificación correspondientes. | No localizada en el expediente auditado. |
| **Reconstrucción moderna** | Una construcción identificada y un recuento reproducible que recuperen ese escalón. | No obtenida. |

La frase publicada acredita el anuncio. No proporciona las ecuaciones de la mejora, no identifica las operaciones eliminadas y no permite reconstruir por sí misma el coste 149.

**[R]** La conclusión de la auditoría es, por tanto:

> El escalón $o=149$ sólo ha sido localizado como anuncio en Jones 1978; no se ha encontrado una construcción publicada que documente $243\to149$.

**[A]** Permanece sin resolver documentalmente qué construcción tenía Jones en mente y si dejó una exposición de ella en alguna fuente no localizada. Esta laguna no autoriza a afirmar que la construcción nunca existió o que nunca se publicó.

**[R]** Tampoco permite convertir 149 en una etapa demostrada del camino hacia 100. La sucesión cronológica de cifras y la genealogía matemática de las transformaciones son cosas distintas: las fuentes pueden acreditar la primera sin permitir reconstruir la segunda.

## 7. El teorema de las 100 operaciones {#seccion-07}

**[P]** En *Undecidable Diophantine Equations* (1980), p. 862, Jones afirma que las ecuaciones del Teorema 3, modificadas para prescindir de la relación

$$
q=b^{5^{60}},
$$

permiten alcanzar

$$
o_{\rm Jones}=100.
$$

La modificación es parte de la afirmación. El pasaje no atribuye sin más ese coste a las ecuaciones tal como aparecen impresas, incluida la enorme potencia.

A continuación, Jones presenta su **Teorema 5**: para cualquier teoría axiomatizable $T$ y cualquier proposición demostrable en ella, existe otra prueba consistente en 100 sumas y multiplicaciones de enteros.

**[R]** La inferencia que sostiene esta formulación puede explicitarse usando las distinciones de las secciones anteriores. Fijadas una axiomatización efectiva y una numeración de Gödel:

$$
\text{teoremas de }T
\longrightarrow
\operatorname{Th}(T)\text{ r.e.}
\longrightarrow
\text{representación universal especializada}
\longrightarrow
\text{certificado aritmético}.
$$

La especialización fija los parámetros que seleccionan el conjunto de teoremas de $T$. Para cada enunciado $\sigma$, su código constituye la entrada cuya pertenencia se comprueba. Si $T\vdash\sigma$, existe una tupla que satisface las ecuaciones; según la cota publicada por Jones, la comprobación aritmética correspondiente admite el presupuesto de 100 operaciones.

En este argumento, «ecuación universal» designa el mecanismo de representación. El presupuesto debe atribuirse a la formulación concreta que se evalúa: combinar un sistema en una sola ecuación puede añadir operaciones, como ya mostró el caso de 1978.

**[I]** La uniformidad de la cifra es lo sorprendente. El número de operaciones del comprobador permanece acotado, mientras los enteros suministrados pueden contener cantidades de información cada vez mayores. El resultado no proporciona un procedimiento de cien pasos para descubrir cualquier demostración.

**[R]** El límite documental aparece al pedir la reproducción exacta del presupuesto. El artículo de 1980 **publica la cota**, pero no proporciona una lista operacional del sistema modificado que permita seguir cien operaciones identificadas y comprobar su total. Para reproducirla con ese nivel de detalle necesitaríamos conocer las ecuaciones definitivas, las sustituciones empleadas y la organización de su evaluación.

**[P]** Jones reitera el resultado en *Universal Diophantine Equation* (1982), p. 553. Vuelve a vincular $o_{\rm Jones}=100$ con la modificación del Teorema 3, repite el Teorema 5 y compara expresamente el nuevo valor con las 243 operaciones de su artículo anterior.

**[R]** El trabajo de 1982 desarrolla extensamente la construcción matemática y proporciona mecanismos relevantes para eliminar potencias. Sin embargo, el expediente auditado no identifica allí una especificación completa acompañada del recuento histórico de 100. En particular, no basta con encontrar un sistema destinado a mejorar el grado y el número de incógnitas para atribuirle también ese coste operacional.

Los trabajos relacionados —Matiyasevich–Robinson 1975, Jones 1979 y Jones–Matiyasevich 1982a, 1982b— aportan técnicas de representación, combinación de relaciones y tratamiento de condiciones exponenciales o binomiales. Su pertinencia matemática no los convierte en documentos de una transición $243\to149\to100$.

**[P]** La interpretación sobre las demostraciones recibió una crítica contemporánea de William S. Hatcher y Bernard R. Hodgson en *Complexity Bounds on Proofs* (1981). Su objeto explícito es el **Corolario 1 de Jones 1978**, relativo a 243 operaciones. Los autores distinguen la prueba formal dentro de una teoría de la comprobación metamatemática de un certificado y aclaran que no cuestionan la construcción de las representaciones diofánticas universales.

Su advertencia tiene dos componentes. Primero, un número acotado de sumas y multiplicaciones no controla el tamaño de los enteros: la complejidad computacional puede crecer con sus cifras. Segundo, una verificación completa de la relación entre el enunciado y su código debe considerar también el trabajo de codificación y comprobación de esa correspondencia (pp. 255–257).

**[R]** Hatcher–Hodgson documenta, así, la recepción crítica de la interpretación lógica del antecedente de 243. No constituye una reconstrucción ni una refutación del circuito de 100. Su análisis explica por qué el alcance de ambas cifras debe expresarse como una cota de operaciones aritméticas del certificado, sin convertirla en una cota ordinaria del coste total de demostrar.

La secuencia final recoge **estados documentales**; sus flechas no representan transformaciones matemáticas íntegramente recuperadas:

$$
\boxed{
243\ {\rm documentado}
\;\longrightarrow\;
149\ {\rm anunciado}
\;\longrightarrow\;
100\ {\rm publicado}.
}
$$

**[R]** $o_{\rm Jones}=100$: resultado publicado y recibido posteriormente, pero construcción histórica no reproducible con la documentación localizada. El escalón $o=149$ sólo ha sido localizado como anuncio en Jones 1978; no se ha encontrado una construcción publicada que documente $243\to149\to100$.

### 7.1. Publicación, peer review y reproducibilidad {#seccion-07-1}

**[I]** La publicación de un resultado, su evaluación por pares y la posibilidad de reproducir su demostración son aspectos relacionados, pero no equivalentes:

$$
\boxed{\text{publicado}\neq\text{independientemente verificado}},
\qquad
\boxed{\text{recepción posterior}\neq\text{reproducción de la demostración}}.
$$

El peer review puede evaluar los argumentos, sus hipótesis y el uso de resultados previos sin reproducir cada cálculo o reconstruir un circuito completo. Una publicación breve puede comunicar un resultado y las ideas que lo sustentan sin imprimir toda su derivación. Esto limita lo que un lector posterior puede verificar a partir del texto; no implica por sí solo que el resultado sea falso. No sabemos qué material adicional, si alguno, tuvo el referee de Jones: no inferimos nada sobre ello ni sobre su actuación.

**[P/R]** Un ejemplo de recepción posterior es *Hilbert’s Tenth Problem* de Matiyasevich (1993), p. 163: sigue atribuyendo a Jones la cota universal de 100 operaciones, pero ese pasaje no reconstruye el circuito ni desglosa su presupuesto. El expediente S1-02 localizó la atribución en una vista OCR; el testimonio de Friedman (1998), que remite al libro y a Jones 1982, también la documenta. El cotejo visual de la página del libro sigue pendiente. Esta evidencia acredita la transmisión del resultado con ese alcance documental; no proporciona una verificación independiente de las cien operaciones. ([Friedman 1998](https://fomarchive.ugent.be/1998-March/001726.html); `JONES100_SOURCE_HUNT_S1_02_MISSING_SOURCES.md`, §3).

**[I]** La filosofía de trabajo puede expresarse mediante una **paráfrasis provisional atribuida a Pascal a través de Morris Kline**: cuando citemos autores, citaremos sus demostraciones, no sus nombres. La fuente exacta y su formulación no están verificadas aquí; por eso no se presenta como cita literal ni se añade una referencia bibliográfica a Pascal o Kline. Adoptamos la idea como criterio de trabajo: identificar qué se demuestra, bajo qué hipótesis y mediante qué objeto verificable. El mismo criterio se aplica a los resultados del proyecto. La recepción histórica de 100 y el certificado reproducible de S126 responden a preguntas distintas y deben evaluarse mediante sus respectivas evidencias.

**Nota de estado posterior a RED TEAM R1.** **[R]** Las versiones impresas auditadas del Teorema 3 presentan una inconsistencia global de la conjunción; designamos ese objeto como $J_{\rm print}$. El proyecto ha derivado una reparación matemática, $J_{\rm repair}$, cuya forma completa no está documentada históricamente en las fuentes localizadas. La derivación propia no se atribuye a Jones ni se confunde con una errata histórica documentada.

En $J_{\rm repair}$, la selección Pell reparada es segura bajo las cotas explícitas del expediente, y la eliminación local de la potencia es semánticamente viable. Estas conclusiones no identifican el objeto histórico modificado que Jones contó como 100 ni establecen su recuento. Se mantienen separados $J_{\rm print}$, $J_{\rm repair}$, el objeto histórico de cien operaciones todavía no identificado y S126, construcción independiente con certificado de 126 operaciones bajo la convención del proyecto.

**R1 no refuta $o=100$.** Su conclusión sobre el sistema impreso no se transfiere al objeto histórico modificado que sustenta la cota anunciada. Tampoco permite inferir mala praxis de Jones o de sus evaluadores. El problema pendiente sigue siendo documental y matemático: identificar ese objeto y reproducir su demostración y su presupuesto.

## 8. ¿Podemos construir nosotros un certificado completamente verificable? {#seccion-08}

**[R]** Jones publica una cota de cien operaciones, pero las fuentes localizadas no nos permiten reconstruir el circuito histórico correspondiente. Esta dificultad documental motivó una pregunta distinta:

$$
\boxed{
\begin{gathered}
\text{¿Podemos construir de manera independiente una representación universal}\\
\text{cuyo circuito pueda auditarse operación por operación?}
\end{gathered}
}
$$

La construcción **S126** responde a esta pregunta. Consta de **25 ecuaciones y 37 incógnitas estrictamente positivas**, acompañadas de una prueba de la relación representada y de un circuito explícito de evaluación.

S126 **no es la construcción de Jones, no refuta el resultado de cien operaciones y no mejora su cota publicada**. Su interés es la reproducibilidad: permite identificar las hipótesis, seguir las dependencias matemáticas y examinar cada operación del comprobador.

**[R]** La independencia tiene aquí un alcance preciso. Utilizamos resultados publicados sobre representaciones diofánticas y técnicas desarrolladas por Jones y otros autores. Lo propio es la reconstrucción explícita y su organización certificada. No atribuimos a Jones nuestras transformaciones ni presentamos el sistema como una afirmación de novedad o prioridad.

**[I]** La reproducibilidad exige dos comprobaciones diferentes. Una consiste en demostrar que las ecuaciones representan correctamente la pertenencia al conjunto elegido. La otra consiste en verificar que el circuito evalúa esas ecuaciones con el presupuesto declarado. Contar correctamente las operaciones no basta si las ecuaciones representan una condición equivocada; demostrar la equivalencia lógica tampoco determina automáticamente el coste de evaluarlas.

## 9. La arquitectura de S126 {#seccion-09}

**[R]** Antes de escribir las ecuaciones completas, conviene distinguir cinco funciones que se entrelazan dentro del sistema.

| Bloque funcional | Papel en la construcción |
|---|---|
| **Codificación universal** | Incorporar una representación polinómica del conjunto $W$ mediante parámetros que codifican sus coeficientes y las posiciones de los datos. |
| **Selección exponencial** | Certificar $q=b^{5^{60}}$ mediante relaciones polinómicas y las cotas disponibles. |
| **Recurrencias y Pell** | Identificar términos de sucesiones y sostener las condiciones sobre potencias, selección de términos y divisibilidad binomial. |
| **Ventanas y cotas** | Restringir los testigos a intervalos que permiten interpretar los códigos sin soluciones espurias. |
| **Codificación final de pertenencia** | Hacer que las condiciones aritméticas sobre esos códigos equivalgan a la anulación del polinomio fuente. |

Son bloques funcionales, no cinco verificadores independientes. Comparten expresiones y, sobre todo, dependen de hipótesis que se justifican dentro del sistema completo.

**[R]** La codificación utiliza expansiones posicionales: ciertos números almacenan coeficientes; otros delimitan las posiciones donde pueden aparecer los valores buscados. Las condiciones sobre acarreos permiten relacionar la aritmética de esos grandes enteros con la información que contienen.

El circuito no dispone de una instrucción gratuita para extraer dígitos o detectar acarreos. Estas propiedades se certifican mediante ecuaciones polinómicas, utilizando la conexión con la divisibilidad de coeficientes binomiales.

El bloque de Pell contiene relaciones como

$$
d^2=(A^2-1)c^2+1.
$$

Una igualdad de este tipo restringe sus soluciones a una estructura aritmética especial. Para seleccionar los términos adecuados de las sucesiones asociadas se necesitan, además, las otras condiciones del bloque. El selector exponencial aprovecha esa infraestructura para certificar la relación entre $b$ y $q$.

**[I]** El verificador recibe números propuestos y comprueba sus relaciones. No recorre uno por uno todos los términos de las sucesiones que esos números representan.

**[R]** Las ventanas y cotas de la versión final son esenciales. La ventana lineal incorporada en C2 es

$$
c=ksn^2+\zeta,\qquad
k=\zeta+\eta,\qquad
\zeta,\eta>0.
$$

Estas igualdades implican

$$
sn^2<\frac{c}{k}<sn^2+1.
$$

La división sirve aquí para explicar la consecuencia matemática: no es una operación ejecutada por el circuito. La suficiencia de esta ventana se demuestra dentro del sistema, no como una equivalencia aislada con la ventana anterior.

Las cotas finales de C3 se expresan mediante holguras positivas:

$$
b=xy+\alpha,\qquad
e+\varepsilon_e=q^2,\qquad
\ell+\varepsilon_\ell=q^2,\qquad
g+\varepsilon_g=q.
$$

Así se obtienen

$$
b>xy,\qquad e,\ell<q^2,\qquad g<q.
$$

Estas restricciones participan en la recuperación de las expansiones y en el control de los acarreos. La prueba certifica su funcionamiento conjunto con las restantes ecuaciones.

**[R]** El enunciado lógico requiere precisar los parámetros admisibles. Sea $W\subseteq\mathbb Z_{>0}$ computablemente enumerable. La representación fuente utilizada por el certificado proporciona un polinomio entero

$$
P(x,\xi_1,\ldots,\xi_{58}),
$$

de grado total a lo sumo cuatro, tal que

$$
x\in W
\iff
\exists\boldsymbol\xi\in\mathbb Z_{\ge0}^{58}\;
P(x,\boldsymbol\xi)=0,
$$

con la normalización

$$
P(x,0,\ldots,0)\ne0
\qquad(x>0).
$$

Escribamos $\xi_0=x$ y

$$
P=\sum_{|\boldsymbol i|\le4}
p_{\boldsymbol i}\prod_{j=0}^{58}\xi_j^{i_j},
\qquad
P_{\boldsymbol i}
=(4-|\boldsymbol i|)!
\left(\prod_{j=0}^{58}i_j!\right)p_{\boldsymbol i}.
$$

Tomamos $K=5^{59}$, elegimos una potencia de dos

$$
z>1+\max_{\boldsymbol i}|P_{\boldsymbol i}|,
$$

y compilamos

$$
u=\sum_{j=1}^{58}(2z)^{5^j},
$$

$$
y=\sum_{|\boldsymbol i|\le4}
(z+P_{\boldsymbol i})
(2z)^{K-\sum_{j=0}^{58}i_j5^j}.
$$

Los exponentes son no negativos. Las ternas $(z,u,y)$ obtenidas de este modo son las **ternas admisibles** consideradas en el certificado.

**[R]** Para cada representación fuente y cada terna así compilada, S126 certifica:

$$
\boxed{
\forall x\in\mathbb Z_{>0},\qquad
x\in W
\iff
\exists\boldsymbol v\in\mathbb Z_{>0}^{37}\;
S126(x,\boldsymbol v;z,u,y).
}
$$

El predicado $S126$ es la conjunción de sus 25 igualdades. Los parámetros $(z,u,y)$ dependen de la representación de $W$, no de la entrada particular $x$.

La dirección de **corrección** establece que toda solución positiva determina $x\in W$. La dirección de **completitud** establece que, cuando $x\in W$, pueden construirse los 37 testigos positivos requeridos.

**[R]** Los 58 testigos no negativos del polinomio fuente no son las 37 incógnitas positivas del sistema final. Tampoco se extiende el enunciado a ternas arbitrarias, a $x=0$ o a soluciones con testigos racionales, reales o enteros de signo libre.

## 10. Cómo se cuentan exactamente 126 operaciones {#seccion-10}

**[R]** El presupuesto corresponde a un circuito aritmético con registros reutilizables. La convención del proyecto fija lo siguiente:

- La entrada, los parámetros admisibles y los testigos ya propuestos están disponibles sin coste de introducción.
- Las constantes literales están disponibles, incluido $E=5^{60}$.
- Cada operación binaria $+,-,\times$ cuesta una unidad; elevar al cuadrado es un producto y multiplicar por una constante también cuesta una operación.
- Los resultados intermedios pueden reutilizarse sin repetir su cálculo.
- Los registros intermedios pueden tener signo, aunque los testigos existenciales sean positivos.
- Las comparaciones de igualdad, la búsqueda del testigo, la compilación previa de parámetros y el tamaño binario de los enteros no forman parte del presupuesto.
- No se incluye transformar las 25 ecuaciones en una sola suma de cuadrados.

La disponibilidad de $E$ como constante no convierte $b^E$ en una operación gratuita. Su relación con $q$ se certifica mediante el selector, cuyas operaciones sí se cuentan.

**[R]** El desglose certificado es:

| Operación | Cantidad |
|---|---:|
| Suma $+$ | 42 |
| Resta $-$ | 16 |
| Producto $\times$ | 68 |
| **Total** | **126** |

El circuito forma un **grafo dirigido acíclico**, o DAG. Cada registro se calcula a partir de entradas o de registros anteriores, y un mismo resultado puede alimentar varias expresiones. Las 25 comparaciones se realizan sobre los valores obtenidos.

Por ello, sumar el coste de cada ecuación evaluada por separado sobrecontaría algunas operaciones compartidas.

**[R]** Un primer ejemplo aparece en los registros

$$
t_4=q\cdot q,\qquad
t_5=t_4\cdot q,\qquad
t_6=t_4\cdot t_4.
$$

Tres productos proporcionan $q^2,q^3,q^4$. El registro $t_4$ también se utiliza en las comparaciones

$$
e+\varepsilon_e=t_4,\qquad
\ell+\varepsilon_\ell=t_4,
$$

y en otras expresiones de la codificación. Las sumas de estas igualdades se pagan; el cuadrado $q^2$ no vuelve a calcularse.

Otro ejemplo conecta el bloque de Pell con el selector:

$$
t_{96}=A\cdot A,\qquad
t_{97}=t_{96}-1.
$$

El valor $A^2-1$ cuesta un producto y una resta. Después se reutiliza en varias condiciones, entre ellas

$$
d^2=(A^2-1)c^2+1,
\qquad
D_1^2=(A^2-1)C_1^2+1.
$$

Cada producto y suma posterior conserva su coste. Lo compartido es únicamente el cálculo ya realizado.

**[I]** Compartir un registro no equivale a suprimir una condición lógica. Dos ecuaciones pueden usar el mismo valor y seguir siendo ambas necesarias.

**[R]** El circuito íntegro, con sus 126 instrucciones y 25 comparaciones, corresponde al apéndice reproducible. La auditoría aritmética comprueba operadores, dependencias y salidas; la equivalencia con $x\in W$ requiere además el certificado lógico.

[Consultar el certificado reproducible completo — Apéndice A](#apendice-a).

## 11. Qué demuestra S126 y qué no demuestra {#seccion-11}

**[R] Lo que S126 sí establece.** Existe una construcción universal explícita cuyo certificado aritmético puede comprobarse con **126 operaciones**, bajo la convención operacional fijada y las condiciones de admisibilidad del teorema.

El respaldo consta de una prueba escrita de la equivalencia bidireccional y de una especificación auditable del circuito. La prueba lógica no está formalizada en un asistente de pruebas; el verificador simbólico del DAG no debe confundirse con una formalización completa de aquella.

Para hablar de un mínimo, escribiremos $\mathcal O_{\rm univ}^{(\mathcal C)}$, donde $\mathcal C$ es una convención operacional previamente fijada. En la convención del proyecto se cuentan operaciones binarias $+,-,\times$, con constantes disponibles y reutilización de registros; las comparaciones, la búsqueda, la compilación de parámetros y el coste binario quedan excluidos, como precisa §10. La convención histórica de Jones se mantiene separada.

**[R] Lo que S126 no establece.** El coste de esta construcción no demuestra

$$
\mathcal O_{\rm univ}^{(\mathcal C)}=126,
$$

ni

$$
\mathcal O_{\rm univ}^{(\mathcal C)}>100.
$$

No demuestra que Jones contara incorrectamente y no proporciona una cota inferior para otras representaciones. Construir un circuito de determinado tamaño establece una posibilidad; no excluye circuitos menores.

El estado debe conservar tres afirmaciones separadas: **[P]** Jones publica 100; **[R]** nuestro sistema explícito tiene coste 126; **[A]** el óptimo universal permanece sin determinar:

$$
\boxed{
o_{\rm Jones}=100,\qquad
o_{\rm proj}(S126)=126,\qquad
\mathcal O_{\rm univ}^{(\mathcal C)}\text{ óptimo}=?
}
$$

**[R]** La comparación entre 100 y 126 es informativa, pero no debe sobreinterpretarse mientras el circuito histórico no pueda auditarse bajo exactamente la misma convención. Deben contrastarse la reutilización de resultados frente al conteo de apariciones de una expresión; el tratamiento de constantes y cálculos entre parámetros; la evaluación de potencias; las operaciones necesarias para formar residuos antes de comparar; y la elección entre verificar un sistema o su combinación en una sola ecuación. Son posibles fuentes de diferencia que requieren documentación, no discrepancias ya demostradas entre ambos recuentos.

**[A]** No disponemos de una correspondencia operación por operación que explique la distancia entre las cifras. La igualdad $126-100=26$ no identifica veintiséis operaciones que Jones eliminara de nuestra construcción.

**[I]** La reproducibilidad de S126 consiste en que su presupuesto puede examinarse sin completar decisiones implícitas: están especificados los datos propuestos, los cálculos, las comparaciones y las condiciones bajo las cuales una solución certifica pertenencia.

[Consultar el certificado reproducible completo — Apéndice A](#apendice-a).

## 12. Optimizar una representación universal {#seccion-12}

**[R]** Reducir el número de operaciones de una representación universal exige conservar una equivalencia: las ecuaciones deben admitir un testigo exactamente cuando la entrada pertenece al conjunto representado. Una expresión más corta puede perder alguna condición necesaria; una sustitución válida puede necesitar nuevas hipótesis cuyo coste supere el ahorro obtenido.

Por eso, la simplificación algebraica es sólo una parte del trabajo. También hay que controlar los dominios, las cotas, las dependencias entre condiciones y la construcción de testigos en ambas direcciones.

**[R]** Bajo la convención operacional del proyecto, tres principios orientaron la optimización:

$$
\begin{gathered}
\text{Introducir testigos existenciales puede ser barato;}\\
\text{comprobar las relaciones que deben satisfacer tiene coste;}\\
\text{compartir cálculos puede importar más que reducir variables o grado.}
\end{gathered}
$$

Un testigo adicional no añade por sí mismo una operación al comprobador: se recibe como un dato propuesto. Sin embargo, si no se comprueba la relación que le da significado, puede introducir soluciones espurias. La economía procede de encontrar relaciones suficientes que sean baratas de verificar.

**[I]** Proponer un número que supuestamente representa una potencia es sencillo. La dificultad consiste en certificar que realmente es esa potencia y que cumple las condiciones necesarias para utilizarla en el resto del sistema.

**[R]** El DAG permite distinguir estos costes. Sus nodos son operaciones aritméticas; sus conexiones indican qué resultados utiliza cada cálculo posterior. Una subexpresión calculada una vez puede servir a varias ecuaciones. En consecuencia, el ahorro relevante es el del circuito global, no necesariamente el de una ecuación considerada de manera aislada.

La genealogía interna muestra distintas formas de obtener ahorros verificables:

$$
146\longrightarrow142\longrightarrow141
\longrightarrow130\longrightarrow128\longrightarrow126.
$$

| Paso | Cambio certificado |
|---|---|
| $146\to142$ | Compartición de subexpresiones y reorganización del DAG. |
| $142\to141$ | Transformación algebraica de dos relaciones, preservando su equivalencia conjunta. |
| $141\to130$ | Rediseño del selector exponencial mediante las cotas disponibles. |
| $130\to128$ | Sustitución de una ventana cuadrática por una ventana lineal suficiente dentro del sistema. |
| $128\to126$ | Sustitución de una cota multiplicativa por cuatro cotas con holguras positivas. |

**[R]** Son versiones del proyecto, no etapas históricas de Jones. El último paso resulta especialmente instructivo: aumenta el número de incógnitas y ecuaciones, pero reduce el número de operaciones. Las medidas de complejidad responden a preguntas distintas.

## 13. Qué aprendimos intentando bajar de 126 {#seccion-13}

**[R]** Las exploraciones posteriores produjeron lemas y circuitos locales útiles, pero no una representación universal más económica que S126. Su interés se comprende mejor por las ideas matemáticas examinadas que por el orden de los experimentos.

**Recurrencias empaquetadas.** **[R]** Una sucesión finita puede codificarse mediante los dígitos de un solo entero. Una identidad aritmética entre códigos puede expresar entonces muchas relaciones entre términos. Si varias sucesiones comparten base, longitud y condiciones de crecimiento, parte de la infraestructura puede utilizarse conjuntamente.

En un control experimental, esta técnica redujo el coste de

$$
646\longrightarrow314.
$$

Para $m\ge1$ obligaciones con la interfaz común especificada en el certificado, se obtuvieron los presupuestos

$$
C_{\rm pack}(m)=313+m,
\qquad
C_{\rm sep}(m)=476+170m.
$$

**[I]** El primer presupuesto tiene un coste inicial considerable y un incremento pequeño por cada obligación adicional. Compartir ese coste puede ser mucho más importante que simplificar por separado cada columna de datos.

**[R]** Estas cifras pertenecen a dispositivos aritméticos experimentales. No constituyen una nueva cota universal. Sus hipótesis incluyen las certificaciones de potencias, extremos y tamaños: una ecuación terminal aislada puede aceptar códigos cuyos dígitos no siguen la recurrencia pretendida.

**Infraestructura de potencias.** **[R]** Otra reducción afectó a la certificación conjunta de dos potencias relacionadas con la base y la longitud de una codificación:

$$
313\longrightarrow105.
$$

También se construyó una variante de **102 operaciones** que entrega un reloj binario y máscaras geométricas. Su interfaz es diferente: no se trata simplemente de ahorrar tres operaciones adicionales en exactamente el mismo problema.

Un reloj y unas máscaras proporcionan posiciones donde representar datos. Todavía falta certificar que esos datos constituyen una computación: que comienzan con la entrada correcta, respetan todas las transiciones, interpretan adecuadamente los estados y alcanzan la condición de parada o aceptación.

**[I]** Disponer de la estructura donde escribir una ejecución no equivale a comprobar la ejecución.

**La barrera de las trazas explícitas.** **[R]** El experimento universal completo basado en una máquina de ocho registros cerró con un coste registrado de

$$
66\,196
$$

operaciones. El presupuesto no depende del tiempo de ejecución de la computación codificada; su tamaño queda absorbido en los enteros del testigo. Sin embargo, el circuito resultante es ampliamente más costoso que S126.

El informe de cierre conserva esta cifra y su corroboración en los expedientes posteriores, con una limitación documental explícita: no se recuperó el expediente original de la máquina para repetir íntegramente su recuento.

**[I]** El resultado distingue dos objetivos. Comprimir una ejecución de longitud arbitraria en un certificado de estructura fija puede eliminar la dependencia del número de operaciones respecto del tiempo simulado. Obtener, además, un circuito aritmético pequeño exige otra economía. «Tiempo comprimido» y «pocas operaciones» no son sinónimos.

**Selección de índices Pell.** **[R]** Una dificultad recurrente consiste en reconocer el término correcto de una sucesión de Pell. Una ecuación de Pell puede certificar que un par pertenece a la sucesión sin determinar el índice que necesitamos.

Se obtuvo un núcleo condicional de **ocho operaciones**. Escribiendo

$$
\Delta=A^2-1,\qquad B=A+\delta,\qquad
M=B^2-2AB+1,
$$

el mecanismo compara un residuo con el código lineal $d+\delta c$. Bajo una congruencia de potencia y cotas que hacen inyectiva esta codificación en el intervalo pertinente, permite identificar el par Pell deseado. El coste ocho supone $\Delta$ ya disponible y no incluye gratuitamente las hipótesis externas.

La condición de crecimiento pudo deducirse de las relaciones del sistema anfitrión mediante **seis operaciones adicionales**. Quedó pendiente certificar

$$
(k^2)^{2r+1}\equiv W
\pmod{k^4-2Ak^2+1},
$$

donde aquí $W$ designa el valor aritmético

$$
W=d+(k^2-A)c,
$$

no el conjunto enumerable de las secciones anteriores.

**[R]** El exponente $2r+1$ es variable. Saber que la base es invertible módulo el denominador no proporciona una reducción uniforme a un período corto que pueda aprovecharse dentro del presupuesto. Las rutas examinadas no obtuvieron esa certificación económica.

Además, la relación cuadrática

$$
B^2\equiv2AB-1\pmod M
$$

hace que la reducción de las potencias vuelva a generar la recurrencia Pell. El cálculo cambia de presentación, pero reaparece la obligación que debía resolverse. Este obstáculo afecta a las estrategias estudiadas; no demuestra que todo sistema existencial alternativo deba tener el mismo coste.

**Fingerprints y alias.** **[R]** Otra idea fue reconocer el índice mediante congruencias baratas, usadas como *huellas aritméticas* o *fingerprints*. Una huella conserva parte de la información del índice; un **alias** es otro índice que produce una huella aceptada.

Con $\Delta=A^2-1$, el primer filtro combinaba

$$
d^2=\Delta c^2+1,
\qquad
c=N+\Delta v,
\qquad c,d,v>0.
$$

Su coste era de **seis operaciones**, con $\Delta$ compartido. Permitía restringir los índices posibles y establecer una dirección útil, $h\ge N$, pero no garantizaba $h=N$.

Un segundo filtro añadía **siete operaciones** y refinaba la congruencia hasta

$$
c\equiv N+\frac{N(N^2-1)}6\,\Delta
\pmod{\Delta^2}.
$$

La fracción describe el valor entero utilizado en la prueba; el circuito lo certificaba mediante una igualdad polinómica, sin división gratuita.

**[R]** Ambos filtros seguían admitiendo alias. El contraejemplo concreto conservado es

$$
\boxed{A=5,\qquad N=3,\qquad h=195.}
$$

Para $A=5$, tenemos $\Delta=24$ y

$$
\frac{N(N^2-1)}6=4.
$$

El término de índice 195 satisface

$$
\psi_5(195)\equiv99
=3+4\cdot24
\pmod{576}.
$$

Por tanto, supera los dos filtros aunque $195\ne3$. También sobrevive a la condición auxiliar examinada junto con ellos. Esto invalida el reemplazo local propuesto; **no constituye una solución espuria de todo S126**.

**[I]** Una condición puede superar miles de comprobaciones finitas y seguir siendo insuficiente. En este caso, el corpus contabilizaba combinaciones de contratos, no miles de puntos Pell independientes. La prueba posterior identificó familias infinitas de alias: el problema era estructural, no un accidente que bastara corregir ampliando una lista de ejemplos.

## 14. El problema que permanece abierto {#seccion-14}

**[P]** El resultado publicado por Jones proporciona históricamente, bajo su convención operacional, la cota superior

$$
o_{\rm Jones}=100.
$$

**[R]** S126 no mejora esa cota. Aporta una construcción independiente cuyo sistema, prueba escrita y circuito pueden examinarse explícitamente. Los tres estados deben permanecer separados:

$$
\boxed{o_{\rm Jones}=100}
$$

$$
\boxed{o_{\rm proj}(S126)=126}
$$

$$
\boxed{\mathcal O_{\rm univ}^{(\mathcal C)}\text{ óptimo: desconocido}.}
$$

**[A]** De aquí surgen tres preguntas diferentes:

1. **¿Puede reconstruirse el circuito histórico de cien operaciones?** Es una cuestión de identificación documental y reproducción de la construcción publicada.
2. **¿Existe una representación explícita reproducible con $o_{\mathcal C}\le100$, bajo una convención explícita comparable con la histórica?** En el marco de este trabajo, se busca disponer de una especificación completa y un recuento comprobable, sea mediante la recuperación histórica o mediante otra construcción. La pregunta no niega la cota publicada ni afirma que ninguna fuente ajena al corpus pueda contener tal especificación.
3. **¿Cuál es el mínimo posible de $o$?** Resolverlo exige fijar rigurosamente la convención y justificar una cota inferior que acompañe a las construcciones disponibles.

Ni el número 100 ha quedado establecido aquí como óptimo ni el número 126 constituye una cota inferior.

**[R]** El cribado final examinó nuevas recompilaciones, codificaciones mediante el teorema chino del resto y bases mixtas, arquitecturas con muchos testigos y relaciones locales, y combinaciones globales de condiciones. Ninguna reunió simultáneamente una semántica universal completa, costes suficientemente determinados y una estimación conservadora de

$$
o_{\rm proj}\le120.
$$

Algunas compilaciones concretas resultaban demasiado costosas; otras trasladaban el trabajo a un componente esencial cuyo presupuesto seguía sin cerrarse. Estas conclusiones se refieren a las implementaciones y estrategias examinadas. No son cotas inferiores universales ni pruebas de imposibilidad para familias enteras.

Estados de investigación:

- `OUC GENERATION 1 — CLOSED AT S126`
- `OUC GENERATION 2 — CLOSED AT S126`
- `OUC GENERATION 3 — WORK IN PROGRESS`

**[R]** La primera generación de investigación se cerró en S126. El cierre es una decisión de investigación: conserva S126, los lemas locales y los contraejemplos obtenidos, y termina las líneas examinadas. **No es un resultado de optimalidad.**

### Investigación en curso: más allá de S126

**[R]** La segunda generación (G2) cerró sin mejorar S126. En la tercera (G3), todavía en curso, se obtuvo el resultado `EXACTNESS EMERGENT FROM GLOBAL CONTEXT`: la exactitud emerge del contexto global. Esto permitió debilitar el contrato de puertos y eliminar $q_\ast$ como obligación independiente.

**[A]** Quedan pendientes la condición $k<(2p)^r$ y el margen interior de $P_0$ respecto de la celda de $Y$. Todavía no se dispone de un coste completo, un ahorro certificado ni una nueva cota. **S126 sigue en 126 operaciones.**

## 15. Entonces, ¿puede cualquier teorema demostrarse con 100 operaciones? {#seccion-15}

**[P]** La respuesta es afirmativa en el sentido preciso del resultado publicado por Jones. Para una teoría efectivamente axiomatizable, el conjunto de códigos de sus teoremas es computablemente enumerable y admite una representación diofántica. Jones publica el resultado de que la construcción modificada admite una comprobación aritmética con cien operaciones bajo su convención histórica. Denotaremos esta cota por

$$
o_{\rm Jones}=100.
$$

**[R]** Esta afirmación presupone una representación fijada y los números que se proponen como testigo. La comprobación establece que esos números satisfacen las relaciones que certifican la demostrabilidad del enunciado. No afirma que una deducción ordinaria dentro de la teoría pueda escribirse con cien inferencias, cien líneas o cien pasos de razonamiento.

La palabra «prueba» aparece, por tanto, en dos niveles. Una prueba formal es una derivación conforme a los axiomas y reglas de una teoría. El certificado diofántico es una presentación aritmética de evidencia de que tal derivación existe. El argumento metamatemático que conecta ambos niveles es indispensable para interpretar correctamente las igualdades verificadas.

**[I]** Tampoco obtenemos una cota ordinaria de tiempo computacional. Una multiplicación cuenta como una operación aritmética aunque intervengan enteros con una cantidad enorme de cifras. El coste de leerlos, almacenarlos y operar sobre su representación binaria no queda controlado por la cifra cien. Además, encontrar el testigo queda fuera del presupuesto. Comprobar una solución propuesta y buscar una solución son tareas diferentes.

**[R]** A estas precisiones se añade una cuestión documental. El resultado está publicado y fue reiterado por Jones, pero el circuito histórico de cien operaciones no ha podido reconstruirse operación por operación con las fuentes localizadas. Debemos conservar simultáneamente ambos hechos: la existencia de la cota publicada y la limitación de nuestra reproducción.

La construcción S126 aporta un contraste explícito:

$$
o_{\rm proj}(S126)=126.
$$

Este valor corresponde a la convención del proyecto: operaciones binarias de suma, resta y multiplicación; registros compartidos; entradas, testigos y constantes disponibles; comparaciones y búsqueda excluidas del recuento. No identificamos automáticamente esa convención con todos los detalles del cómputo histórico de Jones.

**[R]** Así entendida, la respuesta al título conserva su fuerza matemática sin atribuirle consecuencias que no establece. Jones publica una cota uniforme para una forma aritmética de certificación de la demostrabilidad. No publica una reducción de toda actividad demostrativa a cien pasos ordinarios ni un procedimiento que resuelva cualquier problema matemático en tiempo acotado.

## 16. Conclusión {#seccion-16}

**[R]** El recorrido del artículo comienza con una transformación de perspectiva. Una demostración formal puede codificarse; las demostraciones de una teoría efectivamente axiomatizable pueden enumerarse; y el teorema DPRM permite expresar la pertenencia a ese conjunto mediante la existencia de soluciones diofánticas. La representación universal proporciona entonces un esquema fijo de certificación:

$$
\begin{gathered}
\text{prueba formal}
\longrightarrow
\text{enumerabilidad}
\longrightarrow
\text{DPRM}\\
\longrightarrow
\text{representación universal}
\longrightarrow
\text{certificado aritmético}.
\end{gathered}
$$

La uniformidad pertenece al esquema que se comprueba. Los valores de sus parámetros y testigos pueden variar enormemente.

**[R]** La trayectoria documental de las cifras quedó delimitada por tres estados:

$$
243\ {\rm documentado}
\longrightarrow
149\ {\rm anunciado}
\longrightarrow
100\ {\rm publicado}.
$$

Jones presenta en 1978 el sistema al que atribuye 243 operaciones y anuncia una reducción futura a 149. En 1980 publica el resultado de cien operaciones y lo reitera en 1982. Las fuentes localizadas no permiten convertir esa sucesión documental en una cadena íntegramente reconstruida de transformaciones $243\to149\to100$.

**[R]** S126 responde a una exigencia complementaria: disponer de una construcción cuyo funcionamiento y presupuesto puedan examinarse explícitamente. Su especificación final contiene

$$
37\text{ incógnitas positivas},\qquad
25\text{ ecuaciones},
$$

y su circuito satisface

$$
o_{\rm proj}(S126)
=
42\text{ sumas}
+
16\text{ restas}
+
68\text{ productos}
=
126.
$$

No sustituye la construcción histórica de Jones ni mejora su cota publicada. Hace reproducible una construcción propia bajo una convención declarada.

Los intentos de reducir ese presupuesto produjeron lemas sobre recurrencias empaquetadas, infraestructura compartida de potencias y selección de términos de Pell. También identificaron obstáculos concretos: hipótesis externas cuyo coste no podía omitirse, certificaciones universales demasiado grandes y congruencias que admitían índices alternativos. La primera generación de investigación se cerró en S126. Ese cierre delimita el trabajo realizado; no demuestra optimalidad.

**[I]** La apariencia paradójica del resultado de Jones procede de una separación entre dos tamaños. Una cantidad arbitrariamente grande de información puede quedar alojada en el **tamaño de los enteros**, mientras permanece acotado el número de relaciones aritméticas que se comprueban y de operaciones utilizadas para evaluarlas. Contar operaciones sin contar cifras permite esa concentración de información. La complejidad no desaparece: una parte decisiva permanece en los números y en la búsqueda que conduce a ellos.

**[A]** Quedan abiertas la reconstrucción histórica del circuito de cien operaciones, la obtención de una construcción moderna completamente reproducible con coste comparable no superior a cien y la determinación del mínimo posible bajo una convención operacional fijada.

---

## Apéndice A. Certificado reproducible de S126 {#apendice-a}

[Volver al cuerpo principal: §10](#seccion-10) · [§11](#seccion-11) · [Índice](#contenido)

**Archivo:** `S126_REPRODUCIBLE_CERTIFICATE_v01.md`<br>
**Versión:** 1.0. **Objeto:** sistema final de C3, congelado por `OUC_GENERATION1_FINAL_REPORT_v01.md`.<br>
**Etiquetas:** [P] resultado publicado utilizado como dependencia; [R] construcción y verificación del proyecto; [I] explicación de la convención; [A] cuestión no establecida.

Este documento fija el sistema, sus dominios y su circuito. Conserva los nombres históricos de los registros del apéndice B de C3, incluidos sus huecos: el número de registro no es un coste acumulado. Las instrucciones nuevas `I001`–`I126` son únicamente números de fila consecutivos. No se modifica ni se optimiza S126.

### A.1 Convención y dominio {#apendice-a-1}

[R] La entrada es un entero $x>0$. Los parámetros $(z,u,y)$ son los índices admisibles definidos exactamente en A.4, fijos para el conjunto representado. Los 37 testigos pertenecen a $\mathbb Z_{>0}$. Su orden es

$$
\begin{split}
\mathbf v={}&(b,e,g,\ell,m,n,q,r,t,w,\alpha,\lambda,\theta,p,s,k,\tau,\eta,h_0,A,\\
&c,\varphi,d,\gamma,f,i,j,\omega,C_1,D_1,J,\nu,\rho,\zeta,
\varepsilon_e,\varepsilon_\ell,\varepsilon_g).
\end{split}
$$

Definimos la convención $\mathcal C_{\rm proj}$: cada operación binaria $+,-,\times$ cuesta una unidad. Multiplicar por una constante cuesta uno; un cuadrado cuesta un producto. Las entradas, los testigos ya propuestos y los literales están disponibles. Copiar o reutilizar un registro calculado no añade coste. Los intermedios pertenecen a $\mathbb Z$ y pueden ser negativos. El DAG usa solamente los literales $1,2,4,5,E$, con

$$
E=5^{60}=867361737988403547205962240695953369140625.
$$

Se excluyen las comparaciones finales y de dominio, la búsqueda de testigos, la compilación de parámetros, el almacenamiento de constantes y el tamaño binario de los enteros. No hay división, exponenciación, binomiales, extracción de cifras ni selección de índices como instrucciones gratuitas. Las potencias que aparecen en las ecuaciones se desarrollan en A.5. No se incluye la conversión de las 25 ecuaciones en una sola suma de cuadrados.

[I] El verificador recibe todos los valores, ejecuta las 126 instrucciones y acepta si se cumplen los dominios y las 25 igualdades de A.7. Una igualdad entre testigos no autoriza sustituir uno por otro durante la evaluación: cada uno sigue siendo una entrada propuesta.

La afirmación de coste es $o_{\rm proj}(S126)=126$ para este circuito y esta convención; no es una afirmación de coste mínimo.

### A.2 Lista de símbolos {#apendice-a-2}

En las tablas ejecutables se usa ASCII: `ell` significa $\ell$, `lambda` significa $\lambda$, etc. `C1` es el testigo $C_1$, no una comparación ni el nombre de la fase C1. `t` es un testigo; `t1`, `t2`, etc., son registros distintos. `E01`–`E25` abrevia las etiquetas `S126-E01`–`S126-E25`.

La tabla siguiente enumera individualmente todas las entradas, constantes operacionales y salidas. «Primera utilización» se refiere al orden del DAG y después al de las comparaciones.

| símbolo | tipo | entrada/parámetro/testigo/registro | dominio | primera utilización |
| --- | --- | --- | --- | --- |
| `x` / $x$ | entero | entrada | $\mathbb Z_{>0}$ | I009 |
| `z` / $z$ | entero | parámetro | $\mathbb Z_{>0}$ | I014 |
| `u` / $u$ | entero | parámetro | $\mathbb Z_{>0}$ | I017 |
| `y` / $y$ | entero | parámetro | $\mathbb Z_{>0}$ | I009 |
| `b` / $b$ | entero | testigo | $\mathbb Z_{>0}$ | I001 |
| `e` / $e$ | entero | testigo | $\mathbb Z_{>0}$ | I026 |
| `g` / $g$ | entero | testigo | $\mathbb Z_{>0}$ | I022 |
| `ell` / $\ell$ | entero | testigo | $\mathbb Z_{>0}$ | I033 |
| `m` / $m$ | entero | testigo | $\mathbb Z_{>0}$ | I018 |
| `n` / $n$ | entero | testigo | $\mathbb Z_{>0}$ | I047 |
| `q` / $q$ | entero | testigo | $\mathbb Z_{>0}$ | I004 |
| `r` / $r$ | entero | testigo | $\mathbb Z_{>0}$ | I054 |
| `t` / $t$ | entero | testigo | $\mathbb Z_{>0}$ | I016 |
| `w` / $w$ | entero | testigo | $\mathbb Z_{>0}$ | I056 |
| `alpha` / $\alpha$ | entero | testigo | $\mathbb Z_{>0}$ | I010 |
| `lambda` / $\lambda$ | entero | testigo | $\mathbb Z_{>0}$ | I011 |
| `theta` / $\theta$ | entero | testigo | $\mathbb Z_{>0}$ | I015 |
| `p` / $p$ | entero | testigo | $\mathbb Z_{>0}$ | I059 |
| `s` / $s$ | entero | testigo | $\mathbb Z_{>0}$ | I053 |
| `k` / $k$ | entero | testigo | $\mathbb Z_{>0}$ | I061 |
| `tau` / $\tau$ | entero | testigo | $\mathbb Z_{>0}$ | I064 |
| `eta` / $\eta$ | entero | testigo | $\mathbb Z_{>0}$ | I067 |
| `h0` / $h_0$ | entero | testigo | $\mathbb Z_{>0}$ | I070 |
| `A` / $A$ | entero | testigo | $\mathbb Z_{>0}$ | I055 |
| `c` / $c$ | entero | testigo | $\mathbb Z_{>0}$ | I078 |
| `varphi` / $\varphi$ | entero | testigo | $\mathbb Z_{>0}$ | I075 |
| `d` / $d$ | entero | testigo | $\mathbb Z_{>0}$ | I089 |
| `gamma` / $\gamma$ | entero | testigo | $\mathbb Z_{>0}$ | I081 |
| `f` / $f$ | entero | testigo | $\mathbb Z_{>0}$ | I094 |
| `i` / $i$ | entero | testigo | $\mathbb Z_{>0}$ | I090 |
| `j` / $j$ | entero | testigo | $\mathbb Z_{>0}$ | I103 |
| `omega` / $\omega$ | entero | testigo | $\mathbb Z_{>0}$ | I095 |
| `C1` / $C_1$ | entero | testigo | $\mathbb Z_{>0}$ | I074 |
| `D1` / $D_1$ | entero | testigo | $\mathbb Z_{>0}$ | I114 |
| `J` / $J$ | entero | testigo | $\mathbb Z_{>0}$ | I109 |
| `nu` / $\nu$ | entero | testigo | $\mathbb Z_{>0}$ | I120 |
| `rho` / $\rho$ | entero | testigo | $\mathbb Z_{>0}$ | I123 |
| `zeta` / $\zeta$ | entero | testigo | $\mathbb Z_{>0}$ | I066 |
| `eps_e` / $\varepsilon_e$ | entero | testigo | $\mathbb Z_{>0}$ | I124 |
| `eps_l` / $\varepsilon_\ell$ | entero | testigo | $\mathbb Z_{>0}$ | I125 |
| `eps_g` / $\varepsilon_g$ | entero | testigo | $\mathbb Z_{>0}$ | I126 |
| `1` | entero fijo | constante | 1 | I012 |
| `2` | entero fijo | constante | 2 | I014 |
| `4` | entero fijo | constante | 4 | I079 |
| `5` | entero fijo | constante | 5 | I080 |
| `E` | entero fijo | constante | $E=5^{60}$ | I110 |
| `t1` | entero calculado | registro | $\mathbb Z$ | I001 (definición); I002 (uso) |
| `t2` | entero calculado | registro | $\mathbb Z$ | I002 (definición); I003 (uso) |
| `t3` | entero calculado | registro | $\mathbb Z$ | I003 (definición); I011 (uso) |
| `t4` | entero calculado | registro | $\mathbb Z$ | I004 (definición); I005 (uso) |
| `t5` | entero calculado | registro | $\mathbb Z$ | I005 (definición); I036 (uso) |
| `t6` | entero calculado | registro | $\mathbb Z$ | I006 (definición); I007 (uso) |
| `t8` | entero calculado | registro | $\mathbb Z$ | I007 (definición); I008 (uso) |
| `t9` | entero calculado | registro | $\mathbb Z$ | I008 (definición); E09 (uso) |
| `t15` | entero calculado | registro | $\mathbb Z$ | I009 (definición); I010 (uso) |
| `t16` | entero calculado | registro | $\mathbb Z$ | I010 (definición); E01 (uso) |
| `t18` | entero calculado | registro | $\mathbb Z$ | I011 (definición); I012 (uso) |
| `t19` | entero calculado | registro | $\mathbb Z$ | I012 (definición); E05 (uso) |
| `t20` | entero calculado | registro | $\mathbb Z$ | I013 (definición); E05 (uso) |
| `t21` | entero calculado | registro | $\mathbb Z$ | I014 (definición); I015 (uso) |
| `t22` | entero calculado | registro | $\mathbb Z$ | I015 (definición); E06 (uso) |
| `t23` | entero calculado | registro | $\mathbb Z$ | I016 (definición); I017 (uso) |
| `t24` | entero calculado | registro | $\mathbb Z$ | I017 (definición); E07 (uso) |
| `t25` | entero calculado | registro | $\mathbb Z$ | I018 (definición); I019 (uso) |
| `t26` | entero calculado | registro | $\mathbb Z$ | I019 (definición); E08 (uso) |
| `t27` | entero calculado | registro | $\mathbb Z$ | I020 (definición); I021 (uso) |
| `t28` | entero calculado | registro | $\mathbb Z$ | I021 (definición); I022 (uso) |
| `t29` | entero calculado | registro | $\mathbb Z$ | I022 (definición); I023 (uso) |
| `t30` | entero calculado | registro | $\mathbb Z$ | I023 (definición); I024 (uso) |
| `t31` | entero calculado | registro | $\mathbb Z$ | I024 (definición); I027 (uso) |
| `t32` | entero calculado | registro | $\mathbb Z$ | I025 (definición); I026 (uso) |
| `t33` | entero calculado | registro | $\mathbb Z$ | I026 (definición); I027 (uso) |
| `t34` | entero calculado | registro | $\mathbb Z$ | I027 (definición); I028 (uso) |
| `t35` | entero calculado | registro | $\mathbb Z$ | I028 (definición); I030 (uso) |
| `t36` | entero calculado | registro | $\mathbb Z$ | I029 (definición); I031 (uso) |
| `t37` | entero calculado | registro | $\mathbb Z$ | I030 (definición); I031 (uso) |
| `t38` | entero calculado | registro | $\mathbb Z$ | I031 (definición); I032 (uso) |
| `t39` | entero calculado | registro | $\mathbb Z$ | I032 (definición); I033 (uso) |
| `t40` | entero calculado | registro | $\mathbb Z$ | I033 (definición); I034 (uso) |
| `t41` | entero calculado | registro | $\mathbb Z$ | I034 (definición); I035 (uso) |
| `t42` | entero calculado | registro | $\mathbb Z$ | I035 (definición); I036 (uso) |
| `t43` | entero calculado | registro | $\mathbb Z$ | I036 (definición); I037 (uso) |
| `t44` | entero calculado | registro | $\mathbb Z$ | I037 (definición); I050 (uso) |
| `t45` | entero calculado | registro | $\mathbb Z$ | I038 (definición); I039 (uso) |
| `t46` | entero calculado | registro | $\mathbb Z$ | I039 (definición); I040 (uso) |
| `t47` | entero calculado | registro | $\mathbb Z$ | I040 (definición); I043 (uso) |
| `t48` | entero calculado | registro | $\mathbb Z$ | I041 (definición); I042 (uso) |
| `t49` | entero calculado | registro | $\mathbb Z$ | I042 (definición); I043 (uso) |
| `t50` | entero calculado | registro | $\mathbb Z$ | I043 (definición); I046 (uso) |
| `t51` | entero calculado | registro | $\mathbb Z$ | I044 (definición); I045 (uso) |
| `t52` | entero calculado | registro | $\mathbb Z$ | I045 (definición); I046 (uso) |
| `t53` | entero calculado | registro | $\mathbb Z$ | I046 (definición); I051 (uso) |
| `t54` | entero calculado | registro | $\mathbb Z$ | I047 (definición); I048 (uso) |
| `t55` | entero calculado | registro | $\mathbb Z$ | I048 (definición); I050 (uso) |
| `t56` | entero calculado | registro | $\mathbb Z$ | I049 (definición); I051 (uso) |
| `t57` | entero calculado | registro | $\mathbb Z$ | I050 (definición); I052 (uso) |
| `t58` | entero calculado | registro | $\mathbb Z$ | I051 (definición); I052 (uso) |
| `t59` | entero calculado | registro | $\mathbb Z$ | I052 (definición); E10 (uso) |
| `t60` | entero calculado | registro | $\mathbb Z$ | I053 (definición); I054 (uso) |
| `t61` | entero calculado | registro | $\mathbb Z$ | I054 (definición); I055 (uso) |
| `t62` | entero calculado | registro | $\mathbb Z$ | I055 (definición); I057 (uso) |
| `t63` | entero calculado | registro | $\mathbb Z$ | I056 (definición); I072 (uso) |
| `t64` | entero calculado | registro | $\mathbb Z$ | I057 (definición); I058 (uso) |
| `t65` | entero calculado | registro | $\mathbb Z$ | I058 (definición); E11 (uso) |
| `t66` | entero calculado | registro | $\mathbb Z$ | I059 (definición); I060 (uso) |
| `t67` | entero calculado | registro | $\mathbb Z$ | I060 (definición); I062 (uso) |
| `t68` | entero calculado | registro | $\mathbb Z$ | I061 (definición); I062 (uso) |
| `t69` | entero calculado | registro | $\mathbb Z$ | I062 (definición); I063 (uso) |
| `t70` | entero calculado | registro | $\mathbb Z$ | I063 (definición); E12 (uso) |
| `t71` | entero calculado | registro | $\mathbb Z$ | I064 (definición); E12 (uso) |
| `t73` | entero calculado | registro | $\mathbb Z$ | I065 (definición); I066 (uso) |
| `t74` | entero calculado | registro | $\mathbb Z$ | I066 (definición); E13 (uso) |
| `t77` | entero calculado | registro | $\mathbb Z$ | I067 (definición); E14 (uso) |
| `t78` | entero calculado | registro | $\mathbb Z$ | I068 (definición); I071 (uso) |
| `t79` | entero calculado | registro | $\mathbb Z$ | I069 (definición); I070 (uso) |
| `t80` | entero calculado | registro | $\mathbb Z$ | I070 (definición); I071 (uso) |
| `t81` | entero calculado | registro | $\mathbb Z$ | I071 (definición); E15 (uso) |
| `t84` | entero calculado | registro | $\mathbb Z$ | I072 (definición); E16 (uso) |
| `t85` | entero calculado | registro | $\mathbb Z$ | I073 (definición); I074 (uso) |
| `t86` | entero calculado | registro | $\mathbb Z$ | I074 (definición); I075 (uso) |
| `t87` | entero calculado | registro | $\mathbb Z$ | I075 (definición); E17 (uso) |
| `t88` | entero calculado | registro | $\mathbb Z$ | I076 (definición); I082 (uso) |
| `t89` | entero calculado | registro | $\mathbb Z$ | I077 (definición); I078 (uso) |
| `t90` | entero calculado | registro | $\mathbb Z$ | I078 (definición); I082 (uso) |
| `t91` | entero calculado | registro | $\mathbb Z$ | I079 (definición); I080 (uso) |
| `t92` | entero calculado | registro | $\mathbb Z$ | I080 (definición); I081 (uso) |
| `t93` | entero calculado | registro | $\mathbb Z$ | I081 (definición); I083 (uso) |
| `t94` | entero calculado | registro | $\mathbb Z$ | I082 (definición); I083 (uso) |
| `t95` | entero calculado | registro | $\mathbb Z$ | I083 (definición); E18 (uso) |
| `t96` | entero calculado | registro | $\mathbb Z$ | I084 (definición); I085 (uso) |
| `t97` | entero calculado | registro | $\mathbb Z$ | I085 (definición); I087 (uso) |
| `t98` | entero calculado | registro | $\mathbb Z$ | I086 (definición); I087 (uso) |
| `t99` | entero calculado | registro | $\mathbb Z$ | I087 (definición); I088 (uso) |
| `t100` | entero calculado | registro | $\mathbb Z$ | I088 (definición); E19 (uso) |
| `t101` | entero calculado | registro | $\mathbb Z$ | I089 (definición); I098 (uso) |
| `t102` | entero calculado | registro | $\mathbb Z$ | I090 (definición); I091 (uso) |
| `t103` | entero calculado | registro | $\mathbb Z$ | I091 (definición); I092 (uso) |
| `t104` | entero calculado | registro | $\mathbb Z$ | I092 (definición); I093 (uso) |
| `t105` | entero calculado | registro | $\mathbb Z$ | I093 (definición); E20 (uso) |
| `t106` | entero calculado | registro | $\mathbb Z$ | I094 (definición); I099 (uso) |
| `t107` | entero calculado | registro | $\mathbb Z$ | I095 (definición); I096 (uso) |
| `t108` | entero calculado | registro | $\mathbb Z$ | I096 (definición); I097 (uso) |
| `t109` | entero calculado | registro | $\mathbb Z$ | I097 (definición); E21 (uso) |
| `t110` | entero calculado | registro | $\mathbb Z$ | I098 (definición); I099 (uso) |
| `t111` | entero calculado | registro | $\mathbb Z$ | I099 (definición); I100 (uso) |
| `t112` | entero calculado | registro | $\mathbb Z$ | I100 (definición); I101 (uso) |
| `t113` | entero calculado | registro | $\mathbb Z$ | I101 (definición); I102 (uso) |
| `t114` | entero calculado | registro | $\mathbb Z$ | I102 (definición); I106 (uso) |
| `t115` | entero calculado | registro | $\mathbb Z$ | I103 (definición); I104 (uso) |
| `t116` | entero calculado | registro | $\mathbb Z$ | I104 (definición); I105 (uso) |
| `t117` | entero calculado | registro | $\mathbb Z$ | I105 (definición); I106 (uso) |
| `t118` | entero calculado | registro | $\mathbb Z$ | I106 (definición); I107 (uso) |
| `t119` | entero calculado | registro | $\mathbb Z$ | I107 (definición); E21 (uso) |
| `t129` | entero calculado | registro | $\mathbb Z$ | I108 (definición); I109 (uso) |
| `t130` | entero calculado | registro | $\mathbb Z$ | I109 (definición); I110 (uso) |
| `t131` | entero calculado | registro | $\mathbb Z$ | I110 (definición); E22 (uso) |
| `t132` | entero calculado | registro | $\mathbb Z$ | I111 (definición); I112 (uso) |
| `t133` | entero calculado | registro | $\mathbb Z$ | I112 (definición); I113 (uso) |
| `t134` | entero calculado | registro | $\mathbb Z$ | I113 (definición); E23 (uso) |
| `t135` | entero calculado | registro | $\mathbb Z$ | I114 (definición); E23 (uso) |
| `t136` | entero calculado | registro | $\mathbb Z$ | I115 (definición); I116 (uso) |
| `t137` | entero calculado | registro | $\mathbb Z$ | I116 (definición); I117 (uso) |
| `t138` | entero calculado | registro | $\mathbb Z$ | I117 (definición); I118 (uso) |
| `t139` | entero calculado | registro | $\mathbb Z$ | I118 (definición); I120 (uso) |
| `t140` | entero calculado | registro | $\mathbb Z$ | I119 (definición); I121 (uso) |
| `t142` | entero calculado | registro | $\mathbb Z$ | I120 (definición); I122 (uso) |
| `t143` | entero calculado | registro | $\mathbb Z$ | I121 (definición); I122 (uso) |
| `t144` | entero calculado | registro | $\mathbb Z$ | I122 (definición); E24 (uso) |
| `t146` | entero calculado | registro | $\mathbb Z$ | I123 (definición); E25 (uso) |
| `t147` | entero calculado | registro | $\mathbb Z$ | I124 (definición); E02 (uso) |
| `t148` | entero calculado | registro | $\mathbb Z$ | I125 (definición); E03 (uso) |
| `t149` | entero calculado | registro | $\mathbb Z$ | I126 (definición); E04 (uso) |


Las siguientes abreviaturas no añaden testigos ni nodos. Sus definiciones se expanden por sustitución; los alias operacionales señalan registros que ya se pagan.

| símbolo | tipo | entrada/parámetro/testigo/registro | dominio | primera utilización |
| --- | --- | --- | --- | --- |
| $\beta=b^5$ | expresión | alias de `t3` | $\mathbb Z$ | A.3, E05 |
| $C_0=1+x\beta+g$ | expresión | alias de `t29` | $\mathbb Z$ | A.3, definición de $H$ |
| $H$ | expresión | alias de `t38` | $\mathbb Z$ | A.3 |
| $S$ | expresión | alias de `t44` | $\mathbb Z$ | A.3, E10 |
| $T+1$ | expresión | alias de `t53`; $T$ sólo se usa en la prueba | $\mathbb Z$ | A.3, E10 |
| $M=rsn^2$ | expresión | alias de `t61` | $\mathbb Z$ | A.3, E11 |
| $V=A-M$ | expresión | alias de `t62` | $\mathbb Z$ | A.3, E11 |
| $U=wn^2$ | expresión | alias de `t63` | $\mathbb Z$ | A.3, E16 |
| $N=2r+1$ | expresión | alias de `t85` | $\mathbb Z$ | A.4 |
| $Y=sn^2$ | expresión | alias de `t60` | $\mathbb Z$ | A.4 |
| $\kappa=5^{58},K=5^{59}$ | constantes | sólo prueba/compilación | $\mathbb Z_{>0}$ | A.4 |
| $W$ | conjunto c.e. | objeto representado | subconjunto de $\mathbb Z_{>0}$ | A.4 |
| $P,p_{\boldsymbol i},P_{\boldsymbol i}$ | polinomio y coeficientes | fuente y compilación | $\mathbb Z[\xi_0,\ldots,\xi_{58}]$, $\mathbb Z$, $\mathbb Z$ | A.4 |
| $\xi_0=x,\xi_1,\ldots,\xi_{58}$ | variables fuente | entrada y auxiliares de la fuente; no testigos del DAG | $x>0$, restantes $\ge0$ | A.4 |
| $\boldsymbol i=(i_0,\ldots,i_{58}),\lvert\boldsymbol i\rvert$ | multiíndice y suma de componentes | compilación | $\mathbb Z_{\ge0}^{59}$, suma $\le4$ | A.4 |
| $a,h,j_0,d_0$ | base, índices y cifra genéricos | variables locales de prueba | enteros en los rangos indicados | A.4 |
| $\chi_a(h),\psi_a(h)$ | sucesiones Pell | sólo prueba | $\mathbb Z_{\ge0}$, $a\ge2,h\ge0$ | A.4 |
| $W_0=bw,\Delta_b=2Ab-b^2-1$ | expresiones | sólo prueba | $\mathbb Z$, positivas bajo las hipótesis | A.4 |
| $F_h,Q_h$ | sucesiones auxiliares | sólo prueba del selector | $\mathbb Z$ | A.4 |
| $R=c/k,P_0=(U+1)^{2r}/U^r,T_0$ | racionales | sólo prueba de ventana | $\mathbb Q_{>0}$ | A.4 |
| $Z$ | parte entera binomial | sólo prueba | $\mathbb Z_{>0}$ | A.4 |
| $S_a,T_a,N_a$, $a=1,2,3$ | bloques digitales | sólo prueba | enteros con cotas explícitas | A.4 |
| $\tau_2(v,w)=0$ | predicado de ausencia de acarreos binarios | sólo prueba; no instrucción | $v,w\ge0$ | A.4 |
| $X,[X^K]$ | indeterminada y extracción de coeficiente | sólo prueba | anillo $\mathbb Z[X]$ | A.4 |
| $\mathcal C(X),\mathcal E(X),\Lambda(X),E_0$ | polinomios y entero detector | sólo prueba | $\mathbb Z[X]$, $\mathbb Z$ | A.4 |
| $h$, $j$ en sumatorios | índices mudos | sólo prueba | rangos escritos en cada suma | A.4 |
| $N_+,N_-,N_\times$ | contadores | metadatos del circuito | $\mathbb Z_{\ge0}$ | A.6 |

Los índices mudos no son los testigos $i,j,t$; se escribirá $j_0$ para un índice Pell cuya confusión con el testigo $j$ sería posible. Los identificadores locales del programa de A.9 son variables del verificador, no símbolos del sistema diofántico.

### A.3 Sistema S126 {#apendice-a-3}

[R] Abreviaturas completamente determinadas:

$$
\begin{gathered}
\beta=b^5,\quad C_0=1+x\beta+g,\\
H=2(e-z\lambda)C_0^4+\lambda\beta(1+q^4),\\
S=g+eq^3+\ell q^5+Hq^7,\\
T+1=q^3-b\ell+\ell+\theta\lambda q^3+(\beta-2)q^8,\\
M=rsn^2,\quad V=A-M,\quad U=wn^2.
\end{gathered}
$$

Las ecuaciones finales son las siguientes. No se presupone que una de ellas ya se haya satisfecho al evaluar otra.

$$
\begin{array}{rl}
\text{S126-E01}&b=xy+\alpha,\\
\text{S126-E02}&e+\varepsilon_e=q^2,\\
\text{S126-E03}&\ell+\varepsilon_\ell=q^2,\\
\text{S126-E04}&g+\varepsilon_g=q,\\
\text{S126-E05}&\lambda+q^4=1+\lambda\beta,\\
\text{S126-E06}&\theta+2z=\beta,\\
\text{S126-E07}&\ell=u+t\theta,\\
\text{S126-E08}&e=y+m\theta,\\
\text{S126-E09}&n=q^{16},\\
\text{S126-E10}&r=S(n^2-n)+(T+1)(n^2-1),\\
\text{S126-E11}&p=2MV,\\
\text{S126-E12}&(p^2-1)k^2+1=\tau^2,\\
\text{S126-E13}&c=ksn^2+\zeta,\\
\text{S126-E14}&k=\zeta+\eta,\\
\text{S126-E15}&k=r+1+h_0(p-1),\\
\text{S126-E16}&V=MU,\\
\text{S126-E17}&c=2r+1+C_1+\varphi,\\
\text{S126-E18}&d=bw+c(A-2)+(4A-5)\gamma,\\
\text{S126-E19}&d^2=(A^2-1)c^2+1,\\
\text{S126-E20}&f^2=(A^2-1)(ic^2)^2+1,\\
\text{S126-E21}&(d+\omega f)^2=\bigl((A+f^2(d^2-A))^2-1\bigr)(2r+1+jc)^2+1,\\
\text{S126-E22}&C_1=E+J(A-1),\\
\text{S126-E23}&D_1^2=(A^2-1)C_1^2+1,\\
\text{S126-E24}&D_1=q+C_1(A-b)+\nu(2Ab-b^2-1),\\
\text{S126-E25}&r=n+\rho.
\end{array}
$$

Procedencia exacta: E01–E04 son M1a–M1d de C3; E13–E14 son L10a–L10b de C2; E22–E24 son H18–H20 de C1. E17 conserva la forma $c=2r+1+C_1+\varphi$, con los testigos del selector C1. Las restantes ecuaciones son las preservadas en C3. La nueva $\alpha$ y la nueva $\eta$ tienen las funciones indicadas aquí; no se identifican con los testigos homónimos de versiones anteriores.

### A.4 Teorema lógico {#apendice-a-4}

#### Fuente, normalización y admisibilidad

[P] Se utiliza la representación normalizada de Jones (1982, pp. 560–561): el conjunto c.e. $W\subseteq\mathbb Z_{>0}$ tiene una representación mediante un polinomio entero de **grado total a lo sumo cuatro**, con 58 auxiliares no negativos, tal que

$$
x\in W\iff\exists\xi_1,\ldots,\xi_{58}\ge0\;P(x,\xi_1,\ldots,\xi_{58})=0,
\qquad P(x,0,\ldots,0)\ne0\quad(x>0).
$$

Esta representación publicada es una dependencia de la construcción; no se afirma que cualquier polinomio cuártico arbitrario ya tenga esa normalización. Se incluye la variable $x=\xi_0$ en el grado total. Escribimos

$$
P=\sum_{|\boldsymbol i|\le4}p_{\boldsymbol i}\prod_{j=0}^{58}\xi_j^{i_j},
\qquad P_{\boldsymbol i}=(4-|\boldsymbol i|)!\left(\prod_{j=0}^{58}i_j!\right)p_{\boldsymbol i}.
$$

La suma recorre **todos** los multiíndices de grado a lo sumo cuatro, incluidos los de coeficiente cero. Con $\kappa=5^{58},K=5^{59},E=5^{60}$, la admisibilidad significa exactamente que se ha elegido una potencia de dos

$$
z>1+\max_{|\boldsymbol i|\le4}|P_{\boldsymbol i}|,
$$

y se han compilado

$$
u=\sum_{j=1}^{58}(2z)^{5^j},\qquad
y=\sum_{|\boldsymbol i|\le4}(z+P_{\boldsymbol i})(2z)^{K-\sum_{j=0}^{58}i_j5^j}.
$$

Los exponentes son distintos y no negativos, pues $\sum i_j5^j\le4\kappa<K$. Además $0<z+P_{\boldsymbol i}<2z$, $u\ge2z$ y $y\ge(2z)^K>2z60^4>32z$. Los parámetros dependen de $P$, no de la entrada $x$.

**[R] Teorema.** Para cualquier representación fuente y cualquier terna admisible así obtenida,

$$
\boxed{\forall x\in\mathbb Z_{>0},\qquad
x\in W\iff\exists\mathbf v\in\mathbb Z_{>0}^{37}\;S126(x,\mathbf v;z,u,y).}
$$

#### Dependencias matemáticas de la demostración

[P] Se utilizan los siguientes resultados de Jones (1982), en las instancias fijadas por los expedientes. Se explicitan porque verificar identidades polinómicas no demuestra por sí solo el teorema lógico.

1. **Pell (lemas 2.18 y 2.20).** Para $a\ge2$, se define $(\chi_a(0),\psi_a(0))=(1,0)$ y
   $$
   \chi_a(h+1)=a\chi_a(h)+(a^2-1)\psi_a(h),\quad
   \psi_a(h+1)=\chi_a(h)+a\psi_a(h).
   $$
   Las soluciones positivas de $X^2-(a^2-1)Y^2=1$ son exactamente $(\chi_a(h),\psi_a(h))$, $h\ge1$. Se tiene $\psi_a(h)\equiv h\pmod{a-1}$, monotonía estricta y, para los índices $h>2$ usados abajo, $(2a-1)^{h-1}<\psi_a(h)<(2a)^{h-1}$.
2. **Índice Pell impar (corolario 2.29).** Con $A>1$, $N$ impar y $1<N<c$, las ecuaciones E19–E21 —con $N=2r+1$ en E21— y testigos positivos $f,i,j,\omega$ certifican exactamente $c=\psi_A(N),d=\chi_A(N)$. Recíprocamente esos valores admiten dichos testigos positivos, conservando $d$.
3. **Puente exponencial/binomial (lemas 2.22, 2.24–2.26).** La congruencia $3W_0\psi_A(N)\equiv2(W_0^2-1)\pmod{4A-5}$, bajo $N>1$, $W_0>1$, $A>W_0^3$ y $A>2^{3N}$, da $W_0=2^N$ en la instancia de base dos usada aquí. En la dirección constructiva del paquete, para $b$ potencia de dos, $r>n>b>1$, $n>8$ y $n^2\mid\binom{2r}{r}$, se toma $w=2^{2r+1}/b$, $U=wn^2$, $Y=\lfloor(U+1)^{2r}/U^r\rfloor$, $s=Y/n^2$, $M=rY$, $A=M(U+1)$, $p=2M^2U$, $k=\psi_p(r+1)$, $c=\psi_A(2r+1)$, $d=\chi_A(2r+1)$. El paquete proporciona la norma de $k$, su congruencia de índice, la ventana $|c/k-Y|<1/2$, la congruencia de E18 y las cotas de crecimiento utilizadas abajo. C2 refina la ventana a $0<c/k-Y<1/4$; esa refinación se justifica explícitamente en la corrección.
4. **Acarreos y cambio de base (lemas 2.7–2.9, 2.11 y 2.16; §4).** Para $n$ potencia de dos, $0<S,T<n$ y $r=S(n^2-n)+(T+1)(n^2-1)$, se tiene $n^2\mid\binom{2r}{r}\iff\tau_2(S,T)=0$. Los bloques de longitudes potencia de dos, con $0\le S_a,T_a<N_a$, separan esta condición en tres condiciones independientes. El cambio de base usa bases potencia de dos $2z<\beta$, longitudes $K+1<2K<4K$, la cota $2(2z)^{2K+1}<\beta$ y las congruencias de E07–E08: con $e,\ell<q^2$ y la máscara de $4K$ posiciones, recupera las expansiones escritas abajo. La primera máscara recupera los dígitos de $g$. No se utiliza ninguna de estas operaciones digitales como instrucción del DAG.

#### Completitud

[R] Supongamos $x\in W$. Elegimos una solución fuente $\boldsymbol\xi\ge0$ de $P=0$. No es totalmente nula por la normalización. Tomamos $b$, potencia de dos, suficientemente grande para que $b>xy$ y $\xi_j<b$, y definimos

$$
\beta=b^5,\quad q=\beta^K=b^E,\quad
\lambda=\frac{q^4-1}{\beta-1},\quad\theta=\beta-2z,
$$
$$
\ell=\sum_{j=1}^{58}\beta^{5^j},\quad
e=\sum_{|\boldsymbol i|\le4}(z+P_{\boldsymbol i})\beta^{K-\sum i_j5^j},\quad
g=\sum_{j=1}^{58}\xi_j\beta^{5^j}.
$$

Estos enteros son positivos. Las cotas $\ell<2\beta^\kappa$, $e<2z\beta^{K+1}$, $g<b\beta^\kappa$ implican $e,\ell<q^2$ y $g<q$. Por tanto

$$
\alpha=b-xy,\quad\varepsilon_e=q^2-e,\quad
\varepsilon_\ell=q^2-\ell,\quad\varepsilon_g=q-g
$$

son positivos. Evaluar el mismo polinomio en $\beta$ y en $2z$ da congruencias módulo $\beta-2z$; además $\ell>u,e>y$. Se fijan $t=(\ell-u)/\theta>0$, $m=(e-y)/\theta>0$. Quedan satisfechas E01–E08.

Se toma $n=q^{16}$ y se define $r$ por E10. Los bloques digitales de la corrección son positivos y menores que sus ventanas. Sus dos primeras condiciones de ausencia de acarreo se cumplen por las expansiones; la tercera equivale a $P=0$ por la identidad detectora demostrada abajo. De ahí $n^2\mid\binom{2r}{r}$ y $r>n$. Ponemos $\rho=r-n>0$.

Aplicamos ahora la construcción del puente binomial del punto 3. El cociente $w=2^{2r+1}/b$ es entero porque $b$ es potencia de dos y $r>b$. La expansión binomial de $P_0$ y $n^2\mid\binom{2r}{r}$ aseguran que $Y$ es divisible por $n^2$. Así $s,M,A,p,k,c,d$ quedan fijados como allí se indica. Tomamos

$$
\tau=\chi_p(r+1),\qquad h_0=\frac{k-r-1}{p-1}>0.
$$

La congruencia Pell hace entero a $h_0$, y el crecimiento de $\psi_p(r+1)$ da su positividad. E11, E12, E15 y E16 se satisfacen. El argumento de C2 expuesto abajo, que también vale partiendo de la ventana simétrica del puente, da $0<c-kY<k/4$. Definimos

$$
\zeta=c-kY>0,\qquad\eta=k-\zeta>0,
$$

y obtenemos E13–E14. La congruencia constructiva del puente hace entero a

$$
\gamma=\frac{d-bw-(A-2)c}{4A-5}.
$$

Es positivo: $d=Ac-\psi_A(N-1)$, $N=2r+1$, y las cotas del paquete dan $c>bw$, de modo que el numerador es $2c-\psi_A(N-1)-bw>c-bw>0$. E18 queda satisfecha; el corolario 2.29 proporciona los testigos positivos $f,i,j,\omega$ para E19–E21.

Resta construir el selector final. Se tienen $E<N<A$. Elegimos

$$
C_1=\psi_A(E),\quad D_1=\chi_A(E),\quad
J=\frac{\psi_A(E)-E}{A-1},\quad
\varphi=c-N-\psi_A(E).
$$

La congruencia Pell y $\psi_A(E)>E$ dan $J>0$ entero. Los incrementos de $\psi_A$ satisfacen $\psi_A(h+1)-\psi_A(h)\ge2h+1$; por ello
$\psi_A(N)-\psi_A(E)\ge N^2-E^2>N$ y $\varphi>0$. Esto prueba E17, E22 y E23 con todos sus dominios.

Definamos $\Delta_b=2Ab-b^2-1$, $F_h=\chi_A(h)+(b-A)\psi_A(h)$. La recurrencia da

$$
F_{h+1}-bF_h=\Delta_b\psi_A(h),\qquad
F_E=b^E+\Delta_b Q_E,\quad
Q_E=\sum_{h=1}^{E-1}b^{E-1-h}\psi_A(h)>0.
$$

Con $\nu=Q_E$ y $q=b^E$ se cumple E24. Se han construido los 37 testigos estrictamente positivos de las 25 ecuaciones.

#### Corrección

[R] Supongamos una solución positiva de S126. E01–E04 dan $b>xy$, $e,\ell<q^2$, $g<q$. E05 implica $q^4=1+\lambda(\beta-1)\ge b^5$, luego $q>b$. E09 y E25 dan $n=q^{16}<r$. La admisibilidad implica, antes de recuperar la exponencial, $b>y>32z$, $b>2z60^4$ y $b>3E$.

**Paquete Pell y ventana C2.** Pongamos $Y=sn^2,U=wn^2,M=rY,N=2r+1,W_0=bw,R=c/k$. E11 y E16 dan

$$
A=M(U+1),\qquad p=2M^2U.
$$

En particular $A>1,p>A,2A<2p-1,p>r+2$, y $Y,U>64$. Por E17, $1<N<c$; el corolario 2.29 aplica a E19–E21 y da $c=\psi_A(N),d=\chi_A(N)$. E12 identifica $k=\psi_p(j_0)$ para algún $j_0\ge1$. E15 y la congruencia Pell dan $j_0=r+1+h(p-1)$, $h\ge0$. E13–E14 implican $0<R-Y<1$. Si $h\ge1$, las cotas Pell dan

$$
R<\frac{(2A)^{2r}}{(2p-1)^{r+p-1}}
<(2p-1)^{r-p+1}<1,
$$

en contradicción con $R>Y-1>63$. Por tanto $k=\psi_p(r+1)$.

Para $P_0=(U+1)^{2r}/U^r$, las cotas Pell y Bernoulli proporcionan

$$
P_0(1-r/A)<R<P_0(1+r/p).
$$

Como $r/A=1/[Y(U+1)]<1/64$ y $R<Y+1$, se obtiene $P_0/Y<2$ y $Y>U^{r-1}$. En consecuencia

$$
A>rU^r>n^n,\quad N<A,\quad A>2^{3N},\quad A>W_0^3.
$$

E18 y E19 dan algebraicamente
$3W_0c\equiv2(W_0^2-1)\pmod{4A-5}$. El lema 2.22, con las cotas recién verificadas, fuerza $W_0=2^N$; por tanto $b$ es potencia de dos.

Ahora $n^2>4b$, así que $U>4W_0=8\cdot4^r$. Descomponemos exactamente

$$
P_0=Z+T_0,\quad
Z=\sum_{h=r}^{2r}\binom{2r}{h}U^{h-r},\quad
T_0=\sum_{h=0}^{r-1}\binom{2r}{h}U^{h-r}.
$$

Se tiene $\binom{2r}{r-1}/U\le T_0<4^r/U<1/8$, con $\binom{2r}{r-1}>2$. Las estimaciones previas dan $|R-P_0|<2/(U+1)$, de donde

$$
0<T_0-\frac2{U+1}<R-Z<T_0+\frac2{U+1}<\frac14.
$$

La ventana $0<R-Y<1$ fuerza $Y=Z$. El mismo resultado vale para la ventana constructiva $|R-Y|<1/2$: cualquier entero distinto de $Z$ queda a distancia mayor que $3/4$ o mayor que uno. Esto justifica la refinación usada en completitud. Finalmente $Z\equiv\binom{2r}{r}\pmod U$, $n^2\mid U$ y $n^2\mid Y$, luego

$$
n^2\mid\binom{2r}{r}.
$$

**Selector C1.** Las cotas $3E<b<q<n<r$, $A>n^n$ dan $E<N<A$, $b^{3E}<A$, $q^3<A$. E23 identifica $C_1=\psi_A(j_0),D_1=\chi_A(j_0)$. E17 implica $C_1<c=\psi_A(N)$, luego $1\le j_0<N<A$. E22 y la congruencia de Pell dan $j_0\equiv E\pmod{A-1}$; ambos están entre 1 y $A-2$, de modo que $j_0=E$. La identidad de $F_E$ y E24 implican $q\equiv b^E\pmod{\Delta_b}$. Puesto que $0<q,b^E<A<\Delta_b$, resulta

$$
q=b^E=\beta^K,\qquad
\lambda=\sum_{h=0}^{4K-1}\beta^h,\qquad\theta=\beta-2z.
$$

**Bloques digitales.** Definimos

$$
\begin{array}{lll}
S_1=g,&T_1=q^3-1-(b-1)\ell,&N_1=q^3,\\
S_2=e+\ell q^2,&T_2=\theta\lambda,&N_2=q^4,\\
S_3=H,&T_3=(\beta-2)q,&N_3=q^9.
\end{array}
$$

Entonces $S=S_1+S_2N_1+S_3N_1N_2$, $T=T_1+T_2N_1+T_3N_1N_2$, $N_1N_2N_3=n$. Las cotas previas dan $0<S_a,T_a<N_a$: para el segundo bloque, $S_2\le q^4-1$ y $T_2<(\beta-1)\lambda=q^4-1$. Para el tercero, $x\beta<q$, $C_0<2q$ y

$$
0<\lambda q^4(\beta-32z)<H
<32q^6+2q^4+2q^8<4q^8<q^9.
$$

Aquí se utiliza la desigualdad válida $\beta\lambda<2q^4$. C3 corrigió explícitamente la desigualdad heredada $\beta\lambda<q^4$, que es falsa porque $\beta\lambda=q^4+\lambda-1$. Este apéndice conserva esa corrección ya documentada, sin cambiar el sistema.

Los lemas de acarreos se aplican ahora, con todas sus cotas verificadas:

$$
n^2\mid\binom{2r}{r}
\iff\tau_2(S,T)=0
\iff\bigwedge_{a=1}^3\tau_2(S_a,T_a)=0.
$$

Las zonas de $e+\ell q^2$ no se solapan. E07–E08 dan las congruencias módulo $\beta-2z$. Se cumplen $2(2z)^{2K+1}<\beta$, $e,\ell<(2z)\beta^{2K}$, y las longitudes del cambio de base son $K+1,2K,4K$. La segunda máscara recupera exactamente las expansiones de $e,\ell$ de la completitud. La primera máscara y $g<q$ recuperan

$$
g=\sum_{j=1}^{58}\xi_j\beta^{5^j},\qquad0\le\xi_j<b.
$$

**Detector final.** Definimos

$$
\mathcal C(X)=1+xX+\sum_{j=1}^{58}\xi_jX^{5^j},\quad
\Lambda(X)=\sum_{h=0}^{4K-1}X^h,
$$
$$
\mathcal E(X)=\sum_{|\boldsymbol i|\le4}(z+P_{\boldsymbol i})X^{K-\sum i_j5^j}.
$$

La inyectividad de las posiciones en base cinco y la normalización factorial dan

$$
[X^K]\mathcal C(X)^4(\mathcal E(X)-z\Lambda(X))=24P(x,\boldsymbol\xi).
$$

Todos sus coeficientes tienen valor absoluto menor que $z60^4b^4<\beta/2$, y el soporte está en $[0,8K)$. Añadir $(\beta/2)\Lambda(X)(1+X^{4K})$ sitúa cada cifra estrictamente entre 0 y $\beta$, sin transportes al evaluar en $\beta$. El dígito de orden $K$ de

$$
E_0=C_0^4(e-z\lambda)+(\beta/2)\lambda(1+q^4)
$$

es $\beta/2+24P(x,\boldsymbol\xi)$. Para $0<d_0<\beta$, con $\beta$ potencia de dos, la ausencia de acarreo con $\beta/2-1$ equivale a $d_0=\beta/2$. Por tanto

$$
\tau_2(E_0,(\beta/2-1)q)=0\iff P(x,\boldsymbol\xi)=0.
$$

Multiplicar ambos sumandos por dos sólo desplaza los bits: $H=2E_0$, $T_3=2(\beta/2-1)q$. La tercera condición de acarreo fuerza $P=0$, y con ello $x\in W$. Esto completa la corrección. La prueba no presupone la antigua cota multiplicativa de S146 ni la usa para justificar circularmente el selector.

### A.5 DAG aritmético completo {#apendice-a-5}

[R] Cada fila tiene exactamente una operación binaria. `*` significa producto. «Reutilizada en» lista todos los consumidores **directos**, incluidas las comparaciones finales. Usar dos veces un registro en un cuadrado no crea dos consumidores distintos ni dos productos. Las comparaciones se ejecutan al final y cuestan cero bajo la convención fijada.

| ID | operación | operandos | salida | reutilizada en | coste acumulado |
| --- | --- | --- | --- | --- | --- |
| I001 | * | `b`, `b` | `t1` | I002 | 1 |
| I002 | * | `t1`, `t1` | `t2` | I003 | 2 |
| I003 | * | `t2`, `b` | `t3` | I011, I020, I044, E06 | 3 |
| I004 | * | `q`, `q` | `t4` | I005, I006, I032, I034, E02, E03 | 4 |
| I005 | * | `t4`, `q` | `t5` | I036, I039, I042 | 5 |
| I006 | * | `t4`, `t4` | `t6` | I007, I013, I029 | 6 |
| I007 | * | `t6`, `t6` | `t8` | I008, I045 | 7 |
| I008 | * | `t8`, `t8` | `t9` | E09 | 8 |
| I009 | * | `x`, `y` | `t15` | I010 | 9 |
| I010 | + | `t15`, `alpha` | `t16` | E01 | 10 |
| I011 | * | `lambda`, `t3` | `t18` | I012, I029, I030 | 11 |
| I012 | + | `t18`, `1` | `t19` | E05 | 12 |
| I013 | + | `lambda`, `t6` | `t20` | E05 | 13 |
| I014 | * | `2`, `z` | `t21` | I015 | 14 |
| I015 | + | `theta`, `t21` | `t22` | E06 | 15 |
| I016 | * | `t`, `theta` | `t23` | I017 | 16 |
| I017 | + | `u`, `t23` | `t24` | E07 | 17 |
| I018 | * | `m`, `theta` | `t25` | I019 | 18 |
| I019 | + | `y`, `t25` | `t26` | E08 | 19 |
| I020 | * | `x`, `t3` | `t27` | I021 | 20 |
| I021 | + | `t27`, `1` | `t28` | I022 | 21 |
| I022 | + | `t28`, `g` | `t29` | I023 | 22 |
| I023 | * | `t29`, `t29` | `t30` | I024 | 23 |
| I024 | * | `t30`, `t30` | `t31` | I027 | 24 |
| I025 | * | `z`, `lambda` | `t32` | I026 | 25 |
| I026 | - | `e`, `t32` | `t33` | I027 | 26 |
| I027 | * | `t33`, `t31` | `t34` | I028 | 27 |
| I028 | * | `2`, `t34` | `t35` | I030 | 28 |
| I029 | * | `t18`, `t6` | `t36` | I031 | 29 |
| I030 | + | `t35`, `t18` | `t37` | I031 | 30 |
| I031 | + | `t37`, `t36` | `t38` | I032 | 31 |
| I032 | * | `t38`, `t4` | `t39` | I033 | 32 |
| I033 | + | `ell`, `t39` | `t40` | I034 | 33 |
| I034 | * | `t40`, `t4` | `t41` | I035 | 34 |
| I035 | + | `e`, `t41` | `t42` | I036 | 35 |
| I036 | * | `t42`, `t5` | `t43` | I037 | 36 |
| I037 | + | `g`, `t43` | `t44` | I050 | 37 |
| I038 | * | `b`, `ell` | `t45` | I039 | 38 |
| I039 | - | `t5`, `t45` | `t46` | I040 | 39 |
| I040 | + | `t46`, `ell` | `t47` | I043 | 40 |
| I041 | * | `theta`, `lambda` | `t48` | I042 | 41 |
| I042 | * | `t48`, `t5` | `t49` | I043 | 42 |
| I043 | + | `t47`, `t49` | `t50` | I046 | 43 |
| I044 | - | `t3`, `2` | `t51` | I045 | 44 |
| I045 | * | `t51`, `t8` | `t52` | I046 | 45 |
| I046 | + | `t50`, `t52` | `t53` | I051 | 46 |
| I047 | * | `n`, `n` | `t54` | I048, I049, I053, I056 | 47 |
| I048 | - | `t54`, `n` | `t55` | I050 | 48 |
| I049 | - | `t54`, `1` | `t56` | I051 | 49 |
| I050 | * | `t44`, `t55` | `t57` | I052 | 50 |
| I051 | * | `t53`, `t56` | `t58` | I052 | 51 |
| I052 | + | `t57`, `t58` | `t59` | E10 | 52 |
| I053 | * | `s`, `t54` | `t60` | I054, I065 | 53 |
| I054 | * | `r`, `t60` | `t61` | I055, I057, I072 | 54 |
| I055 | - | `A`, `t61` | `t62` | I057, E16 | 55 |
| I056 | * | `w`, `t54` | `t63` | I072 | 56 |
| I057 | * | `t61`, `t62` | `t64` | I058 | 57 |
| I058 | * | `2`, `t64` | `t65` | E11 | 58 |
| I059 | * | `p`, `p` | `t66` | I060 | 59 |
| I060 | - | `t66`, `1` | `t67` | I062 | 60 |
| I061 | * | `k`, `k` | `t68` | I062 | 61 |
| I062 | * | `t67`, `t68` | `t69` | I063 | 62 |
| I063 | + | `t69`, `1` | `t70` | E12 | 63 |
| I064 | * | `tau`, `tau` | `t71` | E12 | 64 |
| I065 | * | `k`, `t60` | `t73` | I066 | 65 |
| I066 | + | `t73`, `zeta` | `t74` | E13 | 66 |
| I067 | + | `zeta`, `eta` | `t77` | E14 | 67 |
| I068 | + | `r`, `1` | `t78` | I071, I073 | 68 |
| I069 | - | `p`, `1` | `t79` | I070 | 69 |
| I070 | * | `h0`, `t79` | `t80` | I071 | 70 |
| I071 | + | `t78`, `t80` | `t81` | E15 | 71 |
| I072 | * | `t61`, `t63` | `t84` | E16 | 72 |
| I073 | + | `r`, `t78` | `t85` | I074, I104 | 73 |
| I074 | + | `t85`, `C1` | `t86` | I075 | 74 |
| I075 | + | `t86`, `varphi` | `t87` | E17 | 75 |
| I076 | * | `b`, `w` | `t88` | I082 | 76 |
| I077 | - | `A`, `2` | `t89` | I078 | 77 |
| I078 | * | `c`, `t89` | `t90` | I082 | 78 |
| I079 | * | `4`, `A` | `t91` | I080 | 79 |
| I080 | - | `t91`, `5` | `t92` | I081 | 80 |
| I081 | * | `t92`, `gamma` | `t93` | I083 | 81 |
| I082 | + | `t88`, `t90` | `t94` | I083 | 82 |
| I083 | + | `t94`, `t93` | `t95` | E18 | 83 |
| I084 | * | `A`, `A` | `t96` | I085 | 84 |
| I085 | - | `t96`, `1` | `t97` | I087, I092, I112 | 85 |
| I086 | * | `c`, `c` | `t98` | I087, I090 | 86 |
| I087 | * | `t97`, `t98` | `t99` | I088 | 87 |
| I088 | + | `t99`, `1` | `t100` | E19 | 88 |
| I089 | * | `d`, `d` | `t101` | I098, E19 | 89 |
| I090 | * | `i`, `t98` | `t102` | I091 | 90 |
| I091 | * | `t102`, `t102` | `t103` | I092 | 91 |
| I092 | * | `t97`, `t103` | `t104` | I093 | 92 |
| I093 | + | `t104`, `1` | `t105` | E20 | 93 |
| I094 | * | `f`, `f` | `t106` | I099, E20 | 94 |
| I095 | * | `omega`, `f` | `t107` | I096 | 95 |
| I096 | + | `d`, `t107` | `t108` | I097 | 96 |
| I097 | * | `t108`, `t108` | `t109` | E21 | 97 |
| I098 | - | `t101`, `A` | `t110` | I099 | 98 |
| I099 | * | `t106`, `t110` | `t111` | I100 | 99 |
| I100 | + | `A`, `t111` | `t112` | I101 | 100 |
| I101 | * | `t112`, `t112` | `t113` | I102 | 101 |
| I102 | - | `t113`, `1` | `t114` | I106 | 102 |
| I103 | * | `j`, `c` | `t115` | I104 | 103 |
| I104 | + | `t85`, `t115` | `t116` | I105 | 104 |
| I105 | * | `t116`, `t116` | `t117` | I106 | 105 |
| I106 | * | `t114`, `t117` | `t118` | I107 | 106 |
| I107 | + | `t118`, `1` | `t119` | E21 | 107 |
| I108 | - | `A`, `1` | `t129` | I109 | 108 |
| I109 | * | `J`, `t129` | `t130` | I110 | 109 |
| I110 | + | `t130`, `E` | `t131` | E22 | 110 |
| I111 | * | `C1`, `C1` | `t132` | I112 | 111 |
| I112 | * | `t97`, `t132` | `t133` | I113 | 112 |
| I113 | + | `t133`, `1` | `t134` | E23 | 113 |
| I114 | * | `D1`, `D1` | `t135` | E23 | 114 |
| I115 | - | `A`, `b` | `t136` | I116, I119 | 115 |
| I116 | + | `t136`, `A` | `t137` | I117 | 116 |
| I117 | * | `b`, `t137` | `t138` | I118 | 117 |
| I118 | - | `t138`, `1` | `t139` | I120 | 118 |
| I119 | * | `C1`, `t136` | `t140` | I121 | 119 |
| I120 | * | `nu`, `t139` | `t142` | I122 | 120 |
| I121 | + | `q`, `t140` | `t143` | I122 | 121 |
| I122 | + | `t143`, `t142` | `t144` | E24 | 122 |
| I123 | + | `n`, `rho` | `t146` | E25 | 123 |
| I124 | + | `e`, `eps_e` | `t147` | E02 | 124 |
| I125 | + | `ell`, `eps_l` | `t148` | E03 | 125 |
| I126 | + | `g`, `eps_g` | `t149` | E04 | 126 |


### A.6 Desglose independiente {#apendice-a-6}

[R] El recuento directo de la columna «operación» de A.5 da

$$
N_+=42,\qquad N_-=16,\qquad N_\times=68,\qquad42+16+68=126.
$$

Esta segunda partición agrupa filas disjuntas por función; cada registro aparece en un solo bloque, aunque lo utilicen varias ecuaciones:

| bloque disjunto | + | − | × | total |
| --- | --- | --- | --- | --- |
| Potencias iniciales | 0 | 0 | 8 | 8 |
| Cotas C3 | 4 | 0 | 1 | 5 |
| E05–E08 | 5 | 0 | 4 | 9 |
| Detector H | 4 | 1 | 7 | 12 |
| Ensamblaje S | 3 | 0 | 3 | 6 |
| Ensamblaje T+1 | 3 | 2 | 4 | 9 |
| Cuadrado n² | 0 | 0 | 1 | 1 |
| Cierre E10 | 1 | 2 | 2 | 5 |
| Resto | 22 | 11 | 38 | 71 |


Además se ejecutó el verificador independiente de A.9: vuelve a analizar las filas, cuenta los operadores mediante dos recorridos y compara simbólicamente los **50 miembros** del sistema con una especificación polinómica separada del DAG. El verificador original de C3, escrito en JavaScript, también se ejecutó sin cambios: devolvió 42/16/68, 25 comparaciones, 37 testigos, 21 ecuaciones preservadas y cero registros muertos. Las dos implementaciones no deducen la distribución de operadores del total declarado.

### A.7 Cobertura de ecuaciones {#apendice-a-7}

[R] `lhs` y `rhs` indican entradas o registros finales, sin aritmética adicional. «Registros» enumera el cono de dependencias completo de cada igualdad, en orden topológico. Su unión es exactamente el conjunto de las 126 salidas de A.5. No se calcula un residuo `lhs-rhs`: se comparan los valores directamente.

| ecuación | lhs | rhs | registros | comparación final |
| --- | --- | --- | --- | --- |
| S126-E01 | `b` | `t16` | t15, t16 | `b == t16` |
| S126-E02 | `t147` | `t4` | t4, t147 | `t147 == t4` |
| S126-E03 | `t148` | `t4` | t4, t148 | `t148 == t4` |
| S126-E04 | `t149` | `q` | t149 | `t149 == q` |
| S126-E05 | `t20` | `t19` | t1, t2, t3, t4, t6, t18, t19, t20 | `t20 == t19` |
| S126-E06 | `t22` | `t3` | t1, t2, t3, t21, t22 | `t22 == t3` |
| S126-E07 | `ell` | `t24` | t23, t24 | `ell == t24` |
| S126-E08 | `e` | `t26` | t25, t26 | `e == t26` |
| S126-E09 | `n` | `t9` | t4, t6, t8, t9 | `n == t9` |
| S126-E10 | `r` | `t59` | t1, t2, t3, t4, t5, t6, t8, t18, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59 | `r == t59` |
| S126-E11 | `p` | `t65` | t54, t60, t61, t62, t64, t65 | `p == t65` |
| S126-E12 | `t70` | `t71` | t66, t67, t68, t69, t70, t71 | `t70 == t71` |
| S126-E13 | `c` | `t74` | t54, t60, t73, t74 | `c == t74` |
| S126-E14 | `k` | `t77` | t77 | `k == t77` |
| S126-E15 | `k` | `t81` | t78, t79, t80, t81 | `k == t81` |
| S126-E16 | `t62` | `t84` | t54, t60, t61, t62, t63, t84 | `t62 == t84` |
| S126-E17 | `c` | `t87` | t78, t85, t86, t87 | `c == t87` |
| S126-E18 | `d` | `t95` | t88, t89, t90, t91, t92, t93, t94, t95 | `d == t95` |
| S126-E19 | `t101` | `t100` | t96, t97, t98, t99, t100, t101 | `t101 == t100` |
| S126-E20 | `t106` | `t105` | t96, t97, t98, t102, t103, t104, t105, t106 | `t106 == t105` |
| S126-E21 | `t109` | `t119` | t78, t85, t101, t106, t107, t108, t109, t110, t111, t112, t113, t114, t115, t116, t117, t118, t119 | `t109 == t119` |
| S126-E22 | `C1` | `t131` | t129, t130, t131 | `C1 == t131` |
| S126-E23 | `t135` | `t134` | t96, t97, t132, t133, t134, t135 | `t135 == t134` |
| S126-E24 | `D1` | `t144` | t136, t137, t138, t139, t140, t142, t143, t144 | `D1 == t144` |
| S126-E25 | `r` | `t146` | t146 | `r == t146` |


### A.8 Dependencias compartidas {#apendice-a-8}

[R] La siguiente lista es exhaustiva para los registros que pertenecen al cono de **más de una ecuación**. La expresión de cada registro está definida en A.5; se incluyen tanto reutilizaciones directas como transitivas.

| registro / subexpresión definida en A.5 | ecuaciones que lo usan (directa o transitivamente) |
| --- | --- |
| `t1` | E05, E06, E10 |
| `t2` | E05, E06, E10 |
| `t3` | E05, E06, E10 |
| `t4` | E02, E03, E05, E09, E10 |
| `t6` | E05, E09, E10 |
| `t8` | E09, E10 |
| `t18` | E05, E10 |
| `t54` | E10, E11, E13, E16 |
| `t60` | E11, E13, E16 |
| `t61` | E11, E16 |
| `t62` | E11, E16 |
| `t78` | E15, E17, E21 |
| `t85` | E17, E21 |
| `t96` | E19, E20, E23 |
| `t97` | E19, E20, E23 |
| `t98` | E19, E20 |
| `t101` | E19, E21 |
| `t106` | E20, E21 |


Por ejemplo, `t4=q*q` verifica las dos cotas E02–E03, alimenta `t6=q^4` y participa en el ensamblaje de E10. `t54=n*n` sirve a E10 y a la infraestructura de E11, E13 y E16. `t97=A*A-1` se comparte entre E19, E20 y E23. Ninguno se vuelve a calcular por cada uso.

Si se sumaran los tamaños de los 25 conos por separado, se contarían **157** operaciones, repitiendo esas dependencias. La unión de los conos contiene 126 nodos. El coste certificado es el del DAG global, no la suma de costes de evaluaciones independientes de cada ecuación.

### A.9 QA reproducible {#apendice-a-9}

[R] Se ejecutaron los tres verificadores originales, extraídos de los bloques JavaScript de C1, C2 y C3, con sus respectivos expedientes como entrada. C1 confirmó 130 operaciones y las identidades de su selector; C2 confirmó 128 operaciones y la preservación de 20 ecuaciones; C3 confirmó las 126 operaciones finales y la preservación de las 21 ecuaciones ajenas a su sustitución. Estos datos sólo documentan la concordancia entre expedientes; no se incorporan circuitos anteriores al certificado final.

Se contrastaron además las referencias internas de los verificadores con los expedientes efectivos: las 130 instrucciones y 21 comparaciones de C1 coinciden exactamente con la base incorporada por C2; las 128 instrucciones y 22 comparaciones de C2 coinciden exactamente con la base incorporada por C3. No se detectaron discrepancias de ecuaciones, operaciones ni dominios en esa cadena.

El contraste documental con el informe final confirma el dominio positivo, las 37 incógnitas, las 25 ecuaciones, los parámetros admisibles, la normalización y el desglose 42/16/68. La palabra «provisional» del expediente C3 describe su estado antes del cierre: el informe final lo congela como S126. El informe escribe $\phi$ donde C3 escribe $\varphi$; aquí se mantiene `varphi`, el identificador del DAG. Para evitar colisiones de notación, se escribe $\Delta_b=2Ab-b^2-1$ en el selector y se deja $A^2-1$ explícito en las normas. Son aclaraciones de nombres, no modificaciones de ecuaciones.

| comprobación | resultado ejecutado o contraste documental |
| --- | --- |
| DAG acíclico y orden topológico | PASS; cada operando está disponible antes de usarse |
| Dependencias y nombres de salida | PASS; sin redefiniciones ni referencias adelantadas |
| Nodos operacionales | PASS; exactamente 126 |
| Distribución de operadores | PASS; 42 sumas, 16 restas, 68 productos |
| Comparaciones finales | PASS; exactamente 25 |
| Entrada, parámetros y testigos | PASS; 1 + 3 + 37; todos utilizados |
| Símbolos operacionales huérfanos | PASS; ninguno |
| Registros muertos | PASS; ninguno; los 126 llegan a una comparación |
| Cobertura | PASS; 25 conos calculados y comparados con A.7 |
| Doble cómputo | PASS; 126 salidas distintas, cada una pagada una vez |
| Especificación algebraica | PASS; igualdad polinómica exacta de los 50 miembros |
| Consumidores de A.5 | PASS; listas reconstruidas desde operandos y comparaciones |
| C1/C2/C3 | PASS; verificadores originales ejecutados; transformaciones y pruebas conservadas |
| Informe final | Conforme en interfaz, admisibilidad y presupuesto; contraste textual |
| Formalización de la prueba lógica | No realizada; prueba escrita de A.4 con dependencias publicadas explícitas |

#### Verificador independiente del propio apéndice

Guardar el bloque siguiente como `verify_certificate.py` y ejecutar:

```bash
python3 verify_certificate.py S126_REPRODUCIBLE_CERTIFICATE_v01.md
```

Sólo requiere Python 3 y su biblioteca estándar. No genera testigos ni prueba automáticamente los lemas de A.4. Analiza las tablas publicadas, comprueba su estructura y expande polinomios exactamente sobre $\mathbb Z$; no emplea muestreo numérico.

```python
"""Python 3, biblioteca estándar. Uso: python3 verify_certificate.py certificado.md"""
import ast
import collections
import json
import re
import sys
from pathlib import Path

# Polinomios dispersos sobre Z. Monomio: tupla ordenada (variable, exponente).
class Poly:
    def __init__(self, terms):
        self.terms = {m: c for m, c in terms.items() if c}
    @staticmethod
    def cast(x):
        return x if isinstance(x, Poly) else Poly({(): x})
    @staticmethod
    def var(name):
        return Poly({((name, 1),): 1})
    def __add__(self, other):
        other = Poly.cast(other)
        d = dict(self.terms)
        for m, c in other.terms.items():
            d[m] = d.get(m, 0) + c
        return Poly(d)
    __radd__ = __add__
    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})
    def __sub__(self, other):
        return self + -Poly.cast(other)
    def __rsub__(self, other):
        return Poly.cast(other) + -self
    def __mul__(self, other):
        other = Poly.cast(other)
        d = collections.defaultdict(int)
        for m, c in self.terms.items():
            for n, e in other.terms.items():
                powers = dict(m)
                for v, h in n:
                    powers[v] = powers.get(v, 0) + h
                d[tuple(sorted(powers.items()))] += c * e
        return Poly(d)
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        r = Poly.cast(1)
        for _ in range(n):
            r = r * self
        return r
    def __eq__(self, other):
        return self.terms == Poly.cast(other).terms

def expression(text, env):
    def walk(node):
        if isinstance(node, ast.Name):
            return env[node.id]
        if isinstance(node, ast.Constant):
            assert type(node.value) is int
            return node.value
        if isinstance(node, ast.BinOp):
            a, b = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add): return a + b
            if isinstance(node.op, ast.Sub): return a - b
            if isinstance(node.op, ast.Mult): return a * b
            if isinstance(node.op, ast.Pow): return a ** b
        raise ValueError(ast.dump(node))
    return Poly.cast(walk(ast.parse(text, mode='eval').body))

md = Path(sys.argv[1]).read_text()
dag = md.split('## A.5 ')[1].split('## A.6 ')[0]
coverage = md.split('## A.7 ')[1].split('## A.8 ')[0]
ops = []
for row in dag.splitlines():
    if not re.match(r'^\| I\d{3} \|', row): continue
    fields = [s.strip() for s in row.strip('|').split('|')]
    ident, op, operands, out, uses, accumulated = fields
    a, b = re.fullmatch(r'`(\w+)`, `(\w+)`', operands).groups()
    reg = out.strip('`')
    assert op in '+-*'
    assert ident == 'I%03d' % (len(ops)+1)
    assert int(accumulated) == len(ops)+1
    ops.append((reg, a, op, b, uses))
cs = []
for row in coverage.splitlines():
    if not row.startswith('| S126-E'): continue
    ident, a, b, regs, comparison = [s.strip() for s in row.strip('|').split('|')]
    assert ident == 'S126-E%02d' % (len(cs)+1)
    a, b = a.strip('`'), b.strip('`')
    assert comparison == f'`{a} == {b}`'
    cs.append((a, b, set(regs.split(', ')) if regs else set()))

inputs = 'x z u y b e g ell m n q r t w alpha lambda theta p s k tau eta h0 A c varphi d gamma f i j omega C1 D1 J nu rho zeta eps_e eps_l eps_g'.split()
assert len(inputs) == len(set(inputs)) == 41
env = {v: Poly.var(v) for v in inputs + ['E']}
env.update({str(n): Poly.cast(n) for n in [1, 2, 4, 5]})
orig = dict(env)
ancestors = {}; consumers = collections.defaultdict(list)
counts = collections.Counter()
for index, (reg, a, op, b, uses) in enumerate(ops, 1):
    assert reg not in env and a in env and b in env
    counts[op] += 1
    env[reg] = (env[a] + env[b] if op == '+' else
                env[a] - env[b] if op == '-' else env[a] * env[b])
    ancestors[reg] = {reg} | ancestors.get(a, set()) | ancestors.get(b, set())
    for v in set([a, b]): consumers[v].append('I%03d' % index)
live = set()
for index, (a, b, listed) in enumerate(cs, 1):
    assert a in env and b in env
    actual = ancestors.get(a, set()) | ancestors.get(b, set())
    assert listed == actual, ('coverage', index)
    live |= actual
    for v in set([a, b]): consumers[v].append('E%02d' % index)
assert len(ops) == len(ancestors) == len(live) == 126
assert len(cs) == 25
assert counts == {'+': 42, '-': 16, '*': 68}
assert all(consumers[v] for v in orig), 'unused input/constant'
for reg, a, op, b, uses in ops:
    assert uses == ', '.join(consumers[reg]), ('consumers', reg)

# Segunda cuenta por filas, independiente del Counter acumulado en la evaluación.
independent = {op: sum(row[2] == op for row in ops) for op in '+-*'}
assert independent == {'+': 42, '-': 16, '*': 68}
assert sum(independent.values()) == 126

# Especificación polinómica independiente del DAG, transcripción de A.3.
definitions = {
    'beta': 'b**5', 'C0': '1+x*b**5+g',
    'H': '2*(e-z*lambda)*C0**4+lambda*beta*(1+q**4)',
    'S': 'g+e*q**3+ell*q**5+H*q**7',
    'Tp': 'q**3-b*ell+ell+theta*lambda*q**3+(beta-2)*q**8',
    'M': 'r*s*n**2', 'V': 'A-M', 'U': 'w*n**2'
}
# lambda es palabra reservada de Python; se renombra solo en el analizador.
def parse(text, scope):
    return expression(re.sub(r'\blambda\b', 'lam', text),
                      {('lam' if k == 'lambda' else k): v for k,v in scope.items()})
for k, text in definitions.items(): orig[k] = parse(text, orig)
equations = [
    ('b','x*y+alpha'), ('e+eps_e','q**2'),
    ('ell+eps_l','q**2'), ('g+eps_g','q'),
    ('lambda+q**4','1+lambda*beta'), ('theta+2*z','beta'),
    ('ell','u+t*theta'), ('e','y+m*theta'), ('n','q**16'),
    ('r','S*(n**2-n)+Tp*(n**2-1)'), ('p','2*M*V'),
    ('(p**2-1)*k**2+1','tau**2'), ('c','k*s*n**2+zeta'),
    ('k','zeta+eta'), ('k','r+1+h0*(p-1)'), ('V','M*U'),
    ('c','2*r+1+C1+varphi'), ('d','b*w+c*(A-2)+(4*A-5)*gamma'),
    ('d**2','(A**2-1)*c**2+1'), ('f**2','(A**2-1)*(i*c**2)**2+1'),
    ('(d+omega*f)**2','((A+f**2*(d**2-A))**2-1)*(2*r+1+j*c)**2+1'),
    ('C1','E+J*(A-1)'), ('D1**2','(A**2-1)*C1**2+1'),
    ('D1','q+C1*(A-b)+nu*(2*A*b-b**2-1)'), ('r','n+rho')
]
for index, ((a,b,_),(lhs,rhs)) in enumerate(zip(cs,equations),1):
    assert env[a] == parse(lhs,orig), ('lhs',index)
    assert env[b] == parse(rhs,orig), ('rhs',index)
assert len(equations) == 25
print(json.dumps({'status':'PASS','operations':len(ops),'count':dict(counts),
 'independent_count':independent,'comparisons':len(cs),'witnesses':37,
 'live_registers':len(live),'exact_polynomial_sides':50,
 'topological':True,'coverage':True,'consumer_lists':True}, indent=2))

```

Salida obtenida:

```json
{
  "status": "PASS",
  "operations": 126,
  "count": {"*": 68, "+": 42, "-": 16},
  "independent_count": {"+": 42, "-": 16, "*": 68},
  "comparisons": 25,
  "witnesses": 37,
  "live_registers": 126,
  "exact_polynomial_sides": 50,
  "topological": true,
  "coverage": true,
  "consumer_lists": true
}
```

#### Expedientes utilizados y trazabilidad

Los expedientes se leyeron íntegramente. Las huellas corresponden a las copias textuales UTF-8 utilizadas en esta ejecución, reconstruidas de la lectura íntegra; no se presentan como huellas de los archivos binarios originales.

| expediente (texto leído íntegro) | SHA-256 del texto local UTF-8 |
| --- | --- |
| `C1_SELECTOR_EXPONENCIAL.md` | 5b8fc89e60356a859918f33703d8f6255497e6d503097220627c44e33872cc0e |
| `C2_PELL_BINOMIAL.md` | fecc3845a64e3d1f54e7d8fdd414d68399e75422ae4d57f76dcc045259373085 |
| `C3_MASCARAS_CODIFICACION.md` | a152fc4219c9aac88c85c631010c058180f47bf74d5828c01b916991d598b981 |
| `OUC_GENERATION1_FINAL_REPORT_v01.md` | 82e5e1dfa5aee22962cb1abd7ee561996338109f730cf79946667dfb8b6d67f8 |
| `Texto pegado(2).txt` | c878dee2f01041acae06b053bdc713d547a447f2bba360445223c4cfedc9248a |


- **[C1]** `C1_SELECTOR_EXPONENCIAL.md`, §§1–3, sistema y verificador: selector final, dominios y completitud positiva.
- **[C2]** `C2_PELL_BINOMIAL.md`, §§1–3, §9 y verificador: ventana lineal y prueba contextual de suficiencia.
- **[C3]** `C3_MASCARAS_CODIFICACION.md`, §§1, 3–4 y apéndices B–C: cotas positivas, corrección de estimaciones, DAG final y comparaciones.
- **[F]** `OUC_GENERATION1_FINAL_REPORT_v01.md`, §§3–4 y cierre: estado canónico y alcance lógico/aritmético.
- **[S0]** `S146_CERTIFICADO_v1.0.md`, contenido en `Texto pegado(2).txt`, §§1–6: fuente normalizada, índice admisible y dependencias publicadas de la completitud. Se utilizan únicamente esas dependencias; no se trasladan sus ecuaciones ni sus cotas auxiliares corregidas posteriormente por C3.
- **[P]** James P. Jones, “Universal Diophantine Equation”, *The Journal of Symbolic Logic* **47**(3), 1982, pp. 549–571. Referencias internas utilizadas: lemas 2.7–2.9, 2.11, 2.16, 2.18, 2.20, 2.22–2.26, corolario 2.29 y §4, según los expedientes auditados. No se realizó nueva búsqueda histórica.

### A.10 Alcance {#apendice-a-10}

[R] Este apéndice certifica **S126**: el sistema final de 25 ecuaciones con 37 testigos positivos, su equivalencia lógica bajo los parámetros admisibles y su verificador aritmético explícito de 126 operaciones bajo $\mathcal C_{\rm proj}$.

No reconstruye el circuito histórico de Jones ni identifica automáticamente $o_{\rm proj}$ con la convención histórica de $o_{\rm Jones}$. No prueba optimalidad, no convierte 126 en una cota inferior y no formaliza toda la demostración en Lean, Coq o Isabelle. [A] El mínimo bajo una convención operacional fijada permanece sin determinar. «VERIFIED» designa las comprobaciones ejecutadas y el alcance documental y matemático explicitado en A.4 y A.9; no designa una formalización completa en un asistente de pruebas.

$$
\boxed{\texttt{S126-REPRO v1.0 — VERIFIED}}
$$


## Bibliografía {#bibliografia}

### Fuentes publicadas

- **Hatcher, William S.; Hodgson, Bernard R.** «Complexity Bounds on Proofs». *The Journal of Symbolic Logic* **46**(2), 1981, pp. 255–258. [DOI](https://doi.org/10.2307/2273619).
- **Jones, James P.** «Three Universal Representations of Recursively Enumerable Sets». *The Journal of Symbolic Logic* **43**(2), 1978, pp. 335–351. [DOI](https://doi.org/10.2307/2272832).
- **Jones, James P.** «Diophantine Representation of Mersenne and Fermat Primes». *Acta Arithmetica* **35**(3), 1979, pp. 209–221. [DOI](https://doi.org/10.4064/aa-35-3-209-221).
- **Jones, James P.** «Undecidable Diophantine Equations». *Bulletin of the American Mathematical Society*, nueva serie, **3**(2), 1980, pp. 859–862. [DOI](https://doi.org/10.1090/S0273-0979-1980-14832-6).
- **Jones, James P.** «Universal Diophantine Equation». *The Journal of Symbolic Logic* **47**(3), 1982, pp. 549–571. [DOI](https://doi.org/10.2307/2273588).
- **Jones, James P.; Matiyasevich, Yuri V. (1982a).** «A New Representation for the Symmetric Binomial Coefficient and Its Applications». *Annales des sciences mathématiques du Québec* **6**(1), 1982, pp. 81–97. [Texto](https://www.labmath.uqam.ca/~annales/volumes/06-1/PDF/081-097.pdf).
- **Jones, James P.; Matiyasevich, Yuri V. (1982b).** «Exponential Diophantine Representation of Recursively Enumerable Sets». En J. Stern (ed.), *Logic Colloquium ’81*, *Studies in Logic and the Foundations of Mathematics* **107**, North-Holland, 1982, pp. 159–177. [Ficha editorial](https://www.sciencedirect.com/science/article/pii/S0049237X08718822).
- **Matiyasevich, Yuri V.** «Diophantine Representation of Enumerable Predicates». *Mathematics of the USSR-Izvestiya* **5**(1), 1971, pp. 1–28. [DOI](https://doi.org/10.1070/IM1971v005n01ABEH001004).
- **Matiyasevich, Yuri V.; Robinson, Julia.** «Reduction of an Arbitrary Diophantine Equation to One in 13 Unknowns». *Acta Arithmetica* **27**, 1975, pp. 521–553. [DOI](https://doi.org/10.4064/aa-27-1-521-553).
- **Schwarz, Wolfgang.** *Logic, Computability, and Incompleteness*, capítulo 5, «Computability». Material docente en línea, sin fecha consignada. [Texto](https://www.wolfgangschwarz.net/logic3/05-computability.html).

### Documentación técnica propia

Los siguientes expedientes son documentos de trabajo y certificación propios, no publicaciones históricas. Sus nombres se conservan como identificadores de trazabilidad.

- **`OUC_GENERATION1_FINAL_REPORT_v01.md`**, OUC-G1 v1.0, 3 de octubre de 2026. Informe rector de cierre: genealogía, teorema lógico, costes, resultados locales, límites y auditoría final.
- **`C1_SELECTOR_EXPONENCIAL.md`**. Selector exponencial y equivalencia contextual.
- **`C2_PELL_BINOMIAL.md`**. Ventana lineal y certificación dentro del bloque Pell/binomial.
- **`C3_MASCARAS_CODIFICACION.md`**. Cotas positivas, sistema S126, DAG y verificador simbólico.
- **`OUC_EXP01_PACKED_RECURRENCE.md`**. Certificación de recurrencias empaquetadas.
- **`OUC_EXP02_AMORTIZED_PACKING.md`**. Infraestructura compartida y fórmulas de coste.
- **`OUC_EXP03_POWER_BACKBONE.md`**. Certificación conjunta de potencias y variante de reloj.
- **`OUC_EXP04A_UNIVERSAL_INTEGRATION.md`**. Obligaciones de integración de una computación universal.
- **`OUC_EXP05_PACKED_PELL.md`**. Integración del empaquetado y selector Pell condicionado.
- **`OUC_EXP06_HYPOTHESIS_ABSORPTION.md`**. Absorción de la condición de crecimiento.
- **`OUC_EXP07_MODULAR_POWER.md`**. Obligación de potencia modular y alcance de las estrategias examinadas.
- **`OUC_EXP08_INDEX_SELECTOR.md`**. Selección de índices y primer fingerprint.
- **`OUC_EXP08B_ALIAS_KILLING.md`**. Segundo fingerprint, familias de alias y contraejemplo $(5,3,195)$.
- **`OUC_EXP09_TERMINAL_SCREEN.md`**. Cribado final de arquitecturas y cierre de la primera generación.
- **`S126_REPRODUCIBLE_CERTIFICATE_v01.md`**, S126-REPRO v1.0: sistema, prueba escrita, DAG y verificador independiente; reproducido en el Apéndice A.

[Descargar las fuentes canónicas, el certificado S126-REPRO y su verificador](../assets/articles/ma-art-0013/S126_REPRO_v1.0.zip).

