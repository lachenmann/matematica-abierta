## 4.8. Programa de completación de $\mathbb Q$ {#sec-ta-4-8}

Ya podemos expresar con precisión el objetivo de las dos construcciones siguientes.

### Definición 4.8.1 — Incrustación de cuerpos ordenados {#ta-incrustacion-cuerpos-ordenados}

*Glosario: [incrustación de cuerpos ordenados](../otros/tratado-de-analisis-glosario.md#gl-incrustacion-cuerpos-ordenados)*

Sean $F$ y $E$ cuerpos ordenados. Una función

$$
\iota:F\to E
$$

es una **incrustación de cuerpos ordenados** si es inyectiva y, para todos $x,y\in F$,

$$
\iota(0_F)=0_E,
\qquad
\iota(1_F)=1_E,
$$

$$
\iota(x+y)=\iota(x)+\iota(y),
$$

$$
\iota(xy)=\iota(x)\iota(y),
$$

y

$$
x\leq_F y
\iff
\iota(x)\leq_E\iota(y).
$$

### Definición 4.8.2 — Completación ordenada de $\mathbb Q$ {#ta-completacion-ordenada-q}

*Glosario: [completación ordenada de $\mathbb Q$](../otros/tratado-de-analisis-glosario.md#gl-completacion-ordenada-q)*

Una **completación ordenada de $\mathbb Q$** es un par $(E,\iota)$ tal que:

1. $E$ es un [cuerpo ordenado completo](../otros/tratado-de-analisis-glosario.md#gl-cuerpo-ordenado-completo);
2. $\iota:\mathbb Q\to E$ es una [incrustación de cuerpos ordenados](#ta-incrustacion-cuerpos-ordenados).

No exigimos separadamente que $\iota[\mathbb Q]$ sea denso: demostraremos que esa propiedad se sigue de las condiciones anteriores.

### Proposición 4.8.3 — La imagen racional de una completación es densa {#ta-imagen-racional-densa-completacion}

Sea $(E,\iota)$ una completación ordenada de $\mathbb Q$. Entonces, para cualesquiera $x<y$ en $E$, existe $q\in\mathbb Q$ tal que

$$
\boxed{
x<\iota(q)<y.
}
$$

**Demostración.**

Como $E$ es completo, el [Teorema 4.6.3](#ta-completo-implica-arquimediano) implica —clásicamente bajo la interfaz actual— que es arquimediano. La imagen

$$
K:=\iota[\mathbb Q]
$$

es un subcuerpo de $E$. Contiene $0_E$ y $1_E$ y es cerrado bajo suma y producto por la [Definición 4.8.1](#ta-incrustacion-cuerpos-ordenados). Si $z=\iota(q)\in K$, entonces

$$
\iota(q)+\iota(-q)=\iota(q-q)=\iota(0)=0_E,
$$

de modo que, por unicidad del opuesto aditivo, $\iota(-q)=-\iota(q)$ y $K$ es cerrado bajo opuestos.

Para la clausura bajo inversos, sea ahora $z=\iota(q)\in K$ con $z\neq0_E$. Entonces $q\neq0_{\mathbb Q}$, pues $q=0_{\mathbb Q}$ implicaría $z=\iota(0_{\mathbb Q})=0_E$. Por tanto $q^{-1}$ existe y

$$
\iota(q)\iota(q^{-1})
=
\iota(qq^{-1})
=1_E.
$$

Por unicidad del inverso multiplicativo, $\iota(q^{-1})=\iota(q)^{-1}$. Así $K$ satisface todas las condiciones de subcuerpo. Por el [Corolario 4.5.2](#ta-todo-subcuerpo-denso-arquimediano), todo subcuerpo de un cuerpo arquimediano es denso. Por tanto existe $z\in K$ con

$$
x<z<y.
$$

Como $z\in\iota[\mathbb Q]$, existe $q\in\mathbb Q$ con $z=\iota(q)$. ∎

> **Nota fundacional.** La densidad racional de una completación es un teorema válido del tratado clásico, no una consecuencia constructiva de la mera definición actual de completitud. Tampoco se afirma aquí un procedimiento efectivo para calcular, a partir de $x<y$, un racional intermedio.

La definición anterior fija el blanco estructural. Los capítulos siguientes producirán dos objetos concretos distintos:

$$
(\mathbb R_D,\iota_D)
$$

mediante **cortaduras de Dedekind**, y

$$
(\mathbb R_C,\iota_C)
$$

mediante **clases de equivalencia de sucesiones de Cauchy racionales**.

Cada construcción deberá demostrar, sin importar resultados de la otra:

1. existencia del conjunto subyacente;
2. operaciones bien definidas;
3. estructura de cuerpo ordenado;
4. existencia de supremos para todos los subconjuntos no vacíos y acotados superiormente;
5. incrustación canónica de $\mathbb Q$.

Sólo después compararemos ambos modelos y demostraremos que representan la misma estructura pertinente hasta isomorfismo ordenado de cuerpos que fija la copia racional.

La diferencia entre las dos estrategias puede resumirse así:

$$
\boxed{
\begin{aligned}
\text{Dedekind:}&\quad \text{añadir fronteras de orden},\\
\text{Cauchy:}&\quad \text{añadir límites de aproximaciones racionales}.
\end{aligned}
}
$$

---

::: {.callout-note title="Publicación progresiva"}
Con §4.8 queda fijado el programa estructural que deberán satisfacer las dos construcciones de los números reales y se demuestra que toda completación ordenada de $\mathbb Q$ contiene una copia racional densa. La siguiente entrega será **§4.9 — Qué hemos establecido**.
:::
