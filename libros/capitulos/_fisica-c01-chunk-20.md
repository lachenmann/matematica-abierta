### 9.7. Demostración de FPM-I-01-P01

#### Paso 1 — Fijar uno de los datos

Sea

$$
j\in\{1,\ldots,n\}.
$$

Queremos evaluar

$$
p_c(x_j).
$$

Por definición:

$$
p_c(x_j)
=
p(x_j)
+
c\prod_{i=1}^{n}(x_j-x_i).
$$

#### Paso 2 — Usar el dato conocido

Como $p$ es compatible con los datos,

$$
p(x_j)=y_j.
$$

Por tanto:

$$
p_c(x_j)
=
y_j
+
c\prod_{i=1}^{n}(x_j-x_i).
$$

#### Paso 3 — Detectar el factor nulo

En el producto aparece el factor

$$
x_j-x_j=0.
$$

Luego:

$$
\prod_{i=1}^{n}(x_j-x_i)=0.
$$

Así,

$$
p_c(x_j)
=
y_j+c\cdot0
=
y_j.
$$

Como $j$ era arbitrario,

$$
\boxed{
p_c(x_i)=y_i
\quad
\text{para todo }i=1,\ldots,n.
}
$$

#### Paso 4 — Mostrar que la familia contiene polinomios distintos

Sean

$$
c_1\neq c_2.
$$

Entonces:

$$
p_{c_1}(x)-p_{c_2}(x)
=
(c_1-c_2)
\prod_{i=1}^{n}(x-x_i).
$$

Como

$$
c_1-c_2\neq0
$$

y

$$
\prod_{i=1}^{n}(x-x_i)
$$

no es el polinomio cero, tenemos:

$$
p_{c_1}-p_{c_2}
\neq
0.
$$

Por tanto:

$$
p_{c_1}\neq p_{c_2}.
$$

Finalmente, como existen infinitos números reales $c$, obtenemos infinitos polinomios distintos compatibles con los mismos datos.

$$
\boxed{\text{QED}}
$$
### 9.8. Qué se demostró exactamente

La proposición **no** dice que cualquier polinomio pase por los datos.

Dice algo más preciso.

Partimos de **un** polinomio compatible:

$$
p.
$$

Después construimos una familia:

$$
\{p_c\}.
$$

Todos los miembros conservan las observaciones porque la modificación añadida desaparece en los puntos medidos.

La estructura es:

$$
\boxed{
\text{ajuste conocido}
+
\text{término invisible en los datos}
=
\text{nuevo ajuste igualmente compatible}.
}
$$

Ésa es la idea que debemos conservar.
### 9.9. La demostración es matemática; la conclusión física necesita interpretación

`FPM-I-01-P01` es una proposición matemática.

Su estatus es:

$$
[\mathrm{MATH}].
$$

La proposición no afirma por sí sola:

> «Las leyes de la naturaleza son polinomios».

Tampoco afirma:

> «Nunca podemos conocer ninguna ley física».

Lo que demuestra es más limitado y más útil:

> una colección finita de valores no basta, por sí sola, para seleccionar una única función polinómica entre todas las que podrían reproducirlos.

La inferencia física será:

$$
\boxed{
\text{ajuste exacto a datos finitos}
\not\Rightarrow
\text{identificación lógica de una ley única}.
}
$$
### 9.10. El papel de las hipótesis adicionales

¿Cómo puede la física elegir entre funciones compatibles?

Necesitamos información adicional.

Por ejemplo, podemos imponer:

- una clase restringida de funciones;
- una simetría;
- una estructura teórica;
- un mecanismo;
- un principio de conservación;
- un régimen de validez;
- restricciones sobre parámetros;
- nuevas observaciones.

La función no se elige solamente preguntando:

> «¿pasa por los puntos?»

También preguntamos:

> «¿qué estructura física la justifica?»

