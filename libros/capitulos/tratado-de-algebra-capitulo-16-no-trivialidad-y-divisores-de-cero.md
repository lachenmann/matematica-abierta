---
title: 'Tratado moderno de Álgebra — Capítulo 16: No trivialidad y divisores de cero'
description: Capítulo del Tratado moderno de Álgebra dedicado a no trivialidad y divisores de cero, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0041
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-16'
date-modified: '2026-09-16'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- algebra
- estructuras-algebraicas
prerequisites:
- MA-BCH-0040
related:
- MA-BOK-0007
- MA-BCH-0040
- MA-BCH-0042
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 16 — No trivialidad y divisores de cero

## 16.0. Propósito y convención lateral

La definición general de anillo adoptada en la [Definición 14.1.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00032) admite el caso $0=1$. Esa amplitud era útil mientras se construían las leyes básicas y el grupo de unidades, pero la teoría de divisores de cero necesita separar explícitamente el caso trivial.

Además, en un anillo no conmutativo las ecuaciones

$$
ab=0
\qquad\text{y}\qquad
ba=0
$$

no son intercambiables. Por ello, este tratado distinguirá **divisores de cero por la izquierda** y **por la derecha** antes de introducir la terminología sin calificativo en el caso conmutativo.

La convención lateral será literal: un elemento será divisor de cero **por la izquierda** cuando aparezca como factor izquierdo de un producto nulo con otro factor no nulo; será divisor de cero **por la derecha** cuando aparezca como factor derecho.

> **Contraste bibliográfico.** La distinción lateral y la teoría general de anillos se controlan principalmente con Lam (`BIB-TALG-0008`) y Dummit–Foote (`BIB-TALG-0001`). Para la especialización conmutativa se usa también Atiyah–Macdonald (`BIB-TALG-0007`). Las fuentes cumplen funciones de contraste y terminología; las pruebas se desarrollan dentro del tratado.

---

## 16.1. Anillos no triviales

### Definición 16.1.1 — Anillo no trivial {#talg-def-00035}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo. Se dice que $\mathcal R$ es **no trivial** si

$$
\boxed{0\neq1}.
$$

Si $0=1$, se dice que el anillo es **trivial**.

La no trivialidad no modifica las operaciones ni añade estructura: es una propiedad del anillo ya construido.

---

### Corolario 16.1.2 — No trivialidad e invertibilidad del cero {#talg-cor-00005}

Para todo anillo $\mathcal R$,

$$
\boxed{
\mathcal R\text{ es no trivial}
\quad\Longleftrightarrow\quad
0\notin R^\times
}.
$$

#### Demostración {#talg-prf-00042}

Por la [Proposición 15.6.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00028),

$$
0\in R^\times\quad\Longleftrightarrow\quad0=1.
$$

Negando ambos lados y usando la [Definición 16.1.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00035), obtenemos

$$
0\notin R^\times\quad\Longleftrightarrow\quad0\neq1,
$$

que es exactamente la afirmación.

$\square$

---

## 16.2. Divisores de cero laterales

### Definición 16.2.1 — Divisores de cero por la izquierda, por la derecha y bilaterales {#talg-def-00036}

Sea $\mathcal R$ un anillo no trivial y sea $a\in R$ con $a\neq0$.

1. $a$ es un **divisor de cero por la izquierda** si existe $b\in R$ tal que
   $$
   b\neq0
   \qquad\text{y}\qquad
   ab=0.
   $$
2. $a$ es un **divisor de cero por la derecha** si existe $b\in R$ tal que
   $$
   b\neq0
   \qquad\text{y}\qquad
   ba=0.
   $$
3. $a$ es un **divisor de cero bilateral** si es simultáneamente divisor de cero por la izquierda y por la derecha.

En este tratado no se usará sin calificación la expresión “divisor de cero” para un anillo general no conmutativo. La lateralidad forma parte de la información matemática.

> **Convención.** El propio elemento $a$ se exige no nulo, y el factor testigo $b$ también. Así, el cero no es divisor de cero por definición.

---

## 16.3. Las unidades no son divisores de cero

### Proposición 16.3.1 — Una unidad no puede ser divisor de cero lateral {#talg-pro-00029}

Sea $\mathcal R$ un anillo no trivial y sea $u\in R^\times$. Entonces $u$ no es divisor de cero por la izquierda ni por la derecha.

#### Demostración {#talg-prf-00043}

Supongamos que

$$
ub=0
$$

para algún $b\in R$. Multiplicando por $u^{-1}$ a la izquierda y usando asociatividad,

$$
u^{-1}(ub)=(u^{-1}u)b=1b=b.
$$

Por otro lado, la [Proposición 14.3.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00024) da

$$
u^{-1}0=0.
$$

Por tanto $b=0$. No existe, pues, un $b\neq0$ con $ub=0$, y $u$ no es divisor de cero por la izquierda.

Análogamente, si

$$
bu=0,
$$

multiplicando por $u^{-1}$ a la derecha se obtiene

$$
(bu)u^{-1}=b(uu^{-1})=b1=b,
$$

mientras que $0u^{-1}=0$. Luego $b=0$, y $u$ tampoco es divisor de cero por la derecha.

$\square$

> **Importante.** No se afirma el recíproco. “No ser divisor de cero” y “ser unidad” son propiedades distintas.

---

## 16.4. Divisores de cero y cancelación

### Teorema 16.4.1 — Caracterización lateral por cancelación {#talg-thm-00008}

Sea $\mathcal R$ un anillo no trivial y sea $a\in R$ con $a\neq0$.

Entonces:

1. $a$ no es divisor de cero por la izquierda si y sólo si
   $$
   \forall x,y\in R,
   \qquad
   ax=ay\Longrightarrow x=y;
   $$
2. $a$ no es divisor de cero por la derecha si y sólo si
   $$
   \forall x,y\in R,
   \qquad
   xa=ya\Longrightarrow x=y.
   $$

#### Demostración {#talg-prf-00044}

Demostremos primero la afirmación izquierda.

Supongamos que $a$ no es divisor de cero por la izquierda y que

$$
ax=ay.
$$

Por distributividad y por las reglas de signos de la [Proposición 14.4.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00025),

$$
\begin{aligned}
a\bigl(x+(-y)\bigr)
&=ax+a(-y)\\
&=ax+\bigl(-(ay)\bigr)\\
&=0.
\end{aligned}
$$

Como $a\neq0$ y $a$ no es divisor de cero por la izquierda, si $x+(-y)\neq0$ entonces $x+(-y)$ sería un testigo no nulo con producto cero, contradiciendo la [Definición 16.2.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00036). Por tanto,

$$
\neg\neg\bigl(x+(-y)=0\bigr).
$$

Aplicando eliminación de doble negación, válida en la lógica clásica fijada por el tratado, obtenemos

$$
x+(-y)=0.
$$

En el grupo aditivo de $R$, esto implica $x=y$.

Recíprocamente, supongamos que vale la cancelación izquierda y que

$$
ab=0.
$$

Por la [Proposición 14.3.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00024), $a0=0$, luego

$$
ab=a0.
$$

La hipótesis de cancelación da $b=0$. Por consiguiente, no existe un testigo no nulo $b$ con $ab=0$, y $a$ no es divisor de cero por la izquierda.

La afirmación derecha se demuestra de forma simétrica. Si $xa=ya$, entonces

$$
\bigl(x+(-y)\bigr)a=xa+(-y)a=xa+\bigl(-(ya)\bigr)=0,
$$

la ausencia de divisores de cero por la derecha da primero $\neg\neg(x+(-y)=0)$; por DNE obtenemos $x+(-y)=0$, y de aquí $x=y$. En sentido inverso, de $ba=0=0a$ y la cancelación derecha se deduce $b=0$.

$\square$

> **Lectura fundacional.** La implicación «cancelación $\Rightarrow$ ausencia de divisor de cero» es constructivamente compatible. La implicación inversa, bajo la definición negativa actual de «no ser divisor de cero», usa estabilidad de la igualdad / eliminación de doble negación.

---

## 16.5. El caso conmutativo

### Corolario 16.5.1 — Coincidencia de las nociones laterales en un anillo conmutativo {#talg-cor-00006}

Sea $\mathcal R$ un anillo conmutativo no trivial y sea $a\in R$ con $a\neq0$. Entonces

$$
\boxed{
a\text{ es divisor de cero por la izquierda}
\quad\Longleftrightarrow\quad
a\text{ es divisor de cero por la derecha}
}.
$$

#### Demostración {#talg-prf-00045}

Si $a$ es divisor de cero por la izquierda, existe $b\neq0$ con

$$
ab=0.
$$

Como la multiplicación es conmutativa,

$$
ba=ab=0,
$$

por lo que $a$ es divisor de cero por la derecha. La implicación recíproca es idéntica.

$\square$

---

### Definición 16.5.2 — Divisor de cero en un anillo conmutativo {#talg-def-00037}

Sea $\mathcal R$ un anillo conmutativo no trivial. Un elemento $a\in R$ es un **divisor de cero** si

$$
a\neq0
$$

y existe $b\in R$ tal que

$$
b\neq0
\qquad\text{y}\qquad
ab=0.
$$

Por el [Corolario 16.5.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-cor-00006), esta definición es equivalente a cualquiera de las dos nociones laterales de la [Definición 16.2.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00036).

---

### Corolario 16.5.3 — Cancelación en el caso conmutativo {#talg-cor-00007}

Sea $\mathcal R$ un anillo conmutativo no trivial y sea $a\in R$ con $a\neq0$. Entonces

$$
\boxed{
a\text{ no es divisor de cero}
\quad\Longleftrightarrow\quad
\forall x,y\in R,\; ax=ay\Longrightarrow x=y
}.
$$

#### Demostración {#talg-prf-00046}

En un anillo conmutativo, el [Corolario 16.5.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-cor-00006) identifica las nociones izquierda y derecha de divisor de cero, y la [Definición 16.5.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00037) adopta esa noción común. La equivalencia buscada es entonces la primera equivalencia del [Teorema 16.4.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-thm-00008).

$\square$

---

## 16.6. Cierre deductivo

Queda cerrada la cadena

```text
anillo
  ↓
0 ≠ 1
  ↓
anillo no trivial
  ↓
divisor de cero izquierdo / derecho
  ↓
unidad ⇒ no divisor de cero lateral
  ↓
ausencia de divisor de cero ↔ cancelación lateral (clásicamente)
  ↓
conmutatividad
  ↓
coincidencia izquierda = derecha
  ↓
divisor de cero (sin calificativo)
  ↓
ausencia de divisor de cero ↔ cancelación (clásicamente)
```

No se ha utilizado el axioma de elección. Tampoco se ha introducido todavía la noción de dominio íntegro: el capítulo sólo prepara su infraestructura multiplicativa.

El siguiente paso de la Parte III será definir **subanillos** y después los homomorfismos de anillos, antes de avanzar hacia ideales, cocientes y dominios.

---

[← **Capítulo 15 — Unidades de un anillo**](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md) · [**Capítulo 17 — Subanillos y homomorfismos de anillos** →](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md)
