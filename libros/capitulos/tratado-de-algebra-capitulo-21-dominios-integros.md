---
title: 'Tratado moderno de Álgebra — Capítulo 21: Dominios íntegros'
description: Capítulo del Tratado moderno de Álgebra dedicado a dominios íntegros, publicado desde la fuente canónica cerrada del tratado.
author: Gustav A. Tachek
content-id: MA-BCH-0046
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
- MA-BCH-0045
related:
- MA-BOK-0007
- MA-BCH-0045
- MA-BCH-0047
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 21 — Dominios íntegros

## 21.0. Propósito y posición deductiva

La teoría construida hasta aquí permite aislar una clase fundamental de anillos conmutativos. Ya disponemos de:

1. la noción de anillo conmutativo ([Definición 14.5.1](tratado-de-algebra-capitulo-14-anillos.md#talg-def-00033));
2. la separación entre anillos triviales y no triviales ([Definición 16.1.1](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00035));
3. la noción de divisor de cero en el caso conmutativo ([Definición 16.5.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00037));
4. la equivalencia entre ausencia de divisores de cero y cancelación por un factor no nulo ([Corolario 16.5.3](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-cor-00007)).

Estas cuatro piezas permiten definir un **dominio íntegro** sin introducir nueva estructura: se trata de un anillo conmutativo, no trivial, en el que el producto de dos elementos no nulos nunca puede ser cero.

La importancia deductiva de la noción es doble. Por una parte, la ausencia de divisores de cero se reformula en la conocida **ley del producto nulo**,

$$
ab=0\Longrightarrow a=0\ \text{o}\ b=0,
$$

y, por otra, todos los elementos no nulos pueden cancelarse multiplicativamente. Estas formas serán las que más tarde se reutilicen al construir cuerpos y cuerpos de fracciones.

> **Contraste bibliográfico.** La convención se contrasta con Dummit–Foote (`BIB-TALG-0001`), Atiyah–Macdonald (`BIB-TALG-0007`) y Lam (`BIB-TALG-0008`). En este tratado, “dominio íntegro” significa siempre **anillo conmutativo unitario, no trivial y sin divisores de cero no nulos**. Las demostraciones se desarrollan internamente.

---

## 21.1. Dominio íntegro

### Definición 21.1.1 — Dominio íntegro {#talg-def-00047}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo. Diremos que $\mathcal R$ es un **dominio íntegro** si se cumplen simultáneamente:

1. $\mathcal R$ es conmutativo;
2. $\mathcal R$ es no trivial, es decir,
   $$
   0\neq1;
   $$
3. $\mathcal R$ no posee divisores de cero en el sentido de la [Definición 16.5.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00037).

Equivalentemente, la tercera condición afirma que no existen $a,b\in R$ tales que

$$
a\neq0,\qquad b\neq0,\qquad ab=0.
$$

La palabra “íntegro” no añade una operación ni un dato auxiliar. Designa una propiedad conjunta de la multiplicación, la conmutatividad y la no trivialidad del anillo.

> **Convención terminológica.** En este tratado no se llamará “dominio íntegro” a un anillo no conmutativo sin divisores de cero. La conmutatividad forma parte de la definición.

---

## 21.2. Caracterizaciones equivalentes

### Teorema 21.2.1 — Caracterizaciones del dominio íntegro {#talg-thm-00013}

Sea $\mathcal R=\langle R,+,\cdot\rangle$ un anillo conmutativo. Son equivalentes:

1. $\mathcal R$ es un dominio íntegro.

2. $\mathcal R$ es no trivial y satisface la **ley del producto nulo**:
   $$
   \forall a,b\in R,
   \qquad
   ab=0
   \Longrightarrow
   (a=0\ \lor\ b=0).
   $$

3. $\mathcal R$ es no trivial y todo elemento no nulo es cancelable multiplicativamente:
   $$
   \forall a\in R,\quad
   a\neq0
   \Longrightarrow
   \forall x,y\in R,\quad
   ax=ay\Longrightarrow x=y.
   $$

#### Demostración {#talg-prf-00074}

**(1) $\Longrightarrow$ (2).**  
Supongamos que $\mathcal R$ es un dominio íntegro. La no trivialidad forma parte de la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047).

Sean ahora $a,b\in R$ y supongamos

$$
ab=0.
$$

Por LEM, o bien $a=0$, en cuyo caso la conclusión ya está obtenida, o bien $a\neq0$. En el segundo caso, si $b\neq0$, la [Definición 16.5.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00037) implicaría que $a$ es un divisor de cero, contradiciendo la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047). Por tanto $\neg(b\neq0)$, es decir, $\neg\neg(b=0)$. Aplicando DNE obtenemos

$$
b=0.
$$

En consecuencia,

$$
ab=0\Longrightarrow a=0\ \lor\ b=0.
$$

**(2) $\Longrightarrow$ (1).**  
Supongamos que $\mathcal R$ es no trivial y satisface la ley del producto nulo.

Si existiera un divisor de cero $a$, la [Definición 16.5.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00037) proporcionaría un elemento $b\neq0$ tal que

$$
a\neq0
\qquad\text{y}\qquad
ab=0.
$$

La ley del producto nulo daría

$$
a=0\ \lor\ b=0,
$$

en contradicción con las dos desigualdades anteriores. Por tanto no existen divisores de cero. Como $\mathcal R$ ya es conmutativo y no trivial, la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047) implica que es un dominio íntegro.

**(1) $\Longleftrightarrow$ (3).**  
Por el [Corolario 16.5.3](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-cor-00007), en todo anillo conmutativo no trivial y para cada $a\neq0$,

$$
a\text{ no es divisor de cero}
\quad\Longleftrightarrow\quad
\forall x,y\in R,\;
ax=ay\Longrightarrow x=y.
$$

Ahora bien, la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047) afirma precisamente que en un dominio íntegro no existe ningún divisor de cero no nulo. Por tanto, exigir que todos los elementos $a\neq0$ no sean divisores de cero equivale a exigir que todos esos elementos satisfagan la ley de cancelación. Esto establece la equivalencia entre (1) y (3).

Las tres condiciones son equivalentes. $\square$

> **Lectura fundacional.** Bajo la definición negativa actual de dominio íntegro, las implicaciones hacia la ley positiva del producto nulo y hacia cancelación usan lógica clásica. Las implicaciones desde esas propiedades positivas hacia la ausencia de divisores de cero son constructivamente compatibles.

---

## 21.3. Dos formas operativas

### Corolario 21.3.1 — Ley del producto nulo en un dominio íntegro {#talg-cor-00012}

Sea $\mathcal R$ un dominio íntegro. Para todos $a,b\in R$,

$$
\boxed{
ab=0
\quad\Longleftrightarrow\quad
a=0\ \lor\ b=0.
}
$$

#### Demostración {#talg-prf-00075}

La implicación

$$
ab=0\Longrightarrow a=0\ \lor\ b=0
$$

es la condición (2) del [Teorema 21.2.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-thm-00013).

Recíprocamente, si $a=0$, la [Proposición 14.3.1](tratado-de-algebra-capitulo-14-anillos.md#talg-pro-00024) da

$$
ab=0b=0.
$$

Si $b=0$, la misma proposición da

$$
ab=a0=0.
$$

Por tanto,

$$
a=0\ \lor\ b=0
\Longrightarrow
ab=0.
$$

$\square$

---

### Corolario 21.3.2 — Cancelación multiplicativa en un dominio íntegro {#talg-cor-00013}

Sea $\mathcal R$ un dominio íntegro y sea $a\in R$ con $a\neq0$. Entonces, para todos $x,y\in R$,

$$
\boxed{
ax=ay\Longrightarrow x=y
}
$$

y, equivalentemente,

$$
\boxed{
xa=ya\Longrightarrow x=y.
}
$$

#### Demostración {#talg-prf-00076}

La primera implicación es exactamente la condición (3) del [Teorema 21.2.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-thm-00013).

Para la segunda, si

$$
xa=ya,
$$

la conmutatividad multiplicativa da

$$
ax=ay.
$$

Aplicando la primera implicación se obtiene $x=y$.

$\square$

> **Advertencia.** La hipótesis $a\neq0$ es esencial. Cancelar un factor cero produciría conclusiones falsas en cualquier anillo no trivial.

---

## 21.4. Herencia por subanillos

### Proposición 21.4.1 — Todo subanillo de un dominio íntegro es un dominio íntegro {#talg-pro-00048}

Sea $\mathcal R=\langle R,+,\cdot\rangle$ un dominio íntegro y sea

$$
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

un subanillo de $\mathcal R$ en el sentido unital de la [Definición 17.1.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00038). Entonces $\mathcal S$ es un dominio íntegro.

#### Demostración {#talg-prf-00077}

Como $\mathcal R$ es un dominio íntegro, es conmutativo y no trivial. Por la [Proposición 17.1.4](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00031), la conmutatividad desciende al subanillo y, además,

$$
\mathcal S\text{ es no trivial}.
$$

Resta verificar que $\mathcal S$ no posee divisores de cero en el sentido negativo de la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047). Supongamos, para obtener contradicción, que $a\in S$ es un divisor de cero de $\mathcal S$. Por la [Definición 16.5.2](tratado-de-algebra-capitulo-16-no-trivialidad-y-divisores-de-cero.md#talg-def-00037) existe $b\in S$ tal que

$$
a\neq0_{\mathcal S},\qquad b\neq0_{\mathcal S},\qquad a\cdot_S b=0_{\mathcal S}.
$$

Por la [Proposición 17.1.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00030), las operaciones de $\mathcal S$ son restricciones de las de $\mathcal R$ y

$$
0_{\mathcal S}=0_{\mathcal R}.
$$

Por tanto, en el anillo ambiente tenemos

$$
a\neq0_{\mathcal R},\qquad b\neq0_{\mathcal R},\qquad ab=0_{\mathcal R}.
$$

Así $a$ sería un divisor de cero de $\mathcal R$, contradiciendo que $\mathcal R$ sea un dominio íntegro según la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047). En consecuencia, $\mathcal S$ no posee divisores de cero. Junto con conmutatividad y no trivialidad, la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047) implica que $\mathcal S$ es un dominio íntegro.

$\square$

---

## 21.5. Frontera conceptual con los cuerpos

Un dominio íntegro garantiza dos propiedades multiplicativas decisivas:

```text
producto nulo
    ↓
uno de los factores es cero

factor no nulo
    ↓
cancelación multiplicativa
```

Pero **no** se ha exigido que todo elemento no nulo posea inverso multiplicativo. Esa condición será estrictamente más fuerte y pertenecerá a la Parte IV.

Por tanto, en este punto del tratado deben mantenerse separadas tres capas:

1. **anillo conmutativo no trivial:** no impone ausencia de divisores de cero;
2. **dominio íntegro:** añade ausencia de divisores de cero;
3. **cuerpo:** añadirá invertibilidad de todo elemento no nulo.

La noción de anillo de división, si se introduce posteriormente, se tratará por separado y no se identificará con la de dominio íntegro, pues la conmutatividad forma parte de la [Definición 21.1.1](tratado-de-algebra-capitulo-21-dominios-integros.md#talg-def-00047).

---

## 21.6. Cierre deductivo

Queda cerrada la cadena

```text
anillo conmutativo
+ no trivialidad
+ ausencia de divisores de cero
        ↓
dominio íntegro
        ↓
ley del producto nulo
        ↓
cancelación por todo factor no nulo
        ↓
herencia por subanillos unitarios
```

No se ha utilizado el axioma de elección. No se ha abierto ninguna nueva dependencia intertratados.

Con este capítulo queda cerrada la sección **3.5 — Dominios íntegros** y, con ella, la Parte III en su arquitectura actual. El siguiente nodo canónico abre la Parte IV:

$$
\boxed{\text{[Definición 22.1.1](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md#talg-def-00048) — Cuerpo}.}
$$

---

[← **Capítulo 20 — Isomorfismos y primer teorema de isomorfía para anillos**](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md) · [**Capítulo 22 — Cuerpos y subcuerpos** →](tratado-de-algebra-capitulo-22-cuerpos-y-subcuerpos.md)
