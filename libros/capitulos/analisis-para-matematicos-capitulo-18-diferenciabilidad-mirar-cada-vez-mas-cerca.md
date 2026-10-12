---
content-id: MA-BCH-0274
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-018
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
title: 'Capítulo 18 — Diferenciabilidad: mirar cada vez más cerca'
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C18.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)

Una secante compara cambios de valores; una derivada identifica un único límite finito de esas pendientes. Al ampliar alrededor del centro, esa pendiente será la única recta cuyo error se vuelve pequeño en relación con la escala de entrada. Estudiaremos lo que esta información permite y las hipótesis que impiden convertirla en conclusiones demasiado fuertes.

Los prerrequisitos centrales son límites relativos de C13 y continuidad de C14. Acumulación y densidad C04, rutas dadas C06, raíces C10 y tipos/finitud C12 son interfaces heredadas. C15/C16 sólo se mencionan como garantías adicionales de continuidad de inversas. Todas las reglas se prueban antes de reutilizarlas. No usamos Rolle, valor medio, convexidad, Taylor ni integrales; el zoom se controla por estimaciones explícitas dentro de marcos admisibles.

## 18.1. Pendientes con un centro fijo

[]{#MA-SEC-ANM-01-018-001}

La secante conserva un extremo en $(a,f(a))$ y mueve el otro dentro del dominio. Su pendiente compara cambio de salida con cambio de entrada. Para hablar de un límite de pendientes debemos poder acercarnos al centro con puntos distintos de él.

**R1 — Derivada relativa.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Definimos una función perforada
$$q_{f,a}:D\setminus\{a\}\to\mathbb R,\qquad q_{f,a}(x)=\frac{f(x)-f(a)}{x-a}.$$
Decimos que $f$ es diferenciable o derivable en $a$, relativamente a $D$, si existe un real $L$ tal que
$$\forall\eta>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ |q_{f,a}(x)-L|<\eta.$$
La unicidad del límite de C13 hace único a $L$, que escribimos $f'(a)$. El dominio de $q$ no contiene $a$: la notación $f'(a)$ designa un límite, nunca una división por cero. El valor $f(a)$ sí interviene en cada secante.

**Por qué la acumulación es necesaria.** Si $a$ fuera aislado, un radio sin otros puntos haría verdadera la condición para cualquier $L$. Por ejemplo, una función en $\{0\}$ no tendría una pendiente identificada. Nuestra definición excluye esa vacuidad. En $D=[0,\infty)$, el cero sí es de acumulación; el límite relativo usa sólo entradas positivas. Hay que indicar ese dominio: una derivada derecha no es automáticamente una derivada bilateral en $\mathbb R$.

**Primera reutilización.** Para $f(x)=mx+b$ en $\mathbb R$, $q_{f,a}=m$ y $f'(a)=m$. Para $f(x)=x^2$,
$$q_{f,a}(a+h)=2a+h\qquad(h\ne0).$$
El radio $\delta=\eta$ prueba $f'(a)=2a$ para cada $a$. En particular las secantes del cuadrado centradas en uno tienen pendientes $2+h$, que convergen a dos desde ambos lados. Para $x^3$ en cero el cociente es $h^2$, con radio $\sqrt\eta$. Una pendiente infinita no es un real $L$; la raíz en cero tendrá precisamente esa dificultad.

![Para x² en a=1, las secantes de incrementos 1/2, −1/2 y 1/10 tienen pendientes 5/2, 3/2 y 21/10. La función de pendientes es 2+h para h≠0; el círculo abierto recuerda que no se evalúa el cociente en h=0. El límite es dos, probado para todos los argumentos por R1.](../../assets/books/anm/C18/C18-F01.svg){#fig-anm-c18-f01 fig-alt="Para x² en a=1, las secantes de incrementos 1/2, −1/2 y 1/10 tienen pendientes 5/2, 3/2 y 21/10. La función de pendientes es 2+h para h≠0; el círculo abierto recuerda que no se evalúa el cociente en h=0. El límite es dos, probado para todos los argumentos por R1."}

**Restricción que conserva el centro.** Si $a\in A\subseteq D$ y $a\in\operatorname{Acc}(A)$, una derivada respecto de $D$ conserva su valor respecto de $A$: los mismos radios sirven sobre menos entradas. La recíproca falla: restringir $|x|$ a $[0,\infty)$ elimina las secantes izquierdas. Si $A$ coincide con $D$ dentro de alguna bola centrada en $a$, la acumulación y las pendientes cercanas se conservan en ambos sentidos. Para un radio arbitrario $r$, un testigo de acumulación en una bola menor que $\min(r,\rho)$ pertenece también a $A$.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-001}

1. ¿Dónde vive el cociente incremental centrado en $a$?

[]{#MA-MIC-ANM-01-018-002}

2. ¿Por qué se exige $a\in\operatorname{Acc}(D)$?

[]{#MA-MIC-ANM-01-018-003}

3. ¿Qué variables están fijadas antes de elegir el radio de derivabilidad?

[]{#MA-MIC-ANM-01-018-004}

4. ¿Cuál es la derivada de $x^2$ en $a$ y qué identidad la prueba?

[]{#MA-MIC-ANM-01-018-005}

5. ¿Una pendiente secante muy grande equivale a una derivada real?

[]{#MA-MIC-ANM-01-018-006}

6. ¿Qué debe conservar una restricción para heredar la derivada?

[]{#MA-MIC-ANM-01-018-007}

7. ¿Qué derivada relativa tiene $|x|$ en cero sobre $[0,\infty)$?

[]{#MA-MIC-ANM-01-018-008}

8. ¿Tiene derivada según R1 una función en un singleton?

## 18.2. El error que desaparece al ampliar

[]{#MA-SEC-ANM-01-018-002}

Una recta que pase por el punto puede tener error absoluto tendente a cero sin tener la pendiente correcta. La escala relevante compara ese error con el incremento que estamos ampliando.

**R2 — Mejor aproximación lineal local.** Con los tipos y el centro de R1, sea
$$r_L(x)=f(x)-f(a)-L(x-a),\qquad r_L(a)=0.$$
Entonces $f'(a)=L$ si y sólo si
$$\forall\eta>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\ |r_L(x)|<\eta|x-a|.$$
**Estrategia y prueba.** Restamos la recta candidata y dividimos únicamente en el dominio perforado. Allí
$$\frac{r_L(x)}{x-a}=q_{f,a}(x)-L,$$
así la condición es exactamente el límite cero de este cociente. Esta equivalencia prueba existencia en ambos sentidos, sin una fórmula futura de Taylor. La notación $r_L(x)=o(|x-a|)$ abrevia esta condición relativa; no designa una función nueva ni una cota cuadrática obligatoria.

**Unicidad desde el error.** Si $L$ y $M$ sirvieran y $d=|L-M|>0$, pedimos a ambas estimaciones presupuesto $d/3$. Tomamos el mínimo de sus dos radios y un solo testigo $x\in D$ distinto de $a$ dentro de él, obtenido de la acumulación. Como $r_M-r_L=(L-M)(x-a)$, al dividir magnitudes resulta $d<2d/3$, contradicción. No se elige una sucesión de testigos.

**Zoom con la misma escala en los dos ejes.** Para $t>0$ y entradas admisibles $u$ tales que $a+tu\in D$, definimos
$$G_t(u)=\frac{f(a+tu)-f(a)}t.$$
Si $|u|\le R$ y $0<t<\delta/(R+1)$, la estimación anterior da $|G_t(u)-Lu|<\eta|u|\le\eta R$ para $u\ne0$; en $u=0$ el error es cero. Para un presupuesto $\varepsilon>0$ elegimos primero $\eta=\varepsilon/(R+1)$ y luego ese límite para $t$. Todos los puntos admisibles del marco $|u|\le R$ quedan a error menor que $\varepsilon$. Si $D$ contiene una vecindad de $a$, todo el marco se vuelve admisible para $t$ pequeño; en dominios rotos hay que conservar el conjunto de $u$ permitido. Aquí se prueba una estimación común, sin introducir teoría de sucesiones de funciones.

![Para el cuadrado en a=1, G_t(u)=2u+tu². Los tres paneles usan el mismo marco |u|≤2 y los mismos ejes; el error respecto de 2u está acotado por 4t. Se ilustran t=1/2,1/8,1/32. La prueba controla todos los puntos del marco, sin inferir el límite de tres imágenes.](../../assets/books/anm/C18/C18-F02.svg){#fig-anm-c18-f02 fig-alt="Para el cuadrado en a=1, G_t(u)=2u+tu². Los tres paneles usan el mismo marco |u|≤2 y los mismos ejes; el error respecto de 2u está acotado por 4t. Se ilustran t=1/2,1/8,1/32. La prueba controla todos los puntos del marco, sin inferir el límite de tres imágenes."}

**Ejemplo y diagnóstico.** Para el cuadrado, $r_{2a}(a+h)=h^2$ y $G_t(u)=2au+tu^2$. La desaparición del término $tu^2$ explica el acercamiento a la recta dentro de un marco acotado. Con otra pendiente $M$, el error absoluto $(2a-M)h+h^2$ también tiende a cero, pero su cociente por $h$ tiende a $2a-M$, que sólo es cero para $M=2a$. «Mejor» significa única recta con error de orden menor que $|h|$, sin afirmar que minimice cada error a distancia finita.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-009}

1. ¿Qué error identifica la pendiente correcta?

[]{#MA-MIC-ANM-01-018-010}

2. ¿Por qué error absoluto tendente a cero no identifica $L$?

[]{#MA-MIC-ANM-01-018-011}

3. ¿Cuánto vale el resto del cuadrado con pendiente $2a$?

[]{#MA-MIC-ANM-01-018-012}

4. ¿Qué papel cumple la acumulación en la unicidad del modelo?

[]{#MA-MIC-ANM-01-018-013}

5. ¿Qué entradas admite $G_t(u)$?

[]{#MA-MIC-ANM-01-018-014}

6. ¿Por qué se limita el marco de zoom a $|u|\le R$?

[]{#MA-MIC-ANM-01-018-015}

7. ¿Qué significa $o(|x-a|)$ en este capítulo?

[]{#MA-MIC-ANM-01-018-016}

8. ¿La recta de R2 minimiza necesariamente todo error a distancia finita?

## 18.3. Continuidad, esquinas y alcance del control

[]{#MA-SEC-ANM-01-018-003}

El límite finito de pendientes tiene una consecuencia inmediata sobre valores. Conviene demostrarla antes de usar álgebra o composición de derivadas.

**R3 — Diferenciabilidad implica continuidad.** Sean $L=f'(a)$ y $C=|L|+1>0$. La tolerancia uno en R1 entrega un radio $r$ para el que $|q_{f,a}(x)|<C$ en la bola perforada. Por tanto
$$|f(x)-f(a)|<C|x-a|\qquad(0<|x-a|<r,\ x\in D).$$
Para $\varepsilon>0$, $\delta=\min(r,\varepsilon/C)$ controla el error de salida por $\varepsilon$ si $x\ne a$; si $x=a$, el error vale cero. Ésta es la continuidad de C14 sobre el mismo dominio. También queda la cota no estricta $|f(x)-f(a)|\le C|x-a|$ incluyendo el centro.

**La cota tiene un centro fijo.** No controla automáticamente $|f(x)-f(y)|$ por $C|x-y|$ para cualquier par vecino. Para ver la diferencia, definamos $F:\mathbb R\to\mathbb R$ por $F(x)=x^2$ si $x\in\mathbb Q$ y $F(x)=0$ si $x\notin\mathbb Q$. En cero, $F(0)=0$ y $|q_{F,0}(x)|\le|x|$, así $F'(0)=0$. En cualquier $b\ne0$, la densidad de racionales e irracionales impide continuidad. Si $b$ es racional, irracionales arbitrariamente próximos tienen salida cero, separada de $b^2$. Si es irracional, racionales próximos con $|x-b|<|b|/2$ tienen $x^2>b^2/4$ mientras $F(b)=0$. Un control Lipschitz para todos los pares de alguna vecindad de cero implicaría continuidad en sus puntos interiores, contradicción. Diferenciabilidad en un punto no asegura diferenciabilidad cerca.

**Una esquina continua.** La triangular inversa da $||x|-|y||\le|x-y|$, por lo que $|x|$ es continua. Su cociente en cero vale uno para $x>0$ y menos uno para $x<0$. Si existiera un límite $L$, con tolerancia $1/2$ y testigos $\pm\delta/2$ tendríamos $|1-L|<1/2$ y $|-1-L|<1/2$, contradiciendo $2\le|1-L|+|L+1|$. Una gráfica puede mostrar la esquina; los dos testigos refutan todo radio candidato.

![La función |x| es continua en cero, pero su cociente perforado vale −1 a la izquierda y 1 a la derecha. Los puntos abiertos indican que el cociente no se define en cero. R3 refuta cualquier límite común mediante los testigos ±δ/2. Sobre el dominio no negativo sólo permanece la rama derecha.](../../assets/books/anm/C18/C18-F03.svg){#fig-anm-c18-f03 fig-alt="La función |x| es continua en cero, pero su cociente perforado vale −1 a la izquierda y 1 a la derecha. Los puntos abiertos indican que el cociente no se define en cero. R3 refuta cualquier límite común mediante los testigos ±δ/2. Sobre el dominio no negativo sólo permanece la rama derecha."}

**Pendiente nula no significa constancia.** $x^3$ tiene derivada cero en cero y cambia de signo allí: no es constante ni tiene extremo en ese punto. El dato sólo identifica su recta local horizontal. Si $L>0$, la tolerancia $L/2$ sí asegura que $q_{f,a}(x)>0$ cerca: las salidas a la derecha superan $f(a)$ y las de la izquierda quedan por debajo. Son comparaciones con $a$, sin una conclusión sobre todos los pares de la vecindad. El paso a propiedades en intervalos exigirá otras herramientas.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-017}

1. ¿Qué tolerancia inicial produce una cota de pendientes?

[]{#MA-MIC-ANM-01-018-018}

2. ¿Cómo se trata el argumento $x=a$ al demostrar continuidad?

[]{#MA-MIC-ANM-01-018-019}

3. ¿Qué radio transforma la cota $C|x-a|$ en error menor que $\varepsilon$?

[]{#MA-MIC-ANM-01-018-020}

4. ¿Por qué falla la derivada bilateral de $|x|$ en cero?

[]{#MA-MIC-ANM-01-018-021}

5. ¿Pendiente nula en un punto implica constancia cerca?

[]{#MA-MIC-ANM-01-018-022}

6. ¿Qué centro queda fijo en la cota de R3?

[]{#MA-MIC-ANM-01-018-023}

7. ¿Qué derivada tiene en cero la función racional/irracional de R3?

[]{#MA-MIC-ANM-01-018-024}

8. ¿Qué comparación local permite $f\prime(a)>0$?

## 18.4. Operaciones sobre incrementos

[]{#MA-SEC-ANM-01-018-004}

Las reglas algebraicas serán identidades de incrementos seguidas de límites. Hay que justificar los dominios antes de cancelar denominadores.

**R4 — Suma y producto.** Sean $f,g:D\to\mathbb R$ derivables en $a\in D\cap\operatorname{Acc}(D)$, con derivadas $L,M$. Para constantes $\alpha,\beta$, la identidad $q_{\alpha f+\beta g,a}=\alpha q_{f,a}+\beta q_{g,a}$ y el álgebra de límites C13 dan
$$ (\alpha f+\beta g)'(a)=\alpha L+\beta M.$$
Para el producto, sumar y restar $f(a)g(x)$ produce
$$q_{fg,a}(x)=f(x)q_{g,a}(x)+g(a)q_{f,a}(x).$$
R3 asegura $f(x)\to f(a)$; C13 permite multiplicar los límites finitos. Así $(fg)'(a)=f(a)M+g(a)L$. La continuidad se usa exactamente para el factor no centrado. Todos los cocientes viven en $D\setminus\{a\}$; no se ha aplicado la cadena.

**Recíproco y cociente.** Si $g(a)\ne0$, continuidad con tolerancia $|g(a)|/2$ da $\rho>0$ tal que $|g(x)|>|g(a)|/2$ en $D\cap B(a,\rho)$. El dominio efectivo $E=\{x\in D:g(x)\ne0\}$ contiene esa vecindad relativa y acumula en $a$. Las derivadas de las restricciones conservan sus valores por R1. En $E\setminus\{a\}$,
$$q_{1/g,a}(x)=-\frac{q_{g,a}(x)}{g(x)g(a)}.$$
Los límites del denominador y el margen anterior justifican
$$ (1/g)'(a)=-\frac{M}{g(a)^2},\qquad
(f/g)'(a)=\frac{L g(a)-f(a)M}{g(a)^2}.$$
La segunda fórmula resulta del producto de $f|_E$ con $1/g$, ambos tipados $E\to\mathbb R$. Es una derivada relativa a $E$, aunque use datos calculados primero sobre $D$.

**Reutilización finita.** De $(x)'=1$, constantes y producto se obtiene por inducción $(x^n)'(a)=na^{n-1}$ para enteros $n\ge1$ en $\mathbb R$. La potencia cero es constante uno y su derivada es cero, sin escribir $0a^{-1}$ en $a=0$. Para enteros $n\ge1$, el recíproco da $(x^{-n})'(a)=-na^{-n-1}$ en $\mathbb R\setminus\{0\}$. Sumas finitas derivan polinomios; cocientes derivan funciones racionales en sus dominios efectivos. No se extiende esta prueba a exponentes reales no construidos.

**Cancelar no cambia el dominio.** $x/x$ en $\mathbb R\setminus\{0\}$ vale uno y tiene derivada cero en cada punto de ese dominio. En cero no hay valor ni derivada. La constante uno en $\mathbb R$ es una extensión distinta. Si numerador y denominador se anulan en el centro, la regla de cociente no sirve; se debe estudiar una extensión expresamente definida, si existe.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-025}

1. ¿Qué factor requiere continuidad en la prueba del producto?

[]{#MA-MIC-ANM-01-018-026}

2. ¿Qué dominio comparte la regla de suma?

[]{#MA-MIC-ANM-01-018-027}

3. ¿Qué margen da $g(a)\ne0$ junto con continuidad?

[]{#MA-MIC-ANM-01-018-028}

4. ¿Cuál es el dominio efectivo de $f/g$?

[]{#MA-MIC-ANM-01-018-029}

5. ¿Por qué ese dominio efectivo acumula en $a$?

[]{#MA-MIC-ANM-01-018-030}

6. ¿Qué signo aparece en la derivada de $1/g$?

[]{#MA-MIC-ANM-01-018-031}

7. ¿Cómo se trata la potencia cero en el origen?

[]{#MA-MIC-ANM-01-018-032}

8. ¿Cancelar $x/x$ añade cero al dominio original?

## 18.5. La cadena cuando el incremento interior se anula

[]{#MA-SEC-ANM-01-018-005}

En una composición, puede variar $x$ mientras el valor interior permanece igual. Dividir por ese cambio interior perdería argumentos válidos.

**R5 — Regla de la cadena.** Sean $g:D\to E$, $f:E\to\mathbb R$, $a\in D\cap\operatorname{Acc}(D)$ y $b=g(a)\in E\cap\operatorname{Acc}(E)$. Supongamos $g'(a)=L$ y $f'(b)=M$. Construimos la función auxiliar
$$A:E\to\mathbb R,\qquad
A(y)=\begin{cases}\dfrac{f(y)-f(b)}{y-b},&y\ne b,\\ M,&y=b.\end{cases}$$
Es continua en $b$: en argumentos perforados lo dice la definición de $M$; en $b$ la diferencia respecto de $M$ vale cero. No se ha definido un cociente con denominador cero; $A$ es otra función. Para todo $y\in E$ se tiene $f(y)-f(b)=A(y)(y-b)$, también si $y=b$, porque ambos lados valen cero.

**Identidad y paso al límite.** Para todo $x\in D\setminus\{a\}$,
$$q_{f\circ g,a}(x)=A(g(x))q_{g,a}(x).$$
R3 da continuidad de $g$ en $a$; C14 da $A(g(x))\to M$, incluso en los puntos que llegan exactamente a $b$. El álgebra de límites C13 concluye $(f\circ g)'(a)=ML$. Para ver los presupuestos, fijamos $C=|L|+1$: cerca del centro $|q_g|<C$. Pedimos a $A\circ g$ error $\varepsilon/(2C)$ y a $q_g$ error $\varepsilon/[2(|M|+1)]$, además de su cota. El mínimo de los radios da
$$|A(g(x))q_g(x)-ML|\le |A(g(x))-M||q_g(x)|+|M||q_g(x)-L|<\varepsilon.$$
La única división en la identidad es por $x-a\ne0$. No se exige $L\ne0$ ni que $g[D]$ acumule en $b$; una función interior constante queda incluida.

![La interior vale 1 para x<0 y 1+x² para x≥0. Su derivada en cero es cero; la exterior y² tiene derivada dos en uno. La composición tiene derivada cero. En toda la rama negativa el incremento interior es cero: el factor A(1)=2 conserva la identidad de cocientes multiplicándolo por q_g=0, sin división 0/0.](../../assets/books/anm/C18/C18-F04.svg){#fig-anm-c18-f04 fig-alt="La interior vale 1 para x&lt;0 y 1+x² para x≥0. Su derivada en cero es cero; la exterior y² tiene derivada dos en uno. La composición tiene derivada cero. En toda la rama negativa el incremento interior es cero: el factor A(1)=2 conserva la identidad de cocientes multiplicándolo por q_g=0, sin división 0/0."}

**Detención de la función interior.** Sea $g(x)=1$ para $x<0$ y $g(x)=1+x^2$ para $x\ge0$. En cero, $q_g(x)=0$ a la izquierda y $q_g(x)=x$ a la derecha; $g'(0)=0$. Para $f(y)=y^2$, $f'(1)=2$ y $(f\circ g)'(0)=0$. El cociente que divide por $g(x)-1$ no existe en ningún $x<0$; la identidad con $A$ sigue siendo válida allí.

**Si no está dada la inclusión de imágenes.** Para $g:D\to\mathbb R$ y $f:E\to\mathbb R$, el dominio de composición es $T=\{x\in D:g(x)\in E\}$. Hay que exigir $a\in T\cap\operatorname{Acc}(T)$, restringir $g$ a $T$ y cambiar su codominio a $E$. La acumulación no se deduce de la de $D$ y $E$: con $g(x)=x^2$, $E=(-\infty,0]$ y $D=\mathbb R$, resulta $T=\{0\}$. Incluso si $f(y)=y$ es derivable relativamente a $E$ en cero, la composición sobre ese singleton no tiene derivada según R1.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-033}

1. ¿Qué división falla si $g(x)=g(a)$?

[]{#MA-MIC-ANM-01-018-034}

2. ¿Qué valor se asigna al factor exterior $A$ en $b$?

[]{#MA-MIC-ANM-01-018-035}

3. ¿Por qué $A$ es continua en $b$?

[]{#MA-MIC-ANM-01-018-036}

4. ¿Qué identidad admite incremento interior cero?

[]{#MA-MIC-ANM-01-018-037}

5. ¿Exige la cadena una derivada interior no nula?

[]{#MA-MIC-ANM-01-018-038}

6. ¿Qué inclusión de tipos simplifica la composición?

[]{#MA-MIC-ANM-01-018-039}

7. ¿Qué condición adicional hay que verificar sobre un dominio efectivo $T$?

[]{#MA-MIC-ANM-01-018-040}

8. ¿La imagen de una función interior constante acumula en su valor?

## 18.6. Invertir la pendiente exige volver al punto

[]{#MA-SEC-ANM-01-018-006}

La pendiente inversa intercambia cambio de entrada y salida. Pero una salida próxima al valor central debe recuperar una entrada próxima al centro original.

**R6 — Derivada de la inversa.** Sea $f:D\to\mathbb R$ inyectiva, $a\in D\cap\operatorname{Acc}(D)$ y $f'(a)=L\ne0$. Ponemos $H=f[D]$, $b=f(a)$ y construimos la inversa $h:H\to D$, considerada con los mismos valores como función real $h:H\to\mathbb R$. Suponemos explícitamente que es continua en $b$ respecto de $H$. Entonces $h'(b)=1/L$.

**Metas intermedias y prueba.** Primero $b\in\operatorname{Acc}(H)$. Para $\rho>0$, continuidad de $f$ en $a$ da $\delta$ con error menor que $\rho$. La acumulación de $D$ proporciona un $x\ne a$ dentro de ese radio, y la inyectividad asegura $f(x)\ne b$. Así $0<|f(x)-b|<\rho$. El dominio perforado de la inversa es legítimo.

Después pedimos a $q_{f,a}$ error $|L|/2$; en algún radio $r$ resulta $|q_{f,a}|>|L|/2$. Para una tolerancia final $\varepsilon$, otro radio $s$ asegura error menor que $\varepsilon|L|^2/2$. Continuidad de $h$ da $\eta>0$ tal que $|y-b|<\eta$, $y\in H$, implica $|h(y)-a|<\min(r,s)$. Si $y\ne b$, inyectividad fuerza $h(y)\ne a$, y
$$q_{h,b}(y)=\frac1{q_{f,a}(h(y))},\qquad
\left|q_{h,b}(y)-\frac1L\right|
=\frac{|q_{f,a}(h(y))-L|}{|L|\,|q_{f,a}(h(y))|}<\varepsilon.$$
Esto prueba existencia de la derivada de $h$ sin derivar primero la identidad $f\circ h=\mathrm{id}$. Aquella derivación sería circular si aún no sabemos que $h$ es derivable. Inyectividad construye la inversa; continuidad aproxima entradas recuperadas; $L\ne0$ separa el denominador de cero.

![Para el cuadrado no negativo, el par 1,3/2 produce valores 1,9/4 y pendiente 5/2. La inversa raíz intercambia coordenadas y tiene pendiente secante 2/5 para ese par. En los centros 1, las pendientes límite son dos y un medio. R6 justifica el paso al límite con inversa continua y pendiente original no nula.](../../assets/books/anm/C18/C18-F05.svg){#fig-anm-c18-f05 fig-alt="Para el cuadrado no negativo, el par 1,3/2 produce valores 1,9/4 y pendiente 5/2. La inversa raíz intercambia coordenadas y tiene pendiente secante 2/5 para ese par. En los centros 1, las pendientes límite son dos y un medio. R6 justifica el paso al límite con inversa continua y pendiente original no nula."}

**Raíz con centro positivo.** En $D=[0,\infty)$, el cuadrado es inyectivo y su inversa es $\sqrt y$ por C10. En $b=a^2>0$,
$|\sqrt y-a|=|y-a^2|/(\sqrt y+a)\le|y-a^2|/a$, de modo que la inversa es continua. R6 da $(\sqrt y)'|_{y=b}=1/(2a)$. En cero, el cuadrado tiene derivada relativa cero, pero el cociente de su inversa es $1/\sqrt y$ para $y>0$ y crece sin cota al acercarse a cero; no hay derivada finita allí. Para cualquier cota $B>0$ y radio $r>0$, tomar $0<y<\min(r,1/(B+1)^2)$ da cociente mayor que $B$.

**La continuidad de la inversa no es automática.** Sea $D=[0,1)\cup[2,3]$, con $f(x)=x$ en la primera pieza y $f(x)=x-1$ en la segunda. Es inyectiva, tiene imagen $H=[0,2]$ y derivada relativa uno en $a=2$. Sin embargo $h(1)=2$, mientras $y_n=1-1/(n+2)$ satisface $h(y_n)=y_n\to1$. La inversa no es continua en $b=1$; R3 impide que sea derivable allí. En compactos, C16 proporciona continuidad de la inversa de una función continua e inyectiva; en intervalos, se puede usar la interfaz correspondiente de C15. Son garantías adicionales sobre el dominio, no parte oculta de R6.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-041}

1. ¿Qué hipótesis construye una inversa única sobre la imagen?

[]{#MA-MIC-ANM-01-018-042}

2. ¿Qué asegura la acumulación de la imagen en $f(a)$?

[]{#MA-MIC-ANM-01-018-043}

3. ¿Qué hipótesis aproxima $h(y)$ a $a$ cuando $y$ se acerca a $b$?

[]{#MA-MIC-ANM-01-018-044}

4. ¿Para qué se exige $L\ne0$?

[]{#MA-MIC-ANM-01-018-045}

5. ¿Por qué $y\ne b$ implica $h(y)\ne a$?

[]{#MA-MIC-ANM-01-018-046}

6. ¿Cuál es la derivada de la raíz en $b>0$?

[]{#MA-MIC-ANM-01-018-047}

7. ¿Por qué no se deriva primero $f\circ h=\mathrm{id}$ para probar R6?

[]{#MA-MIC-ANM-01-018-048}

8. ¿Qué falla para la raíz en cero?

## 18.7. Una derivada es otra función

[]{#MA-SEC-ANM-01-018-007}

Cuando cambiamos el centro obtenemos otra función, con su propio dominio. Que cada derivada exista no significa que sus valores dependan continuamente del centro.

**R7 — Dominio de la función derivada.** Definimos
$$\operatorname{Diff}(f)=\{a\in D\cap\operatorname{Acc}(D):f\text{ es derivable en }a\},\qquad
f':\operatorname{Diff}(f)\to\mathbb R.$$
R1 da un valor único por punto, así esta regla determina una función, sin escoger entre pendientes. Para $|x|$ sobre $\mathbb R$, el dominio es $\mathbb R\setminus\{0\}$; sus valores son $-1$ a la izquierda y $1$ a la derecha. El límite de esta función en cero puede preguntarse porque cero acumula en su dominio; su continuidad en cero no puede afirmarse porque no está definido allí.

**Ejemplo sin herramientas trigonométricas.** Para $n\in\mathbb N$ (desde cero), sean $c_n=2^{-(n+1)}$, $w_n=c_n^2/8$ y $I_n=[c_n-w_n,c_n+w_n]$. Los intervalos son positivos y disjuntos: entre centros consecutivos hay distancia $c_n/2$, mientras la suma de semianchos es $5c_n^2/32<c_n/2$. Todos quedan dentro de $[c_n/2,3c_n/2]$. Definimos $\phi(u)=(1-u^2)^2$ en $[-1,1]$ y
$$F(x)=\begin{cases}w_n\phi((x-c_n)/w_n),&x\in I_n\text{ para algún }n,\\0,&x\notin\bigcup_n I_n.\end{cases}$$
La disjunción evita valores incompatibles. En cada intervalo $0\le F(x)\le w_n\le x^2/2$, y fuera de ellos $F=0$. Como $F(0)=0$, $|q_{F,0}(x)|\le|x|/2$, de donde $F'(0)=0$.

**Comprobar los otros puntos.** En el interior de $I_n$, R4/R5 derivan el polinomio y dan
$$F'(x)=\phi'((x-c_n)/w_n)=-4u(1-u^2),\qquad u=(x-c_n)/w_n.$$
En los extremos, $\phi(\pm1)=\phi'(\pm1)=0$. Más explícitamente, si $e=c_n\pm w_n$ y $x$ está en la rama interior, $|\phi(u)|\le4|u\mp1|^2$, así $|F(x)|\le4|x-e|^2/w_n$. El cociente centrado en $e$ tiende a cero; en la rama exterior es cero. No se usa un teorema de pegado de derivadas sin probarlo. Cada punto distinto de cero tiene una vecindad que sólo puede tocar finitos intervalos: los centros de la cola tienden a cero; se separan después los intervalos restantes que no contienen el punto. Fuera de ellos hay una vecindad constante. Esto justifica las ramas anteriores y demuestra diferenciabilidad en toda $\mathbb R$.

![Se muestran n=0,…,4 de la familia con c_n=2^{−(n+1)}, w_n=c_n²/8 y perfil (1−u²)². Toda la función satisface 0≤F(x)≤x²/2 y F′(0)=0. En x_n=c_n+w_n/2, la derivada vale −3/2 para todo n, refutando continuidad de F′ en cero. La figura representa una muestra finita; disjunción, extremos, finitud local y cola se prueban en R7.](../../assets/books/anm/C18/C18-F06.svg){#fig-anm-c18-f06 fig-alt="Se muestran n=0,…,4 de la familia con c_n=2^{−(n+1)}, w_n=c_n²/8 y perfil (1−u²)². Toda la función satisface 0≤F(x)≤x²/2 y F′(0)=0. En x_n=c_n+w_n/2, la derivada vale −3/2 para todo n, refutando continuidad de F′ en cero. La figura representa una muestra finita; disjunción, extremos, finitud local y cola se prueban en R7."}

**La derivada no es continua.** Para $x_n=c_n+w_n/2$, tenemos $x_n\to0$ pero $F'(x_n)=\phi'(1/2)=-3/2$, distinto del valor $F'(0)=0$. La continuidad de $F'$ en cero exigiría diferencias menores que uno desde algún radio, contradichas por estos puntos explícitos. La amplitud de cada bulto es cuadrática respecto de su distancia al origen, suficiente para la derivada cero allí; su anchura permite pendientes interiores que no se hacen pequeñas. La figura muestra sólo una cantidad finita de bultos; la prueba controla toda la familia.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-049}

1. ¿Cuál es el dominio de $f\prime$?

[]{#MA-MIC-ANM-01-018-050}

2. ¿Puede preguntarse continuidad de $f\prime$ en un punto donde no está definida?

[]{#MA-MIC-ANM-01-018-051}

3. ¿Qué impide solapamiento de los intervalos $I_n$?

[]{#MA-MIC-ANM-01-018-052}

4. ¿Qué cota prueba $F\prime(0)=0$?

[]{#MA-MIC-ANM-01-018-053}

5. ¿Por qué coinciden las derivadas en los extremos de cada bulto?

[]{#MA-MIC-ANM-01-018-054}

6. ¿Qué puntos refutan continuidad de $F\prime$ en cero?

[]{#MA-MIC-ANM-01-018-055}

7. ¿Cómo se evita usar un pegado infinito sin justificación?

[]{#MA-MIC-ANM-01-018-056}

8. ¿La figura con varios bultos prueba el caso infinito?

## 18.8. Certificar una aproximación local

[]{#MA-SEC-ANM-01-018-008}

Una derivada identifica la recta local. Para convertirla en una aproximación con tolerancia hace falta una estimación del resto en el dominio donde se va a evaluar.

**R8 — De una cota a un certificado.** Si $f'(a)=L$ y para $|h|<\rho$, $a+h\in D$, se conoce
$$|f(a+h)-f(a)-Lh|\le B h^2\qquad(B\ge0),$$
entonces la aproximación $f(a)+Lh$ tiene error absoluto a lo sumo $Bh^2$. Si $B>0$, pedir además $|h|<\eta/B$ certifica error normalizado menor que $\eta$. Si $B=0$, el error es exactamente cero en esa vecindad. La existencia de la derivada sólo garantiza un resto $o(|h|)$, sin garantizar por sí sola una cota cuadrática o un algoritmo para encontrar radios.

**Un certificado por álgebra.** Para $f(x)=\sqrt x$ y $a=1$, R6 da $L=1/2$. Con $h>-1$ y $s=\sqrt{1+h}$, dos racionalizaciones dan la identidad exacta
$$\sqrt{1+h}=1+\frac h2-\frac{h^2}{2(\sqrt{1+h}+1)^2}.$$
Para $|h|\le1/2$, $s\ge0$ y por tanto el resto tiene magnitud a lo sumo $h^2/2$. En $h=1/100$, el valor aproximado es $201/200$ y el error está entre cero y $1/20000$ por debajo de esa recta. También $q_{f,1}(1+h)=1/(s+1)$ y $|q_{f,1}-1/2|\le|h|/2$. Son dos errores distintos: error del valor y error de la pendiente secante.

![En |h|≤1/2, el modelo 1+h/2 aproxima √(1+h) por encima. La identidad exacta da error h²/\[2(√(1+h)+1)²\]≤h²/2. En h=1/100, el modelo es 201/200 y el error es a lo sumo 1/20000. El panel de errores tiene su propia escala vertical; no es el error de pendiente secante, que divide por |h|.](../../assets/books/anm/C18/C18-F07.svg){#fig-anm-c18-f07 fig-alt="En |h|≤1/2, el modelo 1+h/2 aproxima √(1+h) por encima. La identidad exacta da error h²/\[2(√(1+h)+1)²\]≤h²/2. En h=1/100, el modelo es 201/200 y el error es a lo sumo 1/20000. El panel de errores tiene su propia escala vertical; no es el error de pendiente secante, que divide por |h|."}

**Existencia sin resto cuadrático.** Para $f(x)=|x|^{3/2}=|x|\sqrt{|x|}$, $f(0)=0$ y $|q_{f,0}(x)|=\sqrt{|x|}\to0$, así $f'(0)=0$. Si hubiera una cota $|x|^{3/2}\le Bx^2$ con $B>0$ en una vecindad perforada, tendríamos $1/\sqrt{|x|}\le B$, imposible. Aquí la potencia fraccionaria sólo abrevia producto y raíz ya construidos; no se ha usado una regla de potencias reales.

**Las muestras finitas no determinan la derivada.** Sea $S\subseteq\mathbb R$ finito con $0\in S$, y sea $c\in\mathbb R$ cualquier pendiente prescrita. El polinomio
$$p_c(x)=c x\prod_{s\in S\setminus\{0\}}\frac{x-s}{-s}$$
se anula en todos los puntos de $S$, pero $p_c'(0)=c$. Cada denominador es no nulo y el producto vacío vale uno. Para $x\ne0$, el cociente centrado en cero es $c$ por el producto de los factores, que tienden a uno; C13 prueba el límite $c$. Una tabla finita de ceros es compatible con cualquier pendiente. La certificación de la derivada exige control sobre todos los argumentos suficientemente cercanos, no sólo sobre secantes muestreadas.

**Herramientas que salen.** Disponemos de derivada relativa, único modelo lineal de primer orden, continuidad, reglas algebraicas, cadena sin división por incremento interior e inversa bajo continuidad y pendiente no nula. Sabemos distinguir el dominio de $f'$ y su continuidad, y certificar errores cuando tenemos una cota demostrada. Los próximos resultados deberán explicar cuándo información local en todos los centros gobierna un intervalo completo.

**Microcontroles.**

[]{#MA-MIC-ANM-01-018-057}

1. ¿Qué dato convierte una recta local en certificado cuadrático?

[]{#MA-MIC-ANM-01-018-058}

2. ¿Cuánto vale el modelo de $\sqrt{1+h}$ en $h=1/100$?

[]{#MA-MIC-ANM-01-018-059}

3. ¿En qué lado del valor exacto queda ese modelo de raíz?

[]{#MA-MIC-ANM-01-018-060}

4. ¿Qué diferencia hay entre error de valor y error de pendiente secante?

[]{#MA-MIC-ANM-01-018-061}

5. ¿La derivabilidad garantiza resto cuadrático?

[]{#MA-MIC-ANM-01-018-062}

6. ¿Qué significa el producto vacío en $p_c$?

[]{#MA-MIC-ANM-01-018-063}

7. ¿Qué derivada en cero tiene $p_c$ aunque sus muestras sean cero?

[]{#MA-MIC-ANM-01-018-064}

8. ¿Qué controla un certificado de derivada que no controla una tabla finita?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)

[← Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Capítulo 19 →](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html)
