## 13.8. Sucesiones de Cauchy y criterio de Cauchy {#sec-ta-13-8}

La convergencia compara una sucesión con un real fijo que ya conocemos. La condición de Cauchy elimina esa referencia externa: pregunta únicamente si los términos suficientemente tardíos están arbitrariamente próximos **entre sí**.

Esta idea ya apareció en el Capítulo 8, pero allí cumplía una función distinta. En $\mathbb Q$ demostramos que toda sucesión racional convergente es de Cauchy y construimos después una sucesión racional de Cauchy sin límite racional. La condición detectaba una estabilización interna que el sistema racional no siempre podía realizar como un punto de $\mathbb Q$.

Ahora trabajamos en $\mathbb R$. La definición tendrá la misma forma lógica, pero la completitud cambia radicalmente su fuerza. El objetivo de esta sección es demostrar

$$
\boxed{
(a_n)\text{ converge en }\mathbb R
\iff
(a_n)\text{ es de Cauchy}.
}
$$

La dirección de izquierda a derecha utilizará sólo la desigualdad triangular. La recíproca será el segundo mecanismo fundamental del capítulo en el que la completitud produce existencia de un límite.

### Definición 13.8.1 — Sucesión real de Cauchy

Sea $a=(a_n)$ una sucesión real. Diremos que $a$ es una **sucesión de Cauchy** si para todo $\varepsilon>0$ existe $N\in\mathbb N$ tal que, para cualesquiera $m,n\in\mathbb N$,

$$
N\le m
\quad\text{y}\quad
N\le n
$$

implican

$$
\boxed{
|a_m-a_n|<\varepsilon.
}
$$

Equivalentemente,

$$
\boxed{
\forall\varepsilon\in\mathbb R,
\quad
0<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall m,n\in\mathbb N,
\quad
(N\le m\wedge N\le n)
\Longrightarrow
|a_m-a_n|<\varepsilon.
}
$$

La definición no menciona ningún candidato a límite. Toda la información es **interna a la sucesión**.

> **Lectura lógica.** En la convergencia, el patrón es
> $$
> |a_n-\ell|<\varepsilon.
> $$
> En la condición de Cauchy, el punto fijo $\ell$ desaparece y se reemplaza por un segundo término tardío:
> $$
> |a_m-a_n|<\varepsilon.
> $$
> La pregunta ya no es «¿cerca de qué punto están los términos?», sino «¿se vuelven mutuamente tan próximos como queramos?».

> **Nota fundacional.** La definición afirma la existencia de un umbral $N$ para cada precisión positiva. No proporciona por sí sola una función $\varepsilon\mapsto N$, y mucho menos un procedimiento computable para producirla. Como en el Capítulo 8, un **módulo de Cauchy** sería información adicional y no forma parte de la definición extensional.

---

### Teorema 13.8.2 — Toda sucesión real convergente es de Cauchy

Sea $a=(a_n)$ una sucesión real y sea $\ell\in\mathbb R$. Si

$$
a_n\longrightarrow\ell,
$$

entonces $a$ es de Cauchy.

**Demostración.**

Sea $\varepsilon>0$. Pondremos

$$
s:=1+1.
$$

Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (3) se tiene $0<1$; sumando $1$ obtenemos

$$
1<s,
$$

y por tanto $0<s$. En particular $s^{-1}>0$ por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (6).

Definamos

$$
\eta:=\varepsilon s^{-1}.
$$

Entonces $\eta>0$ y

$$
\eta+\eta
=
\varepsilon s^{-1}+\varepsilon s^{-1}
=
\varepsilon(1+1)s^{-1}
=
\varepsilon ss^{-1}
=
\varepsilon.
$$

Como $a_n\to\ell$, existe $N\in\mathbb N$ tal que

$$
N\le k
\Longrightarrow
|a_k-\ell|<\eta.
$$

Sean ahora $m,n\ge N$. La desigualdad triangular da

$$
|a_m-a_n|
=
|(a_m-\ell)+(\ell-a_n)|
\le
|a_m-\ell|+|\ell-a_n|.
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto (3),

$$
|\ell-a_n|=|a_n-\ell|.
$$

Por tanto

$$
|a_m-a_n|
<
\eta+\eta
=
\varepsilon.
$$

