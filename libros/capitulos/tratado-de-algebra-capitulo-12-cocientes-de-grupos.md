---
title: 'Tratado moderno de Álgebra — Capítulo 12: Cocientes de grupos'
description: Capítulo del Tratado moderno de Álgebra dedicado a cocientes de grupos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0037
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
- MA-BCH-0036
related:
- MA-BOK-0007
- MA-BCH-0036
- MA-BCH-0038
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 12 — Cocientes de grupos

## 12.0. Propósito y posición deductiva

Ya disponemos de subgrupos normales y de clases laterales. Falta realizar el paso decisivo: convertir las clases laterales en elementos de un nuevo conjunto y demostrar que la multiplicación de representantes produce una operación independiente de la representación elegida.

La cadena deductiva será

$$
\text{clases laterales}
\longrightarrow
\text{equivalencia inducida}
\longrightarrow
G/H
\longrightarrow
\text{normalidad}
\longrightarrow
\text{producto bien definido}
\longrightarrow
\mathcal G/N\text{ grupo}
\longrightarrow
q_N:G\to G/N.
$$

El punto crítico del capítulo es la **buena definición**. La fórmula informal

$$
(gN)(hN)=(g\star h)N
$$

no será aceptada como definición hasta demostrar que cambiar $g$ o $h$ por otros representantes de las mismas clases produce exactamente la misma clase resultado.

---

## 12.1. La equivalencia inducida por un subgrupo

### Definición 12.1.1 — Relación asociada a las clases laterales izquierdas {#talg-def-00028}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo y sea $H\subseteq G$ un subconjunto que determina un subgrupo. Definimos una relación $\sim_H$ sobre $G$ por

$$
g\sim_H k
\quad\Longleftrightarrow\quad
gH=kH.
$$

Conjuntistamente,

$$
\sim_H
:=
\{\langle g,k\rangle\in G\times G:gH=kH\},
$$

