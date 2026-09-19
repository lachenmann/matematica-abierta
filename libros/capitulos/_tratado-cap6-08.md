## 6.8. Leyes de cuerpo {#sec-ta-6-8}

La estructura aditiva está cerrada. Para promover $\mathbb R_D$ a cuerpo debemos demostrar las leyes globales de la multiplicación y su interacción con la suma. Conviene comenzar registrando la compatibilidad aditiva del orden y, después, demostrar conmutatividad, asociatividad y distributividad primero en el cono positivo.

### Proposición 6.8.1 — Invariancia del orden por traslación

Para $\alpha,\beta,\gamma\in\mathbb R_D$,

$$
\boxed{
\alpha\leq_D\beta
\iff
\alpha+_D\gamma\leq_D\beta+_D\gamma,
}
$$

y

$$
\boxed{
\alpha<_D\beta
\iff
\alpha+_D\gamma<_D\beta+_D\gamma.
}
$$

**Demostración.**

Si $\alpha\leq_D\beta$, entonces $\alpha\subseteq\beta$. Todo elemento $x=a+c$ de $\alpha+_D\gamma$ tiene $a\in\alpha\subseteq\beta$ y $c\in\gamma$, de modo que $x\in\beta+_D\gamma$. Así la suma preserva $\leq_D$.

Recíprocamente, si $\alpha+_D\gamma\leq_D\beta+_D\gamma$, aplicamos la implicación ya probada sumando $-_D\gamma$ a ambos miembros. La asociatividad, la ley del opuesto y el neutro reducen la desigualdad resultante a $\alpha\leq_D\beta$.

Para el orden estricto, si $\alpha<_D\beta$, la parte no estricta ya probada da $\alpha+_D\gamma\leq_D\beta+_D\gamma$. La igualdad de estos dos miembros implicaría $\alpha=\beta$ por cancelación, contradicción. La recíproca se obtiene trasladando por $-_D\gamma$. ∎

### Corolario 6.8.2 — Signo de una diferencia

Para $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{
\alpha<_D\beta
\iff
0_D<_D\beta-_D\alpha.
}
$$

**Demostración.**

Trasladamos $\alpha<_D\beta$ por $-_D\alpha$ y usamos $\alpha-_D\alpha=0_D$. La recíproca es la misma equivalencia leída en sentido inverso. ∎

### Teorema 6.8.3 — Conmutatividad del producto positivo

Si $\alpha,\beta\in\mathbb R_D^{>0}$, entonces

$$
\boxed{\alpha\cdot_D^+\beta=\beta\cdot_D^+\alpha.}
$$

**Demostración.**

$x\in\alpha\cdot_D^+\beta$ significa que existen $a\in\alpha_{>0}$ y $b\in\beta_{>0}$ con $x<ab$. La conmutatividad del producto racional da $ab=ba$, y los mismos testigos intercambiados muestran $x\in\beta\cdot_D^+\alpha$. La recíproca es idéntica. ∎

### Teorema 6.8.4 — Asociatividad del producto positivo

Para $\alpha,\beta,\gamma\in\mathbb R_D^{>0}$,

$$
\boxed{
(\alpha\cdot_D^+\beta)\cdot_D^+\gamma
=
\alpha\cdot_D^+(\beta\cdot_D^+\gamma).
}
$$

**Demostración.**

Sea $x\in(\alpha\cdot_D^+\beta)\cdot_D^+\gamma$. Existen $u>0$ y $c\in\gamma_{>0}$ tales que

$$
u\in\alpha\cdot_D^+\beta,
\qquad
x<uc.
$$

Existen $a\in\alpha_{>0}$ y $b\in\beta_{>0}$ con $u<ab$. Como $c>0$,

$$
x<uc<abc.
$$

Si $x\le0$, elegimos por densidad cualquier $v$ con $0<v<bc$. Entonces $v\in\beta\cdot_D^+\gamma$ y $x<0<av$, por lo que $x\in\alpha\cdot_D^+(\beta\cdot_D^+\gamma)$.

