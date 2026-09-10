## Ejercicios y soluciones {#sec-t1-c04-11}

Llegamos al banco final de `T1-C04`. Hasta aquí las técnicas aparecieron primero de manera aislada y después, en §4.10, como estaciones guiadas. En esta sección desaparece esa señalización: antes de comenzar una prueba habrá que decidir si el problema pide trabajar directamente con cuantificadores, usar álgebra de límites, estimar por sándwich, explotar monotonía y completitud, controlar una recurrencia o interpretar un límite infinito.

El banco contiene exactamente cuarenta ejercicios, distribuidos en siete niveles:

$$
7A+7B+7C+6D+5E+5F+3G=40.
$$

Los niveles no miden solo dificultad de cálculo. En particular, los niveles D y E obligan a distinguir afirmaciones verdaderas de recíprocas falsas, mientras que los niveles F y G exigen reconstruir por qué funcionan las herramientas del capítulo.

Todos los problemas pueden resolverse con `T1-C01--T1-C04`. No se necesitan límites de funciones, continuidad, derivadas, subsucesiones, Bolzano–Weierstrass, criterio de Cauchy ni $\limsup/\liminf$.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0116}
<!-- CPM-T1-EXR-0116 | A | CONCEPTUAL | COMPUTATION | ORIGINAL -->
**Ejercicio A1. Índices y términos.** Sea

$$
a_n=\frac{2n+1}{n+1},
\qquad n\ge0.
$$

1. Escribe los cuatro primeros términos.
2. Identifica el término de índice $3$.
3. Explica la diferencia entre el índice $3$ y el término $a_3$.
:::

