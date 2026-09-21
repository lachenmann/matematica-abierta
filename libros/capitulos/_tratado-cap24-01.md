## 24.1. Series centradas y conjunto de convergencia {#sec-ta-24-1}

### Definición 24.1.1 — Serie de potencias real centrada
Sean un centro $c\in\mathbb R$ y una sucesión de coeficientes **dada** $a:\mathbb N\to\mathbb R$, $n\mapsto a_n$. Para $n\in\mathbb N$ y $x\in\mathbb R$ escribimos

$$
\boxed{p_n^{a,c}(x):=a_n(x-c)^n.}
\tag{24.1.1}
$$

Llamamos **serie de potencias real centrada en $c$ y con coeficientes $a$** a la serie de funciones asociada a la familia $(p_n^{a,c})_{n\in\mathbb N}$ en el sentido del Capítulo 23. Su notación es

$$
\boxed{\sum_{n=0}^{\infty}a_n(x-c)^n.}
\tag{24.1.2}
$$

La escritura (24.1.2) designa inicialmente un **proceso de sumación**, no una igualdad con un número real ni una función suma definida sobre toda $\mathbb R$. El índice $n$, el centro y los coeficientes son datos diferenciados: cambiar $c$ o la sucesión $a$ cambia, en general, la serie considerada.

### Proposición 24.1.2 — Construcción tipada de los términos y las sumas parciales
Para todo $c\in\mathbb R$ y toda $a:\mathbb N\to\mathbb R$ existen una única sucesión de funciones

$$
\mathbf p^{a,c}:\mathbb N\longrightarrow\mathbb R^{\mathbb R},
\qquad n\longmapsto p_n^{a,c},
\tag{24.1.3}
$$

cuyos términos tienen dominio exacto $\mathbb R$, codominio $\mathbb R$ y satisfacen (24.1.1), y una única sucesión de sumas parciales

$$
\mathbf S^{a,c}:=\operatorname{PS}_{\mathbb R}(\mathbf p^{a,c}):
\mathbb N\longrightarrow\mathbb R^{\mathbb R}
\tag{24.1.4}
$$

para la cual, para todo $N\in\mathbb N$ y $x\in\mathbb R$,

$$
\boxed{S_N^{a,c}(x)=\sum_{n=0}^{N}a_n(x-c)^n.}
\tag{24.1.5}
$$

Estas funciones están definidas en toda la recta aunque la serie infinita pueda divergir en algunos puntos.

**Demostración.**
Fijemos $n\in\mathbb N$. La sucesión $a$ proporciona un único real $a_n$. Para cualquier $x\in\mathbb R$, la resta $x-c$, su potencia natural y el producto por $a_n$ son valores reales únicos por la estructura de cuerpo y por «Potencias naturales de un número real». Por tanto, Separación en el producto existente $\mathbb R\times\mathbb R$ define

$$
G_n:=\{\langle x,r\rangle\in\mathbb R\times\mathbb R:
 r=a_n(x-c)^n\}.
$$

Este conjunto es el grafo de una función de dominio $\mathbb R$ y codominio $\mathbb R$. La igualdad tipada de funciones («Criterio de igualdad de funciones») asegura su unicidad; la existencia de $\mathbb R^{\mathbb R}$ («Existencia de $B^A$») permite considerarla elemento de ese conjunto. Separación en $\mathbb N\times\mathbb R^{\mathbb R}$ forma entonces el grafo

$$
G_{\mathbf p}:=\{\langle n,f\rangle\in
\mathbb N\times\mathbb R^{\mathbb R}:
\forall x\in\mathbb R,\ f(x)=a_n(x-c)^n\}.
$$

Para cada $n$ existe exactamente un $f$ que satisface la condición, a saber, la función de grafo $G_n$. Así obtenemos una sola función $\mathbf p^{a,c}$ del tipo (24.1.3), sin escoger separadamente funciones para una infinidad de índices. Aplicamos ahora la operación de sumas parciales de funciones ya construida en «Sucesión de sumas parciales de funciones» para el dominio $E=\mathbb R$. Produce la sucesión única (24.1.4). Al evaluar en un $x$ arbitrario, su construcción coincide con la sucesión de sumas parciales numéricas de los valores $p_n^{a,c}(x)$ («Evaluación en un punto y sucesión real inducida» y «Sucesión de sumas parciales y serie numérica»), de donde resulta (24.1.5). $\square$

**Precisión.** No hemos demostrado que $\mathbf S^{a,c}$ tenga límite puntual en toda la recta. La existencia de cada función $S_N^{a,c}$, que implica únicamente una suma finita, no contiene esa afirmación.

### Definición 24.1.3 — Conjunto de convergencia
Para los datos fijos $a$ y $c$, definimos el **conjunto de convergencia** de la serie de potencias como

$$
\boxed{C(a,c):=\Bigl\{x\in\mathbb R:
\exists L\in\mathbb R\ \forall\varepsilon>0\ 
\exists N_0\in\mathbb N\ \forall N\in\mathbb N\,
\bigl(N\ge N_0\Rightarrow |S_N^{a,c}(x)-L|<\varepsilon\bigr)
\Bigr\}.}
\tag{24.1.6}
$$

