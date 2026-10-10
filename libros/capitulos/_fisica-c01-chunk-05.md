Pero cuando sí es posible, el buen experimento no se limita a acumular datos: **busca información que discrimine**.
### 2.17. Ejemplo desarrollado 5 — Dos hipótesis sobre hojas de papel

Consideremos:

- **Hipótesis A:** el tiempo de caída depende principalmente de la masa.
- **Hipótesis B:** para hojas de masa semejante, la forma y la interacción con el aire pueden modificar fuertemente el tiempo de caída.

Diseñemos comparaciones.

#### Experimento 1
Una hoja extendida frente a la misma hoja arrugada.

La masa prácticamente no cambia; la forma sí.

Si los tiempos cambian mucho, la comparación proporciona evidencia contra una explicación puramente basada en la masa.

#### Experimento 2
Dos objetos de distinta masa pero formas muy semejantes.

Ahora variamos masa manteniendo aproximadamente la geometría.

#### Experimento 3
Repetir en un entorno con mucho menos aire.

La diferencia entre ciertos comportamientos puede reducirse.

No estamos derivando todavía una teoría de la caída. Estamos aprendiendo a **separar variables mediante diseño experimental**.
### 2.18. Control y comparación

La palabra «control» tiene varios usos en ciencia. Aquí la utilizaremos informalmente para cualquier disposición que nos ayude a atribuir diferencias observadas a un cambio específico.

Si modificamos simultáneamente diez aspectos de un experimento y el resultado cambia, será difícil saber cuál produjo el efecto.

La comparación más informativa suele intentar:

$$
\text{cambiar lo que queremos estudiar}
\quad\text{y}\quad
\text{mantener el resto suficientemente controlado}.
$$
En la práctica nunca se mantiene «todo lo demás exactamente igual». Lo que hacemos es justificar que las variaciones restantes no dominan el efecto investigado.

Esta frase —**no dominan el efecto**— anticipa el lenguaje de escalas que aprenderemos después.
### 2.19. Una observación negativa también necesita procedimiento

Supongamos que afirmamos:

> «No observamos desviación.»

La frase puede significar muchas cosas.

¿No hubo desviación exactamente? ¿O fue menor que la capacidad del instrumento para detectarla?

Una afirmación negativa debería leerse como:

> «Bajo este procedimiento y dentro de su sensibilidad, no se registró una desviación distinguible.»

Esta forma de hablar evita convertir limitaciones instrumentales en afirmaciones ontológicas.

El principio será importante en toda la física experimental.
### 2.20. Predicción observable y predicción matemática

Imaginemos que un modelo produce exactamente el número

$$
1.003847261\ldots
$$
para cierta cantidad.

El instrumento solo distingue cambios del orden de una centésima.

Entonces muchas cifras de la predicción matemática no tienen contraparte experimental accesible en ese montaje.

Aquí reaparece nuestra distinción central:

$$
\text{precisión matemática}
\not\Rightarrow
\text{precisión experimental}.
$$
Y también su recíproca:

un experimento muy preciso puede revelar que un modelo matemáticamente elegante es físicamente insuficiente.
### 2.21. El péndulo como experimento

Construyamos una ficha experimental mínima.

#### Sistema
Esfera suspendida por un hilo de un soporte.

#### Fenómeno
Oscilación después de separar la esfera de su posición de equilibrio aparente.

#### Pregunta
¿Cómo varía el tiempo de oscilación al modificar una condición determinada?

#### Observable principal
Intervalo temporal asociado a una oscilación según un procedimiento definido.

#### Procedimiento
1. fijar una marca de referencia;
2. definir un evento de inicio;
3. definir el evento final correspondiente;
4. registrar tiempo;
5. repetir.

#### Variables que podemos modificar
- longitud;
- amplitud inicial;
- masa;
- geometría del cuerpo;
- medio circundante.

#### Condiciones que intentamos controlar
- soporte;
- procedimiento de liberación;
- instrumento temporal;
- localización;
- definición de una oscilación.

Todavía no sabemos qué variables **deben** aparecer en la ley. Precisamente el experimento puede ayudarnos a descubrirlo.
### 2.22. De la observación al modelo y del modelo a la observación

La relación entre teoría y experimento no es una flecha única.

No hacemos simplemente:

$$
\text{observación}\to\text{teoría}.
$$
Tampoco:

$$
\text{teoría}\to\text{observación}.
$$
El trabajo real forma un ciclo:

$$
\boxed{
\text{observación}
\to
\text{modelo}
\to
\text{predicción}
\to
\text{nuevo experimento}
\to
\text{revisión del modelo}
}
$$
Cada vuelta puede modificar:

- qué variables consideramos;
- qué precisión necesitamos;
- qué experimento es informativo;
- qué idealización aceptamos.

Este ciclo será más importante que cualquier fórmula aislada del libro.
### 2.23. Ejercicios de §2


::: {.ma-block .ma-enunciado #fpm-i-01-e005}
**Ejercicio FPM-I-01-E005 — Definir una oscilación**

Propón dos definiciones experimentales distintas de «una oscilación completa» de un péndulo. Explica por qué ambas pueden ser válidas si se usan consistentemente.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

**Definición A:** intervalo entre dos cruces sucesivos del centro en la misma dirección.

**Definición B:** intervalo entre dos máximos sucesivos alcanzados en el mismo lado.

Ambas intentan identificar dos estados equivalentes dentro del ciclo. Pueden producir estimaciones compatibles si el movimiento es suficientemente regular y el procedimiento está bien definido.

La lección es que una magnitud experimental necesita una regla de identificación de eventos. No basta el nombre «período».
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e006}
**Ejercicio FPM-I-01-E006 — Video y calibración**

Una cámara registra una pelota que cae. El centro de la pelota aparece en la fila $420$ de la imagen.

Explica por qué el número $420$ no es todavía una altura física.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

El número $420$ es una coordenada en la matriz de imagen. Para transformarla en una altura física necesitamos, como mínimo:

- conocer la geometría de la cámara;
- establecer una escala mediante objetos de longitud conocida;
- fijar un origen;
- conocer la orientación de la imagen;
- decidir qué punto de la pelota representa su posición;
- controlar o corregir distorsiones relevantes.

Solo después puede construirse una relación `[OBS]` entre coordenada de imagen y altura.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e007}
**Ejercicio FPM-I-01-E007 — Un experimento poco discriminante**

Queremos decidir si el color de una esfera afecta el período de un péndulo.

Un estudiante reemplaza una esfera pequeña de acero pintada de rojo por una esfera grande de madera azul y encuentra una diferencia.

¿Por qué el experimento no discrimina adecuadamente la hipótesis «el color importa»?

:::

::: {.ma-block .ma-comprobacion}
**Solución**

Se modificaron simultáneamente muchas propiedades:

- color;
- material;
- masa;
- tamaño;
- geometría superficial;
- posiblemente distribución de masa.

Por tanto, aunque aparezca una diferencia, el experimento no permite atribuirla específicamente al color.

Un diseño mejor cambiaría el color manteniendo tanto como sea posible las demás propiedades relevantes, por ejemplo usando el mismo cuerpo antes y después de aplicar una capa de pintura cuyo efecto adicional se evalúe.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e008}
**Ejercicio FPM-I-01-E008 — «No vimos ningún efecto»**

Un detector puede registrar desplazamientos mayores que $1\ \mathrm{mm}$. En un experimento no registra ningún cambio.

¿Cuál de las siguientes conclusiones está justificada?

1. El desplazamiento es exactamente cero.
2. El desplazamiento, si existe, no fue distinguible con ese procedimiento.
3. La teoría que predice desplazamiento es necesariamente falsa.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

La conclusión justificada es **2**.

El resultado experimental informa sobre lo que el procedimiento puede distinguir.

No podemos inferir que el desplazamiento sea matemáticamente exactamente cero. Tampoco podemos rechazar automáticamente toda teoría que prediga un desplazamiento, porque esta podría predecir un valor inferior al umbral de detección o porque habría que revisar otros aspectos del experimento.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e009}
**Ejercicio FPM-I-01-E009 — Repetición**

Se mide cinco veces el tiempo asociado a un mismo procedimiento y se obtienen valores ligeramente distintos.

¿Por qué no es correcto escoger simplemente el valor que «parece más razonable» y descartar los otros?

:::

::: {.ma-block .ma-comprobacion}
**Solución**

Las diferencias contienen información acerca del procedimiento y del sistema.

Antes de descartar datos necesitamos criterios explícitos: fallo instrumental identificado, violación de una condición experimental, error de transcripción u otra causa justificable.

Elegir el valor preferido porque coincide mejor con una expectativa introduce un sesgo.

En `FPM-I-03` aprenderemos a resumir conjuntos de mediciones y tratar incertidumbres de forma cuantitativa.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e010}
**Ejercicio FPM-I-01-E010 — Diseñar una prueba**

Hipótesis:

> «El tiempo de oscilación de nuestro péndulo cambia apreciablemente si reemplazamos la esfera por otra de masa distinta, manteniendo lo demás igual.»

Diseña un experimento conceptual para poner a prueba la afirmación.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

Una estrategia:
