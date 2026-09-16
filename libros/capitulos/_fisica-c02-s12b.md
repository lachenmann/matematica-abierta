### 12.15. Los grupos Π no son únicos

Supongamos que:

$$
\Pi_1,\Pi_2
$$

son dos grupos independientes.

Entonces también pueden servir, por ejemplo:

$$
\widetilde\Pi_1=\Pi_1\Pi_2,
$$

$$
\widetilde\Pi_2=\Pi_2.
$$

O:

$$
\widehat\Pi_1=\Pi_1^2,
$$

$$
\widehat\Pi_2=\frac{\Pi_2}{\Pi_1},
$$

si la transformación entre conjuntos conserva independencia y puede invertirse en la región considerada.

Por tanto:

$$
\boxed{
\text{el conjunto de grupos }\Pi
\text{ no es canónico}.
}
$$

Lo canónico es la cantidad de grados de libertad:

$$
n-r.
$$

La elección práctica debe favorecer grupos con interpretación física clara.

### 12.16. Ejemplo elemental: número de Reynolds dimensional

Consideremos las variables:

$$
v,\quad L,\quad \rho,\quad \mu,
$$

con:

$$
[v]=LT^{-1},
$$

$$
[L]=L,
$$

$$
[\rho]=ML^{-3},
$$

$$
[\mu]=ML^{-1}T^{-1}.
$$

Usaremos el orden:

$$
(T,L,M).
$$

La matriz dimensional es:

$$
A
=
\begin{pmatrix}
-1 & 0 & 0 & -1\\
1 & 1 & -3 & -1\\
0 & 0 & 1 & 1
\end{pmatrix}.
$$

Su rango es:

$$
r=3.
$$

Como:

$$
n=4,
$$

esperamos:

$$
n-r=1
$$

grupo independiente.

Buscamos:

$$
\Pi
=
v^\alpha
L^\beta
\rho^\gamma
\mu^\delta.
$$

La condición:

$$
A
\begin{pmatrix}
\alpha\\
\beta\\
\gamma\\
\delta
\end{pmatrix}
=
0
$$

produce:

$$
-\alpha-\delta=0,
$$

$$
\alpha+\beta-3\gamma-\delta=0,
$$

$$
\gamma+\delta=0.
$$

Tomando:

$$
\alpha=1,
$$

obtenemos:

$$
\delta=-1,
$$

$$
\gamma=1,
$$

$$
\beta=1.
$$

Por tanto:

$$
\boxed{
\Pi
=
\frac{\rho vL}{\mu}.
}
$$

Éste es el grupo que, en mecánica de fluidos, se denomina número de Reynolds.

Aquí nos interesa primero su estructura dimensional.

Su interpretación física detallada pertenecerá a capítulos posteriores de fluidos.

### 12.17. Poner a prueba: contar dimensiones sin calcular rango

Supongamos que las variables tienen dimensiones:

$$
[x]=L,
$$

$$
[y]=L^2T^{-1},
$$

$$
[z]=L^3T^{-2}.
$$

Alguien dice:

> «Aparecen $L$ y $T$, así que el rango es $2$.»

No necesariamente.

Miremos las columnas en el orden $(L,T)$:

$$
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
\begin{pmatrix}
2\\
-1
\end{pmatrix},
\qquad
\begin{pmatrix}
3\\
-2
\end{pmatrix}.
$$

Las dos primeras son independientes.

La tercera satisface:

$$
\begin{pmatrix}
3\\
-2
\end{pmatrix}
=
-1
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
2
\begin{pmatrix}
2\\
-1
\end{pmatrix}.
$$

Por tanto:

$$
r=2.
$$

En este caso el conteo superficial acertó.

Pero acertó porque las columnas realmente alcanzan rango $2$.

Si todas las columnas fueran múltiplos de una sola, el rango sería $1$ aunque aparecieran varios exponentes numéricos.

La eliminación gaussiana es el control fiable.

### 12.18. Ejercicios práctica guiada

::: {.ma-block .ma-enunciado}
**Ejercicio 24 — Construir un grupo $\Pi$ por eliminación**

**Objetivo:** `Consolidación`

**Intenta primero: 3–5 min antes de leer la solución.**

Usa:

$$
v,\quad L,\quad\rho,\quad\mu
$$

con las dimensiones de §12.16.

1. Construye la matriz dimensional.
2. Comprueba que su rango es $3$.
3. Resuelve $A\alpha=0$.
4. Construye un grupo $\Pi$.
5. Verifica directamente que $[\Pi]=1$.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

La matriz es:

$$
A
=
\begin{pmatrix}
-1 & 0 & 0 & -1\\
1 & 1 & -3 & -1\\
0 & 0 & 1 & 1
\end{pmatrix}.
$$

Las columnas de $v,L,\rho$ son independientes, por lo que:

$$
r=3.
$$

Con $n=4$:

$$
n-r=1.
$$

El sistema homogéneo es:

$$
-\alpha-\delta=0,
$$

