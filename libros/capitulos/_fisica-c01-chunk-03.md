::: {.ma-block .ma-comprobacion}
**Solución**

Una posible respuesta es:

**Pregunta A:** ¿cuánta agua contiene el vaso?

- incluir: volumen interior, nivel del agua;
- omitir inicialmente: viscosidad, rotación terrestre.

**Pregunta B:** ¿cómo oscila la superficie si movemos el vaso lateralmente?

- incluir: geometría del recipiente, movimiento del agua, gravedad;
- omitir inicialmente: evaporación, composición isotópica del agua.

**Pregunta C:** ¿cuánto tarda el agua caliente en enfriarse?

- incluir: temperatura, intercambio térmico con el ambiente, material del vaso;
- omitir inicialmente: movimiento de la Tierra alrededor del Sol, pequeñas irregularidades geométricas que no afecten apreciablemente al intercambio térmico.

La enseñanza no está en que estas elecciones sean únicas. Deben justificarse respecto de cada pregunta.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e002}
**Ejercicio FPM-I-01-E002 — Modelo más detallado**

Un estudiante afirma:

> «Entre dos modelos, siempre es físicamente mejor el que incluye más detalles.»

Explica por qué la afirmación es falsa. Da un ejemplo.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

Más detalle no garantiza mayor adecuación para una pregunta concreta. Un modelo puede introducir parámetros desconocidos, ocultar la estructura relevante o resolver con gran precisión efectos que son insignificantes frente a la precisión requerida.

Ejemplo: para estimar la distancia recorrida por una persona al caminar cien metros por una calle, un modelo que incorpore la curvatura del espacio-tiempo terrestre es muchísimo más detallado que un modelo euclídeo local, pero esa complejidad no mejora de manera útil la respuesta.

La comparación correcta no es «más detalles frente a menos detalles», sino:

$$
\text{adecuación para la pregunta y precisión buscada}.
$$
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e003}
**Ejercicio FPM-I-01-E003 — ¿Qué significa «sin rozamiento»?**

En un problema se dice que un bloque se mueve sobre una superficie «sin rozamiento».

¿Es esto una afirmación acerca de una superficie real o una hipótesis de modelo? Explica qué información adicional necesitaríamos para decidir si esa idealización es adecuada.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

«Sin rozamiento» funciona aquí como una **hipótesis de modelo**. No implica que exista una superficie material con rozamiento exactamente cero.

Para evaluar su adecuación necesitamos saber, entre otras cosas:

- qué magnitud queremos predecir;
- durante cuánto tiempo o distancia;
- qué precisión exigimos;
- qué tan pequeño es el efecto del rozamiento en comparación con los efectos conservados en el modelo.

La idealización puede ser excelente para una pregunta y mala para otra.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e004}
**Ejercicio FPM-I-01-E004 — Una fotografía no es una trayectoria**

Se toma una única fotografía de una pelota en el aire.

¿Basta esa imagen para responder «cómo se mueve la pelota»? Enumera información que falta.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

No. Una fotografía registra, como máximo, cierta información espacial en un instante y bajo una proyección particular.

Faltan, por ejemplo:

- una escala espacial;
- el instante o una referencia temporal;
- información sobre posiciones en otros instantes;
- información sobre profundidad si la imagen es bidimensional;
- identificación del sistema de referencia;
- procedimiento que conecte píxeles con posiciones físicas;
- datos sobre el entorno y el mecanismo que produjo el movimiento.

Incluso el significado de «posición» requiere una regla de reconstrucción a partir de la imagen.
:::

### 1.18. Cierre de la sección

Todavía no hemos escrito la ecuación de un péndulo.

Eso no significa que aún no hayamos hecho física.

Ya hemos aprendido que antes de una ecuación debemos:

- formular una pregunta;
- seleccionar un sistema;
- elegir qué propiedades representar;
- idealizar;
- registrar omisiones;
- decidir qué observaciones serían relevantes.

En la sección siguiente examinaremos precisamente el último punto.

¿Qué cuenta como observación física?

Ver que «el péndulo se mueve» no es lo mismo que producir un dato que pueda compararse con una predicción.

Pasaremos, por tanto, de

$$
\boxed{\text{¿qué queremos representar?}}
$$
a

$$
\boxed{\text{¿cómo se conecta esa representación con una observación?}}
$$

---

## 2. Fenómeno, observación y experimento {#fpm-i-01-s02}

### 2.1. Ver no es todavía medir

Volvamos al péndulo.

Lo apartamos y lo soltamos. Podemos decir:

> «Oscila.»

Esta frase registra algo real. Pero si queremos confrontar un modelo con el mundo necesitamos avanzar.

Podríamos preguntar:

- ¿cuánto dura una oscilación?;
- ¿hasta qué altura llega?;
- ¿la amplitud disminuye?;
- ¿dos oscilaciones sucesivas duran lo mismo?;
- ¿cambia el resultado si usamos otra esfera?;
- ¿cambia si repetimos el experimento mañana?