Este será precisamente el tema de §10.
### 9.11. Si restringimos la clase, la situación puede cambiar

Supongamos que tenemos los dos puntos

$$
(0,0),
\qquad
(1,1).
$$

Entre **todas** las funciones hay innumerables posibilidades.

Entre todos los polinomios también.

Pero si imponemos la hipótesis adicional:

> «la relación debe ser lineal y de la forma $y=mx+b$»,

entonces los dos datos pueden determinar $m$ y $b$.

La unicidad no proviene solamente de los dos puntos.

Proviene de:

$$
\boxed{
\text{datos}
+
\text{restricción de clase}.
}
$$

Por tanto, cuando un conjunto de datos parece «determinar» una ley debemos preguntar:

> **¿dentro de qué clase de modelos?**
### 9.12. Ajuste perfecto y complejidad

Imaginemos cien datos experimentales.

Una función muy flexible podría construirse para pasar exactamente por todos ellos.

¿Debemos preferirla automáticamente?

No.

Un ajuste perfecto puede ocultar varios problemas:

- sensibilidad excesiva;
- mala extrapolación;
- gran cantidad de parámetros;
- ausencia de interpretación;
- adaptación a irregularidades accidentales;
- falta de conexión con una teoría física.

Todavía no desarrollaremos estos problemas estadísticamente.

Solo fijaremos la diferencia lógica:

$$
\boxed{
\text{capacidad de reproducir datos}
\neq
\text{calidad física automática del modelo}.
}
$$
### 9.13. Volver a §8: ajuste frente a predicción

La proposición explica por qué `MP13` era necesaria.

Supongamos que elegimos $p_c$ después de conocer todos los datos.

Entonces todos los miembros de la familia pueden ajustarlos perfectamente.

Pero en un valor nuevo

$$
x_\ast
\notin
\{x_1,\ldots,x_n\},
$$

tenemos:

$$
p_c(x_\ast)
=
p(x_\ast)
+
c\prod_{i=1}^{n}(x_\ast-x_i).
$$

Como ningún factor es necesariamente cero, el resultado depende de $c$.

Distintos modelos compatibles con los mismos datos pueden producir predicciones diferentes.

Por eso un nuevo experimento puede ser discriminante.
### 9.14. Ejemplo desarrollado 14 — Dos datos, infinitas predicciones

Retomemos:

$$
(0,0),
\qquad
(1,1).
$$

La familia es:

$$
p_c(x)
=
x+c\,x(x-1).
$$

Preguntemos qué predice cada modelo para:

$$
x=2.
$$

Tenemos:

$$
p_c(2)
=
2+c\cdot2\cdot1
=
2+2c.
$$

Si:

$$
c=0,
$$

obtenemos:

$$
p_0(2)=2.
$$

Si:

$$
c=1,
$$

obtenemos:

$$
p_1(2)=4.
$$

Si:

$$
c=-1,
$$

obtenemos:

$$
p_{-1}(2)=0.
$$

Tres funciones indistinguibles en los datos originales producen tres predicciones completamente distintas en el nuevo punto.

Por tanto:

$$
\boxed{
\text{nuevo dato}
\longrightarrow
\text{posible discriminación entre modelos}.
}
$$
### 9.15. Un dato nuevo elimina modelos, pero no necesariamente deja uno solo

Supongamos que el nuevo experimento produce:

$$
(2,4).
$$

Dentro de nuestra familia:

$$
p_c(2)=2+2c.
$$

Para reproducir $4$ necesitamos:

$$
2+2c=4.
$$

Entonces:

$$
c=1.
$$

Parece que hemos seleccionado:

$$
p(x)=x^2.
$$

Pero debemos ser cuidadosos.

Hemos seleccionado $c=1$ **dentro de esta familia particular**.

Todavía podemos construir otras funciones que coincidan en:

$$
x=0,\quad x=1,\quad x=2
$$

y difieran en otra parte.

De hecho, podemos añadir:

$$
d\,x(x-1)(x-2).
$$

Por tanto:

$$
\boxed{
\text{más datos restringen}
\neq
\text{datos finitos garantizan unicidad absoluta}.
}
$$
### 9.16. Tres datos y la misma construcción

Supongamos ahora:

$$
(0,0),
\qquad
(1,1),
\qquad
(2,4).
$$

El polinomio

$$
p(x)=x^2
$$

reproduce los tres datos.

Construimos:

$$
p_c(x)
=
x^2
+
c\,x(x-1)(x-2).
$$

En cada punto observado, uno de los factores del producto se anula.

Por tanto:

$$
p_c(0)=0,
$$

$$
p_c(1)=1,
$$

$$
p_c(2)=4.
$$

Pero en

$$
x=3
$$

obtenemos:

$$
p_c(3)
=
9+6c.
$$

Así, los tres datos tampoco fijan una predicción única para $x=3$.
### 9.17. Lo que los datos sí hacen

No debemos ir al extremo contrario.

Los datos finitos no son inútiles.

Cada nuevo dato puede:

- eliminar modelos incompatibles;
- restringir parámetros;
- reducir familias posibles;
- revelar fallos de una aproximación;
- sugerir nuevas regularidades;
- distinguir hipótesis rivales.

La conclusión correcta no es:

> «Los datos no dicen nada».

Es:

> «Los datos no seleccionan una ley sin ayuda de hipótesis, estructura y nuevas pruebas».
### 9.18. La subdeterminación es concreta, no retórica

La palabra **subdeterminación** se utiliza en filosofía de la ciencia para problemas mucho más generales.

No necesitamos adoptarla aquí como término técnico.

Nuestro resultado es completamente concreto:

$$
\{(x_i,y_i)\}_{i=1}^{n}
$$

puede ser compatible con una familia infinita de polinomios.

No estamos formulando una tesis metafísica.

Estamos exhibiendo las funciones.
### 9.19. El papel del matemático

Para un lector matemático aparece una lección importante.

La demostración de `P01` es sencilla.

La dificultad física comienza después.

La matemática nos dice:

$$
\text{hay no unicidad}.
$$

La física debe preguntar:

> ¿qué criterio permite seleccionar una familia relevante?

Es aquí donde vuelven:

- fenómeno;
- sistema;
- estado;
- idealización;
- aproximación;
- teoría;
- interpretación;
- predicción;
- experimento.

El teorema no reemplaza esas decisiones.

Las hace necesarias de manera explícita.
### 9.20. El planteamiento correcto del problema

Arnold insiste en que una contribución matemática esencial a las ciencias naturales ocurre antes del cálculo rutinario: al formular correctamente la pregunta y elegir el modelo apropiado.[@arnold2014mathematical, prefacio, p. xiii]

`P01` muestra una razón elemental para esa insistencia.

Una tabla finita no contiene instrucciones suficientes para producir automáticamente su continuación.

Debemos añadir estructura.

Así:

$$
\boxed{
\text{datos}
+
\text{elección de modelo}
\longrightarrow
\text{predicciones}.
}
$$

La elección de modelo no es una operación puramente mecánica escondida dentro del álgebra.
### 9.21. Principio metodológico

::: {.ma-block .ma-metodo #fpm-i-01-mp15}
**Principio FPM-I-01-MP15 — Ajuste exacto no implica identificación única**
Que un modelo reproduzca exactamente un conjunto finito de datos no basta para identificarlo como la única ley compatible. La selección requiere restricciones adicionales, estructura física o nuevas observaciones capaces de discriminar entre alternativas.
:::

Este principio no añade contenido al teorema.

Registra su consecuencia metodológica para el resto del libro.
### 9.22. Qué no demuestra P01

Conviene cerrar varias interpretaciones incorrectas.

#### P01 no demuestra que todas las teorías sean igualmente buenas

Los modelos pueden diferir en:
