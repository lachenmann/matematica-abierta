---
content-id: MA-BCH-0290
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-022
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
title: Capítulo 22 — Partir, refinar, acumular
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C22.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-22)

La integral elemental sugiere acumular alturas sobre anchuras. Aquí construimos los datos finitos y el control que permitirán convertir esa intuición en un número estable. Separamos cortes, resolución y elecciones de etiquetas; ninguna figura ni antiderivada proporciona por sí sola el límite.

C01–C03 aportan naturales, orden real y arquimedianidad; funciones, inducción y sumas finitas son interfaces heredadas. La integral elemental externa motiva y no se usa para demostrar. C23 reserva Darboux y sus equivalencias; C24 el teorema fundamental.

## 22.1. Un intervalo convertido en datos finitos

[]{#MA-SEC-ANM-01-022-001}

Fijemos reales $a<b$. Una partición es una lista finita estrictamente creciente

$$P=(x_0,\ldots,x_n),\qquad a=x_0<x_1<\cdots<x_n=b,\quad n\ge1.$$

La lista representa una función tipada del segmento natural $\{0,\ldots,n\}$ a $[a,b]$, junto con su longitud. El índice es natural, el nodo y la anchura son reales. La colección de tales objetos es un conjunto: sus grafos viven en el conjunto potencia de $\mathbb N\times[a,b]$; separar los grafos tipados y las listas que cumplen las condiciones da las particiones. Es no vacía porque $(a,b)$ es una partición.

Para $1\le i\le n$, llamamos $I_i=[x_{i-1},x_i]$ y $\Delta_i=x_i-x_{i-1}>0$. La inducción que añade una diferencia al final prueba la telescopía

$$\sum_{i=1}^n\Delta_i=b-a.$$

En el paso, $(x_n-a)+(x_{n+1}-x_n)=x_{n+1}-a$; no hay suma infinita. Además, estos intervalos cubren $[a,b]$. Si $t<b$, el menor índice $j$ con $t<x_j$ existe en un conjunto natural finito no vacío; entonces $x_{j-1}\le t<x_j$. Si $t=b$, usamos el último intervalo. Dos interiores distintos son disjuntos; intervalos consecutivos comparten un nodo. No llamamos disjuntos a los intervalos cerrados.

Para una representación como piezas disjuntas se puede usar $[a,x_1]$ y $(x_{i-1},x_i]$ para $i\ge2$. Más adelante distinguiremos el reparto de nodos de la longitud de las piezas. En $[0,1]$, la lista $(0,1/4,1)$ tiene anchuras $1/4,3/4$, no dos partes iguales.

La longitud $b-a$ es un dato algebraico demostrado. Un dibujo de rectángulos ayuda a reconocerla, pero aquí no presupone una noción de área para regiones curvas. Los intervalos degenerados y la orientación inversa quedan fuera de este contrato inicial.

![En \[0,1\], P=(0,1/4,1) tiene anchuras1/4 y3/4, suma1. Los cerrados vecinos comparten1/4; sus interiores son disjuntos.](../../assets/books/anm/C22/C22-F01.svg){#fig-anm-c22-f01 fig-alt="En \[0,1\], P=(0,1/4,1) tiene anchuras1/4 y3/4, suma1. Los cerrados vecinos comparten1/4; sus interiores son disjuntos."}

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-022-001}

¿Qué datos exige una partición de $[a,b]$?

[]{#MA-MSOL-ANM-01-022-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Una lista finita estrictamente creciente con primer nodo $a$, último $b$ y al menos una pieza, bajo $a<b$.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-022-002}

¿Son reales los índices?

[]{#MA-MSOL-ANM-01-022-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

No: son naturales. Los nodos y las anchuras son reales; cuando se multiplica por un índice se usa su copia real.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-022-003}

¿Por qué una anchura es positiva?

[]{#MA-MSOL-ANM-01-022-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

Porque $x_{i-1}<x_i$, por lo que $x_i-x_{i-1}>0$.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-022-004}

¿Cuánto suman las anchuras?

[]{#MA-MSOL-ANM-01-022-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

$b-a$, por telescopía finita: cada nodo interior aparece una vez positivo y otra negativo.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-022-005}

¿Son disjuntos los intervalos cerrados vecinos?

[]{#MA-MSOL-ANM-01-022-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

No: comparten su nodo. Sus interiores sí son disjuntos.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-022-006}

¿Cómo se localiza una entrada $t<b$?

[]{#MA-MSOL-ANM-01-022-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

Con el menor $j$ que cumple $t<x_j$; entonces $x_{j-1}\le t<x_j$.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-022-007}

¿Cuáles son las anchuras de $(0,1/4,1)$?

[]{#MA-MSOL-ANM-01-022-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

$1/4$ y $3/4$; suman1 y no son iguales.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-022-008}

¿Admite el contrato inicial $a=b$?

[]{#MA-MSOL-ANM-01-022-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No. Exige $a<b$; una convención degenerada se debe declarar separadamente.

</details>

### Ejercicios de la sección 22.1

[]{#ejercicios-22}

#### Ejercicio 1. Lista o dibujo

[]{#MA-EX-ANM-01-022-001}

Decide cuáles de $(0,1/2,1)$, $(0,1/2,1/2,1)$ y $(0,3/4,1/4,1)$ son particiones de $[0,1]$.

[]{#MA-SOL-ANM-01-022-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Sólo la primera: conserva extremos y tiene comparaciones estrictas. La segunda repite un nodo, por lo que hay anchura cero; la tercera disminuye de3/4 a1/4. Un dibujo con varios cortes no corrige esas fallas.

</details>

#### Ejercicio 2. Longitudes que telescopan

[]{#MA-EX-ANM-01-022-002}

Calcula anchuras de $P=(-1,-1/4,1/2,2)$ y demuestra la suma general por inducción.

[]{#MA-SOL-ANM-01-022-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Son3/4,3/4,3/2; suman3=2−(−1). Para una pieza la identidad es $x_1-x_0$. Si vale para $r$ piezas, añadir $x_{r+1}-x_r$ da $(x_r-x_0)+(x_{r+1}-x_r)=x_{r+1}-x_0$, que prueba el paso.

**Retorno visual.** Véase [C22-F01](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 3. Una entrada en su pieza

[]{#MA-EX-ANM-01-022-003}

Para la partición del ejercicio anterior localiza $t=0$ y $t=2$; demuestra la cobertura general.

[]{#MA-SOL-ANM-01-022-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Cero pertenece a $[-1/4,1/2]$ y2 al último intervalo. En general, si $t<b$, el menor $j$ con $t<x_j$ existe pues $n$ pertenece; no es0 porque $t\ge a$. La minimalidad da $x_{j-1}\le t<x_j$. Si $t=b$ pertenece al último, existente por $n\ge1$.

</details>

#### Ejercicio 4. Cerrar no es separar

[]{#MA-EX-ANM-01-022-004}

Explica el solapamiento de piezas cerradas y construye una cobertura disjunta para $(0,1/3,2/3,1)$.

[]{#MA-SOL-ANM-01-022-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Los cerrados vecinos comparten1/3 o2/3. La cobertura disjunta es $[0,1/3]$, $(1/3,2/3]$, $(2/3,1]$; cada punto pertenece a una sola pieza y la unión es $[0,1]$. No cambian las anchuras.

</details>

#### Ejercicio 5. El tipo de los objetos

[]{#MA-EX-ANM-01-022-005}

Describe una codificación de todas las particiones como conjunto y exhibe un elemento.

[]{#MA-SOL-ANM-01-022-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Codificar por $(n,p)$ con $p:\{0,\ldots,n\}\to[a,b]$ tipada. Sus grafos están en $\mathcal P(\mathbb N\times[a,b])$ y dominios en $\mathcal P(\mathbb N)$; el producto con $\mathbb N$ es conjunto ambiente. Separar los que tienen extremos y crecimiento estricto da el conjunto. $(1,p)$ con $p(0)=a,p(1)=b$ es un elemento porque $a<b$.

</details>
## 22.2. Refinar conservando los cortes

[]{#MA-SEC-ANM-01-022-002}

Escribimos $V(P)=\{x_0,\ldots,x_n\}$. La relación $P\preceq Q$ significa $V(P)\subseteq V(Q)$: el miembro derecho conserva todos los cortes antiguos. Admitimos igualdad; un refinamiento propio exige inclusión propia. Reflexividad y transitividad vienen de inclusión. Si hay inclusión en ambas direcciones, las listas estrictamente ordenadas del mismo conjunto finito coinciden: su primer nodo es el mínimo y se repite este argumento en el conjunto restante. Así tenemos antisimetría.

Para insertar $t\in(a,b)\setminus V(P)$, tomamos el menor $j$ con $t<x_j$. La minimalidad y $t\ne x_{j-1}$ dan $x_{j-1}<t<x_j$. La nueva lista copia los nodos anteriores a $j$, coloca $t$ en $j$ y desplaza una posición los demás. Sus únicas nuevas comparaciones son $x_{j-1}<t<x_j$; conserva extremos y es estricta. Divide una anchura en dos cuya suma es la antigua:

$$(t-x_{j-1})+(x_j-t)=x_j-x_{j-1}.$$

Insertar un nodo ya presente no modifica la lista. Repetir un nodo produciría una anchura cero y violaría la definición.

Para dos particiones $P,Q$, recorramos la lista de $Q$: conservamos cada nodo que ya aparece e insertamos cada otro por el procedimiento anterior. Una inducción finita construye $R$ con $V(R)=V(P)\cup V(Q)$. Entonces $P\preceq R$, $Q\preceq R$ y, si $S$ refina a ambas, la unión de nodos está contenida en $V(S)$: $R\preceq S$. Es el menor refinamiento común, no una elección de una familia infinita.

Por ejemplo, $(0,1/2,1)$ y $(0,1/3,2/3,1)$ tienen refinamiento común $(0,1/3,1/2,2/3,1)$. Sus cuatro anchuras son $1/3,1/6,1/6,1/3$. Refinar no quiere decir desplazar los cortes a posiciones aparentemente más regulares: reemplazar $1/2$ por $1/3$ pierde un nodo.

![P=(0,1/2,1) y Q=(0,1/3,2/3,1) se conservan en R=(0,1/3,1/2,2/3,1). Las anchuras de R son1/3,1/6,1/6,1/3.](../../assets/books/anm/C22/C22-F02.svg){#fig-anm-c22-f02 fig-alt="P=(0,1/2,1) y Q=(0,1/3,2/3,1) se conservan en R=(0,1/3,1/2,2/3,1). Las anchuras de R son1/3,1/6,1/6,1/3."}

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-022-009}

¿Qué significa $P\preceq Q$?

[]{#MA-MSOL-ANM-01-022-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

$V(P)\subseteq V(Q)$: $Q$ conserva todos los nodos de $P$.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-022-010}

¿Es una partición refinamiento de sí misma?

[]{#MA-MSOL-ANM-01-022-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

Sí. La inclusión permite igualdad; sólo el refinamiento propio exige un nodo nuevo.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-022-011}

¿Por qué la relación es transitiva?

[]{#MA-MSOL-ANM-01-022-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

La inclusión de nodos es transitiva.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-022-012}

¿Dónde se inserta un punto nuevo $t$?

[]{#MA-MSOL-ANM-01-022-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

Entre $x_{j-1}$ y $x_j$, donde $j$ es el menor índice con $t<x_j$.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-022-013}

¿Qué sucede si el punto ya era nodo?

[]{#MA-MSOL-ANM-01-022-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

No se modifica la partición. Repetirlo violaría crecimiento estricto.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-022-014}

¿Cuántas piezas añade una inserción propia?

[]{#MA-MSOL-ANM-01-022-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

Una: reemplaza una pieza por dos.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-022-015}

¿Qué nodos tiene el menor refinamiento común?

[]{#MA-MSOL-ANM-01-022-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

La unión finita $V(P)\cup V(Q)$, ordenada sin repeticiones.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-022-016}

¿Reemplazar $1/2$ por $1/3$ es refinar?

[]{#MA-MSOL-ANM-01-022-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

No en general: se pierde el nodo antiguo $1/2$.

</details>

### Ejercicios de la sección 22.2

#### Ejercicio 6. Insertar sin repetir

[]{#MA-EX-ANM-01-022-006}

Inserta $t=2/5$ en $(0,1/4,3/4,1)$; identifica las dos anchuras nuevas.

[]{#MA-SOL-ANM-01-022-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

La lista es $(0,1/4,2/5,3/4,1)$. La pieza original de anchura1/2 se divide en3/20 y7/20, cuya suma es1/2. Las restantes anchuras son1/4. El crecimiento estricto queda preservado.

</details>

#### Ejercicio 7. La unión que compara

[]{#MA-EX-ANM-01-022-007}

Construye el menor refinamiento común de $(0,1/2,1)$ y $(0,1/3,2/3,1)$ y justifica minimalidad.

[]{#MA-SOL-ANM-01-022-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

Es $(0,1/3,1/2,2/3,1)$. Cada nodo viene de una de las listas, por lo que refina a ambas. Cualquier refinamiento de ambas contiene su unión, y por eso refina a esta lista. Sus anchuras son1/3,1/6,1/6,1/3.

**Retorno visual.** Véase [C22-F02](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 8. Un nodo antiguo

[]{#MA-EX-ANM-01-022-008}

Explica por qué insertar $1/2$ en $(0,1/2,1)$ no añade una pieza válida.

[]{#MA-SOL-ANM-01-022-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

El conjunto de nodos permanece igual. Repetir1/2 en la lista rompería la comparación estricta y produciría una pieza de anchura cero. La única lista ordenada de ese conjunto es la original.

</details>

#### Ejercicio 9. Orden de resolución

[]{#MA-EX-ANM-01-022-009}

Demuestra reflexividad, transitividad y antisimetría de $\preceq$.

[]{#MA-SOL-ANM-01-022-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Las dos primeras son las propiedades de inclusión de nodos. Si $P\preceq Q$ y $Q\preceq P$, los conjuntos finitos coinciden. Sus listas crecientes tienen el mismo mínimo; eliminarlo y repetir por inducción da igualdad de todas las entradas y longitudes, luego $P=Q$.

</details>

#### Ejercicio 10. Mover no es añadir

[]{#MA-EX-ANM-01-022-010}

Compara $(0,1/2,1)$ y $(0,1/3,2/3,1)$ bajo refinamiento; explica cómo corregir la comparación.

[]{#MA-SOL-ANM-01-022-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Ninguna refina a la otra:1/2 falta en la segunda y1/3 falta en la primera. La comparación legítima se hace en la unión ordenada, que conserva todos los cortes y es refinamiento común.

</details>
## 22.3. La malla mide el peor intervalo

[]{#MA-SEC-ANM-01-022-003}

La **malla** es el máximo finito de las anchuras positivas:

$$\|P\|=\max_{1\le i\le n}\Delta_i.$$

Ese máximo existe por inducción finita: comparar el siguiente real con el máximo anterior. Se cumplen $0<\|P\|\le b-a$ y $b-a\le n\|P\|$, donde $n$ en la última expresión significa su copia real. Por tanto $\|P\|\ge(b-a)/n$.

Si $P\preceq Q$, cada pieza de $Q$ queda dentro de alguna pieza de $P$. Para verlo, localizamos su extremo izquierdo en los nodos de $P$; no puede atravesar un nodo antiguo en su interior, porque ese nodo también es de $Q$ y sus extremos son consecutivos. Su anchura es menor o igual que la antigua. Al tomar máximos, $\|Q\|\le\|P\|$. Una inserción propia puede conservar la malla si deja sin dividir una pieza máxima.

La partición uniforme $U_n$ tiene nodos $a+(b-a)i/n$ y malla $(b-a)/n$. Positividad de $n$ permite dividir; la arquimedianidad de C03 da, para $\delta>0$, un natural $n>(b-a)/\delta$, por lo que $\|U_n\|<\delta$. Hay siempre particiones suficientemente finas. Si necesitamos además conservar una partición dada, el refinamiento común con $U_n$ tiene malla menor que $\delta$.

Contar intervalos no basta. En $[0,1]$ podemos conservar $[0,1/2]$ y dividir $[1/2,1]$ en $m$ piezas iguales. Hay $m+1$ piezas, pero la malla es siempre $1/2$. Repetir este refinamiento con $m=2^k$ da una cadena anidada cuyo número de piezas crece sin que la malla tienda a cero. La resolución requerida es global sobre todas las piezas, no sólo sobre la región donde se añadieron cortes.

![Dividir sólo la mitad derecha produce2^k+1 piezas y malla fija1/2. La uniforme de n piezas tiene malla1/n. Contar no controla la pieza mayor.](../../assets/books/anm/C22/C22-F03.svg){#fig-anm-c22-f03 fig-alt="Dividir sólo la mitad derecha produce2^k+1 piezas y malla fija1/2. La uniforme de n piezas tiene malla1/n. Contar no controla la pieza mayor."}

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-022-017}

¿Qué mide la malla?

[]{#MA-MSOL-ANM-01-022-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

La máxima anchura de las piezas, no la anchura media ni su número.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-022-018}

¿Por qué existe ese máximo?

[]{#MA-MSOL-ANM-01-022-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

Es el máximo de una lista finita no vacía de reales, construido por comparaciones sucesivas.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-022-019}

¿Qué pasa con la malla al refinar?

[]{#MA-MSOL-ANM-01-022-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

No aumenta: cada pieza hija está contenida en un padre.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-022-020}

¿Un refinamiento propio reduce estrictamente la malla?

[]{#MA-MSOL-ANM-01-022-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

No. Puede dejar intacta una pieza de anchura máxima.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-022-021}

¿Cuál es la malla uniforme de $n$ piezas?

[]{#MA-MSOL-ANM-01-022-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

$(b-a)/n$, con $n\ge1$ y copia real positiva.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-022-022}

¿Cómo se logra malla menor que $\delta$?

[]{#MA-MSOL-ANM-01-022-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Arquimedianidad: elegir $n>(b-a)/\delta$ y usar la partición uniforme.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-022-023}

¿Por qué muchas piezas no bastan?

[]{#MA-MSOL-ANM-01-022-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

Se puede conservar una pieza de anchura1/2 y subdividir sólo el resto; la malla sigue siendo1/2.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-022-024}

¿Cómo se conserva una partición dada y se reduce su malla?

[]{#MA-MSOL-ANM-01-022-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

Se toma su refinamiento común con una uniforme suficientemente fina.

</details>

### Ejercicios de la sección 22.3

#### Ejercicio 11. Máximo o promedio

[]{#MA-EX-ANM-01-022-011}

Calcula malla y anchura media de $(0,1/4,1)$; demuestra $(b-a)/n\le\|P\|$.

[]{#MA-SOL-ANM-01-022-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Malla3/4, promedio1/2. Como cada anchura es≤malla, sumar $n$ desigualdades da $b-a\le n\|P\|$. La copia real de $n$ es positiva, por lo que dividir conserva el orden y da la cota.

</details>

#### Ejercicio 12. Cada hija tiene padre

[]{#MA-EX-ANM-01-022-012}

Demuestra que $P\preceq Q$ implica $\|Q\|\le\|P\|$.

[]{#MA-SOL-ANM-01-022-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Una pieza entre dos nodos consecutivos de $Q$ no puede contener un nodo de $P$ en su interior: también sería nodo de $Q$, contradicción. Localizarla entre nodos consecutivos antiguos da un padre que la contiene. Su anchura≤anchura padre≤malla antigua; el máximo de todas las hijas conserva la cota.

**Retorno visual.** Véase [C22-F03](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 13. Más piezas, mismo defecto

[]{#MA-EX-ANM-01-022-013}

Construye una cadena de refinamientos de $[0,1]$ con número de piezas creciente y malla1/2.

[]{#MA-SOL-ANM-01-022-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Para $k\ge0$, usar0,1/2 y los cortes $1/2+j/2^{k+1}$ con $1\le j\le2^k$. Cada siguiente lista divide las piezas de la mitad derecha y conserva los nodos anteriores. La izquierda mide1/2 y las derechas≤1/2; la malla es siempre1/2, aunque hay $2^k+1$ piezas.

</details>

#### Ejercicio 14. Resolución prescrita

[]{#MA-EX-ANM-01-022-014}

Construye una partición de $[-1,2]$ con malla estrictamente menor que1/10.

[]{#MA-SOL-ANM-01-022-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Longitud3; elegir uniforme con31 piezas da malla3/31<1/10. Los nodos $-1+3i/31$ son crecientes y tienen los extremos exigidos. Una de30 piezas sólo daría igualdad, que no satisface el pedido estricto.

</details>

#### Ejercicio 15. Conservar y mejorar

[]{#MA-EX-ANM-01-022-015}

Dada $P$ y $\delta>0$, prueba que hay un refinamiento de $P$ de malla menor que $\delta$.

[]{#MA-SOL-ANM-01-022-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Arquimedianidad proporciona $n>(b-a)/\delta$. $U_n$ tiene malla $(b-a)/n<\delta$. El menor refinamiento común $R$ de $P,U_n$ refina a $P$ y su malla≤malla de $U_n$, por el ejercicio anterior; así cumple el radio.

</details>
## 22.4. Etiquetas y acumulación firmada

[]{#MA-SEC-ANM-01-022-004}

Una partición etiquetada es $(P,\xi)$, con un dato real $\xi_i\in[x_{i-1},x_i]$ por cada pieza. La familia de etiquetas es una función de índices, no un conjunto que olvide cuál corresponde a cada pieza. Un nodo compartido puede etiquetar las dos piezas vecinas; no hay prohibición de repetir etiquetas. Existen etiquetas explícitas: extremos izquierdos, derechos o puntos medios.

Para $f:[a,b]\to\mathbb R$ definimos la suma finita

$$S(f;P,\xi)=\sum_{i=1}^n f(\xi_i)\Delta_i.$$

Cada altura se evalúa dentro del dominio. La suma existe incluso si $f$ no es acotada, pues se evalúa sólo un número finito de valores reales; eso no garantiza control uniforme de todas las sumas. Para $f\equiv c$, telescopía da $S=c(b-a)$ para cualquier partición y etiquetas. Alturas negativas producen contribuciones negativas: la suma es acumulación firmada, no área geométrica siempre positiva.

Por distributividad de sumas finitas,

$$S(\alpha f+\beta g;P,\xi)=\alpha S(f;P,\xi)+\beta S(g;P,\xi).$$

Si $f\le g$ en todo el intervalo, la positividad de cada anchura da $S(f;P,\xi)\le S(g;P,\xi)$. Se comparan la misma partición y las mismas etiquetas; cambiar esos datos puede cambiar el orden. Si $|f|\le M$, la triangular da $|S(f;P,\xi)|\le M(b-a)$, sin que $f$ alcance su cota.

Para $f(x)=x$ en $[0,1]$, $P=(0,1/2,1)$ tiene sumas izquierda $1/4$, media $1/2$ y derecha $3/4$. Para $f(x)=2x-1$, las mismas etiquetas producen $-1/2,0,1/2$. La cancelación de la suma media no borra las dos contribuciones de distinto signo.

![Para x en\[0,1\], dos piezas iguales dan sumas izquierda1/4, media1/2 y derecha3/4. Alturas etiquetadas, anchuras y valores se distinguen.](../../assets/books/anm/C22/C22-F04.svg){#fig-anm-c22-f04 fig-alt="Para x en\[0,1\], dos piezas iguales dan sumas izquierda1/4, media1/2 y derecha3/4. Alturas etiquetadas, anchuras y valores se distinguen."}

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-022-025}

¿Qué es una etiqueta?

[]{#MA-MSOL-ANM-01-022-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

Un punto dado $\xi_i\in[x_{i-1},x_i]$ para cada índice de pieza.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-022-026}

¿Pueden repetirse etiquetas?

[]{#MA-MSOL-ANM-01-022-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Sí: un nodo compartido puede etiquetar las dos piezas vecinas.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-022-027}

¿Cuál es la suma etiquetada?

[]{#MA-MSOL-ANM-01-022-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

$S(f;P,\xi)=\sum_i f(\xi_i)\Delta_i$, una suma real finita.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-022-028}

¿Una suma finita requiere que $f$ sea acotada?

[]{#MA-MSOL-ANM-01-022-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

No para existir; sí se necesitan hipótesis adicionales para controlar uniformemente todas las sumas.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-022-029}

¿Qué suma produce la constante $c$?

[]{#MA-MSOL-ANM-01-022-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

$c(b-a)$, cualquiera sea la partición y sus etiquetas.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-022-030}

¿Qué significa una contribución negativa?

[]{#MA-MSOL-ANM-01-022-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

Altura negativa por anchura positiva: acumulación firmada, no área geométrica negativa.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-022-031}

¿Qué datos se fijan al comparar $S(f)$ y $S(g)$?

[]{#MA-MSOL-ANM-01-022-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

La misma partición y las mismas etiquetas; $f\le g$ en el intervalo da el orden de sus sumas.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-022-032}

¿Qué cota da $|f|\le M$?

[]{#MA-MSOL-ANM-01-022-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

$|S|\le M\sum_i\Delta_i=M(b-a)$, sin máximo alcanzado.

</details>

### Ejercicios de la sección 22.4

#### Ejercicio 16. Lineal con tres etiquetas

[]{#MA-EX-ANM-01-022-016}

Para $f(x)=x$ y $(0,1/2,1)$ calcula sumas izquierda, media y derecha.

[]{#MA-SOL-ANM-01-022-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Las alturas son $(0,1/2)$, $(1/4,3/4)$ y $(1/2,1)$; las anchuras son ambas1/2. Las sumas son1/4,1/2 y3/4. No hay todavía igualdad de todas las sumas de una partición.

</details>

#### Ejercicio 17. Acumular con signo

[]{#MA-EX-ANM-01-022-017}

Para $f(x)=2x-1$ y la misma partición calcula las tres sumas y explica la cancelación media.

[]{#MA-SOL-ANM-01-022-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Alturas izquierda−1,0 dan−1/2; medias−1/2,1/2 dan0; derechas0,1 dan1/2. En la media hay una contribución−1/4 y otra1/4. El valor0 es su suma firmada y no una afirmación de área geométrica nula.

**Retorno visual.** Véase [C22-F04](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 18. Álgebra de una suma

[]{#MA-EX-ANM-01-022-018}

Demuestra linealidad y preservación de orden con partición y etiquetas fijas.

[]{#MA-SOL-ANM-01-022-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Sustituir $(\alpha f+\beta g)(\xi_i)=\alpha f(\xi_i)+\beta g(\xi_i)$, multiplicar por anchura y usar distributividad finita separa las dos sumas. Si $f\le g$, cada diferencia $(g(\xi_i)-f(\xi_i))\Delta_i\ge0$; sumar da el orden.

</details>

#### Ejercicio 19. Compartir una etiqueta

[]{#MA-EX-ANM-01-022-019}

En $(0,1/2,1)$ usa la etiqueta1/2 para ambas piezas. ¿Es válida? Calcula la suma de $x^2$.

[]{#MA-SOL-ANM-01-022-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Sí:1/2 pertenece a ambos intervalos cerrados. Ambas alturas valen1/4; multiplicar por1/2 y sumar da1/4. La familia de etiquetas conserva dos índices aun cuando sus valores coinciden.

</details>

#### Ejercicio 20. Cota sin máximo

[]{#MA-EX-ANM-01-022-020}

Si $-2\le f\le3$ en $[-1,2]$, acota todas las sumas y su valor absoluto.

[]{#MA-SOL-ANM-01-022-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Comparar con las constantes−2 y3 da $-6\le S\le9$. También $|f|\le3$ da $|S|\le9$ por triangular y longitud3. No se requiere que $f$ alcance−2 o3; son cotas universales dadas.

</details>
## 22.5. Lo que un cambio de etiquetas puede alterar

[]{#MA-SEC-ANM-01-022-005}

En una partición fija, dos familias $\xi,\eta$ cumplen

$$|S(f;P,\xi)-S(f;P,\eta)|
\le\sum_i |f(\xi_i)-f(\eta_i)|\Delta_i.$$

Es triangular después de restar término a término. Si disponemos de números dados $d_i\ge0$ que acotan $|f(s)-f(t)|$ para todos $s,t\in I_i$, obtenemos el certificado $\sum_i d_i\Delta_i$. No se exige un máximo ni llamamos aquí $d_i$ la oscilación exacta; C23 construirá esa noción con supremos.

Si $f$ es Lipschitz con constante dada $L\ge0$, entonces $|f(s)-f(t)|\le L|s-t|$ en todo el intervalo. Como las dos etiquetas de una pieza distan a lo sumo $\Delta_i$,

$$|S(f;P,\xi)-S(f;P,\eta)|\le L\sum_i\Delta_i^2
\le L\|P\|(b-a).$$

Se ha demostrado independencia progresiva de etiquetas sobre una partición; aún no existencia de un número límite para todas las particiones.

También podemos comparar con un refinamiento $Q$. Cada pieza hija $J$ queda en un padre $I_i$ y sus anchuras suman $\Delta_i$. Reescribimos la contribución antigua como suma de $f(\xi_i)|J|$ y restamos las nuevas. Tanto la etiqueta hija como la antigua están en $I_i$; la cota Lipschitz da

$$|S(f;Q,\eta)-S(f;P,\xi)|\le L\|P\|(b-a).$$

Para $P,Q$ arbitrarias, usar su refinamiento común y una familia explícita de etiquetas en él, luego triangular, da $L(b-a)(\|P\|+\|Q\|)$. No se requiere escoger etiquetas para una familia infinita.

No hay monotonía general de sumas etiquetadas al refinar. Para $f(x)=x$, la partición trivial etiquetada en $1/2$ da $1/2$; el refinamiento en mitades con etiquetas izquierdas da $1/4$ y con derechas $3/4$. Malla decreciente y orden de valores son asuntos distintos.

![Para x, la partición trivial etiquetada en1/2 da1/2. El refinamiento en mitades puede dar1/4 con izquierdas o3/4 con derechas. No hay monotonía de sumas arbitrarias.](../../assets/books/anm/C22/C22-F05.svg){#fig-anm-c22-f05 fig-alt="Para x, la partición trivial etiquetada en1/2 da1/2. El refinamiento en mitades puede dar1/4 con izquierdas o3/4 con derechas. No hay monotonía de sumas arbitrarias."}

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-022-033}

¿Cómo se controla cambiar sólo etiquetas?

[]{#MA-MSOL-ANM-01-022-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Por $\sum_i |f(\xi_i)-f(\eta_i)|\Delta_i$, usando resta y triangular.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-022-034}

¿Qué exige una cota local $d_i$?

[]{#MA-MSOL-ANM-01-022-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

Que controle todos los pares de entradas de la pieza, no sólo los dos valores muestreados.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-022-035}

¿Qué cota da Lipschitz para dos etiquetas de una pieza?

[]{#MA-MSOL-ANM-01-022-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

$L\Delta_i$, porque ambas distan a lo sumo su anchura.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-022-036}

¿Por qué $\sum_i\Delta_i^2\le\|P\|(b-a)$?

[]{#MA-MSOL-ANM-01-022-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

Cada $\Delta_i\le\|P\|$ y es positiva; multiplicar por $\Delta_i$ y sumar.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-022-037}

¿Qué controla comparar con un refinamiento?

[]{#MA-MSOL-ANM-01-022-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

$L\|P\|(b-a)$, por reescribir cada contribución antigua en las piezas hijas.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-022-038}

¿Cómo se comparan particiones diferentes?

[]{#MA-MSOL-ANM-01-022-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

Por su refinamiento común y triangular; cota $L(b-a)(\|P\|+\|Q\|)$.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-022-039}

¿Refinar ordena las sumas etiquetadas?

[]{#MA-MSOL-ANM-01-022-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

No. Para $x$, una suma1/2 puede dar1/4 o3/4 en el mismo refinamiento, según etiquetas.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-022-040}

¿Independencia de etiquetas ya prueba existencia de integral?

[]{#MA-MSOL-ANM-01-022-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No por sí sola; todavía se necesita un número que cumpla el contrato universal.

</details>

### Ejercicios de la sección 22.5

#### Ejercicio 21. Etiquetas que cambian

[]{#MA-EX-ANM-01-022-021}

Demuestra la cota de diferencia de etiquetas y aplícala a $f(x)=x$ en una partición de $[0,1]$.

[]{#MA-SOL-ANM-01-022-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Restar sumas y triangular da $|S_\xi-S_\eta|\le\sum|f(\xi_i)-f(\eta_i)|\Delta_i$. Para $x$, cada diferencia≤anchura, de modo que la suma≤$\sum\Delta_i^2\le\|P\|$, usando telescopía de longitudes1.

</details>

#### Ejercicio 22. De muestras a todas las entradas

[]{#MA-EX-ANM-01-022-022}

Explica por qué dos alturas casi iguales no proporcionan una cota local universal.

[]{#MA-SOL-ANM-01-022-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

Se puede definir una función cero en los dos puntos muestreados y con valor arbitrariamente grande en un tercer punto de la pieza. Las dos muestras coinciden, pero una etiqueta en el tercer punto cambia la suma en esa altura por la anchura. La cota $d_i$ necesita todos los pares, no dos evaluaciones.

</details>

#### Ejercicio 23. Comparar con hijas

[]{#MA-EX-ANM-01-022-023}

Prueba la cota $L\|P\|(b-a)$ entre una suma sobre $P$ y otra sobre un refinamiento bajo Lipschitz.

[]{#MA-SOL-ANM-01-022-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Las hijas de cada padre tienen anchuras que suman la antigua. Reescribir la suma vieja como $\sum_{J\subset I_i}f(\xi_i)|J|$ y restar las hijas. La diferencia de alturas≤$L\Delta_i$ porque ambas entradas están en el padre. Triangular y sumar dan $L\sum_i\Delta_i^2\le L\|P\|(b-a)$.

</details>

#### Ejercicio 24. Una suma puede ir a ambos lados

[]{#MA-EX-ANM-01-022-024}

Da dos sumas de un mismo refinamiento que estén a ambos lados de la suma media1/2 de $x$ en la partición trivial.

[]{#MA-SOL-ANM-01-022-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

Refinar en0,1/2,1. Etiquetas izquierdas dan1/4 y derechas3/4, respectivamente menores y mayores que1/2. Se conservan función e intervalo; cambia sólo la familia de etiquetas. Refinamiento no obliga monotonía de suma.

**Retorno visual.** Véase [C22-F05](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 25. Dos resoluciones distintas

[]{#MA-EX-ANM-01-022-025}

Si $f$ es Lipschitz3 en $[0,2]$ y las mallas de $P,Q$ son≤1/10 y≤1/20, acota cualquier diferencia de sus sumas.

[]{#MA-SOL-ANM-01-022-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

El refinamiento común $R$ y etiquetas dadas en él permiten triangular dos comparaciones con padres. La cota es $3\cdot2(\|P\|+\|Q\|)\le6(1/10+1/20)=9/10$. Es independiente de todas las etiquetas; no afirma por sí sola un valor integral.

</details>
## 22.6. Escalones: exactitud finita y nodos excepcionales

[]{#MA-SEC-ANM-01-022-006}

Un modelo escalonado tiene nodos $a=z_0<\cdots<z_m=b$ y valores $c_j$ constantes en cada interior $(z_{j-1},z_j)$. En los nodos permite valores reales dados, distintos de los vecinos. Definimos su acumulación elemental

$$A(s)=\sum_{j=1}^m c_j(z_j-z_{j-1}).$$

Insertar un corte dentro de una pieza copia la misma constante en las dos hijas y conserva $A$ por suma de anchuras. Si dos representaciones describen la misma función en los interiores, su refinamiento común tiene en cada interior hijo la misma constante de ambas: sumando allí muestra que $A$ no depende de la representación. Un punto interior hijo existe por el punto medio; los valores en un número finito de nodos no añaden una anchura.

No confundamos ese funcional con cualquier suma etiquetada. Si una partición respeta los cortes y sus etiquetas evitan los nodos, la suma es exactamente $A$. Si una etiqueta cae en un nodo cuyo valor es excepcional, puede perder esa igualdad.

Más generalmente, si $f,g$ sólo difieren en $k$ puntos y $|f-g|\le D$, una etiqueta que no esté en esos puntos da diferencia cero. Cada punto puede pertenecer a lo sumo a dos piezas cerradas de una partición. Por ello

$$|S(f;P,\xi)-S(g;P,\xi)|\le2kD\|P\|.$$

La cuenta puede sobreestimar, y en extremos sólo interviene una pieza; es una cota suficiente. Para $k=0$ es cero.

Probemos además estabilidad del escalón para particiones que no respetan sus cortes. Sea $B\ge0$ una cota de todos sus valores, incluidas las excepciones. Llevamos $P$ al refinamiento común con la representación del escalón. A cada hija damos como altura su constante interior; su suma es $A$. Padres cerrados que no tocan ningún nodo tienen altura constante, y contribución exactamente igual. Cada uno de los $m+1$ nodos toca a lo sumo dos padres, así que la longitud total de padres malos es como máximo $2(m+1)\|P\|$. La diferencia de alturas en cada uno es como máximo $2B$. Resulta

$$|S(s;P,\xi)-A(s)|\le4B(m+1)\|P\|.$$

Es un certificado conservador válido para cualquier partición y etiquetas; no se invoca una integral previa.

![Función cero salvo valor10 en1/2: en la partición en mitades ambas etiquetas pueden caer en1/2 y dar S=10, aunque la acumulación escalonada sea0. La cota2D·malla controla el efecto cuando la malla disminuye.](../../assets/books/anm/C22/C22-F06.svg){#fig-anm-c22-f06 fig-alt="Función cero salvo valor10 en1/2: en la partición en mitades ambas etiquetas pueden caer en1/2 y dar S=10, aunque la acumulación escalonada sea0. La cota2D·malla controla el efecto cuando la malla disminuye."}

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-022-041}

¿Cómo se calcula la acumulación de un escalón?

[]{#MA-MSOL-ANM-01-022-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

$A=\sum_j c_j(z_j-z_{j-1})$ con constantes interiores dadas.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-022-042}

¿Por qué insertar un corte conserva $A$?

[]{#MA-MSOL-ANM-01-022-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Se copia la altura y las dos anchuras suman la original.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-022-043}

¿Cómo se comparan dos representaciones del mismo escalón?

[]{#MA-MSOL-ANM-01-022-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

En el refinamiento común las constantes interiores coinciden; sumar allí da el mismo $A$.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-022-044}

¿Un valor aislado añade anchura a $A$?

[]{#MA-MSOL-ANM-01-022-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

No. Un nodo es un punto sin intervalo de anchura positiva.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-022-045}

¿Cualquier suma etiquetada coincide exactamente con $A$?

[]{#MA-MSOL-ANM-01-022-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

No. Puede usar etiquetas en nodos excepcionales o piezas que cruzan un salto.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-022-046}

¿Cuántas piezas cerradas contienen un punto fijo?

[]{#MA-MSOL-ANM-01-022-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

A lo sumo dos; en extremos a lo sumo una.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-022-047}

¿Qué cota da modificar $k$ puntos por diferencias de tamaño $D$?

[]{#MA-MSOL-ANM-01-022-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

Diferencia de sumas $\le2kD\|P\|$ para la misma partición y etiquetas.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-022-048}

¿Qué certificado universal obtuvo el escalón?

[]{#MA-MSOL-ANM-01-022-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

$|S-A|\le4B(m+1)\|P\|$, contando padres que tocan sus nodos.

</details>

### Ejercicios de la sección 22.6

#### Ejercicio 26. Un escalón firmado

[]{#MA-EX-ANM-01-022-026}

Sea $s=2$ en $(0,1/3)$ y $s=-1$ en $(1/3,1)$ con valores nodales arbitrarios. Calcula $A$ y prueba invariancia por una inserción.

[]{#MA-SOL-ANM-01-022-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

$A=2/3-2/3=0$. Insertar dentro de una región reemplaza $c(v-u)$ por $c(t-u)+c(v-t)=c(v-u)$. Los nodos excepcionales no entran en la fórmula de $A$. En el refinamiento común de dos representaciones las mismas constantes interiores prueban invariancia completa.

</details>

#### Ejercicio 27. Una etiqueta excepcional

[]{#MA-EX-ANM-01-022-027}

Para la función cero salvo $s(1/2)=10$, toma $(0,1/2,1)$ con ambas etiquetas en1/2. Compara $S$ y $A$.

[]{#MA-SOL-ANM-01-022-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Ambas alturas son10 y cada anchura1/2; $S=10$. Las constantes interiores son cero y $A=0$. Una suma etiquetada finita puede diferir mucho por repetir una etiqueta excepcional, aunque la integral futura sea0.

**Retorno visual.** Véase [C22-F06](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 28. Dos piezas por punto

[]{#MA-EX-ANM-01-022-028}

Prueba la cota $2kD\|P\|$ para funciones que sólo difieren en $k$ puntos y $|f-g|\le D$.

[]{#MA-SOL-ANM-01-022-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Una etiqueta con diferencia no nula debe ser uno de esos puntos. Cada punto está en a lo sumo dos piezas cerradas; las piezas no vecinas están separadas por nodos. Hay a lo sumo $2k$ términos no nulos, cada uno de valor absoluto≤$D\|P\|$. Triangular da la cota; para $k=0$ no hay términos.

</details>

#### Ejercicio 29. Sin alinear los cortes

[]{#MA-EX-ANM-01-022-029}

Demuestra el certificado $4B(m+1)\|P\|$ para un escalón con $m$ piezas y $|s|\le B$.

[]{#MA-SOL-ANM-01-022-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Refinar $P$ con todos los nodos del escalón y sumar las constantes interiores en las hijas: da $A$. Un padre que no toca ningún nodo aporta exactamente esa suma. Los otros padres son a lo sumo $2(m+1)$, porque cada nodo toca como máximo dos; su longitud total≤$2(m+1)\|P\|$. En ellos la diferencia de alturas≤$2B$. Multiplicar y triangular da la cota, con posibles sobrecuentas que sólo la ensanchan.

</details>

#### Ejercicio 30. Representación duplicada

[]{#MA-EX-ANM-01-022-030}

Representa la constante3 en $[0,2]$ con una pieza y con cortes1/2 y3/2; demuestra que ambas acumulaciones valen6.

[]{#MA-SOL-ANM-01-022-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Una pieza da $3\cdot2=6$. Las tres anchuras son1/2,1,1/2 y dan3/2+3+3/2=6. La invariancia general usa el refinamiento común y las constantes iguales en cada interior hijo, no un acuerdo casual de este ejemplo.

</details>
## 22.7. Un límite que todas las etiquetas deben compartir

[]{#MA-SEC-ANM-01-022-007}

Una función $f:[a,b]\to\mathbb R$ es **integrable de Riemann** si existe un real $I$ tal que

$$\forall\varepsilon>0\ \exists\delta>0\ \forall(P,\xi):
\quad \|P\|<\delta\ \Longrightarrow\ |S(f;P,\xi)-I|<\varepsilon.$$

El radio puede depender de $f,[a,b]$ y $\varepsilon$, pero se elige antes de la partición y de todas sus etiquetas. Denotamos ese real por $\int_a^b f(x)\,dx$. Es una definición mediante sumas finitas y tolerancias; la notación no afirma una antiderivada ni integra infinitesimales. Que se vea área en una figura es interpretación, no existencia automática.

El valor es único. Si $I,J$ cumplen el contrato y $d=|I-J|>0$, pedimos tolerancia $d/3$ a ambos y tomamos una partición uniforme de malla menor que los dos radios, con etiquetas explícitas. La triangular da $d<2d/3$, contradicción. La existencia de particiones pequeñas impide que el cuantificador universal sea vacío.

Si un certificado demostrado tiene forma $|S-I|\le C\|P\|$ para todas las particiones y etiquetas, con $C\ge0$, la definición se cumple: para $C>0$ tomamos $\delta=\varepsilon/C$ y para $C=0$ cualquier radio positivo. Por la sección anterior, los escalones son integrables y su integral es $A$. La cota de diferencias en $k$ puntos prueba que cambiar valores finitos conserva cualquier integral existente: para $2kD>0$ escogemos además $\|P\|<\varepsilon/(4kD)$ y pedimos error $\varepsilon/2$ al original; los casos de constante cero se separan.

El límite de una selección de sumas es consecuencia, no sustituto del contrato. Si $\|P_r\|\to0$ y cada $\xi^{(r)}$ es una familia dada, integrabilidad implica $S(f;P_r,\xi^{(r)})\to I$: para un $\delta$ válido, las mallas eventualmente quedan por debajo. Observar sólo una familia de etiquetas o una cadena de refinamientos no controla las demás. En particular, contar piezas no demuestra ni siquiera que sus mallas tiendan a cero.

No hemos probado que toda función acotada sea integrable ni que toda continua lo sea. C23 construirá cotas inferiores/superiores, oscilación y equivalencias. C24 conectará acumulación y derivación.

![Para x en\[0,1\], todas las sumas cumplen |S−1/2|≤malla/2. Con tolerancia1/20, un radio1/10 sirve; se exige malla estrictamente menor. Las muestras sólo ilustran la banda universal demostrada.](../../assets/books/anm/C22/C22-F07.svg){#fig-anm-c22-f07 fig-alt="Para x en\[0,1\], todas las sumas cumplen |S−1/2|≤malla/2. Con tolerancia1/20, un radio1/10 sirve; se exige malla estrictamente menor. Las muestras sólo ilustran la banda universal demostrada."}

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-022-049}

¿En qué orden se eligen los datos del límite?

[]{#MA-MSOL-ANM-01-022-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

Primero $I$, después cada tolerancia $\varepsilon$, luego $\delta$, y sólo entonces todas las particiones y etiquetas.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-022-050}

¿Puede $\delta$ depender de las etiquetas?

[]{#MA-MSOL-ANM-01-022-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

No. Debe servir para todas las etiquetas de todas las particiones de malla menor.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-022-051}

¿Por qué el contrato no es vacío?

[]{#MA-MSOL-ANM-01-022-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Existen particiones uniformes con malla menor que cualquier radio positivo.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-022-052}

¿Cómo se prueba unicidad?

[]{#MA-MSOL-ANM-01-022-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Si $d=|I-J|>0$, una suma dentro de $d/3$ de ambos daría $d<2d/3$ por triangular.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-022-053}

¿Qué radio sirve si $|S-I|\le C\|P\|$ y $C>0$?

[]{#MA-MSOL-ANM-01-022-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

$\delta=\varepsilon/C$; malla estrictamente menor da error estrictamente menor que $\varepsilon$.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-022-054}

¿Qué ocurre si $C=0$?

[]{#MA-MSOL-ANM-01-022-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Todas las sumas valen $I$; cualquier radio positivo sirve.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-022-055}

¿Qué implica integrabilidad para una sucesión dada de mallas que tienden a cero?

[]{#MA-MSOL-ANM-01-022-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

Sus sumas etiquetadas tienden a $I$ para cualquier familia dada de etiquetas.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-022-056}

¿Ya se probó integrabilidad de toda continua?

[]{#MA-MSOL-ANM-01-022-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No. Aquí se probaron escalones y ejemplos con certificados; C23 construirá resultados generales.

</details>

### Ejercicios de la sección 22.7

#### Ejercicio 31. El orden de los cuantificadores

[]{#MA-EX-ANM-01-022-031}

Escribe el contrato de integral y explica qué falla si el radio se permite depender de una partición ya elegida.

[]{#MA-SOL-ANM-01-022-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Existe $I$ tal que para cada $\varepsilon>0$ hay $\delta>0$ que sirve para todas las particiones y etiquetas con malla<radio. Si la partición se elige primero, se puede tomar un radio≤su malla y la implicación será vacía para ese objeto. No se controla ninguna familia de resoluciones pequeñas ni las demás etiquetas.

</details>

#### Ejercicio 32. Un valor único

[]{#MA-EX-ANM-01-022-032}

Demuestra unicidad del valor integral incluyendo una partición que satisfaga los dos radios.

[]{#MA-SOL-ANM-01-022-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Si $I\ne J$, sea $d=|I-J|>0$. Obtener radios $\delta_I,\delta_J$ para tolerancia $d/3$; una uniforme suficientemente fina cumple ambos. Con etiquetas izquierdas dadas, triangular da $d\le|I-S|+|S-J|<2d/3$, contradicción. La existencia de esa partición es arquimediana.

</details>

#### Ejercicio 33. Un radio efectivo

[]{#MA-EX-ANM-01-022-033}

Si todas las sumas cumplen $|S-I|\le5\|P\|$ en $[0,1]$, produce radio para tolerancia1/100 y número uniforme suficiente.

[]{#MA-SOL-ANM-01-022-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Tomar $\delta=1/500$. Malla estrictamente menor da error<1/100. La uniforme de501 piezas cumple1/501<1/500;500 piezas sólo garantizarían error≤1/100 y no la exigencia estricta.

**Retorno visual.** Véase [C22-F07](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Cambiar finitos valores

[]{#MA-EX-ANM-01-022-034}

Si $f$ es integrable y $g$ difiere sólo en $k$ puntos por diferencias≤$D$, demuestra misma integral.

[]{#MA-SOL-ANM-01-022-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Triangular $|S_g-I|\le|S_g-S_f|+|S_f-I|$. Pedir a $f$ error<ε/2. Si $2kD>0$, tomar además malla<ε/(4kD), que da diferencia<ε/2. El mínimo de los dos radios sirve. Si $2kD=0$, las sumas coinciden y basta el radio de $f$.

</details>

#### Ejercicio 35. De universal a una sucesión

[]{#MA-EX-ANM-01-022-035}

Sea $\|P_r\|\to0$ con etiquetas dadas. Demuestra convergencia de las sumas si $f$ es integrable y distingue la recíproca no demostrada.

[]{#MA-SOL-ANM-01-022-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Para ε, obtener δ del contrato universal; la convergencia de mallas da un índice tras el cual todas son<δ. Entonces todos los errores son<ε, que es convergencia a $I$. Invertir esta prueba no es válido: el control de una sola lista de particiones/etiquetas no abarca todas las demás.

</details>
## 22.8. Certificados antes de fórmulas de integración

[]{#MA-SEC-ANM-01-022-008}

Para $f(x)=x$ en $[a,b]$, el punto medio $m_i=(x_{i-1}+x_i)/2$ satisface

$$\sum_i m_i\Delta_i=\frac12\sum_i(x_i^2-x_{i-1}^2)=\frac{b^2-a^2}{2}.$$

Como $|\xi_i-m_i|\le\Delta_i/2$, cualquier suma etiquetada tiene error a lo sumo $(b-a)\|P\|/2$ respecto de ese número. Así queda probada su integral sin antiderivada. Para $\alpha x+\beta$, distributividad y telescopía producen valor $\alpha(b^2-a^2)/2+\beta(b-a)$ y cota $|\alpha|(b-a)\|P\|/2$.

Para $f(x)=x^2$ en $[0,1]$, pongamos $u=x_{i-1}$, $v=x_i$. La identidad del cubo da

$$\frac{v^3-u^3}{3}=(v-u)\frac{u^2+uv+v^2}{3}.$$

Todos $u^2,uv,v^2,\xi_i^2$ quedan entre $u^2$ y $v^2$. La diferencia entre $\xi_i^2$ y la media indicada es a lo sumo $v^2-u^2=(v-u)(v+u)\le2\Delta_i$. Sumando, telescopía prueba

$$\left|S(x^2;P,\xi)-\frac13\right|\le2\sum_i\Delta_i^2\le2\|P\|.$$

Existe integral y vale $1/3$. No hemos usado una regla general de integrar potencias. En la partición uniforme, sumas izquierda/derecha dan valores exactos

$$\frac13-\frac1{2n}+\frac1{6n^2},\qquad
\frac13+\frac1{2n}+\frac1{6n^2}.$$

La identidad $\sum_{i=1}^n i^2=n(n+1)(2n+1)/6$ que los produce se demuestra por inducción: el caso1 es directo; añadir $(n+1)^2$ y factorizar da la expresión con $n+1$. Las copias reales de índices y $n>0$ preceden a estas divisiones. Para $n=4$ los valores son $7/32$ y $15/32$, alrededor de $1/3$. La suma media es $1/3-1/(12n^2)$; procede de expandir $(i-1/2)^2$ y sumar. Una etiqueta central no da exactitud cuadrática.

Para error menor que $1/100$, el certificado universal $2\|P\|$ permite elegir $n>200$ en la partición uniforme, pero se aplica también a cualquier otra partición de esa malla. El límite probado conserva todas las etiquetas, incluso mezclas que no sean izquierda/derecha/media. Gráficas de unas pocas sumas ilustran este control ya demostrado. Preparar la integral es fabricar un límite estable; las cotas óptimas y las clases generales integrables pertenecen al capítulo siguiente.

![Para x² en\[0,1\], sumas uniformes izquierda/media/derecha se acercan a1/3 por fórmulas finitas. Con n4 valen7/32,21/64,15/32; el certificado2·malla sirve para toda etiqueta, no sólo estas tres.](../../assets/books/anm/C22/C22-F08.svg){#fig-anm-c22-f08 fig-alt="Para x² en\[0,1\], sumas uniformes izquierda/media/derecha se acercan a1/3 por fórmulas finitas. Con n4 valen7/32,21/64,15/32; el certificado2·malla sirve para toda etiqueta, no sólo estas tres."}

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-022-057}

¿Qué suma media da $x$ en $[a,b]$?

[]{#MA-MSOL-ANM-01-022-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

$(b^2-a^2)/2$ exactamente, por telescopía de cuadrados.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-022-058}

¿Qué cota controla otras etiquetas para $x$?

[]{#MA-MSOL-ANM-01-022-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

$(b-a)\|P\|/2$, pues la distancia al punto medio es a lo sumo media anchura.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-022-059}

¿Qué valor tiene $\alpha x+\beta$?

[]{#MA-MSOL-ANM-01-022-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

$\alpha(b^2-a^2)/2+\beta(b-a)$, por álgebra finita y el certificado del caso lineal.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-022-060}

¿Qué identidad local controla $x^2$?

[]{#MA-MSOL-ANM-01-022-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

$(v^3-u^3)/3=(v-u)(u^2+uv+v^2)/3$.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-022-061}

¿Qué cota universal certifica $1/3$?

[]{#MA-MSOL-ANM-01-022-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

$|S(x^2)-1/3|\le2\|P\|$ en $[0,1]$.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-022-062}

¿Cuáles son las sumas izquierda y derecha para $n=4$?

[]{#MA-MSOL-ANM-01-022-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

$7/32$ y $15/32$, respectivamente.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-022-063}

¿La etiqueta media es exacta para $x^2$?

[]{#MA-MSOL-ANM-01-022-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

No. La suma uniforme es $1/3-1/(12n^2)$.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-022-064}

¿Qué se requiere para error menor que $1/100$ mediante $2\|P\|$?

[]{#MA-MSOL-ANM-01-022-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Malla menor que1/200; en uniforme, un natural $n>200$.

</details>

### Ejercicios de la sección 22.8

#### Ejercicio 36. Una integral sin antiderivada

[]{#MA-EX-ANM-01-022-036}

Demuestra integral de $x$ en $[-1,2]$ usando puntos medios y da certificado.

[]{#MA-SOL-ANM-01-022-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

En cada pieza, media por anchura es $(v^2-u^2)/2$; sumar telescopa a $(4-1)/2=3/2$. Cualquier etiqueta difiere de la media≤anchura/2, por lo que el error total≤$(1/2)\sum\Delta_i^2\le(3/2)\|P\|$. El contrato con ese certificado prueba el valor3/2.

</details>

#### Ejercicio 37. Afín y firmada

[]{#MA-EX-ANM-01-022-037}

Calcula la integral de $2x-1$ en $[0,1]$ mediante sumas finitas y certificado.

[]{#MA-SOL-ANM-01-022-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

La suma es dos veces la de $x$ menos1, pues las anchuras suman1. El valor candidato es $2(1/2)-1=0$. El error≤$2\cdot\|P\|/2=\|P\|$. Escoger radioε prueba el contrato; no se ha interpretado el resultado como área geométrica total.

</details>

#### Ejercicio 38. El cubo controla el cuadrado

[]{#MA-EX-ANM-01-022-038}

Prueba el certificado universal de $x^2$ en $[0,1]$ y su valor integral.

[]{#MA-SOL-ANM-01-022-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

En $[u,v]$, la media $(u^2+uv+v^2)/3$ está entre $u^2,v^2$, igual que $\xi^2$. La diferencia≤$v^2-u^2\le2(v-u)$. Multiplicar por anchura y comparar con $(v^3-u^3)/3$ da error≤$2\Delta^2$. Sumar telescopa a1/3 y error≤$2\|P\|$. Para ε tomarδ=ε/2.

</details>

#### Ejercicio 39. Cuatro piezas no son el límite

[]{#MA-EX-ANM-01-022-039}

Calcula sumas izquierda, derecha y media de $x^2$ en uniforme de cuatro piezas, justificando las identidades de sumas.

[]{#MA-SOL-ANM-01-022-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Izquierda: $(0+1+4+9)/64=7/32$. Derecha: $(1+4+9+16)/64=15/32$. Media: $(1+9+25+49)/256=21/64$. Para todo n, inducción de $\sum i=n(n+1)/2$ y $\sum i^2=n(n+1)(2n+1)/6$, expandir $(i-1)^2$ o $(i-1/2)^2$ da las fórmulas del texto;21/64=1/3−1/192. Ninguna de estas sumas finitas es el límite1/3.

</details>

#### Ejercicio 40. Resolución de una tolerancia

[]{#MA-EX-ANM-01-022-040}

Elige una uniforme que certifique error de $x^2$ menor que1/100 para todas sus etiquetas; compara con el error de sus puntos medios.

[]{#MA-SOL-ANM-01-022-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La cota universal es2/n, así que n201 da2/201<1/100 para cualquier etiqueta. El error medio exacto es1/(12·201²), mucho menor. La cota universal sirve aun al mezclar etiquetas arbitrarias; usar sólo el error medio no certifica las demás familias.

**Retorno visual.** Véase [C22-F08](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-22)

[← Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Capítulo 23 →](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html)
