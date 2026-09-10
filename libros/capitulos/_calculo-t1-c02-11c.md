La solución debe separar todos los casos determinados por los argumentos de los valores absolutos y por el punto excluido del denominador.
:::

::: {#exr-t1-0062}
<!-- CPM-T1-EXR-0062 | D | CONCEPTUAL | ORIGINAL -->
**Ejercicio D6. Una prueba correcta en otro momento, pero circular aquí.** Un estudiante propone demostrar la existencia de $\sqrt3$ así:

> «La función $x^2$ es continua; como $1^2<3<2^2$, el teorema del valor intermedio produce un $c\in(1,2)$ con $c^2=3$».

Explica por qué este argumento no es admisible dentro de `T1-C02`, aunque llegará a ser matemáticamente válido más adelante. Indica cuál es la dependencia correcta en este capítulo.
:::

### Nivel E — Contraejemplos y fronteras de los teoremas

::: {#exr-t1-0063}
<!-- CPM-T1-EXR-0063 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E1. Acotado pero sin máximo.** Construye un subconjunto no vacío de $\mathbb R$ que esté acotado superiormente, tenga supremo y no tenga máximo. Justifica las tres afirmaciones.
:::

::: {#exr-t1-0064}
<!-- CPM-T1-EXR-0064 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. No acotado, sin supremo real.** Da un conjunto no vacío de reales que no tenga cota superior y demuestra que no puede tener supremo real.
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
<!-- CPM-T1-EXR-0066 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E4. Encajados y pequeños, pero abiertos.** Construye una familia de intervalos abiertos $J_n$ tal que

1. $J_{n+1}\subseteq J_n$;
2. sus longitudes puedan hacerse menores que cualquier $\varepsilon>0$;
3. $\bigcap_nJ_n=\varnothing$.

Explica qué hipótesis del principio de intervalos encajados falta.
:::

::: {#exr-t1-0067}
<!-- CPM-T1-EXR-0067 | E | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio E5. El axioma del supremo falla en $\mathbb Q$.** Exhibe un subconjunto no vacío de $\mathbb Q$ acotado superiormente en $\mathbb Q$ que no tenga supremo racional. Puedes reutilizar la arquitectura del ejemplo central del capítulo, pero debes explicar por qué ningún candidato racional puede funcionar.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0068}
<!-- CPM-T1-EXR-0068 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Redescubrir la caracterización del supremo.** Sea $A\neq\varnothing$ y sea $s$ una cota superior de $A$.

1. Supón que existe $\varepsilon_0>0$ tal que ningún $a\in A$ satisface $s-\varepsilon_0<a$. ¿Qué puedes decir de $s-\varepsilon_0$?
2. ¿Por qué eso es incompatible con que $s$ sea la menor cota superior?
3. Formula y demuestra el criterio resultante para reconocer que $s=\sup A$.
:::

::: {#exr-t1-0069}
<!-- CPM-T1-EXR-0069 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Una sola elección para ser grande y tener recíproco pequeño.** Dados $M\in\mathbb R$ y $\varepsilon>0$:

1. encuentra una condición única sobre $n\in\mathbb N$ que garantice simultáneamente $n>M$ y $1/n<\varepsilon$;
2. usa la propiedad arquimediana para demostrar que tal $n$ existe.
:::

::: {#exr-t1-0070}
<!-- CPM-T1-EXR-0070 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Reconstruir la densidad racional.** Sean $a<b$.

1. Elige $n\in\mathbb N_{>0}$ de modo que $1/n<b-a$.
2. Explica por qué entonces $nb-na>1$.
3. Usa el lema de encajonamiento entero para encontrar $m\in\mathbb Z$ con $na<m<nb$.
4. Concluye que $m/n\in(a,b)\cap\mathbb Q$.
:::

::: {#exr-t1-0071}
<!-- CPM-T1-EXR-0071 | F | DISCOVERY | GEOMETRY | SYNTHESIS | ORIGINAL -->
**Ejercicio F4. Diseñar una bisección para $\sqrt7$.** Parte del intervalo $[2,3]$.

1. Realiza cuatro bisecciones conservando la mitad que contiene $\sqrt7$.
2. Escribe los cinco intervalos, incluido el inicial.
3. Demuestra que el intervalo final tiene longitud $1/16$.
4. Explica qué teorema garantiza que una bisección indefinida determina un único punto común.
:::

::: {#exr-t1-0072}
<!-- CPM-T1-EXR-0072 | F | DISCOVERY | PROOF | AXIOMATIC | RETROFIT_AXIOMATIC -->
**Ejercicio F5. Reconstruir $a0=0$ desde `C1--C9`.** Sea $F$ un cuerpo y fija $a\in F$. No uses cancelación, producto nulo ni la regla $a0=0$ como resultado previo.

1. Usa el neutro aditivo para obtener una igualdad que relacione $0+0$ con $0$.
2. Multiplica ambos miembros por $a$ mediante sustitución de iguales en iguales.
3. Aplica distributividad para obtener una igualdad de la forma
   $$
   a0+a0=a0.
   $$
4. Suma el inverso aditivo de $a0$ a ambos miembros y usa asociatividad.
5. Concluye que $a0=0$ e identifica, paso por paso, qué axiomas de `C1--C9` fueron realmente necesarios.

El objetivo no es recordar la prueba de §2.2, sino reconstruir su arquitectura.
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

