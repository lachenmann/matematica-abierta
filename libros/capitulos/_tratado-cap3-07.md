## 3.7. Orden racional {#sec-ta-3-7}

La fórmula de comparación

$$
\frac ab\leq\frac cd
\quad\Longleftrightarrow\quad
ad\leq bc
$$

es correcta cuando los denominadores $b$ y $d$ son positivos. Sin esa hipótesis, multiplicar cruzadamente puede invertir el sentido del orden. Por eso no introduciremos el orden racional hasta demostrar que toda clase admite representantes con denominador positivo y que la comparación cruzada es independiente de tales representantes.

### Lema 3.7.1 — Representante con denominador positivo {#ta-representante-denominador-positivo}

Para todo $q\in\mathbb Q$ existen $a\in\mathbb Z$ y $n\in\mathbb N$ con $n\neq0$ tales que

$$
q
=
\frac{a}{\iota_{\mathbb N}^{\mathbb Z}(n)}
$$

y

$$
0_{\mathbb Z}
<
\iota_{\mathbb N}^{\mathbb Z}(n).
$$

**Demostración.**  
Tomemos una representación

$$
q=\frac ab,
\qquad
b\neq0_{\mathbb Z}.
$$

Por la forma normal con signo de los enteros demostrada en el Capítulo 2, existe un único $n\in\mathbb N$, $n\neq0$, tal que

$$
b=\iota(n)
\qquad\text{o}\qquad
b=-\iota(n).
$$

Como $0\leq n$ en $\mathbb N$ y $n\neq0$, tenemos $0<n$. La [incrustación natural en los enteros](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-incrustacion-preserva-orden) preserva y refleja el orden, de modo que

$$
0_{\mathbb Z}<\iota(n).
$$

Si $b=\iota(n)$, ya terminamos. Si $b=-\iota(n)$, entonces

$$
\frac ab
=
\frac{-a}{-b}
=
\frac{-a}{\iota(n)},
$$

porque

$$
a(-b)=b(-a)
$$

en el anillo conmutativo $\mathbb Z$. Así toda clase racional admite una representación con denominador positivo. ∎

### Lema 3.7.2 — Invariancia de la comparación cruzada {#ta-invariancia-comparacion-cruzada}

Supongamos

$$
\frac ab=\frac{a'}{b'},
\qquad
\frac cd=\frac{c'}{d'},
$$

con

$$
0<b,\quad0<b',\quad0<d,\quad0<d'
$$

en $\mathbb Z$. Entonces

$$
\boxed{
ad\leq bc
\iff
a'd'\leq b'c'.
}
$$

**Demostración.**  
Las igualdades de fracciones dan

$$
ab'=ba',
\qquad
cd'=dc'.
$$

Supongamos $ad\leq bc$. Como $b'd'>0$ por el [producto de enteros positivos](#ta-producto-enteros-positivos), el [escalamiento por un entero positivo](#ta-escalamiento-entero-positivo) permite multiplicar la desigualdad por $b'd'$ sin alterar su sentido:

$$
ad\,b'd'
\leq
bc\,b'd'.
$$

Usando las dos igualdades anteriores y reordenando factores,

$$
bd(a'd')
\leq
bd(b'c').
$$

Como $bd>0$, aplicamos la implicación inversa del mismo lema de escalamiento y obtenemos

$$
a'd'\leq b'c'.
$$

La recíproca se obtiene intercambiando los pares primados y no primados. ∎

### Definición 3.7.3 — Orden racional {#ta-orden-racional}

*Glosario: [orden racional](../otros/tratado-de-analisis-glosario.md#gl-orden-racional)*

Para $q,r\in\mathbb Q$ definimos

$$
\boxed{
q\leq_{\mathbb Q}r
}
$$

si existen representaciones

$$
q=\frac ab,
\qquad
r=\frac cd,
$$

con $0<b$ y $0<d$, tales que

$$
ad\leq_{\mathbb Z}bc.
$$

El lema anterior garantiza que la condición no depende de cuáles representantes con denominador positivo se utilicen.

### Proposición 3.7.4 — Criterio práctico de orden {#ta-criterio-practico-orden-racional}

Sean

$$
q=\frac ab,
\qquad
r=\frac cd
$$

representaciones con $0<b$ y $0<d$. Entonces

$$
\boxed{
q\leq_{\mathbb Q}r
\iff
ad\leq_{\mathbb Z}bc.
}
$$

**Demostración.**  
La implicación de derecha a izquierda es la definición. Para la recíproca, si $q\leq_{\mathbb Q}r$, la definición proporciona alguna pareja de representantes positivos para la cual vale la desigualdad cruzada. El Lema 3.7.2 transporta esa desigualdad a las representaciones positivas dadas. ∎

### Teorema 3.7.5 — El orden racional es total {#ta-orden-racional-total}

La relación $\leq_{\mathbb Q}$ es un orden total sobre $\mathbb Q$.

**Demostración.**  
Por el Lema 3.7.1, todo racional admite representación con denominador positivo.

**Reflexividad.** Si $q=a/b$ con $b>0$, entonces

$$
ab=ba,
$$

luego $ab\leq ba$ y $q\leq_{\mathbb Q}q$.

**Antisimetría.** Sean

$$
q=\frac ab,
\qquad
r=\frac cd,
\qquad
b,d>0,
$$

y supongamos $q\leq r$ y $r\leq q$. Por la Proposición 3.7.4,

$$
ad\leq bc
\qquad\text{y}\qquad
bc\leq ad.
$$

La antisimetría en $\mathbb Z$ da $ad=bc$, y el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales) implica $q=r$.

**Transitividad.** Sean

$$
q=\frac ab,\qquad
r=\frac cd,\qquad
s=\frac ef
$$

con $b,d,f>0$, y supongamos $q\leq r$ y $r\leq s$. Entonces

$$
ad\leq bc,
\qquad
cf\leq de.
$$

Como $f>0$, el Lema 3.1.3 da

$$
adf\leq bcf.
$$

Como $b>0$,

$$
bcf\leq bde.
$$

Por transitividad,

$$
adf\leq bde.
$$

Reordenando,

$$
d(af)\leq d(be).
$$

Como $d>0$, el Lema 3.1.3 permite cancelar el factor positivo:

$$
af\leq be.
$$

Por la Proposición 3.7.4, $q\leq s$.

**Totalidad.** Para representaciones positivas $q=a/b$ y $r=c/d$, la totalidad del orden entero aplicada a $ad$ y $bc$ da

$$
ad\leq bc
\qquad\text{o}\qquad
bc\leq ad.
$$

Por la Proposición 3.7.4, esto equivale a

$$
q\leq r
\qquad\text{o}\qquad
r\leq q.
$$

Así $\leq_{\mathbb Q}$ es reflexivo, antisimétrico, transitivo y total. ∎

Desde ahora, $<_{\mathbb Q}$ denota el orden estricto asociado a $\leq_{\mathbb Q}$.

### Corolario 3.7.6 — Criterio estricto de comparación cruzada {#ta-criterio-estricto-orden-racional}

Si $b,d>0$ en $\mathbb Z$, entonces

$$
\boxed{
\frac ab<_{\mathbb Q}\frac cd
\iff
ad<_{\mathbb Z}bc.
}
$$

**Demostración.**  
Por definición del orden estricto,

$$
\frac ab<\frac cd
$$

significa simultáneamente

$$
\frac ab\leq\frac cd
\qquad\text{y}\qquad
\frac ab\neq\frac cd.
$$

Por la Proposición 3.7.4, la primera condición equivale a $ad\leq bc$; por el criterio de igualdad racional, la segunda equivale a $ad\neq bc$. Juntas son exactamente

$$
ad<bc
$$

en el orden estricto asociado de $\mathbb Z$. La recíproca es la misma cadena de equivalencias leída de derecha a izquierda. ∎

### Proposición 3.7.7 — Compatibilidad del orden con las operaciones {#ta-orden-racional-compatible-operaciones}

Para $x,y,z\in\mathbb Q$:

1. si $x\leq y$, entonces
   $$
   x+z\leq y+z;
   $$
2. si $x\leq y$ y $0_{\mathbb Q}\leq z$, entonces
   $$
   xz\leq yz.
   $$

**Demostración.**  
Escribamos

$$
x=\frac ab,\qquad
y=\frac cd,\qquad
z=\frac ef
$$

con $b,d,f>0$. La hipótesis $x\leq y$ equivale a

$$
ad\leq bc.
$$

Para la suma,

$$
x+z=\frac{af+be}{bf},
\qquad
y+z=\frac{cf+de}{df}.
$$

Los denominadores son positivos. Como $f^2>0$, de $ad\leq bc$ obtenemos

$$
adf^2\leq bcf^2.
$$

Sumando $bdef$ a ambos miembros,

$$
adf^2+bdef
\leq
bcf^2+bdef.
$$

Esto es, tras factorizar,

$$
(af+be)(df)
\leq
(bf)(cf+de),
$$

y por la Proposición 3.7.4 concluimos

$$
x+z\leq y+z.
$$

Supongamos además $0_{\mathbb Q}\leq z$. Como $0_{\mathbb Q}=0/1$ y $f>0$, el criterio de orden da

$$
0\leq e.
$$

Como $f>0$, también $0\leq f$; por la compatibilidad multiplicativa del orden entero,

$$
0\leq ef.
$$

Multiplicando ahora $ad\leq bc$ por el entero no negativo $ef$ obtenemos

$$
adef\leq bcef.
$$

Pero

$$
xz=\frac{ae}{bf},
\qquad
yz=\frac{ce}{df},
$$

y la desigualdad anterior es precisamente

$$
(ae)(df)\leq(bf)(ce).
$$

Luego, por la Proposición 3.7.4,

$$
xz\leq yz.
$$

∎

### Proposición 3.7.8 — La incrustación $\mathbb Z\to\mathbb Q$ preserva y refleja el orden {#ta-incrustacion-zq-preserva-refleja-orden}

Para $a,c\in\mathbb Z$,

$$
\boxed{
a\leq_{\mathbb Z}c
\iff
\jmath(a)\leq_{\mathbb Q}\jmath(c).
}
$$

**Demostración.**  
El entero $1_{\mathbb Z}$ es positivo. En $\mathbb N$ tenemos $0<1$, y la incrustación $\iota:\mathbb N\to\mathbb Z$ preserva y refleja el orden; por tanto

$$
0_{\mathbb Z}<1_{\mathbb Z}.
$$

Las representaciones

$$
\jmath(a)=\frac a1,
\qquad
\jmath(c)=\frac c1
$$

tienen así denominador positivo. La Proposición 3.7.4 da

$$
\jmath(a)\leq\jmath(c)
\iff
a\cdot1\leq1\cdot c
\iff
a\leq c.
$$

∎

### Lema 3.7.9 — Positividad y escalamiento estricto en $\mathbb Q$ {#ta-positividad-escalamiento-estricto-q}

En $\mathbb Q$:

1. si $0<x$ y $0<y$, entonces $0<xy$;
2. si $0<x$, entonces $0<x^{-1}$;
3. si $x<y$ y $0<z$, entonces $xz<yz$.

**Demostración.**  
Para (1), de $0\leq x$ y $0\leq y$, la Proposición 3.7.7 da $0\leq xy$. Si $xy=0$, el [Corolario 3.6.9](#ta-sin-divisores-cero-racionales) implicaría $x=0$ o $y=0$, contradicción. Luego $0<xy$.

Para (2), sea $x>0$. El inverso $x^{-1}$ no es cero, porque

$$
xx^{-1}=1_{\mathbb Q}\neq0_{\mathbb Q}.
$$

Si no fuera positivo, la tricotomía del orden total daría $x^{-1}<0$. En particular,

$$
x^{-1}\leq0.
$$

Como $0\leq x$, la compatibilidad multiplicativa aplicada a $x^{-1}\leq0$ produce

$$
x^{-1}x\leq0_{\mathbb Q}x.
$$

El miembro izquierdo es $1_{\mathbb Q}$. Además, por distributividad y cancelación aditiva,

$$
0_{\mathbb Q}x=0_{\mathbb Q},
$$

de modo que

$$
1_{\mathbb Q}\leq0_{\mathbb Q}.
$$

Por la Proposición 3.7.8 y $0_{\mathbb Z}<1_{\mathbb Z}$ obtenemos, en cambio,

$$
0_{\mathbb Q}<1_{\mathbb Q},
$$

contradicción. Por tanto

$$
0<x^{-1}.
$$

Para (3), la Proposición 3.7.7 da $xz\leq yz$. Si hubiera igualdad, entonces

$$
(y-x)z=0_{\mathbb Q}.
$$

Como $x<y$, tenemos $y-x\neq0_{\mathbb Q}$; además $z\neq0_{\mathbb Q}$. Esto contradice la ausencia de divisores de cero. Por tanto $xz\neq yz$, y así

$$
xz<yz.
$$

∎

---
