## 14.2. Criterio de Cauchy para series y condición necesaria de convergencia {#sec-ta-14-2}

Una serie se definió como una sucesión de sumas parciales. Por ello, el criterio de Cauchy del Capítulo 13 puede aplicarse sin introducir una nueva noción de completitud. Sin embargo, necesitamos traducir la diferencia entre dos sumas parciales al lenguaje natural de una **suma de términos consecutivos**. Éste es el contenido de la primera notación.

### Notación 14.2.1 — Suma de un bloque finito posterior

Sea $a=(a_n)$ una sucesión real y sea $s=\operatorname{PS}(a)$. Para naturales $n<m$, definimos la suma del **bloque de términos posterior a $n$ y terminado en $m$** por

$$
\boxed{
\sum_{k=n+1}^{m}a_k:=s_m-s_n.
}
$$

El bloque comienza en $n+1$, **no** en $n$: el término $a_n$ ya está contenido en $s_n$. Esta notación sólo se utiliza aquí cuando $n<m$, por lo que el bloque contiene al menos un término. No definimos todavía sumas vacías ni intervalos arbitrarios de índices. La igualdad precedente es una definición de una cantidad real finita, no una serie infinita.

---

### Proposición 14.2.2 — Identidades de los bloques de sumación

Si $a$ es una sucesión real, $s=\operatorname{PS}(a)$ y $n<m$ son naturales, entonces:

1. el primer bloque tiene un solo término:
   $$
   \boxed{\sum_{k=n+1}^{n+1}a_k=a_{n+1};}
   $$
2. prolongar el extremo derecho añade exactamente el siguiente término:
   $$
   \boxed{\sum_{k=n+1}^{m+1}a_k
   =\left(\sum_{k=n+1}^{m}a_k\right)+a_{m+1};}
   $$
3. las sumas parciales se recuperan del bloque:
   $$
   \boxed{s_m=s_n+\sum_{k=n+1}^{m}a_k;}
   $$
4. si $n<r<m$, podemos partir el bloque en dos:
   $$
   \boxed{\sum_{k=n+1}^{m}a_k
   =\sum_{k=n+1}^{r}a_k+\sum_{k=r+1}^{m}a_k.}
   $$

**Demostración.**

La recursión Definición 14.1.1 — Sucesión de sumas parciales y serie numérica y la recuperación de términos Proposición 14.1.3 — Recuperación de los términos y unicidad del proceso de sumación dan

$$
\sum_{k=n+1}^{n+1}a_k=s_{n+1}-s_n=a_{n+1}.
$$

Para el segundo punto, por la misma recursión,

$$
\begin{aligned}
\sum_{k=n+1}^{m+1}a_k
&=s_{m+1}-s_n\\
&=(s_m+a_{m+1})-s_n\\
&=(s_m-s_n)+a_{m+1}\\
&=\sum_{k=n+1}^{m}a_k+a_{m+1}.
\end{aligned}
$$

La tercera identidad resulta de sumar $s_n$ a $s_m-s_n$. Para la cuarta, la asociatividad y las leyes de opuesto en $\mathbb R$ permiten escribir

$$
\begin{aligned}
s_m-s_n
&=(s_r-s_n)+(s_m-s_r)\\
&=\sum_{k=n+1}^{r}a_k+\sum_{k=r+1}^{m}a_k.
\end{aligned}
$$

Por definición, el miembro izquierdo es el bloque completo. ∎

Las dos primeras identidades verifican además que nuestra notación reproduce exactamente la adición finita ordinaria de los términos $a_{n+1},\ldots,a_m$: empieza por el primero y incorpora sucesivamente los restantes. No hemos introducido una suma infinita encubierta.

---

### Teorema 14.2.3 — Criterio de Cauchy para una serie numérica

Sea $a=(a_n)$ una sucesión real. Son equivalentes:

1. la serie $\sum_{k=0}^{\infty}a_k$ converge en $\mathbb R$;
2. para cada $\varepsilon\in\mathbb R$ con $\varepsilon>0$ existe $N\in\mathbb N$ tal que, para todos los naturales $n,m$,
   $$
   \boxed{
   N\le n<m
   \quad\Longrightarrow\quad
   \left|\sum_{k=n+1}^{m}a_k\right|<\varepsilon.
   }
   $$

**Demostración.**

Escribamos $s=\operatorname{PS}(a)$. Por Definición 14.1.4 — Convergencia, divergencia y suma de una serie, la afirmación (1) significa que $s$ converge. El criterio de Cauchy real Corolario 13.8.8 — Criterio de Cauchy en $\mathbb R$ proporciona la equivalencia

$$
s\text{ converge}
\iff
\forall\varepsilon>0\;\exists N\in\mathbb N\;
\forall m,n\ge N:
|s_m-s_n|<\varepsilon.
$$

Si vale esta última condición y $N\le n<m$, entonces la definición del bloque da directamente

$$
\left|\sum_{k=n+1}^{m}a_k\right|
=|s_m-s_n|<\varepsilon.
$$

Recíprocamente, supongamos (2) y fijemos $\varepsilon>0$. Tomemos el umbral $N$ que proporciona (2). Sean $m,n\ge N$. La tricotomía natural ya cerrada en Proposición 1.6.7 — Tricotomía decidible de los naturales permite distinguir tres posibilidades. Si $n<m$, la identidad del bloque entrega $|s_m-s_n|<\varepsilon$. Si $m<n$, aplicamos (2) al par ordenado $m<n$ y utilizamos $|s_m-s_n|=|s_n-s_m|$, propiedad ya probada en Proposición 4.2.2 — Propiedades elementales del valor absoluto (3). Si $m=n$, obtenemos $|s_m-s_n|=0<\varepsilon$. Por consiguiente, $s$ es de Cauchy según Definición 13.8.1 — Sucesión real de Cauchy y converge en $\mathbb R$ por Corolario 13.8.8 — Criterio de Cauchy en $\mathbb R$. La definición de serie concluye (1). ∎

> **Qué mide el criterio.** No pide que una sola suma parcial sea pequeña ni que los términos individuales se hagan pequeños: exige que **cada bloque finito completo** suficientemente alejado del origen tenga suma de valor absoluto menor que la tolerancia. Los dos extremos $n,m$ se cuantifican después de elegir un único umbral $N$.

> **Auditoría fundacional.** La implicación «serie convergente $\Rightarrow$ bloques pequeños» utiliza sólo «convergente $\Rightarrow$ Cauchy», sin completitud. Para la recíproca importamos la completitud de $\mathbb R$ ya encapsulada en Corolario 13.8.8 — Criterio de Cauchy en $\mathbb R$ y su lógica clásica declarada. No usamos Choice: el criterio afirma un umbral por tolerancia, no una selección global de umbrales. Tampoco obtenemos un módulo computable de convergencia.

---

### Teorema 14.2.4 — Condición necesaria de convergencia: el término general tiende a cero

Si la serie de términos $a=(a_n)$ converge, entonces

$$
\boxed{a_n\longrightarrow0.}
$$

**Demostración.**

Sea $\varepsilon>0$. Sea $s=\operatorname{PS}(a)$. Su convergencia es la hipótesis por Definición 14.1.4 — Convergencia, divergencia y suma de una serie. El teorema Teorema 13.8.2 — Toda sucesión real convergente es de Cauchy demuestra directamente —sin utilizar completitud— que $s$ es de Cauchy: existe $N\in\mathbb N$ tal que

$$
m,n\ge N\Longrightarrow |s_m-s_n|<\varepsilon.
$$

En particular, para cada $n\ge N$, tomemos $m=n+1$. La identidad de un bloque con un término (Proposición 14.2.2 — Identidades de los bloques de sumación) da

$$
\boxed{|a_{n+1}|<\varepsilon\qquad(n\ge N).}
$$

Para verificar la definición de convergencia de la sucesión **original** —que empieza en $a_0$, no en $a_1$—, establezcamos el umbral $N':=N+1$. Si $k\ge N'$, la definición del orden natural da un $j\in\mathbb N$ con

$$
k=(N+1)+j=(N+j)+1.
$$

La última igualdad utiliza asociatividad y conmutatividad de la suma natural. Pongamos $n:=N+j$; entonces $n\ge N$ y $k=n+1$. Por la estimación anterior,

$$
|a_k-0|=|a_{n+1}|<\varepsilon.
$$

Hemos probado que para cada $\varepsilon>0$ existe un umbral $N'$ que sirve para **todos** los índices $k\ge N'$. Por Definición 13.3.1 — Convergencia de una sucesión real, $a_n\to0$. ∎

> **Una implicación, no una equivalencia.** El resultado demuestra que los términos de una serie convergente se anulan asintóticamente. No afirma que la mera anulación asintótica controle la suma de bloques con un número arbitrariamente grande de términos.

---

### Corolario 14.2.5 — Criterio de divergencia por el término general

Si $a_n$ **no converge a cero**, entonces la serie $\sum_{k=0}^{\infty}a_k$ diverge. En particular, si $a_n\to\ell$ para algún $\ell\in\mathbb R$ con $\ell\ne0$, la serie diverge.

**Demostración.**

Si la serie convergiera, Teorema 14.2.4 — Condición necesaria de convergencia: el término general tiende a cero implicaría $a_n\to0$, en contradicción con la hipótesis. Para la segunda afirmación, si además $a_n\to\ell$ y la serie convergiera, la unicidad del límite Teorema 13.3.5 — Unicidad del límite real produciría $\ell=0$, contra $\ell\ne0$. ∎

Por ejemplo, recuperamos inmediatamente la divergencia de la serie de términos constantes iguales a $1_{\mathbb R}$, ya mostrada en §14.1. El corolario permite detectarla mirando los términos. No debemos, sin embargo, invertir esta regla lógica: para decidir si una sucesión de términos que sí tiende a cero genera una serie convergente, necesitamos información adicional.

---

### Lema 14.2.6 — Cota inferior para un bloque de términos acotados inferiormente

Sean $a$ una sucesión real, $n\in\mathbb N$, $d\in\mathbb N$ con $d\ne0$ y $c\in\mathbb R$. Si

$$
\forall k\in\mathbb N,
\quad n<k\le n+d\Longrightarrow c\le a_k,
$$

entonces

$$
\boxed{
\sum_{k=n+1}^{n+d}a_k\ge\nu_{\mathbb R}(d)\,c.
}
$$

**Demostración.**

La suma tiene sentido porque $d\ne0$ implica $n<n+d$, por las propiedades ya demostradas del orden y la suma natural. Demostraremos por inducción sobre $j\in\mathbb N$ la afirmación del enunciado para $d=j+1$. Esta formulación cubre todos los naturales no nulos por Teorema 1.2.7 — Predecesor de todo natural no nulo.

Para $j=0$, la hipótesis proporciona $a_{n+1}\ge c$. Por la identidad del bloque de un término,

$$
\sum_{k=n+1}^{n+1}a_k=a_{n+1}
\ge c=\nu_{\mathbb R}(1)c.
$$

Supongamos ahora válida la afirmación para $d=j+1$ y consideremos un bloque terminado en $n+(j+2)$ cuyos términos son todos mayores o iguales que $c$. Sus primeros $j+1$ términos satisfacen la misma cota. La hipótesis inductiva da

$$
\sum_{k=n+1}^{n+(j+1)}a_k
\ge\nu_{\mathbb R}(j+1)c.
$$

El término nuevo satisface $a_{n+(j+2)}\ge c$. Por la identidad de prolongación de Proposición 14.2.2 — Identidades de los bloques de sumación y la compatibilidad aditiva de los numerales (Proposición 4.1.6 — Aritmética y orden de los numerales naturales),

$$
\begin{aligned}
\sum_{k=n+1}^{n+(j+2)}a_k
&=\sum_{k=n+1}^{n+(j+1)}a_k+a_{n+(j+2)}\\
&\ge\nu_{\mathbb R}(j+1)c+c\\
&=\nu_{\mathbb R}(j+2)c.
\end{aligned}
$$

El paso usa sólo que sumar desigualdades preserva el orden en el cuerpo real; no se exige $c\ge0$. La inducción concluye el resultado para cada $d\ge1$. ∎

> **Lectura de la estimación.** Una cota inferior para cada término de un bloque produce una cota para la suma que depende también de **cuántos términos tiene**. Ese número de términos será precisamente lo que impida invertir el teorema anterior.

---

### Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica

Definamos para cada $n\in\mathbb N$

$$
\boxed{
h_n:=\nu_{\mathbb R}(n+1)^{-1}.
}
$$

Entonces $h=(h_n)$ es una sucesión real positiva tal que $h_n\to0$, pero la serie

