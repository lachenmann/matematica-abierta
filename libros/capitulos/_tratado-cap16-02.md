## 16.2. Criterio secuencial y alcance fundacional {#sec-ta-16-2}

Una sucesión convierte la aproximación a $a$ en una lista indexada por los naturales. Si se dispone de esa lista, la definición $\varepsilon$–$\delta$ controla todas sus imágenes suficientemente avanzadas. El problema lógico surge al invertir el razonamiento: que exista **algún** punto infractor para cada radio no significa que esté dada una función que elija simultáneamente todos esos puntos. Mantendremos separadas ambas operaciones.

En toda la sección, $D\subseteq\mathbb R$, $f:D\to\mathbb R$, $a\in\operatorname{Acc}(D)$ y $L\in\mathbb R$. Una sucesión real $s=(s_n)_{n\in\mathbb N}$ será *admisible para aproximarse a $a$ a través de $D$* cuando

$$
\forall n\in\mathbb N\ (s_n\in D\setminus\{a\})
\quad\text{y}\quad s_n\to a.
$$

Es una descripción local, no un nuevo tipo de límite: garantiza que $f(s_n)$ está definido y que nunca se utiliza el valor puntual $f(a)$. Para una sucesión así, el grafo de $s:\mathbb N\to\mathbb R$ tiene su recorrido contenido en $D$. Conservando ese grafo y declarando el codominio $D$, obtenemos una función bien tipada $s_D:\mathbb N\to D$. La composición $f\circ s_D:\mathbb N\to\mathbb R$ tiene por términos exactamente $f(s_n)$; no requiere elegir valores ni confunde funciones con distintos codominios.

### Proposición 16.2.1 — El límite funcional controla toda sucesión admisible
Si

$$
\lim_{\substack{x\to a\\x\in D}}f(x)=L,
$$

entonces, para **toda** sucesión real $(s_n)$ tal que $s_n\in D\setminus\{a\}$ para cada $n$ y $s_n\to a$, se tiene

$$
\boxed{f(s_n)\to L.}
$$

**Demostración.**
Fijemos una sucesión admisible $s$ y un $\varepsilon>0$. Por la hipótesis funcional existe $\delta>0$ tal que, para cada $x\in D$,

$$
0<|x-a|<\delta\quad\Longrightarrow\quad |f(x)-L|<\varepsilon.
$$

Como $s_n\to a$, la definición secuencial Definición §13.3.1 — Convergencia de una sucesión real proporciona $N\in\mathbb N$ con $|s_n-a|<\delta$ para todo $n\ge N$. Además, $s_n\in D$ y $s_n\ne a$ para **todos** los índices, así que $0<|s_n-a|<\delta$ si $n\ge N$. Sustituir $x=s_n$ en la implicación funcional da $|f(s_n)-L|<\varepsilon$ para toda esa cola. Ésta es exactamente la definición de $f(s_n)\to L$. La sucesión de imágenes existe por la composición tipada $f\circ s_D$ y ningún argumento ha seleccionado una nueva sucesión. ∎

> **Hipótesis indispensable.** Si permitiésemos $s_n=a$ y $a\in D$, la sucesión constante $s_n=a$ pondría a prueba $f(a)$, que la definición de límite excluye. La restricción $s_n\ne a$ no puede omitirse sin imponer una condición adicional acerca del valor puntual.


### Lema 16.2.2 — La falla del límite produce conjuntos de infractores, no automáticamente una sucesión
Utilicemos la escala positiva $\eta_n=(\nu_{\mathbb R}(S(n)))^{-1}$ de Lema §15.8.1 — Una escala numerable cofinal de radios positivos. Las siguientes afirmaciones son equivalentes:

1. $L$ **no** es límite de $f$ en $a$ a través de $D$.
2. Existe $\varepsilon_0>0$ tal que, para cada $n\in\mathbb N$, el conjunto

   $$
   E_n:=\{x\in D:0<|x-a|<\eta_n\ \land\ |f(x)-L|\ge\varepsilon_0\}
   $$

   es no vacío.

Para cada $\varepsilon_0$ fijado, $(E_n)_{n\in\mathbb N}$ es una familia determinada por una fórmula y tiene valores en $\mathcal P(\mathbb R)$.

**Demostración.**
Negar la relación cuantificada de Definición §16.1.2 — Límite real finito de una función relativo a su dominio, manteniendo $a\in\operatorname{Acc}(D)$, equivale en la lógica clásica admitida a

$$
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D:
0<|x-a|<\delta\ \land\ |f(x)-L|\ge\varepsilon_0.
$$

