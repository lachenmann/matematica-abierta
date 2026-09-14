## 1.6. Orden natural {#sec-ta-1-6}

Una vez disponible la suma podemos expresar aritméticamente la idea de que un natural no supera a otro: $m$ está antes que $n$ si a $m$ puede añadírsele algún natural para llegar a $n$. Esta caracterización tiene la ventaja de no presuponer ningún orden previo sobre $\mathbb N$.

Definiremos, pues, el orden mediante **alcanzabilidad aditiva**. Después habrá que demostrar que la relación obtenida es realmente un orden total y, sólo entonces, compararla con la estructura conjuntista de los ordinales de von Neumann.

### Definición 1.6.1 — Orden aritmético {#ta-orden-natural}

*Glosario: [orden natural](../otros/tratado-de-analisis-glosario.md#gl-orden-natural) · [alcanzabilidad aditiva](../otros/tratado-de-analisis-glosario.md#gl-alcanzabilidad-aditiva)*

Para $m,n\in\mathbb N$, definimos

$$
\boxed{m\leq n\iff\exists k\in\mathbb N\;(n=m+k).}
$$

El orden estricto conserva la convención global

$$
m<n\iff(m\leq n\text{ y }m\neq n).
$$

### Proposición 1.6.2 — Reflexividad y transitividad {#ta-orden-natural-reflexividad-transitividad}

La relación $\leq$ es reflexiva y transitiva.

**Demostración.**  
$m=m+0$, luego $m\leq m$. Si $n=m+a$ y $p=n+b$, entonces

$$
p=(m+a)+b=m+(a+b),
$$

así que $m\leq p$. ∎

### Proposición 1.6.3 — Antisimetría {#ta-orden-natural-antisimetria}

Si $m\leq n$ y $n\leq m$, entonces $m=n$.

**Demostración.**  
Sean $n=m+a$ y $m=n+b$. Entonces

$$
m=m+(a+b)=m+0.
$$

Por conmutatividad y cancelación, $a+b=0$; por la Proposición 1.4.7 — Suma nula, $a=b=0$, y $n=m$. ∎

### Teorema 1.6.4 — Totalidad {#ta-totalidad-orden-natural}

*Glosario: [totalidad (conexidad)](../otros/tratado-de-analisis-glosario.md#gl-totalidad)*

Para cualesquiera $m,n\in\mathbb N$,

$$
m\leq n\quad\text{o}\quad n\leq m.
$$

**Demostración.**  
Inducimos sobre $n$ la comparabilidad con todo $m$. Para $n=0$, $m=0+m$, luego $0\leq m$.

Supongamos la comparabilidad con $n$. Si $m\leq n$, $n=m+k$ y

$$
S(n)=S(m+k)=m+S(k),
$$

por lo que $m\leq S(n)$.

Si $n\leq m$, escribimos $m=n+k$. Si $k=0$, entonces $m=n$ y $m\leq S(n)$ porque $S(n)=n+1$. Si $k\neq0$, el Teorema 1.2.7 — Predecesor de todo natural no nulo da $k=S(r)$, y

$$
m=n+S(r)=S(n+r)=S(n)+r,
$$

por el Lema 1.4.3 — Sucesor en el primer argumento; así $S(n)\leq m$. ∎

### Teorema 1.6.5 — Orden total {#ta-orden-natural-total}

*Glosario: [orden total](../otros/tratado-de-analisis-glosario.md#gl-orden-total)*

La relación $\leq$ es un orden total sobre $\mathbb N$.

**Demostración.**  
La reflexividad y la transitividad son la Proposición 1.6.2; la antisimetría es la Proposición 1.6.3; la totalidad es el Teorema 1.6.4. Son exactamente las condiciones de la definición de orden total establecida en el Capítulo 0. ∎

### Proposición 1.6.6 — Compatibilidad con la suma {#ta-orden-natural-compatible-suma}

Si $a\leq b$, entonces $a+c\leq b+c$. Si $a<b$, entonces $a+c<b+c$.

**Demostración.**  
Si $b=a+k$, entonces

$$
b+c=(a+k)+c=(a+c)+k.
$$

Si además $a<b$ y $a+c=b+c$, la Proposición 1.4.6 — Cancelación aditiva daría $a=b$. ∎

### Proposición 1.6.7 — Compatibilidad con el producto {#ta-orden-natural-compatible-producto}

Si $a\leq b$, entonces $ac\leq bc$ para todo $c$. Si $a<b$ y $c\neq0$, entonces $ac<bc$.

**Demostración.**  
Si $b=a+k$, entonces

$$
bc=(a+k)c=ac+kc,
$$

luego $ac\leq bc$. Si $a<b$, el testigo $k$ no es $0$; si además $c\neq0$, la Proposición 1.5.9 — Producto nulo garantiza $kc\neq0$. La igualdad $ac=bc=ac+kc$ contradice la Proposición 1.4.6 — Cancelación aditiva. ∎

Hasta aquí el orden ha sido puramente aritmético: se definió en términos de suma. Pero cada natural es también un conjunto. Podemos preguntar ahora si ambas estructuras —la aritmética y la conjuntista— están relacionadas. La respuesta será más fuerte que una mera compatibilidad: son dos expresiones del mismo orden.

### Proposición 1.6.8 — El orden coincide con la inclusión {#ta-orden-natural-inclusion}

Para $m,n\in\mathbb N$,

$$
\boxed{m\leq n\iff m\subseteq n.}
$$

**Demostración.**  
Si $m\leq n$, escribimos $n=m+k$ e inducimos sobre $k$ para demostrar $m\subseteq m+k$: el caso $0$ es igualdad y, si $m\subseteq m+k$, entonces

$$
m\subseteq m+k\subseteq S(m+k)=m+S(k).
$$

Recíprocamente, supongamos $m\subseteq n$. Por totalidad, $m\leq n$ o $n\leq m$. En el segundo caso, la implicación ya demostrada da $n\subseteq m$; por doble inclusión $m=n$, y entonces $m\leq n$. ∎

### Corolario 1.6.9 — Inclusión propia y orden estricto {#ta-orden-estricto-inclusion-propia}

Para $m,n\in\mathbb N$,

$$
m<n\iff m\subsetneq n.
$$

**Demostración.**  
Se combinan la definición de $<$ con la Proposición 1.6.8. ∎

### Lema 1.6.10 — Incremento positivo {#ta-incremento-positivo}

Para $m,k\in\mathbb N$,

$$
m\in m+S(k).
$$

**Demostración.**  
Inducción sobre $k$. Para $0$, $m+S(0)=S(m)$ contiene a $m$. Si $m\in m+S(k)$, entonces también

$$
m\in S(m+S(k))=m+S(S(k)).
$$

∎

La inclusión propia traduce ya el orden estricto. En los naturales de von Neumann podemos afinar todavía más: como cada natural es el conjunto de sus predecesores, «ser estrictamente menor» deberá equivaler a **pertenecer** al otro natural.

### Teorema 1.6.11 — Orden estricto y pertenencia {#ta-orden-estricto-pertenencia}

*Glosario: [orden estricto](../otros/tratado-de-analisis-glosario.md#gl-orden-estricto)*

Para $m,n\in\mathbb N$,

$$
\boxed{m<n\iff m\in n.}
$$

**Demostración.**  
Si $m\in n$, la transitividad de $n$ da $m\subseteq n$, y $m\neq n$ porque $n\notin n$; luego $m\subsetneq n$ y el Corolario 1.6.9 da $m<n$.

Si $m<n$, escribimos $n=m+k$. Como $m\neq n$, $k\neq0$, y por el Teorema 1.2.7 — Predecesor de todo natural no nulo, $k=S(r)$. Entonces

$$
n=m+S(r),
$$

y el Lema 1.6.10 da $m\in n$. ∎

**Interpretación estructural.** Hemos llegado a una coincidencia característica de la representación de von Neumann:

$$
m<n\iff m\in n,
\qquad
m\leq n\iff m\subseteq n.
$$

El orden que construimos aritméticamente mediante la suma estaba ya inscrito en la arquitectura conjuntista de $\omega$. No son dos órdenes diferentes que casualmente sean compatibles: sobre $\mathbb N$ son la misma estructura vista desde dos lenguajes.

### Teorema 1.6.12 — Principio de buen orden {#ta-principio-buen-orden-naturales}

*Glosario: [buen orden](../otros/tratado-de-analisis-glosario.md#gl-buen-orden)*

Todo subconjunto no vacío $A\subseteq\mathbb N$ tiene un elemento mínimo.

**Demostración.**  
Primero inducimos sobre $n$ la afirmación: «todo subconjunto no vacío de $S(n)$ tiene mínimo».

Para $n=0$, $S(0)=\{0\}$; su único subconjunto no vacío es $\{0\}$, cuyo mínimo es $0$. Supongamos el resultado para $S(n)$ y sea $B\subseteq S(S(n))$ no vacío. Si $B\cap S(n)$ es no vacío, tiene mínimo $b$ por hipótesis inductiva; cualquier elemento adicional de $B$ sólo puede ser $S(n)$, y como $b\in S(n)$, el Teorema 1.6.11 da $b<S(n)$. Si $B\cap S(n)=\varnothing$, necesariamente $B=\{S(n)\}$.

Ahora sea $A\subseteq\mathbb N$ no vacío y tome un testigo $n\in A$. El conjunto $A\cap S(n)$ es no vacío porque $n\in S(n)$, y por lo anterior tiene mínimo $b$. Para $x\in A$, la totalidad da $x\leq n$ o $n\leq x$. En el primer caso $x\in S(n)$, así $b\leq x$; en el segundo, $b\leq n\leq x$. Por tanto $b$ es mínimo de $A$. ∎

### Corolario 1.6.13 — Inducción fuerte {#ta-induccion-fuerte}

*Glosario: [inducción fuerte](../otros/tratado-de-analisis-glosario.md#gl-induccion-fuerte)*

Si para todo $n\in\mathbb N$

$$
[\forall m<n,\ P(m)]\Rightarrow P(n),
$$

entonces $P(n)$ vale para todo $n\in\mathbb N$.

**Demostración.**  
Si el conjunto $C=\{n\in\mathbb N:\neg P(n)\}$ fuera no vacío, tendría un mínimo $c$. Todo $m<c$ estaría fuera de $C$, luego satisfaría $P(m)$; la hipótesis daría $P(c)$, contradicción. ∎
