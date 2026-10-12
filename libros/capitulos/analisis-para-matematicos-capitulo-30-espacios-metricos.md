---
content-id: MA-BCH-0322
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-030
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
title: Capítulo 30 — Espacios métricos
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C30.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-30)

C1 separó orden y distancia; C4,C6,C10 yC14 construyeron ventanas, convergencia, Cauchy y continuidad. Ahora reconstruiremos esas pruebas cuando los puntos sólo tienen una métrica. El destino debe vivir en su espacio, y las recíprocas secuenciales declaran selección de testigos. C31 queda como única puerta siguiente.

## 30.1. Conservar la distancia, soltar las coordenadas

[]{#MA-SEC-ANM-01-030-001}

En la recta, muchas pruebas parecían usar simultáneamente orden, operaciones y distancia. Ahora preguntamos cuáles sobreviven cuando los puntos ya no son números. El conjunto puede estar formado por palabras, funciones o configuraciones; la información disponible será una distancia real entre cada par.

Una **métrica** en un conjunto $X$ es una función $d:X\times X\to[0,\infty)$ que, para todos $x,y,z\in X$, cumple
$$d(x,y)=0\iff x=y,\qquad d(x,y)=d(y,x),\qquad d(x,z)\le d(x,y)+d(y,z).$$
El par $(X,d)$ es un espacio métrico. Las distancias son números reales finitos; los puntos no necesitan sumar, restar ni compararse por un orden. El espacio vacío satisface los axiomas de modo vacuo, pero no tiene sucesiones ni centros. Declararemos no vacío el dominio cuando necesitemos un punto de referencia.

La métrica usual $d(x,y)=|x-y|$ en $\mathbb R$ cumple los axiomas por C1. La restricción a cualquier subconjunto conserva las tres propiedades. Así $\mathbb Q$ y $(0,1)$ tienen métricas usuales sin heredar por ello todas las propiedades globales de $\mathbb R$.

**La métrica discreta** en cualquier conjunto es $d_D(x,y)=0$ si $x=y$, y $1$ en otro caso. Positividad y simetría son inmediatas. Si los extremos son distintos, cualquier punto intermedio coincide con uno de ellos o es distinto de ambos; la suma de las dos distancias es respectivamente $1$ o $2$, y domina a $1$. Si los extremos coinciden, la triangular tiene lado izquierdo cero. La prueba cubre todos los triples, no sólo una muestra finita.

**Palabras binarias.** Para $X=\{0,1\}^m$, con $m\ge1$ fijo, la distancia de Hamming cuenta coordenadas diferentes. Si $x_i\ne z_i$, no pueden cumplirse a la vez $x_i=y_i$ y $y_i=z_i$. Por tanto
$$\mathbf1_{\{x_i\ne z_i\}}\le\mathbf1_{\{x_i\ne y_i\}}+\mathbf1_{\{y_i\ne z_i\}}.$$
Sumar las $m$ desigualdades prueba la triangular; las otras propiedades son directas. La proximidad mide coincidencia de símbolos, sin necesidad de una recta que ordene las palabras.

**Diagnosticar propuestas.** $|x-y|^2$ no es una métrica en $\mathbb R$: entre $0,1,2$, el trayecto directo cuesta $4$ y el desvío cuesta $1+1$. Una función no negativa y simétrica que vale cero en la diagonal todavía puede fallar. Asimismo $p((a,b),(c,e))=|a-c|$ en $\mathbb R^2$ satisface triangular y simetría, pero distancia cero no distingue puntos con primera coordenada igual. Es una pseudométrica, no una métrica sobre ese conjunto. Si se omitiera la separación, la unicidad de límites que probaremos después perdería su conclusión de igualdad de puntos.

**La primera herramienta universal.** De la triangular, primero en un sentido y luego en el otro,
$$|d(x,a)-d(y,a)|\le d(x,y).$$
Aquí sí restamos números: los valores reales de la distancia, no los puntos $x,y$. Esta desigualdad triangular inversa permitirá cambiar centros, abrir ventanas y demostrar continuidad sin coordenadas.

![Las palabras000,101 y111 tienen distancias de Hamming2,1 y3. Cada columna contribuye según desacuerdo de símbolos; el triángulo directo3 coincide con el desvío2+1. La propuesta cuadrática real falla en0,1,2: directo4 y desvío1+1. El primer mecanismo se prueba para todas las coordenadas; el segundo es un contraejemplo completo.](../../assets/books/anm/C30/C30-F01.svg){#fig-anm-c30-f01 fig-alt="Las palabras000,101 y111 tienen distancias de Hamming2,1 y3. Cada columna contribuye según desacuerdo de símbolos; el triángulo directo3 coincide con el desvío2+1. La propuesta cuadrática real falla en0,1,2: directo4 y desvío1+1. El primer mecanismo se prueba para todas las coordenadas; el segundo es un contraejemplo completo."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-030-001}

¿Qué estructura deben tener los puntos de un espacio métrico?

[]{#MA-MSOL-ANM-01-030-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Sólo pertenecer a un conjunto con una métrica; no se exige orden ni operaciones.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-030-002}

¿Qué tipo de números son las distancias?

[]{#MA-MSOL-ANM-01-030-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Reales no negativos y finitos.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-030-003}

¿Qué axioma impide distancia cero entre puntos distintos?

[]{#MA-MSOL-ANM-01-030-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

La separación: $d(x,y)=0$ si y sólo si $x=y$.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-030-004}

¿Por qué la discreta cumple triangular?

[]{#MA-MSOL-ANM-01-030-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

Entre extremos distintos, el desvío cuesta uno o dos y domina la distancia uno.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-030-005}

¿Qué cuenta Hamming?

[]{#MA-MSOL-ANM-01-030-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Coordenadas diferentes en palabras de longitud fija.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-030-006}

¿Qué triple refuta la distancia usual al cuadrado?

[]{#MA-MSOL-ANM-01-030-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

$0,1,2$: la distancia directa es cuatro y el desvío suma dos.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-030-007}

¿Qué se resta en la triangular inversa?

[]{#MA-MSOL-ANM-01-030-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

Valores reales de distancias, no puntos abstractos.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-030-008}

¿Una restricción de una métrica sigue siendo métrica?

[]{#MA-MSOL-ANM-01-030-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

Sí. Conserva sus tres propiedades en todos los triples del subconjunto.

</details>

### Ejercicios de la sección 30.1

[]{#ejercicios-30}

#### Ejercicio 1. Tres distancias de Hamming

[]{#MA-EX-ANM-01-030-001}

En palabras binarias de longitud tres, calcule las distancias entre $x=000$, $y=101$ y $z=111$, y compruebe las tres triangulares de este triple.

[]{#MA-SOL-ANM-01-030-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

$d_H(x,y)=2$, $d_H(y,z)=1$ y $d_H(x,z)=3$. Las tres desigualdades son $3\le2+1$, $2\le3+1$ y $1\le2+3$. La primera es igualdad. Este cotejo acredita ese triple; la propiedad para todas las palabras se demuestra mediante indicadores de desacuerdo en cada coordenada, no mediante esta sola muestra.

**Retorno visual.** Véase [C30-F01](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 2. Separación de una pseudométrica

[]{#MA-EX-ANM-01-030-002}

Pruebe que $p((a,b),(c,e))=|a-c|$ cumple simetría y triangular, y refute que sea métrica. Exhiba una sucesión con dos destinos diferentes para sus distancias.

[]{#MA-SOL-ANM-01-030-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

La simetría y la triangular son las del valor absoluto en la primera coordenada. Pero $p((0,0),(0,1))=0$ con puntos distintos. La sucesión constante $(0,0)$ tiene distancia cero tanto a $(0,0)$ como a $(0,1)$ en todos sus términos, así que satisface ambos contratos de convergencia formulados con $p$. La separación es la hipótesis que convierte distancia cero en igualdad y protege la unicidad métrica.

</details>

#### Ejercicio 3. La distancia al cuadrado

[]{#MA-EX-ANM-01-030-003}

Identifique exactamente el axioma que falla para $s(x,y)=|x-y|^2$ en $\mathbb R$. Compare con $2|x-y|$.

[]{#MA-SOL-ANM-01-030-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

La propuesta cuadrática es no negativa, separa puntos y es simétrica. Falla la triangular: $s(0,2)=4> s(0,1)+s(1,2)=2$. En cambio $2|x-y|$ multiplica por un escalar positivo todas las propiedades de la métrica usual; la triangular usual multiplicada por dos sigue válida. Escalar una distancia por una constante positiva difiere de elevarla al cuadrado.

</details>

#### Ejercicio 4. Un triple finito completo

[]{#MA-EX-ANM-01-030-004}

En $X=\{a,b,c\}$ fije distancias simétricas $d(a,b)=2$, $d(b,c)=3$, $d(a,c)=t>0$ y diagonal cero. Determine exactamente los valores de $t$ que dan métrica.

[]{#MA-SOL-ANM-01-030-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Para triples con alguna repetición, la triangular se reduce a igualdad o a no negatividad. Para tres puntos distintos hay sólo tres desigualdades: $t\le2+3$, $2\le3+t$ y $3\le2+t$. La segunda vale para todo $t>0$; las otras exigen $t\le5$ y $t\ge1$. Por tanto exactamente $1\le t\le5$. Positividad fuera de diagonal y simetría ya están declaradas. Aquí sí se ha agotado el universo finito de triples.

</details>

#### Ejercicio 5. Triangular inversa a dos centros

[]{#MA-EX-ANM-01-030-005}

Demuestre $|d(x,y)-d(a,b)|\le d(x,a)+d(y,b)$ y señale qué objetos se restan.

[]{#MA-SOL-ANM-01-030-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

La triangular iterada da $d(x,y)\le d(x,a)+d(a,b)+d(b,y)$, por lo que $d(x,y)-d(a,b)\le d(x,a)+d(y,b)$. Intercambiar los dos pares da $d(a,b)-d(x,y)\le d(x,a)+d(y,b)$. Reunir ambas desigualdades prueba la cota absoluta. Se restan valores reales finitos de la métrica; no se supone una resta de puntos en $X$.

</details>
## 30.2. Bolas y el margen de una ventana

[]{#MA-SEC-ANM-01-030-002}

Para $a\in X$ y $r>0$, definimos la bola abierta y la bola cerrada métrica
$$B_d(a,r)=\{x\in X:d(x,a)<r\},\qquad C_d(a,r)=\{x\in X:d(x,a)\le r\}.$$
La segunda notación evita confundirla con la clausura de la primera, que no siempre coincide con ella. El centro pertenece a ambas; aumentar el radio amplía cada bola por monotonía de la desigualdad.

**Una entrada interior conserva margen.** Si $y\in B_d(a,r)$, la cantidad $\eta=r-d(a,y)$ es positiva. Para $z\in B_d(y,\eta)$,
$$d(a,z)\le d(a,y)+d(y,z)<d(a,y)+\eta=r.$$
Por tanto $B_d(y,\eta)\subset B_d(a,r)$. La forma concreta de la bola puede cambiar; el margen nace siempre de la triangular. Más generalmente, $B_d(y,s)\subset B_d(a,r)$ cuando $d(a,y)+s\le r$ y $s>0$, porque la pertenencia a la primera bola aporta una desigualdad estricta. La inclusión puede darse sin esa condición suficiente, por ejemplo en espacios discretos.

Un conjunto $V\subset X$ es una vecindad de $a$ si contiene alguna bola abierta centrada en $a$. Puede tener componentes adicionales y no necesita ser una bola. El enunciado es local: se exige una ventana positiva alrededor del punto, no una forma particular del conjunto completo.

**Dos geometrías sin una norma presupuesta.** Para pares $x=(x_1,x_2)$, $y=(y_1,y_2)$, definimos
$$d_1(x,y)=|x_1-y_1|+|x_2-y_2|,\qquad d_\infty(x,y)=\max\{|x_1-y_1|,|x_2-y_2|\}.$$
Positividad y separación se leen coordenada a coordenada; simetría procede del valor absoluto. Para $d_1$, sumamos las dos triangulares reales. Para $d_\infty$, cada diferencia de coordenadas es a lo sumo $d_\infty(x,z)+d_\infty(z,y)$; el máximo conserva esa cota. Las bolas unitarias en el origen son respectivamente un rombo abierto y un cuadrado abierto. No se deduce una métrica de una figura: las desigualdades ya la probaron.

En la métrica discreta, $B_D(a,r)=\{a\}$ cuando $0<r\le1$, y $B_D(a,r)=X$ cuando $r>1$. En el radio exactamente $1$, todos los otros puntos están excluidos. En cambio $C_D(a,1)=X$. No hay una interpolación entre radios que produzca una región gradual de puntos.

**Una bola cerrada es cerrada.** Anticipando la definición por complemento que formalizaremos enseguida, si $x\notin C_d(a,r)$, el radio $s=(d(x,a)-r)/2>0$ cumple, para $d(x,y)<s$,
$$d(y,a)\ge d(x,a)-d(x,y)>d(x,a)-s>r.$$
Así la ventana alrededor de $x$ queda en el complemento. Esto prueba cierre de $C_d(a,r)$, pero no igualdad con la clausura de $B_d(a,r)$. En un espacio discreto de al menos dos puntos, la bola abierta de radio $1$ es el singleton $\{a\}$, ya cerrado, mientras la bola cerrada de ese radio es todo $X$.

![Las bolas unidad de d1 y d∞ en el origen son rombo y cuadrado, con fronteras excluidas. La entrada(1/2,1/2) pertenece al cuadrado y queda en la frontera del rombo. En la discreta, la bola abierta de radio1 sólo contiene el centro y la cerrada de radio1 contiene todos los puntos del conjunto ilustrado. Abierto/cerrado se codifica con formas además de color.](../../assets/books/anm/C30/C30-F02.svg){#fig-anm-c30-f02 fig-alt="Las bolas unidad de d1 y d∞ en el origen son rombo y cuadrado, con fronteras excluidas. La entrada(1/2,1/2) pertenece al cuadrado y queda en la frontera del rombo. En la discreta, la bola abierta de radio1 sólo contiene el centro y la cerrada de radio1 contiene todos los puntos del conjunto ilustrado. Abierto/cerrado se codifica con formas además de color."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-030-009}

¿Qué desigualdad define una bola abierta?

[]{#MA-MSOL-ANM-01-030-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

$d(x,a)<r$ con radio $r>0$ y entrada $x\in X$.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-030-010}

¿Qué radio interior entrega un punto $y\in B(a,r)$?

[]{#MA-MSOL-ANM-01-030-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

$r-d(a,y)>0$.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-030-011}

¿Por qué ese radio produce inclusión de bolas?

[]{#MA-MSOL-ANM-01-030-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

La triangular suma la distancia del centro a $y$ y una distancia menor que el margen.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-030-012}

¿Una vecindad tiene que ser una bola?

[]{#MA-MSOL-ANM-01-030-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

No. Basta que contenga una bola positiva del centro.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-030-013}

¿Qué forma tiene la bola unidad de $d_1$ en el plano?

[]{#MA-MSOL-ANM-01-030-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

Un rombo abierto definido por $|x_1|+|x_2|<1$.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-030-014}

¿Qué forma tiene la bola unidad de $d_\infty$?

[]{#MA-MSOL-ANM-01-030-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Un cuadrado abierto con ambas coordenadas de magnitud menor que uno.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-030-015}

¿Cuánto contiene $B_D(a,1)$?

[]{#MA-MSOL-ANM-01-030-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

Sólo el centro, porque los otros puntos tienen distancia exactamente uno.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-030-016}

¿Bola cerrada y clausura de bola abierta siempre coinciden?

[]{#MA-MSOL-ANM-01-030-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

No. En la discreta con varios puntos y radio uno, la primera es todo el espacio y la segunda sólo el centro.

</details>

### Ejercicios de la sección 30.2

#### Ejercicio 6. Bolas con dos formas

[]{#MA-EX-ANM-01-030-006}

Describa las bolas abiertas de radio $2$ centradas en $(1,-1)$ para $d_1$ y $d_\infty$. Decida pertenencia de $(2,0)$ y $(3,-1)$.

[]{#MA-SOL-ANM-01-030-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

La primera región es $|x_1-1|+|x_2+1|<2$, un rombo con frontera excluida. La segunda es $-1<x_1<3$ y $-3<x_2<1$, un cuadrado abierto. Para $(2,0)$ las distancias son $2$ y $1$: no pertenece a la primera y sí a la segunda. Para $(3,-1)$ ambas distancias son $2$, de modo que está excluido de ambas bolas abiertas y pertenece a ambas bolas cerradas del mismo radio.

**Retorno visual.** Véase [C30-F02](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 7. El radio de margen

[]{#MA-EX-ANM-01-030-007}

Si $d(a,y)=3/5$ y $r=1$, pruebe $B(y,2/5)\subset B(a,1)$. ¿Puede incluirse el borde de la bola pequeña sin más información?

[]{#MA-SOL-ANM-01-030-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Para $d(y,z)<2/5$, la triangular da $d(a,z)\le3/5+d(y,z)<1$. Si se permite $d(y,z)=2/5$, sólo queda $d(a,z)\le1$. En la recta usual tome $a=0$, $y=3/5$ y $z=1$: está en la bola pequeña cerrada, pero no en la grande abierta. La pertenencia estricta de la ventana pequeña paga la desigualdad estricta final.

</details>

#### Ejercicio 8. Clausura de una bola discreta

[]{#MA-EX-ANM-01-030-008}

En un espacio discreto con al menos dos puntos, compare $B_D(a,1)$, $C_D(a,1)$ y $\operatorname{cl} B_D(a,1)$.

[]{#MA-SOL-ANM-01-030-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

La bola abierta contiene sólo $a$, porque los otros puntos distan exactamente uno. La cerrada contiene todo $X$. Todo singleton es cerrado, pues cada punto distinto tiene su propia bola de radio $1/2$ que evita a $a$. Así la clausura de la bola abierta es $\{a\}$, diferente de la bola cerrada. La notación de clausura no debe confundirse con una desigualdad no estricta en una definición de bola.

</details>

#### Ejercicio 9. Dos ventanas separadas

[]{#MA-EX-ANM-01-030-009}

Si $D=d(a,b)>0$, pruebe que $B(a,D/3)$ y $B(b,D/3)$ son disjuntas. Generalice a radios positivos cuya suma es a lo sumo $D$.

[]{#MA-SOL-ANM-01-030-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Una entrada común $z$ daría $D\le d(a,z)+d(z,b)<2D/3$, imposible. Para radios $r,s>0$ con $r+s\le D$, la misma entrada daría $D<r+s\le D$. No hace falta localizar un punto medio ni usar un orden de los centros; las dos pertenencias estrictas y la triangular bastan.

</details>

#### Ejercicio 10. Una bola cerrada es cerrada

[]{#MA-EX-ANM-01-030-010}

Reconstruya la prueba del cierre de $C_d(a,r)$ y explique por qué no demuestra que sea la clausura de $B_d(a,r)$.

[]{#MA-SOL-ANM-01-030-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Para $x$ fuera de la bola cerrada, $s=(d(x,a)-r)/2>0$. Si $d(x,y)<s$, la triangular inversa da $d(y,a)>d(x,a)-s>r$, así que la bola de $x$ queda en el complemento. Éste es abierto y la bola cerrada es cerrada. Como contiene a la bola abierta, contiene su clausura; la prueba sólo da esa inclusión. La métrica discreta en radio uno proporciona inclusión estricta.

</details>
## 30.3. Abiertos, cerrados y ambiente relativo

[]{#MA-SEC-ANM-01-030-003}

Un conjunto $U\subset X$ es **abierto** si cada $x\in U$ tiene un radio $r>0$ con $B_d(x,r)\subset U$. Es **cerrado** si $X\setminus U$ es abierto. Por esta definición, $\varnothing$ y $X$ son abiertos y cerrados. Una bola abierta es abierta por el margen de §30.2.

**Reunir regiones.** La unión arbitraria de abiertos es abierta: una entrada de la unión pertenece a alguno de sus miembros y usa el radio de ese miembro. La intersección de una cantidad finita de abiertos es abierta: para un punto común, tomamos el mínimo positivo de sus radios. La intersección vacía es $X$. Una intersección infinita puede perder todo radio: en la recta, $\bigcap_{n\ge0}(-1/(n+1),1/(n+1))=\{0\}$. Los complementos dan intersecciones arbitrarias y uniones finitas de cerrados.

**Interior y clausura.** El interior $\operatorname{int}_X A$ contiene puntos de $A$ con una bola completa dentro de $A$. Es abierto por el lema del margen y es el mayor abierto contenido en $A$. La clausura $\operatorname{cl}_X A$ contiene puntos $x\in X$ tales que cada bola centrada en $x$ encuentra a $A$:
$$x\in\operatorname{cl}_X A\iff\forall r>0:\ B_d(x,r)\cap A\ne\varnothing.$$
Contiene $A$. Su complemento es abierto: si una bola $B_d(x,r)$ evita $A$, cualquier $y$ de esa bola tiene una bola alrededor de sí contenida en ella, y por ello también queda fuera de la clausura. Así la clausura es cerrada. Si $F$ es cerrado y contiene $A$, un punto fuera de $F$ tiene una bola que evita $F$, luego evita $A$; no pertenece a la clausura. Esto prueba que la clausura es el menor cerrado que contiene $A$. En particular $A$ es cerrado si y sólo si $A=\operatorname{cl}_X A$.

La frontera es $\partial_X A=\operatorname{cl}_X A\cap\operatorname{cl}_X(X\setminus A)$. Sus puntos encuentran ambos conjuntos en cualquier ventana. Puesto que $x\notin\operatorname{cl}_X(X\setminus A)$ equivale a tener una bola dentro de $A$, también
$$\partial_X A=\operatorname{cl}_X A\setminus\operatorname{int}_X A.$$
Es cerrada por intersección de cerrados. No depende de que exista una orientación izquierda/derecha.

**Cambiar el ambiente.** Un subconjunto $Y\subset X$ lleva la métrica restringida. Sus bolas son exactamente $B_Y(y,r)=Y\cap B_X(y,r)$. Para $A\subset Y$,
$$A\text{ abierto en }Y\iff A=Y\cap U\text{ para algún abierto }U\subset X.$$
La ida construye $U$ como la unión de todas las bolas de $X$ con centro en $A$ y cuya intersección con $Y$ quede en $A$. Cada centro tiene al menos una, sin elegir un radio simultáneamente para cada punto. La vuelta usa una bola interior de $U$ en cada punto. Complementar dentro de $Y$ da la representación de cerrados relativos como $Y\cap F$. Además, la fórmula de bolas demuestra directamente
$$\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A.$$
Interior y frontera requieren también el complemento correcto: no se obtienen en general intersectando los correspondientes objetos de $X$ con $Y$.

Por ejemplo, $Y=[0,1]$ y $A=[0,1/2)$ con distancia usual. En $Y$, $A$ es abierto, su clausura es $[0,1/2]$ y su frontera es sólo $\{1/2\}$. En toda la recta su interior es $(0,1/2)$ y su frontera es $\{0,1/2\}$. La etiqueta del ambiente cambia una conclusión concreta.

![Para A=\[0,1/2), el ambienteR da frontera{0,1/2}, mientras Y=\[0,1\] da frontera{1/2}. El punto0 pertenece aA en ambos, pero enY es interior relativo. Las bandas distinguen conjunto, ambiente y marcadores de frontera; no se obtiene frontera relativa sólo intersectando la absoluta.](../../assets/books/anm/C30/C30-F03.svg){#fig-anm-c30-f03 fig-alt="Para A=\[0,1/2), el ambienteR da frontera{0,1/2}, mientras Y=\[0,1\] da frontera{1/2}. El punto0 pertenece aA en ambos, pero enY es interior relativo. Las bandas distinguen conjunto, ambiente y marcadores de frontera; no se obtiene frontera relativa sólo intersectando la absoluta."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-030-017}

¿Cómo se define abierto sin coordenadas?

[]{#MA-MSOL-ANM-01-030-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

Cada punto del conjunto posee una bola abierta completa contenida en él.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-030-018}

¿Qué operación arbitraria conserva abiertos?

[]{#MA-MSOL-ANM-01-030-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

La unión; cada entrada reutiliza un radio de un miembro.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-030-019}

¿Por qué sólo se promete intersección finita de abiertos?

[]{#MA-MSOL-ANM-01-030-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

El mínimo de finitísimos radios positivos es positivo; una familia infinita puede dejar sólo radio cero.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-030-020}

¿Qué exige pertenecer a la clausura?

[]{#MA-MSOL-ANM-01-030-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

Que cada bola del punto encuentre al conjunto.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-030-021}

¿Qué caracteriza la frontera?

[]{#MA-MSOL-ANM-01-030-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

Cada bola encuentra tanto el conjunto como su complemento dentro del ambiente declarado.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-030-022}

¿Qué bola tiene un subespacio $Y$?

[]{#MA-MSOL-ANM-01-030-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

$B_Y(y,r)=Y\cap B_X(y,r)$.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-030-023}

¿Cómo cambia la clausura al restringir el ambiente?

[]{#MA-MSOL-ANM-01-030-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

$\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A$ para $A\subset Y$.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-030-024}

¿El interior relativo se obtiene siempre intersectando el absoluto?

[]{#MA-MSOL-ANM-01-030-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

No. Un extremo del propio subespacio puede ser interior relativo sin ser interior absoluto.

</details>

### Ejercicios de la sección 30.3

#### Ejercicio 11. Un borde que depende del ambiente

[]{#MA-EX-ANM-01-030-011}

Para $A=[0,1/2)$ calcule interior, clausura y frontera en $\mathbb R$ y en $Y=[0,1]$.

[]{#MA-SOL-ANM-01-030-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

En $\mathbb R$, interior $(0,1/2)$, clausura $[0,1/2]$ y frontera $\{0,1/2\}$. En $Y$, $A=Y\cap(-1,1/2)$ es abierto relativo, así que es su propio interior. La fórmula de clausura relativa deja $[0,1/2]$ y la frontera es $\{1/2\}$. El punto cero tiene una ventana relativa completa dentro de $A$, aunque no tenga una ventana de la recta dentro de $A$.

**Retorno visual.** Véase [C30-F03](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 12. Uniones e intersecciones

[]{#MA-EX-ANM-01-030-012}

Pruebe unión arbitraria e intersección finita de abiertos. Refute la extensión a intersecciones infinitas con un ejemplo exacto.

[]{#MA-SOL-ANM-01-030-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Una entrada de una unión pertenece a un miembro y reutiliza su radio. En una intersección finita no vacía, cada punto tiene finitísimos radios positivos y su mínimo protege simultáneamente todas las condiciones. La intersección de familia vacía es el abierto $X$. En la recta, los intervalos $(-1/(n+1),1/(n+1))$ tienen intersección $\{0\}$: cero pertenece a todos, mientras para cualquier $x\ne0$ existe $n$ con $1/(n+1)<|x|$. Ninguna bola real positiva alrededor de cero cabe en el singleton, que no es abierto.

</details>

#### Ejercicio 13. Todo abierto y todo cerrado

[]{#MA-EX-ANM-01-030-013}

Demuestre que en un espacio discreto todos los subconjuntos son abiertos y cerrados. Calcule su frontera.

[]{#MA-SOL-ANM-01-030-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Para $a\in A$, $B_D(a,1/2)=\{a\}\subset A$, así que $A$ es abierto. Su complemento satisface el mismo argumento, luego $A$ es cerrado. Interior y clausura de $A$ son ambos $A$, por lo que la frontera $\operatorname{cl}A\setminus\operatorname{int}A$ es vacía. Esto vale también para vacío y espacio completo.

</details>

#### Ejercicio 14. Clausura por ventanas

[]{#MA-EX-ANM-01-030-014}

Pruebe que $\operatorname{cl}_X A$ es cerrada y el menor cerrado que contiene a $A$, directamente por bolas.

[]{#MA-SOL-ANM-01-030-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Contiene $A$ porque cada bola de un punto de $A$ contiene al propio punto. Si $x$ está fuera de la clausura, alguna bola $B(x,r)$ evita $A$. Para cada $y$ en ella, el margen produce una bola alrededor de $y$ contenida en $B(x,r)$, también disjunta de $A$. Así toda la bola original queda fuera de la clausura y su complemento es abierto. Si un cerrado $F$ contiene $A$, cada punto fuera de $F$ tiene una bola que evita $F$ y por ello evita $A$; no puede pertenecer a la clausura. Luego ésta está contenida en todo tal $F$.

</details>

#### Ejercicio 15. Intersecar la clausura, no el interior

[]{#MA-EX-ANM-01-030-015}

Pruebe $\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A$ para $A\subset Y\subset X$. Refute la fórmula análoga para interiores.

[]{#MA-SOL-ANM-01-030-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Para $y\in Y$, la intersección $B_Y(y,r)\cap A$ es igual a $B_X(y,r)\cap A$, porque $A\subset Y$. La no vaciedad para cada radio es entonces la misma condición, con la pertenencia a $Y$ añadida. Para el interior, tome $A=Y=[0,1]$ en $X=\mathbb R$. El interior en $Y$ es todo $Y$, mientras $Y\cap\operatorname{int}_X A=(0,1)$. El ambiente cambia los puntos admisibles de la ventana, y con ellos la inclusión completa dentro de $A$.

</details>
## 30.4. Convergencia con un destino en el espacio

[]{#MA-SEC-ANM-01-030-004}

Una sucesión en $X$ es una función $x:\mathbb N_0\to X$. Converge a $a\in X$ si
$$\forall\varepsilon>0\ \exists N\ \forall n\ge N:\quad d(x_n,a)<\varepsilon.$$
El destino debe pertenecer al espacio declarado. La condición equivale a captura eventual por cada vecindad de $a$: una vecindad contiene una bola, y cada bola es una vecindad. No se requiere que los puntos tengan coordenadas o puedan restarse.

**Unicidad sin orden.** Si hubiera dos destinos $a\ne b$, su separación $D=d(a,b)>0$ permitiría pedir a ambas convergencias tolerancia $D/3$. Después del máximo de sus cortes, un mismo término cumpliría
$$D\le d(a,x_n)+d(x_n,b)<2D/3,$$
contradicción. Sólo se usaron separación, triangular y sincronización de cortes. Ninguna completitud interviene.

Una sucesión convergente es acotada: existe una bola de radio finito que contiene todos sus valores. La captura con tolerancia $1$ acota la cola respecto del destino; las distancias del prefijo finito tienen un máximo. Aumentar ese máximo y $1$ en una unidad proporciona una bola abierta que contiene todo. Si no hay prefijo, basta radio $2$. Cambiar el centro a $b\in X$ aumenta la cota a lo sumo en $d(a,b)$; la acotación no depende de una referencia privilegiada. La sucesión tiene valores, por lo que aquí $X$ es necesariamente no vacío.

**Transportar lo eventual.** Cambiar finitos términos no altera un destino. Si $n_k$ es estrictamente creciente en $\mathbb N_0$, la inducción da $n_k\ge k$; por ello la subsucesión conserva cualquier corte de convergencia. Si $x_n\to a$ y $d(x_n,y_n)\to0$, entonces $y_n\to a$ por
$$d(y_n,a)\le d(y_n,x_n)+d(x_n,a).$$
Cada error se hace menor que $\varepsilon/2$ y se toma el máximo de cortes. Aun sin operaciones en $X$, existe una regla de perturbación pequeña. La triangular inversa también da $d(x_n,b)\to d(a,b)$ para cada $b$ fijo. Más generalmente, si $y_n\to b$, dos aplicaciones de triangular prueban
$$|d(x_n,y_n)-d(a,b)|\le d(x_n,a)+d(y_n,b)\to0.$$
Los límites del último renglón son reales, ya acreditados por C6.

**Cierre y selección de testigos.** Si una sucesión con valores en $A$ converge a $a\in X$, cada bola de $a$ contiene términos tardíos, así que $a\in\operatorname{cl}_X A$. En particular un conjunto cerrado retiene todos esos destinos. La vuelta requiere reunir testigos: si $a\in\operatorname{cl}_X A$, los conjuntos $A\cap B(a,1/(n+1))$ son no vacíos. Si se dispone de una selección $a_n$ en cada uno, su distancia a $a$ es menor que $1/(n+1)$ y converge. La existencia general de esa selección se garantiza bajo **elección numerable para subconjuntos de $X$**, que denotaremos $\mathrm{CC}(X)$; también basta una selección explícitamente dada. No se esconde esta interfaz lógica en la frase «escojamos una sucesión».

Bajo esa misma condición, $A$ es cerrado si y sólo si contiene el límite de toda sucesión suya convergente en $X$: si no fuera cerrado, un punto de su clausura fuera de $A$ y la selección anterior refutarían la propiedad. La dirección desde cerrado no usa elección. Si los testigos son naturales dentro de un conjunto enumerado, se puede escoger el primer índice admisible y evitar una elección arbitraria.

En la métrica discreta, converger a $a$ equivale a ser eventualmente igual a $a$, porque la tolerancia $1/2$ excluye cualquier otro punto. En la usual sobre $\mathbb R$, $1/(n+1)\to0$ sin ser eventualmente cero. La misma sintaxis de captura adquiere contenido diferente al cambiar la métrica.

![Los recíprocos1/(n+1) convergen a0 en la métrica usual y tienen error1/(n+1), con corte estricto n4 para tolerancia1/4. Los mismos valores tienen distancia discreta1 a0 en todos los índices y no convergen a ningún destino discreto, pues sus términos son todos distintos. Los puntos representan índices enteros, sin interpolar una sucesión.](../../assets/books/anm/C30/C30-F04.svg){#fig-anm-c30-f04 fig-alt="Los recíprocos1/(n+1) convergen a0 en la métrica usual y tienen error1/(n+1), con corte estricto n4 para tolerancia1/4. Los mismos valores tienen distancia discreta1 a0 en todos los índices y no convergen a ningún destino discreto, pues sus términos son todos distintos. Los puntos representan índices enteros, sin interpolar una sucesión."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-030-025}

¿Dónde debe vivir el destino de una sucesión en $X$?

[]{#MA-MSOL-ANM-01-030-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

En $X$, no sólo en un espacio mayor que lo contenga.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-030-026}

¿Qué orden de cuantificadores expresa convergencia?

[]{#MA-MSOL-ANM-01-030-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

$\forall\varepsilon>0\exists N\forall n\ge N$ para la distancia al destino menor que $\varepsilon$.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-030-027}

¿Qué prueba unicidad sin completitud?

[]{#MA-MSOL-ANM-01-030-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

Dos ventanas de radios un tercio de la separación y un corte común contradicen triangular.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-030-028}

¿Cómo se acota el prefijo de una convergente?

[]{#MA-MSOL-ANM-01-030-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

Por el máximo de sus finitísimas distancias al destino; se reúne con la cota de cola.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-030-029}

¿Por qué una subsucesión conserva un corte?

[]{#MA-MSOL-ANM-01-030-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Sus índices estrictamente crecientes satisfacen $n_k\ge k$.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-030-030}

¿Qué hace una perturbación de distancia nula al destino?

[]{#MA-MSOL-ANM-01-030-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Lo conserva, sumando el error de perturbación y el de la sucesión por triangular.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-030-031}

¿Qué dirección entre clausura y sucesiones no requiere selección?

[]{#MA-MSOL-ANM-01-030-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

Una sucesión de $A$ convergente en $X$ tiene su destino en la clausura de $A$.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-030-032}

¿Qué interfaz se declara para construir testigos de clausura?

[]{#MA-MSOL-ANM-01-030-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

$\mathrm{CC}(X)$, elección numerable para los conjuntos no vacíos de testigos, o una selección explícitamente dada.

</details>

### Ejercicios de la sección 30.4

#### Ejercicio 16. Mismos términos, distinta captura

[]{#MA-EX-ANM-01-030-016}

Estudie $x_n=1/(n+1)$ en la recta con métrica usual y con métrica discreta. Considere cualquier posible destino discreto.

[]{#MA-SOL-ANM-01-030-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

En la usual, $|x_n|=1/(n+1)\to0$, luego converge a cero. En la discreta, converger a algún $a$ exigiría $x_n=a$ desde cierto índice por tolerancia $1/2$. Los recíprocos son todos distintos, de modo que ninguna cola es constante. No converge a ningún destino discreto, incluido cero. El conjunto de puntos es el mismo y la métrica cambia la condición efectiva.

**Retorno visual.** Véase [C30-F04](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 17. Un destino único

[]{#MA-EX-ANM-01-030-017}

Pruebe unicidad de límites métricos sin usar coordenadas, orden de puntos ni completitud.

[]{#MA-SOL-ANM-01-030-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Suponga dos límites distintos $a,b$ y escriba $D=d(a,b)>0$. Las dos convergencias con tolerancia $D/3$ dan cortes; su máximo garantiza que el mismo término de la sucesión está a distancia menor que $D/3$ de cada destino. Triangular da $D<2D/3$, contradicción. Separación transforma distancia cero en igualdad. El orden sólo se usa al comparar las distancias reales positivas, no los puntos del espacio.

</details>

#### Ejercicio 18. Dos referencias acotan el mismo conjunto

[]{#MA-EX-ANM-01-030-018}

Si $A\subset X$ cumple $d(x,a)\le R$ para todo $x\in A$, dé una cota respecto de otro centro $b$ y un radio abierto que contenga $A$.

[]{#MA-SOL-ANM-01-030-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Por triangular $d(x,b)\le d(x,a)+d(a,b)\le R+d(a,b)$. La distancia fija de centros es real finita. Así $A$ queda dentro de la bola abierta de centro $b$ y radio $R+d(a,b)+1$, que excede la cota débil. El conjunto vacío satisface la cota de modo vacuo; disponer de los centros declarados asegura aquí que $X$ no sea vacío.

</details>

#### Ejercicio 19. Un criterio secuencial con su interfaz

[]{#MA-EX-ANM-01-030-019}

Formule la relación entre clausura y límites de sucesiones de $A$. Separe la dirección incondicional de la que necesita testigos.

[]{#MA-SOL-ANM-01-030-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Si $a_n\in A$ y $a_n\to a\in X$, cada bola de $a$ contiene algún término tardío de $A$, por lo que $a\in\operatorname{cl}A$, sin elección. Para la vuelta, la adherencia asegura que cada $A\cap B(a,1/(n+1))$ sea no vacío. Una selección $a_n$ en esos conjuntos, dada o garantizada por $\mathrm{CC}(X)$, satisface $d(a_n,a)<1/(n+1)$ y converge. Sin esa interfaz no se declara la existencia simultánea de los testigos arbitrarios. La caracterización secuencial inversa de cerrado tiene el mismo alcance.

</details>

#### Ejercicio 20. Perturbación y dos distancias

[]{#MA-EX-ANM-01-030-020}

Si $x_n\to a$ y $y_n\to b$, pruebe $d(x_n,y_n)\to d(a,b)$ y deduzca la regla cuando $d(x_n,y_n)\to0$.

[]{#MA-SOL-ANM-01-030-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

La cota de dos centros de E005 da $|d(x_n,y_n)-d(a,b)|\le d(x_n,a)+d(y_n,b)$. Para tolerancia $\varepsilon$, pedir $\varepsilon/2$ a cada convergencia y sincronizar cortes hace menor que $\varepsilon$ el error real. Si además $d(x_n,y_n)\to0$, unicidad del límite real implica $d(a,b)=0$ y separación da $a=b$. Si no se sabe aún que $y_n$ converja pero se sabe $x_n\to a$ y $d(x_n,y_n)\to0$, triangular directamente acredita $y_n\to a$.

</details>
## 30.5. Cauchy compara toda la cola

[]{#MA-SEC-ANM-01-030-005}

La condición de **Cauchy** compara dos índices tardíos sin nombrar destino:
$$\forall\varepsilon>0\ \exists N\ \forall p,q\ge N:\quad d(x_p,x_q)<\varepsilon.$$
El corte precede a ambos índices. Conocer sólo $d(x_{n+1},x_n)\to0$ no basta. La negación fija una tolerancia $\varepsilon_0>0$ antes del corte adversario y exige, para todo $N$, algún par $p,q\ge N$ con $d(x_p,x_q)\ge\varepsilon_0$.

**Convergente implica Cauchy.** Si $x_n\to a$, usemos tolerancia $\varepsilon/2$ en la convergencia. Después de su corte, la triangular a través de $a$ da distancia entre cualesquiera dos términos menor que $\varepsilon$. Esta prueba no necesita construir un destino: lo recibe de la hipótesis.

**Cauchy implica acotada.** Con tolerancia $1$ fijamos una cola y su término $x_{N_0}$. Todo término posterior está a distancia menor que $1$ de esa referencia. Las distancias de los finitísimos términos anteriores tienen máximo; un radio que exceda ese máximo y $1$ contiene la sucesión. De nuevo la prueba no usa completitud. La recíproca falla: una alternancia entre dos puntos distintos es acotada y conserva separación positiva después de todo corte.

**Una subsucesión puede revelar el destino.** Si $x$ es de Cauchy y una subsucesión $x_{n_k}\to a\in X$, entonces toda $x$ converge a $a$. Recibido $\varepsilon$, tomamos el corte de Cauchy para $\varepsilon/2$. Elegimos un término de la subsucesión posterior a ese corte y a su propio corte de convergencia, lo que es posible porque $n_k\ge k$. Fijado ese término como referencia, para todo $n$ posterior al corte de Cauchy,
$$d(x_n,a)\le d(x_n,x_{n_k})+d(x_{n_k},a)<\varepsilon.$$
Se usa una elección finita de un índice natural, no se supone que exista siempre una subsucesión convergente.

**Cauchy no garantiza destino en un espacio arbitrario.** En $X=(0,1)$ con distancia usual, $x_n=1/(n+2)$ es de Cauchy: para $p,q\ge N$ sus valores están en $(0,1/(N+2)]$, y su separación es a lo sumo $1/(N+2)$. Vista en $\mathbb R$, converge a cero. Si convergiera a $a\in(0,1)$, las mismas distancias acreditarían esa convergencia en $\mathbb R$, y unicidad forzaría $a=0$, imposible. C10 construía destinos reales mediante completitud; aquí no hemos añadido esa propiedad a todo conjunto con distancia.

En la métrica discreta, Cauchy implica cola constante: con tolerancia $1/2$, todos los pares tardíos deben coincidir con $x_N$. Por eso esas sucesiones sí tienen destino. La existencia de destinos de Cauchy será una pregunta central de C31, junto con compacidad y conexidad; aquí sólo hemos distinguido las obligaciones.

**Un presupuesto de saltos que sí controla bloques.** Si $d(x_{n+1},x_n)\le C\rho^n$, con $C\ge0$ y $0<\rho<1$, la triangular iterada finitamente da, para $p>q$,
$$d(x_p,x_q)\le\sum_{j=q}^{p-1}C\rho^j\le\frac{C\rho^q}{1-\rho}.$$
La identidad geométrica finita y $\rho^q\to0$ hacen Cauchy a $x$. Sin una propiedad adicional del espacio no se declara un destino. Si ya existe $a$ con $x_p\to a$, pasar $p$ al límite en la distancia prueba el certificado $d(x_q,a)\le C\rho^q/(1-\rho)$. Estabilización, existencia y error quedan como pasos distintos.

![En(0,1), los términos1/(n+2) son Cauchy con cota de pares1/(N+2), pero el candidato externo0 queda fuera del espacio. En sumas armónicas finitas, los saltos vecinos desaparecen y los pares de bloques de longitud creciente siguen separados al menos por1/2. Las diferencias exactas acreditan la negación de Cauchy.](../../assets/books/anm/C30/C30-F05.svg){#fig-anm-c30-f05 fig-alt="En(0,1), los términos1/(n+2) son Cauchy con cota de pares1/(N+2), pero el candidato externo0 queda fuera del espacio. En sumas armónicas finitas, los saltos vecinos desaparecen y los pares de bloques de longitud creciente siguen separados al menos por1/2. Las diferencias exactas acreditan la negación de Cauchy."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-030-033}

¿Qué compara Cauchy?

[]{#MA-MSOL-ANM-01-030-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Todos los pares de términos posteriores a un corte común, sin nombrar destino.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-030-034}

¿Cuál es la negación correcta de Cauchy?

[]{#MA-MSOL-ANM-01-030-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Existe una tolerancia positiva fija tal que después de cualquier corte hay un par separado al menos por ella.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-030-035}

¿Qué tolerancia de convergencia demuestra Cauchy con $\varepsilon$?

[]{#MA-MSOL-ANM-01-030-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

$\varepsilon/2$, para sumar dos errores alrededor del destino.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-030-036}

¿Qué tolerancia de Cauchy basta para acotar?

[]{#MA-MSOL-ANM-01-030-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Una sola, por ejemplo uno, y un término de referencia más el prefijo finito.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-030-037}

¿Cauchy implica destino en cualquier métrica?

[]{#MA-MSOL-ANM-01-030-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

No. Los recíprocos en $(0,1)$ son Cauchy y su único posible destino real queda fuera.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-030-038}

¿Qué significa Cauchy en la discreta?

[]{#MA-MSOL-ANM-01-030-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Que la cola es constante, por usar tolerancia $1/2$.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-030-039}

¿Una subsucesión convergente basta sin Cauchy?

[]{#MA-MSOL-ANM-01-030-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

No. La hipótesis Cauchy es la que acerca toda la cola al término de referencia elegido.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-030-040}

¿Qué acredita una barrera geométrica de saltos?

[]{#MA-MSOL-ANM-01-030-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

Cauchy por bloques finitos; el destino requiere otra justificación y, si existe, se obtiene una cota de error.

</details>

### Ejercicios de la sección 30.5

#### Ejercicio 21. Cauchy sin cero admisible

[]{#MA-EX-ANM-01-030-021}

Pruebe que $x_n=1/(n+2)$ es de Cauchy en $(0,1)$ y no converge a ningún elemento de ese espacio.

[]{#MA-SOL-ANM-01-030-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Después de un corte $N$, todos los valores están en $(0,1/(N+2)]$ y cualquier separación es a lo sumo $1/(N+2)$. Arquimedianidad permite hacerlo menor que una tolerancia dada. En la recta, los mismos términos convergen a cero. Si hubiera un límite $a\in(0,1)$, la igualdad de distancias con la inclusión acreditaría también límite real $a$. Unicidad real lo igualaría a cero, contradiciendo la pertenencia al espacio. Cauchy sólo controla pares internos, sin imponer que el destino externo pertenezca al dominio.

**Retorno visual.** Véase [C30-F05](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 22. Cauchy y captura constante

[]{#MA-EX-ANM-01-030-022}

Caracterice todas las sucesiones de Cauchy de una métrica discreta y sus límites.

[]{#MA-SOL-ANM-01-030-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Con tolerancia $1/2$, cualquier par posterior al corte tiene distancia cero. Fijando uno de los índices en el corte, toda la cola es igual a $x_N$. Recíprocamente, una cola constante tiene todas sus distancias posteriores cero y cumple Cauchy para toda tolerancia. Esa misma cola converge a su valor constante, que pertenece al espacio. La unicidad ya probada excluye otros destinos.

</details>

#### Ejercicio 23. Vecinos pequeños no bastan

[]{#MA-EX-ANM-01-030-023}

Para $h_n=\sum_{j=1}^{n+1}1/j$ en $\mathbb R$, pruebe saltos vecinos nulos y refute Cauchy mediante pares dados después de cualquier corte.

[]{#MA-SOL-ANM-01-030-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

El salto es $h_{n+1}-h_n=1/(n+2)\to0$. Dado un corte $N$, tome $m=N+1$ y los índices $m-1=N$ y $2m-1\ge N$. La diferencia es $\sum_{j=m+1}^{2m}1/j$, con $m$ términos cada uno al menos $1/(2m)$, así que es al menos $1/2$. La tolerancia fija $1/2$ y estos pares niegan Cauchy. Los bloques crecen con el corte; controlar sólo vecinos omite precisamente esa obligación.

</details>

#### Ejercicio 24. Subsucesión y cola completa

[]{#MA-EX-ANM-01-030-024}

Pruebe que una sucesión de Cauchy con una subsucesión convergente en $X$ converge al mismo destino. Identifique el índice fijado como referencia.

[]{#MA-SOL-ANM-01-030-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Para $\varepsilon>0$, tome el corte $N$ de Cauchy con tolerancia $\varepsilon/2$, y el corte $K$ de la subsucesión convergente a $a$ con la misma tolerancia. Elija $k\ge\max\{N,K\}$; entonces $n_k\ge k\ge N$. Ese término fijo satisface $d(x_{n_k},a)<\varepsilon/2$. Para todo $n\ge N$, triangular da $d(x_n,a)\le d(x_n,x_{n_k})+d(x_{n_k},a)<\varepsilon$. No se asume existencia de una subsucesión convergente para una Cauchy arbitraria; es la hipótesis del ejercicio.

</details>

#### Ejercicio 25. Saltos geométricos y tres obligaciones

[]{#MA-EX-ANM-01-030-025}

Si $d(x_{n+1},x_n)\le3\,2^{-n}$, acredite Cauchy y una cota de error si el destino ya existe. Indique qué corte certifica error estrictamente menor que $3/8$.

[]{#MA-SOL-ANM-01-030-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Para $p>q$, triangular iterada y suma geométrica finita dan $d(x_p,x_q)\le6\,2^{-q}$. Como el presupuesto tiende a cero, hay un corte común para todos los pares y la sucesión es de Cauchy. No se afirma existencia de destino en un espacio arbitrario. Si $x_p\to a\in X$, continuidad real de la distancia al punto fijo $x_q$ permite pasar $p$ al límite y da $d(x_q,a)\le6\,2^{-q}$. Para error estrictamente menor que $3/8$, basta $6\,2^{-q}<3/8$, es decir $q>4$, por lo que el primer índice certificado es $5$.

</details>
## 30.6. Continuidad entre espacios métricos

[]{#MA-SEC-ANM-01-030-006}

Sean espacios métricos $(X,d_X)$ y $(Y,d_Y)$ y una función $f:X\to Y$. Es continua en $a\in X$ si
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x\in X:\quad d_X(x,a)<\delta\ \Longrightarrow\ d_Y(f(x),f(a))<\varepsilon.$$
Se incluye el centro. El radio de entrada puede depender de $a$ y de la tolerancia. En un punto aislado la continuidad de cualquier función es automática: una bola que sólo contiene el centro cumple todas las exigencias.

**Continuidad transporta sucesiones dadas.** Si $x_n\to a$, primero pedimos a $f$ un radio $\delta$ para la tolerancia de salida, y luego a la sucesión un corte que la sitúe dentro de esa bola. Entonces $f(x_n)\to f(a)$. No se elige una sucesión para probar esta dirección: ya es parte de la hipótesis.

Para la vuelta, la falla de continuidad en $a$ fija $\varepsilon_0>0$ y, para cada $\delta>0$, una entrada con $d_X(x,a)<\delta$ y $d_Y(f(x),f(a))\ge\varepsilon_0$. Los conjuntos de infractores con $\delta=1/(n+1)$ son no vacíos. Bajo $\mathrm{CC}(X)$, o si esos testigos se suministran, forman una sucesión que converge a $a$ y cuyas imágenes no convergen a $f(a)$. Así el criterio secuencial es una equivalencia con esa interfaz explícita; la implicación directa es incondicional.

**La caracterización por abiertos no necesita esa selección.** $f$ es continua en todos sus puntos si y sólo si $f^{-1}[V]$ es abierto en $X$ para todo abierto $V\subset Y$. Si $f$ es continua y $a$ está en la preimagen, una bola de salida alrededor de $f(a)$ cabe en $V$; su radio entra como tolerancia y produce una bola de entrada contenida en la preimagen. Ésta es abierta por definición. Recíprocamente, para $a,\varepsilon$, la bola abierta $B_Y(f(a),\varepsilon)$ tiene preimagen abierta que contiene $a$. Alguna bola alrededor de $a$ cabe en ella y da exactamente el radio requerido. Complementar y usar $f^{-1}[Y\setminus F]=X\setminus f^{-1}[F]$ acredita el criterio equivalente por cerrados.

**Componer y restringir.** Para $f:X\to Y$ continua en $a$ y $g:Y\to Z$ continua en $f(a)$, una tolerancia de $Z$ da primero un radio $\eta$ en $Y$; usar $\eta$ como tolerancia de $f$ da el radio de $X$. La cadena de implicaciones prueba continuidad de $g\circ f$. Restringir el dominio conserva la prueba porque sus bolas son intersecciones. Un cambio a un subespacio de salida que contiene el recorrido tampoco cambia las distancias de salida; debe declararse el codominio correcto.

**Funciones que siempre tenemos.** Para $b\in X$, $x\mapsto d_X(x,b)$ es continua hacia $\mathbb R$: la triangular inversa da error a lo sumo $d_X(x,a)$, así que sirve $\delta=\varepsilon$. Los singletons son cerrados: alrededor de $x\ne b$ la bola de radio $d_X(x,b)/2$ evita a $b$. Los conjuntos de nivel de una función continua real son cerrados por preimagen de singletons, y las regiones definidas por desigualdades estrictas son abiertas por preimagen de intervalos abiertos.

La continuidad asegura preimágenes abiertas, no imágenes abiertas. Una función constante $\mathbb R\to\mathbb R$ envía el abierto completo a un singleton no abierto. Tampoco una biyección continua garantiza inversa continua: la identidad del conjunto $\mathbb R$, desde su métrica discreta hacia la usual, es continua en cada punto aislado; su inversa no es continua, pues ninguna ventana usual en cero contiene sólo ese punto. Son funciones tipadas entre métricas distintas, aunque la regla de valores sea la misma.

![La función valor absoluto lleva hacia atrás la banda abierta de salida(1,2) a las dos ventanas(−2,−1) y(1,2). Para la identidad de la usual hacia la discreta, cualquier radioδ falla con una entradaδ/2 distinta de0: la distancia discreta de salida sigue siendo1. Las tres radios ilustrados no sustituyen la regla válida para todoδ>0.](../../assets/books/anm/C30/C30-F06.svg){#fig-anm-c30-f06 fig-alt="La función valor absoluto lleva hacia atrás la banda abierta de salida(1,2) a las dos ventanas(−2,−1) y(1,2). Para la identidad de la usual hacia la discreta, cualquier radioδ falla con una entradaδ/2 distinta de0: la distancia discreta de salida sigue siendo1. Las tres radios ilustrados no sustituyen la regla válida para todoδ&gt;0."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-030-041}

¿Cuál es el centro de salida en continuidad en $a$?

[]{#MA-MSOL-ANM-01-030-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

El valor efectivo $f(a)$, perteneciente al codominio declarado.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-030-042}

¿Qué sucede en un punto aislado?

[]{#MA-MSOL-ANM-01-030-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Toda función es continua allí, porque una bola puede contener sólo el centro.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-030-043}

¿Continuidad transporta una sucesión dada sin elección?

[]{#MA-MSOL-ANM-01-030-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Sí. Primero obtiene un radio y luego un corte de esa sucesión.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-030-044}

¿Qué necesita la recíproca secuencial general?

[]{#MA-MSOL-ANM-01-030-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

Reunir infractores en una sucesión, mediante $\mathrm{CC}(X)$ o testigos suministrados.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-030-045}

¿En qué dirección viajan los abiertos bajo continuidad?

[]{#MA-MSOL-ANM-01-030-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

Hacia atrás por preimágenes, que son abiertas en el dominio.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-030-046}

¿El criterio por preimágenes necesita construir sucesiones?

[]{#MA-MSOL-ANM-01-030-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

No. Se prueba directamente con radios en cada punto y bolas del codominio.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-030-047}

¿Por qué la distancia a un punto es continua?

[]{#MA-MSOL-ANM-01-030-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

La triangular inversa acota su error de salida por la distancia de entrada.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-030-048}

¿Una biyección continua siempre tiene inversa continua?

[]{#MA-MSOL-ANM-01-030-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

No. La identidad de la recta discreta hacia la usual tiene inversa discontinua.

</details>

### Ejercicios de la sección 30.6

#### Ejercicio 26. Preimagen de una banda

[]{#MA-EX-ANM-01-030-026}

Para $f(x)=|x|$ en la recta usual, calcule $f^{-1}[(1,2)]$ y pruebe continuidad usando una desigualdad métrica.

[]{#MA-SOL-ANM-01-030-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La preimagen es $(-2,-1)\cup(1,2)$, abierta. Para todo par, $||x|-|y||\le|x-y|$ por triangular inversa real, así que en cualquier centro sirve $\delta=\varepsilon$. La desigualdad acredita continuidad de la función en todos los puntos, y el criterio de preimágenes explica la apertura de la región calculada. El mapa no necesita ser inyectivo.

**Retorno visual.** Véase [C30-F06](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 27. La equivalencia por abiertos

[]{#MA-EX-ANM-01-030-027}

Pruebe continuidad global equivalente a preimágenes abiertas, con espacios métricos distintos y sin construir sucesiones.

[]{#MA-SOL-ANM-01-030-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Para continuidad→preimagen, dado abierto $V$ y $a$ con $f(a)\in V$, obtenga una bola de salida contenida en $V$ y use su radio como tolerancia de continuidad. La bola de entrada obtenida queda en la preimagen, que es abierta punto por punto. Para la vuelta, la preimagen de $B_Y(f(a),\varepsilon)$ es abierta y contiene a $a$; una bola de entrada dentro de ella entrega el radio $\delta$ de la definición. Las dos métricas intervienen en sus respectivas bolas; no se seleccionan testigos para una sucesión ni se necesita elección numerable.

</details>

#### Ejercicio 28. Identidad con inversa fallida

[]{#MA-EX-ANM-01-030-028}

Pruebe que la identidad de $\mathbb R$ discreto hacia $\mathbb R$ usual es una biyección continua y que su inversa falla en cero.

[]{#MA-SOL-ANM-01-030-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

La regla es biyectiva. Para cualquier tolerancia de salida usual, tome radio discreto $1/2$: la única entrada admisible es el centro y el error de salida es cero. Para la inversa, la tolerancia discreta $1/2$ exigiría que todas las entradas de alguna ventana usual de cero fueran cero. Dado cualquier radio $\delta>0$, la entrada $\delta/2$ está en esa ventana y es distinta de cero, por lo que su distancia discreta al centro es uno. Ningún radio funciona.

</details>

#### Ejercicio 29. Un fracaso secuencial condicionado

[]{#MA-EX-ANM-01-030-029}

Si $f$ no es continua en $a$, construya una sucesión infractora bajo $\mathrm{CC}(X)$ y explique el papel de ese supuesto.

[]{#MA-SOL-ANM-01-030-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Negar continuidad fija $\varepsilon_0>0$ tal que para cada radio hay una entrada cercana cuya distancia de salida a $f(a)$ es al menos $\varepsilon_0$. Para el radio $1/(n+1)$, forme su conjunto no vacío de infractores. $\mathrm{CC}(X)$ permite escoger una entrada $x_n$ de cada conjunto. Entonces $d_X(x_n,a)<1/(n+1)$ acredita convergencia, pero todas las distancias de salida son al menos $\varepsilon_0$, negando convergencia de imágenes al valor central. La selección explícita de esos testigos también basta; su existencia simultánea es el único paso que usa el supuesto.

</details>

#### Ejercicio 30. Transportar el dominio de un nivel

[]{#MA-EX-ANM-01-030-030}

Para $b\in X$ pruebe continuidad de $F(x)=d(x,b)$ y determine si $\{x:d(x,b)=r\}$ es cerrado y $\{x:d(x,b)<r\}$ es abierto.

[]{#MA-SOL-ANM-01-030-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

La triangular inversa da $|F(x)-F(a)|\le d(x,a)$, así que $\delta=\varepsilon$ sirve en todo centro. El conjunto de igualdad es la preimagen del singleton real cerrado $\{r\}$ y por ello es cerrado. La región estricta es la preimagen del abierto real $(-\infty,r)$ y es abierta, incluso cuando resulte vacía. Estas pruebas no necesitan que los valores de distancia recorran un intervalo continuo ni que exista algún punto a distancia $r$.

</details>
## 30.7. Una escala común y espacios de funciones

[]{#MA-SEC-ANM-01-030-007}

La continuidad uniforme exige un radio común para todos los pares de entradas:
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in X:\quad d_X(x,y)<\delta\ \Longrightarrow\ d_Y(f(x),f(y))<\varepsilon.$$
No se fija un centro antes de pedir el radio. Una función es $L$-Lipschitz, con $L\ge0$, si $d_Y(f(x),f(y))\le Ld_X(x,y)$ para todo par. Si $L>0$, $\delta=\varepsilon/L$ acredita continuidad uniforme; si $L=0$, todas las imágenes coinciden y sirve cualquier radio positivo. Para dominio vacío, las condiciones son vacuas y no hace falta nombrar una imagen común.

**Cauchy se transporta bajo una escala común.** Recibida una tolerancia de salida, continuidad uniforme entrega $\delta$ para todos los pares. Cauchy en $X$ sitúa después de un corte todas las parejas a distancia menor que $\delta$. Sus imágenes quedan a distancia menor que la tolerancia, por lo que forman una sucesión de Cauchy en $Y$. No se necesita que la sucesión original ni su imagen tengan destino.

La continuidad punto a punto no basta para ese transporte. En $(0,1)$, $f(x)=1/x$ es continua: en un centro $a>0$, si $|x-a|<a/2$, entonces $x>a/2$ y $|1/x-1/a|\le2|x-a|/a^2$, lo que permite un radio dependiente de $a$. Pero para $x_n=1/(n+2)$ e $y_n=1/(n+3)$, la distancia de entrada es $1/((n+2)(n+3))\to0$ y la de salida es exactamente $1$. Estos pares niegan uniformidad, con tolerancia fija $1/2$. Además la sucesión Cauchy $x_n$ tiene imágenes $n+2$, que no son de Cauchy. La falla ocurre hacia un punto que no pertenece al dominio, de modo que no contradice continuidad en ningún centro suyo.

**Distancia a un conjunto.** Si $A\subset X$ es no vacío, definimos $\operatorname{dist}(x,A)=\inf\{d(x,a):a\in A\}$. El conjunto de distancias es no vacío y acotado inferiormente por cero, por lo que el ínfimo real de C3 existe y es finito. Para $\eta>0$ hay $a\in A$ con $d(y,a)<\operatorname{dist}(y,A)+\eta$. La triangular da
$$\operatorname{dist}(x,A)\le d(x,y)+\operatorname{dist}(y,A)+\eta.$$
Si la desigualdad sin $\eta$ fallara, elegir $\eta$ menor que su diferencia positiva daría contradicción. Intercambiar $x,y$ demuestra
$$|\operatorname{dist}(x,A)-\operatorname{dist}(y,A)|\le d(x,y).$$
Es una función $1$-Lipschitz. Además $\operatorname{dist}(x,A)=0$ si y sólo si $x\in\operatorname{cl}_X A$: cada bola encuentra una distancia menor que su radio, y recíprocamente un ínfimo cero permite obtener esa distancia. No es necesario que el ínfimo se alcance; distancia cero a un conjunto no significa pertenencia si el conjunto no es cerrado. Para $A=\varnothing$ no se define aquí una distancia real finita mediante ese ínfimo.

**Los puntos también pueden ser funciones.** Para un conjunto no vacío $T$, sea $\mathcal B(T)$ el conjunto de funciones reales acotadas sobre $T$. Definimos
$$D_\infty(f,g)=\sup_{t\in T}|f(t)-g(t)|.$$
Las cotas de $f,g$ aseguran finitud; el conjunto de magnitudes no vacío tiene supremo por C3. Si el supremo es cero, todas las magnitudes son cero y $f=g$. Simetría es directa. La triangular puntual queda dominada por $D_\infty(f,h)+D_\infty(h,g)$; tomar supremo prueba la triangular métrica. C27 ya había desarrollado esta distancia, y ahora reconocemos su lugar entre las métricas generales.

Convergencia en esta métrica equivale a convergencia uniforme hacia una función acotada: una distancia de supremo menor que $\varepsilon$ controla todas las entradas; en sentido inverso, control puntual estricto con tolerancia $\varepsilon/2$ deja supremo a lo sumo $\varepsilon/2<\varepsilon$. Se conserva el margen entre desigualdad estricta y supremo. Por ejemplo en $T=[0,1]$, $f_n(t)=t/(n+1)$ tiene distancia exacta $1/(n+1)$ a cero. La convergencia puntual sola de $t^{n+1}$ al destino discontinuo que vale uno en $1$ y cero antes tiene distancia de supremo $1$ en cada índice. No hay convergencia métrica aunque cada evaluación converja.

![Los errores de t^(n+1) frente al destino puntual valen t^(n+1) para t<1 y0 en1; su supremo es1 sin alcanzarse. Las curvas no contienen una falsa unión entre el límite izquierdo y el valor extremo. La distancia real aA=(0,1) vale0 en\[0,1\], aunque el ínfimo no se alcance en los extremos; fuera es la separación al extremo más cercano.](../../assets/books/anm/C30/C30-F07.svg){#fig-anm-c30-f07 fig-alt="Los errores de t^(n+1) frente al destino puntual valen t^(n+1) para t&lt;1 y0 en1; su supremo es1 sin alcanzarse. Las curvas no contienen una falsa unión entre el límite izquierdo y el valor extremo. La distancia real aA=(0,1) vale0 en\[0,1\], aunque el ínfimo no se alcance en los extremos; fuera es la separación al extremo más cercano."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-030-049}

¿Qué cambia en los cuantificadores de continuidad uniforme?

[]{#MA-MSOL-ANM-01-030-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

El radio se elige antes de cualquier par de entradas y debe servir para todos.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-030-050}

¿Qué radio da una cota Lipschitz con $L>0$?

[]{#MA-MSOL-ANM-01-030-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

$\delta=\varepsilon/L$.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-030-051}

¿Por qué la uniforme transporta Cauchy?

[]{#MA-MSOL-ANM-01-030-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Un radio común de entrada se aplica a todos los pares de una cola de Cauchy.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-030-052}

¿Qué pares refutan uniformidad de $1/x$ en $(0,1)$?

[]{#MA-MSOL-ANM-01-030-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

$1/(n+2)$ y $1/(n+3)$: su distancia desaparece y la de imágenes vale uno.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-030-053}

¿Qué condición necesita la distancia real a un conjunto?

[]{#MA-MSOL-ANM-01-030-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Que el conjunto sea no vacío, para tener un ínfimo real finito de distancias.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-030-054}

¿Distancia cero a $A$ implica pertenencia a $A$?

[]{#MA-MSOL-ANM-01-030-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Implica pertenencia a su clausura; pertenece a $A$ si éste es cerrado.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-030-055}

¿Qué asegura finitud de $D_\infty(f,g)$?

[]{#MA-MSOL-ANM-01-030-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Que ambas funciones sean acotadas y el dominio de evaluación no vacío.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-030-056}

¿Cómo se pasa de error uniforme estricto a supremo estricto?

[]{#MA-MSOL-ANM-01-030-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

Se usa tolerancia $\varepsilon/2$, que deja supremo a lo sumo $\varepsilon/2<\varepsilon$.

</details>

### Ejercicios de la sección 30.7

#### Ejercicio 31. Un radio Lipschitz

[]{#MA-EX-ANM-01-030-031}

Para una función $L$-Lipschitz entre métricas, dé radios de continuidad uniforme y pruebe que transporta sucesiones de Cauchy. Separe $L=0$.

[]{#MA-SOL-ANM-01-030-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Si $L>0$, use $\delta=\varepsilon/L$; la desigualdad estricta de entrada da error de salida menor que $\varepsilon$. Cauchy proporciona un corte para esta tolerancia de entrada y controla todos los pares de imágenes. Si $L=0$, cualquier par tiene distancia de salida cero, así que sirve cualquier radio y cualquier sucesión de imágenes existente es constante y Cauchy. Un dominio vacío no tiene sucesiones y el transporte es vacuo.

</details>

#### Ejercicio 32. Distancia cero sin pertenencia

[]{#MA-EX-ANM-01-030-032}

Para $A=(0,1)$ dentro de $\mathbb R$, calcule $\operatorname{dist}(x,A)$ en toda la recta y decida dónde vale cero y dónde se alcanza el ínfimo.

[]{#MA-SOL-ANM-01-030-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Para $x<0$, el ínfimo es $-x$ al acercar entradas a cero; para $0\le x\le1$ es cero; para $x>1$ es $x-1$ al acercar entradas a uno. El cero ocurre en $[0,1]=\operatorname{cl}A$, no sólo en $A$. El ínfimo se alcanza únicamente si $0<x<1$, tomando la propia entrada como punto de $A$. En cero y uno no se alcanza, y fuera del cerrado tampoco, pues sus extremos no están en $A$. La función es $1$-Lipschitz por el teorema general.

</details>

#### Ejercicio 33. Continuidad que destruye Cauchy

[]{#MA-EX-ANM-01-030-033}

Pruebe continuidad de $1/x$ en $(0,1)$, niegue su uniformidad con pares explícitos y muestre una Cauchy cuya imagen no lo es.

[]{#MA-SOL-ANM-01-030-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

En un centro $a>0$, si $|x-a|<a/2$ entonces $|1/x-1/a|\le2|x-a|/a^2$. El radio $\min\{a/2,\varepsilon a^2/2\}$ sirve. Para $x_n=1/(n+2)$, $y_n=1/(n+3)$, las separaciones de entrada $1/((n+2)(n+3))$ tienden a cero y las de salida valen uno. Con tolerancia fija $1/2$ no hay radio uniforme. La primera sucesión es Cauchy por su cola recíproca, mientras las imágenes $n+2$ tienen vecinos a distancia uno y niegan Cauchy.

</details>

#### Ejercicio 34. Un supremo que no se alcanza

[]{#MA-EX-ANM-01-030-034}

En $T=[0,1]$ tome $f_n(t)=t^{n+1}$ y su destino puntual $f(t)=0$ para $t<1$, $f(1)=1$. Calcule $D_\infty(f_n,f)$ y compare con $g_n(t)=t/(n+1)$.

[]{#MA-SOL-ANM-01-030-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

El error de $f_n$ es $t^{n+1}$ antes del extremo y cero en él. Siempre es menor que uno, pero se aproxima arbitrariamente a uno cuando $t$ se acerca a $1$ desde la izquierda, luego el supremo es exactamente uno y no se alcanza. Por ello no hay convergencia métrica, aunque cada entrada converja. Para $g_n$, el destino es cero y el máximo de error es $1/(n+1)$, alcanzado en $t=1$, de modo que sí hay convergencia en el supremo. El criterio se refiere al supremo, no sólo a errores estrictos en entradas individuales.

**Retorno visual.** Véase [C30-F07](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 35. Una distancia de funciones bien definida

[]{#MA-EX-ANM-01-030-035}

Pruebe los axiomas de $D_\infty$ en $\mathcal B(T)$ con $T$ no vacío y la equivalencia con convergencia uniforme. Indique dónde se usa completitud real.

[]{#MA-SOL-ANM-01-030-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Las cotas de cada función hacen finitas y acotadas las magnitudes $|f(t)-g(t)|$; al ser $T$ no vacío, completitud por supremo de C3 construye un número real $D_\infty$. Si es cero, todas las magnitudes son cero y las funciones coinciden. Simetría es puntual. La triangular puntual queda bajo la suma de los dos supremos, y tomar el tercero prueba triangular. Si las distancias tienden a cero, controlan todas las entradas. A la inversa, uniformidad con tolerancia $\varepsilon/2$ da supremo a lo sumo $\varepsilon/2<\varepsilon$. Se usa completitud de los valores reales para definir supremos; no se ha demostrado aquí completitud del espacio de funciones.

</details>
## 30.8. Cambiar la métrica y auditar lo que permanece

[]{#MA-SEC-ANM-01-030-008}

Un conjunto puede llevar varias métricas. Antes de decir que son «equivalentes», precisemos qué propiedad se quiere conservar.

**Comparación cuantitativa.** Si $c,C>0$ y $c\,d(x,y)\le e(x,y)\le C\,d(x,y)$ para todos los pares, las identidades en ambos sentidos son Lipschitz. Las inclusiones de bolas
$$B_d(a,r/C)\subset B_e(a,r),\qquad B_e(a,cr)\subset B_d(a,r)$$
prueban que ambas métricas definen los mismos abiertos. Las mismas desigualdades convierten tolerancias y demuestran que tienen las mismas convergencias, los mismos destinos y las mismas sucesiones de Cauchy. También convierten cotas de conjuntos. Para $d_1,d_\infty$ en $\mathbb R^2$,
$$d_\infty\le d_1\le2d_\infty.$$
Las bolas son diferentes, pero las capturas eventuales y los conjuntos abiertos coinciden. Una sucesión converge para ellas si y sólo si sus dos coordenadas convergen en $\mathbb R$, pues cada error de coordenada está bajo el máximo, y el máximo de dos cortes controla ambas. El mismo razonamiento con pares prueba la equivalencia coordenada a coordenada de Cauchy.

**Una métrica acotada que conserva controles pequeños.** Para cualquier métrica $d$, sea $e(x,y)=\min\{1,d(x,y)\}$. Separación y simetría se conservan. Para números no negativos $u,v$,
$$\min\{1,u+v\}\le\min\{1,u\}+\min\{1,v\};$$
si alguno es al menos uno, el lado derecho es al menos uno; si ambos son menores, el lado derecho es $u+v$. Combinarlo con la triangular prueba que $e$ es métrica. Para $0<r\le1$, sus bolas abiertas coinciden con las de $d$. Por tanto definen los mismos abiertos. Para controlar convergencia o Cauchy en $d$, pedir en $e$ tolerancia $\min\{\varepsilon/2,1/2\}$ fuerza una distancia menor que uno, donde $e=d$, y menor que $\varepsilon$. La dirección inversa usa $e\le d$. Sin embargo todo el espacio es acotado en $e$, mientras puede no serlo en $d$. La comparación local no impone una cota global por un múltiplo fijo de $e$.

**Los mismos abiertos no bastan para Cauchy.** Definamos
$$\phi(x)=\frac{x}{1+|x|},\qquad e_\phi(x,y)=|\phi(x)-\phi(y)|\quad(x,y\in\mathbb R).$$
La función $\phi$ es una biyección de $\mathbb R$ a $(-1,1)$, con inversa $\psi(t)=t/(1-|t|)$. En cada semirrecta la regla es estrictamente creciente; las imágenes negativa y positiva están separadas por cero. Como $|\phi(x)|=|x|/(1+|x|)$, tenemos $1-|\phi(x)|=1/(1+|x|)$ y $\psi(\phi(x))=x$. Para $|t|<1$, $|\psi(t)|=|t|/(1-|t|)$ y $1+|\psi(t)|=1/(1-|t|)$, luego $\phi(\psi(t))=t$. Estas identidades prueban inyectividad y sobreyectividad sin una elección de preimágenes. Ambas funciones son continuas por las reglas de valor absoluto, suma y cociente de C14; los denominadores son positivos en sus respectivos dominios. La separación de $e_\phi$ procede de inyectividad, y simetría/triangular de la métrica usual en las imágenes.

Las mismas funciones continuas e inversas prueban que $e_\phi$ y la distancia usual tienen los mismos abiertos: una bola $e_\phi$ es la preimagen por $\phi$ de una ventana relativa de $(-1,1)$, abierta en la distancia usual; a la inversa, la imagen por $\phi$ de un abierto usual es la preimagen por $\psi$ de ese abierto y es abierta relativa, de donde cada punto recibe una bola $e_\phi$ interior. Con esas bolas se convierten capturas y radios locales. Las convergencias a destinos reales y las funciones continuas son las mismas.

Pero $x_n=n$ es de Cauchy en $e_\phi$: sus imágenes $n/(n+1)$ tienen toda la cola entre $N/(N+1)$ y $1$, así que las distancias son a lo sumo $1/(N+1)$. No es de Cauchy usual, porque los vecinos distan uno. No converge a ningún real en $e_\phi$, pues las imágenes convergen a $1$, que queda fuera de $(-1,1)$. Una coincidencia de ventanas locales no garantiza un radio uniforme global para la identidad inversa. La sucesión también demuestra que misma topología no significa mismos conjuntos acotados.

**Balance de herramientas.** Sobreviven las pruebas de ventanas, unicidad, perturbación, convergente implica Cauchy, acotación y continuidad por preimágenes. El orden y las operaciones sólo se usan en los valores reales de las distancias o en ejemplos que poseen esas estructuras. La equivalencia secuencial inversa conserva su interfaz $\mathrm{CC}(X)$ o testigos dados. El paso Cauchy→destino, las equivalencias de compacidad y la estructura de conjuntos conexos requieren un nuevo examen. La única puerta siguiente es C31, *Completitud, compacidad y conexidad en espacios métricos*.

![La transformaciónφ(x)=x/(1+|x|) envíaR biyectivamente a(−1,1), con inversa continua. Por ella la métricaeφ tiene los mismos abiertos que la usual. La sucesiónn tiene cota de cola1/(N+1) en eφ y separación de vecinos1 en la usual. Sus imágenes tienden al punto externo1, por lo que no tiene destino real en eφ. La ventana gráfica\[−6,6\] no representa todo el recorrido deφ.](../../assets/books/anm/C30/C30-F08.svg){#fig-anm-c30-f08 fig-alt="La transformaciónφ(x)=x/(1+|x|) envíaR biyectivamente a(−1,1), con inversa continua. Por ella la métricaeφ tiene los mismos abiertos que la usual. La sucesiónn tiene cota de cola1/(N+1) en eφ y separación de vecinos1 en la usual. Sus imágenes tienden al punto externo1, por lo que no tiene destino real en eφ. La ventana gráfica\[−6,6\] no representa todo el recorrido deφ."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-030-057}

¿Qué compara $d_1$ y $d_\infty$ en el plano?

[]{#MA-MSOL-ANM-01-030-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

$d_\infty\le d_1\le2d_\infty$ para todos los pares.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-030-058}

¿Qué preserva una comparación global por constantes positivas?

[]{#MA-MSOL-ANM-01-030-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

Abiertos, destinos de convergencia, sucesiones de Cauchy y acotación.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-030-059}

¿Qué radios conservan bolas al usar $\min\{1,d\}$?

[]{#MA-MSOL-ANM-01-030-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Todos los radios abiertos $0<r\le1$.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-030-060}

¿La métrica recortada conserva acotación global?

[]{#MA-MSOL-ANM-01-030-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

Puede cambiarla: hace acotado todo espacio no vacío aunque la métrica original no lo hiciera.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-030-061}

¿Cuál es la inversa de $\phi(x)=x/(1+|x|)$?

[]{#MA-MSOL-ANM-01-030-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

$\psi(t)=t/(1-|t|)$ en $(-1,1)$.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-030-062}

¿Por qué $n$ es Cauchy en $e_\phi$?

[]{#MA-MSOL-ANM-01-030-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

Sus imágenes $n/(n+1)$ tienen todas las distancias de cola a lo sumo $1/(N+1)$.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-030-063}

¿Mismos abiertos garantizan mismas Cauchy?

[]{#MA-MSOL-ANM-01-030-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

No. La usual y $e_\phi$ tienen los mismos abiertos y difieren para la sucesión $n$.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-030-064}

¿Qué queda para C31?

[]{#MA-MSOL-ANM-01-030-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Examinar existencia de destinos de Cauchy y las nociones de compacidad y conexidad, con sus hipótesis métricas.

</details>

### Ejercicios de la sección 30.8

#### Ejercicio 36. Un par y dos métricas

[]{#MA-EX-ANM-01-030-036}

Para $x=(1,2)$ e $y=(4,-2)$, calcule $d_1,d_\infty$ y pruebe las desigualdades generales entre ambas métricas.

[]{#MA-SOL-ANM-01-030-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Las magnitudes de coordenadas son $3$ y $4$, por lo que $d_1=7$ y $d_\infty=4$, con $4\le7\le8$. En general, para magnitudes $u,v\ge0$, $\max\{u,v\}\le u+v\le2\max\{u,v\}$. Aplicarlo al par de coordenadas prueba $d_\infty\le d_1\le2d_\infty$ para todos los puntos. Las constantes positivas convierten bolas, cortes de convergencia y pares de Cauchy.

</details>

#### Ejercicio 37. Recortar una métrica

[]{#MA-EX-ANM-01-030-037}

Pruebe que $e=\min\{1,d\}$ es métrica y que conserva convergencia y Cauchy, aunque puede cambiar acotación.

[]{#MA-SOL-ANM-01-030-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

La positividad separadora y simetría son directas. La triangular se obtiene de monotonía del mínimo y $\min\{1,u+v\}\le\min\{1,u\}+\min\{1,v\}$: si algún sumando es al menos uno, la derecha domina uno; si no, es $u+v$. Para convertir un control en $e$ a $d$, use tolerancia $\eta=\min\{\varepsilon/2,1/2\}$. La distancia menor que $\eta$ es menor que uno, donde $e=d$, y menor que $\varepsilon$. La vuelta usa $e\le d$. Todo $X$ está en una bola de radio dos para $e$ si hay un centro, mientras $\mathbb R$ no es acotada en la usual.

</details>

#### Ejercicio 38. Una métrica con los mismos abiertos

[]{#MA-EX-ANM-01-030-038}

Pruebe que $e_\phi(x,y)=|\phi(x)-\phi(y)|$, $\phi(x)=x/(1+|x|)$, es métrica y tiene los mismos abiertos que la usual.

[]{#MA-SOL-ANM-01-030-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

$\phi$ es biyectiva hacia $(-1,1)$ con inversa $\psi(t)=t/(1-|t|)$, pues $1-|\phi(x)|=1/(1+|x|)$ da $\psi(\phi(x))=x$, y $1+|\psi(t)|=1/(1-|t|)$ da $\phi(\psi(t))=t$ para $|t|<1$. La separación de $e_\phi$ usa inyectividad, y simetría/triangular usan la distancia usual de las imágenes. Ambas funciones son continuas por las reglas reales y denominadores positivos. Las bolas $e_\phi$ son preimágenes de bolas relativas por $\phi$, abiertas usuales. Para un abierto usual $U$, $\phi[U]=\psi^{-1}[U]$ es abierto relativo; una bola de salida dentro de él vuelve a una bola $e_\phi$ dentro de $U$. Así cada tipo de abierto es del otro tipo, sin una cota uniforme global presupuesta.

</details>

#### Ejercicio 39. Misma topología, otra Cauchy

[]{#MA-EX-ANM-01-030-039}

Para $x_n=n$ compare Cauchy, convergencia y acotación en la usual y en $e_\phi$.

[]{#MA-SOL-ANM-01-030-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

En la usual, los vecinos distan uno, luego no es Cauchy y por tanto no converge; sus valores son no acotados. En $e_\phi$, las imágenes son $n/(n+1)$ y toda cola tiene separaciones a lo sumo $1/(N+1)$, así que es Cauchy. El espacio completo queda a distancia menor que dos de cualquier centro, por lo que la sucesión es acotada. Si convergiera a un real $a$, las imágenes convergerían a $\phi(a)$ y también a uno por el cálculo numérico; unicidad obligaría $\phi(a)=1$, fuera del recorrido. No tiene destino en esa métrica. La coincidencia de abiertos no preserva Cauchy ni acotación.

**Retorno visual.** Véase [C30-F08](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 40. Auditar la identidad inversa

[]{#MA-EX-ANM-01-030-040}

Muestre explícitamente que la identidad desde $(\mathbb R,e_\phi)$ hacia la usual es continua pero no uniformemente continua. Compare con la identidad entre $d_1$ y $d_\infty$.

[]{#MA-SOL-ANM-01-030-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La continuidad punto a punto se sigue de la igualdad de abiertos, ya probada. Para negar uniformidad, compare $n$ y $n+1$: su distancia usual es uno y la distancia $e_\phi$ es $1/((n+1)(n+2))\to0$. Con tolerancia de salida $1/2$, estos pares impiden un radio común. En contraste, la identidad de $d_\infty$ hacia $d_1$ es $2$-Lipschitz y la inversa es $1$-Lipschitz, por las desigualdades globales entre ambas. Esos certificados sí dan radios uniformes y transportan Cauchy en los dos sentidos.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-30)

[← Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Capítulo 31 →](analisis-para-matematicos-capitulo-31-completitud-compacidad-y-conexidad-en-espacios-metricos.html)
