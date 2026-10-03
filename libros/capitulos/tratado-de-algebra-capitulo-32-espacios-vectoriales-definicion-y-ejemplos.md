---
title: 'Tratado moderno de Álgebra — Capítulo 32: Espacios vectoriales: definición y ejemplos'
description: Definición de espacio vectorial sobre un cuerpo, identidades escalares y construcción de espacios de funciones y potencias finitas.
author: Gustav A. Tachek
content-id: MA-BCH-0140
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
- cuerpos
- grupos-abelianos
- espacios-de-funciones
prerequisites:
- MA-BCH-0021
- MA-BCH-0028
- MA-BCH-0047
- MA-BCH-0136
related:
- MA-BOK-0007
- MA-BCH-0139
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## 32.0. Propósito y posición deductiva

Un [grupo abeliano](tratado-de-algebra-capitulo-5-conmutatividad-y-grupos-abelianos.md#talg-def-00010) permite sumar vectores; una acción de un [cuerpo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) permite variar su escala. La compatibilidad entre ambas operaciones define el espacio vectorial. Se fija un cuerpo conmutativo arbitrario $F$. Los ejemplos se construyen como conjuntos de funciones, sin presuponer coordenadas o bases.

El marco fundacional es ZF con lógica clásica. Las construcciones y pruebas de este capítulo no utilizan el axioma de elección. La disyunción final de la [Proposición 32.2.1](#talg-pro-00107) emplea explícitamente el tercero excluido; no se presupone decidibilidad efectiva de la igualdad.

---

## 32.1. Espacio vectorial sobre un cuerpo

### Definición 32.1.1 — Espacio vectorial sobre un cuerpo {#talg-def-00070}

Fijado un [cuerpo conmutativo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) $F$, un **espacio vectorial sobre $F$** es un dato $(V,+,\mu)$ donde $(V,+)$ es un [grupo abeliano](tratado-de-algebra-capitulo-5-conmutatividad-y-grupos-abelianos.md#talg-def-00010) y $\mu:F\times V\to V$ es una función. Escribimos $av=\mu(a,v)$ y exigimos, para $a,b\in F$, $u,v\in V$,
$$
a(u+v)=au+av,\quad (a+b)v=av+bv,\quad
(ab)v=a(bv),\quad 1_Fv=v.
$$
Los elementos de $F$ son escalares; los de $V$, vectores. El neutro aditivo del grupo es $0_V$; se distingue de $0_F$. Las operaciones y sus dominios son parte del dato, y las igualdades son leyes del dato. El grupo garantiza que $V$ está habitado por $0_V$. No se exige que $V\ne\{0_V\}$. Dos espacios pueden ser isomorfos sin ser conjuntos iguales.

## 32.2. Ceros, opuestos y cancelación escalar

### Proposición 32.2.1 — Ceros, opuestos y cancelación escalar {#talg-pro-00107}

En un [espacio vectorial](#talg-def-00070) sobre $F$,
$$
0_Fv=0_V,\quad a0_V=0_V,\quad
(-a)v=-(av)=a(-v),\quad (-1_F)v=-v.
$$
Si $a\ne0_F$, entonces $av=0_V$ implica $v=0_V$ y $au=av$ implica $u=v$. En lógica clásica, $av=0_V$ equivale a $a=0_F$ o $v=0_V$.

#### Demostración {#talg-prf-00169}

Como $(0_F+0_F)v=0_Fv+0_Fv$ y $0_F+0_F=0_F$, obtenemos $0_Fv=0_Fv+0_Fv$. Sumando el opuesto de $0_Fv$ en el grupo aditivo, resulta $0_Fv=0_V$. Como $a(0_V+0_V)=a0_V+a0_V$, el mismo paso de cancelación explícita da $a0_V=0_V$.

La distributividad implica $av+(-a)v=(a-a)v=0_Fv=0_V$. Por [unicidad de opuesto aditivo](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002), $(-a)v=-(av)$. También $av+a(-v)=a(v-v)=a0_V=0_V$, de donde $a(-v)=-(av)$. Con $a=1_F$ se obtiene $(-1_F)v=-v$.

Si $a\ne0_F$, la [definición de cuerpo](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) proporciona el inverso único $a^{-1}$. De $av=0_V$,
$$
v=1_Fv=(a^{-1}a)v=a^{-1}(av)=a^{-1}0_V=0_V.
$$
Si $au=av$, aplicamos $a^{-1}$ a ambos lados: $a^{-1}(au)=u$ y $a^{-1}(av)=v$, luego $u=v$.

Para la última equivalencia, si $a=0_F$ o $v=0_V$, las identidades anteriores dan $av=0_V$. Si $av=0_V$, usamos explícitamente el tercero excluido $a=0_F$ o $a\ne0_F$. En la segunda rama el argumento con el inverso da $v=0_V$. No se afirma que esa disyunción sea decidible por un procedimiento efectivo. $\square$

## 32.3. Espacios de funciones y potencias finitas

### Proposición 32.3.1 — Espacios de funciones y potencias finitas {#talg-pro-00108}

Para cualquier conjunto $I$, el conjunto $F^I$ de funciones $I\to F$ es espacio vectorial sobre $F$ con operaciones
$$
(x+y)(i)=x(i)+y(i),\qquad (ax)(i)=a\,x(i).
$$
Su cero es la función constante cero y el opuesto de $x$ es $i\mapsto-x(i)$. Si $I=\varnothing$, $F^I$ tiene una sola función y es el espacio cero. Para $n\in\mathbb N$, escribimos $F^n=F^{\{i\in\mathbb N:i<n\}}$, usando los naturales de la [interfaz cerrada](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006). El cuerpo $F$ con su adición y su multiplicación como acción es también un espacio vectorial sobre sí mismo.

#### Demostración {#talg-prf-00170}

El [conjunto de funciones](tratado-de-algebra-capitulo-0-interfaz-fundacional.md#talg-imp-00001) $I\to F$ existe por Separación dentro de $\mathcal P(I\times F)$: se seleccionan los grafos totales y funcionales con dominio $I$. Para $x,y\in F^I$, los grafos de $i\mapsto x(i)+y(i)$ y $i\mapsto ax(i)$ existen por Separación en $I\times F$ y definen funciones porque las operaciones del cuerpo son funciones. Cada par de entradas determina una salida única; así existen las operaciones anunciadas con los dominios y codominios correctos.

Para $x,y,z$ y $i\in I$,
$$
((x+y)+z)(i)=(x(i)+y(i))+z(i)
=x(i)+(y(i)+z(i))=(x+(y+z))(i).
$$
La conmutatividad se comprueba por $(x+y)(i)=x(i)+y(i)=y(i)+x(i)=(y+x)(i)$. La constante cero existe incluso si $I$ es vacío, y $(x+0)(i)=x(i)+0_F=x(i)$. El opuesto existe y $(x+(-x))(i)=x(i)-x(i)=0_F$. Extensionalidad funcional convierte estas igualdades puntuales en las leyes del grupo abeliano.

Las cuatro leyes escalares se verifican en cada entrada:
$$
\begin{aligned}
(a(x+y))(i)&=a(x(i)+y(i))=ax(i)+ay(i),\\
((a+b)x)(i)&=(a+b)x(i)=ax(i)+bx(i),\\
((ab)x)(i)&=(ab)x(i)=a(bx(i)),\\
(1_Fx)(i)&=x(i).
\end{aligned}
$$
Las derechas son respectivamente los valores de $ax+ay$, $ax+bx$, $a(bx)$ y $x$. Esto prueba todos los axiomas vectoriales. Cuando $I$ es vacío, el único grafo funcional es vacío; todas las leyes se mantienen y el conjunto subyacente es singleton.

La [interfaz natural](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md#talg-imp-00006) permite formar por Separación el conjunto de índices menor que $n$. Aplicar la construcción anterior da $F^n$, incluyendo $n=0$.

Finalmente, la adición de $F$ ya es grupo abeliano. La multiplicación $F\times F\to F$ satisface las dos distributividades, asociatividad y unidad por las leyes del cuerpo. Por tanto define la acción escalar de un espacio vectorial en $F$. No se identifica literalmente $F$ con un conjunto de funciones. $\square$

---

## 32.99. Síntesis

El espacio vectorial combina un grupo abeliano con una acción escalar compatible. Las identidades de ceros y opuestos se deducen, no se añaden como axiomas. Los espacios de funciones proporcionan ejemplos sobre un cuerpo arbitrario y permiten construir potencias finitas sin disponer aún de bases. La [unidad siguiente](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md) estudiará qué subconjuntos conservan las dos operaciones.

---

[← **Capítulo 31 — Descenso y transporte de estructura**](tratado-de-algebra-capitulo-31-descenso-y-transporte-de-estructura.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md) · [**Capítulo 33 — Subespacios y generación** →](tratado-de-algebra-capitulo-33-subespacios-y-generacion.md)
