## 13.4. Acotación de sucesiones reales {#sec-ta-13-4}

La convergencia controla los términos de una sucesión cuando el índice es suficientemente grande. La **acotación**, en cambio, es una propiedad global: exige que todos los términos permanezcan dentro de una misma región limitada de la recta real.

Esta diferencia obliga a separar dos tareas. Primero debemos formular la acotación en términos de la teoría de cotas ya construida para subconjuntos ordenados. Después mostraremos que una cota válida sólo eventualmente puede extenderse a toda la sucesión porque antes del umbral quedan únicamente finitos términos.

### Definición 13.4.1 — Sucesiones acotadas superiormente, inferiormente y acotadas

Sea

$$
a=(a_n)_{n\in\mathbb N}\in\mathbb R^{\mathbb N}.
$$

Su recorrido es el subconjunto

$$
a[\mathbb N]\subseteq\mathbb R.
$$

Decimos que $a$ está **acotada superiormente** si $a[\mathbb N]$ está acotado superiormente en $\mathbb R$. Equivalentemente,

$$
\boxed{
\exists U\in\mathbb R\;\forall n\in\mathbb N,
\qquad
a_n\le U.
}
$$

En ese caso, $U$ es una **cota superior de la sucesión**.

Decimos que $a$ está **acotada inferiormente** si $a[\mathbb N]$ está acotado inferiormente. Equivalentemente,

$$
\boxed{
\exists L\in\mathbb R\;\forall n\in\mathbb N,
\qquad
L\le a_n.
}
$$

En ese caso, $L$ es una **cota inferior de la sucesión**.

Finalmente, $a$ es **acotada** si está acotada tanto superior como inferiormente.

> **Lectura de la definición.** La acotación no es una propiedad eventual. Las desigualdades deben controlar también los términos iniciales. Una sucesión puede poseer términos iniciales muy grandes y seguir siendo convergente; esos términos no afectan el límite, pero sí influyen en el tamaño de una cota global.

> **Nota de tipos.** No identificamos la sucesión $a$ con su recorrido $a[\mathbb N]$. La definición transporta a la sucesión una propiedad de ese subconjunto, pero ambos objetos siguen siendo distintos: $a$ es una función y $a[\mathbb N]$ es un conjunto de números reales.

### Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto

Sea $a=(a_n)$ una sucesión real. Son equivalentes:

1. $a$ es acotada;
2. existe $M\in\mathbb R$ tal que
   $$
   0\le M
   $$
   y
   $$
   \boxed{
   \forall n\in\mathbb N,
   \qquad
   |a_n|\le M.
   }
   $$

**Demostración.**

Supongamos primero que $a$ es acotada. Existen entonces $L,U\in\mathbb R$ tales que, para todo $n\in\mathbb N$,

$$
L\le a_n\le U.
$$

Definamos

$$
M:=|L|+|U|.
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto (1), ambos sumandos son no negativos, luego

$$
0\le M.
$$

Además, Proposición 4.2.2 — Propiedades elementales del valor absoluto (4) da

$$
-|L|\le L
\qquad\text{y}\qquad
U\le |U|.
$$

Como $|L|\le M$ y $|U|\le M$, obtenemos

$$
-M\le -|L|\le L\le a_n\le U\le |U|\le M.
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto (6),

$$
|a_n|\le M.
$$

Esto vale para todo $n\in\mathbb N$.

Recíprocamente, supongamos que existe $M\ge0$ con

$$
|a_n|\le M
$$

para todo $n$. Aplicando nuevamente Proposición 4.2.2 — Propiedades elementales del valor absoluto (6),

$$
-M\le a_n\le M
$$

para todo índice. Por tanto $M$ es una cota superior, $-M$ es una cota inferior y $a$ es acotada. ∎

Esta formulación será especialmente útil en estimaciones: en lugar de transportar simultáneamente una cota superior y otra inferior, podremos trabajar con un único número no negativo que controle $|a_n|$.

### Proposición 13.4.3 — Todo prefijo finito de una sucesión real está acotado

Sea $a=(a_n)$ una sucesión real. Para todo $N\in\mathbb N$ existe $B\in\mathbb R$ tal que

$$
0\le B
$$

y

$$
\boxed{
\forall n\in\mathbb N,
\qquad
n<N\Longrightarrow |a_n|\le B.
}
$$

**Demostración.**

Procedemos por inducción sobre $N$.

Para $N=0$, tomamos $B=0$. No existe $n\in\mathbb N$ con $n<0$: por Teorema 1.6.12 — Orden estricto y pertenencia, tal desigualdad equivaldría a $n\in0=\varnothing$. La afirmación queda entonces satisfecha vacíamente.

Supongamos ahora que para cierto $N\in\mathbb N$ existe $B\ge0$ tal que

$$
n<N\Longrightarrow |a_n|\le B.
$$

Definimos

$$
B':=B+|a_N|.
$$

Como $B\ge0$ y $|a_N|\ge0$, la compatibilidad del orden con la suma da

$$
0\le B'.
$$

Sea $n<S(N)$. Por Teorema 1.6.12 — Orden estricto y pertenencia,

$$
n\in S(N)=N\cup\{N\}.
$$

Hay dos casos.

Si $n\in N$, entonces nuevamente por Teorema 1.6.12 — Orden estricto y pertenencia se tiene $n<N$, y la hipótesis inductiva produce

$$
|a_n|\le B\le B+|a_N|=B'.
$$

Si $n=N$, entonces

$$
|a_n|=|a_N|\le B+|a_N|=B',
$$

pues $B\ge0$.

Así el mismo enunciado vale para $S(N)$. El principio de inducción Teorema 1.1.10 — Principio de inducción concluye la proposición para todo $N\in\mathbb N$. ∎

### Proposición 13.4.4 — Una cota eventual se extiende a una cota global

Sea $a=(a_n)$ una sucesión real. Supongamos que existe $B_0\in\mathbb R$ con

$$
0\le B_0
$$

tal que la propiedad

$$
|a_n|\le B_0
$$

vale eventualmente. Entonces $a$ es acotada.

**Demostración.**

Por eventualidad existe $N\in\mathbb N$ tal que

$$
N\le n
\Longrightarrow
|a_n|\le B_0.
$$

Por Proposición 13.4.3 — Todo prefijo finito de una sucesión real está acotado, existe $B_1\ge0$ tal que

$$
n<N
\Longrightarrow
|a_n|\le B_1.
$$

Definimos

$$
M:=B_0+B_1.
$$

Como $B_0,B_1\ge0$, se tiene $M\ge0$, además de

$$
B_0\le M
\qquad\text{y}\qquad
B_1\le M.
$$

Sea ahora $n\in\mathbb N$. Por la tricotomía decidible de los naturales Proposición 1.6.7 — Tricotomía decidible de los naturales, exactamente una de las relaciones

$$
n<N,
\qquad
n=N,
\qquad
N<n
$$

se cumple.

En el primer caso,

$$
|a_n|\le B_1\le M.
$$

Si $n=N$, la reflexividad del orden natural da $N\le n$, y si $N<n$, la definición del orden estricto implica también $N\le n$. En ambos casos la cota eventual produce

$$
|a_n|\le B_0\le M.
$$

Así

$$
\forall n\in\mathbb N,
\qquad
|a_n|\le M.
$$

La caracterización Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto concluye que $a$ es acotada. ∎

La proposición anterior formaliza una operación que en análisis se realiza constantemente: **absorber un prefijo finito dentro de una cota global**.

### Teorema 13.4.5 — Toda sucesión real convergente es acotada

Sea $a=(a_n)$ una sucesión real y sea $\ell\in\mathbb R$. Si

$$
a_n\to\ell,
$$

entonces $a$ es acotada.

**Demostración.**

En todo cuerpo ordenado,

$$
0<1
$$

por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (3). Aplicamos la definición de convergencia con

$$
\varepsilon=1.
$$

La propiedad

$$
|a_n-\ell|<1
$$

vale eventualmente.

Para todo índice en el que se cumpla esa desigualdad, la desigualdad triangular da

$$
\begin{aligned}
|a_n|
&=|(a_n-\ell)+\ell|\\
&\le |a_n-\ell|+|\ell|\\
&<1+|\ell|\\
&=|\ell|+1.
\end{aligned}
$$

En particular, para todo índice en el que vale la propiedad eventual anterior se cumple

$$
|a_n|\le |\ell|+1.
$$

Por la regla de estabilidad de la eventualidad bajo implicación Proposición 13.2.5 — Reglas elementales de eventualidad (5), la propiedad

$$
|a_n|\le |\ell|+1
$$

vale eventualmente. Además,

$$
0\le |\ell|+1
$$

por la no negatividad del valor absoluto y la positividad de $1$.

Proposición 13.4.4 — Una cota eventual se extiende a una cota global transforma esta cota eventual en una cota global. Por tanto $a$ es acotada. ∎

> **Arquitectura de la prueba.** La convergencia controla primero una **cola** de la sucesión. La proposición de prefijos controla después los términos anteriores al umbral. El teorema surge al ensamblar esas dos piezas:
>
> $$
> \boxed{
> \text{cola controlada}
> +
> \text{prefijo finito}
> \Longrightarrow
> \text{sucesión globalmente acotada}.
> }
> $$

> **Nota fundacional.** No interviene la completitud de $\mathbb R$, ni Choice, ni una decisión clásica sobre la igualdad real. La prueba usa únicamente la estructura de cuerpo ordenado, el valor absoluto, la inducción natural y la definición de convergencia. En particular, el mismo argumento vale en cualquier cuerpo ordenado una vez formulada allí la correspondiente noción de convergencia secuencial.

La acotación elimina ahora el principal obstáculo para estudiar productos de sucesiones convergentes. Si $a_n\to a$, ya podemos disponer de una cota uniforme para $|a_n|$ y utilizarla en estimaciones del término

$$
|a_nb_n-ab|.
$$

La siguiente sección desarrollará la **álgebra de los límites**, comenzando por suma y opuesto y utilizando la acotación precisamente cuando el producto la requiera.
