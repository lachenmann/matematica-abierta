## 13. Exactitud matemática y adecuación física {#fpm-i-01-s13}


### 13.1. Dos evaluaciones que no deben confundirse

A lo largo del capítulo hemos usado expresiones como:

- «resultado exacto»;
- «aproximación»;
- «modelo adecuado»;
- «predicción compatible con la observación».

Estas expresiones pertenecen a planos diferentes.

Cuando preguntamos:

> ¿La derivación es matemáticamente correcta?

examinamos la relación entre premisas y conclusión.

Cuando preguntamos:

> ¿El modelo describe adecuadamente el sistema físico?

examinamos la relación entre la representación y el mundo.

Por tanto:

$$
\boxed{
\text{exactitud matemática}
\neq
\text{adecuación física}.
}
$$

Esta es quizá la distinción más importante del capítulo completo.
Supongamos que hemos declarado un paquete de premisas:

$$
\Pi.
$$

Y demostramos rigurosamente:

$$
\Pi\to P.
$$

Si la demostración es válida, entonces $P$ es una consecuencia matemática exacta de $\Pi$.

Pero esto no establece todavía que:

$$
\Pi
$$

sea una descripción físicamente adecuada del sistema real.

La forma lógica es:

$$
\boxed{
\Pi\ \text{aceptada}
\Longrightarrow
P\ \text{exactamente derivada}.
}
$$

La palabra **exactamente** modifica aquí a la derivación, no al mundo.
::: {.ma-block .ma-definicion #fpm-i-01-d31}
**Definición operativa FPM-I-01-D31 — Exactitud matemática relativa al modelo**
Diremos que un resultado es **matemáticamente exacto respecto de un modelo** cuando se obtiene sin introducir nuevas aproximaciones matemáticas a partir de las definiciones, hipótesis y relaciones formales declaradas en ese modelo.
:::

Esta definición contiene dos restricciones.

Primera:

> **respecto de un modelo**.

Segunda:

> **sin introducir nuevas aproximaciones matemáticas**.

No afirmamos que el modelo mismo sea exacto como representación de la naturaleza.
::: {.ma-block .ma-definicion #fpm-i-01-d32}
**Definición operativa FPM-I-01-D32 — Adecuación física**
La **adecuación física** de un modelo es el grado en que sus representaciones, relaciones y predicciones conservan los rasgos relevantes del sistema real para una pregunta, un régimen y una precisión determinados.
:::

No la tratamos aquí como una cantidad numérica.

La definición es metodológica.

Obliga a declarar:

- **qué pregunta**;
- **qué régimen**;
- **qué precisión**;
- **qué rasgos son relevantes**.

Sin esos datos, la expresión «modelo correcto» es demasiado vaga.
El contraste puede resumirse así:

| Pregunta | Evaluación |
|---|---|
| ¿La conclusión se sigue de las premisas? | corrección o exactitud matemática relativa |
| ¿Las premisas representan adecuadamente el sistema? | adecuación física |
| ¿La solución satisface restricciones y condiciones? | admisibilidad física |
| ¿La diferencia prevista puede observarse? | accesibilidad observacional |

Imaginemos un sensor cuyo modelo ideal es:

$$
[\mathrm{MOD}]
\qquad
y=2x.
$$

Dentro del modelo, si:

$$
x=4,
$$

obtenemos exactamente:

$$
y=8.
$$

No hay error algebraico.

Ahora supongamos que el dispositivo real posee una limitación física:

> su salida no puede superar $10$.

Entonces, para:

$$
x=8,
$$

el modelo lineal produce exactamente:

$$
y=16.
$$

Pero el dispositivo real no puede entregar ese valor.

La conclusión:

$$
y=16
$$

es matemáticamente exacta **dentro del modelo lineal** y físicamente inadecuada **para el dispositivo real en ese régimen**.

No hay contradicción.

Las dos evaluaciones pertenecen a niveles diferentes.
Ante el ejemplo anterior sería incorrecto decir:

> «La cuenta $2\cdot8=16$ salió mal».

La cuenta es correcta.

El problema está en la premisa física:

$$
[\mathrm{MOD}]
\qquad
y=2x
$$

aplicada fuera del régimen donde representa adecuadamente al sensor.

Por tanto:

$$
\boxed{
\text{predicción físicamente mala}
\not\Rightarrow
\text{matemática incorrecta}.
}
$$

Este es exactamente el tipo de diagnóstico que §12 nos enseñó a realizar.
Un mapa puede ser excelente sin ser el territorio.

De manera análoga, un modelo físico no necesita reproducir todos los detalles del sistema.

La pregunta correcta no es:

> «¿Es idéntico al objeto real?»

Sino:

> «¿Conserva la estructura necesaria para responder la pregunta?»

Esto conecta:

$$
D32
$$

con:

$$
MP09,
\qquad
MP11,
\qquad
D29.
$$

Una descripción efectiva puede ser muy adecuada precisamente porque **no** intenta representar todo.
El matemático puede, por tanto, resolver perfectamente una pregunta mal formulada o un modelo innecesariamente detallado:

Spivak insiste, en su proyecto de física para matemáticos, en una dificultad característica: una vez reducida una situación física a una cuestión matemática, el matemático puede manejar con comodidad el formalismo; el trabajo específicamente físico está en construir correctamente esa reducción.[@spivak2010physics, prefacio, p. vii]

Podemos expresarlo así:

$$
\boxed{
\text{resolver exactamente una pregunta matemática}
\neq
\text{haber formulado la pregunta física correcta}.
}
$$

Esta no es una crítica a la matemática.

Es una advertencia sobre el paso:

$$
\text{fenómeno}
\longrightarrow
\text{modelo}.
$$
Supongamos que agregamos diez variables a un modelo.

¿Se volvió más exacto?

No necesariamente.

Tal vez las nuevas variables:

- no estén bien determinadas;
- representen efectos irrelevantes;
- introduzcan parámetros arbitrarios;
- dificulten la interpretación;
- no mejoren ninguna predicción.

La adecuación física no se mide por el número de componentes del formalismo.

Por eso:

$$
\boxed{
\text{más detalle}
\neq
\text{más adecuación automática}.
}
$$
