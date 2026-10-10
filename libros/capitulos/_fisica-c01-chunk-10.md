::: {.ma-block .ma-metodo #fpm-i-01-mp09}
**Principio FPM-I-01-MP09 — Modelo mínimo suficiente**
Entre modelos que responden adecuadamente una pregunta con la precisión exigida, preferiremos inicialmente aquel que haga explícita la menor cantidad de estructura necesaria para comprender qué produce el resultado.
:::

No es una ley universal de la ciencia.

Es una estrategia pedagógica y metodológica.

Un modelo más rico se justifica cuando el modelo mínimo deja de responder la pregunta o cuando buscamos fenómenos nuevos.
### 4.18. Ejemplo desarrollado 9 — Clasificar una simplificación

Consideremos cuatro frases.

#### A
«No registraremos el color del proyectil.»

**Clasificación:** abstracción.

No se introduce la afirmación «el proyectil carece de color». El color queda fuera del lenguaje del modelo.

#### B
«El proyectil se tratará como una partícula puntual.»

**Clasificación:** idealización.

Se sustituye el cuerpo extendido por un objeto de extensión nula.

#### C
«La resistencia del aire se toma exactamente igual a cero.»

**Clasificación:** idealización de modelo.

#### D
«La resistencia del aire produce una corrección menor que la precisión que buscamos y por eso omitiremos su contribución.»

**Clasificación:** aproximación, siempre que exista una comparación que justifique la afirmación.

Las frases C y D pueden conducir a ecuaciones semejantes, pero su **estatus epistemológico** es diferente.
### 4.19. Ejemplo desarrollado 10 — El término cuadrático

Sea

$$
Q(\varepsilon)=1-2\varepsilon+\varepsilon^2.
$$
Queremos sustituirlo por

$$
Q_1(\varepsilon)=1-2\varepsilon.
$$
#### Paso 1 — Diferencia exacta

$$
Q(\varepsilon)-Q_1(\varepsilon)
=
\varepsilon^2.
$$
#### Paso 2 — Comparación con el término lineal

Para $\varepsilon\neq0$,

$$
\frac{|\varepsilon^2|}{|2\varepsilon|}
=
\frac{|\varepsilon|}{2}.
$$
#### Paso 3 — Casos

Si

$$
|\varepsilon|=10^{-2},
$$
entonces

$$
\frac{|\varepsilon^2|}{|2\varepsilon|}
=
5\times10^{-3}.
$$
Si

$$
|\varepsilon|=1,
$$
entonces

$$
\frac{|\varepsilon^2|}{|2\varepsilon|}
=
\frac12.
$$
La omisión que era pequeña en el primer caso ya no lo es en el segundo.

#### Conclusión

No existe «la aproximación» sin su régimen.
### 4.20. Ejercicios de §4


::: {.ma-block .ma-enunciado #fpm-i-01-e015}
**Ejercicio FPM-I-01-E015 — Idealización no es aproximación**

**Familia:** `E-CON / BASIC`

Clasifica cada operación como **abstracción**, **idealización** o **aproximación** y justifica.

a) No incluir el color de una esfera entre las variables del modelo.  
b) Tratar la esfera como partícula puntual.  
c) Reemplazar $1+\varepsilon+\varepsilon^2$ por $1+\varepsilon$ para $|\varepsilon|$ pequeño.  
d) Tratar una barra como perfectamente rígida.  
e) No distinguir químicamente dos cuerpos porque la pregunta solo utiliza su masa y posición.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

a) **Abstracción.** El color queda fuera de la descripción; no se afirma que sea cero o inexistente.

b) **Idealización.** Un cuerpo extendido se sustituye por un punto.

c) **Aproximación.** Se reemplaza una expresión por otra cercana bajo una condición de pequeñez.

d) **Idealización.** La rigidez perfecta se trata como exacta en el modelo aunque ningún material real la posea exactamente.

e) **Abstracción.** Se conserva solo la estructura relevante para la pregunta y se omite la composición química.

La clave es preguntar qué operación se realiza sobre la representación.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e016}
**Ejercicio FPM-I-01-E016 — Escalera del péndulo**

**Familia:** `E-LIM / CORE`

Ordena conceptualmente los siguientes pasos y clasifica cada uno:

1. cuerpo real + hilo real + aire + Tierra;
2. no registrar el color de la esfera;
3. representar la esfera como masa puntual;
4. tratar el hilo como inextensible y sin masa;
5. tomar la disipación exactamente nula;
6. más adelante, reemplazar una relación exacta por otra válida para pequeñas oscilaciones.

Explica qué información o efecto se pierde en cada paso.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

Un orden razonable es:

$$
1\to2\to3\to4\to5\to6.
$$
**1 → 2:** abstracción. Se elimina de la descripción una propiedad que no se considera relevante.

**2 → 3:** idealización. Se pierde tamaño, forma y estructura interna.

**3 → 4:** idealización. Se eliminan masa y extensibilidad del hilo.

**4 → 5:** idealización. El modelo declara exactamente ausente la disipación.

**5 → 6:** aproximación. Una relación del modelo se reemplaza por otra más simple dentro de un régimen que deberá justificarse.

El ejercicio muestra que varias simplificaciones pueden acumularse y que cada una tiene una justificación diferente.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e017}
**Ejercicio FPM-I-01-E017 — Más complicado no es siempre mejor**

**Familia:** `E-CON / ADVANCED`

Un equipo quiere estimar el tiempo aproximado que tarda una pelota en caer desde una altura moderada.

El **Modelo A** utiliza pocas propiedades macroscópicas.

El **Modelo B** añade cuarenta parámetros: composición microscópica, distribución térmica interna, rugosidad detallada, pequeñas vibraciones y muchas propiedades adicionales que el equipo no puede medir con precisión.

Explica por qué no se sigue que B sea mejor que A. Indica qué evidencia justificaría pasar de A a B o a un modelo intermedio.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

El número de detalles no establece por sí solo la calidad del modelo.

B puede resultar peor porque:

- contiene parámetros desconocidos;
- aumenta la incertidumbre de las entradas;
- dificulta identificar qué mecanismo controla el resultado;
- puede no mejorar la predicción a la escala requerida;
- puede ser imposible de contrastar con los datos disponibles.

A puede ser preferible si responde la pregunta dentro de la precisión necesaria.

Pasar a un modelo más rico se justificaría si observamos, por ejemplo:

1. discrepancias sistemáticas mayores que la precisión requerida;
2. dependencia del resultado respecto de una propiedad omitida;
3. un nuevo experimento que necesite explicar estructura que A no representa;
4. necesidad de mayor precisión.

El criterio es **suficiencia para la pregunta**, no cantidad de detalles.
:::

### 4.21. Síntesis

Ahora podemos distinguir tres maneras de simplificar.

$$
\boxed{
\text{abstracción}
=
\text{seleccionar estructura y omitir particulares}
}
$$
$$
\boxed{
\text{idealización}
=
\text{tratar como exacta una condición simplificada del modelo}
}
$$
$$
\boxed{
\text{aproximación}
=
\text{reemplazar por algo cercano en un régimen controlado}
}
$$
Y podemos asociar una pregunta de auditoría a cada una:

$$
\begin{array}{c|c}
\text{operación} & \text{pregunta}\\
\hline
\text{abstracción} & \text{¿qué información se omite?}\\
\text{idealización} & \text{¿qué se declara exacto solo en el modelo?}\\
\text{aproximación} & \text{¿qué error se acepta y en qué régimen?}
\end{array}
$$
La siguiente sección dará un paso más.

Hasta ahora hemos hablado de sistemas, estados, variables y simplificaciones.

Debemos reunir todo eso en una plantilla matemática suficientemente precisa para leer un modelo sin confundir el formalismo con su interpretación.

Entraremos entonces en:

$$
\boxed{
\text{§5 — De la representación física al objeto matemático}.
}
$$

---

## 5. De la representación física al objeto matemático {#fpm-i-01-s05}

### 5.1. El símbolo no trae consigo su significado físico

Supongamos que encontramos escrita la ecuación

$$
x^2+y^2=L^2.
$$

Como objeto matemático, podemos estudiarla sin saber nada de física. Podemos preguntar por sus soluciones, despejar una variable o reconocer una estructura geométrica.

Pero ninguna de esas operaciones nos dice por sí sola qué representan $x$, $y$ y $L$.

La misma ecuación podría aparecer para describir una restricción geométrica, una trayectoria idealizada, dos componentes de una cantidad, una relación entre magnitudes reescaladas o un problema puramente matemático sin interpretación física.

La sintaxis no determina la semántica.

$$
\boxed{
\text{expresión matemática}
+
\text{interpretación física}
=
\text{enunciado físico modelado}
}
$$

Este es el punto de partida de la sección.

Un matemático puede manipular correctamente una expresión y, sin embargo, no saber todavía qué pregunta física está respondiendo.

### 5.2. Dos tareas diferentes

Cuando construimos un modelo físico realizamos al menos dos tareas.

#### Tarea matemática

Elegimos objetos como conjuntos, números, funciones, relaciones, espacios, ecuaciones y parámetros.

#### Tarea física

Decidimos qué sistema representa cada objeto, qué magnitud corresponde a cada símbolo, qué procedimientos conectan ciertos símbolos con observaciones, qué hipótesis permiten usar esas relaciones y en qué régimen esperamos que el modelo sea adecuado.

Estas tareas se necesitan mutuamente, pero no son idénticas.

La matemática organiza la estructura. La física asigna significado y la conecta con el mundo.

::: {.ma-block .ma-metodo #fpm-i-01-mp10}
**Principio FPM-I-01-MP10 — Ningún símbolo físico se interpreta a sí mismo**
El significado físico de un objeto matemático debe declararse mediante el modelo, una definición, una regla de observación o una convención explícita; no puede deducirse únicamente de la forma del símbolo o de la ecuación en la que aparece.
:::

### 5.3. El diccionario de interpretación
