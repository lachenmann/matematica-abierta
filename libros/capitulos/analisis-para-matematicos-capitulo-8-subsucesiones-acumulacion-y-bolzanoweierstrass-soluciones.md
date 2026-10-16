---
content-id: MA-BCH-0236
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-008-SOLUCIONES
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
title: Soluciones — Capítulo 8
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C08_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html) · [Ejercicios](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-soluciones.html)

## 8.1. Mapas de selección

[]{#MA-EX-ANM-01-008-001}

[]{#MA-SOL-ANM-01-008-001}

[]{#MA-SEC-ANM-01-008-001}

Los mapas $\varphi$ y $\theta$ tienen incrementos dos y uno, respectivamente; son estrictamente crecientes. $\psi(k+1)-\psi(k)=2k+1>0$, también desde cero. Sus primeros valores seleccionados son, respectivamente, $(1,1/3,1/5)$, $(1,1/2,1/5)$ y $(1/6,1/7,1/8)$. En cambio, $\eta(0)=\eta(1)=0$, por lo que no es estrictamente creciente. El hecho de que $\eta$ sea no decreciente no satisface la definición: permite reutilizar un índice.

La distinción entre índices y alturas también se aprecia en la [figura 8.1](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f01).

## 8.2. Enumerar índices sin saltos ocultos

[]{#MA-EX-ANM-01-008-002}

[]{#MA-SOL-ANM-01-008-002}

La base existe por buen orden. En cada paso, $E$ no está contenido en el prefijo finito hasta $e_k$, de modo que el conjunto siguiente es no vacío y tiene mínimo. Los índices obtenidos crecen estrictamente y pertenecen a $E$, lo que prueba una inclusión. Para la otra, fija $m\in E$. Como $e_k\ge k$, existe un primer $j$ con $e_j\ge m$. Si $j=0$, la minimalidad de $e_0$ fuerza $e_0=m$. Si $j>0$, tenemos $e_{j-1}<m$, y $m$ era admisible al definir $e_j$; por eso $e_j\le m$, luego $e_j=m$. No basta decir que la lista es infinita: la regla del mínimo es lo que evita omitir un elemento de $E$.

## 8.3. Dos extracciones consecutivas

[]{#MA-EX-ANM-01-008-003}

[]{#MA-SOL-ANM-01-008-003}

Tanto $n$ como $k$ y $j$ recorren $\mathbb N$, pero indexan funciones distintas. El recorrido es $j\mapsto2j+1\mapsto3(2j+1)+2=6j+5$, así que $c_j=(6j+5)/(6j+6)$. Ambos mapas y su composición crecen estrictamente. Invertir el orden produciría $2(3j+2)+1=6j+5$ en este caso: sí conmutan. Esta igualdad particular se verifica por cálculo y no por una ley general. Por ejemplo, los selectores $2k$ y $k+1$ dan composiciones $2k+2$ y $2k+1$, distintas.

## 8.4. Misma imagen, distinta selección

[]{#MA-EX-ANM-01-008-004}

[]{#MA-SOL-ANM-01-008-004}

Toma $a_n=(-1)^n$, la identidad $\varphi(k)=k$ y el selector $\psi(k)=k+1$. Resultan $b_k=(-1)^k$ y $c_k=(-1)^{k+1}$. Ambos tienen imagen $\{-1,1\}$ porque ambas paridades aparecen, pero $b_0=1$ y $c_0=-1$. Por tanto las funciones son distintas. Comparar las imágenes elimina el orden y no permite recuperar la función.

## 8.5. Un umbral transportado y uno propio

[]{#MA-EX-ANM-01-008-005}

[]{#MA-SOL-ANM-01-008-005}

[]{#MA-SEC-ANM-01-008-002}

En $a$ se requiere $1/(n+1)<1/10$, equivalente a $n>9$; el menor umbral es $N=10$, pues en nueve hay igualdad. Para $b_k=3+1/(2k+2)$, la condición equivale a $k>4$, así que el menor umbral es $K=5$. El transporte general $K=N=10$ también sirve, pero no es mínimo. La estrictitud de la tolerancia explica ambos casos de frontera.

La [figura 8.2](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f02) permite comprobar por qué un punto de frontera obliga a retrasar el corte.

## 8.6. Intercalar dos límites iguales

[]{#MA-EX-ANM-01-008-006}

[]{#MA-SOL-ANM-01-008-006}

Fija $\varepsilon>0$ y toma umbrales $K_0,K_1$ para las dos selecciones. Sea $K=\max\{K_0,K_1\}$ y $N=2K$. Si $n\ge N$ es par, $n=2k$ con $k\ge K$; si es impar, $n=2k+1\ge2K$ obliga también a $k\ge K$, pues $k\le K-1$ daría $n\le2K-1$. En ambos casos $|a_n-L|<\varepsilon$. Se ha cubierto toda la cola, que era lo que una selección aislada no permitía hacer.

## 8.7. Una partición finita de índices

[]{#MA-EX-ANM-01-008-007}

[]{#MA-SOL-ANM-01-008-007}

La dirección directa aplica §8.2 a cada selector $k\mapsto mk+r$. Para la recíproca, fija $\varepsilon>0$ y elige un umbral $K_r$ para cada uno de los finitísimos residuos. Toma $K=\max_r K_r$ y $N=mK$. La división euclídea escribe cualquier $n\ge N$ como $n=mk+r$, con $0\le r<m$. Si $k<K$, entonces $n\le m(K-1)+(m-1)=mK-1$, contradicción. Luego $k\ge K_r$ y el término está a distancia menor que $\varepsilon$ de $L$. La finitud de la partición permite reunir los umbrales en un máximo.

## 8.8. Todos los términos salvo algunos

[]{#MA-EX-ANM-01-008-008}

[]{#MA-SOL-ANM-01-008-008}

Infinitud de índices seleccionados no implica control de todos los posteriores. El ejemplo $a_{2k}=0$, $a_{2k+1}=1$ refuta la afirmación: las dos paridades tienen límites diferentes. Para la reparación, supón $a_{\varphi(k)}\to0$ y que $E=\varphi(\mathbb N)$ tiene complemento finito. Dado $\varepsilon>0$, toma $K$ para la selección. El conjunto de índices omitidos junto con $\{\varphi(0),\ldots,\varphi(K-1)\}$ es finito. Escoge $N$ mayor que todos ellos, o cero si está vacío. Todo $n\ge N$ es $\varphi(k)$ con $k\ge K$; por tanto $|a_n|<\varepsilon$. Lo decisivo es que las excepciones sean finitas.

La [figura 8.2](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f02) recuerda qué términos quedan fuera del control de una selección.

## 8.9. Selección convergente de una monótona

[]{#MA-EX-ANM-01-008-009}

[]{#MA-SOL-ANM-01-008-009}

Supón primero que $a$ es no decreciente. Para un índice fijo $n$, los índices seleccionados son eventualmente mayores que $n$, por lo que $a_n\le a_{\varphi(k)}$ eventualmente. El orden de límites de C06 da $a_n\le L$. Dado $\varepsilon>0$, toma un término seleccionado $a_{\varphi(K)}>L-\varepsilon$ y pon $N=\varphi(K)$. Para $n\ge N$, la monotonía y la cota recién probada dan $L-\varepsilon<a_N\le a_n\le L$, así que $|a_n-L|<\varepsilon$. Si $a$ es no creciente, aplica el argumento a $-a$, cuya selección converge a $-L$, y cambia de signo. La dirección monótona propaga a toda una cola la información de un solo término seleccionado.

## 8.10. Una escala de radios basta

[]{#MA-EX-ANM-01-008-010}

[]{#MA-SOL-ANM-01-008-010}

[]{#MA-SEC-ANM-01-008-003}

La definición aplicada a los radios $1/(q+1)$ da una dirección. Para la otra, dados $\varepsilon>0$ y $N$, arquimedianidad permite escoger $q$ con $1/(q+1)<\varepsilon$. La hipótesis proporciona $n\ge N$ con error menor que ese radio, luego menor que $\varepsilon$. El orden es fijar la tolerancia, reducirla a una escala disponible y después elegir el índice.

## 8.11. Un destino prescrito con escapes

[]{#MA-EX-ANM-01-008-011}

[]{#MA-SOL-ANM-01-008-011}

Toma $a_{2k}=L$ y $a_{2k+1}=H$. Las selecciones constantes muestran que ambos son puntos secuenciales y la cota $\max\{|L|,|H|\}$ acredita acotación. Si $T\notin\{L,H\}$, el radio $r=\frac12\min\{|T-L|,|T-H|\}>0$ define una bola que no contiene ningún término. Así $T$ no satisface la condición de visitas. Como los dos destinos son distintos, la sucesión no converge.

## 8.12. Alejar los índices tanto como se quiera

[]{#MA-EX-ANM-01-008-012}

[]{#MA-SOL-ANM-01-008-012}

Elige $\varphi(0)$ como el mínimo índice al menos $h(0)$ con error menor que uno. Para el paso siguiente utiliza el corte $\max\{\varphi(k)+1,h(k+1)\}$ y radio $1/(k+2)$. La acumulación secuencial garantiza un testigo después de cada corte, por lo que el mínimo existe. Por inducción se cumplen ambas desigualdades y el crecimiento estricto. El control de errores prueba convergencia como en §8.3. No hace falta que $h$ sea monótona: el máximo incorpora por separado el corte heredado y la nueva exigencia.

## 8.13. El conjunto de destinos es cerrado

[]{#MA-EX-ANM-01-008-013}

[]{#MA-SOL-ANM-01-008-013}

Por C04 basta probar que todo punto adherente a $C$ pertenece a $C$. Sea $L$ adherente a $C$. Dados $\varepsilon>0$ y un corte $N$, elige $H\in C$ con $|H-L|<\varepsilon/2$. Como $H$ es punto secuencial de $a$, existe $n\ge N$ con $|a_n-H|<\varepsilon/2$. La desigualdad triangular da $|a_n-L|<\varepsilon$. Esto vale para cada tolerancia y cada corte, por lo que $L\in C$. Si $C$ es vacío, no tiene puntos adherentes y es cerrado. La estrategia consiste en gastar la mitad de la tolerancia en aproximar el centro y la otra mitad en aproximar un término.

## 8.14. Destinos de una partición finita

[]{#MA-EX-ANM-01-008-014}

[]{#MA-SOL-ANM-01-008-014}

Un punto secuencial de alguna $b^{(r)}$ es límite de una extracción de ella; componiendo selectores resulta límite de una extracción de $a$, así que es punto secuencial de $a$. Para la inclusión inversa, sea $L$ punto secuencial de $a$ y supón que no lo es de ninguna $b^{(r)}$. Para cada residuo existen $\varepsilon_r>0$ y $K_r$ tales que $|b^{(r)}_k-L|\ge\varepsilon_r$ si $k\ge K_r$. Toma $\varepsilon=\min_r\varepsilon_r>0$ y $N=m\max_r K_r$. La división euclídea y el argumento de cortes del ejercicio 8.7 muestran que todo $n\ge N$ tiene error al menos $\varepsilon$. Esto contradice que $L$ sea punto secuencial. La finitud de residuos permite obtener un radio positivo común.

## 8.15. Tres conjuntos diferentes

[]{#MA-EX-ANM-01-008-015}

[]{#MA-SOL-ANM-01-008-015}

[]{#MA-SEC-ANM-01-008-004}

La imagen es $A=\{3\}\cup\{1,1/2,1/3,\ldots\}$. La sucesión converge a cero, pues el prefijo no afecta el límite, así que su único punto secuencial es cero. Cero es punto de acumulación de $A$ por los recíprocos. Para excluir cualquier $x\ne0$ como punto de acumulación, elige $J\ge1$ natural con $1/J<|x|/2$. Para $n\ge J$, la triangular inversa da $|x-1/n|\ge|x|-1/n>|x|/2$. Sólo queda el conjunto finito $F=\{3\}\cup\{1/n:1\le n<J\}$. Si $F\setminus\{x\}$ es no vacío, toma

$$
r=\min\left\{\frac{|x|}{2},\frac12\min_{y\in F\setminus\{x\}}|x-y|\right\}>0.
$$

Si es vacío, toma $r=|x|/2$. Esta bola excluye todos los puntos de $A$ distintos de $x$: los recíprocos tardíos quedan fuera por la primera estimación y los puntos finitos restantes por la elección del radio. Por tanto $x$ no es de acumulación. Si además $x\notin A$, la misma bola no contiene ningún punto de $A$ y excluye adherencia. Los puntos de $A$ sí son adherentes por pertenencia, y $0$ por los recíprocos. En consecuencia $\overline A=A\cup\{0\}$ y $\operatorname{Acc}(A)=\{0\}$.

La [figura 8.4](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f03) ayuda a distinguir los tres conjuntos que se han calculado.

## 8.16. Cambios finitos del conjunto

[]{#MA-EX-ANM-01-008-016}

[]{#MA-SOL-ANM-01-008-016}

La inclusión por monotonía da $\operatorname{Acc}(A\setminus F)\subseteq\operatorname{Acc}(A)\subseteq\operatorname{Acc}(A\cup F)$. Si $L\in\operatorname{Acc}(A)$, cada bola contiene infinitos puntos de $A$; retirar $F\cup\{L\}$ aún deja un testigo, así que $L\in\operatorname{Acc}(A\setminus F)$. Finalmente, si $L\in\operatorname{Acc}(A\cup F)$, cada bola contiene infinitos puntos de la unión, y al retirar los finitísimos de $F$ quedan puntos de $A$ distintos de $L$. Esto prueba la última inclusión necesaria. El argumento usa infinitud de valores, no multiplicidad de una lista.

## 8.17. Cuando no se repiten valores

[]{#MA-EX-ANM-01-008-017}

[]{#MA-SOL-ANM-01-008-017}

Si $L$ es punto secuencial, cada bola alrededor de $L$ recibe infinitos índices. Si sólo contuviera finitos valores de $A$, cada uno aportaría finitos índices por hipótesis, dando una unión finita de conjuntos finitos: contradicción. Así hay infinitos valores y $L\in\operatorname{Acc}(A)$. Recíprocamente, si $L\in\operatorname{Acc}(A)$, cada bola contiene infinitos valores de $A$. Dado un corte $N$, el prefijo $a_0,\ldots,a_{N-1}$ sólo aporta finitos valores; existe un valor de esa bola fuera del prefijo y un índice que lo realiza, necesariamente al menos $N$. Esto prueba acumulación secuencial. La segunda dirección no necesita la hipótesis de multiplicidad finita.

## 8.18. Misma imagen y destinos diferentes

[]{#MA-EX-ANM-01-008-018}

[]{#MA-SOL-ANM-01-008-018}

La primera es $a_n=1/(n+1)$; converge a cero y sus puntos secuenciales son exactamente $\{0\}$. Para la segunda, sea $B_m=m(m-1)/2$ el índice inicial del bloque de longitud $m\ge1$. Los naturales $B_m$ crecen estrictamente y sin cota, así que cada $n$ pertenece a un único bloque $B_m\le n<B_{m+1}$. Definimos $b_n=1/(n-B_m+1)$. Se obtienen los bloques $(1)$, $(1,1/2)$, $(1,1/2,1/3)$ y así sucesivamente; todos sus valores están en $A$, y cada $1/j$ aparece en el bloque $m=j$.

Para un $j\ge1$ fijo y cualquier corte $N$, toma $m\ge\max\{j,N+2\}$. El índice $n=B_m+j-1\ge N$ tiene $b_n=1/j$, por lo que ese valor es punto secuencial. Para $0$, recibidos $\varepsilon>0$ y $N$, toma $m\ge N+2$ con $m>1/\varepsilon$. El último índice del bloque, $n=B_m+m-1\ge N$, tiene $0<b_n=1/m<\varepsilon$. Así también $0$ es punto secuencial. No hay otros, pues todo punto secuencial es adherente a la imagen y la clausura de $A$ es $A\cup\{0\}$, demostrada mediante finitud local fuera de cero como en el ejercicio 8.15. La imagen por sí sola no fija las multiplicidades temporales.

## 8.19. Una elección mal justificada

[]{#MA-EX-ANM-01-008-019}

[]{#MA-SOL-ANM-01-008-019}

Toma $A=(0,1)$, $L=0$ y $k=0$. La intersección es $(0,1)$ y no tiene menor elemento: si $x$ pertenece, $x/2$ es menor y también pertenece. La adherencia sólo garantiza no vacuidad. La reparación usa la función de elección $c$ sobre los subconjuntos no vacíos de $A$: $x_k=c(A\cap B(L,1/(k+1)))$. Entonces $|x_k-L|<1/(k+1)$ y el argumento arquimediano da convergencia. No hay que imponer a $A$ un orden con mínimos que el enunciado no ofrece.

Los testigos elegidos se interpretan como aproximaciones al centro, como en la [figura 8.4](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f03); su existencia procede de adherencia y de la elección fijada.

## 8.20. Caracterizar los cerrados por límites

[]{#MA-EX-ANM-01-008-020}

[]{#MA-SOL-ANM-01-008-020}

Si $F$ es cerrado y $x_n\in F$ converge a $L$, cada bola alrededor de $L$ contiene términos de $F$, así que $L$ es adherente y pertenece a $F$. Recíprocamente, si todos esos límites pertenecen a $F$, toma cualquier punto adherente $L$. Por §8.4 existe una sucesión de puntos de $F$ que converge a $L$; la hipótesis da $L\in F$. Así $F$ contiene todos sus puntos adherentes y es cerrado por C04. Si $F=\varnothing$, no existen sucesiones con valores en él; la propiedad universal es vacua y el vacío es cerrado. La equivalencia no requiere acotación porque sólo considera sucesiones que ya convergen.

## 8.21. Primeras mitades y reserva

[]{#MA-EX-ANM-01-008-021}

[]{#MA-SOL-ANM-01-008-021}

[]{#MA-SEC-ANM-01-008-005}

Se obtiene $I_1=[-1,0]$, $I_2=[-1/2,0]$ e $I_3=[-1/4,0]$. En el primer paso la mitad izquierda contiene todos los índices impares. Para $I_2$, la otra mitad $[-1,-1/2]$ recibe sólo el índice uno; la mitad que llega a cero recibe todos los impares. Para $I_3$, $[-1/2,-1/4]$ recibe sólo los índices uno y tres, mientras que $[-1/4,0]$ recibe todos los impares desde tres. Compartir el extremo $-1/4$ no afecta la infinitud. La justificación general usa $1/(n+1)\to0$, no el recuento de los primeros puntos dibujados.

La [figura 8.5](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f05) permite seguir el encajamiento; la reserva infinita se acredita con las desigualdades sobre los recíprocos.

## 8.22. Un invariante demasiado débil

[]{#MA-EX-ANM-01-008-022}

[]{#MA-SOL-ANM-01-008-022}

Para $k\ge1$, $I_k\subseteq[-1/2,1/2]$ y sólo recibe el índice original cero. Por ello la pertenencia exigiría $n_k=0$ para todos los $k\ge1$, incompatible con crecimiento estricto. El punto común existe y es cero, pero no hay reserva infinita de índices alrededor de él. De hecho la sucesión converge a uno y cero no es punto secuencial. La condición «contiene algún término» no permite la extracción temporal.

La condición de reserva de la [figura 8.5](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f05) excluye precisamente la reutilización de un único índice que haría fallar esta extracción.

## 8.23. Dividir en más partes

[]{#MA-EX-ANM-01-008-023}

[]{#MA-SOL-ANM-01-008-023}

Los $m$ subintervalos cubren al anterior, aunque compartan extremos. Si cada conjunto de índices fuese finito, su unión finita sería finita; alguno conserva infinitos índices. Elegimos el primero de izquierda a derecha entre los que sirven. Esto define una familia encajada de intervalos cerrados no vacíos con anchuras $2M/m^k$. Como $m^k\ge2^k\ge k+1$, arquimedianidad permite hacer la anchura menor que cualquier tolerancia. C03 da un punto común por completitud, y la anchura arbitrariamente pequeña da unicidad mediante la comparación de dos supuestos puntos. Para $M=0$ se trata directamente la constante cero. La prueba no depende específicamente de dos mitades, sino de una partición finita con reducción uniforme de anchura.

## 8.24. Anchuras pequeñas sin intersección

[]{#MA-EX-ANM-01-008-024}

[]{#MA-SOL-ANM-01-008-024}

Toma $I_k=(0,1/(k+1))$. Son abiertos, no vacíos y encajados, y su anchura puede hacerse tan pequeña como se quiera por arquimedianidad. Un punto común tendría que ser positivo; para un $x>0$ fijado existe $k$ con $1/(k+1)<x$, por lo que $x\notin I_k$. Cero tampoco pertenece a ninguno. La intersección es vacía. Falla la hipótesis de intervalos cerrados en la interfaz de C03; la disminución de anchuras no reemplaza esa hipótesis.

El carácter cerrado de los intervalos de la [figura 8.5](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f05) es esencial para garantizar el punto común.

## 8.25. El punto común como supremo

[]{#MA-EX-ANM-01-008-025}

[]{#MA-SOL-ANM-01-008-025}

El conjunto de extremos izquierdos es no vacío y está acotado superiormente por $v_0$, así que completitud da su supremo $L$. Para cada $k$, $u_k\le L$. Además $v_k$ es cota superior de todos los $u_j$: si $j\ge k$, el encajamiento da $u_j\le v_j\le v_k$; si $j<k$, da $u_j\le u_k\le v_k$. Por minimalidad del supremo, $L\le v_k$. Luego $L\in I_k$ para todo $k$. Si dos puntos comunes distaran $d>0$, una anchura menor que $d$ lo impediría. Esta prueba abre la interfaz de C03 y muestra que completitud se usa en la existencia del supremo, no en calcular una fórmula del candidato.

## 8.26. Los mínimos de la extracción

[]{#MA-EX-ANM-01-008-026}

[]{#MA-SOL-ANM-01-008-026}

[]{#MA-SEC-ANM-01-008-006}

Como $E_0=\mathbb N$, $n_0=0$. En $I_1=[-1,0]$ el primer índice posterior es uno; en $I_2=[-1/2,0]$ el primero posterior a uno es tres; en $I_3=[-1/4,0]$ el primero posterior a tres es cinco. Para $k\ge1$, la pertenencia de un término exige índice impar y $1/(n+1)\le2^{1-k}$, equivalente a $n\ge2^{k-1}-1$. Para $k=4$ ese primer impar admisible es siete, mayor que cinco; para $k=5$ es quince. Si la fórmula vale en algún $k\ge4$, el primer impar admisible en $I_{k+1}$ es $2^k-1$, mayor que $n_k$. La recursión de mínimos da la fórmula por inducción. Se obtiene $0,1,3,5,7,15$; la fórmula no debe extenderse a los primeros pasos, donde la condición de ser posterior puede dominar a la cota espacial.

En la [figura 8.6](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f06) se separan la pertenencia al intervalo y la obligación de avanzar en los índices; ambas intervienen en estos mínimos.

## 8.27. Una extracción todavía más tardía

[]{#MA-EX-ANM-01-008-027}

[]{#MA-SOL-ANM-01-008-027}

Cada conjunto admisible es no vacío porque $E_k$ es infinito y la nueva exigencia sólo excluye un prefijo finito. El mínimo existe por buen orden. Las elecciones mantienen $n_{k+1}>n_k$ y $a_{n_k}\in I_k$, así que forman una subsucesión. Dado $\varepsilon>0$, elige $K$ con $w_K<\varepsilon$. Para $k\ge K$, los puntos $a_{n_k}$ y $L$ siguen estando en $I_K$, de donde $|a_{n_k}-L|\le w_K<\varepsilon$. El tamaño de los saltos temporales no interviene en la estimación espacial.

La estimación por anchura de la [figura 8.6](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f06) sigue funcionando al retrasar las elecciones de índices.

## 8.28. Lo que no promete la existencia

[]{#MA-EX-ANM-01-008-028}

[]{#MA-SOL-ANM-01-008-028}

Toma $a_n=(-1)^n$. El selector $\varphi(k)=2k$ produce la constante uno. El selector $\psi(k)=k+1$ produce $b_k=(-1)^{k+1}$, cuyas selecciones par e impar son constantes menos uno y uno; por §8.2 y unicidad no converge. La primera sucesión difiere de $a$ en el índice uno y la segunda difiere ya en cero. Ambas son subsucesiones porque sus selectores crecen estrictamente. La existencia garantizada por el teorema no convierte toda elección en convergente.

La [figura 8.2](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f02) permite contrastar lo que controla una selección con lo que permanece en la sucesión original.

## 8.29. Extracciones simultáneas

[]{#MA-EX-ANM-01-008-029}

[]{#MA-SOL-ANM-01-008-029}

Aplica Bolzano–Weierstrass a $a$ y obtiene $\varphi$ con $a_{\varphi(k)}\to A$. La sucesión $b_{\varphi(k)}$ sigue acotada; extrae de ella mediante $\psi$ una sucesión convergente a $B$. Pon $\theta=\varphi\circ\psi$, estrictamente creciente. La selección $a_{\theta(j)}$ converge a $A$ porque es una subsucesión de una sucesión que ya convergía, mientras que $b_{\theta(j)}\to B$ por construcción. Para una familia finita se procede por inducción: la siguiente extracción conserva los límites previamente obtenidos y añade uno nuevo. No se afirma que el selector sea determinado de forma única; muchos pueden servir. La técnica transferible consiste en conservar las propiedades adquiridas al hacer cada extracción posterior.

## 8.30. Un selector para numerables sucesiones

[]{#MA-EX-ANM-01-008-030}

[]{#MA-SOL-ANM-01-008-030}

Construimos selectores originales $\varphi_r$ anidados. Aplica la construcción determinada de Bolzano–Weierstrass a $a^{(0)}$ y obtiene $\varphi_0$. Dado $\varphi_r$, extrae de $a^{(r+1)}_{\varphi_r(k)}$ mediante un selector $\psi_{r+1}$ y define $\varphi_{r+1}=\varphi_r\circ\psi_{r+1}$. Para cada $s\le r$, $a^{(s)}_{\varphi_r(k)}$ converge, por conservación de límites. Las elecciones pueden fijarse usando la menor cota natural positiva disponible y las reglas de mitades y mínimos ya especificadas; no se precisa escoger arbitrariamente entre selectores.

Define la diagonal $\theta(k)=\varphi_k(k)$. Como $\psi_{k+1}(k+1)\ge k+1$, se tiene $\theta(k+1)=\varphi_k(\psi_{k+1}(k+1))\ge\varphi_k(k+1)>\varphi_k(k)=\theta(k)$. Por tanto $\theta$ es selector. Fija $r$. Para $k\ge r$, el anidamiento permite escribir $\theta(k)=\varphi_r(t_k)$, con $t_k\ge k$; esto se deduce componiendo los selectores posteriores, cada uno mayor o igual a la identidad. Como $\theta$ crece y $\varphi_r$ es estrictamente creciente, los $t_k$ también crecen. Dada una tolerancia para el límite de $a^{(r)}_{\varphi_r(j)}$, toma su umbral $J$ y luego $K=\max\{r,J\}$. Para $k\ge K$, $t_k\ge k\ge J$ y el término diagonal cumple la tolerancia. Cada $r$ fijo queda controlado; no se ha afirmado un umbral uniforme en $r$.

## 8.31. Dos hipótesis de un conjunto

[]{#MA-EX-ANM-01-008-031}

[]{#MA-SOL-ANM-01-008-031}

[]{#MA-SEC-ANM-01-008-007}

El conjunto $\{0,2\}$ es acotado y finito. En cada centro real una bola suficientemente pequeña excluye todos los puntos distintos del centro; si el centro no pertenece, toma radio menor que ambas distancias. No tiene acumulación. El conjunto $\mathbb N\subset\mathbb R$ es infinito y no acotado. Cualquier bola acotada contiene sólo finitísimos naturales, y puede reducirse para excluir todos los distintos de su centro; por tanto tampoco tiene acumulación. El primer caso carece de infinitud y el segundo de acotación: ninguno cumple las dos hipótesis del teorema.

## 8.32. Un cerrado que retiene el destino

[]{#MA-EX-ANM-01-008-032}

[]{#MA-SOL-ANM-01-008-032}

La cota $|a_n|\le\max\{|u|,|v|\}$ permite aplicar Bolzano–Weierstrass. Si una extracción converge a $L$, el orden de límites da $u\le L\le v$; también puede usarse que el intervalo es cerrado. Esto incluye $u=v$, caso constante. Para $u<v$, define $a_n=u+(v-u)/(n+2)$. Sus valores están estrictamente entre $u$ y $v$ y converge a $u$, por las reglas de C06. Toda subsucesión tiene el mismo límite $u$ y por unicidad ninguna converge a un punto del intervalo abierto. El carácter cerrado decide si el destino permanece dentro.

La [figura 8.7](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f07) distingue que exista un destino real de que pertenezca al conjunto que contiene los términos.

## 8.33. Conjunto cerrado acotado sin acumulación

[]{#MA-EX-ANM-01-008-033}

[]{#MA-SOL-ANM-01-008-033}

Si $A$ fuera infinito y acotado, el teorema de §8.7 le daría un punto de acumulación, contradicción. Por tanto es finito. No hace falta cerradura: la existencia de acumulación para conjuntos infinitos acotados ocurre en $\mathbb R$, sin prometer pertenencia a $A$. De hecho todo conjunto finito es cerrado por C04, pero esa conclusión adicional no se usó como hipótesis. El argumento es la contrapositiva del teorema con la acotación mantenida.

## 8.34. Conjuntos de destinos acotados

[]{#MA-EX-ANM-01-008-034}

[]{#MA-SOL-ANM-01-008-034}

Bolzano–Weierstrass da una extracción convergente, cuyo límite pertenece a $C$ por §8.3; así $C$ es no vacío. El ejercicio 8.13 probó cerradura sin requerir acotación; alternativamente, si $L$ es adherente a $C$, aproxima $L$ por un $H\in C$ a error $\varepsilon/2$ y después elige un término tardío cerca de $H$ al mismo error. Eso demuestra $L\in C$. Finalmente, si $H\in C$, una extracción converge a $H$ y todos sus términos están entre $-M$ y $M$. El orden de límites da $-M\le H\le M$. Las tres conclusiones proceden de obligaciones distintas: existencia, estabilidad por aproximación y cota heredada.

## 8.35. Distancia positiva entre dos cerrados

[]{#MA-EX-ANM-01-008-035}

[]{#MA-SOL-ANM-01-008-035}

Supón que no existe tal $\delta$. Para cada $n$ hay $x_n\in A$ y $y_n\in B$ con $|x_n-y_n|<1/(n+1)$. Se eligen estos testigos bajo la base clásica de elección; puede hacerse eligiendo primero un $x$ admisible en $A$ y luego un $y$ admisible en $B$. La sucesión $x$ es acotada; una extracción $x_{\varphi(k)}$ converge a un real $L$, y como $A$ es cerrado, $L\in A$. Además

$$
|y_{\varphi(k)}-L|\le |y_{\varphi(k)}-x_{\varphi(k)}|+|x_{\varphi(k)}-L|
<\frac1{\varphi(k)+1}+|x_{\varphi(k)}-L|.
$$

El primer sumando está acotado por $1/(k+1)$ y el segundo tiende a cero. Para cualquier tolerancia se hacen ambos menores que su mitad reuniendo los umbrales. Así $y_{\varphi(k)}\to L$; como $B$ es cerrado, $L\in B$, contradiciendo $A\cap B=\varnothing$. No necesitábamos acotación global de $B$: la proximidad a la extracción de $A$ produjo la convergencia necesaria.

## 8.36. Toda extracción puede refinarse

[]{#MA-EX-ANM-01-008-036}

[]{#MA-SOL-ANM-01-008-036}

[]{#MA-SEC-ANM-01-008-008}

Si $a_n\to L$, toda subsucesión ya converge a $L$ por §8.2 y la identidad sirve como extracción adicional. Recíprocamente, si $a$ no converge a $L$, existe $\varepsilon_0>0$ con términos tardíos de error al menos $\varepsilon_0$. Construyendo mínimos después de cada corte se obtiene una subsucesión $b$ con $|b_k-L|\ge\varepsilon_0$ para todo $k$. Ninguna extracción suya puede converger a $L$, porque todas conservan esa desigualdad y contradicen la captura estricta para la tolerancia $\varepsilon_0$. Esto contradice la hipótesis. Aquí ésta garantiza directamente la extracción hacia $L$, por lo que no se necesita Bolzano–Weierstrass ni acotación.

## 8.37. Clasificar una familia intercalada

[]{#MA-EX-ANM-01-008-037}

[]{#MA-SOL-ANM-01-008-037}

La selección par converge a $p$ y la impar a $q$, así que ambos son puntos secuenciales, posiblemente iguales. No hay otros: por el resultado de partición finita del ejercicio 8.14, cada punto secuencial proviene de una de esas dos selecciones, y una sucesión convergente sólo tiene su límite como punto secuencial. Por tanto el conjunto es $\{p,q\}$. La sucesión es acotada por $\max\{|p|,|q|\}+1$. Si $p=q$, el criterio de §8.8 da convergencia a ese valor; también sirve intercalar dos límites iguales. Si $p\ne q$, los dos destinos diferentes impiden convergencia.

La [figura 8.8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f08) sitúa el papel de acotación y unicidad del destino; aquí los dos límites se han identificado por paridades.

## 8.38. Un radio que depende del corte

[]{#MA-EX-ANM-01-008-038}

[]{#MA-SOL-ANM-01-008-038}

Toma $a_n=1/(n+1)$ y $L=0$. Para cada $N$, el índice $n=N$ y el radio $\varepsilon_N=1/(N+1)$ cumplen la condición, aunque $a_n\to0$. Los radios pueden disminuir y no establecen un margen de error persistente. La negación correcta fija primero $\varepsilon_0>0$: para todo $N$ existe $n\ge N$ con $|a_n-L|\ge\varepsilon_0$. Con ese orden sí se construye una extracción cuyos términos nunca entran en una misma ventana, lo que refuta convergencia.

La [figura 8.8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html#fig-anm-c08-f08) permite leer la refutación con una sola ventana fijada antes de todos los cortes.

## 8.39. Acercarse a un conjunto finito de destinos

[]{#MA-EX-ANM-01-008-039}

[]{#MA-SOL-ANM-01-008-039}

Si falla para algún $\varepsilon_0>0$, hay términos después de todo corte fuera de la unión. Extrae por mínimos una subsucesión $b$ que satisfaga $|b_k-L_i|\ge\varepsilon_0$ para todos los $k$ y todos los $i$. Como $b$ es acotada, Bolzano–Weierstrass proporciona una extracción convergente a $H$. Por composición y §8.3, $H$ es punto secuencial de $a$, así que $H=L_j$ para algún $j$. La convergencia a ese $L_j$ contradice la desigualdad de error fijo. La conclusión encierra la cola en varias ventanas, sin afirmar que permanezca en una sola ni que converja.

## 8.40. Saltos pequeños y destinos intermedios

[]{#MA-EX-ANM-01-008-040}

[]{#MA-SOL-ANM-01-008-040}

Fija $t\in(p,q)$, una tolerancia $\varepsilon>0$ y un corte $N$. Toma $\eta=\min\{\varepsilon,t-p,q-t\}/2>0$; es menor que las tres cantidades. Existe $N_0\ge N$ tal que $|a_{n+1}-a_n|<\eta$ para $n\ge N_0$. Como $p$ es punto secuencial, hay $i\ge N_0$ con $|a_i-p|<\eta$, luego $a_i<t$. Como $q$ es punto secuencial, hay $j>i$ con $|a_j-q|<\eta$, luego $a_j>t$.

En el conjunto finito de índices entre $i+1$ y $j$ existe un primer $r$ con $a_r\ge t$. Entonces $a_{r-1}<t\le a_r$ y $r-1\ge N_0$, por lo que $0\le a_r-t\le a_r-a_{r-1}<\eta<\varepsilon$. Además $r\ge N$. Hemos encontrado una visita a la bola de $t$ después de cualquier corte, así que $t$ es punto secuencial. El paso transferible es localizar el primer cruce: saltos pequeños impiden atravesar una altura sin acercarse a ella. La acotación pertenece al contexto de destinos de la sucesión, pero este argumento concreto sólo necesita los dos destinos y la condición sobre saltos.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html) · [Ejercicios](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-soluciones.html)
