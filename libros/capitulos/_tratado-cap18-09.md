## 18.9. Teorema del valor intermedio y recorrido de una función continua {#sec-ta-18-9}

La sección anterior establece una propiedad estructural de la imagen: si el dominio considerado es un intervalo y la función es continua, el conjunto de sus valores también es un intervalo. Traduciremos ahora esa afirmación sobre conjuntos a su forma cuantificada: entre dos valores alcanzados no puede faltar ninguno de los valores intermedios. El punto donde se alcanza el valor buscado podrá localizarse dentro del segmento que une los dos argumentos originales; no necesitamos suponer que todo el dominio sea cerrado, acotado o compacto.

### Teorema 18.9.1 — Teorema del valor intermedio en un intervalo
Sea $D\subseteq\mathbb R$, sea $f:D\to\mathbb R$ continua en $D$ y sea $I\subseteq D$ un intervalo. Para cualesquiera $u,v\in I$ y cualquier $y\in\mathbb R$ que satisfaga

$$
\min\{f(u),f(v)\}\le y\le\max\{f(u),f(v)\},
$$

existe $c\in I$ tal que $f(c)=y$. Más precisamente, poniendo $a:=\min\{u,v\}$ y $b:=\max\{u,v\}$, se puede exigir

$$
\boxed{\exists c\in[a,b]\subseteq I:\quad f(c)=y.}
$$

Los mínimos y máximos de estas fórmulas corresponden a pares concretos de reales, definidos por comparación en el orden total; no se invoca un teorema de existencia de extremos sobre conjuntos arbitrarios. No se presupone que $u\le v$ ni que los valores de $f$ estén ordenados de la misma manera que sus argumentos.

**Demostración.**
**1. Reducimos el problema a un segmento existente.** Por la totalidad del orden real, uno de los puntos $u,v$ es el menor y el otro el mayor. Los reales $a$ y $b$ definidos en el enunciado satisfacen $a\le b$ y $\{a,b\}=\{u,v\}$. Como $u,v\in I$, también $a,b\in I$. La definición de intervalo Definición §18.7.3 — Intervalo como subconjunto convexo para el orden da

$$
J:=[a,b]\subseteq I\subseteq D.
$$

El segmento $J$ es asimismo un intervalo: si $s,t\in J$ y $s\le t$, todo $z\in[s,t]$ cumple $a\le s\le z\le t\le b$, y pertenece a $J$. Por tanto, el corolario Corolario §18.8.2 — La imagen continua de un intervalo es un intervalo, aplicado a la función dada $f:D\to\mathbb R$ y al intervalo $J$, afirma que $f[J]$ es un intervalo de $\mathbb R$. No hemos cambiado el codominio de $f$; su imagen se entiende en el sentido de Definición §0.6.9 — Imagen y preimagen.

**2. El valor intermedio pertenece a la imagen.** Puesto que $u,v\in J$, los dos reales $f(u),f(v)$ pertenecen a $f[J]$. Sean

$$
m:=\min\{f(u),f(v)\},\qquad M:=\max\{f(u),f(v)\}.
$$

De nuevo $m,M\in f[J]$ y $m\le M$. Al ser $f[J]$ un intervalo, su definición implica $[m,M]\subseteq f[J]$. La hipótesis $m\le y\le M$ muestra que $y\in f[J]$.

Por la definición de imagen directa, esta última pertenencia equivale a que exista un $c\in J$ con $f(c)=y$. Fijamos ese único testigo existencial y obtenemos $c\in[a,b]\subseteq I$, como se quería. Si $u=v$, entonces $a=b=u$, $m=M=f(u)$ y necesariamente $y=f(u)$; sirve $c=u$. Si $I=\varnothing$, no pueden darse las hipótesis $u,v\in I$ y el enunciado universal es vacuo. No se ha elegido un punto para cada $y$ ni se ha supuesto una función inversa. $\square$

**Interpretación.** El teorema afirma existencia, no unicidad: una función puede alcanzar el mismo valor varias veces, y no se presupone monotonía. La fortaleza de la conclusión $c\in[a,b]$ procede de aplicar la preservación de intervalos al segmento comprendido entre los argumentos, en lugar de aplicarla sólo al intervalo posiblemente mayor $I$.

### Corolario 18.9.2 — Formulación clásica sobre un intervalo cerrado
Sean $a,b\in\mathbb R$ con $a\le b$ y $f:[a,b]\to\mathbb R$ continua en su dominio. Para todo $y\in\mathbb R$ comprendido entre $f(a)$ y $f(b)$, incluidos ambos extremos, existe $c\in[a,b]$ tal que $f(c)=y$. Si $a<b$ y la desigualdad entre $y$ y ambos valores extremos es estricta, puede exigirse $c\in(a,b)$.

**Demostración.**
Apliquemos Teorema §18.9.1 — Teorema del valor intermedio en un intervalo con $D=I=[a,b]$, $u=a$ y $v=b$. Como $a\le b$, el segmento entre ambos argumentos es exactamente el dominio y obtenemos $c\in[a,b]$ con $f(c)=y$. Si además $a<b$ y

$$
\min\{f(a),f(b)\}<y<\max\{f(a),f(b)\},
$$

entonces $y\ne f(a)$ y $y\ne f(b)$, de modo que el punto obtenido no puede ser ni $a$ ni $b$. Resulta $a<c<b$. Para $a=b$, las dos cotas coinciden y la única posibilidad es $y=f(a)$, alcanzado en $c=a$; no afirmamos existencia de un punto en el intervalo abierto vacío. $\square$

La compacidad de $[a,b]$ no es necesaria para este corolario: la hipótesis de cerrado y acotado facilita la formulación habitual, pero el argumento usa únicamente continuidad y carácter intervalar del dominio. La compacidad sí entrará cuando queramos garantizar la existencia de valores mínimo y máximo sin conocer de antemano los valores que alcanza la función.

### Corolario 18.9.3 — Existencia de un cero cuando hay cambio estricto de signo
Sean $a,b\in\mathbb R$ con $a<b$ y $f:[a,b]\to\mathbb R$ continua. Si

$$
f(a)<0<f(b)\qquad\text{o bien}\qquad f(b)<0<f(a),
$$

entonces existe $c\in(a,b)$ tal que $f(c)=0$.

**Demostración.**
En cualquiera de los dos casos, el cero real se encuentra estrictamente entre $f(a)$ y $f(b)$. El apartado estricto de Corolario §18.9.2 — Formulación clásica sobre un intervalo cerrado, aplicado a $y=0$, proporciona $c\in(a,b)$ con $f(c)=0$. El punto es interior porque ninguno de los valores extremos es cero. Si sólo se conoce $f(a)\le0\le f(b)$, o la desigualdad invertida, el mismo corolario asegura un cero en $[a,b]$, pero éste puede ser un extremo: no se debe fortalecer ilegítimamente la conclusión. $\square$

### Corolario 18.9.4 — El recorrido sobre un intervalo cerrado es un intervalo cerrado alcanzado
Si $a\le b$ y $f:[a,b]\to\mathbb R$ es continua, existen reales $m\le M$ y puntos $x_-,x_+\in[a,b]$ tales que $f(x_-)=m$, $f(x_+)=M$ y

$$
\boxed{fa,b=[m,M].}
$$

La expresión $fa,b$ significa la imagen directa del conjunto $[a,b]$ por $f$, con los corchetes exteriores de Definición §0.6.9 — Imagen y preimagen; no es evaluación de $f$ sobre un par de argumentos. En particular, $m$ y $M$ son el mínimo y máximo efectivamente alcanzados de la función sobre el segmento, no necesariamente $f(a)$ y $f(b)$.

**Demostración.**
El intervalo $K:=[a,b]$ es compacto por Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto y no vacío porque $a\in K$. El teorema de Weierstrass Teorema §18.5.4 — Teorema del valor extremo: Weierstrass, aplicado a la función tipada $f:K\to\mathbb R$, proporciona dos puntos $x_-,x_+\in K$ tales que

$$
\forall x\in K:\qquad f(x_-)\le f(x)\le f(x_+).
$$

Pongamos $m:=f(x_-)$ y $M:=f(x_+)$. Como $x_+\in K$, la desigualdad con $x=x_+$ prueba $m\le M$. Para cualquier $z\in f[K]$ existe un $x\in K$ con $z=f(x)$, y las desigualdades obtenidas dan $m\le z\le M$. Por tanto,

$$
f[K]\subseteq[m,M].
$$

Para la inclusión contraria fijemos un $y\in[m,M]$. Los puntos $x_-,x_+$ pertenecen al intervalo $K$, y $y$ está entre sus imágenes. Aplicando Teorema §18.9.1 — Teorema del valor intermedio en un intervalo a esos dos argumentos, sin presuponer cuál de ellos es menor, obtenemos $c\in K$ con $f(c)=y$. Luego $y\in f[K]$ y $[m,M]\subseteq f[K]$. Las dos inclusiones demuestran la igualdad. Si $a=b$ o $f$ es constante, puede ocurrir $m=M$; entonces ambos conjuntos son el singleton $\{m\}$, sin ninguna excepción. Sólo se fijan los dos testigos de extremos y un testigo para el valor $y$ considerado, sin elección simultánea de preimágenes. $\square$

**Por qué importan las hipótesis.** La continuidad es indispensable para garantizar que no haya saltos de valores: en $[-1,1]$, la función que vale $-1$ para $x<0$ y $1$ para $x\ge0$ toma valores de ambos signos pero no toma el valor cero; no es continua en $0$. También importa el carácter intervalar del dominio: la restricción de la identidad al conjunto $\{-1,1\}$ es continua en su dominio relativo y alcanza $-1$ y $1$, pero no alcanza $0$, porque el dominio no contiene los puntos intermedios. Estos casos delimitan el teorema sin imponer hipótesis de monotonía.

**Transición.** La compacidad y la conexidad producen consecuencias globales distintas y complementarias: la primera garantiza extremos alcanzados y uniformidad; la segunda garantiza ausencia de huecos en las imágenes continuas. Juntas, sobre $[a,b]$, identifican exactamente la imagen como $[m,M]$. Con este resultado concluye el capítulo. Sus demostraciones han sido auditadas integralmente bajo ZF y lógica clásica; la equivalencia secuencial recíproca de §18.4 permanece condicionada a $\mathrm{CC}(\mathbb R)$, no adoptada. El Capítulo 19 iniciará la diferenciación desde el cociente incremental y la aproximación lineal local, sin anticipar los teoremas del valor medio reservados al Capítulo 20.
