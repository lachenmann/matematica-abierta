La taxonomía es una herramienta de lectura, no una policía terminológica.
Una predicción concreta está más situada que la teoría que la hace posible, y la teoría tampoco es un formalismo sin semántica:

Podemos escribir de forma esquemática:

$$
T
\longrightarrow
M
\longrightarrow
P,
$$

donde:

- $T$ representa una teoría;
- $M$ un modelo particular;
- $P$ una predicción.

Pero normalmente una predicción concreta requiere además datos y condiciones:

$$
T
+
M
+
I
+
B
+
\theta
+
\text{aproximaciones}
\longrightarrow
P.
$$

Por eso, si la predicción falla, no podemos concluir inmediatamente:

$$
\text{«la teoría completa es falsa».}
$$

En §12 analizaremos formalmente esta lógica de revisión.
Podríamos imaginar una teoría como una estructura puramente formal.

Pero para ser teoría **física** debe existir alguna manera de conectar parte del formalismo con fenómenos y observaciones.

En términos de §5, una teoría debe permitir construir diccionarios como

$$
\mathfrak I_{\mathcal M}
$$

para sus modelos.

En términos de §6, debe haber relaciones `[OBS]` suficientes para confrontar consecuencias con datos.

Por eso:

$$
\boxed{
\text{formalismo sin interpretación}
\neq
\text{teoría física completa}
}
$$

aunque el formalismo pueda constituir un objeto matemático perfectamente interesante por sí mismo.
Feynman insiste en una idea que conviene conservar metodológicamente: el experimento pone a prueba las leyes, pero los datos no generan por sí solos las grandes generalizaciones.[@feynman2011lectures1, vol. I, cap. 1, §1-1, p. 1-1]

Hay un salto creativo y estructural:

$$
\text{observaciones}
\longrightarrow
\text{regularidades sugeridas}
\longrightarrow
\text{hipótesis y generalizaciones}
\longrightarrow
\text{nuevas predicciones}.
$$

La flecha central no es una inferencia lógica automática.

En §9 veremos una razón matemática elemental: los datos finitos no determinan una función única.

Por tanto, una teoría no es una simple compresión mecánica de una tabla experimental.
Hassani subraya que las estructuras matemáticas utilizadas en física poseen simultáneamente poder y límites.[@hassani2013mathematical, «Preface to First Edition», p. xii]

Para nuestro libro esto implica dos reglas.

##### Regla 1

No presentar una estructura matemática como si su aplicabilidad física fuera automática.

##### Regla 2

No reducir la matemática a una calculadora.

Una estructura matemática puede revelar:

- invariantes;
- relaciones ocultas;
- posibilidades;
- imposibilidades;
- equivalencias;
- límites;
- nuevas variables naturales.

Así, la relación entre teoría y matemática es bidireccional:

$$
\text{estructura física}
\longrightarrow
\text{formalismo matemático}
\longrightarrow
\text{nueva comprensión física}.
$$
### 7.3. Matriz de lectura

| Pregunta | Ley | Modelo | Teoría |
|---|---|---|---|
| ¿Qué organiza? | una regularidad, relación o principio | un sistema o clase de sistemas | una familia de modelos |
| ¿Qué necesita además? | interpretación y dominio | estados, parámetros, condiciones, idealizaciones, observación | principios, estructuras y reglas comunes |
| ¿Está situada en una realización concreta? | no necesariamente | sí, o en una clase bien especificada | normalmente no |
| ¿Su nombre histórico fija su función? | no | no | no |

