---
title: 'Tratado moderno de Álgebra — Capítulo 9: Núcleo e imagen de homomorfismos de grupos'
description: Construcción del núcleo y la imagen de un homomorfismo de grupos, prueba de que ambos son subgrupos y caracterizaciones algebraicas de inyectividad y sobreyectividad.
author: Gustav A. Tachek
content-id: MA-BCH-0034
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
- nucleo
- imagen
- homomorfismos-de-grupos
- subgrupos
- inyectividad
- sobreyectividad
prerequisites:
- MA-BCH-0032
- MA-BCH-0030
- MA-BCH-0022
related:
- MA-BOK-0007
- MA-BCH-0027
- MA-BCH-0033
- MA-BCH-0035
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 9 — Núcleo e imagen de homomorfismos de grupos

## 9.0. Propósito y posición deductiva

Un homomorfismo de grupos

$$
f:G\to H
$$

puede estudiarse desde dos subconjuntos canónicos asociados a él:

- los elementos del dominio que son enviados al neutro del grupo destino;
- los elementos del codominio que son alcanzados por la función.

El primero será el **núcleo** y el segundo la **imagen**. Ambos se construirán como subconjuntos mediante Separación, sin importar todavía la infraestructura general de imágenes y preimágenes de `TA-0003`.

La secuencia deductiva será

$$
\text{homomorfismo de grupos}
\longrightarrow
\ker f,\ \operatorname{im}f
\longrightarrow
\text{subgrupos}
\longrightarrow
\text{inyectividad y sobreyectividad caracterizadas algebraicamente}.
$$

La normalidad del núcleo y los cocientes se posponen hasta introducir formalmente los subgrupos normales.

---

## 9.1. Núcleo de un homomorfismo

### Definición 9.1.1 — Núcleo de un homomorfismo de grupos {#talg-def-00024}

Sean

$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

grupos y sea

$$
f:G\to H
$$

un homomorfismo de grupos. Definimos el **núcleo de $f$** como el subconjunto de $G$

$$
\{x\in G:f(x)=e_{\mathcal H}\}.
$$

Este conjunto existe por Separación aplicada a $G$.

La definición depende del homomorfismo completo, incluido su codominio: el neutro utilizado es el de la estructura destino $\mathcal H$.

---

### Notación 9.1.2 — Núcleo {#talg-not-00006}

En la situación anterior escribiremos

$$
\ker f
:=
\{x\in G:f(x)=e_{\mathcal H}\}.
$$

Por construcción,

$$
\ker f\subseteq G.
$$

La notación $\ker f$ no se utilizará para una función arbitraria: en este tratado queda introducida inicialmente para homomorfismos de grupos.

---

### Proposición 9.1.3 — El núcleo es un subgrupo {#talg-pro-00014}

Sea

$$
f:G\to H
$$

un homomorfismo de grupos. Entonces $\ker f$ determina un subgrupo de $\mathcal G$.

#### Demostración {#talg-prf-00018}

Aplicaremos el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) al subconjunto $\ker f\subseteq G$.

Por la [Proposición 7.4.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007),

$$
f(e_{\mathcal G})=e_{\mathcal H},
$$

por lo que

$$
e_{\mathcal G}\in\ker f.
$$

En particular, $\ker f$ está habitado, con testigo explícito $e_{\mathcal G}$.

Sean ahora $a,b\in\ker f$. Entonces

$$
f(a)=e_{\mathcal H}
\qquad\text{y}\qquad
f(b)=e_{\mathcal H}.
$$

Por la [Proposición 7.4.3](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008),

$$
f(b^{-1})=f(b)^{-1}=e_{\mathcal H}^{-1}.
$$

El elemento $e_{\mathcal H}$ es un inverso bilateral de sí mismo, pues

$$
e_{\mathcal H}\diamond e_{\mathcal H}=e_{\mathcal H}.
$$

