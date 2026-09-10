La comparación entre modelos puede organizarse en tres capas.

#### Coherencia mínima

Antes de comparar virtudes, debemos eliminar candidatos que fallan requisitos básicos.

Podemos pensar esta primera capa como una serie de filtros.

##### Filtro 1 — Coherencia matemática interna

El modelo no debe contradecir sus propias definiciones, restricciones y condiciones.

Si declara:

$$
s\in\mathcal S
$$

pero luego exige un estado que no pertenece a $\mathcal S$, el problema es interno.

No necesitamos ningún experimento para detectarlo.

##### Filtro 2 — Compatibilidad con la evidencia relevante

Si un modelo predice algo incompatible con observaciones fiables dentro del régimen que afirma describir, necesita revisión.

##### Filtro 3 — Interpretación física suficiente

Los símbolos que se comparan con datos deben tener una interpretación y una conexión observacional.

##### Filtro 4 — Régimen pertinente

No debemos juzgar un modelo usando una condición que él mismo no pretende describir sin antes preguntar si estamos extendiéndolo legítimamente.

Estos filtros no garantizan que el modelo sea correcto.

Solo impiden mantener candidatos que ya fallan requisitos elementales.
#### Adecuación y estructura

Una vez superados los filtros mínimos, pueden importar varios criterios que no forman un algoritmo universal:

| Criterio | Pregunta de control |
|---|---|
| economía de estructura | ¿cuánta estructura independiente se introduce para obtener las consecuencias? |
| integración teórica | ¿cómo se relaciona con conocimiento ya bien establecido en el mismo régimen? |
| poder explicativo | ¿qué dependencias, mecanismos o estructuras comunes hace visibles? |
| alcance | ¿qué diversidad de fenómenos organiza sin ocultar su régimen? |
| robustez | ¿la conclusión depende críticamente de ajustes irrelevantes o excesivamente delicados? |
| acceso observacional | ¿cómo se conectan sus predicciones con procedimientos `[OBS]`? |

La simplicidad es un criterio metodológico, no una demostración de verdad.

Si dos modelos describen igual de bien los fenómenos relevantes, puede ser razonable preferir el que requiere menos estructura no justificada.

Pero debemos formular esta idea con cuidado.

**Más simple** no significa necesariamente:

- fórmula más corta;
- menos símbolos impresos;
- cálculo más fácil;
- menor número de páginas.

Una expresión compacta puede ocultar muchas hipótesis.

Una expresión larga puede desarrollar explícitamente una estructura sencilla.

La pregunta útil es:

> ¿cuánta estructura independiente debemos introducir para obtener las consecuencias observadas?

Esta idea suele llamarse **parsimonia**.

La utilizaremos como criterio metodológico, no como ley lógica de la naturaleza.
Un modelo no vive aislado.

Puede compartir estructuras con teorías que ya explican otros fenómenos.

Si un candidato requiere abandonar relaciones bien contrastadas en el mismo régimen, ese costo debe ser visible.

En cambio, un modelo que surge naturalmente de un marco ya exitoso puede tener una ventaja metodológica.

Esto tampoco constituye una prueba automática.

Una teoría nueva puede precisamente mostrar que un marco anterior era limitado.

La regla correcta es más modesta:

$$
\boxed{
\text{compatibilidad teórica amplia}
=
\text{evidencia estructural relevante},
}
$$

no:

$$
\boxed{
\text{compatibilidad con lo conocido}
=
\text{imposibilidad de revisión}.
}
$$
En §8 distinguimos predecir de explicar.

Dos modelos pueden reproducir el mismo dato y, sin embargo, uno puede mostrar por qué ocurre el patrón.

Por ejemplo, una relación ajustada puede decir:

$$
Y=f(X).
$$

Otro modelo puede además mostrar que esa forma surge de:

- una simetría;
- una restricción;
- una interacción;
- una estructura común a varios fenómenos.

El segundo no es mejor únicamente por contar una historia más atractiva.

Su explicación gana valor si organiza consecuencias que pueden ponerse a prueba.

Por eso el poder explicativo está estrechamente ligado a la capacidad de generar nuevas preguntas.
Un modelo que explica varios fenómenos con una misma estructura puede ser preferible a una colección de reglas independientes.

Pero mayor alcance no significa validez ilimitada.

Debemos conservar:

$$
\mathcal R.
$$

Un modelo puede unificar mucho dentro de cierto régimen y fallar fuera de él.

La pregunta correcta es:

> ¿qué diversidad de fenómenos explica con la misma estructura, y bajo qué condiciones?

No:

> ¿puede aplicarse sin restricciones a todo?
Supongamos que una conclusión depende de que un parámetro tenga exactamente el valor:

$$
a=1.0000000000.
$$

Si un cambio minúsculo de $a$ destruye completamente el fenómeno, debemos preguntarnos si el mecanismo propuesto es físicamente estable frente a las variaciones inevitables de preparación y modelización.

No desarrollaremos todavía una teoría matemática de estabilidad.

Usaremos **robustez** en sentido cualitativo:

> una conclusión es robusta si no depende críticamente de elecciones irrelevantes o ajustes excesivamente delicados para el fenómeno estudiado.

La falta de robustez no invalida automáticamente un modelo.

Algunos fenómenos físicos son genuinamente sensibles.

Pero, si la sensibilidad es esencial, el modelo debe hacerla visible en lugar de esconderla.
Un modelo puede introducir una cantidad que matemáticamente está perfectamente definida.

Pero si la comparación con el mundo depende de ella, necesitamos preguntar:

> ¿cómo se observa?

En términos de §5:

$$
\mathfrak I_{\mathcal M}
$$

debe ser suficientemente explícito.

Y en términos de §6:

$$
[\mathrm{OBS}]
$$

debe conectar la cantidad con un procedimiento.

Un modelo cuyas predicciones no poseen ninguna conexión observacional accesible puede seguir teniendo interés teórico.

Pero no podemos contar esas predicciones como contrastes experimentales realizados.
#### Fecundidad predictiva

El criterio más fuerte aparece cuando los modelos, compatibles con los datos actuales, divergen en una situación todavía no observada.

Volvamos a §9.

Supongamos:

$$
f(x_i)=g(x_i)
$$

para todos los puntos medidos.

Los modelos son indistinguibles en la evidencia disponible.

La estrategia natural es buscar un valor $x_\ast$ tal que:

$$
f(x_\ast)\neq g(x_\ast).
$$

Entonces los modelos producen predicciones rivales.

Si podemos realizar una observación en $x_\ast$, obtenemos una prueba potencialmente discriminante.

Esta idea merece una definición propia.

::: {.ma-block .ma-definicion #fpm-i-01-d27}
**Definición operativa FPM-I-01-D27 — Experimento discriminante**
Un **experimento discriminante** entre dos o más modelos es un experimento diseñado en condiciones donde los modelos candidatos producen consecuencias observacionales distinguibles, de modo que el resultado pueda favorecer algunos candidatos frente a otros.
:::

La palabra **distinguibles** importa.

No basta que las fórmulas sean diferentes.

La diferencia debe poder conectarse, mediante `[OBS]`, con una observación capaz de separarlas.
Este principio cambia la estrategia experimental.

Si queremos distinguir $M_1$ y $M_2$, no conviene repetir indefinidamente condiciones donde:

$$
P_1=P_2.
$$

Debemos buscar, cuando sea posible:

$$
P_1\neq P_2.
$$

::: {.ma-block .ma-metodo #fpm-i-01-mp17}
**Principio FPM-I-01-MP17 — Para discriminar modelos, buscar divergencia predictiva**
Si varios modelos son compatibles con los datos existentes, una prueba informativa debe buscar condiciones accesibles dentro de sus regímenes pertinentes en las que sus predicciones observables difieran.
:::

El principio contiene tres restricciones:

1. **condiciones accesibles**;
2. **regímenes pertinentes**;
3. **diferencias observables**.

Una diferencia puramente formal que no puede medirse no basta todavía.
### 10.3. Diseñar una prueba discriminante

En §9 vimos los datos:

$$
(0,0),
\qquad
(1,1).
$$

Consideremos:

$$
M_1:\quad f(x)=x,
$$

y:

$$
M_2:\quad g(x)=x^2.
$$

Ambos reproducen:

$$
f(0)=g(0)=0,
$$

$$
f(1)=g(1)=1.
$$

Repetir observaciones únicamente en $x=0$ y $x=1$ no añade capacidad discriminante.

Probemos:

$$
x_\ast=\frac12.
$$

Entonces:

$$
f\left(\frac12\right)
=
\frac12,
$$

mientras:

$$
g\left(\frac12\right)
=
\frac14.
$$

Las predicciones son diferentes.

Por tanto, una observación en:

$$
x=\frac12
$$

puede distinguir los modelos, siempre que el procedimiento experimental sea capaz de separar una salida próxima a $1/2$ de una próxima a $1/4$.
En §9 también usamos:

$$
x=2.
$$

Allí las predicciones eran distintas.

¿Por qué ahora preferimos:

$$
x=\frac12?
$$

Porque los datos originales estaban en:

$$
x=0
$$

y:

$$
x=1.
$$

Una medición intermedia puede mantenerse más cerca del régimen ya explorado.

Ir directamente a:

$$
x=2
$$

podría introducir una dificultad adicional:

> ¿estamos extrapolando fuera del dominio donde ambos modelos eran plausibles?

Un buen experimento discriminante intenta cambiar **lo necesario para separar los modelos** sin introducir simultáneamente nuevas ambigüedades evitables.
Supongamos ahora:

$$
f(x_\ast)=1.000000,
$$

$$
g(x_\ast)=1.000001.
$$

Matemáticamente:

$$
f(x_\ast)\neq g(x_\ast).
$$

Pero si el instrumento solo permite distinguir diferencias del orden de:

$$
0.01,
$$

el experimento no separará operativamente ambos modelos.

No desarrollaremos aquí teoría de errores.

Solo fijamos la lógica:

$$
\boxed{
\text{predicciones matemáticamente distintas}
\not\Rightarrow
\text{predicciones experimentalmente distinguibles}.
}
$$
