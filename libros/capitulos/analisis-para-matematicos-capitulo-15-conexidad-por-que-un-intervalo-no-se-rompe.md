---
content-id: MA-BCH-0262
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-015
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: 'Capítulo 15 — Conexidad: por qué un intervalo no se rompe'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C15.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-15)

En cálculo usamos el valor intermedio para asegurar que una función alcanza una altura entre dos alturas conocidas. Aquí demostraremos el mecanismo que lo sostiene: una continuidad local no puede romper la indivisibilidad de un intervalo. La geometría de la recta permitirá traducir la ausencia de separaciones en ausencia de huecos.

Partimos de abiertos y orden de C04 y continuidad de C14, con las interfaces heredadas de completitud de C00, convergencia de C06 y tipos de C12. Primero probaremos conexidad mediante supremo; después la transportaremos por continuidad y deduciremos el valor intermedio. Bisección añadirá encierros y cotas de posición. Las últimas secciones usarán el orden para controlar inversas y describir componentes. No se presupone compacidad ni derivadas. Los reales se tratan con lógica clásica; la recurrencia de bisección no promete evaluación computable de toda función.

## 15.1. Qué tendría que hacer una separación

[]{#MA-SEC-ANM-01-015-001}

¿Qué significa que un conjunto tenga dos partes? Todo intervalo puede dividirse, por ejemplo, en puntos menores que cero y puntos mayores o iguales que cero. Esa partición no prueba que esté roto: en el punto cero, la segunda parte no tiene una vecindad relativa libre de la primera. Buscamos una partición cuyas dos partes se protejan localmente.

**Definición.** Una separación de $E\subseteq\mathbb R$ es un par $A,B\subseteq E$ que satisface simultáneamente

$$A\ne\varnothing,\quad B\ne\varnothing,\quad A\cap B=\varnothing,
\quad E=A\cup B,$$

con $A$ y $B$ abiertos relativos a $E$. Diremos que $E$ es **conexo** cuando no admite ninguna separación. Según C14, $A$ es abierto relativo a $E$ si $A=E\cap U$ para algún abierto real $U$; equivalentemente, para cada $a\in A$ existe $r>0$ con $E\cap(a-r,a+r)\subseteq A$. El radio protege sólo entradas que pertenecen a $E$.

La definición no exige que las partes sean abiertas en toda la recta. En $E=[-2,-1]\cup[1,2]$, los conjuntos $A=[-2,-1]=E\cap(-\infty,0)$ y $B=[1,2]=E\cap(0,\infty)$ forman una separación. No son abiertos reales, pero sí relativos. En $[-1,1]$, en cambio, la partición $[-1,0)$ y $[0,1]$ falla: para cualquier $r>0$, el punto $-\min(r/2,1/2)$ pertenece al intervalo y a la primera parte, y está a distancia menor que $r$ de cero. Por ello $[0,1]$ no es abierto relativo a $[-1,1]$.

![Arriba, los dos segmentos se separan por el corte 0. Abajo, asignar 0 a la parte derecha de un intervalo no la protege de entradas negativas próximas. La banda representa una vecindad ilustrativa; el texto prueba el fallo para todo radio.](../../assets/books/anm/C15/C15-F01.svg){#fig-anm-c15-f01 fig-alt="Arriba, los dos segmentos se separan por el corte 0. Abajo, asignar 0 a la parte derecha de un intervalo no la protege de entradas negativas próximas. La banda representa una vecindad ilustrativa; el texto prueba el fallo para todo radio."}

**R1. Criterio de una sola parte.** $E$ es conexo si y sólo si sus únicos subconjuntos simultáneamente abiertos y cerrados relativos son $\varnothing$ y $E$.

La estrategia consiste en recuperar la otra parte por complemento. Si $A\subseteq E$ es abierto y cerrado relativo, $B=E\setminus A$ es abierto relativo. Si $A$ no es vacío ni todo $E$, ambas partes son no vacías, disjuntas y exhaustivas: una separación. En un conexo eso es imposible. En la otra dirección, si existiera una separación $A,B$, su disjunción y cobertura darían $B=E\setminus A$. Así $A$ sería abierto relativo y, por apertura de su complemento, cerrado relativo; sería además no vacío y propio. Contradice el criterio. Quedan probadas ambas implicaciones.

El vacío es conexo porque no admite partes no vacías. Un singleton es conexo porque sus únicos subconjuntos son el vacío y él mismo. No hay que decidir si el singleton es abierto en la recta: aquí el ambiente es el conjunto dado.

La negación de conexidad exige exhibir una separación completa; la afirmación exige excluirlas todas. Un dibujo con dos colores es una conjetura hasta justificar apertura, no vacuidad, disjunción y cobertura. Una partición puede fallar sólo en un punto de frontera, y ese fallo basta para impedir que sea una separación.

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-015-001}

¿Qué cuatro condiciones conjuntistas acompañan la apertura relativa en una separación?

[]{#MA-MSOL-ANM-01-015-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

No vacuidad de ambas partes, disjunción, cobertura del conjunto y pertenencia de las partes al conjunto ambiente. Junto a la apertura relativa, se escriben $A,B\subseteq E$, $A,B\ne\varnothing$, $A\cap B=\varnothing$, $A\cup B=E$.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-015-002}

¿Por qué $[-2,-1]$ puede ser una parte abierta relativa de $[-2,-1]\cup[1,2]$?

[]{#MA-MSOL-ANM-01-015-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Es la intersección del ambiente con el abierto real $(-\infty,0)$. La apertura se mide dentro del ambiente, aunque el segmento no sea abierto real.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-015-003}

¿Dónde falla la partición $[-1,0)$ y $[0,1]$ de $[-1,1]$?

[]{#MA-MSOL-ANM-01-015-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

La segunda parte no es abierta relativa en cero: dado $r>0$, $-\min(r/2,1/2)$ pertenece al ambiente, dista menos que $r$ de cero y no pertenece a $[0,1]$.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-015-004}

¿Qué complemento convierte una parte abierta y cerrada relativa en una separación candidata?

[]{#MA-MSOL-ANM-01-015-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

$E\setminus A$. Si $A$ es propia y no vacía, el complemento también es no vacío; la cerradura relativa de $A$ significa que ese complemento es abierto relativo. Disjunción y cobertura son identidades de complementos.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-015-005}

¿El vacío es conexo bajo la definición adoptada?

[]{#MA-MSOL-ANM-01-015-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Sí. Toda parte del vacío es vacía, y no pueden existir las dos partes no vacías exigidas por una separación.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-015-006}

¿Hace falta que un singleton sea abierto real para probar que es conexo?

[]{#MA-MSOL-ANM-01-015-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

No. Sus únicos subconjuntos son el vacío y él mismo; no admite dos partes disjuntas no vacías. La apertura real del singleton no interviene.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-015-007}

¿Basta dibujar una partición de dos colores para negar conexidad?

[]{#MA-MSOL-ANM-01-015-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

No. Hay que demostrar apertura relativa de ambas partes y verificar no vacuidad, disjunción y cobertura. Una frontera mal asignada puede impedir la apertura de una parte.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-015-008}

¿Qué niega exactamente la afirmación «$E$ es conexo»?

[]{#MA-MSOL-ANM-01-015-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

Niega la existencia de cualquier par que satisfaga todas las condiciones de separación; no niega la existencia de particiones arbitrarias. Un intervalo sí admite particiones, pero ninguna con ambas partes abiertas relativas y no vacías.

</details>

### Ejercicios de la sección 15.1

[]{#ejercicios-15}

#### Ejercicio 1. Una separación relativa verificable

[]{#MA-EX-ANM-01-015-001}

Sea $E=[-3,-1]\cup[2,4]$. Construye una separación por un corte y comprueba todas las condiciones, distinguiendo apertura relativa de apertura real.

[]{#MA-SOL-ANM-01-015-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Tomamos $A=E\cap(-\infty,0)=[-3,-1]$ y $B=E\cap(0,\infty)=[2,4]$. Los rayos son abiertos reales, así las partes son abiertas relativas a $E$. $-2\in A$ y $3\in B$ prueban no vacuidad. Las desigualdades $x<0$ y $x>0$ son incompatibles, dando disjunción; todo punto de $E$ está en uno de los segmentos y por ello en una parte, dando cobertura. Ninguno de los segmentos es abierto real: cualquier bola alrededor de su extremo exterior contiene puntos que no pertenecen al segmento. El ambiente relativo es indispensable.

**Retorno visual.** Véase [C15-F01](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Una partición que no rompe el intervalo

[]{#MA-EX-ANM-01-015-002}

En $E=[0,2]$, examina $A=[0,1)$ y $B=[1,2]$. ¿Qué condición de separación falla? Da un testigo para cada radio en el punto problemático.

[]{#MA-SOL-ANM-01-015-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Ambas partes son no vacías, disjuntas y cubren $E$. Además $A=E\cap(-\infty,1)$ es abierta relativa. $B$ no lo es en $1$: dado $r>0$, ponemos $h=\min(r/2,1/2)>0$, $t=1-h$. Entonces $t\in[0,1)\subseteq E$, $|t-1|=h<r$ y $t\notin B$. Ningún radio de $1$ dentro de $E$ queda en $B$. Por eso la partición no es separación.

**Retorno visual.** Véase [C15-F01](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 3. Equivalencia por complemento

[]{#MA-EX-ANM-01-015-003}

Demuestra desde las definiciones que $E$ es conexo si y sólo si todo subconjunto abierto y cerrado relativo a $E$ es vacío o todo $E$. Incluye $E=\varnothing$.

[]{#MA-SOL-ANM-01-015-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Si $E$ es conexo y $A$ es abierto y cerrado relativo, $E\setminus A$ es abierto relativo. Si $A$ no fuese vacío ni todo $E$, las dos partes serían no vacías, disjuntas y exhaustivas, separando $E$. Luego $A=\varnothing$ o $A=E$. Recíprocamente, una separación $A,B$ da $B=E\setminus A$; la apertura de $B$ hace a $A$ cerrado relativo y la de $A$ ya está dada. Por no vacuidad de ambas partes $A$ es no vacío y propio, contradiciendo el criterio. Si $E$ es vacío, su único subconjunto es vacío y no puede existir separación; ambas afirmaciones se cumplen.

</details>

#### Ejercicio 4. Separar un conjunto finito

[]{#MA-EX-ANM-01-015-004}

Prueba que un subconjunto finito de $\mathbb R$ es conexo exactamente cuando tiene a lo sumo un punto. Para dos o más puntos, construye un corte sin invocar la caracterización por intervalos.

[]{#MA-SOL-ANM-01-015-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Vacío y singleton no pueden dividirse en dos partes disjuntas no vacías, luego son conexos. Si el conjunto finito tiene al menos dos puntos, se puede ordenar como $t_1<\cdots<t_m$ con $m\ge2$, usando repetidamente el menor de una lista finita por comparación. Sea $c=(t_1+t_2)/2$. No pertenece al conjunto porque está entre sus dos primeros puntos. Las partes $E\cap(-\infty,c)=\{t_1\}$ y $E\cap(c,\infty)$ son abiertas relativas, disjuntas y exhaustivas; contienen $t_1$ y $t_2$. Son una separación. Sólo se usó una lista finita y el orden real.

</details>

#### Ejercicio 5. Ambientes anidados

[]{#MA-EX-ANM-01-015-005}

Si $F\subseteq E\subseteq\mathbb R$ y $A$ es abierto relativo a $E$, prueba que $F\cap A$ es abierto relativo a $F$. Explica por qué restringir una separación de $E$ a $F$ puede no separar $F$.

[]{#MA-SOL-ANM-01-015-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Escribimos $A=E\cap U$ con $U$ abierto real. Como $F\subseteq E$, $F\cap A=F\cap U$, abierto relativo a $F$. Para una separación $A,B$ de $E$, sus intersecciones con $F$ siguen siendo abiertas relativas, disjuntas y exhaustivas. Pero alguna puede ser vacía: con $E=[-2,-1]\cup[1,2]$, sus dos segmentos como partes y $F=[1,2]$, la intersección de la primera parte con $F$ es vacía. Por ello no queda una separación de $F$.

</details>
## 15.2. El supremo impide romper un intervalo

[]{#MA-SEC-ANM-01-015-002}

**Definición.** Llamamos intervalo a todo $I\subseteq\mathbb R$ que contiene los puntos situados entre dos de sus puntos:

$$a,b\in I,\quad a\le b\quad\Longrightarrow\quad[a,b]\subseteq I.$$

Esta definición incluye vacío, singletons, semirrectas, la recta completa y todas las modalidades de extremos. No confunde intervalo con abierto ni con cerrado. Nuestra meta es demostrar conexidad sin usar valor intermedio: éste será una consecuencia posterior.

**R2. Todo intervalo real es conexo.** Supongamos una separación $I=A\cup B$. Hay dos puntos, uno en cada parte; son distintos. Intercambiando los nombres si hace falta, fijamos $a\in A$, $b\in B$, $a<b$. La propiedad intervalar da $[a,b]\subseteq I$.

Necesitamos localizar una frontera aunque no exista último punto de $A$. Por eso definimos

$$S=A\cap[a,b],\qquad c=\sup S.$$

$a\in S$ hace al conjunto no vacío y $b$ lo acota superiormente. La completitud real de C00 suministra $c$, con $a\le c\le b$. El intervalo vuelve a ser decisivo: $c\in I$. La cobertura obliga a que $c$ pertenezca a $A$ o a $B$, y la disjunción impide ambas cosas a la vez.

**Primer caso: $c\in A$.** Como $b\in B$, tenemos $c<b$. La apertura relativa de $A$ entrega un $r>0$ tal que $I\cap(c-r,c+r)\subseteq A$. Para avanzar sin salir del dominio tomamos

$$h=\min\left(\frac{b-c}{2},\frac r2\right)>0,\qquad d=c+h.$$

Entonces $c<d<b$, $d\in[a,b]\subseteq I$ y $|d-c|=h<r$. Resulta $d\in A\cap[a,b]=S$. Pero $d>c$ contradice que $c$ sea una cota superior. La elección del mínimo tiene un trabajo preciso: satisface a la vez la restricción de dominio y la de vecindad. Escribir simplemente $c+r/2$ no asegura que el punto quede antes de $b$.

**Segundo caso: $c\in B$.** Existe $s>0$ con $I\cap(c-s,c+s)\subseteq B$. El número $c-s/2<c$ no es cota superior de $S$, por minimalidad del supremo. Por tanto existe $t\in S$ con

$$c-s/2<t\le c.$$

Como $t\in A$ y $c\in B$, son distintos; así $0<c-t<s/2<s$. De aquí $t\in I\cap(c-s,c+s)\subseteq B$, en contradicción con $t\in A$. No suponemos que el supremo esté en $S$ ni construimos una sucesión de puntos de $S$: usamos un solo testigo para esta vecindad concreta.

![Esquemas de una separación supuesta, no ejemplos de separaciones existentes. Si c pertenece a A, un avance recortado por dominio y radio excede la cota. Si pertenece a B, un punto t de S entra en su vecindad. Distancias ilustrativas; las fórmulas de R2 son autoritativas.](../../assets/books/anm/C15/C15-F02.svg){#fig-anm-c15-f02 fig-alt="Esquemas de una separación supuesta, no ejemplos de separaciones existentes. Si c pertenece a A, un avance recortado por dominio y radio excede la cota. Si pertenece a B, un punto t de S entra en su vecindad. Distancias ilustrativas; las fórmulas de R2 son autoritativas."}

Ambos destinos posibles de la frontera llevan a contradicción. No puede existir separación. En vacío y singleton la supuesta separación ni siquiera proporciona los dos puntos iniciales, de modo que el resultado los incluye.

La prueba gastó tres hipótesis distintas: el orden/completitud ubicó $c$; el carácter intervalar lo mantuvo en el dominio y permitió avanzar dentro de él; la apertura relativa dio las vecindades incompatibles. Acotamos sólo el conjunto auxiliar $S$, aunque el intervalo original sea no acotado. Ninguna compacidad ni continuidad de una función intervino.

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-015-009}

¿Qué definición de intervalo incluye las semirrectas y el vacío?

[]{#MA-MSOL-ANM-01-015-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

La condición $a,b\in I$, $a\le b\Rightarrow[a,b]\subseteq I$. En el vacío no hay pares y la condición es vacía; en una semirrecta todo punto entre dos miembros satisface la misma desigualdad que define la semirrecta.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-015-010}

¿Por qué $S=A\cap[a,b]$ tiene supremo en la prueba R2?

[]{#MA-MSOL-ANM-01-015-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

Contiene $a$ y está acotado superiormente por $b$. La completitud real da un supremo para todo conjunto real no vacío acotado superiormente.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-015-011}

¿Dónde se usa que el dominio sea intervalo para ubicar la frontera $c$?

[]{#MA-MSOL-ANM-01-015-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

De $a\le c\le b$ y $a,b\in I$ se deduce $c\in[a,b]\subseteq I$. Sin esa inclusión la cobertura por las dos partes no permitiría asignar $c$ a una de ellas.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-015-012}

Si $c\in A$, ¿por qué $b-c$ es positivo?

[]{#MA-MSOL-ANM-01-015-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

$b\in B$ y la disjunción impiden $c=b$; además $c\le b$ por la cota del supremo. Por tanto $c<b$.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-015-013}

¿Qué dos controles satisface $h=\min((b-c)/2,r/2)$?

[]{#MA-MSOL-ANM-01-015-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Es positivo, no avanza hasta $b$ y es menor que $r$. Así $c+h$ pertenece al segmento original y a la vecindad relativa de $c$; ambas pertenencias son necesarias para concluir que está en $A$.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-015-014}

Si $c\in B$, ¿por qué existe $t\in S$ mayor que $c-s/2$?

[]{#MA-MSOL-ANM-01-015-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

El número $c-s/2<c$ no puede ser cota superior de $S$, pues $c$ es la menor cota superior. La negación de ser cota da un $t\in S$ con $t>c-s/2$, y $t\le c$ por ser $c$ cota.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-015-015}

¿Se supone en R2 que $c$ sea máximo de $S$?

[]{#MA-MSOL-ANM-01-015-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

No. Si $c$ está en $B$, ni siquiera pertenece a $S\subseteq A$. Se usa la aproximación por debajo del supremo, no la existencia de un máximo.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-015-016}

¿Se necesita compacidad del intervalo original para R2?

[]{#MA-MSOL-ANM-01-015-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

No. Se acota sólo el auxiliar $S$ entre dos puntos concretos. Supremo, propiedad intervalar y apertura relativa bastan, incluso para intervalos no acotados.

</details>

### Ejercicios de la sección 15.2

#### Ejercicio 6. Preparar un supremo legítimo

[]{#MA-EX-ANM-01-015-006}

En una separación hipotética $I=A\cup B$, con $a\in A$, $b\in B$, $a<b$, justifica existencia y localización de $c=\sup(A\cap[a,b])$. ¿Por qué puede hablarse de la parte que contiene $c$?

[]{#MA-SOL-ANM-01-015-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

$S=A\cap[a,b]$ contiene $a$ y todos sus elementos son menores o iguales que $b$. Completitud da $c=\sup S$. Como $a\in S$, $a\le c$; como $b$ es cota, $c\le b$. La hipótesis intervalar da $[a,b]\subseteq I$, luego $c\in I=A\cup B$. La cobertura asigna una parte y la disjunción impide que pertenezca a ambas. Sin intervalaridad, $c$ podría faltar en el dominio y no habría esa dicotomía.

</details>

#### Ejercicio 7. Reparar un avance fuera del dominio

[]{#MA-EX-ANM-01-015-007}

Una prueba toma, cuando $c\in A$, $d=c+r/2$ y afirma que $d\in A\cap[a,b]$ por apertura relativa. Señala la obligación ausente y repara el argumento con una fórmula explícita.

[]{#MA-SOL-ANM-01-015-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

La apertura relativa sólo garantiza pertenencia a $A$ de puntos de $I$ próximos a $c$. El punto $c+r/2$ puede superar $b$ y hasta salir de $I$; por ejemplo $c=0.9$, $b=1$, $r=1$ da $d=1.4$. En el argumento correcto, $c<b$ porque $b\in B$ y $c\in A$. Ponemos $h=\min((b-c)/2,r/2)>0$, $d=c+h$. Entonces $c<d<b$, $d\in[a,b]\subseteq I$ y $|d-c|<r$. La apertura da $d\in A$, luego $d\in S$, en contradicción con $d>\sup S$. La reparación usa por separado dominio y radio.

**Retorno visual.** Véase [C15-F02](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 8. La propiedad aproximante necesaria

[]{#MA-EX-ANM-01-015-008}

En el caso $c\in B$, desarrolla desde la definición de supremo la contradicción usando un radio $s>0$ de apertura relativa. No supongas que $c$ esté en $S$.

[]{#MA-SOL-ANM-01-015-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

$c-s/2<c$ no es cota superior de $S$, porque sería una cota menor que la menor cota superior $c$. Por negación de la condición de cota existe $t\in S$ con $t>c-s/2$. Además $t\le c$ pues $c$ sí es cota. Como $S\subseteq A$ y $c\in B$, la disjunción da $t\ne c$. Así $0<c-t<s/2<s$, y $t\in I$ pertenece a la vecindad de $c$ dentro de $I$, que está en $B$. Queda $t\in A\cap B$, contradicción. Sólo se usó un testigo para este radio.

</details>

#### Ejercicio 9. La completitud en el paso correcto

[]{#MA-EX-ANM-01-015-009}

Explica por qué el argumento del supremo no prueba conexidad de $\mathbb Q$ visto con su orden heredado. Exhibe una partición relativa que ilustre el fallo.

[]{#MA-SOL-ANM-01-015-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

El orden racional no garantiza un supremo racional para todo subconjunto racional no vacío acotado. Si se toma el supremo en $\mathbb R$, puede quedar fuera del dominio racional y la dicotomía «pertenece a una parte» falla. El corte $c=\sqrt2\notin\mathbb Q$ da las partes racionales menores y mayores que $c$. Son abiertas relativas, disjuntas, exhaustivas y no vacías por los testigos $1$ y $2$. La densidad racional no incorpora a $c$ ni subsana el gasto de completitud y pertenencia.

</details>

#### Ejercicio 10. Intervalos no acotados y degenerados

[]{#MA-EX-ANM-01-015-010}

Prueba que $(a,\infty)$, $\mathbb R$, $\{a\}$ y $\varnothing$ son conexos, indicando por qué R2 no necesita una cota global de todo el dominio.

[]{#MA-SOL-ANM-01-015-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

En la semirrecta, si $u\le v$ son miembros, todo $t\in[u,v]$ satisface $t\ge u>a$, así también pertenece. La recta contiene todos sus segmentos. Singleton y vacío satisfacen el predicado intervalar vacíamente o con segmentos degenerados. R2 los hace conexos. Su prueba acota sólo $S=A\cap[u,v]$ después de fijar dos puntos de una supuesta separación; no necesita acotar todo el intervalo. En vacío y singleton no hay dos puntos de partes disjuntas no vacías, de modo que la separación ya es imposible.

</details>
## 15.3. Un hueco produce dos lados

[]{#MA-SEC-ANM-01-015-003}

La implicación contraria será más corta, pero requiere una construcción distinta. Para negar que $E$ sea intervalo hay dos puntos $a<b$ de $E$ y un $c$ estrictamente entre ellos que no pertenece a $E$. No basta un punto ausente fuera del conjunto: debe quedar entre dos puntos presentes.

**R3. Todo conexo real es intervalo.** Por contraposición, dados $a<c<b$ con $a,b\in E$ y $c\notin E$, definimos

$$A=E\cap(-\infty,c),\qquad B=E\cap(c,\infty).$$

Los rayos son abiertos reales, luego las partes son abiertas relativas. Son no vacías, pues contienen $a$ y $b$ respectivamente. Son disjuntas por incompatibilidad de las desigualdades. Cubren $E$ porque ningún punto de $E$ es $c$ y la tricotomía da $x<c$ o $x>c$. Hemos comprobado las cuatro condiciones: $E$ no es conexo. Contraponiendo obtenemos el resultado.

![Se muestran sólo algunos racionales a ambos lados de √2. El corte irracional no pertenece al dominio; ambas partes son abiertas relativas y no vacías. Los puntos finitos ilustrados no representan una enumeración exhaustiva ni prueban densidad o desconexión.](../../assets/books/anm/C15/C15-F03.svg){#fig-anm-c15-f03 fig-alt="Se muestran sólo algunos racionales a ambos lados de √2. El corte irracional no pertenece al dominio; ambas partes son abiertas relativas y no vacías. Los puntos finitos ilustrados no representan una enumeración exhaustiva ni prueban densidad o desconexión."}

R2 y R3 producen la caracterización exacta

$$E\text{ conexo}\quad\Longleftrightarrow\quad E\text{ intervalo}.$$

En la recta, una condición formulada con vecindades equivale a una condición de orden. Esta equivalencia es específica del ambiente real que estudiamos. No la extendemos a espacios arbitrarios.

Por ejemplo, $\mathbb R\setminus\{0\}$ se separa mediante los dos rayos. $\mathbb Q$ también se separa: usando la raíz positiva algebraica $\sqrt2$, irracional por C10, tomamos $\{q\in\mathbb Q:q<\sqrt2\}$ y $\{q\in\mathbb Q:q>\sqrt2\}$. Contienen respectivamente $1$ y $2$, y cubren $\mathbb Q$. La densidad racional no rellena el corte: proporciona racionales próximos al punto omitido, pero nunca hace que ese punto sea racional. Densidad y conexidad responden a preguntas diferentes.

También hay que distinguir unión e intersección. Una intersección arbitraria de intervalos es intervalo: si contiene $a$ y $b$, cada intervalo de la familia contiene todo $[a,b]$, y por ello la intersección también. La intersección de una familia vacía se entiende aquí relativa a $\mathbb R$ y es $\mathbb R$. Una unión arbitraria puede tener huecos: $(0,1)\cup(2,3)$ no es intervalo.

Si dos intervalos tienen un punto común, su unión sí es intervalo. Para ver el mecanismo sin escoger orientaciones complicadas, supongamos una separación de la unión y restrinjámosla a cada intervalo. Cada intervalo, por R2, debe quedar enteramente en una de las partes: si tocara ambas, las intersecciones relativas lo separarían. El punto común obliga a que ambos estén en la misma parte, y entonces la otra parte es vacía. La contradicción prueba conexidad, y R3 vuelve a dar intervalo. El mismo razonamiento sirve para cualquier familia no vacía de conexos que comparte un punto: cada miembro queda en la parte que contiene ese punto. No se selecciona un punto por miembro, pues usamos el punto común ya fijado.

La condición de intersección es suficiente, no necesaria para toda unión conexa: $[0,1)\cup[1,2]=[0,2]$ es intervalo aunque las dos piezas sean disjuntas. Antes de diagnosticar un hueco hay que comprobar qué extremos están realmente presentes.

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-015-017}

¿Qué omisión permite construir un corte que separa un conjunto?

[]{#MA-MSOL-ANM-01-015-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Un $c\notin E$ situado estrictamente entre dos puntos $a<b$ de $E$. Una omisión fuera de todos sus puntos no asegura dos partes no vacías.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-015-018}

¿Por qué las partes $E\cap(-\infty,c)$ y $E\cap(c,\infty)$ cubren $E$?

[]{#MA-MSOL-ANM-01-015-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Como $c\notin E$, todo $x\in E$ es distinto de $c$. La tricotomía deja sólo $x<c$ o $x>c$.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-015-019}

¿Qué testigos aseguran la no vacuidad de ambos lados del corte?

[]{#MA-MSOL-ANM-01-015-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

Los puntos dados $a<c<b$: $a$ está en el lado izquierdo y $b$ en el derecho.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-015-020}

¿La densidad de $\mathbb Q$ implica su conexidad?

[]{#MA-MSOL-ANM-01-015-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

No. $\sqrt2$ es un punto real entre $1$ y $2$ que no es racional. Los racionales menores y mayores que ese corte forman una separación; aproximarse al corte no lo incluye en el dominio.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-015-021}

¿Por qué una intersección de intervalos es intervalo?

[]{#MA-MSOL-ANM-01-015-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

Si $a,b$ pertenecen a todos los miembros, cada miembro contiene $[a,b]$, luego la intersección también lo contiene. Si la intersección es vacía, la condición entre pares se cumple vacíamente.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-015-022}

¿Qué ocurre al unir $(0,1)$ y $(2,3)$?

[]{#MA-MSOL-ANM-01-015-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

La unión omite, por ejemplo, $3/2$ entre los puntos presentes $1/2$ y $5/2$. No es intervalo y por R3 no es conexa.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-015-023}

¿Por qué un punto común ayuda a unir dos conexos?

[]{#MA-MSOL-ANM-01-015-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

En una supuesta separación de la unión, cada conexo debe quedar en una sola parte. El punto común obliga a que ambos queden en la misma, dejando vacía la otra parte.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-015-024}

¿La intersección no vacía es necesaria para que dos intervalos tengan unión conexa?

[]{#MA-MSOL-ANM-01-015-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

No. $[0,1)$ y $[1,2]$ son disjuntos, pero su unión es $[0,2]$, que es intervalo y conexo. La condición de punto común es suficiente, no necesaria.

</details>

### Ejercicios de la sección 15.3

#### Ejercicio 11. Un punto omitido suficiente

[]{#MA-EX-ANM-01-015-011}

Para $E=[0,1]\cup(1,3]\setminus\{2\}$, interpreta los paréntesis como $E=([0,1]\cup(1,3])\setminus\{2\}$. Construye una separación. ¿Es $1$ otro hueco?

[]{#MA-SOL-ANM-01-015-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

La unión anterior a quitar $2$ es $[0,3]$, pues $1$ está en la primera pieza. Por tanto $E=[0,3]\setminus\{2\}$. Tomamos $A=E\cap(-\infty,2)=[0,2)$ y $B=E\cap(2,\infty)=(2,3]$. Son abiertas relativas por los rayos, disjuntas y cubren $E$ porque $2$ fue omitido. Son no vacías por $0$ y $3$. $1$ no es hueco: pertenece a $E$. Las modalidades de extremos de cada pieza no deben leerse aisladas de la unión.

</details>

#### Ejercicio 12. Densidad y ruptura

[]{#MA-EX-ANM-01-015-012}

Construye una separación de $\mathbb Q$ por un corte irracional y demuestra cada condición. Explica por qué las partes pueden tener puntos arbitrariamente próximos al corte.

[]{#MA-SOL-ANM-01-015-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Usamos $c=\sqrt2$, real irracional, y $A=\mathbb Q\cap(-\infty,c)$, $B=\mathbb Q\cap(c,\infty)$. Las partes son abiertas relativas, disjuntas y cubren los racionales por $c\notin\mathbb Q$. $1\in A$, $2\in B$. Para todo $r>0$, densidad racional da un punto en $(c-r,c)$ y otro en $(c,c+r)$, pertenecientes a las partes respectivas. Aproximación arbitraria al corte es compatible con separación: el punto límite común está fuera del ambiente racional.

**Retorno visual.** Véase [C15-F03](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 13. Intersecciones y uniones

[]{#MA-EX-ANM-01-015-013}

Demuestra que toda intersección de intervalos reales es conexa, con la convención de intersección vacía igual a $\mathbb R$. Refuta la afirmación análoga para uniones arbitrarias.

[]{#MA-SOL-ANM-01-015-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Si $x,y$ pertenecen a la intersección, están en cada intervalo de la familia, y el segmento entre ellos está en cada miembro, luego en la intersección. Es intervalo y R2 da conexidad. Para una familia sin miembros, la intersección relativa a $\mathbb R$ es toda $\mathbb R$, también intervalo. La unión falla para $(0,1)\cup(2,3)$: $1/2$ y $5/2$ pertenecen pero $3/2$ no; R3 da desconexión o se exhibe el corte por $3/2$.

</details>

#### Ejercicio 14. Una familia con punto común

[]{#MA-EX-ANM-01-015-014}

Sea $(E_i)_{i\in J}$ una familia no vacía de conexos reales y supón que hay $p\in\bigcap_{i\in J}E_i$. Prueba que $H=\bigcup_{i\in J}E_i$ es conexo sin seleccionar puntos o radios por miembro.

[]{#MA-SOL-ANM-01-015-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Supongamos una separación $H=A\cup B$ y, intercambiando nombres, $p\in A$. Para cada índice fijo $i$, las partes $E_i\cap A$ y $E_i\cap B$ son abiertas relativas a $E_i$, disjuntas y exhaustivas. La primera contiene el punto común $p$. Si la segunda fuese no vacía, separaría $E_i$; por conexidad es vacía. Se ha probado para todo $i$ que $E_i\subseteq A$. Por definición de unión, $H\subseteq A$, luego $B=\varnothing$, contradicción. El punto $p$ es único testigo compartido fijado desde la hipótesis; no se produce una familia de elecciones.

</details>

#### Ejercicio 15. Cerrar un intervalo sin romperlo

[]{#MA-EX-ANM-01-015-015}

Prueba directamente que la adherencia real $\overline I$ de un intervalo $I$ es intervalo, por tanto conexa. Incluye el caso vacío.

[]{#MA-SOL-ANM-01-015-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Para $I=\varnothing$, ninguna vecindad toca $I$ y su adherencia es vacía. En el resto, tomemos $u<v$ en $\overline I$ y $u<t<v$. La vecindad de $u$ de radio $(t-u)/2$ toca $I$, dando $a\in I$ con $a<t$. La de $v$ de radio $(v-t)/2$ da $b\in I$ con $t<b$. Intervalaridad implica $t\in[a,b]\subseteq I\subseteq\overline I$. Los extremos $u,v$ ya están en la adherencia. Así todo segmento entre miembros está en ella, y es intervalo. R2 prueba conexidad. Sólo se fijaron dos testigos de vecindades para el punto $t$ considerado.

</details>
## 15.4. La continuidad transporta la imposibilidad de separar

[]{#MA-SEC-ANM-01-015-004}

Ya sabemos reconocer los dominios conexos. Ahora preguntamos qué hace una función continua con ellos. C14 no afirmó que las imágenes de abiertos fueran abiertas; sí demostró apertura de preimágenes. Ésa es exactamente la dirección necesaria.

**R4. Imagen continua de un conexo.** Sea $f:D\to\mathbb R$ continua y sea $E\subseteq D$ conexo. Entonces $H=f[E]$ es conexo. La restricción $h=f\mathbin{\upharpoonright}E:E\to\mathbb R$ es continua por C14 y tiene imagen $H$. Si $E$ es vacío también lo es $H$, y el resultado es inmediato.

La estrategia para el caso general es suponer una separación de valores y devolverla a entradas. Sean $H=A\cup B$ las partes de esa supuesta separación. Por apertura relativa hay abiertos reales $V,W$ con $A=H\cap V$, $B=H\cap W$. Definimos

$$P=\{x\in E:h(x)\in A\},\qquad Q=\{x\in E:h(x)\in B\}.$$

Como todas las salidas de $h$ están en $H$, tenemos $P=h^{-1}[V]$ y $Q=h^{-1}[W]$. C14 garantiza que son abiertos relativos a $E$. Son disjuntos, pues un punto común produciría una salida en $A\cap B$. Cubren $E$, porque toda salida está en una de las dos partes.

Falta una condición que suele perderse: ambas preimágenes deben ser no vacías. Tomamos un valor $y_A\in A$. Al pertenecer a $H=h[E]$, existe $x_A\in E$ con $h(x_A)=y_A$; por tanto $x_A\in P$. De igual forma hay un punto en $Q$. Se fijan sólo dos testigos de fibras, no una función que escoja preimágenes para todos los valores. Así $P,Q$ separan $E$, contradicción. $H$ es conexo.

**Consecuencia.** La imagen continua de un intervalo es intervalo: el dominio es conexo por R2, la imagen es conexa por R4 y vuelve a ser intervalo por R3. No se requiere inyectividad, monotonía, dominio cerrado ni acotación.

La preservación tiene límites claros. Con $q(x)=x^2$ en $[-2,2]$, el conjunto $\{1\}$ es conexo, pero su preimagen $\{-1,1\}$ no lo es. Tampoco una imagen conexa obliga a un dominio conexo: una función constante en $\{-1,1\}$ es continua en ese dominio y su imagen es singleton. Las dos afirmaciones falsas invierten una implicación cuya prueba iba de una separación de salidas hacia una de entradas.

Hay una prueba equivalente mediante funciones con sólo dos valores. **$E$ es conexo si y sólo si toda función continua $u:E\to\{0,1\}$ es constante**, donde la continuidad se entiende con distancias reales. Si $E$ es conexo, R4 da imagen conexa contenida en $\{0,1\}$; si tomara ambos valores, la imagen no sería intervalo. En vacío, «constante» significa que todos los pares de entradas tienen igual salida, condición vacía. En sentido contrario, una separación $A,B$ define $u=0$ en $A$, $u=1$ en $B$. En cada punto la apertura relativa de su parte da una vecindad donde $u$ no cambia, y prueba continuidad para todo $\varepsilon>0$. $u$ no es constante por la no vacuidad de ambas partes. El criterio transforma una ruptura del dominio en una función continua de dos colores.

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-015-025}

¿Qué operación de conjuntos usa la continuidad para transportar una separación de la imagen?

[]{#MA-MSOL-ANM-01-015-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

Preimágenes. Si las partes de la imagen son $H\cap V$ y $H\cap W$, sus preimágenes por $h:E\to\mathbb R$ son $h^{-1}[V]$ y $h^{-1}[W]$, abiertas relativas a $E$.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-015-026}

¿Por qué se restringe $f$ al conexo $E\subseteq D$?

[]{#MA-MSOL-ANM-01-015-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Así la función $h=f\upharpoonright E$ tiene exactamente el ambiente de entradas que queremos separar. Su continuidad se hereda de $f$ y su imagen es $f[E]$.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-015-027}

¿Qué garantiza que la preimagen de una parte no vacía de $f[E]$ sea no vacía?

[]{#MA-MSOL-ANM-01-015-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

Que sus valores pertenecen a la imagen: para un valor concreto $y$ de esa parte existe $x\in E$ con $f(x)=y$. No bastaría que $y$ perteneciera solamente al codominio.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-015-028}

¿R4 necesita escoger una entrada para cada valor de la imagen?

[]{#MA-MSOL-ANM-01-015-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

No. Para refutar la separación se fijan sólo un valor y una preimagen en cada una de sus dos partes. No se construye un selector global de fibras.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-015-029}

¿La preimagen de un conexo por una función continua tiene que ser conexa?

[]{#MA-MSOL-ANM-01-015-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

No. Para $q(x)=x^2$ en $[-2,2]$, $q^{-1}[\{1\}]=\{-1,1\}$, que no es intervalo, aunque $\{1\}$ sí es conexo.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-015-030}

¿Una imagen singleton prueba que el dominio es conexo?

[]{#MA-MSOL-ANM-01-015-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

No. Una función constante en $\{-1,1\}$ es continua en el dominio relativo y tiene imagen singleton, pero el dominio admite un corte por cero.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-015-031}

¿Cómo una separación define una función continua con valores cero y uno?

[]{#MA-MSOL-ANM-01-015-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Se asigna cero a una parte y uno a la otra. En cada punto la apertura relativa da una vecindad donde la función es constante; el error de salida allí es cero para cualquier tolerancia positiva.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-015-032}

¿Qué significa «constante» para una función con dominio vacío en este criterio?

[]{#MA-MSOL-ANM-01-015-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

Que para todos $x,z$ del dominio se cumple $u(x)=u(z)$. La condición universal es vacía; no se exige un valor alcanzado ni una entrada testigo.

</details>

### Ejercicios de la sección 15.4

#### Ejercicio 16. Separación de valores a entradas

[]{#MA-EX-ANM-01-015-016}

Reconstruye R4 para una continua $f:D\to\mathbb R$ y un conexo $E\subseteq D$. Identifica los ambientes de las dos parejas de abiertos y dónde se usa pertenencia a la imagen.

[]{#MA-SOL-ANM-01-015-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Sea $h=f\upharpoonright E$, continua. Si $H=f[E]$ se separara como $A=H\cap V$, $B=H\cap W$ con $V,W$ abiertos reales, tomamos $P=\{x\in E:h(x)\in A\}=h^{-1}[V]$ y $Q=h^{-1}[W]$. Son abiertos relativos a $E$, mientras $A,B$ lo eran a $H$. Disjunción y cobertura se trasladan porque toda salida de $h$ está en $H=A\cup B$. Para un valor concreto en cada parte, pertenecer a $H$ da una entrada en $E$ con esa salida; ambas preimágenes son no vacías. Así separan $E$, contradicción. Si $E$ es vacío, su imagen es vacía y ya es conexa. No se usa inversa funcional ni selector de todas las fibras.

</details>

#### Ejercicio 17. La preimagen que se divide

[]{#MA-EX-ANM-01-015-017}

Para $q:[-2,2]\to\mathbb R$, $q(x)=x^2$, calcula $q^{-1}[\{1\}]$ y prueba que no es conexa. ¿Qué hipótesis de R4 siguen siendo verdaderas?

[]{#MA-SOL-ANM-01-015-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

La ecuación $x^2=1$ equivale a $(x-1)(x+1)=0$, luego la preimagen es $\{-1,1\}$. Sus dos singletons se obtienen cortando por cero; son abiertos relativos, disjuntos y no vacíos, y cubren la preimagen. No es conexa. $q$ es continua por C14, su dominio $[-2,2]$ es conexo y $\{1\}$ también. Nada contradice R4: el teorema preserva conexidad por imagen directa, no por preimagen.

</details>

#### Ejercicio 18. Una imagen global intervalar no certifica continuidad

[]{#MA-EX-ANM-01-015-018}

En $[-1,1]$ define $f(x)=x$ si $x<0$ y $f(x)=x-1$ si $x\ge0$. Calcula su imagen y decide su continuidad en cero. Refuta «si la imagen es intervalo, la función es continua».

[]{#MA-SOL-ANM-01-015-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

La primera rama tiene imagen $[-1,0)$ y la segunda $[-1,0]$, luego la imagen total es $[-1,0]$, intervalo. Pero $f(0)=-1$. Dado $\delta>0$, ponemos $t=\min(\delta/2,1/4)>0$, $x=-t\in[-1,0)$. Entonces $|x|<\delta$ y $|f(x)-f(0)|=1-t\ge3/4>1/2$. La tolerancia $1/2$ refuta continuidad en cero. El resultado de preservación es una implicación con continuidad como premisa; que la imagen total sea intervalar no prueba controles locales ni el valor intermedio en cada subsegmento.

</details>

#### Ejercicio 19. El criterio de dos valores

[]{#MA-EX-ANM-01-015-019}

Demuestra que $E$ es conexo si y sólo si toda continua $u:E\to\{0,1\}$ es constante, con la convención de constancia por igualdad entre todas las parejas de entradas.

[]{#MA-SOL-ANM-01-015-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Si $E$ es conexo, R4 da imagen conexa de $u$ como subconjunto real. Una imagen que contuviera $0$ y $1$ sería exactamente $\{0,1\}$, que omite $1/2$ y no es intervalo; contradicción con R3. Así no hay dos entradas con salidas distintas, que es constancia. Si $E$ tuviera separación $A,B$, definimos $u=0$ en $A$, $u=1$ en $B$. Cobertura/disjunción hacen válida la función. Para cada entrada, una bola relativa contenida en su parte hace el error cero, dando continuidad para todo $\varepsilon>0$. Las dos partes no vacías dan salidas diferentes, contradicción con el criterio. En vacío la condición de constancia es universal vacía y no se exige valor alcanzado.

</details>

#### Ejercicio 20. Conexidad preservada por homeomorfismo

[]{#MA-EX-ANM-01-015-020}

Sea $f:E\to F$ un homeomorfismo entre subconjuntos reales. Prueba que $E$ es conexo si y sólo si $F$ lo es. Explica cuál de las dos direcciones puede fallar para una continua sobreyectiva.

[]{#MA-SOL-ANM-01-015-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Si $E$ es conexo, continuidad de $f$ y sobreyectividad dan $F=f[E]$ conexo por R4. Si $F$ es conexo, la inversa $h:F\to E$ es continua y sobreyectiva sobre $E$, luego $E=h[F]$ es conexo. Para una continua sobreyectiva sin inversa continua sólo está garantizada la primera dirección. La constante $\{-1,1\}\to\{0\}$ es continua y sobreyectiva; el codominio es conexo y el dominio no. No hay inversa funcional en ese ejemplo, lo cual ya basta para refutar la recíproca general.

</details>
## 15.5. El valor intermedio como consecuencia estructural

[]{#MA-SEC-ANM-01-015-005}

En cálculo solemos comenzar con el dibujo de una curva que atraviesa una altura. Ahora podemos justificar la existencia sin depender de la apariencia del gráfico. La continuidad preserva una estructura del dominio: la ausencia de puntos omitidos entre dos puntos presentes.

**R5. Teorema del valor intermedio.** Sea $I\subseteq\mathbb R$ intervalo, $f:I\to\mathbb R$ continua, y sean $u,v\in I$. Para cualquier $y$ entre $f(u)$ y $f(v)$, incluidos los extremos, existe

$$c\in[\min(u,v),\max(u,v)]\quad\text{tal que}\quad f(c)=y.$$

Para obtener esta localización, aplicamos R4 a la restricción de $f$ al segmento

$$J=[\min(u,v),\max(u,v)].$$

Por definición de intervalo, $J\subseteq I$; también $J$ es intervalo, porque una desigualdad entre sus puntos permanece dentro de sus extremos. La imagen $f[J]$ es intervalo y contiene $f(u),f(v)$. Por ello contiene todos los valores entre ellos, en particular $y$. La definición de imagen da el testigo $c\in J$. Si $u=v$, necesariamente $y=f(u)$ y sirve $c=u$. Si el valor buscado es estrictamente intermedio y $u\ne v$, el testigo no puede ser ninguno de los extremos, porque sus salidas no son $y$.

![A la izquierda F(x)=x³+x−1 alcanza cero entre 0 y 1; el gráfico no calcula la raíz exacta. El escalón del centro tiene signos opuestos y omite cero por discontinuidad. La identidad del panel derecho es continua en su dominio de dos puntos, pero ese dominio no es intervalo.](../../assets/books/anm/C15/C15-F04.svg){#fig-anm-c15-f04 fig-alt="A la izquierda F(x)=x³+x−1 alcanza cero entre 0 y 1; el gráfico no calcula la raíz exacta. El escalón del centro tiene signos opuestos y omite cero por discontinuidad. La identidad del panel derecho es continua en su dominio de dos puntos, pero ese dominio no es intervalo."}

**Cambio de signo.** Si $a<b$ y $f:[a,b]\to\mathbb R$ es continua con $f(a)<0<f(b)$ o la orientación inversa, R5 con $y=0$ da $c\in(a,b)$ con $f(c)=0$. Con desigualdades no estrictas sólo se concluye un cero en $[a,b]$: podría ser un extremo. Para buscar un nivel $y$ definimos $g=f-y$; C14 prueba su continuidad y la ecuación $g=0$ equivale a $f=y$.

**Signo constante sin ceros.** Si $f$ es continua en un intervalo y nunca vale cero, no puede tomar un valor positivo y otro negativo, pues R5 produciría un cero entre sus argumentos. Si el intervalo es no vacío, fijando una entrada obtenemos que todos los valores tienen el mismo signo. En un dominio roto esto falla: $1/x$ es continua en $\mathbb R\setminus\{0\}$ y tiene ambos signos. También falla sin continuidad: la función escalón que vale $-1$ para $x<0$ y $1$ para $x\ge0$ en $[-1,1]$ no tiene ceros. En cero, todo radio incluye una entrada negativa cuya salida dista $2$ del valor central; la tolerancia $1$ refuta continuidad. Y la identidad restringida a $\{-1,1\}$ es continua pero no alcanza cero: el dominio no es intervalo.

El teorema garantiza existencia, no unicidad. $x^2$ alcanza $1$ en dos puntos de $[-2,2]$. Tampoco dice que una función tome sólo valores entre los de los extremos: en ese dominio los extremos tienen ambos valor $4$, y el centro vale $0$. Lo garantizado es la inclusión de los valores intermedios en la imagen, no una descripción completa de la imagen por $f(a),f(b)$.

Consideremos $F(x)=x^3+x-1$. Es continua por C14, y $F(0)=-1$, $F(1)=1$, luego tiene una raíz en $(0,1)$. Además, para $0\le x<z\le1$,

$$F(z)-F(x)=(z-x)(z^2+zx+x^2+1)>0.$$

Esta desigualdad, independiente del argumento de existencia, prueba unicidad en $[0,1]$. La raíz no se conoce por una fórmula en esta prueba, pero existe y es única en el segmento indicado.

Una imagen intervalar puede no estar acotada ni ser cerrada: la identidad en $(0,1)$ tiene imagen $(0,1)$, y la identidad en $\mathbb R$ tiene imagen no acotada. Garantizar extremos alcanzados exige una herramienta adicional de C16. Aquí no la presuponemos.

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-015-033}

¿En qué segmento se localiza el testigo del valor intermedio entre $f(u)$ y $f(v)$?

[]{#MA-MSOL-ANM-01-015-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

En $[\min(u,v),\max(u,v)]$, contenido en el intervalo de partida. Se aplica preservación a ese segmento, no sólo a todo el dominio.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-015-034}

¿Por qué un nivel estrictamente intermedio no se alcanza en los extremos de ese segmento?

[]{#MA-MSOL-ANM-01-015-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Porque es distinto de $f(u)$ y $f(v)$. Un testigo con esa salida no puede ser $u$ ni $v$, así queda en el interior si son distintos.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-015-035}

¿Qué cambia si sólo se conoce $f(a)\le0\le f(b)$?

[]{#MA-MSOL-ANM-01-015-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Se garantiza un cero en $[a,b]$, que puede estar en un extremo. Para asegurar uno en $(a,b)$ hacen falta signos estrictos opuestos.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-015-036}

¿Cómo se reduce encontrar $f(x)=y$ a encontrar un cero?

[]{#MA-MSOL-ANM-01-015-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Con $g(x)=f(x)-y$, continua por álgebra de C14. Entonces $g(x)=0$ equivale exactamente a $f(x)=y$ y el dominio no cambia.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-015-037}

¿Qué prueba signo constante de una continua sin ceros en un intervalo no vacío?

[]{#MA-MSOL-ANM-01-015-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

Si hubiera dos valores de signos opuestos, R5 produciría un cero entre sus argumentos. Fijando un valor, todos los demás deben tener su mismo signo.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-015-038}

¿Por qué $1/x$ no contradice ese resultado al tener ambos signos?

[]{#MA-MSOL-ANM-01-015-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Su dominio $\mathbb R\setminus\{0\}$ no es intervalo. La continuidad se conserva en ese dominio roto, pero falta la hipótesis que conecta los argumentos de signos opuestos.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-015-039}

¿R5 afirma unicidad del argumento que alcanza un nivel?

[]{#MA-MSOL-ANM-01-015-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

No. $x^2$ alcanza $1$ en $-1$ y $1$. La existencia de al menos un argumento se distingue de cualquier prueba adicional de inyectividad o monotonía.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-015-040}

¿La imagen de una continua intervalar tiene necesariamente mínimo y máximo?

[]{#MA-MSOL-ANM-01-015-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No bajo estas hipótesis. La identidad en $(0,1)$ tiene imagen $(0,1)$, sin mínimo ni máximo. R5 prueba ausencia de huecos entre valores alcanzados, no extremos alcanzados.

</details>

### Ejercicios de la sección 15.5

#### Ejercicio 21. Localización con orientación invertida

[]{#MA-EX-ANM-01-015-021}

Sea $I$ intervalo, $f:I\to\mathbb R$ continua y $u>v$ con $f(u)<y<f(v)$. Indica dónde existe un argumento con salida $y$ y justifica por qué no es extremo.

[]{#MA-SOL-ANM-01-015-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

$[v,u]\subseteq I$ por intervalaridad. La restricción continua a ese segmento tiene imagen intervalar que contiene $f(u)$ y $f(v)$, por R4 y R3. Contiene el valor intermedio $y$, así existe $c\in[v,u]$ con $f(c)=y$. Las desigualdades estrictas hacen $y$ distinto de las dos salidas extremas, luego $c\ne u,v$ y $c\in(v,u)$. El orden de las salidas no tiene que coincidir con el de los argumentos.

</details>

#### Ejercicio 22. Existencia y unicidad por pruebas distintas

[]{#MA-EX-ANM-01-015-022}

Prueba que $F(x)=x^3+x-1$ tiene exactamente una raíz en $[0,1]$, y que está en $(0,1)$. No uses derivadas.

[]{#MA-SOL-ANM-01-015-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

$F$ es continua por álgebra polinomial de C14. $F(0)=-1<0$ y $F(1)=1>0$, así R5 da una raíz interior. Para $0\le x<z\le1$, $F(z)-F(x)=(z-x)(z^2+zx+x^2+1)>0$, porque el primer factor es positivo y el segundo al menos $1$. Por tanto es estrictamente creciente en el segmento y no puede tener dos ceros. Existencia e interioridad vienen del valor intermedio; unicidad viene de la desigualdad algebraica independiente.

**Retorno visual.** Véase [C15-F04](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 23. Una coincidencia de dos continuas

[]{#MA-EX-ANM-01-015-023}

Sean $f,g:[0,1]\to\mathbb R$ continuas, con $f(0)<g(0)$ y $f(1)>g(1)$. Prueba que coinciden en alguna entrada interior. ¿Se garantiza una sola coincidencia?

[]{#MA-SOL-ANM-01-015-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

$h=f-g$ es continua por C14. En cero es negativa y en uno positiva, luego R5 da $c\in(0,1)$ con $h(c)=0$, es decir $f(c)=g(c)$. No se garantiza unicidad. Por ejemplo $f(x)=(x-1/4)(x-1/2)(x-3/4)$ y $g(x)=0$ cumplen $f(0)=-3/32<0$, $f(1)=3/32>0$ y coinciden en tres entradas interiores distintas. Todas las funciones indicadas son polinomiales o constantes y por ello continuas.

</details>

#### Ejercicio 24. Sin ceros, un signo

[]{#MA-EX-ANM-01-015-024}

Sea $I$ intervalo no vacío y $f:I\to\mathbb R$ continua sin ceros. Prueba que $f>0$ en todo $I$ o $f<0$ en todo $I$. Refuta la conclusión si se elimina sólo la intervalaridad.

[]{#MA-SOL-ANM-01-015-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Fijamos $a\in I$. Como $f(a)\ne0$, es positivo o negativo. Si fuese positivo y hubiera $b$ con $f(b)<0$, R5 produciría cero entre $a,b$, contradicción. Todos los valores son no negativos y, al no haber ceros, positivos. El caso $f(a)<0$ es simétrico. Sin intervalaridad, $f(x)=1/x$ en $\mathbb R\setminus\{0\}$ es continua por C14, no tiene ceros y toma $-1$ y $1$. El punto omitido impide aplicar R5 entre esos argumentos.

</details>

#### Ejercicio 25. Inclusión no es descripción de toda la imagen

[]{#MA-EX-ANM-01-015-025}

Un razonamiento afirma que para toda continua en $[a,b]$ se cumple

$$f[[a,b]]=[\min(f(a),f(b)),\max(f(a),f(b))].$$

Da un contraejemplo y enuncia la conclusión exacta que sí aporta R5.

[]{#MA-SOL-ANM-01-015-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Para $f(x)=x^2$ en $[-2,2]$, ambos extremos valen $4$, pero $f(0)=0$. La fórmula propuesta daría sólo $\{4\}$, y es falsa. La imagen es de hecho $[0,4]$: todo cuadrado del dominio está ahí, y para cada $y\in[0,4]$ la raíz positiva $\sqrt y\in[0,2]$ da la preimagen. R5 garantiza la inclusión del segmento entre las dos salidas extremas dentro de la imagen. No garantiza que no haya otros valores; identificar extremos globales alcanzados requiere argumentos adicionales.

</details>
## 15.6. Bisección: existencia, localización y alcance del cálculo

[]{#MA-SEC-ANM-01-015-006}

El valor intermedio ya prueba existencia. La bisección añade una sucesión determinada de encierros y una cota de error posicional. La desarrollaremos también como prueba alternativa de existencia para comparar qué trabajo hacen las hipótesis.

**R6. Encierros de signo.** Sean $a<b$, $g:[a,b]\to\mathbb R$ continua, $g(a)<0<g(b)$. La orientación contraria se reduce usando $-g$. Definimos $L_0=a$, $U_0=b$. Si alguna evaluación de un punto medio da cero, ya hay un testigo exacto y detenemos el proceso. Mientras eso no ocurra, para $n\ge0$ ponemos $M_n=(L_n+U_n)/2$ y

$$
(L_{n+1},U_{n+1})=
\begin{cases}
(M_n,U_n),&g(M_n)<0,\\
(L_n,M_n),&g(M_n)>0.
\end{cases}
$$

La tricotomía clásica y la regla explícita dan una transición única; no se elige un punto arbitrario por paso. Por inducción, cada segmento está contenido en el anterior, $L_n\le U_n$, $g(L_n)<0<g(U_n)$ y

$$U_n-L_n=\frac{b-a}{2^n}.$$

La base es inmediata. En cada caso de la transición se conserva un extremo del signo correspondiente y se reemplaza el otro por el punto medio del mismo signo; la longitud se divide por dos. Éste es el invariante que hace útil al objeto auxiliar.

Si no encontramos un cero en un número finito de pasos, definimos $c=\sup\{L_n:n\in\mathbb N\}$. Los extremos inferiores están acotados por $b$. Para cada $n$, $U_n$ es cota de todos los $L_k$: si $k\le n$, $L_k\le L_n\le U_n$; si $k>n$, el encierro anidado da $L_k\le U_k\le U_n$. Así

$$L_n\le c\le U_n,\qquad c\in[a,b].$$

Como $(b-a)/2^n\to0$ por las escalas de C06, las desigualdades prueban directamente $L_n\to c$ y $U_n\to c$. La dirección secuencial directa de continuidad de C14 da $g(L_n)\to g(c)$ y $g(U_n)\to g(c)$. Límites de valores negativos son no positivos y de positivos son no negativos: si el límite fuese positivo en el primer caso, la tolerancia de la mitad de ese límite haría eventualmente positivos los términos, contradicción; el otro caso es análogo. Resulta $g(c)\le0$ y $g(c)\ge0$, de donde $g(c)=0$.

Cada encierro contiene este cero y su punto medio satisface

$$|M_n-c|\le\frac{U_n-L_n}{2}=\frac{b-a}{2^{n+1}}.$$

Para obtener error posicional menor que $\tau>0$, basta elegir $n$ con $(b-a)/2^{n+1}<\tau$. No se demuestra que $M_n$ sea raíz ni que la raíz sea única; sin monotonía puede haber varias raíces, y esta recurrencia localiza una de ellas. En el caso de detención temprana tenemos error cero en el testigo encontrado.

![Encierros tras 0, 1, 2 y 3 actualizaciones. Extremos inferiores negativos y superiores positivos; la marca central indica el medio de cada encierro. En n=3 el medio es 11/16 y su error posicional respecto de la raíz encerrada es a lo sumo 1/16. No se afirma error residual ni raíz exacta en el medio.](../../assets/books/anm/C15/C15-F05.svg){#fig-anm-c15-f05 fig-alt="Encierros tras 0, 1, 2 y 3 actualizaciones. Extremos inferiores negativos y superiores positivos; la marca central indica el medio de cada encierro. En n=3 el medio es 11/16 y su error posicional respecto de la raíz encerrada es a lo sumo 1/16. No se afirma error residual ni raíz exacta en el medio."}

Para $F(x)=x^3+x-1$, los primeros medios de $[0,1]$ son $1/2$, $3/4$ y $5/8$, con valores respectivos $-3/8$, $11/64$ y $-67/512$. Los encierros pasan por $[1/2,1]$, $[1/2,3/4]$, $[5/8,3/4]$. Después de tres actualizaciones, el medio es $11/16$ y su error de posición es a lo sumo $1/16$. Los cálculos racionales exactos certifican los signos, no una lectura de píxeles.

La cota de longitud no da por sí sola una cota del residual $|g(M_n)|$: una función puede variar mucho dentro de un intervalo pequeño. Un módulo cuantitativo conocido sí permitiría convertir error de posición en error funcional. Y una función arbitraria no viene con un procedimiento que decida exactamente si cada evaluación real es positiva, negativa o cero. La recurrencia matemática usa comparación clásica; un programa requiere evaluación y certificados de signo. Si un intervalo numérico de evaluación contiene cero, no autoriza ninguna de las dos actualizaciones ni la declaración de raíz exacta. Esta distinción preserva el valor de la prueba sin prometer una computabilidad que las hipótesis no dan.

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-015-041}

¿Cuál es la longitud del encierro después de $n$ actualizaciones de bisección?

[]{#MA-MSOL-ANM-01-015-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

Con $L_0=a$, $U_0=b$, es $(b-a)/2^n$, mientras no haya detención por un cero exacto. Cada transición divide por dos la longitud anterior.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-015-042}

¿Qué extremo se reemplaza cuando $g(M_n)<0$ y los signos iniciales son negativo/positivo?

[]{#MA-MSOL-ANM-01-015-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

El inferior: $L_{n+1}=M_n$, $U_{n+1}=U_n$. El nuevo inferior conserva signo negativo y el superior conserva positivo.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-015-043}

¿Por qué $U_n$ es cota de todos los extremos inferiores y no sólo de $L_n$?

[]{#MA-MSOL-ANM-01-015-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Para $k\le n$, $L_k\le L_n\le U_n$. Para $k>n$, el anidamiento da $L_k\le U_k\le U_n$. Ambos casos prueban la cota para todo $k$.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-015-044}

¿Qué dirección secuencial de continuidad se usa para pasar al cero límite?

[]{#MA-MSOL-ANM-01-015-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

La directa: convergencia de entradas a $c$ implica convergencia de salidas a $g(c)$. No se usa la recíproca secuencial ni selección de infractores.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-015-045}

¿Cuál es el error posicional máximo del punto medio $M_n$ respecto del cero encerrado?

[]{#MA-MSOL-ANM-01-015-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

Como $c\in[L_n,U_n]$, $|M_n-c|\le(U_n-L_n)/2=(b-a)/2^{n+1}$. Es una cota de distancia de argumentos.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-015-046}

¿Un encierro pequeño da por sí solo una cota numérica del residual $|g(M_n)|$?

[]{#MA-MSOL-ANM-01-015-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

No. Falta control cuantitativo de la variación de $g$. Continuidad permite un radio para una tolerancia dada, pero la longitud sola no proporciona una fórmula universal de residual.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-015-047}

¿Un intervalo de evaluación que contiene cero certifica que $g(M_n)=0$?

[]{#MA-MSOL-ANM-01-015-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

No. Sólo indica que no se certificó un signo estricto. Puede contener valores positivos o negativos; no autoriza detención por raíz exacta ni actualización de uno de los extremos.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-015-048}

¿Por qué la recurrencia clásica no es una promesa de algoritmo efectivo para toda función continua?

[]{#MA-MSOL-ANM-01-015-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Las hipótesis no incluyen una evaluación computable ni una decisión efectiva de signos reales exactos. La regla única es válida matemáticamente por tricotomía; una implementación exige certificados de signo.

</details>

### Ejercicios de la sección 15.6

#### Ejercicio 26. Tres actualizaciones exactas

[]{#MA-EX-ANM-01-015-026}

Aplica tres actualizaciones de bisección a $F(x)=x^3+x-1$ desde $[0,1]$, empezando en $n=0$. Calcula signos exactos, encierro final, medio final y su cota posicional.

[]{#MA-SOL-ANM-01-015-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

$M_0=1/2$ y $F(M_0)=1/8+1/2-1=-3/8<0$, así $[L_1,U_1]=[1/2,1]$. $M_1=3/4$ y $F(M_1)=27/64+48/64-64/64=11/64>0$, así $[L_2,U_2]=[1/2,3/4]$. $M_2=5/8$ y $F(M_2)=125/512+320/512-512/512=-67/512<0$, así $[L_3,U_3]=[5/8,3/4]$. Su medio es $M_3=11/16$. La raíz encerrada $c$ satisface $|M_3-c|\le(3/4-5/8)/2=1/16$. Se usaron tres evaluaciones/actualizaciones; no se evaluó $M_3$ para obtener esta cota.

**Retorno visual.** Véase [C15-F05](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 27. Número de actualizaciones

[]{#MA-EX-ANM-01-015-027}

Con encierro inicial de longitud $3$, encuentra un número de actualizaciones que garantice error del medio estrictamente menor que $1/1000$. Da la regla general y explica la estrictitud.

[]{#MA-SOL-ANM-01-015-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Después de $n$ actualizaciones, el error es a lo sumo $3/2^{n+1}$. Buscamos que esa cota sea estrictamente menor que $1/1000$, equivalente a $2^{n+1}>3000$. Para $n=11$, $2^{12}=4096>3000$, así sirve; $n=10$ no lo garantiza pues $2048<3000$. En general se elige $n\in\mathbb N$ con $2^{n+1}>(b-a)/\tau$. Una cota igual a $\tau$ sólo garantiza error menor o igual, no estricto. Si hubo cero exacto antes, se dispone de error cero.

</details>

#### Ejercicio 28. El cero límite sin compacidad

[]{#MA-EX-ANM-01-015-028}

En el caso infinito de bisección, prueba que $c=\sup\{L_n\}$ pertenece a todos los encierros y que $g(c)=0$. No cites un teorema de intervalos anidados ni compacidad.

[]{#MA-SOL-ANM-01-015-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Los $L_n$ están acotados por $b$ y el conjunto no vacío tiene supremo $c$. Para un $n$ fijo, si $k\le n$, $L_k\le L_n\le U_n$; si $k>n$, anidamiento da $L_k\le U_k\le U_n$. Así $U_n$ es cota de todos los inferiores y $L_n\le c\le U_n$. En particular $c\in[a,b]$. De $0\le c-L_n\le(b-a)/2^n$ y $0\le U_n-c\le(b-a)/2^n$ resultan ambas convergencias a $c$. Continuidad directa da $g(L_n),g(U_n)\to g(c)$. Una sucesión negativa no puede converger a un real positivo, pues una tolerancia de la mitad de ese real haría los términos positivos; análogamente la positiva no converge a negativo. Así $g(c)\le0$ y $g(c)\ge0$, luego vale cero. No se usó selección de rutas ni recíproca secuencial.

</details>

#### Ejercicio 29. Longitud frente a residual

[]{#MA-EX-ANM-01-015-029}

Refuta que exista una cota del residual del medio determinada sólo por la longitud del encierro y los signos opuestos en sus extremos, válida para toda función continua. Construye ejemplos lineales para una longitud $\ell>0$ fija.

[]{#MA-SOL-ANM-01-015-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Para $A>0$ definimos $g_A(x)=A(x-\ell/4)$ en $[0,\ell]$. Es continua, $g_A(0)=-A\ell/4<0$, $g_A(\ell)=3A\ell/4>0$, y su raíz es $\ell/4$. El medio $\ell/2$ tiene error posicional $\ell/4$, compatible con la cota $\ell/2$, pero residual $|g_A(\ell/2)|=A\ell/4$. Dado cualquier candidato finito $B\ge0$ para esa longitud, elegimos $A>4B/\ell$, y el residual supera $B$. La longitud no controla la escala vertical; haría falta información cuantitativa adicional de la función.

</details>

#### Ejercicio 30. Una evaluación incierta

[]{#MA-EX-ANM-01-015-030}

Un programa devuelve una inclusión certificada $g(M)\in[-10^{-6},2\cdot10^{-6}]$ y actualiza el extremo inferior afirmando «es prácticamente negativo». Evalúa esa decisión e indica qué datos autorizan las actualizaciones o la detención exacta.

[]{#MA-SOL-ANM-01-015-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La inclusión permite valores negativos, cero y positivos, por lo que no certifica $g(M)<0$. Sustituir el extremo inferior puede destruir el invariante si el valor es positivo. Un certificado contenido estrictamente en $(-\infty,0)$ autoriza reemplazar el inferior; uno contenido estrictamente en $(0,\infty)$ autoriza reemplazar el superior. Una igualdad exacta certificada $g(M)=0$ autoriza detener con raíz exacta. Si el intervalo de evaluación contiene cero, se requiere refinar o conservar el encierro anterior y declarar que no se decidió el signo; no se deduce igualdad de una tolerancia pequeña. La recurrencia clásica no proporciona por sí sola esos certificados computacionales.

</details>
## 15.7. Inyectividad, orden y continuidad de la inversa

[]{#MA-SEC-ANM-01-015-007}

C14 mostró que una biyección continua en un dominio roto puede tener inversa discontinua. ¿Qué cambia si el dominio es intervalo? Primero aparece una orientación de orden; después esa orientación construye radios para la inversa.

**R7. Una inyección continua en un intervalo es estrictamente monótona y es un homeomorfismo sobre su imagen.** Sea $f:I\to\mathbb R$ continua e inyectiva. Para vacío y singleton la monotonía estricta, entendida como condición sobre pares distintos ordenados, es vacía; la inversa sobre la imagen es continua. Supongamos que $I$ tiene al menos dos puntos.

El paso clave es demostrar que para $x<y<z$ en $I$, $f(y)$ está estrictamente entre $f(x)$ y $f(z)$. Si fuese mayor que ambos, elegiríamos un nivel $w$ estrictamente entre $\max(f(x),f(z))$ y $f(y)$, por ejemplo su punto medio. R5 en $[x,y]$ y $[y,z]$ produciría $s\in(x,y)$ y $t\in(y,z)$ con $f(s)=w=f(t)$. Son distintos, contradicción. Si $f(y)$ fuese menor que ambos, usamos un nivel entre $f(y)$ y $\min(f(x),f(z))$ y obtenemos la misma contradicción. Inyectividad excluye igualdades. Por tanto, todo triple conserva una orientación creciente o decreciente.

Para justificar que la orientación es global, fijamos $a<b$ en $I$. Supongamos $f(a)<f(b)$; el caso contrario se reduce a $-f$. Dados cualesquiera $x<y$ en $I$, ordenamos el conjunto finito de puntos distintos de $\{a,b,x,y\}$ como $t_1<\cdots<t_m$. Hay al menos dos puntos. Si $m\ge3$, la propiedad de cada triple consecutivo obliga a que las diferencias $f(t_{i+1})-f(t_i)$ tengan el mismo signo: en un triple son ambas positivas o ambas negativas. Por propagación finita todas tienen el mismo signo. La desigualdad $f(a)<f(b)$ excluye el signo negativo. Si $m=2$, los pares $a<b$ y $x<y$ son el mismo par. En todos los casos $f(x)<f(y)$. Así $f$ es estrictamente creciente; o estrictamente decreciente en la otra orientación. No bastaba probar la propiedad de un único triple.

Sea $J=f[I]$, intervalo por R4. Inyectividad y la definición de imagen dan una inversa $h:J\to I$. Probemos su continuidad para el caso creciente. Fijamos $y_0=f(x_0)$ y $\varepsilon>0$. Queremos excluir toda entrada original que esté a distancia al menos $\varepsilon$ de $x_0$ cuando su salida está suficientemente próxima a $y_0$.

Si hay algún punto de $I$ menor o igual que $x_0-\varepsilon$, el carácter intervalar asegura que $\ell=x_0-\varepsilon/2$ pertenece a $I$. Ponemos $\eta_-=y_0-f(\ell)>0$. Si no hay tal punto, todas las entradas ya satisfacen $x>x_0-\varepsilon$ y no hace falta barrera izquierda; usamos $\eta_-=1$. De forma simétrica, si hay un punto de $I$ mayor o igual que $x_0+\varepsilon$, $r=x_0+\varepsilon/2\in I$ y $\eta_+=f(r)-y_0>0$; si no, usamos $\eta_+=1$.

Tomamos $\eta=\min(\eta_-,\eta_+)>0$. Para $y\in J$ con $|y-y_0|<\eta$, sea $x=h(y)$. Si $x\le x_0-\varepsilon$, la barrera izquierda existe y $x<\ell$; monotonía da $y=f(x)<f(\ell)=y_0-\eta_-$, incompatible con la proximidad. Si $x\ge x_0+\varepsilon$, la barrera derecha da $y>y_0+\eta_+$, también imposible. Así $|h(y)-h(y_0)|<\varepsilon$. La prueba incluye extremos porque una barrera innecesaria se sustituye por un radio positivo arbitrario. Para $f$ decreciente se aplica el caso creciente a $-f$ y se compone su inversa con $y\mapsto-y$, continua por C14. Queda probado el homeomorfismo $I\to J$.

![Para f(x)=x² en \[0,∞), x₀=1 y ε=3/5, las barreras 7/10 y 13/10 están dentro de la zona permitida (2/5,8/5). Sus distancias de salida a 1 son 51/100 y 69/100. La tolerancia η=51/100 impide que una preimagen de salida cercana cruce las barreras. Bandas abiertas según las desigualdades estrictas de R7.](../../assets/books/anm/C15/C15-F06.svg){#fig-anm-c15-f06 fig-alt="Para f(x)=x² en \[0,∞), x₀=1 y ε=3/5, las barreras 7/10 y 13/10 están dentro de la zona permitida (2/5,8/5). Sus distancias de salida a 1 son 51/100 y 69/100. La tolerancia η=51/100 impide que una preimagen de salida cercana cruce las barreras. Bandas abiertas según las desigualdades estrictas de R7."}

No se han usado derivadas, compacidad ni una cota lineal inferior. Estricta monotonía por sí sola no implica continuidad: $k(x)=x$ para $x<0$ y $k(x)=x+1$ para $x\ge0$ es estrictamente creciente en $\mathbb R$ y salta en cero; su imagen omite $[0,1)$. La continuidad es la hipótesis que impide el salto y hace intervalar la imagen.

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-015-049}

¿Qué condición entre las imágenes de $x<y<z$ inicia la prueba de monotonía?

[]{#MA-MSOL-ANM-01-015-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

$f(y)$ está estrictamente entre $f(x)$ y $f(z)$. Un pico o valle permitiría, por R5 en los dos subsegmentos, dos argumentos distintos con una misma salida, violando inyectividad.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-015-050}

¿Por qué se escoge un nivel estrictamente entre el pico y ambos extremos?

[]{#MA-MSOL-ANM-01-015-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

Para que R5 entregue un punto interior en cada subsegmento. Así los dos testigos son distintos, uno antes de $y$ y otro después, y la contradicción de inyectividad es segura.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-015-051}

¿Basta estudiar un único triple para concluir monotonía en todo el intervalo?

[]{#MA-MSOL-ANM-01-015-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

No. Se fija un par orientado $a<b$ y se ordenan junto con cualquier par $x<y$. Los triples consecutivos propagan el signo de las diferencias en ese conjunto finito; el par fijado determina la orientación.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-015-052}

¿Qué garantiza que exista una inversa $h:f[I]\to I$?

[]{#MA-MSOL-ANM-01-015-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Inyectividad da unicidad de la entrada por valor; la definición de imagen da existencia para todo valor de $f[I]$. No se requiere sobreyectividad sobre toda $\mathbb R$.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-015-053}

¿Qué hipótesis permite usar $x_0-\varepsilon/2$ como barrera si existe una entrada $x\le x_0-\varepsilon$?

[]{#MA-MSOL-ANM-01-015-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Que $I$ sea intervalo: el punto barrera está entre esa entrada y $x_0$, ambos de $I$. Así la evaluación $f(x_0-\varepsilon/2)$ está definida.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-015-054}

¿Qué se hace si no hay entradas de $I$ menores o iguales que $x_0-\varepsilon$?

[]{#MA-MSOL-ANM-01-015-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

No hace falta barrera izquierda porque todas las entradas ya superan ese umbral. Se asigna a ese lado una tolerancia positiva arbitraria, por ejemplo $1$, para formar el mínimo final.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-015-055}

¿La inversa continua obtenida requiere una cota lineal inferior de $f$?

[]{#MA-MSOL-ANM-01-015-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

No. El radio se obtiene por diferencias positivas de valores en puntos barrera y monotonía. No se supone $|f(x)-f(z)|\ge c|x-z|$ ni derivada no nula.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-015-056}

¿Estricto crecimiento por sí solo excluye saltos?

[]{#MA-MSOL-ANM-01-015-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No. $k(x)=x$ para $x<0$ y $k(x)=x+1$ para $x\ge0$ es estrictamente creciente, pero en cero las salidas por la izquierda se aproximan a cero y $k(0)=1$. Falta continuidad.

</details>

### Ejercicios de la sección 15.7

#### Ejercicio 31. Excluir un pico por dos fibras

[]{#MA-EX-ANM-01-015-031}

Sea $f:I\to\mathbb R$ continua e inyectiva y $x<y<z$ en $I$. Prueba que $f(y)$ está estrictamente entre $f(x)$ y $f(z)$, sin derivadas.

[]{#MA-SOL-ANM-01-015-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Inyectividad hace distintos los tres valores. Si $f(y)>\max(f(x),f(z))$, tomamos $w=(f(y)+\max(f(x),f(z)))/2$. Es estrictamente intermedio en cada par de salidas de $[x,y]$ y $[y,z]$. R5 entrega $s\in(x,y)$ y $t\in(y,z)$ con $f(s)=w=f(t)$; como $s<t$, contradice inyectividad. Si $f(y)<\min(f(x),f(z))$, usamos el punto medio entre esas dos cantidades y repetimos. Las posibilidades restantes son precisamente $f(x)<f(y)<f(z)$ o $f(z)<f(y)<f(x)$.

</details>

#### Ejercicio 32. Propagar una orientación

[]{#MA-EX-ANM-01-015-032}

Explica detalladamente cómo la propiedad entre triples de E031, junto con un par $a<b$ con $f(a)<f(b)$, fuerza $f(x)<f(y)$ para todo $x<y$ del intervalo.

[]{#MA-SOL-ANM-01-015-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Ordenamos los puntos distintos de $\{a,b,x,y\}$ como $t_1<\cdots<t_m$, con $2\le m\le4$. Si $m=2$, ambos pares son el mismo y la conclusión está dada. Si $m\ge3$, para cada triple consecutivo la propiedad implica que las diferencias adyacentes $f(t_{i+1})-f(t_i)$ y $f(t_{i+2})-f(t_{i+1})$ tienen igual signo estricto. Por propagación a lo largo de la lista todas tienen el mismo signo. Si fuese negativo, sumando las diferencias entre las posiciones de $a$ y $b$ resultaría $f(b)<f(a)$, contradicción. Todas son positivas; sumando entre $x$ e $y$ obtenemos $f(y)>f(x)$. El procedimiento trata puntos exteriores al par fijado y no se limita a un subintervalo.

</details>

#### Ejercicio 33. Barrera en un extremo del dominio

[]{#MA-EX-ANM-01-015-033}

Para $f:[0,1)\to\mathbb R$, $f(x)=x^2$, prueba continuidad de la inversa en el valor $0$ por una barrera de orden, sin invocar un teorema de raíces continuas. Da un radio para cada $\varepsilon>0$.

[]{#MA-SOL-ANM-01-015-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

La imagen es $J=[0,1)$: los cuadrados pertenecen a ese intervalo y cada $y\in J$ tiene raíz no negativa menor que $1$. La función es inyectiva creciente ahí, pues para $0\le x<z<1$, $z^2-x^2=(z-x)(z+x)>0$. Su inversa $h$ está definida. Si $0<\varepsilon<1$, tomamos el punto barrera $r=\varepsilon/2\in[0,1)$ y $\eta=r^2=\varepsilon^2/4$. Si $y\in J$ y $|y|<\eta$, su preimagen no puede ser $x\ge\varepsilon$, pues entonces $x>r$ y $y=x^2>r^2=\eta$. Así $|h(y)-h(0)|=x<\varepsilon$. Si $\varepsilon\ge1$, toda preimagen satisface $0\le x<1\le\varepsilon$, por lo que sirve $\eta=1$. No hay barrera izquierda porque todas las entradas son no negativas.

**Retorno visual.** Véase [C15-F06](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Crecimiento con salto

[]{#MA-EX-ANM-01-015-034}

Sea $k(x)=x$ si $x<0$ y $k(x)=x+1$ si $x\ge0$. Prueba estricto crecimiento, refuta continuidad en cero y calcula la imagen. ¿Qué premisa de R7 falta?

[]{#MA-SOL-ANM-01-015-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

En cada rama la diferencia entre salidas es la diferencia entre entradas y es positiva. Si $x<0\le z$, $k(x)=x<0<1\le z+1=k(z)$, así también crece entre ramas. Pero $k(0)=1$; dado $\delta>0$, $x=-\min(\delta/2,1/2)$ tiene $|x|<\delta$ y $|k(x)-k(0)|=1-x>1$, refutando continuidad con tolerancia $1$. La imagen es $(-\infty,0)\cup[1,\infty)$, no intervalo. Falta continuidad en la premisa de R7; estricto crecimiento solo no la garantiza.

</details>

#### Ejercicio 35. Por qué el dominio intervalar importa para la inversa

[]{#MA-EX-ANM-01-015-035}

Retoma $D=[0,1)\cup[2,3]$ y $f(x)=x$ en la primera pieza, $f(x)=x-1$ en la segunda. Prueba biyección continua a $[0,2]$ e inversa discontinua en $1$. Identifica exactamente qué hipótesis impide usar R7.

[]{#MA-SOL-ANM-01-015-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Las imágenes de las piezas son $[0,1)$ y $[1,2]$, disjuntas y exhaustivas de $[0,2]$; cada rama es inyectiva, de modo que $f$ es biyección. En cualquier centro de $D$, el radio $\delta=\min(1/2,\varepsilon)$ evita la otra pieza y dentro de la misma rama el error de salida es la distancia de entradas, menor que $\varepsilon$. Así $f$ es continua relativa. La inversa vale $h(y)=y$ para $y<1$ y $h(y)=y+1$ para $y\ge1$, luego $h(1)=2$. Dado $\eta>0$, $t=\min(\eta/2,1/2)>0$ da $y=1-t\in[0,1)$ con $|y-1|<\eta$ y $|h(y)-2|=1+t>1$. Falla continuidad con tolerancia $1$. $D$ omite puntos entre $0$ y $2$ y no es intervalo; ésa es la premisa faltante de R7.

</details>
## 15.8. Componentes: los intervalos máximos dentro de un dominio

[]{#MA-SEC-ANM-01-015-008}

Un conjunto no conexo puede contener muchas regiones conexas. Para describirlas sin escoger una familia de representantes usamos una relación determinada por el orden. Para $x,y\in D\subseteq\mathbb R$ escribimos

$$x\sim y\quad\Longleftrightarrow\quad[\min(x,y),\max(x,y)]\subseteq D.$$

**R8. Componentes reales.** Esta relación es de equivalencia. Es reflexiva porque $[x,x]=\{x\}\subseteq D$, y simétrica por su definición. Si $x\sim y$ y $y\sim z$, los dos segmentos están en $D$ y comparten $y$. Su unión es intervalo por §15.3 y contiene $x,z$; por eso contiene el segmento entre ellos. Esto prueba transitividad.

Para cada $x\in D$, la clase $C_x=\{y\in D:x\sim y\}$ es intervalo. Si $u,v\in C_x$, transitividad da $u\sim v$ y el segmento entre ellos está en $D$. Para cualquier punto $t$ de ese segmento, $u\sim t$, y con $x\sim u$ obtenemos $x\sim t$; por ello todo el segmento pertenece a $C_x$. La clase es conexa por R2.

Además es el mayor subconjunto conexo de $D$ que contiene $x$. Si $E\subseteq D$ es conexo y $x\in E$, R3 convierte $E$ en intervalo. Para $y\in E$, el segmento entre $x,y$ está en $E\subseteq D$, luego $y\in C_x$. Así $E\subseteq C_x$. Llamamos **componente conexa** a cada clase. Como clases de equivalencia, cubren $D$ y dos de ellas son iguales o disjuntas. Cada subconjunto conexo no vacío queda en una sola componente: se fija cualquiera de sus puntos y se aplica maximalidad. No hay que escoger un representante simultáneo por componente para definir la partición.

Cada componente es cerrada **relativa a $D$**, aunque puede no ser cerrada en $\mathbb R$. Para probarlo, tomemos $z\in D$ adherente a $C_x$, es decir, toda vecindad real de $z$ toca la clase. Si $z=x$ ya pertenece. Si $x<z$, todo $t$ con $x<t<z$ pertenece a $D$: la adherencia proporciona $w\in C_x$ con $|w-z|<(z-t)/2$, luego $w>t$, y el segmento entre $x$ y $w$ contiene $t$ y está en $D$. Junto a los extremos $x,z\in D$, esto prueba $[x,z]\subseteq D$, así $z\in C_x$. Para $z<x$ usamos una vecindad de radio $(t-z)/2$ para cada $z<t<x$, obteniendo un $w<t$ y el mismo argumento. Por el criterio de cerrado relativo de C04/C14, $C_x$ es cerrada relativa.

Las componentes no siempre son abiertas relativas. En

$$D=\{0\}\cup\{1/(n+1):n\in\mathbb N\},$$

todas son singletons: entre dos puntos positivos distintos hay un punto fuera de $D$, y entre cero y un punto positivo también. Se puede ver sin enumerar huecos uno por uno: todos los puntos de $D$ son racionales y la densidad de irracionales de C04 proporciona un punto omitido entre cada par distinto. Sin embargo, $\{0\}$ no es abierto relativo a $D$, porque toda vecindad de cero contiene algún $1/(n+1)>0$, por arquimedianidad. Cada singleton positivo sí es abierto relativo: sus vecinos consecutivos dejan un radio positivo de aislamiento. No confundimos singleton componente con punto aislado.

![Cada punto de D es una componente, porque entre dos puntos racionales distintos hay un irracional fuera de D. Los puntos positivos son aislados; cero no lo es. Los paneles muestran sólo muestras finitas; la arquimedianidad prueba que cualquier radio en cero contiene otro punto del dominio.](../../assets/books/anm/C15/C15-F07.svg){#fig-anm-c15-f07 fig-alt="Cada punto de D es una componente, porque entre dos puntos racionales distintos hay un irracional fuera de D. Los puntos positivos son aislados; cero no lo es. Los paneles muestran sólo muestras finitas; la arquimedianidad prueba que cualquier radio en cero contiene otro punto del dominio."}

En $\mathbb Q$ las componentes también son singletons por densidad irracional, pero ninguna es abierta relativa, por densidad racional. En $(0,1)$ hay una única componente, el conjunto entero, cerrada relativa a sí misma aunque no cerrada real. Son tres formas diferentes de leer el mismo criterio.

Finalmente, toda función continua transporta cada componente de su dominio a un conjunto conexo, que queda dentro de una componente de la imagen. Puede fusionar componentes: una función constante lo hace. Si la función es homeomorfismo, transporta componentes exactamente a componentes. En efecto, $f[C_x]$ es conexo y queda en la componente $K$ de $f(x)$; la inversa continua hace conexo $f^{-1}[K]$, que contiene $x$ y queda en $C_x$ por maximalidad. Aplicando $f$ obtenemos $K\subseteq f[C_x]$, y ambas inclusiones dan igualdad.

La caja de herramientas de C15 reúne tres niveles: un dominio conexo no admite separaciones; en la recta eso equivale a ser intervalo; la continuidad preserva esa indivisibilidad y produce valores intermedios. La compacidad de C16 resolverá una pregunta distinta: cómo reducir una familia de controles locales a información finita.

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-015-057}

¿Qué relación determina las componentes reales sin escoger representantes?

[]{#MA-MSOL-ANM-01-015-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

$x\sim y$ si el segmento entre $x$ y $y$ está contenido en $D$. Cada clase $C_x$ se define por esa fórmula; la familia de todas las clases existe como colección de subconjuntos de $D$ determinados por la relación.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-015-058}

¿Por qué es transitiva la relación por segmentos?

[]{#MA-MSOL-ANM-01-015-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

Los segmentos entre $x,y$ y entre $y,z$ están en $D$ y comparten $y$. Su unión es intervalo y contiene $x,z$, por lo que incluye el segmento entre ellos.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-015-059}

¿Cómo se prueba la maximalidad conexa de $C_x$?

[]{#MA-MSOL-ANM-01-015-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Si un conexo $E\subseteq D$ contiene $x$, R3 dice que es intervalo. Para cada $y\in E$, el segmento entre $x,y$ está en $E\subseteq D$, luego $y\in C_x$. Así $E\subseteq C_x$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-015-060}

¿Dos componentes diferentes pueden intersectarse?

[]{#MA-MSOL-ANM-01-015-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

No. Son clases de equivalencia; si compartieran $z$, cualquier miembro de una estaría relacionado con $z$ y por transitividad con los miembros de la otra. Las clases serían iguales.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-015-061}

¿En qué ambiente son siempre cerradas las componentes de $D$?

[]{#MA-MSOL-ANM-01-015-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

Relativamente a $D$. El argumento de adherencia exige que el punto adherente también esté en $D$; no incorpora puntos exteriores al dominio. Una componente como $(0,1)$ no es cerrada real.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-015-062}

¿Por qué $\{0\}$ no es abierta relativa en $\{0\}\cup\{1/(n+1):n\in\mathbb N\}$?

[]{#MA-MSOL-ANM-01-015-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

Para todo $r>0$, por arquimedianidad existe $n$ con $0<1/(n+1)<r$. La vecindad de cero en el dominio siempre contiene otro punto. Aun así $\{0\}$ es una componente.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-015-063}

¿Cuáles son las componentes de $\mathbb Q$ y son abiertas relativas?

[]{#MA-MSOL-ANM-01-015-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

Son singletons, porque entre dos racionales distintos hay un irracional omitido. Ningún singleton es abierto relativo: todo radio alrededor de un racional contiene otro racional por densidad.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-015-064}

¿Qué refuerzo garantiza transporte exacto de componentes y no sólo inclusión?

[]{#MA-MSOL-ANM-01-015-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Que la función sea homeomorfismo. Continuidad lleva una componente a un conexo contenido en una componente de la imagen; continuidad de la inversa y maximalidad dan la inclusión contraria. Una constante puede fusionar componentes.

</details>

### Ejercicios de la sección 15.8

#### Ejercicio 36. Relación por segmentos

[]{#MA-EX-ANM-01-015-036}

Prueba reflexividad, simetría y transitividad de $x\sim y\Leftrightarrow[\min(x,y),\max(x,y)]\subseteq D$. Después prueba que cada clase es intervalo.

[]{#MA-SOL-ANM-01-015-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Reflexividad usa $[x,x]=\{x\}\subseteq D$; simetría usa que min/max no cambian al permutar. Si $x\sim y$ y $y\sim z$, los dos segmentos comparten $y$ y su unión es intervalo contenido en $D$, por §15.3; contiene $x,z$, luego también el segmento entre ellos. Así $x\sim z$. Si $u,v$ están en $C_x$, transitividad da $u\sim v$. Todo $t$ entre ellos está en $D$ y satisface $u\sim t$ porque su segmento con $u$ queda en el de $u,v$. De $x\sim u$ resulta $x\sim t$, así $t\in C_x$. Es intervalo.

</details>

#### Ejercicio 37. Un dominio con tres componentes

[]{#MA-EX-ANM-01-015-037}

Determina y justifica las componentes de $D=(-2,-1]\cup\{0\}\cup[1,3)$. Indica cuáles son abiertas relativas y cuáles cerradas relativas.

[]{#MA-SOL-ANM-01-015-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Las tres piezas son intervalos, luego conexas. Ningún conexo de $D$ puede tocar dos piezas: si tocara la izquierda y otra, omitiría un punto entre $-1$ y $0$, como $-1/2$; si tocara cero y la derecha, omitiría $1/2$. Por R3 no sería conexo. Cada pieza es por tanto máxima y es componente. Son todas abiertas relativas: la izquierda es $D\cap(-\infty,-1/2)$, el singleton $D\cap(-1/2,1/2)$ y la derecha $D\cap(1/2,\infty)$. También son cerradas relativas por R8 o porque el complemento de cada una es unión de las otras dos abiertas relativas. No todas son cerradas reales, pues los extremos $-2$ y $3$ faltan.

</details>

#### Ejercicio 38. Componentes acumuladas sin apertura

[]{#MA-EX-ANM-01-015-038}

Para $D=\{0\}\cup\{1/(n+1):n\in\mathbb N\}$, prueba que todas las componentes son singletons. Decide apertura relativa de cada una y explica por qué cerradura relativa no basta para apertura.

[]{#MA-SOL-ANM-01-015-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Todos los puntos de $D$ son racionales. Entre dos distintos hay un irracional por densidad de irracionales; éste no pertenece a $D$. El segmento entre los puntos no queda en $D$, así ninguna clase contiene dos puntos. Para $t_n=1/(n+1)$ con $n\ge1$, las distancias a sus vecinos $t_{n-1}$ y $t_{n+1}$ son positivas; la mitad del menor de ellas da una bola relativa que sólo contiene $t_n$. Para $n=0$, basta la mitad de $t_0-t_1=1/2$, es decir $1/4$, pues todos los otros positivos son a lo sumo $1/2$. Así los singletons positivos son abiertos relativos. $\{0\}$ no lo es: para cada $r>0$, arquimedianidad da $n$ con $0<t_n<r$. Todos los singletons son cerrados reales y por ello relativos, pero sólo la apertura de una vecindad determina aislamiento. La componente de cero es cerrada sin ser abierta relativa.

**Retorno visual.** Véase [C15-F07](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 39. Cerradura relativa desde la adherencia

[]{#MA-EX-ANM-01-015-039}

Prueba que una componente $C_x$ es cerrada relativa a $D$ usando un punto $z\in D$ adherente a ella. Desarrolla ambos órdenes de $x,z$ y refuta la afirmación de cerradura absoluta universal.

[]{#MA-SOL-ANM-01-015-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Si $z=x$, ya está en $C_x$. Si $x<z$, para todo $x<t<z$ la adherencia da $w\in C_x$ con $|w-z|<(z-t)/2$, así $w>t$. Como el segmento entre $x,w$ está en $D$, $t\in D$. Los extremos $x,z$ pertenecen a $D$, así $[x,z]\subseteq D$ y $z\in C_x$. Si $z<x$, para $z<t<x$ usamos radio $(t-z)/2$ alrededor de $z$, obteniendo $w<t$ en $C_x$; el segmento entre $w,x$ contiene $t$ y está en $D$. De nuevo $[z,x]\subseteq D$, luego $z\in C_x$. Todos los puntos adherentes que están en $D$ quedan en la clase, criterio de cierre relativo. En $D=(0,1)$ hay una componente única $(0,1)$, cerrada relativa a sí misma pero no cerrada real porque cero es adherente exterior.

</details>

#### Ejercicio 40. Transportar o fusionar componentes

[]{#MA-EX-ANM-01-015-040}

Prueba que un homeomorfismo transporta exactamente las componentes de su dominio a las de su codominio. Da una continua que fusione dos componentes y explica qué paso de la prueba deja de funcionar.

[]{#MA-SOL-ANM-01-015-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Sea $f:D\to H$ homeomorfismo, $C$ componente de $x$. R4 hace conexo $f[C]$, que contiene $f(x)$ y queda en la componente $K$ de ese punto por maximalidad. La inversa continua hace conexo $f^{-1}[K]$, que contiene $x$ y por maximalidad está en $C$. Aplicando la biyección $f$ obtenemos $K\subseteq f[C]$, y las dos inclusiones dan igualdad. La constante $\{-1,1\}\to\{0\}$ es continua en el dominio relativo y fusiona sus dos componentes singleton en una sola. No existe inversa funcional, mucho menos continua, por lo que no puede transportarse $K$ hacia atrás para aplicar maximalidad. Una continua general sólo garantiza imagen conexa dentro de una componente.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-15)

[← Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Capítulo 16 →](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html)
