---
content-id: MA-BCH-0297
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-023-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 23
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C23_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §23.1 — Cotas de valores y oscilación

### Microcontrol 001

[]{#MA-MIC-ANM-01-023-001}

[]{#MA-MSOL-ANM-01-023-001}

[]{#MA-SEC-ANM-01-023-001}

**Pregunta.** ¿Qué hipótesis permite extremos locales reales?

**Solución.** Para un conjunto no vacío $J$, se necesita que $f[J]$ esté acotado. La completitud de los reales proporciona $m(f,J)=\inf f[J]$ y $M(f,J)=\sup f[J]$. Estos extremos del conjunto de valores existen aunque ningún punto los alcance; un extremo local en el sentido del cálculo sería otra afirmación.

### Microcontrol 002

[]{#MA-MIC-ANM-01-023-002}

[]{#MA-MSOL-ANM-01-023-002}

**Pregunta.** ¿La oscilación es una derivada?

**Solución.** La oscilación es $\omega(f,J)=M(f,J)-m(f,J)$. Mide el rango de alturas en toda la pieza y se define para cualquier función acotada allí. Una función constante tiene oscilación cero; una función con un salto puede tener oscilación positiva aunque la derivada no exista en el salto.

### Microcontrol 003

[]{#MA-MIC-ANM-01-023-003}

[]{#MA-MSOL-ANM-01-023-003}

**Pregunta.** ¿Deben alcanzarse $m$ y $M$?

**Solución.** El supremo es una cota superior mínima y el ínfimo una cota inferior máxima. Para $f(x)=x$ en $(0,1)$ son uno y cero, respectivamente, sin pertenecer a la imagen. La definición de las sumas de Darboux utiliza esas cotas y no necesita puntos de máximo o mínimo.

### Microcontrol 004

[]{#MA-MIC-ANM-01-023-004}

[]{#MA-MSOL-ANM-01-023-004}

**Pregunta.** ¿Qué ocurre al restringir a $J\subseteq K$?

**Solución.** La inclusión $f[J]\subseteq f[K]$ da $m(f,K)\le m(f,J)\le M(f,J)\le M(f,K)$. Las cotas de la imagen grande siguen valiendo sobre la pequeña. Al restar los extremos resulta $0\le\omega(f,J)\le\omega(f,K)$. Se supone que las dos imágenes son no vacías y acotadas.

### Microcontrol 005

[]{#MA-MIC-ANM-01-023-005}

[]{#MA-MSOL-ANM-01-023-005}

**Pregunta.** ¿Qué cota da $|f|\le B$ para la oscilación?

**Solución.** De $-B\le f(x)\le B$ se deduce $-B\le m\le M\le B$. Por ello $0\le M-m\le B-(-B)=2B$. La cota es alcanzable si la imagen contiene ambas alturas $-B$ y $B$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-023-006}

[]{#MA-MSOL-ANM-01-023-006}

**Pregunta.** ¿Cómo se obtiene una altura cercana al supremo?

**Solución.** Para $\eta>0$, si ninguna entrada satisficiera $f(s)>M-\eta$, todas cumplirían $f(s)\le M-\eta$. Ese real sería una cota superior estrictamente menor que $M$, contra la minimalidad del supremo. Así se obtiene una altura próxima a $M$ sin suponer que éste sea un valor de la función.

### Microcontrol 007

[]{#MA-MIC-ANM-01-023-007}

[]{#MA-MSOL-ANM-01-023-007}

**Pregunta.** ¿Cuál es la oscilación de $x^2$ en $[u,v]\subseteq[0,1]$?

**Solución.** Para $0\le u\le x\le v$, el orden de los cuadrados da $u^2\le x^2\le v^2$. Como ambos extremos están en la pieza, $m=u^2$ y $M=v^2$. La oscilación es $v^2-u^2=(v-u)(v+u)$, a lo sumo $2(v-u)$ en $[0,1]$.

### Microcontrol 008

[]{#MA-MIC-ANM-01-023-008}

[]{#MA-MSOL-ANM-01-023-008}

**Pregunta.** ¿Dos muestras determinan la oscilación?

**Solución.** Tomemos una función que vale cero en las dos entradas muestreadas y una altura $H>0$ en una tercera entrada. Sus dos muestras siguen siendo cero, mientras su oscilación es $H$. Como $H$ puede crecer sin límite, el control de toda la pieza exige información sobre las entradas restantes.

## §23.2 — Dos sumas que el refinamiento sí ordena

### Microcontrol 009

[]{#MA-MIC-ANM-01-023-009}

[]{#MA-MSOL-ANM-01-023-009}

[]{#MA-SEC-ANM-01-023-002}

**Pregunta.** ¿Cómo se define $L$?

**Solución.** En $P=(x_0,\ldots,x_n)$, ponemos $I_i=[x_{i-1},x_i]$ y $\Delta_i=x_i-x_{i-1}>0$. La suma inferior es $L(f,P)=\sum_{i=1}^n m(f,I_i)\Delta_i$. Cada altura es una cota inferior válida en su pieza; puede ser negativa o no alcanzarse.

### Microcontrol 010

[]{#MA-MIC-ANM-01-023-010}

[]{#MA-MSOL-ANM-01-023-010}

**Pregunta.** ¿Cómo se define $U$?

**Solución.** Con las mismas piezas y anchuras, $U(f,P)=\sum_{i=1}^n M(f,I_i)\Delta_i$. Las alturas superiores acotan todas las evaluaciones posibles, incluso cuando no hay puntos de máximo. La acotación de $f$ asegura que cada término es real.

### Microcontrol 011

[]{#MA-MIC-ANM-01-023-011}

[]{#MA-MSOL-ANM-01-023-011}

**Pregunta.** ¿Dónde queda una suma etiquetada?

**Solución.** Para cualquier etiqueta $\xi_i\in I_i$, se tiene $m_i\le f(\xi_i)\le M_i$. Multiplicar por $\Delta_i>0$ y sumar conserva el orden y da $L(f,P)\le S(f,P,\xi)\le U(f,P)$. El encierro vale simultáneamente para todas las etiquetas de esa partición.

### Microcontrol 012

[]{#MA-MIC-ANM-01-023-012}

[]{#MA-MSOL-ANM-01-023-012}

**Pregunta.** ¿Qué expresa la brecha?

**Solución.** Restar las dos sumas sobre una misma lista da $G(f,P)=\sum_i(M_i-m_i)\Delta_i=\sum_i\omega(f,I_i)\Delta_i$. Cada término es no negativo. La brecha pondera la incertidumbre de alturas por la longitud de la pieza que la sostiene.

### Microcontrol 013

[]{#MA-MIC-ANM-01-023-013}

[]{#MA-MSOL-ANM-01-023-013}

**Pregunta.** ¿Qué significa brecha cero sobre piezas cerradas?

**Solución.** Si la suma de los productos no negativos $\omega_i\Delta_i$ es cero, cada producto es cero. Las anchuras positivas fuerzan $\omega_i=0$, de modo que $f$ es constante en cada pieza. Dos piezas vecinas comparten un nodo y sus constantes coinciden allí; la cadena finita obliga a una sola constante global.

### Microcontrol 014

[]{#MA-MIC-ANM-01-023-014}

[]{#MA-MSOL-ANM-01-023-014}

**Pregunta.** ¿Qué sumas ordena el refinamiento?

**Solución.** Las hijas de una pieza tienen ínfimos al menos tan grandes como el del padre y supremos a lo sumo tan grandes como el suyo. Sus anchuras suman la antigua, por lo que $L$ aumenta o permanece y $U$ disminuye o permanece. Las etiquetas pueden cambiar de altura al refinar, así sus sumas pueden moverse en cualquiera de los dos sentidos.

### Microcontrol 015

[]{#MA-MIC-ANM-01-023-015}

[]{#MA-MSOL-ANM-01-023-015}

**Pregunta.** ¿Cómo se comparan $L(P)$ y $U(Q)$ con cortes distintos?

**Solución.** Ordenamos sin repeticiones la unión de los nodos de $P$ y $Q$. La partición $R$ obtenida refina ambas, y por monotonía $L(f,P)\le L(f,R)\le U(f,R)\le U(f,Q)$. El refinamiento común permite comparar sumas cuyos términos originales pertenecen a piezas diferentes.

### Microcontrol 016

[]{#MA-MIC-ANM-01-023-016}

[]{#MA-MSOL-ANM-01-023-016}

**Pregunta.** ¿Cuál es la brecha uniforme de $x^2$ en $[0,1]$?

**Solución.** Para $n\ge1$, en cada pieza uniforme la diferencia de alturas es $(i/n)^2-((i-1)/n)^2$. Todas las anchuras son $1/n$, así $G=(1/n)\sum_{i=1}^n[(i/n)^2-((i-1)/n)^2]=1/n$. La telescopía da una brecha positiva para cada partición finita y arbitrariamente pequeña al aumentar $n$.

## §23.3 — Completitud y criterio de Darboux

### Microcontrol 017

[]{#MA-MIC-ANM-01-023-017}

[]{#MA-MSOL-ANM-01-023-017}

[]{#MA-SEC-ANM-01-023-003}

**Pregunta.** ¿Por qué los conjuntos de sumas son no vacíos?

**Solución.** La partición $(a,b)$ es válida cuando $a<b$ y produce una suma inferior y una superior. Por tanto $\mathcal L_f=\{L(f,P):P\}$ y $\mathcal U_f=\{U(f,P):P\}$ contienen al menos un real. Esa no vaciedad es necesaria para aplicar completitud.

### Microcontrol 018

[]{#MA-MIC-ANM-01-023-018}

[]{#MA-MSOL-ANM-01-023-018}

**Pregunta.** ¿Qué define la integral inferior?

**Solución.** Se define $\ell_f=\sup\mathcal L_f$. Si $|f|\le B$, todas las sumas inferiores están entre $-B(b-a)$ y $B(b-a)$. El conjunto es no vacío y acotado, así el supremo es real; representa la mejor cota inferior obtenible mediante particiones.

### Microcontrol 019

[]{#MA-MIC-ANM-01-023-019}

[]{#MA-MSOL-ANM-01-023-019}

**Pregunta.** ¿Qué define la integral superior?

**Solución.** Se define $u_f=\inf\mathcal U_f$. La misma cota absoluta limita todas las sumas superiores, y la partición trivial hace no vacío el conjunto. Su ínfimo es real y puede existir sin que ninguna partición logre exactamente ese valor.

### Microcontrol 020

[]{#MA-MIC-ANM-01-023-020}

[]{#MA-MSOL-ANM-01-023-020}

**Pregunta.** ¿Por qué $\ell_f\le u_f$?

**Solución.** Fijado $Q$, el refinamiento común prueba $L(f,P)\le U(f,Q)$ para todo $P$. Por ser cota superior de $\mathcal L_f$, $U(f,Q)\ge\ell_f$. Esto vale para toda $Q$, de modo que $\ell_f$ es cota inferior de $\mathcal U_f$ y $\ell_f\le u_f$.

### Microcontrol 021

[]{#MA-MIC-ANM-01-023-021}

[]{#MA-MSOL-ANM-01-023-021}

**Pregunta.** ¿Cuál es el criterio de Darboux?

**Solución.** Para una función acotada en $[a,b]$, la integrabilidad de Darboux equivale a $\forall\varepsilon>0\ \exists P:\ G(f,P)<\varepsilon$. Si $\ell_f=u_f=I$, se aproximan ambos extremos y se refina en común. Si hay brechas arbitrariamente pequeñas, $0\le u_f-\ell_f\le G(f,P)$ impide una diferencia positiva.

### Microcontrol 022

[]{#MA-MIC-ANM-01-023-022}

[]{#MA-MSOL-ANM-01-023-022}

**Pregunta.** ¿Cómo se aproxima a ambos extremos a la vez?

**Solución.** Si $\ell_f=u_f=I$, la propiedad del supremo proporciona $P$ con $L(f,P)>I-\varepsilon/2$ y la del ínfimo proporciona $Q$ con $U(f,Q)<I+\varepsilon/2$. El refinamiento común $R$ conserva las dos mejoras, así $G(f,R)<\varepsilon$. Se necesitan sólo dos particiones para la tolerancia fijada.

### Microcontrol 023

[]{#MA-MIC-ANM-01-023-023}

[]{#MA-MSOL-ANM-01-023-023}

**Pregunta.** ¿Una partición buena conserva su precisión al refinar?

**Solución.** Para $P\preceq Q$, la monotonía de ambas sumas implica $G(f,Q)\le G(f,P)$. Así cualquier refinamiento de una partición con brecha menor que $\varepsilon$ conserva esa precisión. Recíprocamente, si todos sus refinamientos tienen brecha menor que $\varepsilon$, se toma $Q=P$, permitido por reflexividad.

### Microcontrol 024

[]{#MA-MIC-ANM-01-023-024}

[]{#MA-MSOL-ANM-01-023-024}

**Pregunta.** ¿Qué error certifica $(L+U)/2$?

**Solución.** Una integral existente $I$ satisface $L\le I\le U$. El centro $A=(L+U)/2$ dista de cada extremo $(U-L)/2$, por lo que $|A-I|\le(U-L)/2$. La brecha certifica un error máximo; el error efectivo puede ser mucho menor.

## §23.4 — El puente hacia todas las sumas de Riemann

### Microcontrol 025

[]{#MA-MIC-ANM-01-023-025}

[]{#MA-MSOL-ANM-01-023-025}

[]{#MA-SEC-ANM-01-023-004}

**Pregunta.** ¿El contrato de Riemann obliga acotación?

**Solución.** El contrato con error uno entrega un radio. Fijamos una partición de malla menor que ese radio y etiquetas de referencia. Al variar sólo la etiqueta de la pieza $i$, la suma se escribe $f(t)\Delta_i+C_i$ y sigue teniendo magnitud menor que $|I|+1$. Por ello $|f(t)|\le(|I|+1+|C_i|)/\Delta_i$ en toda esa pieza. El máximo finito de estas cotas cubre $[a,b]$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-023-026}

[]{#MA-MSOL-ANM-01-023-026}

**Pregunta.** ¿Se necesitan máximos alcanzados para aproximar $U$ con etiquetas?

**Solución.** En cada pieza escogemos una altura mayor que $M_i-\eta/(b-a)$. Multiplicar por las anchuras y sumar da $S>U-\eta$, porque $\sum_i\Delta_i=b-a$. La elección usa aproximaciones del supremo; la longitud positiva y el número finito de piezas permiten realizarla sin máximos alcanzados.

### Microcontrol 027

[]{#MA-MIC-ANM-01-023-027}

[]{#MA-MSOL-ANM-01-023-027}

**Pregunta.** ¿Una familia finita de testigos exige elección infinita?

**Solución.** Para la primera pieza existe un testigo. Si ya se construyó una familia de los primeros $k$ testigos, la existencia en la pieza siguiente permite añadir uno y obtener $k+1$. La inducción termina en el número finito de piezas de la partición. No se está seleccionando una familia sobre todas las particiones simultáneamente.

### Microcontrol 028

[]{#MA-MIC-ANM-01-023-028}

[]{#MA-MSOL-ANM-01-023-028}

**Pregunta.** ¿Qué prueba Riemann⇒Darboux?

**Solución.** Elegimos una partición de malla menor que el radio de Riemann para error $\varepsilon/4$. Hay sumas $S^+$ y $S^-$ con $U-\varepsilon/4<S^+$ y $S^-<L+\varepsilon/4$. El contrato da $U<I_R+\varepsilon/2$ y $L>I_R-\varepsilon/2$, luego $U-L<\varepsilon$. El criterio prueba Darboux y esos mismos encierros identifican su valor con $I_R$.

### Microcontrol 029

[]{#MA-MIC-ANM-01-023-029}

[]{#MA-MSOL-ANM-01-023-029}

**Pregunta.** ¿Por qué no basta refinar sólo la partición buena?

**Solución.** Una partición fina $Q$ puede omitir todos los nodos interiores de $P_*$. La monotonía de refinamientos sólo se aplica después de formar $R=P_*\cup Q$. Para volver desde $R$ a $Q$ se limita el efecto de las piezas que esos nodos dividen; su longitud total tiende a cero con la malla de $Q$.

### Microcontrol 030

[]{#MA-MIC-ANM-01-023-030}

[]{#MA-MSOL-ANM-01-023-030}

**Pregunta.** ¿Qué cuenta $q$ en el puente inverso?

**Solución.** Aquí $q$ es el número finito de nodos interiores de $P_*$. Una pieza de $Q$ se divide sólo si contiene alguno de ellos en su interior. Los interiores de las piezas de $Q$ son disjuntos, así cada nodo puede dividir una sola pieza y hay a lo sumo $q$ piezas afectadas. Varios nodos pueden caer en una misma pieza.

### Microcontrol 031

[]{#MA-MIC-ANM-01-023-031}

[]{#MA-MSOL-ANM-01-023-031}

**Pregunta.** ¿Qué cota conecta las brechas?

**Solución.** Sea $|f|\le B$ y $R=P_*\cup Q$. En una pieza dividida de anchura $\Delta$, la caída de la suma superior y el aumento de la inferior son cada uno a lo sumo $2B\Delta$. Sumar sobre a lo sumo $q$ piezas da $G(f,Q)-G(f,R)\le4Bq\|Q\|$. Como $R$ refina $P_*$, se obtiene $G(f,Q)\le G(f,P_*)+4Bq\|Q\|$.

### Microcontrol 032

[]{#MA-MIC-ANM-01-023-032}

[]{#MA-MSOL-ANM-01-023-032}

**Pregunta.** ¿Qué se hace si $Bq=0$?

**Solución.** Si $Bq=0$, el término de corrección $4Bq\|Q\|$ desaparece. Con $G(f,P_*)<\varepsilon/2$, queda $G(f,Q)<\varepsilon/2$ para toda $Q$. Puede tomarse cualquier radio positivo, por ejemplo uno. La fórmula que divide por $Bq$ se reserva para $Bq>0$.

## §23.5 — Clases integrables y radios útiles

### Microcontrol 033

[]{#MA-MIC-ANM-01-023-033}

[]{#MA-MSOL-ANM-01-023-033}

[]{#MA-SEC-ANM-01-023-005}

**Pregunta.** ¿Por qué una monótona en un cerrado está acotada?

**Solución.** Si $f$ es no decreciente, $f(a)\le f(x)\le f(b)$; si es no creciente se invierte el orden de los extremos. En ambos casos $|f(x)|\le\max(|f(a)|,|f(b)|)$ en todo el cerrado. Esta acotación permite formar las sumas de Darboux incluso cuando hay saltos.

### Microcontrol 034

[]{#MA-MIC-ANM-01-023-034}

[]{#MA-MSOL-ANM-01-023-034}

**Pregunta.** ¿Qué cota de brecha tiene una no decreciente?

**Solución.** En la pieza $[x_{i-1},x_i]$, los extremos de una función no decreciente son sus valores en los bordes. Por tanto $G=\sum_i(f(x_i)-f(x_{i-1}))\Delta_i\le\|P\|\sum_i(f(x_i)-f(x_{i-1}))=\|P\|(f(b)-f(a))$. Las diferencias no negativas permiten sustituir cada anchura por la malla.

### Microcontrol 035

[]{#MA-MIC-ANM-01-023-035}

[]{#MA-MSOL-ANM-01-023-035}

**Pregunta.** ¿Qué cota da Lipschitz L?

**Solución.** Si $|f(s)-f(t)|\le L|s-t|$, las diferencias de alturas de la pieza $I_i$ no superan $L\Delta_i$. Tomar extremos da $\omega(f,I_i)\le L\Delta_i$. Así $G\le L\sum_i\Delta_i^2\le L\|P\|(b-a)$. Para $L>0$, una malla menor que $\varepsilon/(L(b-a))$ garantiza brecha menor que $\varepsilon$.

### Microcontrol 036

[]{#MA-MIC-ANM-01-023-036}

[]{#MA-MSOL-ANM-01-023-036}

**Pregunta.** ¿Qué herramienta adicional usa el caso continuo?

**Solución.** La continuidad entrega un radio alrededor de cada centro para el error de alturas pedido. La compacidad de $[a,b]$ permite reducir las correspondientes vecindades a una lista finita. El mínimo positivo de sus radios reducidos construye una escala que sirve para todas las parejas cercanas del intervalo.

### Microcontrol 037

[]{#MA-MIC-ANM-01-023-037}

[]{#MA-MSOL-ANM-01-023-037}

**Pregunta.** ¿Por qué continuidad en el cerrado da cota global?

**Solución.** En cada centro $c$ existe una vecindad donde $|f(x)-f(c)|<1$. Estas vecindades cubren el cerrado y un subcubrimiento finito tiene centros $c_1,\ldots,c_k$. Cualquier entrada pertenece a una de ellas y satisface $|f(x)|<|f(c_j)|+1$. El máximo de esas $k$ cantidades es una cota global.

### Microcontrol 038

[]{#MA-MIC-ANM-01-023-038}

[]{#MA-MSOL-ANM-01-023-038}

**Pregunta.** ¿Cómo se fabrica un radio uniforme?

**Solución.** Consideramos todos los pares válidos $(c,r)$ con $|f(x)-f(c)|<\eta/2$ si $|x-c|<r$. Sus bolas de radio $r/2$ cubren el intervalo. Un subcubrimiento finito permite tomar $\delta=\min_j r_j/2>0$. Si $s$ pertenece a una de esas bolas y $|s-t|<\delta$, ambos están a distancia menor que $r_j$ de su centro y $|f(s)-f(t)|<\eta$.

### Microcontrol 039

[]{#MA-MIC-ANM-01-023-039}

[]{#MA-MSOL-ANM-01-023-039}

**Pregunta.** ¿Por qué se pide η=ε/(2(b−a))?

**Solución.** El radio uniforme garantiza diferencias estrictamente menores que $\eta$, pero al tomar supremo e ínfimo puede quedar sólo $\omega_i\le\eta$. Con $\eta=\varepsilon/(2(b-a))$, las piezas de malla menor que ese radio satisfacen $G\le\eta\sum_i\Delta_i=\varepsilon/2<\varepsilon$. El factor dos conserva la estrictitud requerida.

### Microcontrol 040

[]{#MA-MIC-ANM-01-023-040}

[]{#MA-MSOL-ANM-01-023-040}

**Pregunta.** ¿La continuidad es necesaria para integrar?

**Solución.** La función que vale cero antes de $1/2$ y uno desde $1/2$ es monótona y tiene un salto. Su brecha está acotada por la malla, de modo que el criterio de Darboux prueba su integrabilidad. La continuidad proporciona otra clase integrable, pero este ejemplo muestra que no es necesaria.

## §23.6 — Álgebra de funciones e integrales

### Microcontrol 041

[]{#MA-MIC-ANM-01-023-041}

[]{#MA-MSOL-ANM-01-023-041}

[]{#MA-SEC-ANM-01-023-006}

**Pregunta.** ¿Qué cota tiene la oscilación de una suma?

**Solución.** Para entradas $s,t$ en $J$, $|(f+g)(s)-(f+g)(t)|\le|f(s)-f(t)|+|g(s)-g(t)|\le\omega(f,J)+\omega(g,J)$. Tomar los extremos de la imagen de $f+g$ da la cota. No se requiere que las alturas extremas de $f$ y $g$ ocurran en las mismas entradas.

### Microcontrol 042

[]{#MA-MIC-ANM-01-023-042}

[]{#MA-MSOL-ANM-01-023-042}

**Pregunta.** ¿Qué sucede con un múltiplo negativo?

**Solución.** Si $\alpha<0$, multiplicar invierte el orden: $M(\alpha f,J)=\alpha m(f,J)$ y $m(\alpha f,J)=\alpha M(f,J)$. Restar da $\omega(\alpha f,J)=-\alpha\omega(f,J)=|\alpha|\omega(f,J)$. Para $\alpha>0$ el orden se conserva, y para cero ambas alturas extremas son cero.

### Microcontrol 043

[]{#MA-MIC-ANM-01-023-043}

[]{#MA-MSOL-ANM-01-023-043}

**Pregunta.** ¿Qué controla el valor absoluto?

**Solución.** La desigualdad triangular inversa da $\big||f(s)|-|f(t)|\big|\le|f(s)-f(t)|\le\omega(f,J)$. Al tomar extremos resulta $\omega(|f|,J)\le\omega(f,J)$. Por ello toda partición buena para $f$ tiene una brecha al menos tan pequeña para $|f|$, que también es integrable.

### Microcontrol 044

[]{#MA-MIC-ANM-01-023-044}

[]{#MA-MSOL-ANM-01-023-044}

**Pregunta.** ¿Qué cota controla un producto?

**Solución.** Escribimos $f(s)g(s)-f(t)g(t)=f(s)(g(s)-g(t))+g(t)(f(s)-f(t))$. Con $|f|\le B_f$ y $|g|\le B_g$, la triangular limita su magnitud por $B_f\omega(g,J)+B_g\omega(f,J)$. La cota vale para toda pareja, así controla la oscilación del producto al tomar extremos.

### Microcontrol 045

[]{#MA-MIC-ANM-01-023-045}

[]{#MA-MSOL-ANM-01-023-045}

**Pregunta.** ¿Por qué se necesita un refinamiento común en álgebra?

**Solución.** La tolerancia de $f$ puede producir una partición $P$ y la de $g$ otra $Q$. La unión ordenada $R$ de sus nodos conserva ambas cotas de brecha por monotonía. Entonces las estimaciones de suma o producto se aplican pieza por pieza sobre una misma lista y pueden sumarse.

### Microcontrol 046

[]{#MA-MIC-ANM-01-023-046}

[]{#MA-MSOL-ANM-01-023-046}

**Pregunta.** ¿Cómo se identifica el valor de una combinación lineal?

**Solución.** Para las mismas etiquetas, $S(\alpha f+\beta g)=\alpha S(f)+\beta S(g)$. Pedimos a cada contrato error menor que $\varepsilon/(|\alpha|+|\beta|+1)$ y tomamos el mínimo de sus radios. La triangular da error combinado menor que $\varepsilon$ respecto de $\alpha I_f+\beta I_g$. La unicidad identifica ese candidato con la integral de la combinación.

### Microcontrol 047

[]{#MA-MIC-ANM-01-023-047}

[]{#MA-MSOL-ANM-01-023-047}

**Pregunta.** ¿Siempre $I_{fg}=I_f I_g$?

**Solución.** En $[0,1]$, los certificados de C22 dan $I_x=1/2$ e $I_{x^2}=1/3$. Para $f=g=x$, resulta $I_{fg}=1/3$ mientras $I_fI_g=1/4$. El cierre de la clase integrable bajo producto garantiza que existe la primera integral; no impone esa identidad entre valores.

### Microcontrol 048

[]{#MA-MIC-ANM-01-023-048}

[]{#MA-MSOL-ANM-01-023-048}

**Pregunta.** ¿Qué desigualdad integral da el valor absoluto?

**Solución.** El control de oscilación prueba la integrabilidad de $|f|$. Como $-|f|\le f\le|f|$, el orden de integrales y la linealidad dan $-I_{|f|}\le I_f\le I_{|f|}$, equivalente a $|I_f|\le I_{|f|}$. Para $f(x)=2x-1$ en $[0,1]$, los valores son cero y $1/2$, respectivamente, y la desigualdad es estricta.

## §23.7 — Restringir, pegar y orientar

### Microcontrol 049

[]{#MA-MIC-ANM-01-023-049}

[]{#MA-MSOL-ANM-01-023-049}

[]{#MA-SEC-ANM-01-023-007}

**Pregunta.** ¿Cómo se restringe una función integrable?

**Solución.** Para $a<c<b$, insertamos $c$ en una partición con brecha menor que $\varepsilon$. El refinamiento no aumenta la brecha y ésta se separa en las dos brechas no negativas de las restricciones. Cada una es menor que $\varepsilon$. Como puede hacerse para toda tolerancia, ambas restricciones cumplen Darboux.

### Microcontrol 050

[]{#MA-MIC-ANM-01-023-050}

[]{#MA-MSOL-ANM-01-023-050}

**Pregunta.** ¿Cómo se pegan dos restricciones integrables?

**Solución.** Elegimos una partición de $[a,c]$ y otra de $[c,b]$ con brechas menores que $\varepsilon/2$. Concatenar las listas dejando una sola copia del nodo $c$ produce una partición global. Sus piezas son las mismas y la brecha es la suma de las dos, menor que $\varepsilon$.

### Microcontrol 051

[]{#MA-MIC-ANM-01-023-051}

[]{#MA-MSOL-ANM-01-023-051}

**Pregunta.** ¿Qué ocurre con el valor del nodo común?

**Solución.** Las restricciones de una sola función asignan a $c$ la misma altura $f(c)$. Como las piezas son cerradas, ese dato pertenece a la última pieza izquierda y a la primera derecha. Dos asignaciones diferentes en $c$ no definen directamente una función global; primero hay que fijar un único valor nodal.

### Microcontrol 052

[]{#MA-MIC-ANM-01-023-052}

[]{#MA-MSOL-ANM-01-023-052}

**Pregunta.** ¿Cómo se prueba aditividad del valor?

**Solución.** Con particiones buenas en ambos lados, cualquier familia de etiquetas concatenada cumple $S_{ab}=S_{ac}+S_{cb}$. Cada suma queda a distancia de su integral a lo sumo la brecha correspondiente. Al hacer las dos brechas arbitrariamente pequeñas, la triangular obliga a $I_{ab}=I_{ac}+I_{cb}$.

### Microcontrol 053

[]{#MA-MIC-ANM-01-023-053}

[]{#MA-MSOL-ANM-01-023-053}

**Pregunta.** ¿Se probó aditividad numerable?

**Solución.** La identidad para dos intervalos se repite por inducción para cualquier lista finita de cortes. Una lista numerable exigiría justificar el paso al límite de una serie de valores integrales. Ese paso no forma parte de la prueba finita y necesita hipótesis y argumentos adicionales.

### Microcontrol 054

[]{#MA-MIC-ANM-01-023-054}

[]{#MA-MSOL-ANM-01-023-054}

**Pregunta.** ¿Cambiar valores en finitos puntos conserva la integral?

**Solución.** Si dos funciones difieren en $k$ puntos y las diferencias de altura no superan $D$, C22 da $|S_f-S_g|\le2kD\|P\|$. El término tiende uniformemente a cero con la malla y conserva el contrato de Riemann y su valor. La equivalencia lleva el resultado a Darboux, aunque una suma superior concreta pueda cambiar.

### Microcontrol 055

[]{#MA-MIC-ANM-01-023-055}

[]{#MA-MSOL-ANM-01-023-055}

**Pregunta.** ¿Qué significa orientación inversa?

**Solución.** Una vez construida la integral en $[a,b]$ con $a<b$, se define $\int_b^a f=-\int_a^b f$. El cambio de orientación altera el signo del valor. Las particiones utilizadas en la construcción mantienen nodos crecientes y anchuras positivas.

### Microcontrol 056

[]{#MA-MIC-ANM-01-023-056}

[]{#MA-MSOL-ANM-01-023-056}

**Pregunta.** ¿Qué vale el intervalo degenerado?

**Solución.** Se adopta la convención $\int_a^a f=0$. Una partición estrictamente creciente con al menos una pieza no puede tener extremos iguales. La convención extiende la notación al caso degenerado sin introducir divisiones por una longitud cero.

## §23.8 — Certificar un valor y reconocer el alcance

### Microcontrol 057

[]{#MA-MIC-ANM-01-023-057}

[]{#MA-MSOL-ANM-01-023-057}

[]{#MA-SEC-ANM-01-023-008}

**Pregunta.** ¿Qué necesitan las cotas numéricas $a_i,b_i$?

**Solución.** En cada pieza debe probarse $a_i\le f(x)\le b_i$ para toda entrada $x$ de ella. Entonces $a_i\le m_i\le M_i\le b_i$ y, al ponderar, $\sum_i a_i\Delta_i\le L\le I\le U\le\sum_i b_i\Delta_i$. Dos muestras aisladas no justifican las cotas de toda la imagen.

### Microcontrol 058

[]{#MA-MIC-ANM-01-023-058}

[]{#MA-MSOL-ANM-01-023-058}

**Pregunta.** ¿Una brecha pequeña una sola vez prueba integrabilidad?

**Solución.** Una partición de brecha $10^{-3}$ sólo limita $u_f-\ell_f$ por esa cantidad. El criterio exige brechas menores que cualquier real positivo. Por ejemplo una función que toma las alturas cero y $10^{-3}$ en toda pieza de $[0,1]$ tiene esa misma brecha pequeña en todas las particiones y no es integrable.

### Microcontrol 059

[]{#MA-MIC-ANM-01-023-059}

[]{#MA-MSOL-ANM-01-023-059}

**Pregunta.** ¿Cuál es el encierro de $x^2$ con n4?

**Solución.** La uniforme de cuatro piezas tiene ínfimos $0,1/16,1/4,9/16$ y supremos $1/16,1/4,9/16,1$. Multiplicar cada lista por $1/4$ da $L=7/32$ y $U=15/32$. La integral existente de $x^2$ queda entre ambas cotas.

### Microcontrol 060

[]{#MA-MIC-ANM-01-023-060}

[]{#MA-MSOL-ANM-01-023-060}

**Pregunta.** ¿Cuál es su punto medio y error certificado?

**Solución.** El centro de esas cotas es $(7/32+15/32)/2=11/32$. La mitad de su diferencia es $1/8$, así el error certificado no supera $1/8$. Frente al valor $1/3$, el error real es $|11/32-1/3|=1/96$. El centro de las cotas difiere de la suma con etiquetas medias.

### Microcontrol 061

[]{#MA-MIC-ANM-01-023-061}

[]{#MA-MSOL-ANM-01-023-061}

**Pregunta.** ¿Qué n certifica error medio menor que1/100?

**Solución.** La brecha uniforme es $1/n$, así el centro de las cotas tiene error a lo sumo $1/(2n)$. Para garantizar error estrictamente menor que $1/100$ mediante ese certificado basta $n>50$, por ejemplo $n=51$. Una suma etiquetada arbitraria sólo recibe del encierro la cota $1/n$.

### Microcontrol 062

[]{#MA-MIC-ANM-01-023-062}

[]{#MA-MSOL-ANM-01-023-062}

**Pregunta.** ¿Qué brecha tiene el pico con nodos1/2±r?

**Solución.** En la partición con nodos $0,1/2-r,1/2,1/2+r,1$, los ínfimos son cero. Las dos piezas adyacentes a $1/2$ contienen el pico, tienen supremo uno y anchura $r$; las otras tienen supremo cero. Por ello $L=0$, $U=2r$ y $G=2r$.

### Microcontrol 063

[]{#MA-MIC-ANM-01-023-063}

[]{#MA-MSOL-ANM-01-023-063}

**Pregunta.** ¿El pico integrable tiene alguna partición de brecha cero?

**Solución.** Toda partición cubre $1/2$ con alguna pieza cerrada de anchura positiva. Esa pieza contiene también una entrada distinta del pico, donde la función vale cero. Su oscilación es uno y aporta una cantidad positiva a la brecha. Aun así, las particiones que encierran el pico en longitud $2r$ prueban integral cero al hacer $r$ arbitrariamente pequeño.

### Microcontrol 064

[]{#MA-MIC-ANM-01-023-064}

[]{#MA-MSOL-ANM-01-023-064}

**Pregunta.** ¿Qué impide integrar una función que toma0 y1 en toda pieza?

**Solución.** Si cada pieza no degenerada contiene alturas cero y uno y la función sólo toma esos valores, todos los ínfimos son cero y todos los supremos uno. Así $L(f,P)=0$ y $U(f,P)=\sum_i\Delta_i=b-a$ para toda partición. Como $a<b$, la brecha fija positiva impide el criterio y las integrales inferior y superior no coinciden.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)
