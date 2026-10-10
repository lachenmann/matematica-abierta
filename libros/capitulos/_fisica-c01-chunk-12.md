Supongamos que queremos predecir la evolución de un sistema y conocemos su espacio de estados y parámetros, pero no hemos declarado ninguna ley dinámica.

Entonces el modelo está incompleto para esa pregunta.

De manera semejante, una ecuación dinámica puede estar especificada pero las condiciones iniciales necesarias pueden faltar.

::: {.ma-block .ma-metodo #fpm-i-01-mp11}
**Principio FPM-I-01-MP11 — La suficiencia de un modelo depende de la tarea**
Un conjunto de objetos matemáticos constituye una descripción suficiente solo si contiene la información necesaria para responder la pregunta física planteada; que una fórmula sea correcta no implica que el problema esté completamente especificado.
:::

### 5.17. Ejemplo desarrollado 11 — Un sistema físico de dos estados

Construyamos un modelo deliberadamente sencillo.

Tenemos un dispositivo idealizado que puede estar en dos configuraciones distinguibles:

$$
\text{cerrado},\qquad \text{abierto}.
$$

Representamos los estados mediante

$$
\mathcal S=\{0,1\},
$$

con el diccionario

$$
0\longleftrightarrow\text{cerrado},
\qquad
1\longleftrightarrow\text{abierto}.
$$

Definimos un observable

$$
O:\mathcal S\to\{0,1\},
\qquad
O(s)=s.
$$

La fórmula es trivial.

La física no está en la dificultad algebraica. Está en declarar qué diferencia física corresponde a $0$ y $1$, cómo determinamos experimentalmente si el dispositivo está abierto o cerrado, qué estados intermedios hemos excluido por idealización y para qué pregunta esa idealización es adecuada.

La estructura

$$
\{0,1\}
$$

puede modelar innumerables sistemas distintos.

El conjunto por sí solo no especifica cuál.

### 5.18. Ejemplo desarrollado 12 — Esqueleto del modelo del péndulo

Volvamos al péndulo, pero sin escribir todavía su ecuación de movimiento.

Podemos preparar una ficha.

#### Sistema físico

Una pequeña esfera suspendida mediante un hilo.

#### $\mathcal S$

Estados admitidos por la idealización elegida.

No los parametrizaremos técnicamente todavía.

#### $X$

Cantidades que deseamos representar, por ejemplo la posición angular, información sobre el movimiento y el tiempo de oscilación como observable derivado.

Las definiciones precisas se darán en capítulos posteriores.

#### $\theta$

Parámetros como la longitud del hilo y otras propiedades que el modelo trate como fijas.

#### $\mathcal L$

Todavía no especificado.

La ley dinámica aparecerá después de desarrollar la mecánica necesaria.

#### $I$

Condición inicial: cómo se prepara el péndulo al comenzar el experimento.

#### $B$

No necesitamos aquí una condición de frontera espacial independiente.

#### $\mathcal R$

Régimen en el cual las idealizaciones adoptadas sean adecuadas.

#### $\mathfrak I_{\mathcal M}$

Reglas que explican qué representa la posición angular, cómo se identifica experimentalmente una oscilación y cómo se mide el tiempo correspondiente.

La ficha es útil precisamente porque muestra qué sabemos y qué **todavía falta**.

### 5.19. Ejemplo desarrollado 13 — Una ecuación, dos modelos

Consideremos

$$
x+y=1.
$$

#### Modelo A — Dos fracciones de composición

Interpretamos

$$
x=\text{fracción del componente A},
$$

$$
y=\text{fracción del componente B}.
$$

La ecuación expresa que el modelo solo admite esos dos componentes y que las fracciones están normalizadas.

#### Modelo B — Distribución idealizada de un recurso

Interpretamos

$$
x=\text{fracción asignada al subsistema 1},
$$

$$
y=\text{fracción asignada al subsistema 2}.
$$

La misma ecuación posee otra semántica.

Matemáticamente,

$$
x+y=1
$$

es idéntica.

Físicamente, los modelos son diferentes porque cambia

$$
\mathfrak I_{\mathcal M}.
$$

Por tanto,

$$
\boxed{
\text{misma estructura matemática}
\not\Rightarrow
\text{mismo modelo físico}.
}
$$

### 5.20. Ejercicio de §5


::: {.ma-block .ma-enunciado #fpm-i-01-e018}
**Ejercicio FPM-I-01-E018 — Construir la ficha matemática mínima de un modelo**

**Familia:** `E-MOD / ADVANCED`

Considera un depósito idealizado que solo puede registrarse como **vacío** o **lleno** mediante un sensor binario.

Construye una ficha mínima utilizando

$$
\mathcal M=(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R)
$$

y un diccionario $\mathfrak I_{\mathcal M}$.

No es necesario inventar una ley dinámica si la pregunta solo es:

> «¿Qué estado registra el sensor en el instante de observación?»

Explica también qué información física real elimina este modelo.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

Una ficha posible es la siguiente.

#### Sistema físico

El depósito y el mecanismo relevante para decidir si el sensor lo clasifica como vacío o lleno.

#### Pregunta

Determinar cuál de los dos estados registra el sensor.

#### Espacio de estados

$$
\mathcal S=\{0,1\}.
$$

#### Diccionario de estados

$$
0\longleftrightarrow \text{vacío según el criterio del sensor},
$$

$$
1\longleftrightarrow \text{lleno según el criterio del sensor}.
$$

Es importante añadir «según el criterio del sensor»: un depósito real puede contener cantidades intermedias.

#### Variables/observables

Podemos tomar

$$
X=\{O\},
$$

con

$$
O:\mathcal S\to\{0,1\},
\qquad
O(s)=s.
$$

#### Parámetros

Si el sensor utiliza un umbral fijo para decidir la clasificación, ese umbral puede formar parte de

$$
\theta.
$$

No necesitamos asignarle un valor numérico concreto.

#### Leyes o relaciones

Para la pregunta instantánea no necesitamos especificar una ley dinámica.

Por tanto, $\mathcal L$ puede quedar sin componente dinámico relevante para esta tarea.

Esto no significa que el depósito real carezca de dinámica.

#### Condición inicial

No es necesaria si solo preguntamos por el estado registrado en el instante actual.

#### Condiciones de frontera

No se requieren para este modelo binario elemental.

#### Régimen de validez

El modelo sirve únicamente para preguntas cuya respuesta dependa de la clasificación binaria y no de la cantidad exacta de contenido.

#### Diccionario de interpretación

$\mathfrak I_{\mathcal M}$ debe incluir qué significa «vacío», qué significa «lleno», cómo funciona la regla de clasificación del sensor y qué señal corresponde a $0$ y cuál a $1$.

#### Información omitida

El modelo elimina, entre otras cosas, todos los niveles intermedios, la forma de la superficie del contenido, temperatura, presión, composición y la dinámica de llenado o vaciado.

La conclusión metodológica es importante:

$$
\boxed{
\text{un modelo puede ser suficiente para una pregunta aunque omita casi toda la física del sistema}.
}
$$

La suficiencia depende de la tarea.

:::

### 5.21. Síntesis

Ya podemos distinguir cuatro niveles:

$$
\boxed{\text{sistema físico}}
$$

$$
\boxed{
\text{núcleo formal }
\mathcal M
=
(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R)
}
$$

$$
\boxed{
\text{diccionario de interpretación }
\mathfrak I_{\mathcal M}
}
$$

$$
\boxed{\text{observaciones y contraste}}
$$

La tupla organiza la matemática.

El diccionario explica qué significa físicamente.

Las reglas `[OBS]` conectan parte de ese significado con procedimientos de observación.

El régimen $\mathcal R$ recuerda que la representación no reclama validez ilimitada.

Por tanto, la fórmula central de esta sección no debe leerse como una axiomatización de la física, sino como una disciplina de lectura:

$$
\boxed{
\text{no preguntes solo «¿qué ecuación tengo?»; pregunta «¿qué modelo está representando esta ecuación?»}
}
$$

Ahora podemos abordar el problema que hemos aplazado deliberadamente.

Dentro de $\mathcal L$ aparecen ecuaciones de tipos muy diferentes. Algunas definen. Algunas resumen regularidades empíricas. Algunas expresan postulados. Algunas son hipótesis del modelo. Algunas son aproximaciones. Y otras se deducen matemáticamente.

La forma algebraica no permite distinguirlas.

Este será el objeto de:

$$
\boxed{\text{§6 — El estatus de una ecuación}.}
$$

---

## 6. El estatus de una ecuación {#fpm-i-01-s06}

### 6.1. La misma fórmula puede cumplir funciones distintas

Consideremos la fórmula

$$
y=kx.
$$
Aislada en una página, es solo una relación matemática entre símbolos.

Pero dentro de distintos contextos puede desempeñar papeles muy diferentes.

#### Contexto A — Definición

Podemos decidir definir una nueva cantidad $y$ mediante

$$
y:=kx.
$$
Entonces la relación fija el significado de $y$.

Su estatus es:

$$
[\mathrm{DEF}].
$$
#### Contexto B — Regularidad empírica

Podemos medir dos magnitudes $x$ e $y$ y descubrir que, dentro de cierto intervalo experimental,

$$
y\approx kx.
$$
Ahora la relación resume un patrón observado.

Su respaldo depende de datos.

Su estatus puede ser:

$$
[\mathrm{EMP}].
$$
#### Contexto C — Hipótesis de modelo

Podemos construir deliberadamente un modelo en el que supongamos que dos cantidades obedecen exactamente

$$
y=kx,
$$
aunque sepamos que el sistema real solo se comporta así aproximadamente.

Entonces tenemos:

$$
[\mathrm{MOD}].
$$
#### Contexto D — Consecuencia matemática

Podemos partir de premisas anteriores y demostrar algebraicamente que

$$
y=kx.
$$
Entonces la relación no introduce nuevo contenido físico.

Su estatus es:

$$
[\mathrm{MATH}].
$$
La forma algebraica es idéntica.

El estatus no.
