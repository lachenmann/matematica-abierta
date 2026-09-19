## 15.7. Operaciones de interior, clausura y frontera {#sec-ta-15-7}

Las secciones anteriores construyeron tres aplicaciones de $\mathcal P(\mathbb R)$ en sí mismo: $A\mapsto A^\circ$, $A\mapsto\overline A$ y $A\mapsto\partial A$. Hemos probado por separado que el interior es el mayor abierto incluido en $A$ (Teorema 15.2.8 — El interior es el mayor abierto contenido en el conjunto), que la clausura es el menor cerrado que lo contiene (Teorema 15.4.6 — La clausura es el menor cerrado que contiene al conjunto) y que la frontera reúne los puntos adherentes a $A$ y a su complemento (Teorema 15.6.3 — Caracterización de la frontera por dos clausuras). Podemos ahora examinar sus leyes sin volver a definirlas.

Conviene separar dos problemas: **cómo se comporta cada operación al ampliar el conjunto** y **cómo interactúa con las operaciones conjuntistas**. La clausura ya dispone de una teoría completa de uniones e intersecciones en §15.4 (Teorema 15.4.10 — Clausura de uniones e intersecciones y Proposición 15.4.11 — Dos inclusiones que pueden ser estrictas); aquí no duplicaremos esas pruebas. Completaremos primero las leyes del interior y después deduciremos las de la frontera.

### Proposición 15.7.1 — Monotonía y leyes del interior

Para $A,B\subseteq\mathbb R$ se tienen

$$
\boxed{A\subseteq B\ \Longrightarrow\ A^\circ\subseteq B^\circ,}
$$

$$
\boxed{\varnothing^\circ=\varnothing,\quad (\mathbb R)^\circ=\mathbb R,\quad (A^\circ)^\circ=A^\circ,}
$$

$$
\boxed{(A\cap B)^\circ=A^\circ\cap B^\circ,\qquad
A^\circ\cup B^\circ\subseteq(A\cup B)^\circ.}
$$

Para toda familia $(A_i)_{i\in I}$ de subconjuntos de $\mathbb R$, con $I$ un conjunto de índices, valen además

$$
\boxed{\bigcup_{i\in I}A_i^\circ\subseteq
\left(\bigcup_{i\in I}A_i\right)^\circ,\qquad
\left(\bigcap_{i\in I}A_i\right)^\circ\subseteq
\bigcap_{i\in I}A_i^\circ.}
$$

La intersección vacía está referida al ambiente $\mathbb R$ y la unión vacía es $\varnothing$. La igualdad para intersecciones se afirma aquí sólo para **familias finitas**; la igualdad binaria, junto con inducción, cubre también la intersección finita vacía.

**Demostración.**

**Monotonía.** Si $x\in A^\circ$, existe $r>0$ con $B_r(x)\subseteq A$. Bajo la hipótesis $A\subseteq B$, ese mismo radio da $B_r(x)\subseteq B$, de modo que $x\in B^\circ$. No se necesitan radios seleccionados simultáneamente.

**Vacío, recta e idempotencia.** El interior está contenido en el conjunto original (Proposición 15.2.3 — Interior y vecindades), así que $\varnothing^\circ=\varnothing$. La recta es abierta por Teorema 15.2.7 — Leyes fundamentales de los conjuntos abiertos, luego $(\mathbb R)^\circ=\mathbb R$ por Proposición 15.2.6 — Caracterización de los abiertos mediante el interior. El interior $A^\circ$ es abierto por Teorema 15.2.8 — El interior es el mayor abierto contenido en el conjunto; el mismo criterio aplicado a $A^\circ$ da $(A^\circ)^\circ=A^\circ$.

**Intersección binaria.** Como $A\cap B\subseteq A,B$, la monotonía recién probada implica $(A\cap B)^\circ\subseteq A^\circ\cap B^\circ$. En sentido inverso, $A^\circ$ y $B^\circ$ son abiertos (Teorema 15.2.8 — El interior es el mayor abierto contenido en el conjunto), y su intersección es abierta (Teorema 15.2.7 — Leyes fundamentales de los conjuntos abiertos). Está contenida en $A\cap B$ porque cada interior está contenido en su conjunto. La maximalidad de $(A\cap B)^\circ$ (Teorema 15.2.8 — El interior es el mayor abierto contenido en el conjunto) produce $A^\circ\cap B^\circ\subseteq(A\cap B)^\circ$. Ambas inclusiones prueban la igualdad.

**Unión binaria y familias.** De $A\subseteq A\cup B$ y $B\subseteq A\cup B$ se deduce por monotonía que ambos interiores están contenidos en $(A\cup B)^\circ$; lo mismo vale para su unión. Para una familia general, las operaciones $A\mapsto A^\circ$ y $i\mapsto A_i$ son funciones ya construidas; su composición determina $i\mapsto A_i^\circ$ sin elegir radios. Si $x\in\bigcup_i A_i^\circ$, existe un índice particular $i$ con $x\in A_i^\circ$, y $A_i\subseteq\bigcup_j A_j$ permite aplicar monotonía. Para la intersección, sea $V=\bigcap_i A_i\subseteq\mathbb R$. Para cada $i\in I$, $V\subseteq A_i$ implica $V^\circ\subseteq A_i^\circ$; por tanto $V^\circ\subseteq\bigcap_i A_i^\circ$. Si $I=\varnothing$, las afirmaciones se reducen respectivamente a $\varnothing\subseteq\varnothing$ y $\mathbb R\subseteq\mathbb R$.

Por último, la igualdad de intersecciones para cualquier número finito de conjuntos se obtiene por inducción sobre ese número, utilizando el caso binario y el caso vacío ya establecidos. ∎

La asimetría es deliberada: el interior **preserva intersecciones finitas**, pero una unión puede crear puntos interiores que no lo eran en ninguno de los sumandos. En una intersección infinita puede ocurrir lo contrario: los márgenes positivos disponibles para cada factor pueden desaparecer al exigirlos todos a la vez.

### Proposición 15.7.2 — Dos inclusiones del interior pueden ser estrictas

Existen conjuntos $A,B\subseteq\mathbb R$ tales que

$$
\boxed{A^\circ\cup B^\circ\subsetneq(A\cup B)^\circ,}
$$

y una familia de conjuntos abiertos $(U_r)_{r\in I}$ tal que

$$
\boxed{\left(\bigcap_{r\in I}U_r\right)^\circ
\subsetneq\bigcap_{r\in I}U_r^\circ.}
$$

**Demostración.**

Para la unión, fijemos $a<b<c$ en $\mathbb R$ y consideremos $A=[a,b]$ y $B=[b,c]$. La demostración de Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía estableció que el interior de un intervalo cerrado no degenerado es el correspondiente intervalo abierto. Así,

$$
A^\circ\cup B^\circ=(a,b)\cup(b,c),
\qquad (A\cup B)^\circ=[a,c]^\circ=(a,c).
$$

El punto $b$ pertenece al conjunto de la derecha, pero no al de la izquierda. La inclusión es, pues, propia.

Para la intersección, fijemos $a\in\mathbb R$ y reutilicemos el conjunto de índices $I:=\{r\in\mathbb R:r>0\}$ y la familia explícita $U_r:=B_r(a)$ de Proposición 15.3.11 — Las restricciones de finitud son necesarias. Allí se probó que $\bigcap_{r\in I}U_r=\{a\}$. Toda bola es abierta (Teorema 15.2.5 — Toda bola abierta es un conjunto abierto), por lo que $U_r^\circ=U_r$; en cambio $\{a\}^\circ=\varnothing$, ya que ninguna bola positiva está contenida en el singleton, como se verificó en Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía. En consecuencia,

$$
\left(\bigcap_{r\in I}U_r\right)^\circ=\varnothing
\subsetneq\{a\}=\bigcap_{r\in I}U_r^\circ.
$$

El índice $I$, la familia de bolas y su intersección están definidos por fórmulas anteriores: no hay selección de radios ni elección numerable. ∎

**Síntesis de las dos primeras operaciones.** Por Proposición 15.4.4 — Extensividad y monotonía de la clausura y Proposición 15.4.8 — Idempotencia de la clausura, la clausura es extensiva, monótona e idempotente. Por Proposición 15.7.1 — Monotonía y leyes del interior, el interior es contractivo, monótono e idempotente. La clausura conserva las uniones finitas y satisface las inclusiones indexadas de Teorema 15.4.10 — Clausura de uniones e intersecciones, cuyos límites exactos se demostraron en Proposición 15.4.11 — Dos inclusiones que pueden ser estrictas. La dualidad ya obtenida en §15.4 toma la forma

$$
A^\circ=\mathbb R\setminus\overline{\mathbb R\setminus A},
\qquad
\overline A=\mathbb R\setminus(\mathbb R\setminus A)^\circ.
$$

Estas igualdades expresan una correspondencia entre interior y clausura mediante complementos **relativos a $\mathbb R$**. No las usamos para reemplazar las demostraciones anteriores ni introducimos una topología abstracta.

### Teorema 15.7.3 — Frontera de uniones e intersecciones binarias

Para cualesquiera $A,B\subseteq\mathbb R$ se cumplen las inclusiones

$$
\boxed{\partial(A\cup B)\subseteq\partial A\cup\partial B,}
$$

$$
\boxed{\partial(A\cap B)\subseteq\partial A\cup\partial B.}
$$

No se afirma, en general, ninguna de las dos igualdades.

**Demostración.**

Escribamos $C=\mathbb R\setminus A$ y $D=\mathbb R\setminus B$. Todas las operaciones siguientes están definidas sobre subconjuntos de $\mathbb R$.

**Unión.** Supongamos $x\in\partial(A\cup B)$. La caracterización de frontera de Teorema 15.6.3 — Caracterización de la frontera por dos clausuras y la ley de clausura de uniones binarias Teorema 15.4.10 — Clausura de uniones e intersecciones dan

$$
x\in\overline{A\cup B}=\overline A\cup\overline B.
$$

Por De Morgan, el complemento de $A\cup B$ es $C\cap D$. La otra condición fronteriza y la ley de clausura de intersecciones proporcionan

$$
x\in\overline{C\cap D}\subseteq\overline C\cap\overline D.
$$

Si $x\in\overline A$, entonces $x\in\overline A\cap\overline C=\partial A$. Si, por el contrario, la pertenencia a la unión inicial se verifica mediante $x\in\overline B$, tenemos $x\in\overline B\cap\overline D=\partial B$. En ambos casos $x\in\partial A\cup\partial B$.

**Intersección.** Sea ahora $x\in\partial(A\cap B)$. Por la ley de clausura de intersecciones,

$$
x\in\overline{A\cap B}\subseteq\overline A\cap\overline B.
$$

El complemento de $A\cap B$ es $C\cup D$. La otra condición fronteriza, junto con la ley de clausura de uniones, implica

$$
x\in\overline{C\cup D}=\overline C\cup\overline D.
$$

En el primer caso, $x\in\overline C$ y también $x\in\overline A$, de donde $x\in\partial A$. En el segundo, $x\in\overline D\cap\overline B=\partial B$. Así queda probada la segunda inclusión. Los casos son finitos y se consideran para un $x$ arbitrario ya fijado: no hay función de elección ni selección simultánea de testigos de bolas. ∎

La frontera de una unión o intersección no puede surgir fuera de las fronteras de los conjuntos iniciales; sin embargo, algunas fronteras **pueden desaparecer** cuando dos conjuntos se unen o se intersectan.

### Proposición 15.7.4 — Las dos inclusiones fronterizas pueden ser estrictas

Existen $A,B\subseteq\mathbb R$ para los cuales **ambas** inclusiones de Teorema 15.7.3 — Frontera de uniones e intersecciones binarias son propias.

**Demostración.**

Tomemos $a<b<c$ y definamos $A=[a,b]$, $B=[b,c]$. Por las definiciones de intervalos,

$$
A\cup B=[a,c],\qquad A\cap B=\{b\}.
$$

Los cálculos de frontera de Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía se aplican a los tres intervalos cerrados y al singleton:

$$
\partial A\cup\partial B
=\{a,b\}\cup\{b,c\}=\{a,b,c\},
$$

$$
\partial(A\cup B)=\partial[a,c]=\{a,c\},
\qquad
\partial(A\cap B)=\partial\{b\}=\{b\}.
$$

