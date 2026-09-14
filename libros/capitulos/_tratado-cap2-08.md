## 2.8. Forma normal con signo y ausencia de divisores de cero {#sec-ta-2-8}

La representación de un entero por un par no es única, pero todo entero puede reducirse a una forma especialmente simple: o bien $[(n,0)]$, o bien $[(0,n)]$. Este resultado convierte la intuición de «positivo o negativo» en un teorema.

### Teorema 2.8.1 — Forma normal con signo {#ta-forma-normal-signo}

*Glosario: [forma normal con signo](../otros/tratado-de-analisis-glosario.md#gl-forma-normal-signo)*

Para todo $z\in\mathbb Z$, exactamente una de las siguientes alternativas es verdadera:

1. $z=0_{\mathbb Z}$;
2. existe un único $n\in\mathbb N$ con $n\neq0$ tal que $z=\iota(n)$;
3. existe un único $n\in\mathbb N$ con $n\neq0$ tal que $z=-\iota(n)$.

**Demostración.**  
Sea

$$
z=[(a,b)].
$$

Por totalidad del orden natural,

$$
b\leq a
\qquad\text{o}\qquad
a\leq b.
$$

Supongamos primero $b\leq a$. Por definición del orden en $\mathbb N$, existe $n\in\mathbb N$ tal que

$$
a=b+n.
$$

Entonces

$$
[(a,b)]=[(n,0)],
$$

porque el criterio de igualdad de clases exige

$$
a+0=b+n,
$$

que es precisamente la igualdad anterior. Por tanto

$$
z=\iota(n).
$$

Si $n=0$, entonces $a=b$ y $z=[(0,0)]=0_{\mathbb Z}$. Si $n\neq0$, obtenemos la segunda alternativa.

Si, en cambio, $a\leq b$, existe $n\in\mathbb N$ tal que

$$
b=a+n.
$$

Entonces

$$
[(a,b)]=[(0,n)].
$$

Pero

$$
-\iota(n)
=
-[(n,0)]
=
[(0,n)],
$$

de modo que

$$
z=-\iota(n).
$$

Nuevamente, $n=0$ produce $z=0_{\mathbb Z}$ y $n\neq0$ produce la tercera alternativa.

Queda demostrar unicidad y exclusión mutua.

Si

$$
\iota(m)=\iota(n),
$$

la inyectividad de $\iota$ da $m=n$. Si

$$
-\iota(m)=-\iota(n),
$$

entonces, usando la definición del opuesto,

$$
[(0,m)]=[(0,n)].
$$

El criterio de igualdad da

$$
0+n=m+0,
$$

y por tanto $m=n$.

Las alternativas no nulas tampoco pueden confundirse con el cero. Si

$$
\iota(n)=0_{\mathbb Z},
$$

entonces $\iota(n)=\iota(0)$ y la inyectividad de $\iota$ da $n=0$. Del mismo modo, si

$$
-\iota(n)=0_{\mathbb Z},
$$

entonces

$$
[(0,n)]=[(0,0)],
$$

y el criterio de igualdad da $n=0$.

Finalmente, si para $m,n\neq0$

$$
\iota(m)=-\iota(n),
$$

entonces

$$
[(m,0)]=[(0,n)].
$$

Por el criterio de igualdad,

$$
m+n=0.
$$

La propiedad de suma nula en $\mathbb N$ obliga a $m=0$ y $n=0$, contradicción. Por tanto las alternativas positiva y negativa no pueden coincidir cuando los índices son no nulos.

Las tres alternativas son, pues, exhaustivas y mutuamente excluyentes. ∎

### Proposición 2.8.2 — $0_{\mathbb Z}\neq1_{\mathbb Z}$ {#ta-cero-uno-enteros-distintos}

Se tiene

$$
0_{\mathbb Z}\neq1_{\mathbb Z}.
$$

**Demostración.**  
Si $[(0,0)]=[(1,0)]$, el criterio de igualdad daría

$$
0+0=0+1,
$$

es decir,

$$
0=1.
$$

Pero $1=S(0)$ y, por las propiedades de Peano demostradas para $\mathbb N$, $0$ no es sucesor de ningún natural. Contradicción. ∎

### Proposición 2.8.3 — Ausencia de divisores de cero {#ta-ausencia-divisores-cero-enteros}

Para $x,y\in\mathbb Z$,

$$
xy=0_{\mathbb Z}
\quad\Longrightarrow\quad
x=0_{\mathbb Z}
\ \text{o}\
y=0_{\mathbb Z}.
$$

**Demostración.**  
Demostraremos la contraposición. Supongamos

$$
x\neq0_{\mathbb Z},
\qquad
y\neq0_{\mathbb Z}.
$$

Por el teorema de forma normal con signo existen $m,n\in\mathbb N$, ambos no nulos, tales que cada uno de $x$ e $y$ es, respectivamente, una de las dos formas

$$
\iota(m)=[(m,0)],
\qquad
-\iota(m)=[(0,m)],
$$

y

$$
\iota(n)=[(n,0)],
\qquad
-\iota(n)=[(0,n)].
$$

Calculamos los cuatro casos directamente con la definición del producto:

$$
[(m,0)][(n,0)]=[(mn,0)]=\iota(mn),
$$

$$
[(m,0)][(0,n)]=[(0,mn)]=-\iota(mn),
$$

$$
[(0,m)][(n,0)]=[(0,mn)]=-\iota(mn),
$$

y

$$
[(0,m)][(0,n)]=[(mn,0)]=\iota(mn).
$$

Por tanto $xy$ es siempre una de las dos clases $\iota(mn)$ o $-\iota(mn)$.

Como $m\neq0$ y $n\neq0$, la propiedad de producto nulo ya demostrada en $\mathbb N$ implica

$$
mn\neq0.
$$

El teorema de forma normal con signo muestra que ni $\iota(mn)$ ni $-\iota(mn)$ es $0_{\mathbb Z}$. Por tanto

$$
xy\neq0_{\mathbb Z}.
$$

La contraposición queda demostrada. ∎

### Teorema 2.8.4 — $\mathbb Z$ es un dominio de integridad {#ta-dominio-integridad-enteros}

El anillo conmutativo $\mathbb Z$ es un **[dominio de integridad](../otros/tratado-de-analisis-glosario.md#gl-dominio-integridad)**.

**Demostración.**  
En §2.6 demostramos que $\mathbb Z$ es un anillo conmutativo con identidad. La Proposición 2.8.2 demuestra $0_{\mathbb Z}\neq1_{\mathbb Z}$ y la Proposición 2.8.3 demuestra la ausencia de divisores de cero. Éstas son exactamente las condiciones fijadas en la convención de dominio de integridad. ∎

---

::: {.callout-note title="Publicación progresiva"}
Con §2.8 queda demostrado que todo entero posee una forma normal con signo y que $\mathbb Z$ no tiene divisores de cero; por tanto, $\mathbb Z$ es un dominio de integridad. La siguiente entrega será **§2.9 — Orden de los enteros**.
:::
