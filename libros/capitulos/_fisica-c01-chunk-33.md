## 14. Cómo leer el resto de Física para matemáticos {#fpm-i-01-s14}


### 14.1. Este capítulo no era un prólogo

Podría parecer que hemos dedicado demasiadas páginas a hablar de física antes de empezar a «hacer física».

Pero el objetivo de este capítulo nunca fue retrasar las ecuaciones.

Fue aprender a leerlas.

A partir del capítulo siguiente comenzarán a aparecer de manera progresiva:

- magnitudes;
- unidades;
- vectores;
- curvas;
- leyes de movimiento;
- energía;
- campos;
- ecuaciones diferenciales;
- principios variacionales;
- operadores;
- probabilidades;
- estructuras geométricas.

Cada una de esas herramientas puede ser estudiada matemáticamente.

Pero en este libro siempre aparecerá además una segunda pregunta:

> **¿qué trabajo físico está realizando aquí esta estructura matemática?**

Este es el contrato de lectura del resto de la obra.
Todo tema importante intentará conservar, cuando corresponda, la secuencia:

$$
\boxed{
\text{fenómeno físico}
\longleftrightarrow
\text{modelo matemático}
\longleftrightarrow
\text{estructura matemática}.
}
$$

La flecha doble es esencial.

No leeremos la física como una simple aplicación posterior de matemáticas ya terminadas.

Tampoco trataremos la matemática como una colección de trucos para producir números.

Buscaremos un movimiento en ambas direcciones.

La física plantea problemas que exigen estructuras matemáticas.

La matemática reorganiza la comprensión física y permite descubrir consecuencias que no eran visibles al comienzo.
### 14.2. El protocolo permanente FPM

En vez de repetir por separado cada una de las quince preguntas desarrolladas a lo largo del capítulo, las reuniremos desde ahora en un único protocolo acumulativo.

Podemos condensar todo el capítulo en una secuencia.

::: {.ma-block .ma-metodo}
**Protocolo permanente de lectura FPM**

**1. Fenómeno**  
¿Qué ocurre físicamente?

**2. Pregunta**  
¿Qué queremos explicar, predecir o comparar?

**3. Sistema**  
¿Qué incluimos y qué dejamos en el entorno?

**4. Estado y variables**  
¿Qué información conserva el modelo?

**5. Representación**  
¿Qué objetos matemáticos utilizamos y qué significan?

**6. Estatus**  
¿Qué es definición, dato empírico, postulado, modelo, aproximación, condición o consecuencia matemática?

**7. Estructura matemática**  
¿Qué teoremas, operaciones o estructuras producen las consecuencias?

**8. Régimen**  
¿Dónde esperamos que la representación sea adecuada?

**9. Observación**  
¿Cómo se conecta el formalismo con una medición?

**10. Predicción o explicación**  
¿Qué resultado nuevo produce y qué estructura lo hace inteligible?

**11. Contraste**  
¿Qué observación podría discriminar esta descripción de alternativas?

**12. Revisión**  
Si falla, ¿qué parte del paquete predictivo debe auditarse?
:::

Esta secuencia no será una plantilla rígida.

No todos los problemas necesitan doce apartados explícitos.

Pero todos los pasos relevantes deben poder reconstruirse.
### 14.3. Cómo se usará el protocolo en el resto del tratado

Cuando una teoría física requiera una herramienta matemática todavía no disponible, no la utilizaremos silenciosamente.

El texto deberá:

1. identificar la necesidad física;
2. declarar el objeto matemático requerido;
3. construir o recordar sus definiciones;
4. demostrar los resultados necesarios;
5. volver al problema físico;
6. interpretar qué ganó la descripción.

La progresión será:

$$
\boxed{
\text{problema físico}
\to
\text{necesidad matemática}
\to
\text{estructura}
\to
\text{retorno a la física}.
}
$$

Esta regla evita dos extremos:

- convertir la física en un pretexto para una lista de fórmulas;
- convertir el libro en un tratado abstracto de matemáticas desconectado del fenómeno.
Cuando un resultado sea puramente matemático, deberá distinguirse de las premisas físicas que permiten aplicarlo.

Por ejemplo:

$$
[\mathrm{POST}]
+
[\mathrm{MOD}]
+
[\mathrm{IC}]
\longrightarrow
[\mathrm{MATH}].
$$

El teorema matemático puede tener demostración completa.

Pero la aplicación física debe conservar visibles las hipótesis que lo hacen relevante.

Así podremos responder siempre:

> ¿qué parte del argumento está demostrada matemáticamente y qué parte pertenece a la construcción física del modelo?
Las aproximaciones no serán tratadas como errores vergonzosos que debamos esconder.

Son una herramienta central de la física.

Pero deben estar controladas.

Cuando sea posible, registraremos:

$$
\text{efecto omitido},
$$

$$
\text{parámetro de control},
$$

$$
\text{régimen},
$$

$$
\text{criterio de fallo}.
$$

El objetivo no es eliminar las aproximaciones.

Es saber exactamente qué trabajo realizan.
Los ejercicios del tratado pertenecen a familias distintas.

No todos pedirán calcular.

Encontraremos:

- `E-CALC` — cálculo;
- `E-DER` — derivación;
- `E-PROOF` — demostración;
- `E-MOD` — modelización;
- `E-DIM` — análisis dimensional;
- `E-EST` — estimación;
- `E-CON` — comprensión conceptual;
- `E-LIM` — límites y regímenes;
- `E-FAIL` — diagnóstico de fallos;
- `E-NUM` — exploración numérica;
- `E-HIST` — reconstrucción histórica o conceptual.

La solución completa no consistirá solamente en producir el resultado final.

Deberá hacer visible qué tipo de razonamiento exige el problema.
