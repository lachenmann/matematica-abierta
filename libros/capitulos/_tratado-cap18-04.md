## 18.4. Compacidad secuencial y Bolzano–Weierstrass: alcance fundacional {#sec-ta-18-4}

Heine–Borel caracteriza los compactos de la recta mediante dos propiedades de conjuntos. Las sucesiones ofrecen una tercera perspectiva, pero exigen distinguir dos operaciones lógicas: **extraer una subsucesión de una sucesión ya dada** y **fabricar una sucesión eligiendo un punto de cada uno de infinitos conjuntos no vacíos**. La primera operación puede realizarse en nuestro desarrollo sin elección, gracias a la bisección canónica de §13.11. La segunda, para subconjuntos arbitrarios de $\mathbb R$, no está autorizada por ZF sin hipótesis adicional.

### Definición 18.4.1 — Compacidad secuencial de un subconjunto de la recta
Un conjunto $K\subseteq\mathbb R$ es **secuencialmente compacto** si para toda función $s:\mathbb N\to\mathbb R$ cuyos términos pertenecen a $K$ existen un selector estrictamente creciente $\varphi:\mathbb N\to\mathbb N$ y un punto $\ell\in K$ tales que la subsucesión $s\circ\varphi$ converge a $\ell$:

$$
\boxed{\begin{gathered}
\forall s:\mathbb N\to\mathbb R,\quad
\bigl[(\forall n\in\mathbb N)\ s_n\in K\bigr]
\Longrightarrow\\
\exists\varphi:\mathbb N\to\mathbb N\ \exists\ell\in K:\quad
\bigl[(\forall n)\ \varphi(n)<\varphi(n+1)\bigr]
\land s_{\varphi(n)}\longrightarrow\ell.
\end{gathered}}
$$

La definición reutiliza los selectores y las subsucesiones tipadas de Definición §13.9.1 — Selector de índices de subsucesión–Definición §13.9.3 — Subsucesión de una sucesión real. La flecha de límite es la convergencia real de Definición §13.3.1 — Convergencia de una sucesión real. **El límite debe pertenecer a $K$**: obtener sólo una subsucesión convergente en la recta es una afirmación distinta. En particular, para $K=\varnothing$ no existe ninguna sucesión $\mathbb N\to\mathbb R$ con todos sus términos en $K$ (pues $0\in\mathbb N$); la condición universal es verdadera, de modo que el vacío es secuencialmente compacto.

### Teorema 18.4.2 — Todo compacto real es secuencialmente compacto
Para todo $K\subseteq\mathbb R$,

$$
\boxed{K\text{ compacto}\Longrightarrow K\text{ secuencialmente compacto}.}
$$

**Demostración.**
Sea $K$ compacto. Por Proposición §18.3.2 — Todo compacto de la recta es acotado, $K$ es acotado; por Proposición §18.3.3 — Todo compacto de la recta es cerrado, es cerrado. Fijemos **una sucesión dada** $s:\mathbb N\to\mathbb R$ con $s_n\in K$ para todo $n$. Si $K=\varnothing$, tal sucesión no existe y no hay nada que demostrar. En el caso no vacío, las cotas de $K$ son también cotas de $s$, de manera que $s$ es una sucesión acotada en el sentido de Definición §13.4.1 — Sucesiones acotadas superiormente, inferiormente y acotadas.

El teorema de Bolzano–Weierstrass ya cerrado, Teorema §13.11.5 — Bolzano–Weierstrass para sucesiones reales, proporciona un selector estrictamente creciente $\varphi:\mathbb N\to\mathbb N$ y un real $\ell$ tales que

$$
 s_{\varphi(n)}\longrightarrow\ell.
$$

Cada término de esta subsucesión pertenece a $K$, pues $\varphi(n)\in\mathbb N$ y todos los términos de $s$ pertenecen a $K$. La dirección incondicional del criterio de cerradura Teorema §15.8.8 — Criterios secuenciales de cerradura y apertura: alcance exacto afirma que el límite de cualquier sucesión convergente contenida en un cerrado está en dicho cerrado. Por tanto, $\ell\in K$. El selector y el límite satisfacen exactamente Definición §18.4.1 — Compacidad secuencial de un subconjunto de la recta.

**Control de elección.** La sucesión $s$ era un dato, no el producto de una selección. La construcción de la subsucesión se delega a Teorema §13.11.5 — Bolzano–Weierstrass para sucesiones reales, cuya prueba utiliza bisección determinista e índices naturales mínimos. La aplicación de cerradura sólo considera la subsucesión ya obtenida. No se escogieron puntos de una familia numerable de subconjuntos arbitrarios de $\mathbb R$. $\square$

**Relación con Bolzano–Weierstrass.** Este último teorema garantiza, para *toda sucesión acotada*, una subsucesión convergente **en $\mathbb R$**; la cerradura de $K$ es el paso adicional que coloca su límite **dentro de $K$**. La compacidad por cubiertas proporciona ambas hipótesis mediante §§18.3.2–18.3.3.

### Proposición 18.4.3 — Acotación secuencial bajo elección numerable explícita
**Bajo la hipótesis adicional $\mathrm{CC}(\mathbb R)$ formulada en Teorema §15.8.9 — Formulaciones habituales bajo una hipótesis de elección explícita**, todo conjunto secuencialmente compacto $K\subseteq\mathbb R$ es acotado. Esta hipótesis es local al enunciado y **no se adopta como axioma del tratado**.

**Demostración condicional.**
Supongamos $K$ secuencialmente compacto y no acotado. Para cada $n\in\mathbb N$ definamos

$$
 E_n:=\{x\in K:|x|>\nu_{\mathbb R}(n)\}.
$$

Estos conjuntos existen por Separación, y la dependencia unívoca de $n$ permite constituir una función $E:\mathbb N\to\mathcal P(\mathbb R)$ mediante su grafo. **Cada $E_n$ es no vacío**: si alguno fuese vacío, tendríamos $|x|\le\nu_{\mathbb R}(n)$ para todo $x\in K$, y por las propiedades del valor absoluto $K$ estaría contenido en el intervalo acotado $[-\nu_{\mathbb R}(n),\nu_{\mathbb R}(n)]$, contra la hipótesis.

**Éste es el único paso que requiere elección numerable:** por $\mathrm{CC}(\mathbb R)$ obtenemos una función $s:\mathbb N\to\mathbb R$ con $s_n\in E_n$ para cada $n$; en particular,

$$
 s_n\in K,\qquad |s_n|>\nu_{\mathbb R}(n).
$$

La compacidad secuencial da una subsucesión $s_{\varphi(k)}$ convergente. Por Teorema §13.4.5 — Toda sucesión real convergente es acotada, dicha subsucesión es acotada: existe $M>0$ con $|s_{\varphi(k)}|\le M$ para todo $k$. Pero Proposición §13.9.2 — Crecimiento, inyectividad y cofinalidad de los selectores de índices garantiza $\varphi(k)\ge k$; como los numerales reales preservan el orden,

$$
 |s_{\varphi(k)}|>\nu_{\mathbb R}(\varphi(k))
 \ge\nu_{\mathbb R}(k).
$$

La propiedad arquimediana proporciona un $k$ con $\nu_{\mathbb R}(k)>M$, contradicción. Así $K$ es acotado **bajo la hipótesis indicada**. $\square$

### Proposición 18.4.4 — Cerradura secuencial bajo elección numerable explícita
**Bajo la misma hipótesis adicional $\mathrm{CC}(\mathbb R)$**, todo conjunto secuencialmente compacto $K\subseteq\mathbb R$ es cerrado en $\mathbb R$. Tampoco aquí se adopta la hipótesis globalmente.

**Demostración condicional.**
Supongamos que $K$ es secuencialmente compacto, pero no cerrado. Por el criterio de cerrado Proposición §15.3.6 — Criterio de cerradura mediante puntos exteriores existe un $x\in\mathbb R\setminus K$ tal que **toda** bola $B_r(x)$ de radio positivo corta a $K$: de lo contrario el complemento sería abierto en cada uno de sus puntos.

Para $n\in\mathbb N$, sea $\rho_n:=(\nu_{\mathbb R}(n+1))^{-1}>0$ y definamos el conjunto no vacío

$$
 E_n:=K\cap B_{\rho_n}(x).
$$

El grafo de $E:\mathbb N\to\mathcal P(\mathbb R)$ se obtiene por Separación y los radios están determinados por una fórmula, sin selección. Aplicamos **explícitamente** $\mathrm{CC}(\mathbb R)$ a esta familia: existe una sucesión $s:\mathbb N\to\mathbb R$ con $s_n\in E_n$ para todo $n$. Se cumple entonces

$$
 s_n\in K,\qquad |s_n-x|<\rho_n.
$$

Como $\rho_n\to0$ por Lema §13.10.2 — Los recíprocos de los numerales positivos tienden a cero aplicada al cuerpo real, se sigue directamente de la definición $\varepsilon$–$N$ que $s_n\to x$. La compacidad secuencial proporciona un selector creciente $\varphi$ y un límite $\ell\in K$ con $s_{\varphi(n)}\to\ell$. Por Teorema §13.9.5 — Toda subsucesión de una sucesión convergente converge al mismo límite, también $s_{\varphi(n)}\to x$. La unicidad del límite Teorema §13.3.5 — Unicidad del límite real implica $\ell=x$, contradictorio con $\ell\in K$ y $x\notin K$. Concluimos que $K$ es cerrado **bajo $\mathrm{CC}(\mathbb R)$**. $\square$

### Teorema 18.4.5 — Equivalencia secuencial de Heine–Borel, formulación condicional
**Si se supone $\mathrm{CC}(\mathbb R)$**, para todo $K\subseteq\mathbb R$ son equivalentes las tres propiedades:

1. $K$ es compacto por cubiertas abiertas.
2. $K$ es cerrado y acotado.
3. $K$ es secuencialmente compacto.

**Demostración condicional.**
La equivalencia entre (1) y (2) es el teorema de Heine–Borel Teorema §18.3.4 — Heine–Borel en la recta real, demostrado sin elección. La implicación (1) $\Rightarrow$ (3) es Teorema §18.4.2 — Todo compacto real es secuencialmente compacto, también incondicional. Para (3) $\Rightarrow$ (2) se utilizan Proposición §18.4.3 — Acotación secuencial bajo elección numerable explícita y Proposición §18.4.4 — Cerradura secuencial bajo elección numerable explícita, **ambas exclusivamente bajo la hipótesis adicional indicada**. Finalmente, (2) $\Rightarrow$ (1) es de nuevo Heine–Borel. Esto cierra las tres equivalencias bajo $\mathrm{CC}(\mathbb R)$, sin cambiar el fundamento general del tratado. $\square$

**Alcance exacto.** En ZF con lógica clásica, el tratado dispone ya de $K$ compacto $\Rightarrow$ $K$ secuencialmente compacto y de cerrado y acotado $\Leftrightarrow$ compacto. La recíproca secuencial establecida en esta sección tiene **una hipótesis explícita adicional**. No es correcto omitirla al citar el teorema ni trasladar sin prueba una equivalencia topológica familiar a nuestro marco fundacional. La diferencia aparece al intentar construir, a partir de una condición existencial en cada vecindad o en cada región lejana, una *sola sucesión de testigos*.

**Transición.** Regresamos ahora a las cubiertas abiertas: la siguiente unidad demostrará que la imagen de un compacto bajo una función continua vuelve a ser compacta. Esta prueba utilizará preimágenes de abiertos y una subcubierta finita; no necesitará ninguna equivalencia secuencial ni $\mathrm{CC}(\mathbb R)$.
