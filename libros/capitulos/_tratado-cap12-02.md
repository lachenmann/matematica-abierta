## 12.2. Copia canónica de $\mathbb Q$ {#sec-ta-12-2}

La sección anterior prolongó los numerales naturales hasta una incrustación ordenada

$$
\jmath_{\mathbb Z}^{F}:\mathbb Z\longrightarrow F.
$$

Para llegar a los racionales debemos incorporar inversos multiplicativos. Sin embargo, tampoco aquí podemos definir una función sobre $\mathbb Q$ diciendo simplemente «escojamos una fracción que represente a $q$». El conjunto $\mathbb Q$ fue construido como cociente, y la definición debe respetar esa construcción.

Recordemos que

$$
D_{\mathbb Q}=\mathbb Z\times\mathbb Z_{\neq0}
$$

y que

$$
(a,b)\sim_{\mathbb Q}(c,d)\iff ad=bc.
$$

Procederemos, por tanto, exactamente como en las construcciones anteriores: primero evaluaremos todos los representantes racionales en $F$, después probaremos invariancia sobre las clases y sólo entonces descenderemos al cociente.

### Definición 12.2.1 — Evaluación de representantes racionales en un cuerpo ordenado

Para $(a,b)\in D_{\mathbb Q}$ definimos

$$
\boxed{
\psi_F(a,b):=
\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}.
}
$$

Así obtenemos una función

$$
\boxed{\psi_F:D_{\mathbb Q}\longrightarrow F.}
$$

La expresión está bien tipada. En efecto, si $(a,b)\in D_{\mathbb Q}$, entonces $b\neq0_{\mathbb Z}$. Como Teorema 12.1.5 — La copia entera es una incrustación ordenada demuestra que $\jmath_{\mathbb Z}^{F}$ es inyectiva y Proposición 12.1.4 — Compatibilidad aritmética de la copia entera da

$$
\jmath_{\mathbb Z}^{F}(0_{\mathbb Z})=0_F,
$$

se sigue que

$$
\jmath_{\mathbb Z}^{F}(b)\neq0_F.
$$

Por tanto su inverso multiplicativo existe en el cuerpo $F$.

Conjuntistamente, el grafo de $\psi_F$ se obtiene por Separación dentro de

$$
D_{\mathbb Q}\times F,
$$

pues para cada $(a,b)\in D_{\mathbb Q}$ la fórmula anterior determina un único elemento de $F$.

La función $\psi_F$ vive todavía en el nivel de representantes. El paso decisivo es demostrar que la equivalencia racional no altera su valor.

---

### Proposición 12.2.2 — Invariancia bajo la equivalencia racional

Si

$$
(a,b)\sim_{\mathbb Q}(c,d),
$$

entonces

$$
\boxed{\psi_F(a,b)=\psi_F(c,d).}
$$

**Demostración.**

Por Definición 3.2.1 — Relación de equivalencia racional, la hipótesis equivale a

$$
ad=bc
$$

en $\mathbb Z$. Aplicando la compatibilidad multiplicativa de Proposición 12.1.4 — Compatibilidad aritmética de la copia entera, obtenemos

$$
\jmath_{\mathbb Z}^{F}(a)\jmath_{\mathbb Z}^{F}(d)
=
\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(c).
$$

Como $b,d\neq0_{\mathbb Z}$ y $\jmath_{\mathbb Z}^{F}$ es inyectiva, ambos elementos $\jmath_{\mathbb Z}^{F}(b)$ y $\jmath_{\mathbb Z}^{F}(d)$ son no nulos. Multiplicando la igualdad anterior por

$$
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}
\bigl(\jmath_{\mathbb Z}^{F}(d)\bigr)^{-1}
$$

y usando asociatividad y conmutatividad del producto en $F$, resulta

$$
\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}
=
\jmath_{\mathbb Z}^{F}(c)
\bigl(\jmath_{\mathbb Z}^{F}(d)\bigr)^{-1}.
$$

Por Definición 12.2.1 — Evaluación de representantes racionales en un cuerpo ordenado, los dos miembros son respectivamente $\psi_F(a,b)$ y $\psi_F(c,d)$. ∎

