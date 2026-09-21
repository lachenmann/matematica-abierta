## 21.6. Aditividad por intervalos y extremos coincidentes {#sec-ta-21-6}

La linealidad de §21.5 compara funciones definidas sobre el mismo intervalo. Dividir el intervalo plantea un problema distinto: antes de escribir una igualdad entre tres integrales, debemos demostrar que las restricciones son integrables. El punto de corte será un nodo de la partición, no una operación sobre límites de integración todavía no definidos. Sólo después extenderemos la notación al intervalo formado por un único punto.

Fijemos $a,b,c\in\mathbb R$ con $a<c<b$ y una función acotada $f:[a,b]\to\mathbb R$. Por la restricción tipada de §1.3, escribiremos

$$
f_-:=f\upharpoonright[a,c]:[a,c]\to\mathbb R,\qquad
f_+:=f\upharpoonright[c,b]:[c,b]\to\mathbb R.
\tag{21.6.1}
$$

Ambas funciones son acotadas: cualesquiera dos cotas globales de $f$ sirven también para cada restricción. En el punto compartido $c$ sus valores coinciden con $f(c)$; sin embargo, sus dominios son diferentes y no las identificamos con $f$.

### Lema 21.6.1 — Corte y concatenación de particiones
Si $P=\langle n,p\rangle\in\operatorname{Part}[a,b]$ tiene $c\in V(P)$, existen particiones determinadas unívocamente por sus listas de nodos, $P_-\in\operatorname{Part}[a,c]$ y $P_+\in\operatorname{Part}[c,b]$, tales que sus listas son respectivamente la porción inicial de $P$ hasta $c$ y la porción final desde $c$. Recíprocamente, cualesquiera particiones $Q_-\in\operatorname{Part}[a,c]$ y $Q_+\in\operatorname{Part}[c,b]$ admiten una concatenación $Q_-\mathbin{\star_c}Q_+\in\operatorname{Part}[a,b]$ que conserva ambas listas, escribiendo el nodo $c$ una sola vez. Cortar una concatenación devuelve exactamente sus dos componentes, y concatenar las dos partes de $P$ devuelve $P$.

**Demostración.**
La lista estricta $x_i=p(i)$ no repite nodos. Por $c\in V(P)$ existe un único $j\in J_n$ con $x_j=c$. Dado que $a<c<b$, tenemos $0<j<n$. Existe un natural único $s\ge1$ tal que $j+s=n$: existe por la definición del orden aritmético, y es único por cancelación de la suma natural. Definimos dos funciones tipadas mediante grafos explícitos:

$$
p_-:J_j\to[a,c],\quad p_-(i)=p(i),\qquad
p_+:J_s\to[c,b],\quad p_+(i)=p(j+i).
\tag{21.6.2}
$$

Sus índices permanecen dentro de $J_n$, los extremos son $a,c$ y $c,b$, respectivamente, y el crecimiento estricto se hereda de $P$. Por tanto, $P_-:=\langle j,p_-\rangle$ y $P_+:=\langle s,p_+\rangle$ son particiones de intervalos no degenerados. Cada función tiene como codominio el intervalo correspondiente: $p_-$ no es simplemente una copia de la función original con un codominio incorrecto.

Para la vuelta, escribamos las particiones dadas como $Q_-=\langle r,u\rangle$ y $Q_+=\langle s,v\rangle$, con $u(r)=v(0)=c$ y $r,s\ge1$. Formemos $n:=r+s$ y el grafo de una función $w:J_n\to[a,b]$ por

$$
w(i)=\begin{cases}
u(i),&i\le r,\\
v(t),&r<i\le n\text{ y }i=r+t\ (t\in J_s).
\end{cases}
\tag{21.6.3}
$$

La existencia y unicidad de $t$ provienen de la aritmética natural; para $i>r$ se tiene $t>0$. Las ramas no se solapan y cubren el dominio finito; el conjunto de pares de su grafo existe por separación en $J_n\times[a,b]$. Todas las desigualdades consecutivas se heredan de $u$ o de $v$: la última de la lista izquierda concluye en $c$ y la primera de la derecha comienza en $c$. Los extremos son $a$ y $b$, de modo que $Q:=\langle n,w\rangle$ es una partición. Su conjunto de nodos es $V(Q_-)\cup V(Q_+)$; los únicos nodos compartidos por ambas listas son los $c$ finales e iniciales. Denotamos $Q=Q_-\star_c Q_+$.

