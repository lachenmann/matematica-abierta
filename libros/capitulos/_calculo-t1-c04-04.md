## El álgebra de límites: cuándo podemos calcular sin volver a $\varepsilon$ {#sec-t1-c04-04}

Hasta ahora, cada vez que quisimos demostrar un límite tuvimos que regresar a la definición

$$
\forall\varepsilon>0\;\exists N\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

Ese trabajo era necesario. Antes de utilizar reglas de cálculo debíamos demostrar que esas reglas son compatibles con la noción rigurosa de convergencia que acabamos de construir.

La pregunta de esta sección es la siguiente:

$$
\boxed{
\text{si conocemos los límites de dos sucesiones, ¿qué ocurre al sumarlas, multiplicarlas o dividirlas?}
}
$$

Las respuestas serán las que sugiere el álgebra ordinaria, pero no las aceptaremos por analogía. Las deduciremos de la definición $\varepsilon$–$N$.

El premio por hacer ese trabajo una vez será considerable: después podremos calcular muchos límites sin reconstruir desde cero una prueba con tolerancias.

### Las reglas algebraicas son teoremas, no convenciones

Supongamos que

$$
a_n\to A
$$

y

$$
b_n\to B.
$$

Es natural esperar

$$
a_n+b_n\to A+B,
$$

$$
a_nb_n\to AB,
$$

y, cuando el denominador no plantee problemas,

$$
\frac{a_n}{b_n}\to\frac AB.
$$

Pero cada una de estas afirmaciones contiene una dificultad distinta.

Para la suma, la distancia al límite esperado se separa inmediatamente:

$$
\begin{aligned}
|(a_n+b_n)-(A+B)|
&=|(a_n-A)+(b_n-B)|\\
&\le |a_n-A|+|b_n-B|.
\end{aligned}
$$

Así, podemos repartir la tolerancia entre dos errores que ya sabemos controlar.

Para el producto aparece algo nuevo. La identidad útil es

$$
\begin{aligned}
a_nb_n-AB
&=a_nb_n-Ab_n+Ab_n-AB\\
&=b_n(a_n-A)+A(b_n-B).
\end{aligned}
$$

Por tanto,

$$
|a_nb_n-AB|
\le
|b_n|\,|a_n-A|+|A|\,|b_n-B|.
$$

El segundo término contiene una constante $|A|$, pero el primero contiene el factor variable $|b_n|$. Saber únicamente que $|a_n-A|$ puede hacerse pequeño no basta si no controlamos cuánto puede valer $|b_n|$.

Aquí reaparece exactamente el resultado de §4.3:

> toda sucesión convergente es acotada.

La acotación permitirá reemplazar el factor variable $|b_n|$ por una constante fija.

El cociente contiene una dificultad diferente: aunque $B\ne0$, necesitamos asegurar que los términos $b_n$ tampoco se acerquen peligrosamente a cero cuando $n$ sea grande.

Estas tres ideas —**repartir el error**, **acotar factores variables** y **separar denominadores de cero**— constituyen la ingeniería de las leyes algebraicas del límite.

::: {#prp-t1-0021}
**Álgebra de límites secuenciales.** Sean $(a_n)$ y $(b_n)$ sucesiones reales tales que

$$
a_n\to A
\qquad\text{y}\qquad
b_n\to B.
$$

Entonces:

1. para todo $c\in\mathbb R$,
   $$
   ca_n\to cA;
   $$
2. 
   $$
   a_n+b_n\to A+B;
   $$
3. 
   $$
   a_nb_n\to AB;
   $$
4. si $B\ne0$, entonces existe una cola en la que $b_n\ne0$ y, sobre esa cola,
   $$
   \frac{a_n}{b_n}\to\frac AB.
   $$

En particular, usando $c=-1$, también

$$
a_n-b_n\to A-B.
$$

**Demostración.** Demostraremos cada afirmación directamente desde la definición de convergencia.

**1. Multiplicación por una constante.** Si $c=0$, entonces $ca_n=0$ para todo $n$, y la sucesión constante nula converge a $0=cA$.

Supongamos ahora $c\ne0$. Sea $\varepsilon>0$. Como $a_n\to A$, existe $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
|a_n-A|<\frac{\varepsilon}{|c|}.
$$

Entonces, para todo $n\ge N$,

$$
|ca_n-cA|
=|c|\,|a_n-A|
<|c|\frac{\varepsilon}{|c|}
=\varepsilon.
$$

Por tanto,

$$
ca_n\to cA.
$$

**2. Suma.** Sea $\varepsilon>0$. Como $a_n\to A$, existe $N_1$ tal que

$$
n\ge N_1
\quad\Longrightarrow\quad
|a_n-A|<\frac\varepsilon2.
$$

Como $b_n\to B$, existe $N_2$ tal que

$$
n\ge N_2
\quad\Longrightarrow\quad
|b_n-B|<\frac\varepsilon2.
$$

Tomemos

$$
N=\max\{N_1,N_2\}.
$$

Si $n\ge N$, ambas estimaciones son válidas simultáneamente y, por la desigualdad triangular,

$$
\begin{aligned}
|(a_n+b_n)-(A+B)|
&\le |a_n-A|+|b_n-B|\\
&<\frac\varepsilon2+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Luego

$$
a_n+b_n\to A+B.
$$

**3. Producto.** Esta es la parte delicada. Por @prp-t1-0020, la sucesión convergente $(b_n)$ es acotada. Por tanto existe $M>0$ tal que

$$
|b_n|\le M
$$

para todo índice de la sucesión.

Sea $\varepsilon>0$. Como $a_n\to A$, existe $N_1$ tal que

$$
n\ge N_1
\quad\Longrightarrow\quad
|a_n-A|<\frac{\varepsilon}{2M}.
$$

Como $b_n\to B$, existe $N_2$ tal que

$$
n\ge N_2
\quad\Longrightarrow\quad
|b_n-B|<\frac{\varepsilon}{2(|A|+1)}.
$$

Elegimos

$$
N=\max\{N_1,N_2\}.
$$

Para todo $n\ge N$,

$$
\begin{aligned}
|a_nb_n-AB|
&=|b_n(a_n-A)+A(b_n-B)|\\
&\le |b_n|\,|a_n-A|+|A|\,|b_n-B|\\
&\le M|a_n-A|+|A|\,|b_n-B|\\
&<M\frac{\varepsilon}{2M}
+|A|\frac{\varepsilon}{2(|A|+1)}\\
&<\frac\varepsilon2+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Por consiguiente,

$$
a_nb_n\to AB.
$$

**4. Cociente.** Supongamos $B\ne0$. Antes de estudiar $a_n/b_n$ debemos demostrar que el denominador no se anula en una cola.

Como $b_n\to B$, podemos aplicar la definición con la tolerancia

$$
\frac{|B|}{2}>0.
$$

Existe $N_0$ tal que

$$
n\ge N_0
\quad\Longrightarrow\quad
|b_n-B|<\frac{|B|}{2}.
$$

Por la desigualdad triangular inversa,

$$
\bigl||b_n|-|B|\bigr|
\le |b_n-B|.
$$

Así, para $n\ge N_0$,

$$
|b_n|
>|B|-\frac{|B|}{2}
=\frac{|B|}{2}>0.
$$

En particular,

$$
b_n\ne0
$$

para todo $n\ge N_0$. El cociente está, por tanto, bien definido en esa cola.

Demostremos primero que

$$
\frac1{b_n}\to\frac1B.
$$

Sea $\varepsilon>0$. Además del umbral $N_0$, como $b_n\to B$ existe $N_1$ tal que

$$
n\ge N_1
\quad\Longrightarrow\quad
|b_n-B|<\frac{\varepsilon |B|^2}{2}.
$$

Tomemos

$$
N=\max\{N_0,N_1\}.
$$

Entonces, si $n\ge N$,

$$
\begin{aligned}
\left|\frac1{b_n}-\frac1B\right|
&=\frac{|B-b_n|}{|B|\,|b_n|}\\
&\le
\frac{|B-b_n|}{|B|(|B|/2)}\\
&=\frac{2|b_n-B|}{|B|^2}\\
&<\varepsilon.
\end{aligned}
$$

Por tanto,

$$
\frac1{b_n}\to\frac1B.
$$

Finalmente,

$$
\frac{a_n}{b_n}
=a_n\frac1{b_n}
$$

para todo $n$ suficientemente grande. Aplicando la parte del producto,

$$
\frac{a_n}{b_n}\to A\frac1B=\frac AB.
$$

Esto completa la demostración.
:::

### Cómo leer la prueba del producto

La prueba anterior contiene una técnica que aparecerá muchas veces en análisis.

Nuestro objetivo era controlar

$$
|a_nb_n-AB|.
$$

La expresión no estaba inicialmente escrita en términos de los dos errores que la convergencia nos permite hacer pequeños:

$$
|a_n-A|
\qquad\text{y}\qquad
|b_n-B|.
$$

Para hacerlos aparecer introdujimos un término intermedio:

$$
a_nb_n
\longrightarrow
Ab_n
\longrightarrow
AB.
$$

Algebraicamente, esto equivale a sumar y restar $Ab_n$:

$$
a_nb_n-AB
=(a_nb_n-Ab_n)+(Ab_n-AB).
$$

Después la desigualdad triangular transformó el problema en

$$
|b_n|\,|a_n-A|+|A|\,|b_n-B|.
$$

Ahora sí aparecen los errores conocidos, pero uno viene multiplicado por $|b_n|$. La acotación de $(b_n)$ convierte ese factor variable en una constante manejable.

La cadena de ideas es, por tanto,

$$
\boxed{
\text{crear los errores conocidos}
\to
\text{usar desigualdad triangular}
\to
\text{acotar el factor variable}
\to
\text{repartir }\varepsilon.
}
$$

Esto explica por qué @prp-t1-0020 no era una propiedad decorativa. El teorema de acotación se convierte inmediatamente en una herramienta para demostrar otro teorema.

### Una observación sobre las cotas usadas en una prueba

En la demostración del producto usamos una cota global

$$
|b_n|\le M.
$$

En realidad habría bastado una **cota eventual**. Como $b_n\to B$, tomando, por ejemplo, $\varepsilon=1$ obtenemos

$$
|b_n-B|<1
$$

desde algún índice, y entonces

$$
|b_n|
\le |b_n-B|+|B|
<1+|B|.
$$

Esto controla exactamente la cola que interviene en la definición de límite.

La versión global obtenida en §4.3 es más fuerte y más cómoda, pero conviene reconocer qué parte de una hipótesis utiliza realmente una demostración.

### El denominador no nulo no puede tratarse como un detalle

La afirmación

$$
b_n\to B\ne0
$$

contiene más información que simplemente «el límite del denominador no es cero». Garantiza que los términos quedan finalmente dentro de una región que no contiene al cero.

En efecto, desde cierto índice tenemos

$$
|b_n-B|<\frac{|B|}{2},
$$

y por tanto

$$
|b_n|>\frac{|B|}{2}.
$$

Geométricamente, los términos terminan atrapados en un intervalo centrado en $B$ cuyo radio es menor que la distancia de $B$ al origen.

Este paso cumple dos funciones distintas:

1. garantiza que $1/b_n$ está definido en una cola;
2. proporciona la estimación
   $$
   \frac1{|b_n|}<\frac2{|B|},
   $$
   necesaria para controlar el error del recíproco.

No debemos escribir simplemente «como $B\ne0$, dividimos». El denominador de cada término es $b_n$, no $B$; la separación eventual de cero es el puente entre ambos hechos.

### Sucesiones constantes y diferencias

Las leyes anteriores producen inmediatamente varias herramientas básicas.

Para cualquier $c\in\mathbb R$, la sucesión constante

$$
a_n=c
$$

converge a $c$, porque

$$
|a_n-c|=0<\varepsilon
$$

para toda $\varepsilon>0$ y para todos los índices.

Además, si

$$
a_n\to A,
\qquad
b_n\to B,
$$

entonces, aplicando primero la multiplicación por $-1$ y después la suma,

$$
a_n-b_n
=a_n+(-1)b_n
\to
A-B.
$$

Estas consecuencias pequeñas permiten construir expresiones algebraicas cada vez más complejas sin regresar a la definición en cada paso.

### El valor absoluto también respeta el límite

El valor absoluto no es una operación algebraica binaria como suma o producto, pero la desigualdad triangular inversa permite controlarlo directamente.

::: {#cor-t1-0007}
**Límite del valor absoluto.** Si

$$
a_n\to A,
$$

entonces

$$
|a_n|\to|A|.
$$

**Demostración.** Para todo $n$, la desigualdad triangular inversa da

$$
\bigl||a_n|-|A|\bigr|
\le |a_n-A|.
$$

Sea $\varepsilon>0$. Como $a_n\to A$, existe $N$ tal que

$$
n\ge N
\quad\Longrightarrow\quad
|a_n-A|<\varepsilon.
$$

Para esos mismos índices,

$$
\bigl||a_n|-|A|\bigr|
\le |a_n-A|
<\varepsilon.
$$

Por definición,

$$
|a_n|\to|A|.
$$
:::

La demostración merece atención por su economía. No hemos utilizado ninguna afirmación sobre la continuidad de la función $x\mapsto|x|$. Esa teoría todavía no existe en nuestro desarrollo. Todo proviene de una desigualdad ya demostrada en `T1-C02`.

### De la prueba a la herramienta de cálculo

Una vez demostrado @prp-t1-0021, ya podemos utilizarlo como un resultado previo. Esto cambia el modo de resolver muchos problemas.

Si sabemos, por ejemplo, que

$$
a_n\to A
$$

y queremos estudiar una expresión como

$$
3a_n^2-5a_n+7,
$$

no necesitamos construir desde cero un $N(\varepsilon)$ para toda la expresión.

Podemos razonar en capas:

$$
a_n\to A,
$$

luego

$$
a_n^2=a_na_n\to A^2,
$$

entonces

$$
3a_n^2\to3A^2,
$$

$$
-5a_n\to-5A,
$$

y, sumando con la sucesión constante $7$,

$$
3a_n^2-5a_n+7
\to
3A^2-5A+7.
$$

La definición $\varepsilon$–$N$ no ha desaparecido. Está **encapsulada** dentro de los teoremas que acabamos de demostrar.

Esta es una característica fundamental del trabajo matemático: una vez justificada una herramienta, podemos reutilizarla sin repetir cada vez toda su construcción interna.

### Un cociente de polinomios en $n$

Veamos ahora cómo estas leyes convierten un límite aparentemente más complicado en una combinación de límites ya conocidos.

::: {#exm-t1-0035}
**Un límite racional calculado mediante el álgebra de límites.** Consideremos

$$
r_n=\frac{2n+1}{3n-4},
\qquad n\in\mathbb N.
$$

El denominador nunca se anula para un índice natural, porque la ecuación

$$
3n-4=0
$$

tendría la solución $n=4/3$, que no pertenece a $\mathbb N$.

Para $n\ge1$ podemos dividir numerador y denominador por $n$:

$$
r_n
=
\frac{2+1/n}{3-4/n}.
$$

Ya sabemos que

$$
\frac1n\to0
$$

para $n\ge1$. En efecto, dada $\varepsilon>0$, la propiedad arquimediana permite elegir $N$ con $N>1/\varepsilon$; entonces, si $n\ge N$,

$$
0<\frac1n\le\frac1N<\varepsilon.
$$

Es la misma estimación básica que utilizamos en §4.2, ahora escrita para una sucesión que comienza en $n=1$.

Por la multiplicación por constantes,

$$
\frac4n\to0.
$$

Como las sucesiones constantes $2$ y $3$ convergen respectivamente a $2$ y $3$, la ley de la suma da

$$
2+\frac1n\to2
$$

y

$$
3-\frac4n\to3.
$$

El límite del denominador es $3\ne0$. Por la ley del cociente,

$$
\frac{2+1/n}{3-4/n}
\to
\frac23.
$$

Por tanto,

$$
\boxed{
\frac{2n+1}{3n-4}\to\frac23.
}
$$
:::

Obsérvese qué cambió respecto de §4.2. Allí una afirmación como

$$
\frac1{n+1}\to0
$$

requirió abrir la definición, fijar $\varepsilon$ y fabricar un umbral mediante la propiedad arquimediana.

Aquí ya no necesitamos repetir ese mecanismo para toda la fracción. Hemos reducido el problema a piezas cuyos límites conocemos y hemos aplicado resultados generales previamente demostrados.

### Qué está permitido escribir desde ahora

Después de esta sección podremos abreviar razonamientos como

$$
a_n\to A,
\qquad
b_n\to B
$$

mediante expresiones del tipo

$$
\lim_{n\to\infty}(a_n+b_n)=A+B,
$$

$$
\lim_{n\to\infty}(a_nb_n)=AB,
$$

o, si $B\ne0$,

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\frac AB.
$$

Pero estas fórmulas deben leerse como aplicaciones de @prp-t1-0021, no como una licencia para sustituir símbolos mecánicamente.

Antes de usar una regla conviene comprobar:

- que los límites de las piezas realmente existen;
- que la expresión está definida en una cola suficiente;
- que, en un cociente, el límite del denominador es no nulo.

La última condición es esencial. Si

$$
b_n\to0,
$$

la ley del cociente no autoriza ninguna conclusión del tipo

$$
\frac{a_n}{b_n}\to\frac A0.
$$

La expresión $A/0$ ni siquiera es un número real. Los cocientes con denominadores que tienden a cero requerirán análisis adicional según el problema concreto; no existe aquí una regla algebraica automática.

### Qué hemos ganado

La teoría de límites dispone ahora de su primer cálculo interno.

A partir de

$$
a_n\to A,
\qquad
b_n\to B,
$$

sabemos transportar la convergencia a través de:

$$
\text{escalas},
\qquad
\text{sumas y diferencias},
\qquad
\text{productos},
\qquad
\text{cocientes con límite denominador no nulo},
$$

y también a través del valor absoluto.

La estructura de las pruebas revela tres principios reutilizables:

$$
\boxed{
\begin{array}{c}
\text{sincronizar varios controles mediante }\max,\\[3pt]
\text{convertir factores variables en cotas fijas},\\[3pt]
\text{separar de cero aquello que aparecerá en un denominador}.
\end{array}
}
$$

En la siguiente sección añadiremos una estructura distinta: el **orden**. Ya no preguntaremos qué ocurre al combinar sucesiones algebraicamente, sino qué información sobre desigualdades sobrevive al pasar al límite y cómo dos sucesiones pueden atrapar a una tercera.

