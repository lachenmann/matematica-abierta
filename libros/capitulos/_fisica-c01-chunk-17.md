$$
y=kx.
$$

Realizamos una observación:

$$
x=2,
\qquad
y=6.
$$

Si elegimos $k$ de modo que la relación reproduzca ese dato, obtenemos

$$
k=\frac{6}{2}=3.
$$

Entonces el modelo

$$
y=3x
$$

reproduce automáticamente el dato utilizado para fijar $k$:

$$
6=3\cdot2.
$$

Eso puede ser útil.

Pero no constituye todavía una prueba independiente del modelo.

::: {.ma-block .ma-definicion #fpm-i-01-d22}
**Definición operativa FPM-I-01-D22 — Ajuste**
Llamaremos **ajuste** al proceso mediante el cual seleccionamos parámetros, condiciones o alguna parte de la forma de un modelo utilizando datos que queremos que el propio modelo reproduzca.
:::

No suponemos aquí ningún método estadístico específico.

El ajuste puede ser tan sencillo como determinar una constante a partir de una observación.
En el ejemplo anterior,

$$
(x_1,y_1)=(2,6)
$$

se utilizó para fijar

$$
k=3.
$$

Por eso, obtener luego

$$
y_1=kx_1
$$

no es un éxito predictivo independiente.

Era parte del procedimiento de construcción.

::: {.ma-block .ma-metodo #fpm-i-01-mp13}
**Principio FPM-I-01-MP13 — No confundir ajuste con predicción**
Un dato utilizado para seleccionar parámetros, condiciones o estructura de un modelo no debe contarse después como una predicción independiente del mismo modelo.
:::

Esta regla parece obvia cuando el ejemplo contiene una sola constante.

En problemas reales puede quedar mucho más escondida.

Un modelo puede contener muchos parámetros y haber sido diseñado tras observar una gran cantidad de datos.

Si evaluamos después su «éxito» únicamente sobre esos mismos datos, podemos estar midiendo principalmente su capacidad de ajuste.
Shankar formula, en esencia, una de las preguntas clásicas de la mecánica: dada suficiente información sobre el estado presente de un sistema, ¿qué puede decirse de su evolución futura?[@shankar2019fundamentals1, cap. 1, §1.2, p. 3]

Este es el sentido temporal habitual de **predicción**:

$$
\text{estado presente}
\longrightarrow
\text{estado futuro}.
$$

Pero para nuestro método necesitamos una noción un poco más amplia.

Una teoría puede producir una consecuencia acerca de:

- un experimento que todavía no hemos realizado;
- una condición todavía no ensayada;
- una observación pasada que no fue utilizada para construir el modelo;
- una cantidad desconocida aunque no esté en el futuro cronológico.

La distinción relevante es entonces **informacional** además de temporal.

::: {.ma-block .ma-definicion #fpm-i-01-d23}
**Definición operativa FPM-I-01-D23 — Predicción**
Una **predicción** es una consecuencia físicamente interpretable de un modelo para una observación, condición o caso cuyo resultado no ha sido utilizado para fijar precisamente esa consecuencia mediante el ajuste del modelo.
:::

Esta definición incluye la predicción temporal como caso central, pero no la reduce a ella.
La predicción física requiere además una conexión observacional:

Supongamos que un modelo, ya fijado, implica:

$$
[\mathrm{MATH}]
\qquad
Y_{\mathrm{pred}}=f(X_0;\theta).
$$

Mientras $Y_{\mathrm{pred}}$ siga siendo solo un objeto del formalismo, todavía falta la conexión experimental.

Necesitamos:

$$
[\mathrm{OBS}]
\qquad
Y
\longleftrightarrow
\text{procedimiento de medición}.
$$

Entonces podemos comparar

$$
Y_{\mathrm{pred}}
$$

con

$$
Y_{\mathrm{obs}}.
$$

La cadena completa es:

$$
\boxed{
\text{modelo fijado}
\to
[\mathrm{MATH}]
\ \text{predicción}
\to
[\mathrm{OBS}]
\ \text{dato}
\to
\text{comparación}.
}
$$

Una predicción física no termina al obtener una fórmula.

Debe poder traducirse en algo contrastable.
Tomemos otra vez

$$
y=kx.
$$

#### Paso 1 — Dato de ajuste

Observamos:

$$
x_1=2,
\qquad
y_1=6.
$$

#### Paso 2 — Ajuste

Fijamos:

$$
k=3.
$$

#### Paso 3 — Nuevo caso

Antes de observar el resultado para

$$
x_2=5,
$$

el modelo produce:

$$
[\mathrm{MATH}]
\qquad
y_{2,\mathrm{pred}}=3\cdot5=15.
$$

#### Paso 4 — Observación nueva

Realizamos el procedimiento experimental y obtenemos cierto

$$
y_{2,\mathrm{obs}}.
$$

Ahora sí existe un contraste entre una consecuencia obtenida **sin usar ese resultado** y una observación posterior.

Si ocurre que

$$
y_{2,\mathrm{obs}}=15
$$

dentro de la precisión pertinente, el nuevo dato es compatible con la predicción.

No hemos demostrado que el modelo sea verdadero.

Hemos superado una prueba nueva.
Una predicción acertada apoya un modelo, pero no lo convierte en teorema:

Supongamos que un modelo predice correctamente un dato.

Podemos concluir:

> el modelo ha producido una consecuencia compatible con esa observación.

No podemos concluir automáticamente:

> ninguna otra descripción física podría producirla.

Ni:

> todas las hipótesis del modelo han quedado demostradas.

Ni:

> el modelo funcionará fuera del régimen contrastado.

La lógica es asimétrica.

Una predicción acertada proporciona apoyo.

Pero no convierte una hipótesis física en un teorema.

En §9 veremos una razón matemática elemental para mantener esta cautela: datos finitos pueden ser compatibles con muchas leyes funcionales distintas.
La predicción temporal conserva una estructura especialmente importante para la mecánica:

Supongamos que el modelo posee un conjunto de estados

$$
\mathcal S
$$

y una regla de evolución de un paso:

$$
E:\mathcal S\to\mathcal S.
$$

Si el estado actual es

$$
s_0\in\mathcal S,
$$

el modelo predice:

$$
s_1=E(s_0).
$$

Y después:

$$
s_2=E(s_1).
$$

No necesitamos ecuaciones diferenciales para comprender la estructura lógica.

La predicción temporal consiste en combinar:

- un estado inicial;
- una regla de evolución;
- parámetros;
- condiciones externas pertinentes.

Esquemáticamente:

$$
\boxed{
(s_0,\theta,\mathcal L)
\longrightarrow
s_1.
}
$$
En §3 vimos que una fotografía del péndulo puede mostrar la misma posición para dos estados dinámicamente diferentes.

Esto significa que una descripción insuficiente del presente puede producir ambigüedad futura.

Si dos estados

$$
s_a\neq s_b
$$

comparten la misma observación:

$$
O(s_a)=O(s_b),
$$

pero evolucionan de manera distinta:

$$
E(s_a)\neq E(s_b),
$$

entonces el dato observable actual no basta para una predicción única.

La dificultad no está en «resolver mal la ecuación».

Está en que no conocemos suficiente estado.
En §3 dejamos abierto un punto importante.

No toda teoría predice un único resultado.

Podemos encontrar:

##### Predicción determinista

$$
s_0
\longrightarrow
s_1.
$$

##### Predicción probabilística

$$
s_0
\longrightarrow
\{\text{probabilidades para resultados posibles}\}.
$$

Por tanto:

$$
\boxed{
\text{predecir}
\neq
\text{afirmar siempre un único valor futuro}.
}
$$

Más adelante desarrollaremos formalmente la probabilidad física.

Aquí solo preservamos una definición suficientemente general.
La palabra «nuevo» no significa siempre «futuro» ni garantiza el mismo nivel de riesgo. Una predicción dentro de la región ya contrastada y una extrapolación lejana son metodológicamente diferentes.

Usaremos informalmente:

- **interpolación**: predecir dentro de una región rodeada o cubierta por condiciones previamente observadas;
- **extrapolación**: extender la predicción más allá del dominio donde el modelo fue ajustado o contrastado.

No fijaremos todavía una definición matemática general.

Lo importante es:

$$
\boxed{
\text{dato nuevo}
\not\Rightarrow
\text{mismo nivel de riesgo}.
}
$$

Una extrapolación puede poner a prueba una estructura de manera particularmente fuerte, pero también puede simplemente abandonar el régimen de validez del modelo.

Por eso toda extrapolación exige revisar

$$
\mathcal R.
$$
### 8.2. Retrodicción

A veces conocemos información actual y queremos reconstruir un estado anterior.

La dirección de la pregunta cambia:

$$
\text{presente}
\longrightarrow
\text{pasado posible}.
$$

::: {.ma-block .ma-definicion #fpm-i-01-d24}
**Definición operativa FPM-I-01-D24 — Retrodicción**
Una **retrodicción** es una inferencia, realizada mediante un modelo, desde datos o estados posteriores hacia estados, condiciones o acontecimientos anteriores compatibles con ellos.
:::

No es simplemente «recordar el pasado».

Es usar una estructura física para reconstruirlo.
Supongamos que

$$
E:\mathcal S\to\mathcal S
$$

es una regla de evolución.

Dado un estado final

$$
s_1,
$$

queremos encontrar estados $s_0$ tales que

$$
E(s_0)=s_1.
$$

Puede ocurrir que exista:

- ningún estado previo compatible;
- un único estado previo;
- varios estados previos.

La retrodicción no es automáticamente única.
Sea

$$
\mathcal S=\{a,b,c\}
$$

y definamos:

$$
E(a)=c,
$$

$$
E(b)=c,
$$

$$
E(c)=b.
$$

Supongamos que observamos actualmente:

$$
s_1=c.
$$

¿Qué estados anteriores son compatibles?

Buscamos soluciones de:

$$
E(s_0)=c.
$$

Tenemos:

$$
E(a)=c
$$

y

$$
E(b)=c.
$$

Por tanto, el pasado compatible puede ser:

$$
s_0=a
$$

o

$$
s_0=b.
$$

La información actual no determina cuál ocurrió.

Así:

$$
\boxed{
\text{evolución bien definida hacia adelante}
\not\Rightarrow
\text{retrodicción única}.
}
$$
En la práctica quizá ni siquiera conozcamos el estado final completo.

Conocemos un dato:

$$
O(s_1)=d.
$$

Si el observable

$$
O:\mathcal S\to\mathcal V
$$

no es inyectivo, varios estados presentes pueden producir el mismo dato.

Entonces existen dos fuentes de ambigüedad:

1. varios estados presentes compatibles con el dato;
2. varios estados pasados compatibles con cada estado presente.
