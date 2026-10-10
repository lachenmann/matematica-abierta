## 13.1. Sucesiones como funciones {#sec-ta-13-1}

### Definición 13.1.1 — Sucesión real

Una sucesión real es una función

$$
\boxed{
a:\mathbb N\longrightarrow\mathbb R.
}
$$

El conjunto de todas las sucesiones reales es, por tanto,

$$
\boxed{
\mathbb R^{\mathbb N}.
}
$$

Su existencia como conjunto es una instancia de Proposición 0.6.12 — Existencia de $B^A$, aplicada a los conjuntos $\mathbb N$ y $\mathbb R$.

Como una sucesión es una familia indexada, utilizaremos la notación general ya fijada en Definición 0.6.16 — Familia indexada:

$$
a=(a_n)_{n\in\mathbb N},
\qquad
a_n:=a(n).
$$

No introducimos una convención notacional nueva. Cuando el conjunto de índices sea inequívoco escribiremos también, de manera abreviada,

$$
(a_n).
$$

La definición obliga a distinguir tres objetos:

$$
\boxed{
 a,
 \qquad
 a_n,
 \qquad
 \{a_n:n\in\mathbb N\}.
}
$$

Aquí $a$ es una función, $a_n$ es un número real y $\{a_n:n\in\mathbb N\}$ es el recorrido de la sucesión. Una sucesión no queda determinada únicamente por su recorrido: el índice forma parte de su estructura. El orden en que aparecen los términos y sus posibles repeticiones son datos matemáticos del objeto.

> **Lectura conceptual.** Una sucesión no es todavía un límite ni una aproximación. La definición sólo organiza una familia numerable de reales. Palabras como «se acerca», «tiende» o «se estabiliza» adquirirán contenido matemático únicamente después de introducir cuantificadores que expresen qué ocurre para índices suficientemente grandes.

> **Nota fundacional.** Al igual que en el Capítulo 8, la sucesión es un objeto extensional. La existencia de una función $a:\mathbb N\to\mathbb R$ no afirma que exista un algoritmo que calcule $a_n$ a partir de $n$. No confundiremos existencia conjuntista, especificación matemática y computabilidad.

### Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales

Sean

$$
a=(a_n)_{n\in\mathbb N},
\qquad
b=(b_n)_{n\in\mathbb N}
$$

sucesiones reales. Entonces

$$
\boxed{
a=b
\iff
\forall n\in\mathbb N,\;a_n=b_n.
}
$$

**Demostración.**

Si $a=b$, entonces para cada $n\in\mathbb N$ la sustitución de iguales produce

$$
a(n)=b(n),
$$

y por tanto

$$
a_n=b_n.
$$

Recíprocamente, supongamos

$$
\forall n\in\mathbb N,
\qquad
a_n=b_n.
$$

Sean $G_a$ y $G_b$ los grafos de $a$ y $b$. Mostraremos

$$
G_a=G_b.
$$

Sea $p\in G_a$. Puesto que $a:\mathbb N\to\mathbb R$, existen $n\in\mathbb N$ y $x\in\mathbb R$ tales que

$$
p=\langle n,x\rangle
$$

y

$$
x=a(n)=a_n.
$$

Por hipótesis,

$$
a_n=b_n=b(n),
$$

de modo que

$$
\langle n,x\rangle\in G_b.
$$

Así $G_a\subseteq G_b$. Intercambiando $a$ y $b$ obtenemos $G_b\subseteq G_a$; por Teorema 0.2.4 — Criterio extensional por doble inclusión,

$$
G_a=G_b.
$$

Las dos funciones tienen además el mismo dominio $\mathbb N$ y el mismo codominio $\mathbb R$. El criterio de igualdad de funciones Proposición 0.6.3 — Criterio de igualdad de funciones da entonces

$$
a=b.
$$

Queda demostrada la equivalencia. ∎

La proposición anterior será utilizada constantemente. En adelante, para demostrar una igualdad entre sucesiones podremos trabajar término a término, siempre que la igualdad obtenida valga para todo índice natural.

### Definición 13.1.3 — Operaciones puntuales sobre sucesiones reales

Sean

$$
a=(a_n)_{n\in\mathbb N},
\qquad
b=(b_n)_{n\in\mathbb N}
$$

sucesiones reales.

Definimos su suma puntual, su opuesto puntual y su producto puntual mediante

$$
\boxed{
(a+b)_n:=a_n+b_n,
}
$$

$$
\boxed{
(-a)_n:=-a_n,
}
$$

$$
\boxed{
(ab)_n:=a_nb_n
}
$$

para todo $n\in\mathbb N$. La sustracción se define por

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

Debemos verificar que estas fórmulas determinan realmente sucesiones.

Para la suma, fijados $a,b\in\mathbb R^{\mathbb N}$, consideremos

$$
G_{a+b}
:=
\left\{
\langle n,x\rangle\in\mathbb N\times\mathbb R:
 x=a_n+b_n
\right\}.
$$

El conjunto existe por Separación. Para cada $n\in\mathbb N$, como $a_n,b_n\in\mathbb R$ y la suma real es una operación

