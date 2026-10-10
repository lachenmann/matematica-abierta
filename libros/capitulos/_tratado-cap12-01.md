## 12.1. Subcuerpo primo de un cuerpo ordenado {#sec-ta-12-1}

Fijemos durante toda la sección un cuerpo ordenado

$$
F=(F,+,\cdot,0_F,1_F,\le_F).
$$

La aplicación de numerales

$$
\nu_F:\mathbb N\to F
$$

ya está disponible por Definición 4.1.5 — Aplicación de numerales naturales en un cuerpo ordenado. Para prolongarla a los enteros no podemos escribir simplemente $m-n$ dentro de $\mathbb N$: debemos respetar la construcción de $\mathbb Z$ como cociente de pares de naturales. Por ello comenzamos en el nivel de representantes.

### Definición 12.1.1 — Evaluación de diferencias formales en un cuerpo ordenado

Definimos

$$
\boxed{
\theta_F:\mathbb N\times\mathbb N\longrightarrow F,
\qquad
\theta_F(m,n):=\nu_F(m)-\nu_F(n).
}
$$

Aquí la resta se interpreta en el grupo aditivo subyacente al cuerpo $F$:

$$
\nu_F(m)-\nu_F(n)
=
\nu_F(m)+(-\nu_F(n)).
$$

El grafo de $\theta_F$ se obtiene por Separación dentro de

$$
(\mathbb N\times\mathbb N)\times F,
$$

pues para cada par $(m,n)$ el término $\nu_F(m)-\nu_F(n)$ determina un único elemento de $F$.

La función $\theta_F$ todavía vive sobre pares de naturales. Para obtener una función definida sobre $\mathbb Z$ debemos demostrar que dos pares equivalentes producen el mismo valor.

### Proposición 12.1.2 — Invariancia bajo la equivalencia entera

Si

$$
(m,n)\sim_{\mathbb Z}(p,q),
$$

entonces

$$
\boxed{
\theta_F(m,n)=\theta_F(p,q).
}
$$

**Demostración.**

Por Definición 2.1.1 — Relación de equivalencia entera, la hipótesis significa

$$
m+q=n+p.
$$

Aplicando $\nu_F$ a ambos miembros y usando la compatibilidad con la suma de Proposición 4.1.6 — Aritmética y orden de los numerales naturales, obtenemos

$$
\nu_F(m)+\nu_F(q)
=
\nu_F(n)+\nu_F(p).
$$

Sumemos a ambos lados $-\nu_F(n)-\nu_F(q)$. Las leyes del grupo aditivo de $F$ dan

$$
\nu_F(m)-\nu_F(n)
=
\nu_F(p)-\nu_F(q).
$$

Por Definición 12.1.1 — Evaluación de diferencias formales en un cuerpo ordenado, esto es exactamente

$$
\theta_F(m,n)=\theta_F(p,q).
$$

Por tanto $\theta_F$ es constante sobre cada clase de la equivalencia que define a $\mathbb Z$. ∎

### Definición 12.1.3 — Copia canónica de los enteros en un cuerpo ordenado

Como

$$
\mathbb Z=(\mathbb N\times\mathbb N)/{\sim_{\mathbb Z}}
$$

y Proposición 12.1.2 — Invariancia bajo la equivalencia entera demuestra que $\theta_F$ es constante sobre las clases, el principio de definición sobre clases Teorema 0.6.15 — Principio de definición sobre clases produce una única función

$$
\boxed{
\jmath_{\mathbb Z}^{F}:\mathbb Z\longrightarrow F
}
$$

tal que, para todo $m,n\in\mathbb N$,

$$
\boxed{
\jmath_{\mathbb Z}^{F}\bigl([(m,n)]_{\mathbb Z}\bigr)
=
\nu_F(m)-\nu_F(n).
}
$$

Llamaremos a $\jmath_{\mathbb Z}^{F}$ la copia canónica de los enteros en $F$.

No se ha escogido un representante de cada entero. La función inducida existe porque una función ya definida sobre todos los representantes es constante en cada clase; el descenso al cociente es funcional y canónico.

### Proposición 12.1.4 — Compatibilidad aritmética de la copia entera

Para todos $x,y\in\mathbb Z$ y todo $n\in\mathbb N$ se cumplen:

$$
\boxed{
\jmath_{\mathbb Z}^{F}(0_{\mathbb Z})=0_F,
\qquad
\jmath_{\mathbb Z}^{F}(1_{\mathbb Z})=1_F,
}
$$

$$
\boxed{
\jmath_{\mathbb Z}^{F}(x+y)
=
\jmath_{\mathbb Z}^{F}(x)+\jmath_{\mathbb Z}^{F}(y),
}
$$

$$
\boxed{
\jmath_{\mathbb Z}^{F}(-x)
=
-\jmath_{\mathbb Z}^{F}(x),
}
$$

$$
\boxed{
\jmath_{\mathbb Z}^{F}(xy)
=
\jmath_{\mathbb Z}^{F}(x)\jmath_{\mathbb Z}^{F}(y),
}
$$

y

