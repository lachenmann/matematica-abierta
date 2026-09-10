### Laboratorio 4 — Cuando una prueba fallida descubre el teorema correcto

Sea

$$
f\colon A\to B
$$

y sean $E,F\subseteq A$.

Una igualdad tentadora es

$$
\boxed{f(E\setminus F)=f(E)\setminus f(F).}
$$

**Problema.** Investigar si la igualdad es siempre verdadera. No debemos comenzar buscando un contraejemplo al azar: intentemos primero demostrarla por doble inclusión y observemos dónde se detiene la prueba.

#### Diagnóstico

En §3.6 aprendimos que las imágenes directas pueden mezclar testigos distintos. Aquí aparece una dificultad parecida: que un punto $x$ no pertenezca a $F$ no impide, en principio, que otro punto $z\in F$ tenga la misma imagen.

La prueba debe revelar exactamente dónde importa esa posibilidad.

#### Primera inclusión

Tomemos

$$
y\in f(E)\setminus f(F).
$$

Como $y\in f(E)$, existe $x\in E$ tal que

$$
f(x)=y.
$$

Además,

$$
y\notin f(F).
$$

Si $x$ perteneciera a $F$, entonces $f(x)=y$ pertenecería a $f(F)$, contradicción. Por tanto,

$$
x\notin F.
$$

Así,

$$
x\in E\setminus F,
$$

y por ello

$$
y=f(x)\in f(E\setminus F).
$$

Hemos probado siempre que

$$
\boxed{f(E)\setminus f(F)\subseteq f(E\setminus F).}
$$

#### Intento de la inclusión inversa

Tomemos ahora

$$
y\in f(E\setminus F).
$$

Existe entonces $x\in E\setminus F$ tal que

$$
f(x)=y.
$$

Sabemos que $x\in E$, así que

$$
y\in f(E).
$$

Para concluir que

$$
y\in f(E)\setminus f(F)
$$

necesitamos demostrar

$$
y\notin f(F).
$$

Aquí se atasca la prueba. Del hecho

$$
x\notin F
$$

**no** podemos deducir automáticamente

$$
f(x)\notin f(F).
$$

Podría existir otro punto $z\in F$ con

$$
f(z)=f(x).
$$

Ese es el paso ilegítimo que habría que introducir para completar la demostración sin hipótesis adicionales.

#### La hipótesis que repara la prueba

Supongamos ahora que $f$ es inyectiva. Si $y=f(x)$ perteneciera también a $f(F)$, existiría $z\in F$ con

$$
f(z)=y=f(x).
$$

Por inyectividad,

$$
z=x.
$$

Pero $z\in F$ y $x\notin F$, contradicción. Por tanto,

$$
y\notin f(F),
$$

y obtenemos la inclusión inversa.

Así, bajo inyectividad,

$$
\boxed{f(E\setminus F)=f(E)\setminus f(F).}
$$

#### Contraejemplo sin inyectividad

Tomemos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

$$
E=\{-1\},
\qquad
F=\{1\}.
$$

Como $E\cap F=\varnothing$,

$$
E\setminus F=\{-1\},
$$

y por tanto

$$
f(E\setminus F)=\{1\}.
$$

Pero

$$
f(E)=\{1\}=f(F),
$$

de modo que

$$
f(E)\setminus f(F)=\varnothing.
$$

Así,

$$
\boxed{
\varnothing
=
f(E)\setminus f(F)
\subsetneq
f(E\setminus F)
=
\{1\}.
}
$$

#### Lectura de la solución

El laboratorio reproduce un patrón de investigación matemática muy útil:

$$
\boxed{
\text{conjetura}
\to
\text{intento de prueba}
\to
\text{punto de atasco}
\to
\text{hipótesis necesaria}
\to
\text{enunciado corregido}
\to
\text{contraejemplo sin la hipótesis}
}
$$

Una prueba que se atasca no es necesariamente tiempo perdido. Si sabemos leer el atasco, puede revelar la estructura exacta del resultado verdadero.

### Laboratorio 5 — Fabricar una inversa eligiendo la rama adecuada

Consideremos

$$
q\colon\mathbb R\to\mathbb R,
\qquad
q(x)=(x-2)^2+1.
$$

**Problema.** La función $q$ no es biyectiva. Construir dos restricciones naturales que sí sean biyectivas sobre su imagen y determinar sus inversas.

#### Diagnóstico

Hay dos fallos en la declaración original.

Primero,

$$
q(1)=2=q(3),
$$

así que $q$ no es inyectiva.

Segundo,

$$
q(x)=(x-2)^2+1\ge1,
$$

por lo que ningún real menor que $1$ pertenece a la imagen. Así, $q$ tampoco es sobreyectiva sobre $\mathbb R$.

La gráfica algebraica tiene un punto central en $x=2$. A la derecha de ese punto la regla es estrictamente creciente; a la izquierda es estrictamente decreciente. Eso sugiere dos restricciones posibles.

#### Primera rama: $x\ge2$

Definamos

$$
q_+\colon[2,\infty)\to[1,\infty),
\qquad
q_+(x)=(x-2)^2+1.
$$

Si

$$
2\le x_1<x_2,
$$

entonces

$$
q_+(x_2)-q_+(x_1)
=
(x_2-x_1)(x_1+x_2-4).
$$

El primer factor es positivo. Además, $x_2>2$ y $x_1\ge2$, así que

$$
x_1+x_2-4>0.
$$

Por tanto,

$$
q_+(x_1)<q_+(x_2).
$$

La función es estrictamente creciente y, en consecuencia, inyectiva.

Para demostrar sobreyectividad sobre $[1,\infty)$, sea $y\ge1$. Entonces

$$
y-1\ge0
$$

y podemos tomar

$$
x=2+\sqrt{y-1}\ge2.
$$

Se cumple

$$
q_+(x)
=
(\sqrt{y-1})^2+1
=
y.
$$

Así, $q_+$ es biyectiva. Resolviendo

$$
y=(x-2)^2+1
$$

con la condición $x\ge2$, obtenemos

$$
x-2=\sqrt{y-1},
$$

y por tanto

$$
\boxed{q_+^{-1}(y)=2+\sqrt{y-1},\qquad y\ge1.}
$$

#### Segunda rama: $x\le2$

Definamos ahora

$$
q_-\colon(-\infty,2]\to[1,\infty),
\qquad
q_-(x)=(x-2)^2+1.
$$

Si

$$
x_1<x_2\le2,
$$

entonces

$$
q_-(x_2)-q_-(x_1)
=
(x_2-x_1)(x_1+x_2-4).
$$

El primer factor es positivo, pero ahora

$$
x_1+x_2-4<0,
$$

porque $x_1<2$ y $x_2\le2$. Por tanto,

$$
q_-(x_2)<q_-(x_1),
$$

de modo que $q_-$ es estrictamente decreciente y, por ello, inyectiva.

Dado $y\ge1$, el número

$$
x=2-\sqrt{y-1}\le2
$$

satisface $q_-(x)=y$. Así, $q_-$ también es sobreyectiva sobre $[1,\infty)$ y por tanto biyectiva.

Esta vez la condición $x\le2$ selecciona el signo negativo:

$$
\boxed{q_-^{-1}(y)=2-\sqrt{y-1},\qquad y\ge1.}
$$

#### Lectura de la solución

No existe contradicción entre las dos fórmulas de inversa. No estamos afirmando que una misma función tenga dos inversas. Hemos construido **dos funciones distintas** mediante restricciones distintas del dominio:

$$
q_+
e q_-.
$$

Cada una posee su propia inversa única.

El patrón general es importante:

$$
\boxed{
\text{función no invertible}
\to
\text{localizar una región inyectiva}
\to
\text{restringir dominio}
\to
\text{ajustar codominio a la imagen}
\to
\text{invertir}
}
$$

### Laboratorio 6 — Una sucesión antes de hablar de límites

Definamos

$$
a\colon\mathbb N\to\mathbb R,
\qquad
 a(n)=\frac{n}{n+1},
$$

donde

$$
\mathbb N=\{0,1,2,\dots\}.
$$

**Problema.** Analizar esta regla utilizando únicamente el lenguaje funcional del capítulo: dominio, codominio, imagen, preimágenes puntuales, monotonía, inyectividad, sobreyectividad y gráfica. No debemos hablar todavía de convergencia.

#### Diagnóstico

La notación $a(n)$ puede hacer que el objeto parezca nuevo, pero estructuralmente no lo es. Tenemos simplemente una función cuyo dominio es $\mathbb N$.

