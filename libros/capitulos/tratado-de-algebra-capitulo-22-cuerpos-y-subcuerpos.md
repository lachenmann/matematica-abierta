---
title: 'Tratado moderno de Álgebra — Capítulo 22: Cuerpos y subcuerpos'
description: Capítulo del Tratado moderno de Álgebra dedicado a cuerpos y subcuerpos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0047
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
- MA-BCH-0046
related:
- MA-BOK-0007
- MA-BCH-0046
- MA-BCH-0048
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 22 — Cuerpos y subcuerpos

## 22.0. Propósito y posición deductiva

La Parte III dejó construida la jerarquía

```text
anillo conmutativo
→ anillo no trivial
→ ausencia de divisores de cero
→ dominio íntegro.
```

La Parte IV añade una exigencia multiplicativa más fuerte: que **todo elemento no nulo sea invertible**. La noción resultante será la de cuerpo.

La infraestructura necesaria ya está disponible:

1. anillos y anillos conmutativos ([Definición 14.1.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00032), la [Definición 14.5.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00033));
2. unidades e inversos multiplicativos únicos ([Definición 15.1.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-def-00034), la [Proposición 15.2.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00026), la [Notación 15.3.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-not-00013));
3. no trivialidad ([Definición 16.1.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00035));
4. dominios íntegros ([Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047));
5. subanillos unitarios y su criterio ([Definición 17.1.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00038), el [Teorema 17.1.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-thm-00009)).

No se introduce una nueva operación. Un cuerpo será una clase especial de anillos; un subcuerpo será una clase especial de subanillos.

> **Contraste bibliográfico.** La convención se contrasta con Dummit–Foote (`BIB-TALG-0001`), Aluffi (`BIB-TALG-0002`) y Lang (`BIB-TALG-0004`). En este tratado, “cuerpo” significa siempre **anillo conmutativo unitario, no trivial, en el que todo elemento no nulo es invertible**. No se introduce aquí la noción no conmutativa de anillo de división. Las demostraciones se desarrollan internamente.

---

## 22.1. Cuerpos

### Definición 22.1.1 — Cuerpo {#talg-def-00048}

Sea

$$
\mathcal F=\langle F,+,\cdot\rangle
$$

un anillo. Diremos que $\mathcal F$ es un **cuerpo** si se cumplen simultáneamente:

1. $\mathcal F$ es conmutativo;
2. $\mathcal F$ es no trivial, es decir,
   $$
   0\neq1;
   $$
3. todo elemento no nulo de $F$ es una unidad:
   $$
   \forall a\in F,\qquad
   a\neq0\Longrightarrow a\in F^\times.
   $$

La tercera condición significa que para cada $a\neq0$ existe un elemento $b\in F$ tal que

$$
ab=ba=1.
$$

Por la [Proposición 15.2.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00026), ese inverso es único y puede escribirse $a^{-1}$ mediante la [Notación 15.3.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-not-00013).

> **Convención terminológica.** La conmutatividad forma parte de la definición de cuerpo. Un anillo no conmutativo en el que todo elemento no nulo sea invertible no será llamado “cuerpo” en este tratado.

---

## 22.2. Los elementos no nulos son exactamente las unidades

### Proposición 22.2.1 — Unidades de un cuerpo {#talg-pro-00049}

Sea $\mathcal F$ un cuerpo. Entonces

$$
\boxed{
F^\times=\{a\in F:a\neq0\}.
}
$$

#### Demostración {#talg-prf-00078}

Sea $a\in F$.

Si $a\neq0$, la condición (3) de la [Definición 22.1.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) implica directamente

$$
a\in F^\times.
$$

Recíprocamente, supongamos $a\in F^\times$. Como todo cuerpo es no trivial por definición, el [Corolario 16.1.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-cor-00005) da

$$
0\notin F^\times.
$$

Por tanto $a\neq0$.

Así, para todo $a\in F$,

$$
a\in F^\times
\quad\Longleftrightarrow\quad
a\neq0,
$$

lo que prueba la igualdad de conjuntos. $\square$

> **Consecuencia estructural.** En un cuerpo, el grupo de unidades construido en el [Teorema 15.5.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-thm-00007) tiene como conjunto subyacente exactamente $F\setminus\{0\}$.

---

## 22.3. Todo cuerpo es un dominio íntegro

### Teorema 22.3.1 — Todo cuerpo es un dominio íntegro {#talg-thm-00014}

