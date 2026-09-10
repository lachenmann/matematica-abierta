No cites simplemente la unicidad de los inversos: reconstruye la prueba desde los axiomas de cuerpo.
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
<!-- CPM-T1-EXR-0048 | B | PROOF | AXIOMATIC | RETROFIT_AXIOMATIC -->
**Ejercicio B6. Fabricar una regla de signos.** Sean $a,b\in F$, donde $F$ es un cuerpo. Demuestra que

$$
(-a)b=-(ab).
$$

La estrategia debe ser estructural: prueba primero que $(-a)b$ es un inverso aditivo de $ab$ y concluye por unicidad. Señala dónde intervienen distributividad, conmutatividad y el hecho ya demostrado de que $b0=0$.
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
<!-- CPM-T1-EXR-0052 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C3. Dos tipos de números dentro de cualquier intervalo.** Sean $a<b$. Demuestra que existe un racional $q$ y un irracional $\xi$ tales que

$$
a<q<\xi<b.
$$
:::

::: {#exr-t1-0053}
<!-- CPM-T1-EXR-0053 | C | PROOF | EXISTENCE_UNIQUENESS | RETROFIT_AXIOMATIC -->
**Ejercicio C4. Despejar significa demostrar existencia y unicidad.** Sean $a,b\in F$, con $F$ un cuerpo. Considera la ecuación

$$
a+x=b.
$$

1. Construye explícitamente un candidato $x_0$ usando el inverso aditivo de $a$ y demuestra que satisface la ecuación.
2. Si $y$ es cualquier otra solución, demuestra que $y=x_0$.
3. Explica qué parte es una prueba de **existencia** y qué parte es una prueba de **unicidad**.

No basta escribir «restamos $a$ en ambos miembros»: debes traducir esa operación a suma e inverso aditivo.
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
<!-- CPM-T1-EXR-0056 | C | PROOF | ORIGINAL -->
**Ejercicio C7. Un criterio de unicidad para intervalos encajados.** Sean

$$
I_n=[a_n,b_n]
$$
intervalos cerrados, no vacíos y encajados. Supón además que para todo $\varepsilon>0$ existe $N$ tal que

$$
b_N-a_N<\varepsilon.
$$

Demuestra que $\bigcap_n I_n$ contiene exactamente un punto.
:::

### Nivel D — Hipótesis esenciales, reversibilidad y diagnóstico

::: {#exr-t1-0057}
<!-- CPM-T1-EXR-0057 | D | CONCEPTUAL | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D1. El supremo no tiene que estar dentro.** Un estudiante afirma:

> «Si $s=\sup A$, entonces $s\in A$».

Explica el error, da un contraejemplo y formula una condición adicional sencilla que sí garantice $s=\max A$.
:::

::: {#exr-t1-0058}
<!-- CPM-T1-EXR-0058 | D | CONCEPTUAL | COUNTEREXAMPLE | PROOF | RETROFIT_AXIOMATIC -->
**Ejercicio D2. Cancelar exige una hipótesis.** Un estudiante afirma:

> «De $ab=ac$ siempre se sigue $b=c$; basta cancelar $a$».

1. Construye un contraejemplo con $a=0$ que refute la afirmación.
2. Formula la ley correcta de cancelación multiplicativa e identifica la hipótesis que faltaba.
3. Usando **solo** esa ley de cancelación, el hecho $a0=0$ y una separación de casos $a=0$ / $a\ne0$, reconstruye la implicación
   $$
   ab=0\Longrightarrow a=0\ \text{o}\ b=0.
   $$
4. Demuestra también la implicación recíproca y concluye la regla del producto nulo.

No cites la regla del producto nulo para probarse a sí misma.
:::
::: {#exr-t1-0059}
<!-- CPM-T1-EXR-0059 | D | CONCEPTUAL | ORIGINAL -->
**Ejercicio D3. Las dos hipótesis que no pueden borrarse.** Explica por qué el axioma de completitud no puede formularse correctamente como

> «Todo subconjunto de $\mathbb R$ tiene supremo real».

Da un ejemplo que muestre la necesidad de **no vacío** y otro que muestre la necesidad de **acotado superiormente**.
:::

::: {#exr-t1-0060}
<!-- CPM-T1-EXR-0060 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D4. Denso no significa completo.** Explica por qué el hecho de que $\mathbb Q$ sea denso en $\mathbb R$ no contradice que $\mathbb Q$ sea incompleto. Debes mencionar un conjunto racional concreto que exhiba el fracaso de completitud.
:::

::: {#exr-t1-0061}
<!-- CPM-T1-EXR-0061 | D | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio D5. Inecuación racional con valor absoluto III.** Resuelve completamente

$$
\frac{|x-2|+|x+1|}{|x-1|}\le3.
$$

