## 8.4. Sucesiones de Cauchy {#sec-ta-8-4}

La convergencia racional de §8.3 compara los términos tardíos de una sucesión con un racional fijo $\ell$. Esa definición es adecuada cuando tal racional existe, pero no puede servir todavía para detectar procesos que se estabilizan sin converger dentro de $\mathbb Q$.

La idea de Cauchy elimina precisamente esa referencia externa. En lugar de preguntar si $q_n$ está cerca de un candidato a límite, preguntaremos si **dos términos suficientemente tardíos cualesquiera están cerca entre sí**.

El cambio lógico es pequeño en apariencia, pero decisivo:

$$
\boxed{
\text{convergencia racional: }d_{\mathbb Q}(q_n,\ell)<\varepsilon
\qquad\longrightarrow\qquad
\text{Cauchy: }d_{\mathbb Q}(q_m,q_n)<\varepsilon.
}
$$

En la condición de la derecha ya no aparece ningún objeto que deba ser el límite. La sucesión se examina desde dentro de $\mathbb Q$.

### Definición 8.4.1 — Sucesión racional de Cauchy

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional. Diremos que $q$ es una **sucesión de Cauchy** si

$$
\boxed{
\forall\varepsilon\in\mathbb Q,
\quad
0_{\mathbb Q}<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall m,n\in\mathbb N,
\quad
\bigl(N\leq m\land N\leq n\bigr)
\Longrightarrow
 d_{\mathbb Q}(q_m,q_n)<\varepsilon.
}
$$

El orden de los cuantificadores forma parte esencial de la definición. Para cada precisión racional positiva $\varepsilon$ puede elegirse una etapa $N$ dependiente de $\varepsilon$; una vez fijada esa etapa, **todo par** de términos con índices posteriores a $N$ debe encontrarse a distancia menor que $\varepsilon$.

No se exige que exista un racional $\ell$ al cual se aproximen los términos. Tampoco se menciona $\mathbb R_D$ ni ningún otro sistema de números reales.

Un **módulo de Cauchy** para $q$ es una función
$$
\mu_C:\mathbb Q_{>0}\to\mathbb N
$$
tal que
$$
m,n\geq\mu_C(\varepsilon)
\Longrightarrow
d_{\mathbb Q}(q_m,q_n)<\varepsilon.
$$
Cuando tanto $n\mapsto q_n$ como $\mu_C$ son computables, diremos que $q$ está dada por un
**nombre efectivo de Cauchy con módulo**.

La existencia clásica de algún índice para cada precisión no suministra automáticamente un módulo
computable. Incluso el módulo mínimo obtenido por buen orden puede ser canónico sin ser efectivo.

---

### Definición 8.4.2 — Conjunto de las sucesiones racionales de Cauchy

Definimos

$$
\boxed{
\mathcal C_{\mathbb Q}
:=
\{q\in\mathbb Q^{\mathbb N}:q\text{ es de Cauchy}\}.
}
$$

De manera completamente expandida,

$$
\mathcal C_{\mathbb Q}
=
\left\{
q\in\mathbb Q^{\mathbb N}:
\forall\varepsilon\in\mathbb Q,
\ 0_{\mathbb Q}<\varepsilon
\Rightarrow
\exists N\in\mathbb N\;
\forall m,n\in\mathbb N,
\ (N\leq m\land N\leq n)
\Rightarrow
 d_{\mathbb Q}(q_m,q_n)<\varepsilon
\right\}.
$$

Como $\mathbb Q^{\mathbb N}$ ya existe y la condición anterior es una propiedad definible, $\mathcal C_{\mathbb Q}$ existe por separación.

> **Nota fundacional.** La definición forma un subconjunto de un conjunto previamente construido. No selecciona límites, índices simultáneos ni representantes; no utiliza Choice.

> Además, la pertenencia $q\in\mathcal C_{\mathbb Q}$ contiene una alternancia
> $\forall\varepsilon\,\exists N\,\forall m,n$. Para una sucesión arbitraria, esa propiedad no es
> decidible en general.

---