Por unicidad del inverso ([Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002)),

$$
e_{\mathcal H}^{-1}=e_{\mathcal H}.
$$

Como $f$ es homomorfismo,

$$
\begin{aligned}
f(a\star b^{-1})
&=f(a)\diamond f(b^{-1})\\
&=e_{\mathcal H}\diamond e_{\mathcal H}\\
&=e_{\mathcal H}.
\end{aligned}
$$

Por la definición del núcleo,

$$
a\star b^{-1}\in\ker f.
$$

El [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) implica que $\ker f$ determina un subgrupo de $\mathcal G$. $\square$

---

## 9.2. Imagen de un homomorfismo

### Definición 9.2.1 — Imagen de un homomorfismo de grupos {#talg-def-00025}

Sean

$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

grupos y sea

$$
f:G\to H
$$

un homomorfismo de grupos. Definimos la **imagen de $f$** como el subconjunto de $H$

$$
\{y\in H:\exists x\in G,\ f(x)=y\}.
$$

Este conjunto existe por Separación aplicada a $H$.

No se necesita aquí importar la operación general de imagen de subconjuntos desde `TA-0003`: la construcción anterior es suficiente y mantiene mínima la interfaz intertratados.

---

### Notación 9.2.2 — Imagen {#talg-not-00007}

En la situación anterior escribiremos

$$
\operatorname{im}f
:=
\{y\in H:\exists x\in G,\ f(x)=y\}.
$$

Por construcción,

$$
\operatorname{im}f\subseteq H.
$$

---

### Proposición 9.2.3 — La imagen es un subgrupo {#talg-pro-00015}

Sea

$$
f:G\to H
$$

un homomorfismo de grupos. Entonces $\operatorname{im}f$ determina un subgrupo de $\mathcal H$.

#### Demostración {#talg-prf-00019}

Aplicaremos el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) al subconjunto $\operatorname{im}f\subseteq H$.

Por la [Proposición 7.4.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007),

$$
f(e_{\mathcal G})=e_{\mathcal H},
$$

luego

$$
e_{\mathcal H}\in\operatorname{im}f.
$$

Así, $\operatorname{im}f$ está habitada, con testigo explícito $e_{\mathcal H}=f(e_{\mathcal G})$.

Sean $u,v\in\operatorname{im}f$. Por definición de imagen, existen $a,b\in G$ tales que

$$
f(a)=u,
\qquad
f(b)=v.
$$

Por la [Proposición 7.4.3](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008),

$$
f(b^{-1})=f(b)^{-1}=v^{-1}.
$$

Por preservación de la operación,

$$
\begin{aligned}
u\diamond v^{-1}
&=f(a)\diamond f(b^{-1})\\
&=f(a\star b^{-1}).
\end{aligned}
$$

Como $a\star b^{-1}\in G$, la última igualdad muestra que

$$
u\diamond v^{-1}\in\operatorname{im}f.
$$

Por el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $\operatorname{im}f$ determina un subgrupo de $\mathcal H$. $\square$

---

## 9.3. Caracterizaciones funcionales

### Teorema 9.3.1 — Inyectividad y núcleo trivial {#talg-thm-00002}

Sea

$$
f:G\to H
$$

un homomorfismo de grupos. Son equivalentes:

1. $f$ es inyectiva;
2. $\ker f=\{e_{\mathcal G}\}$.

Cuando se cumple la segunda condición diremos que $f$ tiene **núcleo trivial**.

#### Demostración {#talg-prf-00020}

**$(1)\Rightarrow(2)$.** Supongamos que $f$ es inyectiva. Por la [Proposición 7.4.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007),

$$
f(e_{\mathcal G})=e_{\mathcal H},
$$

así que

$$
e_{\mathcal G}\in\ker f.
$$

Sea $x\in\ker f$. Entonces

$$
f(x)=e_{\mathcal H}=f(e_{\mathcal G}).
$$

