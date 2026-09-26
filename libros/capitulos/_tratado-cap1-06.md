## 1.6. Orden natural {#sec-ta-1-6}

Una vez disponible la suma podemos expresar aritméticamente la idea de que un natural no supera a otro: $m$ está antes que $n$ si a $m$ puede añadírsele algún natural para llegar a $n$. Esta caracterización tiene la ventaja de no presuponer ningún orden previo sobre $\mathbb N$.

Definiremos, pues, el orden mediante alcanzabilidad aditiva. Después habrá que demostrar que la relación obtenida es realmente un orden total y, sólo entonces, compararla con la estructura conjuntista de los ordinales de von Neumann.

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
Demostramos por inducción sobre $m$ que todo $n$ es comparable con $m$.

Para $m=0$, tenemos $n=0+n$, luego $0\leq n$.

Supongamos que todo $n$ es comparable con $m$ y fijemos $n$. Hacemos una segunda inducción sobre $n$.

Si $n=0$, entonces $0\leq S(m)$.

Supongamos ahora la comparación decidida para $n$ y consideremos $S(n)$. Por la hipótesis exterior aplicada a $n$, tenemos

$$
m\leq n
\quad\text{o}\quad
n\leq m.
$$

En el primer caso, existe $k$ con $n=m+k$, y por el Lema 1.4.3,

$$
S(n)=S(m+k)=S(m)+k,
$$

así que $S(m)\leq S(n)$.

En el segundo caso existe $k$ con $m=n+k$, y nuevamente

$$
S(m)=S(n+k)=S(n)+k,
$$

por lo que $S(n)\leq S(m)$.

Así todo $S(n)$ es comparable con $S(m)$. La inducción interior prueba que todo natural es comparable con $S(m)$; la inducción exterior concluye la totalidad para todos $m,n$. ∎

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

Si además $a<b$ y $a+c=b+c$, la cancelación aditiva daría $a=b$. ∎

### Proposición 1.6.7 — Tricotomía decidible de los naturales {#ta-tricotomia-decidible-naturales}

*Glosario: [tricotomía](../otros/tratado-de-analisis-glosario.md#gl-tricotomia)*

Para cualesquiera $m,n\in\mathbb N$, exactamente una de las relaciones

$$
m<n,
\qquad
m=n,
\qquad
n<m
$$

se cumple. Además, la alternativa correcta se determina mediante un procedimiento recursivo finito sobre los dos naturales.

**Demostración.**  
Procedemos por inducción exterior sobre $m$ y, en el paso sucesor, por inducción interior sobre $n$.

Si $m=0$, inducimos sobre $n$. Para $n=0$ vale la igualdad. En el paso $n=S(k)$, tenemos $0\leq S(k)$ y $0\neq S(k)$ porque el cero no es sucesor; por la definición del orden estricto, $0<S(k)$. Así la clasificación está decidida para todo $n$.

Supongamos ahora que la tricotomía está decidida para $m$ frente a todo natural y consideremos $S(m)$. Inducimos nuevamente sobre $n$. Para $n=0$, el argumento anterior da $0<S(m)$, es decir, $n<S(m)$.

En el paso $n=S(k)$, por la hipótesis exterior exactamente una de

$$
m<k,
\qquad
m=k,
\qquad
k<m
$$

se cumple. Si $m=k$, la inyectividad del sucesor da $S(m)=S(k)$. Si $m<k$, la compatibilidad estricta de la suma aplicada a $1$ da

$$
S(m)=m+1<k+1=S(k).
$$

El caso $k<m$ es simétrico. La exclusión mutua se preserva por la inyectividad del sucesor y por la antisimetría de $\leq$ junto con la definición del orden estricto.

El argumento describe simultáneamente un procedimiento recursivo: se eliminan sucesores de ambos datos hasta alcanzar uno de los casos base. Por tanto igualdad y orden en $\mathbb N$ son decidibles. ∎

> **Nota fundacional.** La totalidad del Teorema 1.6.4 es un enunciado de comparabilidad. Esta proposición registra algo más fuerte para la presentación concreta de von Neumann: la comparación puede decidirse por recursión finita.

### Proposición 1.6.8 — Compatibilidad con el producto {#ta-orden-natural-compatible-producto}

Si $a\leq b$, entonces $ac\leq bc$ para todo $c$. Si $a<b$ y $c\neq0$, entonces $ac<bc$.

**Demostración.**  
Si $b=a+k$, entonces

$$
bc=(a+k)c=ac+kc,
$$

luego $ac\leq bc$. Si $a<b$, el testigo $k$ no es $0$; si además $c\neq0$, la Proposición 1.5.9 — Producto nulo garantiza $kc\neq0$. La igualdad $ac=bc=ac+kc$ contradice la cancelación aditiva. ∎

Hasta aquí el orden ha sido puramente aritmético: se definió en términos de suma. Pero cada natural es también un conjunto. Podemos preguntar ahora si ambas estructuras —la aritmética y la conjuntista— están relacionadas. La respuesta será más fuerte que una mera compatibilidad: son dos expresiones del mismo orden.

### Proposición 1.6.9 — El orden coincide con la inclusión {#ta-orden-natural-inclusion}

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

### Corolario 1.6.10 — Inclusión propia y orden estricto {#ta-orden-estricto-inclusion-propia}

Para $m,n\in\mathbb N$,

$$
m<n\iff m\subsetneq n.
$$

**Demostración.**  
Se combinan la definición de $<$ con la Proposición 1.6.9. ∎

### Lema 1.6.11 — Incremento positivo {#ta-incremento-positivo}

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

La inclusión propia traduce ya el orden estricto. En los naturales de von Neumann podemos afinar todavía más: como cada natural es el conjunto de sus predecesores, «ser estrictamente menor» deberá equivaler a pertenecer al otro natural.

### Teorema 1.6.12 — Orden estricto y pertenencia {#ta-orden-estricto-pertenencia}

*Glosario: [orden estricto](../otros/tratado-de-analisis-glosario.md#gl-orden-estricto)*

Para $m,n\in\mathbb N$,

$$
\boxed{m<n\iff m\in n.}
$$

**Demostración.**  
Si $m\in n$, la transitividad de $n$ da $m\subseteq n$, y $m\neq n$ porque $n\notin n$; luego $m\subsetneq n$ y el Corolario 1.6.10 da $m<n$.

Si $m<n$, escribimos $n=m+k$. Como $m\neq n$, $k\neq0$, y por el Teorema 1.2.7 — Predecesor de todo natural no nulo, $k=S(r)$. Entonces

$$
n=m+S(r),
$$

y el Lema 1.6.11 da $m\in n$. ∎

**Interpretación estructural.** Hemos llegado a una coincidencia característica de la representación de von Neumann:

$$
m<n\iff m\in n,
\qquad
m\leq n\iff m\subseteq n.
$$

El orden que construimos aritméticamente mediante la suma estaba ya inscrito en la arquitectura conjuntista de $\omega$. No son dos órdenes diferentes que casualmente sean compatibles: sobre $\mathbb N$ son la misma estructura vista desde dos lenguajes.

### Teorema 1.6.13 — Principio de buen orden {#ta-principio-buen-orden-naturales}

*Glosario: [buen orden](../otros/tratado-de-analisis-glosario.md#gl-buen-orden)*

Todo subconjunto no vacío $A\subseteq\mathbb N$ tiene un elemento mínimo.

**Demostración.**  
Primero inducimos sobre $n$ la afirmación: «todo subconjunto no vacío de $S(n)$ tiene mínimo».

Para $n=0$, $S(0)=\{0\}$; su único subconjunto no vacío es $\{0\}$, cuyo mínimo es $0$. Supongamos el resultado para $S(n)$ y sea $B\subseteq S(S(n))$ no vacío. Por lógica clásica, $B\cap S(n)$ es no vacío o es vacío. En el primer caso tiene mínimo $b$ por hipótesis inductiva; cualquier elemento adicional de $B$ sólo puede ser $S(n)$, y como $b\in S(n)$, el Teorema 1.6.12 da $b<S(n)$. En el segundo caso, la no vaciedad de $B$ y la descripción $S(S(n))=S(n)\cup\{S(n)\}$ fuerzan $B=\{S(n)\}$.

Sea ahora $A\subseteq\mathbb N$ no vacío. Bajo la lógica clásica del tratado, $A\neq\varnothing$ permite obtener un testigo $n\in A$. El conjunto $A\cap S(n)$ es no vacío porque $n\in S(n)$, y por lo anterior tiene mínimo $b$. Para $x\in A$, la totalidad da $x\leq n$ o $n\leq x$. En el primer caso $x\in S(n)$, así $b\leq x$; en el segundo, $b\leq n\leq x$. Por tanto $b$ es mínimo de $A$. ∎

> **Nota fundacional.** El teorema es correcto en la base clásica del tratado y no utiliza Choice. Sin embargo, su formulación parte sólo de $A\neq\varnothing$ y la prueba decide además si ciertos subconjuntos finitos son vacíos. La variante siguiente separa el núcleo constructivo: un testigo de habitabilidad y membresía decidible bastan para efectuar una búsqueda acotada.

### Proposición 1.6.14 — Buen orden constructivo bajo membresía decidible {#ta-buen-orden-constructivo-decidible}

Sea $A\subseteq\mathbb N$. Supongamos que:

1. $A$ está habitado, es decir, se dispone de un testigo $a\in A$;
2. la membresía es decidible:
   $$
   \forall n\in\mathbb N,
   \qquad
   n\in A\;\lor\;n\notin A.
   $$

Entonces $A$ posee un elemento mínimo. Además, a partir del testigo $a$ y del procedimiento de decisión de membresía, ese mínimo se obtiene mediante búsqueda finita en $S(a)$.

**Demostración.**  
Como $a\in A$ y $a\in S(a)$, el conjunto $A\cap S(a)$ está habitado. Recorremos los elementos de $S(a)$ en el orden natural

$$
0,1,\ldots,a.
$$

La membresía decidible permite comprobar sucesivamente si cada candidato pertenece a $A$. Como $a$ pertenece, el proceso termina. Sea $b$ el primer candidato que pertenece a $A$.

Por construcción, $b\in A$. Si $x\in A$ y $x<b$, entonces el Teorema 1.6.12 da $x\in b$; en particular $x$ aparece antes que $b$ en la búsqueda, contradiciendo la elección de $b$ como primer miembro encontrado. Por tanto ningún elemento de $A$ es estrictamente menor que $b$. La tricotomía decidible de la Proposición 1.6.7 da entonces $b\leq x$ para todo $x\in A$, de modo que $b$ es mínimo. ∎

### Corolario 1.6.15 — Inducción fuerte {#ta-induccion-fuerte}

*Glosario: [inducción fuerte](../otros/tratado-de-analisis-glosario.md#gl-induccion-fuerte)*

Si para todo $n\in\mathbb N$

$$
[\forall m<n,\ P(m)]\Rightarrow P(n),
$$

entonces $P(n)$ vale para todo $n\in\mathbb N$.

**Demostración.**  
Definamos

$$
Q(n)
\quad\Longleftrightarrow\quad
\forall m<n,\ P(m).
$$

Probaremos $Q(n)$ para todo $n$ por inducción ordinaria.

Para $n=0$, no existe $m<0$, de modo que $Q(0)$ vale vacíamente.

Supongamos $Q(n)$. La hipótesis de inducción fuerte aplicada a $n$ da entonces $P(n)$. Queremos probar $Q(S(n))$. Sea $m<S(n)$. Por el Teorema 1.6.12, $m\in S(n)=n\cup\{n\}$. Si $m\in n$, nuevamente el Teorema 1.6.12 da $m<n$, y $Q(n)$ implica $P(m)$. Si $m=n$, acabamos de obtener $P(n)$. Así todo $m<S(n)$ satisface $P(m)$ y, por tanto, $Q(S(n))$.

La inducción ordinaria da $Q(n)$ para todo $n$. Aplicando una vez más la hipótesis fuerte a cada $n$, concluimos $P(n)$ para todo natural. ∎

> **Nota fundacional.** Esta prueba no usa mínimo contraejemplo ni el principio de buen orden; por ello no hereda la dependencia clásica del Teorema 1.6.13.