$$
\alpha+\beta-3\gamma-\delta=0,
$$

$$
\gamma+\delta=0.
$$

Tomando:

$$
\alpha=1,
$$

resulta:

$$
\delta=-1,
\qquad
\gamma=1,
\qquad
\beta=1.
$$

Así:

$$
\boxed{
\Pi=\frac{\rho vL}{\mu}.
}
$$

Verificación:

$$
[\rho vL]
=
ML^{-3}
\cdot
LT^{-1}
\cdot
L
=
ML^{-1}T^{-1}.
$$

Como:

$$
[\mu]=ML^{-1}T^{-1},
$$

obtenemos:

$$
\boxed{
[\Pi]=1.
}
$$
:::

::: {.ma-block .ma-enunciado}
**Ejercicio 25 — Reconstruir la cuenta $n-r$**

**Objetivo:** `Demostración — consolidación`

**Intenta primero: 3–5 min antes de leer la solución.**

Sea $A$ una matriz dimensional con $n$ columnas y rango $r$.

1. Explica mediante eliminación gaussiana por qué el sistema

$$
A\alpha=0
$$

tiene $n-r$ variables libres.
2. Explica por qué cada solución produce un monomio adimensional.
3. Explica por qué una elección de $n-r$ soluciones independientes genera todos los monomios adimensionales.
4. Señala qué paso adicional hace falta para pasar de este resultado algebraico al teorema físico de Buckingham.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

**1.**

El rango $r$ significa que una forma escalonada de $A$ posee:

$$
r
$$

pivotes.

Como existen:

$$
n
$$

incógnitas, quedan:

$$
\boxed{
n-r
}
$$

variables libres.

**2.**

Si:

$$
A\alpha=0,
$$

entonces la firma dimensional de:

$$
\Pi
=
\prod_iq_i^{\alpha_i}
$$

es cero.

Por tanto:

$$
[\Pi]=1.
$$

**3.**

Las soluciones del sistema homogéneo se obtienen asignando valores a las variables libres y resolviendo las pivote.

Una base de soluciones independientes permite escribir cualquier solución como combinación de ellas.

Al volver a los monomios, la suma de vectores de exponentes se convierte en producto de potencias de grupos $\Pi$.

Por tanto, los grupos asociados generan todos los monomios adimensionales.

**4.**

Falta la hipótesis física de que la relación sea independiente de la elección de unidades.

Solo entonces podemos concluir que la información de la relación puede reorganizarse mediante los invariantes adimensionales.

Esta separación es esencial:

$$
\boxed{
\text{álgebra dimensional}
+
\text{invariancia física}
\Longrightarrow
\text{Buckingham }\Pi.
}
$$
:::

::: {.ma-block .ma-enunciado}
**Ejercicio 26 — Variables redundantes y rango dimensional**

**Objetivo:** `Diagnóstico → Síntesis`

**Intenta primero: 3–5 min antes de leer la solución.**

Considera:

$$
F,\quad m,\quad a,\quad \ell_1,\quad \ell_2,
$$

con:

$$
[F]=MLT^{-2},
$$

$$
[m]=M,
$$

$$
[a]=LT^{-2},
$$

$$
[\ell_1]=[\ell_2]=L.
$$

1. Construye la matriz dimensional usando $(T,L,M)$.
2. Determina su rango.
3. ¿Cuántos grupos $\Pi$ independientes deben existir?
4. Encuentra dos.
5. Explica por qué añadir $\ell_2$ aumenta $n$ pero no el rango.
6. Explica qué enseña esto sobre la expresión $n-r$.
:::

::: {.ma-block .ma-comprobacion}
**Solución**

Las columnas son:

$$
F:
\begin{pmatrix}
-2\\
1\\
1
\end{pmatrix},
\qquad
m:
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix},
$$

$$
a:
\begin{pmatrix}
-2\\
1\\
0
\end{pmatrix},
\qquad
\ell_1:
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix},
\qquad
\ell_2:
\begin{pmatrix}
0\\
1\\
0
\end{pmatrix}.
$$

Por tanto:

$$
A
=
\begin{pmatrix}
-2 & 0 & -2 & 0 & 0\\
1 & 0 & 1 & 1 & 1\\
1 & 1 & 0 & 0 & 0
\end{pmatrix}.
$$

Las columnas de:

$$
m,\quad a,\quad\ell_1
$$

son independientes.

Luego:

$$
\boxed{
r=3.
}
$$

Como:

$$
n=5,
$$

tenemos:

$$
\boxed{
n-r=2.
}
$$

Dos grupos independientes son:

$$
\boxed{
\Pi_1=\frac{F}{ma}
}
$$

y:

$$
\boxed{
\Pi_2=\frac{\ell_1}{\ell_2}.
}
$$

Verificación:

$$
[ma]
=
MLT^{-2}
=
[F],
$$

por lo que:

$$
[\Pi_1]=1.
$$

Además:

$$
[\Pi_2]
=
\frac LL
=
1.
$$

Añadir $\ell_2$ aumenta el número de variables:

$$
4\to5,
$$

pero su columna dimensional es idéntica a la de $\ell_1$.

Por tanto, no añade una nueva dirección dimensional independiente.

El rango permanece:

$$
r=3.
$$

Sin embargo, aparece una nueva razón adimensional:

$$
\frac{\ell_1}{\ell_2}.
$$

Esto muestra el significado de:

$$
\boxed{
n-r:
}
$$

variables adicionales que no aumentan el rango producen nuevas libertades adimensionales.
:::

### 12.19. Autoexplicación

::: {.ma-block .ma-metodo}
**Pausa de autoexplicación**
Responde sin volver a la demostración:

1. ¿por qué un grupo $\Pi$ corresponde a una solución de $A\alpha=0$?;
2. ¿por qué el número de grupos independientes es $n-r$?;
3. ¿por qué los grupos no son únicos?;
4. ¿qué hipótesis física convierte el resultado algebraico en el teorema de Buckingham?;
5. ¿qué información sigue faltando después de escribir

$$
\Phi(\Pi_1,\ldots,\Pi_{n-r})=0?
$$
:::

### 12.20. Variar: cambiar las variables repetidoras

En el ejemplo:

$$
v,\quad L,\quad\rho,\quad\mu,
$$

podemos construir el grupo usando diferentes conjuntos de tres variables repetidoras, siempre que sus columnas dimensionales sean independientes.

Las formas intermedias cambiarán.

El resultado puede aparecer como:

$$
\Pi
=
\frac{\rho vL}{\mu},
$$

o como su inverso:

$$
\Pi^{-1}
=
\frac{\mu}{\rho vL}.
$$

Ambos contienen la misma información.

En general, si:

$$
\widetilde\Pi=\Pi^{-1},
$$

entonces:

$$
\Phi(\Pi)=0
$$

puede reescribirse como otra relación:

$$
\widetilde\Phi(\widetilde\Pi)=0.
$$

La física no depende de nuestra elección particular de coordenadas adimensionales.

### 12.21. Conectar con semejanza

§11 definió semejanza como preservación de las relaciones relevantes y de los parámetros adimensionales que controlan el modelo.

Buckingham explica ahora por qué esos parámetros aparecen.

Si dos sistemas tienen los mismos valores de un conjunto completo de:

$$
\Pi_1,\ldots,\Pi_{n-r},
$$

entonces ocupan el mismo punto en la descripción adimensional del problema.

Bajo las hipótesis del modelo, esto constituye la base algebraica de una comparación por semejanza.

Pero debemos conservar la cautela:

$$
\boxed{
\text{mismos grupos }\Pi
+
\text{mismo modelo}
}
$$

es la afirmación relevante.

Los grupos solos no garantizan que dos sistemas físicos distintos compartan todas las leyes, condiciones de frontera o regímenes necesarios.

### 12.22. Qué hemos ganado

Partimos de una relación con:

$$
n
$$

variables dimensionales.

Buckingham la reorganiza mediante:

$$
n-r
$$

parámetros de dimensión uno.

La reducción puede ser enorme.

Por ejemplo, si:

$$
n=8
$$

y:

$$
r=3,
$$

pasamos conceptualmente de ocho variables dimensionales a:

$$
5
$$

grupos adimensionales.

Esto no resuelve la función física.

Pero reduce el espacio en que debemos:

- experimentar;
- ajustar datos;
- comparar modelos;
- realizar simulaciones;
- buscar semejanzas.

Ésta es una de las razones por las que el análisis dimensional es una herramienta de modelización y no solamente de comprobación de unidades.

### 12.23. Síntesis

El procedimiento completo es:

$$
\boxed{
\text{variables}
\to
\text{firmas}
\to
A
\to
r
\to
A\alpha=0
\to
\Pi_1,\ldots,\Pi_{n-r}.
}
$$

La parte algebraica establece:

$$
\boxed{
\dim(\text{libertad adimensional})
=
n-r
}
$$

en el sentido elemental de:

$$
n-r
$$

variables libres del sistema homogéneo.

La parte física añade invariancia bajo cambios de unidades y permite escribir:

$$
\boxed{
F(q_1,\ldots,q_n)=0
\quad\Longrightarrow\quad
\Phi(\Pi_1,\ldots,\Pi_{n-r})=0.
}
$$

Pero:

$$
\boxed{
\text{Buckingham }\Pi
\not\Rightarrow
\text{función }\Phi\text{ conocida}.
}
$$

El siguiente paso será usar todo el aparato en problemas físicos completos:

$$
\boxed{
\text{§13 — Ejemplos de modelización dimensional}.
}
$$

Allí volveremos al péndulo y añadiremos un segundo caso de semejanza para separar con precisión:

- lo que obliga la dimensión;
- lo que debe aportar la física;
- lo que queda para experimento o teoría.

---

### Notas y fuentes

[^s12-zorich-pi]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §1.3.1, pp. 9–10; §1.3.2, p. 10.
