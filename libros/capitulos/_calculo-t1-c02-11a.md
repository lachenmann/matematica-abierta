## Ejercicios y soluciones {#sec-t1-c02-11}

Llegamos al bloque de práctica sistemática de `T1-C02`. Hasta aquí las herramientas aparecieron acompañadas por motivación, estrategias modelo y laboratorios guiados. En esta sección disminuye deliberadamente la ayuda: el lector debe decidir qué parte de la estructura de $\mathbb R$ es pertinente y justificar cada dependencia.

El banco contiene exactamente cuarenta ejercicios, organizados en siete niveles.

| Nivel | Función principal | Cantidad |
|---|---|---:|
| A | reconocimiento estructural, definiciones e intervalos | 7 |
| B | aplicación directa: álgebra, desigualdades y estimaciones | 7 |
| C | combinación estructural: cuerpo ordenado, cotas y completitud | 7 |
| D | hipótesis esenciales, reversibilidad y diagnóstico | 6 |
| E | contraejemplos y fronteras de los teoremas | 5 |
| F | descubrimiento guiado | 5 |
| G | síntesis y desafío | 3 |
| **Total** |  | **40** |

El banco reabierto incorpora explícitamente la nueva capa axiomática de §2.2. A lo largo de los niveles A--F aparecerán tareas de clasificación **axioma / definición / resultado demostrado**, unicidad, reglas de signos, cancelación y producto nulo, existencia y unicidad de ecuaciones, diagnóstico de división por cero y reconstrucción de una prueba directamente desde `C1--C9`. Esta incorporación se hace sin retirar la cobertura de completitud, densidad, bisección ni las tres inecuaciones racionales avanzadas.

Todos los ejercicios pueden resolverse usando únicamente `T1-C01`, este capítulo y álgebra escolar. No es necesario —ni está permitido en las soluciones canónicas— invocar convergencia de sucesiones, límites, continuidad, teorema del valor intermedio, Bolzano–Weierstrass o resultados posteriores.

::: {.callout-tip title="Cómo trabajar esta sección"}
Antes de consultar una solución, deja por escrito cuatro cosas:

1. qué se supone y cuál es el dominio;
2. qué debe demostrarse, construirse o calcularse;
3. qué resultado previo parece pertinente;
4. si ese resultado depende directamente de completitud o solo de estructura de cuerpo ordenado.

En una inecuación racional añade una quinta pregunta: **¿qué puntos están excluidos o pueden cambiar la forma algebraica del problema?**
:::

### Nivel A — Reconocimiento estructural, definiciones e intervalos

::: {#exr-t1-0036}
<!-- CPM-T1-EXR-0036 | A | CONCEPTUAL | GEOMETRY | ORIGINAL -->
**Ejercicio A1. Cuatro lenguajes para la misma región.** Escribe el conjunto

$$
\{x\in\mathbb R:|x-3|<2\}
$$

de tres maneras adicionales: como desigualdad doble, como intervalo y como afirmación verbal de distancia.
:::

::: {#exr-t1-0037}
<!-- CPM-T1-EXR-0037 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. Multiplicar desigualdades.** Decide qué puede concluirse de $a<b$ en cada caso y justifica la dirección de la desigualdad:

1. $c>0$;
2. $c<0$;
3. $c=0$.

Compara $ac$ y $bc$.
:::

::: {#exr-t1-0038}
<!-- CPM-T1-EXR-0038 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A3. Cota, máximo y supremo.** Sea $A=(0,4)$. Decide si cada afirmación es verdadera o falsa y justifica brevemente:

1. $5$ es cota superior de $A$;
2. $4$ es cota superior de $A$;
3. $4$ es máximo de $A$;
4. $\sup A=4$.
:::

::: {#exr-t1-0039}
<!-- CPM-T1-EXR-0039 | A | CONCEPTUAL | PROOF_AUDIT | RETROFIT_AXIOMATIC -->
**Ejercicio A4. Axioma, definición o resultado demostrado.** Clasifica cada afirmación en una de las categorías **axioma**, **definición** o **resultado demostrado**. Cuando corresponda, identifica el axioma `C1--C9` o el resultado de §2.2 que la respalda.

1. $a(b+c)=ab+ac$.
2. $a-b:=a+(-b)$.
3. $a0=0$.
4. Si $a\ne0$ y $ab=ac$, entonces $b=c$.
5. $a<b$ significa que $b-a$ es positivo.

Explica por qué confundir estas categorías puede ocultar una dependencia lógica en una demostración.
:::
::: {#exr-t1-0040}
<!-- CPM-T1-EXR-0040 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. ¿Cuándo puede aplicarse completitud?** Para cada conjunto indica si el axioma del supremo garantiza directamente la existencia de un supremo real:

1. $(0,1)$;
2. $\mathbb N$;
3. $\varnothing$;
4. $\{-3,7,10\}$.

No se pide calcular el supremo cuando exista; se pide auditar las hipótesis del axioma.
:::

::: {#exr-t1-0041}
<!-- CPM-T1-EXR-0041 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A6. Dependencia estructural.** Clasifica cada hecho según dependa de **cuerpo ordenado**, **completitud directamente** o **una consecuencia previa de completitud**:

1. $|x+y|\le |x|+|y|$;
2. todo conjunto no vacío acotado superiormente tiene supremo;
3. para todo $\varepsilon>0$ existe $n$ con $1/n<\varepsilon$;
4. entre dos reales distintos hay un racional.
:::

::: {#exr-t1-0042}
<!-- CPM-T1-EXR-0042 | A | CONCEPTUAL | GEOMETRY | ORIGINAL -->
**Ejercicio A7. Intervalos encajados.** Considera

$$
I_n=\left[1-\frac1{n+1},\,1+\frac1{n+1}\right].
$$

1. Verifica que $I_{n+1}\subseteq I_n$.
2. Comprueba que $1\in I_n$ para todo $n$.
3. Explica por qué el principio de intervalos encajados garantiza una intersección no vacía, sin afirmar todavía que $1$ sea el único punto común.
:::

### Nivel B — Aplicación directa: álgebra, desigualdades y estimaciones

::: {#exr-t1-0043}
<!-- CPM-T1-EXR-0043 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Valor absoluto como intervalo.** Resuelve

$$
|2x-5|<3.
$$
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
<!-- CPM-T1-EXR-0045 | B | PROOF | AXIOMATIC | RETROFIT_AXIOMATIC -->
**Ejercicio B3. La unicidad no viene incluida en el axioma.** Sea $F$ un cuerpo y sea $a\in F$. Supón que $b,c\in F$ satisfacen

$$
a+b=0,
\qquad
a+c=0.
$$

Demuestra directamente que $b=c$. En tu cadena de igualdades indica dónde utilizas asociatividad, conmutatividad y la propiedad del neutro aditivo.