$$
\sum_{k=0}^{\infty}h_k
$$

**diverge**. Ésta es la serie armónica, escrita con índices desde cero y numerales reales explícitos.

**Demostración.**

El lema cerrado Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero demuestra, exactamente para los recíprocos de los numerales positivos $\nu_{\mathbb R}(n+1)$, que $h$ es una sucesión real, $h_n>0$ y

$$
h_n\longrightarrow0.
$$

Demostraremos que sus sumas parciales no son de Cauchy. Fijemos **un natural arbitrario** $N$ y pongamos

$$
d:=N+1,
\qquad
m:=N+d.
$$

Así $N<m$ y, por las leyes de suma natural,

$$
m+1=d+d.
$$

Escribamos $r:=\nu_{\mathbb R}(d)$. Como $d>0$, la preservación del orden por los numerales Proposición 4.1.6 — Aritmética y orden de los numerales naturales asegura $r>0$. Para cada índice $k$ del bloque $N<k\le m$, tenemos $k+1\le m+1$ y, por tanto,

$$
0<\nu_{\mathbb R}(k+1)
\le\nu_{\mathbb R}(m+1)=r+r.
$$

La inversión revierte el orden de los positivos. Para justificar aquí la versión **no estricta** sin separar artificialmente casos de igualdad, podemos multiplicar la desigualdad anterior por el producto positivo de los dos recíprocos: de $0<x\le y$ obtenemos $y^{-1}\le x^{-1}$. Aplicándolo a los numerales precedentes resulta

$$
h_k=\nu_{\mathbb R}(k+1)^{-1}
\ge(r+r)^{-1}=:c.
$$

Hay exactamente $d$ términos entre los índices $N+1$ y $N+d=m$. El lema Lema 14.2.6 — Cota inferior para un bloque de términos acotados inferiormente aplicado al bloque proporciona

$$
\sum_{k=N+1}^{m}h_k
\ge\nu_{\mathbb R}(d)c
=r(r+r)^{-1}.
$$

Como $r+r=(1+1)r$ y $r\ne0$, las leyes del cuerpo real dan

$$
\boxed{
\sum_{k=N+1}^{m}h_k
\ge(1+1)^{-1}.
}
$$

El número $\eta:=(1+1)^{-1}$ es positivo. Si la serie convergiera, su sucesión de sumas parciales sería de Cauchy por Teorema 13.8.2 — Toda sucesión real convergente es de Cauchy y la definición Definición 14.1.4 — Convergencia, divergencia y suma de una serie. Para la tolerancia $\varepsilon:=\eta$ existiría un umbral $N_0$ tal que todos los pares $m>n\ge N_0$ verificaran $|s_m-s_n|<\eta$. Pero tomando $N=N_0$ en la construcción precedente, y recordando que el bloque es $s_m-s_N$, obtenemos

$$
|s_m-s_N|
\ge\eta,
$$

pues la suma del bloque es al menos $\eta>0$. Esto contradice la condición de Cauchy. Por tanto la serie armónica diverge. ∎

> **Prueba de estrés de la condición necesaria.** Cada término $h_n$ se vuelve pequeño; sin embargo, para cualquier lugar desde el que comencemos podemos sumar suficientes términos posteriores —en este caso, desde $N+1$ hasta $2N+1$— y obtener una cantidad al menos igual a $(1+1)^{-1}$. La diferencia entre **controlar un término** y **controlar todos los bloques** no es una sutileza notacional: es la razón exacta por la que la implicación del teorema 14.2.4 no admite conversa.

> **Frontera deductiva.** La prueba no usa logaritmos, potencias naturales generales, el criterio de comparación ni la condensación de Cauchy; todos ellos quedan fuera de esta unidad. Los recíprocos de numerales y la arquimedianidad se importan de Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero. No se presupone una suma infinita real para la serie armónica: precisamente demostramos que no existe.

---

La sección nos deja una distinción operacional: la convergencia de una serie es una propiedad de sus **sumas parciales**; el criterio de Cauchy la mide mediante **bloques enteros**; y la anulación del término general es sólo una consecuencia necesaria. El siguiente apartado podrá estudiar series geométricas a partir de identidades finitas, sin confundir una fórmula para sumas parciales con una suma infinita ya existente.

---