Por inyectividad,

$$
x=e_{\mathcal G}.
$$

Por doble inclusión y Extensionalidad,

$$
\ker f=\{e_{\mathcal G}\}.
$$

**$(2)\Rightarrow(1)$.** Supongamos ahora

$$
\ker f=\{e_{\mathcal G}\}.
$$

Sean $x,y\in G$ tales que

$$
f(x)=f(y).
$$

Por la [Proposición 7.4.3](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008),

$$
f(y^{-1})=f(y)^{-1}.
$$

Entonces

$$
\begin{aligned}
f(x\star y^{-1})
&=f(x)\diamond f(y^{-1})\\
&=f(y)\diamond f(y)^{-1}\\
&=e_{\mathcal H}.
\end{aligned}
$$

Por tanto,

$$
x\star y^{-1}\in\ker f=\{e_{\mathcal G}\},
$$

de donde

$$
x\star y^{-1}=e_{\mathcal G}.
$$

Multiplicando a la derecha por $y$ y usando asociatividad, inversos y neutro en $\mathcal G$,

$$
\begin{aligned}
x
&=x\star e_{\mathcal G}\\
&=x\star(y^{-1}\star y)\\
&=(x\star y^{-1})\star y\\
&=e_{\mathcal G}\star y\\
&=y.
\end{aligned}
$$

Así, $f(x)=f(y)$ implica $x=y$. Por la definición de inyectividad importada mediante [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002), $f$ es inyectiva. $\square$

---

### Proposición 9.3.2 — Sobreyectividad e imagen total {#talg-pro-00016}

Sea

$$
f:G\to H
$$

un homomorfismo de grupos. Son equivalentes:

1. $f$ es sobreyectiva;
2. $\operatorname{im}f=H$.

#### Demostración {#talg-prf-00021}

**$(1)\Rightarrow(2)$.** Por definición,

$$
\operatorname{im}f\subseteq H.
$$

Si $f$ es sobreyectiva y $h\in H$, existe $g\in G$ tal que

$$
f(g)=h.
$$

Entonces $h\in\operatorname{im}f$. Por tanto,

$$
H\subseteq\operatorname{im}f.
$$

Por Extensionalidad,

$$
\operatorname{im}f=H.
$$

**$(2)\Rightarrow(1)$.** Supongamos

$$
\operatorname{im}f=H.
$$

Sea $h\in H$. Entonces $h\in\operatorname{im}f$, y por definición de imagen existe $g\in G$ tal que

$$
f(g)=h.
$$

Esto es exactamente la sobreyectividad de $f$ según [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002). $\square$

---

## 9.4. Lectura estructural

El núcleo y la imagen miden dos aspectos diferentes de un homomorfismo:

$$
\ker f
\quad\text{mide la pérdida de distinción en el dominio,}
$$

mientras que

$$
\operatorname{im}f
\quad\text{mide la porción del codominio alcanzada por la función.}
$$

Los resultados anteriores convierten estas intuiciones en equivalencias exactas:

$$
f\text{ inyectiva}
\iff
\ker f=\{e_{\mathcal G}\},
$$

$$
f\text{ sobreyectiva}
\iff
\operatorname{im}f=H.
$$

Además, la [Proposición 9.1.3](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-pro-00014) y la [Proposición 9.2.3](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-pro-00015) muestran que ambos subconjuntos son algebraicamente estables: no son subconjuntos accidentales, sino subgrupos canónicos asociados a $f$.

El siguiente paso será distinguir una propiedad especial del núcleo que todavía no ha sido definida: la **normalidad**. Sólo después se construirán cocientes de grupos y los teoremas de isomorfía.

---

[← **Capítulo 8 — Isomorfismos**](tratado-de-algebra-capitulo-8-isomorfismos.md) · [**Capítulo 10 — Subgrupos normales** →](tratado-de-algebra-capitulo-10-subgrupos-normales.md)
