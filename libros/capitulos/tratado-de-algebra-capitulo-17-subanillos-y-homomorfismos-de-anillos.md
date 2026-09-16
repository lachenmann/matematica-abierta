---
title: 'Tratado moderno de Álgebra — Capítulo 17: Subanillos y homomorfismos de anillos'
description: Capítulo del Tratado moderno de Álgebra dedicado a subanillos y homomorfismos de anillos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0042
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
- MA-BCH-0041
related:
- MA-BOK-0007
- MA-BCH-0041
- MA-BCH-0043
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 17 — Subanillos y homomorfismos de anillos

## 17.0. Propósito y convención unital

El paso siguiente consiste en trasladar a los anillos dos ideas ya construidas para estructuras con una sola operación:

1. **subestructura:** restringir las operaciones a un subconjunto compatible;
2. **morfismo:** comparar dos estructuras mediante una función que preserve las operaciones pertinentes.

Hay, sin embargo, una decisión de convención que debe fijarse antes de proceder. En este tratado un anillo posee unidad multiplicativa por definición ([Definición 14.1.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00032)), y un submonoide contiene el neutro del monoide ambiente ([Definición 6.3.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-def-00014)). Adoptaremos la misma política para subanillos y homomorfismos:

- un **subanillo** contiene el mismo elemento $1$ que el anillo ambiente;
- un **homomorfismo de anillos** preserva explícitamente la unidad multiplicativa.

Esta convención excluye como subanillos ciertas estructuras que, con las operaciones restringidas, podrían constituir anillos con una unidad distinta de la ambiente. Por ejemplo, si $\mathcal R$ es no trivial, el subconjunto $\{0\}$ forma un anillo trivial con las operaciones restringidas, pero no será un subanillo de $\mathcal R$ porque no contiene $1_{\mathcal R}$.

> **Contraste bibliográfico.** La literatura no es uniforme respecto de la exigencia de unidad en subanillos y de preservación de $1$ en homomorfismos. La convención de este tratado se controla por contraste con Dummit–Foote (`BIB-TALG-0001`), Lam (`BIB-TALG-0008`) y Atiyah–Macdonald (`BIB-TALG-0007`), pero queda determinada internamente por nuestra arquitectura unital previa.

---

## 17.1. Subanillos

### Definición 17.1.1 — Subanillo {#talg-def-00038}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo y sea $S\subseteq R$.

Diremos que la estructura inducida

$$
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

es un **subanillo** de $\mathcal R$ si se satisfacen simultáneamente:

1. $\langle S,+_S\rangle$ es un subgrupo de $\langle R,+\rangle$;
2. $\langle S,\cdot_S\rangle$ es un submonoide de $\langle R,\cdot\rangle$.

Aquí $+_S$ y $\cdot_S$ son las restricciones canónicas de $+$ y $\cdot$ a $S$, en el sentido del [Lema 6.1.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00001) y la [Notación 6.1.3](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-not-00004).

Como los submonoides del tratado son unitarios, la segunda condición incorpora

$$
1_{\mathcal R}\in S.
$$

No se permite, por tanto, que un subanillo tenga una unidad multiplicativa distinta de la unidad del anillo ambiente.

---

### Proposición 17.1.2 — La estructura inducida es un anillo y hereda $0$ y $1$ {#talg-pro-00030}

Si $\mathcal S=\langle S,+_S,\cdot_S\rangle$ es un subanillo de

$$
\mathcal R=\langle R,+,\cdot\rangle,
$$

entonces $\mathcal S$ es un anillo en el sentido de la [Definición 14.1.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00032). Además,

$$
\boxed{
0_{\mathcal S}=0_{\mathcal R},
\qquad
1_{\mathcal S}=1_{\mathcal R}.
}
$$

#### Demostración {#talg-prf-00047}

Por la [Definición 17.1.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00038), $\langle S,+_S\rangle$ es un subgrupo del grupo aditivo $\langle R,+\rangle$. En particular es un grupo. Como la suma de $R$ es conmutativa, para $x,y\in S$ se tiene

$$
x+_S y=x+y=y+x=y+_S x,
$$

de modo que $\langle S,+_S\rangle$ es un grupo abeliano.

