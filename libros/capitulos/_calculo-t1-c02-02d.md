### Cuando el signo es desconocido, hay que separar casos

El riesgo aumenta cuando multiplicamos por una expresión cuyo signo depende de la incógnita. Consideremos

$$
\frac{2}{x}<3,
\qquad x\ne0.
$$

No podemos «multiplicar por $x$» sin más, porque todavía no sabemos si $x$ es positivo o negativo.

**Caso 1: $x>0$.** Multiplicar por $x$ conserva el sentido:

$$
2<3x,
$$

de donde

$$
x>\frac23.
$$

Esta condición ya implica $x>0$. Por tanto, las soluciones positivas son

$$
\left(\frac23,\infty\right).
$$

**Caso 2: $x<0$.** Multiplicar por $x$ invierte el sentido:

$$
2>3x.
$$

Dividir por $3>0$ da

$$
x<\frac23.
$$

Junto con la condición del caso $x<0$, esto deja simplemente

$$
x<0.
$$

Por tanto, el conjunto solución completo es

$$
\boxed{
(-\infty,0)
\cup
\left(\frac23,\infty\right).
}
$$

El punto $x=0$ no se considera porque la expresión original no está definida allí.

::: {.callout-warning title="Error frecuente"}
Antes de multiplicar o dividir una desigualdad por una expresión variable, determine su signo.

Si el signo no está fijado por las hipótesis, normalmente habrá que separar casos. Y si la expresión puede valer $0$, deberá auditarse además el dominio antes de dividir.
:::

### Intervalos: traducir entre orden y conjuntos

Las desigualdades describen regiones de la recta real. Para evitar repetir expresiones largas, utilizaremos la notación de intervalos.

::: {#def-t1-0013}
**Intervalos reales.** Sean $a,b\in\mathbb R$. Definimos las notaciones siguientes directamente mediante desigualdades. Cuando $a<b$, describen los intervalos usuales con extremos distintos; los casos $a=b$ y $a>b$ se interpretan literalmente por las mismas fórmulas y se analizan enseguida.

El **intervalo abierto** entre $a$ y $b$ es

$$
(a,b)=\{x\in\mathbb R:a<x<b\}.
$$

El **intervalo cerrado** es

$$
[a,b]=\{x\in\mathbb R:a\le x\le b\}.
$$

Los intervalos **semiabiertos** son

$$
[a,b)=\{x\in\mathbb R:a\le x<b\}
$$

y

$$
(a,b]=\{x\in\mathbb R:a<x\le b\}.
$$

También utilizaremos los intervalos no acotados

$$
(a,\infty)=\{x\in\mathbb R:x>a\},
\qquad
[a,\infty)=\{x\in\mathbb R:x\ge a\},
$$

$$
(-\infty,b)=\{x\in\mathbb R:x<b\},
\qquad
(-\infty,b]=\{x\in\mathbb R:x\le b\}.
$$

Finalmente,

$$
(-\infty,\infty)=\mathbb R.
$$
:::

Los paréntesis y corchetes codifican pertenencia de los extremos finitos. Así,

$$
2\in[2,5)
$$

pero

$$
5\notin[2,5).
$$

La notación es simplemente una traducción compacta entre conjuntos y desigualdades:

$$
x\in(-3,4]
\iff
-3<x\le4.
$$

::: {.callout-note title="Lectura de la fórmula"}
La expresión

$$
(-\infty,5]
$$

no significa que $-\infty$ sea un número real que actúa como extremo izquierdo. Significa exactamente

$$
\{x\in\mathbb R:x\le5\}.
$$

Los símbolos $\infty$ y $-\infty$ funcionan aquí como parte de una notación para describir ausencia de cota en una dirección. **No son números reales.** Por eso nunca «pertenecen» a estos intervalos y la notación usa paréntesis del lado infinito.
:::

### Intervalos degenerados y conjuntos vacíos

Como la notación se ha definido mediante desigualdades para cualesquiera $a,b\in\mathbb R$, los casos frontera no requieren una convención adicional.

Por definición de pertenencia,

$$
[a,a]=\{a\},
$$

mientras que

$$
(a,a)=\varnothing.
$$

Si $a>b$, no existe ningún real que satisfaga simultáneamente $a<x<b$, y el conjunto descrito sería vacío. En la práctica reservaremos la expresión «intervalo de extremos $a$ y $b$» para el orden natural $a\le b$, pero las definiciones por desigualdades permiten diagnosticar cualquier caso sin recurrir a una regla adicional.

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** Si $-4<x\le7$, ¿a qué intervalo pertenece $x$?

**Respuesta:**

$$
x\in(-4,7].
$$
:::

::: {.callout-tip title="Antes de seguir"}
**2.** Si $a<b$ y $c=-3$, ¿qué relación existe entre $ac$ y $bc$?

Como $c<0$, la desigualdad se invierte:

$$
ac>bc.
$$
:::

::: {.callout-tip title="Antes de seguir"}
**3.** Si $0<a<b$, ¿cuál de los recíprocos es mayor?

Por la parte 7 de @prp-t1-0007,

$$
\frac1b<\frac1a.
$$

El orden se invierte al tomar recíprocos positivos.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿Por qué no escribimos $[2,\infty]$ para los reales mayores o iguales que $2$?

Porque $\infty$ no es un número real ni un elemento del conjunto. La notación correcta es

$$
[2,\infty).
$$
:::

### Lo que un cuerpo ordenado todavía no resuelve

Hemos hecho explícitas dos capas distintas de estructura.

La primera fue puramente algebraica:

$$
\text{axiomas de cuerpo}
\longrightarrow
\text{reglas de cálculo algebraico}.
$$

La segunda añadió positividad y comparación:

$$
\text{axiomas de orden}
\longrightarrow
\text{reglas de desigualdad e intervalos}.
$$

Podemos resumir el recorrido de §2.2 así:

$$
\boxed{
\text{cuerpo}
\longrightarrow
\text{álgebra derivada}
\longrightarrow
\text{orden}
\longrightarrow
\text{desigualdades e intervalos}.
}
$$

Pero todavía no hemos respondido la pregunta central de este capítulo.

La razón es decisiva:

$$
\boxed{\mathbb Q\ \text{también es un cuerpo ordenado}.}
$$

Los racionales satisfacen las mismas leyes algebraicas y de orden que acabamos de imponer a $\mathbb R$. Podemos sumar y multiplicar racionales, tomar inversos de racionales no nulos y ordenar racionales de una manera compatible con esas operaciones. Sin embargo, §2.1 demostró que el sistema racional sigue teniendo el hueco asociado a $x^2=2$.

Por tanto,

$$
\boxed{
\text{cuerpo}+\text{orden}
\quad\text{no bastan para explicar la propiedad decisiva de }\mathbb R.
}
$$

Esta observación determina la arquitectura de lo que viene. En §2.3 utilizaremos el orden para construir el lenguaje de **valor absoluto y distancia**. En §2.4 aprenderemos a hablar de **cotas, máximos, mínimos, supremos e ínfimos**. Solo entonces podremos formular en §2.5 la propiedad adicional que distingue a los reales dentro de nuestro desarrollo:

$$
\boxed{\text{la completitud}.}
$$

La secuencia no es accidental. Antes de afirmar que una frontera existe, necesitamos saber con precisión qué significa ser una frontera.
