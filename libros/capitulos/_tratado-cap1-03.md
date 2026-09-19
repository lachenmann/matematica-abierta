## 1.3. Teorema de recursión {#sec-ta-1-3}

La inducción permite **demostrar** propiedades de todos los naturales a partir de un caso inicial y un paso sucesor. La recursión cumple una función distinta y complementaria: permite **definir** objetos paso a paso a lo largo de $\mathbb N$.

Antes de introducir las ecuaciones recursivas de la suma debemos justificar que una regla de ese tipo determina realmente una función sobre todos los naturales y que la determina de manera única. No basta, por tanto, con anunciar una receta iterativa.

La estrategia será finitaria en cada etapa:

$$
\text{fragmentos finitos}
\longrightarrow
\text{extensión}
\longrightarrow
\text{coherencia}
\longrightarrow
\text{función global}.
$$

Primero construiremos soluciones sobre segmentos finitos $S(n)$; después veremos que cada una se prolonga al paso siguiente; probaremos que dos aproximaciones coinciden donde sus dominios se solapan; finalmente reuniremos todos esos valores en un único grafo. Esta arquitectura hará visible, además, por qué no necesitamos escoger simultáneamente una aproximación para cada $n$ y, por tanto, por qué no interviene el axioma de elección.

### Definición 1.3.1 — Restricción de una función {#ta-restriccion-funcion}

