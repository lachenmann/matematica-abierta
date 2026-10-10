## 22.6. Consecuencias estructurales: normalización, linealidad y determinación {#sec-ta-22-6}

La integral definida y las primitivas no son dos nombres para un mismo objeto. La primera es un número asociado a una función integrable y a un intervalo ordenado; una primitiva, cuando existe, es una función determinada sólo hasta una constante. La acumulación permite relacionarlas fijando el valor en el extremo inicial. Esta última unidad estudia tres propiedades de esa construcción —normalización, linealidad y cambio de origen— y precisa en qué sentido recupera la integranda.

Fijaremos de nuevo $a<b$. Todas las funciones de esta sección tienen dominios y codominios explícitos; el símbolo $F_{f,a}$ conserva la definición de §22.1. La afirmación de que una función integrable tiene *una acumulada* no se confundirá con la afirmación, en general falsa, de que toda acumulada sea una primitiva de su integranda.

### Proposición 22.6.1 — Reconstrucción de la acumulada desde cualquier primitiva
Sea $f:[a,b]\to\mathbb R$ integrable y supongamos que se ha dado una primitiva $H:[a,b]\to\mathbb R$ de $f$. Entonces, para todo $x\in[a,b]$,

$$
\boxed{F_{f,a}(x)=H(x)-H(a).}
\tag{22.6.1}
$$

En particular, $F_{f,a}$ es una primitiva de $f$ y es la única que se anula en $a$. No se afirma la existencia de una primitiva cuando solamente se conoce la integrabilidad de $f$.

**Demostración.**
Sea $x\in[a,b]$ arbitrario. Por Corolario §22.3.6 — Newton–Leibniz en cualquier subintervalo ordenado, aplicada al intervalo ordenado $[a,x]$, la restricción tipada de $f$ es integrable y

$$
\int_a^x(f\upharpoonright[a,x])=H(x)-H(a).
$$

El miembro izquierdo es precisamente $F_{f,a}(x)$ por Definición §22.1.1 — Función integral acumulada; cuando $x=a$ vale cero conforme a Definición §21.6.5 — Integración en un intervalo degenerado, coincidiendo con la diferencia de valores. Esto demuestra (22.6.1) para cada argumento y, por igualdad de dominio, codominio y grafo (Proposición §0.6.3 — Criterio de igualdad de funciones), determina la función completa. Como $H$ es primitiva, la recíproca de Proposición §22.3.4 — Dos primitivas difieren en una constante demuestra que restarle la constante $H(a)$ conserva esa propiedad. La nueva función se anula en $a$; si $K$ fuera otra primitiva con $K(a)=0$, la diferencia entre $K$ y $F_{f,a}$ sería la constante $K(a)-F_{f,a}(a)=0$, de nuevo por Proposición §22.3.4 — Dos primitivas difieren en una constante. Por tanto $K=F_{f,a}$. No seleccionamos una primitiva de cada función: trabajamos con la única $H$ suministrada como hipótesis. $\square$

**Lectura.** Newton–Leibniz permite calcular la acumulada utilizando una primitiva *ya conocida*; la normalización fija la ambigüedad aditiva. La existencia de una primitiva para cualquier integranda continua es el resultado anterior Corolario §22.3.5 — Existencia de primitivas para integrandas continuas y fórmula clásica, no una consecuencia de la mera integrabilidad.

### Teorema 22.6.2 — Linealidad de la acumulación para funciones integrables
Sean $f,g:[a,b]\to\mathbb R$ integrables y $\alpha,\beta\in\mathbb R$. La combinación puntual tipada

$$
h:[a,b]\longrightarrow\mathbb R,\qquad h(t):=\alpha f(t)+\beta g(t)
$$

es integrable y sus acumuladas satisfacen la identidad de funciones

$$
\boxed{F_{h,a}=\alpha F_{f,a}+\beta F_{g,a}.}
\tag{22.6.2}
$$