---

### Definición 12.2.3 — Copia canónica de los racionales en un cuerpo ordenado

Como

$$
\mathbb Q=D_{\mathbb Q}/{\sim_{\mathbb Q}}
$$

y Proposición 12.2.2 — Invariancia bajo la equivalencia racional demuestra que $\psi_F$ es constante sobre las clases de $\sim_{\mathbb Q}$, el principio de definición sobre clases Teorema 0.6.15 — Principio de definición sobre clases produce una única función

$$
\boxed{\jmath_{\mathbb Q}^{F}:\mathbb Q\longrightarrow F}
$$

tal que, para todos $a,b\in\mathbb Z$ con $b\neq0_{\mathbb Z}$,

$$
\boxed{
\jmath_{\mathbb Q}^{F}\left(\frac ab\right)
=
\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}.
}
$$

Llamaremos a $\jmath_{\mathbb Q}^{F}$ la **copia canónica de los racionales en $F$**.

La fórmula no depende de una selección de representantes: la independencia ya fue demostrada antes de definir la función sobre el cociente. En particular, seguimos sin identificar literalmente $\mathbb Q$ con un subconjunto de $F$.

---

### Proposición 12.2.4 — Compatibilidad algebraica de la copia racional

Para todos $q,r\in\mathbb Q$ y todo $a\in\mathbb Z$ se cumplen:

$$
\boxed{
\jmath_{\mathbb Q}^{F}(0_{\mathbb Q})=0_F,
\qquad
\jmath_{\mathbb Q}^{F}(1_{\mathbb Q})=1_F,
}
$$

$$
\boxed{
\jmath_{\mathbb Q}^{F}(q+r)
=
\jmath_{\mathbb Q}^{F}(q)+\jmath_{\mathbb Q}^{F}(r),
}
$$

$$
\boxed{
\jmath_{\mathbb Q}^{F}(qr)
=
\jmath_{\mathbb Q}^{F}(q)\jmath_{\mathbb Q}^{F}(r),
}
$$

$$
\boxed{
\jmath_{\mathbb Q}^{F}(-q)
=
-\jmath_{\mathbb Q}^{F}(q),
}
$$

y

$$
\boxed{
\jmath_{\mathbb Q}^{F}
\bigl(\jmath_{\mathbb Z}^{\mathbb Q}(a)\bigr)
=
\jmath_{\mathbb Z}^{F}(a).
}
$$

Además, si $q\neq0_{\mathbb Q}$, entonces

$$
\boxed{
\jmath_{\mathbb Q}^{F}(q^{-1})
=
\bigl(\jmath_{\mathbb Q}^{F}(q)\bigr)^{-1}.
}
$$

**Demostración.**

Como todo racional es una clase del cociente Definición 3.2.4 — Conjunto de los números racionales, para los racionales fijos $q$ y $r$ podemos tomar representantes

$$
q=\frac ab,
\qquad
r=\frac cd,
$$

con $a,c\in\mathbb Z$ y $b,d\in\mathbb Z_{\neq0}$. No se está definiendo una selección simultánea de representantes para todos los racionales.

Para el cero y la unidad usamos las representaciones

$$
0_{\mathbb Q}=\frac{0_{\mathbb Z}}{1_{\mathbb Z}},
\qquad
1_{\mathbb Q}=\frac{1_{\mathbb Z}}{1_{\mathbb Z}}.
$$

Por Proposición 12.1.4 — Compatibilidad aritmética de la copia entera,

$$
\jmath_{\mathbb Z}^{F}(0_{\mathbb Z})=0_F,
\qquad
\jmath_{\mathbb Z}^{F}(1_{\mathbb Z})=1_F,
$$

y por tanto Definición 12.2.3 — Copia canónica de los racionales en un cuerpo ordenado da las dos primeras identidades.

La suma racional satisface

$$
q+r=\frac{ad+bc}{bd}.
$$

En consecuencia,

$$
\begin{aligned}
\jmath_{\mathbb Q}^{F}(q+r)
&=\jmath_{\mathbb Z}^{F}(ad+bc)
\bigl(\jmath_{\mathbb Z}^{F}(bd)\bigr)^{-1}\\
&=\bigl(
\jmath_{\mathbb Z}^{F}(a)\jmath_{\mathbb Z}^{F}(d)
+\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(c)
\bigr)
\bigl(
\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(d)
\bigr)^{-1}\\
&=\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}
+\jmath_{\mathbb Z}^{F}(c)
\bigl(\jmath_{\mathbb Z}^{F}(d)\bigr)^{-1}\\
&=\jmath_{\mathbb Q}^{F}(q)+\jmath_{\mathbb Q}^{F}(r).
\end{aligned}
$$

En el tercer paso usamos únicamente las leyes de cuerpo y el hecho de que las imágenes de $b$ y $d$ son no nulas.

Para el producto,

$$
qr=\frac{ac}{bd},
$$

de modo que

$$
\begin{aligned}
\jmath_{\mathbb Q}^{F}(qr)
&=\jmath_{\mathbb Z}^{F}(ac)
\bigl(\jmath_{\mathbb Z}^{F}(bd)\bigr)^{-1}\\
&=\jmath_{\mathbb Z}^{F}(a)\jmath_{\mathbb Z}^{F}(c)
\bigl(
\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(d)
\bigr)^{-1}\\
&=\jmath_{\mathbb Q}^{F}(q)\jmath_{\mathbb Q}^{F}(r).
\end{aligned}
$$

La compatibilidad con el opuesto se obtiene de

$$
-q=\frac{-a}{b}
$$

y de Proposición 12.1.4 — Compatibilidad aritmética de la copia entera:

$$
\begin{aligned}
\jmath_{\mathbb Q}^{F}(-q)
&=\jmath_{\mathbb Z}^{F}(-a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}\\
&=-\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}\\
&=-\jmath_{\mathbb Q}^{F}(q).
\end{aligned}
$$

Para la extensión de la copia entera, Definición 3.5.1 — Incrustación entera en los racionales da

$$
\jmath_{\mathbb Z}^{\mathbb Q}(a)=\frac{a}{1_{\mathbb Z}}.
$$

Entonces

$$
\begin{aligned}
\jmath_{\mathbb Q}^{F}
\bigl(\jmath_{\mathbb Z}^{\mathbb Q}(a)\bigr)
&=\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(1_{\mathbb Z})\bigr)^{-1}\\
&=\jmath_{\mathbb Z}^{F}(a)1_F^{-1}\\
&=\jmath_{\mathbb Z}^{F}(a).
\end{aligned}
$$

Finalmente, sea $q\neq0_{\mathbb Q}$. Como

$$
qq^{-1}=1_{\mathbb Q},
$$

la compatibilidad multiplicativa ya demostrada da

$$
\jmath_{\mathbb Q}^{F}(q)
\jmath_{\mathbb Q}^{F}(q^{-1})=1_F.
$$

En particular $\jmath_{\mathbb Q}^{F}(q)\neq0_F$, pues $0_F$ no puede multiplicarse por ningún elemento y producir $1_F$. Por unicidad del inverso multiplicativo,

$$
\jmath_{\mathbb Q}^{F}(q^{-1})
=
\bigl(\jmath_{\mathbb Q}^{F}(q)\bigr)^{-1}.
$$

Todas las compatibilidades quedan demostradas. ∎

> **Auditoría de elección.** Sólo se fijan representantes para los racionales concretos que intervienen en cada argumento. La función $\jmath_{\mathbb Q}^{F}$ ya fue definida por descenso al cociente y no depende de ninguna sección de representantes.

---

### Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados

La función

$$
\jmath_{\mathbb Q}^{F}:\mathbb Q\longrightarrow F
$$

es una incrustación de cuerpos ordenados. En particular, para todos $q,r\in\mathbb Q$,

$$
\boxed{
q\le_{\mathbb Q}r
\iff
\jmath_{\mathbb Q}^{F}(q)\le_F\jmath_{\mathbb Q}^{F}(r),
}
$$

y

$$
\boxed{
q<_{\mathbb Q}r
\iff
\jmath_{\mathbb Q}^{F}(q)<_F\jmath_{\mathbb Q}^{F}(r).
}
$$

**Demostración.**

La preservación de $0$, $1$, suma y producto ya fue demostrada en Proposición 12.2.4 — Compatibilidad algebraica de la copia racional. Falta establecer la comparación de órdenes y la inyectividad.

Fijemos $q,r\in\mathbb Q$. Por el lema de denominador positivo Lema 3.7.1 — Representante con denominador positivo existen representantes

$$
q=\frac ab,
\qquad
r=\frac cd,
$$

con

$$
b>_{\mathbb Z}0_{\mathbb Z},
\qquad
d>_{\mathbb Z}0_{\mathbb Z}.
$$

Por Corolario 3.7.7 — Criterio estricto de comparación cruzada,

$$
q<_{\mathbb Q}r\iff ad<_{\mathbb Z}bc.
$$

Como Teorema 12.1.5 — La copia entera es una incrustación ordenada preserva y refleja el orden estricto entero, y Proposición 12.1.4 — Compatibilidad aritmética de la copia entera preserva el producto,

$$
ad<_{\mathbb Z}bc
\iff
\jmath_{\mathbb Z}^{F}(a)\jmath_{\mathbb Z}^{F}(d)
<_F
\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(c).
$$

Además,

$$
0_F<\jmath_{\mathbb Z}^{F}(b),
\qquad
0_F<\jmath_{\mathbb Z}^{F}(d).
$$

Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado, su producto es positivo. Apliquemos ahora Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (9) con el factor

$$
R:=\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(d)>0_F.
$$

Si escribimos

$$
X:=\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1},
\qquad
Y:=\jmath_{\mathbb Z}^{F}(c)
\bigl(\jmath_{\mathbb Z}^{F}(d)\bigr)^{-1},
$$

entonces

$$
XR=\jmath_{\mathbb Z}^{F}(a)\jmath_{\mathbb Z}^{F}(d),
\qquad
YR=\jmath_{\mathbb Z}^{F}(c)\jmath_{\mathbb Z}^{F}(b).
$$

Como el producto es conmutativo,

$$
YR=\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(c).
$$

Por tanto Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (9) da exactamente

$$
\jmath_{\mathbb Z}^{F}(a)\jmath_{\mathbb Z}^{F}(d)
<_F
\jmath_{\mathbb Z}^{F}(b)\jmath_{\mathbb Z}^{F}(c)
$$

si y sólo si

$$
\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}
<_F
\jmath_{\mathbb Z}^{F}(c)
\bigl(\jmath_{\mathbb Z}^{F}(d)\bigr)^{-1}.
$$

Por Definición 12.2.3 — Copia canónica de los racionales en un cuerpo ordenado, concluimos

$$
q<_{\mathbb Q}r
\iff
\jmath_{\mathbb Q}^{F}(q)<_F\jmath_{\mathbb Q}^{F}(r).
$$

Esta equivalencia estricta implica inyectividad. En efecto, si las imágenes de $q$ y $r$ fueran iguales con $q\neq r$, la tricotomía decidible de Proposición 3.7.6 — Tricotomía decidible de los racionales daría $q<r$ o $r<q$, y la equivalencia anterior produciría una desigualdad estricta entre elementos iguales de $F$, contradicción.

Finalmente, la misma tricotomía decidible racional permite descomponer el orden no estricto como

$$
x\le y\iff(x<y\ \text{o}\ x=y).
$$

La equivalencia estricta y la inyectividad recién demostradas producen entonces

$$
q\le_{\mathbb Q}r
\iff
\jmath_{\mathbb Q}^{F}(q)\le_F\jmath_{\mathbb Q}^{F}(r).
$$

Se satisfacen todas las condiciones de Definición 4.8.1 — Incrustación de cuerpos ordenados; por tanto $\jmath_{\mathbb Q}^{F}$ es una incrustación de cuerpos ordenados. ∎

---

### Lema 12.2.6 — La imagen de la copia racional es un subcuerpo

El subconjunto

$$
\boxed{\jmath_{\mathbb Q}^{F}[\mathbb Q]\subseteq F}
$$

es un subcuerpo de $F$.

**Demostración.**

Por Proposición 12.2.4 — Compatibilidad algebraica de la copia racional,

$$
0_F=\jmath_{\mathbb Q}^{F}(0_{\mathbb Q}),
\qquad
1_F=\jmath_{\mathbb Q}^{F}(1_{\mathbb Q}),
$$

de modo que ambos elementos pertenecen a la imagen.

Sean

$$
x=\jmath_{\mathbb Q}^{F}(q),
\qquad
y=\jmath_{\mathbb Q}^{F}(r)
$$

dos elementos de la imagen. Entonces

$$
x+y=\jmath_{\mathbb Q}^{F}(q+r),
\qquad
xy=\jmath_{\mathbb Q}^{F}(qr),
$$

y

$$
-x=\jmath_{\mathbb Q}^{F}(-q),
$$

por Proposición 12.2.4 — Compatibilidad algebraica de la copia racional. Por tanto la imagen es cerrada bajo suma, producto y opuesto.

Supongamos además $x\neq0_F$. Si $q=0_{\mathbb Q}$, la preservación del cero daría $x=0_F$, contradicción; luego $q\neq0_{\mathbb Q}$. El último apartado de Proposición 12.2.4 — Compatibilidad algebraica de la copia racional da

$$
x^{-1}
=
\bigl(\jmath_{\mathbb Q}^{F}(q)\bigr)^{-1}
=
\jmath_{\mathbb Q}^{F}(q^{-1}),
$$

que pertenece de nuevo a la imagen.

Se satisfacen las cuatro condiciones de Definición 4.1.7 — Subcuerpo. ∎

---

### Corolario 12.2.7 — La copia racional es exactamente el subcuerpo primo

Para todo cuerpo ordenado $F$,

$$
\boxed{
\jmath_{\mathbb Q}^{F}[\mathbb Q]=P_F.
}
$$

**Demostración.**

Por Lema 12.2.6 — La imagen de la copia racional es un subcuerpo, la imagen $\jmath_{\mathbb Q}^{F}[\mathbb Q]$ es un subcuerpo de $F$. La minimalidad de $P_F$ (Proposición 4.1.9 — Minimalidad del subcuerpo primo) implica entonces

$$
P_F\subseteq\jmath_{\mathbb Q}^{F}[\mathbb Q].
$$

Para la inclusión recíproca, sea

$$
x\in\jmath_{\mathbb Q}^{F}[\mathbb Q].
$$

Existe $q\in\mathbb Q$ tal que

$$
x=\jmath_{\mathbb Q}^{F}(q).
$$

Como $q$ es una clase racional, para este $q$ fijo existen $a,b\in\mathbb Z$, con $b\neq0_{\mathbb Z}$, tales que

$$
q=\frac ab.
$$

Por Corolario 12.1.6 — La copia entera está contenida en el subcuerpo primo,

$$
\jmath_{\mathbb Z}^{F}(a),
\jmath_{\mathbb Z}^{F}(b)
\in P_F.
$$

Además $\jmath_{\mathbb Z}^{F}(b)\neq0_F$ por la inyectividad de Teorema 12.1.5 — La copia entera es una incrustación ordenada. Como Proposición 4.1.9 — Minimalidad del subcuerpo primo demuestra que $P_F$ es un subcuerpo, también

$$
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}\in P_F
$$

y, por clausura multiplicativa,

$$
\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}
\in P_F.
$$

Por Definición 12.2.3 — Copia canónica de los racionales en un cuerpo ordenado, este último elemento es $\jmath_{\mathbb Q}^{F}(q)=x$. Así

$$
\jmath_{\mathbb Q}^{F}[\mathbb Q]\subseteq P_F.
$$

Las dos inclusiones dan la igualdad. ∎

> **Interpretación.** El subcuerpo primo abstracto construido en el Capítulo 4 ha quedado ahora identificado estructuralmente: en todo cuerpo ordenado es exactamente la imagen de la copia canónica de los racionales. Esto no significa que $P_F$ sea literalmente el mismo conjunto que $\mathbb Q$; significa que $\jmath_{\mathbb Q}^{F}$ proporciona un isomorfismo de $\mathbb Q$ sobre $P_F$ con las operaciones y el orden heredados.

---

### Teorema 12.2.8 — Unicidad de la incrustación racional

Sea $F$ un cuerpo ordenado. Si

$$
\iota:\mathbb Q\longrightarrow F
$$

es una incrustación de cuerpos ordenados, entonces

$$
\boxed{\iota=\jmath_{\mathbb Q}^{F}.}
$$

En particular, existe **una única** incrustación de cuerpos ordenados de $\mathbb Q$ en $F$.

**Demostración.**

Por Definición 4.8.1 — Incrustación de cuerpos ordenados, $\iota$ preserva $0$, $1$, suma y producto.

Consideremos primero la aplicación de numerales de $\mathbb Q$. Por Proposición 4.4.3 — La formulación abstracta coincide con la arquimedianidad ya probada en $\mathbb Q$, la aplicación abstracta $\nu_{\mathbb Q}:\mathbb N\to\mathbb Q$ coincide con la incrustación $\nu_{\mathbb N}^{\mathbb Q}$ de Definición 3.8.1 — Incrustación canónica de $\mathbb N$ en $\mathbb Q$. La composición

$$
\iota\circ\nu_{\mathbb Q}:\mathbb N\longrightarrow F
$$

satisface

$$
(\iota\circ\nu_{\mathbb Q})(0)
=\iota(0_{\mathbb Q})=0_F
$$

y

$$
\begin{aligned}
(\iota\circ\nu_{\mathbb Q})(S(n))
&=\iota\bigl(\nu_{\mathbb Q}(n)+1_{\mathbb Q}\bigr)\\
&=\iota(\nu_{\mathbb Q}(n))+1_F.
\end{aligned}
$$

Por la unicidad de la aplicación de numerales en Definición 4.1.5 — Aplicación de numerales naturales en un cuerpo ordenado,

$$
\boxed{
\iota\bigl(\nu_{\mathbb N}^{\mathbb Q}(n)\bigr)=\nu_F(n)
}
$$

para todo $n\in\mathbb N$.

Ahora fijemos $z\in\mathbb Z$. Por la forma normal con signo Teorema 2.8.1 — Forma normal con signo existe $n\in\mathbb N$ tal que

$$
z=\iota_{\mathbb N}^{\mathbb Z}(n)
$$

o bien

$$
z=-\iota_{\mathbb N}^{\mathbb Z}(n).
$$

Como

$$
\nu_{\mathbb N}^{\mathbb Q}
=
\jmath_{\mathbb Z}^{\mathbb Q}\circ\iota_{\mathbb N}^{\mathbb Z},
$$

el primer caso da

$$
\iota\bigl(\jmath_{\mathbb Z}^{\mathbb Q}(z)\bigr)
=\nu_F(n)
=\jmath_{\mathbb Z}^{F}(z)
$$

por Proposición 12.1.4 — Compatibilidad aritmética de la copia entera.

En el segundo caso necesitamos únicamente observar que toda aplicación que preserva suma y cero preserva opuestos. En efecto,

$$
\iota(u)+\iota(-u)
=\iota(u+(-u))
=\iota(0_{\mathbb Q})
=0_F,
$$

por lo que $\iota(-u)=-\iota(u)$. Aplicando esto a

$$
u=\jmath_{\mathbb Z}^{\mathbb Q}
\bigl(\iota_{\mathbb N}^{\mathbb Z}(n)\bigr),
$$

y usando que Proposición 3.5.2 — La incrustación preserva la aritmética y Proposición 12.1.4 — Compatibilidad aritmética de la copia entera preservan opuestos, tenemos

$$
\jmath_{\mathbb Z}^{\mathbb Q}(z)=-u,
\qquad
\jmath_{\mathbb Z}^{F}(z)=-\nu_F(n).
$$

Por consiguiente obtenemos nuevamente

$$
\boxed{
\iota\bigl(\jmath_{\mathbb Z}^{\mathbb Q}(z)\bigr)
=\jmath_{\mathbb Z}^{F}(z)
}
$$

para todo $z\in\mathbb Z$.

Sea finalmente $q\in\mathbb Q$. Para este racional fijo tomemos una representación

$$
q=\frac ab,
\qquad
b\neq0_{\mathbb Z}.
$$

Por Definición 3.6.6 — División racional,

$$
q
=
\jmath_{\mathbb Z}^{\mathbb Q}(a)
\bigl(\jmath_{\mathbb Z}^{\mathbb Q}(b)\bigr)^{-1}.
$$

Una aplicación que preserva producto y unidad preserva también inversos de elementos no nulos: si $y\neq0$, entonces

$$
\iota(y)\iota(y^{-1})
=\iota(yy^{-1})
=1_F,
$$

luego $\iota(y^{-1})=\iota(y)^{-1}$. Además $\jmath_{\mathbb Z}^{\mathbb Q}(b)\neq0_{\mathbb Q}$ por la inyectividad de Proposición 3.5.2 — La incrustación preserva la aritmética. Por consiguiente,

$$
\begin{aligned}
\iota(q)
&=\iota\bigl(\jmath_{\mathbb Z}^{\mathbb Q}(a)\bigr)
\left(
\iota\bigl(\jmath_{\mathbb Z}^{\mathbb Q}(b)\bigr)
\right)^{-1}\\
&=\jmath_{\mathbb Z}^{F}(a)
\bigl(\jmath_{\mathbb Z}^{F}(b)\bigr)^{-1}\\
&=\jmath_{\mathbb Q}^{F}(q).
\end{aligned}
$$

Como $q$ era arbitrario, ambas funciones $\mathbb Q\to F$ tienen los mismos valores en todos los argumentos. Por el criterio de igualdad de funciones Proposición 0.6.3 — Criterio de igualdad de funciones,

$$
\iota=\jmath_{\mathbb Q}^{F}.
$$

La existencia de una incrustación está dada por Teorema 12.2.5 — La copia racional es una incrustación de cuerpos ordenados, y acabamos de probar que cualquier otra coincide con ella. ∎

> **Consecuencia estructural.** La palabra «canónica» ya no significa sólo que poseemos una fórmula preferida. La copia racional es canónica en sentido fuerte: está determinada de manera única por la estructura de cuerpo ordenado.

---

### Corolario 12.2.9 — La copia racional de toda completación es la copia canónica

Sea $(E,\iota_E)$ una completación ordenada de $\mathbb Q$. Entonces

$$
\boxed{\iota_E=\jmath_{\mathbb Q}^{E}}
$$

y

$$
\boxed{\iota_E[\mathbb Q]=P_E.}
$$

**Demostración.**

Por Definición 4.8.2 — Completación ordenada de $\mathbb Q$, $\iota_E:\mathbb Q\to E$ es una incrustación de cuerpos ordenados. Teorema 12.2.8 — Unicidad de la incrustación racional implica entonces

$$
\iota_E=\jmath_{\mathbb Q}^{E}.
$$

Sustituyendo esta igualdad en Corolario 12.2.7 — La copia racional es exactamente el subcuerpo primo, obtenemos

$$
\iota_E[\mathbb Q]
=\jmath_{\mathbb Q}^{E}[\mathbb Q]
=P_E.
$$

∎

La sección ha eliminado una ambigüedad que permanecía abierta desde el Capítulo 4. En un cuerpo ordenado no hay varias maneras estructuralmente distintas de insertar los racionales: la copia está forzada por $0$, $1$ y las operaciones del cuerpo. En una completación, por tanto, la incrustación racional que forma parte de los datos no añade libertad adicional.

El siguiente problema es de orden. Para comparar dos completaciones necesitaremos que esa copia racional única sea suficientemente rica dentro del cuerpo: entre dos elementos distintos deberá aparecer un racional. Esa densidad será el objeto de §12.3.

---
