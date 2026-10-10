## 23.3. Continuidad de los límites uniformes {#sec-ta-23-3}

El ejemplo de las potencias de §23.1 mostró que el límite puntual de funciones continuas puede ser discontinuo. La convergencia uniforme introduce justamente el control que faltaba: un término suficientemente avanzado aproxima a la función límite en todos los puntos antes de que fijemos un entorno del punto de continuidad. Primero probaremos la transmisión de continuidad en un punto; después distinguiremos continuidad global, control uniforme sólo en un entorno y continuidad uniforme sobre todo el dominio. Ninguno de estos resultados presupone que el dominio sea abierto, compacto o siquiera no vacío.

### Teorema 23.3.1 — Continuidad de un límite uniforme en un punto
Sean $E\subseteq\mathbb R$, $\mathbf f=(f_n)_{n\in\mathbb N}:\mathbb N\to\mathbb R^E$ y $f:E\to\mathbb R$. Supongamos que $f_n$ converge uniformemente a $f$ en $E$. Si $a\in E$ y cada $f_n$ es continua en $a$ relativamente a $E$, entonces $f$ es continua en $a$ relativamente a $E$.

**Demostración.**
Fijemos $a\in E$ y $\varepsilon>0$. La convergencia uniforme aplicada a $\varepsilon/3$ proporciona $N\in\mathbb N$ tal que

$$
|f_n(y)-f(y)|<\frac\varepsilon3
\quad\text{para todo }n\ge N\text{ y todo }y\in E.
\tag{23.3.1}
$$

En particular, seleccionamos el término ya determinado $f_N$, que es continuo en $a$ por hipótesis. Con tolerancia $\varepsilon/3$, su continuidad relativa suministra $\delta>0$ tal que

$$
x\in E,\quad |x-a|<\delta
\quad\Longrightarrow\quad
|f_N(x)-f_N(a)|<\frac\varepsilon3.
\tag{23.3.2}
$$

Para cualquier $x\in E$ con $|x-a|<\delta$, la desigualdad triangular aplicada dos veces, junto con (23.3.1) en $y=x$ y en $y=a$, y con (23.3.2), da

$$
\begin{aligned}
|f(x)-f(a)|
&\le |f(x)-f_N(x)|+|f_N(x)-f_N(a)|
       +|f_N(a)-f(a)|\\
&<\frac\varepsilon3+\frac\varepsilon3+\frac\varepsilon3
 =\varepsilon.
\end{aligned}
\tag{23.3.3}
$$

El radio $\delta$ funciona para todos los puntos de $E$ suficientemente cercanos a $a$, como requiere Definición §17.1.1 — Continuidad relativa al dominio en un punto. El orden de las operaciones es esencial: $N$ se obtiene uniformemente, sin depender de $x$; sólo después recurrimos a la continuidad de esa función concreta. No hemos elegido una sucesión de radios ni intercambiado dos límites. $\square$

**Lectura de la prueba.** Los errores de los extremos de (23.3.3) se controlan con la convergencia uniforme; el error central se controla con la continuidad de un solo término. La partición $\varepsilon/3$ es una elección explícita de tolerancias y no una propiedad adicional de las funciones.

### Corolario 23.3.2 — Continuidad del límite uniforme en todo el dominio
Si todas las funciones $f_n:E\to\mathbb R$ son continuas en cada punto de $E$ y $f_n$ converge uniformemente a $f:E\to\mathbb R$ en $E$, entonces $f$ es continua en cada punto de $E$.

**Demostración.**
Sea $a\in E$ arbitrario. Cada $f_n$ es continua en $a$ y la convergencia es uniforme en $E$, por lo que Teorema §23.3.1 — Continuidad de un límite uniforme en un punto afirma que $f$ es continua en $a$. La arbitrariedad del punto prueba el enunciado global. Si $E=\varnothing$, la conclusión es una afirmación universal vacía sobre la única función de dominio vacío y codominio $\mathbb R$; no fijamos un punto inexistente. $\square$

**Consecuencia para las potencias.** En Proposición §23.1.7 — Contraejemplo: potencias puntualmente convergentes sin convergencia uniforme ya se construyó una sucesión de funciones continuas $x\mapsto x^n$ sobre $[0,1]$ cuyo límite puntual no es continuo en $1$. El corolario demuestra de nuevo que aquella convergencia no puede ser uniforme: si lo fuera, su límite puntual único sería continuo. Este segundo argumento utiliza una propiedad estructural del límite, en lugar de calcular directamente su error máximo.

### Proposición 23.3.3 — Basta la convergencia uniforme cerca del punto
Sean $E\subseteq\mathbb R$, $a\in E$, $f_n:E\to\mathbb R$ y $f:E\to\mathbb R$. Supongamos que cada $f_n$ es continua en $a$ relativamente a $E$ y que existe $r>0$ para el cual, en el conjunto

$$
V:=E\cap(a-r,a+r),
\tag{23.3.4}
$$

