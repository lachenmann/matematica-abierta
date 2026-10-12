---
content-id: MA-BCH-0270
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-017
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: 'Capítulo 17 — Continuidad uniforme: una escala que sirve para todo'
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C17.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html)

Una función continua puede exigir radios de entrada cada vez menores al cambiar el centro. La continuidad uniforme pregunta si, para cada precisión de salida, una sola escala protege todos los pares del dominio. Aquí demostraremos cómo la compacidad produce esa escala y qué puede hacerse con ella.

Los prerrequisitos centrales son continuidad de C14 y compacidad de C16. Supremo e ínfimo de C00, adherencia de C04, sucesiones de C06, Cauchy y raíces de C10 y tipos de C12 son interfaces heredadas. La prueba de Heine–Cantor usa una cubierta de todos los pares centro-radio admisibles y finitud, sin seleccionar radios por todos los puntos ni fabricar rutas. Las recíprocas secuenciales se declaran condicionales a CC(R) o a una enumeración dada. La extensión al cierre se construye por cortes de imágenes locales y la aproximación poligonal por una malla finita. No usamos derivadas, integrales ni teoría de límites uniformes de funciones.

## 17.1. Un radio antes de conocer los dos puntos

[]{#MA-SEC-ANM-01-017-001}

La continuidad de C14 permite que el radio de entrada dependa del centro. Si queremos controlar una función en todo su dominio, debemos preguntar si una sola escala puede servir para todos los centros a la vez. Esa pregunta depende de la función **y del dominio**.

**Definición.** Para $f:D\to\mathbb R$, la continuidad uniforme en $D$ significa

$$\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in D:
|x-y|<\delta\Longrightarrow|f(x)-f(y)|<\varepsilon.$$

La función y el dominio ya están fijados. El radio puede depender de ellos y de $\varepsilon$, pero se fija antes de conocer $x,y$. En la continuidad puntual el orden es $\forall a\in D\;\forall\varepsilon>0\;\exists\delta>0\;\forall x\in D$: conocer $a$ antes permite un radio dependiente del centro. Uniformidad implica continuidad puntual por usar el mismo radio en cada centro; también se hereda por restricción a cualquier subconjunto. En el dominio vacío ambas propiedades son vacías: $\delta=1$ sirve para cualquier tolerancia.

**Negación.** Fallar la uniformidad significa que existe **una** tolerancia $\varepsilon_0>0$ tal que, para **todo** $\delta>0$, hay $x,y\in D$ con

$$|x-y|<\delta,\qquad |f(x)-f(y)|\ge\varepsilon_0.$$

El error de salida permanece separado de cero mientras la distancia de entrada puede hacerse arbitrariamente pequeña. Un radio propuesto que dependa del centro no demuestra este fallo: podría existir otro radio común que la prueba no haya encontrado.

**R1. Controles algebraicos.** Si $|f(x)-f(y)|\le L|x-y|$ en todo $D$, con una constante $L\ge0$, llamamos a $f$ Lipschitz. Cuando $L>0$, $\delta=\varepsilon/L$ da uniformidad; cuando $L=0$, todas las diferencias son cero y sirve cualquier radio positivo. Por ejemplo, $f(x)=ax+b$ en $\mathbb R$ tiene constante $|a|$. El valor absoluto tiene constante uno por la desigualdad triangular inversa.

Para $q(x)=x^2$ en $[-M,M]$, $M>0$,

$$|q(x)-q(y)|=|x-y||x+y|\le2M|x-y|.$$

Por tanto un radio uniforme es $\varepsilon/(2M)$. En cambio, sobre toda la recta fijamos $\varepsilon_0=1$. Dado $\delta>0$, tomamos $h=\min(\delta/2,1)>0$, $x=1/h$ y $y=x+h$. Entonces $h<\delta$ y

$$y^2-x^2=h(2x+h)=2+h^2>1.$$

Estos testigos refutan todo candidato a radio común. La continuidad puntual del cuadrado sigue siendo válida por C14.

![En \[−1,1\], la identidad de diferencia de cuadrados da radio 1/2 para tolerancia 1. En la recta, el par 4 y 17/4 tiene distancia 1/4 y error 33/16, y refuta ese candidato. La prueba general de R1/E002 produce testigos para todo radio: un solo gráfico no refuta todos los candidatos.](../../assets/books/anm/C17/C17-F01.svg){#fig-anm-c17-f01 fig-alt="En \[−1,1\], la identidad de diferencia de cuadrados da radio 1/2 para tolerancia 1. En la recta, el par 4 y 17/4 tiene distancia 1/4 y error 33/16, y refuta ese candidato. La prueba general de R1/E002 produce testigos para todo radio: un solo gráfico no refuta todos los candidatos."}

La raíz cuadrada muestra que uniformidad no exige una constante Lipschitz. Para $x\ge y\ge0$, escribimos $a=\sqrt{x}$, $b=\sqrt{y}$; como $a\ge b$,

$$(a-b)^2\le(a-b)(a+b)=x-y.$$

Así $|\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}$ en $[0,\infty)$, y $\delta=\varepsilon^2$ asegura uniformidad. En $[0,1]$ no es Lipschitz: si hubiera una constante $L>0$, con $y=0$ se exigiría $1/\sqrt{x}\le L$ para todo $x>0$. Tomar $x=1/(n+1)^2$ con $n+1>L$ contradice esa cota. $L=0$ tampoco sirve, porque la función no es constante. Raíces y sus reglas de orden/algebra son interfaces de C10, no resultados diferenciales.

### Microcontroles

[]{#MA-MIC-ANM-01-017-001}

1. ¿Qué debe quedar fijado antes de conocer $x,y$ en continuidad uniforme?

[]{#MA-MIC-ANM-01-017-002}

2. ¿Qué dependencia adicional admite la continuidad puntual?

[]{#MA-MIC-ANM-01-017-003}

3. ¿Por qué la uniformidad implica continuidad en cada punto?

[]{#MA-MIC-ANM-01-017-004}

4. ¿Qué tolerancia se mantiene fija al negar uniformidad?

[]{#MA-MIC-ANM-01-017-005}

5. ¿Un radio local dependiente del centro prueba falta de uniformidad?

[]{#MA-MIC-ANM-01-017-006}

6. ¿Qué radio sirve para una constante Lipschitz $L>0$?

[]{#MA-MIC-ANM-01-017-007}

7. ¿Por qué la raíz puede ser uniforme sin ser Lipschitz?

[]{#MA-MIC-ANM-01-017-008}

8. ¿Qué ocurre con el dominio vacío?

## 17.2. Una cubierta y una escala de protección

[]{#MA-SEC-ANM-01-017-002}

Una subcubierta finita contiene todos los puntos del compacto, pero necesitaremos algo más: un margen que asegure que una vecindad de cada punto queda dentro de un miembro de la cubierta original. No basta tomar los radios de bolas que cubren si no hemos reservado espacio para mover el centro.

**R2. Número de Lebesgue para una cubierta dada.** Sea $K\subseteq\mathbb R$ compacto y $(U_i)_{i\in I}$ una cubierta por abiertos reales. Existe $\lambda>0$ tal que

$$\forall z\in K\;\exists i\in I:\quad
K\cap(z-\lambda,z+\lambda)\subseteq U_i.$$

No se afirma una función que elija el índice para cada $z$. Para $K=\varnothing$ sirve $\lambda=1$, incluso si $I=\varnothing$. Supongamos $K$ no vacío.

Construimos **todos** los triples admisibles

$$T=\{(a,i,r)\in K\times I\times\mathbb R_{>0}:
(a-2r,a+2r)\subseteq U_i\}.$$

La regla $t=(a,i,r)\mapsto B(a,r)$, donde $B(a,r)=(a-r,a+r)$, determina una familia de abiertos reales. Cubre $K$: para un $a$ fijado la cubierta da algún $i$ con $a\in U_i$ y la apertura da $\rho>0$ con $B(a,\rho)\subseteq U_i$; $r=\rho/2$ hace admisible el triple y $a\in B(a,r)$. Ésta es una verificación de cobertura, sin seleccionar un triple para cada punto.

Compacidad entrega $J\subseteq T$ finito cuyas bolas pequeñas cubren $K$. No puede ser vacío. Por C16, el conjunto finito de sus radios positivos tiene mínimo positivo; definimos

$$\lambda=\min\{r:(a,i,r)\in J\}>0.$$

Para $z\in K$ hay un triple $(a,i,r)\in J$ con $|z-a|<r$. Si $w\in B(z,\lambda)$, entonces

$$|w-a|\le|w-z|+|z-a|<\lambda+r\le2r.$$

Por ello $B(z,\lambda)\subseteq B(a,2r)\subseteq U_i$. Hemos obtenido incluso la inclusión de la bola ambiental completa, que implica la inclusión relativa del enunciado. El índice se fija para este $z$ después de fijar $\lambda$.

![Para K=\[0,1\] y los dos abiertos indicados, λ=1/10 sirve: se usa U1 si z≤1/2 y U2 si z>1/2. Los tres centros dibujados son ilustrativos. λ=1/5 falla en el centro 1/2, porque su bola relativa contiene 2/5 y 3/5, y ningún miembro contiene ambos. Extremos de la bola se interpretan por desigualdades estrictas del texto.](../../assets/books/anm/C17/C17-F02.svg){#fig-anm-c17-f02 fig-alt="Para K=\[0,1\] y los dos abiertos indicados, λ=1/10 sirve: se usa U1 si z≤1/2 y U2 si z&gt;1/2. Los tres centros dibujados son ilustrativos. λ=1/5 falla en el centro 1/2, porque su bola relativa contiene 2/5 y 3/5, y ningún miembro contiene ambos. Extremos de la bola se interpretan por desigualdades estrictas del texto."}

La familia de todos los triples admisibles reemplaza una elección simultánea de radios. La duplicación de radios reserva margen; la finitud permite convertirlo en una escala positiva común. No tomamos el ínfimo de infinitos radios positivos, que podría ser cero.

Por ejemplo, en $K=[0,1]$ la cubierta $U_1=(-1,3/5)$ y $U_2=(2/5,2)$ admite $\lambda=1/10$ para la inclusión relativa. Si $z\le1/2$, todo $w\in K$ con $|w-z|<1/10$ satisface $w<3/5$ y entra en $U_1$. Si $z>1/2$, satisface $w>2/5$ y entra en $U_2$. La desigualdad estricta protege también el caso $z=1/2$.

Una cubierta de un dominio no compacto no garantiza este margen. En $D=(0,1)$, los abiertos $U_n=(1/(n+2),2)$ forman una cubierta sin subcubierta finita, según C16. Tampoco tienen número de Lebesgue positivo: para todo $z\in D$, cualquier bola relativa que alcance arbitrariamente cerca de cero omite estar contenida en un único $U_n$. Dado $\lambda>0$, basta tomar $0<z<\min(\lambda,1)$; su bola relativa contiene puntos positivos por debajo de cada umbral.

Si una cubierta se da por abiertos **relativos** $A_i$ de un compacto $K$, C16 proporciona el levantamiento canónico $W_i=(\mathbb R\setminus K)\cup A_i$, abierto real, con $K\cap W_i=A_i$. Aplicar R2 a $W$ da la misma conclusión relativa para $A$. No se elige una familia de ambientes.

### Microcontroles

[]{#MA-MIC-ANM-01-017-009}

1. ¿Qué expresa un número de Lebesgue para una cubierta de $K$?

[]{#MA-MIC-ANM-01-017-010}

2. ¿Por qué se reúnen todos los triples admisibles?

[]{#MA-MIC-ANM-01-017-011}

3. ¿Con qué bolas se cubre y en cuáles se reserva protección?

[]{#MA-MIC-ANM-01-017-012}

4. ¿Qué ocurre antes de tomar el mínimo de radios?

[]{#MA-MIC-ANM-01-017-013}

5. ¿Qué desigualdad mueve la protección desde $a$ hasta $z$?

[]{#MA-MIC-ANM-01-017-014}

6. ¿Se elige un abierto para todos los centros simultáneamente?

[]{#MA-MIC-ANM-01-017-015}

7. ¿Cómo se tratan cubiertas por abiertos relativos?

[]{#MA-MIC-ANM-01-017-016}

8. ¿Qué número sirve para el compacto vacío?

## 17.3. Heine–Cantor: reducir antes de tomar el mínimo

[]{#MA-SEC-ANM-01-017-003}

**R3. Heine–Cantor.** Si $f:D\to\mathbb R$ es continua en cada punto de un compacto $K\subseteq D$, relativamente a $D$, su restricción $h:K\to\mathbb R$ es uniformemente continua. No hace falta que $D$ sea compacto ni que $K$ sea intervalo.

La restricción es continua por C14. Fijamos $\varepsilon>0$. Si $K$ es vacío, $\delta=1$ sirve. Para $K$ no vacío, reunimos todos los pares centro-radio que controlan las salidas en la bola doble:

$$T_\varepsilon=\{(a,r)\in K\times\mathbb R_{>0}:
\forall z\in K,\ |z-a|<2r\Longrightarrow|h(z)-h(a)|<\varepsilon/2\}.$$

Cada par determina el abierto ambiental $B(a,r)$. Estas bolas cubren $K$: en un $a$ fijado, continuidad con tolerancia $\varepsilon/2$ da $\rho>0$; $r=\rho/2$ hace admisible $(a,r)$ y su bola contiene $a$. No hemos escogido una función $a\mapsto r_a$: la relación y su familia de bolas ya están determinadas por sus fórmulas.

Compacidad entrega un $J\subseteq T_\varepsilon$ finito que cubre $K$ mediante las bolas pequeñas. Es no vacío, y

$$\delta=\min\{r:(a,r)\in J\}>0.$$

Fijamos ahora $x,y\in K$ con $|x-y|<\delta$. La cubierta finita da $(a,r)\in J$ con $|x-a|<r$. No necesitamos que $y$ esté en esa misma bola pequeña. Basta observar

$$|y-a|\le|y-x|+|x-a|<\delta+r\le2r.$$

Tanto $x$ como $y$ están en la bola doble donde se guardó el control. Así

$$|h(x)-h(y)|\le|h(x)-h(a)|+|h(a)-h(y)|
<\varepsilon/2+\varepsilon/2=\varepsilon.$$

El radio quedó fijado antes de los dos puntos. La prueba produjo exactamente la uniformidad, sin compacidad secuencial ni selección de rutas o radios por todos los centros.

![Esquema con a=0, r=1, δ=3/5, x=4/5 e y=13/10. El par tiene distancia 1/2<δ; y queda fuera de la bola pequeña pero dentro de la doble. Cada índice admisible asegura error menor que ε/2 respecto de f(a) en toda la bola doble relativa. La geometría representa el paso de la prueba, no una función particular.](../../assets/books/anm/C17/C17-F03.svg){#fig-anm-c17-f03 fig-alt="Esquema con a=0, r=1, δ=3/5, x=4/5 e y=13/10. El par tiene distancia 1/2&lt;δ; y queda fuera de la bola pequeña pero dentro de la doble. Cada índice admisible asegura error menor que ε/2 respecto de f(a) en toda la bola doble relativa. La geometría representa el paso de la prueba, no una función particular."}

**Segunda lectura mediante R2.** Para cada $a\in K$, sea $A_a=\{z\in K:|h(z)-h(a)|<\varepsilon/2\}$. Son abiertos relativos por continuidad y forman una cubierta, porque $a\in A_a$. Levantarlos por $W_a=(\mathbb R\setminus K)\cup A_a$ y aplicar R2 proporciona $\lambda>0$. Si $|x-y|<\lambda$, los dos puntos pertenecen a un mismo $A_a$: $x$ está en su propia bola relativa y $y$ también. Cada salida dista menos que $\varepsilon/2$ de $h(a)$, y la desigualdad triangular concluye. Esta lectura expresa el mismo mecanismo como una propiedad de la cubierta, no como una elección global de centros.

Por Heine–Borel de C16, toda continua en un cerrado acotado real es uniformemente continua. La garantía incluye segmentos, conjuntos finitos, compactos rotos y conjuntos de recíprocos con su límite. Las hipótesis garantizan uniformidad para **toda** continua sobre ese dominio; no son necesarias para una función particular. La identidad en $\mathbb R$ es uniformemente continua aunque el dominio no sea compacto.

Acotación sola no asegura la garantía: $1/x$ en $(0,1]$ es continua pero falla la uniformidad. En efecto, para $x_n=1/(n+2)$, $y_n=1/(n+3)$,

$$|x_n-y_n|=\frac1{(n+2)(n+3)}\longrightarrow0,
\qquad |1/x_n-1/y_n|=1.$$

Dado un radio cualquiera, arquimedianidad proporciona un índice con la distancia menor que él, mientras la separación de salida sigue siendo uno. Cerradura sola tampoco basta: el cuadrado en $\mathbb R$ ya dio testigos. No se deduce ninguno de estos fallos de la mera forma de una estimación local.

### Microcontroles

[]{#MA-MIC-ANM-01-017-017}

1. ¿Qué uniformiza Heine–Cantor cuando $K\subseteq D$?

[]{#MA-MIC-ANM-01-017-018}

2. ¿Qué información guarda un par admisible $(a,r)$?

[]{#MA-MIC-ANM-01-017-019}

3. ¿Cómo se verifica cobertura sin función de radios?

[]{#MA-MIC-ANM-01-017-020}

4. ¿Tiene que entrar $y$ en la bola pequeña que cubre $x$?

[]{#MA-MIC-ANM-01-017-021}

5. ¿Por qué se divide el error en dos mitades?

[]{#MA-MIC-ANM-01-017-022}

6. ¿Se usa la recíproca secuencial para Heine–Cantor?

[]{#MA-MIC-ANM-01-017-023}

7. ¿Necesita $K$ ser un intervalo?

[]{#MA-MIC-ANM-01-017-024}

8. ¿Compacidad es necesaria para uniformidad de una función particular?

## 17.4. Medir la oscilación a cada escala

[]{#MA-SEC-ANM-01-017-004}

Heine–Cantor garantiza una escala, pero puede no dar una fórmula sencilla para ella. Podemos registrar cuánto varía la función cuando restringimos la distancia de entrada.

**R4. Módulo de oscilación.** Supongamos $D$ no vacío y $f:D\to\mathbb R$ acotada: $|f(x)|\le B$ con $B\ge0$. Para $t\ge0$ definimos

$$\omega_f(t)=\sup\{|f(x)-f(y)|:x,y\in D,\ |x-y|\le t\}.$$

El conjunto es no vacío porque admite pares diagonales con diferencia cero; está acotado entre cero y $2B$. El supremo existe por C00. Si $D$ es vacío, fijamos por convención $\omega_f(t)=0$; no se toma supremo real del conjunto vacío. La acotación de valores es una hipótesis suficiente para que este módulo global sea real finito. Uniformidad sola no acota los valores: la identidad en $\mathbb R$ lo recuerda. Esa identidad tiene, de hecho, módulo finito $\omega(t)=t$; no afirmamos que toda función no acotada carezca de módulo finito.

Los conjuntos de diferencias aumentan al aumentar $t$; por eso $\omega$ es no decreciente, $\omega(0)=0$, y

$$|f(x)-f(y)|\le\omega_f(t)\quad\text{si }|x-y|\le t.$$

En este marco acotado, $f$ es uniformemente continua si y sólo si $\omega_f(t)\to0$ cuando $t\downarrow0$. Para la dirección directa, dada $\varepsilon>0$, uniformidad con tolerancia $\varepsilon/2$ da $\delta>0$. Si $0<t<\delta$, todos los valores del conjunto que define $\omega(t)$ son menores que $\varepsilon/2$, por lo que

$$0\le\omega(t)\le\varepsilon/2<\varepsilon.$$

El supremo podría igualar $\varepsilon/2$; por eso reservamos presupuesto. Para la recíproca, el límite da $\eta>0$ con $\omega(t)<\varepsilon$ para $0<t<\eta$. Tomamos $t=\eta/2$ y $\delta=t$. Toda pareja de distancia menor que $\delta$ está en el conjunto del módulo a escala $t$, y su diferencia es a lo sumo $\omega(t)<\varepsilon$.

Si $f$ es Lipschitz con constante $L$, su módulo satisface $\omega_f(t)\le Lt$. La raíz tiene $\omega(t)\le\sqrt t$ en cualquier dominio no negativo donde este módulo sea definido; son dos tipos distintos de dependencia entre escalas.

**Un módulo exacto.** Para $q(x)=x^2$ en $[0,1]$,

$$\omega_q(t)=
\begin{cases}2t-t^2,&0\le t\le1,\\1,&t\ge1.\end{cases}$$

Si $0\le v\le u\le1$ y $d=u-v\le t\le1$, entonces $u^2-v^2=d(2u-d)\le d(2-d)\le t(2-t)$. La última desigualdad resulta de $(t-d)(2-t-d)\ge0$. El par $u=1$, $v=1-t$ alcanza la cota. Si $t\ge1$, todas las diferencias son a lo sumo uno y el par $1,0$ lo alcanza. Para todo $t$, $\omega_q(t)\le2t$; esa cota Lipschitz es más simple pero menos precisa.

![En \[0,1\], los módulos exactos de x² y √x son 2t−t² y √t para 0≤t≤1; después de uno ambos valen uno. La recta 2t es una cota más sencilla del módulo del cuadrado. Las fórmulas se prueban por álgebra y pares que alcanzan las cotas; las curvas sólo las representan.](../../assets/books/anm/C17/C17-F04.svg){#fig-anm-c17-f04 fig-alt="En \[0,1\], los módulos exactos de x² y √x son 2t−t² y √t para 0≤t≤1; después de uno ambos valen uno. La recta 2t es una cota más sencilla del módulo del cuadrado. Las fórmulas se prueban por álgebra y pares que alcanzan las cotas; las curvas sólo las representan."}

No exigimos que el supremo sea alcanzado para un dominio arbitrario, ni continuidad del módulo como función de $t$. Para aplicar el criterio sólo necesitamos la definición del supremo y el control cerca de cero. En un compacto, C16 acota toda continua y R3 hace que su módulo tienda a cero.

### Microcontroles

[]{#MA-MIC-ANM-01-017-025}

1. ¿Qué garantiza que el módulo global definido sea real finito?

[]{#MA-MIC-ANM-01-017-026}

2. ¿Qué significa $\omega_f(t)$?

[]{#MA-MIC-ANM-01-017-027}

3. ¿Por qué $\omega_f(0)=0$?

[]{#MA-MIC-ANM-01-017-028}

4. ¿Por qué el módulo no decrece?

[]{#MA-MIC-ANM-01-017-029}

5. ¿Por qué una cota estricta de todos los valores no da supremo estrictamente menor?

[]{#MA-MIC-ANM-01-017-030}

6. ¿Cómo da uniformidad el límite del módulo en cero?

[]{#MA-MIC-ANM-01-017-031}

7. ¿Qué par alcanza el módulo de $x^2$ en $[0,1]$ para $0\le t\le1$?

[]{#MA-MIC-ANM-01-017-032}

8. ¿Uniformidad obliga a valores acotados en todo dominio?

## 17.5. Transportar tolerancias por operaciones

[]{#MA-SEC-ANM-01-017-005}

La continuidad puntual se conserva por muchas operaciones. Uniformidad exige además controlar los factores que multiplican errores y los denominadores. Todas las funciones de una operación se consideran en el mismo dominio efectivo.

**R5. Sumas y productos.** Si $f,g:D\to\mathbb R$ son uniformemente continuas, $f+g$ también: elegimos radios para error $\varepsilon/2$ en cada una y tomamos su mínimo. La desigualdad triangular suma los dos errores. Multiplicar por una constante $c$ se trata con $\varepsilon/|c|$ cuando $c\ne0$; para $c=0$ la salida es constante.

Para productos suponemos además $|f|\le M_f$, $|g|\le M_g$ en $D$, con cotas no negativas. Pedimos a ambas funciones errores menores que $\eta=\varepsilon/(M_f+M_g+1)>0$ y usamos el mínimo de sus radios. Entonces

$$|f(x)g(x)-f(y)g(y)|
\le |g(x)|\,|f(x)-f(y)|+|f(y)|\,|g(x)-g(y)|
\le(M_f+M_g)\eta<\varepsilon.$$

El caso $M_f+M_g=0$ entrega diferencia cero y satisface la conclusión. Sólo se combinan dos radios dados, no una familia infinita. Las cotas son suficientes: sin ellas, dos funciones uniformes pueden tener producto no uniforme. $f(x)=g(x)=x$ en $\mathbb R$ tiene producto $x^2$. No son necesarias para cada producto particular: multiplicar la identidad por la constante uno sigue siendo uniforme.

**Recíprocos y cocientes.** Si $g$ es uniforme y $|g(x)|\ge m>0$ en $D$, entonces $1/g$ tiene exactamente ese dominio y

$$\left|\frac1{g(x)}-\frac1{g(y)}\right|
\le\frac{|g(x)-g(y)|}{m^2}.$$

Un radio que da error $\varepsilon m^2$ para $g$ da error $\varepsilon$ para el recíproco. Éste también está acotado por $1/m$. Si $f$ es uniforme y acotada, el producto de $f$ y $1/g$ muestra uniformidad del cociente. «No tener ceros» por sí solo no proporciona $m$: en $(0,1]$, la identidad es uniforme, no tiene ceros y su recíproco no es uniforme.

En un compacto, C16 proporciona acotación para las continuas y un margen positivo para el denominador continuo sin ceros. R3 uniformiza las funciones, y las reglas anteriores justifican el cociente. Alternativamente, C14 da continuidad del cociente y R3 vuelve a aplicarse, siempre con el dominio compacto declarado.

**Composición.** Sea $f:D\to E$ uniforme y $g:E\to\mathbb R$ uniforme sobre $E$; bastaría uniformidad de $g$ en $f[D]$. Para error final $\varepsilon$, primero elegimos $\eta>0$ que controle $g$. Después elegimos $\delta>0$ que produzca error de salida menor que $\eta$ para $f$. Así

$$|x-y|<\delta\Longrightarrow|f(x)-f(y)|<\eta
\Longrightarrow|g(f(x))-g(f(y))|<\varepsilon.$$

![Para f(x)=2x en \[0,1\] y g(y)=y² en \[0,2\], el error exterior tiene cota cuatro veces la distancia. Para ε=1, sirve η=1/4 y después δ=η/2=1/8. El par de entrada 1/2,3/5 ilustra distancias 1/10,1/5 y 11/25, cada una bajo su presupuesto. Las tolerancias se eligen desde la salida final hacia la entrada.](../../assets/books/anm/C17/C17-F05.svg){#fig-anm-c17-f05 fig-alt="Para f(x)=2x en \[0,1\] y g(y)=y² en \[0,2\], el error exterior tiene cota cuatro veces la distancia. Para ε=1, sirve η=1/4 y después δ=η/2=1/8. El par de entrada 1/2,3/5 ilustra distancias 1/10,1/5 y 11/25, cada una bajo su presupuesto. Las tolerancias se eligen desde la salida final hacia la entrada."}

El orden de elección sigue el transporte de tolerancias en sentido inverso al de las funciones. Continuidad meramente puntual de la función exterior no basta: componer la identidad uniforme en $\mathbb R$ con el cuadrado continuo pierde uniformidad.

Finalmente, una inyección continua sobre un compacto $K$ tiene inversa continua en $H=f[K]$ por C16. Considerar la inversa como función $H\to\mathbb R$ conserva continuidad porque las distancias de salida son las mismas. Como $H$ es compacto, R3 hace también uniforme a esa inversa. No afirmamos que tenga constante Lipschitz: el cuadrado en $[0,1]$ tiene inversa raíz, uniforme pero no Lipschitz.

### Microcontroles

[]{#MA-MIC-ANM-01-017-033}

1. ¿Cómo se combinan dos radios para una suma?

[]{#MA-MIC-ANM-01-017-034}

2. ¿Qué hipótesis suficientes se añaden para productos?

[]{#MA-MIC-ANM-01-017-035}

3. ¿Qué producto refuta conservación automática en dominios arbitrarios?

[]{#MA-MIC-ANM-01-017-036}

4. ¿Qué dato positivo controla un recíproco?

[]{#MA-MIC-ANM-01-017-037}

5. ¿Ausencia de ceros basta para ese margen?

[]{#MA-MIC-ANM-01-017-038}

6. ¿Qué tolerancia se elige primero en una composición?

[]{#MA-MIC-ANM-01-017-039}

7. ¿Qué dominio basta controlar uniformemente para la función exterior?

[]{#MA-MIC-ANM-01-017-040}

8. ¿Por qué una inversa compacta continua es también uniforme?

## 17.6. Pares próximos y rutas dadas

[]{#MA-SEC-ANM-01-017-006}

**R6. Prueba mediante dos sucesiones dadas.** Si $f:D\to\mathbb R$ es uniforme y $(x_n),(y_n)$ son dos sucesiones dadas en $D$ con $|x_n-y_n|\to0$, entonces $|f(x_n)-f(y_n)|\to0$. Para $\varepsilon>0$ fijamos el radio uniforme $\delta$. La convergencia de las distancias proporciona $N$ tal que son menores que $\delta$ para $n\ge N$; desde ese índice las diferencias de salida son menores que $\varepsilon$. No hace falta que ninguna de las dos rutas converja, ni que sea acotada.

Por ejemplo, $x_n=n+1$ y $y_n=n+1+1/(n+1)$ se acercan entre sí aunque escapen al infinito. Para el cuadrado,

$$|y_n-x_n|=\frac1{n+1}\to0,
\qquad y_n^2-x_n^2=2+\frac1{(n+1)^2}\ge2.$$

R6 refuta uniformidad sin fabricar una ruta por selección: las fórmulas ya la determinan. Los pares recíprocos de R3 muestran el mismo fallo junto a un extremo omitido.

![Se representan n=0,1,2,4 de las rutas recíprocas dadas. La distancia de entrada es 1/\[(n+2)(n+3)\] y tiende a cero; bajo f(x)=1/x la distancia de salida es siempre uno. R6 directo refuta uniformidad; no se usa la recíproca ni selección de rutas. Muestra finita, no prueba visual de convergencia.](../../assets/books/anm/C17/C17-F06.svg){#fig-anm-c17-f06 fig-alt="Se representan n=0,1,2,4 de las rutas recíprocas dadas. La distancia de entrada es 1/\[(n+2)(n+3)\] y tiende a cero; bajo f(x)=1/x la distancia de salida es siempre uno. R6 directo refuta uniformidad; no se usa la recíproca ni selección de rutas. Muestra finita, no prueba visual de convergencia."}

**Recíproca con alcance declarado.** Supongamos que toda pareja de rutas dadas en $D$ con distancia tendente a cero tiene diferencias de salida tendentes a cero. Para deducir uniformidad en un dominio arbitrario mediante el argumento siguiente usamos $\mathrm{CC}(\mathbb R)$, sólo como premisa del resultado condicional.

Si falla uniformidad, fijamos la tolerancia $\varepsilon_0>0$ de la negación. Los conjuntos

$$A_n=\{x\in D:\exists y\in D,
|x-y|<1/(n+1),\ |f(x)-f(y)|\ge\varepsilon_0\}$$

son no vacíos. Una aplicación de $\mathrm{CC}(\mathbb R)$ da una ruta $x_n\in A_n$. Definimos ahora

$$B_n=\{y\in D:|x_n-y|<1/(n+1),
|f(x_n)-f(y)|\ge\varepsilon_0\}.$$

Son no vacíos por la pertenencia anterior; otra aplicación de la misma premisa da $y_n\in B_n$. Las distancias tienden a cero, pero las diferencias de salida permanecen al menos en $\varepsilon_0$, contradicción. Se gastó selección al fabricar ambas rutas, no en la prueba directa R6. Heine–Cantor no depende de esta recíproca.

Si $D$ no vacío viene con una sobreyección **dada** $e:\mathbb N\to D$, podemos fabricar estos pares sin CC(R): tomamos el menor $j$ para el que existe $k$ con el par $e(j),e(k)$ malo a escala $1/(n+1)$; después el menor $k$ que satisface la condición para ese $j$. Buen orden y sobreyectividad determinan las dos rutas. No se presupone una enumeración para dominios arbitrarios. El dominio vacío es uniforme por separado.

**Preservación de Cauchy.** Toda uniforme envía una sucesión de Cauchy dada a otra de Cauchy. Para $\varepsilon>0$ elegimos $\delta$ uniforme; la condición de Cauchy de entrada da un $N$ con $|x_n-x_m|<\delta$ para $n,m\ge N$, y entonces las diferencias de salida son menores que $\varepsilon$. La definición y acotación de rutas de Cauchy son interfaces de C07.

Esta preservación sola no caracteriza uniformidad en dominios arbitrarios. El cuadrado en $\mathbb R$ la cumple: cada ruta de Cauchy es acotada por algún $M>0$, y $|x_n^2-x_m^2|\le2M|x_n-x_m|$ hace Cauchy a su imagen. Pero el cuadrado no es uniforme en toda la recta. El test con **dos rutas próximas** es más exigente que el test sobre una ruta de Cauchy.

### Microcontroles

[]{#MA-MIC-ANM-01-017-041}

1. ¿Deben converger las dos rutas próximas de R6?

[]{#MA-MIC-ANM-01-017-042}

2. ¿Dónde se gasta selección en la recíproca general?

[]{#MA-MIC-ANM-01-017-043}

3. ¿Qué reemplaza CC(R) con una enumeración dada?

[]{#MA-MIC-ANM-01-017-044}

4. ¿Qué diferencia de salida tienen los pares del cuadrado que escapan?

[]{#MA-MIC-ANM-01-017-045}

5. ¿Por qué una uniforme preserva una ruta de Cauchy?

[]{#MA-MIC-ANM-01-017-046}

6. ¿Esa preservación caracteriza uniformidad en toda $\mathbb R$?

[]{#MA-MIC-ANM-01-017-047}

7. ¿Por qué las diferencias de salida separadas refutan uniformidad sin recíproca?

[]{#MA-MIC-ANM-01-017-048}

8. ¿Qué valor evita el problema del índice inicial cero?

## 17.7. Completar el dominio sin seleccionar aproximantes

[]{#MA-SEC-ANM-01-017-007}

Una uniforme real no puede perder control al aproximarse a un punto omitido de adherencia. Vamos a construir el valor de frontera mediante supremos e ínfimos de **todos** los valores cercanos, sin escoger una sucesión que se aproxime a cada punto.

**R7. Extensión uniforme al cierre.** Toda uniforme $f:D\to\mathbb R$ admite una extensión uniforme $F:\overline D\to\mathbb R$, y ésta es la única extensión continua. Si $D$ es vacío, también lo es su cierre y la función vacía resuelve el enunciado. Supongamos $D$ no vacío.

Uniformidad para error uno da un $\delta_0>0$, que fijamos una sola vez para toda la construcción. Sea $r_0=\delta_0/4$. Para $p\in\overline D$ y $0<r\le r_0$, ponemos

$$E_{p,r}=f[D\cap B(p,r)],\qquad
L_{p,r}=\inf E_{p,r},\quad U_{p,r}=\sup E_{p,r}.$$

Las imágenes son no vacías por adherencia. Para probar acotación fijamos, sólo para este $p$, un $a\in D\cap B(p,r_0)$. Todos los $x$ de esa vecindad satisfacen $|x-a|<2r_0<\delta_0$, por lo que $|f(x)-f(a)|<1$. Así $E_{p,r_0}$ es acotada y también todas sus subimágenes. No se forma una familia elegida $p\mapsto a_p$.

Las imágenes se anidan al disminuir $r$. El conjunto de todos los $L_{p,r}$ es no vacío y está acotado superiormente por $U_{p,r_0}$; definimos por fórmula

$$F(p)=\sup\{L_{p,r}:0<r\le r_0\}.$$

Para cualquier $r$ admisible, $L_{p,r}\le F(p)$. También $F(p)\le U_{p,r}$: para cada $s$ admisible, la imagen a escala $\min(r,s)$ es no vacía y está contenida en las dos imágenes; un valor de esa intersección da $L_{p,s}\le U_{p,r}$. Por tanto $U_{p,r}$ acota todos los ínfimos del corte. Hemos probado

$$L_{p,r}\le F(p)\le U_{p,r}\qquad(0<r\le r_0).$$

**Anchura pequeña.** Dada $\eta>0$, uniformidad da $\delta>0$ para error $\eta$. Si $0<r\le r_0$ y $2r<\delta$, todos los pares de entradas en $B(p,r)\cap D$ distan menos que $\delta$, y todos sus valores difieren menos que $\eta$. Esto implica $U_{p,r}-L_{p,r}\le\eta$: para cada valor $v$, todos los demás son a lo sumo $v+\eta$, así $U_{p,r}\le v+\eta$; entonces $U_{p,r}-\eta$ es cota inferior y no excede $L_{p,r}$. Reservar $\eta=\varepsilon/2$ hace la anchura menor que $\varepsilon$ a una escala adecuada.

Consecuentemente sólo un real puede pertenecer a todos estos intervalos: dos candidatos distintos a distancia $d>0$ no caben en un intervalo de anchura a lo sumo $d/2$. Esta unicidad muestra que el resultado no depende del radio inicial admitido. Si se usaron dos radios iniciales, sus intervalos coinciden a todas las escalas menores que ambos y se estrechan igual. Si $p\in D$, el valor $f(p)$ está en todas las imágenes y en todos sus intervalos, luego $F(p)=f(p)$. La fórmula de valor único define una función, no una selección entre posibles límites.

![Para p=0 y f(x)=√x en (0,1\], las imágenes de bolas de radio r≤1 son (0,√r); sus envolventes cerradas son \[0,√r\]. Se ilustran cuatro escalas exactas. Cero no es un valor de las imágenes originales, pero pertenece a todas las envolventes y es el único candidato al estrecharse. La prueba de R7 usa todas las escalas, no sólo las cuatro dibujadas.](../../assets/books/anm/C17/C17-F07.svg){#fig-anm-c17-f07 fig-alt="Para p=0 y f(x)=√x en (0,1\], las imágenes de bolas de radio r≤1 son (0,√r); sus envolventes cerradas son \[0,√r\]. Se ilustran cuatro escalas exactas. Cero no es un valor de las imágenes originales, pero pertenece a todas las envolventes y es el único candidato al estrecharse. La prueba de R7 usa todas las escalas, no sólo las cuatro dibujadas."}

**Uniformidad en el cierre.** Dada $\varepsilon>0$, tomamos $\delta>0$ uniforme para $f$ con error $\varepsilon/3$ y fijamos $\Delta=\delta/3$. Sean $p,q\in\overline D$ con $|p-q|<\Delta$. Elijamos un solo radio $0<r\le r_0$ con $r\le\delta/6$. Para cualesquiera entradas $a\in D\cap B(p,r)$ y $b\in D\cap B(q,r)$,

$$|a-b|\le|a-p|+|p-q|+|q-b|<2r+\delta/3\le2\delta/3<\delta.$$

Así todo valor de $E_{p,r}$ difiere de todo valor de $E_{q,r}$ menos que $\varepsilon/3$. La regla de cotas anterior da $U_{p,r}-L_{q,r}\le\varepsilon/3$ y $U_{q,r}-L_{p,r}\le\varepsilon/3$. Como $F(p),F(q)$ están en sus respectivos intervalos, $|F(p)-F(q)|\le\varepsilon/3<\varepsilon$. El mismo $\Delta$ sirve para todos los puntos del cierre.

**Unicidad continua.** Si $G:\overline D\to\mathbb R$ es continua y coincide con $f$ en $D$, para un $p$ fijado y $\varepsilon>0$ su continuidad da un radio en el que $|G(x)-G(p)|<\varepsilon/2$. Una escala $r$ menor que ese radio y que $r_0$ hace que $E_{p,r}$ esté dentro de esa banda; por supremo e ínfimo, también $F(p)$ está en la banda cerrada correspondiente. Luego $|F(p)-G(p)|\le\varepsilon/2<\varepsilon$. Como esto vale para todo $\varepsilon>0$, son iguales.

La raíz en $(0,1]$ se extiende a cero con valor cero, y la identidad se extiende igualmente. La función $1/x$ no tiene extensión real continua en cero y ya falló uniformidad. En un dominio acotado, su cierre es compacto por C16; por tanto una función admite extensión continua al cierre si y sólo si es uniforme: R7 da una dirección y Heine–Cantor más restricción da la otra. No se ha empleado selección numerable ni anticipado teoría de límites uniformes de funciones.

### Microcontroles

[]{#MA-MIC-ANM-01-017-049}

1. ¿Qué garantiza que $E_{p,r}$ no sea vacía?

[]{#MA-MIC-ANM-01-017-050}

2. ¿Cómo se acotan las imágenes locales sin elegir aproximantes globales?

[]{#MA-MIC-ANM-01-017-051}

3. ¿Qué corte define el valor extendido?

[]{#MA-MIC-ANM-01-017-052}

4. ¿Por qué ese corte no supera ningún $U_{p,r}$?

[]{#MA-MIC-ANM-01-017-053}

5. ¿Qué hace único al valor entre todos los intervalos?

[]{#MA-MIC-ANM-01-017-054}

6. ¿Por qué la extensión coincide con $f$ en $D$?

[]{#MA-MIC-ANM-01-017-055}

7. ¿Qué radio uniforme sobre el cierre se obtiene en la prueba?

[]{#MA-MIC-ANM-01-017-056}

8. ¿Se necesita una sucesión aproximante por punto de frontera?

## 17.8. Datos finitos y aproximaciones poligonales

[]{#MA-SEC-ANM-01-017-008}

El radio común permite elegir un número finito de muestras que controle también lo que ocurre entre ellas. No pretendemos reconstruir una función arbitraria exactamente, ni evaluar computablemente todos sus valores: probaremos existencia de una aproximación finita con error certificado.

**R8. Aproximación poligonal de una continua en un segmento.** Sea $f:[a,b]\to\mathbb R$ continua, $a<b$, y $\varepsilon>0$. R3 proporciona $\delta>0$ uniforme con tolerancia $\varepsilon/2$. Por arquimedianidad elegimos un entero $n\ge1$ tal que

$$h=\frac{b-a}{n}<\delta.$$

Definimos nodos $t_j=a+jh$, $0\le j\le n$. En cada celda $[t_j,t_{j+1}]$, la función interpolante es

$$P(x)=(1-\theta)f(t_j)+\theta f(t_{j+1}),
\qquad \theta=\frac{x-t_j}{h}\in[0,1].$$

En un nodo compartido ambas fórmulas dan el mismo valor $f(t_j)$, así la regla define una función sobre todo el segmento. Cada rama es afín continua, y el pegado finito sobre segmentos cerrados relativos, demostrado en C14, hace continua a $P$.

Para $x$ en esa celda, sus distancias a ambos nodos son a lo sumo $h<\delta$. Entonces ambas diferencias $|f(t_j)-f(x)|$ y $|f(t_{j+1})-f(x)|$ son menores que $\varepsilon/2$. Por combinación convexa y desigualdad triangular,

$$|P(x)-f(x)|
\le(1-\theta)|f(t_j)-f(x)|+\theta|f(t_{j+1})-f(x)|
<\varepsilon/2.$$

La última desigualdad también vale si un peso es cero: el otro es uno y su error mantiene la cota estricta. Por C16, la continua $|P-f|$ alcanza máximo en el segmento; su máximo es menor que $\varepsilon/2$ y, por tanto, menor que $\varepsilon$. Sin invocar la consecución de ese máximo, el supremo de errores ya sería a lo sumo $\varepsilon/2<\varepsilon$. Para $a=b$, la constante con valor $f(a)$ da error cero. En el segmento vacío la afirmación es vacía.

![La poligonal interpola x² en los nodos 0,1/4,1/2,3/4,1. En cada celda, P(x)−x²=(x−t)(t+1/4−x) y el máximo es 1/64, alcanzado en 1/8,3/8,5/8,7/8. El cálculo es algebraico, sin derivadas ni convexidad futura. Para una continua general, el radio uniforme da existencia de una malla suficientemente fina, sin promesa de evaluación computable.](../../assets/books/anm/C17/C17-F08.svg){#fig-anm-c17-f08 fig-alt="La poligonal interpola x² en los nodos 0,1/4,1/2,3/4,1. En cada celda, P(x)−x²=(x−t)(t+1/4−x) y el máximo es 1/64, alcanzado en 1/8,3/8,5/8,7/8. El cálculo es algebraico, sin derivadas ni convexidad futura. Para una continua general, el radio uniforme da existencia de una malla suficientemente fina, sin promesa de evaluación computable."}

**Certificado exacto para el cuadrado.** En $[0,1]$, tomando $f(x)=x^2$ y una malla de paso $h=1/n$, dentro de una celda con extremo izquierdo $t$ y $x=t+\theta h$, la expansión algebraica da

$$P(x)-x^2=\theta(1-\theta)h^2
=(x-t)(t+h-x)\ge0.$$

Como $(2\theta-1)^2\ge0$, $\theta(1-\theta)\le1/4$. El error máximo exacto es $h^2/4$, alcanzado en el medio de cada celda. Para $n=4$ es $1/64$. No se usaron derivadas, convexidad como teorema futuro ni fórmulas de error que requieran segundas derivadas.

La malla funciona por el radio uniforme, no por proximidad a un centro privilegiado. Una lista finita de muestras sin una hipótesis que controle lo que pasa entre nodos no da una garantía de error: entre dos nodos de una lista se puede insertar un pico triangular continuo, de altura arbitraria, que vale cero en todos ellos. R3 garantiza una escala para cada función dada; no un radio común para todas las continuas sin más restricciones.

El capítulo deja tres formas de leer la misma disciplina: elegir el radio antes de los pares, reducir una cubierta con margen antes de tomar mínimos, y transportar un presupuesto de salida hacia una escala de entrada. Las consecuencias —operaciones, rutas, frontera y aproximación finita— declaran qué hipótesis gastan. La diferenciabilidad del siguiente capítulo añadirá otra herramienta local; ninguna prueba actual depende de ella.

### Microcontroles

[]{#MA-MIC-ANM-01-017-057}

1. ¿Qué condición cumple el paso de la malla?

[]{#MA-MIC-ANM-01-017-058}

2. ¿Por qué coinciden las fórmulas de dos celdas en un nodo?

[]{#MA-MIC-ANM-01-017-059}

3. ¿Qué mantiene a $\theta$ entre cero y uno?

[]{#MA-MIC-ANM-01-017-060}

4. ¿Cómo se controla el error entre las muestras?

[]{#MA-MIC-ANM-01-017-061}

5. ¿Por qué el pegado poligonal es continuo?

[]{#MA-MIC-ANM-01-017-062}

6. ¿Cuál es el error máximo del cuadrado con cuatro celdas iguales?

[]{#MA-MIC-ANM-01-017-063}

7. ¿Por qué muestras finitas sin escala no dan error certificado?

[]{#MA-MIC-ANM-01-017-064}

8. ¿Qué aproximante sirve en un segmento degenerado?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html)

[← Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Capítulo 18 →](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html)
