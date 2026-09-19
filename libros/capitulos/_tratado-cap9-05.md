## 9.5. Suma y producto en el cociente {#sec-ta-9-5}

Las operaciones término a término ya existen sobre todo el espacio de sucesiones racionales Definición 8.1.3 — Operaciones puntuales sobre sucesiones racionales. Sin embargo, no podemos trasladarlas automáticamente al cociente. Hay dos obstáculos distintos que deben resolverse en este orden:

1. si $a,b\in\mathcal C_{\mathbb Q}$, debemos demostrar que $a+b$ y $ab$ siguen siendo sucesiones de Cauchy;
2. si sustituimos $a$ y $b$ por representantes equivalentes, debemos demostrar que las clases de $a+b$ y $ab$ no cambian.

Sólo después de resolver ambos problemas será legítimo definir suma y producto en $\mathbb R_C$.

### Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto

Sean

$$
a,b\in\mathcal C_{\mathbb Q}.
$$

Entonces

$$
\boxed{
a+b\in\mathcal C_{\mathbb Q}
}
$$

y

$$
\boxed{
ab\in\mathcal C_{\mathbb Q}.
}
$$

**Demostración.**

**Suma.** Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}
$$

y

$$
\eta:=\frac{\varepsilon}{s}.
$$

Como $\mathbb Q$ es un cuerpo ordenado, $s>0$, $\eta>0$ y

$$
\eta+\eta=\varepsilon.
$$

Como $a$ es de Cauchy, existe $N_a\in\mathbb N$ tal que para cualesquiera $m,n\in\mathbb N$,

$$
N_a\le m,
\quad
N_a\le n
\Longrightarrow
|a_n-a_m|<\eta.
$$

Como $b$ es de Cauchy, existe $N_b\in\mathbb N$ tal que

$$
N_b\le m,
\quad
N_b\le n
\Longrightarrow
|b_n-b_m|<\eta.
$$

Por totalidad del orden natural, uno de los índices $N_a,N_b$ es mayor o igual que el otro. Tomamos ese índice como $N$. Entonces

$$
N_a\le N,
\qquad
N_b\le N.
$$

Sean $m,n\in\mathbb N$ con $N\le m$ y $N\le n$. Por transitividad,

$$
|a_n-a_m|<\eta,
\qquad
|b_n-b_m|<\eta.
$$

Usando la definición término a término de la suma y la desigualdad triangular,

$$
\begin{aligned}
|(a+b)_n-(a+b)_m|
&=|(a_n+b_n)-(a_m+b_m)|\\
&=|(a_n-a_m)+(b_n-b_m)|\\
&\le |a_n-a_m|+|b_n-b_m|\\
&<\eta+\eta\\
&=\varepsilon.
\end{aligned}
$$

Por tanto $a+b$ es de Cauchy, y así

$$
a+b\in\mathcal C_{\mathbb Q}.
$$

**Producto.** Por Teorema 8.6.3 — Toda sucesión racional de Cauchy es acotada, las sucesiones $a$ y $b$ son acotadas. Existen por tanto $A,B\in\mathbb Q$ tales que

$$
0\le A,
\qquad
0\le B,
$$

y, para todo $k\in\mathbb N$,

$$
|a_k|\le A,
\qquad
|b_k|\le B.
$$

Definamos

$$
H:=A+B+1_{\mathbb Q}.
$$

Como $A,B\ge0$ y $1_{\mathbb Q}>0$,

$$
0<H
$$

y

$$
A+B<H.
$$

Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$ y pongamos

$$
\delta:=\frac{\varepsilon}{H}.
$$

Entonces $\delta>0$ y

$$
H\delta=\varepsilon.
$$

Aplicando la condición de Cauchy de $a$ y de $b$ con la precisión $\delta$, existen $N_a,N_b\in\mathbb N$ tales que, para $m,n$ suficientemente grandes,

$$
|a_n-a_m|<\delta,
\qquad
|b_n-b_m|<\delta.
$$

Como antes, por totalidad del orden natural tomamos un único $N$ mayor o igual que ambos índices. Sean $m,n\ge N$. En el cuerpo racional,

$$
a_nb_n-a_mb_m
=
a_n(b_n-b_m)+b_m(a_n-a_m).
$$

Por la desigualdad triangular y la multiplicatividad del valor absoluto,

$$
\begin{aligned}
|a_nb_n-a_mb_m|
&\le |a_n|\,|b_n-b_m|+|b_m|\,|a_n-a_m|\\
&\le A|b_n-b_m|+B|a_n-a_m|\\
&\le A\delta+B\delta\\
&=(A+B)\delta\\
&<H\delta\\
&=\varepsilon.
\end{aligned}
$$

En el tercer paso sólo usamos $A,B\ge0$; no necesitamos que sean estrictamente positivos. La estricta desigualdad final procede de

$$
A+B<H
$$

y $\delta>0$.

Así $ab$ satisface la condición de Cauchy y, por consiguiente,

$$
ab\in\mathcal C_{\mathbb Q}.
$$

Esto prueba ambas afirmaciones. ∎

> **Auditoría de elección.** Los acotantes $A$ y $B$ son dos testigos locales proporcionados por Teorema 8.6.3 — Toda sucesión racional de Cauchy es acotada para las dos sucesiones fijadas. Los índices de Cauchy se eligen únicamente para una precisión racional fija y se unifican mediante la totalidad del orden natural. No se construye ninguna función global de elección.

---

### Proposición 9.5.2 — Compatibilidad de suma y producto con $\sim_C$

Sean

$$
a,a',b,b'\in\mathcal C_{\mathbb Q}
$$

tales que

$$
a\sim_C a',
\qquad
b\sim_C b'.
$$

Entonces

$$
\boxed{
a+b\sim_C a'+b'
}
$$

y

$$
\boxed{
ab\sim_C a'b'.
}
$$

**Demostración.**

Por Definición 9.3.1 — Equivalencia de Cauchy, las hipótesis significan

$$
a-a'\in\mathcal N_{\mathbb Q},
\qquad
b-b'\in\mathcal N_{\mathbb Q}.
$$

**Compatibilidad con la suma.** Por las leyes del cuerpo racional, aplicadas término a término,

$$
(a+b)-(a'+b')
=
(a-a')+(b-b').
$$

La igualdad de sucesiones se justifica por Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones, pues ambas expresiones coinciden en cada índice. Como $\mathcal N_{\mathbb Q}$ es estable bajo suma (Proposición 9.2.3 — Estabilidad aditiva de las sucesiones nulas), obtenemos

$$
(a+b)-(a'+b')\in\mathcal N_{\mathbb Q}.
$$

Además, Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto garantiza que $a+b$ y $a'+b'$ pertenecen a $\mathcal C_{\mathbb Q}$. Por definición de $\sim_C$,

$$
a+b\sim_C a'+b'.
$$

**Compatibilidad con el producto.** En cada índice vale la identidad algebraica

