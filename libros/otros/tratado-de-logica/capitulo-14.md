---
title: Capítulo 14 — Relaciones, productos y funciones
status: published
draft: false
book-id: MA-BOK-0014
editorial-project: TLOG
date-modified: '2026-10-11'
license: GFDL-1.3-or-later
areas:
- fundamentos
level: avanzado
topics:
- logica
number-sections: false
content-id: MA-BCH-0216
content-type: book-chapter
source-id: TLOG-CH14-0001
prerequisites:
- MA-BCH-0211
- MA-BCH-0214
- MA-BCH-0215
related:
- MA-BOK-0014
source-sha256: f56dd2e5bfb9659dba88cb325013e3e3a3bb282fee9eb6109931fff08fe2ebd6
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 13](capitulo-13.md) · [Capítulo 15 →](capitulo-15.md)

## 14.0. Del conjunto no ordenado a la codificación de relaciones

Los capítulos 12–13 establecieron la teoría objeto $\mathsf{ZF}_{\mathrm{obj}}$ sobre la **firma pura** $\tau_{\in}$: su único símbolo extralógico es la pertenencia binaria; la igualdad es lógica. Se han obtenido, mediante axiomas y demostraciones internas, par no ordenado, singleton, unión, potencia, separación y operaciones definicionales. En este capítulo construimos **pares ordenados como conjuntos**, productos cartesianos y relaciones binarias como subconjuntos de productos. Las funciones, composiciones funcionales y aplicaciones inversas se reservarán para `CH14-M02`.

**Disciplina de niveles.** Una expresión familiar $\langle a,b\rangle$ no es un término primitivo de $\tau_{\in}$. En cada enunciado objeto es la abreviación eliminable de una gráfica con valor único; $\mathsf{ZF}_{\mathrm{obj}}\vdash\varphi$ significa existencia de una derivación desde $\operatorname{Ax}_{\mathsf{ZF}}$, y no que $\varphi$ sea un axioma de la metateoría $\mathsf M_{\mathrm{ext}}$. Ninguna construcción emplea AC ni BPI.

**Procedencia:** resultados reconstruidos internamente a partir de `TLOG-SRC-0002`, `TLOG-SRC-0003` y del control conjuntista `TLOG-SRC-00011` ya registrados. No se atribuye cotejo nuevo de páginas ni importación de pruebas.

## 14.1. Regla de formación de códigos de par ordenado

### Convención 14.1.1 — Par ordenado como descripción interna y no como primitivo {#tlog-cnv-00019}

Para $a,b$ objetos, **definiremos** $\langle a,b\rangle$ por el código de Kuratowski
$$
\langle a,b\rangle:=\bigl\{\{a\},\{a,b\}\bigr\}.
$$
El lado derecho tiene significado por dos aplicaciones finitas de la operación par ya justificada (§13.3–§13.4). No denota, todavía, una función primitiva de dos argumentos. Es esencial distinguirlo de $\{a,b\}$, que no conserva el orden.

**Regla de expansión:** toda fórmula que contenga $p\doteq\langle a,b\rangle$ será reemplazada por el grafo puro $\Delta_K(p,a,b)$ de §14.2, con renombrado alfa previo de las variables auxiliares. El empleo de $=$ para igualdad legible entre códigos no sustituye a $\doteq$ en la fórmula objeto expandida.

## 14.2. Fórmula gráfica del código de Kuratowski

### Definición 14.2.1 — Gráfica pura del par ordenado {#tlog-def-00073}

Sean $\operatorname{Sing}(s,a)$ y $\operatorname{Pair}(t,a,b)$ las fórmulas **puras** caracterizadoras de singleton y par no ordenado en §13.4. Definimos, con $s,t$ frescas,
$$
\boxed{\Delta_K(p,a,b):\equiv\exists s\exists t\,[\operatorname{Sing}(s,a)\land\operatorname{Pair}(t,a,b)\land\operatorname{Pair}(p,s,t)].}
$$
Cada símbolo `Sing` o `Pair` representa su expansión en $\in,\doteq$, no un predicado nuevo del lenguaje. Las variables $s,t$ no aparecen libres en el contexto, ni son capturadas por los vinculantes de la fórmula que recibe la macro. La expresión $p\doteq\langle a,b\rangle$ nombra esta descripción y ninguna otra.

## 14.3. Existencia y unicidad de pares ordenados

### Proposición 14.3.1 — Totalidad y unicidad del constructor codificado {#tlog-pro-00051}

En la teoría objeto vale el enunciado universal, entendido tras expansión de la macro:
$$
\boxed{\mathsf{ZF}_{\mathrm{obj}}\vdash\forall a\forall b\exists!p\,\Delta_K(p,a,b).}
$$
**Demostración.** Para $a,b$, el teorema del par no ordenado y su caso diagonal dan **únicos** $s=\{a\}$ y $t=\{a,b\}$. Una tercera aplicación del mismo teorema da el único conjunto $p=\{s,t\}$. Sustituyendo los tres testimonios en $\Delta_K$ se obtiene existencia. Si $p,p'$ satisfacen la gráfica con testigos $s,t$ y $s',t'$, la unicidad de los gráficos anteriores implica $s=s'$, $t=t'$ y, por unicidad extensional del par, $p=p'$. La prueba utiliza una cantidad **finita** de testigos existenciales, sin función de elección y sin afirmar que hay una función externa definida sobre todos los conjuntos. Se universaliza sólo después de descargar los parámetros. $\square$

## 14.4. Extracción extensional de las coordenadas

### Lema 14.4.1 — Intersección y unión internas de un par ordenado {#tlog-lem-00041}

Para $p=\langle a,b\rangle$, se cumplen los dos enunciados internos
$$
\boxed{p\ne\varnothing,\qquad \bigcap p=\{a\},\qquad \bigcup p=\{a,b\}.}
$$
Aquí $\bigcap p$ es legítima **porque** $\{a\}\in p$, de modo que $p\ne\varnothing$.

**Demostración.** Del gráfico de §14.2 se obtiene $p=\{\{a\},\{a,b\}\}$. El primer conjunto indicado es miembro de $p$, y ambos miembros contienen $a$; por tanto $a\in\bigcap p$. Si $z\in\bigcap p$, entonces $z\in\{a\}$, pues $\{a\}\in p$; así $z=a$. Se obtiene $\bigcap p=\{a\}$ por extensionalidad. Para la unión, $z\in\bigcup p$ equivale a $z\in\{a\}\lor z\in\{a,b\}$, es decir, $z=a\lor z=b$; nuevamente extensionalidad entrega $\bigcup p=\{a,b\}$. El argumento comprende el caso degenerado $a=b$, donde $p=\{\{a\}\}$. $\square$

## 14.5. Identidad característica del par ordenado

### Metateorema 14.5.1 — Teorema de identidad de Kuratowski en ZF objeto {#tlog-mth-00056}

Para cualesquiera $a,b,c,d$ la teoría objeto demuestra, con todas las macros eliminadas,
$$
\boxed{\langle a,b\rangle=\langle c,d\rangle\iff (a\doteq c\land b\doteq d).}
$$
**Demostración.** La dirección de derecha a izquierda es la congruencia de las descripciones únicas de §14.3. Supongamos la igualdad de códigos y llamemos $p$ al conjunto común. Por §14.4, $\bigcap p=\{a\}=\{c\}$, y la ley de singletons de §13.5 implica $a=c$. Por la unión de §14.4, $\{a,b\}=\bigcup p=\{a,d\}$. Si $b=a$, entonces el conjunto izquierdo es $\{a\}$; en consecuencia $d\in\{a,d\}=\{a\}$, y $d=a=b$. Si $b\ne a$, la pertenencia $b\in\{a,b\}=\{a,d\}$ fuerza $b=d$. Por eliminación de casos clásica se obtiene $b=d$. La conclusión se universaliza y se expresa en la signatura original por la traducción de los grafos $\Delta_K$; no se invoca una función primitiva de par ordenado. $\square$

**Nota de tipado:** esta ley se formula sobre los **conjuntos-código**. No identifica por definición los pares ordenados con los pares no ordenados ni presupone un producto cartesiano.

## 14.6. Descripción del producto cartesiano

### Definición 14.6.1 — Fórmula de producto con cota explícita {#tlog-def-00074}

Dados los conjuntos $A,B$, escribamos $U:=A\cup B$ y $C:=\mathcal P(\mathcal P(U))$, cuyas existencias fueron demostradas en el Capítulo 13. Para un posible producto $Q$, definimos la fórmula de gráfica
$$
\boxed{\begin{aligned}
\Delta_{\times}(Q,A,B):\equiv\;&\forall p\,[p\in Q\leftrightarrow\\
&\quad(p\in C\land\exists a\in A\,\exists b\in B\,\Delta_K(p,a,b))].
\end{aligned}}
$$
Todas las apariciones de $U,C$, de las pertenencias acotadas y de $\Delta_K$ se **eliminan** por sus grafos puros con nombres auxiliares frescos. La cota $C$ no es meramente editorial: permite obtener $Q$ por separación sin comprensión irrestricta. Una vez demostrada la unicidad, denotaremos este $Q$ por $A\times B$.

## 14.7. Existencia del producto cartesiano en la teoría objeto

### Proposición 14.7.1 — Existencia y unicidad de $A\times B$, sin elección {#tlog-pro-00052}

La teoría objeto demuestra
$$
\boxed{\forall A\forall B\,\exists!Q\,\Delta_{\times}(Q,A,B)}
$$
y el objeto así construido satisface
$$
\boxed{\langle a,b\rangle\in A\times B\iff(a\in A\land b\in B).}
$$
**Demostración.** Sea $U=A\cup B$ y $C=\mathcal P(\mathcal P(U))$. Si $a\in A$ y $b\in B$, entonces $a,b\in U$, por lo que $\{a\}\subseteq U$ y $\{a,b\}\subseteq U$. Los dos miembros de $p=\langle a,b\rangle$ pertenecen a $\mathcal P(U)$, así que $p\subseteq\mathcal P(U)$ y $p\in C$. La **instancia de separación** en el conjunto $C$, aplicada a $\exists a\in A\exists b\in B\Delta_K(p,a,b)$, forma el conjunto $Q$ de todos los códigos correspondientes, con parámetros $A,B$. La unicidad de $Q$ sigue de extensionalidad; la equivalencia de membresía se obtiene desplegando la instancia y usando la cota que se acaba de probar. Para la dirección inversa, si $\langle a,b\rangle\in Q$, existen $a'\in A,b'\in B$ con el mismo código. §14.5 fuerza $a=a',b=b'$, y por tanto $a\in A,b\in B$. Todas las operaciones usadas son pares, potencia y separación ya justificados, y no se elige simultáneamente un miembro de cada conjunto de una familia. $\square$

**Cota formal útil:** $A\times B\subseteq \mathcal P(\mathcal P(A\cup B))$. Se mantiene incluso cuando cualquiera de los factores es vacío.

## 14.8. Leyes elementales del producto

### Proposición 14.8.1 — Vacío, no vacío, monotonía y recuperación de factores {#tlog-pro-00053}

Como abreviaciones de sentencias demostrables en $\mathsf{ZF}_{\mathrm{obj}}$, obtenemos
$$
\begin{aligned}
A\times B=\varnothing&\iff(A=\varnothing\lor B=\varnothing),\\
(A\subseteq A'\land B\subseteq B')&\Longrightarrow A\times B\subseteq A'\times B',\\
\{a\}\times\{b\}&=\{\langle a,b\rangle\},\\
A\times(B\cup C)&=(A\times B)\cup(A\times C).
\end{aligned}
$$
**Demostración.** Si un factor es vacío, la caracterización de §14.7 excluye cualquier miembro del producto; extensionalidad lo iguala a $\varnothing$. Recíprocamente, si ambos factores son no vacíos, la eliminación de **dos** existenciales proporciona $a\in A,b\in B$; §14.7 da un miembro del producto, que por tanto no es vacío. Son dos testigos de una misma prueba finita, no una función de elección sobre una familia arbitraria. La monotonía resulta de transportar las dos inclusiones a la condición de membresía. Para los singletons, los únicos valores admisibles son $a,b$, por §13.5 y §14.5. Para la distributividad, las condiciones $a\in A\land (b\in B\lor b\in C)$ y $(a\in A\land b\in B)\lor(a\in A\land b\in C)$ son lógicamente equivalentes; todo elemento es un código de par, y extensionalidad concluye. $\square$

**Frontera:** no se identifica $A\times B$ con $B\times A$ ni con $\{A,B\}$; el orden es relevante.

## 14.9. Relaciones binarias como objetos conjuntistas

### Definición 14.9.1 — Relación tipada $R\subseteq A\times B$ y relación sin factores declarados {#tlog-def-00075}

Definimos la relación binaria **entre conjuntos declarados** $A,B$ como un conjunto $R$ con $R\subseteq A\times B$. Escribimos
$$
a\mathrel{R}b\quad:\Longleftrightarrow\quad\langle a,b\rangle\in R,
$$
siempre como **macro objeto** traducible mediante la gráfica $\Delta_K$. Por separado, $\operatorname{Rel}(R)$ expresa
$$
\boxed{\forall p\,[p\in R\to\exists a\exists b\,\Delta_K(p,a,b)]},
$$
propiedad de ser un conjunto compuesto exclusivamente de pares ordenados, sin elegir $A,B$ a priori. La segunda noción no convierte a la totalidad de las relaciones en un conjunto universal; es un predicado objeto sobre un conjunto variable $R$.

Se distingue **relación como conjunto de códigos** de **relación definible por fórmula**. Una fórmula $\theta(a,b,\bar p)$ sólo produce una relación-objeto tras probar un conjunto que acote sus pares; el producto $A\times B$ suministrará dicha cota.

## 14.10. Construcción de relaciones por separación

### Proposición 14.10.1 — Relación de extensión para una condición sobre un producto {#tlog-pro-00054}

Sea $\theta(a,b,A,B,\bar p)$ una **fórmula fija** de la firma pura, sin captura al insertar sus parámetros. En ZF objeto existe un único conjunto $R_\theta(A,B;\bar p)$ tal que
$$
\boxed{\begin{aligned}
R_\theta\subseteq A\times B,\qquad
\langle a,b\rangle\in R_\theta\iff&(a\in A\land b\in B\\
&\land\theta(a,b,A,B,\bar p)).
\end{aligned}}
$$
**Demostración.** §14.7 ya construye el conjunto $A\times B$. Para un código variable $p$, formamos la matriz pura
$$
\exists a\exists b\,[a\in A\land b\in B\land\Delta_K(p,a,b)\land\theta(a,b,A,B,\bar p)].
$$
La separación **sobre $A\times B$** entrega el subconjunto $R_\theta$. Si $p=\langle a,b\rangle$, §14.5 asegura unicidad de las coordenadas, por lo que la matriz equivale a la condición enunciada. Extensionalidad asegura unicidad del conjunto separado. Este procedimiento es una **familia esquemática de derivaciones**, una para cada $\theta$, no una función objeto que reciba fórmulas como argumentos. $\square$

**Observación:** si $R\subseteq A\times B$, la fórmula $\theta(a,b;R):\equiv\langle a,b\rangle\in R$ recupera exactamente $R$ por separación, con el parámetro conjunto $R$. Esto no afirma que todo $R$ sea definible *sin parámetros*.

## 14.11. Dominio y recorrido de una relación

### Definición 14.11.1 — Dominios y recorridos por separación sobre una cota uniforme {#tlog-def-00076}

Para cualquier $R$ que satisfaga $\operatorname{Rel}(R)$, el conjunto $D_R:=\bigcup\bigcup R$ existe por dos uniones sucesivas, aun si $R=\varnothing$. Fijamos los grafos
$$
\begin{aligned}
\operatorname{dom}(R)&:=\{a\in D_R:\exists p\in R\,\exists b\,\Delta_K(p,a,b)\},\\
\operatorname{ran}(R)&:=\{b\in D_R:\exists p\in R\,\exists a\,\Delta_K(p,a,b)\}.
\end{aligned}
$$
Aquí $\operatorname{dom}$ y $\operatorname{ran}$ son **macros con guarda $\operatorname{Rel}(R)$**, no funciones unarias totales primitivas en la firma pura. Su existencia y acotación exacta se prueban en §14.12. Los testigos del código son únicos, y el uso de cuantificadores se efectúa con variables frescas.

## 14.12. Existencia y tipado de dominio y recorrido

### Proposición 14.12.1 — Caracterización de coordenadas y cotas de una relación {#tlog-pro-00055}

Para $\operatorname{Rel}(R)$, existen únicos los conjuntos anteriores, y son caracterizados por
$$
\boxed{\begin{aligned}
a\in\operatorname{dom}(R)&\iff\exists b\ (\langle a,b\rangle\in R),\\
b\in\operatorname{ran}(R)&\iff\exists a\ (\langle a,b\rangle\in R).
\end{aligned}}
$$
Si además $R\subseteq A\times B$, entonces $\operatorname{dom}(R)\subseteq A$ y $\operatorname{ran}(R)\subseteq B$. Para $R=\varnothing$, ambos conjuntos son vacíos.

**Demostración.** Si $p=\langle a,b\rangle\in R$, entonces $\{a\}\in p$ y $a\in\{a\}$, de donde $a\in\bigcup p\subseteq\bigcup\bigcup R=D_R$. Del mismo modo, $\{a,b\}\in p$ y $b\in\{a,b\}$, así que $b\in D_R$. Por tanto las coordenadas de **cualquier** par de $R$ cumplen las condiciones de separación que definen dominio y recorrido. A la inversa, una pertenencia a los conjuntos separados incluye explícitamente la existencia de un $p\in R$ que es el código de un par con la coordenada señalada, luego se obtiene la fórmula de la derecha. Separación da existencia; extensionalidad, unicidad. Bajo $R\subseteq A\times B$, §14.7 transforma cada pertenencia $\langle a,b\rangle\in R$ en $a\in A,b\in B$, de donde las cotas. Si $R=\varnothing$ no hay códigos y las dos matrices son falsas. $\square$

Esta construcción usa sólo conjuntos $R$, $D_R$ y separación; no emplea selección arbitraria de una segunda coordenada a partir de la primera.

## 14.13. Restricción de relaciones a subproductos

### Proposición 14.13.1 — Restricción acotada y estabilidad de las coordenadas {#tlog-pro-00056}

Para una relación $R\subseteq A\times B$ y conjuntos $A'\subseteq A,B'\subseteq B$, existe la relación restringida
$$
\boxed{R\upharpoonright(A'\times B'):=R\cap(A'\times B')},
$$
que satisface
$$
\begin{aligned}
\langle a,b\rangle\in R\upharpoonright(A'\times B')&\iff(\langle a,b\rangle\in R\land a\in A'\land b\in B'),\\
\operatorname{dom}(R\upharpoonright(A'\times B'))&\subseteq\operatorname{dom}(R)\cap A',\\
\operatorname{ran}(R\upharpoonright(A'\times B'))&\subseteq\operatorname{ran}(R)\cap B'.
\end{aligned}
$$
**Demostración.** Los dos factores $A',B'$ son conjuntos, por lo que su producto existe. §13.13 construye la intersección $R\cap(A'\times B')$; es subconjunto de ambos, y por ende un conjunto de códigos de pares. La caracterización por membresía del producto da la primera identidad. Si $a$ está en el dominio restringido, una pareja $\langle a,b\rangle$ pertenece al conjunto restringido; por tanto pertenece a $R$ y satisface $a\in A'$. §14.12 da $a\in\operatorname{dom}(R)$, lo cual prueba la inclusión. El recorrido se trata simétricamente. **No** se afirma igualdad para los dominios restringidos, pues pueden desaparecer todas las parejas de algún $a$ cuando se restringe la segunda coordenada. $\square$

## 14.14. Identidad extensional de relaciones

### Proposición 14.14.1 — Dos relaciones son iguales exactamente cuando tienen los mismos pares {#tlog-pro-00057}

Para $\operatorname{Rel}(R)\land\operatorname{Rel}(S)$, ZF objeto demuestra
$$
\boxed{R=S\iff\forall a\forall b\,[\langle a,b\rangle\in R\leftrightarrow\langle a,b\rangle\in S].}
$$
**Demostración.** Si $R=S$, la bicondicionalidad es sustitución lógica de iguales. A la inversa, sea $p\in R$. Por $\operatorname{Rel}(R)$, existen $a,b$ con $p=\langle a,b\rangle$. La hipótesis universal da $\langle a,b\rangle\in S$, luego $p\in S$. El argumento es simétrico para $S\subseteq R$. Extensionalidad concluye. La hipótesis $\operatorname{Rel}$ es sustantiva: si los conjuntos incluyeran objetos que no son pares ordenados, la comparación de membresía exclusivamente sobre códigos no detectaría esas diferencias. $\square$

## 14.15. Conservatividad de los nuevos nombres de operación

### Metateorema 14.15.1 — Eliminación de pares ordenados y productos cartesianos {#tlog-mth-00057}

Sea $L_0=\tau_\in$. Formemos $L_1$ incorporando un símbolo binario $k$ con su **única** ecuación definitoria $\forall a\forall b\,\Delta_K(k(a,b),a,b)$. Formemos después $L_2$ añadiendo un símbolo binario $\operatorname{prod}$ con la ecuación de gráfica $\forall A\forall B\,\Delta_{\times}(\operatorname{prod}(A,B),A,B)$, formulada en $L_1$ o, equivalentemente, en el lenguaje puro por sustitución de $\Delta_K$. Entonces:
$$
\boxed{\text{Para toda fórmula pura }\varphi,\quad T_2\vdash\varphi\iff\mathsf{ZF}_{\mathrm{obj}}\vdash\varphi.}
$$
**Demostración metateórica.** §14.3 demuestra total y únicamente el valor de $k$ para cada par de parámetros. §14.7 demuestra total y únicamente el valor de $\operatorname{prod}$ para cada par de conjuntos. El orden de introducción es finito y acíclico. Aplicamos el metateorema general §13.14 ([TLOG-MTH-00054](capitulo-13.md#tlog-mth-00054)) a esas **dos** funciones definibles: cada término nuevo se traduce por el correspondiente grafo con nombres frescos, y una prueba de una fórmula pura en la extensión no crea teoremas adicionales de la firma primitiva. La existencia de expansiones semánticas utiliza unicidad, no AC. Los predicados $\operatorname{Rel}(R)$, la relación de pertenencia $aRb$ y $\operatorname{dom},\operatorname{ran}$ permanecen **macros con hipótesis de uso**, no nuevas funciones unarias globales sin totalización explícita. $\square$

## 14.16. Frontera hacia funciones como conjuntos de pares

### Corolario 14.16.1 — Infraestructura relacional construida sin axioma de elección {#tlog-cor-00016}

Las pruebas de §§14.1–14.15 fijan, dentro de ZF objeto, una codificación fiel de pares ordenados, conjuntos producto $A\times B$, relaciones binarias como subconjuntos de esos productos, relaciones definibles relativas a dominios dados, dominios, recorridos y restricciones. Los símbolos nuevos son grafos eliminables y **ninguna relación funcional ha sido todavía identificada con una aplicación total**. Esto último requerirá en `CH14-M02` demostrar el criterio de unicidad de segundo componente, fijar dominio/codominio y construir imágenes, composiciones e inversas bajo las condiciones correctas.

No se añade $\mathsf{AC}$, $\mathsf{BPI}$, un axioma de comprensión irrestricta ni un nuevo primitivo de ZF. El corpus permanece en $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ clásica sin elección, distinto de $\mathsf{ZF}_{\mathrm{obj}}$. La derivabilidad objeto no implica haber demostrado la consistencia de la teoría ni haberla formalizado en Lean. $\square$

## 14.17. Estado del microtramo y obligaciones de cierre del capítulo

`TLOG-CH14-M01` cierra matemáticamente la **primera** unidad sobre productos y relaciones. `TLOG-CH14-0001` permanece en `PARTIAL-CLOSURE`: la arquitectura exige todavía construir funciones como conjuntos de pares, composición y aplicaciones inversas en sus ámbitos válidos. Los resultados tienen identificadores estables, dependencias directas explícitas y localizadores §§14.1–14.16. Las obras de Enderton, Rautenberg y el control SEP conservan exclusivamente el alcance de consulta previamente registrado, sin atribuir cotejos nuevos. La publicación web continúa pendiente.

**Próximo microtramo:** `TLOG-CH14-M02 — Funciones como relaciones unívocas, evaluación, composición e inversas`.


## 14.18. Funciones como grafos, no como símbolos primitivos

### Convención 14.18.1 — Grafo funcional y flecha tipada {#tlog-cnv-00020}

Llamaremos **función conjuntista** a una relación que asigna a cada elemento de *su dominio* exactamente un valor. Una función como conjunto es, por tanto, su **grafo**; no es una operación extralógica nueva de la signatura primitiva de ZF. Escribiremos separadamente «$f:A\to B$» para el dato **tipado** de una función cuyo dominio es $A$ y cuyos valores pertenecen al codominio declarado $B$. Este dato incluye la elección *de un conjunto codominio especificado*, no una función de elección para una familia arbitraria.

El grafo $f$ determina sin ambigüedad $\operatorname{dom}(f)$ y $\operatorname{ran}(f)$, pero **no determina por sí solo el codominio** $B$: un mismo conjunto de pares puede ser tipado como $A\to B$ y como $A\to C$ cuando su recorrido está contenido en ambos. Las palabras «inyectiva», «sobreyectiva» y «biyectiva» recibirán sus guardas explícitas; particularmente, «sobreyectiva» requiere un codominio declarado. Cada símbolo de aplicación, imagen y composición que sigue es una abreviación eliminable conforme al metateorema §13.14.

## 14.19. Predicado puro de funcionalidad

### Definición 14.19.1 — Función parcial y aplicación total entre conjuntos {#tlog-def-00077}

Usamos el predicado de relación $\operatorname{Rel}(f)$ de §14.9 y fijamos la fórmula de pura pertenencia

$$
\operatorname{Fun}(f):\Longleftrightarrow
\operatorname{Rel}(f)\ \land\
\forall x\forall y\forall z\,
[\langle x,y\rangle\in f\land\langle x,z\rangle\in f\to y\doteq z].
$$

De igual modo, la inscripción $f:A\to B$ significa el predicado conjuntivo

$$
\operatorname{App}(f,A,B):\Longleftrightarrow
\operatorname{Fun}(f)\land f\subseteq A\times B
\land \operatorname{dom}(f)\doteq A.
$$

La pertenencia de códigos, el producto, el dominio y los cuantificadores acotados se expanden a fórmulas de $\tau_\in$, con auxiliares frescos y sin captura. En la misma lengua, $\operatorname{Inj}(f)$ es la fórmula

$$
\operatorname{Fun}(f)\land
\forall x\forall x'\forall y\,
(\langle x,y\rangle\in f\land\langle x',y\rangle\in f\to x\doteq x').
$$

Para una flecha tipada $f:A\to B$, la sobreyectividad es $\operatorname{ran}(f)\doteq B$, y la biyectividad es la conjunción de esa propiedad con $\operatorname{Inj}(f)$. Ninguna de estas fórmulas cuantifica sobre una clase de todas las funciones como si fuera un conjunto.

## 14.20. Unicidad de valor y caracterización tipada

### Proposición 14.20.1 — Caracterización de la funcionalidad por testigos únicos {#tlog-pro-00058}

En ZF objeto se demuestra, para todo $f$ con $\operatorname{Fun}(f)$,

$$
\boxed{\forall x\in\operatorname{dom}(f)\ \exists!y\,
(\langle x,y\rangle\in f).}
$$

Recíprocamente, para todo $R$ con $\operatorname{Rel}(R)$, si cada $x\in\operatorname{dom}(R)$ tiene a lo sumo un valor $y$, entonces $\operatorname{Fun}(R)$; la existencia de valores sobre el dominio ya es parte de la definición de $\operatorname{dom}$.

**Demostración objeto.** Si $x\in\operatorname{dom}(f)$, §14.12 entrega un $y$ con $\langle x,y\rangle\in f$. Para $y,z$ con esa misma primera coordenada, la cláusula definitoria de $\operatorname{Fun}(f)$ da $y=z$; por ello el testigo es único. Inversamente, si dos pares $\langle x,y\rangle,\langle x,z\rangle$ pertenecen a $R$, la existencia del primero implica $x\in\operatorname{dom}(R)$. Aplicando la unicidad local se obtiene $y=z$. La guarda $\operatorname{Rel}(R)$ completa la definición de $\operatorname{Fun}(R)$. Las cuantificaciones de testigos se efectúan dentro de condicionales con parámetros y sólo al final se toma clausura universal. $\square$

## 14.21. Evaluación como descripción única condicionada

### Definición 14.21.1 — Valor $f(x)$ y su dominio exacto de impresión {#tlog-def-00078}

Bajo la **guarda** $\operatorname{Fun}(f)\land x\in\operatorname{dom}(f)$, se permite la expresión $f(x)$ para el único $y$ con $\langle x,y\rangle\in f$. La escritura

$$
\boxed{f(x)=y\quad:\Longleftrightarrow\quad \langle x,y\rangle\in f}
$$

se autoriza solamente bajo dicha guarda. Si $x\notin\operatorname{dom}(f)$, no hay valor: **no** se define silenciosamente $f(x)=\varnothing$. El gráfico original de aplicación $\langle x,y\rangle\in f$ es la expresión segura incluso en fórmulas con hipótesis aún no descargadas. Un símbolo funcional total de una extensión definicional sólo podría añadirse después de una **totalización expresa** fuera de la guarda, usando §13.31, lo cual sería otra convención.

## 14.22. Tipado, imagen y casos extremos

### Proposición 14.22.1 — Dominio, recorrido y codominio declarado {#tlog-pro-00059}

Para cualesquiera $f,A,B$,

$$
\boxed{f:A\to B\quad\Longleftrightarrow\quad
\operatorname{Fun}(f)\land
\operatorname{dom}(f)=A\land\operatorname{ran}(f)\subseteq B.}
$$

Asimismo, si $f:A\to B$, $A=\varnothing$ implica $f=\varnothing$. Si $B=\varnothing$, entonces $A=\varnothing$ y $f=\varnothing$. La flecha vacía $\varnothing:\varnothing\to B$ existe para **todo** conjunto $B$, sin requerir $B\ne\varnothing$.

**Demostración.** La definición de §14.19 exige $f\subseteq A\times B$, y §14.12 dice que la inclusión fuerza $\operatorname{dom}(f)\subseteq A$, $\operatorname{ran}(f)\subseteq B$. La igualdad de dominios da la condición derecha. Para la recíproca, cualquier miembro $p\in f$ es $\langle x,y\rangle$ por $\operatorname{Fun}(f)$; las hipótesis $x\in\operatorname{dom}(f)=A$ y $y\in\operatorname{ran}(f)\subseteq B$ garantizan $p\in A\times B$, y por extensionalidad de inclusiones se obtiene $f\subseteq A\times B$. Si $A$ o $B$ es vacío, §14.8 da $A\times B=\varnothing$, y entonces $f=\varnothing$; la igualdad del dominio fuerza $A=\varnothing$ en el segundo caso. En el primero, el grafo vacío es funcional, está contenido en el producto vacío y tiene dominio vacío, para cualquier $B$. $\square$

## 14.23. El conjunto de todas las aplicaciones entre dos conjuntos

### Definición 14.23.1 — Espacio funcional $B^A$ como subconjunto de una potencia {#tlog-def-00079}

Dado que $A\times B$ es un conjunto, también lo es su potencia. Definimos el gráfico único del **conjunto funcional**

$$
\boxed{B^A:=\{f\in\mathcal P(A\times B):\operatorname{App}(f,A,B)\}.}
$$

La matriz $\operatorname{App}$ se expande a una fórmula de pertenencia y se aplica separación a $\mathcal P(A\times B)$. No designa una función universal $B^{\mathsf V}$, ni se presupone que el espacio funcional sea no vacío: esto depende de $A,B$, como se demostrará en §14.24. El superíndice $A$ es aquí un conjunto-dominio, no un ordinal ni una cardinalidad.

## 14.24. Existencia y condiciones de no vacuidad del espacio funcional

### Proposición 14.24.1 — Funciones como elementos de una potencia y casos vacíos {#tlog-pro-00060}

ZF objeto demuestra $f\in B^A\iff f:A\to B$ y

$$
\boxed{B^A\ne\varnothing\quad\Longleftrightarrow\quad
(A=\varnothing\ \lor\ B\ne\varnothing).}
$$

En particular, $\varnothing^\varnothing=\{\varnothing\}$ y, si $A\ne\varnothing$, entonces $\varnothing^A=\varnothing$.

**Demostración.** El bicondicional inicial se sigue de la separación que define $B^A$: la inclusión $f\subseteq A\times B$ ya forma parte de $\operatorname{App}$. Si $A=\varnothing$, el grafo vacío es una flecha total por §14.22 y constituye un elemento de $B^A$. Si $B\ne\varnothing$, la eliminación de un existencial da un $b\in B$. Por §14.10, la relación $f_b:=\{\langle a,b\rangle:a\in A\}$ existe por separación sobre $A\times B$ y tiene exactamente un valor por cada $a\in A$; por tanto $f_b\in B^A$. No hay elección sobre una familia: se usa **un solo** testigo $b$. Recíprocamente, si $f\in B^A$ y $A\ne\varnothing$, tomamos $a\in A$. La totalidad de $f$ da $b\in B$, así que $B\ne\varnothing$. Para $A=B=\varnothing$, el único subconjunto del producto vacío es el vacío y éste es una función, lo que da el singleton. $\square$

## 14.25. Grafo conjuntista de una operación definida por fórmula

### Proposición 14.25.1 — Del reemplazo funcional a un conjunto de pares {#tlog-pro-00061}

Sea $\Theta(x,y,\bar p)$ una fórmula fija de pertenencia, con variables auxiliares frescas, y supongamos la **premisa objeto** de funcionalidad sobre el dominio

$$
F_\Theta(a,\bar p)\;:\Longleftrightarrow\;\forall x\in a\,\exists!y\,\Theta(x,y,\bar p),
$$

con la guarda $F_\Theta$ de §13.17. Para cada $a,\bar p$ que satisfaga esa guarda, existe un único **grafo funcional** $G_\Theta$ tal que

$$
\boxed{\langle x,y\rangle\in G_\Theta\quad\Longleftrightarrow\quad
x\in a\land\Theta(x,y,\bar p).}
$$

Se tiene $\operatorname{dom}(G_\Theta)=a$ y $\operatorname{ran}(G_\Theta)=\operatorname{Im}_\Theta(a;\bar p)$.

**Demostración.** Por §13.18, reemplazo funcional construye el conjunto exacto $M:=\operatorname{Im}_\Theta(a;\bar p)$ de los valores $y$ para $x\in a$. Formamos el conjunto $a\times M$ según §14.7. Aplicando separación al producto con la matriz pura

$$
\exists x\in a\,\exists y\in M\,
(\Delta_K(q,x,y)\land\Theta(x,y,\bar p))
$$

obtenemos un conjunto $G_\Theta\subseteq a\times M$. La identidad de Kuratowski garantiza que un código no representa dos pares distintos; la unicidad de $y$ bajo $\Theta$ asegura la univocidad de $G_\Theta$. La existencia bajo $\Theta$ para cada $x\in a$ da el dominio exactamente $a$. Los valores que aparecen en el grafo son precisamente los que definen $M$, por doble inclusión y extensionalidad. La cota $a\times M$ evita una comprensión no acotada y no necesita elección. $\square$

Si ya se dispone de un conjunto cota $B$ con $\forall x\in a\,\forall y(\Theta(x,y,\bar p)\to y\in B)$, basta **separación sobre $a\times B$**, sin reemplazo, como caso particular.

## 14.26. Imagen directa e imagen inversa de una función

### Definición 14.26.1 — Imágenes de subconjuntos, con preimagen guardada {#tlog-def-00080}

Para $\operatorname{Fun}(f)$ y conjuntos arbitrarios $S,T$, definimos, siempre por separación, las expresiones

$$
\begin{aligned}
f[S]&:=\{y\in\operatorname{ran}(f):\exists x\in S\,(\langle x,y\rangle\in f)\},\\
f^{-1}[T]&:=\{x\in\operatorname{dom}(f):\exists y\in T\,(\langle x,y\rangle\in f)\}.
\end{aligned}
$$

El segundo objeto es **preimagen de un conjunto**, no el grafo de una función inversa. En particular, $f[S]$ toma automáticamente sólo los puntos de $S\cap\operatorname{dom}(f)$; no requiere $S\subseteq\operatorname{dom}(f)$. En la definición de $f^{-1}[T]$, la existencia de valor es automática por estar acotada al dominio. Las dos operaciones están definidas bajo la guarda $\operatorname{Fun}(f)$, pero sus valores son conjuntos incluso para $S$ y $T$ vacíos.

## 14.27. Cálculo de imágenes y preimágenes

### Proposición 14.27.1 — Álgebra de imagen directa e inversa {#tlog-pro-00062}

Para toda función $f$ y conjuntos $S,T,U,V$, se obtienen los teoremas de pertenencia

$$
\begin{aligned}
f[\varnothing]&=\varnothing,&
f[S\cup T]&=f[S]\cup f[T],\\
f[S\cap T]&\subseteq f[S]\cap f[T],&
f^{-1}[U\cup V]&=f^{-1}[U]\cup f^{-1}[V],\\
f^{-1}[U\cap V]&=f^{-1}[U]\cap f^{-1}[V],&
f^{-1}[\varnothing]&=\varnothing,\\
f[\operatorname{dom}(f)]&=\operatorname{ran}(f),&
f^{-1}[\operatorname{ran}(f)]&=\operatorname{dom}(f).
\end{aligned}
$$

Además, si $\operatorname{Inj}(f)$, se cumple la igualdad $f[S\cap T]=f[S]\cap f[T]$ para cualesquiera $S,T$. La inclusión general puede ser estricta cuando $f$ no es inyectiva.

**Demostración.** Para la unión directa, $y\in f[S\cup T]$ equivale a $\exists x\,(x\in S\lor x\in T)\land\langle x,y\rangle\in f$; la distribución del existencial sobre la disyunción produce pertenencia a $f[S]$ o a $f[T]$. Para la intersección sólo se deduce que el **mismo** testigo $x\in S\cap T$ sirve para ambas imágenes; los testigos extraídos por separado de $f[S]$ y $f[T]$ podrían ser distintos. Bajo inyectividad, si $y=f(x)=f(x')$ con $x\in S,x'\in T$, la inyectividad obliga $x=x'$, y entonces $x\in S\cap T$. Para las preimágenes, dado $x\in\operatorname{dom}(f)$, §14.20 garantiza el **único** valor $y$; por tanto $y\in U\cap V$ equivale a $y\in U\land y\in V$, y la igualdad de conjuntos se sigue de separación y extensionalidad. Las leyes de vacío y de recorrido se obtienen desplegando las matrices correspondientes. No se necesita seleccionar una familia de valores: cada valor está determinado por $f$. $\square$

## 14.28. Identidades y composición de relaciones funcionales

### Definición 14.28.1 — Gráfico identidad y composición relacional acotada {#tlog-def-00081}

Para todo conjunto $A$, el **grafo identidad** es el conjunto
$$
\operatorname{id}_A:=\{p\in A\times A:\exists a\in A\,\Delta_K(p,a,a)\}.
$$
Para cualesquiera relaciones $R,S$ con $\operatorname{Rel}(R)\land\operatorname{Rel}(S)$, la **composición de relaciones** es la separación sobre el conjunto $\operatorname{dom}(R)\times\operatorname{ran}(S)$
$$
\boxed{S\circ R:=\{\langle x,z\rangle:\exists y\,
(\langle x,y\rangle\in R\land\langle y,z\rangle\in S)\}.}
$$

La notación por comprensión entre llaves en la última línea es abreviatura de la instancia de separación **con la cota recién indicada**; no es comprensión irrestricta. Las condiciones sobre $R,S$ son guardas para sus dominios y recorridos. La existencia del grafo identidad usa únicamente $A\times A$ y separación. La composición está definida también cuando alguna relación es vacía; entonces es vacía. No hemos supuesto que $R,S$ sean funciones para construir la relación compuesta.

## 14.29. Totalidad y funcionalidad de una composición

### Proposición 14.29.1 — Dominio exacto de la composición de funciones {#tlog-pro-00063}

Si $\operatorname{Fun}(f)$ y $\operatorname{Fun}(g)$, entonces $\operatorname{Fun}(g\circ f)$ y
$$
\boxed{\operatorname{dom}(g\circ f)=
\{x\in\operatorname{dom}(f):f(x)\in\operatorname{dom}(g)\}.}
$$
En cada $x$ de ese dominio se cumple $(g\circ f)(x)=g(f(x))$, con las guardas de evaluación satisfechas. En particular, si $f:A\to B$ y $g:B\to C$, entonces $g\circ f:A\to C$.

**Demostración.** Por §14.28 la relación compuesta está acotada por $\operatorname{dom}(f)\times\operatorname{ran}(g)$ y todos sus miembros son códigos de pares. Si $\langle x,z\rangle,\langle x,z'\rangle$ pertenecen a $g\circ f$, se obtienen testigos $y,y'$ con $f(x)=y$, $f(x)=y'$, $g(y)=z$ y $g(y')=z'$. La funcionalidad de $f$ da $y=y'$ y la de $g$ da $z=z'$; por ello la composición es una función. Si $x\in\operatorname{dom}(g\circ f)$, la existencia de un par compuesto proporciona $y=f(x)\in\operatorname{dom}(g)$. A la inversa, para $x\in\operatorname{dom}(f)$ con $f(x)\in\operatorname{dom}(g)$, la **eliminación de dos existenciales** entrega los valores únicos $y=f(x)$ y $z=g(y)$, que producen $\langle x,z\rangle\in g\circ f$; no hay selección simultánea sobre una familia. Para las flechas tipadas, cada $f(x)\in B=\operatorname{dom}(g)$, luego el dominio compuesto es todo $A$, y $\operatorname{ran}(g\circ f)\subseteq\operatorname{ran}(g)\subseteq C$. §14.22 completa el tipado. $\square$

**Reserva de tipado:** si sólo sabemos $f:A\to B$ y $g:C\to D$, con $B\not\subseteq C$, la composición aún existe como función **parcial** sobre $\{x\in A:f(x)\in C\}$, pero no se afirma que tenga dominio $A$.

## 14.30. Leyes de identidad y asociatividad

### Proposición 14.30.1 — Leyes del monoide parcial de composición {#tlog-pro-00064}

Para funciones conjuntistas $f,g,h$ arbitrarias (posiblemente de dominio vacío) se tienen las identidades de grafos
$$
\boxed{h\circ(g\circ f)=(h\circ g)\circ f,\quad
\operatorname{id}_{\operatorname{ran}(f)}\circ f=f,
\quad f\circ\operatorname{id}_{\operatorname{dom}(f)}=f.}
$$
Además, $\operatorname{id}_A:A\to A$, y $\operatorname{id}_A$ es inyectiva y sobreyectiva con respecto al codominio $A$.

**Demostración.** La gráfica identidad consta exactamente de los pares $\langle a,a\rangle$ con $a\in A$. Un primer componente $a$ aparece una sola vez, por lo que $\operatorname{id}_A$ es función total, y su recorrido es $A$. Para la asociatividad, desplegar dos veces §14.28 en el lado izquierdo da
$$
\langle x,w\rangle\in h\circ(g\circ f)
\iff\exists y\exists z\,[\langle x,y\rangle\in f\land
\langle y,z\rangle\in g\land\langle z,w\rangle\in h],
$$
tras renombrar los testigos. El lado derecho admite **la misma fórmula**, por mera reagrupación de conjunciones y existenciales, y §14.14 aplica al ser ambos conjuntos de pares. Para la identidad izquierda, $\langle x,z\rangle\in\operatorname{id}_{\operatorname{ran}(f)}\circ f$ equivale a $\exists y(\langle x,y\rangle\in f\land y=z\land y\in\operatorname{ran}(f))$; la última pertenencia es automática cuando aparece un par de $f$, así que la condición equivale a $\langle x,z\rangle\in f$. La identidad derecha se demuestra simétricamente mediante el dominio. No se exige que el conjunto de **todas** las funciones exista: son teoremas universalmente cuantificados sobre grafos conjuntos. $\square$

## 14.31. Conversión de una relación

### Definición 14.31.1 — Relación conversa de un grafo {#tlog-def-00082}

Para $\operatorname{Rel}(R)$ se autoriza la **relación conversa**
$$
\boxed{R^{\smile}:=\{\langle y,x\rangle\in
\operatorname{ran}(R)\times\operatorname{dom}(R):
\langle x,y\rangle\in R\}.}
$$

Se construye por separación sobre el producto indicado, y se tiene $\operatorname{dom}(R^{\smile})=\operatorname{ran}(R)$, $\operatorname{ran}(R^{\smile})=\operatorname{dom}(R)$ y $(R^{\smile})^{\smile}=R$, por el criterio de identidad de pares y extensionalidad. La relación conversa **siempre existe como conjunto**, aun si $R$ no es función. El símbolo $f^{-1}$, **sin corchetes de preimagen**, quedará reservado al caso en que el converso de una función sea también función; por ahora empleamos $f^{\smile}$.

## 14.32. Condición exacta para la inversa funcional

### Proposición 14.32.1 — Converso funcional si y sólo si inyectividad {#tlog-pro-00065}

Para $\operatorname{Fun}(f)$,
$$
\boxed{\operatorname{Fun}(f^{\smile})\quad\Longleftrightarrow\quad
\operatorname{Inj}(f).}
$$
En el caso inyectivo, $f^{\smile}$ es una función total $\operatorname{ran}(f)\to\operatorname{dom}(f)$ y se autoriza escribir $f^{-1}:=f^{\smile}$, con el **dominio de esa notación restringido** por $\operatorname{Inj}(f)$.

**Demostración.** Si $\operatorname{Inj}(f)$, y $\langle y,x\rangle,\langle y,x'\rangle\in f^{\smile}$, entonces $\langle x,y\rangle,\langle x',y\rangle\in f$, por lo que $x=x'$. §14.31 proporciona que todos los elementos de $f^{\smile}$ son pares, de modo que éste es funcional. Su dominio y recorrido son exactamente los intercambiados por §14.31. Recíprocamente, si $f^{\smile}$ es funcional y $f(x)=f(x')=y$, sus dos pares intercambiados tienen el primer componente $y$, de donde la funcionalidad de $f^{\smile}$ implica $x=x'$. En ningún paso se elige un preimagen de una colección arbitraria de fibras: **cada fibra tiene a lo sumo un elemento**. $\square$

Para funciones no inyectivas, $f^{-1}[T]$ (preimagen de conjunto, §14.26) continúa perfectamente definida, pero la expresión de **función inversa** $f^{-1}$ no está autorizada. Las dos operaciones tienen tipos distintos.

## 14.33. Biyectividad y equivalencia de inversas

### Metateorema 14.33.1 — Inversa bilateral y biyectividad relativa al codominio {#tlog-mth-00058}

Sean conjuntos $A,B$ y una función tipada $f:A\to B$. Son equivalentes las condiciones siguientes:

1. $\operatorname{Inj}(f)$ y $\operatorname{ran}(f)=B$.
2. Existe $g:B\to A$ con $g\circ f=\operatorname{id}_A$ y $f\circ g=\operatorname{id}_B$.
3. La relación conversa $f^{\smile}$ es una función $B\to A$ y satisface las mismas dos igualdades.

En este caso $g=f^{\smile}$ es la **única** inversa bilateral, autorizando la notación $f^{-1}:B\to A$. La equivalencia admite $A=B=\varnothing$.

**Demostración.** De (1), §14.32 dice que $f^{\smile}$ es función sobre $\operatorname{ran}(f)=B$ con recorrido $\operatorname{dom}(f)=A$, luego es flecha total $B\to A$. Si $x\in A$, existe un único $y\in B$ con $f(x)=y$; el converso contiene $\langle y,x\rangle$, y la composición $f^{\smile}\circ f$ contiene $\langle x,x\rangle$. Dado que las dos gráficas son funcionales, no contiene otro par de primera coordenada $x$, y por extensionalidad es $\operatorname{id}_A$. Para cada $y\in B=\operatorname{ran}(f)$ hay un $x\in A$ con $f(x)=y$; el mismo argumento da $f\circ f^{\smile}=\operatorname{id}_B$. Así (1) implica (3), y (3) implica trivialmente (2).

Supongamos (2). Para inyectividad, si $f(x)=f(x')$, aplicar el único valor de $g$ a ambos lados da $(g\circ f)(x)=(g\circ f)(x')$; como $g\circ f=\operatorname{id}_A$, resulta $x=x'$. Para sobreyectividad, si $y\in B$, la totalidad de $g:B\to A$ proporciona $x=g(y)\in A$; la identidad $(f\circ g)(y)=y$ prueba $y=f(x)\in\operatorname{ran}(f)$. La inclusión inversa $\operatorname{ran}(f)\subseteq B$ sigue de que $f:A\to B$, por lo que se obtiene igualdad. Finalmente, si $g,h:B\to A$ son inversas bilaterales, por asociatividad
$$
g=g\circ\operatorname{id}_B=g\circ(f\circ h)
=(g\circ f)\circ h=\operatorname{id}_A\circ h=h.
$$
La prueba usa sólo composición funcional de dos valores únicos y no el axioma de elección. Si $A=B=\varnothing$, las gráficas vacías satisfacen directamente las ecuaciones. $\square$

**Frontera fundacional:** de una sobreyección arbitraria $f:A\to B$ *no* se infiere, en ZF sin elección, que exista una sección $s:B\to A$ con $f\circ s=\operatorname{id}_B$. La demostración anterior exige **inyectividad** para construir una inversa única, y evita seleccionar un elemento de cada fibra no unitaria.

## 14.34. Conservatividad de la notación funcional

### Metateorema 14.34.1 — Eliminación de aplicaciones, composición e inversas guardadas {#tlog-mth-00059}

Todas las afirmaciones de §§14.18–14.33 son familias de derivaciones en la signatura $\tau_\in$, una vez que las macros se expanden con nombres frescos. En particular, las expresiones $B^A$, $\operatorname{id}_A$ y $g\circ f$ tienen grafos caracterizadores **totales en los dominios de parámetros explícitamente declarados**, y $f(x)$, $f^{-1}$, $\operatorname{dom}(f)$ y $\operatorname{ran}(f)$ tienen las **guardas** registradas en §§14.11, 14.21 y 14.32. Para cada colección **finita** de esas abreviaciones utilizada en una prueba, existe una traducción que elimina por completo los símbolos añadidos, sustituyéndolos por fórmulas de pertenencia.

**Demostración metateórica.** En una fórmula concreta sólo aparecen finitamente muchas operaciones construidas. Se reemplazan primero los grafos de Kuratowski y de producto de §14.15, luego los de funciones y sus espacios de §14.23 y de composición de §14.28. Los nombres auxiliares son elegidos frescos respecto de la fórmula entera por el procedimiento de §6.18, evitando captura. Las operaciones totales introducidas como símbolos nuevos satisfacen las hipótesis de existencia y unicidad de §13.14, así que cada extensión finita es conservativa. Para una macro **guardada** $f(x)$ o $f^{-1}$, la prueba opera dentro del antecedente que garantiza existencia/unicidad; si se desea convertirla en símbolo total, el procedimiento de §13.31 reemplaza su valor fuera de la guarda por un objeto fijo ya existente, por ejemplo $\varnothing$. Esa **totalización es explícita** y no redefine el significado de la macro parcial en su dominio natural. La expansión deja de usar símbolos funcionales primitivos distintos de $\in$, y el resultado obtenido es una derivación en $\mathsf{ZF}_{\mathrm{obj}}$, no una demostración de su consistencia. $\square$

## 14.35. Cierre de la infraestructura relacional y funcional

### Corolario 14.35.1 — Funciones conjuntistas disponibles sin elección {#tlog-cor-00017}

Con los capítulos 12–14 quedan disponibles, como teoremas objeto y abreviaciones conservativas, los códigos de pares ordenados, productos cartesianos, relaciones, dominios y recorridos, funciones parciales y flechas totales entre conjuntos, espacios funcionales $B^A$, gráficos de operaciones funcionales definibles, imágenes y preimágenes, identidades, composición asociativa, relación conversa e inversas **funcionales bajo inyectividad**. Ninguno de estos resultados necesita $\mathsf{AC}$ ni $\mathsf{BPI}$; la inversión bilateral exige biyectividad relativa al codominio, y no se afirma que toda sobreyección admita sección.

La signatura primitiva sigue conteniendo sólo pertenencia y la igualdad lógica. Tampoco se importa una demostración de consistencia o un modelo estándar de $\mathsf{ZF}_{\mathrm{obj}}$, se activa una interfaz intertratados ni se considera una prueba humana equivalente a compilación Lean. Quedan preparados los cocientes, relaciones de equivalencia y órdenes del Capítulo 15. $\square$

## 14.36. Balance editorial del capítulo

`TLOG-CH14-M02` completa la función de salida de `TLOG-CH14-0001 — Relaciones, productos y funciones`. Los resultados §§14.18–14.35 tienen identificadores estables y dependencias directas en el DAG, y las abreviaciones de objetos funcionales conservan sus condiciones de existencia y unicidad. El capítulo 14 se declara `CLOSED / SCOPE-AUDITED` tras QA matemático y readback canónico; la **Parte III permanece abierta para los capítulos 15 y 16**. La fuente canónica es Markdown en Obsidian/Drive; ninguna operación de escritura pasa por Google Docs y no existe publicación web ni formalización Lean verificada.

**Próximo capítulo:** `TLOG-CH15-M01 — Relaciones de equivalencia, clases y cocientes`; la función de salida será construir las clases de equivalencia y justificar que las operaciones sobre cocientes estén bien definidas, antes de estudiar órdenes.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 13](capitulo-13.md) · [Capítulo 15 →](capitulo-15.md)

