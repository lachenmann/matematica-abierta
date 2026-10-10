## 6.3. Opuestos de Dedekind {#sec-ta-6-3}

Negar directamente los elementos de una cortadura produce esencialmente un lado superior, no otra cortadura inferior. Tampoco basta negar el complemento: para $\delta_p$ se obtendría un conjunto con frontera incluida. El opuesto correcto deberá excluir nuevamente la frontera.

### Lema 6.3.1 — Aproximación racional de la frontera

Sean $\alpha\in\mathbb R_D$ y $h\in\mathbb Q$ con $0<h$. Entonces existe $a\in\alpha$ tal que

$$
\boxed{a+h\notin\alpha.}
$$

**Demostración.**

Supongamos, por contradicción, que

$$
\forall a\in\alpha\;(a+h\in\alpha).
$$

Como $\alpha$ es no vacía y propia, existen $a_0\in\alpha$ y $u\notin\alpha$. Afirmamos por inducción que

$$
a_0+\widehat n h\in\alpha
\qquad(n\in\mathbb N),
$$

donde $\widehat n$ es la imagen canónica de $n$ en $\mathbb Q$. Para $n=0$ es inmediato. Si vale para $n$, la hipótesis de contradicción da

$$
a_0+\widehat n h+h\in\alpha,
$$

y las propiedades de la incrustación natural identifican este racional con $a_0+\widehat{n+1}h$.

Por la arquimedianidad de $\mathbb Q$ existe $n\in\mathbb N$ tal que

$$
\frac{u-a_0}{h}<\widehat n.
$$

Como $h>0$,

$$
u<a_0+\widehat n h.
$$

Pero el miembro derecho pertenece a $\alpha$; por clausura inferior se seguiría $u\in\alpha$, contradicción. Luego existe $a\in\alpha$ con $a+h\notin\alpha$. ∎

Ninguna cortadura puede permanecer cerrada bajo traslaciones indefinidas por un paso racional positivo. En particular, su frontera puede aproximarse desde dentro y desde fuera con precisión racional arbitraria.

### Definición 6.3.2 — Candidato a opuesto de una cortadura

Para $\alpha\in\mathbb R_D$ definimos

$$
\boxed{
\Omega_D(\alpha)
:=
\{q\in\mathbb Q:\exists s\in\mathbb Q\;(s\notin\alpha\land q<-s)\}.
}
$$

El conjunto existe por Separación. La desigualdad estricta $q<-s$ es esencial: evita incorporar la frontera.

### Proposición 6.3.3 — El candidato a opuesto es una cortadura

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{\Omega_D(\alpha)\in\mathbb R_D.}
$$

**Demostración.**

**No vaciedad.** Como $\alpha$ es propia, existe $s\notin\alpha$. Entonces $-s-1<-s$, por lo que $-s-1\in\Omega_D(\alpha)$.

**Propiedad.** Como $\alpha$ es no vacía, existe $a\in\alpha$. Afirmamos que $-a\notin\Omega_D(\alpha)$. Si no, existiría $s\notin\alpha$ con $-a<-s$, es decir, $s<a$. La clausura inferior daría $s\in\alpha$, contradicción.

**Clausura inferior.** Si $q\in\Omega_D(\alpha)$ mediante un testigo $s\notin\alpha$ con $q<-s$ y $r<q$, entonces $r<-s$; el mismo $s$ demuestra $r\in\Omega_D(\alpha)$.

**Ausencia de máximo.** Si $q<-s$ con $s\notin\alpha$, la densidad racional proporciona $r$ con

$$
q<r<-s.
$$

El mismo testigo $s$ da $r\in\Omega_D(\alpha)$. ∎

### Definición 6.3.4 — Opuesto de Dedekind

La asignación anterior determina una función

$$
\boxed{
-_D:\mathbb R_D\longrightarrow\mathbb R_D,
\qquad
-_D\alpha:=\Omega_D(\alpha).
}
$$

Por tanto,

$$
q\in-_D\alpha
\iff
\exists s\in\mathbb Q\;(s\notin\alpha\land q<-s).
$$

### Proposición 6.3.5 — Ley del opuesto aditivo

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{\alpha+_D(-_D\alpha)=0_D.}
$$

**Demostración.**

Sea $x\in\alpha+_D(-_D\alpha)$. Existen $a\in\alpha$ y $b\in-_D\alpha$ con $x=a+b$. Existe a su vez $s\notin\alpha$ tal que $b<-s$. Por Lema 6.1.1 — Todo punto exterior domina una cortadura, $a<s$. Así

$$
x=a+b<a-s<0,
$$

y $x\in0_D$. Luego

$$
\alpha+_D(-_D\alpha)\subseteq0_D.
$$

Recíprocamente, sea $x\in0_D$, de modo que $x<0$. Por densidad elegimos $h$ con

$$
0<h<-x.
$$

