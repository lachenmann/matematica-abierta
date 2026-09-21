## 24.8. Derivadas sucesivas, recuperación y unicidad de los coeficientes {#sec-ta-24-8}

La derivación término a término de §24.7 se demostró para **una** serie de potencias de radio positivo o infinito. Para reiterarla no basta afirmar informalmente que «podemos seguir derivando»: debemos construir la sucesión de coeficientes correspondiente a cada orden, comprobar que ninguna iteración reduce el radio y preservar el dominio común de las funciones derivadas. Después identificaremos los datos que la función suma determina en su centro y distinguiremos rigurosamente la igualdad en un entorno de la coincidencia en un único punto. Usaremos la notación factorial ya construida en §20.8: $k!\in\mathbb N$ y $\eta_k:=\nu_{\mathbb R}(k!)>0$ es su imagen real. Los cocientes con $\eta_k$ no identifican literalmente los naturales con números reales.

### Definición 24.8.1 — Iteración canónica de la transformación de coeficientes
Sea $a:\mathbb N\to\mathbb R$ una sucesión dada. La operación $\partial$ de «Coeficientes de la serie derivada formal» envía cada sucesión real $u$ a la única sucesión definida por $(\partial u)_n=\nu_{\mathbb R}(n+1)u_{n+1}$. Por «Existencia de $B^A$» existe el conjunto $\mathbb R^{\mathbb N}$ de sucesiones reales y, mediante Separación en $\mathbb R^{\mathbb N}\times\mathbb R^{\mathbb N}$, esa fórmula determina el grafo de una función total $\partial:\mathbb R^{\mathbb N}\to\mathbb R^{\mathbb N}$.

La recursión natural «Teorema de recursión sobre $\mathbb N$», aplicada a esta función total y al dato $a$, produce una **única** sucesión de sucesiones

$$
\boxed{\mathbf a:\mathbb N\longrightarrow\mathbb R^{\mathbb N},\qquad
\mathbf a(0)=a,\qquad \mathbf a(k+1)=\partial\bigl(\mathbf a(k)\bigr).}
\tag{24.8.1}
$$

Escribiremos localmente $a^{[k]}:=\mathbf a(k)$ y $a^{[k]}_n:=\mathbf a(k)(n)$. Los corchetes distinguen la **iteración algebraica de coeficientes** de las potencias de números y de la derivada de una función. En particular, $a^{[0]}=a$ y $a^{[1]}=\partial a$; los términos existen para todos los pares $(k,n)$, incluso si la serie de potencias de radio cero carece de un intervalo abierto de convergencia. No se ha elegido una sucesión independiente en cada etapa: la recursión sobre una operación total determina la familia completa de manera única.

### Lema 24.8.2 — Fórmula factorial de los coeficientes iterados
Para todos $k,n\in\mathbb N$ se tiene la identidad **entre números reales**

$$
\boxed{a^{[k]}_n=\frac{\eta_{n+k}}{\eta_n}\,a_{n+k}.}
\tag{24.8.2}
$$

En particular,

$$
\boxed{a^{[k]}_0=\eta_k a_k.}
\tag{24.8.3}
$$

**Demostración.**
Inducimos sobre $k$ demostrando una proposición **para todos** los índices $n$ en cada paso. Para $k=0$, la definición da $a^{[0]}_n=a_n$; el cociente $\eta_n/\eta_n=1$ es válido porque $\eta_n>0$ («Positividad y recurrencia de los factoriales»). Supongamos ahora que (24.8.2) vale para el orden $k$ y todo $n$. Por la recurrencia (24.8.1), la definición de $\partial$ y la hipótesis inductiva evaluada en $n+1$,

$$
\begin{aligned}
a^{[k+1]}_n
&=\nu_{\mathbb R}(n+1)\,a^{[k]}_{n+1}\\
&=\nu_{\mathbb R}(n+1)\,
  \frac{\eta_{n+1+k}}{\eta_{n+1}}a_{n+1+k}\\
&=\frac{\eta_{n+(k+1)}}{\eta_n}a_{n+(k+1)}.
\end{aligned}
\tag{24.8.4}
$$

La última igualdad utiliza la recurrencia real de los factoriales $\eta_{n+1}=\nu_{\mathbb R}(n+1)\eta_n$, la asociatividad de la adición natural y la cancelación de un factor estrictamente positivo. Concluye la inducción para todos los pares $(k,n)$. Tomar $n=0$ y usar $\eta_0=1$ da (24.8.3). No aparece un cociente con factorial nulo ni una selección numerable. $\square$

### Teorema 24.8.3 — Derivadas de todo orden y conservación del radio
Sea $a:\mathbb N\to\mathbb R$, $c\in\mathbb R$ y supongamos que el radio $R(a,c)$ es un real **estrictamente positivo** o la marca formal $+\infty$. Sea $I=(c-R,c+R)$ en el caso finito positivo e $I=\mathbb R$ en el infinito, como en «Continuidad de la función suma en el interior». Entonces, para **todo** $k\in\mathbb N$:

1. La serie de potencias con coeficientes $a^{[k]}$ tiene exactamente el mismo radio que la original, incluidos los casos de radio finito positivo e infinito.
2. Su función suma restringida
   $$
   F_k:=F_{a^{[k]},c}\upharpoonright I:I\longrightarrow\mathbb R
   \tag{24.8.5}
   $$
   existe, y su serie converge absoluta y uniformemente en cada $K_r=[c-r,c+r]$ estrictamente interior; la cota uniforme puede depender de $k$ y de $r$.
3. $F_0=F_{a,c}\upharpoonright I$ y $F_k$ es derivable en todos los puntos de $I$, con $F_k'=F_{k+1}$ allí. Por tanto $F_0$ posee derivadas de **todo orden** en $I$ y, usando la definición recursiva $F_0^{(0)}:=F_0$, $F_0^{(k+1)}:=(F_0^{(k)})'$, se cumple
   $$
   \boxed{F_0^{(k)}(x)=\sum_{n=0}^{\infty}
   \frac{\eta_{n+k}}{\eta_n}a_{n+k}(x-c)^n
   \qquad(k\in\mathbb N,\ x\in I).}
   \tag{24.8.6}
   $$

La iteración funcional $F_0^{(k)}$ **sólo** se entiende sobre $I$, donde quedará verificada su existencia. La cuantificación $\forall k\,\forall r$ de la convergencia uniforme no afirma la existencia de una cota única válida para todos los órdenes simultáneamente. Si el radio es cero, la familia algebraica (24.8.1) continúa definida, pero este teorema no atribuye derivadas a la función con dominio singleton $\{c\}$.

**Demostración.**
**1. Radios por inducción.** Para $k=0$ la igualdad $R(a^{[0]},c)=R(a,c)$ es inmediata. Si vale para $k$, la identidad $a^{[k+1]}=\partial(a^{[k]})$ y «Igualdad exacta de los radios de la serie y su derivada formal» demuestran

$$
R(a^{[k+1]},c)=R(a^{[k]},c)=R(a,c).
\tag{24.8.7}
$$

La inducción vale igualmente cuando ambos radios son la marca formal infinita, pues sólo se establece igualdad de casos y no se opera con $+\infty$. Bajo la hipótesis de radio positivo/infinito, la clasificación «Clasificación por el radio y convergencia interior» da $I\subseteq C(a^{[k]},c)$ para cada $k$.

**2. Funciones tipadas y convergencia.** La función suma $F_{a^{[k]},c}$ existe con dominio exacto $C(a^{[k]},c)$ por «Existencia y unicidad de la función suma sobre su dominio exacto». Su restricción $F_k$ tiene dominio exacto $I$ y codominio $\mathbb R$; la igualdad (24.8.5) no identifica indebidamente los conjuntos de convergencia en los extremos. Para un $k$ **arbitrario y fijo** y cualquier radio $r$ admisible, aplicamos «Convergencia absoluta uniforme y cota geométrica del resto» a la serie $a^{[k]}$: proporciona la convergencia absoluta uniforme en $K_r$ y un resto geométrico para ese par de parámetros. Los testigos $M,q$ de esa aplicación no se ensamblan en una función $(k,r)\mapsto(M,q)$ y no se usa Choice. Como cada $F_k$ está caracterizada por el límite único en cada $x$, su grafo se obtiene por Separación en $I\times\mathbb R$; el grafo de $k\mapsto F_k$ se obtiene dentro de $\mathbb N\times\mathbb R^I$, porque para cada $k$ hay exactamente una función del tipo indicado.

**3. Relación entre derivadas.** Fijemos de nuevo $k$. El teorema de derivación término a término «Derivación término a término en el interior del radio» se aplica a la serie de coeficientes $a^{[k]}$, cuyo radio acabamos de comprobar que es positivo o infinito. Su serie derivada tiene coeficientes $\partial(a^{[k]})=a^{[k+1]}$ y su intervalo abierto es el mismo $I$. En consecuencia, **sin cambiar de dominio**,

$$
\boxed{F_k'(x)=F_{k+1}(x)\qquad(x\in I).}
\tag{24.8.8}
$$

Para $k=0$, (24.8.5) coincide con $F_{a,c}\upharpoonright I$. Induciendo sobre $k$ en (24.8.8), las derivadas funcionales sucesivas de $F_0$ existen en todo $I$ y coinciden con la función ya construida $F_k$. Finalmente la serie que define $F_k$ tiene coeficientes $a^{[k]}_n$, cuya expresión factorial es (24.8.2); sustituirla prueba (24.8.6). En particular, **para cada orden**, se aplica un teorema ya probado a datos dados, y nunca se deriva una serie por un intercambio ilimitado de límites. $\square$

**Lectura matemática.** Hemos probado más que la existencia de $F_0'$: todas las derivadas existen, son continuas en $I$ (cada una es suma de una serie de potencias con radio positivo) y tienen una expansión explícita. Este hecho no afirma todavía que una función real cualquiera con derivadas de todos los órdenes coincida con su serie de Taylor.

### Corolario 24.8.4 — Recuperación de cada coeficiente mediante la derivada en el centro
Bajo las hipótesis de «Derivadas de todo orden y conservación del radio», todos los coeficientes de la serie original están determinados por la función suma en un entorno del centro:

$$
\boxed{F_0^{(k)}(c)=\eta_k a_k,
\qquad a_k=\frac{F_0^{(k)}(c)}{\eta_k}
\quad(k\in\mathbb N).}
\tag{24.8.9}
$$

**Demostración.**
El centro $c$ pertenece al abierto $I$. Por el teorema anterior, $F_0^{(k)}=F_k$ en ese dominio; por la evaluación en el centro de una serie de potencias («El centro siempre pertenece al conjunto de convergencia»), $F_k(c)=a^{[k]}_0$. La fórmula factorial (24.8.3) da $a^{[k]}_0=\eta_k a_k$. El denominador $\eta_k$ es estrictamente positivo por «Positividad y recurrencia de los factoriales», de modo que dividir por él es legítimo y produce la segunda igualdad. Para $k=0$, $\eta_0=1$, y se recupera $F_0(c)=a_0$. $\square$

### Teorema 24.8.5 — Unicidad de una expansión en potencias alrededor del mismo centro
Sean $a,b:\mathbb N\to\mathbb R$ sucesiones reales y $c\in\mathbb R$ un centro **común**. Supongamos que ambas series poseen radio estrictamente positivo o infinito y que existe un real $\delta>0$ tal que el intervalo $U:=(c-\delta,c+\delta)$ está contenido en los dos interiores radiales y

$$
F_{a,c}(x)=F_{b,c}(x)\qquad(x\in U).
\tag{24.8.10}
$$

Entonces los coeficientes coinciden en **todos** los índices:

$$
\boxed{a=b:\mathbb N\longrightarrow\mathbb R,\qquad
 a_k=b_k\ (k\in\mathbb N).}
\tag{24.8.11}
$$

La conclusión exige identidad de centro y coincidencia en un entorno abierto; no exige que los radios o los conjuntos de convergencia completos sean idénticos *a priori*. Recíprocamente, si $a=b$ y el centro es el mismo, las sumas parciales son idénticas en toda $\mathbb R$, y las funciones suma coinciden en su dominio exacto común.

**Demostración.**
Sean $I_a,I_b$ los interiores radiales; $U$ es un abierto contenido en ambos y contiene $c$. Definamos las restricciones tipadas $f:=F_{a,c}\upharpoonright U$ y $g:=F_{b,c}\upharpoonright U$. La hipótesis (24.8.10) y «Criterio de igualdad de funciones» dan $f=g$ como funciones con dominio y codominio comunes. Por «Derivadas de todo orden y conservación del radio», tanto $f$ como $g$ son derivables de todo orden en $U$: para cada punto de $U$ existe un entorno contenido en $U$ en que sus cocientes incrementales coinciden con los de las funciones sumas sobre $I_a$ e $I_b$; por inducción, la misma observación vale para las derivadas sucesivas. Derivar la igualdad $f=g$ produce, por unicidad del límite de cada cociente incremental, $f'=g'$; la inducción da

$$
f^{(k)}(x)=g^{(k)}(x)
\qquad(k\in\mathbb N,\ x\in U).
\tag{24.8.12}
$$

En el centro $c\in U$ esas derivadas coinciden con las de las sumas sobre sus interiores respectivos. El corolario anterior aplicado a cada serie da $\eta_k a_k=f^{(k)}(c)=g^{(k)}(c)=\eta_k b_k$. Como $\eta_k>0$, cancelar el mismo factor implica $a_k=b_k$. El índice $k$ era arbitrario, por lo que las sucesiones coinciden punto por punto y, al compartir dominio $\mathbb N$ y codominio $\mathbb R$, son la misma función. Para la recíproca, cada sumando y cada suma parcial coinciden por igualdad de los datos; por definición también coinciden los predicados de convergencia y, cuando ésta ocurre, el único límite. No se compara una derivada en extremos ni se importa el principio de identidad de funciones analíticas complejas. $\square$

**Por qué importa el entorno.** Una coincidencia *sólo* en $x=c$ no determina más que $a_0=b_0$: las series con coeficientes $a_n=0$ para todo $n$ y $b_0=0$, $b_1=1$, $b_n=0$ para $n\ge2$ representan respectivamente las funciones $0$ y $x-c$; ambas tienen radio infinito y ambas valen cero en $c$, pero $a_1\ne b_1$. La unicidad anterior tampoco compara coeficientes de desarrollos centrados en **puntos diferentes**.

### Proposición 24.8.6 — Los polinomios de Taylor finitos de una suma de potencias son sus sumas parciales
Supongamos, como en el teorema 24.8.3, que la serie tiene radio positivo o infinito. Para cada $N\in\mathbb N$, el polinomio de Taylor finito de orden $N$ de $F_0$ en el centro $c$, en el sentido de «Polinomio de Taylor finito en un centro», está bien definido sobre cualquier cerrado interior $K_r$ **no degenerado** y coincide, como función polinómica sobre $\mathbb R$, con la suma parcial original:

$$
\boxed{P_{N,c}(x)=\sum_{k=0}^{N}\frac{F_0^{(k)}(c)}{\eta_k}(x-c)^k
=\sum_{k=0}^{N}a_k(x-c)^k=S_N^{a,c}(x).}
\tag{24.8.13}
$$

**Demostración.**
Como el radio es positivo o infinito, existe un $r>0$ admisible: en el caso finito $r:=R(a,c)/2$; en el infinito, $r:=1$. Entonces $K_r=[c-r,c+r]\subseteq I$, es un intervalo cerrado no degenerado y contiene $c$. Para cada $0\le k\le N$ restringimos la función **ya determinada** $F_k$ del teorema 24.8.3 a $K_r$. Es continua en todo $K_r$ por «Continuidad de la función suma en el interior» aplicado a la serie $a^{[k]}$, y satisface $F_k'=F_{k+1}$ en su interior por (24.8.8) cuando $k<N$. Las restricciones $F_0\upharpoonright K_r,\ldots,F_N\upharpoonright K_r$ forman una cadena diferencial finita de orden $N$ en el sentido de «Cadena diferencial finita sobre un intervalo cerrado»; se define por restricción única para un conjunto **finito** de índices, sin elegir funciones.

Por «Polinomio de Taylor finito en un centro», su polinomio de Taylor es la primera suma de (24.8.13). La recuperación (24.8.9) prueba que cada coeficiente de esa suma es exactamente $a_k$. La construcción de las sumas parciales en «Construcción tipada de los términos y las sumas parciales» identifica el resultado con $S_N^{a,c}$ sobre toda la recta, pues ambas expresiones polinómicas definen el mismo valor para cada real. Hemos establecido una igualdad **finita**; la identificación de la serie de Taylor infinita con una función arbitraria deberá justificarse con el comportamiento de los restos, no sólo mediante la existencia de las derivadas. $\square$

**Balance y transición.** Los coeficientes iterados están construidos mediante recursión única; para todo orden la serie correspondiente conserva el radio y representa la derivada funcional legítima en el interior. Los datos diferenciales en el centro recuperan los coeficientes de manera inequívoca, y dos series centradas en el mismo punto no pueden representar una misma función en un entorno abierto con coeficientes distintos. En el caso de una **función ya representada** por una serie de potencias, sus polinomios de Taylor finitos son las sumas parciales; resta distinguir este hecho de la pregunta inversa: ¿cuándo una función $C^{\infty}$ dada coincide con la serie construida a partir de sus derivadas? Ésta será la materia de §24.9, mediante restos y un contraejemplo pertinente. La parte fundacional sigue en ZF + lógica clásica, sin Choice; no se abre un nuevo checkpoint Lean.

---
