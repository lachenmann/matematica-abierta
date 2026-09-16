---
title: 'Tratado moderno de Álgebra — Capítulo 14: Anillos'
description: Capítulo del Tratado moderno de Álgebra dedicado a anillos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0039
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
- MA-BCH-0038
related:
- MA-BOK-0007
- MA-BCH-0038
- MA-BCH-0040
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 14 — Anillos

## 14.0. Propósito y convención estructural

La teoría de grupos estudia una sola operación. Un anillo introduce dos operaciones sobre el mismo conjunto y, por primera vez en el tratado, exige leyes que relacionan estructuras ya construidas de manera independiente.

La decisión de arquitectura es explícita: en este tratado la palabra **anillo** significará **anillo asociativo con unidad multiplicativa**, sin exigir conmutatividad de la multiplicación. La conmutatividad será una condición adicional. Tampoco se incorporará en la definición básica la desigualdad entre los neutros aditivo y multiplicativo; la no trivialidad se impondrá sólo en las estructuras posteriores que realmente la necesiten.

Esta elección permite reutilizar exactamente la jerarquía ya cerrada:

$$
\text{grupo abeliano aditivo}
\quad+\quad
\text{monoide multiplicativo}
\quad+\quad
\text{distributividad}.
$$

La escritura

$$
\langle R,+,\cdot\rangle
$$

se entenderá como abreviatura tipográfica de la codificación conjuntista anidada

$$
\langle R,\langle +,\cdot\rangle\rangle.
$$

No se introduce, por tanto, un nuevo tipo primitivo de objeto estructural.

> **Contraste bibliográfico.** La literatura no usa una única convención para la palabra *ring*. Nuestra convención separa dos cuestiones: adopta unidad multiplicativa desde el nivel básico, como en tratamientos modernos de teoría de anillos, pero no incorpora conmutatividad, que se definirá aparte. Para el bloque conmutativo se incorpora Atiyah–Macdonald (`BIB-TALG-0007`) y para el bloque general no conmutativo, Lam (`BIB-TALG-0008`). Estas fuentes funcionan como contraste de convención y arquitectura, no como fundamento deductivo.

---

## 14.1. Definición de anillo

### Definición 14.1.1 — Anillo {#talg-def-00032}

Un **anillo** es una estructura

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

tal que:

1. $\langle R,+\rangle$ es un grupo abeliano;
2. $\langle R,\cdot\rangle$ es un monoide;
3. la multiplicación es distributiva por la izquierda respecto de la suma:

   $$
   a\cdot(b+c)=(a\cdot b)+(a\cdot c)
   \qquad(a,b,c\in R);
   $$

4. la multiplicación es distributiva por la derecha respecto de la suma:

   $$
   (a+b)\cdot c=(a\cdot c)+(b\cdot c)
   \qquad(a,b,c\in R).
   $$

No se supone que

$$
a\cdot b=b\cdot a,
$$

y no se exige en esta definición ninguna desigualdad entre los dos elementos neutros.

La no vacuidad de $R$ no es un axioma adicional: ya forma parte de la estructura de grupo aditivo y del monoide multiplicativo.

---

## 14.2. Notación aditiva y multiplicativa

### Notación 14.2.1 — Cero, uno y opuesto aditivo {#talg-not-00012}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo.

El único neutro del grupo aditivo $\langle R,+\rangle$ se denota

$$
0_{\mathcal R},
$$

o simplemente $0$ cuando el anillo ambiente es inequívoco.

El único neutro del monoide multiplicativo $\langle R,\cdot\rangle$ se denota

$$
1_{\mathcal R},
$$

o simplemente $1$ cuando el contexto determina el anillo.

Para $a\in R$, el inverso de $a$ en el grupo aditivo se escribe

$$
-a.
$$

Así,

$$
a+(-a)=(-a)+a=0_{\mathcal R}.
$$

La notación $a^{-1}$ seguirá reservada al inverso respecto de una operación multiplicativa cuando éste exista; no todo elemento de un anillo posee inverso multiplicativo.

---

## 14.3. El cero es absorbente para la multiplicación

### Proposición 14.3.1 — Absorción del cero {#talg-pro-00024}

Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo. Para todo $a\in R$,

$$
\boxed{
a\cdot0=0=0\cdot a
}.
$$

#### Demostración {#talg-prf-00036}

Como $0+0=0$, la distributividad por la izquierda da

$$
\begin{aligned}
a\cdot0
&=a\cdot(0+0)\\
&=(a\cdot0)+(a\cdot0).
\end{aligned}
$$

Sumemos el opuesto aditivo de $a\cdot0$ a ambos miembros. Usando asociatividad, inverso aditivo y neutro,

$$
\begin{aligned}
0
&=-(a\cdot0)+(a\cdot0)\\
&=-(a\cdot0)+\bigl((a\cdot0)+(a\cdot0)\bigr)\\
&=\bigl(-(a\cdot0)+(a\cdot0)\bigr)+(a\cdot0)\\
&=0+(a\cdot0)\\
&=a\cdot0.
\end{aligned}
$$

Por tanto $a\cdot0=0$.

De manera análoga, usando ahora distributividad por la derecha,

$$
0\cdot a=(0+0)\cdot a=(0\cdot a)+(0\cdot a),
$$

y sumando el opuesto aditivo de $0\cdot a$ se obtiene

$$
0\cdot a=0.
$$

$\square$

> **Punto lógico.** La absorción del cero no forma parte de la definición de anillo. Se deduce de distributividad y de la estructura de grupo aditivo.

---

## 14.4. Compatibilidad con los opuestos aditivos

### Proposición 14.4.1 — Reglas de signos {#talg-pro-00025}

Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo. Para cualesquiera $a,b\in R$,

$$
\boxed{
(-a)\cdot b=-(a\cdot b),
\qquad
a\cdot(-b)=-(a\cdot b),
\qquad
(-a)\cdot(-b)=a\cdot b
}.
$$

#### Demostración {#talg-prf-00037}

Por distributividad por la derecha,

$$
\begin{aligned}
((-a)+a)\cdot b
&=(-a)\cdot b+a\cdot b.
\end{aligned}
$$

El miembro izquierdo es $0\cdot b=0$ por la [Proposición 14.3.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00024). Luego

$$
(-a)\cdot b+a\cdot b=0.
$$

Así, $(-a)\cdot b$ es un inverso aditivo de $a\cdot b$. Por la unicidad del inverso ([Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002)) en el grupo aditivo,

$$
(-a)\cdot b=-(a\cdot b).
$$

Del mismo modo, por distributividad por la izquierda,

$$
a\cdot((-b)+b)=a\cdot(-b)+a\cdot b=0,
$$

de donde

$$
a\cdot(-b)=-(a\cdot b).
$$

Aplicando la segunda identidad con $a$ reemplazado por $-a$,

$$
(-a)\cdot(-b)=-\bigl((-a)\cdot b\bigr).
$$

La primera identidad da $(-a)\cdot b=-(a\cdot b)$. Por unicidad del inverso aditivo, el inverso de $-(a\cdot b)$ es $a\cdot b$. Por tanto,

$$
(-a)\cdot(-b)=a\cdot b.
$$

$\square$

---

## 14.5. Anillos conmutativos

### Definición 14.5.1 — Anillo conmutativo {#talg-def-00033}

Un **anillo conmutativo** es un anillo

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

cuya multiplicación es conmutativa:

$$
a\cdot b=b\cdot a
\qquad(a,b\in R).
$$

La suma ya es conmutativa por la definición de anillo, pues $\langle R,+\rangle$ es un grupo abeliano. Por tanto, el adjetivo *conmutativo* aplicado a un anillo se refiere exclusivamente a la multiplicación.

---

## 14.6. Cierre deductivo

Queda cerrada la primera interfaz de la Parte III:

```text
grupo abeliano aditivo
+
monoide multiplicativo
+
distributividad bilateral
        ↓
anillo unitario
        ↓
0, 1, opuesto aditivo
        ↓
absorción del cero
        ↓
reglas de signos
        ↓
anillo conmutativo
```

No se ha utilizado el axioma de elección.

El siguiente paso natural será distinguir los elementos multiplicativamente invertibles del anillo y estudiar su relación con el monoide multiplicativo antes de introducir divisores de cero y dominios.

---

[← **Capítulo 13 — Primer teorema de isomorfía para grupos**](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md) · [**Capítulo 15 — Unidades de un anillo** →](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md)
