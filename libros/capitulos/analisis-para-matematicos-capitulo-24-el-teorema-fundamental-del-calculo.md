---
content-id: MA-BCH-0298
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-024
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
title: Capítulo 24 — El teorema fundamental del cálculo
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C24.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)

La tasa local de C18 y la acumulación global de C23 fueron construidas por separado. Ahora demostraremos qué hipótesis las conectan. La primera dirección recupera una tasa continua en un punto; la segunda evalúa una integral mediante una primitiva cuya continuidad en el cerrado debe conservarse.

C18 aporta derivadas relativas y reglas; C19, Lagrange y constancia; C23, integrabilidad, cotas, álgebra, aditividad y orientación. C14 es interfaz de continuidad. C15/C16 se declaran sólo para el promedio integral alcanzado opcional, después de las dos pruebas centrales. No se supone integrabilidad de toda derivada.

## 24.1. Construir una función de acumulación

[]{#MA-SEC-ANM-01-024-001}

Fijemos $a<b$ y una función integrable $f:[a,b]\to\mathbb R$. C23 ya garantiza acotación, una integral única, restricción a subintervalos y aditividad. El extremo superior puede variar sólo después de que esas garantías estén disponibles.

**R1 — Acumulación con origen fijo.** Para $x\in[a,b]$ definimos
$$A_f(x)=\int_a^x f(t)\,dt.$$
La notación abrevia la integral de la restricción $f|_{[a,x]}$. Si $x>a$, existe por restricción de C23. Si $x=a$, usamos exclusivamente la convención de integral degenerada, de valor cero; no hay partición estricta de un singleton. La unicidad del valor integral hace única la salida para cada entrada.

Podemos construir el grafo como el subconjunto de $[a,b]\times\mathbb R$ formado por los pares $(x,z)$ que cumplen esa igualdad, con el caso degenerado separado. Existencia y unicidad muestran que es una función de dominio exacto $[a,b]$ y codominio real. No se elige una familia de testigos para construirla: cada salida está determinada por la relación funcional. En particular,
$$A_f(a)=0,\qquad A_f(b)=\int_a^b f.$$

**Primera identidad reutilizable.** Para $a\le x\le y\le b$, las restricciones sucesivas de $f$ conservan dominio, codominio y valores; por aditividad finita,
$$A_f(y)-A_f(x)=\int_x^y f.$$
Si $x=y$, ambos miembros son cero. Para $y<x$, la convención de orientación de C23 da la misma fórmula: invertir los límites cambia el signo. Así el incremento depende sólo del tramo entre las entradas, aunque cada valor de $A_f$ recuerde el origen $a$.

Si elegimos otro origen $c\in[a,b]$, la función $A_{f,c}(x)=\int_c^x f$ también existe para todas las entradas, incluidas las anteriores a $c$, y aditividad orientada prueba
$$A_{f,c}(x)=A_f(x)-A_f(c).$$
Cambiar el origen traslada toda la acumulación por una constante; no altera ninguno de sus incrementos. Esto se prueba antes de derivar y no presupone primitivas.

Para $f(t)=2t-1$ en $[0,1]$, C22 evaluó integrales afines por sumas finitas. Aplicando esa fórmula en cada $[0,x]$ resulta $A_f(x)=x^2-x$. Es negativa dentro y vuelve a cero en $1$. La integral es firmada: el nombre acumulación no obliga a crecer ni a ser no negativa.

![En \[0,1\], f(t)=2t−1 y A(x)=x²−x. La acumulada tiene origen0, valor−1/4 en1/2 y valor0 en1; contribuciones firmadas de mitades opuestas.](../../assets/books/anm/C24/C24-F01.svg){#fig-anm-c24-f01 fig-alt="En \[0,1\], f(t)=2t−1 y A(x)=x²−x. La acumulada tiene origen0, valor−1/4 en1/2 y valor0 en1; contribuciones firmadas de mitades opuestas."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-001}

1. ¿Qué debe existir antes de definir $A_f(x)$?

[]{#MA-MIC-ANM-01-024-002}

2. ¿Cuánto vale $A_f(a)$?

[]{#MA-MIC-ANM-01-024-003}

3. ¿Por qué la fórmula determina una función?

[]{#MA-MIC-ANM-01-024-004}

4. ¿Qué expresa $A_f(y)-A_f(x)$?

[]{#MA-MIC-ANM-01-024-005}

5. ¿Qué ocurre si $x=y$?

[]{#MA-MIC-ANM-01-024-006}

6. ¿Qué cambia al mover el origen a $c$?

[]{#MA-MIC-ANM-01-024-007}

7. ¿Debe ser no negativa la acumulación?

[]{#MA-MIC-ANM-01-024-008}

8. ¿Se ha usado una primitiva en R1?

## 24.2. Incrementos, cotas y continuidad

[]{#MA-SEC-ANM-01-024-002}

La identidad exacta del incremento permite transportar cotas universales de la integranda a la acumulación. No se necesita una derivada ni un punto de valor medio integral.

**R2 — Encierro y regularidad automática.** Si $x<y$ y $m\le f(t)\le M$ para todo $t\in[x,y]$, el orden de la integral de C23 y la integral de una constante dan
$$m(y-x)\le A_f(y)-A_f(x)\le M(y-x).$$
Dividir por $y-x>0$ conserva el orden. Podemos tomar $m=\inf f([x,y])$, $M=\sup f([x,y])$, porque la imagen es no vacía y acotada; no tienen por qué alcanzarse. El cociente queda encerrado entre cotas de toda la pieza, no entre dos muestras.

La integrabilidad asegura una cota global $|f(t)|\le B$ con $B\ge0$. Para $x<y$, aplicar el encierro con $-B,B$ da $|A_f(y)-A_f(x)|\le B(y-x)$. Para $y<x$, intercambiar las entradas y usar simetría del absoluto; para igualdad, ambos lados son cero. Por tanto,
$$|A_f(y)-A_f(x)|\le B|y-x|\qquad(x,y\in[a,b]).$$
La acumulada es Lipschitz. Para cada $\varepsilon>0$, el radio $\delta=\varepsilon/(B+1)>0$ funciona para todos los pares: si $B>0$, la diferencia es menor que $B\delta<\varepsilon$; si $B=0$, es cero. Queda probada continuidad uniforme, incluso en los bordes relativos del dominio. También $|A_f(x)|\le B(b-a)$ por comparar con $a$.

**El signo gobierna incrementos.** Si $f\ge0$ en todo el intervalo, cada integral sobre $[x,y]$ es no negativa y $A_f$ es no decreciente. Si $f\le0$, es no creciente. Si existe $m>0$ con $f\ge m$, entonces $A_f(y)-A_f(x)\ge m(y-x)>0$ para todo $x<y$. Un valor positivo en un punto aislado no basta para crecimiento estricto; C23 mostró que un pico aislado tiene integral cero. Para una continua estrictamente positiva, cada subintervalo contiene un pequeño segmento donde $f$ conserva una cota positiva por continuidad; orden, aditividad y no negatividad en el resto prueban incremento positivo. Aquí se declara continuidad donde se gasta.

Para el escalón $s(t)=0$ si $t<1/2$ y $s(t)=1$ si $t\ge1/2$ en $[0,1]$, la acumulada es $0$ hasta $1/2$ y $x-1/2$ después. El valor nodal no aporta anchura, por cambios finitos de C23. Es continua y Lipschitz de constante $1$ aunque la integranda tenga un salto.

![El escalón vale0 antes de1/2 y1 desde el corte. Su acumulada vale0 hasta1/2 y x−1/2 después: continua y Lipschitz1, aunque haya salto.](../../assets/books/anm/C24/C24-F02.svg){#fig-anm-c24-f02 fig-alt="El escalón vale0 antes de1/2 y1 desde el corte. Su acumulada vale0 hasta1/2 y x−1/2 después: continua y Lipschitz1, aunque haya salto."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-009}

1. ¿Qué encierra el cociente medio?

[]{#MA-MIC-ANM-01-024-010}

2. ¿Deben alcanzarse las cotas extremas locales?

[]{#MA-MIC-ANM-01-024-011}

3. ¿Qué da una cota $|f|\le B$?

[]{#MA-MIC-ANM-01-024-012}

4. ¿Qué radio evita dividir por $B=0$?

[]{#MA-MIC-ANM-01-024-013}

5. ¿Se necesita continuidad de $f$ para continuidad de $A_f$?

[]{#MA-MIC-ANM-01-024-014}

6. ¿Qué signo garantiza acumulación no decreciente?

[]{#MA-MIC-ANM-01-024-015}

7. ¿Un pico positivo garantiza crecimiento estricto?

[]{#MA-MIC-ANM-01-024-016}

8. ¿Cuál es la acumulada del escalón con corte $1/2$?

## 24.3. La tasa reaparece en un punto

[]{#MA-SEC-ANM-01-024-003}

La continuidad de la acumulada ya está probada para toda integranda integrable. Recuperar la tasa exige ahora una hipótesis en el centro donde vamos a derivar.

**Lema del promedio local.** Sean $x\ne y$ en $[a,b]$ y $\eta\ge0$. Si $|f(t)-f(x)|\le\eta$ para toda entrada del segmento que une $x$ con $y$, entonces
$$\left|\frac{A_f(y)-A_f(x)}{y-x}-f(x)\right|\le\eta.$$
Para $y>x$, integrar las cotas $f(x)-\eta\le f(t)\le f(x)+\eta$ y dividir por anchura positiva prueba la afirmación. Para $y<x$, aplicar el mismo argumento a $[y,x]$ produce el cociente $[A_f(x)-A_f(y)]/(x-y)$; cambiar los signos de numerador y denominador lo identifica con el cociente requerido. No se divide una desigualdad por un negativo conservando su orden.

**R3 — Primera parte, continuidad puntual.** Si $f$ es continua en un punto $x\in(a,b)$, entonces $A_f$ es derivable allí y $A_f'(x)=f(x)$.

Fijemos $\varepsilon>0$. Continuidad relativa de $f$ en $x$ da $\rho>0$ tal que $|t-x|<\rho$ y $t\in[a,b]$ implican $|f(t)-f(x)|<\varepsilon/2$. Elegimos
$$\delta=\min\{\rho,(x-a)/2,(b-x)/2\}>0.$$
Para cualquier $y$ admisible con $0<|y-x|<\delta$, cada punto $t$ del segmento entre ellos satisface $|t-x|\le|y-x|<\rho$. El lema con $\eta=\varepsilon/2$ da error del cociente a lo sumo $\varepsilon/2<\varepsilon$. Ese mismo radio controla todas las entradas a ambos lados; es exactamente la definición de C18. El centro acumula por ambos lados: para cualquier radio $r>0$, $x\pm\frac12\min\{r,x-a,b-x\}$ son entradas distintas suficientemente cercanas. Unicidad legitima la notación de derivada.

La continuidad utilizada es sólo en $x$. La existencia de $A_f$ sí usa integrabilidad en todo el intervalo. No hemos aplicado valor medio integral ni escogido un punto que dependa de cada incremento. Todo el segmento corto queda controlado simultáneamente.

**Certificado adicional cuando hay Lipschitz.** Si $|f(t)-f(x)|\le L|t-x|$, el lema da error del cociente a lo sumo $L|y-x|$. Hay una cota más fina: por álgebra y orden de integrales,
$$|A_f(y)-A_f(x)-f(x)(y-x)|\le \frac L2|y-x|^2.$$
Para $y>x$, integrar $|f(t)-f(x)|\le L(t-x)$ y usar la integral afín heredada da $L(y-x)^2/2$. Para $y<x$, invertir orientación y usar $L(x-t)$ sobre $[y,x]$ da el mismo resultado. No se usó Taylor. Si $L=0$, el residuo es exactamente cero.

Con $f(t)=t^2$ y $x=1/2$ en $[0,1]$, la acumulada ya calculada por sumas es $x^3/3$. Para incrementos admisibles $h\ne0$, el cociente es $1/4+h/2+h^2/3$, que converge a $f(1/2)=1/4$. El término adicional tiene signo y tamaño explícitos, sin depender de una lista de muestras.

![Para f(t)=t², A(x)=x³/3 y centro1/2, el cociente con incremento h es1/4+h/2+h²/3. Desde ambos signos converge a1/4; la curva exacta, no las muestras, prueba el límite.](../../assets/books/anm/C24/C24-F03.svg){#fig-anm-c24-f03 fig-alt="Para f(t)=t², A(x)=x³/3 y centro1/2, el cociente con incremento h es1/4+h/2+h²/3. Desde ambos signos converge a1/4; la curva exacta, no las muestras, prueba el límite."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-017}

1. ¿Qué controla el lema del promedio local?

[]{#MA-MIC-ANM-01-024-018}

2. ¿Cómo se trata un incremento negativo?

[]{#MA-MIC-ANM-01-024-019}

3. ¿Qué continuidad usa R3?

[]{#MA-MIC-ANM-01-024-020}

4. ¿Por qué aplicar continuidad a $\varepsilon/2$?

[]{#MA-MIC-ANM-01-024-021}

5. ¿Quién precede a toda entrada cercana?

[]{#MA-MIC-ANM-01-024-022}

6. ¿Se escoge un punto de valor medio integral?

[]{#MA-MIC-ANM-01-024-023}

7. ¿Qué cota fina da Lipschitz $L$ para el residuo?

[]{#MA-MIC-ANM-01-024-024}

8. ¿Cuál es la derivada de la acumulada de $t^2$ en $1/2$?

## 24.4. Bordes, saltos y valores aislados

[]{#MA-SEC-ANM-01-024-004}

Los bordes del segmento no tienen dos lados dentro del dominio. C18 permite derivadas relativas; ahora debemos decir cuál es su alcance.

**R4 — Bordes y límites de la recuperación.** Si $f$ es continua relativamente a $[a,b]$ en $a$, el mismo lema local prueba
$$\lim_{y\downarrow a}\frac{A_f(y)-A_f(a)}{y-a}=f(a).$$
Basta tomar el radio de continuidad para $\varepsilon/2$, reducirlo si hace falta a $(b-a)/2$, y controlar $t\in[a,y]$. En $b$, usar $[y,b]$ y cambiar ambos signos prueba el límite desde la izquierda, de valor $f(b)$. Ambos extremos acumulan unilateralmente. No se afirma una derivada bilateral de una prolongación desconocida.

Si $f$ es continua en todo $[a,b]$, C23 garantiza integrabilidad. R2 asegura continuidad de $A_f$, R3 da derivada en cada punto interior y este argumento da las derivadas relativas de borde. Así existe una primitiva concreta; el término se precisará en la siguiente sección.

**Un salto impide la derivada de la acumulada.** Para el escalón de R2, en $c=1/2$ los cocientes de la acumulada son $0$ desde la izquierda y $1$ desde la derecha. Si existiera una derivada $D$, la tolerancia $1/3$ y un radio común permitirían tomar $c-r,c+r$ dentro del dominio, con $r$ positivo menor que ese radio. Resultarían $|D|<1/3$ y $|1-D|<1/3$, contradiciendo $1\le|D|+|1-D|<2/3$. Continuidad de la acumulada no implica derivabilidad.

**Un valor aislado muestra otra falla.** Sea $p(c)=1$ y $p(t)=0$ para $t\ne c$, con $c=1/2$. Cambios finitos de C23 dan integral cero en cualquier restricción, luego $A_p\equiv0$. Su derivada existe también en $c$ y vale cero, distinta de $p(c)=1$. Sin continuidad local puede existir la derivada y fallar la igualdad. Continuidad es una condición suficiente de recuperación, no se ha probado que sea necesaria para que exista una derivada.

Modificar un valor de borde también deja todas las integrales intactas. La función que vale cero salvo $f(a)=1$ tiene acumulada cero y derivada derecha cero, distinta de ese valor de borde. Precisamente falla la continuidad relativa en $a$. El teorema no puede recuperar información que los cambios finitos borran de la integral.

![En el salto, los cocientes de la acumulada en el corte son0 y1 desde lados distintos. El pico aislado tiene acumulada cero y derivada cero, diferente del valor1 en el pico.](../../assets/books/anm/C24/C24-F04.svg){#fig-anm-c24-f04 fig-alt="En el salto, los cocientes de la acumulada en el corte son0 y1 desde lados distintos. El pico aislado tiene acumulada cero y derivada cero, diferente del valor1 en el pico."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-025}

1. ¿Qué derivada se afirma en $a$?

[]{#MA-MIC-ANM-01-024-026}

2. ¿Y en $b$?

[]{#MA-MIC-ANM-01-024-027}

3. ¿Se afirma una derivada bilateral de una prolongación?

[]{#MA-MIC-ANM-01-024-028}

4. ¿Qué ocurre con la acumulada de un salto?

[]{#MA-MIC-ANM-01-024-029}

5. ¿Qué cocientes tiene el escalón en su corte?

[]{#MA-MIC-ANM-01-024-030}

6. ¿Qué acumulada tiene el pico aislado?

[]{#MA-MIC-ANM-01-024-031}

7. ¿En el pico existe la derivada de la acumulada?

[]{#MA-MIC-ANM-01-024-032}

8. ¿Continuidad local se probó necesaria para que exista la derivada?

## 24.5. De una primitiva a la integral

[]{#MA-SEC-ANM-01-024-005}

Derivar una acumulación y evaluar una integral mediante una primitiva son resultados relacionados, pero sus hipótesis no coinciden.

**Primitiva en un cerrado.** Para $f:[a,b]\to\mathbb R$, llamaremos primitiva a una función $H:[a,b]\to\mathbb R$ continua en todo el cerrado, derivable en $(a,b)$ y con $H'(t)=f(t)$ allí. No pedimos derivadas bilaterales en los extremos ni incorporamos integrabilidad de $f$ a la definición. La continuidad de $H$ en los bordes será necesaria al usar C19.

**Encierro antes de integrar.** Si $f$ es acotada y $H$ es primitiva, para toda partición $P=(x_0,\ldots,x_n)$,
$$L(f,P)\le H(b)-H(a)\le U(f,P).$$
Fijado un índice $i$, la restricción de $H$ es continua en $[x_{i-1},x_i]$ y derivable dentro, por C14/C18. C19, valor medio de Lagrange, entrega $c$ interior con $H(x_i)-H(x_{i-1})=H'(c)\Delta_i=f(c)\Delta_i$. Cotas locales y $\Delta_i>0$ dan
$$m_i\Delta_i\le H(x_i)-H(x_{i-1})\le M_i\Delta_i.$$
El testigo ya no aparece en esta desigualdad. Por tanto podemos sumar la afirmación universal para todos los índices finitos sin construir una familia de puntos seleccionados. La suma central telescopa por cancelación finita y da el incremento total. La cota no ha supuesto integrabilidad.

**R5 — Newton–Leibniz.** Si además $f$ es integrable, entonces
$$\int_a^b f(t)\,dt=H(b)-H(a).$$
La integral $I$ y el incremento $D=H(b)-H(a)$ están ambos en $[L(f,P),U(f,P)]$ para cualquier $P$. Dada $\varepsilon>0$, el criterio de Darboux da una partición con brecha menor que $\varepsilon$, luego $|I-D|<\varepsilon$. Si esa distancia fuera positiva $d$, elegir $\varepsilon=d/2$ contradice el encierro; así $I=D$. Esta prueba no usa R3 ni continuidad de $f$. La primitiva es una hipótesis, su existencia no se deduce aquí de mera integrabilidad.

La restricción a cualquier $[u,v]\subseteq[a,b]$, con $u<v$, conserva todas las hipótesis y da $\int_u^v f=H(v)-H(u)$. Para igualdad, ambos lados cero; para límites invertidos, orientación de C23 cambia ambos signos. Así también $A_f(x)=H(x)-H(a)$ si existe esta primitiva, aun cuando $f$ no sea continua.

**Por qué conservar los bordes.** En $[0,1]$, tome $f\equiv0$, $H(0)=1$ y $H(x)=0$ para $x>0$. La igualdad $H'=f$ vale en el interior, pero la integral es cero y $H(1)-H(0)=-1$. Falta continuidad de la primitiva en el borde; Lagrange no se aplica al primer segmento. La fórmula de evaluación no es una nueva definición de integral.

![Para H(x)=x³/3, los incrementos sobre nodos0,1/4,1/2,3/4,1 suman1/3. Cada incremento se encierra por Darboux; la suma cancela nodos interiores.](../../assets/books/anm/C24/C24-F05.svg){#fig-anm-c24-f05 fig-alt="Para H(x)=x³/3, los incrementos sobre nodos0,1/4,1/2,3/4,1 suman1/3. Cada incremento se encierra por Darboux; la suma cancela nodos interiores."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-033}

1. ¿Qué exige una primitiva sobre el cerrado?

[]{#MA-MIC-ANM-01-024-034}

2. ¿La definición de primitiva incluye integrabilidad de $f$?

[]{#MA-MIC-ANM-01-024-035}

3. ¿Qué herramienta controla el incremento en cada pieza?

[]{#MA-MIC-ANM-01-024-036}

4. ¿Qué se suma tras eliminar el testigo de Lagrange?

[]{#MA-MIC-ANM-01-024-037}

5. ¿Por qué telescopa la suma central?

[]{#MA-MIC-ANM-01-024-038}

6. ¿Qué convierte el encierro en igualdad con la integral?

[]{#MA-MIC-ANM-01-024-039}

7. ¿Se usa continuidad de $f$ en la segunda parte?

[]{#MA-MIC-ANM-01-024-040}

8. ¿Por qué conservar continuidad de $H$ en los bordes?

## 24.6. Normalización, cálculo y signo

[]{#MA-SEC-ANM-01-024-006}

Podemos ahora normalizar una primitiva y calcular integrales sin reconstruir cada suma de Darboux. Las fórmulas de derivación deben estar disponibles antes de reutilizarlas.

**R6 — Unicidad salvo constante.** Si $H,K$ son primitivas de la misma $f$ en $[a,b]$, su diferencia es continua en el cerrado y derivable dentro, con $(H-K)'=0$ por C18. C19 aplicado a cualquier par de entradas prueba constancia: $H(x)-K(x)=C$, donde $C=H(a)-K(a)$ es único al evaluar en $a$. Recíprocamente, sumar cualquier constante a una primitiva conserva ambas condiciones. El intervalo completo importa: dos componentes separadas podrían llevar constantes distintas.

Si $f$ es continua, R4 construye la primitiva $A_f$, con $A_f(a)=0$. Toda otra primitiva es $A_f+C$; por ello $A_f$ es la única que se anula en $a$. Más generalmente, para un dato $H(a)=c_0$, la solución única de $H'=f$ entre las funciones continuas en el cerrado y derivables dentro es $H(x)=c_0+A_f(x)$. Existencia viene de R4; unicidad de R6. No se ha resuelto una ecuación diferencial general ni una condición que contenga la función desconocida a la derecha.

**Polinomios y potencias enteras.** C18 demostró por inducción $D(x^{n+1})=(n+1)x^n$ para enteros $n\ge0$; el denominador $n+1$ es positivo. La función $H(t)=t^{n+1}/(n+1)$ es continua y primitiva de $t^n$. Esa integranda es continua e integrable por C23, de modo que
$$\int_u^v t^n\,dt=\frac{v^{n+1}-u^{n+1}}{n+1}.$$
Con $n=0$ se recupera la integral constante sin potencias negativas. Sumas finitas y escalar de C23 permiten integrar polinomios término a término. No se extiende esta prueba a exponentes reales, ni a una serie infinita.

En particular $\int_0^1t^2\,dt=1/3$, en acuerdo con el cálculo por sumas de C22/C23. Para $f(t)=2t-1$, una primitiva es $t^2-t$, y $\int_0^1f=0$; sin embargo, partir en $1/2$ da
$$\int_0^{1/2}|2t-1|\,dt=\frac14,\qquad
\int_{1/2}^1|2t-1|\,dt=\frac14.$$
La integral de su absoluto es $1/2$. La cancelación no mide variación total ni vuelve cero a la integranda.

La acumulación de una continua positiva crece, por R3/C19 o directamente por R2. Cuando la tasa continua cambia de negativa a positiva, la acumulada puede tener un mínimo: para $2t-1$ en $[0,1]$, $A_f(1/2)=-1/4$. Ceros de la tasa corresponden a puntos estacionarios interiores por R3; no todo punto estacionario es extremo, como muestra una tasa $f(t)=3t^2$ en $[-1,1]$, cuya acumulada $t^3+1$ sigue creciendo a través de cero.

![Las primitivas x²−x y x²−x+1 difieren en constante1. Integral firmada de2t−1 es0; integral absoluta1/2 y aportes absolutos1/4 por mitad.](../../assets/books/anm/C24/C24-F06.svg){#fig-anm-c24-f06 fig-alt="Las primitivas x²−x y x²−x+1 difieren en constante1. Integral firmada de2t−1 es0; integral absoluta1/2 y aportes absolutos1/4 por mitad."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-041}

1. ¿En qué difieren dos primitivas sobre el mismo intervalo?

[]{#MA-MIC-ANM-01-024-042}

2. ¿Cómo se fija esa constante?

[]{#MA-MIC-ANM-01-024-043}

3. ¿Qué primitiva de una continua está normalizada?

[]{#MA-MIC-ANM-01-024-044}

4. ¿Qué solución corresponde al dato inicial $H(a)=c_0$?

[]{#MA-MIC-ANM-01-024-045}

5. ¿Qué primitiva tiene $t^n$ para entero $n\ge0$?

[]{#MA-MIC-ANM-01-024-046}

6. ¿Una integral firmada cero obliga a función cero?

[]{#MA-MIC-ANM-01-024-047}

7. ¿Cuánto integra $|2t-1|$ en $[0,1]$?

[]{#MA-MIC-ANM-01-024-048}

8. ¿Todo punto estacionario de la acumulada es extremo?

## 24.7. Partes y cambio de variable

[]{#MA-SEC-ANM-01-024-007}

El puente entre derivadas e integrales convierte reglas locales en identidades globales. Hay que declarar existencia de las integrales antes de evaluar sus valores.

**R7a — Integración por partes.** Sean $p,q$ continuas en $[a,b]$, derivables en $(a,b)$. Sean $v,w:[a,b]\to\mathbb R$ integrables, iguales respectivamente a $p',q'$ en el interior. Los valores en los bordes son extensiones declaradas; cambios finitos no afectan integrales. Las funciones continuas $p,q$ son integrables por C23; productos y sumas de integrables lo son por su álgebra. Por tanto $pw$ y $vq$ son integrables.

La regla del producto de C18 dice que $pq$ es una primitiva, continua en el cerrado, de $vq+pw$. Newton–Leibniz y linealidad dan
$$\int_a^b p(t)w(t)\,dt
=p(b)q(b)-p(a)q(a)-\int_a^b v(t)q(t)\,dt.$$
No basta que $p',q'$ existan; aquí se exige la integrabilidad de las extensiones. Un caso suficiente es que sean continuas en el cerrado. Para $p(t)=t$, $q(t)=t^2/2$ en $[0,1]$, la identidad da $\int_0^1t^2=1/2-1/6=1/3$, con el segundo valor calculado por R6. Es comprobación, no prueba circular del valor usado.

**R7b — Cambio de variable con signo.** Sea $f:[a,b]\to\mathbb R$ continua. Sea $g:[\alpha,\beta]\to[a,b]$ continua, con $\alpha<\beta$, derivable en el interior, y sea $v$ una extensión integrable de $g'$ a ese cerrado. La composición $f\circ g$ es continua, por lo que $(f\circ g)v$ es integrable por C23. Entonces
$$\int_\alpha^\beta f(g(t))v(t)\,dt=\int_{g(\alpha)}^{g(\beta)}f(s)\,ds.$$
Para probarlo, tome $F=A_f$. R3/R4 dan su derivada relativa de valor $f$ en todo $[a,b]$, incluidos los extremos. La cadena relativa de C18 aplicada a $F\circ g$ da derivada $f(g(t))g'(t)$ en cada punto interior. Todos los centros $g(t)$ acumulan en $[a,b]$; si un incremento de $g$ se anula, la versión de la cadena de C18 no divide por él. La composición es continua en el cerrado y constituye una primitiva de la integranda. R5 evalúa su integral como $F(g(\beta))-F(g(\alpha))$, y R1 identifica ese incremento con la integral orientada requerida.

No se exige monotonía de $g$: los recorridos de ida y vuelta se cancelan con el signo de $g'$. Con $f(s)=s$ en $[0,1]$ y $g(t)=t^2$ en $[-1,1]$, el integrando es $2t^3$ y la integral vale cero porque ambos valores extremos de $g$ son uno. Con $g(t)=1-t$ en $[0,1]$, el integrando es $-(1-t)$ y el valor es $-1/2$, igual a $\int_1^0s\,ds$. Reemplazar $g'$ por $|g'|$ cambia el problema: ya no es esta identidad de acumulación firmada.

![Con g(t)=t² en\[−1,1\] y f(s)=s, el integrando es2t³. Aportes−1/2 y1/2 cancelan; ambos extremos transformados son1. Con valor absoluto de g′ se obtiene1, una expresión diferente.](../../assets/books/anm/C24/C24-F07.svg){#fig-anm-c24-f07 fig-alt="Con g(t)=t² en\[−1,1\] y f(s)=s, el integrando es2t³. Aportes−1/2 y1/2 cancelan; ambos extremos transformados son1. Con valor absoluto de g′ se obtiene1, una expresión diferente."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-049}

1. ¿Qué regla diferencial produce integración por partes?

[]{#MA-MIC-ANM-01-024-050}

2. ¿Qué condición extra se pide a las derivadas en esa fórmula?

[]{#MA-MIC-ANM-01-024-051}

3. ¿Importan los valores de esas extensiones en los bordes?

[]{#MA-MIC-ANM-01-024-052}

4. ¿Qué primitiva prueba el cambio de variable?

[]{#MA-MIC-ANM-01-024-053}

5. ¿Debe ser monótono $g$ en la versión probada?

[]{#MA-MIC-ANM-01-024-054}

6. ¿Qué pasa si $g(\alpha)=g(\beta)$?

[]{#MA-MIC-ANM-01-024-055}

7. ¿Puede la cadena dividir siempre por el incremento de $g$?

[]{#MA-MIC-ANM-01-024-056}

8. ¿Reemplazar $g'$ por $|g'|$ conserva la misma identidad?

## 24.8. Qué invierte el teorema y qué conserva

[]{#MA-SEC-ANM-01-024-008}

Las dos operaciones se invierten con una normalización y un dominio precisos. Conviene cerrar el capítulo distinguiendo lo demostrado de lo que las fórmulas podrían sugerir.

**R8 — Dos direcciones y estabilidad.** En las funciones continuas $f:[a,b]\to\mathbb R$, integrar desde $a$ y después derivar recupera $f$ en el interior, y en los bordes mediante derivadas relativas. En las funciones $H$ continuas en el cerrado, derivables dentro y con una extensión integrable $f$ de su derivada, derivar e integrar recupera $H(x)-H(a)$. La constante inicial desaparece al derivar y debe reponerse al reconstruir $H$. La segunda dirección es R5 sobre cada restricción, no una consecuencia de continuidad de $f$ que no se ha exigido.

Para dos integrables $f,g$ con cota universal $|f(t)-g(t)|\le\eta$, $\eta\ge0$, la linealidad y la estimación integral dan
$$|A_f(x)-A_g(x)|\le\eta(x-a)\le\eta(b-a).$$
Además, para dos entradas, el cambio de la diferencia está acotado por $\eta|y-x|$. La acumulación amortigua perturbaciones uniformemente acotadas en el sentido de este certificado. Si $H'=f$ con $H(a)=c_0$ y otra primitiva $K'=g$ con $K(a)=d_0$, R5 sobre restricciones da
$$|H(x)-K(x)|\le |c_0-d_0|+\eta(x-a).$$
Cada hipótesis es universal sobre el intervalo: una tabla de errores pequeños no certifica la desigualdad. Si $f,g$ difieren sólo en un conjunto finito, C23 asegura integrales iguales en todas las restricciones, por lo que $A_f=A_g$ aunque no haya recuperación de sus valores excepcionales.

**Promedio alcanzado, con una herramienta adicional declarada.** Para una continua en $[u,v]$ con $u<v$, C16 da mínimo $m$ y máximo $M$ alcanzados. Orden integral encierra el promedio $\frac1{v-u}\int_u^v f$ entre ellos; C15, valor intermedio, entrega una entrada $c\in[u,v]$ donde $f(c)$ coincide con él. Es una consecuencia opcional del encierro, distinta de Lagrange y no usada en R3 ni R5. No garantiza unicidad ni un punto prescrible; para una constante, todos sirven. Para el escalón con salto a $1/2$, el promedio en $[0,1]$ es $1/2$, que no es ninguno de sus valores $0,1$: integrabilidad sola no garantiza un promedio alcanzado.

**Lo que queda fuera.** No hemos afirmado que toda derivada sea integrable, que toda integrable posea primitiva, ni que continuidad de la acumulada recupere continuidad de la tasa. El escalón y el pico de R4 ya refutan dos lecturas excesivas. La teoría de C25 estudiará qué discontinuidades permite Riemann; aquí no se importan criterios de medida ni una teoría de integrales impropias.

En el libro de cálculo podíamos usar estos puentes como reglas. Aquí cada dirección tiene su prueba: encierro de promedios para la primera, Lagrange y telescopía de incrementos para la segunda. Tasa local y acumulación global se conectan después de haber sido construidas por separado.

![En\[0,3\], tasas f(t)=t y g(t)=t+1/100 satisfacen error uniforme1/100. Diferencia de acumuladas x/100 y cota global3/100; la banda es un certificado universal probado.](../../assets/books/anm/C24/C24-F08.svg){#fig-anm-c24-f08 fig-alt="En\[0,3\], tasas f(t)=t y g(t)=t+1/100 satisfacen error uniforme1/100. Diferencia de acumuladas x/100 y cota global3/100; la banda es un certificado universal probado."}

**Microcontroles.**

[]{#MA-MIC-ANM-01-024-057}

1. ¿Qué recupera integrar y luego derivar una continua?

[]{#MA-MIC-ANM-01-024-058}

2. ¿Qué recupera derivar e integrar una primitiva admisible?

[]{#MA-MIC-ANM-01-024-059}

3. ¿Qué certificado da $|f-g|\le\eta$?

[]{#MA-MIC-ANM-01-024-060}

4. ¿Qué término agrega un error en el dato inicial?

[]{#MA-MIC-ANM-01-024-061}

5. ¿Cambios finitos de tasas alteran sus acumuladas?

[]{#MA-MIC-ANM-01-024-062}

6. ¿Qué asegura un promedio integral alcanzado?

[]{#MA-MIC-ANM-01-024-063}

7. ¿El escalón alcanza su promedio integral?

[]{#MA-MIC-ANM-01-024-064}

8. ¿Se ha probado que toda derivada es integrable?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)

[← Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Capítulo 25 →](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html)
