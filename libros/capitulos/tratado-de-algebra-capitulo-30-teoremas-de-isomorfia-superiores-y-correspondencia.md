---
title: 'Tratado moderno de Álgebra — Capítulo 30: Teoremas de isomorfía superiores y correspondencia'
description: Capítulo del Tratado moderno de Álgebra dedicado a los segundos y terceros teoremas de isomorfía y a la correspondencia de subgrupos e ideales en cocientes.
author: Gustav A. Tachek
content-id: MA-BCH-0138
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
- teoremas-de-isomorfia
- correspondencia
- grupos
- anillos
- cocientes
prerequisites:
- MA-BCH-0137
related:
- MA-BOK-0007
- MA-BCH-0137
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## 30.0. Propósito y posición deductiva

El capítulo 29 estableció las propiedades universales de productos, cocientes y cuerpo de fracciones. En este capítulo, los primeros teoremas de isomorfía para [grupos](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md#talg-thm-00006) y [anillos](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-thm-00012), junto con las propiedades universales de los cocientes, permiten organizar los resultados superiores de isomorfía.

El desarrollo sigue, para grupos y anillos, una misma secuencia: construcción de las combinaciones de subestructuras, segundo teorema de isomorfía, correspondencia y tercer teorema de isomorfía.

Los subanillos conservan la convención unital del tratado; los ideales se consideran bilaterales y mantienen su tipo propio. Las construcciones generales de descenso y transporte de estructura se desarrollan en el [capítulo 31](tratado-de-algebra-capitulo-31-descenso-y-transporte-de-estructura.md).

---

## 30.6. Producto de subconjuntos de un grupo

### Definición 30.6.1 — Producto de subconjuntos de un grupo {#talg-def-00068}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo y sean $A,B\subseteq G$. Definimos el **producto de los subconjuntos $A$ y $B$** por

$$
\boxed{
AB
:=
\{x\in G:\exists a\in A\,\exists b\in B,\ x=a\star b\}.
} \tag{1}
$$

Equivalentemente, en notación descriptiva,

$$
AB=\{a\star b:a\in A,\ b\in B\}. \tag{2}
$$

La definición (1) es la conjuntista canónica: $AB$ existe por Separación aplicada a $G$. El cierre de la operación del grupo garantiza que todo producto $a\star b$ con $a,b\in G$ pertenece nuevamente a $G$.

En particular, para todo $x\in G$,

$$
\boxed{
x\in AB
\iff
\exists a\in A\,\exists b\in B,\ x=a\star b.
} \tag{3}
$$

No se exige que $A$ ni $B$ sean no vacíos. Si alguno de los dos es vacío, entonces $AB=\varnothing$ por (3).

> **Alcance de la definición.** La escritura $AB$ denota un subconjunto de $G$. No afirma que $AB$ determine un subgrupo, no implica $AB=BA$ y no identifica $AB$ con el producto cartesiano $A\times B$. Esas propiedades, cuando correspondan bajo hipótesis adicionales, deberán demostrarse en resultados posteriores.

> **Uso del producto de subconjuntos.** Para subgrupos $H,N\le G$, la expresión $HN$ queda desde ahora bien formada como producto de subconjuntos. La normalidad de $N$ y el hecho de que $HN$ sea un subgrupo no forman parte de esta definición.

---

## 30.8. El producto de un subgrupo por un subgrupo normal es un subgrupo

### Proposición 30.8.1 — El producto de un subgrupo por un subgrupo normal es un subgrupo {#talg-pro-00102}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo. Sean $H,N\subseteq G$ tales que $H$ determina un subgrupo de $\mathcal G$ y $N$ determina un subgrupo normal de $\mathcal G$.

Entonces el producto de subconjuntos

$$
HN
=
\{h\star n:h\in H,\ n\in N\}
$$

determina un subgrupo de $\mathcal G$.

#### Demostración {#talg-prf-00152}

Aplicaremos el criterio constructivo de subgrupo [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004).

**1. Habitabilidad de $HN$.** Como $H$ y $N$ son subgrupos, ambos contienen el neutro ambiente $e_{\mathcal G}$. Por tanto

$$
e_{\mathcal G}
=
e_{\mathcal G}\star e_{\mathcal G}
\in HN.
$$

Así, $HN$ está habitado con un testigo explícito.

**2. Preparación del inverso de un producto.** Sean

$$
x,y\in HN.
$$

Por la Definición 30.6.1 existen, localmente,

$$
h_1,h_2\in H,
\qquad
n_1,n_2\in N
$$

tales que

$$
x=h_1\star n_1,
\qquad
y=h_2\star n_2.
\tag{1}
$$

Afirmamos que

$$
y^{-1}=n_2^{-1}\star h_2^{-1}.
\tag{2}
$$

En efecto,

$$
\begin{aligned}
(h_2\star n_2)\star(n_2^{-1}\star h_2^{-1})
&=
h_2\star(n_2\star n_2^{-1})\star h_2^{-1}\\
&=
h_2\star e_{\mathcal G}\star h_2^{-1}\\
&=
e_{\mathcal G},
\end{aligned}
$$

y, en el orden inverso,

$$
\begin{aligned}
(n_2^{-1}\star h_2^{-1})\star(h_2\star n_2)
&=
n_2^{-1}\star(h_2^{-1}\star h_2)\star n_2\\
&=
n_2^{-1}\star e_{\mathcal G}\star n_2\\
&=
e_{\mathcal G}.
\end{aligned}
$$

Luego $n_2^{-1}\star h_2^{-1}$ es un inverso bilateral de $y$; por la unicidad de [Proposición 4.1.2](tratado-de-algebra-capitulo-4-inversos-y-grupos.md#talg-pro-00002), se obtiene (2).

**3. Cierre bajo $x\star y^{-1}$.** Como $N$ es subgrupo,

$$
m:=n_1\star n_2^{-1}\in N.
\tag{3}
$$

La normalidad de $N$ en $G$ implica, aplicada a $h_2\in G$ y $m\in N$,

$$
c:=h_2\star m\star h_2^{-1}\in N.
\tag{4}
$$

Además, como $H$ es subgrupo,

$$
h:=h_1\star h_2^{-1}\in H.
\tag{5}
$$

Usando (1)–(5) y asociatividad,

$$
\begin{aligned}
x\star y^{-1}
&=
(h_1\star n_1)\star(n_2^{-1}\star h_2^{-1})\\
&=
h_1\star(n_1\star n_2^{-1})\star h_2^{-1}\\
&=
h_1\star m\star h_2^{-1}\\
&=
(h_1\star h_2^{-1})
\star
(h_2\star m\star h_2^{-1})\\
&=
h\star c.
\end{aligned}
$$

Por (4), $c\in N$, y por (5), $h\in H$. La definición de producto de subconjuntos da entonces

$$
x\star y^{-1}\in HN.
$$

Hemos demostrado que $HN$ está habitado y que

$$
\forall x,y\in HN,
\qquad
x\star y^{-1}\in HN.
$$

Por [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $HN$ determina un subgrupo de $\mathcal G$. $\square$

> **Punto estructural.** La normalidad de $N$ interviene exactamente al reordenar el factor $m\in N$ a través de $h_2^{-1}$. Sin esa hipótesis, el producto conjuntista de dos subgrupos no tiene por qué ser un subgrupo.

> **Lectura fundacional.** Los representantes $h_i,n_i$ se eliminan sólo localmente desde las pertenencias $x,y\in HN$; no se elige una familia global de descomposiciones. La prueba no usa el axioma de elección ni lógica clásica sustantiva.

---

## 30.10. Normalidad de $N$ en $HN$ y de $H\cap N$ en $H$

### Proposición 30.10.1 — Normalidad de $N$ en $HN$ y de $H\cap N$ en $H$ {#talg-pro-00103}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo. Sean $H,N\subseteq G$ tales que $H$ determina un subgrupo de $\mathcal G$ y $N\trianglelefteq G$. Entonces:

1. $N$ determina un subgrupo normal del grupo inducido sobre $HN$; en particular,
   $$
   \boxed{N\trianglelefteq HN.}
   $$
2. $H\cap N$ determina un subgrupo normal del grupo inducido sobre $H$; en particular,
   $$
   \boxed{H\cap N\trianglelefteq H.}
   $$

#### Demostración {#talg-prf-00153}

Por [Proposición 30.8.1](#talg-pro-00102), el subconjunto $HN$ determina un subgrupo de $\mathcal G$; por tanto dispone de la estructura de grupo inducida por restricción.

##### 1. $N\trianglelefteq HN$

Primero verificamos que $N\subseteq HN$. Sea $n\in N$. Como $H$ es subgrupo,

$$
e_{\mathcal G}\in H,
$$

y

$$
n=e_{\mathcal G}\star n.
$$

Por la Definición 30.6.1,

$$
n\in HN.
$$

Así,

$$
N\subseteq HN. \tag{1}
$$

Debemos comprobar que $N$ determina un subgrupo del grupo inducido sobre $HN$. El conjunto $N$ está habitado por $e_{\mathcal G}$. Si $a,b\in N$, como $N$ es subgrupo de $G$,

$$
a\star b^{-1}\in N.
$$

Por (1), este elemento pertenece también a $HN$. Aplicando [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) al grupo inducido sobre $HN$, concluimos que $N$ determina un subgrupo de $HN$.

Resta la estabilidad por conjugación. Sean

$$
x\in HN,
\qquad
n\in N.
$$

Como $HN\subseteq G$, tenemos $x\in G$. La hipótesis $N\trianglelefteq G$ y [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026) dan

$$
(x\star n)\star x^{-1}\in N.
$$

Las operaciones e inversos del grupo inducido sobre $HN$ son las restricciones de los del grupo ambiente, de modo que ésta es exactamente la condición de normalidad dentro de $HN$. Por [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026),

$$
N\trianglelefteq HN.
$$

##### 2. $H\cap N\trianglelefteq H$

El conjunto

$$
H\cap N
=
\{x\in H:x\in N\}
$$

existe por Separación aplicada a $H$.

Como $H$ y $N$ son subgrupos,

$$
e_{\mathcal G}\in H\cap N,
$$

por lo que la intersección está habitada. Sean ahora $a,b\in H\cap N$. Entonces $a,b\in H$ y $a,b\in N$. Del cierre de ambos subgrupos se sigue simultáneamente

$$
a\star b^{-1}\in H
$$

y

$$
a\star b^{-1}\in N.
$$

Por tanto,

$$
a\star b^{-1}\in H\cap N.
$$

Aplicando [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) al grupo inducido sobre $H$, concluimos que $H\cap N$ determina un subgrupo de $H$.

Finalmente, sean

$$
h\in H,
\qquad
x\in H\cap N.
$$

Como $x\in N$, $h\in H\subseteq G$ y $N\trianglelefteq G$,

$$
(h\star x)\star h^{-1}\in N. \tag{2}
$$

Por otra parte, $h,x\in H$ y $H$ es subgrupo, así que $h^{-1}\in H$ y el cierre bajo $\star$ da

$$
(h\star x)\star h^{-1}\in H. \tag{3}
$$

De (2) y (3),

$$
(h\star x)\star h^{-1}\in H\cap N.
$$

Por [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026),

$$
H\cap N\trianglelefteq H.
$$

Quedan demostradas ambas afirmaciones. $\square$

> **Punto estructural.** Las dos normalidades se heredan de la misma hipótesis $N\trianglelefteq G$, pero por mecanismos distintos: $N\trianglelefteq HN$ usa la inclusión $HN\subseteq G$, mientras que $H\cap N\trianglelefteq H$ combina normalidad en $G$ con cierre de $H$.

> **Lectura fundacional.** La intersección se construye por Separación y los testigos usados son explícitos. No se emplea el axioma de elección ni lógica clásica sustantiva.

---

## 30.13. Segundo teorema de isomorfía para grupos

### Teorema 30.13.1 — Segundo teorema de isomorfía para grupos {#talg-thm-00024}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo, sea $H\subseteq G$ un subconjunto que determina un subgrupo y sea $N\trianglelefteq G$. Entonces existe un isomorfismo de grupos

$$
\boxed{
H/(H\cap N)\cong HN/N.
}
\tag{1}
$$

Más precisamente, existe un isomorfismo

$$
\widehat\varphi:H/(H\cap N)\longrightarrow HN/N
$$

caracterizado por

$$
\boxed{
\widehat\varphi\bigl(h(H\cap N)\bigr)=hN
}
\qquad(h\in H).
\tag{2}
$$

#### Demostración {#talg-prf-00154}

Por [Proposición 30.8.1](#talg-pro-00102), el subconjunto $HN$ determina un subgrupo de $\mathcal G$. Por [Proposición 30.10.1](#talg-pro-00103),

$$
N\trianglelefteq HN
\qquad\text{y}\qquad
H\cap N\trianglelefteq H.
\tag{3}
$$

Por tanto los dos cocientes de (1) están bien tipados como grupos. Además, [Proposición 12.5.2](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00023), aplicado al grupo inducido sobre $HN$ y al subgrupo normal $N$, proporciona la proyección canónica

$$
q_N:HN\to HN/N,
$$

que es un homomorfismo sobreyectivo y satisface

$$
\ker q_N=N.
\tag{4}
$$

**1. Construcción del morfismo $\varphi:H\to HN/N$.** Primero observamos que

$$
H\subseteq HN.
\tag{5}
$$

En efecto, si $h\in H$, entonces $e_{\mathcal G}\in N$ porque $N$ es subgrupo, y

$$
h=h\star e_{\mathcal G}\in HN
$$

por [Definición 30.6.1](#talg-def-00068).

Definamos

$$
\Gamma_\varphi
:=
\{\langle h,C\rangle\in H\times(HN/N):C=q_N(h)\}.
\tag{6}
$$

Por Separación, $\Gamma_\varphi$ es un conjunto. Para cada $h\in H$, (5) permite evaluar $q_N(h)$, y el valor es único porque $q_N$ es función. Así (6) es el grafo de una función

$$
\varphi:H\to HN/N,
\qquad
\varphi(h)=q_N(h)=hN.
\tag{7}
$$

Sean $h_1,h_2\in H$. Como la operación del grupo inducido sobre $H$ es la restricción de la operación de $G$ y $q_N$ es un homomorfismo,

$$
\varphi(h_1\star h_2)
=q_N(h_1\star h_2)
$$

es el producto, en $HN/N$, de $q_N(h_1)$ y $q_N(h_2)$, es decir, de $\varphi(h_1)$ y $\varphi(h_2)$. Por [Definición 7.4.1](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-def-00019), $\varphi$ es un homomorfismo de grupos.

**2. Cálculo del núcleo.** Sea $h\in H$. Usando (4),

$$
\begin{aligned}
h\in\ker\varphi
&\iff \varphi(h)=e_{HN/N}\\
&\iff q_N(h)=e_{HN/N}\\
&\iff h\in\ker q_N\\
&\iff h\in N.
\end{aligned}
\tag{8}
$$

Como el dominio de $\varphi$ es $H$, (8) equivale a

$$
h\in\ker\varphi
\iff
h\in H\cap N.
$$

Por Extensionalidad,

$$
\boxed{\ker\varphi=H\cap N.}
\tag{9}
$$

**3. Sobreyectividad.** Sea $C\in HN/N$. Como $q_N$ es sobreyectiva, existe $x\in HN$ tal que

$$
C=q_N(x).
\tag{10}
$$

Por [Definición 30.6.1](#talg-def-00068), de $x\in HN$ obtenemos localmente $h\in H$ y $n\in N$ tales que

$$
x=h\star n.
\tag{11}
$$

Como $n\in N=\ker q_N$, tenemos

$$
q_N(n)=e_{HN/N}.
\tag{12}
$$

Usando la homomorfía de $q_N$ y (10)–(12),

$$
\begin{aligned}
C
&=q_N(h\star n)\\
&=q_N(h)\,q_N(n)\\
&=q_N(h)\\
&=\varphi(h).
\end{aligned}
$$

Por tanto $\varphi$ es sobreyectiva.

**4. Aplicación del primer teorema de isomorfía.** La forma sobreyectiva del primer teorema de isomorfía, [Corolario 13.2.1](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md#talg-cor-00004), aplicada a $\varphi$, produce un isomorfismo

$$
\widehat\varphi:H/\ker\varphi\longrightarrow HN/N
$$

caracterizado por

$$
\widehat\varphi(h\ker\varphi)=\varphi(h).
\tag{13}
$$

Sustituyendo (9) en (13) y usando (7), obtenemos

$$
\widehat\varphi\bigl(h(H\cap N)\bigr)=hN,
$$

que es exactamente (2). En particular,

$$
H/(H\cap N)\cong HN/N.
$$

$\square$

> **Punto estructural.** El segundo teorema no exige un nuevo principio general de descenso: el morfismo $\varphi$ es la restricción concreta de la proyección $q_N$ al subgrupo $H$, y el isomorfismo final procede de la forma sobreyectiva del primer teorema.

> **Lectura fundacional.** La función $\varphi$ se construye por su grafo. Los testigos $h,n$ usados en la sobreyectividad se eliminan localmente desde la pertenencia $x\in HN$; no se elige una descomposición para cada elemento de $HN$. No intervienen el axioma de elección ni lógica clásica sustantiva nueva.

---

## 30.16. Teorema de correspondencia para subgrupos sobre un cociente

### Teorema 30.16.1 — Teorema de correspondencia para subgrupos sobre un cociente {#talg-thm-00025}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo y sea $N\trianglelefteq G$. Definamos las familias

$$
\mathscr S_N(G)
:=
\{L\in\mathcal P(G):L\text{ determina un subgrupo de }G\text{ y }N\subseteq L\},
\tag{25}
$$

y

$$
\mathscr S(G/N)
:=
\{K\in\mathcal P(G/N):K\text{ determina un subgrupo de }G/N\}.
\tag{26}
$$

Para $L\in\mathscr S_N(G)$ escribamos

$$
L/N
:=
\{C\in G/N:\exists \ell\in L,\ C=q_N(\ell)\},
\tag{27}
$$

y para $K\in\mathscr S(G/N)$ definamos

$$
P_K
:=
\{g\in G:q_N(g)\in K\}.
\tag{28}
$$

Entonces las asignaciones

$$
\Phi_N:\mathscr S_N(G)\to\mathscr S(G/N),
\qquad
\Phi_N(L)=L/N,
\tag{29}
$$

y

$$
\Psi_N:\mathscr S(G/N)\to\mathscr S_N(G),
\qquad
\Psi_N(K)=P_K,
\tag{30}
$$

son funciones mutuamente inversas. En particular, establecen una biyección entre los subgrupos de $G$ que contienen $N$ y los subgrupos de $G/N$.

Además, para $L_1,L_2\in\mathscr S_N(G)$,

$$
\boxed{
L_1\subseteq L_2
\iff
L_1/N\subseteq L_2/N,
}
\tag{31}
$$

y, para todo $L\in\mathscr S_N(G)$,

$$
\boxed{
L\trianglelefteq G
\iff
L/N\trianglelefteq G/N.
}
\tag{32}
$$

La notación $L/N$ de (27) coincide con el conjunto cociente del grupo inducido sobre $L$ por $N$. En efecto, como $N\subseteq L$, el conjunto $N$ determina un subgrupo del grupo inducido sobre $L$; y, si $\ell\in L$ y $n\in N$, la normalidad $N\trianglelefteq G$ da $(\ell\star n)\star\ell^{-1}\in N$, de modo que $N\trianglelefteq L$. Cada clase del cociente de $L$ por $N$ es entonces literalmente la clase lateral $\ell N=q_N(\ell)$.

#### Demostración {#talg-prf-00155}

Por [Proposición 12.5.2](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00023), la proyección canónica

$$
q_N:G\to G/N,
\qquad
q_N(g)=gN,
\tag{33}
$$

es un homomorfismo sobreyectivo y

$$
\ker q_N=N.
\tag{34}
$$

Las familias (25)–(26) existen por Conjunto Potencia y Separación. Verificaremos primero que (27)–(28) toman valores en las familias declaradas.

**1. Si $L\in\mathscr S_N(G)$, entonces $L/N$ es subgrupo de $G/N$.** Como $L$ es subgrupo, $e_{\mathcal G}\in L$; por tanto

$$
q_N(e_{\mathcal G})\in L/N.
$$

Por [Proposición 7.4.2](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00007), $q_N(e_{\mathcal G})=e_{G/N}$, de modo que $L/N$ está habitado.

Sean $C,D\in L/N$. Por (27) existen localmente $a,b\in L$ tales que

$$
C=q_N(a),
\qquad
D=q_N(b).
$$

Como $L$ es subgrupo,

$$
a\star b^{-1}\in L.
$$

La homomorfía de $q_N$ y [Proposición 7.4.3](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00008) dan

$$
\begin{aligned}
CD^{-1}
&=q_N(a)q_N(b)^{-1}\\
&=q_N(a)q_N(b^{-1})\\
&=q_N(a\star b^{-1})
\in L/N.
\end{aligned}
$$

Por [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $L/N$ determina un subgrupo de $G/N$.

**2. Si $K\in\mathscr S(G/N)$, entonces $P_K$ es un subgrupo de $G$ que contiene $N$.** Como $K$ es subgrupo,

$$
e_{G/N}\in K.
$$

La preservación del neutro da

$$
q_N(e_{\mathcal G})=e_{G/N}\in K,
$$

por lo que $e_{\mathcal G}\in P_K$.

Sean $a,b\in P_K$. Entonces $q_N(a),q_N(b)\in K$. Como $K$ es subgrupo,

$$
q_N(a)q_N(b)^{-1}\in K.
$$

Por homomorfía y preservación de inversos,

$$
q_N(a\star b^{-1})
=
q_N(a)q_N(b)^{-1}
\in K.
$$

Así $a\star b^{-1}\in P_K$, y [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) muestra que $P_K$ determina un subgrupo de $G$.

Finalmente, sea $n\in N$. Por (34), $n\in\ker q_N$, así que

$$
q_N(n)=e_{G/N}\in K.
$$

Por tanto $n\in P_K$ y

$$
N\subseteq P_K.
\tag{35}
$$

Esto prueba que las asignaciones (29)–(30) están bien tipadas. Sus grafos existen por Separación aplicada a los productos cartesianos de (25)–(26), y cada entrada posee una única salida porque (27) y (28) determinan subconjuntos únicos. Por consiguiente, $\Phi_N$ y $\Psi_N$ son funciones.

**3. Primera identidad de saturación.** Sea $L\in\mathscr S_N(G)$. Demostraremos

$$
\boxed{
\Psi_N(\Phi_N(L))=L.
}
\tag{36}
$$

Si $\ell\in L$, entonces $q_N(\ell)\in L/N=\Phi_N(L)$, de modo que

$$
\ell\in\Psi_N(\Phi_N(L)).
$$

Por tanto

$$
L\subseteq\Psi_N(\Phi_N(L)).
\tag{37}
$$

Recíprocamente, sea $g\in\Psi_N(\Phi_N(L))$. Entonces

$$
q_N(g)\in L/N.
$$

Por (27), existe localmente $\ell\in L$ con

$$
q_N(g)=q_N(\ell).
\tag{38}
$$

Usando la homomorfía y la preservación de inversos,

$$
\begin{aligned}
q_N(\ell^{-1}\star g)
&=q_N(\ell^{-1})q_N(g)\\
&=q_N(\ell)^{-1}q_N(\ell)\\
&=e_{G/N}.
\end{aligned}
$$

Por (34),

$$
\ell^{-1}\star g\in N\subseteq L.
\tag{39}
$$

Como $\ell\in L$ y $L$ es subgrupo, el cierre de $L$ y (39) dan

$$
g
=
\ell\star(\ell^{-1}\star g)
\in L.
$$

Así

$$
\Psi_N(\Phi_N(L))\subseteq L.
\tag{40}
$$

Por Extensionalidad, (37) y (40) producen (36).

**4. Segunda identidad de saturación.** Sea $K\in\mathscr S(G/N)$. Demostraremos

$$
\boxed{
\Phi_N(\Psi_N(K))=K.
}
\tag{41}
$$

Si $C\in\Phi_N(\Psi_N(K))$, existe $g\in\Psi_N(K)$ con $C=q_N(g)$. Por la definición de $\Psi_N(K)$, $q_N(g)\in K$, luego $C\in K$. Por tanto

$$
\Phi_N(\Psi_N(K))\subseteq K.
\tag{42}
$$

Para la inclusión opuesta, sea $C\in K$. Como $q_N$ es sobreyectiva, existe localmente $g\in G$ con

$$
C=q_N(g).
$$

Entonces $q_N(g)\in K$, de modo que $g\in\Psi_N(K)$ y, por (27),

$$
C\in\Phi_N(\Psi_N(K)).
$$

Así

$$
K\subseteq\Phi_N(\Psi_N(K)).
\tag{43}
$$

y Extensionalidad da (41).

Las identidades (36) y (41) muestran que $\Phi_N$ y $\Psi_N$ son mutuamente inversas. Por [interfaz funcional de biyectividad e inversas](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002), ambas son biyectivas.

**5. Inclusiones.** Si $L_1\subseteq L_2$, la definición (27) implica inmediatamente

$$
L_1/N\subseteq L_2/N.
$$

Recíprocamente, si $L_1/N\subseteq L_2/N$, entonces la definición (28) da

$$
\Psi_N(L_1/N)\subseteq\Psi_N(L_2/N).
$$

Aplicando (36) a $L_1$ y $L_2$ obtenemos

$$
L_1\subseteq L_2.
$$

Queda demostrada (31).

**6. Preservación de la normalidad.** Supongamos $L\trianglelefteq G$. Sean

$$
C\in G/N,
\qquad
D\in L/N.
$$

Por la sobreyectividad de $q_N$ existe localmente $g\in G$ con $C=q_N(g)$; por (27) existe localmente $\ell\in L$ con $D=q_N(\ell)$. Entonces

$$
\begin{aligned}
CDC^{-1}
&=
q_N(g)q_N(\ell)q_N(g)^{-1}\\
&=
q_N\bigl((g\star\ell)\star g^{-1}\bigr).
\end{aligned}
$$

Como $L\trianglelefteq G$,

$$
(g\star\ell)\star g^{-1}\in L,
$$

y por (27) la última clase pertenece a $L/N$. Así $L/N$ es estable bajo conjugación por elementos de $G/N$. Como ya es subgrupo, [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026) da

$$
L/N\trianglelefteq G/N.
\tag{44}
$$

**7. Reflexión de la normalidad.** Supongamos ahora

$$
L/N\trianglelefteq G/N.
$$

Sean $g\in G$ y $\ell\in L$. Por normalidad en el cociente,

$$
q_N(g)q_N(\ell)q_N(g)^{-1}
\in L/N.
$$

La homomorfía y la preservación de inversos transforman esta pertenencia en

$$
q_N\bigl((g\star\ell)\star g^{-1}\bigr)
\in L/N.
$$

Por (36), la preimagen de $L/N$ bajo $q_N$ es exactamente $L$. Por tanto

$$
(g\star\ell)\star g^{-1}\in L.
$$

Como $g$ y $\ell$ eran arbitrarios, [Definición 10.1.1](tratado-de-algebra-capitulo-10-subgrupos-normales.md#talg-def-00026) concluye

$$
L\trianglelefteq G.
\tag{45}
$$

Las implicaciones (44)–(45) prueban (32). $\square$

> **Punto estructural.** La correspondencia no es sólo una biyección de colecciones: identifica exactamente los subgrupos saturados respecto de $q_N$ con los subgrupos del cociente, conserva y refleja inclusión, y conserva y refleja normalidad.

> **Lectura fundacional.** Las familias de subgrupos son conjuntos por Potencia y Separación. Las imágenes y preimágenes utilizadas son subconjuntos definidos por Separación, y los representantes de clases se usan sólo mediante eliminación existencial local. No se elige una familia global de representantes y no interviene el axioma de elección ni lógica clásica sustantiva nueva.

---

## 30.18. Tercer teorema de isomorfía para grupos

### Teorema 30.18.1 — Tercer teorema de isomorfía para grupos {#talg-thm-00026}

Sea

$$
\mathcal G=\langle G,\star\rangle
$$

un grupo y sean $N,H\subseteq G$ tales que

$$
N\subseteq H,
\qquad
N\trianglelefteq G,
\qquad
H\trianglelefteq G.
\tag{46}
$$

Entonces

$$
H/N\trianglelefteq G/N
\tag{47}
$$

y existe un isomorfismo de grupos

$$
\boxed{
(G/N)/(H/N)\cong G/H.
}
\tag{48}
$$

Más precisamente, existe un isomorfismo

$$
\widehat\rho:(G/N)/(H/N)\longrightarrow G/H
$$

caracterizado por

$$
\boxed{
\widehat\rho\bigl((gN)(H/N)\bigr)=gH
}
\qquad(g\in G).
\tag{49}
$$

#### Demostración {#talg-prf-00156}

Por [Teorema 30.16.1](#talg-thm-00025), la correspondencia de subgrupos sobre el cociente por $N$ preserva y refleja normalidad. Como $N\subseteq H$ y $H\trianglelefteq G$, obtenemos inmediatamente

$$
H/N\trianglelefteq G/N,
$$

que es (47).

Consideremos ahora las proyecciones canónicas

$$
q_N:G\to G/N,
\qquad
q_H:G\to G/H.
$$

Por [Proposición 12.5.2](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00023), ambas son homomorfismos sobreyectivos y

$$
\ker q_N=N,
\qquad
\ker q_H=H.
\tag{50}
$$

Como $N\subseteq H=\ker q_H$, la propiedad universal del cociente de grupos [Teorema 29.29.1](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md#talg-thm-00021), aplicada al homomorfismo $q_H$, proporciona un único homomorfismo

$$
\rho:G/N\to G/H
\tag{51}
$$

tal que

$$
\rho\circ q_N=q_H.
\tag{52}
$$

Además, para todo $g\in G$,

$$
\boxed{
\rho(gN)=gH.
}
\tag{53}
$$

**1. Sobreyectividad de $\rho$.** Sea $D\in G/H$. Como $q_H$ es sobreyectiva, existe localmente $g\in G$ tal que

$$
D=q_H(g).
$$

Usando (52),

$$
D=q_H(g)=\rho(q_N(g)).
$$

Por tanto $\rho$ es sobreyectiva.

**2. Cálculo del núcleo.** Sea $C\in G/N$. Por la sobreyectividad de $q_N$, existe localmente $g\in G$ tal que

$$
C=q_N(g)=gN.
\tag{54}
$$

Entonces, usando (52) y (50),

$$
\begin{aligned}
C\in\ker\rho
&\iff \rho(C)=e_{G/H}\\
&\iff \rho(q_N(g))=e_{G/H}\\
&\iff q_H(g)=e_{G/H}\\
&\iff g\in\ker q_H\\
&\iff g\in H.
\end{aligned}
\tag{55}
$$

Por la identidad de saturación demostrada en [Teorema 30.16.1](#talg-thm-00025), bajo la hipótesis $N\subseteq H$,

$$
g\in H
\iff
q_N(g)\in H/N.
\tag{56}
$$

Combinando (54)–(56),

$$
C\in\ker\rho
\iff
C\in H/N.
$$

Como $C\in G/N$ era arbitrario, por Extensionalidad,

$$
\boxed{
\ker\rho=H/N.
}
\tag{57}
$$

**3. Aplicación del primer teorema de isomorfía.** El homomorfismo $\rho$ es sobreyectivo y, por (57), su núcleo es $H/N$. La forma sobreyectiva del primer teorema de isomorfía, [Corolario 13.2.1](tratado-de-algebra-capitulo-13-primer-teorema-de-isomorfia-para-grupos.md#talg-cor-00004), produce un isomorfismo

$$
\widehat\rho:(G/N)/\ker\rho\longrightarrow G/H
$$

caracterizado por

$$
\widehat\rho\bigl(C\ker\rho\bigr)=\rho(C).
\tag{58}
$$

Sustituyendo $\ker\rho=H/N$ y tomando $C=gN$, (53) y (58) dan

$$
\widehat\rho\bigl((gN)(H/N)\bigr)=gH.
$$

Ésta es exactamente la fórmula (49), y en particular obtenemos (48). $\square$

> **Punto estructural.** El tercer teorema combina dos mecanismos ya establecidos: la correspondencia identifica $H/N$ como subgrupo normal del primer cociente y la propiedad universal de $q_N$ hace descender la proyección $q_H$. El primer teorema de isomorfía se aplica sólo al homomorfismo concreto resultante.

> **Lectura fundacional.** La representación $C=q_N(g)$ se usa únicamente de forma local a partir de la sobreyectividad de $q_N$; no se elige un representante para cada clase de $G/N$. No intervienen el axioma de elección ni lógica clásica sustantiva nueva.

---

## 30.21. Suma de un subanillo y un ideal

### Definición 30.21.1 — Suma de un subanillo y un ideal {#talg-def-00069}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo, sea $S\subseteq R$ un subconjunto que determina un subanillo de $\mathcal R$ y sea $I\subseteq R$ un ideal bilateral de $R$. Definimos la **suma del subanillo $S$ y el ideal $I$** por

$$
\boxed{
S+I
:=
\{x\in R:\exists s\in S\,\exists i\in I,\ x=s+i\}.
}
\tag{64}
$$

Equivalentemente, en notación descriptiva,

$$
S+I=\{s+i:s\in S,\ i\in I\}.
\tag{65}
$$

La forma (64) es la definición conjuntista canónica. El conjunto $S+I$ existe por Separación aplicada al conjunto ambiente $R$. Si $s\in S$ e $i\in I$, entonces $s,i\in R$ y la clausura de la suma del anillo garantiza

$$
s+i\in R,
$$

de modo que la descripción (65) está bien tipada.

En particular, para todo $x\in R$,

$$
\boxed{
x\in S+I
\iff
\exists s\in S\,\exists i\in I,\ x=s+i.
}
\tag{66}
$$

La definición no selecciona una descomposición privilegiada de cada elemento de $S+I$. Cuando posteriormente se use $x\in S+I$, los testigos $s\in S$ e $i\in I$ de (66) se introducirán únicamente de manera local.

> **Alcance de la definición.** La escritura $S+I$ denota por ahora sólo un subconjunto de $R$. No afirma todavía que $S+I$ determine un subanillo, que $I$ sea ideal del anillo inducido sobre $S+I$ ni que $S\cap I$ sea ideal del anillo inducido sobre $S$. Esas propiedades se demuestran en la Proposición 30.23.1.

> **Convención unital preservada.** El ideal $I$ no se reinterpreta como subanillo. La hipótesis de subanillo unital recae exclusivamente sobre $S$; la bilateralidad de $I$ se mantiene en el sentido de [Definición 18.1.1](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00040).

---

## 30.23. Estructura de $S+I$ e idealidad de $I$ y $S\cap I$

### Proposición 30.23.1 — Estructura de $S+I$ e idealidad de $I$ y $S\cap I$ {#talg-pro-00104}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo, sea $S\subseteq R$ un subconjunto que determina un subanillo de $\mathcal R$ y sea $I\subseteq R$ un ideal bilateral de $R$. Entonces:

1. $S+I$ determina un subanillo unital de $\mathcal R$;
2. $I$ determina un ideal bilateral del anillo inducido sobre $S+I$;
3. $S\cap I$ determina un ideal bilateral del anillo inducido sobre $S$.

#### Demostración {#talg-prf-00157}

##### 1. $S+I$ es un subanillo unital de $R$

Aplicaremos el criterio de subanillo unital [Teorema 17.1.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-thm-00009).

Como $S$ es subanillo, $1_R\in S$. Como $I$ es un ideal, su estructura aditiva es un subgrupo y, por tanto, $0_R\in I$. Luego

$$
1_R=1_R+0_R\in S+I.
\tag{67}
$$

Sean ahora $x,y\in S+I$. Por [Definición 30.21.1](#talg-def-00069) existen localmente

$$
s,t\in S,
\qquad
i,j\in I
$$

tales que

$$
x=s+i,
\qquad
y=t+j.
\tag{68}
$$

Como el grupo aditivo de un anillo es abeliano, las leyes de grupo permiten reagrupar y reordenar términos, y obtenemos

$$
x-y=(s-t)+(i-j).
\tag{69}
$$

El subconjunto $S$ determina un subgrupo aditivo, de modo que $s-t\in S$. El ideal $I$ determina también un subgrupo aditivo, de modo que $i-j\in I$. Por la definición de $S+I$,

$$
x-y\in S+I.
\tag{70}
$$

Para el producto, la distributividad del anillo da

$$
\begin{aligned}
xy
&=(s+i)(t+j)\\
&=st+sj+it+ij.
\end{aligned}
\tag{71}
$$

Como $S$ es subanillo, $st\in S$. Además, $s,t,i,j\in R$ y $I$ es bilateral, luego

$$
sj\in I,
\qquad
it\in I,
\qquad
ij\in I.
$$

El cierre aditivo de $I$ implica

$$
k:=sj+it+ij\in I.
$$

Por (71),

$$
xy=st+k\in S+I.
\tag{72}
$$

Las ecuaciones (67), (70) y (72) verifican las tres condiciones de [Teorema 17.1.3](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-thm-00009). Por tanto, $S+I$ determina un subanillo unital de $R$.

##### 2. $I$ es un ideal bilateral del anillo inducido sobre $S+I$

Primero,

$$
I\subseteq S+I.
\tag{73}
$$

En efecto, si $i\in I$, entonces $0_R\in S$ porque $S$ es subanillo, y

$$
i=0_R+i\in S+I.
$$

El conjunto $I$ está habitado por $0_R$. Si $a,b\in I$, entonces $a-b\in I$ porque $I$ es un subgrupo del grupo aditivo de $R$; por (73), $a-b\in S+I$. Aplicando [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) al grupo aditivo inducido sobre $S+I$, concluimos que $I$ determina un subgrupo aditivo de $S+I$.

Sean ahora $x\in S+I$ e $i\in I$. Como $S+I\subseteq R$, tenemos $x\in R$. La bilateralidad de $I$ en $R$ da

$$
xi\in I,
\qquad
ix\in I.
\tag{74}
$$

Así se cumplen las dos absorciones respecto del anillo inducido sobre $S+I$. Por [Definición 18.1.1](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00040), $I$ es un ideal bilateral de $S+I$.

##### 3. $S\cap I$ es un ideal bilateral del anillo inducido sobre $S$

La intersección

$$
S\cap I=\{x\in S:x\in I\}
$$

existe por Separación aplicada a $S$.

Como $0_R\in S$ y $0_R\in I$,

$$
0_R\in S\cap I.
$$

Sean $a,b\in S\cap I$. Entonces $a,b\in S$ y $a,b\in I$. Por la estructura aditiva de subgrupo de ambos conjuntos,

$$
a-b\in S
\qquad\text{y}\qquad
a-b\in I,
$$

de modo que

$$
a-b\in S\cap I.
$$

Por [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $S\cap I$ determina un subgrupo del grupo aditivo inducido sobre $S$.

Finalmente, sean $s\in S$ y $x\in S\cap I$. Como $S$ es subanillo,

$$
sx\in S,
\qquad
xs\in S.
$$

Como $x\in I$, $s\in S\subseteq R$ e $I$ es ideal bilateral de $R$,

$$
sx\in I,
\qquad
xs\in I.
$$

Por tanto,

$$
sx\in S\cap I,
\qquad
xs\in S\cap I.
$$

La [Definición 18.1.1](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00040) concluye que $S\cap I$ es un ideal bilateral del anillo inducido sobre $S$.

Quedan demostradas las tres afirmaciones. $\square$

> **Punto estructural.** La condición unital sólo interviene en la primera afirmación: $1_R\in S$ permite exhibir $1_R=1_R+0_R\in S+I$. Los ideales $I$ y $S\cap I$ no se convierten en subanillos unitarios; se mantienen en su tipo propio de ideal bilateral.

> **Lectura fundacional.** Las descomposiciones $x=s+i$ se eliminan únicamente de manera local desde la pertenencia a $S+I$. La intersección $S\cap I$ se obtiene por Separación. No se usa el axioma de elección ni lógica clásica sustantiva nueva.

---

## 30.25. Segundo teorema de isomorfía para anillos

### Teorema 30.25.1 — Segundo teorema de isomorfía para anillos {#talg-thm-00027}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo, sea $S\subseteq R$ un subconjunto que determina un subanillo unital y sea $I\subseteq R$ un ideal bilateral. Entonces existe un isomorfismo de anillos

$$
\boxed{
S/(S\cap I)\cong (S+I)/I.
}
\tag{76}
$$

Más precisamente, existe un isomorfismo

$$
\widehat\varphi:S/(S\cap I)\longrightarrow (S+I)/I
$$

caracterizado por

$$
\boxed{
\widehat\varphi([s]_{S\cap I})=[s]_I
}
\qquad(s\in S).
\tag{77}
$$

#### Demostración {#talg-prf-00158}

Por [Proposición 30.23.1](#talg-pro-00104), el subconjunto $S+I$ determina un subanillo unital de $\mathcal R$, $I$ determina un ideal bilateral del anillo inducido sobre $S+I$ y $S\cap I$ determina un ideal bilateral del anillo inducido sobre $S$. Por tanto ambos cocientes de (76) están bien tipados como anillos.

Además, [Proposición 19.4.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00045), aplicado al anillo inducido sobre $S+I$ y al ideal $I$, proporciona la proyección canónica

$$
q_I:S+I\longrightarrow (S+I)/I,
\qquad
q_I(x)=[x]_I,
\tag{78}
$$

que es un homomorfismo sobreyectivo de anillos y satisface

$$
\ker q_I=I.
\tag{79}
$$

**1. Construcción del morfismo $\varphi:S\to (S+I)/I$.** Primero observamos que

$$
S\subseteq S+I.
\tag{80}
$$

En efecto, si $s\in S$, como $0_R\in I$,

$$
s=s+0_R\in S+I
$$

por [Definición 30.21.1](#talg-def-00069).

Definamos

$$
\Gamma_\varphi
:=
\{\langle s,C\rangle\in S\times((S+I)/I):C=q_I(s)\}.
\tag{81}
$$

Por Separación, $\Gamma_\varphi$ es un conjunto. Para cada $s\in S$, (80) permite evaluar $q_I(s)$, y el valor es único porque $q_I$ es función. Así (81) es el grafo de una función

$$
\varphi:S\longrightarrow (S+I)/I,
\qquad
\varphi(s)=q_I(s)=[s]_I.
\tag{82}
$$

Sean $s,t\in S$. Como las operaciones del anillo inducido sobre $S$ son las restricciones de las operaciones de $R$, y $q_I$ es un homomorfismo de anillos,

$$
\varphi(s+t)
=
q_I(s+t)
=
q_I(s)+q_I(t)
=
\varphi(s)+\varphi(t),
$$

y

$$
\varphi(st)
=
q_I(st)
=
q_I(s)q_I(t)
=
\varphi(s)\varphi(t).
$$

Además, el subanillo inducido sobre $S$ tiene unidad $1_R$, y

$$
\varphi(1_R)=q_I(1_R)=1_{(S+I)/I}.
$$

Por [Definición 17.2.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-def-00039), $\varphi$ es un homomorfismo de anillos.

**2. Cálculo del núcleo.** Sea $s\in S$. Usando (79),

$$
\begin{aligned}
s\in\ker\varphi
&\iff \varphi(s)=0_{(S+I)/I}\\
&\iff q_I(s)=0_{(S+I)/I}\\
&\iff s\in\ker q_I\\
&\iff s\in I.
\end{aligned}
\tag{83}
$$

Como el dominio de $\varphi$ es $S$, (83) equivale a

$$
s\in\ker\varphi
\iff
s\in S\cap I.
$$

Por Extensionalidad,

$$
\boxed{\ker\varphi=S\cap I.}
\tag{84}
$$

**3. Sobreyectividad.** Sea $C\in (S+I)/I$. Como $q_I$ es sobreyectiva, existe $x\in S+I$ tal que

$$
C=q_I(x).
\tag{85}
$$

Por [Definición 30.21.1](#talg-def-00069), de $x\in S+I$ obtenemos localmente $s\in S$ e $i\in I$ tales que

$$
x=s+i.
\tag{86}
$$

Como $i\in I=\ker q_I$,

$$
q_I(i)=0_{(S+I)/I}.
\tag{87}
$$

Usando la aditividad de $q_I$ y (85)–(87),

$$
\begin{aligned}
C
&=q_I(s+i)\\
&=q_I(s)+q_I(i)\\
&=q_I(s)\\
&=\varphi(s).
\end{aligned}
$$

Por tanto $\varphi$ es sobreyectiva.

**4. Aplicación del primer teorema de isomorfía.** La forma sobreyectiva del primer teorema de isomorfía para anillos, [Corolario 20.3.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-cor-00011), aplicada a $\varphi$, produce un isomorfismo

$$
\widehat\varphi:S/\ker\varphi\longrightarrow (S+I)/I
$$

caracterizado por

$$
\widehat\varphi([s]_{\ker\varphi})=\varphi(s).
\tag{88}
$$

Sustituyendo (84) en (88) y usando (82), obtenemos

$$
\widehat\varphi([s]_{S\cap I})=[s]_I,
$$

que es exactamente (77). En particular,

$$
S/(S\cap I)\cong (S+I)/I.
$$

$\square$

> **Punto estructural.** El segundo teorema de isomorfía para anillos no requiere una teoría general de restricción de morfismos: $\varphi$ es la restricción concreta de la proyección $q_I$ al subanillo $S$, y el isomorfismo final procede de la forma sobreyectiva del primer teorema.

> **Lectura fundacional.** La función $\varphi$ se construye por su grafo. Los testigos $s,i$ usados para escribir localmente $x=s+i$ se eliminan dentro de la prueba de sobreyectividad; no se elige una descomposición para cada elemento de $S+I$. No intervienen el axioma de elección ni lógica clásica sustantiva nueva.

---

## 30.28. Teorema de correspondencia para ideales sobre un cociente

### Teorema 30.28.1 — Teorema de correspondencia para ideales sobre un cociente {#talg-thm-00028}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo y sea $I\subseteq R$ un ideal bilateral. Definamos

$$
\mathscr I_I(R)
=
\{J\in\mathcal P(R):J\text{ es ideal bilateral de }R\text{ e }I\subseteq J\},
\tag{109}
$$

y

$$
\mathscr I(R/I)
=
\{K\in\mathcal P(R/I):K\text{ es ideal bilateral de }R/I\}.
\tag{110}
$$

Para $J\in\mathscr I_I(R)$ escribamos

$$
J/I
:=
\{C\in R/I:\exists j\in J,\ C=q_I(j)\},
\tag{111}
$$

y para $K\in\mathscr I(R/I)$ definamos

$$
P_K:=\{r\in R:q_I(r)\in K\}.
\tag{112}
$$

Entonces

$$
\Phi_I:\mathscr I_I(R)\to\mathscr I(R/I),
\qquad
\Phi_I(J)=J/I,
\tag{113}
$$

y

$$
\Psi_I:\mathscr I(R/I)\to\mathscr I_I(R),
\qquad
\Psi_I(K)=P_K,
\tag{114}
$$

son funciones mutuamente inversas. En particular, establecen una biyección entre los ideales bilaterales de $R$ que contienen $I$ y los ideales bilaterales de $R/I$.

Además, para $J_1,J_2\in\mathscr I_I(R)$,

$$
\boxed{
J_1\subseteq J_2
\iff
J_1/I\subseteq J_2/I.
}
\tag{115}
$$

La escritura $J/I$ de (111) significa aquí el **ideal imagen de $J$ dentro de $R/I$**. No se interpreta $J$ como subanillo unital ni se forma un anillo cociente de $J$ por $I$.

#### Demostración {#talg-prf-00159}

Por [Proposición 19.4.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00045), la proyección canónica

$$
q_I:R\to R/I,
\qquad q_I(r)=[r]_I,
\tag{116}
$$

es un homomorfismo sobreyectivo de anillos y

$$
\boxed{\ker q_I=I.}
\tag{117}
$$

Las familias (109)–(110) existen por Conjunto Potencia y Separación.

**1. Imagen de un ideal que contiene $I$.** Sea $J\in\mathscr I_I(R)$. Como $0_R\in J$ y [Proposición 17.2.2](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00032) da $q_I(0_R)=0_{R/I}$, tenemos $0_{R/I}\in J/I$.

Sean $C,D\in J/I$. Existen localmente $a,b\in J$ con $C=q_I(a)$ y $D=q_I(b)$. Como $J$ es subgrupo aditivo, $a-b\in J$, y

$$
\begin{aligned}
C-D
&=q_I(a)-q_I(b)\\
&=q_I(a)+q_I(-b)\\
&=q_I(a-b)
\in J/I.
\end{aligned}
\tag{118}
$$

Por [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $J/I$ determina un subgrupo del grupo aditivo de $R/I$.

Sean ahora $A\in R/I$ y $C\in J/I$. Por sobreyectividad de $q_I$ existe localmente $r\in R$ con $A=q_I(r)$, y por (111) existe localmente $j\in J$ con $C=q_I(j)$. La bilateralidad de $J$ da $rj,jr\in J$, y la multiplicatividad de $q_I$ produce

$$
AC=q_I(rj)\in J/I,
\qquad
CA=q_I(jr)\in J/I.
\tag{119}
$$

Por [Definición 18.1.1](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00040), $J/I$ es un ideal bilateral de $R/I$.

**2. Preimagen de un ideal del cociente.** Sea $K\in\mathscr I(R/I)$. Como $0_{R/I}\in K$ y $q_I(0_R)=0_{R/I}$, se tiene $0_R\in P_K$.

Si $a,b\in P_K$, entonces $q_I(a),q_I(b)\in K$. El cierre aditivo de $K$ y la preservación de opuestos dan

$$
q_I(a-b)=q_I(a)-q_I(b)\in K,
$$

de modo que $a-b\in P_K$. Por [Lema 6.4.4](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004), $P_K$ es un subgrupo aditivo de $R$.

Si $r\in R$ y $a\in P_K$, la bilateralidad de $K$ implica

$$
q_I(r)q_I(a)\in K,
\qquad
q_I(a)q_I(r)\in K.
$$

Por multiplicatividad,

$$
q_I(ra),q_I(ar)\in K,
$$

y por tanto $ra,ar\in P_K$. Así [Definición 18.1.1](tratado-de-algebra-capitulo-18-ideales.md#talg-def-00040) certifica que $P_K$ es un ideal bilateral de $R$.

Finalmente, para $i\in I=\ker q_I$,

$$
q_I(i)=0_{R/I}\in K,
$$

por lo que

$$
\boxed{I\subseteq P_K.}
\tag{120}
$$

Las asignaciones (113)–(114) están, pues, bien tipadas. Sus grafos existen por Separación sobre los productos cartesianos de las familias (109)–(110), y cada entrada posee una única salida porque (111) y (112) determinan subconjuntos únicos.

**3. Primera identidad de saturación.** Sea $J\in\mathscr I_I(R)$. Afirmamos

$$
\boxed{\Psi_I(\Phi_I(J))=J.}
\tag{121}
$$

Si $j\in J$, entonces $q_I(j)\in J/I$, luego $j\in\Psi_I(\Phi_I(J))$. Así

$$
J\subseteq\Psi_I(\Phi_I(J)).
$$

Recíprocamente, sea $r\in\Psi_I(\Phi_I(J))$. Entonces $q_I(r)\in J/I$, por lo que existe localmente $j\in J$ con

$$
q_I(r)=q_I(j).
\tag{122}
$$

La aditividad y la preservación de opuestos dan $q_I(r-j)=0_{R/I}$. Por (117),

$$
r-j\in I\subseteq J.
$$

Como $j\in J$ y $J$ es subgrupo aditivo,

$$
r=(r-j)+j\in J.
$$

La inclusión recíproca queda probada y Extensionalidad da (121).

**4. Segunda identidad de saturación.** Sea $K\in\mathscr I(R/I)$. Afirmamos

$$
\boxed{\Phi_I(\Psi_I(K))=K.}
\tag{123}
$$

Si $C\in\Phi_I(\Psi_I(K))$, existe $r\in\Psi_I(K)$ con $C=q_I(r)$; por definición de $\Psi_I$, $q_I(r)\in K$, luego $C\in K$.

A la inversa, si $C\in K$, la sobreyectividad de $q_I$ proporciona localmente $r\in R$ con $C=q_I(r)$. Entonces $r\in\Psi_I(K)$ y, por (111), $C\in\Phi_I(\Psi_I(K))$. Extensionalidad da (123).

Las identidades (121) y (123) muestran que $\Phi_I$ y $\Psi_I$ son mutuamente inversas. Por [interfaz funcional de biyectividad e inversas](tratado-de-algebra-interfaz-funcional-biyectividad-inversas.md#talg-imp-00002), ambas son biyectivas.

**5. Inclusiones.** Si $J_1\subseteq J_2$, (111) implica inmediatamente $J_1/I\subseteq J_2/I$. Recíprocamente, si $J_1/I\subseteq J_2/I$, entonces

$$
\Psi_I(J_1/I)\subseteq\Psi_I(J_2/I).
$$

Aplicando (121) a $J_1$ y $J_2$ se obtiene $J_1\subseteq J_2$. Esto prueba (115). $\square$

> **Punto estructural.** La correspondencia identifica exactamente los ideales bilaterales de $R$ saturados respecto de $q_I$, es decir, los que contienen $\ker q_I=I$, con los ideales bilaterales del cociente. La identidad (121) es el mecanismo que hace reversible la imagen por la proyección.

> **Lectura fundacional.** Las familias de ideales son conjuntos por Potencia y Separación. Las imágenes y preimágenes se construyen como subconjuntos y los representantes se usan sólo mediante eliminación existencial local. No se selecciona una familia global de representantes y no interviene el axioma de elección ni lógica clásica sustantiva nueva.

---

## 30.30. Tercer teorema de isomorfía para anillos

### Teorema 30.30.1 — Tercer teorema de isomorfía para anillos {#talg-thm-00029}

Sea

$$
\mathcal R=\langle R,+,\cdot\rangle
$$

un anillo y sean $I,J\subseteq R$ ideales bilaterales tales que

$$
I\subseteq J.
\tag{124}
$$

Entonces $J/I$ es un ideal bilateral de $R/I$ y existe un isomorfismo de anillos

$$
\boxed{
(R/I)/(J/I)\cong R/J.
}
\tag{125}
$$

Más precisamente, existe un isomorfismo

$$
\widehat\rho:(R/I)/(J/I)\longrightarrow R/J
$$

caracterizado por

$$
\boxed{
\widehat\rho\bigl([[r]_I]_{J/I}\bigr)=[r]_J
}
\qquad(r\in R).
\tag{126}
$$

#### Demostración {#talg-prf-00160}

Por [Teorema 30.28.1](#talg-thm-00028), como $I\subseteq J$, el ideal imagen $J/I$ determina un ideal bilateral del anillo cociente $R/I$. Por tanto el cociente $(R/I)/(J/I)$ está bien tipado.

Consideremos las proyecciones canónicas

$$
q_I:R\longrightarrow R/I,
\qquad
q_J:R\longrightarrow R/J.
\tag{127}
$$

Por [Proposición 19.4.2](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00045), ambas son homomorfismos sobreyectivos de anillos y

$$
\ker q_I=I,
\qquad
\ker q_J=J.
\tag{128}
$$

Como $I\subseteq J=\ker q_J$, la propiedad universal del cociente de anillos, [Teorema 29.32.1](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md#talg-thm-00022), aplicada a $q_J$, proporciona un único homomorfismo de anillos

$$
\rho:R/I\longrightarrow R/J
\tag{129}
$$

tal que

$$
\rho\circ q_I=q_J.
\tag{130}
$$

En particular, para todo $r\in R$,

$$
\boxed{
\rho([r]_I)=[r]_J.
}
\tag{131}
$$

**1. Sobreyectividad de $\rho$.** Sea $D\in R/J$. Como $q_J$ es sobreyectiva, existe localmente $r\in R$ tal que

$$
D=q_J(r).
$$

Usando (130),

$$
D=q_J(r)=\rho(q_I(r)).
$$

Por tanto $\rho$ es sobreyectiva.

**2. Cálculo del núcleo.** Sea $C\in R/I$. Por la sobreyectividad de $q_I$, existe localmente $r\in R$ tal que

$$
C=q_I(r)=[r]_I.
\tag{132}
$$

Entonces, usando (130) y (128),

$$
\begin{aligned}
C\in\ker\rho
&\iff \rho(C)=0_{R/J}\\
&\iff \rho(q_I(r))=0_{R/J}\\
&\iff q_J(r)=0_{R/J}\\
&\iff r\in\ker q_J\\
&\iff r\in J.
\end{aligned}
\tag{133}
$$

La identidad de saturación de [Teorema 30.28.1](#talg-thm-00028) da, bajo la hipótesis $I\subseteq J$,

$$
r\in J
\iff
q_I(r)\in J/I.
\tag{134}
$$

Combinando (132)–(134),

$$
C\in\ker\rho
\iff
C\in J/I.
$$

Como $C\in R/I$ era arbitrario, Extensionalidad produce

$$
\boxed{
\ker\rho=J/I.
}
\tag{135}
$$

**3. Aplicación del primer teorema de isomorfía.** El homomorfismo $\rho$ es sobreyectivo y su núcleo es $J/I$. La forma sobreyectiva del primer teorema de isomorfía para anillos, [Corolario 20.3.1](tratado-de-algebra-capitulo-20-isomorfismos-y-primer-teorema-de-isomorfia-para-anillos.md#talg-cor-00011), produce un isomorfismo

$$
\widehat\rho:(R/I)/\ker\rho\longrightarrow R/J
$$

caracterizado por

$$
\widehat\rho([C]_{\ker\rho})=\rho(C).
\tag{136}
$$

Sustituyendo $\ker\rho=J/I$ y tomando $C=[r]_I$, las ecuaciones (131) y (136) dan

$$
\widehat\rho\bigl([[r]_I]_{J/I}\bigr)=[r]_J.
$$

Ésta es exactamente (126), y en particular obtenemos (125). $\square$

> **Punto estructural.** El tercer teorema combina tres mecanismos ya establecidos: la correspondencia certifica $J/I\triangleleft R/I$, la propiedad universal hace descender $q_J$ a $R/I$, y el primer teorema de isomorfía se aplica al homomorfismo concreto resultante. La teoría general de descenso se desarrolla en el [capítulo 31](tratado-de-algebra-capitulo-31-descenso-y-transporte-de-estructura.md#talg-thm-00031).

> **Lectura fundacional.** La representación $C=q_I(r)$ se utiliza sólo localmente a partir de la sobreyectividad de $q_I$; no se selecciona un representante para cada clase de $R/I$. No intervienen el axioma de elección ni lógica clásica sustantiva nueva.

---

## 30.32. Síntesis estructural

El capítulo completa la secuencia anunciada en §30.0 para grupos y anillos.

En grupos, para un subgrupo $H\le G$ y un subgrupo normal $N\trianglelefteq G$, el producto de subconjuntos $HN$ es un subgrupo y se tienen las normalidades $N\trianglelefteq HN$ y $H\cap N\trianglelefteq H$. Esto permite construir el segundo isomorfismo:

$$
H/(H\cap N)\cong HN/N.
$$

La correspondencia identifica los subgrupos de $G$ que contienen $N$ con los subgrupos de $G/N$ y preserva y refleja inclusión y normalidad. Cuando además $N\subseteq H$ y $H\trianglelefteq G$, se obtiene el tercer isomorfismo:

$$
(G/N)/(H/N)\cong G/H.
$$

Los resultados de esta cadena son [Definición 30.6.1](#talg-def-00068), [Proposición 30.8.1](#talg-pro-00102), [Proposición 30.10.1](#talg-pro-00103), [Teorema 30.13.1](#talg-thm-00024), [Teorema 30.16.1](#talg-thm-00025) y [Teorema 30.18.1](#talg-thm-00026).

En anillos, para un subanillo unital $S$ de $R$ y un ideal bilateral $I$, el conjunto $S+I$ es un subanillo unital, $I$ es un ideal bilateral de $S+I$ y $S\cap I$ es un ideal bilateral de $S$. Esto permite construir el segundo isomorfismo:

$$
S/(S\cap I)\cong (S+I)/I.
$$

La correspondencia identifica los ideales bilaterales de $R$ que contienen $I$ con los ideales bilaterales de $R/I$ y preserva y refleja inclusión. Si $I\subseteq J$ son ideales bilaterales de $R$, se obtiene el tercer isomorfismo:

$$
(R/I)/(J/I)\cong R/J.
$$

Los resultados de esta cadena son [Definición 30.21.1](#talg-def-00069), [Proposición 30.23.1](#talg-pro-00104), [Teorema 30.25.1](#talg-thm-00027), [Teorema 30.28.1](#talg-thm-00028) y [Teorema 30.30.1](#talg-thm-00029).

En ambos casos, los morfismos se construyen concretamente como restricciones de proyecciones canónicas o como factores únicos suministrados por las propiedades universales de los cocientes de grupos ([Teorema 29.29.1](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md#talg-thm-00021)) y anillos ([Teorema 29.32.1](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md#talg-thm-00022)). La identidad y composición generales de morfismos inducidos, el transporte sistemático de subestructuras y los criterios generales de isomorfía inducida se estudian en el [capítulo 31](tratado-de-algebra-capitulo-31-descenso-y-transporte-de-estructura.md).

---

[← **Capítulo 29 — Productos directos y propiedades universales**](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md) · [**Capítulo 31 — Descenso y transporte de estructura** →](tratado-de-algebra-capitulo-31-descenso-y-transporte-de-estructura.md)