Todo cuerpo es un dominio íntegro.

#### Demostración {#talg-prf-00079}

Sea $\mathcal F$ un cuerpo. Por la [Definición 22.1.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048), $\mathcal F$ es un anillo conmutativo y no trivial.

Resta demostrar que no posee divisores de cero. Sea $a\in F$ con $a\neq0$. Por la [Proposición 22.2.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-pro-00049),

$$
a\in F^\times.
$$

Como $\mathcal F$ es no trivial, la [Proposición 16.3.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-pro-00029) afirma que una unidad no puede ser divisor de cero por la izquierda ni por la derecha. En particular, en el caso conmutativo $a$ no es divisor de cero en el sentido de la [Definición 16.5.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00037).

Esto vale para todo $a\neq0$. Por consiguiente, $\mathcal F$ no posee divisores de cero. Junto con conmutatividad y no trivialidad, la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047) implica que $\mathcal F$ es un dominio íntegro. $\square$

En consecuencia, todos los resultados ya demostrados para dominios íntegros se aplican a los cuerpos. En particular,

$$
ab=0
\quad\Longrightarrow\quad
a=0\ \lor\ b=0,
$$

y todo factor no nulo puede cancelarse multiplicativamente.

> **Lectura fundacional.** Bajo la definición negativa actual de dominio íntegro, estas dos formas operativas se obtienen mediante los resultados clásicos auditados del Capítulo 21; no se atribuyen automáticamente a la parte constructiva del [Teorema 22.3.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-thm-00014).

---

## 22.4. Ideales de un cuerpo

### Proposición 22.4.1 — Los únicos ideales de un cuerpo son el cero y el total {#talg-pro-00050}

Sea $\mathcal F$ un cuerpo y sea $I\subseteq F$ un ideal bilateral. Entonces

$$
\boxed{
I=\{0\}
\quad\text{o}\quad
I=F.
}
$$

#### Demostración {#talg-prf-00080}

Aplicamos LEM a la proposición $\exists a\in I\,(a\neq0)$. Si no existe tal elemento, sea $x\in I$. Entonces $\neg(x\neq0)$, es decir, $\neg\neg(x=0)$; por DNE, $x=0$. Como esto vale para todo $x\in I$ y todo ideal contiene $0$, por Extensionalidad se obtiene

$$
I=\{0\}.
$$

En el otro caso existe $a\in I$ con $a\neq0$. Por la [Proposición 22.2.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-pro-00049), $a$ es una unidad de $F$, de modo que $a^{-1}\in F$ y

$$
a^{-1}a=1.
$$

Como $I$ es un ideal bilateral y $a\in I$, la absorción por elementos del anillo implica

$$
a^{-1}a\in I.
$$

Por tanto,

$$
1\in I.
$$

