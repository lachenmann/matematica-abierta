## 4.6. Propiedad del supremo {#sec-ta-4-6}

La arquimedianidad controla el tamaño relativo de los elementos, pero no obliga a que existan fronteras internas para todos los conjuntos acotados. La propiedad que falta en $\mathbb Q$ es más fuerte.

### Definición 4.6.1 — Propiedad del supremo y cuerpo ordenado completo {#ta-propiedad-supremo-cuerpo-completo}

*Glosario: [propiedad del supremo](../otros/tratado-de-analisis-glosario.md#gl-propiedad-supremo) · [cuerpo ordenado completo](../otros/tratado-de-analisis-glosario.md#gl-cuerpo-ordenado-completo)*

Un cuerpo ordenado $F$ tiene la **propiedad del supremo** si todo subconjunto $A\subseteq F$ que sea

1. no vacío, y
2. acotado superiormente,

posee un supremo en $F$.

Un cuerpo ordenado con esta propiedad se llamará **cuerpo ordenado completo**.

La palabra «completo» tendrá en esta parte del tratado este significado de orden. La definición cuantifica sobre **subconjuntos arbitrarios** de $F$; en el marco ZF del tratado, esto es una condición extensional sobre la totalidad $\mathcal P(F)$.

> **Nota fundacional.** La afirmación
> $$
> \forall A\subseteq F\;\exists!\sup A
> $$
> bajo las hipótesis correspondientes no proporciona por sí sola un algoritmo $A\mapsto\sup A$. Existencia y unicidad del supremo no equivalen a computabilidad del supremo. Cuando se requiera una lectura positiva/constructiva, sustituiremos el simple predicado $A\neq\varnothing$ por datos explícitos de habitabilidad.

Más adelante demostraremos la relación de esta completitud de orden con otras nociones de completitud cuando los conceptos necesarios hayan sido construidos.

### Proposición 4.6.2 — La propiedad del supremo implica la propiedad del ínfimo {#ta-supremo-implica-infimo}

Sea $F$ un cuerpo ordenado completo. Todo subconjunto no vacío $A\subseteq F$ acotado inferiormente posee [ínfimo](../otros/tratado-de-analisis-glosario.md#gl-infimo).

**Demostración.**

Definimos, por separación dentro de $F$,

$$
-A:=\{y\in F:\exists a\in A\;(y=-a)\}.
$$

En la lectura positiva, fijado un testigo $a_0\in A$, el elemento $-a_0$ muestra directamente que $-A$ está habitado. En la formulación clásica actual, esta disponibilidad de un testigo se obtiene de la no vaciedad de $A$.

Si $\ell$ es una cota inferior de $A$, entonces $\ell\leq a$ para todo $a\in A$, y por inversión del orden,

$$
-a\leq-\ell.
$$

Así $-\ell$ es cota superior de $-A$. Por completitud existe

$$
s:=\sup(-A).
$$

Afirmamos que $-s=\inf A$. Para todo $a\in A$, $-a\leq s$, luego $-s\leq a$; por tanto $-s$ es cota inferior de $A$.

Sea $c$ cualquier cota inferior de $A$. Entonces $-c$ es cota superior de $-A$, de modo que

$$
s\leq-c.
$$

Invirtiendo signos,

$$
c\leq-s.
$$

Así $-s$ es la mayor cota inferior de $A$. ∎

> **Versión positiva.** Si la hipótesis se formula directamente para un subconjunto **habitado** $A$ y se proporciona un testigo $a_0\in A$, el argumento anterior —incluida la habitabilidad de $-A$— es constructivamente compatible.

### Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano {#ta-completo-implica-arquimediano}

Todo cuerpo ordenado completo $F$ es arquimediano.

**Demostración.**

Supongamos, por contradicción, que $F$ no es arquimediano. Negando clásicamente la condición positiva de [Definición 4.4.1](#ta-cuerpo-ordenado-arquimediano), obtenemos un elemento $u\in F$ tal que para todo $n\in\mathbb N$ no se cumple

$$
u<\nu_F(n).
$$

Usando la totalidad del orden y eliminación clásica de la doble negación, esto implica

$$
\nu_F(n)\leq u
$$

para todo $n$. Por tanto la imagen

$$
N_F:=\nu_F[\mathbb N]
$$

—que existe por separación como imagen directa dentro de $F$— está acotada superiormente. Está habitada porque contiene $0_F$. Por completitud existe

$$
s:=\sup N_F.
$$

Por el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado), $0_F<1_F$ y, al sumar $s-1_F$, se obtiene $s-1_F<s$. El elemento $s-1_F$ no puede ser una cota superior de $N_F$, pues de lo contrario sería una cota superior estrictamente menor que el supremo $s$.

Decir que $s-1_F$ no es cota superior es negar un universal. Por negación clásica de cuantificadores existe, por tanto, $n\in\mathbb N$ tal que

$$
\neg\bigl(\nu_F(n)\leq s-1_F\bigr).
$$

La totalidad del orden fuerza entonces

$$
s-1_F\leq\nu_F(n),
$$

y la igualdad también queda excluida por la negación anterior; así

$$
s-1_F<\nu_F(n).
$$

Sumando $1_F$,

$$
s<\nu_F(n)+1_F
=\nu_F(S(n)).
$$

Pero $\nu_F(S(n))\in N_F$, contradiciendo que $s$ sea cota superior de $N_F$. Luego $F$ es arquimediano. ∎

> **Nota fundacional.** La clasicidad de este teorema es esencial bajo la interfaz actual de completitud: aparece tanto al convertir la negación de arquimedianidad en una cota superior como al extraer un elemento que viola la condición de ser cota superior. No interviene ninguna forma del axioma de elección.

### Corolario 4.6.4 — El subcuerpo primo es denso en todo cuerpo ordenado completo {#ta-subcuerpo-primo-denso-completo}

Si $F$ es un cuerpo ordenado completo y $x<y$, existe $q\in P_F$ tal que

$$
x<q<y.
$$

**Demostración.**

El [Teorema 4.6.3](#ta-completo-implica-arquimediano) da arquimedianidad y el [Teorema 4.5.1](#ta-densidad-subcuerpo-primo-arquimediano) da la densidad de $P_F$. ∎

### Proposición 4.6.5 — $\mathbb Q$ no es un cuerpo ordenado completo {#ta-q-no-completo}

El cuerpo ordenado $\mathbb Q$ no tiene la propiedad del supremo.

**Demostración.**

La [Proposición 3.9.8](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-s2-no-vacio-acotado) demuestra que

$$
S_2=\{q\in\mathbb Q:0\leq q,\ q^2<2\}
$$

es no vacío y está acotado superiormente. El [Teorema 3.9.9](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-s2-sin-supremo-racional) demuestra que $S_2$ no posee supremo racional. Esto contradice exactamente la condición de la [Definición 4.6.1](#ta-propiedad-supremo-cuerpo-completo). ∎

Tenemos ahora una formulación abstracta del defecto detectado al final del capítulo anterior: $\mathbb Q$ es arquimediano, pero no completo.

---
