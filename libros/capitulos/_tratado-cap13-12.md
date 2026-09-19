## 13.12. Límites inferior y superior {#sec-ta-13-12}

Una sucesión acotada puede no converger y, sin embargo, conservar una estructura asintótica precisa. Bolzano--Weierstrass garantiza que alguna subsucesión converge, pero no identifica los extremos del conjunto de todos esos límites. Para hacerlo no basta observar el supremo y el ínfimo del recorrido completo: un único término inicial excepcional podría alterarlos. Debemos examinar los valores que sobreviven en cada cola.

En §13.8 construimos, para una sucesión acotada $a$, los conjuntos no vacíos $T_N(a)$ y las envolventes reales

$$
L_N(a)=\inf T_N(a),\qquad U_N(a)=\sup T_N(a).
$$

Se probó también que $L(a)$ es creciente y acotada superiormente, que $U(a)$ es decreciente y acotada inferiormente, y que

$$
\boxed{L_N(a)\le a_N\le U_N(a).}
$$

La completitud permite obtener dos límites; la cuestión esencial de esta sección es qué significan.

### Teorema 13.12.1 — Convergencia de las envolventes de colas

Sea $a=(a_n)$ una sucesión real acotada. Existen únicos $\alpha,\beta\in\mathbb R$ tales que

$$
\boxed{L_N(a)\longrightarrow\alpha,\qquad U_N(a)\longrightarrow\beta.}
$$

Además, si $L(a)[\mathbb N]$ y $U(a)[\mathbb N]$ denotan los recorridos de las respectivas envolventes,

$$
\boxed{
\alpha=\sup L(a)[\mathbb N],
\qquad
\beta=\inf U(a)[\mathbb N].
}
$$

**Demostración.**

Por Definición 13.8.4 — Envolventes inferior y superior de las colas, $L(a)$ y $U(a)$ son sucesiones reales. Sus recorridos existen como imágenes de funciones y son no vacíos, pues $0\in\mathbb N$. La proposición Proposición 13.8.5 — Monotonía y encajamiento de las envolventes de colas establece que $L(a)$ es creciente y está acotada superiormente, mientras que $U(a)$ es decreciente y está acotada inferiormente. Aplicando a cada una el teorema de convergencia monótona Teorema 13.7.3 — Teorema de convergencia monótona, obtenemos respectivamente

$$
L_N(a)\to\sup L(a)[\mathbb N],
\qquad
U_N(a)\to\inf U(a)[\mathbb N].
$$

Ambos extremos son reales porque los recorridos son no vacíos y están acotados en la dirección correspondiente. La unicidad de cada límite se sigue de Teorema 13.3.5 — Unicidad del límite real. Denominándolos $\alpha$ y $\beta$, se obtienen exactamente las afirmaciones. ∎

> **Dependencia decisiva.** La existencia de los extremos de cada cola y la convergencia de sus envolventes son dos intervenciones diferenciadas de la completitud. No se deduce que exista un procedimiento para calcular ninguno de esos extremos.

---

### Definición 13.12.2 — Límite inferior y límite superior

Sea $a=(a_n)$ una **sucesión real acotada**. Definimos su **límite inferior** y su **límite superior** por

$$
\boxed{
\liminf_{n\to\infty}a_n
:=\lim_{N\to\infty}L_N(a)
=\sup L(a)[\mathbb N],
}
$$

$$
\boxed{
\limsup_{n\to\infty}a_n
:=\lim_{N\to\infty}U_N(a)
=\inf U(a)[\mathbb N].
}
$$

Son dos **números reales**, no valores de un nuevo conjunto numérico. La escritura habitual equivalente es

$$
\boxed{
\liminf_{n\to\infty}a_n
=\sup_{N\in\mathbb N}\inf T_N(a),
\qquad
\limsup_{n\to\infty}a_n
=\inf_{N\in\mathbb N}\sup T_N(a).
}
$$

En estas expresiones, el supremo y el ínfimo exteriores se aplican a los conjuntos de valores de las envolventes, cuya existencia se acaba de demostrar. El índice $N$ de la envolvente y el índice $n$ de la sucesión original cumplen papeles distintos.

