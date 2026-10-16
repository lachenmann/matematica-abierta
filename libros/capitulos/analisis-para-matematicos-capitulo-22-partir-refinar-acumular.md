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
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C22.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-22)

Para acumular los valores de una función en un intervalo, podemos dividirlo en piezas, escoger una altura en cada una y sumar los productos de altura por anchura. El resultado depende de las piezas y de las alturas elegidas. Antes de llamarlo integral necesitamos precisar qué significa hacer pequeñas todas las piezas y cómo controlar el efecto de esas elecciones. Las primeras garantías procederán de identidades entre sumas finitas.

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

![En \[0,1\], P=(0,1/4,1) tiene anchuras1/4 y3/4, suma1. Los cerrados vecinos comparten1/4; sus interiores son disjuntos.](../../assets/books/anm/C22/C22-F01.svg){#fig-anm-c22-f01 fig-alt="En [0,1], P=(0,1/4,1) tiene anchuras1/4 y3/4, suma1. Los cerrados vecinos comparten1/4; sus interiores son disjuntos."}

### Ejercicios de la sección 22.1

[]{#ejercicios-22}

#### Ejercicio 1. Lista o dibujo

[]{#MA-EX-ANM-01-022-001}

Decide cuáles de $(0,1/2,1)$, $(0,1/2,1/2,1)$ y $(0,3/4,1/4,1)$ son particiones de $[0,1]$.

[]{#MA-SOL-ANM-01-022-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

La lista $(0,1/2,1)$ cumple $0<1/2<1$ y conserva los dos extremos, así es una partición. En $(0,1/2,1/2,1)$ aparece una comparación de igualdad y la anchura correspondiente es cero. La tercera lista tiene $3/4>1/4$, por lo que deja de crecer y produce una anchura negativa. Sólo la primera satisface todas las condiciones del contrato.

</details>

#### Ejercicio 2. Longitudes que telescopan

[]{#MA-EX-ANM-01-022-002}

Calcula anchuras de $P=(-1,-1/4,1/2,2)$ y demuestra la suma general por inducción.

[]{#MA-SOL-ANM-01-022-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

Las anchuras son $-1/4-(-1)=3/4$, $1/2-(-1/4)=3/4$ y $2-1/2=3/2$. Su suma vale $3=2-(-1)$. Para una pieza, la suma general es $x_1-x_0$. Si hasta la pieza $r$ vale $x_r-x_0$, añadir $x_{r+1}-x_r$ deja $x_{r+1}-x_0$. La inducción finita prueba la identidad de longitudes para cualquier partición.

**Retorno visual.** Véase [C22-F01](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 3. Una entrada en su pieza

[]{#MA-EX-ANM-01-022-003}

Para la partición del ejercicio anterior localiza $t=0$ y $t=2$; demuestra la cobertura general.

[]{#MA-SOL-ANM-01-022-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Cero queda en $[-1/4,1/2]$, la segunda pieza, y dos en $[1/2,2]$, la última. Para una entrada $t<b$, el conjunto de índices con $t<x_j$ es no vacío porque contiene a $n$. Su mínimo $j$ es positivo y la minimalidad da $x_{j-1}\le t<x_j$. Para $t=b$ se usa directamente la última pieza, existente porque $n\ge1$. Así todo el segmento queda cubierto.

</details>

#### Ejercicio 4. Cerrar no es separar

[]{#MA-EX-ANM-01-022-004}

Explica el solapamiento de piezas cerradas y construye una cobertura disjunta para $(0,1/3,2/3,1)$.

[]{#MA-SOL-ANM-01-022-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Las piezas cerradas comparten sus nodos interiores: un tercio está en las dos primeras y dos tercios en las dos últimas. Una cobertura disjunta es $[0,1/3]$, $(1/3,2/3]$ y $(2/3,1]$. Los nodos compartidos se asignan ahora a una sola pieza y las demás entradas conservan su ubicación. La unión sigue siendo $[0,1]$ y las longitudes son las mismas.

</details>

#### Ejercicio 5. El tipo de los objetos

[]{#MA-EX-ANM-01-022-005}

Describe una codificación de todas las particiones como conjunto y exhibe un elemento.

[]{#MA-SOL-ANM-01-022-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Una partición puede codificarse por $(n,p)$, donde $n\in\mathbb N$, $n\ge1$ y $p:\{0,\ldots,n\}\to[a,b]$. Los grafos de esas funciones pertenecen al conjunto $\mathcal P(\mathbb N\times[a,b])$, así un ambiente para los códigos es $\mathbb N\times\mathcal P(\mathbb N\times[a,b])$. Separar los códigos con extremos $p(0)=a$, $p(n)=b$ y crecimiento estricto define el conjunto de particiones. El código con $n=1$ y valores $a,b$ pertenece a él porque $a<b$.

</details>

## 22.2. Refinar conservando los cortes

[]{#MA-SEC-ANM-01-022-002}

Escribimos $V(P)=\{x_0,\ldots,x_n\}$. La relación $P\preceq Q$ significa $V(P)\subseteq V(Q)$: el miembro derecho conserva todos los cortes antiguos. Admitimos igualdad; un refinamiento propio exige inclusión propia. Reflexividad y transitividad vienen de inclusión. Si hay inclusión en ambas direcciones, las listas estrictamente ordenadas del mismo conjunto finito coinciden: su primer nodo es el mínimo y se repite este argumento en el conjunto restante. Así tenemos antisimetría.

Para insertar $t\in(a,b)\setminus V(P)$, tomamos el menor $j$ con $t<x_j$. La minimalidad y $t\ne x_{j-1}$ dan $x_{j-1}<t<x_j$. La nueva lista copia los nodos anteriores a $j$, coloca $t$ en $j$ y desplaza una posición los demás. Sus únicas nuevas comparaciones son $x_{j-1}<t<x_j$; conserva extremos y es estricta. Divide una anchura en dos cuya suma es la antigua:

$$(t-x_{j-1})+(x_j-t)=x_j-x_{j-1}.$$

Insertar un nodo ya presente no modifica la lista. Repetir un nodo produciría una anchura cero y violaría la definición.

Dos particiones pueden tener cortes diferentes, de modo que ninguna refine a la otra. Para compararlas conservaremos todos los nodos de ambas. Recorremos la lista de $Q$ e insertamos en $P$ cada nodo que aún no aparezca. El procedimiento de inserción anterior y una inducción finita construyen una partición $R$ con $V(R)=V(P)\cup V(Q)$. Por construcción $P\preceq R$ y $Q\preceq R$. Si otra partición $S$ refina a ambas, contiene todos los nodos de la unión y por ello $R\preceq S$. Así obtenemos el menor refinamiento común mediante un número finito de inserciones.

Por ejemplo, $(0,1/2,1)$ y $(0,1/3,2/3,1)$ tienen refinamiento común $(0,1/3,1/2,2/3,1)$. Sus cuatro anchuras son $1/3,1/6,1/6,1/3$. Refinar no quiere decir desplazar los cortes a posiciones aparentemente más regulares: reemplazar $1/2$ por $1/3$ pierde un nodo.

![P=(0,1/2,1) y Q=(0,1/3,2/3,1) se conservan en R=(0,1/3,1/2,2/3,1). Las anchuras de R son1/3,1/6,1/6,1/3.](../../assets/books/anm/C22/C22-F02.svg){#fig-anm-c22-f02 fig-alt="P=(0,1/2,1) y Q=(0,1/3,2/3,1) se conservan en R=(0,1/3,1/2,2/3,1). Las anchuras de R son1/3,1/6,1/6,1/3."}

### Ejercicios de la sección 22.2

#### Ejercicio 6. Insertar sin repetir

[]{#MA-EX-ANM-01-022-006}

Inserta $t=2/5$ en $(0,1/4,3/4,1)$; identifica las dos anchuras nuevas.

[]{#MA-SOL-ANM-01-022-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

Las desigualdades $1/4<2/5<3/4$ localizan la inserción en la segunda pieza. La nueva lista es $(0,1/4,2/5,3/4,1)$. Sus dos anchuras nuevas son $2/5-1/4=3/20$ y $3/4-2/5=7/20$, ambas positivas y con suma $1/2$. Las otras dos anchuras siguen siendo $1/4$. Se conserva cada corte antiguo y se añade una pieza.

</details>

#### Ejercicio 7. La unión que compara

[]{#MA-EX-ANM-01-022-007}

Construye el menor refinamiento común de $(0,1/2,1)$ y $(0,1/3,2/3,1)$ y justifica minimalidad.

[]{#MA-SOL-ANM-01-022-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

La unión de nodos ordenada es $(0,1/3,1/2,2/3,1)$. Contiene ambas listas originales, por lo que las refina. Cualquier refinamiento común debe contener cada nodo de una u otra y por tanto esta unión; de ahí que sea el menor. Las anchuras son $1/3,1/6,1/6,1/3$, todas positivas y con suma uno.

**Retorno visual.** Véase [C22-F02](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 8. Un nodo antiguo

[]{#MA-EX-ANM-01-022-008}

Explica por qué insertar $1/2$ en $(0,1/2,1)$ no añade una pieza válida.

[]{#MA-SOL-ANM-01-022-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

El punto medio ya pertenece al conjunto de nodos. Insertar una segunda copia produciría dos coordenadas consecutivas iguales y anchura cero. La inserción válida deja la lista $(0,1/2,1)$ como estaba. Su conjunto ordenado de nodos no contiene una nueva pieza.

</details>

#### Ejercicio 9. Orden de resolución

[]{#MA-EX-ANM-01-022-009}

Demuestra reflexividad, transitividad y antisimetría de $\preceq$.

[]{#MA-SOL-ANM-01-022-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Reflexividad y transitividad proceden de las mismas propiedades de inclusión de conjuntos de nodos. Para antisimetría, $P\preceq Q$ y $Q\preceq P$ implican $V(P)=V(Q)$. Un conjunto finito de reales tiene una única lista estrictamente creciente: su primera entrada es el mínimo y, al retirarla, la inducción determina las restantes. Así las listas y sus longitudes coinciden y $P=Q$.

</details>

#### Ejercicio 10. Mover no es añadir

[]{#MA-EX-ANM-01-022-010}

Compara $(0,1/2,1)$ y $(0,1/3,2/3,1)$ bajo refinamiento; explica cómo corregir la comparación.

[]{#MA-SOL-ANM-01-022-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

La segunda lista no contiene el nodo $1/2$ y la primera no contiene $1/3$ ni $2/3$. Ninguna conserva todos los nodos de la otra, así son incomparables bajo refinamiento. Su unión ordenada sí da un refinamiento común. Mover un corte o comparar sólo el número de piezas no sustituye la inclusión requerida.

</details>

## 22.3. La malla mide el peor intervalo

[]{#MA-SEC-ANM-01-022-003}

La **malla** es el máximo finito de las anchuras positivas:

$$\|P\|=\max_{1\le i\le n}\Delta_i.$$

Ese máximo existe por inducción finita: comparar el siguiente real con el máximo anterior. Se cumplen $0<\|P\|\le b-a$ y $b-a\le n\|P\|$, donde $n$ en la última expresión significa su copia real. Por tanto $\|P\|\ge(b-a)/n$.

Si $P\preceq Q$, cada pieza de $Q$ queda dentro de alguna pieza de $P$. En efecto, entre dos nodos consecutivos de $Q$ no puede haber un nodo antiguo: también sería de $Q$ y contradiría que los extremos son consecutivos. Localizando el extremo izquierdo se identifica, pues, una pieza antigua que contiene toda la nueva. Su anchura no supera la del padre, y tomar máximos da $\|Q\|\le\|P\|$. La desigualdad puede ser una igualdad aun en un refinamiento propio: basta dejar sin dividir una pieza que conserve la anchura máxima.

Para conseguir una malla menor que un radio dado $\delta>0$, repartimos la longitud en partes iguales. La partición uniforme $U_n$ tiene nodos $a+(b-a)i/n$ y malla $(b-a)/n$. La arquimedianidad de C03 proporciona un natural $n>(b-a)/\delta$; es positivo y permite dividir para obtener $\|U_n\|<\delta$. Si también debemos conservar una partición ya fijada, tomamos su refinamiento común con $U_n$. Como refina a la uniforme, su malla sigue siendo menor que $\delta$.

Contar intervalos no basta. En $[0,1]$ podemos conservar $[0,1/2]$ y dividir $[1/2,1]$ en $m$ piezas iguales. Hay $m+1$ piezas, pero la malla es siempre $1/2$. Repetir este refinamiento con $m=2^k$ da una cadena anidada cuyo número de piezas crece sin que la malla tienda a cero. La resolución requerida es global sobre todas las piezas, no sólo sobre la región donde se añadieron cortes.

![Dividir sólo la mitad derecha produce2^k+1 piezas y malla fija1/2. La uniforme de n piezas tiene malla1/n. Contar no controla la pieza mayor.](../../assets/books/anm/C22/C22-F03.svg){#fig-anm-c22-f03 fig-alt="Dividir sólo la mitad derecha produce2^k+1 piezas y malla fija1/2. La uniforme de n piezas tiene malla1/n. Contar no controla la pieza mayor."}

### Ejercicios de la sección 22.3

#### Ejercicio 11. Máximo o promedio

[]{#MA-EX-ANM-01-022-011}

Calcula malla y anchura media de $(0,1/4,1)$; demuestra $(b-a)/n\le\|P\|$.

[]{#MA-SOL-ANM-01-022-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Las anchuras son $1/4$ y $3/4$, por lo que la malla es $3/4$ y el promedio $1/2$. En general, cada $\Delta_i\le\|P\|$. Sumar las $n$ desigualdades y usar telescopía da $b-a\le n\|P\|$. La copia real de $n\ge1$ es positiva, y dividir entrega $(b-a)/n\le\|P\|$.

</details>

#### Ejercicio 12. Cada hija tiene padre

[]{#MA-EX-ANM-01-022-012}

Demuestra que $P\preceq Q$ implica $\|Q\|\le\|P\|$.

[]{#MA-SOL-ANM-01-022-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Sean $u<v$ dos nodos consecutivos de $Q$. Ningún nodo de $P$ puede quedar estrictamente entre ellos, pues también sería nodo de $Q$. Por ello la pieza $[u,v]$ está contenida en algún padre de $P$. Su anchura no supera la del padre, que a su vez no supera $\|P\|$. Tomar el máximo de todas las anchuras nuevas da $\|Q\|\le\|P\|$.

**Retorno visual.** Véase [C22-F03](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 13. Más piezas, mismo defecto

[]{#MA-EX-ANM-01-022-013}

Construye una cadena de refinamientos de $[0,1]$ con número de piezas creciente y malla1/2.

[]{#MA-SOL-ANM-01-022-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Para $k\ge0$ tomamos los nodos cero, un medio y $1/2+j/2^{k+1}$ para $1\le j\le2^k$. Los nuevos cortes sólo subdividen la mitad derecha y los cortes anteriores se conservan. La mitad izquierda sigue siendo una pieza de anchura $1/2$, mientras todas las derechas miden $1/2^{k+1}\le1/2$. La malla es siempre $1/2$, aunque el número de piezas $2^k+1$ crece sin cota.

</details>

#### Ejercicio 14. Resolución prescrita

[]{#MA-EX-ANM-01-022-014}

Construye una partición de $[-1,2]$ con malla estrictamente menor que1/10.

[]{#MA-SOL-ANM-01-022-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

El segmento tiene longitud tres. Una uniforme de treinta y una piezas tiene nodos $x_i=-1+3i/31$ y anchura $3/31<1/10$. Su lista es estrictamente creciente y va de menos uno a dos. Con treinta piezas se obtendría malla exactamente $1/10$, insuficiente para el pedido estricto.

</details>

#### Ejercicio 15. Conservar y mejorar

[]{#MA-EX-ANM-01-022-015}

Dada $P$ y $\delta>0$, prueba que hay un refinamiento de $P$ de malla menor que $\delta$.

[]{#MA-SOL-ANM-01-022-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Arquimedianidad da un natural $n>(b-a)/\delta$, y la uniforme $U_n$ cumple $\|U_n\|<\delta$. Formamos el refinamiento común $R$ con los nodos de $P$ y $U_n$. Conserva todos los cortes de $P$ y su malla no supera la de $U_n$. Por tanto $P\preceq R$ y $\|R\|<\delta$.

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

![Para x en\[0,1\], dos piezas iguales dan sumas izquierda1/4, media1/2 y derecha3/4. Alturas etiquetadas, anchuras y valores se distinguen.](../../assets/books/anm/C22/C22-F04.svg){#fig-anm-c22-f04 fig-alt="Para x en[0,1], dos piezas iguales dan sumas izquierda1/4, media1/2 y derecha3/4. Alturas etiquetadas, anchuras y valores se distinguen."}

### Ejercicios de la sección 22.4

#### Ejercicio 16. Lineal con tres etiquetas

[]{#MA-EX-ANM-01-022-016}

Para $f(x)=x$ y $(0,1/2,1)$ calcula sumas izquierda, media y derecha.

[]{#MA-SOL-ANM-01-022-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Las dos anchuras son $1/2$. Las etiquetas izquierdas $(0,1/2)$ dan $0\cdot1/2+(1/2)\cdot1/2=1/4$. Las medias $(1/4,3/4)$ dan $1/2$, y las derechas $(1/2,1)$ dan $3/4$. La función y partición son las mismas; sólo cambia la familia de alturas. Estas sumas finitas todavía no son iguales entre sí.

</details>

#### Ejercicio 17. Acumular con signo

[]{#MA-EX-ANM-01-022-017}

Para $f(x)=2x-1$ y la misma partición calcula las tres sumas y explica la cancelación media.

[]{#MA-SOL-ANM-01-022-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Para $2x-1$, las alturas izquierdas son menos uno y cero, las medias menos un medio y un medio, y las derechas cero y uno. Ponderar cada pareja por las anchuras $1/2$ produce sumas $-1/2$, cero y $1/2$. En la media se cancelan contribuciones $-1/4$ y $1/4$. El resultado describe acumulación firmada; las magnitudes geométricas de ambas regiones no se cancelarían.

**Retorno visual.** Véase [C22-F04](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 18. Álgebra de una suma

[]{#MA-EX-ANM-01-022-018}

Demuestra linealidad y preservación de orden con partición y etiquetas fijas.

[]{#MA-SOL-ANM-01-022-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Con partición y etiquetas fijas, sustituimos $(\alpha f+\beta g)(\xi_i)=\alpha f(\xi_i)+\beta g(\xi_i)$. La distributividad de sumas finitas da $S(\alpha f+\beta g)=\alpha S(f)+\beta S(g)$. Si $f\le g$, cada término $(g(\xi_i)-f(\xi_i))\Delta_i$ es no negativo porque la anchura es positiva. Sumar prueba $S(f)\le S(g)$.

</details>

#### Ejercicio 19. Compartir una etiqueta

[]{#MA-EX-ANM-01-022-019}

En $(0,1/2,1)$ usa la etiqueta1/2 para ambas piezas. ¿Es válida? Calcula la suma de $x^2$.

[]{#MA-SOL-ANM-01-022-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

La etiqueta $1/2$ pertenece tanto a $[0,1/2]$ como a $[1/2,1]$, así es válida en ambas. Para el cuadrado, ambas alturas valen $1/4$. La suma es $(1/4)(1/2)+(1/4)(1/2)=1/4$. Las etiquetas siguen siendo dos datos indexados aunque coincida su coordenada.

</details>

#### Ejercicio 20. Cota sin máximo

[]{#MA-EX-ANM-01-022-020}

Si $-2\le f\le3$ en $[-1,2]$, acota todas las sumas y su valor absoluto.

[]{#MA-SOL-ANM-01-022-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

La longitud de $[-1,2]$ es tres. Comparar las alturas con constantes da $-2\cdot3\le S\le3\cdot3$, es decir $-6\le S\le9$. La triangular y $|f|\le3$ dan además $|S|\le9$. Las barreras protegen todas las entradas sin exigir que exista un argumento de máximo o mínimo.

</details>

## 22.5. Lo que un cambio de etiquetas puede alterar

[]{#MA-SEC-ANM-01-022-005}

En una partición fija, dos familias $\xi,\eta$ cumplen

$$|S(f;P,\xi)-S(f;P,\eta)|
\le\sum_i |f(\xi_i)-f(\eta_i)|\Delta_i.$$

Al restar las sumas con la misma partición, las anchuras coinciden término a término. La desigualdad triangular da entonces la fórmula. Si para cada pieza disponemos de un número $d_i\ge0$ que acota $|f(s)-f(t)|$ para todos $s,t\in I_i$, podemos sustituir esas cotas y obtener el certificado $\sum_i d_i\Delta_i$. Basta que sean barreras válidas; no exigimos que se alcancen ni que sean las mejores posibles. La oscilación exacta se construirá con supremos en C23.

Si $f$ es Lipschitz con constante dada $L\ge0$, entonces $|f(s)-f(t)|\le L|s-t|$ en todo el intervalo. Como las dos etiquetas de una pieza distan a lo sumo $\Delta_i$,

$$|S(f;P,\xi)-S(f;P,\eta)|\le L\sum_i\Delta_i^2
\le L\|P\|(b-a).$$

Se ha demostrado independencia progresiva de etiquetas sobre una partición; aún no existencia de un número límite para todas las particiones.

La misma idea permite comparar una partición con un refinamiento $Q$. Dentro de cada padre $I_i$, las anchuras de las piezas hijas $J$ suman $\Delta_i$. Podemos por ello escribir su contribución antigua como $\sum_{J\subset I_i}f(\xi_i)|J|$ y restar las nuevas contribuciones. Las dos alturas se evalúan en el mismo padre, así que su diferencia absoluta es a lo sumo $L\Delta_i\le L\|P\|$. Multiplicar por $|J|$ y sumar todas las hijas deja como longitud total $b-a$. Resulta

$$|S(f;Q,\eta)-S(f;P,\xi)|\le L\|P\|(b-a).$$

Para comparar $P,Q$ arbitrarias, las llevamos a su refinamiento común $R$ y elegimos allí etiquetas explícitas, por ejemplo los extremos izquierdos. El error entre cada suma original y la de $R$ está controlado por la malla de su propia partición. La triangular da así $L(b-a)(\|P\|+\|Q\|)$. Una sola familia de etiquetas en un refinamiento finito basta para esta comparación.

No hay monotonía general de sumas etiquetadas al refinar. Para $f(x)=x$, la partición trivial etiquetada en $1/2$ da $1/2$; el refinamiento en mitades con etiquetas izquierdas da $1/4$ y con derechas $3/4$. Malla decreciente y orden de valores son asuntos distintos.

![Para x, la partición trivial etiquetada en1/2 da1/2. El refinamiento en mitades puede dar1/4 con izquierdas o3/4 con derechas. No hay monotonía de sumas arbitrarias.](../../assets/books/anm/C22/C22-F05.svg){#fig-anm-c22-f05 fig-alt="Para x, la partición trivial etiquetada en1/2 da1/2. El refinamiento en mitades puede dar1/4 con izquierdas o3/4 con derechas. No hay monotonía de sumas arbitrarias."}

### Ejercicios de la sección 22.5

#### Ejercicio 21. Etiquetas que cambian

[]{#MA-EX-ANM-01-022-021}

Demuestra la cota de diferencia de etiquetas y aplícala a $f(x)=x$ en una partición de $[0,1]$.

[]{#MA-SOL-ANM-01-022-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Restar sumas con las mismas anchuras da $S_\xi-S_\eta=\sum_i(f(\xi_i)-f(\eta_i))\Delta_i$. Por triangular, su magnitud no supera $\sum_i|f(\xi_i)-f(\eta_i)|\Delta_i$. Para la identidad, cada diferencia es $|\xi_i-\eta_i|\le\Delta_i$. En $[0,1]$ resulta $|S_\xi-S_\eta|\le\sum_i\Delta_i^2\le\|P\|$, porque las anchuras suman uno.

</details>

#### Ejercicio 22. De muestras a todas las entradas

[]{#MA-EX-ANM-01-022-022}

Explica por qué dos alturas casi iguales no proporcionan una cota local universal.

[]{#MA-SOL-ANM-01-022-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

En una pieza de longitud positiva tomamos dos entradas muestreadas y una tercera distinta. Una función puede valer cero en las dos primeras y una altura $H$ arbitrariamente grande en la tercera. Las muestras coinciden exactamente, pero usar la tercera como etiqueta cambia su contribución en $H$ por la anchura. La cota local que protege cualquier etiqueta debe limitar todas las parejas de entradas de la pieza.

</details>

#### Ejercicio 23. Comparar con hijas

[]{#MA-EX-ANM-01-022-023}

Prueba la cota $L\|P\|(b-a)$ entre una suma sobre $P$ y otra sobre un refinamiento bajo Lipschitz.

[]{#MA-SOL-ANM-01-022-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

En cada padre $I_i$, las anchuras de sus hijas suman $\Delta_i$. Reescribimos la contribución antigua como $\sum_{J\subseteq I_i}f(\xi_i)|J|$. La etiqueta de cada hija y la antigua están en ese padre, de modo que Lipschitz limita su diferencia de alturas por $L\Delta_i$. Ponderar por las longitudes hijas y sumar da $L\Delta_i^2$. Finalmente, la triangular entrega $|S_P-S_Q|\le L\sum_i\Delta_i^2\le L\|P\|(b-a)$.

</details>

#### Ejercicio 24. Una suma puede ir a ambos lados

[]{#MA-EX-ANM-01-022-024}

Da dos sumas de un mismo refinamiento que estén a ambos lados de la suma media1/2 de $x$ en la partición trivial.

[]{#MA-SOL-ANM-01-022-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

La partición trivial $(0,1)$ con etiqueta media produce suma $1/2$ para la identidad. En el refinamiento $(0,1/2,1)$, las etiquetas izquierdas producen $1/4$ y las derechas $3/4$. Una queda por debajo y otra por encima de la suma antigua. Refinar conserva cortes, pero no decide un sentido de cambio para sumas etiquetadas.

**Retorno visual.** Véase [C22-F05](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 25. Dos resoluciones distintas

[]{#MA-EX-ANM-01-022-025}

Si $f$ es Lipschitz3 en $[0,2]$ y las mallas de $P,Q$ son≤1/10 y≤1/20, acota cualquier diferencia de sus sumas.

[]{#MA-SOL-ANM-01-022-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Tomamos el refinamiento común y una familia explícita de etiquetas en él, por ejemplo las izquierdas. Cada suma original se compara con esa tercera usando su malla y la barrera Lipschitz tres. La triangular da $|S_P-S_Q|\le3\cdot2(\|P\|+\|Q\|)\le6(1/10+1/20)=9/10$. La cota protege todas las etiquetas originales y no identifica todavía un valor integral.

</details>

## 22.6. Escalones: exactitud finita y nodos excepcionales

[]{#MA-SEC-ANM-01-022-006}

Un modelo escalonado tiene nodos $a=z_0<\cdots<z_m=b$ y valores $c_j$ constantes en cada interior $(z_{j-1},z_j)$. En los nodos permite valores reales dados, distintos de los vecinos. Definimos su acumulación elemental

$$A(s)=\sum_{j=1}^m c_j(z_j-z_{j-1}).$$

Insertar un corte dentro de una pieza reparte su anchura y copia la misma constante en las dos hijas, por lo que conserva $A$. Si dos representaciones describen la misma función en los interiores, pasamos a su refinamiento común. Cada interior hijo contiene su punto medio y está dentro de un interior de cada representación. Evaluar allí la función identifica las dos constantes; sumar las contribuciones de las hijas muestra que ambas representaciones dan el mismo $A$. Los valores en los nodos pueden ser excepcionales, pero esos puntos no añaden ninguna anchura a la suma definida.

No confundamos ese funcional con cualquier suma etiquetada. Si una partición respeta los cortes y sus etiquetas evitan los nodos, la suma es exactamente $A$. Si una etiqueta cae en un nodo cuyo valor es excepcional, puede perder esa igualdad.

Más generalmente, si $f,g$ sólo difieren en $k$ puntos y $|f-g|\le D$, una etiqueta que no esté en esos puntos da diferencia cero. Cada punto puede pertenecer a lo sumo a dos piezas cerradas de una partición. Por ello

$$|S(f;P,\xi)-S(g;P,\xi)|\le2kD\|P\|.$$

La cuenta puede sobreestimar, y en extremos sólo interviene una pieza; es una cota suficiente. Para $k=0$ es cero.

Para controlar también particiones que no respetan los cortes del escalón, sea $B\ge0$ una cota de todos sus valores, incluidas las excepciones. Refinamos $P$ con la representación del escalón y asignamos a cada hija su constante interior; esta suma vale $A$. Un padre cerrado que no toca ningún nodo del escalón tiene altura constante y su contribución no cambia. Sólo debemos estimar los padres que tocan algún nodo. Cada uno de los $m+1$ nodos pertenece a lo sumo a dos padres, cada padre tiene longitud a lo sumo $\|P\|$ y cada diferencia de alturas es a lo sumo $2B$. Aunque esta cuenta repita algún padre, proporciona la barrera suficiente

$$|S(s;P,\xi)-A(s)|\le4B(m+1)\|P\|.$$

Es un certificado conservador válido para cualquier partición y etiquetas; no se invoca una integral previa.

![Función cero salvo valor10 en1/2: en la partición en mitades ambas etiquetas pueden caer en1/2 y dar S=10, aunque la acumulación escalonada sea0. La cota2D·malla controla el efecto cuando la malla disminuye.](../../assets/books/anm/C22/C22-F06.svg){#fig-anm-c22-f06 fig-alt="Función cero salvo valor10 en1/2: en la partición en mitades ambas etiquetas pueden caer en1/2 y dar S=10, aunque la acumulación escalonada sea0. La cota2D·malla controla el efecto cuando la malla disminuye."}

### Ejercicios de la sección 22.6

#### Ejercicio 26. Un escalón firmado

[]{#MA-EX-ANM-01-022-026}

Sea $s=2$ en $(0,1/3)$ y $s=-1$ en $(1/3,1)$ con valores nodales arbitrarios. Calcula $A$ y prueba invariancia por una inserción.

[]{#MA-SOL-ANM-01-022-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

La acumulación es $A=2(1/3)+(-1)(2/3)=0$. Insertar un corte $t$ dentro de una región constante de altura $c$ conserva su contribución porque $c(t-u)+c(v-t)=c(v-u)$. Las demás regiones quedan intactas. Los valores nodales arbitrarios no aparecen en esta fórmula; su efecto sobre sumas etiquetadas se controla por otro argumento.

</details>

#### Ejercicio 27. Una etiqueta excepcional

[]{#MA-EX-ANM-01-022-027}

Para la función cero salvo $s(1/2)=10$, toma $(0,1/2,1)$ con ambas etiquetas en1/2. Compara $S$ y $A$.

[]{#MA-SOL-ANM-01-022-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Las dos etiquetas iguales a un medio leen la altura excepcional diez. Con anchuras medias, $S=10/2+10/2=10$. Las constantes interiores de ambos lados son cero y su acumulación $A$ es cero. Esta diferencia pertenece a una suma concreta de malla $1/2$; al reducir la malla el certificado limita cuánto pueden pesar etiquetas excepcionales.

**Retorno visual.** Véase [C22-F06](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 28. Dos piezas por punto

[]{#MA-EX-ANM-01-022-028}

Prueba la cota $2kD\|P\|$ para funciones que sólo difieren en $k$ puntos y $|f-g|\le D$.

[]{#MA-SOL-ANM-01-022-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Un término sólo cambia si su etiqueta es alguno de los $k$ puntos modificados. Cada punto pertenece como máximo a dos piezas cerradas, así hay a lo sumo $2k$ términos afectados. Cada uno tiene magnitud a lo sumo $D\Delta_i\le D\|P\|$. La triangular da $|S_f-S_g|\le2kD\|P\|$. Si $k=0$ o $D=0$, las sumas coinciden.

</details>

#### Ejercicio 29. Sin alinear los cortes

[]{#MA-EX-ANM-01-022-029}

Demuestra el certificado $4B(m+1)\|P\|$ para un escalón con $m$ piezas y $|s|\le B$.

[]{#MA-SOL-ANM-01-022-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Refinamos $P$ añadiendo los $m+1$ nodos del escalón y calculamos $A$ con sus constantes interiores en las piezas hijas. Un padre que no toca esos nodos queda dentro de una región constante y aporta exactamente lo mismo que sus hijas. Los padres restantes son a lo sumo $2(m+1)$ y su longitud total no supera $2(m+1)\|P\|$. En cada uno, la diferencia entre su altura y cualquier altura hija no supera $2B$. Ponderar y sumar produce $|S-A|\le4B(m+1)\|P\|$, aun si el recuento repite algún padre.

</details>

#### Ejercicio 30. Representación duplicada

[]{#MA-EX-ANM-01-022-030}

Representa la constante3 en $[0,2]$ con una pieza y con cortes1/2 y3/2; demuestra que ambas acumulaciones valen6.

[]{#MA-SOL-ANM-01-022-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Una única pieza de longitud dos y altura tres aporta seis. Con cortes $1/2$ y $3/2$, las anchuras son $1/2$, uno y $1/2$, y las contribuciones $3/2$, tres y $3/2$ suman seis. La identidad de longitudes explica esta igualdad para cualquier subdivisión de una región constante. Dos representaciones generales se comparan mediante su refinamiento común.

</details>

## 22.7. Un límite que todas las etiquetas deben compartir

[]{#MA-SEC-ANM-01-022-007}

Una función $f:[a,b]\to\mathbb R$ es **integrable de Riemann** si existe un real $I$ tal que

$$\forall\varepsilon>0\ \exists\delta>0\ \forall(P,\xi):
\quad \|P\|<\delta\ \Longrightarrow\ |S(f;P,\xi)-I|<\varepsilon.$$

El radio puede depender de $f,[a,b]$ y $\varepsilon$, pero se elige antes de la partición y de todas sus etiquetas. Denotamos ese real por $\int_a^b f(x)\,dx$. Es una definición mediante sumas finitas y tolerancias; la notación no afirma una antiderivada ni integra infinitesimales. Que se vea área en una figura es interpretación, no existencia automática.

Para probar unicidad, supongamos que dos reales $I,J$ cumplen el contrato y que $d=|I-J|>0$. Pedimos error menor que $d/3$ a ambos. La construcción de §22.3 permite tomar una partición uniforme con malla menor que los dos radios; fijamos en ella etiquetas explícitas. Su suma queda a distancia menor que $d/3$ de cada candidato. La triangular daría entonces $d<2d/3$, contradicción. La existencia de particiones pequeñas es esencial: permite usar las dos garantías sobre una misma suma.

Si un certificado demostrado tiene forma $|S-I|\le C\|P\|$ para todas las particiones y etiquetas, con $C\ge0$, la definición se cumple: para $C>0$ tomamos $\delta=\varepsilon/C$ y para $C=0$ cualquier radio positivo. Por la sección anterior, los escalones son integrables y su integral es $A$. La cota de diferencias en $k$ puntos prueba que cambiar valores finitos conserva cualquier integral existente: para $2kD>0$ escogemos además $\|P\|<\varepsilon/(4kD)$ y pedimos error $\varepsilon/2$ al original; los casos de constante cero se separan.

El límite de una selección de sumas es consecuencia, no sustituto del contrato. Si $\|P_r\|\to0$ y cada $\xi^{(r)}$ es una familia dada, integrabilidad implica $S(f;P_r,\xi^{(r)})\to I$: para un $\delta$ válido, las mallas eventualmente quedan por debajo. Observar sólo una familia de etiquetas o una cadena de refinamientos no controla las demás. En particular, contar piezas no demuestra ni siquiera que sus mallas tiendan a cero.

Estos certificados dan existencia para escalones y para las modificaciones finitas de una función ya integrable. Todavía falta un procedimiento que decida la integrabilidad de clases más amplias, como las funciones continuas. Las cotas inferiores y superiores de Darboux proporcionarán ese procedimiento en C23; la relación con la derivación requerirá después el teorema fundamental de C24.

![Para x en\[0,1\], todas las sumas cumplen |S−1/2|≤malla/2. Con tolerancia1/20, un radio1/10 sirve; se exige malla estrictamente menor. Las muestras sólo ilustran la banda universal demostrada.](../../assets/books/anm/C22/C22-F07.svg){#fig-anm-c22-f07 fig-alt="Para x en[0,1], todas las sumas cumplen |S−1/2|≤malla/2. Con tolerancia1/20, un radio1/10 sirve; se exige malla estrictamente menor. Las muestras sólo ilustran la banda universal demostrada."}

### Ejercicios de la sección 22.7

#### Ejercicio 31. El orden de los cuantificadores

[]{#MA-EX-ANM-01-022-031}

Escribe el contrato de integral y explica qué falla si el radio se permite depender de una partición ya elegida.

[]{#MA-SOL-ANM-01-022-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

El contrato pide un real $I$ tal que para cada $\varepsilon>0$ exista $\delta>0$ y para toda partición etiquetada con $\|P\|<\delta$ se cumpla $|S-I|<\varepsilon$. Si se permite elegir el radio después de una partición particular, puede tomarse $\delta\le\|P\|$ y dejar falsa la premisa de esa implicación. Ese truco no controla las particiones realmente finas. El radio debe responder a la tolerancia antes de examinar cualquier partición o etiqueta.

</details>

#### Ejercicio 32. Un valor único

[]{#MA-EX-ANM-01-022-032}

Demuestra unicidad del valor integral incluyendo una partición que satisfaga los dos radios.

[]{#MA-SOL-ANM-01-022-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Si $I\ne J$, fijamos $d=|I-J|>0$ y obtenemos radios para error $d/3$ de ambos contratos. Arquimedianidad da una uniforme de malla menor que su mínimo. Con etiquetas izquierdas explícitas, su suma $S$ cumple ambos errores. La triangular da $d\le|I-S|+|S-J|<2d/3$, contradicción. La partición construida muestra que la prueba aplica a una suma existente.

</details>

#### Ejercicio 33. Un radio efectivo

[]{#MA-EX-ANM-01-022-033}

Si todas las sumas cumplen $|S-I|\le5\|P\|$ en $[0,1]$, produce radio para tolerancia1/100 y número uniforme suficiente.

[]{#MA-SOL-ANM-01-022-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

La barrera cinco pide malla estrictamente menor que $(1/100)/5=1/500$. Por ello sirve radio $\delta=1/500$. Una uniforme de quinientas una piezas en $[0,1]$ tiene malla $1/501<\delta$ y garantiza el desafío. Con quinientas, la cota sólo daría error menor o igual que $1/100$, insuficiente para garantizar estrictitud.

**Retorno visual.** Véase [C22-F07](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Cambiar finitos valores

[]{#MA-EX-ANM-01-022-034}

Si $f$ es integrable y $g$ difiere sólo en $k$ puntos por diferencias≤$D$, demuestra misma integral.

[]{#MA-SOL-ANM-01-022-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Con los mismos datos, $|S_g-I|\le|S_g-S_f|+|S_f-I|$. Pedimos primero a la integrabilidad de $f$ un radio para error $\varepsilon/2$. Si $kD>0$, la cota de modificación finita queda menor que $\varepsilon/2$ al exigir además malla menor que $\varepsilon/(4kD)$. El mínimo de ambos radios protege cualquier suma de $g$. Si $kD=0$, las sumas coinciden y basta el primer radio. Así $g$ cumple el contrato con el mismo $I$.

</details>

#### Ejercicio 35. De universal a una sucesión

[]{#MA-EX-ANM-01-022-035}

Sea $\|P_r\|\to0$ con etiquetas dadas. Demuestra convergencia de las sumas si $f$ es integrable y distingue la recíproca no demostrada.

[]{#MA-SOL-ANM-01-022-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Para una tolerancia $\varepsilon$, el contrato universal entrega $\delta>0$. Como las mallas dadas tienden a cero, existe un índice $N$ desde el que todas son menores que $\delta$. Sus sumas, con las etiquetas dadas, cumplen entonces $|S_r-I|<\varepsilon$. Esto prueba convergencia a $I$. Una sola sucesión de datos no controla por ese argumento las otras particiones y etiquetas cuantificadas por el contrato.

</details>

## 22.8. Certificados antes de fórmulas de integración

[]{#MA-SEC-ANM-01-022-008}

Para $f(x)=x$ en $[a,b]$, el punto medio $m_i=(x_{i-1}+x_i)/2$ satisface

$$\sum_i m_i\Delta_i=\frac12\sum_i(x_i^2-x_{i-1}^2)=\frac{b^2-a^2}{2}.$$

Como $|\xi_i-m_i|\le\Delta_i/2$, cualquier suma etiquetada tiene error a lo sumo $(b-a)\|P\|/2$ respecto de ese número. Así queda probada su integral sin antiderivada. Para $\alpha x+\beta$, distributividad y telescopía producen valor $\alpha(b^2-a^2)/2+\beta(b-a)$ y cota $|\alpha|(b-a)\|P\|/2$.

Para $f(x)=x^2$ en $[0,1]$, pongamos $u=x_{i-1}$, $v=x_i$. La identidad del cubo da

$$\frac{v^3-u^3}{3}=(v-u)\frac{u^2+uv+v^2}{3}.$$

Como $0\le u\le\xi_i\le v\le1$, los números $u^2,uv,v^2$ y $\xi_i^2$ quedan entre $u^2$ y $v^2$. También la media de los tres primeros está en esa banda. La diferencia entre ella y $\xi_i^2$ tiene, por tanto, magnitud a lo sumo $v^2-u^2=(v-u)(v+u)\le2\Delta_i$. Al multiplicar por la anchura y sumar, los incrementos cúbicos de la identidad anterior telescopan y dejan $1/3$. Obtenemos

$$\left|S(x^2;P,\xi)-\frac13\right|\le2\sum_i\Delta_i^2\le2\|P\|.$$

Existe integral y vale $1/3$. No hemos usado una regla general de integrar potencias. En la partición uniforme, sumas izquierda/derecha dan valores exactos

$$\frac13-\frac1{2n}+\frac1{6n^2},\qquad
\frac13+\frac1{2n}+\frac1{6n^2}.$$

La identidad $\sum_{i=1}^n i^2=n(n+1)(2n+1)/6$ que los produce se demuestra por inducción: el caso1 es directo; añadir $(n+1)^2$ y factorizar da la expresión con $n+1$. Las copias reales de índices y $n>0$ preceden a estas divisiones. Para $n=4$ los valores son $7/32$ y $15/32$, alrededor de $1/3$. La suma media es $1/3-1/(12n^2)$; procede de expandir $(i-1/2)^2$ y sumar. Una etiqueta central no da exactitud cuadrática.

Para exigir error menor que $1/100$, la cota $2\|P\|$ pide malla menor que $1/200$. En la partición uniforme basta elegir $n>200$; cualquier otra partición con esa malla satisface la misma garantía, incluidas todas sus mezclas de etiquetas. Las fórmulas izquierda, derecha y media permiten comparar aproximaciones concretas, mientras el certificado universal es el que demuestra la existencia de la integral.

![Para x² en\[0,1\], sumas uniformes izquierda/media/derecha se acercan a1/3 por fórmulas finitas. Con n4 valen7/32,21/64,15/32; el certificado2·malla sirve para toda etiqueta, no sólo estas tres.](../../assets/books/anm/C22/C22-F08.svg){#fig-anm-c22-f08 fig-alt="Para x² en[0,1], sumas uniformes izquierda/media/derecha se acercan a1/3 por fórmulas finitas. Con n4 valen7/32,21/64,15/32; el certificado2·malla sirve para toda etiqueta, no sólo estas tres."}

### Ejercicios de la sección 22.8

#### Ejercicio 36. Una integral sin antiderivada

[]{#MA-EX-ANM-01-022-036}

Demuestra integral de $x$ en $[-1,2]$ usando puntos medios y da certificado.

[]{#MA-SOL-ANM-01-022-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

En cada pieza $[u,v]$, la contribución media de la identidad vale $(u+v)(v-u)/2=(v^2-u^2)/2$. La suma telescópica en $[-1,2]$ es $(4-1)/2=3/2$. Cualquier etiqueta dista del medio a lo sumo media anchura, así su error total no supera $(1/2)\sum_i\Delta_i^2\le(3/2)\|P\|$. Para una tolerancia $\varepsilon$ sirve radio $2\varepsilon/3$. El contrato prueba integral $3/2$ sin antiderivadas.

</details>

#### Ejercicio 37. Afín y firmada

[]{#MA-EX-ANM-01-022-037}

Calcula la integral de $2x-1$ en $[0,1]$ mediante sumas finitas y certificado.

[]{#MA-SOL-ANM-01-022-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

La linealidad finita da $S(2x-1)=2S(x)-1$ en $[0,1]$. El certificado de la identidad ofrece candidato $1/2$ y error a lo sumo $\|P\|/2$. Por tanto el nuevo candidato es cero y $|S(2x-1)|\le\|P\|$. El radio $\delta=\varepsilon$ satisface el contrato para todas las etiquetas. El valor cero representa una cancelación firmada de contribuciones.

</details>

#### Ejercicio 38. El cubo controla el cuadrado

[]{#MA-EX-ANM-01-022-038}

Prueba el certificado universal de $x^2$ en $[0,1]$ y su valor integral.

[]{#MA-SOL-ANM-01-022-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

En una pieza $[u,v]\subseteq[0,1]$, tanto $\xi^2$ como $(u^2+uv+v^2)/3$ quedan entre $u^2$ y $v^2$. Su diferencia de magnitudes no supera $v^2-u^2=(v-u)(v+u)\le2(v-u)$. Multiplicar por la anchura compara la contribución etiquetada con $(v^3-u^3)/3$ con error a lo sumo $2\Delta_i^2$. Los incrementos cúbicos telescopan a $1/3$ y la triangular da $|S-1/3|\le2\|P\|$. Para $\varepsilon>0$, el radio $\varepsilon/2$ prueba el contrato.

</details>

#### Ejercicio 39. Cuatro piezas no son el límite

[]{#MA-EX-ANM-01-022-039}

Calcula sumas izquierda, derecha y media de $x^2$ en uniforme de cuatro piezas, justificando las identidades de sumas.

[]{#MA-SOL-ANM-01-022-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Para cuatro piezas, las sumas de bordes son $(0+1+4+9)/64=7/32$ y $(1+4+9+16)/64=15/32$. Las medias producen $(1+9+25+49)/256=21/64$. Las identidades finitas $\sum_{i=1}^n i=n(n+1)/2$ y $\sum_{i=1}^n i^2=n(n+1)(2n+1)/6$ se prueban por inducción sumando el término siguiente. Sustituirlas da sumas izquierda $1/3-1/(2n)+1/(6n^2)$, derecha $1/3+1/(2n)+1/(6n^2)$ y media $1/3-1/(12n^2)$. En $n=4$ esta última difiere de $1/3$ en $1/192$. Las tres cuentas son sumas finitas y no el valor límite.

</details>

#### Ejercicio 40. Resolución de una tolerancia

[]{#MA-EX-ANM-01-022-040}

Elige una uniforme que certifique error de $x^2$ menor que1/100 para todas sus etiquetas; compara con el error de sus puntos medios.

[]{#MA-SOL-ANM-01-022-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La uniforme de doscientas una piezas tiene malla $1/201$. El certificado universal da error a lo sumo $2/201<1/100$ para cualquier etiqueta. Las medias de esa misma partición tienen error exacto $1/(12\cdot201^2)$, mucho menor. Esa mejora depende de usar las medias y no protege una familia arbitraria de etiquetas. La elección de resolución universal utiliza la barrera que sí cubre todas.

**Retorno visual.** Véase [C22-F08](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html#fig-anm-c22-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-22)

[← Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Capítulo 23 →](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html)
