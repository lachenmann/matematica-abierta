## 22.3. Primitivas y regla de Newton–Leibniz {#sec-ta-22-3}

La primera parte del teorema construyó una primitiva de cada integranda continua, aunque todavía no le habíamos dado ese nombre. El problema inverso admite un enunciado más amplio: si conocemos una función cuya derivada interior coincide con una integranda **ya integrable**, ¿podemos recuperar la integral a partir de sus valores extremos? Debemos separar las condiciones: la mera existencia de una primitiva no proporciona, por sí sola, la integrabilidad de su derivada. Asimismo, la continuidad de la primitiva en los extremos es indispensable para aplicar el teorema del valor medio allí.

### Definición 22.3.1 — Primitiva sobre un intervalo cerrado
Sean $a<b$ y $f:[a,b]\to\mathbb R$. Llamaremos **primitiva de $f$ en $[a,b]$** a una función $H:[a,b]\to\mathbb R$ que cumpla conjuntamente:

1. $H$ es continua en **cada** punto de $[a,b]$, con la topología relativa del dominio;
2. $H$ es derivable en cada $x\in(a,b)$ y $H'(x)=f(x)$.

La igualdad de derivadas se exige solamente en el interior. Los valores $f(a)$ y $f(b)$ no se recuperan de derivadas bilaterales inexistentes en los extremos. Tampoco incluimos la integrabilidad de $f$ en esta definición: será una hipótesis separada cuando usemos el símbolo $\int_a^b f$.

### Lema 22.3.2 — El incremento de una primitiva queda encerrado entre las sumas de Darboux
Sea $f:[a,b]\to\mathbb R$ **acotada**, sin suponer todavía su integrabilidad, y sea $H$ una primitiva suya. Para toda partición $P\in\operatorname{Part}[a,b]$ se cumple

$$
\boxed{L(f,P)\le H(b)-H(a)\le U(f,P).}
\tag{22.3.1}
$$

**Demostración.**
Fijemos una partición $P=\langle n,p\rangle$ y usemos la notación ya definida $x_k:=p(k)$, $\Delta_k:=x_{k+1}-x_k>0$ e $I_k:=[x_k,x_{k+1}]$ para $k<n$. Los extremos locales $m_k:=\inf f[I_k]$ y $M_k:=\sup f[I_k]$ existen por acotación y por la no vacuidad de $I_k$ (Lema §21.2.2 — Existencia de las cotas extremas locales y comparación por inclusión). Por definición,

$$
 m_k\le f(t)\le M_k\qquad(t\in I_k).
\tag{22.3.2}
$$

Consideremos un índice **arbitrario y fijo** $k<n$. La continuidad de $H$ en todo el dominio contiene la continuidad relativa en $I_k$; su derivabilidad interior contiene la derivabilidad en $(x_k,x_{k+1})$. Por el valor medio en subintervalos Corolario §20.3.3 — Valor medio en un subintervalo del dominio original, existe $c\in(x_k,x_{k+1})$ con

$$
 H(x_{k+1})-H(x_k)=H'(c)\Delta_k=f(c)\Delta_k.
$$

Como $c\in I_k$, (22.3.2), multiplicada por $\Delta_k>0$, demuestra

$$
 m_k\Delta_k\le H(x_{k+1})-H(x_k)\le M_k\Delta_k.
\tag{22.3.3}
$$

El punto $c$ ya no aparece en (22.3.3). Por tanto, **para cada índice $k<n$ hemos probado directamente una proposición universal**, sin formar una función $k\mapsto c_k$ ni elegir testigos de manera simultánea. La monotonía de las sumas finitas, demostrable por inducción a partir de las propiedades del orden real y de Proposición §14.2.2 — Identidades de los bloques de sumación, permite sumar (22.3.3):

$$
 \sum_{k=0}^{n-1}m_k\Delta_k
 \le\sum_{k=0}^{n-1}\bigl(H(x_{k+1})-H(x_k)\bigr)
 \le\sum_{k=0}^{n-1}M_k\Delta_k.
$$

La suma central es telescópica: por asociatividad y cancelación de términos adyacentes, o por inducción sobre el número finito de subintervalos, vale $H(x_n)-H(x_0)=H(b)-H(a)$. Las sumas externas son precisamente $L(f,P)$ y $U(f,P)$ según Definición §21.2.4 — Sumas inferior y superior de Darboux. Resulta (22.3.1). $\square$