Hemos encontrado un mismo umbral $N$ que sirve simultáneamente para todos los pares $m,n\ge N$. Por Definición 13.8.1 — Sucesión real de Cauchy, $a$ es de Cauchy. ∎

> **Arquitectura de la prueba.** La convergencia coloca todos los términos tardíos en una misma ventana de radio $\eta$, con $\eta+\eta=\varepsilon$, alrededor de $\ell$; la desigualdad triangular convierte esa ventana común en proximidad mutua menor que $\varepsilon$.

> **Auditoría fundacional.** No intervienen completitud, Choice ni lógica clásica sustantiva. Para la precisión fija $\eta$ se utiliza un único testigo de convergencia. Si se dispusiera además de un módulo efectivo de convergencia, esta misma prueba produciría un módulo de Cauchy mediante la transformación $\varepsilon\mapsto\varepsilon(1+1)^{-1}$.

---

### Teorema 13.8.3 — Toda sucesión real de Cauchy es acotada

Toda sucesión real de Cauchy es acotada.

**Demostración.**

Sea $a=(a_n)$ de Cauchy. Como $0<1$, aplicamos la definición con

$$
\varepsilon:=1.
$$

Existe $N\in\mathbb N$ tal que, si $m,n\ge N$, entonces

$$
|a_m-a_n|<1.
$$

Fijando $m=N$, obtenemos para todo $n\ge N$

$$
|a_n-a_N|<1.
$$

Por la desigualdad triangular,

$$
|a_n|
=
|(a_n-a_N)+a_N|
\le
|a_n-a_N|+|a_N|
<
1+|a_N|.
$$

En particular,

$$
|a_n|\le 1+|a_N|
$$

eventualmente. Además,

$$
0\le 1+|a_N|.
$$

La proposición Proposición 13.4.4 — Una cota eventual se extiende a una cota global extiende toda cota eventual de los valores absolutos a una cota global. Por tanto $a$ es acotada. ∎

> **Economía deductiva.** En el Capítulo 8 fue necesario controlar por separado la cola racional y el prefijo finito. Aquí esa infraestructura ya está encapsulada en Proposición 13.4.4 — Una cota eventual se extiende a una cota global. La idea matemática sigue siendo la misma:
> $$
> \boxed{
> \text{Cauchy controla una cola}
> +
> \text{el prefijo finito no puede escapar}
> \Longrightarrow
> \text{acotación global}.
> }
> $$

> **Auditoría fundacional.** Se extrae un único umbral para la precisión fija $1$ y se utiliza el término determinado $a_N$ como centro de la cola. No se forma ninguna familia de elecciones. Tampoco se utiliza completitud.

---

### Definición 13.8.4 — Envolventes inferior y superior de las colas

Sea $a=(a_n)$ una sucesión real acotada y sea $N\in\mathbb N$. Definimos el **conjunto de valores de la cola desde $N$** por

$$
\boxed{
T_N(a):=a[\mathbb N_{\ge N}].
}
$$

El conjunto $T_N(a)$ está habitado, pues

$$
N\in\mathbb N_{\ge N}
$$

y por tanto

$$
a_N\in T_N(a).
$$

Como $a$ es acotada, toda cota inferior o superior global de $a[\mathbb N]$ lo es también de $T_N(a)$. La completitud de $\mathbb R$ garantiza entonces la existencia de los dos extremos

$$
\inf T_N(a),
\qquad
\sup T_N(a).
$$

Definimos

$$
\boxed{
L_N(a):=\inf T_N(a),
\qquad
U_N(a):=\sup T_N(a).
}
$$

Llamaremos a

$$
L(a):=(L_N(a))_{N\in\mathbb N}
$$

la **envolvente inferior de las colas** de $a$, y a

$$
U(a):=(U_N(a))_{N\in\mathbb N}
$$

la **envolvente superior de las colas**.

Debemos justificar que estas asignaciones son realmente sucesiones reales. Consideremos, por ejemplo,

$$
G_L
:=
\left\{
\langle N,x\rangle\in\mathbb N\times\mathbb R:
 x=\inf T_N(a)
\right\}.
$$

El conjunto existe por Separación. Para cada $N\in\mathbb N$, la existencia del ínfimo está garantizada por la completitud y su unicidad por Proposición 0.7.8 — Unicidad de supremo e ínfimo; por tanto existe un único $x\in\mathbb R$ con $\langle N,x\rangle\in G_L$. Así $G_L$ es el grafo de una función

$$
L(a):\mathbb N\longrightarrow\mathbb R.
$$

El mismo argumento produce $U(a)$.

> **Auditoría de elección.** Aunque para cada $N$ aparece un extremo de la cola, no estamos eligiendo arbitrariamente un elemento entre varios. Supremo e ínfimo, cuando existen, son únicos; los grafos anteriores quedan determinados por una propiedad funcional y se obtienen por Separación dentro de $\mathbb N\times\mathbb R$. No interviene Choice.

> **Contenido efectivo.** La existencia extensional de $L_N(a)$ y $U_N(a)$ no proporciona algoritmos para calcularlos a partir de una descripción de $a$. La construcción usa la completitud de orden de $\mathbb R$ en su sentido clásico actual.

---

### Proposición 13.8.5 — Monotonía y encajamiento de las envolventes de colas

Sea $a=(a_n)$ una sucesión real acotada. Entonces:

1. si $N\le M$, se tiene
   $$
   \boxed{
   T_M(a)\subseteq T_N(a);
   }
   $$
2. $L(a)$ es creciente;
3. $U(a)$ es decreciente;
4. para todo $N\in\mathbb N$,
   $$
   \boxed{
   L_N(a)\le a_N\le U_N(a);
   }
   $$
5. si $A$ es una cota inferior global de $a$ y $B$ una cota superior global, entonces
   $$
   \boxed{
   A\le L_N(a)\le U_N(a)\le B
   }
   $$
   para todo $N$.

En particular, $L(a)$ es creciente y acotada superiormente, mientras que $U(a)$ es decreciente y acotada inferiormente.

**Demostración.**

Supongamos $N\le M$. Por Proposición 13.2.2 — Monotonía de los segmentos finales,

$$
\mathbb N_{\ge M}
\subseteq
\mathbb N_{\ge N}.
$$

Sea $x\in T_M(a)$. Entonces existe $k\in\mathbb N_{\ge M}$ con $x=a_k$. La inclusión anterior da $k\in\mathbb N_{\ge N}$ y, por tanto, $x\in T_N(a)$. Así

$$
T_M(a)\subseteq T_N(a).
$$

Como $L_N(a)$ es cota inferior de $T_N(a)$, también lo es del subconjunto $T_M(a)$. La maximalidad de $L_M(a)=\inf T_M(a)$ entre las cotas inferiores da

$$
L_N(a)\le L_M(a).
$$

Luego $L(a)$ es creciente.

Análogamente, $U_N(a)$ es cota superior de $T_N(a)$ y, por tanto, de $T_M(a)$. La minimalidad de $U_M(a)=\sup T_M(a)$ da

$$
U_M(a)\le U_N(a),
$$

de modo que $U(a)$ es decreciente.

Además,

$$
a_N\in T_N(a),
$$

por lo que las propiedades de ínfimo y supremo implican

$$
L_N(a)\le a_N\le U_N(a).
$$

Finalmente, si $A$ y $B$ son respectivamente cotas inferior y superior globales de $a$, también lo son de cada $T_N(a)$. La maximalidad del ínfimo y la minimalidad del supremo producen

$$
A\le L_N(a),
\qquad
U_N(a)\le B.
$$

Junto con $a_N\in T_N(a)$ obtenemos

$$
A\le L_N(a)\le a_N\le U_N(a)\le B,
$$

y en particular la cadena anunciada. ∎

> **Representación.** A medida que $N$ aumenta, descartamos términos iniciales y las colas se encajan:
> $$
> T_0(a)\supseteq T_1(a)\supseteq T_2(a)\supseteq\cdots.
> $$
> Sus ínfimos sólo pueden subir y sus supremos sólo pueden bajar. Las dos envolventes forman así un corredor ordenado que contiene al término $a_N$.

---

### Lema 13.8.6 — En una sucesión de Cauchy la anchura de las envolventes tiende a cero

Sea $a=(a_n)$ una sucesión real de Cauchy. Entonces, para sus envolventes de colas,

$$
\boxed{
U_N(a)-L_N(a)\longrightarrow0.
}
$$

**Demostración.**

