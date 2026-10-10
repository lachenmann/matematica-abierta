## Función {#gl-funcion}

**Idea.** Una asignación que proporciona a cada entrada exactamente una salida.

**En este tratado.** Una función $f$ de $A$ en $B$ es el objeto
$$
f=\langle A,B,G_f\rangle,
$$
donde $G_f\subseteq A\times B$ y para todo $a\in A$ existe un único $b\in B$ con $\langle a,b\rangle\in G_f$. Dominio, codominio y grafo forman parte de los datos de la función.

**En el Tratado:** [Definición 0.6.1 — Función como dominio, codominio y grafo](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-funcion).

**Véase también:** [Dominio de una función](#gl-dominio-funcion), [Codominio](#gl-codominio), [Grafo de una función](#gl-grafo-funcion).

---

## Función identidad {#gl-funcion-identidad}

**Idea.** La función que deja cada elemento donde está.

**En este tratado.** Para un conjunto $A$,
$$
\operatorname{id}_A:A\to A,
\qquad
\operatorname{id}_A(a)=a.
$$
Actúa como identidad para la composición de funciones.

**En el Tratado:** [Definición 0.6.4 — Identidad y composición de funciones](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-identidad-composicion-funciones).

**Véase también:** [Composición de funciones](#gl-composicion-funciones), [Función](#gl-funcion).

---

## Función inversa {#gl-funcion-inversa}

**Idea.** La función que deshace una función biyectiva.

**En este tratado.** Si $f:A\to B$ es biyectiva, $f^{-1}:B\to A$ denota la única función que satisface
$$
f^{-1}\circ f=\operatorname{id}_A,
\qquad
f\circ f^{-1}=\operatorname{id}_B.
$$
El símbolo $f^{-1}$ sólo se usa como función inversa después de demostrar la biyectividad de $f$.

**En el Tratado:** [Notación 0.6.8 — Función inversa](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-funcion-inversa).

**Véase también:** [Biyectividad](#gl-biyectividad), [Relación inversa](#gl-relacion-inversa), [Preimagen](#gl-preimagen).

---

## Grafo de una función {#gl-grafo-funcion}

**Idea.** El conjunto de todos los pares entrada–salida de una función.

**En este tratado.** Si $f:A\to B$, su grafo $G_f$ es un subconjunto de $A\times B$ tal que para cada $a\in A$ existe un único $b\in B$ con
$$
\langle a,b\rangle\in G_f.
$$
La escritura $f(a)=b$ abrevia precisamente esta pertenencia al grafo.

**En el Tratado:** [Definición 0.6.1](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-funcion) y [Notación 0.6.2 — Flecha y evaluación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-flecha-evaluacion).

**Véase también:** [Función](#gl-funcion), [Producto cartesiano](#gl-producto-cartesiano), [Relación binaria](#gl-relacion-binaria).

---

## Igualdad de clases {#gl-igualdad-clases}

**Idea.** Dos representantes determinan la misma clase exactamente cuando son equivalentes.

**En este tratado.** Para $a,b\in A$,

$$
[a]=[b]
\quad\Longleftrightarrow\quad
a\sim b.
$$

Este criterio permite dejar de depender de un representante particular: cambiar un elemento por otro equivalente no cambia la clase.

**En el Tratado:** [Lema 0.5.3 — Igualdad de clases](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-igualdad-clases).

**Véase también:** [Clase de equivalencia](#gl-clase-equivalencia), [Representante](#gl-representante), [Relación de equivalencia](#gl-relacion-equivalencia).

---

## Imagen directa {#gl-imagen-directa}

**Idea.** Los valores que una función alcanza a partir de un subconjunto del dominio.

**En este tratado.** Si $f:A\to B$ y $X\subseteq A$,
$$
f[X]
:=
\{b\in B:\exists x\in X\;(f(x)=b)\}.
$$
Los corchetes distinguen la imagen de subconjuntos de la evaluación puntual $f(a)$.

**En el Tratado:** [Definición 0.6.9 — Imagen y preimagen](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-imagen-preimagen).

**Véase también:** [Preimagen](#gl-preimagen), [Función](#gl-funcion), [Sobreyectividad](#gl-sobreyectividad).

---

## Intersección {#gl-interseccion}

**Idea.** La parte común de dos conjuntos.

**En este tratado.**

$$
A\cap B:=\{x\in A:x\in B\}.
$$

Se construye por separación dentro de $A$.

**En el Tratado:** [Definición 0.2.10 — Intersección binaria](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-interseccion-binaria).

**Véase también:** [Unión](#gl-union), [Separación restringida](#gl-separacion-restringida), [Conjuntos disjuntos](#gl-conjuntos-disjuntos).

---

## Inyectividad {#gl-inyectividad}

**Idea.** Entradas distintas no pueden producir la misma salida.

**En este tratado.** Una función $f:A\to B$ es **inyectiva** si
$$
f(a)=f(a')\Longrightarrow a=a'.
$$

**En el Tratado:** [Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-inyectiva-sobreyectiva-biyectiva).

**Véase también:** [Sobreyectividad](#gl-sobreyectividad), [Biyectividad](#gl-biyectividad).

---

## Lógica clásica {#gl-logica-clasica}

**Idea.** El marco lógico ordinario en el que se permiten, entre otros principios, el tercero excluido y la reducción al absurdo.

**En este tratado.** La lógica ambiente es lógica clásica de primer orden con igualdad. La igualdad es lógica y primitiva; $\in$ es el único símbolo no lógico primitivo del lenguaje conjuntista.

**En el Tratado:** [Convención 0.1.2 — Lógica ambiente](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-logica-ambiente).

**Véase también:** [Metanivel](#gl-metanivel), [Nivel objeto](#gl-nivel-objeto), [ZF](#gl-zf).

---

## Metanivel {#gl-metanivel}

**Idea.** El nivel desde el cual hablamos *sobre* las expresiones y demostraciones matemáticas.

**En este tratado.** En el metanivel hablamos de fórmulas, variables, demostraciones, definiciones, dependencias y numeración editorial. Los numerales de capítulos o resultados pertenecen a este nivel mientras los números naturales todavía no hayan sido construidos como objetos del tratado.

**En el Tratado:** [Convención 0.1.1 — Metanivel y nivel objeto](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-metanivel-nivel-objeto).

**Véase también:** [Nivel objeto](#gl-nivel-objeto).

---

## Nivel objeto {#gl-nivel-objeto}

**Idea.** El nivel en el que viven los objetos matemáticos de los que habla la teoría.

**En este tratado.** En el nivel objeto, las variables del lenguaje conjuntista recorren conjuntos. Se distingue deliberadamente del metanivel editorial y lógico.

**En el Tratado:** [Convención 0.1.1 — Metanivel y nivel objeto](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-metanivel-nivel-objeto).

**Véase también:** [Metanivel](#gl-metanivel), [ZF](#gl-zf).

---

## Par de Kuratowski {#gl-par-kuratowski}

**Idea.** Una realización concreta de la noción de par ordenado mediante conjuntos ordinarios.

**En este tratado.** El par ordenado de $a$ y $b$ se codifica por

$$
\langle a,b\rangle
:=
\bigl\{\{a\},\{a,b\}\bigr\}.
$$

Esta elección es una implementación conjuntista. Su propiedad esencial es el criterio

$$
\langle a,b\rangle=\langle c,d\rangle
\iff
(a=c\ \text{y}\ b=d).
$$

**En el Tratado:** [Definición 0.3.1 — Par ordenado de Kuratowski](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-par-ordenado-kuratowski).

**Véase también:** [Par ordenado](#gl-par-ordenado), [Par no ordenado](#gl-par-no-ordenado), [Singleton](#gl-singleton).

---

## Par no ordenado {#gl-par-no-ordenado}

**Idea.** Un conjunto que contiene exactamente dos objetos, sin distinguir cuál aparece “primero”.

**En este tratado.** $\{a,b\}$ denota el único conjunto cuyos elementos son exactamente $a$ y $b$. La unicidad se sigue de extensionalidad. No debe confundirse con el par ordenado, que se introducirá más adelante.

**En el Tratado:** [Notación 0.2.8 — Pares no ordenados y singletons](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-par-no-ordenado-singleton).

**Véase también:** [Singleton](#gl-singleton), [Extensionalidad](#gl-extensionalidad).

---

## Par ordenado {#gl-par-ordenado}

**Idea.** Un objeto con dos componentes en el que importa cuál es la primera y cuál la segunda.

**En este tratado.** Los pares ordenados se realizan mediante la codificación de Kuratowski. Después de demostrar su teorema característico, la notación $\langle a,b\rangle$ podrá usarse atendiendo a sus coordenadas y no a la implementación conjuntista subyacente.

**En el Tratado:** [Definición 0.3.1 — Par ordenado de Kuratowski](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-par-ordenado-kuratowski).

**Véase también:** [Par de Kuratowski](#gl-par-kuratowski), [Producto cartesiano](#gl-producto-cartesiano).

---

## Partición {#gl-particion}

**Idea.** Una descomposición de un conjunto en piezas no vacías que no se solapan y que, juntas, cubren todo el conjunto.

**En este tratado.** Una partición de $A$ es un conjunto $\mathscr P$ de subconjuntos de $A$ tal que:

1. $\varnothing\notin\mathscr P$;
2. si $C,D\in\mathscr P$ y $C\neq D$, entonces $C\cap D=\varnothing$;
3. todo $a\in A$ pertenece a algún $C\in\mathscr P$.

Las clases de cualquier relación de equivalencia sobre $A$ forman una partición de $A$.

**En el Tratado:** [Definición 0.5.5 — Partición](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-particion).

**Véase también:** [Clase de equivalencia](#gl-clase-equivalencia), [Conjunto cociente](#gl-conjunto-cociente), [Conjuntos disjuntos](#gl-conjuntos-disjuntos).

---

## Preimagen {#gl-preimagen}

**Idea.** Los elementos del dominio cuyos valores caen en un subconjunto dado del codominio.

**En este tratado.** Si $f:A\to B$ y $Y\subseteq B$,
$$
f^{-1}[Y]
:=
\{a\in A:f(a)\in Y\}.
$$
Esta notación no presupone que $f$ sea biyectiva y no debe confundirse con la función inversa.

**En el Tratado:** [Definición 0.6.9 — Imagen y preimagen](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-imagen-preimagen).

**Véase también:** [Imagen directa](#gl-imagen-directa), [Función inversa](#gl-funcion-inversa), [Función](#gl-funcion).

---
