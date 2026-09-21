## 9.2. Sucesiones nulas {#sec-ta-9-2}

### Definición 9.2.1 — Sucesión racional nula y conjunto $\mathcal N_{\mathbb Q}$

Sea

$$
q=(q_n)_{n\in\mathbb N}\in\mathbb Q^{\mathbb N}.
$$

Diremos que $q$ es una sucesión racional nula si converge racionalmente a $0_{\mathbb Q}$:

$$
\boxed{
q_n\to_{\mathbb Q}0_{\mathbb Q}.
}
$$

Definimos el conjunto de las sucesiones racionales nulas por

$$
\boxed{
\mathcal N_{\mathbb Q}
:=
\left\{
q\in\mathbb Q^{\mathbb N}:
q_n\to_{\mathbb Q}0_{\mathbb Q}
\right\}.
}
$$

Este conjunto existe por separación dentro de $\mathbb Q^{\mathbb N}$.

Desplegando Definición 8.3.1 — Convergencia racional, la condición $q\in\mathcal N_{\mathbb Q}$ significa

$$
\forall\varepsilon\in\mathbb Q\;
\Bigl(
0<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\in\mathbb N\;
\bigl(
N\le n
\Longrightarrow
|q_n|<\varepsilon
\bigr)
\Bigr).
$$

No hay aquí una nueva noción de convergencia: «nula» es el caso particular del límite racional igual a cero.

### Proposición 9.2.2 — Toda sucesión nula es de Cauchy

Se tiene

$$
\boxed{
\mathcal N_{\mathbb Q}
\subseteq
\mathcal C_{\mathbb Q}.
}
$$

**Demostración.**

Sea $q\in\mathcal N_{\mathbb Q}$. Por Definición 9.2.1 — Sucesión racional nula y conjunto $\mathcal N_{\mathbb Q}$,

$$
q_n\to_{\mathbb Q}0_{\mathbb Q}.
$$

El teorema Teorema 8.5.1 — Toda sucesión racionalmente convergente es de Cauchy afirma que toda sucesión racionalmente convergente es de Cauchy. Por tanto

$$
q\in\mathcal C_{\mathbb Q}.
$$

Como $q$ era arbitraria,

$$
\mathcal N_{\mathbb Q}\subseteq\mathcal C_{\mathbb Q}.
$$

∎

### Proposición 9.2.3 — Estabilidad aditiva de las sucesiones nulas

Para $u,v\in\mathbb Q^{\mathbb N}$:

1. la sucesión constante $\underline{0_{\mathbb Q}}$ pertenece a $\mathcal N_{\mathbb Q}$;
2. si $u,v\in\mathcal N_{\mathbb Q}$, entonces $u+v\in\mathcal N_{\mathbb Q}$;
3. si $u\in\mathcal N_{\mathbb Q}$, entonces $-u\in\mathcal N_{\mathbb Q}$;
4. si $u,v\in\mathcal N_{\mathbb Q}$, entonces $u-v\in\mathcal N_{\mathbb Q}$.

**Demostración.**

(1) Por Proposición 8.3.4 — Las sucesiones constantes convergen a su valor, toda sucesión constante converge racionalmente a su valor. En particular,

$$
\underline{0_{\mathbb Q}}{}_n
\to_{\mathbb Q}
0_{\mathbb Q}.
$$

Luego

$$
\underline{0_{\mathbb Q}}\in\mathcal N_{\mathbb Q}.
$$

(2) Supongamos

$$
u,v\in\mathcal N_{\mathbb Q}.
$$

Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}
$$

y

$$
\eta:=\frac{\varepsilon}{s}.
$$

Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado, Proposición 3.6.5 — Ley del inverso multiplicativo y las leyes del cuerpo racional, $s>0$, $\eta>0$ y

$$
\eta+\eta=\varepsilon.
$$

Como $u$ es nula, existe $N_u\in\mathbb N$ tal que

$$
N_u\le n
\Longrightarrow
|u_n|<\eta.
$$

Como $v$ es nula, existe $N_v\in\mathbb N$ tal que

$$
N_v\le n
\Longrightarrow
|v_n|<\eta.
$$

El orden natural es total (Teorema 1.6.5 — Orden total). Por tanto

$$
N_u\le N_v
\qquad\text{o}\qquad
N_v\le N_u.
$$

En el primer caso tomamos $N:=N_v$; en el segundo, $N:=N_u$. Así

$$
N_u\le N
\qquad\text{y}\qquad
N_v\le N.
$$

Sea $n\in\mathbb N$ con $N\le n$. Por transitividad,

$$
|u_n|<\eta,
\qquad
|v_n|<\eta.
$$

La desigualdad triangular del valor absoluto (Teorema 4.2.3 — Desigualdad triangular) da

$$
|u_n+v_n|
\le
|u_n|+|v_n|.
$$

La compatibilidad estricta del orden con la suma produce

$$
|u_n|+|v_n|
<
\eta+\eta
=
\varepsilon.
$$

Por tanto

$$
|(u+v)_n|<\varepsilon.
$$

