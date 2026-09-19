## 9.7. Inversos multiplicativos {#sec-ta-9-7}

La estructura obtenida en §9.6 es ya un anillo conmutativo no trivial con identidad. Para convertirla en un cuerpo falta demostrar que todo elemento distinto de $0_C$ posee inverso multiplicativo.

Aquí aparece una dificultad que no existía para la suma, el producto ni el opuesto. Si $x=[a]_C\neq0_C$, no podemos definir ingenuamente el inverso término a término mediante $(a_n^{-1})$: un representante no nulo puede contener términos iguales a $0_{\mathbb Q}$ en posiciones iniciales. Lo que sí debe suceder —y primero debemos probarlo— es que una sucesión de Cauchy que no sea nula quede, a partir de cierto índice, uniformemente separada de cero.

La estrategia será, por tanto,

$$
[a]_C\neq0_C
\Longrightarrow
a\notin\mathcal N_{\mathbb Q}
\Longrightarrow
|a_n|>\delta\text{ eventualmente}
\Longrightarrow
\text{recíproco eventual de }a
\Longrightarrow
\text{inverso de }[a]_C.
$$

No elegiremos simultáneamente representantes para todas las clases. El representante se utilizará sólo como testigo local dentro de una prueba de existencia; la función inversa sobre el cociente se construirá después mediante un grafo definido por la ecuación $xy=1_C$.

---

### Proposición 9.7.1 — Criterio de nulidad de una clase de Cauchy

Para todo $a\in\mathcal C_{\mathbb Q}$,

$$
\boxed{
[a]_C=0_C
\iff
a\in\mathcal N_{\mathbb Q}.
}
$$

En particular,

$$
\boxed{
[a]_C\neq0_C
\iff
a\notin\mathcal N_{\mathbb Q}.
}
$$

**Demostración.**

Por Definición 9.6.1 — Cero y unidad de Cauchy,

$$
0_C=[\underline{0_{\mathbb Q}}]_C.
$$

El criterio de igualdad de clases Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy da

$$
[a]_C=0_C
\iff
a-\underline{0_{\mathbb Q}}\in\mathcal N_{\mathbb Q}.
$$

Para todo $n\in\mathbb N$, las operaciones puntuales y las leyes del grupo aditivo racional producen

$$
\bigl(a-\underline{0_{\mathbb Q}}\bigr)_n
=a_n-0_{\mathbb Q}
=a_n.
$$

Por el criterio término a término Proposición 8.1.2 — Criterio término a término para la igualdad de sucesiones,

$$
a-\underline{0_{\mathbb Q}}=a.
$$

Por consiguiente,

$$
[a]_C=0_C
\iff
a\in\mathcal N_{\mathbb Q}.
$$

Negando ambos miembros obtenemos la segunda equivalencia. ∎

---

### Lema 9.7.2 — Separación eventual respecto de cero

Sea

$$
a=(a_n)_{n\in\mathbb N}\in\mathcal C_{\mathbb Q}.
$$

Si

$$
a\notin\mathcal N_{\mathbb Q},
$$

entonces existen $\delta\in\mathbb Q$ y $N_0\in\mathbb N$ tales que

$$
\boxed{
0<\delta
\qquad\text{y}\qquad
N_0\le n\Longrightarrow \delta<|a_n|.
}
$$

**Demostración.**

La condición $a\notin\mathcal N_{\mathbb Q}$ es la negación de

$$
\forall\varepsilon\in\mathbb Q\;
\Bigl(
0<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\in\mathbb N\;
\bigl(N\le n\Longrightarrow |a_n|<\varepsilon\bigr)
\Bigr).
$$

Negando sucesivamente los cuantificadores mediante lógica clásica y usando que, en el orden total racional, la negación de $x<y$ equivale a $y\le x$, existe por tanto $\varepsilon_0\in\mathbb Q$ con $0<\varepsilon_0$ tal que

$$
\forall N\in\mathbb N\;
\exists k\in\mathbb N\;
\bigl(
N\le k
\land
|a_k|\ge\varepsilon_0
\bigr).
$$

Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}
$$

y

$$
\delta:=\frac{\varepsilon_0}{s}.
$$

Por las leyes del cuerpo ordenado racional, $s>0$, $\delta>0$ y

$$
\delta+\delta=\varepsilon_0.
$$

