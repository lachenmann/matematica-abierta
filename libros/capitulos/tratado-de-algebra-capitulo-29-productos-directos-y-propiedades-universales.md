---
title: 'Tratado moderno de Álgebra — Capítulo 29: Productos directos y propiedades universales'
description: Capítulo del Tratado moderno de Álgebra dedicado a productos directos y propiedades universales de productos, cocientes y cuerpos de fracciones.
author: Gustav A. Tachek
content-id: MA-BCH-0137
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
- productos-directos
- propiedades-universales
- cocientes
- cuerpo-de-fracciones
prerequisites:
- MA-BCH-0136
related:
- MA-BOK-0007
- MA-BCH-0136
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

## 29.0. Por qué la Parte VI comienza aquí

Las Partes II–V ya construyeron homomorfismos, núcleos, imágenes, cocientes, isomorfismos y primeros teoremas de isomorfía para grupos y anillos. Por tanto, la Parte VI no debe volver a demostrar que

$$
G/\ker f\cong \operatorname{im}f
$$

o que

$$
R/\ker f\cong \operatorname{im}f.
$$

Su función es hacer explícitos los **principios estructurales que esas pruebas particulares ya anticipaban** y utilizarlos después de manera transversal.

Quedan tres huecos concretos:

1. la arquitectura inicial prometía productos de estructuras, pero ninguna unidad canónica de las Partes I–V llegó a construirlos;
2. los cocientes de grupos y anillos fueron construidos y sus proyecciones demostradas homomórficas, pero todavía no se ha aislado la propiedad universal general de factorización por un cociente;
3. el cuerpo de fracciones fue construido y recibió su inmersión canónica, pero su propiedad universal quedó pendiente para esta Parte VI.

El capítulo 29 reunirá esas tres capas antes de pasar a los teoremas de isomorfía superiores.

## 29.2. Alcance del capítulo 29

El capítulo organiza su desarrollo en cinco núcleos matemáticos —productos de grupos, productos de anillos, cocientes de grupos, cocientes de anillos y cuerpo de fracciones— seguidos por una síntesis estructural. el objetivo no es sólo comprobar ecuaciones, sino hacer visible la diferencia entre **construir un objeto**, **probar que satisface una propiedad** y **demostrar que esa propiedad lo caracteriza mediante existencia y unicidad de morfismos**.

### 29.2.1. Alcance excluido

Quedan fuera del capítulo 29:

- productos infinitos;
- coproductos y productos libres;
- una axiomatización general de categorías, límites o colímites;
- módulos, espacios vectoriales y productos tensoriales;
- topología de productos;
- elección de bases o representantes;
- segundo y tercer teorema de isomorfía, que pertenecen a 6.2;
- teoría general de morfismos inducidos entre dos cocientes, que se sistematizará en 6.3.

La palabra **universal** se expresará aquí mediante diagramas y cuantificadores de existencia y unicidad de homomorfismos, sin presuponer lenguaje categórico adicional.

## 29.6. Producto directo de dos magmas

La primera construcción de la Parte VI combina dos estructuras sin hacer interactuar sus coordenadas. Si el primer magma opera en $A$ y el segundo en $B$, la operación del producto actuará en $A\times B$ aplicando cada operación únicamente en su componente correspondiente.

Este paso debe distinguir dos cuestiones. Primero, la regla coordenada debe definir realmente una operación binaria sobre $A\times B$. Segundo, como en este tratado un magma tiene conjunto subyacente no vacío, debemos verificar también que $A\times B$ sea no vacío.

### Definición 29.6.1 — Producto directo de dos magmas {#talg-def-00065}
Sean

$$
\mathcal M=\langle A,\star\rangle,
\qquad
\mathcal N=\langle B,\diamond\rangle
$$

dos magmas. Para $a,a'\in A$ y $b,b'\in B$ definimos la regla coordenada

$$
\boxed{
\langle a,b\rangle\,(\star\times\diamond)\,\langle a',b'\rangle
:=
\langle a\star a',\,b\diamond b'\rangle.
}
$$

Esta regla determina una función

$$
\star\times\diamond:
(A\times B)\times(A\times B)
\longrightarrow
A\times B.
$$

En efecto, si $a,a'\in A$, entonces $a\star a'\in A$ porque $\star$ es una operación binaria sobre $A$; análogamente, $b\diamond b'\in B$. Por tanto

$$
\langle a\star a',\,b\diamond b'\rangle\in A\times B.
$$

Además, cada elemento de $A\times B$ tiene coordenadas determinadas por la igualdad de pares ordenados. Así, para cada elemento de $(A\times B)\times(A\times B)$ la fórmula anterior asigna un único valor en $A\times B$; su grafo existe por Separación dentro del producto cartesiano correspondiente. Por la Definición 1.1.1, $\star\times\diamond$ es una operación binaria sobre $A\times B$.

Queda verificar la convención de no vacuidad. Como $\mathcal M$ y $\mathcal N$ son magmas, $A\ne\varnothing$ y $B\ne\varnothing$. En la lógica clásica ambiente, de estas dos no vacuidades obtenemos testigos locales $a_0\in A$ y $b_0\in B$. Entonces

$$
\langle a_0,b_0\rangle\in A\times B,
$$

de modo que $A\times B\ne\varnothing$.

Definimos el **producto directo** de $\mathcal M$ y $\mathcal N$ por

$$
\boxed{
\mathcal M\times\mathcal N
:=
\langle A\times B,\,\star\times\diamond\rangle.
}
$$

Por lo anterior, $\mathcal M\times\mathcal N$ es un magma.

> **Lectura tipológica.** En $\mathcal M\times\mathcal N$ el símbolo exterior $\times$ designa una estructura algebraica cuyo conjunto subyacente es el producto cartesiano $A\times B$. No se identifica el magma con su conjunto subyacente. Del mismo modo, $\star\times\diamond$ es una nueva operación binaria construida a partir de las operaciones de los dos factores.

> **Frontera de esta definición.** No se ha demostrado todavía que asociatividad, neutros o inversos pasen al producto. La definición construye únicamente el magma producto; las leyes adicionales se tratarán como consecuencias separadas.

### Sobre el uso clásico de no vacuidad

La operación coordenada y su tipado no requieren lógica clásica sustantiva. El único paso clásico aparece al verificar que el conjunto subyacente del producto es no vacío bajo la convención vigente de magma: el protocolo distingue $A\ne\varnothing$ de disponer constructivamente de un testigo $a\in A$.

Para estos dos conjuntos fijos, la lógica clásica permite extraer sendos testigos y formar un elemento de $A\times B$. Esta eliminación existencial es local y no define una función que seleccione elementos de una familia de conjuntos; por tanto **no usa el axioma de elección**. Si los conjuntos subyacentes vinieran dados como habitados, la misma verificación sería constructiva.

## 29.8. Herencia de semigrupo, monoide y grupo

La operación producto ya existe al nivel de magmas. El paso siguiente no consiste en definir nuevas operaciones, sino en comprobar qué leyes adicionales de los factores se conservan coordenada por coordenada.

### Proposición 29.8.1 — Herencia de semigrupo, monoide y grupo por producto directo {#talg-pro-00098}
Sean
$$
\mathcal M=\langle A,\star\rangle,
\qquad
\mathcal N=\langle B,\diamond\rangle,
$$
y sea $\mathcal M\times\mathcal N$ el magma producto de la Definición 29.6.1.

1. Si $\mathcal M$ y $\mathcal N$ son semigrupos, entonces $\mathcal M\times\mathcal N$ es un semigrupo.
2. Si $\mathcal M$ y $\mathcal N$ son monoides, entonces $\mathcal M\times\mathcal N$ es un monoide y
   $$
   e_{\mathcal M\times\mathcal N}
   =
   \langle e_{\mathcal M},e_{\mathcal N}\rangle.
   $$
3. Si $\mathcal M$ y $\mathcal N$ son grupos, entonces $\mathcal M\times\mathcal N$ es un grupo y, para todo $\langle a,b\rangle\in A\times B$,
   $$
   \langle a,b\rangle^{-1}
   =
   \langle a^{-1},b^{-1}\rangle.
   $$

#### Demostración {#talg-prf-00143}
**Hipótesis.** En cada apartado, los dos factores poseen la estructura indicada.

**Objetivo.** Verificar que la estructura correspondiente pasa al producto y determinar, cuando existan, su neutro y sus inversos.

**1. Caso de semigrupos.** Por la Definición 29.6.1, $\mathcal M\times\mathcal N$ ya es un magma. Sean
$$
x=\langle a,b\rangle,\qquad
y=\langle a',b'\rangle,\qquad
z=\langle a'',b''\rangle
$$
elementos de $A\times B$. Entonces
$$
\begin{aligned}
(x(\star\times\diamond)y)(\star\times\diamond)z
&=
\langle (a\star a')\star a'',\,(b\diamond b')\diamond b''\rangle\\
&=
\langle a\star(a'\star a''),\,b\diamond(b'\diamond b'')\rangle\\
&=
x(\star\times\diamond)(y(\star\times\diamond)z).
\end{aligned}
$$
La segunda igualdad usa exactamente la asociatividad de $\star$ y de $\diamond$, disponible porque ambos factores son semigrupos; la igualdad de los pares se justifica coordenada por coordenada. Por la Definición 2.1.1, el magma producto es un semigrupo.

**2. Caso de monoides.** Supongamos ahora que $\mathcal M$ y $\mathcal N$ son monoides. Por el apartado anterior, su producto ya es un semigrupo. Consideremos
$$
e:=
\langle e_{\mathcal M},e_{\mathcal N}\rangle
\in A\times B.
$$
Para todo $x=\langle a,b\rangle\in A\times B$,
$$
\begin{aligned}
e(\star\times\diamond)x
&=
\langle e_{\mathcal M}\star a,\,
        e_{\mathcal N}\diamond b\rangle
=
\langle a,b\rangle
=
x,\\
x(\star\times\diamond)e
&=
\langle a\star e_{\mathcal M},\,
        b\diamond e_{\mathcal N}\rangle
=
\langle a,b\rangle
=
x.
\end{aligned}
$$
Así, $e$ es neutro bilateral de la operación producto. Por la Definición 3.2.1, $\mathcal M\times\mathcal N$ es un monoide. Como la notación $e_{\mathcal M\times\mathcal N}$ designa su único neutro,
$$
e_{\mathcal M\times\mathcal N}
=
\langle e_{\mathcal M},e_{\mathcal N}\rangle.
$$

**3. Caso de grupos.** Supongamos finalmente que $\mathcal M$ y $\mathcal N$ son grupos. Por el apartado anterior, su producto es un monoide con neutro
$$
e_{\mathcal M\times\mathcal N}
=
\langle e_{\mathcal M},e_{\mathcal N}\rangle.
$$
Sea $x=\langle a,b\rangle\in A\times B$. Como los factores son grupos, existen los inversos $a^{-1}\in A$ y $b^{-1}\in B$. Por tanto
$$
y:=
\langle a^{-1},b^{-1}\rangle
\in A\times B.
$$
Usando la operación producto,
$$
\begin{aligned}
y(\star\times\diamond)x
&=
\langle a^{-1}\star a,\,
        b^{-1}\diamond b\rangle
=
\langle e_{\mathcal M},e_{\mathcal N}\rangle
=
e_{\mathcal M\times\mathcal N},\\
x(\star\times\diamond)y
&=
\langle a\star a^{-1},\,
        b\diamond b^{-1}\rangle
=
\langle e_{\mathcal M},e_{\mathcal N}\rangle
=
e_{\mathcal M\times\mathcal N}.
\end{aligned}
$$
Así, todo elemento del producto posee un inverso bilateral. Por la Definición 4.2.1, $\mathcal M\times\mathcal N$ es un grupo. La unicidad incorporada en la Notación 4.2.2 identifica el inverso encontrado:
$$
\langle a,b\rangle^{-1}
=
\langle a^{-1},b^{-1}\rangle.
$$
Esto concluye los tres apartados. $\square$

> **Lectura estructural.** Ninguna ley «aparece» por el símbolo $\times$. Cada propiedad se verifica en las dos coordenadas: asociatividad en la primera y en la segunda; luego neutro en la primera y en la segunda; finalmente inversos en la primera y en la segunda.

> **Prueba de estrés.** Si uno de los factores es solamente un magma no asociativo, el producto no puede justificarse como semigrupo por este argumento: la coordenada defectuosa reaparece sin alteración en la ecuación asociativa del producto. Del mismo modo, un neutro o un inverso ausente en una coordenada no se crea por formar el producto.

## 29.11. Proyecciones canónicas del producto directo de grupos

El producto directo de grupos ya está construido sobre el conjunto cartesiano $G\times H$. Antes de formular su propiedad universal aislamos las dos funciones que recuperan las coordenadas. Primero se construyen como funciones; que preserven la operación será una proposición posterior.

### Definición 29.11.1 — Proyecciones canónicas del producto directo de grupos {#talg-def-00066}
Sean

$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

dos grupos. Por la Definición 29.6.1 y la Proposición 29.8.1, su producto directo

$$
\mathcal G\times\mathcal H
=
\langle G\times H,\star\times\diamond\rangle
$$

es un grupo.

Consideremos los subconjuntos

$$
\Gamma_G
:=
\bigl\{\langle x,g\rangle\in(G\times H)\times G:
\exists h\in H\;(x=\langle g,h\rangle)\bigr\},
$$

y

$$
\Gamma_H
:=
\bigl\{\langle x,h\rangle\in(G\times H)\times H:
\exists g\in G\;(x=\langle g,h\rangle)\bigr\}.
$$

Ambos conjuntos existen por Separación a partir de los productos cartesianos indicados. Verifiquemos que son grafos funcionales con dominio $G\times H$.

Sea $x\in G\times H$. Por la definición de producto cartesiano existen $g\in G$ y $h\in H$ tales que

$$
x=\langle g,h\rangle.
$$

En consecuencia,

$$
\langle x,g\rangle\in\Gamma_G,
\qquad
\langle x,h\rangle\in\Gamma_H,
$$

de modo que cada una de las dos relaciones asigna al menos un valor a $x$ en su codominio respectivo.

La unicidad procede de la igualdad de pares ordenados. Si

$$
x=\langle g,h\rangle=\langle g',h'\rangle,
$$

entonces

$$
g=g',
\qquad
h=h'.
$$

Por tanto, para cada $x\in G\times H$, $\Gamma_G$ contiene exactamente un par de la forma $\langle x,g\rangle$ y $\Gamma_H$ exactamente uno de la forma $\langle x,h\rangle$. Así, estos grafos determinan funciones

$$
\boxed{
\pi_G:G\times H\longrightarrow G,
\qquad
\pi_G(\langle g,h\rangle)=g,
}
$$

y

$$
\boxed{
\pi_H:G\times H\longrightarrow H,
\qquad
\pi_H(\langle g,h\rangle)=h.
}
$$

Llamaremos a $\pi_G$ la **primera proyección canónica** y a $\pi_H$ la **segunda proyección canónica** del producto directo $\mathcal G\times\mathcal H$.

> **Lectura tipológica.** Las proyecciones tienen como dominio el conjunto subyacente $G\times H$ del grupo producto y como codominios los conjuntos subyacentes $G$ y $H$. En esta definición no se ha usado todavía la ley de grupo para demostrar que preserven operaciones.

> **Frontera de la definición.** No se afirma aquí que $\pi_G$ o $\pi_H$ sean homomorfismos, inyectivas o sobreyectivas. Tampoco se formula aún la propiedad universal del producto ni se introduce la notación $\langle f,g\rangle$ para un morfismo mediador.

---

## 29.13. Las proyecciones preservan la operación

Las proyecciones canónicas ya existen como funciones. Para utilizarlas en la propiedad universal del producto debemos comprobar ahora, y sólo ahora, que respetan las operaciones de los grupos implicados. La verificación es puramente coordenada.

### Proposición 29.13.1 — Homomorfía de las proyecciones canónicas del producto directo de grupos {#talg-pro-00099}
Sean

$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

dos grupos. Sean

$$
\pi_G:G\times H\to G,
\qquad
\pi_H:G\times H\to H
$$

las proyecciones canónicas de la Definición 29.11.1. Entonces ambas funciones son homomorfismos de grupos desde el producto directo $\mathcal G\times\mathcal H$ hacia sus respectivos factores.

#### Demostración {#talg-prf-00144}
Por la Proposición 29.8.1,

$$
\mathcal G\times\mathcal H
=
\langle G\times H,\star\times\diamond\rangle
$$

es un grupo. Por la Definición 29.11.1, $\pi_G$ y $\pi_H$ son funciones con los dominios y codominios indicados. De acuerdo con la Definición 7.4.1, basta comprobar que cada una preserva la operación correspondiente.

Sean

$$
x=\langle g,h\rangle,
\qquad
y=\langle g',h'\rangle
$$

elementos arbitrarios de $G\times H$. Por la definición de la operación producto,

$$
x(\star\times\diamond)y
=
\langle g\star g',\,h\diamond h'\rangle.
$$

**Primera proyección.** Aplicando $\pi_G$,

$$
\begin{aligned}
\pi_G\bigl(x(\star\times\diamond)y\bigr)
&=
\pi_G\bigl(\langle g\star g',h\diamond h'\rangle\bigr)\\
&=g\star g'\\
&=\pi_G(x)\star\pi_G(y).
\end{aligned}
$$

Como $x$ e $y$ eran arbitrarios, $\pi_G$ preserva la operación del grupo producto. Por la definición «Homomorfismo de grupos»,

$$
\pi_G:G\times H\to G
$$

es un homomorfismo de grupos.

**Segunda proyección.** Análogamente,

$$
\begin{aligned}
\pi_H\bigl(x(\star\times\diamond)y\bigr)
&=
\pi_H\bigl(\langle g\star g',h\diamond h'\rangle\bigr)\\
&=h\diamond h'\\
&=\pi_H(x)\diamond\pi_H(y).
\end{aligned}
$$

Así, $\pi_H$ preserva la operación y, nuevamente por la definición «Homomorfismo de grupos»,

$$
\pi_H:G\times H\to H
$$

es un homomorfismo de grupos. $\square$

> **Lectura estructural.** La homomorfía no es una propiedad añadida a las proyecciones por definición. Surge porque la operación del producto fue definida coordenada por coordenada y cada proyección descarta precisamente la coordenada que no necesita.

> **Qué no se ha usado.** No fue necesario demostrar por separado preservación del neutro o de los inversos: la Definición 7.4.1 caracteriza los homomorfismos de grupos únicamente por la preservación de la operación. Tampoco se usaron cancelación, conmutatividad, inyectividad ni sobreyectividad.

---

## 29.16. Propiedad universal del producto directo de grupos

Las proyecciones canónicas ya existen y son homomorfismos. Podemos cerrar ahora el principio que caracteriza al producto directo: todo par de homomorfismos con dominio común determina un único homomorfismo hacia el producto cuyas dos coordenadas son precisamente los homomorfismos dados.

### Teorema 29.16.1 — Propiedad universal del producto directo de grupos {#talg-thm-00019}
Sean

$$
\mathcal K=\langle K,\circ\rangle,
\qquad
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

grupos, y sean homomorfismos

$$
f:K\to G,
\qquad
g:K\to H.
$$

Sean además

$$
\pi_G:G\times H\to G,
\qquad
\pi_H:G\times H\to H
$$

las proyecciones canónicas del producto directo $\mathcal G\times\mathcal H$.

Entonces existe un **único homomorfismo de grupos**

$$
u:K\to G\times H
$$

tal que

$$
\boxed{\pi_G\circ u=f},
\qquad
\boxed{\pi_H\circ u=g}. \tag{1}
$$

Ese homomorfismo está determinado punto a punto por

$$
\boxed{
 u(k)=\langle f(k),g(k)\rangle
}\qquad(k\in K). \tag{2}
$$

#### Demostración {#talg-prf-00145}
**1. Construcción y tipado del mediador.** Consideremos

$$
\Gamma
:=
\bigl\{
\langle k,z\rangle\in K\times(G\times H):
 z=\langle f(k),g(k)\rangle
\bigr\}. \tag{3}
$$

El conjunto $\Gamma$ existe por Separación. Sea $k\in K$. Como $f:K\to G$ y $g:K\to H$,

$$
f(k)\in G,
\qquad
g(k)\in H,
$$

y por la definición de producto cartesiano

$$
\langle f(k),g(k)\rangle\in G\times H. \tag{4}
$$

Por tanto, $\Gamma$ asigna al menos un valor a cada $k\in K$. Ese valor es único: si

$$
\langle k,z\rangle\in\Gamma
\qquad\text{y}\qquad
\langle k,z'\rangle\in\Gamma,
$$

entonces, por la condición que define a $\Gamma$,

$$
z=\langle f(k),g(k)\rangle=z'.
$$

Así, $\Gamma$ determina una función

$$
u:K\to G\times H
$$

satisfaciendo exactamente (2).

**2. El mediador es un homomorfismo.** Por la Proposición 29.8.1,

$$
\mathcal G\times\mathcal H
=
\langle G\times H,\star\times\diamond\rangle
$$

es un grupo. Sean $k,\ell\in K$. Como $f$ y $g$ son homomorfismos,

$$
f(k\circ\ell)=f(k)\star f(\ell),
\qquad
g(k\circ\ell)=g(k)\diamond g(\ell). \tag{5}
$$

Entonces

$$
\begin{aligned}
u(k\circ\ell)
&=\langle f(k\circ\ell),g(k\circ\ell)\rangle\\
&=\langle f(k)\star f(\ell),\,g(k)\diamond g(\ell)\rangle\\
&=\langle f(k),g(k)\rangle
   (\star\times\diamond)
   \langle f(\ell),g(\ell)\rangle\\
&=u(k)(\star\times\diamond)u(\ell).
\end{aligned} \tag{6}
$$

Por la Definición 7.4.1, $u$ es un homomorfismo de grupos.

**3. Primera ecuación de proyección.** Para todo $k\in K$,

$$
\begin{aligned}
(\pi_G\circ u)(k)
&=\pi_G(u(k))\\
&=\pi_G(\langle f(k),g(k)\rangle)\\
&=f(k).
\end{aligned}
$$

Las funciones $\pi_G\circ u$ y $f$ tienen el mismo dominio $K$ y coinciden en cada elemento de él; por extensionalidad funcional,

$$
\pi_G\circ u=f. \tag{7}
$$

**4. Segunda ecuación de proyección.** Del mismo modo, para todo $k\in K$,

$$
\begin{aligned}
(\pi_H\circ u)(k)
&=\pi_H(u(k))\\
&=\pi_H(\langle f(k),g(k)\rangle)\\
&=g(k),
\end{aligned}
$$

y por extensionalidad funcional

$$
\pi_H\circ u=g. \tag{8}
$$

Esto demuestra la existencia de un homomorfismo que satisface (1).

**5. Unicidad.** Sea

$$
v:K\to G\times H
$$

un homomorfismo de grupos que también satisfaga

$$
\pi_G\circ v=f,
\qquad
\pi_H\circ v=g. \tag{9}
$$

Fijemos $k\in K$. Como $v(k)\in G\times H$, existen $a\in G$ y $b\in H$ tales que

$$
v(k)=\langle a,b\rangle. \tag{10}
$$

Aplicando la primera proyección y usando (9),

$$
a
=\pi_G(v(k))
=(\pi_G\circ v)(k)
=f(k). \tag{11}
$$

Análogamente,

$$
b
=\pi_H(v(k))
=(\pi_H\circ v)(k)
=g(k). \tag{12}
$$

Sustituyendo (11) y (12) en (10),

$$
v(k)
=\langle f(k),g(k)\rangle
=u(k).
$$

Como $k$ era arbitrario, la extensionalidad funcional da

$$
v=u.
$$

Por tanto, el homomorfismo construido es único. $\square$

> **Lectura estructural.** La existencia usa la fórmula coordenada explícita; la homomorfía se verifica en ambas coordenadas; la unicidad dice que ninguna otra función hacia $G\times H$ puede tener simultáneamente las mismas dos proyecciones. Éste es el contenido concreto de la palabra «universal» en este capítulo.

> **Fortaleza de la unicidad.** En el último paso no fue necesario usar que $v$ fuera homomorfismo: su tipado $K\to G\times H$ y las dos ecuaciones de proyección ya fuerzan sus valores. El teorema, sin embargo, cuantifica la unicidad entre homomorfismos porque ése es el tipo estructural pertinente.

### Notación habilitada por el teorema

Una vez demostradas existencia y unicidad, para homomorfismos con dominio común

$$
f:K\to G,
\qquad
g:K\to H,
$$

denotaremos por

$$
\boxed{
\langle f,g\rangle:K\to G\times H
}
$$

el único homomorfismo mediador del teorema. Así,

$$
\langle f,g\rangle(k)
=
\langle f(k),g(k)\rangle,
$$

$$
\pi_G\circ\langle f,g\rangle=f,
\qquad
\pi_H\circ\langle f,g\rangle=g.
$$

En este contexto tipado, $\langle f,g\rangle$ designa **una función hacia el producto**, no el par ordenado conjuntista de las funciones $f$ y $g$. Fuera de este contexto no se hará esa lectura automáticamente.

---

## 29.19. Estructura producto coordenada de dos anillos

Conviene separar dos tareas: primero construir, sobre el conjunto $R\times S$, las dos operaciones coordenadas que provienen de los factores; sólo después demostrar que el paquete resultante satisface los axiomas de anillo.

### Definición 29.19.1 — Estructura producto coordenada de dos anillos {#talg-def-00067}
Sean

$$
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

dos anillos.

Por la definición «Anillo», $+_R$ y $+_S$ son operaciones binarias sobre $R$ y $S$, respectivamente; lo mismo ocurre con $\cdot_R$ y $\cdot_S$. Por tanto la definición «Producto directo de dos magmas» puede aplicarse por separado a cada par de operaciones.

Definimos la **suma coordenada** sobre $R\times S$ por

$$
\boxed{
+_{R\times S}
:=
+_R\times+_S,
}
$$

de modo que, para $r,r'\in R$ y $s,s'\in S$,

$$
\boxed{
\langle r,s\rangle+_{R\times S}\langle r',s'\rangle
=
\langle r+_Rr',\,s+_Ss'\rangle.
}
$$

Esta es una función bien tipada

$$
+_{R\times S}:
(R\times S)\times(R\times S)
\longrightarrow
R\times S.
$$

Análogamente, definimos el **producto coordenado** por

$$
\boxed{
\cdot_{R\times S}
:=
\cdot_R\times\cdot_S,
}
$$

de modo que

$$
\boxed{
\langle r,s\rangle\cdot_{R\times S}\langle r',s'\rangle
=
\langle r\cdot_Rr',\,s\cdot_Ss'\rangle,
}
$$

y

$$
\cdot_{R\times S}:
(R\times S)\times(R\times S)
\longrightarrow
R\times S.
$$

Reunimos ambas operaciones en la estructura

$$
\boxed{
\mathcal R\times\mathcal S
:=
\left\langle
R\times S,
+_{R\times S},
\cdot_{R\times S}
\right\rangle.
}
$$

Llamaremos a este objeto la **estructura producto coordenada** de $\mathcal R$ y $\mathcal S$.

> **Frontera de la definición.** La expresión $\mathcal R\times\mathcal S$ designa aquí únicamente el conjunto $R\times S$ equipado con las dos operaciones coordenadas recién construidas. Todavía no se afirma que constituya un anillo: faltan por demostrar la estructura de grupo abeliano para la suma, la estructura de monoide para el producto y ambas leyes distributivas.

> **Neutros todavía no fijados.** Aunque la arquitectura anticipa que el cero y la unidad del futuro anillo producto serán $\langle0_R,0_S\rangle$ y $\langle1_R,1_S\rangle$, esas identidades no forman parte de esta definición. Se obtendrán en el resultado que certifique los axiomas de anillo.

> **Lectura tipológica.** Las dos operaciones tienen exactamente el mismo conjunto subyacente y exactamente el mismo dominio cuadrado. No se construyen dos productos cartesianos distintos: se equipa un único conjunto $R\times S$ con dos funciones binarias diferentes.

---

## 29.21. La estructura producto coordinada es un anillo

La estructura de la Definición 29.19.1 ya posee dos operaciones binarias bien tipadas sobre el mismo conjunto $R\times S$. Falta comprobar ahora que esas operaciones satisfacen exactamente los axiomas de anillo, sin introducir ninguna ley adicional.

### Proposición 29.21.1 — La estructura producto coordenada de dos anillos es un anillo {#talg-pro-00100}
Sean

$$
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

dos anillos, y sea

$$
\mathcal R\times\mathcal S
=
\left\langle
R\times S,
+_{R\times S},
\cdot_{R\times S}
\right\rangle
$$

