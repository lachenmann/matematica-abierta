Pero si preguntamos por:

- su rotación;
- su deformación;
- el momento en que una parte de su superficie toca otra superficie;
- su resistencia aerodinámica;

la extensión espacial deja de ser irrelevante.

La misma idealización puede pasar de buena a mala sin que el objeto físico haya cambiado.

Ha cambiado la **pregunta**.
### 4.6. Idealización y abstracción: diferencia mediante un mismo cuerpo

Tomemos una pelota real.

#### Abstracción

Decidimos no registrar su color.

La pelota del modelo todavía puede conservar tamaño, masa y forma.

No hemos afirmado:

$$
\text{color}=0.
$$
Simplemente no hay una variable «color» en nuestra descripción.

#### Idealización

Representamos la pelota como un punto.

Ahora introducimos una condición exacta del modelo:

$$
\text{extensión espacial}=0.
$$
Esta condición no describe literalmente la pelota.

Por tanto:

$$
\boxed{
\text{abstracción}=\text{no representar cierta información}
}
$$
mientras que

$$
\boxed{
\text{idealización}=\text{representar mediante una condición simplificada tratada como exacta}.
}
$$
La frontera entre ambas puede depender del formalismo, pero la distinción es metodológicamente útil.
### 4.7. Aproximación: reemplazar por algo cercano

Pasemos ahora a una operación diferente.

Supongamos que una relación exacta dentro de un modelo es

$$
Q=1-2\varepsilon+\varepsilon^2.
$$
Podemos decidir usar

$$
Q\approx 1-2\varepsilon
$$
cuando $\varepsilon$ es suficientemente pequeño para la precisión que buscamos.

Aquí no hemos cambiado necesariamente el objeto físico ni la frontera del sistema.

Hemos reemplazado una expresión por otra que esperamos que sea **cercana** en cierto régimen.

