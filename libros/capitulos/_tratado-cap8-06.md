## 8.6. Una sucesión de Cauchy es acotada {#sec-ta-8-6}

La condición de Cauchy controla directamente sólo una cola de la sucesión. Si fijamos una tolerancia racional positiva, obtenemos un índice a partir del cual todos los términos están próximos entre sí. Esto basta para acotar la cola alrededor de uno de sus términos.

Queda, sin embargo, un problema que no debe ocultarse bajo la frase “los términos anteriores son finitos”: debemos demostrar dentro de la infraestructura ya construida que todo segmento inicial

$$
q_0,q_1,\ldots,q_{N-1}
$$

admite una cota racional común.

Primero fijaremos qué significa que una sucesión racional sea acotada y después resolveremos por inducción el segmento inicial.

### Definición 8.6.1 — Sucesión racional acotada

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional. Diremos que $q$ es acotada si existe $M\in\mathbb Q$ tal que

$$
0_{\mathbb Q}\leq M
$$

y

$$
\forall n\in\mathbb N,\qquad
|q_n|\leq M.
$$

Equivalentemente, todos los términos de la sucesión quedan contenidos en el intervalo racional simétrico determinado por $M$.

La exigencia $0_{\mathbb Q}\leq M$ no es una restricción artificial: el valor absoluto de cada término es ya no negativo.

### Lema 8.6.2 — Acotación de todo segmento inicial

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional. Para todo $N\in\mathbb N$ existe $M\in\mathbb Q$ tal que

$$
0_{\mathbb Q}\leq M
$$

y

$$
\forall n\in\mathbb N,\qquad
n<N\Longrightarrow |q_n|\leq M.
$$

**Demostración.**

Demostraremos la afirmación por inducción sobre $N$.

**Caso base.** Sea $N=0$. Tomamos

$$
M:=0_{\mathbb Q}.
$$

Se cumple $0_{\mathbb Q}\leq M$. Además no existe $n\in\mathbb N$ con $n<0$: por Teorema 1.6.12 — Orden estricto y pertenencia, $n<0$ equivaldría a $n\in0$, pero $0=\varnothing$. Por tanto

$$
n<0\Longrightarrow |q_n|\leq M
$$

es vacuamente verdadera para todo $n\in\mathbb N$.

**Paso inductivo.** Supongamos que para cierto $N\in\mathbb N$ existe $M\in\mathbb Q$ tal que

$$
0_{\mathbb Q}\leq M
$$

y

$$
n<N\Longrightarrow |q_n|\leq M.
$$

Definimos

$$
M':=M+|q_N|.
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto, $0_{\mathbb Q}\leq |q_N|$. La compatibilidad del orden racional con la suma y las leyes del grupo aditivo implican

$$
0_{\mathbb Q}\leq M',
\qquad
M\leq M',
\qquad
|q_N|\leq M'.
$$

Sea ahora $n\in\mathbb N$ con

$$
n<S(N).
$$

Por Teorema 1.6.12 — Orden estricto y pertenencia,

$$
n\in S(N).
$$

Como

$$
S(N)=N\cup\{N\},
$$

las leyes de pertenencia de la unión dan dos posibilidades:

1. $n\in N$;
2. $n=N$.

En el primer caso, Teorema 1.6.12 — Orden estricto y pertenencia da $n<N$, y por la hipótesis inductiva

$$
|q_n|\leq M\leq M'.
$$

En el segundo caso,

$$
|q_n|=|q_N|\leq M'.
$$

Así, en ambos casos,

$$
n<S(N)\Longrightarrow |q_n|\leq M'.
$$

Hemos construido una cota racional no negativa para el segmento inicial de longitud $S(N)$. El principio de inducción Teorema 1.1.10 — Principio de inducción concluye el resultado para todo $N\in\mathbb N$. ∎

### Teorema 8.6.3 — Toda sucesión racional de Cauchy es acotada

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional de Cauchy. Entonces $q$ es acotada.

**Demostración.**

Como $\mathbb Q$ es un cuerpo ordenado, Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (3) da

$$
0_{\mathbb Q}<1_{\mathbb Q}.
$$

Aplicamos la condición de Cauchy con la tolerancia racional positiva

$$
\varepsilon:=1_{\mathbb Q}.
$$

Por Definición 8.4.1 — Sucesión racional de Cauchy, existe $N\in\mathbb N$ tal que, para cualesquiera $m,n\in\mathbb N$,

$$
N\leq m
\quad\text{y}\quad
N\leq n
$$

implican

$$
d_{\mathbb Q}(q_m,q_n)<1_{\mathbb Q}.
$$

En particular, como $N\leq N$, para todo $n\in\mathbb N$ con $N\leq n$ tenemos

$$
d_{\mathbb Q}(q_n,q_N)<1_{\mathbb Q}.
$$

Por el lema anterior aplicado al mismo $N$, existe $M\in\mathbb Q$ tal que

$$
0_{\mathbb Q}\leq M
$$

y

$$
n<N\Longrightarrow |q_n|\leq M.
$$

Definamos ahora

$$
T:=1_{\mathbb Q}+|q_N|
$$

y

$$
B:=M+T.
$$

Por la no negatividad del valor absoluto y la positividad de $1_{\mathbb Q}$,

$$
0_{\mathbb Q}\leq T.
$$

Como también $0_{\mathbb Q}\leq M$, la compatibilidad del orden con la suma da

$$
0_{\mathbb Q}\leq B,
\qquad
M\leq B,
\qquad
T\leq B.
$$

Mostremos que $B$ acota todos los términos de $q$.

Sea $n\in\mathbb N$. Como el orden natural es total, se cumple $n\leq N$ o $N\leq n$.

Si $N\leq n$, la desigualdad triangular para $d_{\mathbb Q}$ produce

$$
d_{\mathbb Q}(q_n,0_{\mathbb Q})
\leq
d_{\mathbb Q}(q_n,q_N)
+
d_{\mathbb Q}(q_N,0_{\mathbb Q}).
$$

Por la definición de la distancia racional,

$$
d_{\mathbb Q}(q_n,0_{\mathbb Q})=|q_n|
$$

y

$$
d_{\mathbb Q}(q_N,0_{\mathbb Q})=|q_N|.
$$

Por tanto,

$$
|q_n|
<
1_{\mathbb Q}+|q_N|
=
T
\leq B.
$$

En particular,

$$
|q_n|\leq B.
$$

Supongamos ahora $n\leq N$. Si $n=N$, entonces también $N\leq n$ y el caso anterior se aplica. Si $n\neq N$, por la definición del orden estricto asociado,

$$
n<N.
$$

El lema de acotación del segmento inicial da entonces

$$
|q_n|\leq M\leq B.
$$

Hemos probado

$$
\forall n\in\mathbb N,\qquad |q_n|\leq B,
$$

con $B\in\mathbb Q$ y $0_{\mathbb Q}\leq B$. Por Definición 8.6.1 — Sucesión racional acotada, la sucesión $q$ es acotada. ∎

> **Contenido efectivo.** Si $q$ viene con un módulo computable de Cauchy, podemos tomar
> $N=\mu_C(1_{\mathbb Q})$. El segmento inicial $q_0,\ldots,q_{N-1}$ es finito y sus valores
> racionales pueden compararse efectivamente; junto con $1+|q_N|$ obtenemos una cota global
> computable. La acotación abstracta de una sucesión de Cauchy y la computación de una cota a partir
> de datos efectivos son, por tanto, dos niveles distintos.

### Lo que hemos ganado

Toda sucesión racional de Cauchy posee una cota racional global:

$$
\boxed{
q\in\mathcal C_{\mathbb Q}
\Longrightarrow
\exists B\in\mathbb Q\;
\left(
0_{\mathbb Q}\leq B
\land
\forall n\in\mathbb N,\ |q_n|\leq B
\right).
}
$$

La demostración separa dos mecanismos distintos: la condición de Cauchy controla la cola, mientras la inducción controla el segmento inicial.

Esta propiedad será necesaria para analizar la incompletitud secuencial de $\mathbb Q$. En §8.7 construiremos un proceso racional de Cauchy que no converge racionalmente, sin apelar a la construcción de Dedekind.