Como $a$ es de Cauchy, la formulación de Proposición 8.4.3 — Formulaciones equivalentes de la condición de Cauchy aplicada a la precisión $\delta$ proporciona $N_0\in\mathbb N$ tal que

$$
N_0\le m,
\quad
N_0\le n
\Longrightarrow
|a_m-a_n|<\delta.
$$

Aplicando ahora la propiedad obtenida de la no nulidad con $N=N_0$, existe $k\in\mathbb N$ tal que

$$
N_0\le k
\qquad\text{y}\qquad
|a_k|\ge\varepsilon_0.
$$

Sea $n\in\mathbb N$ con $N_0\le n$. Como también $N_0\le k$,

$$
|a_k-a_n|<\delta.
$$

La desigualdad triangular aplicada a

$$
a_k=(a_k-a_n)+a_n
$$

da

$$
|a_k|
\le
|a_k-a_n|+|a_n|
<
\delta+|a_n|.
$$

Por otra parte,

$$
\delta+\delta
=
\varepsilon_0
\le
|a_k|.
$$

Por transitividad,

$$
\delta+\delta
<
\delta+|a_n|.
$$

La invariancia estricta del orden bajo traslación (Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado) permite cancelar el primer $\delta$ y concluir

$$
\delta<|a_n|.
$$

Como $n\ge N_0$ era arbitrario, queda demostrada la separación eventual. ∎

> **Auditoría de elección.** La negación de la nulidad produce un único testigo $\varepsilon_0$ para la sucesión fija $a$. Después se toma un único índice $k$ correspondiente al índice fijo $N_0$. No se construye ninguna función $N\mapsto k_N$ ni se seleccionan testigos simultáneamente.
>
> **Frontera clásica.** El paso desde la información negativa
> $$ a\notin\mathcal N_{\mathbb Q} $$
> hasta un margen positivo eventual $\delta<|a_n|$ usa negación clásica de cuantificadores. En una
> futura interfaz constructiva, ese margen debe tratarse como **apartness positiva** dada explícitamente.

---

### Definición 9.7.3 — Recíproco seguro de una sucesión racional

Definimos la función

$$
\boxed{
\rho_0:\mathbb Q^{\mathbb N}\longrightarrow\mathbb Q^{\mathbb N}
}
$$

por la regla término a término

$$
\boxed{
(\rho_0(a))_n
:=
\begin{cases}
a_n^{-1},&a_n\neq0_{\mathbb Q},\\[2mm]
0_{\mathbb Q},&a_n=0_{\mathbb Q}.
\end{cases}
}
$$

La denominaremos **función de recíproco seguro**. Su finalidad es evitar que los posibles ceros iniciales de una sucesión impidan definir una sucesión racional completa.

Conjuntistamente, para cada $a\in\mathbb Q^{\mathbb N}$ el grafo correspondiente se obtiene por separación dentro de $\mathbb N\times\mathbb Q$:

$$
\left\{
\langle n,r\rangle\in\mathbb N\times\mathbb Q:
\bigl(a_n\neq0_{\mathbb Q}\land r=a_n^{-1}\bigr)
\lor
\bigl(a_n=0_{\mathbb Q}\land r=0_{\mathbb Q}\bigr)
\right\}.
$$

Para cada $n$ exactamente uno de los dos casos se cumple y determina un único $r\in\mathbb Q$. Por tanto el conjunto anterior es el grafo de una única sucesión racional. El criterio término a término garantiza unicidad, y separando dentro de

$$
\mathbb Q^{\mathbb N}\times\mathbb Q^{\mathbb N}
$$

obtenemos el grafo de la función global $\rho_0$.

No se ha elegido ningún valor arbitrario: tanto en el caso $a_n\neq0$ como en el caso $a_n=0$ la salida está determinada de manera canónica.

> **Contenido efectivo.** Esta definición por casos sí es efectiva sobre nombres racionales, porque la
> igualdad $a_n=0_{\mathbb Q}$ es decidible para cada término racional. Aquí “canónico” y
> “computable” coinciden por una razón adicional explícita: la decidibilidad racional.

---

### Lema 9.7.4 — El recíproco seguro de un representante no nulo es de Cauchy

Sea

$$
a\in\mathcal C_{\mathbb Q}
\setminus
\mathcal N_{\mathbb Q}
$$

y pongamos

$$
b:=\rho_0(a).
$$

Entonces:

1. $b\in\mathcal C_{\mathbb Q}$;
2. $ab\sim_C\underline{1_{\mathbb Q}}$.