**Lectura.** El teorema del valor medio entrega un testigo por intervalo, pero la prueba sólo retiene desigualdades que no dependen del testigo. El encierro tiene sentido incluso antes de conocer si $f$ es integrable.

### Teorema 22.3.3 — Regla de Newton–Leibniz para integrandas integrables que admiten primitiva
Sean $a<b$, sea $f:[a,b]\to\mathbb R$ **integrable** y sea $H:[a,b]\to\mathbb R$ una primitiva de $f$ en el sentido de Definición §22.3.1 — Primitiva sobre un intervalo cerrado. Entonces

$$
\boxed{\int_a^b f(t)\,dt=H(b)-H(a).}
\tag{22.3.4}
$$

No se exige que $f$ sea continua: bastan su integrabilidad, la continuidad de $H$ en el cerrado y la identidad $H'=f$ en el interior.

**Demostración.**
La integrabilidad de $f$ incorpora su acotación y legitima las sumas de Darboux. Escribamos $D:=H(b)-H(a)$. El lema Lema §22.3.2 — El incremento de una primitiva queda encerrado entre las sumas de Darboux asegura que, **para toda** partición $P$,

$$
 L(f,P)\le D\le U(f,P).
$$

Por consiguiente, $D$ es una cota superior del conjunto no vacío de las sumas inferiores y una cota inferior del conjunto no vacío de las sumas superiores. Los extremos de estos conjuntos ya existen por Proposición §21.3.4 — Orden y encierro de las integrales extremas y están definidos en Definición §21.3.3 — Integrales inferior y superior de Darboux; sus propiedades características dan

$$
 \underline{\int_a^b}f\le D\le\overline{\int_a^b}f.
\tag{22.3.5}
$$

La integrabilidad significa, exactamente, que los dos extremos coinciden. Su valor común es $\int_a^b f$ por Definición §21.4.3 — Integral de Riemann–Darboux para funciones integrables. Así (22.3.5) se convierte en $\int_a^b f\le D\le\int_a^b f$. La antisimetría del orden real obliga a $D=\int_a^b f$, que prueba (22.3.4). No usamos Teorema §22.2.2 — Primera parte del teorema fundamental del cálculo: continuidad puntual: el resultado no depende de la continuidad de $f$ en ninguno de sus puntos. $\square$

### Proposición 22.3.4 — Dos primitivas difieren en una constante
Si $H,K:[a,b]\to\mathbb R$ son primitivas de una misma función $f:[a,b]\to\mathbb R$, existe un único real $C$ tal que

$$
\boxed{H(x)=K(x)+C\quad\text{para todo }x\in[a,b].}
\tag{22.3.6}
$$

Recíprocamente, para cada $C\in\mathbb R$ la función tipada $x\mapsto K(x)+C$ también es primitiva de $f$.

**Demostración.**
Por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales existe la función diferencia $G:=H-K:[a,b]\to\mathbb R$. Es continua en todo el intervalo por la estabilidad algebraica de la continuidad (Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto). Las reglas de derivación de las diferencias (Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias) garantizan, para todo $x\in(a,b)$,

$$
 G'(x)=H'(x)-K'(x)=f(x)-f(x)=0.
$$

El corolario Corolario §20.5.4 — Derivada idénticamente nula si y sólo si la función es constante afirma entonces que $G$ es constante **también en los extremos**. Definimos el real determinado $C:=G(a)=H(a)-K(a)$; así $G(x)=C$ para cada $x$, lo que equivale a (22.3.6). Si $C'$ verificase la misma fórmula, evaluar en $a$ daría $C'=H(a)-K(a)=C$.

Para la recíproca, fijemos un real $C$ y construyamos la función $J(x):=K(x)+C$, mediante operaciones puntuales tipadas. Es continua en $[a,b]$ por Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto y derivable en el interior con $J'(x)=K'(x)+0=f(x)$ por Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias. Cumple, pues, ambas cláusulas de la definición de primitiva. $\square$

### Corolario 22.3.5 — Existencia de primitivas para integrandas continuas y fórmula clásica
Si $f:[a,b]\to\mathbb R$ es continua en todo $[a,b]$, entonces admite una primitiva $F_{f,a}$ en el sentido anterior. Además, para **cualquier** primitiva $H$ de $f$,

$$
\boxed{\int_a^b f=F_{f,a}(b)=H(b)-H(a).}
\tag{22.3.7}
$$

Todas las primitivas se obtienen de la acumulada sumándole una constante real; en particular, $F_{f,a}$ es la única primitiva que se anula en $a$.

**Demostración.**
Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable establece que $f$ es integrable; por tanto la función $F_{f,a}:[a,b]\to\mathbb R$ está definida. Teorema §22.1.4 — Acotación global, condición de Lipschitz y continuidad uniforme prueba su continuidad uniforme en el cerrado, y Corolario §22.2.3 — Integranda continua sobre todo el intervalo prueba su derivabilidad y la identidad $F_{f,a}'=f$ en el interior. Satisface, pues, las dos condiciones de Definición §22.3.1 — Primitiva sobre un intervalo cerrado. Si $H$ es otra primitiva, el teorema Teorema §22.3.3 — Regla de Newton–Leibniz para integrandas integrables que admiten primitiva se aplica a $H$ y da la primera igualdad de (22.3.7), mientras que Proposición §22.1.2 — Valores extremos e identidad exacta de los incrementos da $F_{f,a}(b)=\int_a^b f$. Por Proposición §22.3.4 — Dos primitivas difieren en una constante, $H=F_{f,a}+C$ con $C=H(a)-F_{f,a}(a)=H(a)$, ya que $F_{f,a}(a)=0$. En particular, $H(a)=0$ equivale a $C=0$, luego $H=F_{f,a}$ como funciones tipadas. $\square$

### Corolario 22.3.6 — Newton–Leibniz en cualquier subintervalo ordenado
Supongamos $f:[a,b]\to\mathbb R$ integrable y $H:[a,b]\to\mathbb R$ primitiva suya. Entonces, para cualesquiera $a\le u\le v\le b$,

$$
\boxed{\int_u^v(f\upharpoonright[u,v])=H(v)-H(u).}
\tag{22.3.8}
$$

**Demostración.**
Si $u=v$, la integral de la restricción tipada al singleton es $0$ por Definición §21.6.5 — Integración en un intervalo degenerado y $H(v)-H(u)=0$ por igualdad de argumentos. Supongamos $u<v$. La integrabilidad de $g:=f\upharpoonright[u,v]:[u,v]\to\mathbb R$ se deduce de Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado. La función $J:=H\upharpoonright[u,v]$ es continua en el cerrado por Corolario §17.4.6 — Clausura global, restricciones y cocientes y derivable en cada punto interior por Proposición §19.5.2 — Restricción de una función derivable, con $J'(x)=H'(x)=f(x)=g(x)$. Luego $J$ es primitiva de $g$, y Teorema §22.3.3 — Regla de Newton–Leibniz para integrandas integrables que admiten primitiva proporciona $\int_u^v g=J(v)-J(u)=H(v)-H(u)$. Sólo se usan extremos ordenados; no queda introducida una integral con $u>v$. $\square$

**Síntesis deductiva.** La continuidad global de la integranda proporciona integrabilidad y una primitiva concreta (§§21.7 y 22.2); la integrabilidad más una primitiva ya existente proporciona Newton–Leibniz sin exigir continuidad de la integranda (§22.3). La regla de Newton–Leibniz no es una definición alternativa de integral ni sustituye su construcción por Darboux.

**Nota de fuentes.** Jacob y Evans, *A Course in Analysis*, vol. I, cap. 26, es una referencia de contraste para la articulación de las dos partes del teorema fundamental, conforme al cotejo bibliográfico registrado en §§22.1–22.2. La demostración de (22.3.4) es interna al tratado, por encierro Darboux–Lagrange, y no importa una prueba ajena.

**Transición.** La regla de Newton–Leibniz convierte el conocimiento de una primitiva en un cálculo de valores extremos. En la siguiente unidad combinaremos esta relación con la regla de derivación de un producto para deducir rigurosamente la integración por partes, verificando por separado que todas las integrandas estén integradas legítimamente.