::: {#exr-t1-0117}
<!-- CPM-T1-EXR-0117 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A2. Cola y eventualidad.** Sea

$$
a_n=\frac{(-1)^n}{n+1}.
$$

Decide cuáles de las siguientes propiedades se cumplen eventualmente:

1. $|a_n|<1/10$;
2. $a_n>0$;
3. $-1/10<a_n<1/10$.

Cuando la respuesta sea afirmativa, proporciona un umbral $N$ que funcione.
:::

::: {#exr-t1-0118}
<!-- CPM-T1-EXR-0118 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A3. Tres comportamientos distintos.** Considera

$$
p_n=2-\frac1{n+1},
\qquad
q_n=(-1)^n,
\qquad
r_n=n.
$$

Para cada sucesión, indica si es acotada, si es monótona y cuál de las siguientes descripciones corresponde:

- converge a un número real;
- tiende a $+\infty$;
- diverge sin límite infinito unilateral.
:::

::: {#exr-t1-0119}
<!-- CPM-T1-EXR-0119 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A4. Leer $\varepsilon$–$N$.** Traduce a lenguaje ordinario la afirmación

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N:
|a_n-5|<\varepsilon.
$$

Después responde:

1. ¿puede $N$ depender de $\varepsilon$?;
2. ¿puede $N$ depender de un índice $n$ elegido después?;
3. ¿qué número afirma la fórmula que es el límite?
:::

::: {#exr-t1-0120}
<!-- CPM-T1-EXR-0120 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A5. Un cambio finito.** Sean

$$
a_n=\frac1{n+1}
$$

y

$$
b_n=
\begin{cases}
1000-n, & 0\le n\le50,\\[4pt]
\dfrac1{n+1}, & n>50.
\end{cases}
$$

Sin volver a demostrar el límite desde la definición, determina el límite de $(b_n)$ y explica qué resultado del capítulo estás usando.
:::

::: {#exr-t1-0121}
<!-- CPM-T1-EXR-0121 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A6. Real, infinito o ninguno.** Clasifica cada sucesión:

$$
a_n=\frac1{n+1},
\qquad
b_n=n,
\qquad
c_n=-n,
\qquad
d_n=(-1)^n.
$$

Para cada una indica si tiene límite real, límite $+\infty$, límite $-\infty$ o ninguna de esas tres posibilidades.
:::

::: {#exr-t1-0122}
<!-- CPM-T1-EXR-0122 | A | CONCEPTUAL | ORIGINAL -->
**Ejercicio A7. Infinitas visitas no son una cola.** Define

$$
a_n=
\begin{cases}
0, & n\text{ par},\\
1, & n\text{ impar}.
\end{cases}
$$

1. Explica por qué hay términos arbitrariamente tardíos exactamente iguales a $0$.
2. Decide si $a_n\to0$.
3. Señala qué orden de cuantificadores distingue ambas afirmaciones.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0123}
<!-- CPM-T1-EXR-0123 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B1. Álgebra de límites.** Supón que

$$
a_n\to2,
\qquad
b_n\to-1.
$$

Calcula

$$
\lim_{n\to\infty}
\frac{3a_n-2b_n}{a_n+b_n}.
$$

Justifica por qué el cociente puede tratarse con el álgebra de límites.
:::

::: {#exr-t1-0124}
<!-- CPM-T1-EXR-0124 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B2. Cociente de polinomios.** Para $n\ge1$, calcula

$$
\lim_{n\to\infty}
\frac{5n^3-2n}{2n^3+n^2+1}.
$$
:::

::: {#exr-t1-0125}
<!-- CPM-T1-EXR-0125 | B | COMPUTATION | PROOF | ORIGINAL -->
**Ejercicio B3. Oscilación amortiguada.** Demuestra que

$$
\frac{2+\sin n}{n+1}\to0.
$$
:::

::: {#exr-t1-0126}
<!-- CPM-T1-EXR-0126 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B4. Geométrica dentro de una expresión.** Calcula

$$
\lim_{n\to\infty}
\left(2+4\left(-\frac35\right)^n\right).
$$
:::

::: {#exr-t1-0127}
<!-- CPM-T1-EXR-0127 | B | CONCEPTUAL | PROOF | ORIGINAL -->
**Ejercicio B5. Qué preserva el orden.** Sean $(a_n)$ y $(b_n)$ sucesiones convergentes tales que

$$
a_n<b_n
$$

para todo $n$. Si

$$
a_n\to A,
\qquad
b_n\to B,
$$

¿qué relación entre $A$ y $B$ está garantizada? Da un ejemplo que muestre por qué no puede exigirse siempre una desigualdad estricta entre los límites.
:::

::: {#exr-t1-0128}
<!-- CPM-T1-EXR-0128 | B | COMPUTATION | ORIGINAL -->
**Ejercicio B6. Valor absoluto y cociente.** Supón que

$$
a_n\to-3,
\qquad
b_n\to2.
$$

Calcula

$$
\lim_{n\to\infty}\frac{|a_n|}{b_n+1}.
$$
:::

::: {#exr-t1-0129}
<!-- CPM-T1-EXR-0129 | B | PROOF | ORIGINAL -->
**Ejercicio B7. Una barrera cualquiera.** Demuestra desde la definición $M$–$N$ que

$$
2n-5\to+\infty.
$$
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0130}
<!-- CPM-T1-EXR-0130 | C | PROOF | ORIGINAL -->
**Ejercicio C1. Una prueba $\varepsilon$–$N$ completa.** Demuestra directamente desde la definición que

$$
\frac{3n+1}{n+1}\to3.
$$

Tu prueba debe exhibir una elección explícita de $N(\varepsilon)$.
:::

::: {#exr-t1-0131}
<!-- CPM-T1-EXR-0131 | C | PROOF | ORIGINAL -->
**Ejercicio C2. Diseñar el umbral.** Demuestra directamente que

$$
\frac1{2n+3}\to0.
$$

Antes de escribir la prueba final, determina qué condición suficiente sobre $n$ garantiza

$$
\frac1{2n+3}<\varepsilon.
$$
:::

::: {#exr-t1-0132}
<!-- CPM-T1-EXR-0132 | C | PROOF | ORIGINAL -->
**Ejercicio C3. Convergencia y acotación visible.** Para

$$
a_n=\frac{(-1)^n}{n+1},
$$

demuestra que $a_n\to0$ mediante sándwich y encuentra además una cota global $M$ tal que

$$
|a_n|\le M
$$

para todo $n$.
:::

::: {#exr-t1-0133}
<!-- CPM-T1-EXR-0133 | C | PROOF | ORIGINAL -->
**Ejercicio C4. Sándwich racional.** Para $n\ge1$, demuestra que

$$
\frac{n}{n^2+1}\to0
$$

sin dividir numerador y denominador por $n^2$. Busca directamente una sucesión dominante sencilla.
:::

::: {#exr-t1-0134}
<!-- CPM-T1-EXR-0134 | C | PROOF | ORIGINAL -->
**Ejercicio C5. Separar un denominador de cero.** Supón que

$$
b_n\to4.
$$

1. Demuestra que existe $N$ tal que $b_n>2$ para todo $n\ge N$.
2. Deduce que $b_n\ne0$ eventualmente.
3. Concluye que
   $$
   \frac1{b_n}\to\frac14.
   $$
:::

::: {#exr-t1-0135}
<!-- CPM-T1-EXR-0135 | C | PROOF | DISCOVERY | ORIGINAL -->
**Ejercicio C6. Una geométrica desde Bernoulli.** Demuestra que

$$
\left(\frac34\right)^n\to0
$$

usando únicamente la desigualdad de Bernoulli y el teorema del sándwich.

Sugerencia: escribe

$$
\frac34=\frac1{1+h}
$$

con $h>0$.
:::

::: {#exr-t1-0136}
<!-- CPM-T1-EXR-0136 | C | PROOF | ORIGINAL -->
**Ejercicio C7. Un límite infinito desde la definición.** Demuestra que

$$
n^2\to+\infty
$$

usando directamente la definición $M$–$N$.
:::

### Nivel D — Inversión y diagnóstico

En cada ejercicio decide si la afirmación es verdadera. Si es falsa, construye un contraejemplo y verifica las propiedades relevantes.

::: {#exr-t1-0137}
<!-- CPM-T1-EXR-0137 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D1. «Acotada implica convergente».** Decide si toda sucesión real acotada converge.
:::

::: {#exr-t1-0138}
<!-- CPM-T1-EXR-0138 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D2. «Convergente implica monótona».** Decide si toda sucesión real convergente es monótona.
:::

::: {#exr-t1-0139}
<!-- CPM-T1-EXR-0139 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D3. «No acotada implica límite infinito».** Decide si toda sucesión no acotada satisface

$$
a_n\to+\infty
$$

o

$$
a_n\to-\infty.
$$
:::

::: {#exr-t1-0140}
<!-- CPM-T1-EXR-0140 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D4. Cuadrados convergentes.** Decide si

$$
a_n^2\text{ converge}
\quad\Longrightarrow\quad
a_n\text{ converge}.
$$
:::

::: {#exr-t1-0141}
<!-- CPM-T1-EXR-0141 | D | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio D5. Diferencias sucesivas pequeñas.** Decide si

$$
a_{n+1}-a_n\to0
\quad\Longrightarrow\quad
a_n\text{ converge}.
$$
:::

::: {#exr-t1-0142}
<!-- CPM-T1-EXR-0142 | D | COUNTEREXAMPLE | CONCEPTUAL | ORIGINAL -->
**Ejercicio D6. El punto fijo no garantiza convergencia.** Una sucesión satisface

$$
y_0=0,
\qquad
y_{n+1}=3-y_n.
$$

La ecuación de punto fijo

$$
L=3-L
$$

tiene la solución $L=3/2$. Decide si $(y_n)$ converge y explica qué error lógico cometeríamos al concluir convergencia solo a partir de esa ecuación.
:::

### Nivel E — Contraejemplos construidos

::: {#exr-t1-0143}
<!-- CPM-T1-EXR-0143 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E1. Acotada y divergente.** Construye una sucesión que permanezca en el intervalo $[0,2]$ y no converja a ningún número real. Verifica ambas afirmaciones.
:::

::: {#exr-t1-0144}
<!-- CPM-T1-EXR-0144 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E2. Convergente pero no monótona.** Construye una sucesión que converja a $1$ y no sea monótona. Demuestra las dos propiedades.
:::

::: {#exr-t1-0145}
<!-- CPM-T1-EXR-0145 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E3. No acotada sin escape unilateral.** Construye una sucesión no acotada que no tienda ni a $+\infty$ ni a $-\infty$. Justifica las tres afirmaciones.
:::

::: {#exr-t1-0146}
<!-- CPM-T1-EXR-0146 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E4. Un prefijo arbitrariamente largo no decide el límite.** Sea $M\in\mathbb N$ arbitrario. Construye dos sucesiones $(a_n)$ y $(b_n)$ tales que

$$
a_n=b_n
\qquad
\text{para }0\le n\le M,
$$

pero cuyos límites reales sean distintos.
:::

::: {#exr-t1-0147}
<!-- CPM-T1-EXR-0147 | E | COUNTEREXAMPLE | ORIGINAL -->
**Ejercicio E5. Infinitamente cerca y, sin embargo, divergente.** Construye una sucesión que tenga términos arbitrariamente tardíos exactamente iguales a $0$, pero que no converja a $0$. Verifica la negación $\varepsilon$–$N$.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0148}
<!-- CPM-T1-EXR-0148 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F1. Reconstruir $1/(n+1)\to0$.** Completa el siguiente programa.

1. Parte de
   $$
   \frac1{n+1}<\varepsilon.
   $$
   ¿Qué desigualdad suficiente sobre $n$ aparece al invertir?
2. Usa la propiedad arquimediana para producir un natural que satisfaga esa desigualdad.
3. Reescribe el argumento en el orden
   $$
   \varepsilon\to N\to n\ge N\to |a_n|<\varepsilon.
   $$
:::

::: {#exr-t1-0149}
<!-- CPM-T1-EXR-0149 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F2. Descubrir la estimación del producto.** Sean

$$
a_n\to A,
\qquad
b_n\to B.
$$

Reconstruye una prueba de

$$
a_nb_n\to AB
$$

siguiendo estas pistas:

1. suma y resta $a_nB$;
2. demuestra primero que $(a_n)$ está eventualmente acotada;
3. obtiene una estimación de
   $$
   |a_nb_n-AB|
   $$
   mediante dos errores;
4. elige tolerancias para que cada error contribuya menos que $\varepsilon/2$.
:::

::: {#exr-t1-0150}
<!-- CPM-T1-EXR-0150 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F3. Descubrir el límite geométrico.** Sea $q$ real con $0<q<1$.

1. Escribe
   $$
   q=\frac1{1+h}
   $$
   con $h>0$.
2. Usa Bernoulli para demostrar
   $$
   0<q^n\le\frac1{1+nh}.
   $$
3. Demuestra que el término de la derecha tiende a $0$.
4. Concluye $q^n\to0$ por sándwich.
5. Explica cómo se extiende el resultado a $-1<q<0$.
:::

::: {#exr-t1-0151}
<!-- CPM-T1-EXR-0151 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F4. Una recurrencia completa.** Define

$$
a_0=0,
\qquad
a_{n+1}=\frac{a_n+4}{2}.
$$

Demuestra, en este orden:

1. que $0\le a_n<4$ para todo $n$;
2. que $(a_n)$ es creciente;
3. que converge por el teorema de convergencia monótona;
4. que su límite es $4$, usando desplazamiento de índices y álgebra de límites.
:::

::: {#exr-t1-0152}
<!-- CPM-T1-EXR-0152 | F | DISCOVERY | PROOF | ORIGINAL -->
**Ejercicio F5. Reconstruir convergencia monótona.** Sea $(a_n)$ creciente y acotada superiormente, y define

$$
S=\{a_n:n\ge n_0\},
\qquad
L=\sup S.
$$

Usando únicamente la caracterización aproximativa del supremo y la monotonía, demuestra que $a_n\to L$. Señala exactamente dónde se utilizó la completitud de $\mathbb R$.
:::

### Nivel G — Desafíos de síntesis

::: {#exr-t1-0153}
<!-- CPM-T1-EXR-0153 | G | SYNTHESIS | PROOF | ORIGINAL -->
**Ejercicio G1. Intervalos encajados y sándwich secuencial.** Sea

$$
I_n=[a_n,b_n],
\qquad n\ge0,
$$

una sucesión de intervalos cerrados no vacíos tal que

$$
I_{n+1}\subseteq I_n
$$

para todo $n$ y

$$
b_n-a_n\to0.
$$

1. Demuestra que existe un único $L\in\mathbb R$ perteneciente a todos los intervalos.
2. Demuestra que
   $$
   a_n\to L,
   \qquad
   b_n\to L.
   $$
3. Si $(x_n)$ satisface $x_n\in[a_n,b_n]$ para todo $n$, demuestra que $x_n\to L$.
:::

::: {#exr-t1-0154}
<!-- CPM-T1-EXR-0154 | G | SYNTHESIS | PROOF | ORIGINAL -->
**Ejercicio G2. Método de Herón sin derivadas ni continuidad.** Sea $a>0$ y elige

$$
x_0>\sqrt a.
$$

Define

$$
x_{n+1}
=
\frac12\left(x_n+\frac{a}{x_n}\right).
$$

Demuestra que:

1. la sucesión está bien definida;
2. para todo $n$,
   $$
   \sqrt a\le x_{n+1}\le x_n;
   $$
3. $(x_n)$ converge;
4. su límite es $\sqrt a$.

La identificación final debe utilizar únicamente desplazamiento de índices y álgebra de límites.
:::

::: {#exr-t1-0155}
<!-- CPM-T1-EXR-0155 | G | SYNTHESIS | COUNTEREXAMPLE | PROOF | ORIGINAL -->
**Ejercicio G3. Diferencias pequeñas no bastan.** Define

$$
a_n=\sqrt{n+1}.
$$

1. Demuestra que
   $$
   a_n\to+\infty.
   $$
2. Demuestra que
   $$
   a_{n+1}-a_n
   =
   \frac1{\sqrt{n+2}+\sqrt{n+1}}
   \to0.
   $$
3. Explica con precisión qué afirmación falsa destruye este ejemplo.
:::

