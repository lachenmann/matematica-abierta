### Nivel F — Descubrimiento guiado

::: {#exr-t1-0068}
<!-- CPM-T1-EXR-0068 | F | DISCOVERY | SUPREMUM | TRANSLATION | TRANSFER -->
**Ejercicio F1. Redescubrir el supremo de una traslación.** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, sea

$$
s=\sup A,
$$

y fija $c\in\mathbb R$. Define

$$
A+c=\{a+c:a\in A\}.
$$

Utiliza la **caracterización aproximativa** del supremo —no una fórmula previamente memorizada— para demostrar

$$
\boxed{\sup(A+c)=s+c}.
$$
:::
::: {#exr-t1-0069}
<!-- CPM-T1-EXR-0069 | F | DISCOVERY | ARCHIMEDEAN | FINITE_CONSTRAINTS | TRANSFER -->
**Ejercicio F2. Una sola elección para muchas exigencias.** Sean

$$
M_1,\dots,M_r\in\mathbb R
$$

y

$$
\varepsilon_1,\dots,\varepsilon_s>0,
$$

con $r,s\ge1$. Demuestra que existe un único natural elegido **una sola vez**, $n\in\mathbb N_{>0}$, que satisface simultáneamente

$$
n>M_i\quad(i=1,\dots,r)
$$

y

$$
\frac1n<\varepsilon_j\quad(j=1,\dots,s).
$$
:::
::: {#exr-t1-0070}
<!-- CPM-T1-EXR-0070 | F | DISCOVERY | DENSITY | DENOMINATOR_CONTROL | TRANSFER -->
**Ejercicio F3. Densidad racional con control del denominador.** Sean $a<b$ y $N\in\mathbb N_{>0}$. Demuestra que existen $m\in\mathbb Z$ y $n\in\mathbb N_{>0}$ tales que

$$
n>N
$$

y

$$
a<\frac mn<b.
$$

No basta citar densidad de $\mathbb Q$: debes adaptar su construcción para imponer además la cota inferior sobre el denominador.
:::
::: {#exr-t1-0071}
<!-- CPM-T1-EXR-0071 | F | DISCOVERY | BISECTION | ERROR_BUDGET | TRANSFER -->
**Ejercicio F4. Presupuesto de bisección sin calcular todos los puntos medios.** Parte de un intervalo de longitud $1$ que contiene a $\sqrt7$ y aplica bisección conservando siempre una mitad que contenga la raíz.

1. Demuestra por inducción que después de $n$ bisecciones la longitud es $2^{-n}$.
2. Determina el menor $n$ que garantiza una longitud estrictamente menor que $1/100$.
3. Explica qué certificado de localización de $\sqrt7$ proporciona esa etapa, aunque no calcules sus extremos concretos.
:::
::: {#exr-t1-0072}
<!-- CPM-T1-EXR-0072 | F | DISCOVERY | AXIOMATIC | TRANSFER -->
**Ejercicio F5. Reconstruir $(-1)a=-a$ sin usar las reglas de signos.** Sea $F$ un cuerpo y $a\in F$.

Puedes utilizar la unicidad del inverso aditivo y el resultado ya demostrado $a0=0$, pero **no** las identidades $(-a)b=-(ab)$ ni $a(-b)=-(ab)$.

1. Demuestra que $(-1)a$ es un inverso aditivo de $a$.
2. Concluye que
   $$
   (-1)a=-a.
   $$
3. Particulariza el resultado para deducir
   $$
   (-1)(-1)=1.
   $$

Identifica dónde intervienen distributividad, conmutatividad y unicidad.
:::
### Nivel G — Síntesis y desafío

::: {#exr-t1-0073}
<!-- CPM-T1-EXR-0073 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G1. Supremo de una suma de conjuntos.** Sean $A,B\subseteq\mathbb R$ no vacíos y acotados superiormente. Define

$$
A+B=\{a+b:a\in A,\ b\in B\}.
$$

Demuestra que

$$
\boxed{\sup(A+B)=\sup A+\sup B.}
$$
:::

::: {#exr-t1-0074}
<!-- CPM-T1-EXR-0074 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G2. Una propiedad de corte obtenida de completitud.** Sean $L,U\subseteq\mathbb R$ no vacíos, disjuntos, con

$$
L\cup U=\mathbb R,
$$

y supón que

$$
\ell<u
\qquad
\text{para todo }\ell\in L,\ u\in U.
$$

1. Demuestra que $L$ está acotado superiormente.
2. Sea $c=\sup L$. Demuestra que
   $$
   \ell\le c\le u
   $$
   para todo $\ell\in L$ y $u\in U$.
3. Como $c\in L\cup U$, demuestra que ocurre exactamente una de estas dos posibilidades: $c=\max L$ o $c=\min U$.

Esta es una forma elemental de propiedad de corte de la recta real.
:::

::: {#exr-t1-0075}
<!-- CPM-T1-EXR-0075 | G | PROOF | SYNTHESIS | DISCOVERY | ORIGINAL -->
**Ejercicio G3. Construir una raíz cúbica sin continuidad.** Sea $a>0$ y define

$$
S=\{x\in\mathbb R:x\ge0,\ x^3<a\}.
$$

1. Demuestra que $S$ es no vacío y está acotado superiormente.
2. Define $\alpha=\sup S$.
3. Demuestra, mediante perturbaciones algebraicas explícitas, que ni $\alpha^3<a$ ni $\alpha^3>a$ son posibles.
4. Concluye que existe un único $\alpha>0$ tal que $\alpha^3=a$.

No utilices continuidad ni el teorema del valor intermedio.
:::