En particular, la clase $[b]_C$ es un candidato legítimo al inverso de $[a]_C$.

**Demostración.**

Por Lema 9.7.2 — Separación eventual respecto de cero, existen $\delta\in\mathbb Q$ y $N_0\in\mathbb N$ tales que

$$
0<\delta
$$

y

$$
N_0\le n
\Longrightarrow
\delta<|a_n|.
$$

Por tanto, para todo $n\ge N_0$,

$$
a_n\neq0_{\mathbb Q}
$$

y, por definición de $\rho_0$,

$$
b_n=a_n^{-1}.
$$

**(1) La sucesión $b$ es de Cauchy.** Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Definamos

$$
\eta:=\varepsilon\delta\delta.
$$

Como $\varepsilon>0$ y $\delta>0$, las reglas de signos del cuerpo ordenado racional dan

$$
0<\eta.
$$

La condición de Cauchy para $a$ proporciona $N_1\in\mathbb N$ tal que

$$
N_1\le m,
\quad
N_1\le n
\Longrightarrow
|a_n-a_m|<\eta.
$$

Combinamos $N_0$ y $N_1$ sin introducir una operación de máximo. Por la totalidad del orden natural (Teorema 1.6.5 — Orden total), o bien $N_0\le N_1$ o bien $N_1\le N_0$. Tomamos como $N$ el mayor de los dos en el caso correspondiente. Entonces

$$
N_0\le N,
\qquad
N_1\le N.
$$

Sean $m,n\ge N$. Tenemos

$$
b_n=a_n^{-1},
\qquad
b_m=a_m^{-1}.
$$

En el cuerpo racional,

$$
a_n^{-1}-a_m^{-1}
=
(a_m-a_n)a_n^{-1}a_m^{-1}.
$$

Además, por multiplicatividad del valor absoluto,

$$
|a_n|\,|a_n^{-1}|
=
|a_na_n^{-1}|
=
|1_{\mathbb Q}|
=
1_{\mathbb Q}.
$$

Como $|a_n|>0$, podemos multiplicar la igualdad anterior por $|a_n|^{-1}$. Las leyes del cuerpo racional dan entonces

$$
|a_n^{-1}|=|a_n|^{-1}.
$$

La desigualdad

$$
0<\delta<|a_n|
$$

y la inversión del orden positivo (Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado) implican

$$
0<|a_n^{-1}|<\delta^{-1}.
$$

Del mismo modo,

$$
0<|a_m^{-1}|<\delta^{-1}.
$$

Por compatibilidad estricta del orden con el producto de factores positivos,

$$
0<|a_n^{-1}|\,|a_m^{-1}|
<
\delta^{-1}\delta^{-1}.
$$

Como además

$$
0\le |a_m-a_n|<\eta,
$$

obtenemos sucesivamente

$$
|a_m-a_n|\,|a_n^{-1}|\,|a_m^{-1}|
<
\eta\,|a_n^{-1}|\,|a_m^{-1}|
<
\eta\,\delta^{-1}\delta^{-1}.
$$

Por consiguiente,

$$
\begin{aligned}
|b_n-b_m|
&=|a_n^{-1}-a_m^{-1}|\\
&=|a_m-a_n|\,|a_n^{-1}|\,|a_m^{-1}|\\
&<\eta\,\delta^{-1}\delta^{-1}\\
&=(\varepsilon\delta\delta)\delta^{-1}\delta^{-1}\\
&=\varepsilon.
\end{aligned}
$$

Hemos demostrado la condición de Cauchy para $b$, luego

$$
b\in\mathcal C_{\mathbb Q}.
$$

**(2) El producto $ab$ es equivalente a la unidad constante.** Como $a,b\in\mathcal C_{\mathbb Q}$, Proposición 9.5.1 — Estabilidad de $\mathcal C_{\mathbb Q}$ bajo suma y producto da

$$
ab\in\mathcal C_{\mathbb Q}.
$$

Para todo $n\ge N_0$,

$$
(ab)_n
=a_nb_n
=a_na_n^{-1}
=1_{\mathbb Q}.
$$

Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Para todo $n\ge N_0$,

$$
\left|
(ab)_n-\underline{1_{\mathbb Q}}{}_n
\right|
=
|1_{\mathbb Q}-1_{\mathbb Q}|
=0_{\mathbb Q}
<
\varepsilon.
$$

Por tanto

$$
ab-\underline{1_{\mathbb Q}}
\in
\mathcal N_{\mathbb Q}.
$$

Como $\underline{1_{\mathbb Q}}\in\mathcal C_{\mathbb Q}$, la definición de $\sim_C$ produce

$$
\boxed{
ab\sim_C\underline{1_{\mathbb Q}}.
}
$$

∎

> **Nota estructural.** Los valores de $\rho_0(a)$ antes de $N_0$ son irrelevantes para la clase asintótica. La modificación queda confinada al segmento inicial $n<N_0$, porque la separación eventual garantiza que, desde $N_0$ en adelante, ningún término de $a$ vuelve a ser cero.

---

### Definición 9.7.5 — Reales de Cauchy no nulos

Definimos

$$
\boxed{
\mathbb R_{C,\neq0}
:=
\{x\in\mathbb R_C:x\neq0_C\}.
}
$$

Este conjunto existe por separación dentro de $\mathbb R_C$.

---

### Proposición 9.7.6 — Existencia local de inversos multiplicativos

Para todo

$$
x\in\mathbb R_{C,\neq0},
$$

existe

$$
y\in\mathbb R_{C,\neq0}
$$

tal que

$$
\boxed{
xy=1_C=yx.
}
$$

**Demostración.**

Sea $x\in\mathbb R_{C,\neq0}$. Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, para este $x$ fijo existe $a\in\mathcal C_{\mathbb Q}$ tal que

$$
x=[a]_C.
$$

Como $x\neq0_C$, Proposición 9.7.1 — Criterio de nulidad de una clase de Cauchy implica

$$
a\notin\mathcal N_{\mathbb Q}.
$$

Pongamos

$$
b:=\rho_0(a).
$$

El lema Lema 9.7.4 — El recíproco seguro de un representante no nulo es de Cauchy da

$$
b\in\mathcal C_{\mathbb Q}
$$

y

$$
ab\sim_C\underline{1_{\mathbb Q}}.
$$

Definamos, dentro de esta prueba,

$$
y:=[b]_C.
$$

Entonces

$$
\begin{aligned}
xy
&=[a]_C[b]_C\\
&=[ab]_C\\
&=[\underline{1_{\mathbb Q}}]_C\\
&=1_C.
\end{aligned}
$$

Debemos verificar que $y\neq0_C$. Si $y=0_C$, la ley absorbente de Proposición 9.6.2 — Leyes del cero y de la unidad daría

$$
xy=x0_C=0_C,
$$

mientras que acabamos de probar $xy=1_C$. Esto contradice Proposición 9.6.7 — Distinción entre cero y unidad. Por tanto

$$
y\in\mathbb R_{C,\neq0}.
$$

Finalmente, la conmutatividad del producto en $\mathbb R_C$ da

$$
yx=xy=1_C.
$$

∎

> **Auditoría de elección.** La prueba usa un representante $a$ únicamente para el elemento fijo $x$. No se define una familia de representantes de todas las clases. La existencia de la futura función inversa se obtendrá por unicidad algebraica, no por una elección global de representantes.

---

### Proposición 9.7.7 — Construcción de la función inversa en $\mathbb R_C$

Existe una única función

$$
\boxed{
\operatorname{inv}_C:
\mathbb R_{C,\neq0}
\longrightarrow
\mathbb R_{C,\neq0}
}
$$

tal que, para todo $x\in\mathbb R_{C,\neq0}$,

$$
x\operatorname{inv}_C(x)=1_C.
$$

**Demostración.**

Consideremos

$$
G_C
:=
\left\{
\langle x,y\rangle
\in
\mathbb R_{C,\neq0}\times\mathbb R_{C,\neq0}:
xy=1_C
\right\}.
$$

El producto cartesiano existe y $G_C$ existe por separación.

Por Proposición 9.7.6 — Existencia local de inversos multiplicativos, para cada $x\in\mathbb R_{C,\neq0}$ existe al menos un $y\in\mathbb R_{C,\neq0}$ con $xy=1_C$.

Probemos unicidad. Supongamos

$$
xy=1_C
\qquad\text{y}\qquad
xz=1_C.
$$

Usando las leyes del anillo conmutativo Teorema 9.6.6 — $\mathbb R_C$ es un anillo conmutativo con identidad,

$$
\begin{aligned}
y
&=y1_C\\
&=y(xz)\\
&=(yx)z\\
&=(xy)z\\
&=1_Cz\\
&=z.
\end{aligned}
$$

Así, para cada $x$ existe exactamente un $y$ relacionado con él por $G_C$. Por la definición de función, $G_C$ es el grafo de una única función

$$
\operatorname{inv}_C:
\mathbb R_{C,\neq0}\to\mathbb R_{C,\neq0}.
$$

No se ha elegido ningún representante ni ningún inverso entre varias posibilidades: el valor queda determinado de manera única por la ecuación $xy=1_C$. ∎

---

### Notación 9.7.8 — Recíproco de un real de Cauchy

Para $x\in\mathbb R_{C,\neq0}$ escribiremos

$$
\boxed{
x^{-1}:=\operatorname{inv}_C(x).
}
$$

El símbolo $x^{-1}$ está sobrecargado por tipo: para racionales designa el recíproco definido en Notación 3.6.4 — Recíproco; para reales de Cauchy designa la función anterior. No debe confundirse con $f^{-1}$, que para funciones denota la función inversa de una biyección.

---

### Proposición 9.7.9 — Ley del inverso multiplicativo en $\mathbb R_C$

Para todo $x\in\mathbb R_{C,\neq0}$,

$$
\boxed{
xx^{-1}=1_C=x^{-1}x.
}
$$

**Demostración.**

La primera igualdad es la propiedad definitoria de $\operatorname{inv}_C$ en Proposición 9.7.7 — Construcción de la función inversa en $\mathbb R_C$:

$$
xx^{-1}=1_C.
$$

La segunda se sigue de la conmutatividad del producto establecida en Teorema 9.6.6 — $\mathbb R_C$ es un anillo conmutativo con identidad. ∎

---

### Teorema 9.7.10 — $\mathbb R_C$ es un cuerpo

Con las operaciones ya construidas,

$$
\boxed{
(\mathbb R_C,+_C,\cdot_C,0_C,1_C)
\text{ es un cuerpo.}
}
$$

**Demostración.**

El teorema Teorema 9.6.6 — $\mathbb R_C$ es un anillo conmutativo con identidad demuestra que

$$
(\mathbb R_C,+_C,\cdot_C,0_C,1_C)
$$

es un anillo conmutativo con identidad. La proposición Proposición 9.6.7 — Distinción entre cero y unidad establece

$$
0_C\neq1_C.
$$

Finalmente, si $x\neq0_C$, entonces $x\in\mathbb R_{C,\neq0}$ y Proposición 9.7.9 — Ley del inverso multiplicativo en $\mathbb R_C$ proporciona $x^{-1}\in\mathbb R_{C,\neq0}$ con

$$
xx^{-1}=1_C=x^{-1}x.
$$

Éstas son exactamente las condiciones de la convención de cuerpo Convención 3.6.7 — Terminología de cuerpo. ∎

> **Nota fundacional.** El anillo de Cauchy se obtiene con argumentos algebraicos robustos; el salto
> fundacional aparece al construir inversos de clases meramente **no nulas**, porque la separación
> cuantitativa respecto de cero se obtiene mediante Lema 9.7.2 — Separación eventual respecto de cero. Por ello:
> $$ \boxed{\text{no nulidad negativa}\neq\text{apartness positiva}.} $$

---

### Lo que hemos ganado

La construcción por sucesiones ha alcanzado ya el nivel algebraico de cuerpo:

$$
\boxed{
\mathbb R_C\text{ es un cuerpo.}
}
$$

La dificultad de los ceros iniciales de un representante quedó resuelta sin alterar la clase asintótica y sin recurrir a una selección global. El punto decisivo fue demostrar que un representante de una clase no nula está **eventualmente separado de cero**; desde ese momento, el recíproco término a término existe en toda la cola relevante.

La función inversa sobre $\mathbb R_{C,\neq0}$ no se definió escogiendo representantes. Se construyó a partir del grafo de la ecuación

$$
xy=1_C,
$$

cuya solución es única. De este modo se conserva el principio fundacional de que las clases son los objetos numéricos y los representantes son sólo instrumentos locales de prueba.

Todavía no hemos definido un orden en $\mathbb R_C$. El siguiente frente, §9.8, será construirlo directamente a partir de la información eventual de los representantes y demostrar que es independiente de la clase elegida. Sólo después podremos relacionarlo con las sucesiones constantes y completar la estructura de cuerpo ordenado.
