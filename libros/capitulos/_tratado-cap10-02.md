## 10.2. Aproximantes racionales y política de elección {#sec-ta-10-2}

La equivalencia de §10.1 permite medir la condición de Cauchy mediante escalas racionales, pero todavía no nos entrega una sucesión racional concreta que pueda diagonalizarse.

Hay una dificultad fundacional que no debemos ocultar. Para cada término

$$
x_n\in\mathbb R_C
$$

podríamos afirmar que existe una sucesión racional de Cauchy que lo representa. Sin embargo, escoger simultáneamente un representante para cada $x_n$ sería una elección numerable de elementos de clases de equivalencia. El argumento usual de manual suele efectuar esa selección sin comentarla; aquí no lo haremos.

La estrategia será distinta:

1. construir una enumeración fija y definible de $\mathbb Q$;
2. demostrar que todo $x\in\mathbb R_C$ admite racionales arbitrariamente próximos;
3. entre todos los racionales suficientemente próximos, escoger el primero que aparece en la enumeración fijada.

El buen orden de $\mathbb N$ convertirá así una existencia local en una función canónica, sin utilizar ningún principio de elección.

### Definición 10.2.1 — Código natural de pares

Definimos

$$
\kappa_2:
\mathbb N\times\mathbb N
\longrightarrow
\mathbb N
$$

por

$$
\boxed{
\kappa_2(a,b)
=
(a+b)(a+b)+a.
}
$$

No pretendemos que $\kappa_2$ recorra consecutivamente todos los naturales. Sólo necesitamos que pares distintos reciban códigos distintos.

### Lema 10.2.2 — Inyectividad del código de pares

La función $\kappa_2$ es inyectiva.

**Demostración.**

Supongamos

$$
\kappa_2(a,b)=\kappa_2(c,d).
$$

Pongamos

$$
s:=a+b,
\qquad
t:=c+d.
$$

Como $a\le s$, la compatibilidad del orden natural con la suma da

$$
s\cdot s+a\le s\cdot s+s.
$$

Análogamente,

$$
t\cdot t\le t\cdot t+c.
$$

Afirmamos que $s<t$ implicaría

$$
\kappa_2(a,b)<\kappa_2(c,d).
$$

En efecto, la caracterización aritmética del orden natural, junto con la existencia de predecesor para todo natural no nulo, da

$$
s<t
\Longrightarrow
S(s)\le t.
$$

Por compatibilidad del orden con el producto,

$$
S(s)\cdot S(s)\le t\cdot t.
$$

Por las leyes de sucesor, producto y suma,

$$
s\cdot s+s<S(s)\cdot S(s).
$$

Por tanto

$$
\kappa_2(a,b)
=
s\cdot s+a
\le
s\cdot s+s
<
S(s)\cdot S(s)
\le
t\cdot t
\le
t\cdot t+c
=
\kappa_2(c,d),
$$

contradicción con la igualdad supuesta.

El caso $t<s$ produce simétricamente la contradicción opuesta. Como el orden de $\mathbb N$ es total,

$$
s=t.
$$

La igualdad de códigos se reduce entonces a

$$
s\cdot s+a=s\cdot s+c.
$$

Por cancelación aditiva,

$$
a=c.
$$

Finalmente,

$$
a+b=c+d
$$

y $a=c$, de modo que una segunda cancelación da

$$
b=d.
$$

Luego

$$
(a,b)=(c,d),
$$

y $\kappa_2$ es inyectiva. ∎

### Definición 10.2.3 — Decodificador canónico de pares

Definimos

$$
d_2:
\mathbb N
\longrightarrow
\mathbb N\times\mathbb N
$$

por la regla

$$
\boxed{
d_2(n)
=
\begin{cases}
(a,b),
&
\text{si existe }(a,b)\in\mathbb N\times\mathbb N
\text{ con }\kappa_2(a,b)=n,
\\[1mm]
(0,0),
&
\text{si no existe tal par}.
\end{cases}
}
$$

La primera rama determina a lo sumo un par por Lema 10.2.2 — Inyectividad del código de pares; la segunda determina explícitamente el valor cuando $n$ no es código de ningún par. El grafo de $d_2$ se obtiene por separación, de modo que $d_2$ es una función total y definible.

### Proposición 10.2.4 — Sobreyectividad del decodificador

La función

$$
d_2:\mathbb N\to\mathbb N\times\mathbb N
$$

es sobreyectiva.

**Demostración.**

Sea $(a,b)\in\mathbb N\times\mathbb N$. Consideremos el natural

$$
n:=\kappa_2(a,b).
$$

Por definición, existe un par cuyo código es $n$, a saber $(a,b)$. La primera rama de Definición 10.2.3 — Decodificador canónico de pares se aplica, y la unicidad garantizada por Lema 10.2.2 — Inyectividad del código de pares da

$$
d_2(n)=(a,b).
$$

Todo par natural aparece, por tanto, como valor de $d_2$. ∎

> **Nota.** $d_2$ puede repetir el par $(0,0)$ en los naturales que no son códigos. Esto es irrelevante: lo que necesitaremos es sobreyectividad, no biyectividad.

### Definición 10.2.5 — Enumeración racional canónica

A partir de $d_2$ construiremos una función fija

$$
e_{\mathbb Q}:\mathbb N\to\mathbb Q.
$$

Primero definimos una enumeración auxiliar de los enteros. Si

$$
d_2(n)=(a,b),
$$

ponemos

$$
\zeta(n):=[(a,b)]_{\mathbb Z}.
$$

Definimos además un denominador seguro

$$
\widehat\zeta(n)
:=
\begin{cases}
\zeta(n),&\text{si }\zeta(n)\neq0_{\mathbb Z},
\\
1_{\mathbb Z},&\text{si }\zeta(n)=0_{\mathbb Z}.
\end{cases}
$$

Como $d_2$ es una función y cada par determina una única clase entera, $\zeta$ es una función $\mathbb N\to\mathbb Z$. Por Proposición 2.8.2 — $0_{\mathbb Z}\neq1_{\mathbb Z}$,

$$
1_{\mathbb Z}\neq0_{\mathbb Z},
$$

así que

$$
\widehat\zeta(n)\in\mathbb Z_{\neq0}
$$

para todo $n$.

Finalmente, si

$$
d_2(n)=(i,j),
$$

definimos

$$
\boxed{
e_{\mathbb Q}(n)
:=
\frac{\zeta(i)}{\widehat\zeta(j)}.
}
$$

La fracción de la derecha es una clase racional legítima porque su denominador entero es no nulo.

Esta función queda fijada desde ahora para todo el tratado. La palabra enumeración se usa en el sentido de aplicación sobreyectiva; no se exige ausencia de repeticiones.

### Proposición 10.2.6 — La enumeración racional es sobreyectiva

La función

$$
e_{\mathbb Q}:\mathbb N\to\mathbb Q
$$

es sobreyectiva.

**Demostración.**

Primero observemos que

$$
\zeta:\mathbb N\to\mathbb Z
$$

es sobreyectiva. Sea $z\in\mathbb Z$. Por definición de $\mathbb Z$ como cociente existe $(a,b)\in\mathbb N\times\mathbb N$ tal que

$$
z=[(a,b)]_{\mathbb Z}.
$$

Por Proposición 10.2.4 — Sobreyectividad del decodificador, existe $i\in\mathbb N$ con

$$
d_2(i)=(a,b).
$$

Entonces

$$
\zeta(i)=z.
$$

Sea ahora $q\in\mathbb Q$. Como

$$
\mathbb Q
=
D_{\mathbb Q}/{\sim_{\mathbb Q}},
$$

existe un representante

$$
(z,w)\in D_{\mathbb Q}
=
\mathbb Z\times\mathbb Z_{\neq0}
$$

tal que

$$
q=\frac zw.
$$

Por la sobreyectividad de $\zeta$ existen $i,j\in\mathbb N$ con

$$
\zeta(i)=z,
\qquad
\zeta(j)=w.
$$

Como $w\neq0_{\mathbb Z}$,

$$
\widehat\zeta(j)=w.
$$

Por la sobreyectividad de $d_2$, existe $n\in\mathbb N$ tal que

$$
d_2(n)=(i,j).
$$

Por definición de $e_{\mathbb Q}$,

$$
e_{\mathbb Q}(n)
=
\frac{\zeta(i)}{\widehat\zeta(j)}
=
\frac zw
=
q.
$$

Así todo racional aparece en la enumeración. ∎

### Proposición 10.2.7 — Aproximación racional de todo real de Cauchy

Para todo $x\in\mathbb R_C$ y todo $\eta\in\mathbb Q$ con $0<\eta$, existe $q\in\mathbb Q$ tal que

$$
\boxed{
|x-\iota_C(q)|
<_C
\iota_C(\eta).
}
$$

**Demostración.**

Fijemos $x\in\mathbb R_C$ y $\eta\in\mathbb Q$ con $0<\eta$.

Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existe un representante

$$
a=(a_n)_{n\in\mathbb N}\in\mathcal C_{\mathbb Q}
$$

tal que

$$
x=[a]_C.
$$

Esta elección es local y sólo se usa para demostrar existencia.

Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q},
$$

$$
\rho:=\frac{\eta}{s},
\qquad
\delta:=\frac{\rho}{s}.
$$

Por las propiedades del cuerpo ordenado racional,

$$
0<\delta<\rho<\eta
$$

y

$$
\rho+\rho=\eta.
$$

Como $a$ es de Cauchy, aplicando Proposición 8.4.3 — Formulaciones equivalentes de la condición de Cauchy a la tolerancia $\rho$ existe $N\in\mathbb N$ tal que, para todo $n\ge N$,

$$
|a_n-a_N|<\rho.
$$

Definamos

$$
q:=a_N\in\mathbb Q.
$$

Sea

$$
y:=x-\iota_C(q).
$$

Las operaciones inducidas y la definición de $\iota_C$ dan

$$
y=[a-\underline q]_C.
$$

Para $n\ge N$, Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional transforma

$$
|a_n-q|<\rho
$$

en

$$
-\rho<a_n-q<\rho.
$$

Como $\delta<\rho$ y $\rho+\rho=\eta$,

$$
\rho+\delta
<
\rho+\rho
=
\eta.
$$

Por tanto, para todo $n\ge N$,

$$
(a_n-q)+\delta
<
\rho+\delta
<
\eta.
$$

El criterio de separación eventual Proposición 9.8.6 — Criterio de separación eventual para el orden estricto, aplicado a los representantes $a-\underline q$ y $\underline\eta$, produce

$$
y<_C\iota_C(\eta).
$$

Del otro lado, usando nuevamente $\delta<\rho$ y $\eta=\rho+\rho$,

$$
-\eta+\delta
=
-(\rho+\rho)+\delta
<
-(\rho+\rho)+\rho
=
-\rho.
$$

Por tanto,

$$
-\eta+\delta<-\rho<a_n-q
$$

para todo $n\ge N$. Aplicando nuevamente Proposición 9.8.6 — Criterio de separación eventual para el orden estricto, ahora a $\underline{-\eta}$ y $a-\underline q$, obtenemos

$$
\iota_C(-\eta)<_C y.
$$

Por preservación de opuestos,

$$
\iota_C(-\eta)
=
-\iota_C(\eta).
$$

En consecuencia,

$$
-\iota_C(\eta)
<_C
y
<_C
\iota_C(\eta).
$$

Además,

$$
0_C<_C\iota_C(\eta)
$$

por Proposición 9.9.5 — Preservación y reflexión del orden racional. Si $0_C\le_C y$, la definición del valor absoluto da $|y|=y$; si $y<_C0_C$, entonces $|y|=-y$, y la desigualdad izquierda anterior, al tomar opuestos, da nuevamente $|y|<_C\iota_C(\eta)$.

Así, en ambos casos,

$$
|y|<_C\iota_C(\eta),
$$

es decir,

$$
|x-\iota_C(q)|
<_C
\iota_C(\eta).
$$

∎

El resultado anterior establece la densidad que necesitamos en forma operativa. La siguiente definición es la que elimina el posible uso de elección cuando debamos aproximar una sucesión entera de reales de Cauchy.

### Definición 10.2.8 — Selector canónico de aproximantes racionales

Para $x\in\mathbb R_C$ y $\eta\in\mathbb Q$ definimos

$$
I(x,\eta)
:=
\left\{
n\in\mathbb N:
0<\eta
\ \land\\
\left|
x-\iota_C(e_{\mathbb Q}(n))
\right|
<_C
\iota_C(\eta)
\right\}.
$$

