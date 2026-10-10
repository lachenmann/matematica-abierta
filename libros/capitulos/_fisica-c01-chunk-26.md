::: {.ma-block .ma-enunciado #fpm-i-01-e027}
**Ejercicio FPM-I-01-E027 — Órbita marciana y perceptibilidad**

**Familia:** `E-LIM / CORE`

**Fuente del motivo:** adaptación y ampliación del ejemplo de Arnold sobre la excentricidad de la órbita de Marte.[@arnold2014mathematical, cap. 1, pp. 1–2]

Una elipse de semieje mayor $a$ y excentricidad $e$ tiene semieje menor:

$$
b=a\sqrt{1-e^2}.
$$

Para Marte podemos tomar, como orden de magnitud:

$$
e\approx0.1.
$$

Responde:

1. Calcula:

$$
\frac{b}{a}.
$$

2. Usando la aproximación de §4,

$$
\sqrt{1-A}
\approx
1-\frac{A}{2},
$$

estima:

$$
\frac{b}{a}
$$

sin calculadora.

3. Estima la diferencia relativa:

$$
1-\frac{b}{a}.
$$

4. Explica por qué una excentricidad de orden $0.1$ puede corresponder a una diferencia visual entre los semiejes de solo alrededor de medio punto porcentual.
5. Explica por qué este ejemplo distingue:
   - diferencia matemática;
   - perceptibilidad física;
   - régimen de una aproximación.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

##### 1. Razón exacta

Con:

$$
e=0.1,
$$

tenemos:

$$
e^2=0.01.
$$

Por tanto:

$$
\frac{b}{a}
=
\sqrt{1-0.01}
=
\sqrt{0.99}.
$$

Numéricamente:

$$
\sqrt{0.99}
\approx0.99499.
$$

Así:

$$
\boxed{
\frac{b}{a}
\approx0.995.
}
$$
##### 2. Aproximación elemental

Tomamos:

$$
A=0.01.
$$

Entonces:

$$
\sqrt{1-A}
\approx
1-\frac{A}{2}.
$$

Por tanto:

$$
\frac{b}{a}
\approx
1-\frac{0.01}{2}.
$$

Así:

$$
\boxed{
\frac{b}{a}
\approx0.995.
}
$$

La aproximación reproduce muy bien el valor anterior.
##### 3. Diferencia relativa

Tenemos:

$$
1-\frac{b}{a}
\approx
1-0.995
=
0.005.
$$

Como porcentaje:

$$
0.005\times100\%
=
0.5\%.
$$

Por tanto:

$$
\boxed{
a-b
\text{ representa aproximadamente el }0.5\%\text{ de }a.
}
$$
##### 4. Excentricidad y apariencia

La excentricidad entra al cuadrado en:

$$
\frac{b}{a}
=
\sqrt{1-e^2}.
$$

Así, aunque:

$$
e\approx0.1,
$$

la corrección geométrica relevante para comparar ambos semiejes es del orden de:

$$
e^2\approx0.01.
$$

La diferencia final entre $a$ y $b$ es todavía menor, aproximadamente:

$$
0.5\%.
$$

Por eso una cantidad matemática que no parece extremadamente pequeña puede producir una diferencia visual difícil de percibir directamente.
##### 5. Las tres distinciones

**Diferencia matemática:** la elipse no es un círculo.

**Perceptibilidad física:** la diferencia entre sus semiejes puede ser demasiado pequeña para distinguirla fácilmente a simple vista o con un procedimiento poco sensible.

**Régimen de aproximación:** la fórmula:

$$
\sqrt{1-A}
\approx
1-\frac{A}{2}
$$

funciona aquí porque:

$$
A=e^2=0.01
$$

es pequeño.

Por tanto:

$$
\boxed{
\text{diferencia real}
\neq
\text{diferencia fácilmente observable}.
}
$$
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e028}
**Ejercicio FPM-I-01-E028 — Rayos, ondas y fotones**

**Familia:** `E-LIM / CORE`

En física aparecen distintas descripciones de la luz:

- rayos;
- ondas;
- fotones.

Sin desarrollar todavía ninguna de estas teorías, responde:

1. ¿Por qué la existencia de una descripción ondulatoria no vuelve automáticamente inútil la óptica de rayos?
2. ¿Qué tipo de pregunta puede hacer insuficiente una descripción mediante rayos?
3. ¿Por qué una descripción cuántica más amplia no implica que debamos usar fotones en todo problema óptico elemental?
4. Formula la relación entre estas descripciones usando las ideas de:
   - pregunta;
   - escala;
   - observable;
   - dominio de validez;
   - descripción efectiva.
5. Explica por qué sería incorrecto escribir simplemente:

$$
\text{rayos}
\subset
\text{ondas}
\subset
\text{fotones}.
$$
:::

::: {.ma-block .ma-comprobacion}
**Solución**

##### 1. Utilidad de los rayos

Una descripción de rayos puede capturar con enorme eficacia:

- propagación aproximada de trayectorias;
- formación geométrica de imágenes;
- direcciones relevantes;
- relaciones entre objetos e instrumentos.

Si la pregunta no resuelve efectos donde la estructura ondulatoria es esencial, la descripción de rayos puede ser suficiente.

Por tanto:

$$
\boxed{
\text{descripción más amplia}
\not\Rightarrow
\text{descripción efectiva inútil}.
}
$$
##### 2. Cuándo pueden ser insuficientes los rayos

Si el fenómeno que queremos comprender depende precisamente de propiedades que una descripción de rayos omite, debemos cambiar de modelo.

Por ejemplo, una pregunta donde sean esenciales patrones producidos por la estructura ondulatoria requerirá una descripción capaz de representar esa estructura.

La conclusión correcta es:

> el modelo deja de ser suficiente para la nueva pregunta.

No:

> el modelo nunca fue útil.
##### 3. Por qué no usar siempre la descripción más fundamental

Una descripción cuántica puede contener estructura innecesaria para una tarea geométrica elemental.

Si el objetivo es determinar, por ejemplo, una dirección de propagación aproximada o una construcción geométrica de imagen, una teoría efectiva más simple puede ser:

- suficiente;
- más transparente;
- más eficiente.

Esto es precisamente `MP19`.
##### 4. Relación entre las descripciones

Podemos representarla conceptualmente:

$$
\text{pregunta}
+
\text{escala}
+
\text{observable}
\longrightarrow
\text{descripción adecuada}.
$$

Cada descripción posee un dominio físico donde ciertas variables y estructuras son las relevantes.

Una descripción efectiva selecciona justamente esas estructuras sin afirmar que sean la última descripción posible de la luz.
##### 5. Por qué no es inclusión conjuntista

Las teorías no son simplemente conjuntos de fórmulas colocados unos dentro de otros.

El paso entre descripciones puede requerir:

- nuevas variables;
- nuevas interpretaciones;
- aproximaciones;
- límites físicos;
- cambios en lo que consideramos observable.

Por tanto, la relación correcta es funcional:

$$
\boxed{
\text{descripciones distintas}
\longleftrightarrow
\text{regímenes y preguntas distintas},
}
$$

no una cadena literal de inclusión de conjuntos.
:::

### 11.5. Síntesis

Esta sección incorpora definitivamente el régimen:

$$
\mathcal R
$$

a la lectura de cualquier modelo.

La regla central es:

$$
\boxed{
\text{fórmula matemáticamente válida}
\not\Rightarrow
\text{predicción físicamente válida en todo régimen}.
}
$$

Definimos además una descripción efectiva como aquella que conserva la estructura necesaria para una pregunta y una escala determinadas sin reclamar universalidad.

Por eso:

$$
\boxed{
\text{efectivo}
\neq
\text{falso}.
}
$$

Y:

$$
\boxed{
\text{más fundamental}
\neq
\text{más útil para toda tarea}.
}
$$

A partir de ahora, cada aproximación importante deberá venir acompañada por preguntas de control:

- ¿qué se omitió?;
- ¿qué lo hace pequeño?;
- ¿qué precisión necesitamos?;
- ¿qué señal indicará que salimos del régimen?;
- ¿qué descripción más amplia debemos usar entonces?

Esto prepara la siguiente sección.

Cuando una predicción contradice una observación, debemos evitar el salto:

> «la teoría está equivocada».

Una predicción depende de teoría, modelo, condiciones, aproximaciones y reglas de observación.

La lógica de esa revisión será el objeto de:

$$
\boxed{
\text{§12 — Cuando una predicción falla: lógica de revisión}.
}
$$

---

## 12. Cuando una predicción falla: lógica de revisión {#fpm-i-01-s12}

### 12.1. El error más tentador

Supongamos que una teoría, junto con un modelo concreto, produce una predicción:

$$
P.
$$

Realizamos el experimento y obtenemos un resultado incompatible con esa predicción:

$$
\neg P.
$$

La reacción inmediata puede ser:

> «Entonces la teoría es falsa».

Pero esa inferencia es demasiado rápida.

La predicción no provenía de una teoría desnuda.

Para llegar a $P$ tuvimos que combinar:

- principios o hipótesis físicas;
- condiciones iniciales y de frontera;
- parámetros;
- idealizaciones;
- aproximaciones;
- reglas de interpretación;
- procedimientos de medición.

La predicción depende de un **paquete de premisas**.

Por eso un fallo predictivo pone en cuestión el paquete completo, no identifica automáticamente qué componente debe abandonarse.
### 12.2. El paquete predictivo

Para hacer visible la lógica, comprimiremos temporalmente las premisas en cuatro grupos.

Usaremos:

$$
H
$$

para las hipótesis, leyes o principios físicos relevantes;

$$
I
$$

para la información que fija la realización concreta, como condiciones iniciales, condiciones de frontera y parámetros pertinentes;

$$
A
$$

para las idealizaciones y aproximaciones utilizadas;

y:

$$
M
$$

para la mediación observacional: interpretación de magnitudes, calibración, procedimiento experimental y reglas `[OBS]` necesarias para comparar la consecuencia formal con una observación.

La letra $M$ de esta sección significa **mediación observacional** y no debe confundirse con el símbolo:

$$
\mathcal M
$$

que usamos para el modelo físico completo.

::: {.ma-block .ma-definicion #fpm-i-01-d30}
**Definición operativa FPM-I-01-D30 — Paquete predictivo**
Llamaremos **paquete predictivo** a la conjunción de premisas físicas, condiciones, aproximaciones y reglas de observación cuya aceptación conjunta permite derivar una predicción contrastable.
:::

En nuestra notación esquemática:

$$
\Pi
=
H\land I\land A\land M.
$$
### 12.3. La estructura lógica de una predicción

Una derivación física puede representarse esquemáticamente como:

$$
(H\land I\land A\land M)\to P.
$$

Esta fórmula no significa que toda teoría física real pueda reducirse literalmente a cuatro proposiciones simples.

Es un **esqueleto lógico**.
