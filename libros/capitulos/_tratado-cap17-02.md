## 17.2. Criterio secuencial y alcance fundacional {#sec-ta-17-2}

La definición puntual de continuidad cuantifica sobre todos los argumentos suficientemente próximos a $a$. Una sucesión particular que converge a $a$ sólo examina una colección numerable de esos argumentos. La primera dirección, de continuidad a convergencia de imágenes, es inmediata una vez respetados los tipos. La dirección inversa exige justificar que, ante una falla de continuidad, podemos **construir simultáneamente** una sucesión de puntos infractores; no confundiremos su existencia individual con la existencia de una función de selección.

En toda la sección fijamos $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$. Una sucesión *admisible para la continuidad* es una función $s:\mathbb N\to D$ tal que, al considerar sus términos como reales, $s_n\to a$. **Se admite $s_n=a$**, incluso para todos los índices: la condición buscada es $f(s_n)\to f(a)$ y la continuidad, a diferencia del límite del Capítulo 16, incluye el centro. Si inicialmente se da una sucesión $s:\mathbb N\to\mathbb R$ con $s_n\in D$, se obtiene la versión con codominio $D$ conservando su grafo y cambiando expresamente el codominio, no por identificación de funciones de tipos distintos.

### Proposición 17.2.1 — La continuidad preserva la convergencia de toda sucesión del dominio
Si $f$ es continua en $a$, entonces para toda sucesión $s:\mathbb N\to D$ que satisface $s_n\to a$, se tiene

$$
\boxed{f(s_n)\longrightarrow f(a).}
$$

**Demostración.**
Fijemos una sucesión admisible $s$ y una tolerancia $\varepsilon>0$. Por continuidad en $a$, existe $\delta>0$ tal que, para cada $x\in D$,

$$
|x-a|<\delta\quad\Longrightarrow\quad |f(x)-f(a)|<\varepsilon.
$$

La convergencia $s_n\to a$ aplicada a esta $\delta$ proporciona $N\in\mathbb N$ con $|s_n-a|<\delta$ para todo $n\ge N$. Como $s_n\in D$, podemos sustituir $x=s_n$ y obtener $|f(s_n)-f(a)|<\varepsilon$ para cada $n\ge N$. La sucesión de imágenes es la composición bien tipada $f\circ s:\mathbb N\to\mathbb R$. Ésta es precisamente su convergencia a $f(a)$. Los términos con $s_n=a$ satisfacen la estimación porque su error de salida es cero; no requieren una excepción. ∎

> **Comparación.** En §16.2.1 el criterio de límite exige $s_n\ne a$ para todos los índices, porque el límite perforado ignora $f(a)$. En continuidad hacemos exactamente lo contrario: permitimos todos los términos en $a$ y exigimos convergencia al valor $f(a)$.


### Lema 17.2.2 — Una falla de continuidad define una familia de conjuntos infractores
Tomemos la escala de radios $\eta_n=(\nu_{\mathbb R}(S(n)))^{-1}>0$ de Lema §15.8.1 — Una escala numerable cofinal de radios positivos. Las siguientes proposiciones son equivalentes:

1. $f$ no es continua en $a$.
2. Existe $\varepsilon_0>0$ tal que, para cada $n\in\mathbb N$, es no vacío el conjunto

   $$
   E_n:=\{x\in D:\ |x-a|<\eta_n\ \land\ |f(x)-f(a)|\ge\varepsilon_0\}.
   $$

Fijado $\varepsilon_0$, los $E_n$ forman una función $E:\mathbb N\to\mathcal P(\mathbb R)$ determinada por su fórmula. Cada infractor satisface automáticamente $x\ne a$.

**Demostración.**
Negar clásicamente la condición cuantificada de continuidad, conservando los datos fijos $a\in D$ y $f:D\to\mathbb R$, equivale a

$$
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D:\quad
|x-a|<\delta\ \land\ |f(x)-f(a)|\ge\varepsilon_0.
$$