Si $0<\eta$, Proposición 10.2.7 — Aproximación racional de todo real de Cauchy proporciona algún racional suficientemente próximo a $x$, y Proposición 10.2.6 — La enumeración racional es sobreyectiva garantiza que ese racional aparece como $e_{\mathbb Q}(n)$ para algún $n$. Por tanto,

$$
I(x,\eta)\neq\varnothing.
$$

El principio de buen orden Teorema 1.6.13 — Principio de buen orden proporciona entonces un único mínimo

$$
\mu(x,\eta):=\min I(x,\eta).
$$

Definimos la función

$$
A_C:
\mathbb R_C\times\mathbb Q
\longrightarrow
\mathbb Q
$$

por

$$
\boxed{
A_C(x,\eta)
=
\begin{cases}
e_{\mathbb Q}(\mu(x,\eta)),
&
\text{si }0<\eta,
\\[1mm]
0_{\mathbb Q},
&
\text{si }\eta\le0.
\end{cases}
}
$$

La segunda rama sólo hace total la función. En todas las aplicaciones analíticas posteriores la tolerancia será positiva.

La importancia fundacional de esta definición es que $A_C(x,\eta)$ no es «un racional escogido» entre muchos: es el racional determinado por el menor índice natural que satisface la condición de aproximación.

> **Advertencia fundacional.** La unicidad del mínimo elimina cualquier uso de Choice, pero el predicado $n\in I(x,\eta)$ no es decidible para un real de Cauchy extensional arbitrario. Por tanto,
> $$
> \boxed{
> \text{selector canónico}
> \neq
> \text{selector computable en general}.
> }
> $$
> $A_C$ resuelve el problema de selección simultánea en ZF clásico; no convierte una clase de Cauchy arbitraria en un objeto algorítmico.

### Proposición 10.2.9 — Corrección y selección simultánea sin Choice

Se cumplen las siguientes propiedades.

1. Si $x\in\mathbb R_C$ y $\eta\in\mathbb Q$ con $0<\eta$, entonces

   $$
   \boxed{
   \left|
   x-\iota_C(A_C(x,\eta))
   \right|
   <_C
   \iota_C(\eta).
   }
   $$

2. Si

   $$
   x:\mathbb N\to\mathbb R_C
   $$

   y

   $$
   \eta:\mathbb N\to\mathbb Q
   $$

   satisfacen

   $$
   0<\eta_n
   \qquad
   \text{para todo }n\in\mathbb N,
   $$

   entonces la fórmula

   $$
   \boxed{
   q_n:=A_C(x_n,\eta_n)
   }
   $$

   determina una función

   $$
   q:\mathbb N\to\mathbb Q
   $$

   y, para todo $n$,

   $$
   \left|
   x_n-\iota_C(q_n)
   \right|
   <_C
   \iota_C(\eta_n).
   $$

**Demostración.**

Sea primero $0<\eta$. Por definición,

$$
\mu(x,\eta)\in I(x,\eta).
$$

Por la propia condición que define $I(x,\eta)$,

$$
\left|
x-\iota_C(e_{\mathbb Q}(\mu(x,\eta)))
\right|
<_C
\iota_C(\eta).
$$

Como

$$
A_C(x,\eta)
=
e_{\mathbb Q}(\mu(x,\eta)),
$$

queda probada $1$.

Para $2$, $A_C$ es una función ya definida sobre todo

$$
\mathbb R_C\times\mathbb Q.
$$

Por tanto, para cada $n$ existe un único valor

$$
A_C(x_n,\eta_n)\in\mathbb Q.
$$

Por separación en $\mathbb N\times\mathbb Q$, la condición $r=A_C(x_n,\eta_n)$ determina directamente el grafo de una función

$$
q:\mathbb N\to\mathbb Q.
$$

No hay que escoger uno de varios posibles valores en cada índice: el valor ya es único por definición de $A_C$.

Como $0<\eta_n$ para todo $n$, la parte $1$, aplicada índice por índice, da

$$
\left|
x_n-\iota_C(q_n)
\right|
<_C
\iota_C(\eta_n).
$$

∎