Si $x>0$, de $x<abc$ y $a>0$ se sigue $x/a<bc$. Por densidad elegimos

$$
\frac xa<v<bc.
$$

Entonces $v>0$, $v\in\beta\cdot_D^+\gamma$ y $x<av$. Así obtenemos la primera inclusión.

Para la inclusión inversa, sea $x\in\alpha\cdot_D^+(\beta\cdot_D^+\gamma)$. Existen $a\in\alpha_{>0}$ y $v>0$ con

$$
v\in\beta\cdot_D^+\gamma,
\qquad
x<av.
$$

Existen $b\in\beta_{>0}$ y $c\in\gamma_{>0}$ con $v<bc$. Por tanto

$$
x<av<abc.
$$

Si $x\le0$, por densidad elegimos $0<u<ab$. Entonces $u\in\alpha\cdot_D^+\beta$ y $x<0<uc$, de modo que $x$ pertenece al miembro izquierdo.

Si $x>0$, de $x<abc$ y $c>0$ se obtiene $x/c<ab$. Por densidad elegimos

$$
\frac xc<u<ab.
$$

Entonces $u>0$, $u\in\alpha\cdot_D^+\beta$ y $x<uc$. Así $x\in(\alpha\cdot_D^+\beta)\cdot_D^+\gamma$.

Las dos inclusiones prueban la igualdad. ∎

### Teorema 6.8.5 — Distributividad positiva

Si $\alpha,\beta,\gamma\in\mathbb R_D^{>0}$, entonces

$$
\boxed{
\alpha\cdot_D^+(\beta+_D\gamma)
=
(\alpha\cdot_D^+\beta)+_D(\alpha\cdot_D^+\gamma).
}
$$

**Demostración.**

Como $0\in\beta$ y $0\in\gamma$, tenemos $0=0+0\in\beta+_D\gamma$; por Lema 6.4.2 — Caracterizaciones de la positividad, esta suma es positiva.

Sea

$$
x\in\alpha\cdot_D^+(\beta+_D\gamma).
$$

Existen $a\in\alpha_{>0}$ y $u\in(\beta+_D\gamma)_{>0}$ con

$$
x<au.
$$

Por definición de la suma existe una representación $u=b_0+c_0$ con $b_0\in\beta$ y $c_0\in\gamma$. Como $u>0$, no pueden ser ambos no positivos. Queremos una representación con ambos términos positivos.

Si $b_0>0$ y $c_0>0$, tomamos $b=b_0$, $c=c_0$. Supongamos $b_0\le0$; entonces necesariamente $c_0>0$. Como $\beta$ es positiva, existe $d\in\beta$ con $d>0$. Elegimos $b\in\mathbb Q$ con

$$
0<b<\min\{u,d\}.
$$

Esta elección puede hacerse por densidad, considerando primero el menor de los dos racionales positivos $u,d$. Como $b<d$ y $d\in\beta$, la clausura inferior da $b\in\beta$. Definimos $c:=u-b$. Entonces $c>0$. Además $b>b_0$, por lo que

$$
c=u-b<u-b_0=c_0.
$$

Como $c_0\in\gamma$, se sigue $c\in\gamma$. El caso $c_0\le0$ es simétrico. Hemos obtenido siempre

$$
u=b+c,
\qquad
b\in\beta_{>0},
\quad
c\in\gamma_{>0}.
$$

Así

$$
x<a(b+c)=ab+ac.
$$

De $x-ac<ab$, la densidad proporciona $y$ con

$$
x-ac<y<ab.
$$

Pongamos $z:=x-y$. Entonces $y\in\alpha\cdot_D^+\beta$, mientras que $z<ac$ implica $z\in\alpha\cdot_D^+\gamma$. Como $x=y+z$,

$$
x\in(\alpha\cdot_D^+\beta)+_D(\alpha\cdot_D^+\gamma).
$$

Esto prueba la primera inclusión.

Recíprocamente, sea

$$
x\in(\alpha\cdot_D^+\beta)+_D(\alpha\cdot_D^+\gamma).
$$

Existen $y,z$ tales que

$$
x=y+z,
\qquad
y\in\alpha\cdot_D^+\beta,
\qquad
z\in\alpha\cdot_D^+\gamma.
$$

Por definición del producto positivo existen

$$
a_1,a_2\in\alpha_{>0},
\qquad
b\in\beta_{>0},
\qquad
c\in\gamma_{>0}
$$

con

$$
y<a_1b,
\qquad
z<a_2c.
$$

Entre $a_1$ y $a_2$, sea $m$ el mayor. Como $m$ es uno de ellos, $m\in\alpha$. La ausencia de máximo proporciona $a\in\alpha$ con $m<a$; en particular $a>0$, $a_1<a$ y $a_2<a$. Como $b,c>0$,

$$
x=y+z<a_1b+a_2c<ab+ac=a(b+c).
$$

Además $b+c\in\beta+_D\gamma$ y $b+c>0$. Por tanto

$$
x\in\alpha\cdot_D^+(\beta+_D\gamma).
$$

La doble inclusión prueba la identidad distributiva. ∎

### Lema 6.8.6 — Opuesto de una suma

Para $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{
-_D(\alpha+_D\beta)
=
(-_D\alpha)+_D(-_D\beta).
}
$$

**Demostración.**

Por asociatividad y conmutatividad,

$$
(\alpha+_D\beta)+_D\bigl((-_D\alpha)+_D(-_D\beta)\bigr)
=
(\alpha+_D(-_D\alpha))+_D(\beta+_D(-_D\beta))
=0_D.
$$

La unicidad del inverso aditivo da la igualdad. ∎

### Lema 6.8.7 — Reglas de signo para el producto

Para $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{(-_D\alpha)\cdot_D\beta=-_D(\alpha\cdot_D\beta),}
$$

$$
\boxed{\alpha\cdot_D(-_D\beta)=-_D(\alpha\cdot_D\beta),}
$$

y

$$
\boxed{(-_D\alpha)\cdot_D(-_D\beta)=\alpha\cdot_D\beta.}
$$

**Demostración.**

Si alguno de los factores es $0_D$, las identidades se reducen a $-_D0_D=0_D$. Supongamos ambos no nulos. Por tricotomía hay cuatro combinaciones de signos. En cada una, la definición Definición 6.5.4 — Producto signado candidato reduce ambos miembros al mismo producto positivo, con o sin un único opuesto exterior.

Por ejemplo, si $\alpha,\beta>_D0_D$,

$$
(-_D\alpha)\cdot_D\beta
=-_D(\alpha\cdot_D^+\beta)
=-_D(\alpha\cdot_D\beta).
$$

Si $\alpha>_D0_D>_D\beta$,

$$
(-_D\alpha)\cdot_D\beta
=\alpha\cdot_D^+(-_D\beta),
$$

mientras

$$
-_D(\alpha\cdot_D\beta)
=-_D\bigl(-_D(\alpha\cdot_D^+(-_D\beta))\bigr)
=\alpha\cdot_D^+(-_D\beta)
$$

por involutividad. Los otros signos se verifican del mismo modo y las otras dos fórmulas son las mismas verificaciones con el factor negado correspondiente. ∎

### Proposición 6.8.8 — Distributividad para un factor positivo

Si $\alpha>_D0_D$, entonces, para $\beta,\gamma\in\mathbb R_D$,

$$
\boxed{
\alpha\cdot_D(\beta+_D\gamma)
=
\alpha\cdot_D\beta+_D\alpha\cdot_D\gamma.
}
$$

**Demostración.**

Si alguno de $\beta,\gamma$ es cero, la identidad es inmediata. Si ambos son positivos, es Teorema 6.8.5 — Distributividad positiva.