Responder estas preguntas exige algo más que mirar.

Debemos especificar **qué observaremos y cómo**.

Esta es la segunda idea rectora del capítulo:

::: {.ma-block .ma-metodo #fpm-i-01-mp03}
**Principio FPM-I-01-MP03 — Una observación física requiere una regla de conexión**
Para comparar una teoría o un modelo con el mundo necesitamos un procedimiento que conecte algún objeto de la representación matemática con un resultado observable.
:::

No basta con que aparezca un número en una ecuación. Debemos saber qué procedimiento físico produciría el número correspondiente.
### 2.2. Fenómeno

Usaremos la palabra **fenómeno** de manera amplia pero operativa.

::: {.ma-block .ma-definicion #fpm-i-01-d03}
**Definición operativa FPM-I-01-D03 — Fenómeno**
Un **fenómeno físico** es un proceso, comportamiento o regularidad del mundo físico que seleccionamos para describir, comparar, predecir o explicar.
:::

Ejemplos:

- la oscilación de un péndulo;
- la caída de un cuerpo;
- la expansión de un gas al calentarse;
- la desviación de la luz al atravesar ciertos medios;
- una corriente eléctrica;
- la interferencia de ondas;
- la desintegración de una partícula.

Un fenómeno no tiene por qué ser un «objeto». La oscilación no es la esfera; es un comportamiento del sistema.

Tampoco es necesario que sea un acontecimiento único. Podemos estudiar regularidades:

> cuerpos soltados de manera semejante muestran ciertos patrones de caída;

o transiciones:

> cierta sustancia cambia de fase bajo determinadas condiciones.

La selección del fenómeno ya contiene una pregunta implícita: de todo lo que ocurre, decidimos prestar atención a cierta estructura.
### 2.3. Observación

Consideremos dos afirmaciones:

1. «La esfera pasó por el centro.»
2. «La esfera cruzó la marca central cuando el reloj indicaba $12.4\ \mathrm{s}$.»

La segunda contiene una especificación mayor. Pero incluso ella deja preguntas:

- ¿qué marca se considera «el centro»?;
- ¿qué instante asociamos al cruce si la esfera tiene tamaño finito?;
- ¿qué reloj utilizamos?;
- ¿quién leyó el reloj?;
- ¿cómo se sincronizó el comienzo?;
- ¿qué resolución posee el aparato?

No resolveremos todavía todos estos problemas. El objetivo de `FPM-I-03` será precisamente desarrollar medición e incertidumbre.

Por ahora necesitamos una definición de trabajo.

::: {.ma-block .ma-definicion #fpm-i-01-d04}
**Definición operativa FPM-I-01-D04 — Observación**
Una **observación física** es un registro obtenido mediante un procedimiento especificado que asigna al sistema una descripción, clasificación o valor susceptible de comparación.
:::

La expresión **mediante un procedimiento especificado** es esencial.

Una observación física no es únicamente una sensación privada. Debe existir alguna regla suficientemente clara para que podamos preguntar si dos procedimientos registran lo mismo o si producen resultados comparables.
### 2.4. Del fenómeno al dato

Supongamos que queremos medir el tiempo de una oscilación.

Necesitamos definir al menos:

1. **evento inicial**;
2. **evento final**;
3. **procedimiento temporal**.

Por ejemplo:

- inicio: primer cruce de una marca central en una dirección determinada;
- final: siguiente cruce de la misma marca en la misma dirección;
- tiempo: diferencia entre dos lecturas de un reloj.

Esta descripción ya convierte una pregunta vaga en una operación más precisa.

Podemos simbolizar las lecturas como

$$
t_{\mathrm{i}},\qquad t_{\mathrm{f}},
$$
y definir

$$
T := t_{\mathrm{f}}-t_{\mathrm{i}}.
$$
Aquí debemos leer cuidadosamente el estatus de cada relación.

::: {.ma-block .ma-dominio}
$$
[\mathrm{DEF}]\qquad T:=t_{\mathrm{f}}-t_{\mathrm{i}}.
$$
Esta ecuación no es una ley de la naturaleza. Es una **definición** de la cantidad $T$ a partir de las lecturas especificadas.
:::

Aún no hemos afirmado que $T$ sea constante, que dependa de la longitud o que obedezca alguna ley.

Esto muestra por qué dos ecuaciones algebraicamente similares pueden tener papeles físicos muy distintos.
### 2.5. Observable y procedimiento

En física se habla con frecuencia de **observables**. La noción adquirirá significados técnicos diferentes en teorías posteriores, especialmente en mecánica cuántica.

Aquí necesitamos solamente una versión inicial.

::: {.ma-block .ma-definicion #fpm-i-01-d05}
**Definición operativa FPM-I-01-D05 — Observable**
Un **observable**, en este nivel, es una propiedad del sistema que el modelo conecta con un procedimiento de observación o medición.
:::

Ejemplos elementales pueden ser:
