---
content-id: MA-BCH-0293
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-022-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 22
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C22_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §22.1 — Un intervalo convertido en datos finitos

### Microcontrol 001

[]{#MA-MIC-ANM-01-022-001}

[]{#MA-MSOL-ANM-01-022-001}

[]{#MA-SEC-ANM-01-022-001}

**Pregunta.** ¿Qué datos exige una partición de $[a,b]$?

**Solución.** Una lista finita estrictamente creciente con primer nodo $a$, último $b$ y al menos una pieza, bajo $a<b$.

Escribimos $a=x_0<x_1<\cdots<x_n=b$ con $n\ge1$. La lista proporciona exactamente $n$ piezas y ninguna tiene anchura cero. Para comprobar una partición hay que revisar extremos y todas las comparaciones consecutivas.

### Microcontrol 002

[]{#MA-MIC-ANM-01-022-002}

[]{#MA-MSOL-ANM-01-022-002}

**Pregunta.** ¿Son reales los índices?

**Solución.** No: son naturales. Los nodos y las anchuras son reales; cuando se multiplica por un índice se usa su copia real.

El índice identifica una posición de la lista; el nodo es la coordenada que ocupa esa posición. En $x_i=a+i(b-a)/n$, las operaciones de coordenadas son reales y utilizan las copias reales de $i$ y $n$. Como $n\ge1$, su denominador real es positivo.

### Microcontrol 003

[]{#MA-MIC-ANM-01-022-003}

[]{#MA-MSOL-ANM-01-022-003}

**Pregunta.** ¿Por qué una anchura es positiva?

**Solución.** Porque $x_{i-1}<x_i$, por lo que $x_i-x_{i-1}>0$.

La positividad permite usar la anchura como peso de una altura sin invertir desigualdades. Un nodo repetido daría peso cero y violaría el contrato de partición. Una pareja en orden inverso daría anchura negativa y tampoco sería una pieza válida.

### Microcontrol 004

[]{#MA-MIC-ANM-01-022-004}

[]{#MA-MSOL-ANM-01-022-004}

**Pregunta.** ¿Cuánto suman las anchuras?

**Solución.** $b-a$, por telescopía finita: cada nodo interior aparece una vez positivo y otra negativo.

La suma es $(x_1-x_0)+\cdots+(x_n-x_{n-1})$. Los términos interiores se cancelan y quedan $x_n-x_0=b-a$. Esta identidad convierte cotas locales por pieza en cotas globales por longitud.

### Microcontrol 005

[]{#MA-MIC-ANM-01-022-005}

[]{#MA-MSOL-ANM-01-022-005}

**Pregunta.** ¿Son disjuntos los intervalos cerrados vecinos?

**Solución.** No: comparten su nodo. Sus interiores sí son disjuntos.

Las piezas $[x_{i-1},x_i]$ y $[x_i,x_{i+1}]$ contienen ambas a $x_i$. Al quitar sus extremos, sus interiores no se intersectan. Una suma asigna un término a cada pieza y conserva esa convención aunque alguna etiqueta sea el nodo compartido.

### Microcontrol 006

[]{#MA-MIC-ANM-01-022-006}

[]{#MA-MSOL-ANM-01-022-006}

**Pregunta.** ¿Cómo se localiza una entrada $t<b$?

**Solución.** Con el menor $j$ que cumple $t<x_j$; entonces $x_{j-1}\le t<x_j$.

El último índice satisface $t<x_n=b$, así existe un índice admisible. El menor de ellos es positivo y su anterior no satisface la desigualdad, dando $x_{j-1}\le t$. Para $t=b$ se usa directamente la última pieza.

### Microcontrol 007

[]{#MA-MIC-ANM-01-022-007}

[]{#MA-MSOL-ANM-01-022-007}

**Pregunta.** ¿Cuáles son las anchuras de $(0,1/4,1)$?

**Solución.** $1/4$ y $3/4$; suman1 y no son iguales.

Restar nodos consecutivos da $1/4-0=1/4$ y $1-1/4=3/4$. La suma es uno, pero la pieza más ancha mide tres cuartos. Más adelante esa mayor anchura, y no el promedio, determinará la malla.

### Microcontrol 008

[]{#MA-MIC-ANM-01-022-008}

[]{#MA-MSOL-ANM-01-022-008}

**Pregunta.** ¿Admite el contrato inicial $a=b$?

**Solución.** No. Exige $a<b$; una convención degenerada se debe declarar separadamente.

Una lista estrictamente creciente con al menos una pieza no puede empezar y terminar en el mismo real. Las pruebas que dividen la longitud o toman máximos de anchuras se desarrollan bajo $a<b$. El segmento degenerado necesita sus propias convenciones.

## §22.2 — Refinar conservando los cortes

### Microcontrol 009

[]{#MA-MIC-ANM-01-022-009}

[]{#MA-MSOL-ANM-01-022-009}

[]{#MA-SEC-ANM-01-022-002}

**Pregunta.** ¿Qué significa $P\preceq Q$?

**Solución.** $V(P)\subseteq V(Q)$: $Q$ conserva todos los nodos de $P$.

Todos los cortes antiguos aparecen en la lista nueva, quizá con índices diferentes. Los cortes adicionales subdividen piezas y permiten comparar contribuciones dentro de sus padres. La definición se formula mediante conjuntos de nodos, no mediante igualdad de posiciones en las listas.

### Microcontrol 010

[]{#MA-MIC-ANM-01-022-010}

[]{#MA-MSOL-ANM-01-022-010}

**Pregunta.** ¿Es una partición refinamiento de sí misma?

**Solución.** Sí. La inclusión permite igualdad; sólo el refinamiento propio exige un nodo nuevo.

La inclusión $V(P)\subseteq V(P)$ siempre vale. El símbolo de refinamiento expresa conservar cortes, lo que incluye conservarlos todos sin añadir ninguno. La condición de ser propio se declara aparte como una inclusión estricta.

### Microcontrol 011

[]{#MA-MIC-ANM-01-022-011}

[]{#MA-MSOL-ANM-01-022-011}

**Pregunta.** ¿Por qué la relación es transitiva?

**Solución.** La inclusión de nodos es transitiva.

Si todos los nodos de $P$ están en $Q$ y todos los de $Q$ en $R$, cada nodo de $P$ está en $R$. Ordenar las listas no altera sus conjuntos de nodos. Por ello $P\preceq R$ con el mismo intervalo de extremos.

### Microcontrol 012

[]{#MA-MIC-ANM-01-022-012}

[]{#MA-MSOL-ANM-01-022-012}

**Pregunta.** ¿Dónde se inserta un punto nuevo $t$?

**Solución.** Entre $x_{j-1}$ y $x_j$, donde $j$ es el menor índice con $t<x_j$.

Si el punto aún no es nodo, la localización proporciona desigualdades estrictas $x_{j-1}<t<x_j$. Insertarlo allí conserva la lista creciente y divide una única pieza. Los otros nodos y anchuras permanecen como estaban.

### Microcontrol 013

[]{#MA-MIC-ANM-01-022-013}

[]{#MA-MSOL-ANM-01-022-013}

**Pregunta.** ¿Qué sucede si el punto ya era nodo?

**Solución.** No se modifica la partición. Repetirlo violaría crecimiento estricto.

Cada coordenada aparece una sola vez en una lista estrictamente creciente. Insertar otra copia crearía dos nodos consecutivos iguales y una anchura cero. En el caso de un nodo existente, la operación de inserción devuelve la partición original.

### Microcontrol 014

[]{#MA-MIC-ANM-01-022-014}

[]{#MA-MSOL-ANM-01-022-014}

**Pregunta.** ¿Cuántas piezas añade una inserción propia?

**Solución.** Una: reemplaza una pieza por dos.

Una pieza $[u,v]$ pasa a las dos $[u,t]$ y $[t,v]$, ambas de anchura positiva. Su número aumenta de uno a dos. La longitud se conserva porque $(t-u)+(v-t)=v-u$.

### Microcontrol 015

[]{#MA-MIC-ANM-01-022-015}

[]{#MA-MSOL-ANM-01-022-015}

**Pregunta.** ¿Qué nodos tiene el menor refinamiento común?

**Solución.** La unión finita $V(P)\cup V(Q)$, ordenada sin repeticiones.

La unión contiene cada corte de las dos listas y sigue siendo finita. Ordenarla sin repeticiones produce una partición de los mismos extremos. Cualquier otro refinamiento común contiene también esa unión, que explica su minimalidad.

### Microcontrol 016

[]{#MA-MIC-ANM-01-022-016}

[]{#MA-MSOL-ANM-01-022-016}

**Pregunta.** ¿Reemplazar $1/2$ por $1/3$ es refinar?

**Solución.** No en general: se pierde el nodo antiguo $1/2$.

La nueva lista puede tener incluso menor malla y aun así perder un corte antiguo. Refinamiento exige conservación de nodos, no sólo una mejora numérica de resolución. Para comparar ambas listas se ordena la unión de sus nodos.

## §22.3 — La malla mide el peor intervalo

### Microcontrol 017

[]{#MA-MIC-ANM-01-022-017}

[]{#MA-MSOL-ANM-01-022-017}

[]{#MA-SEC-ANM-01-022-003}

**Pregunta.** ¿Qué mide la malla?

**Solución.** La máxima anchura de las piezas, no la anchura media ni su número.

Una pieza grande puede permitir etiquetas bastante alejadas dentro de ella. Por eso se usa la peor anchura para controlar todas las etiquetas simultáneamente. El número de piezas sólo ofrece una anchura media y puede ocultar esa pieza grande.

### Microcontrol 018

[]{#MA-MIC-ANM-01-022-018}

[]{#MA-MSOL-ANM-01-022-018}

**Pregunta.** ¿Por qué existe ese máximo?

**Solución.** Es el máximo de una lista finita no vacía de reales, construido por comparaciones sucesivas.

La lista de anchuras tiene $n\ge1$ miembros positivos. Se empieza por la primera y se compara sucesivamente con las demás, conservando la mayor. El resultado es una de las anchuras y domina a todas, con lo que define la malla.

### Microcontrol 019

[]{#MA-MIC-ANM-01-022-019}

[]{#MA-MSOL-ANM-01-022-019}

**Pregunta.** ¿Qué pasa con la malla al refinar?

**Solución.** No aumenta: cada pieza hija está contenida en un padre.

Entre nodos consecutivos nuevos no puede quedar un nodo antiguo, pues éste también sería nuevo. Cada pieza nueva queda entonces dentro de una pieza antigua y su longitud no la supera. Tomar el máximo conserva la desigualdad de mallas.

### Microcontrol 020

[]{#MA-MIC-ANM-01-022-020}

[]{#MA-MSOL-ANM-01-022-020}

**Pregunta.** ¿Un refinamiento propio reduce estrictamente la malla?

**Solución.** No. Puede dejar intacta una pieza de anchura máxima.

Si se subdivide una pieza pequeña y queda otra de longitud máxima sin tocar, el máximo sigue siendo el mismo. La relación de mallas sólo asegura desigualdad no estricta. Para reducirla de verdad hay que controlar todas las piezas más anchas.

### Microcontrol 021

[]{#MA-MIC-ANM-01-022-021}

[]{#MA-MSOL-ANM-01-022-021}

**Pregunta.** ¿Cuál es la malla uniforme de $n$ piezas?

**Solución.** $(b-a)/n$, con $n\ge1$ y copia real positiva.

Los nodos uniformes son $x_i=a+i(b-a)/n$. Restar dos consecutivos elimina $a$ y da siempre $(b-a)/n$. Como todas las anchuras coinciden, su máximo tiene ese mismo valor.

### Microcontrol 022

[]{#MA-MIC-ANM-01-022-022}

[]{#MA-MSOL-ANM-01-022-022}

**Pregunta.** ¿Cómo se logra malla menor que $\delta$?

**Solución.** Arquimedianidad: elegir $n>(b-a)/\delta$ y usar la partición uniforme.

El cociente $(b-a)/\delta$ es real positivo. Arquimedianidad proporciona un natural mayor y por ello al menos uno. Dividir la longitud por ese número positivo da una malla estrictamente menor que la escala pedida.

### Microcontrol 023

[]{#MA-MIC-ANM-01-022-023}

[]{#MA-MSOL-ANM-01-022-023}

**Pregunta.** ¿Por qué muchas piezas no bastan?

**Solución.** Se puede conservar una pieza de anchura1/2 y subdividir sólo el resto; la malla sigue siendo1/2.

Subdividir únicamente $[1/2,1]$ puede aumentar indefinidamente el número de piezas. La pieza $[0,1/2]$ sigue aportando al máximo su longitud fija. Esa cadena de refinamientos muestra que aumentar piezas no garantiza malla tendente a cero.

### Microcontrol 024

[]{#MA-MIC-ANM-01-022-024}

[]{#MA-MSOL-ANM-01-022-024}

**Pregunta.** ¿Cómo se conserva una partición dada y se reduce su malla?

**Solución.** Se toma su refinamiento común con una uniforme suficientemente fina.

El refinamiento común conserva todos los nodos antiguos y todos los de la uniforme elegida. Su malla no supera la de esta última por la propiedad de hijos y padres. Así cumple a la vez conservación de datos y resolución prescrita.

## §22.4 — Etiquetas y acumulación firmada

### Microcontrol 025

[]{#MA-MIC-ANM-01-022-025}

[]{#MA-MSOL-ANM-01-022-025}

[]{#MA-SEC-ANM-01-022-004}

**Pregunta.** ¿Qué es una etiqueta?

**Solución.** Un punto dado $\xi_i\in[x_{i-1},x_i]$ para cada índice de pieza.

La etiqueta indica en qué entrada se toma la altura que multiplica la anchura. Puede ser interior o cualquiera de los dos extremos de su pieza. La familia tiene un dato por cada índice de pieza, aunque algunas coordenadas se repitan.

### Microcontrol 026

[]{#MA-MIC-ANM-01-022-026}

[]{#MA-MSOL-ANM-01-022-026}

**Pregunta.** ¿Pueden repetirse etiquetas?

**Solución.** Sí: un nodo compartido puede etiquetar las dos piezas vecinas.

El punto $x_i$ pertenece a sus dos piezas vecinas y puede elegirse para ambas. Las dos contribuciones siguen siendo términos distintos, con sus propias anchuras. Este hecho será importante al contar el efecto de valores excepcionales en nodos.

### Microcontrol 027

[]{#MA-MIC-ANM-01-022-027}

[]{#MA-MSOL-ANM-01-022-027}

**Pregunta.** ¿Cuál es la suma etiquetada?

**Solución.** $S(f;P,\xi)=\sum_i f(\xi_i)\Delta_i$, una suma real finita.

Cada término combina una evaluación real definida de $f$ con una anchura real positiva. El número de términos es finito y la suma se calcula con operaciones reales ordinarias. Todavía no se ha pasado a un límite de particiones.

### Microcontrol 028

[]{#MA-MIC-ANM-01-022-028}

[]{#MA-MSOL-ANM-01-022-028}

**Pregunta.** ¿Una suma finita requiere que $f$ sea acotada?

**Solución.** No para existir; sí se necesitan hipótesis adicionales para controlar uniformemente todas las sumas.

Una lista finita de evaluaciones reales siempre tiene suma real. Una función no acotada puede producir sumas cada vez mayores al cambiar etiquetas o particiones. La existencia de una suma particular y el control universal de toda la familia son obligaciones diferentes.

### Microcontrol 029

[]{#MA-MIC-ANM-01-022-029}

[]{#MA-MSOL-ANM-01-022-029}

**Pregunta.** ¿Qué suma produce la constante $c$?

**Solución.** $c(b-a)$, cualquiera sea la partición y sus etiquetas.

Todos los términos tienen altura $c$, así se factoriza $c\sum_i\Delta_i$. La identidad de longitudes da $c(b-a)$. Esto vale también si $c$ es negativo y para cualquier elección admisible de etiquetas.

### Microcontrol 030

[]{#MA-MIC-ANM-01-022-030}

[]{#MA-MSOL-ANM-01-022-030}

**Pregunta.** ¿Qué significa una contribución negativa?

**Solución.** Altura negativa por anchura positiva: acumulación firmada, no área geométrica negativa.

La anchura nunca es negativa en una partición válida. El signo de cada término procede únicamente del valor de la función. Alturas de signos opuestos pueden cancelarse al sumar, mientras las áreas geométricas de sus regiones se sumarían como magnitudes.

### Microcontrol 031

[]{#MA-MIC-ANM-01-022-031}

[]{#MA-MSOL-ANM-01-022-031}

**Pregunta.** ¿Qué datos se fijan al comparar $S(f)$ y $S(g)$?

**Solución.** La misma partición y las mismas etiquetas; $f\le g$ en el intervalo da el orden de sus sumas.

Con los mismos datos, la comparación se realiza término a término en cada entrada $\xi_i$. La anchura positiva conserva el sentido de $f(\xi_i)\le g(\xi_i)$. Sumar esas desigualdades prueba el orden de las sumas.

### Microcontrol 032

[]{#MA-MIC-ANM-01-022-032}

[]{#MA-MSOL-ANM-01-022-032}

**Pregunta.** ¿Qué cota da $|f|\le M$?

**Solución.** $|S|\le M\sum_i\Delta_i=M(b-a)$, sin máximo alcanzado.

La triangular da $|\sum f(\xi_i)\Delta_i|\le\sum|f(\xi_i)|\Delta_i$. Sustituir la barrera y sumar longitudes produce $M(b-a)$. Basta que la barrera valga en todas las entradas; ninguna debe alcanzarla.

## §22.5 — Lo que un cambio de etiquetas puede alterar

### Microcontrol 033

[]{#MA-MIC-ANM-01-022-033}

[]{#MA-MSOL-ANM-01-022-033}

[]{#MA-SEC-ANM-01-022-005}

**Pregunta.** ¿Cómo se controla cambiar sólo etiquetas?

**Solución.** Por $\sum_i |f(\xi_i)-f(\eta_i)|\Delta_i$, usando resta y triangular.

Las anchuras quedan fijas, de modo que restar las dos sumas sólo cambia sus alturas. La triangular limita el error total por la suma de errores locales ponderados. Cada estimación por pieza debe proteger las dos etiquetas que finalmente se usen.

### Microcontrol 034

[]{#MA-MIC-ANM-01-022-034}

[]{#MA-MSOL-ANM-01-022-034}

**Pregunta.** ¿Qué exige una cota local $d_i$?

**Solución.** Que controle todos los pares de entradas de la pieza, no sólo los dos valores muestreados.

Las etiquetas todavía pueden cambiar dentro de toda la pieza. Por eso se necesita $|f(u)-f(v)|\le d_i$ para cualesquiera $u,v$ de ella. Comprobar únicamente una pareja concreta dejaría otras etiquetas fuera del certificado.

### Microcontrol 035

[]{#MA-MIC-ANM-01-022-035}

[]{#MA-MSOL-ANM-01-022-035}

**Pregunta.** ¿Qué cota da Lipschitz para dos etiquetas de una pieza?

**Solución.** $L\Delta_i$, porque ambas distan a lo sumo su anchura.

La distancia entre dos puntos del mismo intervalo cerrado no supera su longitud. Aplicar Lipschitz a esa pareja da $|f(\xi_i)-f(\eta_i)|\le L\Delta_i$. Multiplicar por la anchura introduce el término cuadrático $L\Delta_i^2$.

### Microcontrol 036

[]{#MA-MIC-ANM-01-022-036}

[]{#MA-MSOL-ANM-01-022-036}

**Pregunta.** ¿Por qué $\sum_i\Delta_i^2\le\|P\|(b-a)$?

**Solución.** Cada $\Delta_i\le\|P\|$ y es positiva; multiplicar por $\Delta_i$ y sumar.

El máximo domina cada anchura y todas son positivas. Por ello $\Delta_i^2\le\|P\|\Delta_i$. Sumar y usar telescopía de longitudes obtiene la cota por malla y longitud total.

### Microcontrol 037

[]{#MA-MIC-ANM-01-022-037}

[]{#MA-MSOL-ANM-01-022-037}

**Pregunta.** ¿Qué controla comparar con un refinamiento?

**Solución.** $L\|P\|(b-a)$, por reescribir cada contribución antigua en las piezas hijas.

Las longitudes hijas suman la del padre y permiten repetir su altura antigua en todos los términos hijos. Cada etiqueta hija permanece dentro del padre y se compara con la antigua mediante su anchura. La misma cota cuadrática por padres produce el certificado.

### Microcontrol 038

[]{#MA-MIC-ANM-01-022-038}

[]{#MA-MSOL-ANM-01-022-038}

**Pregunta.** ¿Cómo se comparan particiones diferentes?

**Solución.** Por su refinamiento común y triangular; cota $L(b-a)(\|P\|+\|Q\|)$.

Una tercera suma en el refinamiento común se usa como puente entre las dos anteriores. Cada comparación con ese puente tiene una barrera de su propia malla original. La triangular suma ambas barreras y elimina la dependencia de etiquetas.

### Microcontrol 039

[]{#MA-MIC-ANM-01-022-039}

[]{#MA-MSOL-ANM-01-022-039}

**Pregunta.** ¿Refinar ordena las sumas etiquetadas?

**Solución.** No. Para $x$, una suma1/2 puede dar1/4 o3/4 en el mismo refinamiento, según etiquetas.

La conservación de nodos no decide qué alturas se tomarán en las piezas nuevas. Etiquetas izquierdas o derechas pueden desplazar la suma en sentidos opuestos. Las cotas de error controlan esa variación sin prometer monotonía.

### Microcontrol 040

[]{#MA-MIC-ANM-01-022-040}

[]{#MA-MSOL-ANM-01-022-040}

**Pregunta.** ¿Independencia de etiquetas ya prueba existencia de integral?

**Solución.** No por sí sola; todavía se necesita un número que cumpla el contrato universal.

Que las sumas de una misma partición sean cercanas sólo relaciona miembros de una familia. El contrato de integral pide además un real candidato al que todas se aproximen con el orden de tolerancias declarado. Existencia de ese valor requiere un argumento propio.

## §22.6 — Escalones: exactitud finita y nodos excepcionales

### Microcontrol 041

[]{#MA-MIC-ANM-01-022-041}

[]{#MA-MSOL-ANM-01-022-041}

[]{#MA-SEC-ANM-01-022-006}

**Pregunta.** ¿Cómo se calcula la acumulación de un escalón?

**Solución.** $A=\sum_j c_j(z_j-z_{j-1})$ con constantes interiores dadas.

Cada intervalo entre cortes aporta su constante interior multiplicada por la longitud. La lista de cortes y constantes es finita y determina un real. Los valores asignados únicamente en los nodos no aparecen en esa fórmula de acumulación.

### Microcontrol 042

[]{#MA-MIC-ANM-01-022-042}

[]{#MA-MSOL-ANM-01-022-042}

**Pregunta.** ¿Por qué insertar un corte conserva $A$?

**Solución.** Se copia la altura y las dos anchuras suman la original.

El corte nuevo cae dentro de una región de altura constante $c$. Sustituir $c(v-u)$ por $c(t-u)+c(v-t)$ no cambia el resultado por distributividad. Repetir finitamente esta operación conserva la acumulación al refinar.

### Microcontrol 043

[]{#MA-MIC-ANM-01-022-043}

[]{#MA-MSOL-ANM-01-022-043}

**Pregunta.** ¿Cómo se comparan dos representaciones del mismo escalón?

**Solución.** En el refinamiento común las constantes interiores coinciden; sumar allí da el mismo $A$.

En cada interior del refinamiento común, ambas representaciones describen los mismos valores de la función. Sus constantes coinciden y las contribuciones son iguales. La invariancia por inserciones relaciona después esa suma común con las dos originales.

### Microcontrol 044

[]{#MA-MIC-ANM-01-022-044}

[]{#MA-MSOL-ANM-01-022-044}

**Pregunta.** ¿Un valor aislado añade anchura a $A$?

**Solución.** No. Un nodo es un punto sin intervalo de anchura positiva.

La fórmula del escalón sólo asigna pesos a intervalos de longitud positiva. Modificar un valor puntual no crea uno de esos intervalos. Una suma etiquetada sí puede tomar esa altura puntual, de modo que su efecto debe estimarse aparte.

### Microcontrol 045

[]{#MA-MIC-ANM-01-022-045}

[]{#MA-MSOL-ANM-01-022-045}

**Pregunta.** ¿Cualquier suma etiquetada coincide exactamente con $A$?

**Solución.** No. Puede usar etiquetas en nodos excepcionales o piezas que cruzan un salto.

Una etiqueta en un corte puede leer un valor distinto de las constantes de ambos lados. Una pieza que cruza un salto puede usar una altura de un solo lado para toda su anchura. El certificado universal controla esas situaciones sin afirmar exactitud de cada suma.

### Microcontrol 046

[]{#MA-MIC-ANM-01-022-046}

[]{#MA-MSOL-ANM-01-022-046}

**Pregunta.** ¿Cuántas piezas cerradas contienen un punto fijo?

**Solución.** A lo sumo dos; en extremos a lo sumo una.

Un punto interior a una pieza sólo pertenece a ella. Si coincide con un nodo interior, pertenece a las dos vecinas; los demás intervalos quedan separados por nodos. En los bordes del segmento sólo existe una pieza vecina.

### Microcontrol 047

[]{#MA-MIC-ANM-01-022-047}

[]{#MA-MSOL-ANM-01-022-047}

**Pregunta.** ¿Qué cota da modificar $k$ puntos por diferencias de tamaño $D$?

**Solución.** Diferencia de sumas $\le2kD\|P\|$ para la misma partición y etiquetas.

Cada punto modificado puede afectar como máximo dos términos de una suma con etiquetas dadas. Hay por ello a lo sumo $2k$ contribuciones distintas que requieren cota. Cada una tiene magnitud a lo sumo $D\|P\|$, dando el resultado por triangular.

### Microcontrol 048

[]{#MA-MIC-ANM-01-022-048}

[]{#MA-MSOL-ANM-01-022-048}

**Pregunta.** ¿Qué certificado universal obtuvo el escalón?

**Solución.** $|S-A|\le4B(m+1)\|P\|$, contando padres que tocan sus nodos.

Los padres que no tocan cortes del escalón tienen altura constante y contribución exacta. Los que sí los tocan son finitos y su longitud total se acota por el número de nodos y la malla. La barrera $2B$ de diferencias de alturas completa el certificado.

## §22.7 — Un límite que todas las etiquetas deben compartir

### Microcontrol 049

[]{#MA-MIC-ANM-01-022-049}

[]{#MA-MSOL-ANM-01-022-049}

[]{#MA-SEC-ANM-01-022-007}

**Pregunta.** ¿En qué orden se eligen los datos del límite?

**Solución.** Primero $I$, después cada tolerancia $\varepsilon$, luego $\delta$, y sólo entonces todas las particiones y etiquetas.

El candidato integral pertenece al enunciado antes de pedir precisiones. El radio responde a cada precisión y después debe proteger cualquier partición suficientemente fina con cualquier etiqueta admisible. Ese orden impide elegir una escala que excluya sólo el objeto ya examinado.

### Microcontrol 050

[]{#MA-MIC-ANM-01-022-050}

[]{#MA-MSOL-ANM-01-022-050}

**Pregunta.** ¿Puede $\delta$ depender de las etiquetas?

**Solución.** No. Debe servir para todas las etiquetas de todas las particiones de malla menor.

Las etiquetas son parte de los datos universalmente cuantificados tras fijar el radio. Una escala que se adapte a ellas no demostraría independencia de sus elecciones. La malla controla la separación de entradas dentro de todas las piezas y ofrece la escala común.

### Microcontrol 051

[]{#MA-MIC-ANM-01-022-051}

[]{#MA-MSOL-ANM-01-022-051}

**Pregunta.** ¿Por qué el contrato no es vacío?

**Solución.** Existen particiones uniformes con malla menor que cualquier radio positivo.

Arquimedianidad permite una uniforme de anchura menor que cualquier radio dado. Sus etiquetas izquierdas son explícitas y válidas. Así siempre existe alguna suma a la que aplicar dos candidatos de límite, evitando una unicidad vacía.

### Microcontrol 052

[]{#MA-MIC-ANM-01-022-052}

[]{#MA-MSOL-ANM-01-022-052}

**Pregunta.** ¿Cómo se prueba unicidad?

**Solución.** Si $d=|I-J|>0$, una suma dentro de $d/3$ de ambos daría $d<2d/3$ por triangular.

Se piden radios a ambos candidatos con la misma tolerancia $d/3$ y se toma su mínimo. Una uniforme fina y etiquetas explícitas producen una suma que cumple los dos errores. La triangular fuerza una distancia entre candidatos menor que ella misma, contradicción.

### Microcontrol 053

[]{#MA-MIC-ANM-01-022-053}

[]{#MA-MSOL-ANM-01-022-053}

**Pregunta.** ¿Qué radio sirve si $|S-I|\le C\|P\|$ y $C>0$?

**Solución.** $\delta=\varepsilon/C$; malla estrictamente menor da error estrictamente menor que $\varepsilon$.

La barrera es común a toda la familia de sumas. Si la malla es estrictamente menor que $\varepsilon/C$, el producto de barrera y malla queda estrictamente bajo el desafío. El radio no depende de la partición ni de sus etiquetas.

### Microcontrol 054

[]{#MA-MIC-ANM-01-022-054}

[]{#MA-MSOL-ANM-01-022-054}

**Pregunta.** ¿Qué ocurre si $C=0$?

**Solución.** Todas las sumas valen $I$; cualquier radio positivo sirve.

La desigualdad $|S-I|\le0$ obliga a igualdad para cada suma. Ninguna reducción adicional de malla es necesaria para aproximar ese valor. Se trata este caso antes de introducir una fórmula que dividiría por la barrera nula.

### Microcontrol 055

[]{#MA-MIC-ANM-01-022-055}

[]{#MA-MSOL-ANM-01-022-055}

**Pregunta.** ¿Qué implica integrabilidad para una sucesión dada de mallas que tienden a cero?

**Solución.** Sus sumas etiquetadas tienden a $I$ para cualquier familia dada de etiquetas.

Para una tolerancia se obtiene primero el radio universal. La convergencia de mallas proporciona después un índice a partir del cual todas las particiones dadas lo cumplen. Sus etiquetas pueden variar porque el contrato ya las controla a todas.

### Microcontrol 056

[]{#MA-MIC-ANM-01-022-056}

[]{#MA-MSOL-ANM-01-022-056}

**Pregunta.** ¿Ya se probó integrabilidad de toda continua?

**Solución.** No. Aquí se probaron escalones y ejemplos con certificados; C23 construirá resultados generales.

El escalón y los polinomios examinados disponen de candidatos explícitos y certificados de todas sus sumas. El resultado general para continuas aún necesita construir ese candidato. La proximidad entre sumas y su acotación son herramientas, pero aquí no se sustituyen por un teorema todavía pendiente.

## §22.8 — Certificados antes de fórmulas de integración

### Microcontrol 057

[]{#MA-MIC-ANM-01-022-057}

[]{#MA-MSOL-ANM-01-022-057}

[]{#MA-SEC-ANM-01-022-008}

**Pregunta.** ¿Qué suma media da $x$ en $[a,b]$?

**Solución.** $(b^2-a^2)/2$ exactamente, por telescopía de cuadrados.

En una pieza $[u,v]$, su altura media $(u+v)/2$ multiplicada por $v-u$ vale $(v^2-u^2)/2$. Al sumar se cancelan los cuadrados de nodos interiores. Queda un candidato exacto para todas las particiones con esas etiquetas medias.

### Microcontrol 058

[]{#MA-MIC-ANM-01-022-058}

[]{#MA-MSOL-ANM-01-022-058}

**Pregunta.** ¿Qué cota controla otras etiquetas para $x$?

**Solución.** $(b-a)\|P\|/2$, pues la distancia al punto medio es a lo sumo media anchura.

Cualquier etiqueta está a distancia como máximo $(v-u)/2$ del medio de su pieza. Para la identidad esa distancia es también diferencia de alturas. Ponderar y sumar da media suma de cuadrados de anchuras, dominada por la malla y longitud.

### Microcontrol 059

[]{#MA-MIC-ANM-01-022-059}

[]{#MA-MSOL-ANM-01-022-059}

**Pregunta.** ¿Qué valor tiene $\alpha x+\beta$?

**Solución.** $\alpha(b^2-a^2)/2+\beta(b-a)$, por álgebra finita y el certificado del caso lineal.

La linealidad de sumas transforma el candidato del caso lineal y añade la acumulación exacta de la constante. La magnitud $|\alpha|$ multiplica su certificado de error. La altura constante no agrega error, cualquiera que sea su signo.

### Microcontrol 060

[]{#MA-MIC-ANM-01-022-060}

[]{#MA-MSOL-ANM-01-022-060}

**Pregunta.** ¿Qué identidad local controla $x^2$?

**Solución.** $(v^3-u^3)/3=(v-u)(u^2+uv+v^2)/3$.

La factorización del incremento cúbico permite compararlo con una media de tres alturas cuadráticas. Esa media queda entre las alturas de borde de una pieza no negativa. Al sumar los incrementos cúbicos se obtiene telescopía, que produce el candidato del cuadrado.

### Microcontrol 061

[]{#MA-MIC-ANM-01-022-061}

[]{#MA-MSOL-ANM-01-022-061}

**Pregunta.** ¿Qué cota universal certifica $1/3$?

**Solución.** $|S(x^2)-1/3|\le2\|P\|$ en $[0,1]$.

La diferencia local entre una altura etiquetada y la media cuadrática no supera dos veces la anchura. Tras ponderar, el error es a lo sumo $2\Delta_i^2$. Sumar en $[0,1]$ produce la barrera $2\|P\|$ para cualquier familia de etiquetas.

### Microcontrol 062

[]{#MA-MIC-ANM-01-022-062}

[]{#MA-MSOL-ANM-01-022-062}

**Pregunta.** ¿Cuáles son las sumas izquierda y derecha para $n=4$?

**Solución.** $7/32$ y $15/32$, respectivamente.

Cada anchura mide un cuarto y cada altura de borde es un cuadrado de múltiplos de un cuarto. El denominador de las contribuciones es por ello sesenta y cuatro. Las listas de cuadrados empiezan en cero para la izquierda y en uno para la derecha.

### Microcontrol 063

[]{#MA-MIC-ANM-01-022-063}

[]{#MA-MSOL-ANM-01-022-063}

**Pregunta.** ¿La etiqueta media es exacta para $x^2$?

**Solución.** No. La suma uniforme es $1/3-1/(12n^2)$.

El error de puntos medios mantiene un término positivo que sólo desaparece al aumentar indefinidamente la resolución. Para cualquier natural finito $n\ge1$, $1/(12n^2)>0$. La exactitud media del caso lineal no se transfiere al cuadrado.

### Microcontrol 064

[]{#MA-MIC-ANM-01-022-064}

[]{#MA-MSOL-ANM-01-022-064}

**Pregunta.** ¿Qué se requiere para error menor que $1/100$ mediante $2\|P\|$?

**Solución.** Malla menor que1/200; en uniforme, un natural $n>200$.

La condición estricta $2\|P\|<1/100$ se satisface con malla menor que $1/200$. En una uniforme de $[0,1]$ la malla es $1/n$, así se toma un natural mayor que doscientos. Esa elección protege todas las etiquetas, no sólo las medias.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Ejercicios](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-22-partir-refinar-acumular-microcontroles.html)

