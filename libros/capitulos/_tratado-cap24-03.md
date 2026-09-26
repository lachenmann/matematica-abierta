## 24.3. Los extremos: convergencia absoluta e independencia de la convergencia ordinaria {#sec-ta-24-3}

El radio determina completamente la convergencia a distancias estrictamente menores o mayores que él, pero no decide qué sucede en su frontera. Supondremos en toda esta sección que el radio de la serie considerada es un real $R>0$; su finitud significa que $R\in\mathbb R$, no que efectuemos operaciones con la marca $+\infty$. Los dos puntos fronterizos son $c-R$ y $c+R$, ya legitimados por la clasificación de §24.2.

### Proposición 24.3.1 — Reducción de los extremos a series numéricas y simetría de la convergencia absoluta
Sea $R=R(a,c)>0$ un radio real finito. Escribamos $b_n:=a_nR^n$ para todo $n\in\mathbb N$. Entonces

$$
\boxed{c+R\in C(a,c)\iff\sum_{n=0}^{\infty}b_n\text{ converge},}
\tag{24.3.1}
$$

$$
\boxed{c-R\in C(a,c)\iff\sum_{n=0}^{\infty}(-1)^nb_n\text{ converge}.}
\tag{24.3.2}
$$

La serie de potencias converge absolutamente en $c+R$ si y sólo si converge absolutamente en $c-R$. En caso afirmativo ambos extremos pertenecen a $C(a,c)$. Si alguno de los extremos presenta convergencia condicional, ninguno puede presentar convergencia absoluta.

**Demostración.**
Por las evaluaciones tipadas de «Construcción tipada de los términos y las sumas parciales», los términos en el extremo derecho son $a_n((c+R)-c)^n=a_nR^n=b_n$. En el izquierdo son $a_n(-R)^n=(-1)^na_nR^n=(-1)^nb_n$. La segunda identidad se demuestra por inducción sobre $n$ usando $(-R)=(-1)R$, la recursión de potencias y las leyes del cuerpo; para $n=0$ ambos miembros valen $1$. Las equivalencias (24.3.1)–(24.3.2) siguen exactamente de «Conjunto de convergencia» y «Convergencia, divergencia y suma de una serie».

Por la multiplicatividad del valor absoluto, $|(-1)^n|=1$ y $R>0$, para todo $n$ se tiene

$$
\boxed{|(-1)^nb_n|=|b_n|=|a_n|R^n.}
\tag{24.3.3}
$$

Las dos series de magnitudes tienen, pues, la misma sucesión de términos y las mismas sumas parciales, y convergen simultáneamente o divergen simultáneamente. La convergencia absoluta implica convergencia ordinaria por «La convergencia absoluta implica convergencia ordinaria». En cambio, una serie numérica que converge sólo condicionalmente posee serie de magnitudes divergente («Serie de valores absolutos; convergencia absoluta y condicional»), y (24.3.3) impide que el otro extremo sea absolutamente convergente. $\square$

**Límite de la simetría.** Cambiar $R$ por $-R$ introduce el factor $(-1)^n$, no una permutación de los índices ni una simple multiplicación de toda la suma por $-1$. Las sumas parciales de las dos series ordinarias no tienen por qué comportarse del mismo modo.

### Lema 24.3.2 — Una progresión geométrica supera a un denominador cuadrático
Para todo real $q>1$, la sucesión positiva

$$
\boxed{u_n:=\frac{q^n}{(n+1)(n+2)}\qquad(n\in\mathbb N)}
\tag{24.3.4}
$$

no tiende a cero. Los naturales que aparecen en el denominador se entienden mediante su imagen canónica $\nu_{\mathbb R}$ en los reales, omitiendo la imagen sólo para facilitar la lectura.

**Demostración.**
Definamos $t:=(q+1)/2$, de modo que $1<t<q$. La propiedad arquimediana «Todo cuerpo ordenado completo es arquimediano» aplicada al real positivo $q-t$ permite fijar un natural $N$ tal que

$$
(q-t)(N+1)\ge 2t.
\tag{24.3.5}
$$

Para $n\ge N$, la monotonía de los numerales da $(q-t)(n+1)\ge2t$, equivalente a $q(n+1)\ge t(n+3)$. Todos los denominadores son positivos, así que

$$
\frac{u_{n+1}}{u_n}
=q\frac{n+1}{n+3}\ge t>1
\qquad(n\ge N).
\tag{24.3.6}
$$

Por inducción en $k$, $u_{N+k}\ge t^ku_N\ge u_N>0$; la última desigualdad utiliza $t>1$ y la recursión de potencias. Todo natural $n\ge N$ se escribe $N+k$, de modo que todos los términos de esa cola están acotados inferiormente por el mismo real positivo $u_N$. Con la tolerancia $\varepsilon=u_N/2$, ninguno de ellos puede satisfacer $|u_n-0|<\varepsilon$. Por «Convergencia de una sucesión real», $u_n$ no converge a cero. La construcción toma una base $q$ fija y un solo índice $N$; no postula una elección simultánea para todas las bases. $\square$