La primera pregunta, por tanto, no es «¿a qué se acerca?», sino

$$
\boxed{\text{¿qué función es y qué propiedades funcionales tiene?}}
$$

#### Solución

El dominio es

$$
\mathbb N,
$$

y el codominio declarado es

$$
\mathbb R.
$$

Como $n\ge0$, el denominador $n+1$ es siempre positivo, de modo que la regla está definida para cada natural.

Podemos reescribir

$$
a(n)
=
1-\frac1{n+1}.
$$

En particular,

$$
0\le a(n)<1
$$

para todo $n\in\mathbb N$. Sin embargo, la imagen no es todo el intervalo $[0,1)$. Es el conjunto discreto

$$
\boxed{
\operatorname{Im}(a)
=
\left\{\frac{n}{n+1}:n\in\mathbb N\right\}
=
\left\{0,\frac12,\frac23,\frac34,\dots\right\}.
}
$$

Por ejemplo,

$$
a^{-1}\left(\left\{\frac12\right\}\right)=\{1\},
$$

$$
a^{-1}\left(\left\{\frac23\right\}\right)=\{2\},
$$

y

$$
a^{-1}(\{1\})=\varnothing.
$$

Estudiemos ahora la monotonía. Para $n\in\mathbb N$,

$$
a(n+1)-a(n)
=
\frac{n+1}{n+2}-\frac{n}{n+1}.
$$

Llevando a común denominador,

$$
a(n+1)-a(n)
=
\frac{(n+1)^2-n(n+2)}{(n+1)(n+2)}
=
\frac1{(n+1)(n+2)}.
$$

Como el denominador es positivo,

$$
a(n+1)>a(n).
$$

Más generalmente, si $m<n$, entonces

$$
\frac{m}{m+1}<\frac{n}{n+1},
$$

pues, al multiplicar por los denominadores positivos,

$$
m(n+1)<n(m+1)
$$

equivale a

$$
m<n.
$$

Así, $a$ es estrictamente creciente sobre $\mathbb N$. Por el teorema de §3.9,

$$
\boxed{a\text{ es inyectiva}.}
$$

No es sobreyectiva como función $\mathbb N\to\mathbb R$, porque, por ejemplo,

$$
2\notin\operatorname{Im}(a).
$$

Si en cambio consideramos

$$
a\colon\mathbb N\to\operatorname{Im}(a),
$$

la función es biyectiva. Para $y\in\operatorname{Im}(a)$, de

$$
y=\frac{n}{n+1}
$$

obtenemos

$$
y(n+1)=n,
$$

$$
y=n(1-y),
$$

y por tanto

$$
\boxed{n=\frac{y}{1-y}.}
$$

Así, sobre la imagen,

$$
a^{-1}(y)=\frac{y}{1-y}.
$$

No hay conflicto con el hecho de que la expresión de la derecha parezca real: si $y$ pertenece realmente a $\operatorname{Im}(a)$, ese cociente es precisamente el natural que produjo $y$.

La gráfica es

$$
\Gamma_a
=
\left\{
\left(n,\frac{n}{n+1}\right):n\in\mathbb N
\right\}.
$$

A diferencia de muchas gráficas anteriores, no forma una curva completa sobre un intervalo: solo contiene los puntos cuyas primeras coordenadas son naturales.

#### Lectura de la solución

Este objeto es lo que en el capítulo siguiente llamaremos una **sucesión real**. Pero todo lo que acabamos de hacer pertenece ya a la teoría de funciones:

$$
\boxed{
\text{sucesión}
=
\text{función con dominio }\mathbb N.
}
$$

Todavía no hemos preguntado si los valores «se acercan» a algún número ni hemos definido qué significaría rigurosamente esa frase. Esa será precisamente la nueva cuestión de `T1-C04`.

### Qué estructuras se combinaron

Las seis estaciones permiten revisar el capítulo como una red y no como una lista lineal.

- El Laboratorio 1 separó **restricciones de una expresión** de **datos de una función**.
- El Laboratorio 2 mostró simultáneamente la sensibilidad de inyectividad al dominio y de sobreyectividad al codominio.
- El Laboratorio 3 obligó a verificar **tipos** antes de componer y distinguió composición funcional de mera sustitución algebraica.
- El Laboratorio 4 utilizó una **prueba fallida** como instrumento para descubrir la hipótesis correcta.
- El Laboratorio 5 combinó restricción, monotonía, imagen, biyectividad e inversión.
- El Laboratorio 6 mostró que el siguiente objeto del curso, una sucesión, entra naturalmente en el lenguaje funcional ya construido.