Como $a<b<c$, tanto $\{a,c\}$ como $\{b\}$ están propiamente incluidos en $\{a,b,c\}$. El mismo par de conjuntos certifica la estrictez de las dos inclusiones. ∎

### Corolario 15.7.5 — Frontera de una diferencia de conjuntos

Para $A,B\subseteq\mathbb R$,

$$
\boxed{\partial(A\setminus B)\subseteq\partial A\cup\partial B.}
$$

**Demostración.**

La diferencia se expresa, dentro del ambiente $\mathbb R$, como $A\setminus B=A\cap(\mathbb R\setminus B)$. Aplicamos la inclusión para fronteras de intersecciones de Teorema 15.7.3 — Frontera de uniones e intersecciones binarias y luego la simetría de la frontera bajo complemento de Proposición 15.6.5 — La frontera es cerrada y no cambia al tomar el complemento:

$$
\partial(A\setminus B)
\subseteq\partial A\cup\partial(\mathbb R\setminus B)
=\partial A\cup\partial B.
$$

Concluye la prueba. ∎

### Proposición 15.7.6 — La frontera después de tomar interior o clausura

Para todo $A\subseteq\mathbb R$ se verifica

$$
\boxed{\partial(A^\circ)\subseteq\partial A,
\qquad\partial(\overline A)\subseteq\partial A.}
$$

Las dos inclusiones pueden ser estrictas, aunque no necesariamente para el mismo conjunto.

**Demostración.**

**Frontera del interior.** Fijemos $x\in\partial(A^\circ)$. La identidad $\partial E=\overline E\setminus E^\circ$ de Teorema 15.6.4 — Descomposición de la recta en interior, frontera y exterior, aplicada a $E=A^\circ$, implica

$$
x\in\overline{A^\circ}
\quad\text{y}\quad x\notin(A^\circ)^\circ=A^\circ,
$$

donde usamos la idempotencia de Proposición 15.7.1 — Monotonía y leyes del interior. Como $A^\circ\subseteq A$, la monotonía de clausura (Proposición 15.4.4 — Extensividad y monotonía de la clausura) da $\overline{A^\circ}\subseteq\overline A$. Así $x\in\overline A\setminus A^\circ=\partial A$.

**Frontera de la clausura.** Si $x\in\partial(\overline A)$, la misma identidad y la idempotencia de la clausura (Proposición 15.4.8 — Idempotencia de la clausura) dan $x\in\overline A$ y $x\notin(\overline A)^\circ$. Por $A\subseteq\overline A$ y monotonía del interior (Proposición 15.7.1 — Monotonía y leyes del interior), tenemos $A^\circ\subseteq(\overline A)^\circ$. Por tanto $x\notin A^\circ$, lo que de nuevo implica $x\in\partial A$.

**Estrictez de la primera inclusión.** Para $A=\{a\}$, Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía establece $A^\circ=\varnothing$ y $\partial A=\{a\}$. La misma proposición prueba $\partial(A^\circ)=\partial\varnothing=\varnothing\subsetneq\{a\}$.

**Estrictez de la segunda inclusión.** Tomemos $A=\mathbb R\setminus\{a\}$. Proposición 15.4.11 — Dos inclusiones que pueden ser estrictas probó explícitamente $\overline A=\mathbb R$, de modo que $\partial(\overline A)=\partial\mathbb R=\varnothing$ por Proposición 15.6.8 — Ejemplos: extremos, singletons y falta de monotonía. En cambio, por la simetría bajo complemento de Proposición 15.6.5 — La frontera es cerrada y no cambia al tomar el complemento, $\partial A=\partial\{a\}=\{a\}$. La inclusión es estricta. ∎

> **Interpretación.** Interior y clausura disponen de leyes de monotonía e idempotencia; la frontera no. Sin embargo, las tres están ligadas por $\partial A=\overline A\setminus A^\circ$: tomar primero interior o clausura puede eliminar parte de la frontera original, pero no crea puntos fronterizos fuera de ella. Estos resultados son relativos a la recta real; las descripciones mediante sucesiones y las cuestiones de densidad siguen pendientes en las unidades posteriores.
