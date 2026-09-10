- coherencia;
- simplicidad;
- alcance;
- capacidad predictiva;
- compatibilidad con otros fenómenos;
- estructura teórica;
- adecuación física.

#### P01 no demuestra que nunca haya unicidad

Puede haber unicidad **dentro de una clase restringida**.

#### P01 no demuestra que la predicción sea imposible

Precisamente las distintas predicciones permiten diseñar experimentos discriminantes.

#### P01 no demuestra que la matemática sea insuficiente

La matemática es la que hace visible la no unicidad.

Lo que no puede hacer, sin premisas adicionales, es inventar qué estructura física debemos imponer.
### 9.23. De la no unicidad al diseño experimental

Supongamos que dos candidatos:

$$
f
$$

y

$$
g
$$

coinciden en todos los datos conocidos:

$$
f(x_i)=g(x_i).
$$

Para distinguirlos debemos buscar algún $x_\ast$ tal que:

$$
f(x_\ast)\neq g(x_\ast).
$$

Entonces diseñamos una observación en esa condición.

La lógica es:

$$
\boxed{
f(x_\ast)\neq g(x_\ast)
\longrightarrow
\text{experimento potencialmente discriminante}.
}
$$

Este es el puente entre §9 y §10.

No basta saber que existen muchos modelos.

Debemos aprender **cómo elegir dónde mirar** para separarlos.
### 9.24. Ejercicios de §9


::: {.ma-block .ma-enunciado #fpm-i-01-e023}
**Ejercicio FPM-I-01-E023 — Demostrar la familia de no unicidad**

**Familia:** `E-PROOF / CORE`

Sean $x_1,\ldots,x_n$ distintos y supón que

$$
p(x_i)=y_i
$$

para todo $i$.

Define

$$
q(x)
=
p(x)
+
7\prod_{i=1}^{n}(x-x_i).
$$

Demuestra directamente que:

$$
q(x_i)=y_i
$$

para todo $i$.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

Fijemos un índice $j$.

Por definición:

$$
q(x_j)
=
p(x_j)
+
7\prod_{i=1}^{n}(x_j-x_i).
$$

Como:

$$
p(x_j)=y_j,
$$

tenemos:

$$
q(x_j)
=
y_j
+
7\prod_{i=1}^{n}(x_j-x_i).
$$

En el producto aparece el factor:

$$
x_j-x_j=0.
$$

Por tanto:

$$
\prod_{i=1}^{n}(x_j-x_i)=0.
$$

Luego:

$$
q(x_j)=y_j.
$$

Como $j$ era arbitrario:

$$
\boxed{
q(x_i)=y_i
\quad
\text{para todo }i.
}
$$

La constante $7$ no desempeña ningún papel especial. Podría sustituirse por cualquier $c$.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e024}
**Ejercicio FPM-I-01-E024 — Dos puntos, infinitas leyes**

**Familia:** `E-CON / CORE`

Considera los datos:

$$
(0,1),
\qquad
(1,2).
$$

1. Encuentra un polinomio lineal $p$ que pase por ambos puntos.
2. Construye una familia $p_c$ de polinomios que pase por los mismos puntos.
3. Calcula las predicciones para $x=2$ cuando $c=0$, $c=1$ y $c=-1$.
4. Explica qué demuestra el ejercicio.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

#### 1. Polinomio lineal

La recta:

$$
p(x)=x+1
$$

satisface:

$$
p(0)=1,
$$

$$
p(1)=2.
$$

#### 2. Familia

El factor que se anula en los puntos observados es:

$$
x(x-1).
$$

Por tanto:

$$
p_c(x)
=
x+1+c\,x(x-1).
$$

Para $x=0$:

$$
p_c(0)=1.
$$

Para $x=1$:

$$
p_c(1)=2.
$$

#### 3. Predicción en $x=2$

Tenemos:

$$
p_c(2)
=
3+2c.
$$

Entonces:

$$
p_0(2)=3,
$$

$$
p_1(2)=5,
$$

$$
p_{-1}(2)=1.
$$

#### 4. Interpretación

Los datos originales no distinguen entre estas funciones.

Pero un nuevo dato en $x=2$ podría hacerlo.

Por tanto:

$$
\boxed{
\text{mismo ajuste}
\not\Rightarrow
\text{misma predicción}.
}
$$
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e025}
**Ejercicio FPM-I-01-E025 — Tres puntos y una nueva familia**

**Familia:** `E-PROOF / ADVANCED`

Considera los datos:

$$
(0,1),
\qquad
(1,1),
\qquad
(2,3).
$$

El polinomio

$$
p(x)=x^2-x+1
$$

es compatible con ellos.

1. Verifica los tres datos.
2. Construye la familia

$$
p_c(x)
=
p(x)+c\,x(x-1)(x-2).
$$

3. Demuestra que todos los miembros de la familia conservan los tres datos.
4. Calcula $p_c(3)$.
5. Si una nueva observación produce $(3,7)$, determina qué valor de $c$ queda seleccionado **dentro de esta familia**.
6. Explica por qué ese nuevo dato todavía no demuestra unicidad absoluta entre todas las funciones posibles.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

#### 1. Verificación

Para $x=0$:

$$
p(0)=1.
$$

Para $x=1$:

$$
p(1)=1-1+1=1.
$$

Para $x=2$:

$$
p(2)=4-2+1=3.
$$

Por tanto, $p$ reproduce los tres datos.

#### 2. Familia

Definimos:

$$
p_c(x)
=
x^2-x+1
+
c\,x(x-1)(x-2).
$$

#### 3. Conservación de los datos

En $x=0$, el factor $x$ es cero.

En $x=1$, el factor $(x-1)$ es cero.

En $x=2$, el factor $(x-2)$ es cero.

Por tanto:

$$
p_c(0)=1,
$$

$$
p_c(1)=1,
$$

$$
p_c(2)=3
$$

para todo $c$.

#### 4. Valor en $x=3$

Tenemos:

$$
p(3)
=
9-3+1
=
7.
$$

Además:

$$
3(3-1)(3-2)
=
3\cdot2\cdot1
=
6.
$$

Luego:

$$
p_c(3)
=
7+6c.
$$

#### 5. Nuevo dato

Si observamos:

$$
p_c(3)=7,
$$

entonces:

$$
7+6c=7.
$$

Así:

$$
6c=0
$$

y:

$$
\boxed{c=0}.
$$

Dentro de esta familia queda seleccionado el polinomio:

$$
p(x)=x^2-x+1.
$$

#### 6. Por qué no hay unicidad absoluta

Ahora tenemos cuatro datos.

Podemos modificar nuevamente $p$ mediante un término que se anule en los cuatro valores:

$$
d\,x(x-1)(x-2)(x-3).
$$

Por tanto:

$$
p_d(x)
=
p(x)
+
d\,x(x-1)(x-2)(x-3)
$$

reproduce los cuatro datos para cualquier $d$.

La nueva observación restringió la familia anterior, pero los datos siguen siendo finitos.

$$
\boxed{
\text{más evidencia}
\Rightarrow
\text{más restricciones},
}
$$

pero no:

$$
\boxed{
\text{evidencia finita}
\Rightarrow
\text{unicidad entre todas las funciones}.
}
$$
:::

### 9.25. Síntesis

La primera proposición formal del capítulo establece:

$$
\boxed{
p_c(x)
=
p(x)
+
c\prod_{i=1}^{n}(x-x_i)
}
$$

y:

$$
\boxed{
p_c(x_i)=p(x_i)=y_i
}
$$

para todos los datos observados.

Por tanto:

$$
\boxed{
\text{datos finitos}
\not\Rightarrow
\text{ley funcional única}.
}
$$

La consecuencia metodológica es `MP15`:

$$
\boxed{
\text{ajuste exacto}
\not\Rightarrow
\text{identificación única}.
}
$$

Pero esto abre una pregunta constructiva.

Si muchas funciones son compatibles con los mismos datos, ¿cómo elegimos entre ellas?

