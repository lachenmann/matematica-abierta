---
content-id: MA-BCH-0278
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-019
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
title: Capítulo 19 — De lo local a lo global
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C19.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html)

Una derivada describe un centro. Este capítulo demuestra cuándo las pendientes locales gobiernan valores separados: el intervalo conserva el segmento que une dos entradas, y las hipótesis de continuidad y derivabilidad permiten encontrar una pendiente interior que transporta su incremento.

Los prerrequisitos centrales son continuidad de C14 y diferenciabilidad de C18. Se usan explícitamente los extremos alcanzados sobre segmentos compactos de C16 para Rolle y Darboux, y el valor intermedio de C15 para existencia de una raíz. Límites, acumulación, raíces y finitud son interfaces heredadas. La cadena lógica es Fermat, Rolle y valor medio, seguida de consecuencias sobre signos, cotas, dos funciones, valores intermedios de derivadas y ceros. No suponemos continuidad de la función derivada ni usamos convexidad, segunda derivada, Taylor, integrales o L’Hôpital.

## 19.1. Un extremo interior obliga a detenerse

[]{#MA-SEC-ANM-01-019-001}

Una derivada describe el comportamiento cerca de un centro. Para obtener información en un intervalo completo necesitaremos que las condiciones valgan en todos sus puntos pertinentes. El primer puente es local: una función derivable no puede alcanzar un extremo interior con pendiente distinta de cero.

**R1 — Fermat.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a$ interior a $D$. Si $f$ tiene un máximo o mínimo local en $a$ y es derivable allí, entonces $f'(a)=0$. Un mínimo local significa que existe $r>0$ tal que $f(x)\ge f(a)$ para $x\in D$ con $|x-a|<r$; un máximo invierte la desigualdad. La interioridad proporciona $\rho>0$ con $B(a,\rho)\subseteq D$, y por tanto acumulación desde ambos lados.

**Estrategia y prueba para un mínimo.** En la vecindad del extremo, las pendientes secantes son no negativas a la derecha y no positivas a la izquierda. Sea $L=f'(a)$. Si $L>0$, tolerancia $L/2$ da $\delta$ con $q_{f,a}>L/2$ cerca. Tomamos $t=\min(r,\rho,\delta)/2>0$ y $x=a-t$. Este argumento pertenece al dominio, está a la izquierda y su cociente debería ser no positivo: contradicción. Si $L<0$, tolerancia $|L|/2$ fuerza $q_{f,a}<L/2<0$; el argumento explícito $x=a+t$ contradice el signo de la derecha. Sólo queda $L=0$. Para un máximo se aplica el resultado a $-f$, cuya derivada es $-L$ por C18. Se usaron dos lados y un testigo por caso, sin fabricar una sucesión.

![El cuadrado tiene mínimo interior en cero y derivada cero. La identidad en \[0,1\] tiene mínimo y máximo de frontera con derivadas relativas uno. Fermat necesita interioridad o acumulación por ambos lados además de extremo y derivabilidad; las figuras no sustituyen la prueba por signos.](../../assets/books/anm/C19/C19-F01.svg){#fig-anm-c19-f01 fig-alt="El cuadrado tiene mínimo interior en cero y derivada cero. La identidad en \[0,1\] tiene mínimo y máximo de frontera con derivadas relativas uno. Fermat necesita interioridad o acumulación por ambos lados además de extremo y derivabilidad; las figuras no sustituyen la prueba por signos."}

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-001}

1. ¿Qué es un mínimo local relativo?

[]{#MA-MIC-ANM-01-019-002}

2. ¿Qué aporta interioridad a Fermat?

[]{#MA-MIC-ANM-01-019-003}

3. ¿Qué signo tienen las secantes a la izquierda de un mínimo?

[]{#MA-MIC-ANM-01-019-004}

4. ¿Qué signo tienen las secantes a la derecha de un mínimo?

[]{#MA-MIC-ANM-01-019-005}

5. ¿Por qué una derivada positiva contradice un mínimo interior?

[]{#MA-MIC-ANM-01-019-006}

6. ¿Qué ocurre con la identidad en los bordes de $[0,1]$?

[]{#MA-MIC-ANM-01-019-007}

7. ¿Pendiente cero basta para un extremo?

[]{#MA-MIC-ANM-01-019-008}

8. ¿Se usa valor medio para probar Fermat?

## 19.2. Rolle: volver a la misma altura

[]{#MA-SEC-ANM-01-019-002}

Fermat convierte un extremo interior en una pendiente nula. Todavía falta garantizar un extremo que no esté en la frontera. Aquí entra una herramienta heredada: C16 asegura que una continua en un segmento cerrado no vacío alcanza máximo y mínimo.

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

![Para x(1−x) en \[0,1\], los bordes valen cero y el máximo interior en 1/2 tiene valor 1/4 y derivada cero. Este ejemplo tiene un único punto estacionario por la fórmula 1−2x; Rolle en general sólo garantiza existencia, sin unicidad ni un cero adicional de la función.](../../assets/books/anm/C19/C19-F02.svg){#fig-anm-c19-f02 fig-alt="Para x(1−x) en \[0,1\], los bordes valen cero y el máximo interior en 1/2 tiene valor 1/4 y derivada cero. Este ejemplo tiene un único punto estacionario por la fórmula 1−2x; Rolle en general sólo garantiza existencia, sin unicidad ni un cero adicional de la función."}

**Auditar una hipótesis a la vez.** Sin continuidad de borde, $u(x)=x$ para $0\le x<1$ y $u(1)=0$ tiene valores de borde iguales, pero derivada uno en todo el interior. Sin derivabilidad interior, $v(x)=|x-1/2|$ en $[0,1]$ tiene bordes iguales y es continua, pero ninguna derivada interior existente vale cero. Sin igualdad de borde, la identidad continua y derivable tampoco se detiene. Estos ejemplos prueban que no puede eliminarse cada condición del enunciado universal; no que las condiciones sean necesarias para toda función particular que casualmente tenga una derivada nula.

**Existencia no es selección ni unicidad.** La función constante satisface la conclusión en todos los puntos interiores. Una curva puede tener varios puntos de derivada nula. Rolle entrega al menos uno, sin elegir un punto para todos los intervalos simultáneamente. Si dos ceros de $f$ delimitan un segmento con las hipótesis, existe entre ellos un cero de $f'$; no tiene por qué ser otro cero de $f$.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-009}

1. ¿Dónde se exige continuidad en Rolle?

[]{#MA-MIC-ANM-01-019-010}

2. ¿Dónde se exige derivabilidad en Rolle?

[]{#MA-MIC-ANM-01-019-011}

3. ¿Qué herramienta asegura extremos alcanzados?

[]{#MA-MIC-ANM-01-019-012}

4. ¿Por qué una altura mayor que la de los bordes produce un extremo interior?

[]{#MA-MIC-ANM-01-019-013}

5. ¿Qué punto sirve si la función es constante?

[]{#MA-MIC-ANM-01-019-014}

6. ¿Rolle exige que ambos extremos globales sean interiores?

[]{#MA-MIC-ANM-01-019-015}

7. ¿Un cero de la derivada entre dos ceros es necesariamente otro cero de la función?

[]{#MA-MIC-ANM-01-019-016}

8. ¿La conclusión de Rolle identifica un punto único?

## 19.3. Restar la secante para encontrar una tangente

[]{#MA-SEC-ANM-01-019-003}

Una curva que termina a otra altura no cumple la igualdad de bordes de Rolle. Restar la recta secante transforma el problema en uno que sí vuelve a la misma altura.

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

![En \[1,3\], la secante del cuadrado tiene pendiente cuatro y recta 4x−3. La tangente en dos tiene igual pendiente. Restar la secante da H=(x−1)(x−3), con bordes cero y H′(2)=0. El punto medio funciona aquí por el cuadrado; no es un punto prescrito por el teorema general.](../../assets/books/anm/C19/C19-F03.svg){#fig-anm-c19-f03 fig-alt="En \[1,3\], la secante del cuadrado tiene pendiente cuatro y recta 4x−3. La tangente en dos tiene igual pendiente. Restar la secante da H=(x−1)(x−3), con bordes cero y H′(2)=0. El punto medio funciona aquí por el cuadrado; no es un punto prescrito por el teorema general."}

**Restricciones verificadas.** Para una función original $f:D\to\mathbb R$, sólo se aplica el resultado al par $u<v$ si $[u,v]\subseteq D$, con continuidad en ese segmento y derivabilidad dentro. La restricción a $[u,v]$ conserva continuidad por C14 y derivadas en puntos interiores por C18, porque todos ellos acumulan en el segmento. Así la conclusión usa las derivadas de la función original. Tener sólo los dos extremos en $D$ no basta si falta el segmento entre ellos.

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

Si $a=b$, la expresión secante divide por cero y el interior es vacío: ese caso no se incorpora al enunciado. Las hipótesis son las de Rolle salvo la igualdad de borde; se conservan los contraejemplos de continuidad o derivabilidad omitidas. La igualdad es exacta para algún punto, aunque no conozcamos cuál.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-017}

1. ¿Qué pendiente se resta en la prueba de Lagrange?

[]{#MA-MIC-ANM-01-019-018}

2. ¿Qué función tiene bordes cero?

[]{#MA-MIC-ANM-01-019-019}

3. ¿Cuánto vale $H\prime$ en el interior?

[]{#MA-MIC-ANM-01-019-020}

4. ¿Qué convierte Rolle en la igualdad de valor medio?

[]{#MA-MIC-ANM-01-019-021}

5. ¿Por qué no se admite $a=b$?

[]{#MA-MIC-ANM-01-019-022}

6. ¿Qué debe comprobarse antes de restringir al par $u<v$?

[]{#MA-MIC-ANM-01-019-023}

7. ¿El punto de valor medio del cubo en $[0,1]$ es un medio?

[]{#MA-MIC-ANM-01-019-024}

8. ¿Hace falta continuidad de $f\prime$?

## 19.4. El intervalo convierte signos en orden

[]{#MA-SEC-ANM-01-019-004}

Ahora sí podemos transformar signos en comparaciones entre dos entradas cualesquiera. El segmento que une esas entradas es el lugar donde se transporta la información.

**R4 — Monotonía en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo no degenerado y $f:I\to\mathbb R$ continua en $I$, derivable en $\operatorname{int}(I)$. Si $f'\ge0$ en el interior, $f$ es no decreciente. Si $f'>0$ en el interior, es estrictamente creciente. Las desigualdades opuestas dan los resultados decrecientes.

**Prueba y gasto de la geometría.** Fijados $x<y$ de $I$, su carácter intervalar garantiza $[x,y]\subseteq I$. C18 conserva las derivadas interiores al restringir. R3 entrega algún $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El segundo factor es positivo, así el signo del primero es el de $f'(c)$; si la cota era débil, la comparación es débil. Los puntos $c$ pueden depender del par: no se selecciona una familia de ellos. En intervalos abiertos, la continuidad ya sigue de la diferenciabilidad en cada punto por C18; en extremos incluidos debe conservarse explícitamente.

**Recíproca con alcance.** Si $f$ es no decreciente y tiene derivada en un punto interior $a$, todos sus cocientes centrados allí son no negativos: a la derecha ambos incrementos son no negativos, a la izquierda ambos son no positivos. Un límite negativo sería contradicho por tolerancia $|L|/2$ y un argumento suficientemente cercano. Por tanto $f'(a)\ge0$. La estricta monotonía no fuerza $f'(a)>0$: $x^3$ es estrictamente creciente y $f'(0)=0$. Para justificar su crecimiento directamente, si $x<y$,
$$y^3-x^3=(y-x)(x^2+xy+y^2)>0,$$
pues $x^2+xy+y^2=(x+y/2)^2+3y^2/4$ sólo se anula con $x=y=0$, imposible para ese par.

![En un intervalo, continuidad y derivada interior cero fuerzan constancia por Lagrange. En \[0,1\]∪\[2,3\], la función cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto, incluidos bordes, pero no es constante en todo el dominio. El hueco no se rellena y el valor medio no se aplica a través de él.](../../assets/books/anm/C19/C19-F04.svg){#fig-anm-c19-f04 fig-alt="En un intervalo, continuidad y derivada interior cero fuerzan constancia por Lagrange. En \[0,1\]∪\[2,3\], la función cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto, incluidos bordes, pero no es constante en todo el dominio. El hueco no se rellena y el valor medio no se aplica a través de él."}

**Derivada nula y constantes.** Si $f'=0$ en todo el interior, R3 aplicado a cada par prueba que $f$ es constante en $I$. La recíproca sigue de cocientes cero. Si $f'=g'$ bajo las mismas condiciones, $f-g$ tiene derivada cero y es constante: $f(x)-g(x)$ no depende de $x$. Un valor común en un centro fija esa constante en cero.

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto del dominio, pero no es constante en $D$. No se puede aplicar R3 entre uno y dos porque falta $(1,2)$. Similarmente, derivadas positivas en piezas separadas no ordenan automáticamente salidas a través del hueco. Si se incluye una frontera con salto de valor, derivabilidad en todo el interior tampoco basta para concluir constancia o monotonía en el dominio completo.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-025}

1. ¿Qué propiedad del dominio conecta dos entradas por Lagrange?

[]{#MA-MIC-ANM-01-019-026}

2. ¿Qué conclusión da $f\prime\ge0$ en el interior?

[]{#MA-MIC-ANM-01-019-027}

3. ¿Qué condición suficiente da crecimiento estricto?

[]{#MA-MIC-ANM-01-019-028}

4. ¿Una función estrictamente creciente tiene siempre derivada positiva?

[]{#MA-MIC-ANM-01-019-029}

5. ¿Qué da derivada idénticamente cero en un intervalo?

[]{#MA-MIC-ANM-01-019-030}

6. ¿Qué da igualdad de dos derivadas en el interior?

[]{#MA-MIC-ANM-01-019-031}

7. ¿Qué falla para constantes diferentes en dos piezas separadas?

[]{#MA-MIC-ANM-01-019-032}

8. ¿Se selecciona un punto $c$ para todos los pares a la vez?

## 19.5. De cotas de derivadas a cotas de incrementos

[]{#MA-SEC-ANM-01-019-005}

Aunque el punto de valor medio sea desconocido, una cota válida para todas las derivadas pertinentes también vale para la derivada de ese punto. Esto convierte existencia en un certificado cuantitativo.

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

![Para el cubo en \[1,2\], 3≤f′≤12 en el interior. R5 da 3(y−x)≤f(y)−f(x)≤12(y−x) para cualquier par ordenado. El panel derecho representa el caso de centro uno, con bandas 1+3(x−1) y 1+12(x−1). Las fórmulas prueban las cotas universales; un muestreo de la derivada no bastaría.](../../assets/books/anm/C19/C19-F05.svg){#fig-anm-c19-f05 fig-alt="Para el cubo en \[1,2\], 3≤f′≤12 en el interior. R5 da 3(y−x)≤f(y)−f(x)≤12(y−x) para cualquier par ordenado. El panel derecho representa el caso de centro uno, con bandas 1+3(x−1) y 1+12(x−1). Las fórmulas prueban las cotas universales; un muestreo de la derivada no bastaría."}

**Primera reutilización.** Para el cubo en $[-A,A]$, $A>0$, su derivada $3t^2$ está entre cero y $3A^2$: cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Para la raíz en $[\alpha,\beta]$, $0<\alpha<\beta$, la derivada es $1/(2\sqrt t)$ y no supera $1/(2\sqrt\alpha)$. En $[0,1]$ no hay una constante Lipschitz finita para la raíz, como muestra el cociente $1/\sqrt y$ centrado en cero. Su continuidad uniforme de C17 permanece válida: la cota lineal es suficiente, sin ser necesaria.

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

**Lo inverso.** Si $f$ satisface una cota Lipschitz $L$ y existe $f'(a)$ en un centro acumulante, cada cociente perforado tiene magnitud a lo sumo $L$. C13 conserva la cota en el límite, así $|f'(a)|\le L$. La existencia no se deduce: el valor absoluto es Lipschitz y falla derivabilidad en cero. Unas pocas pendientes muestreadas tampoco demuestran una cota que deba valer en todos los centros.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-033}

1. ¿Qué desigualdad producen $m\le f\prime\le M$?

[]{#MA-MIC-ANM-01-019-034}

2. ¿Por qué no se invierte el orden al multiplicar?

[]{#MA-MIC-ANM-01-019-035}

3. ¿Qué controla una cota $|f\prime|\le L$?

[]{#MA-MIC-ANM-01-019-036}

4. ¿Cómo se trata $L=0$?

[]{#MA-MIC-ANM-01-019-037}

5. ¿Qué radio uniforme da $L>0$?

[]{#MA-MIC-ANM-01-019-038}

6. ¿Qué cota funciona para el cubo en $[-A,A]$?

[]{#MA-MIC-ANM-01-019-039}

7. ¿Lipschitz implica existencia de derivada en cada punto?

[]{#MA-MIC-ANM-01-019-040}

8. ¿Basta la derivada en un centro para acotar las derivadas vecinas?

## 19.6. Comparar dos variaciones en el mismo punto

[]{#MA-SEC-ANM-01-019-006}

Aplicar Lagrange por separado a dos funciones puede producir dos puntos diferentes. Para comparar sus variaciones en un mismo punto debemos construir una sola función auxiliar.

**R6 — Valor medio de Cauchy, sin divisiones.** Sean $f,g:[a,b]\to\mathbb R$, $a<b$, continuas en el segmento y derivables en su interior. Existe $c\in(a,b)$ con
$$[f(b)-f(a)]g'(c)=[g(b)-g(a)]f'(c).$$
Escribamos los incrementos determinados por los bordes como $\Delta f,\Delta g$. Definimos
$$H(x)=\Delta g\,[f(x)-f(a)]-\Delta f\,[g(x)-g(a)].$$
Entonces $H(a)=H(b)=0$, es continua en todo el segmento y derivable dentro, con $H'(x)=\Delta g f'(x)-\Delta f g'(x)$ por C18. Los coeficientes son constantes, no funciones del argumento. Rolle aplicado a $H$ produce la igualdad. La construcción no divide por ningún incremento o derivada y admite los casos nulos.

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

![Para f=x² y g=x³ en \[0,1\], ambos incrementos valen uno y Cauchy se satisface en c=2/3. El par (g(c),f(c))=(8/27,4/9) tiene tangente de pendiente f′/g′=1, paralela a la secante de bordes. El gráfico representa el par por su argumento x, sin introducir una regla nueva para curvas. Los puntos de Lagrange separados son 1/2 y 1/√3.](../../assets/books/anm/C19/C19-F06.svg){#fig-anm-c19-f06 fig-alt="Para f=x² y g=x³ en \[0,1\], ambos incrementos valen uno y Cauchy se satisface en c=2/3. El par (g(c),f(c))=(8/27,4/9) tiene tangente de pendiente f′/g′=1, paralela a la secante de bordes. El gráfico representa el par por su argumento x, sin introducir una regla nueva para curvas. Los puntos de Lagrange separados son 1/2 y 1/√3."}

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

Si $\Delta g\ne0$ pero la derivada de $g$ se anula en algunos centros, no se puede dividir en un testigo arbitrario sin verificarlo. Con $f=g=x^3$ en $[-1,1]$, el producto cruzado vale en todos los puntos, incluido cero donde ambas derivadas son cero. Lagrange se recupera tomando $g(x)=x$, cuyo incremento $b-a$ y derivada uno son no nulos.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-041}

1. ¿Qué forma de Cauchy permite incrementos nulos?

[]{#MA-MIC-ANM-01-019-042}

2. ¿Qué coeficientes tiene la función auxiliar?

[]{#MA-MIC-ANM-01-019-043}

3. ¿Por qué sus bordes coinciden?

[]{#MA-MIC-ANM-01-019-044}

4. ¿Qué condición evita todos los denominadores nulos en la forma de cocientes?

[]{#MA-MIC-ANM-01-019-045}

5. ¿Por qué dos aplicaciones separadas de Lagrange no bastan?

[]{#MA-MIC-ANM-01-019-046}

6. ¿Qué punto sirve para $f=x^2$, $g=x^3$ en $[0,1]$?

[]{#MA-MIC-ANM-01-019-047}

7. ¿Qué ocurre si $g$ es constante?

[]{#MA-MIC-ANM-01-019-048}

8. ¿Cómo se recupera Lagrange?

## 19.7. Darboux: discontinuidad sin saltar valores

[]{#MA-SEC-ANM-01-019-007}

C18 mostró una función derivable cuya derivada no es continua. Sin embargo, una derivada en un intervalo no puede omitir un valor situado entre dos de sus valores. No lo demostraremos suponiendo continuidad de $f'$.

**R7 — Darboux.** Sea $f:I\to\mathbb R$ derivable en todos los puntos de un intervalo abierto $I$. Para $u<v$ en $I$ y un real $\lambda$ estrictamente entre $f'(u)$ y $f'(v)$, existe $c\in(u,v)$ con $f'(c)=\lambda$.

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

C18 da continuidad de $H$ en cada punto del segmento; su restricción es continua allí. C16 entrega un mínimo alcanzado, que las dos comparaciones sitúan en algún $c\in(u,v)$. Ese mínimo es local para la función original: una bola suficientemente pequeña de $c$ queda en $(u,v)$. Fermat da $H'(c)=0$, luego $f'(c)=\lambda$. Si $f'(u)>\lambda>f'(v)$, se aplica el caso anterior a $-f$ y $-\lambda$, o se usa un máximo para la misma función auxiliar. No se elige una familia de minimizadores.

![En un bulto de C18, F′=−4u(1−u²) y entre u=0 y u=1/2 aparecen todos los valores entre cero y −3/2. La familia completa tiene F′(0)=0 y F′(x_n)=−3/2 con x_n→0, así no es continua en cero. Se representan cinco términos; R7 garantiza todos los valores intermedios entre los centros por una prueba de extremos, sin suponer continuidad de F′.](../../assets/books/anm/C19/C19-F07.svg){#fig-anm-c19-f07 fig-alt="En un bulto de C18, F′=−4u(1−u²) y entre u=0 y u=1/2 aparecen todos los valores entre cero y −3/2. La familia completa tiene F′(0)=0 y F′(x_n)=−3/2 con x_n→0, así no es continua en cero. Se representan cinco términos; R7 garantiza todos los valores intermedios entre los centros por una prueba de extremos, sin suponer continuidad de F′."}

**Consecuencia de signo.** Si $f'$ no se anula en $I$, no puede tener un valor positivo y otro negativo: Darboux con $\lambda=0$ daría una anulación entre ellos. Su signo es constante; si el intervalo es no vacío, fijar un punto y su signo determina cuál. R4 convierte ese signo en monotonía estricta. La premisa $f'\ne0$ no significa una cota positiva uniforme de $|f'|$.

**Discontinuidad y valores intermedios son compatibles.** La familia de bultos de C18 es derivable en toda la recta, tiene $F'(0)=0$ y puntos $x_n\to0$ con $F'(x_n)=-3/2$. R7 obliga a alcanzar cada valor de $(-3/2,0)$ entre cero y cada $x_n$, aunque las derivadas no converjan al valor central. En el perfil de cada bulto, la fórmula $-4u(1-u^2)$ también muestra variación continua dentro de esa pieza. Representar sólo una pieza no prueba toda la propiedad; ésta sigue de R7 aplicado a la función completa. Una función escalón que pase directamente de $-1$ a $1$ y omita cero no puede ser la derivada de una función derivable en un intervalo que contenga ambos lados.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-049}

1. ¿Darboux presupone continuidad de la derivada?

[]{#MA-MIC-ANM-01-019-050}

2. ¿Qué resta se usa para buscar $f\prime(c)=\lambda$?

[]{#MA-MIC-ANM-01-019-051}

3. ¿Por qué $H\prime(u)<0$ impide mínimo en el borde izquierdo?

[]{#MA-MIC-ANM-01-019-052}

4. ¿Por qué $H\prime(v)>0$ impide mínimo en el borde derecho?

[]{#MA-MIC-ANM-01-019-053}

5. ¿Qué ocurre si se invierte el orden de los dos valores de derivada?

[]{#MA-MIC-ANM-01-019-054}

6. ¿Qué garantiza una derivada que nunca se anula en un intervalo abierto?

[]{#MA-MIC-ANM-01-019-055}

7. ¿Valores intermedios implican continuidad?

[]{#MA-MIC-ANM-01-019-056}

8. ¿Puede una derivada saltar directamente de menos uno a uno omitiendo cero?

## 19.8. Certificar ceros y soluciones únicas

[]{#MA-SEC-ANM-01-019-008}

Rolle y las cotas de incrementos producen certificados de número de soluciones y de error. Es necesario distinguir la existencia de una raíz, su unicidad y la precisión de un aproximante.

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

**Existencia por una herramienta diferente.** Para $p(x)=x^3+x-1$ en $[0,1]$, $p(0)=-1$ y $p(1)=1$. La continuidad y el valor intermedio de C15 dan un cero $r\in(0,1)$. Su derivada $3x^2+1\ge1$ hace imposible otro cero por R8, y también prueba crecimiento estricto por R4. El valor medio no creó la raíz: asegura su unicidad y cuantifica cambios una vez que C15 la garantiza.

**Certificado de posición y error.** Los valores $p(1/2)=-3/8$ y $p(3/4)=11/64$ encierran la única raíz en $(1/2,3/4)$. En $x=2/3$, $p(x)=-1/27$, así el crecimiento la sitúa a la derecha. Dentro de $[1/2,3/4]$,
$$\frac74\le p'(t)\le\frac{43}{16}.$$
Aplicar R5 al par $x,r$ da
$$\frac74(r-x)\le p(r)-p(x)=\frac1{27}\le\frac{43}{16}(r-x),$$
por lo que
$$\frac{16}{1161}\le r-\frac23\le\frac4{189}.$$
Estas son cotas racionales demostradas, no cifras leídas de un gráfico. En general, una cota $f'\ge m>0$ sobre el segmento entre un aproximante $x$ y un cero $r$ da $|x-r|\le|f(x)|/m$, siempre que el cero y el segmento satisfagan las hipótesis.

![C15 garantiza la raíz r y Rolle su unicidad. Los signos exactos en 1/2 y 3/4 la encierran; p(2/3)=−1/27 la sitúa a la derecha del aproximante. Las cotas 7/4≤p′≤43/16 en ese segmento dan 16/1161≤r−2/3≤4/189. Los extremos de la banda son cotas cerradas, sin atribuir a r una coordenada numérica extraída del dibujo.](../../assets/books/anm/C19/C19-F08.svg){#fig-anm-c19-f08 fig-alt="C15 garantiza la raíz r y Rolle su unicidad. Los signos exactos en 1/2 y 3/4 la encierran; p(2/3)=−1/27 la sitúa a la derecha del aproximante. Las cotas 7/4≤p′≤43/16 en ese segmento dan 16/1161≤r−2/3≤4/189. Los extremos de la banda son cotas cerradas, sin atribuir a r una coordenada numérica extraída del dibujo."}

**Un número máximo puede alcanzarse.** Para $q(x)=x^3-3x$ sobre la recta, $q'(x)=3x^2-3$ tiene exactamente dos ceros, $-1,1$. R8 permite a lo sumo tres ceros de $q$. La factorización $q(x)=x(x^2-3)$ y las raíces de C10 muestran tres: $-\sqrt3,0,\sqrt3$. El conteo es finito y no usa un teorema sobre derivadas de orden superior.

**Lo que debe quedar certificado.** Una cota de derivada tiene que valer en todos los puntos interiores pertinentes, no sólo en una tabla de pendientes. Un par de valores iguales no autoriza Rolle sobre un dominio con huecos, ni una raíz garantiza otras entre cada par de puntos estacionarios. Disponemos ya de los puentes entre pendientes locales y orden, incrementos, valores intermedios de la derivada y soluciones sobre intervalos. Convexidad y modelos de orden superior tendrán sus propias hipótesis en los capítulos siguientes.

**Microcontroles.**

[]{#MA-MIC-ANM-01-019-057}

1. ¿Qué da Rolle si dos entradas tienen el mismo valor?

[]{#MA-MIC-ANM-01-019-058}

2. ¿Qué cota de ceros de $f$ da a lo sumo $k$ ceros de $f\prime$?

[]{#MA-MIC-ANM-01-019-059}

3. ¿Por qué los ceros de derivada de los segmentos vecinos son distintos?

[]{#MA-MIC-ANM-01-019-060}

4. ¿Qué herramienta garantiza existencia del cero de $x^3+x-1$?

[]{#MA-MIC-ANM-01-019-061}

5. ¿Qué cota inferior de derivada vale en $[0,1]$ para ese polinomio?

[]{#MA-MIC-ANM-01-019-062}

6. ¿Qué residuo tiene el aproximante $2/3$?

[]{#MA-MIC-ANM-01-019-063}

7. ¿Qué error da una cota $f\prime\ge m>0$ entre $x$ y un cero $r$?

[]{#MA-MIC-ANM-01-019-064}

8. ¿Qué falta cuando sólo se han muestreado unas pocas derivadas?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html)

[← Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Capítulo 20 →](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html)
