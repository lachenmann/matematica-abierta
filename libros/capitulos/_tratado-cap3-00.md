## 3.0. El problema de la división {#sec-ta-3-0}

El paso de $\mathbb N$ a $\mathbb Z$ resolvió una obstrucción algebraica concreta: la sustracción dejó de ser parcial porque todo entero adquirió un opuesto aditivo. El sistema obtenido sigue teniendo, sin embargo, una limitación igualmente fundamental. Si $a,b\in\mathbb Z$ y $a\neq0_{\mathbb Z}$, la ecuación

$$
ax=b
$$

no tiene por qué poseer una solución entera.

La ecuación

$$
(1_{\mathbb Z}+1_{\mathbb Z})x=1_{\mathbb Z}
$$

es el ejemplo más elemental. Queremos ampliar $\mathbb Z$ a un sistema en el que todo elemento no nulo admita inverso multiplicativo, sin destruir la suma, el producto ni el orden ya construidos.

La idea heurística consiste en representar un cociente mediante un par

$$
(a,b),
\qquad
a,b\in\mathbb Z,
\qquad
b\neq0_{\mathbb Z},
$$

que informalmente pensaríamos como $a/b$. Pero esa escritura todavía no tiene significado formal. Igual que en la construcción de los enteros, distintos pares deben representar el mismo número. La igualdad esperada

$$
\frac ab=\frac cd
$$

se traduce, sin utilizar división, en la condición

$$
ad=bc.
$$

La construcción seguirá la cadena

$$
\mathbb Z
\longrightarrow
\mathbb Z\times\mathbb Z_{\neq0}
\longrightarrow
\text{representantes fraccionarios}
\longrightarrow
\text{equivalencia}
\longrightarrow
\mathbb Q
\longrightarrow
+,-,\cdot,(\ )^{-1},\leq_{\mathbb Q}.
$$

La notación fraccionaria $\frac ab$ sólo se legitimará después de formar el cociente; inmediatamente después se demostrará el criterio de igualdad de clases que permite reconocer cuándo dos de esas escrituras designan el mismo racional. No se utilizará el axioma de elección.

---
