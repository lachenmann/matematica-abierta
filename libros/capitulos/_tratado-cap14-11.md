## 14.11. Series alternadas, criterio de Leibniz y estimación del resto {#sec-ta-14-11}

El ejemplo condicional de §14.8 se construyó cancelando exactamente cada pareja de términos; el reordenamiento de §14.10 mostró que esa cancelación no autoriza cambiar libremente el orden. Ahora estudiaremos una situación más regular: los signos se alternan y las magnitudes, aun sin formar una serie convergente, disminuyen hacia cero. La clave no será acotar una cola por la suma de sus valores absolutos, sino **encerrar las sumas parciales entre dos sucesiones monótonas**.

Conviene distinguir tres hipótesis. La alternancia prescribe los signos; el decrecimiento controla la comparación entre términos contiguos; la tendencia a cero obliga a que desaparezca la separación entre las dos familias de sumas parciales. Ninguna de esas tres funciones debe confundirse con las demás.

### Definición 14.11.1 — Serie alternada asociada a una sucesión de magnitudes

Sea $b:\mathbb N\to\mathbb R$ una sucesión con $b_n\ge0$ para todo $n$. Definimos la **sucesión alternada que comienza con signo positivo** por

$$
\boxed{a_n:=(-1)^n b_n\qquad(n\in\mathbb N).}
\tag{14.11.1}
$$

Aquí $-1$ es un elemento de $\mathbb R$ y la potencia $(-1)^n$ es la potencia de **exponente natural** definida en Definición 14.3.1 — Potencias naturales de un número real; no es una operación sobre índices enteros ni una potencia real de exponente arbitrario. Por la recursión de las potencias y las leyes del cuerpo,

$$
(-1)^{2k}=1,\qquad (-1)^{2k+1}=-1.
$$

Por tanto $a_{2k}=b_{2k}$ y $a_{2k+1}=-b_{2k+1}$. La dicotomía de paridad Lema 3.9.3 — Dicotomía de paridad establece que estas dos fórmulas determinan todos los índices. El grafo de $a$ se obtiene por Separación dentro de $\mathbb N\times\mathbb R$ porque a cada $n$ le corresponde exactamente un producto real. La **serie alternada** es la serie de términos $a$ en el sentido de §14.1; que sea alternada no presupone su convergencia.

Si deseamos comenzar con signo negativo, tomaremos el opuesto de esta sucesión; no modificaremos silenciosamente la convención (14.11.1). Admitimos magnitudes nulas y, por consiguiente, no exigimos que cada término tenga signo estrictamente positivo o negativo.

---

### Lema 14.11.2 — Las sumas parciales pares decrecen y las impares crecen

Supongamos que $b_n\ge0$ y $b_{n+1}\le b_n$ para todo $n\in\mathbb N$. Sean $a_n=(-1)^n b_n$ y $s=\operatorname{PS}(a)$. Definamos, sólo como abreviaturas de sucesiones reales ya determinadas,

$$
E_k:=s_{2k},\qquad O_k:=s_{2k+1}\qquad(k\in\mathbb N).
$$

Entonces $E$ es decreciente, $O$ es creciente y, para todo $k$,

$$
\boxed{O_k\le E_{k+1}\le E_k,\qquad O_k\le O_{k+1},}
\tag{14.11.2}
$$

$$
\boxed{E_k-O_k=b_{2k+1}.}
\tag{14.11.3}
$$

En particular, $O_0\le E_k\le E_0$ y $O_0\le O_k\le E_0$ para todo $k$: ambas sucesiones son acotadas. Sus límites existen, y cada uno de los valores $O_k$ es menor o igual que el límite de $O$, mientras cada $E_k$ es mayor o igual que el límite de $E$.

**Demostración.**

Las ecuaciones recursivas de las sumas parciales y la paridad de las potencias dan

$$
\begin{aligned}
O_k&=E_k-b_{2k+1},\\
E_{k+1}&=O_k+b_{2k+2},\\
O_{k+1}&=E_{k+1}-b_{2k+3}.
\end{aligned}
\tag{14.11.4}
$$

La no negatividad asegura $O_k\le E_{k+1}$ y $O_k\le E_k$. Además,

$$
E_{k+1}-E_k=-b_{2k+1}+b_{2k+2}\le0,
$$

$$
O_{k+1}-O_k=b_{2k+2}-b_{2k+3}\ge0,
$$

pues $b$ es decreciente. Esto prueba (14.11.2); la primera ecuación de (14.11.4) prueba (14.11.3). La disminución de $E$ y el crecimiento de $O$, junto con $O_0\le E_k$ y $O_k\le E_k\le E_0$, muestran las cotas anunciadas sin recurrir a ninguna suma infinita.

Apliquemos ahora el teorema de convergencia monótona Teorema 13.7.3 — Teorema de convergencia monótona **por separado** a $E$ y $O$. Existen $U,V\in\mathbb R$ con $E_k\to U$ y $O_k\to V$. La monotonía y el orden en el límite (Teorema 13.6.2 — Preservación del orden en el paso al límite) justifican $E_k\ge U$ y $O_k\le V$ para cada índice fijo: por ejemplo, $E_j\le E_k$ para todo $j\ge k$, y al pasar al límite de $j$ obtenemos $U\le E_k$; análogamente para $O$. No se afirma aún que $U=V$; eso necesitará $b_n\to0$. ∎

> **Lectura geométrica.** Las sumas de índice par descienden por escalones; las de índice impar ascienden. En cada etapa el intervalo $[O_k,E_k]$ tiene longitud $b_{2k+1}$. Si esa longitud tiende a cero, los dos límites no pueden seguir siendo distintos.

---

### Teorema 14.11.3 — Criterio de Leibniz

Sea $b:\mathbb N\to\mathbb R$ una sucesión tal que, para todo $n\in\mathbb N$,

$$
\boxed{0\le b_{n+1}\le b_n,\qquad b_n\longrightarrow0.}
\tag{14.11.5}
$$

Entonces la serie alternada

$$
\boxed{\sum_{n=0}^{\infty}(-1)^n b_n}
$$

**converge a un número real** $S$. Si $s$ es su sucesión de sumas parciales, se verifica además

$$
\boxed{s_{2k+1}\le S\le s_{2k}\qquad(k\in\mathbb N).}
\tag{14.11.6}
$$

**Demostración.**

El lema Lema 14.11.2 — Las sumas parciales pares decrecen y las impares crecen proporciona los límites $E_k\to U$ y $O_k\to V$. Como $2k+1\ge k$, la hipótesis $b_n\to0$ implica $b_{2k+1}\to0$: dado $\varepsilon>0$, basta tomar el mismo umbral para $k$ que el proporcionado para $n$. La identidad finita (14.11.3) da

$$
E_k-O_k=b_{2k+1}\longrightarrow0.
$$

El álgebra de límites del Capítulo 13 (Proposición 13.5.2 — Límite del opuesto y de una diferencia) muestra a la vez que $E_k-O_k\to U-V$; por unicidad del límite, $U-V=0$ y $U=V$. Escribamos $S:=U=V$. Las cotas individuales del lema se convierten inmediatamente en

$$
O_k\le S\le E_k.
$$

Debemos comprobar aún la convergencia de la **sucesión completa** $s$, no sólo la de sus dos familias de índices. Sea $\varepsilon>0$. Como $E_k\to S$ y $O_k\to S$, existen índices $K_E,K_O$ a partir de los cuales sus diferencias con $S$ son menores que $\varepsilon$. Tomemos $K$ igual al mayor de estos dos naturales y $N:=2K$. Si $n\ge N$, la dicotomía de paridad escribe $n=2k$ o $n=2k+1$. En cualquiera de los dos casos $k\ge K$: si $k<K$, el crecimiento estricto de la multiplicación natural por $2$ produciría $2k+1<2K$, incompatible con $n\ge2K$. Por ello

$$
|s_n-S|=
\begin{cases}
|E_k-S|<\varepsilon,&n=2k,\\
|O_k-S|<\varepsilon,&n=2k+1.
\end{cases}
$$

Hemos probado $s_n\to S$, que es exactamente la definición de convergencia de la serie. La desigualdad (14.11.6) ya se obtuvo de los límites monótonos. El razonamiento sólo escoge **dos umbrales para una tolerancia fijada**, no una familia de testigos mediante el axioma de elección. ∎

> **Alcance.** «Decreciente» significa aquí *no creciente*: se permiten igualdades y ceros. El teorema no declara que la serie de magnitudes $\sum b_n$ converja. Precisamente por eso será útil para reconocer convergencia condicional.

---

### Corolario 14.11.4 — Encierro de la suma y cota del primer término omitido

Bajo las hipótesis del criterio de Leibniz, escribamos $S=\sum_{k=0}^{\infty}(-1)^k b_k$ y $s_n=\sum_{k=0}^{n}(-1)^k b_k$. Para **todo** $n\in\mathbb N$,

$$
\boxed{\begin{cases}s_{n+1}\le S\le s_n,&n\text{ par},\\s_n\le S\le s_{n+1},&n\text{ impar}.\end{cases}}
\tag{14.11.7}
$$

$$
\boxed{0\le(-1)^n(s_n-S)\le b_{n+1},\qquad
|S-s_n|\le b_{n+1}.}
\tag{14.11.8}
$$

La expresión $R_n:=S-s_n$ designará **localmente**, sólo para esta serie ya convergente, el resto después de sumar hasta el índice $n$. La desigualdad anterior estima ese número real, no una «suma infinita de cola» presupuesta sin demostración.

**Demostración.**

La paridad separa exhaustivamente los casos. Si $n=2k$, por (14.11.6) tenemos $O_k\le S\le E_k=s_n$ y $O_k=s_{n+1}$. Restando $S$ y utilizando (14.11.3),

$$
0\le s_n-S\le E_k-O_k=b_{2k+1}=b_{n+1}.
$$

Si $n=2k+1$, entonces $s_n=O_k\le S$. La demostración de Lema 14.11.2 — Las sumas parciales pares decrecen y las impares crecen dio $S\le E_j$ para **cada** $j$; en particular $S\le E_{k+1}=s_{n+1}$. Como $E_{k+1}=O_k+b_{2k+2}$,

$$
0\le S-s_n\le E_{k+1}-O_k=b_{2k+2}=b_{n+1}.
$$

En ambos casos $S$ se encuentra entre las dos sumas parciales consecutivas. El signo de $s_n-S$ es $(-1)^n$, de donde se obtiene la primera desigualdad de (14.11.8); la segunda se sigue de la definición de valor absoluto y de $b_{n+1}\ge0$. ∎

> **Uso práctico de la estimación.** Para garantizar $|S-s_n|<\varepsilon$, basta encontrar un índice con $b_{n+1}<\varepsilon$. La mera afirmación $b_n\to0$ asegura que existen tales índices, pero no proporciona automáticamente un algoritmo para calcularlos a partir de una sucesión dada sin información efectiva.
>
> **La cota es óptima como constante universal.** Con $b_0=b_1=1$ y $b_n=0$ para $n\ge2$, la suma de la serie es $0$, mientras $s_0=1$ y $b_1=1$; por tanto $|S-s_0|=b_1$. No puede reemplazarse el factor $1$ por una constante estrictamente menor válida para todas las series del teorema.

---

### Corolario 14.11.5 — Caracterización para magnitudes decrecientes

Si $b_n\ge0$ y $b_{n+1}\le b_n$ para todos los naturales, entonces

$$
\boxed{\sum_{n=0}^{\infty}(-1)^n b_n\text{ converge}
\iff b_n\longrightarrow0.}
\tag{14.11.9}
$$

**Demostración.**

La implicación de derecha a izquierda es Teorema 14.11.3 — Criterio de Leibniz. Para la recíproca, la convergencia de la serie implica $a_n=(-1)^n b_n\to0$ por Teorema 14.2.4 — Condición necesaria de convergencia: el término general tiende a cero. Como $|(-1)^n|=|-1|^n=1$ (potencias y Lema 14.3.3 — El valor absoluto conmuta con las potencias naturales) y $b_n\ge0$, tenemos $|a_n|=b_n$. El valor absoluto preserva límites (Proposición 13.5.5 — El valor absoluto preserva límites), de modo que $b_n=|a_n|\to|0|=0$. ∎

El resultado no debe leerse como un criterio universal para series con signos mezclados: presupone exactamente la forma alternada y la monotonía de $b$. Tampoco da una condición necesaria y suficiente de **convergencia absoluta**; esa última pregunta se refiere, por definición, a $\sum b_n$.

---

### Proposición 14.11.6 — La serie armónica alternada converge condicionalmente

Sea $h_n:=\nu_{\mathbb R}(n+1)^{-1}$ la sucesión armónica de §14.2. La serie

$$
\boxed{\sum_{n=0}^{\infty}(-1)^n\,\nu_{\mathbb R}(n+1)^{-1}}
\tag{14.11.10}
$$

converge, pero no converge absolutamente; es, por tanto, **condicionalmente convergente**.

**Demostración.**

