---
title: 'Tratado moderno de Álgebra — Capítulo 31: Descenso y transporte de estructura'
description: Capítulo del Tratado moderno de Álgebra dedicado al descenso de homomorfismos entre cocientes y al transporte de subestructuras mediante isomorfismos.
author: Gustav A. Tachek
content-id: MA-BCH-0139
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
- homomorfismos
- cocientes
- isomorfismos
- transporte-de-estructura
- grupos
- anillos
prerequisites:
- MA-BCH-0138
related:
- MA-BOK-0007
- MA-BCH-0138
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Capítulo 31 — Descenso y transporte de estructura

## 31.0. Propósito y posición deductiva

Los capítulos 29 y 30 establecieron las propiedades universales de los cocientes, los teoremas de isomorfía superiores y las correspondencias de subestructuras sobre cocientes. Este capítulo sistematiza el paso de un homomorfismo compatible con los subgrupos normales o ideales elegidos a un homomorfismo inducido entre sus cocientes.

El desarrollo comprende cuatro aspectos:

1. descenso general de homomorfismos entre cocientes;
2. compatibilidad del descenso con identidad y composición;
3. criterios de inyectividad, sobreyectividad e isomorfía del morfismo inducido;
4. transporte de subestructuras, normalidad e ideales bajo isomorfismos.

Los resultados se formulan en el lenguaje concreto de grupos y anillos del tratado. Los anillos y sus homomorfismos conservan la convención unital; los ideales son bilaterales.

El marco fundacional es ZF con lógica clásica. Las pruebas de este capítulo utilizan representantes y testigos sólo localmente, sin el axioma de elección. No presuponen decidibilidad de igualdad o pertenencia ni afirman algoritmos.

---

## 31.9. Descenso de homomorfismos de grupos entre cocientes

### Teorema 31.9.1 — Descenso de homomorfismos de grupos entre cocientes {#talg-thm-00030}

Sean $f:G\to H$ un homomorfismo de grupos, $N\trianglelefteq G$ y $M\trianglelefteq H$. Si $f(n)\in M$ para todo $n\in N$, existe un único homomorfismo
$$
\overline f:G/N\longrightarrow H/M
$$
tal que
$$
\overline f\circ q_N=q_M\circ f.
$$
Está determinado por $\overline f(gN)=f(g)M$ para cada $g\in G$. Recíprocamente, la existencia de un homomorfismo con esa identidad implica $f(n)\in M$ para todo $n\in N$.

#### Demostración {#talg-prf-00161}

**Hipótesis y objetivo.** Las normalidades permiten formar ambos cocientes y sus proyecciones; la compatibilidad $f(N)\subseteq M$ se usa para anular $N$ en el codominio cociente. Se busca existencia y unicidad con la identidad indicada.

