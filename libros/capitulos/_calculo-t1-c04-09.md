## Cuando no hay límite real: límites infinitos y divergencia {#sec-t1-c04-09}

Hasta ahora, cuando una sucesión convergía, buscábamos un número real $L$ alrededor del cual terminara concentrándose toda la cola. Pero hay sucesiones cuyo comportamiento final es ordenado y describible aunque no se acerquen a ningún número real.

El ejemplo más simple es

$$
a_n=n.
$$

Los términos

$$
0,1,2,3,\dots
$$

no se aproximan a un real fijo. Al contrario: sobrepasan cualquier barrera real que fijemos, siempre que avancemos lo suficiente.

La frase importante no es

> «los términos se hacen muy grandes»,

sino una afirmación cuantificada:

> **dada cualquier cota real que queramos superar, toda la cola termina quedando por encima de ella.**

Este patrón es análogo a la definición $\varepsilon$–$N$, pero cambia el tipo de desafío. Allí alguien fijaba una tolerancia alrededor de un candidato $L$; aquí alguien fija una barrera real $M$ que debemos superar de manera permanente.

### Superar cualquier barrera

::: {#def-t1-0031}
**Límites infinitos de una sucesión.** Sea $(a_n)_{n\ge n_0}$ una sucesión real.

Diremos que

$$
a_n\to+\infty
$$

si para todo número real $M$ existe un índice $N\ge n_0$ tal que

$$
a_n>M
$$

para todo $n\ge N$. En símbolos,

$$
\forall M\in\mathbb R\;\exists N\ge n_0\;\forall n\ge N:
\quad a_n>M.
$$

Diremos que

$$
a_n\to-\infty
$$

si para todo número real $M$ existe un índice $N\ge n_0$ tal que

$$
a_n<M
$$

para todo $n\ge N$. En símbolos,

$$
\forall M\in\mathbb R\;\exists N\ge n_0\;\forall n\ge N:
\quad a_n<M.
$$
:::

La estructura lógica debe leerse con el mismo cuidado que en la convergencia ordinaria:

$$
\boxed{
\text{barrera arbitraria}
\longrightarrow
\text{umbral adecuado}
\longrightarrow
\text{toda la cola al otro lado de la barrera}.
}
$$

Para $+\infty$, la barrera se supera por arriba. Para $-\infty$, se supera por abajo.

### El símbolo $\infty$ no nombra un número real

La notación

$$
\lim_{n\to\infty}a_n=+\infty
$$

es útil, pero debe interpretarse mediante @def-t1-0031. No significa que exista un número real llamado $+\infty$ al cual se acerquen los términos.

En particular,

$$
+\infty\notin\mathbb R,
\qquad
-\infty\notin\mathbb R.
$$

Por eso, si $a_n\to+\infty$ o $a_n\to-\infty$, la sucesión **no converge en el sentido real ordinario** de @def-t1-0028.

Hay también una razón estructural inmediata. Si $a_n\to+\infty$, entonces la sucesión no está acotada superiormente: dada cualquier supuesta cota $B$, la definición con $M=B$ produce términos tardíos mayores que $B$. Análogamente, si $a_n\to-\infty$, no está acotada inferiormente.

Pero @prp-t1-0020 demostró que toda sucesión convergente a un número real es acotada. Por tanto,

$$
\boxed{
 a_n\to\pm\infty
 \Longrightarrow
 (a_n)\text{ diverge como sucesión real.}
}
$$

La palabra **diverge**, sin embargo, es más amplia. Una sucesión puede divergir sin escapar ordenadamente hacia ninguno de los dos infinitos.

### El ejemplo básico: $n\to+\infty$

Probemos la afirmación directamente desde la propiedad arquimediana de $\mathbb R$.

Sea $M\in\mathbb R$ arbitrario. Por la propiedad arquimediana existe un número natural $N$ tal que

$$
N>M.
$$

Entonces, para todo $n\ge N$,

$$
n\ge N>M.
$$

Por consiguiente,

$$
\forall M\in\mathbb R\;\exists N\in\mathbb N\;\forall n\ge N:
\quad n>M,
$$

y por @def-t1-0031,

$$
\boxed{n\to+\infty.}
$$

El argumento muestra con precisión qué papel desempeña la arquimedianidad: garantiza que ninguna barrera real puede quedar por encima de todos los naturales.

De la misma manera,

$$
-n\to-\infty,
$$

porque dada una barrera real $M$, basta elegir $N>-M$; entonces, si $n\ge N$,

$$
-n\le -N<M.
$$

### No acotada no significa tender a infinito

Una sucesión que tiende a $+\infty$ es necesariamente no acotada superiormente. Pero la recíproca es falsa. Ser no acotada solo afirma que podemos encontrar términos arbitrariamente grandes; no dice que **todos los términos suficientemente tardíos** sean grandes.

La diferencia vuelve a estar en los cuantificadores.

No estar acotada superiormente significa

$$
\forall M\in\mathbb R\;\exists n\ge n_0:
\quad a_n>M.
$$

Tender a $+\infty$ exige mucho más:

$$
\forall M\in\mathbb R\;\exists N\ge n_0\;\forall n\ge N:
\quad a_n>M.
$$

En la primera afirmación encontramos **algún término** que supera la barrera. En la segunda encontramos **una cola completa** que queda por encima de ella.

::: {#exm-t1-0039}
**No acotación frente a límite infinito.** Consideremos

$$
a_n=(-1)^n n.
$$

La sucesión toma la forma

$$
0,-1,2,-3,4,-5,\dots
$$

Es no acotada superiormente y no acotada inferiormente. Sin embargo,

$$
a_n\not\to+\infty
$$

y

$$
a_n\not\to-\infty.
$$
:::

**No está acotada superiormente.** Sea $B\in\mathbb R$. Por arquimedianidad podemos elegir un número natural $m$ tan grande que

$$
2m>B.
$$

Para el índice par $n=2m$,

$$
a_{2m}=2m>B.
$$

Así, ninguna cota superior real puede controlar todos los términos.

**No está acotada inferiormente.** Dado $B\in\mathbb R$, elijamos $m$ con

$$
2m+1>-B.
$$

Entonces

$$
a_{2m+1}=-(2m+1)<B.
$$

Por tanto, tampoco existe una cota inferior real.

**No tiende a $+\infty$.** Fijemos la barrera

$$
M=0.
$$

Para que $a_n\to+\infty$, debería existir un índice $N$ después del cual todos los términos fueran positivos. Pero, dado cualquier $N$, podemos elegir un índice impar $n\ge N$. Para ese índice,

$$
a_n=-n<0.
$$

Así, ninguna cola queda enteramente por encima de $0$.

**No tiende a $-\infty$.** De nuevo usemos la barrera $M=0$. Dado cualquier $N$, podemos elegir un índice par $n\ge N$. Entonces

$$
a_n=n\ge0,
$$

de modo que ninguna cola queda enteramente por debajo de $0$.

La sucesión escapa a cotas arbitrariamente grandes en ambos sentidos, pero sigue cruzando una y otra vez de un lado al otro. No existe una dirección unilateral de escape.

El ejemplo separa tres ideas:

$$
\boxed{
\text{no acotada}
\not\Longrightarrow
+\infty,
\qquad
\text{no acotada}
\not\Longrightarrow
-\infty.
}
$$

### El recíproco convierte crecimiento infinito en pequeñez

Hay una conexión muy útil entre los límites infinitos y los límites reales ya estudiados. Para números positivos, afirmar que $a_n$ termina superando cualquier barrera equivale a afirmar que su recíproco termina siendo tan pequeño como queramos.

::: {#prp-t1-0024}
**Recíprocos y crecimiento hacia $+\infty$.** Sea $(a_n)_{n\ge n_0}$ una sucesión real que es eventualmente positiva. Entonces

$$
a_n\to+\infty
\quad\Longleftrightarrow\quad
\frac1{a_n}\to0.
$$
:::

**Demostración.** Supongamos primero que

$$
a_n\to+\infty.
$$

Sea $\varepsilon>0$. Como $1/\varepsilon$ es un número real, la definición de límite infinito proporciona un índice $N_1$ tal que

$$
a_n>\frac1\varepsilon
$$

para todo $n\ge N_1$.

Además, por positividad eventual existe $N_0$ tal que

$$
a_n>0
$$

para todo $n\ge N_0$.

Si

$$
N=\max\{N_0,N_1\},
$$

entonces, para $n\ge N$,

$$
0<\frac1{a_n}<\varepsilon.
$$

Por tanto,

$$
\left|\frac1{a_n}-0\right|<\varepsilon,
$$

y concluimos

$$
\frac1{a_n}\to0.
$$

Recíprocamente, supongamos que

$$
\frac1{a_n}\to0
$$

y que $a_n>0$ eventualmente. Queremos demostrar que toda barrera real termina siendo superada.

Sea $M\in\mathbb R$.

Si $M\le0$, la positividad eventual basta: existe $N_0$ tal que, para $n\ge N_0$,

$$
a_n>0\ge M.
$$

Si $M>0$, tomemos

$$
\varepsilon=\frac1M.
$$

Como $1/a_n\to0$, existe $N_1$ tal que, para todo $n\ge N_1$,

$$
\left|\frac1{a_n}\right|<\frac1M.
$$

Tomando además una cola donde $a_n>0$, obtenemos

$$
0<\frac1{a_n}<\frac1M.
$$

Como ambos lados son positivos, el orden de los recíprocos se invierte y resulta

$$
a_n>M.
$$

En ambos casos existe un umbral después del cual $a_n>M$. Como $M$ era arbitrario,

$$
a_n\to+\infty.
$$

$\blacksquare$

La hipótesis de positividad eventual no es decorativa. Sin ella, la condición

$$
\frac1{a_n}\to0
$$

solo informa que $|a_n|$ se hace grande en magnitud; no selecciona hacia qué lado de la recta escapan los términos. El ejemplo $a_n=(-1)^n n$ lo muestra de inmediato: su recíproco, a partir de $n=1$, satisface

$$
\frac1{a_n}=\frac{(-1)^n}{n}\to0,
$$

pero $(a_n)$ no tiende ni a $+\infty$ ni a $-\infty$.

Por simetría de signo, una versión análoga relaciona $a_n\to-\infty$ con $1/a_n\to0$ cuando la sucesión es eventualmente negativa. No necesitamos introducir un nuevo principio: basta aplicar el resultado anterior a $(-a_n)$.

### Divergir tiene varias formas

A esta altura conviene ordenar el vocabulario.

Una sucesión puede:

- converger a un número real $L$;
- tender a $+\infty$;
- tender a $-\infty$;
- divergir sin tener ninguno de esos comportamientos, como $(-1)^n$ o $(-1)^n n$.

Así, decir simplemente

> «la sucesión diverge»

no especifica **cómo** falla la convergencia real.

En particular,

$$
\boxed{
\text{divergente}
\not\Longrightarrow
\text{límite infinito}.
}
$$

Esta distinción será importante cuando más adelante clasifiquemos comportamientos de funciones y series.

### No haremos álgebra formal con el símbolo $\infty$

Las leyes de @prp-t1-0021 fueron demostradas para límites **reales**. No hemos demostrado todavía un cálculo general para expresiones que involucren $+\infty$ o $-\infty$.

Y no podemos obtenerlo tratando esos símbolos como números.

Por ejemplo, las tres parejas

$$
a_n=n,
\qquad
b_n=-n,
$$

$$
c_n=2n,
\qquad
b_n=-n,
$$

y

$$
a_n=n,
\qquad
d_n=-2n
$$

tienen siempre un término que tiende a $+\infty$ y otro que tiende a $-\infty$. Sin embargo,

$$
a_n+b_n=0,
$$

$$
c_n+b_n=n\to+\infty,
$$

y

$$
a_n+d_n=-n\to-\infty.
$$

Por tanto, la escritura informal

$$
+\infty+(-\infty)
$$

no determina por sí sola un resultado.

Más adelante aprenderemos a reconocer y resolver distintas **formas indeterminadas** bajo hipótesis adicionales. Por ahora basta fijar una disciplina:

$$
\boxed{
\text{los símbolos }\pm\infty\text{ se interpretan mediante definiciones cuantificadas, no mediante aritmética ficticia.}
}
$$

### Qué hemos ganado

Ya podemos distinguir cuatro niveles de comportamiento final:

$$
\boxed{
\begin{array}{c}
\text{convergencia a un real}\\[2pt]
\text{escape a }+\infty\text{ o }-\infty\\[2pt]
\text{no acotación sin dirección unilateral}\\[2pt]
\text{otras formas de divergencia}
\end{array}
}
$$

La herramienta común sigue siendo la misma: controlar **toda una cola** mediante cuantificadores.

Para un límite real, dada una tolerancia $\varepsilon>0$, toda la cola debe entrar en un intervalo alrededor de $L$.

Para $+\infty$, dada una barrera $M$, toda la cola debe quedar por encima de ella.

Para $-\infty$, dada una barrera $M$, toda la cola debe quedar por debajo.

Con esto hemos completado el repertorio conceptual principal del capítulo. En §4.10 dejaremos de introducir teoría nueva y recorreremos un laboratorio de diagnóstico: reconocer qué herramienta conviene usar, reconstruir pruebas y detectar errores lógicos antes de afrontar el banco final de ejercicios.