En efecto, negamos sucesivamente $\forall\varepsilon$, $\exists\delta$ y la implicación universal; la negación de $|f(x)-L|<\varepsilon_0$ es $|f(x)-L|\ge\varepsilon_0$ en el orden total real. Dado ese $\varepsilon_0$, cada $\eta_n$ es positivo, por lo que basta instanciar $\delta=\eta_n$ para concluir $E_n\ne\varnothing$.

Inversamente, supongamos que un $\varepsilon_0>0$ hace no vacíos todos los $E_n$. Fijado cualquier $\delta>0$, Lema §15.8.1 — Una escala numerable cofinal de radios positivos proporciona $n$ con $0<\eta_n<\delta$. La no vaciedad de **este único** $E_n$ entrega un $x\in D$ tal que

$$
0<|x-a|<\eta_n<\delta,
\qquad |f(x)-L|\ge\varepsilon_0.
$$

Por tanto ningún $\delta$ sirve para la tolerancia $\varepsilon_0$; $L$ no es límite. Los conjuntos $E_n$ existen por Separación sobre $D$; una regla funcional única $n\mapsto E_n$ se obtiene por Separación dentro de $\mathbb N\times\mathcal P(\mathbb R)$. **No** hemos afirmado que exista una función $n\mapsto x_n$ con $x_n\in E_n$: ése es el paso adicional que se examinará ahora. ∎

> **Comparación lógica.** El lema construye una familia de conjuntos no vacíos, $\forall n\ (E_n\ne\varnothing)$. Para contradecir un criterio secuencial necesitamos una sucesión de sus elementos, $\exists s\ \forall n\ (s_n\in E_n)$. La segunda afirmación no se obtiene por mera reordenación de cuantificadores.


### Teorema 16.2.3 — Criterio secuencial con enumeración del dominio
Supongamos **dada una sobreyección** $e:\mathbb N\to D$. Entonces las siguientes condiciones son equivalentes:

$$
\boxed{\lim_{\substack{x\to a\\x\in D}}f(x)=L}
$$

y

$$
\boxed{\begin{gathered}
\text{para toda sucesión }s\in\mathbb R^{\mathbb N}\text{ con}\\
\forall n\ (s_n\in D\setminus\{a\})\text{ y }s_n\to a,\\
f(s_n)\to L.
\end{gathered}}
$$

La enumeración $e$ es un **dato del enunciado**; no se supone que cualquier subconjunto de $\mathbb R$ tenga una.

**Demostración.**
La primera condición implica la segunda por Proposición §16.2.1 — El límite funcional controla toda sucesión admisible sin utilizar $e$. Para la recíproca razonaremos por contradicción. Si $L$ no fuese límite, Lema §16.2.2 — La falla del límite produce conjuntos de infractores, no automáticamente una sucesión suministraría $\varepsilon_0>0$ y conjuntos no vacíos $E_n$. Para cada $n$ formemos

$$
I_n:=\{k\in\mathbb N:e(k)\in E_n\}.
$$

Como $E_n\subseteq D$ es no vacío y $e$ es sobreyectiva, $I_n\ne\varnothing$. Por el buen orden de los naturales Teorema §1.6.13 — Principio de buen orden existe un mínimo **único** $k_n:=\min I_n$. La fórmula

$$
 k=k_n\iff k\in I_n\ \land\ \forall j\in I_n\ (k\le j)
$$

define funcionalmente los $k_n$; su grafo es un conjunto por Separación dentro de $\mathbb N\times\mathbb N$. Así, $s_n:=e(k_n)$ constituye una sucesión real con

$$
s_n\in D\setminus\{a\},\qquad
|s_n-a|<\eta_n,\qquad
|f(s_n)-L|\ge\varepsilon_0
\quad(n\in\mathbb N).
$$

Por el carácter cofinal de la escala $\eta_n$ (Lema §15.8.1 — Una escala numerable cofinal de radios positivos), $s_n\to a$: para cada $r>0$, finalmente $|s_n-a|<\eta_n<r$. Sin embargo, $f(s_n)$ **no** converge a $L$, porque la tolerancia $\varepsilon_0>0$ es infringida en todos sus términos. Hemos construido una sucesión admisible que contradice la segunda condición. Luego $L$ es el límite funcional. ∎

La prueba no exige una enumeración *computable*. Requiere una función matemática sobreyectiva ya proporcionada: el mínimo se toma en $\mathbb N$ y no en un subconjunto arbitrario de reales. La existencia de $a\in\operatorname{Acc}(D)$ asegura que el dominio es no vacío, pero por sí sola no proporciona $e$.


### Teorema 16.2.4 — Criterio secuencial universal bajo una hipótesis explícita
Supongamos, **sólo para este teorema**, el principio $\mathrm{CC}(\mathbb R)$ formulado en Teorema §15.8.9 — Formulaciones habituales bajo una hipótesis de elección explícita: toda sucesión de subconjuntos no vacíos de $\mathbb R$ admite una función que selecciona un elemento de cada uno. Entonces, para **cualquier** $D\subseteq\mathbb R$ y los datos $f,a,L$ fijados al comienzo de la sección, son equivalentes el límite funcional $L$ y la condición de convergencia de imágenes a lo largo de todas las sucesiones admisibles del Teorema 16.2.3.

**Demostración condicional.**
La implicación desde el límite funcional es Proposición §16.2.1 — El límite funcional controla toda sucesión admisible y no necesita la hipótesis adicional. Supongamos la condición secuencial y neguemos que $L$ sea el límite. El Lema 16.2.2 produce $\varepsilon_0>0$ y una función $n\mapsto E_n$ con $E_n\subseteq\mathbb R$ no vacío para cada $n$. **En este punto exacto** aplicamos $\mathrm{CC}(\mathbb R)$ a la familia $(E_n)$: obtenemos $s:\mathbb N\to\mathbb R$ con $s_n\in E_n$ para todo $n$. Las propias desigualdades que definen $E_n$ prueban $s_n\in D\setminus\{a\}$, $s_n\to a$ y $|f(s_n)-L|\ge\varepsilon_0$ para cada $n$. La última desigualdad impide $f(s_n)\to L$, en contradicción con la hipótesis secuencial. Concluimos que el límite funcional es $L$. ∎

**Estatuto fundacional.** El teorema está demostrado en la forma $\mathrm{CC}(\mathbb R)\Rightarrow\text{criterio secuencial universal}$. Su premisa adicional **no** se incorpora al contrato ZF. Tampoco se sustituye por la premisa «$D$ es abierto»: los conjuntos de infractores $E_n$ pueden ser arbitrarios cuando no se ha supuesto ninguna regularidad sobre $f$.


### Corolario 16.2.5 — Criterio incondicional sobre la copia racional canónica
Sea $D_{\mathbb Q}:=\jmath_{\mathbb Q}^{\mathbb R}[\mathbb Q]$ la imagen racional canónica. Para toda función $f:D_{\mathbb Q}\to\mathbb R$, todo $a\in\operatorname{Acc}(D_{\mathbb Q})$ y todo $L\in\mathbb R$ vale, **en ZF sin elección**, la equivalencia entre $\lim_{\substack{x\to a\\x\in D_{\mathbb Q}}}f(x)=L$ y la convergencia $f(s_n)\to L$ para cada sucesión $s_n\in D_{\mathbb Q}\setminus\{a\}$ con $s_n\to a$.

**Demostración.**
La enumeración racional canónica $e_{\mathbb Q}:\mathbb N\to\mathbb Q$ es sobreyectiva por Proposición §10.2.6 — Sobreyectividad de la enumeración racional canónica. La composición $h:=\jmath_{\mathbb Q}^{\mathbb R}\circ e_{\mathbb Q}:\mathbb N\to\mathbb R$ tiene recorrido exactamente $D_{\mathbb Q}$: cada punto de la imagen racional tiene alguna preimagen racional y ésta aparece en $e_{\mathbb Q}$. Conservando el grafo de $h$ y **reduciendo explícitamente su codominio** a $D_{\mathbb Q}$ obtenemos una sobreyección $e:\mathbb N\to D_{\mathbb Q}$. Aplicamos Teorema §16.2.3 — Criterio secuencial con enumeración del dominio a $e$. No se ha identificado $\mathbb Q$ con un subconjunto literal de $\mathbb R$ ni se ha utilizado elección. ∎

> **Ejemplo de contraste.** En el dominio $D_{\mathbb Q}$, la función que toma el valor $1$ para $x>0$ y $-1$ para $x\le0$ no tiene límite en $a=0$. Para cada $\delta>0$, la densidad racional proporciona puntos de ambos signos en la bola perforada de radio $\delta$. Si existiese un límite $L$, con $\varepsilon=1$ se exigirían simultáneamente $|1-L|<1$ y $|-1-L|<1$, lo cual contradice $2=|1-(-1)|\le |1-L|+|L+1|<2$. La enumeración del dominio permite convertir las infracciones en una sucesión admisible por el mínimo índice, sin escoger arbitrariamente infinitos puntos. Este ejemplo sólo utiliza los valores reales $\pm1$ y la copia racional tipada.


El criterio secuencial queda así disponible en tres niveles: una dirección incondicional para toda función; una equivalencia en dominios provistos de enumeración (en particular la imagen racional canónica); y una equivalencia universal **únicamente bajo la hipótesis declarada** $\mathrm{CC}(\mathbb R)$. En la siguiente unidad estudiaremos las reglas algebraicas de los límites directamente mediante desigualdades $\varepsilon$–$\delta$, sin depender de la recíproca secuencial condicional.