> **Lectura de los cuantificadores.** El ínfimo de una cola es su frontera inferior; al descartar progresivamente los primeros términos, esas fronteras pueden subir. Su supremo registra la frontera inferior asintótica. Dualmente, el supremo de una cola es su frontera superior; al descartar términos, esas fronteras pueden bajar. Su ínfimo registra la frontera superior asintótica.

> **Restricción de dominio.** No definimos todavía $\liminf$ o $\limsup$ para sucesiones reales no acotadas: podrían requerir límites infinitos y los reales extendidos, que no forman parte de la infraestructura actual. La acotación garantiza aquí que ambas expresiones denotan reales finitos.

---

### Lema 13.12.3 — Aproximación de los extremos de cada cola por valores de la cola

Sean $a$ una sucesión real acotada, $N\in\mathbb N$ y $\eta>0$. Existen índices $m,n\in\mathbb N$, ambos mayores o iguales que $N$, tales que

$$
\boxed{
L_N(a)\le a_m<L_N(a)+\eta,
}
$$

$$
\boxed{
U_N(a)-\eta<a_n\le U_N(a).
}
$$

**Demostración.**

Fijemos $N$ y $\eta>0$. Como $L_N(a)$ es una cota inferior de $T_N(a)$, todo $y\in T_N(a)$ verifica $L_N(a)\le y$. Si no existiera ningún $y\in T_N(a)$ con $y<L_N(a)+\eta$, la totalidad del orden daría

$$
L_N(a)+\eta\le y
\qquad(y\in T_N(a)).
$$

Entonces $L_N(a)+\eta$ sería una cota inferior de $T_N(a)$ estrictamente mayor que su ínfimo $L_N(a)$, en contradicción con la maximalidad de este último. Existe, pues, $y\in T_N(a)$ con

$$
L_N(a)\le y<L_N(a)+\eta.
$$

La definición de imagen $T_N(a)=a[\mathbb N_{\ge N}]$ proporciona un índice $m\ge N$ con $a_m=y$.

De modo dual, $U_N(a)$ es cota superior de $T_N(a)$. Si ningún $y\in T_N(a)$ satisficiera $U_N(a)-\eta<y$, entonces todos cumplirían $y\le U_N(a)-\eta$. Este último número sería una cota superior estrictamente menor que el supremo $U_N(a)$, contradicción. Existe $y\in T_N(a)$ con $U_N(a)-\eta<y\le U_N(a)$ y, por ser valor de la cola, existe $n\ge N$ con $a_n=y$. ∎

> **Qué se obtiene realmente.** Para cada par fijo $(N,\eta)$ se demuestra la existencia de índices de aproximación. No se ha elegido una familia simultánea de índices para todos los pares. Este lema no afirma que el supremo o ínfimo de la cola deban alcanzarse: sólo exige valores arbitrariamente próximos por el lado apropiado.

---

### Proposición 13.12.4 — Orden de los límites extremos y confinamiento de los puntos límite

Sea $a$ una sucesión real acotada. Escribamos

$$
\alpha:=\liminf_{n\to\infty}a_n,
\qquad
\beta:=\limsup_{n\to\infty}a_n.
$$

Entonces

$$
\boxed{\alpha\le\beta,}
$$

y todo punto límite secuencial $x\in\operatorname{LimSub}(a)$ satisface

$$
\boxed{\alpha\le x\le\beta.}
$$

**Demostración.**

Por Proposición 13.8.5 — Monotonía y encajamiento de las envolventes de colas, para cada $N$ tenemos $L_N(a)\le U_N(a)$. Como ambas envolventes convergen por Teorema 13.12.1 — Convergencia de las envolventes de colas, el teorema de conservación de orden Teorema 13.6.2 — Preservación del orden en el paso al límite implica

$$
\alpha\le\beta.
$$

Fijemos ahora $x\in\operatorname{LimSub}(a)$. Por las definiciones Definición 13.10.1 — Punto límite secuencial y Definición 13.10.4 — Conjunto de puntos límite secuenciales, existe un selector estrictamente creciente $\phi:\mathbb N\to\mathbb N$ tal que la subsucesión

$$
b_k:=a_{\phi(k)}
$$

converge a $x$. Fijemos un $N\in\mathbb N$ cualquiera. Por la cofinalidad de los selectores (Proposición 13.9.2 — Crecimiento, inyectividad y cofinalidad de los selectores de índices), existe $K$ tal que $\phi(k)\ge N$ para todo $k\ge K$. Así $b_k\in T_N(a)$ y

$$
L_N(a)\le b_k\le U_N(a)
\qquad(k\ge K).
$$

Las sucesiones constantes de valores $L_N(a)$ y $U_N(a)$ convergen respectivamente a esos valores por Proposición 13.3.4 — Las sucesiones constantes convergen a su valor. Aplicando dos veces Teorema 13.6.2 — Preservación del orden en el paso al límite a las desigualdades eventuales, deducimos

$$
L_N(a)\le x\le U_N(a).
$$

Como $N$ era arbitrario, estas desigualdades valen para todo $N$. Aplicamos otra vez la conservación de orden a las sucesiones $L(a)$, constante $\underline x$ y $U(a)$, que convergen respectivamente a $\alpha,x,\beta$. Obtenemos

$$
\alpha\le x\le\beta.
$$

Quedan probadas ambas afirmaciones. ∎

> **Precaución lógica.** El resultado no afirma que todo real entre $\alpha$ y $\beta$ sea punto límite. Sólo dice que ninguno puede quedar fuera del intervalo cerrado determinado por ambos extremos.

---

### Teorema 13.12.5 — Los límites inferior y superior son puntos límite secuenciales

Para toda sucesión real acotada $a$,

$$
\boxed{
\liminf_{n\to\infty}a_n\in\operatorname{LimSub}(a),
\qquad
\limsup_{n\to\infty}a_n\in\operatorname{LimSub}(a).
}
$$

**Demostración.**

Denotemos por $\alpha$ y $\beta$ los dos límites de Teorema 13.12.1 — Convergencia de las envolventes de colas. Aplicaremos el criterio de visitas arbitrariamente tardías Proposición 13.10.3 — Criterio de visitas arbitrariamente tardías: basta demostrar, para un real candidato $z$, que

$$
\forall\varepsilon>0\;\forall N\in\mathbb N\;
\exists n\ge N:\ |a_n-z|<\varepsilon.
$$

**El extremo inferior.** Fijemos $\varepsilon>0$ y $N\in\mathbb N$. Definamos $s:=1+1>0$ y $\eta:=\varepsilon s^{-1}>0$, de manera que $\eta+\eta=\varepsilon$. Como $L_K(a)\to\alpha$, existe $K_0\in\mathbb N$ tal que para todo $K\ge K_0$,

$$
\alpha-\eta<L_K(a)<\alpha+\eta.
$$

Fijamos un índice $K$ mayor o igual que $K_0$ y que $N$; por ejemplo, tomamos $K_0$ si $N\le K_0$ y $N$ en caso contrario. Esta es una definición por casos sobre dos naturales, no una elección entre infinitos candidatos.

Por Lema 13.12.3 — Aproximación de los extremos de cada cola por valores de la cola, existe $n\ge K$ tal que

$$
L_K(a)\le a_n<L_K(a)+\eta.
$$

Combinando las desigualdades,

$$
\alpha-\eta<a_n<\alpha+\eta+\eta
=\alpha+\varepsilon.
$$

Puesto que $\eta<\varepsilon$, también $\alpha-\varepsilon<a_n$. Así

$$
\alpha-\varepsilon<a_n<\alpha+\varepsilon,
\qquad n\ge N,
$$

lo que equivale a $|a_n-\alpha|<\varepsilon$. El criterio de visitas prueba $\alpha\in\operatorname{LimSub}(a)$.

**El extremo superior.** Con los mismos $\varepsilon,N,s,\eta$, ahora de $U_K(a)\to\beta$ obtenemos un umbral $K_0$ tal que $|U_K(a)-\beta|<\eta$ para todo $K\ge K_0$. Tomamos de nuevo $K\ge K_0,N$. El lema Lema 13.12.3 — Aproximación de los extremos de cada cola por valores de la cola proporciona $n\ge K$ con

$$
U_K(a)-\eta<a_n\le U_K(a).
$$

Se sigue que

$$
\beta-\varepsilon
=\beta-\eta-\eta<a_n<\beta+\eta<\beta+\varepsilon.
$$

Por tanto $|a_n-\beta|<\varepsilon$ para algún $n\ge N$. Como $\varepsilon,N$ eran arbitrarios, Proposición 13.10.3 — Criterio de visitas arbitrariamente tardías da $\beta\in\operatorname{LimSub}(a)$. ∎

> **Arquitectura de la prueba.** Primero hacemos que el extremo de una cola quede cerca de su límite; después usamos la propiedad característica de ínfimo o supremo para encontrar **un término de esa misma cola** próximo al extremo. El criterio de visitas ya cerrado convierte esas aproximaciones en una subsucesión convergente usando mínimos naturales. No hemos escogido de forma arbitraria una sucesión de testigos.

---

### Corolario 13.12.6 — Extremos del conjunto de puntos límite

Para toda sucesión real acotada $a$, el conjunto $\operatorname{LimSub}(a)$ tiene mínimo y máximo, y

$$
\boxed{
\min\operatorname{LimSub}(a)
=\liminf_{n\to\infty}a_n,
\qquad
\max\operatorname{LimSub}(a)
=\limsup_{n\to\infty}a_n.
}
$$

**Demostración.**

Sean $\alpha=\liminf a_n$ y $\beta=\limsup a_n$. Teorema 13.12.5 — Los límites inferior y superior son puntos límite secuenciales establece que ambos pertenecen a $\operatorname{LimSub}(a)$; en particular, el conjunto no es vacío. Por Proposición 13.12.4 — Orden de los límites extremos y confinamiento de los puntos límite, todo $x$ en él verifica $\alpha\le x\le\beta$. Así $\alpha$ pertenece al conjunto y es menor o igual que cualquiera de sus elementos, por lo que es su mínimo. Dualmente, $\beta$ es su máximo. ∎

La palabra «extremo» adquiere ahora su sentido exacto: los límites inferior y superior no son sólo cotas abstractas de los límites de subsucesiones; **son límites de subsucesiones y constituyen los extremos de todos ellos**.

---

### Teorema 13.12.7 — Criterio de convergencia mediante los límites extremos

Sea $a=(a_n)$ una sucesión real **acotada**. Son equivalentes:

1. $a$ converge en $\mathbb R$;
2. $\displaystyle\liminf_{n\to\infty}a_n=\limsup_{n\to\infty}a_n$;
3. $\operatorname{LimSub}(a)$ consta de un único elemento.

Cuando se cumplen estas condiciones, los tres valores —límite ordinario, límite inferior y límite superior— son iguales al único punto límite secuencial.

**Demostración.**

Supongamos primero que $a_n\to\ell$. Por Proposición 13.10.5 — Puntos límite de una sucesión convergente,

$$
\operatorname{LimSub}(a)=\{\ell\},
$$

luego se cumple la condición 3.

Si el conjunto de puntos límite es $\{\ell\}$, su mínimo y su máximo coinciden con $\ell$. Por Corolario 13.12.6 — Extremos del conjunto de puntos límite, el límite inferior y el superior son iguales. Así 3 implica 2.

Supongamos finalmente 2 y escribamos $r$ para ese valor común. Por Teorema 13.12.1 — Convergencia de las envolventes de colas,

$$
L_N(a)\to r,
\qquad
U_N(a)\to r.
$$

Por Proposición 13.8.5 — Monotonía y encajamiento de las envolventes de colas, para **cada** $N$ se tiene

$$
L_N(a)\le a_N\le U_N(a).
$$

El teorema del sándwich Teorema 13.6.5 — Teorema del sándwich demuestra entonces $a_N\to r$. Así 2 implica 1. La unicidad del límite ordinario (Teorema 13.3.5 — Unicidad del límite real) y el corolario de extremos identifican todos los valores indicados. ∎

> **Dónde es indispensable la hipótesis.** Para una sucesión no acotada no están definidos aquí los límites extremos, y la condición «un único punto límite» **no** bastaría por sí sola para concluir convergencia. El ejemplo de §13.11 que alterna ceros con numerales reales crecientes tiene $0$ como único límite de subsucesiones convergentes, pero no converge como sucesión completa. La acotación impide precisamente que una porción de la sucesión escape sin dejar puntos límite adicionales.

---

### Proposición 13.12.8 — Invariancia de los límites extremos bajo coincidencia eventual

Sean $a,b$ sucesiones reales acotadas que coinciden eventualmente. Entonces

$$
\boxed{
\liminf_{n\to\infty}a_n=\liminf_{n\to\infty}b_n,
\qquad
\limsup_{n\to\infty}a_n=\limsup_{n\to\infty}b_n.
}
$$

**Demostración.**

Por coincidencia eventual existe $N_0$ tal que $a_n=b_n$ para todo $n\ge N_0$. Para cada $N\ge N_0$, las dos sucesiones tienen exactamente el mismo conjunto de valores en la cola:

$$
T_N(a)=T_N(b).
$$

En efecto, todo elemento del conjunto de la izquierda tiene la forma $a_n$ con $n\ge N$, y entonces $a_n=b_n$; la inclusión inversa es simétrica. Por unicidad de supremos e ínfimos,

$$
L_N(a)=L_N(b),
\qquad
U_N(a)=U_N(b)
\qquad(N\ge N_0).
$$

Así $L(a)$ y $L(b)$ coinciden eventualmente, lo mismo que $U(a)$ y $U(b)$. Sus cuatro límites existen por Teorema 13.12.1 — Convergencia de las envolventes de colas. La estabilidad de la convergencia bajo coincidencia eventual Proposición 13.3.7 — Invariancia de la convergencia bajo coincidencia eventual y la unicidad Teorema 13.3.5 — Unicidad del límite real igualan cada par de límites. Por Definición 13.12.2 — Límite inferior y límite superior, son precisamente las dos identidades buscadas. ∎

---

**Ejemplos y pruebas de estrés.** En la sucesión alternante $0,1,0,1,\ldots$ de §13.10, cada cola contiene ambos valores. En consecuencia, $L_N=0$ y $U_N=1$ para todo $N$; su límite inferior es $0$, su límite superior es $1$ y el conjunto de puntos límite es exactamente $\{0,1\}$. No todos los números del intervalo $[0,1]$ son puntos límite: por ejemplo, $1/2$ no lo es. En cambio, si $a_0=100$ y $a_n=0$ para $n\ge1$, el supremo del recorrido total es $100$, pero las envolventes de toda cola con $N\ge1$ valen $0$; de aquí $\liminf a_n=\limsup a_n=0$, y la sucesión converge a $0$. Los límites extremos registran el comportamiento persistente, no los accidentes de un prefijo finito.

Hemos cerrado así la cadena

$$
\boxed{
\text{envolventes de colas}
\longrightarrow
\liminf,\limsup
\longrightarrow
\min\operatorname{LimSub}(a),\max\operatorname{LimSub}(a)
\longrightarrow
\text{criterio de convergencia}.
}
$$

La teoría anterior se ha desarrollado exclusivamente para sucesiones reales acotadas. Con ella queda cerrado el primer capítulo propiamente analítico de la Parte II: la completitud de $\mathbb R$ se ha convertido en una teoría operativa de convergencia, Cauchy, subsucesiones, puntos límite y extremos asintóticos.

El paso siguiente cambia el objeto sin cambiar todavía la noción de convergencia: una **serie numérica** será estudiada mediante la sucesión de sus sumas parciales. El Capítulo 14 comenzará, por tanto, reutilizando íntegramente la infraestructura secuencial construida aquí.

---
