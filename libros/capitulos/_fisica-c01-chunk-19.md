$$
\boxed{
\text{fallo predictivo}
\neq
\text{diagnóstico automático}.
}
$$
::: {.ma-block .ma-metodo}
**Ficha FPM — Ajuste, predicción, retrodicción y explicación**
1. **Datos usados:** ¿qué observaciones ya conocíamos?
2. **Ajuste:** ¿qué parámetros o elecciones se fijaron con esos datos?
3. **Predicción:** ¿qué resultado no fue utilizado para fijar la consecuencia?
4. **Régimen:** ¿la nueva condición pertenece a $\mathcal R$?
5. **Observación:** ¿qué regla `[OBS]` conecta la predicción con un dato?
6. **Retrodicción:** si inferimos el pasado, ¿la reconstrucción es única?
7. **Explicación:** ¿qué estructura concreta del modelo produce el resultado?
8. **Alternativas:** ¿otra estructura podría producir observaciones semejantes?
9. **Nueva prueba:** ¿qué observación distinguiría las alternativas?
:::
Esta separación prepara §9: incluso un ajuste perfecto sobre datos finitos no determina por sí solo una ley única. La fuerza de una prueba aumenta cuando el modelo se compromete con resultados que no fueron utilizados para construir precisamente esa consecuencia.

### 8.5. Ejercicio

::: {.ma-block .ma-enunciado #fpm-i-01-e022}
**Ejercicio FPM-I-01-E022 — Ajuste, predicción, retrodicción y explicación**

**Familia:** `E-CON / ADVANCED`

Considera el modelo

$$
y=kx.
$$

Se observa primero:

$$
(x_1,y_1)=(2,6).
$$

Con ese dato se fija:

$$
k=3.
$$

##### Parte A

Clasifica cada operación.

1. Verificar que $6=3\cdot2$.
2. Antes de medir un segundo caso, calcular que para $x_2=5$ el modelo da $y_2=15$.
3. Medir después $y_2$ y compararlo con $15$.
4. Usar también el segundo dato para modificar $k$ y después presentar ambos datos como «predicciones independientes».

##### Parte B

Sea ahora

$$
\mathcal S=\{a,b,c\}
$$

con evolución

$$
E(a)=c,
\qquad
E(b)=c,
\qquad
E(c)=b.
$$

Si el estado actual es $c$, determina todos los estados anteriores posibles.

##### Parte C

Un estudiante afirma:

> «Como el modelo reproduce correctamente todos los datos con los que fue construido, ya hemos explicado el fenómeno.»

Analiza la afirmación.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

##### Parte A.1

Comprobar

$$
6=3\cdot2
$$

es verificar que el modelo ajustado reproduce el dato utilizado para fijar $k$.

Clasificación:

$$
\boxed{\text{reproducción de dato de ajuste}}.
$$

No es una predicción independiente.

##### Parte A.2

El cálculo

$$
y_{2,\mathrm{pred}}
=
3\cdot5
=
15
$$

se hace antes de usar el resultado del segundo caso.

Clasificación:

$$
\boxed{\text{predicción}}.
$$

Es una consecuencia `[MATH]` del modelo ya fijado.

##### Parte A.3

Medir $y_2$ y compararlo con $15$ es:

$$
\boxed{\text{contraste experimental de una predicción}}.
$$

La comparación necesita una regla `[OBS]`.

Si la observación coincide, el nuevo dato apoya el modelo dentro del régimen considerado.

Si no coincide, habrá que diagnosticar qué componente falla.

##### Parte A.4

Si utilizamos también el segundo dato para volver a escoger $k$, ese dato deja de ser independiente respecto del ajuste resultante.

Presentarlo después como si hubiera sido predicho sin haber intervenido en la construcción viola `MP13`.

Clasificación:

$$
\boxed{\text{nuevo ajuste, no predicción independiente}}.
$$

##### Parte B

Buscamos todos los $s_0\in\mathcal S$ tales que

$$
E(s_0)=c.
$$

Como

$$
E(a)=c
$$

y

$$
E(b)=c,
$$

los estados pasados compatibles son:

$$
\boxed{s_0\in\{a,b\}}.
$$

No podemos distinguirlos utilizando solo el estado actual $c$.

Por tanto, la retrodicción no es única.

##### Parte C

La afirmación es demasiado fuerte.

Que el modelo reproduzca los datos utilizados para construirlo muestra, como mínimo, **compatibilidad con esos datos**.

No demuestra por sí solo:

- capacidad predictiva independiente;
- unicidad del modelo;
- corrección de todas sus idealizaciones;
- adecuación fuera del régimen contrastado;
- explicación física del mecanismo.

Para hablar de explicación necesitamos identificar qué estructura del modelo produce el fenómeno y qué diferencias observables esperaríamos si esa estructura cambiara.

Además, una prueba más fuerte debería reservar algún resultado nuevo:

$$
D_{\mathrm{ajuste}}
\longrightarrow
M
\longrightarrow
P(D_{\mathrm{nuevo}})
\longleftrightarrow
D_{\mathrm{nuevo}}.
$$

La conclusión correcta es:

$$
\boxed{
\text{ajustar}
\neq
\text{predecir}
\neq
\text{explicar}.
}
$$
:::

### 8.6. Síntesis

Ya podemos distinguir cuatro operaciones.

$$
\boxed{
\text{ajuste}
=
\text{usar datos para fijar el modelo}
}
$$

$$
\boxed{
\text{predicción}
=
\text{obtener una consecuencia para un caso no usado para fijarla}
}
$$

$$
\boxed{
\text{retrodicción}
=
\text{inferir estados o condiciones anteriores desde información posterior}
}
$$

$$
\boxed{
\text{explicación}
=
\text{hacer visible qué estructura produce el fenómeno}
}
$$

La relación entre ellas puede representarse como:

$$
D_{\mathrm{ajuste}}
\to
M
\to
\begin{cases}
\text{predicción},\\
\text{retrodicción},\\
\text{explicación}
\end{cases}
\longleftrightarrow
D_{\mathrm{nuevo}}.
$$

Y conservaremos dos reglas:

$$
\boxed{
\text{dato usado para ajustar}
\neq
\text{predicción independiente}
}
$$

y

$$
\boxed{
\text{éxito predictivo}
\neq
\text{explicación automática}.
}
$$

Ahora podemos enfrentar una pregunta más profunda.

Si observamos una colección finita de datos y encontramos una función que pasa exactamente por todos ellos, ¿hemos descubierto **la** ley?

La respuesta matemática será no.

En la sección siguiente lo demostraremos.

Entramos así en:

$$
\boxed{
\text{§9 — Datos finitos no determinan una ley única}.
}
$$

---

## 9. Datos finitos no determinan una ley única {#fpm-i-01-s09}

### 9.1. Una tabla no trae escrita su ley

Supongamos que realizamos un experimento y obtenemos los pares

$$
(x_1,y_1),\ldots,(x_n,y_n).
$$

Imaginemos además que encontramos una función $f$ que reproduce exactamente todos los datos:

$$
f(x_i)=y_i
$$

para cada

$$
i=1,\ldots,n.
$$

La tentación es decir:

> «Hemos encontrado la ley que generan los datos».

Pero esa conclusión contiene más información que las observaciones.

Los datos nos dicen qué debe ocurrir en los puntos medidos:

$$
x_1,\ldots,x_n.
$$

No nos dicen directamente qué debe ocurrir en los demás valores de $x$.

Entre dos puntos observados, o fuera del intervalo observado, quedan infinitas posibilidades.

Esta sección convertirá esa cautela en un resultado matemático exacto.
### 9.2. Compatibilidad no es unicidad

Conviene separar dos afirmaciones.

#### Afirmación A

La función $f$ es **compatible** con los datos:

$$
f(x_i)=y_i
$$

para todos los $i$.

#### Afirmación B

La función $f$ es la **única** función compatible con los datos.

La primera no implica la segunda.

En símbolos:

$$
\boxed{
f(x_i)=y_i\ \text{para todos los datos}
\not\Rightarrow
f\ \text{es la única ley compatible}.
}
$$

El salto de compatibilidad a unicidad necesita hipótesis adicionales.
### 9.3. Dos puntos: la intuición geométrica más simple

Tomemos dos observaciones:

$$
(0,0),
\qquad
(1,1).
$$

La función

$$
p(x)=x
$$

pasa por ambos puntos.

Podríamos pensar que los datos sugieren la recta

$$
y=x.
$$

Pero consideremos ahora

$$
q(x)=x+c\,x(x-1),
$$

donde $c$ es cualquier constante.

En $x=0$,

$$
q(0)
=
0+c\cdot0\cdot(-1)
=
0.
$$

En $x=1$,

$$
q(1)
=
1+c\cdot1\cdot0
=
1.
$$

Por tanto, **todos** los valores de $c$ producen funciones que pasan por los dos mismos puntos.

Para $c=0$:

$$
q(x)=x.
$$

Para $c=1$:

$$
q(x)=x+x(x-1)=x^2.
$$

Para $c=-1$:

$$
q(x)=x-x(x-1)=2x-x^2.
$$

Las tres funciones coinciden en los datos:

$$
q(0)=0,
\qquad
q(1)=1,
$$

pero no coinciden, por ejemplo, en

$$
x=\frac12.
$$

Así aparecen muchas continuaciones posibles de la misma evidencia finita.
### 9.4. El truco algebraico

¿Qué hizo funcionar el ejemplo?

Añadimos a $p(x)$ un término que vale cero exactamente en todos los puntos observados.

Con dos datos usamos:

$$
x(x-1).
$$

Este producto se anula cuando:

$$
x=0
$$

o

$$
x=1.
$$

Por eso modificar

$$
p(x)
$$

mediante

$$
p(x)+c\,x(x-1)
$$

no altera ninguno de los datos.

La idea general será construir un polinomio que se anule en todos los valores observados.
### 9.5. El polinomio que desaparece en los datos

Sean

$$
x_1,\ldots,x_n\in\mathbb R
$$

valores distintos de la variable independiente.

Definimos

$$
Z(x)
=
\prod_{i=1}^{n}(x-x_i).
$$

No necesitamos ninguna teoría avanzada de polinomios para observar que, para cada índice $j$,

$$
Z(x_j)
=
\prod_{i=1}^{n}(x_j-x_i).
$$

En ese producto aparece el factor correspondiente a $i=j$:

$$
x_j-x_j=0.
$$

Por tanto,

$$
\boxed{
Z(x_j)=0
}
$$

para todo

$$
j=1,\ldots,n.
$$

Esta es toda la idea algebraica que necesitaremos.
### 9.6. Primera proposición formal del capítulo

::: {.ma-block .ma-enunciado #fpm-i-01-p01}
**FPM-I-01-P01 — Datos finitos no determinan una ley polinómica única**

Sean $x_1,\ldots,x_n\in\mathbb R$ valores distintos y sean $y_1,\ldots,y_n\in\mathbb R$. Supongamos que un polinomio

$$
p\in\mathbb R[x]
$$

satisface

$$
p(x_i)=y_i
$$

para todo

$$
i=1,\ldots,n.
$$

Entonces, para toda constante

$$
c\in\mathbb R,
$$

el polinomio

$$
p_c(x)
=
p(x)
+
c\prod_{i=1}^{n}(x-x_i)
$$

satisface exactamente los mismos datos:

$$
p_c(x_i)=y_i
$$

para todo

$$
i=1,\ldots,n.
$$

Además, si $c_1\neq c_2$, entonces

$$
p_{c_1}\neq p_{c_2}.
$$

Por tanto, una vez que existe un polinomio compatible con los datos, existen infinitos polinomios distintos compatibles con esos mismos datos.
:::
