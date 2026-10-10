Puede ser útil si queremos tratar la interacción esfera–Tierra como interna al sistema, por ejemplo en una contabilidad global de intercambios.

No hay una frontera universalmente correcta. La justificación depende de la pregunta.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e012}
**Ejercicio FPM-I-01-E012 — Cinco Tierras**

**Familia:** `E-MOD / CORE`

Elige entre los modelos **plano local**, **esfera**, **geoide/elipsoide**, **cuerpo extenso en rotación** y **masa puntual** para las siguientes preguntas:

a) posiciones dentro de una cancha;  
b) navegación intercontinental;  
c) geodesia de alta precisión;  
d) efectos asociados a la rotación terrestre;  
e) primera aproximación a la interacción gravitatoria con un objeto muy lejano.

Justifica cada elección.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

a) **Plano local.** La curvatura es irrelevante para la precisión ordinaria de una cancha.

b) **Esfera.** La curvatura global afecta distancias y rutas.

c) **Geoide/elipsoide.** La forma real necesita mayor precisión que una esfera.

d) **Cuerpo extenso en rotación.** Debemos conservar orientación y rotación.

e) **Masa puntual**, bajo un régimen en el que la estructura interna y el tamaño sean despreciables para la pregunta.

La solución muestra que el mismo objeto físico puede exigir distintos espacios de estados y parámetros según el modelo.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e013}
**Ejercicio FPM-I-01-E013 — Estado, parámetro u observable**

**Familia:** `E-CON / CORE`

En cada caso clasifica la cantidad por su **rol principal dentro del modelo indicado**.

1. La longitud fija $\ell$ de un péndulo ideal durante una serie de oscilaciones.
2. La posición instantánea de la esfera.
3. La lectura temporal obtenida por un sensor.
4. La longitud de un hilo elástico cuando precisamente estudiamos su estiramiento.
5. La masa de una esfera medida antes del experimento y tratada después como fija.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

1. **Parámetro.** Se fija para esa realización.
2. **Variable de estado.** Ayuda a distinguir estados.
3. **Dato asociado a un observable.** Es un resultado del procedimiento de medición.
4. **Variable de estado** en ese modelo, porque cambia durante el proceso estudiado.
5. **Parámetro** dentro del modelo dinámico, aunque su valor haya sido obtenido mediante una observación previa.

La pregunta se refiere al rol en el modelo, no a una naturaleza absoluta de la magnitud.
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e014}
**Ejercicio FPM-I-01-E014 — Una observación no determina el estado**

**Familia:** `E-PROOF / BASIC`

Sea un modelo con estados

$$
s=(q_1,q_2)\in\mathbb R^2
$$
y un observable

$$
O(s)=q_1+q_2.
$$
a) Encuentra dos estados distintos con el mismo valor $O=5$.  
b) Explica qué demuestra este ejemplo acerca de la reconstrucción de un estado a partir de una sola observación.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

a) Por ejemplo,

$$
s_1=(2,3),\qquad s_2=(1,4).
$$
Son estados distintos porque

$$
s_1\neq s_2,
$$
pero

$$
O(s_1)=2+3=5,
$$
y

$$
O(s_2)=1+4=5.
$$
b) La aplicación $O$ no es inyectiva. Por tanto, conocer un único valor observable no permite distinguir todos los estados del modelo.

Físicamente:

$$
\boxed{\text{mismo dato observable}\not\Rightarrow\text{mismo estado}}
$$
a menos que tengamos información adicional que garantice una correspondencia unívoca.
:::

### 3.17. Síntesis

La frontera de un sistema, su estado y sus observables no vienen determinados por el objeto material considerado aisladamente.

Dependen de la pregunta y del modelo.

Hemos construido ahora la cadena

$$
\boxed{
\text{pregunta}
\to
\text{sistema/entorno}
\to
\text{estado}
\to
\text{variables y parámetros}
\to
\text{observables}
\to
\text{datos}
}.
$$
También hemos aprendido cuatro distinciones que reaparecerán continuamente:

$$
\boxed{
\text{sistema}\neq\text{entorno}
}
$$
$$
\boxed{
\text{estado}\neq\text{observación individual}
}
$$
$$
\boxed{
\text{variable de estado}\neq\text{parámetro}
}
$$
y

$$
\boxed{
\text{observable}\neq\text{dato}.
}
$$
La siguiente pregunta es inevitable.

Para obtener un modelo manejable hemos omitido estructura real, sustituido objetos por representaciones simplificadas y, en ocasiones, reemplazaremos relaciones exactas por otras más simples.

Pero esas operaciones no son todas iguales.

La sección siguiente distinguirá cuidadosamente:

$$
\boxed{
\text{abstracción}
\neq
\text{idealización}
\neq
\text{aproximación}.
}
$$

---

## 4. Idealización, abstracción y aproximación {#fpm-i-01-s04}

### 4.1. Tres operaciones que no debemos confundir

En las secciones anteriores hemos construido modelos seleccionando sistemas, variables, parámetros y observables. Para hacerlo hemos simplificado.

Pero **simplificar** no nombra una sola operación.

Cuando decimos que una esfera se representa mediante un punto, que ignoramos el color de una pelota o que reemplazamos una expresión por otra numéricamente cercana, estamos haciendo cosas conceptualmente distintas.

En este libro distinguiremos tres operaciones:

$$
\boxed{
\text{abstracción}
\neq
\text{idealización}
\neq
\text{aproximación}.
}
$$
La separación será importante porque cada una exige una pregunta de control diferente.

- Ante una **abstracción** preguntaremos:  
  **¿qué estructura conservamos y qué particularidades dejamos fuera?**

- Ante una **idealización** preguntaremos:  
  **¿qué propiedad imposible o límite estamos suponiendo exactamente?**

- Ante una **aproximación** preguntaremos:  
  **¿qué diferencia estamos despreciando, comparada con qué, y en qué régimen?**

Estas tres preguntas reaparecerán durante los cuatro tomos.
### 4.2. Abstracción: conservar estructura y olvidar particulares

Consideremos tres objetos:

- una esfera metálica;
- una pelota de goma;
- una piedra redondeada.

Para una pregunta acerca de su color, debemos distinguirlos.

Para una pregunta acerca de su volumen, quizá debamos conservar forma y tamaño.

Para una primera pregunta sobre la trayectoria de sus centros, podríamos representar los tres mediante posiciones en el espacio y olvidar temporalmente color, textura y composición.

::: {.ma-block .ma-definicion #fpm-i-01-d13}
**Definición operativa FPM-I-01-D13 — Abstracción**
Una **abstracción** es la operación mediante la cual seleccionamos ciertas relaciones, propiedades o estructuras como relevantes para una pregunta y dejamos de representar explícitamente otras particularidades del sistema.
:::

Abstraer no significa afirmar que las propiedades omitidas sean nulas.

Si en un problema representamos una pelota únicamente por su posición, no estamos afirmando que no tenga color o temperatura.

Estamos diciendo que esas propiedades **no forman parte de la descripción actual**.

En forma esquemática:

$$
\text{sistema concreto}
\longrightarrow
\text{estructura seleccionada}.
$$
La flecha pierde información deliberadamente.
### 4.3. Abstracción no significa falsificación

Un mapa vial omite la composición química del asfalto. Esa omisión no convierte al mapa en falso.

Una lista de temperaturas de una ciudad omite la forma de cada edificio. Tampoco por ello es falsa.

El criterio es funcional:

> ¿la estructura conservada es la que necesitamos para responder la pregunta?

Podemos llamar a esta idea **pérdida controlada de información**.

No toda pérdida es aceptable.

Si queremos estudiar cómo gira un cuerpo rígido, abstraer toda información acerca de su orientación destruiría precisamente la estructura que necesitamos.

::: {.ma-block .ma-metodo #fpm-i-01-mp07}
**Principio FPM-I-01-MP07 — Una abstracción es adecuada si conserva las distinciones relevantes para la pregunta**
Omitir información es legítimo solo en la medida en que las distinciones eliminadas no sean necesarias para las predicciones, comparaciones o explicaciones que el modelo pretende realizar.
:::

### 4.4. Idealización: introducir un objeto que no existe exactamente

La idealización hace algo más fuerte.

Pensemos en una **partícula puntual**.

Un cuerpo material ocupa una región del espacio. Una partícula puntual, en cambio, se representa como si toda la estructura espacial relevante estuviera concentrada en un punto.

No hemos simplemente dejado de hablar del radio.

Hemos reemplazado el cuerpo por un objeto con una propiedad exacta que ningún cuerpo macroscópico posee literalmente: extensión espacial nula.

::: {.ma-block .ma-definicion #fpm-i-01-d14}
**Definición operativa FPM-I-01-D14 — Idealización**
Una **idealización** sustituye un sistema o una de sus propiedades por un objeto, condición o comportamiento simplificado que se trata como exacto dentro del modelo, aunque no se realice exactamente en el sistema físico.
:::

Ejemplos típicos:

- partícula puntual;
- hilo sin masa;
- cuerpo perfectamente rígido;
- superficie sin rozamiento;
- gas ideal;
- lente infinitamente delgada;
- campo exactamente uniforme;
- recipiente perfectamente aislado.

La marca conceptual es:

$$
\boxed{\text{«exacto en el modelo» no significa «exacto en el mundo».}}
$$
### 4.5. Una idealización puede ser excelente sin ser literalmente realizable

Supongamos que modelamos una esfera pequeña como partícula puntual.

Si la pregunta concierne a una trayectoria cuya escala espacial es enorme comparada con el tamaño de la esfera, la estructura interna puede tener un efecto despreciable sobre la cantidad que queremos calcular.

Entonces la idealización puede ser extraordinariamente útil.
