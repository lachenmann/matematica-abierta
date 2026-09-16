---
title: 'Tratado moderno de Álgebra — Capítulo 13: Primer teorema de isomorfía para grupos'
description: Capítulo del Tratado moderno de Álgebra dedicado a primer teorema de isomorfía para grupos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0038
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
- MA-BCH-0037
related:
- MA-BOK-0007
- MA-BCH-0037
- MA-BCH-0039
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 13 — Primer teorema de isomorfía para grupos

## 13.0. Propósito y posición deductiva

Ya disponemos de todas las piezas que el primer teorema de isomorfía necesita: núcleo, imagen, normalidad del núcleo, grupos cociente e isomorfismos. El objetivo de este capítulo es mostrar que esas piezas no son construcciones independientes, sino partes de una misma estructura.

Sea

$$
f:G\to H
$$

un homomorfismo de grupos. El núcleo registra exactamente qué elementos de $G$ se vuelven indistinguibles bajo $f$; el cociente $G/\ker f$ identifica precisamente esos elementos; y la imagen reúne exactamente los valores que $f$ alcanza. El teorema demostrará que, después de realizar esas identificaciones, no queda pérdida adicional de información:

$$
G/\ker f\cong \operatorname{im}f.
$$

El punto crítico no es la fórmula informal

$$
g\ker f\longmapsto f(g),
$$

sino demostrar que define realmente una función sobre clases sin elegir un representante privilegiado de cada una.

---

## 13.1. Primer teorema de isomorfía

### Teorema 13.1.1 — Primer teorema de isomorfía para grupos {#talg-thm-00006}

Sean

$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

grupos, y sea

$$
f:G\to H
$$

un homomorfismo de grupos. Escribamos

$$
K:=\ker f.
$$

Entonces $K\trianglelefteq G$ y existe una única función

$$
\overline f:G/K\longrightarrow \operatorname{im}f
$$

que satisface

$$
\overline f(gK)=f(g)
\qquad(g\in G).
$$

Además, $\overline f$ es un isomorfismo de grupos de

$$
\mathcal G/K
$$

sobre la estructura de subgrupo inducida

$$
\mathcal H|_{\operatorname{im}f}.
$$

En particular,

$$
\boxed{
\mathcal G/\ker f
\cong
\mathcal H|_{\operatorname{im}f}
}.
$$

#### Demostración {#talg-prf-00034}

Por la [Proposición 10.2.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-pro-00017), el núcleo $K=\ker f$ es un subgrupo normal de $G$. Por el [Teorema 12.4.2](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-thm-00005), el cociente

$$
\mathcal G/K
$$

es por tanto un grupo. Por la [Proposición 9.2.3](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-pro-00015), $\operatorname{im}f$ determina un subgrupo de $\mathcal H$, cuya estructura inducida escribimos

$$
\mathcal H|_{\operatorname{im}f}.
$$

La demostración se divide en cinco pasos.

### Paso 1. Invariancia respecto de representantes

Supongamos

$$
gK=hK.
$$

Por el [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003),

$$
h^{-1}\star g\in K=\ker f.
$$

Por definición de núcleo,

$$
f(h^{-1}\star g)=e_{\mathcal H}.
$$

Como $f$ es homomorfismo y preserva inversos por la [Proposición 7.4.3](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008),

$$
f(h)^{-1}\diamond f(g)=e_{\mathcal H}.
$$

Multiplicando a la izquierda por $f(h)$ y usando asociatividad, inverso y neutro en $\mathcal H$,

$$
\begin{aligned}
f(g)
&=(f(h)\diamond f(h)^{-1})\diamond f(g)\\
&=f(h)\diamond\bigl(f(h)^{-1}\diamond f(g)\bigr)\\
&=f(h)\diamond e_{\mathcal H}\\
&=f(h).
\end{aligned}
$$

Por tanto,

$$
\boxed{gK=hK\Longrightarrow f(g)=f(h)}.
$$

Ésta es la buena definición que necesitamos.

### Paso 2. Construcción de $\overline f$ sin elección de representantes

Consideremos el subconjunto

$$
\Gamma_{\overline f}
:=
\left\{
\langle C,y\rangle\in (G/K)\times\operatorname{im}f:
\exists g\in G\;(C=gK\land y=f(g))
\right\}.
$$

Existe por producto cartesiano y Separación.

Sea $C\in G/K$. Por la descripción de $G/K$ como conjunto de clases laterales, existe $g\in G$ tal que

$$
C=gK.
$$

Entonces $f(g)\in\operatorname{im}f$ y

$$
\langle C,f(g)\rangle\in\Gamma_{\overline f}.
$$

Así, el grafo es total sobre $G/K$.

Para la funcionalidad, supongamos

$$
\langle C,y\rangle,
\langle C,z\rangle
\in\Gamma_{\overline f}.
$$

Existen $g,h\in G$ con

$$
C=gK=hK,
\qquad
y=f(g),
\qquad
z=f(h).
$$

Por el Paso 1,

$$
f(g)=f(h),
$$

y por tanto $y=z$.

Así, $\Gamma_{\overline f}$ es el grafo de una función

$$
\overline f:G/K\to\operatorname{im}f
$$

que satisface

$$
\overline f(gK)=f(g).
$$

No se ha elegido simultáneamente un representante de cada clase: para cada argumento se usa únicamente la existencia de algún representante, y la funcionalidad garantiza que el valor no depende de cuál sea.

La unicidad también es inmediata. Si

$$
\psi:G/K\to\operatorname{im}f
$$

satisface $\psi(gK)=f(g)$ para todo $g\in G$, entonces, para cualquier $C\in G/K$, existe $g\in G$ con $C=gK$, y

$$
\psi(C)=\psi(gK)=f(g)=\overline f(gK)=\overline f(C).
$$

Por Extensionalidad de funciones, $\psi=\overline f$.

### Paso 3. $\overline f$ es un homomorfismo

Sean $gK,hK\in G/K$. Por la definición de la operación cociente,

$$
(gK)\star_K(hK)=(g\star h)K.
$$

Entonces

$$
\begin{aligned}
\overline f\bigl((gK)\star_K(hK)\bigr)
&=\overline f((g\star h)K)\\
&=f(g\star h)\\
&=f(g)\diamond f(h).
\end{aligned}
$$

Como la operación sobre $\mathcal H|_{\operatorname{im}f}$ es la restricción canónica de $\diamond$, para elementos de la imagen tenemos

$$
f(g)\diamond_{\operatorname{im}f}f(h)
=
f(g)\diamond f(h).
$$

Por consiguiente,

$$
\overline f\bigl((gK)\star_K(hK)\bigr)
=
\overline f(gK)\diamond_{\operatorname{im}f}\overline f(hK),
$$

y $\overline f$ es un homomorfismo de grupos.

### Paso 4. $\overline f$ es sobreyectiva

Sea $y\in\operatorname{im}f$. Por definición de imagen, existe $g\in G$ tal que

$$
y=f(g).
$$

Entonces

$$
y=f(g)=\overline f(gK).
$$

Luego $\overline f$ es sobreyectiva.

### Paso 5. $\overline f$ es inyectiva

Supongamos

$$
\overline f(gK)=\overline f(hK).
$$

Entonces

$$
f(g)=f(h).
$$

Por homomorfía y preservación de inversos,

$$
\begin{aligned}
f(h^{-1}\star g)
&=f(h)^{-1}\diamond f(g)\\
&=f(h)^{-1}\diamond f(h)\\
&=e_{\mathcal H}.
\end{aligned}
$$

Así,

$$
h^{-1}\star g\in\ker f=K.
$$

Por el [Teorema 11.2.1](tratado-de-algebra-capitulo-11-clases-laterales-y-caracterizacion-de-la-normalidad.md#talg-thm-00003), se sigue

$$
gK=hK.
$$

Por tanto, $\overline f$ es inyectiva.

Hemos demostrado que $\overline f$ es un homomorfismo biyectivo entre grupos. Por la [Definición 8.2.3](tratado-de-algebra-capitulo-8-isomorfismos.md#talg-def-00023), es un isomorfismo de grupos. En consecuencia,

$$
\mathcal G/\ker f
\cong
\mathcal H|_{\operatorname{im}f}.
$$

$\square$

> **Lectura estructural.** El núcleo mide exactamente la información que $f$ identifica. Al cocientar por el núcleo se elimina esa redundancia y el homomorfismo resultante ya no colapsa nada: se vuelve inyectivo. La imagen, por su parte, elimina del codominio todo lo que $f$ nunca alcanza. Después de ambas operaciones queda un isomorfismo.

---

## 13.2. Caso sobreyectivo

### Corolario 13.2.1 — Forma sobreyectiva del primer teorema de isomorfía {#talg-cor-00004}

Sea

$$
f:G\to H
$$

un homomorfismo **sobreyectivo** de grupos. Entonces existe un isomorfismo de grupos

$$
\widehat f:G/\ker f\longrightarrow H
$$

caracterizado por

$$
\widehat f(g\ker f)=f(g).
$$

En particular,

$$
\boxed{
\mathcal G/\ker f\cong\mathcal H
}.
$$

#### Demostración {#talg-prf-00035}

Por la [Proposición 9.3.2](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-pro-00016), la sobreyectividad de $f$ equivale a

$$
\operatorname{im}f=H.
$$

No cambiaremos silenciosamente el codominio de la función construida en el [Teorema 13.1.1](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md#talg-thm-00006). Definimos, en cambio, un nuevo grafo

$$
\Gamma_{\widehat f}
:=
\left\{
\langle C,y\rangle\in (G/\ker f)\times H:
\exists g\in G\;(C=g\ker f\land y=f(g))
\right\}.
$$

La invariancia respecto de representantes demostrada en el [Teorema 13.1.1](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md#talg-thm-00006) garantiza que este grafo es funcional; y cada clase posee algún representante, de modo que es total. Así determina una función

$$
\widehat f:G/\ker f\to H
$$

con

$$
\widehat f(g\ker f)=f(g).
$$

La misma igualdad, junto con la definición del producto cociente y la homomorfía de $f$, da

$$
\widehat f\bigl((g\ker f)\star_{\ker f}(h\ker f)\bigr)
=f(g\star h)
=f(g)\diamond f(h),
$$

de modo que $\widehat f$ es un homomorfismo. Si

$$
\widehat f(g\ker f)=\widehat f(h\ker f),
$$

entonces $f(g)=f(h)$ y el argumento de inyectividad del [Teorema 13.1.1](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md#talg-thm-00006) produce

$$
g\ker f=h\ker f.
$$

Finalmente, como $f$ es sobreyectiva, para todo $y\in H$ existe $g\in G$ con $y=f(g)=\widehat f(g\ker f)$. Por tanto, $\widehat f$ es biyectiva.

Por la [Definición 8.2.3](tratado-de-algebra-capitulo-8-isomorfismos.md#talg-def-00023), $\widehat f$ es un isomorfismo de grupos.

$\square$

---

## 13.3. Cierre del bloque de grupos

El primer teorema de isomorfía cierra la primera gran arquitectura del tratado:

$$
\text{homomorfismo}
\longrightarrow
\ker f
\longrightarrow
G/\ker f
\longrightarrow
\operatorname{im}f
\longrightarrow
\text{isomorfismo}.
$$

El resultado no afirma una igualdad literal entre $G/\ker f$ y $\operatorname{im}f$. Afirma la existencia de un isomorfismo canónicamente determinado por $f$.

Tampoco se ha utilizado el axioma de elección. La función inducida se construyó mediante su grafo y la invariancia respecto de representantes, no seleccionando una familia global de representantes del cociente.

Con esto queda cerrada la infraestructura básica de la Parte II necesaria para pasar a estructuras con dos operaciones.

---

[← **Capítulo 12 — Cocientes de grupos**](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md) · [**Capítulo 14 — Anillos** →](tratado-de-algebra-capitulo-14-anillos.md)