### Proposición 8.4.3 — Formulaciones equivalentes de la condición de Cauchy

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional. Son equivalentes:

1. $q$ es de Cauchy;
2. para todo $\varepsilon\in\mathbb Q$ con $0_{\mathbb Q}<\varepsilon$, existe $N\in\mathbb N$ tal que, para cualesquiera $m,n\in\mathbb N$ con $N\leq m$ y $N\leq n$,
   $$
   |q_m-q_n|<\varepsilon;
   $$
3. para todo $\varepsilon\in\mathbb Q$ con $0_{\mathbb Q}<\varepsilon$, existe $N\in\mathbb N$ tal que, para cualesquiera $m,n\in\mathbb N$ con $N\leq m$ y $N\leq n$,
   $$
   q_n-\varepsilon<q_m<q_n+\varepsilon.
   $$

**Demostración.**

Por Definición 8.4.1 — Sucesión racional de Cauchy, la primera condición exige exactamente que, para cada $\varepsilon>0$ racional, exista $N$ tal que todo par de índices $m,n\geq N$ satisfaga

$$
d_{\mathbb Q}(q_m,q_n)<\varepsilon.
$$

Para cada par fijo $(m,n)$, la definición de la distancia y Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional proporcionan las equivalencias

$$
d_{\mathbb Q}(q_m,q_n)<\varepsilon
\iff
|q_m-q_n|<\varepsilon
$$

y

$$
|q_m-q_n|<\varepsilon
\iff
q_n-\varepsilon<q_m<q_n+\varepsilon.
$$

Como estas equivalencias no alteran ninguno de los cuantificadores exteriores, las tres formulaciones son equivalentes. ∎

---

### Proposición 8.4.4 — Las sucesiones constantes son de Cauchy

Para todo $c\in\mathbb Q$,

$$
\boxed{
\underline c\in\mathcal C_{\mathbb Q}.
}
$$

En particular,

$$
\mathcal C_{\mathbb Q}\neq\varnothing.
$$

**Demostración.**

Sea $\varepsilon\in\mathbb Q$ con $0_{\mathbb Q}<\varepsilon$. Tomemos $N:=0$. Si $m,n\in\mathbb N$ satisfacen $N\leq m$ y $N\leq n$, entonces

$$
\underline c_m=c=\underline c_n.
$$

Por la definitud de la distancia racional (Proposición 8.2.2 — Propiedades fundamentales de la distancia racional),

$$
d_{\mathbb Q}(\underline c_m,\underline c_n)=0_{\mathbb Q}.
$$

Como $0_{\mathbb Q}<\varepsilon$,

$$
d_{\mathbb Q}(\underline c_m,\underline c_n)<\varepsilon.
$$

Por Definición 8.4.1 — Sucesión racional de Cauchy, $\underline c$ es de Cauchy; por Definición 8.4.2 — Conjunto de las sucesiones racionales de Cauchy,

$$
\underline c\in\mathcal C_{\mathbb Q}.
$$

Así $\mathcal C_{\mathbb Q}$ contiene, por ejemplo, la sucesión constante $\underline{0_{\mathbb Q}}$, y por tanto no es vacío. ∎

---

### Lo que hemos ganado

La condición de Cauchy permite reconocer una forma de estabilización racional que no menciona ningún límite:

$$
q\in\mathcal C_{\mathbb Q}
$$

significa que los términos tardíos de $q$ pueden hacerse mutuamente tan próximos como se quiera, con precisión medida enteramente dentro de $\mathbb Q$.

Éste es el cambio conceptual que necesitábamos para la segunda construcción de los reales. Una sucesión puede ser de Cauchy aun cuando todavía no hayamos demostrado que posea un límite racional; de hecho, esa posibilidad será precisamente la que permitirá superar la insuficiencia de $\mathbb Q$.

Antes de usar las sucesiones de Cauchy como representaciones de nuevos números debemos establecer el puente mínimo con la noción anterior de convergencia: **todo proceso que ya converge racionalmente debe satisfacer necesariamente la condición de Cauchy**. Ése será el contenido de §8.5.
---
