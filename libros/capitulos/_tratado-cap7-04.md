## 7.4. Demostración de la propiedad del supremo {#sec-ta-7-4}

### Teorema 7.4.1 — El supremo de una familia de cortaduras es su unión

Sea $\mathcal A\subseteq\mathbb R_D$ una familia no vacía y acotada superiormente. Entonces $U_D(\mathcal A)$ es el supremo de $\mathcal A$ y, por la unicidad establecida en Proposición 0.7.8 — Unicidad de supremo e ínfimo, podemos escribir

$$
\boxed{\sup_D\mathcal A=\bigcup\mathcal A.}
$$

**Demostración.**

Por Proposición 7.3.1 — Unión de una familia no vacía y acotada, $U_D(\mathcal A)=\bigcup\mathcal A$ pertenece a $\mathbb R_D$.

Primero es una cota superior. Si $\alpha\in\mathcal A$, entonces

$$
\alpha\subseteq\bigcup\mathcal A,
$$

y por la definición del orden de Dedekind,

$$
\alpha\leq_D\bigcup\mathcal A.
$$

Ahora sea $\gamma\in\mathbb R_D$ cualquier cota superior de $\mathcal A$. Por Proposición 7.1.1 — Caracterización conjuntista de las cotas superiores, toda $\alpha\in\mathcal A$ satisface $\alpha\subseteq\gamma$. Si $q\in\bigcup\mathcal A$, existe $\alpha\in\mathcal A$ con $q\in\alpha$, y por ello $q\in\gamma$. Así,

$$
\bigcup\mathcal A\subseteq\gamma,
$$

es decir,

$$
\bigcup\mathcal A\leq_D\gamma.
$$

Por tanto la unión es una cota superior menor o igual que cualquier otra cota superior: es el supremo. ∎

La operación que repara la incompletitud racional resulta ser una de las operaciones conjuntistas más elementales:

$$
\boxed{\sup_D\mathcal A=\bigcup\mathcal A.}
$$

Para una familia dada que satisface las hipótesis, la fórmula del supremo es literalmente la unión. Esto debe distinguirse de un operador efectivo global. Puede definirse conjuntistamente, sobre el dominio apropiado de subconjuntos no vacíos y acotados de $\mathbb R_D$, una función canónica
$$
\operatorname{Sup}_D(\mathcal A):=\bigcup\mathcal A,
$$
sin Choice, porque el valor es único. Pero su existencia extensional sobre un dominio construido dentro de $\mathcal P(\mathbb R_D)$ no suministra por sí sola una representación computable de las familias ni un algoritmo uniforme de supremo.

### Teorema 7.4.2 — Completitud del cuerpo de Dedekind

La estructura

$$
\boxed{(\mathbb R_D,+_D,\cdot_D,\leq_D)}
$$

es un cuerpo ordenado completo.

**Demostración.**

Por Teorema 6.8.14 — El modelo de Dedekind es un cuerpo ordenado, $\mathbb R_D$ es un cuerpo ordenado. Sea $\mathcal A\subseteq\mathbb R_D$ no vacío y acotado superiormente. Teorema 7.4.1 — El supremo de una familia de cortaduras es su unión demuestra que

$$
\sup_D\mathcal A=\bigcup\mathcal A\in\mathbb R_D.
$$

Así, todo subconjunto no vacío y acotado superiormente de $\mathbb R_D$ posee supremo en $\mathbb R_D$. Ésta es exactamente la propiedad del supremo de Definición 4.6.1 — Propiedad del supremo y cuerpo ordenado completo. Por tanto,

$$
\boxed{\mathbb R_D\text{ es un cuerpo ordenado completo}.}
$$

∎

> **Nota fundacional.** La completitud anterior cuantifica sobre todos los subconjuntos de $\mathbb R_D$ que satisfacen las hipótesis. Es una propiedad extensional clásica:
> $$
> \boxed{
> \text{completitud plena}
> \neq
> \text{algoritmo uniforme de supremo}.
> }
> $$
> El resultado no utiliza Choice, pero tampoco afirma que una familia arbitraria venga acompañada de una presentación efectiva.
