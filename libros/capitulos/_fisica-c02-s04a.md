## §4 — Magnitudes derivadas y unidades coherentes {#fpm-i-02-s04}

### 4.1. Las unidades también obedecen relaciones

En §1 distinguimos una magnitud de su valor numérico y de la unidad elegida para expresarla. En §2 vimos que la comparabilidad física precede a la comparación numérica. En §3 fijamos la arquitectura contemporánea del Sistema Internacional.

Ahora aparece una cuestión nueva: las magnitudes físicas no se presentan siempre de manera aislada. Un modelo puede relacionarlas mediante productos, cocientes y potencias. Por ejemplo,

$$
v=\frac{\ell}{t},
$$

$$
\rho=\frac{m}{V},
$$

o

$$
A=xy.
$$

Estas relaciones entre magnitudes inducen relaciones entre las unidades utilizadas para expresarlas.

La idea rectora será:

$$
\boxed{
\text{estructura algebraica entre magnitudes}
\longrightarrow
\text{estructura correspondiente entre unidades}
}
$$

Pero no toda combinación de unidades es **coherente** con el sistema elegido, y una misma expresión de unidad puede corresponder a tipos de magnitud físicamente distintos.

### 4.2. Magnitud derivada

::: {.ma-block .ma-definicion #fpm-i-02-d11}
**Definición 11 — Magnitud derivada**
Una **magnitud derivada** es una magnitud definida, dentro de un sistema de magnitudes, mediante una relación algebraica con otras magnitudes del sistema, en particular con las magnitudes tomadas como base.
:::

Ejemplos elementales son:

$$
A=xy,
$$

para un área rectangular;

$$
V=xyz,
$$

para un volumen;

$$
v=\frac{\ell}{t},
$$

para una rapidez o velocidad escalar en un modelo elemental;

y

$$
\rho=\frac{m}{V},
$$

para densidad de masa.

La palabra **derivada** no significa que la magnitud sea menos física, menos importante o menos observable. Describe su papel dentro de la arquitectura elegida.

Así,

$$
\boxed{
\text{base/derivada}
=
\text{papel dentro de un sistema de magnitudes}
}
$$

y no una jerarquía ontológica.

### 4.3. Producto, cociente y potencia

Sean

$$
Q_1=q_1u_1,
\qquad
Q_2=q_2u_2.
$$

Si

$$
Q=Q_1Q_2,
$$

entonces

$$
Q=(q_1q_2)(u_1u_2).
$$

La unidad producto natural es

$$
u=u_1u_2.
$$

Si

$$
Q=\frac{Q_1}{Q_2},
$$

entonces

$$
Q=
\frac{q_1}{q_2}
\frac{u_1}{u_2},
$$

de modo que aparece

$$
u=\frac{u_1}{u_2}.
$$

Y si

$$
Q=Q_1^n,
$$

para un exponente entero $n$, entonces

$$
Q=q_1^n u_1^n.
$$

Por tanto, producto, cociente y potencia de magnitudes inducen producto, cociente y potencia de unidades.

Todavía no estamos hablando formalmente de dimensiones. Eso corresponde a §5.

### 4.4. Unidad derivada

::: {.ma-block .ma-definicion #fpm-i-02-d12}
**Definición 12 — Unidad derivada**
Una **unidad derivada** es una unidad asociada a una magnitud derivada y expresable, dentro del sistema de unidades considerado, mediante productos de potencias de unidades base.
:::

En el SI:

$$
\text{área}\longrightarrow \mathrm{m^2},
$$

$$
\text{volumen}\longrightarrow \mathrm{m^3},
$$

$$
\text{rapidez o velocidad}\longrightarrow \mathrm{m\,s^{-1}},
$$

$$
\text{aceleración}\longrightarrow \mathrm{m\,s^{-2}},
$$

$$
\text{densidad de masa}\longrightarrow \mathrm{kg\,m^{-3}}.
$$

La *SI Brochure* vigente incluye precisamente estas expresiones entre sus ejemplos de unidades derivadas coherentes.[^s4-bipm-derived]

### 4.5. Unidad derivada coherente

::: {.ma-block .ma-definicion #fpm-i-02-d13}
**Definición 13 — Unidad derivada coherente**
Una **unidad derivada coherente**, respecto de un sistema de magnitudes y un conjunto elegido de unidades base, es una unidad derivada que se obtiene como producto de potencias de las unidades base sin introducir ningún factor de proporcionalidad distinto de $1$.
:::

Así,

$$
\mathrm{m\,s^{-1}}
$$

es la unidad coherente SI de rapidez o velocidad,

$$
\mathrm{m\,s^{-2}}
$$

la de aceleración, y

$$
\mathrm{kg\,m^{-3}}
$$

la de densidad de masa.

En cambio,

$$
\mathrm{cm\,s^{-1}}
$$

puede ser una unidad perfectamente válida para expresar una rapidez, pero no es la unidad derivada coherente de rapidez **en el SI**, porque

$$
1\,\mathrm{cm}=10^{-2}\,\mathrm m
$$

introduce un factor distinto de $1$ respecto de la unidad base metro.

La coherencia no significa «unidad correcta frente a unidad incorrecta». Significa que la unidad se obtiene de la base elegida sin factores adicionales.

### 4.6. Por qué importa la coherencia

Consideremos

$$
v=\frac{\ell}{t}.
$$

Escribamos

$$
\ell=\{\ell\}_{\mathrm m}\,\mathrm m,
$$

$$
t=\{t\}_{\mathrm s}\,\mathrm s,
$$

$$
v=\{v\}_{\mathrm{m\,s^{-1}}}\,\mathrm{m\,s^{-1}}.
$$

Sustituyendo:

$$
\{v\}_{\mathrm{m\,s^{-1}}}\,\mathrm{m\,s^{-1}}
=
\frac{\{\ell\}_{\mathrm m}\,\mathrm m}
{\{t\}_{\mathrm s}\,\mathrm s}.
$$

Por tanto,

$$
\boxed{
\{v\}_{\mathrm{m\,s^{-1}}}
=
\frac{\{\ell\}_{\mathrm m}}{\{t\}_{\mathrm s}}
}.
$$

La ecuación entre valores numéricos conserva exactamente la forma de la ecuación entre magnitudes.

Éste es el sentido técnico de coherencia empleado por el BIPM.[^s4-bipm-coherent]

::: {.ma-block .ma-metodo #fpm-i-02-mp07}
**Principio 7 — La coherencia preserva la forma numérica de las ecuaciones de magnitudes**
Cuando todas las magnitudes de una relación se expresan mediante unidades pertenecientes a un sistema coherente, la ecuación entre sus valores numéricos tiene la misma forma que la ecuación entre las magnitudes, sin factores de conversión adicionales.
:::

### 4.7. Ejemplo: rapidez en unidades coherentes

Si

$$
\ell=120\,\mathrm m
$$

y

$$
t=30\,\mathrm s,
$$

entonces

$$
v=\frac{120\,\mathrm m}{30\,\mathrm s}
=
4\,\mathrm{m\,s^{-1}}.
$$

La ecuación numérica es simplemente

$$
4=\frac{120}{30}.
$$

No aparece ningún factor extra.

### 4.8. Qué ocurre cuando mezclamos unidades no coherentes

Expresemos la misma longitud como

$$
\ell=12\,000\,\mathrm{cm}.
$$

Si mantenemos $t$ en segundos y queremos $v$ en $\mathrm{m\,s^{-1}}$, entonces

$$
1\,\mathrm{cm}=10^{-2}\,\mathrm m
$$

y

$$
v
=
\frac{12\,000\times10^{-2}\,\mathrm m}
{30\,\mathrm s}
=
4\,\mathrm{m\,s^{-1}}.
$$

La ecuación numérica se vuelve

$$
\boxed{
\{v\}_{\mathrm{m\,s^{-1}}}
=
10^{-2}
\frac{\{\ell\}_{\mathrm{cm}}}{\{t\}_{\mathrm s}}
}.
$$

El factor $10^{-2}$ no pertenece a la física de la relación. Pertenece a nuestra mezcla de unidades.

Ésa es una ventaja práctica de la coherencia: separa la estructura física de los factores de conversión.

### 4.9. Área, volumen y potencias de unidades

Si un cuadrado tiene lado

$$
\ell=3\,\mathrm m,
$$

entonces

$$
A=\ell^2
=
(3\,\mathrm m)^2
=
9\,\mathrm{m^2}.
$$

La potencia actúa sobre el número y sobre la unidad.

Análogamente, si

$$
\ell=2\,\mathrm m,
$$

entonces

$$
V=\ell^3
=
(2\,\mathrm m)^3
=
8\,\mathrm{m^3}.
$$

Por eso

$$
1\,\mathrm{cm^2}
=
(10^{-2}\,\mathrm m)^2
=
10^{-4}\,\mathrm{m^2},
$$

y

$$
1\,\mathrm{cm^3}
=
(10^{-2}\,\mathrm m)^3
=
10^{-6}\,\mathrm{m^3}.
$$

### 4.10. Densidad de masa

Para

$$
\rho=\frac{m}{V},
$$

las unidades coherentes dan

$$
\rho
=
\frac{\{m\}_{\mathrm{kg}}}{\{V\}_{\mathrm{m^3}}}
\mathrm{kg\,m^{-3}}.
$$

Así,

$$
\boxed{
\{\rho\}_{\mathrm{kg\,m^{-3}}}
=
\frac{\{m\}_{\mathrm{kg}}}
{\{V\}_{\mathrm{m^3}}}
}.
$$

Si

$$
m=6\,\mathrm{kg}
$$

y

$$
V=2\times10^{-3}\,\mathrm{m^3},
$$

entonces

$$
\rho
=
3\times10^3\,\mathrm{kg\,m^{-3}}.
$$

### 4.11. Prefijos y coherencia

En §3 vimos que los prefijos introducen factores decimales.

Aunque el centímetro sea una unidad construida correctamente mediante un prefijo SI,

$$
1\,\mathrm{cm}=10^{-2}\,\mathrm m,
$$

y por tanto no pertenece al conjunto de unidades SI coherentes respecto de la base cuyo representante de longitud es el metro.

La *SI Brochure* indica expresamente que una unidad prefijada deja de ser coherente porque aparece un factor numérico distinto de $1$.[^s4-bipm-derived]

### 4.12. Unidades coherentes con nombres especiales

Ciertas combinaciones aparecen tan frecuentemente que el SI les asigna nombres y símbolos especiales.

Por ejemplo:

$$
1\,\mathrm N
=
1\,\mathrm{kg\,m\,s^{-2}},
$$

$$
1\,\mathrm{Pa}
=
1\,\mathrm{kg\,m^{-1}\,s^{-2}},
$$

$$
1\,\mathrm J
=
1\,\mathrm{kg\,m^2\,s^{-2}},
$$

$$
1\,\mathrm W
=
1\,\mathrm{kg\,m^2\,s^{-3}}.
$$

El nombre especial no cambia la estructura algebraica de la unidad.

::: {.ma-block .ma-metodo #fpm-i-02-mp08}
**Principio 8 — Un nombre especial no crea una nueva clase algebraica de unidad**
Una unidad SI con nombre especial sigue siendo una unidad coherente expresable mediante productos de potencias de unidades base. El nombre especial mejora la lectura y puede ayudar a distinguir contextos físicos, pero no altera la estructura algebraica de la unidad.
:::

### 4.13. Las 22 unidades SI con nombres especiales

La *SI Brochure* vigente enumera 22 unidades SI con nombres y símbolos especiales.[^s4-bipm-special]

| Magnitud asociada | Nombre | Símbolo | Expresión o relación coherente |
|---|---|---:|---|
| ángulo plano | radián | $\mathrm{rad}$ | $1$ |
| ángulo sólido | estereorradián | $\mathrm{sr}$ | $1$ |
| frecuencia | hercio | $\mathrm{Hz}$ | $\mathrm{s^{-1}}$ |
| fuerza | newton | $\mathrm N$ | $\mathrm{kg\,m\,s^{-2}}$ |
| presión, tensión mecánica | pascal | $\mathrm{Pa}$ | $\mathrm{kg\,m^{-1}\,s^{-2}}$ |
| energía, trabajo, calor | joule | $\mathrm J$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| potencia, flujo radiante | watt | $\mathrm W$ | $\mathrm{kg\,m^2\,s^{-3}}$ |
| carga eléctrica | coulomb | $\mathrm C$ | $\mathrm{A\,s}$ |
| diferencia de potencial | volt | $\mathrm V$ | $\mathrm{kg\,m^2\,s^{-3}\,A^{-1}}$ |
| capacitancia | farad | $\mathrm F$ | $\mathrm{kg^{-1}\,m^{-2}\,s^4\,A^2}$ |
| resistencia eléctrica | ohm | $\mathrm{\Omega}$ | $\mathrm{kg\,m^2\,s^{-3}\,A^{-2}}$ |
| conductancia eléctrica | siemens | $\mathrm S$ | $\mathrm{kg^{-1}\,m^{-2}\,s^3\,A^2}$ |
| flujo magnético | weber | $\mathrm{Wb}$ | $\mathrm{kg\,m^2\,s^{-2}\,A^{-1}}$ |
| densidad de flujo magnético | tesla | $\mathrm T$ | $\mathrm{kg\,s^{-2}\,A^{-1}}$ |
| inductancia | henry | $\mathrm H$ | $\mathrm{kg\,m^2\,s^{-2}\,A^{-2}}$ |
| temperatura Celsius | grado Celsius | $\mathrm{^\circ C}$ | mismo tamaño de intervalo que $\mathrm K$ |
| flujo luminoso | lumen | $\mathrm{lm}$ | $\mathrm{cd\,sr}$ |
| iluminancia | lux | $\mathrm{lx}$ | $\mathrm{lm\,m^{-2}}$ |
| actividad de un radionúclido | becquerel | $\mathrm{Bq}$ | $\mathrm{s^{-1}}$ |
| dosis absorbida | gray | $\mathrm{Gy}$ | $\mathrm{m^2\,s^{-2}}$ |
| dosis equivalente | sievert | $\mathrm{Sv}$ | $\mathrm{m^2\,s^{-2}}$ |
| actividad catalítica | katal | $\mathrm{kat}$ | $\mathrm{mol\,s^{-1}}$ |

No necesitamos memorizar la tabla. Debemos reconocer su arquitectura.

### 4.14. Misma expresión de unidad, distinta magnitud

Tenemos:

$$
\mathrm{Hz}=\mathrm{s^{-1}},
$$

pero también

$$
\mathrm{Bq}=\mathrm{s^{-1}}.
$$

Frecuencia y actividad de un radionúclido no son el mismo tipo de magnitud.

Análogamente,

$$
\mathrm{Gy}
=
\mathrm{m^2\,s^{-2}},
$$

y

$$
\mathrm{Sv}
=
\mathrm{m^2\,s^{-2}},
$$

pero dosis absorbida y dosis equivalente no son la misma magnitud física.

Por tanto:

$$
\boxed{
\text{misma expresión de unidad}
\not\Rightarrow
\text{mismo tipo de magnitud}.
}
$$

Los nombres especiales pueden ayudar a conservar la distinción semántica.

### 4.15. Energía y torque

La unidad coherente de energía puede escribirse

$$
\mathrm J=\mathrm{N\,m}.
$$

El torque o momento de una fuerza también utiliza una unidad expresable como

$$
\mathrm{N\,m}.
$$

Sin embargo, no se acostumbra llamar joule a la unidad de torque.

La razón es semántica: `J` señala magnitudes como energía o trabajo, mientras que `N m` conserva visible una interpretación distinta.

Así,

$$
\boxed{
\text{estructura dimensional}
\neq
\text{significado físico completo}.
}
$$

### 4.16. Coherencia no significa una única escritura

Una misma unidad coherente puede escribirse, por ejemplo,

$$
\mathrm{Pa}
=
\mathrm{N\,m^{-2}}
=
\mathrm{kg\,m^{-1}\,s^{-2}}.
$$

Las tres expresiones representan la misma unidad coherente.

La elección puede resaltar distintos aspectos de la estructura.

### 4.17. Ejemplo: expandir nombres especiales

Como

$$
\mathrm N
=
\mathrm{kg\,m\,s^{-2}},
$$

tenemos

$$
\mathrm{Pa}
=
\mathrm{N\,m^{-2}}
=
\mathrm{kg\,m^{-1}\,s^{-2}}.
$$

Además,

$$
\mathrm J
=
\mathrm{N\,m}
=
\mathrm{kg\,m^2\,s^{-2}},
$$

y

$$
\mathrm W
=
\mathrm{J\,s^{-1}}
=
\mathrm{kg\,m^2\,s^{-3}}.
$$

Los nombres especiales forman parte de la misma álgebra coherente.

### 4.18. Conversión de densidad

Calculemos

$$
1\,\mathrm{g\,cm^{-3}}
$$

en unidades coherentes SI.

Tenemos

$$
1\,\mathrm g
=
10^{-3}\,\mathrm{kg},
$$

y

$$
1\,\mathrm{cm^3}
=
10^{-6}\,\mathrm{m^3}.
$$

Por tanto,

$$
1\,\mathrm{g\,cm^{-3}}
=
\frac{10^{-3}\,\mathrm{kg}}
{10^{-6}\,\mathrm{m^3}}
=
10^3\,\mathrm{kg\,m^{-3}}.
$$

Así,

$$
\boxed{
1\,\mathrm{g\,cm^{-3}}
=
1000\,\mathrm{kg\,m^{-3}}.
}
$$

### 4.19. El álgebra de unidades no elige la física

Podemos formar matemáticamente

$$
\frac{m}{t},
$$

pero la teoría de unidades no decide por sí sola si esa combinación representa una magnitud relevante para el problema.

Para eso necesitamos una definición, una ley, una hipótesis de modelo o alguna otra razón física.

Por tanto:

$$
\boxed{
\text{álgebra de unidades}
\neq
\text{selección automática de variables físicas}.
}
$$

Esta limitación reaparecerá en el análisis dimensional.

### 4.20. Ficha de construcción de una unidad derivada

::: {.ma-block .ma-metodo}
**Ficha FPM — Construcción de una unidad derivada**
1. **Magnitud:** ¿qué cantidad estamos definiendo?
2. **Ecuación de magnitudes:** ¿qué relación la conecta con otras magnitudes?
3. **Tipos:** ¿qué tipos de magnitud intervienen?
4. **Unidades de entrada:** ¿qué unidades usamos?
5. **Álgebra:** ¿qué producto, cociente o potencia resulta?
6. **Factor:** ¿aparece un factor distinto de $1$?
7. **Coherencia:** ¿la unidad resultante es coherente en el SI?
8. **Nombre especial:** ¿existe uno?
9. **Semántica:** ¿otras magnitudes comparten la misma expresión?
10. **Modelo:** ¿qué justifica físicamente esta combinación?
:::