El miembro derecho designa la función $[a,b]\to\mathbb R$ definida punto a punto por la combinación indicada; ninguna de las tres funciones tiene por qué ser primitiva de su integranda.

**Demostración.**
La construcción puntual de $h$ es legítima por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales, y su integrabilidad procede de Corolario §21.5.7 — Linealidad para combinaciones finitas de dos funciones. En consecuencia las tres acumuladas están definidas por Definición §22.1.1 — Función integral acumulada y son funciones tipadas $[a,b]\to\mathbb R$. Fijemos $x\in[a,b]$. Si $x=a$, las tres acumuladas valen cero por la convención Definición §21.6.5 — Integración en un intervalo degenerado, así que (22.6.2) se verifica en ese argumento.

Si $a<x\le b$, Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado garantiza previamente que las restricciones de $f$, $g$ y $h$ a $[a,x]$ son integrables. La restricción de $h$ coincide como función tipada con $\alpha(f\upharpoonright[a,x])+\beta(g\upharpoonright[a,x])$, por coincidencia de dominio, codominio y valores (Proposición §1.3.2 — Existencia y unicidad de la restricción). La linealidad de la integral, aplicada ahora sobre el intervalo no degenerado $[a,x]$, da

$$
\begin{aligned}
F_{h,a}(x)
&=\int_a^x(h\upharpoonright[a,x])\\
&=\alpha\int_a^x(f\upharpoonright[a,x])
 +\beta\int_a^x(g\upharpoonright[a,x])\\
&=\alpha F_{f,a}(x)+\beta F_{g,a}(x).
\end{aligned}
$$

Todos los argumentos de $[a,b]$ quedan cubiertos. La igualdad puntual y la igualdad de tipos prueban (22.6.2) por Proposición §0.6.3 — Criterio de igualdad de funciones. No se dedujo la integrabilidad de una suma a partir de una fórmula escrita anticipadamente, ni se eligió una familia de particiones para todos los valores de $x$. $\square$

**Interpretación.** La integración sobre un intervalo fijo era lineal (§21.5). La acumulación hereda esa estructura *simultáneamente en todos sus extremos superiores* porque la igualdad de integrales se aplica a cada restricción ya legitimada.

### Proposición 22.6.3 — Cambio del origen de acumulación
Sea $f:[a,b]\to\mathbb R$ integrable y sea $c\in[a,b)$ un nuevo origen. La restricción $f_c:=f\upharpoonright[c,b]:[c,b]\to\mathbb R$ es integrable. Para todo $x\in[c,b]$ se tiene

$$
\boxed{F_{f_c,c}(x)=F_{f,a}(x)-F_{f,a}(c).}
\tag{22.6.3}
$$

La condición $c<b$ garantiza que la definición de acumulada de §22.1 se aplica a $f_c$; el argumento variable $x=c$ sí está permitido y su integral es la de un singleton.

**Demostración.**
Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado, aplicado al corte $c$, asegura que $f_c$ es integrable, de modo que $F_{f_c,c}$ existe por Definición §22.1.1 — Función integral acumulada. Sean $c\le x\le b$. La identidad exacta de incrementos Proposición §22.1.2 — Valores extremos e identidad exacta de los incrementos, aplicada a la acumulada original y a los dos extremos ordenados $c,x$, proporciona

$$
F_{f,a}(x)-F_{f,a}(c)
=\int_c^x(f\upharpoonright[c,x]).
$$

Las restricciones sucesivas dan la misma función tipada $f_c\upharpoonright[c,x]=f\upharpoonright[c,x]$ (Proposición §1.3.2 — Existencia y unicidad de la restricción), y la integral de ésta es, por definición, $F_{f_c,c}(x)$. Si $x=c$, la igualdad afirma $0=0$ y se apoya exclusivamente en la integral degenerada Definición §21.6.5 — Integración en un intervalo degenerado. No se reorienta ningún intervalo ni se construye una función diferente para cada punto mediante elección. $\square$

**Lectura.** El origen de acumulación sólo modifica la función acumulada en una constante. Este desplazamiento algebraico no afecta los incrementos posteriores; es la misma estructura que explica por qué las primitivas difieren en una constante, aunque el enunciado actual requiere únicamente integrabilidad.

### Corolario 22.6.4 — Determinación de una integranda continua por su acumulada
Sean $f,g:[a,b]\to\mathbb R$ continuas en todos los puntos de $[a,b]$, donde $a<b$. Si sus acumuladas son iguales como funciones tipadas,

$$
F_{f,a}=F_{g,a},
$$

entonces $f=g$ en todo $[a,b]$, incluidos sus extremos.

**Demostración.**
La continuidad de $f$ y $g$ implica su integrabilidad por Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable, de modo que ambas acumuladas están definidas. Sea $x\in(a,b)$. Por Corolario §22.2.3 — Integranda continua sobre todo el intervalo son derivables en $x$ y satisfacen $F_{f,a}'(x)=f(x)$ y $F_{g,a}'(x)=g(x)$. Como las acumuladas son la misma función, sus cocientes incrementales son idénticos y la unicidad de la derivada Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada obliga a $f(x)=g(x)$. Hemos demostrado la igualdad en todo el interior.

Quedan los extremos; no los trataremos mediante derivadas bilaterales. Supongamos $f(a)\ne g(a)$ y pongamos $D:=|f(a)-g(a)|>0$, $\varepsilon:=D/3$. La continuidad relativa de cada función en $a$, aplicada a esta tolerancia, proporciona radios positivos $\delta_f,\delta_g$ para los cuales

$$
|t-a|<\delta_f\Longrightarrow |f(t)-f(a)|<\varepsilon,
\qquad
|t-a|<\delta_g\Longrightarrow |g(t)-g(a)|<\varepsilon
$$

si $t\in[a,b]$. Definamos explícitamente

$$
r:=\tfrac12\min\{\delta_f,\delta_g,b-a\}>0,
\qquad t:=a+r\in(a,b).
$$

Por la igualdad interior $f(t)=g(t)$ y la desigualdad triangular,

$$
D=|f(a)-g(a)|
\le |f(a)-f(t)|+|g(t)-g(a)|
<2\varepsilon=2D/3<D,
$$

contradicción. Así $f(a)=g(a)$. Para el extremo $b$ el mismo argumento utiliza la continuidad en $b$ y el punto determinado $t:=b-\tfrac12\min\{\delta_f,\delta_g,b-a\}\in(a,b)$; se obtiene igualmente $f(b)=g(b)$. En consecuencia los grafos de $f$ y $g$ coinciden, y Proposición §0.6.3 — Criterio de igualdad de funciones da su igualdad como funciones. Sólo se emplearon dos testigos de continuidad en cada argumento extremo y un punto construido por fórmula; no se apeló a sucesiones elegidas ni a $CC(\mathbb R)$. $\square$

**Alcance.** La continuidad es esencial para recuperar también los valores puntuales en los extremos: la fórmula de derivación de la acumulada se ha demostrado en el interior bajo continuidad puntual, no para cualquier integranda discontinua. No hemos probado una regla general de diferenciación de toda función integrable ni una teoría de integración orientada.

**Conclusión del capítulo.** La acumulada existe para toda integranda Riemann-integrable y es continua incluso si la integranda presenta saltos. Donde la integranda es continua, su derivada interior recupera el valor de ésta; cuando existe una primitiva, Newton–Leibniz expresa toda integral en un intervalo ordenado mediante la diferencia de valores de la primitiva. La integración por partes y la sustitución se derivan de estas identidades, pero requieren comprobar por separado la integrabilidad de sus nuevas integrandas. Normalización, linealidad y traslado del origen completan la estructura. El paso siguiente será el estudio de sucesiones y series de funciones: habrá que distinguir convergencia puntual de convergencia uniforme antes de intercambiar límites con integrales o derivadas.
