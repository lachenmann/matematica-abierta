#### Tarea A

Necesitamos una estimación cualitativa.

#### Tarea B

Queremos detectar una corrección extremadamente pequeña.

El mismo modelo puede ser excelente para A e insuficiente para B.

Por tanto, no preguntamos:

> «¿Es exacto el modelo?»

sino:

> «¿Es suficientemente adecuado para esta tarea, en este régimen y con esta precisión?»

Esto conecta directamente con:

$$
D28
$$

y:

$$
D32.
$$
La distinción también alcanza a la observación: dos resultados matemáticamente diferentes pueden quedar por debajo de la capacidad discriminante del procedimiento experimental.

El ejemplo de la órbita marciana nos dio una lección distinta.[@arnold2014mathematical, cap. 1, pp. 1–2]

Una elipse puede ser matemáticamente distinta de un círculo.

Pero para cierta excentricidad, la diferencia entre sus semiejes puede ser visualmente pequeña.

Entonces tenemos tres planos:

$$
\text{distinción matemática},
$$

$$
\text{magnitud física de la diferencia},
$$

$$
\text{capacidad observacional para detectarla}.
$$

No deben colapsarse.

Un modelo puede distinguir exactamente dos casos que un instrumento o la percepción disponible no puede separar.
Supongamos que dos modelos predicen:

$$
P_1=1.000000,
$$

$$
P_2=1.000001.
$$

La diferencia matemática es exacta:

$$
P_1\neq P_2.
$$

Pero si el procedimiento `[OBS]` solo discrimina diferencias del orden de:

$$
0.01,
$$

esa distinción no es experimentalmente accesible.

Por tanto:

$$
\boxed{
\text{distinguibilidad matemática}
\not\Rightarrow
\text{distinguibilidad física disponible}.
}
$$

La exactitud del formalismo no puede sustituir la resolución del experimento.
### 13.3. Dos principios permanentes

::: {.ma-block .ma-metodo #fpm-i-01-mp21}
**Principio FPM-I-01-MP21 — La exactitud matemática no repara una representación física inadecuada**
Una derivación exacta puede garantizar que la conclusión se sigue de las premisas del modelo; no puede garantizar por sí sola que esas premisas representen adecuadamente el sistema real, la pregunta o el régimen considerado.
:::

En forma condensada:

$$
\boxed{
\text{corrección formal}
\not\Rightarrow
\text{adecuación física}.
}
$$

Este principio permanecerá activo en todo el tratado.
::: {.ma-block .ma-metodo #fpm-i-01-mp22}
**Principio FPM-I-01-MP22 — Una aproximación controlada puede ser físicamente superior a una solución exacta de un modelo inadecuado**
Al comparar descripciones físicas, la exactitud matemática de la solución debe evaluarse junto con la adecuación del modelo y su régimen. Una aproximación cuyas omisiones y límites están controlados puede representar mejor el fenómeno que una solución exacta obtenida de premisas físicamente inadecuadas.
:::

Este principio resume la tensión central de §13.
La consecuencia editorial y metodológica es importante: el texto debe declarar dónde se ha aproximado y qué relación permanece exacta dentro del modelo simplificado.

Supongamos que declaramos:

$$
[\mathrm{APPROX}]
\qquad
F(x)\approx G(x).
$$

Después definimos un modelo simplificado usando:

$$
G(x).
$$

Dentro de ese modelo simplificado podemos obtener exactamente:

$$
H=2G(x).
$$

No hay contradicción entre:

$$
F\approx G
$$

y:

$$
H=2G.
$$

La primera relación compara dos niveles de descripción.

La segunda es una igualdad exacta **dentro del modelo simplificado**.

Este es un patrón que aparecerá continuamente en física.
El protocolo de §6 permite mantener la jerarquía visible.

Por ejemplo:

$$
[\mathrm{APPROX}]
\qquad
F\approx G,
$$

seguido de:

$$
[\mathrm{MATH}]
\qquad
G=K,
$$

no autoriza escribir sin comentario:

$$
F=K.
$$

La cadena correcta conserva el estatus:

$$
F\approx G=K,
$$

y por tanto:

$$
F\approx K
$$

en el régimen pertinente.

La sintaxis matemática también debe reflejar la epistemología del argumento.
Como cierre operativo, cualquier cálculo físico debe auditar corrección, estatus, admisibilidad, régimen, observabilidad y adecuación:

#### Lista de control

Cada vez que obtengamos un resultado, seguiremos este orden.

#### 1. Corrección lógica

> ¿La conclusión se sigue de las premisas?

#### 2. Corrección algebraica

> ¿Las operaciones matemáticas se realizaron correctamente?

#### 3. Estatus

> ¿Qué pasos eran `[MATH]`, `[MOD]` o `[APPROX]`?
