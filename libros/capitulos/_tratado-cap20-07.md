## 20.7. Propiedad de Darboux de las derivadas {#sec-ta-20-7}

La continuidad de una función, por sí sola, no garantiza su derivabilidad; y la derivabilidad de una función tampoco promete continuidad de sus valores derivados. Aun así, hay una restricción notable: una derivada definida en todos los puntos interiores de un intervalo no puede omitir un valor situado estrictamente entre dos de sus valores. Esta propiedad, conocida como *propiedad de Darboux*, no es una aplicación del teorema del valor intermedio a una supuesta función derivada continua.

La estrategia será distinta. Para un número real dado $\lambda$, restaremos la función afín $x\mapsto\lambda x$ —o invertiremos su diferencia—. Si las derivadas en dos extremos tienen signos opuestos en la orientación adecuada, una cota local excluye que el mínimo de la función auxiliar esté en esos extremos. Weierstrass coloca entonces un mínimo en el interior y Fermat obliga a anular allí la derivada auxiliar.

### Lema 20.7.1 — Un cambio orientado de signo fuerza una derivada nula
Sean $D\subseteq\mathbb R$, $u,v\in D$ con $u<v$, $[u,v]\subseteq D$ y $h:D\to\mathbb R$. Supongamos que $h$ es derivable, relativamente a $D$, en todos los puntos de $[u,v]$ y que

$$
h'(u)<0<h'(v).
\tag{20.7.1}
$$

Entonces existe $c\in(u,v)$ tal que $h'(c)=0$.

**Demostración.**
**Primero, los bordes no pueden minimizar.** Pongamos $d_u:=h'(u)<0$. El criterio cuantificado de derivada Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada, con $\varepsilon_u:=-d_u/2>0$, proporciona $\delta_u>0$ tal que para $x\in D$,

$$
0<|x-u|<\delta_u\quad\Longrightarrow\quad
\frac{h(x)-h(u)}{x-u}<\frac{d_u}{2}<0.
$$

Elijamos el punto *determinado* $t:=u+\frac12\min\{\delta_u,v-u\}$. Se tiene $u<t<v$ y $t\in D$, porque $[u,v]\subseteq D$. Puesto que $t-u>0$, la desigualdad del cociente implica $h(t)<h(u)$.

Análogamente, sea $d_v:=h'(v)>0$. Para $\varepsilon_v:=d_v/2$, la definición de derivada ofrece $\delta_v>0$ de modo que los cocientes correspondientes a argumentos con $0<|x-v|<\delta_v$ son mayores que $d_v/2>0$. Tomemos

$$
s:=v-\frac12\min\{\delta_v,v-u\}\in(u,v).
$$

Como $s-v<0$, multiplicar la desigualdad positiva para el cociente por ese denominador negativo produce $h(s)<h(v)$. En consecuencia, ni $u$ ni $v$ puede ser un punto de mínimo sobre $[u,v]$.

**Segundo, el mínimo existe y es interior.** Por Teorema §19.2.1 — Toda función derivable en un punto es continua en él, la derivabilidad de $h$ en cada $x\in[u,v]$ implica su continuidad relativa a $D$ en cada uno de esos puntos. La restricción $h\upharpoonright[u,v]:[u,v]\to\mathbb R$ es, pues, continua en todo su dominio por Corolario §17.4.6 — Clausura global, restricciones y cocientes. El intervalo $[u,v]$ es compacto y no vacío por Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto; Teorema §18.5.4 — Teorema del valor extremo: Weierstrass proporciona $c\in[u,v]$ tal que $h(c)\le h(x)$ para todo $x\in[u,v]$. Las dos desigualdades estrictas recién demostradas excluyen $c=u$ y $c=v$, luego $u<c<v$.

Tomemos $r:=\frac12\min\{c-u,v-c\}>0$. Si $x\in D$ y $|x-c|<r$, entonces $u<x<v$ y $h(c)\le h(x)$; por tanto, $c$ es un mínimo local de la función original $h:D\to\mathbb R$. Además $B_r(c)\subseteq D$, por lo que $c$ es interior a $D$. Como $h$ es derivable en $c$, el teorema de Fermat Teorema §20.1.4 — Fermat: derivada nula en un extremo local interior se aplica sin cambiar el dominio de su derivada y da $h'(c)=0$. Sólo fijamos dos argumentos explícitos y un mínimo cuya existencia ya estaba demostrada: no se elige una familia de minimizadores. $\square$

### Teorema 20.7.2 — Darboux: valores intermedios de una derivada
Sean $D\subseteq\mathbb R$ un intervalo, $f:D\to\mathbb R$ derivable en cada punto interior de $D$, y $u,v\in\operatorname{int}(D)$ con $u<v$. Si $\lambda\in\mathbb R$ satisface una de las desigualdades

$$
f'(u)<\lambda<f'(v)
\qquad\text{o}\qquad
f'(v)<\lambda<f'(u),
$$

entonces existe $c\in(u,v)$ tal que

$$
\boxed{f'(c)=\lambda.}
\tag{20.7.2}
$$

La derivabilidad se exige sólo en el interior de $D$: no se postula continuidad ni derivabilidad de $f$ en los extremos que pudieran pertenecer a $D$. La conclusión compara valores puntuales de derivadas existentes; no presupone haber construido una función derivada global ni le atribuye continuidad.

**Demostración.**
El carácter intervalar de $D$ y $u<v$ implican $[u,v]\subseteq D$. Los extremos $u,v$ son interiores a $D$ por hipótesis, y cualquier $c\in(u,v)$ también lo es, pues la bola de radio $\frac12\min\{c-u,v-c\}$ queda contenida en $[u,v]\subseteq D$. Así $f$ es derivable, relativamente a su dominio original, en cada punto de $[u,v]$. En particular, es continua en esos puntos por Teorema §19.2.1 — Toda función derivable en un punto es continua en él.

Sea $A:\mathbb R\to\mathbb R$ la función afín $A(x)=\lambda x$ y sea $A_D:=A\upharpoonright D:D\to\mathbb R$ su restricción. Las construcciones y reglas de §§19.1, 19.4–19.5 (Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática, Proposición §19.5.2 — Restricción de una función derivable, Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales, Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias) garantizan que, en cada $x\in[u,v]$, las diferencias puntuales $f-A_D$ y $A_D-f$ son derivables relativamente a $D$ y que

$$
(f-A_D)'(x)=f'(x)-\lambda,
\qquad (A_D-f)'(x)=\lambda-f'(x).
\tag{20.7.3}
$$

Si $f'(u)<\lambda<f'(v)$, definimos $h:=f-A_D$. La fórmula (20.7.3) da $h'(u)<0<h'(v)$. Aplicamos Lema §20.7.1 — Un cambio orientado de signo fuerza una derivada nula a esa misma función $h:D\to\mathbb R$ y al segmento $[u,v]$; resulta $c\in(u,v)$ con $0=h'(c)=f'(c)-\lambda$, de donde $f'(c)=\lambda$.

Si $f'(v)<\lambda<f'(u)$, definimos en cambio $h:=A_D-f$. Entonces $h'(u)=\lambda-f'(u)<0$ y $h'(v)=\lambda-f'(v)>0$. El mismo lema proporciona $c\in(u,v)$ con $0=h'(c)=\lambda-f'(c)$, y otra vez $f'(c)=\lambda$. Los casos agotan la hipótesis. No se aplicó el teorema del valor intermedio a $f'$ ni se supuso su continuidad. $\square$

**Lectura deductiva.** Los límites de pendientes que definen $f'(u)$ y $f'(v)$ excluyen determinados extremos de una función auxiliar. La continuidad necesaria para Weierstrass es la de esa función auxiliar —deducida de su derivabilidad—, no la continuidad de los valores derivados. Darboux es una propiedad de valores intermedios que puede existir sin continuidad.

### Corolario 20.7.3 — Si una derivada no se anula, su signo es constante
Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo $[a,b]$ y derivable en todos los puntos interiores. Si

$$
\forall x\in(a,b),\qquad f'(x)\ne0,
$$

entonces ocurre exactamente una de las dos alternativas siguientes: $f'(x)>0$ para todo $x\in(a,b)$ y $f$ es estrictamente creciente en $[a,b]$; o bien $f'(x)<0$ para todo $x\in(a,b)$ y $f$ es estrictamente decreciente en $[a,b]$.

**Demostración.**
El punto $x_0:=(a+b)/2$ pertenece a $(a,b)$, de modo que la derivada $f'(x_0)$ existe y, por hipótesis, es distinta de cero. Por tricotomía, tiene signo positivo o negativo. No pueden existir puntos $u,v\in(a,b)$ con $f'(u)>0$ y $f'(v)<0$: ordenando esos dos puntos como $p<q$, el número $0$ queda estrictamente entre $f'(p)$ y $f'(q)$, y Teorema §20.7.2 — Darboux: valores intermedios de una derivada obligaría a encontrar $c\in(p,q)$ con $f'(c)=0$, contradicción. Por tanto todos los valores interiores de la derivada tienen el mismo signo que $f'(x_0)$.

Si son positivos, el criterio Teorema §20.5.2 — Criterios suficientes de monotonía por el signo de la derivada establece que $f$ es estrictamente creciente sobre $[a,b]$; si son negativos, establece que es estrictamente decreciente. Las alternativas son excluyentes porque $(a,b)$ contiene $x_0$. La continuidad de borde se emplea sólo en el paso final hacia la monotonía global, no en Darboux. $\square$

### Proposición 20.7.4 — Una derivada puede carecer de continuidad: ejemplo algebraico
Existe una función $F:[-1,1]\to\mathbb R$ derivable en cada punto de su dominio, incluido el punto interior $0$, para la cual los valores derivados no son continuos en $0$. La construiremos sin emplear funciones trigonométricas ni potencias generales no definidas.

**Demostración.**
Para cada natural $n\ge1$ consideremos su numeral real $N_n:=\nu_{\mathbb R}(n)$, que es positivo; escribiremos localmente $x_n:=1/N_n$ y

$$
\Delta_n:=x_n-x_{n+1}
=\frac{1}{N_nN_{n+1}}>0,
\qquad I_n:=[x_{n+1},x_n].
\tag{20.7.4}
$$

La compatibilidad de la aplicación de numerales con la suma permite escribir $N_{n+1}=N_n+1$ en estas identidades, sin identificar los conjuntos $\mathbb N$ y $\mathbb R$. Por arquimedianidad (Teorema §4.6.3 — Todo cuerpo ordenado completo es arquimediano), para cada $x\in(0,1]$ existe $k\ge2$ con $x_k<x$. El buen orden (Teorema §1.6.13 — Principio de buen orden) da el menor índice con esta propiedad; poniéndolo como $n+1$, se obtiene $x_{n+1}<x\le x_n$. Por tanto, los intervalos $I_n$ cubren $(0,1]$ y sólo se solapan, cuando lo hacen, en extremos comunes.

Para $x\in I_n$ pongamos $t_n(x):=(x-x_{n+1})/\Delta_n\in[0,1]$ y prescribamos

$$
F(x):=0\quad(-1\le x\le0),\qquad
F(x):=\Delta_n\,t_n(x)^2\,[1-t_n(x)]^2
\quad (x\in I_n).
\tag{20.7.5}
$$

En los extremos de $I_n$ la expresión vale $0$, independientemente del índice. Así, cuando dos intervalos comparten un extremo, ambas fórmulas coinciden, y la prescripción determina un único valor para cada $x\in[-1,1]$. Por Separación del conjunto ambiente $[-1,1]\times\mathbb R$ se obtiene el grafo funcional de $F:[-1,1]\to\mathbb R$, sin escoger un índice para cada argumento.

En el interior de $I_n$, las reglas de derivación de funciones afines, productos y composiciones ya demostradas en el Capítulo 19 proporcionan, escribiendo $t:=t_n(x)$,

$$
F'(x)=2t(1-t)(1-2t).
\tag{20.7.6}
$$

Las expresiones polinómicas definidas en toda la recta por cada rama tienen derivada $0$ en sus dos extremos, pues el miembro derecho de (20.7.6) se anula en $t=0$ y $t=1$. En cada punto compartido $x_n$ con $n\ge2$, las derivadas laterales de $F$ coinciden en $0$; el criterio Teorema §19.8.4 — Reconstrucción de la derivada desde los lados activos acredita la derivada relativa $F'(x_n)=0$. En $x_1=1$ sólo está activo el lado izquierdo y proporciona también $F'(1)=0$. Para cada $x\in[-1,0)$ la función es localmente constante y su derivada es $0$; en $-1$ la derivada relativa derecha es también $0$.

Resta comprobar el origen, donde las ramas se acumulan. En $[0,1]$, $0\le t(1-t)\le1/4$, de donde $0\le F(x)\le\Delta_n/16$ para $x\in I_n$. Si $x>0$ pertenece a $I_n$, entonces $x\ge x_{n+1}=1/N_{n+1}$ y

$$
0\le\frac{F(x)-F(0)}{x}
\le\frac{\Delta_n}{16x}
\le\frac{1}{16N_n}.
\tag{20.7.7}
$$

Dado $\varepsilon>0$, la arquimedianidad permite fijar $N\ge1$ con $1/(16N_N)<\varepsilon$. Si $0<x<x_N$, el intervalo $I_n$ que contiene a $x$ debe tener $n\ge N$: de lo contrario $n+1\le N$ y $x\ge x_{n+1}\ge x_N$, contradicción. La desigualdad (20.7.7) da entonces $0\le F(x)/x<\varepsilon$. Además, $0$ acumula por ambos lados en $[-1,1]$: para cada $r>0$ sirven $x_+:=\frac12\min\{r,1\}$ y $x_-:=-x_+$. Para $x<0$ el cociente de $F$ respecto de $0$ es exactamente cero; para $x>0$ está acotado por (20.7.7). Con el mismo radio $x_N>0$ todos los cocientes tienen módulo menor que $\varepsilon$. Por la definición de derivada relativa, $F'(0)=0$.

Finalmente, para cada $n\ge1$ el punto explícito

$$
y_n:=x_{n+1}+\frac{\Delta_n}{4}\in(x_{n+1},x_n)
$$

satisface $t_n(y_n)=1/4$ y, por (20.7.6),

$$
\boxed{F'(y_n)=\frac{3}{16}\ne0=F'(0).}
\tag{20.7.8}
$$

Dado cualquier radio $r>0$, la propiedad arquimediana permite tomar un índice $n$ con $x_n<r$; entonces $0<y_n<x_n<r$ y $|F'(y_n)-F'(0)|=3/16>1/8$. La aplicación local $d:[-1,1]\to\mathbb R$, $d(x):=F'(x)$, existe como grafo por Separación y unicidad de cada derivada; la desigualdad anterior refuta su continuidad en $0$ con tolerancia $1/8$. Sin embargo, Teorema §20.7.2 — Darboux: valores intermedios de una derivada sigue garantizando los valores intermedios de $d$ entre puntos interiores. No hubo funciones trigonométricas, una serie ni una elección numerable de puntos. $\square$

**Distinción esencial.** La propiedad de Darboux prohíbe los saltos que omiten valores intermedios, pero no fuerza continuidad. El ejemplo exhibe una función derivable en todos los puntos de $[-1,1]$ cuya derivada es discontinua en el punto interior $0$: por tanto, el teorema no puede ser una aplicación del valor intermedio basada en continuidad de la derivada.

**Transición.** Fermat y Weierstrass han permitido establecer una propiedad de las derivadas que no se obtiene aplicando continuidad a la propia derivada. El siguiente tramo, §20.8, desarrollará la fórmula de Taylor de orden finito y sus restos, con hipótesis diferenciables explícitas; ninguna igualdad con una serie infinita será presumida. §20.7 queda estabilizada como unidad humana. El capítulo permanece abierto y no se abre un nuevo checkpoint Lean.
