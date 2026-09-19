## 14.1. Serie, sumas parciales y convergencia {#sec-ta-14-1}

### Definición 14.1.1 — Sucesión de sumas parciales y serie numérica

Sea $a=(a_n)_{n\in\mathbb N}$ una sucesión real. Definimos su **sucesión de sumas parciales** como la única sucesión real

$$
\operatorname{PS}(a)=s^a=(s^a_n)_{n\in\mathbb N}
$$

que satisface las ecuaciones recursivas

$$
\boxed{
\begin{aligned}
s^a_0&=a_0,\\
s^a_{n+1}&=s^a_n+a_{n+1}
\qquad(n\in\mathbb N).
\end{aligned}
}
$$

La **serie numérica de términos $a$** es el proceso de sumación representado por esta sucesión $\operatorname{PS}(a)$. Por tanto, una serie existe como objeto secuencial **antes** de saber si converge. El calificativo «serie» indica aquí cuál es el objeto que se someterá al estudio de límites, no un número real ya obtenido.

Verifiquemos la existencia y unicidad de la construcción sin reforzar el teorema de recursión previamente cerrado. Su paso tiene la forma $g:X\to X$ y no puede depender de un índice externo. Por ello incorporaremos el índice al **estado recursivo**. Fijado $a$, tomemos

$$
X:=\mathbb N\times\mathbb R,
\qquad
H_a:X\longrightarrow X,
\qquad
H_a(\langle m,x\rangle):=
\langle m+1,x+a_{m+1}\rangle.
$$

El grafo de $H_a$ se obtiene por Separación dentro de $X\times X$. Es funcional y total: $m+1\in\mathbb N$, $a_{m+1}\in\mathbb R$, y las operaciones natural y real utilizadas están definidas y son unívocas. Aplicamos exactamente Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$ al conjunto $X$, al estado inicial $\langle0,a_0\rangle$ y a la función $H_a$. Obtenemos una única función

$$
r:\mathbb N\longrightarrow X,
\qquad
r(0)=\langle0,a_0\rangle,
\qquad
r(n+1)=H_a(r(n)).
$$

Por inducción sobre $n$, la primera componente de $r(n)$ es $n$: lo es en $0$ y el paso $H_a$ incrementa exactamente en una unidad esa componente. Denotemos por $s^a_n$ la segunda componente de $r(n)$. El grafo $\{\langle n,x\rangle\in\mathbb N\times\mathbb R:r(n)=\langle n,x\rangle\}$ existe por Separación; su funcionalidad y totalidad se siguen de las propiedades de $r$. La ecuación inicial y el paso de $r$ entregan ahora

$$
s^a_0=a_0,
\qquad
s^a_{n+1}=s^a_n+a_{n+1}.
$$

Si otra sucesión satisficiera ambas ecuaciones, una inducción sobre $n$ probaría su igualdad término a término con $s^a$, por lo que la sucesión de sumas parciales es única.

También queda determinada una operación genuina sobre el conjunto de sucesiones:

$$
\boxed{
\operatorname{PS}:\mathbb R^{\mathbb N}
\longrightarrow\mathbb R^{\mathbb N},
\qquad a\longmapsto s^a.
}
$$

En efecto, su grafo se obtiene por Separación dentro de $\mathbb R^{\mathbb N}\times\mathbb R^{\mathbb N}$ imponiendo las ecuaciones recursivas anteriores. La existencia y unicidad para cada $a$ aseguran que se trata del grafo de una función.

> **Auditoría fundacional.** No hemos escogido una suma para cada índice mediante Choice: la recursión construye una única función completa. Tampoco afirmamos que, para una sucesión arbitraria dada sólo extensionalmente, exista un procedimiento computable capaz de evaluar sus términos. La recursión proporciona una definición matemática, no un algoritmo uniforme sin datos efectivos de entrada.

---

### Notación 14.1.2 — Suma finita de términos consecutivos

Para todo $n\in\mathbb N$ escribiremos

$$
\boxed{
\sum_{k=0}^{n}a_k:=s^a_n.
}
$$

En particular,

$$
\sum_{k=0}^{0}a_k=a_0,
\qquad
\sum_{k=0}^{n+1}a_k
=\left(\sum_{k=0}^{n}a_k\right)+a_{n+1}.
$$

El símbolo de suma finita abrevia la recursión ya legitimada; no es una operación primitiva ni presupone una suma infinita. La convención inicial es $k=0$ porque $\mathbb N$ contiene $0$. Todavía no utilizamos la notación para una suma vacía ni para límites inferiores arbitrarios: se definirán cuando resulten necesarios.

