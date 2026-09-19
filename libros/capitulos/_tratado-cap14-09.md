## 14.9. Criterios de razón y raíz {#sec-ta-14-9}

La comparación por límite de §14.6 relaciona *dos* series ya dadas. Los criterios de este apartado buscan un patrón geométrico dentro de una sola sucesión: la **razón** compara magnitudes consecutivas; la **raíz enésima** mide el tamaño de un término frente a una potencia de exponente igual a su índice. Las dos pruebas remitirán a la serie geométrica de §14.3 y a la convergencia absoluta de §14.8. No afirmaremos que un límite igual a $1$ decida la convergencia.

El cociente secuencial ya existe (Definición 14.6.2 — Cociente secuencial totalizado y cociente eventual) y permite precisar dónde puede anularse el denominador. No ocurre lo mismo con la raíz enésima: todavía no la hemos definido. Antes de utilizar el segundo criterio demostraremos su existencia, unicidad y dominio, directamente a partir de la completitud real y de las potencias naturales construidas en §14.3.

### Lema 14.9.1 — Monotonía de las potencias positivas y cota de variación finita

Dados $k\in\mathbb N$ y $0\le u\le v\le M$ en $\mathbb R$, se verifican

$$
\boxed{0\le v^{k+1}-u^{k+1}
\le\nu_{\mathbb R}(k+1)M^k(v-u).}
\tag{14.9.1}
$$

Si $0\le u<v$, entonces $u^{k+1}<v^{k+1}$. Por tanto, para cada exponente natural **positivo**, la potenciación es estrictamente creciente en los reales no negativos.

**Demostración.**

La positividad de $t^j$ para $t\ge0$ y $j\in\mathbb N$ se obtiene inmediatamente por inducción usando $t^0=1$ y $t^{j+1}=t^jt$. Igualmente, si $0\le s\le t$, la inducción da $s^j\le t^j$ para todo $j$. Fijados $u,v,M$ como en el enunciado, probaremos (14.9.1) por inducción sobre $k$.

Para $k=0$ la diferencia es $v-u$, y el factor derecho es $\nu_{\mathbb R}(1)M^0=1$, incluso si $M=0$. Supongamos válida la estimación para $k$ y escribamos, con $\delta=v-u\ge0$,

$$
\begin{aligned}
v^{k+2}-u^{k+2}
&=v^{k+1}(v-u)+u(v^{k+1}-u^{k+1})\\
&\le M^{k+1}\delta
 +M\,\nu_{\mathbb R}(k+1)M^k\delta\\
&=\nu_{\mathbb R}(k+2)M^{k+1}\delta.
\end{aligned}
$$

Ambos sumandos de la primera línea son no negativos. La última igualdad utiliza la preservación de la suma natural por $\nu_{\mathbb R}$ (Proposición 4.1.6 — Aritmética y orden de los numerales naturales), y completa la inducción.

Para la versión estricta, el caso $k=0$ es $u<v$. Si $u^{k+1}<v^{k+1}$ y $0\le u<v$, entonces $v^{k+1}>0$ y

$$
v^{k+2}=v^{k+1}v>v^{k+1}u\ge u^{k+1}u=u^{k+2}.
$$

El principio de inducción concluye también este segundo aserto. ∎

> **Uso de la cota.** La desigualdad (14.9.1) controla una potencia al modificar ligeramente su base. No presupone continuidad de funciones, derivadas, un binomio general ni raíces previamente definidas. El exponente se escribe $k+1$ para no utilizar una resta natural que no hemos introducido como operación total.

---

### Teorema 14.9.2 — Existencia y unicidad de la raíz no negativa de índice positivo

Para cada $k\in\mathbb N$ y cada real $x\ge0$ existe **un único** $r\ge0$ tal que

$$
\boxed{r^{k+1}=x.}
\tag{14.9.2}
$$

Además, $x>0$ implica $r>0$; y para $0\le x\le y$, sus respectivas raíces no negativas de un mismo índice conservan el orden.

**Demostración.**

Fijemos $k$ y $x\ge0$, y escribamos $m:=k+1$. Por Separación existe

$$
S:=\{t\in\mathbb R:0\le t\ \text{y}\ t^m\le x\}.
$$

Es no vacío: $0\in S$, pues $m$ es positivo y $0^m=0$. También está acotado superiormente por $B:=1+x$. En efecto, si $t>B$, entonces $t>1$ y $t>x$; por inducción $t^m\ge t>x$, de modo que $t\notin S$. El orden total muestra que ningún elemento de $S$ supera $B$. La completitud proporciona el real $r:=\sup S$, y $0\le r\le B$.

La clave es verificar que $r^m=x$; ser supremo por sí solo no da esa igualdad. Para aplicar (14.9.1) sin exponentes negativos, fijemos

$$
K:=\nu_{\mathbb R}(m)(r+1)^k>0.
$$

**Caso $r^m<x$.** Sea $g:=x-r^m>0$. Tomemos el número real determinado

$$
\delta:=\frac{g}{(1+1)(K+g+1)}.
$$

El denominador es positivo y $0<\delta<1$, mientras que $K\delta<g$. Aplicando (14.9.1) a $u=r$, $v=r+\delta$, $M=r+1$ obtenemos

$$
(r+\delta)^m-r^m\le K\delta<g,
$$

luego $(r+\delta)^m<x$ y $r+\delta\in S$. Esto contradice que $r$ sea cota superior de $S$.

**Caso $r^m>x$.** Necesariamente $r>0$; pongamos $g:=r^m-x>0$ y fijemos

$$
\delta:=\min\left\{\frac r2,\frac{g}{(1+1)(K+1)}\right\}>0.
$$

Aquí $0<\delta<r$, $K\delta<g$ y $0\le r-\delta<r\le r+1$. Por (14.9.1), ahora con $u=r-\delta$, $v=r$ y $M=r+1$,

$$
(r-\delta)^m\ge r^m-K\delta>x.
$$

Todo $t\in S$ satisface $t<r-\delta$: de lo contrario, la monotonía de las potencias positivas daría $t^m\ge(r-\delta)^m>x$, contrario a la definición de $S$. Así, $r-\delta$ sería una cota superior de $S$ estrictamente menor que su supremo. Contradicción.

La tricotomía excluye ambos casos y entrega $r^m=x$. Si $0\le r<s$ fueran dos soluciones, la estricta monotonía de Lema 14.9.1 — Monotonía de las potencias positivas y cota de variación finita daría $r^m<s^m$, imposible. La solución es única. Si $x>0$ no puede ser $r=0$. Finalmente, si $x\le y$ y sus raíces fueran $r>s$, la misma monotonía produciría $x=r^m>s^m=y$, contradicción. ∎

> **Auditoría fundacional.** Se toma el supremo de *un conjunto explícito*, no una familia de elecciones. Las perturbaciones $\delta$ son expresiones unívocas de reales previamente fijados. La demostración no presupone el teorema del valor intermedio ni una continuidad general de $t\mapsto t^m$; la estimación finita del lema proporciona exactamente lo necesario.

---

### Notación 14.9.3 — Raíz enésima real no negativa

Si $m\in\mathbb N$ es positivo y $x\in\mathbb R$ satisface $x\ge0$, denotamos por

$$
\boxed{\sqrt[m]{x}}
$$

el único real no negativo cuya potencia $m$-ésima es $x$. La asignación $(m,x)\mapsto\sqrt[m]{x}$ es una función sobre el conjunto $\mathbb N_{\ge1}\times\mathbb R_{\ge0}$: su grafo existe por Separación dentro de $(\mathbb N_{\ge1}\times\mathbb R_{\ge0})\times\mathbb R$, y el teorema precedente garantiza existencia y unicidad para cada entrada. Aquí $\mathbb N_{\ge1}$ es el segmento final ya definido en §13.2 y $\mathbb R_{\ge0}:=\{x\in\mathbb R:x\ge0\}$ es una abreviatura conjuntista explícita.

No definimos $\sqrt[0]{x}$, raíces reales de radicandos negativos ni raíces complejas. La raíz conserva el orden para cada índice fijo y, si $c\ge0$, cumple $\sqrt[m]{c^m}=c$ por unicidad. Los índices pertenecen a $\mathbb N$, mientras que radicandos y raíces pertenecen a $\mathbb R$.

---

### Definición 14.9.4 — Sucesión de raíces asociada a una serie

Para cada sucesión real $a$ definimos una nueva sucesión real $R(a)$ mediante

$$
\boxed{R(a)_0:=0,
\qquad R(a)_n:=\sqrt[n]{|a_n|}\quad(n\ge1).}
\tag{14.9.3}
$$

Para cada índice positivo el radicando es no negativo y la raíz existe y es única; en $n=0$ se asigna expresamente $0$, sin escribir una raíz de índice cero. El grafo de $R(a)$ existe por Separación dentro de $\mathbb N\times\mathbb R$ y es total y funcional. Asimismo existe el operador $R:\mathbb R^{\mathbb N}\to\mathbb R^{\mathbb N}$ por Separación en el producto de conjuntos de sucesiones.

Todos los términos de $R(a)$ son no negativos. Su posible límite es, pues, no negativo por la preservación del orden al límite (Teorema 13.6.2 — Preservación del orden en el paso al límite). El valor convencional de $R(a)_0$ no afecta a la convergencia. No presupone que $a_n$ sea positivo ni que la serie de $a$ converja.

---

### Lema 14.9.5 — Las raíces enésimas de una constante positiva tienden a uno

Para cada real $C>0$, la sucesión definida en los índices positivos por $c_n:=\sqrt[n]{C}$ (y, por convención, $c_0:=1$) satisface

$$
\boxed{c_n\longrightarrow1.}
\tag{14.9.4}
$$

Además, para $C>0$, $q>0$ y $n\ge1$,

$$
\boxed{\sqrt[n]{Cq^n}=\sqrt[n]{C}\,q.}
\tag{14.9.5}
$$

**Demostración.**

Primero comprobemos dos identidades algebraicas que no supondremos implícitas. Una inducción con la recursión de Definición 14.3.1 — Potencias naturales de un número real da $(uv)^j=u^jv^j$ para $u,v\in\mathbb R$ y $j\in\mathbb N$. Si $u,v>0$ y $j\ge1$, entonces $u^j,v^j>0$. Por tanto,

$$
\bigl(\sqrt[n]{C}\,q\bigr)^n
=\bigl(\sqrt[n]{C}\bigr)^n q^n=Cq^n.
$$

La base es no negativa, y la unicidad de la raíz prueba (14.9.5).

Para la convergencia, demostremos por inducción la desigualdad de Bernoulli elemental

$$
(1+\eta)^n\ge1+\nu_{\mathbb R}(n)\eta
\qquad(\eta>0,\ n\in\mathbb N).
\tag{14.9.6}
$$

El caso $n=0$ es igualdad. Multiplicar el paso inductivo por $1+\eta>0$ da, además del término $\nu_{\mathbb R}(n+1)\eta$, un sumando no negativo $\nu_{\mathbb R}(n)\eta^2$. Con esto queda demostrada la desigualdad.

Si $C=1$, todas sus raíces son $1$. Si $C>1$, fijemos $\varepsilon>0$. La arquimedianidad de $\mathbb R$ (Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano) permite encontrar $N\ge1$ con $\nu_{\mathbb R}(N)\varepsilon>C-1$. Para todo $n\ge N$, la monotonía de los numerales y (14.9.6) dan $(1+\varepsilon)^n>C$. Por la estricta monotonía de las potencias positivas,

$$
1<\sqrt[n]{C}<1+\varepsilon.
$$

Esto demuestra $\sqrt[n]{C}\to1$.

Si $0<C<1$, apliquemos el caso anterior a $C^{-1}>1$. La identidad de potencias producto y la unicidad de raíz implican

$$
\sqrt[n]{C}\,\sqrt[n]{C^{-1}}=1,
$$

porque el producto es positivo y su potencia $n$-ésima vale $1$. Para un $\varepsilon>0$, elijamos $0<\eta<\min\{\varepsilon,1\}$. Eventualmente $1<\sqrt[n]{C^{-1}}<1+\eta$, luego

$$
1-\varepsilon<\frac1{1+\eta}
<\sqrt[n]{C}<1.
$$

La primera desigualdad se deduce de $(1+\eta)(1-\eta)=1-\eta^2<1$ y $\eta<\varepsilon$. Así también $\sqrt[n]{C}\to1$. El valor elegido en el índice cero carece de efecto. ∎

---

### Teorema 14.9.6 — Criterio de la raíz

Sea $a\in\mathbb R^{\mathbb N}$ y supongamos que la sucesión $R(a)$ converge a un **número real** $L$. Entonces $L\ge0$ y:

1. Si $L<1$, la serie $\sum_{n=0}^{\infty}a_n$ **converge absolutamente**.
2. Si $L>1$, la serie $\sum_{n=0}^{\infty}a_n$ **diverge**: sus términos no tienden a cero.
3. Si $L=1$, estas hipótesis no bastan para decidir. En §14.9.9 construiremos series de ambos comportamientos con este mismo límite.