$$
\boxed{
\jmath_{\mathbb Z}^{F}\bigl(\iota_{\mathbb N}^{\mathbb Z}(n)\bigr)
=
\nu_F(n).
}
$$

**Demostración.**

Fijemos representantes

$$
x=[(a,b)]_{\mathbb Z},
\qquad
y=[(c,d)]_{\mathbb Z}.
$$

La fórmula de Definición 12.1.3 — Copia canónica de los enteros en un cuerpo ordenado permite calcular sobre estos representantes sin que el resultado dependa de la elección realizada.

Para el cero y la unidad,

$$
\jmath_{\mathbb Z}^{F}(0_{\mathbb Z})
=
\jmath_{\mathbb Z}^{F}([(0,0)]_{\mathbb Z})
=
\nu_F(0)-\nu_F(0)
=
0_F,
$$

mientras que

$$
\jmath_{\mathbb Z}^{F}(1_{\mathbb Z})
=
\jmath_{\mathbb Z}^{F}([(1,0)]_{\mathbb Z})
=
\nu_F(1)-\nu_F(0)
=
1_F
$$

por Proposición 4.1.6 — Aritmética y orden de los numerales naturales.

La suma entera satisface

$$
x+y=[(a+c,b+d)]_{\mathbb Z}.
$$

Por tanto,

$$
\begin{aligned}
\jmath_{\mathbb Z}^{F}(x+y)
&=\nu_F(a+c)-\nu_F(b+d)\\
&=(\nu_F(a)+\nu_F(c))-(\nu_F(b)+\nu_F(d))\\
&=(\nu_F(a)-\nu_F(b))+(\nu_F(c)-\nu_F(d))\\
&=\jmath_{\mathbb Z}^{F}(x)+\jmath_{\mathbb Z}^{F}(y).
\end{aligned}
$$

Por Proposición 2.4.3 — Buena definición del opuesto,

$$
-x=[(b,a)]_{\mathbb Z},
$$

luego

$$
\jmath_{\mathbb Z}^{F}(-x)
=
\nu_F(b)-\nu_F(a)
=
-(\nu_F(a)-\nu_F(b))
=
-\jmath_{\mathbb Z}^{F}(x).
$$

Para el producto, Definición 2.5.3 — Multiplicación en $\mathbb Z$ da

$$
xy
=
[(ac+bd,ad+bc)]_{\mathbb Z}.
$$

Usando las compatibilidades aditiva y multiplicativa de $\nu_F$,

$$
\begin{aligned}
\jmath_{\mathbb Z}^{F}(xy)
&=\nu_F(ac+bd)-\nu_F(ad+bc)\\
&=\nu_F(a)\nu_F(c)+\nu_F(b)\nu_F(d)
  -\nu_F(a)\nu_F(d)-\nu_F(b)\nu_F(c)\\
&=(\nu_F(a)-\nu_F(b))(\nu_F(c)-\nu_F(d))\\
&=\jmath_{\mathbb Z}^{F}(x)\jmath_{\mathbb Z}^{F}(y).
\end{aligned}
$$

Finalmente, por Definición 2.7.1 — Incrustación natural en los enteros,

$$
\iota_{\mathbb N}^{\mathbb Z}(n)=[(n,0)]_{\mathbb Z},
$$

y por consiguiente

$$
\jmath_{\mathbb Z}^{F}\bigl(\iota_{\mathbb N}^{\mathbb Z}(n)\bigr)
=
\nu_F(n)-\nu_F(0)
=
\nu_F(n).
$$

Quedan verificadas todas las identidades. ∎

### Teorema 12.1.5 — La copia entera es una incrustación ordenada

La función

$$
\jmath_{\mathbb Z}^{F}:\mathbb Z\to F
$$

es inyectiva y, para todos $x,y\in\mathbb Z$,

$$
\boxed{
x\le_{\mathbb Z}y
\iff
\jmath_{\mathbb Z}^{F}(x)
\le_F
\jmath_{\mathbb Z}^{F}(y).
}
$$

En particular, también preserva y refleja el orden estricto.

**Demostración.**

Comenzamos por la inyectividad. Supongamos

$$
\jmath_{\mathbb Z}^{F}(z)=0_F.
$$

Por la forma normal con signo Teorema 2.8.1 — Forma normal con signo, existe $n\in\mathbb N$ tal que

$$
z=\iota_{\mathbb N}^{\mathbb Z}(n)
$$

o bien

$$
z=-\iota_{\mathbb N}^{\mathbb Z}(n).
$$

En el primer caso, Proposición 12.1.4 — Compatibilidad aritmética de la copia entera da

$$
0_F
=
\jmath_{\mathbb Z}^{F}(z)
=
\nu_F(n).
$$

Como $\nu_F(0)=0_F$ y $\nu_F$ es inyectiva por Proposición 4.1.6 — Aritmética y orden de los numerales naturales, resulta $n=0$. Luego $z=0_{\mathbb Z}$. En el segundo caso,

$$
0_F
=
-\nu_F(n)
$$

implica igualmente $\nu_F(n)=0_F$, de modo que $n=0$ y otra vez $z=0_{\mathbb Z}$.

Hemos probado

$$
\jmath_{\mathbb Z}^{F}(z)=0_F
\Longrightarrow
z=0_{\mathbb Z}.
$$

Si ahora

$$
\jmath_{\mathbb Z}^{F}(x)
=
\jmath_{\mathbb Z}^{F}(y),
$$

la compatibilidad con suma y opuesto de Proposición 12.1.4 — Compatibilidad aritmética de la copia entera produce

$$
\jmath_{\mathbb Z}^{F}(x-y)=0_F.
$$

Por lo anterior, $x-y=0_{\mathbb Z}$, y las leyes del grupo aditivo entero dan $x=y$. Así $\jmath_{\mathbb Z}^{F}$ es inyectiva.

Probemos ahora la preservación del orden. Si

$$
x\le_{\mathbb Z}y,
$$

por Definición 2.9.1 — Relación de orden entera existe $n\in\mathbb N$ tal que

$$
y=x+\iota_{\mathbb N}^{\mathbb Z}(n).
$$

Aplicando Proposición 12.1.4 — Compatibilidad aritmética de la copia entera,

$$
\jmath_{\mathbb Z}^{F}(y)
=
\jmath_{\mathbb Z}^{F}(x)+\nu_F(n).
$$

Como $0\le n$ en $\mathbb N$ y Proposición 4.1.6 — Aritmética y orden de los numerales naturales preserva el orden, $0_F\le_F\nu_F(n)$; por tanto la compatibilidad del orden con la suma en el cuerpo ordenado $F$ implica

$$
\jmath_{\mathbb Z}^{F}(x)
\le_F
\jmath_{\mathbb Z}^{F}(y).
$$

Para la reflexión, supongamos

$$
\jmath_{\mathbb Z}^{F}(x)
\le_F
\jmath_{\mathbb Z}^{F}(y).
$$

Por la tricotomía decidible de Corolario 2.9.6 — Tricotomía decidible en $\mathbb Z$, la comparación de $x$ e $y$ se resuelve constructivamente; en particular, se cumple $x\le_{\mathbb Z}y$ o $y\le_{\mathbb Z}x$. En el primer caso terminamos. En el segundo, la preservación ya demostrada da

$$
\jmath_{\mathbb Z}^{F}(y)
\le_F
\jmath_{\mathbb Z}^{F}(x).
$$

La antisimetría en $F$ produce igualdad de las dos imágenes; por inyectividad, $x=y$. En particular $x\le_{\mathbb Z}y$.

Queda demostrada la equivalencia de órdenes. Como el orden estricto es el asociado al orden no estricto y la función es inyectiva, también

$$
x<_{\mathbb Z}y
\iff
\jmath_{\mathbb Z}^{F}(x)
<_F
\jmath_{\mathbb Z}^{F}(y).
$$

∎

El teorema contiene un hecho estructural importante: todo cuerpo ordenado tiene característica cero en el sentido relevante para este tratado. Los enteros construidos en el Capítulo 2 aparecen en él de una manera canónica e inyectiva; no pueden colapsar dos enteros distintos.

### Corolario 12.1.6 — La copia entera está contenida en el subcuerpo primo

Para todo cuerpo ordenado $F$,

$$
\boxed{
\jmath_{\mathbb Z}^{F}[\mathbb Z]
\subseteq
P_F.
}
$$

**Demostración.**

Sea $z\in\mathbb Z$. Por Teorema 2.8.1 — Forma normal con signo existe $n\in\mathbb N$ tal que

$$
z=\iota_{\mathbb N}^{\mathbb Z}(n)
$$

o

$$
z=-\iota_{\mathbb N}^{\mathbb Z}(n).
$$

En el primer caso, Proposición 12.1.4 — Compatibilidad aritmética de la copia entera da

$$
\jmath_{\mathbb Z}^{F}(z)=\nu_F(n),
$$

y Corolario 4.1.10 — Los numerales naturales pertenecen al subcuerpo primo asegura que $\nu_F(n)\in P_F$.

En el segundo caso,

$$
\jmath_{\mathbb Z}^{F}(z)=-\nu_F(n).
$$

Por Proposición 4.1.9 — Minimalidad del subcuerpo primo, $P_F$ es un subcuerpo; por tanto es cerrado bajo opuestos. De nuevo

$$
\jmath_{\mathbb Z}^{F}(z)\in P_F.
$$

Como $z$ era arbitrario, la imagen entera está contenida en $P_F$. ∎

El corolario no afirma que la imagen de $\mathbb Z$ sea ya todo $P_F$. En general no lo es: el subcuerpo primo debe ser también cerrado bajo el inverso de cada elemento no nulo. La etapa que falta consiste precisamente en añadir a la copia entera todas las fracciones determinadas por esos inversos.

Así, la siguiente sección no construirá un nuevo sistema racional. Utilizará el $\mathbb Q$ ya construido en el Capítulo 3 para demostrar que todo cuerpo ordenado contiene una única copia canónica de $\mathbb Q$, y que su imagen es exactamente $P_F$.
