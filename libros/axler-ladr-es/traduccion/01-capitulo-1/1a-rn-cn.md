# 1A · $\mathbf{R}^n$ y $\mathbf{C}^n$

**Estado:** `COTEJADO`  
**Fuente:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª ed., PDF oficial de 16-08-2026, sección 1A, pp. 2–11.  
**Licencia:** adaptación/traducción no oficial bajo CC BY-NC 4.0.  
**Control de erratas:** la lista oficial de erratas consultada el 13-09-2026 no registra correcciones específicas para la sección 1A.

> [TRAD] Traducción de trabajo de Matemática Abierta. Se preservan la numeración, las fórmulas y la jerarquía del original. Las figuras no se reproducen todavía; se conservan sus referencias y pies pertinentes.

## Números complejos

Ya deberías estar familiarizado con las propiedades básicas del conjunto $\mathbf{R}$ de los números reales. Los números complejos se inventaron para que podamos tomar raíces cuadradas de números negativos. La idea consiste en suponer que tenemos una raíz cuadrada de $-1$, denotada por $i$, que obedece las reglas usuales de la aritmética. Estas son las definiciones formales.

### 1.1 Definición: números complejos, $\mathbf{C}$

- Un **número complejo** es un par ordenado $(a,b)$, donde $a,b\in\mathbf{R}$, pero lo escribiremos como $a+bi$.
- El conjunto de todos los números complejos se denota por $\mathbf{C}$:

$$
\mathbf{C}=\{a+bi:a,b\in\mathbf{R}\}.
$$

- La suma y la multiplicación en $\mathbf{C}$ se definen por

$$
(a+bi)+(c+di)=(a+c)+(b+d)i,
$$

$$
(a+bi)(c+di)=(ac-bd)+(ad+bc)i,
$$

donde $a,b,c,d\in\mathbf{R}$.

Si $a\in\mathbf{R}$, identificamos $a+0i$ con el número real $a$. Así, consideramos $\mathbf{R}$ como un subconjunto de $\mathbf{C}$. Normalmente escribimos $0+bi$ simplemente como $bi$, y $0+1i$ simplemente como $i$.

El símbolo $i$ fue utilizado por primera vez para denotar $\sqrt{-1}$ por Leonhard Euler en 1777.

Para motivar la definición anterior de multiplicación de números complejos, imagina que ya supiéramos que $i^2=-1$ y utiliza las reglas usuales de la aritmética para deducir la fórmula anterior para el producto de dos números complejos. Luego usa esa fórmula para verificar que, en efecto, $i^2=-1$.

No memorices la fórmula del producto de dos números complejos: siempre puedes volver a deducirla recordando que $i^2=-1$ y utilizando después las reglas usuales de la aritmética (dadas en 1.3). El ejemplo siguiente ilustra este procedimiento.

### 1.2 Ejemplo: aritmética compleja

El producto $(2+3i)(4+5i)$ puede calcularse aplicando las propiedades distributiva y conmutativa de 1.3:

$$
\begin{aligned}
(2+3i)(4+5i)
&=2(4+5i)+(3i)(4+5i)\\
&=2\cdot4+2\cdot5i+3i\cdot4+(3i)(5i)\\
&=8+10i+12i-15\\
&=-7+22i.
\end{aligned}
$$

Nuestro primer resultado afirma que la suma y la multiplicación de números complejos tienen las propiedades familiares que esperamos.

### 1.3 Propiedades de la aritmética compleja

**Conmutatividad**

$$
\alpha+\beta=\beta+\alpha
\quad\text{y}\quad
\alpha\beta=\beta\alpha
$$

para todos $\alpha,\beta\in\mathbf{C}$.

**Asociatividad**

$$
(\alpha+\beta)+\lambda=\alpha+(\beta+\lambda)
$$

 y

$$
(\alpha\beta)\lambda=\alpha(\beta\lambda)
$$

para todos $\alpha,\beta,\lambda\in\mathbf{C}$.

**Identidades**

$$
\lambda+0=\lambda
\quad\text{y}\quad
\lambda1=\lambda
$$

para todo $\lambda\in\mathbf{C}$.

**Inverso aditivo**

Para todo $\alpha\in\mathbf{C}$ existe un único $\beta\in\mathbf{C}$ tal que

$$
\alpha+\beta=0.
$$

**Inverso multiplicativo**

Para todo $\alpha\in\mathbf{C}$ con $\alpha\neq0$ existe un único $\beta\in\mathbf{C}$ tal que

$$
\alpha\beta=1.
$$

**Propiedad distributiva**

$$
\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta
$$

para todos $\lambda,\alpha,\beta\in\mathbf{C}$.

Las propiedades anteriores se demuestran utilizando las propiedades familiares de los números reales y las definiciones de suma y multiplicación complejas. El ejemplo siguiente muestra cómo se demuestra la conmutatividad de la multiplicación compleja. Las demostraciones de las demás propiedades se dejan como ejercicios.

### 1.4 Ejemplo: conmutatividad de la multiplicación compleja

Para mostrar que $\alpha\beta=\beta\alpha$ para todos $\alpha,\beta\in\mathbf{C}$, supongamos

$$
\alpha=a+bi
\quad\text{y}\quad
\beta=c+di,
$$

con $a,b,c,d\in\mathbf{R}$. Entonces, por la definición de multiplicación de números complejos,

$$
\alpha\beta=(ac-bd)+(ad+bc)i
$$

mientras que

$$
\beta\alpha=(ca-db)+(cb+da)i.
$$

Estas igualdades, junto con la conmutatividad de la multiplicación y de la suma de números reales, muestran que $\alpha\beta=\beta\alpha$.

A continuación definimos los inversos aditivo y multiplicativo de los números complejos, y luego usamos esos inversos para definir las operaciones de resta y división con números complejos.

### 1.5 Definición: $-\alpha$, resta, $1/\alpha$, división

Supongamos $\alpha,\beta\in\mathbf{C}$.

- Sea $-\alpha$ el inverso aditivo de $\alpha$. Así, $-\alpha$ es el único número complejo tal que

$$
\alpha+(-\alpha)=0.
$$

- La resta en $\mathbf{C}$ se define por

$$
\beta-\alpha=\beta+(-\alpha).
$$

- Para $\alpha\neq0$, sean $1/\alpha$ y $\frac{1}{\alpha}$ notaciones para el inverso multiplicativo de $\alpha$. Así, $1/\alpha$ es el único número complejo tal que

$$
\alpha\left(\frac1\alpha\right)=1.
$$

- Para $\alpha\neq0$, la división por $\alpha$ se define por

$$
\frac{\beta}{\alpha}=\beta\left(\frac1\alpha\right).
$$

Para poder formular cómodamente definiciones y demostrar teoremas que se apliquen tanto a los números reales como a los complejos, adoptamos la siguiente notación.

### 1.6 Notación: $\mathbf{F}$

A lo largo de este libro, $\mathbf{F}$ representa o bien $\mathbf{R}$ o bien $\mathbf{C}$.

La letra $\mathbf{F}$ se utiliza porque $\mathbf{R}$ y $\mathbf{C}$ son ejemplos de lo que en inglés se llaman *fields* (cuerpos). Por tanto, si demostramos un teorema que involucra $\mathbf{F}$, sabremos que es válido cuando $\mathbf{F}$ se reemplaza por $\mathbf{R}$ y cuando se reemplaza por $\mathbf{C}$.

Los elementos de $\mathbf{F}$ se llaman **escalares**. La palabra «escalar» —que no es más que una manera más especializada de decir «número»— suele usarse cuando queremos enfatizar que un objeto es un número, en contraste con un vector (los vectores se definirán pronto).

Para $\alpha\in\mathbf{F}$ y $m$ un entero positivo, definimos $\alpha^m$ como el producto de $\alpha$ consigo mismo $m$ veces:

$$
\alpha^m=\underbrace{\alpha\cdots\alpha}_{m\text{ veces}}.
$$

Esta definición implica que

$$
(\alpha^m)^n=\alpha^{mn}
\quad\text{y}\quad
(\alpha\beta)^m=\alpha^m\beta^m
$$

para todos $\alpha,\beta\in\mathbf{F}$ y todos los enteros positivos $m,n$.

## Listas

Antes de definir $\mathbf{R}^n$ y $\mathbf{C}^n$, veamos dos ejemplos importantes.

### 1.7 Ejemplo: $\mathbf{R}^2$ y $\mathbf{R}^3$

- El conjunto $\mathbf{R}^2$, que puede pensarse como un plano, es el conjunto de todos los pares ordenados de números reales:

$$
\mathbf{R}^2=\{(x,y):x,y\in\mathbf{R}\}.
$$

- El conjunto $\mathbf{R}^3$, que puede pensarse como el espacio usual, es el conjunto de todas las ternas ordenadas de números reales:

$$
\mathbf{R}^3=\{(x,y,z):x,y,z\in\mathbf{R}\}.
$$

Para generalizar $\mathbf{R}^2$ y $\mathbf{R}^3$ a dimensiones superiores, primero necesitamos discutir el concepto de lista.

### 1.8 Definición: lista, longitud

- Supongamos que $n$ es un entero no negativo. Una **lista de longitud $n$** es una colección ordenada de $n$ elementos, que pueden ser números, otras listas u objetos más abstractos.
- Dos listas son iguales si y sólo si tienen la misma longitud y los mismos elementos en el mismo orden.

Muchos matemáticos llaman **$n$-tupla** a una lista de longitud $n$.

Las listas suelen escribirse poniendo sus elementos separados por comas y rodeados por paréntesis. Así, una lista de longitud dos es un par ordenado, que puede escribirse $(a,b)$. Una lista de longitud tres es una terna ordenada, que puede escribirse $(x,y,z)$. Una lista de longitud $n$ puede tener el aspecto

$$
(z_1,\ldots,z_n).
$$

A veces utilizaremos la palabra «lista» sin especificar su longitud. Recuerda, sin embargo, que por definición toda lista tiene longitud finita, dada por un entero no negativo. Por tanto, un objeto que tenga el aspecto $(x_1,x_2,\ldots)$, al que podría atribuirse longitud infinita, no es una lista.

Una lista de longitud $0$ se escribe $(\ )$. Consideramos que tal objeto es una lista para que algunos de nuestros teoremas no tengan excepciones triviales.

Las listas difieren de los conjuntos finitos en dos aspectos: en las listas el orden importa y las repeticiones tienen significado; en los conjuntos, el orden y las repeticiones son irrelevantes.

### 1.9 Ejemplo: listas frente a conjuntos

- Las listas $(3,5)$ y $(5,3)$ no son iguales, pero los conjuntos $\{3,5\}$ y $\{5,3\}$ son iguales.
- Las listas $(4,4)$ y $(4,4,4)$ no son iguales, porque no tienen la misma longitud, aunque los conjuntos $\{4,4\}$ y $\{4,4,4\}$ son ambos iguales al conjunto $\{4\}$.

## $\mathbf{F}^n$

Para definir los análogos de dimensión superior de $\mathbf{R}^2$ y $\mathbf{R}^3$, simplemente reemplazaremos $\mathbf{R}$ por $\mathbf{F}$ —que es $\mathbf{R}$ o $\mathbf{C}$— y reemplazaremos el $2$ o el $3$ por un entero positivo arbitrario.

### 1.10 Notación: $n$

Fijemos un entero positivo $n$ para el resto de este capítulo.

### 1.11 Definición: $\mathbf{F}^n$, coordenada

$\mathbf{F}^n$ es el conjunto de todas las listas de longitud $n$ cuyos elementos pertenecen a $\mathbf{F}$:

$$
\mathbf{F}^n=\{(x_1,\ldots,x_n):x_k\in\mathbf{F}\text{ para }k=1,\ldots,n\}.
$$

Si $(x_1,\ldots,x_n)\in\mathbf{F}^n$ y $k\in\{1,\ldots,n\}$, decimos que $x_k$ es la **$k$-ésima coordenada** de $(x_1,\ldots,x_n)$.

Si $\mathbf{F}=\mathbf{R}$ y $n$ es $2$ o $3$, la definición anterior de $\mathbf{F}^n$ coincide con nuestras nociones previas de $\mathbf{R}^2$ y $\mathbf{R}^3$.

### 1.12 Ejemplo: $\mathbf{C}^4$

$\mathbf{C}^4$ es el conjunto de todas las listas de cuatro números complejos:

$$
\mathbf{C}^4=\{(z_1,z_2,z_3,z_4):z_1,z_2,z_3,z_4\in\mathbf{C}\}.
$$

Lee *Flatland: A Romance of Many Dimensions*, de Edwin A. Abbott, para encontrar una entretenida descripción de cómo $\mathbf{R}^3$ sería percibido por criaturas que vivieran en $\mathbf{R}^2$. Esta novela, publicada en 1884, puede ayudarte a imaginar un espacio físico de cuatro o más dimensiones.

Si $n\ge4$, no podemos visualizar $\mathbf{R}^n$ como un objeto físico. De manera análoga, $\mathbf{C}^1$ puede pensarse como un plano, pero para $n\ge2$ el cerebro humano no puede proporcionar una imagen completa de $\mathbf{C}^n$. Sin embargo, aunque $n$ sea grande, podemos realizar manipulaciones algebraicas en $\mathbf{F}^n$ con la misma facilidad que en $\mathbf{R}^2$ o $\mathbf{R}^3$. Por ejemplo, la suma en $\mathbf{F}^n$ se define del siguiente modo.

### 1.13 Definición: suma en $\mathbf{F}^n$

La suma en $\mathbf{F}^n$ se define sumando las coordenadas correspondientes:

$$
(x_1,\ldots,x_n)+(y_1,\ldots,y_n)
=(x_1+y_1,\ldots,x_n+y_n).
$$

A menudo, la matemática de $\mathbf{F}^n$ se vuelve más limpia si usamos una sola letra para denotar una lista de $n$ números, sin escribir explícitamente las coordenadas. Por ejemplo, el resultado siguiente se formula con $x$ e $y$ en $\mathbf{F}^n$, aunque su demostración requiere la notación más engorrosa $(x_1,\ldots,x_n)$ y $(y_1,\ldots,y_n)$.

### 1.14 Conmutatividad de la suma en $\mathbf{F}^n$

Si $x,y\in\mathbf{F}^n$, entonces

$$
x+y=y+x.
$$

**Demostración.** Supongamos

$$
x=(x_1,\ldots,x_n)\in\mathbf{F}^n
\quad\text{e}\quad
y=(y_1,\ldots,y_n)\in\mathbf{F}^n.
$$

Entonces

$$
\begin{aligned}
x+y
&=(x_1,\ldots,x_n)+(y_1,\ldots,y_n)\\
&=(x_1+y_1,\ldots,x_n+y_n)\\
&=(y_1+x_1,\ldots,y_n+x_n)\\
&=(y_1,\ldots,y_n)+(x_1,\ldots,x_n)\\
&=y+x,
\end{aligned}
$$

donde la segunda y la cuarta igualdad se deben a la definición de suma en $\mathbf{F}^n$, y la tercera a la conmutatividad usual de la suma en $\mathbf{F}$. $\square$

El símbolo $\square$ significa «fin de la demostración». Si se usa una sola letra para denotar un elemento de $\mathbf{F}^n$, suele emplearse la misma letra con subíndices apropiados cuando es necesario mostrar sus coordenadas. Por ejemplo, si $x\in\mathbf{F}^n$, escribir $x=(x_1,\ldots,x_n)$ es una buena notación, como muestra la demostración anterior. Mejor aún: trabaja sólo con $x$ y evita escribir las coordenadas explícitamente cuando sea posible.

### 1.15 Notación: $0$

Sea $0$ la lista de longitud $n$ cuyas coordenadas son todas $0$:

$$
0=(0,\ldots,0).
$$

Aquí utilizamos el símbolo $0$ de dos maneras diferentes: en el lado izquierdo de la igualdad, $0$ denota una lista de longitud $n$, que es un elemento de $\mathbf{F}^n$; en el lado derecho, cada $0$ denota un número. Esta práctica, potencialmente confusa, no causa problemas porque el contexto debería dejar siempre claro qué $0$ se quiere decir.

### 1.16 Ejemplo: el contexto determina qué $0$ se quiere decir

Consideremos el enunciado de que $0$ es una identidad aditiva para $\mathbf{F}^n$:

$$
x+0=x\qquad\text{para todo }x\in\mathbf{F}^n.
$$

Aquí, el $0$ anterior es la lista definida en 1.15, no el número $0$, porque no hemos definido la suma de un elemento de $\mathbf{F}^n$ —a saber, $x$— con el número $0$.

Los elementos de $\mathbf{R}^2$ pueden pensarse como puntos o como vectores. Una figura puede ayudar a nuestra intuición. Dibujaremos figuras en $\mathbf{R}^2$ porque podemos representar este espacio en superficies bidimensionales como el papel o una pantalla. Un elemento típico de $\mathbf{R}^2$ es un punto $v=(a,b)$.

A veces pensamos en $v$ no como un punto sino como una flecha que comienza en el origen y termina en $(a,b)$. Cuando pensamos un elemento de $\mathbf{R}^2$ como una flecha, lo llamamos **vector**.

> [FIGURA] Un vector.

Cuando pensamos en los vectores de $\mathbf{R}^2$ como flechas, podemos trasladar una flecha paralelamente a sí misma —sin cambiar su longitud ni su dirección— y seguir considerándola el mismo vector. Desde este punto de vista, a menudo comprenderás mejor si prescindes de los ejes coordenados y de las coordenadas explícitas y piensas simplemente en el vector. Dos flechas con la misma longitud y la misma dirección representan el mismo vector.

Los modelos matemáticos de la economía pueden tener miles de variables, por ejemplo $x_1,\ldots,x_{5000}$, lo cual significa que debemos trabajar en $\mathbf{R}^{5000}$. Un espacio así no puede abordarse geométricamente. Sin embargo, el enfoque algebraico funciona bien. Por eso nuestra disciplina se llama **álgebra lineal**.

Siempre que utilicemos figuras en $\mathbf{R}^2$ o empleemos el lenguaje algo impreciso de puntos y vectores, recuerda que se trata sólo de ayudas para nuestra comprensión, no de sustitutos de la matemática propiamente dicha que desarrollaremos. Aunque no podamos dibujar buenas figuras en espacios de dimensión alta, los elementos de esos espacios están definidos con tanto rigor como los elementos de $\mathbf{R}^2$.

Por ejemplo,

$$
(2,-3,17,\pi,\sqrt2)
$$

es un elemento de $\mathbf{R}^5$, y podemos referirnos informalmente a él como un punto de $\mathbf{R}^5$ o como un vector de $\mathbf{R}^5$ sin preocuparnos por si la geometría de $\mathbf{R}^5$ tiene algún significado físico.

Recordemos que definimos la suma de dos elementos de $\mathbf{F}^n$ como el elemento de $\mathbf{F}^n$ obtenido sumando las coordenadas correspondientes; véase 1.13. Como veremos ahora, en el caso especial de $\mathbf{R}^2$ la suma tiene una interpretación geométrica sencilla.

Supongamos que tenemos dos vectores $u$ y $v$ en $\mathbf{R}^2$ que queremos sumar. Traslada el vector $v$ paralelamente a sí mismo de modo que su punto inicial coincida con el punto final de $u$. Entonces $u+v$ es el vector cuyo punto inicial coincide con el punto inicial de $u$ y cuyo punto final coincide con el punto final de $v$.

> [FIGURA] La suma de dos vectores.

En la definición siguiente, el $0$ del lado derecho de la igualdad mostrada es la lista $0\in\mathbf{F}^n$.

### 1.17 Definición: inverso aditivo en $\mathbf{F}^n$, $-x$

Para $x\in\mathbf{F}^n$, el **inverso aditivo** de $x$, denotado por $-x$, es el vector $-x\in\mathbf{F}^n$ tal que

$$
x+(-x)=0.
$$

Así, si

$$
x=(x_1,\ldots,x_n),
$$

entonces

$$
-x=(-x_1,\ldots,-x_n).
$$

El inverso aditivo de un vector de $\mathbf{R}^2$ tiene la misma longitud que el vector original, pero apunta en la dirección opuesta.

> [FIGURA] Un vector y su inverso aditivo.

Una vez tratada la suma en $\mathbf{F}^n$, pasemos a la multiplicación. Podríamos definir una multiplicación en $\mathbf{F}^n$ de forma análoga, partiendo de dos elementos de $\mathbf{F}^n$ y obteniendo otro elemento de $\mathbf{F}^n$ al multiplicar coordenadas correspondientes. La experiencia muestra que esta definición no es útil para nuestros propósitos. Otro tipo de multiplicación, llamado **multiplicación por escalares**, será central en nuestro estudio. En concreto, necesitamos definir qué significa multiplicar un elemento de $\mathbf{F}^n$ por un elemento de $\mathbf{F}$.

### 1.18 Definición: multiplicación por escalares en $\mathbf{F}^n$

El producto de un número $\lambda$ y un vector de $\mathbf{F}^n$ se calcula multiplicando cada coordenada del vector por $\lambda$:

$$
\lambda(x_1,\ldots,x_n)
=(\lambda x_1,\ldots,\lambda x_n),
$$

donde $\lambda\in\mathbf{F}$ y $(x_1,\ldots,x_n)\in\mathbf{F}^n$.

La multiplicación por escalares en $\mathbf{F}^n$ multiplica un escalar por un vector y produce un vector. En cambio, el **producto punto** en $\mathbf{R}^2$ o $\mathbf{R}^3$ multiplica dos vectores y produce un escalar. Las generalizaciones del producto punto serán importantes en el capítulo 6.

La multiplicación por escalares tiene una interpretación geométrica sencilla en $\mathbf{R}^2$. Si $\lambda>0$ y $x\in\mathbf{R}^2$, entonces $\lambda x$ es el vector que apunta en la misma dirección que $x$ y cuya longitud es $\lambda$ veces la longitud de $x$. En otras palabras, para obtener $\lambda x$ contraemos o estiramos $x$ por un factor $\lambda$, según si $\lambda<1$ o $\lambda>1$.

Si $\lambda<0$ y $x\in\mathbf{R}^2$, entonces $\lambda x$ es el vector que apunta en la dirección opuesta a $x$ y cuya longitud es $|\lambda|$ veces la longitud de $x$.

> [FIGURA] Multiplicación por escalares.

## Digresión sobre cuerpos

Un **cuerpo** es un conjunto que contiene al menos dos elementos distintos llamados $0$ y $1$, junto con operaciones de suma y multiplicación que satisfacen todas las propiedades enumeradas en 1.3.

Así, $\mathbf{R}$ y $\mathbf{C}$ son cuerpos, al igual que el conjunto de los números racionales con las operaciones usuales de suma y multiplicación. Otro ejemplo de cuerpo es el conjunto $\{0,1\}$ con las operaciones usuales de suma y multiplicación, salvo que $1+1$ se define como $0$.

En este libro no trataremos cuerpos distintos de $\mathbf{R}$ y $\mathbf{C}$. Sin embargo, muchas de las definiciones, teoremas y demostraciones del álgebra lineal que funcionan para los cuerpos $\mathbf{R}$ y $\mathbf{C}$ también funcionan sin cambios para cuerpos arbitrarios.

Si lo prefieres, a lo largo de buena parte de este libro —excepto en los capítulos 6 y 7, dedicados a espacios con producto interno— puedes pensar que $\mathbf{F}$ denota un cuerpo arbitrario en lugar de $\mathbf{R}$ o $\mathbf{C}$. En los resultados —excepto en los capítulos sobre producto interno— que tienen como hipótesis $\mathbf{F}=\mathbf{C}$, probablemente puedas reemplazar esa hipótesis por la de que $\mathbf{F}$ sea un **cuerpo algebraicamente cerrado**, lo cual significa que todo polinomio no constante con coeficientes en $\mathbf{F}$ tiene una raíz. Algunos resultados, como el Ejercicio 13 de la Sección 1C, requieren además la hipótesis $1+1\neq0$ sobre $\mathbf{F}$.

## Ejercicios 1A

1. Demuestra que $\alpha+\beta=\beta+\alpha$ para todos $\alpha,\beta\in\mathbf{C}$.
2. Demuestra que $(\alpha+\beta)+\lambda=\alpha+(\beta+\lambda)$ para todos $\alpha,\beta,\lambda\in\mathbf{C}$.
3. Demuestra que $(\alpha\beta)\lambda=\alpha(\beta\lambda)$ para todos $\alpha,\beta,\lambda\in\mathbf{C}$.
4. Demuestra que $\lambda(\alpha+\beta)=\lambda\alpha+\lambda\beta$ para todos $\lambda,\alpha,\beta\in\mathbf{C}$.
5. Demuestra que para todo $\alpha\in\mathbf{C}$ existe un único $\beta\in\mathbf{C}$ tal que $\alpha+\beta=0$.
6. Demuestra que para todo $\alpha\in\mathbf{C}$ con $\alpha\neq0$ existe un único $\beta\in\mathbf{C}$ tal que $\alpha\beta=1$.
7. Demuestra que

$$
\frac{-1+\sqrt3\,i}{2}
$$

es una raíz cúbica de $1$; es decir, que su cubo es $1$.
8. Encuentra dos raíces cuadradas distintas de $i$.
9. Encuentra $x\in\mathbf{R}^4$ tal que

$$
(4,-3,1,7)+2x=(5,9,-6,8).
$$

10. Explica por qué no existe $\lambda\in\mathbf{C}$ tal que

$$
\lambda(2-3i,5+4i,-6+7i)
=(12-5i,7+22i,-32-9i).
$$

11. Demuestra que $(x+y)+z=x+(y+z)$ para todos $x,y,z\in\mathbf{F}^n$.
12. Demuestra que $(ab)x=a(bx)$ para todo $x\in\mathbf{F}^n$ y todos $a,b\in\mathbf{F}$.
13. Demuestra que $1x=x$ para todo $x\in\mathbf{F}^n$.
14. Demuestra que $\lambda(x+y)=\lambda x+\lambda y$ para todo $\lambda\in\mathbf{F}$ y todos $x,y\in\mathbf{F}^n$.
15. Demuestra que $(a+b)x=ax+bx$ para todos $a,b\in\mathbf{F}$ y todo $x\in\mathbf{F}^n$.

> «¿Sabes sumar?», preguntó la Reina Blanca. «¿Cuánto es uno y uno y uno y uno y uno y uno y uno y uno y uno y uno?»  
> «No lo sé», dijo Alicia. «Perdí la cuenta.»  
> — Lewis Carroll, *Through the Looking-Glass*

---

**Atribución:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª edición. Traducción/adaptación no oficial realizada para Matemática Abierta bajo CC BY-NC 4.0. Fuente oficial: <https://linear.axler.net/>.
