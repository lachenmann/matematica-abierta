## 15.5. Puntos de acumulación y puntos aislados {#sec-ta-15-5}

Un punto adherente puede encontrarse en todas las bolas centradas en él por una razón trivial: **él mismo** pertenece al conjunto. Para captar una proximidad que no dependa de esa coincidencia, excluiremos expresamente el centro. La acumulación es, por tanto, una condición más fuerte que la adherencia, aun cuando el centro no pertenezca al conjunto.

### Definición 15.5.1 — Punto de acumulación

Sean $A\subseteq\mathbb R$ y $x\in\mathbb R$. Decimos que **$x$ es punto de acumulación de $A$** si toda bola abierta de radio positivo centrada en $x$ contiene un punto de $A$ *distinto de $x$*:

$$
\boxed{\forall r\in\mathbb R\ \bigl(r>0\implies
(B_r(x)\setminus\{x\})\cap A\ne\varnothing\bigr).}
$$

Equivalentemente, para todo $r>0$ existe $y\in A$ tal que $0<|y-x|<r$: la primera desigualdad equivale a $y\ne x$ y la segunda equivale a $y\in B_r(x)$. Los conjuntos involucrados ya existen por las operaciones de diferencia e intersección. El punto $x$ **no tiene por qué pertenecer a $A$**. Cada radio puede aportar un testigo diferente; no se pide escoger una función de testigos indexada por los radios.

> **Distinción lógica.** Adherencia exige $B_r(x)\cap A\ne\varnothing$ para todo $r>0$; acumulación exige además un testigo diferente del centro. La diferencia entre ambas nociones es significativa precisamente cuando $x\in A$.

### Definición 15.5.2 — Conjunto derivado o conjunto de puntos de acumulación

Para cada $A\subseteq\mathbb R$ definimos su **conjunto derivado** mediante

$$
\boxed{\operatorname{Acc}(A):=\{x\in\mathbb R:
\forall r\in\mathbb R\ (r>0\implies
(B_r(x)\setminus\{x\})\cap A\ne\varnothing)\}.}
$$

La Separación sobre $\mathbb R$ proporciona este conjunto; la extensionalidad lo determina de manera única. También queda definida una función total $\operatorname{Acc}:\mathcal P(\mathbb R)\to\mathcal P(\mathbb R)$: se separan en $\mathcal P(\mathbb R)\times\mathcal P(\mathbb R)$ los pares cuyo segundo componente satisface exactamente la fórmula exhibida para el primero. No se selecciona ningún punto de las intersecciones que aparecen en ella.

Escribimos $\operatorname{Acc}(A)$ en vez de introducir aquí $A'$: la abreviatura evita anticipar la notación de derivadas de funciones. La expresión designa un conjunto, no una operación de diferenciación.

### Proposición 15.5.3 — Acumulación implica adherencia y respeta la inclusión

Para cualesquiera $A,B\subseteq\mathbb R$ se tiene

$$
\boxed{\operatorname{Acc}(A)\subseteq\overline A,\qquad
A\subseteq B\implies\operatorname{Acc}(A)\subseteq\operatorname{Acc}(B).}
$$

**Demostración.**

Sea $x\in\operatorname{Acc}(A)$ y fijemos $r>0$. Por definición existe $y\in(B_r(x)\setminus\{x\})\cap A$. En particular, $y\in B_r(x)\cap A$, luego esta última intersección es no vacía. Como el radio era arbitrario, $x\in\overline A$.

Supongamos ahora $A\subseteq B$ y fijemos $x\in\operatorname{Acc}(A)$. Dado cualquier $r>0$, el testigo $y\in B_r(x)\setminus\{x\}$ anterior pertenece a $A$ y, por la inclusión, también a $B$. Por consiguiente $(B_r(x)\setminus\{x\})\cap B\ne\varnothing$ para cada radio positivo; así $x\in\operatorname{Acc}(B)$. ∎

La primera inclusión puede ser estricta: un punto que pertenece a un singleton es adherente a él, pero veremos que no puede ser punto de acumulación de ese singleton.

### Teorema 15.5.4 — Descomposición de la clausura y criterio de cerradura

Para todo $A\subseteq\mathbb R$,

$$
\boxed{\overline A=A\cup\operatorname{Acc}(A).}
$$

Además, la condición de ser cerrado admite la caracterización

$$
\boxed{A\text{ es cerrado}\iff\operatorname{Acc}(A)\subseteq A.}
$$

**Demostración.**

La extensividad de Proposición 15.4.4 — Extensividad y monotonía de la clausura proporciona $A\subseteq\overline A$; Proposición 15.5.3 — Acumulación implica adherencia y respeta la inclusión proporciona $\operatorname{Acc}(A)\subseteq\overline A$. Por tanto, su unión también está incluida en $\overline A$.

Para la otra inclusión fijemos $x\in\overline A$. Distinguimos mediante lógica clásica dos casos. Si $x\in A$, ya pertenece a $A\cup\operatorname{Acc}(A)$. Si $x\notin A$, consideremos cualquier $r>0$. Por adherencia, hay $y\in B_r(x)\cap A$. Como $x\notin A$, necesariamente $y\ne x$, de modo que $y\in(B_r(x)\setminus\{x\})\cap A$. Esto vale para todo radio positivo; luego $x\in\operatorname{Acc}(A)$ y, de nuevo, $x$ pertenece a la unión. La doble inclusión y extensionalidad prueban la identidad.

Si $A$ es cerrado, Corolario 15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura afirma que $\overline A=A$. Como $\operatorname{Acc}(A)\subseteq\overline A$, deducimos $\operatorname{Acc}(A)\subseteq A$. Recíprocamente, si $\operatorname{Acc}(A)\subseteq A$, la identidad recién probada da $\overline A=A\cup\operatorname{Acc}(A)=A$; el mismo criterio Corolario 15.4.7 — Un conjunto es cerrado si y sólo si coincide con su clausura implica que $A$ es cerrado. ∎

> **Lectura del resultado.** La clausura reúne los puntos que ya están en $A$ y los puntos que no pueden separarse de él mediante bolas perforadas. No afirma que $\operatorname{Acc}(A)$ esté incluido en $A$: esa inclusión es precisamente una caracterización de los conjuntos cerrados.

### Definición 15.5.5 — Punto aislado

Un punto $x$ es **aislado en $A\subseteq\mathbb R$** si $x\in A$ y existe un radio $r>0$ tal que

$$
\boxed{B_r(x)\cap A=\{x\}.}
$$

La pertenencia $x\in A$ es indispensable: una bola que no encuentre ningún punto de $A$ describe un punto exterior, no un punto aislado *de $A$*. La igualdad exige que dentro de cierta bola el único punto del conjunto sea el centro; otros puntos de $A$ pueden existir fuera de ella.

### Proposición 15.5.6 — Los puntos aislados son los puntos propios no acumulativos

Para $x\in\mathbb R$ y $A\subseteq\mathbb R$,

$$
\boxed{x\text{ es aislado en }A\iff
x\in A\ \text{y}\ x\notin\operatorname{Acc}(A).}
$$

En particular, el conjunto de los puntos aislados de $A$ es exactamente $A\setminus\operatorname{Acc}(A)$.

**Demostración.**

Supongamos que $x$ es aislado. Entonces $x\in A$ y existe $r>0$ con $B_r(x)\cap A=\{x\}$. Al retirar $x$ de esa intersección resulta $(B_r(x)\setminus\{x\})\cap A=\varnothing$. La condición universal que define la acumulación falla para ese radio; por ello $x\notin\operatorname{Acc}(A)$.

Recíprocamente, supongamos $x\in A$ y $x\notin\operatorname{Acc}(A)$. La negación clásica de la condición universal de Definición 15.5.1 — Punto de acumulación proporciona un $r>0$ tal que $(B_r(x)\setminus\{x\})\cap A=\varnothing$. Como $x\in A$ y, por Proposición 15.1.2 — Las bolas son intervalos abiertos centrados, $x\in B_r(x)$, tenemos $x\in B_r(x)\cap A$. Si $y$ es cualquier otro elemento de esta intersección, $y\ne x$ lo situaría en la intersección perforada vacía, contradicción. Por tanto $B_r(x)\cap A=\{x\}$ y $x$ es aislado. La descripción del conjunto de puntos aislados se obtiene por Separación en $A$. ∎

La oposición entre «aislado» y «de acumulación» concierne a los puntos **que pertenecen a $A$**: un punto exterior también puede no ser de acumulación, pero nunca se le llamará aislado en $A$.

### Teorema 15.5.7 — El conjunto de puntos de acumulación es cerrado

Para todo $A\subseteq\mathbb R$, el conjunto $\operatorname{Acc}(A)$ es cerrado en $\mathbb R$.

**Demostración.**

Aplicaremos el criterio Proposición 15.3.6 — Criterio de cerradura mediante puntos exteriores: basta mostrar que cada punto del complemento de $\operatorname{Acc}(A)$ posee una bola disjunta de ese conjunto. Fijemos $x\notin\operatorname{Acc}(A)$. La negación de la definición de acumulación proporciona un radio $r>0$ tal que

$$
(B_r(x)\setminus\{x\})\cap A=\varnothing. \tag{*}
$$

Afirmamos que $B_r(x)\cap\operatorname{Acc}(A)=\varnothing$. El centro $x$ no pertenece a $\operatorname{Acc}(A)$ por hipótesis. Sea entonces $y\in B_r(x)$ con $y\ne x$. Los dos reales $r-|y-x|$ y $|y-x|$ son positivos; definamos explícitamente

$$
\delta:=\frac{\min\{r-|y-x|,\,|y-x|\}}{1+1}>0.
$$

Si $z\in B_\delta(y)$, las desigualdades triangular e inversa dan

$$
|z-x|\le |z-y|+|y-x|<\delta+|y-x|<r
$$

y

$$
|z-x|\ge |y-x|-|z-y|>|y-x|-\delta>0.
$$

Por tanto $z\in B_r(x)\setminus\{x\}$, y así $B_\delta(y)\subseteq B_r(x)\setminus\{x\}$. La intersección de esta última región con $A$ es vacía por (*); en particular $B_\delta(y)\cap A=\varnothing$. El punto $y$ no es de acumulación, porque para el radio $\delta$ ni siquiera hay un punto de $A$ en la bola. En consecuencia, ningún $y\in B_r(x)$ pertenece a $\operatorname{Acc}(A)$.

Hemos hallado para cada $x\notin\operatorname{Acc}(A)$ un radio positivo $r$ con $B_r(x)\cap\operatorname{Acc}(A)=\varnothing$. El criterio de cerradura Proposición 15.3.6 — Criterio de cerradura mediante puntos exteriores completa la demostración. ∎

La prueba es local: una única bola que evita a $A$ salvo, eventualmente, por su centro también evita a **todos** los puntos de acumulación de $A$. No se extrajeron sucesiones de puntos, por lo que tampoco se requirió elección numerable.

### Teorema 15.5.8 — El conjunto derivado conserva las uniones binarias

Para cualesquiera $A,B\subseteq\mathbb R$,

$$
\boxed{\operatorname{Acc}(A\cup B)
=\operatorname{Acc}(A)\cup\operatorname{Acc}(B).}
$$

Para una familia indexada arbitraria sólo afirmamos, por monotonía,

$$
\boxed{\bigcup_{i\in I}\operatorname{Acc}(A_i)
\subseteq\operatorname{Acc}\left(\bigcup_{i\in I}A_i\right).}
$$

**Demostración.**

Como $A\subseteq A\cup B$ y $B\subseteq A\cup B$, la monotonía Proposición 15.5.3 — Acumulación implica adherencia y respeta la inclusión implica que cada conjunto derivado de la derecha está incluido en $\operatorname{Acc}(A\cup B)$. Esto da la inclusión de derecha a izquierda.

Para la inclusión opuesta, fijemos $x\in\operatorname{Acc}(A\cup B)$ y supongamos, por contradicción, que $x\notin\operatorname{Acc}(A)$ y $x\notin\operatorname{Acc}(B)$. Negando clásicamente ambas condiciones universales, obtenemos radios $r,s>0$ tales que

$$
(B_r(x)\setminus\{x\})\cap A=\varnothing,
\qquad
(B_s(x)\setminus\{x\})\cap B=\varnothing.
$$

El número $t=\min\{r,s\}$ es positivo. Puesto que $B_t(x)\subseteq B_r(x)\cap B_s(x)$, ningún punto de $B_t(x)\setminus\{x\}$ pertenece a $A$ ni a $B$, y por lo tanto

$$
(B_t(x)\setminus\{x\})\cap(A\cup B)=\varnothing.
$$