En efecto, el fracaso de una implicación universal proporciona un argumento cercano cuya desigualdad de salida falla; el orden total transforma la negación de $|f(x)-f(a)|<\varepsilon_0$ en la desigualdad no estricta. Si fijamos ese $\varepsilon_0$ y ponemos $\delta=\eta_n$, la fórmula anterior produce al menos un elemento de $E_n$ para cada $n$.

Recíprocamente, supongamos no vacíos todos los $E_n$ para un mismo $\varepsilon_0>0$. Para cualquier $\delta>0$, la cofinalidad de Lema §15.8.1 — Una escala numerable cofinal de radios positivos entrega un índice $n$ tal que $0<\eta_n<\delta$. De la no vaciedad de **ese único** $E_n$ obtenemos un $x\in D$ con $|x-a|<\eta_n<\delta$ y $|f(x)-f(a)|\ge\varepsilon_0$. Ningún $\delta$ acredita continuidad para $\varepsilon_0$. Por Separación cada $E_n\subseteq D$ existe y su grafo funcional queda determinado por Separación en $\mathbb N\times\mathcal P(\mathbb R)$; no elegimos un elemento de todos ellos simultáneamente. Finalmente, $x=a$ no puede estar en $E_n$ porque $|f(a)-f(a)|=0<\varepsilon_0$. ∎

La distinción lógica es estricta: de $\forall n\ (E_n\ne\varnothing)$ no se infiere por simple intercambio de cuantificadores que exista $s:\mathbb N\to\mathbb R$ con $s_n\in E_n$ para todos los índices. En el próximo teorema construiremos tal sucesión cuando dispongamos de una enumeración del dominio.


### Teorema 17.2.3 — Criterio secuencial con enumeración dada del dominio
Supongamos **dada una sobreyección** $e:\mathbb N\to D$. Entonces son equivalentes:

$$
\boxed{f\text{ es continua en }a}
$$

y

$$
\boxed{\begin{gathered}
\text{para toda sucesión }s:\mathbb N\to D\text{ con }s_n\to a,\\
f(s_n)\to f(a).
\end{gathered}}
$$

La sobreyección es un dato adicional: no se declara enumerable cualquier subconjunto de la recta.

**Demostración.**
La implicación directa está probada en Proposición §17.2.1 — La continuidad preserva la convergencia de toda sucesión del dominio. Para la recíproca supongamos válida la condición sobre todas las sucesiones, pero que $f$ no es continua en $a$. Por Lema §17.2.2 — Una falla de continuidad define una familia de conjuntos infractores disponemos de $\varepsilon_0>0$ y de conjuntos no vacíos $E_n\subseteq D$, para cada $n$.

Definamos por Separación

$$
I_n:=\{k\in\mathbb N:e(k)\in E_n\}.
$$

La sobreyectividad de $e$ y la no vaciedad de $E_n$ garantizan $I_n\ne\varnothing$. El buen orden de $\mathbb N$ (Teorema §1.6.13 — Principio de buen orden) proporciona un único $k_n:=\min I_n$. La condición $k\in I_n\land\forall j\in I_n\,(k\le j)$ determina de manera funcional $k_n$ a partir de $n$, y su grafo existe por Separación en $\mathbb N\times\mathbb N$. Por tanto, $s_n:=e(k_n)$ define una función $s:\mathbb N\to D$ con

$$
|s_n-a|<\eta_n,
\qquad |f(s_n)-f(a)|\ge\varepsilon_0
\qquad(n\in\mathbb N).
$$

La escala $\eta_n$ tiende a cero por Lema §15.8.1 — Una escala numerable cofinal de radios positivos, luego $s_n\to a$. Sin embargo, su sucesión de imágenes no converge a $f(a)$: para la tolerancia fija $\varepsilon_0$, **ningún** término cumple $|f(s_n)-f(a)|<\varepsilon_0$. Esto contradice la hipótesis secuencial. Concluimos que $f$ es continua en $a$. La construcción utiliza la mínima posición en una enumeración dada, no un principio de elección sobre conjuntos arbitrarios. ∎

Este teorema comprende los puntos aislados sin una excepción: allí la continuidad es automática y cualquier sucesión del dominio que converja a $a$ acaba siendo constantemente $a$, al quedar confinada en una bola que sólo contiene ese punto del dominio.