---

### Proposición 14.1.3 — Recuperación de los términos y unicidad del proceso de sumación

Sean $a,b$ sucesiones reales y escribamos $s=\operatorname{PS}(a)$. Entonces

$$
\boxed{
a_0=s_0,\qquad
a_{n+1}=s_{n+1}-s_n
\quad(n\in\mathbb N).
}
$$

En consecuencia,

$$
\boxed{
\operatorname{PS}(a)=\operatorname{PS}(b)
\Longrightarrow a=b.
}
$$

**Demostración.**

La ecuación inicial de Definición 14.1.1 — Sucesión de sumas parciales y serie numérica establece $s_0=a_0$. Para cada $n\in\mathbb N$, la segunda ecuación da

$$
s_{n+1}=s_n+a_{n+1}.
$$

Restando $s_n$ a ambos miembros y aplicando las leyes del grupo aditivo del cuerpo real obtenemos

$$
s_{n+1}-s_n=a_{n+1}.
$$

Si $\operatorname{PS}(a)=\operatorname{PS}(b)=s$, las fórmulas anteriores dan $a_0=b_0$ y $a_{n+1}=b_{n+1}$ para todo $n$. Todo natural es $0$ o el sucesor de otro natural (Teorema 1.2.7 — Predecesor de todo natural no nulo, o directamente el principio de inducción Teorema 1.1.10 — Principio de inducción); por ello $a_n=b_n$ para todo $n\in\mathbb N$. Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales demuestra $a=b$. ∎

> **Interpretación.** Los términos y las sumas parciales cumplen funciones distintas, aunque cada sucesión de sumas parciales determina inequívocamente los términos que la generaron. Una sucesión de valores no se transforma en una suma real por cambiarle el nombre: necesitamos todavía una condición de convergencia.

---

### Definición 14.1.4 — Convergencia, divergencia y suma de una serie

Sea $a\in\mathbb R^{\mathbb N}$ y sea $s=\operatorname{PS}(a)$.

Diremos que la **serie de términos $a$ converge** si la sucesión real $s$ converge en el sentido de Definición 13.3.1 — Convergencia de una sucesión real; diremos que **diverge** si no es convergente. Es decir,

$$
\boxed{
\text{la serie de términos }a\text{ converge}
\iff
\exists\ell\in\mathbb R,\quad s_n\to\ell.
}
$$

Cuando la serie converge, el teorema de unicidad del límite Teorema 13.3.5 — Unicidad del límite real garantiza que existe un único $\ell\in\mathbb R$ al que convergen las sumas parciales. Llamamos a ese número la **suma de la serie** y lo denotamos, cuando se necesite como función parcial, por

$$
\operatorname{sum}(a):=\lim_{n\to\infty}\operatorname{PS}(a)_n.
$$

El dominio natural de $\operatorname{sum}$ es el conjunto

$$
\mathcal C_{\mathrm{ser}}
:=\{a\in\mathbb R^{\mathbb N}:
\operatorname{PS}(a)\text{ converge}\},
$$

que existe por Separación. La relación

$$
\left\{\langle a,\ell\rangle
\in\mathcal C_{\mathrm{ser}}\times\mathbb R:
\operatorname{PS}(a)_n\to\ell\right\}
$$

existe por Separación y es funcional por unicidad del límite. Por tanto determina una función legítima

$$
\boxed{
\operatorname{sum}:\mathcal C_{\mathrm{ser}}\longrightarrow\mathbb R.
}
$$

Si $a\notin\mathcal C_{\mathrm{ser}}$, la sucesión de sumas parciales sigue existiendo, pero $\operatorname{sum}(a)$ **no está definida**. En particular, no le asignamos por defecto los símbolos $+\infty$ o $-\infty$, que no son elementos del cuerpo real considerado.

> **Prueba de estrés.** «La serie converge» no significa «cada término es una suma bien definida», porque esa propiedad se cumple para cualquier sucesión real. Significa que la sucesión completa de sumas parciales tiene un límite **real**. La definición tampoco exige que todos los términos sean no negativos o que la sucesión original sea convergente: esas serán cuestiones separadas, cuya relación precisa demostraremos más adelante.

---

### Notación 14.1.5 — Símbolo de serie y valor de una suma infinita

La expresión

$$
\sum_{k=0}^{\infty}a_k
$$

