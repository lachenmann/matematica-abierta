## 19.8. Derivadas laterales y dependencia del dominio {#sec-ta-19-8}

La definición de §19.1 permite derivar en el extremo de un intervalo: exige un límite de pendientes sobre todos los puntos disponibles del dominio, aunque sólo se aproximen por un lado. Para distinguir esa situación de un punto interior, reutilizaremos los dominios laterales y sus límites, ya construidos en §16.5. Una derivada lateral no será una derivada definida por una condición vacía: exigiremos acumulación desde el lado correspondiente. Esta distinción prepara los extremos locales y los teoremas del valor medio, cuyo estudio pertenece al capítulo siguiente.

### Definición 19.8.1 — Derivabilidad por la izquierda y por la derecha
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$. Escribimos, conforme a Definición §16.5.1 — Dominios laterales de aproximación,

$$
D_a^-:=\{x\in D:x<a\},\qquad D_a^+:=\{x\in D:a<x\},
\qquad D_a=D\setminus\{a\}=D_a^-\cup D_a^+.
$$

Si $a\in\operatorname{Acc}(D_a^-)$, diremos que $f$ es *derivable por la izquierda en $a$* cuando existe $L_-\in\mathbb R$ tal que

$$
\lim_{\substack{x\to a^-\\x\in D}}q_{f,a}(x)
=\lim_{\substack{x\to a\\x\in D_a^-}}
(q_{f,a}\upharpoonright D_a^-)(x)=L_-.
$$

Si $a\in\operatorname{Acc}(D_a^+)$, diremos que $f$ es *derivable por la derecha en $a$* cuando existe $L_+\in\mathbb R$ tal que

$$
\lim_{\substack{x\to a^+\\x\in D}}q_{f,a}(x)
=\lim_{\substack{x\to a\\x\in D_a^+}}
(q_{f,a}\upharpoonright D_a^+)(x)=L_+.
$$

El cociente $q_{f,a}:D_a\to\mathbb R$ está definido en §19.1; sus restricciones laterales son funciones tipadas a $\mathbb R$. Las igualdades anteriores son instancias del límite finito de Definición §16.5.3 — Límites finitos por la izquierda y por la derecha, cuya notación sólo se activa si el lado acumula. Ni $q_{f,a}(a)$ ni una derivada lateral del lado vacío tienen significado. El valor central $f(a)$ sí es imprescindible en el numerador.

### Proposición 19.8.2 — Criterios cuantificados y unicidad lateral
Cuando $a\in\operatorname{Acc}(D_a^-)$, la derivada izquierda existe y vale $L_-$ si y sólo si

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\quad
0<a-x<\delta\ \Longrightarrow\quad
\left|\frac{f(x)-f(a)}{x-a}-L_-\right|<\varepsilon.}
$$

Cuando $a\in\operatorname{Acc}(D_a^+)$, la derivada derecha existe y vale $L_+$ si y sólo si

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\quad
0<x-a<\delta\ \Longrightarrow\quad
\left|\frac{f(x)-f(a)}{x-a}-L_+\right|<\varepsilon.}
$$

El número de cada lado, cuando existe, es único; los dos valores no tienen por qué coincidir.

**Demostración.**
Apliquemos Proposición §16.5.4 — Caracterizaciones unilaterales $\varepsilon$–$\delta$ a la función $q_{f,a}:D_a\to\mathbb R$. Sus dominios laterales relativos a $a$ son exactamente $D_a^-$ y $D_a^+$, pues $a$ ya está excluido. En el lado izquierdo, $0<a-x<\delta$ equivale a $x\in D_a^-$ y $0<|x-a|<\delta$; la equivalencia derecha se obtiene sustituyendo $a-x$ por $x-a$. La caracterización de límites laterales da las dos condiciones anunciadas, sin evaluar el cociente en $a$. Para cada lado activo, Teorema §16.1.4 — Unicidad del límite finito aplicado a la correspondiente restricción del cociente garantiza que dos valores de límite necesariamente coinciden. No existe razón para identificar entre sí los límites de dos funciones restringidas a dominios distintos. $\square$

### Notación 19.8.3 — Derivadas laterales
Si existe la derivada del lado indicado, la designamos por $f'_-(a)$ o $f'_+(a)$, respectivamente. Los subíndices $-$ y $+$ describen la dirección de aproximación, no el signo del número obtenido: ambas derivadas pueden ser positivas, negativas o nulas. Si un lado no acumula, no se le asigna derivada ni un símbolo con valor ficticio. Esas notaciones se refieren siempre al dominio de la función $f:D\to\mathbb R$ en cuestión.

