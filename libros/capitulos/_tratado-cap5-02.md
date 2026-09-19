## 5.2. Cortaduras determinadas por racionales {#sec-ta-5-2}

Hemos construido $\mathbb R_D$ como un conjunto de ciertos subconjuntos de $\mathbb Q$, pero todavía no hemos establecido ninguna relación formal entre los racionales y los elementos de este nuevo conjunto.

Si $q\in\mathbb Q$, el candidato natural es el conjunto formado por todos los racionales estrictamente menores que $q$. Ese conjunto representa, dentro del orden racional, todo el lado situado por debajo de la posición de $q$.

Es importante mantener separados los dos objetos. El racional $q$ y el conjunto de racionales menores que $q$ no son el mismo objeto. El segundo será una cortadura que representará posteriormente a $q$ dentro del modelo de Dedekind.

### Definición 5.2.1 — Sección inferior determinada por un racional

Sea $q\in\mathbb Q$. Definimos la **sección inferior determinada por $q$** mediante

$$
\boxed{
\delta_q
:=
\{r\in\mathbb Q:r<q\}.
}
$$

Este conjunto existe por Separación aplicada a $\mathbb Q$, pues la condición $r<q$ se expresa mediante el orden racional ya construido.

La definición no afirma todavía que $\delta_q\in\mathbb R_D$. Para ello debemos verificar las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind.

Obsérvese además que

$$
q\notin\delta_q,
$$

pues $q<q$ es falso por irreflexividad del orden estricto.

Como la comparación racional es decidible (Proposición 3.7.6 — Tricotomía decidible de los racionales), para $q$ fijo también lo es la membresía:
$$
\boxed{
r\in\delta_q\iff r<q.
}
$$
Así, las cortaduras racionales poseen una presentación efectiva particularmente simple; esto no se extiende automáticamente a una cortadura arbitraria de $\mathbb R_D$.

### Proposición 5.2.2 — Toda sección racional es una cortadura

Para todo $q\in\mathbb Q$,

$$
\boxed{
\delta_q\in\mathbb R_D.
}
$$

**Demostración.**

Sea $q\in\mathbb Q$. Verificamos las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind.

**No vaciedad.** Como $\mathbb Q$ es un cuerpo ordenado por Proposición 4.1.4 — $\mathbb Q$ es un cuerpo ordenado, Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado proporciona

$$
0_{\mathbb Q}<1_{\mathbb Q}.
$$

Invirtiendo el signo obtenemos

$$
-1_{\mathbb Q}<0_{\mathbb Q},
$$

y trasladando por $q$,

$$
q-1_{\mathbb Q}<q.
$$

Por tanto

$$
q-1_{\mathbb Q}\in\delta_q,
$$

y $\delta_q\neq\varnothing$.

**Propiedad.** Por irreflexividad,

$$
q\not<q.
$$

Así

$$
q\notin\delta_q.
$$

Como $q\in\mathbb Q$, se sigue que

$$
\delta_q\neq\mathbb Q.
$$

**Clausura inferior.** Si $r\in\delta_q$ y $s<r$, entonces $r<q$, de modo que

$$
s<r<q.
$$

Por transitividad,

$$
s<q,
$$

y por tanto $s\in\delta_q$.

**Ausencia de máximo.** Sea $r\in\delta_q$. Entonces $r<q$. Como todo cuerpo ordenado es densamente ordenado, Teorema 4.1.11 — Todo cuerpo ordenado es densamente ordenado proporciona $s\in\mathbb Q$ tal que

$$
r<s<q.
$$

Entonces $s\in\delta_q$ y $r<s$. Por tanto $\delta_q$ no posee máximo.

Se cumplen las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind. Por Definición 5.1.3 — Conjunto subyacente del modelo de Dedekind,

$$
\boxed{
\delta_q\in\mathbb R_D.
}
$$

∎

La proposición anterior proporciona para cada racional $q$ un elemento bien determinado de $\mathbb R_D$. Pero todavía debemos resistir una abreviatura tentadora:

$$
q\neq\delta_q
$$

como objetos de nuestra construcción. El miembro izquierdo es un racional construido como clase de equivalencia; el miembro derecho es un subconjunto de $\mathbb Q$.

Lo que hemos establecido es la asignación

$$
q\longmapsto\delta_q.
$$

Más adelante demostraremos que esta asignación es una función inyectiva que preserva y refleja el orden. Antes conviene responder una cuestión aún más fundamental: ¿toda cortadura es alguna $\delta_q$?