La cota es deliberadamente suficiente para nuestros ejemplos: si los términos de otra sucesión tienen magnitud al menos $u_n$ eventualmente, esa sucesión tampoco puede tender a cero.

### Proposición 24.3.3 — Realización de los cuatro comportamientos de los extremos
Para cada centro $c\in\mathbb R$ y cada real prescrito $r>0$ existen series de potencias de radio exactamente $r$ cuyos conjuntos de extremos convergentes son, respectivamente,

$$
\boxed{\varnothing,\quad\{c-r\},\quad\{c+r\},\quad\{c-r,c+r\}.}
\tag{24.3.7}
$$

Los cuatro ejemplos pueden elegirse mediante las sucesiones explícitas de coeficientes de la tabla; en ella $h:=1/r>0$ y todas las expresiones se interpretan en $\mathbb R$:

| Coeficientes $a_n$ | Extremo izquierdo $c-r$ | Extremo derecho $c+r$ |
|---|---|---|
| $h^n$ | diverge | diverge |
| $h^n/(n+1)$ | converge condicionalmente | diverge |
| $(-1)^nh^n/(n+1)$ | diverge | converge condicionalmente |
| $h^n/((n+1)(n+2))$ | converge absolutamente | converge absolutamente |

**Demostración.**
**1. Existencia de las sucesiones y convergencia interior.** Cada coeficiente está dado por operaciones reales únicas, potencias naturales e índices naturales de denominador estrictamente positivo. La Separación sobre el conjunto existente $\mathbb N\times\mathbb R$ determina un grafo funcional total para cada una de las cuatro sucesiones; no se escoge una familia arbitraria de coeficientes. Fijemos un punto $x$ y pongamos $z:=(x-c)/r$. La identidad de potencias de productos demostrada en (24.1.13) transforma los términos en $z^n$, $z^n/(n+1)$, $(-1)^nz^n/(n+1)$ y $z^n/((n+1)(n+2))$, respectivamente. Si $|z|<1$, sus magnitudes están acotadas por $|z|^n$, pues todos los denominadores son al menos $1$. La serie geométrica converge por «Convergencia y suma de la serie geométrica para $»; el criterio de comparación «Criterio de comparación directa» y «La convergencia absoluta implica convergencia ordinaria» dan convergencia absoluta en los cuatro casos.

**2. Divergencia exterior y radio exacto.** Si $|z|=:q>1$, las magnitudes de los cuatro términos son, respectivamente,

$$
q^n,\qquad\frac{q^n}{n+1},\qquad
\frac{q^n}{n+1},\qquad\frac{q^n}{(n+1)(n+2)}.
$$

Todas son mayores o iguales que $u_n=q^n/((n+1)(n+2))>0$. Según «Una progresión geométrica supera a un denominador cuadrático», existe una cola sobre la cual $u_n\ge\delta$ para un real fijo $\delta>0$. Ninguna de las cuatro sucesiones de términos puede tender a cero. Por la condición necesaria «Condición necesaria de convergencia: el término general tiende a cero», las cuatro series divergen en todo punto con $|x-c|>r$.

Ya sabemos que los cuatro conjuntos de distancias admitidas contienen todo $d<r$, porque los puntos $c+d$ convergen absolutamente, y no contienen distancia alguna $d>r$. Por tanto son conjuntos no vacíos y acotados, y su supremo es $r$: si $b<r$ fuese cota superior, el punto medio de $\max\{b,0\}$ y $r$ sería una distancia admitida superior a $b$. La definición «Radio finito y radio infinito» prueba, para cada plantilla, $R(a,c)=r$, independientemente de lo que suceda en $d=r$. Así evitamos deducir circularmente el radio a partir de los ejemplos fronterizos.

**3. Evaluación de los extremos.** Por «Reducción de los extremos a series numéricas y simetría de la convergencia absoluta», basta estudiar la serie de los valores $b_n=a_nr^n$ y su versión alternada.

- **Ninguno.** Para $a_n=h^n$ tenemos $b_n=1$ y $(-1)^nb_n=(-1)^n$. Los términos de ambas series no tienden a cero; ambas divergen por «Condición necesaria de convergencia: el término general tiende a cero».
- **Sólo el izquierdo.** Para $a_n=h^n/(n+1)$ tenemos $b_n=1/(n+1)$ y la serie armónica diverge por «La condición $a_n\to0$ no es suficiente: la serie armónica». En el extremo izquierdo aparece la armónica alternada $\sum(-1)^n/(n+1)$, que converge condicionalmente por «La serie armónica alternada converge condicionalmente».
- **Sólo el derecho.** Para $a_n=(-1)^nh^n/(n+1)$, en el extremo derecho aparece la armónica alternada y en el izquierdo $(-1)^{2n}/(n+1)=1/(n+1)$, por inducción elemental de paridad de potencias. El primero converge condicionalmente y el segundo diverge por los mismos resultados cerrados.
- **Ambos.** Para $a_n=h^n/((n+1)(n+2))$ tenemos $b_n=1/((n+1)(n+2))$ y la identidad algebraica

  $$
  \frac1{(n+1)(n+2)}=\frac1{n+1}-\frac1{n+2}.
  \tag{24.3.8}
  $$

  Una inducción finita sobre $N$ demuestra que las sumas parciales son $1-1/(N+2)$. Por «Los recíprocos de los numerales positivos tienden a cero», $1/(N+2)\to0$ (es una cola de los recíprocos de numerales positivos); así la serie no negativa converge a $1$. Su convergencia en $c+r$ es absoluta. La igualdad de las series de magnitudes (24.3.3) prueba inmediatamente la convergencia absoluta también en $c-r$; no se afirma que sus sumas ordinarias sean iguales.

Quedan construidas las cuatro posibilidades (24.3.7) con radio prescrito $r$, mediante pruebas internas y sin recurrir a elección. $\square$

**Ejemplo adicional: convergencia condicional en ambos extremos.** La presencia de los dos extremos no exige convergencia absoluta. Fijemos $r>0$, $h=1/r$, y definamos por paridad

$$
a_{2k}=\frac{(-1)^kh^{2k}}{k+1},\qquad a_{2k+1}=0
\quad(k\in\mathbb N).
\tag{24.3.9}
$$

La descomposición par/impar y estas fórmulas dan una sucesión única por Separación. Para $|x-c|<r$, la magnitud del término de índice $n$ está acotada por $q^n$ con $q=|x-c|/r<1$; la comparación geométrica da convergencia absoluta. Para $q>1$, los términos de índice par tienen magnitud $q^{2k}/(k+1)\ge u_{2k}$, donde $u_n$ es la sucesión del lema anterior; como $u_n$ queda eventualmente por encima de un real positivo, los términos pares no tienden a cero. El radio es $r$ por el mismo argumento de supremo del paso 2. En $x=c\pm r$, los términos impares son cero y los pares valen $(-1)^k/(k+1)$, porque $(-1)^{2k}=1$. Las sumas parciales de índices $2K$ y $2K+1$ coinciden con la suma parcial de índice $K$ de la armónica alternada: ambas convergen por «La serie armónica alternada converge condicionalmente». Sus series de magnitudes tienen, en esos índices, exactamente las sumas parciales armónicas, que divergen por «La condición $a_n\to0$ no es suficiente: la serie armónica». Por tanto los dos extremos son condicionalmente convergentes. Esta construcción refina el cuarto patrón sin alterar el conjunto de extremos.

### Corolario 24.3.4 — Clasificación exhaustiva de los conjuntos de convergencia de radio finito positivo
Si una serie de potencias tiene radio real $R>0$, su conjunto de convergencia es exactamente uno de los cuatro conjuntos

$$
\boxed{
\begin{aligned}
&(c-R,c+R),\\
&[c-R,c+R),\\
&(c-R,c+R],\\
&[c-R,c+R].
\end{aligned}}
\tag{24.3.10}
$$

Para cualquier centro dado y cualquier radio positivo prescrito existen series que realizan cada una de esas cuatro formas.

**Demostración.**
Por «Forma exacta del conjunto de convergencia salvo los extremos», $C(a,c)=(c-R,c+R)\cup E_{a,c}$ y $E_{a,c}$ es un subconjunto del par $\{c-R,c+R\}$. La lógica clásica aplicada a la pertenencia de cada uno de sus dos elementos arroja únicamente las cuatro posibilidades de (24.3.10). Son distintas porque $R>0$ implica $c-R<c+R$. La proposición anterior construyó, para cualquier $c$ y $r>0$, una serie de cada tipo. $\square$

**Conclusión y transición.** El radio gobierna las distancias estrictas y la convergencia absoluta interior; los dos extremos se resuelven mediante series numéricas específicas, no mediante una regla universal de pertenencia. La convergencia absoluta es simultánea en ambos extremos, mientras que la ordinaria puede ocurrir en ninguno, uno o los dos. A continuación investigaremos cómo calcular el radio a partir de los coeficientes mediante límites superiores y cómo obtener, con una cota geométrica uniforme, convergencia en intervalos cerrados estrictamente interiores. Todavía no se afirma convergencia uniforme en el intervalo abierto completo ni se autoriza diferenciación o integración término a término.
---
