1. utilizar el mismo hilo y soporte;
2. preparar varias esferas de geometría exterior lo más semejante posible pero masas distintas;
3. fijar un procedimiento de liberación;
4. definir una oscilación mediante eventos reproducibles;
5. utilizar el mismo método temporal;
6. medir varias veces para cada esfera;
7. alternar el orden de las mediciones para reducir efectos de deriva temporal;
8. comparar los resultados.

Todavía no podemos decidir aquí qué diferencia cuenta como «apreciable» en sentido metrológico riguroso; eso requerirá incertidumbre y escalas.
:::

### 2.24. Síntesis de §1–§2

Ya podemos describir una primera parte del trabajo físico.

Comenzamos con un fenómeno:

$$
\text{péndulo oscilando}.
$$
Formulamos una pregunta:

$$
\text{¿qué aspecto queremos explicar o predecir?}
$$
Seleccionamos un sistema:

$$
\text{¿qué incluimos y qué tratamos como entorno?}
$$
Construimos una representación:

$$
\text{¿qué objetos matemáticos simbolizarán propiedades físicas?}
$$
Definimos observaciones:

$$
\text{¿mediante qué procedimiento obtenemos datos comparables?}
$$
Y diseñamos experimentos:

$$
\text{¿qué debemos controlar o variar para obtener información discriminante?}
$$
La cadena que empieza a formarse es

$$
\boxed{
\text{fenómeno}
\to
\text{pregunta}
\to
\text{sistema}
\to
\text{representación}
\leftrightarrow
\text{observación}
\to
\text{experimento}
}.
$$
Todavía falta algo decisivo.

¿Qué partes del sistema quedan dentro y cuáles fuera?

¿Cómo distinguimos **estado**, **parámetro** y **observable**?

Ése será el objeto de la sección siguiente:

$$
\boxed{\text{§3 — Sistema, entorno, estado y observables}.}
$$

---

## 3. Sistema, entorno, estado y observables {#fpm-i-01-s03}

### 3.1. Elegir el sistema es trazar una frontera

En las dos secciones anteriores hemos usado varias veces la palabra **sistema**. Ahora necesitamos precisar qué trabajo realiza ese concepto.

Volvamos al péndulo.

Frente a nosotros hay una esfera, un hilo, un soporte, aire, una mesa, un edificio y la Tierra. Todo ello forma parte de una única realidad física continua. Sin embargo, para construir un problema no intentamos describir simultáneamente el universo completo. Seleccionamos una parte.

Podemos decidir, por ejemplo, que nuestro sistema sea:

1. solo la esfera;
2. esfera + hilo;
3. esfera + hilo + soporte;
4. esfera + hilo + Tierra;
5. esfera + hilo + aire + Tierra.

Cada elección produce una frontera distinta entre aquello que describiremos **dentro** del modelo y aquello que trataremos como **entorno**.

::: {.ma-block .ma-definicion #fpm-i-01-d07}
**Definición operativa FPM-I-01-D07 — Sistema físico (formulación refinada)**
Para una pregunta dada, llamaremos **sistema físico** al conjunto de objetos, componentes o procesos que elegimos describir explícitamente como objeto principal del modelo.

[!definicion] **Definición operativa FPM-I-01-D08 — Entorno**
Llamaremos **entorno** a aquello que queda fuera de la frontera elegida del sistema pero que puede influir en él, recibir influencia de él o ser relevante para interpretar las observaciones.
:::

La frontera puede coincidir con una superficie material, pero no tiene por qué hacerlo.

Si estudiamos la temperatura de una taza de café, podríamos tomar como sistema:

- solo el líquido;
- líquido + taza;
- líquido + taza + una capa de aire circundante.

La frontera del sistema es, en primer lugar, una **decisión de modelización**.
### 3.2. La frontera no separa «lo real» de «lo irreal»

Cuando dejamos el aire fuera del sistema del péndulo, el aire no deja de existir.

Cuando modelamos la Tierra como parte del entorno, la gravedad no desaparece.

Esto parece obvio, pero evita un error frecuente: interpretar la frontera del modelo como una frontera ontológica.

El esquema correcto es:

$$
\boxed{
\text{fuera del sistema}
\not\Rightarrow
\text{sin efecto}
}
$$
Un efecto externo puede aparecer en el modelo mediante una cantidad prescrita, una condición o una interacción efectiva, aun cuando el mecanismo que la produce no sea descrito en detalle.

Más adelante, por ejemplo, podremos representar la influencia de un entorno mediante campos externos, fuerzas externas, condiciones de frontera, fuentes o depósitos. Todavía no necesitamos ese formalismo.

Por ahora basta distinguir dos operaciones:

- **incluir** un componente significa modelar explícitamente parte de su estado o dinámica;
- **externalizar** un componente significa no seguir todos sus detalles internos, aunque podamos representar algunos de sus efectos.
### 3.3. Tres fronteras para el mismo péndulo

Consideremos tres elecciones.

#### Modelo A — La esfera como sistema

El hilo, el soporte, el aire y la Tierra pertenecen al entorno.

Este modelo puede ser útil si nuestro interés está concentrado en la trayectoria de la esfera y representamos los demás efectos de forma externa.

#### Modelo B — Esfera + hilo como sistema

Ahora la tensión, deformación o movimiento del hilo pueden convertirse en parte explícita de la descripción.

#### Modelo C — Esfera + hilo + Tierra como sistema

Esta elección puede ser útil si nos interesa contabilizar intercambios internos entre el cuerpo suspendido y la Tierra en una descripción más global.

Las tres fronteras son legítimas.

No existe una regla general según la cual «el sistema más grande sea el más correcto».

::: {.ma-block .ma-metodo #fpm-i-01-mp05}
**Principio FPM-I-01-MP05 — La frontera del sistema se elige para la pregunta**
Una buena frontera incluye la estructura necesaria para responder la pregunta sin obligarnos a modelar detalles que no aportan información relevante en el régimen considerado.
:::

Esta es una forma temprana del principio de **modelo mínimo suficiente** que usaremos repetidamente.
### 3.4. ¿Qué significa conocer el estado de un sistema?

Supongamos que vemos un péndulo en una fotografía.

La esfera aparece a la derecha de la vertical.

¿Sabemos cómo continuará el movimiento?

No necesariamente.

Podría estar moviéndose hacia la derecha y acercándose a su punto de retorno. O podría estar moviéndose hacia la izquierda después de haberlo alcanzado.

La misma posición visible puede corresponder a evoluciones posteriores diferentes.

La lección es fundamental:

$$
\boxed{
\text{describir dónde está algo}
\neq
\text{describir completamente su estado}
}
$$
En mecánica elemental aprenderemos que cierta información adicional —por ejemplo, información asociada al movimiento— resulta necesaria.

Pero queremos formular ahora una noción suficientemente general para que sobreviva a teorías posteriores.

::: {.ma-block .ma-definicion #fpm-i-01-d09}
**Definición operativa FPM-I-01-D09 — Estado**
Dado un modelo físico, un **estado** es una especificación matemática de la condición del sistema que contiene la información que ese modelo considera suficiente para formular sus predicciones, una vez fijados los parámetros, las leyes y las influencias externas pertinentes.
:::

Hay dos palabras que no debemos omitir:

$$
\boxed{\text{dado un modelo}}
$$
La noción de estado no se define independientemente de la teoría.
### 3.5. El estado es relativo al nivel de descripción

Consideremos un gas dentro de un recipiente.

Podríamos construir una descripción microscópica en la que intentamos seguir una enorme cantidad de información sobre sus constituyentes.

También podemos construir una descripción macroscópica mediante unas pocas magnitudes globales.

Ambas pueden hablar de «estado», pero no contienen la misma información.

Más adelante distinguiremos con precisión **microestado** y **macroestado**. Aquí basta extraer la regla:

$$
\boxed{
\text{qué cuenta como estado depende de qué estructura conserva el modelo}
}
$$
Lo mismo ocurre con un cuerpo extenso.

En un modelo de partícula puntual, su orientación puede no formar parte del estado.

En un modelo de cuerpo rígido, la orientación puede ser esencial.

En un modelo que además permite deformaciones, necesitaremos todavía más información.

Por tanto, preguntar simplemente «¿cuál es el estado real del objeto?» sin especificar una teoría o nivel de descripción puede ser demasiado ambiguo para nuestro propósito.
### 3.6. Espacio de estados: primera aparición

El lector matemático reconocerá inmediatamente una estructura útil.

Si llamamos $\mathcal S$ al conjunto de todos los estados admitidos por un modelo, podemos escribir

$$
s\in\mathcal S.
$$
::: {.ma-block .ma-definicion #fpm-i-01-d10}
**Definición operativa FPM-I-01-D10 — Espacio de estados**
El **espacio de estados** de un modelo es el conjunto —dotado más adelante de la estructura matemática que corresponda— cuyos elementos representan los estados admitidos por ese modelo.
:::

Por ahora, la palabra «espacio» no presupone topología, métrica, estructura vectorial ni variedad diferenciable.

Solo estamos diciendo:

$$
\mathcal S=\{\text{estados permitidos por el modelo}\}.
$$
En capítulos posteriores veremos ejemplos muy distintos:

- espacios de configuraciones;
- espacios de fases;
- espacios de estados termodinámicos;
- espacios de Hilbert.

No debemos confundirlos de antemano.
### 3.7. Variable: una palabra demasiado amplia

En física usamos constantemente la palabra **variable**.

Puede referirse a:

- una coordenada que cambia con el estado;
- una magnitud que registramos;
- una cantidad que controlamos experimentalmente;
- un parámetro que variamos de un experimento a otro;
- incluso una variable matemática auxiliar.

Por eso necesitamos distinguir funciones.
