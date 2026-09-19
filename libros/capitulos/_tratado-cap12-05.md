## 12.5. Preservación del orden {#sec-ta-12-5}

La construcción de §12.4 produjo, para dos completaciones ordenadas $(E,\iota_E)$ y $(F,\iota_F)$, una función

$$
\Psi_{E,F}:E\longrightarrow F
$$

que reconstruye exactamente la misma traza racional:

$$
L_F\bigl(\Psi_{E,F}(x)\bigr)=L_E(x).
$$

Para convertir esta identidad en una afirmación sobre el orden debemos demostrar primero que la traza racional inferior determina por completo la posición de un elemento. El hecho decisivo vuelve a ser la densidad de la copia racional: si dos elementos están ordenados de manera distinta, algún racional canónico queda entre ellos y detecta esa diferencia en sus trazas.

### Proposición 12.5.1 — La inclusión de trazas racionales caracteriza el orden

Sea $E$ un cuerpo ordenado arquimediano. Para todos $x,y\in E$,

$$
\boxed{
x\le y
\iff
L_E(x)\subseteq L_E(y).
}
$$

Además,

$$
\boxed{
x<y
\iff
L_E(x)\subsetneq L_E(y).
}
$$

**Demostración.**

Supongamos primero

$$
x\le y.
$$

Sea $q\in L_E(x)$. Por Definición 12.4.1 — Traza racional inferior de un elemento,

$$
\jmath_{\mathbb Q}^{E}(q)<x.
$$

Como $x\le y$, la transitividad mixta del orden da

$$
\jmath_{\mathbb Q}^{E}(q)<y.
$$

Por tanto $q\in L_E(y)$. Hemos probado

$$
L_E(x)\subseteq L_E(y).
$$

Para la implicación inversa, supongamos

$$
L_E(x)\subseteq L_E(y)
$$

y neguemos $x\le y$. Como el orden de $E$ es total, resulta

$$
y<x.
$$

Por la densidad de la copia racional canónica Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano, existe $q\in\mathbb Q$ tal que

$$
y
<
\jmath_{\mathbb Q}^{E}(q)
<
x.
$$

La desigualdad de la derecha implica

$$
q\in L_E(x),
$$

y, por la inclusión supuesta,

$$
q\in L_E(y).
$$

Pero esta última pertenencia significa

$$
\jmath_{\mathbb Q}^{E}(q)<y,
$$

lo cual contradice $y<\jmath_{\mathbb Q}^{E}(q)$. Luego necesariamente

$$
x\le y.
$$

Queda la equivalencia estricta. Supongamos $x<y$. La equivalencia no estricta ya probada da

$$
L_E(x)\subseteq L_E(y).
$$

Aplicando de nuevo Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano, existe $q\in\mathbb Q$ con

$$
x
<
\jmath_{\mathbb Q}^{E}(q)
<
y.
$$

Entonces

$$
q\in L_E(y).
$$

En cambio $q\notin L_E(x)$: si perteneciera, tendríamos

$$
\jmath_{\mathbb Q}^{E}(q)<x,
$$

contradiciendo $x<\jmath_{\mathbb Q}^{E}(q)$. Así,

$$
L_E(x)\subsetneq L_E(y).
$$

Recíprocamente, si

$$
L_E(x)\subsetneq L_E(y),
$$

entonces la primera equivalencia da $x\le y$. Además $x\neq y$, pues de $x=y$ se seguiría inmediatamente

$$
L_E(x)=L_E(y),
$$

contradiciendo la inclusión propia. Por la definición del orden estricto asociado,

$$
x<y.
$$

Quedan demostradas ambas equivalencias. ∎

La proposición permite leer el orden del cuerpo directamente en $\mathcal P(\mathbb Q)$. Dos elementos tienen la misma posición ordenada exactamente cuando sus lados racionales inferiores coinciden; y avanzar estrictamente en el cuerpo equivale a ampliar estrictamente la traza.

### Teorema 12.5.2 — El transporte preserva y refleja el orden

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Para todos $x,y\in E$,

$$
\boxed{
x\le y
\iff
\Psi_{E,F}(x)\le\Psi_{E,F}(y).
}
$$

Asimismo,

$$
\boxed{
x<y
\iff
\Psi_{E,F}(x)<\Psi_{E,F}(y).
}
$$

En particular, $\Psi_{E,F}$ es inyectiva.

**Demostración.**

Como $E$ y $F$ son completos, Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano implica que ambos son arquimedianos. Podemos aplicar Proposición 12.5.1 — La inclusión de trazas racionales caracteriza el orden en los dos cuerpos.

Para el orden no estricto,

