## Ejercicios y soluciones {#sec-t1-c03-11}

Llegamos al banco final de `T1-C03`. En las secciones anteriores las herramientas funcionales fueron apareciendo de manera progresiva y, en §3.10, se combinaron todavía con una guía explícita de estrategia. Aquí la ayuda disminuye deliberadamente: antes de calcular, habrá que decidir qué estructura es relevante y qué datos de la función deben controlarse.

El banco contiene exactamente cuarenta ejercicios, distribuidos en siete niveles:

$$
7A+7B+7C+6D+5E+5F+3G=40.
$$

Los niveles no miden solamente dificultad algebraica. Un ejercicio puede resultar corto y, sin embargo, exigir una distinción conceptual importante. En particular, se evaluará de manera recurrente la capacidad de separar:

- fórmula, función completa y gráfica;
- dominio, codominio e imagen;
- preimagen de un conjunto y función inversa;
- existencia de una inversa y cálculo de una fórmula candidata;
- propiedades de una función y propiedades de una composición.

Todos los problemas pueden resolverse con el material construido en `T1-C01--T1-C03`. No se necesitan límites, continuidad ni derivadas.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0076}
<!-- CPM-T1-EXR-0076 | A | CONCEPTUAL | COMPUTATION | ORIGINAL -->
**Ejercicio A1. Dominio, codominio e imagen.** Sea

$$
f\colon[-2,3]\to\mathbb R,
\qquad
f(x)=x^2.
$$

Identifica el dominio, el codominio y la imagen de $f$. Decide si imagen y codominio coinciden.
:::

::: {#exr-t1-0077}
<!-- CPM-T1-EXR-0077 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. ¿Es realmente una función?** Considera la relación

$$
R=\{(0,1),(1,2),(2,2),(2,3)\}
$$

desde $A=\{0,1,2\}$ hacia $B=\{1,2,3\}$.

1. ¿Define $R$ una función $A\to B$?
2. Identifica exactamente qué parte de la condición «a cada entrada corresponde exactamente una salida» falla.
3. Elimina el menor número posible de pares para obtener una función $A\to B$.
:::

::: {#exr-t1-0078}
<!-- CPM-T1-EXR-0078 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A3. Misma fórmula, ¿misma función?** Sean

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

y

$$
g\colon\mathbb R\to[0,\infty),
\qquad g(x)=x^2.
$$

Según la convención adoptada en este libro, decide si $f=g$ y justifica tu respuesta. Después compara sus imágenes.
:::

::: {#exr-t1-0079}
<!-- CPM-T1-EXR-0079 | A | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio A4. Imagen y preimagen.** Sea

$$
q\colon\mathbb R\to[0,\infty),
\qquad q(x)=x^2.
$$

Calcula

$$
q([-2,1])
$$

y

$$
q^{-1}([1,4)).
$$

Recuerda que en la segunda expresión $q^{-1}$ designa una **preimagen de conjunto**.
:::

::: {#exr-t1-0080}
<!-- CPM-T1-EXR-0080 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Leer una función desde una tabla.** Sea

$$
p\colon\{-2,-1,0,1\}\to\{1,2,3,4\}
$$

la función dada por

| $x$ | $-2$ | $-1$ | $0$ | $1$ |
|---:|---:|---:|---:|---:|
| $p(x)$ | $3$ | $1$ | $1$ | $4$ |

Determina:

1. $\operatorname{Im}(p)$;
2. si $p$ es inyectiva;
3. si $p$ es sobreyectiva.
:::

::: {#exr-t1-0081}
<!-- CPM-T1-EXR-0081 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A6. Una restricción cambia la función.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

y considera la restricción

$$
f|_{[0,\infty)}\colon[0,\infty)\to\mathbb R.
$$

1. ¿Cuál es su imagen?
2. ¿Es inyectiva?
3. ¿Es sobreyectiva?
4. ¿Qué cambio adicional permitiría convertir esta restricción en una biyección?
:::

::: {#exr-t1-0082}
<!-- CPM-T1-EXR-0082 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A7. Leer la notación como una afirmación lógica.** Sea

$$
a\colon\{0,1,2,3\}\to\mathbb R,
\qquad
 a(n)=\frac{n}{n+1}.
$$

1. Traduce la declaración $a\colon\{0,1,2,3\}\to\mathbb R$ a una frase que haga explícitas existencia y unicidad de la salida.
2. Calcula $\operatorname{Im}(a)$.
3. Explica por qué el hecho de que la imagen no sea todo $\mathbb R$ no impide que $a$ sea una función.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0083}
<!-- CPM-T1-EXR-0083 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Dos órdenes de composición.** Sean

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=2x-1,
$$

y

$$
g\colon\mathbb R\to\mathbb R,
\qquad g(x)=x^2.
$$

Calcula $g\circ f$ y $f\circ g$. Decide si son la misma función.
:::

::: {#exr-t1-0084}
<!-- CPM-T1-EXR-0084 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B2. Antes de componer, controla los tipos.** Sean

$$
u\colon[-1,\infty)\to[0,\infty),
\qquad u(x)=\sqrt{x+1},
$$

y

$$
v\colon[0,\infty)\setminus\{2\}\to\mathbb R,
\qquad v(t)=\frac1{t-2}.
$$

1. Explica por qué $v\circ u$ no está definida como composición sobre todo $[-1,\infty)$ con las funciones tal como fueron declaradas.
2. Encuentra el mayor subconjunto $E\subseteq[-1,\infty)$ tal que
   $$
   v\circ(u|_E)
   $$
   esté bien definida.
3. Escribe su fórmula.
:::

::: {#exr-t1-0085}
<!-- CPM-T1-EXR-0085 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B3. Intervalos bajo una función afín.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=3x-2.
$$

Calcula

$$
f([1,4))
$$

y

$$
f^{-1}((-5,4]).
$$
:::

::: {#exr-t1-0086}
<!-- CPM-T1-EXR-0086 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B4. La preimagen puede tener dos ramas.** Sea

$$
q\colon\mathbb R\to[0,\infty),
\qquad q(x)=x^2.
$$

Calcula

$$
q^{-1}((4,9])
$$

y explica por qué el resultado no es un solo intervalo.
:::

::: {#exr-t1-0087}
<!-- CPM-T1-EXR-0087 | B | CONCEPTUAL | ORIGINAL -->
**Ejercicio B5. Clasificar y reparar.** Considera

$$
r\colon[0,\infty)\to\mathbb R,
\qquad r(x)=x^2.
$$

1. Clasifica $r$ respecto de inyectividad y sobreyectividad.
2. Modifica solamente el codominio para obtener una biyección.
3. Escribe la inversa de la función resultante.
:::

::: {#exr-t1-0088}
<!-- CPM-T1-EXR-0088 | B | COMPUTATION | CONCEPTUAL | ORIGINAL -->
**Ejercicio B6. Función por tramos.** Sea

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=
\begin{cases}
x+1, & x<0,\\
x^2, & x\ge0.
\end{cases}
$$

1. Calcula $p(-2)$, $p(0)$ y $p(2)$.
2. Determina $\operatorname{Im}(p)$.
3. Decide si $p$ es inyectiva y si es sobreyectiva.
:::

::: {#exr-t1-0089}
<!-- CPM-T1-EXR-0089 | B | GEOMETRY | CONCEPTUAL | ORIGINAL -->
**Ejercicio B7. Transformar una gráfica sin memorizar recetas.** Sea $f\colon\mathbb R\to\mathbb R$ una función y define

$$
h(x)=2f(x-3)-1.
$$

Supón que $(a,b)$ pertenece a la gráfica de $f$.

1. Determina qué punto de la gráfica de $h$ corresponde a $(a,b)$.
2. Describe, en orden, las transformaciones geométricas que llevan la gráfica de $f$ a la de $h$.
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0090}
<!-- CPM-T1-EXR-0090 | C | PROOF | ORIGINAL -->
**Ejercicio C1. Inyectividad de una función afín.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=ax+b,
$$

donde $a\ne0$. Demuestra que $f$ es inyectiva.
:::

::: {#exr-t1-0091}
<!-- CPM-T1-EXR-0091 | C | PROOF | ORIGINAL -->
**Ejercicio C2. Biyectividad del recíproco.** Sea

$$
r\colon(0,\infty)\to(0,\infty),
\qquad r(x)=\frac1x.
$$

Demuestra que $r$ es biyectiva y determina $r^{-1}$.
:::

::: {#exr-t1-0092}
<!-- CPM-T1-EXR-0092 | C | PROOF | COMPUTATION | ORIGINAL -->
**Ejercicio C3. Probar primero, invertir después.** Sea

$$
f\colon[0,\infty)\to[1,\infty),
\qquad f(x)=x^2+1.
$$

1. Demuestra que $f$ es inyectiva.
2. Demuestra que $f$ es sobreyectiva construyendo un antecedente de un $y\in[1,\infty)$ arbitrario.
3. Solo después de lo anterior, determina $f^{-1}$.
:::

::: {#exr-t1-0093}
<!-- CPM-T1-EXR-0093 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C4. La composición conserva la inyectividad.** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C
$$

funciones inyectivas. Demuestra directamente, a partir de la definición, que $g\circ f$ es inyectiva.
:::

::: {#exr-t1-0094}
<!-- CPM-T1-EXR-0094 | C | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio C5. Álgebra de preimágenes.** Sea $f\colon A\to B$ y sean $U,V\subseteq B$. Demuestra:

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V)
$$

y

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

Haz la demostración mediante pertenencia de un elemento arbitrario.
:::

::: {#exr-t1-0095}
<!-- CPM-T1-EXR-0095 | C | PROOF | CONCEPTUAL | ORIGINAL -->
**Ejercicio C6. El cuadrado cambia de monotonía.** Demuestra que

$$
q(x)=x^2
$$

es estrictamente creciente en $[0,\infty)$ y estrictamente decreciente en $(-\infty,0]$. Deduce que su restricción a cualquiera de esos intervalos es inyectiva.
:::

::: {#exr-t1-0096}
<!-- CPM-T1-EXR-0096 | C | GEOMETRY | PROOF | ORIGINAL -->
**Ejercicio C7. Gráfica de una función y de su inversa.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=2x-3.
$$

1. Demuestra que $f$ es biyectiva y calcula $f^{-1}$.
2. Prueba que
   $$
   (x,y)\in\Gamma_f
   \quad\Longleftrightarrow\quad
   (y,x)\in\Gamma_{f^{-1}}.
   $$
3. Interpreta geométricamente la equivalencia anterior.
:::

### Nivel D — Inversión y diagnóstico

::: {#exr-t1-0097}
<!-- CPM-T1-EXR-0097 | D | PROOF | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D1. ¿Qué hereda una composición inyectiva?** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C.
$$

Supón que $g\circ f$ es inyectiva.

1. Demuestra que $f$ debe ser inyectiva.
2. Decide si $g$ debe ser inyectiva. Si la respuesta es negativa, construye un contraejemplo explícito.
:::

::: {#exr-t1-0098}
<!-- CPM-T1-EXR-0098 | D | PROOF | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D2. ¿Qué hereda una composición sobreyectiva?** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C.
$$

Supón que $g\circ f$ es sobreyectiva.

1. Demuestra que $g$ debe ser sobreyectiva.
2. Decide si $f$ debe ser sobreyectiva. Si la respuesta es negativa, construye un contraejemplo explícito.
:::

::: {#exr-t1-0099}
<!-- CPM-T1-EXR-0099 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D3. Auditoría de dominio y codominio.** Considera las cuatro funciones

$$
p\colon\mathbb R\to\mathbb R,
\qquad p(x)=x^2,
$$

$$
q\colon\mathbb R\to[0,\infty),
\qquad q(x)=x^2,
$$

$$
r\colon[0,\infty)\to\mathbb R,
\qquad r(x)=x^2,
$$

y

$$
s\colon[0,\infty)\to[0,\infty),
\qquad s(x)=x^2.
$$

1. Decide qué pares, si alguno, son funciones iguales según la convención del libro.
2. Clasifica cada función como inyectiva, sobreyectiva, biyectiva o ninguna de las anteriores.
3. Explica qué propiedad se modifica al cambiar solo el dominio y qué propiedad puede modificarse al cambiar solo el codominio.
:::

::: {#exr-t1-0100}
<!-- CPM-T1-EXR-0100 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D4. Una «inversa» demasiado rápida.** Un estudiante escribe:

> Si $f(x)=x^2$, entonces $y=x^2$, de donde $x=\sqrt y$. Por tanto, $f^{-1}(y)=\sqrt y$.

Analiza el argumento para la función

$$
f\colon\mathbb R\to[0,\infty),
\qquad f(x)=x^2.
$$

1. Localiza el error conceptual.
2. Explica por qué resolver una ecuación no basta para demostrar que existe una función inversa.
3. Repara la situación modificando el dominio de $f$ de dos maneras distintas y escribe las inversas correspondientes.
:::

::: {#exr-t1-0101}
<!-- CPM-T1-EXR-0101 | D | PROOF | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio D5. Una igualdad plausible que puede fallar.** Sea $f\colon A\to B$ y $E,F\subseteq A$.

1. Demuestra que siempre se cumple
   $$
   f(E\cap F)\subseteq f(E)\cap f(F).
   $$
2. Explica dónde se atascaría un intento de demostrar la inclusión inversa sin hipótesis adicionales.
3. Indica una hipótesis suficiente sobre $f$ que convierta la inclusión en igualdad.
:::

::: {#exr-t1-0102}
<!-- CPM-T1-EXR-0102 | D | CONCEPTUAL | SYNTHESIS | ORIGINAL -->
**Ejercicio D6. Reparar una función por tramos mal definida.** Se pretende definir

$$
h\colon\mathbb R\to\mathbb R,
\qquad
h(x)=
\begin{cases}
x+1, & x\ge0,\\
-x, & x\le0.
\end{cases}
$$

1. Explica por qué esta regla no define una función.
2. Propón dos reparaciones distintas que cambien únicamente las condiciones de los tramos, no las fórmulas $x+1$ y $-x$.
3. ¿Las dos reparaciones obtenidas definen necesariamente la misma función? Justifica.
:::

### Nivel E — Contraejemplos

::: {#exr-t1-0103}
<!-- CPM-T1-EXR-0103 | E | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio E1. Misma fórmula, funciones distintas.** Construye dos funciones distintas que utilicen la misma fórmula $1/x$. Deben diferir por su dominio, por su codominio o por ambos. Justifica formalmente que no son iguales.
:::

::: {#exr-t1-0104}
<!-- CPM-T1-EXR-0104 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. Separar inyectividad y sobreyectividad.** Construye:

1. una función inyectiva que no sea sobreyectiva;
2. una función sobreyectiva que no sea inyectiva.

Puedes usar conjuntos finitos o subconjuntos de $\mathbb R$, pero debes declarar dominio, codominio y regla.
:::

::: {#exr-t1-0105}
<!-- CPM-T1-EXR-0105 | E | COUNTEREXAMPLE | COMPUTATION | ORIGINAL -->
**Ejercicio E3. La composición no es conmutativa.** Construye funciones $f,g\colon\mathbb R\to\mathbb R$ tales que

$$
g\circ f\ne f\circ g.
$$

Calcula ambas composiciones y exhibe al menos un valor de $x$ en el que difieran.
:::

::: {#exr-t1-0106}
<!-- CPM-T1-EXR-0106 | E | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio E4. Intersecciones e imágenes.** Construye una función $f\colon A\to B$ y subconjuntos $E,F\subseteq A$ tales que

$$
f(E\cap F)\subsetneq f(E)\cap f(F).
$$

Explica qué rasgo de $f$ hace posible la inclusión estricta.
:::

::: {#exr-t1-0107}
<!-- CPM-T1-EXR-0107 | E | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio E5. No decreciente no significa inyectiva.** Construye una función $m\colon\mathbb R\to\mathbb R$ que sea no decreciente pero no inyectiva. Verifica ambas afirmaciones.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0108}
<!-- CPM-T1-EXR-0108 | F | DISCOVERY | CONCEPTUAL | ORIGINAL -->
**Ejercicio F1. Reconstruir una función desde su gráfica como conjunto.** Se sabe que $f\colon A\to B$ tiene

$$
B=\{1,2,4\}
$$

y que su gráfica es exactamente

$$
\Gamma_f=\{(-2,1),(0,1),(3,4)\}.
$$

1. Reconstruye $A$.
2. Escribe todos los valores de $f$.
3. Determina $\operatorname{Im}(f)$.
4. Decide si $f$ es inyectiva y si es sobreyectiva.
5. Explica por qué conocer solo la gráfica como conjunto de pares no habría bastado, bajo la convención de este libro, para reconstruir el codominio si $B$ no hubiese sido declarado.
:::

::: {#exr-t1-0109}
<!-- CPM-T1-EXR-0109 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Descubrir las leyes de preimagen.** Sea $f\colon A\to B$ y sean $U,V\subseteq B$.

Completa una cadena de equivalencias empezando por un elemento arbitrario $x\in A$ para demostrar:

$$
f^{-1}(U\cup V)=f^{-1}(U)\cup f^{-1}(V),
$$

$$
f^{-1}(U\cap V)=f^{-1}(U)\cap f^{-1}(V),
$$

y

$$
f^{-1}(B\setminus U)=A\setminus f^{-1}(U).
$$

Después explica por qué ninguna de estas identidades requiere inyectividad ni sobreyectividad.
:::

::: {#exr-t1-0110}
<!-- CPM-T1-EXR-0110 | F | DISCOVERY | SYNTHESIS | ORIGINAL -->
**Ejercicio F3. Fabricar dos biyectividades a partir del cuadrado.** Parte de la regla

$$
x\mapsto x^2.
$$

1. Encuentra una restricción del dominio y un codominio que produzcan una biyección cuya inversa sea $y\mapsto\sqrt y$.
2. Encuentra otra restricción, distinta de la anterior, que produzca una biyección cuya inversa sea $y\mapsto-\sqrt y$.
3. Demuestra en ambos casos inyectividad y sobreyectividad.
:::

::: {#exr-t1-0111}
<!-- CPM-T1-EXR-0111 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F4. Descubrir el criterio exacto de existencia de una inversa.** Sea $f\colon A\to B$. Para cada $y\in B$, considera la ecuación

$$
f(x)=y.
$$

1. Explica qué propiedad de $f$ garantiza que para cada $y$ exista **al menos una** solución $x\in A$.
2. Explica qué propiedad garantiza que exista **a lo sumo una** solución.
3. Deduce que existe una función inversa $f^{-1}\colon B\to A$ si y solo si $f$ es biyectiva.
4. Indica cómo se define $f^{-1}(y)$ a partir de la solución única.
:::

::: {#exr-t1-0112}
<!-- CPM-T1-EXR-0112 | F | DISCOVERY | GEOMETRY | ORIGINAL -->
**Ejercicio F5. Reconstruir una transformación como composición.** Define

$$
s(x)=x^2,
\qquad
q(x)=-2(x-3)^2+1.
$$

Para $a,c\in\mathbb R$, escribe

$$
T_a(x)=x+a,
\qquad
M_c(x)=cx.
$$

1. Expresa $q$ como una composición de $s$, traslaciones $T_a$ y una dilatación/reflexión $M_c$.
2. Usa la composición obtenida para describir, en orden, cómo se transforma la gráfica de $s$ en la de $q$.
3. Determina el punto al que se transforma el vértice $(0,0)$.
:::

### Nivel G — Desafíos

::: {#exr-t1-0113}
<!-- CPM-T1-EXR-0113 | G | PROOF | SYNTHESIS | ORIGINAL -->
**Ejercicio G1. Caracterización de la inyectividad mediante intersecciones.** Sea $f\colon A\to B$. Demuestra que las siguientes afirmaciones son equivalentes:

1. $f$ es inyectiva;
2. para todos $E,F\subseteq A$,
   $$
   f(E\cap F)=f(E)\cap f(F).
   $$

En la dirección menos inmediata, elige subconjuntos apropiados para recuperar la inyectividad a partir de la igualdad de imágenes.
:::

::: {#exr-t1-0114}
<!-- CPM-T1-EXR-0114 | G | PROOF | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio G2. Inversas laterales y cancelación.** Sean

$$
f\colon A\to B,
\qquad g\colon B\to A.
$$

1. Demuestra que
   $$
   g\circ f=\operatorname{id}_A
   $$
   implica que $f$ es inyectiva y $g$ es sobreyectiva.
2. Demuestra que
   $$
   f\circ g=\operatorname{id}_B
   $$
   implica que $f$ es sobreyectiva y $g$ es inyectiva.
3. Construye contraejemplos que muestren que, en general, las conclusiones de 1 o de 2 no bastan por sí solas para recuperar la identidad de composición correspondiente.
:::

::: {#exr-t1-0115}
<!-- CPM-T1-EXR-0115 | G | PROOF | COUNTEREXAMPLE | SYNTHESIS | ORIGINAL -->
**Ejercicio G3. Composición biyectiva: qué puede concluirse.** Sean

$$
f\colon A\to B,
\qquad g\colon B\to C,
$$

y supón que $g\circ f$ es biyectiva.

1. Demuestra que $f$ es inyectiva.
2. Demuestra que $g$ es sobreyectiva.
3. Decide, mediante prueba o contraejemplo, si $f$ y $g$ deben ser biyectivas.
4. Encuentra una hipótesis adicional sobre $f$ que sea suficiente para forzar que **ambas** funciones sean biyectivas.
5. Encuentra una hipótesis adicional sobre $g$ que también sea suficiente para forzar que **ambas** sean biyectivas.
:::
