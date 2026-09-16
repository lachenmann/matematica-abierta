---
title: "Tratado moderno de Álgebra — Capítulo 8: Isomorfismos"
description: "Isomorfismos como homomorfismos biyectivos, con inversión, identidad, composición y relación de isomorfía para magmas, semigrupos, monoides y grupos."
author: "Gustav A. Tachek"
content-id: MA-BCH-0033
content-type: book-chapter
book-id: MA-BOK-0007
status: published
date-created: 2026-09-15
date-modified: 2026-09-16
areas:
  - algebra
  - fundamentos
level: avanzado
topics:
  - isomorfismos
  - homomorfismos
  - biyectividad
  - funcion-inversa
  - magmas
  - semigrupos
  - monoides
  - grupos
prerequisites:
  - MA-BCH-0032
  - MA-BCH-0022
related:
  - MA-BOK-0007
  - MA-BCH-0022
  - MA-BCH-0024
  - MA-BCH-0025
  - MA-BCH-0026
  - MA-BCH-0027
  - MA-BCH-0032
  - MA-BCH-0034
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 8 — Isomorfismos

**Coordenada deductiva:** `TALG-0012`

[**← Volver al Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md)

## 8.0. Propósito

Un homomorfismo expresa compatibilidad entre operaciones. Un **isomorfismo** añade la exigencia de que esa compatibilidad sea reversible: la función subyacente debe ser biyectiva y su inversa debe recuperar la estructura sin pérdida.

La biyectividad y la función inversa ya están disponibles mediante [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002). En este capítulo se combinarán con la teoría de homomorfismos de [`TALG-0010`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md).

La política sigue siendo separar las dos capas:

- **capa conjuntista:** función, biyectividad, inversa funcional;
- **capa algebraica:** preservación de la operación y, cuando corresponda, del neutro.

---

## 8.1. Isomorfismos de magmas

### Definición 8.1.1 — Isomorfismo de magmas {#talg-def-00020}

**Coordenada:** [`TALG-DEF-00020`](#talg-def-00020)

**Dependencias deductivas:** [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) — interfaz funcional: biyectividad e inversas; [`TALG-DEF-00016`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00016) — homomorfismo de magmas.

Sean
$$
\mathcal M=\langle A,\star\rangle,
\qquad
\mathcal N=\langle B,\diamond\rangle
$$
magmas. Una función
$$
f:A\to B
$$
es un **isomorfismo de magmas** si:

1. $f$ es un homomorfismo de magmas;
2. $f$ es biyectiva.

La primera condición pertenece a la estructura algebraica; la segunda, a la función subyacente.

---

### Proposición 8.1.2 — La inversa de un isomorfismo de magmas es un isomorfismo {#talg-pro-00009}

**Coordenada:** [`TALG-PRO-00009`](#talg-pro-00009)

**Dependencias deductivas:** [`TALG-DEF-00020`](#talg-def-00020) — isomorfismo de magmas; [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) — interfaz funcional: biyectividad e inversas.

Sean
$$
\mathcal M=\langle A,\star\rangle,
\qquad
\mathcal N=\langle B,\diamond\rangle
$$
magmas y sea
$$
f:A\to B
$$
un isomorfismo. Entonces la función inversa
$$
f^{-1}:B\to A
$$
es un isomorfismo de $\mathcal N$ en $\mathcal M$.

#### Demostración {#talg-prf-00012}

**Coordenada de prueba:** [`TALG-PRF-00012`](#talg-prf-00012)

Como $f$ es biyectiva, [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) autoriza la función inversa $f^{-1}:B\to A$ y proporciona
$$
f^{-1}\circ f=\operatorname{id}_A,
\qquad
f\circ f^{-1}=\operatorname{id}_B.
$$

Sean $u,v\in B$ y pongamos
$$
x:=f^{-1}(u),
\qquad
y:=f^{-1}(v).
$$
Entonces $f(x)=u$ y $f(y)=v$. Como $f$ es homomorfismo,
$$
f(x\star y)=f(x)\diamond f(y)=u\diamond v.
$$
Aplicando $f^{-1}$,
$$
x\star y=f^{-1}(u\diamond v).
$$
Sustituyendo $x=f^{-1}(u)$ e $y=f^{-1}(v)$,
$$
f^{-1}(u\diamond v)
=
f^{-1}(u)\star f^{-1}(v).
$$
Por tanto $f^{-1}$ es un homomorfismo de magmas.

Además, $f$ es una inversa bilateral de $f^{-1}$, de modo que [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) implica que $f^{-1}$ es biyectiva. Luego $f^{-1}$ es un isomorfismo. $\square$

---

### Proposición 8.1.3 — Identidad y composición de isomorfismos de magmas {#talg-pro-00010}

**Coordenada:** [`TALG-PRO-00010`](#talg-pro-00010)

**Dependencias deductivas:** [`TALG-DEF-00020`](#talg-def-00020) — isomorfismo de magmas; [`TALG-PRO-00006`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00006) — identidad y composición de homomorfismos de magmas; [`TALG-PRO-00009`](#talg-pro-00009) — inversa de un isomorfismo de magmas; [`TALG-IMP-00001`](tratado-de-algebra-capitulo-0-interfaz-fundacional.md#talg-imp-00001) — interfaz fundacional de funciones; [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) — interfaz funcional: biyectividad e inversas.

Sean
$$
\mathcal M=\langle A,\star\rangle,
\quad
\mathcal N=\langle B,\diamond\rangle,
\quad
\mathcal P=\langle C,\triangle\rangle
$$
magmas.

1. $\operatorname{id}_A:A\to A$ es un isomorfismo de $\mathcal M$ consigo mismo.
2. Si $f:A\to B$ es un isomorfismo de $\mathcal M$ en $\mathcal N$ y $g:B\to C$ es un isomorfismo de $\mathcal N$ en $\mathcal P$, entonces
   $$
   g\circ f:A\to C
   $$
   es un isomorfismo de $\mathcal M$ en $\mathcal P$.

#### Demostración {#talg-prf-00013}

**Coordenada de prueba:** [`TALG-PRF-00013`](#talg-prf-00013)

Por [`TALG-PRO-00006`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00006), la identidad es un homomorfismo de magmas. Ella misma es una inversa bilateral de sí misma; por [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002), es biyectiva. Luego es un isomorfismo.

Ahora sean $f$ y $g$ isomorfismos. Por [`TALG-PRO-00006`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00006), $g\circ f$ es homomorfismo. Por [`TALG-PRO-00009`](#talg-pro-00009), existen isomorfismos inversos
$$
f^{-1}:B\to A,
\qquad
g^{-1}:C\to B.
$$
Consideremos
$$
h:=f^{-1}\circ g^{-1}:C\to A.
$$
Verificaremos directamente, por evaluación, que $h$ es inversa bilateral de $g\circ f$, sin invocar ninguna ley adicional de asociatividad de la composición.

Sea $a\in A$. Entonces
$$
\begin{aligned}
h((g\circ f)(a))
&=f^{-1}(g^{-1}(g(f(a))))\\
&=f^{-1}(f(a))\\
&=a.
\end{aligned}
$$
Por tanto,
$$
h\circ(g\circ f)=\operatorname{id}_A.
$$

Sea ahora $c\in C$. Entonces
$$
\begin{aligned}
(g\circ f)(h(c))
&=g(f(f^{-1}(g^{-1}(c))))\\
&=g(g^{-1}(c))\\
&=c.
\end{aligned}
$$
Por tanto,
$$
(g\circ f)\circ h=\operatorname{id}_C.
$$

Por [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002), $g\circ f$ es biyectiva. Luego es un isomorfismo. $\square$

---

## 8.2. Isomorfismos de semigrupos, monoides y grupos

### Definición 8.2.1 — Isomorfismo de semigrupos {#talg-def-00021}

**Coordenada:** [`TALG-DEF-00021`](#talg-def-00021)

**Dependencias deductivas:** [`TALG-DEF-00017`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00017) — homomorfismo de semigrupos; [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) — interfaz funcional: biyectividad e inversas.

Sean semigrupos
$$
\mathcal S=\langle S,\star\rangle,
\qquad
\mathcal T=\langle T,\diamond\rangle.
$$
Una función $f:S\to T$ es un **isomorfismo de semigrupos** si es un homomorfismo de semigrupos y es biyectiva.

---

### Definición 8.2.2 — Isomorfismo de monoides {#talg-def-00022}

**Coordenada:** [`TALG-DEF-00022`](#talg-def-00022)

**Dependencias deductivas:** [`TALG-DEF-00018`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00018) — homomorfismo de monoides; [`TALG-NOT-00002`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-not-00002) — notación del neutro; [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) — interfaz funcional: biyectividad e inversas.

Sean monoides
$$
\mathcal M=\langle M,\star\rangle,
\qquad
\mathcal N=\langle N,\diamond\rangle.
$$
Una función $f:M\to N$ es un **isomorfismo de monoides** si es un homomorfismo de monoides y es biyectiva.

En particular, además de preservar la operación, satisface
$$
f(e_{\mathcal M})=e_{\mathcal N}.
$$

---

### Definición 8.2.3 — Isomorfismo de grupos {#talg-def-00023}

**Coordenada:** [`TALG-DEF-00023`](#talg-def-00023)

**Dependencias deductivas:** [`TALG-DEF-00019`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019) — homomorfismo de grupos; [`TALG-PRO-00007`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007) — preservación del neutro; [`TALG-PRO-00008`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008) — preservación de inversos; [`TALG-IMP-00002`](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002) — interfaz funcional: biyectividad e inversas.

Sean grupos
$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle.
$$
Una función $f:G\to H$ es un **isomorfismo de grupos** si es un homomorfismo de grupos y es biyectiva.

No se añade una condición separada sobre neutros o inversos: por [`TALG-PRO-00007`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007) y [`TALG-PRO-00008`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008), todo homomorfismo de grupos ya los preserva.

---

### Proposición 8.2.4 — Las inversas preservan el tipo de isomorfismo {#talg-pro-00011}

**Coordenada:** [`TALG-PRO-00011`](#talg-pro-00011)

**Dependencias deductivas:** [`TALG-PRO-00009`](#talg-pro-00009) — inversa de un isomorfismo de magmas; [`TALG-DEF-00017`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00017) — homomorfismo de semigrupos; [`TALG-DEF-00018`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00018) — homomorfismo de monoides; [`TALG-DEF-00019`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019) — homomorfismo de grupos; [`TALG-DEF-00021`](#talg-def-00021) — isomorfismo de semigrupos; [`TALG-DEF-00022`](#talg-def-00022) — isomorfismo de monoides; [`TALG-DEF-00023`](#talg-def-00023) — isomorfismo de grupos; [`TALG-NOT-00002`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-not-00002) — notación del neutro.

La inversa funcional de un isomorfismo de semigrupos, monoides o grupos es, respectivamente, un isomorfismo del mismo tipo en sentido contrario.

#### Demostración {#talg-prf-00014}

**Coordenada de prueba:** [`TALG-PRF-00014`](#talg-prf-00014)

Para semigrupos, [`TALG-PRO-00009`](#talg-pro-00009) muestra que la inversa es un isomorfismo de los magmas subyacentes; por [`TALG-DEF-00017`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00017) y [`TALG-DEF-00021`](#talg-def-00021), esto basta para obtener un isomorfismo de semigrupos.

Para monoides, sea $f:M\to N$ un isomorfismo. Por [`TALG-PRO-00009`](#talg-pro-00009), $f^{-1}$ preserva la operación y es biyectiva. Además,
$$
f(e_{\mathcal M})=e_{\mathcal N}.
$$
Aplicando $f^{-1}$,
$$
f^{-1}(e_{\mathcal N})=e_{\mathcal M}.
$$
Por tanto $f^{-1}$ es homomorfismo de monoides y, siendo biyectiva, isomorfismo de monoides.

Para grupos, [`TALG-PRO-00009`](#talg-pro-00009) proporciona preservación de la operación y biyectividad de la inversa. Como [`TALG-DEF-00019`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019) no exige condiciones adicionales, $f^{-1}$ es un homomorfismo de grupos y por [`TALG-DEF-00023`](#talg-def-00023) un isomorfismo de grupos. $\square$

---

### Proposición 8.2.5 — Identidades y composiciones preservan el tipo de isomorfismo {#talg-pro-00012}

**Coordenada:** [`TALG-PRO-00012`](#talg-pro-00012)

**Dependencias deductivas:** [`TALG-PRO-00010`](#talg-pro-00010) — identidad y composición de isomorfismos de magmas; [`TALG-DEF-00017`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00017) — homomorfismo de semigrupos; [`TALG-DEF-00018`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00018) — homomorfismo de monoides; [`TALG-DEF-00019`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019) — homomorfismo de grupos; [`TALG-DEF-00021`](#talg-def-00021) — isomorfismo de semigrupos; [`TALG-DEF-00022`](#talg-def-00022) — isomorfismo de monoides; [`TALG-DEF-00023`](#talg-def-00023) — isomorfismo de grupos; [`TALG-NOT-00002`](tratado-de-algebra-capitulo-3-elementos-neutros-y-monoides.md#talg-not-00002) — notación del neutro.

Dentro de cada una de las clases de semigrupos, monoides y grupos:

1. la identidad de una estructura es un isomorfismo;
2. la composición de dos isomorfismos composables es un isomorfismo.

#### Demostración {#talg-prf-00015}

**Coordenada de prueba:** [`TALG-PRF-00015`](#talg-prf-00015)

Para semigrupos y grupos, [`TALG-PRO-00010`](#talg-pro-00010) ya garantiza identidad y composición como isomorfismos de los magmas subyacentes; las definiciones correspondientes no añaden condiciones funcionales nuevas.

Para monoides, la identidad preserva evidentemente el neutro. Si
$$
f:M\to N,
\qquad
g:N\to P
$$
son isomorfismos de monoides, entonces
$$
(g\circ f)(e_{\mathcal M})
=
g(f(e_{\mathcal M}))
=
g(e_{\mathcal N})
=
e_{\mathcal P}.
$$
[`TALG-PRO-00010`](#talg-pro-00010) proporciona además preservación de la operación y biyectividad de la composición. Por [`TALG-DEF-00022`](#talg-def-00022), $g\circ f$ es un isomorfismo de monoides. $\square$

---

## 8.3. Notación y relación de isomorfía

### Notación 8.3.1 — Isomorfía {#talg-not-00005}

**Coordenada:** [`TALG-NOT-00005`](#talg-not-00005)

**Dependencias deductivas:** [`TALG-DEF-00020`](#talg-def-00020) — isomorfismo de magmas; [`TALG-DEF-00021`](#talg-def-00021) — isomorfismo de semigrupos; [`TALG-DEF-00022`](#talg-def-00022) — isomorfismo de monoides; [`TALG-DEF-00023`](#talg-def-00023) — isomorfismo de grupos.

Cuando dos estructuras del mismo tipo estén relacionadas por al menos un isomorfismo del tipo correspondiente, escribiremos
$$
\mathcal A\cong\mathcal B.
$$
El contexto debe determinar si se habla de magmas, semigrupos, monoides o grupos. El símbolo $\cong$ afirma existencia de un isomorfismo; no identifica literalmente las dos estructuras.

---

### Proposición 8.3.2 — Reflexividad, simetría y transitividad de la isomorfía {#talg-pro-00013}

**Coordenada:** [`TALG-PRO-00013`](#talg-pro-00013)

**Dependencias deductivas:** [`TALG-NOT-00005`](#talg-not-00005) — notación de isomorfía; [`TALG-PRO-00009`](#talg-pro-00009) — inversa de un isomorfismo de magmas; [`TALG-PRO-00010`](#talg-pro-00010) — identidad y composición de isomorfismos de magmas; [`TALG-PRO-00011`](#talg-pro-00011) — inversas preservan el tipo de isomorfismo; [`TALG-PRO-00012`](#talg-pro-00012) — identidades y composiciones preservan el tipo.

Para cada tipo fijo entre magmas, semigrupos, monoides y grupos, la relación de isomorfía es reflexiva, simétrica y transitiva.

#### Demostración {#talg-prf-00016}

**Coordenada de prueba:** [`TALG-PRF-00016`](#talg-prf-00016)

La reflexividad viene dada por el isomorfismo identidad. La simetría viene dada por la inversa de un isomorfismo. La transitividad viene dada por la composición. Para magmas se usan [`TALG-PRO-00009`](#talg-pro-00009) y [`TALG-PRO-00010`](#talg-pro-00010); para semigrupos, monoides y grupos se usan [`TALG-PRO-00011`](#talg-pro-00011) y [`TALG-PRO-00012`](#talg-pro-00012). $\square$

---

### Corolario 8.3.3 — Todo isomorfismo de grupos es un isomorfismo de monoides {#talg-cor-00002}

**Coordenada:** [`TALG-COR-00002`](#talg-cor-00002)

**Dependencias deductivas:** [`TALG-DEF-00022`](#talg-def-00022) — isomorfismo de monoides; [`TALG-DEF-00023`](#talg-def-00023) — isomorfismo de grupos; [`TALG-COR-00001`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-cor-00001) — todo homomorfismo de grupos es homomorfismo de monoides.

Sean grupos $\mathcal G$ y $\mathcal H$. Todo isomorfismo de grupos $f:G\to H$ es, al considerar ambos grupos como monoides, un isomorfismo de monoides.

#### Demostración {#talg-prf-00017}

**Coordenada de prueba:** [`TALG-PRF-00017`](#talg-prf-00017)

Por [`TALG-COR-00001`](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-cor-00001), $f$ es un homomorfismo de monoides. Por hipótesis de isomorfismo de grupos, $f$ es biyectiva. Éstas son exactamente las condiciones de [`TALG-DEF-00022`](#talg-def-00022). $\square$

---

## 8.4. Lectura estructural

Hasta este punto la noción de isomorfismo queda completamente separada de la igualdad literal:

$$
\mathcal A=\mathcal B
\quad\Longrightarrow\quad
\mathcal A\cong\mathcal B,
$$

cuando la igualdad literal tiene sentido para estructuras del mismo tipo, pero en general

$$
\mathcal A\cong\mathcal B
$$

sólo afirma que existe una traducción biyectiva que preserva la estructura pertinente.

El tratado no sustituirá estructuras isomorfas por estructuras iguales sin una identificación explícita. Esta distinción será crucial al construir cocientes, cuerpos de fracciones, completaciones y espacios vectoriales.

---

## Cierre deductivo

- **Fundamento:** ZF + lógica clásica.
- **Axioma de elección:** no utilizado.
- **Isomorfismo de magmas:** [`TALG-DEF-00020`](#talg-def-00020).
- **Inversa de un isomorfismo de magmas:** [`TALG-PRO-00009`](#talg-pro-00009), con prueba [`TALG-PRF-00012`](#talg-prf-00012).
- **Identidad y composición en magmas:** [`TALG-PRO-00010`](#talg-pro-00010), con prueba [`TALG-PRF-00013`](#talg-prf-00013).
- **Isomorfismo de semigrupos:** [`TALG-DEF-00021`](#talg-def-00021).
- **Isomorfismo de monoides:** [`TALG-DEF-00022`](#talg-def-00022).
- **Isomorfismo de grupos:** [`TALG-DEF-00023`](#talg-def-00023).
- **Inversas preservan el tipo:** [`TALG-PRO-00011`](#talg-pro-00011), con prueba [`TALG-PRF-00014`](#talg-prf-00014).
- **Identidad y composición preservan el tipo:** [`TALG-PRO-00012`](#talg-pro-00012), con prueba [`TALG-PRF-00015`](#talg-prf-00015).
- **Notación de isomorfía:** [`TALG-NOT-00005`](#talg-not-00005).
- **Isomorfía como relación reflexiva, simétrica y transitiva:** [`TALG-PRO-00013`](#talg-pro-00013), con prueba [`TALG-PRF-00016`](#talg-prf-00016).
- **Isomorfismos de grupos y monoides:** [`TALG-COR-00002`](#talg-cor-00002), con prueba [`TALG-PRF-00017`](#talg-prf-00017).
- **Circularidad:** ninguna.
- **Siguiente nodo:** [`TALG-DEF-00024`](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-def-00024) — núcleo de un homomorfismo de grupos.

---

[← **Capítulo 7 — Homomorfismos de magmas, monoides y grupos**](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md) · [**Capítulo 9 — Núcleo e imagen de homomorfismos de grupos** →](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md)
