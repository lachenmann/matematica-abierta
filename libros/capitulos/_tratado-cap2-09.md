## 2.9. Orden de los enteros {#sec-ta-2-9}

No definiremos el orden de $\mathbb Z$ recurriendo a una noción previa de «número positivo» no construida. Utilizaremos la incrustación de $\mathbb N$ y la estructura aditiva ya demostrada.

La idea es la misma que en los naturales:

$$
m\leq n
\iff
\exists k\in\mathbb N\;(n=m+k).
$$

En $\mathbb Z$ diremos que $x$ precede a $y$ cuando la diferencia de $y$ respecto de $x$ es la imagen de algún natural.

### Definición 2.9.1 — Relación de orden entera {#ta-orden-entero-def}

*Glosario: [orden entero](../otros/tratado-de-analisis-glosario.md#gl-orden-entero)*

Para $x,y\in\mathbb Z$ definimos

$$
\boxed{
x\leq_{\mathbb Z} y
\iff
\exists n\in\mathbb N\;
\bigl(y=x+\iota(n)\bigr).
}
$$

La relación acaba de ser definida; todavía debemos demostrar que es un orden total.

### Proposición 2.9.2 — Criterio de orden mediante representantes {#ta-orden-entero-representantes}

Para $a,b,c,d\in\mathbb N$,

$$
\boxed{
[(a,b)]\leq_{\mathbb Z}[(c,d)]
\iff
a+d\leq c+b.
}
$$

El orden del miembro derecho es el orden ya construido en $\mathbb N$.

**Demostración.**  
Supongamos primero

$$
[(a,b)]\leq_{\mathbb Z}[(c,d)].
$$

Por definición existe $n\in\mathbb N$ tal que

$$
[(c,d)]=[(a,b)]+\iota(n).
$$

Por la fórmula de la suma y la definición de $\iota$,

$$
[(c,d)]=[(a+n,b)].
$$

El criterio de igualdad de clases da

$$
c+b=(a+n)+d.
$$

Reordenando,

$$
c+b=(a+d)+n.
$$

Por definición del orden natural,

$$
a+d\leq c+b.
$$

Recíprocamente, supongamos

$$
a+d\leq c+b.
$$

Existe entonces $n\in\mathbb N$ tal que

$$
c+b=(a+d)+n.
$$

Por asociatividad y conmutatividad,

$$
c+b=(a+n)+d.
$$

El criterio de igualdad de clases produce

$$
[(c,d)]=[(a+n,b)].
$$

Pero

$$
[(a+n,b)]
=
[(a,b)]+[(n,0)]
=
[(a,b)]+\iota(n).
$$

Por definición,

$$
[(a,b)]\leq_{\mathbb Z}[(c,d)].
$$

∎

Esta caracterización muestra, en particular, que el orden es independiente de los representantes. No se ha definido una condición sobre pares para luego confiar en que descienda al cociente: el orden se definió directamente en $\mathbb Z$, y ahora hemos demostrado el criterio equivalente sobre cualquier representación.

> **Nota de decidibilidad.** Para representantes $[(a,b)]$ y $[(c,d)]$, tanto la igualdad como el orden entero se reducen a comparaciones de naturales:
>
> $$
> [(a,b)]=[(c,d)]\iff a+d=b+c,
> $$
>
> $$
> [(a,b)]\leq_{\mathbb Z}[(c,d)]\iff a+d\leq c+b.
> $$
>
> Como igualdad y orden en $\mathbb N$ son decidibles por la Proposición 1.6.7, igualdad y orden en $\mathbb Z$ son decidibles sobre estos nombres finitos.

### Teorema 2.9.3 — El orden entero es total {#ta-orden-entero-total}

La relación $\leq_{\mathbb Z}$ es un [orden total](../otros/tratado-de-analisis-glosario.md#gl-orden-total) sobre $\mathbb Z$.

**Demostración.**  
**Reflexividad.** Como

$$
\iota(0)=0_{\mathbb Z},
$$

para todo $x\in\mathbb Z$,

$$
x=x+0_{\mathbb Z}=x+\iota(0).
$$

Luego $x\leq_{\mathbb Z}x$.

**Transitividad.** Si $x\leq_{\mathbb Z}y$ y $y\leq_{\mathbb Z}z$, existen $m,n\in\mathbb N$ tales que

$$
y=x+\iota(m),
\qquad
z=y+\iota(n).
$$

Entonces

$$
z=x+\iota(m)+\iota(n)=x+\iota(m+n),
$$

porque $\iota$ preserva la suma. Así $x\leq_{\mathbb Z}z$.

**Antisimetría.** Supongamos $x\leq_{\mathbb Z}y$ y $y\leq_{\mathbb Z}x$. Existen $m,n\in\mathbb N$ con

$$
y=x+\iota(m),
\qquad
x=y+\iota(n).
$$

Sustituyendo,

$$
x=x+\iota(m+n).
$$

Sumando $-x$ y usando la inyectividad de $\iota$,

$$
m+n=0.
$$

La suma nula en $\mathbb N$ da $m=n=0$, y por tanto $y=x$.

**Totalidad.** Sean

$$
x=[(a,b)],
\qquad
y=[(c,d)].
$$

Por totalidad del orden natural, al menos una de

$$
a+d\leq c+b,
\qquad
c+b\leq a+d
$$

se cumple. Por la Proposición 2.9.2, esto equivale a $x\leq_{\mathbb Z}y$ o $y\leq_{\mathbb Z}x$. ∎

A partir de este teorema, $<_{\mathbb Z}$ es el [orden estricto asociado](../otros/tratado-de-analisis-glosario.md#gl-orden-estricto) a $\leq_{\mathbb Z}$.

### Proposición 2.9.4 — Compatibilidad del orden con suma y producto {#ta-orden-entero-compatible}

Para $x,y,z\in\mathbb Z$:

1. si $x\leq_{\mathbb Z}y$, entonces
   $$
   x+z\leq_{\mathbb Z}y+z;
   $$
2. si $x\leq_{\mathbb Z}y$ y $0_{\mathbb Z}\leq_{\mathbb Z}z$, entonces
   $$
   xz\leq_{\mathbb Z}yz.
   $$

**Demostración.**  
Si $x\leq_{\mathbb Z}y$, existe $n\in\mathbb N$ tal que

$$
y=x+\iota(n).
$$

Entonces

$$
y+z=(x+\iota(n))+z=(x+z)+\iota(n),
$$

por asociatividad y conmutatividad. Así $x+z\leq_{\mathbb Z}y+z$.

Supongamos además $0_{\mathbb Z}\leq_{\mathbb Z}z$. Por definición existe $m\in\mathbb N$ tal que

$$
z=0_{\mathbb Z}+\iota(m)=\iota(m).
$$

Por distributividad,

$$
yz=(x+\iota(n))z=xz+\iota(n)z.
$$

Como $z=\iota(m)$ y $\iota$ preserva productos,

$$
\iota(n)z=\iota(nm).
$$

Luego $yz=xz+\iota(nm)$ y, por definición, $xz\leq_{\mathbb Z}yz$. ∎

### Proposición 2.9.5 — La incrustación preserva y refleja el orden {#ta-incrustacion-preserva-orden}

Para $m,n\in\mathbb N$,

$$
\boxed{
m\leq n
\iff
\iota(m)\leq_{\mathbb Z}\iota(n).
}
$$

**Demostración.**  
Si $m\leq n$, existe $k\in\mathbb N$ tal que $n=m+k$. Aplicando $\iota$ y usando preservación de suma,

$$
\iota(n)=\iota(m)+\iota(k),
$$

de modo que $\iota(m)\leq_{\mathbb Z}\iota(n)$.

Recíprocamente, si $\iota(m)\leq_{\mathbb Z}\iota(n)$, existe $k\in\mathbb N$ tal que

$$
\iota(n)=\iota(m)+\iota(k)=\iota(m+k).
$$

La inyectividad de $\iota$ da $n=m+k$, y por definición del orden natural, $m\leq n$. ∎

La incrustación canónica preserva ahora $0$, $1$, suma, producto y orden. Éste es el sentido preciso en que la aritmética natural vive dentro de la aritmética entera.

### Corolario 2.9.6 — Tricotomía decidible en $\mathbb Z$ {#ta-tricotomia-enteros}

*Glosario: [tricotomía](../otros/tratado-de-analisis-glosario.md#gl-tricotomia)*

Para cualesquiera $x,y\in\mathbb Z$, exactamente una de las siguientes alternativas es verdadera:

$$
x<_{\mathbb Z}y,
\qquad
x=y,
\qquad
y<_{\mathbb Z}x.
$$

Además, la alternativa correcta es decidible a partir de representantes finitos de $x$ e $y$.

**Demostración.**  
Escribamos

$$
x=[(a,b)],
\qquad
y=[(c,d)].
$$

La tricotomía decidible de los naturales aplicada a

$$
a+d
\qquad\text{y}\qquad
c+b
$$

determina exactamente una de las relaciones

$$
a+d<c+b,
\qquad
a+d=c+b,
\qquad
c+b<a+d.
$$

Por el criterio de igualdad de clases y la Proposición 2.9.2, estas tres alternativas equivalen respectivamente a

$$
x<_{\mathbb Z}y,
\qquad
x=y,
\qquad
y<_{\mathbb Z}x.
$$

La exclusión mutua se hereda de la tricotomía natural, y el procedimiento es finito porque sólo requiere suma y comparación decidible en $\mathbb N$. ∎

---
