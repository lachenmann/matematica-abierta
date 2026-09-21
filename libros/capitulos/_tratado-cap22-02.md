## 22.2. Primera parte del teorema fundamental del cálculo {#sec-ta-22-2}

Una función integrable puede ser discontinua; aun así, su acumulada es continua (§22.1). La afirmación que ahora buscamos es distinta: en cada punto interior donde la integranda sí sea continua, la acumulada resulta derivable y su derivada recupera el valor de la integranda en ese punto. Separaremos una estimación algebraica que vale sin continuidad del argumento de límite que utiliza esa hipótesis.

### Lema 22.2.1 — Estimación del cociente incremental por la oscilación alrededor de un valor
Sea $f:[a,b]\to\mathbb R$ integrable y sea $F:=F_{f,a}$. Fijemos $x,y\in[a,b]$ con $x\ne y$ y $\eta\ge0$. Supongamos que

$$
|f(t)-f(x)|\le\eta
\qquad\text{para todo }t\text{ comprendido entre }x\text{ e }y,
\tag{22.2.1}
$$

incluidos ambos extremos. Entonces el cociente está bien definido y satisface

$$
\boxed{\left|\frac{F(y)-F(x)}{y-x}-f(x)\right|\le\eta.}
\tag{22.2.2}
$$

**Demostración.**
La hipótesis equivale, por la definición de valor absoluto, a

$$
f(x)-\eta\le f(t)\le f(x)+\eta
\tag{22.2.3}
$$

sobre el subintervalo cuyos extremos son $x,y$. Si $x<y$, aplicamos (22.1.5) a $[x,y]$ con las cotas constantes $m=f(x)-\eta$ y $M=f(x)+\eta$; como $y-x>0$, obtenemos

$$
f(x)-\eta\le\frac{F(y)-F(x)}{y-x}\le f(x)+\eta.
\tag{22.2.4}
$$

Si $y<x$, aplicamos la misma estimación, pero al intervalo legítimo $[y,x]$. Al dividir por $x-y>0$ se obtiene

$$
f(x)-\eta\le\frac{F(x)-F(y)}{x-y}\le f(x)+\eta.
$$

La identidad algebraica

$$
\frac{F(x)-F(y)}{x-y}=\frac{F(y)-F(x)}{y-x}
$$

transforma esta última desigualdad en (22.2.4). En ninguno de los casos escribimos una integral con extremos invertidos; sólo se cambian de signo numerador y denominador de un cociente de reales. Finalmente, (22.2.4) equivale a (22.2.2). $\square$

**Lectura del lema.** No hay aquí un punto escogido donde la función alcance un máximo ni una aplicación del teorema del valor medio integral. Basta una cota puntual uniforme sobre el tramo que une los dos argumentos; la cota del cociente es igualmente válida a derecha e izquierda.

### Teorema 22.2.2 — Primera parte del teorema fundamental del cálculo: continuidad puntual
Sean $a<b$, $f:[a,b]\to\mathbb R$ integrable y $x\in(a,b)$. Si $f$ es continua en $x$ relativamente a $[a,b]$, entonces la función acumulada $F_{f,a}:[a,b]\to\mathbb R$ es derivable en $x$ y

$$
\boxed{F_{f,a}'(x)=f(x).}
\tag{22.2.5}
$$

**Demostración.**
Escribamos $F:=F_{f,a}$. Primero verificamos el dominio de la derivada. Puesto que $a<x<b$, para cada $r>0$ el número

$$
s_r:=\frac12\min\{r,x-a,b-x\}>0
$$

satisface $x-s_r,x+s_r\in[a,b]$ y $0<|x\pm s_r-x|=s_r<r$. Así $x\in\operatorname{Acc}([a,b])$; ambos lados acumulan en $x$. El cociente incremental de Definición §19.1.1 — Cociente incremental en un punto está por tanto definido en $[a,b]\setminus\{x\}$ y tiene un dominio que acumula en $x$, como exige Definición §19.1.3 — Derivabilidad en un punto.

Fijemos ahora una tolerancia arbitraria $\varepsilon>0$. La continuidad de $f$ en $x$ (Definición §17.1.1 — Continuidad relativa al dominio en un punto), aplicada a $\varepsilon/2$, suministra un único radio testigo para esta tolerancia $\rho>0$ tal que

$$
t\in[a,b],\quad |t-x|<\rho
\quad\Longrightarrow\quad
|f(t)-f(x)|<\frac\varepsilon2.
\tag{22.2.6}
$$

Definamos, sin efectuar ninguna elección adicional,

$$
\delta:=\min\left\{\rho,\frac{x-a}{2},\frac{b-x}{2}\right\}>0.
\tag{22.2.7}
$$

Consideremos cualquier $y\in[a,b]$ con $0<|y-x|<\delta$. Si $y>x$, cada $t\in[x,y]$ cumple $|t-x|\le y-x=|y-x|<\delta\le\rho$. Si $y<x$, para cada $t\in[y,x]$ se cumple $|t-x|\le x-y=|y-x|<\delta\le\rho$. En ambos casos (22.2.6) proporciona, sobre todo el intervalo comprendido entre $x$ e $y$,

$$
|f(t)-f(x)|<\frac\varepsilon2
\quad\Longrightarrow\quad
|f(t)-f(x)|\le\frac\varepsilon2.
$$

El lema Lema §22.2.1 — Estimación del cociente incremental por la oscilación alrededor de un valor, con $\eta=\varepsilon/2$, da entonces

$$
\left|\frac{F(y)-F(x)}{y-x}-f(x)\right|
\le\frac\varepsilon2<\varepsilon.
\tag{22.2.8}
$$

El mismo $\delta$ funciona para todos los argumentos admisibles, tanto por la izquierda como por la derecha. Ésta es exactamente la condición cuantificada de derivabilidad Definición §19.1.3 — Derivabilidad en un punto con candidato $L=f(x)$. La unicidad Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada legitima la notación puntual Notación §19.1.5 — Valor de la derivada y demuestra (22.2.5). No se aplicaron Rolle, el valor medio diferencial, un teorema del valor medio integral, sucesiones de puntos escogidos ni ninguna forma de Choice. $\square$

**Interpretación.** La integral recoge incrementos globales y la derivada examina el comportamiento infinitesimal de esos incrementos. La continuidad en $x$ obliga a que todos los valores de $f$ en un tramo suficientemente corto estén próximos a $f(x)$; por ello también lo está su promedio integral. La continuidad exigida es puntual, no una condición global adicional.

### Corolario 22.2.3 — Integranda continua sobre todo el intervalo
Si $f:[a,b]\to\mathbb R$ es continua en todos los puntos de $[a,b]$, entonces es integrable y su función acumulada está definida en todo $[a,b]$. Además,

$$
\boxed{F_{f,a}'(x)=f(x)\qquad\text{para cada }x\in(a,b).}
\tag{22.2.9}
$$

**Demostración.**
La continuidad en el intervalo cerrado implica integrabilidad por Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable, de modo que Definición §22.1.1 — Función integral acumulada construye $F_{f,a}$ con dominio y codominio explícitos. Tomemos ahora un $x\in(a,b)$ arbitrario. La hipótesis de continuidad global incluye la continuidad relativa de $f$ en ese $x$, por lo que Teorema §22.2.2 — Primera parte del teorema fundamental del cálculo: continuidad puntual proporciona su derivabilidad y (22.2.9). La cuantificación universal sobre los puntos interiores concluye la prueba. No hemos afirmado una derivada bilateral en $a$ o $b$. $\square$

### Proposición 22.2.4 — Necesidad de una hipótesis local: el escalón y su acumulada
Sea $a<c<b$ y retomemos la función escalón $s_c:[a,b]\to\mathbb R$ construida en (21.8.8): vale cero en $[a,c)$ y uno en $[c,b]$. Es integrable, pero discontinua en $c$ (Proposición §21.8.4 — Ejemplo explícito: una función monótona integrable con un salto). Su función acumulada es

$$
\boxed{F_{s_c,a}(x)=
\begin{cases}
0, &a\le x\le c,\\
x-c,&c\le x\le b.
\end{cases}}
\tag{22.2.10}
$$

Las dos fórmulas coinciden en $x=c$. Esta acumulada es continua en todo $[a,b]$ por §22.1, pero no es derivable en $c$.

**Demostración.**
Si $a\le x<c$, la restricción de $s_c$ a $[a,x]$ es la función constante cero y Proposición §21.5.1 — Acotación de las operaciones y cálculo de las constantes da $F_{s_c,a}(x)=0$ (si $x=a$, vale además la definición de intervalo degenerado). Para $x=c$, la identidad de incremento Proposición §22.1.2 — Valores extremos e identidad exacta de los incrementos y la aditividad sobre el punto $c$ producen

$$
\int_a^b s_c=F_{s_c,a}(c)+\int_c^b(s_c\upharpoonright[c,b]).
$$

La integral de la izquierda vale $b-c$ por Proposición §21.8.5 — Cálculo directo de la integral de la función escalón; la restricción de la derecha es la constante uno y tiene integral $b-c$ por Proposición §21.5.1 — Acotación de las operaciones y cálculo de las constantes. En consecuencia, $F_{s_c,a}(c)=0$. Para $c<x\le b$, la identidad de incrementos en $[c,x]$, donde $s_c$ es constante uno, da

$$
F_{s_c,a}(x)-F_{s_c,a}(c)
=\int_c^x(s_c\upharpoonright[c,x])=x-c.
$$

Esto demuestra (22.2.10), sin atribuir longitud positiva al singleton $\{c\}$.

Para $y<c$ y $y>c$, respectivamente, los cocientes incrementales de esta misma función en $c$ son

$$
\frac{F_{s_c,a}(y)-F_{s_c,a}(c)}{y-c}=0,
\qquad
\frac{F_{s_c,a}(y)-F_{s_c,a}(c)}{y-c}=1.
\tag{22.2.11}
$$

Supongamos que existe una derivada $L$ en $c$. La condición cuantificada de Definición §19.1.3 — Derivabilidad en un punto con tolerancia $\varepsilon=1/3$ produce $\delta>0$ tal que todo argumento distinto de $c$ a distancia menor que $\delta$ tiene su cociente a distancia estrictamente menor que $1/3$ de $L$. Pero el real

$$
r:=\frac12\min\{\delta,c-a,b-c\}>0
$$

determina los dos puntos admisibles $c-r$ y $c+r$, ambos a distancia $r<\delta$ de $c$. Por (22.2.11), tendríamos simultáneamente $|L|<1/3$ y $|1-L|<1/3$. La desigualdad triangular de Teorema §4.2.3 — Desigualdad triangular implicaría

$$
1=|L+(1-L)|\le|L|+|1-L|<2/3<1,
$$

contradicción. La derivada en $c$ no existe. El fracaso no contradice el teorema anterior: precisamente en ese punto $s_c$ no es continua. $\square$

**Nota de contraste bibliográfico.** Jacob y Evans, *A Course in Analysis*, vol. I, cap. 26, teorema 26.1, p. 369, presentan el vínculo para integrandas continuas sobre el intervalo. Nuestra formulación puntual separa la hipótesis necesaria para cada punto de derivación de la hipótesis global más fuerte del corolario. El ejemplar y la localización ya fueron cotejados y registrados en el control de §22.1; esta unidad no importa ni reproduce una demostración externa.

**Transición.** Hemos obtenido una función cuya derivada recupera la integranda donde ésta es continua, y hemos comprobado qué puede fallar en un salto. A continuación estudiaremos las *primitivas* y estableceremos la regla de Newton–Leibniz, cuidando que la existencia de una primitiva y las condiciones de continuidad o integrabilidad se enuncien por separado.
