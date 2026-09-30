---
title: "Soluciones de microcontroles — Capítulo 4"
content-id: MA-BCH-0098
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-004-MICROCONTROLES
book-id: MA-BOK-0009
status: published
solution-status: complete
date-created: 2026-09-30
date-modified: 2026-09-30
areas: [analisis]
level: universitario
topics: [analisis-real, orden, topologia]
prerequisites: [MA-BCH-0083]
related: [MA-BOK-0009]
provenance:
  type: original
  sources:
    - "Manuscrito ANM C04; referencias de contraste en la portada del libro."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Capítulo 4](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto.md) · [Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Ejercicios](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-4-mirar-localmente-un-conjunto-microcontroles.md)

# Soluciones de microcontroles — Capítulo 4

## §4.1. Ventanas alrededor de un punto: vecindades

[]{#MA-MSOL-ANM-01-004-001}

### 1. Escribe $B(2,1/3)$ como intervalo abierto y explica qué desigualdad de valor absoluto describe sus puntos.

Por definición,

$$
B\left(2,\frac13\right)
=
\left\{
y\in\mathbb R:
|y-2|<\frac13
\right\}.
$$

La desigualdad

$$
|y-2|<\frac13
$$

equivale a

$$
-\frac13<y-2<\frac13.
$$

Sumando $2$ en los tres miembros,

$$
\frac53<y<\frac73.
$$

Por tanto,

$$
\boxed{
B\left(2,\frac13\right)
=
\left(\frac53,\frac73\right).
}
$$

La desigualdad de valor absoluto expresa exactamente que la distancia de $y$ al centro $2$ es menor que el radio $1/3$.

[]{#MA-MSOL-ANM-01-004-002}

### 2. Para $V=(-1,1)\cup\{3\}$, exhibe dos radios distintos que certifiquen que $V$ es vecindad de $0$.

Podemos elegir, por ejemplo,

$$
r_1=1
\qquad\text{y}\qquad
r_2=\frac12.
$$

En efecto,

$$
B(0,1)=(-1,1)\subseteq V,
$$

y también

$$
B\left(0,\frac12\right)
=
\left(-\frac12,\frac12\right)
\subseteq(-1,1)\subseteq V.
$$

Por tanto existen al menos dos radios positivos que certifican que $V$ es vecindad de $0$.

El punto aislado $3$ no interviene en la certificación: basta con que alguna bola centrada en $0$ quede contenida en $V$.

[]{#MA-MSOL-ANM-01-004-003}

### 3. Decide si $[0,2)$ es una vecindad de $0$. No basta responder sí o no: debes justificarlo directamente a partir de la definición.

No es una vecindad de $0$.

Para que lo fuera tendría que existir $r>0$ tal que

$$
B(0,r)\subseteq[0,2).
$$

Sea, sin embargo, $r>0$ arbitrario. El punto

$$
-\frac r2
$$

satisface

$$
\left|-\frac r2\right|
=
\frac r2<r,
$$

de modo que

$$
-\frac r2\in B(0,r).
$$

Pero

$$
-\frac r2<0,
$$

por lo que

$$
-\frac r2\notin[0,2).
$$

Así,

$$
B(0,r)\not\subseteq[0,2)
$$

para todo $r>0$. Por tanto,

$$
\boxed{
[0,2)\text{ no es vecindad de }0.
}
$$

La pertenencia

$$
0\in[0,2)
$$

no basta: falta margen a la izquierda del centro.

[]{#MA-MSOL-ANM-01-004-004}

### 4. Demuestra que si $V$ es vecindad de $x$, entonces $x\in V$. Da después un contraejemplo que muestre que la conversa es falsa.

Si $V$ es vecindad de $x$, existe $r>0$ tal que

$$
B(x,r)\subseteq V.
$$

Como

$$
|x-x|=0<r,
$$

tenemos

$$
x\in B(x,r).
$$

La inclusión anterior da entonces

$$
x\in V.
$$

Por tanto,

$$
\boxed{
V\text{ vecindad de }x
\Longrightarrow
x\in V.
}
$$

La conversa es falsa. Tomemos

$$
V=[0,2),
\qquad
x=0.
$$

Tenemos

$$
0\in V,
$$

pero el microcontrol anterior demuestra que ninguna bola positiva centrada en $0$ queda contenida en $V$.

Así,

$$
x\in V
\quad\not\Rightarrow\quad
V\text{ es vecindad de }x.
$$

[]{#MA-MSOL-ANM-01-004-005}

### 5. Supón que $V$ es vecindad de $x$ y que $V\subseteq W$. Demuestra que $W$ también es vecindad de $x$.

Como $V$ es vecindad de $x$, existe $r>0$ tal que

$$
B(x,r)\subseteq V.
$$

Por hipótesis,

$$
V\subseteq W.
$$

Encadenando las inclusiones,

$$
B(x,r)\subseteq V\subseteq W.
$$

Así, el mismo radio $r$ certifica que

$$
\boxed{
W\text{ es vecindad de }x.
}
$$

Geométricamente, agrandar un conjunto no destruye una ventana que ya cabía dentro de él.

[]{#MA-MSOL-ANM-01-004-006}

### 6. Si $V$ y $W$ son vecindades de $x$, demuestra que $V\cap W$ es vecindad de $x$ indicando explícitamente qué radio eliges.

Como $V$ es vecindad de $x$, existe $r>0$ tal que

$$
B(x,r)\subseteq V.
$$

Como $W$ es vecindad de $x$, existe $s>0$ tal que

$$
B(x,s)\subseteq W.
$$

Elegimos

$$
\rho=\min\{r,s\}.
$$

Como $r,s>0$,

$$
\rho>0.
$$

Además,

$$
\rho\le r
\qquad\text{y}\qquad
\rho\le s.
$$

Por tanto,

$$
B(x,\rho)\subseteq B(x,r)\subseteq V
$$

y

$$
B(x,\rho)\subseteq B(x,s)\subseteq W.
$$

Luego

$$
B(x,\rho)\subseteq V\cap W.
$$

Así,

$$
\boxed{
V\cap W\text{ es vecindad de }x.
}
$$

El radio elegido es exactamente

$$
\boxed{\rho=\min\{r,s\}.}
$$

[]{#MA-MSOL-ANM-01-004-007}

### 7. Si $B(x,r)\subseteq V$ y $0<s\le r$, demuestra que $B(x,s)\subseteq V$. ¿Qué te dice esto sobre la frase «podemos mirar con ventanas arbitrariamente pequeñas»?

Sea

$$
y\in B(x,s).
$$

Entonces

$$
|y-x|<s.
$$

Como

$$
s\le r,
$$

obtenemos

$$
|y-x|<r,
$$

y por tanto

$$
y\in B(x,r).
$$

Así,

$$
B(x,s)\subseteq B(x,r).
$$

Como por hipótesis

$$
B(x,r)\subseteq V,
$$

concluimos

$$
\boxed{
B(x,s)\subseteq V.
}
$$

La frase «podemos mirar con ventanas arbitrariamente pequeñas» significa que, una vez encontrado un radio $r>0$ que funciona, **todo radio positivo menor o igual que $r$ también funciona**.

No significa que todos los radios positivos funcionen. La estructura lógica es

$$
\exists r>0
\quad\Longrightarrow\quad
\forall s\in(0,r].
$$

[]{#MA-MSOL-ANM-01-004-008}

### 8. Sea $y\in B(x,r)$. Construye un $\delta>0$ en función de $r$ y $|y-x|$ tal que $B(y,\delta)\subseteq B(x,r)$, y señala exactamente dónde usas la desigualdad triangular.

Como

$$
y\in B(x,r),
$$

tenemos

$$
|y-x|<r.
$$

Por tanto,

$$
\delta=r-|y-x|
$$

es positivo.

Afirmamos que

$$
B(y,\delta)\subseteq B(x,r).
$$

Sea

$$
z\in B(y,\delta).
$$

Entonces

$$
|z-y|<\delta.
$$

Aquí usamos la desigualdad triangular:

$$
|z-x|
\le
|z-y|+|y-x|.
$$

Como

$$
|z-y|<\delta,
$$

se sigue que

$$
|z-x|
<
\delta+|y-x|.
$$

Sustituyendo

$$
\delta=r-|y-x|,
$$

obtenemos

$$
|z-x|
<
r-|y-x|+|y-x|
=
r.
$$

Por tanto,

$$
z\in B(x,r).
$$

Como $z$ era arbitrario,

$$
\boxed{
B(y,\delta)\subseteq B(x,r),
\qquad
\delta=r-|y-x|>0.
}
$$

La desigualdad triangular se usa exactamente en el paso

$$
|z-x|
\le
|z-y|+|y-x|.
$$

## §4.2. Interior y exterior: tener margen

[]{#MA-MSOL-ANM-01-004-009}

### 9. Para $A=[-2,3]$, determina cuáles de los puntos $-2$, $0$ y $3$ son interiores. En cada caso interior, exhibe un radio que funcione; en cada caso no interior, demuestra que ningún radio puede funcionar.

El punto $0$ es interior. Por ejemplo,

$$
B(0,1)=(-1,1)\subseteq[-2,3].
$$

Por tanto,

$$
0\in\operatorname{int}(A).
$$

En cambio, $-2$ no es interior. Sea $r>0$. El punto

$$
-2-\frac r2
$$

pertenece a $B(-2,r)$, pero no a $[-2,3]$. Luego ninguna bola positiva centrada en $-2$ queda contenida en $A$.

De manera análoga, para cualquier $r>0$,

$$
3+\frac r2\in B(3,r)
$$

y

$$
3+\frac r2\notin[-2,3].
$$

Así, $3$ tampoco es interior.

En conclusión,

$$
\boxed{
0\text{ es interior, mientras que }-2\text{ y }3\text{ no lo son.}
}
$$

[]{#MA-MSOL-ANM-01-004-010}

### 10. Demuestra directamente desde la definición que $\operatorname{int}(A)\subseteq A$ para todo $A\subseteq\mathbb R$.

Sea

$$
x\in\operatorname{int}(A).
$$

Por definición, existe $r>0$ tal que

$$
B(x,r)\subseteq A.
$$

Como el centro pertenece a su propia bola,

$$
x\in B(x,r).
$$

Por la inclusión,

$$
x\in A.
$$

Como $x$ era arbitrario,

$$
\boxed{
\operatorname{int}(A)\subseteq A.
}
$$

[]{#MA-MSOL-ANM-01-004-011}

### 11. Sea $A=(a,b)$ con $a<b$ y $x\in(a,b)$. Construye un radio explícito en función de $x-a$ y $b-x$ que certifique que $x$ es interior.

Como

$$
a<x<b,
$$

las cantidades

$$
x-a
\qquad\text{y}\qquad
b-x
$$

son positivas.

Podemos elegir

$$
r=
\frac12\min\{x-a,b-x\}>0.
$$

Si

$$
y\in B(x,r),
$$

entonces

$$
|y-x|<r.
$$

En particular,

$$
y>x-r
\ge
x-\frac{x-a}{2}
>
a,
$$

y también

$$
y<x+r
\le
x+\frac{b-x}{2}
<
b.
$$

Por tanto,

$$
a<y<b,
$$

de modo que

$$
B(x,r)\subseteq(a,b).
$$

Así,

$$
\boxed{
r=\frac12\min\{x-a,b-x\}
}
$$

certifica que $x$ es interior a $(a,b)$.

[]{#MA-MSOL-ANM-01-004-012}

### 12. Para $A=(0,1)$, explica por qué $0\notin A$ pero $0$ no es exterior a $A$. Tu argumento debe comenzar con un radio arbitrario $r>0$.

Es claro que

$$
0\notin(0,1).
$$

Para que $0$ fuera exterior tendría que existir $r>0$ tal que

$$
B(0,r)\cap(0,1)=\varnothing.
$$

Veamos que esto nunca ocurre.

Sea $r>0$ arbitrario y tomemos

$$
y=
\min\left\{\frac r2,\frac12\right\}.
$$

Entonces

$$
0<y<1,
$$

por lo que

$$
y\in A.
$$

Además,

$$
|y|=y<r,
$$

así que

$$
y\in B(0,r).
$$

Por tanto,

$$
B(0,r)\cap A\ne\varnothing
$$

para todo $r>0$.

Concluimos

$$
\boxed{
0\notin A
\quad\text{pero}\quad
0\notin\operatorname{ext}(A).
}
$$

No pertenecer al conjunto no basta para tener margen exterior.

[]{#MA-MSOL-ANM-01-004-013}

### 13. Demuestra que $x$ es exterior a $A$ si y sólo si $A^c$ es vecindad de $x$.

Por definición,

$$
x\in\operatorname{ext}(A)
$$

si y sólo si existe $r>0$ tal que

$$
B(x,r)\subseteq A^c.
$$

Pero ésta es exactamente la condición que define que $A^c$ sea una vecindad de $x$.

Por tanto,

$$
\boxed{
x\in\operatorname{ext}(A)
\iff
A^c\text{ es vecindad de }x.
}
$$

[]{#MA-MSOL-ANM-01-004-014}

### 14. Prueba la identidad $\operatorname{ext}(A)=\operatorname{int}(A^c)$ sin usar ninguna noción posterior de este capítulo.

Sea $x\in\mathbb R$.

Por definición,

$$
x\in\operatorname{ext}(A)
\iff
\exists r>0:
B(x,r)\subseteq A^c.
$$

Pero la condición de la derecha es precisamente la definición de

$$
x\in\operatorname{int}(A^c).
$$

Así, para todo $x\in\mathbb R$,

$$
x\in\operatorname{ext}(A)
\iff
x\in\operatorname{int}(A^c).
$$

Por extensionalidad,

$$
\boxed{
\operatorname{ext}(A)=\operatorname{int}(A^c).
}
$$

[]{#MA-MSOL-ANM-01-004-015}

### 15. Si $A\subseteq B$, demuestra $\operatorname{int}(A)\subseteq\operatorname{int}(B)$ y deriva después $\operatorname{ext}(B)\subseteq\operatorname{ext}(A)$.

Supongamos

$$
A\subseteq B.
$$

Sea

$$
x\in\operatorname{int}(A).
$$

Existe $r>0$ tal que

$$
B(x,r)\subseteq A.
$$

Como

$$
A\subseteq B,
$$

tenemos

$$
B(x,r)\subseteq B.
$$

Por tanto,

$$
x\in\operatorname{int}(B).
$$

Así,

$$
\boxed{
\operatorname{int}(A)\subseteq\operatorname{int}(B).
}
$$

Para el exterior observamos que

$$
A\subseteq B
\quad\Longrightarrow\quad
B^c\subseteq A^c.
$$

Aplicando la monotonicidad del interior,

$$
\operatorname{int}(B^c)
\subseteq
\operatorname{int}(A^c).
$$

Usando

$$
\operatorname{ext}(C)=\operatorname{int}(C^c),
$$

obtenemos

$$
\boxed{
\operatorname{ext}(B)
\subseteq
\operatorname{ext}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-016}

### 16. Para $A=[0,1)$, verifica que $\operatorname{int}(A)=(0,1)$ y $\operatorname{ext}(A)=(-\infty,0)\cup(1,\infty)$. ¿Qué ocurre localmente en $0$ y en $1$ que impide clasificarlos en cualquiera de esos dos conjuntos?

Primero calculemos el interior.

Si

$$
0<x<1,
$$

el radio

$$
r=
\frac12\min\{x,1-x\}>0
$$

satisface

$$
B(x,r)\subseteq(0,1)\subseteq[0,1).
$$

Por tanto,

$$
(0,1)\subseteq\operatorname{int}(A).
$$

El punto $0$ no es interior porque, para todo $r>0$,

$$
-\frac r2\in B(0,r)
$$

pero

$$
-\frac r2\notin A.
$$

No hay otros puntos de $A$. Así,

$$
\boxed{
\operatorname{int}(A)=(0,1).
}
$$

Ahora calculemos el exterior.

Si $x<0$, podemos tomar

$$
r=\frac{-x}{2}>0.
$$

Entonces

$$
B(x,r)\subset(-\infty,0)\subseteq A^c.
$$

Si $x>1$, sirve

$$
r=\frac{x-1}{2}>0,
$$

y entonces

$$
B(x,r)\subset(1,\infty)\subseteq A^c.
$$

Por tanto,

$$
(-\infty,0)\cup(1,\infty)
\subseteq
\operatorname{ext}(A).
$$

El punto $1$ no es exterior. Dado $r>0$, tomemos

$$
y=
1-
\min\left\{\frac r2,\frac12\right\}.
$$

Entonces

$$
0<y<1,
$$

de modo que

$$
y\in A,
$$

y además

$$
|y-1|<r.
$$

Por tanto toda bola centrada en $1$ toca a $A$.

El punto $0$ tampoco es exterior porque pertenece a $A$ y toda bola centrada en él contiene al propio centro.

Así,

$$
\boxed{
\operatorname{ext}(A)
=
(-\infty,0)\cup(1,\infty).
}
$$

Localmente, en $0$ ninguna bola queda completamente dentro de $A$ porque siempre aparecen puntos negativos, y ninguna bola queda completamente fuera porque el centro pertenece a $A$.

En $1$, ninguna bola queda completamente dentro de $A$ porque $1\notin A$, y ninguna queda completamente fuera porque toda bola alcanza puntos de $(0,1)$.

Por eso ninguno de los dos extremos pertenece al interior ni al exterior.

## §4.3. Clausura: puntos que no pueden evitar al conjunto

[]{#MA-MSOL-ANM-01-004-017}

### 17. Despliega la negación lógica de $\exists r>0:\ B(x,r)\cap A=\varnothing$ y explica por qué produce exactamente la definición de punto adherente.

Negar
$$
\exists r>0:\ B(x,r)\cap A=\varnothing
$$
cambia el cuantificador existencial por uno universal y niega la igualdad:
$$
\forall r>0:\ B(x,r)\cap A\ne\varnothing.
$$
Ésta es exactamente la definición de adherencia:
$$
\boxed{
x\in\overline A
\iff
\forall r>0:\ B(x,r)\cap A\ne\varnothing.
}
$$
Por tanto, ser adherente a $A$ es la negación exacta de ser exterior a $A$.

[]{#MA-MSOL-ANM-01-004-018}

### 18. Demuestra directamente que $A\subseteq\overline A$ para todo $A\subseteq\mathbb R$.

Sea $x\in A$. Para cualquier $r>0$, el centro pertenece a su propia bola:
$$
x\in B(x,r).
$$
Como también $x\in A$,
$$
x\in B(x,r)\cap A.
$$
Así,
$$
B(x,r)\cap A\ne\varnothing
$$
para todo $r>0$, y por tanto
$$
x\in\overline A.
$$
Como $x$ era arbitrario,
$$
\boxed{
A\subseteq\overline A.
}
$$

[]{#MA-MSOL-ANM-01-004-019}

### 19. Para $A=(0,1)$, prueba con un radio arbitrario que $0,1\in\overline A$, aunque ninguno de los dos pertenezca a $A$.

Es claro que
$$
0,1\notin(0,1).
$$
Sea $r>0$. Para $0$, tomemos
$$
a_0=\min\left\{\frac r2,\frac12\right\}.
$$
Entonces $0<a_0<1$ y $a_0<r$, de modo que
$$
a_0\in B(0,r)\cap A.
$$
Así,
$$
0\in\overline A.
$$

Para $1$, tomemos
$$
a_1=1-\min\left\{\frac r2,\frac12\right\}.
$$
Entonces $0<a_1<1$ y $|a_1-1|<r$, por lo que
$$
a_1\in B(1,r)\cap A.
$$
Así,
$$
1\in\overline A.
$$

Por tanto,
$$
\boxed{
0,1\in\overline{(0,1)}
\quad\text{aunque}\quad
0,1\notin(0,1).
}
$$

[]{#MA-MSOL-ANM-01-004-020}

### 20. Demuestra $\overline A=(\operatorname{ext}(A))^c=(\operatorname{int}(A^c))^c$.

Por definición,
$$
x\in\overline A
\iff
\forall r>0:\ B(x,r)\cap A\ne\varnothing.
$$
Esta afirmación es la negación de
$$
\exists r>0:\ B(x,r)\cap A=\varnothing,
$$
que equivale a
$$
x\in\operatorname{ext}(A).
$$
Por tanto,
$$
x\in\overline A
\iff
x\notin\operatorname{ext}(A),
$$
y así
$$
\boxed{
\overline A=(\operatorname{ext}(A))^c.
}
$$

Como
$$
\operatorname{ext}(A)=\operatorname{int}(A^c),
$$
se obtiene
$$
\boxed{
\overline A=(\operatorname{int}(A^c))^c.
}
$$

[]{#MA-MSOL-ANM-01-004-021}

### 21. Si $A\subseteq B$, demuestra la monotonicidad $\overline A\subseteq\overline B$.

Supongamos $A\subseteq B$ y sea
$$
x\in\overline A.
$$
Entonces, para todo $r>0$,
$$
B(x,r)\cap A\ne\varnothing.
$$
Sea $r>0$. Elijamos
$$
a\in B(x,r)\cap A.
$$
Como $A\subseteq B$, también $a\in B$, de modo que
$$
a\in B(x,r)\cap B.
$$
Por tanto,
$$
B(x,r)\cap B\ne\varnothing
$$
para todo $r>0$, y así
$$
x\in\overline B.
$$
Concluimos
$$
\boxed{
A\subseteq B
\Longrightarrow
\overline A\subseteq\overline B.
}
$$

[]{#MA-MSOL-ANM-01-004-022}

### 22. Reproduce la prueba de $\overline{\overline A}=\overline A$ indicando por qué se usan radios $r/2$ y dónde interviene la desigualdad triangular.

Como
$$
A\subseteq\overline A,
$$
la monotonicidad da
$$
\overline A\subseteq\overline{\overline A}.
$$

Para la inclusión contraria, sea
$$
x\in\overline{\overline A}
$$
y sea $r>0$ arbitrario. Como $x$ es adherente a $\overline A$, existe
$$
y\in B\left(x,\frac r2\right)\cap\overline A.
$$
Como $y\in\overline A$, existe
$$
a\in B\left(y,\frac r2\right)\cap A.
$$
Aquí usamos la desigualdad triangular:
$$
|a-x|
\le
|a-y|+|y-x|
<
\frac r2+\frac r2
=
r.
$$
Por tanto,
$$
a\in B(x,r)\cap A.
$$
Como $r$ era arbitrario,
$$
x\in\overline A.
$$
Así,
$$
\overline{\overline A}\subseteq\overline A,
$$
y por ambas inclusiones,
$$
\boxed{
\overline{\overline A}=\overline A.
}
$$

Los radios $r/2$ reparten el margen total $r$ entre los dos desplazamientos que después suma la desigualdad triangular.

[]{#MA-MSOL-ANM-01-004-023}

### 23. Sea $A=(0,1)\setminus\{1/2\}$. Demuestra sin usar sucesiones que $1/2\in\overline A$ y que ningún punto de $(-\infty,0)\cup(1,\infty)$ pertenece a $\overline A$.

Sea $r>0$. Para $x=1/2$, tomemos
$$
a=
\frac12+
\min\left\{
\frac r2,\frac14
\right\}.
$$
Entonces
$$
\frac12<a\le\frac34<1,
$$
por lo que $a\in A$, y además
$$
\left|a-\frac12\right|<r.
$$
Así,
$$
\frac12\in\overline A.
$$

Si $x<0$, tomemos
$$
r=\frac{-x}{2}>0.
$$
Entonces
$$
B(x,r)\subset(-\infty,0),
$$
por lo que
$$
B(x,r)\cap A=\varnothing.
$$
Así $x\notin\overline A$.

Si $x>1$, tomemos
$$
r=\frac{x-1}{2}>0.
$$
Entonces
$$
B(x,r)\subset(1,\infty),
$$
y otra vez
$$
B(x,r)\cap A=\varnothing.
$$
Por tanto ningún punto de
$$
(-\infty,0)\cup(1,\infty)
$$
pertenece a $\overline A$.

[]{#MA-MSOL-ANM-01-004-024}

### 24. Demuestra que $x\in\overline A$ si y sólo si toda vecindad de $x$ intersecta $A$. Tu prueba debe volver explícitamente a una bola contenida en la vecindad.

Supongamos primero que
$$
x\in\overline A.
$$
Sea $V$ una vecindad de $x$. Existe $r>0$ tal que
$$
B(x,r)\subseteq V.
$$
Como $x$ es adherente,
$$
B(x,r)\cap A\ne\varnothing.
$$
Si
$$
a\in B(x,r)\cap A,
$$
entonces, por la inclusión,
$$
a\in V\cap A.
$$
Así,
$$
V\cap A\ne\varnothing.
$$

Recíprocamente, supongamos que toda vecindad de $x$ intersecta $A$. Sea $r>0$. La propia bola $B(x,r)$ es una vecindad de $x$, de modo que
$$
B(x,r)\cap A\ne\varnothing.
$$
Como esto vale para todo $r>0$,
$$
x\in\overline A.
$$

Por tanto,
$$
\boxed{
x\in\overline A
\iff
\text{toda vecindad de }x\text{ intersecta }A.
}
$$

## §4.4. Frontera: toda ventana ve ambos lados

[]{#MA-MSOL-ANM-01-004-025}

### 25. Demuestra directamente desde la definición que $\partial(A^c)=\partial A$.

Por definición,

$$
x\in\partial(A^c)
$$

si y sólo si, para todo $r>0$,

$$
B(x,r)\cap A^c\ne\varnothing
$$

y

$$
B(x,r)\cap(A^c)^c\ne\varnothing.
$$

Como

$$
(A^c)^c=A,
$$

la condición anterior equivale a

$$
\forall r>0:
\bigl(B(x,r)\cap A^c\ne\varnothing\bigr)
\ \text{y}\
\bigl(B(x,r)\cap A\ne\varnothing\bigr).
$$

El orden de las dos condiciones no importa. Por tanto,

$$
x\in\partial(A^c)
\iff
x\in\partial A.
$$

Así,

$$
\boxed{
\partial(A^c)=\partial A.
}
$$

[]{#MA-MSOL-ANM-01-004-026}

### 26. Para $A=[-1,2)$, demuestra que $\partial A=\{-1,2\}$, indicando en cada extremo cómo encuentras, para un radio arbitrario, un punto de $A$ y uno de $A^c$ dentro de la bola.

Primero consideremos $x=-1$.

Sea $r>0$. Como

$$
-1\in A,
$$

el propio centro pertenece a

$$
B(-1,r)\cap A.
$$

Además,

$$
-1-\frac r2\in B(-1,r)
$$

y

$$
-1-\frac r2<-1,
$$

de modo que

$$
-1-\frac r2\in A^c.
$$

Así,

$$
-1\in\partial A.
$$

Ahora consideremos $x=2$.

Sea $r>0$. El punto

$$
2+\frac r2
$$

pertenece a

$$
B(2,r)\cap A^c.
$$

Para encontrar un punto de $A$ dentro de la misma bola, tomemos

$$
a=
2-\min\left\{\frac r2,\frac12\right\}.
$$

Entonces

$$
-1<a<2,
$$

por lo que

$$
a\in A,
$$

y además

$$
|a-2|<r.
$$

Así,

$$
2\in\partial A.
$$

Si

$$
-1<x<2,
$$

podemos elegir

$$
\rho=
\frac12\min\{x+1,2-x\}>0,
$$

y entonces

$$
B(x,\rho)\subseteq[-1,2),
$$

de modo que $x$ no es fronterizo.

Si $x<-1$ o $x>2$, existe una bola suficientemente pequeña completamente contenida en $A^c$, por lo que tampoco es fronterizo.

Concluimos

$$
\boxed{
\partial[-1,2)=\{-1,2\}.
}
$$

[]{#MA-MSOL-ANM-01-004-027}

### 27. Demuestra $\partial A=\overline A\cap\overline{A^c}$ desplegando ambos lados únicamente mediante cuantificadores sobre bolas.

Sea $x\in\mathbb R$.

Por definición,

$$
x\in\partial A
$$

si y sólo si

$$
\forall r>0:
B(x,r)\cap A\ne\varnothing
$$

y

$$
\forall r>0:
B(x,r)\cap A^c\ne\varnothing.
$$

La primera condición equivale a

$$
x\in\overline A,
$$

y la segunda a

$$
x\in\overline{A^c}.
$$

Por tanto,

$$
x\in\partial A
\iff
x\in\overline A
\ \text{y}\
x\in\overline{A^c}.
$$

Es decir,

$$
x\in\partial A
\iff
x\in
\overline A\cap\overline{A^c}.
$$

Como esto vale para todo $x$,

$$
\boxed{
\partial A
=
\overline A\cap\overline{A^c}.
}
$$

[]{#MA-MSOL-ANM-01-004-028}

### 28. Deduce de la identidad anterior que $\partial A=\overline A\setminus\operatorname{int}(A)$.

Partimos de

$$
\partial A
=
\overline A\cap\overline{A^c}.
$$

Por la dualidad de clausura e interior,

$$
\overline{A^c}
=
\bigl(\operatorname{int}((A^c)^c)\bigr)^c
=
\bigl(\operatorname{int}(A)\bigr)^c.
$$

Sustituyendo,

$$
\partial A
=
\overline A
\cap
\bigl(\operatorname{int}(A)\bigr)^c.
$$

Por definición de diferencia de conjuntos,

$$
X\setminus Y=X\cap Y^c.
$$

Por tanto,

$$
\boxed{
\partial A
=
\overline A\setminus\operatorname{int}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-029}

### 29. Para $A=(0,1)\setminus\{1/2\}$, demuestra que $\partial A=\{0,1/2,1\}$. Explica por qué este ejemplo impide definir frontera como «conjunto de extremos».

Sabemos que

$$
\overline A=[0,1].
$$

También,

$$
\operatorname{int}(A)
=
\left(0,\frac12\right)
\cup
\left(\frac12,1\right).
$$

Usando

$$
\partial A
=
\overline A\setminus\operatorname{int}(A),
$$

obtenemos

$$
\partial A
=
[0,1]
\setminus
\left[
\left(0,\frac12\right)
\cup
\left(\frac12,1\right)
\right].
$$

Por tanto,

$$
\boxed{
\partial A
=
\left\{
0,\frac12,1
\right\}.
}
$$

El punto

$$
\frac12
$$

no es un extremo global del intervalo $(0,1)$, pero sí es fronterizo: toda bola centrada en $1/2$ contiene al propio centro, que pertenece a $A^c$, y también puntos de $A$ arbitrariamente cercanos.

Por eso la frontera no puede definirse como «conjunto de extremos». Es una propiedad local de las ventanas alrededor de cada punto.

[]{#MA-MSOL-ANM-01-004-030}

### 30. Demuestra que ningún punto interior y ningún punto exterior puede pertenecer a $\partial A$.

Supongamos

$$
x\in\operatorname{int}(A).
$$

Existe $r>0$ tal que

$$
B(x,r)\subseteq A.
$$

Entonces

$$
B(x,r)\cap A^c=\varnothing.
$$

Pero para que $x$ fuera fronterizo, **toda** bola positiva centrada en $x$ tendría que intersectar $A^c$. Este radio lo contradice.

Por tanto,

$$
x\notin\partial A.
$$

Así,

$$
\operatorname{int}(A)\cap\partial A=\varnothing.
$$

Del mismo modo, si

$$
x\in\operatorname{ext}(A),
$$

existe $r>0$ tal que

$$
B(x,r)\subseteq A^c,
$$

y entonces

$$
B(x,r)\cap A=\varnothing.
$$

Por tanto $x$ tampoco puede ser fronterizo.

Así,

$$
\boxed{
\operatorname{int}(A)\cap\partial A=\varnothing,
\qquad
\operatorname{ext}(A)\cap\partial A=\varnothing.
}
$$

[]{#MA-MSOL-ANM-01-004-031}

### 31. Prueba la partición disjunta $\mathbb R=\operatorname{int}(A)\,\dot\cup\,\partial A\,\dot\cup\,\operatorname{ext}(A)$.

Ya sabemos que

$$
\operatorname{int}(A),
\qquad
\partial A,
\qquad
\operatorname{ext}(A)
$$

son disjuntos dos a dos.

Falta demostrar que su unión es toda la recta.

Sea

$$
x\in\mathbb R.
$$

Si

$$
x\in\operatorname{ext}(A),
$$

ya está clasificado.

Supongamos ahora

$$
x\notin\operatorname{ext}(A).
$$

Como

$$
\overline A
=
(\operatorname{ext}(A))^c,
$$

tenemos

$$
x\in\overline A.
$$

Dentro de $\overline A$ hay dos casos.

Si

$$
x\in\operatorname{int}(A),
$$

queda clasificado como interior.

Si

$$
x\notin\operatorname{int}(A),
$$

entonces

$$
x\in
\overline A\setminus\operatorname{int}(A)
=
\partial A.
$$

Por tanto, todo real pertenece a una de las tres clases.

Así,

$$
\boxed{
\mathbb R
=
\operatorname{int}(A)
\,\dot\cup\,
\partial A
\,\dot\cup\,
\operatorname{ext}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-032}

### 32. Compara $(0,1)$, $[0,1]$, $[0,1)$ y $(0,1]$. ¿Qué cambia al incluir o excluir los extremos y qué permanece invariante respecto de la frontera?

En los cuatro conjuntos, los puntos estrictamente interiores al intervalo satisfacen

$$
0<x<1,
$$

y poseen margen interior.

Los puntos fuera de $[0,1]$ poseen margen exterior.

En cambio, alrededor de $0$ y $1$, toda bola positiva contiene puntos de $(0,1)$ y también puntos exteriores a $[0,1]$.

Por eso, en los cuatro casos,

$$
\boxed{
\partial A=\{0,1\}.
}
$$

Lo que sí cambia es la pertenencia de los extremos:

- en $(0,1)$, ninguno pertenece;
- en $[0,1]$, ambos pertenecen;
- en $[0,1)$, sólo $0$ pertenece;
- en $(0,1]$, sólo $1$ pertenece.

Así, incluir o excluir un extremo modifica la pertenencia del centro, pero no cambia su comportamiento fronterizo.

La frontera depende de lo que ve **toda ventana alrededor del punto**, no de si el propio centro fue incluido o excluido del conjunto.

## §4.5. Acumulación: el conjunto reaparece alrededor del punto

[]{#MA-MSOL-ANM-01-004-033}

### 33. Escribe en cuantificadores la diferencia exacta entre $x\in\overline A$ y $x\in\operatorname{Acc}(A)$. ¿Qué único conjunto cambia dentro de la intersección?

La adherencia se expresa como

$$
x\in\overline A
\iff
\forall r>0:
B(x,r)\cap A\ne\varnothing.
$$

La acumulación exige

$$
x\in\operatorname{Acc}(A)
\iff
\forall r>0:
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A\ne\varnothing.
$$

La diferencia exacta es la perforación del centro:

$$
B(x,r)
\quad\longrightarrow\quad
B(x,r)\setminus\{x\}.
$$

Todo lo demás permanece igual: el cuantificador es universal y seguimos pidiendo intersección no vacía con $A$.

La acumulación es más exigente porque impide usar siempre el propio centro como testigo cuando $x\in A$.

[]{#MA-MSOL-ANM-01-004-034}

### 34. Demuestra directamente que $\operatorname{Acc}(A)\subseteq\overline A$.

Sea

$$
x\in\operatorname{Acc}(A).
$$

Entonces, para todo $r>0$,

$$
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A\ne\varnothing.
$$

Como

$$
B(x,r)\setminus\{x\}
\subseteq
B(x,r),
$$

se sigue que

$$
B(x,r)\cap A\ne\varnothing
$$

para todo $r>0$.

Por tanto,

$$
x\in\overline A.
$$

Así,

$$
\boxed{
\operatorname{Acc}(A)\subseteq\overline A.
}
$$

[]{#MA-MSOL-ANM-01-004-035}

### 35. Para $A=(0,1)\cup\{2\}$, demuestra que $0$ y $1/2$ son puntos de acumulación, mientras que $2$ no lo es.

Primero, sea $r>0$. Para $x=0$, tomemos

$$
a=
\min\left\{
\frac r2,\frac12
\right\}.
$$

Entonces

$$
0<a<1,
$$

por lo que $a\in A$, además $a\ne0$ y $|a|<r$. Así,

$$
a\in
\bigl(B(0,r)\setminus\{0\}\bigr)\cap A.
$$

Por tanto,

$$
0\in\operatorname{Acc}(A).
$$

Para $x=1/2$, sea

$$
\delta=
\min\left\{
\frac r2,\frac14
\right\}>0
$$

y tomemos

$$
a=\frac12+\delta.
$$

Entonces

$$
\frac12<a<1,
$$

de modo que $a\in A$, $a\ne1/2$ y

$$
\left|a-\frac12\right|<r.
$$

Así,

$$
\frac12\in\operatorname{Acc}(A).
$$

En cambio,

$$
B\left(2,\frac12\right)
=
\left(\frac32,\frac52\right)
$$

sólo encuentra al conjunto $A$ en el propio punto $2$:

$$
B\left(2,\frac12\right)\cap A=\{2\}.
$$

Al perforar el centro,

$$
\left(
B\left(2,\frac12\right)\setminus\{2\}
\right)\cap A
=
\varnothing.
$$

Por tanto,

$$
\boxed{
0,\frac12\in\operatorname{Acc}(A),
\qquad
2\notin\operatorname{Acc}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-036}

### 36. Da un ejemplo de un punto de acumulación que no pertenezca al conjunto y otro de un punto de acumulación que sí pertenezca.

Podemos usar otra vez

$$
A=(0,1)\cup\{2\}.
$$

El punto

$$
0
$$

no pertenece a $A$, pero el microcontrol anterior muestra que

$$
0\in\operatorname{Acc}(A).
$$

Así, $0$ es un punto de acumulación exterior al conjunto.

Por otro lado,

$$
\frac12\in A
$$

y también

$$
\frac12\in\operatorname{Acc}(A).
$$

Por tanto,

$$
\boxed{
0\notin A,\ 0\in\operatorname{Acc}(A),
}
$$

mientras que

$$
\boxed{
\frac12\in A\cap\operatorname{Acc}(A).
}
$$

La acumulación no decide la pertenencia del centro.

[]{#MA-MSOL-ANM-01-004-037}

### 37. Demuestra que ningún punto exterior a $A$ puede pertenecer a $\operatorname{Acc}(A)$.

Supongamos

$$
x\in\operatorname{ext}(A).
$$

Entonces existe $r>0$ tal que

$$
B(x,r)\cap A=\varnothing.
$$

Como

$$
B(x,r)\setminus\{x\}
\subseteq
B(x,r),
$$

también

$$
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A=\varnothing.
$$

Así hemos encontrado un radio positivo para el cual falla la condición universal de acumulación.

Por tanto,

$$
x\notin\operatorname{Acc}(A).
$$

Concluimos

$$
\boxed{
\operatorname{Acc}(A)\cap\operatorname{ext}(A)=\varnothing.
}
$$

[]{#MA-MSOL-ANM-01-004-038}

### 38. Prueba $\overline A=A\cup\operatorname{Acc}(A)$ sin usar sucesiones.

Primero,

$$
A\subseteq\overline A
$$

y

$$
\operatorname{Acc}(A)\subseteq\overline A.
$$

Por tanto,

$$
A\cup\operatorname{Acc}(A)
\subseteq
\overline A.
$$

Para la inclusión contraria, sea

$$
x\in\overline A.
$$

Si

$$
x\in A,
$$

entonces ya tenemos

$$
x\in A\cup\operatorname{Acc}(A).
$$

Supongamos ahora

$$
x\notin A.
$$

Como $x\in\overline A$, para todo $r>0$,

$$
B(x,r)\cap A\ne\varnothing.
$$

Pero como $x\notin A$, cualquier punto de esa intersección es automáticamente distinto de $x$.

Por tanto,

$$
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A\ne\varnothing
$$

para todo $r>0$.

Así,

$$
x\in\operatorname{Acc}(A).
$$

Luego,

$$
\overline A
\subseteq
A\cup\operatorname{Acc}(A).
$$

Por ambas inclusiones,

$$
\boxed{
\overline A
=
A\cup\operatorname{Acc}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-039}

### 39. Si $A\subseteq B$, demuestra $\operatorname{Acc}(A)\subseteq\operatorname{Acc}(B)$.

Supongamos

$$
A\subseteq B
$$

y sea

$$
x\in\operatorname{Acc}(A).
$$

Entonces para todo $r>0$,

$$
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A\ne\varnothing.
$$

Sea $r>0$. Elijamos

$$
a\in
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A.
$$

Como $A\subseteq B$, el mismo punto satisface

$$
a\in B.
$$

Así,

$$
a\in
\bigl(B(x,r)\setminus\{x\}\bigr)\cap B.
$$

Por tanto,

$$
\bigl(B(x,r)\setminus\{x\}\bigr)\cap B\ne\varnothing
$$

para todo $r>0$.

Luego,

$$
x\in\operatorname{Acc}(B).
$$

Concluimos

$$
\boxed{
A\subseteq B
\Longrightarrow
\operatorname{Acc}(A)\subseteq\operatorname{Acc}(B).
}
$$

[]{#MA-MSOL-ANM-01-004-040}

### 40. Para $a<b$, demuestra directamente mediante bolas perforadas que $\operatorname{Acc}((a,b))=[a,b]$.

Sea

$$
A=(a,b).
$$

Primero demostremos

$$
[a,b]\subseteq\operatorname{Acc}(A).
$$

Si

$$
x\in(a,b),
$$

sea $r>0$. Tomemos

$$
\delta
=
\min\left\{
\frac r2,\frac{b-x}{2}
\right\}>0
$$

y definamos

$$
y=x+\delta.
$$

Entonces

$$
x<y<b,
$$

de modo que $y\in A$, además $y\ne x$ y $|y-x|<r$. Así,

$$
x\in\operatorname{Acc}(A).
$$

Para $x=a$, dado $r>0$, tomemos

$$
y=
a+
\min\left\{
\frac r2,\frac{b-a}{2}
\right\}.
$$

Entonces

$$
a<y<b,
$$

$y\ne a$ y $|y-a|<r$. Por tanto,

$$
a\in\operatorname{Acc}(A).
$$

Para $x=b$, tomemos

$$
y=
b-
\min\left\{
\frac r2,\frac{b-a}{2}
\right\}.
$$

Análogamente,

$$
a<y<b,
$$

$y\ne b$ y $|y-b|<r$, de modo que

$$
b\in\operatorname{Acc}(A).
$$

Así,

$$
[a,b]\subseteq\operatorname{Acc}(A).
$$

Ahora sea

$$
x<a.
$$

Tomemos

$$
r=\frac{a-x}{2}>0.
$$

Entonces

$$
B(x,r)\subset(-\infty,a),
$$

por lo que

$$
B(x,r)\cap A=\varnothing.
$$

Así,

$$
x\notin\operatorname{Acc}(A).
$$

Si

$$
x>b,
$$

tomamos

$$
r=\frac{x-b}{2}>0,
$$

y obtenemos una bola disjunta de $A$. Por tanto tampoco es punto de acumulación.

No quedan más casos. Luego,

$$
\boxed{
\operatorname{Acc}((a,b))=[a,b].
}
$$

## §4.6. Puntos aislados y descomposición local

[]{#MA-MSOL-ANM-01-004-041}

### 41. Demuestra directamente que si $x$ es aislado en $A$, entonces $x\in\overline A$ pero $x\notin\operatorname{Acc}(A)$.

Si $x$ es aislado en $A$, entonces

$$
x\in A
$$

y existe $r>0$ tal que

$$
B(x,r)\cap A=\{x\}.
$$

Como $x\in A$ y siempre $A\subseteq\overline A$, obtenemos

$$
x\in\overline A.
$$

Además,

$$
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A=\varnothing.
$$

Así existe un radio positivo para el cual falla el test universal de acumulación. Por tanto,

$$
x\notin\operatorname{Acc}(A).
$$

En conclusión,

$$
\boxed{
x\text{ aislado en }A
\Longrightarrow
x\in\overline A
\ \text{y}\
x\notin\operatorname{Acc}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-042}

### 42. Prueba la equivalencia $x\text{ aislado en }A\iff x\in A\setminus\operatorname{Acc}(A)$.

Supongamos primero que $x$ es aislado en $A$. Entonces

$$
x\in A
$$

y, por el microcontrol anterior,

$$
x\notin\operatorname{Acc}(A).
$$

Por tanto,

$$
x\in A\setminus\operatorname{Acc}(A).
$$

Recíprocamente, supongamos

$$
x\in A\setminus\operatorname{Acc}(A).
$$

Entonces $x\in A$ y

$$
x\notin\operatorname{Acc}(A).
$$

Negar la acumulación significa que existe $r>0$ tal que

$$
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A=\varnothing.
$$

Como además $x\in A$ y $x\in B(x,r)$, la única intersección posible es el propio centro:

$$
B(x,r)\cap A=\{x\}.
$$

Así, $x$ es aislado en $A$.

Por tanto,

$$
\boxed{
x\text{ aislado en }A
\iff
x\in A\setminus\operatorname{Acc}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-043}

### 43. Para $A=(0,1)\cup\{2\}$, clasifica $0$, $1/2$ y $2$ respecto de pertenencia, adherencia, acumulación y aislamiento.

Para $x=0$:

$$
0\notin A.
$$

Sin embargo, toda bola positiva centrada en $0$ intersecta $(0,1)$, por lo que

$$
0\in\overline A
$$

y

$$
0\in\operatorname{Acc}(A).
$$

Como $0\notin A$, no puede ser aislado en $A$.

Para $x=1/2$:

$$
\frac12\in A.
$$

Además, aparecen puntos de $(0,1)$ distintos de $1/2$ arbitrariamente cerca, de modo que

$$
\frac12\in\overline A
$$

y

$$
\frac12\in\operatorname{Acc}(A).
$$

Por tanto no es aislado.

Para $x=2$:

$$
2\in A\subseteq\overline A.
$$

Pero

$$
B\left(2,\frac12\right)\cap A=\{2\},
$$

de modo que

$$
2\notin\operatorname{Acc}(A).
$$

Así, $2$ es aislado en $A$.

La clasificación es

$$
\begin{array}{c|c|c|c|c}
x & x\in A & x\in\overline A & x\in\operatorname{Acc}(A) & \text{aislado}\\
\hline
0 & \text{no} & \text{sí} & \text{sí} & \text{no}\\
1/2 & \text{sí} & \text{sí} & \text{sí} & \text{no}\\
2 & \text{sí} & \text{sí} & \text{no} & \text{sí}
\end{array}
$$

[]{#MA-MSOL-ANM-01-004-044}

### 44. Demuestra que todo $n\in\mathbb Z$ es aislado en $\mathbb Z$ usando un radio que pueda elegirse igual para todos los enteros.

Sea

$$
n\in\mathbb Z.
$$

Tomemos el radio uniforme

$$
r=\frac12.
$$

Si

$$
m\in\mathbb Z
$$

y

$$
m\ne n,
$$

entonces

$$
|m-n|\ge1.
$$

Por tanto ningún entero distinto de $n$ pertenece a

$$
B\left(n,\frac12\right).
$$

Como $n$ sí pertenece a esa bola,

$$
B\left(n,\frac12\right)\cap\mathbb Z=\{n\}.
$$

Así,

$$
\boxed{
\text{todo }n\in\mathbb Z\text{ es aislado en }\mathbb Z.
}
$$

El mismo radio $1/2$ sirve para todos los enteros.

[]{#MA-MSOL-ANM-01-004-045}

### 45. Demuestra directamente que $\mathbb Z\cap\operatorname{Acc}(\mathbb Z)=\varnothing$.

Sea

$$
n\in\mathbb Z.
$$

Por el microcontrol anterior,

$$
B\left(n,\frac12\right)\cap\mathbb Z=\{n\}.
$$

Al perforar el centro,

$$
\left(
B\left(n,\frac12\right)\setminus\{n\}
\right)\cap\mathbb Z
=
\varnothing.
$$

Por tanto,

$$
n\notin\operatorname{Acc}(\mathbb Z).
$$

Como esto vale para todo

$$
n\in\mathbb Z,
$$

ningún punto del propio conjunto $\mathbb Z$ es de acumulación.

Así,

$$
\boxed{
\mathbb Z\cap\operatorname{Acc}(\mathbb Z)=\varnothing.
}
$$

Esta afirmación es local respecto de los puntos pertenecientes a $\mathbb Z$ y no requiere clasificar aquí los centros reales exteriores a $\mathbb Z$.

[]{#MA-MSOL-ANM-01-004-046}

### 46. Sea $F\subseteq\mathbb R$ finito. Demuestra que cada punto de $F$ es aislado. Separa explícitamente el caso en que $F$ tiene un solo elemento.

Si

$$
F=\{x\},
$$

entonces cualquier radio $r>0$ satisface

$$
B(x,r)\cap F=\{x\}.
$$

Por tanto $x$ es aislado.

Supongamos ahora que

$$
F=\{x_1,\dots,x_n\},
\qquad
n\ge2,
$$

con puntos distintos.

Fijemos

$$
x_k\in F.
$$

Las distancias

$$
|x_k-x_j|,
\qquad
j\ne k,
$$

son positivas y forman una familia finita. Por tanto existe

$$
d_k=
\min_{j\ne k}|x_k-x_j|>0.
$$

Tomemos

$$
r=\frac{d_k}{2}.
$$

Si $j\ne k$, entonces

$$
|x_j-x_k|\ge d_k>r,
$$

de modo que

$$
x_j\notin B(x_k,r).
$$

El único punto de $F$ dentro de la bola es $x_k$:

$$
B(x_k,r)\cap F=\{x_k\}.
$$

Así, $x_k$ es aislado.

Como $x_k$ era arbitrario,

$$
\boxed{
\text{todo punto de un conjunto finito }F\text{ es aislado en }F.
}
$$

[]{#MA-MSOL-ANM-01-004-047}

### 47. Explica por qué el hecho de que $x$ sea aislado en $A$ no implica que $\{x\}$ contenga una bola abierta de $\mathbb R$ alrededor de $x$.

Que $x$ sea aislado en $A$ significa que existe $r>0$ tal que

$$
B(x,r)\cap A=\{x\}.
$$

Esta igualdad sólo controla qué puntos de **$A$** aparecen dentro de la bola.

No afirma

$$
B(x,r)\subseteq\{x\}.
$$

De hecho, toda bola positiva centrada en $x$ contiene infinitos números reales distintos de $x$. Por ejemplo,

$$
x+\frac r2\in B(x,r)
$$

y

$$
x+\frac r2\ne x.
$$

Por tanto,

$$
B(x,r)\not\subseteq\{x\}.
$$

Así, aislamiento significa que $x$ queda solo **respecto del conjunto $A$**, no que el singleton $\{x\}$ contenga una bola de la recta real.

[]{#MA-MSOL-ANM-01-004-048}

### 48. Demuestra la descomposición disjunta $A=(A\cap\operatorname{Acc}(A))\,\dot\cup\,(A\setminus\operatorname{Acc}(A))$, e interpreta matemáticamente ambas partes.

Todo punto de $A$ cae en una de dos posibilidades:

$$
x\in\operatorname{Acc}(A)
$$

o

$$
x\notin\operatorname{Acc}(A).
$$

Por tanto,

$$
A
=
\bigl(A\cap\operatorname{Acc}(A)\bigr)
\cup
\bigl(A\setminus\operatorname{Acc}(A)\bigr).
$$

Las dos partes son disjuntas por definición: ningún punto puede pertenecer simultáneamente a $\operatorname{Acc}(A)$ y a su complemento.

Así,

$$
\boxed{
A
=
\bigl(A\cap\operatorname{Acc}(A)\bigr)
\,\dot\cup\,
\bigl(A\setminus\operatorname{Acc}(A)\bigr).
}
$$

La primera parte contiene los puntos de $A$ que son puntos de acumulación: otros puntos de $A$ reaparecen arbitrariamente cerca.

La segunda parte contiene exactamente los puntos aislados, porque

$$
x\text{ aislado en }A
\iff
x\in A\setminus\operatorname{Acc}(A).
$$

Por tanto la descomposición separa exhaustivamente, dentro del propio conjunto, los puntos acumulados de los puntos aislados.

## §4.7. Abiertos y cerrados: de lo local a lo global

[]{#MA-MSOL-ANM-01-004-049}

### 49. Demuestra directamente, usando la definición, que todo intervalo abierto $(a,b)$ es un conjunto abierto.

Sea

$$
x\in(a,b).
$$

Entonces

$$
x-a>0
\qquad\text{y}\qquad
b-x>0.
$$

Tomemos

$$
r_x=
\frac12\min\{x-a,b-x\}>0.
$$

Si

$$
y\in B(x,r_x),
$$

entonces

$$
|y-x|<r_x.
$$

De aquí se sigue

$$
a<y<b.
$$

Por tanto,

$$
B(x,r_x)\subseteq(a,b).
$$

Como $x\in(a,b)$ era arbitrario, cada punto del intervalo posee una bola contenida en él.

Así,

$$
\boxed{
(a,b)\text{ es abierto.}
}
$$

[]{#MA-MSOL-ANM-01-004-050}

### 50. Prueba $A\text{ abierto}\iff A=\operatorname{int}(A)$.

Supongamos primero que $A$ es abierto.

Entonces todo punto de $A$ es interior a $A$, de modo que

$$
A\subseteq\operatorname{int}(A).
$$

Pero siempre

$$
\operatorname{int}(A)\subseteq A.
$$

Por ambas inclusiones,

$$
A=\operatorname{int}(A).
$$

Recíprocamente, supongamos

$$
A=\operatorname{int}(A).
$$

Sea

$$
x\in A.
$$

Entonces

$$
x\in\operatorname{int}(A),
$$

por lo que existe $r>0$ tal que

$$
B(x,r)\subseteq A.
$$

Así, todo punto de $A$ es interior y, por definición,

$$
A\text{ es abierto}.
$$

Por tanto,

$$
\boxed{
A\text{ abierto}
\iff
A=\operatorname{int}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-051}

### 51. Sea $\{A_i\}_{i\in I}$ una familia arbitraria de abiertos. Demuestra que $\bigcup_{i\in I}A_i$ es abierto, identificando exactamente dónde se elige un índice de la familia.

Definamos

$$
A=\bigcup_{i\in I}A_i.
$$

Sea

$$
x\in A.
$$

Por definición de unión, existe al menos un índice

$$
j\in I
$$

tal que

$$
x\in A_j.
$$

Aquí se elige el índice de la familia.

Como $A_j$ es abierto, existe $r>0$ tal que

$$
B(x,r)\subseteq A_j.
$$

Y como

$$
A_j\subseteq\bigcup_{i\in I}A_i=A,
$$

obtenemos

$$
B(x,r)\subseteq A.
$$

Por tanto $x$ es interior a $A$.

Como $x$ era arbitrario,

$$
\boxed{
\bigcup_{i\in I}A_i
\text{ es abierto.}
}
$$

La familia puede ser arbitraria porque, para un punto de la unión, basta encontrar **un** conjunto de la familia que lo contenga.

[]{#MA-MSOL-ANM-01-004-052}

### 52. Demuestra que la intersección de dos abiertos es abierta y explica por qué aparece el radio $\min\{r,s\}$.

Sean $A$ y $B$ abiertos y sea

$$
x\in A\cap B.
$$

Como $A$ es abierto, existe $r>0$ tal que

$$
B(x,r)\subseteq A.
$$

Como $B$ es abierto, existe $s>0$ tal que

$$
B(x,s)\subseteq B.
$$

Para satisfacer simultáneamente ambas inclusiones, elegimos

$$
\rho=\min\{r,s\}>0.
$$

Entonces

$$
B(x,\rho)\subseteq B(x,r)\subseteq A
$$

y

$$
B(x,\rho)\subseteq B(x,s)\subseteq B.
$$

Por tanto,

$$
B(x,\rho)\subseteq A\cap B.
$$

Así, $x$ es interior a $A\cap B$.

Como $x$ era arbitrario,

$$
\boxed{
A\cap B\text{ es abierto.}
}
$$

El mínimo aparece porque necesitamos un único radio que no exceda ninguno de los dos radios disponibles.

[]{#MA-MSOL-ANM-01-004-053}

### 53. Prueba $F\text{ cerrado}\iff F=\overline F$ únicamente con las definiciones y la dualidad entre exterior y clausura.

Supongamos primero que $F$ es cerrado.

Entonces

$$
F^c
$$

es abierto.

Sea

$$
x\notin F.
$$

Entonces

$$
x\in F^c.
$$

Como $F^c$ es abierto, existe $r>0$ tal que

$$
B(x,r)\subseteq F^c.
$$

Por tanto,

$$
B(x,r)\cap F=\varnothing,
$$

de modo que

$$
x\notin\overline F.
$$

Hemos probado

$$
\overline F\subseteq F.
$$

Pero siempre

$$
F\subseteq\overline F.
$$

Así,

$$
F=\overline F.
$$

Recíprocamente, supongamos

$$
F=\overline F.
$$

Sea

$$
x\in F^c.
$$

Entonces

$$
x\notin\overline F.
$$

Como

$$
\overline F
=
(\operatorname{ext}(F))^c,
$$

se sigue que

$$
x\in\operatorname{ext}(F).
$$

Por tanto existe $r>0$ tal que

$$
B(x,r)\subseteq F^c.
$$

Así, todo punto de $F^c$ es interior a $F^c$, y por tanto $F^c$ es abierto.

Luego,

$$
F\text{ es cerrado}.
$$

Concluimos

$$
\boxed{
F\text{ cerrado}
\iff
F=\overline F.
}
$$

[]{#MA-MSOL-ANM-01-004-054}

### 54. Deduce $A\text{ cerrado}\iff\operatorname{Acc}(A)\subseteq A$.

Sabemos que

$$
A\text{ cerrado}
\iff
A=\overline A.
$$

También sabemos que

$$
\overline A
=
A\cup\operatorname{Acc}(A).
$$

Por tanto,

$$
A\text{ cerrado}
$$

si y sólo si

$$
A
=
A\cup\operatorname{Acc}(A).
$$

Esta igualdad ocurre exactamente cuando

$$
\operatorname{Acc}(A)\subseteq A.
$$

Así,

$$
\boxed{
A\text{ cerrado}
\iff
\operatorname{Acc}(A)\subseteq A.
}
$$

La condición no dice que todos los puntos de $A$ sean de acumulación; sólo exige que ningún punto de acumulación quede fuera del conjunto.

[]{#MA-MSOL-ANM-01-004-055}

### 55. Demuestra que $\overline A$ es el menor conjunto cerrado que contiene a $A$.

Primero,

$$
A\subseteq\overline A.
$$

Además, por idempotencia,

$$
\overline{\overline A}
=
\overline A.
$$

Por la caracterización de cerrados,

$$
\overline A
$$

es cerrado.

Así, $\overline A$ es un conjunto cerrado que contiene a $A$.

Ahora sea $F$ cualquier conjunto cerrado con

$$
A\subseteq F.
$$

Por monotonicidad de la clausura,

$$
\overline A
\subseteq
\overline F.
$$

Como $F$ es cerrado,

$$
\overline F=F.
$$

Por tanto,

$$
\overline A\subseteq F.
$$

Así,

$$
\boxed{
\overline A
\text{ es el menor conjunto cerrado que contiene a }A.
}
$$

[]{#MA-MSOL-ANM-01-004-056}

### 56. Usa complementos y las leyes de De Morgan para demostrar que las intersecciones arbitrarias de cerrados son cerradas y las uniones finitas de cerrados son cerradas.

Sea

$$
\{F_i\}_{i\in I}
$$

una familia de conjuntos cerrados.

Entonces cada

$$
F_i^c
$$

es abierto.

Por De Morgan,

$$
\left(
\bigcap_{i\in I}F_i
\right)^c
=
\bigcup_{i\in I}F_i^c.
$$

La unión arbitraria de abiertos es abierta. Por tanto,

$$
\left(
\bigcap_{i\in I}F_i
\right)^c
$$

es abierto, y así

$$
\boxed{
\bigcap_{i\in I}F_i
\text{ es cerrado.}
}
$$

Ahora sean

$$
F_1,\dots,F_n
$$

cerrados.

Por De Morgan,

$$
\left(
\bigcup_{k=1}^nF_k
\right)^c
=
\bigcap_{k=1}^nF_k^c.
$$

Cada complemento es abierto y una intersección finita de abiertos es abierta. Por tanto,

$$
\left(
\bigcup_{k=1}^nF_k
\right)^c
$$

es abierto.

Así,

$$
\boxed{
\bigcup_{k=1}^nF_k
\text{ es cerrado.}
}
$$

[]{#MA-MSOL-ANM-01-004-057}

### 57. Clasifica $(0,1)$, $[0,1]$, $[0,1)$, $\varnothing$ y $\mathbb R$ como abiertos, cerrados, ambos o ninguno, justificando cada respuesta mediante los criterios de esta sección.

Para

$$
(0,1),
$$

cada punto posee margen interior, así que el conjunto es abierto. No es cerrado porque

$$
\overline{(0,1)}=[0,1]\ne(0,1).
$$

Por tanto,

$$
\boxed{
(0,1)\text{ es abierto y no cerrado.}
}
$$

Para

$$
[0,1],
$$

tenemos

$$
\overline{[0,1]}=[0,1],
$$

así que es cerrado. No es abierto porque $0$ y $1$ no son puntos interiores.

Por tanto,

$$
\boxed{
[0,1]\text{ es cerrado y no abierto.}
}
$$

Para

$$
[0,1),
$$

el punto $0$ pertenece al conjunto pero no es interior, de modo que no es abierto.

Además,

$$
1\in\overline{[0,1)}
$$

pero

$$
1\notin[0,1),
$$

así que

$$
[0,1)\ne\overline{[0,1)}.
$$

Por tanto,

$$
\boxed{
[0,1)\text{ no es abierto ni cerrado.}
}
$$

El conjunto vacío es abierto por vacuidad. Como

$$
\varnothing^c=\mathbb R
$$

y $\mathbb R$ es abierto, $\varnothing$ también es cerrado.

Así,

$$
\boxed{
\varnothing\text{ es abierto y cerrado.}
}
$$

Finalmente, $\mathbb R$ es abierto porque toda bola real permanece en $\mathbb R$. Como

$$
\mathbb R^c=\varnothing
$$

y $\varnothing$ es abierto, $\mathbb R$ también es cerrado.

Por tanto,

$$
\boxed{
\mathbb R\text{ es abierto y cerrado.}
}
$$

## §4.8. Un diccionario local para leer conjuntos

[]{#MA-MSOL-ANM-01-004-058}

### 58. Completa, sin consultar las secciones anteriores, los seis tests locales para interior, exterior, adherencia, frontera, acumulación y aislamiento. Después verifica cada cuantificador.

Los seis tests son

$$
x\in\operatorname{int}(A)
\iff
\exists r>0:\ B(x,r)\subseteq A,
$$

$$
x\in\operatorname{ext}(A)
\iff
\exists r>0:\ B(x,r)\subseteq A^c,
$$

$$
x\in\overline A
\iff
\forall r>0:\ B(x,r)\cap A\ne\varnothing,
$$

$$
x\in\partial A
\iff
\forall r>0:
\begin{cases}
B(x,r)\cap A\ne\varnothing,\\
B(x,r)\cap A^c\ne\varnothing,
\end{cases}
$$

$$
x\in\operatorname{Acc}(A)
\iff
\forall r>0:
\bigl(B(x,r)\setminus\{x\}\bigr)\cap A\ne\varnothing,
$$

y

$$
x\text{ aislado en }A
\iff
x\in A
\ \text{y}\
\exists r>0:\ B(x,r)\cap A=\{x\}.
$$

Interior, exterior y aislamiento buscan algún radio favorable. Adherencia, frontera y acumulación exigen controlar todo radio positivo. La frontera observa simultáneamente $A$ y $A^c$; la acumulación perfora el centro.

[]{#MA-MSOL-ANM-01-004-059}

### 59. Demuestra de nuevo $\operatorname{int}(A)\subseteq A\subseteq\overline A$, indicando qué definición justifica cada inclusión.

Sea

$$
x\in\operatorname{int}(A).
$$

Existe $r>0$ tal que

$$
B(x,r)\subseteq A.
$$

Como $x\in B(x,r)$, se sigue que $x\in A$. Por tanto,

$$
\operatorname{int}(A)\subseteq A.
$$

Ahora sea $x\in A$. Para cualquier $r>0$,

$$
x\in B(x,r)\cap A.
$$

Así,

$$
B(x,r)\cap A\ne\varnothing
$$

para todo $r>0$, y por tanto $x\in\overline A$.

Concluimos

$$
\boxed{
\operatorname{int}(A)\subseteq A\subseteq\overline A.
}
$$

La primera inclusión usa la definición de interior; la segunda, la definición de adherencia.

[]{#MA-MSOL-ANM-01-004-060}

### 60. Prueba $\operatorname{int}(\operatorname{int}(A))=\operatorname{int}(A)$ y compara su mecanismo con la prueba de $\overline{\overline A}=\overline A$.

Siempre,

$$
\operatorname{int}(\operatorname{int}(A))
\subseteq
\operatorname{int}(A),
$$

porque $\operatorname{int}(B)\subseteq B$ para todo conjunto $B$.

Para la inclusión contraria, sea $x\in\operatorname{int}(A)$. Existe $r>0$ tal que

$$
B(x,r)\subseteq A.
$$

La bola $B(x,r)$ es abierta, de modo que todos sus puntos son interiores a $A$:

$$
B(x,r)\subseteq\operatorname{int}(A).
$$

Así,

$$
x\in\operatorname{int}(\operatorname{int}(A)).
$$

Por tanto,

$$
\boxed{
\operatorname{int}(\operatorname{int}(A))
=
\operatorname{int}(A).
}
$$

El mecanismo es dual al de la idempotencia de la clausura: una vez aplicada la operación, repetirla no descubre una capa local nueva.

[]{#MA-MSOL-ANM-01-004-061}

### 61. Para $a<b$, construye una tabla con interior, clausura, frontera y condición abierto/cerrado de $(a,b)$, $[a,b]$ y $[a,b)$.

Los tres conjuntos tienen

$$
\operatorname{int}(A)=(a,b),
\qquad
\overline A=[a,b],
\qquad
\partial A=\{a,b\}.
$$

La clasificación es

$$
\begin{array}{c|c|c|c|c}
A & \operatorname{int}(A) & \overline A & \partial A & \text{clasificación}\\
\hline
(a,b) & (a,b) & [a,b] & \{a,b\} & \text{abierto, no cerrado}\\
[a,b] & (a,b) & [a,b] & \{a,b\} & \text{cerrado, no abierto}\\
[a,b) & (a,b) & [a,b] & \{a,b\} & \text{ni abierto ni cerrado}
\end{array}
$$

La diferencia está en la pertenencia de los extremos, mientras que la clausura y la frontera permanecen invariantes.

[]{#MA-MSOL-ANM-01-004-062}

### 62. Para $A=(0,1)\cup\{2\}$, determina $\operatorname{int}(A)$, $\overline A$, $\partial A$ y $\operatorname{Acc}(A)$, y explica qué propiedad local distingue al punto $2$.

Tenemos

$$
\operatorname{int}(A)=(0,1),
$$

$$
\overline A=[0,1]\cup\{2\},
$$

$$
\partial A=\{0,1,2\},
$$

y

$$
\operatorname{Acc}(A)=[0,1].
$$

El punto $2$ se distingue porque es aislado. Por ejemplo,

$$
B\left(2,\frac12\right)\cap A=\{2\}.
$$

Así,

$$
2\in A\setminus\operatorname{Acc}(A).
$$

Es adherente y fronterizo, pero no es punto de acumulación.

[]{#MA-MSOL-ANM-01-004-063}

### 63. Para $A=(0,1)\setminus\{1/2\}$, explica por qué $1/2$ pertenece simultáneamente a $\overline A$, $\partial A$ y $\operatorname{Acc}(A)$, pero no a $A$.

Por construcción,

$$
\frac12\notin A.
$$

Sea $r>0$ y tomemos

$$
a=
\frac12+
\min\left\{
\frac r2,\frac14
\right\}.
$$

Entonces $a\in A$, $a\ne1/2$ y

$$
\left|a-\frac12\right|<r.
$$

Por tanto,

$$
\frac12\in\operatorname{Acc}(A).
$$

Como $\operatorname{Acc}(A)\subseteq\overline A$,

$$
\frac12\in\overline A.
$$

Además, el propio centro $1/2$ pertenece a $A^c$ y a toda bola centrada en él. Así, toda bola toca $A$ y $A^c$:

$$
\frac12\in\partial A.
$$

Por tanto,

$$
\boxed{
\frac12\notin A,
\qquad
\frac12\in\overline A\cap\partial A\cap\operatorname{Acc}(A).
}
$$

[]{#MA-MSOL-ANM-01-004-064}

### 64. Decide cuál es la negación correcta de cada afirmación y explica qué noción del capítulo aparece al interpretar cada negación.

La negación de

$$
\exists r>0:\ B(x,r)\subseteq A
$$

es

$$
\forall r>0:\ B(x,r)\not\subseteq A.
$$

Equivalentemente,

$$
\forall r>0:\ B(x,r)\cap A^c\ne\varnothing,
$$

es decir,

$$
x\in\overline{A^c}.
$$

La negación de

$$
\forall r>0:\ B(x,r)\cap A\ne\varnothing
$$

es

$$
\exists r>0:\ B(x,r)\cap A=\varnothing,
$$

que equivale a

$$
x\in\operatorname{ext}(A).
$$

La negación de

$$
\forall r>0:
(B(x,r)\setminus\{x\})\cap A\ne\varnothing
$$

es

$$
\exists r>0:
(B(x,r)\setminus\{x\})\cap A=\varnothing.
$$

Si además $x\in A$, esto equivale a

$$
B(x,r)\cap A=\{x\},
$$

y por tanto $x$ es aislado en $A$.

Así, negar un universal produce un radio testigo, mientras que negar un existencial obliga a controlar todos los radios.

[]{#MA-MSOL-ANM-01-004-065}

### 65. Resume en dos o tres frases el mecanismo común de C04 sin enumerar definiciones. Tu resumen debe explicar qué papel cumplen la ventana, el cuantificador y el conjunto observado.

C04 estudia un conjunto fijando un punto y observando qué puede o debe ocurrir dentro de las ventanas $B(x,r)$ al cambiar la escala. El cuantificador decide si basta encontrar una ventana favorable o si la condición debe cumplirse para todas, mientras que el conjunto observado —$A$, $A^c$, ambos lados o la bola perforada— determina qué rasgo local se está leyendo.

Una misma infraestructura métrica produce así todo el diccionario local del capítulo.