La arquitectura general puede verse así:

$$
\boxed{
\begin{array}{c}
\text{función completa}
\to
\text{imagen/preimagen}
\to
\text{inyectividad/sobreyectividad}
\to
\text{composición}
\to
\text{inversa},\\[6pt]
\text{función}+\text{producto cartesiano}
\to
\text{gráfica},\\[6pt]
\text{función}+\text{orden}
\to
\text{monotonía}
\to
\text{inyectividad}.
\end{array}}
$$

### Un mapa de decisión antes del banco final

Cuando aparezca un problema funcional, conviene formular preguntas en un orden parecido al siguiente:

$$
\boxed{
\begin{array}{c}
\text{¿qué función es?}
\to
\text{dominio/codominio}
\to
\text{imagen/preimagen}\\
\to
\text{inyectiva/sobreyectiva?}
\to
\text{¿se compone?}
\to
\text{¿se puede invertir?}
\end{array}}
$$

El diagrama no es un algoritmo rígido. Algunas preguntas pueden no ser relevantes en un problema concreto. Su función es impedir que empecemos manipulando una fórmula antes de haber identificado la estructura matemática.

A ese eje principal podemos añadir dos preguntas transversales:

- **¿la gráfica aporta información útil?** Entonces conviene traducir entre puntos $(x,f(x))$ y propiedades funcionales, sin confundir imagen con codominio;
- **¿el dominio está ordenado?** Entonces puede ser útil estudiar monotonía, especialmente si buscamos inyectividad o una restricción invertible.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** En el Laboratorio 1, ¿por qué $[-2,2]$ no debe llamarse automáticamente «el dominio de $p$»?

**Respuesta.** Porque $[-2,2]$ es el dominio real máximo permitido por la expresión $\sqrt{4-x^2}$. Una función puede declararse sobre cualquier subconjunto adecuado de ese conjunto. El dominio forma parte de los datos de la función, no es siempre sinónimo de «todos los puntos donde la fórmula puede evaluarse».
:::

::: {.callout-tip title="Antes de seguir"}
**2.** En el Laboratorio 4, ¿qué inclusión sobre diferencias de imágenes es válida sin suponer inyectividad?

**Respuesta.** Siempre se cumple

$$
f(E)\setminus f(F)\subseteq f(E\setminus F).
$$

La inclusión inversa puede fallar porque un punto de $E\setminus F$ y otro punto de $F$ pueden compartir la misma imagen. La inyectividad elimina exactamente esa posibilidad.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Por qué las dos ramas del Laboratorio 5 no contradicen la unicidad de la función inversa?

**Respuesta.** Porque $q_+$ y $q_-$ son funciones distintas: tienen dominios distintos. Cada una posee una única inversa, y esas inversas son diferentes porque revierten asignaciones diferentes.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** En el Laboratorio 6, ¿por qué no podemos escribir

$$
\operatorname{Im}(a)=[0,1)?
$$

**Respuesta.** Porque $a$ solo toma valores correspondientes a entradas naturales. Aunque todos sus valores pertenecen a $[0,1)$, la mayoría de los números de ese intervalo no son alcanzados. Por ejemplo, no existe $n\in\mathbb N$ con $n/(n+1)=1/3$.
:::

### Lo que queda antes de cerrar el capítulo

La arquitectura conceptual de `T1-C03` está ya completa. La última sección será el banco final de ejercicios y soluciones.

Allí desaparecerá gran parte del andamiaje del laboratorio. El lector deberá decidir de manera autónoma qué herramientas utilizar entre

$$
\boxed{
\text{dominio/codominio}
+
\text{imagen/preimagen}
+
\text{clasificación}
+
\text{composición}
+
\text{inversa}
+
\text{gráfica}
+
\text{monotonía}.
}
$$

Además, algunas consignas exigirán construir contraejemplos, reparar afirmaciones falsas o diseñar restricciones que hagan posible una inversa. La cuestión central seguirá siendo la misma con la que comenzó el capítulo: antes de calcular, debemos saber **qué función tenemos delante**.