la estructura producto coordenada de la Definición 29.19.1. Entonces $\mathcal R\times\mathcal S$ es un anillo.

Sus neutros y opuestos aditivos están dados por

$$
\boxed{
0_{\mathcal R\times\mathcal S}
=
\langle0_{\mathcal R},0_{\mathcal S}\rangle,
}
$$

$$
\boxed{
1_{\mathcal R\times\mathcal S}
=
\langle1_{\mathcal R},1_{\mathcal S}\rangle,
}
$$

y, para todo $\langle r,s\rangle\in R\times S$,

$$
\boxed{
-\langle r,s\rangle
=
\langle-r,-s\rangle.
}
$$

#### Demostración {#talg-prf-00146}
Debemos verificar las cuatro condiciones de la definición «Anillo».

**1. Grupo aditivo abeliano.** Como $\mathcal R$ y $\mathcal S$ son anillos, sus estructuras aditivas

$$
\langle R,+_R\rangle,
\qquad
\langle S,+_S\rangle
$$

son grupos abelianos. En particular son grupos. Aplicando la proposición «Herencia de semigrupo, monoide y grupo por producto directo» a esas estructuras y usando que la suma de la Definición 29.19.1 es precisamente $+_R\times+_S$, obtenemos que

$$
\langle R\times S,+_{R\times S}\rangle
$$

es un grupo. La misma proposición fija su neutro y sus inversos:

$$
0_{\mathcal R\times\mathcal S}
=
\langle0_{\mathcal R},0_{\mathcal S}\rangle,
$$

$$
-\langle r,s\rangle
=
\langle-r,-s\rangle.
$$

Queda comprobar la conmutatividad. Sean

$$
x=\langle r,s\rangle,
\qquad
y=\langle r',s'\rangle
$$

elementos de $R\times S$. Como las sumas de los factores son conmutativas,

$$
\begin{aligned}
x+_{R\times S}y
&=\langle r+_Rr',\,s+_Ss'\rangle\\
&=\langle r'+_Rr,\,s'+_Ss\rangle\\
&=y+_{R\times S}x.
\end{aligned}
$$

Por tanto la estructura aditiva del producto es un grupo abeliano.

**2. Monoide multiplicativo.** Los factores multiplicativos

$$
\langle R,\cdot_R\rangle,
\qquad
\langle S,\cdot_S\rangle
$$

son monoides. Aplicando nuevamente la proposición «Herencia de semigrupo, monoide y grupo por producto directo», ahora a las multiplicaciones, y usando $\cdot_{R\times S}=\cdot_R\times\cdot_S$, obtenemos que

$$
\langle R\times S,\cdot_{R\times S}\rangle
$$

es un monoide y que su neutro es

$$
1_{\mathcal R\times\mathcal S}
=
\langle1_{\mathcal R},1_{\mathcal S}\rangle.
$$

No se ha supuesto conmutatividad de la multiplicación.

**3. Distributividad por la izquierda.** Sean

$$
x=\langle r,s\rangle,
\qquad
y=\langle a,b\rangle,
\qquad
z=\langle c,d\rangle
$$

elementos de $R\times S$. Entonces

$$
\begin{aligned}
x\cdot_{R\times S}(y+_{R\times S}z)
&=\langle r,s\rangle\cdot_{R\times S}
  \langle a+_Rc,\,b+_Sd\rangle\\
&=\langle r\cdot_R(a+_Rc),\,s\cdot_S(b+_Sd)\rangle\\
&=\langle r\cdot_Ra+_Rr\cdot_Rc,\,
          s\cdot_Sb+_Ss\cdot_Sd\rangle\\
&=\langle r\cdot_Ra,\,s\cdot_Sb\rangle
  +_{R\times S}
  \langle r\cdot_Rc,\,s\cdot_Sd\rangle\\
&=(x\cdot_{R\times S}y)+_{R\times S}(x\cdot_{R\times S}z).
\end{aligned}
$$

La tercera igualdad usa la distributividad izquierda en $\mathcal R$ y en $\mathcal S$.

**4. Distributividad por la derecha.** Con los mismos elementos,

$$
\begin{aligned}
(x+_{R\times S}y)\cdot_{R\times S}z
&=\langle r+_Ra,\,s+_Sb\rangle\cdot_{R\times S}\langle c,d\rangle\\
&=\langle (r+_Ra)\cdot_Rc,\,(s+_Sb)\cdot_Sd\rangle\\
&=\langle r\cdot_Rc+_Ra\cdot_Rc,\,
          s\cdot_Sd+_Sb\cdot_Sd\rangle\\
&=\langle r\cdot_Rc,\,s\cdot_Sd\rangle
  +_{R\times S}
  \langle a\cdot_Rc,\,b\cdot_Sd\rangle\\
&=(x\cdot_{R\times S}z)+_{R\times S}(y\cdot_{R\times S}z).
\end{aligned}
$$

La tercera igualdad usa la distributividad derecha en ambos factores.

Hemos verificado grupo aditivo abeliano, monoide multiplicativo y las dos leyes distributivas. Por la definición «Anillo», $\mathcal R\times\mathcal S$ es un anillo. $\square$

> **Lectura estructural.** Los axiomas de anillo del producto no requieren nuevas leyes: cada axioma se verifica por separado en las dos coordenadas. La única pieza que no se obtiene directamente de la proposición «Herencia de semigrupo, monoide y grupo por producto directo» es la conmutatividad de la suma, porque esa proposición hereda estructura de grupo pero no añade abelianidad.

> **Orden deductivo.** La homomorfía de las proyecciones, incluida la preservación de la unidad multiplicativa, se demuestra en §29.23.

> **Qué no se ha supuesto.** No se exige $0\neq1$, no se presupone conmutatividad multiplicativa y no se utiliza cancelación. El producto es un anillo incluso cuando uno o ambos factores son triviales.

---

## 29.23. Las proyecciones del producto de anillos son homomorfismos unitarios

Las funciones coordenadas ya construidas para productos de grupos pueden reutilizarse sin redefinición: los anillos $\mathcal R$ y $\mathcal S$ tienen grupos aditivos subyacentes sobre los mismos conjuntos $R$ y $S$, de modo que las proyecciones canónicas de la Definición 29.11.1 son exactamente las funciones

$$
\pi_R:R\times S\to R,
\qquad
\pi_S:R\times S\to S.
$$

Ahora que la Proposición 29.21.1 certificó que $\mathcal R\times\mathcal S$ es un anillo, resta verificar que estas funciones preservan las tres piezas exigidas por la convención unital del tratado: suma, producto y unidad multiplicativa.

### Proposición 29.23.1 — Homomorfía de las proyecciones canónicas del producto directo de anillos {#talg-pro-00101}
Sean

$$
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

dos anillos, y sea $\mathcal R\times\mathcal S$ el anillo producto de la Proposición 29.21.1. Sean

$$
\pi_R:R\times S\to R,
\qquad
\pi_S:R\times S\to S
$$

las funciones coordenadas canónicas de la Definición 29.11.1, aplicada a los grupos aditivos subyacentes.

Entonces $\pi_R$ y $\pi_S$ son homomorfismos de anillos.

#### Demostración {#talg-prf-00147}
Por la proposición «La estructura producto coordenada de dos anillos es un anillo», $\mathcal R\times\mathcal S$ es un anillo. Por la definición «Homomorfismo de anillos», para demostrar que cada proyección es un homomorfismo de anillos debemos verificar preservación de la suma, del producto y de la unidad multiplicativa.

**1. Preservación de la suma.** Como $\mathcal R$ y $\mathcal S$ son anillos, sus estructuras aditivas

$$
\langle R,+_R\rangle,
\qquad
\langle S,+_S\rangle
$$

son grupos. Aplicando la proposición «Homomorfía de las proyecciones canónicas del producto directo de grupos» a estos dos grupos, las mismas funciones coordenadas satisfacen, para cualesquiera $x,y\in R\times S$,

$$
\pi_R(x+_{R\times S}y)
=
\pi_R(x)+_R\pi_R(y),
$$

$$
\pi_S(x+_{R\times S}y)
=
\pi_S(x)+_S\pi_S(y).
$$

Por tanto ambas proyecciones preservan la suma.

**2. Preservación del producto.** Sean

$$
x=\langle r,s\rangle,
\qquad
y=\langle r',s'\rangle
$$

elementos de $R\times S$. Por la definición «Estructura producto coordenada de dos anillos»,

$$
x\cdot_{R\times S}y
=
\langle r\cdot_Rr',\,s\cdot_Ss'\rangle.
$$

Aplicando la primera proyección,

$$
\begin{aligned}
\pi_R(x\cdot_{R\times S}y)
&=\pi_R(\langle r\cdot_Rr',s\cdot_Ss'\rangle)\\
&=r\cdot_Rr'\\
&=\pi_R(x)\cdot_R\pi_R(y).
\end{aligned}
$$

Análogamente,

$$
\begin{aligned}
\pi_S(x\cdot_{R\times S}y)
&=\pi_S(\langle r\cdot_Rr',s\cdot_Ss'\rangle)\\
&=s\cdot_Ss'\\
&=\pi_S(x)\cdot_S\pi_S(y).
\end{aligned}
$$

Así ambas proyecciones preservan el producto.

**3. Preservación de la unidad.** Por la proposición «La estructura producto coordenada de dos anillos es un anillo»,

$$
1_{\mathcal R\times\mathcal S}
=
\langle1_{\mathcal R},1_{\mathcal S}\rangle.
$$

Luego

$$
\pi_R(1_{\mathcal R\times\mathcal S})
=
\pi_R(\langle1_{\mathcal R},1_{\mathcal S}\rangle)
=
1_{\mathcal R},
$$

y

$$
\pi_S(1_{\mathcal R\times\mathcal S})
=
\pi_S(\langle1_{\mathcal R},1_{\mathcal S}\rangle)
=
1_{\mathcal S}.
$$

Por la definición «Homomorfismo de anillos», $\pi_R$ y $\pi_S$ son homomorfismos de anillos. $\square$

> **Lectura estructural.** La parte aditiva no se vuelve a demostrar coordenada por coordenada: ya está contenida en la propiedad correspondiente de las proyecciones del producto de grupos. El caso de anillos añade sólo lo específico del tipo «anillo»: multiplicatividad y preservación explícita de la unidad.

> **Convención unital visible.** Si el tratado usara homomorfismos de anillos no necesariamente unitarios, las dos primeras verificaciones bastarían. Bajo la definición «Homomorfismo de anillos», las ecuaciones sobre $1$ son una obligación real y no pueden omitirse.

> **Frontera del resultado.** Todavía no se ha cerrado la propiedad universal en el tipo de anillos. El siguiente paso debe auditar cómo reutilizar el teorema «Propiedad universal del producto directo de grupos» sobre los grupos aditivos y qué dependencias adicionales son necesarias para promover el mediador a homomorfismo de anillos.

---

## 29.26. Propiedad universal del producto directo de anillos

No es necesario reconstruir el mediador. Los homomorfismos de anillos son, en particular, homomorfismos de los grupos aditivos, de modo que la propiedad universal ya cerrada para grupos proporciona la función subyacente correcta y su unicidad. Sólo resta comprobar que esa misma función preserva la multiplicación y la unidad.

### Teorema 29.26.1 — Propiedad universal del producto directo de anillos {#talg-thm-00020}
Sean

$$
\mathcal T=\langle T,+_T,\cdot_T\rangle,
\qquad
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

anillos, y sean homomorfismos de anillos

$$
f:T\to R,
\qquad
g:T\to S.
$$

Sean

$$
\pi_R:R\times S\to R,
\qquad
\pi_S:R\times S\to S
$$

las proyecciones canónicas, consideradas como homomorfismos de anillos por la Proposición 29.23.1. Entonces existe un **único homomorfismo de anillos**

$$
u:T\to R\times S
$$

tal que

$$
\boxed{\pi_R\circ u=f},
\qquad
\boxed{\pi_S\circ u=g}. \tag{1}
$$

Ese homomorfismo es la función emparejada

$$
\boxed{
u=\langle f,g\rangle,
}
$$

y satisface, para todo $t\in T$,

$$
\boxed{
u(t)=\langle f(t),g(t)\rangle.
} \tag{2}
$$

#### Demostración {#talg-prf-00148}
**1. El mediador aditivo ya existe y es único.** Por la definición «Anillo», los conjuntos subyacentes $T$, $R$ y $S$ llevan grupos aditivos. Como $f$ y $g$ son homomorfismos de anillos, la definición «Homomorfismo de anillos» da, para todos $t,t'\in T$,

$$
f(t+_Tt')=f(t)+_Rf(t'),
$$

$$
g(t+_Tt')=g(t)+_Sg(t').
$$

Por la definición «Homomorfismo de grupos», $f$ y $g$ son por tanto homomorfismos de los grupos aditivos subyacentes.

Aplicamos el teorema «Propiedad universal del producto directo de grupos» a esos tres grupos. Obtenemos un único homomorfismo aditivo

$$
u:T\to R\times S
$$

tal que

$$
\pi_R\circ u=f,
\qquad
\pi_S\circ u=g,
$$

y cuya fórmula puntual es

$$
u(t)=\langle f(t),g(t)\rangle. \tag{3}
$$

La suma del grupo producto utilizada aquí es precisamente $+_{R\times S}$ por la definición «Estructura producto coordenada de dos anillos»; además, la proposición «La estructura producto coordenada de dos anillos es un anillo» certifica que esa estructura aditiva es la del anillo producto.

**2. Multiplicatividad.** Sean $t,t'\in T$. Como $f$ y $g$ son homomorfismos de anillos,

$$
f(t\cdot_Tt')=f(t)\cdot_Rf(t'),
$$

$$
g(t\cdot_Tt')=g(t)\cdot_Sg(t').
$$

Usando (3) y la definición del producto coordenado,

