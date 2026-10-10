### Nivel B — Aplicación directa: álgebra, desigualdades y estimaciones

::: {#exr-t1-0043}
<!-- CPM-T1-EXR-0043 | B | COMPUTATION | ABSOLUTE_VALUE | TRANSFER -->
**Ejercicio B1. Valor absoluto anidado.** Resuelve completamente

$$
\bigl||x-1|-2\bigr|\le1.
$$

Entrega el conjunto solución como unión de intervalos cerrados.
:::
::: {#exr-t1-0044}
<!-- CPM-T1-EXR-0044 | B | PROOF | ORIGINAL -->
**Ejercicio B2. Una estimación alrededor de $2$.** Supón que

$$
|x-2|<\frac1{10}.
$$

Demuestra, sin usar aproximaciones decimales, que

$$
|x^2-4|<\frac{41}{100}.
$$
:::

::: {#exr-t1-0045}
<!-- CPM-T1-EXR-0045 | B | PROOF | ORDER | QUOTIENTS | TRANSFER -->
**Ejercicio B3. La diferencia entre dos recíprocos.** Sean $a,b\ne0$.

1. Demuestra que
   $$
   a^{-1}-b^{-1}=\frac{b-a}{ab}.
   $$
2. Usa esta identidad, junto con las leyes de signo ya demostradas, para recuperar el hecho de que
   $$
   0<a<b
   \quad\Longrightarrow\quad
   \frac1b<\frac1a,
   $$
   sin citar directamente la parte 7 de @prp-t1-0007.
:::
::: {#exr-t1-0046}
<!-- CPM-T1-EXR-0046 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B4. Una elección arquimediana explícita.** Encuentra un natural $n$ que satisfaga simultáneamente

$$
n>200,
\qquad
\frac1n<\frac1{137}.
$$

Explica por qué tu elección funciona.
:::

::: {#exr-t1-0047}
<!-- CPM-T1-EXR-0047 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B5. Tres pasos de bisección para $\sqrt{10}$.** Comienza con $[3,4]$ y conserva en cada paso la mitad cerrada que contiene $\sqrt{10}$. Realiza tres bisecciones y entrega un intervalo racional final $[a,b]$ con

$$
a<\sqrt{10}<b.
$$

Justifica cada decisión comparando cuadrados.
:::

::: {#exr-t1-0048}
<!-- CPM-T1-EXR-0048 | B | PROOF | SIGNS | QUOTIENTS | TRANSFER -->
**Ejercicio B6. Regla de signos para un cociente.** Sean $a,b\ne0$. Demuestra, sin hacer una tabla memorizada, que

$$
\frac ab>0
\iff
(a>0\text{ y }b>0)\ \text{o}\ (a<0\text{ y }b<0),
$$

y que

$$
\frac ab<0
\iff
(a>0\text{ y }b<0)\ \text{o}\ (a<0\text{ y }b>0).
$$

Debes reducir el problema al signo de $b^{-1}$ y al teorema del signo de un producto.
:::
::: {#exr-t1-0049}
<!-- CPM-T1-EXR-0049 | B | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio B7. Inecuación racional con valor absoluto I.** Resuelve completamente

$$
\left|\frac{x-1}{x+2}\right|
\le
\frac{|x-3|}{2}.
$$

Tu solución debe registrar dominio, puntos críticos, transformación algebraica equivalente, análisis de signos y verificación de extremos.
:::

### Nivel C — Combinación estructural: cuerpo ordenado, cotas y completitud

::: {#exr-t1-0050}
<!-- CPM-T1-EXR-0050 | C | PROOF | ORIGINAL -->
**Ejercicio C1. Escalar un supremo por un número positivo.** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, y sea $c>0$. Define

$$
cA=\{ca:a\in A\}.
$$

Demuestra que

$$
\sup(cA)=c\sup A.
$$
:::

::: {#exr-t1-0051}
<!-- CPM-T1-EXR-0051 | C | PROOF | ORIGINAL -->
**Ejercicio C2. El ínfimo como supremo reflejado.** Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente, y define

$$
-A=\{-a:a\in A\}.
$$

Demuestra que

$$
\inf A=-\sup(-A).
$$
:::

::: {#exr-t1-0052}
<!-- CPM-T1-EXR-0052 | C | PROOF | DENSITY | SYNTHESIS | TRANSFER -->
**Ejercicio C3. Alternar racionales e irracionales.** Sean $a<b$ y $N\in\mathbb N_{>0}$. Demuestra que existen racionales $q_1,\dots,q_N$ e irracionales $\xi_1,\dots,\xi_N$ tales que

$$
a<q_1<\xi_1<q_2<\xi_2<\cdots<q_N<\xi_N<b.
$$

No basta afirmar que ambos conjuntos son densos: organiza una construcción que garantice simultáneamente todo el orden indicado.
:::
::: {#exr-t1-0053}
<!-- CPM-T1-EXR-0053 | C | PROOF | EXISTENCE_UNIQUENESS | TRANSFER -->
**Ejercicio C4. Una ecuación afín completa.** Sean $a,b,c\in F$, donde $F$ es un cuerpo y $a\ne0$. Considera

$$
ax+b=c.
$$

1. Construye un candidato explícito para $x$.
2. Verifica que satisface la ecuación.
3. Demuestra que ninguna otra solución es posible.

La solución debe combinar las dos ecuaciones elementales del capítulo; no basta escribir una cadena escolar de «pasar términos».
:::
::: {#exr-t1-0054}
<!-- CPM-T1-EXR-0054 | C | PROOF | ORIGINAL -->
**Ejercicio C5. Producto de raíces cuadradas.** Sean $a,b\ge0$. Utiliza el teorema de existencia y unicidad de raíces cuadradas para demostrar

$$
\sqrt{ab}=\sqrt a\,\sqrt b.
$$
:::

::: {#exr-t1-0055}
<!-- CPM-T1-EXR-0055 | C | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio C6. Inecuación racional con valor absoluto II.** Resuelve completamente

$$
\frac{|x-2|}{|x+1|}\ge\frac{|x|}{2}.
$$

Debes identificar el dominio, todos los puntos críticos relevantes y justificar cualquier operación de elevar al cuadrado.
:::

::: {#exr-t1-0056}
<!-- CPM-T1-EXR-0056 | C | PROOF | NESTED_INTERVALS | SYNTHESIS | TRANSFER -->
**Ejercicio C7. Dos cadenas encajadas que no pueden terminar en puntos distintos.** Sean $(I_n)$ y $(J_n)$ dos familias de intervalos cerrados, no vacíos y encajados. Supón que las longitudes de ambas familias pueden hacerse menores que cualquier $\varepsilon>0$ y que

$$
I_n\cap J_n\ne\varnothing
\qquad
\text{para todo }n.
$$

Demuestra que las dos familias tienen el **mismo** único punto común.
:::