Lema 6.3.1 — Aproximación racional de la frontera proporciona $a\in\alpha$ tal que $s:=a+h\notin\alpha$. Pongamos $b:=x-a$. Como $x<-h$,

$$
b=x-a<-a-h=-s.
$$

Por tanto $b\in-_D\alpha$, y $x=a+b$. Así $x\in\alpha+_D(-_D\alpha)$. La doble inclusión da la igualdad. ∎

### Corolario 6.3.6 — El opuesto prolonga el opuesto racional

Para todo $p\in\mathbb Q$,

$$
\boxed{-_D\iota_D(p)=\iota_D(-p).}
$$

Equivalentemente, $-_D\delta_p=\delta_{-p}$.

**Demostración.**

Si $q\in-_D\delta_p$, existe $s\notin\delta_p$ con $q<-s$. La primera condición equivale a $p\le s$; al cambiar signos, $-s\le-p$, y por tanto $q<-p$. Así $q\in\delta_{-p}$.

Recíprocamente, si $q<-p$, tomamos $s=p$. Como $p\notin\delta_p$ y $q<-s$, la definición da $q\in-_D\delta_p$. Por extensionalidad, $-_D\delta_p=\delta_{-p}$. ∎

### Teorema 6.3.7 — Asociatividad de la suma de Dedekind

Para $\alpha,\beta,\gamma\in\mathbb R_D$,

$$
\boxed{(\alpha+_D\beta)+_D\gamma=\alpha+_D(\beta+_D\gamma).}
$$

**Demostración.**

Si $x\in(\alpha+_D\beta)+_D\gamma$, existen $a\in\alpha$, $b\in\beta$ y $c\in\gamma$ tales que

$$
x=(a+b)+c=a+(b+c),
$$

por asociatividad racional. Como $b+c\in\beta+_D\gamma$, se sigue $x\in\alpha+_D(\beta+_D\gamma)$. La inclusión inversa se obtiene leyendo el mismo argumento desde una representación $x=a+(b+c)$ y usando la asociatividad racional en sentido inverso. ∎

### Teorema 6.3.8 — Conmutatividad de la suma de Dedekind

Para $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{\alpha+_D\beta=\beta+_D\alpha.}
$$

**Demostración.**

Si $x=a+b$ con $a\in\alpha$ y $b\in\beta$, la conmutatividad racional da $x=b+a$, por lo que $x\in\beta+_D\alpha$. La inclusión contraria es idéntica. ∎

### Corolario 6.3.9 — Ley bilateral del opuesto

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{\alpha+_D(-_D\alpha)=0_D=(-_D\alpha)+_D\alpha.}
$$

**Demostración.**

La primera igualdad es Proposición 6.3.5 — Ley del opuesto aditivo; la segunda se obtiene por conmutatividad. ∎

### Teorema 6.3.10 — Estructura de grupo abeliano aditivo

La estructura

$$
\boxed{(\mathbb R_D,+_D,0_D)}
$$

es un grupo abeliano, y el inverso aditivo de $\alpha$ es $-_D\alpha$.

**Demostración.**

La clausura es Proposición 6.1.3 — La suma de dos cortaduras es una cortadura, la asociatividad Teorema 6.3.7 — Asociatividad de la suma de Dedekind, el neutro Proposición 6.2.2 — El cero de Dedekind es neutro para la suma, los inversos Corolario 6.3.9 — Ley bilateral del opuesto y la conmutatividad Teorema 6.3.8 — Conmutatividad de la suma de Dedekind. Son exactamente las leyes de un grupo abeliano. ∎

### Proposición 6.3.11 — Cancelación aditiva en $\mathbb R_D$

Si

$$
\alpha+_D\gamma=\beta+_D\gamma,
$$

entonces $\alpha=\beta$. Análogamente vale la cancelación por la izquierda.

**Demostración.**

Sumamos $-_D\gamma$ a ambos miembros y usamos asociatividad, la ley del opuesto y el neutro:

$$
\alpha
=(\alpha+_D\gamma)+_D(-_D\gamma)
=(\beta+_D\gamma)+_D(-_D\gamma)
=\beta.
$$

La cancelación por la izquierda es análoga. ∎

En particular, el inverso aditivo es único.

### Definición 6.3.12 — Sustracción de Dedekind

Para $\alpha,\beta\in\mathbb R_D$ definimos

$$
\boxed{\alpha-_D\beta:=\alpha+_D(-_D\beta).}
$$

### Corolario 6.3.13 — La sustracción prolonga la sustracción racional

Para $p,q\in\mathbb Q$,

$$
\boxed{\iota_D(p-q)=\iota_D(p)-_D\iota_D(q).}
$$

**Demostración.**

Como $p-q=p+(-q)$,

$$
\iota_D(p-q)
=\iota_D(p)+_D\iota_D(-q)
=\iota_D(p)+_D(-_D\iota_D(q))
=\iota_D(p)-_D\iota_D(q).
$$

∎
