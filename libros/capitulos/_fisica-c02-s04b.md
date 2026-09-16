### 4.21. Ejercicios

::: {.ma-block .ma-enunciado #fpm-i-02-e08}
**Ejercicio 8 — Construir unidades derivadas coherentes**
**Tipo:** análisis dimensional · **Nivel:** básico

Determina la unidad derivada coherente SI para:

1. $A=xy$.
2. $V=xyz$.
3. $v=\ell/t$.
4. $a=v/t$.
5. $\rho=m/V$.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

1.

$$
\mathrm m\cdot\mathrm m
=
\boxed{\mathrm{m^2}}.
$$

2.

$$
\mathrm m^3
=
\boxed{\mathrm{m^3}}.
$$

3.

$$
\frac{\mathrm m}{\mathrm s}
=
\boxed{\mathrm{m\,s^{-1}}}.
$$

4.

$$
\frac{\mathrm{m\,s^{-1}}}{\mathrm s}
=
\boxed{\mathrm{m\,s^{-2}}}.
$$

5.

$$
\frac{\mathrm{kg}}{\mathrm{m^3}}
=
\boxed{\mathrm{kg\,m^{-3}}}.
$$

Todas se obtienen con factor $1$ respecto de las unidades base del SI.
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e09}
**Ejercicio 9 — Coherencia y factor de conversión**
**Tipo:** cálculo · **Nivel:** central

Sea

$$
\ell=750\,\mathrm{cm},
\qquad
t=25\,\mathrm s.
$$

1. Calcula $v=\ell/t$ en $\mathrm{cm\,s^{-1}}$.
2. Convierte el resultado a $\mathrm{m\,s^{-1}}$.
3. Escribe la relación entre $\{v\}_{\mathrm{m\,s^{-1}}}$, $\{\ell\}_{\mathrm{cm}}$ y $\{t\}_{\mathrm s}$.
4. Explica el factor de conversión.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

1.

$$
v
=
\frac{750\,\mathrm{cm}}{25\,\mathrm s}
=
30\,\mathrm{cm\,s^{-1}}.
$$

2.

$$
30\,\mathrm{cm\,s^{-1}}
=
30\times10^{-2}\,\mathrm{m\,s^{-1}}
=
\boxed{0.30\,\mathrm{m\,s^{-1}}}.
$$

3.

$$
\boxed{
\{v\}_{\mathrm{m\,s^{-1}}}
=
10^{-2}
\frac{\{\ell\}_{\mathrm{cm}}}{\{t\}_{\mathrm s}}
}.
$$

4. El factor $10^{-2}$ aparece porque el centímetro introduce una escala distinta de la unidad base metro.
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e10}
**Ejercicio 10 — Nombres especiales, expansión y significado**
**Familia:** `E-DIM / E-CON / CORE`

1. Expande en unidades base:

$$
\mathrm N,\qquad
\mathrm{Pa},\qquad
\mathrm J,\qquad
\mathrm W.
$$

2. Demuestra:

$$
\mathrm{Pa}=\mathrm{N\,m^{-2}},
\qquad
\mathrm J=\mathrm{N\,m}.
$$

3. Explica por qué

$$
\mathrm{Hz}=\mathrm{Bq}=\mathrm{s^{-1}}
$$

no implica que frecuencia y actividad sean la misma magnitud.

4. Convierte

$$
2.5\,\mathrm{g\,cm^{-3}}
$$

a $\mathrm{kg\,m^{-3}}$.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

1.

$$
\mathrm N
=
\boxed{\mathrm{kg\,m\,s^{-2}}},
$$

$$
\mathrm{Pa}
=
\boxed{\mathrm{kg\,m^{-1}\,s^{-2}}},
$$

$$
\mathrm J
=
\boxed{\mathrm{kg\,m^2\,s^{-2}}},
$$

$$
\mathrm W
=
\boxed{\mathrm{kg\,m^2\,s^{-3}}}.
$$

2.

$$
\mathrm{N\,m^{-2}}
=
\mathrm{kg\,m\,s^{-2}}\mathrm{m^{-2}}
=
\mathrm{kg\,m^{-1}\,s^{-2}}
=
\mathrm{Pa},
$$

y

$$
\mathrm{N\,m}
=
\mathrm{kg\,m^2\,s^{-2}}
=
\mathrm J.
$$

3. La igualdad algebraica de las expresiones de unidad no identifica el tipo de magnitud. `Hz` conserva la interpretación de frecuencia; `Bq` la de actividad.

4.

$$
2.5\,\mathrm{g\,cm^{-3}}
=
2.5\times10^3\,\mathrm{kg\,m^{-3}}
=
\boxed{2500\,\mathrm{kg\,m^{-3}}}.
$$
:::

### 4.22. Síntesis

Las relaciones entre magnitudes generan relaciones entre unidades:

$$
Q=Q_1Q_2
\quad\Rightarrow\quad
u=u_1u_2,
$$

$$
Q=\frac{Q_1}{Q_2}
\quad\Rightarrow\quad
u=\frac{u_1}{u_2},
$$

$$
Q=Q_1^n
\quad\Rightarrow\quad
u=u_1^n.
$$

Definimos magnitud derivada, unidad derivada y unidad derivada coherente.

La propiedad central es:

$$
\boxed{
\text{coherencia}
\Longrightarrow
\text{misma forma de la ecuación para magnitudes y valores numéricos}.
}
$$

Pero conservamos dos límites:

$$
\boxed{
\text{misma expresión de unidad}
\not\Rightarrow
\text{mismo tipo de magnitud}
}
$$

y

$$
\boxed{
\text{álgebra de unidades}
\not\Rightarrow
\text{selección automática de las variables físicas correctas}.
}
$$

La siguiente sección construirá una estructura que no depende de la unidad concreta elegida:

$$
\boxed{
\text{§5 — Dimensión física}.
}
$$

[^s4-bipm-derived]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01 (2026), §2.3.4, pp. 133–137.
[^s4-bipm-coherent]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.4, pp. 133–137; compárese JCGM, *VIM*, entrada 1.12, «coherent derived unit».
[^s4-bipm-special]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.4, tabla 4, pp. 133–136.
