## 22.5. Cambio de variable {#sec-ta-22-5}

En una integral definida, la sustitución de una variable no consiste únicamente en reemplazar letras. La composición $f\circ\varphi$ debe tener dominio efectivo comprobado, el producto con la derivada debe ser integrable y los extremos transformados deben ordenarse antes de escribir otra integral. Además, una función diferenciable puede recorrer varias veces un mismo tramo: la monotonía no será una hipótesis de nuestra regla básica.

Fijaremos $a<b$, $c<d$, una función continua $f:[c,d]\to\mathbb R$ y una función $\varphi:[a,b]\to[c,d]$ continua en el cerrado y derivable en $(a,b)$. Construiremos primero la composición de $\varphi$ con la acumulada de $f$. Esa acumulada puede no tener derivada bilateral en $c$ o $d$; resolveremos expresamente el caso en que $\varphi$ alcanza uno de esos extremos en un punto interior. Después separaremos la hipótesis necesaria de integrabilidad del producto transformado de una condición suficiente de continuidad.

### Lema 22.5.1 — Regla de la cadena para la acumulada, incluidos los extremos de su dominio
Sean $c<d$, $f:[c,d]\to\mathbb R$ continua en todo el cerrado y $F:=F_{f,c}:[c,d]\to\mathbb R$ su acumulada. Sean $a<b$ y $\varphi:[a,b]\to[c,d]$ continua en $[a,b]$ y derivable en $(a,b)$. La composición tipada

$$
H:=F\circ\varphi:[a,b]\longrightarrow\mathbb R
\tag{22.5.1}
$$

es continua en el cerrado y, para cada $x\in(a,b)$, es derivable y satisface

$$
\boxed{H'(x)=f(\varphi(x))\,\varphi'(x).}
\tag{22.5.2}
$$

La igualdad vale también si $\varphi(x)=c$ o $\varphi(x)=d$; no atribuye a $F$ una derivada bilateral en esos extremos.

**Demostración.**
La continuidad de $f$ implica integrabilidad por Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable; por tanto Definición §22.1.1 — Función integral acumulada define $F$ sobre todo $[c,d]$. La estimación Teorema §22.1.4 — Acotación global, condición de Lipschitz y continuidad uniforme proporciona un real fijo $K\ge0$ tal que

$$
|F(v)-F(u)|\le K|v-u|\qquad(u,v\in[c,d]).
\tag{22.5.3}
$$

La composición está definida en todo $[a,b]$ porque $\varphia,b\subseteq[c,d]$: Proposición §16.4.1 — Dominio efectivo y tipado de la composición controla su dominio efectivo y Teorema §17.4.5 — Composición en el dominio efectivo prueba su continuidad, incluidos los extremos $a,b$.

Fijemos $x\in(a,b)$. Si $c<\varphi(x)<d$, la continuidad de $f$ en $\varphi(x)$ y la primera parte del teorema fundamental Teorema §22.2.2 — Primera parte del teorema fundamental del cálculo: continuidad puntual dan $F'(\varphi(x))=f(\varphi(x))$. Aplicando la regla de la cadena Teorema §19.6.2 — Regla de la cadena en el dominio efectivo en el dominio efectivo resulta (22.5.2).

Supongamos ahora $\varphi(x)=c$. Como $\varphi(t)\ge c=\varphi(x)$ para todo $t\in[a,b]$, $\varphi$ presenta un mínimo local en el punto interior $x$; por Fermat Corolario §20.1.5 — Fermat en puntos interiores de un intervalo cerrado se sigue $\varphi'(x)=0$. Si $\varphi(x)=d$, el mismo argumento, mediante un máximo local, vuelve a dar $\varphi'(x)=0$. En cualquiera de los dos casos, sea $\varepsilon>0$. La definición de la derivada de $\varphi$ con valor cero proporciona $\delta>0$ tal que, para todo $y\in[a,b]$ con $0<|y-x|<\delta$,

$$
\left|\frac{\varphi(y)-\varphi(x)}{y-x}\right|<\frac{\varepsilon}{K+1_{\mathbb R}}.
$$

