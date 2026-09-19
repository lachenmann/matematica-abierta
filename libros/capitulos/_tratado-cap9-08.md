## 9.8. Orden {#sec-ta-9-8}

La estructura de cuerpo no determina por sí sola qué elementos deben considerarse positivos. En la construcción de Cauchy, además, una comparación puntual entre representantes no puede adoptarse sin más como comparación entre clases: una perturbación nula puede cambiar infinitas veces el signo de diferencias muy pequeñas.

Por ejemplo, aunque dos sucesiones representen la misma clase, no hay razón para que una desigualdad como $a_n\le b_n$ se conserve término a término después de sustituir $a$ o $b$ por representantes equivalentes. La comparación correcta debe tolerar errores racionales arbitrariamente pequeños.

La idea será primero comparar **representantes** mediante una relación asintótica estable bajo perturbaciones nulas y sólo después hacerla descender a $\mathbb R_C$.

### Definición 9.8.1 — Comparación asintótica de representantes

Sean

$$
a=(a_n)_{n\in\mathbb N},
\qquad
b=(b_n)_{n\in\mathbb N}
$$

elementos de $\mathcal C_{\mathbb Q}$. Definimos

$$
\boxed{
a\preccurlyeq_C b
}
$$

si y sólo si

$$
\boxed{
\forall\varepsilon\in\mathbb Q\;
\Bigl(
0_{\mathbb Q}<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\in\mathbb N\;
\bigl(
N\le n
\Longrightarrow
a_n<b_n+\varepsilon
\bigr)
\Bigr).
}
$$

Conjuntistamente,

$$
\preccurlyeq_C
:=
\left\{
\langle a,b\rangle
\in
\mathcal C_{\mathbb Q}\times\mathcal C_{\mathbb Q}
:
a\preccurlyeq_C b
\right\}.
$$

El producto cartesiano existe y el subconjunto indicado existe por separación. Por tanto $\preccurlyeq_C$ es una relación bien formada sobre $\mathcal C_{\mathbb Q}$.

La presencia de **toda** tolerancia racional positiva es esencial. La condición no dice que $a_n\le b_n$ para todo índice suficientemente grande; dice que, por pequeña que sea la tolerancia positiva prescrita, la primera sucesión queda finalmente por debajo de la segunda salvo ese error.

> **Nota fundacional.** El preorder asintótico es una relación extensional bien definida, pero su
> verdad no es decidible en general a partir de representantes arbitrarios.

### Proposición 9.8.2 — Propiedades e invariancia de la comparación asintótica

Para $a,b,c,a',b'\in\mathcal C_{\mathbb Q}$:

1. $a\preccurlyeq_C a$;
2. si $a\preccurlyeq_C b$ y $b\preccurlyeq_C c$, entonces $a\preccurlyeq_C c$;
3. si $a\sim_C a'$ y $b\sim_C b'$, entonces
   $$
   a\preccurlyeq_C b
   \iff
   a'\preccurlyeq_C b';
   $$
4. si $a\preccurlyeq_C b$ y $b\preccurlyeq_C a$, entonces $a\sim_C b$.

En particular, la comparación asintótica depende sólo de las clases de Cauchy.

**Demostración.**

**(1) Reflexividad.** Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Para todo $n\in\mathbb N$,

$$
a_n<a_n+\varepsilon,
$$

por invariancia estricta del orden bajo traslación. Podemos tomar $N=0$. Luego

$$
a\preccurlyeq_C a.
$$

**(2) Transitividad.** Supongamos

$$
a\preccurlyeq_C b,
\qquad
b\preccurlyeq_C c.
$$

Sea $\varepsilon>0$. Escribamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q},
\qquad
\eta:=\frac{\varepsilon}{s}.
$$

Como $\mathbb Q$ es un cuerpo ordenado, $s>0$, $\eta>0$ y

$$
\eta+\eta=\varepsilon.
$$

De $a\preccurlyeq_C b$ existe $N_1$ tal que, para $n\ge N_1$,

$$
a_n<b_n+\eta.
$$

De $b\preccurlyeq_C c$ existe $N_2$ tal que, para $n\ge N_2$,

$$
b_n<c_n+\eta.
$$

Por totalidad del orden natural, uno de $N_1,N_2$ es mayor o igual que el otro; tomamos ese índice como $N$. Entonces, para todo $n\ge N$,

$$
a_n
<
b_n+\eta
<
(c_n+\eta)+\eta
=
c_n+\varepsilon.
$$

Por tanto $a\preccurlyeq_C c$.

**(3) Invariancia bajo equivalencia.** Supongamos

$$
a\sim_C a',
\qquad
b\sim_C b',
\qquad
a\preccurlyeq_C b.
$$

Sea $\varepsilon>0$. Pongamos otra vez

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}
$$

y ahora

$$
\eta:=\frac{\varepsilon}{ss}.
$$

Como $s>0$, también $ss>0$ y $\eta>0$. Las leyes del cuerpo dan

$$
\eta+\eta+\eta+\eta=\varepsilon.
$$

De $a\sim_C a'$ se sigue que $a-a'$ es nula. Para la tolerancia $\eta$ existe $N_a$ tal que, si $n\ge N_a$,

$$
|a_n-a'_n|<\eta.
$$

Por la caracterización epsilon-local Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional,

$$
a'_n<a_n+\eta.
$$

Análogamente, de $b\sim_C b'$ obtenemos un $N_b$ tal que, para $n\ge N_b$,

$$
b_n<b'_n+\eta.
$$

Finalmente, de $a\preccurlyeq_C b$ obtenemos $N_0$ tal que, para $n\ge N_0$,

$$
a_n<b_n+\eta.
$$

Comparamos primero $N_a$ y $N_b$ y conservamos el mayor; después comparamos ese índice con $N_0$. Así obtenemos, mediante dos aplicaciones finitas de la totalidad de $\mathbb N$, un índice $N$ que domina a los tres.

Para $n\ge N$,

$$
\begin{aligned}
a'_n
&<a_n+\eta\\
&<b_n+\eta+\eta\\
&<b'_n+\eta+\eta+\eta\\
&<b'_n+\eta+\eta+\eta+\eta\\
&=b'_n+\varepsilon.
\end{aligned}
$$

En el penúltimo paso usamos $\eta>0$. Por tanto

$$
a'\preccurlyeq_C b'.
$$

La implicación recíproca se obtiene intercambiando $(a,b)$ con $(a',b')$, pues $\sim_C$ es simétrica.

**(4) Antisimetría módulo $\sim_C$.** Supongamos

$$
a\preccurlyeq_C b,
\qquad
b\preccurlyeq_C a.
$$

Sea $\varepsilon>0$. Existen $N_1,N_2$ tales que

$$
n\ge N_1
\Longrightarrow
a_n<b_n+\varepsilon
$$

y

$$
n\ge N_2
\Longrightarrow
b_n<a_n+\varepsilon.
$$

Tomando, por totalidad, un índice $N$ que domine a ambos, obtenemos para $n\ge N$

$$
b_n-\varepsilon<a_n<b_n+\varepsilon.
$$

Por Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional,

$$
|a_n-b_n|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitraria,

$$
a-b\in\mathcal N_{\mathbb Q},
$$

y por Definición 9.3.1 — Equivalencia de Cauchy,

$$
a\sim_C b.
$$

∎

### Lema 9.8.3 — Dicotomía eventual de signo

Sea

$$
a\in\mathcal C_{\mathbb Q}\setminus\mathcal N_{\mathbb Q}.
$$

Entonces existen $\delta\in\mathbb Q$, $\delta>0$, y $N\in\mathbb N$ tales que se cumple **exactamente una** de las dos alternativas:

$$
\boxed{
\forall n\ge N,
\qquad
\delta<a_n,
}
$$

o bien

$$
\boxed{
\forall n\ge N,
\qquad
a_n<-\delta.
}
$$

Así, una sucesión racional de Cauchy que no es nula no puede seguir cambiando de signo arbitrariamente cerca de cero: termina situada a una distancia positiva de cero y en un solo lado.

**Demostración.**

Por Lema 9.7.2 — Separación eventual respecto de cero existen $\delta>0$ y $N_0\in\mathbb N$ tales que

$$
n\ge N_0
\Longrightarrow
\delta<|a_n|.
$$

Como $a$ es de Cauchy, para la tolerancia positiva $\delta$ existe $N_1\in\mathbb N$ tal que

$$
m,n\ge N_1
\Longrightarrow
|a_m-a_n|<\delta.
$$

Por totalidad de $\mathbb N$, tomamos $N$ igual al mayor de $N_0$ y $N_1$ mediante la correspondiente comparación de los dos índices.

En particular,

$$
\delta<|a_N|,
$$

de modo que $a_N\neq0_{\mathbb Q}$. Por totalidad del orden racional,

$$
0<a_N
\qquad\text{o}\qquad
a_N<0.
$$

Supongamos primero $0<a_N$. Por la definición del valor absoluto,

$$
|a_N|=a_N,
$$

y por tanto

$$
\delta<a_N.
$$

