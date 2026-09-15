## 3.8. Incrustación natural, densidad y propiedad arquimediana {#sec-ta-3-8}

Una vez construido el orden racional y comprobada su compatibilidad con las operaciones, podemos identificar cómo se sitúan canónicamente los naturales dentro de $\mathbb Q$ y demostrar dos propiedades decisivas del orden racional: entre dos racionales distintos siempre hay otro racional, y todo racional queda finalmente por debajo de algún natural canónicamente incorporado.

### Definición 3.8.1 — Incrustación canónica de $\mathbb N$ en $\mathbb Q$ {#ta-incrustacion-natural-nq}

Definimos

$$
\boxed{
\nu_{\mathbb N}^{\mathbb Q}
:=
\jmath_{\mathbb Z}^{\mathbb Q}
\circ
\iota_{\mathbb N}^{\mathbb Z}.
}
$$

Así, para $n\in\mathbb N$,

$$
\boxed{
\nu(n)
=
\frac{\iota(n)}{1_{\mathbb Z}}.
}
$$

### Corolario 3.8.2 — Propiedades de la incrustación natural {#ta-propiedades-incrustacion-natural-nq}

La función

$$
\nu:\mathbb N\to\mathbb Q
$$

es inyectiva y preserva $0$, $1$, suma, producto y orden; además refleja el orden.

**Demostración.**  
Es la composición de las incrustaciones

$$
\iota:\mathbb N\to\mathbb Z
\qquad\text{y}\qquad
\jmath:\mathbb Z\to\mathbb Q.
$$

La primera es inyectiva y preserva $0$, $1$, suma, producto y orden por los resultados del Capítulo 2. La segunda es inyectiva y preserva $0$, $1$, suma, producto y opuestos por la [Proposición 3.5.2](#ta-incrustacion-entera-preserva-aritmetica), y preserva y refleja el orden por la [Proposición 3.7.8](#ta-incrustacion-zq-preserva-refleja-orden). Por composición, $\nu$ posee las propiedades indicadas. ∎

### Teorema 3.8.3 — Densidad del orden racional {#ta-densidad-orden-racional}

*Glosario: [densidad del orden racional](../otros/tratado-de-analisis-glosario.md#gl-densidad-orden-racional)*

Si $x,y\in\mathbb Q$ y

$$
x<_{\mathbb Q}y,
$$

existe $z\in\mathbb Q$ tal que

$$
\boxed{
x<_{\mathbb Q}z<_{\mathbb Q}y.
}
$$

**Demostración.**  
Por el [Lema 3.7.1](#ta-representante-denominador-positivo), tomemos representaciones con denominador positivo

$$
x=\frac ab,
\qquad
y=\frac cd,
\qquad
b,d>0.
$$

Como $x<y$, el [criterio estricto de comparación cruzada](#ta-criterio-estricto-orden-racional) da

$$
ad<bc.
$$

Definimos el **mediante**

$$
z:=\frac{a+c}{b+d}.
$$

El denominador $b+d$ es positivo. En efecto, de $0<d$ obtenemos $0\leq d$, y por compatibilidad con la suma,

$$
b=b+0\leq b+d.
$$

Si hubiera igualdad $b=b+d$, la cancelación aditiva daría $d=0$, contradicción. Así

$$
b<b+d.
$$

Como $0<b$, por transitividad,

$$
0<b+d.
$$

Para comparar $x$ con $z$, por el criterio estricto de comparación cruzada basta demostrar

$$
a(b+d)<b(a+c).
$$

Tras expandir, esta desigualdad es

$$
ab+ad<ab+bc,
$$

que se sigue de $ad<bc$ por invariancia estricta bajo traslación: la invariancia del orden entero por traslación preserva la desigualdad no estricta, y la cancelación aditiva impide que aparezca una igualdad después de sumar $ab$ a ambos miembros.

Análogamente,

$$
(a+c)d<(b+d)c
$$

equivale a

$$
ad+cd<bc+cd,
$$

y nuevamente se sigue de $ad<bc$ por el mismo argumento de traslación estricta.

Los denominadores $b$, $d$ y $b+d$ son positivos. Por tanto el criterio estricto convierte estas dos desigualdades cruzadas en

$$
x<z<y.
$$

∎

### Definición 3.8.4 — Propiedad arquimediana de $\mathbb Q$ {#ta-propiedad-arquimediana-q}

*Glosario: [propiedad arquimediana](../otros/tratado-de-analisis-glosario.md#gl-propiedad-arquimediana)*

Diremos que $\mathbb Q$ satisface la **propiedad arquimediana respecto de su copia canónica de $\mathbb N$** si

$$
\boxed{
\forall q\in\mathbb Q\;
\exists n\in\mathbb N
\quad
q<_{\mathbb Q}\nu(n).
}
$$

### Teorema 3.8.5 — $\mathbb Q$ es arquimediano {#ta-q-arquimediano}

$\mathbb Q$ satisface la propiedad arquimediana de la Definición 3.8.4.

**Demostración.**  
Sea $q\in\mathbb Q$. Por el [Lema 3.7.1](#ta-representante-denominador-positivo) podemos escribir

$$
q=\frac a{\iota(k)}
$$

con $k\in\mathbb N$, $k\neq0$, y

$$
\iota(k)>0.
$$

Si

$$
a\leq0_{\mathbb Z},
$$

entonces

$$
a<\iota(k)=\iota(k)\iota(1),
$$

porque $\iota(k)>0$ y $\iota(k)=\iota(k)\iota(1)$. Como ambos denominadores son positivos, el criterio estricto de comparación cruzada convierte esta desigualdad en

$$
q<\nu(1).
$$

Supongamos ahora

$$
a>0.
$$

Por la forma normal con signo de los enteros, existe $m\in\mathbb N$, $m\neq0$, tal que

$$
a=\iota(m).
$$

Tomemos

$$
n:=S(m).
$$

Como $k\neq0$, el resultado previamente demostrado de que todo natural no nulo es sucesor proporciona $r\in\mathbb N$ con

$$
k=S(r).
$$

Por las leyes de la suma natural,

$$
k=1+r.
$$

Entonces

$$
kn=(1+r)n=n+rn,
$$

de modo que

$$
n\leq kn.
$$

Además

$$
m<S(m)=n.
$$

Por transitividad,

$$
m<kn.
$$

La incrustación $\iota:\mathbb N\to\mathbb Z$ preserva el orden no estricto y es inyectiva; por tanto preserva también esta desigualdad estricta:

$$
a=\iota(m)<\iota(kn).
$$

Como $\iota$ preserva productos,

$$
\iota(kn)=\iota(k)\iota(n).
$$

El denominador $\iota(k)$ es positivo, así que el criterio estricto de comparación cruzada da

$$
q
=
\frac{\iota(m)}{\iota(k)}
<
\frac{\iota(n)}{1}
=
\nu(n).
$$

En ambos casos se encuentra el natural requerido. ∎

---