Aplicando el [Teorema 18.1.3](tratado-de-algebra-capitulo-18-ideales.md#talg-thm-00010), concluimos

$$
I=F.
$$

Las dos posibilidades son, pues, exactamente el ideal cero y el ideal total, ambos ya construidos en la [Proposición 18.1.2](tratado-de-algebra-capitulo-18-ideales.md#talg-pro-00036). $\square$

> **Núcleo constructivo.** Sin usar la disyunción clásica completa, la parte operativa de la prueba permanece válida: si se exhibe $a\in I$ con $a\neq0$, entonces $I=F$.

> **Uso posterior.** Este resultado será la herramienta central para demostrar que un homomorfismo unital desde un cuerpo hacia un anillo no trivial tiene núcleo cero y, por tanto, es inyectivo.

---

## 22.5. Subcuerpos

### Definición 22.5.1 — Subcuerpo {#talg-def-00049}

Sea $\mathcal F=\langle F,+,\cdot\rangle$ un cuerpo y sea $S\subseteq F$.

Diremos que la estructura inducida

$$
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

es un **subcuerpo** de $\mathcal F$ si se cumplen simultáneamente:

1. $\mathcal S$ es un subanillo de $\mathcal F$ en el sentido unital de la [Definición 17.1.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00038);
2. para todo $a\in S$ con $a\neq0$, el inverso multiplicativo de $a$ en $F$ pertenece a $S$:
   $$
   a^{-1}\in S.
   $$

La segunda condición está bien tipada porque, al ser $\mathcal F$ un cuerpo, todo $a\neq0$ es una unidad y la [Notación 15.3.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-not-00013) define unívocamente $a^{-1}$.

> **Punto estructural.** Un subcuerpo comparte con el cuerpo ambiente las dos operaciones, el cero y la unidad. No se permite una unidad multiplicativa distinta de la ambiente.

---

### Proposición 22.5.2 — La estructura inducida por un subcuerpo es un cuerpo {#talg-pro-00051}

Si $\mathcal S$ es un subcuerpo de un cuerpo $\mathcal F$, entonces $\mathcal S$ es un cuerpo en el sentido de la [Definición 22.1.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048).

#### Demostración {#talg-prf-00081}

Por la [Definición 22.5.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00049), $\mathcal S$ es un subanillo de $\mathcal F$. Entonces la [Proposición 17.1.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00030) asegura que $\mathcal S$ es un anillo y que

$$
0_{\mathcal S}=0_{\mathcal F},
\qquad
1_{\mathcal S}=1_{\mathcal F}.
$$

Como $\mathcal F$ es conmutativo y no trivial, la [Proposición 17.1.4](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00031) implica que $\mathcal S$ es también conmutativo y no trivial.

Sea ahora $a\in S$ con $a\neq0$. Por la condición (2) de la [Definición 22.5.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00049),

$$
a^{-1}\in S.
$$

Como las operaciones de $\mathcal S$ son las restricciones de las operaciones de $\mathcal F$,

$$
a\cdot_S a^{-1}
=aa^{-1}
=1_{\mathcal F}
=1_{\mathcal S},
$$

y análogamente

$$
a^{-1}\cdot_S a=1_{\mathcal S}.
$$

Por la [Definición 15.1.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-def-00034), $a$ es una unidad de $\mathcal S$. Esto vale para todo elemento no nulo de $S$. Por la [Definición 22.1.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048), $\mathcal S$ es un cuerpo. $\square$

---

## 22.6. Criterio de subcuerpo

### Teorema 22.6.1 — Criterio de subcuerpo {#talg-thm-00015}

Sea $\mathcal F=\langle F,+,\cdot\rangle$ un cuerpo y sea $S\subseteq F$. Entonces $S$ determina un subcuerpo de $\mathcal F$ si y sólo si se cumplen las cuatro condiciones siguientes:

1. $1\in S$;
2. para todos $a,b\in S$,
   $$
   a-b\in S;
   $$
3. para todos $a,b\in S$,
   $$
   ab\in S;
   $$
4. para todo $a\in S$ con $a\neq0$,
   $$
   a^{-1}\in S.
   $$

#### Demostración {#talg-prf-00082}

Supongamos primero que $S$ determina un subcuerpo. Por la [Definición 22.5.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00049), $S$ determina en particular un subanillo de $\mathcal F$. Aplicando el [Teorema 17.1.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-thm-00009), obtenemos las condiciones (1), (2) y (3). La condición (4) es exactamente la segunda cláusula de la [Definición 22.5.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00049).

Recíprocamente, supongamos (1)–(4). Las tres primeras condiciones y el [Teorema 17.1.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-thm-00009) muestran que $S$ determina un subanillo unital de $\mathcal F$. La cuarta condición asegura que ese subanillo es cerrado bajo el inverso multiplicativo ambiente de cada elemento no nulo. Por la [Definición 22.5.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00049), $S$ determina un subcuerpo de $\mathcal F$.

$\square$

---

## 22.7. Cierre deductivo

Queda cerrada la cadena

```text
cuerpo
  ↓
todo elemento no nulo es unidad
  ↓
F^× = F \ {0}
  ↓
todo cuerpo es dominio íntegro
  ↓
los únicos ideales son {0} y F
  ↓
subcuerpo = subanillo unital cerrado bajo inversos no nulos
  ↓
criterio por 1, diferencias, productos e inversos
```

No se ha utilizado el axioma de elección. En particular, no se ha elegido una familia de inversos: para cada elemento no nulo el inverso multiplicativo es único por [Proposición 15.2.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00026).

El siguiente nodo canónico será:

[**Definición 23.1.1 — Homomorfismo de cuerpos**](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-def-00050).

Ese paso reutilizará la teoría de homomorfismos de anillos y la trivialidad de los ideales de un cuerpo para aislar la inyectividad característica de los homomorfismos entre cuerpos no triviales.

---

[← **Capítulo 21 — Dominios íntegros**](tratado-de-algebra-capitulo-21-dominios-integros.md) · [**Capítulo 23 — Homomorfismos de cuerpos** →](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md)