Por Teorema 13.8.3 — Toda sucesión real de Cauchy es acotada, $a$ es acotada, de modo que $L(a)$ y $U(a)$ están definidos.

Sea $\varepsilon>0$. Como en Teorema 13.8.2 — Toda sucesión real convergente es de Cauchy, pongamos

$$
s:=1+1,
\qquad
\eta:=\varepsilon s^{-1}.
$$

Entonces

$$
0<\eta,
\qquad
\eta+\eta=\varepsilon.
$$

En particular,

$$
\eta<\varepsilon,
$$

pues de $0<\eta$ y la invariancia estricta del orden por traslación se obtiene

$$
\eta<\eta+\eta=\varepsilon.
$$

Como $a$ es de Cauchy, existe $N_0\in\mathbb N$ tal que

$$
m,n\ge N_0
\Longrightarrow
|a_m-a_n|<\eta.
$$

Fijemos $N\ge N_0$. Sean $x,y\in T_N(a)$. Existen $m,n\ge N$ tales que

$$
x=a_m,
\qquad
y=a_n.
$$

Por transitividad del orden natural, $m,n\ge N_0$, y por tanto

$$
|x-y|<\eta.
$$

Como

$$
x-y\le|x-y|,
$$

obtenemos

$$
x-y<\eta,
$$

y, sumando $y$,

$$
x<y+\eta.
$$

Fijado $y\in T_N(a)$, esta desigualdad vale para todo $x\in T_N(a)$. Por tanto $y+\eta$ es una cota superior de $T_N(a)$, y la minimalidad del supremo da

$$
U_N(a)\le y+\eta.
$$

Equivalentemente,

$$
U_N(a)-\eta\le y.
$$

Como esto vale para todo $y\in T_N(a)$, el número $U_N(a)-\eta$ es una cota inferior de la cola. La maximalidad del ínfimo produce

$$
U_N(a)-\eta\le L_N(a).
$$

Reordenando,

$$
U_N(a)-L_N(a)\le\eta.
$$

Por Proposición 13.8.5 — Monotonía y encajamiento de las envolventes de colas,

$$
L_N(a)\le U_N(a),
$$

de modo que

$$
0\le U_N(a)-L_N(a)\le\eta<\varepsilon.
$$

Al ser no negativo,

$$
|U_N(a)-L_N(a)|=U_N(a)-L_N(a)<\varepsilon.
$$

Hemos demostrado que para todo $N\ge N_0$ la anchura de la envolvente está a distancia menor que $\varepsilon$ de $0$. Por Definición 13.3.1 — Convergencia de una sucesión real,

$$
U_N(a)-L_N(a)\to0.
$$

∎

> **Idea central.** La condición de Cauchy no sólo dice que pares concretos de términos están próximos. Obliga a que **todo el conjunto de valores de una cola** quede encerrado en un intervalo de anchura arbitrariamente pequeña. Los supremos e ínfimos de las colas convierten esa información pareada en una única magnitud:
> $$
> \boxed{
> \text{diámetro de la cola}
> \rightsquigarrow
> U_N(a)-L_N(a)\to0.
> }
> $$

---

### Teorema 13.8.7 — Toda sucesión real de Cauchy converge

Toda sucesión real de Cauchy converge a un número real.

**Demostración.**

Sea $a=(a_n)$ una sucesión real de Cauchy. Por Teorema 13.8.3 — Toda sucesión real de Cauchy es acotada, $a$ es acotada. Consideremos sus envolventes $L(a)$ y $U(a)$.

Por Proposición 13.8.5 — Monotonía y encajamiento de las envolventes de colas, la sucesión $L(a)$ es creciente y acotada superiormente. El teorema de convergencia monótona Teorema 13.7.3 — Teorema de convergencia monótona garantiza, por tanto, la existencia de un real $\ell$ tal que

$$
L_N(a)\to\ell.
$$

Del mismo modo, $U(a)$ es decreciente y acotada inferiormente, de modo que existe $u\in\mathbb R$ con

$$
U_N(a)\to u.
$$

La proposición Proposición 13.5.2 — Límite del opuesto y de una diferencia sobre diferencias de límites da

$$
U_N(a)-L_N(a)
\longrightarrow
u-\ell.
$$

Pero Lema 13.8.6 — En una sucesión de Cauchy la anchura de las envolventes tiende a cero demuestra también

$$
U_N(a)-L_N(a)
\longrightarrow
0.
$$

Por unicidad del límite real, Teorema 13.3.5 — Unicidad del límite real,

$$
u-\ell=0.
$$

Sumando $\ell$ a ambos miembros y usando las leyes de cuerpo fijadas en Convención 3.6.7 — Terminología de cuerpo,

$$
u=\ell.
$$

Denotemos por

$$
r:=\ell=u
$$

este límite común.

Para todo $N\in\mathbb N$, Proposición 13.8.5 — Monotonía y encajamiento de las envolventes de colas da

$$
L_N(a)\le a_N\le U_N(a).
$$

Además,

$$
L_N(a)\to r,
\qquad
U_N(a)\to r.
$$

El teorema del sándwich Teorema 13.6.5 — Teorema del sándwich implica entonces

$$
\boxed{
a_N\to r.
}
$$

Por tanto $a$ converge en $\mathbb R$. ∎

> **Arquitectura de la prueba.** El mecanismo completo es
> $$
> \boxed{
> \begin{aligned}
> \text{Cauchy}
> &\Longrightarrow \text{acotación}\\
> &\Longrightarrow L_N\uparrow,\;U_N\downarrow\\
> &\xrightarrow{\text{completitud}} L_N\to\ell,\;U_N\to u\\
> &\Longrightarrow U_N-L_N\to u-\ell\\
> &\overset{\text{Cauchy}}{\Longrightarrow}u-\ell=0\\
> &\Longrightarrow L_N\le a_N\le U_N\to r\\
> &\Longrightarrow a_N\to r.
> \end{aligned}
> }
> $$

> **Dónde entra la completitud.** La condición de Cauchy por sí sola sólo estrecha las colas. La completitud de $\mathbb R$ garantiza que los extremos de esas colas existen y que las dos envolventes monótonas poseen límites reales. Éste es exactamente el paso que falla en $\mathbb Q$.

> **Auditoría fundacional.** No interviene Choice. Las envolventes están determinadas de manera única; los límites de las sucesiones monótonas existen por completitud. La prueba sí hereda la lógica clásica ya declarada en la interfaz actual de ínfimo, en el teorema de convergencia monótona y en la unicidad del límite. Tampoco proporciona, a partir de una sucesión de Cauchy dada extensionalmente, un algoritmo para calcular su límite.

---

### Corolario 13.8.8 — Criterio de Cauchy en $\mathbb R$

Para toda sucesión real $a=(a_n)$,

$$
\boxed{
a\text{ converge en }\mathbb R
\iff
a\text{ es de Cauchy}.
}
$$

**Demostración.**

La implicación

$$
a\text{ converge}
\Longrightarrow
a\text{ es de Cauchy}
$$

es Teorema 13.8.2 — Toda sucesión real convergente es de Cauchy. La recíproca

$$
a\text{ es de Cauchy}
\Longrightarrow
a\text{ converge}
$$

es Teorema 13.8.7 — Toda sucesión real de Cauchy converge. ∎

El contraste con los racionales queda ahora completamente identificado:

$$
\boxed{
\begin{array}{c}
\text{en }\mathbb Q:\quad
\text{convergente}\Longrightarrow\text{Cauchy},
\quad\text{pero no recíprocamente};\\[4pt]
\text{en }\mathbb R:\quad
\text{convergente}\Longleftrightarrow\text{Cauchy}.
\end{array}
}
$$

No ha cambiado la definición de Cauchy; ha cambiado el sistema numérico en el que vive la sucesión. La completitud convierte una condición interna de coherencia asintótica en **existencia formal de un límite real**, sin que ello implique computabilidad del límite.

---

Con §13.8 disponemos ya de dos grandes mecanismos de existencia de límites:

$$
\boxed{
\begin{aligned}
\text{monotonía + acotación}
&\Longrightarrow
\text{convergencia},\\
\text{Cauchy}
&\Longrightarrow
\text{convergencia}.
\end{aligned}
}
$$

El siguiente paso será estudiar **subsucesiones**. Dejaremos de exigir que toda la cola posea un único comportamiento y aprenderemos a extraer procesos parciales conservando el orden de los índices. Esta infraestructura permitirá después formular puntos límite secuenciales y preparar el teorema de Bolzano--Weierstrass.
