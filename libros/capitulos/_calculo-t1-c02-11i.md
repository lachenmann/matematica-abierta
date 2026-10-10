#### Soluciones del nivel G

::: {#sol-t1-0073}
<!-- CPM-T1-SOL-0073 -->
**Solución G1.**

Sea

$$
\alpha=\sup A,
\qquad
\beta=\sup B.
$$

Primero comprobamos que $\alpha+\beta$ es cota superior de $A+B$. Si $a\in A$ y $b\in B$, entonces

$$
a\le\alpha,
\qquad
b\le\beta,
$$

y sumando,

$$
a+b\le\alpha+\beta.
$$

Ahora debemos demostrar que ninguna cota menor funciona. Sea $\varepsilon>0$. Por la caracterización aproximativa del supremo existen $a\in A$ y $b\in B$ tales que

$$
\alpha-\frac\varepsilon2<a\le\alpha,
$$

$$
\beta-\frac\varepsilon2<b\le\beta.
$$

Sumando,

$$
\alpha+\beta-\varepsilon<a+b\le\alpha+\beta.
$$

Como $a+b\in A+B$, la caracterización aproximativa vuelve a decir que

$$
\boxed{\sup(A+B)=\alpha+\beta=\sup A+\sup B.}
$$

La completitud interviene para garantizar la existencia de $\alpha$ y $\beta$; el resto es orden y la caracterización del supremo.
:::

::: {#sol-t1-0074}
<!-- CPM-T1-SOL-0074 -->
**Solución G2.**

La condición de separación es

$$
\ell<u
\qquad
\text{para todo }\ell\in L\text{ y todo }u\in U.
$$

Como $U\ne\varnothing$, elegimos $u_0\in U$. Para todo $\ell\in L$,

$$
\ell<u_0,
$$

de modo que $u_0$ es cota superior de $L$. Como $L\ne\varnothing$, completitud garantiza

$$
c=\sup L.
$$

Por definición de supremo,

$$
\ell\le c
$$

para todo $\ell\in L$.

Por otro lado, cada $u\in U$ es cota superior de $L$, porque todo $\ell\in L$ satisface $\ell<u$. Como $c$ es la menor cota superior,

$$
c\le u
$$

para todo $u\in U$.

Así,

$$
\boxed{\ell\le c\le u}
$$

para todos $\ell\in L$, $u\in U$.

Como $L\cup U=\mathbb R$, el real $c$ pertenece a uno de los dos conjuntos. Son disjuntos, así que pertenece exactamente a uno.

- Si $c\in L$, como $c$ domina a todo elemento de $L$, tenemos $c=\max L$.
- Si $c\in U$, como $c\le u$ para todo $u\in U$, tenemos $c=\min U$.

Por tanto ocurre exactamente una de las dos posibilidades:

$$
\boxed{c=\max L\quad\text{o}\quad c=\min U.}
$$

Esta propiedad traduce completitud en lenguaje de cortes: una separación ordenada de la recta posee un punto frontera real.
:::

::: {#sol-t1-0075}
<!-- CPM-T1-SOL-0075 -->
**Solución G3.**

Sea $a>0$ y

$$
S=\{x\ge0:x^3<a\}.
$$

La estrategia replica, con un grado algebraico mayor, la construcción de raíces cuadradas: completitud produce un candidato frontera y dos perturbaciones descartan que su cubo quede por debajo o por encima de $a$.

**1. No vacuidad y acotación.**

El número

$$
t=\frac{a}{1+a}
$$

es positivo y pertenece a $S$. En efecto, si $a\ge1$, entonces $0<t<1$ y $t^3<1\le a$; si $0<a<1$, entonces $0<t<a<1$, por lo que $t^3<a^3<a$.

Además, $a+1$ es cota superior de $S$. Si $x\ge a+1$, entonces $x>1$ y $x>a$ cuando $a<1$, o $x>a\ge1$ cuando $a\ge1$; en ambos casos $x^3>a$, de modo que tal $x$ no pertenece a $S$.

Por completitud existe

$$
\alpha=\sup S.
$$

Como $t\in S$ y $t>0$, tenemos $\alpha>0$.

**2. No puede ocurrir $\alpha^3<a$.**

Supongamos

$$
\alpha^3<a
$$

y definamos

$$
\delta=a-\alpha^3>0.
$$

Elegimos

$$
h=\frac12\min\left\{1,\frac{\delta}{3\alpha^2+3\alpha+1}\right\}>0.
$$

Entonces $h<1$ y

$$
h(3\alpha^2+3\alpha+1)<\delta.
$$

Como $h<1$,

$$
3\alpha h\le3\alpha,
\qquad
h^2<1,
$$

y por tanto

$$
\begin{aligned}
(\alpha+h)^3
&=\alpha^3+h(3\alpha^2+3\alpha h+h^2)\\
&<\alpha^3+h(3\alpha^2+3\alpha+1)\\
&<\alpha^3+\delta\\
&=a.
\end{aligned}
$$

Así $\alpha+h\in S$, pero $\alpha+h>\alpha$, contradiciendo que $\alpha$ sea cota superior.

**3. No puede ocurrir $\alpha^3>a$.**

Supongamos ahora

$$
\alpha^3>a
$$

y pongamos

$$
\delta=\alpha^3-a>0.
$$

Elegimos

$$
h=\frac12\min\left\{\alpha,\frac{\delta}{3\alpha^2}\right\}>0
$$

y definimos

$$
c=\alpha-h.
$$

Como $h<\alpha$, $c>0$. Además,

$$
\alpha^3-c^3
=3\alpha^2h-3\alpha h^2+h^3.
$$

Como $0<h<\alpha$, el término

$$
-3\alpha h^2+h^3=h^2(h-3\alpha)<0,
$$

de modo que

$$
\alpha^3-c^3<3\alpha^2h<\delta.
$$

Por tanto,

$$
c^3>\alpha^3-\delta=a.
$$

Si $x\in S$ y $x\ge c$, como $x,c\ge0$, la identidad

$$
x^3-c^3=(x-c)(x^2+xc+c^2)\ge0
$$

justifica directamente que $x^3\ge c^3>a$. Esto contradice la condición $x^3<a$ que define a $S$. Así todo $x\in S$ satisface $x<c$. Por tanto $c$ es una cota superior de $S$, pero

$$
c<\alpha,
$$

contradiciendo que $\alpha$ sea la menor cota superior.

Los dos casos estrictos son imposibles. Por tricotomía,

$$
\boxed{\alpha^3=a.}
$$

**4. Unicidad.**

Sean $0<u<v$. Entonces

$$
v^3-u^3=(v-u)(v^2+uv+u^2)>0.
$$

Así el cubo es estrictamente creciente sobre los reales no negativos. Por consiguiente, no pueden existir dos números no negativos distintos con cubo $a$.

Hemos demostrado, sin continuidad, que para todo $a>0$ existe un único $\alpha>0$ tal que

$$
\boxed{\alpha^3=a.}
$$

La prueba muestra de nuevo la arquitectura central del capítulo:

$$
\boxed{
\text{conjunto de aproximantes}
\to
\text{supremo}
\to
\text{perturbaciones}
\to
\text{identificación de la frontera}.
}
$$
:::

### Auditoría del banco

Antes de cerrar el capítulo, conviene verificar el contrato de esta sección.

- Ejercicios publicados: **40**.
- Soluciones publicadas: **40**.
- Correspondencia `EXR-0036--0075` / `SOL-0036--0075`: **completa**.
- Distribución A–G: $7+7+7+6+5+5+3=40$.
- Tipologías `CONCEPTUAL`, `PROOF`, `COUNTEREXAMPLE`, `DISCOVERY`, `SYNTHESIS` y `GEOMETRY`: presentes.
- Inecuaciones racionales con valor absoluto de alta complejidad: **3**, en B7, C6 y D5.
- Reproducciones literales de demostraciones ya resueltas en el desarrollo: **eliminadas del banco**. Cuando una idea reaparece, exige transferencia, generalización, diagnóstico o combinación de herramientas.
- Capa axiomática: clasificación axioma/definición/resultado (A4), identidad y orden de recíprocos (B3), signo de cocientes (B6), ecuación afín con existencia y unicidad (C4), cancelación con solución perdida (D2), división por cero (E3) y reconstrucción estructural de $(-1)a=-a$ (F5).
- Transferencias de completitud: supremos bajo unión y traslación, eliminación finita de puntos, transporte del hueco racional, intervalos racionales encajados y propiedad de corte.
- Problemas F: traslación del supremo, elección arquimediana simultánea, densidad con control de denominador, presupuesto de bisección y reconstrucción axiomática: **5/5**.
- Problemas G de síntesis: suma de conjuntos, propiedad de corte y construcción de una raíz cúbica mediante supremo: **3/3**.
- Dependencias de `T1-C03` o posteriores: **ninguna**.

La política pedagógica del banco queda así alineada con la progresión del capítulo: **primero modelar la justificación, después retirar el andamiaje y exigir transferencia**.