que existe por Separación. Por [`TALG-IMP-00003`](tratado-de-algebra-relaciones-equivalencia-cocientes.md#talg-imp-00003), esto es una relación binaria sobre $G$.

La orientación mediante clases **izquierdas** queda fijada en esta definición. Para subgrupos normales, las clases izquierdas y derechas coinciden por el [Teorema 11.3.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00004).

---

### Proposición 12.1.2 — La relación $\sim_H$ es una equivalencia {#talg-pro-00020}

Para todo subgrupo $H$ de $\mathcal G$, la relación $\sim_H$ es una relación de equivalencia sobre $G$.

#### Demostración {#talg-prf-00028}

La prueba utiliza únicamente las propiedades lógicas de la igualdad de conjuntos.

- **Reflexividad.** Para todo $g\in G$, $gH=gH$, luego $g\sim_H g$.
- **Simetría.** Si $g\sim_H k$, entonces $gH=kH$. Por simetría de la igualdad, $kH=gH$, luego $k\sim_H g$.
- **Transitividad.** Si $g\sim_H k$ y $k\sim_H \ell$, entonces $gH=kH$ y $kH=\ell H$. Por transitividad de la igualdad, $gH=\ell H$, luego $g\sim_H\ell$.

Por la definición importada de relación de equivalencia en [`TALG-IMP-00003`](tratado-de-algebra-relaciones-equivalencia-cocientes.md#talg-imp-00003), $\sim_H$ es una equivalencia sobre $G$. $\square$

---

### Proposición 12.1.3 — Las clases de $\sim_H$ son exactamente las clases laterales {#talg-pro-00021}

Sea $H$ un subgrupo de $\mathcal G$ y sea $g\in G$. Entonces

$$
[g]_{\sim_H}=gH.
$$

#### Demostración {#talg-prf-00029}

Sea $x\in G$. Por definición de clase de equivalencia y de $\sim_H$,

$$
x\in[g]_{\sim_H}
\iff
x\sim_H g
\iff
xH=gH.
$$

Por el [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003),

$$
xH=gH
\iff
g^{-1}\star x\in H.
$$

Si $g^{-1}\star x\in H$, llamando

$$
h:=g^{-1}\star x\in H,
$$

tenemos, por asociatividad, inverso y neutro,

$$
g\star h
=
g\star(g^{-1}\star x)
=
(g\star g^{-1})\star x
=
x,
$$

luego $x\in gH$.

Recíprocamente, si $x\in gH$, existe $h\in H$ con $x=g\star h$. Entonces

$$
g^{-1}\star x
=
g^{-1}\star(g\star h)
=
(g^{-1}\star g)\star h
=
h\in H,
$$

y por el [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003), $xH=gH$, es decir, $x\in[g]_{\sim_H}$.

Hemos probado

$$
x\in[g]_{\sim_H}
\iff
x\in gH
$$

para todo $x$. Por Extensionalidad,

$$
[g]_{\sim_H}=gH.
$$

$\square$

---

## 12.2. El espacio de clases laterales

### Definición 12.2.1 — Espacio de clases laterales $G/H$ {#talg-def-00029}

Sea $H$ un subgrupo de $\mathcal G=\langle G,\star\rangle$. Como $\sim_H$ es una relación de equivalencia, definimos

$$
G/H
:=
G/{\sim_H}.
$$

Por la construcción importada mediante [`TALG-IMP-00003`](tratado-de-algebra-relaciones-equivalencia-cocientes.md#talg-imp-00003), $G/H$ es un conjunto y

$$
G/H\subseteq\mathcal P(G).
$$

Usando la [Proposición 12.1.3](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00021), sus elementos son precisamente las clases laterales izquierdas:

$$
G/H
=
\{gH:g\in G\}.
$$

La igualdad anterior es descriptiva; la definición conjuntista canónica sigue siendo el cociente $G/{\sim_H}$.

---

### Notación 12.2.2 — Cociente conjuntista por un subgrupo {#talg-not-00010}

La expresión

$$
G/H
$$

denota en este punto **sólo el conjunto de clases laterales izquierdas**. Si $H$ no es normal, no se presupone ninguna operación de grupo sobre este conjunto.

---

## 12.3. Normalidad y buena definición del producto

### Proposición 12.3.1 — Independencia de representantes del producto de clases {#talg-pro-00022}

Sea $N\trianglelefteq G$. Si

$$
gN=g'N
\qquad\text{y}\qquad
hN=h'N,
$$

entonces

$$
(g\star h)N=(g'\star h')N.
$$

#### Demostración {#talg-prf-00030}

Por el [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003), de $gN=g'N$ se sigue

$$
a:=(g')^{-1}\star g\in N.
$$

Por tanto

$$
g=g'\star a.
$$

Análogamente, de $hN=h'N$ se sigue

$$
b:=(h')^{-1}\star h\in N,
\qquad
h=h'\star b.
$$

Como $N$ es normal, el [Teorema 11.3.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00004) da

$$
h'N=Nh'.
$$

Puesto que $a\in N$, tenemos

$$
a\star h'\in Nh'=h'N.
$$

Por definición de $h'N$, existe $c\in N$ tal que

$$
a\star h'=h'\star c.
$$

Entonces

$$
\begin{aligned}
g\star h
&=(g'\star a)\star(h'\star b)\\
&=g'\star\bigl((a\star h')\star b\bigr)\\
&=g'\star\bigl((h'\star c)\star b\bigr)\\
&=(g'\star h')\star(c\star b).
\end{aligned}
$$

Como $c,b\in N$ y $N$ es un subgrupo,

$$
c\star b\in N.
$$

Por tanto

$$
g\star h\in(g'\star h')N.
$$

Por la [Proposición 11.1.3](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-pro-00019), también

$$
g\star h\in(g\star h)N.
$$

Las dos clases laterales $(g\star h)N$ y $(g'\star h')N$ tienen, pues, un elemento común, a saber $g\star h$. Por el [Lema 11.2.3](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-lem-00005), deben coincidir:

$$
(g\star h)N=(g'\star h')N.
$$

$\square$

> **Punto estructural.** Éste es el lugar exacto donde la normalidad deja de ser una propiedad auxiliar y se convierte en una condición de descenso: permite mover un factor de $N$ a través de un representante del grupo sin abandonar $N$.

---

### Lema 12.3.2 — Existencia y unicidad de la operación cociente {#talg-lem-00002}

Sea $N\trianglelefteq G$. Existe una única operación binaria

$$
\star_N:(G/N)\times(G/N)\to G/N
$$

tal que, para todos $g,h\in G$,

$$
(gN)\star_N(hN)=(g\star h)N.
$$

#### Demostración {#talg-prf-00031}

Consideremos el subconjunto

$$
\Gamma_N
\subseteq
\bigl((G/N)\times(G/N)\bigr)\times(G/N)
$$

dado por

$$
\left\langle\langle C,D\rangle,E\right\rangle\in\Gamma_N
$$

si y sólo si existen $g,h\in G$ tales que

$$
C=gN,
\qquad
D=hN,
\qquad
E=(g\star h)N.
$$

El ambiente cartesiano existe por la interfaz [`TALG-IMP-00001`](tratado-de-algebra-capitulo-0-interfaz-fundacional.md#talg-imp-00001), y $\Gamma_N$ existe por Separación.

Sea $\langle C,D\rangle\in(G/N)\times(G/N)$. Por la definición de $G/N$ y la [Proposición 12.1.3](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00021), existen $g,h\in G$ con

$$
C=gN,
\qquad
D=hN.
$$

Entonces

$$
E:=(g\star h)N\in G/N,
$$

y

$$
\left\langle\langle C,D\rangle,E\right\rangle\in\Gamma_N.
$$

Por tanto existe al menos una salida.

Para la unicidad, supongamos que también

$$
C=g'N,
\qquad
D=h'N
$$

produce

$$
E'=(g'\star h')N.
$$

Entonces

$$
gN=g'N,
\qquad
hN=h'N,
$$

y la [Proposición 12.3.1](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00022) implica

$$
(g\star h)N=(g'\star h')N.
$$

Por tanto $E=E'$. Así $\Gamma_N$ es el grafo de una función

$$
\star_N:(G/N)\times(G/N)\to G/N.
$$

La fórmula exigida se cumple por construcción.

Finalmente, cualquier otra operación con esa misma fórmula coincide con $\star_N$ en todo par $\langle gN,hN\rangle$, y todo elemento de $(G/N)\times(G/N)$ tiene esa forma. Por extensionalidad de funciones, la operación es única. $\square$

> No se ha elegido un representante de cada clase. Para cada par de clases se usa la existencia local de representantes, y la [Proposición 12.3.1](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00022) demuestra que el resultado no depende de cuáles sean. No interviene el axioma de elección.

---

### Notación 12.3.3 — Multiplicación cociente {#talg-not-00011}

La única operación proporcionada por el [Lema 12.3.2](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-lem-00002) se denotará por

$$
\star_N.
$$

Cuando no haya riesgo de confusión podrá omitirse el subíndice en cálculos locales, pero el registro canónico conservará $\star_N$.

---

## 12.4. El grupo cociente

### Definición 12.4.1 — Estructura cociente {#talg-def-00030}

Sea $N\trianglelefteq G$. Definimos la **estructura cociente** de

$$
\mathcal G=\langle G,\star\rangle
$$

por $N$ como

$$
\mathcal G/N
:=
\langle G/N,\star_N\rangle.
$$

En esta definición todavía no se presupone que la estructura sea un grupo; ésa será la conclusión del teorema siguiente.

---

### Teorema 12.4.2 — El cociente por un subgrupo normal es un grupo {#talg-thm-00005}

Sea $N\trianglelefteq G$. Entonces

$$
\mathcal G/N
=
\langle G/N,\star_N\rangle
$$

es un grupo.

#### Demostración {#talg-prf-00032}

La clausura ya está incorporada en el tipo de la operación

$$
\star_N:(G/N)\times(G/N)\to G/N.
$$

**Asociatividad.** Sean $gN,hN,kN\in G/N$. Entonces

$$
\begin{aligned}
\bigl((gN)\star_N(hN)\bigr)\star_N(kN)
&=((g\star h)N)\star_N(kN)\\
&=((g\star h)\star k)N\\
&=(g\star(h\star k))N\\
&=(gN)\star_N((h\star k)N)\\
&=(gN)\star_N\bigl((hN)\star_N(kN)\bigr).
\end{aligned}
$$

**Neutro.** Sea $e_{\mathcal G}$ el neutro de $\mathcal G$. Como $e_{\mathcal G}\in G$, la clase $e_{\mathcal G}N$ pertenece a $G/N$. Para todo $gN\in G/N$,

$$
(e_{\mathcal G}N)\star_N(gN)
=(e_{\mathcal G}\star g)N
=gN,
$$

y

$$
(gN)\star_N(e_{\mathcal G}N)
=(g\star e_{\mathcal G})N
=gN.
$$

Por tanto $e_{\mathcal G}N$ es neutro en el cociente.

**Inversos.** Para $gN\in G/N$, consideremos $g^{-1}N\in G/N$. Entonces

$$
(gN)\star_N(g^{-1}N)
=(g\star g^{-1})N
=e_{\mathcal G}N,
$$

y

$$
(g^{-1}N)\star_N(gN)
=(g^{-1}\star g)N
=e_{\mathcal G}N.
$$

Así cada elemento posee inverso bilateral.

Por la [Definición 4.2.1](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-def-00008), $\mathcal G/N$ es un grupo. $\square$

> En adelante, cuando $N\trianglelefteq G$, llamaremos **grupo cociente** a $\mathcal G/N$.

---

## 12.5. La proyección canónica algebraica

### Definición 12.5.1 — Proyección canónica del grupo cociente {#talg-def-00031}

Sea $N\trianglelefteq G$. Definimos

$$
q_N:G\to G/N,
\qquad
q_N(g):=gN.
$$

Conjuntistamente, su grafo es

$$
\{\langle g,C\rangle\in G\times(G/N):C=gN\},
$$

que existe por Separación. Para cada $g\in G$ existe una única salida, a saber $gN$; por tanto el grafo determina una función $G\to G/N$. La salida está bien tipada porque $gN$ es precisamente una clase de la equivalencia $\sim_N$, por la [Proposición 12.1.3](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00021).

Esta construcción se realiza en Álgebra y no importa la proyección canónica general `TA-DEF-00023`.

---

### Proposición 12.5.2 — La proyección es sobreyectiva, homomórfica y tiene núcleo $N$ {#talg-pro-00023}

Sea $N\trianglelefteq G$. Entonces

$$
q_N:G\to G/N
$$

es un homomorfismo sobreyectivo de grupos y

$$
\ker q_N=N.
$$

#### Demostración {#talg-prf-00033}

**Homomorfismo.** Para $g,h\in G$,

$$
\begin{aligned}
q_N(g\star h)
&=(g\star h)N\\
&=(gN)\star_N(hN)\\
&=q_N(g)\star_N q_N(h).
\end{aligned}
$$

Por la [Definición 7.4.1](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019), $q_N$ es un homomorfismo de grupos.

**Sobreyectividad.** Sea $C\in G/N$. Por la definición del cociente y la [Proposición 12.1.3](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00021), existe $g\in G$ tal que

$$
C=gN=q_N(g).
$$

Por tanto $q_N$ es sobreyectiva.

**Núcleo.** El neutro del grupo cociente es

$$
e_{\mathcal G}N.
$$

Además,

$$
e_{\mathcal G}N=N.
$$

En efecto, $x\in e_{\mathcal G}N$ si y sólo si existe $n\in N$ con $x=e_{\mathcal G}\star n=n$, lo cual equivale a $x\in N$; por Extensionalidad ambos conjuntos son iguales.

Para $g\in G$,

$$
\begin{aligned}
g\in\ker q_N
&\iff q_N(g)=e_{\mathcal G}N\\
&\iff gN=e_{\mathcal G}N\\
&\iff e_{\mathcal G}^{-1}\star g\in N\\
&\iff g\in N.
\end{aligned}
$$

Para la última equivalencia, $e_{\mathcal G}$ es inverso de sí mismo porque $e_{\mathcal G}\star e_{\mathcal G}=e_{\mathcal G}$; por la unicidad del inverso la [Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002), $e_{\mathcal G}^{-1}=e_{\mathcal G}$. Luego $e_{\mathcal G}^{-1}\star g=g$.

Por Extensionalidad,

$$
\ker q_N=N.
$$

$\square$

---

## 12.6. Lectura estructural

El capítulo ha separado cuidadosamente cuatro niveles que a menudo se colapsan informalmente:

1. una clase lateral $gH$ es primero un subconjunto de $G$;
2. la igualdad de clases laterales induce una relación de equivalencia $\sim_H$;
3. el conjunto $G/H$ es el conjunto de esas clases, exista o no una estructura de grupo sobre él;
4. sólo cuando $N$ es normal la multiplicación de representantes desciende a una operación binaria bien definida $\star_N$ sobre $G/N$.

Así, la normalidad puede leerse como una condición de **congruencia algebraica** para la multiplicación del grupo.

La proyección

$$
q_N:G\to G/N
$$

resume el mecanismo:

$$
q_N(g\star h)=q_N(g)\star_Nq_N(h),
\qquad
\ker q_N=N,
\qquad
q_N\text{ es sobreyectiva}.
$$

Esto deja preparada la formulación del primer teorema de isomorfía.

---

[← **Capítulo 11 — Clases laterales y caracterización de la normalidad**](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md) · [**Capítulo 13 — Primer teorema de isomorfía para grupos** →](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md)
