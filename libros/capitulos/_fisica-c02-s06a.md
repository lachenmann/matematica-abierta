## §6 — Homogeneidad dimensional {#fpm-i-02-s06}

### 6.1. Una igualdad física debe sobrevivir al cambio de unidades

En §5 vimos que una magnitud conserva su dimensión cuando cambiamos las unidades concretas con que expresamos sus magnitudes base.[^s6-bipm-homogeneity]

Por ejemplo,

$$
[v]=LT^{-1}
$$

tanto si escribimos una velocidad en

$$
\mathrm{m\,s^{-1}}
$$

como si la escribimos en

$$
\mathrm{km\,h^{-1}}.
$$

Ahora preguntaremos qué ocurre con una **ecuación física completa**.

Consideremos

$$
x=x_0+vt.
$$

Dimensionalmente,

$$
[x]=L,
$$

$$
[x_0]=L,
$$

y

$$
[vt]
=
[v][t]
=
LT^{-1}T
=
L.
$$

Todos los términos poseen dimensión $L$.

En cambio, si alguien escribiera

$$
x=x_0+vt^2,
$$

tendríamos

$$
[vt^2]
=
LT^{-1}T^2
=
LT.
$$

La suma intentaría combinar:

$$
L
$$

con

$$
LT.
$$

El problema aparece antes de sustituir números.

La expresión no conserva una interpretación física coherente bajo cambios de unidades.

### 6.2. Homogeneidad dimensional

::: {.ma-block .ma-definicion #fpm-i-02-d17}
**Definición 17 — Ecuación dimensionalmente homogénea**
Una ecuación física es **dimensionalmente homogénea** cuando todos los términos que se suman o se igualan poseen la misma dimensión, una vez incorporadas las dimensiones de todos los parámetros y constantes físicas que aparecen en ellos.
:::

Por ejemplo,

$$
x=x_0+vt
$$

es dimensionalmente homogénea porque

$$
[x]=[x_0]=[vt]=L.
$$

La expresión

$$
x=x_0+vt^2
$$

no lo es porque

$$
[x]=[x_0]=L
$$

mientras

$$
[vt^2]=LT.
$$

La homogeneidad dimensional es una condición estructural sobre la ecuación.

No depende de los valores numéricos particulares que sustituyamos.[^s6-zorich-homogeneity]

### 6.3. Sumar magnitudes exige compatibilidad

En §2 distinguimos **tipo de magnitud** y **dimensión**.

Dos magnitudes del mismo tipo tienen la misma dimensión.[^s6-vim-dimension]

La recíproca, como vimos en §5, no es cierta.

Esto nos obliga a formular dos niveles de control.

#### Nivel 1 — Condición dimensional

Para que una suma física

$$
A+B
$$

pueda tener sentido, es necesario que

$$
[A]=[B].
$$

#### Nivel 2 — Compatibilidad física

La igualdad dimensional no basta por sí sola.

También debemos saber que $A$ y $B$ representan magnitudes que el modelo permite combinar mediante esa operación.

Por ejemplo, presión y densidad de energía tienen la misma dimensión:

$$
ML^{-1}T^{-2}.
$$

Pero la igualdad dimensional por sí sola no autoriza cualquier suma entre ambas fuera de una relación física que le otorgue significado.

::: {.ma-block .ma-metodo #fpm-i-02-mp11}
**Principio 11 — La homogeneidad dimensional es necesaria para la suma física**
Los términos que se suman o se comparan mediante una igualdad física deben poseer dimensiones compatibles. Si sus dimensiones difieren, la ecuación no puede representar una relación física independiente de la elección de unidades.
:::

### 6.4. De la dimensión al factor de reescalado

En §5 escribimos

$$
[Q]
=
T^\alpha
L^\beta
M^\gamma
I^\delta
\Theta^\varepsilon
N^\zeta
J^\eta.
$$

Supongamos ahora que cambiamos independientemente los tamaños de las siete unidades base:

$$
u_T'=\lambda_Tu_T,
$$

$$
u_L'=\lambda_Lu_L,
$$

$$
u_M'=\lambda_Mu_M,
$$

$$
u_I'=\lambda_Iu_I,
$$

$$
u_\Theta'=\lambda_\Theta u_\Theta,
$$

$$
u_N'=\lambda_Nu_N,
$$

$$
u_J'=\lambda_Ju_J,
$$

con todos los factores positivos.

Por la Proposición 1, el valor numérico de una magnitud base cambia de manera inversa al tamaño de su unidad.

Por tanto, una magnitud con dimensión

$$
T^\alpha
L^\beta
M^\gamma
I^\delta
\Theta^\varepsilon
N^\zeta
J^\eta
$$

adquiere el factor numérico

$$
\lambda_T^{-\alpha}
\lambda_L^{-\beta}
\lambda_M^{-\gamma}
\lambda_I^{-\delta}
\lambda_\Theta^{-\varepsilon}
\lambda_N^{-\zeta}
\lambda_J^{-\eta}.
$$

Definiremos, solo como notación auxiliar,

$$
\chi_Q(\lambda)
=
\lambda_T^{-\alpha}
\lambda_L^{-\beta}
\lambda_M^{-\gamma}
\lambda_I^{-\delta}
\lambda_\Theta^{-\varepsilon}
\lambda_N^{-\zeta}
\lambda_J^{-\eta}.
$$

Entonces, bajo el cambio de unidades,

$$
\{Q\}'
=
\chi_Q(\lambda)\{Q\}.
$$

La función $\chi_Q$ codifica cómo cambia el **valor numérico** de $Q$ al reescalar las unidades base.

No es una nueva magnitud física.

Es una herramienta algebraica para la demostración.

### 6.5. Por qué una suma obliga a un mismo factor

Consideremos una relación física

$$
A+B=C.
$$

En cierto sistema de unidades, sus valores numéricos satisfacen

$$
a+b=c.
$$

Después de reescalar las unidades base, obtendríamos

$$
\chi_A a
+
\chi_B b
=
\chi_C c.
$$

Como

$$
c=a+b,
$$

la ecuación transformada es

$$
\chi_A a
+
\chi_B b
=
\chi_C(a+b).
$$

Reordenando:

$$
(\chi_A-\chi_C)a
+
(\chi_B-\chi_C)b
=
0.
$$

Si la relación física pretende ser una ley y no una coincidencia numérica para un único par especial $(a,b)$, debe mantener su forma para las realizaciones admisibles del modelo.

En particular, si $a$ y $b$ pueden variar independientemente dentro de una familia no degenerada de realizaciones, la igualdad anterior solo puede mantenerse para todas ellas si

$$
\chi_A=\chi_C
$$

y

$$
\chi_B=\chi_C.
$$

Por tanto,

$$
\chi_A=\chi_B=\chi_C.
$$

La suma exige que todos sus términos transformen de la misma manera al cambiar las unidades.

### 6.6. Igualdad de factores implica igualdad de exponentes

Supongamos ahora que

$$
\chi_A(\lambda)=\chi_B(\lambda)
$$

para **todo** cambio independiente de unidades base.

Escribamos

$$
[A]
=
T^{\alpha_A}
L^{\beta_A}
M^{\gamma_A}
I^{\delta_A}
\Theta^{\varepsilon_A}
N^{\zeta_A}
J^{\eta_A},
$$

y

$$
[B]
=
T^{\alpha_B}
L^{\beta_B}
M^{\gamma_B}
I^{\delta_B}
\Theta^{\varepsilon_B}
N^{\zeta_B}
J^{\eta_B}.
$$

Entonces

$$
\lambda_T^{-\alpha_A}
\lambda_L^{-\beta_A}
\cdots
\lambda_J^{-\eta_A}
=
\lambda_T^{-\alpha_B}
\lambda_L^{-\beta_B}
\cdots
\lambda_J^{-\eta_B}
$$

para todo conjunto de factores positivos.

Mantengamos todas las $\lambda$ iguales a $1$ salvo $\lambda_T$.

Obtenemos

$$
\lambda_T^{-\alpha_A}
=
\lambda_T^{-\alpha_B}
$$

para todo

$$
\lambda_T>0.
$$

Por tanto,

$$
\alpha_A=\alpha_B.
$$

Repitiendo el argumento una dimensión base a la vez,

$$
\beta_A=\beta_B,
$$

$$
\gamma_A=\gamma_B,
$$

$$
\delta_A=\delta_B,
$$

$$
\varepsilon_A=\varepsilon_B,
$$

$$
\zeta_A=\zeta_B,
$$

$$
\eta_A=\eta_B.
$$

Luego

$$
[A]=[B].
$$

Esta observación completa la idea necesaria para nuestro segundo resultado formal.

### 6.7. Segunda proposición formal del capítulo

::: {.ma-block .ma-enunciado #fpm-i-02-p02}
**Proposición 2 — Homogeneidad dimensional necesaria bajo cambios independientes de unidades base**

Considérese una relación física de la forma

$$
Q_1+\cdots+Q_r
=
R_1+\cdots+R_s,
$$

donde cada término tiene una dimensión bien definida respecto de un sistema de magnitudes base.

Supongamos:

1. que la relación representa una ley o familia de realizaciones no degenerada, y no una igualdad numérica accidental;
2. que su forma numérica debe conservarse bajo cambios multiplicativos independientes de las unidades base;
3. que los términos que aparecen en cada suma pueden variar suficientemente como para que la validez de la relación no dependa de una cancelación especial entre valores numéricos concretos.

Entonces todos los términos que participan aditivamente deben poseer la misma dimensión:

$$
[Q_1]
=
\cdots
=
[Q_r]
=
[R_1]
=
\cdots
=
[R_s].
$$
:::

#### Demostración

Basta demostrar la afirmación para una relación elemental

$$
A+B=C,
$$

porque una suma finita puede reagruparse y el mismo argumento se aplica a cada término.

Sea

$$
a+b=c
$$

la ecuación entre valores numéricos en un sistema de unidades.

Bajo un cambio independiente de las unidades base, los valores numéricos cambian según los factores dimensionales:

$$
a'
=
\chi_Aa,
$$

$$
b'
=
\chi_Bb,
$$

$$
c'
=
\chi_Cc.
$$

La invariancia de forma exige

$$
a'+b'=c'.
$$

Por tanto,

$$
\chi_Aa+\chi_Bb
=
\chi_Cc.
$$

Como

$$
c=a+b,
$$

tenemos

$$
(\chi_A-\chi_C)a
+
(\chi_B-\chi_C)b
=
0.
$$

Por la hipótesis de no degeneración, esta relación debe mantenerse para una familia en la que los valores de $a$ y $b$ no están fijados por una cancelación accidental.

Así,

$$
\chi_A=\chi_C
$$

y

$$
\chi_B=\chi_C.
$$

Luego

$$
\chi_A=\chi_B=\chi_C
$$

para todo cambio independiente de las unidades base.

Ahora variamos una unidad base cada vez.

La igualdad de los factores de reescalado para todo valor positivo de cada $\lambda$ obliga a que coincidan todos los exponentes dimensionales de $A$, $B$ y $C$.

Por tanto,

$$
[A]=[B]=[C].
$$

El mismo argumento se aplica a cualquier suma finita de términos.

Así,

$$
\boxed{
[Q_1]
=
\cdots
=
[Q_r]
=
[R_1]
=
\cdots
=
[R_s].
}
$$

$$
\boxed{\text{QED}}
$$

### 6.8. Qué demuestra exactamente la Proposición 2

La Proposición 2 establece una **condición necesaria** para una ecuación física aditiva que deba conservar su forma bajo cambios de unidades.

No demuestra que toda ecuación dimensionalmente homogénea sea físicamente correcta.

Por ejemplo,

$$
x=x_0+vt
$$

y

$$
x=x_0+2vt
$$

son ambas dimensionalmente homogéneas.

También lo es

$$
x=x_0-17vt.
$$

La dimensión no decide cuál, si alguna, describe un sistema físico concreto.

Por tanto:

$$
\boxed{
\text{homogeneidad dimensional}
\not\Rightarrow
\text{verdad física}.
}
$$

::: {.ma-block .ma-metodo #fpm-i-02-mp12}
**Principio 12 — Pasar el control dimensional no prueba una ley**
La homogeneidad dimensional es una condición necesaria de consistencia para una amplia clase de ecuaciones físicas, pero no constituye una demostración de su corrección empírica, de su interpretación ni de su dominio de validez.
:::

### 6.9. Un error dimensional sí puede ser decisivo

La asimetría es importante.

Si una ecuación falla el control dimensional, entonces tenemos una razón estructural para rechazarla **tal como está escrita**.

Si una ecuación pasa el control dimensional, solo sabemos que ha superado una prueba necesaria.

En símbolos:

$$
\boxed{
\text{inhomogeneidad}
\Longrightarrow
\text{ecuación físicamente inadmisible tal como está escrita},
}
$$

mientras que

$$
\boxed{
\text{homogeneidad}
\not\Longrightarrow
\text{ecuación físicamente correcta}.
}
$$

Esta asimetría convierte el análisis dimensional en una excelente herramienta de auditoría.

### 6.10. Ejemplo: cinemática elemental

Consideremos

$$
x=x_0+v_0t+\frac12 at^2.
$$

Sin derivarla todavía desde una teoría del movimiento, podemos auditarla dimensionalmente.

Tenemos:

$$
[x]=L,
$$

$$
[x_0]=L.
$$

Además,

$$
[v_0t]
=
LT^{-1}T
=
L,
$$

y

$$
[at^2]
=
LT^{-2}T^2
=
L.
$$

El factor

$$
\frac12
$$

es un número puro y no modifica la dimensión.

Por tanto,

$$
\boxed{
[x]
=
[x_0]
=
[v_0t]
=
[at^2]
=
L.
}
$$

La ecuación pasa el control de homogeneidad.

Esto no constituye todavía una derivación física de la fórmula.

Solo demuestra que su estructura aditiva es dimensionalmente compatible.

### 6.11. Ejemplo de ecuación defectuosa

Supongamos que aparece

$$
x=x_0+v_0t+at.
$$

Los dos primeros términos tienen dimensión:

$$
L.
$$

Pero

$$
[at]
=
LT^{-2}T
=
LT^{-1}.
$$

Por tanto,

$$
[at]\neq L.
$$

La suma intenta combinar longitud con velocidad.

La ecuación no puede ser correcta tal como está escrita.

No necesitamos datos experimentales para detectar este problema.

### 6.12. Unidades iguales no bastan para justificar una suma

En §5 vimos que presión y densidad de energía poseen la misma dimensión:

$$
ML^{-1}T^{-2}.
$$

En SI ambas pueden incluso expresarse mediante unidades algebraicamente equivalentes:

$$
\mathrm{Pa}
=
\mathrm{J\,m^{-3}}.
$$

Sin embargo, la Proposición 2 no dice:

> «Toda magnitud con la misma dimensión puede sumarse físicamente con cualquier otra.»

Dice únicamente que una suma físicamente significativa debe superar el control dimensional.

Después debemos verificar también:

- el tipo de magnitud;
- la interpretación del modelo;
- la procedencia de cada término;
- el estatus físico de la ecuación.

Así, la homogeneidad es un filtro estructural, no un diccionario semántico completo.

### 6.13. Constantes numéricas y constantes físicas

Consideremos

$$
Q=2X.
$$

El factor $2$ es un número puro.

Por tanto,

$$
[Q]=[X].
$$

Pero en

$$
Q=kX,
$$

no podemos suponer que $k$ sea adimensional.

Su dimensión debe satisfacer

$$
[k]
=
\frac{[Q]}{[X]}.
$$

Por ejemplo, si

$$
F=kx,
$$

y queremos

$$
[F]=MLT^{-2},
$$

mientras

$$
[x]=L,
$$

entonces

$$
[k]
=
MT^{-2}.
$$

La letra $k$ no trae consigo una dimensión universal.

Su dimensión depende del papel que desempeña en la relación física.

### 6.14. Las constantes pueden reparar una ecuación solo si pertenecen al modelo

Supongamos que alguien propone

$$
x=t.
$$

Dimensionalmente,

$$
L\neq T.
$$

La ecuación falla.

Podríamos introducir una constante $c$ con dimensión

$$
[c]=LT^{-1}
$$

y escribir

$$
x=ct.
$$

Ahora:

$$
[ct]
=
LT^{-1}T
=
L.
$$

La nueva ecuación es homogénea.

Pero no hemos demostrado que exista físicamente una constante $c$ apropiada ni que la relación describa el sistema.

Solo hemos construido una forma dimensionalmente admisible.

Por tanto:

$$
\boxed{
\text{restaurar dimensiones}
\neq
\text{derivar una ley física}.
}
$$

### 6.15. Igualdades entre magnitudes y ecuaciones numéricas

Una ecuación física puede leerse en dos niveles.

#### Nivel de magnitudes

$$
Q_1+Q_2=Q_3.
$$

#### Nivel de valores numéricos en un sistema de unidades coherente

$$
q_1+q_2=q_3.
$$

La coherencia estudiada en §4 permite que ambas formas se parezcan.

Pero la Proposición 2 nos recuerda por qué esa semejanza no es accidental:

si los términos tuvieran dimensiones distintas, cambiarían con factores distintos al cambiar las unidades base y la forma numérica dejaría de ser estable.

La homogeneidad es, por tanto, una manifestación de la independencia física respecto de la convención de unidades.
