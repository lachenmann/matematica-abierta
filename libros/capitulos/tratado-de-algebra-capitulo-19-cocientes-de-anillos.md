---
title: 'Tratado moderno de Álgebra — Capítulo 19: Cocientes de anillos'
description: Capítulo del Tratado moderno de Álgebra dedicado a cocientes de anillos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0044
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-16'
date-modified: '2026-09-27'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
prerequisites:
- MA-BCH-0043
related:
- MA-BOK-0007
- MA-BCH-0043
- MA-BCH-0045
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 19 — Cocientes de anillos

## 19.0. Propósito y posición deductiva

Un ideal bilateral no sólo aparece como núcleo de un homomorfismo: también determina exactamente la relación de congruencia necesaria para identificar elementos de un anillo sin destruir la suma ni el producto.

La cadena deductiva será

$$
\text{ideal bilateral }I\subseteq R
\longrightarrow
\equiv_I
\longrightarrow
R/I
\longrightarrow
\text{compatibilidad con }+
\longrightarrow
\text{compatibilidad con }\cdot
\longrightarrow
+_I,\cdot_I
\longrightarrow
\mathcal R/I\text{ anillo}
\longrightarrow
q_I:R\to R/I.
$$

La dificultad no está en escribir informalmente

$$
[a]_I+[b]_I=[a+b]_I,
\qquad
[a]_I\cdot[b]_I=[ab]_I,
$$

sino en probar primero que el resultado no depende de los representantes elegidos. En particular, la multiplicación requiere las dos absorciones que caracterizan a un ideal bilateral.

> **Contraste bibliográfico.** La arquitectura general se controla con Dummit–Foote (`BIB-TALG-0001`) y Lam (`BIB-TALG-0008`); el caso conmutativo se contrasta con Atiyah–Macdonald (`BIB-TALG-0007`). Las pruebas se desarrollan íntegramente dentro del tratado.

---

## 19.1. Congruencia módulo un ideal

### Definición 19.1.1 — Congruencia módulo un ideal bilateral {#talg-def-00042}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo y sea $I\subseteq R$ un ideal bilateral. Definimos una relación $\equiv_I$ sobre $R$ mediante

$$
a\equiv_I b
\quad\Longleftrightarrow\quad
a-b\in I.
$$

Equivalentemente,

$$
\equiv_I
:=
\{\langle a,b\rangle\in R\times R:a-b\in I\},
$$

que existe por Separación. Cuando sea conveniente escribiremos también

$$
a\equiv b\pmod I.
$$

En esta etapa la palabra *congruencia* nombra la relación definida; que sea una relación de equivalencia y que sea compatible con ambas operaciones se demostrará a continuación.

---

### Proposición 19.1.2 — La congruencia módulo $I$ es una relación de equivalencia {#talg-pro-00039}

Para todo ideal bilateral $I$ de $R$, la relación $\equiv_I$ es una relación de equivalencia sobre $R$.

#### Demostración {#talg-prf-00060}

Como $I$ determina un subgrupo del grupo aditivo de $R$, contiene $0$, es cerrado bajo suma y es cerrado bajo opuestos.

- **Reflexividad.** Para todo $a\in R$,
  $$
  a-a=0\in I,
  $$
  luego $a\equiv_I a$.

- **Simetría.** Si $a\equiv_I b$, entonces, por la [Definición 19.1.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042),
  $$
  a-b\in I.
  $$
  Como $I$ es cerrado bajo opuestos,
  $$
  -(a-b)\in I.
  $$
  En el grupo aditivo abeliano de $R$,
  $$
  \begin{aligned}
  -(a-b)
  &=-(a+(-b))\\
  &=(-a)+(-(-b))\\
  &=(-a)+b\\
  &=b+(-a)\\
  &=b-a,
  \end{aligned}
  $$
  usando las leyes de inversos, doble opuesto y conmutatividad de la suma. Sustituyendo en la pertenencia anterior,
  $$
  b-a\in I.
  $$
  Por la [Definición 19.1.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042),
  $$
  b\equiv_I a.
  $$

- **Transitividad.** Si $a\equiv_I b$ y $b\equiv_I c$, la [Definición 19.1.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042) proporciona
  $$
  a-b\in I,
  \qquad
  b-c\in I.
  $$
  Como $I$ es cerrado bajo suma,
  $$
  (a-b)+(b-c)\in I.
  $$
  Desarrollando las restas en el grupo aditivo y usando asociatividad, inverso y neutro,
  $$
  \begin{aligned}
  (a-b)+(b-c)
  &=(a+(-b))+(b+(-c))\\
  &=a+\bigl((-b)+b\bigr)+(-c)\\
  &=a+0+(-c)\\
  &=a+(-c)\\
  &=a-c.
  \end{aligned}
  $$
  Por sustitución en la pertenencia anterior,
  $$
  a-c\in I.
  $$
  De nuevo por la [Definición 19.1.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042),
  $$
  a\equiv_I c.
  $$

Por `TALG-IMP-00003`, $\equiv_I$ es una relación de equivalencia. $\square$

---

### Definición 19.1.3 — Conjunto cociente $R/I$ {#talg-def-00043}

Como $\equiv_I$ es una relación de equivalencia sobre $R$, definimos

$$
R/I
:=
R/{\equiv_I}.
$$

Por [`TALG-IMP-00003`](tratado-de-algebra-relaciones-equivalencia-cocientes.md#talg-imp-00003), este cociente existe como conjunto y satisface

$$
R/I\subseteq\mathcal P(R).
$$

Sus elementos son clases de equivalencia, no representantes individuales.

---

### Notación 19.1.4 — Clases módulo $I$ {#talg-not-00014}

Para $a\in R$ escribiremos

$$
[a]_I
:=
[a]_{\equiv_I}.
$$

La expresión $R/I$ seguirá denotando, hasta que se introduzcan y verifiquen las operaciones cociente, únicamente el conjunto de clases de equivalencia.

---

### Proposición 19.1.5 — Criterio de igualdad de clases módulo $I$ {#talg-pro-00040}

Para $a,b\in R$ son equivalentes:

$$
[a]_I=[b]_I,
\qquad
a\equiv_I b,
\qquad
a-b\in I.
$$

#### Demostración {#talg-prf-00061}

Por la [Definición 19.1.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042),

$$
a\equiv_I b
\quad\Longleftrightarrow\quad
a-b\in I.
$$

Por tanto, basta relacionar la congruencia con la igualdad de clases.

Supongamos primero

$$
a\equiv_I b.
$$

Para probar $[a]_I=[b]_I$ demostraremos ambas inclusiones.

Sea $x\in[a]_I$. Por la [Definición 19.1.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00043) de clase de equivalencia,

$$
x\equiv_I a.
$$

Junto con $a\equiv_I b$, la transitividad de $\equiv_I$, demostrada en la [Proposición 19.1.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00039), da

$$
x\equiv_I b.
$$

De nuevo por la [Definición 19.1.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00043),

$$
x\in[b]_I.
$$

Como $x\in[a]_I$ era arbitrario,

$$
[a]_I\subseteq[b]_I.
$$

Para la inclusión inversa, sea ahora $y\in[b]_I$. Por la [Definición 19.1.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00043),

$$
y\equiv_I b.
$$

La simetría de $a\equiv_I b$, establecida como parte de la [Proposición 19.1.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00039), proporciona

$$
b\equiv_I a.
$$

Aplicando transitividad a $y\equiv_I b$ y $b\equiv_I a$, obtenemos

$$
y\equiv_I a.
$$

Por la [Definición 19.1.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00043),

$$
y\in[a]_I.
$$

Como $y\in[b]_I$ era arbitrario,

$$
[b]_I\subseteq[a]_I.
$$

Las dos inclusiones y Extensionalidad implican

$$
[a]_I=[b]_I.
$$

Recíprocamente, si $[a]_I=[b]_I$, la reflexividad de $\equiv_I$ da $a\in[a]_I$. Por igualdad de clases,

$$
a\in[b]_I,
$$

lo que significa $a\equiv_I b$. $\square$

---

## 19.2. Compatibilidad con las operaciones del anillo

### Proposición 19.2.1 — Compatibilidad aditiva {#talg-pro-00041}

Si

$$
a\equiv_I a'
\qquad\text{y}\qquad
b\equiv_I b',
$$

entonces

$$
a+b\equiv_I a'+b'.
$$

Equivalentemente,

$$
[a]_I=[a']_I,
\quad
[b]_I=[b']_I
\quad\Longrightarrow\quad
[a+b]_I=[a'+b']_I.
$$

#### Demostración {#talg-prf-00062}

Por la [Definición 19.1.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042), las hipótesis

$$
a\equiv_I a'
\qquad\text{y}\qquad
b\equiv_I b'
$$

equivalen respectivamente a

$$
a-a'\in I,
\qquad
b-b'\in I.
$$

Como $I$ es un subgrupo del grupo aditivo de $R$, es cerrado bajo suma. Por tanto,

$$
(a-a')+(b-b')\in I.
$$

Desarrollando las restas,

$$
(a-a')+(b-b')
=
(a+(-a'))+(b+(-b')).
$$

Por asociatividad y conmutatividad de la suma,

$$
(a+(-a'))+(b+(-b'))
=
(a+b)+\bigl((-a')+(-b')\bigr).
$$

El elemento $(-a')+(-b')$ es el inverso aditivo de $a'+b'$. En efecto,

$$
\begin{aligned}
(a'+b')+\bigl((-a')+(-b')\bigr)
&=a'+b'+(-a')+(-b')\\
&=a'+(-a')+b'+(-b')\\
&=0+0\\
&=0,
\end{aligned}
$$

donde sólo hemos usado asociatividad y conmutatividad de la suma y las leyes de inverso. Como el grupo aditivo es abeliano, la misma igualdad vale también en el orden opuesto; por unicidad del inverso aditivo,

$$
(-a')+(-b')=-(a'+b').
$$

Sustituyendo,

$$
(a-a')+(b-b')
=
(a+b)+\bigl(-(a'+b')\bigr)
=
(a+b)-(a'+b').
$$

Como el miembro izquierdo pertenece a $I$, obtenemos

$$
(a+b)-(a'+b')\in I.
$$

Por la [Definición 19.1.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042),

$$
a+b\equiv_I a'+b'.
$$

Para la formulación mediante clases, supongamos

$$
[a]_I=[a']_I,
\qquad
[b]_I=[b']_I.
$$

La [Proposición 19.1.5](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00040) da

$$
a\equiv_I a',
\qquad
b\equiv_I b'.
$$

Por lo ya demostrado,

$$
a+b\equiv_I a'+b',
$$

y una nueva aplicación de la [Proposición 19.1.5](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00040) produce

$$
[a+b]_I=[a'+b']_I.
$$

$\square$

---

### Proposición 19.2.2 — Compatibilidad multiplicativa {#talg-pro-00042}

Si

$$
a\equiv_I a'
\qquad\text{y}\qquad
b\equiv_I b',
$$

entonces

$$
ab\equiv_I a'b'.
$$

Equivalentemente,

$$
[a]_I=[a']_I,
\quad
[b]_I=[b']_I
\quad\Longrightarrow\quad
[ab]_I=[a'b']_I.
$$

#### Demostración {#talg-prf-00063}

Tenemos

$$
a-a'\in I,
\qquad
b-b'\in I.
$$

Como $I$ es ideal bilateral,

$$
a(b-b')\in I
$$

por absorción izquierda, y

$$
(a-a')b'\in I
$$

por absorción derecha. Por cierre aditivo,

$$
a(b-b')+(a-a')b'\in I.
$$

Usando distributividad y las reglas del grupo aditivo,

$$
\begin{aligned}
a(b-b')+(a-a')b'
&=ab-ab'+ab'-a'b'\\
&=ab-a'b'.
\end{aligned}
$$

Por tanto,

$$
ab-a'b'\in I,
$$

es decir,

$$
ab\equiv_I a'b'.
$$

La formulación mediante clases sigue de la [Proposición 19.1.5](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00040). $\square$

> **Punto estructural.** La prueba utiliza los dos lados de la absorción: $a(b-b')$ exige absorción izquierda y $(a-a')b'$ exige absorción derecha. Éste es el lugar exacto donde un ideal meramente lateral deja de ser suficiente para construir, en general, el producto cociente.

---

### Lema 19.2.3 — Existencia y unicidad de las operaciones cociente {#talg-lem-00003}

Existen únicas funciones

$$
+_I:(R/I)\times(R/I)\to R/I
$$

y

$$
\cdot_I:(R/I)\times(R/I)\to R/I
$$

tales que, para todo $a,b\in R$,

$$
+_I(\langle[a]_I,[b]_I\rangle)=[a+b]_I
$$

y

$$
\cdot_I(\langle[a]_I,[b]_I\rangle)=[ab]_I.
$$

#### Demostración {#talg-prf-00064}

Sea

$$
D:=(R/I)\times(R/I).
$$

Por la [Definición 19.1.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00043) y la [Notación 19.1.4](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-not-00014), todo elemento de $R/I$ es una clase $[a]_I$ para algún $a\in R$. Por tanto, si

$$
\langle A,B\rangle\in D,
$$

existen $a,b\in R$ tales que

$$
A=[a]_I,
\qquad
B=[b]_I.
$$

La existencia de estos representantes se utilizará sólo localmente para la entrada fija $\langle A,B\rangle$.

**Construcción de la suma.** Consideremos el subconjunto

$$
\Gamma_+
\subseteq
D\times(R/I)
$$

definido por

$$
\left\langle\langle A,B\rangle,C\right\rangle\in\Gamma_+
$$

si y sólo si existen $a,b\in R$ tales que

$$
A=[a]_I,
\qquad
B=[b]_I,
\qquad
C=[a+b]_I.
$$

El producto cartesiano $D\times(R/I)$ existe por la interfaz conjuntista `TALG-IMP-00001`, y $\Gamma_+$ existe por Separación.

Fijemos $\langle A,B\rangle\in D$. Elijamos localmente representantes $a,b\in R$ con

$$
A=[a]_I,
\qquad
B=[b]_I.
$$

Entonces

$$
C:=[a+b]_I
$$

pertenece a $R/I$ y satisface

$$
\left\langle\langle A,B\rangle,C\right\rangle\in\Gamma_+.
$$

Así, para cada entrada existe al menos una salida.

Para demostrar que la salida es independiente de los representantes, supongamos que también

$$
A=[a']_I,
\qquad
B=[b']_I.
$$

Entonces

$$
[a]_I=[a']_I,
\qquad
[b]_I=[b']_I.
$$

La formulación en clases de la [Proposición 19.2.1](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00041) proporciona

$$
[a+b]_I=[a'+b']_I.
$$

Por consiguiente, dos pares de representantes de la misma entrada producen la misma clase de salida. Esto demuestra que para cada $\langle A,B\rangle\in D$ existe un único $C\in R/I$ con

$$
\left\langle\langle A,B\rangle,C\right\rangle\in\Gamma_+.
$$

Por tanto, $\Gamma_+$ es el grafo de una función

$$
+_I:D\to R/I
$$

que satisface, para todos $a,b\in R$,

$$
+_I(\langle[a]_I,[b]_I\rangle)=[a+b]_I.
$$

Falta justificar la unicidad de la función con esta propiedad. Sea

$$
\oplus:D\to R/I
$$

otra función que satisfaga la misma fórmula para todos los representantes. Dada una entrada arbitraria $\langle A,B\rangle\in D$, tomamos localmente $a,b\in R$ con $A=[a]_I$ y $B=[b]_I$. Entonces

$$
\oplus(\langle A,B\rangle)
=
[a+b]_I
=
+_I(\langle A,B\rangle).
$$

Como ambas funciones tienen el mismo dominio, el mismo codominio y coinciden en toda entrada, son iguales. La función $+_I$ es única.

**Construcción del producto.** Definimos ahora

$$
\Gamma_{\cdot}
\subseteq
D\times(R/I)
$$

mediante la condición

$$
\left\langle\langle A,B\rangle,C\right\rangle\in\Gamma_{\cdot}
$$

si y sólo si existen $a,b\in R$ tales que

$$
A=[a]_I,
\qquad
B=[b]_I,
\qquad
C=[ab]_I.
$$

El conjunto $\Gamma_{\cdot}$ existe por Separación dentro de $D\times(R/I)$.

Fijemos de nuevo una entrada $\langle A,B\rangle\in D$ y representantes locales $a,b\in R$ con

$$
A=[a]_I,
\qquad
B=[b]_I.
$$

La clase

$$
C:=[ab]_I
$$

pertenece a $R/I$, de modo que existe al menos una salida para esa entrada.

Supongamos que $a',b'\in R$ son otros representantes de las mismas clases:

$$
A=[a']_I,
\qquad
B=[b']_I.
$$

Entonces

$$
[a]_I=[a']_I,
\qquad
[b]_I=[b']_I.
$$

La formulación en clases de la [Proposición 19.2.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00042) da exactamente

$$
[ab]_I=[a'b']_I.
$$

Por tanto, la clase producto no depende de los representantes elegidos. En consecuencia, para cada $\langle A,B\rangle\in D$ existe un único $C\in R/I$ tal que

$$
\left\langle\langle A,B\rangle,C\right\rangle\in\Gamma_{\cdot}.
$$

Así, $\Gamma_{\cdot}$ es el grafo de una función

$$
\cdot_I:D\to R/I
$$

que satisface

$$
\cdot_I(\langle[a]_I,[b]_I\rangle)=[ab]_I
$$

para todos $a,b\in R$.

Finalmente, sea

$$
\odot:D\to R/I
$$

otra función con esa misma propiedad. Para una entrada arbitraria $\langle A,B\rangle\in D$, elegimos localmente representantes $a,b\in R$. Entonces

$$
\odot(\langle A,B\rangle)
=
[ab]_I
=
\cdot_I(\langle A,B\rangle).
$$

Las dos funciones coinciden en toda entrada y tienen el mismo dominio y codominio; por tanto, son iguales. La función $\cdot_I$ es única.

En ninguna de las dos construcciones se ha elegido globalmente un sistema de representantes. Sólo se eliminan existenciales localmente para una entrada ya fijada, y las Proposiciones 19.2.1 y 19.2.2 garantizan que el valor obtenido es independiente de esa elección local. $\square$

---

### Notación 19.2.4 — Operaciones cociente {#talg-not-00015}

Escribiremos

$$
[a]_I+_I[b]_I=[a+b]_I,
$$

$$
[a]_I\cdot_I[b]_I=[ab]_I.
$$

Estas expresiones ya denotan operaciones binarias genuinas sobre $R/I$ por el [Lema 19.2.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-lem-00003).

---

## 19.3. El anillo cociente

### Definición 19.3.1 — Estructura cociente asociada a un ideal {#talg-def-00044}

Definimos la estructura

$$
\mathcal R/I
:=
\langle R/I,+_I,\cdot_I\rangle.
$$

Por ahora se trata de una estructura con dos operaciones binarias bien definidas. Que satisfaga los axiomas de anillo se demuestra en el siguiente teorema.

---

### Teorema 19.3.2 — El cociente por un ideal bilateral es un anillo {#talg-thm-00011}

La estructura

$$
\mathcal R/I=\langle R/I,+_I,\cdot_I\rangle
$$

es un anillo. Además,

$$
0_{\mathcal R/I}=[0_{\mathcal R}]_I,
\qquad
1_{\mathcal R/I}=[1_{\mathcal R}]_I,
$$

y el opuesto aditivo de $[a]_I$ es $[-a]_I$.

#### Demostración {#talg-prf-00065}

Sean $[a]_I,[b]_I,[c]_I\in R/I$. Todas las operaciones que aparecen a continuación están bien definidas por el [Lema 19.2.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-lem-00003).

Para la suma,

$$
\begin{aligned}
([a]_I+_I[b]_I)+_I[c]_I
&=[(a+b)+c]_I\\
&=[a+(b+c)]_I\\
&=[a]_I+_I([b]_I+_I[c]_I),
\end{aligned}
$$

así que $+_I$ es asociativa. Asimismo,

$$
[a]_I+_I[0]_I=[a+0]_I=[a]_I,
$$

$$
[0]_I+_I[a]_I=[0+a]_I=[a]_I,
$$

por lo que $[0]_I$ es el neutro aditivo.

Para verificar que $[-a]_I$ es el inverso aditivo de $[a]_I$ debemos comprobar las dos identidades exigidas en el grupo aditivo. Por la definición de la operación cociente, fijada en la [Notación 19.2.4](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-not-00015),

$$
\begin{aligned}
[a]_I+_I[-a]_I
&=[a+(-a)]_I\\
&=[0]_I,
\end{aligned}
$$

porque $a+(-a)=0$ en el grupo aditivo del anillo. En el orden opuesto, usando la misma operación cociente pero ahora la igualdad $(-a)+a=0$,

$$
\begin{aligned}
[-a]_I+_I[a]_I
&=[(-a)+a]_I\\
&=[0]_I.
\end{aligned}
$$

Así, $[-a]_I$ es simultáneamente inverso aditivo por la derecha y por la izquierda de $[a]_I$. Por tanto, es su inverso aditivo bilateral en $R/I$. Finalmente,

$$
[a]_I+_I[b]_I=[a+b]_I=[b+a]_I=[b]_I+_I[a]_I,
$$

de modo que el grupo aditivo es abeliano.

Para la multiplicación,

$$
\begin{aligned}
([a]_I\cdot_I[b]_I)\cdot_I[c]_I
&=[(ab)c]_I\\
&=[a(bc)]_I\\
&=[a]_I\cdot_I([b]_I\cdot_I[c]_I),
\end{aligned}
$$

por asociatividad en $R$. Además,

$$
[a]_I\cdot_I[1]_I=[a1]_I=[a]_I,
$$

$$
[1]_I\cdot_I[a]_I=[1a]_I=[a]_I,
$$

por lo que $[1]_I$ es neutro multiplicativo.

Las distributividades descienden del anillo ambiente:

$$
\begin{aligned}
[a]_I\cdot_I([b]_I+_I[c]_I)
&=[a(b+c)]_I\\
&=[ab+ac]_I\\
&=[ab]_I+_I[ac]_I\\
&=([a]_I\cdot_I[b]_I)+_I([a]_I\cdot_I[c]_I),
\end{aligned}
$$

mientras que

$$
\begin{aligned}
([a]_I+_I[b]_I)\cdot_I[c]_I
&=[(a+b)c]_I\\
&=[ac+bc]_I\\
&=[ac]_I+_I[bc]_I\\
&=([a]_I\cdot_I[c]_I)+_I([b]_I\cdot_I[c]_I).
\end{aligned}
$$

Se cumplen así todos los axiomas de la [Definición 14.1.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00032). La identificación del cero, de la unidad y de los opuestos ya quedó exhibida en la prueba. $\square$

---

### Proposición 19.3.3 — No trivialidad del cociente e ideal propio {#talg-pro-00043}

El anillo cociente $\mathcal R/I$ es no trivial si y sólo si $I$ es un ideal propio de $R$:

$$
\boxed{
0_{\mathcal R/I}\neq1_{\mathcal R/I}
\quad\Longleftrightarrow\quad
I\neq R.
}
$$

#### Demostración {#talg-prf-00066}

Por el [Teorema 19.3.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-thm-00011),

$$
0_{\mathcal R/I}=[0]_I,
\qquad
1_{\mathcal R/I}=[1]_I.
$$

Por la [Proposición 19.1.5](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00040),

$$
[1]_I=[0]_I
\iff
1-0\in I
\iff
1\in I.
$$

Por el [Teorema 18.1.3](tratado-de-algebra-capitulo-18-ideales.md#talg-thm-00010),

$$
1\in I
\iff
I=R.
$$

Negando ambos lados de la equivalencia obtenemos

$$
[0]_I\neq[1]_I
\iff
I\neq R.
$$

Por la [Definición 16.1.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00035) y la [Definición 18.1.4](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00041), esto equivale exactamente a la afirmación del enunciado. $\square$

---

### Proposición 19.3.4 — La conmutatividad desciende al cociente {#talg-pro-00044}

Si $\mathcal R$ es un anillo conmutativo, entonces $\mathcal R/I$ es un anillo conmutativo.

#### Demostración {#talg-prf-00067}

Para $[a]_I,[b]_I\in R/I$,

$$
[a]_I\cdot_I[b]_I
=[ab]_I
=[ba]_I
=[b]_I\cdot_I[a]_I,
$$

porque $ab=ba$ en $R$. Por la [Definición 14.5.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00033), el cociente es conmutativo. $\square$

---

## 19.4. Proyección canónica

### Definición 19.4.1 — Proyección canónica al cociente {#talg-def-00045}

Definimos la función

$$
q_I:R\to R/I,
\qquad
q_I(a):=[a]_I.
$$

Conjuntistamente, su grafo es

$$
\{\langle a,C\rangle\in R\times(R/I):C=[a]_I\},
$$

que existe por Separación. Para cada $a\in R$ existe una única clase $[a]_I$, por lo que este grafo determina una función con dominio $R$ y codominio $R/I$.

---

### Proposición 19.4.2 — La proyección canónica es sobreyectiva, homomórfica y tiene núcleo $I$ {#talg-pro-00045}

La función

$$
q_I:R\to R/I
$$

es un homomorfismo de anillos sobreyectivo y

$$
\boxed{\ker q_I=I.}
$$

#### Demostración {#talg-prf-00068}

Para $a,b\in R$,

$$
q_I(a+b)
=[a+b]_I
=[a]_I+_I[b]_I
=q_I(a)+_Iq_I(b),
$$

$$
q_I(ab)
=[ab]_I
=[a]_I\cdot_I[b]_I
=q_I(a)\cdot_Iq_I(b),
$$

y, por el [Teorema 19.3.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-thm-00011),

$$
q_I(1_R)=[1_R]_I=1_{\mathcal R/I}.
$$

Por la [Definición 17.2.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00039), $q_I$ es un homomorfismo de anillos.

Sea ahora $C\in R/I$. Por definición del cociente existe $a\in R$ tal que

$$
C=[a]_I.
$$

Entonces $q_I(a)=C$. Así, $q_I$ es sobreyectiva en el sentido importado por [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002). No se requiere una elección simultánea de representantes.

Finalmente, considerando $q_I$ como homomorfismo de los grupos aditivos,

$$
\begin{aligned}
a\in\ker q_I
&\iff q_I(a)=0_{\mathcal R/I}\\
&\iff [a]_I=[0]_I\\
&\iff a-0\in I\\
&\iff a\in I,
\end{aligned}
$$

usando la [Proposición 19.1.5](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00040). Por Extensionalidad,

$$
\ker q_I=I.
$$

$\square$

---

### Corolario 19.4.3 — Todo ideal bilateral es núcleo de un homomorfismo sobreyectivo {#talg-cor-00010}

Sea $I$ un ideal bilateral de $R$. Entonces existe un homomorfismo de anillos sobreyectivo

$$
q_I:R\to R/I
$$

tal que

$$
\ker q_I=I.
$$

Si además $I$ es propio, el codominio $\mathcal R/I$ es no trivial.

#### Demostración {#talg-prf-00069}

La primera afirmación es exactamente la [Proposición 19.4.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00045). Si $I$ es propio, la [Proposición 19.3.3](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00043) implica que $\mathcal R/I$ es no trivial. $\square$

---

## 19.5. Cierre deductivo

Queda cerrada la cadena

```text
ideal bilateral I
      ↓
congruencia a ≡ b (mod I)
      ↓
relación de equivalencia
      ↓
R/I como conjunto de clases
      ↓
compatibilidad aditiva
+
compatibilidad multiplicativa
      ↓
+_I y ·_I bien definidas
      ↓
anillo cociente R/I
      ↓
I propio ↔ R/I no trivial
      ↓
proyección q_I:R→R/I
      ↓
q_I sobreyectiva, ker q_I = I
```

No se ha utilizado el axioma de elección. No se ha importado ningún teorema general de descenso a cocientes: la buena definición de ambas operaciones fue demostrada directamente.

El siguiente nodo canónico será

[Definición 20.1.1 — Isomorfismo de anillos](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-def-00046).

---

[← **Capítulo 18 — Ideales**](tratado-de-algebra-capitulo-18-ideales.md) · [**Capítulo 20 — Isomorfismos y primer teorema de isomorfía para anillos** →](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md)
