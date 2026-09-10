## Un pequeño repertorio de límites fundamentales {#sec-t1-c04-06}

Las secciones anteriores construyeron herramientas generales. Ya sabemos trabajar directamente con la definición $\varepsilon$–$N$, combinar límites mediante operaciones algebraicas y utilizar desigualdades para atrapar una sucesión entre otras más sencillas.

Ahora conviene transformar esas herramientas en un pequeño repertorio de resultados que podamos reutilizar sin reconstruir cada prueba desde cero.

La palabra **repertorio** debe interpretarse con cuidado. No queremos una tabla de límites que se memoriza y se aplica mecánicamente. Queremos unas pocas piezas cuya demostración entendamos y que después puedan convertirse en componentes de argumentos más grandes.

El criterio será siempre el mismo:

$$
\boxed{
\text{un límite fundamental debe quedar apoyado en resultados anteriores y no en teoría todavía no construida.}
}
$$

Por eso en esta sección no utilizaremos continuidad de funciones, exponenciales reales, logaritmos, series ni regla de l'Hôpital. Todo saldrá de arquimedianidad, inducción, álgebra de límites y teorema del sándwich.

### Las potencias recíprocas también desaparecen

Ya demostramos que

$$
\frac1{n+1}\to0.
$$

¿Qué ocurre si aumentamos la potencia del denominador?

Sea $p\in\mathbb N_{>0}$. Para todo $n\in\mathbb N$ tenemos

$$
n+1\ge1.
$$

Como $p\ge1$,

$$
(n+1)^p\ge n+1,
$$

y, al tomar recíprocos positivos,

$$
0<\frac1{(n+1)^p}\le\frac1{n+1}.
$$

Los extremos satisfacen

$$
0\to0
$$

y

$$
\frac1{n+1}\to0.
$$

Por el teorema del sándwich,

$$
\boxed{
\frac1{(n+1)^p}\to0
\qquad
\text{para todo }p\in\mathbb N_{>0}.
}
$$

Este pequeño argumento ya muestra una ventaja importante de disponer de resultados generales. No necesitamos volver a fabricar un $N(\varepsilon)$ diferente para cada potencia. Una sola comparación con una sucesión cuyo límite conocemos resuelve toda la familia.

También podemos multiplicar por una constante. Si $c\in\mathbb R$, el álgebra de límites da

$$
\frac{c}{(n+1)^p}\to0.
$$

Así obtenemos un primer patrón reutilizable:

$$
\boxed{
\text{constante}
\times
\text{potencia recíproca positiva}
\longrightarrow 0.
}
$$

### Un problema diferente: ¿por qué una potencia geométrica tiende a cero?

Consideremos ahora una sucesión de la forma

$$
q^n.
$$

La intuición es familiar cuando

$$
|q|<1.
$$

Por ejemplo,

$$
\left(\frac12\right)^n,
\qquad
\left(\frac23\right)^n,
\qquad
\left(-\frac34\right)^n
$$

parecen hacerse cada vez menores en valor absoluto.

Pero aquí aparece una dificultad distinta de la que encontramos con $1/(n+1)$. La variable $n$ está en el **exponente**, de modo que una desigualdad como

$$
q^n<\varepsilon
$$

no se despeja mediante el álgebra elemental que hemos utilizado hasta ahora sin introducir logaritmos. Y los logaritmos todavía no forman parte de nuestra teoría.

Necesitamos, por tanto, otra estrategia.

Para $0<q<1$ podemos escribir

$$
q=\frac1{1+h}
$$

con algún $h>0$. Basta tomar

$$
h=\frac{1-q}{q}.
$$

Entonces

$$
q^n=\frac1{(1+h)^n}.
$$

Si conseguimos una **cota inferior sencilla** para $(1+h)^n$, obtendremos una cota superior para $q^n$.

La herramienta adecuada es una desigualdad elemental que puede demostrarse por inducción.

### La desigualdad de Bernoulli como puente entre crecimiento multiplicativo y crecimiento lineal

Sea $h>0$. Afirmamos que para todo $n\in\mathbb N$,

$$
\boxed{
(1+h)^n\ge1+nh.
}
$$

La demostración es exactamente del tipo estudiado en `T1-C01`.

**Caso base.** Para $n=0$,

$$
(1+h)^0=1=1+0h.
$$

**Paso inductivo.** Supongamos que

