La capacidad del procedimiento `[OBS]` forma parte del diseño.
Supongamos tres modelos:

$$
M_1,\quad M_2,\quad M_3.
$$

En una condición $C$ predicen:

$$
P_1=a,
$$

$$
P_2=b,
$$

$$
P_3=b.
$$

Si el experimento favorece $b$, podemos debilitar $M_1$.

Pero todavía no distinguimos entre:

$$
M_2
$$

y:

$$
M_3.
$$

El experimento fue informativo aunque no produjera una selección única.

Así:

$$
\boxed{
\text{discriminación}
\neq
\text{decisión final garantizada}.
}
$$

La investigación puede proceder por sucesivas particiones de la familia de modelos.
Imaginemos tres candidatos que coinciden en los datos iniciales.

#### Primera prueba

Elegimos una condición $C_1$ donde:

$$
M_1
$$

predice algo diferente de:

$$
M_2,\ M_3.
$$

El resultado descarta o debilita $M_1$.

#### Segunda prueba

Ahora buscamos una condición $C_2$ donde:

$$
M_2
$$

y:

$$
M_3
$$

difieran.

La selección de experimentos se vuelve adaptativa:

$$
\boxed{
\text{datos}
\to
\text{familia de candidatos}
\to
\text{prueba discriminante}
\to
\text{familia reducida}
\to
\text{nueva prueba}.
}
$$

No necesitamos todavía una teoría estadística para comprender esta arquitectura lógica.
Si elegimos puntos de prueba al azar, quizá los modelos sigan coincidiendo.

La estructura física puede guiarnos.

Dos modelos pueden diferir especialmente:

- cuando una idealización deja de ser adecuada;
- cerca de una frontera del régimen;
- cuando cambia una simetría;
- cuando un efecto antes despreciado se vuelve importante;
- al variar un parámetro que afecta de modo diferente a los mecanismos rivales.

La teoría no solo produce predicciones.

También ayuda a diseñar **experimentos informativos**.
Supongamos que $M_1$:

- requiere menos hipótesis independientes;
- se integra con una teoría más amplia;
- explica varios fenómenos;
- produce nuevas predicciones acertadas.

Mientras $M_2$:

- reproduce solo los datos originales;
- necesita varios ajustes independientes;
- no produce consecuencias nuevas.

Es razonable preferir $M_1$.

Pero la forma correcta de expresarlo es:

> «La evidencia y la estructura disponibles favorecen $M_1$».

No:

> «$M_1$ ha sido demostrado como descripción final de la naturaleza».

La selección física es revisable.
Los criterios pueden entrar en tensión; ni la complejidad ni la sencillez merecen premio automático:

Consideremos dos candidatos.

#### Modelo A

- muy simple;
- fácil de calcular;
- válido solo en un régimen pequeño.

#### Modelo B

- más complejo;
- explica varios regímenes;
- requiere más estructura matemática.

¿Cuál es mejor?

La pregunta está incompleta.

Para una estimación rápida dentro del régimen pequeño, A puede ser preferible.

Para estudiar la transición entre regímenes, B puede ser necesario.

Esto refuerza:

$$
\boxed{
\text{preferencia}
=
\text{relación entre modelo, pregunta y régimen}.
}
$$
También debemos evitar el sesgo contrario.

Un modelo no mejora automáticamente al agregar:

- más parámetros;
- más mecanismos;
- más términos;
- más variables;
- más detalle microscópico.

Cada nueva estructura debe responder:

> ¿qué problema resuelve?

Si una ampliación no cambia ninguna predicción relevante, no explica ningún fenómeno nuevo y no extiende el régimen, puede ser innecesaria para la tarea actual.

Esto recupera `MP09`:

> **modelo mínimo suficiente**.
Pero tampoco debemos eliminar estructura necesaria solo para obtener una fórmula elegante.

Si dos efectos observados requieren mecanismos distintos, un modelo que ignora uno de ellos puede ser más corto y peor.

La economía debe entenderse como:

$$
\boxed{
\text{no introducir estructura innecesaria}
}
$$

y no como:

$$
\boxed{
\text{eliminar estructura necesaria para que la fórmula sea corta}.
}
$$
La selección de modelos debe conservar tres preguntas: ¿es coherente?, ¿es adecuada para la tarea?, ¿produce nuevas consecuencias capaces de ser contrastadas?

Podemos organizar los criterios en tres grupos.

#### 1. Coherencia

Preguntas:

- ¿el modelo es matemáticamente consistente?;
- ¿sus definiciones y condiciones son compatibles?;
- ¿su interpretación es clara?

#### 2. Adecuación

Preguntas:

- ¿reproduce los fenómenos relevantes?;
- ¿funciona en el régimen declarado?;
- ¿las magnitudes pueden conectarse con observaciones?

#### 3. Fecundidad

Preguntas:

- ¿produce predicciones nuevas?;
- ¿explica varios fenómenos?;
- ¿sugiere experimentos?;
- ¿organiza relaciones antes separadas?;
- ¿muestra dónde debería fallar?

Un modelo científicamente potente no solo encaja lo ya observado.

También abre trabajo nuevo.
Puede parecer extraño valorar un modelo porque declara sus límites.

Pero un modelo que especifica:

$$
\mathcal R
$$

y anticipa dónde una aproximación debe dejar de funcionar es más informativo que uno que simplemente se aplica sin control.

Una teoría física madura suele permitir preguntar:

> ¿qué parámetro controla esta aproximación?

y:

> ¿qué fenómeno aparecerá cuando deje de ser pequeño?

Por eso la capacidad de delimitar el propio fracaso puede ser parte de la calidad del modelo.
Podemos ahora reunir el proceso:

$$
\boxed{
\text{fenómeno}
\to
\text{modelos candidatos}
\to
\text{filtros}
\to
\text{criterios comparativos}
\to
\text{predicciones divergentes}
\to
\text{experimento}
\to
\text{revisión}.
}
$$

El resultado no es necesariamente un modelo definitivo.

Puede ser:

- descartar uno;
- restringir otro;
- modificar una aproximación;
- descubrir un nuevo régimen;
- formular un tercer candidato.

La selección y la revisión forman un proceso continuo.
::: {.ma-block .ma-metodo}
**Ficha FPM — Comparación y discriminación de modelos**
1. **Pregunta:** ¿qué queremos explicar o predecir?
2. **Candidatos:** ¿qué modelos se comparan?
3. **Datos compartidos:** ¿qué evidencia reproducen todos?
4. **Coherencia:** ¿algún candidato falla internamente?
5. **Interpretación:** ¿qué significa físicamente cada formalismo?
6. **Régimen:** ¿en qué $\mathcal R$ pretende funcionar cada modelo?
7. **Hipótesis:** ¿qué estructura independiente introduce cada uno?
8. **Explicación:** ¿qué mecanismo o estructura hace responsable del fenómeno?
9. **Predicciones rivales:** ¿dónde difieren?
10. **Observabilidad:** ¿esa diferencia puede medirse?
11. **Prueba:** ¿qué experimento discrimina mejor?
12. **Resultado:** ¿qué modelos quedan favorecidos, debilitados o todavía indistinguibles?
:::

### 10.4. Ejercicio

::: {.ma-block .ma-enunciado #fpm-i-01-e026}
**Ejercicio FPM-I-01-E026 — Diseñar un experimento discriminante**

**Familia:** `E-MOD / SYNTHESIS`

Se han observado únicamente los datos:

$$
(0,0),
\qquad
(1,1).
$$

Dos modelos candidatos son:

$$
M_1:\quad y=x,
$$

$$
M_2:\quad y=x^2.
$$

Responde:

1. Verifica que ambos modelos reproducen los datos conocidos.
2. Explica por qué repetir exactamente las mismas condiciones $x=0$ y $x=1$ no discrimina los modelos.
3. Propón un valor $x_\ast$ dentro del intervalo $[0,1]$ donde las predicciones difieran.
4. Calcula ambas predicciones.
5. Explica qué debe cumplir el procedimiento `[OBS]` para que el experimento sea realmente discriminante.
6. Supón que la observación nueva es compatible con $y=1/4$. ¿Qué modelo queda favorecido dentro de este par?
7. Explica por qué el resultado no demuestra que el modelo favorecido sea la única función posible compatible con todos los datos.
8. Indica al menos dos criterios adicionales, distintos del nuevo dato, que sería razonable examinar antes de adoptar el modelo para una aplicación física.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

##### 1. Datos conocidos

Para $M_1$:

$$
M_1(0)=0,
$$

$$
M_1(1)=1.
$$

Para $M_2$:

$$
M_2(0)=0^2=0,
$$

$$
M_2(1)=1^2=1.
$$

Por tanto:

$$
\boxed{
M_1\sim D
\quad
\text{y}
\quad
M_2\sim D.
}
$$
##### 2. Repetir los extremos

En:

$$
x=0
$$

y:

$$
x=1,
$$

ambos modelos producen exactamente las mismas predicciones.

Por tanto, aunque mejoremos mucho la repetición experimental, esas condiciones no separan la estructura de los candidatos.

Necesitamos una condición donde:

$$
M_1(x_\ast)\neq M_2(x_\ast).
$$
##### 3. Elección de $x_\ast$

Una elección sencilla es:

$$
x_\ast=\frac12.
$$

Está dentro del intervalo ya explorado entre los dos datos originales.
##### 4. Predicciones

Para $M_1$:

$$
M_1\left(\frac12\right)
=
\frac12.
$$

Para $M_2$:

$$
M_2\left(\frac12\right)
=
\left(\frac12\right)^2
=
\frac14.
$$

Así:

$$
\boxed{
P_1=\frac12,
\qquad
P_2=\frac14.
}
$$
##### 5. Papel de `[OBS]`

No basta que:

$$
\frac12\neq\frac14.
$$

El procedimiento experimental debe poder distinguir resultados compatibles con ambos valores.

Esto requiere una conexión observacional:

$$
[\mathrm{OBS}]
\qquad
y
\longleftrightarrow
\text{procedimiento de medición}
$$

capaz de separar las dos predicciones con la precisión pertinente.
##### 6. Resultado $y=1/4$

Si la nueva observación es compatible con:

$$
y=\frac14,
$$

entonces, dentro del par considerado, queda favorecido:

$$
\boxed{M_2}.
$$

El modelo $M_1$ predice:

$$
y=\frac12,
$$

por lo que la nueva evidencia lo contradice bajo las condiciones y el régimen asumidos.
##### 7. Por qué no hay unicidad absoluta

Los tres datos:

$$
(0,0),
\qquad
\left(\frac12,\frac14\right),
\qquad
(1,1)
$$

siguen siendo finitos.

Por `P01`, una vez conocido un polinomio compatible podemos construir otros añadiendo un término que se anule en los tres valores observados.

Por ejemplo:

$$
q_c(x)
=
x^2
+
c\,x
\left(x-\frac12\right)
(x-1).
$$

Todos los $q_c$ conservan los tres datos.

Por tanto:
