## 8.2. Distancia racional y valor absoluto {#sec-ta-8-2}

La noción de aproximación exige poder expresar cuantitativamente que dos racionales están próximos. No necesitamos introducir una nueva teoría del tamaño: el valor absoluto ya fue construido en Definición 4.2.1 — Valor absoluto para todo cuerpo ordenado, y Proposición 4.1.4 — $\mathbb Q$ es un cuerpo ordenado demuestra que $\mathbb Q$ es un cuerpo ordenado. Por tanto, para todo $q\in\mathbb Q$, la expresión

$$
|q|
$$

está ya legitimada y conserva todas las propiedades demostradas en §4.2.

Lo que necesitamos ahora es convertir ese tamaño de una diferencia en una medida de separación entre dos racionales.

### Definición 8.2.1 — Distancia racional

Definimos la **distancia racional** como la función

$$
\boxed{
d_{\mathbb Q}:\mathbb Q\times\mathbb Q\longrightarrow\mathbb Q
}
$$

dada por

$$
\boxed{
d_{\mathbb Q}(x,y):=|x-y|.
}
$$

La existencia de esta función no se presupone. Su grafo puede escribirse como

$$
G_{d_{\mathbb Q}}
:=
\left\{
\left\langle\langle x,y\rangle,r\right\rangle
\in(\mathbb Q\times\mathbb Q)\times\mathbb Q:
r=|x-y|
\right\}.
$$

El conjunto ambiente existe por Proposición 0.3.7 — Existencia del producto cartesiano, y el subconjunto indicado existe por separación. Para cada $(x,y)\in\mathbb Q\times\mathbb Q$, la sustracción racional determina un único $x-y\in\mathbb Q$, y el valor absoluto determina un único $|x-y|\in\mathbb Q$. Por Definición 0.6.1 — Función como dominio, codominio y grafo, el grafo anterior determina una función con dominio $\mathbb Q\times\mathbb Q$ y codominio $\mathbb Q$.

Aunque el codominio declarado sea $\mathbb Q$, veremos inmediatamente que sus valores son siempre no negativos.

---

### Proposición 8.2.2 — Propiedades fundamentales de la distancia racional

Para cualesquiera $x,y,z\in\mathbb Q$:

1. **no negatividad**:
   $$
   0\leq d_{\mathbb Q}(x,y);
   $$
2. **separación de puntos**:
   $$
   d_{\mathbb Q}(x,y)=0
   \iff
   x=y;
   $$
3. **simetría**:
   $$
   d_{\mathbb Q}(x,y)=d_{\mathbb Q}(y,x);
   $$
4. **desigualdad triangular**:
   $$
   d_{\mathbb Q}(x,z)
   \leq
   d_{\mathbb Q}(x,y)+d_{\mathbb Q}(y,z);
   $$
5. **invariancia por traslación**:
   $$
   d_{\mathbb Q}(x+z,y+z)
   =
   d_{\mathbb Q}(x,y).
   $$

**Demostración.**

La no negatividad es Proposición 4.2.2 — Propiedades elementales del valor absoluto (1) aplicada a $x-y$:

$$
d_{\mathbb Q}(x,y)=|x-y|\geq0.
$$

Para la separación de puntos, Proposición 4.2.2 — Propiedades elementales del valor absoluto (2) da

$$
|x-y|=0
\iff
x-y=0.
$$

Por las leyes del grupo aditivo racional (Proposición 3.3.8 — Leyes del grupo aditivo racional),

$$
x-y=0
\iff
x=y.
$$

Luego

$$
d_{\mathbb Q}(x,y)=0
\iff
x=y.
$$

Para la simetría, las leyes aditivas dan

$$
x-y=-(y-x),
$$

y Proposición 4.2.2 — Propiedades elementales del valor absoluto (3) implica

$$
|x-y|
=
|-(y-x)|
=
|y-x|.
$$

Por tanto

$$
d_{\mathbb Q}(x,y)=d_{\mathbb Q}(y,x).
$$

Para la desigualdad triangular, observamos que

$$
x-z=(x-y)+(y-z).
$$

Aplicando Teorema 4.2.3 — Desigualdad triangular,

$$
|x-z|
\leq
|x-y|+|y-z|,
$$

es decir,

$$
d_{\mathbb Q}(x,z)
\leq
 d_{\mathbb Q}(x,y)+d_{\mathbb Q}(y,z).
$$

Finalmente,

$$
(x+z)-(y+z)=x-y
$$

por las leyes del grupo aditivo. En consecuencia,

$$
d_{\mathbb Q}(x+z,y+z)
=
|(x+z)-(y+z)|
=
|x-y|
=
d_{\mathbb Q}(x,y).
$$

Quedan demostradas las cinco propiedades. ∎

> **Nota conceptual.** Las cuatro primeras propiedades son precisamente las que más adelante permitirían reconocer a $d_{\mathbb Q}$ como una métrica. No necesitamos todavía desarrollar la teoría abstracta de espacios métricos; para la construcción de Cauchy basta trabajar directamente con estas propiedades racionales.

---

### Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional

Sean $x,y,\varepsilon\in\mathbb Q$ con

$$
0<\varepsilon.
$$

Entonces son equivalentes las condiciones

$$
\boxed{
d_{\mathbb Q}(x,y)<\varepsilon,
}
$$

$$
\boxed{
-\varepsilon<x-y<\varepsilon,
}
$$

y

$$
\boxed{
y-\varepsilon<x<y+\varepsilon.
}
$$

**Demostración.**

Escribamos

$$
t:=x-y.
$$

Supongamos primero

$$
|t|<\varepsilon.
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto (4),

$$
-|t|\leq t\leq|t|.
$$

De $|t|<\varepsilon$, al invertir el orden mediante opuestos, obtenemos

$$
-\varepsilon<-|t|.
$$

Por transitividad,

$$
-\varepsilon<t<\varepsilon.
$$

Recíprocamente, supongamos

$$
-\varepsilon<t<\varepsilon.
$$

Por totalidad del orden, $0\leq t$ o $t<0$.

Si $0\leq t$, la definición de valor absoluto da $|t|=t$, y por hipótesis

$$
|t|=t<\varepsilon.
$$

Si $t<0$, entonces $|t|=-t$. De

$$
-\varepsilon<t
$$

sumamos $\varepsilon-t$ a ambos lados, usando la invariancia estricta por traslación de Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (8), y obtenemos

$$
-t<\varepsilon.
$$

Por tanto también en este caso

$$
|t|<\varepsilon.
$$

Hemos demostrado

$$
|x-y|<\varepsilon
\iff
-\varepsilon<x-y<\varepsilon.
$$

Finalmente, por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (8), sumar $y$ en cada desigualdad produce

$$
-\varepsilon<x-y
\iff
y-\varepsilon<x,
$$

y

$$
x-y<\varepsilon
\iff
x<y+\varepsilon.
$$

Así

$$
-\varepsilon<x-y<\varepsilon
\iff
y-\varepsilon<x<y+\varepsilon.
$$

Las tres condiciones son equivalentes. ∎

---

### Lo que hemos ganado

La frase informal “$x$ está cerca de $y$” dispone ahora de una formulación enteramente racional:

$$
d_{\mathbb Q}(x,y)<\varepsilon.
$$

Además, esta condición puede leerse de dos maneras equivalentes:

$$
|x-y|<\varepsilon
$$

como control de una diferencia, o

$$
y-\varepsilon<x<y+\varepsilon
$$

como pertenencia a una ventana racional centrada en $y$.

Con esto ya tenemos el lenguaje necesario para formular rigurosamente qué significa que los términos de una sucesión se acerquen a un racional.

---