La misma definición establece que $\langle S,\cdot_S\rangle$ es un submonoide de $\langle R,\cdot\rangle$; por tanto es un monoide y, por la convención unital de la [Definición 6.3.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-def-00014) junto con la [Proposición 6.3.1](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00004), su neutro es el neutro multiplicativo ambiente:

$$
1_{\mathcal S}=1_{\mathcal R}.
$$

Para el neutro aditivo, la [Proposición 6.4.1](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00005) garantiza que el subgrupo hereda la estructura de grupo del ambiente; en particular, su neutro coincide con el neutro del grupo aditivo ambiente:

$$
0_{\mathcal S}=0_{\mathcal R}.
$$

Sólo resta comprobar la distributividad. Sean $a,b,c\in S$. Como las operaciones inducidas son restricciones de las operaciones ambiente,

$$
a\cdot_S(b+_S c)
=
a\cdot(b+c).
$$

La distributividad en $\mathcal R$ da

$$
a\cdot(b+c)=a\cdot b+a\cdot c,
$$

y, como todos los términos pertenecen a $S$ por cierre, esto equivale a

$$
a\cdot_S(b+_S c)
=
(a\cdot_S b)+_S(a\cdot_S c).
$$

La distributividad por la derecha se hereda de la misma manera. Por consiguiente, $\mathcal S$ satisface todos los axiomas de anillo de la [Definición 14.1.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00032).

$\square$

---

### Teorema 17.1.3 — Criterio de subanillo unital {#talg-thm-00009}

Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo y sea $S\subseteq R$. Entonces $S$ determina un subanillo de $\mathcal R$ si y sólo si:

1. $1\in S$;
2. para todos $a,b\in S$,
   $$
   a-b\in S;
   $$
3. para todos $a,b\in S$,
   $$
   ab\in S.
   $$

#### Demostración {#talg-prf-00048}

Supongamos primero que $S$ determina un subanillo. Entonces $\langle S,\cdot_S\rangle$ es un submonoide del monoide multiplicativo de $R$, por lo que

$$
1\in S
$$

y $S$ es cerrado bajo multiplicación.

Además, $\langle S,+_S\rangle$ es un subgrupo del grupo aditivo. Por cierre bajo suma e inversos aditivos, si $a,b\in S$, entonces

$$
a-b=a+(-b)\in S.
$$

Recíprocamente, supongamos las tres condiciones. Como $1\in S$, el conjunto $S$ está habitado, con testigo explícito $1$. Aplicando el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) al grupo aditivo $\langle R,+\rangle$, la condición

$$
a-b=a+(-b)\in S
$$

para todos $a,b\in S$ implica que $\langle S,+_S\rangle$ es un subgrupo de $\langle R,+\rangle$.

Por la tercera condición, $S$ es cerrado bajo la multiplicación. Junto con $1\in S$, la [Proposición 6.3.1](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-pro-00004) y la [Definición 6.3.2](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-def-00014) muestran que $\langle S,\cdot_S\rangle$ es un submonoide del monoide multiplicativo de $R$.

Se cumplen, por tanto, las dos condiciones de la [Definición 17.1.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00038), y $S$ determina un subanillo de $\mathcal R$.

$\square$

---

### Proposición 17.1.4 — Herencia de conmutatividad y equivalencia de no trivialidad {#talg-pro-00031}

Sea $\mathcal S$ un subanillo de $\mathcal R$.

1. Si $\mathcal R$ es conmutativo, entonces $\mathcal S$ es conmutativo.
2. $\mathcal S$ es no trivial si y sólo si $\mathcal R$ es no trivial.

#### Demostración {#talg-prf-00049}

Si $x,y\in S$ y la multiplicación de $R$ es conmutativa, entonces

$$
x\cdot_S y
=
x\cdot y
=
y\cdot x
=
y\cdot_S x.
$$

Luego $\mathcal S$ es conmutativo.

Por la [Proposición 17.1.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00030),

$$
0_{\mathcal S}=0_{\mathcal R}
\qquad\text{y}\qquad
1_{\mathcal S}=1_{\mathcal R}.
$$

Así,

$$
0_{\mathcal S}\neq1_{\mathcal S}
\quad\Longleftrightarrow\quad
0_{\mathcal R}\neq1_{\mathcal R}.
$$

Por la [Definición 16.1.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00035), esto equivale exactamente a

$$
\mathcal S\text{ no trivial}
\quad\Longleftrightarrow\quad
\mathcal R\text{ no trivial}.
$$

$\square$

---

## 17.2. Homomorfismos de anillos

### Definición 17.2.1 — Homomorfismo de anillos {#talg-def-00039}

Sean

$$
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

anillos. Una función

$$
f:R\to S
$$

es un **homomorfismo de anillos** si, para todos $a,b\in R$,

$$
f(a+_R b)=f(a)+_S f(b),
$$

$$
f(a\cdot_R b)=f(a)\cdot_S f(b),
$$

y además

$$
\boxed{f(1_{\mathcal R})=1_{\mathcal S}.}
$$

La preservación del cero y de los opuestos aditivos **no** se incorpora como axioma: se demostrará a continuación.

> **Convención unital.** En este tratado todo homomorfismo de anillos preserva $1$. No se utilizará la misma expresión para aplicaciones multiplicativas y aditivas que no preserven la unidad multiplicativa.

---

### Proposición 17.2.2 — Preservación del cero y de los opuestos aditivos {#talg-pro-00032}

Sea $f:R\to S$ un homomorfismo de anillos. Entonces

$$
\boxed{f(0_{\mathcal R})=0_{\mathcal S}}
$$

y, para todo $a\in R$,

$$
\boxed{f(-a)=-f(a)}.
$$

#### Demostración {#talg-prf-00050}

Por la [Definición 17.2.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00039), la función $f$ preserva la suma. Considerando únicamente los grupos aditivos

$$
\langle R,+_R\rangle
\qquad\text{y}\qquad
\langle S,+_S\rangle,
$$

$f$ es por tanto un homomorfismo de grupos en el sentido de la [Definición 7.4.1](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019).

La preservación del neutro por homomorfismos de grupos ([Proposición 7.4.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007)) da

$$
f(0_{\mathcal R})=0_{\mathcal S}.
$$

La preservación de inversos ([Proposición 7.4.3](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008)) aplicada a los inversos aditivos da

$$
f(-a)=-f(a).
$$

$\square$

---

### Proposición 17.2.3 — Identidad y composición de homomorfismos de anillos {#talg-pro-00033}

1. Para todo anillo $\mathcal R$, la función identidad
   $$
   \operatorname{id}_R:R\to R
   $$
   es un homomorfismo de anillos.
2. Si
   $$
   f:R\to S
   \qquad\text{y}\qquad
   g:S\to T
   $$
   son homomorfismos de anillos, entonces
   $$
   g\circ f:R\to T
   $$
   es un homomorfismo de anillos.

#### Demostración {#talg-prf-00051}

La identidad preserva inmediatamente suma, producto y unidad:

$$
\operatorname{id}_R(a+b)=a+b
=
\operatorname{id}_R(a)+\operatorname{id}_R(b),
$$

$$
\operatorname{id}_R(ab)=ab
=
\operatorname{id}_R(a)\operatorname{id}_R(b),
$$

y

$$
\operatorname{id}_R(1_R)=1_R.
$$

Sean ahora $f$ y $g$ homomorfismos de anillos. Para $a,b\in R$,

$$
\begin{aligned}
(g\circ f)(a+b)
&=g(f(a+b))\\
&=g(f(a)+f(b))\\
&=g(f(a))+g(f(b))\\
&=(g\circ f)(a)+(g\circ f)(b),
\end{aligned}
$$

y del mismo modo

$$
(g\circ f)(ab)
=
g(f(a)f(b))
=
g(f(a))g(f(b))
=
(g\circ f)(a)(g\circ f)(b).
$$

Finalmente,

$$
(g\circ f)(1_R)
=
g(f(1_R))
=
g(1_S)
=
1_T.
$$

Luego $g\circ f$ es un homomorfismo de anillos.

$\square$

---

### Proposición 17.2.4 — Las unidades se envían en unidades {#talg-pro-00034}

Sea $f:R\to S$ un homomorfismo de anillos. Si $u\in R^\times$, entonces

$$
f(u)\in S^\times
$$

y