La respuesta no puede ser simplemente:

> «escogemos la que nos gusta».

Necesitamos criterios físicos y matemáticos:

- estructura;
- simplicidad relevante;
- simetría;
- mecanismo;
- compatibilidad con teorías;
- régimen;
- capacidad de producir nuevas predicciones;
- experimentos discriminantes.

Ése será el objeto de:

$$
\boxed{
\text{§10 — Cómo se elige entre modelos compatibles con los datos}.
}
$$

---

## 10. Cómo se elige entre modelos compatibles con los datos {#fpm-i-01-s10}

### 10.1. Después de la no unicidad

En §9 demostramos que, si un polinomio $p$ reproduce una colección finita de datos

$$
(x_1,y_1),\ldots,(x_n,y_n),
$$

entonces toda la familia

$$
p_c(x)
=
p(x)
+
c\prod_{i=1}^{n}(x-x_i)
$$

reproduce exactamente esos mismos datos.

Por tanto:

$$
\boxed{
\text{ajuste exacto}
\not\Rightarrow
\text{identificación única}.
}
$$

Ahora aparece la pregunta físicamente interesante:

> Si varios modelos son compatibles con los datos disponibles, ¿cómo elegimos entre ellos?

Una primera respuesta sería:

> obteniendo más datos.

Eso es correcto, pero incompleto.

Antes de medir algo nuevo debemos decidir **qué** medir.

Si dos modelos coinciden en todas las condiciones que volvemos a observar, el nuevo experimento no los distinguirá.

La selección de modelos exige combinar:

- evidencia;
- estructura física;
- teoría;
- economía de hipótesis;
- régimen de validez;
- capacidad explicativa;
- nuevas predicciones;
- diseño experimental.
Sería cómodo disponer de una regla:

$$
\text{modelo A}
>
\text{modelo B}
$$

que pudiera decidirse siempre mediante un solo número.

No adoptaremos tal regla.

En distintas situaciones pueden importar criterios diferentes.

Un modelo puede ser:

- más simple;
- más preciso;
- más general;
- más fácil de medir;
- más conectado con una teoría;
- más explicativo;
- más robusto;
- más útil para una pregunta concreta.

Y esas ventajas pueden entrar en tensión.

Por tanto:

$$
\boxed{
\text{selección de modelos}
\neq
\text{aplicación mecánica de una única regla}.
}
$$

La comparación debe conservar visible **para qué pregunta**, **con qué datos** y **en qué régimen** se está eligiendo.
::: {.ma-block .ma-definicion #fpm-i-01-d26}
**Definición operativa FPM-I-01-D26 — Criterio de selección de modelos**
Un **criterio de selección de modelos** es una propiedad, condición o prueba utilizada para comparar modelos candidatos respecto de una pregunta física, una evidencia disponible y un régimen de aplicación determinados.
:::

La definición es deliberadamente contextual.

Un criterio que resulta decisivo para una tarea puede ser secundario para otra.

Por ejemplo, si queremos una predicción de baja precisión en un régimen estrecho, un modelo sencillo puede ser suficiente.

Si queremos comprender un nuevo fenómeno fuera de ese régimen, la misma descripción puede dejar de ser adecuada.
Recordemos `MP02` y `MP11`:

- la adecuación es relativa a una pregunta;
- la suficiencia depende de la tarea.

No existe «el mejor modelo» sin contexto.

Puede existir:

> el modelo más adecuado para estimar cierta cantidad con determinada precisión en cierto régimen.

Un modelo muy detallado puede ser innecesario para una pregunta.

Uno muy simple puede ser insuficiente para otra.

Por tanto:

::: {.ma-block .ma-metodo #fpm-i-01-mp16}
**Principio FPM-I-01-MP16 — La preferencia entre modelos es relativa a la tarea**
Comparar modelos exige declarar la pregunta, la evidencia y el régimen. Una preferencia metodológica no constituye un orden absoluto entre modelos independiente de su uso.
:::

### 10.2. Tres capas de comparación
