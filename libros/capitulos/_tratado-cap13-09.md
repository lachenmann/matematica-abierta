## 13.9. Subsucesiones {#sec-ta-13-9}

Hasta ahora hemos estudiado el comportamiento de una sucesión mirando su cola completa. Una subsucesión cambia la perspectiva: conserva algunos términos y descarta otros, pero **sin alterar el orden en que aparecían**.

Esta última condición es esencial. Si escribimos informalmente

$$
a_{n_0},a_{n_1},a_{n_2},\ldots,
$$

no basta exigir que cada $n_k$ sea un natural. Debemos imponer

$$
n_0<n_1<n_2<\cdots.
$$

Así, una subsucesión no es un subconjunto del recorrido de la sucesión y tampoco es una reordenación de sus términos. Es un nuevo proceso indexado por $\mathbb N$ obtenido mediante una selección de índices que avanza siempre hacia adelante.

La construcción posee además una propiedad menos visible pero fundamental: un selector estrictamente creciente no puede quedarse confinado en una región inicial de $\mathbb N$. Sus valores terminan superando cualquier umbral natural. Precisaremos primero este mecanismo antes de definir formalmente la subsucesión.

### Definición 13.9.1 — Selector de índices de subsucesión

Llamaremos **selector de índices de subsucesión** a una función

$$
\boxed{
\phi:\mathbb N\longrightarrow\mathbb N
}
$$

que sea estrictamente creciente, es decir,

$$
\boxed{
m<n\Longrightarrow \phi(m)<\phi(n)
}
$$

para todos $m,n\in\mathbb N$.

El adjetivo «selector» no significa que estemos escogiendo elementos de una familia mediante Choice. Aquí $\phi$ es una función concreta que forma parte de los datos. La condición de crecimiento estricto expresa simultáneamente dos restricciones:

- no puede reutilizar un índice ya empleado;
- no puede invertir el orden de dos índices seleccionados.

Puede, en cambio, saltar tantos índices como quiera entre dos selecciones consecutivas.

> **Prueba de estrés.** Una función constante $\phi(k)=N$ no es un selector: repite siempre el mismo índice. Una permutación que intercambie dos índices tampoco lo es si destruye el orden estricto. En cambio, $k\mapsto N+k$ sí será un selector y producirá exactamente la cola reindexada introducida en §13.2.

### Proposición 13.9.2 — Crecimiento, inyectividad y cofinalidad de los selectores de índices

Sea $\phi:\mathbb N\to\mathbb N$ un selector de índices. Entonces:

1. $\phi$ es inyectiva;
2. para todo $n\in\mathbb N$,
   $$
   \boxed{n\leq\phi(n)};
   $$
3. para todos $N,k\in\mathbb N$,
   $$
   \boxed{
   N\leq k\Longrightarrow N\leq\phi(k).
   }
   $$

En particular, los valores de $\phi$ son **cofinales en $\mathbb N$**: ningún segmento inicial de los naturales contiene todos los índices seleccionados.

**Demostración.**

Probemos primero la inyectividad. Supongamos

$$
\phi(m)=\phi(n).
$$

La tricotomía decidible Proposición 1.6.7 — Tricotomía decidible de los naturales da exactamente una de las posibilidades

$$
m<n,
\qquad
m=n,
\qquad
n<m.
$$

Si $m<n$, el crecimiento estricto del selector produciría

$$
\phi(m)<\phi(n),
$$

contradiciendo la igualdad. El caso $n<m$ es simétrico. Luego necesariamente

$$
m=n,
$$

y $\phi$ es inyectiva en el sentido de Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad.

Demostraremos ahora

$$
n\leq\phi(n)
$$

por inducción sobre $n$.

Para $n=0$, Proposición 1.4.2 — Cero neutro por la izquierda da

$$
\phi(0)=0+\phi(0),
$$

de modo que la definición aritmética del orden Definición 1.6.1 — Orden aritmético implica

$$
0\leq\phi(0).
$$

Supongamos como hipótesis inductiva

$$
n\leq\phi(n).
$$

Como $n\in S(n)$, Teorema 1.6.12 — Orden estricto y pertenencia da

$$
n<S(n).
$$

El crecimiento estricto de $\phi$ implica entonces

$$
\phi(n)<\phi(S(n)).
$$

Usaremos el siguiente hecho elemental sobre los naturales:

$$
\boxed{
p<q\Longrightarrow S(p)\leq q.}
$$

En efecto, $p<q$ implica $p\leq q$, así que existe $r\in\mathbb N$ con

$$
q=p+r.
$$

Como $p\neq q$, necesariamente $r\neq0$. Por Teorema 1.2.7 — Predecesor de todo natural no nulo, existe $s\in\mathbb N$ tal que

$$
r=S(s).
$$

Por la definición recursiva de la suma y Lema 1.4.3 — Sucesor en el primer argumento,

$$
q=p+S(s)=S(p+s)=S(p)+s.
$$

Por Definición 1.6.1 — Orden aritmético, esto significa

$$
S(p)\leq q.
$$

Aplicando este hecho a

$$
\phi(n)<\phi(S(n)),
$$

obtenemos

$$
S(\phi(n))\leq\phi(S(n)).
$$

Por otra parte, la compatibilidad del orden natural con la suma Proposición 1.6.6 — Compatibilidad con la suma, aplicada a la hipótesis inductiva con el sumando $1=S(0)$, da

$$
n+1\leq\phi(n)+1.
$$

La definición recursiva de la suma identifica ambos miembros con sucesores:

$$
S(n)\leq S(\phi(n)).
$$

Por transitividad de $\leq$ (Proposición 1.6.2 — Reflexividad y transitividad),

$$
S(n)\leq\phi(S(n)).
$$

La inducción queda cerrada.

Finalmente, si $N\leq k$, el resultado recién probado da

$$
k\leq\phi(k).
$$

Otra aplicación de la transitividad produce

$$
N\leq\phi(k).
$$

Esto demuestra $3$. ∎

> **Lectura conceptual.** La desigualdad $n\leq\phi(n)$ es más importante de lo que parece. Nos dice que la extracción puede acelerar el recorrido de los índices, pero nunca retrasarlo indefinidamente. Por eso cualquier propiedad que ya vale después de un umbral $N$ seguirá siendo accesible desde una subsucesión: basta tomar índices de la nueva sucesión a partir de $N$.

### Definición 13.9.3 — Subsucesión de una sucesión real

Sean

$$
a=(a_n)_{n\in\mathbb N},
\qquad
b=(b_k)_{k\in\mathbb N}
$$

sucesiones reales. Diremos que $b$ es una **subsucesión** de $a$ si existe un selector de índices

$$
\phi:\mathbb N\to\mathbb N
$$

tal que

$$
\boxed{
b=a\circ\phi.}
$$

Equivalentemente, para todo $k\in\mathbb N$,

$$
\boxed{
b_k=a_{\phi(k)}.}
$$

La equivalencia entre ambas escrituras es sólo la definición de composición y evaluación; Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales permite recuperar la igualdad de sucesiones a partir de la igualdad término a término.

> **Distinción de tipos.** El selector $\phi$ actúa sobre **índices**,
> $$
> \phi:\mathbb N\to\mathbb N,
> $$
> mientras que $a$ actúa sobre esos índices y devuelve **valores reales**,
> $$
> a:\mathbb N\to\mathbb R.
> $$
> La subsucesión es la composición de ambos niveles.

> **Nota fundacional.** La definición es existencial: para afirmar que una sucesión concreta $b$ es subsucesión de $a$ debe existir un selector que la testimonie. No se escoge simultáneamente un selector para todas las posibles subsucesiones y no interviene Choice.

### Proposición 13.9.4 — Las colas son subsucesiones y las subsucesiones se componen

Sea $a$ una sucesión real.

1. Para todo $N\in\mathbb N$, la cola reindexada $a^{\langle N\rangle}$ es una subsucesión de $a$.
2. Si $b$ es una subsucesión de $a$ y $c$ es una subsucesión de $b$, entonces $c$ es una subsucesión de $a$.

**Demostración.**

Fijemos $N\in\mathbb N$. La regla

$$
\phi_N(k):=N+k
$$

determina una función $\phi_N:\mathbb N\to\mathbb N$: su grafo puede obtenerse por Separación dentro de $\mathbb N\times\mathbb N$, y para cada $k$ el valor $N+k$ está determinado de manera única por la suma natural ya construida.

Si $k<\ell$, Proposición 1.6.6 — Compatibilidad con la suma da

$$
k+N<\ell+N.
$$

Por conmutatividad de la suma,

$$
N+k<N+\ell.
$$

Así $\phi_N$ es un selector de índices. Por Definición 13.2.3 — Cola reindexada de una sucesión,

$$
a^{\langle N\rangle}_k=a_{N+k}=a_{\phi_N(k)},
$$

y Definición 13.9.3 — Subsucesión de una sucesión real muestra que $a^{\langle N\rangle}$ es una subsucesión de $a$.

Probemos ahora $2$. Como $b$ es subsucesión de $a$, existe un selector $\phi$ tal que

$$
b=a\circ\phi.
$$

Como $c$ es subsucesión de $b$, existe un selector $\psi$ tal que

$$
c=b\circ\psi.
$$

Definimos

$$
\theta:=\phi\circ\psi:\mathbb N\to\mathbb N.
$$

Si $k<\ell$, entonces

$$
\psi(k)<\psi(\ell)
$$

y, aplicando el crecimiento estricto de $\phi$,

$$
\theta(k)=\phi(\psi(k))
<
\phi(\psi(\ell))=\theta(\ell).
$$

Por tanto $\theta$ es un selector. La asociatividad de la composición de funciones Proposición 0.6.5 — Asociatividad y leyes de identidad da

$$
\begin{aligned}
c
&=b\circ\psi\\
&=(a\circ\phi)\circ\psi\\
&=a\circ(\phi\circ\psi)\\
&=a\circ\theta.
\end{aligned}
$$

Luego $c$ es una subsucesión de $a$. ∎

La segunda parte muestra que «extraer de una extracción» no produce una noción nueva: dos etapas de selección pueden comprimirse en un único selector estrictamente creciente.

### Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite

Sea $a=(a_n)$ una sucesión real y sea $b=(b_k)$ una subsucesión de $a$. Si

$$
a_n\to\ell,
$$

entonces

$$
\boxed{b_k\to\ell.}
$$

**Demostración.**

Por definición de subsucesión existe un selector $\phi:\mathbb N\to\mathbb N$ tal que

$$
b_k=a_{\phi(k)}.
$$

Sea $\varepsilon>0$. Como $a_n\to\ell$, existe $N\in\mathbb N$ tal que

$$
n\geq N
\Longrightarrow
|a_n-\ell|<\varepsilon.
$$

Tomemos ahora $k\geq N$. Proposición 13.9.2 — Crecimiento, inyectividad y cofinalidad de los selectores de índices da

$$
k\leq\phi(k).
$$

Como además $N\leq k$, Proposición 13.9.2 — Crecimiento, inyectividad y cofinalidad de los selectores de índices (3) produce directamente

$$
N\leq\phi(k).
$$

Por la elección del umbral $N$,

$$
|b_k-\ell|
=
|a_{\phi(k)}-\ell|
<\varepsilon.
$$

Así

$$
\forall\varepsilon>0\;\exists N\;\forall k\geq N,
\qquad
|b_k-\ell|<\varepsilon,
$$

y por Definición 13.3.1 — Convergencia de una sucesión real,

