Por eso reconstruir el pasado puede ser un problema mucho más delicado que simplemente «poner tiempo negativo».
Imaginemos que un modelo, a partir de datos actuales, retrodice:

> en una etapa anterior debía haber ocurrido cierto evento observable.

Si posteriormente encontramos un registro independiente de ese pasado —un archivo experimental, una huella material, una observación astronómica conservada— podemos contrastar la retrodicción.

Así, el valor metodológico de una consecuencia física no depende solamente de que apunte hacia el futuro cronológico.

También puede depender de que alcance información **no utilizada para producirla**.
### 8.3. Explicación

Ahora aparece una cuarta palabra.

Supongamos que un modelo:

- ajusta correctamente los datos;
- predice correctamente una observación nueva;
- permite reconstruir estados anteriores.

¿Hemos explicado el fenómeno?

Tal vez.

Pero no automáticamente.

La palabra **explicación** exige preguntar qué parte de la estructura del modelo hace inteligible el resultado.
::: {.ma-block .ma-definicion #fpm-i-01-d25}
**Definición operativa FPM-I-01-D25 — Explicación física**
Llamaremos **explicación física**, en sentido operativo, a un argumento que muestra cómo un fenómeno, regularidad o resultado depende de estructuras, mecanismos, principios, condiciones o relaciones del modelo o de la teoría, de modo que podamos identificar qué elementos son responsables de que el resultado tenga la forma observada.
:::

Esta definición no pretende resolver toda la filosofía de la explicación científica.

Nos basta para distinguir:

$$
\text{«el modelo da el número correcto»}
$$

de:

$$
\text{«podemos identificar por qué el modelo produce este comportamiento»}.
$$
Consideremos un resultado esquemático:

$$
Q=f(a,b,c).
$$

Una explicación útil puede preguntar:

- ¿qué ocurre si cambiamos $a$?;
- ¿el resultado depende realmente de $b$?;
- ¿qué término domina?;
- ¿qué simetría obliga a cierta forma?;
- ¿qué mecanismo produce el signo?;
- ¿qué hipótesis es responsable de la regularidad?;
- ¿qué cambiaría si eliminamos una interacción?

La explicación no consiste solamente en repetir la derivación.

Consiste en reconocer **qué estructura produce qué consecuencia**.

::: {.ma-block .ma-metodo #fpm-i-01-mp14}
**Principio FPM-I-01-MP14 — Explicar exige identificar dependencias**
Una explicación física no queda completa por el solo hecho de reproducir o predecir un resultado; debe hacer visible qué estructura, hipótesis, mecanismo o principio del modelo es responsable del comportamiento que se quiere comprender.
:::
Una derivación correcta puede ser poco explicativa si oculta qué dependencia produce el resultado:

Imaginemos una cadena algebraica de cincuenta pasos que termina en el número observado.

Puede ser matemáticamente impecable.

Pero quizá no sepamos todavía:

- qué hipótesis controla el resultado;
- por qué cambia de signo;
- por qué una variable no aparece;
- qué efecto es dominante;
- qué simplificación sería fatal.

En ese sentido, una derivación larga puede proporcionar una consecuencia sin proporcionar todavía una buena explicación física.

Esto conecta con §4:

una aproximación bien elegida puede ser más explicativa que una fórmula exacta si hace visible la jerarquía de efectos.
Una explicación puede ser mecanística, estructural o unificadora, pero en todos los casos debe mostrar una dependencia que vaya más allá de reproducir un dato conocido.

No todas las explicaciones físicas tienen la misma forma.

#### Explicación causal o mecanística

Identifica una cadena de interacciones o procesos.

#### Explicación estructural

Muestra que un resultado está obligado por cierta geometría, restricción, invariancia o estructura matemática.

#### Explicación por unificación

Muestra que fenómenos aparentemente distintos son casos de un mismo principio.

No fijaremos fronteras rígidas entre estas categorías.

Solo queremos evitar identificar «explicación» con una única clase de relato.
El peligro contrario también existe.

Podemos contar una historia intuitiva y llamarla «explicación».

Pero una explicación física debe estar conectada con el modelo y sus consecuencias.

Si afirmamos que cierto mecanismo produce un resultado, debemos poder preguntar:

> ¿qué cambiaría si ese mecanismo no estuviera presente?

La explicación gana contenido cuando produce diferencias contrastables.

Por eso:

$$
\boxed{
\text{explicación física}
\leftrightarrow
\text{estructura del modelo}
\leftrightarrow
\text{consecuencias}.
}
$$
Supongamos que dos modelos $M_1$ y $M_2$ producen, para todos los datos disponibles:

$$
P_1=P_2.
$$

No se sigue que posean la misma explicación.

Pueden atribuir el comportamiento a estructuras distintas.

Mientras no encontremos una observación capaz de distinguirlas, los datos no seleccionan necesariamente una interpretación única.

Esta situación prepara §9.

Allí mostraremos matemáticamente, en un caso elemental, que una colección finita de datos no determina una única ley funcional.
Existen al menos cuatro situaciones conceptuales.

| Caso | Predice | Explica |
|---|---|---|
| A | sí | sí |
| B | sí | débilmente |
| C | no todavía | propone mecanismo |
| D | reproduce datos | no necesariamente |

#### Caso A

Un modelo predice observaciones nuevas y muestra qué estructura las produce.

#### Caso B

Un modelo entrega resultados precisos, pero su mecanismo físico permanece poco transparente.

#### Caso C

Una hipótesis ofrece una explicación plausible, pero todavía no produce predicciones suficientemente precisas.

#### Caso D

Una fórmula flexible reproduce datos conocidos sin revelar por qué el fenómeno ocurre.

La ciencia intenta, idealmente, mejorar simultáneamente capacidad predictiva y comprensión.

Pero no son la misma propiedad.
Supongamos que observamos:

> dos configuraciones aparentemente diferentes producen el mismo resultado.

Proponemos una explicación:

> ambas comparten una estructura relevante $S$ y las diferencias restantes no intervienen en el fenómeno.

Esta explicación debería permitir una prueba.

Buscamos una tercera configuración que:

- conserve $S$;
- cambie otros aspectos;
- no haya sido usada para construir la hipótesis.

Si el modelo predice que el resultado permanecerá igual y la observación coincide, la explicación gana apoyo.

La idea es:

$$
\boxed{
\text{una buena explicación abre nuevas preguntas contrastables}.
}
$$
### 8.4. Separar construcción y contraste

Recordemos:

$$
\mathcal M
=
(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R),
$$

junto con

$$
\mathfrak I_{\mathcal M}.
$$

Podemos situar nuestras nuevas operaciones.

#### Ajuste

Usa observaciones para fijar parte de:

$$
\theta,\quad I,\quad \mathcal L
$$

o incluso elecciones de estructura.

#### Predicción

Con el modelo ya fijado, deriva consecuencias para casos no utilizados en ese ajuste.

#### Retrodicción

Busca estados o condiciones anteriores compatibles con datos posteriores.

#### Explicación

Identifica qué componentes de

$$
\mathcal M
$$

y de

$$
\mathfrak I_{\mathcal M}
$$

son responsables de la forma del fenómeno.
Podemos representar un buen procedimiento mediante dos conjuntos de datos conceptualmente separados.

#### Datos de construcción

$$
D_{\mathrm{ajuste}}.
$$

Se usan para elegir parámetros o estructura.

#### Datos de contraste

$$
D_{\mathrm{nuevo}}.
$$

No se utilizan para fijar aquello que se va a poner a prueba.

Entonces:

$$
D_{\mathrm{ajuste}}
\longrightarrow
M_{\mathrm{fijado}}
\longrightarrow
P(D_{\mathrm{nuevo}})
\longleftrightarrow
D_{\mathrm{nuevo}}.
$$

No introducimos todavía estadística.

La separación es puramente lógica.
A veces tenemos pocos datos y necesitamos utilizarlos todos para construir el modelo.

Eso puede ser razonable.

Pero debemos describir correctamente lo que hemos logrado.

Podemos afirmar:

> «El modelo es compatible con los datos utilizados para construirlo.»

No debemos exagerar:

> «El modelo ha predicho independientemente todos esos datos.»

Entonces la siguiente tarea científica puede ser buscar:

- nuevos casos;
- nuevas escalas;
- nuevos observables;
- nuevas condiciones experimentales.
Supongamos que un modelo ha funcionado para:

$$
x\in[0,10].
$$

Ahora predecimos para:

$$
x=10.1.
$$

Tal vez sea razonable.

Pero predecir para:

$$
x=10^{12}
$$

puede exigir una justificación completamente distinta.

Antes de aceptar una extrapolación debemos preguntar:

$$
\boxed{
\text{¿seguimos dentro de }\mathcal R\text{?}
}
$$

Una predicción algebraicamente bien calculada puede ser físicamente irrelevante si abandona el régimen de validez.
Supongamos:

$$
P_{\mathrm{modelo}}
\neq
O_{\mathrm{experimento}}.
$$

¿Qué ha fallado?

Todavía no podemos decir.

Podrían estar implicados:

- la teoría;
- el modelo particular;
- un parámetro;
- una condición inicial;
- una aproximación;
- una idealización;
- una regla `[OBS]`;
- el procedimiento experimental.

En §12 formalizaremos esta lógica.

Por ahora la lección es:
