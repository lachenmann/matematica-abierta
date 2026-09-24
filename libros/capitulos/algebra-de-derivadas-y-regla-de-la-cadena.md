---
title: "Álgebra de derivadas y regla de la cadena"
description: "Capítulo 7 de Cálculo para matemáticos: linealidad, producto, cociente, potencias y regla de la cadena; 40 ejercicios resueltos."
content-id: MA-BCH-0065
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas:
  - calculo
  - analisis
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: 2026-09-20
date-modified: 2026-09-20
prerequisites:
  - MA-BCH-0003
  - MA-BCH-0004
  - MA-BCH-0010
  - MA-BCH-0077
  - MA-BCH-0063
  - MA-BCH-0064
number-sections: true
number-depth: 2
number-offset: [6]
---

# Álgebra de derivadas y regla de la cadena {#sec-t1-c08}

En el capítulo anterior aprendimos a determinar la derivada de una función *en un punto*. Si $a$ pertenece al dominio $A$ de $f$ y es punto de acumulación de $A$, la existencia de $f'_A(a)$ significa que el cociente de incrementos tiene un límite real finito. Aprendimos también a interpretar ese número como el coeficiente de una aproximación afín cuyo error es despreciable frente al incremento.

Hasta aquí, las derivadas se han obtenido principalmente desde su definición. Pero las funciones que queremos estudiar rara vez llegan aisladas: se suman, se multiplican, se dividen y se componen. Por ejemplo, incluso cuando conocemos las derivadas de $f$ y de $g$, todavía debemos justificar qué podemos afirmar sobre $f+g$, $fg$, $f/g$ o $g\circ f$.

Este capítulo convierte la información diferencial puntual en un conjunto de procedimientos demostrados. Su propósito no será presentar una tabla para memorizar, sino descubrir **por qué funcionan las reglas, cuándo se pueden aplicar y qué afirmaciones no permiten hacer**. La regla de la cadena constituirá el punto culminante: componer funciones exige seguir el paso de los incrementos por dos escalas y no dividir por una cantidad que podría anularse.

La ruta de construcción será

$$
\boxed{
\text{cociente incremental}
\to\text{combinaciones lineales}
\to\text{producto}
\to\text{recíproco y cociente}
\to\text{potencias y racionales}
\to\text{composición y cadena}.
}
$$

Comenzaremos, sin embargo, con una dificultad previa. Conocer las derivadas de dos funciones no nos autoriza a trasladar mecánicamente a sus derivadas la operación con la que formamos una función nueva.

## Por qué las reglas de derivación necesitan demostración {#sec-t1-c08-01}

### Una conjetura natural que no resiste la definición

Consideremos dos funciones $f,g:\mathbb R\to\mathbb R$ diferenciables y formemos su producto puntual:

$$
(fg)(x)=f(x)g(x).
$$

Si conocemos $f'(a)$ y $g'(a)$, ¿bastará multiplicar ambas pendientes para obtener la pendiente de $fg$? Es tentador escribir

$$
\underbrace{(fg)'(a)}_{\text{pendiente del producto}}
\stackrel{?}{=}
\underbrace{f'(a)g'(a)}_{\text{producto de las pendientes}}.
$$

La igualdad tiene una apariencia razonable: como el producto se forma multiplicando valores, podría parecer que su derivada se forma multiplicando derivadas. Pero la apariencia de una fórmula no demuestra que describa el límite que define su miembro izquierdo.

::: {#exm-t1-0072}
**Dos pendientes iguales a $1$ cuyo producto tiene pendiente $2$.** Sean

$$
f(x)=x,\qquad g(x)=x,
\qquad x\in\mathbb R,
$$

y fijemos $a=1$. Desde la definición de derivada, para todo $h\ne0$,

$$
\frac{f(1+h)-f(1)}h
=\frac{(1+h)-1}{h}=1.
$$

Por tanto, $f'(1)=1$; exactamente el mismo cálculo da $g'(1)=1$. Si nuestra conjetura fuera correcta, tendríamos

$$
(fg)'(1)=f'(1)g'(1)=1.
$$

Sin embargo, el producto es la función $p(x)=(fg)(x)=x^2$. Su cociente incremental en $1$ es

$$
\begin{aligned}
\frac{p(1+h)-p(1)}h
&=\frac{(1+h)^2-1}{h}\\
&=\frac{2h+h^2}{h}\\
&=2+h,
\qquad h\ne0.
\end{aligned}
$$

La cancelación se efectuó **antes** de tomar el límite y solo para $h\ne0$; no se ha sustituido $h=0$ en una fracción indefinida. Al hacer $h\to0$ obtenemos

$$
\boxed{(fg)'(1)=2\ne1=f'(1)g'(1).}
$$

Este único caso refuta la presunta identidad universal $(fg)'=f'g'$. No hemos utilizado ninguna regla de derivación para el producto: hemos calculado las tres derivadas directamente mediante cocientes incrementales.
:::

Detengámonos en el paso que determina el resultado. Cuando ambos factores pasan de $1$ a $1+h$, el producto pasa de $1$ a

$$
(1+h)(1+h)=1+2h+h^2.
$$

La variación total es $2h+h^2$, no $h^2$. A escala de primer orden, los dos términos lineales aportan $2h$, mientras $h^2$ se vuelve despreciable frente a $h$. Este mecanismo elemental sugiere qué debe estudiar la verdadera regla del producto; **no constituye todavía su demostración para funciones arbitrarias**, que realizaremos en §7.3.

::: {.callout-important title="Diagnóstico: una fórmula falsa, no una excepción de cálculo"}
El problema no consiste en que $f(x)=g(x)=x$ sea un caso excepcional o en que hayamos elegido mal el punto. Una afirmación formulada para *todas* las funciones diferenciables queda refutada por un solo par admisible que incumpla su conclusión. Lo que falla es identificar la variación de un producto con el producto de las variaciones.
:::

### Recuperar el objeto que realmente estamos derivando

El capítulo anterior definió la derivada a partir de un **límite de cocientes de diferencias**. Para recordarlo con precisión, sea $u:A\to\mathbb R$, con $a\in A$ punto de acumulación, y consideremos el conjunto de incrementos admisibles

$$
H_a=\{h\in\mathbb R:a+h\in A\}.
$$

Si existe un límite real finito, entonces

$$
u'_A(a)=
\lim_{\substack{h\to0\\h\in H_a\setminus\{0\}}}
\frac{u(a+h)-u(a)}h.
$$

En particular, para $u=fg$ debemos comenzar por

$$
\frac{f(a+h)g(a+h)-f(a)g(a)}h,
\qquad h\in H_a\setminus\{0\}.
$$

**No** hemos demostrado que esta expresión pueda sustituirse por el producto de los cocientes incrementales de $f$ y de $g$. Sería necesario justificar primero una identidad algebraica que permitiera hacerlo, y el ejemplo anterior demuestra que la pretendida identidad no puede ser válida en general.

Tampoco debemos confundir este problema con el álgebra de límites estudiada en el capítulo 4. Si $F(h)\to L$ y $G(h)\to M$, sabemos que $F(h)G(h)\to LM$. Ese teorema permite pasar al límite **una vez que hemos expresado correctamente** el cociente de diferencias; no nos dice que el cociente del incremento de $fg$ sea el producto de los cocientes de sus factores.

La estrategia matemática será, por tanto, siempre la misma: escribir la diferencia que corresponde a la función nueva, encontrar una transformación algebraica válida para incrementos admisibles no nulos y solo entonces utilizar los teoremas de límites. En §7.2 veremos que las combinaciones lineales admiten una descomposición inmediata; el producto requerirá una idea adicional.

### La segunda lectura: qué ocurre con las aproximaciones locales

Hay otra manera de apreciar la dificultad, sin inventar una regla. El capítulo 6 demostró que, cuando $f$ es diferenciable en $a$,

$$
f(a+h)=f(a)+f'_A(a)h+r_f(h),
\qquad r_f(h)=o(h),
$$

para incrementos admisibles. Existe una expresión análoga para $g$. Esta fórmula enseña a separar **valor central, variación lineal y error menor que el incremento**.

En nuestro ejemplo, al tomar $a=1$, ambas aproximaciones son exactas:

$$
f(1+h)=1+h,
\qquad
g(1+h)=1+h.
$$

El producto muestra inmediatamente por qué no basta multiplicar los coeficientes $1$ y $1$: también intervienen los valores centrales de los factores. En capítulos posteriores veremos que la perspectiva de los residuos permite seguir composiciones enteras de aproximaciones; por ahora solo necesitamos advertir que **operar con funciones no equivale a operar sin más con sus pendientes**.

### Antes de aplicar una regla: cuatro preguntas

De aquí en adelante, una operación con funciones deberá pasar por una auditoría breve:

1. **¿Qué función nueva hemos formado y en qué dominio está definida?** Una suma o un producto de funciones con dominios distintos solo tiene sentido donde ambas estén definidas; el cociente exige, además, un denominador no nulo.
2. **¿En qué punto calculamos y qué incrementos son admisibles?** El punto debe pertenecer al dominio pertinente y ser punto de acumulación para que exista una derivada en nuestro sentido. En extremos de dominio trabajaremos con límites relativos, no con extensiones supuestas.
3. **¿Qué hipótesis conocemos realmente?** Que dos funciones sean diferenciables en un punto es un dato que podemos usar; que su combinación sea diferenciable y satisfaga cierta fórmula es precisamente lo que habrá que demostrar.
4. **¿Qué identidad y qué límite justifican la conclusión?** La transformación debe ser válida antes del paso al límite y no puede introducir divisiones por cantidades posiblemente nulas.

Estas preguntas distinguen dos actividades que suelen mezclarse en un cálculo rutinario: **probar una regla** y **aplicarla después de haber comprobado sus hipótesis**. Una prueba de suficiencia tampoco demostraría, por sí sola, que las mismas hipótesis fueran necesarias.

::: {.callout-note title="Antes de seguir"}
Reconstruye sin consultar el ejemplo: si $p(x)=x^2$, ¿por qué el cociente incremental en $1$ vale $2+h$ y no $1$? Señala exactamente dónde es lícito cancelar $h$ y qué límite se usa después. A continuación, explica en una frase por qué el teorema del límite de un producto no permite afirmar $(fg)'=f'g'$.
:::

### El programa demostrativo del capítulo

La primera regla que investigaremos será la de las **combinaciones lineales**, porque sus incrementos se separan mediante la propia distributividad de los números reales. Después estudiaremos el producto y descubriremos qué término intermedio permite controlar sus dos factores. El recíproco y el cociente exigirán, además, demostrar que un denominador no nulo en el centro permanece no nulo cerca de él. Con esas herramientas construiremos las derivadas de potencias enteras, polinomios y funciones racionales.

Por último abordaremos las composiciones. En ellas, el incremento de la función interior puede anularse incluso cuando el incremento de entrada es distinto de cero. Una demostración correcta de la regla de la cadena deberá funcionar también en ese caso, sin introducir una división ilegítima.

Así, el compromiso de este capítulo puede formularse en una sola frase:

$$
\boxed{\text{Primero justificar la transformación; después utilizar la fórmula.}}
$$

La siguiente sección comienza por la situación algebraicamente más sencilla: demostrar, desde la definición, cómo se comporta la derivada frente a la suma y la multiplicación por escalares.

## La derivación respeta combinaciones lineales {#sec-t1-c08-02}

### ¿Qué hace distinta a una suma?

En §7.1 vimos que no hay razón para identificar el incremento de un producto con el producto de los incrementos. La suma plantea una situación diferente. Si una función cambia en cierta cantidad y otra cambia en otra cantidad, la variación de su suma es *exactamente* la suma de esas dos variaciones. No hay términos adicionales que controlar. La misma observación vale cuando multiplicamos previamente cada función por un número fijo.

Sean $f,g:A\to\mathbb R$, con $a\in A$ punto de acumulación de $A$, y sean $\alpha,\beta\in\mathbb R$. Definimos sobre el **mismo dominio** $A$ la función

$$
u(x)=\alpha f(x)+\beta g(x),\qquad x\in A.
$$

¿Qué información necesitamos para afirmar que $u$ es diferenciable en $a$? No basta advertir que la fórmula tiene la forma de una combinación lineal: debemos mostrar que su cociente incremental posee un límite real finito. El trabajo algebraico, esta vez, es directo.

::: {#thm-t1-0027}
**Teorema — Linealidad de la derivada.** Sean $A\subseteq\mathbb R$, $a\in A$ un punto de acumulación de $A$ y $f,g:A\to\mathbb R$ diferenciables en $a$ relativamente a $A$. Para cualesquiera escalares $\alpha,\beta\in\mathbb R$, la función $u=\alpha f+\beta g:A\to\mathbb R$ es diferenciable en $a$ y satisface

$$
\boxed{u'_A(a)=\alpha f'_A(a)+\beta g'_A(a).}
$$

**Demostración.** Consideremos el conjunto de incrementos admisibles $H_a=\{h\in\mathbb R:a+h\in A\}$. Para $h\in H_a\setminus\{0\}$, la definición puntual de $u$ y las propiedades distributivas de los números reales dan la identidad exacta

$$
\begin{aligned}
\frac{u(a+h)-u(a)}{h}
&=\frac{\alpha f(a+h)+\beta g(a+h)-\alpha f(a)-\beta g(a)}{h}\\
&=\alpha\frac{f(a+h)-f(a)}h
 +\beta\frac{g(a+h)-g(a)}h.
\end{aligned}
$$

Por hipótesis, los dos cocientes del último miembro convergen a $f'_A(a)$ y $g'_A(a)$, respectivamente, cuando $h\to0$ a través de $H_a\setminus\{0\}$. El álgebra de límites funcionales, demostrada en el capítulo 4, permite multiplicarlos por los escalares fijos y sumarlos. En consecuencia,

$$
\lim_{\substack{h\to0\\h\in H_a\setminus\{0\}}}
\frac{u(a+h)-u(a)}h
=\alpha f'_A(a)+\beta g'_A(a)\in\mathbb R.
$$

El límite es finito, por lo que $u$ es diferenciable en $a$ según la definición del capítulo 6, y el número obtenido es precisamente su derivada. $\square$
:::

**Lectura de la prueba.** El primer paso es un hecho de álgebra de *valores*: la diferencia de una combinación lineal se separa en las diferencias de sus componentes. El segundo paso es un hecho de *análisis*: cada cociente tiene un límite por una hipótesis explícita. Solo después se usa el álgebra de límites. La existencia de la derivada de $u$ es una **conclusión**; no se presupone para manipular el cociente. Tampoco hemos usado la regla del producto, que aún no está demostrada.

### Suma, resta y multiplicación por constantes: una sola regla

El teorema comprende varias fórmulas familiares, sin necesidad de repetir la demostración. Si $\alpha=\beta=1$,

$$
(f+g)'_A(a)=f'_A(a)+g'_A(a).
$$

Si $\alpha=1$ y $\beta=-1$, obtenemos

$$
(f-g)'_A(a)=f'_A(a)-g'_A(a).
$$

Si $\beta=0$, la combinación es $\alpha f$, y el resultado se reduce a

$$
(\alpha f)'_A(a)=\alpha f'_A(a).
$$

El caso $\alpha=0$ no requiere dividir por $\alpha$ ni tratarlo como una excepción: el teorema lo incluye. Una función constante $c$ tiene derivada $0$ por cálculo directo desde la definición (capítulo 6), pues su cociente incremental es siempre $0$. Así, añadir una constante modifica el valor central y la altura de la tangente, pero no su pendiente:

$$
(f+c)'_A(a)=f'_A(a).
$$

Esta última afirmación es *puntual*: solo requiere que $f$ sea diferenciable en $a$. No afirma por sí misma que $f$ sea diferenciable en los demás puntos de $A$.

### Verificar una fórmula por dos caminos

::: {#exm-t1-0073}
**Una combinación de dos funciones conocidas.** Sean $f(x)=x^2$ y $g(x)=x$ sobre $\mathbb R$, y formemos

$$
u(x)=3f(x)-2g(x)=3x^2-2x.
$$

Fijemos un $a\in\mathbb R$ cualquiera. **Primera ruta: desde la definición.** Para $h\ne0$,

$$
\begin{aligned}
\frac{u(a+h)-u(a)}h
&=\frac{3(a+h)^2-2(a+h)-(3a^2-2a)}h\\
&=\frac{6ah+3h^2-2h}{h}\\
&=6a+3h-2.
\end{aligned}
$$

El límite cuando $h\to0$ existe y vale $6a-2$. Por tanto, $u'(a)=6a-2$.

**Segunda ruta: aplicar el teorema recién demostrado.** Los cocientes incrementales de las funciones de partida, calculados en C07, dan $f'(a)=2a$ y $g'(a)=1$. Como ambas son diferenciables en $a$ y comparten dominio,

$$
u'(a)=3f'(a)-2g'(a)=3(2a)-2(1)=6a-2.
$$

Las dos rutas coinciden. La primera verifica el cálculo directamente; la segunda ilustra cómo un teorema demostrado ahorra rehacer expansiones y límites cada vez. La segunda ruta **no** sustituye la prueba general: solo es legítima porque @thm-t1-0027 ya ha sido establecido.
:::

### ¿Por qué también funcionan las combinaciones finitas?

El teorema trata dos funciones, pero una suma finita no debe quedar como una extrapolación informal. Sean $f_1,\ldots,f_n:A\to\mathbb R$ diferenciables en un mismo punto de acumulación $a\in A$, y $c_1,\ldots,c_n\in\mathbb R$, con $n\ge1$. Se afirma que

$$
\left(\sum_{k=1}^n c_k f_k\right)'_A(a)
=\sum_{k=1}^n c_k f'_{k,A}(a).
$$

**Demostración por inducción sobre $n$.** Para $n=1$, es el caso de multiplicación escalar del teorema. Supongamos demostrada la afirmación para $n$ funciones. La suma parcial $s_n=\sum_{k=1}^n c_k f_k$ es entonces diferenciable en $a$ y tiene derivada $\sum_{k=1}^n c_k f'_{k,A}(a)$. Aplicando @thm-t1-0027 a $s_n$ y $f_{n+1}$ con coeficientes $1$ y $c_{n+1}$, concluimos que $s_n+c_{n+1}f_{n+1}$ es diferenciable y que

$$
\begin{aligned}
(s_n+c_{n+1}f_{n+1})'_A(a)
&=s'_{n,A}(a)+c_{n+1}f'_{n+1,A}(a)\\
&=\sum_{k=1}^{n+1}c_k f'_{k,A}(a).
\end{aligned}
$$

Esto cierra el paso inductivo. Se trata de una **suma finita**; no hemos afirmado que se pueda intercambiar derivación y una serie infinita, problema que requerirá hipótesis adicionales en el Tomo II.

Si todas las funciones son diferenciables en cada punto de un conjunto $E\subseteq A$ cuyos puntos sean de acumulación de $A$, podemos reunir las igualdades puntuales en una igualdad de funciones sobre $E$:

$$
D(\alpha f+\beta g)=\alpha Df+\beta Dg
\qquad\text{en }E.
$$

Aquí $Df$ es la función derivada donde está definida; $D$ no introduce una segunda definición de derivada. La fórmula funcional **no** extiende automáticamente las derivadas a puntos fuera de $E$.

### Las hipótesis no son decoración

El dominio común del teorema garantiza que los tres cocientes —el de $f$, el de $g$ y el de $\alpha f+\beta g$— se calculan mediante los mismos incrementos admisibles. Si dos funciones vienen dadas sobre dominios $A$ y $B$ distintos, primero se define su suma sobre $C=A\cap B$. Solo podemos aplicar la regla cuando $a\in C$ es punto de acumulación de $C$ y ambas restricciones a $C$ son diferenciables en $a$.

Por ejemplo, tomemos

$$
A=\{0\}\cup\{1/n:n\in\mathbb N,\ n\ge1\},
\qquad
B=\{0\}\cup\{-1/n:n\in\mathbb N,\ n\ge1\}.
$$

El punto $0$ es de acumulación de ambos conjuntos. Las funciones constantes nulas sobre $A$ y sobre $B$ son diferenciables en $0$ con derivada relativa $0$. Sin embargo, $A\cap B=\{0\}$, cuyo único punto es aislado; de acuerdo con nuestra definición, **la suma definida exclusivamente en la intersección no tiene derivada relativa en $0$**. No es una falla de la fórmula algebraica, sino la desaparición de los incrementos con los que se define el límite.

En cambio, en el extremo $a=0$ de $A=[0,\infty)$, dos funciones diferenciables relativamente a $A$ sí satisfacen el teorema con incrementos $h>0$; no hace falta inventar extensiones ni suponer derivadas bilaterales.

::: {.callout-important title="Qué se ha probado y qué no"}
La diferenciabilidad de **ambas** funciones sobre el mismo dominio en $a$ es una hipótesis suficiente para que su combinación lineal sea diferenciable allí. No es una condición necesaria: por ejemplo, $f(x)=|x|$ y $g(x)=-|x|$ no son diferenciables en $0$, mientras $f+g=0$ sí lo es. Por tanto, de la diferenciabilidad de una suma no se deduce que cada sumando sea diferenciable. Tampoco se deduce ninguna regla para $fg$ o para $g\circ f$; esas operaciones tienen incrementos de otra forma.
:::

### Reconstruir la estrategia

Antes de pasar a la siguiente regla, intenta explicar qué diferencia hay entre la identidad algebraica de incrementos y el teorema analítico de existencia del límite. ¿Qué hipótesis asegura cada límite por separado? ¿Por qué el caso de un coeficiente cero no exige una prueba nueva? ¿Dónde interviene la inducción para pasar de dos funciones a un número finito de funciones? Si puedes responder sin recurrir a una tabla de fórmulas, has reconstruido la arquitectura de la prueba.

La próxima sección estudiará un producto. Su incremento ya no se separa por simple distributividad en dos diferencias independientes: tendremos que **inventar un término intermedio** para encontrar una identidad útil, y justificar un límite adicional mediante continuidad.

## La regla del producto: separar una variación en dos {#sec-t1-c08-03}

### Una diferencia que no se deja repartir directamente

En §7.1 calculamos, desde la definición, que el producto de dos funciones con pendiente $1$ puede tener pendiente $2$. Ya sabemos, por tanto, que la fórmula $(fg)'=f'g'$ es falsa en general. El problema no se resuelve memorizando una expresión diferente: necesitamos descubrir una **identidad algebraica verdadera** para el incremento del producto.

Sean $f,g:A\to\mathbb R$ y $a\in A$. Para un incremento $h$ tal que $a+h\in A$, escribamos abreviadamente

$$
\Delta f=f(a+h)-f(a),\qquad
\Delta g=g(a+h)-g(a).
$$

El producto cambia desde $f(a)g(a)$ hasta $f(a+h)g(a+h)$. Si intentamos describir esa variación solo mediante $\Delta f\,\Delta g$, perdemos el efecto de los valores iniciales. Una manera de recuperar toda la información consiste en efectuar el cambio **en dos etapas**: primero modificamos un factor y después el otro. Introducimos el valor intermedio $f(a+h)g(a)$, que pertenece a la misma aritmética real y no requiere ninguna hipótesis analítica:

$$
\begin{aligned}
f(a+h)g(a+h)-f(a)g(a)
&=f(a+h)g(a+h)-f(a+h)g(a)\\
&\quad+f(a+h)g(a)-f(a)g(a)\\
&=f(a+h)\bigl(g(a+h)-g(a)\bigr)\\
&\quad+g(a)\bigl(f(a+h)-f(a)\bigr).
\end{aligned}
$$

Esta identidad vale para **todos** los incrementos admisibles, incluso $h=0$. Solo al dividirla por $h$ exigiremos $h\ne0$. La prueba general podrá construirse ahora con resultados de límites que ya conocemos.

::: {#thm-t1-0028}
**Teorema — Regla del producto.** Sean $A\subseteq\mathbb R$, $a\in A$ un punto de acumulación de $A$ y $f,g:A\to\mathbb R$ diferenciables en $a$ relativamente a $A$. Entonces el producto puntual $p=fg:A\to\mathbb R$ es diferenciable en $a$ y

$$
\boxed{(fg)'_A(a)=f'_A(a)g(a)+f(a)g'_A(a).}
$$

**Demostración.** Sea

$$
H_a=\{h\in\mathbb R:a+h\in A\}.
$$

Para cada $h\in H_a\setminus\{0\}$, la identidad anterior y la división legítima por $h$ proporcionan

$$
\begin{aligned}
\frac{p(a+h)-p(a)}h
&=f(a+h)\frac{g(a+h)-g(a)}h\\
&\quad+g(a)\frac{f(a+h)-f(a)}h.
\end{aligned}
$$

Identifiquemos **cada límite antes de combinarlo**. Por hipótesis de diferenciabilidad,

$$
\frac{f(a+h)-f(a)}h\longrightarrow f'_A(a),
\qquad
\frac{g(a+h)-g(a)}h\longrightarrow g'_A(a)
$$

cuando $h\to0$ a través de $H_a\setminus\{0\}$. Además, la diferenciabilidad de $f$ implica su continuidad relativa en $a$, por @thm-t1-0024; por tanto,

$$
f(a+h)\longrightarrow f(a).
$$

El número $g(a)$ permanece fijo. Aplicamos ahora, y solo ahora, el álgebra de límites a los dos sumandos del cociente incremental:

$$
\begin{aligned}
\lim_{\substack{h\to0\\h\in H_a\setminus\{0\}}}
\frac{p(a+h)-p(a)}h
&=f(a)g'_A(a)+g(a)f'_A(a)\\
&=f'_A(a)g(a)+f(a)g'_A(a).
\end{aligned}
$$

El resultado es un número real finito. En consecuencia, el límite que **define** $p'_A(a)$ existe y coincide con el miembro derecho de la fórmula. $\square$
:::

**Auditoría de la prueba.** La identidad algebraica produce dos términos, no el producto de dos cocientes incrementales. Las hipótesis aportan los límites de esos cocientes. El factor adicional $f(a+h)$ tiene límite porque diferenciabilidad implica continuidad, un resultado demostrado antes de este capítulo. La existencia de $(fg)'_A(a)$ es la conclusión de la prueba, no una premisa encubierta.

### Leer la fórmula sin perder los valores centrales

La igualdad del teorema tiene dos contribuciones: el cambio de $f$ ponderado por el valor de $g$ en el centro, y el cambio de $g$ ponderado por el valor de $f$ en el centro. Conviene leerla como

$$
\boxed{\text{variación de primer orden del producto}
=\text{primer factor variable}+\text{segundo factor variable}.}
$$

El orden de los sumandos es indiferente, pero sus **factores no son intercambiables arbitrariamente**: en cada término aparece una derivada y el *valor* del otro factor. La fórmula no contiene $f'_A(a)g'_A(a)$ como único término.

::: {#exm-t1-0074}
**Verificación directa en dos funciones polinómicas.** Tomemos $f(x)=x^2$, $g(x)=x+1$ sobre $\mathbb R$ y fijemos un $a\in\mathbb R$. Por el capítulo 6, $f'(a)=2a$ y $g'(a)=1$. El teorema, cuyas hipótesis se cumplen, da

$$
\begin{aligned}
(fg)'(a)
&=2a(a+1)+a^2\\
&=3a^2+2a.
\end{aligned}
$$

Comprobemos el mismo resultado **sin aplicar la regla del producto**. Como $p(x)=x^3+x^2$, expandimos directamente para $h\ne0$:

$$
\begin{aligned}
\frac{p(a+h)-p(a)}h
&=\frac{(a+h)^3+(a+h)^2-a^3-a^2}{h}\\
&=3a^2+2a+(3a+1)h+h^2.
\end{aligned}
$$

Al tomar el límite obtenemos $p'(a)=3a^2+2a$. Los dos caminos coinciden. Esta comprobación particular no reemplaza la demostración universal: muestra cómo utilizarla y cómo contrastar un cálculo cuando existe una ruta independiente.
:::

### ¿Qué ocurre si un factor vale cero?

El teorema **no exige** que $f(a)$ ni $g(a)$ sean distintos de cero. Si $f(a)=0$, la fórmula se simplifica a

$$
(fg)'_A(a)=f'_A(a)g(a).
$$

Si además $g(a)=0$, entonces $(fg)'_A(a)=0$, aunque las derivadas de los factores puedan ser no nulas. Por ejemplo, $f(x)=g(x)=x$ en $a=0$ tiene $f'(0)=g'(0)=1$, pero $(x^2)'(0)=0$. Esto no contradice el contraejemplo de §7.1, que utilizó el **mismo par de funciones en otro punto**, $a=1$. Los valores centrales son parte indispensable de la regla.

### De dos factores a un producto finito

La regla también permite derivar un producto de un número finito de factores sin inventar una fórmula nueva para cada cantidad. Si $f_1,\ldots,f_n:A\to\mathbb R$ son diferenciables en $a$, con $n\ge2$, entonces el producto $P=\prod_{j=1}^n f_j$ es diferenciable en $a$ y

$$
\boxed{
P'_A(a)=\sum_{k=1}^n f'_{k,A}(a)
\prod_{\substack{1\le j\le n\\j\ne k}}f_j(a).}
$$

**Demostración por inducción.** Para $n=2$ es el teorema recién probado. Supongamos conocida la afirmación para $n$ factores y pongamos $P_n=\prod_{j=1}^n f_j$. Por la hipótesis inductiva, $P_n$ es diferenciable. La regla del producto aplicada a $P_{n+1}=P_nf_{n+1}$ produce

$$
\begin{aligned}
P'_{n+1,A}(a)
&=P'_{n,A}(a)f_{n+1}(a)
+P_n(a)f'_{n+1,A}(a)\\
&=\sum_{k=1}^{n+1}f'_{k,A}(a)
\prod_{\substack{1\le j\le n+1\\j\ne k}}f_j(a).
\end{aligned}
$$

La última igualdad reúne los $n$ términos inductivos y el término correspondiente a $k=n+1$. Así queda justificada la fórmula para todo $n\ge2$. **No hemos probado** una regla para productos infinitos; la inducción solo permite un número finito de factores.

### Una segunda lectura mediante la aproximación afín

Podemos comprobar conceptualmente por qué aparecen precisamente los dos términos del teorema. La linealización demostrada en el capítulo 6 permite escribir, para incrementos admisibles,

$$
\begin{aligned}
f(a+h)&=f(a)+f'_A(a)h+r_f(h),\\
g(a+h)&=g(a)+g'_A(a)h+r_g(h),
\end{aligned}
$$

con $r_f(h)=o(h)$ y $r_g(h)=o(h)$. Multiplicamos las expresiones y sustraemos $f(a)g(a)$. Los términos lineales en $h$ son exactamente

$$
\bigl(f'_A(a)g(a)+f(a)g'_A(a)\bigr)h.
$$

¿Por qué lo demás es $o(h)$? Los términos $f(a)r_g(h)$ y $g(a)r_f(h)$ son $o(h)$; los productos de $h$ por un residuo y el producto de residuos también son $o(h)$ porque $r_f(h)/h\to0$, $r_g(h)/h\to0$ y, por consiguiente, ambos residuos tienden a cero. El término $f'_A(a)g'_A(a)h^2$ es asimismo $o(h)$. La interpretación afín confirma así la misma fórmula sin asumir ninguna regla posterior. No la necesitamos para establecer el teorema —la prueba por cocientes ya lo hizo—, pero revela por qué el producto de dos aproximaciones de primer orden conserva dos contribuciones lineales.

### Dominios distintos, extremos y límites de la inferencia

La hipótesis de **dominio común** no es decorativa. Si inicialmente $f:A\to\mathbb R$ y $g:B\to\mathbb R$, definimos $fg$ sobre $C=A\cap B$. Para aplicar la regla en $a\in C$ debemos verificar que $a$ sea punto de acumulación de $C$ y que las **restricciones** $f|_C$ y $g|_C$ sean diferenciables en $a$ relativamente a $C$. La diferenciabilidad de las funciones originales, por sí sola, no asegura que el producto tenga derivada si la intersección carece de puntos próximos distintos de $a$, tal como comprobamos para sumas en §7.2.

En un extremo, por ejemplo $a=0$ para $A=[0,\infty)$, la prueba permanece válida con incrementos admisibles $h>0$. No hemos supuesto derivadas bilaterales ni prolongaciones fuera de $A$.

::: {.callout-warning title="La conclusión no se puede invertir"}
Que $fg$ sea diferenciable en $a$ no implica que **ambos** factores lo sean. En $\mathbb R$, la función $f(x)=|x|$ no es diferenciable en $0$, mientras que $g(x)=0$ y $fg=0$ sí lo son. La regla demostrada es una **condición suficiente** para la diferenciabilidad del producto, no una caracterización necesaria de los factores.
:::

### Antes de continuar

Reconstruye la prueba sin mirar la fórmula: ¿qué valor agregamos y sustraemos para separar el incremento del producto? ¿Qué límite exige invocar derivabilidad $\Rightarrow$ continuidad? ¿Por qué la expresión tiene sentido incluso si $f(a)=0$ o $g(a)=0$? ¿Qué cambia si las funciones se han definido sobre dominios distintos? Identificar estas cuatro decisiones prepara el siguiente problema: **el recíproco y el cociente exigirán además controlar que un denominador no se anule cerca del punto**. Esa será la tarea de §7.4.

## Recíprocos y cocientes: la hipótesis que impide dividir por cero {#sec-t1-c08-04}

### Antes de derivar, determinar dónde existe la función

En §7.3 no exigimos que ninguno de los factores de un producto fuera distinto de cero. Para formar un recíproco la situación cambia: la expresión $1/g(x)$ solo define un valor real cuando $g(x)\ne0$. La primera pregunta no es, por tanto, «¿qué fórmula de derivación usamos?», sino **«¿en qué conjunto está definida la función que pretendemos derivar?»**.

Sean $g:A\to\mathbb R$ y $a\in A$, donde $A\subseteq\mathbb R$ y $a$ es punto de acumulación de $A$. Definamos el dominio natural del recíproco:

$$
A_g=\{x\in A:g(x)\ne0\}.
$$

Aunque $g(a)\ne0$ garantiza que $a\in A_g$, todavía debemos justificar que hay puntos de $A_g$ arbitrariamente próximos a $a$ y que allí los denominadores no se anulan. La diferenciabilidad de $g$ proporciona precisamente el control que necesitamos.

### La no anulación local no es una suposición adicional

Supongamos que $g$ es diferenciable relativamente a $A$ en $a$ y que $g(a)\ne0$. Por el teorema «diferenciabilidad implica continuidad» (@thm-t1-0024), $g$ es continua relativamente a $A$ en $a$. Apliquemos la definición de continuidad con la tolerancia positiva $\varepsilon=|g(a)|/2$. Existe $\delta>0$ tal que, para todo $x\in A$ con $|x-a|<\delta$,

$$
|g(x)-g(a)|<\frac{|g(a)|}{2}.
$$

Por la desigualdad triangular inversa,

$$
|g(x)|\ge |g(a)|-|g(x)-g(a)|
>\frac{|g(a)|}{2}>0.
$$

En particular, $g(x)\ne0$ para todos esos puntos. Hemos obtenido una **cota inferior cuantitativa** para el valor absoluto del denominador; no hemos supuesto que el cociente exista fuera del dominio $A_g$. Además, $A$ y $A_g$ coinciden dentro del entorno relativo $A\cap(a-\delta,a+\delta)$. Como $a$ es punto de acumulación de $A$, también lo es de $A_g$.

Esta coincidencia local permite usar la derivada de $g$ relativa a $A$ al calcular límites a través de $A_g$. No hemos extendido la función a puntos nuevos: solo hemos reconocido que la restricción $g|_{A_g}$ conserva, cerca de $a$, los mismos incrementos admisibles.

::: {#prp-t1-0039}
**Proposición — Derivada del recíproco.** Sean $A\subseteq\mathbb R$, $a\in A$ un punto de acumulación y $g:A\to\mathbb R$ diferenciable en $a$ relativamente a $A$. Si $g(a)\ne0$, entonces $a$ es punto de acumulación de $A_g=\{x\in A:g(x)\ne0\}$, la función

$$
r:A_g\to\mathbb R,\qquad r(x)=\frac1{g(x)},
$$

es diferenciable en $a$ relativamente a $A_g$ y satisface

$$
\boxed{r'_{A_g}(a)=-\frac{g'_A(a)}{g(a)^2}.}
$$

**Demostración.** La continuidad de $g$ y la condición $g(a)\ne0$ garantizan, por el argumento precedente, que existe $\delta>0$ tal que $g(a+h)\ne0$ cuando $a+h\in A$ y $|h|<\delta$. También garantizan que $a$ es punto de acumulación de $A_g$.

Para cada incremento $h\ne0$ admisible suficientemente pequeño, la identidad algebraica

$$
\frac1{g(a+h)}-\frac1{g(a)}
=\frac{g(a)-g(a+h)}{g(a+h)g(a)}
$$

es válida porque **ambos denominadores son no nulos**. Dividiendo ahora por $h$ obtenemos

$$
\frac{r(a+h)-r(a)}h
=-\frac{g(a+h)-g(a)}h\,
  \frac1{g(a+h)g(a)}.
$$

El primer factor converge a $-g'_A(a)$ por definición de derivada; la coincidencia local de $A$ y $A_g$ justifica el dominio del límite. Por continuidad, $g(a+h)\to g(a)$, y el límite del producto de denominadores es $g(a)^2\ne0$. El teorema del límite de un recíproco, que es un resultado previo sobre límites y **no** la regla de derivación que estamos probando, permite concluir

$$
\lim_{\substack{h\to0\\a+h\in A_g,\ h\ne0}}
\frac1{g(a+h)g(a)}=\frac1{g(a)^2}.
$$

Multiplicando los dos límites se sigue que el cociente incremental de $r$ converge a $-g'_A(a)/g(a)^2$, un número real finito. Esto demuestra la diferenciabilidad y la fórmula. $\square$
:::

**Lectura de la prueba.** La hipótesis $g(a)\ne0$ actúa en tres lugares: define el recíproco en el centro, proporciona no anulación local mediante continuidad y permite tomar el límite del denominador. La derivada no se obtuvo «derivando el uno y el denominador»: se obtuvo de una identidad de diferencias, seguida de límites previamente justificados.

### Un recíproco en todo su dominio

::: {#exm-t1-0075}
**La función $r(x)=1/(1+x^2)$.** Definamos $g(x)=1+x^2$ sobre $\mathbb R$. Como $x^2\ge0$, se cumple $g(x)\ge1>0$ para todo $x\in\mathbb R$. Por tanto, el dominio natural de $r$ es todo $\mathbb R$. La derivada de $x^2$, calculada directamente en el capítulo 6, y la linealidad de §7.2 dan $g'(a)=2a$.

Aplicando la proposición, válida en cada $a\in\mathbb R$, obtenemos

$$
\boxed{r'(a)=-\frac{2a}{(1+a^2)^2}.}
$$

En particular, $r'(0)=0$ y $r'(1)=-1/2$. Podemos verificar el primer valor independientemente: para $h\ne0$,

$$
\frac{r(h)-r(0)}h
=\frac{\frac1{1+h^2}-1}{h}
=-\frac{h}{1+h^2}\longrightarrow0.
$$

Aquí la no anulación es global y explícita. El teorema general, en cambio, solo requiere controlar el denominador cerca del punto considerado.
:::

### El cociente se construye a partir del producto y del recíproco

Ahora sean $f,g:A\to\mathbb R$ diferenciables relativamente a $A$ en $a$, con $g(a)\ne0$. El cociente original tiene dominio

$$
A_g=\{x\in A:g(x)\ne0\},\qquad
q:A_g\to\mathbb R,\quad q(x)=\frac{f(x)}{g(x)}.
$$

Por el control de no anulación, $A_g$ coincide con $A$ suficientemente cerca de $a$. En particular, las restricciones de $f$ y $g$ a $A_g$ tienen en $a$ las mismas derivadas relativas que las funciones originales. Podemos escribir entonces $q=(f|_{A_g})r$, donde $r=1/(g|_{A_g})$, y aplicar **en ese orden** la proposición recién demostrada y la regla del producto de §7.3.

::: {#thm-t1-0029}
**Teorema — Regla del cociente.** Sean $A\subseteq\mathbb R$, $a\in A$ un punto de acumulación y $f,g:A\to\mathbb R$ diferenciables en $a$ relativamente a $A$. Si $g(a)\ne0$, el cociente $q=f/g$, definido en $A_g=\{x\in A:g(x)\ne0\}$, es diferenciable en $a$ relativamente a $A_g$ y

$$
\boxed{q'_{A_g}(a)=
\frac{f'_A(a)g(a)-f(a)g'_A(a)}{g(a)^2}.}
$$

**Demostración.** La no anulación local prueba que $a$ es punto de acumulación de $A_g$ y que las restricciones de $f$ y $g$ conservan sus derivadas en $a$. Por @prp-t1-0039, $r=1/g$ es diferenciable en $a$ sobre $A_g$ y

$$
r'_{A_g}(a)=-\frac{g'_A(a)}{g(a)^2}.
$$

Como $q=(f|_{A_g})r$, el teorema del producto (@thm-t1-0028) proporciona tanto la existencia de $q'_{A_g}(a)$ como la igualdad

$$
\begin{aligned}
q'_{A_g}(a)
&=f'_A(a)\frac1{g(a)}
  +f(a)\left(-\frac{g'_A(a)}{g(a)^2}\right)\\
&=\frac{f'_A(a)g(a)-f(a)g'_A(a)}{g(a)^2}.
\end{aligned}
$$

Solo se ha utilizado la regla del producto **después** de disponer de la derivada del recíproco, de manera que no hay circularidad. $\square$
:::

Una forma útil de reconstruir la fórmula es partir de la identidad exacta

$$
\frac{f(a+h)}{g(a+h)}-\frac{f(a)}{g(a)}
=\frac{g(a)\bigl(f(a+h)-f(a)\bigr)
-f(a)\bigl(g(a+h)-g(a)\bigr)}{g(a+h)g(a)}.
$$

La identidad, válida para incrementos admisibles suficientemente pequeños, explica el **signo menos** del numerador y muestra por qué el denominador final es $g(a)^2$. Al dividir por $h$ y aplicar los mismos límites que antes se obtiene directamente el teorema; esta lectura sirve para controlar la fórmula sin memorizarla. No hemos supuesto que $g'_A(a)$ sea distinto de cero: esa condición no interviene en absoluto.

### Una simplificación algebraica no rellena un hueco del dominio

::: {#exm-t1-0076}
**Un cociente con discontinuidad removible.** Consideremos

$$
q(x)=\frac{x^2-1}{x-1},
\qquad A_q=\mathbb R\setminus\{1\}.
$$

Si $x\in A_q$, la factorización $x^2-1=(x-1)(x+1)$ permite cancelar el factor $x-1$ y concluir que $q(x)=x+1$. De ello se sigue que $q'(a)=1$ para **todo $a\in A_q$**, ya que cerca de cada uno de esos puntos el cociente coincide con una función afín.

La regla recién probada lo verifica también: para $a\ne1$,

$$
\begin{aligned}
q'(a)
&=\frac{2a(a-1)-(a^2-1)}{(a-1)^2}\\
&=\frac{(a-1)^2}{(a-1)^2}=1.
\end{aligned}
$$

En $a=1$ la función **no está definida**; no tiene valor ni derivada allí. La función distinta $\widetilde q:\mathbb R\to\mathbb R$, $\widetilde q(x)=x+1$, es una extensión continua de $q$ y sí tiene $\widetilde q'(1)=1$. Debemos distinguir las propiedades de la extensión de las de la función original: simplificar una expresión no cambia retroactivamente el dominio especificado.
:::

### Condiciones suficientes, extremos y errores de interpretación

La fórmula del cociente no dice que «se deriva arriba y abajo». Por ejemplo, $f(x)=x^2$ y $g(x)=x$ determinan el cociente $q(x)=x$ en $\mathbb R\setminus\{0\}$. En $a=2$, su derivada es $q'(2)=1$, mientras que $f'(2)/g'(2)=4$. La expresión $f'/g'$ no es la regla del cociente, ni siquiera cuando $g'(a)\ne0$.

Si $a$ es un extremo de $A$, por ejemplo $A=[0,\infty)$ y $a=0$, todas las pruebas anteriores funcionan con los incrementos admisibles de ese dominio, siempre que $g(0)\ne0$. No afirman una derivada bilateral para prolongaciones no especificadas.

Finalmente, nuestras hipótesis son **suficientes**, no necesarias para que un cociente particular sea diferenciable. En $\mathbb R$, las funciones $f(x)=g(x)=1+|x|$ no son diferenciables en $0$; sin embargo, como $g(x)>0$ en todo punto, $f/g=1$ sí lo es. Esto no invalida el teorema: sencillamente impide invertir su implicación.

::: {.callout-important title="Control antes de aplicar la regla del cociente"}
Comprueba por orden: (1) el dominio efectivo $A_g$; (2) que el punto pertenece a él y es de acumulación; (3) diferenciabilidad de ambos factores en el dominio pertinente; (4) $g(a)\ne0$; (5) los valores y las derivadas en el **mismo punto**. No añadas puntos excluidos mediante cancelaciones ni dividas por $g'(a)$.
:::

La regla del cociente ha quedado deducida a partir de resultados anteriores. En §7.5 utilizaremos la regla del producto, junto con la linealidad, para **demostrar por inducción** la derivada de las potencias naturales y, después, la fórmula de los polinomios. Las potencias enteras negativas y las funciones racionales se desarrollarán en §7.6, una vez construidas esas herramientas.

## Potencias naturales y derivación de polinomios {#sec-t1-c08-05}

### Una fórmula conocida todavía necesita una prueba

Las reglas establecidas hasta aquí permiten derivar sumas y productos de funciones diferenciables. Podemos, por ejemplo, obtener la derivada de $x^2=x\cdot x$ mediante la regla del producto, pero **no** hemos demostrado todavía una fórmula para una potencia de exponente arbitrario. Escribir de inmediato $(x^n)'=nx^{n-1}$ y utilizar esa misma fórmula para justificarla sería un argumento circular.

El paso decisivo es reconocer una construcción finita: para cada entero $n\ge1$, la función $x\mapsto x^{n+1}$ es el producto de $x\mapsto x^n$ y la función identidad. Esto permite utilizar una inducción, con una hipótesis inductiva que incluye **la existencia de la derivada**, y no solamente una igualdad formal de expresiones.

### Del producto a todas las potencias naturales positivas

::: {#prp-t1-0040}
**Proposición — Derivada de una potencia natural.** Para cada entero $n\ge1$, la función $p_n:\mathbb R\to\mathbb R$ definida por $p_n(x)=x^n$ es diferenciable en todo $a\in\mathbb R$ y satisface

$$
\boxed{p_n'(a)=na^{n-1}.}
$$

Aquí, cuando $n=1$, la expresión $a^0$ designa el valor de la **función constante** $x\mapsto1$, también en $a=0$.

**Demostración por inducción sobre $n$.** Sea $P(n)$ la afirmación completa «$p_n$ es diferenciable en cada punto real y $p_n'(a)=na^{n-1}$ para todo $a\in\mathbb R$».

**Caso inicial, $n=1$.** La función $p_1(x)=x$ es la identidad. Para cualquier $a\in\mathbb R$ y $h\ne0$,

$$
\frac{p_1(a+h)-p_1(a)}h
=\frac{(a+h)-a}{h}=1.
$$

El límite existe y vale $1=1\cdot a^0$, según la convención recién explicitada. Por tanto, $P(1)$ es verdadera.

**Paso inductivo.** Supongamos verdadera $P(n)$ para cierto $n\ge1$. Para cada $x\in\mathbb R$ tenemos la identidad de funciones

$$
p_{n+1}(x)=p_n(x)\,p_1(x)=x^n x.
$$

Ambos factores son diferenciables en cualquier $a$: el primero por hipótesis inductiva y el segundo por el caso inicial. La regla del producto, demostrada en @thm-t1-0028, prueba **también la existencia** de la derivada de $p_{n+1}$ y proporciona

$$
\begin{aligned}
p_{n+1}'(a)
&=p_n'(a)p_1(a)+p_n(a)p_1'(a)\\
&=na^{n-1}a+a^n\\
&=(n+1)a^n.
\end{aligned}
$$

La igualdad algebraica $a^{n-1}a=a^n$ vale igualmente para $a=0$ con $n\ge1$ y $a^0$ interpretado como la función constante $1$. Queda probada $P(n+1)$. El principio de inducción concluye la afirmación para todos los enteros $n\ge1$. $\square$
:::

**Lectura de la prueba.** El paso inductivo no deriva una potencia mediante una regla que aún desconocemos: deriva un **producto** utilizando @thm-t1-0028. De ese teorema obtenemos simultáneamente la existencia de la derivada y su valor. La inducción construye una familia de resultados, uno para cada exponente natural positivo; no es una autorización para sustituir $n$ por un exponente real cualquiera.

Podemos comprobar el primer paso sin acudir a la fórmula general: $D(x^2)=D(x\cdot x)=1\cdot x+x\cdot1=2x$. A continuación, $D(x^3)=D(x^2\cdot x)=2x\cdot x+x^2\cdot1=3x^2$. Son aplicaciones particulares de una demostración que ya cubre **todos** los enteros positivos, no evidencias aisladas que debamos extrapolar.

### El exponente cero: una función constante, no una potencia problemática

Para construir polinomios necesitamos también el término constante. Lo definimos sin recurrir a una expresión indeterminada: la función $p_0:\mathbb R\to\mathbb R$ es $p_0(x)=1$ para **todo** $x\in\mathbb R$. Su cociente incremental es

$$
\frac{p_0(a+h)-p_0(a)}h=\frac{1-1}{h}=0,
\qquad h\ne0,
$$

por lo que $p_0'(a)=0$ en todo punto. Esta definición funcional permite escribir convencionalmente $x^0=1$ dentro de un polinomio incluso en $x=0$; **no estamos evaluando una expresión $0^0$ cuyo significado no se haya fijado**. La fórmula $na^{n-1}$ se ha demostrado para $n\ge1$; no se obtiene el caso $n=0$ sustituyendo mecánicamente $n=0$ en ella.

Si restringimos $p_n$ o $p_0$ a un conjunto $A\subseteq\mathbb R$, sus derivadas relativas en cualquier $a\in A$ que sea punto de acumulación de $A$ coinciden con las derivadas recién demostradas: el límite relativo utiliza solamente algunos de los incrementos para los que ya existe el límite sobre $\mathbb R$. Esto incluye extremos de dominio y conjuntos no intervalares, siempre que exista acumulación.

### Un polinomio es una suma *finita* de monomios

::: {#cor-t1-0014}
**Corolario — Derivada de un polinomio.** Sean $m\in\mathbb N\cup\{0\}$ y $c_0,\ldots,c_m\in\mathbb R$. La función polinómica

$$
p:\mathbb R\to\mathbb R,
\qquad p(x)=\sum_{k=0}^{m}c_kx^k,
$$

con $x^0$ entendido como la función constante $1$, es diferenciable en todo punto real y

$$
\boxed{p'(a)=\sum_{k=1}^{m}k c_ka^{k-1}.}
$$

Cuando $m=0$, la suma del miembro derecho es vacía y su valor es $0$.

**Demostración.** El término $c_0p_0$ es constante y tiene derivada nula. Para cada $1\le k\le m$, la proposición @prp-t1-0040 demuestra que $p_k(x)=x^k$ es diferenciable en todo punto y que $p_k'(a)=ka^{k-1}$. La regla de las combinaciones lineales finitas, establecida en §7.2 a partir de @thm-t1-0027, asegura que la suma $p=\sum_{k=0}^m c_kp_k$ es diferenciable y que su derivada es la suma de las derivadas:

$$
\begin{aligned}
p'(a)
&=c_0p_0'(a)+\sum_{k=1}^m c_kp_k'(a)\\
&=0+\sum_{k=1}^m kc_ka^{k-1}.
\end{aligned}
$$

Si $m=0$, solo interviene la función constante y el mismo razonamiento da $p'(a)=0$. La conclusión vale para cada $a\in\mathbb R$. $\square$
:::

**El orden deductivo importa.** Una función polinómica no se declara diferenciable por tener una expresión algebraica familiar: hemos probado la diferenciabilidad de cada monomio y después la de su suma finita. Tampoco se ha intercambiado derivación con una **serie infinita**. El número de sumandos $m+1$ es finito, una condición esencial para aplicar sin hipótesis adicionales el resultado de §7.2.

Si dos fórmulas algebraicas expresan la misma función polinómica, el cálculo no puede producir derivadas diferentes: en cada punto donde existe, la derivada es el límite único del cociente incremental de esa función. Por eso expandir y reunir términos semejantes puede modificar la presentación de una expresión sin modificar su derivada. La simplificación, sin embargo, no autoriza a cambiar el dominio de una función racional; ese problema ya fue examinado en §7.4.

### Una verificación por dos caminos

::: {#exm-t1-0077}
**Un polinomio de quinto grado.** Sea

$$
p(x)=2x^5-3x^3+4x-7,
\qquad x\in\mathbb R.
$$

El dominio es todo $\mathbb R$. La proposición para potencias y la linealidad finita dan, en cualquier $a\in\mathbb R$,

$$
\begin{aligned}
p'(a)
&=2(5a^4)-3(3a^2)+4(1)-0\\
&=\boxed{10a^4-9a^2+4}.
\end{aligned}
$$

En particular, $p'(0)=4$ y $p'(1)=5$. **Control independiente en $a=0$.** Para $h\ne0$,

$$
\frac{p(h)-p(0)}h
=\frac{2h^5-3h^3+4h}{h}
=2h^4-3h^2+4\longrightarrow4.
$$

**Segundo control, en $a=1$.** La expansión puramente algebraica, previa al límite, proporciona

$$
\frac{p(1+h)-p(1)}h
=5+11h+17h^2+10h^3+2h^4
\longrightarrow5.
$$

Los dos cocientes confirman valores particulares de la fórmula general sin utilizarla durante sus verificaciones. La prueba de diferenciabilidad para todo $a$, en cambio, ya está garantizada por el corolario y no depende de revisar unos cuantos puntos.
:::

### Qué hemos demostrado y qué queda fuera

Las igualdades de esta sección pueden reunirse en una identidad de funciones sobre $\mathbb R$: si $p(x)=\sum_{k=0}^m c_kx^k$, entonces $Dp(x)=\sum_{k=1}^m kc_kx^{k-1}$. La igualdad representa el conjunto de afirmaciones puntuales que acabamos de probar; $D$ no es aquí una regla adicional.

Para una función diferenciable arbitraria $f$, la regla de productos finitos de §7.3 permite deducir también $(f^n)'=nf^{n-1}f'$ en el dominio pertinente. No la utilizaremos como premisa de la proposición sobre $x^n$: allí la inducción se apoyó únicamente en resultados anteriores. Su relación con la composición se retomará después, al demostrar la regla de la cadena. Tampoco hemos tratado $x^{-n}$ para exponentes negativos, $x^{1/2}$ o $x^\alpha$ con exponente real: sus dominios e hipótesis requieren un examen específico. Los exponentes enteros negativos y las funciones racionales serán el asunto inmediato de §7.6; las potencias con otros exponentes corresponden a desarrollos posteriores.

::: {.callout-note title="Reconstruir la deducción antes de continuar"}
Explica por qué el caso inicial de la inducción debe demostrar *existencia* y *valor* de la derivada. En el paso $x^{n+1}=x^nx$, indica qué resultado permite afirmar que el nuevo producto es diferenciable. Después, localiza el único lugar de la prueba del corolario donde se utiliza que un polinomio tiene un número **finito** de términos. Finalmente, explica por qué $x^0$ se trata como función constante y por qué el corolario no autoriza aún la derivación de $x^{-3}$ en $0$.
:::

La transición a §7.6 exige ahora responder dos preguntas distintas: ¿qué cambia cuando una potencia necesita dividir por $x$, y qué dominio debemos conservar cuando una función es el cociente de dos polinomios?

## Potencias enteras negativas y funciones racionales {#sec-t1-c08-06}

### El exponente negativo no elimina una división

En §7.5 demostramos la derivada de $x^n$ para cada entero $n\ge1$, y tratamos $x^0$ como la función constante $1$. Al pasar a exponentes negativos aparece una diferencia que no podemos ocultar bajo la semejanza de las fórmulas: para $n\ge1$, la escritura $x^{-n}$ significa el **recíproco** de $x^n$. Antes de derivar, hay que decidir dónde existe ese recíproco.

Para cualquier entero $n\ge1$, definimos

$$
 u_{-n}:\mathbb R\setminus\{0\}\longrightarrow\mathbb R,
 \qquad u_{-n}(x)=x^{-n}=\frac1{x^n}.
$$

En un cuerpo, $x^n\ne0$ si $x\ne0$: es un producto finito de factores no nulos. En cambio, para $x=0$ el denominador vale cero. Así, **el dominio es $\mathbb R\setminus\{0\}$**, aunque una manipulación posterior produzca una expresión aparentemente más simple. Todo punto de ese dominio es de acumulación; además, en torno a cada $a\ne0$ podemos escoger un intervalo que no contenga el origen, por ejemplo $|x-a|<|a|/2$.

La semejanza entre exponentes positivos y negativos debe, por tanto, construirse con una prueba; no se obtiene sustituyendo un entero negativo en una proposición demostrada solo para $n\ge1$.

### Del recíproco a las potencias negativas

El resultado de §7.4 ya contiene la herramienta necesaria. Si tomamos $g(x)=x^n$, sabemos por @prp-t1-0040 que $g$ es diferenciable en todo punto real y que $g'(a)=na^{n-1}$. Para $a\ne0$ también sabemos que $g(a)=a^n\ne0$. En consecuencia, la proposición del recíproco (@prp-t1-0039) es aplicable **en ese punto**.

No necesitamos inventar una nueva regla ni recurrir a la regla de la cadena, que todavía no hemos probado. La derivada se obtiene como

$$
\begin{aligned}
 u_{-n}'(a)
 &=-\frac{g'(a)}{g(a)^2}\\
 &=-\frac{na^{n-1}}{a^{2n}}\\
 &=-n\,a^{-n-1},\qquad a\ne0.
\end{aligned}
$$

La última igualdad utiliza únicamente las leyes de exponentes enteros **para una base no nula**. En $a=0$ no hay fórmula que aplicar: $u_{-n}(0)$ no existe, de modo que tampoco existe una derivada de esa función en el origen. La regla de exponentes negativos es una conclusión válida en su dominio, no una autorización para añadir el punto excluido.

### De los polinomios a sus cocientes

Una función racional se construye escogiendo dos polinomios reales $p$ y $q$, con $q$ no idénticamente nulo, y definiendo la función sobre el conjunto

$$
 D_{p,q}=\{x\in\mathbb R:q(x)\ne0\},
 \qquad r:D_{p,q}\to\mathbb R,
 \qquad r(x)=\frac{p(x)}{q(x)}.
$$

El conjunto $D_{p,q}$ se determina con el **denominador de la expresión que define la función**; una factorización posterior puede facilitar los cálculos, pero no modifica por sí sola ese dominio. Ambos polinomios son diferenciables en toda la recta, por @cor-t1-0014, y por tanto son continuos. Si $a\in D_{p,q}$, la continuidad de $q$ y $q(a)\ne0$ proporcionan un entorno de $a$ donde $q$ no se anula. Ese entorno está contenido en $D_{p,q}$: en particular, $a$ es punto de acumulación de su dominio natural.

Estamos exactamente en las hipótesis de la regla del cociente de §7.4. Podemos reunir las dos consecuencias en un enunciado que mantiene visibles sus dominios.

::: {#cor-t1-0015}
**Corolario — Potencias enteras negativas y funciones racionales.** Se cumplen las siguientes afirmaciones.

1. Para cada entero $n\ge1$, la función $u_{-n}(x)=x^{-n}$ definida en $\mathbb R\setminus\{0\}$ es diferenciable en todo punto $a\ne0$ y

   $$
   \boxed{u_{-n}'(a)=-n a^{-n-1}.}
   $$

2. Si $p,q:\mathbb R\to\mathbb R$ son polinomios y $q$ no es el polinomio nulo, la función $r=p/q$, definida sobre $D_{p,q}=\{x:q(x)\ne0\}$, es diferenciable en cada $a\in D_{p,q}$ y

   $$
   \boxed{r'(a)=\frac{p'(a)q(a)-p(a)q'(a)}{q(a)^2}.}
   $$

En la segunda fórmula, $p'$ y $q'$ son los polinomios derivados obtenidos por @cor-t1-0014.

**Demostración.** Para la primera afirmación, sea $n\ge1$ y sea $a\ne0$. La proposición @prp-t1-0040 da la derivabilidad de $g(x)=x^n$ y $g'(a)=na^{n-1}$. Como $g(a)=a^n\ne0$, @prp-t1-0039 demuestra la existencia de la derivada de $1/g$ en $a$ sobre su dominio natural y proporciona

$$
 u_{-n}'(a)=-\frac{na^{n-1}}{a^{2n}}=-na^{-n-1}.
$$

Para la segunda, fijemos $a\in D_{p,q}$. Ambos polinomios son diferenciables en $a$ por @cor-t1-0014 y $q(a)\ne0$ por la definición del dominio. La no anulación local establecida en §7.4 asegura que $a$ es de acumulación de $D_{p,q}$. Aplicar @thm-t1-0029 a $p$ y $q$ demuestra simultáneamente la diferenciabilidad de $r$ sobre ese dominio y la fórmula indicada. Como $a$ era arbitrario, la conclusión vale en cada punto de $D_{p,q}$. $\square$
:::

**Auditoría de dependencias.** La primera parte se apoya en potencias naturales y recíproco; la segunda, en polinomios y cociente. La regla de la cadena no aparece en ninguna prueba. La hipótesis $q\not\equiv0$ permite hablar de un cociente racional no vacío en el sentido habitual; la derivada solo se afirma en puntos donde $q(a)\ne0$. No se requiere que $q'(a)$ sea no nulo.

### Dos cálculos y dos controles independientes

::: {#exm-t1-0078}
**Una potencia negativa y un cociente con puntos excluidos.** Comencemos con

$$
 u(x)=x^{-3}=\frac1{x^3},
 \qquad \operatorname{Dom}(u)=\mathbb R\setminus\{0\}.
$$

El primer apartado del corolario, con $n=3$, da

$$
 \boxed{u'(x)=-3x^{-4}=-\frac3{x^4},\qquad x\ne0.}
$$

Así, $u'(-2)=-3/16$. Como control **independiente** del cálculo en $a=1$, usemos directamente el cociente incremental. Para $h\ne0$ suficientemente pequeño y $1+h\ne0$,

$$
\begin{aligned}
 \frac{u(1+h)-u(1)}h
 &=\frac{(1+h)^{-3}-1}{h}\\
 &=\frac{1-(1+h)^3}{h(1+h)^3}\\
 &=-\frac{3+3h+h^2}{(1+h)^3}
 \longrightarrow-3.
\end{aligned}
$$

Hemos cancelado $h$ solo para $h\ne0$ y comprobado por separado que el denominador restante tiende a $1$, no a cero. El límite reproduce $u'(1)=-3$ sin invocar la fórmula que pretendemos controlar.

Consideremos ahora

$$
 r(x)=\frac{x^2+1}{x^2-4}.
$$

La ecuación $x^2-4=(x-2)(x+2)=0$ excluye exactamente dos puntos. Por tanto,

$$
 \operatorname{Dom}(r)=\mathbb R\setminus\{-2,2\}.
$$

Los polinomios $p(x)=x^2+1$ y $q(x)=x^2-4$ cumplen $p'(x)=2x$ y $q'(x)=2x$. Para todo $x$ del dominio, la segunda parte del corolario da

$$
\begin{aligned}
 r'(x)
 &=\frac{2x(x^2-4)-(x^2+1)2x}{(x^2-4)^2}\\
 &=\boxed{-\frac{10x}{(x^2-4)^2}},
 \qquad x\ne-2,2.
\end{aligned}
$$

En particular, $r'(1)=-10/9$. También podemos comprobarlo directamente, puesto que $r(1)=-2/3$. Para $h\ne0$ suficientemente pequeño,

$$
\begin{aligned}
 \frac{r(1+h)-r(1)}h
 &=\frac{1}{h}\left(\frac{2+2h+h^2}{-3+2h+h^2}+\frac23\right)\\
 &=\frac{10+5h}{3(-3+2h+h^2)}
 \longrightarrow-\frac{10}{9}.
\end{aligned}
$$

El control directo confirma la derivada en $1$. En $-2$ y $2$ la función original no está definida; ninguna de las fórmulas permite atribuirle allí un valor ni una derivada.
:::

### Simplificar una expresión y respetar la función son tareas distintas

El cálculo racional exige distinguir dos operaciones. Una **identidad algebraica** puede permitir cancelar factores cuando son no nulos; una **extensión de dominio**, en cambio, exige definir explícitamente una función nueva. En §7.4 ya analizamos $\frac{x^2-1}{x-1}$: coincide con $x+1$ solo en su dominio original, que excluye $1$. Su derivada en ese punto sigue sin estar definida aunque la expresión simplificada admita una extensión diferenciable.

También es incorrecto deducir de la fórmula del cociente que el denominador derivado deba satisfacer $q'(a)\ne0$. El requisito es $q(a)\ne0$. Por ejemplo, en el cociente de nuestro ejemplo, $q'(0)=0$ y $q(0)=-4\ne0$; la regla es plenamente aplicable en $0$ y produce $r'(0)=0$.

Si se restringen $p$ y $q$ a un conjunto $A\subseteq\mathbb R$, el cociente restringido se define en $A\cap D_{p,q}$. Para hablar de su derivada relativa en $a$ es necesario que $a$ pertenezca a este conjunto y sea punto de acumulación de $A$. La condición $q(a)\ne0$ garantiza entonces que $A$ y $A\cap D_{p,q}$ coinciden suficientemente cerca de $a$, de modo que la fórmula del corolario sigue siendo válida como derivada relativa. **En un punto aislado de $A$ no se define derivada relativa**, aunque el polinomio original tenga derivada bilateral en toda la recta.

### La frontera exacta de la regla de potencias

Con §7.5 y esta sección hemos demostrado $(x^m)'=mx^{m-1}$ para enteros positivos $m$ sobre $\mathbb R$, para $m=0$ mediante la función constante, y para enteros negativos sobre $\mathbb R\setminus\{0\}$. Esto no demuestra la fórmula para exponentes fraccionarios o reales. Por ejemplo, antes de escribir una derivada para $\sqrt{x}$ necesitamos fijar su dominio y justificar su diferenciabilidad en los puntos pertinentes; no basta sustituir formalmente $m=1/2$ en un teorema de exponentes enteros.

::: {.callout-note title="Control de lectura: primero dominio, después fórmula"}
Explica qué resultado garantiza $x^n\ne0$ cuando $x\ne0$; identifica en qué paso se usa la proposición del recíproco y por qué no interviene todavía la cadena. En el ejemplo racional, determina dónde se comprueba $q(a)\ne0$ y por qué $q'(0)=0$ no causa ningún problema. Por último, distingue la afirmación «una expresión simplificada tiene derivada en $a$» de «la función original tiene derivada en $a$».
:::

La derivación de potencias enteras y racionales queda así reducida a resultados ya probados. En §7.7 estudiaremos una operación diferente: **componer funciones**. Allí el incremento de la función interior puede valer cero aunque el incremento de la variable independiente no lo sea; una demostración de la regla de la cadena deberá funcionar también en ese caso, sin dividir por una diferencia posiblemente nula.

## La regla de la cadena: cuando el incremento interior puede anularse {#sec-t1-c08-07}

### Dos cambios de escala, una sola derivada

La suma, el producto y el cociente combinan valores de funciones calculados en una misma entrada. La composición hace algo diferente: la salida de una función se convierte en la entrada de otra. Sean $f:A\to B\subseteq\mathbb R$ y $g:B\to\mathbb R$. Para estudiar $g\circ f$ en un punto $a\in A$ debemos seguir el recorrido

$$
a\longmapsto b=f(a)\longmapsto g(b).
$$

Si desplazamos $a$ hasta $a+h$, el incremento de la función interior es

$$
\Delta f=f(a+h)-f(a).
$$

La función exterior recibe **ese** incremento, no necesariamente $h$. El problema consiste en relacionar la variación de $g$ entre $b$ y $b+\Delta f$ con la variación de $f$ entre $a$ y $a+h$.

La aproximación afín del capítulo 6 sugiere el resultado: una variación pequeña $h$ produce, a primer orden, una variación $f'_A(a)h$; la función exterior transforma esta última, a primer orden, en $g'_B(b)f'_A(a)h$. Deberíamos obtener una derivada igual al producto de esas pendientes, con la exterior evaluada en **$b=f(a)$**. Esta interpretación orienta la prueba, pero no la reemplaza.

### La división tentadora y el punto donde falla

Partamos del cociente incremental de la composición. Una manipulación habitual intenta escribir

$$
\frac{g(f(a+h))-g(f(a))}{h}
\stackrel{?}{=}
\frac{g(f(a+h))-g(f(a))}{f(a+h)-f(a)}
\frac{f(a+h)-f(a)}{h}.
$$

Cuando $f(a+h)\ne f(a)$ y $h\ne0$, esta identidad es correcta. **La diferenciabilidad de $f$ no garantiza, sin embargo, que $f(a+h)\ne f(a)$ para todo incremento pequeño no nulo.** Una función puede repetir el valor central en una sucesión de puntos próximos, o incluso en todo un lado del punto. Entonces el primer factor carece de sentido: presenta denominador cero y numerador cero. Tampoco basta afirmar que su límite existe, porque la expresión propuesta no está definida para esos incrementos.

La reparación adecuada consiste en dar un valor justificado al cociente exterior *cuando su entrada es exactamente el punto central*. Esto se puede hacer antes de estudiar cualquier composición.

### Un cociente exterior que también tiene valor en el centro

::: {#lem-t1-0002}
**Lema — Extensión continua del cociente incremental exterior.** Sean $B\subseteq\mathbb R$, $b\in B$ un punto de acumulación y $g:B\to\mathbb R$ diferenciable en $b$ relativamente a $B$. Definamos $K:B\to\mathbb R$ mediante

$$
K(t)=
\begin{cases}
\dfrac{g(t)-g(b)}{t-b},&t\in B,\ t\ne b,\\[6pt]
g'_B(b),&t=b.
\end{cases}
$$

Entonces $K$ es continua en $b$ relativamente a $B$, y para **todo** $t\in B$ se cumple la identidad

$$
\boxed{g(t)-g(b)=K(t)(t-b).}
$$

**Demostración.** La definición de la derivada de $g$ afirma que

$$
\lim_{\substack{t\to b\\t\in B\setminus\{b\}}}
\frac{g(t)-g(b)}{t-b}=g'_B(b).
$$

Para $t\ne b$, $K(t)$ coincide con el cociente que aparece en este límite; por definición, $K(b)=g'_B(b)$. Dado $\varepsilon>0$, la existencia del límite proporciona $\delta>0$ tal que, si $t\in B$ y $0<|t-b|<\delta$, entonces $|K(t)-K(b)|<\varepsilon$. Si $t=b$, la misma desigualdad vale porque $|K(b)-K(b)|=0$. Se ha probado, también en el centro, la condición de continuidad relativa de $K$ en $b$.

Para $t\ne b$, multiplicar la primera rama de su definición por $t-b$ recupera exactamente $g(t)-g(b)$. Para $t=b$, ambos miembros de la identidad valen cero. La igualdad es, por tanto, válida en todo $B$, sin excepción. $\square$
:::

La extensión no consiste en asignar arbitrariamente un número a una fracción $0/0$. La derivada previamente existente determina el **único valor que hace continua a $K$ en $b$**: si otro valor produjera continuidad, el límite del cociente sobre $B\setminus\{b\}$ tendría que coincidir también con él, en contradicción con la unicidad del límite. Es importante distinguir el cociente original, definido solo fuera del centro, de la nueva función $K$, definida allí también.

### La regla general y su demostración

::: {#thm-t1-0030}
**Teorema — Regla de la cadena.** Sean $A,B\subseteq\mathbb R$, $f:A\to B$ y $g:B\to\mathbb R$. Supongamos que $a\in A$ es punto de acumulación de $A$ y que $b=f(a)\in B$ es punto de acumulación de $B$. Si $f$ es diferenciable en $a$ relativamente a $A$ y $g$ es diferenciable en $b$ relativamente a $B$, entonces $g\circ f:A\to\mathbb R$ es diferenciable en $a$ y satisface

$$
\boxed{(g\circ f)'_A(a)=g'_B(f(a))\,f'_A(a).}
$$

**Demostración.** Sea $K:B\to\mathbb R$ la función construida en @lem-t1-0002 para $g$ y $b=f(a)$. Su identidad fundamental, aplicada al valor $t=f(a+h)\in B$, da

$$
g(f(a+h))-g(f(a))
=K(f(a+h))\bigl(f(a+h)-f(a)\bigr)
$$

para **todo** incremento $h$ admisible, incluso cuando $f(a+h)=f(a)$. Definamos $H_a=\{h\in\mathbb R:a+h\in A\}$. Solo dividimos por $h$ cuando $h\in H_a\setminus\{0\}$; así obtenemos la identidad exacta

$$
\frac{(g\circ f)(a+h)-(g\circ f)(a)}h
=K(f(a+h))\,
\frac{f(a+h)-f(a)}h.
$$

Verifiquemos separadamente los dos límites del segundo miembro. Por la diferenciabilidad de $f$,

$$
\frac{f(a+h)-f(a)}h\longrightarrow f'_A(a).
$$

Además, diferenciabilidad implica continuidad (@thm-t1-0024), de modo que $f(a+h)\to f(a)=b$ a través de $A$. El lema establece que $K$ es continua en $b$ **incluido su valor central**. La composición de funciones continuas, ya demostrada en el capítulo 5, permite concluir que

$$
K(f(a+h))\longrightarrow K(b)=g'_B(b).
$$

Aquí no se exige que $f(a+h)\ne b$: cuando se produce la igualdad, $K(f(a+h))=K(b)$ está perfectamente definido. Aplicando el teorema del límite de un producto a los dos factores obtenemos

$$
\lim_{\substack{h\to0\\h\in H_a\setminus\{0\}}}
\frac{(g\circ f)(a+h)-(g\circ f)(a)}h
=g'_B(b)f'_A(a)\in\mathbb R.
$$

El cociente incremental de la composición posee, por tanto, un límite real finito. Esta es justamente la existencia de su derivada relativa en $a$, y su valor es el anunciado. $\square$
:::

**Lectura de la demostración en sentido inverso.** La conclusión exige demostrar que converge el cociente incremental de $g\circ f$. Para aplicar el álgebra de límites necesitábamos factorizarlo. La identidad del lema suministra esa factorización sin dividir por $\Delta f$. Para controlar el primer factor utilizamos continuidad de $K$ y de $f$; para el segundo, la definición de $f'_A(a)$. La derivada exterior aparece evaluada en $f(a)$ porque ese es el punto alrededor del cual cambia su argumento; evaluarla en $a$ sería, en general, incorrecto o incluso carecería de sentido si $a\notin B$.

La prueba es puntual y respeta dominios arbitrarios, incluidos extremos. No presupone que $f$ sea inyectiva, estrictamente monótona ni localmente distinta de su valor central. Las hipótesis son suficientes; no se ha demostrado su necesidad para toda composición particular.

### Un polinomio compuesto: verificar por dos rutas

::: {#exm-t1-0079}
**La potencia cuarta de un polinomio cuadrático.** Definamos $f:\mathbb R\to\mathbb R$ y $g:\mathbb R\to\mathbb R$ por

$$
f(x)=3x^2-1,\qquad g(t)=t^4.
$$

Ambas funciones son diferenciables en toda la recta por §7.5. Su composición es $u(x)=(3x^2-1)^4$. En un punto arbitrario $a$, tenemos $f'(a)=6a$, $f(a)=3a^2-1$ y $g'(f(a))=4(3a^2-1)^3$. La regla de la cadena demuestra la existencia de $u'(a)$ y da

$$
\boxed{u'(a)=24a(3a^2-1)^3.}
$$

En particular, $u'(1)=24\cdot 2^3=192$. Para controlar el resultado sin usar la cadena, expandamos algebraicamente **antes** de derivar:

$$
u(x)=81x^8-108x^6+54x^4-12x^2+1.
$$

El corolario polinómico @cor-t1-0014, demostrado antes de la regla de la cadena, produce

$$
u'(x)=648x^7-648x^5+216x^3-24x.
$$

Esta expresión coincide con $24x(3x^2-1)^3$ por expansión ordinaria; en $x=1$ también da $648-648+216-24=192$. Son dos rutas lícitas que conducen a la misma derivada. La primera muestra la estructura de composición; la segunda sirve como verificación independiente y utiliza únicamente una regla anterior.
:::

### Un caso en el que dividir por el incremento interior destruye la prueba

::: {#exm-t1-0080}
**Una función interior que repite su valor central en todo un semieje.** Consideremos

$$
f:\mathbb R\to[0,\infty),\qquad
f(x)=\begin{cases}0,&x\le0,\\x^2,&x>0,\end{cases}
\qquad
g:[0,\infty)\to\mathbb R,\quad g(t)=t^2+1.
$$

El punto de estudio es $a=0$ y su imagen es $b=f(0)=0$. Ambos son puntos de acumulación de los respectivos dominios. Para $h<0$ tenemos $f(h)-f(0)=0$, aunque $h\ne0$; por ello la división tentadora por el incremento interior no está definida en **ninguno** de esos incrementos.

Calculemos las derivadas necesarias desde la definición. Para $h\ne0$,

$$
\frac{f(h)-f(0)}h=
\begin{cases}0,&h<0,\\h,&h>0,\end{cases}
\longrightarrow0.
$$

Por tanto, $f'_{\mathbb R}(0)=0$. Para $t>0$, los incrementos admisibles de $g$ en el extremo $b=0$ son positivos y

$$
\frac{g(t)-g(0)}t=\frac{t^2}{t}=t\longrightarrow0.
$$

Así, $g'_{[0,\infty)}(0)=0$. El teorema recién demostrado proporciona $(g\circ f)'_{\mathbb R}(0)=0\cdot0=0$ sin división ilegítima.

Comprobémoslo directamente. La composición es

$$
(g\circ f)(x)=
\begin{cases}1,&x\le0,\\1+x^4,&x>0.\end{cases}
$$

Su cociente incremental en $0$ vale $0$ cuando $h<0$ y $h^3$ cuando $h>0$; ambos tienden a cero. En este ejemplo la función $K$ del lema es $K(t)=t$ para $t>0$ y $K(0)=0$. La identidad $g(t)-g(0)=K(t)t$ es válida aun en $t=0$ y permite factorizar el cociente de la composición para **todos** los $h\ne0$. Precisamente ahí reside la reparación de la demostración.
:::

### Qué hipótesis debemos conservar al reutilizarla

La notación compacta $(g\circ f)'(a)=g'(f(a))f'(a)$ omite información indispensable si se escribe fuera de un contexto fijado. Antes de utilizarla, hay que identificar un dominio $A$ donde $f$ esté definida, un conjunto $B$ que contenga **toda** la imagen pertinente de $f$, y el dominio de $g$. Debemos comprobar además que $a$ y $f(a)$ sean puntos de acumulación de los dominios respectivos y que las dos derivadas indicadas existan como límites reales finitos. Una función exterior definida solo en un punto aislado no tiene derivada allí bajo nuestra convención, aunque alguna composición específica resulte diferenciable.

En un extremo de $A$, la derivada de la composición es relativa a los incrementos disponibles. Si $f(a)$ es un extremo de $B$, también puede utilizarse una derivada exterior unilateral relativa a $B$. El teorema no atribuye derivadas bilaterales a extensiones que no se hayan definido. En cambio, puede ocurrir que $f(A)$ acumule o no en $f(a)$: la prueba no exige una derivada exterior relativa a la imagen efectiva si ya disponemos de $g'_B(f(a))$ en un dominio $B$ apropiado.

::: {.callout-important title="La regla de la cadena no es una regla de cancelación"}
La fórmula final multiplica dos derivadas, pero no se obtiene cancelando formalmente símbolos $df$. Su demostración utiliza una identidad válida en todos los incrementos admisibles y dos límites justificados. En particular, no exige $f'_A(a)\ne0$ ni que $f(a+h)-f(a)$ sea no nulo.
:::

### Reconstrucción de la prueba

Intenta demostrar el teorema partiendo solo de su conclusión: ¿qué cociente incremental debe converger?, ¿cuál es la división que no está permitida en general?, ¿cómo se define $K$ en el punto omitido y qué propiedad justifica ese valor?, ¿qué teorema garantiza $f(a+h)\to f(a)$?, ¿en qué punto se evalúa finalmente $g'$? Repite después la prueba sobre el ejemplo por tramos, donde todos los incrementos negativos anulan la variación interior. Si la demostración sigue siendo válida, has identificado el mecanismo esencial.

En §7.8 aplicaremos esta regla a composiciones sucesivas. El nuevo problema ya no será justificar una división, sino **conservar correctamente cada punto intermedio de evaluación** cuando la cadena tenga más de dos eslabones.

## Composiciones repetidas sin perder los puntos de evaluación {#sec-t1-c08-08}

### Una cadena tiene más de un punto de referencia

La regla demostrada en §7.7 deriva una composición de dos funciones. Ante una expresión con tres, cuatro o más operaciones anidadas, el peligro ya no es solamente omitir un factor: es **evaluar una derivada en la entrada equivocada**. Una composición transporta el punto inicial a través de varias funciones; cada derivada corresponde al punto al que llega la etapa anterior.

Supongamos, por ejemplo, que tenemos funciones correctamente encadenadas

$$
A_0\xrightarrow{\ f_1\ }A_1
\xrightarrow{\ f_2\ }A_2
\xrightarrow{\ f_3\ }A_3,
$$

y fijemos $x_0=a\in A_0$. Los puntos que intervienen son

$$
x_1=f_1(x_0),\qquad
x_2=f_2(x_1),\qquad
x_3=f_3(x_2).
$$

La derivada de $f_1$ se evalúa en $x_0$; la de $f_2$, en $x_1$; y la de $f_3$, en $x_2$. Escribir $f'_3(a)f'_2(a)f'_1(a)$ no está justificado: incluso podría ser una expresión indefinida si $a$ no pertenece a $A_1$ o a $A_2$.

Para tres eslabones, la regla de §7.7, aplicada primero a $f_2\circ f_1$ y después a $f_3\circ(f_2\circ f_1)$, sugiere

$$
\bigl(f_3\circ f_2\circ f_1\bigr)'_{A_0}(a)
=f'_{3,A_2}(x_2)\,f'_{2,A_1}(x_1)\,f'_{1,A_0}(x_0).
$$

La fórmula es una consecuencia de dos aplicaciones sucesivas, no una nueva regla admitida por analogía. Para extenderla a cualquier cantidad **finita** de eslabones, debemos controlar tanto las derivadas como los dominios durante una inducción.

### Teorema para una cantidad finita de composiciones

::: {#prp-t1-0041}
**Proposición — Regla de la cadena finita.** Sea $n\ge1$ un entero, sean $A_0,\ldots,A_n\subseteq\mathbb R$ y, para $1\le k\le n$, sean funciones

$$
f_k:A_{k-1}\longrightarrow A_k.
$$

Fijemos $x_0=a\in A_0$ y definamos sucesivamente

$$
x_k=f_k(x_{k-1}),\qquad 1\le k\le n.
$$

Supongamos que, para cada $1\le k\le n$, el punto $x_{k-1}$ es de acumulación de $A_{k-1}$ y $f_k$ es diferenciable en $x_{k-1}$ relativamente a ese conjunto. Entonces la composición

$$
F=f_n\circ f_{n-1}\circ\cdots\circ f_1:A_0\longrightarrow A_n
$$

es diferenciable en $a$ relativamente a $A_0$ y satisface

$$
\boxed{F'_{A_0}(a)=\prod_{k=1}^{n}f'_{k,A_{k-1}}(x_{k-1}).}
$$

**Demostración por inducción.** Llamemos $F_m=f_m\circ\cdots\circ f_1:A_0\to A_m$ para $1\le m\le n$. Demostraremos simultáneamente que $F_m$ es diferenciable en $a$ y que

$$
F'_{m,A_0}(a)=\prod_{k=1}^{m}f'_{k,A_{k-1}}(x_{k-1}).
$$

Para $m=1$, $F_1=f_1$; la existencia de su derivada es una hipótesis, y el producto de un único factor es $f'_{1,A_0}(a)$. Supongamos establecida la afirmación para un $m<n$. Por la definición de los puntos intermedios,

$$
F_m(a)=f_m(\cdots f_1(a)\cdots)=x_m.
$$

La hipótesis inductiva garantiza que $F_m:A_0\to A_m$ es diferenciable en $a$. La hipótesis correspondiente a $k=m+1$ garantiza que $x_m$ es punto de acumulación de $A_m$ y que $f_{m+1}:A_m\to A_{m+1}$ es diferenciable allí. Por tanto, **se cumplen las dos hipótesis de diferenciabilidad y las dos de acumulación** del teorema de la cadena @thm-t1-0030. Aplicándolo a $F_{m+1}=f_{m+1}\circ F_m$, obtenemos la existencia de $F'_{m+1,A_0}(a)$ y

$$
\begin{aligned}
F'_{m+1,A_0}(a)
&=f'_{m+1,A_m}\bigl(F_m(a)\bigr)\,F'_{m,A_0}(a)\\
&=f'_{m+1,A_m}(x_m)
\prod_{k=1}^{m}f'_{k,A_{k-1}}(x_{k-1})\\
&=\prod_{k=1}^{m+1}f'_{k,A_{k-1}}(x_{k-1}).
\end{aligned}
$$

Esto cierra el paso inductivo. La afirmación se sigue para $m=n$. En ningún paso hemos dividido por una derivada ni por un incremento interior: utilizamos exclusivamente la regla de §7.7, ya demostrada para incrementos interiores posiblemente nulos. $\square$
:::

**Lectura de las hipótesis.** La acumulación se exige en $x_0,\ldots,x_{n-1}$, pues en esos puntos se calculan las derivadas de $f_1,\ldots,f_n$, respectivamente. No se necesita exigir que el valor final $x_n$ sea punto de acumulación de $A_n$: **no estamos derivando ninguna función adicional en $x_n$**. Tampoco exigimos que cada $f_k$ sea diferenciable en todos los puntos de su dominio; bastan los puntos de evaluación indicados. La propiedad es puntual, aun cuando la función compuesta se haya definido sobre todo $A_0$.

La prueba tiene una frontera precisa: demuestra una regla para $n$ **finito**. No autoriza a derivar una composición infinita ni a tomar un producto infinito de pendientes. Esos procesos requerirían nuevas nociones y controles de convergencia.

### Laboratorio de cuatro eslabones: desarmar antes de derivar

Consideremos

$$
H(x)=\bigl(2(3x-2)^2+1\bigr)^3,
\qquad x\in\mathbb R.
$$

En lugar de interpretar la expresión como un bloque indivisible, definamos cuatro funciones, cada una con dominio y codominio $\mathbb R$:

$$
\begin{aligned}
f_1(t)&=3t-2,\\
f_2(t)&=t^2,\\
f_3(t)&=2t+1,\\
f_4(t)&=t^3.
\end{aligned}
$$

Todas son polinómicas y, por @cor-t1-0014, diferenciables en toda la recta. La composición tipada es

$$
H=f_4\circ f_3\circ f_2\circ f_1.
$$

Fijemos un punto arbitrario $a$. El **árbol de dependencias** —en este caso, una cadena lineal de entradas y salidas— conserva los cuatro valores diferentes:

$$
\begin{aligned}
x_0&=a,\\
x_1&=3a-2,\\
x_2&=(3a-2)^2,\\
x_3&=2(3a-2)^2+1,\\
x_4&=\bigl(2(3a-2)^2+1\bigr)^3.
\end{aligned}
$$

La tabla de evaluación de las derivadas se reconstruye sin adivinar:

| Eslabón | Derivada de la función | Evaluación correcta |
|---|---|---|
| $f_1$ | $f'_1(t)=3$ | $f'_1(x_0)=3$ |
| $f_2$ | $f'_2(t)=2t$ | $f'_2(x_1)=2(3a-2)$ |
| $f_3$ | $f'_3(t)=2$ | $f'_3(x_2)=2$ |
| $f_4$ | $f'_4(t)=3t^2$ | $f'_4(x_3)=3\bigl(2(3a-2)^2+1\bigr)^2$ |

Como se satisfacen todas las hipótesis de @prp-t1-0041, podemos multiplicar los cuatro valores. El resultado es

$$
\begin{aligned}
H'(a)
&=f'_4(x_3)f'_3(x_2)f'_2(x_1)f'_1(x_0)\\
&=3\bigl(2(3a-2)^2+1\bigr)^2
\cdot2\cdot2(3a-2)\cdot3\\
&=\boxed{36(3a-2)\bigl(2(3a-2)^2+1\bigr)^2}.
\end{aligned}
$$

En $a=1$, los puntos intermedios son $x_1=1$, $x_2=1$ y $x_3=3$, de donde $H'(1)=3\cdot2\cdot2\cdot3\cdot3^2=324$. **Control independiente:** el polinomio interior completo es $u(x)=18x^2-24x+9$. Como $H=u\cdot u\cdot u$, la fórmula para productos finitos de §7.3 —demostrada *antes* de la regla de la cadena— y el corolario polinómico permiten obtener

$$
H'(x)=3u(x)^2u'(x)
=3(18x^2-24x+9)^2(36x-24),
$$

que coincide con la expresión anterior porque $u(x)=2(3x-2)^2+1$ y $36x-24=12(3x-2)$. Este control usa el producto de tres funciones y la derivada de un polinomio, **no** la regla para composiciones que estamos comprobando.

### Dos errores que parecen inofensivos

**Evaluar todas las derivadas en $a$.** Tomemos simplemente $f(x)=3x-2$, $g(t)=t^2$ y $a=2$. Como $f(2)=4$, la cadena da $(g\circ f)'(2)=g'(4)f'(2)=8\cdot3=24$. El producto incorrecto $g'(2)f'(2)=4\cdot3=12$ evalúa la derivada exterior en otro punto. Las funciones son diferenciables en toda $\mathbb R$: el fallo no está en las hipótesis, sino en el argumento utilizado.

**Olvidar que un factor puede ser cero.** Si, en alguna composición finita que satisfaga la proposición, $f'_j(x_{j-1})=0$, el producto de las derivadas vale cero. La regla sigue siendo válida: no hemos cancelado factores ni supuesto pendientes distintas de cero. Sin embargo, la igualdad $F'(a)=0$ por sí sola no permite deducir qué factor se anula si desconocemos que todas las derivadas individuales existen; y aun conociéndolas, no permite afirmar que las funciones sean localmente constantes. La regla describe únicamente el comportamiento de primer orden.

### Identidad funcional y dominios restringidos

Si las hipótesis de la proposición se verifican en todos los puntos de un conjunto $E\subseteq A_0$ que sean de acumulación de $A_0$, podemos reunir las fórmulas puntuales en una igualdad de funciones derivadas *sobre $E$*. Para cada $a\in E$, los puntos $x_k$ deben recalcularse mediante las funciones de la cadena. No existe una lista fija de puntos intermedios independiente de $a$.

En dominios como $A_0=[0,\infty)$, la conclusión en el extremo $a=0$ se refiere a los incrementos admisibles de $A_0$. Las derivadas intermedias se toman relativamente a **sus propios dominios** $A_{k-1}$, que pueden ser distintos unos de otros. No se ha afirmado la existencia de derivadas bilaterales para extensiones arbitrarias ni se requiere que la imagen efectiva de cada composición parcial acumule en su valor si el codominio intermedio elegido ya satisface la hipótesis pertinente.

::: {.callout-note title="Rehacer la cadena sin memorizar una fórmula larga"}
Reconstruye la derivada de $H(x)=\bigl(2(3x-2)^2+1\bigr)^3$ partiendo del punto $a$, no de la expresión final: escribe $x_0,\ldots,x_4$; asigna a cada función la entrada en la que se evalúa su derivada; comprueba por qué no necesitamos que $x_4$ sea de acumulación de un conjunto adicional. Después indica exactamente qué cambia en el paso inductivo al pasar de $m$ a $m+1$ eslabones.
:::

La regla de la cadena finita ya está demostrada. En §7.9 examinaremos el alcance lógico de las reglas: **que una composición sea diferenciable no implica, en general, que cada función empleada satisfaga todas las hipótesis suficientes de la regla**. Allí distinguiremos una conclusión verdadera de una aplicación injustificada del teorema.

## Lo que las reglas no afirman {#sec-t1-c08-09}

### Un teorema condicional no es una equivalencia

Hemos demostrado reglas que permiten construir derivadas a partir de otras derivadas previamente conocidas. Su forma lógica es siempre condicional. Por ejemplo, la regla de la cadena afirma que, bajo las hipótesis de dominio, acumulación y diferenciabilidad de @thm-t1-0030, **la composición es diferenciable** y su derivada tiene una expresión determinada. No afirma que esas hipótesis sean necesarias para que *alguna* composición resulte diferenciable.

Conviene separar tres preguntas: ¿la función está definida en el punto?, ¿se han verificado las hipótesis de una regla que garantiza su diferenciabilidad?, ¿podría demostrarse su diferenciabilidad por otra vía aunque esas hipótesis fallen? Una respuesta negativa a la segunda no decide la tercera. Una respuesta negativa a la primera, en cambio, impide atribuir una derivada a la función original en ese punto.

Formalmente, de una implicación $P\Rightarrow Q$ y de la verdad de $Q$ no se deduce $P$. Para refutar la conversa basta encontrar un caso en el que $Q$ sea verdadera y $P$ falsa. El siguiente ejemplo se ocupa de la regla de la cadena, donde esta distinción resulta especialmente instructiva.

### Una composición diferenciable con una función exterior no diferenciable

::: {#exm-t1-0081}
**El valor absoluto queda oculto al componerlo con un cuadrado.** Consideremos las funciones completas

$$
f:\mathbb R\longrightarrow\mathbb R,
\qquad f(x)=x^2,
$$

$$
g:\mathbb R\longrightarrow\mathbb R,
\qquad g(t)=|t|,
$$

y fijemos $a=0$, de modo que $b=f(a)=0$. La función interior es diferenciable en $0$: su cociente incremental es $h^2/h=h$ para $h\ne0$, luego $f'(0)=0$.

La función exterior **no** es diferenciable en $b=0$ relativamente a su dominio declarado $\mathbb R$. En efecto, para $t\ne0$,

$$
\frac{g(t)-g(0)}{t}
=\frac{|t|}{t}
=\begin{cases}-1,&t<0,\\1,&t>0.\end{cases}
$$

Los límites laterales son distintos, por lo que $g'_{\mathbb R}(0)$ no existe. Sin embargo, para todo $x\in\mathbb R$ tenemos $x^2\ge0$ y, por tanto,

$$
(g\circ f)(x)=|x^2|=x^2.
$$

Desde la definición, el cociente incremental de la composición en $0$ es $h$ y converge a $0$. Así,

$$
\boxed{(g\circ f)'_{\mathbb R}(0)=0,
\qquad g'_{\mathbb R}(f(0))\ \text{no existe}.}
$$

La conclusión «la composición es diferenciable» es verdadera, pero **no podemos justificarla aplicando @thm-t1-0030 a estas dos funciones completas**, pues falta una de sus hipótesis. Escribir $g'_{\mathbb R}(0)f'_{\mathbb R}(0)=0$ sería ilegítimo: un factor indefinido no adquiere valor por multiplicarlo formalmente por cero.
:::

**Un matiz importante sobre los dominios.** En este ejemplo, la imagen de $f$ está contenida en $B=[0,\infty)$. Si declaramos explícitamente una función exterior distinta, a saber, la restricción $\widetilde g=g|_B:B\to\mathbb R$, entonces $\widetilde g(t)=t$ para $t\ge0$. Su derivada **relativa a $B$** existe en $0$ y vale $1$, porque los incrementos admisibles allí son positivos. La regla de la cadena sí puede aplicarse a la composición tipada $\widetilde g\circ f$ y da

$$
(\widetilde g\circ f)'_{\mathbb R}(0)
=\widetilde g'_B(0)f'_{\mathbb R}(0)=1\cdot0=0.
$$

No hay contradicción: $g'_{\mathbb R}(0)$ y $\widetilde g'_B(0)$ son afirmaciones sobre **dominios diferentes**. Restringir la función exterior puede proporcionar una nueva demostración, pero no convierte retroactivamente en verdadera la hipótesis que fallaba para $g:\mathbb R\to\mathbb R$. El ejemplo refuta la conversa formulada para las funciones completas originales.

La diferenciabilidad de la composición tampoco obliga a que la **función interior** sea diferenciable. Para comprobarlo sin introducir nuevas reglas, tomemos $u:\mathbb R\to[0,\infty)$, $u(x)=|x|$, y $v:[0,\infty)\to\mathbb R$, $v(t)=t^2$. La función $u$ no es diferenciable en $0$ por sus cocientes laterales $-1$ y $1$, pero $(v\circ u)(x)=|x|^2=x^2$ sí lo es. La diferenciabilidad de la composición no permite reconstruir por sí sola la diferenciabilidad de cada eslabón.

### Las operaciones algebraicas también pueden ocultar dificultades

La regla del producto @thm-t1-0028 garantiza la diferenciabilidad de $fg$ cuando ambos factores son diferenciables en el punto pertinente. Su conversa falla incluso si **ninguno** de los dos factores es diferenciable. Sean $f(x)=g(x)=|x|$ en $\mathbb R$. Sus cocientes incrementales en $0$ son $|h|/h$, con límites laterales distintos. Sin embargo,

$$
(fg)(x)=|x|^2=x^2,
\qquad (fg)'(0)=\lim_{h\to0}\frac{h^2}{h}=0.
$$

La regla del producto no era aplicable en $0$, aunque el producto resultante tenga derivada. Esta constatación complementa el ejemplo de §7.3, donde bastaba que uno de los factores fuese la función nula.

Tampoco podemos invertir la regla del cociente @thm-t1-0029. Definamos $f(x)=g(x)=1+|x|$ para todo $x\in\mathbb R$. Ninguno de los dos factores es diferenciable en $0$: para $h\ne0$ su cociente incremental vale $|h|/h$. No obstante, $g(x)\ge1$, de manera que el cociente está definido **en toda la recta**, incluida la entrada central, y satisface

$$
q(x)=\frac{1+|x|}{1+|x|}=1,
\qquad q'(0)=0.
$$

La falla de la conversa no depende aquí de dividir por cero ni de rellenar un agujero: el cociente original tiene dominio $\mathbb R$ y es diferenciable en $0$, pese a que sus dos componentes no lo sean. Lo que no está permitido es emplear la fórmula del teorema en ese punto, pues sus derivadas de partida no existen.

Estos ejemplos permiten un diagnóstico común. Que una operación produzca una función suave en determinado punto no obliga a que los objetos de partida sean individualmente suaves allí. La operación puede cancelar o transformar las dificultades; solo la definición o un teorema cuyas hipótesis se cumplan permite establecer la conclusión en cada caso.

### Una hipótesis que falla y una expresión que ni siquiera está definida

La ausencia de diferenciabilidad de un factor no equivale a la ausencia de definición de la función formada. En los ejemplos anteriores, los productos, cocientes y composiciones estaban definidos en $0$; por eso tenía sentido calcular sus derivadas directamente. Un denominador nulo en el centro plantea un problema diferente.

Tomemos $p(x)=x$ y $q(x)=x$ sobre $\mathbb R$. Su cociente natural es

$$
r:\mathbb R\setminus\{0\}\longrightarrow\mathbb R,
\qquad r(x)=\frac{x}{x}=1.
$$

La cancelación demuestra $r(x)=1$ **para $x\ne0$**, no que $r(0)$ exista. La función original no tiene derivada en $0$, pues $0$ no pertenece a su dominio. Podemos definir otra función $\widetilde r:\mathbb R\to\mathbb R$ por $\widetilde r(x)=1$ y obtener $\widetilde r'(0)=0$, pero ese resultado pertenece a la extensión, no al cociente original. La condición $q(a)\ne0$ de la regla no es un formalismo prescindible: en este caso delimita dónde existe la operación.

Existe otra pérdida posible de dominio. Si $f:A\to\mathbb R$ y $g:B\to\mathbb R$ son diferenciables en $a$ relativamente a sus respectivos dominios, su producto puntual o su suma se definen sobre $C=A\cap B$. Para utilizar una regla en $a$ es necesario que $a$ sea de acumulación de $C$, no solo de $A$ y de $B$ por separado. Retomemos el ejemplo de §7.2:

$$
A=\{0\}\cup\{1/n:n\ge1\},\qquad
B=\{0\}\cup\{-1/n:n\ge1\}.
$$

Las funciones nulas en cada uno de esos dominios son diferenciables relativamente a ellos en $0$, pero $A\cap B=\{0\}$. El producto y la suma, considerados **únicamente sobre esa intersección**, no tienen derivada relativa en $0$ conforme a nuestra definición, porque el punto ha quedado aislado. No es un contraejemplo a una regla correctamente enunciada: faltan las condiciones necesarias para formular su conclusión.

### Auditar una inferencia, no solamente una fórmula

Las comprobaciones anteriores se pueden ordenar según el tipo de obstáculo:

| Situación | Qué es legítimo concluir |
|---|---|
| Todas las hipótesis de la regla están verificadas. | La diferenciabilidad y la fórmula se siguen del teorema. |
| La función resultante está definida, pero falla una hipótesis suficiente. | El teorema no decide el caso; hay que buscar una demostración independiente o verificar una restricción apropiada. |
| La función resultante no está definida en el punto. | No tiene derivada allí; una extensión definida expresamente es otra función. |
| El dominio de una operación deja aislado el punto. | No hay derivada relativa bajo la definición adoptada en el capítulo 6. |

Esta distinción también impide una inferencia inversa frecuente: si una composición diferenciable tiene derivada nula, no cabe buscar automáticamente un factor nulo en la fórmula de la cadena **antes de haber verificado que dicha fórmula es aplicable**. Cuando todas sus hipótesis sí se cumplen, el producto de derivadas es legítimo y, si vale cero, al menos un factor es cero por la propiedad del producto nulo; aun así, una derivada puntual nula no demuestra que una función sea constante en ningún entorno. Las conclusiones globales sobre el comportamiento de una función requieren otros argumentos.

::: {.callout-note title="Tres preguntas para diagnosticar una aplicación injustificada"}
En el ejemplo $|x^2|$, explica por qué $g'_{\mathbb R}(0)$ no existe y $\widetilde g'_{[0,\infty)}(0)$ sí existe. Después, para $(1+|x|)/(1+|x|)$, distingue la derivada del cociente de las derivadas de sus factores. Finalmente, identifica la diferencia entre «la regla del cociente no puede aplicarse en $a$» y «el cociente no es una función definida en $a$». ¿Qué prueba o dato necesitarías en cada caso?
:::

Con estas distinciones, el repertorio de reglas queda cerrado en su alcance exacto: sabemos construir derivadas cuando disponemos de las hipótesis suficientes, reconocer situaciones que exigen volver a la definición y detectar cuándo la expresión ni siquiera define una función en el punto. La siguiente sección reunirá estos procedimientos en un laboratorio de reconstrucción, reparación y combinación; no introducirá reglas nuevas.

## Laboratorio: reconstruir, reparar y combinar {#sec-t1-c08-10}

### De la respuesta a la justificación

En §§7.2–7.8 demostramos las reglas de derivación y en §7.9 examinamos lo que sus conclusiones no permiten invertir. El propósito de este laboratorio no es aprender otras ocho fórmulas. Es practicar una secuencia de decisiones: **reconocer la función, localizar el punto y su dominio, elegir una identidad o un teorema, comprobar las hipótesis y justificar el límite**. Las ocho estaciones se resuelven aquí de manera guiada; los ejercicios autónomos y sus soluciones quedarán reunidos en §7.11.

En cada estación conviene intentar primero la consigna, detenerse en la dificultad indicada y cotejar después la reconstrucción. Todos los cálculos se apoyan exclusivamente en los resultados ya establecidos; no introduciremos definiciones, teoremas ni identificadores de ejemplos nuevos.

### Estación 1. Leer una expresión como una construcción de funciones

**Consigna.** Antes de derivar, identifica el dominio y las operaciones que forman

$$
R(x)=\frac{(x^2+1)(2x-1)^3}{x^2-1}.
$$

¿Qué regla corresponde a la operación exterior? ¿En qué orden necesitarías las otras reglas? ¿Tiene sentido solicitar $R'(1)$ después de simplificar alguna expresión?

**Reconstrucción.** El numerador es un *producto*: sus factores son $p(x)=x^2+1$ y $q(x)=(2x-1)^3$. El segundo factor es a su vez una *composición*: primero $u(x)=2x-1$ y después $v(t)=t^3$. El denominador es $d(x)=x^2-1$. Así, la operación exterior es un cociente de $pq$ entre $d$; no una composición de los tres términos. El dominio natural es

$$
A=\{x\in\mathbb R:x^2-1\ne0\}
=\mathbb R\setminus\{-1,1\}.
$$

Para calcular $R'_A(a)$ debemos escoger $a\in A$ —todos sus puntos son de acumulación—, derivar $p,d$ mediante las fórmulas polinómicas, $q$ mediante la regla de la cadena, $pq$ mediante el producto y, finalmente, aplicar el cociente. No necesitamos realizar el cálculo completo para establecer esa dependencia. La solicitud $R'(1)$ carece de sentido para **esta** función: $1\notin A$. Una eventual extensión definida en ese punto sería una función distinta y exigiría análisis propio.

**Control inverso.** La mera presencia de una potencia no autoriza comenzar por una supuesta «regla de potencia para todo»: debemos reconocer qué objeto está elevado a una potencia y cuáles son sus dominios. Tampoco se puede evaluar una derivada antes de decidir qué función está definida.

### Estación 2. Inventar el término intermedio del producto

**Consigna.** Reconstruye la regla del producto sin recordarla de memoria. Para $f,g:A\to\mathbb R$ diferenciables en un punto de acumulación $a\in A$, empieza por la única expresión que define la derivada de $fg$ y separa su numerador en dos variaciones aprovechables.

**Reconstrucción.** Para todo incremento admisible $h\ne0$, agregamos y sustraemos el mismo término $f(a+h)g(a)$:

$$
\begin{aligned}
&f(a+h)g(a+h)-f(a)g(a)\\
&\quad=f(a+h)\bigl(g(a+h)-g(a)\bigr)
       +g(a)\bigl(f(a+h)-f(a)\bigr).
\end{aligned}
$$

Dividimos **solo por $h\ne0$**:

$$
\frac{(fg)(a+h)-(fg)(a)}{h}
=f(a+h)\frac{g(a+h)-g(a)}h
 +g(a)\frac{f(a+h)-f(a)}h.
$$

La diferenciabilidad de $f$ implica $f(a+h)\to f(a)$; los dos cocientes convergen a sus derivadas. Por las leyes de los límites obtenemos

$$
(fg)'_A(a)=f'_A(a)g(a)+f(a)g'_A(a).
$$

Como comprobación concreta, toma $f(x)=x^2-1$, $g(x)=x+2$ y $a=1$. Aunque $f(1)=0$, la regla da $f'(1)g(1)+f(1)g'(1)=2\cdot3+0=6$. Desde la definición, con $h\ne0$,

$$
\frac{(fg)(1+h)-(fg)(1)}h
=\frac{(2h+h^2)(3+h)}h=(2+h)(3+h)\longrightarrow6.
$$

**Punto de reparación.** El término intermedio no se «deriva»: se suma y se resta para construir una identidad exacta. En ningún momento es necesario dividir por $f(a)$, que aquí es cero.

### Estación 3. Encontrar el lugar exacto de la continuidad

**Consigna.** En la identidad anterior, identifica qué paso sería ilegítimo si solo conociéramos el límite del cociente incremental de $g$. ¿De dónde proviene el límite del factor $f(a+h)$? Reconstruye además una descomposición simétrica.

**Reconstrucción.** Para afirmar que

$$
f(a+h)\frac{g(a+h)-g(a)}h
\longrightarrow f(a)g'_A(a)
$$

necesitamos **dos** límites. El del cociente procede de la diferenciabilidad de $g$; el del factor $f(a+h)$ procede de la diferenciabilidad de $f$ mediante «derivabilidad implica continuidad» (@thm-t1-0024). El otro sumando tiende a $g(a)f'_A(a)$ porque $g(a)$ es constante respecto de $h$. Esta identificación muestra que la continuidad no es una hipótesis suplementaria oculta: ya está garantizada por las hipótesis de la regla.

Podemos reconstruir la misma identidad usando otro término intermedio, ahora $f(a)g(a+h)$:

$$
\begin{aligned}
&f(a+h)g(a+h)-f(a)g(a)\\
&\quad=g(a+h)\bigl(f(a+h)-f(a)\bigr)
+f(a)\bigl(g(a+h)-g(a)\bigr).
\end{aligned}
$$

Aquí el factor cuyo límite requiere continuidad es $g(a+h)$, y la conclusión no cambia. Las dos rutas son válidas porque **ambas funciones** son diferenciables y, por ello, continuas en $a$. Si solo supiéramos que $g$ es diferenciable, no tendríamos derecho a declarar automáticamente que el producto es diferenciable: faltaría información sobre $f$.

**Lectura inversa.** Una vez escrita la fórmula de la derivada del producto, pregunta qué términos debían converger para obtener cada sumando. Esa pregunta conduce hacia atrás a la identidad algebraica y a la continuidad necesaria; evita convertir la regla en una consigna mnemotécnica.

### Estación 4. Probar que un denominador permanece separado de cero

**Consigna.** Sean $g:A\to\mathbb R$, $a\in A$ punto de acumulación, $g'_A(a)$ existente y $g(a)\ne0$. Demuestra que el cociente $f/g$ estará definido en todos los puntos de $A$ suficientemente cercanos a $a$, siempre que $f:A\to\mathbb R$ esté definida. No sustituyas esta prueba por «el denominador parece no anularse».

**Reconstrucción.** Por @thm-t1-0024, $g$ es continua en $a$ relativamente a $A$. Elegimos la tolerancia positiva $\varepsilon=|g(a)|/2$. Existe $\delta>0$ tal que, para $x\in A$ con $|x-a|<\delta$,

$$
|g(x)-g(a)|<\frac{|g(a)|}{2}.
$$

La desigualdad triangular inversa proporciona

$$
|g(x)|\ge |g(a)|-|g(x)-g(a)|
>\frac{|g(a)|}{2}>0.
$$

En consecuencia, $g(x)\ne0$ en ese entorno relativo y $a$ pertenece al dominio natural $A_g=\{x\in A:g(x)\ne0\}$; además, $A_g$ contiene todos los puntos de $A$ suficientemente cercanos a $a$. Los cocientes incrementales relativos a $A_g$ y a $A$ coinciden para incrementos suficientemente pequeños. Esta es la justificación local que permite usar el recíproco y el cociente.

**Variación diagnóstica.** Si $g(a)=0$, la tolerancia elegida deja de ser positiva y falla el argumento. No hemos demostrado que $f/g$ sea imposible en todo el dominio: hemos constatado que el cociente natural **no está definido en $a$**, de modo que carece de derivada allí. Ni una cancelación algebraica ni la existencia de $g'(a)$ restablecen por sí solas el valor ausente.

### Estación 5. Reparar la falsa derivación «arriba y abajo»

**Consigna.** Un razonamiento propone $\bigl(f/g\bigr)'=f'/g'$. Localiza el error con un caso en el que $g'$ no sea cero, y reconstruye la fórmula correcta sin utilizar previamente la regla del cociente.

**Diagnóstico.** En $A=\mathbb R\setminus\{0\}$ tomemos $f(x)=x^2$ y $g(x)=x$. La función cociente es $q(x)=x$ en $A$, y por ello $q'_A(1)=1$. En cambio, $f'(1)/g'(1)=2/1=2$. La fórmula propuesta falla aun cuando ambos miembros pretendidos están definidos. No existe una identidad que identifique el incremento del cociente con el cociente de los incrementos de sus componentes.

**Reconstrucción.** Para funciones diferenciables en un punto de acumulación $a$ de un dominio común, y con $g(a)\ne0$, la estación anterior da no anulación local. Comenzamos por el recíproco, cuya diferencia exacta es

$$
\frac{1}{g(a+h)}-\frac{1}{g(a)}
=-\frac{g(a+h)-g(a)}{g(a+h)g(a)}.
$$

Al dividir por $h\ne0$ y pasar al límite obtenemos

$$
\left(\frac1g\right)'(a)=-\frac{g'(a)}{g(a)^2}.
$$

Solo ahora aplicamos la regla del producto a $f(1/g)$ y simplificamos:

$$
\begin{aligned}
\left(\frac fg\right)'(a)
&=\frac{f'(a)}{g(a)}-
  \frac{f(a)g'(a)}{g(a)^2}\\
&=\boxed{\frac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}}.
\end{aligned}
$$

**Control de hipótesis.** La condición decisiva es $g(a)\ne0$, no $g'(a)\ne0$. Por ejemplo, $g(x)=1$ tiene derivada cero, pero $f/g=f$ está perfectamente definido y puede derivarse cuando $f$ lo sea. La expresión $f'/g'$ sería entonces una división por cero aunque el cociente original no presente dificultad alguna.

### Estación 6. Reparar la división imposible en la regla de la cadena

**Consigna.** Se intenta escribir

$$
\frac{g(f(a+h))-g(f(a))}{h}
=\frac{g(f(a+h))-g(f(a))}{f(a+h)-f(a)}
  \frac{f(a+h)-f(a)}{h}.
$$

¿Por qué la igualdad no es válida para todos los $h\ne0$ admisibles? Construye una identidad que sí lo sea y úsala con una función interior que conserve su valor en un semieje.

**Diagnóstico.** Puede ocurrir $f(a+h)=f(a)$ aunque $h\ne0$; la fracción exterior del miembro derecho queda entonces indefinida. Para evitarla, sea $b=f(a)$ y definamos sobre el dominio $B$ de la función exterior

$$
K(t)=
\begin{cases}
\dfrac{g(t)-g(b)}{t-b},&t\ne b,\\[4pt]
g'_B(b),&t=b.
\end{cases}
$$

Siempre que $b$ sea de acumulación de $B$ y $g$ sea diferenciable allí, $K(t)\to g'_B(b)$ relativamente a $B$ y $K$ es continua en $b$. Además, para **todo** $t\in B$, incluido $t=b$, se cumple $g(t)-g(b)=K(t)(t-b)$. En consecuencia, para todos los incrementos $h\ne0$ admisibles,

$$
\frac{g(f(a+h))-g(f(a))}h
=K(f(a+h))\frac{f(a+h)-f(a)}h.
$$

No aparece ningún incremento interior en un denominador. La continuidad de $f$ en $a$ y la de $K$ en $b$ dan el límite del primer factor; la diferenciabilidad de $f$ da el del segundo. Recuperamos @thm-t1-0030 sin excepción para los incrementos interiores nulos.

**Prueba de estrés.** Definamos $f:\mathbb R\to[0,\infty)$ por $f(x)=0$ si $x\le0$ y $f(x)=x^2$ si $x>0$; definamos $g:[0,\infty)\to\mathbb R$ por $g(t)=t^2+1$. En $a=0$, $f'_{\mathbb R}(0)=0$ porque su cociente es $0$ para $h<0$ y $h$ para $h>0$; $g'_{[0,\infty)}(0)=0$ porque su cociente exterior es $t$ para $t>0$. Aquí $K(t)=t$ para $t\ge0$. Para todo $h<0$ se cumple $f(h)-f(0)=0$, pero la identidad corregida sigue definida. Directamente, el cociente de la composición es $0$ para $h<0$ y $h^3$ para $h>0$: converge a $0$, como exige la regla.

### Estación 7. Auditar una composición triple y sus puntos de evaluación

**Consigna.** Considera las funciones tipadas

$$
\begin{aligned}
f&:[0,\infty)\longrightarrow[1,\infty),& f(x)&=x^2+1,\\
g&:[1,\infty)\longrightarrow[0,\infty),& g(t)&=(t-1)^2,\\
k&:[0,\infty)\longrightarrow\mathbb R,& k(s)&=\frac1{1+s}.
\end{aligned}
$$

Determina la derivada relativa de $H=k\circ g\circ f$ en $0$ y en $1$. Indica el punto de evaluación de **cada** derivada; no evalúes las tres automáticamente en la entrada original.

**Reconstrucción en el extremo.** En $a=0$ los puntos intermedios son $x_0=0$, $x_1=f(0)=1$ y $x_2=g(1)=0$. Son puntos de acumulación de sus dominios respectivos, y las derivadas relativas —obtenidas mediante las reglas ya demostradas, o desde sus cocientes en los extremos— son

$$
f'_{[0,\infty)}(0)=0,\qquad
g'_{[1,\infty)}(1)=0,\qquad
k'_{[0,\infty)}(0)=-1.
$$

La regla finita @prp-t1-0041 entrega

$$
H'_{[0,\infty)}(0)=k'(x_2)g'(x_1)f'(x_0)
=(-1)\cdot0\cdot0=0.
$$

No sería lícito escribir $g'(0)$: $0$ ni siquiera pertenece al dominio declarado de $g$. Tampoco hemos exigido que la salida final $H(0)=1$ sea punto de acumulación del codominio $\mathbb R$ para derivar una cuarta función inexistente.

**Reconstrucción en un punto interior.** En $a=1$, $x_0=1$, $x_1=2$ y $x_2=1$; por tanto,

$$
H'_{[0,\infty)}(1)=k'(1)g'(2)f'(1)
=-\frac14\cdot2\cdot2=\boxed{-1}.
$$

La expresión compuesta es $H(x)=1/(1+x^4)$ para $x\ge0$. Como verificación por cocientes, para $h\ne0$ suficientemente pequeño,

$$
\begin{aligned}
\frac{H(1+h)-H(1)}h
&=-\frac{(1+h)^4-1}{2h\bigl(1+(1+h)^4\bigr)}\\
&\longrightarrow-\frac4{2\cdot2}=-1.
\end{aligned}
$$

En $0$, el cociente directo es $-h^3/(1+h^4)\to0$ para $h>0$, en concordancia con el cálculo relativo. Se han comprobado tanto el orden de evaluación como la naturaleza unilateral del extremo, sin suponer derivadas de extensiones no declaradas.

### Estación 8. Reconocer dónde termina el capítulo

**Consigna.** Clasifica las siguientes peticiones: ¿pueden justificarse enteramente con las reglas de este capítulo o exigen un resultado que todavía no hemos demostrado?

| Petición | Diagnóstico y fundamento |
|---|---|
| Derivar $1/(1+x^2)$ sobre $\mathbb R$. | **Sí.** El denominador es positivo; la regla del recíproco y la derivada polinómica bastan. |
| Derivar $(x^2+1)^3$ sobre $\mathbb R$. | **Sí.** La función interior es polinómica y la exterior es la potencia cúbica; aplicar cadena con evaluación en $x^2+1$. |
| Deducir una fórmula general para la derivada de $f^{-1}$ a partir de $f'$. | **No todavía.** $f^{-1}$ denota una función inversa por composición, no el recíproco puntual $1/f$; la derivación de inversas pertenece al capítulo 8. |
| Derivar una relación $x^2+y^2=1$ tratando $y$ como función de $x$, sin fijar una rama ni probar su diferenciabilidad. | **No todavía.** Deben justificarse primero la existencia de una función pertinente y las hipótesis para derivarla; la derivación implícita pertenece al capítulo 8. |
| Concluir de $u'(a)>0$ que $u$ es creciente en todo un intervalo. | **No.** Una derivada positiva en un solo punto no autoriza tal conclusión. Los teoremas del valor medio y las aplicaciones globales de las derivadas se estudiarán en los capítulos 9 y 10. |

**Una frontera comprobable.** La función $u(x)=x-x^2$ satisface $u'(0)=1>0$ mediante las reglas polinómicas, pero no es creciente en toda $\mathbb R$: $u(1)=0>u(2)=-2$, mientras $1<2$. Incluso cuando una conclusión global resulta verdadera para una función particular, hace falta una prueba que corresponda a la amplitud de la conclusión. Del mismo modo, $v(x)=x^2$ tiene $v'(0)=0$ sin ser constante en ningún entorno de $0$. Las fórmulas puntuales no sustituyen a los teoremas globales.

### Mapa de decisión: de la expresión a una conclusión justificada

La ruta común a las ocho estaciones puede reconstruirse en el siguiente orden, sin tomar ninguna fórmula como licencia para ignorar sus hipótesis:

1. **Definir el objeto.** Identificar función completa, dominio de cada componente y dominio efectivo de la operación. Excluir los ceros de denominadores antes de simplificar.
2. **Fijar el punto.** Comprobar pertenencia y acumulación en el dominio pertinente; distinguir derivada bilateral y derivada relativa en un extremo.
3. **Desarmar la operación exterior.** Reconocer suma, producto, recíproco, cociente o composición; para composiciones, registrar los puntos intermedios y los dominios de cada eslabón.
4. **Auditar las hipótesis.** Verificar la diferenciabilidad de las funciones que exige la regla; para un cociente, demostrar no anulación local; para la cadena, disponer de la derivada exterior en el punto correcto.
5. **Justificar la transformación.** Si se reconstruye una prueba, escribir una identidad exacta de incrementos y señalar qué continuidad y qué límites se utilizan. No dividir por cantidades que puedan anularse.
6. **Obtener y controlar el resultado.** Aplicar la fórmula únicamente en los puntos habilitados; cuando sea conveniente, contrastarla mediante un cociente incremental o una expansión algebraica independiente.
7. **Distinguir el diagnóstico final.** Hipótesis suficientes incumplidas no equivale a no diferenciabilidad; falta de valor central sí impide derivar la función original; conclusiones sobre inversas, derivación implícita o comportamiento global exigen nuevas pruebas.

::: {.callout-note title="Comprobación de autonomía"}
Ante una composición con un cociente en su interior, ¿puedes señalar el dominio antes de derivar, nombrar los puntos de evaluación, identificar la única división peligrosa de la prueba de la cadena y sustituirla por una identidad válida? ¿Puedes además explicar por qué una regla que no se aplica no demuestra que la derivada buscada no exista? Si las respuestas contienen una hipótesis y un argumento, no solo una fórmula, has recuperado el método del capítulo.
:::

Hemos pasado de construir reglas aisladas a **elegir y justificar una ruta de derivación**. La sección siguiente reúne cuarenta ejercicios originales con sus cuarenta soluciones desarrolladas: allí estas decisiones se practicarán sin el andamiaje completo de las estaciones y se auditará cada correspondencia entre problema y solución antes del cierre del capítulo.

## Ejercicios y soluciones {#sec-t1-c08-11}

Las reglas de derivación han sido demostradas, pero emplearlas correctamente exige algo más que reconocer una fórmula: debemos definir la función, comprobar el dominio y los puntos de acumulación, identificar qué resultados están disponibles y distinguir las hipótesis suficientes de sus conversas. Este banco trabaja esas decisiones en orden creciente de autonomía. Antes de mirar cada solución, escribe la operación exterior y comprueba en qué puntos está autorizada la derivada.

Los cuarenta ejercicios están distribuidos en siete niveles, $7A+7B+7C+6D+5E+5F+3G=40$. Cada ejercicio tiene una solución homóloga desarrollada al final de la sección. Solo se utilizan resultados de los capítulos anteriores y de las §§7.1–7.10. Ni la regla de la función inversa ni la derivación implícita, los teoremas del valor medio, Taylor o las derivadas trascendentes forman parte del repertorio autorizado.

### Nivel A — Reconocimiento y comprensión

::: {#exr-t1-0276}
**Ejercicio A1. Linealidad no significa multiplicatividad.** Enuncia la regla para $D(\alpha f+\beta g)$ y explica por qué no permite concluir que $D(fg)=(Df)(Dg)$. Refuta esta última fórmula con $f(x)=g(x)=x$ en $a=1$, calculando ambos miembros.
:::

::: {#exr-t1-0277}
**Ejercicio A2. Datos puntuales y combinación lineal.** Sean $f,g:A\to\mathbb R$ diferenciables en un punto de acumulación $a\in A$, y supón que $f(a)=2$, $g(a)=-1$, $f'_A(a)=3$ y $g'_A(a)=4$. Calcula $(2f-3g)'_A(a)$ y explica qué datos se utilizan.
:::

::: {#exr-t1-0278}
**Ejercicio A3. Los valores centrales también intervienen.** Con las funciones y los cuatro datos del ejercicio A2, calcula $(fg)'_A(a)$. Identifica los sumandos procedentes de la variación de cada factor.
:::

::: {#exr-t1-0279}
**Ejercicio A4. La condición del cociente.** Sean $f,g:A\to\mathbb R$ diferenciables en $a$, punto de acumulación de $A$. ¿Qué hipótesis adicional garantiza que $f/g$ esté definido en un entorno relativo de $a$ y sea diferenciable **en $a$**? Explica por qué la condición pertinente no es $g'_A(a)\ne0$.
:::

::: {#exr-t1-0280}
**Ejercicio A5. Primero el dominio.** Determina el dominio natural de $r(x)=(x^2+1)/(x^2-4)$ y calcula $r'(x)$ en ese dominio. ¿Tiene sentido pedir la derivada de *esa función* en $2$?
:::

::: {#exr-t1-0281}
**Ejercicio A6. Reconstruir la derivada cúbica.** Demuestra que $D(x^3)=3x^2$ utilizando solamente $D(x)=1$ y la regla del producto; no cites como premisa la regla general para potencias.
:::

::: {#exr-t1-0282}
**Ejercicio A7. ¿Dónde se evalúa la derivada exterior?** Escribe $(3x+1)^4$ como $g\circ f$, indica los dominios y calcula la derivada en un punto arbitrario $a$. Explica por qué el argumento de $g'$ es $3a+1$ y no necesariamente $a$.
:::

### Nivel B — Aplicación directa

::: {#exr-t1-0283}
**Ejercicio B1. Un polinomio.** Deriva $p(x)=3x^5-2x^3+7x-4$ para todo $x\in\mathbb R$. Indica qué resultados justifican la derivación término a término.
:::

::: {#exr-t1-0284}
**Ejercicio B2. Un producto comprobado de dos modos.** Calcula la derivada de $p(x)=(x^2+1)(x^3-2x)$ aplicando la regla del producto; expande después $p$ y verifica independientemente la respuesta.
:::

::: {#exr-t1-0285}
**Ejercicio B3. Un cociente racional.** Declara el dominio natural de $r(x)=(x^2+1)/(x-2)$, deriva y simplifica el numerador resultante. ¿Es legítimo evaluar $r'(2)$?
:::

::: {#exr-t1-0286}
**Ejercicio B4. Una potencia negativa.** Deduce la derivada de $r(x)=x^{-4}$ utilizando el recíproco de $x^4$, con indicación del dominio. No supongas de antemano la fórmula para exponentes negativos.
:::

::: {#exr-t1-0287}
**Ejercicio B5. Una potencia compuesta.** Calcula $D((2x^2-1)^5)$ identificando función interior, exterior y puntos de evaluación de sus derivadas.
:::

::: {#exr-t1-0288}
**Ejercicio B6. Dos capas de composición.** Deriva $H(x)=((x^2+1)^3-2)^4$. Define los valores intermedios y muestra cómo se obtiene cada factor de la derivada.
:::

::: {#exr-t1-0289}
**Ejercicio B7. Derivar en un extremo.** Sea $A=[0,\infty)$ y sea $p:A\to\mathbb R$ dada por $p(x)=x^2(x+1)$. Calcula $p'_A(0)$ mediante la regla del producto relativa a $A$ y verifica el valor directamente con el cociente incremental derecho.
:::

### Nivel C — Combinación estructural

::: {#exr-t1-0290}
**Ejercicio C1. Linealidad finita.** Para $n\ge1$, supón que $f_1,\ldots,f_n:A\to\mathbb R$ son diferenciables en el mismo punto de acumulación $a\in A$ y $c_1,\ldots,c_n\in\mathbb R$. Demuestra por inducción que $\sum_{k=1}^n c_kf_k$ es diferenciable en $a$ y que su derivada es $\sum_{k=1}^n c_kf'_{k,A}(a)$.
:::

::: {#exr-t1-0291}
**Ejercicio C2. Producto de un número finito de factores.** Para $n\ge1$, demuestra por inducción que, si $f_1,\ldots,f_n:A\to\mathbb R$ son diferenciables en un punto de acumulación $a\in A$, entonces

$$
\left(\prod_{k=1}^n f_k\right)'_A(a)
=\sum_{j=1}^n f'_{j,A}(a)\prod_{\substack{1\le k\le n\\k\ne j}}f_k(a).
$$

Convén explícitamente que el producto vacío vale $1$. No dividas por ningún factor.
:::

::: {#exr-t1-0292}
**Ejercicio C3. La derivada de $x^{-1}$.** Demuestra sobre $\mathbb R\setminus\{0\}$ que $D(x^{-1})=-x^{-2}$ aplicando la proposición del recíproco a la función identidad. Explica por qué el resultado no atribuye derivada en $0$.
:::

::: {#exr-t1-0293}
**Ejercicio C4. Recíproco de una composición.** Determina el dominio y la derivada de

$$
R(x)=\frac{1}{1+(x^2+1)^3}.
$$

Justifica primero que el denominador no se anula en ningún real.
:::

::: {#exr-t1-0294}
**Ejercicio C5. Una composición con puntos excluidos.** Sean $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, y $g:\mathbb R\setminus\{1\}\to\mathbb R$, $g(t)=1/(t-1)$. Determina el dominio efectivo de $g\circ f$ y su derivada allí, sin reintegrar los puntos excluidos.
:::

::: {#exr-t1-0295}
**Ejercicio C6. Dos pruebas para un mismo cuadrado.** Deriva $H(x)=(x^2+1)^2$ de dos maneras: interpretándolo como producto de dos polinomios iguales e interpretándolo como composición $g\circ f$. Comprueba que ambos resultados coinciden para todo real.
:::

::: {#exr-t1-0296}
**Ejercicio C7. No anulación local cuantitativa.** Sean $g:A\to\mathbb R$ diferenciable en el punto de acumulación $a\in A$, con $g(a)\ne0$. Demuestra que existe $\delta>0$ tal que $g(a+h)\ne0$ si $a+h\in A$ y $|h|<\delta$. Obtén, de hecho, una cota inferior positiva para $|g(a+h)|$.
:::

### Nivel D — Inversión y diagnóstico

::: {#exr-t1-0297}
**Ejercicio D1. Una falsa multiplicación de pendientes.** Un estudiante escribe $(fg)'=f'g'$ y pretende demostrarlo multiplicando los dos cocientes incrementales. Localiza el error con $f=g=x$ en $a=1$; después reconstruye la identidad de incrementos que conduce a la fórmula correcta para funciones diferenciables en un dominio común.
:::

::: {#exr-t1-0298}
**Ejercicio D2. Derivar «arriba y abajo» no funciona.** Refuta $(f/g)'=f'/g'$ usando $f(x)=x^2$, $g(x)=x$ en $a=1$. Demuestra que todos los cocientes numéricos que comparas están definidos y escribe la fórmula correcta.
:::

::: {#exr-t1-0299}
**Ejercicio D3. Un incremento interior nulo.** Define $f:\mathbb R\to[0,\infty)$ por $f(x)=0$ si $x\le0$ y $f(x)=x^2$ si $x>0$; sea $g:[0,\infty)\to\mathbb R$, $g(t)=t^2+1$. Explica por qué no es válido dividir siempre por $f(h)-f(0)$ al derivar $g\circ f$ en $0$. Repara la demostración con la extensión continua del cociente de $g$ y comprueba la derivada directamente.
:::

::: {#exr-t1-0300}
**Ejercicio D4. Una conversa inexistente.** Refuta la afirmación «si $g\circ f$ es diferenciable en $a$, entonces $g$ lo es en $f(a)$» mediante $f(x)=x^2$, $g(t)=|t|$ declaradas sobre $\mathbb R$, con $a=0$. Distingue este caso de restringir $g$ explícitamente a $[0,\infty)$.
:::

::: {#exr-t1-0301}
**Ejercicio D5. Cancelar no crea un valor perdido.** Examina la afirmación «$r(x)=x^2/x$ tiene derivada en $0$ porque se simplifica a $x$». Especifica el dominio natural de $r$, determina dónde vale la simplificación y construye, si es posible, una extensión distinta que sí tenga derivada en $0$.
:::

::: {#exr-t1-0302}
**Ejercicio D6. La intersección puede aislar un punto.** Sean $A=\{0\}\cup\{1/n:n\ge1\}$ y $B=\{0\}\cup\{-1/n:n\ge1\}$. Define $f:A\to\mathbb R$ y $g:B\to\mathbb R$ como funciones constantemente nulas. Comprueba que ambas tienen derivada relativa en $0$. ¿Tiene derivada relativa en $0$ su suma definida sobre $A\cap B$? Justifica sin utilizar un límite vacuo.
:::

### Nivel E — Construcción de contraejemplos

::: {#exr-t1-0303}
**Ejercicio E1. Producto regular, factores irregulares.** Construye dos funciones no diferenciables en $0$ cuyo producto sí lo sea. Usa $f(x)=g(x)=|x|$ y verifica las tres afirmaciones con cocientes incrementales.
:::

::: {#exr-t1-0304}
**Ejercicio E2. El cociente puede ocultar dos esquinas.** Construye numerador y denominador no diferenciables en $0$ pero con denominador no nulo en toda la recta y cociente diferenciable. Utiliza $f(x)=g(x)=1+|x|$ y demuestra cada propiedad.
:::

::: {#exr-t1-0305}
**Ejercicio E3. Una función exterior no diferenciable.** Da un ejemplo de funciones completas $f,g:\mathbb R\to\mathbb R$ tal que $g\circ f$ tenga derivada en $0$ pero $g$ no la tenga en $f(0)$. Verifica con $f(x)=x^2$ y $g(t)=|t|$ y explica qué hipótesis de la regla de la cadena falla.
:::

::: {#exr-t1-0306}
**Ejercicio E4. Infinitos incrementos interiores nulos.** Define $f:\mathbb R\to[0,\infty)$ por $f(x)=0$ si $x\in\mathbb Q$ y $f(x)=x^2$ si $x\notin\mathbb Q$. Demuestra que $f'(0)=0$ pero $f$ no es constante en ningún entorno de $0$ y que $f(h)-f(0)=0$ para infinitos $h\ne0$ arbitrariamente cercanos a $0$. Con $g:[0,\infty)\to\mathbb R$, $g(t)=t^2+1$, verifica la regla de la cadena en $0$ sin dividir por ese incremento interior.
:::

::: {#exr-t1-0307}
**Ejercicio E5. Una función interior no diferenciable.** Da una composición diferenciable en $0$ cuya función interior no sea diferenciable. Usa $f(x)=|x|$ y una función exterior constante $g(t)=7$, declarando dominios y verificando la derivada de la composición.
:::

### Nivel F — Descubrimiento guiado

::: {#exr-t1-0308}
**Ejercicio F1. Inventar el término intermedio.** Para $f,g:A\to\mathbb R$ diferenciables en $a$, punto de acumulación, parte de $f(a+h)g(a+h)-f(a)g(a)$. Añade y sustrae un mismo término para separar el cambio de los factores. Divide por $h\ne0$, identifica todos los límites necesarios y demuestra la regla del producto sin citarla como premisa.
:::

::: {#exr-t1-0309}
**Ejercicio F2. Construir el recíproco.** Sean $g:A\to\mathbb R$ diferenciable en $a$, punto de acumulación, y $g(a)\ne0$. Obtén un entorno relativo donde $g$ no se anule, transforma exactamente $1/g(a+h)-1/g(a)$ y deduce la derivada del recíproco desde la definición. Indica en qué paso se requiere la continuidad.
:::

::: {#exr-t1-0310}
**Ejercicio F3. Inducir la regla de las potencias.** Usando la derivada de la identidad y la regla del producto, demuestra por inducción que $D(x^n)=nx^{n-1}$ para todo entero $n\ge1$. Trata por separado el exponente $0$ y especifica por qué esta demostración no cubre exponentes fraccionarios.
:::

::: {#exr-t1-0311}
**Ejercicio F4. Reparar la cadena en el centro.** Sean $f:A\to B\subseteq\mathbb R$ y $g:B\to\mathbb R$, con $a\in A$, $b=f(a)$, ambos puntos de acumulación de sus respectivos dominios y ambas derivadas relativas finitas. Define una función $K:B\to\mathbb R$ prolongando $(g(t)-g(b))/(t-b)$ en $t=b$; demuestra su continuidad en $b$ y deduce la regla de la cadena mediante una identidad válida incluso cuando $f(a+h)=b$.
:::

::: {#exr-t1-0312}
**Ejercicio F5. La composición desde residuos.** En las hipótesis del ejercicio F4, escribe $f(a+h)=b+Lh+r_f(h)$ y $g(b+t)=g(b)+Mt+t\eta(t)$ con $r_f(h)=o(h)$ y $\eta(t)\to0$, definiendo $\eta(0)=0$. Para $t=f(a+h)-b$, demuestra directamente que el último término de la segunda linealización es $o(h)$, incluso cuando $t=0$. Concluye la derivada de la composición sin citar la regla de la cadena.
:::

### Nivel G — Desafíos

::: {#exr-t1-0313}
**Ejercicio G1. Ceros en un producto finito.** Prueba por inducción la fórmula de la derivada de $P=\prod_{k=1}^n f_k$, para $n\ge2$ y factores diferenciables en $a$ sobre un dominio común. Demuestra que $P'(a)=0$ si al menos dos factores se anulan en $a$. ¿Qué fórmula queda si exactamente un factor, $f_j$, se anula allí? No dividas por ninguno.
:::

::: {#exr-t1-0314}
**Ejercicio G2. Un conjunto denso de incrementos nulos.** Construye una función $f:\mathbb R\to\mathbb R$ diferenciable en $0$, con $f'(0)=0$ e infinitos ceros no nulos arbitrariamente próximos a $0$, pero que no sea localmente constante. Usa $f(x)=0$ en los racionales y $f(x)=x^2$ en los irracionales. Para $g(t)=3t+1$ sobre $\mathbb R$, comprueba directamente $(g\circ f)'(0)=g'(f(0))f'(0)$ y explica por qué la habitual división por $f(h)-f(0)$ fracasa.
:::

::: {#exr-t1-0315}
**Ejercicio G3. El cociente desde las linealizaciones.** Sean $f,g:A\to\mathbb R$ diferenciables en un punto de acumulación $a$, con $g(a)\ne0$. Escribe sus aproximaciones de primer orden con residuos $o(h)$ y demuestra *directamente* que $f/g$ es diferenciable en $a$ y que

$$
\left(\frac fg\right)'_A(a)
=\frac{f'_A(a)g(a)-f(a)g'_A(a)}{g(a)^2}.
$$

No uses las reglas del recíproco ni del cociente; identifica el papel de la no anulación local y evita cualquier división por $f(a+h)-f(a)$ o $g(a+h)-g(a)$.
:::

### Soluciones desarrolladas

#### Soluciones del nivel A

::: {#sol-t1-0276}
**Solución A1.** Para funciones diferenciables en un punto de acumulación $a$ de un dominio común y escalares fijos, @thm-t1-0027 da

$$
(\alpha f+\beta g)'_A(a)=\alpha f'_A(a)+\beta g'_A(a).
$$

Esta es una propiedad de las *combinaciones lineales*, no de los productos. Si $f(x)=g(x)=x$ en $\mathbb R$, entonces $f'(1)=g'(1)=1$. Pero $(fg)(x)=x^2$ y, para $h\ne0$,

$$
\frac{(1+h)^2-1}{h}=2+h\longrightarrow2.
$$

Por tanto, $(fg)'(1)=2\ne1=f'(1)g'(1)$. La regla verdadera exige los valores de los factores: $(fg)'=f'g+fg'$ donde se cumplen sus hipótesis. El ejemplo refuta la multiplicatividad; no contradice la linealidad.
:::

::: {#sol-t1-0277}
**Solución A2.** Ambas funciones son diferenciables en $a$ relativamente al mismo dominio, de modo que podemos aplicar linealidad con coeficientes $2$ y $-3$:

$$
(2f-3g)'_A(a)=2f'_A(a)-3g'_A(a)
=2\cdot3-3\cdot4=\boxed{-6}.
$$

Los valores $f(a)=2$ y $g(a)=-1$ no intervienen: la derivada de una combinación lineal depende aquí solo de las derivadas y de los coeficientes constantes. No se está derivando un producto de funciones.
:::

::: {#sol-t1-0278}
**Solución A3.** La regla del producto @thm-t1-0028, aplicable por diferenciabilidad común, proporciona

$$
(fg)'_A(a)=f'_A(a)g(a)+f(a)g'_A(a)
=3(-1)+2(4)=\boxed{5}.
$$

El primer término $-3$ corresponde a la variación de $f$, ponderada por el valor central $g(a)$; el segundo, $8$, corresponde a la variación de $g$, ponderada por $f(a)$. Multiplicar solamente las pendientes daría $12$, que no es la respuesta.
:::

::: {#sol-t1-0279}
**Solución A4.** Se requiere $g(a)\ne0$. Como $g$ es diferenciable en $a$, es continua allí por @thm-t1-0024. Con $\varepsilon=|g(a)|/2>0$ encontramos $\delta>0$ tal que, para $x\in A$ y $|x-a|<\delta$,

$$
|g(x)|\ge|g(a)|-|g(x)-g(a)|>
\frac{|g(a)|}{2}>0.
$$

Así $a$ y un entorno relativo suyo pertenecen al dominio natural del cociente; las restricciones tienen las mismas derivadas puntuales por localidad y @thm-t1-0029 asegura la derivabilidad de $f/g$ en $a$. No se necesita $g'_A(a)\ne0$: si $g=1$, entonces $g'=0$ y $f/g=f$ sigue siendo derivable.
:::

::: {#sol-t1-0280}
**Solución A5.** El denominador se factoriza como $x^2-4=(x-2)(x+2)$. El dominio natural es, por tanto,

$$
A=\mathbb R\setminus\{-2,2\}.
$$

Los polinomios son diferenciables en toda la recta y el denominador es distinto de cero en $A$. Por @thm-t1-0029,

$$
\begin{aligned}
r'(x)&=\frac{2x(x^2-4)-(x^2+1)2x}{(x^2-4)^2}\\
&=\boxed{-\frac{10x}{(x^2-4)^2}},\qquad x\in A.
\end{aligned}
$$

No existe $r(2)$ en la función original; en consecuencia, tampoco existe $r'(2)$. Una fórmula de derivada no puede extender el dominio por sí sola.
:::

::: {#sol-t1-0281}
**Solución A6.** Por la definición aplicada a la identidad, $D(x)=1$. La regla del producto, ya demostrada, da primero

$$
D(x^2)=D(x\cdot x)=1\cdot x+x\cdot1=2x.
$$

Escribimos ahora $x^3=x^2\cdot x$ y volvemos a utilizar la misma regla:

$$
D(x^3)=D(x^2)\,x+x^2D(x)=2x\cdot x+x^2
=\boxed{3x^2}.
$$

Todas las funciones se consideran sobre $\mathbb R$, así que no hay restricciones de dominio. La fórmula general para las potencias es una conclusión posterior que este cálculo ayuda a reconstruir, no una hipótesis utilizada.
:::

::: {#sol-t1-0282}
**Solución A7.** Tomamos $f:\mathbb R\to\mathbb R$, $f(x)=3x+1$, y $g:\mathbb R\to\mathbb R$, $g(t)=t^4$. Entonces $g\circ f(x)=(3x+1)^4$. Para un punto $a$:

$$
f(a)=3a+1,\quad f'(a)=3,\quad
g'(t)=4t^3.
$$

Ambas funciones son diferenciables en todos los puntos pertinentes. Aplicando @thm-t1-0030,

$$
(g\circ f)'(a)=g'(f(a))f'(a)
=4(3a+1)^3\cdot3=\boxed{12(3a+1)^3}.
$$

La derivada exterior se calcula en la *salida* de la función interior, $f(a)$; escribir $g'(a)$ sustituiría injustificadamente una entrada por otra.
:::

#### Soluciones del nivel B

::: {#sol-t1-0283}
**Solución B1.** Cada monomio es diferenciable por @prp-t1-0040, la constante tiene derivada cero, y @thm-t1-0027 permite derivar la combinación finita. Obtenemos, para cualquier $x\in\mathbb R$,

$$
\begin{aligned}
p'(x)&=3(5x^4)-2(3x^2)+7(1)-0\\
&=\boxed{15x^4-6x^2+7}.
\end{aligned}
$$

El dominio es toda la recta: ninguna de estas operaciones introduce un denominador ni restringe las entradas. No se ha usado una regla de composición.
:::

::: {#sol-t1-0284}
**Solución B2.** Definimos $f(x)=x^2+1$, $g(x)=x^3-2x$ sobre $\mathbb R$. Sus derivadas polinómicas son $f'(x)=2x$, $g'(x)=3x^2-2$. Por la regla del producto,

$$
\begin{aligned}
p'(x)&=2x(x^3-2x)+(x^2+1)(3x^2-2)\\
&=2x^4-4x^2+3x^4+x^2-2\\
&=\boxed{5x^4-3x^2-2}.
\end{aligned}
$$

De modo independiente, antes de derivar expandimos la función: $p(x)=x^5-x^3-2x$. La derivación polinómica da $5x^4-3x^2-2$, coincidente con el cálculo anterior. Esta comprobación no presupone la regla del producto para obtener la forma expandida.
:::

::: {#sol-t1-0285}
**Solución B3.** El dominio original es $A=\mathbb R\setminus\{2\}$. Para $x\in A$, numerador y denominador son polinomios diferenciables y $x-2\ne0$. La regla del cociente da

$$
\begin{aligned}
r'(x)&=\frac{2x(x-2)-(x^2+1)}{(x-2)^2}\\
&=\boxed{\frac{x^2-4x-1}{(x-2)^2}}.
\end{aligned}
$$

En $x=2$ la función $r$ no está definida y no puede tener derivada, con independencia de que una manipulación formal sugiera otra expresión.
:::

::: {#sol-t1-0286}
**Solución B4.** En $A=\mathbb R\setminus\{0\}$, la potencia cuarta $u(x)=x^4$ no se anula. Su derivada es $u'(x)=4x^3$ por @prp-t1-0040. Como $r=1/u$, la proposición del recíproco @prp-t1-0039 implica

$$
r'(x)=-\frac{u'(x)}{u(x)^2}
=-\frac{4x^3}{x^8}=\boxed{-4x^{-5}},
\qquad x\ne0.
$$

La simplificación se realiza únicamente donde $x\ne0$; no se ha supuesto una regla previa para exponentes negativos. En cero, $x^{-4}$ no tiene valor definido.
:::

::: {#sol-t1-0287}
**Solución B5.** La función interior es $f(x)=2x^2-1$, la exterior $g(t)=t^5$, ambas de $\mathbb R$ en $\mathbb R$. Sus derivadas son

$$
f'(x)=4x,\qquad g'(t)=5t^4.
$$

La composición satisface todas las hipótesis de la regla de la cadena. Por ello,

$$
\boxed{D((2x^2-1)^5)=5(2x^2-1)^4\,4x
=20x(2x^2-1)^4}.
$$

En particular, el término exterior se evalúa en $t=f(x)=2x^2-1$, no en $t=x$.
:::

::: {#sol-t1-0288}
**Solución B6.** Introducimos los valores intermedios

$$
u_1=x^2+1,\qquad u_2=u_1^3,\qquad
u_3=u_2-2,\qquad H=u_3^4.
$$

Las cuatro funciones elementales de esta cadena son polinómicas, luego sus derivadas existen sobre $\mathbb R$. Sucesivas aplicaciones de @thm-t1-0030, o @prp-t1-0041, entregan

$$
\begin{aligned}
H'(x)&=4u_3^3\cdot1\cdot3u_1^2\cdot2x\\
&=\boxed{24x(x^2+1)^2\bigl((x^2+1)^3-2\bigr)^3}.
\end{aligned}
$$

La resta de $2$ aporta derivada $1$ respecto de $u_2$. Es decisivo sustituir cada valor intermedio solo *después* de calcular la derivada del eslabón correspondiente.
:::

::: {#sol-t1-0289}
**Solución B7.** Las funciones $f(x)=x^2$ y $g(x)=x+1$, restringidas a $A=[0,\infty)$, son diferenciables relativamente a ese dominio en $0$. Sus derivadas relativas son $f'_A(0)=0$, $g'_A(0)=1$, y sus valores centrales son $f(0)=0$, $g(0)=1$. Por @thm-t1-0028,

$$
p'_A(0)=f'_A(0)g(0)+f(0)g'_A(0)
=0\cdot1+0\cdot1=\boxed{0}.
$$

Para verificarlo desde la definición, los incrementos admisibles no nulos son $h>0$:

$$
\frac{p(h)-p(0)}h=\frac{h^2(h+1)}h
=h(h+1)\longrightarrow0\quad(h\downarrow0).
$$

La derivada solicitada es relativa al dominio declarado; no hemos supuesto ninguna extensión bilateral.
:::

#### Soluciones del nivel C

::: {#sol-t1-0290}
**Solución C1.** Escribamos $S_n=\sum_{k=1}^n c_kf_k$. Para $n=1$, la multiplicación por un escalar, caso particular de @thm-t1-0027, establece la diferenciabilidad de $S_1=c_1f_1$ y $S'_{1,A}(a)=c_1f'_{1,A}(a)$.

Supongamos para cierto $n\ge1$ que $S_n$ es diferenciable y que $S'_{n,A}(a)=\sum_{k=1}^n c_kf'_{k,A}(a)$. Entonces $S_{n+1}=S_n+c_{n+1}f_{n+1}$ es combinación lineal de dos funciones diferenciables en el mismo punto y dominio. La linealidad proporciona

$$
\begin{aligned}
S'_{n+1,A}(a)&=S'_{n,A}(a)+c_{n+1}f'_{n+1,A}(a)\\
&=\sum_{k=1}^{n+1}c_kf'_{k,A}(a).
\end{aligned}
$$

El paso está probado y la inducción concluye el resultado para todo $n\ge1$. La finitud es esencial: aquí no se ha intercambiado una derivada con una serie infinita.
:::

::: {#sol-t1-0291}
**Solución C2.** Para $n=1$, la fórmula tiene un único término $f'_{1,A}(a)$ multiplicado por el producto vacío $1$. Supongamos probada la fórmula para $P_n=\prod_{k=1}^n f_k$. Es una función diferenciable en $a$. Como $P_{n+1}=P_nf_{n+1}$, @thm-t1-0028 da

$$
P'_{n+1,A}(a)=P'_{n,A}(a)f_{n+1}(a)
+P_n(a)f'_{n+1,A}(a).
$$

Insertando la hipótesis inductiva, el primer sumando contiene los términos indexados por $1\le j\le n$, cada uno multiplicado por $f_{n+1}(a)$; el segundo es precisamente el término $j=n+1$. Así,

$$
\boxed{P'_{n+1,A}(a)=\sum_{j=1}^{n+1} f'_{j,A}(a)
\prod_{\substack{1\le k\le n+1\\k\ne j}} f_k(a)}.
$$

La inducción vale aun si uno o varios factores se anulan, porque en ningún paso se ha dividido por ellos.
:::

::: {#sol-t1-0292}
**Solución C3.** Sea $u:\mathbb R\to\mathbb R$, $u(x)=x$. Es diferenciable con $u'(a)=1$ para todo real $a$. Para $a\ne0$ podemos tomar su recíproco en un entorno del punto. @prp-t1-0039 asegura

$$
D\!\left(\frac1u\right)(a)
=-\frac{u'(a)}{u(a)^2}=-\frac1{a^2}.
$$

Por tanto, en el dominio $\mathbb R\setminus\{0\}$,

$$
\boxed{D(x^{-1})=-x^{-2}}.
$$

En $a=0$ la función recíproca no está definida; tampoco existe una derivada de esa función allí. La fórmula se ha construido desde el recíproco, no desde una regla general para exponentes negativos.
:::

::: {#sol-t1-0293}
**Solución C4.** Para todo $x\in\mathbb R$, se tiene $x^2+1\ge1$, luego $(x^2+1)^3\ge1$ y

$$
q(x)=1+(x^2+1)^3\ge2>0.
$$

El dominio natural de $R=1/q$ es toda $\mathbb R$. Por cadena y linealidad,

$$
q'(x)=3(x^2+1)^2\cdot2x=6x(x^2+1)^2.
$$

La regla del recíproco, aplicada ahora que $q$ es diferenciable y no nula, da

$$
\boxed{R'(x)=-\frac{6x(x^2+1)^2}
{\bigl(1+(x^2+1)^3\bigr)^2}},
\qquad x\in\mathbb R.
$$

La demostración de positividad no es una formalidad: justifica que no hay puntos excluidos donde la fórmula resultaría ilegítima.
:::

::: {#sol-t1-0294}
**Solución C5.** La composición solo está definida donde $f(x)=x^2$ pertenece al dominio de $g$, es decir, donde $x^2\ne1$. Su dominio efectivo es

$$
A=\mathbb R\setminus\{-1,1\}.
$$

Para $t\ne1$, la regla del recíproco aplicada a $t-1$ da $g'(t)=-1/(t-1)^2$. Como $f'(x)=2x$, la cadena sobre $A$ permite concluir

$$
\boxed{(g\circ f)'_A(x)
=g'(x^2)\,2x=-\frac{2x}{(x^2-1)^2}},
\quad x\in A.
$$

En $x=\pm1$ la función exterior recibe la entrada prohibida $t=1$. No hay valor de la composición allí y no puede atribuirse una derivada a la función original en esos puntos.
:::

::: {#sol-t1-0295}
**Solución C6.** En la ruta del producto, $H=(x^2+1)(x^2+1)$ y ambos factores son diferenciables. Aplicando @thm-t1-0028,

$$
H'(x)=2x(x^2+1)+(x^2+1)2x
=4x(x^2+1).
$$

En la ruta de composición, $f(x)=x^2+1$ y $g(t)=t^2$. Puesto que $g'(t)=2t$ y $f'(x)=2x$, @thm-t1-0030 da

$$
(g\circ f)'(x)=2f(x)\,f'(x)
=2(x^2+1)2x=4x(x^2+1).
$$

Ambos razonamientos son válidos para todo real y concuerdan. La primera ruta no necesita la cadena; la segunda explica el punto donde se evalúa la derivada exterior.
:::

::: {#sol-t1-0296}
**Solución C7.** Como $g$ es diferenciable en $a$, @thm-t1-0024 la hace continua relativamente a $A$ en ese punto. Elegimos $\varepsilon=|g(a)|/2>0$. Existe $\delta>0$ tal que, para $x=a+h\in A$ con $|h|<\delta$,

$$
|g(a+h)-g(a)|<\frac{|g(a)|}{2}.
$$

Aplicamos la desigualdad triangular inversa:

$$
|g(a+h)|\ge|g(a)|-|g(a+h)-g(a)|
>\boxed{\frac{|g(a)|}{2}}>0.
$$

Esta cota proporciona simultáneamente la no anulación local y una separación cuantitativa de cero. El dominio del recíproco contiene así un entorno relativo de $a$, de manera que las derivadas calculadas en él preservan los incrementos suficientemente pequeños del dominio inicial.
:::

#### Soluciones del nivel D

::: {#sol-t1-0297}
**Solución D1.** Con $f=g=x$ en $\mathbb R$, las pendientes en $1$ son $1$ y $1$; sin embargo, el producto $x^2$ tiene derivada $2$. El error consiste en reemplazar el cociente incremental de $fg$ por el *producto* de los cocientes de $f$ y $g$: esas expresiones no son iguales. Para encontrar la identidad correcta, añadimos y sustraemos $f(a+h)g(a)$:

$$
\begin{aligned}
&f(a+h)g(a+h)-f(a)g(a)\\
&=f(a+h)[g(a+h)-g(a)]
+g(a)[f(a+h)-f(a)].
\end{aligned}
$$

Para $h\ne0$ admisible dividimos por $h$. Los cocientes de $f$ y $g$ convergen a sus derivadas; además, $f(a+h)\to f(a)$ porque diferenciabilidad implica continuidad. Por el álgebra de límites,

$$
\boxed{(fg)'_A(a)=f(a)g'_A(a)+g(a)f'_A(a)}.
$$

La continuidad solo se invoca después de establecer la identidad. En particular, la derivabilidad del producto es una conclusión del argumento.
:::

::: {#sol-t1-0298}
**Solución D2.** Tomemos $f(x)=x^2$, $g(x)=x$ y $a=1$. Como $g(1)=1\ne0$, el cociente $q=f/g$ está definido sobre $\mathbb R\setminus\{0\}$ y allí satisface $q(x)=x$. En el punto $1$,

$$
q'(1)=1,\qquad \frac{f'(1)}{g'(1)}=\frac21=2.
$$

Todas las cantidades exhibidas existen, pero no coinciden; queda refutada la fórmula. Cuando $f$ y $g$ son diferenciables y $g(a)\ne0$, la regla demostrada en §7.4 establece en cambio

$$
\boxed{\left(\frac fg\right)'(a)
=\frac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}}.
$$

Para este ejemplo resulta $(2\cdot1-1\cdot1)/1^2=1$. La condición de no anulación se refiere a $g(a)$, no a $g'(a)$.
:::

::: {#sol-t1-0299}
**Solución D3.** Aquí $a=b=0$, $f(h)-f(0)=0$ para *todo* $h<0$. Por eso la descomposición que divide por tal diferencia no es una identidad válida para todos los incrementos $h\ne0$ admisibles. En cambio, la función

$$
K(t)=\begin{cases}(g(t)-g(0))/t,&t>0,\\g'_{[0,\infty)}(0),&t=0\end{cases}
=\begin{cases}t,&t>0,\\0,&t=0\end{cases}
$$

está definida sobre $[0,\infty)$ y es continua en $0$. Como $g(t)-g(0)=K(t)t$ incluso para $t=0$, obtenemos para todo $h\ne0$ la identidad válida

$$
\frac{g(f(h))-g(f(0))}{h}
=K(f(h))\frac{f(h)-f(0)}h.
$$

La derivada de $f$ en $0$ existe y vale $0$: su cociente es $0$ para $h<0$ y $h$ para $h>0$. También $g'_{[0,\infty)}(0)=0$. Finalmente, $g(f(h))=1$ para $h\le0$ y $1+h^4$ para $h>0$; el cociente directo de la composición es $0$ o $h^3$, respectivamente, y converge a $\boxed{0}$. La prueba reparada y la definición concuerdan sin ninguna división por $\Delta f$.
:::

::: {#sol-t1-0300}
**Solución D4.** La interior $f(x)=x^2$ tiene $f(0)=0$ y derivada $f'(0)=0$. Para la exterior *declarada sobre $\mathbb R$*, los cocientes incrementales en $0$ son $|t|/t$, que valen $-1$ si $t<0$ y $1$ si $t>0$; por tanto, $g'_{\mathbb R}(0)$ no existe. Pero

$$
(g\circ f)(x)=|x^2|=x^2,
\qquad(g\circ f)'(0)=0.
$$

La composición tiene derivada sin que la función exterior original satisfaga las hipótesis suficientes de la cadena. Si definimos *otra función*, $\widetilde g=g|_{[0,\infty)}$, entonces $\widetilde g'_{[0,\infty)}(0)=1$ por cocientes con $t>0$, y la regla sí se aplica a $\widetilde g\circ f$: $1\cdot0=0$. No es lícito confundir esta derivada relativa con la derivada bilateral inexistente de $g$.
:::

::: {#sol-t1-0301}
**Solución D5.** El cociente original $r(x)=x^2/x$ exige $x\ne0$, de modo que su dominio natural es $A=\mathbb R\setminus\{0\}$. En $A$ podemos cancelar el factor y concluir $r(x)=x$; por consiguiente, $r'_A(a)=1$ para cada $a\in A$. Sin embargo, $r(0)$ no está definido: no existe derivada de *esa función* en $0$.

Sí podemos construir una función nueva $\widetilde r:\mathbb R\to\mathbb R$ por $\widetilde r(x)=x$, incluida la asignación expresa $\widetilde r(0)=0$. Su cociente incremental en $0$ es $h/h=1$ para $h\ne0$, así que $\widetilde r'(0)=1$. Este valor pertenece a la extensión, no al cociente original.
:::

::: {#sol-t1-0302}
**Solución D6.** Hay elementos $1/n\in A\setminus\{0\}$ que convergen a $0$, y elementos $-1/n\in B\setminus\{0\}$ que también lo hacen: $0$ es punto de acumulación de ambos dominios. Para sus respectivas funciones nulas, todos los cocientes incrementales admisibles valen $0$, luego $f'_A(0)=g'_B(0)=0$.

La suma natural solo está definida donde ambos dominios coinciden. Como los puntos no nulos de $A$ son positivos y los de $B$ negativos,

$$
A\cap B=\{0\}.
$$

En la intersección, $0$ es aislado. La definición de derivada relativa exige un punto de acumulación del dominio, de modo que la suma *no tiene derivada relativa allí en nuestro sentido*. La fórmula de linealidad no es aplicable: no hay incrementos no nulos del dominio común sobre los cuales calcular el límite.
:::

#### Soluciones del nivel E

::: {#sol-t1-0303}
**Solución E1.** En $\mathbb R$, tanto $f$ como $g$ valen $|x|$. Como $f(0)=g(0)=0$, para $h\ne0$ los cocientes incrementales de ambos son

$$
\frac{|h|}{h}=\begin{cases}-1,&h<0,\\1,&h>0.\end{cases}
$$

No tienen límite bilateral, luego ninguno de los factores es diferenciable en $0$. Sin embargo, $(fg)(x)=|x|^2=x^2$ en toda la recta y

$$
\frac{(fg)(h)-(fg)(0)}h=\frac{h^2}{h}=h\longrightarrow0.
$$

El producto es diferenciable en $0$, con $(fg)'(0)=0$. La regla del producto solo ofrecía una hipótesis suficiente, no una caracterización necesaria de los productos diferenciables.
:::

::: {#sol-t1-0304}
**Solución E2.** Definimos $f=g=1+|x|$ sobre $\mathbb R$. Para ambos, el cociente incremental en $0$ es

$$
\frac{1+|h|-1}{h}=\frac{|h|}{h},
$$

que tiene límites laterales distintos. Ninguna función es diferenciable en $0$. No obstante, $g(x)=1+|x|\ge1>0$ para todo $x$; el cociente original está definido en toda la recta y

$$
q(x)=\frac{1+|x|}{1+|x|}=1.
$$

Por definición, $(q(h)-q(0))/h=0$ para $h\ne0$ y $q'(0)=0$. La fórmula del cociente no podía aplicarse porque faltan las derivadas de los factores, aunque el resultado sí se deriva directamente. No se ha rellenado ningún punto ausente.
:::

::: {#sol-t1-0305}
**Solución E3.** Tomemos $f(x)=x^2$ y $g(t)=|t|$, cada una con dominio $\mathbb R$ y codominio $\mathbb R$. El punto central es $a=0$, con imagen $b=f(0)=0$. La derivada $f'(0)=0$ existe, pero el cociente de $g$ en $b$ toma los valores $-1$ a la izquierda y $1$ a la derecha, así que $g'_{\mathbb R}(0)$ no existe.

Como $f(x)\ge0$ para todo $x$,

$$
(g\circ f)(x)=|x^2|=x^2,
\qquad(g\circ f)'(0)=\lim_{h\to0}h=0.
$$

Falla la hipótesis de diferenciabilidad de la exterior en $b$ para las funciones completas declaradas. El valor de la derivada compuesta se obtuvo desde su definición, no multiplicando una derivada inexistente por cero.
:::

::: {#sol-t1-0306}
**Solución E4.** Puesto que $0\in\mathbb Q$, $f(0)=0$. Para todo $h\ne0$ tenemos $0\le f(h)\le h^2$, independientemente de si $h$ es racional o irracional. En consecuencia,

$$
\left|\frac{f(h)-f(0)}h\right|\le|h|\longrightarrow0,
$$

por lo que $f'_{\mathbb R}(0)=0$ y, en particular, $f$ es continua en $0$. La densidad de los racionales garantiza infinitos racionales no nulos arbitrariamente próximos a $0$ con $f(h)=f(0)=0$; la densidad de los irracionales garantiza, en cada entorno de $0$, un irracional no nulo $s$ para el que $f(s)=s^2>0$. Así, $f$ no es localmente constante.

La exterior $g:[0,\infty)\to\mathbb R$, $g(t)=t^2+1$, tiene derivada relativa $g'_{[0,\infty)}(0)=0$ desde $(g(t)-g(0))/t=t$ para $t>0$. La composición vale $1+f(x)^2$ y, para $h\ne0$,

$$
\left|\frac{(g\circ f)(h)-(g\circ f)(0)}h\right|
=\frac{f(h)^2}{|h|}\le|h|^3\longrightarrow0.
$$

Por tanto, $(g\circ f)'(0)=0=g'_{[0,\infty)}(0)f'(0)$. La comprobación utiliza cotas y no divide por $f(h)-f(0)$, que es nulo para infinitos incrementos.
:::

::: {#sol-t1-0307}
**Solución E5.** Declaramos $f:\mathbb R\to[0,\infty)$, $f(x)=|x|$, y $g:[0,\infty)\to\mathbb R$, $g(t)=7$. La derivada de la interior en $0$ no existe: $|h|/h$ vale $-1$ a la izquierda y $1$ a la derecha. La exterior es constante y posee derivada relativa cero en todos los puntos de acumulación de su dominio, incluido el extremo $0$.

La composición está definida para todo real y satisface $(g\circ f)(x)=7$. Su cociente incremental en $0$ es

$$
\frac{(g\circ f)(h)-(g\circ f)(0)}h=
\frac{7-7}{h}=0,
$$

así que $(g\circ f)'(0)=0$. No podemos *invocar* la regla de la cadena con la interior original, que carece de derivada en $0$; el cálculo directo muestra que la composición puede ser diferenciable igualmente.
:::

#### Soluciones del nivel F

::: {#sol-t1-0308}
**Solución F1.** La variación que debemos analizar es $f(a+h)g(a+h)-f(a)g(a)$. Añadimos y sustraemos el producto intermedio $f(a+h)g(a)$ y agrupamos:

$$
\begin{aligned}
&f(a+h)g(a+h)-f(a)g(a)\\
&=f(a+h)[g(a+h)-g(a)]
+g(a)[f(a+h)-f(a)].
\end{aligned}
$$

La identidad es puramente algebraica y vale incluso con $h=0$. Para $h\ne0$ admisible, dividimos por $h$:

$$
\frac{(fg)(a+h)-(fg)(a)}h
=f(a+h)\frac{g(a+h)-g(a)}h
+g(a)\frac{f(a+h)-f(a)}h.
$$

Por diferenciabilidad, los dos cocientes convergen a $g'_A(a)$ y $f'_A(a)$. La diferenciabilidad de $f$ implica además $f(a+h)\to f(a)$ por @thm-t1-0024. Aplicamos el álgebra de límites una vez comprobadas estas tres convergencias: el límite existe, es finito y vale $f(a)g'_A(a)+g(a)f'_A(a)$. Esto prueba, desde la definición, la diferenciabilidad de $fg$ y la fórmula correspondiente sin presuponerla.
:::

::: {#sol-t1-0309}
**Solución F2.** La continuidad de $g$ en $a$, consecuencia de su diferenciabilidad, nos permite elegir $\delta>0$ tal que, si $a+h\in A$ y $|h|<\delta$,

$$
|g(a+h)-g(a)|<|g(a)|/2,
\qquad |g(a+h)|>|g(a)|/2>0.
$$

El recíproco se define, por tanto, en un entorno relativo del punto central. Su diferencia exacta es

$$
\frac1{g(a+h)}-\frac1{g(a)}
=-\frac{g(a+h)-g(a)}{g(a+h)g(a)}.
$$

Para $h\ne0$ dividimos por $h$ y reordenamos:

$$
\frac{1/g(a+h)-1/g(a)}h
=-\frac1{g(a+h)g(a)}
\frac{g(a+h)-g(a)}h.
$$

La continuidad se usa **dos veces**: primero para probar que los denominadores cercanos no son cero y después para obtener $g(a+h)\to g(a)$. El otro factor tiende a $g'_A(a)$ por definición. El límite existe y da

$$
\boxed{(1/g)'(a)=-\frac{g'_A(a)}{g(a)^2}}.
$$

No se ha utilizado la regla del cociente que esta prueba ayuda a construir.
:::

::: {#sol-t1-0310}
**Solución F3.** Para $n=1$, la función identidad es diferenciable sobre $\mathbb R$ y $D(x)=1=1\cdot x^0$. Supongamos que, para cierto $n\ge1$, la potencia $x^n$ es diferenciable y satisface $D(x^n)=nx^{n-1}$. Factorizamos $x^{n+1}=x^n\cdot x$. La regla del producto asegura su diferenciabilidad y

$$
\begin{aligned}
D(x^{n+1})&=D(x^n)\,x+x^nD(x)\\
&=nx^{n-1}x+x^n=(n+1)x^n.
\end{aligned}
$$

Queda probado el paso inductivo y, con la base, $\boxed{D(x^n)=nx^{n-1}}$ para todo entero $n\ge1$. Para $n=0$ tratamos $x^0=1$ como la función constante sobre $\mathbb R$, cuya derivada es cero; así evitamos expresiones ambiguas en $x=0$ cuando se pretendiera sustituir mecánicamente en $0x^{-1}$. La inducción solo recorre enteros naturales y no demuestra que las potencias de exponentes fraccionarios sean diferenciables: eso exige justificar antes las funciones raíz y sus derivadas.
:::

::: {#sol-t1-0311}
**Solución F4.** Definimos en *todo* $B$ la función

$$
K(t)=\begin{cases}
\dfrac{g(t)-g(b)}{t-b},&t\in B\setminus\{b\},\\[5pt]
g'_B(b),&t=b.
\end{cases}
$$

El límite definitorio de $g'_B(b)$ asegura $\lim_{t\to b,\,t\in B\setminus\{b\}}K(t)=g'_B(b)=K(b)$. Por tanto, $K$ es continua en $b$ relativamente a $B$. La identidad

$$
g(t)-g(b)=K(t)(t-b)
$$

vale para $t\ne b$ por construcción y para $t=b$ porque ambos lados son cero. En particular, para todo $h\ne0$ admisible en $A$, incluso cuando $f(a+h)=b$,

$$
\frac{(g\circ f)(a+h)-(g\circ f)(a)}h
=K(f(a+h))\frac{f(a+h)-f(a)}h.
$$

La diferenciabilidad de $f$ proporciona tanto $f(a+h)\to b$ como el límite $f'_A(a)$ del segundo factor. La continuidad relativa de $K$ en $b$ proporciona $K(f(a+h))\to g'_B(b)$. Por las leyes de límites, el cociente de la composición converge al número finito $g'_B(b)f'_A(a)$. Esto demuestra la diferenciabilidad y la regla de la cadena sin cociente interior indefinido.
:::

::: {#sol-t1-0312}
**Solución F5.** Sean $L=f'_A(a)$ y $M=g'_B(b)$, con $b=f(a)$. De la diferenciabilidad de $f$ obtenemos, para $h$ admisible,

$$
f(a+h)=b+Lh+r_f(h),
\qquad \frac{r_f(h)}h\longrightarrow0.
$$

Escribamos $t=t(h)=f(a+h)-b=Lh+r_f(h)$; entonces $t(h)\to0$ y

$$
\frac{t(h)}h=L+\frac{r_f(h)}h\longrightarrow L.
$$

En particular, $t(h)/h$ está acotado para $h\ne0$ suficientemente pequeño. La diferenciabilidad de $g$ permite definir $\eta(t)=\frac{g(b+t)-g(b)}t-M$ cuando $t\ne0$ y $\eta(0)=0$, restringiendo $t$ a los desplazamientos admisibles de $B$. Entonces $\eta(t)\to0$ y la identidad

$$
g(b+t)=g(b)+Mt+t\eta(t)
$$

es válida también para $t=0$. Como $\eta(t(h))\to0$, se tiene

$$
\frac{t(h)\eta(t(h))}{h}
=\frac{t(h)}h\eta(t(h))\longrightarrow0.
$$

Por ello $t(h)\eta(t(h))=o(h)$ incluso si $t(h)=0$ para infinitos incrementos. Sustituyendo la primera linealización en la segunda,

$$
\begin{aligned}
(g\circ f)(a+h)
&=g(b)+M[Lh+r_f(h)]+t(h)\eta(t(h))\\
&=g(b)+MLh+o(h).
\end{aligned}
$$

La unicidad del coeficiente lineal, o directamente el cociente incremental, da $(g\circ f)'_A(a)=\boxed{ML=g'_B(f(a))f'_A(a)}$. No se aplicó la regla de la cadena: se reconstruyó su conclusión mediante residuos controlados.
:::

#### Soluciones del nivel G

::: {#sol-t1-0313}
**Solución G1.** Para $n=1$ vale la fórmula con producto vacío igual a $1$. Si para $P_n=\prod_{k=1}^n f_k$ sabemos que

$$
P'_n(a)=\sum_{j=1}^n f'_j(a)
\prod_{\substack{1\le k\le n\\k\ne j}}f_k(a),
$$

la regla del producto aplicada a $P_{n+1}=P_nf_{n+1}$ da

$$
P'_{n+1}(a)=P'_n(a)f_{n+1}(a)+P_n(a)f'_{n+1}(a).
$$

La sustitución de la hipótesis inductiva genera los términos $j=1,\ldots,n$ con el nuevo factor $f_{n+1}(a)$ y el término adicional $j=n+1$. La fórmula queda demostrada para todo $n\ge1$, en particular para el $n\ge2$ pedido, sin dividir por factores.

Si $f_p(a)=f_q(a)=0$ con $p\ne q$, cada sumando de la fórmula omite como máximo *un* factor: contiene entonces al menos uno de los factores nulos. Por tanto,

$$
\boxed{P'(a)=0}.
$$

Si exactamente un factor $f_j(a)$ es cero, todos los términos con índice distinto de $j$ incluyen ese valor nulo. Solo sobrevive el término indexado por $j$:

$$
\boxed{P'(a)=f'_j(a)\prod_{k\ne j} f_k(a)}.
$$

No se concluye automáticamente que esta última derivada sea distinta de cero, pues también podría anularse $f'_j(a)$.
:::

::: {#sol-t1-0314}
**Solución G2.** Definimos $f(0)=0$ y, para cualquier real $x$, $f(x)=0$ si $x\in\mathbb Q$ y $f(x)=x^2$ si $x\notin\mathbb Q$. Para $h\ne0$,

$$
\left|\frac{f(h)-f(0)}h\right|\le|h|,
$$

pues $|f(h)|\le h^2$. El criterio del sándwich muestra que $f'(0)=0$. Por densidad de $\mathbb Q$, cada entorno de $0$ contiene infinitos racionales $h\ne0$ tales que $f(h)-f(0)=0$; por densidad de los irracionales, cada entorno contiene también un irracional $s\ne0$ con $f(s)=s^2>0$. Luego $f$ no es constante en ningún entorno de $0$.

Tomamos $g:\mathbb R\to\mathbb R$, $g(t)=3t+1$. Como $g'(t)=3$ para todo $t$, $g'(f(0))f'(0)=3\cdot0=0$. Verificamos la derivada compuesta *sin recurrir a la cadena*:

$$
\frac{(g\circ f)(h)-(g\circ f)(0)}h
=3\frac{f(h)}h\longrightarrow0.
$$

Así, $(g\circ f)'(0)=0=g'(f(0))f'(0)$. La descomposición formal que divide por $f(h)-f(0)$ carece de sentido en cualquiera de los infinitos incrementos racionales citados; la identidad por extensión o el cálculo directo sí son válidos. La exterior es afín y no constante, por lo que la coincidencia no depende de aplanar la composición mediante una función constante.
:::

::: {#sol-t1-0315}
**Solución G3.** Escribamos $F=f(a)$, $G=g(a)\ne0$, $L=f'_A(a)$ y $M=g'_A(a)$. Por diferenciabilidad existen residuos tales que, para incrementos admisibles,

$$
f(a+h)=F+Lh+r_f(h),\qquad
g(a+h)=G+Mh+r_g(h),
$$

con $r_f(h)/h\to0$ y $r_g(h)/h\to0$. Como $g$ es continua en $a$, elegimos $\delta>0$ de modo que $|g(a+h)-G|<|G|/2$ cuando $a+h\in A$ y $|h|<\delta$. En ese entorno, $|g(a+h)|>|G|/2>0$, por lo que el cociente está definido. Para $h\ne0$ suficientemente pequeño, restamos el valor central *sin usar ninguna regla de derivación de cocientes*:

$$
\begin{aligned}
\frac{\dfrac{f(a+h)}{g(a+h)}-\dfrac FG}{h}
&=\frac{G[f(a+h)-F]-F[g(a+h)-G]}
{h\,G\,g(a+h)}\\
&=\frac{G\left(L+\dfrac{r_f(h)}h\right)
-F\left(M+\dfrac{r_g(h)}h\right)}
{G\,g(a+h)}.
\end{aligned}
$$

El numerador tiende a $GL-FM$. Por continuidad, $g(a+h)\to G$; el denominador tiende al número no nulo $G^2$. Las leyes de límites, aplicadas a esta *identidad exacta*, prueban que el cociente incremental converge al número finito

$$
\boxed{\left(\frac fg\right)'_A(a)
=\frac{LG-FM}{G^2}
=\frac{f'_A(a)g(a)-f(a)g'_A(a)}{g(a)^2}}.
$$

La no anulación local fue necesaria para escribir la fracción inicial y pasar al límite. No se dividió por incrementos de $f$ o $g$, que podrían ser cero, ni se usaron las reglas del recíproco o del cociente como premisas.
:::
