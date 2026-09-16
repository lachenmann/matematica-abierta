## §11 — Semejanza, escalamiento y cambio de escala {#fpm-i-02-s11}

### 11.1. Intuir: hacer un sistema más grande no significa multiplicarlo todo por el mismo número

Imaginemos dos modelos geométricamente semejantes de una misma figura.

Si todas las longitudes del segundo son

$$
\lambda
$$

veces las del primero, es natural escribir

$$
L'=\lambda L.
$$

Pero el área no cambia por el mismo factor:

$$
A'=\lambda^2A.
$$

Y el volumen cambia como

$$
V'=\lambda^3V.
$$

Por tanto,

$$
\boxed{
\text{cambiar de escala}
\neq
\text{multiplicar todas las magnitudes por el mismo factor}.
}
$$

Cada magnitud responde al reescalado según su estructura.

Ésta es la idea básica de una **ley de escalamiento**.

### 11.2. Representar: una familia de sistemas relacionados por un parámetro

Introduciremos un parámetro positivo

$$
\lambda>0.
$$

Una magnitud $X$ puede transformarse según

$$
X(\lambda)=\lambda^sX_0,
$$

donde $s$ describe cómo responde al cambio de escala.

Por ejemplo:

$$
L(\lambda)=\lambda L_0
$$

tiene exponente de escalamiento $1$;

$$
A(\lambda)=\lambda^2A_0
$$

tiene exponente $2$;

$$
V(\lambda)=\lambda^3V_0
$$

tiene exponente $3$.

::: {.ma-block .ma-definicion}
**Definición 27 — Ley de escalamiento**
Una **ley de escalamiento** para una magnitud $Q$ respecto de un parámetro positivo $\lambda$ es una relación que describe cómo cambia $Q$ al variar $\lambda$. Cuando tiene la forma

$$
Q(\lambda)=\lambda^sQ(1),
$$

llamaremos $s$ **exponente de escalamiento** de $Q$ respecto de esa transformación.
:::

### 11.3. Dimensión y escalamiento no son lo mismo

Debemos separar dos ideas.

La **dimensión** responde:

> ¿cómo depende una magnitud de las magnitudes base del sistema dimensional?

El **escalamiento** responde:

> ¿cómo cambia una magnitud dentro de una familia concreta de transformaciones?

Una longitud tiene dimensión

$$
L.
$$

Pero no toda longitud física debe escalar necesariamente como

$$
\lambda^1
$$

en cualquier problema.

Por ejemplo, en una transformación podríamos duplicar el radio de un objeto y mantener fija otra longitud externa.

Ambas tienen dimensión $L$, pero sus leyes de escalamiento son distintas.

Por tanto,

$$
\boxed{
\text{misma dimensión}
\not\Rightarrow
\text{mismo exponente de escalamiento}.
}
$$

::: {.ma-block .ma-metodo}
**Principio 21 — El escalamiento pertenece al modelo de transformación**
La dimensión de una magnitud es una propiedad relativa al sistema dimensional; su exponente de escalamiento depende además de qué familia de sistemas o transformación física estamos comparando.
:::

### 11.4. Escalamiento geométrico uniforme

Consideremos una familia de cuerpos geométricamente semejantes en la que toda longitud lineal se multiplica por

$$
\lambda.
$$

Entonces:

$$
L'=\lambda L.
$$

Un área construida como producto de dos longitudes satisface

$$
A'
=
(\lambda L_1)(\lambda L_2)
=
\lambda^2A.
$$

Un volumen construido como producto de tres longitudes satisface

$$
V'
=
\lambda^3V.
$$

Así obtenemos:

$$
\boxed{
L\sim\lambda,
\qquad
A\sim\lambda^2,
\qquad
V\sim\lambda^3.
}
$$

Aquí el símbolo

$$
\sim
$$

indica dependencia de escala, no igualdad exacta entre magnitudes.

### 11.5. Consecuencia: superficie frente a volumen

Para objetos geométricamente semejantes,

$$
\frac AV
\sim
\frac{\lambda^2}{\lambda^3}.
$$

Por tanto,

$$
\boxed{
\frac AV
\sim
\lambda^{-1}.
}
$$

Al aumentar el tamaño lineal de un objeto, disminuye su razón superficie/volumen.

Si duplicamos la escala lineal,

$$
\lambda=2,
$$

entonces

$$
\frac{(A/V)'}{A/V}
=
\frac12.
$$

Esta conclusión es geométrica.

No necesitamos todavía afirmar ninguna consecuencia biológica, térmica o mecánica concreta.

Esas aplicaciones requerirían modelos físicos adicionales.

### 11.6. Masa bajo densidad constante

Supongamos ahora que comparamos objetos semejantes fabricados con un material de densidad constante

$$
\rho.
$$

Como

$$
m=\rho V,
$$

si

$$
\rho'=\rho
$$

y

$$
V'=\lambda^3V,
$$

entonces

$$
m'
=
\rho V'
=
\lambda^3m.
$$

Por tanto,

$$
\boxed{
m\sim\lambda^3
}
$$

bajo las hipótesis:

- semejanza geométrica;
- misma densidad.

Si cambia el material o la densidad, esta ley deja de seguirse automáticamente.

### 11.7. Precisar: semejanza respecto de un modelo

Dos objetos pueden tener la misma forma geométrica y no comportarse físicamente de manera semejante.

Para hablar de semejanza física necesitamos declarar qué estructura queremos preservar.[^s11-zorich-similarity]

::: {.ma-block .ma-definicion}
**Definición 28 — Semejanza respecto de un modelo**
Dos realizaciones de un modelo son **semejantes respecto de un conjunto declarado de variables y relaciones** cuando pueden relacionarse mediante transformaciones de escala que preservan la forma de esas relaciones y los parámetros de dimensión uno relevantes para la comparación.
:::

Esta definición es deliberadamente relativa.

No existe una única noción universal de «ser semejante» para todos los propósitos físicos.

Podemos estudiar:

- semejanza geométrica;
- semejanza cinemática;
- semejanza dinámica;
- semejanza térmica;

según las variables y relaciones que el modelo conserve.

### 11.8. Un ejemplo temporal: péndulos semejantes

En §10 obtuvimos, para el modelo elemental,

$$
T_p
=
C\sqrt{\frac{\ell}{g}}.
$$

Supongamos ahora que mantenemos fijo $g$ y cambiamos

$$
\ell'=\lambda\ell.
$$

Entonces

$$
T_p'
=
C\sqrt{\frac{\lambda\ell}{g}}
=
\lambda^{1/2}T_p.
$$

Por tanto,

$$
\boxed{
T_p\sim\lambda^{1/2}.
}
$$

Un péndulo cuatro veces más largo tiene, dentro de este modelo,

$$
T_p'=2T_p.
$$

La longitud creció por un factor $4$.

El período solo creció por un factor $2$.

### 11.9. Otro ejemplo: escala orbital

En §10 obtuvimos

$$
T_o
=
C\sqrt{\frac{r^3}{GM}}.
$$

Si mantenemos fijos $G$ y $M$ y reescalamos

$$
r'=\lambda r,
$$

entonces

$$
T_o'
=
C\sqrt{\frac{\lambda^3r^3}{GM}}
=
\lambda^{3/2}T_o.
$$

Así,

$$
\boxed{
T_o\sim r^{3/2}
}
$$

cuando $M$ permanece fija dentro del modelo.

Ésta es una ley de escala más informativa que una simple afirmación dimensional.

Nos dice cómo comparar dos miembros de una familia física.

### 11.10. Teorema elemental de escalamiento monomial

::: {.ma-block .ma-enunciado}
**Proposición 4 — Escalamiento de un ansatz monomial**

Sea

$$
Q=C\prod_{i=1}^nX_i^{\alpha_i},
$$

donde $C$ permanece invariante bajo una transformación parametrizada por $\lambda>0$.

Supongamos que cada variable escala como

$$
X_i(\lambda)=\lambda^{s_i}X_i(1).
$$

Entonces

$$
\boxed{
Q(\lambda)
=
\lambda^{\sum_i\alpha_is_i}Q(1).
}
$$

Por tanto, el exponente de escalamiento de $Q$ es

$$
\boxed{
s_Q
=
\sum_i\alpha_is_i.
}
$$
:::

#### Demostración

Sustituimos las leyes de escala de las variables:

$$
Q(\lambda)
=
C\prod_i
\left(
\lambda^{s_i}X_i(1)
\right)^{\alpha_i}.
$$

Separando los factores de $\lambda$,

$$
Q(\lambda)
=
C
\left(
\prod_i
\lambda^{\alpha_is_i}
\right)
\left(
\prod_iX_i(1)^{\alpha_i}
\right).
$$

Como

$$
\prod_i
\lambda^{\alpha_is_i}
=
\lambda^{\sum_i\alpha_is_i},
$$

obtenemos

$$
Q(\lambda)
=
\lambda^{\sum_i\alpha_is_i}
C\prod_iX_i(1)^{\alpha_i}.
$$

Pero

$$
C\prod_iX_i(1)^{\alpha_i}
=
Q(1).
$$

Luego

$$
\boxed{
Q(\lambda)
=
\lambda^{\sum_i\alpha_is_i}Q(1).
}
$$

$$
\boxed{\text{QED}}
$$

### 11.11. Leer la Proposición 4 correctamente

La Proposición 4 no afirma que toda magnitud física siga una potencia de $\lambda$.

La conclusión depende de dos hipótesis:

1. que la relación tenga la forma monomial indicada;
2. que conozcamos cómo escala cada variable $X_i$.

Así, la Proposición 4 traduce una ley monomial en una ley de escala.

No crea por sí sola la relación física.

### 11.12. Cantidades de dimensión uno e invariantes de semejanza

Supongamos que bajo una transformación

$$
X'=\lambda^aX
$$

y

$$
Y'=\lambda^bY.
$$

La combinación

$$
\Pi
=
X^pY^q
$$

será invariante bajo el reescalado si

$$
ap+bq=0.
$$

Entonces

$$
\Pi'=\Pi.
$$

Esto es distinto de decir solamente que

$$
[\Pi]=1.
$$

Una cantidad puede tener dimensión uno y aun cambiar durante una transformación física concreta.

Para que funcione como **invariante de semejanza**, debe además conservar su valor bajo la familia de escalamiento elegida.

::: {.ma-block .ma-metodo}
**Principio 22 — Semejanza exige preservar los parámetros adimensionales relevantes**
En una comparación por semejanza, no basta con que una combinación tenga dimensión uno: los parámetros adimensionales que controlan el modelo deben conservar valores compatibles entre los sistemas comparados.
:::

Esta idea anticipa directamente los grupos $\Pi$ de §12.

### 11.13. Poner a prueba: dimensión uno no implica invariancia de escala

Sea

$$
R=\frac{x}{y},
$$

con

$$
[x]=[y]=L.
$$

Entonces

$$
[R]=1.
$$

Pero supongamos que

$$
x'=2x
$$

y

$$
y'=3y.
$$

Entonces

$$
R'
=
\frac{2x}{3y}
=
\frac23R.
$$

Por tanto,

$$
R'\neq R.
$$

La cantidad es de dimensión uno, pero no es invariante bajo ese reescalado.

En cambio, si

$$
x'=\lambda x
$$

y

$$
y'=\lambda y,
$$

entonces

$$
R'=R.
$$

La semejanza depende del patrón de transformación.

### 11.14. Diagnóstico: miniatura geométrica no equivale automáticamente a modelo físico

Supongamos que construimos una maqueta a escala

$$
1:10.
$$

Todas las longitudes se reducen por

$$
\lambda=\frac1{10}.
$$

Geométricamente,

$$
A'=10^{-2}A,
$$

y

$$
V'=10^{-3}V.
$$

Si conservamos densidad,

$$
m'=10^{-3}m.
$$

Pero de aquí no sigue que todos los tiempos, fuerzas o velocidades deban reducirse también por

$$
10^{-1}.
$$

Cada una requiere su propia ley de escala.

Una maqueta geométricamente semejante puede no ser dinámicamente semejante.

Esta distinción es central en modelos experimentales.

### 11.15. Ejemplo: velocidad bajo escalamiento de longitud y tiempo

La velocidad satisface

$$
v=\frac{L}{T}.
$$

Si una familia transforma

$$
L'=\lambda^aL
$$

y

$$
T'=\lambda^bT,
$$

entonces

$$
v'
=
\frac{\lambda^aL}{\lambda^bT}
=
\lambda^{a-b}v.
$$

Así,

$$
\boxed{
s_v=a-b.
}
$$

La dimensión de $v$ sigue siendo

$$
LT^{-1},
$$

pero su exponente de escalamiento depende de los valores concretos

$$
a,\ b.
$$

Éste es otro modo de ver por qué dimensión y escalamiento no son sinónimos.

### 11.16. Ejemplo: aceleración bajo un escalamiento general

Como

$$
a_{\mathrm f}
\sim
\frac{L}{T^2},
$$

si

$$
L'=\lambda^pL
$$

y

$$
T'=\lambda^qT,
$$

entonces

$$
a_{\mathrm f}'
=
\lambda^{p-2q}a_{\mathrm f}.
$$

Por tanto,

$$
\boxed{
s_{a_{\mathrm f}}=p-2q.
}
$$

Si queremos preservar una aceleración externa fija, debemos imponer

$$
p-2q=0.
$$

Entonces

$$
q=\frac p2.
$$

Para

$$
p=1,
$$

obtenemos

$$
T\sim\lambda^{1/2},
$$

exactamente como en el escalamiento temporal del péndulo bajo gravedad fija.

### 11.17. Autoexplicación

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Responde sin volver a los ejemplos:

1. ¿por qué dos magnitudes con la misma dimensión pueden tener exponentes de escalamiento diferentes?;
2. ¿qué hipótesis permiten deducir $m\sim\lambda^3$ para objetos semejantes?;
3. ¿por qué una cantidad de dimensión uno puede no ser invariante bajo un cambio de escala?;
4. ¿qué diferencia hay entre semejanza geométrica y semejanza física?
:::

### 11.18. Práctica guiada

::: {.ma-block .ma-enunciado}
**Ejercicio 23 — Escalar una familia de modelos**

**Objetivo:** `Síntesis`

**Intenta primero: 3–5 min antes de leer la solución.**

Considera una familia de cuerpos geométricamente semejantes construidos con el mismo material.

La escala lineal cambia según

$$
L'=\lambda L.
$$

### A. Recuperación

Determina cómo escalan:

1. área $A$;
2. volumen $V$;
3. masa $m$;
4. razón $A/V$.

### B. Consolidación

Si una cantidad característica satisface

$$
Q=Cm^\alpha L^\beta,
$$

demuestra usando la Proposición 4 que

$$
Q'
=
\lambda^{3\alpha+\beta}Q.
$$

### C. Diagnóstico

Un estudiante afirma:

> «Una maqueta diez veces más pequeña tiene todas sus magnitudes físicas diez veces más pequeñas.»

Identifica el error.

### D. Síntesis

Supón además que un proceso posee una escala temporal

$$
T=C\sqrt{\frac{L}{g}},
$$

con $g$ fijo.

Determina cómo cambia $T$ cuando

$$
\lambda=\frac1{100}.
$$

Explica por qué la respuesta no es

$$
T'=\frac1{100}T.
$$
:::

::: {.ma-block .ma-comprobacion}
**Solución**

### A. Recuperación

Por semejanza geométrica,

$$
A'=\lambda^2A,
$$

$$
V'=\lambda^3V.
$$

Con el mismo material,

$$
\rho'=\rho.
$$

Como

$$
m=\rho V,
$$

resulta

$$
m'=\lambda^3m.
$$

Finalmente,

$$
\frac{A'}{V'}
=
\frac{\lambda^2A}{\lambda^3V}
=
\lambda^{-1}\frac AV.
$$

Por tanto:

$$
\boxed{
A\sim\lambda^2,\quad
V\sim\lambda^3,\quad
m\sim\lambda^3,\quad
A/V\sim\lambda^{-1}.
}
$$

### B. Consolidación

Tenemos

$$
Q=Cm^\alpha L^\beta.
$$

Como

$$
m'=\lambda^3m
$$

y

$$
L'=\lambda L,
$$

entonces

$$
Q'
=
C(\lambda^3m)^\alpha(\lambda L)^\beta.
$$

Así,

$$
Q'
=
\lambda^{3\alpha+\beta}
Cm^\alpha L^\beta.
$$

Luego

$$
\boxed{
Q'
=
\lambda^{3\alpha+\beta}Q.
}
$$

### C. Diagnóstico

El estudiante confunde una escala **lineal** con una regla universal para todas las magnitudes.

Las áreas cambian como

$$
\lambda^2,
$$

los volúmenes y masas bajo densidad fija como

$$
\lambda^3,
$$

y otras magnitudes dependen de las relaciones físicas del modelo.

No existe una regla

$$
Q'=\lambda Q
$$

válida para toda magnitud.

### D. Síntesis

Si

$$
T=C\sqrt{\frac Lg}
$$

y $g$ permanece fijo, entonces

$$
T'=\lambda^{1/2}T.
$$

Con

$$
\lambda=\frac1{100},
$$

tenemos

$$
\lambda^{1/2}
=
\frac1{10}.
$$

Por tanto,

$$
\boxed{
T'=\frac1{10}T.
}
$$

El tiempo no disminuye cien veces porque su ley de escala no es lineal en $L$:

$$
T\propto L^{1/2}.
$$

La conclusión sintetiza la sección:

$$
\boxed{
\text{el escalamiento de una magnitud viene de la estructura del modelo,
no del tamaño lineal por sí solo}.
}
$$
:::

### 11.19. Variar: escalamiento simultáneo de varias magnitudes

Supongamos ahora que

$$
r'=\lambda r
$$

y

$$
M'=\lambda^\mu M
$$

en la relación orbital

$$
T_o
=
C\sqrt{\frac{r^3}{GM}}.
$$

Con $G$ fijo,

$$
T_o'
=
\sqrt{
\frac{\lambda^3r^3}
{G\lambda^\mu M}
}\,C.
$$

Por tanto,

$$
\boxed{
T_o'
=
\lambda^{(3-\mu)/2}T_o.
}
$$

Distintos valores de $\mu$ producen familias de semejanza distintas.

Por ejemplo:

- si $\mu=0$, $T_o\sim\lambda^{3/2}$;
- si $\mu=3$, $T_o$ permanece invariante;
- si $\mu=1$, $T_o\sim\lambda$.

Esto muestra que una ley dimensional puede contener muchas reglas de escalamiento según qué variables se transformen conjuntamente.

### 11.20. Conectar con el teorema $\Pi$

§10 mostró que una relación dimensional puede dejar funciones arbitrarias de cantidades de dimensión uno.

§11 añade una nueva lectura:

esas cantidades pueden actuar como **invariantes de semejanza** cuando sus valores permanecen fijos a través de una familia de sistemas.

La estructura que buscamos es:

$$
\boxed{
\text{variables dimensionales}
\longrightarrow
\text{combinaciones de dimensión uno}
\longrightarrow
\text{familias semejantes}.
}
$$

Buckingham $\Pi$ hará sistemática esta reducción.

En §12 preguntaremos:

> Dadas $n$ variables físicas construidas a partir de $r$ dimensiones independientes, ¿cuántas combinaciones de dimensión uno independientes podemos esperar?

### 11.21. Síntesis

El cambio de escala se describe mediante leyes como

$$
Q(\lambda)=\lambda^sQ(1).
$$

El exponente $s$ depende de:

- la relación física;
- las variables que cambian;
- las variables que permanecen fijas;
- el modelo de semejanza adoptado.

Para un ansatz monomial,

$$
Q=C\prod_iX_i^{\alpha_i},
$$

si

$$
X_i(\lambda)=\lambda^{s_i}X_i(1),
$$

La Proposición 4 demuestra:

$$
\boxed{
s_Q=\sum_i\alpha_is_i.
}
$$

Además,

$$
\boxed{
\text{dimensión uno}
\not\Rightarrow
\text{invariante de escala},
}
$$

y

$$
\boxed{
\text{semejanza geométrica}
\not\Rightarrow
\text{semejanza física completa}.
}
$$

La semejanza exige declarar qué relaciones e invariantes queremos preservar.

El siguiente paso es:

$$
\boxed{
\text{§12 — El teorema }\Pi\text{ de Buckingham}.
}
$$

---

### Notas y fuentes

[^s11-zorich-similarity]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §1.3.2, p. 10, y cap. 2, pp. 11–18.
