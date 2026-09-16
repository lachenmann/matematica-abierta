## §12 — El teorema Π de Buckingham {#fpm-i-02-s12}

### 12.1. Intuir: muchas variables, pocas combinaciones esenciales

Supongamos que un fenómeno se describe mediante

$$
q_1,q_2,\ldots,q_n.
$$

Cada variable puede tener unidades y dimensiones distintas.

A primera vista, una relación

$$
F(q_1,\ldots,q_n)=0
$$

parece depender de las $n$ variables por separado.

Sin embargo, §§8–11 nos han mostrado algo importante:

- las combinaciones de dimensión uno sobreviven al cambio de unidades;
- esas combinaciones pueden funcionar como invariantes de semejanza;
- una libertad adimensional contiene precisamente información que las dimensiones no fijan.

La pregunta natural es:

$$
\boxed{
\text{¿cuántas combinaciones adimensionales independientes podemos construir?}
}
$$

El teorema $\Pi$ de Buckingham responde, bajo hipótesis precisas:[^s12-zorich-pi]

$$
\boxed{
n-r,
}
$$

donde $r$ es el **rango dimensional** de las variables.

La clave está en entender qué significa ese rango.

### 12.2. Representar: columnas de exponentes dimensionales

Fijemos un orden de dimensiones base relevantes:

$$
D_1,\ldots,D_d.
$$

Para cada variable $q_i$, escribimos

$$
[q_i]
=
D_1^{a_{1i}}
D_2^{a_{2i}}
\cdots
D_d^{a_{di}}.
$$

La firma dimensional de $q_i$ es la columna

$$
\mathbf a_i
=
\begin{pmatrix}
a_{1i}\\
a_{2i}\\
\vdots\\
a_{di}
\end{pmatrix}.
$$

Colocamos todas las columnas juntas:

$$
A
=
\begin{pmatrix}
| & | & & |\\
\mathbf a_1 & \mathbf a_2 & \cdots & \mathbf a_n\\
| & | & & |
\end{pmatrix}.
$$

::: {.ma-block .ma-definicion}
**Definición 29 — Matriz dimensional**
La **matriz dimensional** de las variables $q_1,\ldots,q_n$, respecto de una lista ordenada de dimensiones base, es la matriz cuyas columnas son sus firmas dimensionales.
:::

La matriz dimensional no contiene los valores de las variables.

Contiene solamente sus exponentes dimensionales.

### 12.3. Rango dimensional sin presuponer álgebra lineal avanzada

Aplicamos eliminación gaussiana a $A$.

El número de columnas pivote —equivalentemente, el número de filas no nulas de una forma escalonada— mide cuántas direcciones dimensionales independientes aparecen realmente entre las variables.

::: {.ma-block .ma-definicion}
**Definición 30 — Rango dimensional**
El **rango dimensional** de un conjunto de variables es el rango $r$ de su matriz dimensional, calculado por eliminación gaussiana. Es el número de restricciones dimensionales independientes que intervienen en el problema.
:::

Siempre:

$$
r\le d
$$

y

$$
r\le n.
$$

El número relevante en Buckingham no es simplemente «cuántos símbolos $M,L,T,\ldots$ vemos».

Es el número de combinaciones dimensionales **independientes**.

::: {.ma-block .ma-metodo}
**Principio 23 — La cuenta de Buckingham usa rango, no conteo superficial de dimensiones**
Para determinar el número de grupos adimensionales independientes debemos calcular el rango de la matriz de exponentes. Contar símbolos dimensionales sin verificar su independencia puede producir una cuenta incorrecta.
:::

### 12.4. Un monomio es adimensional exactamente cuando resuelve un sistema homogéneo

Consideremos un producto de potencias:

$$
\Pi
=
q_1^{\alpha_1}
q_2^{\alpha_2}
\cdots
q_n^{\alpha_n}.
$$

Su firma dimensional es

$$
\mathbf d(\Pi)
=
\alpha_1\mathbf a_1
+
\cdots+
\alpha_n\mathbf a_n.
$$

En forma matricial:

$$
\mathbf d(\Pi)
=
A\alpha,
$$

donde

$$
\alpha
=
\begin{pmatrix}
\alpha_1\\
\vdots\\
\alpha_n
\end{pmatrix}.
$$

Por tanto:

$$
[\Pi]=1
$$

si y solo si

$$
\boxed{
A\alpha=0.
}
$$

Así, construir combinaciones adimensionales equivale a resolver un sistema lineal homogéneo.

### 12.5. ¿Por qué aparecen $n-r$ parámetros libres?

Sea $A$ una matriz con $n$ columnas y rango $r$.

Al reducir

$$
A\alpha=0
$$

por eliminación gaussiana, aparecen:

- $r$ variables pivote;
- $n-r$ variables libres.

Cada elección independiente de las variables libres produce una solución del sistema.

Por tanto, el conjunto de exponentes que generan monomios adimensionales posee

$$
\boxed{
n-r
}
$$

grados de libertad independientes.

Éste es el núcleo algebraico de la cuenta de Buckingham.

No necesitamos todavía una teoría abstracta del espacio nulo.

Basta la lógica de los sistemas lineales:

$$
\boxed{
n\text{ incógnitas}
-
r\text{ pivotes}
=
n-r\text{ variables libres}.
}
$$

### 12.6. Grupo Π

::: {.ma-block .ma-definicion}
**Definición 31 — Grupo $\Pi$**
Un **grupo $\Pi$** es una combinación monomial de las variables pertinentes,

$$
\Pi
=
\prod_{i=1}^nq_i^{\alpha_i},
$$

cuya dimensión es uno:

$$
[\Pi]=1.
$$

Un conjunto de grupos $\Pi_1,\ldots,\Pi_k$ será llamado **independiente** cuando ninguno pueda obtenerse como producto de potencias de los demás.
:::

Esta independencia es multiplicativa.

Al pasar a los vectores de exponentes, se convierte en la independencia ordinaria de soluciones de

$$
A\alpha=0.
$$

### 12.7. Variables repetidoras

Si

$$
\operatorname{rank}A=r,
$$

podemos escoger $r$ columnas independientes.

Después de reordenar variables, llamémoslas:

$$
q_1,\ldots,q_r.
$$

La submatriz formada por esas columnas será:

$$
B.
$$

Como las columnas son independientes, $B$ posee rango de columnas $r$. En general $B$ es una matriz $d\times r$ y no tiene por qué ser cuadrada. Lo que necesitaremos es que sus columnas formen una base del espacio generado por todas las columnas de $A$.

Llamaremos a

$$
q_1,\ldots,q_r
$$

**variables repetidoras**.

No porque aparezcan físicamente «más veces», sino porque se reutilizan para construir cada grupo adimensional.

### 12.8. Construcción de los grupos

Tomemos una variable no repetidora:

$$
q_{r+k}.
$$

Buscamos un grupo de la forma

$$
\Pi_k
=
q_{r+k}
q_1^{c_{1k}}
\cdots
q_r^{c_{rk}}.
$$

Queremos:

$$
[\Pi_k]=1.
$$

Si

$$
\mathbf a_{r+k}
$$

es la columna dimensional de $q_{r+k}$, la condición es:

$$
Bc^{(k)}
+
\mathbf a_{r+k}
=
0,
$$

donde

$$
c^{(k)}
=
\begin{pmatrix}
c_{1k}\\
\vdots\\
c_{rk}
\end{pmatrix}.
$$

Como cada columna de $A$ pertenece al espacio generado por las columnas independientes de $B$, existe una solución de

$$
Bc^{(k)}
=
-\mathbf a_{r+k}.
$$

Esa solución es única porque las columnas de $B$ son independientes: si

$$
Bc=Bc',
$$

entonces

$$
B(c-c')=0,
$$

y la independencia obliga a

$$
c=c'.
$$

No escribiremos $B^{-1}$, porque $B$ puede ser rectangular cuando el número de dimensiones base $d$ es mayor que el rango $r$. En la práctica resolveremos el sistema por eliminación.

Como existen

$$
n-r
$$

variables no repetidoras, esta construcción produce

$$
\Pi_1,\ldots,\Pi_{n-r}.
$$

### 12.9. Por qué esos grupos son independientes

Cada grupo construido tiene exponente $1$ en una variable no repetidora distinta:

$$
\Pi_k
=
q_{r+k}
\times
\text{potencias de las variables repetidoras}.
$$

Supongamos que

$$
\Pi_1^{\lambda_1}
\cdots
\Pi_{n-r}^{\lambda_{n-r}}
=
1
$$

como identidad monomial.

Miremos el exponente de

$$
q_{r+k}.
$$

Esa variable aparece con exponente $\lambda_k$ y no aparece en los otros grupos.

Por tanto:

$$
\lambda_k=0.
$$

Esto vale para todo $k$.

Luego los grupos son independientes.

### 12.10. Por qué generan todos los monomios adimensionales

Sea

$$
\Pi
=
q_1^{\alpha_1}\cdots q_n^{\alpha_n}
$$

cualquier monomio adimensional.

Queremos mostrar que se obtiene a partir de los grupos construidos.

Formemos:

$$
\widetilde\Pi
=
\Pi
\Pi_1^{-\alpha_{r+1}}
\cdots
\Pi_{n-r}^{-\alpha_n}.
$$

Por construcción, se cancelan todos los exponentes de las variables no repetidoras.

Por tanto,

$$
\widetilde\Pi
=
q_1^{\beta_1}\cdots q_r^{\beta_r}.
$$

Además, $\widetilde\Pi$ sigue siendo adimensional porque es producto y cociente de cantidades de dimensión uno.

Entonces:

$$
B\beta=0.
$$

Pero las columnas de $B$ son independientes.

La única solución es:

$$
\beta=0.
$$

Por tanto:

$$
\widetilde\Pi=1.
$$

Luego:

$$
\boxed{
\Pi
=
\Pi_1^{\alpha_{r+1}}
\cdots
\Pi_{n-r}^{\alpha_n}.
}
$$

Toda combinación monomial adimensional se genera mediante los

$$
n-r
$$

grupos construidos.

### 12.11. La parte física: invariancia frente a cambios de unidades

Hasta aquí hemos probado un hecho algebraico.

Para llegar al teorema de Buckingham debemos añadir una hipótesis física:

> la relación entre las cantidades no debe depender de la elección arbitraria de las unidades base.

Supongamos:

$$
F(q_1,\ldots,q_n)=0.
$$

Cambiamos independientemente las unidades base.

Los valores numéricos de los $q_i$ cambian según sus firmas dimensionales.

La relación física, sin embargo, debe describir la misma situación.

Por tanto, debe ser constante a lo largo de las transformaciones numéricas inducidas únicamente por cambios de unidades.

Los grupos $\Pi_k$, al ser adimensionales, permanecen invariantes bajo esas transformaciones.

La información que sobrevive al cambio de unidades puede organizarse entonces mediante ellos.

### 12.12. Normalizar las variables repetidoras

Hay una forma concreta de verlo.

Trabajemos con valores positivos para poder usar logaritmos y potencias reales sin discutir signos.

Queremos cambiar las unidades base de modo que los valores numéricos de las $r$ variables repetidoras adopten valores de referencia, por ejemplo:

$$
1,\ldots,1.
$$

Sea

$$
u=
\begin{pmatrix}
\log\lambda_1\\
\vdots\\
\log\lambda_d
\end{pmatrix}
$$

el vector de logaritmos de los factores de reescalado de las $d$ unidades base.

Si

$$
b=
\begin{pmatrix}
\log q_1\\
\vdots\\
\log q_r
\end{pmatrix}
$$

contiene los logaritmos de los valores numéricos de las variables repetidoras, la condición de llevar esos valores a $1$ se escribe:

$$
B^{\mathsf T}u=b.
$$

Como $B$ tiene rango de columnas $r$, la matriz $B^{\mathsf T}$ tiene rango de filas $r$. Por tanto, el sistema es compatible para todo $b$.

Si $d>r$, la solución $u$ no tiene por qué ser única: quedan cambios de unidades que no afectan a las variables repetidoras. Esa no unicidad es irrelevante para la reducción, porque basta con que exista una normalización.

Después de esta normalización:

- las variables repetidoras ya no aportan parámetros numéricos libres;
- los valores normalizados de las variables restantes quedan representados por combinaciones adimensionales equivalentes a los grupos $\Pi_k$.

Por tanto, una relación invariante bajo cambios de unidades puede describirse únicamente mediante esos invariantes.

### 12.13. Teorema Π de Buckingham

::: {.ma-block .ma-enunciado}
**Teorema 5 — $\Pi$ de Buckingham, forma elemental**

Sean

$$
q_1,\ldots,q_n>0
$$

variables físicas pertinentes, y sea $A$ su matriz dimensional, de rango

$$
r.
$$

Supongamos que:

1. las dimensiones de las variables están expresadas respecto de un sistema fijo de dimensiones base;
2. la relación física

$$
F(q_1,\ldots,q_n)=0
$$

es independiente de la elección multiplicativa de las unidades base;
3. el conjunto de variables es el declarado por el modelo y la relación se considera en una región positiva donde las potencias reales utilizadas están bien definidas.

Entonces pueden construirse

$$
\boxed{
n-r
}
$$

grupos adimensionales independientes

$$
\Pi_1,\ldots,\Pi_{n-r},
$$

tales que:

1. toda combinación monomial adimensional de las $q_i$ es producto de potencias de esos grupos;
2. la relación física puede reescribirse en la forma

$$
\boxed{
\Phi(\Pi_1,\ldots,\Pi_{n-r})=0
}
$$

para alguna función $\Phi$.
:::

#### Demostración

Como

$$
\operatorname{rank}A=r,
$$

elegimos $r$ columnas independientes y, reordenando las variables si es necesario, las llamamos

$$
q_1,\ldots,q_r.
$$

Para cada una de las

$$
n-r
$$

variables restantes construimos:

$$
\Pi_k
=
q_{r+k}
q_1^{c_{1k}}
\cdots
q_r^{c_{rk}},
$$

eligiendo los exponentes mediante:

$$
Bc^{(k)}
=
-\mathbf a_{r+k}.
$$

Esto es posible porque las columnas de $B$ generan el espacio de columnas de $A$, y determina de manera única cada $c^{(k)}$ porque esas columnas son independientes.

Así:

$$
[\Pi_k]=1.
$$

Los grupos son independientes porque cada uno contiene una variable no repetidora distinta con exponente $1$.

La argumentación de §12.10 muestra además que cualquier otro monomio adimensional es un producto de potencias de estos grupos.

Queda demostrar la reducción funcional.

Por invariancia frente al cambio de unidades, podemos reescalar las unidades base sin cambiar el contenido físico de la relación.

Como las variables repetidoras tienen firmas independientes, el sistema

$$
B^{\mathsf T}u=b
$$

tiene solución para cualquier vector de valores positivos que queramos normalizar. Por ello podemos elegir un cambio de unidades que lleve sus valores numéricos a valores fijos.

Una vez fijados esos $r$ valores, los únicos parámetros numéricos libres que sobreviven a la normalización son los valores de las

$$
n-r
$$

combinaciones adimensionales.

Por tanto, la validez de la relación depende solamente de:

$$
\Pi_1,\ldots,\Pi_{n-r}.
$$

Existe entonces una función $\Phi$ tal que:

$$
\Phi(\Pi_1,\ldots,\Pi_{n-r})=0.
$$

Así queda demostrada la forma elemental del teorema.

$$
\boxed{\text{QED}}
$$

### 12.14. Qué significa exactamente $n-r$

La fórmula:

$$
n-r
$$

no significa:

> «el problema físico ha quedado completamente resuelto».

Significa:

> la dependencia de unidades permite reducir una relación entre $n$ variables a una relación entre $n-r$ parámetros adimensionales independientes.

Todavía queda por determinar:

$$
\Phi.
$$

Esa función puede requerir:

- teoría física;
- ecuaciones diferenciales;
- experimentos;
- simulaciones;
- datos;
- aproximaciones adicionales.

::: {.ma-block .ma-metodo}
**Principio 24 — Buckingham reduce variables, no determina la función adimensional**
El teorema $\Pi$ identifica una representación mediante parámetros adimensionales, pero no determina en general la función que relaciona esos parámetros.
:::