$$
+_{\mathbb R}:\mathbb R\times\mathbb R\longrightarrow\mathbb R,
$$

existe un único $x\in\mathbb R$ tal que $x=a_n+b_n$. Por Definición 0.6.1 — Función como dominio, codominio y grafo, $G_{a+b}$ es el grafo de una función

$$
a+b:\mathbb N\longrightarrow\mathbb R.
$$

El mismo argumento, usando las operaciones de opuesto y producto del cuerpo real, produce sucesiones $-a$ y $ab$.

Estas construcciones determinan operaciones genuinas sobre el conjunto de sucesiones. Para la suma, por ejemplo, el grafo

$$
\mathcal G_+
:=
\left\{
\left\langle\langle a,b\rangle,c\right\rangle
\in
\bigl(\mathbb R^{\mathbb N}\times\mathbb R^{\mathbb N}\bigr)
\times\mathbb R^{\mathbb N}:
\forall n\in\mathbb N,\;c_n=a_n+b_n
\right\}
$$

existe por Separación. La construcción precedente da existencia para cada par $(a,b)$ y Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales da unicidad. Por tanto determina una función

$$
+_{\mathrm{seq}}:
\mathbb R^{\mathbb N}\times\mathbb R^{\mathbb N}
\longrightarrow
\mathbb R^{\mathbb N}.
$$

De igual modo obtenemos

$$
-_{\mathrm{seq}}:
\mathbb R^{\mathbb N}\longrightarrow\mathbb R^{\mathbb N}
$$

y

$$
\cdot_{\mathrm{seq}}:
\mathbb R^{\mathbb N}\times\mathbb R^{\mathbb N}
\longrightarrow
\mathbb R^{\mathbb N}.
$$

Cuando el tipo sea inequívoco omitiremos el subíndice `seq`.

> **Principio de lectura.** Las operaciones sobre sucesiones se realizan índice por índice. Esto permite heredar identidades algebraicas del cuerpo real, pero no autoriza todavía a intercambiar operaciones con límites: esa será una afirmación matemática posterior que deberá demostrarse.

### Definición 13.1.4 — Sucesiones reales constantes

Sea $c\in\mathbb R$. Definimos la sucesión real constante de valor $c$ por

$$
\boxed{
\underline c:\mathbb N\longrightarrow\mathbb R,
\qquad
\underline c_n:=c
\quad(n\in\mathbb N).
}
$$

Su grafo es

$$
G_{\underline c}
:=
\left\{
\langle n,x\rangle\in\mathbb N\times\mathbb R:
x=c
\right\},
$$

que existe por Separación y determina una función $\mathbb N\to\mathbb R$.

La asignación

$$
\boxed{
\kappa_{\mathbb R}:\mathbb R\longrightarrow\mathbb R^{\mathbb N},
\qquad
\kappa_{\mathbb R}(c):=\underline c
}
$$

es una función. Su grafo se obtiene por Separación dentro de

$$
\mathbb R\times\mathbb R^{\mathbb N},
$$

y la unicidad de la sucesión cuyos términos son todos iguales a $c$ se sigue de Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales.

La distinción de tipos seguirá siendo estricta:

$$
\boxed{
 c\in\mathbb R,
 \qquad
 \underline c\in\mathbb R^{\mathbb N}.
}
$$

No identificaremos un número real con la sucesión constante que determina.

### Proposición 13.1.5 — Compatibilidad de las sucesiones constantes con las operaciones puntuales

Para todos $c,d\in\mathbb R$ se cumplen

$$
\boxed{
\underline c+\underline d=\underline{c+d},
}
$$

$$
\boxed{
-\underline c=\underline{-c},
}
$$

$$
\boxed{
\underline c\,\underline d=\underline{cd}.
}
$$

En consecuencia,

$$
\boxed{
\underline c-\underline d=\underline{c-d}.
}
$$

**Demostración.**

Fijemos $n\in\mathbb N$. Por las definiciones de operación puntual y sucesión constante,

$$
(\underline c+\underline d)_n
=
\underline c_n+\underline d_n
=
c+d
=
\underline{c+d}_n.
$$

Como esta igualdad vale para todo $n\in\mathbb N$, Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales da

$$
\underline c+\underline d=\underline{c+d}.
$$

Del mismo modo,

$$
(-\underline c)_n
=-\underline c_n
=-c
=
\underline{-c}_n,
$$

y

$$
(\underline c\,\underline d)_n
=
\underline c_n\underline d_n
=cd
=
\underline{cd}_n.
$$

Aplicando nuevamente Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales obtenemos las dos identidades restantes. Finalmente,

$$
\underline c-\underline d
=
\underline c+(-\underline d)
=
\underline c+\underline{-d}
=
\underline{c-d}.
$$

Esto prueba todas las afirmaciones. ∎

La aplicación $\kappa_{\mathbb R}$ reproduce así, dentro de las sucesiones, la aritmética del cuerpo real. No necesitamos todavía clasificar esta observación mediante vocabulario algebraico adicional; lo importante para el análisis es que las sucesiones constantes proporcionan el primer modelo de comportamiento asintótico perfectamente estable.
