### 10.20. Variar: si añadimos una variable de dimensión uno

Volvamos al péndulo.

Si además del largo $\ell$ y de $g$ incluimos un ángulo inicial $\theta_0$, con

$$
[\theta_0]=1,
$$

la dimensión ya no puede fijar completamente la dependencia.

Podemos escribir

$$
\boxed{
T_p
=
\sqrt{\frac{\ell}{g}}\,\Phi(\theta_0).
}
$$

Para oscilaciones pequeñas,

$$
\Phi(\theta_0)
\approx
2\pi.
$$

Para amplitudes mayores, la función cambia.

La dimensión no puede decidir esa dependencia porque $\theta_0$ ya es de dimensión uno.

Este ejemplo muestra por qué los parámetros adimensionales concentran información física que el análisis dimensional deja libre.

### 10.21. Ejercicios práctica guiada

::: {.ma-block .ma-enunciado #fpm-i-02-e21}
**Ejercicio 21 — Adimensionalizar una relación cinemática**

**Objetivo:** `Consolidación`

**Intenta primero: 3–5 min antes de leer la solución.**

Considera:

$$
x=x_0+vt.
$$

Elige escalas $L_\ast$ y $T_\ast$ y define:

$$
V_\ast=\frac{L_\ast}{T_\ast}.
$$

1. Introduce

$$
\widehat x=\frac{x}{L_\ast},
\quad
\widehat x_0=\frac{x_0}{L_\ast},
\quad
\widehat t=\frac{t}{T_\ast},
\quad
\widehat v=\frac{v}{V_\ast}.
$$

2. Demuestra que la relación se convierte en

$$
\boxed{
\widehat x=\widehat x_0+\widehat v\,\widehat t.
}
$$

3. Explica por qué todas las variables con sombrero tienen dimensión uno.
4. Explica qué ocurriría si se eligiera una escala de velocidad distinta de $L_\ast/T_\ast$.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

Sustituimos:

$$
x=L_\ast\widehat x,
\qquad
x_0=L_\ast\widehat x_0,
$$

$$
v=V_\ast\widehat v,
\qquad
t=T_\ast\widehat t.
$$

Entonces:

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
L_\ast\widehat x
=
L_\ast
\left(
\widehat x_0+\widehat v\widehat t
\right).
$$

Dividiendo por $L_\ast$:

$$
\boxed{
\widehat x=\widehat x_0+\widehat v\widehat t.
}
$$

Además:

$$
[\widehat x]
=
\frac{L}{L}
=
1,
$$

y análogamente:

$$
[\widehat x_0]
=
[\widehat t]
=
[\widehat v]
=
1.
$$

Si eligiéramos una escala de velocidad arbitraria $V_\ast'$,
aparecería el parámetro

$$
\frac{V_\ast'T_\ast}{L_\ast}.
$$

La elección

$$
V_\ast=L_\ast/T_\ast
$$

absorbe ese factor y revela una forma reducida más simple.
:::

::: {.ma-block .ma-enunciado #fpm-i-02-e22}
**Ejercicio 22 — Qué sobrevive a la adimensionalización**

**Objetivo:** `Diagnóstico → Síntesis`

**Intenta primero: 3–5 min antes de leer la solución.**

Sean $x$ e $y$ dos longitudes y $Q$ otra longitud. Buckingham y la homogeneidad permiten una forma

$$
Q=y\,\Phi\left(\frac{x}{y}\right).
$$

1. Define:

$$
\widehat Q=\frac{Q}{y},
\qquad
\xi=\frac{x}{y}.
$$

2. Reescribe la relación en forma adimensional.
3. Explica qué información ha desaparecido y cuál permanece.
4. ¿Puede el análisis dimensional determinar $\Phi$?
5. Aplica la misma lectura al péndulo:

$$
P=
\sqrt{\frac{\ell}{g}}
\Psi(\varphi_0).
$$
:::

::: {.ma-block .ma-comprobacion}
**Solución**

Dividiendo por $y$:

$$
\boxed{
\widehat Q=\Phi(\xi).
}
$$

Tanto:

$$
\widehat Q
$$

como:

$$
\xi
$$

tienen dimensión uno.

La unidad concreta de longitud ha desaparecido de la forma reducida.

Pero no ha desaparecido la física: permanece en la función $\Phi$ y en el significado de la razón $x/y$.

El análisis dimensional no determina $\Phi$.

Para el péndulo podemos definir:

$$
\widehat P
=
P\sqrt{\frac g\ell}.
$$

Entonces:

$$
\boxed{
\widehat P=\Psi(\varphi_0).
}
$$

La adimensionalización ha aislado exactamente la dependencia que no puede fijarse solo con dimensiones.
:::

### 10.22. Autoexplicación

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Sin revisar los ejemplos, responde:

1. ¿qué hipótesis adicional introducimos al escribir un ansatz monomial?;
2. ¿por qué una solución única para los exponentes no equivale a una ley física única?;
3. ¿qué significa que aparezca una función $\Phi$ de una cantidad de dimensión uno?;
4. ¿qué información proviene de las dimensiones y cuál proviene de la modelización?
:::

### 10.23. Conectar con Buckingham $\Pi$

La estructura que acabamos de encontrar puede resumirse así.

A veces las dimensiones fijan una combinación monomial básica:

$$
Q_0.
$$

Pero si existen combinaciones independientes de dimensión uno,

$$
\Pi_1,\ldots,\Pi_k,
$$

la forma más general puede contener

$$
\boxed{
Q
=
Q_0\,\Phi(\Pi_1,\ldots,\Pi_k).
}
$$

Ésta es precisamente la dirección que formalizará el teorema $\Pi$.

No lo demostramos todavía.

§10 ha construido el problema que ese teorema resolverá.

### 10.24. Síntesis

La inferencia dimensional comienza con una elección física de variables y una hipótesis de forma.

Para un ansatz

$$
Q=C\prod_iX_i^{\alpha_i},
$$

la homogeneidad se convierte en un sistema lineal para los exponentes:

$$
\boxed{
\mathbf d(Q)
=
\sum_i\alpha_i\mathbf d(X_i).
}
$$

La Proposición 3 demuestra que resolver ese sistema es exactamente la condición de homogeneidad del ansatz monomial.

Pero la dimensión no determina por sí sola:

- la selección correcta de variables;
- la validez del ansatz;
- constantes numéricas adimensionales;
- funciones de parámetros de dimensión uno;
- el régimen físico de validez.

Por tanto:

$$
\boxed{
\text{inferencia dimensional}
=
\text{restricción estructural},
\not\equiv
\text{derivación completa de una ley}.
}
$$

El siguiente paso será:

$$
\boxed{
\text{§11 — Semejanza, escalamiento y cambio de escala}.
}
$$

---

### Notas y fuentes

[^s10-zorich-dim]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §§1.2–1.3, pp. 6–10, y cap. 2, §§2.1–2.3, pp. 11–14.