$$
(1+h)^n\ge1+nh.
$$

Como $1+h>0$, podemos multiplicar la desigualdad por ese número sin cambiar su sentido:

$$
(1+h)^{n+1}
\ge
(1+nh)(1+h).
$$

Desarrollando el lado derecho,

$$
(1+nh)(1+h)
=
1+(n+1)h+nh^2.
$$

Como

$$
nh^2\ge0,
$$

tenemos

$$
(1+h)^{n+1}
\ge
1+(n+1)h.
$$

La inducción queda cerrada.

La importancia de esta desigualdad en nuestro problema no consiste en que describa con gran precisión $(1+h)^n$. De hecho, la cota lineal

$$
1+nh
$$

es muy rudimentaria comparada con la potencia. Pero es suficiente para nuestro objetivo.

Al tomar recíprocos positivos obtenemos

$$
0<\frac1{(1+h)^n}\le\frac1{1+nh}.
$$

Hemos convertido una potencia en una expresión lineal en $n$ que sí podemos controlar directamente.

### Un caso completo antes del resultado general

::: {#exm-t1-0037}
**Construcción detallada del límite geométrico: $(2/3)^n\to0$.** Consideremos

$$
a_n=\left(\frac23\right)^n,
\qquad n\ge0.
$$

No utilizaremos logaritmos ni una función exponencial real.

Escribimos

$$
\frac23
=
\frac1{1+1/2}.
$$

Por la desigualdad de Bernoulli con $h=1/2$,

$$
\left(1+\frac12\right)^n
\ge
1+\frac n2.
$$

Tomando recíprocos,

$$
0<
\left(\frac23\right)^n
\le
\frac1{1+n/2}
=
\frac2{n+2}.
$$

Ahora debemos justificar que la sucesión de la derecha tiende a cero. Podemos hacerlo con el álgebra ya disponible:

$$
\frac2{n+2}
=
\frac{2/(n+1)}{(n+2)/(n+1)}
=
\frac{2/(n+1)}{1+1/(n+1)}.
$$

Como

$$
\frac1{n+1}\to0,
$$

tenemos

$$
\frac{2}{n+1}\to0
$$

y

$$
1+\frac1{n+1}\to1.
$$

Por la ley del cociente,

$$
\frac2{n+2}\to0.
$$

Por tanto,

$$
0
\le
\left(\frac23\right)^n
\le
\frac2{n+2},
$$

con ambos extremos convergiendo a $0$. El teorema del sándwich da

$$
\boxed{
\left(\frac23\right)^n\to0.
}
$$

**Lectura de la estrategia.** La potencia no se resolvió despejando $n$. La reemplazamos por una cota más sencilla:

$$
\left(\frac23\right)^n
=
\frac1{(1+1/2)^n}
\le
\frac1{1+n/2}.
$$

Bernoulli produjo la comparación y el sándwich convirtió esa comparación en convergencia.
:::

El ejemplo contiene ya toda la estructura necesaria para el caso general.

::: {#cor-t1-0008}
**Límite de una sucesión geométrica con razón de módulo menor que uno.** Sea $q\in\mathbb R$ con

$$
|q|<1.
$$

Entonces, considerando la sucesión $(q^n)_{n\ge1}$,

$$
\boxed{q^n\to0.}
$$

**Demostración.** Distinguimos casos.

Si $q=0$, entonces

$$
q^n=0
$$

para todo $n\ge1$, y la conclusión es inmediata.

Supongamos ahora

$$
0<|q|<1.
$$

Definimos

$$
r=|q|.
$$

Entonces $0<r<1$. Existe $h>0$ tal que

$$
r=\frac1{1+h};
$$

por ejemplo,

$$
h=\frac{1-r}{r}>0.
$$

Por Bernoulli,

$$
(1+h)^n\ge1+nh.
$$

Por tanto,

$$
0<r^n
=
\frac1{(1+h)^n}
\le
\frac1{1+nh}.
$$

Veamos directamente que

$$
\frac1{1+nh}\to0.
$$

Sea $\varepsilon>0$. Por la propiedad arquimediana podemos elegir $N\in\mathbb N$ con

$$
N>\frac1{h\varepsilon}.
$$

En particular $N>0$. Si $n\ge N$, entonces

$$
1+nh>nh\ge Nh>\frac1\varepsilon.
$$

Tomando recíprocos positivos,

$$
0<\frac1{1+nh}<\varepsilon.
$$

Así,

$$
\frac1{1+nh}\to0.
$$

El sándwich produce

$$
r^n\to0.
$$

Finalmente,

$$
|q^n|
=
|q|^n
=
r^n.
$$

Como $r^n\to0$, la forma absoluta del teorema del sándwich implica

$$
q^n\to0.
$$
:::

Esta prueba merece una segunda lectura porque combina casi todo lo construido hasta ahora:

1. **álgebra:** $|q|=1/(1+h)$;
2. **inducción:** Bernoulli;
3. **arquimedianidad:** producir un umbral para $1/(1+nh)$;
4. **orden:** convertir una desigualdad en una cota útil;
5. **sándwich:** transportar el límite de la cota a la potencia geométrica;
6. **valor absoluto:** reducir el caso negativo al positivo.

No hemos utilizado ninguna teoría de la función exponencial. El resultado pertenece enteramente a la teoría secuencial ya disponible.

### Por qué la hipótesis $|q|<1$ es esencial

Conviene auditar la frontera del corolario.

Si

$$
q=1,
$$

entonces

$$
q^n=1
$$

para todo $n$, de modo que el límite es $1$, no $0$.

Si

$$
q=-1,
$$

obtenemos

$$
(-1)^n,
$$

cuya divergencia ya demostramos en §4.2.

Por tanto, no podemos reemplazar la condición

$$
|q|<1
$$

por

$$
|q|\le1.
$$

Cuando $|q|>1$, los tamaños $|q|^n$ crecen en lugar de contraerse. Todavía no formalizaremos ese comportamiento mediante límites infinitos; esa será tarea de §4.9.

### Cocientes de polinomios: dividir por la potencia dominante

Los límites anteriores permiten sistematizar una familia importante de ejemplos.

Consideremos

$$
a_n=
\frac{3n^2-5n+7}{2n^2+n-4}.
$$

La dificultad aparente es que numerador y denominador aumentan de tamaño. Pero para un límite real no necesitamos estudiar ambos por separado. Dividimos toda la fracción por la mayor potencia presente, aquí $n^2$.

Para $n\ge1$,

$$
\frac{3n^2-5n+7}{2n^2+n-4}
=
\frac{3-5/n+7/n^2}{2+1/n-4/n^2}.
$$

Ya sabemos que

$$
\frac1n\to0
$$

y

$$
\frac1{n^2}\to0.
$$

Por el álgebra de límites,

$$
3-\frac5n+\frac7{n^2}\to3
$$

y

$$
2+\frac1n-\frac4{n^2}\to2.
$$

Como el límite del denominador es distinto de cero, la ley del cociente da

$$
\boxed{
\frac{3n^2-5n+7}{2n^2+n-4}
\to
\frac32.
}
$$

El procedimiento general ya es visible. Si numerador y denominador son polinomios del mismo grado, dividir por la potencia dominante hace desaparecer todos los términos de grado inferior mediante factores del tipo $1/n^p$. El límite queda determinado por el cociente de los coeficientes principales.

Si el grado del numerador es menor que el del denominador, la misma operación deja en el numerador únicamente términos que contienen potencias recíprocas. Por ejemplo,

$$
\frac{4n+1}{n^3+2}
=
\frac{4/n^2+1/n^3}{1+2/n^3}
\to0.
$$

Así obtenemos, para los casos de límite real que necesitamos ahora, la regla estructural:

$$
\boxed{
\begin{array}{ll}
\deg P<\deg Q
&\Longrightarrow\dfrac{P(n)}{Q(n)}\to0,\\[8pt]
\deg P=\deg Q
&\Longrightarrow\dfrac{P(n)}{Q(n)}\to
\dfrac{\text{coeficiente principal de }P}
{\text{coeficiente principal de }Q},
\end{array}
}
$$

siempre que el denominador esté definido en la cola correspondiente.

No hemos creado una nueva regla independiente. Todo proviene de

$$
\frac1{n^p}\to0
$$

y del álgebra de límites.

El caso

$$
\deg P>\deg Q
$$

suele producir crecimiento sin límite real finito. Lo estudiaremos cuando dispongamos de la definición rigurosa de $+\infty$ y $-\infty$ en §4.9.

### Oscilaciones amortiguadas: lo complicado puede quedar encerrado en una cota

El ejemplo de §4.5 con

$$
\frac{\sin n}{n+1}
$$

mostró un fenómeno general: una parte de la sucesión puede oscilar sin converger, mientras otro factor reduce su tamaño hasta volver irrelevante esa oscilación para el límite.

Consideremos, por ejemplo,

$$
a_n=
\frac{3(-1)^n-2\sin n}{(n+1)^2}.
$$

No necesitamos comprender la interacción exacta entre $(-1)^n$ y $\sin n$. Basta estimar:

$$
\begin{aligned}
|3(-1)^n-2\sin n|
&\le
3|(-1)^n|+2|\sin n|\\
&\le3+2\\
&=5.
\end{aligned}
$$

Por tanto,

$$
|a_n|
\le
\frac5{(n+1)^2}.
$$

Como

$$
\frac5{(n+1)^2}\to0,
$$

la forma absoluta del sándwich da

$$
\boxed{
\frac{3(-1)^n-2\sin n}{(n+1)^2}
\to0.
}
$$

Aquí aparece un principio que conviene conservar:

$$
\boxed{
\text{numerador uniformemente acotado}
\quad+
\text{denominador cuyo recíproco tiende a }0
\quad\Longrightarrow\quad
\text{cociente que tiende a }0,
}
$$

siempre que la estimación se formule rigurosamente.

Más generalmente, si $(u_n)$ es una sucesión acotada y

$$
v_n\to0,
$$

entonces

$$
u_nv_n\to0.
$$

Podemos justificarlo de dos maneras con herramientas ya conocidas.

Por un lado, como $(u_n)$ es acotada, existe $M>0$ tal que

$$
|u_n|\le M.
$$

Entonces

$$
|u_nv_n|
\le
M|v_n|.
$$

Como

$$
|v_n|\to0
$$

y por álgebra

$$
M|v_n|\to0,
$$

el sándwich da

$$
u_nv_n\to0.
$$

Por otro lado, si además supiéramos que $(u_n)$ converge, el resultado sería un caso particular de la ley del producto. La estimación anterior es más fuerte para este propósito: **no exige que $(u_n)$ converja**, solo que esté acotada.

Esto explica por qué podemos controlar factores como

$$
(-1)^n,
\qquad
\sin n,
\qquad
\cos n,
$$

cuando aparecen multiplicados por una sucesión que tiende a cero.

### Una red mínima de límites que ya podemos reutilizar

Podemos reunir lo construido hasta ahora sin convertirlo en una lista aislada de recetas.

Sabemos que

$$
\frac1{n+1}\to0,
$$

que para cada $p\in\mathbb N_{>0}$,

$$
\frac1{(n+1)^p}\to0,
$$

y que si $|q|<1$,

$$
q^n\to0.
$$

Además, mediante álgebra y sándwich podemos obtener inmediatamente límites de expresiones construidas con estas piezas.

Por ejemplo,

$$
\frac{7}{(n+1)^3}\to0,
$$

$$
\left(-\frac45\right)^n\to0,
$$

y

$$
\frac{2+\sin n}{n+1}\to0,
$$

porque

$$
|2+\sin n|\le3.
$$

La meta de esta sección no era acumular ejemplos, sino disponer de unas pocas **unidades de construcción** cuyo origen conocemos.

### Qué no hemos utilizado

Es importante hacer explícita la frontera lógica de los argumentos.

Para obtener los límites de esta sección usamos:

- la propiedad arquimediana;
- inducción matemática;
- desigualdades elementales;
- álgebra de límites;
- preservación del orden;
- teorema del sándwich;
- valor absoluto.

No utilizamos:

- límites de funciones;
- continuidad;
- función exponencial real;
- logaritmos;
- derivadas;
- regla de l'Hôpital;
- series;
- subsucesiones;
- Bolzano–Weierstrass;
- criterio de Cauchy.

Esta auditoría importa porque el siguiente gran paso del capítulo será cualitativamente distinto.

Hasta ahora, en todos los límites que hemos demostrado, **ya conocíamos o sospechábamos el candidato** y después verificábamos que los términos se acercaban a él.

En §4.7 preguntaremos algo más profundo:

> ¿puede la estructura de $\mathbb R$ garantizar que una sucesión converge aunque todavía no conozcamos de antemano su límite?

La respuesta será afirmativa para sucesiones monótonas y acotadas. Allí aparecerá por primera vez en este capítulo la completitud de $\mathbb R$ como mecanismo directo de existencia de límites.

