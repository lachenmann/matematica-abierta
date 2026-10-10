## §10 — Adimensionalización e inferencia dimensional {#fpm-i-02-s10}

### 10.1. Intuir: cambiar de unidades no debería cambiar la forma esencial del problema

En §9 elegimos escalas características.

Ahora utilizaremos esas escalas para construir variables de dimensión uno.

Si:

$$
x
$$

es una longitud y:

$$
L_\ast
$$

una escala característica de longitud, definimos:

$$
\widehat x
=
\frac{x}{L_\ast}.
$$

El número $\widehat x$ ya no pregunta «¿cuántos metros mide $x$?».

Pregunta:

> ¿qué tamaño tiene $x$ respecto de la escala física elegida?

### 10.2. Variable adimensionalizada

::: {.ma-block .ma-definicion #fpm-i-02-d33}
**Definición 33 — Variable adimensionalizada**
Dada una magnitud $Q$ y una escala característica $Q_\ast$ del mismo tipo, la variable

$$
\widehat Q=\frac{Q}{Q_\ast}
$$

es una **variable adimensionalizada** o **variable reducida** asociada a esa escala.
:::

Tenemos:

$$
[\widehat Q]=1.
$$

Pero $\widehat Q$ conserva una interpretación: expresa el tamaño relativo de $Q$.

### 10.3. Adimensionalización

::: {.ma-block .ma-definicion #fpm-i-02-d34}
**Definición 34 — Adimensionalización**
La **adimensionalización** de una relación o modelo es el procedimiento de elegir escalas características para sus magnitudes y reescribirlo en términos de variables de dimensión uno, de modo que queden explícitos los parámetros adimensionales que controlan su forma.
:::

La operación tiene dos objetivos:

1. separar unidades y escalas convencionales de la estructura esencial;
2. identificar los parámetros de dimensión uno que no pueden eliminarse mediante una simple elección de escalas.

::: {.ma-block .ma-metodo #fpm-i-02-mp28}
**Principio 28 — Adimensionalizar reorganiza la física; no la elimina**
Al adimensionalizar desaparecen las unidades explícitas de las variables reducidas, pero permanecen las relaciones físicas y los parámetros de dimensión uno que controlan el modelo.
:::

### 10.4. Ejemplo elemental: una relación cinemática

Consideremos:

$$
x=x_0+vt.
$$

Elegimos:

$$
L_\ast,
\qquad
T_\ast,
$$

y construimos:

$$
V_\ast=\frac{L_\ast}{T_\ast}.
$$

Definimos:

$$
\widehat x=\frac{x}{L_\ast},
\qquad
\widehat x_0=\frac{x_0}{L_\ast},
$$

$$
\widehat t=\frac{t}{T_\ast},
\qquad
\widehat v=\frac{v}{V_\ast}.
$$

Sustituyendo:

$$
L_\ast\widehat x
=
L_\ast\widehat x_0
+
V_\ast T_\ast
\widehat v\widehat t.
$$

Como:

$$
V_\ast T_\ast=L_\ast,
$$

obtenemos:

$$
\boxed{
\widehat x
=
\widehat x_0
+
\widehat v\widehat t.
}
$$

La ecuación conserva su forma y todas las variables son de dimensión uno.

### 10.5. Qué puede quedar después de adimensionalizar

No siempre podemos absorber todos los parámetros.

Si una relación contiene varias escalas independientes, aparecerán razones como:

$$
\varepsilon=\frac{\ell}{L}
$$

o combinaciones más complejas.

Esos parámetros son importantes precisamente porque **sobreviven** al cambio de unidades y a la elección de escalas.

La adimensionalización prepara así el camino hacia:

- inferencia dimensional;
- semejanza;
- grupos $\Pi$ de Buckingham.

### 10.6. Inferir: ¿puede la dimensión ayudarnos a construir una fórmula?

Hasta ahora hemos usado la dimensión principalmente como herramienta de control.

Dada una expresión como

$$
x=x_0+vt,
$$

podemos preguntar si es homogénea.

Pero supongamos ahora que conocemos solamente esto:

- una magnitud objetivo $Q$;
- varias magnitudes relevantes $X_1,\ldots,X_n$;
- sus dimensiones.

¿Podemos obtener alguna información sobre la forma de $Q$ antes de conocer una ley completa?

La respuesta es sí, con una restricción importante.

Si suponemos que la dependencia puede escribirse como un producto de potencias,

$$
Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},
$$

la homogeneidad dimensional produce ecuaciones para los exponentes

$$
\alpha_1,\ldots,\alpha_n.
$$

Esto no deriva toda la física.

Pero puede restringir fuertemente la forma posible.

### 10.7. Representar: del problema físico a un ansatz

La palabra **ansatz** designará aquí una forma propuesta de solución o dependencia que todavía debe justificarse.

::: {.ma-block .ma-definicion #fpm-i-02-d25}
**Definición 25 — Ansatz dimensional monomial**
Un **ansatz dimensional monomial** para una magnitud $Q$ en función de magnitudes $X_1,\ldots,X_n$ es una expresión de la forma

$$
Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},
$$

donde $C$ tiene dimensión uno y los exponentes $\alpha_i$ son desconocidos que se determinan, cuando es posible, imponiendo homogeneidad dimensional.
:::

La hipótesis monomial no es una consecuencia automática de la física.

Es una elección de clase funcional.

Por tanto, el razonamiento correcto tiene dos capas:

$$
\boxed{
\text{hipótesis de forma}
+
\text{restricciones dimensionales}
}
$$

### 10.8. Precisar: convertir dimensiones en ecuaciones para exponentes

Supongamos que

$$
[Q]=T^aL^bM^c,
$$

y

$$
[X_i]=T^{a_i}L^{b_i}M^{c_i}.
$$

Si

$$
Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},
$$

entonces

$$
[Q]
=
[X_1]^{\alpha_1}\cdots[X_n]^{\alpha_n}.
$$

Por tanto,

$$
T^aL^bM^c
=
T^{\sum a_i\alpha_i}
L^{\sum b_i\alpha_i}
M^{\sum c_i\alpha_i}.
$$

La igualdad de dimensiones exige igualdad de exponentes base a base:

$$
a=\sum_i a_i\alpha_i,
$$

$$
b=\sum_i b_i\alpha_i,
$$

$$
c=\sum_i c_i\alpha_i.
$$

Aparece así un **sistema lineal de ecuaciones para los exponentes**.

No necesitamos todavía teoría formal de espacios vectoriales para utilizarlo.

### 10.9. Firma dimensional y sistema lineal

Con la firma de §7,

$$
\mathbf d(Q)
=
(a,b,c,\ldots),
$$

la relación anterior puede escribirse conceptualmente como

$$
\boxed{
\mathbf d(Q)
=
\alpha_1\mathbf d(X_1)
+
\cdots
+
\alpha_n\mathbf d(X_n).
}
$$

Ésta es la razón por la que introdujimos las firmas dimensionales.

El problema de inferir potencias se convierte en un problema de combinar vectores de exponentes.

::: {.ma-block .ma-metodo #fpm-i-02-mp19}
**Principio 19 — La inferencia dimensional restringe exponentes dentro de una clase funcional elegida**
El análisis dimensional puede determinar o restringir los exponentes de un ansatz monomial, pero no justifica por sí solo que la dependencia física real pertenezca a esa clase funcional.
:::

### 10.10. Primer ejemplo: período de un péndulo simple

Supongamos que buscamos una escala temporal $T_p$ para un péndulo y aceptamos, como modelo dimensional mínimo, que depende de:

- una longitud $\ell$;
- una aceleración gravitatoria $g$.

Proponemos

$$
T_p=C\ell^\alpha g^\beta.
$$

Sabemos:

$$
[T_p]=T,
$$

$$
[\ell]=L,
$$

$$
[g]=LT^{-2}.
$$

Entonces

$$
T
=
L^\alpha
(LT^{-2})^\beta.
$$

Por tanto,

$$
T
=
L^{\alpha+\beta}T^{-2\beta}.
$$

Igualamos exponentes.

Para longitud:

$$
\alpha+\beta=0.
$$

Para tiempo:

$$
-2\beta=1.
$$

De la segunda,

$$
\beta=-\frac12.
$$

Luego

$$
\alpha=\frac12.
$$

Por tanto,

$$
\boxed{
T_p=C\sqrt{\frac{\ell}{g}}.
}
$$

El análisis dimensional ha fijado la dependencia en $\ell$ y $g$.

No ha determinado $C$.

### 10.11. Qué falta en el ejemplo del péndulo

La teoría del péndulo simple para oscilaciones pequeñas conduce a

$$
T_p=2\pi\sqrt{\frac{\ell}{g}}.
$$

Pero la dimensión solo produjo

$$
T_p=C\sqrt{\frac{\ell}{g}}.
$$

Por tanto,

$$
\boxed{
C=2\pi
}
$$

no es una conclusión del análisis dimensional.

Debe provenir de información adicional:

- ecuación de movimiento;
- aproximación de ángulo pequeño;
- solución matemática del modelo;
- o evidencia experimental.

Éste es un ejemplo limpio de la frontera del método.

### 10.12. Poner a prueba una intuición: ¿la dimensión determina siempre una única forma?

No.

Supongamos que queremos una cantidad $Q$ con dimensión

$$
[Q]=L
$$

a partir de dos longitudes $x$ e $y$.

Un ansatz monomial sería

$$
Q=Cx^\alpha y^\beta.
$$

La dimensión exige solamente

$$
\alpha+\beta=1.
$$

Hay infinitas soluciones:

$$
(\alpha,\beta)=(1,0),
$$

$$
(0,1),
$$

$$
\left(\frac12,\frac12\right),
$$

y muchas más.

Por tanto, la información dimensional es insuficiente para elegir una sola dependencia.

### 10.13. La aparición de una libertad adimensional

Escribamos

$$
\beta=1-\alpha.
$$

Entonces

$$
Q=Cx^\alpha y^{1-\alpha}.
$$

Factorizamos $y$:

$$
Q
=
y\,C\left(\frac xy\right)^\alpha.
$$

La razón

$$
\frac xy
$$

tiene dimensión uno.

Esto sugiere una forma mucho más general:

$$
\boxed{
Q
=
y\,\Phi\left(\frac xy\right),
}
$$

donde $\Phi$ es una función de dimensión uno.

La dimensión no determina $\Phi$.

Este fenómeno será central en Buckingham $\Pi$.

### 10.14. Segunda definición: libertad funcional adimensional

::: {.ma-block .ma-definicion #fpm-i-02-d26}
**Definición 26 — Libertad funcional adimensional**
Existe **libertad funcional adimensional** cuando las restricciones dimensionales permiten multiplicar una forma dimensionalmente admisible por una función arbitraria de una o más combinaciones de dimensión uno sin alterar la dimensión total.
:::

Por ejemplo, si

$$
[Q]=L
$$

y

$$
[x]=[y]=L,
$$

entonces

$$
Q=y\,\Phi(x/y)
$$

es dimensionalmente admisible para cualquier función adecuada $\Phi$.

La física debe determinar cuál, si alguna, es la función correcta.

::: {.ma-block .ma-metodo #fpm-i-02-mp20}
**Principio 20 — Toda libertad adimensional marca información física aún no determinada**
Cuando el análisis dimensional deja una función arbitraria de cantidades de dimensión uno, esa libertad no es un defecto del método: identifica exactamente la parte de la relación que las dimensiones no pueden fijar.
:::

### 10.15. Resultado formal: condición para un ansatz monomial

::: {.ma-block .ma-enunciado #fpm-i-02-p03}
**Proposición 3 — Criterio de homogeneidad para un ansatz monomial**

Sea

$$
Q=C\prod_{i=1}^n X_i^{\alpha_i},
$$

con $[C]=1$.
Escribamos las dimensiones respecto de una base dimensional $D_1,\ldots,D_r$ como

$$
[Q]
=
\prod_{j=1}^r D_j^{q_j},
$$

y

$$
[X_i]
=
\prod_{j=1}^r D_j^{a_{ji}}.
$$

Entonces el ansatz es dimensionalmente homogéneo si y solo si, para cada $j$,

$$
\boxed{
q_j
=
\sum_{i=1}^n a_{ji}\alpha_i.
}
$$
:::

#### Demostración

Partimos de

$$
Q=C\prod_{i=1}^n X_i^{\alpha_i}.
$$

Como

$$
[C]=1,
$$

obtenemos

$$
[Q]
=
\prod_{i=1}^n [X_i]^{\alpha_i}.
$$

Sustituyendo

$$
[X_i]
=
\prod_{j=1}^rD_j^{a_{ji}},
$$

resulta

$$
[Q]
=
\prod_{i=1}^n
\left(
\prod_{j=1}^rD_j^{a_{ji}}
\right)^{\alpha_i}.
$$

Reagrupando por dimensión base,

$$
[Q]
=
\prod_{j=1}^r
D_j^{\sum_i a_{ji}\alpha_i}.
$$

Pero también

$$
[Q]
=
\prod_{j=1}^rD_j^{q_j}.
$$

Dos expresiones dimensionales son iguales exactamente cuando coinciden los exponentes de cada dimensión base.

Por tanto,

$$
q_j
=
\sum_{i=1}^n a_{ji}\alpha_i
$$

para todo $j$.

Recíprocamente, si estas igualdades se cumplen, entonces las dos expresiones dimensionales coinciden y el ansatz es homogéneo.

$$
\boxed{\text{QED}}
$$

### 10.16. Lectura de la Proposición 3

La Proposición 3 no dice que toda ley física tenga forma monomial.

Dice algo más preciso:

> **si** elegimos una forma monomial, **entonces** la homogeneidad es equivalente a resolver un sistema lineal para sus exponentes.

La hipótesis y la conclusión deben permanecer separadas.

#### Hipótesis estructural

$$
Q=C\prod_iX_i^{\alpha_i}.
$$

#### Restricción dimensional

$$
q_j=\sum_i a_{ji}\alpha_i.
$$

#### Información no obtenida

- validez física del ansatz;
- valor de $C$;
- presencia de funciones adimensionales adicionales;
- régimen de validez;
- signos o correcciones aditivas.

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Explica por qué la Proposición 3 es un teorema matemático correcto y, al mismo tiempo, no constituye una ley física.

Una respuesta adecuada debe distinguir la hipótesis monomial de la información dimensional.
:::

### 10.17. Segundo ejemplo: período orbital

Siguiendo un ejemplo clásico de teoría dimensional,[^s10-zorich-dim] supongamos que una escala temporal orbital $T_o$ depende de:

- radio orbital $r$;
- masa central $M$;
- constante gravitacional $G$.

Proponemos

$$
T_o=Cr^\alpha M^\beta G^\gamma.
$$

Las dimensiones son:

$$
[T_o]=T,
$$

$$
[r]=L,
$$

$$
[M]=M,
$$

$$
[G]=L^3M^{-1}T^{-2}.
$$

Entonces

$$
T
=
L^\alpha
M^\beta
\left(L^3M^{-1}T^{-2}\right)^\gamma.
$$

Agrupando:

$$
T
=
L^{\alpha+3\gamma}
M^{\beta-\gamma}
T^{-2\gamma}.
$$

Igualamos exponentes:

$$
\alpha+3\gamma=0,
$$

$$
\beta-\gamma=0,
$$

$$
-2\gamma=1.
$$

De la última:

$$
\gamma=-\frac12.
$$

Entonces

$$
\beta=-\frac12,
$$

y

$$
\alpha=\frac32.
$$

Por tanto,

$$
\boxed{
T_o
=
C\sqrt{\frac{r^3}{GM}}.
}
$$

La dimensión fija los exponentes dentro del ansatz.

No fija $C$ ni demuestra que $r,M,G$ sean las únicas variables físicamente relevantes.

### 10.18. El problema de las variables omitidas

Ésta es una limitación decisiva.

El análisis dimensional opera sobre **las variables que le damos**.

Si omitimos una magnitud relevante, podemos obtener una fórmula dimensionalmente impecable y físicamente incompleta.

Por ejemplo, si un fenómeno depende además de una viscosidad $\mu$ y no la incluimos, ningún cálculo dimensional posterior puede recuperar mágicamente esa variable.

Por eso la inferencia debe empezar con una pregunta física:

$$
\boxed{
\text{¿qué variables son plausiblemente relevantes para el fenómeno?}
}
$$

La selección de variables es parte de la modelización, no del álgebra dimensional.

### 10.19. Un no-ejemplo: deducir demasiado de una solución única

Supongamos que el sistema dimensional produce una única pareja

$$
(\alpha,\beta).
$$

Sería incorrecto concluir:

> «Hemos demostrado la ley física.»

Lo único demostrado es:

> dentro del ansatz monomial elegido y con las variables incluidas, existe una única combinación de exponentes compatible con las dimensiones.

Todavía puede faltar:

- una constante numérica;
- una función de parámetros adimensionales no incluidos explícitamente;
- otra clase funcional;
- una variable relevante omitida.
