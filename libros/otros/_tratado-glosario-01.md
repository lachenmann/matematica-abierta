---

## Antisimetría {#gl-antisimetria}

**Idea.** Una relación no puede relacionar mutuamente dos elementos distintos en ambos sentidos.

**En este tratado.** Una relación $R$ sobre $A$ es **antisimétrica** si

$$
(aRb\land bRa)\Longrightarrow a=b.
$$

La antisimetría no significa que $aRb$ impida $bRa$; significa que, si ambas relaciones ocurren, entonces los elementos deben coincidir.

**En el Tratado:** [Definición 0.4.6 — Propiedades de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion).

**Véase también:** [Simetría](#gl-simetria), [Reflexividad](#gl-reflexividad), [Transitividad](#gl-transitividad).

---

## Biyectividad {#gl-biyectividad}

**Idea.** Una función que establece una correspondencia uno a uno entre dominio y codominio.

**En este tratado.** Una función $f:A\to B$ es **biyectiva** cuando es a la vez inyectiva y sobreyectiva. Equivalentemente, es biyectiva si y sólo si posee una función inversa $f^{-1}:B\to A$.

**En el Tratado:** [Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-inyectiva-sobreyectiva-biyectiva) y [Teorema 0.6.7 — Caracterización de las funciones invertibles](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-funciones-invertibles).

**Véase también:** [Inyectividad](#gl-inyectividad), [Sobreyectividad](#gl-sobreyectividad), [Función inversa](#gl-funcion-inversa).

---

## Clase de equivalencia {#gl-clase-equivalencia}

**Idea.** El conjunto de todas las representaciones que la relación de equivalencia considera indistinguibles de una representación dada.

**En este tratado.** Si $\sim$ es una relación de equivalencia sobre $A$ y $a\in A$, definimos

$$
[a]_{\sim}:=\{x\in A:x\sim a\}.
$$

Cuando la relación esté clara por el contexto, escribiremos simplemente $[a]$.

**En el Tratado:** [Definición 0.5.1 — Clase de equivalencia](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-clase-equivalencia).

**Véase también:** [Representante](#gl-representante), [Igualdad de clases](#gl-igualdad-clases), [Relación de equivalencia](#gl-relacion-equivalencia), [Conjunto cociente](#gl-conjunto-cociente).

---

## Codominio {#gl-codominio}

**Idea.** El conjunto de llegada declarado como parte de los datos de una función.

**En este tratado.** Si
$$
f=\langle A,B,G_f\rangle,
$$
entonces $B$ es el **codominio** de $f$. El codominio forma parte de la identidad de la función: dos funciones con el mismo dominio y el mismo grafo, pero codominios distintos, son funciones distintas.

**En el Tratado:** [Definición 0.6.1 — Función como dominio, codominio y grafo](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-funcion).

**Véase también:** [Función](#gl-funcion), [Dominio de una función](#gl-dominio-funcion), [Grafo de una función](#gl-grafo-funcion).

---

## Composición de funciones {#gl-composicion-funciones}

**Idea.** Aplicar una función y, sobre su resultado, aplicar una segunda función.

**En este tratado.** Si $f:A\to B$ y $g:B\to C$, definimos
$$
g\circ f:A\to C,
\qquad
(g\circ f)(a):=g(f(a)).
$$
Su grafo coincide con la composición relacional de los grafos correspondientes.

**En el Tratado:** [Definición 0.6.4 — Identidad y composición de funciones](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-identidad-composicion-funciones).

**Véase también:** [Función](#gl-funcion), [Función identidad](#gl-funcion-identidad), [Composición de relaciones](#gl-composicion-relaciones).

---

## Composición de relaciones {#gl-composicion-relaciones}

**Idea.** Encadenar dos relaciones haciendo coincidir la salida intermedia de la primera con la entrada de la segunda.

**En este tratado.** Si $R\subseteq A\times B$ y $S\subseteq B\times C$, definimos

$$
S\circ R
:=
\{\langle a,c\rangle\in A\times C:\exists b\in B\;(aRb\land bSc)\}.
$$

La composición se lee de derecha a izquierda: primero $R$, después $S$.

**En el Tratado:** [Definición 0.4.4 — Composición de relaciones](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-composicion-relaciones).

**Véase también:** [Relación binaria](#gl-relacion-binaria), [Producto cartesiano](#gl-producto-cartesiano).

---

## Conjunto cociente {#gl-conjunto-cociente}

**Idea.** El nuevo conjunto cuyos elementos son las clases de equivalencia, no las representaciones individuales.

**En este tratado.** Si $\sim$ es una relación de equivalencia sobre $A$,

$$
A/{\sim}
:=
\{C\in\mathcal P(A):\exists a\in A\;(C=[a])\}.
$$

Equivalentemente,

$$
A/{\sim}=\{[a]:a\in A\}.
$$

La primera expresión es la definición conjuntista canónica; la segunda es notación descriptiva.

**En el Tratado:** [Definición 0.5.7 — Conjunto cociente](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjunto-cociente).

**Véase también:** [Clase de equivalencia](#gl-clase-equivalencia), [Partición](#gl-particion), [Representante](#gl-representante).

---

## Conjunto de funciones {#gl-conjunto-funciones}

**Idea.** El conjunto formado por todas las funciones que tienen un dominio y un codominio fijados.

**En este tratado.** Para conjuntos $A$ y $B$,
$$
B^A
$$
denota el conjunto de todas las funciones $f:A\to B$. Su existencia se demuestra dentro de ZF a partir de $\mathcal P(A\times B)$, reemplazo y separación.

**En el Tratado:** [Definición 0.6.11 — Conjunto de funciones](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjunto-funciones).

**Véase también:** [Función](#gl-funcion), [Conjunto potencia](#gl-conjunto-potencia), [Producto cartesiano](#gl-producto-cartesiano).

---

## Conjunto potencia {#gl-conjunto-potencia}

**Idea.** El conjunto que reúne todos los subconjuntos de un conjunto dado.

**En este tratado.** Para cada conjunto $A$, $\mathcal P(A)$ es el conjunto caracterizado por

$$
X\in\mathcal P(A)
\quad\Longleftrightarrow\quad
X\subseteq A.
$$

Su existencia pertenece a los axiomas admitidos de ZF.

**En el Tratado:** [Definición 0.2.12 — Conjunto potencia](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjunto-potencia).

**Véase también:** [Subconjunto](#gl-subconjunto), [ZF](#gl-zf).

---

## Conjunto vacío {#gl-conjunto-vacio}

**Idea.** El conjunto que no contiene ningún elemento.

**En este tratado.** El símbolo $\varnothing$ sólo se introduce después de demostrar que existe un único conjunto sin elementos. No se presupone su existencia como una notación anterior a esa prueba.

**En el Tratado:** [existencia y unicidad](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-existencia-vacio) y [Notación 0.2.6 — Conjunto vacío](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjunto-vacio).

**Véase también:** [Extensionalidad](#gl-extensionalidad), [Separación restringida](#gl-separacion-restringida).

---

## Conjuntos disjuntos {#gl-conjuntos-disjuntos}

**Idea.** Dos conjuntos que no comparten elementos.

**En este tratado.** $A$ y $B$ son disjuntos cuando

$$
A\cap B=\varnothing.
$$

**En el Tratado:** [Definición 0.2.14 — Conjuntos disjuntos](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-conjuntos-disjuntos).

**Véase también:** [Intersección](#gl-interseccion), [Conjunto vacío](#gl-conjunto-vacio).

---

## Diferencia conjuntista {#gl-diferencia-conjuntista}

**Idea.** Los elementos de un conjunto que no pertenecen a otro.

**En este tratado.**

$$
A\setminus B:=\{x\in A:x\notin B\}.
$$

La notación $A-B$ no se usa para diferencia de conjuntos, porque se reserva para contextos algebraicos posteriores.

**En el Tratado:** [Definición 0.2.11 — Diferencia conjuntista](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-diferencia-conjuntista).

**Véase también:** [Separación restringida](#gl-separacion-restringida), [Subconjunto](#gl-subconjunto).

---

## Dominio de una función {#gl-dominio-funcion}

**Idea.** El conjunto de entradas sobre las que una función está definida.

**En este tratado.** Si
$$
f=\langle A,B,G_f\rangle,
$$
entonces $A$ es el **dominio** de $f$. No se recupera sólo del grafo por convención: forma parte explícita del objeto función.

**En el Tratado:** [Definición 0.6.1 — Función como dominio, codominio y grafo](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-funcion).

**Véase también:** [Función](#gl-funcion), [Codominio](#gl-codominio), [Dominio de una relación](#gl-dominio-relacion).

---

## Dominio de una relación {#gl-dominio-relacion}

**Idea.** Los elementos que aparecen como primera componente de algún par perteneciente a la relación.

**En este tratado.** Si $R\subseteq A\times B$,

$$
\operatorname{dom}R
:=
\{a\in A:\exists b\in B\;(aRb)\}.
$$

**En el Tratado:** [Definición 0.4.2 — Dominio y recorrido de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-dominio-recorrido-relacion).

**Véase también:** [Recorrido de una relación](#gl-recorrido-relacion), [Relación binaria](#gl-relacion-binaria).

---

## Extensionalidad {#gl-extensionalidad}

**Idea.** Un conjunto queda determinado por sus elementos.

**En este tratado.** El axioma de extensionalidad permite concluir $A=B$ cuando $A$ y $B$ tienen exactamente los mismos elementos. Es el fundamento del criterio práctico de igualdad por doble inclusión.

**En el Tratado:** [Axioma de extensionalidad](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-axioma-extensionalidad).

**Véase también:** [Subconjunto](#gl-subconjunto), [ZF](#gl-zf).

---

## Familia indexada {#gl-familia-indexada}

**Idea.** Una colección cuyos elementos están organizados por un conjunto de índices.

**En este tratado.** Una **familia indexada** de elementos de $X$, con conjunto de índices $I$, es una función
$$
x:I\to X.
$$
La escribimos $(x_i)_{i\in I}$, con $x_i:=x(i)$. Para familias de subconjuntos de un ambiente $U$, esta notación permite definir uniones e intersecciones indexadas.

**En el Tratado:** [Definición 0.6.16 — Familia indexada](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-familia-indexada).

**Véase también:** [Función](#gl-funcion), [Imagen directa](#gl-imagen-directa), [Unión](#gl-union), [Intersección](#gl-interseccion).

---
