---
title: 'Tratado moderno de Álgebra — Capítulo 11: Clases laterales y caracterización de la normalidad'
description: Capítulo del Tratado moderno de Álgebra dedicado a clases laterales y caracterización de la normalidad, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0036
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
- MA-BCH-0035
related:
- MA-BOK-0007
- MA-BCH-0035
- MA-BCH-0037
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 11 — Clases laterales y caracterización de la normalidad

## 11.0. Propósito y posición deductiva

El capítulo anterior introdujo la normalidad mediante estabilidad bajo conjugación, deliberadamente antes de hablar de clases laterales. Ahora construiremos esas clases como subconjuntos explícitamente definidos del grupo ambiente y demostraremos las propiedades que hacen posible el paso posterior a los cocientes.

La secuencia deductiva será

$$
\text{subgrupo}
\longrightarrow
\text{clases laterales izquierda y derecha}
\longrightarrow
\text{criterios de igualdad}
\longrightarrow
\text{igualdad o disjunción}
\longrightarrow
\text{normalidad}\iff gN=Ng.
$$

No se definirá todavía el grupo cociente $G/N$. En particular, no se multiplicarán clases laterales antes de demostrar en un capítulo posterior que la operación correspondiente está bien definida.

---

## 11.1. Construcción de las clases laterales

### Definición 11.1.1 — Clases laterales izquierda y derecha {#talg-def-00027}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo, sea $H\subseteq G$ un subconjunto que determina un subgrupo de $\mathcal G$ y sea $g\in G$.

La **clase lateral izquierda de $H$ determinada por $g$** es el subconjunto de $G$

$$
\{x\in G:\exists h\in H,\ x=g\star h\}.
$$

La **clase lateral derecha de $H$ determinada por $g$** es el subconjunto de $G$

$$
\{x\in G:\exists h\in H,\ x=h\star g\}.
$$

Ambos conjuntos existen por Separación aplicada a $G$.

La definición no identifica una clase lateral con un elemento ni con una clase de equivalencia previamente construida: en este punto se trata literalmente de subconjuntos de $G$ definidos por las fórmulas anteriores.

---

### Notación 11.1.2 — $gH$ y $Hg$ {#talg-not-00009}

En la situación de la [Definición 11.1.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-def-00027) escribiremos

$$
gH
:=
\{x\in G:\exists h\in H,\ x=g\star h\}
$$

y

$$
Hg
:=
\{x\in G:\exists h\in H,\ x=h\star g\}.
$$

El orden de los símbolos es significativo: $gH$ denota una clase lateral izquierda y $Hg$ una clase lateral derecha.

---

### Proposición 11.1.3 — El representante pertenece a sus clases laterales {#talg-pro-00019}

Sea $H$ un subgrupo de $\mathcal G=\langle G,\star\rangle$ y sea $g\in G$. Entonces

$$
g\in gH
\qquad\text{y}\qquad
g\in Hg.
$$

En particular, toda clase lateral izquierda o derecha es no vacía.

#### Demostración {#talg-prf-00024}

Como $H$ determina un subgrupo, el neutro ambiente $e_{\mathcal G}$ pertenece a $H$. Por las leyes de neutro,

$$
g=g\star e_{\mathcal G}
$$

y

$$
g=e_{\mathcal G}\star g.
$$

La primera igualdad muestra que $g\in gH$ y la segunda que $g\in Hg$. $\square$

---

## 11.2. Criterios de igualdad

### Teorema 11.2.1 — Criterios de igualdad de clases laterales {#talg-thm-00003}

Sea $H$ un subgrupo de $\mathcal G=\langle G,\star\rangle$ y sean $g,k\in G$. Entonces:

1. para clases laterales izquierdas,
   $$
   gH=kH
   \iff
   k^{-1}\star g\in H;
   $$
2. para clases laterales derechas,
   $$
   Hg=Hk
   \iff
   g\star k^{-1}\in H.
   $$

#### Demostración {#talg-prf-00025}

**Clases izquierdas.** Supongamos primero

$$
gH=kH.
$$

Por la [Proposición 11.1.3](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-pro-00019), $g\in gH$, y por la igualdad supuesta $g\in kH$. Por definición de clase lateral existe $h\in H$ tal que

$$
g=k\star h.
$$

Multiplicando a la izquierda por $k^{-1}$ y usando asociatividad, inverso y neutro,

$$
k^{-1}\star g
=
k^{-1}\star(k\star h)
=
(k^{-1}\star k)\star h
=
h\in H.
$$

Recíprocamente, supongamos

$$
a:=k^{-1}\star g\in H.
$$

Entonces

$$
k\star a
=
k\star(k^{-1}\star g)
=
(k\star k^{-1})\star g
=
g.
$$

Sea $x\in gH$. Existe $h\in H$ con $x=g\star h$. Por la igualdad anterior,

$$
x
=
(k\star a)\star h
=
k\star(a\star h).
$$

Como $a,h\in H$ y $H$ es cerrado bajo la operación, $a\star h\in H$. Por tanto $x\in kH$, y así

$$
gH\subseteq kH.
$$

Como $H$ es subgrupo, $a^{-1}\in H$. Además,

$$
g\star a^{-1}
=
(k\star a)\star a^{-1}
=
k\star(a\star a^{-1})
=
k.
$$

El mismo argumento, ahora usando $a^{-1}\in H$, da

$$
kH\subseteq gH.
$$

Por Extensionalidad,

$$
gH=kH.
$$

**Clases derechas.** La demostración es simétrica. Si $Hg=Hk$, entonces $g\in Hk$, de modo que existe $h\in H$ con

$$
g=h\star k.
$$

Multiplicando a la derecha por $k^{-1}$,

$$
g\star k^{-1}
=
(h\star k)\star k^{-1}
=
h\star(k\star k^{-1})
=
h\in H.
$$

Recíprocamente, supongamos

$$
b:=g\star k^{-1}\in H.
$$

Entonces

$$
b\star k
=
(g\star k^{-1})\star k
=
g\star(k^{-1}\star k)
=
g.
$$

Si $x\in Hg$, existe $h\in H$ con $x=h\star g$. Luego

$$
x
=
h\star(b\star k)
=
(h\star b)\star k.
$$

Como $h\star b\in H$, resulta $x\in Hk$, y por tanto $Hg\subseteq Hk$. Como $b^{-1}\in H$ y

$$
b^{-1}\star g=k,
$$

el mismo argumento da $Hk\subseteq Hg$. Por Extensionalidad,

$$
Hg=Hk.
$$

Quedan demostradas ambas equivalencias. $\square$

---

### Corolario 11.2.2 — Dos clases laterales del mismo lado son iguales o disjuntas {#talg-cor-00003}

Sea $H$ un subgrupo de $\mathcal G=\langle G,\star\rangle$ y sean $g,k\in G$. Entonces:

1. o bien $gH=kH$, o bien $gH\cap kH=\varnothing$;
2. o bien $Hg=Hk$, o bien $Hg\cap Hk=\varnothing$.

#### Demostración {#talg-prf-00026}

Para las clases laterales izquierdas aplicamos LEM a la proposición

$$
\exists x\in gH\cap kH.
$$

Si existe tal $x$, entonces $x\in gH$ y $x\in kH$. De $x\in gH$ existe $h_1\in H$ con $x=g\star h_1$, y por tanto

$$
g^{-1}\star x=h_1\in H.
$$

Por el [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003), aplicado a $xH$ y $gH$, se obtiene $xH=gH$. Análogamente, de $x\in kH$ obtenemos $xH=kH$. Luego

$$
gH=kH.
$$

Si, por el contrario,

$$
\neg\exists x\in gH\cap kH,
$$

entonces ningún elemento pertenece a $gH\cap kH$; por Extensionalidad,

$$
gH\cap kH=\varnothing.
$$

Así,

$$
gH=kH\quad\lor\quad gH\cap kH=\varnothing.
$$

El argumento para clases laterales derechas es idéntico, aplicando LEM a $\exists x\in Hg\cap Hk$ y usando la segunda equivalencia del [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003). Concluimos

$$
Hg=Hk\quad\lor\quad Hg\cap Hk=\varnothing.
$$

No se ha utilizado elección. El único principio clásico sustantivo es LEM aplicado a la existencia de un elemento en cada intersección. $\square$

> **Lectura conjuntista.** Cada elemento de $G$ pertenece a su propia clase lateral por la [Proposición 11.1.3](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-pro-00019), y dos clases del mismo lado nunca se solapan parcialmente: si comparten un elemento, coinciden por completo. Esto prepara la futura construcción de un cociente sin haber introducido todavía el conjunto cociente.

---

### Lema 11.2.3 — Intersección habitada de clases laterales implica igualdad {#talg-lem-00005}

Sea $H$ un subgrupo de $\mathcal G=\langle G,\star\rangle$ y sean $g,k\in G$. Entonces:

1. si $\exists x\in gH\cap kH$, entonces $gH=kH$;
2. si $\exists x\in Hg\cap Hk$, entonces $Hg=Hk$.

#### Demostración {#talg-prf-00089}

Para la primera afirmación, supongamos

$$
\exists x\in gH\cap kH.
$$

Por eliminación existencial ordinaria tomamos localmente un testigo $x\in gH\cap kH$. Entonces $x\in gH$ y $x\in kH$. Como $x\in gH$, existe $h_1\in H$ con $x=g\star h_1$, de donde