### Teorema 17.2.4 — Criterio secuencial universal bajo elección numerable explícita
**Sólo bajo la hipótesis adicional** $\mathrm{CC}(\mathbb R)$ de Teorema §15.8.9 — Formulaciones habituales bajo una hipótesis de elección explícita —toda familia numerable de subconjuntos no vacíos de $\mathbb R$ admite una función selectora—, la equivalencia del Teorema 17.2.3 vale para **todo** $D\subseteq\mathbb R$, sin necesidad de proporcionar una enumeración de $D$.

**Demostración condicional.**
La continuidad implica la propiedad secuencial en ZF por Proposición §17.2.1 — La continuidad preserva la convergencia de toda sucesión del dominio. Para la otra dirección, supongamos que todas las sucesiones admisibles tienen imágenes convergentes a $f(a)$ y que, por contradicción, $f$ no es continua. Lema §17.2.2 — Una falla de continuidad define una familia de conjuntos infractores suministra $\varepsilon_0>0$ y la familia funcional $E:\mathbb N\to\mathcal P(\mathbb R)$ de conjuntos infractores no vacíos. **Exactamente aquí** aplicamos la premisa adicional $\mathrm{CC}(\mathbb R)$: existe $s:\mathbb N\to\mathbb R$ con $s_n\in E_n$ para todos los índices. Como $E_n\subseteq D$, reescribimos esta misma función con codominio $D$. Sus desigualdades definitorias dan $|s_n-a|<\eta_n$ y $|f(s_n)-f(a)|\ge\varepsilon_0$ para todo $n$. Así, $s_n\to a$ pero $f(s_n)\not\to f(a)$, contradicción. ∎

**Estatuto fundacional.** Lo demostrado es la implicación *condicional* $\mathrm{CC}(\mathbb R)\Rightarrow$ «criterio universal para dominios arbitrarios». El tratado **no adopta** esa premisa en ZF ni declara demostrada su recíproca sin hipótesis. La primera implicación, el caso de dominio enumerado y el caso racional canónico permanecen incondicionales.


### Corolario 17.2.5 — Criterio incondicional en la copia racional canónica
Sea $D_{\mathbb Q}:=\jmath_{\mathbb Q}^{\mathbb R}[\mathbb Q]\subseteq\mathbb R$. Para cualquier función $f:D_{\mathbb Q}\to\mathbb R$ y cualquier $a\in D_{\mathbb Q}$, la continuidad de $f$ en $a$ equivale, **en ZF sin elección**, a que $f(s_n)\to f(a)$ para toda sucesión $s:\mathbb N\to D_{\mathbb Q}$ que tienda a $a$.

**Demostración.**
Proposición §10.2.6 — Sobreyectividad de la enumeración racional canónica proporciona una sobreyección $e_{\mathbb Q}:\mathbb N\to\mathbb Q$. La composición $h=\jmath_{\mathbb Q}^{\mathbb R}\circ e_{\mathbb Q}:\mathbb N\to\mathbb R$ tiene recorrido exactamente $D_{\mathbb Q}$ por la definición de imagen directa. Conservando el grafo de $h$ y cambiando expresamente su codominio a $D_{\mathbb Q}$ obtenemos una sobreyección $e:\mathbb N\to D_{\mathbb Q}$. Aplicamos Teorema §17.2.3 — Criterio secuencial con enumeración dada del dominio. No hemos identificado $\mathbb Q$ con un subconjunto literal de $\mathbb R$ ni elegido representantes globalmente. ∎

**Lectura de cierre.** Sobre cualquier dominio podemos probar sin elección que continuidad implica preservación de todas las sucesiones convergentes. Para reconocer la continuidad a partir de sucesiones, una enumeración dada permite construir infractores mediante mínimos naturales; una hipótesis de elección numerable proporciona la misma selección sobre dominios arbitrarios, pero sólo de modo condicional. Esta distinción no afecta la definición puntual, que será la base de la caracterización mediante preimágenes de abiertos en §17.3.