### Teorema 19.8.4 — Reconstrucción de la derivada desde los lados activos
Sean $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Entonces $f$ es derivable en $a$ si y sólo si existen todas las derivadas laterales correspondientes a los lados que acumulan en $a$, y tienen un valor común $L$. Precisamente:

1. Si ambos lados acumulan, $f'(a)$ existe si y sólo si existen $f'_-(a)$ y $f'_+(a)$ y son iguales; entonces $f'(a)=f'_-(a)=f'_+(a)$.
2. Si sólo acumula el izquierdo, $f'(a)$ existe si y sólo si existe $f'_-(a)$, y ambos valores coinciden.
3. Si sólo acumula el derecho, $f'(a)$ existe si y sólo si existe $f'_+(a)$, y ambos valores coinciden.

No aparece un cuarto caso, pues Lema §16.5.2 — La acumulación procede de al menos un lado descarta que ambos lados carezcan de acumulación cuando $a\in\operatorname{Acc}(D)$.

**Demostración.**
La función $q_{f,a}$ tiene dominio $D_a$ y, por Lema §19.1.2 — Perforar el dominio preserva la acumulación en el centro, $a\in\operatorname{Acc}(D_a)$. La identidad conjuntista de Definición §16.5.1 — Dominios laterales de aproximación muestra que los dominios laterales de $D_a$ en $a$ son exactamente $D_a^-$ y $D_a^+$. Para un $L\in\mathbb R$ fijado, el criterio completo de límites Teorema §16.5.6 — Criterio completo para dominios de uno o dos lados, aplicado a esta función $q_{f,a}$, afirma que

$$
\lim_{\substack{x\to a\\x\in D_a}}q_{f,a}(x)=L
$$

si y sólo si cada lado activo tiene límite lateral igual a $L$. La definición Definición §19.1.3 — Derivabilidad en un punto identifica la existencia del límite de la izquierda con la derivabilidad de $f$, mientras que Definición §19.8.1 — Derivabilidad por la izquierda y por la derecha y la notación anterior identifican los límites laterales con las derivadas laterales. La unicidad bilateral Proposición §19.1.4 — Unicidad y criterio cuantificado de la derivada y la unicidad lateral Proposición §19.8.2 — Criterios cuantificados y unicidad lateral permiten escribir sus igualdades numéricas.

En el caso de dos lados activos, Teorema §16.5.5 — Reconstrucción bilateral cuando ambos lados acumulan reconstruye el límite a partir de los dos valores coincidentes. Si sólo uno acumula, Teorema §16.5.6 — Criterio completo para dominios de uno o dos lados combina el radio correspondiente con un radio que excluye los puntos del lado inactivo; éste existe por la negación clásica del criterio de acumulación y se toma un mínimo de dos números, no una elección de infinitos testigos. Lema §16.5.2 — La acumulación procede de al menos un lado asegura que los tres casos expuestos son exhaustivos. $\square$

**Interpretación.** La palabra «bilateral», aplicada al límite que define $f'(a)$, significa «respecto de todo $D_a$». No impone la existencia de puntos a ambos lados. Por ello la derivada relativa en un extremo legítimo coincide con su única derivada lateral, mientras que en un punto interior es imprescindible la concordancia de ambas.

### Corolario 19.8.5 — Extremos e interior de un intervalo cerrado no degenerado
Sean $a<b$ y $f:[a,b]\to\mathbb R$. La derivada relativa a $[a,b]$ en $a$ existe si y sólo si existe $f'_+(a)$; cuando existen, son iguales. En $b$ existe si y sólo si existe $f'_-(b)$, y entonces coinciden. Para cada $c\in(a,b)$, $f$ es derivable en $c$ si y sólo si las derivadas izquierda y derecha existen y son iguales.

**Demostración.**
En $a$, el dominio izquierdo está vacío porque todos los puntos de $[a,b]$ son mayores o iguales que $a$. Para un radio arbitrario $r>0$, el punto

$$
x:=a+\tfrac12\min\{r,b-a\}
$$

pertenece a $(a,b)$ y satisface $0<x-a<r$; el lado derecho acumula. En $b$ ocurre simétricamente: $b-\tfrac12\min\{r,b-a\}$ es un testigo izquierdo para cada radio $r>0$, y el dominio derecho está vacío. Si $a<c<b$, los dos puntos

$$
c-\tfrac12\min\{r,c-a,b-c\},\qquad
c+\tfrac12\min\{r,c-a,b-c\}
$$

pertenecen a $[a,b]$ y acreditan acumulación en ambos lados de $c$. Aplicar los tres casos de Teorema §19.8.4 — Reconstrucción de la derivada desde los lados activos a esos dominios demuestra todas las equivalencias. Las fórmulas proporcionan un testigo para el radio fijado; no construyen una selección infinita. $\square$

