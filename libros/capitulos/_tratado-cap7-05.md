## 7.5. Consecuencias inmediatas {#sec-ta-7-5}

### Corolario 7.5.1 — Propiedad del ínfimo en $\mathbb R_D$

Todo subconjunto no vacío de $\mathbb R_D$ que esté acotado inferiormente posee ínfimo en $\mathbb R_D$.

**Demostración.**

Proposición 4.6.2 — La propiedad del supremo implica la propiedad del ínfimo demuestra que, en un cuerpo ordenado, la propiedad del supremo implica la propiedad del ínfimo. Aplicamos ese resultado a Teorema 7.4.2 — Completitud del cuerpo de Dedekind. ∎

### Corolario 7.5.2 — El cuerpo de Dedekind es arquimediano

El cuerpo ordenado $\mathbb R_D$ es arquimediano.

**Demostración.**

Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano establece que todo cuerpo ordenado completo es arquimediano. La hipótesis se cumple por Teorema 7.4.2 — Completitud del cuerpo de Dedekind. ∎

### Proposición 7.5.3 — El modelo de Dedekind es una completación ordenada de $\mathbb Q$

El par formado por el cuerpo ordenado completo $\mathbb R_D$ y la incrustación canónica

$$
\iota_D:\mathbb Q\hookrightarrow\mathbb R_D
$$

es una completación ordenada de $\mathbb Q$ en el sentido de Definición 4.8.2 — Completación ordenada de $\mathbb Q$.

**Demostración.**

Corolario 6.8.15 — La aplicación canónica es una incrustación de cuerpos ordenados demuestra que $\iota_D$ es una incrustación de cuerpos ordenados. Teorema 7.4.2 — Completitud del cuerpo de Dedekind demuestra que su codominio $\mathbb R_D$ es un cuerpo ordenado completo. Son exactamente los datos exigidos por Definición 4.8.2 — Completación ordenada de $\mathbb Q$. ∎

### Corolario 7.5.4 — Densidad de la copia racional

La imagen

$$
\boxed{\iota_D[\mathbb Q]}
$$

es densa en $\mathbb R_D$. En particular, si

$$
\alpha<_D\beta,
$$

existe $q\in\mathbb Q$ tal que

$$
\boxed{\alpha<_D\iota_D(q)<_D\beta.}
$$

**Demostración.**

Por Proposición 7.5.3 — El modelo de Dedekind es una completación ordenada de $\mathbb Q$, $(\mathbb R_D,\iota_D)$ es una completación ordenada de $\mathbb Q$. Proposición 4.8.3 — La imagen racional de una completación es densa establece que la imagen racional de toda completación ordenada de $\mathbb Q$ es densa. ∎

La copia de los racionales no sólo está contenida estructuralmente en el modelo: continúa pudiendo aproximar desde ambos lados cualquier posición real.

### Lema 7.5.5 — Pertenencia a una cortadura y posición de la copia racional

Para toda $\alpha\in\mathbb R_D$ y todo $q\in\mathbb Q$,

$$
\boxed{q\in\alpha\iff\iota_D(q)<_D\alpha.}
$$

**Demostración.**

Supongamos primero $q\in\alpha$. Si $r\in\delta_q$, entonces $r<q$ y la clausura inferior de $\alpha$ da $r\in\alpha$. Así $\delta_q\subseteq\alpha$. La inclusión es propia porque $q\in\alpha$ mientras $q\notin\delta_q$. Por tanto

$$
\iota_D(q)=\delta_q<_D\alpha.
$$

Recíprocamente, supongamos $\delta_q\subsetneq\alpha$. Existe $x\in\alpha\setminus\delta_q$. Entonces no se cumple $x<q$, y por totalidad del orden racional,

$$
q\le x.
$$

Si $q=x$, entonces $q\in\alpha$. Si $q<x$, la clausura inferior de $\alpha$ vuelve a dar $q\in\alpha$. ∎

> **Nota fundacional.** La dirección
> $$
> q\in\alpha\Longrightarrow\iota_D(q)<_D\alpha
> $$
> es positiva. La recíproca, con el orden estricto actual definido mediante desigualdad extensional, extrae de $\delta_q\subsetneq\alpha$ un testigo $x\in\alpha\setminus\delta_q$ y utiliza negación clásica de cuantificadores. Por tanto las dos direcciones no tienen la misma fuerza constructiva.

Este lema convierte una afirmación interna sobre los racionales que forman una cortadura en una afirmación externa sobre la posición de la copia racional dentro de $\mathbb R_D$.

### Teorema 7.5.6 — Existencia y unicidad de la raíz cuadrada positiva de $2$

Existe un único $\rho\in\mathbb R_D$ tal que

$$
\boxed{0_D<_D\rho\qquad\text{y}\qquad \rho^2=\iota_D(2_{\mathbb Q}).}
$$

**Demostración.**

Para abreviar escribamos en esta demostración

$$
2_D:=\iota_D(2_{\mathbb Q}),
\qquad
4_D:=\iota_D(4_{\mathbb Q}),
\qquad
5_D:=\iota_D(5_{\mathbb Q}).
$$

Consideremos

$$
E_2:=\{x\in\mathbb R_D:0_D\leq_Dx\ \land\ x^2<_D2_D\}.
$$

El conjunto existe por Separación sobre $\mathbb R_D$.

**No vaciedad.** Como $1_{\mathbb Q}^2<2_{\mathbb Q}$, la preservación de la aritmética y del orden por $\iota_D$ da

$$
1_D^2<_D2_D.
$$

Así $1_D\in E_2$.

**Acotación superior.** Afirmamos que $2_D$ es cota superior. Si $x\in E_2$ y $2_D\leq_Dx$, entonces $0_D<_D2_D\leq_Dx$. La compatibilidad del orden con el producto da

$$
4_D=2_D^2\leq_Dx^2<_D2_D,
$$

lo cual contradice $2_D<_D4_D$. Luego $x<_D2_D$ para todo $x\in E_2$.

Por completitud existe

$$
s:=\sup_D E_2.
$$

Como $1_D\in E_2$ y $2_D$ es cota superior,

$$
1_D\leq_Ds\leq_D2_D.
$$

En particular, $s>_D0_D$.

Demostraremos que $s^2=2_D$.

Supongamos primero

$$
s^2<_D2_D.
$$

Pongamos

$$
d:=2_D-s^2>_D0_D.
$$

Como $d\cdot_D5_D^{-1_D}>_D0_D$, y $1_D>_D0_D$, por totalidad uno de estos dos elementos es menor o igual que el otro. Llamemos $m$ al menor. Entonces $m>_D0_D$. Por la densidad de $\iota_D[\mathbb Q]$ existe $\varepsilon\in\iota_D[\mathbb Q]$ tal que

$$
0_D<_D\varepsilon<_Dm.
$$

En particular,

$$
\varepsilon<_D1_D,
\qquad
5_D\varepsilon<_Dd.
$$

Como $s\leq_D2_D$,

$$
2_Ds+_D\varepsilon<_D5_D.
$$

Por positividad,

$$
\varepsilon(2_Ds+_D\varepsilon)<_D5_D\varepsilon<_Dd.
$$

Usando la identidad cuadrática,

$$
(s+_D\varepsilon)^2
=s^2+_D\varepsilon(2_Ds+_D\varepsilon)
<_Ds^2+_Dd
=2_D.
$$

Además $s+_D\varepsilon>_Ds>_D0_D$, de modo que $s+_D\varepsilon\in E_2$. Esto contradice que $s$ sea una cota superior de $E_2$.

Por tanto no puede ocurrir $s^2<_D2_D$.

Supongamos ahora

$$
2_D<_Ds^2.
$$

Pongamos

$$
d:=s^2-_D2_D>_D0_D.
$$

Los elementos $s$ y $d\cdot_D4_D^{-1_D}$ son positivos. Sea $m$ el menor de ambos. Por densidad racional existe $\varepsilon\in\iota_D[\mathbb Q]$ con

$$
0_D<_D\varepsilon<_Dm.
$$

Entonces

$$
\varepsilon<_Ds,
\qquad
4_D\varepsilon<_Dd.
$$

Como $s\leq_D2_D$,

$$
2_Ds\varepsilon\leq_D4_D\varepsilon<_Dd.
$$

Por tanto

$$
(s-_D\varepsilon)^2
=s^2-_D2_Ds\varepsilon+_D\varepsilon^2
>_Ds^2-_D2_Ds\varepsilon
>_Ds^2-_Dd
=2_D.
$$

Afirmamos que $s-_D\varepsilon$ es una cota superior de $E_2$. En efecto, si existiera $x\in E_2$ con

$$
s-_D\varepsilon<_Dx,
$$

ambos miembros serían no negativos. La identidad

$$
x^2-(s-_D\varepsilon)^2
=(x-(s-_D\varepsilon))(x+(s-_D\varepsilon))
$$

y el cálculo de signos en un cuerpo ordenado darían

$$
x^2>_D(s-_D\varepsilon)^2>_D2_D,
$$

contradiciendo $x\in E_2$.

Así $s-_D\varepsilon$ es una cota superior. Pero

$$
s-_D\varepsilon<_Ds,
$$

lo que contradice que $s$ sea la menor cota superior.

No puede ocurrir tampoco $2_D<_Ds^2$. Por tricotomía,

$$
\boxed{s^2=2_D.}
$$

Tomamos $\rho:=s$. Ya sabemos que $\rho>_D0_D$.

Para la unicidad, sean $u,v>_D0_D$ con $u^2=v^2=2_D$. Si $u<_Dv$, entonces

$$
v^2-u^2=(v-u)(v+u)>_D0_D,
$$

contradicción. El caso $v<_Du$ es análogo. Por tricotomía, $u=v$.

Existe, por tanto, un único real de Dedekind positivo cuyo cuadrado es $2_D$. ∎

> **Nota fundacional.** Esta prueba de existencia es clásica: usa la completitud plena, la densidad clásica de la copia racional y tricotomía en $\mathbb R_D$. Además,
> $$
> s=\sup_D E_2
> $$
> no constituye por sí mismo un algoritmo de aproximación de $s$. Este caso debe contrastarse con la cortadura explícita
> $$
> \alpha_2=\{q\in\mathbb Q:q<0\ \lor\ (0\leq q\land q^2<2)\},
> $$
> cuya pertenencia racional es decidible. Así,
> $$
> \boxed{
> \text{existencia por completitud}
> \neq
> \text{construcción explícita / efectiva de }\alpha_2.
> }
> $$

La completitud ha convertido en un elemento del cuerpo precisamente el tipo de frontera que faltaba en $\mathbb Q$.

### Corolario 7.5.7 — La cortadura $\alpha_2$ es la raíz cuadrada positiva de $2$

La cortadura introducida en el Capítulo 5 satisface

$$
\boxed{0_D<_D\alpha_2}
$$

y

$$
\boxed{\alpha_2^2=\iota_D(2_{\mathbb Q}).}
$$

En particular, $\alpha_2$ es el único elemento positivo de $\mathbb R_D$ cuyo cuadrado es $\iota_D(2_{\mathbb Q})$.

**Demostración.**

Sea $\rho>_D0_D$ el único elemento proporcionado por Teorema 7.5.6 — Existencia y unicidad de la raíz cuadrada positiva de $2$. Demostraremos

$$
\rho=\alpha_2
$$

por extensionalidad.

Sea $q\in\mathbb Q$.

Si $q<0_{\mathbb Q}$, entonces $q\in\alpha_2$ por definición. Además

$$
\iota_D(q)<_D0_D<_D\rho,
$$

por lo que Lema 7.5.5 — Pertenencia a una cortadura y posición de la copia racional da $q\in\rho$.

Supongamos ahora $0_{\mathbb Q}\leq q$.

Si $q\in\alpha_2$, entonces por Definición 5.3.1 — Cortadura cuadrática asociada a $2$ y Definición 3.9.7 — El conjunto racional asociado a $x^2<2$,

$$
q^2<2_{\mathbb Q}.
$$

La incrustación preserva producto y orden, así que

$$
\iota_D(q)^2<_D\rho^2.
$$

Como ambos elementos son no negativos, no puede cumplirse $\rho\leq_D\iota_D(q)$, pues la compatibilidad del orden con el producto produciría la desigualdad contraria entre sus cuadrados. Luego

$$
\iota_D(q)<_D\rho.
$$

Por Lema 7.5.5 — Pertenencia a una cortadura y posición de la copia racional, $q\in\rho$.

Recíprocamente, supongamos $q\in\rho$. Entonces

$$
\iota_D(q)<_D\rho.
$$

Como $q\geq0$, ambos miembros son no negativos. La diferencia de cuadrados factoriza como

$$
\rho^2-\iota_D(q)^2
=(\rho-\iota_D(q))(\rho+\iota_D(q))>_D0_D.
$$

Por tanto

$$
\iota_D(q)^2<_D\rho^2=\iota_D(2_{\mathbb Q}).
$$

La preservación y reflexión del orden por $\iota_D$, junto con la preservación del producto, implican

$$
q^2<2_{\mathbb Q}.
$$

Así $q\in S_2$ y, por definición, $q\in\alpha_2$.

Hemos probado

$$
q\in\rho\iff q\in\alpha_2
$$

para todo racional $q$. Por extensionalidad,

$$
\rho=\alpha_2.
$$

Como $\rho^2=\iota_D(2_{\mathbb Q})$ y $\rho>_D0_D$, obtenemos las dos afirmaciones del corolario. La unicidad procede de Teorema 7.5.6 — Existencia y unicidad de la raíz cuadrada positiva de $2$. ∎

Así se cierra el círculo iniciado en el Capítulo 3:

$$
\boxed{
\text{en }\mathbb Q\text{ no existe }q\text{ con }q^2=2,
\qquad
\text{en }\mathbb R_D\text{ existe }\alpha_2\text{ con }\alpha_2^2=2_D.
}
$$
