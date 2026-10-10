## 1. Una pregunta física no es todavía una ecuación {#fpm-i-01-s01}

### 1.1. El primer problema

Supongamos que frente a nosotros cuelga una pequeña esfera metálica de un hilo. La apartamos de la vertical y la soltamos. La esfera va hacia un lado, regresa, atraviesa la posición central, sube por el otro lado, vuelve otra vez y continúa oscilando.

La pregunta parece inmediata:

> **¿Cómo se mueve el péndulo?**

Para quien ya ha estudiado algo de física, la tentación es casi automática: buscar una fórmula conocida. Quizá recuerde una ecuación para el péndulo, una expresión para su período o una aproximación válida cuando el ángulo es pequeño. Pero en este libro queremos detenernos **antes** de ese paso.

La pregunta «¿cómo se mueve el péndulo?» todavía no es una pregunta matemática bien determinada. Ni siquiera es aún una pregunta física suficientemente precisa.

¿Qué llamamos *el péndulo*?

¿La esfera? ¿La esfera y el hilo? ¿Incluimos el soporte? ¿Incluimos la Tierra, cuya atracción influye en el movimiento? ¿Incluimos el aire, que frena lentamente la oscilación? ¿Incluimos la rotación terrestre? ¿La elasticidad del hilo? ¿La temperatura, que puede cambiar mínimamente sus dimensiones? ¿El aparato con que medimos? ¿La persona que lo soltó?

Y, aun si acordamos qué sistema estudiaremos, queda otra cuestión: ¿qué significa exactamente «cómo se mueve»?

Podríamos querer conocer:

- cuánto tarda en ir y volver;
- la posición de la esfera en distintos instantes;
- la amplitud de cada oscilación;
- cuánto disminuye esa amplitud con el tiempo;
- cómo cambia el comportamiento si modificamos la longitud del hilo;
- si dos péndulos aparentemente iguales se comportan de manera indistinguible;
- cuánto cambia el movimiento si lo llevamos a otro lugar de la Tierra;
- qué aspectos del movimiento permanecen iguales aunque cambiemos el tamaño del aparato.

Cada una de estas preguntas selecciona aspectos distintos del mismo objeto físico.

Este será nuestro punto de partida:

::: {.ma-block .ma-metodo #fpm-i-01-mp01}
**Principio FPM-I-01-MP01 — La modelización comienza antes de la primera fórmula**
Antes de escribir una ecuación física ya hemos tomado decisiones acerca de qué sistema consideramos, qué pregunta formulamos, qué propiedades describiremos y qué efectos trataremos como relevantes o irrelevantes.
:::

No se trata de una precaución filosófica externa a la física. Es una parte del trabajo físico mismo.
### 1.2. El objeto real contiene más física que nuestro primer modelo

Observemos con mayor cuidado el péndulo que tenemos delante.

La esfera no es un punto: posee radio, densidad, rugosidad y distribución de masa. El hilo tampoco es una línea geométrica: tiene masa, grosor, elasticidad y puede torcerse. El punto de suspensión puede ceder o vibrar. El aire ejerce fuerzas sobre el conjunto. La Tierra gira. El campo gravitatorio no es perfectamente uniforme. El laboratorio vibra. La esfera intercambia calor con el ambiente. El dispositivo utilizado para medir el tiempo tiene resolución finita.

Nada de eso es imaginario. Todos son aspectos físicos reales.

Sin embargo, si intentáramos incluir desde el comienzo todos los detalles que pudieran tener alguna influencia, probablemente no avanzaríamos. Un modelo físico no pretende copiar el mundo en miniatura. Su tarea es más selectiva:

$$
\boxed{\text{un modelo conserva ciertos rasgos del sistema y omite otros}}
$$
de acuerdo con una pregunta.

La palabra importante es **de acuerdo con una pregunta**.

La masa del hilo puede ser irrelevante si solo queremos una primera descripción aproximada de la oscilación de una esfera pesada sostenida por un hilo muy ligero. Pero esa misma masa puede ser decisiva si estudiamos vibraciones del hilo. La deformación del soporte puede ser despreciable en una experiencia de aula y esencial en un experimento de precisión. La resistencia del aire puede no importar durante dos oscilaciones y volverse evidente después de cientos.

No existen, por tanto, detalles «irrelevantes en sí mismos». Hay detalles irrelevantes **para una pregunta y dentro de una precisión determinada**.
### 1.3. Una escalera de representaciones

Podemos ordenar varias descripciones posibles del mismo dispositivo.

#### Nivel A — El péndulo real

Tenemos un cuerpo extendido suspendido de un hilo real, dentro de aire, unido a un soporte real, en un laboratorio situado sobre una Tierra real.

Esta descripción es físicamente rica, pero todavía demasiado abierta para calcular o predecir algo concreto.

#### Nivel B — Selección del sistema

Decidimos estudiar principalmente:

- el cuerpo suspendido;
- el hilo;
- la interacción con la Tierra.

Tratamos el resto como **entorno**.

Todavía no hemos convertido el sistema en un objeto matemático. Solo hemos trazado una primera frontera conceptual.

#### Nivel C — Idealización geométrica

Representamos la esfera por un punto y el hilo por un segmento de longitud fija.

Aquí ya hemos hecho dos operaciones fuertes:

1. ignoramos el tamaño y la forma del cuerpo;
2. ignoramos las deformaciones del hilo.

El objeto matemático que aparece no existe literalmente en el laboratorio. No hay masas puntuales ni segmentos materiales de grosor cero. Son **idealizaciones**.

#### Nivel D — Omisión de disipación

Decidimos ignorar, en una primera descripción, la pérdida de energía asociada al aire y a la fricción del soporte.

No estamos diciendo que esas pérdidas sean cero en el mundo. Estamos diciendo:

> «Para la pregunta actual, construiremos un modelo en el que no aparezcan.»

#### Nivel E — Modelo ulterior de pequeñas oscilaciones

En un capítulo posterior podremos hacer una aproximación adicional válida bajo condiciones específicas para simplificar todavía más el modelo.

Pero no debemos saltar a ella ahora. Primero tendremos que aprender qué significa justificar una aproximación y cómo se especifica su régimen de validez.

La secuencia conceptual es, por tanto,

$$
\text{objeto real}
\longrightarrow
\text{sistema seleccionado}
\longrightarrow
\text{idealización}
\longrightarrow
\text{modelo}
\longrightarrow
\text{aproximaciones adicionales}.
$$
No todos estos pasos son matemáticos. Algunos son decisiones físicas acerca de qué aspectos del mundo vamos a representar.
### 1.4. Primera distinción fundamental: sistema real y objeto matemático

Consideremos una esfera de acero que cuelga de un hilo.

La esfera que tocamos pertenece al mundo físico. Podemos pesarla, calentarla, rayarla o reemplazarla.

Un punto geométrico no tiene esas propiedades. Carece de volumen y de estructura interna. Sin embargo, para ciertas preguntas podemos representar la esfera mediante un punto cuya posición simboliza la posición del cuerpo.

Es importante no confundir ambas cosas.

::: {.ma-block .ma-definicion #fpm-i-01-d01}
**Definición operativa FPM-I-01-D01 — Sistema físico (primera formulación)**
Llamaremos **sistema físico** a la porción o colección de aspectos del mundo que elegimos como objeto principal de estudio para una pregunta determinada.
:::

La expresión «elegimos» es deliberada. La frontera de un sistema no siempre viene impuesta por la naturaleza.

::: {.ma-block .ma-definicion #fpm-i-01-d02}
**Definición operativa FPM-I-01-D02 — Representación matemática**
Una **representación matemática** asigna a aspectos seleccionados de un sistema físico objetos matemáticos —números, puntos, vectores, funciones, espacios, operadores, probabilidades u otras estructuras— junto con una interpretación que indica qué significan físicamente.
:::

La representación no es simplemente una traducción de palabras a símbolos. Implica una correspondencia.

Si escribimos un símbolo $x$, todavía no hemos hecho física. Necesitamos saber **qué representa $x$** y mediante qué procedimiento podría relacionarse con una observación.
### 1.5. El problema del mapa

Hay una manera útil de pensar la relación entre realidad y modelo.

Un mapa de una ciudad no reproduce la ciudad. No contiene los mismos edificios, personas, sonidos, temperaturas ni materiales. Contiene líneas, nombres, símbolos y escalas.

Un buen mapa omite casi todo.

Y precisamente por omitir casi todo puede ser útil.

Un plano del metro y un mapa topográfico del mismo territorio pueden ser excelentes aunque sean muy diferentes. El primero representa conexiones entre estaciones y simplifica distancias y direcciones; el segundo conserva información geométrica que el plano del metro descarta.

Preguntar cuál de los dos es «el mapa verdadero» sería formular mal la cuestión. Debemos preguntar:

> **¿verdadero o adecuado para qué tarea?**

Algo semejante ocurre con los modelos físicos.

La Tierra puede ser representada como:

- un plano, para ciertos problemas locales;
- una esfera, para una primera descripción global;
- un geoide, para geodesia;
- un cuerpo rígido en rotación, para ciertos problemas dinámicos;
- una masa puntual, para ciertas cuestiones orbitales;
- una distribución continua de materia, para estudiar su campo interior.

Ninguna de esas representaciones agota lo que la Tierra es.

El modelo adecuado depende de la pregunta, de la escala y de la precisión exigida.
### 1.6. ¿Podemos incluir todo?

Podría parecer que la solución más rigurosa consiste simplemente en introducir un modelo cada vez más detallado hasta incluir «todo lo importante».

Pero esta idea contiene varios problemas.

### 1.7. No sabemos de antemano qué es «todo lo importante»
