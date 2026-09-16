---
title: 'Tratado moderno de Álgebra — Capítulo 7: Homomorfismos de magmas, monoides y grupos'
description: Construcción de la noción de homomorfismo desde magmas hasta grupos, con identidad y composición y demostraciones de preservación del neutro y de los inversos.
author: Gustav A. Tachek
content-id: MA-BCH-0032
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: '2026-09-15'
date-modified: '2026-09-16'
areas:
- algebra
- fundamentos
level: avanzado
topics:
- homomorfismos
- magmas
- semigrupos
- monoides
- grupos
- preservacion-de-estructura
- morfismos
prerequisites:
- MA-BCH-0027
related:
- MA-BOK-0007
- MA-BCH-0022
- MA-BCH-0024
- MA-BCH-0025
- MA-BCH-0026
- MA-BCH-0027
- MA-BCH-0030
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 7 — Homomorfismos de magmas, monoides y grupos

## 7.0. Propósito y criterio de economía axiomática

Una estructura algebraica no se estudia solamente por sus elementos y operaciones, sino también por las funciones que respetan esas operaciones. El objetivo de este capítulo es introducir la noción de **homomorfismo** en el nivel mínimo —los magmas— y especializarla después a semigrupos, monoides y grupos.

La política será no repetir como axioma aquello que pueda deducirse de la estructura ya disponible.

En particular:

1. un homomorfismo de magmas deberá preservar la operación;
2. un homomorfismo de semigrupos no necesita ninguna condición adicional;
3. un homomorfismo de monoides deberá preservar además el neutro;
4. un homomorfismo de grupos se definirá únicamente por preservación de la operación, porque la preservación del neutro y de los inversos será demostrada.

Esta asimetría entre monoides y grupos no es terminológica: refleja una diferencia deductiva real.

---

## 7.1. Homomorfismos de magmas

### Definición 7.1.1 — Homomorfismo de magmas {#talg-def-00016}

Sean

$$
\mathcal M=\langle A,\star\rangle,
\qquad
\mathcal N=\langle B,\diamond\rangle
$$

magmas. Una función

$$
f:A\to B
$$

es un **homomorfismo de magmas** de $\mathcal M$ en $\mathcal N$ si, para todos $x,y\in A$,

$$
f(x\star y)=f(x)\diamond f(y).
$$

La condición anterior expresa que aplicar primero la operación de $\mathcal M$ y después $f$ produce el mismo resultado que aplicar primero $f$ a cada entrada y después la operación de $\mathcal N$.

El dominio y el codominio de $f$ forman parte de la función; por tanto, hablar de homomorfismo exige especificar tanto la estructura fuente como la estructura destino.

---

### Proposición 7.1.2 — Identidad y composición de homomorfismos de magmas {#talg-pro-00006}

Sean

$$
\mathcal M=\langle A,\star\rangle,
\qquad
\mathcal N=\langle B,\diamond\rangle,
\qquad
\mathcal P=\langle C,\triangle\rangle
$$

magmas.

1. La función identidad $\operatorname{id}_A:A\to A$ es un homomorfismo de $\mathcal M$ en sí mismo.
2. Si $f:A\to B$ es un homomorfismo de $\mathcal M$ en $\mathcal N$ y $g:B\to C$ es un homomorfismo de $\mathcal N$ en $\mathcal P$, entonces
   $$
   g\circ f:A\to C
   $$
   es un homomorfismo de $\mathcal M$ en $\mathcal P$.

#### Demostración {#talg-prf-00008}

Para la identidad, sean $x,y\in A$. Entonces

$$
\operatorname{id}_A(x\star y)
=
x\star y
=
\operatorname{id}_A(x)\star\operatorname{id}_A(y).
$$

Por la [Definición 7.1.1](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00016), $\operatorname{id}_A$ es un homomorfismo de magmas.

Para la composición, sean $x,y\in A$. Como $f$ es homomorfismo,

$$
f(x\star y)=f(x)\diamond f(y).
$$

Aplicando $g$ y usando que $g$ es homomorfismo,

$$
g(f(x\star y))
=
g(f(x)\diamond f(y))
=
g(f(x))\triangle g(f(y)).
$$

Por definición de composición,

$$
(g\circ f)(x\star y)
=
(g\circ f)(x)\triangle(g\circ f)(y).
$$

Luego $g\circ f$ es un homomorfismo de magmas. $\square$

> **Lectura estructural.** Los homomorfismos de magmas son estables bajo identidad y composición. Esta propiedad será reutilizada por todas las clases posteriores de estructuras cuya noción de homomorfismo incluya la preservación de la operación.

---

## 7.2. Homomorfismos de semigrupos

### Definición 7.2.1 — Homomorfismo de semigrupos {#talg-def-00017}

Sean
$$
\mathcal S=\langle S,\star\rangle,
\qquad
\mathcal T=\langle T,\diamond\rangle
$$
semigrupos. Una función
$$
f:S\to T
$$
es un **homomorfismo de semigrupos** si es un homomorfismo de los magmas subyacentes.

No se añade una condición de «preservación de la asociatividad»: la asociatividad es una ley de las operaciones de $\mathcal S$ y $\mathcal T$, no un dato adicional que la función deba transportar.

Cuando sea necesario evitar cualquier ambigüedad tipográfica, se escribirán explícitamente los conjuntos y operaciones subyacentes.

---

## 7.3. Homomorfismos de monoides

### Definición 7.3.1 — Homomorfismo de monoides {#talg-def-00018}

Sean

$$
\mathcal M=\langle M,\star\rangle,
\qquad
\mathcal N=\langle N,\diamond\rangle
$$

monoides, con neutros $e_{\mathcal M}$ y $e_{\mathcal N}$. Una función

$$
f:M\to N
$$

es un **homomorfismo de monoides** si satisface simultáneamente:

1. preservación de la operación:
   $$
   \forall x,y\in M,
   \qquad
   f(x\star y)=f(x)\diamond f(y);
   $$
2. preservación del neutro:
   $$
   f(e_{\mathcal M})=e_{\mathcal N}.
   $$

Equivalente y más brevemente: un homomorfismo de monoides es un homomorfismo de los magmas subyacentes que preserva el neutro.

> **Nota conceptual.** La segunda condición no se elimina de la definición general de homomorfismo de monoides. La multiplicatividad por sí sola sólo garantiza que $f(e_{\mathcal M})$ actúe como neutro sobre los elementos de la imagen de $f$; sin una hipótesis adicional, esa imagen no tiene por qué ser todo $N$.

---

## 7.4. Homomorfismos de grupos

### Definición 7.4.1 — Homomorfismo de grupos {#talg-def-00019}

Sean

$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

grupos. Una función

$$
f:G\to H
$$

es un **homomorfismo de grupos** si es un homomorfismo de los magmas subyacentes, es decir, si

$$
\forall x,y\in G,
\qquad
f(x\star y)=f(x)\diamond f(y).
$$

A diferencia del caso de los monoides, no se exige en la definición ni

$$
f(e_{\mathcal G})=e_{\mathcal H}
$$

ni

$$
f(x^{-1})=f(x)^{-1}.
$$

Ambas identidades serán consecuencias de la multiplicatividad y de la existencia de inversos en el grupo destino.

---

### Proposición 7.4.2 — Preservación del neutro por homomorfismos de grupos {#talg-pro-00007}

Sea
$$
f:G\to H
$$
un homomorfismo de los grupos
$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle.
$$
Entonces

$$
f(e_{\mathcal G})=e_{\mathcal H}.
$$

#### Demostración {#talg-prf-00009}

Pongamos

$$
u:=f(e_{\mathcal G}).
$$

Como $e_{\mathcal G}\star e_{\mathcal G}=e_{\mathcal G}$ y $f$ preserva la operación,

$$
u
=
f(e_{\mathcal G})
=
f(e_{\mathcal G}\star e_{\mathcal G})
=
f(e_{\mathcal G})\diamond f(e_{\mathcal G})
=
u\diamond u.
$$

El elemento $u$ pertenece al grupo $\mathcal H$, por lo que posee inverso $u^{-1}$. Multiplicando la igualdad anterior por $u^{-1}$ a la izquierda,

$$
u^{-1}\diamond u
=
u^{-1}\diamond(u\diamond u).
$$

Por asociatividad en $\mathcal H$,

$$
e_{\mathcal H}
=
(u^{-1}\diamond u)\diamond u
=
e_{\mathcal H}\diamond u
=
u.
$$

Por tanto,

$$
f(e_{\mathcal G})=u=e_{\mathcal H}.
$$

No se ha supuesto la preservación del neutro; se ha deducido de la multiplicatividad. $\square$

---

### Proposición 7.4.3 — Preservación de inversos por homomorfismos de grupos {#talg-pro-00008}

Sea
$$
f:G\to H
$$
un homomorfismo de los grupos
$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle.
$$
Entonces, para todo $x\in G$,

$$
f(x^{-1})=f(x)^{-1}.
$$

#### Demostración {#talg-prf-00010}

Sea $x\in G$. En $\mathcal G$,

$$
x^{-1}\star x=e_{\mathcal G}
\qquad\text{y}\qquad
x\star x^{-1}=e_{\mathcal G}.
$$

Aplicando $f$ y usando que preserva la operación,

$$
f(x^{-1})\diamond f(x)
=
f(e_{\mathcal G})
$$

y

$$
f(x)\diamond f(x^{-1})
=
f(e_{\mathcal G}).
$$

Por la [Proposición 7.4.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007),

$$
f(e_{\mathcal G})=e_{\mathcal H}.
$$

Luego $f(x^{-1})$ es un inverso bilateral de $f(x)$ en $\mathcal H$. Por unicidad del inverso ([Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002)),

$$
f(x^{-1})=f(x)^{-1}.
$$

$\square$

---

### Corolario 7.4.4 — Todo homomorfismo de grupos es un homomorfismo de monoides {#talg-cor-00001}

Sean
$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$
grupos. Si $f:G\to H$ es un homomorfismo de grupos, entonces, al considerar $\mathcal G$ y $\mathcal H$ como monoides, $f$ es un homomorfismo de monoides.

#### Demostración {#talg-prf-00011}

Por definición de homomorfismo de grupos, $f$ preserva la operación. Por la [Proposición 7.4.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007), preserva además el neutro. Éstas son exactamente las dos condiciones de la [Definición 7.3.1](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00018). $\square$

---

## 7.5. Consecuencias estructurales inmediatas

La jerarquía de morfismos construida en este capítulo puede resumirse así:

$$
\text{homomorfismo de magmas}
\supset
\text{homomorfismo de semigrupos},
$$

en el sentido de que todo homomorfismo de semigrupos es, por definición, un homomorfismo de los magmas subyacentes.

Para monoides se añade la preservación explícita del neutro. Para grupos, la estructura de inversos hace esa condición deducible:

$$
\text{homomorfismo de grupos}
\Longrightarrow
\text{preserva }e
\Longrightarrow
\text{preserva inversos}.
$$

La [Proposición 7.1.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00006) garantiza además que la identidad y la composición ya funcionan correctamente desde el nivel de magmas.

Antes de definir isomorfismos será necesario ampliar de manera explícita la interfaz fundacional con las nociones ya cerradas en `TA-0003` de inyectividad, sobreyectividad, biyectividad e inversa funcional. Esa ampliación se registrará como una nueva importación intertratados, sin alterar retrospectivamente la interfaz mínima anterior.

---

[← **Capítulo 6 — Subestructuras y criterio de subgrupo**](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md) · [**Capítulo 8 — Isomorfismos** →](tratado-de-algebra-capitulo-8-isomorfismos.md)
