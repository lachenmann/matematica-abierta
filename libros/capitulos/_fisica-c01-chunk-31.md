#### 4. Admisibilidad

> ¿La solución satisface las restricciones físicas?

#### 5. Régimen

> ¿Estamos dentro de $\mathcal R$?

#### 6. Observabilidad

> ¿La cantidad calculada corresponde a una medición bien definida?

#### 7. Adecuación

> ¿La predicción representa el fenómeno con la precisión necesaria?

Una respuesta positiva en el primer nivel no garantiza las restantes.
::: {.ma-block .ma-metodo}
**Ficha FPM — Exactitud matemática y adecuación física**
1. **Modelo:** ¿qué sistema está siendo representado?
2. **Premisas:** ¿qué se supone exactamente?
3. **Idealizaciones:** ¿qué rasgos reales se han eliminado?
4. **Aproximaciones:** ¿qué reemplazos no exactos se han realizado?
5. **Derivación:** ¿es exacta dentro de esas premisas?
6. **Soluciones:** ¿todas las soluciones matemáticas son físicamente admisibles?
7. **Parámetros:** ¿son definidos, ajustados o medidos?
8. **Régimen:** ¿pertenece el caso a $\mathcal R$?
9. **Observación:** ¿cómo se conecta el resultado con `[OBS]`?
10. **Precisión:** ¿qué nivel de adecuación exige la pregunta?
11. **Comparación:** ¿una aproximación controlada representa mejor el fenómeno?
12. **Conclusión:** ¿qué es exactamente lo que podemos afirmar?
:::
### 13.4. Ejercicio

::: {.ma-block .ma-enunciado #fpm-i-01-e031}
**Ejercicio FPM-I-01-E031 — Solución exacta de un modelo inadecuado**

**Familia:** `E-FAIL / ADVANCED`

Un dispositivo convierte una entrada física $x\ge0$ en una señal de salida $y$.

Un primer modelo ideal propone:

$$
M_1:
\qquad
y=2x.
$$

La electrónica real del dispositivo posee, sin embargo, una saturación física:

$$
0\le y\le10.
$$

Para entradas pequeñas, las mediciones disponibles son compatibles con $M_1$.

Responde:

1. Calcula exactamente la predicción de $M_1$ para:
   $$
   x=3.
   $$
2. Calcula exactamente la predicción de $M_1$ para:
   $$
   x=8.
   $$
3. Explica por qué el segundo cálculo puede ser matemáticamente correcto y físicamente inadmisible.
4. Propón un modelo efectivo elemental que incorpore la saturación.
5. Calcula su predicción para $x=3$ y $x=8$.
6. ¿Cuál de los dos modelos es «más exacto»? Explica por qué la pregunta es ambigua.
7. Un estudiante afirma: «Como $M_1$ tiene una fórmula más simple y sus cálculos son exactos, es científicamente superior». Analiza el argumento.
8. Identifica los estatus `[MOD]`, `[MATH]` y `[OBS]` que deberían aparecer en una investigación real del dispositivo.
:::
#### Solución

#### 1. Predicción para $x=3$

El modelo declara:

$$
y=2x.
$$

Entonces:

$$
y=2\cdot3.
$$

Por tanto:

$$
\boxed{y=6}.
$$

El cálculo es exacto dentro de $M_1$.

Además:

$$
6\le10,
$$

por lo que la predicción no viola la restricción de saturación.
#### 2. Predicción para $x=8$

Aplicando la misma relación:

$$
y=2\cdot8.
$$

Luego:

$$
\boxed{y=16}.
$$

Nuevamente, la aritmética es exacta.
#### 3. Corrección matemática y admisibilidad física

La electrónica real exige:

$$
y\le10.
$$

Pero:

$$
16>10.
$$

Por tanto, el valor:

$$
y=16
$$

es una consecuencia matemática exacta de:

$$
M_1,
$$

pero no es físicamente admisible para el dispositivo descrito.

La conclusión correcta es:

$$
\boxed{
\text{el modelo lineal ha sido extrapolado fuera de su régimen adecuado}.
}
$$

No:

$$
\boxed{
2\cdot8\neq16.
}
$$
#### 4. Modelo efectivo con saturación

Podemos proponer:

$$
M_2:
\qquad
y=
\begin{cases}
2x, & 0\le x\le5,\\
10, & x>5.
\end{cases}
$$

Este modelo conserva la relación lineal donde la salida todavía no ha alcanzado el límite y representa la saturación después.

No afirmamos que sea una descripción microscópica completa de la electrónica.

Es un modelo efectivo para la pregunta.
#### 5. Predicciones de $M_2$

Para:

$$
x=3,
$$

como:

$$
3\le5,
$$

tenemos:

$$
y=2\cdot3=6.
$$

Para:

$$
x=8,
$$

como:

$$
8>5,
$$

tenemos:

$$
y=10.
$$

Por tanto:

$$
\boxed{
M_2(3)=6,
\qquad
M_2(8)=10.
}
$$
#### 6. ¿Cuál es más exacto?

La pregunta mezcla dos sentidos.

Dentro de sus propias fórmulas, ambos modelos permiten cálculos exactos.

Pero como representación del dispositivo en el régimen que incluye $x=8$, $M_2$ es físicamente más adecuado porque incorpora la restricción de saturación.

Por tanto:

$$
\boxed{
\text{exactitud matemática}
\neq
\text{adecuación física}.
}
$$
