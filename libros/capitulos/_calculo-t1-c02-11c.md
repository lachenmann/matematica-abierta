### Nivel D — Hipótesis esenciales, reversibilidad y diagnóstico

::: {#exr-t1-0057}
<!-- CPM-T1-EXR-0057 | D | CONCEPTUAL | COUNTEREXAMPLE | SUPREMUM | TRANSFER -->
**Ejercicio D1. Supremo de una unión: diagnosticar una fórmula falsa.** Sean $A,B\subseteq\mathbb R$ no vacíos y acotados superiormente. Un estudiante afirma

$$
\sup(A\cup B)=\sup A+\sup B.
$$

1. Da un contraejemplo.
2. Formula la identidad correcta.
3. Demuéstrala a partir de la definición de supremo.
:::
::: {#exr-t1-0058}
<!-- CPM-T1-EXR-0058 | D | CONCEPTUAL | CANCELLATION | DIAGNOSIS | TRANSFER -->
**Ejercicio D2. Cancelar puede borrar una solución.** Resuelve en un cuerpo ordenado

$$
(x-1)(x+2)=(x-1)(3x-4).
$$

Un estudiante cancela inmediatamente el factor $x-1$ y obtiene una sola solución. Explica por qué ese procedimiento es incompleto y determina **todas** las soluciones.
:::
::: {#exr-t1-0059}
<!-- CPM-T1-EXR-0059 | D | PROOF | SUPREMUM | FINITE_DELETION | TRANSFER -->
**Ejercicio D3. ¿Eliminar finitos puntos cambia el supremo?** Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, sea $F\subseteq A$ finito y supón $A\setminus F\ne\varnothing$. Un estudiante afirma:

> «Eliminar finitos puntos nunca cambia el supremo».

1. Da un contraejemplo.
2. Demuestra que la afirmación sí es correcta bajo la hipótesis adicional
   $$
   \sup A\notin F.
   $$
:::
::: {#exr-t1-0060}
<!-- CPM-T1-EXR-0060 | D | CONCEPTUAL | NESTED_INTERVALS | INCOMPLETENESS | TRANSFER -->
**Ejercicio D4. Intervalos racionales encajados alrededor de un punto que no es racional.** Parte de $I_0=[1,2]$ y aplica bisección conservando siempre la mitad cerrada que contiene a $\sqrt2$.

1. Explica por qué todos los extremos de $I_n$ son racionales.
2. Demuestra que las longitudes son $2^{-n}$.
3. Explica por qué
   $$
   \bigcap_n I_n=\{\sqrt2\}
   $$
   como subconjuntos de $\mathbb R$.
4. Concluye que, vistos como intervalos de $\mathbb Q$, tienen intersección vacía.

Explica por qué este fenómeno muestra que densidad y completitud son propiedades diferentes.
:::
::: {#exr-t1-0061}
<!-- CPM-T1-EXR-0061 | D | COMPUTATION | SYNTHESIS | ORIGINAL -->
**Ejercicio D5. Inecuación racional con valor absoluto III.** Resuelve completamente

$$
\frac{|x-2|+|x+1|}{|x-1|}\le3.
$$

La solución debe separar todos los casos determinados por los argumentos de los valores absolutos y por el punto excluido del denominador.
:::

::: {#exr-t1-0062}
<!-- CPM-T1-EXR-0062 | D | CONCEPTUAL | ORIGINAL -->
**Ejercicio D6. Una prueba correcta en otro momento, pero circular aquí.** Un estudiante propone demostrar la existencia de $\sqrt3$ así:

> «La función $x^2$ es continua; como $1^2<3<2^2$, el teorema del valor intermedio produce un $c\in(1,2)$ con $c^2=3$».

Explica por qué este argumento no es admisible dentro de este capítulo, aunque llegará a ser matemáticamente válido más adelante. Indica cuál es la dependencia correcta en este capítulo.
:::

### Nivel E — Contraejemplos y fronteras de los teoremas

::: {#exr-t1-0063}
<!-- CPM-T1-EXR-0063 | E | COUNTEREXAMPLE | ENDPOINTS | TRANSFER -->
**Ejercicio E1. Cuatro comportamientos con la misma frontera superior.** Construye cuatro subconjuntos no vacíos y acotados de $\mathbb R$, todos con supremo $1$, que presenten respectivamente estos comportamientos:

1. tienen máximo y mínimo;
2. no tienen máximo, pero sí mínimo;
3. tienen máximo, pero no mínimo;
4. no tienen ni máximo ni mínimo.

Justifica cada elección.
:::
::: {#exr-t1-0064}
<!-- CPM-T1-EXR-0064 | E | COUNTEREXAMPLE | ONE_SIDED_BOUNDS | TRANSFER -->
**Ejercicio E2. El mismo supremo con comportamientos inferiores opuestos.** Encuentra dos conjuntos $A,B\subseteq\mathbb R$ tales que

$$
\sup A=\sup B=0,
$$

pero $A$ esté acotado inferiormente y $B$ no. Determina además si existe $\inf A$ y explica por qué $B$ no posee ínfimo real.
:::
::: {#exr-t1-0065}
<!-- CPM-T1-EXR-0065 | E | COUNTEREXAMPLE | DIAGNOSIS | RETROFIT_AXIOMATIC -->
**Ejercicio E3. La división por cero no es una simplificación pendiente.** Un estudiante escribe

$$
0x=0
\quad\Longrightarrow\quad
x=\frac00
\quad\Longrightarrow\quad
x=1,
$$

invocando informalmente la regla $a/a=1$.

Refuta el argumento de dos maneras complementarias:

1. demuestra que la ecuación $0x=0$ tiene **todos** los elementos del cuerpo como soluciones;
2. explica desde la definición de división por qué $0/0$ no está definido y por qué la identidad $a/a=1$ exige $a\ne0$.

Identifica exactamente el primer paso ilegítimo de la cadena.
:::
::: {#exr-t1-0066}
<!-- CPM-T1-EXR-0066 | E | COUNTEREXAMPLE | NESTED_INTERVALS | TRANSFER -->
**Ejercicio E4. Cerrados y cada vez más pequeños, pero no encajados.** Construye una familia de intervalos cerrados y no vacíos $I_n$ tal que

1. sus longitudes puedan hacerse menores que cualquier $\varepsilon>0$;
2. $\bigcap_n I_n=\varnothing$;
3. la razón del fracaso sea exactamente que la familia **no** es encajada.

Explica por qué esto no contradice el principio de intervalos encajados.
:::
::: {#exr-t1-0067}
<!-- CPM-T1-EXR-0067 | E | COUNTEREXAMPLE | INCOMPLETENESS | AFFINE_TRANSFER -->
**Ejercicio E5. Transportar el hueco racional.** Sea

$$
S_{\mathbb Q}=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

y define

$$
T=\{2q+1:q\in S_{\mathbb Q}\}\subseteq\mathbb Q.
$$

1. Demuestra que $T$ es no vacío y está acotado superiormente en $\mathbb Q$.
2. Demuestra que $T$ no tiene supremo racional.

La segunda parte debe reducir un supuesto $\sup_{\mathbb Q}T$ a un supuesto supremo racional de $S_{\mathbb Q}$.
:::
