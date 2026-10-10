## Principio de definición sobre clases {#gl-definicion-sobre-clases}

**Idea.** Una regla definida sobre representantes desciende al cociente exactamente cuando no cambia al sustituir un representante por otro equivalente.

**En este tratado.** Si $\sim$ es una relación de equivalencia sobre $A$ y $\varphi:A\to B$ satisface
$$
a\sim a'
\Longrightarrow
\varphi(a)=\varphi(a'),
$$
entonces existe una única función
$$
\overline{\varphi}:A/{\sim}\to B
$$
con $\overline{\varphi}([a])=\varphi(a)$.

**En el Tratado:** [Teorema 0.6.15 — Principio de definición sobre clases](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-definicion-sobre-clases).

**Véase también:** [Conjunto cociente](#gl-conjunto-cociente), [Proyección canónica](#gl-proyeccion-canonica), [Representante](#gl-representante).

---

## Producto cartesiano {#gl-producto-cartesiano}

**Idea.** El conjunto de todos los pares ordenados cuya primera componente proviene de un conjunto y cuya segunda componente proviene de otro.

**En este tratado.** Para conjuntos $A$ y $B$,

$$
A\times B
:=
\{\langle a,b\rangle:a\in A,\ b\in B\}.
$$

La existencia de este conjunto se demuestra construyéndolo por separación dentro de $\mathcal P(\mathcal P(A\cup B))$.

**En el Tratado:** [Definición 0.3.6 — Producto cartesiano](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-producto-cartesiano).

**Véase también:** [Par ordenado](#gl-par-ordenado), [Conjunto potencia](#gl-conjunto-potencia), [Separación restringida](#gl-separacion-restringida).

---

## Proyección canónica {#gl-proyeccion-canonica}

**Idea.** La función que envía cada representante a su clase de equivalencia.

**En este tratado.** Si $\sim$ es una relación de equivalencia sobre $A$,
$$
\pi_{\sim}:A\to A/{\sim},
\qquad
\pi_{\sim}(a):=[a].
$$
Esta función es sobreyectiva.

**En el Tratado:** [Definición 0.6.13 — Proyección canónica de un cociente](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-proyeccion-canonica).

**Véase también:** [Conjunto cociente](#gl-conjunto-cociente), [Clase de equivalencia](#gl-clase-equivalencia), [Principio de definición sobre clases](#gl-definicion-sobre-clases).

---

## Recorrido de una relación {#gl-recorrido-relacion}

**Idea.** Los elementos que aparecen como segunda componente de algún par perteneciente a la relación.

**En este tratado.** Si $R\subseteq A\times B$,

$$
\operatorname{ran}R
:=
\{b\in B:\exists a\in A\;(aRb)\}.
$$

Usaremos `ran` para relaciones y reservaremos `im` para la imagen de un subconjunto bajo una función.

**En el Tratado:** [Definición 0.4.2 — Dominio y recorrido de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-dominio-recorrido-relacion).

**Véase también:** [Dominio de una relación](#gl-dominio-relacion), [Relación binaria](#gl-relacion-binaria).

---

## Reflexividad {#gl-reflexividad}

**Idea.** Cada elemento está relacionado consigo mismo.

**En este tratado.** Una relación $R$ sobre $A$ es **reflexiva** si

$$
\forall a\in A,\quad aRa.
$$

**En el Tratado:** [Definición 0.4.6 — Propiedades de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion).

**Véase también:** [Simetría](#gl-simetria), [Transitividad](#gl-transitividad), [Relación de equivalencia](#gl-relacion-equivalencia).

---

## Relación binaria {#gl-relacion-binaria}

**Idea.** Una selección de pares ordenados que indica qué elementos de un conjunto se relacionan con elementos de otro.

**En este tratado.** Una relación binaria de $A$ en $B$ es un conjunto

$$
R\subseteq A\times B.
$$

Cuando $A=B$, hablamos de una relación **sobre** $A$. La escritura $aRb$ abrevia $\langle a,b\rangle\in R$.

**En el Tratado:** [Definición 0.4.1 — Relación binaria](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-binaria).

**Véase también:** [Par ordenado](#gl-par-ordenado), [Producto cartesiano](#gl-producto-cartesiano), [Dominio de una relación](#gl-dominio-relacion).

---

## Relación de equivalencia {#gl-relacion-equivalencia}

**Idea.** Una relación que permite considerar como indistinguibles, para cierto propósito, elementos que pertenecen a una misma clase.

**En este tratado.** Una relación $\sim$ sobre $A$ es una **relación de equivalencia** si es reflexiva, simétrica y transitiva.

Las clases de equivalencia y el conjunto cociente se construyen en §0.5 a partir de esta noción.

**En el Tratado:** [Definición 0.4.7 — Relación de equivalencia](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-equivalencia).

**Véase también:** [Reflexividad](#gl-reflexividad), [Simetría](#gl-simetria), [Transitividad](#gl-transitividad).

---

## Relación inversa {#gl-relacion-inversa}

**Idea.** La relación obtenida al intercambiar la primera y la segunda componente de cada par.

**En este tratado.** Si $R\subseteq A\times B$,

$$
R^{-1}
:=
\{\langle b,a\rangle\in B\times A:aRb\}.
$$

Esta notación no presupone que $R$ sea una función ni que exista una función inversa.

**En el Tratado:** [Definición 0.4.3 — Relación inversa](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-relacion-inversa).

**Véase también:** [Relación binaria](#gl-relacion-binaria), [Par ordenado](#gl-par-ordenado).

---

## Representante {#gl-representante}

**Idea.** Un elemento usado para nombrar una clase de equivalencia, sin que la clase dependa de cuál de sus elementos elijamos para nombrarla.

**En este tratado.** Si $a\in A$, entonces $a\in[a]$. Llamamos **representante** de una clase a cualquiera de sus elementos. Si $b\in[a]$, entonces $b\sim a$ y, por el criterio de igualdad de clases,

$$
[b]=[a].
$$

Por eso ninguna construcción sobre clases deberá depender de escoger un representante privilegiado.

**En el Tratado:** [Proposición 0.5.2 — Existencia y pertenencia del representante](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-representante-clase) y [Lema 0.5.3 — Igualdad de clases](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-igualdad-clases).

**Véase también:** [Clase de equivalencia](#gl-clase-equivalencia), [Igualdad de clases](#gl-igualdad-clases), [Conjunto cociente](#gl-conjunto-cociente).

---

## Separación restringida {#gl-separacion-restringida}

**Idea.** Formar un subconjunto seleccionando, dentro de un conjunto ya existente, los elementos que satisfacen una propiedad.

**En este tratado.**

$$
\{x\in A:P(x)\}
$$

denota el subconjunto de $A$ formado por los $x$ que satisfacen $P(x)$. Esta notación no autoriza una comprensión irrestricta $\{x:P(x)\}$ sin conjunto ambiente.

**En el Tratado:** [Notación 0.1.3 — Separación restringida](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-separacion-restringida).

**Véase también:** [Subconjunto](#gl-subconjunto), [ZF](#gl-zf).

---

## Simetría {#gl-simetria}

**Idea.** Si un elemento se relaciona con otro, la relación también vale en sentido contrario.

**En este tratado.** Una relación $R$ sobre $A$ es **simétrica** si

$$
aRb\Longrightarrow bRa.
$$

**En el Tratado:** [Definición 0.4.6 — Propiedades de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion).

**Véase también:** [Antisimetría](#gl-antisimetria), [Reflexividad](#gl-reflexividad), [Relación de equivalencia](#gl-relacion-equivalencia).

---

## Singleton {#gl-singleton}

**Idea.** Un conjunto con exactamente un elemento.

**En este tratado.**

$$
\{a\}:=\{a,a\}.
$$

El singleton se obtiene como caso degenerado del par no ordenado.

**En el Tratado:** [Notación 0.2.8 — Pares no ordenados y singletons](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-par-no-ordenado-singleton).

**Véase también:** [Par no ordenado](#gl-par-no-ordenado).

---

## Sobreyectividad {#gl-sobreyectividad}

**Idea.** Todo elemento del codominio es alcanzado por alguna entrada.

**En este tratado.** Una función $f:A\to B$ es **sobreyectiva** si para todo $b\in B$ existe $a\in A$ tal que
$$
f(a)=b.
$$

**En el Tratado:** [Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-inyectiva-sobreyectiva-biyectiva).

**Véase también:** [Inyectividad](#gl-inyectividad), [Biyectividad](#gl-biyectividad), [Codominio](#gl-codominio).

---

## Subconjunto {#gl-subconjunto}

**Idea.** $A$ está contenido en $B$ cuando todo elemento de $A$ también pertenece a $B$.

**En este tratado.**

$$
A\subseteq B
\quad\Longleftrightarrow\quad
\forall x\,(x\in A\rightarrow x\in B).
$$

La inclusión propia se escribe $A\subsetneq B$ y exige además $A\neq B$.

**En el Tratado:** [Definición 0.2.1 — Subconjunto](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-subconjunto).

**Véase también:** [Extensionalidad](#gl-extensionalidad), [Conjunto potencia](#gl-conjunto-potencia).

---

## Totalidad (conexidad) {#gl-totalidad}

**Idea.** Cualquier par de elementos puede compararse en al menos uno de los dos sentidos de la relación.

**En este tratado.** Una relación $R$ sobre $A$ es **total** o **conexa** si, para cualesquiera $a,b\in A$,

$$
aRb\quad\text{o}\quad bRa.
$$

**En el Tratado:** [Definición 0.4.6 — Propiedades de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion).

**Véase también:** [Relación binaria](#gl-relacion-binaria), [Antisimetría](#gl-antisimetria), [Transitividad](#gl-transitividad).

---
