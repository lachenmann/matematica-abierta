---
title: "Tratado de análisis — Glosario matemático"
description: "Glosario vivo del Tratado de análisis, con definiciones breves y enlaces al punto exacto de la obra donde cada noción se introduce."
author: "Gustav A. Tachek"
content-id: MA-BCH-0006
content-type: book-chapter
book-id: MA-BOK-0003
status: published
date-created: 2026-09-09
date-modified: 2026-09-13
areas:
  - fundamentos
  - analisis
level: avanzado
topics:
  - glosario
  - logica-matematica
  - teoria-de-conjuntos
  - relaciones-de-equivalencia
  - conjuntos-cociente
  - funciones
prerequisites: []
related:
  - MA-BOK-0003
  - MA-BCH-0005
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Glosario matemático

[**← Volver al Tratado de análisis**](tratado-de-analisis.md) ·
[**Capítulo 0 — Fundamento lógico y conjuntista**](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md)

Este glosario acompaña la publicación progresiva del *Tratado de análisis*. **No se adelanta al texto**: una entrada se incorpora cuando la noción correspondiente ya ha sido definida, construida o fijada en la edición pública.

Cada entrada distingue dos niveles:

- **Idea:** una orientación conceptual breve para recuperar rápidamente la intuición;
- **En este tratado:** la acepción precisa adoptada en la obra.

El enlace **En el Tratado** conduce al punto exacto donde la noción se introduce o queda justificada.

## Índice actual

[Antisimetría](#gl-antisimetria) ·
[Biyectividad](#gl-biyectividad) ·
[Clase de equivalencia](#gl-clase-equivalencia) ·
[Codominio](#gl-codominio) ·
[Composición de funciones](#gl-composicion-funciones) ·
[Composición de relaciones](#gl-composicion-relaciones) ·
[Conjunto cociente](#gl-conjunto-cociente) ·
[Conjunto de funciones](#gl-conjunto-funciones) ·
[Conjunto potencia](#gl-conjunto-potencia) ·
[Conjunto vacío](#gl-conjunto-vacio) ·
[Conjuntos disjuntos](#gl-conjuntos-disjuntos) ·
[Diferencia conjuntista](#gl-diferencia-conjuntista) ·
[Dominio de una función](#gl-dominio-funcion) ·
[Dominio de una relación](#gl-dominio-relacion) ·
[Extensionalidad](#gl-extensionalidad) ·
[Familia indexada](#gl-familia-indexada) ·
[Función](#gl-funcion) ·
[Función identidad](#gl-funcion-identidad) ·
[Función inversa](#gl-funcion-inversa) ·
[Grafo de una función](#gl-grafo-funcion) ·
[Igualdad de clases](#gl-igualdad-clases) ·
[Imagen directa](#gl-imagen-directa) ·
[Intersección](#gl-interseccion) ·
[Inyectividad](#gl-inyectividad) ·
[Lógica clásica](#gl-logica-clasica) ·
[Metanivel](#gl-metanivel) ·
[Nivel objeto](#gl-nivel-objeto) ·
[Par de Kuratowski](#gl-par-kuratowski) ·
[Par no ordenado](#gl-par-no-ordenado) ·
[Par ordenado](#gl-par-ordenado) ·
[Partición](#gl-particion) ·
[Preimagen](#gl-preimagen) ·
[Principio de definición sobre clases](#gl-definicion-sobre-clases) ·
[Producto cartesiano](#gl-producto-cartesiano) ·
[Proyección canónica](#gl-proyeccion-canonica) ·
[Recorrido de una relación](#gl-recorrido-relacion) ·
[Reflexividad](#gl-reflexividad) ·
[Relación binaria](#gl-relacion-binaria) ·
[Relación de equivalencia](#gl-relacion-equivalencia) ·
[Relación inversa](#gl-relacion-inversa) ·
[Representante](#gl-representante) ·
[Separación restringida](#gl-separacion-restringida) ·
[Simetría](#gl-simetria) ·
[Singleton](#gl-singleton) ·
[Sobreyectividad](#gl-sobreyectividad) ·
[Subconjunto](#gl-subconjunto) ·
[Totalidad (conexidad)](#gl-totalidad) ·
[Transitividad](#gl-transitividad) ·
[Tupla finita](#gl-tupla-finita) ·
[Unión](#gl-union) ·
[ZF](#gl-zf)

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

## Transitividad {#gl-transitividad}

**Idea.** Dos pasos consecutivos de la relación pueden comprimirse en uno.

**En este tratado.** Una relación $R$ sobre $A$ es **transitiva** si

$$
(aRb\land bRc)\Longrightarrow aRc.
$$

**En el Tratado:** [Definición 0.4.6 — Propiedades de una relación](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-propiedades-relacion).

**Véase también:** [Reflexividad](#gl-reflexividad), [Simetría](#gl-simetria), [Relación de equivalencia](#gl-relacion-equivalencia).

---

## Tupla finita {#gl-tupla-finita}

**Idea.** Una lista ordenada de un número finito de componentes.

**En este tratado.** Las tuplas de longitud mayor que dos se codifican mediante pares ordenados anidados. Salvo indicación contraria,

$$
\langle a,b,c\rangle
:=
\langle a,\langle b,c\rangle\rangle.
$$

La forma concreta de anidación es representacional y no se considera contenido matemático adicional.

**En el Tratado:** [Convención 0.3.5 — Tuplas finitas](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-tuplas-finitas).

**Véase también:** [Par ordenado](#gl-par-ordenado), [Par de Kuratowski](#gl-par-kuratowski).

---

## Unión {#gl-union}

**Idea.** El conjunto formado por los elementos que pertenecen a uno u otro de dos conjuntos.

**En este tratado.**

$$
A\cup B:=\bigcup\{A,B\},
$$

de modo que

$$
x\in A\cup B
\iff
(x\in A\lor x\in B).
$$

**En el Tratado:** [Definición 0.2.9 — Unión binaria](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-union-binaria).

**Véase también:** [Intersección](#gl-interseccion), [Par no ordenado](#gl-par-no-ordenado).

---

## ZF {#gl-zf}

**Idea.** La teoría axiomática de conjuntos de Zermelo–Fraenkel que sirve como suelo conjuntista del tratado.

**En este tratado.** ZF, junto con lógica clásica de primer orden con igualdad, constituye el fundamento ambiente. Los axiomas no se cuentan como teoremas internos. El axioma de elección no se presupone ni se utiliza silenciosamente.

**En el Tratado:** [§0.1.1 — Inventario axiomático](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-zf).

**Véase también:** [Lógica clásica](#gl-logica-clasica), [Separación restringida](#gl-separacion-restringida), [Extensionalidad](#gl-extensionalidad).

---

::: {.callout-note title="Glosario vivo"}
Las próximas entradas se incorporarán al mismo ritmo que el Tratado. La siguiente publicación, **§0.7 — Órdenes**, añadirá el vocabulario correspondiente a preórdenes, órdenes parciales y totales, orden estricto, cotas, máximo, mínimo, supremo e ínfimo.
:::
