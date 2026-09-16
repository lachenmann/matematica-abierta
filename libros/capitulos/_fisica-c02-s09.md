## §9 — Escalas características y órdenes de magnitud {#fpm-i-02-s09}

### 9.1. Intuir: una magnitud puede ser grande o pequeña solo respecto de una escala

Decir que

$$
\ell=2\,\mathrm{mm}
$$

es «pequeño» no tiene todavía un significado físico completo.

Dos milímetros pueden ser enormes frente al espesor de una membrana y diminutos frente al tamaño de una habitación.

La afirmación correcta necesita una referencia:

$$
\boxed{
\text{grande o pequeño}
\quad
\text{respecto de una escala}.
}
$$

Ésta es la función de una **escala característica**.

### 9.2. Escala característica

::: {.ma-block .ma-definicion}
**Definición 32 — Escala característica**
Una **escala característica** de una magnitud $Q$ en un modelo es un valor de referencia $Q_\ast$, del mismo tipo de magnitud, elegido para representar el tamaño relevante de $Q$ en el fenómeno o régimen considerado.
:::

La escala puede proceder de:

- una dimensión geométrica del sistema;
- un parámetro del modelo;
- una condición inicial;
- un valor experimental representativo;
- una escala impuesta externamente.

No tiene por qué ser un promedio ni el valor máximo.

Su elección depende de la pregunta física.

::: {.ma-block .ma-metodo}
**Principio 27 — Una escala característica pertenece al modelo**
Una escala característica no se deduce únicamente de la dimensión de una magnitud. Debe justificarse por la geometría, el régimen, los datos o la estructura física del problema.
:::

### 9.3. Representar una magnitud respecto de su escala

Si $Q_\ast$ es una escala característica de $Q$, la razón

$$
\widehat Q
=
\frac{Q}{Q_\ast}
$$

tiene dimensión uno:

$$
[\widehat Q]=1.
$$

Entonces podemos interpretar:

$$
\widehat Q\ll1
$$

como «$Q$ es pequeño respecto de $Q_\ast$»,

$$
\widehat Q\sim1
$$

como «$Q$ es comparable con $Q_\ast$», y

$$
\widehat Q\gg1
$$

como «$Q$ es grande respecto de $Q_\ast$».

La escala convierte una comparación cualitativa en una afirmación cuantitativa.

### 9.4. Varias escalas características pueden coexistir

Un sistema puede contener más de una longitud relevante.

Por ejemplo:

$$
L,\qquad \ell.
$$

Si

$$
\ell\ll L,
$$

la razón

$$
\varepsilon=\frac{\ell}{L}
$$

es pequeña.

Pero no existe una regla universal que obligue a elegir $L$ como escala y no $\ell$.

La elección depende de la representación que resulte útil.

Si normalizamos con $L$:

$$
\frac{\ell}{L}=\varepsilon.
$$

Si normalizamos con $\ell$:

$$
\frac{L}{\ell}=\varepsilon^{-1}.
$$

Ambas descripciones contienen la misma comparación.

### 9.5. Década decimal

Conservaremos una herramienta numérica de la primera redacción.

::: {.ma-block .ma-definicion}
**Definición 22 — Década decimal**
Si

$$
x=a\times10^n,
\qquad
1\le a<10,
$$

llamaremos **década decimal** de $x$ al intervalo

$$
[10^n,10^{n+1}).
$$
:::

La década registra una escala decimal gruesa.

### 9.6. Orden de magnitud

::: {.ma-block .ma-definicion}
**Definición 23 — Orden de magnitud**
Para $x>0$, el **orden de magnitud decimal** de $x$ será la potencia de diez más cercana en escala logarítmica.
:::

Si

$$
x=a\times10^n,
\qquad
1\le a<10,
$$

entonces:

$$
\operatorname{OM}(x)=
\begin{cases}
10^n, & 1\le a<\sqrt{10},\\
10^{n+1}, & \sqrt{10}<a<10.
\end{cases}
$$

En el caso frontera

$$
a=\sqrt{10},
$$

declararemos explícitamente la convención utilizada.

El umbral aparece porque el punto medio multiplicativo satisface:

$$
\frac{x}{10^n}
=
\frac{10^{n+1}}{x},
$$

de donde:

$$
x=\sqrt{10}\,10^n.
$$

::: {.ma-block .ma-metodo}
**Principio 17 — Un orden de magnitud describe escala, no precisión**
Informar un orden de magnitud identifica una escala multiplicativa dominante. No equivale a conocer con precisión el coeficiente numérico ni sus cifras significativas.
:::

### 9.7. Escala característica y orden de magnitud no son lo mismo

Una escala característica es una **elección física del modelo**.

Un orden de magnitud es una **clasificación numérica aproximada**.

Por ejemplo, podemos adoptar:

$$
L_\ast=2.4\,\mathrm m
$$

como escala geométrica relevante.

Su orden de magnitud puede ser:

$$
10^0\,\mathrm m.
$$

Pero reemplazar sistemáticamente $L_\ast$ por $1\,\mathrm m$ puede perder información física útil.

Así:

$$
\boxed{
\text{escala característica}
\neq
\text{orden de magnitud}.
}
$$

### 9.8. Escalas derivadas

Si elegimos una escala de longitud:

$$
L_\ast
$$

y una escala de tiempo:

$$
T_\ast,
$$

aparece naturalmente una escala de velocidad:

$$
V_\ast
=
\frac{L_\ast}{T_\ast}.
$$

También una escala de aceleración:

$$
A_\ast
=
\frac{L_\ast}{T_\ast^2}.
$$

La estructura dimensional permite construir escalas coherentes a partir de las escalas básicas seleccionadas por el modelo.

### 9.9. Ejemplo: movimiento en una pista

Supongamos que una pista tiene longitud característica:

$$
L_\ast=400\,\mathrm m
$$

y que el fenómeno que estudiamos dura típicamente:

$$
T_\ast=50\,\mathrm s.
$$

La escala de velocidad asociada es:

$$
V_\ast
=
\frac{400\,\mathrm m}{50\,\mathrm s}
=
8\,\mathrm{m\,s^{-1}}.
$$

Una velocidad:

$$
v=2\,\mathrm{m\,s^{-1}}
$$

corresponde a:

$$
\widehat v
=
\frac{v}{V_\ast}
=
0.25.
$$

Una velocidad:

$$
v=10\,\mathrm{m\,s^{-1}}
$$

corresponde a:

$$
\widehat v
=
1.25.
$$

La comparación no depende de memorizar si $2$ o $10$ son números «grandes».

Depende del fenómeno y de su escala.

### 9.10. Parámetros pequeños y grandes

Las razones de escala permiten identificar regímenes.

Si:

$$
\varepsilon
=
\frac{\ell}{L}
\sim10^{-3},
$$

entonces:

$$
\varepsilon\ll1.
$$

Esa información puede justificar más adelante aproximaciones del tipo:

$$
\text{corrección de orden }\varepsilon
$$

o:

$$
\text{efecto dominante frente a uno pequeño}.
$$

El análisis dimensional no decide por sí solo qué términos pueden descartarse.

Pero ayuda a construir el parámetro que hace cuantitativa la pregunta.

### 9.11. Estimación física: puente hacia el capítulo siguiente

Conservamos el concepto ya activado:

::: {.ma-block .ma-definicion}
**Definición 24 — Estimación física**
Una **estimación física** es una inferencia cuantitativa aproximada construida a partir de un modelo simplificado, valores representativos, cotas o escalas plausibles, con las hipótesis y la precisión pretendida explícitas.
:::

::: {.ma-block .ma-metodo}
**Principio 18 — Toda estimación debe exponer su modelo**
Una estimación es auditable solo si hace visibles las cantidades intermedias, los valores representativos y las simplificaciones utilizadas.
:::

En este capítulo usaremos esta idea solo para **identificar escalas**.

El desarrollo sistemático de:

- estimaciones tipo Fermi;
- cifras significativas;
- cotas experimentales;
- incertidumbre;
- propagación de incertidumbres;
- precisión de resultados;

pertenece al capítulo 3.

### 9.12. Práctica guiada

::: {.ma-block .ma-enunciado}
**Ejercicio 20 — Elegir y usar escalas características**

**Objetivo:** `Consolidación → Diagnóstico → Síntesis`

**Intenta primero: 3–5 min antes de leer la solución.**

Un movimiento ocurre en una región cuya longitud relevante es

$$
L_\ast=100\,\mathrm m
$$

y durante un tiempo característico

$$
T_\ast=20\,\mathrm s.
$$

1. Construye la escala de velocidad $V_\ast$.
2. Para $x=5\,\mathrm m$, $t=4\,\mathrm s$ y $v=15\,\mathrm{m\,s^{-1}}$, calcula

$$
\widehat x=\frac{x}{L_\ast},
\qquad
\widehat t=\frac{t}{T_\ast},
\qquad
\widehat v=\frac{v}{V_\ast}.
$$

3. Clasifica cada razón como pequeña, de orden uno o grande respecto de la escala elegida.
4. Explica por qué cambiar metros por centímetros no cambia $\widehat x$.
5. Si elegimos por error una escala $L_\ast=1\,\mathrm{mm}$ para el mismo fenómeno, explica qué se vuelve pedagógicamente poco útil aunque la razón siga siendo matemáticamente válida.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

La escala de velocidad es:

$$
V_\ast
=
\frac{L_\ast}{T_\ast}
=
\frac{100\,\mathrm m}{20\,\mathrm s}
=
5\,\mathrm{m\,s^{-1}}.
$$

Entonces:

$$
\widehat x
=
\frac{5}{100}
=
0.05,
$$

$$
\widehat t
=
\frac{4}{20}
=
0.2,
$$

y:

$$
\widehat v
=
\frac{15}{5}
=
3.
$$

Respecto de las escalas elegidas:

- $\widehat x=0.05$ es pequeño;
- $\widehat t=0.2$ es menor que uno pero no extremadamente pequeño;
- $\widehat v=3$ es de orden uno en sentido de escala: difiere de la referencia solo por un factor de pocos.

Si escribimos:

$$
x=500\,\mathrm{cm}
$$

y:

$$
L_\ast=10\,000\,\mathrm{cm},
$$

la razón sigue siendo:

$$
\widehat x
=
\frac{500}{10\,000}
=
0.05.
$$

La variable reducida es independiente de la unidad coherentemente utilizada.

Finalmente, elegir:

$$
L_\ast=1\,\mathrm{mm}
$$

daría:

$$
\widehat x=5000.
$$

La razón es correcta, pero la escala elegida no representa bien el tamaño característico del fenómeno y oculta en lugar de revelar su estructura.
:::

### 9.13. Autoexplicación

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Explica:

1. por qué una escala característica no es una unidad;
2. por qué una escala característica no es necesariamente un orden de magnitud;
3. qué información añade la razón $Q/Q_\ast$;
4. por qué una mala elección de escala puede ser matemáticamente válida y físicamente poco informativa.
:::

### 9.14. Conectar

Hemos construido razones:

$$
\widehat Q=\frac{Q}{Q_\ast}
$$

de dimensión uno.

La siguiente sección convertirá esta idea en un procedimiento sistemático para reescribir modelos completos:

$$
\boxed{
\text{§10 — Adimensionalización e inferencia dimensional}.
}
$$

La pregunta dejará de ser únicamente:

> ¿cuál es el tamaño característico de cada variable?

y pasará a ser:

> ¿cómo reescribimos todo el problema en variables de dimensión uno y qué parámetros sobreviven a esa reducción?