$$
\boxed{f(u^{-1})=f(u)^{-1}.}
$$

#### Demostración {#talg-prf-00052}

Como $u$ es una unidad,

$$
uu^{-1}=u^{-1}u=1_R.
$$

Aplicando $f$ y usando preservación del producto y de la unidad,

$$
f(u)f(u^{-1})
=
f(uu^{-1})
=
f(1_R)
=
1_S,
$$

y también

$$
f(u^{-1})f(u)
=
1_S.
$$

Por tanto, $f(u^{-1})$ es un inverso multiplicativo bilateral de $f(u)$. Así, $f(u)$ es una unidad de $S$ y, por la unicidad del inverso multiplicativo ([Proposición 15.2.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00026)),

$$
f(u^{-1})=f(u)^{-1}.
$$

$\square$

---

## 17.3. Imagen y núcleo

### Proposición 17.3.1 — La imagen de un homomorfismo de anillos es un subanillo {#talg-pro-00035}

Sea

$$
f:R\to S
$$

un homomorfismo de anillos. Considerando $f$ como homomorfismo entre los grupos aditivos, su imagen

$$
\operatorname{im}f\subseteq S
$$

determina un subanillo de $\mathcal S$.

#### Demostración {#talg-prf-00053}

Como

$$
f(1_R)=1_S,
$$

se tiene

$$
1_S\in\operatorname{im}f.
$$

Sean $x,y\in\operatorname{im}f$. Existen $a,b\in R$ tales que

$$
x=f(a),
\qquad
y=f(b).
$$

Por la [Proposición 17.2.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00032),

$$
-f(b)=f(-b),
$$

y entonces

$$
x-y
=
f(a)-f(b)
=
f(a)+f(-b)
=
f(a-b)
\in\operatorname{im}f.
$$

Asimismo,

$$
xy
=
f(a)f(b)
=
f(ab)
\in\operatorname{im}f.
$$

El [Teorema 17.1.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-thm-00009) implica que $\operatorname{im}f$ determina un subanillo de $S$.

$\square$

---

### Corolario 17.3.2 — Con codominio no trivial, el núcleo no es un subanillo {#talg-cor-00008}

Sea

$$
f:R\to S
$$

un homomorfismo de anillos y supongamos que el anillo codominio $\mathcal S$ es no trivial. Entonces, considerando $f$ como homomorfismo de los grupos aditivos,

$$
\boxed{\ker f\text{ no determina un subanillo de }R.}
$$

#### Demostración {#talg-prf-00054}

Si $1_R\in\ker f$, por la definición de núcleo se tendría

$$
f(1_R)=0_S.
$$

Pero, por ser $f$ un homomorfismo de anillos,

$$
f(1_R)=1_S.
$$

Luego

$$
0_S=1_S,
$$

en contradicción con la no trivialidad de $\mathcal S$.

Por tanto,

$$
1_R\notin\ker f.
$$

Todo subanillo de $R$ contiene $1_R$ por la [Definición 17.1.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00038). En consecuencia, $\ker f$ no determina un subanillo de $R$.

$\square$

> **Transición estructural.** El núcleo sigue siendo un subgrupo del grupo aditivo por la teoría general de homomorfismos de grupos, pero la convención unital impide tratarlo como subanillo cuando el codominio es no trivial. La estructura correcta para describir núcleos de homomorfismos de anillos será la noción de **ideal**, que se introduce a continuación.

---

## 17.4. Cierre deductivo

Queda cerrada la cadena

```text
subgrupo aditivo
+
submonoide multiplicativo unital
        ↓
subanillo
        ↓
criterio: 1, diferencias y productos
        ↓
herencia de 0 y 1
        ↓
homomorfismo de anillos unital
        ↓
preservación de 0, opuestos y unidades
        ↓
imagen = subanillo
        ↓
núcleo ≠ subanillo en codominio no trivial
        ↓
ideales
```

No se ha utilizado el axioma de elección.

El siguiente nodo canónico será

[Definición 18.1.1 — Ideal izquierdo, derecho y bilateral](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00040).

---

[← **Capítulo 16 — No trivialidad y divisores de cero**](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md) · [**Capítulo 18 — Ideales** →](tratado-de-algebra-capitulo-18-ideales.md)