Hemos demostrado

$$
u+v\in\mathcal N_{\mathbb Q}.
$$

(3) Supongamos $u\in\mathcal N_{\mathbb Q}$. Sea $\varepsilon>0$. Existe $N$ tal que para $n\ge N$,

$$
|u_n|<\varepsilon.
$$

Por la invariancia del valor absoluto frente al opuesto (Proposición 4.2.2 — Propiedades elementales del valor absoluto),

$$
|(-u)_n|
=
|-u_n|
=
|u_n|
<
\varepsilon.
$$

Así

$$
-u\in\mathcal N_{\mathbb Q}.
$$

(4) Si $u,v\in\mathcal N_{\mathbb Q}$, entonces por $3$,

$$
-v\in\mathcal N_{\mathbb Q},
$$

y por $2$,

$$
u+(-v)\in\mathcal N_{\mathbb Q}.
$$

Como la sustracción puntual fue definida por

$$
u-v=u+(-v),
$$

concluimos

$$
u-v\in\mathcal N_{\mathbb Q}.
$$

∎

### Lema 9.2.4 — Producto de una sucesión acotada por una sucesión nula

Sean

$$
u=(u_n)_{n\in\mathbb N},
\qquad
v=(v_n)_{n\in\mathbb N}
$$

sucesiones racionales. Si $u$ es acotada y $v$ es nula, entonces la sucesión producto $uv$ es nula.

**Demostración.**

Como $u$ es acotada, existe $M\in\mathbb Q$ tal que

$$
0\le M
$$

y

$$
|u_n|\le M
\qquad
\text{para todo }n\in\mathbb N.
$$

Definamos

$$
H:=M+1_{\mathbb Q}.
$$

Como $0\le M$ y $0<1_{\mathbb Q}$,

$$
0<H
$$

y además

$$
M<H.
$$

Sea ahora $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Definamos

$$
\delta:=\frac{\varepsilon}{H}.
$$

Como $H>0$, su inverso es positivo y por tanto

$$
0<\delta.
$$

Además,

$$
H\delta
=
H\frac{\varepsilon}{H}
=
\varepsilon.
$$

Como $v$ es nula, existe $N\in\mathbb N$ tal que, para todo $n\ge N$,

$$
|v_n|<\delta.
$$

Sea $n\ge N$. Por multiplicatividad del valor absoluto,

$$
|(uv)_n|
=
|u_nv_n|
=
|u_n|\,|v_n|.
$$

Como

$$
|u_n|\le M\le H
$$

y $|v_n|\ge0$, la compatibilidad del orden con el producto da

$$
|u_n|\,|v_n|
\le
H|v_n|.
$$

De

$$
|v_n|<\delta
$$

y $H>0$, la compatibilidad estricta del orden con la multiplicación por un factor positivo produce

$$
H|v_n|
<
H\delta
=
\varepsilon.
$$

Por transitividad,

$$
|(uv)_n|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitraria,

$$
uv\in\mathcal N_{\mathbb Q}.
$$

∎

> **Nota fundacional.** De la acotación se utiliza un único testigo $M$ para la sucesión fija $u$, y de la nulidad un único índice para la precisión $\delta$ construida. No interviene Choice.

### Corolario 9.2.5 — Producto de una sucesión de Cauchy por una sucesión nula

Si

$$
u\in\mathcal C_{\mathbb Q}
$$

y

$$
v\in\mathcal N_{\mathbb Q},
$$

entonces

$$
\boxed{
uv\in\mathcal N_{\mathbb Q}.
}
$$

**Demostración.**

Por Teorema 8.6.3 — Toda sucesión racional de Cauchy es acotada, toda sucesión racional de Cauchy es acotada. Por tanto $u$ es acotada.

Aplicando Lema 9.2.4 — Producto de una sucesión acotada por una sucesión nula a $u$ y $v$ obtenemos

$$
uv\in\mathcal N_{\mathbb Q}.
$$

∎

### Lo que hemos ganado

Disponemos ahora de dos capas de sucesiones racionales:

$$
\mathcal N_{\mathbb Q}
\subseteq
\mathcal C_{\mathbb Q}
\subseteq
\mathbb Q^{\mathbb N}.
$$

Las sucesiones nulas son precisamente las perturbaciones que desaparecen asintóticamente. Son estables bajo suma, opuesto y diferencia, y permanecen nulas al multiplicarlas por cualquier sucesión de Cauchy:

$$
u\in\mathcal C_{\mathbb Q},
\quad
v\in\mathcal N_{\mathbb Q}
\Longrightarrow
uv\in\mathcal N_{\mathbb Q}.
$$

Con esta infraestructura ya podemos definir rigurosamente cuándo dos sucesiones de Cauchy representan la misma posición asintótica:

$$
a\sim_C b
\quad\Longleftrightarrow\quad
a-b\in\mathcal N_{\mathbb Q}.
$$

Ése será el contenido de §9.3. Todavía no formaremos el cociente hasta haber demostrado que $\sim_C$ es una relación de equivalencia.
