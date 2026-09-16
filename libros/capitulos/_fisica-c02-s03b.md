### 3.14. La excepción histórica del kilogramo

El kilogramo tiene una peculiaridad nominal:

$$
\boxed{\mathrm{kg}}
$$

es la única unidad base del SI cuyo nombre ya contiene un prefijo.

Por esa razón, los múltiplos y submúltiplos de masa se forman aplicando prefijos a **gramo**, no añadiendo un segundo prefijo a kilogramo.

Por ejemplo:

$$
1\,\mathrm{mg}
=
10^{-3}\,\mathrm g
=
10^{-6}\,\mathrm{kg}.
$$

Y:

$$
1\,\mathrm{\mu g}
=
10^{-6}\,\mathrm g
=
10^{-9}\,\mathrm{kg}.
$$

No escribimos:

$$
\mathrm{mkg}
$$

para representar miligramos.

Esta regla es histórica y notacional, no una dificultad matemática.

### 3.15. Las mayúsculas importan

Los símbolos SI son sensibles a mayúsculas y minúsculas.

Por ejemplo:

$$
\mathrm m
$$

es metro, mientras que

$$
\mathrm M
$$

es el prefijo mega cuando antecede a un símbolo de unidad.

Del mismo modo:

$$
\mathrm k
$$

es kilo, mientras que

$$
\mathrm K
$$

es kelvin.

Por eso:

$$
1\,\mathrm{km}
$$

y

$$
1\,\mathrm{Km}
$$

no son escrituras equivalentes del SI.

La segunda combina una grafía de prefijo incorrecta con el símbolo del metro.

### 3.16. Reglas elementales de escritura

Usaremos desde ahora las siguientes convenciones.

#### Regla 1 — Espacio entre número y símbolo de unidad

Escribiremos:

$$
25\,\mathrm m,
$$

$$
3.2\,\mathrm s,
$$

$$
300\,\mathrm K.
$$

En texto Markdown/LaTeX representaremos el espacio tipográfico dentro de la fórmula mediante `\,` cuando sea útil.

#### Regla 2 — Los símbolos de unidad no se pluralizan

Escribimos:

$$
5\,\mathrm{kg},
$$

no:

$$
5\,\mathrm{kgs}.
$$

#### Regla 3 — El símbolo no lleva punto por ser abreviatura

Escribimos:

$$
10\,\mathrm m
$$

y no añadimos un punto a $\mathrm m$ salvo que el signo de puntuación corresponda al final de la oración.

#### Regla 4 — Los prefijos se unen al símbolo de unidad

Escribimos:

$$
\mathrm{mm},
\qquad
\mathrm{MHz},
\qquad
\mathrm{\mu s}.
$$

El prefijo no se separa mediante un espacio del símbolo de la unidad.

#### Regla 5 — Una potencia actúa sobre toda la unidad

Ya vimos:

$$
\mathrm{cm^2}
=
(10^{-2}\,\mathrm m)^2.
$$

Esta regla será esencial en conversiones de área y volumen.

### 3.17. Unidades, símbolos y nombres no son intercambiables sin reglas

Consideremos:

$$
5\,\mathrm m.
$$

Aquí:

- $5$ es valor numérico;
- $\mathrm m$ es símbolo de la unidad metro;
- «metro» es el nombre de esa unidad;
- el producto representa un valor de longitud.

El símbolo $\mathrm m$ no es una variable algebraica ordinaria cuyo significado pueda redefinirse libremente dentro de un cálculo.

En este capítulo lo manipularemos formalmente de acuerdo con las relaciones del sistema de unidades.

Esto permitirá más adelante escribir, por ejemplo:

$$
\frac{\mathrm m}{\mathrm s}
$$

sin perder de vista que estamos calculando con representaciones de unidades físicas.

### 3.18. Ejemplo desarrollado — La misma velocidad en dos unidades

Supongamos una rapidez:

$$
v=25\,\mathrm{m\,s^{-1}}.
$$

Queremos expresarla en kilómetros por hora.

Usamos:

$$
1\,\mathrm{km}=1000\,\mathrm m
$$

y:

$$
1\,\mathrm h=3600\,\mathrm s.
$$

Entonces:

$$
25\,\frac{\mathrm m}{\mathrm s}
\left(
\frac{1\,\mathrm{km}}{1000\,\mathrm m}
\right)
\left(
\frac{3600\,\mathrm s}{1\,\mathrm h}
\right)
=
25\frac{3600}{1000}\,
\frac{\mathrm{km}}{\mathrm h}.
$$

Por tanto:

$$
v=90\,\mathrm{km\,h^{-1}}.
$$

La magnitud física no cambió.

Cambió su representación numérica respecto de otras unidades.

Recuperamos así el Principio 2:

$$
\boxed{
25\,\mathrm{m\,s^{-1}}
=
90\,\mathrm{km\,h^{-1}}.
}
$$

### 3.19. Ejemplo desarrollado — Por qué $1\,\mathrm{cm^2}$ no es $10^{-2}\,\mathrm{m^2}$

Tomemos un cuadrado de lado:

$$
1\,\mathrm{cm}.
$$

Como:

$$
1\,\mathrm{cm}=10^{-2}\,\mathrm m,
$$

su área es:

$$
A
=
(10^{-2}\,\mathrm m)(10^{-2}\,\mathrm m).
$$

Por tanto:

$$
A
=
10^{-4}\,\mathrm{m^2}.
$$

El error

$$
1\,\mathrm{cm^2}=10^{-2}\,\mathrm{m^2}
$$

aparece cuando se aplica el factor del prefijo una sola vez en lugar de elevarlo junto con la unidad.

Este tipo de error será muy importante cuando trabajemos con densidades, presiones y otras magnitudes derivadas.

### 3.20. Ejercicios de §3

::: {.ma-block .ma-enunciado}
**Ejercicio 6 — Leer correctamente el SI actual**

**Tipo:** conceptual · **Nivel:** central

Decide si cada afirmación es correcta o incorrecta. Cuando sea incorrecta, reescríbela.

1. «El SI actual se define fundamentalmente eligiendo siete objetos que materializan las siete unidades base.»
2. «Los valores numéricos de las siete constantes definitorias son exactos dentro del SI.»
3. «Si el valor definitorio de una constante es exacto, cualquier realización experimental de la unidad correspondiente tiene incertidumbre exactamente cero.»
4. «Las siete unidades base siguen desempeñando una función estructural en el SI actual.»
5. «Cada una de las siete constantes definitorias corresponde de manera aislada y uno a uno a exactamente una unidad base.»
6. «Que el joule sea una unidad derivada significa que la energía es físicamente menos fundamental que la longitud.»
7. «La constante $K_{\mathrm{cd}}$ es una constante definitoria del SI, aunque no tenga el mismo carácter físico que $c$ o $h$.»
:::

::: {.ma-block .ma-comprobacion}
**Solución**

**1. Incorrecta.**

El SI contemporáneo se define fijando exactamente los valores numéricos de siete constantes definitorias en unidades especificadas. Las unidades no se definen mediante siete objetos materiales.

**2. Correcta.**

En el SI esos valores no son resultados experimentales ajustables: forman parte de la definición.

**3. Incorrecta.**

Debemos distinguir:

$$
\text{definición exacta}
\neq
\text{realización experimental exacta}.
$$

Una realización concreta utiliza sistemas físicos e instrumentos y puede tener incertidumbre.

**4. Correcta.**

Segundo, metro, kilogramo, amperio, kelvin, mol y candela siguen siendo las siete unidades base y organizan la expresión de unidades derivadas y dimensiones.

**5. Incorrecta.**

No existe una correspondencia uno a uno simple. Varias definiciones de unidades base dependen de más de una constante definitoria.

**6. Incorrecta.**

«Base» y «derivada» son categorías de organización del sistema de unidades. No establecen por sí mismas una jerarquía ontológica de conceptos físicos.

**7. Correcta.**

$K_{\mathrm{cd}}$ pertenece al conjunto de siete constantes definitorias, pero la propia documentación del SI distingue constantes fundamentales y constantes de carácter técnico.

La conclusión conjunta es:

$$
\boxed{
\text{definición del SI}
\neq
\text{lista de siete artefactos}
}
$$

y:

$$
\boxed{
\text{unidad base}
\neq
\text{magnitud físicamente más fundamental}.
}
$$
:::

::: {.ma-block .ma-enunciado}
**Ejercicio 7 — Prefijos y potencias de diez**

**Tipo:** cálculo · **Nivel:** central

Convierte:

1. $3.6\,\mathrm{km}$ a metros.
2. $250\,\mathrm{\mu s}$ a segundos.
3. $7.2\,\mathrm{nm}$ a metros.
4. $4.5\,\mathrm{cm^2}$ a metros cuadrados.
5. $2.0\,\mathrm{mm^3}$ a metros cúbicos.
6. $5\,\mathrm{mg}$ a kilogramos.
7. $2.4\,\mathrm{Rm}$ a metros.
8. $6\,\mathrm{qs}$ a segundos.

Explica además por qué:

$$
1\,\mathrm{cm^2}\neq10^{-2}\,\mathrm{m^2}.
$$
:::

::: {.ma-block .ma-comprobacion}
**Solución**

**1. Kilómetros a metros**

$$
1\,\mathrm{km}=10^3\,\mathrm m.
$$

Entonces:

$$
3.6\,\mathrm{km}
=
3.6\times10^3\,\mathrm m.
$$

Por tanto:

$$
\boxed{
3.6\,\mathrm{km}=3600\,\mathrm m.
}
$$

**2. Microsegundos a segundos**

$$
1\,\mathrm{\mu s}=10^{-6}\,\mathrm s.
$$

Luego:

$$
250\,\mathrm{\mu s}
=
250\times10^{-6}\,\mathrm s
=
2.50\times10^{-4}\,\mathrm s.
$$

**3. Nanómetros a metros**

$$
1\,\mathrm{nm}=10^{-9}\,\mathrm m.
$$

Así:

$$
\boxed{
7.2\,\mathrm{nm}
=
7.2\times10^{-9}\,\mathrm m.
}
$$

**4. Centímetros cuadrados a metros cuadrados**

$$
1\,\mathrm{cm}
=
10^{-2}\,\mathrm m.
$$

Elevamos toda la unidad al cuadrado:

$$
1\,\mathrm{cm^2}
=
(10^{-2}\,\mathrm m)^2
=
10^{-4}\,\mathrm{m^2}.
$$

Entonces:

$$
\boxed{
4.5\,\mathrm{cm^2}
=
4.5\times10^{-4}\,\mathrm{m^2}.
}
$$

**5. Milímetros cúbicos a metros cúbicos**

$$
1\,\mathrm{mm}
=
10^{-3}\,\mathrm m.
$$

Por tanto:

$$
1\,\mathrm{mm^3}
=
(10^{-3}\,\mathrm m)^3
=
10^{-9}\,\mathrm{m^3}.
$$

Así:

$$
\boxed{
2.0\,\mathrm{mm^3}
=
2.0\times10^{-9}\,\mathrm{m^3}.
}
$$

**6. Miligramos a kilogramos**

$$
1\,\mathrm{mg}
=
10^{-3}\,\mathrm g.
$$

Además:

$$
1\,\mathrm g
=
10^{-3}\,\mathrm{kg}.
$$

Entonces:

$$
1\,\mathrm{mg}
=
10^{-6}\,\mathrm{kg}.
$$

Por tanto:

$$
\boxed{
5\,\mathrm{mg}
=
5\times10^{-6}\,\mathrm{kg}.
}
$$

**7. Ronnametros a metros**

El prefijo ronna, símbolo $\mathrm R$, representa:

$$
10^{27}.
$$

Entonces:

$$
\boxed{
2.4\,\mathrm{Rm}
=
2.4\times10^{27}\,\mathrm m.
}
$$

**8. Quectosegundos a segundos**

El prefijo quecto, símbolo $\mathrm q$, representa:

$$
10^{-30}.
$$

Luego:

$$
\boxed{
6\,\mathrm{qs}
=
6\times10^{-30}\,\mathrm s.
}
$$

Finalmente:

$$
1\,\mathrm{cm^2}
=
(10^{-2}\,\mathrm m)^2
=
10^{-4}\,\mathrm{m^2},
$$

porque el exponente $2$ actúa tanto sobre el metro como sobre el factor $10^{-2}$.

Por eso:

$$
\boxed{
1\,\mathrm{cm^2}\neq10^{-2}\,\mathrm{m^2}.
}
$$
:::

### 3.21. Síntesis

El SI contemporáneo se organiza mediante dos capas que no debemos confundir.

La capa definitoria:

$$
\boxed{
\Delta\nu_{\mathrm{Cs}},
c,
h,
e,
k,
N_{\mathrm A},
K_{\mathrm{cd}}
}
$$

con valores numéricos fijados exactamente.

Y la capa organizativa de las unidades base:

$$
\boxed{
\mathrm s,\,
\mathrm m,\,
\mathrm{kg},\,
\mathrm A,\,
\mathrm K,\,
\mathrm{mol},\,
\mathrm{cd}.
}
$$

Las dos están relacionadas, pero no mediante siete parejas aisladas.

Además:

$$
\boxed{
\text{definición}
\neq
\text{realización}
}
$$

y:

$$
\boxed{
\text{base}
\neq
\text{más fundamental físicamente}.
}
$$

Los prefijos SI permiten cambiar cómodamente de escala decimal, pero deben manipularse algebraicamente con cuidado:

$$
\boxed{
(pu)^n=p^n u^n.
}
$$

Por eso las conversiones de área y volumen exigen elevar también el factor del prefijo.

Con esta infraestructura ya podemos avanzar al siguiente nivel.

Hasta ahora hemos trabajado principalmente con unidades escogidas para clases de magnitudes ya conocidas.

En §4 construiremos nuevas magnitudes mediante productos y cocientes y veremos cómo aparecen sistemáticamente las **unidades derivadas coherentes**:

$$
\boxed{
\text{§4 — Magnitudes derivadas y unidades coherentes}.
}
$$

---

### Fuentes normativas de §3

[^s3-bipm-si-2026]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01, junio de 2026, §§2.2–2.3.2, pp. 123–132, DOI 10.59161/AUEZ1291.

[^s3-bipm-defining]: BIPM, *SI — Defining constants*; véase también *SI Brochure*, v4.01 (2026), §2.2, pp. 123–125.

[^s3-bipm-base]: BIPM, *SI — Base units*; véase también *SI Brochure*, v4.01 (2026), §2.3.1, pp. 126–131.

[^s3-bipm-prefixes]: BIPM, *SI — Prefixes*; 27.ª CGPM, Resolución 3 (2022), «On the extension of the range of SI prefixes».
