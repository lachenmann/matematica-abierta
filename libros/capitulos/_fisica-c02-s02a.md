## §2 — Magnitudes, clases de magnitudes y referencias {#fpm-i-02-s02}

### 2.1. Antes de comparar números, debemos saber qué estamos comparando

En §1 distinguimos cuatro niveles:

$$
\text{magnitud}
\neq
\text{valor de magnitud}
\neq
\text{valor numérico}
\neq
\text{unidad}.
$$

Ahora aparece una pregunta anterior incluso a la elección de unidad:

> ¿Cuándo tiene sentido decir que dos magnitudes pueden compararse entre sí?

Consideremos las expresiones:

$$
5\,\mathrm m
$$

y

$$
8\,\mathrm m.
$$

Podemos preguntar cuál longitud es mayor, calcular su diferencia o formar, cuando el contexto lo permite, el cociente entre ambas.

Pero comparemos ahora:

$$
5\,\mathrm m
$$

y

$$
8\,\mathrm s.
$$

Los números $5$ y $8$ sí son comparables como números.

Las magnitudes físicas representadas no lo son de la misma manera.

No tiene sentido físico ordinario afirmar:

$$
5\,\mathrm m<8\,\mathrm s.
$$

La dificultad no está en los números.

Está en que representan **clases distintas de magnitudes**.

Ésta es una de las primeras restricciones estructurales que la física impone al álgebra que usamos para describirla.

### 2.2. Tipo de magnitud

El Vocabulario Internacional de Metrología introduce la noción de *kind of quantity* como el aspecto común a magnitudes mutuamente comparables.[^s2-vim-kind]

Adoptaremos una formulación operativa compatible con esa idea.

::: {.ma-block .ma-definicion #fpm-i-02-d05}
**Definición 5 — Tipo de magnitud**
Un **tipo de magnitud** es la clase determinada por el aspecto cuantificable común que hace mutuamente comparables ciertas magnitudes físicas.
:::

Ejemplos de magnitudes que normalmente consideramos del mismo tipo son:

- el diámetro de una esfera;
- la longitud de una cuerda;
- la longitud de onda de cierta radiación;
- la distancia entre dos puntos.

Todas pertenecen al tipo de magnitud:

$$
\boxed{\text{longitud}.}
$$

En cambio, una longitud y una masa no pertenecen al mismo tipo.

La clasificación no depende de que los valores numéricos coincidan.

Podemos tener:

$$
L=5\,\mathrm m
$$

y

$$
T=5\,\mathrm s.
$$

Entonces:

$$
\{L\}_{\mathrm m}=5
$$

y

$$
\{T\}_{\mathrm s}=5,
$$

pero la igualdad entre los números no convierte longitud y duración en la misma magnitud física.

Por tanto:

$$
\boxed{
\text{mismo valor numérico}
\not\Rightarrow
\text{mismo tipo de magnitud}.
}
$$

### 2.3. Una clase física precede a la elección de unidad

En §1 escribimos:

$$
Q=q\,u.
$$

Esa escritura tiene una condición silenciosa que ahora debemos hacer explícita:

$$
Q
$$

y

$$
u
$$

deben pertenecer al mismo tipo de magnitud.

No podemos usar un segundo como unidad de una longitud ni un metro como unidad de una masa.

La unidad no crea el tipo de magnitud.

Lo presupone.

La secuencia conceptual correcta es:

$$
\boxed{
\text{tipo de magnitud}
\longrightarrow
\text{elección de una referencia compatible}
\longrightarrow
\text{valor numérico}.
}
$$

No:

$$
\boxed{
\text{número}
\longrightarrow
\text{adición posterior de una etiqueta de unidad}.
}
$$

Este orden será esencial cuando estudiemos dimensiones.

### 2.4. La unidad como cantidad de referencia del mismo tipo

El VIM define una unidad de medida como una cantidad escalar real, adoptada por convención, con la cual puede compararse cualquier otra cantidad del mismo tipo para expresar la razón entre ambas como un número.[^s2-vim-unit]

Ésta es la estructura que ya utilizábamos implícitamente en §1.

Si $u$ es una unidad del mismo tipo que $Q$, escribimos:

$$
Q=q\,u.
$$

Entonces:

$$
q=\frac{Q}{u}.
$$

La división tiene aquí una interpretación física precisa: estamos preguntando cuántas veces la referencia $u$ entra, en sentido de razón, en la magnitud $Q$.

Por ejemplo:

$$
L=2.5\,\mathrm m
$$

puede leerse como:

$$
\frac{L}{1\,\mathrm m}=2.5.
$$

El metro no es un comentario sobre el número $2.5$.

Es la referencia que permite producir ese número a partir de una magnitud de longitud.

### 2.5. Comparabilidad no significa identidad física

Que dos magnitudes sean del mismo tipo no significa que sean la misma magnitud particular.

La longitud de una mesa y la longitud de una habitación pueden compararse porque ambas son longitudes.

Pero son propiedades de sistemas diferentes.

Podemos escribir:

$$
L_{\mathrm{mesa}}=1.8\,\mathrm m
$$

y

$$
L_{\mathrm{habitación}}=4.5\,\mathrm m.
$$

Entonces tiene sentido formar:

$$
\frac{L_{\mathrm{habitación}}}{L_{\mathrm{mesa}}}
=
\frac{4.5\,\mathrm m}{1.8\,\mathrm m}
=
2.5.
$$

La razón es numérica porque se canceló una referencia común de longitud.

Pero esto no elimina la diferencia entre los objetos físicos representados.

Debemos distinguir:

$$
\boxed{
\text{mismo tipo}
\neq
\text{misma magnitud particular}
\neq
\text{mismo valor}.
}
$$

### 2.6. El tipo de magnitud tampoco está determinado por el símbolo algebraico

Supongamos que en dos problemas distintos aparece la letra:

$$
x.
$$

En un problema $x$ puede representar una posición.

En otro, una fracción sin unidad.

En un tercero, un tiempo reescalado.

La letra no determina la clase física del objeto.

El significado procede del modelo y del diccionario de interpretación introducido en el capítulo 1.

Por tanto:

$$
\boxed{
\text{misma letra}
\not\Rightarrow
\text{mismo tipo de magnitud}.
}
$$

Esto es una razón adicional para no manipular fórmulas físicas como si fueran expresiones algebraicas descontextualizadas.

### 2.7. ¿Basta la expresión de unidad para identificar el tipo?

Tampoco.

Éste es un punto más sutil.

El VIM advierte que dos tipos de magnitud diferentes pueden compartir la misma expresión de unidad.[^s2-vim-unit]

Por ejemplo, tanto la **capacidad calorífica** como la **entropía** pueden expresarse mediante:

$$
\mathrm{J/K}.
$$

Sin embargo, no se consideran generalmente magnitudes del mismo tipo.

Otro ejemplo especialmente instructivo utiliza:

$$
\mathrm{s}^{-1}.
$$

Una frecuencia puede expresarse con esa estructura de unidad y una actividad radiactiva también.

El SI utiliza nombres especiales distintos:

$$
1\,\mathrm{Hz}=1\,\mathrm{s}^{-1}
$$

para frecuencia, y:

$$
1\,\mathrm{Bq}=1\,\mathrm{s}^{-1}
$$

para actividad de radionúclidos.

La igualdad de las expresiones algebraicas de unidad no significa identidad del concepto físico.

Por tanto:

$$
\boxed{
\text{misma expresión de unidad}
\not\Rightarrow
\text{mismo tipo de magnitud}.
}
$$

Todavía no hemos definido formalmente la dimensión física.

En §5 veremos una versión más profunda de esta advertencia:

> tener la misma dimensión tampoco basta para ser la misma clase de magnitud.

### 2.8. La física de una cantidad no cabe entera en sus unidades

La observación anterior tiene una consecuencia metodológica importante.

Consideremos una expresión como:

$$
3\,\mathrm{s}^{-1}.
$$

Sin información adicional, no sabemos todavía si representa:

- una frecuencia;
- una actividad radiactiva;
- alguna otra tasa inversa de tiempo.

La unidad restringe el significado posible.

No lo determina completamente.

Necesitamos además:

- qué sistema estudiamos;
- qué observable se representa;
- cómo se define esa magnitud en el modelo;
- qué procedimiento `[OBS]` la conecta con datos.

Así reaparece la tesis de el capítulo 1:

$$
\boxed{
\text{formalismo}
+
\text{interpretación física}
}
$$

son inseparables.

### 2.9. Comparar, ordenar, restar y formar razones

Cuando dos valores pertenecen al mismo tipo de magnitud, ciertas operaciones adquieren sentido natural.

Si:

$$
L_1=2\,\mathrm m
$$

y:

$$
L_2=5\,\mathrm m,
$$

podemos comparar:

$$
L_1<L_2,
$$

restar:

$$
L_2-L_1=3\,\mathrm m,
$$

y formar la razón:

$$
\frac{L_2}{L_1}=\frac52.
$$

En cambio, la expresión:

$$
L_2-T
$$

con $T$ una duración no representa, sin una construcción física adicional, una magnitud ordinaria definida por resta.

La regla no debe formularse de manera excesivamente fuerte.

La física sí construye nuevas magnitudes combinando clases diferentes mediante productos y cocientes. Por ejemplo, más adelante aparecerán magnitudes cuya unidad contiene longitud dividida por tiempo.

Lo que no podemos hacer es **sumar o comparar por orden magnitudes de tipos incompatibles como si fueran homogéneas**.

La combinación multiplicativa será objeto de §4.

### 2.10. Comparabilidad y ecuaciones físicas

Supongamos que alguien propone:

$$
L_1=L_2+T.
$$

Antes de preguntar si la ecuación describe algún fenómeno real, ya tenemos un problema semántico:

- $L_1$ es una longitud;
- $L_2$ es una longitud;
- $T$ es una duración.

La suma:

$$
L_2+T
$$

no está definida como suma de magnitudes del mismo tipo.

No necesitamos conocer todavía análisis dimensional para detectar el problema.

La incompatibilidad aparece ya en el nivel de los tipos de magnitud.

En §6 convertiremos esta intuición en una prueba sistemática mediante homogeneidad dimensional.

### 2.11. Primera regla metodológica de §2

::: {.ma-block .ma-metodo #fpm-i-02-mp03}
**Principio 3 — La comparabilidad física precede a la comparación numérica**
Antes de comparar, sumar o interpretar conjuntamente valores numéricos, debe establecerse qué magnitudes representan y si las operaciones propuestas son compatibles con sus tipos de magnitud.
:::

Esto evita errores como:

$$
3\,\mathrm m+4\,\mathrm s=7.
$$

El problema no consiste en que $3+4\neq7$.

De hecho:

$$
3+4=7.
$$

El problema es que la operación física propuesta no está bien tipada.

### 2.12. La palabra «referencia» es más amplia que «unidad»

Hasta ahora hemos trabajado casi exclusivamente con valores del tipo:

$$
Q=q\,u.
$$

Pero el VIM define un valor de magnitud de manera más general como la combinación de un número y una referencia.[^s2-vim-value]

En muchos casos, esa referencia es una unidad de medida.

Sin embargo, el VIM contempla también valores cuya referencia se da mediante:

- un procedimiento de medida especificado;
- un material de referencia.

Por ejemplo, determinadas escalas de dureza dependen de un procedimiento convencional, y algunas magnitudes de laboratorio pueden expresarse respecto de materiales de referencia internacionalmente establecidos.

No desarrollaremos aquí esas ramas de la metrología.

Pero debemos conservar la distinción conceptual.

::: {.ma-block .ma-definicion #fpm-i-02-d06}
**Definición 6 — Referencia de un valor de magnitud**
Una **referencia de un valor de magnitud** es el elemento convencional respecto del cual el número asociado adquiere significado cuantitativo. En las magnitudes tratadas ordinariamente en este capítulo, la referencia será normalmente una unidad de medida; en contextos metrológicos más generales puede ser también un procedimiento o un material de referencia.
:::

Por tanto:

$$
\boxed{
\text{unidad}
\subset
\text{clase más amplia de referencias usadas para expresar valores}.
}
$$

La expresión anterior es conceptual: no afirma una inclusión conjuntista formal entre objetos metrológicos.

### 2.13. Por qué en física elemental podemos concentrarnos en unidades

La mayor parte de las magnitudes de este tratado —longitud, masa, tiempo, velocidad, aceleración, energía, carga, temperatura termodinámica— se manipularán mediante unidades.

Por eso nuestra notación principal seguirá siendo:

$$
Q=\{Q\}_u\,u.
$$

La ampliación de §2.12 cumple otra función:

> impedir que confundamos una convención pedagógica útil con la definición más general de valor de magnitud.

En otras palabras:

$$
\boxed{
\text{nuestro cálculo con unidades es central}
\quad
\text{pero no agota toda la metrología}.
}
$$

La teoría sistemática de medición, incertidumbre y trazabilidad pertenece a el capítulo 3 y a tratamientos metrológicos especializados.

### 2.14. Una unidad no es cualquier cantidad elegida informalmente

Podemos comparar una mesa con otra mesa y obtener una razón de longitudes.

Pero eso no convierte automáticamente la longitud de la segunda mesa en una **unidad de medida** institucionalizada.

Para que una referencia funcione como unidad necesitamos una adopción convencional suficientemente clara y una forma de identificar o realizar esa referencia.

En un ejercicio escolar podemos decir:

> «Tomemos esta barra como una unidad provisional de longitud».

Eso construye un modelo sencillo de comparación.

Pero el SI contemporáneo requiere una estructura metrológica mucho más precisa, que estudiaremos en §3.

La diferencia es:

$$
\boxed{
\text{usar algo como referencia local}
\neq
\text{definir una unidad dentro de un sistema internacional de unidades}.
}
$$

### 2.15. El símbolo de cantidad debe permanecer físicamente estable

Volvamos a una longitud particular $L$.

Podemos escribir:

$$
L=2\,\mathrm m
$$

o:

$$
L=200\,\mathrm{cm}.
$$

La elección de unidad cambia:

$$
\{L\}_{\mathrm m}=2,
$$

$$
\{L\}_{\mathrm{cm}}=200.
$$

Pero la cantidad representada sigue siendo $L$.

Conviene por tanto que nuestra notación separe:

$$
L
$$

de:

$$
\{L\}_u.
$$

El primero representa la magnitud física particular.

El segundo representa el número que obtenemos al expresarla respecto de una unidad concreta.

Esto nos permitirá más adelante distinguir entre:

- **ecuaciones entre magnitudes**;
- **ecuaciones entre valores numéricos**.

La primera clase tiene un grado de independencia respecto de la elección de unidad que la segunda puede no tener.

### 2.16. Mismo fenómeno, magnitudes diferentes

Un solo sistema físico puede portar muchas magnitudes diferentes.

Consideremos una barra.

Podemos asociarle:

- una longitud;
- una masa;
- una temperatura;
- una velocidad, si se mueve;
- una energía, según el modelo considerado.

No debemos pensar que «la barra tiene un número».

Tiene múltiples propiedades cuantificables, cada una perteneciente a un tipo diferente y cada una necesitada de una referencia apropiada.

La estructura correcta es:

$$
\boxed{
\text{sistema físico}
\longrightarrow
\text{familia de magnitudes seleccionadas por el modelo}.
}
$$

Esto vuelve a conectar el capítulo con el concepto de observable de el capítulo 1.
