Usaremos la expresión **diccionario de interpretación** para referirnos al conjunto de correspondencias que explican cómo leer físicamente el formalismo.

Por ejemplo, un modelo podría declarar:

$$
x
\longleftrightarrow
\text{posición de una marca del sistema respecto de un origen especificado}.
$$

Esto todavía no dice cómo se mide $x$.

Una regla adicional podría especificar:

$$
[\mathrm{OBS}]
\qquad
x
\longleftrightarrow
\text{valor obtenido al convertir una coordenada de imagen mediante una calibración}.
$$

La primera correspondencia otorga significado físico al símbolo. La segunda lo conecta con un procedimiento de observación.

::: {.ma-block .ma-definicion #fpm-i-01-d17}
**Definición operativa FPM-I-01-D17 — Diccionario de interpretación**
El **diccionario de interpretación** de un modelo es el conjunto de correspondencias, convenciones y reglas que asignan significado físico a sus objetos matemáticos y, cuando corresponde, los conectan con procedimientos de observación.
:::

No debemos imaginar necesariamente este diccionario como una única función matemática bien definida. Es una estructura semántica que puede incluir definiciones, convenciones, calibraciones, identificaciones, reglas experimentales y elecciones de sistema de referencia.

### 5.4. Representar no significa copiar

Una representación matemática no es una réplica del sistema físico.

El número

$$
2.3
$$

no posee masa, temperatura ni ubicación espacial. Una función no «es» una cuerda. Un punto no «es» una partícula material.

Lo que hacemos es establecer una correspondencia útil entre aspectos del sistema y estructuras matemáticas.

Por eso conviene evitar frases como:

> «La partícula es el punto $P$.»

Es más preciso decir:

> «En este modelo, la posición de la partícula se representa mediante el punto $P$.»

La diferencia verbal protege una diferencia conceptual:

$$
\boxed{
\text{objeto físico}
\neq
\text{objeto matemático que lo representa}.
}
$$

### 5.5. Una representación puede perder información

En §4 vimos que toda abstracción puede omitir estructura.

La representación matemática hereda esa selección.

Si modelamos un cuerpo por un punto,

$$
\text{cuerpo extendido}
\longrightarrow
P,
$$

ya no podemos recuperar del punto la forma del cuerpo, su orientación, su distribución interna, su color o su textura.

La representación es deliberadamente no invertible.

Esto no es un defecto accidental. Es parte del propósito del modelo.

Una representación útil puede olvidar precisamente aquello que no necesitamos.

### 5.6. Una representación puede introducir estructura adicional

También puede ocurrir lo contrario.

Al elegir coordenadas, bases, parámetros o variables auxiliares podemos introducir estructura matemática que no corresponde directamente a una propiedad física independiente.

Por ejemplo, dos descripciones matemáticas distintas pueden representar la misma situación física.

Más adelante veremos esto con gran profundidad: distintos sistemas de coordenadas, distintas bases, transformaciones de referencia y, mucho más adelante, representaciones matemáticas diferentes que conservan los mismos observables físicos.

Por ahora fijamos una advertencia:

$$
\boxed{
\text{diferencia entre descripciones matemáticas}
\not\Rightarrow
\text{diferencia física}.
}
$$

La cuestión «¿qué parte del formalismo representa algo físicamente distinguible?» será recurrente.

### 5.7. Una plantilla mínima de lectura

Necesitamos ahora una manera compacta de preguntar qué contiene un modelo.

Introduciremos la notación

$$
\boxed{
\mathcal M
=
(\mathcal S,\,X,\,\theta,\,\mathcal L,\,I,\,B,\,\mathcal R)
}
$$

como **plantilla provisional de lectura**.

No es una definición axiomática universal de «modelo físico».

No afirmamos que toda teoría física pueda o deba reducirse literalmente a una séptupla de esta forma.

La notación funciona como una lista de control. Nos obliga a preguntar si hemos especificado los componentes necesarios para comprender un problema.

### 5.8. $\mathcal S$: estados admitidos

Ya introdujimos el espacio de estados en §3.

Aquí lo situamos dentro de la plantilla:

$$
\mathcal S
=
\{\text{estados admitidos por el modelo}\}.
$$

El adjetivo **admitidos** importa.

Un modelo no tiene por qué permitir toda asignación imaginable de números a sus variables.

Puede haber restricciones.

Si dos variables $x$ e $y$ deben satisfacer

$$
x^2+y^2=L^2,
$$

entonces el estado

$$
(x,y)=(0,0)
$$

no es admisible cuando $L\neq0$.

Por tanto, especificar variables no basta. Debemos especificar qué combinaciones representan estados físicamente permitidos **dentro del modelo**.

### 5.9. $X$: variables y observables modelados

Usaremos $X$ como símbolo colectivo para la familia de cantidades que el modelo emplea para describir o interrogar el sistema.

Puede incluir variables de estado, observables, variables de control y cantidades derivadas.

No exigiremos que todos estos objetos tengan la misma estructura matemática.

En un modelo elemental, un observable puede ser una función

$$
O:\mathcal S\to V.
$$

En teorías posteriores esta representación tendrá que modificarse.

Por eso $X$ no es una «lista universal de coordenadas». Es un contenedor conceptual para las cantidades relevantes del modelo.

### 5.10. $\theta$: parámetros

Escribiremos esquemáticamente

$$
\theta=(\theta_1,\ldots,\theta_k)
$$

para reunir parámetros.

Por ejemplo, distintos miembros de una familia de modelos pueden diferir en una longitud, una masa, una constante de acoplamiento o una propiedad material.

La plantilla distingue

$$
s\in\mathcal S
$$

como estado de una realización, de

$$
\theta
$$

como parámetros que caracterizan la familia o que se consideran fijos durante el problema.

Pero recordemos §3: la misma magnitud puede cambiar de papel en otro modelo.

### 5.11. $\mathcal L$: leyes y relaciones del modelo

El símbolo

$$
\mathcal L
$$

reunirá las relaciones que el modelo utiliza para vincular estados, variables y parámetros.

Todavía no definiremos formalmente qué diferencia una **ley**, un **principio**, un **postulado** o una **ecuación constitutiva**. Eso corresponde a §§6–7.

Por ahora basta advertir que $\mathcal L$ puede contener relaciones de estatus muy distinto.

Una relación puede ser empírica, postulada, definitoria o derivada matemáticamente de otras.

Por eso nunca debemos leer

$$
\mathcal L=\{\text{ecuaciones}\}
$$

como si todas las ecuaciones tuvieran el mismo origen epistemológico.

La sección siguiente desarrollará precisamente este problema.

### 5.12. $I$: condiciones iniciales

Muchos modelos dinámicos necesitan especificar una condición del sistema en un instante elegido como inicial.

Representaremos ese bloque mediante

$$
I.
$$

La etiqueta canónica será

$$
[\mathrm{IC}].
$$

Pero no toda condición inicial es una ley.

Si escribimos

$$
x(0)=a,
$$

la forma algebraica no nos dice si se trata de un dato experimental, una elección de ejemplo, una condición impuesta o una consecuencia de otra relación.

La expresión se vuelve condición inicial por el papel que cumple en el problema.

No desarrollaremos todavía teoría de problemas de valor inicial. Solo fijamos el casillero conceptual.

### 5.13. $B$: condiciones de frontera

En problemas extendidos espacialmente puede ser necesario especificar qué ocurre en una frontera.

Representaremos esas condiciones por

$$
B.
$$

La etiqueta canónica será

$$
[\mathrm{BC}].
$$

Ejemplos conceptuales posteriores incluirán preguntas como: ¿los extremos están fijos?, ¿qué valor se prescribe en la superficie?, ¿puede atravesar algo la frontera?, ¿qué ocurre en la interfaz entre dos medios?

No necesitamos todavía resolver ninguna ecuación con estas condiciones.

El punto es comprender que

$$
\boxed{
\text{ley}
+
\text{condiciones}
}
$$

suele contener más información que la ley aislada.

### 5.14. $\mathcal R$: régimen de validez

El componente

$$
\mathcal R
$$

recoge las condiciones bajo las cuales esperamos que el modelo represente adecuadamente el fenómeno para la pregunta planteada.

Puede incluir restricciones sobre escalas, velocidades, amplitudes, intensidades, tiempos, precisión o propiedades del medio.

En §4 introdujimos el concepto cualitativamente. En `FPM-I-06` aprenderemos a formular muchos regímenes cuantitativamente.

Por ahora queremos que ningún modelo aparezca como si afirmara:

> «Esta descripción vale para todo sistema, en toda escala y con precisión ilimitada.»

### 5.15. La tupla no contiene todavía toda la semántica

La plantilla

$$
\mathcal M
=
(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R)
$$

es útil, pero sería un error pensar que ya hemos capturado toda la física.

Falta algo esencial:

$$
\boxed{\text{¿qué significa cada componente?}}
$$

Por eso la tupla debe viajar acompañada de un diccionario de interpretación

$$
\mathfrak I_{\mathcal M}.
$$

Usaremos esta notación de manera informal:

$$
\mathfrak I_{\mathcal M}
=
\{\text{significados físicos y reglas de conexión asociados a }\mathcal M\}.
$$

Así, la unidad mínima de lectura será más bien

$$
\boxed{
(\mathcal M,\mathfrak I_{\mathcal M})
}
$$

y no la tupla matemática desnuda.

Esto incorpora una consecuencia de §2: una teoría física necesita conexiones con observaciones, no solo ecuaciones.

### 5.16. Un modelo puede estar incompleto

También debemos distinguir

$$
\text{componente innecesario}
$$

de

$$
\text{componente necesario pero todavía no especificado}.
$$
