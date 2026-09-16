### 6.16. Ecuaciones multiplicativas

La exigencia de igualdad dimensional término a término se refiere especialmente a **sumas e igualdades aditivas**.

En una relación multiplicativa,

$$
Q=AB,
$$

no exigimos

$$
[Q]=[A]=[B].
$$

Exigimos

$$
[Q]=[A][B].
$$

Por ejemplo,

$$
E=F\ell
$$

satisface

$$
[E]
=
[F][\ell]
=
MLT^{-2}L
=
ML^2T^{-2}.
$$

Así, una auditoría dimensional debe respetar la estructura algebraica de la ecuación:

- en productos, las dimensiones se multiplican;
- en cocientes, se dividen;
- en potencias, se elevan;
- en sumas, los términos deben ser homogéneos.

### 6.17. La dimensión de una derivada o cociente incremental

Todavía no necesitamos cálculo diferencial formal para comprender un patrón.

Si una magnitud $Q$ cambia durante un intervalo temporal $\Delta t$, el cociente

$$
\frac{\Delta Q}{\Delta t}
$$

posee dimensión

$$
\frac{[Q]}{T}.
$$

Así, si

$$
[Q]=L,
$$

entonces

$$
\left[
\frac{\Delta Q}{\Delta t}
\right]
=
LT^{-1}.
$$

Más adelante, cuando introduzcamos derivadas, el mismo razonamiento dimensional se conservará:

$$
\left[
\frac{dQ}{dt}
\right]
=
[Q]T^{-1}.
$$

La dimensión no sustituye al concepto de derivada.

Solo registra qué estructura dimensional debe tener el resultado.

### 6.18. La dimensión de una integral

De manera análoga, cuando más adelante encontremos una cantidad definida mediante una integral temporal,

$$
R=\int Q\,dt,
$$

la dimensión esperada será

$$
[R]=[Q]T.
$$

No desarrollaremos aquí integración.

El objetivo es mostrar que el análisis dimensional es compatible con las operaciones matemáticas que aparecerán después.

Cada operación modifica la dimensión de una manera controlable.

### 6.19. Funciones no algebraicas: frontera de esta sección

¿Qué ocurre con expresiones como

$$
\sin x,
$$

$$
e^x,
$$

o

$$
\log x?
$$

La respuesta exige tratar cuidadosamente las **cantidades de dimensión uno**.

Ése será el objeto de §8.

No adelantaremos ahora la discusión.

Solo registramos que no debemos aplicar reglas algebraicas de manera mecánica a funciones no polinómicas sin examinar la dimensión de sus argumentos.

### 6.20. Ejercicios

::: {.ma-block .ma-enunciado #fpm-i-02-e14}
**Ejercicio 14 — Auditoría de ecuaciones**

**Tipo:** análisis dimensional · **Nivel:** central

Decide cuáles de las siguientes ecuaciones son dimensionalmente homogéneas. No juzgues todavía si son físicamente correctas.

1.
$$
x=x_0+vt.
$$

2.
$$
x=x_0+vt^2.
$$

3.
$$
v=v_0+at.
$$

4.
$$
v=v_0+a t^2.
$$

5.
$$
E=F\ell.
$$

6.
$$
p=\frac{F}{A}.
$$
:::

::: {.ma-block .ma-comprobacion}
**Solución**

**1.**

$$
[x]=L,
$$

$$
[x_0]=L,
$$

$$
[vt]=LT^{-1}T=L.
$$

Es homogénea.

**2.**

$$
[vt^2]
=
LT^{-1}T^2
=
LT.
$$

No es homogénea.

**3.**

$$
[v_0]=LT^{-1},
$$

y

$$
[at]
=
LT^{-2}T
=
LT^{-1}.
$$

Es homogénea.

**4.**

$$
[at^2]
=
LT^{-2}T^2
=
L.
$$

No puede sumarse con una velocidad:

$$
L\neq LT^{-1}.
$$

No es homogénea.

**5.**

$$
[F\ell]
=
MLT^{-2}L
=
ML^2T^{-2}.
$$

La ecuación es homogénea si $E$ tiene dimensión de energía.

**6.**

$$
\left[\frac{F}{A}\right]
=
\frac{MLT^{-2}}{L^2}
=
ML^{-1}T^{-2}.
$$

La ecuación es homogénea si $p$ representa una magnitud de esa dimensión.

Resultado:

$$
\boxed{
1,\ 3,\ 5,\ 6
\text{ pasan el control dimensional;}
\quad
2,\ 4
\text{ fallan.}
}
$$
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e15}
**Ejercicio 15 — Determinar la dimensión de una constante**

**Familia:** `E-DIM / E-CALC / CORE`

En cada relación, determina la dimensión que debe tener la constante indicada para que la ecuación sea homogénea.

1.
$$
F=kx.
$$

2.
$$
E=\kappa t.
$$

3.
$$
x=ct.
$$

4.
$$
v^2=\alpha x.
$$
:::

::: {.ma-block .ma-comprobacion}
**Solución**

**1.**

Queremos

$$
[F]=[k][x].
$$

Entonces

$$
[k]
=
\frac{MLT^{-2}}{L}
=
MT^{-2}.
$$

**2.**

$$
[E]=[\kappa]T.
$$

Luego

$$
[\kappa]
=
\frac{ML^2T^{-2}}{T}
=
ML^2T^{-3}.
$$

**3.**

$$
L=[c]T.
$$

Por tanto

$$
[c]=LT^{-1}.
$$

**4.**

$$
[v^2]
=
L^2T^{-2}.
$$

Como

$$
[\alpha x]
=
[\alpha]L,
$$

necesitamos

$$
[\alpha]
=
LT^{-2}.
$$

En conjunto:

$$
\boxed{
[k]=MT^{-2},
\quad
[\kappa]=ML^2T^{-3},
\quad
[c]=LT^{-1},
\quad
[\alpha]=LT^{-2}.
}
$$
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e16}
**Ejercicio 16 — Homogénea pero no determinada**

**Familia:** `E-PROOF / E-CON / ADVANCED`

Considera la familia de ecuaciones

$$
x=x_0+Cvt,
$$

donde $C$ es una constante numérica.

1. Demuestra que la ecuación es dimensionalmente homogénea para todo número real $C$.
2. Explica por qué el análisis dimensional no puede determinar el valor de $C$.
3. ¿Qué tipo de información adicional sería necesaria para determinarlo físicamente?
4. ¿Qué enseña el ejercicio acerca de la Proposición 2?
:::

::: {.ma-block .ma-comprobacion}
**Solución**

Tenemos

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
LT^{-1}T
=
L.
$$

Un número puro $C$ no modifica la dimensión:

$$
[Cvt]=L.
$$

Por tanto,

$$
[x]=[x_0]=[Cvt]=L
$$

para cualquier

$$
C\in\mathbb R.
$$

La ecuación es dimensionalmente homogénea para todo $C$.

El análisis dimensional solo exige compatibilidad de dimensiones.

No distingue entre

$$
C=1,
$$

$$
C=2,
$$

$$
C=-17,
$$

o cualquier otro valor.

Para determinar $C$ necesitaríamos información adicional, por ejemplo:

- una ley física más específica;
- una derivación a partir de postulados del modelo;
- una condición experimental;
- datos empíricos;
- una simetría u otra restricción estructural.

El ejercicio muestra exactamente el alcance de la Proposición 2:

$$
\boxed{
\text{homogeneidad}
=
\text{condición necesaria},
}
$$

pero

$$
\boxed{
\text{homogeneidad}
\neq
\text{determinación completa de la ley}.
}
$$
:::

### 6.21. Síntesis

La idea central de la sección es:

$$
\boxed{
\text{una ecuación física no debe depender de la convención usada para medir}.
}
$$

Al cambiar independientemente las unidades base, cada término adquiere un factor controlado por su dimensión.

Para que una suma conserve su forma física, todos los términos aditivos deben transformarse con el mismo factor.

De ahí la Proposición 2:

$$
\boxed{
Q_1+\cdots+Q_r
=
R_1+\cdots+R_s
}
$$

implica, bajo las hipótesis declaradas,

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

La homogeneidad permite detectar errores estructurales.

Pero no selecciona por sí sola la ley correcta.

Por tanto:

$$
\boxed{
\text{inhomogeneidad}
\Rightarrow
\text{problema},
}
$$

mientras

$$
\boxed{
\text{homogeneidad}
\not\Rightarrow
\text{verdad física}.
}
$$

La siguiente sección convertirá esta condición necesaria en una herramienta de trabajo sistemática:

$$
\boxed{
\text{§7 — El análisis dimensional como auditoría}.
}
$$

---

### Notas y fuentes

[^s6-bipm-homogeneity]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.3, pp. 132–133.
[^s6-vim-dimension]: JCGM, *VIM*, 3.ª ed., entradas 1.2, 1.4 y 1.7.
[^s6-zorich-homogeneity]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §1.2, pp. 6–8.