Si ambos son negativos, escribimos $\beta=-_DB$ y $\gamma=-_DC$ con $B,C>_D0_D$. Por Lema 6.8.6 — Opuesto de una suma,

$$
\beta+_D\gamma=-_D(B+_DC).
$$

Las reglas de signo y la distributividad positiva dan

$$
\begin{aligned}
\alpha(\beta+\gamma)
&=-_D\bigl(\alpha(B+C)\bigr)\\
&=-_D(\alpha B+\alpha C)\\
&=(-_D\alpha B)+(-_D\alpha C)\\
&=\alpha\beta+\alpha\gamma.
\end{aligned}
$$

Supongamos ahora $\beta>_D0_D>_D\gamma$ y pongamos $C:=-_D\gamma>_D0_D$.

Si $\beta=C$, entonces $\beta+\gamma=0_D$ y ambos miembros son cero.

Si $C<_D\beta$, definimos $D:=\beta-_DC$. Por Corolario 6.8.2 — Signo de una diferencia, $D>_D0_D$, y $C+_DD=\beta$. La distributividad positiva da

$$
\alpha\beta=\alpha C+_D\alpha D.
$$

Por cancelación aditiva,

$$
\alpha D=\alpha\beta-_D\alpha C.
$$

Pero $\beta+\gamma=D$ y $\alpha\gamma=-_D(\alpha C)$ por las reglas de signo; por tanto la identidad requerida vale.

Si $\beta<_DC$, definimos $D:=C-_D\beta>_D0_D$. Entonces $C=\beta+_DD$ y $\beta+\gamma=-_DD$. La distributividad positiva produce

$$
\alpha C=\alpha\beta+_D\alpha D.
$$

Por cancelación,

$$
\alpha\beta-_D\alpha C=-_D(\alpha D),
$$

que es precisamente

$$
\alpha\beta+_D\alpha\gamma
=
\alpha(\beta+\gamma).
$$

El caso $\beta<_D0_D<_D\gamma$ se obtiene intercambiando $\beta$ y $\gamma$ y usando la conmutatividad de la suma. ∎

### Teorema 6.8.9 — Conmutatividad de la multiplicación

Para $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{\alpha\cdot_D\beta=\beta\cdot_D\alpha.}
$$

**Demostración.**

Si alguno es cero, es inmediato. Si ambos son positivos, es Teorema 6.8.3 — Conmutatividad del producto positivo. Si ambos son negativos, la definición reduce ambos miembros a

$$
(-_D\alpha)\cdot_D^+(-_D\beta)
$$

y su versión con factores intercambiados, iguales por Teorema 6.8.3 — Conmutatividad del producto positivo. Si tienen signos opuestos, ambos productos son el opuesto del mismo producto positivo, nuevamente por Teorema 6.8.3 — Conmutatividad del producto positivo. ∎

### Teorema 6.8.10 — Asociatividad de la multiplicación

Para $\alpha,\beta,\gamma\in\mathbb R_D$,

$$
\boxed{(\alpha\cdot_D\beta)\cdot_D\gamma
=\alpha\cdot_D(\beta\cdot_D\gamma).}
$$

**Demostración.**

Si alguno de los tres factores es cero, ambos miembros son cero. Supongamos los tres no nulos. A cada uno asociamos su parte positiva: si es positivo, lo dejamos igual; si es negativo, tomamos su opuesto. Obtenemos $A,B,C>_D0_D$.

La definición signada y Lema 6.8.7 — Reglas de signo para el producto muestran que ambos miembros tienen el mismo signo: positivo si hay un número par de factores negativos y negativo si hay un número impar. Su núcleo positivo es, respectivamente,

$$
(A\cdot_D^+B)\cdot_D^+C
$$

y

$$
A\cdot_D^+(B\cdot_D^+C).
$$