$$
\begin{aligned}
u(t\cdot_Tt')
&=\langle f(t\cdot_Tt'),g(t\cdot_Tt')\rangle\\
&=\langle f(t)\cdot_Rf(t'),\,g(t)\cdot_Sg(t')\rangle\\
&=\langle f(t),g(t)\rangle
  \cdot_{R\times S}
  \langle f(t'),g(t')\rangle\\
&=u(t)\cdot_{R\times S}u(t').
\end{aligned}
$$

Luego $u$ preserva la multiplicación.

**3. Preservación de la unidad.** Por la convención unital de la definición «Homomorfismo de anillos»,

$$
f(1_{\mathcal T})=1_{\mathcal R},
\qquad
g(1_{\mathcal T})=1_{\mathcal S}.
$$

Entonces, nuevamente por (3),

$$
\begin{aligned}
u(1_{\mathcal T})
&=\langle f(1_{\mathcal T}),g(1_{\mathcal T})\rangle\\
&=\langle1_{\mathcal R},1_{\mathcal S}\rangle\\
&=1_{\mathcal R\times\mathcal S},
\end{aligned}
$$

donde la última igualdad es la fórmula de la unidad del anillo producto demostrada en la proposición «La estructura producto coordenada de dos anillos es un anillo».

La aditividad de $u$ ya fue obtenida de el teorema «Propiedad universal del producto directo de grupos». Junto con la multiplicatividad y la preservación de la unidad recién demostradas, la definición «Homomorfismo de anillos» implica que

$$
u:T\to R\times S
$$

es un homomorfismo de anillos. Esto prueba la existencia requerida en (1).

**4. Unicidad en el tipo de anillos.** Sea

$$
v:T\to R\times S
$$

un homomorfismo de anillos que también satisfaga

$$
\pi_R\circ v=f,
\qquad
\pi_S\circ v=g. \tag{4}
$$

Como $v$ preserva la suma por la definición «Homomorfismo de anillos», la definición «Homomorfismo de grupos» permite considerarlo como homomorfismo de los grupos aditivos subyacentes. Las ecuaciones (4) son exactamente las mismas ecuaciones universales usadas en el teorema «Propiedad universal del producto directo de grupos». Por la unicidad allí demostrada,

$$
v=u.
$$

Por tanto existe un único homomorfismo de anillos con las dos proyecciones prescritas. $\square$

> **Lectura estructural.** El caso de anillos no necesita una nueva construcción conjuntista: el objeto universal de los anillos tiene la misma función mediadora que el producto de los grupos aditivos. El contenido nuevo consiste en comprobar que esa función respeta la estructura multiplicativa adicional y la unidad.

> **Unicidad heredada.** La unicidad usada aquí es más fuerte de lo estrictamente necesario: el teorema «Propiedad universal del producto directo de grupos» ya determina el mediador entre todos los homomorfismos aditivos con esas proyecciones. La subclase de homomorfismos de anillos no puede contener un segundo mediador distinto.

> **Frontera conceptual.** No se usa ninguna teoría categórica general. La universalidad se demuestra dentro de la infraestructura concreta de funciones, grupos y anillos ya construida en el tratado.

---

## 29.29. Propiedad universal del cociente de grupos

Comenzamos por grupos, donde el principio de factorización puede expresarse como un criterio exacto: un homomorfismo desciende al cociente por $N$ exactamente cuando anula a $N$.

### Teorema 29.29.1 — Propiedad universal del cociente de grupos {#talg-thm-00021}
Sean

$$
\mathcal G=\langle G,\star\rangle,
\qquad
\mathcal H=\langle H,\diamond\rangle
$$

grupos, sea

$$
N\trianglelefteq G,
$$

y sea

$$
f:G\to H
$$

un homomorfismo de grupos. Sea

$$
q_N:G\to G/N
$$

la proyección canónica del grupo cociente.

Entonces son equivalentes:

1. 
   $$
   \boxed{N\subseteq\ker f};
   $$
2. existe un **único homomorfismo de grupos**
   $$
   \overline f:G/N\to H
   $$
   tal que
   $$
   \boxed{\overline f\circ q_N=f}. \tag{1}
   $$

Cuando estas condiciones se cumplen, el homomorfismo inducido está determinado por

$$
\boxed{
\overline f(gN)=f(g)
}
\qquad(g\in G). \tag{2}
$$

#### Demostración {#talg-prf-00149}
Supongamos primero

$$
N\subseteq\ker f. \tag{3}
$$

**1. Invariancia respecto de representantes.** Si

$$
gN=hN,
$$

entonces el teorema «Criterios de igualdad de clases laterales» da

$$
h^{-1}\star g\in N.
$$

Por (3),

$$
h^{-1}\star g\in\ker f,
$$

y por la definición de núcleo,

$$
f(h^{-1}\star g)
$$

es el neutro de $\mathcal H$. Como $f$ es homomorfismo y preserva inversos por la proposición «Preservación de inversos por homomorfismos de grupos»,

$$
f(h)^{-1}\diamond f(g)
$$

es el neutro de $\mathcal H$. Multiplicando a la izquierda por $f(h)$ y usando las leyes de grupo en $\mathcal H$, obtenemos

$$
f(g)=f(h). \tag{4}
$$

Por tanto, la regla $gN\mapsto f(g)$ no depende del representante.

**2. Construcción de la función inducida.** Consideremos

$$
\Gamma_{\overline f}
:=
\left\{
\langle C,y\rangle\in(G/N)\times H:
\exists g\in G\,
\bigl(C=q_N(g)\land y=f(g)\bigr)
\right\}. \tag{5}
$$

El conjunto existe por producto cartesiano y Separación.

Sea $C\in G/N$. Por la proposición «La proyección canónica es sobreyectiva, homomórfica y tiene núcleo N», $q_N$ es sobreyectiva, así que existe $g\in G$ tal que

$$
C=q_N(g).
$$

Entonces

$$
\langle C,f(g)\rangle\in\Gamma_{\overline f},
$$

de modo que el grafo es total.

Para la funcionalidad, supongamos que

$$
\langle C,y\rangle,
\langle C,z\rangle
\in\Gamma_{\overline f}.
$$

Existen $g,h\in G$ tales que

$$
C=q_N(g)=q_N(h),
\qquad
y=f(g),
\qquad
z=f(h).
$$

Por la definición «Proyección canónica q_N:G\to G/N»,

$$
q_N(g)=gN,
\qquad
q_N(h)=hN,
$$

y por tanto

$$
gN=hN.
$$

La invariancia (4) da $f(g)=f(h)$, luego $y=z$. Así, (5) es el grafo de una función

$$
\overline f:G/N\to H
$$

que satisface exactamente

$$
\overline f(gN)=f(g). \tag{6}
$$

No se ha elegido simultáneamente un representante para cada clase: la sobreyectividad sólo se elimina localmente para el argumento que se está tratando.

**3. Homomorfía y factorización.** Sean $C,D\in G/N$. Por la sobreyectividad de $q_N$, existen $g,h\in G$ con

$$
C=gN,
\qquad
D=hN.
$$

Usando la operación cociente de la notación «Operación cociente \star_N»,

$$
\begin{aligned}
\overline f(C\star_N D)
&=\overline f\bigl((gN)\star_N(hN)\bigr)\\
&=\overline f((g\star h)N)\\
&=f(g\star h)\\
&=f(g)\diamond f(h)\\
&=\overline f(C)\diamond\overline f(D).
\end{aligned}
$$

Por la definición «Homomorfismo de grupos», $\overline f$ es un homomorfismo de grupos.

Además, para todo $g\in G$,

$$
\begin{aligned}
(\overline f\circ q_N)(g)
&=\overline f(q_N(g))\\
&=\overline f(gN)\\
&=f(g).
\end{aligned}
$$

Por extensionalidad funcional,

$$
\overline f\circ q_N=f. \tag{7}
$$

**4. Unicidad.** Sea

$$
u:G/N\to H
$$

un homomorfismo de grupos que satisfaga también

$$
u\circ q_N=f. \tag{8}
$$

Sea $C\in G/N$. Por sobreyectividad de $q_N$, existe $g\in G$ con $C=q_N(g)$. Entonces

$$
\begin{aligned}
u(C)
&=u(q_N(g))\\
&=(u\circ q_N)(g)\\
&=f(g)\\
&=(\overline f\circ q_N)(g)\\
&=\overline f(C).
\end{aligned}
$$

Como $C$ era arbitrario, la extensionalidad funcional da

$$
u=\overline f.
$$

Obsérvese que este argumento de unicidad usa solamente la sobreyectividad de $q_N$ y la ecuación de factorización; no necesita la homomorfía de $u$.

Hemos probado la implicación

$$
N\subseteq\ker f
\Longrightarrow
\exists!\,\overline f:G/N\to H
\text{ homomorfismo con }
\overline f\circ q_N=f. \tag{9}
$$

Supongamos ahora, recíprocamente, que existe un homomorfismo

$$
\overline f:G/N\to H
$$

tal que

$$
\overline f\circ q_N=f. \tag{10}
$$

No necesitamos usar aquí su unicidad.

**5. Necesidad de la inclusión en el núcleo.** Sea $n\in N$. Por la proposición «La proyección canónica es sobreyectiva, homomórfica y tiene núcleo N»,

$$
N=\ker q_N,
$$

de modo que $n\in\ker q_N$. Por la definición de núcleo, $q_N(n)$ es el neutro del grupo cociente. Como $\overline f$ es un homomorfismo de grupos, la proposición «Preservación del neutro por homomorfismos de grupos» implica que $\overline f(q_N(n))$ es el neutro de $\mathcal H$. Usando (10),

$$
f(n)
=
(\overline f\circ q_N)(n)
=
\overline f(q_N(n)),
$$

por lo que $f(n)$ es el neutro de $\mathcal H$. Por la definición de $\ker f$,

$$
n\in\ker f.
$$

Como $n\in N$ era arbitrario,

$$
N\subseteq\ker f. \tag{11}
$$

Las dos implicaciones (9) y (11) prueban la equivalencia. $\square$

> **Lectura estructural.** La proyección $q_N$ es universal entre los homomorfismos de grupos que anulan $N$: toda esa información desciende de manera única al cociente.

> **Sin elección de representantes.** La función inducida se construye por su grafo. Los representantes se eliminan sólo localmente mediante la sobreyectividad de $q_N$, y la invariancia (4) garantiza que el valor no depende del representante elegido.

> **Fortaleza del criterio.** En la dirección necesaria basta la existencia de una factorización homomórfica; su unicidad no interviene. En la dirección suficiente, la unicidad del factor incluso vale entre todas las funciones $G/N\to H$ que satisfacen la ecuación de factorización.

---

## 29.32. Propiedad universal del cociente de anillos

En el caso de anillos, Al igual que en grupos, la condición correcta no es cocientar necesariamente por todo el núcleo, sino por cualquier ideal bilateral que el homomorfismo anule. La diferencia estructural es que el factor inducido debe preservar simultáneamente suma, producto y unidad.

### Teorema 29.32.1 — Propiedad universal del cociente de anillos {#talg-thm-00022}
Sean

$$
\mathcal R=\langle R,+_R,\cdot_R\rangle,
\qquad
\mathcal S=\langle S,+_S,\cdot_S\rangle
$$

anillos, sea $I$ un ideal bilateral de $R$ y sea

$$
f:R\to S
$$

un homomorfismo de anillos. Sea

$$
q_I:R\to R/I
$$

la proyección canónica del anillo cociente.

Entonces son equivalentes:

1. 
   $$
   \boxed{I\subseteq\ker f};
   $$
2. existe un **único homomorfismo de anillos**
   $$
   \overline f:R/I\to S
   $$
   tal que
   $$
   \boxed{\overline f\circ q_I=f}. \tag{1}
   $$

Cuando estas condiciones se cumplen, el homomorfismo inducido está determinado por

$$
\boxed{
\overline f([a]_I)=f(a)
}
\qquad(a\in R). \tag{2}
$$

#### Demostración {#talg-prf-00150}
Supongamos primero

$$
I\subseteq\ker f. \tag{3}
$$

**1. Invariancia respecto de representantes.** Supongamos

$$
[a]_I=[b]_I.
$$

Por la proposición «Criterio de igualdad de clases módulo I»,

$$
a-b\in I.
$$

La inclusión (3) implica

$$
a-b\in\ker f,
$$

por lo que, según la definición del núcleo,

$$
f(a-b)=0_{\mathcal S}. \tag{4}
$$

Como $f$ preserva la suma por la definición «Homomorfismo de anillos» y los opuestos aditivos por la proposición «Preservación del cero y de los opuestos aditivos»,

$$
\begin{aligned}
f(a-b)
&=f(a+(-b))\\
&=f(a)+_S f(-b)\\
&=f(a)+_S(-f(b)).
\end{aligned} \tag{5}
$$

De (4) y (5),

$$
f(a)+_S(-f(b))=0_{\mathcal S}.
$$

En el grupo aditivo de $\mathcal S$,

$$
\begin{aligned}
f(a)
&=f(a)+_S0_{\mathcal S}\\
&=f(a)+_S\bigl((-f(b))+_Sf(b)\bigr)\\
&=\bigl(f(a)+_S(-f(b))\bigr)+_Sf(b)\\
&=0_{\mathcal S}+_Sf(b)\\
&=f(b).
\end{aligned}
$$

Así,

$$
\boxed{[a]_I=[b]_I\Longrightarrow f(a)=f(b)}. \tag{6}
$$

**2. Construcción de la función inducida.** Consideremos

$$
\Gamma_{\overline f}
:=
\left\{
\langle C,y\rangle\in(R/I)\times S:
\exists a\in R\,
\bigl(C=q_I(a)\land y=f(a)\bigr)
\right\}. \tag{7}
$$

El ambiente cartesiano existe por la infraestructura funcional y el subconjunto (7) existe por Separación.

Sea $C\in R/I$. Por la proposición «La proyección canónica es sobreyectiva, homomórfica y tiene núcleo I», $q_I$ es sobreyectiva, así que existe $a\in R$ tal que

$$
C=q_I(a).
$$

Entonces

$$
\langle C,f(a)\rangle\in\Gamma_{\overline f},
$$

por lo que el grafo es total.

Para la funcionalidad, supongamos

$$
\langle C,y\rangle,
\langle C,z\rangle
\in\Gamma_{\overline f}.
$$

Existen $a,b\in R$ tales que

$$
C=q_I(a)=q_I(b),
\qquad
y=f(a),
\qquad
z=f(b).
$$

Por la definición «Proyección canónica al cociente»,

$$
q_I(a)=[a]_I,
\qquad
q_I(b)=[b]_I,
$$

luego $[a]_I=[b]_I$. La invariancia (6) da $f(a)=f(b)$ y por tanto $y=z$. Así, (7) es el grafo de una función

$$
\overline f:R/I\to S
$$

que satisface precisamente

$$
\overline f([a]_I)=f(a). \tag{8}
$$

No se ha elegido simultáneamente un representante de cada clase; la sobreyectividad se usa sólo localmente para cada argumento y la invariancia (6) elimina la dependencia del representante.

**3. El factor es un homomorfismo de anillos.** Sean $C,D\in R/I$. Por la sobreyectividad de $q_I$, existen $a,b\in R$ tales que

$$
C=[a]_I,
\qquad
D=[b]_I.
$$

Usando las operaciones cociente de la notación «Operaciones cociente +_I y \cdot_I»,

$$
\begin{aligned}
\overline f(C+_I D)
&=\overline f([a+b]_I)\\
&=f(a+b)\\
&=f(a)+_Sf(b)\\
&=\overline f(C)+_S\overline f(D),
\end{aligned} \tag{9}
$$

y

$$
\begin{aligned}
\overline f(C\cdot_I D)
&=\overline f([ab]_I)\\
&=f(ab)\\
&=f(a)\cdot_Sf(b)\\
&=\overline f(C)\cdot_S\overline f(D).
\end{aligned} \tag{10}
$$

Por el teorema «El cociente por un ideal bilateral es un anillo»,

$$
1_{\mathcal R/I}=[1_{\mathcal R}]_I.
$$

Como $f$ es un homomorfismo de anillos,

$$
\begin{aligned}
\overline f(1_{\mathcal R/I})
&=\overline f([1_{\mathcal R}]_I)\\
&=f(1_{\mathcal R})\\
&=1_{\mathcal S}.
\end{aligned} \tag{11}
$$

Las ecuaciones (9), (10) y (11) son exactamente las condiciones de la definición «Homomorfismo de anillos». Por tanto,

$$
\overline f:R/I\to S
$$

es un homomorfismo de anillos.

**4. Ecuación de factorización.** Para todo $a\in R$,

$$
\begin{aligned}
(\overline f\circ q_I)(a)
&=\overline f(q_I(a))\\
&=\overline f([a]_I)\\
&=f(a).
\end{aligned}
$$

Por extensionalidad funcional,

$$
\overline f\circ q_I=f. \tag{12}
$$

**5. Unicidad.** Sea

$$
u:R/I\to S
$$

un homomorfismo de anillos que satisfaga también

$$
u\circ q_I=f. \tag{13}
$$

Sea $C\in R/I$. Por sobreyectividad de $q_I$, existe $a\in R$ con $C=q_I(a)$. Entonces

$$
\begin{aligned}
u(C)
&=u(q_I(a))\\
&=(u\circ q_I)(a)\\
&=f(a)\\
&=(\overline f\circ q_I)(a)\\
&=\overline f(C).
\end{aligned}
$$

Como $C$ era arbitrario, la extensionalidad funcional da

$$
u=\overline f.
$$

Este argumento utiliza sólo la sobreyectividad de $q_I$ y la ecuación de factorización; de hecho, la unicidad vale entre todas las funciones $R/I\to S$ que satisfacen (13).

Hemos probado

$$
I\subseteq\ker f
\Longrightarrow
\exists!\,\overline f:R/I\to S
\text{ homomorfismo de anillos con }
\overline f\circ q_I=f. \tag{14}
$$

Supongamos ahora, recíprocamente, que existe un homomorfismo de anillos

$$
\overline f:R/I\to S
$$

tal que

$$
\overline f\circ q_I=f. \tag{15}
$$

No necesitamos usar aquí su unicidad.

**6. Necesidad de la inclusión en el núcleo.** Sea $a\in I$. Por la proposición «La proyección canónica es sobreyectiva, homomórfica y tiene núcleo I»,

$$
I=\ker q_I,
$$

de modo que

$$
q_I(a)=0_{\mathcal R/I}.
$$

Como $\overline f$ es un homomorfismo de anillos, la proposición «Preservación del cero y de los opuestos aditivos» da

$$
\overline f(0_{\mathcal R/I})=0_{\mathcal S}.
$$

Usando (15),

$$
\begin{aligned}
f(a)
&=(\overline f\circ q_I)(a)\\
&=\overline f(q_I(a))\\
&=\overline f(0_{\mathcal R/I})\\
&=0_{\mathcal S}.
\end{aligned}
$$

Por la definición de $\ker f$,

$$
a\in\ker f.
$$

Como $a\in I$ era arbitrario,

$$
I\subseteq\ker f. \tag{16}
$$

Las implicaciones (14) y (16) prueban la equivalencia. $\square$

> **Lectura estructural.** La proyección $q_I$ es universal entre los homomorfismos de anillos que anulan el ideal $I$: toda la información compatible con esa identificación desciende de manera única a $R/I$.

> **Sin elección de representantes.** El factor se construye por su grafo; los representantes se usan sólo localmente. La igualdad de clases y la condición $I\subseteq\ker f$ garantizan que todos producen el mismo valor.

> **Fortaleza del criterio.** Para la dirección necesaria basta la existencia de una factorización homomórfica; la unicidad no interviene. En la dirección suficiente, la unicidad del factor incluso vale entre todas las funciones que satisfacen la ecuación de factorización.

---

## 29.35. Propiedad universal del cuerpo de fracciones

La hipótesis exacta que permite extender un homomorfismo desde un dominio íntegro hacia un cuerpo es: los denominadores no nulos del dominio deben conservar imagen no nula. En el tratado esto se garantiza suponiendo que el homomorfismo de anillos de partida es inyectivo.

### Teorema 29.35.1 — Propiedad universal del cuerpo de fracciones {#talg-thm-00023}
Sea

$$
\mathcal D=\langle D,+_D,\cdot_D\rangle
$$

un dominio íntegro, sea

$$
\mathcal K=\langle K,+_K,\cdot_K\rangle
$$

un cuerpo y sea

$$
f:D\to K
$$

un homomorfismo de anillos **inyectivo**. Sea

$$
\iota_D:D\to\operatorname{Frac}(D),
\qquad
\iota_D(a)=\frac a1,
$$

la inmersión canónica.

Entonces existe un **único homomorfismo de cuerpos**

$$
\widetilde f:\operatorname{Frac}(D)\to K
$$

tal que

$$
\boxed{
\widetilde f\circ\iota_D=f.
} \tag{1}
$$

Para toda fracción $a/b$ con $b\neq0$, dicho homomorfismo viene dado por

$$
\boxed{
\widetilde f\!\left(\frac ab\right)
=
f(a)f(b)^{-1}.
} \tag{2}
$$

#### Demostración {#talg-prf-00151}
**1. Las imágenes de los denominadores son no nulas e invertibles.** Sea $b\in D$ con $b\neq0$. Afirmamos que

$$
f(b)\neq0_{\mathcal K}. \tag{3}
$$

En efecto, si $f(b)=0_{\mathcal K}$, la preservación de cero de la proposición «Preservación del cero y de los opuestos aditivos» da

$$
f(b)=f(0_{\mathcal D}).
$$

Como $f$ es inyectiva, se seguiría $b=0_{\mathcal D}$, contradicción. Por tanto (3) vale.

Como $\mathcal K$ es un cuerpo, la definición «Cuerpo» asegura que todo elemento no nulo es una unidad. En consecuencia $f(b)$ posee un inverso multiplicativo único, denotado

$$
f(b)^{-1}
$$

por la notación «Inverso multiplicativo de una unidad y conjunto R^\times». Así la expresión del miembro derecho de (2) está bien tipada para todo denominador admisible.

**2. Independencia del representante.** Supongamos

$$
\frac ab=\frac cd,
\qquad
b\neq0,
\qquad
d\neq0.
$$

Por la proposición «Criterio exacto de igualdad de fracciones»,

$$
ad=bc. \tag{4}
$$

Aplicando el homomorfismo $f$ y usando la definición «Homomorfismo de anillos»,

$$
f(a)f(d)=f(b)f(c). \tag{5}
$$

Por el paso anterior, $f(b)$ y $f(d)$ son no nulos y, por tanto, invertibles en $K$. Multipliquemos ambos miembros de (5) por

$$
f(b)^{-1}f(d)^{-1}.
$$

Como $K$ es conmutativo por la definición «Cuerpo», y usando asociatividad, neutro e identidades de inverso,

$$
\begin{aligned}
f(a)f(d)f(b)^{-1}f(d)^{-1}
&=f(a)f(b)^{-1},\\
f(b)f(c)f(b)^{-1}f(d)^{-1}
&=f(c)f(d)^{-1}.
\end{aligned}
$$

Por tanto

$$
\boxed{
f(a)f(b)^{-1}=f(c)f(d)^{-1}.
} \tag{6}
$$

La regla de (2) no depende del representante de la clase fraccionaria.

**3. Construcción de la función inducida.** Consideremos el subconjunto

$$
\Gamma_{\widetilde f}
:=
\left\{
\langle x,y\rangle\in\operatorname{Frac}(D)\times K:
\begin{array}{l}
\exists a,b\in D\;\bigl(
 b\neq0\land x=a/b\\
\hspace{7em}\land y=f(a)f(b)^{-1}
\bigr)
\end{array}
\right\}. \tag{7}
$$

El conjunto existe por producto cartesiano y Separación, mediante la interfaz «Pares, productos y funciones desde TA-0003».

Sea $x\in\operatorname{Frac}(D)$. Por la construcción del cociente expresada en la notación «Notación de fracciones y del conjunto cociente», existe localmente un par fraccionario $\langle a,b\rangle$ con $b\neq0$ tal que

$$
x=\frac ab.
$$

Entonces el paso 1 proporciona $f(b)^{-1}$ y

$$
\left\langle x,f(a)f(b)^{-1}\right\rangle
\in\Gamma_{\widetilde f}.
$$

Así el grafo es total. Si dos pares fraccionarios representan el mismo $x$, el paso 2 muestra que producen el mismo valor en $K$. Por tanto el grafo es funcional y determina una función

$$
\widetilde f:\operatorname{Frac}(D)\to K
$$

que satisface (2).

No se ha elegido una familia global de representantes: para cada argumento fijo sólo se elimina la existencia local de algún representante y la invariancia (6) garantiza que el valor resultante es único.

**4. $\widetilde f$ es un homomorfismo de cuerpos.** Sean

$$
x=\frac ab,
\qquad
y=\frac cd,
$$

con $b,d\neq0$. Por la notación «Notación de las operaciones fraccionarias»,

$$
x+y=\frac{ad+bc}{bd}.
$$

La estructura de dominio íntegro de $D$ garantiza $bd\neq0$, por lo que el denominador sigue siendo admisible. Entonces

$$
\begin{aligned}
\widetilde f(x+y)
&=f(ad+bc)f(bd)^{-1}\\
&=\bigl(f(a)f(d)+f(b)f(c)\bigr)
  \bigl(f(b)f(d)\bigr)^{-1}.
\end{aligned}
$$

Por la proposición «Identidad, producto e inverso de unidades», el inverso de un producto de unidades es el producto de los inversos en orden inverso. Como $K$ es conmutativo,

$$
\bigl(f(b)f(d)\bigr)^{-1}
=f(d)^{-1}f(b)^{-1}
=f(b)^{-1}f(d)^{-1}.
$$

Distribuyendo y reordenando dentro del cuerpo $K$,

$$
\begin{aligned}
\widetilde f(x+y)
&=f(a)f(b)^{-1}+f(c)f(d)^{-1}\\
&=\widetilde f(x)+\widetilde f(y).
\end{aligned} \tag{8}
$$

Para el producto, nuevamente por la notación «Notación de las operaciones fraccionarias»,

$$
xy=\frac{ac}{bd},
$$

y el mismo cálculo del inverso del producto da

$$
\begin{aligned}
\widetilde f(xy)
&=f(ac)f(bd)^{-1}\\
&=f(a)f(c)\,f(b)^{-1}f(d)^{-1}\\
&=\bigl(f(a)f(b)^{-1}\bigr)
  \bigl(f(c)f(d)^{-1}\bigr)\\
&=\widetilde f(x)\widetilde f(y).
\end{aligned} \tag{9}
$$

Finalmente, el teorema «El cuerpo de fracciones de un dominio íntegro» fija

$$
1_{\mathcal F_D}=\frac11.
$$

Por la preservación unital de $f$ y la identidad de inverso de la unidad incluida en la proposición «Identidad, producto e inverso de unidades»,

$$
\begin{aligned}
\widetilde f(1_{\mathcal F_D})
&=f(1_D)f(1_D)^{-1}\\
&=1_K.
\end{aligned} \tag{10}
$$

Las ecuaciones (8)–(10) son exactamente las condiciones de la definición «Homomorfismo de anillos»; por tanto $\widetilde f$ es un homomorfismo de anillos. Como el teorema «El cuerpo de fracciones de un dominio íntegro» certifica que $\mathcal F_D$ es un cuerpo y $\mathcal K$ es un cuerpo por hipótesis, la definición «Homomorfismo de cuerpos» identifica el mismo mapa como un homomorfismo de cuerpos.

**5. La extensión coincide con $f$ sobre $D$.** Sea $a\in D$. Por la definición «Inmersión canónica en el cuerpo de fracciones»,

$$
\iota_D(a)=\frac a1.
$$

Entonces

$$
\begin{aligned}
(\widetilde f\circ\iota_D)(a)
&=\widetilde f\!\left(\frac a1\right)\\
&=f(a)f(1_D)^{-1}\\
&=f(a).
\end{aligned}
$$

Por extensionalidad funcional,

$$
\widetilde f\circ\iota_D=f. \tag{11}
$$

La Proposición la proposición «La inmersión canónica es un homomorfismo unital inyectivo» certifica, además, que $\iota_D$ es efectivamente un homomorfismo unital inyectivo: (11) es por tanto una extensión a través de la inmersión canónica ya cerrada del dominio en su cuerpo de fracciones.

**6. Unicidad.** Sea

$$
u:\operatorname{Frac}(D)\to K
$$

un homomorfismo de cuerpos que satisfaga también

$$
u\circ\iota_D=f. \tag{12}
$$

Sea $x\in\operatorname{Frac}(D)$. Elijamos sólo localmente un representante

$$
x=\frac ab,
\qquad b\neq0.
$$

Por las operaciones fraccionarias de la notación «Notación de las operaciones fraccionarias»,

$$
\frac ab\cdot\frac b1
=
\frac{ab}{b}.
$$

El criterio la proposición «Criterio exacto de igualdad de fracciones» da

$$
\frac{ab}{b}=\frac a1,
$$

pues $(ab)\cdot1=a\cdot b$. Por tanto

$$
\frac ab\cdot\frac b1=\frac a1. \tag{13}
$$

Como $u$ es un homomorfismo de cuerpos, la definición «Homomorfismo de cuerpos» y la definición «Homomorfismo de anillos» dan preservación del producto. Aplicando $u$ a (13) y usando (12) junto con la definición «Inmersión canónica en el cuerpo de fracciones»,

$$
 u\!\left(\frac ab\right)f(b)=f(a). \tag{14}
$$

Por el paso 1, $f(b)\neq0$ y, al estar en un cuerpo, posee inverso. Multiplicando (14) por $f(b)^{-1}$,

$$
 u\!\left(\frac ab\right)
=f(a)f(b)^{-1}
=\widetilde f\!\left(\frac ab\right).
$$

Como todo elemento de $\operatorname{Frac}(D)$ admite un representante local, $u$ y $\widetilde f$ coinciden punto a punto. Por extensionalidad funcional,

$$
u=\widetilde f.
$$

La existencia y la unicidad quedan demostradas. $\square$

> **Lectura estructural.** El cuerpo de fracciones es el cuerpo generado universalmente por $D$ al hacer invertibles todos sus elementos no nulos: cualquier inmersión de $D$ en un cuerpo determina una única extensión al cuerpo de fracciones.

> **Frontera lógica.** El teorema no añade Choice ni un nuevo principio clásico sustantivo. Usa como objeto dado el cuerpo de fracciones ya construido y auditado en el Capítulo 24; el único DNE sustantivo de esa construcción permanece localizado en el resultado previo que estableció la equivalencia fraccionaria clásica.

> **Sin teoría abstracta de localización.** La universalidad se demuestra directamente con clases fraccionarias, inversos en el cuerpo destino y extensionalidad funcional. No se introduce una maquinaria general de localizaciones.

---

## 29.37. Síntesis estructural de 6.1

Los resultados anteriores permiten leer conjuntamente tres construcciones que, aunque se presentan con fórmulas distintas, comparten un mismo patrón de **existencia y unicidad de un morfismo determinado por datos canónicos**.

### 29.37.1. Productos: mediadores hacia una estructura coordinada

Para grupos y anillos, el producto directo recibe un único morfismo desde cualquier objeto con dos morfismos hacia los factores. En grupos,

$$
\langle f,g\rangle(k)=\langle f(k),g(k)\rangle,
$$

con

$$
\pi_G\circ\langle f,g\rangle=f,\qquad
\pi_H\circ\langle f,g\rangle=g.
$$

En anillos se reutiliza exactamente la misma función subyacente sobre los grupos aditivos y se verifica además que preserve producto y unidad. El paso de grupos a anillos no requiere una nueva construcción conjuntista.

### 29.37.2. Cocientes: factorización de morfismos que anulan el subobjeto

Las proyecciones canónicas de grupos y anillos satisfacen el principio paralelo

$$
N\subseteq\ker f
\Longleftrightarrow
\exists!\,\overline f:G/N\to H\text{ con }\overline f\circ q_N=f,
$$

$$
I\subseteq\ker f
\Longleftrightarrow
\exists!\,\overline f:R/I\to S\text{ con }\overline f\circ q_I=f.
$$

En ambos casos el morfismo inducido se construye por su grafo, sin seleccionar globalmente representantes. La sobreyectividad de la proyección canónica es la razón exacta de la unicidad.

### 29.37.3. Cuerpo de fracciones: extensión por inversión de denominadores

Si $D$ es un dominio íntegro, $K$ un cuerpo y

$$
f:D\hookrightarrow K
$$

es un homomorfismo de anillos inyectivo, existe un único homomorfismo de cuerpos

$$
\widetilde f:\operatorname{Frac}(D)\to K
$$

con

$$
\widetilde f\circ\iota_D=f,
$$

dado por

$$
\widetilde f\!\left(\frac ab\right)=f(a)f(b)^{-1}.
$$

La inyectividad es la condición que garantiza que la imagen de todo denominador no nulo siga siendo no nula y, por tanto, invertible en el cuerpo destino.

### 29.37.4. Patrón común y frontera del capítulo

Los resultados anteriores no introducen una teoría categórica general. El capítulo mantiene todas las propiedades universales en el lenguaje concreto ya construido por el tratado:

1. datos algebraicos bien tipados;
2. una función candidata dada por fórmula explícita o por un grafo funcional;
3. prueba de buena definición cuando hay representantes;
4. verificación del tipo de homomorfismo correspondiente;
5. ecuaciones de mediación o factorización;
6. unicidad por coordenadas, sobreyectividad o inversión de denominadores.

Este nivel es suficiente para que las unidades 6.2 y 6.3 reutilicen los principios universales como herramientas de construcción, sin tener que volver a demostrarlos desde cero.

---

---

[← **Capítulo 28 — Propiedades arquimedianas**](tratado-de-algebra-capitulo-28-propiedades-arquimedianas.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md) · [**Capítulo 30 — Teoremas de isomorfía superiores y correspondencia** →](tratado-de-algebra-capitulo-30-teoremas-de-isomorfia-superiores-y-correspondencia.md)