$$
a_nb_n-a'_nb'_n
=
a_n(b_n-b'_n)+b'_n(a_n-a'_n).
$$

Por Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones, esto da la igualdad de sucesiones

$$
ab-a'b'
=
a(b-b')+b'(a-a').
$$

Como $a\in\mathcal C_{\mathbb Q}$ y $b-b'\in\mathcal N_{\mathbb Q}$, el corolario Corolario 9.2.5 — Producto de una sucesión de Cauchy por una sucesión nula implica

$$
a(b-b')\in\mathcal N_{\mathbb Q}.
$$

Análogamente, como $b'\in\mathcal C_{\mathbb Q}$ y $a-a'\in\mathcal N_{\mathbb Q}$,

$$
b'(a-a')\in\mathcal N_{\mathbb Q}.
$$

La estabilidad aditiva de las sucesiones nulas produce entonces

$$
ab-a'b'\in\mathcal N_{\mathbb Q}.
$$

Por Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto, tanto $ab$ como $a'b'$ pertenecen a $\mathcal C_{\mathbb Q}$. Por definición de la equivalencia de Cauchy,

$$
ab\sim_C a'b'.
$$

Quedan demostradas ambas compatibilidades. ∎

> **Interpretación.** Este resultado es el verdadero criterio de buena definición. No afirma todavía que haya suma o producto en $\mathbb R_C$; afirma que las operaciones sobre representantes son constantes sobre las clases de equivalencia pertinentes.

---

### Proposición 9.5.3 — Existencia y unicidad de las operaciones inducidas

Existen funciones únicas

$$
S_C:\mathbb R_C\times\mathbb R_C\to\mathbb R_C
$$

y

$$
P_C:\mathbb R_C\times\mathbb R_C\to\mathbb R_C
$$

tales que, para cualesquiera $a,b\in\mathcal C_{\mathbb Q}$,

$$
\boxed{
S_C\bigl(\langle[a]_C,[b]_C\rangle\bigr)
=
[a+b]_C
}
$$

y

$$
\boxed{
P_C\bigl(\langle[a]_C,[b]_C\rangle\bigr)
=
[ab]_C.
}
$$

**Demostración.**

Construiremos primero la suma. Dentro del conjunto

$$
(\mathbb R_C\times\mathbb R_C)\times\mathbb R_C
$$

definimos por separación

$$
\begin{aligned}
G_S
:=
\bigl\{
&\langle\langle x,y\rangle,z\rangle
\in
(\mathbb R_C\times\mathbb R_C)\times\mathbb R_C:\\
&\exists a,b\in\mathcal C_{\mathbb Q}\,
\bigl(
 x=[a]_C
 \land
 y=[b]_C
 \land
 z=[a+b]_C
\bigr)
\bigr\}.
\end{aligned}
$$

Sean $x,y\in\mathbb R_C$. Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existen representantes $a,b\in\mathcal C_{\mathbb Q}$ tales que

$$
x=[a]_C,
\qquad
y=[b]_C.
$$

Por Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto,

$$
a+b\in\mathcal C_{\mathbb Q},
$$

de modo que

$$
[a+b]_C\in\mathbb R_C.
$$

Así existe al menos un $z\in\mathbb R_C$ con

$$
\langle\langle x,y\rangle,z\rangle\in G_S.
$$

Veamos la unicidad. Supongamos que otros representantes $a',b'\in\mathcal C_{\mathbb Q}$ satisfacen

$$
x=[a']_C,
\qquad
y=[b']_C.
$$

Entonces

$$
[a]_C=[a']_C,
\qquad
[b]_C=[b']_C.
$$

Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy,

$$
a\sim_C a',
\qquad
b\sim_C b'.
$$

La compatibilidad demostrada en Proposición 9.5.2 — Compatibilidad de suma y producto con $\sim_C$ da

$$
a+b\sim_C a'+b'.
$$

Aplicando otra vez el criterio de igualdad de clases,

$$
[a+b]_C=[a'+b']_C.
$$

Por tanto $G_S$ es total y univaluado sobre $\mathbb R_C\times\mathbb R_C$; con codominio $\mathbb R_C$, es el grafo de una función

$$
S_C:\mathbb R_C\times\mathbb R_C\to\mathbb R_C.
$$

La unicidad de esta función se sigue del criterio de igualdad de funciones Proposición 0.6.3 — Criterio de igualdad de funciones: cualquier otra función con la misma regla sobre clases coincide con $S_C$ en cada par $\langle x,y\rangle$, porque para ese par podemos tomar representantes locales $a,b$ y ambos valores quedan forzados a ser $[a+b]_C$.

Para el producto definimos análogamente

$$
\begin{aligned}
G_P
:=
\bigl\{
&\langle\langle x,y\rangle,z\rangle
\in
(\mathbb R_C\times\mathbb R_C)\times\mathbb R_C:\\
&\exists a,b\in\mathcal C_{\mathbb Q}\,
\bigl(
 x=[a]_C
 \land
 y=[b]_C
 \land
 z=[ab]_C
\bigr)
\bigr\}.
\end{aligned}
$$

La existencia del valor para cada par $\langle x,y\rangle$ usa la clausura $ab\in\mathcal C_{\mathbb Q}$ de Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto; la independencia de los representantes usa la compatibilidad

$$
a\sim_C a',
\quad
b\sim_C b'
\Longrightarrow
ab\sim_C a'b'
$$

de Proposición 9.5.2 — Compatibilidad de suma y producto con $\sim_C$. Así $G_P$ es el grafo de una única función

$$
P_C:\mathbb R_C\times\mathbb R_C\to\mathbb R_C
$$

con la propiedad requerida. ∎

> **Auditoría de elección.** Para un par fijo $\langle x,y\rangle$ se usan representantes cuya existencia está garantizada por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy. No se selecciona simultáneamente un representante para cada clase. La unicidad del valor hace que el grafo funcional quede definido por separación sin construir una sección del cociente.

---

### Definición 9.5.4 — Suma y producto en $\mathbb R_C$

Sean $+_C$ y $\cdot_C$ las funciones únicas proporcionadas por Proposición 9.5.3 — Existencia y unicidad de las operaciones inducidas:

$$
+_C:\mathbb R_C\times\mathbb R_C\to\mathbb R_C,
\qquad
\cdot_C:\mathbb R_C\times\mathbb R_C\to\mathbb R_C.
$$

Para $x,y\in\mathbb R_C$ definimos

$$
x+_Cy
:=
+_C\bigl(\langle x,y\rangle\bigr)
$$

y

$$
x\cdot_C y
:=
\cdot_C\bigl(\langle x,y\rangle\bigr).
$$

Cuando el tipo de los operandos sea inequívoco, escribiremos simplemente

$$
x+y
\qquad\text{y}\qquad
xy.
$$

En particular, para cualesquiera $a,b\in\mathcal C_{\mathbb Q}$,

$$
\boxed{
[a]_C+[b]_C=[a+b]_C
}
$$

y

$$
\boxed{
[a]_C[b]_C=[ab]_C.
}
$$

Estas fórmulas no son reglas informales sobre representantes: son las ecuaciones que caracterizan las operaciones bien definidas en el cociente.

> **Decisión de notación.** No se consume un nuevo `TA-NOT`: los símbolos $+$ y $\cdot$ ya están activos y se sobrecargan por tipado, como en las extensiones numéricas anteriores. Los símbolos explícitos $+_C$ y $\cdot_C$ quedan disponibles cuando sea necesario distinguir la operación de Cauchy de otras operaciones.

---

### Lo que hemos ganado

El conjunto $\mathbb R_C$ ya posee dos operaciones binarias internas,

$$
+_C,\cdot_C:
\mathbb R_C\times\mathbb R_C\to\mathbb R_C,
$$

obtenidas directamente de la suma y el producto término a término de sucesiones racionales. La propiedad decisiva es que ambas operaciones son **independientes del representante**.

Todavía no hemos probado que estas operaciones satisfagan los axiomas de anillo o de cuerpo. En particular, aún debemos identificar sus elementos neutros, construir el opuesto aditivo, verificar las leyes algebraicas heredadas y, más adelante, resolver el problema sustancial de construir el inverso multiplicativo de una clase no nula.

La construcción continúa sin utilizar completitud de Dedekind, sin identificar $\mathbb Q$ con un subconjunto de $\mathbb R_C$ y sin ninguna forma de elección.

---