::: {.ma-block .ma-metodo #fpm-i-01-mp12}
**Principio FPM-I-01-MP12 — No colapsar los niveles de organización**
Al analizar una afirmación física distinguiremos entre la relación o principio que funciona como ley, el modelo concreto en el que se aplica y la teoría que organiza una familia de modelos. Las tres capas pueden estar estrechamente conectadas, pero no son intercambiables.
:::

Este principio será especialmente útil cuando una derivación parezca decir:

> «La teoría predice…»

Preguntaremos entonces:

1. ¿qué modelo particular de la teoría se está usando?;
2. ¿qué condiciones se han fijado?;
3. ¿qué aproximaciones se han introducido?;
4. ¿qué observable se compara con el experimento?
### 7.4. Ejercicio

::: {.ma-block .ma-enunciado #fpm-i-01-e021}
**Ejercicio FPM-I-01-E021 — Ley, modelo o teoría**

**Familia:** `E-CON / CORE`

Clasifica cada descripción principalmente como **ley**, **modelo** o **teoría**, justificando la respuesta. Si el caso admite más de una lectura, explica qué información adicional necesitarías.

1. Una relación experimental entre dos magnitudes, válida en cierto intervalo, escrita como $Y=kX$.
2. Una descripción de un péndulo que especifica sistema, masa puntual, hilo inextensible, variables, parámetros, preparación inicial, observables y régimen de validez.
3. Un marco general que establece conceptos y principios con los que se construyen modelos de muchos sistemas mecánicos diferentes.
4. La ecuación $Y=kX$ escrita sin ninguna interpretación física.
5. Un conjunto de reglas para representar un instrumento concreto y convertir su señal en un valor medido.
6. Un texto histórico titulado «modelo de X» que, al examinarlo, contiene principios generales y permite construir una amplia familia de modelos.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

##### 1. Relación experimental $Y=kX$

La clasificación principal es:

$$
\boxed{\text{ley}}
$$

porque se presenta como una regularidad física entre magnitudes dentro de un dominio.

Su estatus en el sentido de §6 sería principalmente:

$$
[\mathrm{EMP}].
$$

Pero para usarla en un problema concreto todavía necesitamos un modelo.
##### 2. Descripción detallada del péndulo

La clasificación principal es:

$$
\boxed{\text{modelo}}
$$

porque la descripción especifica un sistema particular y organiza:

- idealizaciones;
- variables;
- parámetros;
- condiciones;
- observables;
- régimen.

No basta con que utilice leyes: la característica decisiva es que **sitúa** esas relaciones en una representación concreta.
##### 3. Marco general para muchos sistemas mecánicos

La clasificación principal es:

$$
\boxed{\text{teoría}}
$$

porque proporciona una arquitectura común capaz de generar o estructurar muchos modelos.
##### 4. $Y=kX$ sin interpretación

No podemos clasificarla todavía como ley física.

Es únicamente una relación matemática:

$$
\boxed{\text{estructura formal sin estatus físico determinado}}.
$$

Necesitamos saber:

- qué significan los símbolos;
- cómo se obtuvo la relación;
- qué función cumple.

Este es exactamente el aprendizaje de §§5–6.
##### 5. Reglas para un instrumento concreto

La clasificación principal es:

$$
\boxed{\text{modelo}}
$$

más precisamente, **modelo del instrumento**.

Puede incluir relaciones `[OBS]`, calibraciones e idealizaciones.

No constituye necesariamente una teoría física amplia.
##### 6. Un «modelo» histórico que funciona como marco general

Aquí la respuesta correcta exige separar **nombre histórico** y **función**.

Si realmente contiene principios generales y organiza una amplia familia de modelos, cumple en nuestra taxonomía operativa una función cercana a:

$$
\boxed{\text{teoría}}.
$$

Sin embargo, no renombraríamos obligatoriamente la construcción histórica.

Diríamos:

> «Se llama tradicionalmente modelo, pero en este contexto desempeña una función teórica más amplia.»

##### Conclusión

La clasificación no depende del título.

Depende de la función:

$$
\boxed{
\text{ley}:\text{ relación};
\qquad
\text{modelo}:\text{ representación situada};
\qquad
\text{teoría}:\text{ marco organizador}.
}
$$
:::

### 7.5. Síntesis

Podemos resumir la arquitectura así:

$$
\boxed{
\text{teoría}
\longrightarrow
\text{familias de modelos}
\longrightarrow
\text{realizaciones}
\longrightarrow
\text{predicciones}
\longleftrightarrow
\text{observaciones}
}
$$

Las leyes aparecen como relaciones o principios dentro de esta arquitectura.

Una ley no es todavía un modelo completo.

Un modelo no es todavía una teoría general.

Una teoría no produce por sí sola una predicción concreta sin especificar un modelo, datos, condiciones, parámetros y reglas de interpretación.

El principio que conservará el lector es:

$$
\boxed{
\text{no confundir una relación física,
una representación de un sistema
y el marco que organiza muchas representaciones}
}
$$

Con esta distinción ya podemos formular una nueva pregunta.

Una vez fijados teoría, modelo y condiciones, ¿qué significa **predecir**?

¿Es lo mismo ajustar datos, reconstruir el pasado, predecir una observación nueva y explicar un fenómeno?

Este será el objeto de:

$$
\boxed{\text{§8 — Predicción, retrodicción y explicación}.}
$$

---

## 8. Predicción, retrodicción y explicación {#fpm-i-01-s08}

### 8.1. Ajustar y predecir no son la misma operación

En §7 construimos la cadena

$$
\text{teoría}
\longrightarrow
\text{modelos}
\longrightarrow
\text{realizaciones}
\longrightarrow
\text{predicciones}
\longleftrightarrow
\text{observaciones}.
$$

Ahora debemos detenernos en la palabra **predicción**.

Supongamos que un modelo produce el valor

$$
y=12.
$$

¿Hemos hecho una predicción?

No podemos saberlo todavía.

Tal vez el valor $12$ fue calculado antes de realizar una observación nueva.

Pero también podría haber ocurrido lo contrario:

1. observamos primero el valor $12$;
2. elegimos después los parámetros del modelo para reproducirlo;
3. finalmente mostramos que el modelo devuelve precisamente $12$.

La igualdad matemática es la misma.

La situación metodológica no.

Por tanto:

$$
\boxed{
\text{reproducir un dato conocido}
\neq
\text{predecir un dato nuevo}.
}
$$

Esta será nuestra primera distinción.
Consideremos una relación elemental:
