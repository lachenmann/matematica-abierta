## 12.6. Preservación de las operaciones {#sec-ta-12-6}

La sección anterior estableció que

$$
\Psi_{E,F}:E\longrightarrow F
$$

es una biyección que preserva y refleja exactamente el orden. Falta demostrar que la reconstrucción por trazas racionales conserva también la estructura algebraica.

No introduciremos una segunda construcción del transporte ni apelaremos a la unicidad que corresponde a §12.7. La idea será más interna. Las operaciones de un cuerpo ordenado completo pueden leerse a partir de la posición de sus resultados respecto de la copia racional densa. Si dos elementos poseen la misma traza racional inferior, §12.5 ya nos permite concluir que son iguales.

Comenzaremos verificando que el transporte fija la copia racional canónica. Después describiremos la traza de una suma exclusivamente mediante las trazas de los sumandos. Para el producto será necesario aislar primero el cono no negativo, donde la multiplicación es monótona; los signos permitirán extender luego el resultado a todo el cuerpo.

---

### Lema 12.6.1 — Traza de un racional canónico

Sea $G$ un cuerpo ordenado y sea $q\in\mathbb Q$. Entonces

$$
\boxed{
L_G\bigl(\jmath_{\mathbb Q}^{G}(q)\bigr)=\delta_q.
}
$$

**Demostración.**

Sea $r\in\mathbb Q$. Por Definición 12.4.1 — Traza racional inferior de un elemento,

$$
r\in L_G\bigl(\jmath_{\mathbb Q}^{G}(q)\bigr)
\iff
\jmath_{\mathbb Q}^{G}(r)
<
\jmath_{\mathbb Q}^{G}(q).
$$

Como Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados afirma que la copia racional preserva y refleja el orden estricto,

$$
\jmath_{\mathbb Q}^{G}(r)
<
\jmath_{\mathbb Q}^{G}(q)
\iff
r<q.
$$

Finalmente, por Definición 5.2.1 — Sección inferior determinada por un racional,

$$
r<q
\iff
r\in\delta_q.
$$

Así ambos subconjuntos de $\mathbb Q$ poseen exactamente los mismos elementos. Por extensionalidad (Teorema 0.2.4 — Criterio extensional por doble inclusión),

$$
L_G\bigl(\jmath_{\mathbb Q}^{G}(q)\bigr)=\delta_q.
$$

∎

El lema identifica la traza, no los objetos. El racional $q$, su imagen $\jmath_{\mathbb Q}^{G}(q)$ y la cortadura $\delta_q$ siguen perteneciendo a tipos distintos.

---

### Proposición 12.6.2 — El transporte fija la copia racional canónica

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Para todo $q\in\mathbb Q$,

$$
\boxed{
\Psi_{E,F}\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
=
\jmath_{\mathbb Q}^{F}(q).
}
$$

Equivalentemente,

$$
\boxed{
\Psi_{E,F}\circ\iota_E=\iota_F.
}
$$

**Demostración.**

Fijemos $q\in\mathbb Q$. Por Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional,

$$
L_F\!\left(
\Psi_{E,F}\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
\right)
=
L_E\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr).
$$

Aplicando Lema 12.6.1 — Traza de un racional canónico primero en $E$ y después en $F$,

$$
L_E\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
=
\delta_q
=
L_F\bigl(\jmath_{\mathbb Q}^{F}(q)\bigr).
$$

Por tanto,

$$
L_F\!\left(
\Psi_{E,F}\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
\right)
=
L_F\bigl(\jmath_{\mathbb Q}^{F}(q)\bigr).
$$

Como $F$ es completo, Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano implica que es arquimediano. La igualdad de trazas da las dos inclusiones, y Proposición 12.5.1 — La inclusión de trazas racionales caracteriza el orden las convierte en las dos desigualdades opuestas entre los elementos de $F$. Por antisimetría,

$$
\Psi_{E,F}\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
=
\jmath_{\mathbb Q}^{F}(q).
$$

Finalmente, Corolario 12.2.9 — La copia racional de toda completación es la copia canónica identifica las incrustaciones que forman parte de las completaciones con las copias canónicas:

$$
\iota_E=\jmath_{\mathbb Q}^{E},
\qquad
\iota_F=\jmath_{\mathbb Q}^{F}.
$$

La igualdad anterior es entonces exactamente

$$
\Psi_{E,F}\circ\iota_E=\iota_F.
$$

∎

No se ha identificado $\mathbb Q$ con un subconjunto literal de ninguno de los dos cuerpos. El transporte conmuta con dos funciones explícitamente construidas.

---

### Lema 12.6.3 — Caracterización racional de la suma

Sea $G$ un cuerpo ordenado arquimediano y sean $x,y\in G$. Para todo $q\in\mathbb Q$,

$$
\boxed{
q\in L_G(x+y)
\iff
\exists r,s\in\mathbb Q\;
\bigl(
 r\in L_G(x)
\land
 s\in L_G(y)
\land
 q<r+s
\bigr).
}
$$

**Demostración.**

Supongamos primero

$$
q\in L_G(x+y).
$$

Por definición,

$$
\jmath_{\mathbb Q}^{G}(q)<x+y.
$$

Trasladando términos en el grupo aditivo de $G$,

$$
\jmath_{\mathbb Q}^{G}(q)-y<x.
$$

Como $G$ es arquimediano, Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano proporciona un racional $r$ tal que

$$
\jmath_{\mathbb Q}^{G}(q)-y
<
\jmath_{\mathbb Q}^{G}(r)
<
x.
$$

La segunda desigualdad significa

$$
r\in L_G(x).
$$

De la primera, trasladando de nuevo,

$$
\jmath_{\mathbb Q}^{G}(q)
-
\jmath_{\mathbb Q}^{G}(r)
<
y.
$$

Aplicamos otra vez la densidad racional. Existe $s\in\mathbb Q$ con

$$
\jmath_{\mathbb Q}^{G}(q)
-
\jmath_{\mathbb Q}^{G}(r)
<
\jmath_{\mathbb Q}^{G}(s)
<
y.
$$

Así $s\in L_G(y)$ y

$$
\jmath_{\mathbb Q}^{G}(q)
<
\jmath_{\mathbb Q}^{G}(r)
+
\jmath_{\mathbb Q}^{G}(s).
$$

Por la compatibilidad aditiva de Proposición 12.2.4 — Compatibilidad algebraica de la copia racional, el miembro derecho es

$$
\jmath_{\mathbb Q}^{G}(r+s).
$$

Reflejando el orden mediante Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados, obtenemos

$$
q<r+s.
$$

Esto prueba la implicación directa.

Recíprocamente, supongamos que existen $r,s\in\mathbb Q$ tales que

$$
r\in L_G(x),
\qquad
s\in L_G(y),
\qquad
q<r+s.
$$

Entonces

$$
\jmath_{\mathbb Q}^{G}(r)<x,
\qquad
\jmath_{\mathbb Q}^{G}(s)<y.
$$

La compatibilidad del orden con la suma da

$$
\jmath_{\mathbb Q}^{G}(r)
+
\jmath_{\mathbb Q}^{G}(s)
<
x+y.
$$

Además, $q<r+s$ y Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados implican

$$
\jmath_{\mathbb Q}^{G}(q)
<
\jmath_{\mathbb Q}^{G}(r+s)
=
\jmath_{\mathbb Q}^{G}(r)
+
\jmath_{\mathbb Q}^{G}(s).
$$

Por transitividad,

$$
\jmath_{\mathbb Q}^{G}(q)<x+y,
$$

es decir,

$$
q\in L_G(x+y).
$$

∎

> **Auditoría de elección.** Para un $q$ fijo se usan dos aplicaciones sucesivas de la densidad, cada una de las cuales proporciona un único testigo existencial local para esa demostración. No se construyen funciones $q\mapsto r_q$ ni $q\mapsto s_q$.

---

### Teorema 12.6.4 — El transporte preserva la suma

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Para todos $x,y\in E$,

$$
\boxed{
\Psi_{E,F}(x+y)
=
\Psi_{E,F}(x)+\Psi_{E,F}(y).
}
$$

**Demostración.**

Como $E$ y $F$ son completos, Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano implica que ambos son arquimedianos. Fijemos $x,y\in E$.

Por Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional,

$$
L_F\bigl(\Psi_{E,F}(x)\bigr)=L_E(x),
\qquad
L_F\bigl(\Psi_{E,F}(y)\bigr)=L_E(y),
$$

y también

$$
L_F\bigl(\Psi_{E,F}(x+y)\bigr)=L_E(x+y).
$$

Sea $q\in\mathbb Q$. Aplicando Lema 12.6.3 — Caracterización racional de la suma en $E$,

$$
\begin{aligned}
q\in L_E(x+y)
\iff{}&
\exists r,s\in\mathbb Q\;(
 r\in L_E(x)\land
 s\in L_E(y)\land
 q<r+s).
\end{aligned}
$$

Sustituyendo las dos identidades de trazas,

$$
\begin{aligned}
q\in L_E(x+y)
\iff{}&
\exists r,s\in\mathbb Q\;(
 r\in L_F(\Psi_{E,F}(x))\land\\
&\hspace{33mm}
 s\in L_F(\Psi_{E,F}(y))\land
 q<r+s).
\end{aligned}
$$

Aplicando ahora Lema 12.6.3 — Caracterización racional de la suma en $F$, el miembro derecho equivale a

$$
q\in
L_F\bigl(
\Psi_{E,F}(x)+\Psi_{E,F}(y)
\bigr).
$$

Por tanto, para todo $q\in\mathbb Q$,

$$
q\in L_F\bigl(\Psi_{E,F}(x+y)\bigr)
\iff
q\in
L_F\bigl(
\Psi_{E,F}(x)+\Psi_{E,F}(y)
\bigr).
$$

La extensionalidad da igualdad de las dos trazas. Como $F$ es arquimediano, Proposición 12.5.1 — La inclusión de trazas racionales caracteriza el orden transforma esa igualdad en las dos desigualdades opuestas entre los elementos correspondientes; por antisimetría,

$$
\Psi_{E,F}(x+y)
=
\Psi_{E,F}(x)+\Psi_{E,F}(y).
$$

∎

---

### Corolario 12.6.5 — Cero, opuesto y sustracción

Para toda pareja de completaciones ordenadas $(E,\iota_E)$ y $(F,\iota_F)$ y todo $x,y\in E$,

$$
\boxed{
\Psi_{E,F}(0_E)=0_F,
}
$$

$$
\boxed{
\Psi_{E,F}(-x)=-\Psi_{E,F}(x),
}
$$

y

$$
\boxed{
\Psi_{E,F}(x-y)
=
\Psi_{E,F}(x)-\Psi_{E,F}(y).
}
$$

**Demostración.**

Por Proposición 12.6.2 — El transporte fija la copia racional canónica aplicado a $0_{\mathbb Q}$,

$$
\Psi_{E,F}\bigl(\jmath_{\mathbb Q}^{E}(0_{\mathbb Q})\bigr)
=
\jmath_{\mathbb Q}^{F}(0_{\mathbb Q}).
$$

Proposición 12.2.4 — Compatibilidad algebraica de la copia racional identifica los dos miembros con $\Psi_{E,F}(0_E)$ y $0_F$, respectivamente. Luego

$$
\Psi_{E,F}(0_E)=0_F.
$$

Para el opuesto, Teorema 12.6.4 — El transporte preserva la suma da

$$
\begin{aligned}
0_F
&=\Psi_{E,F}(0_E)\\
&=\Psi_{E,F}(x+(-x))\\
&=\Psi_{E,F}(x)+\Psi_{E,F}(-x).
\end{aligned}
$$

Por unicidad del inverso aditivo en el cuerpo $F$,

$$
\Psi_{E,F}(-x)=-\Psi_{E,F}(x).
$$

Finalmente,

$$
\begin{aligned}
\Psi_{E,F}(x-y)
&=\Psi_{E,F}(x+(-y))\\
&=\Psi_{E,F}(x)+\Psi_{E,F}(-y)\\
&=\Psi_{E,F}(x)-\Psi_{E,F}(y).
\end{aligned}
$$

∎

---

### Lema 12.6.6 — Caracterización racional del producto no negativo

Sea $G$ un cuerpo ordenado arquimediano y sean $x,y\in G$ tales que

$$
0_G\le x,
\qquad
0_G\le y.
$$

Para todo $q\in\mathbb Q$,

$$
\boxed{
\begin{aligned}
q\in L_G(xy)
\iff{}& q<0_{\mathbb Q}\\
&\text{o bien existe }r,s\in\mathbb Q\text{ tales que}\\
&0_{\mathbb Q}<r,
\quad
0_{\mathbb Q}<s,
\quad
r\in L_G(x),
\quad
s\in L_G(y),
\quad
q<rs.
\end{aligned}
}
$$

**Demostración.**

Supongamos primero

$$
q\in L_G(xy),
$$

es decir,

$$
\jmath_{\mathbb Q}^{G}(q)<xy.
$$

