---
content-id: MA-BCH-0249
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-011-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 11
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C11_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §11.1 — De los términos a las sumas parciales

### Microcontrol 001

[]{#MA-MIC-ANM-01-011-001}

[]{#MA-MSOL-ANM-01-011-001}

[]{#MA-SEC-ANM-01-011-001}

**Pregunta.** ¿Cuántos términos contiene $s_n=\sum_{k=0}^n a_k$?

**Solución.** $n+1$, porque los índices van de cero a $n$ inclusive.

Escribamos los primeros casos: $s_0=a_0$ contiene un término, $s_1=a_0+a_1$ contiene dos y $s_2$ contiene tres. En general, contar los enteros desde cero hasta $n$ da $n-0+1=n+1$. El índice final identifica el último término incluido, no el número de sumandos. Esta diferencia importa al calcular un resto: lo que queda después de $s_n$ comienza en $a_{n+1}$.

### Microcontrol 002

[]{#MA-MIC-ANM-01-011-002}

[]{#MA-MSOL-ANM-01-011-002}

**Pregunta.** ¿Cuál es el término inicial de $\operatorname{PS}(a)$?

**Solución.** $s_0=a_0$; no es automáticamente cero.

La definición $s_n=\sum_{k=0}^n a_k$ se aplica también cuando $n=0$: el único índice permitido es cero. Por tanto, el primer total ya incorpora el primer aporte. El total vacío sería cero, pero corresponde a no incorporar ningún término; no es $s_0$ en esta convención. Por ejemplo, para $a_n=1/(n+1)$ tenemos $s_0=1$, lo que permite detectar inmediatamente un desplazamiento incorrecto de los índices.

### Microcontrol 003

[]{#MA-MIC-ANM-01-011-003}

[]{#MA-MSOL-ANM-01-011-003}

**Pregunta.** ¿Qué condición permite llamar suma real a $\sum_{n=0}^{\infty}a_n$?

**Solución.** Que la sucesión de sumas parciales converja a un real $S$; entonces el símbolo de suma designa ese límite único.

Primero construimos cada $s_n$ mediante una suma finita, sin asumir que exista una suma infinita. Después debemos demostrar que hay $S\in\mathbb R$ tal que, para cada $\varepsilon>0$, existe $N$ con $|s_n-S|<\varepsilon$ para todos los $n\ge N$. Sólo entonces definimos la suma de la serie como $S$. La unicidad del límite garantiza que la notación designa un único número y no depende de cuál prueba de convergencia utilicemos.

### Microcontrol 004

[]{#MA-MIC-ANM-01-011-004}

[]{#MA-MSOL-ANM-01-011-004}

**Pregunta.** ¿Cómo se recupera $a_{n+1}$ a partir de dos totales?

**Solución.** $a_{n+1}=s_{n+1}-s_n$, por la recursión.

Los totales consecutivos comparten todos los aportes iniciales:
$$s_{n+1}=a_0+\cdots+a_n+a_{n+1},\qquad s_n=a_0+\cdots+a_n.$$
Al restar, esos términos comunes se cancelan y permanece exactamente el aporte nuevo. Para recuperar toda la sucesión hay que añadir el caso inicial $a_0=s_0$; la regla de diferencias recupera los términos desde $a_1$ en adelante. Conocer todos los totales permite así reconstruir todos los aportes.

### Microcontrol 005

[]{#MA-MIC-ANM-01-011-005}

[]{#MA-MSOL-ANM-01-011-005}

**Pregunta.** ¿Tener la misma suma implica tener los mismos términos?

**Solución.** No. $(1,0,0,\ldots)$ y $(1/2,1/2,0,\ldots)$ tienen suma uno y distintos términos y procesos.

Para la primera sucesión, todos los totales son uno. Para la segunda, el primer total es $1/2$ y todos los siguientes son uno. Las dos sucesiones de totales convergen al mismo número, aunque sus primeros valores y sus términos sean diferentes. La operación de tomar el límite conserva el destino y puede perder información del recorrido. No hay contradicción con la recuperación por diferencias: ésta exige conocer todos los totales, no únicamente su límite.

### Microcontrol 006

[]{#MA-MIC-ANM-01-011-006}

[]{#MA-MSOL-ANM-01-011-006}

**Pregunta.** ¿Qué totales produce $a_n=(-1)^n$?

**Solución.** $s_{2k}=1$ y $s_{2k+1}=0$, al cancelar parejas consecutivas.

Cada pareja de aportes consecutivos vale $1+(-1)=0$. El total $s_{2k+1}$ comprende $2k+2$ términos, que forman $k+1$ parejas completas; por eso vale cero. El total $s_{2k}$ comprende $2k+1$ términos: después de cancelar $k$ parejas queda un aporte igual a uno. La distinción entre índices pares e impares deriva del número de términos incluidos y permite comprobar la fórmula también en $s_0=1$.

### Microcontrol 007

[]{#MA-MIC-ANM-01-011-007}

[]{#MA-MSOL-ANM-01-011-007}

**Pregunta.** ¿La acotación de esos totales garantiza convergencia?

**Solución.** No. Después de cualquier corte hay totales separados por uno, de modo que falla Cauchy.

Todos los totales pertenecen a $\{0,1\}$, así que están acotados. Sin embargo, fijemos $\varepsilon_0=1/2$. Después de cualquier corte $N$ podemos escoger un índice par y otro impar; sus totales difieren en uno, mayor que esa tolerancia. Ninguna cola satisface la condición de Cauchy y, en consecuencia, los totales no convergen. Acotación limita el tamaño de los valores; convergencia exige además que sus separaciones se hagan arbitrariamente pequeñas.

### Microcontrol 008

[]{#MA-MIC-ANM-01-011-008}

[]{#MA-MSOL-ANM-01-011-008}

**Pregunta.** ¿Son $a$, $\operatorname{PS}(a)$ y su suma el mismo tipo de objeto?

**Solución.** No. $a$ y $\operatorname{PS}(a)$ son funciones $\mathbb N\to\mathbb R$ con papeles diferentes; su suma, si existe, es un número real.

La sucesión $a$ registra aportes individuales, mientras $\operatorname{PS}(a)$ registra lo acumulado hasta cada índice. Ambas tienen infinitos valores organizados por $n$. En cambio, si los acumulados convergen, su suma es un solo real $S$. Por ejemplo, para $a=(1,0,0,\ldots)$, los aportes cambian al inicio, los totales son constantemente uno y la suma es el número uno. Distinguir esos objetos evita aplicar a los aportes una propiedad que sólo se ha demostrado para los totales.

## §11.2 — Cauchy mide bloques completos

### Microcontrol 009

[]{#MA-MIC-ANM-01-011-009}

[]{#MA-MSOL-ANM-01-011-009}

[]{#MA-SEC-ANM-01-011-002}

**Pregunta.** ¿Por qué el bloque $s_p-s_q$ empieza en $q+1$?

**Solución.** Porque $s_q$ ya contiene $a_q$; los nuevos términos son $a_{q+1},\ldots,a_p$.

Escribimos ambas sumas antes de restarlas: $s_p=a_0+\cdots+a_q+a_{q+1}+\cdots+a_p$ y $s_q=a_0+\cdots+a_q$. El prefijo hasta $q$, incluido ese índice, desaparece. Queda $\sum_{k=q+1}^p a_k$, que tiene $p-q$ términos. Si el bloque empezara en $q$, contaríamos otra vez un aporte que ya formaba parte del total anterior. La identidad sólo involucra sumas finitas y no requiere convergencia.

### Microcontrol 010

[]{#MA-MIC-ANM-01-011-010}

[]{#MA-MSOL-ANM-01-011-010}

**Pregunta.** ¿En qué orden se eligen tolerancia, corte y extremos de bloque?

**Solución.** Primero $\varepsilon>0$, después un único $N$ que puede depender de ella, y luego todos $p>q\ge N$.

El criterio dice que, recibida una precisión, debe existir una cola en la que cualquier bloque tenga suma de valor absoluto menor que esa precisión. El corte se fija antes de escoger dónde termina el bloque. Puede depender de $\varepsilon$ y de la serie, pero debe servir para todos los $p>q\ge N$. Este orden es exactamente el que convierte el control de bloques en la condición de Cauchy de los totales.

### Microcontrol 011

[]{#MA-MIC-ANM-01-011-011}

[]{#MA-MSOL-ANM-01-011-011}

**Pregunta.** ¿Puede el corte depender de la longitud del bloque?

**Solución.** No en el criterio: debe controlar simultáneamente todas las longitudes.

Si para cada longitud se permitiera escoger un corte distinto, sólo controlaríamos por separado bloques de tamaño fijo. Eso es más débil. En la armónica, un bloque de longitud $L$ situado después de $q$ tiene suma a lo sumo $L/(q+2)$ y se hace pequeño con $q$ para cada $L$ fijo. Aun así, bloques cuya longitud crece con su posición pueden conservar una suma al menos $1/2$. El criterio exige un control simultáneo de esas longitudes arbitrarias.

### Microcontrol 012

[]{#MA-MIC-ANM-01-011-012}

[]{#MA-MSOL-ANM-01-011-012}

**Pregunta.** ¿Cómo se cubre el caso $p=q$ al recuperar Cauchy?

**Solución.** La distancia entre el mismo total y sí mismo es cero, menor que cualquier tolerancia positiva.

El criterio de bloques se enuncia para $p>q$. Para comprobar Cauchy con cualquier par tardío, quedan dos casos: si $p=q$, $|s_p-s_q|=0<\varepsilon$; si $p<q$, intercambiamos los extremos y usamos $|s_p-s_q|=|s_q-s_p|$. Así los casos no incluidos literalmente en el criterio se reducen a una identidad trivial o a la simetría. No hacen falta nuevos cortes ni nuevas hipótesis.

### Microcontrol 013

[]{#MA-MIC-ANM-01-011-013}

[]{#MA-MSOL-ANM-01-011-013}

**Pregunta.** ¿Dónde se usa completitud en el criterio de bloques?

**Solución.** En pasar de Cauchy de $s$ a existencia de un límite real, mediante C10; no en la identidad de sumas finitas.

La identidad $s_p-s_q=\sum_{k=q+1}^p a_k$ traduce una condición sobre bloques en una condición sobre distancias entre totales. Esa traducción es puramente algebraica. Una vez probado que $(s_n)$ es de Cauchy, usamos la completitud de $\mathbb R$ para obtener un límite dentro del mismo espacio. En un espacio incompleto, el control de pares seguiría teniendo sentido, pero no aseguraría que su destino exista en ese espacio.

### Microcontrol 014

[]{#MA-MIC-ANM-01-011-014}

[]{#MA-MSOL-ANM-01-011-014}

**Pregunta.** ¿Por qué convergencia de la serie implica $a_n\to0$?

**Solución.** Para $n\ge N+1$, el bloque de un término entre $n-1$ y $n$ da $|a_n|<\varepsilon$.

Dada $\varepsilon>0$, el criterio proporciona un corte $N$ válido para todos los bloques tardíos. Para $n\ge N+1$ escogemos $q=n-1$ y $p=n$, de modo que $q\ge N$. El bloque contiene únicamente $a_n$, luego $|a_n|=|s_n-s_{n-1}|<\varepsilon$. Hemos obtenido un corte para los términos, posiblemente desplazado en una unidad. Esto prueba una condición necesaria; no demuestra que el control de un solo aporte baste para todos los bloques.

### Microcontrol 015

[]{#MA-MIC-ANM-01-011-015}

[]{#MA-MSOL-ANM-01-011-015}

**Pregunta.** ¿Qué pares de cortes niegan Cauchy en la armónica?

**Solución.** Para cualquier $N$, tomar $m=N+1$, $q=m-1$ y $p=2m-1$ da una diferencia al menos $1/2$.

En la armónica indexada desde cero, $s_n=\sum_{k=0}^n1/(k+1)$. Los índices elegidos dan
$$s_{2m-1}-s_{m-1}=\sum_{j=m+1}^{2m}\frac1j\ge m\frac1{2m}=\frac12.$$
Hay exactamente $m$ sumandos y cada uno es al menos $1/(2m)$. Con $m=N+1$, ambos extremos están después del corte propuesto. La misma tolerancia $1/2$ falla para cualquier $N$, lo que verifica la negación de Cauchy con testigos explícitos.

### Microcontrol 016

[]{#MA-MIC-ANM-01-011-016}

[]{#MA-MSOL-ANM-01-011-016}

**Pregunta.** ¿El término nulo es una condición suficiente?

**Solución.** No. $1/(n+1)\to0$, pero sus bloques largos anteriores mantienen suma al menos $1/2$ después de cada corte.

Que los términos tiendan a cero sólo hace pequeños los bloques de un término. En la armónica, cada aporte $1/(n+1)$ tiende a cero, pero los bloques entre $m+1$ y $2m$ reúnen suficientes aportes para sumar al menos $1/2$. Por eso la condición necesaria no se puede invertir. Conviene comprobar primero el término nulo: si falla, la serie diverge; si se cumple, aún debemos encontrar otro argumento que controle la acumulación.

## §11.3 — Fórmulas finitas y restos exactos

### Microcontrol 017

[]{#MA-MIC-ANM-01-011-017}

[]{#MA-MSOL-ANM-01-011-017}

[]{#MA-SEC-ANM-01-011-003}

**Pregunta.** ¿Qué total produce $a_n=c_n-c_{n+1}$?

**Solución.** $s_n=c_0-c_{n+1}$ por cancelación finita, demostrable por inducción.

La suma finita es $(c_0-c_1)+(c_1-c_2)+\cdots+(c_n-c_{n+1})$. Cada término interior aparece una vez con signo positivo y otra con signo negativo. Sólo sobreviven $c_0$ y $-c_{n+1}$. También podemos verificarlo por inducción: para $n=0$ es la definición; al añadir $c_{n+1}-c_{n+2}$ a $c_0-c_{n+1}$ obtenemos $c_0-c_{n+2}$. La cancelación ocurre antes de tomar cualquier límite.

### Microcontrol 018

[]{#MA-MIC-ANM-01-011-018}

[]{#MA-MSOL-ANM-01-011-018}

**Pregunta.** ¿Cuál es el resto telescópico si $c_n\to C$?

**Solución.** La suma es $c_0-C$ y $R_n=c_{n+1}-C$.

De la identidad finita $s_n=c_0-c_{n+1}$ y de $c_{n+1}\to C$ obtenemos $s_n\to c_0-C$. Definido $S=c_0-C$, restamos el total conocido:
$$R_n=S-s_n=(c_0-C)-(c_0-c_{n+1})=c_{n+1}-C.$$
El resto conserva el signo de esa diferencia y su magnitud es $|c_{n+1}-C|$. La fórmula no presupone que $c_n$ sea positivo ni que se aproxime a $C$ desde un lado determinado.

### Microcontrol 019

[]{#MA-MIC-ANM-01-011-019}

[]{#MA-MSOL-ANM-01-011-019}

**Pregunta.** ¿Cuál es la suma de $1/((n+1)(n+2))$?

**Solución.** Uno: $s_n=1-1/(n+2)\to1$.

Descomponemos cada aporte mediante
$$\frac1{(n+1)(n+2)}=\frac1{n+1}-\frac1{n+2}.$$
Es una telescópica con $c_n=1/(n+1)$, $c_0=1$ y $c_n\to0$. La suma parcial vale $1-1/(n+2)$, de modo que la suma es uno y el resto exacto es $1/(n+2)$. Para garantizar error menor que $\varepsilon$, basta escoger un índice con $n+2>1/\varepsilon$. Así la identidad da tanto el destino como un certificado de aproximación.

### Microcontrol 020

[]{#MA-MIC-ANM-01-011-020}

[]{#MA-MSOL-ANM-01-011-020}

**Pregunta.** ¿Qué identidad geométrica es válida antes de cualquier límite?

**Solución.** $(1-r)\sum_{k=0}^nr^k=1-r^{n+1}$, para todo real $r$ y natural $n$.

Si $G_n=1+r+\cdots+r^n$, entonces $rG_n=r+r^2+\cdots+r^{n+1}$. Restar estas dos sumas cancela todos los términos interiores y da $G_n-rG_n=1-r^{n+1}$. La identidad vale incluso para $r=1$, donde ambos miembros son cero. Lo que requiere $r\ne1$ es el paso adicional de dividir por $1-r$. Separar identidad y división evita atribuir a una fórmula condiciones que pertenecen sólo a un paso posterior.

### Microcontrol 021

[]{#MA-MIC-ANM-01-011-021}

[]{#MA-MSOL-ANM-01-011-021}

**Pregunta.** ¿Para qué razones reales converge la geométrica?

**Solución.** Exactamente para $|r|<1$; fuera de ese intervalo los términos no tienden a cero.

Si $|r|<1$, las potencias $r^{n+1}$ tienden a cero y la fórmula finita da $s_n=(1-r^{n+1})/(1-r)\to1/(1-r)$. Si $|r|\ge1$, en cambio, $|r^n|\ge1$ para todos los índices, de modo que los aportes no tienden a cero. La condición necesaria ya excluye la convergencia. Esto incluye los dos extremos: $r=1$ acumula unos y $r=-1$ produce totales alternados.

### Microcontrol 022

[]{#MA-MIC-ANM-01-011-022}

[]{#MA-MSOL-ANM-01-011-022}

**Pregunta.** ¿Qué ocurre con la geométrica de razón cero?

**Solución.** Con $r^0=1$, sus términos son uno y luego ceros, así que su suma es uno.

La convención de potencias fija $r^0=1$ para cualquier base de esta serie; para la razón cero, todos los términos con exponente positivo son cero. Por eso $s_n=1$ para cada $n$, y no hay error al aproximar su suma con ningún total. El caso merece comprobarse directamente porque algunas estimaciones posteriores usan cocientes o logaritmos que no tienen sentido con base cero, aunque la serie misma sea perfectamente válida.

### Microcontrol 023

[]{#MA-MIC-ANM-01-011-023}

[]{#MA-MSOL-ANM-01-011-023}

**Pregunta.** ¿Cuál es el resto exacto cuando $|r|<1$?

**Solución.** $R_n=r^{n+1}/(1-r)$, después de probar $S=1/(1-r)$.

Primero obtenemos el límite $S=1/(1-r)$ usando $|r|<1$. Después restamos la fórmula del total:
$$S-s_n=\frac1{1-r}-\frac{1-r^{n+1}}{1-r}=\frac{r^{n+1}}{1-r}.$$
Por tanto $|R_n|=|r|^{n+1}/|1-r|$. Como $1-r>0$ en el intervalo considerado, el signo del resto es el de $r^{n+1}$; para una razón negativa puede alternar. No conviene sustituir sin justificación el resto firmado por su magnitud.

### Microcontrol 024

[]{#MA-MIC-ANM-01-011-024}

[]{#MA-MSOL-ANM-01-011-024}

**Pregunta.** ¿Es correcto dividir por $1-r$ para estudiar $r=1$?

**Solución.** No. Para $r=1$, $s_n=n+1$ y la condición del término nulo ya descarta convergencia.

Cuando $r=1$, el denominador $1-r$ es cero, por lo que la fórmula obtenida mediante división no puede usarse. El cálculo directo resulta sencillo: se suman $n+1$ aportes iguales a uno y $s_n=n+1$. Además, la sucesión de aportes es constantemente uno y no tiende a cero. Cualquiera de esos argumentos excluye una suma real finita; la identidad sin dividir permanece válida, pero sólo expresa $0=0$.

## §11.4 — Acumulación positiva y barreras

### Microcontrol 025

[]{#MA-MIC-ANM-01-011-025}

[]{#MA-MSOL-ANM-01-011-025}

[]{#MA-SEC-ANM-01-011-004}

**Pregunta.** ¿Qué hipótesis hace crecientes las sumas parciales?

**Solución.** $a_n\ge0$: el incremento $s_{n+1}-s_n=a_{n+1}$ es no negativo.

Para todo $n$, el paso de $s_n$ a $s_{n+1}$ añade exactamente $a_{n+1}$. Si ese aporte es no negativo, el nuevo total no puede ser menor que el anterior. Se obtiene $s_n\le s_{n+1}$, que significa crecimiento en sentido no estricto: un aporte cero puede dejar el total igual. La hipótesis para todos los términos es la formulación habitual de una serie no negativa; el aporte inicial fija el punto de partida.

### Microcontrol 026

[]{#MA-MIC-ANM-01-011-026}

[]{#MA-MSOL-ANM-01-011-026}

**Pregunta.** ¿Qué cota basta para una serie no negativa?

**Solución.** Una cota superior real común a todas sus sumas parciales.

No necesitamos conocer la suma ni encontrar una cota óptima. Basta exhibir un real $B$ con $s_n\le B$ para cada $n$. Los aportes no negativos hacen creciente la sucesión de totales, y el teorema de convergencia monótona garantiza entonces un límite real. La cota debe controlar los acumulados: acotar cada aporte por separado no basta, como muestra la serie de unos, cuyos términos están acotados y cuyos totales crecen sin límite.

### Microcontrol 027

[]{#MA-MIC-ANM-01-011-027}

[]{#MA-MSOL-ANM-01-011-027}

**Pregunta.** ¿Qué conjunto se usa para construir el destino por supremo?

**Solución.** $\{s_n:n\in\mathbb N\}$, no vacío y acotado superiormente.

Tomamos el conjunto de valores efectivamente alcanzados por los totales. Contiene $s_0$, así que no es vacío; la cota común $B$ garantiza que está acotado superiormente. La completitud permite definir $S=\sup\{s_n:n\in\mathbb N\}$. Elegir el conjunto de aportes $\{a_n\}$ respondería a otra pregunta: su supremo controla el tamaño individual, no lo acumulado. El destino se construye como la menor barrera de los totales.

### Microcontrol 028

[]{#MA-MIC-ANM-01-011-028}

[]{#MA-MSOL-ANM-01-011-028}

**Pregunta.** ¿Cómo se encuentra un total cercano por debajo del supremo?

**Solución.** $S-\varepsilon$ no es cota superior, por lo que existe $N$ con $s_N>S-\varepsilon$.

Como $\varepsilon>0$, tenemos $S-\varepsilon<S$. Si todos los totales fueran menores o iguales que $S-\varepsilon$, éste sería una cota superior más pequeña que el supremo, contradicción. Por eso algún total $s_N$ supera esa barrera. A la vez $s_N\le S$, pues $S$ sí es cota superior. Obtenemos así un primer total dentro de la franja $(S-\varepsilon,S]$, sin asumir previamente la convergencia.

### Microcontrol 029

[]{#MA-MIC-ANM-01-011-029}

[]{#MA-MSOL-ANM-01-011-029}

**Pregunta.** ¿Por qué todos los totales posteriores siguen cerca?

**Solución.** La no negatividad da $s_N\le s_n\le S$ para $n\ge N$.

La monotonía garantiza que, una vez alcanzada la franja, los totales posteriores no retroceden: $s_n\ge s_N>S-\varepsilon$. La propiedad de cota superior impide que sobrepasen $S$. Combinando ambas,
$$S-\varepsilon<s_n\le S\quad(n\ge N),$$
de donde $|S-s_n|=S-s_n<\varepsilon$. La prueba necesita los dos controles: acercarse una vez a la barrera no bastaría si luego los totales pudieran volver a alejarse.

### Microcontrol 030

[]{#MA-MIC-ANM-01-011-030}

[]{#MA-MSOL-ANM-01-011-030}

**Pregunta.** ¿Qué conclusión da $0\le a_n\le b_n$ si la serie de $b$ converge?

**Solución.** La serie de $a$ converge y $0\le S_a\le S_b$ si la comparación vale desde el inicio.

Sumando la comparación término a término obtenemos $0\le s_n^a\le s_n^b$. Como la serie de $b$ tiene aportes no negativos y converge a $S_b$, todos sus totales son menores o iguales que $S_b$. Ésta es una cota común para los totales de $a$, que también son crecientes. Por convergencia monótona existe $S_a$; al pasar al límite en las desigualdades queda $0\le S_a\le S_b$.

### Microcontrol 031

[]{#MA-MIC-ANM-01-011-031}

[]{#MA-MSOL-ANM-01-011-031}

**Pregunta.** ¿Una comparación eventual conserva automáticamente el orden de sumas completas?

**Solución.** No. Los prefijos pueden modificar esas sumas; la comparación garantiza convergencia de las colas.

La comparación de colas no controla lo añadido antes del corte. Por ejemplo, $a=(100,0,0,\ldots)$ y $b=(0,0,0,\ldots)$ cumplen $0\le a_n\le b_n$ para $n\ge1$, pero sus sumas son cien y cero. Ambas convergen, aunque el orden de las sumas completas se invierte. El argumento eventual permite demostrar convergencia de las colas y luego añadir un prefijo finito; para comparar sumas completas hay que incluir explícitamente ese prefijo.

### Microcontrol 032

[]{#MA-MIC-ANM-01-011-032}

[]{#MA-MSOL-ANM-01-011-032}

**Pregunta.** ¿Qué resto garantiza la comparación para $a_n=1/(n+2)^2$?

**Solución.** $0\le S_a-s_n\le1/(n+2)$, comparando el bloque posterior con la serie telescópica.

Para $k\ge0$ tenemos $1/(k+2)^2\le1/((k+1)(k+2))$. Si $p>n$, al sumar sólo el bloque posterior resulta
$$0\le s_p-s_n\le\sum_{k=n+1}^p\left(\frac1{k+1}-\frac1{k+2}\right)=\frac1{n+2}-\frac1{p+2}.$$
La comparación prueba primero la convergencia de la serie no negativa. Después dejamos $p\to\infty$ y obtenemos la cota del resto $0\le S_a-s_n\le1/(n+2)$. La cota no afirma un valor exacto de la suma.

## §11.5 — Control absoluto de la acumulación

### Microcontrol 033

[]{#MA-MIC-ANM-01-011-033}

[]{#MA-MSOL-ANM-01-011-033}

[]{#MA-SEC-ANM-01-011-005}

**Pregunta.** ¿Qué significa convergencia absoluta?

**Solución.** Que converge la serie de términos $|a_n|$.

Construimos los nuevos totales $u_n=\sum_{k=0}^n|a_k|$. Convergencia absoluta significa que esos totales tienen un límite real finito $A$. No significa simplemente que los aportes estén acotados ni que $|a_n|\to0$. Al sustituir cada aporte por su magnitud desaparecen las cancelaciones de signos; el criterio exige que incluso esa acumulación sin compensaciones permanezca controlada. Por eso proporciona un control más fuerte que la convergencia de la serie original.

### Microcontrol 034

[]{#MA-MIC-ANM-01-011-034}

[]{#MA-MSOL-ANM-01-011-034}

**Pregunta.** ¿Qué condición adicional exige llamar condicional a una convergencia?

**Solución.** La original converge, mientras la serie de magnitudes diverge.

Hay dos obligaciones distintas: probar que los totales originales convergen y probar que los totales de magnitudes no convergen a un real finito. No basta demostrar la segunda, porque la serie original podría divergir también. La armónica alternada cumple ambas: el criterio de alternancia proporciona una suma, mientras sus magnitudes forman la armónica divergente. Si convergen las magnitudes, la convergencia es absoluta; si sólo converge la original, es condicional.

### Microcontrol 035

[]{#MA-MIC-ANM-01-011-035}

[]{#MA-MSOL-ANM-01-011-035}

**Pregunta.** ¿Qué desigualdad domina un bloque con signos?

**Solución.** $|\sum_{k=q+1}^pa_k|\le\sum_{k=q+1}^p|a_k|$ por triangular finita.

La desigualdad triangular para dos sumandos se extiende por inducción a cualquier suma finita: al incorporar un aporte nuevo, $|B+a_k|\le|B|+|a_k|$. Aplicándola al bloque completo obtenemos la cota por su suma de magnitudes. El lado izquierdo permite cancelaciones; el derecho mide todo lo acumulado sin cancelarlas. Ésta es una estimación válida antes de conocer la existencia de cualquiera de las dos sumas infinitas.

### Microcontrol 036

[]{#MA-MIC-ANM-01-011-036}

[]{#MA-MSOL-ANM-01-011-036}

**Pregunta.** ¿Por qué un corte para las magnitudes sirve para la original?

**Solución.** La suma del bloque de magnitudes es no negativa y domina la distancia de los totales originales; el mismo corte prueba Cauchy.

La convergencia de $u_n=\sum_{k=0}^n|a_k|$ asegura que es de Cauchy. Dada $\varepsilon>0$, elegimos $N$ con $u_p-u_q<\varepsilon$ para $p>q\ge N$. La triangular finita da
$$|s_p-s_q|\le\sum_{k=q+1}^p|a_k|=u_p-u_q<\varepsilon.$$
El mismo corte controla todos los bloques originales. Cauchy y la completitud de los reales proporcionan entonces su suma, incluso si sus aportes cambian arbitrariamente de signo.

### Microcontrol 037

[]{#MA-MIC-ANM-01-011-037}

[]{#MA-MSOL-ANM-01-011-037}

**Pregunta.** ¿Se necesita sumar primero la original para aplicar control absoluto?

**Solución.** No. Se dominan bloques finitos y se obtiene existencia del límite mediante C10.

Asumir de entrada que existe $S$ para demostrar la convergencia sería circular. La prueba trabaja primero con $s_p-s_q$, que siempre está definido porque ambos son sumas finitas. La comparación con bloques de magnitudes hace de Cauchy a la sucesión $s$. Sólo al final invocamos la completitud para obtener un límite $S$. Este orden permite usar el criterio precisamente cuando todavía desconocemos el destino y quizá no podamos calcularlo explícitamente.

### Microcontrol 038

[]{#MA-MIC-ANM-01-011-038}

[]{#MA-MSOL-ANM-01-011-038}

**Pregunta.** ¿Qué relación hay entre las sumas $S$ y $A$ de la original y las magnitudes?

**Solución.** $|S|\le A$, al pasar al límite en $|s_n|\le u_n$.

Para cada $n$, la triangular finita proporciona $|s_n|\le u_n$. Ya sabemos que $s_n\to S$ y $u_n\to A$. La triangular inversa implica $\bigl||s_n|-|S|\bigr|\le|s_n-S|$, de modo que $|s_n|\to|S|$. Al pasar al límite, el orden conserva la desigualdad no estricta y da $|S|\le A$. Puede haber desigualdad estricta porque los aportes con signos opuestos pueden compensarse.

### Microcontrol 039

[]{#MA-MIC-ANM-01-011-039}

[]{#MA-MSOL-ANM-01-011-039}

**Pregunta.** ¿Qué cota de error proporciona $u_n\to A$?

**Solución.** $|S-s_n|\le A-u_n$, tomando el límite del extremo posterior del bloque.

Fijemos $n$ y dejemos variable el extremo posterior $p>n$. La estimación finita dice $|s_p-s_n|\le u_p-u_n$. Cuando $p\to\infty$, el miembro izquierdo tiende a $|S-s_n|$ y el derecho a $A-u_n$. El orden pasa al límite y conserva la cota. La cantidad $A-u_n$ es no negativa y tiende a cero, por lo que sirve como presupuesto de error para aproximar la suma original, independientemente de sus signos.

### Microcontrol 040

[]{#MA-MIC-ANM-01-011-040}

[]{#MA-MSOL-ANM-01-011-040}

**Pregunta.** ¿Qué error asegura $|a_n|\le C\rho^n$ con $0<\rho<1$?

**Solución.** $|S-s_n|\le C\rho^{n+1}/(1-\rho)$; para $C=0$ el error es cero.

La hipótesis presupone $C\ge0$. Para $p>n$, comparamos el bloque de magnitudes con una suma geométrica finita y obtenemos
$$\sum_{k=n+1}^p|a_k|\le C\sum_{k=n+1}^p\rho^k\le\frac{C\rho^{n+1}}{1-\rho}.$$
La misma comparación demuestra convergencia absoluta. Al pasar al límite posterior, la cota domina el resto. Para un error estrictamente menor que $\varepsilon$, escogemos $n$ haciendo esa expresión menor que $\varepsilon$; si $C=0$, todos los aportes son cero.

## §11.6 — Alternancia: encerrar sin sumar magnitudes

### Microcontrol 041

[]{#MA-MIC-ANM-01-011-041}

[]{#MA-MSOL-ANM-01-011-041}

[]{#MA-SEC-ANM-01-011-006}

**Pregunta.** ¿Qué tres condiciones se imponen a la alternancia?

**Solución.** Los términos son $(-1)^nb_n$, las magnitudes son no negativas y decrecientes, y $b_n\to0$.

Escribimos $a_n=(-1)^nb_n$ con $b_n\ge0$, $b_{n+1}\le b_n$ y $b_n\to0$. La primera condición identifica las magnitudes; la segunda permite controlar las cancelaciones por parejas; la tercera hace que la cota de los bloques tienda a cero. Cada hipótesis tiene una función en la prueba. Aquí decreciente significa no creciente: se permiten igualdades, e incluso que desde algún índice todas las magnitudes sean cero.

### Microcontrol 042

[]{#MA-MIC-ANM-01-011-042}

[]{#MA-MSOL-ANM-01-011-042}

**Pregunta.** ¿Qué cota tiene un bloque alternado que empieza en $q+1$?

**Solución.** $|s_p-s_q|\le b_{q+1}$ para $p>q$, por el lema de emparejamiento.

Multipliquemos el bloque por el signo de su primer aporte. Queda $T=b_{q+1}-b_{q+2}+b_{q+3}-\cdots$. Al agrupar desde el comienzo en parejas, cada diferencia es no negativa y cualquier aporte final también lo es, luego $T\ge0$. Agrupando desde el segundo término, el resto sustrae cantidades no negativas a $b_{q+1}$, luego $T\le b_{q+1}$. Por tanto el valor absoluto del bloque es a lo sumo su primera magnitud, cualquiera que sea su longitud.

### Microcontrol 043

[]{#MA-MIC-ANM-01-011-043}

[]{#MA-MSOL-ANM-01-011-043}

**Pregunta.** ¿Qué hipótesis permite emparejar diferencias no negativas?

**Solución.** El decrecimiento $b_{n+1}\le b_n$.

Si $b_j\ge b_{j+1}$, la pareja $b_j-b_{j+1}$ aporta una cantidad no negativa. Este hecho permite encerrar el bloque alternado entre cero y su primera magnitud. Alternar signos sin ordenar magnitudes no garantiza esa propiedad: una magnitud negativa en el segundo lugar puede ser mayor que la primera y hacer fallar el encierro. La monotonía proporciona el control algebraico de las compensaciones; que las magnitudes tiendan a cero tiene otro papel.

### Microcontrol 044

[]{#MA-MIC-ANM-01-011-044}

[]{#MA-MSOL-ANM-01-011-044}

**Pregunta.** ¿Qué hipótesis hace pequeño el control del bloque?

**Solución.** $b_n\to0$ permite un único corte con $b_{q+1}<\varepsilon$ para todos los bloques tardíos.

Dada $\varepsilon>0$, la convergencia de $b_n$ a cero proporciona $N$ tal que $b_j<\varepsilon$ para todo $j\ge N$. Si $p>q\ge N$, el primer índice del bloque es $q+1\ge N$ y el lema da $|s_p-s_q|\le b_{q+1}<\varepsilon$. Este único corte sirve para todos los extremos posteriores. Ya tenemos Cauchy de los totales, y la completitud garantiza la existencia de la suma real.

### Microcontrol 045

[]{#MA-MIC-ANM-01-011-045}

[]{#MA-MSOL-ANM-01-011-045}

**Pregunta.** ¿Qué error y signo tiene el resto?

**Solución.** $0\le(-1)^{n+1}(S-s_n)\le b_{n+1}$, así que el resto tiene el signo del próximo término salvo que sea cero.

Para cada bloque posterior al total $s_n$, el encierro firmado da $0\le(-1)^{n+1}(s_p-s_n)\le b_{n+1}$. Fijamos $n$ y dejamos $p\to\infty$; el orden se conserva y obtenemos el encierro del resto. Si $n$ es par, el próximo aporte es negativo y $S\le s_n$; si es impar, es positivo y $S\ge s_n$. En ambos casos el error absoluto no supera $b_{n+1}$; un resto cero no tiene signo positivo ni negativo.

### Microcontrol 046

[]{#MA-MIC-ANM-01-011-046}

[]{#MA-MSOL-ANM-01-011-046}

**Pregunta.** ¿Qué intervalo contiene la suma entre los cortes $2k$ y $2k+1$?

**Solución.** $[s_{2k+1},s_{2k}]$, de anchura $b_{2k+1}$.

El control del signo dice que $s_{2k}$ queda por encima de $S$ y $s_{2k+1}$ por debajo. Además, los dos totales difieren en el aporte de índice $2k+1$:
$$s_{2k}-s_{2k+1}=b_{2k+1}.$$
Así ambos extremos forman un intervalo que contiene la suma y cuya anchura está calculada. Como $b_{2k+1}\to0$, esos intervalos ofrecen aproximaciones cada vez más precisas. Ningún extremo tiene por qué coincidir exactamente con la suma.

### Microcontrol 047

[]{#MA-MIC-ANM-01-011-047}

[]{#MA-MSOL-ANM-01-011-047}

**Pregunta.** ¿Por qué la armónica alternada es condicional?

**Solución.** La alternancia decreciente prueba convergencia, mientras la serie de magnitudes es la armónica divergente.

Aquí $b_n=1/(n+1)$ es no negativo, no creciente y tiende a cero, por lo que el criterio alternado prueba la convergencia de $\sum(-1)^n/(n+1)$. Al tomar magnitudes obtenemos $\sum1/(n+1)$, cuyos bloques tardíos mantienen separaciones de al menos $1/2$ y cuya divergencia ya está acreditada. Se cumplen las dos condiciones de convergencia condicional. No hace falta identificar numéricamente la suma para establecer esta clasificación.

### Microcontrol 048

[]{#MA-MIC-ANM-01-011-048}

[]{#MA-MSOL-ANM-01-011-048}

**Pregunta.** ¿Qué falla si se alternan $2/(k+1)$ y $1/(k+1)$ por parejas?

**Solución.** Las magnitudes tienden a cero, pero no decrecen globalmente y cada pareja aporta $1/(k+1)$; los totales de fin de pareja son armónicos no acotados.

Los aportes de la pareja $k$ son $2/(k+1)$ y $-1/(k+1)$; su suma es $1/(k+1)$. Las magnitudes de ambos tienden a cero, pero entre parejas pueden aumentar: el paso de $1/(k+1)$ a $2/(k+2)$ aumenta para $k>0$. Los totales al final de cada pareja son las sumas parciales armónicas. Si convergieran todos los totales, también convergería esa subsucesión, lo que contradice su divergencia. El ejemplo muestra por qué no se puede suprimir la monotonía del criterio.

## §11.7 — Agrupar términos y conservar el recorrido

### Microcontrol 049

[]{#MA-MIC-ANM-01-011-049}

[]{#MA-MSOL-ANM-01-011-049}

[]{#MA-SEC-ANM-01-011-007}

**Pregunta.** ¿Qué son las sumas parciales de la serie agrupada?

**Solución.** $t_k=s_{\phi(k)}$: los totales originales en los extremos de los grupos consecutivos.

Cada grupo reúne un bloque consecutivo de aportes y la agrupación comienza con el prefijo inicial correspondiente. Al sumar los primeros grupos, cada aporte desde cero hasta $\phi(k)$ aparece exactamente una vez; por asociatividad de sumas finitas, el resultado es $s_{\phi(k)}$. La agrupación selecciona ciertos totales del recorrido original. No permuta los aportes ni salta ninguno, pero deja de mostrar lo sucedido dentro de cada bloque.

### Microcontrol 050

[]{#MA-MIC-ANM-01-011-050}

[]{#MA-MSOL-ANM-01-011-050}

**Pregunta.** ¿Por qué convergencia original implica convergencia agrupada?

**Solución.** $\phi(k)\ge k$ por inducción, de modo que el mismo control eventual alcanza los extremos de grupo y conserva el límite.

Los extremos $\phi(k)$ forman una sucesión estrictamente creciente de naturales. Como $\phi(0)\ge0$ y cada aumento es al menos uno, por inducción $\phi(k)\ge k$. Si $s_n\to S$, recibida $\varepsilon$ escogemos un corte $N$ para los totales originales. Cuando $k\ge N$, también $\phi(k)\ge N$, luego $|t_k-S|=|s_{\phi(k)}-S|<\varepsilon$. Así la agrupación conserva la suma con un corte explícito.

### Microcontrol 051

[]{#MA-MIC-ANM-01-011-051}

[]{#MA-MSOL-ANM-01-011-051}

**Pregunta.** ¿Puede fallar la recíproca?

**Solución.** Sí. Parejas $(1,-1)$ dan grupos cero, pero los totales originales alternan uno y cero.

Para $a_n=(-1)^n$, agrupar cada pareja consecutiva produce aportes agrupados $1-1=0$. Todos los totales agrupados valen cero, por lo que convergen. Los originales, en cambio, valen uno en los índices pares y cero en los impares. La agrupación sólo observa los finales impares y oculta los totales intermedios iguales a uno. Por tanto, convergencia de una subsucesión de totales no obliga a converger al recorrido completo.

### Microcontrol 052

[]{#MA-MIC-ANM-01-011-052}

[]{#MA-MSOL-ANM-01-011-052}

**Pregunta.** ¿Qué índices deja de mostrar la agrupación?

**Solución.** Los índices interiores entre dos extremos sucesivos, donde pueden producirse excursiones.

Entre $\phi(k-1)$ y $\phi(k)$ puede haber muchos totales que la serie agrupada no registra. Un bloque puede partir de un valor, alejarse mucho mientras se incorporan sus primeros aportes y volver cerca del destino al terminar. Los finales de grupo describen únicamente el regreso. Para recuperar convergencia de todos los totales necesitamos controlar también la máxima separación dentro de cada grupo, no sólo la distancia de sus finales al límite.

### Microcontrol 053

[]{#MA-MIC-ANM-01-011-053}

[]{#MA-MSOL-ANM-01-011-053}

**Pregunta.** ¿Qué condición interior recupera la convergencia completa?

**Solución.** Que las distancias de todos los totales de cada grupo a su extremo tiendan uniformemente a cero, además de convergencia de los extremos.

Supongamos $s_{\phi(k)}\to S$ y que el máximo de $|s_n-s_{\phi(k)}|$ entre los índices del grupo $k$ tiende a cero. Dada $\varepsilon$, escogemos grupos suficientemente tardíos para que tanto ese máximo como $|s_{\phi(k)}-S|$ sean menores que $\varepsilon/2$. Entonces todo total de esos grupos satisface
$$|s_n-S|\le|s_n-s_{\phi(k)}|+|s_{\phi(k)}-S|<\varepsilon.$$
Como los grupos consecutivos cubren la cola, esto prueba la convergencia completa.

### Microcontrol 054

[]{#MA-MIC-ANM-01-011-054}

[]{#MA-MSOL-ANM-01-011-054}

**Pregunta.** ¿Qué dos hipótesis bastan para ese control interior?

**Solución.** $a_n\to0$ y una cota natural común $M$ para la longitud de cada grupo.

Si cada grupo tiene a lo sumo $M$ aportes y $a_n\to0$, podemos hacer simultáneamente pequeñas todas las magnitudes de una cola. La diferencia entre un total interior y el final de su grupo es una suma de a lo sumo $M$ aportes, por lo que la triangular finita la hace pequeña. El número común $M$ evita acumular una cantidad creciente de errores pequeños. Para concluir convergencia original se necesita además que converjan los finales de grupo.

### Microcontrol 055

[]{#MA-MIC-ANM-01-011-055}

[]{#MA-MSOL-ANM-01-011-055}

**Pregunta.** ¿Cómo se usa la cota $M$?

**Solución.** Se hacen los términos menores que $\varepsilon/M$; cualquier distancia interior suma a lo sumo $M$ magnitudes y resulta menor que $\varepsilon$.

Los grupos son no vacíos, así que una cota natural de sus longitudes puede tomarse con $M\ge1$. Elegimos una cola donde $|a_j|<\varepsilon/M$. Cualquier separación interior suma, en valor absoluto, a lo sumo $M$ de esas magnitudes y queda por debajo de $\varepsilon$; si no hay aportes entre los dos extremos, la distancia es cero. Al combinar este control con el error de los finales de grupo se reparten las tolerancias, por ejemplo usando $\varepsilon/(2M)$ para los aportes.

### Microcontrol 056

[]{#MA-MIC-ANM-01-011-056}

[]{#MA-MSOL-ANM-01-011-056}

**Pregunta.** ¿Qué muestra el bloque de $m$ aportes $1/m$ y $m$ aportes $-1/m$?

**Solución.** Términos que tienden a cero y extremos de grupo cero pueden coexistir con totales interiores uno; sin controlar longitud o excursión, la agrupación oculta divergencia.

El bloque $m$ empieza con $m$ aportes de $1/m$ y termina con $m$ de $-1/m$. Al completar su mitad positiva, el total ha aumentado en uno; al finalizar el bloque vuelve a cero. Cuando $m$ crece, cada aporte tiene magnitud $1/m\to0$, pero las longitudes $2m$ no están acotadas. Hay totales interiores arbitrariamente tardíos iguales a uno y finales iguales a cero, lo que impide Cauchy. Agrupar cada bloque completo ocultaría todas esas excursiones.

## §11.8 — Elegir un control y certificar el error

### Microcontrol 057

[]{#MA-MIC-ANM-01-011-057}

[]{#MA-MSOL-ANM-01-011-057}

[]{#MA-SEC-ANM-01-011-008}

**Pregunta.** ¿Basta $E_n\le\varepsilon$ para certificar error estrictamente menor que $\varepsilon$?

**Solución.** No. Si sólo sabemos $|S-s_n|\le E_n$, es suficiente exigir $E_n<\varepsilon$.

Las desigualdades se encadenan como $|S-s_n|\le E_n$. Si sólo imponemos $E_n\le\varepsilon$, concluimos error menor o igual que $\varepsilon$, y la igualdad puede ocurrir. Para obtener el requisito estricto, basta exigir $E_n<\varepsilon$. Otra opción es buscar $E_n\le\varepsilon/2$, que deja un margen. La distinción no es tipográfica: un certificado debe implicar exactamente la tolerancia prometida.

### Microcontrol 058

[]{#MA-MIC-ANM-01-011-058}

[]{#MA-MSOL-ANM-01-011-058}

**Pregunta.** ¿Qué error tiene el punto medio de un intervalo certificado?

**Solución.** Si $L_n\le S\le U_n$, su punto medio tiene error a lo sumo $(U_n-L_n)/2$.

Sea $m_n=(L_n+U_n)/2$ y $h_n=(U_n-L_n)/2$. Del encierro $L_n\le S\le U_n$, al restar $m_n$ obtenemos $-h_n\le S-m_n\le h_n$. Por tanto $|S-m_n|\le h_n$. El promedio equilibra las distancias a las dos fronteras y reduce a la mitad el peor error que se obtiene usando un extremo. La conclusión requiere que el intervalo esté certificado; un intervalo construido sólo a partir de observaciones no proporciona esa garantía.

### Microcontrol 059

[]{#MA-MIC-ANM-01-011-059}

[]{#MA-MSOL-ANM-01-011-059}

**Pregunta.** ¿Debe ese punto medio ser una suma parcial?

**Solución.** No. Es un real construido como promedio de dos fronteras y puede no coincidir con ningún total.

Las sumas parciales pertenecen a la lista específica $s_0,s_1,\ldots$, mientras que el promedio es una operación nueva sobre dos fronteras. Por ejemplo, en la geométrica con razón $1/2$ los totales iniciales son $1$ y $3/2$; su promedio $5/4$ no es ningún total, porque los posteriores son al menos $3/2$. Ese ejemplo distingue los objetos; para certificar una aproximación a la suma hay que usar fronteras que además la encierren.

### Microcontrol 060

[]{#MA-MIC-ANM-01-011-060}

[]{#MA-MSOL-ANM-01-011-060}

**Pregunta.** ¿Qué intervalo se obtiene con $s_4$ y $s_5$ en la armónica alternada?

**Solución.** $[37/60,47/60]$, cuyo punto medio es $7/10$ y cuyo semiancho es $1/12$.

Calculamos con la indexación desde cero:
$$s_4=1-\frac12+\frac13-\frac14+\frac15=\frac{47}{60},\qquad s_5=s_4-\frac16=\frac{37}{60}.$$
La alternancia sitúa la suma entre estos dos totales. Su promedio es $(47+37)/120=7/10$ y su semianchura es $(47-37)/120=1/12$. Queda certificado $|S-7/10|\le1/12$. No se ha usado una fórmula externa para el valor exacto de la suma.

### Microcontrol 061

[]{#MA-MIC-ANM-01-011-061}

[]{#MA-MSOL-ANM-01-011-061}

**Pregunta.** ¿Ese cálculo demuestra que la suma vale $7/10$?

**Solución.** No. Demuestra $|S-7/10|\le1/12$, una aproximación con error certificado.

El certificado permite que $S$ sea cualquier punto del intervalo $[37/60,47/60]$ compatible con los demás datos; el promedio es sólo una elección de aproximante. Una cota positiva de error no fuerza igualdad. Para demostrar $S=7/10$ necesitaríamos un argumento adicional que hiciera cero esa diferencia o la acotara por toda tolerancia positiva. El intervalo finito aporta información útil sobre precisión, aunque no determine exactamente el número.

### Microcontrol 062

[]{#MA-MIC-ANM-01-011-062}

[]{#MA-MSOL-ANM-01-011-062}

**Pregunta.** ¿Qué permite sumar linealmente dos series convergentes?

**Solución.** La identidad de sumas finitas y el álgebra de límites de C06 dan suma $\alpha A+\beta B$.

Si $a$ y $b$ tienen totales $s_n^a\to A$ y $s_n^b\to B$, la suma finita de los aportes $\alpha a_k+\beta b_k$ es $\alpha s_n^a+\beta s_n^b$. El álgebra de límites lleva esos totales a $\alpha A+\beta B$. Para ver el control explícito, acotamos el error por $|\alpha||s_n^a-A|+|\beta||s_n^b-B|$ y escogemos un único corte que haga pequeños ambos sumandos. Las identidades infinitas resultan de identidades finitas verificadas previamente.

### Microcontrol 063

[]{#MA-MIC-ANM-01-011-063}

[]{#MA-MSOL-ANM-01-011-063}

**Pregunta.** ¿Qué suma tiene la cola reindexada que elimina $m$ términos?

**Solución.** $S-P_m$, con $P_m=\sum_{j=0}^{m-1}a_j$ y $P_0=0$.

Si $c_k=a_{k+m}$, su total es $t_n=\sum_{k=0}^n a_{k+m}=s_{n+m}-P_m$, donde $P_m$ contiene exactamente los aportes eliminados, desde cero hasta $m-1$. Como $s_{n+m}\to S$, el álgebra de límites da $t_n\to S-P_m$. Para $m=0$ el prefijo es vacío, $P_0=0$, y recuperamos la serie original. Eliminar finitos términos conserva la convergencia, pero generalmente modifica el valor de la suma.

### Microcontrol 064

[]{#MA-MIC-ANM-01-011-064}

[]{#MA-MSOL-ANM-01-011-064}

**Pregunta.** ¿Una muestra finita de totales demuestra convergencia?

**Solución.** No. La prueba debe controlar todos los bloques después de un corte; la muestra sólo ilustra valores seleccionados.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-microcontroles.html)

Una lista finita de totales no informa sobre todos los valores posteriores. Incluso si esos totales parecen estabilizados, podemos conservar el prefijo observado y elegir después aportes constantes iguales a uno: los nuevos totales crecerán sin límite. También podemos elegir después aportes cero, obteniendo convergencia. Ambas continuaciones coinciden en toda la muestra. La demostración debe usar una regla o estimación que controle una cola completa; las tablas y gráficos ayudan a explorar esa regla, pero no la sustituyen.