$$
\begin{aligned}
x\le y
&\iff L_E(x)\subseteq L_E(y)\\
&\iff L_F\bigl(\Psi_{E,F}(x)\bigr)
      \subseteq
      L_F\bigl(\Psi_{E,F}(y)\bigr)\\
&\iff \Psi_{E,F}(x)\le\Psi_{E,F}(y).
\end{aligned}
$$

La equivalencia central utiliza dos veces Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional.

Del mismo modo, para el orden estricto,

$$
\begin{aligned}
x<y
&\iff L_E(x)\subsetneq L_E(y)\\
&\iff L_F\bigl(\Psi_{E,F}(x)\bigr)
      \subsetneq
      L_F\bigl(\Psi_{E,F}(y)\bigr)\\
&\iff \Psi_{E,F}(x)<\Psi_{E,F}(y).
\end{aligned}
$$

Resta la inyectividad. Supongamos

$$
\Psi_{E,F}(x)=\Psi_{E,F}(y).
$$

Entonces, en particular,

$$
\Psi_{E,F}(x)\le\Psi_{E,F}(y)
\qquad\text{y}\qquad
\Psi_{E,F}(y)\le\Psi_{E,F}(x).
$$

Reflejando ambas desigualdades mediante la equivalencia ya probada,

$$
x\le y
\qquad\text{y}\qquad
y\le x.
$$

La antisimetría del orden de $E$ da $x=y$. Por tanto $\Psi_{E,F}$ es inyectiva. ∎

El teorema ya muestra que $\Psi_{E,F}$ no deforma la recta ordenada: preserva y refleja exactamente todas las comparaciones. Falta comprobar que ningún elemento de $F$ queda fuera de su imagen. Para ello no necesitaremos buscar una preimagen; la construcción realizada con los cuerpos intercambiados proporciona una función canónica en sentido contrario.

### Corolario 12.5.3 — Los transportes simétricos son inversos

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Entonces, para todo $x\in E$ y todo $y\in F$,

$$
\boxed{
\Psi_{F,E}\bigl(\Psi_{E,F}(x)\bigr)=x,
}
$$

$$
\boxed{
\Psi_{E,F}\bigl(\Psi_{F,E}(y)\bigr)=y.
}
$$

En consecuencia,

$$
\boxed{
\Psi_{E,F}:E\longrightarrow F
\text{ es biyectiva},
}
$$

y su función inversa es exactamente

$$
\boxed{
\Psi_{E,F}^{-1}=\Psi_{F,E}.
}
$$

**Demostración.**

Fijemos $x\in E$. Aplicando Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional primero al transporte de $F$ hacia $E$ y después al transporte de $E$ hacia $F$, obtenemos

$$
\begin{aligned}
L_E\!\left(
\Psi_{F,E}\bigl(\Psi_{E,F}(x)\bigr)
\right)
&=
L_F\bigl(\Psi_{E,F}(x)\bigr)\\
&=
L_E(x).
\end{aligned}
$$

Como $E$ es completo, Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano lo hace arquimediano. La igualdad de trazas implica ambas inclusiones y Proposición 12.5.1 — La inclusión de trazas racionales caracteriza el orden las traduce en

$$
\Psi_{F,E}\bigl(\Psi_{E,F}(x)\bigr)\le x
$$

y

$$
x\le\Psi_{F,E}\bigl(\Psi_{E,F}(x)\bigr).
$$

Por antisimetría,

$$
\Psi_{F,E}\bigl(\Psi_{E,F}(x)\bigr)=x.
$$

El mismo argumento, intercambiando $E$ y $F$, da para todo $y\in F$

$$
\Psi_{E,F}\bigl(\Psi_{F,E}(y)\bigr)=y.
$$

Así $\Psi_{F,E}$ es simultáneamente inversa por la izquierda y por la derecha de $\Psi_{E,F}$. Por Teorema 0.6.7 — Caracterización de las funciones invertibles, $\Psi_{E,F}$ es biyectiva, y la notación de función inversa activada en Notación 0.6.8 — Función inversa permite escribir

$$
\Psi_{E,F}^{-1}=\Psi_{F,E}.
$$

∎

Con esto, $\Psi_{E,F}$ es ya un **isomorfismo de órdenes** entre las dos completaciones. La construcción depende únicamente de sus trazas racionales y la función inversa no requiere una definición adicional: es el mismo transporte con los cuerpos intercambiados.

Aún no hemos demostrado que este isomorfismo de órdenes sea un isomorfismo de cuerpos. Ése será el trabajo de §12.6: probar que el transporte respeta primero la suma y los elementos distinguidos, y después el producto y los inversos, utilizando la caracterización racional de cada operación.