Los numerales $\nu_{\mathbb R}(n+1)$ son estrictamente positivos y $\nu_{\mathbb R}(n+2)>\nu_{\mathbb R}(n+1)$ por la preservación del orden natural (Proposición 4.1.6 — Aritmética y orden de los numerales naturales). En un cuerpo ordenado, si $0<x<y$, entonces $0<y^{-1}<x^{-1}$: multiplicar $x<y$ por el producto positivo $x^{-1}y^{-1}$ da $y^{-1}<x^{-1}$. En consecuencia $h_n>0$ y $h_{n+1}<h_n$. Además $h_n\to0$ por Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero. El criterio de Leibniz prueba la convergencia de (14.11.10).

En cambio, $|(-1)^n h_n|=h_n$, y la serie armónica $\sum h_n$ diverge por Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica. Por definición de §14.8, la convergencia es condicional. No asignamos aquí un valor cerrado a la suma: su existencia se ha demostrado sin logaritmos ni integración. ∎

> **Contraste con §14.8.** Allí construimos una serie condicional cuyo par de términos consecutivos se cancela exactamente. Aquí no hay cancelación exacta de todas las parejas, pero las sumas pares e impares quedan encajadas y su separación tiende a cero. Son dos demostraciones distintas de convergencia, no dos justificaciones intercambiables.

---

### Proposición 14.11.7 — Alternancia y anulación sin decrecimiento no bastan

Existe una sucesión de magnitudes $b:\mathbb N\to\mathbb R$ tal que $b_n\ge0$ y $b_n\to0$, pero $b$ **no** es decreciente y la serie $\sum(-1)^n b_n$ diverge. Por tanto el decrecimiento no puede suprimirse de Teorema 14.11.3 — Criterio de Leibniz dejando intactas las otras dos hipótesis.

**Demostración.**

Definamos por paridad, utilizando la sucesión armónica $h$,

$$
\boxed{b_{2k}:=h_k,\qquad b_{2k+1}:=0.}
\tag{14.11.11}
$$

La dicotomía de paridad y la unicidad de su parámetro hacen de (14.11.11) una función total cuyo grafo existe por Separación en $\mathbb N\times\mathbb R$. Sus valores son no negativos. Para cualquier $\varepsilon>0$, el límite $h_k\to0$ da $K$ tal que $h_k<\varepsilon$ para $k\ge K$. Si $n\ge2K$, la paridad obliga a escribir $n=2k$ o $n=2k+1$ con $k\ge K$; en ambos casos $|b_n|<\varepsilon$. Por tanto $b_n\to0$.

No es decreciente: $b_{2k+1}=0<h_{k+1}=b_{2k+2}$ para todo $k$. Al formar $a_n=(-1)^n b_n$, obtenemos

$$
a_{2k}=h_k,\qquad a_{2k+1}=0.
$$

Si $H_k=\sum_{j=0}^{k}h_j$, la definición recursiva de las sumas parciales y una inducción prueban

$$
\operatorname{PS}(a)_{2k}=\operatorname{PS}(a)_{2k+1}=H_k.
$$

La serie armónica de términos no negativos diverge (Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica). Si $\operatorname{PS}(a)$ convergiera a $S$, dado $\varepsilon>0$ habría un umbral $N$ para el que $|\operatorname{PS}(a)_n-S|<\varepsilon$ siempre que $n\ge N$; tomando $n=2k+1$ y $k\ge N$, deduciríamos $H_k\to S$, contradicción. La serie alternada construida diverge. ∎

> **Dos errores que conviene evitar.** Con $b_n=1$ los signos alternan y las magnitudes decrecen en sentido no estricto, pero los términos no tienden a cero: la serie diverge por Corolario 14.2.5 — Criterio de divergencia por el término general. Con (14.11.11), en cambio, las magnitudes sí tienden a cero, pero un término nulo alterna con uno positivo; se pierde la monotonía y las sumas acumulan toda la serie armónica.

---

El criterio de Leibniz completa un segundo mecanismo de convergencia junto a la convergencia absoluta: una serie puede converger por cancelación **controlada**, aunque la serie de magnitudes diverja. La cota del resto cuantifica esta cancelación sin presuponer una suma infinita de cola. Las permutaciones estudiadas en §14.10 no deben confundirse con una teoría general de agrupaciones consecutivas, que no hemos introducido.

El último asunto pendiente concierne a los criterios de crecimiento: ¿qué podemos concluir si las raíces de los términos no tienen límite ordinario? El límite superior finito desarrollado para sucesiones acotadas permitirá formular una respuesta exacta.

---
