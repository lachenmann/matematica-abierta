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
### 12.17. Ejercicio FPM-I-01-E029 — Modus tollens compuesto

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
#### Solución

Definamos:

$$
Q
=
H\land I\land A\land M.
$$

Entonces la primera premisa es:

$$
Q\to P.
$$

También tenemos:

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

La conclusión:

$$
\neg H
$$

no se sigue porque la negación de una conjunción solo implica que al menos uno de sus componentes falla.

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

Por ejemplo, es lógicamente posible que:

$$
H=\text{verdadero},
$$

pero:

$$
A=\text{falso}.
$$

Entonces la conjunción total sería falsa aunque $H$ siguiera siendo verdadera.
### 12.18. Ejercicio FPM-I-01-E030 — De Morgan y diagnóstico físico

**Familia:** `E-CON / ADVANCED`

Una predicción falla y sabemos:

$$
\neg(H\land I\land A\land M).
$$

Además, mediante pruebas independientes establecemos:

$$
H,
\qquad
I,
\qquad
M.
$$

1. Demuestra que debe cumplirse:

$$
\neg A.
$$

2. Interpreta físicamente el resultado.
3. Explica por qué esta conclusión era imposible antes de obtener la evidencia independiente sobre $H$, $I$ y $M$.
#### Solución

##### 1. Demostración

Por De Morgan:

$$
\neg(H\land I\land A\land M)
$$

es equivalente a:

$$
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
$$

Pero sabemos:

$$
H,
\qquad
I,
\qquad
M.
$$

Por tanto:

$$
\neg H,
\qquad
\neg I,
\qquad
\neg M
$$

son falsas.

La única posibilidad restante en la disyunción es:

$$
\boxed{
\neg A.
}
$$

##### 2. Interpretación física

Dentro del esquema, la discrepancia debe atribuirse a alguna idealización o aproximación contenida en $A$.

Esto no nos dice todavía cuál.

Puede ser necesario descomponer:

$$
A=A_1\land A_2\land\cdots\land A_k
$$

y realizar nuevas pruebas.

##### 3. Por qué antes no era posible

Inicialmente solo sabíamos:

$$
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
$$

La lógica no privilegiaba ningún término.

La evidencia adicional eliminó tres alternativas.

El diagnóstico se volvió posible porque añadimos nuevas premisas.

Esto ilustra:

$$
\boxed{
\text{revisión física}
=
\text{lógica}
+
\text{evidencia adicional}.
}
$$
### 12.19. Síntesis

La segunda proposición formal del capítulo establece:

$$
[(H\land I\land A\land M)\to P]
\land
\neg P
\Longrightarrow
\neg H
\lor
\neg I
\lor
\neg A
\lor
\neg M.
$$

La consecuencia física es clara:

$$
\boxed{
\text{predicción fallida}
\not\Rightarrow
\text{teoría automáticamente falsa}.
}
$$

Un fallo obliga a auditar:

- hipótesis;
- condiciones;
- aproximaciones;
- mediación observacional;
- régimen.

Y después a diseñar pruebas que permitan localizar la discrepancia.

Esta lógica completa el ciclo iniciado en §1:

$$
\boxed{
\text{pregunta}
\to
\text{modelo}
\to
\text{predicción}
\to
\text{experimento}
\to
\text{auditoría}
\to
\text{revisión}.
}
$$

La ciencia no termina cuando una predicción acierta.

Tampoco termina cuando falla.

Un modelo puede:

- sobrevivir;
- restringir su dominio;
- cambiar parámetros;
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
