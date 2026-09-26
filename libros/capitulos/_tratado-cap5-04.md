## 5.4. El orden de Dedekind {#sec-ta-5-4}

Hasta ahora hemos tratado las cortaduras principalmente como subconjuntos de $\mathbb Q$. Si han de desempeñar el papel de números, necesitamos poder compararlas.

La propia forma de la construcción sugiere cómo hacerlo. Una cortadura registra todos los racionales situados por debajo de cierta frontera. Si otra cortadura alcanza más lejos hacia la derecha, entonces todo racional que pertenece a la primera deberá pertenecer también a la segunda.

La comparación natural es, por tanto, la inclusión.

### Definición 5.4.1 — Orden de Dedekind

Sean $\alpha,\beta\in\mathbb R_D$. Definimos

$$
\boxed{
\alpha\leq_D\beta
\quad\Longleftrightarrow\quad
\alpha\subseteq\beta.
}
$$

La relación $\leq_D$ se denominará orden de Dedekind.

La inclusión ordena parcialmente cualquier familia de conjuntos, pero en general no la ordena totalmente. Dos subconjuntos arbitrarios pueden ser incomparables. Lo especial de las cortaduras es que su clausura hacia abajo, combinada con la totalidad del orden racional, impide que se crucen.

### Teorema 5.4.2 — La inclusión ordena totalmente las cortaduras

La relación $\leq_D$ es un orden total sobre $\mathbb R_D$.

**Demostración.**

La reflexividad y la transitividad proceden directamente de las correspondientes propiedades de la inclusión. La antisimetría se sigue del criterio extensional por doble inclusión Teorema 0.2.4 — Criterio extensional por doble inclusión.

Queda demostrar la totalidad.

Sean $\alpha,\beta\in\mathbb R_D$. Por lógica clásica, o bien

$$
\alpha\subseteq\beta,
$$

o bien

$$
\alpha\not\subseteq\beta.
$$

En el primer caso, $\alpha\leq_D\beta$.

Supongamos entonces $\alpha\not\subseteq\beta$. Existe $a\in\alpha$ tal que

$$
a\notin\beta.
$$

Demostraremos que $\beta\subseteq\alpha$.

Sea $b\in\beta$. Como el orden racional es total, tenemos

$$
b\leq a
\qquad\text{o}\qquad
a\leq b.
$$

Si $a\leq b$, no puede ser $a=b$, pues $b\in\beta$ y $a\notin\beta$. Por tanto $a<b$. Como $b\in\beta$ y $\beta$ es cerrada hacia abajo, se seguiría $a\in\beta$, contradicción.

Debe cumplirse entonces

$$
b\leq a.
$$

Tampoco puede ser $b=a$, por la misma razón. Luego

$$
b<a.
$$

Como $a\in\alpha$ y $\alpha$ es cerrada hacia abajo,

$$
b\in\alpha.
$$

El elemento $b\in\beta$ era arbitrario, de modo que

$$
\beta\subseteq\alpha.
$$

Por tanto

$$
\beta\leq_D\alpha.
$$

Hemos probado que para cualesquiera $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{
\alpha\leq_D\beta
\quad\text{o}\quad
\beta\leq_D\alpha.
}
$$

Así $\leq_D$ es un orden total. ∎

La totalidad no es una propiedad automática de la inclusión. Es consecuencia de la forma especial de los elementos de $\mathbb R_D$. Dos subconjuntos arbitrarios de $\mathbb Q$ pueden cruzarse; dos cortaduras no.

En particular, un único testigo $a\in\alpha\setminus\beta$ fuerza ya

$$
\beta\subseteq\alpha.
$$

Obsérvese también que la comparabilidad utiliza únicamente la clausura inferior de las cortaduras y la totalidad del orden racional. La condición de ausencia de máximo no interviene en esta parte.

> **Nota fundacional.** El resultado establece comparabilidad clásica de cualesquiera dos cortaduras. La prueba usa LEM sobre $\alpha\subseteq\beta$ y, desde $\alpha\not\subseteq\beta$, extrae clásicamente un testigo $a\in\alpha\setminus\beta$. Por tanto
> $$
> \boxed{
> \text{comparabilidad clásica}
> \neq
> \text{procedimiento de comparación decidible}.
> }
> $$
> Del mismo modo, la igualdad $\alpha=\beta$ está definida extensionalmente, pero no es decidible en general para cortaduras arbitrarias.

### Corolario 5.4.3 — El orden estricto es inclusión propia

Para $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{
\alpha<_D\beta
\quad\Longleftrightarrow\quad
\alpha\subsetneq\beta.
}
$$

**Demostración.**

Por Teorema 5.4.2 — La inclusión ordena totalmente las cortaduras, $\leq_D$ es un orden total. Su orden estricto asociado está definido por

$$
\alpha<_D\beta
\quad\Longleftrightarrow\quad
\alpha\leq_D\beta
\ \land\\
\alpha\neq\beta.
$$

Usando Definición 5.4.1 — Orden de Dedekind, esto equivale a

$$
\alpha\subseteq\beta
\ \land\\
\alpha\neq\beta,
$$

es decir,

$$
\alpha\subsetneq\beta.
$$

∎

Hemos conseguido así algo conceptualmente decisivo. El conjunto $\mathbb R_D$ ya no es simplemente una colección de subconjuntos racionales: posee un orden total, y ese orden surge directamente de la manera en que una cortadura registra un segmento inferior de $\mathbb Q$.