Es un **conjunto**: se obtiene por Separación sobre $\mathbb R$ a partir del predicado de convergencia de la sucesión real $N\mapsto S_N^{a,c}(x)$, equivalente a la convergencia de la serie numérica de términos $n\mapsto a_n(x-c)^n$ («Convergencia, divergencia y suma de una serie»). No se trata de una comprensión irrestricta. Tampoco hemos escogido simultáneamente un límite para cada $x$: la definición sólo determina los puntos que satisfacen una propiedad.

Para $x\notin C(a,c)$ la serie no tiene suma real en ese punto; la expresión (24.1.2) puede seguir nombrando el proceso formal, pero no se evaluará como si fuera una función suma allí. La pertenencia $x\in C(a,c)$ no se declara decidible ni efectivamente comprobable para una sucesión arbitraria de coeficientes.

### Proposición 24.1.4 — El centro siempre pertenece al conjunto de convergencia
Para toda sucesión real $a$ y todo centro $c\in\mathbb R$,

$$
\boxed{c\in C(a,c),\qquad
\sum_{n=0}^{\infty}a_n(c-c)^n=a_0.}
\tag{24.1.7}
$$

La segunda igualdad se entiende como convergencia de la serie numérica en el punto $c$ hacia $a_0$.

**Demostración.**
Al evaluar en $x=c$, tenemos $x-c=0$. La cláusula inicial de las potencias da $0^0=1$; por tanto, **el término de índice cero es $a_0$**, y no cero ni una expresión indefinida. Para $n\ge1$, la recursión de potencias da $0^n=0$, lo que se verifica por inducción a partir de $0^1=0^0\cdot0=0$. En consecuencia,

$$
p_0^{a,c}(c)=a_0,
\qquad p_n^{a,c}(c)=0\quad(n\ge1).
$$

La recursión de sumas parciales comienza con $S_0^{a,c}(c)=a_0$ y en cada etapa posterior suma cero. Una segunda inducción produce

$$
S_N^{a,c}(c)=a_0\qquad\text{para todo }N\in\mathbb N.
$$

La sucesión constante converge a $a_0$: para cualquier $\varepsilon>0$ basta el índice explícito $N_0=0$, pues $|S_N^{a,c}(c)-a_0|=0<\varepsilon$ para todo $N$. La definición (24.1.6) demuestra $c\in C(a,c)$ y establece (24.1.7). $\square$

**Lectura.** Ninguna condición sobre el crecimiento de $(a_n)$ fue necesaria: en el centro desaparecen todos los términos de índice positivo. Esto demuestra que $C(a,c)$ no es vacío, pero aún no determina su extensión fuera del centro.

### Proposición 24.1.5 — Existencia y unicidad de la función suma sobre su dominio exacto
Existe una única función

$$
\boxed{F_{a,c}:C(a,c)\longrightarrow\mathbb R}
\tag{24.1.8}
$$

que, para cada $x\in C(a,c)$, satisface

$$
\boxed{F_{a,c}(x)=\lim_{N\to\infty}S_N^{a,c}(x)
=\sum_{n=0}^{\infty}a_n(x-c)^n.}
\tag{24.1.9}
$$

No se atribuye a $F_{a,c}$ ningún valor fuera de su dominio $C(a,c)$.

**Demostración.**
Por (24.1.6), fijado $x\in C(a,c)$ existe al menos un real $L$ límite de la sucesión numérica $N\mapsto S_N^{a,c}(x)$. El teorema de unicidad del límite «Unicidad del límite real» prueba que es **uno solo**. El conjunto $C(a,c)\times\mathbb R$ existe; Separación determina

$$
G_F:=\{\langle x,L\rangle\in C(a,c)\times\mathbb R:
S_N^{a,c}(x)\longrightarrow L\}.
$$

La existencia y unicidad verificadas para cada $x$ hacen de $G_F$ el grafo de una función de dominio exacto $C(a,c)$ y codominio $\mathbb R$. Otra función del mismo tipo con (24.1.9) tendría idénticos valores y, por «Criterio de igualdad de funciones», sería igual a ésta. Por la proposición anterior, además, $F_{a,c}(c)=a_0$. En lugar de una elección simultánea de límites, hemos utilizado una definición relacional de valor único y Separación. $\square$

### Lema 24.1.6 — Acotación de los términos al converger una serie numérica
Sea $b:\mathbb N\to\mathbb R$ una sucesión cuya serie numérica $\sum_{n=0}^{\infty}b_n$ converge. Entonces existe un real $M>0$ tal que

$$
\boxed{|b_n|\le M\qquad(n\in\mathbb N).}
\tag{24.1.10}
$$

**Demostración.**
La condición necesaria de convergencia de una serie («Condición necesaria de convergencia: el término general tiende a cero») da $b_n\to0$. Por «Toda sucesión real convergente es acotada», toda sucesión real convergente es acotada. Por consiguiente existe $B\in\mathbb R$ con $|b_n|\le B$ para todo natural $n$. Podemos poner $M:=B+1$, que es estrictamente positivo porque $B\ge|b_0|\ge0$; así obtenemos (24.1.10). Esta prueba no escoge un índice o una cota para cada $n$: extrae **una sola cota** de un resultado previo. $\square$

### Teorema 24.1.7 — Convergencia absoluta hacia el interior
Sean $c\in\mathbb R$, $a:\mathbb N\to\mathbb R$ y $y\in C(a,c)$ con $y\ne c$. Entonces, para **todo** $x\in\mathbb R$ tal que

$$
\boxed{|x-c|<|y-c|,}
\tag{24.1.11}
$$

la serie de potencias $\sum_{n=0}^{\infty}a_n(x-c)^n$ converge **absolutamente**. En particular, $x\in C(a,c)$.

**Demostración.**
Fijemos los datos y un punto $x$ que cumpla (24.1.11). Puesto que $y\in C(a,c)$, por definición converge la serie numérica de términos

$$
b_n:=a_n(y-c)^n\qquad(n\in\mathbb N).
$$

El lema anterior proporciona un **mismo** real $M>0$ tal que

$$
|a_n(y-c)^n|\le M\qquad(n\in\mathbb N).
\tag{24.1.12}
$$

La hipótesis $y\ne c$ legitima la división por $y-c$. Definamos los reales

$$
t:=\frac{x-c}{y-c},\qquad q:=|t|=
\frac{|x-c|}{|y-c|}.
$$

Como $|y-c|>0$, la desigualdad estricta (24.1.11) implica $0\le q<1$. Tenemos $x-c=(y-c)t$. Demostremos, sin importar silenciosamente una ley de exponentes, que

$$
\bigl((y-c)t\bigr)^n=(y-c)^nt^n\qquad(n\in\mathbb N).
\tag{24.1.13}
$$

En $n=0$, ambos miembros valen $1$ por la convención de potencias naturales, incluso si $x=c$ y $t=0$. Si la igualdad vale en $n$, la recursión de potencias, la hipótesis inductiva y la asociatividad y conmutatividad del producto real dan

$$
\begin{aligned}
\bigl((y-c)t\bigr)^{n+1}
&=\bigl((y-c)t\bigr)^n((y-c)t)\\
&=(y-c)^nt^n(y-c)t\\
&=(y-c)^{n+1}t^{n+1}.
\end{aligned}
$$

Así, (24.1.13) se sigue por inducción. Aplicando la multiplicatividad del valor absoluto y «El valor absoluto conmuta con las potencias naturales», obtenemos, para cada $n$,

$$
\begin{aligned}
|a_n(x-c)^n|
&=|a_n(y-c)^nt^n|\\
&=|a_n(y-c)^n|\,|t|^n\\
&\le Mq^n.
\end{aligned}
\tag{24.1.14}
$$

Aquí $q^n\ge0$; por eso es legítima la última desigualdad. La serie geométrica $\sum_{n=0}^{\infty}q^n$ converge por «Convergencia y suma de la serie geométrica para $». Como $M>0$, «Multiplicación de una serie por un escalar no nulo» autoriza multiplicar la serie numérica convergente por el escalar no nulo $M$; sus sumas parciales son precisamente $M$ veces las sumas parciales geométricas. En consecuencia, $\sum_{n=0}^{\infty}Mq^n$ converge. El criterio de comparación directa «Criterio de comparación directa», aplicado a (24.1.14), muestra que

$$
\sum_{n=0}^{\infty}|a_n(x-c)^n|
\quad\text{converge}.
$$

Esto es convergencia absoluta según «Serie de valores absolutos; convergencia absoluta y condicional». Por «La convergencia absoluta implica convergencia ordinaria» implica convergencia ordinaria y, por (24.1.6), $x\in C(a,c)$. No se eligió una sucesión de testigos ni se intercambiaron límites: se usó una cota numérica común y una sola comparación geométrica. $\square$

**Consecuencia geométrica inmediata.** Si $y\in C(a,c)$ y $y\ne c$, poniendo $d:=|y-c|>0$ obtenemos

$$
\boxed{(c-d,c+d)\subseteq C(a,c),}
\tag{24.1.15}
$$

y la convergencia es absoluta en cada punto de ese intervalo. En efecto, $c-d<x<c+d$ equivale a $|x-c|<d$; aplicamos el teorema. **La conclusión es puntual**, todavía no una afirmación de uniformidad en todo ese intervalo abierto ni sobre sus extremos.

**Frontera y transición.** El conjunto de convergencia está bien definido, contiene siempre el centro y posee la propiedad de inclusión hacia distancias estrictamente menores que cualquier distancia donde ya se conozca convergencia. El paso siguiente será construir el conjunto de distancias admitidas, demostrar las condiciones de existencia de su supremo —separando el caso no acotado— y **sólo entonces** definir el radio de convergencia. La pertenencia de los puntos a distancia exactamente igual al radio requerirá análisis independiente. La continuidad, integración y derivación de $F_{a,c}$ no se afirman aún.
---
