## §5 — Dimensión física {#fpm-i-02-s05}

### 5.1. La unidad concreta no es la dimensión

En §4 vimos que una misma magnitud derivada puede expresarse mediante unidades diferentes.

Una rapidez puede escribirse como

$$
72\,\mathrm{km\,h^{-1}},
$$

o como

$$
20\,\mathrm{m\,s^{-1}}.
$$

Los números son distintos y las unidades son distintas, pero la estructura física que relaciona longitud y tiempo es la misma.

Esto sugiere separar dos niveles:

$$
\boxed{
\text{unidad}
\neq
\text{dimensión}
}
$$

La unidad especifica una referencia concreta de medida.

La dimensión registra cómo una magnitud depende, dentro de un sistema de magnitudes, de las magnitudes tomadas como base.

Así,

$$
\mathrm{m\,s^{-1}}
$$

y

$$
\mathrm{km\,h^{-1}}
$$

son unidades diferentes, pero ambas representan magnitudes con la misma estructura dimensional:

$$
LT^{-1}.
$$

Esta separación será la base del análisis dimensional.

### 5.2. Dimensión de una magnitud

El Vocabulario Internacional de Metrología define la dimensión de una magnitud como la expresión de su dependencia respecto de las magnitudes base de un sistema mediante un producto de potencias, omitiendo cualquier factor numérico.[^s5-vim-dimension]

::: {.ma-block .ma-definicion #fpm-i-02-d14}
**Definición 14 — Dimensión de una magnitud**
La **dimensión** de una magnitud $Q$, respecto de un sistema elegido de magnitudes base, es la expresión simbólica que registra su dependencia respecto de esas magnitudes base como producto de potencias, sin incluir factores numéricos.
:::

Usaremos la notación

$$
[Q]
$$

para la dimensión de $Q$.

La documentación metrológica suele escribir también

$$
\dim Q.
$$

Ambas notaciones expresan la misma idea; en este libro utilizaremos preferentemente corchetes porque resultan compactos en los cálculos.

### 5.3. Las siete dimensiones base del SI

El SI organiza las magnitudes físicas mediante siete magnitudes base. A cada una se asocia convencionalmente un símbolo dimensional.[^s5-bipm-dimensions]

| Magnitud base | Símbolo dimensional |
|---|---:|
| tiempo | $T$ |
| longitud | $L$ |
| masa | $M$ |
| corriente eléctrica | $I$ |
| temperatura termodinámica | $\Theta$ |
| cantidad de sustancia | $N$ |
| intensidad luminosa | $J$ |

Debemos leer estos símbolos con cuidado.

Por ejemplo:

- $T$ como dimensión significa **tiempo**;
- $\Theta$ significa **temperatura termodinámica**;
- $J$ como dimensión significa **intensidad luminosa** y no debe confundirse con el símbolo $\mathrm J$ del joule.

Los símbolos dimensionales no son unidades.

Por tanto,

$$
L
\neq
\mathrm m,
$$

$$
T
\neq
\mathrm s,
$$

$$
M
\neq
\mathrm{kg}.
$$

El lado izquierdo representa una dimensión; el lado derecho, una unidad concreta.

::: {.ma-block .ma-metodo #fpm-i-02-mp09}
**Principio 9 — La dimensión es independiente de la unidad particular**
Cambiar la unidad utilizada para expresar una magnitud puede cambiar su valor numérico y el símbolo de unidad, pero no cambia su dimensión dentro del sistema de magnitudes fijado.
:::

### 5.4. El producto dimensional general

En el sistema dimensional utilizado por el SI, una magnitud $Q$ puede representarse dimensionalmente mediante

$$
\boxed{
[Q]
=
T^\alpha
L^\beta
M^\gamma
I^\delta
\Theta^\varepsilon
N^\zeta
J^\eta
}
$$

donde los exponentes

$$
\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta
$$

son los **exponentes dimensionales** de $Q$ respecto de la base elegida.

::: {.ma-block .ma-definicion #fpm-i-02-d15}
**Definición 15 — Exponente dimensional**
Un **exponente dimensional** es el exponente con el que aparece una dimensión base en la expresión dimensional de una magnitud.
:::

Por ejemplo, para una velocidad,

$$
[v]=LT^{-1}.
$$

Podemos escribirla en la forma completa:

$$
[v]
=
T^{-1}
L^1
M^0
I^0
\Theta^0
N^0
J^0.
$$

Por tanto, sus exponentes dimensionales son

$$
(-1,1,0,0,0,0,0)
$$

si usamos el orden

$$
(T,L,M,I,\Theta,N,J).
$$

Esta representación como lista de exponentes será útil más adelante en el teorema $\Pi$ de Buckingham.

### 5.5. Producto, cociente y potencia de dimensiones

Las operaciones dimensionales siguen la estructura algebraica de las magnitudes.

Si

$$
Q=Q_1Q_2,
$$

entonces

$$
[Q]=[Q_1][Q_2].
$$

Si

$$
Q=\frac{Q_1}{Q_2},
$$

entonces

$$
[Q]
=
\frac{[Q_1]}{[Q_2]}.
$$

Y si

$$
Q=Q_1^n,
$$

entonces

$$
[Q]=[Q_1]^n.
$$

No estamos manipulando unidades concretas.

Estamos manipulando la dependencia estructural respecto de las magnitudes base.

### 5.6. Área y volumen

Si

$$
A=xy,
$$

con

$$
[x]=L
$$

y

$$
[y]=L,
$$

entonces

$$
[A]
=
[x][y]
=
L^2.
$$

Por tanto,

$$
\boxed{
[A]=L^2.
}
$$

Análogamente, si

$$
V=xyz,
$$

entonces

$$
[V]
=
L^3.
$$

Por eso metro cuadrado, centímetro cuadrado y kilómetro cuadrado son unidades distintas de magnitudes cuya dimensión es

$$
L^2.
$$

### 5.7. Rapidez y velocidad

Para una relación elemental

$$
v=\frac{\ell}{t},
$$

tenemos

$$
[\ell]=L
$$

y

$$
[t]=T.
$$

Entonces

$$
[v]
=
\frac{L}{T}
=
LT^{-1}.
$$

Así,

$$
\boxed{
[v]=LT^{-1}.
}
$$

Esta expresión no contiene metro, kilómetro, segundo ni hora.

Por eso vale igualmente si la velocidad se expresa en

$$
\mathrm{m\,s^{-1}},
$$

$$
\mathrm{km\,h^{-1}},
$$

o cualquier otra unidad compatible.

### 5.8. Aceleración

Si una aceleración se modela como cambio de velocidad por intervalo de tiempo,

$$
a=\frac{\Delta v}{\Delta t},
$$

entonces

$$
[a]
=
\frac{[v]}{[t]}.
$$

Como

$$
[v]=LT^{-1}
$$

y

$$
[t]=T,
$$

obtenemos

$$
[a]
=
LT^{-2}.
$$

Por tanto,

$$
\boxed{
[a]=LT^{-2}.
}
$$

### 5.9. Densidad de masa

Para

$$
\rho=\frac{m}{V},
$$

tenemos

$$
[m]=M
$$

y

$$
[V]=L^3.
$$

Luego

$$
[\rho]
=
\frac{M}{L^3}
=
ML^{-3}.
$$

Así,

$$
\boxed{
[\rho]=ML^{-3}.
}
$$

Las unidades

$$
\mathrm{kg\,m^{-3}}
$$

y

$$
\mathrm{g\,cm^{-3}}
$$

son diferentes, pero comparten esta misma dimensión.

### 5.10. Algunas dimensiones frecuentes

A partir de las relaciones físicas que las definen dentro del modelo correspondiente podemos obtener:

| Magnitud | Relación elemental | Dimensión |
|---|---|---:|
| área | $A=xy$ | $L^2$ |
| volumen | $V=xyz$ | $L^3$ |
| velocidad | $v=\ell/t$ | $LT^{-1}$ |
| aceleración | $a=v/t$ | $LT^{-2}$ |
| densidad de masa | $\rho=m/V$ | $ML^{-3}$ |
| frecuencia | $f=1/t$ | $T^{-1}$ |
| fuerza | $F=ma$ | $MLT^{-2}$ |
| energía mecánica típica | $E=F\ell$ | $ML^2T^{-2}$ |
| potencia | $P=E/t$ | $ML^2T^{-3}$ |
| presión | $p=F/A$ | $ML^{-1}T^{-2}$ |
| carga eléctrica | $q=It$ | $IT$ |

Esta tabla no debe memorizarse como una lista arbitraria.

Cada entrada se reconstruye a partir de una relación entre magnitudes.

### 5.11. La dimensión no es una unidad abreviada

Es tentador pensar:

> «$LT^{-1}$ es una manera abstracta de escribir $\mathrm{m\,s^{-1}}$.»

La frase es incompleta.

La dimensión

$$
LT^{-1}
$$

no selecciona una unidad concreta.

Muchas unidades pueden corresponder a esa dimensión:

$$
\mathrm{m\,s^{-1}},
$$

$$
\mathrm{km\,h^{-1}},
$$

$$
\mathrm{cm\,s^{-1}},
$$

etc.

La relación correcta es:

$$
\boxed{
\text{una dimensión}
\longrightarrow
\text{muchas unidades posibles}
}
$$

mientras que un sistema coherente selecciona una forma privilegiada de construir unidades a partir de su base.

### 5.12. Cambiar unidades no cambia exponentes dimensionales

Consideremos una velocidad.

En SI:

$$
v=q\,\mathrm{m\,s^{-1}}.
$$

Podemos cambiar las unidades base de longitud y tiempo:

$$
\mathrm{m}
\longrightarrow
\mathrm{cm},
$$

$$
\mathrm{s}
\longrightarrow
\mathrm{min}.
$$

El valor numérico de $v$ cambia.

La unidad cambia.

Pero la relación estructural sigue siendo:

$$
\text{longitud}/\text{tiempo}.
$$

Por tanto,

$$
[v]=LT^{-1}
$$

antes y después del cambio.

Lo mismo ocurre para cualquier magnitud cuya dimensión sea

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

Un cambio de las unidades concretas asociadas a las magnitudes base altera factores numéricos, pero no los exponentes

$$
\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta.
$$

Ésta es la razón algebraica de el Principio 9.

### 5.13. Una demostración elemental de la invariancia

Supongamos, para simplificar, que una magnitud depende solo de longitud y tiempo y tiene la forma

$$
Q=C\,\ell^\beta t^\alpha,
$$

donde $C$ es un factor numérico que no introduce dimensión adicional.

Sean las unidades originales

$$
u_L,
\qquad
u_T,
$$

y nuevas unidades

$$
u_L'=\lambda_Lu_L,
$$

$$
u_T'=\lambda_Tu_T,
$$

con

$$
\lambda_L>0,
\qquad
\lambda_T>0.
$$

Por la Proposición 1, los valores numéricos de longitud y tiempo cambian inversamente:

$$
\{\ell\}_{u_L'}
=
\frac{\{\ell\}_{u_L}}{\lambda_L},
$$

$$
\{t\}_{u_T'}
=
\frac{\{t\}_{u_T}}{\lambda_T}.
$$

Entonces el valor numérico de $Q$ adquiere factores

$$
\lambda_L^{-\beta}
\lambda_T^{-\alpha}.
$$

Cambian los números.

Pero la forma de dependencia continúa siendo

$$
L^\beta T^\alpha.
$$

Por tanto, los exponentes dimensionales no dependen del tamaño concreto de las unidades elegidas.

No elevaremos este resultado a una nueva proposición numerada porque su función aquí es preparar la Proposición 2, que en §6 formalizará una consecuencia más fuerte: la homogeneidad dimensional necesaria de las ecuaciones físicas.

### 5.14. Misma dimensión no significa mismo tipo de magnitud

En §2 aprendimos que la comparabilidad física es más exigente que compartir una notación de unidad.

Ahora podemos formular la versión dimensional de esa cautela.

El VIM establece:

- magnitudes del mismo tipo tienen la misma dimensión;
- magnitudes con dimensiones diferentes son necesariamente de tipos distintos;
- magnitudes con la misma dimensión no son necesariamente del mismo tipo.[^s5-vim-dimension]

Por tanto,

$$
\boxed{
\text{mismo tipo}
\Longrightarrow
\text{misma dimensión}
}
$$

pero no:

$$
\boxed{
\text{misma dimensión}
\Longrightarrow
\text{mismo tipo}.
}
$$

::: {.ma-block .ma-metodo #fpm-i-02-mp10}
**Principio 10 — La igualdad dimensional no identifica el significado físico**
Que dos magnitudes posean la misma dimensión es una condición estructural importante, pero no basta para concluir que pertenecen al mismo tipo de magnitud ni que son físicamente intercambiables.
:::

### 5.15. Ejemplo: frecuencia y actividad radionúclida

En ambos casos aparece

$$
T^{-1}.
$$

Para frecuencia,

$$
[f]=T^{-1}.
$$

Para actividad radionúclida,

$$
[A]=T^{-1}.
$$

Sin embargo, el SI utiliza nombres especiales distintos:

$$
1\,\mathrm{Hz}=1\,\mathrm{s^{-1}},
$$

$$
1\,\mathrm{Bq}=1\,\mathrm{s^{-1}}.
$$

La igualdad dimensional no borra la diferencia física entre frecuencia y número de desintegraciones por unidad de tiempo.

### 5.16. Ejemplo: presión y densidad de energía

Para presión,

$$
p=\frac{F}{A}.
$$

Como

$$
[F]=MLT^{-2}
$$

y

$$
[A]=L^2,
$$

tenemos

$$
[p]
=
ML^{-1}T^{-2}.
$$

Ahora consideremos una densidad de energía

$$
u=\frac{E}{V}.
$$

Como

$$
[E]=ML^2T^{-2}
$$

y

$$
[V]=L^3,
$$

obtenemos

$$
[u]
=
ML^{-1}T^{-2}.
$$

Por tanto,

$$
[p]=[u].
$$

Pero esto no demuestra que presión y densidad de energía sean la misma magnitud.

Solo demuestra que ocupan la misma posición en el sistema dimensional.

### 5.17. Dimensión y forma vectorial

El VIM señala además que, al obtener la dimensión de una magnitud, no se toma en cuenta su carácter escalar, vectorial o tensorial.[^s5-vim-dimension]

Esto será importante más adelante.

Dos objetos matemáticos con naturaleza geométrica distinta pueden compartir dimensión.

Por ejemplo, una posición y un desplazamiento vectorial pueden poseer dimensión

$$
L,
$$

aunque su estructura matemática no sea la de un escalar arbitrario.

Por tanto:

$$
\boxed{
\text{dimensión}
\neq
\text{estructura matemática completa de la magnitud}.
}
$$

El análisis dimensional conserva cierta información y descarta otra.

### 5.18. La dimensión depende del sistema de magnitudes

También debemos evitar presentar la dimensión como una etiqueta metafísica adherida a cada magnitud de manera independiente de toda elección.

El BIPM y el VIM hablan de dimensiones **respecto de un sistema de magnitudes**.

La elección de magnitudes base es convencional.

Una vez fijada la base, la expresión dimensional de las magnitudes derivadas queda determinada por las relaciones adoptadas en ese sistema.

Así:

$$
\boxed{
\text{dimensión}
=
\text{estructura relativa a un sistema de magnitudes}
}
$$

aunque, una vez fijado el sistema, resulte extremadamente estable y útil.

::: {.ma-block .ma-definicion #fpm-i-02-d16}
**Definición 16 — Sistema de dimensiones**
Un **sistema de dimensiones** es la organización de las magnitudes de un sistema mediante dimensiones base elegidas y expresiones dimensionales derivadas construidas como productos de potencias de esas dimensiones base.
:::

En el SI trabajaremos con la base

$$
(T,L,M,I,\Theta,N,J).
$$

### 5.19. Zorich y el cambio de base de unidades

Zorich organiza su teoría dimensional precisamente alrededor del cambio de tamaños de las unidades base y de la manera en que cambian los valores numéricos de las magnitudes mientras se conserva su estructura dimensional.[^s5-zorich-dimensions]

Esta perspectiva es especialmente adecuada para nuestro proyecto porque conecta directamente con la Proposición 1.

La secuencia conceptual es:

$$
\boxed{
\text{magnitud}
\longrightarrow
\text{elección de unidades}
\longrightarrow
\text{valores numéricos}
}
$$

y, al cambiar las unidades,

$$
\boxed{
\text{cambian los números}
\quad\text{pero no}\quad
\text{la dependencia dimensional}.
}
$$

En §6 usaremos exactamente esta invariancia para detectar qué sumas e igualdades pueden conservar significado físico bajo cambios de escala de las unidades base.