Como ambos valores de $\varphi$ pertenecen a $[c,d]$, (22.5.3) implica

$$
\left|\frac{H(y)-H(x)}{y-x}\right|
\le K\left|\frac{\varphi(y)-\varphi(x)}{y-x}\right|
\le\frac{K\varepsilon}{K+1_{\mathbb R}}<\varepsilon.
\tag{22.5.4}
$$

La última desigualdad es válida también para $K=0$, cuando el miembro anterior es cero. Como $x$ es interior al dominio, el cociente tiene puntos admisibles arbitrariamente próximos por ambos lados. Se ha probado, directamente por la definición de derivada, que $H'(x)=0=f(\varphi(x))\varphi'(x)$. Los tres casos agotan $[c,d]$; no hemos derivado $F$ en $c$ ni en $d$, ni escogido una sucesión de puntos. $\square$

**Lectura.** La cadena ordinaria se aplica cuando el valor intermedio es interior. Si el valor intermedio alcanza un extremo, Fermat anula la derivada interior de $\varphi$ y la condición de Lipschitz de la acumulada anula el cociente incremental de la composición. Ambos mecanismos desembocan en la misma fórmula.

### Teorema 22.5.2 — Cambio de variable con integrabilidad explícita y extremos ordenados
Bajo las hipótesis del lema anterior, sea además $p:[a,b]\to\mathbb R$ una función tal que

$$
p(x)=\varphi'(x)\qquad(x\in(a,b)),
\tag{22.5.5}
$$

y definamos, por composición y producto puntuales tipados,

$$
g:[a,b]\longrightarrow\mathbb R,\qquad
g(t):=f(\varphi(t))\,p(t).
\tag{22.5.6}
$$

**Supongamos explícitamente que $g$ es Riemann-integrable.** Escribamos $u:=\varphi(a)$ y $v:=\varphi(b)$; ambos pertenecen a $[c,d]$. Entonces

$$
\boxed{\int_a^b g=F_{f,c}(v)-F_{f,c}(u).}
\tag{22.5.7}
$$

En particular, ésta es una identidad de integrales con límites siempre ordenados en cada uno de los tres casos:

$$
\boxed{
\begin{array}{ll}
 u<v:&\displaystyle \int_a^b g=\int_u^v(f\upharpoonright[u,v]),\\[4pt]
 u=v:&\displaystyle \int_a^b g=0,\\[4pt]
 u>v:&\displaystyle \int_a^b g=-\int_v^u(f\upharpoonright[v,u]).
\end{array}}
\tag{22.5.8}
$$

No se presupone que $\varphi$ sea inyectiva o monótona; el factor $p$ conserva su signo y no se reemplaza por $|p|$. Tampoco se presume la integrabilidad de $g$ a partir de la sola derivabilidad de $\varphi$.

**Demostración.**
Por Proposición §16.4.1 — Dominio efectivo y tipado de la composición, la composición $f\circ\varphi$ es una función de dominio exacto $[a,b]$ y codominio real. El producto con $p$ existe con el mismo tipado por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales, de modo que (22.5.6) define efectivamente $g$. El lema Lema §22.5.1 — Regla de la cadena para la acumulada, incluidos los extremos de su dominio asegura que $H=F_{f,c}\circ\varphi$ es continua sobre $[a,b]$ y, en cada $x\in(a,b)$, satisface

$$
H'(x)=f(\varphi(x))\varphi'(x)=f(\varphi(x))p(x)=g(x).
$$

Así, $H$ es primitiva de $g$ en el sentido de Definición §22.3.1 — Primitiva sobre un intervalo cerrado. Sólo ahora, porque la integrabilidad de $g$ es una hipótesis expresa, podemos aplicar Newton–Leibniz Teorema §22.3.3 — Regla de Newton–Leibniz para integrandas integrables que admiten primitiva:

$$
\int_a^b g=H(b)-H(a)=F_{f,c}(v)-F_{f,c}(u).
$$

Esto prueba (22.5.7). Para obtener (22.5.8), si $u<v$, Proposición §22.1.2 — Valores extremos e identidad exacta de los incrementos identifica la diferencia de la acumulada con la integral de la restricción a $[u,v]$, cuya integrabilidad está garantizada por Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado. Si $u=v$, la diferencia es cero; la integral sobre $[u,u]$, cuando se escribe, vale igualmente cero por Definición §21.6.5 — Integración en un intervalo degenerado. Si $u>v$, aplicamos Proposición §22.1.2 — Valores extremos e identidad exacta de los incrementos a los extremos ordenados $v<u$, obteniendo $F_{f,c}(u)-F_{f,c}(v)=\int_v^u(f\upharpoonright[v,u])$; tomamos el opuesto de ambos miembros en el cuerpo real. En ningún punto se define $\int_u^v$ cuando $u>v$. $\square$

**Interpretación.** La derivada del cambio registra las variaciones con signo. Una trayectoria que regresa al mismo valor extremo produce una diferencia nula de la acumulada, aunque recorra puntos intermedios y la integranda transformada no sea idénticamente cero.

### Corolario 22.5.3 — Versión de uso corriente con derivada prolongable continuamente
Sean $f:[c,d]\to\mathbb R$ y $\varphi:[a,b]\to[c,d]$ como en el lema. Si además existe una función continua $p:[a,b]\to\mathbb R$ que satisface $p=\varphi'$ en $(a,b)$, entonces la función $g(t)=f(\varphi(t))p(t)$ es integrable y valen (22.5.7) y los tres casos (22.5.8). En particular, si $\varphi(a)\le\varphi(b)$, la sustitución toma la forma usual con una integral a la derecha cuyo intervalo está ordenado.

**Demostración.**
El dominio efectivo de $f\circ\varphi$ es $[a,b]$ porque $\varphi$ toma sus valores en $[c,d]$ (Proposición §16.4.1 — Dominio efectivo y tipado de la composición); dicha composición es continua en todo el cerrado por Teorema §17.4.5 — Composición en el dominio efectivo. El producto puntual con la función continua $p$ es continuo por Teorema §17.4.3 — Estabilidad de la continuidad bajo operaciones algebraicas y valor absoluto y existe como función tipada por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. Resulta integrable por Corolario §21.7.4 — Toda función continua en un intervalo cerrado es integrable. Verificadas las hipótesis, se aplica Teorema §22.5.2 — Cambio de variable con integrabilidad explícita y extremos ordenados, sin imponer monotonía ni invertir el orden de integración. $\square$

### Corolario 22.5.4 — La sustitución en cada subintervalo ordenado
Con las hipótesis del teorema Teorema §22.5.2 — Cambio de variable con integrabilidad explícita y extremos ordenados, para cada $a\le r\le s\le b$ se cumple

$$
\boxed{\int_r^s(g\upharpoonright[r,s])
=F_{f,c}(\varphi(s))-F_{f,c}(\varphi(r)).}
\tag{22.5.9}
$$

La diferencia de la derecha se convierte en la integral de $f$ restringida al intervalo cuyos extremos son $\varphi(r)$ y $\varphi(s)$ si están ordenados de menor a mayor, y en el opuesto de esa integral si aparecen en orden contrario. Si coinciden, el resultado es cero.

**Demostración.**
Si $r=s$, la integral del singleton es cero por Definición §21.6.5 — Integración en un intervalo degenerado y la diferencia de valores de la acumulada también es cero. Si $r<s$, la restricción tipada $\varphi\upharpoonright[r,s]$ es continua por Corolario §17.4.6 — Clausura global, restricciones y cocientes y derivable en $(r,s)$ con derivada $p$ allí por Proposición §19.5.2 — Restricción de una función derivable. La integrabilidad de $g\upharpoonright[r,s]$ proviene de Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado. Los productos y las composiciones de las restricciones coinciden punto a punto con la restricción de $g$ y tienen los mismos dominio $[r,s]$ y codominio $\mathbb R$ (Proposición §1.3.2 — Existencia y unicidad de la restricción). Aplicamos Teorema §22.5.2 — Cambio de variable con integrabilidad explícita y extremos ordenados a este intervalo y obtenemos (22.5.9). Las tres alternativas para los nuevos extremos se deducen de (22.5.8). $\square$

### Proposición 22.5.5 — Dos ejemplos: retorno no monótono e inversión de extremos
**(a) Retorno.** En $[-1,1]$ fijemos $\varphi(t)=t^2$, como función $[-1,1]\to[0,1]$, $p(t)=2t$, y en $[0,1]$ la función identidad $f(u)=u$. La integranda transformada $g(t)=2t\cdot t^2$ es continua e integrable, pero

$$
\boxed{\int_{-1}^{1} 2t\,t^2\,dt=0.}
\tag{22.5.10}
$$

La función $\varphi$ no es monótona en $[-1,1]$, pues $\varphi(-1)=1$, $\varphi(0)=0$ y $\varphi(1)=1$.

**(b) Extremos invertidos.** En $[0,1]$ tomemos $\varphi(t)=1-t$, $p(t)=-1$ y $f(u)=u$. La integranda transformada es $g(t)=-(1-t)$, y

$$
\boxed{\int_0^1 -(1-t)\,dt
=-\int_0^1 u\,du=-\frac12.}
\tag{22.5.11}
$$

**Demostración.**
Para (a), de $-1\le t\le1$ se sigue $0\le t^2\le1$ por la compatibilidad del orden real con el producto; la función es, por ello, una aplicación tipada hacia $[0,1]$. Su continuidad y la de $p$ y $f$ se deducen de las operaciones polinómicas ya disponibles (Teorema §17.5.3 — Todo polinomio real es continuo en la recta y restricción Corolario §17.4.6 — Clausura global, restricciones y cocientes); la regla de derivación del producto, o la regla del producto Teorema §19.4.3 — Regla de derivación del producto junto con Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática, proporciona $\varphi'(t)=2t$ para $t\in(-1,1)$. El corolario Corolario §22.5.3 — Versión de uso corriente con derivada prolongable continuamente demuestra la integrabilidad de $g$. Como $\varphi(-1)=\varphi(1)=1$, el caso intermedio de (22.5.8) da (22.5.10). La triple evaluación indicada en el enunciado descarta ambas alternativas de monotonía.

Para (b), la función afín $\varphi:[0,1]\to[0,1]$ tiene derivada interior $-1$ por las reglas de suma y multiplicación por escalares (Teorema §19.4.1 — Regla de derivación de la suma, Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias) y la derivada de la identidad (Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática), con prolongación continua constante $p=-1$. La función $g$ es integrable por Corolario §22.5.3 — Versión de uso corriente con derivada prolongable continuamente; como $\varphi(0)=1>0=\varphi(1)$, aplicamos el tercer caso de (22.5.8). Proposición §22.4.4 — Primer cálculo por integración por partes: la función identidad, para la identidad sobre $[0,1]$, da $\int_0^1 u\,du=(1^2-0^2)/2=1/2$. La igualdad (22.5.11) se sigue sin escribir ninguna integral con extremos invertidos. $\square$

**Nota de fuentes.** Jacob y Evans, *A Course in Analysis*, vol. I (2015), cap. 13, teorema 13.7, p. 186, ofrecen una versión clásica del cambio de variable para una integranda continua y un cambio diferenciable con derivada continua; el teorema 13.12, p. 188, introduce una formulación alternativa con inversión de un cambio estrictamente monótono. Estas localizaciones se han cotejado en la extracción textual del ejemplar bibliográfico. La demostración precedente es propia: separa integrabilidad de continuidad de la derivada, considera los valores intermedios extremos mediante Fermat y Lipschitz y no exige monotonía ni una inversa.

**Transición.** El teorema fundamental permite evaluar las integrales de dos maneras complementarias: una primitiva puede conocerse directamente o construirse mediante acumulación. La siguiente unidad distinguirá las consecuencias estructurales de esa dualidad de las simples técnicas de cálculo, antes de iniciar la auditoría global de cierre del capítulo.
