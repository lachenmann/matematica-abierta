### 14.4. Señales de alarma

A lo largo del libro convendrá detenerse cuando aparezca alguna de estas situaciones:

#### 1. Una ecuación sin interpretación

Preguntar:

> ¿qué significan los símbolos?

#### 2. Una aproximación sin régimen

Preguntar:

> ¿qué la controla?

#### 3. Una idealización sin omisión declarada

Preguntar:

> ¿qué se dejó fuera?

#### 4. Una predicción sin procedimiento observacional

Preguntar:

> ¿cómo se mediría?

#### 5. Una solución matemáticamente válida pero extraña físicamente

Preguntar:

> ¿es admisible dentro del modelo?

#### 6. Un desacuerdo experimental

Preguntar:

> ¿qué parte del paquete predictivo debe auditarse?

#### 7. Una teoría más avanzada que «reemplaza» otra

Preguntar:

> ¿qué régimen recupera y qué estructura cambia?

#### 8. Una fórmula muy elegante

Preguntar:

> ¿su elegancia matemática coincide con adecuación física?

Estas preguntas no son obstáculos.

Son el método.
### 14.5. Principio final del capítulo

::: {.ma-block .ma-metodo #fpm-i-01-mp23}
**Principio FPM-I-01-MP23 — Ningún cálculo físico se cierra al obtener un número**
Un cálculo físico termina solamente cuando el resultado ha sido interpretado respecto del sistema, las premisas, el estatus de las relaciones, el régimen de validez, las restricciones físicas y la conexión observacional pertinentes.
:::

En forma esquemática:

$$
\boxed{
\text{cálculo}
\to
\text{interpretación}
\to
\text{control físico}.
}
$$

Este será el principio operativo que acompañará todo el tratado.
### 14.6. Ejercicio de síntesis

::: {.ma-block .ma-enunciado #fpm-i-01-e032}
**Ejercicio FPM-I-01-E032 — Ficha completa de un modelo**

**Familia:** `E-MOD / SYNTHESIS`

Un pequeño carro se desplaza por una pista recta. Una cámara registra su posición en instantes igualmente espaciados.

En una primera serie de observaciones se obtiene:

$$
x_0=0,
$$

$$
x_1=2,
$$

$$
x_2=4,
$$

$$
x_3=6.
$$

Las posiciones están expresadas en una misma unidad de longitud. No utilizaremos todavía una teoría mecánica para explicar el movimiento.

Se propone el modelo empírico discreto:

$$
[\mathrm{MOD}]
\qquad
x_{n+1}=x_n+d,
$$

con:

$$
d=2.
$$

Construye una **ficha FPM completa** respondiendo:

1. ¿Cuál es el fenómeno?
2. Formula una pregunta física concreta.
3. Define sistema y entorno.
4. Propón un espacio de estados mínimo para la pregunta.
5. Identifica variable de estado, parámetro y observable.
6. Explica el estatus de:
   $$
   x_{n+1}=x_n+d.
   $$
7. Identifica una posible condición inicial.
8. Formula una predicción para $x_4$.
9. Explica qué parte de esa predicción es `[MATH]`.
10. Explica qué regla `[OBS]` sería necesaria para contrastarla.
11. Declara al menos dos idealizaciones o simplificaciones del modelo.
12. Propón un régimen de validez cualitativo.
13. Si la cámara observa $x_4=8$, ¿qué podemos concluir?
14. Si observa $x_4=7.1$, aplica la lógica de §12 y enumera al menos cuatro elementos a auditar.
15. Explica por qué el modelo no constituye todavía una teoría mecánica del carro.
16. Explica qué observación nueva sería útil para probar si la regla continúa funcionando.
17. Evalúa la exactitud matemática y la adecuación física por separado.
18. Resume el modelo usando:
   $$
   (\mathcal M,\mathfrak I_{\mathcal M}).
   $$
:::
#### Solución

#### 1. Fenómeno

El fenómeno es el cambio de posición de un carro sobre una pista recta observado mediante una cámara en instantes sucesivos.

Todavía no afirmamos qué causa el movimiento.
#### 2. Pregunta física

Una pregunta concreta puede ser:

> ¿Qué posición registrará la cámara en el siguiente instante si continúa la regularidad observada?

Esta pregunta es predictiva y deliberadamente modesta.
#### 3. Sistema y entorno

**Sistema:**

el carro, representado solo mediante la información necesaria para registrar su posición.

**Entorno:**

la pista, la cámara y cualquier agente externo que pueda afectar al movimiento quedan fuera de la frontera inicial del sistema, aunque parte de sus efectos puede estar implícitamente presente en la regularidad empírica.

Si más adelante esos efectos importan, la frontera deberá revisarse.
#### 4. Espacio de estados mínimo

Para esta pregunta elemental podemos utilizar:

$$
\mathcal S
=
\{(n,x): n\in\mathbb N,\ x\in\mathbb R\}.
$$

El estado modelado conserva:

- el índice temporal discreto $n$;
- la posición $x$.

No afirmamos que esto sea suficiente para toda pregunta mecánica sobre el carro.

Es suficiente para la tarea predictiva propuesta.
