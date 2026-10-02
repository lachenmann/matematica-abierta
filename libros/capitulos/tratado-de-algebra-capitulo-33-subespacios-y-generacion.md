---
title: 'Tratado moderno de Álgebra — Capítulo 33: Subespacios y generación'
description: Criterio de subespacio, sumas finitas y construcción del subespacio generado, con sus propiedades de minimalidad, intersección y suma.
author: Gustav A. Tachek
content-id: MA-BCH-0141
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-10-02'
date-modified: '2026-10-02'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- espacios-vectoriales
- subespacios
- combinaciones-lineales
- generacion
- sumas-finitas
prerequisites:
- MA-BCH-0140
- MA-BCH-0030
- MA-BCH-0136
related:
- MA-BOK-0007
- MA-BCH-0140
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 33 — Subespacios y generación

## 33.0. Propósito y posición deductiva

Una subestructura vectorial debe conservar suma y acción escalar. Se construye la generación mediante combinaciones finitas, sin presuponer bases. Las sumas se definen mediante la [recursión natural](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006), y su independencia del orden se prueba antes de emplear conjuntos finitos sin enumeración distinguida.

El desarrollo parte de la [definición de espacio vectorial](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-def-00070), sus [identidades escalares](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-pro-00107) y el [criterio de subgrupo habitado](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004). Primero se certifican las estructuras restringidas; después se construyen las sumas finitas y el subespacio generado, y se prueban sus propiedades de minimalidad, intersección y suma.

El marco fundacional es ZF con lógica clásica. Las enumeraciones y las representaciones se utilizan como testigos locales, sin el axioma de elección. Los casos clásicos empleados al eliminar repeticiones se explicitan en la prueba del [Lema 33.3.1](#talg-lem-00008).

---

## 33.1. Subespacio vectorial

### Definición 33.1.1 — Subespacio vectorial {#talg-def-00071}

Sea $V$ [espacio vectorial](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-def-00070) sobre $F$. Un **subespacio** es un subconjunto $U\subseteq V$ tal que, con las operaciones restringidas de $V$ y la acción restringida $F\times U\to U$, $U$ es espacio vectorial sobre el mismo cuerpo. El cero y la suma no se redefinen independientemente de $V$. Escribimos $U\le V$ en esta parte; la notación indica subespacio, no un orden entre vectores.

## 33.2. Criterio de subespacio

### Proposición 33.2.1 — Criterio de subespacio {#talg-pro-00109}

Un subconjunto $U\subseteq V$ es [subespacio](#talg-def-00071) si y sólo si
$$
0_V\in U,\qquad
u+v\in U\ (u,v\in U),\qquad au\in U\ (a\in F,u\in U).
$$
Puede sustituirse el cierre por suma por el cierre por diferencias $u-v$.

#### Demostración {#talg-prf-00171}

Si $U$ es subespacio, sus operaciones restringidas están cerradas. Además $U$ está habitado, por ser grupo aditivo; para un vector $u\in U$, el cierre escalar y $0_Fu=0_V$ dan $0_V\in U$. El cierre por suma y escalares es parte de la restricción vectorial.

A la inversa, supongamos las tres condiciones. El cero es un testigo en $U$. Para $u,v\in U$, $-v=(-1_F)v\in U$ por cierre escalar y la [identidad de opuestos](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md#talg-pro-00107); así $u-v=u+(-v)\in U$. El [criterio de subgrupo habitado](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) prueba que $U$ es subgrupo del grupo aditivo de $V$. La suma restringida hereda conmutatividad de $V$, y la acción restringida existe por el cierre escalar. Para $a,b\in F$, $u,v\in U$, las cuatro igualdades vectoriales en $V$ tienen ambos lados en $U$; por tanto son igualdades de las operaciones restringidas. Así $U$ es espacio vectorial sobre $F$.

Si se supone cierre por diferencias, el testigo $0_V\in U$ da $-v=0_V-v\in U$, y luego $u+v=u-(-v)\in U$. Si se supone cierre por suma y escalares, el argumento anterior da diferencias. Quedan probadas las dos formulaciones. $\square$

## 33.3. Sumas finitas e independencia de enumeración

### Lema 33.3.1 — Sumas finitas e independencia de enumeración {#talg-lem-00008}

Para una lista $(v_0,\ldots,v_{n-1})$ de vectores, la suma finita existe y está determinada recursivamente por $S_0=0_V$, $S_{k+1}=S_k+v_k$. La suma de dos listas concatenadas es la suma de sus sumas; las sumas término a término y la acción escalar satisfacen
$$
\sum_{i<n}(u_i+v_i)=\sum_{i<n}u_i+\sum_{i<n}v_i,\qquad
a\sum_{i<n}v_i=\sum_{i<n}av_i.
$$
La suma es invariante bajo permutaciones. Por tanto, para un conjunto finito $E$ y una familia $(v_e)_{e\in E}$, $\sum_{e\in E}v_e$ es independiente de la enumeración biyectiva de $E$. Las combinaciones finitas pueden reagruparse, juntar coeficientes repetidos y añadir o retirar términos de coeficiente cero.

#### Demostración {#talg-prf-00172}

**Existencia recursiva.** Para una lista de longitud $n$, extiéndase a una función sobre $\mathbb N$ dando el valor $0_V$ fuera de sus índices. La [recursión con parámetros](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006) produce los valores $S_k$ y su unicidad; $S_n$ define la suma. La extensión es única, sin elección.

**Concatenación.** Para listas $u$ de longitud $m$ y $v$ de longitud $n$, inducción sobre $k\le n$ prueba que la suma de los primeros $m+k$ términos concatenados es $S_m(u)+S_k(v)$. En $k=0$, se usa el neutro. El paso da $(S_m(u)+S_k(v))+v_k=S_m(u)+(S_k(v)+v_k)$ por asociatividad. Con $k=n$ queda la fórmula.

**Suma término a término y escalares.** En longitud cero, ambas identidades se reducen a $0+0=0$ y $a0=0$. Supuesto el resultado para $k$, el siguiente término de la primera suma es
$$
(S_k(u)+S_k(v))+(u_k+v_k)
=(S_k(u)+u_k)+(S_k(v)+v_k),
$$
por asociatividad y conmutatividad. En la segunda, $a(S_k(v)+v_k)=aS_k(v)+av_k$, y la hipótesis inductiva concluye el paso.

**Permutaciones.** Una transposición de dos términos adyacentes conserva la suma: la concatenación divide la lista en prefijo, los dos términos y sufijo; se usa $x+y=y+x$ en el bloque central y asociatividad al recomponer. Para cualquier permutación de una lista de longitud $n+1$, localicemos el término que debe ir primero y movámoslo a la primera posición mediante un número finito de transposiciones adyacentes. Cada movimiento conserva la suma. Los $n$ términos restantes pueden ordenarse como exige la permutación por la hipótesis inductiva. La lista vacía inicia la inducción. Esto prueba invariancia bajo cualquier permutación finita.

Dos enumeraciones biyectivas de un mismo conjunto finito se relacionan por la permutación obtenida componiendo una con la inversa de la otra; por tanto sus sumas coinciden. La suma del conjunto finito es así un valor único. La construcción por unicidad no escoge una enumeración para cada conjunto.

**Reagrupamiento.** Al reordenar una lista de términos $a_iv_i$, los términos con un mismo vector pueden hacerse contiguos. La distributividad $(a+b)v=av+bv$ permite reemplazar cada bloque por un término con la suma de sus coeficientes; inducción en la longitud del bloque prueba la afirmación. Un término $0_Fv$ es $0_V$, por lo que puede retirarse o añadirse. Para una lista finita, la eliminación de repeticiones se justifica inductivamente separando las alternativas clásicas «el nuevo elemento coincide con uno anterior» o «no coincide». Esto también prueba que el conjunto de elementos de una lista es finito y que la unión de dos conjuntos finitos es finita: se concatenan sus enumeraciones y se eliminan repeticiones. La prueba no afirma un procedimiento efectivo de igualdad en $V$ o $F$. $\square$

## 33.4. Combinación lineal y subespacio generado

### Definición 33.4.1 — Combinación lineal y subespacio generado {#talg-def-00072}

Una **combinación lineal finita** de vectores de $A\subseteq V$ es un vector de la forma
$$
\sum_{i<n}a_iv_i,\qquad n\in\mathbb N,\quad a_i\in F,\quad v_i\in A.
$$
La combinación vacía tiene valor $0_V$. Definimos
$$
\operatorname{span}_F(A)=
\left\{v\in V:\exists n,\exists(a_i)_{i<n},\exists(v_i)_{i<n},
\ v=\sum_{i<n}a_iv_i,\ a_i\in F,\ v_i\in A\right\}.
$$
El conjunto existe por Separación en $V$, usando la [recursión finita cerrada](#talg-lem-00008). Se llama **subespacio generado** por $A$; la certificación de que es subespacio se da en el [siguiente resultado](#talg-pro-00110). Decimos que $A$ **genera** $V$ si $\operatorname{span}_F(A)=V$. Para una lista o familia, «generar» se refiere a su conjunto imagen. No se exige una representación única ni se selecciona una representación para cada vector.

## 33.5. Generación, intersecciones y sumas de subespacios

### Proposición 33.5.1 — Generación, intersecciones y sumas de subespacios {#talg-pro-00110}

El span de $A$ es el menor subespacio de $V$ que contiene $A$:
$$
A\subseteq\operatorname{span}(A),\qquad
A\subseteq U\le V\Longrightarrow\operatorname{span}(A)\subseteq U.
$$
Además $\operatorname{span}(\varnothing)=\{0_V\}$ y $A\subseteq B$ implica $\operatorname{span}(A)\subseteq\operatorname{span}(B)$.

La intersección de cualquier familia de subespacios es subespacio; la intersección de la familia vacía se define como $V$. Para $U,W\le V$,
$$
U+W=\{u+w:u\in U,w\in W\}
$$
es el menor subespacio que contiene a ambos y
$$
\operatorname{span}(A\cup B)=\operatorname{span}(A)+\operatorname{span}(B).
$$

#### Demostración {#talg-prf-00173}

**Span.** La combinación vacía muestra $0_V\in\operatorname{span}(A)$. Si $x=\sum_{i<m}a_iu_i$ y $y=\sum_{j<n}b_jv_j$, concatenar las listas da una combinación de $A$ con valor $x+y$. Si $c\in F$, la [distributividad finita](#talg-lem-00008) da $cx=\sum_{i<m}(ca_i)u_i$. El [criterio de subespacio](#talg-pro-00109) certifica el span. Para $a\in A$, la lista de un término $1_Fa=a$ muestra que contiene $A$. Si $A\subseteq U\le V$, cada término $a_iv_i$ está en $U$; por inducción, la suma finita también está en $U$, incluyendo la vacía. Esto prueba minimalidad.

Si $A=\varnothing$, sólo es posible una lista de longitud cero con términos en $A$: una longitud positiva tendría un primer término perteneciente al conjunto vacío. Por tanto el span es exactamente $\{0_V\}$. Si $A\subseteq B$, cualquier combinación con términos en $A$ también tiene términos en $B$, lo que prueba monotonía.

**Intersecciones.** Para una familia $(U_i)_{i\in I}$, la intersección es $\{v\in V:\forall i\in I,\ v\in U_i\}$, existente por Separación. Cada $U_i$ contiene cero; si $u,v$ están en todos ellos, $u+v$ y $au$ también lo están. El [criterio de subespacio](#talg-pro-00109) certifica la intersección. Para $I=\varnothing$, la condición universal es vacua y el conjunto es $V$.

**Sumas.** El conjunto $U+W$ existe por Separación en $V$ con testigos $u,w$. Contiene $0_V=0_V+0_V$. Si $x=u+w$, $y=u'+w'$, la [ley de reordenación finita](#talg-lem-00008) da
$$
x+y=(u+u')+(w+w')\in U+W.
$$
La acción da $ax=au+aw\in U+W$. Es subespacio. Contiene $U$ mediante $u=u+0_V$ y $W$ mediante $w=0_V+w$. Si un subespacio $T$ contiene ambos, para $u\in U$, $w\in W$ su cierre aditivo da $u+w\in T$. Por tanto es el menor.

Finalmente, $\operatorname{span}(A)+\operatorname{span}(B)$ es subespacio y contiene $A\cup B$, luego contiene su span. Por monotonía, ambos spans están contenidos en $\operatorname{span}(A\cup B)$, y el cierre por suma da la inclusión recíproca. Extensionalidad concluye la igualdad. Todos los testigos de combinaciones y descomposiciones se utilizan localmente. $\square$

---

## 33.99. Síntesis

Las subestructuras vectoriales conservan simultáneamente suma y acción. La generación ofrece representaciones finitas, sin prometer unicidad: esa diferencia prepara la independencia y las bases. La propiedad mínima permite controlar inclusiones y sumas sin elegir representaciones simultáneamente.

---

[← **Capítulo 32 — Espacios vectoriales: definición y ejemplos**](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)