$$
b_k\to\ell.
$$

∎

> **Arquitectura de la prueba.** No necesitamos conocer una fórmula explícita para $\phi(k)$. Toda la demostración se reduce a transportar el umbral $N$ mediante
> $$
> N\leq k\leq\phi(k).
> $$
> Ésta es la razón estructural por la que una subsucesión de una sucesión convergente no puede escapar de su límite.

### Proposición 13.9.6 — Acotación y condición de Cauchy pasan a las subsucesiones

Sea $b$ una subsucesión de una sucesión real $a$.

1. Si $a$ es acotada, entonces $b$ es acotada.
2. Si $a$ es de Cauchy, entonces $b$ es de Cauchy.

**Demostración.**

Sea $\phi$ un selector que testimonia

$$
b_k=a_{\phi(k)}.
$$

Supongamos primero que $a$ es acotada. Por Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto existe $M\geq0$ tal que

$$
|a_n|\leq M
$$

para todo $n\in\mathbb N$. Entonces, para todo $k$,

$$
|b_k|
=
|a_{\phi(k)}|
\leq M.
$$

Otra aplicación de Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto muestra que $b$ es acotada.

Supongamos ahora que $a$ es de Cauchy y sea $\varepsilon>0$. Existe $N\in\mathbb N$ tal que

$$
m,n\geq N
\Longrightarrow
|a_m-a_n|<\varepsilon.
$$

Sean $k,j\geq N$. Por Proposición 13.9.2 — Crecimiento, inyectividad y cofinalidad de los selectores de índices (3),

$$
\phi(k)\geq N,
\qquad
\phi(j)\geq N.
$$

Por tanto

$$
|b_k-b_j|
=
|a_{\phi(k)}-a_{\phi(j)}|
<\varepsilon.
$$

Esto es exactamente la condición de Cauchy para $b$. ∎

> **Observación.** La segunda afirmación se ha probado directamente. Aunque en $\mathbb R$ podríamos deducirla de
> $$
> \text{Cauchy}\Rightarrow\text{convergente}\Rightarrow
> \text{subsucesión convergente}\Rightarrow\text{Cauchy},
> $$
> esa ruta escondería innecesariamente la simplicidad del argumento y haría intervenir completitud donde no hace falta.

### Corolario 13.9.7 — Caracterización de la convergencia mediante subsucesiones

Para una sucesión real $a=(a_n)$ y un real $\ell$, son equivalentes:

1. $a_n\to\ell$;
2. toda subsucesión de $a$ converge a $\ell$.

**Demostración.**

La implicación $1\Rightarrow2$ es Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite.

Para la recíproca, la identidad

$$
\operatorname{id}_{\mathbb N}:\mathbb N\to\mathbb N
$$

es estrictamente creciente, pues

$$
m<n\Longrightarrow
\operatorname{id}_{\mathbb N}(m)=m<n=
\operatorname{id}_{\mathbb N}(n).
$$

Así es un selector de índices. Por la ley de identidad para la composición Proposición 0.6.5 — Asociatividad y leyes de identidad,

$$
a\circ\operatorname{id}_{\mathbb N}=a.
$$

Luego $a$ es una subsucesión de sí misma. Si toda subsucesión de $a$ converge a $\ell$, en particular

$$
a_n\to\ell.
$$

∎

Una consecuencia inmediata, combinando Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite con la unicidad del límite Teorema 13.3.5 — Unicidad del límite real, es la siguiente rigidez: si $a_n\to\ell$, ninguna subsucesión de $a$ puede converger a un real distinto de $\ell$.

Esta observación señala exactamente el concepto siguiente. Una sucesión que no converge puede contener, sin embargo, subsucesiones convergentes; diferentes extracciones pueden incluso revelar comportamientos asintóticos distintos. El próximo paso será convertir esos límites obtenidos por extracción en objetos de estudio propios: los **puntos límite secuenciales** de una sucesión.