Sea $n\ge N$. Ya sabemos $\delta<|a_n|$. Si $a_n<0$, entonces

$$
|a_n|=-a_n,
$$

y de $\delta<-a_n$ obtenemos

$$
a_n<-\delta.
$$

En consecuencia,

$$
a_N-a_n
>
\delta+\delta
>
\delta.
$$

Como $a_N-a_n>0$, su valor absoluto coincide con él, de manera que

$$
|a_N-a_n|>\delta,
$$

contradiciendo la elección de $N_1$. Por tanto $a_n<0$ es imposible. Debe cumplirse $0\le a_n$, luego $|a_n|=a_n$, y así

$$
\delta<a_n.
$$

Como $n\ge N$ era arbitrario, queda establecida la primera alternativa.

Supongamos ahora $a_N<0$. Entonces

$$
|a_N|=-a_N,
$$

y de $\delta<|a_N|$ obtenemos

$$
a_N<-\delta.
$$

Sea $n\ge N$. Si $0<a_n$, entonces $|a_n|=a_n$ y, por la separación ya conocida,

$$
\delta<a_n.
$$

Por tanto

$$
a_n-a_N
>
\delta+\delta
>
\delta.
$$

Como $a_n-a_N>0$,

$$
|a_n-a_N|=a_n-a_N>\delta,
$$

de nuevo en contradicción con la condición de Cauchy en la cola determinada por $N_1$. Así $0<a_n$ es imposible. Como además $a_n\neq0$ por $\delta<|a_n|$, debe cumplirse

$$
a_n<0.
$$

Entonces $|a_n|=-a_n$, y

$$
\delta<-a_n
$$

equivale a

$$
a_n<-\delta.
$$

Como $n\ge N$ era arbitrario, queda establecida la segunda alternativa.

Finalmente, ambas alternativas no pueden cumplirse simultáneamente, ni siquiera con márgenes e índices distintos. Si eventualmente $\delta<a_n$ y eventualmente $a_n<-\eta$ con $\delta,\eta>0$, al pasar a un índice común tendríamos

$$
0<\delta<a_n<-\eta<0,
$$

contradicción. Por tanto exactamente una de las dos alternativas ocurre. ∎

### Definición 9.8.4 — Orden de Cauchy

Definimos una relación $\le_C$ sobre $\mathbb R_C$ por

$$
\boxed{
x\le_C y
}
$$

si y sólo si existen $a,b\in\mathcal C_{\mathbb Q}$ tales que

$$
x=[a]_C,
\qquad
y=[b]_C,
\qquad
a\preccurlyeq_C b.
$$

Conjuntistamente,

$$
\le_C
:=
\left\{
\langle x,y\rangle
\in
\mathbb R_C\times\mathbb R_C
:
\exists a,b\in\mathcal C_{\mathbb Q}\,
\bigl(
x=[a]_C
\land
y=[b]_C
\land
a\preccurlyeq_C b
\bigr)
\right\}.
$$

Este conjunto existe por separación.

La invariancia demostrada en Proposición 9.8.2 — Propiedades e invariancia de la comparación asintótica (3) garantiza que la definición no depende de los representantes. En particular, para **cualesquiera** $a,b\in\mathcal C_{\mathbb Q}$,

$$
\boxed{
[a]_C\le_C[b]_C
\iff
a\preccurlyeq_C b.
}
$$

Por tanto,

$$
\boxed{
[a]_C\le_C[b]_C
\iff
\forall\varepsilon>0\;
\exists N\in\mathbb N\;
\forall n\ge N,
\quad
a_n<b_n+\varepsilon.
}
$$

El orden estricto asociado, conforme a Definición 0.7.2 — Orden estricto asociado, se denotará por $<_C$:

$$
\boxed{
x<_C y
\iff
x\le_C y
\ \land\\
x\neq y.
}
$$

No se define $<_C$ de manera independiente: es el orden estricto asociado a $\le_C$.

### Teorema 9.8.5 — $\le_C$ es un orden total

La relación $\le_C$ es reflexiva, antisimétrica, transitiva y total sobre $\mathbb R_C$. En consecuencia,

$$
\boxed{
(\mathbb R_C,\le_C)
\text{ es un conjunto totalmente ordenado.}
}
$$

**Demostración.**

**Reflexividad.** Sea $x\in\mathbb R_C$. Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existe $a\in\mathcal C_{\mathbb Q}$ tal que $x=[a]_C$. Por Proposición 9.8.2 — Propiedades e invariancia de la comparación asintótica (1),

$$
a\preccurlyeq_C a,
$$

luego

$$
x\le_C x.
$$

