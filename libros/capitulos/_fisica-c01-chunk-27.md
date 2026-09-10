La utilidad del esquema consiste en impedir que olvidemos que $P$ depende de más de una premisa.

En términos del protocolo de estatus, una cadena real puede contener:

$$
[\mathrm{POST}],
\quad
[\mathrm{EMP}],
\quad
[\mathrm{MOD}],
\quad
[\mathrm{APPROX}],
\quad
[\mathrm{IC}],
\quad
[\mathrm{BC}],
\quad
[\mathrm{OBS}],
$$

antes de llegar a las consecuencias:

$$
[\mathrm{MATH}].
$$
### 12.4. La parte matemática empieza después de declarar las premisas

El protocolo FPM establece:

> la prueba matemática comienza después de declarar las premisas físicas.

La razón puede verse ahora con claridad.

Una vez aceptamos:

$$
H,\ I,\ A,\ M,
$$

podemos realizar una derivación matemática rigurosa.

Pero esa demostración muestra:

$$
\boxed{
H\land I\land A\land M
\Longrightarrow
P,
}
$$

no:

$$
\boxed{
P\ \text{es una verdad matemática independiente del mundo}.
}
$$

La consecuencia es exacta **relativamente a las premisas**.
### 12.5. El modus tollens elemental

Recordemos la forma lógica:

$$
Q\to P.
$$

Si además sabemos:

$$
\neg P,
$$

podemos concluir:

$$
\neg Q.
$$

Este es el modus tollens:

$$
\boxed{
(Q\to P)\land\neg P
\Longrightarrow
\neg Q.
}
$$

En nuestro caso:

$$
Q
=
H\land I\land A\land M.
$$

Entonces el resultado será inmediato.

Pero sus consecuencias físicas merecen una lectura cuidadosa.
### 12.6. Segunda proposición formal del capítulo

::: {.ma-block .ma-enunciado #fpm-i-01-p02}
**FPM-I-01-P02 — Lógica de revisión de un paquete predictivo**

Sean $H$, $I$, $A$, $M$ y $P$ proposiciones. Si:

$$
(H\land I\land A\land M)\to P
$$

y:

$$
\neg P,
$$

entonces:

$$
\neg(H\land I\land A\land M).
$$

Equivalentemente, por las leyes de De Morgan:

$$
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
$$

Por tanto, la falsedad de la predicción no permite concluir lógicamente, a partir de estas premisas solamente, cuál de los componentes $H$, $I$, $A$ o $M$ debe rechazarse.
:::
### 12.7. Demostración de FPM-I-01-P02

Definamos:

$$
Q
=
H\land I\land A\land M.
$$

La primera hipótesis se convierte en:

$$
Q\to P.
$$

La segunda hipótesis es:

$$
\neg P.
$$

Por modus tollens:

$$
\neg Q.
$$

Sustituyendo nuevamente la definición de $Q$:

$$
\neg(H\land I\land A\land M).
$$

Aplicamos ahora la ley de De Morgan para una conjunción finita:

$$
\neg(H\land I\land A\land M)
\equiv
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
$$

Por tanto:

$$
\boxed{
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
}
$$

Esto demuestra la proposición.

$$
\boxed{\text{QED}}
$$
### 12.8. Qué demuestra realmente P02

La conclusión es una **disyunción**:

$$
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
$$

No es:

$$
\neg H.
$$

Tampoco es:

$$
\neg A.
$$

Ni:

$$
\neg M.
$$

Con la información lógica disponible sabemos solamente que **al menos un componente del paquete no puede mantenerse tal como estaba**.

Esta es la diferencia entre:

$$
\boxed{
\text{detección de inconsistencia}
}
$$

y:

$$
\boxed{
\text{diagnóstico de la causa}.
}
$$
### 12.9. El teorema no decide por nosotros

El matemático podría sentir cierta frustración.

Tenemos una demostración perfecta y, sin embargo, la conclusión física parece incompleta.

Pero esto no es una debilidad de la demostración.

Es precisamente lo que la lógica permite concluir.

Para pasar de:

$$
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M
$$

a una afirmación como:

$$
\neg A
$$

necesitamos información adicional que descarte las demás alternativas.

Por ejemplo, podríamos comprobar independientemente:

$$
H,
\qquad
I,
\qquad
M.
$$

Entonces la disyunción obligaría a:

$$
\neg A.
$$

El diagnóstico requiere **nuevas premisas**.
### 12.10. La discrepancia observacional también es una premisa

Hemos escrito:

$$
\neg P.
$$

Pero en un experimento real rara vez recibimos una proposición booleana directamente de la naturaleza.

Recibimos:

- lecturas;
- imágenes;
- conteos;
- señales;
- intervalos;
- resultados procesados.

Para afirmar:

$$
\neg P
$$

debemos decidir que la observación es suficientemente incompatible con la predicción bajo un criterio pertinente.

Ese paso pertenece a:

$$
[\mathrm{OBS}].
$$

Más adelante estudiaremos incertidumbre y tratamiento cuantitativo de datos.

Aquí simplemente registramos:

$$
\boxed{
\text{establecer }\neg P
\text{ también requiere una cadena observacional fiable}.
}
$$

Por eso $M$ forma parte del paquete.
### 12.11. Ejemplo desarrollado 15 — El cronómetro

Supongamos que un modelo de cierto sistema predice un tiempo:

$$
T_{\mathrm{pred}}.
$$

La medición produce un valor incompatible con esa predicción.

Podemos organizar las posibilidades.

#### $H$ — Estructura física

Tal vez alguna relación física utilizada no sea adecuada para el fenómeno.

#### $I$ — Condiciones

Tal vez el estado inicial real no fue el que creíamos.

#### $A$ — Aproximaciones

Tal vez un efecto despreciado se volvió relevante.

#### $M$ — Medición

Tal vez el cronómetro, la calibración o el procedimiento de detección introdujeron un problema.

El resultado experimental, por sí solo, no selecciona una de estas cuatro explicaciones.
### 12.12. Un fallo puede localizarse mediante pruebas auxiliares

La ambigüedad no significa que el diagnóstico sea imposible.

Significa que requiere trabajo adicional.

Podemos diseñar pruebas independientes.

Por ejemplo:

#### Prueba de $I$

Repetir el experimento con una preparación mejor controlada.

#### Prueba de $M$

Calibrar el instrumento mediante un patrón independiente.

#### Prueba de $A$

Cambiar deliberadamente la escala o condición que controla la aproximación.

#### Prueba de $H$

Buscar otra predicción que dependa de la misma hipótesis pero no de las mismas aproximaciones.

La revisión se convierte así en un problema de **discriminación entre causas posibles**, análogo a §10.
### 12.13. El experimento discriminante reaparece

En §10 definimos un experimento discriminante entre modelos.

Ahora podemos extender la idea conceptualmente.

Después de un fallo, nuestras alternativas son:

$$
\neg H,
\qquad
\neg I,
\qquad
\neg A,
\qquad
\neg M.
$$

Buscamos una nueva prueba cuyo resultado cambie según cuál de esas posibilidades sea la responsable.

Por ejemplo:

$$
\text{prueba auxiliar}
\longrightarrow
\begin{cases}
\text{resultado compatible con fallo de }A,\\
\text{resultado compatible con fallo de }M.
\end{cases}
$$

El diagnóstico es una nueva tarea de modelización.
### 12.14. Principio metodológico de auditoría

::: {.ma-block .ma-metodo #fpm-i-01-mp20}
**Principio FPM-I-01-MP20 — Un fallo predictivo exige auditoría, no culpable automático**
Si una predicción fiable contradice una observación fiable, debe revisarse el paquete de premisas que produjo la predicción. La discrepancia, por sí sola, no identifica cuál hipótesis, condición, aproximación o regla de observación es responsable.
:::

Este principio es la lectura metodológica directa de `P02`.
### 12.15. Qué ocurre con una solución físicamente absurda

A veces el problema aparece incluso antes de realizar el experimento.

Una derivación matemática produce una solución que contradice una restricción física declarada.

Entonces no debemos decir automáticamente:

> «La matemática falló».

Debemos preguntar:

1. ¿la solución satisface realmente las ecuaciones?;
2. ¿pertenece al espacio físico de estados admitido?;
3. ¿respeta las condiciones iniciales y de frontera?;
4. ¿viola una idealización o un régimen?;
5. ¿hemos interpretado correctamente las variables?

Una solución puede ser matemáticamente válida para la ecuación y físicamente inadmisible para el modelo completo.

Este punto prepara §13.
### 12.16. Ficha FPM de auditoría de una predicción fallida

::: {.ma-block .ma-metodo}
**Ficha FPM — Auditoría de fallo predictivo**
1. **Predicción:** ¿qué proposición $P$ estaba realmente implicada?
2. **Hipótesis:** ¿qué contiene $H$?
3. **Condiciones:** ¿qué contiene $I$?
4. **Idealizaciones y aproximaciones:** ¿qué contiene $A$?
5. **Mediación observacional:** ¿qué contiene $M$?
6. **Régimen:** ¿estábamos dentro de $\mathcal R$?
7. **Discrepancia:** ¿qué evidencia autoriza afirmar $\neg P$?
8. **Conclusión lógica mínima:** ¿qué conjunción queda negada?
9. **Alternativas:** ¿qué términos aparecen en la disyunción de De Morgan?
10. **Evidencia independiente:** ¿qué alternativas podemos descartar ya?
11. **Prueba nueva:** ¿qué experimento distinguiría las causas restantes?
12. **Revisión:** ¿qué nivel del modelo o teoría debe modificarse?
:::
::: {.ma-block .ma-enunciado #fpm-i-01-e029}
**Ejercicio FPM-I-01-E029 — Modus tollens compuesto**

**Familia:** `E-PROOF / CORE`

Demuestra:

$$
[(H\land I\land A\land M)\to P]
\land
\neg P
\Longrightarrow
\neg(H\land I\land A\land M).
$$

Después explica por qué la conclusión:

$$
\neg H
$$

no se sigue de las premisas.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

Definamos:

$$
Q
=
H\land I\land A\land M.
$$

La primera parte de la hipótesis es:

$$
Q\to P.
$$

La segunda es:

$$
\neg P.
$$

Por modus tollens:

$$
\neg Q.
$$

Sustituyendo:

$$
\boxed{
\neg(H\land I\land A\land M).
}
$$

Ahora preguntamos si podemos concluir:

$$
\neg H.
$$

No.

Por De Morgan:

$$
\neg(H\land I\land A\land M)
\equiv
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
$$

La disyunción puede ser verdadera aunque:

$$
H
$$

sea verdadera.

Por ejemplo, consideremos:

$$
H=\text{V},
\qquad
I=\text{F},
\qquad
A=\text{V},
\qquad
M=\text{V}.
$$

Entonces:

$$
H\land I\land A\land M
=
\text{F},
$$

y por tanto:

$$
\neg(H\land I\land A\land M)
=
\text{V},
$$

pero:

$$
\neg H
=
\text{F}.
$$

Así existe una valuación donde la conclusión de `P02` es verdadera y $\neg H$ es falsa.

Por tanto:

$$
\boxed{
\neg(H\land I\land A\land M)
\not\Rightarrow
\neg H.
}
$$
:::
::: {.ma-block .ma-enunciado #fpm-i-01-e030}
**Ejercicio FPM-I-01-E030 — De Morgan y diagnóstico físico**

**Familia:** `E-PROOF / CORE`

Un experimento se modela mediante el siguiente paquete:

- $H$: la relación física central utilizada es adecuada;
- $I$: las condiciones iniciales y parámetros fueron correctamente determinados;
- $A$: las aproximaciones e idealizaciones siguen dentro de su régimen;
- $M$: el procedimiento de observación y calibración es correcto.

Se ha demostrado que:

$$
(H\land I\land A\land M)\to P.
$$

Una observación fiable es incompatible con $P$.

1. Escribe la conclusión lógica mínima.
2. Aplica De Morgan.
3. Un control independiente confirma $I$.
4. Una calibración independiente confirma $M$.
5. Una prueba adicional muestra que la aproximación principal está fuera de su régimen.
6. ¿Qué revisión está entonces directamente justificada?
7. ¿Se sigue de este diagnóstico que $H$ es falsa?
8. Explica qué habría ocurrido si se hubiera saltado directamente de $\neg P$ a $\neg H$.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

#### 1. Conclusión mínima

Tenemos:

$$
(H\land I\land A\land M)\to P
$$

y:

$$
\neg P.
$$

Por modus tollens:

$$
\boxed{
\neg(H\land I\land A\land M).
}
$$
#### 2. De Morgan

Aplicamos:

$$
\neg(X\land Y)
\equiv
\neg X\lor\neg Y.
$$

Extendida a las cuatro premisas:

$$
\boxed{
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
}
$$
#### 3. Confirmación de $I$

La evidencia independiente autoriza mantener:

$$
I.
$$

Por tanto, dentro del diagnóstico actual podemos eliminar:

$$
\neg I.
$$

La disyunción se reduce informativamente a:

$$
\neg H
\lor
\neg A
\lor
\neg M.
$$
#### 4. Confirmación de $M$

La calibración independiente autoriza mantener:

$$
M.
$$

La disyunción restante es:

$$
\neg H
\lor
\neg A.
$$
#### 5. La aproximación está fuera de régimen

La nueva prueba proporciona evidencia específica para:

$$
\neg A.
$$

Ahora tenemos una causa concreta capaz de explicar la discrepancia.
#### 6. Revisión justificada

La revisión directamente justificada es:

> abandonar o modificar la aproximación que produjo $A$, o sustituirla por una descripción válida en el nuevo régimen.

En símbolos, la evidencia favorece:

$$
\boxed{\neg A}.
$$
#### 7. ¿Implica esto $\neg H$?

No.

La disyunción:

$$
\neg H\lor\neg A
$$

queda satisfecha si:

$$
\neg A
$$

es verdadera.

Por tanto, el fallo de la aproximación no obliga lógicamente a rechazar:

$$
H.
$$

La relación física central puede continuar siendo adecuada.
#### 8. Error del salto directo

Si hubiéramos inferido inmediatamente:

$$
\neg P
\Longrightarrow
\neg H,
$$

habríamos cometido un error lógico.

La predicción dependía de:

$$
H\land I\land A\land M,
$$

no de $H$ sola.

La inferencia válida era:

$$
\neg P
\Longrightarrow
\neg(H\land I\land A\land M),
$$

dado el condicional predictivo.

El diagnóstico posterior requirió evidencia nueva.

La lección es:

$$
\boxed{
\text{fallo predictivo}
\neq
\text{identificación automática de la causa}.
}
$$
:::
### 12.19. Síntesis

La segunda proposición formal del capítulo es:

$$
\boxed{
[(H\land I\land A\land M)\to P]
\land
\neg P
\Longrightarrow
\neg(H\land I\land A\land M).
}
$$

Por De Morgan:

$$
\boxed{
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
}
$$

La matemática nos dice exactamente cuánto podemos concluir.

No menos:

> alguna parte del paquete debe revisarse.

Pero tampoco más:

> la lógica por sí sola no identifica cuál.

Por eso `P02` conduce al principio metodológico:

$$
\boxed{
\text{predicción fallida}
\longrightarrow
\text{auditoría de premisas}.
}
$$

La tarea física comienza entonces de nuevo:

- revisar condiciones;
- revisar régimen;
- revisar aproximaciones;
- revisar observación;
- diseñar pruebas discriminantes;
- y, cuando la evidencia lo exige, revisar la propia teoría.

La sección siguiente afinará una distinción que ya ha aparecido varias veces.

Una solución puede ser matemáticamente exacta y, sin embargo, describir mal el mundo.

Una aproximación puede ser matemáticamente inexacta y, sin embargo, describirlo extraordinariamente bien en su régimen.

Entramos así en:

$$
\boxed{
\text{§13 — Exactitud matemática y adecuación física}.
}
$$
