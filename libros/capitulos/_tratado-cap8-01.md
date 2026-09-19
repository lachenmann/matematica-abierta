## 8.1. Sucesiones en $\mathbb Q$ {#sec-ta-8-1}

### Definición 8.1.1 — Sucesión racional

Una **sucesión racional** es una función

$$
q:\mathbb N\longrightarrow\mathbb Q.
$$

El conjunto de todas las sucesiones racionales es, por tanto,

$$
\boxed{\mathbb Q^{\mathbb N}}.
$$

Su existencia como conjunto es una instancia de Proposición 0.6.12 — Existencia de $B^A$.

Como una sucesión es en particular una familia indexada, la notación general ya establecida en Definición 0.6.16 — Familia indexada se especializa a

$$
q=(q_n)_{n\in\mathbb N},
\qquad
q_n:=q(n).
$$

No introducimos aquí una nueva convención notacional.

Conviene distinguir tres objetos diferentes:

$$
q,
\qquad
q_n,
\qquad
\{q_n:n\in\mathbb N\}.
$$

El primero es una función; el segundo es un racional; el tercero es el conjunto de valores recorridos por la sucesión. En general, ninguno de estos objetos debe confundirse con los otros.

> **Nota fundacional.** Una sucesión es aquí un objeto extensional, esto es, una función
> $$ \mathbb N\to\mathbb Q. $$
> Esta definición no afirma que exista un algoritmo que, dado $n$, calcule $q_n$:
> $$ \boxed{\text{sucesión}\neq\text{algoritmo}.} $$
> La noción de **nombre efectivo** se introducirá sólo cuando la función venga acompañada de un procedimiento computable para sus términos.

### Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones

Sean

$$
a=(a_n)_{n\in\mathbb N},
\qquad
b=(b_n)_{n\in\mathbb N}
$$

sucesiones racionales. Entonces

$$
\boxed{
a=b
\iff
\forall n\in\mathbb N,\;a_n=b_n.
}
$$

**Demostración.**

Supongamos primero que $a=b$. Para todo $n\in\mathbb N$, la sustitución de iguales da

$$
a(n)=b(n),
$$

es decir,

$$
a_n=b_n.
$$

Recíprocamente, supongamos que

$$
\forall n\in\mathbb N,\qquad a_n=b_n.
$$

Denotemos por $G_a$ y $G_b$ los grafos de $a$ y $b$.

Mostraremos primero

$$
G_a\subseteq G_b.
$$

Sea $p\in G_a$. Como $a:\mathbb N\to\mathbb Q$, su grafo está contenido en $\mathbb N\times\mathbb Q$; por tanto existen $n\in\mathbb N$ y $r\in\mathbb Q$ tales que

$$
p=\langle n,r\rangle.
$$

De

$$
\langle n,r\rangle\in G_a
$$

y de la definición de evaluación se sigue

$$
r=a(n)=a_n.
$$

Por hipótesis,

$$
a_n=b_n=b(n),
$$

de modo que

$$
r=b(n).
$$

Por la definición de evaluación de $b$,

$$
\langle n,r\rangle\in G_b.
$$

Así,

$$
G_a\subseteq G_b.
$$

El mismo argumento, intercambiando $a$ y $b$, da

$$
G_b\subseteq G_a.
$$

Por el criterio extensional de Teorema 0.2.4 — Criterio extensional por doble inclusión,

$$
G_a=G_b.
$$

Además, $a$ y $b$ poseen por definición el mismo dominio $\mathbb N$ y el mismo codominio $\mathbb Q$. El criterio de igualdad de funciones Proposición 0.6.3 — Criterio de igualdad de funciones produce entonces

$$
a=b.
$$

Esto demuestra la equivalencia. ∎

### Definición 8.1.3 — Operaciones puntuales sobre sucesiones racionales

Sean

$$
a=(a_n)_{n\in\mathbb N},
\qquad
b=(b_n)_{n\in\mathbb N}
$$

sucesiones racionales.

Definiremos su suma término a término mediante

$$
\boxed{
(a+b)_n:=a_n+b_n
}
\qquad(n\in\mathbb N).
$$

Esta escritura debe ser legitimada conjuntistamente.

Para $a,b\in\mathbb Q^{\mathbb N}$, consideremos

$$
G_{a+b}
:=
\left\{
\langle n,r\rangle\in\mathbb N\times\mathbb Q:
r=a_n+b_n
\right\}.
$$

El conjunto $G_{a+b}$ existe por separación. Para cada $n\in\mathbb N$, los términos $a_n,b_n$ pertenecen a $\mathbb Q$, y como la suma racional ya es una función

$$
+_{\mathbb Q}:
\mathbb Q\times\mathbb Q
\longrightarrow
\mathbb Q,
$$

existe un único $r\in\mathbb Q$ tal que

$$
r=a_n+b_n.
$$

Por Definición 0.6.1 — Función como dominio, codominio y grafo, $G_{a+b}$ es por tanto el grafo de una función

$$
a+b:\mathbb N\longrightarrow\mathbb Q.
$$

Así $a+b\in\mathbb Q^{\mathbb N}$.

El mismo procedimiento define el opuesto y el producto:

$$
\boxed{
(-a)_n:=-a_n,
}
$$

$$
\boxed{
(ab)_n:=a_nb_n.
}
$$

La sustracción se define por

$$
\boxed{
a-b:=a+(-b),
}
$$

y satisface

$$
\boxed{
(a-b)_n=a_n-b_n.
}
$$

No sólo hemos construido una sucesión para cada par de entradas. Estas asignaciones determinan genuinas operaciones sobre $\mathbb Q^{\mathbb N}$.

En efecto, para la suma consideremos

$$
\mathcal G_+
:=
\left\{
\left\langle
\langle a,b\rangle,c
\right\rangle
\in
\bigl(
\mathbb Q^{\mathbb N}\times\mathbb Q^{\mathbb N}
\bigr)
\times
\mathbb Q^{\mathbb N}
:
\forall n\in\mathbb N,\;
c_n=a_n+b_n
\right\}.
$$

Este conjunto existe por separación. La construcción anterior garantiza la existencia de $c$ para cada par $(a,b)$, y Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones garantiza su unicidad. Por consiguiente, $\mathcal G_+$ es el grafo de una función

$$
+_{\mathrm{seq}}:
\mathbb Q^{\mathbb N}\times\mathbb Q^{\mathbb N}
\longrightarrow
\mathbb Q^{\mathbb N}.
$$

De manera idéntica obtenemos

$$
-_{\mathrm{seq}}:
\mathbb Q^{\mathbb N}
\longrightarrow
\mathbb Q^{\mathbb N}
$$

y

$$
\cdot_{\mathrm{seq}}:
\mathbb Q^{\mathbb N}\times\mathbb Q^{\mathbb N}
\longrightarrow
\mathbb Q^{\mathbb N}.
$$

La sustracción queda determinada por las dos primeras operaciones.

Cuando no haya riesgo de confusión tipológica omitiremos los subíndices `seq` y escribiremos simplemente

$$
a+b,
\qquad
-a,
\qquad
a-b,
\qquad
ab.
$$

> **Nota fundacional.** Ninguna de estas construcciones utiliza el axioma de elección. Para cada índice, el valor correspondiente está determinado de manera única por una operación racional ya construida; los grafos se obtienen por separación dentro de conjuntos ambientes previamente existentes.

### Definición 8.1.4 — Sucesiones constantes

Sea $c\in\mathbb Q$. Definimos la **sucesión constante de valor $c$** por

$$
\boxed{
\underline c:\mathbb N\longrightarrow\mathbb Q,
\qquad
\underline c_n:=c
\quad
\text{para todo }n\in\mathbb N.
}
$$

Concretamente, su grafo es

$$
G_{\underline c}
:=
\{
\langle n,r\rangle\in
\mathbb N\times\mathbb Q:
r=c
\}.
$$

Este conjunto existe por separación y contiene para cada $n\in\mathbb N$ exactamente un par cuyo primer componente es $n$. Por tanto determina una función $\mathbb N\to\mathbb Q$.

La asignación

$$
\kappa:\mathbb Q\longrightarrow\mathbb Q^{\mathbb N},
\qquad
\kappa(c):=\underline c,
$$

es igualmente una función: su grafo puede obtenerse por separación dentro de

$$
\mathbb Q\times\mathbb Q^{\mathbb N},
$$

y la unicidad de la sucesión cuyos términos son todos iguales a $c$ se sigue de Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones.

Debe mantenerse estrictamente la distinción de tipos:

$$
\boxed{
c\in\mathbb Q,
\qquad
\underline c\in\mathbb Q^{\mathbb N}.
}
$$

El racional $c$ y la sucesión constante $\underline c$ no son el mismo objeto. No identificaremos $\mathbb Q$ con un subconjunto de $\mathbb Q^{\mathbb N}$.

### Proposición 8.1.5 — Compatibilidad de las sucesiones constantes con las operaciones puntuales

Para cualesquiera $c,d\in\mathbb Q$,

$$
\boxed{
\underline c+\underline d
=
\underline{c+d},
}
$$

$$
\boxed{
-\underline c
=
\underline{-c},
}
$$

$$
\boxed{
\underline c-\underline d
=
\underline{c-d},
}
$$

y

$$
\boxed{
\underline c\,\underline d
=
\underline{cd}.
}
$$

**Demostración.**

Por Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones basta verificar cada igualdad término a término.

Para todo $n\in\mathbb N$,

$$
(\underline c+\underline d)_n
=
\underline c_n+\underline d_n
=
c+d
=
\underline{c+d}_n.
$$

Por tanto,

$$
\underline c+\underline d
=
\underline{c+d}.
$$

Análogamente,

$$
(-\underline c)_n
=
-\underline c_n
=
-c
=
\underline{-c}_n,
$$

de donde

$$
-\underline c=\underline{-c}.
$$

La sustracción satisface

$$
(\underline c-\underline d)_n
=
\underline c_n-\underline d_n
=
c-d
=
\underline{c-d}_n,
$$

y por ello

$$
\underline c-\underline d
=
\underline{c-d}.
$$

Finalmente,

$$
(\underline c\,\underline d)_n
=
\underline c_n\underline d_n
=
cd
=
\underline{cd}_n,
$$

por lo que

$$
\underline c\,\underline d
=
\underline{cd}.
$$

Quedan demostradas las cuatro identidades. ∎

### Lo que hemos ganado

El objeto

$$
\mathbb Q^{\mathbb N}
$$

ya no es sólo un conjunto de funciones. Disponemos en él de suma, opuesto, sustracción y producto definidos término a término, y de una aplicación

$$
\kappa:\mathbb Q\to\mathbb Q^{\mathbb N}
$$

que transforma cada racional en su sucesión constante y respeta esas operaciones.

Todavía no hemos definido ninguna noción de proximidad entre dos términos racionales ni entre dos sucesiones. Tampoco hemos hablado de convergencia, de la condición de Cauchy, de equivalencia de sucesiones ni de números reales construidos a partir de ellas.

Ésa es precisamente la siguiente dificultad.

Para expresar que dos términos de una sucesión están “cerca” necesitamos convertir su diferencia en una cantidad racional no negativa que mida separación sin depender del orden de los términos. El siguiente paso será, por tanto, construir la **distancia racional** que servirá de lenguaje cuantitativo para las aproximaciones.
