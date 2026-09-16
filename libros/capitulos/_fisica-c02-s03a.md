## §3 — El Sistema Internacional contemporáneo {#fpm-i-02-s03}

### 3.1. Una unidad local no basta para una ciencia global

En §1 vimos que un valor de magnitud puede escribirse, en los casos ordinarios que nos interesan, como

$$
Q=\{Q\}_u\,u.
$$

En §2 añadimos que la unidad $u$ debe ser una referencia compatible con el tipo de magnitud de $Q$.

Todavía queda un problema.

Nada impide que dos comunidades elijan referencias diferentes para la misma clase de magnitud.

Una longitud puede expresarse en metros, millas, pulgadas o mediante cualquier otra referencia definida de manera suficientemente precisa. Matemáticamente podemos convertir entre esas elecciones si conocemos sus relaciones. Pero una ciencia experimental internacional necesita algo más que la posibilidad abstracta de convertir.

Necesita un sistema que permita que resultados obtenidos en laboratorios distintos sean comparables sin renegociar desde cero el significado de cada unidad.

Ésta es una de las funciones del **Sistema Internacional de Unidades**.

El SI no es simplemente una tabla de nombres.

Es una infraestructura convencional para expresar valores de magnitudes de forma coherente, reproducible y globalmente comparable.

### 3.2. Qué significa «SI» en 2026

La formulación contemporánea del SI debe leerse con cuidado.

Antes de la revisión adoptada por la 26.ª CGPM en 2018 y efectiva desde el 20 de mayo de 2019, era habitual presentar el sistema diciendo que estaba definido mediante siete unidades base y que las demás unidades se derivaban de ellas.

Esa descripción histórica ya no es la definición fundamental vigente.

La formulación actual procede en la dirección inversa:

$$
\boxed{
\text{siete valores exactos de constantes definitorias}
\longrightarrow
\text{definición del SI}
\longrightarrow
\text{unidades del SI}.
}
$$

La 9.ª edición de la *SI Brochure*, en su versión 4.01 de junio de 2026, mantiene esta arquitectura.[^s3-bipm-si-2026]

::: {.ma-block .ma-definicion #fpm-i-02-d07}
**Definición 7 — Sistema Internacional de Unidades**
El **Sistema Internacional de Unidades (SI)** es el sistema de unidades definido fijando exactamente los valores numéricos de siete constantes definitorias cuando se expresan en las unidades especificadas por el propio SI.
:::

Esta definición operativa conserva el rasgo que necesitaremos matemáticamente:

$$
\boxed{
\text{el sistema se fija mediante relaciones exactas entre valores de constantes y unidades}.
}
$$

No debemos leer esta frase como si las constantes fueran «elegidas arbitrariamente». Algunas son constantes fundamentales de la naturaleza y otra, como $K_{\mathrm{cd}}$, es de carácter técnico. Lo que fija convencionalmente el SI es **su valor numérico exacto en determinadas unidades**.

### 3.3. Las siete constantes definitorias

Las siete constantes son las siguientes.[^s3-bipm-defining]

| Constante definitoria | Símbolo | Valor numérico fijado exactamente | Unidad en la que se fija |
|---|---:|---:|---|
| frecuencia de la transición hiperfina del estado fundamental no perturbado del cesio-133 | $\Delta\nu_{\mathrm{Cs}}$ | $9\,192\,631\,770$ | $\mathrm{Hz}$ |
| velocidad de la luz en el vacío | $c$ | $299\,792\,458$ | $\mathrm{m\,s^{-1}}$ |
| constante de Planck | $h$ | $6.626\,070\,15\times10^{-34}$ | $\mathrm{J\,s}$ |
| carga elemental | $e$ | $1.602\,176\,634\times10^{-19}$ | $\mathrm C$ |
| constante de Boltzmann | $k$ | $1.380\,649\times10^{-23}$ | $\mathrm{J\,K^{-1}}$ |
| constante de Avogadro | $N_{\mathrm A}$ | $6.022\,140\,76\times10^{23}$ | $\mathrm{mol^{-1}}$ |
| eficacia luminosa de una radiación monocromática definida | $K_{\mathrm{cd}}$ | $683$ | $\mathrm{lm\,W^{-1}}$ |

En esta tabla aparecen nombres de unidades derivadas —$\mathrm{Hz}$, $\mathrm J$, $\mathrm C$, $\mathrm{lm}$ y $\mathrm W$— que estudiaremos sistemáticamente en §4.

Por ahora basta registrar las relaciones:

$$
\mathrm{Hz}=\mathrm{s^{-1}},
$$

$$
\mathrm J=\mathrm{kg\,m^2\,s^{-2}},
$$

$$
\mathrm C=\mathrm{A\,s},
$$

$$
\mathrm W=\mathrm{kg\,m^2\,s^{-3}}.
$$

La unidad lumen requerirá además la noción de estereorradián, que retomaremos al estudiar cantidades de dimensión uno.

### 3.4. «Exacto por definición» no significa «medido con incertidumbre cero»

Esta distinción es fundamental.

El valor numérico

$$
299\,792\,458
$$

asignado a $c$ cuando se expresa en $\mathrm{m\,s^{-1}}$ no es en el SI actual el resultado de una nueva medición cuyo último decimal podría modificarse mañana.

Es un valor fijado exactamente por definición.

Lo mismo ocurre con los otros seis valores de la tabla.

Por eso la *SI Brochure* declara que los valores numéricos de las siete constantes definitorias no tienen incertidumbre.[^s3-bipm-defining]

Pero sería un error inferir:

> «Entonces toda realización experimental del metro, del segundo o del kilogramo carece de incertidumbre.»

La definición y la realización son niveles distintos.

Podemos tener:

$$
\boxed{
\text{definición exacta}
\quad+\quad
\text{realización experimental con incertidumbre}.
}
$$

La incertidumbre pertenece al proceso mediante el cual materializamos, comparamos o medimos la unidad en condiciones reales.

Su tratamiento sistemático pertenece a el capítulo 3.

### 3.5. Constantes definitorias: no todas son del mismo carácter físico

Conviene evitar otra simplificación.

A veces se dice:

> «El SI está definido mediante siete constantes fundamentales de la naturaleza.»

La frase es demasiado fuerte.

La propia *SI Brochure* distingue la naturaleza de las constantes definitorias. Algunas, como $c$ y $h$, son propiamente constantes fundamentales; $K_{\mathrm{cd}}$ es una constante técnica asociada a una convención fotométrica.[^s3-bipm-si-2026]

Por tanto, usaremos la expresión exacta:

$$
\boxed{
\text{siete constantes definitorias}
}
$$

y no:

$$
\boxed{
\text{siete constantes fundamentales}
}
$$

como si ambas clases coincidieran.

::: {.ma-block .ma-definicion #fpm-i-02-d08}
**Definición 8 — Constante definitoria del SI**
Una **constante definitoria del SI** es una de las siete constantes cuyo valor numérico se fija exactamente en la definición del SI cuando se expresa en la unidad correspondiente.
:::

La palabra **definitoria** describe el papel que la constante cumple en el sistema de unidades.

### 3.6. Las siete magnitudes base y las siete unidades base

Aunque el SI ya no se define fundamentalmente «a partir de las unidades base», las siete magnitudes base y sus unidades siguen cumpliendo un papel estructural central.[^s3-bipm-base]

| Magnitud base | Símbolo típico | Unidad base | Símbolo |
|---|---:|---|---:|
| tiempo | $t$ | segundo | $\mathrm s$ |
| longitud | $l$, $x$, $r$, etc. | metro | $\mathrm m$ |
| masa | $m$ | kilogramo | $\mathrm{kg}$ |
| corriente eléctrica | $I$, $i$ | amperio | $\mathrm A$ |
| temperatura termodinámica | $T$ | kelvin | $\mathrm K$ |
| cantidad de sustancia | $n$ | mol | $\mathrm{mol}$ |
| intensidad luminosa | $I_{\mathrm v}$ | candela | $\mathrm{cd}$ |

::: {.ma-block .ma-definicion #fpm-i-02-d09}
**Definición 9 — Magnitud base del SI**
Una **magnitud base del SI** es una de las siete magnitudes elegidas convencionalmente como base para organizar el sistema de dimensiones y unidades del SI: tiempo, longitud, masa, corriente eléctrica, temperatura termodinámica, cantidad de sustancia e intensidad luminosa.
:::

::: {.ma-block .ma-definicion #fpm-i-02-d10}
**Definición 10 — Unidad base del SI**
Una **unidad base del SI** es la unidad SI asociada a una de las siete magnitudes base: segundo, metro, kilogramo, amperio, kelvin, mol o candela.
:::

La palabra **base** indica un papel dentro de la arquitectura del sistema.

No significa que una magnitud base sea «más real» o «más importante» que una magnitud derivada.

### 3.7. Las unidades base no son siete patrones materiales

La palabra «unidad» puede evocar una colección de objetos guardados en un laboratorio:

- una barra patrón;
- una masa patrón;
- un reloj patrón;
- y así sucesivamente.

Ésa no es la estructura conceptual del SI actual.

El kilogramo, por ejemplo, ya no se define como la masa del Prototipo Internacional del Kilogramo.

La unidad se define mediante las constantes del SI; después debe **realizarse** experimentalmente mediante métodos compatibles con esa definición.

Esto permite que los métodos de realización mejoren sin obligarnos a cambiar cada vez la definición de la unidad.

La separación es:

$$
\boxed{
\text{definición}
\neq
\text{artefacto particular}
\neq
\text{procedimiento concreto de realización}.
}
$$

### 3.8. No existe una correspondencia simple «una constante = una unidad base»

La presencia de siete constantes y siete unidades base invita a imaginar siete parejas independientes:

$$
c\leftrightarrow \mathrm m,
\qquad
h\leftrightarrow\mathrm{kg},
\qquad\ldots
$$

Esta representación puede servir como recordatorio pedagógico muy aproximado, pero no describe fielmente la estructura lógica.

La propia documentación del BIPM advierte que no existe una correspondencia uno a uno entre las siete constantes definitorias y las siete unidades base: la definición de varias unidades base utiliza más de una constante.[^s3-bipm-si-2026]

Por ejemplo, el kilogramo se expresa mediante la constante de Planck, pero la unidad

$$
\mathrm{J\,s}
$$

que aparece en el valor de $h$ contiene a su vez metro y segundo.

Por tanto, el SI debe entenderse como una **red coherente de relaciones definitorias**, no como siete definiciones aisladas.

### 3.9. Definición y realización

El BIPM utiliza la expresión francesa *mise en pratique* para los documentos que describen maneras de realizar prácticamente las definiciones de las unidades.

Esto nos da una distinción permanente:

::: {.ma-block .ma-metodo #fpm-i-02-mp05}
**Principio 5 — No confundir definición y realización**
La definición de una unidad fija su significado dentro del SI; una realización es un procedimiento físico para materializar o acceder experimentalmente a esa definición. Una definición puede ser exacta aunque toda realización concreta posea incertidumbre.
:::

Esta diferencia será decisiva cuando estudiemos medición.

En términos del capítulo anterior:

$$
\text{definición de unidad}
$$

pertenece a la infraestructura convencional del modelo de medida, mientras que

$$
\text{realización}
$$

introduce sistemas físicos, instrumentos, procedimientos y condiciones experimentales.

### 3.10. «Base» tampoco significa «fundamental en la ontología de la física»

La elección de las siete magnitudes base posee una función organizativa e histórica.

No debemos inferir de ella una jerarquía ontológica.

Por ejemplo, energía no es una magnitud base del SI.

Eso no significa que la energía sea físicamente secundaria o poco importante.

La unidad de energía, el joule, puede expresarse mediante unidades base:

$$
1\,\mathrm J
=
1\,\mathrm{kg\,m^2\,s^{-2}}.
$$

La clasificación «base/derivada» responde a cómo organizamos el sistema de unidades.

::: {.ma-block .ma-metodo #fpm-i-02-mp06}
**Principio 6 — «Base» es una función del sistema de unidades**
Que una magnitud o unidad sea base en el SI no implica que sea físicamente más fundamental que una magnitud o unidad derivada. La distinción organiza la representación metrológica.
:::

Esta regla evitará confundir:

$$
\text{fundamentalidad física}
$$

con

$$
\text{estatus metrológico de base}.
$$

### 3.11. Prefijos SI

El SI permite construir múltiplos y submúltiplos decimales mediante prefijos.

La lista vigente llega desde

$$
10^{-30}
$$

hasta

$$
10^{30}.
$$

Los cuatro prefijos más recientes fueron adoptados por la 27.ª CGPM en 2022: **ronna**, **quetta**, **ronto** y **quecto**.[^s3-bipm-prefixes]

| Factor | Prefijo | Símbolo | Factor | Prefijo | Símbolo |
|---:|---|---:|---:|---|---:|
| $10^{30}$ | quetta | $\mathrm Q$ | $10^{-30}$ | quecto | $\mathrm q$ |
| $10^{27}$ | ronna | $\mathrm R$ | $10^{-27}$ | ronto | $\mathrm r$ |
| $10^{24}$ | yotta | $\mathrm Y$ | $10^{-24}$ | yocto | $\mathrm y$ |
| $10^{21}$ | zetta | $\mathrm Z$ | $10^{-21}$ | zepto | $\mathrm z$ |
| $10^{18}$ | exa | $\mathrm E$ | $10^{-18}$ | atto | $\mathrm a$ |
| $10^{15}$ | peta | $\mathrm P$ | $10^{-15}$ | femto | $\mathrm f$ |
| $10^{12}$ | tera | $\mathrm T$ | $10^{-12}$ | pico | $\mathrm p$ |
| $10^{9}$ | giga | $\mathrm G$ | $10^{-9}$ | nano | $\mathrm n$ |
| $10^{6}$ | mega | $\mathrm M$ | $10^{-6}$ | micro | $\mathrm{\mu}$ |
| $10^{3}$ | kilo | $\mathrm k$ | $10^{-3}$ | mili | $\mathrm m$ |
| $10^{2}$ | hecto | $\mathrm h$ | $10^{-2}$ | centi | $\mathrm c$ |
| $10^{1}$ | deca | $\mathrm{da}$ | $10^{-1}$ | deci | $\mathrm d$ |

La tabla debe leerse algebraicamente.

Por ejemplo:

$$
1\,\mathrm{km}=10^3\,\mathrm m,
$$

$$
1\,\mathrm{\mu s}=10^{-6}\,\mathrm s,
$$

$$
1\,\mathrm{nm}=10^{-9}\,\mathrm m.
$$

### 3.12. El prefijo forma parte de la unidad

Cuando escribimos

$$
1\,\mathrm{cm},
$$

la unidad completa es el **centímetro**.

Su relación con el metro es:

$$
1\,\mathrm{cm}
=
10^{-2}\,\mathrm m.
$$

Esto tiene una consecuencia importante cuando elevamos unidades a potencias.

Para área:

$$
1\,\mathrm{cm^2}
=
(1\,\mathrm{cm})^2
=
(10^{-2}\,\mathrm m)^2
=
10^{-4}\,\mathrm{m^2}.
$$

No:

$$
1\,\mathrm{cm^2}
=
10^{-2}\,\mathrm{m^2}.
$$

Para volumen:

$$
1\,\mathrm{mm^3}
=
(10^{-3}\,\mathrm m)^3
=
10^{-9}\,\mathrm{m^3}.
$$

El exponente afecta a toda la unidad prefijada.

### 3.13. No se encadenan prefijos

Los prefijos SI no se apilan.

Por ejemplo, no escribimos una supuesta unidad «milimicrómetro» mediante una cadena de prefijos.

Se elige un único prefijo cuyo factor total represente la escala deseada.

Así:

$$
10^{-9}\,\mathrm m
=
1\,\mathrm{nm},
$$

no una composición de «mili» y «micro».

Esto mantiene unívoca la lectura de los símbolos.