identifica **formalmente la serie de términos $a$**, incluso cuando no se haya establecido su convergencia. El signo $\infty$ en el límite superior es parte de una notación convencional: no representa un índice natural ni el último término de una suma finita.

Cuando ya se sabe que la serie converge, la misma expresión puede utilizarse, por convención explícita, para su **valor real**. Así, la igualdad

$$
\boxed{
\sum_{k=0}^{\infty}a_k=\ell
}
$$

significa precisamente

$$
\lim_{n\to\infty}\left(\sum_{k=0}^{n}a_k\right)=\ell.
$$

No escribiremos una igualdad numérica con $\sum_{k=0}^{\infty}a_k$ si la convergencia no ha sido demostrada. La expresión puede nombrar una serie divergente, pero en ese caso **no denota un número real**.

---

### Proposición 14.1.6 — Estabilización de sumas parciales cuando los términos tardíos son nulos

Sea $a$ una sucesión real. Si existe $N\in\mathbb N$ tal que

$$
a_n=0
\qquad\text{para todo }n\ge N+1,
$$

entonces

$$
\boxed{
\sum_{k=0}^{\infty}a_k
=\sum_{k=0}^{N}a_k.
}
$$

En concreto, sus sumas parciales son constantes a partir del índice $N$.

**Demostración.**

Escribamos $s=\operatorname{PS}(a)$. Demostraremos por inducción sobre $j\in\mathbb N$ que

$$
s_{N+j}=s_N.
$$

Para $j=0$ es una identidad. Supongamos válida la igualdad para $j$. Por la recursión de las sumas parciales,

$$
s_{N+(j+1)}
=s_{N+j}+a_{N+j+1}.
$$

Por asociatividad y conmutatividad de la suma natural (Teorema 1.4.4 — Asociatividad de la suma y Teorema 1.4.5 — Conmutatividad de la suma), $N+j+1=(N+1)+j$; por la definición del orden natural, $N+1\le (N+1)+j$. La hipótesis sobre los términos da entonces $a_{N+j+1}=0$. La hipótesis inductiva produce entonces

$$
s_{N+(j+1)}=s_N+0=s_N.
$$

Por el principio de inducción Teorema 1.1.10 — Principio de inducción, la igualdad vale para todo $j$. Si $n\ge N$, la definición del orden natural Definición 1.6.1 — Orden aritmético proporciona $j\in\mathbb N$ con $n=N+j$, y así $s_n=s_N$. La sucesión $s$ coincide eventualmente con la sucesión constante $\underline{s_N}$; esta converge a $s_N$ por Proposición 13.3.4 — Las sucesiones constantes convergen a su valor, y la coincidencia eventual preserva el límite por Proposición 13.3.7 — Invariancia de la convergencia bajo coincidencia eventual. De acuerdo con Definición 14.1.4 — Convergencia, divergencia y suma de una serie y las notaciones ya establecidas,

$$
\sum_{k=0}^{\infty}a_k
=s_N
=\sum_{k=0}^{N}a_k.
$$

∎

Por ejemplo, si $a_0=c$, $a_1=d$ y $a_n=0$ para todo $n\ge2$, entonces las sumas parciales son $c,c+d,c+d,\ldots$ y la serie tiene suma $c+d$. En cambio, para la sucesión constante de términos $a_n=1_{\mathbb R}$, las ecuaciones recursivas y la aritmética de los numerales (Proposición 4.1.6 — Aritmética y orden de los numerales naturales) dan $s_n=\nu_{\mathbb R}(n+1)$. Esta sucesión es no acotada por la arquimedianidad de $\mathbb R$ (Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano) y, por Teorema 13.4.5 — Toda sucesión real convergente es acotada, no puede converger. Por consiguiente, la serie de términos todos iguales a $1_{\mathbb R}$ diverge, aunque cada suma parcial está perfectamente definida.

> **Dos controles cognitivos.** Una serie puede converger porque sus sumas parciales llegan a estabilizarse exactamente; también puede divergir aunque cada suma parcial sea un número real. En los siguientes apartados estudiaremos criterios que permitan decidir entre ambas situaciones sin calcular explícitamente todas las sumas parciales.

La definición de suma de serie transforma el problema en uno secuencial. En §14.2 aplicaremos primero el criterio de Cauchy del Capítulo 13 a las sumas parciales y deduciremos de él la condición necesaria de que los términos tiendan a cero. Ninguno de esos resultados ha sido supuesto en la presente construcción.

---