**Antisimetría.** Supongamos

$$
x\le_C y
\qquad\text{y}\qquad
y\le_C x.
$$

Tomemos representantes locales

$$
x=[a]_C,
\qquad
y=[b]_C.
$$

Por el criterio de representantes de Definición 9.8.4 — Orden de Cauchy,

$$
a\preccurlyeq_C b
\qquad\text{y}\qquad
b\preccurlyeq_C a.
$$

Entonces Proposición 9.8.2 — Propiedades e invariancia de la comparación asintótica (4) da

$$
a\sim_C b,
$$

y por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy,

$$
x=[a]_C=[b]_C=y.
$$

**Transitividad.** Supongamos

$$
x\le_C y
\qquad\text{y}\qquad
y\le_C z.
$$

Tomemos representantes locales $a,b,c$ de $x,y,z$. La independencia de representantes permite escribir

$$
a\preccurlyeq_C b,
\qquad
b\preccurlyeq_C c.
$$

Por Proposición 9.8.2 — Propiedades e invariancia de la comparación asintótica (2),

$$
a\preccurlyeq_C c,
$$

de modo que

$$
x\le_C z.
$$

**Totalidad.** Sean $x,y\in\mathbb R_C$, y tomemos representantes

$$
x=[a]_C,
\qquad
y=[b]_C.
$$

Por lógica clásica,

$$
a\sim_C b
\qquad\text{o}\qquad
a\not\sim_C b.
$$

Si $a\sim_C b$, entonces $x=y$ y, por reflexividad, $x\le_C y$ y $y\le_C x$.

Supongamos ahora

$$
a\not\sim_C b.
$$

La sucesión

$$
c:=b-a
$$

pertenece a $\mathcal C_{\mathbb Q}$: el opuesto de $a$ es de Cauchy por Proposición 9.6.3 — El opuesto término a término preserva Cauchy y respeta $\sim_C$ y la suma de dos sucesiones de Cauchy vuelve a ser de Cauchy por Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto.

Además $c$ no es nula. En efecto, si $b-a\in\mathcal N_{\mathbb Q}$, entonces $b\sim_C a$, y por simetría de $\sim_C$ tendríamos $a\sim_C b$, contradicción.

Aplicamos Lema 9.8.3 — Dicotomía eventual de signo a $c$. Existen $\delta>0$ y $N$ tales que ocurre una de las dos alternativas.

Si

$$
\delta<c_n=b_n-a_n
\qquad
(n\ge N),
$$

entonces

$$
a_n<b_n
$$

para todo $n\ge N$. Dado cualquier $\varepsilon>0$,

$$
a_n<b_n<b_n+\varepsilon
$$

en esa misma cola. Por tanto

$$
a\preccurlyeq_C b,
$$

y entonces

$$
x\le_C y.
$$

Si, en cambio,

$$
c_n=b_n-a_n<-\delta
\qquad
(n\ge N),
$$

entonces

$$
b_n<a_n
$$

en esa cola, de donde

$$
b\preccurlyeq_C a
$$

y

$$
y\le_C x.
$$

Así, para cualesquiera $x,y\in\mathbb R_C$,

$$
x\le_C y
\qquad\text{o}\qquad
y\le_C x.
$$

Hemos probado las cuatro propiedades de un orden total. ∎

>
> En particular,
> $$ \boxed{ \text{preorder asintótico} \neq \text{orden total clásico} \neq \text{comparación decidible}. } $$

### Proposición 9.8.6 — Criterio de separación eventual para el orden estricto

Para $a,b\in\mathcal C_{\mathbb Q}$ son equivalentes:

$$
[a]_C<_C[b]_C;
$$

$$
\exists\delta\in\mathbb Q\;
\exists N\in\mathbb N\;
\Bigl(
0<\delta
\ \land\\
\forall n\ge N,\\
\delta<b_n-a_n
\Bigr);
$$

$$
\exists\delta\in\mathbb Q\;
\exists N\in\mathbb N\;
\Bigl(
0<\delta
\ \land\\
\forall n\ge N,\\
a_n+\delta<b_n
\Bigr).
$$

En forma compacta,

$$
\boxed{
[a]_C<_C[b]_C
\iff
\exists\delta>0\;
\exists N\in\mathbb N\;
\forall n\ge N,
\quad
a_n+\delta<b_n.
}
$$

**Demostración.**

Las dos formulaciones con $\delta$ son equivalentes por invariancia estricta del orden racional bajo traslación. Demostraremos la equivalencia con $[a]_C<_C[b]_C$.

Supongamos primero

$$
[a]_C<_C[b]_C.
$$

Entonces

$$
[a]_C\le_C[b]_C
$$

y

$$
[a]_C\neq[b]_C.
$$

La sucesión

$$
c:=b-a
$$

es de Cauchy por la clausura bajo opuesto y suma. Además no es nula: si $c\in\mathcal N_{\mathbb Q}$, entonces $b\sim_C a$ y las clases serían iguales.

Aplicamos Lema 9.8.3 — Dicotomía eventual de signo. Existe $\delta>0$ y una cola en la que o bien

$$
\delta<c_n,
$$

o bien

$$
c_n<-\delta.
$$

La segunda alternativa implicaría, como en la prueba de Teorema 9.8.5 — $\le_C$ es un orden total, que

$$
b\preccurlyeq_C a,
$$

y por tanto

$$
[b]_C\le_C[a]_C.
$$

Junto con $[a]_C\le_C[b]_C$, la antisimetría de Teorema 9.8.5 — $\le_C$ es un orden total daría

$$
[a]_C=[b]_C,
$$

contradicción. Por tanto sólo puede ocurrir la primera alternativa:

$$
\delta<b_n-a_n
$$

eventualmente.

Recíprocamente, supongamos que existen $\delta>0$ y $N$ tales que

$$
n\ge N
\Longrightarrow
\delta<b_n-a_n.
$$

Entonces, para $n\ge N$,

$$
a_n<b_n.
$$

Sea $\varepsilon>0$. Como $b_n<b_n+\varepsilon$,

$$
a_n<b_n+\varepsilon
$$

para todo $n\ge N$. Por tanto

$$
a\preccurlyeq_C b,
$$

y

$$
[a]_C\le_C[b]_C.
$$

Falta excluir la igualdad. Si

$$
[a]_C=[b]_C,
$$

entonces Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy daría

$$
b-a\in\mathcal N_{\mathbb Q}.
$$

Aplicando la definición de nulidad a la tolerancia positiva $\delta$, existiría $N_1$ tal que, para $n\ge N_1$,

$$
|b_n-a_n|<\delta.
$$

Tomamos un índice que domine a $N$ y $N_1$. Allí

$$
0<\delta<b_n-a_n.
$$

Como $b_n-a_n>0$, la definición del valor absoluto da

$$
|b_n-a_n|=b_n-a_n>\delta,
$$

contradicción.

Por tanto

$$
[a]_C\neq[b]_C,
$$

y de la definición del orden estricto asociado obtenemos

$$
[a]_C<_C[b]_C.
$$

∎

> **Advertencia.** La condición meramente puntual «$a_n<b_n$ eventualmente» no se adopta como definición de $[a]_C<_C[b]_C$: puede perderse al cambiar de representantes mediante una perturbación nula. El margen racional positivo $\delta$ es precisamente lo que hace estable la comparación estricta.

> **Nota fundacional.** La dirección desde $x<_Cy$ hacia un margen positivo eventual hereda la
> clasicidad de Lema 9.8.3 — Dicotomía eventual de signo. La dirección inversa —margen positivo dado $\Rightarrow x<_Cy$—
> es constructivamente robusta. Este margen es el candidato natural para una futura relación de
> apartness/orden positivo.

### Lo que hemos ganado

El cociente de Cauchy posee ahora un orden total definido sin apelar a los reales de Dedekind:

$$
\boxed{
(\mathbb R_C,\le_C)
\text{ es totalmente ordenado.}
}
$$

La comparación no se obtuvo declarando que dos representantes deben estar ordenados término a término. Primero se introdujo la relación tolerante

$$
a\preccurlyeq_C b
\iff
\forall\varepsilon>0\;
\exists N\;
\forall n\ge N,
\quad
a_n<b_n+\varepsilon,
$$

se demostró que es invariante bajo $\sim_C$ y sólo entonces se hizo descender al cociente.

El orden estricto recupera una descripción más fuerte y geométrica:

$$
\boxed{
[a]_C<_C[b]_C
\iff
\text{la diferencia }b-a
\text{ queda eventualmente separada de }0
\text{ por un margen racional positivo}.
}
$$

La dicotomía eventual de signo muestra además por qué el orden es total: una sucesión de Cauchy no nula no puede oscilar indefinidamente entre ambos lados de cero.

Todavía falta demostrar que este orden es compatible con la estructura de cuerpo. Antes de hacerlo construiremos, en §9.9, la incrustación canónica de $\mathbb Q$ mediante sucesiones constantes y verificaremos que preserva tanto la aritmética como el orden. Después, en §9.10, podremos cerrar la estructura de cuerpo ordenado.