Esto contradice $x\in\operatorname{Acc}(A\cup B)$. Por lógica clásica, $x$ pertenece a $\operatorname{Acc}(A)$ o a $\operatorname{Acc}(B)$ y queda demostrada la igualdad. Para la familia, cada $A_i$ está contenido en su unión; la monotonía aporta $\operatorname{Acc}(A_i)\subseteq\operatorname{Acc}(\bigcup_j A_j)$ para cada $i$, y la definición de unión entrega la inclusión solicitada. El caso $I=\varnothing$ es inmediato. No se han escogido puntos para todos los radios ni índices simultáneamente. ∎

Una unión **finita** de conjuntos derivados se trata por inducción a partir de la igualdad binaria y del caso vacío que verificaremos enseguida. Para uniones arbitrarias, la inclusión inversa puede fallar.

### Proposición 15.5.9 — Ejemplos y límite de la ley de unión

Dados $a,b\in\mathbb R$ con $a<b$, se tienen las identidades

$$
\boxed{\operatorname{Acc}(\varnothing)=\varnothing,
\quad \operatorname{Acc}(\{a\})=\varnothing,
\quad\operatorname{Acc}((a,b))=[a,b].}
$$

Existe, además, una familia de conjuntos cuyo conjunto derivado **no** conserva la unión arbitraria como igualdad.

**Demostración.**

**Vacío y singleton.** Ninguna bola perforada puede intersectar $\varnothing$. Si $x=a$, la intersección $(B_r(a)\setminus\{a\})\cap\{a\}$ es vacía para *todo* $r>0$. Si $x\ne a$, tomemos $r=|x-a|/(1+1)>0$. Para el único candidato $a$ se tiene $|a-x|>r$, por lo que $a\notin B_r(x)$ y la intersección perforada también es vacía. Ningún punto acumula al singleton, y las dos primeras identidades siguen por extensionalidad.

**Intervalo abierto: inclusión $[a,b]\subseteq\operatorname{Acc}((a,b))$.** Sea $x\in(a,b)$ y $r>0$. El número

$$
\eta:=\frac{\min\{r,b-x\}}{1+1}>0
$$

satisface $0<\eta<r$ y $0<\eta<b-x$, de modo que $y:=x+\eta$ pertenece a $(a,b)$, es distinto de $x$ y está en $B_r(x)$. Por ello $x$ es de acumulación. Si $x=a$, elijamos explícitamente $y=a+\min\{r,b-a\}/(1+1)$; si $x=b$, tomemos $y=b-\min\{r,b-a\}/(1+1)$. En cada caso $y\in(a,b)$, $y\ne x$ y $|y-x|<r$. Así, también los dos extremos son de acumulación.

**Inclusión inversa.** Si $x<a$, fijemos $r=(a-x)/(1+1)>0$. Cada $y\in B_r(x)$ satisface $y<x+r<a$, por lo que $B_r(x)\cap(a,b)=\varnothing$. Si $x>b$, el radio $(x-b)/(1+1)$ garantiza análogamente $B_r(x)\cap(a,b)=\varnothing$. Estos puntos no acumulan al intervalo. Por totalidad del orden, todo real fuera de $[a,b]$ satisface una de esas dos desigualdades; así, $\operatorname{Acc}((a,b))\subseteq[a,b]$. Las inclusiones prueban la tercera igualdad.

**Por qué la unión infinita es distinta.** Sea $I=(0,1)$, conjunto existente de índices reales, y para cada $t\in I$ definamos $F_t=\{t\}$. Su grafo funcional se obtiene por Separación en $I\times\mathcal P(\mathbb R)$ a partir de la fórmula $F_t=\{t\}$; no interviene Choice. Cada $\operatorname{Acc}(F_t)$ es vacío por el caso singleton, por lo que

$$
\bigcup_{t\in I}\operatorname{Acc}(F_t)=\varnothing.
$$

Pero $\bigcup_{t\in I}F_t=(0,1)$, cuyo conjunto derivado es $[0,1]$ por la tercera identidad (entendiendo ahora $0,1$ como elementos del cuerpo real). En particular, $0$ pertenece al derivado de la unión y no a la unión de los derivados. La inclusión indexada de Teorema 15.5.8 — El conjunto derivado conserva las uniones binarias puede ser estricta. ∎

Los ejemplos fijan el alcance de la noción: **una pertenencia solitaria no produce acumulación**, mientras que los extremos de un intervalo pueden acumular puntos aun sin pertenecer al intervalo. El próximo paso será estudiar los puntos de frontera mediante la relación simultánea con un conjunto y su complemento, sin confundir frontera con conjunto derivado.
