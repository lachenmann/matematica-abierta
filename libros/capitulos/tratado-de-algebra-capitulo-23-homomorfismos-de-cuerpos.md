---
title: 'Tratado moderno de Álgebra — Capítulo 23: Homomorfismos de cuerpos'
description: Capítulo del Tratado moderno de Álgebra dedicado a homomorfismos de cuerpos, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0048
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
- MA-BCH-0047
related:
- MA-BOK-0007
- MA-BCH-0047
- MA-BCH-0049
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 23 — Homomorfismos de cuerpos

## 23.0. Propósito y convención

El capítulo anterior definió los cuerpos como anillos conmutativos, no triviales y con todos sus elementos no nulos invertibles. Corresponde ahora fijar la noción de morfismo compatible con esa estructura.

No introduciremos una clase de funciones nueva desde cero. La estructura de cuerpo contiene ya una estructura de anillo, y el tratado ha fijado previamente una convención unital para los homomorfismos de anillos. Por tanto, un homomorfismo de cuerpos será un homomorfismo de anillos entre cuerpos.

La decisión importante es que la **inyectividad no formará parte de la definición**. Se demostrará como consecuencia de la estructura del dominio. Esto separa con claridad:

```text
preservación algebraica
        ↓
homomorfismo de cuerpos
        ↓
estructura ideal del dominio
        ↓
inyectividad automática.
```

> **Contraste bibliográfico.** La terminología y la convención se contrastan con Dummit–Foote (`BIB-TALG-0001`), Aluffi (`BIB-TALG-0002`) y Lang (`BIB-TALG-0004`). Algunas presentaciones incorporan de hecho la inyectividad en el uso informal de “embebimiento de cuerpos”; aquí se mantendrán separadas la definición de homomorfismo y la propiedad de ser inyectivo. Las demostraciones son internas al tratado.

---

## 23.1. Homomorfismos de cuerpos

### Definición 23.1.1 — Homomorfismo de cuerpos {#talg-def-00050}

Sean

$$
\mathcal F=\langle F,+_F,\cdot_F\rangle,
\qquad
\mathcal K=\langle K,+_K,\cdot_K\rangle
$$

cuerpos. Una función

$$
f:F\to K
$$

se llama **homomorfismo de cuerpos** si es un homomorfismo de anillos en el sentido de la [Definición 17.2.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00039).

Equivalentemente, para todos $a,b\in F$,

$$
f(a+_F b)=f(a)+_K f(b),
$$

$$
f(a\cdot_F b)=f(a)\cdot_K f(b),
$$

y

$$
f(1_{\mathcal F})=1_{\mathcal K}.
$$

No se incorpora como axioma que $f$ preserve inversos multiplicativos, que envíe elementos no nulos en elementos no nulos ni que sea inyectiva. Esas propiedades se demostrarán a continuación.

> **Tipado.** La flecha $f:F\to K$ es una flecha entre los conjuntos subyacentes. Las estructuras $\mathcal F$ y $\mathcal K$ determinan qué propiedades algebraicas debe preservar esa función.

---

## 23.2. Identidad y composición

### Proposición 23.2.1 — Identidad y composición de homomorfismos de cuerpos {#talg-pro-00052}

1. La identidad de un cuerpo es un homomorfismo de cuerpos.
2. La composición de dos homomorfismos de cuerpos composables es un homomorfismo de cuerpos.

Más precisamente, si

$$
f:F\to K,
\qquad
g:K\to L
$$

son homomorfismos de cuerpos, entonces

$$
g\circ f:F\to L
$$

es un homomorfismo de cuerpos.

#### Demostración {#talg-prf-00083}

Por la [Definición 23.1.1](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-def-00050), un homomorfismo de cuerpos es, en particular, un homomorfismo de anillos. La [Proposición 17.2.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00033) demuestra que la identidad de un anillo es un homomorfismo de anillos y que la composición de homomorfismos de anillos vuelve a ser un homomorfismo de anillos.

Como los dominios y codominios considerados aquí son cuerpos, la especialización de esas dos afirmaciones satisface exactamente la [Definición 23.1.1](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-def-00050). Por tanto, la identidad y la composición permanecen dentro de la clase de homomorfismos de cuerpos. $\square$

---

## 23.3. Elementos no nulos e inversos

### Proposición 23.3.1 — Preservación de no nulidad e inversos multiplicativos {#talg-pro-00053}

Sea

$$
f:F\to K
$$

un homomorfismo de cuerpos y sea $a\in F$ con $a\neq0$. Entonces:

1. $f(a)\neq0$;
2.
   $$
   \boxed{
   f(a^{-1})=f(a)^{-1}.
   }
   $$

#### Demostración {#talg-prf-00084}

Como $a\neq0$ y $\mathcal F$ es un cuerpo, la [Proposición 22.2.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-pro-00049) da

$$
a\in F^\times.
$$

Por la [Proposición 17.2.4](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00034), los homomorfismos de anillos envían unidades en unidades. Puesto que la [Definición 23.1.1](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-def-00050) hace de $f$ un homomorfismo de anillos,

$$
f(a)\in K^\times.
$$

Aplicando nuevamente la [Proposición 22.2.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-pro-00049), ahora en el cuerpo $\mathcal K$, se obtiene

$$
f(a)\neq0.
$$

Además, $a^{-1}$ está definido por la [Notación 15.3.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-not-00013) y satisface

$$
aa^{-1}=a^{-1}a=1_{\mathcal F}.
$$

Como $f$ preserva producto y unidad,

$$
f(a)f(a^{-1})
=
f(aa^{-1})
=
f(1_{\mathcal F})
=
1_{\mathcal K},
$$

y, análogamente,

$$
f(a^{-1})f(a)=1_{\mathcal K}.
$$

Así, $f(a^{-1})$ es un inverso multiplicativo bilateral de $f(a)$. Por la unicidad demostrada en la [Proposición 15.2.1](tratado-de-algebra-capitulo-15-unidades-de-un-anillo.md#talg-pro-00026),

$$
f(a^{-1})=f(a)^{-1}.
$$

$\square$

> **Punto estructural.** La preservación de inversos no se añadió a la definición. Se deduce de la preservación de producto y unidad, junto con la unicidad del inverso.

---

## 23.4. Inyectividad automática

### Teorema 23.4.1 — Un homomorfismo unital desde un cuerpo hacia un anillo no trivial es inyectivo {#talg-thm-00016}

Sea $\mathcal F$ un cuerpo, sea $\mathcal R$ un anillo no trivial y sea

$$
f:F\to R
$$

un homomorfismo de anillos. Entonces $f$ es inyectivo.

#### Demostración {#talg-prf-00085}

Sean $a,b\in F$ y supongamos

$$
f(a)=f(b).
$$

Por aditividad y preservación de opuestos ([Proposición 17.2.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00032)),

$$
f(a-b)=f(a)-f(b)=0_{\mathcal R}.
$$

Supongamos $a\neq b$. Si $a-b=0_{\mathcal F}$, las leyes del grupo aditivo del anillo dan

$$
a=(a-b)+b=0_{\mathcal F}+b=b,
$$

contradicción. Por tanto $a-b\neq0_{\mathcal F}$. Como $\mathcal F$ es un cuerpo, la [Proposición 22.2.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-pro-00049) implica que $a-b$ es una unidad. La [Proposición 17.2.4](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00034) lleva unidades en unidades, luego

$$
f(a-b)=0_{\mathcal R}
$$

sería una unidad de $\mathcal R$. Pero $\mathcal R$ es no trivial y el [Corolario 16.1.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-cor-00005) da

$$
0_{\mathcal R}\notin R^\times,
$$

contradicción. Hemos probado $\neg(a\neq b)$, esto es, $\neg\neg(a=b)$. Aplicando DNE obtenemos $a=b$. Por consiguiente $f$ es inyectivo. $\square$

> **Lectura fundacional.** El argumento constructivo previo a DNE obtiene $f(a)=f(b)\Rightarrow\neg\neg(a=b)$. La inyectividad ordinaria requiere estabilidad de la igualdad en el dominio; bajo la lógica clásica del tratado se obtiene por DNE.

> **Generalidad deliberada.** El codominio no necesita ser un cuerpo, ni siquiera conmutativo. Basta que sea un anillo no trivial y que $f$ sea un homomorfismo de anillos en nuestra convención unital.

---

### Corolario 23.4.2 — Todo homomorfismo de cuerpos es inyectivo {#talg-cor-00014}

Todo homomorfismo de cuerpos

$$
f:F\to K
$$

es inyectivo.

#### Demostración {#talg-prf-00086}

Por la [Definición 23.1.1](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-def-00050), $f$ es un homomorfismo de anillos. El codominio $\mathcal K$ es un cuerpo y, por la [Definición 22.1.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048), todo cuerpo es un anillo no trivial. Por el [Teorema 23.4.1](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-thm-00016), $f$ es inyectivo. $\square$

> **Consecuencia conceptual.** Entre cuerpos, todo homomorfismo unital es automáticamente inyectivo como función entre los conjuntos subyacentes. Por eso no se incorporó la inyectividad a la definición.

---

## 23.5. La imagen de un homomorfismo de cuerpos

### Proposición 23.5.1 — La imagen determina un subcuerpo del codominio {#talg-pro-00054}

Sea

$$
f:F\to K
$$

un homomorfismo de cuerpos. Entonces la imagen

$$
\operatorname{im}f
=
\{f(a):a\in F\}
$$

determina un subcuerpo de $\mathcal K$.

#### Demostración {#talg-prf-00087}

Por la [Definición 23.1.1](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-def-00050), $f$ es un homomorfismo de anillos. Entonces la [Proposición 17.3.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00035) demuestra que $\operatorname{im}f$ determina un subanillo unital de $\mathcal K$.

Resta verificar el cierre bajo inversos multiplicativos de elementos no nulos. Sea

$$
y\in\operatorname{im}f
$$

con $y\neq0$. Por definición de imagen, existe $a\in F$ tal que

$$
y=f(a).
$$

Si $a=0$, la [Proposición 17.2.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00032) daría

$$
y=f(0)=0,
$$

contradicción. Por tanto,

$$
a\neq0.
$$

Aplicando la [Proposición 23.3.1](tratado-de-algebra-capitulo-23-homomorfismos-de-cuerpos.md#talg-pro-00053),

$$
y^{-1}
=
f(a)^{-1}
=
f(a^{-1}).
$$

Como $a^{-1}\in F$, resulta

$$
f(a^{-1})\in\operatorname{im}f.
$$

Por consiguiente, todo elemento no nulo de $\operatorname{im}f$ tiene su inverso ambiente dentro de $\operatorname{im}f$. Junto con la estructura de subanillo ya obtenida, la [Definición 22.5.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00049) implica que $\operatorname{im}f$ determina un subcuerpo de $\mathcal K$. $\square$

No se ha utilizado el axioma de elección. La obtención de un preimagen $a$ para un elemento fijo $y\in\operatorname{im}f$ es una eliminación ordinaria del cuantificador existencial que forma parte de la definición de pertenencia a la imagen; no se construye una selección simultánea de preimágenes.

---

## 23.6. Cierre deductivo

Queda cerrada la cadena

```text
cuerpo
  ↓
homomorfismo de cuerpos = homomorfismo unital de anillos entre cuerpos
  ↓
identidad y composición
  ↓
no nulos → no nulos
  ↓
f(a⁻¹) = f(a)⁻¹
  ↓
ker(f) ideal propio del cuerpo
  ↓
ker(f) = {0}
  ↓
f inyectivo
  ↓
im(f) subanillo + cierre bajo inversos
  ↓
im(f) subcuerpo
```

No se ha utilizado el axioma de elección y no se ha abierto ninguna nueva arista intertratados.

El siguiente bloque de la Parte IV será la **construcción del cuerpo de fracciones de un dominio íntegro**. El primer paso será aislar el conjunto de pares con denominador no nulo antes de introducir la relación de equivalencia que representará igualdad de fracciones.

---

[← **Capítulo 22 — Cuerpos y subcuerpos**](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md) · [**Capítulo 24 — Cuerpo de fracciones de un dominio íntegro** →](tratado-de-algebra-capitulo-24-cuerpo-de-fracciones-de-un-dominio-integro.md)