*Glosario: [restricción de una función](../otros/tratado-de-analisis-glosario.md#gl-restriccion-funcion)*

Si $f:A\to B$ y $C\subseteq A$, la **restricción** de $f$ a $C$ es la aplicación

$$
f\upharpoonright C:C\to B
$$

cuyo grafo es $G_f\cap(C\times B)$.

### Proposición 1.3.2 — Existencia y unicidad de la restricción {#ta-unicidad-restriccion}

La regla anterior determina una única función $f\upharpoonright C:C\to B$.

**Demostración.**  
Para cada $c\in C\subseteq A$, el grafo de $f$ contiene un único par $\langle c,b\rangle$ con $b\in B$; la intersección con $C\times B$ conserva exactamente esos pares. La definición de función y el criterio de igualdad de funciones dan existencia y unicidad. ∎

La restricción nos permite comparar una solución más larga con sus etapas anteriores. Introducimos ahora los fragmentos finitos que servirán como piezas de la construcción global.

### Definición 1.3.3 — Aproximación finita de una recursión {#ta-aproximacion-finita-recursion}

*Glosario: [aproximación finita de una recursión](../otros/tratado-de-analisis-glosario.md#gl-aproximacion-finita-recursion)*

Sean $X$ un conjunto, $x_0\in X$, $g:X\to X$ y $n\in\mathbb N$. Una **$n$-aproximación** para $(X,x_0,g)$ es una función

$$
h:S(n)\to X
$$

tal que

$$
h(0)=x_0
$$

y, para todo $k\in\mathbb N$ con $S(k)\in S(n)$,

$$
h(S(k))=g(h(k)).
$$

Si $S(k)\in S(n)$, la transitividad de $S(n)$ y $k\in S(k)$ garantizan que $k\in S(n)$, por lo que $h(k)$ está definido.

### Lema 1.3.4 — Extensión de una aproximación {#ta-extension-aproximacion}

Si $h:S(n)\to X$ es una $n$-aproximación, existe una única $(S(n))$-aproximación

$$
h^+:S(S(n))\to X
$$

que extiende a $h$, y necesariamente

$$
h^+(S(n))=g(h(n)).
$$

**Demostración.**  
Por la Proposición 1.2.2, $S(n)\notin S(n)$. Añadimos al grafo de $h$ el único par nuevo

$$
\langle S(n),g(h(n))\rangle.
$$

El resultado es un grafo funcional sobre

$$
S(S(n))=S(n)\cup\{S(n)\}.
$$

Si $S(k)\in S(S(n))$, o bien $S(k)\in S(n)$ y rige la recursión anterior, o bien $S(k)=S(n)$; por inyectividad del sucesor, $k=n$, y rige la nueva igualdad. La unicidad queda forzada por la restricción previa y el valor en $S(n)$. ∎

### Teorema 1.3.5 — Existencia y unicidad de aproximaciones finitas {#ta-existencia-aproximaciones-finitas}

Para cada $n\in\mathbb N$ existe una única $n$-aproximación para $(X,x_0,g)$.

**Demostración.**  
Inducimos sobre $n$. Para $n=0$, $S(0)=\{0\}$ y existe una única función que envía $0$ a $x_0$; la ecuación recursiva es vacía porque ningún sucesor es $0$. En el paso inductivo, la existencia y unicidad de la extensión vienen del lema anterior. Cualquier otra aproximación en $S(S(n))$, restringida a $S(n)$, es la única $n$-aproximación y su valor nuevo está forzado por la recursión. ∎

### Lema 1.3.6 — Coherencia de las aproximaciones {#ta-coherencia-aproximaciones}

Sean $h:S(n)\to X$ y $q:S(m)\to X$ aproximaciones para los mismos datos. Si

$$
k\in S(n)\cap S(m),
$$

entonces $h(k)=q(k)$.

**Demostración.**  
Inducimos sobre $k$ la afirmación de que cualesquiera dos aproximaciones cuyos dominios contienen a $k$ coinciden en $k$. En $0$ ambas toman $x_0$. Si coinciden en $k$ y ambos dominios contienen $S(k)$, por transitividad contienen también a $k$, y

$$
h(S(k))=g(h(k))=g(q(k))=q(S(k)).
$$

∎

Ya tenemos las dos propiedades necesarias para ensamblar una función global: para cada longitud existe una única aproximación y todas las aproximaciones son compatibles entre sí. El paso final consiste en reunir los valores que esas aproximaciones asignan a cada natural.

### Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$ {#ta-teorema-recursion-naturales}

*Glosario: [recursión](../otros/tratado-de-analisis-glosario.md#gl-recursion)*

Sean $X$ un conjunto, $x_0\in X$ y $g:X\to X$. Existe una única función

$$
f:\mathbb N\to X
$$

tal que

$$
\boxed{f(0)=x_0}
$$

y

$$
\boxed{f(S(n))=g(f(n))}
\qquad(n\in\mathbb N).
$$

**Demostración.**  
Por existencia del producto cartesiano existe $\mathbb N\times X$. Definimos por separación $G\subseteq\mathbb N\times X$ declarando que

$$
\langle k,x\rangle\in G
$$

si existe un $n\in\mathbb N$ y una $n$-aproximación $h:S(n)\to X$ con $k\in S(n)$ y $h(k)=x$.

Para cada $k$, la $k$-aproximación existe y su dominio $S(k)$ contiene a $k$, de modo que existe un valor. La coherencia garantiza que dos aproximaciones cualesquiera que contengan a $k$ le asignan el mismo valor. Por tanto $G$ es el grafo de una función $f:\mathbb N\to X$.

Toda aproximación toma $x_0$ en $0$, luego $f(0)=x_0$. Para $n\in\mathbb N$, la aproximación de índice $S(n)$ contiene a $n$ y a $S(n)$, así que por coherencia y por su ecuación recursiva

$$
f(S(n))=g(f(n)).
$$

Si $f,q:\mathbb N\to X$ satisfacen ambas ecuaciones, el conjunto

$$
A=\{n\in\mathbb N:f(n)=q(n)\}
$$

contiene $0$ y es estable por sucesor; por inducción, $A=\mathbb N$, y $f=q$.

La construcción de $G$ es definible por separación y no selecciona simultáneamente una aproximación para cada $n$. No interviene elección. ∎

### Corolario 1.3.8 — Recursión con parámetros {#ta-recursion-parametros}

*Glosario: [recursión con parámetros](../otros/tratado-de-analisis-glosario.md#gl-recursion-parametros)*

Sean $P,X$ conjuntos, $b:P\to X$ y $r:P\times X\to X$. Existe una única función

$$
F:P\times\mathbb N\to X
$$

tal que

$$
F(p,0)=b(p)
$$

y

$$
F(p,S(n))=r(p,F(p,n)).
$$

**Demostración.**  
Para cada parámetro $p$, el Teorema 1.3.7 da una única función recursiva $f_p$. El grafo de $F$ se define por separación en $(P\times\mathbb N)\times X$ mediante la fórmula «$x$ es el valor en $n$ de la única función recursiva asociada a $p$». La unicidad local garantiza funcionalidad y elimina cualquier necesidad de elección. ∎