### Proposición 19.8.6 — Una derivada lateral implica continuidad desde ese lado
Si $f:D\to\mathbb R$ posee derivada derecha en $a\in D$, entonces la restricción de $f$ al conjunto $E_+:=\{a\}\cup D_a^+$ es continua en $a$ y, en particular,

$$
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\quad
0<x-a<\delta\Longrightarrow |f(x)-f(a)|<\varepsilon.
$$

La afirmación simétrica vale para la derivada izquierda y $E_-:=\{a\}\cup D_a^-$. No se deduce continuidad de $f$ en $a$ relativamente a todo $D$ cuando el lado opuesto también acumula pero no está controlado.

**Demostración.**
Consideremos el lado derecho; el otro es simétrico. La definición de derivada lateral incluye $a\in\operatorname{Acc}(D_a^+)$. Por inclusión, $a\in\operatorname{Acc}(E_+)$ y $a\in E_+$. La restricción $F:=f\upharpoonright E_+:E_+\to\mathbb R$ existe con ese dominio y codominio. Para $x\in E_+\setminus\{a\}=D_a^+$ se tiene $F(x)=f(x)$ y $F(a)=f(a)$, de modo que $q_{F,a}(x)=q_{f,a}(x)$. El límite lateral que define la derivada derecha es, por tanto, exactamente el límite del cociente incremental de $F$ sobre todo su dominio perforado. Definición §19.1.3 — Derivabilidad en un punto afirma que $F$ es derivable en $a$; Teorema §19.2.1 — Toda función derivable en un punto es continua en él da su continuidad relativa a $E_+$. Desarrollar la definición de continuidad para $x>a$ produce la desigualdad del enunciado. No se ha restringido una derivada bilateral supuesta: la derivabilidad de $F$ procede únicamente del límite lateral disponible. $\square$

### Proposición 19.8.7 — Dos pendientes laterales distintas y efecto de la restricción
Para $f:\mathbb R\to\mathbb R$, $f(x)=|x|$, las derivadas laterales en cero existen, pero

$$
\boxed{f'_-(0)=-1,\qquad f'_+(0)=1,\qquad f'(0)\text{ no existe}.}
$$

En cambio, si $E:=[0,1]$ y $F:=f\upharpoonright E:E\to\mathbb R$, entonces $F$ es derivable en $0$ relativamente a $E$ y $F'(0)=1$. La existencia de esa derivada no proporciona una derivada de la función original sobre $\mathbb R$.

**Demostración.**
El cero acumula en ambos lados de $\mathbb R$: para todo $r>0$ sirven, separadamente, $-r/2$ y $r/2$. Como $f(0)=0$, los cocientes incrementales satisfacen exactamente

$$
q_{f,0}(x)=\frac{|x|}{x}
=\begin{cases}-1,&x<0,\\ 1,&x>0.\end{cases}
$$

Para cada $\varepsilon>0$, el radio $\delta=1$ comprueba ambas condiciones de Proposición §19.8.2 — Criterios cuantificados y unicidad lateral, con errores nulos; las derivadas laterales son $-1$ y $1$. Puesto que ambos lados acumulan y los valores difieren, Teorema §19.8.4 — Reconstrucción de la derivada desde los lados activos niega la existencia de $f'(0)$, de acuerdo con Proposición §19.2.3 — La continuidad no implica derivabilidad.

Sobre $E=[0,1]$ la misma función satisface $F(x)=x$ para todo $x\in E$. La función identidad $i:\mathbb R\to\mathbb R$ es derivable en cero y $i'(0)=1$ por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática. Como $0\in\operatorname{Acc}(E)$ (testigos $\min\{r,1\}/2$), Proposición §19.5.2 — Restricción de una función derivable establece que $i\upharpoonright E$ es derivable en cero y conserva la derivada $1$. Las funciones $F$ e $i\upharpoonright E$ tienen dominio, codominio y valores idénticos: son iguales como funciones tipadas por Proposición §0.6.3 — Criterio de igualdad de funciones. Así $F'(0)=1$. Pero $F:E\to\mathbb R$ y $f:\mathbb R\to\mathbb R$ tienen dominios distintos; la derivabilidad de la primera no se transmite a la segunda. $\square$

**Transición.** Quedan articuladas las nociones locales de derivada, aproximación lineal, reglas algebraicas, composición, inversión y derivadas laterales. Con estos resultados concluye el capítulo 19, auditado y cerrado canónicamente en el manuscrito humano bajo ZF y lógica clásica. El capítulo 20 comenzará con extremos locales y el teorema de Fermat, para desarrollar después Rolle y los teoremas del valor medio; ninguno de esos resultados intervino en las demostraciones anteriores. La formalización Lean seguirá siendo un proceso de certificación distinto.