$$
g^{-1}\star x=h_1\in H.
$$

Por el [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003), $xH=gH$. Del mismo modo, $xH=kH$. Por transitividad de la igualdad,

$$
gH=kH.
$$

Para la segunda afirmación, si $x\in Hg\cap Hk$, entonces $x\star g^{-1}\in H$ y $x\star k^{-1}\in H$. La segunda equivalencia del [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003) da

$$
Hx=Hg,\qquad Hx=Hk,
$$

y por tanto $Hg=Hk$.

No se ha utilizado lógica clásica sustantiva ni elección. $\square$

> **Uso deductivo.** Éste es el resultado que debe emplearse cuando una construcción posterior ya exhibe un elemento común de dos clases. La disyunción clásica el [Corolario 11.2.2](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-cor-00003) queda reservada para contextos donde realmente se necesite «iguales o disjuntas».

---

## 11.3. Normalidad y coincidencia de clases laterales

### Teorema 11.3.1 — Caracterización de la normalidad por clases laterales {#talg-thm-00004}

Sea $N$ un subgrupo de $\mathcal G=\langle G,\star\rangle$. Son equivalentes:

1. $N\trianglelefteq G$;
2. para todo $g\in G$,
   $$
   gN=Ng.
   $$

#### Demostración {#talg-prf-00027}

**$(1)\Rightarrow(2)$.** Supongamos $N\trianglelefteq G$ y sea $g\in G$.

Sea $x\in gN$. Entonces existe $n\in N$ tal que

$$
x=g\star n.
$$

Por normalidad,

$$
m:=(g\star n)\star g^{-1}\in N.
$$

Usando asociatividad, inverso y neutro,

$$
m\star g
=
\bigl((g\star n)\star g^{-1}\bigr)\star g
=
(g\star n)\star(g^{-1}\star g)
=
g\star n
=
x.
$$

Como $m\in N$, se sigue que $x\in Ng$. Por tanto,

$$
gN\subseteq Ng.
$$

Para la inclusión inversa, sea $y\in Ng$. Existe $n\in N$ tal que

$$
y=n\star g.
$$

Aplicamos la normalidad al elemento $g^{-1}\in G$ y a $n\in N$:

$$
(g^{-1}\star n)\star(g^{-1})^{-1}\in N.
$$

En el grupo $\mathcal G$, $g$ es un inverso bilateral de $g^{-1}$; por unicidad del inverso ([Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002)),

$$
(g^{-1})^{-1}=g.
$$

Definamos

$$
r:=(g^{-1}\star n)\star g\in N.
$$

Entonces

$$
g\star r
=
g\star\bigl((g^{-1}\star n)\star g\bigr)
=
(g\star g^{-1})\star(n\star g)
=
n\star g
=
y.
$$

Así $y\in gN$ y, por tanto,

$$
Ng\subseteq gN.
$$

Por Extensionalidad, $gN=Ng$.

**$(2)\Rightarrow(1)$.** Supongamos ahora que

$$
\forall g\in G,\qquad gN=Ng.
$$

Sean $g\in G$ y $n\in N$. Como $g\star n\in gN$ y $gN=Ng$, existe $m\in N$ tal que

$$
g\star n=m\star g.
$$

Multiplicando a la derecha por $g^{-1}$,

$$
(g\star n)\star g^{-1}
=
(m\star g)\star g^{-1}
=
m\star(g\star g^{-1})
=
m\in N.
$$

Por la [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026), $N$ es normal en $G$. $\square$

---

## 11.4. Lectura estructural

Las clases laterales proporcionan ahora una segunda formulación de la normalidad:

$$
N\trianglelefteq G
\iff
\forall g\in G,\ gN=Ng.
$$

La definición original por conjugación sigue siendo lógicamente anterior; el [Teorema 11.3.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00004) demuestra que, una vez construidas las clases laterales, ambas formulaciones coinciden.

También queda establecida la geometría conjuntista mínima necesaria para un cociente: cada elemento pertenece a una clase lateral y dos clases laterales del mismo lado son iguales o disjuntas.

El paso siguiente exigirá una decisión fundacional adicional. Antes de definir formalmente $G/N$ se abrirá una interfaz mínima con la infraestructura ya cerrada de relaciones de equivalencia y conjuntos cociente, o bien se construirá explícitamente una relación equivalente dentro de este tratado. Esa decisión deberá preservar la aciclicidad intertratados y evitar duplicar infraestructura conjuntista ya demostrada.

---

[← **Capítulo 10 — Subgrupos normales**](tratado-de-algebra-capitulo-10-subgrupos-normales.md) · [**Capítulo 12 — Cocientes de grupos** →](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md)
