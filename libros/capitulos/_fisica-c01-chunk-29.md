### 13.2. Exactitud de la solución y calidad del modelo

Supongamos que tenemos dos opciones.

#### Modelo A

Representa muy pobremente el sistema real, pero podemos resolverlo exactamente.

#### Modelo B

Representa mejor el fenómeno relevante, aunque para obtener una predicción usemos una aproximación controlada.

Podría ocurrir que:

$$
P_A
$$

sea exacta respecto de A, mientras:

$$
P_B
$$

sea aproximada respecto de B.

Y, sin embargo:

$$
P_B
$$

puede describir mucho mejor la observación física.

Por tanto:

$$
\boxed{
\text{resultado matemáticamente aproximado}
\not\Rightarrow
\text{descripción físicamente peor}.
}
$$
Debemos distinguir al menos dos lugares donde puede aparecer una aproximación.

#### Aproximación en la construcción del modelo

Por ejemplo:

$$
[\mathrm{MOD}]
\qquad
\text{objeto real}
\mapsto
\text{partícula puntual}.
$$

#### Aproximación en la resolución matemática

Incluso después de fijar un modelo, puede resultar difícil obtener su solución exacta y empleamos:

$$
[\mathrm{APPROX}].
$$

Así tenemos cuatro combinaciones conceptuales.

| Modelo físico | Solución matemática | Evaluación |
|---|---|---|
| adecuado | exacta | situación favorable |
| adecuado | aproximada y controlada | puede ser físicamente excelente |
| inadecuado | exacta | exactitud formal, mala representación |
| inadecuado | aproximada | dos fuentes potenciales de discrepancia |

La palabra «exacto» no debe ocultar en qué fila estamos.
La potencia del formalismo no elimina sus condiciones de interpretación:

Una estructura matemática puede ser extraordinariamente poderosa.

Puede revelar:

- consecuencias no evidentes;
- invariantes;
- relaciones entre variables;
- imposibilidades;
- simetrías;
- familias completas de soluciones.

Pero su poder lógico comienza **después** de fijar la representación.

Si aplicamos una estructura fuera de su dominio físico, la matemática puede continuar funcionando perfectamente mientras la interpretación se degrada.

De ahí la regla:

> nunca evaluar la calidad física de un modelo solamente por la elegancia o solvencia de su formalismo.
Comparemos dos procedimientos.

#### Procedimiento A

Usamos una aproximación:

$$
Q_{\mathrm{aprox}}
$$

y declaramos:

- qué efecto omitimos;
- qué parámetro lo controla;
- qué régimen utilizamos;
- dónde esperamos que falle.

#### Procedimiento B

Usamos una fórmula exacta:

$$
Q_{\mathrm{exacta}}
$$

pero ocultamos que proviene de una idealización inaplicable al sistema real.

Desde el punto de vista del conocimiento físico, A puede ser superior.

No porque la aproximación sea mágicamente más verdadera, sino porque sus límites están **controlados y visibles**.
En matemáticas, podemos hablar con precisión de igualdad exacta:

$$
a=b.
$$

En física experimental, las afirmaciones dependen de:

- procedimientos;
- resolución;
- calibración;
- condiciones;
- convenciones de representación.

Por eso evitaremos expresiones vagas como:

> «este valor físico es absolutamente exacto».

Preguntaremos siempre:

> exacto ¿en qué sentido?

Puede significar:

- exacto por definición;
- exacto dentro del modelo;
- obtenido sin aproximación matemática;
- compatible con la observación dentro de cierta precisión.

Son afirmaciones diferentes.
Una expresión exacta puede depender de parámetros medidos y una solución exacta puede quedar excluida por restricciones físicas:

Incluso si el modelo produce una expresión exacta:

$$
P=f(\theta),
$$

el parámetro:

$$
\theta
$$

puede provenir de una medición.

Entonces debemos separar:

1. exactitud de la relación formal $P=f(\theta)$;
2. conocimiento empírico de $\theta$;
3. adecuación física del modelo;
4. precisión de la comparación con la observación.

No desarrollaremos todavía propagación de incertidumbre.

Pero la estructura lógica debe quedar visible.
En §12 vimos el ejemplo abstracto de dos soluciones:

$$
x_1,
\qquad
x_2,
$$

cuando una restricción física exige:

$$
x>0.
$$

Si:

$$
x_2<0,
$$

$x_2$ puede seguir siendo solución exacta de la ecuación.

Lo que falla es su admisibilidad física.

Así:

$$
\boxed{
\text{solución exacta de la ecuación}
\neq
\text{estado físicamente permitido}.
}
$$

Esta distinción será esencial cuando aparezcan condiciones de frontera, restricciones y ramas de soluciones.
Consideremos dos tareas.
