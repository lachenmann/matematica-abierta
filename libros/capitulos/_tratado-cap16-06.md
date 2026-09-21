## 16.6. Límites infinitos y límites en infinito {#sec-ta-16-6}

En un límite finito se fija un número real $L$ y se exige que las imágenes permanezcan arbitrariamente próximas a él. Existen otros dos comportamientos que conviene distinguir. Primero, al aproximarse el argumento a un **punto real** $a$, los valores pueden superar cualquier cota real o descender por debajo de cualquiera de ellas. Segundo, podemos preguntar qué ocurre con los valores cuando el **argumento mismo** supera todas las cotas o desciende por debajo de todas ellas. No se trata de insertar dos números nuevos en el cuerpo $\mathbb R$: expresaremos cada fenómeno por una relación cuantificada entre una función y su dominio.

Una vez más, la disponibilidad de argumentos importa. Para evitar afirmaciones verdaderas por vacuidad, exigiremos acumulación del dominio en los puntos finitos y ausencia de cota en la dirección de aproximación cuando el argumento se aleja indefinidamente. La palabra «infinito» tendrá dos funciones sintácticas distintas: describir la dirección del argumento o describir que los valores no tienen cota en un sentido. Ninguna es una operación aritmética con $\infty$.

### Definición 16.6.1 — Dominios no acotados en una dirección
Sea $D\subseteq\mathbb R$. Diremos que $D$ es **no acotado superiormente** si

$$
\boxed{\forall R\in\mathbb R\ \exists x\in D:\ x>R.}
$$

Diremos que es **no acotado inferiormente** si

$$
\boxed{\forall R\in\mathbb R\ \exists x\in D:\ x<R.}
$$

Estas condiciones están formuladas en términos del orden real y coinciden con negar la existencia de una cota superior o inferior, respectivamente. No afirman que un elemento $x=+\infty$ o $x=-\infty$ pertenezca a $D$. Para cada umbral $R$ proporcionan un punto real del dominio; **no** proporcionan una sucesión de puntos simultáneamente seleccionados. Si $D$ no es acotado superiormente, toda cola $\{x\in D:x>R\}$ es no vacía; la afirmación inferior es simétrica. Dichas colas se obtienen por Separación sobre $D$, sin introducir una topología nueva.

> **Distinción con la acumulación.** El conjunto $(0,1)$ acumula en $0$ pero está acotado superior e inferiormente. El conjunto de números naturales reales $\nu_{\mathbb R}[\mathbb N]$ no es acotado superiormente, pero no tiene por ello un punto real de acumulación dado. Acercarse a un punto y abandonar toda región acotada son condiciones diferentes.


### Definición 16.6.2 — Límite infinito en un punto real
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in\operatorname{Acc}(D)$. Diremos que **$f$ crece sin cota al aproximarse $x$ a $a$ a través de $D$** si

$$
\boxed{\forall M\in\mathbb R\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ f(x)>M.}
\tag{16.6+}
$$

Diremos que **$f$ decrece sin cota** en ese régimen si

$$
\boxed{\forall M\in\mathbb R\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ f(x)<M.}
\tag{16.6-}
$$

En las dos relaciones, $M$ es una cota real arbitraria, y $\delta$ puede depender de ella pero no del argumento $x$. El centro se excluye incluso si $a\in D$. La condición $a\in\operatorname{Acc}(D)$ garantiza que cada vecindad perforada contiene argumentos del dominio: las desigualdades no son universalmente verdaderas por ausencia de puntos. Cuando se desea estudiar un solo lado, se aplica la misma definición a $f\upharpoonright D_a^-$ o $f\upharpoonright D_a^+$, **sólo si** dicho lado acumula, conforme a §16.5.

Estas relaciones no tienen «valor» en $\mathbb R$. No se introduce la expresión $|f(x)-\infty|$ ni una supuesta distancia a infinito; la definición utiliza exclusivamente las desigualdades reales $f(x)>M$ o $f(x)<M$.


### Definición 16.6.3 — Límite finito cuando el argumento tiende a infinito
Sean $f:D\to\mathbb R$ y $L\in\mathbb R$. Si $D$ es no acotado superiormente, diremos que **$f$ tiene límite finito $L$ cuando el argumento tiende a infinito positivo** si

$$
\boxed{\forall\varepsilon>0\ \exists R\in\mathbb R\ \forall x\in D:\quad
x>R\ \Longrightarrow\ |f(x)-L|<\varepsilon.}
\tag{16.6F+}
$$

Si $D$ es no acotado inferiormente, diremos que **$f$ tiene límite finito $L$ cuando el argumento tiende a infinito negativo** si

$$
\boxed{\forall\varepsilon>0\ \exists R\in\mathbb R\ \forall x\in D:\quad
x<R\ \Longrightarrow\ |f(x)-L|<\varepsilon.}
\tag{16.6F-}
$$

El umbral $R$ es un número real que depende de la precisión $\varepsilon$. No representa un índice natural y no ha de ser positivo: si conviene imponer además $R>0$ para el primer caso o $R<0$ para el segundo, podemos sustituirlo por un umbral más extremo sin perder la propiedad. La no acotación del dominio es una hipótesis previa indispensable: una función sobre un conjunto acotado superiormente satisfaría la implicación de (16.6F+) para **todo** $L$ eligiendo un umbral por encima del dominio, lo que destruye la unicidad.


### Definición 16.6.4 — Límite infinito cuando el argumento tiende a infinito
Sea $f:D\to\mathbb R$. Si $D$ no es acotado superiormente, distinguimos las dos afirmaciones

$$
\boxed{\forall M\in\mathbb R\ \exists R\in\mathbb R\ \forall x\in D:
\quad x>R\Longrightarrow f(x)>M,}
\tag{16.6I++}
$$

$$
\boxed{\forall M\in\mathbb R\ \exists R\in\mathbb R\ \forall x\in D:
\quad x>R\Longrightarrow f(x)<M.}
\tag{16.6I+-}
$$

La primera afirma que los valores crecen sin cota cuando el argumento crece sin cota; la segunda, que decrecen sin cota cuando el argumento crece sin cota. Si $D$ no es acotado inferiormente, se definen análogamente

$$
\boxed{\forall M\in\mathbb R\ \exists R\in\mathbb R\ \forall x\in D:
\quad x<R\Longrightarrow f(x)>M,}
\tag{16.6I-+}
$$

$$
\boxed{\forall M\in\mathbb R\ \exists R\in\mathbb R\ \forall x\in D:
\quad x<R\Longrightarrow f(x)<M.}
\tag{16.6I--}
$$

Los signos asociados al argumento y a la salida son **independientes**. Por ejemplo, una función puede tener valores cada vez más negativos cuando su argumento crece positivamente. En cada fórmula todos los objetos cuantificados son números reales; no se ha formado un cuerpo ampliado ni se han definido operaciones de suma, resta, producto o cociente con símbolos infinitos.


### Notación 16.6.5 — Escrituras de los límites en infinito
Activamos, exclusivamente como **abreviaturas de afirmaciones**, las siguientes escrituras:

$$
\lim_{\substack{x\to a\\x\in D}}f(x)=+\infty,
\qquad
\lim_{\substack{x\to a\\x\in D}}f(x)=-\infty,
$$

que significan, respectivamente, (16.6+) y (16.6-), siempre bajo $a\in\operatorname{Acc}(D)$; y

$$
\lim_{\substack{x\to+\infty\\x\in D}}f(x)=L,
\qquad
\lim_{\substack{x\to-\infty\\x\in D}}f(x)=L,
$$

que significan (16.6F+) y (16.6F-), con la correspondiente no acotación de $D$. Finalmente, las cuatro escrituras obtenidas al sustituir $L$ por $+\infty$ o $-\infty$ en estas últimas expresiones corresponden, en orden, a (16.6I++), (16.6I+-), (16.6I-+) y (16.6I--). Los límites infinitos laterales $x\to a^-$ o $x\to a^+$ se interpretan aplicando (16.6+) o (16.6-) al dominio lateral **activo**.

En estas expresiones, el signo «$=$» forma parte de una **notación proposicional convencional**: la fórmula entera afirma una propiedad cuantificada y no representa la igualdad entre un número real y un objeto $+\infty$ o $-\infty$. Cuando escribimos $\lim f=L$ con $L\in\mathbb R$, en cambio, invocamos las definiciones de límite finito. No admitiremos a partir de aquí operaciones formales como $+\infty-(+\infty)$, ni límites obtenidos aplicando reglas algebraicas de §16.3 a expresiones que no tienen límites reales.


### Teorema 16.6.6 — Unicidad e incompatibilidad de los regímenes de límite
Fijemos $f:D\to\mathbb R$ y **uno** de estos regímenes admisibles: $x\to a$ con $a\in\operatorname{Acc}(D)$; $x\to+\infty$ con $D$ no acotado superiormente; o $x\to-\infty$ con $D$ no acotado inferiormente. Entonces:

1. En ese régimen puede existir **a lo sumo un límite finito** $L\in\mathbb R$.
2. Un límite finito es incompatible tanto con la afirmación de límite $+\infty$ como con la de límite $-\infty$.
3. Las afirmaciones de límite $+\infty$ y de límite $-\infty$ son incompatibles entre sí.

Estos enunciados comparan *afirmaciones*, no elementos de un supuesto conjunto de valores extendidos.

**Demostración.**
**Unicidad finita.** Para $x\to a$, es Teorema §16.1.4 — Unicidad del límite finito. Si el argumento tiende a $+\infty$ y suponemos dos límites finitos distintos $L,N$, definamos $d:=|L-N|>0$ y $\varepsilon:=d/3$. Cada límite proporciona un umbral, $R_L$ y $R_N$. Como $D$ no es acotado superiormente, existe **un** $x\in D$ con $x>\max\{R_L,R_N\}$. Aplicando las dos desigualdades a ese punto y usando la triangular,

$$
d=|L-N|\le |L-f(x)|+|f(x)-N|<2d/3<d,
$$

contradicción. Si $x\to-\infty$, elegimos en cambio un solo $x<\min\{R_L,R_N\}$; el resto es idéntico.

**Incompatibilidad con un límite finito.** Supongamos que el límite finito es $L$. Tomando $\varepsilon=1$, obtenemos, en la zona suficientemente próxima o en la cola suficientemente extrema, las dos cotas $L-1<f(x)<L+1$. Si además se afirmara límite $+\infty$, el umbral de salida $M=L+2$ proporcionaría en otra zona del mismo régimen la cota $f(x)>L+2$. Intersecamos las dos zonas tomando el mínimo de sus radios cuando $x\to a$, el máximo de sus umbrales cuando $x\to+\infty$, o el mínimo de sus umbrales cuando $x\to-\infty$. La acumulación o no acotación correspondiente proporciona un punto **perteneciente a esa zona común**. En él tendríamos simultáneamente $f(x)<L+1$ y $f(x)>L+2$, imposible. Para un supuesto límite $-\infty$ elegimos $M=L-2$ y obtenemos $f(x)>L-1$ y $f(x)<L-2$, igualmente imposible.

**Incompatibilidad de los dos signos infinitos.** Instanciemos las dos afirmaciones con el mismo umbral de salida $M=0$. Después de combinar las dos zonas como antes y elegir un único punto del dominio dentro de la zona común, deduciríamos a la vez $f(x)>0$ y $f(x)<0$. La contradicción concluye la prueba. Sólo se extrae un número finito de testigos para cada comparación; no hay selección numerable. ∎

> **Alcance exacto.** Dos límites tomados en regímenes *distintos* no tienen por qué coincidir. Por ejemplo, una función puede crecer sin cota por un lado y decrecer sin cota por el otro; el teorema no compara relaciones con dominios de aproximación diferentes.


### Proposición 16.6.7 — Localidad perforada y estabilidad en las colas
Sean $f,g:D\to\mathbb R$. Si existe $r>0$ tal que $f(x)=g(x)$ para cada $x\in D$ con $0<|x-a|<r$, entonces, siempre que $a\in\operatorname{Acc}(D)$, $f$ y $g$ satisfacen **exactamente las mismas** relaciones de límite finito y de límite $\pm\infty$ en $a$. Si $a\in D$, modificar sólo $f(a)$ no altera ninguna de esas afirmaciones.

Si $D$ no es acotado superiormente y existe $R_0\in\mathbb R$ tal que $f(x)=g(x)$ para cada $x\in D$ con $x>R_0$, ambas funciones satisfacen exactamente las mismas afirmaciones de límite finito y de límite $\pm\infty$ cuando $x\to+\infty$. Para el sentido negativo basta sustituir $x>R_0$ por $x<R_0$ y exigir que $D$ no sea acotado inferiormente.

**Demostración.**
Para límites finitos en el punto $a$, la primera conclusión es Proposición §16.1.5 — Carácter local del límite y libertad en el valor puntual. Para límite $+\infty$ o $-\infty$ en $a$, fijemos un umbral real $M$. Supongamos que $f$ satisface la relación y tomemos un radio $\delta_f>0$ que funciona para $M$. Si $x\in D$ cumple $0<|x-a|<\min\{\delta_f,r\}$, entonces $g(x)=f(x)$, de modo que se transfiere la desigualdad $>M$ o $<M$. La implicación inversa intercambia los papeles de $f$ y $g$.

Para $x\to+\infty$, fijemos una precisión $\varepsilon>0$ si la salida prevista es finita, o una cota $M\in\mathbb R$ si es infinita. La relación válida para $f$ proporciona un umbral $R_f$. Si $x\in D$ y $x>\max\{R_f,R_0\}$, se aplica la estimación para $f$ y, por la igualdad de las dos funciones en esa cola, también para $g$. El argumento es simétrico y sirve para las tres clases de salida. En el régimen $x\to-\infty$ se utiliza $\min\{R_f,R_0\}$, obteniendo idéntica conclusión. Ningún paso exige que el centro pertenezca al dominio ni que la coincidencia valga en todo $D$. ∎


### Teorema 16.6.8 — Reducir un límite en infinito a un límite unilateral en cero
**Caso positivo.** Sea $D\subseteq\mathbb R$ no acotado superiormente y $f:D\to\mathbb R$. Definamos por Separación

$$
D_+:=\{x\in D:x>0\},\qquad
E_+:=\{t\in\mathbb R:t>0\ \land\ \exists x\in D_+\ (tx=1)\},
$$

y la función bien tipada $h_+:E_+\to\mathbb R$ dada por $h_+(t):=f(t^{-1})$. Entonces $0\in\operatorname{Acc}(E_+)$ y cada una de las tres equivalencias siguientes vale por separado:

$$
\boxed{\lim_{\substack{x\to+\infty\\x\in D}}f(x)=L
\iff \lim_{\substack{t\to0^+\\t\in E_+}}h_+(t)=L\quad(L\in\mathbb R),}
$$

$$
\boxed{\lim_{\substack{x\to+\infty\\x\in D}}f(x)=+\infty
\iff \lim_{\substack{t\to0^+\\t\in E_+}}h_+(t)=+\infty,}
$$

$$
\boxed{\lim_{\substack{x\to+\infty\\x\in D}}f(x)=-\infty
\iff \lim_{\substack{t\to0^+\\t\in E_+}}h_+(t)=-\infty.}
$$

**Caso negativo.** Si $D$ no es acotado inferiormente, definamos $D_-:=\{x\in D:x<0\}$,

$$
E_-:=\{t\in\mathbb R:t>0\ \land\ \exists x\in D_-\ (tx=-1)\},
\qquad h_-(t):=f(-t^{-1})\quad(t\in E_-).
$$

Entonces $0\in\operatorname{Acc}(E_-)$ y las mismas tres equivalencias valen sustituyendo, en los miembros izquierdos, $x\to+\infty$ por $x\to-\infty$ y, en los derechos, $E_+,h_+$ por $E_-,h_-$. Todos los límites de la derecha son límites laterales sobre dominios que efectivamente acumulan en cero.

**Demostración.**
Los conjuntos $D_+,E_+,D_-,E_-$ existen por Separación sobre $D$ o $\mathbb R$. Cada $t\in E_+$ es no nulo y tiene algún $x\in D_+$ con $tx=1$; por unicidad del inverso del cuerpo, $x=t^{-1}\in D_+$. De modo análogo, $t\in E_-$ implica $-t^{-1}\in D_-$. Así, $h_+$ está definida exactamente sobre $E_+$ y tiene codominio real; el grafo $\{\langle t,f(t^{-1})\rangle:t\in E_+\}$ existe como subconjunto funcional de $E_+\times\mathbb R$. Para el caso negativo se sustituye $t^{-1}$ por $-t^{-1}$; tampoco se divide por cero.

**Acumulación en cero.** Dado $r>0$, el carácter no acotado superior de $D$ permite tomar **un** $x\in D$ con $x>\max\{1,r^{-1}\}$. En particular, $x\in D_+$ y $t:=x^{-1}\in E_+$ cumple $0<t<r$; por Lema §16.1.1 — Acumulación y aproximación perforada, $0\in\operatorname{Acc}(E_+)$. Para el caso negativo, la no acotación inferior permite un $x\in D$ con $x< -\max\{1,r^{-1}\}$; entonces $t:=-x^{-1}>0$, $-t^{-1}=x\in D_-$ y $0<t<r$. Concluimos asimismo $0\in\operatorname{Acc}(E_-)$, sin formar ninguna sucesión de testigos.

**Conversión para $+\infty$ en el argumento.** El esquema de condición sobre la salida es $P(y,\theta)$, donde, según el caso, $P(y,\varepsilon)$ significa $|y-L|<\varepsilon$, $P(y,M)$ significa $y>M$, o $P(y,M)$ significa $y<M$. Las tres afirmaciones comparten exactamente el orden $\forall\theta\ \exists\text{umbral}\ \forall\text{argumento}$; los parámetros son reales y cada cuantificador conserva las restricciones de su definición.

Supongamos que la correspondiente afirmación se verifica para $f$ en $x\to+\infty$. Fijado su parámetro de salida, obtenemos $R\in\mathbb R$. Tomemos $\delta:=(|R|+1)^{-1}>0$. Si $t\in E_+$ y $0<t<\delta$, entonces $x=t^{-1}\in D_+$ y $x>|R|+1>R$, por lo que $P(f(x),\theta)$, es decir $P(h_+(t),\theta)$. Esto prueba el límite derecho en cero. Recíprocamente, si su afirmación en cero proporciona $\delta>0$, fijemos $R:=\delta^{-1}>0$. Para cada $x\in D$ con $x>R$, se tiene $x>0$ y $t:=x^{-1}\in E_+$ con $0<t<\delta$, luego $P(f(x),\theta)$: queda probado el límite al crecer el argumento.

**Conversión para $-\infty$.** Supongamos que la afirmación para $f$ entrega $R\in\mathbb R$ y tomemos $\delta:=(|R|+1)^{-1}$. Si $0<t<\delta$ y $t\in E_-$, entonces $x=-t^{-1}\in D_-$ cumple $x<-(|R|+1)<R$ y $P(h_-(t),\theta)$. Para la implicación inversa, dado $\delta>0$ pongamos $R:=-\delta^{-1}$. Si $x\in D$ y $x<R$, entonces $t:=-x^{-1}\in E_-$ satisface $0<t<\delta$, con lo que $P(f(x),\theta)$. Las transformaciones son recíprocas punto por punto; no requieren elección, ni una continuidad previamente definida, ni reglas algebraicas con infinitos. ∎

> **Interpretación.** El cambio $t=1/x$ para $x>0$ y $t=-1/x$ para $x<0$ transforma un extremo no acotado de la recta en un acercamiento **por la derecha** a cero. Se trata de una equivalencia entre relaciones con dominios precisos, no de asignar al «punto infinito» una coordenada real.


### Corolario 16.6.9 — Los dos comportamientos elementales del recíproco
Definamos $D_+:=\{x\in\mathbb R:x>0\}$ y $D_-:=\{x\in\mathbb R:x<0\}$, y consideremos las funciones $p:D_+\to\mathbb R$ y $n:D_-\to\mathbb R$ dadas por $p(x)=x^{-1}$ y $n(x)=x^{-1}$. Sus dominios son semirrectas definidas por desigualdades reales; no se construyen intervalos con un extremo infinito añadido al cuerpo. Entonces

$$
\boxed{\lim_{x\to0^+}p(x)=+\infty,\qquad
\lim_{x\to+\infty}p(x)=0,}
$$

$$
\boxed{\lim_{x\to0^-}n(x)=-\infty,\qquad
\lim_{x\to-\infty}n(x)=0.}
$$

**Demostración.**
Ambas semirrectas son subconjuntos de $\mathbb R$ por Separación. Dado $r>0$, los puntos $r/2$ y $-r/2$ prueban, respectivamente, acumulación por la derecha y por la izquierda en cero. Dado cualquier umbral real $R$, el punto $|R|+1$ pertenece a la semirrecta positiva y supera $R$, mientras que $-(|R|+1)$ pertenece a la negativa y es menor que $R$; por tanto sus dominios cumplen las respectivas condiciones de no acotación.

Fijemos $M\in\mathbb R$ y tomemos $\delta:=(|M|+1)^{-1}>0$. Para $x>0$ con $x<\delta$, la compatibilidad del orden con los recíprocos positivos da $p(x)=x^{-1}>|M|+1>M$. Para $x<0$ con $-\delta<x<0$, tenemos $0<-x<\delta$, de donde $(-x)^{-1}>|M|+1$ y $n(x)=-(-x)^{-1}<-(|M|+1)<M$. Quedan demostrados los dos límites infinitos en cero.

Finalmente, dada $\varepsilon>0$, tomemos $R:=\varepsilon^{-1}>0$. Si $x>R$, entonces $|p(x)-0|=x^{-1}<\varepsilon$. Si $x<-R$, entonces $|n(x)-0|=(-x)^{-1}<\varepsilon$. Son las dos relaciones definitorias de límite finito con argumentos no acotados. En todas estas expresiones se divide exclusivamente por reales no nulos. ∎


Los límites finitos, laterales e infinitos quedan ahora caracterizados por condiciones sobre argumentos del dominio, con sus hipótesis de acumulación o no acotación. La comparación de límites, sus operaciones algebraicas y la composición se justificaron sin identificar los símbolos de infinito con números reales. El Capítulo 17 estudiará la **continuidad**, que vincula estas nociones de límite con el valor de una función en el punto cuando éste pertenece a su dominio.