La prueba establece también las versiones útiles **sin presuponer un límite**: basta que existan $0<q<1$ y $N\ge1$ con $R(a)_n\le q$ para todo $n\ge N$ para concluir convergencia absoluta; basta que existan $r>1$ y $N\ge1$ con $R(a)_n\ge r$ para todo $n\ge N$ para concluir divergencia.

**Demostración.**

Todos los $R(a)_n$ son no negativos, por lo que $L\ge0$. Si $L<1$, fijemos $q:=(1+L)/2$. Se cumple $0<q<1$ y $L<q$. La definición de límite aplicada a la tolerancia $q-L$ proporciona $N\ge1$ tal que $R(a)_n<q$ para $n\ge N$. Elevando a la potencia natural positiva $n$, la monotonía del lema inicial muestra

$$
|a_n|=R(a)_n^{\,n}<q^n\quad(n\ge N).
$$

Los términos $q^n$ forman una serie geométrica convergente por Teorema 14.3.5 — Convergencia y suma de la serie geométrica para $|r|<1$; la dominación absoluta eventual Corolario 14.8.4 — Dominación absoluta eventual prueba la convergencia absoluta de la serie original. La misma comparación funciona si la cota $R(a)_n\le q$ se da directamente, sin límite.

Si $L>1$, tomemos $r:=(1+L)/2>1$. Eventualmente $R(a)_n>r$ y, por monotonía,

$$
|a_n|>r^n\ge1\qquad(n\ge N),
$$

pues $r^0=1$ y la recurrencia de las potencias conserva la cota $r^n\ge1$. Por definición, $a_n\not\to0$ (basta la tolerancia $1$), así que la condición necesaria Corolario 14.2.5 — Criterio de divergencia por el término general implica divergencia. La versión con $R(a)_n\ge r$ es idéntica, usando $|a_n|\ge1$. El valor $L=1$ no permite obtener de la sola convergencia ninguna de las dos cotas estrictas que acabamos de utilizar; los contraejemplos de §14.9.9 establecen formalmente la indecisión anunciada. ∎

> **Lectura del criterio.** La raíz compara $|a_n|$ con $q^n$ **para el mismo índice $n$**. No exige que cada término sea no nulo: $\sqrt[n]{0}=0$ está definida para $n\ge1$. Si la sucesión de raíces carece de límite, las dos versiones de cota eventual siguen siendo válidas; el teorema no inventa un límite superior extendido $+\infty$.

---

### Teorema 14.9.7 — Criterio de la razón con denominadores eventualmente no nulos

Sea $a\in\mathbb R^{\mathbb N}$ y supongamos que existe $N_0$ tal que $a_n\ne0$ para todo $n\ge N_0$. Definimos la sucesión total

$$
q:=\operatorname{quo}_0\bigl(\operatorname{Abs}(a)^{\langle1\rangle},
\operatorname{Abs}(a)\bigr).
$$

Desde $N_0$, y **sólo desde allí**, $q_n=|a_{n+1}|/|a_n|$. Si $q_n\to L\in\mathbb R$, entonces $L\ge0$ y:

1. Si $L<1$, la serie $\sum a_n$ converge absolutamente.
2. Si $L>1$, la serie $\sum a_n$ diverge porque $a_n\not\to0$.
3. Si $L=1$, el criterio no determina la convergencia (véase §14.9.9).

Sin requerir la existencia de $L$, las conclusiones siguen siendo válidas cuando se cuenta, respectivamente, con una cota eventual $q_n\le c<1$ con $c>0$, o con $q_n\ge d>1$, siempre manteniendo la hipótesis de no anulación desde $N_0$.

**Demostración.**

La sucesión $q$ existe por Definición 14.6.2 — Cociente secuencial totalizado y cociente eventual y es no negativa en todos los índices: en los denominadores nulos se asigna cero, y los demás son cocientes de magnitudes no negativas por números positivos. De ahí $L\ge0$. Para $L<1$, escojamos $c:=(1+L)/2$; satisface $0<c<1$ y $L<c$. Existe $N\ge N_0$ tal que $q_n<c$ para todo $n\ge N$, y por tanto

$$
|a_{n+1}|\le c|a_n|\qquad(n\ge N).
\tag{14.9.7}
$$

La inducción sobre $j$ aplicada a (14.9.7) da $|a_{N+j}|\le|a_N|c^j$. Como $c>0$, $c^N>0$, y definimos el real no negativo $C:=|a_N|(c^N)^{-1}$. La identidad $c^{N+j}=c^Nc^j$, obtenida por inducción desde la recurrencia de las potencias, permite escribir para todos los $n\ge N$ (con $n=N+j$):

$$
\boxed{|a_n|\le Cc^n.}
\tag{14.9.8}
$$

La serie geométrica de $c^n$ converge (Teorema 14.3.5 — Convergencia y suma de la serie geométrica para $|r|<1$), y también la de $Cc^n$: si $C>0$, por escalamiento no nulo Proposición 14.6.1 — Multiplicación de una serie por un escalar no nulo; si $C=0$, por la serie nula Proposición 14.1.6 — Estabilización de sumas parciales cuando los términos tardíos son nulos. La dominación absoluta eventual Corolario 14.8.4 — Dominación absoluta eventual concluye. Este argumento prueba igualmente la versión con cota $q_n\le c$ sin límite.

Si $L>1$, elijamos $d:=(1+L)/2>1$. Eventualmente $q_n>d$ y, con $N\ge N_0$ apropiado,

$$
|a_{N+j}|\ge|a_N|d^j\ge|a_N|>0
\qquad(j\in\mathbb N).
$$

La desigualdad se prueba por inducción; la segunda usa $d^j\ge1$, y la última la hipótesis $a_N\ne0$. La tolerancia $\varepsilon=|a_N|$ impide que $a_n\to0$, así que la serie diverge por Corolario 14.2.5 — Criterio de divergencia por el término general. El mismo razonamiento cubre la cota eventual $q_n\ge d>1$. La frontera $L=1$ queda resuelta por los ejemplos de §14.9.9, no por este argumento. ∎

> **Hipótesis insustituible.** No se permite dividir por $|a_n|$ cuando pueda ser cero arbitrariamente tarde. Si una serie tiene términos nulos en índices no acotados, el criterio de la razón en esta forma no se aplica, pero la serie podría converger o divergir. La definición totalizada del cociente no debe ocultar esa restricción.

---

### Proposición 14.9.8 — Un límite de razones determina el límite de las raíces

En las hipótesis de no anulación eventual del teorema anterior, si

$$
\lim_{n\to\infty}\frac{|a_{n+1}|}{|a_n|}=L
\qquad(L\in\mathbb R),
$$

entonces

$$
\boxed{\lim_{n\to\infty}\sqrt[n]{|a_n|}=L,}
$$

entendiendo el segundo límite mediante la sucesión total $R(a)$ de (14.9.3). En particular, el criterio de razón con límite existente nunca produce un límite de raíz distinto: ambos entregan el mismo umbral $L$.

**Demostración.**

Sea $q_n=|a_{n+1}|/|a_n|$ en la cola legítima y $q_n\to L$. Por no negatividad, $L\ge0$. Fijemos dos constantes positivas $r,R$ tales que

$$
0<r<L<R
$$

si $L>0$. Por convergencia existe un índice $N\ge1$ a partir del cual todos los cocientes están entre $r$ y $R$. Las mismas inducciones de §14.9.7, aplicadas a ambas desigualdades, proporcionan constantes **positivas**

$$
C:=|a_N|(r^N)^{-1},
\qquad D:=|a_N|(R^N)^{-1},
$$

para las cuales

$$
Cr^n\le|a_n|\le DR^n\qquad(n\ge N).
$$

Por monotonía de la raíz y la identidad (14.9.5), para $n\ge N$,

$$
\boxed{r\sqrt[n]{C}\le R(a)_n\le R\sqrt[n]{D}.}
\tag{14.9.9}
$$

El lema Lema 14.9.5 — Las raíces enésimas de una constante positiva tienden a uno y la compatibilidad del límite con multiplicación por una constante hacen converger las cotas izquierda y derecha a $r$ y $R$. Para verificar exactamente $R(a)_n\to L$, demos un $\varepsilon>0$: elegimos $r,R>0$ tales que $L-\varepsilon/2<r<L<R<L+\varepsilon/2$ (si $\varepsilon$ es grande, la condición $r>0$ sigue siendo posible porque $L>0$). A partir de un índice suficientemente grande, los términos de las cotas en (14.9.9) difieren de $r,R$, respectivamente, en menos de $\varepsilon/2$. Se obtiene entonces $L-\varepsilon<R(a)_n<L+\varepsilon$, como exige la definición de límite.

Si $L=0$, sea $\varepsilon>0$ y elijamos $0<c<\min\{1,\varepsilon/2\}$. Eventualmente $0\le q_n<c$; la inducción anterior aporta un $D>0$ con $|a_n|\le Dc^n$ para todos los índices de una cola. La monotonía de la raíz da $0\le R(a)_n\le c\sqrt[n]{D}$. Como $\sqrt[n]{D}\to1$, eventualmente $\sqrt[n]{D}<2$, y $0\le R(a)_n<2c<\varepsilon$. Por tanto también $R(a)_n\to0=L$. No se ha requerido calcular logaritmos ni utilizar una forma extendida de $\limsup$. ∎

---

### Proposición 14.9.9 — La frontera de ambos criterios es indecisiva

Existen dos series de términos **estrictamente positivos** que tienen, simultáneamente, límite de razones igual a $1$ y límite de raíces igual a $1$, pero comportamientos opuestos: una diverge y la otra converge.

**Demostración.**

**Ejemplo divergente.** Utilicemos la sucesión armónica ya cerrada,

$$
h_n:=\nu_{\mathbb R}(n+1)^{-1}>0.
$$

Su serie diverge por Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica, pero $h_n\to0$ por Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero. Sus razones están definidas para todo $n$ y la aritmética del cuerpo y de los numerales da

$$
\frac{h_{n+1}}{h_n}
=\frac{\nu_{\mathbb R}(n+1)}{\nu_{\mathbb R}(n+2)}
=1-h_{n+1}\longrightarrow1.
$$

La convergencia de la cola $h_{n+1}$ se obtiene de Definición 13.2.3 — Cola reindexada de una sucesión y la conservación de los límites de sucesiones por desplazamiento. Proposición 14.9.8 — Un límite de razones determina el límite de las raíces concluye que $\sqrt[n]{h_n}\to1$ en los índices positivos.

**Ejemplo convergente.** Definamos, por Separación en $\mathbb N\times\mathbb R$, la sucesión positiva

$$
\boxed{b_n:=h_nh_{n+1}
=\frac1{\nu_{\mathbb R}(n+1)\nu_{\mathbb R}(n+2)}.}
$$

De la identidad $\nu_{\mathbb R}(n+2)-\nu_{\mathbb R}(n+1)=1$ se sigue, por multiplicación por los inversos de ambos numerales, que

$$
b_n=h_n-h_{n+1}.
$$

La recursión de sumas parciales prueba por inducción, sin ninguna permutación infinita,

$$
\sum_{k=0}^{N}b_k=h_0-h_{N+1}=1-h_{N+1}
\qquad(N\in\mathbb N).
$$

Como $h_{N+1}\to0$, las sumas parciales convergen a $1$, y así $\sum_{k=0}^{\infty}b_k=1$. Por otra parte, la cancelación de factores **positivos** da

$$
\frac{b_{n+1}}{b_n}
=\frac{\nu_{\mathbb R}(n+1)}{\nu_{\mathbb R}(n+3)}
=1-(1+1)h_{n+2}\longrightarrow1.
$$

De nuevo Proposición 14.9.8 — Un límite de razones determina el límite de las raíces proporciona $\sqrt[n]{b_n}\to1$. En los dos ejemplos se satisfacen las hipótesis de ambos criterios y sus límites son idénticos a $1$, pero sólo la segunda serie converge. Esto demuestra que ninguno de los criterios permite concluir nada en la frontera $L=1$. ∎

> **Diagnóstico pedagógico.** El cociente mide un cambio *entre términos consecutivos*; la raíz compara la magnitud del término *con una escala geométrica desde el origen*. Que ambos límites den $1$ expresa la ausencia de una separación exponencial estricta respecto de esa escala; no significa que las sumas parciales se comporten igual.

---

Los criterios de razón y raíz están ahora fundamentados sin notación de raíces anterior a su teorema de existencia, sin divisiones por cero y sin confundir la frontera $1$ con una conclusión de convergencia. El siguiente frente, **§14.10 — Reordenamientos y estabilidad de la suma bajo convergencia absoluta**, deberá distinguir expresamente una permutación de índices de una partición meramente finita: modificar el orden de una suma infinita exige un teorema, no una aplicación informal de la conmutatividad finita.

---
