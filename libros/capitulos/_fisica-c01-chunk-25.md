Esto significa que debemos distinguir:

$$
\text{diferencia numérica}
$$

de:

$$
\text{diferencia estructural}.
$$

Dos teorías pueden producir números casi idénticos en cierto régimen y, sin embargo, organizar el mundo mediante conceptos muy diferentes.

Por tanto:

$$
\boxed{
\text{aproximación numérica excelente}
\not\Rightarrow
\text{identidad conceptual}.
}
$$
No utilizaremos una teoría efectiva para concluir automáticamente qué entidades existen «en último término».

Una descripción macroscópica puede hablar de:

- presión;
- temperatura;
- ondas;
- rayos;
- cuerpos rígidos.

Estas entidades pueden ser extremadamente reales y útiles al nivel de descripción correspondiente aunque una teoría más microscópica utilice otras variables.

La pregunta:

> «¿qué es más fundamental?»

no sustituye a:

> «¿qué variables son adecuadas para esta escala y esta pregunta?»
Imaginemos una caja con una enorme cantidad de componentes microscópicos.

Podríamos intentar registrar el estado detallado de cada componente.

Pero nuestra pregunta podría ser solamente:

> «¿cómo cambia una propiedad macroscópica global de la caja?»

Entonces una descripción efectiva puede utilizar pocas variables colectivas.

No afirmamos que los detalles microscópicos hayan desaparecido físicamente.

Afirmamos que:

$$
\boxed{
\text{no son variables necesarias para la pregunta efectiva}.
}
$$

Esto es una aplicación directa de `MP09` y `MP11`.
::: {.ma-block .ma-metodo #fpm-i-01-mp19}
**Principio FPM-I-01-MP19 — Más fundamental no significa más útil para toda tarea**
Una descripción más amplia o más fundamental no reemplaza automáticamente a una descripción efectiva dentro del régimen donde esta última es suficientemente precisa, interpretable y eficiente para la pregunta planteada.
:::

Este principio no autoriza a ignorar teorías más amplias.

Obliga a comparar niveles de descripción con la tarea.
### 11.3. Escala, control y recuperación de límites

La palabra **escala** aparecerá continuamente en física.

Una estructura puede ser visible en una escala y prácticamente irrelevante en otra.

Imaginemos dos longitudes:

$$
\ell
$$

y:

$$
L.
$$

Si:

$$
\ell\ll L,
$$

ciertos detalles asociados con $\ell$ pueden no afectar a una pregunta formulada a escala $L$.

No convertiremos todavía esta idea en una teoría general de escalas.

Solo conservaremos la regla conceptual:

> la relevancia física de un detalle depende de cómo se compara con las escalas de la pregunta.
En §4 vimos que la palabra «pequeño» necesita una referencia.

Una forma común de hacer visible esa referencia es comparar dos cantidades del mismo tipo.

Por ejemplo:

$$
\varepsilon
=
\frac{\ell}{L}.
$$

Si:

$$
\varepsilon\ll1,
$$

puede existir una aproximación controlada por esa separación de escalas.

La expresión:

$$
\varepsilon\ll1
$$

no prueba por sí sola cuál aproximación es correcta.

Pero nos obliga a declarar **qué comparación** sostiene la simplificación.

Esto anticipa el análisis dimensional del capítulo siguiente sin utilizarlo todavía como técnica formal.
Una buena declaración de validez no dice solamente:

> «esto funciona cuando $\varepsilon$ es pequeño».

Debe intentar responder:

1. ¿qué efecto se omitió?;
2. ¿por qué era despreciable?;
3. ¿qué observación indicaría que ya no lo es?;
4. ¿qué descripción más amplia deberíamos considerar entonces?

Este procedimiento transforma una aproximación en algo auditable.
Un modelo puede ser científicamente valioso incluso cuando falla, si sabemos interpretar el fallo.

Supongamos que una aproximación predice bien para:

$$
\varepsilon=0.01,
$$

aceptablemente para:

$$
\varepsilon=0.05,
$$

y mal para:

$$
\varepsilon=0.5.
$$

Si el modelo declaraba desde el comienzo:

$$
\varepsilon\ll1,
$$

el tercer caso no constituye una sorpresa lógica.

Puede ser precisamente la señal esperada de que un efecto omitido se volvió relevante.

Así:

$$
\boxed{
\text{fallar fuera del régimen}
\neq
\text{haber fracasado dentro del régimen}.
}
$$
La utilidad de una descripción efectiva depende de saber qué cambia al salir de su régimen. Una teoría más amplia debe, cuando corresponda, recuperar la anterior como buena aproximación en las condiciones apropiadas.

En física es frecuente que una descripción más amplia reproduzca una teoría anterior bajo condiciones apropiadas.

Esquemáticamente:

$$
T_{\mathrm{amplia}}
\longrightarrow
T_{\mathrm{efectiva}}
$$

cuando ciertas cantidades son pequeñas, grandes o no resolubles a la escala considerada.

Debemos ser cuidadosos con la flecha.

No significa necesariamente inclusión literal:

$$
T_{\mathrm{efectiva}}
\subset
T_{\mathrm{amplia}}.
$$

La relación puede requerir:

- aproximaciones;
- reexpresión de variables;
- promedios;
- eliminación de grados de detalle;
- identificación de un régimen.
Más adelante estudiaremos relatividad especial.

Por ahora nos basta una relación histórica y metodológica.

La mecánica newtoniana funciona extraordinariamente bien para una enorme clase de movimientos ordinarios.

La relatividad especial modifica la estructura de espacio, tiempo y movimiento cuando las velocidades dejan de ser pequeñas frente a la velocidad de la luz.

La conclusión correcta no es:

> «Newton era simplemente inútil».

Es:

> «la teoría newtoniana posee un dominio de validez extremadamente importante, pero no universal».

Y la teoría más amplia debe explicar por qué la descripción anterior funcionaba tan bien dentro de ese dominio.
El régimen de una aproximación concreta y el dominio de una teoría completa no son necesariamente idénticos; tampoco el dominio puede separarse de observables, condiciones y precisión:

También los observables pueden depender del régimen.

Un instrumento diseñado para distinguir estructuras a gran escala puede no detectar detalles microscópicos.

Entonces dos modelos que difieren microscópicamente pueden ser observacionalmente equivalentes para ese procedimiento.

La situación es:

$$
M_1\neq M_2
$$

pero:

$$
O(M_1)=O(M_2)
$$

para el observable disponible.

Esto conecta §11 con §10:

para discriminar modelos necesitamos no solo una diferencia teórica, sino una diferencia observable en un régimen accesible.
Una teoría puede ser muy general y contener dentro de ella varias aproximaciones.

Por ejemplo, una teoría $T$ puede ser aplicable en un dominio amplio:

$$
\mathcal R_T,
$$

pero cierta fórmula aproximada derivada dentro de ella puede requerir:

$$
\mathcal R_A
\subset
\mathcal R_T.
$$

Entonces no debemos confundir:

$$
\text{fracaso de la aproximación}
$$

con:

$$
\text{fracaso de la teoría completa}.
$$

Este punto será esencial en §12.
Tampoco toda discrepancia proviene del régimen.

Podemos estar dentro de:

$$
\mathcal R
$$

y aun así usar condiciones iniciales incorrectas.

Por eso debemos distinguir:

$$
\text{modelo fuera de régimen}
$$

de:

$$
\text{modelo dentro de régimen con datos de entrada incorrectos}.
$$

La diferencia importa porque las revisiones necesarias son distintas.
Supongamos dos modelos:

$$
M_A,
\qquad
M_B.
$$

En cierto régimen sus predicciones difieren en:

$$
0.01\%.
$$

Si nuestro instrumento solo resuelve:

$$
1\%,
$$

ambos pueden ser indistinguibles para la tarea.

Si un nuevo instrumento alcanza:

$$
0.001\%,
$$

la situación cambia.

Por tanto, el dominio de utilidad práctica de una descripción puede depender también de la precisión observacional disponible.

No estamos introduciendo todavía teoría de incertidumbre.

Solo registramos la dependencia lógica.
Dos ejemplos finales muestran por qué «más exactitud» y «más detalle» no son metas independientes de la pregunta:

Supongamos que una tarea exige estimar una cantidad con precisión del:

$$
1\%.
$$

Tenemos:

#### Modelo A

- error esperado menor que:

$$
0.1\%;
$$

- cálculo sencillo.

#### Modelo B

- error esperado muchísimo menor;
- cálculo y datos mucho más complejos.

Si ambos están dentro de su régimen, el modelo A puede ser suficiente.

Elegir B no es incorrecto.

Pero puede ser innecesario.

El criterio no es:

> «usar siempre la teoría más sofisticada disponible».

Es:

> «usar una descripción cuya adecuación sea controlada para la tarea».
Ahora cambiemos la pregunta.

Supongamos que queremos detectar precisamente una corrección del orden de:

$$
0.05\%.
$$

Entonces el modelo A anterior, cuyo error puede alcanzar:

$$
0.1\%,
$$

ya no basta.

El mismo modelo ha pasado de:

> adecuado

a:

> insuficiente

sin que haya cambiado su matemática.

Cambió la pregunta.

Esto refuerza:

$$
\boxed{
\mathcal R
\text{ depende también del criterio de adecuación exigido}.
}
$$
::: {.ma-block .ma-metodo}
**Ficha FPM — Validez y descripción efectiva**
1. **Pregunta:** ¿qué queremos predecir o explicar?
2. **Modelo:** ¿qué descripción estamos usando?
3. **Régimen:** ¿qué condiciones forman $\mathcal R$?
4. **Escalas:** ¿qué comparaciones hacen pequeños o irrelevantes ciertos efectos?
5. **Idealizaciones:** ¿qué se ha omitido exactamente?
6. **Aproximaciones:** ¿qué término o efecto se ha reemplazado o despreciado?
7. **Control:** ¿qué parámetro o condición vigila la aproximación?
8. **Precisión:** ¿qué error es aceptable para la tarea?
9. **Observables:** ¿el instrumento puede detectar la diferencia entre modelos?
10. **Fallo esperado:** ¿qué señal indicaría salida de régimen?
11. **Descripción más amplia:** ¿qué modelo o teoría debería usarse entonces?
12. **Estatus:** ¿el cálculo es exacto dentro de un modelo aproximado?
:::

### 11.4. Ejercicios
