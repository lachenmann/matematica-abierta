- una posición respecto de referencias definidas;
- un intervalo temporal;
- una masa determinada por un procedimiento de pesaje;
- una temperatura indicada por un instrumento calibrado;
- el número de eventos detectados en cierto intervalo.

La palabra «conecta» evita una simplificación importante.

No siempre «leemos directamente» una propiedad de la naturaleza. Muchas veces inferimos una cantidad mediante una cadena:

$$
\text{sistema}
\to
\text{interacción con instrumento}
\to
\text{señal}
\to
\text{procesamiento}
\to
\text{valor registrado}.
$$
Por ejemplo, una cámara digital no entrega «posición» en metros. Produce datos en una matriz de detectores. Para convertirlos en posiciones físicas necesitamos calibración, geometría y convenciones.
### 2.6. Microcaso: una pelota que cae

Queremos estudiar la caída de una pelota.

Parece obvio qué observar: «la altura».

Pero debemos construirla.

#### Opción A — Marcas sobre una pared

Colocamos referencias de altura y registramos visualmente la posición.

#### Opción B — Video

Filmamos la caída y relacionamos píxeles con una escala física.

#### Opción C — Barreras ópticas

Colocamos sensores a alturas determinadas y registramos los instantes de paso.

Cada método produce datos de forma diferente.

Esto tiene consecuencias:

- los procedimientos pueden tener resoluciones distintas;
- pueden perturbar el sistema de manera diferente;
- requieren distintas calibraciones;
- pueden definir de manera ligeramente distinta el evento «la pelota está a altura $h$».

La variable matemática «altura» no llega al experimento sin mediación.
### 2.7. ¿Qué observar en la caída?

Imaginemos ahora que soltamos dos hojas de papel, una extendida y otra arrugada.

Podemos registrar:

- tiempo de caída;
- orientación;
- forma;
- velocidad del aire;
- trayectoria lateral;
- rotación.

Si solo registramos el instante en que tocan el suelo, quizá concluyamos que una cae más rápido.

Pero esa conclusión no nos dice por sí sola **por qué**.

Podrían importar:

- la resistencia del aire;
- la geometría;
- las corrientes;
- el procedimiento de liberación.

El experimento necesita entonces distinguir hipótesis.

Esto nos lleva a una idea más fuerte que la mera observación.
### 2.8. Experimento

::: {.ma-block .ma-definicion #fpm-i-01-d06}
**Definición operativa FPM-I-01-D06 — Experimento**
Un **experimento** es una disposición o intervención controlada diseñada para producir observaciones que permitan estimar cantidades, comparar comportamientos o discriminar entre hipótesis.
:::

La palabra «controlada» no significa que absolutamente todo esté bajo control.

Significa que intentamos:

- fijar ciertas condiciones;
- variar otras;
- registrar qué se hizo;
- establecer qué diferencias entre resultados pueden atribuirse razonablemente a los cambios introducidos.

Un experimento no es simplemente «hacer algo y mirar qué ocurre».
### 2.9. Ejemplo desarrollado 3 — Diseñar una comparación

Pregunta:

> ¿Influye de manera apreciable la amplitud inicial en el tiempo de oscilación de nuestro péndulo?

No responderemos todavía con una fórmula. Diseñaremos el razonamiento experimental.

#### Paso 1 — Identificar lo que variaremos

Variamos la posición inicial del cuerpo.

#### Paso 2 — Identificar lo que intentaremos mantener fijo

- mismo péndulo;
- mismo punto de suspensión;
- misma definición de período;
- mismo procedimiento temporal;
- condiciones ambientales tan semejantes como sea razonable.

#### Paso 3 — Definir grupos de observaciones

Realizamos varias mediciones para distintas amplitudes iniciales.

#### Paso 4 — Evitar una conclusión prematura

Si obtenemos valores diferentes, todavía debemos preguntar:

- ¿las diferencias son mayores que la variación propia del procedimiento?;
- ¿cambiamos inadvertidamente otra condición?;
- ¿el modo de soltar el péndulo introduce perturbaciones?;
- ¿el instrumento permite distinguir la diferencia?

Estas preguntas pertenecen a la estructura experimental, no a la solución matemática de una ecuación.
### 2.10. Observación y teoría no son mundos aislados

Podría parecer que primero existen «datos puros» y después una teoría se limita a explicarlos.

La situación real es más sutil.

Para producir un dato ya utilizamos conceptos:

- elegimos qué cuenta como evento;
- decidimos qué magnitud registrar;
- elegimos un instrumento;
- aplicamos una calibración;
- organizamos señales según un procedimiento.

Esto no significa que los datos sean arbitrarios o que una teoría pueda imponer cualquier resultado. Significa que la conexión entre mundo y representación posee estructura.

En este libro la indicaremos con la etiqueta:

$$
[\mathrm{OBS}]
$$
para relaciones que especifican cómo una cantidad del modelo se conecta con un procedimiento de observación.

Por ejemplo:

::: {.ma-block .ma-dominio}
$$
[\mathrm{OBS}]
$$
«La coordenada registrada de la esfera se obtiene convirtiendo la posición de su centro en la imagen mediante una calibración espacial previamente fijada.»
:::

No es todavía una ecuación universal; es una **regla de conexión** entre aparato y modelo.
### 2.11. Repetición: ¿por qué medir más de una vez?

Si repetimos un procedimiento aparentemente idéntico, rara vez obtenemos resultados numéricamente idénticos con precisión ilimitada.

Puede haber diferencias debidas a:

- resolución del instrumento;
- variaciones del ambiente;
- pequeñas diferencias en las condiciones iniciales;
- ruido;
- fluctuaciones físicas;
- intervención humana;
- cambios del propio sistema.

Todavía no clasificaremos formalmente estas variaciones. Ese trabajo corresponde a `FPM-I-03`.

Pero sí fijaremos una norma:

::: {.ma-block .ma-metodo #fpm-i-01-mp04}
**Principio FPM-I-01-MP04 — Una observación aislada no caracteriza por sí sola la estabilidad de un procedimiento**
Cuando la pregunta exige comparar o estimar una magnitud, debemos considerar si el resultado persiste al repetir el procedimiento bajo condiciones declaradas.
:::

### 2.12. Repetibilidad y reproducibilidad: primera aproximación

Usaremos dos palabras de manera preliminar.

#### Repetibilidad

Preguntamos si un procedimiento produce resultados compatibles cuando se repite bajo condiciones tan semejantes como sea posible.

#### Reproducibilidad

Preguntamos si el resultado se mantiene cuando cambia razonablemente el realizador, el instrumento, el laboratorio o alguna parte del procedimiento, según el tipo de afirmación que se quiere sostener.

No fijaremos todavía definiciones metrológicas internacionales precisas. Nos basta comprender la diferencia conceptual:

- repetir es volver a hacer algo en condiciones cercanas;
- reproducir pone a prueba si el resultado sobrevive a cambios controlados del contexto experimental.
### 2.13. Un dato necesita contexto

Supongamos que encontramos escrito:

$$
T=2.01.
$$
¿Es un dato físico?

No todavía.

Falta saber:

- qué representa $T$;
- en qué unidades está expresado;
- cómo se obtuvo;
- qué sistema se midió;
- bajo qué condiciones;
- con qué procedimiento;
- con qué precisión.

Un número descontextualizado no es un resultado experimental completo.

Incluso

$$
T=2.01\ \mathrm{s}
$$
sigue siendo insuficiente para muchas preguntas.

La física no opera con números desnudos, sino con resultados insertos en procedimientos y modelos.
### 2.14. El papel del instrumento

Un instrumento físico es también un sistema físico.

Un reloj puede atrasarse. Una regla se expande térmicamente. Un sensor tiene umbral. Una cámara posee distorsión. Un detector puede dejar de registrar ciertos eventos.

Por eso, cuando conectamos una variable teórica con una observación, incorporamos indirectamente un modelo del instrumento.

No siempre necesitaremos describir ese modelo con detalle. Pero debemos recordar que existe.

Esta idea será crucial mucho más adelante. En mecánica cuántica, por ejemplo, el problema de la medición no podrá tratarse como un simple detalle administrativo.

Aquí solo sembramos el hábito:

> **¿Qué interacción física convierte la propiedad que quiero conocer en la señal que efectivamente registro?**
### 2.15. Ejemplo desarrollado 4 — Medir el período sin cronómetro perfecto

Imaginemos que nuestro cronómetro tiene una resolución limitada.

En vez de medir una sola oscilación, podemos medir el tiempo de diez oscilaciones y luego dividir por diez.

Si el tiempo total registrado es $T_{10}$, definimos

$$
[\mathrm{DEF}]
\qquad
\overline T:=\frac{T_{10}}{10}.
$$
¿Por qué podría ayudar?

Porque ciertos errores asociados al inicio y al final de la medición pueden representar una fracción menor del tiempo total cuando observamos muchas oscilaciones.

No cuantificaremos aún esta mejora; eso corresponde al capítulo de incertidumbre.

Lo importante ahora es metodológico:

> el diseño del procedimiento de observación puede cambiar la calidad de la información obtenida.

La medición no es una ventana transparente e indiferente.
### 2.16. Experimentos que discriminan hipótesis

Supongamos que dos explicaciones predicen lo mismo para todas las situaciones que hemos observado.

Entonces los datos disponibles no permiten distinguirlas.

Necesitamos una situación en la que sus predicciones difieran.

Esta es una función fundamental del experimento:

$$
\boxed{
\text{diseñar condiciones en las que hipótesis rivales produzcan consecuencias distinguibles}
}
$$
No siempre es posible. Algunas hipótesis pueden ser empíricamente indistinguibles dentro del régimen accesible.
