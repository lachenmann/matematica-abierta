## 1.2. Estructura de los naturales y Peano {#sec-ta-1-2}

Hemos construido un conjunto; todavía debemos demostrar que se comporta como los números naturales. Ésta es una diferencia metodológica importante: las propiedades de Peano no se postulan aquí como axiomas de un sistema numérico abstracto, sino que deberán aparecer como teoremas de la construcción $\mathbb N=\omega$.

Antes de reunir esas propiedades necesitamos comprender mejor la forma conjuntista de cada natural. En la representación de von Neumann, un natural contiene precisamente a sus predecesores; la noción de conjunto transitivo captura la estabilidad que hace posible esa interpretación.

### Definición 1.2.1 — Conjunto transitivo {#ta-conjunto-transitivo}

*Glosario: [conjunto transitivo](../otros/tratado-de-analisis-glosario.md#gl-conjunto-transitivo)*

Un conjunto $T$ es transitivo si

$$
x\in T\Rightarrow x\subseteq T.
$$

### Proposición 1.2.2 — Transitividad e irreflexividad {#ta-transitividad-irreflexividad-naturales}

Para todo $n\in\mathbb N$, $n$ es transitivo y $n\notin n$.

**Demostración.**

Inducimos sobre $n$. El vacío es transitivo y $0\notin0$. Supongamos $n$ transitivo y $n\notin n$. Si $x\in S(n)$, entonces $x\in n$ o $x=n$; en ambos casos $x\subseteq S(n)$, luego $S(n)$ es transitivo. Si $S(n)\in S(n)$, entonces $S(n)=n$ o $S(n)\in n$; en el primer caso $n\in n$, y en el segundo la transitividad de $n$ y $n\in S(n)$ vuelven a dar $n\in n$. Contradicción. ∎

### Proposición 1.2.3 — Clausura por sucesor {#ta-clausura-sucesor}

Si $n\in\mathbb N$, entonces $S(n)\in\mathbb N$.

**Demostración.**

Es la clausura del conjunto inductivo $\mathbb N$. ∎

### Proposición 1.2.4 — El cero no es sucesor {#ta-cero-no-sucesor}

Para todo $n\in\mathbb N$, $S(n)\neq0$.

**Demostración.**

$n\in S(n)$, mientras que $0=\varnothing$ no tiene elementos. ∎

### Teorema 1.2.5 — Inyectividad del sucesor {#ta-inyectividad-sucesor}

*Glosario: [inyectividad](../otros/tratado-de-analisis-glosario.md#gl-inyectividad)*

Para $m,n\in\mathbb N$,

$$
S(m)=S(n)\Rightarrow m=n.
$$

**Demostración.**

De $m\in S(m)=S(n)$ se sigue $m\in n$ o $m=n$; simétricamente, $n\in m$ o $n=m$. Si $m\neq n$, tendríamos $m\in n$ y $n\in m$. Como $n$ es transitivo, $m\subseteq n$, y entonces $n\in m$ implica $n\in n$, contradicción. ∎

Con la clausura por sucesor, la exclusión del cero como sucesor, la inyectividad de $S$ y el principio de inducción ya podemos reunir el resultado estructural buscado. Lo que en una presentación axiomática sería el punto de partida aparece aquí como consecuencia de la construcción.

### Teorema 1.2.6 — Propiedades de Peano {#ta-propiedades-peano}

*Glosario: [propiedades de Peano](../otros/tratado-de-analisis-glosario.md#gl-propiedades-peano)*

El sistema $(\mathbb N,0,S)$ satisface: $0\in\mathbb N$; clausura por sucesor; cero no es sucesor; el sucesor es inyectivo; y el principio de inducción.

**Demostración.**

Cada una de las cinco afirmaciones ha sido demostrada en los resultados anteriores. ∎

### Teorema 1.2.7 — Predecesor de todo natural no nulo {#ta-predecesor-natural}

*Glosario: [predecesor](../otros/tratado-de-analisis-glosario.md#gl-predecesor)*

Para todo $n\in\mathbb N$, o $n=0$, o existe un único $m\in\mathbb N$ tal que $n=S(m)$.

**Demostración.**

La propiedad «$n=0$ o $n$ es sucesor de algún natural» es inductiva: vale en $0$ y el sucesor de cualquier natural tiene como predecesor a ese natural. La unicidad se sigue de la inyectividad de $S$. ∎

### Notación 1.2.8 — Unidad natural {#ta-unidad-natural}

*Glosario: [uno](../otros/tratado-de-analisis-glosario.md#gl-uno)*

Definimos

$$
\boxed{1:=S(0).}
$$