la sucesión de restricciones $f_n\upharpoonright V:V\to\mathbb R$ converge uniformemente a $f\upharpoonright V:V\to\mathbb R$. Entonces $f$ es continua en $a$ relativamente al dominio original $E$. No se exige convergencia uniforme fuera de $V$.

**Demostración.**
El conjunto $V$ existe por Separación, $V\subseteq E$ y $a\in V$, pues $|a-a|=0<r$. Por Definición §1.3.1 — Restricción de una función y Proposición §1.3.2 — Existencia y unicidad de la restricción, las restricciones indicadas están determinadas de manera única y tienen dominio exacto $V$, codominio $\mathbb R$. La sucesión de restricciones también está determinada término a término por su grafo en $\mathbb N\times\mathbb R^V$; no se elige ninguna función.

Para comprobar la continuidad de $f_n\upharpoonright V$ en $a$ relativa a $V$, fijemos $\eta>0$. La continuidad de $f_n$ relativa a $E$ proporciona un radio $\delta_n>0$ que controla todos los $x\in E$ cercanos a $a$, y por tanto los $x\in V$. Esto vale para cada $n$ fijado sin construir una familia de radios. El teorema Teorema §23.3.1 — Continuidad de un límite uniforme en un punto, aplicado ahora al dominio $V$ y a las funciones restringidas, demuestra que $f\upharpoonright V$ es continua en $a$ relativamente a $V$.

Sea $\varepsilon>0$ y tomemos un radio $\rho>0$ de esa última continuidad. Definamos explícitamente

$$
\delta:=\frac12\min\{r,\rho\}>0.
$$

Si $x\in E$ y $|x-a|<\delta$, entonces $|x-a|<r$, luego $x\in V$; también $|x-a|<\rho$, así que

$$
|f(x)-f(a)|
=|(f\upharpoonright V)(x)-(f\upharpoonright V)(a)|
<\varepsilon.
$$

Se ha producido un radio para la continuidad de $f$ relativa a $E$, sin imponer ninguna condición sobre el comportamiento de la sucesión lejos de $a$. $\square$

**Alcance.** La continuidad en un punto es una propiedad local, mientras que «converger uniformemente» siempre debe referirse a un dominio explícito. La proposición evita confundir ambos alcances.

### Teorema 23.3.4 — La continuidad uniforme se conserva por límites uniformes
Sean $E\subseteq\mathbb R$, $f_n:E\to\mathbb R$ y $f:E\to\mathbb R$. Si cada $f_n$ es uniformemente continua en $E$ y $f_n$ converge uniformemente a $f$ en $E$, entonces $f$ es uniformemente continua en $E$. No se requiere que $E$ sea compacto o acotado.

**Demostración.**
Supongamos primero $E\ne\varnothing$ y fijemos $\varepsilon>0$. De la convergencia uniforme, con tolerancia $\varepsilon/3$, obtenemos un natural $N$ tal que

$$
|f_N(z)-f(z)|<\frac\varepsilon3
\qquad(z\in E).
\tag{23.3.5}
$$

La función $f_N$, uniformemente continua por hipótesis, proporciona para esa misma tolerancia un radio $\delta>0$ independiente de los puntos, que verifica

$$
x,y\in E,\quad |x-y|<\delta
\quad\Longrightarrow\quad
|f_N(x)-f_N(y)|<\frac\varepsilon3.
\tag{23.3.6}
$$

Dados ahora cualesquiera $x,y\in E$ con $|x-y|<\delta$, aplicamos dos veces la desigualdad triangular:

$$
\begin{aligned}
|f(x)-f(y)|
&\le |f(x)-f_N(x)|+|f_N(x)-f_N(y)|
       +|f_N(y)-f(y)|\\
&<\varepsilon.
\end{aligned}
\tag{23.3.7}
$$

El mismo $\delta$ funciona para todas las parejas $x,y\in E$, exactamente como exige Definición §17.6.1 — Continuidad uniforme relativa a un dominio. Si $E=\varnothing$, el radio explícito $\delta=1$ verifica por vacuidad esa definición y no necesitamos seleccionar puntos. Tampoco escogimos radios $\delta_n$ para todos los índices: sólo utilizamos el radio de una función determinada $f_N$. $\square$

**Interpretación.** La continuidad ordinaria se transmite punto por punto mediante Teorema §23.3.1 — Continuidad de un límite uniforme en un punto; la continuidad uniforme exige un único radio para cualquier pareja del dominio. El nuevo teorema conserva también esa exigencia porque el término elegido $f_N$ tiene un radio que no depende de la pareja. La convergencia simplemente puntual no proporciona el primer control uniforme y no autoriza la conclusión, como ilustra Proposición §23.1.7 — Contraejemplo: potencias puntualmente convergentes sin convergencia uniforme.

**Transición.** Ya sabemos que la convergencia uniforme permite conservar una propiedad local (continuidad) e incluso una propiedad global (continuidad uniforme). En §23.4 examinaremos un intercambio distinto: cuándo puede pasarse el límite de una sucesión de funciones a través de una integral de Riemann sobre un intervalo cerrado. Allí habrá que justificar por separado la integrabilidad del límite y una cota de la diferencia de integrales.
