## Ejercicios y soluciones {#sec-t1-c02-11}

Llegamos al bloque de práctica sistemática de este capítulo. Hasta aquí las herramientas aparecieron acompañadas por motivación, estrategias modelo y laboratorios guiados. En esta sección disminuye deliberadamente la ayuda: el lector debe decidir qué parte de la estructura de $\mathbb R$ es pertinente y justificar cada dependencia.

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

El banco ha sido depurado con una regla adicional: **no pedir como ejercicio la reproducción literal de una demostración que el desarrollo ya resolvió línea por línea**. Cuando reaparece una idea conocida, la tarea exige transferencia: combinarla con otra herramienta, generalizarla, diagnosticar una hipótesis, construir un contraejemplo o resolver una variante cuya estrategia no esté escrita de antemano.

Todos los ejercicios pueden resolverse usando los resultados demostrados en este capítulo, el principio de inducción aquí enunciado y el álgebra escolar. No es necesario —ni está permitido en las soluciones canónicas— invocar convergencia de sucesiones, límites, continuidad, teorema del valor intermedio, Bolzano–Weierstrass o resultados posteriores.

Las soluciones siguen también el cambio de régimen pedagógico del capítulo: citan por nombre los resultados ya establecidos y no expanden de nuevo asociatividad, neutros o sustituciones rutinarias, salvo cuando el propio ejercicio sea una auditoría axiomática.

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
<!-- CPM-T1-EXR-0036 | A | CONCEPTUAL | GEOMETRY | TRANSFER -->
**Ejercicio A1. Intersección de dos bandas de distancia.** Describe el conjunto

$$
S=\{x\in\mathbb R:|x-2|<3\text{ y }|x+1|\le2\}
$$

como una desigualdad compuesta y como un intervalo. Indica con cuidado qué extremos pertenecen al conjunto.
:::
::: {#exr-t1-0037}
<!-- CPM-T1-EXR-0037 | A | CONCEPTUAL | ORDER | TRANSFER -->
**Ejercicio A2. Tres transformaciones del mismo orden.** Supón

$$
0<a<b,
\qquad
c<0.
$$

Ordena correctamente, justificando cada caso:

1. $ac$, $bc$ y $0$;
2. $a/c$, $b/c$ y $0$;
3. $1/a$, $1/b$ y $0$.
:::
::: {#exr-t1-0038}
<!-- CPM-T1-EXR-0038 | A | CONCEPTUAL | SUPREMUM | TRANSFER -->
**Ejercicio A3. Dos componentes y cuatro extremos.** Sea

$$
A=(-2,1]\cup[3,5).
$$

Determina $\sup A$, $\inf A$ y decide si $A$ tiene máximo y mínimo. Justifica la diferencia entre frontera y pertenencia.
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
<!-- CPM-T1-EXR-0040 | A | CONCEPTUAL | COMPLETENESS | TRANSFER -->
**Ejercicio A5. Auditar completitud sin calcular el supremo.** Para cada conjunto decide si el axioma de completitud garantiza **directamente** la existencia de un supremo real. En cada caso identifica la hipótesis que se verifica o falla.

1. $\{x\in\mathbb R:|x-2|<1\}$;
2. $[0,\infty)$;
3. $\varnothing$;
4. $\{1/n:n\in\mathbb N_{>0}\}$;
5. $(-\infty,0]$.

No calcules el supremo salvo que sea necesario para justificar una cota.
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

