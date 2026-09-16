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

Aplicamos la [tricotomía decidible de los naturales](tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-tricotomia-decidible-naturales) a $a$ y $b$.

**Caso $a=b$.** El criterio de igualdad de clases da

$$
[(a,b)]=[(0,0)]=0_{\mathbb Z}.
$$

**Caso $b<a$.** Entonces $b\leq a$, de modo que existe $n\in\mathbb N$ con

$$
a=b+n.
$$

Además $n\neq0$: si $n=0$, tendríamos $a=b$, contradicción. El criterio de igualdad de clases da

$$
[(a,b)]=[(n,0)]=\iota(n).
$$

**Caso $a<b$.** Existe $n\in\mathbb N$ con

$$
b=a+n,
$$

y nuevamente $n\neq0$. Entonces

$$
[(a,b)]=[(0,n)]=-\iota(n).
$$

Queda la unicidad dentro de las dos formas no nulas y su exclusión mutua. Si $\iota(m)=\iota(n)$, la inyectividad de $\iota$ da $m=n$. Si $-\iota(m)=-\iota(n)$, el criterio de igualdad de clases aplicado a $[(0,m)]$ y $[(0,n)]$ da $m=n$.

Si $\iota(n)=0_{\mathbb Z}$ o $-\iota(n)=0_{\mathbb Z}$, el mismo criterio fuerza $n=0$. Finalmente, si $m,n\neq0$ y

$$
\iota(m)=-\iota(n),
$$

entonces $[(m,0)]=[(0,n)]$, y por tanto $m+n=0$. La propiedad de suma nula en $\mathbb N$ fuerza $m=n=0$, contradicción.

Como la tricotomía de $a,b$ es decidible y exhaustiva, las tres formas anteriores son exhaustivas y mutuamente excluyentes. ∎

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

Pero $1=S(0)$ y las propiedades de Peano afirman que $0$ no es sucesor. Contradicción. ∎

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
Supongamos $xy=0_{\mathbb Z}$ y apliquemos el Teorema 2.8.1 a $x$ y a $y$.

Si alguna de las dos formas normales es $0_{\mathbb Z}$, la conclusión es inmediata. Quedan sólo los cuatro casos en que existen $m,n\in\mathbb N$, ambos no nulos, y

$$
x\in\{\iota(m),-\iota(m)\},
\qquad
y\in\{\iota(n),-\iota(n)\}.
$$

Por la definición del producto entero, en esos cuatro casos $xy$ es respectivamente una de las clases

$$
\iota(mn)
\qquad\text{o}\qquad
-\iota(mn).
$$

Como $m\neq0$ y $n\neq0$, el producto nulo en $\mathbb N$ da $mn\neq0$. La forma normal implica entonces que ni $\iota(mn)$ ni $-\iota(mn)$ es $0_{\mathbb Z}$, contradiciendo $xy=0_{\mathbb Z}$.

Por tanto los cuatro casos no nulos son imposibles y necesariamente

$$
x=0_{\mathbb Z}
\quad\text{o}\quad
y=0_{\mathbb Z}.
$$

∎

### Teorema 2.8.4 — $\mathbb Z$ es un dominio de integridad {#ta-dominio-integridad-enteros}

El anillo conmutativo $\mathbb Z$ es un **[dominio de integridad](../otros/tratado-de-analisis-glosario.md#gl-dominio-integridad)**.

**Demostración.**  
En §2.6 demostramos que $\mathbb Z$ es un anillo conmutativo con identidad. La Proposición 2.8.2 demuestra $0_{\mathbb Z}\neq1_{\mathbb Z}$ y la Proposición 2.8.3 demuestra la ausencia de divisores de cero. Éstas son exactamente las condiciones fijadas en la convención de dominio de integridad. ∎

---
