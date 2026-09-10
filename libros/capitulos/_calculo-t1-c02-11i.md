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

Si $x\in S$ y $x\ge c$, como $x,c\ge0$, la monotonía algebraica del cubo en los no negativos da

$$
x^3\ge c^3>a,
$$

contradicción. Así todo $x\in S$ satisface $x<c$. Por tanto $c$ es una cota superior de $S$, pero

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
- Cobertura del retrofit axiomático: **8/8 objetivos** — clasificación axioma/definición/resultado (A4), unicidad (B3), regla de signos (B6), existencia/unicidad de ecuaciones (C4), cancelación y producto nulo (D2), división por cero (E3), reconstrucción desde `C1--C9` (F5) y manipulación de desigualdades según signo (A2 + B7/C6/D5).
- Problemas F obligatorios: caracterización del supremo, elección arquimediana, densidad, bisección y reconstrucción axiomática de $a0=0$: **5/5**. La necesidad del cierre permanece cubierta explícitamente en E4.
- Problemas G de síntesis: suma de conjuntos, propiedad de corte y construcción de una raíz cúbica mediante supremo: **3/3**.
- Dependencias de `T1-C03` o posteriores: **ninguna**.

La auditoría final integral `T1_C02_FINAL_AUDIT_v02` recontroló de manera independiente estos recuentos, las dependencias y los problemas algebraicamente delicados. El veredicto es **PASS**; el capítulo queda nuevamente cerrado como `COMPLETE`.


