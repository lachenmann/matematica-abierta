## 0.5. Clases de equivalencia, particiones y cocientes {#sec-ta-0-5}

Una de las ideas constructivas centrales de este tratado aparece aquí por primera vez. Con frecuencia un objeto que deseamos construir admite **muchas representaciones**. En lugar de escoger arbitrariamente una de ellas, declaramos equivalentes las representaciones que expresan el mismo contenido y hacemos del conjunto de todas ellas un único objeto nuevo.

El esquema es

$$
\text{representaciones}
\longrightarrow
\text{relación de equivalencia}
\longrightarrow
\text{clases}
\longrightarrow
\text{cociente}.
$$

No se trata de una preparación ornamental. Los enteros se construirán a partir de pares de naturales, los racionales a partir de pares de enteros y una de nuestras construcciones de los reales a partir de sucesiones de Cauchy. En cada caso, el paso decisivo será exactamente éste: identificar representaciones distintas sin escoger un representante privilegiado.

En toda esta sección, $\sim$ denota una relación de equivalencia sobre un conjunto $A$.

### Definición 0.5.1 — Clase de equivalencia {#ta-clase-equivalencia}

*Glosario: [clase de equivalencia](../otros/tratado-de-analisis-glosario.md#gl-clase-equivalencia) · [representante](../otros/tratado-de-analisis-glosario.md#gl-representante)*

Para $a\in A$, definimos la clase de equivalencia de $a$ por

$$
[a]_{\sim}
:=
\{x\in A:x\sim a\}.
$$

Cuando no haya riesgo de ambigüedad, escribiremos simplemente $[a]$.

---

### Proposición 0.5.2 — Existencia y pertenencia del representante {#ta-representante-clase}

*Glosario: [representante](../otros/tratado-de-analisis-glosario.md#gl-representante)*

Para todo $a\in A$, la clase $[a]$ es un conjunto, satisface $[a]\subseteq A$ y contiene a $a$.

**Demostración.**  
La existencia y la inclusión $[a]\subseteq A$ se siguen de la definición por separación. Como $\sim$ es reflexiva, $a\sim a$; por Definición 0.5.1, $a\in[a]$. ∎

---

### Lema 0.5.3 — Igualdad de clases {#ta-igualdad-clases}

*Glosario: [igualdad de clases](../otros/tratado-de-analisis-glosario.md#gl-igualdad-clases)*

Para $a,b\in A$,

$$
[a]=[b]
\quad\Longleftrightarrow\quad
a\sim b.
$$

**Demostración.**  
Si $[a]=[b]$, entonces $a\in[a]=[b]$ por Proposición 0.5.2; por la definición de $[b]$, $a\sim b$.

Recíprocamente, supongamos $a\sim b$. Sea $x\in[a]$. Entonces $x\sim a$. Como $a\sim b$ y $\sim$ es transitiva, $x\sim b$, luego $x\in[b]$. Por tanto $[a]\subseteq[b]$.

Por simetría, $b\sim a$, y el mismo argumento da $[b]\subseteq[a]$. Aplicando Teorema 0.2.4, $[a]=[b]$. ∎

---

### Proposición 0.5.4 — Clases iguales o disjuntas
Para $a,b\in A$, o bien $[a]=[b]$, o bien $[a]$ y $[b]$ son disjuntas.

**Demostración.**  
Supongamos que $[a]\cap[b]\neq\varnothing$. Entonces existe $x$ con $x\in[a]$ y $x\in[b]$. Por definición,

$$
x\sim a,
\qquad
x\sim b.
$$

Por simetría, $a\sim x$; por transitividad con $x\sim b$, $a\sim b$. Por Lema 0.5.3, $[a]=[b]$.

La contrapositiva afirma que, si $[a]\neq[b]$, entonces $[a]\cap[b]=\varnothing$. ∎

---

### Definición 0.5.5 — Partición {#ta-particion}

*Glosario: [partición](../otros/tratado-de-analisis-glosario.md#gl-particion)*

Una **partición** de un conjunto $A$ es un conjunto $\mathscr P$ de subconjuntos de $A$ tal que:

1. $\varnothing\notin\mathscr P$;
2. si $C,D\in\mathscr P$ y $C\neq D$, entonces $C\cap D=\varnothing$;
3. todo $a\in A$ pertenece a algún $C\in\mathscr P$.

---

### Teorema 0.5.6 — Las clases de equivalencia forman una partición
El conjunto de todas las clases de equivalencia de $\sim$ forma una partición de $A$.

**Demostración.**  
Consideremos

$$
\mathscr P_{\sim}
:=
\{C\in\mathcal P(A):\exists a\in A\;(C=[a])\}.
$$

Existe por conjunto potencia y separación.

Por Proposición 0.5.2, cada $[a]$ contiene a $a$, luego ninguna clase es vacía.

Por Proposición 0.5.4, dos clases distintas son disjuntas.

Finalmente, para cada $a\in A$, el propio $a$ pertenece a $[a]$, y $[a]\in\mathscr P_{\sim}$.

Por Definición 0.5.5, $\mathscr P_{\sim}$ es una partición de $A$. ∎

---

Las proposiciones anteriores muestran que las clases no se solapan parcialmente: dos de ellas son iguales o disjuntas, y juntas recubren $A$. Estamos, por tanto, en condiciones de dejar de mirar las representaciones individuales y considerar **el conjunto de las clases mismas**. Ese nuevo conjunto es el cociente.

### Definición 0.5.7 — Conjunto cociente {#ta-conjunto-cociente}

*Glosario: [conjunto cociente](../otros/tratado-de-analisis-glosario.md#gl-conjunto-cociente)*

Definimos el **conjunto cociente** de $A$ por $\sim$ mediante

$$
A/{\sim}
:=
\{C\in\mathcal P(A):\exists a\in A\;(C=[a])\}.
$$

Equivalentemente,

$$
A/{\sim}=\{[a]:a\in A\}.
$$

La primera forma será considerada la definición conjuntista canónica; la segunda es notación descriptiva.

---

### Proposición 0.5.8 — Existencia del cociente
$A/{\sim}$ existe como conjunto y satisface

$$
A/{\sim}\subseteq\mathcal P(A).
$$

**Demostración.**  
Por Definición 0.5.7, $A/{\sim}$ se obtiene por separación dentro de $\mathcal P(A)$. ∎

---

::: {.callout-note title="Publicación progresiva"}
Esta entrega del capítulo comprende ya §§0.0–0.5. La siguiente incorporará **0.6 — Funciones** y continuará en el orden del manuscrito maestro.

El [**Glosario matemático del Tratado**](../otros/tratado-de-analisis-glosario.md) se actualiza en paralelo: esta incorporación añade **clase de equivalencia**, **representante**, **igualdad de clases**, **partición** y **conjunto cociente**.
:::