::: {.ma-block .ma-definicion #fpm-i-01-d15}
**Definición operativa FPM-I-01-D15 — Aproximación**
Una **aproximación** reemplaza una cantidad, relación o modelo por otro más simple cuya diferencia respecto del original se considera suficientemente pequeña para una pregunta y un régimen especificados.
:::

La palabra decisiva es **diferencia**.

Una aproximación exige, al menos conceptualmente, alguna manera de comparar.
### 4.8. Primera aproximación controlada sin cálculo

Consideremos la identidad exacta

$$
(1-\varepsilon)^2
=
1-2\varepsilon+\varepsilon^2.
$$
Supongamos que usamos

$$
(1-\varepsilon)^2
\approx
1-2\varepsilon.
$$
¿Qué hemos hecho?

El término omitido es exactamente

$$
\varepsilon^2.
$$
Por tanto, el error algebraico introducido por esta sustitución es

$$
E=\varepsilon^2.
$$
Si queremos comparar el término omitido con el término lineal $\varepsilon$, para $\varepsilon\neq0$,

$$
\frac{|\varepsilon^2|}{|\varepsilon|}
=
|\varepsilon|.
$$
Así, si

$$
|\varepsilon|=0.01,
$$
entonces

$$
\frac{|\varepsilon^2|}{|\varepsilon|}
=
0.01.
$$
El término cuadrático posee solo una centésima parte del tamaño de un término proporcional a $\varepsilon$.

No necesitamos todavía series de Taylor para comprender la idea.

::: {.ma-block .ma-metodo #fpm-i-01-mp08}
**Principio FPM-I-01-MP08 — Una aproximación debe hacer visible qué se omite**
Siempre que sea posible, registraremos la cantidad o término despreciado y explicaremos por qué es pequeño respecto de la escala relevante.
:::

### 4.9. «Pequeño» no es una propiedad absoluta

Supongamos que alguien afirma:

> «Un centímetro es pequeño.»

La frase está incompleta.

Un centímetro es pequeño comparado con el radio de la Tierra.

Puede ser enorme comparado con el grosor de una célula.

Puede ser decisivo en el ajuste de una pieza mecánica.

Por eso, la palabra **pequeño** necesita una comparación.

Sin desarrollar todavía análisis dimensional, podemos formular la regla conceptual:

$$
\boxed{
\text{pequeño}
=
\text{pequeño respecto de una escala relevante}.
}
$$
Del mismo modo, decir que «el aire tiene poco efecto» exige preguntar:

> ¿poco efecto sobre qué magnitud, durante qué intervalo y con qué precisión?
### 4.10. Aproximación no significa simplemente redondeo

Si

$$
\pi\approx3.14,
$$
hemos realizado una aproximación numérica.

Pero en física las aproximaciones importantes suelen ser estructurales.

Podemos:

- despreciar un término;
- reemplazar una geometría por otra;
- usar una ley límite;
- linealizar una relación;
- separar escalas;
- reemplazar una interacción compleja por una efectiva.

Algunas de estas operaciones se combinan con idealizaciones.

Por eso debemos registrar el nivel exacto en que ocurre la simplificación.
### 4.11. El péndulo: una escalera de operaciones distintas

Volvamos a nuestro caso conductor.

#### Paso 1 — No registrar el color del cuerpo

**Tipo:** abstracción.

El color queda fuera de las variables del modelo.

#### Paso 2 — Representar el cuerpo como masa puntual

**Tipo:** idealización.

La extensión espacial se hace exactamente nula dentro del modelo.

#### Paso 3 — Representar el hilo como inextensible y sin masa

**Tipo:** idealización.

No estamos diciendo que el hilo real tenga literalmente esas propiedades.

#### Paso 4 — Ignorar la resistencia del aire

Puede formularse de dos maneras distintas:

- como **idealización**, si el modelo declara exactamente nula la disipación;
- como **aproximación**, si partimos de un modelo con disipación y mostramos que su contribución es pequeña en cierto régimen.

La misma frase coloquial —«despreciamos el aire»— puede esconder operaciones conceptuales diferentes.

#### Paso 5 — Reemplazar una relación angular por una relación más simple para ángulos pequeños

**Tipo:** aproximación.

No la utilizaremos todavía. La estudiaremos de manera controlada en `FPM-I-06`.

Esta escalera muestra por qué no basta escribir «hacemos las aproximaciones usuales».
### 4.12. La etiqueta `[MOD]` y la etiqueta `[APPROX]`

El protocolo global de este libro distingue:

$$
[\mathrm{MOD}]
$$
para una hipótesis de modelización o idealización, y

$$
[\mathrm{APPROX}]
$$
para una aproximación.

Ejemplo:

::: {.ma-block .ma-dominio}
$$
[\mathrm{MOD}]
\qquad
\text{El hilo se considera inextensible.}
$$
:::
Esto define una propiedad exacta **del modelo**.

En cambio:

::: {.ma-block .ma-dominio}
$$
[\mathrm{APPROX}]
\qquad
1-2\varepsilon+\varepsilon^2
\approx
1-2\varepsilon
\quad\text{si }|\varepsilon|\text{ es suficientemente pequeño para la precisión requerida.}
$$
:::
Aquí existe una diferencia explícita entre dos expresiones.
### 4.13. Una aproximación debe tener régimen

La expresión

$$
1-2\varepsilon+\varepsilon^2
\approx
1-2\varepsilon
$$
no es una identidad.

Para

$$
\varepsilon=0.01
$$
el término omitido es

$$
10^{-4}.
$$
Para

$$
\varepsilon=1
$$
el término omitido es

$$
1.
$$
La misma sustitución puede ser excelente en un caso y desastrosa en otro.

Por eso toda aproximación física seria viene acompañada, explícita o implícitamente, por un **régimen de validez**.

::: {.ma-block .ma-definicion #fpm-i-01-d16}
**Definición operativa FPM-I-01-D16 — Régimen de validez de una aproximación**
El **régimen de validez** de una aproximación es el conjunto de condiciones bajo las cuales el error o los efectos omitidos permanecen suficientemente pequeños para el propósito declarado.
:::

Todavía no sabemos formular regímenes de manera sistemática.

Eso será tarea de `FPM-I-06`.
### 4.14. «Suficientemente pequeño» depende de la pregunta

Imaginemos dos usos de una misma predicción.

#### Uso A — Demostración de aula

Queremos distinguir si un tiempo es aproximadamente de uno o de diez segundos.

Un error de unas pocas centésimas puede ser irrelevante.

#### Uso B — Instrumento de precisión

Queremos detectar una variación relativa de una parte en cien mil.

El mismo error puede arruinar completamente el experimento.

Por tanto:

$$
\boxed{
\text{validez práctica}
=
\text{error}
+
\text{precisión requerida}
+
\text{pregunta}.
}
$$
No existe una tolerancia universal para todas las aplicaciones.
### 4.15. El peligro contrario: aproximar demasiado pronto

Las aproximaciones son útiles, pero pueden destruir precisamente el fenómeno que queremos estudiar.

Supongamos que dos términos pequeños casi se cancelan y el resultado observable depende de su diferencia.

Si eliminamos uno de ellos por considerarlo «pequeño» de manera aislada, podemos cambiar por completo la respuesta.

O supongamos que una cantidad pequeña actúa durante muchísimo tiempo y su efecto acumulado se vuelve importante.

Por tanto:

$$
\boxed{
\text{término pequeño}
\not\Rightarrow
\text{efecto siempre despreciable}.
}
$$
Necesitamos conocer cómo entra ese término en la estructura completa del problema.
### 4.16. Ejemplo: la rotación terrestre en un péndulo

Durante unas pocas oscilaciones ordinarias, ciertos efectos asociados con la rotación terrestre pueden resultar irrelevantes para una pregunta elemental sobre el período.

Pero si preguntamos por una modificación lenta del plano de oscilación durante muchas horas, precisamente esos efectos pueden convertirse en el fenómeno central.

Lo que parecía una corrección pequeña deja de ser despreciable porque:

1. cambia la pregunta;
2. cambia la escala temporal;
3. cambia la precisión buscada.

Esta observación preparará nuestros estudios de sistemas no inerciales mucho más adelante.
### 4.17. Modelo mínimo suficiente

Podemos formular una regla de trabajo:
