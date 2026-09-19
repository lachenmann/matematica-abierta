## 14.3. Series geométricas {#sec-ta-14-3}

La serie geométrica es el primer ejemplo en el que una fórmula cerrada para las sumas parciales permite transformar el problema de convergencia en el estudio de una sola sucesión auxiliar. Antes de hablar de una suma infinita debemos construir, sin embargo, las potencias naturales y demostrar una identidad **finita**. Este primer tramo no afirma todavía que ninguna serie geométrica converja.

### Definición 14.3.1 — Potencias naturales de un número real

Sea $r\in\mathbb R$. Definimos la **potencia natural de base $r$** como la única sucesión

$$
p^{(r)}:\mathbb N\longrightarrow\mathbb R
$$

que satisface

$$
\boxed{
p^{(r)}_0=1,
\qquad
p^{(r)}_{n+1}=p^{(r)}_n\,r
\quad(n\in\mathbb N).
}
$$

Su existencia y unicidad son una aplicación directa del teorema de recursión Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$ al conjunto $\mathbb R$, al elemento inicial $1\in\mathbb R$ y a la función

$$
M_r:\mathbb R\longrightarrow\mathbb R,
\qquad
M_r(x):=xr.
$$

El grafo de $M_r$ existe por Separación dentro de $\mathbb R\times\mathbb R$ y es funcional y total porque la multiplicación es una operación del cuerpo real. Escribiremos

$$
\boxed{r^n:=p^{(r)}_n.}
$$

Por tanto,

$$
\boxed{
r^0=1,
\qquad
r^{n+1}=r^n r.
}
$$

La asignación $(r,n)\mapsto r^n$ determina además una función

$$
\operatorname{pow}_{\mathbb R}:\mathbb R\times\mathbb N\longrightarrow\mathbb R,
$$

pues su grafo se obtiene por Separación y, para cada par $(r,n)$, la recursión anterior determina un único valor.

Adoptamos en particular

$$
0^0=1,
$$

como consecuencia de la cláusula recursiva inicial. Esta convención no expresa una operación de división ni un paso al límite; sólo fija el valor de la potencia de exponente cero.

> **Control de lectura.** La expresión $r^n$ acaba de adquirir significado para **todo** $r\in\mathbb R$ y $n\in\mathbb N$. No estamos usando una potencia previamente disponible de manera informal: la hemos construido por recursión.

---

### Proposición 14.3.2 — Identidad finita de la suma geométrica

Para todo $r\in\mathbb R$ y todo $n\in\mathbb N$,

$$
\boxed{
(1-r)\sum_{k=0}^{n}r^k
=1-r^{n+1}.
}
$$

**Demostración.**

Fijemos $r\in\mathbb R$ e induzcamos sobre $n$.

Para $n=0$, por la definición de suma finita y de potencia natural,

$$
\sum_{k=0}^{0}r^k=r^0=1.
$$

Por tanto

$$
(1-r)\sum_{k=0}^{0}r^k
=(1-r)\cdot1
=1-r
=1-r^1.
$$

Supongamos ahora que

$$
(1-r)\sum_{k=0}^{n}r^k
=1-r^{n+1}.
$$

La recurrencia de las sumas parciales da

$$
\sum_{k=0}^{n+1}r^k
=\left(\sum_{k=0}^{n}r^k\right)+r^{n+1}.
$$

Multiplicando por $1-r$ y usando distributividad,

$$
\begin{aligned}
(1-r)\sum_{k=0}^{n+1}r^k
&=(1-r)\sum_{k=0}^{n}r^k+(1-r)r^{n+1}\\
&=1-r^{n+1}+r^{n+1}-r\,r^{n+1}\\
&=1-r^{n+2}.
\end{aligned}
$$

En el último paso usamos la conmutatividad del producto real y la ecuación recursiva

$$
r^{n+2}=r^{n+1}r.
$$

El principio de inducción Teorema 1.1.10 — Principio de inducción concluye la identidad para todo $n\in\mathbb N$. ∎

> **Frontera deductiva.** Esta proposición es puramente algebraica y finita. No se ha tomado ningún límite y no se ha dividido por $1-r$. En particular, el caso $r=1$ está incluido y produce la identidad trivial $0=0$. La convergencia de la serie geométrica y la fórmula de su suma requerirán un argumento adicional, que constituirá el siguiente tramo de §14.3.

---

### Lema 14.3.3 — El valor absoluto conmuta con las potencias naturales

Para todo $r\in\mathbb R$ y todo $n\in\mathbb N$,

$$
\boxed{|r^n|=|r|^n.}
$$

**Demostración.**

Fijemos $r\in\mathbb R$ e induzcamos sobre $n$. Para $n=0$,

$$
|r^0|=|1|=1=|r|^0.
$$

Si $|r^n|=|r|^n$, la recurrencia de las potencias y la multiplicatividad del valor absoluto Proposición 4.2.2 — Propiedades elementales del valor absoluto dan

$$
\begin{aligned}
|r^{n+1}|
&=|r^nr|\\
&=|r^n|\,|r|\\
&=|r|^n|r|\\
&=|r|^{n+1}.
\end{aligned}
$$

El principio de inducción Teorema 1.1.10 — Principio de inducción concluye la igualdad para todo $n\in\mathbb N$. ∎

---

### Teorema 14.3.4 — Las potencias de una base de módulo menor que uno tienden a cero

Sea $r\in\mathbb R$. Si

$$
\boxed{|r|<1,}
$$

entonces

$$
\boxed{r^n\longrightarrow0.}
$$

**Demostración.**

Pongamos $q:=|r|$. Entonces $0\le q<1$ y consideremos

$$
p_n:=q^n.
$$

Por inducción, $p_n\ge0$ para todo $n$. Además, $q\le1$, y por compatibilidad del orden con el producto por un elemento no negativo,

$$
p_{n+1}=p_nq\le p_n.
$$

Así $p$ es decreciente y está acotada inferiormente por $0$. Por el teorema de convergencia monótona Teorema 13.7.3 — Teorema de convergencia monótona, existe $L\in\mathbb R$ tal que

$$
p_n\longrightarrow L.
$$

La cola reindexada $p^{\langle1\rangle}$ es una subsucesión de $p$ por Proposición 13.9.4 — Las colas son subsucesiones y las subsucesiones se componen, de modo que Teorema 13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite da

$$
p_{1+n}\longrightarrow L.
$$

Por la aritmética natural y la recurrencia de las potencias,

$$
p_{1+n}=p_{n+1}=q^{n+1}=q\,q^n=qp_n.
$$

Por Corolario 13.5.4 — Compatibilidad con la multiplicación por una constante,

$$
qp_n\longrightarrow qL.
$$

La unicidad del límite Teorema 13.3.5 — Unicidad del límite real obliga a que $L=qL$, luego

$$
(1-q)L=0.
$$

Como $q<1$, el factor $1-q$ es estrictamente positivo y, en particular, no nulo. Multiplicando por su inverso concluimos $L=0$. Por tanto

$$
|r|^n\longrightarrow0.
$$

Finalmente, Lema 14.3.3 — El valor absoluto conmuta con las potencias naturales da

$$
|r^n-0|=|r^n|=|r|^n.
$$

La definición de convergencia prueba entonces

$$
r^n\longrightarrow0.
$$

∎

> **Lectura estructural.** La completitud se usa para garantizar la existencia del límite de la sucesión monótona $|r|^n$. No se construye un módulo efectivo de convergencia; la ecuación satisfecha por el límite es la que permite identificarlo como $0$.

---

### Teorema 14.3.5 — Convergencia y suma de la serie geométrica para $|r|<1$

Sea $r\in\mathbb R$ y supongamos $|r|<1$. Entonces la serie geométrica

$$
\sum_{k=0}^{\infty}r^k
$$

converge y

$$
\boxed{
\sum_{k=0}^{\infty}r^k=(1-r)^{-1}.
}
$$

Equivalentemente,

$$
\boxed{
\sum_{k=0}^{\infty}r^k=\frac1{1-r}.
}
$$

**Demostración.**

Sea

$$
s_n:=\sum_{k=0}^{n}r^k.
$$

De $|r|<1$ se deduce $r\ne1$, pues $r=1$ implicaría $|r|=1$. Por tanto $1-r\ne0$ y existe $(1-r)^{-1}$.

La identidad finita Proposición 14.3.2 — Identidad finita de la suma geométrica da

$$
(1-r)s_n=1-r^{n+1},
$$

y multiplicando por $(1-r)^{-1}$ obtenemos

$$
\boxed{
s_n=(1-r)^{-1}(1-r^{n+1}).
}
$$

Por Teorema 14.3.4 — Las potencias de una base de módulo menor que uno tienden a cero, $r^n\to0$. Como $r^{n+1}=rr^n$, Corolario 13.5.4 — Compatibilidad con la multiplicación por una constante da

$$
r^{n+1}\longrightarrow0.
$$

La sucesión constante de valor $1$ converge a $1$ por Proposición 13.3.4 — Las sucesiones constantes convergen a su valor; aplicando Proposición 13.5.2 — Límite del opuesto y de una diferencia,

$$
1-r^{n+1}\longrightarrow1.
$$

Otra aplicación de Corolario 13.5.4 — Compatibilidad con la multiplicación por una constante, ahora con la constante $(1-r)^{-1}$, produce

$$
s_n\longrightarrow(1-r)^{-1}.
$$

Por Definición 14.1.4 — Convergencia, divergencia y suma de una serie, la serie geométrica converge y su suma es $(1-r)^{-1}$. ∎

> **Frontera del tramo B.** Hemos probado
> $$
> |r|<1
> \Longrightarrow
> \sum_{k=0}^{\infty}r^k\text{ converge}.
> $$
> Los casos $|r|\ge1$ se resuelven a continuación, usando la condición necesaria sobre el término general ya cerrada en §14.2.

---

### Proposición 14.3.6 — Si $|r|\ge1$, las potencias no tienden a cero

Sea $r\in\mathbb R$ y supongamos $|r|\ge1$. Entonces

$$
\boxed{\forall n\in\mathbb N,\quad |r^n|\ge1,}
$$

y, en particular, la sucesión $(r^n)$ **no converge a cero**.

**Demostración.**

Escribamos $q:=|r|$, de modo que $q\ge1>0$. Demostraremos por inducción que $q^n\ge1$ para todo natural $n$.

En $n=0$, la definición de potencia natural da $q^0=1$. Si $q^n\ge1$, entonces $q^n\ge0$ y, como $q\ge1$, la compatibilidad del producto con el orden entrega

$$
q^{n+1}=q^nq\ge q^n\cdot1=q^n\ge1.
$$

La inducción está completa. Por Lema 14.3.3 — El valor absoluto conmuta con las potencias naturales,

$$
|r^n|=|r|^n=q^n\ge1
\qquad(n\in\mathbb N).
$$

Supongamos, buscando una contradicción, que $r^n\to0$. Aplicando la definición de convergencia con la tolerancia real positiva $\varepsilon=1$, existiría $N\in\mathbb N$ tal que

$$
|r^n-0|<1\qquad(n\ge N).
$$

En particular, para $n=N$ tendríamos simultáneamente $1\le|r^N|<1$, contradicción. Por consiguiente, $r^n\not\to0$. ∎

> **Control de casos fronterizos.** El argumento incluye $r=1$ y $r=-1$, además de toda base con $|r|>1$. No necesita demostrar que las potencias crezcan sin cota: basta la cota inferior uniforme de su módulo. No se ha usado completitud ni Choice.

---

### Teorema 14.3.7 — Clasificación completa de la serie geométrica

Para todo $r\in\mathbb R$, la serie geométrica cumple

$$
\boxed{
\sum_{k=0}^{\infty}r^k\text{ converge en }\mathbb R
\quad\Longleftrightarrow\quad |r|<1.
}
$$

Cuando converge, su suma es

$$
\boxed{\displaystyle\sum_{k=0}^{\infty}r^k=\frac1{1-r}.}
$$

Si $|r|\ge1$, la serie diverge y la expresión $\sum_{k=0}^{\infty}r^k$ **no tiene valor real** como suma.

**Demostración.**

Si $|r|<1$, Teorema 14.3.5 — Convergencia y suma de la serie geométrica para $|r|<1$ demuestra que la serie converge y que su suma es $(1-r)^{-1}=1/(1-r)$.

Si $|r|\ge1$, Proposición 14.3.6 — Si $|r|\ge1$, las potencias no tienden a cero establece que sus términos $a_n:=r^n$ **no** tienden a cero. El criterio de divergencia por el término general Corolario 14.2.5 — Criterio de divergencia por el término general implica que la serie diverge.

Recíprocamente, supongamos que la serie converge. No puede cumplirse $|r|\ge1$, pues acabamos de demostrar que esa hipótesis entraña divergencia. Por la totalidad del orden del cuerpo real, $|r|<1$. Queda demostrada la equivalencia y la fórmula de la suma en todos los casos en que ésta existe. ∎

> **Interpretación.** La fórmula $1/(1-r)$ sólo representa la suma de la serie cuando $|r|<1$. Para $r=-1$, el denominador es no nulo y el cociente algebraico existe, pero la serie $1-1+1-1+\cdots$ diverge: no está permitido atribuirle ese cociente como suma ordinaria. Para $r=1$, además de divergir, el cociente ni siquiera está definido.

La serie geométrica nos ha permitido distinguir una **fórmula finita**, una **condición de convergencia** y el **valor de la suma**. En §14.4 pasaremos a las series de términos no negativos, donde la monotonía de las sumas parciales conducirá al primer criterio estructural de convergencia para una clase amplia de series.

---