**Existencia.** Las proyecciones son homomorfismos sobreyectivos por la [Proposición 12.5.2](tratado-de-algebra-capitulo-12-cocientes-de-grupos.md#talg-pro-00023). La [composición de homomorfismos](tratado-de-algebra-capitulo-7-homomorfismos-de-magmas-monoides-y-grupos.md#talg-pro-00006) preserva las operaciones, luego $u=q_M\circ f:G\to H/M$ es un homomorfismo. Si $n\in N$, por hipótesis $f(n)\in M=\ker q_M$, de donde $u(n)=e_{H/M}$. Así $N\subseteq\ker u$. El [Teorema 29.29.1](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md#talg-thm-00021) proporciona un único homomorfismo $\overline f:G/N\to H/M$ con $\overline f\circ q_N=u$. Al evaluar en $g$,
$$
\overline f(gN)=\overline f(q_N(g))=u(g)=q_M(f(g))=f(g)M.
$$
La buena definición de esta regla está incluida en la propiedad universal: no se ha seleccionado un representante para cada clase.

**Unicidad.** Si $v:G/N\to H/M$ es otro homomorfismo con $v\circ q_N=u$, para cualquier clase $C\in G/N$ la sobreyectividad de $q_N$ proporciona localmente $g\in G$ con $C=q_N(g)$. Entonces
$$
v(C)=v(q_N(g))=u(g)=\overline f(q_N(g))=\overline f(C).
$$
La extensionalidad funcional da $v=\overline f$.

**Necesidad.** Si existe tal homomorfismo y $n\in N$, entonces $q_N(n)=e_{G/N}=q_N(e_G)$. Por la identidad conmutativa y $f(e_G)=e_H$,
$$
q_M(f(n))=\overline f(q_N(n))
=\overline f(q_N(e_G))=q_M(f(e_G))=q_M(e_H)=e_{H/M}.
$$
La preservación de neutro usada aquí forma parte de la infraestructura del homomorfismo de grupos heredada por el [Teorema 29.29.1](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md#talg-thm-00021). Como $\ker q_M=M$, se obtiene $f(n)\in M$. Esto concluye ambas direcciones. $\square$

La existencia de representantes se utiliza sólo localmente. No hay elección de una sección de $q_N$, no se presupone decidibilidad de igualdad o pertenencia y no se afirma un algoritmo.

---

## 31.11. Descenso de homomorfismos de anillos entre cocientes

### Teorema 31.11.1 — Descenso de homomorfismos de anillos entre cocientes {#talg-thm-00031}

Sean $f:R\to S$ un homomorfismo de anillos unitarios e $I\triangleleft R$, $J\triangleleft S$ ideales bilaterales. La condición $\forall i\in I,\ f(i)\in J$ equivale a la existencia de un único homomorfismo unital
$$
\overline f:R/I\longrightarrow S/J,\qquad
\overline f\circ q_I=q_J\circ f.
$$
En ese caso $\overline f([r]_I)=[f(r)]_J$. Se admiten los ideales totales y el anillo cero conforme a la convención del tratado.

#### Demostración {#talg-prf-00162}

**Existencia y buena definición.** Por la [propiedad de las proyecciones](tratado-de-algebra-capitulo-19-cocientes-de-anillos.md#talg-pro-00045), $q_J$ es un homomorfismo unital y $\ker q_J=J$. La composición $u=q_J\circ f$ es por tanto un homomorfismo unital. Para $i\in I$, la compatibilidad da $f(i)\in J$, luego $u(i)=0_{S/J}$. Así $I\subseteq\ker u$. La propiedad universal del cociente de anillos, [Teorema 29.32.1](tratado-de-algebra-capitulo-29-productos-directos-y-propiedades-universales.md#talg-thm-00022), produce el único homomorfismo $\overline f$ con $\overline f\circ q_I=u$. Al evaluar en $r$, se obtiene $\overline f([r]_I)=[f(r)]_J$. La propiedad universal garantiza independencia de representantes y preservación de suma, producto y unidad.

**Unicidad explícita.** Para $C\in R/I$, la sobreyectividad de $q_I$ permite tomar localmente $r$ con $C=q_I(r)$. Si $v\circ q_I=u$, entonces $v(C)=u(r)=\overline f(C)$. Extensionalidad funcional da $v=\overline f$.

**Necesidad.** Si existe un homomorfismo con la identidad conmutativa, para $i\in I$ tenemos $q_I(i)=0_{R/I}$. La preservación del cero da
$$
q_J(f(i))=\overline f(q_I(i))=\overline f(0_{R/I})=0_{S/J}.
$$
Luego $f(i)\in\ker q_J=J$. La condición es necesaria y suficiente. $\square$

---

## 31.12. Identidad y composición del descenso de grupos

### Proposición 31.12.1 — Identidad y composición del descenso de grupos {#talg-pro-00105}

Si $N\trianglelefteq G$, el descenso de $\operatorname{id}_G$ respecto de $N,N$ es $\operatorname{id}_{G/N}$. Si $f:G\to H$ y $g:H\to K$ son homomorfismos y $N\trianglelefteq G$, $M\trianglelefteq H$, $L\trianglelefteq K$ satisfacen $f(n)\in M$ para $n\in N$ y $g(m)\in L$ para $m\in M$, entonces $g\circ f$ desciende respecto de $N,L$ y
$$
\overline{g\circ f}=\overline g\circ\overline f.
$$

#### Demostración {#talg-prf-00163}

**Identidad.** Para $n\in N$, $\operatorname{id}_G(n)=n\in N$, luego el [Teorema 31.9.1](#talg-thm-00030) construye el descenso. Para $C=q_N(x)$, obtenido mediante un representante local,
$$
\overline{\operatorname{id}_G}(C)=q_N(\operatorname{id}_G(x))=q_N(x)=C.
$$
Extensionalidad da la identidad del cociente; ésta es un homomorfismo por la infraestructura de identidad.

**Composición.** Para $n\in N$, $f(n)\in M$ y luego $g(f(n))\in L$. Por tanto existen los tres descensos del enunciado. La composición $\overline g\circ\overline f$ es un homomorfismo. Para cada $x\in G$,
$$
(\overline g\circ\overline f)(q_N(x))
=\overline g(q_M(f(x)))=q_L(g(f(x)))
=\overline{g\circ f}(q_N(x)).
$$
Cada $C\in G/N$ tiene localmente esa forma, por la sobreyectividad de $q_N$. Las dos funciones coinciden en cada entrada y Extensionalidad funcional da la igualdad. No se identifica ningún conjunto cociente con otro ni se seleccionan representantes globales. $\square$

---

## 31.13. Identidad y composición del descenso de anillos

### Proposición 31.13.1 — Identidad y composición del descenso de anillos {#talg-pro-00106}

El descenso de $\operatorname{id}_R$ respecto de un ideal bilateral $I$ es $\operatorname{id}_{R/I}$. Para homomorfismos unitarios $f:R\to S$, $g:S\to T$ e ideales bilaterales $I,J,K$ respectivos, si $f(I)\subseteq J$, $g(J)\subseteq K$, entonces $\overline{g\circ f}=\overline g\circ\overline f$.

#### Demostración {#talg-prf-00164}

Para $i\in I$, $\operatorname{id}_R(i)=i\in I$, luego existe el descenso. En cada clase $[r]_I$ toma el valor $[r]_I$ y la sobreyectividad de la proyección prueba que es la identidad.

Para $i\in I$, $f(i)\in J$ implica $g(f(i))\in K$, de modo que también existe el descenso del compuesto. Las aplicaciones inducidas y su composición son homomorfismos unitarios. Para $r\in R$,
$$
(\overline g\circ\overline f)([r]_I)=\overline g([f(r)]_J)
=[g(f(r))]_K=\overline{g\circ f}([r]_I).
$$
Cada clase posee localmente un representante por la sobreyectividad de $q_I$. Las funciones coinciden en cada entrada; Extensionalidad funcional da la igualdad. $\square$

---

## 31.14. Núcleo y criterios del descenso de grupos

### Teorema 31.14.1 — Núcleo y criterios del descenso de grupos {#talg-thm-00032}

Bajo las hipótesis del [Teorema 31.9.1](#talg-thm-00030), sea $P=\{x\in G:f(x)\in M\}$. Entonces $P\trianglelefteq G$, $N\subseteq P$ y
$$
\ker\overline f=P/N:=\{q_N(p):p\in P\}.
$$
Aquí $P/N$ es el subgrupo imagen en $G/N$, con operaciones restringidas. Además,
$$
\overline f\text{ inyectiva}\iff P=N,\qquad
\overline f\text{ sobreyectiva}\iff H=\operatorname{im}(f)M.
$$
El descenso es un isomorfismo exactamente cuando se cumplen ambas condiciones.

#### Demostración {#talg-prf-00165}

**Preimagen normal.** $P$ existe por Separación y contiene $e_G$, pues $f(e_G)=e_H\in M$. Si $x,y\in P$, entonces $f(xy^{-1})=f(x)f(y)^{-1}\in M$; el [criterio de subgrupo habitado](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) prueba que $P$ es subgrupo. Para $g\in G$, $p\in P$, la normalidad de $M$ implica $f(gpg^{-1})=f(g)f(p)f(g)^{-1}\in M$. Así $P$ es normal. La compatibilidad inicial da $N\subseteq P$; el [teorema de correspondencia](tratado-de-algebra-capitulo-30-teoremas-de-isomorfia-superiores-y-correspondencia.md#talg-thm-00025) certifica el subgrupo imagen $P/N$.

**Núcleo.** Para cualquier $C\in G/N$, usemos localmente $x$ con $C=q_N(x)$. Entonces $C\in\ker\overline f$ equivale a $q_M(f(x))=e_{H/M}$, a $f(x)\in M$, y a $x\in P$. Esto implica $C\in P/N$. A la inversa, si $C=q_N(p)$ con $p\in P$, su imagen es $q_M(f(p))=e_{H/M}$. Las dos inclusiones dan la igualdad.

**Inyectividad.** Si el descenso es inyectivo y $x\in P$, sus valores en $q_N(x)$ y $q_N(e_G)$ coinciden. Por inyectividad, $q_N(x)=q_N(e_G)$, de donde $x\in\ker q_N=N$. Con $N\subseteq P$ resulta $P=N$. Si $P=N$, la fórmula del núcleo da $\ker\overline f=N/N=\{e_{G/N}\}$, porque todos los elementos de $N$ se proyectan al neutro y éste aparece como $q_N(e_G)$. El [criterio de núcleo trivial](tratado-de-algebra-capitulo-9-nucleo-e-imagen-de-homomorfismos-de-grupos.md#talg-thm-00002) prueba inyectividad.

**Sobreyectividad.** Si el descenso es sobreyectivo, para $h\in H$ existe localmente $C$ con $\overline f(C)=q_M(h)$ y luego $x$ con $C=q_N(x)$. Entonces $q_M(f(x))=q_M(h)$ y
$$
q_M(f(x)^{-1}h)=q_M(f(x))^{-1}q_M(h)=e_{H/M}.
$$
Así $m=f(x)^{-1}h\in M$ y $h=f(x)m\in\operatorname{im}(f)M$. La inclusión de ese producto en $H$ se sigue del cierre de la operación, luego $H=\operatorname{im}(f)M$.

Si vale esa igualdad, para cada clase $q_M(h)$ existe localmente una descomposición $h=f(x)m$, $m\in M$. Entonces $q_M(h)=q_M(f(x))q_M(m)=q_M(f(x))=\overline f(q_N(x))$. Cada clase tiene preimagen, y el descenso es sobreyectivo. La combinación de ambos criterios equivale a homomorfismo biyectivo, es decir, isomorfismo. $\square$

---

## 31.15. Núcleo y criterios del descenso de anillos

### Teorema 31.15.1 — Núcleo y criterios del descenso de anillos {#talg-thm-00033}

Bajo las hipótesis del [Teorema 31.11.1](#talg-thm-00031), sea $P=\{r\in R:f(r)\in J\}$. Entonces $P$ es ideal bilateral de $R$, $I\subseteq P$ y
$$
\ker\overline f=P/I:=\{q_I(p):p\in P\}.
$$
La notación $P/I$ designa un ideal imagen en $R/I$, sin considerar $P$ como subanillo unital. Además,
$$
\overline f\text{ inyectiva}\iff P=I,\qquad
\overline f\text{ sobreyectiva}\iff S=\operatorname{im}(f)+J.
$$
El descenso es isomorfismo exactamente cuando valen ambas condiciones.

#### Demostración {#talg-prf-00166}

**Ideal preimagen.** $P$ existe por Separación y contiene $0_R$, pues $f(0_R)=0_S\in J$. Si $a,b\in P$, $f(a-b)=f(a)-f(b)\in J$, luego $a-b\in P$. Para $r\in R$, $a\in P$,
$$
f(ra)=f(r)f(a)\in J,\qquad f(ar)=f(a)f(r)\in J.
$$
Las dos absorciones usan la bilateralidad de $J$. Así $P$ es ideal bilateral. La condición de descenso da $I\subseteq P$; la [correspondencia de ideales](tratado-de-algebra-capitulo-30-teoremas-de-isomorfia-superiores-y-correspondencia.md#talg-thm-00028) certifica $P/I$ como ideal de $R/I$.

**Núcleo.** Si $C=q_I(r)$, la fórmula del descenso da
$$
C\in\ker\overline f\iff q_J(f(r))=0_{S/J}
\iff f(r)\in J\iff r\in P.
$$
Toda clase tiene localmente un representante. Si $C$ está en el núcleo, la equivalencia lo sitúa en $P/I$; si $C=q_I(p)$ con $p\in P$, su imagen es cero. Extensionalidad da la igualdad.

**Inyectividad.** Si el descenso es inyectivo y $r\in P$, $\overline f(q_I(r))=0=\overline f(q_I(0_R))$ implica $q_I(r)=0$, luego $r\in I$. Con $I\subseteq P$, resulta $P=I$. A la inversa, supongamos $P=I$ y $\overline f(C)=\overline f(D)$. Tomemos localmente representantes $r,s$ de $C,D$. Por aditividad,
$$
q_J(f(r-s))=\overline f(q_I(r)-q_I(s))=0.
$$
Así $r-s\in P=I$, de donde $q_I(r-s)=0$ y $C-D=0$. En el grupo aditivo esto implica $C=D$, que prueba inyectividad.

**Sobreyectividad.** La imagen de $f$ es un subanillo unital por la [Proposición 17.3.1](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-pro-00035), por lo que su suma con $J$ está definida. Si el descenso es sobreyectivo, para $s\in S$ existen localmente una clase $C$ y un representante $r$ con $\overline f(C)=q_J(s)$ y $C=q_I(r)$. Entonces $q_J(s-f(r))=0$, luego $j=s-f(r)\in J$. Así $s=f(r)+j$ pertenece a $\operatorname{im}(f)+J$. La otra inclusión en $S$ usa cierre aditivo, y queda probada la igualdad.

Si esa igualdad vale, para $q_J(s)$ tomemos localmente $s=f(r)+j$, $j\in J$. Entonces
$$
q_J(s)=q_J(f(r))+q_J(j)=q_J(f(r))
=\overline f(q_I(r)).
$$
Cada clase tiene preimagen; el descenso es sobreyectivo. Un homomorfismo unital biyectivo es un isomorfismo, lo que concluye el criterio conjunto. $\square$

---

## 31.16. Transporte de subgrupos y normalidad bajo isomorfismos

### Teorema 31.16.1 — Transporte de subgrupos y normalidad bajo isomorfismos {#talg-thm-00034}

Sea $\varphi:G\to H$ un isomorfismo de grupos. Para $A\subseteq G$ y $B\subseteq H$ definimos localmente
$$
\varphi[A]=\{h\in H:\exists a\in A,\ h=\varphi(a)\},\qquad
\varphi^{-1}[B]=\{g\in G:\varphi(g)\in B\}.
$$
Entonces $A$ es subgrupo de $G$ si y sólo si $\varphi[A]$ es subgrupo de $H$; $A$ es normal en $G$ si y sólo si $\varphi[A]$ es normal en $H$. Imagen y preimagen dan biyecciones mutuamente inversas entre las familias de subgrupos, y entre las de subgrupos normales. Preservan y reflejan inclusión. La restricción $\varphi|_A:A\to\varphi[A]$ es un isomorfismo cuando $A$ es subgrupo.

#### Demostración {#talg-prf-00167}

**Existencia e inversión.** Las imágenes y preimágenes son subconjuntos por Separación; las familias de subgrupos son conjuntos por Potencia y Separación. La inversa funcional $\psi:H\to G$ de $\varphi$ existe y es homomorfismo por la [infraestructura de isomorfismos](tratado-de-algebra-capitulo-8-isomorfismos.md#talg-pro-00011). Para cualquier $A\subseteq G$, $g\in\varphi^{-1}[\varphi[A]]$ implica $\varphi(g)=\varphi(a)$ para algún $a\in A$. Inyectividad da $g=a\in A$. Si $g\in A$, su imagen pertenece a $\varphi[A]$, por lo que se obtiene la igualdad inversa. Para cualquier $B\subseteq H$, $\varphi[\varphi^{-1}[B]]\subseteq B$ por definición; si $b\in B$, la sobreyectividad proporciona $g$ con $\varphi(g)=b$, y $g\in\varphi^{-1}[B]$. Queda probada la otra igualdad. La preimagen también es $\psi[B]$, usando $\varphi\psi=\operatorname{id}_H$ y $\psi\varphi=\operatorname{id}_G$.

**Subgrupos.** Si $A$ es subgrupo, $\varphi(e_G)=e_H$ pertenece a $\varphi[A]$. Para $u=\varphi(a)$, $v=\varphi(b)$ con $a,b\in A$,
$$
uv^{-1}=\varphi(a)\varphi(b^{-1})=\varphi(ab^{-1})\in\varphi[A].
$$
El [criterio de subgrupo habitado](tratado-de-algebra-capitulo-6-subestructuras-y-criterio-de-subgrupo.md#talg-lem-00004) certifica $\varphi[A]$. Si $\varphi[A]$ es subgrupo, la misma verificación aplicada al homomorfismo $\psi$ da que $\psi[\varphi[A]]=A$ es subgrupo: contiene $\psi(e_H)=e_G$, y la diferencia multiplicativa de dos imágenes es la imagen de la diferencia multiplicativa de sus preimágenes. Así se prueba la reflexión sin presuponerla.

**Normalidad.** Si $A\trianglelefteq G$, para $h\in H$, $u=\varphi(a)\in\varphi[A]$ tomemos localmente $g$ con $\varphi(g)=h$. Entonces
$$
huh^{-1}=\varphi(gag^{-1})\in\varphi[A],
$$
porque $gag^{-1}\in A$. Así la imagen es normal. Recíprocamente, supongamos $\varphi[A]\trianglelefteq H$. Para $g\in G$, $a\in A$, la normalidad da
$$
\varphi(gag^{-1})=\varphi(g)\varphi(a)\varphi(g)^{-1}\in\varphi[A].
$$
La identidad de saturación ya probada implica $gag^{-1}\in A$, y $A$ es normal.

**Biyecciones e inclusión.** Las asignaciones restringidas a las familias indicadas están bien tipadas por los pasos anteriores. Sus grafos existen por Separación en los productos de esas familias; las dos identidades de inversión prueban que son mutuamente inversas. Si $A_1\subseteq A_2$, todo testigo de pertenencia a $\varphi[A_1]$ sirve para $\varphi[A_2]$. Si $\varphi[A_1]\subseteq\varphi[A_2]$ y $a\in A_1$, la saturación de $A_2$ implica $a\in A_2$. Así se preserva y refleja la inclusión.

Finalmente, la restricción conserva la operación porque $\varphi$ la conserva, es inyectiva por restricción y sobreyectiva sobre su imagen por definición. Es un isomorfismo entre las estructuras restringidas. $\square$

---

## 31.17. Transporte de subanillos unitarios e ideales bilaterales

### Teorema 31.17.1 — Transporte de subanillos unitarios e ideales bilaterales {#talg-thm-00035}

Sea $\varphi:R\to S$ un isomorfismo de anillos unitarios. Las asignaciones
$$
A\longmapsto\varphi[A]=\{s\in S:\exists a\in A,\ s=\varphi(a)\},
\qquad
B\longmapsto\varphi^{-1}[B]=\{r\in R:\varphi(r)\in B\}
$$
son mutuamente inversas en los subconjuntos y restringen a biyecciones entre los subanillos unitarios de $R,S$, y entre sus ideales bilaterales. En cada familia se preserva y refleja la inclusión. La restricción a un subanillo es un isomorfismo unital sobre su imagen. Un ideal se transporta como ideal; no se afirma que sea subanillo unital.

#### Demostración {#talg-prf-00168}

**Subconjuntos.** Las asignaciones y las familias existen por Separación y Potencia. Si $r\in\varphi^{-1}[\varphi[A]]$, hay $a\in A$ con $\varphi(r)=\varphi(a)$; inyectividad da $r=a$. La otra inclusión es inmediata por el testigo $a=r$. Si $s\in\varphi[\varphi^{-1}[B]]$, su representante $r$ satisface $\varphi(r)\in B$, de donde $s\in B$. Para $s\in B$, la sobreyectividad da localmente $r$ con $\varphi(r)=s$, luego $s$ está en aquella imagen. Así ambas composiciones son identidades. La inversa $\psi:S\to R$ es homomorfismo unital y $\varphi^{-1}[B]=\psi[B]$.

**Subanillos.** Si $A$ es subanillo unital, $1_S=\varphi(1_R)\in\varphi[A]$. Si $u=\varphi(a)$, $v=\varphi(b)$, con $a,b\in A$, entonces
$$
u-v=\varphi(a-b)\in\varphi[A],\qquad uv=\varphi(ab)\in\varphi[A].
$$
El [criterio de subanillo unital](tratado-de-algebra-capitulo-17-subanillos-y-homomorfismos-de-anillos.md#talg-thm-00009) certifica la imagen. Aplicando el mismo criterio explícitamente a $\psi$, para un subanillo $B$ su imagen contiene $\psi(1_S)=1_R$, contiene $\psi(b)-\psi(c)=\psi(b-c)$ y $\psi(b)\psi(c)=\psi(bc)$ para $b,c\in B$; por tanto la preimagen es subanillo. Las identidades de inversión prueban la reflexión.

**Ideales.** Si $A$ es ideal bilateral, la imagen contiene $\varphi(0_R)=0_S$ y está cerrada por diferencias. Para $s\in S$, $u=\varphi(a)$ con $a\in A$, tomemos localmente $r\in R$ con $\varphi(r)=s$. Entonces
$$
su=\varphi(ra)\in\varphi[A],\qquad us=\varphi(ar)\in\varphi[A].
$$
Así la imagen es ideal bilateral. Si $B$ es ideal de $S$, su preimagen contiene $0_R$; para $a,b$ en la preimagen, $\varphi(a-b)=\varphi(a)-\varphi(b)\in B$. Para $r\in R$, $a$ en la preimagen,
$$
\varphi(ra)=\varphi(r)\varphi(a)\in B,\qquad
\varphi(ar)=\varphi(a)\varphi(r)\in B.
$$
La preimagen es ideal bilateral. Usando la saturación de subconjuntos, esto también refleja la idealidad de $A$ a partir de la de su imagen.

**Inclusión y restricciones.** Si $A_1\subseteq A_2$, todo representante de un elemento de $\varphi[A_1]$ pertenece a $A_2$, luego las imágenes están incluidas. Si las imágenes están incluidas, para $a\in A_1$ tenemos $\varphi(a)\in\varphi[A_2]$, y la identidad de saturación implica $a\in A_2$. Las dos asignaciones son funciones en las familias indicadas y sus identidades de inversión prueban las biyecciones.

Para un subanillo $A$, la restricción es inyectiva y sobreyectiva sobre la imagen; conserva suma, producto y la unidad común porque $\varphi$ los conserva. Es por tanto isomorfismo unital. En el caso ideal, sólo se utilizan cierre aditivo y absorciones; no se presupone $1_R\in A$. $\square$

---

## 31.18. Síntesis estructural

El descenso exige compatibilidad con las relaciones que definen las clases. La propiedad universal construye el morfismo y garantiza buena definición y unicidad. Identidad y composición se conservan porque sus valores coinciden sobre las proyecciones sobreyectivas. La inyectividad mide la ausencia de nuevas identificaciones; la sobreyectividad mide si cada clase del codominio posee un representante procedente de la imagen. El transporte bajo isomorfismos conserva las subestructuras y permite recuperarlas mediante la inversa.

La [Parte VII](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md) utiliza a continuación los grupos aditivos y los principios funcionales y de cocientes como base de la construcción de espacios vectoriales. Cada nuevo objeto requiere definir la acción escalar y comprobar su buena definición.

---

[← **Capítulo 30 — Teoremas de isomorfía superiores y correspondencia**](tratado-de-algebra-capitulo-30-teoremas-de-isomorfia-superiores-y-correspondencia.md) · [**Tratado moderno de Álgebra**](../otros/tratado-de-algebra.md) · [**Capítulo 32 — Espacios vectoriales: definición y ejemplos** →](tratado-de-algebra-capitulo-32-espacios-vectoriales-definicion-y-ejemplos.md)
