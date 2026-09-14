## 2.2. Construcción del conjunto $\mathbb Z$ {#sec-ta-2-2}

Ahora sí podemos formar el cociente. Antes de hacerlo conviene verificar que todos los conjuntos involucrados existen dentro de ZF.

### Proposición 2.2.1 — Existencia del cociente entero {#ta-existencia-cociente-entero}

Existe el conjunto cociente

$$
(\mathbb N\times\mathbb N)/{\sim_{\mathbb Z}}.
$$

**Demostración.**  
El producto cartesiano $\mathbb N\times\mathbb N$ existe por la construcción general establecida en el capítulo fundacional. En §2.1 demostramos que $\sim_{\mathbb Z}$ es una relación de equivalencia sobre ese conjunto. La existencia del cociente es entonces una instancia de la construcción general de conjuntos cociente desarrollada en el Capítulo 0. No interviene el axioma de elección. ∎

### Definición 2.2.2 — Conjunto de los números enteros {#ta-conjunto-enteros}

Definimos

$$
\boxed{
\mathbb Z:=
(\mathbb N\times\mathbb N)/{\sim_{\mathbb Z}}.
}
$$

Un **[número entero](../otros/tratado-de-analisis-glosario.md#gl-numero-entero)** es, por definición, un elemento de $\mathbb Z$.

### Notación 2.2.3 — Clases enteras {#ta-clases-enteras}

Para $(a,b)\in\mathbb N\times\mathbb N$ escribiremos

$$
[(a,b)]_{\mathbb Z}
$$

para su **[clase entera](../otros/tratado-de-analisis-glosario.md#gl-clase-entera)**, es decir, su clase de equivalencia módulo $\sim_{\mathbb Z}$. Cuando no haya riesgo de confusión, abreviaremos a

$$
[(a,b)].
$$

La notación $[(a,b)]$ no designa el par $(a,b)$: designa el conjunto de todas las diferencias formales equivalentes a él.

### Proposición 2.2.4 — Criterio de igualdad de clases enteras {#ta-igualdad-clases-enteras}

Para $a,b,c,d\in\mathbb N$,

$$
\boxed{
[(a,b)]=[(c,d)]
\iff
a+d=b+c.
}
$$

**Demostración.**  
Por el teorema general de igualdad de clases de equivalencia,

$$
[(a,b)]=[(c,d)]
\iff
(a,b)\sim_{\mathbb Z}(c,d).
$$

La definición de $\sim_{\mathbb Z}$ transforma la condición de la derecha exactamente en

$$
a+d=b+c.
$$

∎

Tenemos ya el conjunto de los enteros, pero todavía no una aritmética sobre él. Las operaciones deberán definirse sobre clases, y esto exige demostrar que no dependen del representante escogido.
