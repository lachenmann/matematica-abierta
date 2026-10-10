$$
\boxed{
\text{favorecer }M_2\text{ frente a }M_1
\neq
\text{demostrar unicidad absoluta de }M_2.
}
$$
##### 8. Criterios adicionales

Entre otros, podríamos examinar:

- qué estructura física justifica cada relación;
- qué régimen de validez declara;
- cuántas hipótesis independientes requiere;
- si se integra con una teoría más amplia;
- si explica otros fenómenos;
- qué nuevas predicciones produce;
- si sus conclusiones son robustas;
- cómo se conecta cada variable con observaciones.

La selección no termina con un único dato.
:::

### 10.5. Síntesis

§9 estableció:

$$
\boxed{
\text{datos finitos}
\not\Rightarrow
\text{modelo único}.
}
$$

§10 añade:

$$
\boxed{
\text{no unicidad}
\longrightarrow
\text{comparación estructurada}
+
\text{nuevas pruebas}.
}
$$

Los criterios principales son:

- coherencia;
- adecuación al fenómeno;
- interpretación;
- régimen;
- economía;
- integración teórica;
- poder explicativo;
- robustez;
- fecundidad predictiva.

Pero ninguno reemplaza por sí solo al contraste.

La estrategia experimental más importante queda resumida por `MP17`:

$$
\boxed{
\text{si los modelos coinciden donde ya miramos,
buscar dónde predicen cosas distintas}.
}
$$

Esto nos conduce al siguiente problema.

Incluso después de elegir un modelo razonable debemos saber:

> ¿hasta dónde podemos confiar en él?

Ése será el objeto de:

$$
\boxed{
\text{§11 — Dominio de validez y teorías efectivas}.
}
$$

---

## 11. Dominio de validez y teorías efectivas {#fpm-i-01-s11}

### 11.1. Dominio matemático y dominio físico

Supongamos que un modelo contiene una relación matemática

$$
Y=f(X).
$$

La función puede estar perfectamente definida para muchos valores de $X$.

Puede incluso ocurrir que el problema matemático asociado tenga una solución exacta.

Pero de ahí no se sigue que la relación represente físicamente al sistema para todos esos valores.

Esta es una de las diferencias más importantes entre:

$$
\text{dominio matemático}
$$

y:

$$
\text{dominio físico de aplicación}.
$$

Una expresión puede tener sentido matemático donde el modelo ya no tiene sentido físico.

Por tanto:

$$
\boxed{
\text{estar definido matemáticamente}
\neq
\text{ser físicamente válido}.
}
$$
Desde §5 hemos escrito el modelo como:

$$
\mathcal M
=
(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R),
$$

acompañado de:

$$
\mathfrak I_{\mathcal M}.
$$

Hasta ahora $\mathcal R$ aparecía como uno de los componentes de la ficha.

A partir de esta sección debemos leerlo como una restricción activa.

No basta preguntar:

> «¿Qué predice el modelo?»

Debemos preguntar:

> «¿Bajo qué condiciones afirma poder predecirlo?»

Así, una predicción físicamente completa tiene la forma conceptual:

$$
\boxed{
\text{modelo}
+
\text{condición perteneciente a }\mathcal R
\longrightarrow
\text{predicción físicamente interpretable}.
}
$$
::: {.ma-block .ma-definicion #fpm-i-01-d28}
**Definición operativa FPM-I-01-D28 — Dominio de validez físico**
El **dominio de validez físico** de un modelo, una aproximación o una teoría aplicada es el conjunto de condiciones, escalas, clases de sistemas y preguntas para las cuales se considera que sus representaciones y predicciones alcanzan la adecuación requerida.
:::

Esta definición contiene una palabra importante:

> **requerida**.

Un modelo puede ser adecuado para una precisión y no para otra.

Puede ser adecuado para una pregunta cualitativa y no para una medición extremadamente precisa.

Puede describir bien una escala y omitir fenómenos decisivos en otra.

Por eso el dominio de validez no es una etiqueta binaria del tipo:

$$
\text{verdadero/falso}.
$$

Es una declaración de alcance.
Supongamos:

$$
f:\mathbb R\to\mathbb R.
$$

Matemáticamente podemos evaluar:

$$
f(x)
$$

para cualquier:

$$
x\in\mathbb R.
$$

Pero el modelo físico podría haber sido construido solo para:

$$
x\in\mathcal R.
$$

Entonces:

$$
x_\ast\notin\mathcal R
$$

no impide necesariamente calcular:

$$
f(x_\ast).
$$

Lo que impide es interpretar automáticamente ese cálculo como una predicción confiable del sistema real.

Así:

$$
\boxed{
x_\ast\in\operatorname{Dom}(f)
\not\Rightarrow
x_\ast\in\mathcal R.
}
$$

Esta distinción aparecerá una y otra vez en el resto del libro.
Supongamos una cadena:

$$
[\mathrm{MOD}]
\longrightarrow
[\mathrm{APPROX}]
\longrightarrow
[\mathrm{MATH}]
\longrightarrow
P.
$$

Si la aproximación fue declarada válida solo en cierto régimen:

$$
\mathcal R,
$$

entonces la predicción $P$ no queda mágicamente liberada de esa restricción porque la derivación matemática sea exacta.

::: {.ma-block .ma-metodo #fpm-i-01-mp18}
**Principio FPM-I-01-MP18 — Toda predicción hereda el régimen del modelo**
Una consecuencia matemática derivada de un modelo conserva las restricciones físicas, idealizaciones y aproximaciones de las premisas que la producen. La exactitud de la derivación no amplía por sí sola el dominio de validez físico.
:::

En símbolos:

$$
\boxed{
[\mathrm{MATH}]\ \text{exacto}
+
[\mathrm{MOD}]/[\mathrm{APPROX}]\ \text{restringidos}
\not\Rightarrow
\text{validez física universal}.
}
$$
Imaginemos una aproximación sencilla válida cuando una cantidad adimensional $\varepsilon$ es pequeña:

$$
Q_{\mathrm{aprox}}
=
Q_0(1-\varepsilon).
$$

Supongamos que el modelo declara como régimen:

$$
0\le\varepsilon\le0.05.
$$

Matemáticamente podemos sustituir:

$$
\varepsilon=0.8.
$$

Obtendremos un número perfectamente definido.

Pero el modelo nunca afirmó que la aproximación fuera adecuada allí.

Por tanto:

$$
Q_{\mathrm{aprox}}(0.8)
$$

es un valor matemático de la fórmula, no automáticamente una predicción física autorizada.

La pregunta correcta es:

> ¿Qué control justificaba despreciar los términos omitidos y sigue funcionando para $\varepsilon=0.8$?
No siempre existe una frontera brusca:

$$
\mathcal R
=
\{x:x<x_c\}
$$

donde todo funciona perfectamente a un lado y deja de funcionar de golpe al otro.

Muchas aproximaciones se degradan progresivamente.

Podemos imaginar:

$$
\text{error pequeño}
\longrightarrow
\text{error apreciable}
\longrightarrow
\text{modelo inadecuado}.
$$

Esto significa que el dominio de validez puede depender de la precisión exigida.

Para una tarea basta quizá un error del:

$$
5\%.
$$

Para otra, incluso:

$$
0.1\%
$$

puede ser demasiado.

Por eso el dominio físico debe leerse junto con el objetivo.
Feynman utiliza un ejemplo conceptualmente importante: a velocidades ordinarias puede tratarse la masa como constante con precisión extraordinaria, mientras que a velocidades suficientemente altas esa aproximación deja de ser adecuada.[@feynman2011lectures1, vol. I, cap. 1, §1-1, pp. 1-1–1-2]

La lección que tomaremos no es la teoría relativista —que estudiaremos mucho después—, sino la estructura metodológica:

$$
\boxed{
\text{una relación puede ser excelente en un régimen
y equivocada fuera de él}.
}
$$

Eso no convierte en inútil la relación aproximada.

La convierte en una herramienta con dominio declarado.
### 11.2. Descripciones efectivas

Una descripción puede ser excelente dentro de un régimen sin pretender ser fundamental ni universal.

Supongamos que una teoría $T_2$ describe un dominio más amplio que una teoría anterior $T_1$.

Sería tentador concluir:

> «Entonces debemos dejar de usar $T_1$.»

Pero no se sigue.

Dentro del régimen donde $T_1$ funciona con la precisión requerida, puede tener ventajas decisivas:

- variables más simples;
- cálculos más cortos;
- interpretación más transparente;
- datos más fáciles de obtener;
- suficiente precisión para la tarea.

Por tanto:

$$
\boxed{
\text{teoría más amplia}
\not\Rightarrow
\text{teoría anterior inútil}.
}
$$
::: {.ma-block .ma-definicion #fpm-i-01-d29}
**Definición operativa FPM-I-01-D29 — Descripción efectiva**
Llamaremos **descripción efectiva** a un modelo o marco físico que retiene las variables, estructuras y relaciones relevantes para un régimen determinado y omite, promedia o sustituye detalles cuya influencia no es necesaria para responder las preguntas planteadas con la precisión requerida.
:::

La palabra «efectiva» no significa:

> «falsa».

Significa:

> «construida para capturar eficazmente cierta física a cierta escala o bajo ciertas condiciones».

En física avanzada, la expresión **teoría efectiva** adquirirá usos técnicos más específicos.

Aquí fijamos solamente esta noción operativa.
Sin desarrollar todavía sus teorías, podemos anticipar varios casos.

#### Un cuerpo como partícula puntual

La extensión interna del objeto se omite cuando no afecta a la pregunta.

#### Un fluido como medio continuo

La estructura molecular puede quedar fuera de la descripción cuando interesan variables macroscópicas.

#### La óptica de rayos

Una descripción mediante rayos puede ser extraordinariamente útil cuando la estructura ondulatoria relevante no se resuelve en la pregunta.

#### Mecánica clásica a velocidades ordinarias

Puede proporcionar predicciones excelentes sin incorporar toda la estructura relativista.

En cada caso:

$$
\boxed{
\text{omitir detalle}
\neq
\text{ignorar arbitrariamente}.
}
$$

La omisión debe estar justificada por el régimen.
Una teoría más amplia también puede cambiar la interpretación que hacemos de una descripción anterior, sin volverla inútil dentro del régimen donde funcionaba:

Feynman subraya una sutileza profunda.[@feynman2011lectures1, vol. I, cap. 1, §1-1, p. 1-2]

Una corrección puede ser numéricamente pequeña y, sin embargo, obligarnos a cambiar de manera importante nuestra imagen conceptual.
