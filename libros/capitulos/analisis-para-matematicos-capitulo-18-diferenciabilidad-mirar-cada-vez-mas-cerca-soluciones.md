---
content-id: MA-BCH-0276
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-018-SOLUCIONES
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
title: Soluciones — Capítulo 18
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C18_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)

## 18.1. El centro y el dominio perforado

[]{#MA-EX-ANM-01-018-001}

[]{#MA-SOL-ANM-01-018-001}

[]{#MA-SEC-ANM-01-018-001}

Se exige $a\in D\cap\operatorname{Acc}(D)$ y un real $L$ con $\forall\eta>0\exists\delta>0\forall x\in D$, $0<|x-a|<\delta$ implica $|(f(x)-f(a))/(x-a)-L|<\eta$. El cociente vive en $D\setminus\{a\}$. En un aislado existe un radio sin entradas perforadas, de modo que cualquier $L$ cumpliría la condición vacía y se perdería unicidad. En $\{0\}$ no se define derivada. En $[0,\infty)$, cero es de acumulación y el límite relativo sólo usa entradas positivas; es un concepto de derivada derecha respecto de ese dominio.

La evaluación central y la acumulación son premisas diferentes: la primera permite formar el numerador y la segunda impide que la prueba de límite sea vacía. El radio controla una precisión de pendiente y debe funcionar para todas las entradas perforadas admitidas. En el semieje la aproximación relativa sólo visita un lado, mientras en el singleton no existen secantes que determinen una pendiente.

## 18.2. Secantes del cuadrado

[]{#MA-EX-ANM-01-018-002}

[]{#MA-SOL-ANM-01-018-002}

Para $h\ne0$, $[(a+h)^2-a^2]/h=2a+h$. Dada tolerancia $\eta>0$, $\delta=\eta$ hace la diferencia respecto de $2a$ menor que $\eta$, así $f\prime(a)=2a$. En uno, las tres pendientes son $5/2,3/2,21/10$. Ninguna secante concreta se identifica con la derivada sólo por estar cerca; el límite es dos y controla todas las entradas suficientemente próximas.

**Retorno visual.** Véase [C18-F01](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La cancelación de $h$ se realiza únicamente en el dominio perforado. El radio explícito prueba un control de todas las secantes, algo que no aportan tres valores particulares. Las secantes de incrementos positivos y negativos se sitúan a ambos lados de dos, pero su error se mide con la misma magnitud $|h|$. Así se separa el límite de sus aproximaciones concretas.

## 18.3. Dos límites candidatos

[]{#MA-EX-ANM-01-018-003}

[]{#MA-SOL-ANM-01-018-003}

Si $L,M$ cumplen la definición y $d=|L-M|>0$, pedimos tolerancia $d/3$ a ambas condiciones. El mínimo de sus radios es positivo. Acumulación entrega un único testigo perforado dentro de ese mínimo. Para su pendiente $q$, $d\le|L-q|+|q-M|<2d/3$, contradicción. Se obtiene existencia de un testigo para el radio fijado, sin una elección simultánea de entradas.

Ambos controles se piden para el mismo centro y la misma tolerancia de pendiente. El mínimo de radios permite aplicarlos a una sola secante. Acumulación justifica un testigo dentro de esa ventana y la triangular produce la contradicción. No hace falta construir simultáneamente testigos a todas las escalas ni una ruta seleccionada.

## 18.4. Una restricción pierde un lado

[]{#MA-EX-ANM-01-018-004}

[]{#MA-SOL-ANM-01-018-004}

En el dominio positivo perforado, el cociente es $|x|/x=1$, así cualquier radio sirve para cualquier tolerancia y la derivada relativa es uno. Sobre la recta, el cociente en las entradas negativas es menos uno. Para todo radio hay entradas positivas y negativas con pendientes separadas por dos, incompatibles con acercamiento común a un real. La restricción de una derivada existente la conserva si acumula en el centro, pero una derivada restringida puede omitir entradas que impiden el límite en el dominio mayor.

La derivada relativa sólo exige el límite de las secantes que sobreviven a la restricción. En el semieje todas valen uno. Al ampliar el dominio se agregan secantes negativas de valor menos uno y deja de existir un destino común. La herencia de derivada funciona hacia restricciones acumulantes, pero esta conclusión no se invierte.

## 18.5. Cambiar el valor central

[]{#MA-EX-ANM-01-018-005}

[]{#MA-SOL-ANM-01-018-005}

Para $x\ne0$, $q_{F,0}(x)=x-1/x$, que no tiene límite finito en cero. Más directamente, $F$ no es continua en cero: las entradas $x_n=1/(n+1)$ tienen salidas tendentes a cero, distintas del valor central uno; R3 refuta derivabilidad. Este uso de R3 es una consecuencia posterior de R1 dentro del capítulo. El cuadrado usual sí tiene valor central cero y derivada cero. Que dos funciones coincidan en el dominio perforado no garantiza iguales cocientes si sus valores centrales difieren.

El valor central aparece en todos los numeradores incrementales y no puede modificarse sin cambiar los cocientes. Las salidas perforadas conservan su límite cero mientras la función asigna uno en el centro. La discontinuidad refuta derivabilidad por la implicación de R3. Coincidir fuera del centro no basta para conservar una derivada centrada allí.

## 18.6. Traducir el error

[]{#MA-EX-ANM-01-018-006}

[]{#MA-SOL-ANM-01-018-006}

[]{#MA-SEC-ANM-01-018-002}

Para $x\ne a$, $r_L(x)/(x-a)=q_{f,a}(x)-L$. Por tanto la condición de límite cero de ese cociente equivale término a término a la definición de derivada. En magnitudes, multiplicar o dividir por el positivo $|x-a|$ traduce $|q-L|<\eta$ en $|r_L|<\eta|x-a|$. En el centro $r_L(a)=0$, sin atribuir allí un cociente. Ambos sentidos conservan el mismo radio y dominio perforado.

El resto se define restando el valor central y el término lineal propuesto. La identidad de razones muestra que las dos condiciones son equivalentes para cada entrada perforada, sin cambiar los cuantificadores ni radios. El uso de magnitudes conserva el control también para incrementos negativos. En el centro se comprueba el resto cero por evaluación directa y no por una división.

## 18.7. Un marco completo de zoom

[]{#MA-EX-ANM-01-018-007}

[]{#MA-SOL-ANM-01-018-007}

$G_t(u)=[(1+tu)^2-1]/t=2u+tu^2$. En el marco $|u|\le2$, el error es $tu^2\le4t$. Si $0<t<\varepsilon/4$, es menor que $\varepsilon$ para todos los puntos del marco simultáneamente. El dominio es toda la recta, así todos son admisibles. El marco acotado permite una cota común; sin acotarlo el término $tu^2$ no queda pequeño para todo $u$ con un mismo $t>0$.

**Retorno visual.** Véase [C18-F02](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La ampliación divide la variación vertical por la misma escala que cambia las coordenadas horizontales. El término lineal queda $2u$ y el resto ampliado queda $tu^2$. La cota de marco convierte este último en un error común $4t$. Su dependencia del marco explica por qué la aproximación se afirma en regiones acotadas de coordenadas ampliadas.

## 18.8. Todas las rectas tienen error absoluto pequeño

[]{#MA-EX-ANM-01-018-008}

[]{#MA-SOL-ANM-01-018-008}

El resto es $(2a-M)h+h^2$, cuya magnitud no supera $(|2a-M|+|h|)|h|$ y tiende a cero cuando $h\to0$. Pero su cociente por $h$ es $2a-M+h$, con límite $2a-M$. Este límite sólo vale cero si $M=2a$. El error absoluto no distingue pendientes porque todas las rectas pasan por el mismo punto y son continuas allí; el error normalizado sí las distingue.

El término proporcional a $h$ tiende a cero incluso cuando su coeficiente es no nulo. Por eso cualquier pendiente propuesta produce error absoluto pequeño. Al dividir por $h$, ese coeficiente permanece y sólo desaparece para la pendiente correcta. El modelo de primer orden exige esa segunda comprobación, que es más fuerte que continuidad del error.

## 18.9. No hace falta escoger rutas

[]{#MA-EX-ANM-01-018-009}

[]{#MA-SOL-ANM-01-018-009}

Si sirven $L,M$ distintos, sea $d=|L-M|>0$. Las estimaciones con presupuesto $d/3$ entregan dos radios. Acumulación permite un punto distinto del centro en el menor de ellos. Como $(L-M)(x-a)=r_M(x)-r_L(x)$, la triangular y ambas cotas dan $d|x-a|<2d|x-a|/3$. Dividir por $|x-a|>0$ contradice $d>0$. No se construye una sucesión ni se elige un testigo para cada radio a la vez.

Las dos identidades de resto contienen los mismos valores de función y por ello éstos se cancelan al restarlas. Queda una comparación entre diferencia de pendientes y suma de errores. La entrada de acumulación tiene distancia positiva y permite dividir sin pérdida de información. Un único testigo bajo los dos radios basta para probar unicidad.

## 18.10. Zoom sobre un dominio roto

[]{#MA-EX-ANM-01-018-010}

[]{#MA-SOL-ANM-01-018-010}

Cero acumula en $D$ por las entradas explícitas $1/(n+1)$. Para $x\in D\setminus\{0\}$, $q=x$, por lo que $\delta=\eta$ prueba derivada cero. Para $t>0$, las entradas del zoom son $u=0$ y $u=1/[t(n+1)]$. Allí $G_t(u)=tu^2$. En $|u|\le R$ el error no supera $tR^2$, pero no se ha definido $G_t$ en los otros puntos del marco. La estimación es común a las entradas admisibles y no rellena los huecos del dominio.

La sucesión explícita acredita acumulación del dominio en cero, pero los radios de derivada controlan todas sus entradas, no sólo una cola elegida. En el zoom, resolver $tu\in D$ determina exactamente las coordenadas permitidas. La cota por $tR^2$ es válida en todo el marco admisible. No implica que la función ampliada esté definida en los huecos entre esas coordenadas.

## 18.11. De pendientes a valores

[]{#MA-EX-ANM-01-018-011}

[]{#MA-SOL-ANM-01-018-011}

[]{#MA-SEC-ANM-01-018-003}

La tolerancia uno de derivabilidad da $r>0$ con $|q-L|<1$ en el radio perforado, así $|q|<C=|L|+1>0$. Multiplicar por $|x-a|$ da error de valores menor que $C|x-a|$. Para $\varepsilon>0$, $\delta=\min(r,\varepsilon/C)$ sirve para todo argumento distinto del centro de distancia menor. En el centro el error es cero. Esta última comprobación convierte un control perforado en continuidad sobre una bola no perforada del mismo dominio.

Primero se obtiene una barrera finita de pendientes usando tolerancia uno, sin depender del desafío posterior de valores. Después se reduce la distancia de entrada según esa barrera. El centro, excluido de los cocientes, se incorpora por su error de valor cero. La prueba concluye continuidad relativa en todo el dominio de aproximación sin evaluar la secante en el centro.

## 18.12. La esquina refuta todos los radios

[]{#MA-EX-ANM-01-018-012}

[]{#MA-SOL-ANM-01-018-012}

La triangular inversa da $||x|-|a||\le|x-a|$, de modo que $\delta=\varepsilon$ prueba continuidad en cada $a$. Si existiera derivada $L$ en cero, tolerancia $1/2$ daría un radio $\delta$. En $\delta/2$ y $-\delta/2$ los cocientes valen uno y menos uno, respectivamente, y ambos tendrían error menor que $1/2$ respecto de $L$. Entonces $2\le|1-L|+|L+1|<1$, contradicción. La prueba no se apoya en la apariencia del gráfico.

**Retorno visual.** Véase [C18-F03](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La continuidad usa una desigualdad de valores válida para cualquier par, incluidos los centros. La no derivabilidad usa una precisión fija de pendientes y dos entradas perforadas dentro del radio que ofrecería el candidato. Sus cocientes incompatibles contradicen la triangular. Así continuidad y falta de derivada quedan demostradas con controles distintos y completos.

## 18.13. Pendiente cero sin extremo

[]{#MA-EX-ANM-01-018-013}

[]{#MA-SOL-ANM-01-018-013}

Para $h\ne0$, el cociente vale $h^2$; $\delta=\sqrt\eta$ da error menor que $\eta$ y prueba derivada cero. Todo radio admite $h=\delta/2>0$ y $-h<0$, con valores $h^3>0$ y $-h^3<0$ respecto del valor central cero. Así ninguna vecindad relativa tiene todos sus valores por encima o por debajo del central, y tampoco son constantes. La recta horizontal local no contiene información suficiente para decidir extremos.

La precisión de pendiente se convierte en radio mediante la raíz positiva de $\eta$. Las entradas de signos opuestos dentro de cualquier ventana producen valores a ambos lados de cero. Por eso no hay constancia ni extremo local, aunque el término lineal del modelo sea horizontal. No se utiliza una regla sobre extremos que aún no haya sido demostrada.

## 18.14. Control centrado sin Lipschitz vecino

[]{#MA-EX-ANM-01-018-014}

[]{#MA-SOL-ANM-01-018-014}

Como $F(0)=0$ y $|F(x)|\le x^2$, $|q_{F,0}(x)|\le|x|$ prueba derivada cero con $\delta=\eta$. En cada $b\ne0$ es discontinua: si es racional, irracionales arbitrariamente próximos tienen salida cero en lugar de $b^2$; si es irracional, racionales con $|x-b|<|b|/2$ tienen salida mayor que $b^2/4$ en lugar de cero. La densidad garantiza tales testigos en cualquier radio. Una cota Lipschitz para todos los pares de alguna bola de cero implicaría continuidad en cada punto interior de esa bola, por radio $\varepsilon/L$ si $L>0$, o constancia si $L=0$. Elegir allí un $b\ne0$ produce contradicción. La cota centrada de R3 sigue siendo válida y no equivale a esa cota de pares.

La barrera $|F(x)|\le x^2$ funciona para entradas racionales e irracionales y prueba el límite de secantes en cero. Fuera de cero la densidad entrega entradas de la clase opuesta con salida separada del valor central. Si hubiese una cota Lipschitz en una bola de cero, acreditaría continuidad en un punto no nulo interior de esa bola. Esa contradicción distingue control centrado de control de todos los pares vecinos.

## 18.15. Comparar sólo con el centro

[]{#MA-EX-ANM-01-018-015}

[]{#MA-SOL-ANM-01-018-015}

Con tolerancia $L/2$, la definición entrega un radio donde $q>L/2>0$ para argumentos perforados. La identidad $f(x)-f(a)=q(x)(x-a)$ da diferencia positiva para $x>a$ y negativa para $x<a$, dentro de ese radio y del dominio. No se exige que ambos lados tengan entradas; sólo se afirma la implicación cuando las hay. El centro está fijo: no se han comparado salidas de dos entradas arbitrarias diferentes de $a$, por lo que no se ha probado monotonía en toda una vecindad.

La positividad de las secantes se obtiene de un límite positivo con un presupuesto que conserva la mitad de su valor. Multiplicar por el incremento cambia el signo según el lado, sin exigir que ambos lados existan en el dominio. La conclusión compara sólo con $f(a)$. Para monotonía entre otros pares haría falta un argumento adicional que controle centros variables.

## 18.16. El producto como identidad

[]{#MA-EX-ANM-01-018-016}

[]{#MA-SOL-ANM-01-018-016}

[]{#MA-SEC-ANM-01-018-004}

En el dominio perforado común, $q_{\alpha f+\beta g}=\alpha q_f+\beta q_g$; límites finitos dan $\alpha f\prime(a)+\beta g\prime(a)$. Para producto, sumar y restar $f(a)g(x)$ da $q_{fg}=f(x)q_g+g(a)q_f$. La diferenciabilidad de $f$ da continuidad por R3, así el primer factor tiende a $f(a)$; los demás límites son los de los cocientes o la constante. El resultado es $f(a)g\prime(a)+g(a)f\prime(a)$. Sin ese paso no se habría justificado el límite del factor $f(x)$.

Cada identidad se verifica antes de pasar al límite y utiliza el mismo dominio perforado. En el producto aparece un valor variable, que necesita el límite proporcionado por continuidad desde derivabilidad. Las demás piezas son constantes o secantes con límite ya supuesto. Esa identificación de factores explica por qué la fórmula no es sólo manipulación formal de símbolos.

## 18.17. Dominio del recíproco

[]{#MA-EX-ANM-01-018-017}

[]{#MA-SOL-ANM-01-018-017}

Si $g(a)\ne0$, continuidad da una vecindad relativa donde $|g(x)|>|g(a)|/2$. Por tanto $E=\{g\ne0\}$ contiene esa vecindad y $a\in E$. Para cada radio, acumulación de $D$ da un testigo perforado dentro de su mínimo con el radio de la vecindad, así $a\in\operatorname{Acc}(E)$. En $E\setminus\{a\}$, $q_{1/g}=-q_g/[g(x)g(a)]$. El denominador tiende al no nulo $g(a)^2$; C13 prueba el límite $-g\prime(a)/g(a)^2$. El margen verifica tanto las divisiones como el dominio de la derivada.

La no anulación central proporciona por continuidad una ventana donde todas las divisiones son válidas. Esa ventana relativa también conserva acumulación al reducir cualquier radio propuesto. En ella los cocientes restringidos mantienen su límite original. El signo negativo y el cuadrado del denominador provienen directamente de la diferencia de recíprocos.

## 18.18. Un cociente racional

[]{#MA-EX-ANM-01-018-018}

[]{#MA-SOL-ANM-01-018-018}

El denominador es $x^2+1\ge1$, así el dominio es toda $\mathbb R$. Numerador y denominador tienen derivadas uno y $2a$. La regla da $f\prime(a)=[(a^2+1)-2a(a+1)]/(a^2+1)^2=(1-2a-a^2)/(a^2+1)^2$. Cada centro real es de acumulación y el denominador no se anula allí. La identidad se obtiene dentro de R4 sin regla de la cadena ni valor medio.

La desigualdad global del denominador acredita que ninguna entrada real queda excluida. La fórmula del cociente se aplica en un centro arbitrario y sus evaluaciones están definidas. Expandir el numerador reúne los términos en $1-2a-a^2$. La prueba conserva dominio y acumulación antes de presentar la expresión final de la derivada.

## 18.19. Un hueco no desaparece al cancelar

[]{#MA-EX-ANM-01-018-019}

[]{#MA-SOL-ANM-01-018-019}

La función original tiene dominio $\mathbb R\setminus\{1\}$; no tiene valor ni derivada en uno. En ese dominio coincide con $x+1$ y su derivada es uno en cada centro válido. La función $G:\mathbb R\to\mathbb R$, $G(x)=x+1$, es una extensión distinta que asigna $G(1)=2$ y sí tiene $G\prime(1)=1$. Cancelar permite igualdad de valores donde ambas expresiones están definidas, sin cambiar el dominio de la función original.

La identidad simplificada no modifica el conjunto de entradas del cociente original. En los centros válidos sus cocientes coinciden con los de la afín y tienen derivada uno. Para preguntar por uno hay que definir una extensión con una evaluación allí. La función afín completa ofrece esa extensión y su derivada se acredita como una propiedad del nuevo objeto.

## 18.20. Potencias enteras con base cero

[]{#MA-EX-ANM-01-018-020}

[]{#MA-SOL-ANM-01-018-020}

La base $n=1$ es la identidad, con derivada uno. Si la fórmula vale para $n\ge1$, producto de $x^n$ e identidad da $na^{n-1}a+a^n=(n+1)a^n$, también en cero; no hay exponentes negativos en esa igualdad. La potencia cero es constante uno, con derivada cero por su cociente, sin usar $0a^{-1}$. En el dominio sin cero, recíproco de $x^n$ da $-na^{n-1}/a^{2n}=-na^{-n-1}$. Cada división está legitimada por $a\ne0$.

La inducción para exponentes positivos se realiza con producto y nunca requiere invertir la base. El exponente cero se trata como una constante para evitar una expresión con potencia negativa en el origen. Las potencias negativas se declaran después en el dominio sin cero y usan recíprocos legitimados. Separar los casos conserva la fórmula correcta y las divisiones válidas.

## 18.21. Rellenar el factor exterior

[]{#MA-EX-ANM-01-018-021}

[]{#MA-SOL-ANM-01-018-021}

[]{#MA-SEC-ANM-01-018-005}

En $E\setminus\{b\}$ ponemos $A(y)=(f(y)-f(b))/(y-b)$ y en $b$ ponemos $A(b)=M=f\prime(b)$. Para cualquier tolerancia, los radios de derivabilidad controlan $|A(y)-M|$ fuera del centro; en él esa diferencia es cero, así $A$ es continua en $b$. Multiplicar la definición da $f(y)-f(b)=A(y)(y-b)$ para $y\ne b$, y en $b$ ambos lados valen cero. Es una nueva función con un valor declarado en el centro, no una división por cero.

Rellenar el factor exterior conserva el límite de sus secantes y añade el caso central con error cero. La identidad de incrementos vale entonces para todas las entradas exteriores, incluso $b$. Se obtiene una función continua útil para componer, sin afirmar que el cociente perforado original estuviera definido en su centro. Esta construcción repara el caso de incremento interior nulo.

## 18.22. Los dos presupuestos de la cadena

[]{#MA-EX-ANM-01-018-022}

[]{#MA-SOL-ANM-01-018-022}

Sea $L=g\prime(a)$, $M=f\prime(b)$ y $C=|L|+1$. La identidad de incrementos con $A$ da $q_{f\circ g}=A(g(x))q_g$ para todo $x\ne a$, incluidos los que satisfacen $g(x)=b$. Cerca del centro, $|q_g|<C$. Continuidad de $A$ en $b$ y de $g$ en $a$ entrega radio para error $|A(g(x))-M|<\varepsilon/(2C)$. Derivabilidad interior entrega otro para $|q_g-L|<\varepsilon/[2(|M|+1)]$. En el mínimo de estos radios y el de la cota, la diferencia respecto de $ML$ es a lo sumo $|A-M||q_g|+|M||q_g-L|<\varepsilon$. De este modo se prueba el límite sin dividir por $g(x)-b$.

La barrera positiva $C=|L|+1$ controla el factor interior variable. El primer presupuesto se divide por esa barrera y el segundo por $|M|+1$, evitando problemas si alguna derivada vale cero. El mínimo reúne los tres controles en una misma ventana. Cuando la salida interior es exactamente $b$, la identidad sigue siendo válida y no introduce una secante exterior indefinida.

## 18.23. Una rama detenida

[]{#MA-EX-ANM-01-018-023}

[]{#MA-SOL-ANM-01-018-023}

El cociente interior es cero a la izquierda y $x$ a la derecha, por lo que su magnitud es a lo sumo $|x|$ y $g\prime(0)=0$. La exterior $f(y)=y^2$ tiene derivada dos en uno. La cadena correcta da derivada cero. Directamente, el cociente compuesto es cero para $x<0$ y $2x+x^3$ para $x>0$, con límite cero. En cualquier argumento negativo, $g(x)-g(0)=0$, así el factor exterior habitual es una división $0/0$. Usar $A(1)=2$ mantiene la identidad: factor dos por cociente interior cero da cero.

**Retorno visual.** Véase [C18-F04](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La rama izquierda produce un incremento interior exactamente nulo en muchas entradas perforadas. La derecha produce un cociente que tiende a cero, compatible con la misma derivada interior. La exterior rellenada tiene valor dos en uno y multiplica correctamente el cero izquierdo. El cálculo compuesto directo confirma el límite sin descartar ninguna rama.

## 18.24. Acumulación perdida en la composición

[]{#MA-EX-ANM-01-018-024}

[]{#MA-SOL-ANM-01-018-024}

El dominio efectivo $T=\{x:x^2\le0\}$ es $\{0\}$. La interior tiene derivada cero en cero sobre la recta; la exterior tiene derivada relativa uno en cero sobre $E$, que acumula allí desde la izquierda. Pero cero no acumula en $T$, por lo que R1 no define una derivada de la composición sobre su dominio. Las acumulaciones de los dominios originales no garantizan la de la preimagen efectiva. La multiplicación formal de derivadas omite una hipótesis de la cadena.

La condición de entrada exterior se traduce en $x^2\le0$, cuya única solución real es cero. Así la composición sí tiene valor central, pero su dominio no aporta entradas perforadas. Las derivadas de los factores en sus propios dominios no reparan esa falta de acumulación. La multiplicación formal omite una premisa de la definición aplicada al objeto compuesto.

## 18.25. Interior constante y exterior no lineal

[]{#MA-EX-ANM-01-018-025}

[]{#MA-SOL-ANM-01-018-025}

La interior tiene cociente cero en todo su dominio perforado, así $g\prime(a)=0$. La composición es constante con valor $f(b)$ y también tiene derivada cero. La fórmula da $f\prime(b)\cdot0=0$. La imagen $g[D]=\{b\}$ no acumula en $b$; esto no impide usar la derivada exterior calculada en $E$, donde sí se exige acumulación. El factor $A$ puede evaluarse en $b$ y vale $f\prime(b)$ en todas las entradas compuestas.

La derivada exterior pertenece al dominio $E$ donde fue probada, aunque la interior sólo alcance un valor de él. El factor rellenado se evalúa siempre en ese mismo centro. El cociente interior y el compuesto valen cero en toda entrada perforada. La imagen singleton de la interior no necesita acumular para este argumento compatible de cadena.

## 18.26. Tres hipótesis, tres funciones

[]{#MA-EX-ANM-01-018-026}

[]{#MA-SOL-ANM-01-018-026}

[]{#MA-SEC-ANM-01-018-006}

Inyectividad construye un único antecedente por valor de la imagen y hace que $x\ne a$ produzca $f(x)\ne b$. Continuidad de $h$ en $b$ convierte aproximación de salidas en aproximación de antecedentes a $a$. La condición $L\ne0$ separa las pendientes originales de cero para invertirlas. Para cada $\rho>0$, continuidad de $f$ en $a$ da un radio con error menor que $\rho$; acumulación de $D$ entrega una entrada distinta del centro dentro de él. Su imagen pertenece a $H$, es distinta de $b$ y está a distancia menor que $\rho$. Esto prueba acumulación de la imagen sin seleccionar una sucesión.

La derivabilidad original aporta continuidad en $a$, necesaria para llevar entradas próximas a salidas próximas. La inyectividad protege la evitación del centro y construye la inversa. Su continuidad realiza el transporte contrario de proximidad, y la pendiente no nula protege la inversión de secantes. Nombrar cada función de las hipótesis evita confundir existencia de inversa con continuidad de ese retorno.

## 18.27. Secantes recíprocas del cuadrado

[]{#MA-EX-ANM-01-018-027}

[]{#MA-SOL-ANM-01-018-027}

La inyectividad del cuadrado en el dominio no negativo y C10 identifican la inversa con $h(y)=\sqrt y$. Se tiene $|h(y)-a|=|y-a^2|/(\sqrt y+a)\le|y-a^2|/a$, por lo que es continua en $b$. R6 con $L=2a\ne0$ da $h\prime(b)=1/(2a)$. Para $y=x^2\ne a^2$, con $x\ge0$, la pendiente inversa es $(x-a)/(x^2-a^2)=1/(x+a)$, recíproca de la pendiente original $x+a$. Ambas divisiones requieren $x\ne a$, asegurado por inyectividad.

**Retorno visual.** Véase [C18-F05](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La racionalización de la diferencia de raíces da una cota de continuidad porque $a>0$ mantiene el denominador al menos en $a$. El orden no negativo asegura inyectividad del cuadrado y una inversa legítima. Las secantes inversas son recíprocas de las originales, con denominadores no nulos. El límite original $2a$ permite finalmente invertir y obtener la derivada.

## 18.28. Un centro de pendiente cero

[]{#MA-EX-ANM-01-018-028}

[]{#MA-SOL-ANM-01-018-028}

Para $x>0$, la pendiente del cuadrado centrada en cero es $x\to0$. La pendiente de la raíz sobre $[0,\infty)$ es $1/\sqrt y$ para $y>0$. Dadas cota $B>0$ y escala $r>0$, se elige $0<y<\min(r,1/(B+1)^2)$ y se obtiene cociente mayor que $B$. Si hubiera límite finito, sus cocientes estarían acotados por $|L|+1$ en algún radio, contradicción. La inversa existe y es continua, pero no se satisface la hipótesis de pendiente original no nula.

El cuadrado tiene secantes relativas positivas que tienden a cero. Al invertirlas, las secantes de la raíz pueden superar cualquier número en cualquier ventana positiva. Un límite finito tendría una barrera local, por lo que ese crecimiento lo refuta. La existencia y continuidad de la inversa permanecen verdaderas; la premisa que falla es la pendiente original no nula.

## 18.29. Una inversa que salta

[]{#MA-EX-ANM-01-018-029}

[]{#MA-SOL-ANM-01-018-029}

Las imágenes son $[0,1)$ y $[1,2]$, disjuntas, y ambas ramas son inyectivas; la imagen total es $[0,2]$. En una bola de radio menor que uno centrada en dos sólo hay puntos de la segunda pieza y su cociente es uno, así $f\prime(2)=1$ relativamente a $D$. La inversa satisface $h(1)=2$, pero para $y_n=1-1/(n+2)$ se tiene $h(y_n)=y_n\to1$. Sus diferencias respecto de dos son mayores que uno mientras las entradas convergen a uno. No es continua allí y, por R3, no es derivable. Esto refuta que derivada original no nula e inyectividad hagan innecesaria continuidad de la inversa en dominios arbitrarios.

El dominio separado permite aislar la segunda regla cerca de dos y acreditar una secante constante uno. En la imagen las dos piezas se juntan en uno y las salidas inferiores recuperan entradas de la primera pieza. Esas entradas no se aproximan a dos, pese a que las salidas se aproximan a uno. El ejemplo muestra por qué continuidad inversa es una premisa independiente en R6.

## 18.30. Evitar una prueba circular

[]{#MA-EX-ANM-01-018-030}

[]{#MA-SOL-ANM-01-018-030}

La cadena sólo se aplica si la derivada interior existe, así el despeje presupone la conclusión. Se toma directamente un $y\ne b$ de la imagen y $x=h(y)\ne a$. La identidad de inversa da $q_h(y)=1/q_f(x)$. Continuidad de $h$ asegura $x\to a$; derivada original no nula entrega margen $|q_f|>|L|/2$. Entonces $|q_h-1/L|\le2|q_f-L|/|L|^2$, que se hace menor que cualquier tolerancia con los radios de derivabilidad y continuidad. Así se obtiene existencia antes de usar una regla que la exigiría.

La identidad $q_h=1/q_f$ se obtiene para entradas perforadas de la inversa sin presuponer que exista su límite. La continuidad de $h$ proporciona cercanía de antecedentes y la derivada original los controla. El margen de pendiente mantiene positivo el denominador de la estimación de error recíproco. Así se demuestra primero existencia de la derivada inversa y después su valor, evitando usar cadena circularmente.

## 18.31. El dominio de otra función

[]{#MA-EX-ANM-01-018-031}

[]{#MA-SOL-ANM-01-018-031}

[]{#MA-SEC-ANM-01-018-007}

En cada centro positivo hay una vecindad donde la función es la identidad y la derivada vale uno; en cada centro negativo hay una donde es menos la identidad y vale menos uno. En cero no existe derivada. Así su dominio es $\mathbb R\setminus\{0\}$. Cero acumula en ese dominio, por lo que puede preguntarse su límite; no existe por los dos valores laterales diferentes. No se habla de continuidad allí porque falta un valor de la función derivada en cero.

En los centros no nulos basta una ventana que no cruce cero para identificar la función con una regla afín. En cero las secantes originales impiden definir la derivada. La nueva función derivada tiene por ello dominio perforado y allí dos valores constantes. Un límite en cero es una pregunta válida de acumulación, mientras continuidad allí necesitaría una evaluación que falta.

## 18.32. Separar la familia de bultos

[]{#MA-EX-ANM-01-018-032}

[]{#MA-SOL-ANM-01-018-032}

Como $c_n\le1/2$, $w_n<c_n/2$, por lo que el intervalo es positivo y queda en $[c_n/2,3c_n/2]$. La distancia entre centros vecinos es $c_n/2$ y la suma de semianchos $w_n+w_{n+1}=5c_n^2/32<c_n/2$. Los intervalos quedan ordenados y separados, lo que implica disjunción de cualquier par. Si el punto $x>0$ está fijado, los centros de la cola y sus extremos quedan por debajo de $x/2$ desde algún índice, dejando sólo finitos intervalos posibles en una bola pequeña. Si $x<0$, una bola dentro de la semirrecta negativa no toca ninguno. Sólo en cero se acumula la familia.

La escala geométrica de centros hace que los semianchos disminuyan más rápido que su separación. La desigualdad entre vecinos establece un orden con huecos y separa todos los intervalos. Para finitud local basta eliminar una cola completa por debajo de un punto positivo fijado. El origen se distingue porque cualquier vecindad suya sigue encontrando intervalos de esa cola.

## 18.33. Una derivada discontinua sin trigonometría

[]{#MA-EX-ANM-01-018-033}

[]{#MA-SOL-ANM-01-018-033}

En cada intervalo, $0\le F\le w_n=c_n^2/8\le x^2/2$ porque $x\ge c_n/2$; fuera de ellos es cero. Así $|q_{F,0}|\le|x|/2$ y $F\prime(0)=0$. En interiores, reglas algebraicas y cadena dan $\phi\prime(u)=-4u(1-u^2)$. En un extremo $e$, la rama interior satisface $|F(x)|\le4|x-e|^2/w_n$, así su cociente tiende a cero; la exterior es cero. La finitud local permite aislar el intervalo o la zona exterior en todo punto no nulo. Por tanto $F$ es derivable en toda la recta. Los puntos $x_n=c_n+w_n/2\to0$ tienen derivada $\phi\prime(1/2)=-3/2$, así contradicen continuidad de $F\prime$ en cero con tolerancia uno. No se depende de representar gráficamente la cola infinita.

**Retorno visual.** Véase [C18-F06](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La cota cuadrática de valores resuelve el origen sin presuponer reglas de pegado infinito. En cada punto no nulo la finitud local reduce el análisis a una zona exterior, un interior o un extremo de bulto. Los extremos usan su propia cota de resto y los interiores las reglas ya probadas. La ruta con derivada menos tres medios refuta continuidad de la derivada mediante una precisión fija.

## 18.34. La forma del extremo

[]{#MA-EX-ANM-01-018-034}

[]{#MA-SOL-ANM-01-018-034}

En $[-1,1]$, $(1-u^2)^2=(1-u)^2(1+u)^2\le4(u-1)^2$ y también $\le4(u+1)^2$. Si $e=c_n+w_n$, entonces $u-1=(x-e)/w_n$, de donde $|F(x)|\le4|x-e|^2/w_n$. Como $F(e)=0$, el cociente centrado en $e$ tiene magnitud a lo sumo $4|x-e|/w_n$ en la rama interior y cero fuera. El radio $\eta w_n/4$, reducido para aislar el bulto, da error menor que $\eta$. El extremo izquierdo se trata con $u+1$ y el mismo presupuesto.

El factor que no se anula en el extremo tiene magnitud a lo sumo dos en $[-1,1]$. Elevarlo al cuadrado proporciona la constante cuatro, mientras el otro factor conserva la distancia cuadrática al extremo. El cambio de coordenadas introduce $w_n$ y transforma esa cota en un control de secante lineal en $|x-e|$. El radio se reduce además para excluir otros bultos.

## 18.35. Pendiente puntual y función derivada

[]{#MA-EX-ANM-01-018-035}

[]{#MA-SOL-ANM-01-018-035}

La primera es derivable en cero y discontinua en todo otro punto; por R3 no es derivable fuera de cero. Su dominio de derivada es exactamente $\{0\}$ y la función derivada allí vale cero. La familia de bultos es derivable en toda la recta, pero su derivada es discontinua en cero. Así fallan dos inferencias distintas: derivabilidad en un centro no garantiza derivabilidad en una vecindad, y derivabilidad en toda una vecindad no garantiza continuidad de la función derivada. La derivada sobre un singleton es continua relativamente a él, aunque ese hecho no la extienda al entorno.

La primera función sólo admite derivada en cero porque en todos los otros puntos falla continuidad. Su derivada en dominio singleton es continua relativamente, pero no ofrece valores vecinos. La segunda admite derivada en todo el dominio real y aun así su función derivada falla continuidad en cero. Estos ejemplos refutan dos implicaciones diferentes y deben leerse con sus dominios propios.

## 18.36. Racionalizar el error de raíz

[]{#MA-EX-ANM-01-018-036}

[]{#MA-SOL-ANM-01-018-036}

[]{#MA-SEC-ANM-01-018-008}

Con $s=\sqrt{1+h}\ge0$, $s-1=h/(s+1)$. Entonces $s-1-h/2=h(1-s)/[2(s+1)]=-h^2/[2(s+1)^2]$. El denominador es positivo. Para $|h|\le1/2$ sigue siendo al menos dos, así el error tiene magnitud a lo sumo $h^2/2$. La identidad incluye $h=0$ sin dividir por $h$ y prueba además que el modelo afín está por encima del valor exacto. Se obtuvo por álgebra y raíces C10, sin Taylor.

**Retorno visual.** Véase [C18-F07](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La condición $h>-1$ asegura definición real de la raíz y el denominador $s+1$ es siempre positivo. La racionalización obtiene una identidad de resto, no sólo un límite. Su signo acredita sobreestimación y su magnitud da una cota cuadrática en la vecindad indicada. La identidad incluye el incremento cero sin dividir por él.

## 18.37. Un valor y dos tolerancias

[]{#MA-EX-ANM-01-018-037}

[]{#MA-SOL-ANM-01-018-037}

El incremento es $h=1/100$ y R8 da $0\le201/200-\sqrt{101/100}\le h^2/2=1/20000$. El error de la pendiente secante respecto de $1/2$ es el resto dividido por $h$, con magnitud a lo sumo $1/200$. No son la misma tolerancia: multiplicar el error de pendiente por la magnitud del incremento produce el error del valor. Ambos son certificados para esta entrada admisible, derivados de una identidad que controla toda la vecindad, sin tomar la cifra visual del gráfico como evidencia.

**Retorno visual.** Véase [C18-F07](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html#fig-anm-c18-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El incremento utilizado pertenece a la región donde se demostró la cota de resto. La aproximación y ambas cotas se expresan con fracciones exactas. Dividir el error de valor por $|h|=1/100$ lo amplifica cien veces para obtener el error de secante. La distinción explica por qué las dos tolerancias numéricas son distintas aunque procedan del mismo certificado.

## 18.38. Tolerancias desde una cota dada

[]{#MA-EX-ANM-01-018-038}

[]{#MA-SOL-ANM-01-018-038}

Si $B>0$, basta $|h|<\min(\rho,\sqrt{\varepsilon/B})$ para tener $Bh^2<\varepsilon$. Para el cociente con $h\ne0$, basta $|h|<\min(\rho,\eta/B)$, porque $|r/h|\le B|h|<\eta$. En $h=0$ el error del valor es cero; no se evalúa el cociente. Si $B=0$, el resto es cero en toda la vecindad admisible y cualquier incremento de ella da valor exacto, mientras todas sus secantes perforadas tienen pendiente exactamente $L$.

Cada mínimo conserva la vecindad donde se sabe que la cota vale y añade la escala que responde al desafío. Para $B>0$ el error cuadrático se ajusta con una raíz y el normalizado con un radio lineal. El centro sólo participa en la primera pregunta y tiene resto cero. Cuando $B=0$, se trata directamente la igualdad de valores y secantes antes de introducir cualquier división por la barrera.

## 18.39. Un resto menor que lineal y mayor que cuadrático

[]{#MA-EX-ANM-01-018-039}

[]{#MA-SOL-ANM-01-018-039}

El cociente tiene magnitud $\sqrt{|x|}$, de modo que $\delta=\eta^2$ prueba derivada cero. Si una cota $|f(x)|\le Bx^2$ con $B>0$ valiera en una vecindad perforada, dividir por $x^2$ daría $1/\sqrt{|x|}\le B$. Elegir allí $0<|x|<1/(B+1)^2$ lo contradice. Para $B=0$ cualquier entrada no nula ya contradice la cota. La derivada sólo exige resto de orden menor que lineal; no impone una tasa cuadrática. La expresión usa producto y raíz, sin regla general de potencias fraccionarias.

El resto es todo el valor de la función porque el centro y la pendiente propuestos son cero. Su cociente normalizado tiende a cero y acredita el modelo de primer orden. Al compararlo con $x^2$, la razón crece sin cota y permite infringir cualquier barrera finita dentro de cualquier radio. La ausencia de tasa cuadrática no contradice la derivada ya demostrada.

## 18.40. Muestras idénticas, pendientes arbitrarias

[]{#MA-EX-ANM-01-018-040}

[]{#MA-SOL-ANM-01-018-040}

Sea $p_c(x)=cx\prod_{s\in S\setminus\{0\}}(x-s)/(-s)$, con producto vacío igual a uno. Todos los denominadores son no nulos. En cero se anula por el factor $x$; en cada otro nodo se anula por su factor correspondiente. En $x\ne0$, el cociente centrado en cero es $c\prod_s(x-s)/(-s)$, que tiende a $c$ porque cada factor tiende a uno y sólo hay finitos. Por tanto $p_c\prime(0)=c$, incluso si $c=0$ o no hay otros nodos. La misma tabla de ceros es compatible con toda pendiente prescrita. Las muestras no determinan un control de todas las entradas cercanas y no sustituyen la condición de derivabilidad.

Los factores se construyen sólo para nodos no nulos, por lo que todos sus divisores están definidos. Cada nodo tiene un factor de anulación y cero tiene el factor inicial $x$. El cociente central conserva un producto finito de factores con límite uno, haciendo posible cualquier pendiente $c$. La tabla fija valores, pero no controla todas las entradas perforadas próximas que exige el certificado de derivada.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)
