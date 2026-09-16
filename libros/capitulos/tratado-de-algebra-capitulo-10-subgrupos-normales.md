---
title: 'Tratado moderno de Álgebra — Capítulo 10: Subgrupos normales'
description: Capítulo del Tratado moderno de Álgebra dedicado a subgrupos normales, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0035
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
- MA-BCH-0034
related:
- MA-BOK-0007
- MA-BCH-0034
- MA-BCH-0036
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 10 — Subgrupos normales

## 10.0. Propósito y posición deductiva

El capítulo anterior asoció a cada homomorfismo de grupos dos subgrupos canónicos: su núcleo y su imagen. Para construir cocientes de grupos no basta, sin embargo, con disponer de un subgrupo cualquiera. Es necesario aislar una condición adicional que permita que la multiplicación de representantes descienda de manera coherente a las clases laterales.

Esa condición es la **normalidad**.

La secuencia deductiva será

$$
\text{subgrupo}
\longrightarrow
\text{estabilidad por conjugación}
\longrightarrow
\text{subgrupo normal}
\longrightarrow
\ker f\text{ normal}.
$$

Las clases laterales todavía no forman parte de la infraestructura del tratado. Por ello la normalidad se definirá inicialmente mediante conjugación y no mediante la igualdad entre clases laterales izquierdas y derechas. Esa equivalencia se demostrará sólo después de construir dichas clases.

---

## 10.1. Normalidad

### Definición 10.1.1 — Subgrupo normal {#talg-def-00026}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo y sea $N\subseteq G$ un subconjunto que determina un subgrupo de $\mathcal G$.

Decimos que $N$ es un **subgrupo normal** de $\mathcal G$ si, para todo $g\in G$ y todo $n\in N$,

$$
(g\star n)\star g^{-1}\in N.
$$

La condición expresa que $N$ es estable bajo conjugación por elementos del grupo ambiente.

No se introduce todavía la notación de clases laterales ni se presupone ninguna igualdad de la forma $gN=Ng$. La definición depende únicamente de la estructura de grupo ya construida.

---

### Notación 10.1.2 — Normalidad {#talg-not-00008}

En la situación anterior escribiremos

$$
N\trianglelefteq G
$$

para expresar que $N$ determina un subgrupo normal de $\mathcal G$.

Cuando sea necesario distinguir estructuras distintas sobre un mismo conjunto subyacente, la afirmación de normalidad se formulará mencionando explícitamente la estructura ambiente.

---

## 10.2. El núcleo de un homomorfismo es normal

### Proposición 10.2.1 — Normalidad del núcleo {#talg-pro-00017}

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

un homomorfismo de grupos. Entonces

$$
\ker f\trianglelefteq G.
$$

#### Demostración {#talg-prf-00022}

Por la [Proposición 9.1.3](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-pro-00014), $\ker f$ determina ya un subgrupo de $\mathcal G$. Sólo resta verificar la estabilidad por conjugación exigida en la [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026).

Sean

$$
g\in G
\qquad\text{y}\qquad
n\in\ker f.
$$

Por definición del núcleo,

$$
f(n)=e_{\mathcal H}.
$$

Como $f$ es homomorfismo,

$$
f\bigl((g\star n)\star g^{-1}\bigr)
=
f(g\star n)\diamond f(g^{-1}).
$$

Aplicando nuevamente la preservación de la operación,

$$
f(g\star n)
=
f(g)\diamond f(n),
$$

y por la [Proposición 7.4.3](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008),

$$
f(g^{-1})=f(g)^{-1}.
$$

Por tanto,

$$
\begin{aligned}
f\bigl((g\star n)\star g^{-1}\bigr)
&=
\bigl(f(g)\diamond f(n)\bigr)\diamond f(g)^{-1}\\
&=
\bigl(f(g)\diamond e_{\mathcal H}\bigr)\diamond f(g)^{-1}\\
&=
f(g)\diamond f(g)^{-1}\\
&=
e_{\mathcal H}.
\end{aligned}
$$

De la definición del núcleo se sigue que

$$
(g\star n)\star g^{-1}\in\ker f.
$$

Como $g\in G$ y $n\in\ker f$ eran arbitrarios, $\ker f$ es estable bajo conjugación. Por la [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026),

$$
\ker f\trianglelefteq G.
$$

$\square$

> **Consecuencia estructural.** La normalidad no es una propiedad accidental de ciertos núcleos: todo homomorfismo de grupos produce canónicamente un subgrupo normal de su dominio. Ésta es la razón algebraica que permitirá construir posteriormente el cociente asociado a un homomorfismo.

---

## 10.3. El caso abeliano

### Proposición 10.3.1 — Todo subgrupo de un grupo abeliano es normal {#talg-pro-00018}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo abeliano y sea $N\subseteq G$ un subconjunto que determina un subgrupo de $\mathcal G$. Entonces

$$
N\trianglelefteq G.
$$

#### Demostración {#talg-prf-00023}

Sean $g\in G$ y $n\in N$. Como $\mathcal G$ es abeliano,

$$
g\star n=n\star g.
$$

Entonces, usando asociatividad,

$$
\begin{aligned}
(g\star n)\star g^{-1}
&=
(n\star g)\star g^{-1}\\
&=
n\star(g\star g^{-1})\\
&=
n\star e_{\mathcal G}\\
&=
n.
\end{aligned}
$$

Como $n\in N$, obtenemos

$$
(g\star n)\star g^{-1}\in N.
$$

La condición de normalidad se cumple para todo $g\in G$ y todo $n\in N$. Por la [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026),

$$
N\trianglelefteq G.
$$

$\square$

---

## 10.4. Lectura estructural

La normalidad marca la primera diferencia esencial entre la teoría de subgrupos y la teoría de cocientes.

Un subgrupo ordinario sólo garantiza que la operación ambiente se restringe correctamente al subconjunto. Un subgrupo normal satisface además una compatibilidad con la acción interna del grupo por conjugación:

$$
n\in N
\quad\Longrightarrow\quad
(g\star n)\star g^{-1}\in N
\qquad
(g\in G).
$$

Dos casos importantes quedan ya cerrados:

$$
\ker f\trianglelefteq G
$$

para todo homomorfismo de grupos $f:G\to H$, y

En particular, si $G$ es abeliano, todo subconjunto $N\subseteq G$ que determine un subgrupo determina automáticamente un subgrupo normal.

No se introduce aquí una notación adicional para la relación «ser subgrupo de»; la afirmación anterior se mantiene en el lenguaje ya definido.

El siguiente bloque construirá las **clases laterales izquierdas y derechas** de un subgrupo. Sólo entonces podrá demostrarse que la normalidad equivale a la coincidencia de ambas familias y prepararse la operación sobre el cociente.

---

[← **Capítulo 9 — Núcleo e imagen de homomorfismos de grupos**](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md) · [**Capítulo 11 — Clases laterales y caracterización de la normalidad** →](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md)
