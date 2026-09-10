Partimos de $b$ y usamos únicamente las propiedades exigidas:

$$
\begin{aligned}
b
&=b+0\\
&=b+(a+c)\\
&=(b+a)+c\\
&=(a+b)+c\\
&=0+c\\
&=c.
\end{aligned}
$$

Justifiquemos cada paso.

- $b=b+0$: neutro aditivo `C2`.
- $0=a+c$: una de las hipótesis, usada por sustitución.
- $b+(a+c)=(b+a)+c$: asociatividad `C1`.
- $b+a=a+b$: conmutatividad `C4`.
- $a+b=0$: la otra hipótesis.
- $0+c=c$: por conmutatividad, $0+c=c+0$, y luego `C2`.

Así,

$$
\boxed{b=c}.
$$

Los axiomas de inverso garantizan existencia de candidatos, pero la cadena anterior demuestra que dos candidatos cualesquiera necesariamente coinciden. Esa es exactamente la parte de **unicidad**.
:::
::: {#sol-t1-0046}
<!-- CPM-T1-SOL-0046 -->
**Solución B4.**

La elección más sencilla es

$$
\boxed{n=201}.
$$

Claramente $201>200$. Además, como $201>137>0$, al tomar recíprocos se invierte el orden:

$$
\frac1{201}<\frac1{137}.
$$

Por tanto satisface simultáneamente ambas exigencias.
:::

::: {#sol-t1-0047}
<!-- CPM-T1-SOL-0047 -->
**Solución B5.**

Partimos de

$$
I_0=[3,4],
$$

porque $3^2=9<10<16=4^2$.

Primer punto medio:

$$
m_1=\frac72,
\qquad
\left(\frac72\right)^2=\frac{49}{4}>10.
$$

Conservamos

$$
I_1=\left[3,\frac72\right].
$$

Segundo punto medio:

$$
m_2=\frac{13}{4},
\qquad
\left(\frac{13}{4}\right)^2=\frac{169}{16}>10
$$

porque $169>160$. Luego

$$
I_2=\left[3,\frac{13}{4}\right].
$$

Tercer punto medio:

$$
m_3=\frac{25}{8},
\qquad
\left(\frac{25}{8}\right)^2=\frac{625}{64}<10
$$

porque $625<640$. Por tanto,

$$
I_3=\left[\frac{25}{8},\frac{13}{4}\right].
$$

Así,

$$
\boxed{\frac{25}{8}<\sqrt{10}<\frac{13}{4}.}
$$
:::

::: {#sol-t1-0048}
<!-- CPM-T1-SOL-0048 -->
**Solución B6.**

Queremos demostrar que $(-a)b$ es el inverso aditivo de $ab$. Calculamos:

$$
\begin{aligned}
ab+(-a)b
&=ba+b(-a)\\
&=b\bigl(a+(-a)\bigr)\\
&=b0\\
&=0.
\end{aligned}
$$

En la primera línea usamos conmutatividad del producto para escribir ambos términos con el factor común $b$. En la segunda usamos distributividad en sentido inverso. Después,

$$
a+(-a)=0
$$

por el axioma de inverso aditivo, y finalmente $b0=0$ por el resultado ya demostrado @exm-t1-0040.

Por tanto $(-a)b$ satisface la propiedad que caracteriza al inverso aditivo de $ab$. Como ese inverso es único por @prp-t1-0025,

$$
\boxed{(-a)b=-(ab)}.
$$

La regla escolar de signos aparece así como una consecuencia de distributividad, inversos y unicidad; no como un axioma independiente.
:::
::: {#sol-t1-0049}
<!-- CPM-T1-SOL-0049 -->
**Solución B7.**

Queremos resolver

$$
\left|\frac{x-1}{x+2}\right|
\le
\frac{|x-3|}{2}.
$$

**1. Dominio y puntos críticos.** El denominador exige

$$
x\ne-2.
$$

Los argumentos de los valores absolutos se anulan en $x=1$ y $x=3$. Estos puntos, junto con el polo $-2$, deben registrarse aunque una transformación posterior produzca fronteras adicionales.

**2. Eliminación segura de denominadores y valores absolutos.** Para $x\ne-2$, $2|x+2|>0$. Multiplicamos sin cambiar el sentido:

$$
2|x-1|\le |x-3|\,|x+2|.
$$

Ambos lados son no negativos, así que elevar al cuadrado es una equivalencia:

$$
4(x-1)^2\le (x-3)^2(x+2)^2.
$$

Llevando todo a un lado y factorizando,

$$
(x-3)^2(x+2)^2-4(x-1)^2
=(x-4)(x+1)(x^2+x-8).
$$

Las raíces del factor cuadrático son

$$
r_- =\frac{-1-\sqrt{33}}2,
\qquad
r_+ =\frac{-1+\sqrt{33}}2.
$$

El orden relevante es

$$
r_-<-2<-1<r_+<3<4.
$$

**3. Análisis de signos.** Debemos resolver

$$
(x-4)(x+1)(x-r_-)(x-r_+)\ge0.
$$

Todos los ceros son simples, por lo que el signo alterna al atravesarlos. Como el polinomio es positivo para $x$ grande y positivo, resulta no negativo en

$$
(-\infty,r_-]\cup[-1,r_+]\cup[4,\infty).
$$

El punto excluido $x=-2$ se encuentra en una región que ya no pertenece a la solución, pero debe mantenerse fuera del dominio en todo momento.

**4. Extremos.** En $r_-$, $-1$, $r_+$ y $4$ se obtiene igualdad, y ninguno es un polo; por eso se incluyen.

Por consiguiente,

$$
\boxed{
(-\infty,\tfrac{-1-\sqrt{33}}2]
\cup
[-1,\tfrac{-1+\sqrt{33}}2]
\cup
[4,\infty)
}.
$$

La comprobación final respeta el dominio original y todos los extremos proceden de equivalencias algebraicas reversibles.
:::

#### Soluciones del nivel C

::: {#sol-t1-0050}
<!-- CPM-T1-SOL-0050 -->
**Solución C1.**

Sea

$$
s=\sup A.
$$

Como $a\le s$ para todo $a\in A$ y $c>0$,

$$
ca\le cs.
$$

Así, $cs$ es cota superior de $cA$.

Para demostrar que es la menor, sea $\varepsilon>0$. Como $s=\sup A$, existe $a\in A$ tal que

$$
s-\frac{\varepsilon}{c}<a\le s.
$$

Multiplicando por $c>0$,

$$
cs-\varepsilon<ca\le cs.
$$

Por la caracterización aproximativa del supremo,

$$
\boxed{\sup(cA)=c\sup A.}
$$
:::

::: {#sol-t1-0051}
<!-- CPM-T1-SOL-0051 -->
**Solución C2.**

Sea

$$
t=\sup(-A).
$$

Para todo $a\in A$, el número $-a$ pertenece a $-A$, luego

$$
-a\le t.
$$

Multiplicando por $-1$,

$$
a\ge -t.
$$

Así, $-t$ es cota inferior de $A$.

Si $\ell$ es cualquier cota inferior de $A$, entonces

$$
\ell\le a
$$

para todo $a\in A$, por lo que

$$
-a\le-\ell
$$

para todo $-a\in-A$. Así, $-\ell$ es cota superior de $-A$. Como $t$ es la menor de ellas,

$$
t\le-\ell,
$$

y, al multiplicar por $-1$,

$$
-t\ge\ell.
$$

Por tanto, $-t$ es la mayor cota inferior de $A$:

$$
\boxed{\inf A=-\sup(-A).}
$$
:::

::: {#sol-t1-0052}
<!-- CPM-T1-SOL-0052 -->
**Solución C3.**

Como $a<b$, la densidad de los racionales permite escoger primero

$$
q\in\mathbb Q
\quad\text{con}\quad
a<q<b.
$$

Ahora $q<b$. Aplicamos la densidad de los irracionales al intervalo $(q,b)$ y obtenemos

$$
\xi\in\mathbb R\setminus\mathbb Q
\quad\text{con}\quad
q<\xi<b.
$$

Juntando las desigualdades,

$$
\boxed{a<q<\xi<b.}
$$

La elección en dos etapas es importante: no basta producir independientemente un racional y un irracional dentro de $(a,b)$ si además queremos controlar su orden relativo.
:::

::: {#sol-t1-0053}
<!-- CPM-T1-SOL-0053 -->
**Solución C4.**

Debemos separar existencia de unicidad.

**1. Existencia.** Definimos

$$
x_0=b+(-a).
$$

Entonces

$$
\begin{aligned}
a+x_0
&=a+\bigl(b+(-a)\bigr)\\
&=\bigl(a+(-a)\bigr)+b\\
&=0+b\\
&=b.
\end{aligned}
$$