Las reglas de corte reconstruyen las mismas funciones tipadas $u$ y $v$: en la lista concatenada el índice único de $c$ es $r$. Recíprocamente, cortar $P$ y concatenarlo reproduce su lista estricta original, sus extremos, la longitud $n=j+s$ y su codominio $[a,b]$. Puede concluirse por igualdad de funciones y pares, o por la unicidad de la lista a partir de los nodos (Lema §21.2.7 — Una lista estricta queda determinada por sus nodos). No se eligió ninguna enumeración: las tres listas se especificaron mediante fórmulas únicas. $\square$

### Lema 21.6.2 — Descomposición exacta de las sumas de Darboux
Para toda partición $P\in\operatorname{Part}[a,b]$ que contiene $c$ entre sus nodos y sus dos partes $P_-,P_+$, se cumplen

$$
\boxed{L(f,P)=L(f_-,P_-)+L(f_+,P_+),}
\tag{21.6.4}
$$

$$
\boxed{U(f,P)=U(f_-,P_-)+U(f_+,P_+).}
\tag{21.6.5}
$$

En particular, escribiendo $G(h,Q):=U(h,Q)-L(h,Q)$ como abreviatura local, tenemos

$$
\boxed{G(f,P)=G(f_-,P_-)+G(f_+,P_+),\qquad
G(f_-,P_-),G(f_+,P_+)\ge0.}
\tag{21.6.6}
$$

Las tres identidades también se aplican a la partición que resulta de concatenar cualesquiera particiones de los dos intervalos.

**Demostración.**
Sea $j$ el índice único de $c$ en $P=\langle n,p\rangle$ y $j+s=n$ como en el lema anterior. Para $i<j$, el subintervalo $I_i(P)$ está contenido en $[a,c]$ y coincide, como conjunto, con $I_i(P_-)$. Como $f_-(t)=f(t)$ en ese conjunto, las dos imágenes de valores son iguales, luego coinciden sus ínfimos, sus supremos y su anchura real. Para $0\le i<s$ sucede exactamente lo mismo entre $I_{j+i}(P)$ e $I_i(P_+)$, esta vez utilizando $f_+$; los índices de la segunda lista se trasladan por $j$, sin modificar sus valores.

La identidad de suma finita por bloques Proposición §14.2.2 — Identidades de los bloques de sumación permite entonces separar los $n=j+s$ sumandos de $L(f,P)$ en los primeros $j$ y los siguientes $s$; ambos bloques contienen al menos un término. Esto demuestra (21.6.4), y el mismo cálculo con supremos demuestra (21.6.5). Restar las identidades da (21.6.6). La no negatividad de cada brecha procede de Proposición §21.2.5 — Encierro global e identidad de la brecha, pues las restricciones están acotadas y sus intervalos no son degenerados. Finalmente, toda concatenación contiene $c$ como nodo y tiene como partes las particiones de partida (Lema §21.6.1 — Corte y concatenación de particiones); por eso las mismas igualdades se aplican a ella. $\square$

**Punto de control.** Un corte que no sea nodo de una partición puede atravesar uno de sus subintervalos; no afirmamos para esa partición las identidades (21.6.4)–(21.6.5). Primero se inserta $c$, usando Lema §21.1.4 — Inserción de un único punto interior, y la monotonía de las sumas bajo refinamiento controla el cambio. Esta precisión evitará cualquier uso ilegítimo de la aditividad antes de demostrarla.

### Teorema 21.6.3 — Integrabilidad y restricciones a los dos lados de un punto interior
Para $a<c<b$ y $f:[a,b]\to\mathbb R$ acotada,

$$
\boxed{f\text{ integrable en }[a,b]
\iff f_-\text{ integrable en }[a,c]
\ \text{y}\ f_+\text{ integrable en }[c,b].}
\tag{21.6.7}
$$

**Demostración.**
**Necesidad.** Supongamos integrable $f$. Sea $\varepsilon>0$ fijo. Por el criterio de Darboux (Teorema §21.4.2 — Criterio de Darboux y estabilidad por refinamiento) existe $P\in\operatorname{Part}[a,b]$ con $G(f,P)<\varepsilon$. Si $c\in V(P)$, pongamos $R=P$. Si no, el lema de inserción Lema §21.1.4 — Inserción de un único punto interior produce un refinamiento $R$ que sí contiene $c$; por Teorema §21.2.8 — Monotonía de las sumas bajo refinamiento, $G(f,R)\le G(f,P)<\varepsilon$. El corte de $R$ entrega particiones $R_-,R_+$, y la identidad exacta (21.6.6) dice

$$
0\le G(f_-,R_-)\le G(f,R)<\varepsilon,
\qquad
0\le G(f_+,R_+)\le G(f,R)<\varepsilon.
$$

Como los dos intervalos son no degenerados y sus restricciones están acotadas, el criterio de Darboux aplicado por separado demuestra la integrabilidad de ambas. La misma prueba vale para cada $\varepsilon$ sin construir una función que elija todas las particiones.

**Suficiencia.** Supongamos integrables $f_-$ y $f_+$. Fijemos $\varepsilon>0$. Para la tolerancia $\varepsilon/2$, obtenemos dos particiones $Q_-$ y $Q_+$ tales que $G(f_-,Q_-)<\varepsilon/2$ y $G(f_+,Q_+)<\varepsilon/2$. Su concatenación $Q=Q_-\star_c Q_+$ satisface por (21.6.6)

$$
0\le G(f,Q)=G(f_-,Q_-)+G(f_+,Q_+)<\varepsilon.
$$

La función $f$ ya era acotada; el criterio de Darboux aplicado al intervalo completo demuestra su integrabilidad. Sólo se utilizaron dos testigos finitos para cada $\varepsilon$, no una familia numerable de elecciones. $\square$

### Teorema 21.6.4 — Aditividad de la integral en un punto interior
Si $f:[a,b]\to\mathbb R$ es integrable y $a<c<b$, sus restricciones $f_-$ y $f_+$ son integrables y

$$
\boxed{\int_a^b f
=\int_a^c f_-+\int_c^b f_+.}
\tag{21.6.8}
$$

**Demostración.**
Las restricciones son integrables por Teorema §21.6.3 — Integrabilidad y restricciones a los dos lados de un punto interior; sólo ahora tienen sentido sus integrales. Denotemos por $H$, $H_-$ y $H_+$ las tres integrales de (21.6.8). Fijemos $\varepsilon>0$. El criterio de Darboux da una partición $P$ de $[a,b]$ con brecha menor que $\varepsilon$. Como en la demostración anterior, conservarla o insertarle el punto $c$ produce una partición $R$ con $c\in V(R)$ y $G(f,R)<\varepsilon$. Cortémosla en $R_-,R_+$.

El encierro del valor integral (Proposición §21.4.4 — Encierro del valor integral y control por la brecha) en los tres intervalos, junto con (21.6.4)–(21.6.5), implica simultáneamente

$$
L(f,R)\le H\le U(f,R)
\quad\text{y}\quad
L(f,R)=L(f_-,R_-)+L(f_+,R_+)
\le H_-+H_+
\le U(f_-,R_-)+U(f_+,R_+)=U(f,R).
$$

Así, dos reales $H$ y $H_-+H_+$ están en un intervalo de longitud estrictamente menor que $\varepsilon$, de donde

$$
|H-(H_-+H_+)|\le U(f,R)-L(f,R)<\varepsilon.
$$

Esto vale para toda tolerancia positiva. Si ambos números fueran distintos, la tolerancia $|H-(H_-+H_+)|/2$ daría una contradicción. Se demuestra (21.6.8) sin suponer que alguna suma de Darboux alcance el valor integral, sin derivadas y sin elegir una sucesión de particiones. $\square$

**Lectura.** La identidad procede de partir sumas finitas en dos bloques y después controlar una diferencia de números reales. El valor de $f(c)$ no recibe dos contribuciones: en las sumas, $c$ es un extremo compartido de subintervalos pero no constituye un término independiente. Esto no implica todavía el teorema fundamental del cálculo.

### Definición 21.6.5 — Integración en un intervalo degenerado
Para cada $d\in\mathbb R$, el intervalo $[d,d]=\{d\}$ contiene exactamente un punto. Toda función tipada $h:[d,d]\to\mathbb R$ es acotada (por ejemplo, sus cotas inferior y superior pueden tomarse iguales a $h(d)$). Extendemos por definición el predicado «integrable» a estas funciones declarándolas integrables y asignándoles

$$
\boxed{\int_d^d h:=0_{\mathbb R}.}
\tag{21.6.9}
$$

Esta definición no invoca las integrales inferior y superior de §21.3: éstas requieren $a<b$, y la partición estricta Definición §21.1.1 — Partición estricta de un intervalo cerrado no existe sobre $[d,d]$ porque sus anchuras tendrían que ser positivas. Para funciones $f:[a,b]\to\mathbb R$ con $a\le b$, la expresión $\int_d^d f$ abrevia aquí y en adelante la integral de la restricción tipada $f\upharpoonright\{d\}:[d,d]\to\mathbb R$ cuando $d\in[a,b]$; no se identifica silenciosamente el dominio de $f$ con un singleton. La orientación $b<a$ continúa sin definición.

### Corolario 21.6.6 — Aditividad para todo punto del intervalo cerrado
Sea $f:[a,b]\to\mathbb R$ integrable, con $a\le b$, interpretando el caso $a=b$ según la definición anterior. Para cada $c\in[a,b]$, ambas restricciones $f\upharpoonright[a,c]$ y $f\upharpoonright[c,b]$ son integrables —cada una según la definición pertinente a su intervalo— y

$$
\boxed{\int_a^b f
=\int_a^c\bigl(f\upharpoonright[a,c]\bigr)
+\int_c^b\bigl(f\upharpoonright[c,b]\bigr).}
\tag{21.6.10}
$$

**Demostración.**
Si $a<c<b$, la integrabilidad de las restricciones y la igualdad son los teoremas 21.6.3–21.6.4. Si $c=a<b$, la restricción a $[a,a]$ tiene integral cero por (21.6.9), mientras que la otra tiene el mismo dominio, codominio y grafo que $f$ y, por igualdad de funciones tipadas, la misma integral. El caso $a<c=b$ es simétrico. Finalmente, si $a=b$, el único punto posible es $c=a=b$ y las tres integrales de (21.6.10) son cero. No se escriben sumas de Darboux para los casos degenerados. $\square$

### Corolario 21.6.7 — Aditividad sobre una subdivisión finita
Sea $f:[a,b]\to\mathbb R$ integrable y $a<b$. Dada una lista real estrictamente creciente de nodos $a=x_0<x_1<\cdots<x_n=b$, con $n\ge1$, cada restricción $f_i:=f\upharpoonright[x_i,x_{i+1}]$ está definida e integrable, y

$$
\boxed{\int_a^b f=\sum_{i=0}^{n-1}\int_{x_i}^{x_{i+1}} f_i.}
\tag{21.6.11}
$$

**Demostración.**
Procedemos por inducción finita en $n$. Para $n=1$ hay un solo intervalo $[x_0,x_1]=[a,b]$: la restricción tiene el mismo dominio, codominio y grafo que $f$, luego es integrable y su integral coincide con la original. Supongamos demostrado el enunciado para una lista de $n+1$ nodos y consideremos una lista de $n+2$ nodos $a=x_0<\cdots<x_n<x_{n+1}=b$. El corte $c:=x_n$ es interior y Corolario §21.6.6 — Aditividad para todo punto del intervalo cerrado da dos restricciones integrables junto con

$$
\int_a^b f
=\int_a^{x_n}\bigl(f\upharpoonright[a,x_n]\bigr)
+\int_{x_n}^{x_{n+1}}\bigl(f\upharpoonright[x_n,x_{n+1}]\bigr).
$$

Aplicamos la hipótesis inductiva a la primera restricción y a la lista $x_0<\cdots<x_n$. La restricción de esta función a cada $[x_i,x_{i+1}]$ coincide, por igualdad de grafos y codominio $\mathbb R$, con la restricción de $f$ al mismo subintervalo. Sustituimos en la identidad anterior y anexamos el último sumando por la regla recursiva de la suma finita Proposición §14.2.2 — Identidades de los bloques de sumación. Esto prueba la fórmula para $n+1$. Los extremos $x_i$ son los de la lista suministrada; no se elige una partición nueva para cada subintervalo. $\square$

**Transición.** Concluimos la aditividad por intervalos en los casos interior, extremo y subdivisión finita, manteniendo la ausencia de definición para límites de integración invertidos. §21.7 demostrará que toda función continua en un intervalo cerrado es integrable, y después se tratarán las funciones monótonas. No se ha supuesto la existencia de primitivas.