Si $q<0_{\mathbb Q}$, estamos en la primera alternativa.

Supongamos entonces

$$
0_{\mathbb Q}\le q.
$$

Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados implica

$$
0_G
\le
\jmath_{\mathbb Q}^{G}(q)
<xy,
$$

de modo que $xy>0_G$. Como $x,y\ge0_G$, ninguno de los dos puede ser cero; por totalidad,

$$
0_G<x,
\qquad
0_G<y.
$$

El inverso de $y$ es positivo por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado. Multiplicando

$$
\jmath_{\mathbb Q}^{G}(q)<xy
$$

por $y^{-1}>0_G$, obtenemos

$$
\jmath_{\mathbb Q}^{G}(q)y^{-1}<x.
$$

Además,

$$
0_G\le \jmath_{\mathbb Q}^{G}(q)y^{-1}.
$$

La densidad racional Teorema 12.3.1 — Densidad de la copia racional canónica en un cuerpo arquimediano proporciona $r\in\mathbb Q$ tal que

$$
\jmath_{\mathbb Q}^{G}(q)y^{-1}
<
\jmath_{\mathbb Q}^{G}(r)
<
x.
$$

Como el extremo izquierdo es no negativo,

$$
0_G<\jmath_{\mathbb Q}^{G}(r),
$$

y Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados refleja esto como

$$
0_{\mathbb Q}<r.
$$

Además $r\in L_G(x)$. Multiplicando la primera desigualdad por $y>0_G$,

$$
\jmath_{\mathbb Q}^{G}(q)
<
\jmath_{\mathbb Q}^{G}(r)y.
$$

Como $\jmath_{\mathbb Q}^{G}(r)>0_G$, su inverso es positivo. Multiplicando por él,

$$
\jmath_{\mathbb Q}^{G}(q)
\bigl(\jmath_{\mathbb Q}^{G}(r)\bigr)^{-1}
<
y.
$$

El miembro izquierdo es no negativo. Aplicamos de nuevo la densidad racional y obtenemos $s\in\mathbb Q$ con

$$
\jmath_{\mathbb Q}^{G}(q)
\bigl(\jmath_{\mathbb Q}^{G}(r)\bigr)^{-1}
<
\jmath_{\mathbb Q}^{G}(s)
<
y.
$$

Entonces

$$
0_{\mathbb Q}<s,
\qquad
s\in L_G(y).
$$

Multiplicando la primera desigualdad por $\jmath_{\mathbb Q}^{G}(r)>0_G$,

$$
\jmath_{\mathbb Q}^{G}(q)
<
\jmath_{\mathbb Q}^{G}(r)
\jmath_{\mathbb Q}^{G}(s).
$$

Por Proposición 12.2.4 — Compatibilidad algebraica de la copia racional,

$$
\jmath_{\mathbb Q}^{G}(r)
\jmath_{\mathbb Q}^{G}(s)
=
\jmath_{\mathbb Q}^{G}(rs).
$$

La reflexión del orden de Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados da

$$
q<rs.
$$

Hemos obtenido la segunda alternativa.

Recíprocamente, supongamos primero $q<0_{\mathbb Q}$. Como $x,y\ge0_G$, el cálculo de signos de Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado da

$$
0_G\le xy.
$$

Por Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados,

$$
\jmath_{\mathbb Q}^{G}(q)<0_G\le xy,
$$

y por tanto $q\in L_G(xy)$.

Queda la segunda alternativa. Supongamos que existen $r,s\in\mathbb Q$ tales que

$$
0_{\mathbb Q}<r,
\quad
0_{\mathbb Q}<s,
\quad
r\in L_G(x),
\quad
s\in L_G(y),
\quad
q<rs.
$$

Entonces

$$
0_G<\jmath_{\mathbb Q}^{G}(r)<x,
\qquad
0_G<\jmath_{\mathbb Q}^{G}(s)<y.
$$

Como $0_G<\jmath_{\mathbb Q}^{G}(s)$ y $\jmath_{\mathbb Q}^{G}(r)<x$,

$$
\jmath_{\mathbb Q}^{G}(r)
\jmath_{\mathbb Q}^{G}(s)
<
x\jmath_{\mathbb Q}^{G}(s).
$$

Además $x>0_G$ y $\jmath_{\mathbb Q}^{G}(s)<y$, luego

$$
x\jmath_{\mathbb Q}^{G}(s)<xy.
$$

Por transitividad,

$$
\jmath_{\mathbb Q}^{G}(r)
\jmath_{\mathbb Q}^{G}(s)
<xy.
$$

Por otra parte,

$$
q<rs
$$

implica

$$
\jmath_{\mathbb Q}^{G}(q)
<
\jmath_{\mathbb Q}^{G}(rs)
=
\jmath_{\mathbb Q}^{G}(r)
\jmath_{\mathbb Q}^{G}(s).
$$

Por transitividad,

$$
\jmath_{\mathbb Q}^{G}(q)<xy,
$$

es decir,

$$
q\in L_G(xy).
$$

∎

> **Auditoría de elección.** Cuando $q\ge0$ se obtienen sucesivamente dos racionales, primero $r$ y después $s$, mediante densidad en dos intervalos determinados por los datos ya fijados. No se define una selección simultánea de aproximantes para todos los triples $(x,y,q)$.

---

### Teorema 12.6.7 — El transporte preserva el producto

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Para todos $x,y\in E$,

$$
\boxed{
\Psi_{E,F}(xy)
=
\Psi_{E,F}(x)\Psi_{E,F}(y).
}
$$

**Demostración.**

Como $E$ y $F$ son completos, ambos son arquimedianos por Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano.

Comenzamos por el caso

$$
0_E\le x,
\qquad
0_E\le y.
$$

Por Corolario 12.6.5 — Cero, opuesto y sustracción y la preservación del orden de Teorema 12.5.2 — El transporte preserva y refleja el orden,

$$
0_F\le\Psi_{E,F}(x),
\qquad
0_F\le\Psi_{E,F}(y).
$$

Sea $q\in\mathbb Q$. El criterio de Lema 12.6.6 — Caracterización racional del producto no negativo aplicado en $E$ expresa la pertenencia

$$
q\in L_E(xy)
$$

exclusivamente mediante la relación $q<0_{\mathbb Q}$ y la existencia de racionales positivos $r,s$ pertenecientes respectivamente a $L_E(x)$ y $L_E(y)$ con $q<rs$.

Pero Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional da

$$
L_E(x)=L_F\bigl(\Psi_{E,F}(x)\bigr),
\qquad
L_E(y)=L_F\bigl(\Psi_{E,F}(y)\bigr).
$$

Por tanto el mismo criterio, ahora aplicado en $F$, muestra que

$$
q\in L_E(xy)
\iff
q\in
L_F\bigl(
\Psi_{E,F}(x)\Psi_{E,F}(y)
\bigr).
$$

Además,

$$
L_F\bigl(\Psi_{E,F}(xy)\bigr)=L_E(xy)
$$

por Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional. Como la equivalencia vale para todo racional $q$, la extensionalidad da

$$
L_F\bigl(\Psi_{E,F}(xy)\bigr)
=
L_F\bigl(
\Psi_{E,F}(x)\Psi_{E,F}(y)
\bigr).
$$

La igualdad de trazas y Proposición 12.5.1 — La inclusión de trazas racionales caracteriza el orden implican, por antisimetría,

$$
\Psi_{E,F}(xy)
=
\Psi_{E,F}(x)\Psi_{E,F}(y).
$$

Así el producto queda preservado cuando ambos factores son no negativos.

Extendamos ahora el resultado a signos arbitrarios. Por totalidad del orden, para cada elemento vale $0\le x$ o $x<0$, y análogamente para $y$.

Si $x<0$ y $0\le y$, entonces $0<-x$. Usando las identidades elementales de cuerpo, Corolario 12.6.5 — Cero, opuesto y sustracción y el caso no negativo ya probado,

$$
\begin{aligned}
\Psi_{E,F}(xy)
&=\Psi_{E,F}\bigl(-((-x)y)\bigr)\\
&=-\Psi_{E,F}((-x)y)\\
&=-\bigl(\Psi_{E,F}(-x)\Psi_{E,F}(y)\bigr)\\
&=-\bigl((-\Psi_{E,F}(x))\Psi_{E,F}(y)\bigr)\\
&=\Psi_{E,F}(x)\Psi_{E,F}(y).
\end{aligned}
$$

El caso $0\le x$ y $y<0$ es simétrico.

Finalmente, si $x<0$ y $y<0$, entonces $-x>0$ y $-y>0$, mientras que

$$
xy=(-x)(-y).
$$

Por el caso no negativo,

$$
\begin{aligned}
\Psi_{E,F}(xy)
&=\Psi_{E,F}((-x)(-y))\\
&=\Psi_{E,F}(-x)\Psi_{E,F}(-y)\\
&=(-\Psi_{E,F}(x))(-\Psi_{E,F}(y))\\
&=\Psi_{E,F}(x)\Psi_{E,F}(y).
\end{aligned}
$$

Los cuatro casos cubren todas las posibilidades. ∎

---

### Teorema 12.6.8 — El transporte es un isomorfismo de cuerpos ordenados

Sean $(E,\iota_E)$ y $(F,\iota_F)$ completaciones ordenadas de $\mathbb Q$. Entonces

$$
\boxed{
\Psi_{E,F}:E\longrightarrow F
}
$$

es un isomorfismo de cuerpos ordenados. En particular, para todos $x,y\in E$,

$$
\boxed{
\Psi_{E,F}(0_E)=0_F,
\qquad
\Psi_{E,F}(1_E)=1_F,
}
$$

$$
\boxed{
\Psi_{E,F}(x+y)
=
\Psi_{E,F}(x)+\Psi_{E,F}(y),
}
$$

$$
\boxed{
\Psi_{E,F}(xy)
=
\Psi_{E,F}(x)\Psi_{E,F}(y),
}
$$

y

$$
\boxed{
x\le y
\iff
\Psi_{E,F}(x)\le\Psi_{E,F}(y).
}
$$

La función es biyectiva y satisface además

$$
\boxed{
\Psi_{E,F}\circ\iota_E=\iota_F.
}
$$

Si $x\neq0_E$, entonces

$$
\boxed{
\Psi_{E,F}(x^{-1})
=
\bigl(\Psi_{E,F}(x)\bigr)^{-1}.
}
$$

**Demostración.**

La biyectividad fue demostrada en Corolario 12.5.3 — Los transportes simétricos son inversos; la preservación y reflexión del orden, en Teorema 12.5.2 — El transporte preserva y refleja el orden; la suma, en Teorema 12.6.4 — El transporte preserva la suma; el cero y el opuesto, en Corolario 12.6.5 — Cero, opuesto y sustracción; y el producto, en Teorema 12.6.7 — El transporte preserva el producto.

La unidad se obtiene de Proposición 12.6.2 — El transporte fija la copia racional canónica aplicada a $1_{\mathbb Q}$. En efecto,

$$
\Psi_{E,F}\bigl(\jmath_{\mathbb Q}^{E}(1_{\mathbb Q})\bigr)
=
\jmath_{\mathbb Q}^{F}(1_{\mathbb Q}),
$$

y Proposición 12.2.4 — Compatibilidad algebraica de la copia racional convierte esta igualdad en

$$
\Psi_{E,F}(1_E)=1_F.
$$

La compatibilidad con las incrustaciones racionales es exactamente la segunda afirmación de Proposición 12.6.2 — El transporte fija la copia racional canónica.

Resta el recíproco. Sea $x\neq0_E$. Como $\Psi_{E,F}$ es inyectiva y preserva el cero,

$$
\Psi_{E,F}(x)\neq0_F.
$$

Además,

$$
xx^{-1}=1_E.
$$

Aplicando la preservación del producto y de la unidad,

$$
\Psi_{E,F}(x)
\Psi_{E,F}(x^{-1})
=
1_F.
$$

Por unicidad del inverso multiplicativo en $F$,

$$
\Psi_{E,F}(x^{-1})
=
\bigl(\Psi_{E,F}(x)\bigr)^{-1}.
$$

Así $\Psi_{E,F}$ conserva toda la estructura de cuerpo y toda la estructura de orden, y es biyectiva. Por tanto es un isomorfismo de cuerpos ordenados. ∎

La existencia del isomorfismo abstracto entre dos completaciones queda ya establecida. A diferencia del isomorfismo concreto del Capítulo 11, aquí no hemos usado ninguna codificación particular de los elementos: toda la construcción depende únicamente de la copia racional densa, el orden y la completitud.

Falta todavía una cuestión lógica esencial. Podría existir, en principio, otro isomorfismo de cuerpos ordenados $T:E\to F$ que también satisfaga

$$
T\circ\iota_E=\iota_F.
$$

§12.7 demostrará que esto es imposible: cualquier aplicación con esas propiedades debe preservar todas las trazas racionales y, por tanto, coincidir punto por punto con $\Psi_{E,F}$.

---
