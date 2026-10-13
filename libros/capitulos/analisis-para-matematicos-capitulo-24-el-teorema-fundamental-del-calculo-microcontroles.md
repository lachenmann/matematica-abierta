---
content-id: MA-BCH-0301
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-024-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 24
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C24_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §24.1 — Construir una función de acumulación

### Microcontrol 001

[]{#MA-MIC-ANM-01-024-001}

[]{#MA-MSOL-ANM-01-024-001}

[]{#MA-SEC-ANM-01-024-001}

**Pregunta.** ¿Qué debe existir antes de definir $A_f(x)$?

**Solución.** Si $f$ es integrable en $[a,b]$, C23 prueba que su restricción a cada $[a,x]$, con $a<x\le b$, también lo es. Podemos entonces asignar $A_f(x)=\int_a^x f$. En $x=a$ se usa la convención de integral degenerada. La existencia de estas integrales precede a cualquier pregunta sobre la derivada de la nueva función.

### Microcontrol 002

[]{#MA-MIC-ANM-01-024-002}

[]{#MA-MSOL-ANM-01-024-002}

**Pregunta.** ¿Cuánto vale $A_f(a)$?

**Solución.** Se define $A_f(a)=\int_a^a f=0$. Esta normalización fija el valor inicial de la acumulación. La construcción por particiones estrictamente crecientes se aplica a intervalos de longitud positiva; el caso de extremos iguales tiene su convención propia.

### Microcontrol 003

[]{#MA-MIC-ANM-01-024-003}

[]{#MA-MSOL-ANM-01-024-003}

**Pregunta.** ¿Por qué la fórmula determina una función?

**Solución.** Para cada $x>a$, la restricción tiene una integral existente y única; para $x=a$, la convención determina cero. Por tanto la relación de pares $(x,r)$ con $r=\int_a^x f$ es total y univaluada sobre $[a,b]$. Su separación dentro de $[a,b]\times\mathbb R$ da un grafo sin tener que elegir entre posibles salidas.

### Microcontrol 004

[]{#MA-MIC-ANM-01-024-004}

[]{#MA-MSOL-ANM-01-024-004}

**Pregunta.** ¿Qué expresa $A_f(y)-A_f(x)$?

**Solución.** Si $x<y$, aditividad da $A_f(y)=A_f(x)+\int_x^y f$. Si $y<x$, la misma identidad aplicada al orden inverso y la convención de orientación dan $A_f(y)-A_f(x)=-\int_y^x f=\int_x^y f$. El incremento depende del tramo recorrido entre las entradas.

### Microcontrol 005

[]{#MA-MIC-ANM-01-024-005}

[]{#MA-MSOL-ANM-01-024-005}

**Pregunta.** ¿Qué ocurre si $x=y$?

**Solución.** Con $x=y$, la diferencia $A_f(y)-A_f(x)$ es cero y la integral $\int_x^x f$ también. La fórmula de incrementos sigue siendo válida. El cociente incremental sólo se considera después, bajo la condición $y\ne x$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-024-006}

[]{#MA-MSOL-ANM-01-024-006}

**Pregunta.** ¿Qué cambia al mover el origen a $c$?

**Solución.** La acumulación desde $c$ es $A_{f,c}(x)=\int_c^x f=A_f(x)-A_f(c)$, por aditividad orientada. Al restar los valores en dos entradas, la constante $A_f(c)$ se cancela. Cambiar el origen desplaza la función verticalmente y conserva sus incrementos y sus derivadas donde existan.

### Microcontrol 007

[]{#MA-MIC-ANM-01-024-007}

[]{#MA-MSOL-ANM-01-024-007}

**Pregunta.** ¿Debe ser no negativa la acumulación?

**Solución.** Una tasa negativa aporta acumulación negativa. Para $f(t)=2t-1$ en $[0,1]$, la fórmula afín por sumas da $A_f(x)=x^2-x=x(x-1)$. Vale cero en los extremos y es negativa cuando $0<x<1$. La parte positiva final compensa la contribución negativa inicial.

### Microcontrol 008

[]{#MA-MIC-ANM-01-024-008}

[]{#MA-MSOL-ANM-01-024-008}

**Pregunta.** ¿Se ha usado una primitiva en R1?

**Solución.** La integral de una tasa afín ya se calculó mediante sumas en C22. Para $f(t)=2t-1$, sobre $[0,x]$ esa cuenta da $x^2-x$. Usarla aquí construye la acumulada antes de demostrar el teorema fundamental; por tanto la prueba no presupone la regla de evaluar una primitiva.

## §24.2 — Incrementos, cotas y continuidad

### Microcontrol 009

[]{#MA-MIC-ANM-01-024-009}

[]{#MA-MSOL-ANM-01-024-009}

[]{#MA-SEC-ANM-01-024-002}

**Pregunta.** ¿Qué encierra el cociente medio?

**Solución.** Si $m\le f(t)\le M$ en el segmento entre $x$ e $y$, con $x<y$, el orden integral da $m(y-x)\le A_f(y)-A_f(x)\le M(y-x)$. Dividir por la longitud positiva encierra el cociente entre $m$ y $M$. Para $y<x$ se ordena el segmento y se cambian ambos signos del cociente.

### Microcontrol 010

[]{#MA-MIC-ANM-01-024-010}

[]{#MA-MSOL-ANM-01-024-010}

**Pregunta.** ¿Deben alcanzarse las cotas extremas locales?

**Solución.** La imagen de $f$ sobre el segmento es no vacía y acotada, así tiene ínfimo y supremo reales. Sus desigualdades valen en todas las entradas aunque esos extremos no se alcancen. El orden de integrales sólo usa las cotas universales, de modo que no necesita puntos de máximo o mínimo.

### Microcontrol 011

[]{#MA-MIC-ANM-01-024-011}

[]{#MA-MSOL-ANM-01-024-011}

**Pregunta.** ¿Qué da una cota $|f|\le B$?

**Solución.** Para $x<y$, integrar $-B\le f\le B$ da $-B(y-x)\le A_f(y)-A_f(x)\le B(y-x)$. Por tanto $|A_f(y)-A_f(x)|\le B(y-x)$. Intercambiar entradas cubre el otro orden y la igualdad es inmediata, obteniendo la cota Lipschitz $B|y-x|$ para todos los pares.

### Microcontrol 012

[]{#MA-MIC-ANM-01-024-012}

[]{#MA-MSOL-ANM-01-024-012}

**Pregunta.** ¿Qué radio evita dividir por $B=0$?

**Solución.** Tomamos $\delta=\varepsilon/(B+1)>0$, con $B\ge0$. Si $B>0$ y $|y-x|<\delta$, la cota Lipschitz da error menor que $B\varepsilon/(B+1)<\varepsilon$. Si $B=0$, todos los incrementos son cero. El mismo radio demuestra continuidad uniforme sin una división por cero.

### Microcontrol 013

[]{#MA-MIC-ANM-01-024-013}

[]{#MA-MSOL-ANM-01-024-013}

**Pregunta.** ¿Se necesita continuidad de $f$ para continuidad de $A_f$?

**Solución.** La integrabilidad de $f$ garantiza su acotación y la existencia de las integrales sobre restricciones. Esas dos propiedades bastan para $|A_f(y)-A_f(x)|\le B|y-x|$, que implica continuidad uniforme. El escalón con salto es un ejemplo de tasa discontinua cuya acumulada es continua.

### Microcontrol 014

[]{#MA-MIC-ANM-01-024-014}

[]{#MA-MSOL-ANM-01-024-014}

**Pregunta.** ¿Qué signo garantiza acumulación no decreciente?

**Solución.** Para $x<y$, la no negatividad de la tasa implica $\int_x^y f\ge0$. La identidad de incrementos da $A_f(y)\ge A_f(x)$, así la acumulada es no decreciente. Para asegurar incremento estrictamente positivo basta una cota $f\ge m>0$ sobre ese tramo.

### Microcontrol 015

[]{#MA-MIC-ANM-01-024-015}

[]{#MA-MSOL-ANM-01-024-015}

**Pregunta.** ¿Un pico positivo garantiza crecimiento estricto?

**Solución.** La tasa que vale uno sólo en $1/2$ y cero en el resto es no negativa y positiva en ese punto. Cada restricción difiere de la función cero en a lo sumo una entrada, así sus integrales son cero por C23. Su acumulada es constante. La positividad aislada no fuerza un incremento positivo de la integral.

### Microcontrol 016

[]{#MA-MIC-ANM-01-024-016}

[]{#MA-MSOL-ANM-01-024-016}

**Pregunta.** ¿Cuál es la acumulada del escalón con corte $1/2$?

**Solución.** Para el escalón $f(t)=0$ si $t<1/2$ y $f(t)=1$ si $t\ge1/2$, las restricciones hasta el corte integran cero, incluido el valor excepcional del extremo. Para $x>1/2$, aditividad suma esa contribución nula y la constante uno sobre $[1/2,x]$. Por tanto $A_f(x)=0$ para $x\le1/2$ y $A_f(x)=x-1/2$ para $x\ge1/2$.

## §24.3 — La tasa reaparece en un punto

### Microcontrol 017

[]{#MA-MIC-ANM-01-024-017}

[]{#MA-MSOL-ANM-01-024-017}

[]{#MA-SEC-ANM-01-024-003}

**Pregunta.** ¿Qué controla el lema del promedio local?

**Solución.** La hipótesis $|f(t)-f(x)|\le\eta$ en todo el tramo equivale a $f(x)-\eta\le f(t)\le f(x)+\eta$. Integrar y dividir por la longitud positiva encierra el promedio entre esas dos constantes. Así $\left|(A_f(y)-A_f(x))/(y-x)-f(x)\right|\le\eta$ para $y\ne x$.

### Microcontrol 018

[]{#MA-MIC-ANM-01-024-018}

[]{#MA-MSOL-ANM-01-024-018}

**Pregunta.** ¿Cómo se trata un incremento negativo?

**Solución.** Para $y<x$, trabajamos sobre $[y,x]$, cuya longitud $x-y$ es positiva. Las cotas integradas controlan $(A_f(x)-A_f(y))/(x-y)$. Este número es igual a $(A_f(y)-A_f(x))/(y-x)$ porque se niegan numerador y denominador. Así se obtiene el mismo encierro en ambos lados del centro.

### Microcontrol 019

[]{#MA-MIC-ANM-01-024-019}

[]{#MA-MSOL-ANM-01-024-019}

**Pregunta.** ¿Qué continuidad usa R3?

**Solución.** Para derivar $A_f$ en un punto interior $x$ basta la continuidad de $f$ en ese punto, además de la integrabilidad global. El radio de continuidad controla todas las alturas entre $x$ y una entrada próxima $y$. El promedio de esas alturas se aproxima a $f(x)$, dando la derivada.

### Microcontrol 020

[]{#MA-MIC-ANM-01-024-020}

[]{#MA-MSOL-ANM-01-024-020}

**Pregunta.** ¿Por qué aplicar continuidad a $\varepsilon/2$?

**Solución.** El paso de cotas de valores a cotas integrales produce una desigualdad no estricta. Pedir inicialmente $|f(t)-f(x)|<\varepsilon/2$ permite concluir que el error del cociente es a lo sumo $\varepsilon/2$, todavía menor que $\varepsilon$. Ese margen protege el límite requerido.

### Microcontrol 021

[]{#MA-MIC-ANM-01-024-021}

[]{#MA-MSOL-ANM-01-024-021}

**Pregunta.** ¿Quién precede a toda entrada cercana?

**Solución.** Dada $\varepsilon>0$, la continuidad en $x$ proporciona un radio que se fija antes de considerar las entradas $y$. Para toda $y$ del dominio con $0<|y-x|<\delta$, el segmento completo queda en esa vecindad y el cociente cumple el mismo error. Este orden de cuantificadores constituye la prueba de derivada.

### Microcontrol 022

[]{#MA-MIC-ANM-01-024-022}

[]{#MA-MSOL-ANM-01-024-022}

**Pregunta.** ¿Se escoge un punto de valor medio integral?

**Solución.** La prueba usa que todas las alturas del segmento corto están entre $f(x)-\eta$ y $f(x)+\eta$. Por orden integral, su promedio también queda entre esas cotas. No necesita que alguna entrada alcance el promedio ni construir un testigo que dependa del segmento.

### Microcontrol 023

[]{#MA-MIC-ANM-01-024-023}

[]{#MA-MSOL-ANM-01-024-023}

**Pregunta.** ¿Qué cota fina da Lipschitz $L$ para el residuo?

**Solución.** El residuo es la integral orientada de $f(t)-f(x)$. Lipschitz da $|f(t)-f(x)|\le L|t-x|$, cuya integral sobre el segmento ordenado es $L|y-x|^2/2$ por la fórmula afín. La desigualdad de valor absoluto integral da entonces $|A_f(y)-A_f(x)-f(x)(y-x)|\le L|y-x|^2/2$.

### Microcontrol 024

[]{#MA-MIC-ANM-01-024-024}

[]{#MA-MSOL-ANM-01-024-024}

**Pregunta.** ¿Cuál es la derivada de la acumulada de $t^2$ en $1/2$?

**Solución.** El cuadrado es continuo en $1/2$ y es integrable en $[0,1]$. La primera parte del fundamental da $A_f'(1/2)=f(1/2)=(1/2)^2=1/4$. También puede comprobarse con $A_f(x)=x^3/3$: su cociente es $1/4+h/2+h^2/3$, que tiende a $1/4$.

## §24.4 — Bordes, saltos y valores aislados

### Microcontrol 025

[]{#MA-MIC-ANM-01-024-025}

[]{#MA-MSOL-ANM-01-024-025}

[]{#MA-SEC-ANM-01-024-004}

**Pregunta.** ¿Qué derivada se afirma en $a$?

**Solución.** Si $f$ es continua relativamente en $a$, sus alturas sobre $[a,y]$ se aproximan uniformemente a $f(a)$ cuando $y$ se acerca desde la derecha. El encierro del promedio da $(A_f(y)-A_f(a))/(y-a)\to f(a)$. Es la derivada relativa al dominio $[a,b]$ en su extremo izquierdo.

### Microcontrol 026

[]{#MA-MIC-ANM-01-024-026}

[]{#MA-MSOL-ANM-01-024-026}

**Pregunta.** ¿Y en $b$?

**Solución.** En el extremo $b$, las entradas admisibles cercanas satisfacen $y<b$. Se aplica el encierro sobre $[y,b]$ y se cambian ambos signos del cociente para obtener $(A_f(y)-A_f(b))/(y-b)\to f(b)$. La continuidad relativa de la tasa en $b$ basta para esta derivada izquierda.

### Microcontrol 027

[]{#MA-MIC-ANM-01-024-027}

[]{#MA-MSOL-ANM-01-024-027}

**Pregunta.** ¿Se afirma una derivada bilateral de una prolongación?

**Solución.** La acumulada se ha definido sólo en $[a,b]$. Sus cocientes de borde utilizan las entradas de ese dominio, que llegan desde un único lado. Para hablar de una derivada bilateral habría que especificar una prolongación fuera del intervalo y comprobar su comportamiento adicional.

### Microcontrol 028

[]{#MA-MIC-ANM-01-024-028}

[]{#MA-MSOL-ANM-01-024-028}

**Pregunta.** ¿Qué ocurre con la acumulada de un salto?

**Solución.** La acotación del escalón asegura una acumulada Lipschitz, por tanto continua incluso en el corte. Su fórmula tiene pendiente cero antes de $1/2$ y pendiente uno después. Las dos ramas se unen en altura cero, pero sus cocientes en el punto de unión tienen límites distintos.

### Microcontrol 029

[]{#MA-MIC-ANM-01-024-029}

[]{#MA-MSOL-ANM-01-024-029}

**Pregunta.** ¿Qué cocientes tiene el escalón en su corte?

**Solución.** En $c=1/2$, $A_f(c)=0$. Si $h<0$, $A_f(c+h)=0$ y el cociente vale cero. Si $h>0$, $A_f(c+h)=h$ y el cociente vale uno. Como los dos lados no comparten límite, la acumulada carece de derivada en el corte.

### Microcontrol 030

[]{#MA-MIC-ANM-01-024-030}

[]{#MA-MSOL-ANM-01-024-030}

**Pregunta.** ¿Qué acumulada tiene el pico aislado?

**Solución.** El pico difiere de la función cero en un punto. C23 conserva las integrales de todas sus restricciones, incluso cuando ese punto es un extremo de la restricción. Cada valor de la acumulada es por tanto cero. El efecto nodal desaparece al integrar sobre cualquier tramo.

### Microcontrol 031

[]{#MA-MIC-ANM-01-024-031}

[]{#MA-MSOL-ANM-01-024-031}

**Pregunta.** ¿En el pico existe la derivada de la acumulada?

**Solución.** La acumulada del pico es idénticamente cero, así todos sus cocientes incrementales son cero y su derivada existe en el pico con valor cero. Allí la integranda vale uno. La tasa es discontinua en esa entrada y no cumple la hipótesis de la primera parte del fundamental.

### Microcontrol 032

[]{#MA-MIC-ANM-01-024-032}

[]{#MA-MSOL-ANM-01-024-032}

**Pregunta.** ¿Continuidad local se probó necesaria para que exista la derivada?

**Solución.** El teorema demuestra que la continuidad de la tasa en el centro basta para recuperar su valor al derivar. El pico tiene una acumulada derivable en su punto excepcional aunque la tasa sea discontinua allí. Por tanto esa continuidad no es necesaria para la mera existencia de la derivada de la acumulada.

## §24.5 — De una primitiva a la integral

### Microcontrol 033

[]{#MA-MIC-ANM-01-024-033}

[]{#MA-MSOL-ANM-01-024-033}

[]{#MA-SEC-ANM-01-024-005}

**Pregunta.** ¿Qué exige una primitiva sobre el cerrado?

**Solución.** En este capítulo una primitiva admisible $H$ es continua en $[a,b]$, derivable en $(a,b)$ y satisface $H'(x)=f(x)$ para todo punto interior. La continuidad en los dos extremos permite aplicar Lagrange también a las piezas que los tocan. Las igualdades de derivadas se exigen sólo donde hay derivabilidad interior.

### Microcontrol 034

[]{#MA-MIC-ANM-01-024-034}

[]{#MA-MSOL-ANM-01-024-034}

**Pregunta.** ¿La definición de primitiva incluye integrabilidad de $f$?

**Solución.** La definición de primitiva expresa regularidad de $H$ y una igualdad de derivadas. Para Newton–Leibniz se añade que $f$ sea integrable en el cerrado, asegurando la existencia del valor que se quiere evaluar. La existencia de derivadas por sí sola no proporciona aquí esa integrabilidad.

### Microcontrol 035

[]{#MA-MIC-ANM-01-024-035}

[]{#MA-MSOL-ANM-01-024-035}

**Pregunta.** ¿Qué herramienta controla el incremento en cada pieza?

**Solución.** Sobre una pieza $[x_{i-1},x_i]$, la restricción de $H$ es continua y derivable en su interior. Lagrange proporciona $c_i$ interior con $H(x_i)-H(x_{i-1})=H'(c_i)\Delta_i=f(c_i)\Delta_i$. Las cotas locales de $f$ convierten esa identidad en dos desigualdades de incrementos.

### Microcontrol 036

[]{#MA-MIC-ANM-01-024-036}

[]{#MA-MSOL-ANM-01-024-036}

**Pregunta.** ¿Qué se suma tras eliminar el testigo de Lagrange?

**Solución.** Cada testigo de Lagrange tiene altura entre $m_i$ y $M_i$, así $m_i\Delta_i\le H(x_i)-H(x_{i-1})\le M_i\Delta_i$. Una vez obtenida esta desigualdad para un índice arbitrario, se suma sobre todos los índices. Los testigos dejan de aparecer en la conclusión y no hace falta formar una familia de etiquetas.

### Microcontrol 037

[]{#MA-MIC-ANM-01-024-037}

[]{#MA-MSOL-ANM-01-024-037}

**Pregunta.** ¿Por qué telescopa la suma central?

**Solución.** La suma central es $H(x_1)-H(x_0)+H(x_2)-H(x_1)+\cdots+H(x_n)-H(x_{n-1})$. Cada valor de nodo interior aparece con ambos signos, así se cancela. Queda $H(b)-H(a)$, encerrado entre $L(f,P)$ y $U(f,P)$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-024-038}

[]{#MA-MSOL-ANM-01-024-038}

**Pregunta.** ¿Qué convierte el encierro en igualdad con la integral?

**Solución.** Para cualquier partición, la integral y $H(b)-H(a)$ quedan en $[L(f,P),U(f,P)]$. Su distancia no supera la brecha. La integrabilidad proporciona brechas menores que cada tolerancia positiva, obligando a que esa distancia sea cero. Así $\int_a^b f=H(b)-H(a)$.

### Microcontrol 039

[]{#MA-MIC-ANM-01-024-039}

[]{#MA-MSOL-ANM-01-024-039}

**Pregunta.** ¿Se usa continuidad de $f$ en la segunda parte?

**Solución.** La segunda parte emplea integrabilidad de $f$ y una primitiva continua en el cerrado y derivable dentro. Lagrange controla sus incrementos y Darboux identifica el valor. La continuidad de la tasa no interviene en esos dos pasos y puede omitirse en esta dirección.

### Microcontrol 040

[]{#MA-MIC-ANM-01-024-040}

[]{#MA-MSOL-ANM-01-024-040}

**Pregunta.** ¿Por qué conservar continuidad de $H$ en los bordes?

**Solución.** Si $H(0)=1$ y $H(x)=0$ para $x>0$, su derivada interior es cero. Sin embargo $H(1)-H(0)=-1$, mientras la integral de la tasa cero es cero. La discontinuidad del borde impide aplicar Lagrange en la primera pieza. Conservar la continuidad de $H$ evita ese fallo de evaluación.

## §24.6 — Normalización, cálculo y signo

### Microcontrol 041

[]{#MA-MIC-ANM-01-024-041}

[]{#MA-MSOL-ANM-01-024-041}

[]{#MA-SEC-ANM-01-024-006}

**Pregunta.** ¿En qué difieren dos primitivas sobre el mismo intervalo?

**Solución.** Para primitivas $H,K$ de la misma tasa, $D=H-K$ es continua en el cerrado y derivable dentro, con $D'=H'-K'=0$. Lagrange en cualquier segmento $[u,v]$ del dominio da $D(v)-D(u)=0$. Por tanto $D$ toma una sola constante en todo el intervalo.

### Microcontrol 042

[]{#MA-MIC-ANM-01-024-042}

[]{#MA-MSOL-ANM-01-024-042}

**Pregunta.** ¿Cómo se fija esa constante?

**Solución.** Si $H-K=C$, evaluar en cualquier entrada $c$ da $C=H(c)-K(c)$. En particular, el dato inicial en $a$ fija esa diferencia. Si ambas primitivas tienen el mismo valor inicial, la constante es cero y coinciden en todo el dominio.

### Microcontrol 043

[]{#MA-MIC-ANM-01-024-043}

[]{#MA-MSOL-ANM-01-024-043}

**Pregunta.** ¿Qué primitiva de una continua está normalizada?

**Solución.** Una tasa continua es integrable por C23 y su acumulada $A_f$ es continua en el cerrado, con derivada $f$ dentro por la primera parte. Además $A_f(a)=0$. Cualquier otra primitiva con ese valor inicial difiere de $A_f$ en una constante que vale cero al evaluar en $a$, así coincide con ella.

### Microcontrol 044

[]{#MA-MIC-ANM-01-024-044}

[]{#MA-MSOL-ANM-01-024-044}

**Pregunta.** ¿Qué solución corresponde al dato inicial $H(a)=c_0$?

**Solución.** Para una tasa continua, $H(x)=c_0+A_f(x)$ cumple $H(a)=c_0$ y $H'=f$ en el interior. Sumar una constante conserva continuidad y derivada. Si otra primitiva cumple el mismo dato, la diferencia tiene derivada cero y valor inicial cero, luego es idénticamente cero.

### Microcontrol 045

[]{#MA-MIC-ANM-01-024-045}

[]{#MA-MSOL-ANM-01-024-045}

**Pregunta.** ¿Qué primitiva tiene $t^n$ para entero $n\ge0$?

**Solución.** Para un entero $n\ge0$, la regla de potencias de C18 da $\big(t^{n+1}/(n+1)\big)'=t^n$. El divisor es positivo porque $n+1\ge1$. Esa función es continua en cualquier cerrado y constituye una primitiva admisible; para $n=0$ se obtiene simplemente $t$.

### Microcontrol 046

[]{#MA-MIC-ANM-01-024-046}

[]{#MA-MSOL-ANM-01-024-046}

**Pregunta.** ¿Una integral firmada cero obliga a función cero?

**Solución.** Para $f(t)=2t-1$ en $[0,1]$, una primitiva es $t^2-t$. Su diferencia de valores extremos es cero, así la integral vale cero. La tasa toma valores negativos y positivos y no es la función cero: las dos contribuciones se compensan.

### Microcontrol 047

[]{#MA-MIC-ANM-01-024-047}

[]{#MA-MSOL-ANM-01-024-047}

**Pregunta.** ¿Cuánto integra $|2t-1|$ en $[0,1]$?

**Solución.** Antes de $1/2$, el absoluto es $1-2t$ y su integral es $[t-t^2]_0^{1/2}=1/4$. Después es $2t-1$ y su integral es $[t^2-t]_{1/2}^1=1/4$. La aditividad da $\int_0^1|2t-1|=1/2$.

### Microcontrol 048

[]{#MA-MIC-ANM-01-024-048}

[]{#MA-MSOL-ANM-01-024-048}

**Pregunta.** ¿Todo punto estacionario de la acumulada es extremo?

**Solución.** En $[-1,1]$, la tasa $3t^2$ tiene acumulada $A_f(x)=x^3+1$. Su derivada en cero es cero, pero para entradas negativas próximas su altura es menor que uno y para entradas positivas es mayor. Así cero es estacionario y la función lo atraviesa creciendo, sin máximo ni mínimo allí.

## §24.7 — Partes y cambio de variable

### Microcontrol 049

[]{#MA-MIC-ANM-01-024-049}

[]{#MA-MSOL-ANM-01-024-049}

[]{#MA-SEC-ANM-01-024-007}

**Pregunta.** ¿Qué regla diferencial produce integración por partes?

**Solución.** La regla del producto da $(pq)'=p'q+pq'$ en el interior. Con extensiones integrables $v=p'$ y $w=q'$, el producto $pq$ es una primitiva admisible de $vq+pw$. Newton–Leibniz y linealidad dan $\int_a^b pw=[pq]_a^b-\int_a^b vq$.

### Microcontrol 050

[]{#MA-MIC-ANM-01-024-050}

[]{#MA-MSOL-ANM-01-024-050}

**Pregunta.** ¿Qué condición extra se pide a las derivadas en esa fórmula?

**Solución.** Se piden funciones $v,w$ integrables en $[a,b]$ que coincidan con las derivadas interiores de $p,q$. Como $p,q$ son continuas, también son integrables, y C23 garantiza la integrabilidad de $pw$ y $vq$. Así las dos integrales de la fórmula existen antes de evaluarlas.

### Microcontrol 051

[]{#MA-MIC-ANM-01-024-051}

[]{#MA-MSOL-ANM-01-024-051}

**Pregunta.** ¿Importan los valores de esas extensiones en los bordes?

**Solución.** Las extensiones de las derivadas pueden asignar cualquier valor real en los dos extremos. Cambiar esas alturas modifica sus productos con $p,q$ sólo en un conjunto finito, por lo que las integrales se conservan. La identidad diferencial del producto se usa en el interior y no exige igualdades de derivadas bilaterales en los bordes.

### Microcontrol 052

[]{#MA-MIC-ANM-01-024-052}

[]{#MA-MSOL-ANM-01-024-052}

**Pregunta.** ¿Qué primitiva prueba el cambio de variable?

**Solución.** Ponemos $F=A_f$ para la tasa continua $f$. Las derivadas relativas de $F$ tienen valor $f$ en todo su dominio. La cadena aplicada a $F\circ g$ da $(F\circ g)'(t)=f(g(t))g'(t)$ en el interior del intervalo de $g$. Esa composición, continua en el cerrado, es la primitiva que permite evaluar la integral transformada.

### Microcontrol 053

[]{#MA-MIC-ANM-01-024-053}

[]{#MA-MSOL-ANM-01-024-053}

**Pregunta.** ¿Debe ser monótono $g$ en la versión probada?

**Solución.** El cambio de variable probado usa el signo de $g'$ y no requiere monotonía de $g$. Para $g(t)=t^2$ en $[-1,1]$, el recorrido baja de uno a cero y vuelve a uno. Con $f(s)=s$, la integranda es $2t^3$ y las contribuciones de los dos lados se cancelan.

### Microcontrol 054

[]{#MA-MIC-ANM-01-024-054}

[]{#MA-MSOL-ANM-01-024-054}

**Pregunta.** ¿Qué pasa si $g(\alpha)=g(\beta)$?

**Solución.** Bajo las hipótesis de continuidad y de extensión integrable de $g'$, la integral transformada vale $F(g(\beta))-F(g(\alpha))$. Si las dos imágenes extremas coinciden, esta diferencia es cero. El recorrido interior puede ser no constante y aun así volver al mismo valor acumulado.

### Microcontrol 055

[]{#MA-MIC-ANM-01-024-055}

[]{#MA-MSOL-ANM-01-024-055}

**Pregunta.** ¿Puede la cadena dividir siempre por el incremento de $g$?

**Solución.** Puede ocurrir $g(t+h)=g(t)$ con $h\ne0$, y el cociente exterior dividido por ese incremento no estaría definido. La cadena de C18 escribe el incremento de $F$ como su término lineal más un residuo, que se define cero cuando el incremento interior es cero. Esto mantiene la prueba válida en esas entradas.

### Microcontrol 056

[]{#MA-MIC-ANM-01-024-056}

[]{#MA-MSOL-ANM-01-024-056}

**Pregunta.** ¿Reemplazar $g'$ por $|g'|$ conserva la misma identidad?

**Solución.** El signo de $g'$ registra el sentido del recorrido. Para $g(t)=t^2$ y $f(s)=s$, usar $g'$ da integranda $2t^3$ e integral cero en $[-1,1]$. Usar $|g'|$ da $2|t|^3$, cuya integral es uno. Se pierde la cancelación entre la ida y la vuelta.

## §24.8 — Qué invierte el teorema y qué conserva

### Microcontrol 057

[]{#MA-MIC-ANM-01-024-057}

[]{#MA-MSOL-ANM-01-024-057}

[]{#MA-SEC-ANM-01-024-008}

**Pregunta.** ¿Qué recupera integrar y luego derivar una continua?

**Solución.** Si $f$ es continua en todo $[a,b]$, la derivada interior de $A_f$ vale $f$ en cada punto. En $a$ y $b$ se recuperan los valores mediante derivadas relativas derecha e izquierda. Los tres casos emplean el mismo encierro de promedios sobre segmentos cortos admisibles.

### Microcontrol 058

[]{#MA-MIC-ANM-01-024-058}

[]{#MA-MSOL-ANM-01-024-058}

**Pregunta.** ¿Qué recupera derivar e integrar una primitiva admisible?

**Solución.** Si $H$ es una primitiva admisible y su tasa $f$ es integrable, Newton–Leibniz sobre cada restricción da $A_f(x)=H(x)-H(a)$. La derivación había eliminado la constante inicial. Para reconstruir $H$ se vuelve a sumar el valor $H(a)$.

### Microcontrol 059

[]{#MA-MIC-ANM-01-024-059}

[]{#MA-MSOL-ANM-01-024-059}

**Pregunta.** ¿Qué certificado da $|f-g|\le\eta$?

**Solución.** Para dos tasas integrables con $|f-g|\le\eta$, linealidad da $A_f(x)-A_g(x)=\int_a^x(f-g)$. Integrar la cota absoluta produce $|A_f(x)-A_g(x)|\le\eta(x-a)\le\eta(b-a)$. El certificado vale para toda entrada y usa la cota de la tasa sobre el intervalo completo.

### Microcontrol 060

[]{#MA-MIC-ANM-01-024-060}

[]{#MA-MSOL-ANM-01-024-060}

**Pregunta.** ¿Qué término agrega un error en el dato inicial?

**Solución.** Si $H(x)=c_0+A_f(x)$ y $K(x)=d_0+A_g(x)$, la triangular da $|H(x)-K(x)|\le|c_0-d_0|+|A_f(x)-A_g(x)|$. Con error de tasas a lo sumo $\eta$, queda $|c_0-d_0|+\eta(x-a)$. El error inicial actúa como un desplazamiento fijo y el de la tasa se acumula con la longitud.

### Microcontrol 061

[]{#MA-MIC-ANM-01-024-061}

[]{#MA-MSOL-ANM-01-024-061}

**Pregunta.** ¿Cambios finitos de tasas alteran sus acumuladas?

**Solución.** Cada restricción de dos tasas que difieren en un conjunto finito sigue difiriendo sólo en un conjunto finito. C23 conserva sus integrales, así $A_f(x)=A_g(x)$ para toda entrada. Por ello la acumulada puede olvidar valores excepcionales de la tasa.

### Microcontrol 062

[]{#MA-MIC-ANM-01-024-062}

[]{#MA-MSOL-ANM-01-024-062}

**Pregunta.** ¿Qué asegura un promedio integral alcanzado?

**Solución.** Para una continua en $[u,v]$, con $u<v$, compacidad da mínimo $m$ y máximo $M$ alcanzados. El promedio $\mu=(v-u)^{-1}\int_u^v f$ está entre ellos por orden integral. El valor intermedio sobre el segmento entre puntos de esos extremos proporciona $c$ con $f(c)=\mu$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-024-063}

[]{#MA-MSOL-ANM-01-024-063}

**Pregunta.** ¿El escalón alcanza su promedio integral?

**Solución.** El escalón de corte $1/2$ tiene integral $1/2$ en un intervalo de longitud uno, así su promedio es $1/2$. Sus únicas alturas son cero y uno, y ninguna entrada tiene esa altura promedio. Es integrable, pero la continuidad necesaria para aplicar valor intermedio falla en el corte.

### Microcontrol 064

[]{#MA-MIC-ANM-01-024-064}

[]{#MA-MSOL-ANM-01-024-064}

**Pregunta.** ¿Se ha probado que toda derivada es integrable?

**Solución.** En Newton–Leibniz, partes y cambio de variable se declara explícitamente la integrabilidad de la tasa o de la extensión de la derivada. La existencia puntual de las derivadas no ha sido usada para probarla en general. Las conclusiones del capítulo conservan esa premisa.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)