Estos núcleos son iguales por Teorema 6.8.4 — Asociatividad del producto positivo. Con el mismo signo exterior, los productos generales son iguales. ∎

### Teorema 6.8.11 — Distributividad general

Para $\alpha,\beta,\gamma\in\mathbb R_D$,

$$
\boxed{
\alpha\cdot_D(\beta+_D\gamma)
=
\alpha\cdot_D\beta+_D\alpha\cdot_D\gamma.
}
$$

También

$$
\boxed{
(\beta+_D\gamma)\cdot_D\alpha
=
\beta\cdot_D\alpha+_D\gamma\cdot_D\alpha.
}
$$

**Demostración.**

Si $\alpha=0_D$, es inmediato. Si $\alpha>_D0_D$, la primera igualdad es Proposición 6.8.8 — Distributividad para un factor positivo.

Si $\alpha<_D0_D$, pongamos $A:=-_D\alpha>_D0_D$. Entonces $\alpha=-_DA$, y

$$
\begin{aligned}
\alpha(\beta+\gamma)
&=-_D\bigl(A(\beta+\gamma)\bigr)\\
&=-_D(A\beta+A\gamma)\\
&=(-_DA\beta)+(-_DA\gamma)\\
&=\alpha\beta+\alpha\gamma,
\end{aligned}
$$

usando Proposición 6.8.8 — Distributividad para un factor positivo, Lema 6.8.6 — Opuesto de una suma y las reglas de signo. La distributividad por la derecha se sigue de Teorema 6.8.9 — Conmutatividad de la multiplicación. ∎

### Teorema 6.8.12 — $\mathbb R_D$ es un cuerpo

La estructura

$$
\boxed{(\mathbb R_D,+_D,\cdot_D,0_D,1_D)}
$$

es un cuerpo.

**Demostración.**

La estructura aditiva es un grupo abeliano por Teorema 6.3.10 — Estructura de grupo abeliano aditivo. La multiplicación es conmutativa y asociativa por Teorema 6.8.9 — Conmutatividad de la multiplicación y Teorema 6.8.10 — Asociatividad de la multiplicación; $1_D$ es neutro por Teorema 6.6.5 — Leyes de la unidad multiplicativa; la distributividad es Teorema 6.8.11 — Distributividad general; $0_D\neq1_D$ por Proposición 6.6.2 — La unidad de Dedekind es estrictamente positiva; y todo elemento no nulo posee inverso multiplicativo por Teorema 6.7.10 — Ley del inverso multiplicativo. Son exactamente las leyes de cuerpo fijadas por Convención 3.6.7 — Terminología de cuerpo. ∎

### Proposición 6.8.13 — Compatibilidad del orden de Dedekind con las operaciones

El orden $\le_D$ satisface:

1. si $\alpha\le_D\beta$, entonces
   $$
   \alpha+_D\gamma\le_D\beta+_D\gamma;
   $$
2. si $0_D\le_D\alpha$ y $0_D\le_D\beta$, entonces
   $$
   \boxed{0_D\le_D\alpha\cdot_D\beta.}
   $$

**Demostración.**

La primera afirmación está contenida en Proposición 6.8.1 — Invariancia del orden por traslación. Para la segunda, por tricotomía cada factor no negativo es cero o estrictamente positivo. Si alguno es cero, el producto es $0_D$. Si ambos son positivos, Proposición 6.5.5 — Clausura y regla de signos del producto candidato da un producto estrictamente positivo. En ambos casos $0_D\le_D\alpha\beta$. ∎

### Teorema 6.8.14 — El modelo de Dedekind es un cuerpo ordenado

La estructura

$$
\boxed{(\mathbb R_D,+_D,\cdot_D,\le_D)}
$$

es un cuerpo ordenado.

**Demostración.**

Teorema 6.8.12 — $\mathbb R_D$ es un cuerpo da la estructura de cuerpo, Teorema 5.4.2 — La inclusión ordena totalmente las cortaduras el orden total y Proposición 6.8.13 — Compatibilidad del orden de Dedekind con las operaciones la compatibilidad del orden con las operaciones. Son exactamente las condiciones de Definición 4.1.1 — Cuerpo ordenado. ∎

### Corolario 6.8.15 — La aplicación canónica es una incrustación de cuerpos ordenados

La aplicación

$$
\boxed{\iota_D:\mathbb Q\hookrightarrow\mathbb R_D}
$$

es una incrustación de cuerpos ordenados. En particular,

$$
\begin{aligned}
\iota_D(p+q)&=\iota_D(p)+_D\iota_D(q),\\
\iota_D(pq)&=\iota_D(p)\cdot_D\iota_D(q),\\
\iota_D(0_{\mathbb Q})&=0_D,\\
\iota_D(1_{\mathbb Q})&=1_D,\\
p\le q&\iff\iota_D(p)\le_D\iota_D(q).
\end{aligned}
$$

**Demostración.**

La suma se preserva por Proposición 6.1.5 — La adición de Dedekind prolonga la suma racional, el producto por Proposición 6.5.7 — La multiplicación de Dedekind prolonga la multiplicación racional, las constantes por Definición 6.2.1 — Cero de Dedekind y Definición 6.6.1 — Unidad de Dedekind, el orden se preserva y refleja por Proposición 5.5.2 — Caracterización del orden mediante la aplicación canónica, y la inyectividad es Corolario 5.5.3 — $\iota_D$ es inyectiva y preserva y refleja el orden estricto. Como ambos lados son cuerpos ordenados, se cumplen las condiciones de Definición 4.8.1 — Incrustación de cuerpos ordenados. ∎

### Corolario 6.8.16 — Compatibilidad con los inversos racionales

Si $p\in\mathbb Q$ y $p\neq0_{\mathbb Q}$, entonces

$$
\boxed{
\iota_D(p^{-1})=\iota_D(p)^{-1_D}.
}
$$

**Demostración.**

Por Proposición 3.6.5 — Ley del inverso multiplicativo, $pp^{-1}=1_{\mathbb Q}$. Como $\iota_D$ preserva producto y unidad,

$$
\iota_D(p)\cdot_D\iota_D(p^{-1})=1_D.
$$

La inyectividad y $p\neq0$ implican $\iota_D(p)\neq0_D$, de modo que Teorema 6.7.10 — Ley del inverso multiplicativo da

$$
\iota_D(p)\cdot_D\iota_D(p)^{-1_D}=1_D.
$$

Multiplicamos la primera igualdad por $\iota_D(p)^{-1_D}$ y usamos asociatividad, conmutatividad, la ley del inverso y la unidad:

$$
\begin{aligned}
\iota_D(p^{-1})
&=1_D\cdot_D\iota_D(p^{-1})\\
&=(\iota_D(p)^{-1_D}\cdot_D\iota_D(p))\cdot_D\iota_D(p^{-1})\\
&=\iota_D(p)^{-1_D}\cdot_D(\iota_D(p)\cdot_D\iota_D(p^{-1}))\\
&=\iota_D(p)^{-1_D}\cdot_D1_D\\
&=\iota_D(p)^{-1_D}.
\end{aligned}
$$

∎

**Compatibilidad con la división racional.** Si $p,q\in\mathbb Q$ y $q\neq0_{\mathbb Q}$, las propiedades de la incrustación y el corolario anterior dan

$$
\begin{aligned}
\iota_D(p/q)
&=\iota_D(pq^{-1})\\
&=\iota_D(p)\cdot_D\iota_D(q^{-1})\\
&=\iota_D(p)\cdot_D\iota_D(q)^{-1_D}\\
&=\iota_D(p)\div_D\iota_D(q).
\end{aligned}
$$

El denominador de la última expresión es no nulo por la inyectividad de $\iota_D$. Así, la división derivada prolonga exactamente la división ya definida sobre $\mathbb Q$.
