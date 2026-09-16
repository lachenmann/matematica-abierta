---
title: 'Tratado moderno de Álgebra — Capítulo 18: Ideales'
description: Capítulo del Tratado moderno de Álgebra dedicado a ideales, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0043
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
- MA-BCH-0042
related:
- MA-BOK-0007
- MA-BCH-0042
- MA-BCH-0044
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 18 — Ideales

## 18.0. Propósito y separación conceptual

El capítulo anterior mostró una asimetría fundamental. La imagen de un homomorfismo de anillos unitarios es un subanillo, pero su núcleo, cuando el codominio es no trivial, no puede serlo: un subanillo contiene la unidad multiplicativa ambiente, mientras que el núcleo de un homomorfismo unital no contiene esa unidad salvo que el codominio sea trivial.

La estructura apropiada para los núcleos no exige una unidad multiplicativa interna. En cambio, combina dos condiciones:

1. estructura aditiva de subgrupo;
2. absorción frente a la multiplicación por elementos arbitrarios del anillo ambiente.

En un anillo no conmutativo la absorción debe distinguirse por lados. Por ello se introducirán separadamente **ideales izquierdos**, **ideales derechos** e **ideales bilaterales**. La palabra **ideal**, sin calificativo, significará ideal bilateral salvo indicación expresa.

> **Contraste bibliográfico.** La lateralidad es indispensable en teoría no conmutativa y se controla aquí principalmente con Lam (`BIB-TALG-0008`) y Dummit–Foote (`BIB-TALG-0001`). En el caso conmutativo, Atiyah–Macdonald (`BIB-TALG-0007`) sirve de contraste para la convención usual en la que la distinción lateral desaparece. Las fuentes fijan terminología y arquitectura; las pruebas se desarrollan dentro del tratado.

---

## 18.1. Ideales laterales y bilaterales

### Definición 18.1.1 — Ideal izquierdo, derecho y bilateral {#talg-def-00040}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo y sea $I\subseteq R$.

Diremos que $I$ es un **ideal izquierdo** de $R$ si:

1. $I$ determina un subgrupo del grupo aditivo $\langle R,+\rangle$;
2. para todo $r\in R$ y todo $x\in I$,
   $$
   r\cdot x\in I.
   $$

Diremos que $I$ es un **ideal derecho** de $R$ si:

1. $I$ determina un subgrupo del grupo aditivo $\langle R,+\rangle$;
2. para todo $r\in R$ y todo $x\in I$,
   $$
   x\cdot r\in I.
   $$

Finalmente, $I$ es un **ideal bilateral** —o simplemente un **ideal**— si es simultáneamente ideal izquierdo e ideal derecho.

La condición aditiva incorpora $0\in I$, cierre bajo suma y cierre bajo opuestos. La condición multiplicativa es una **absorción desde el anillo ambiente**; no exige $1\in I$.

> **Distinción estructural.** Un ideal no se define como subanillo. En particular, un ideal propio de un anillo unitario no contiene $1$, mientras que todo subanillo de este tratado sí contiene la unidad multiplicativa ambiente.

---

### Proposición 18.1.2 — El ideal cero y el ideal total {#talg-pro-00036}

Para todo anillo $\mathcal R=\langle R,+,\cdot\rangle$:

1. $\{0\}$ es un ideal bilateral de $R$;
2. $R$ es un ideal bilateral de sí mismo.

#### Demostración {#talg-prf-00055}

El conjunto $\{0\}$ está habitado por $0$. Además, para sus únicos elementos $a=b=0$, se tiene

$$
a-b=0-0=0\in\{0\}.
$$

Por el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $\{0\}$ determina un subgrupo del grupo aditivo $\langle R,+\rangle$.

Sea $r\in R$. Por la [Proposición 14.3.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00024),

$$
r\cdot0=0=0\cdot r.
$$

Por tanto, $\{0\}$ satisface tanto la absorción izquierda como la derecha y es un ideal bilateral.

Para $R$ mismo, $0\in R$ proporciona un testigo explícito de habitabilidad y, si $a,b\in R$, entonces $a-b\in R$ por las operaciones del grupo aditivo; por el [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $R$ determina un subgrupo de su propio grupo aditivo. Además, si $r,x\in R$, entonces

$$
r\cdot x\in R
\qquad\text{y}\qquad
x\cdot r\in R
$$

por cierre de la operación multiplicativa. Así, $R$ es también un ideal bilateral de sí mismo. $\square$

---

### Teorema 18.1.3 — Un ideal lateral contiene $1$ si y sólo si es todo el anillo {#talg-thm-00010}

Sea $I\subseteq R$ un ideal izquierdo o un ideal derecho de un anillo $\mathcal R$. Entonces

$$
\boxed{
I=R
\quad\Longleftrightarrow\quad
1_{\mathcal R}\in I.
}
$$

En particular, el mismo criterio vale para ideales bilaterales.

#### Demostración {#talg-prf-00056}

Si $I=R$, entonces $1_{\mathcal R}\in I$ porque $1_{\mathcal R}\in R$.

Recíprocamente, supongamos $1_{\mathcal R}\in I$.

Si $I$ es un ideal izquierdo, para todo $r\in R$ la absorción izquierda da

$$
r\cdot1_{\mathcal R}\in I.
$$

Como $1_{\mathcal R}$ es neutro multiplicativo,

$$
r=r\cdot1_{\mathcal R}\in I.
$$

Luego $R\subseteq I$, y como $I\subseteq R$, resulta $I=R$.

Si $I$ es un ideal derecho, para todo $r\in R$ la absorción derecha da

$$
1_{\mathcal R}\cdot r\in I,
$$

y por neutralidad

$$
r=1_{\mathcal R}\cdot r\in I.
$$

Nuevamente $I=R$. $\square$

---

### Definición 18.1.4 — Ideal propio {#talg-def-00041}

Sea $I$ un ideal izquierdo, derecho o bilateral de un anillo $R$. Diremos que $I$ es **propio** si

$$
I\neq R.
$$

Por el [Teorema 18.1.3](tratado-de-algebra-capitulo-18-ideales.md#talg-thm-00010), para cualquiera de los tres tipos de ideal esta condición es equivalente a

$$
\boxed{1_R\notin I.}
$$

Cuando se use la expresión *ideal propio* sin calificativo lateral, se entenderá un ideal bilateral propio.

---

## 18.2. El caso conmutativo

### Proposición 18.2.1 — En un anillo conmutativo coinciden las nociones laterales {#talg-pro-00037}

Sea $\mathcal R$ un anillo conmutativo y sea $I\subseteq R$. Entonces son equivalentes:

1. $I$ es un ideal izquierdo;
2. $I$ es un ideal derecho;
3. $I$ es un ideal bilateral.

#### Demostración {#talg-prf-00057}

Supongamos que $I$ es un ideal izquierdo. La condición de subgrupo aditivo ya está satisfecha. Sean $x\in I$ y $r\in R$. Como la multiplicación es conmutativa,

$$
xr=rx.
$$

Por absorción izquierda, $rx\in I$, y por tanto $xr\in I$. Luego $I$ es también ideal derecho y, en consecuencia, bilateral.

El argumento inverso es idéntico: si $I$ es ideal derecho, entonces para $r\in R$ y $x\in I$,

$$
rx=xr\in I,
$$

de modo que también es ideal izquierdo.

Todo ideal bilateral es, por definición, tanto izquierdo como derecho. Quedan así equivalentes las tres condiciones. $\square$

> **Convención terminológica.** Aunque en anillos conmutativos las tres nociones coinciden, el tratado mantendrá la definición bilateral como significado básico de *ideal*. La coincidencia es un teorema, no parte de la definición general.

---

## 18.3. Núcleos de homomorfismos de anillos

### Proposición 18.3.1 — El núcleo de un homomorfismo de anillos es un ideal bilateral {#talg-pro-00038}

Sea

$$
f:R\to S
$$

un homomorfismo de anillos. Considerando $f$ como homomorfismo entre los grupos aditivos, su núcleo

$$
\ker f
=
\{x\in R:f(x)=0_S\}
$$

es un ideal bilateral de $R$.

#### Demostración {#talg-prf-00058}

Por la [Definición 17.2.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00039), $f$ preserva la suma; por tanto, al considerar los grupos aditivos de $R$ y $S$, $f$ es un homomorfismo de grupos en el sentido de la [Definición 7.4.1](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019). Entonces la [Proposición 9.1.3](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-pro-00014) implica que $\ker f$ determina un subgrupo de $\langle R,+\rangle$.

Sea ahora $x\in\ker f$ y sea $r\in R$. Por definición de núcleo,

$$
f(x)=0_S.
$$

Como $f$ preserva la multiplicación,

$$
f(rx)=f(r)f(x)=f(r)0_S.
$$

Por absorción del cero en el anillo $S$ ([Proposición 14.3.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00024)),

$$
f(r)0_S=0_S.
$$

Por tanto,

$$
rx\in\ker f.
$$

Esto demuestra la absorción izquierda.

Análogamente,

$$
f(xr)=f(x)f(r)=0_Sf(r)=0_S,
$$

de donde

$$
xr\in\ker f.
$$

También se cumple la absorción derecha. Junto con la estructura de subgrupo aditivo, la [Definición 18.1.1](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00040) implica que $\ker f$ es un ideal bilateral de $R$. $\square$

---

### Corolario 18.3.2 — El núcleo es propio si y sólo si el codominio es no trivial {#talg-cor-00009}

Sea

$$
f:R\to S
$$

un homomorfismo de anillos. Entonces

$$
\boxed{
\ker f\text{ es un ideal propio de }R
\quad\Longleftrightarrow\quad
S\text{ es un anillo no trivial}.
}
$$

#### Demostración {#talg-prf-00059}

Supongamos primero que $S$ es no trivial. Entonces

$$
0_S\neq1_S.
$$

Como $f$ es un homomorfismo de anillos,

$$
f(1_R)=1_S\neq0_S.
$$

Por tanto,

$$
1_R\notin\ker f.
$$

Por el [Teorema 18.1.3](tratado-de-algebra-capitulo-18-ideales.md#talg-thm-00010), $\ker f\neq R$. Como la [Proposición 18.3.1](tratado-de-algebra-capitulo-18-ideales.md#talg-pro-00038) ya estableció que $\ker f$ es un ideal bilateral, la [Definición 18.1.4](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00041) implica que es propio.

Recíprocamente, supongamos que $\ker f$ es un ideal propio. Queremos demostrar $0_S\neq1_S$. Supongamos, para obtener contradicción,

$$
0_S=1_S.
$$

Sea $s\in S$. Usando el neutro multiplicativo y la absorción del cero,

$$
s=s1_S=s0_S=0_S.
$$

Así, todo elemento de $S$ es igual a $0_S$. En particular, para cada $r\in R$,

$$
f(r)=0_S,
$$

y por tanto

$$
\ker f=R,
$$

contradiciendo que $\ker f$ sea propio. Por consiguiente $0_S\neq1_S$, es decir, $S$ es no trivial. Hemos demostrado la equivalencia. $\square$

> **Lectura estructural.** El corolario refina el [Corolario 17.3.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-cor-00008): el núcleo no sólo deja de ser subanillo en codominio no trivial, sino que aparece exactamente como un ideal bilateral propio. Esta es la estructura que permitirá formar el cociente del dominio por el núcleo.

---

## 18.4. Preparación del cociente

El siguiente problema ya no es identificar una subestructura, sino construir una estructura nueva sobre clases de equivalencia.

Sea $I$ un ideal bilateral de $R$. La relación candidata será

$$
a\equiv b\pmod I
\quad\Longleftrightarrow\quad
 a-b\in I.
$$

La infraestructura de cocientes conjuntistas ya está disponible mediante [`TALG-IMP-00003`](tratado-de-algebra-relaciones-equivalencia-cocientes.md#talg-imp-00003), pero antes de escribir $R/I$ como anillo habrá que demostrar explícitamente:

1. que la relación anterior es de equivalencia;
2. que la suma de representantes desciende a clases;
3. que el producto de representantes desciende a clases;
4. que la bilateralidad del ideal es exactamente la hipótesis que controla la buena definición multiplicativa en el caso no conmutativo.

No se anticipará ninguna operación cociente antes de cerrar esas cuatro verificaciones.

---

## 18.5. Cierre deductivo

Queda cerrada la cadena

```text
subgrupo aditivo
+
absorción por el anillo ambiente
        ↓
ideal izquierdo / derecho / bilateral
        ↓
{0} y R son ideales bilaterales
        ↓
1 ∈ I ↔ I = R
        ↓
ideal propio ↔ 1 ∉ I
        ↓
caso conmutativo: izquierda = derecha = bilateral
        ↓
núcleo de homomorfismo de anillos = ideal bilateral
        ↓
núcleo propio ↔ codominio no trivial
        ↓
congruencia módulo I
```

No se ha utilizado el axioma de elección.

El siguiente nodo canónico será

[Definición 19.1.1 — Congruencia módulo un ideal bilateral](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-def-00042).

---

[← **Capítulo 17 — Subanillos y homomorfismos de anillos**](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md) · [**Capítulo 19 — Cocientes de anillos** →](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md)
