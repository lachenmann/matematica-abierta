---
content-id: MA-BCH-0294
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-023
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
title: Capítulo 23 — Integral de Riemann y Darboux
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C23.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)

C22 construyó sumas finitas y un límite que debe controlar toda etiqueta. Ahora construiremos dos envolventes a partir de cotas de valores, demostraremos cuándo coinciden y probaremos que producen exactamente ese límite. La brecha ponderada de oscilaciones será el certificado que conecta ambos métodos.

C02/C03 orden y completitud, C14 continuidad y C22 particiones/sumas son herramientas centrales. C16/C17 ya cerrados aportan la interfaz de compacidad y escala uniforme sólo para el caso continuo. No usamos antiderivadas ni el teorema fundamental, reservado para C24.

## 23.1. Cotas de valores y oscilación

[]{#MA-SEC-ANM-01-023-001}

Fijemos $a<b$ y una función $f:[a,b]\to\mathbb R$. Hasta que se diga otra cosa, suponemos una cota dada $|f(t)|\le B$ con $B\ge0$, válida para todas las entradas. Para cualquier conjunto no vacío $J\subseteq[a,b]$, su imagen es no vacía y acotada. Completitud de C03 da los reales

$$m(f,J)=\inf f[J],\qquad M(f,J)=\sup f[J],\qquad
\omega(f,J)=M(f,J)-m(f,J)\ge0.$$

La oscilación es una diferencia de cotas extremas, no una derivada ni la diferencia entre dos muestras elegidas. No exigimos que los extremos se alcancen. Si $J\subseteq K$, la inclusión de imágenes y las propiedades de cotas dan

$$m(f,K)\le m(f,J)\le M(f,J)\le M(f,K),\qquad
\omega(f,J)\le\omega(f,K).$$

En efecto, toda cota inferior de $f[K]$ acota $f[J]$, y toda cota superior de $f[K]$ también; maximalidad del ínfimo y minimalidad del supremo prueban las comparaciones. Se dispone de $-B\le m\le M\le B$, de modo que $\omega\le2B$.

Para $\eta>0$ hay entradas $s,t\in J$ con $f(s)>M-\eta$ y $f(t)<m+\eta$: de lo contrario $M-\eta$ sería cota superior o $m+\eta$ cota inferior, contradiciendo su carácter extremo. Son testigos para la precisión fijada; no una regla que alcance el supremo.

Por ejemplo, en $[0,1]$ definamos $g(x)=x$ para $0<x<1$ y $g(0)=g(1)=1/2$. Su ínfimo es0 y su supremo1, ninguno alcanzado. Las cotas son verificables: todo valor está entre0 y1, y entradas positivas arbitrariamente próximas a0 o a1 impiden mejorarlas. La oscilación vale1. Por contraste, para $x^2$ en $[u,v]\subseteq[0,1]$, $m=u^2$, $M=v^2$ y $\omega=v^2-u^2$, pues el cuadrado preserva el orden no negativo.

![g(x)=x en(0,1), con g(0)=g(1)=1/2: ínfimo0 y supremo1 no alcanzados. Extremos de curva abiertos; valores nodales cerrados en1/2.](../../assets/books/anm/C23/C23-F01.svg){#fig-anm-c23-f01 fig-alt="g(x)=x en(0,1), con g(0)=g(1)=1/2: ínfimo0 y supremo1 no alcanzados. Extremos de curva abiertos; valores nodales cerrados en1/2."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-001}

1. ¿Qué hipótesis permite extremos locales reales?

[]{#MA-MIC-ANM-01-023-002}

2. ¿La oscilación es una derivada?

[]{#MA-MIC-ANM-01-023-003}

3. ¿Deben alcanzarse $m$ y $M$?

[]{#MA-MIC-ANM-01-023-004}

4. ¿Qué ocurre al restringir a $J\subseteq K$?

[]{#MA-MIC-ANM-01-023-005}

5. ¿Qué cota da $|f|\le B$ para la oscilación?

[]{#MA-MIC-ANM-01-023-006}

6. ¿Cómo se obtiene una altura cercana al supremo?

[]{#MA-MIC-ANM-01-023-007}

7. ¿Cuál es la oscilación de $x^2$ en $[u,v]\subseteq[0,1]$?

[]{#MA-MIC-ANM-01-023-008}

8. ¿Dos muestras determinan la oscilación?

## 23.2. Dos sumas que el refinamiento sí ordena

[]{#MA-SEC-ANM-01-023-002}

Sea $P=(x_0,\ldots,x_n)$ una partición de C22, $I_i=[x_{i-1},x_i]$ y $\Delta_i>0$. Definimos

$$L(f,P)=\sum_i m(f,I_i)\Delta_i,\qquad
U(f,P)=\sum_i M(f,I_i)\Delta_i.$$

Son números reales finitos. Para cualquier familia de etiquetas admisibles,

$$-B(b-a)\le L(f,P)\le S(f;P,\xi)\le U(f,P)\le B(b-a).$$

Multiplicar $m_i\le f(\xi_i)\le M_i$ por anchuras positivas y sumar prueba el encierro. Restar suma a suma da la identidad fundamental

$$G(f,P):=U(f,P)-L(f,P)=\sum_i\omega(f,I_i)\Delta_i.$$

La brecha es no negativa. Vale cero exactamente cuando todas las oscilaciones de piezas son cero: cada sumando es no negativo y, si su suma es cero, cada producto es cero; dividir por su anchura positiva fuerza oscilación cero. Sobre piezas cerradas, eso hace constante a $f$ en cada una. Los nodos compartidos igualan las constantes vecinas: brecha cero en alguna partición implica que $f$ es constante en todo $[a,b]$. Por ello integrabilidad no exige una partición de brecha cero.

Si $P\preceq Q$, cada pieza hija está contenida en su padre; su ínfimo no es menor y su supremo no es mayor. Las anchuras de las hijas suman la del padre. Multiplicar las comparaciones por esas anchuras y agrupar finitamente prueba

$$L(f,P)\le L(f,Q)\le U(f,Q)\le U(f,P).$$

Aquí sí existe monotonía, a diferencia de sumas etiquetadas arbitrarias. Para particiones distintas $P,Q$, su refinamiento común $R$ da $L(f,P)\le L(f,R)\le U(f,R)\le U(f,Q)$. Toda suma inferior queda bajo toda superior, aunque procedan de cortes incompatibles.

Para $x^2$ en uniforme de $n$ piezas sobre $[0,1]$, las sumas son las izquierda y derecha calculadas en C22:

$$L_n=\frac13-\frac1{2n}+\frac1{6n^2},\quad
U_n=\frac13+\frac1{2n}+\frac1{6n^2},\quad G_n=\frac1n.$$

El encierro usa cotas verdaderas sobre cada pieza, no una colección de muestras sin garantía.

![x² en\[0,1\]: rectángulos inferiores/superiores con n2 y n4. Las cotas locales son extremos verdaderos; brechas1/2 y1/4. La recta curva es la misma en ambos paneles.](../../assets/books/anm/C23/C23-F02.svg){#fig-anm-c23-f02 fig-alt="x² en\[0,1\]: rectángulos inferiores/superiores con n2 y n4. Las cotas locales son extremos verdaderos; brechas1/2 y1/4. La recta curva es la misma en ambos paneles."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-009}

1. ¿Cómo se define $L$?

[]{#MA-MIC-ANM-01-023-010}

2. ¿Cómo se define $U$?

[]{#MA-MIC-ANM-01-023-011}

3. ¿Dónde queda una suma etiquetada?

[]{#MA-MIC-ANM-01-023-012}

4. ¿Qué expresa la brecha?

[]{#MA-MIC-ANM-01-023-013}

5. ¿Qué significa brecha cero sobre piezas cerradas?

[]{#MA-MIC-ANM-01-023-014}

6. ¿Qué sumas ordena el refinamiento?

[]{#MA-MIC-ANM-01-023-015}

7. ¿Cómo se comparan $L(P)$ y $U(Q)$ con cortes distintos?

[]{#MA-MIC-ANM-01-023-016}

8. ¿Cuál es la brecha uniforme de $x^2$ en $[0,1]$?

## 23.3. Completitud y criterio de Darboux

[]{#MA-SEC-ANM-01-023-003}

Los conjuntos $\mathcal L_f=\{L(f,P):P\text{ partición}\}$ y $\mathcal U_f=\{U(f,P):P\text{ partición}\}$ son imágenes de funciones reales sobre el conjunto de particiones construido en C22. La partición trivial prueba que son no vacíos; las cotas de la sección anterior prueban acotación. Definimos la integral inferior $\ell_f=\sup\mathcal L_f$ y la superior $u_f=\inf\mathcal U_f$.

Para toda $P,Q$,

$$L(f,P)\le\ell_f\le u_f\le U(f,Q).$$

La desigualdad central merece prueba: cada $U(f,Q)$ acota todas las sumas inferiores, así que $\ell_f\le U(f,Q)$; al valer para todo $Q$, $\ell_f$ es cota inferior de $\mathcal U_f$ y no supera su ínfimo. No se postula una partición óptima.

Llamamos integrable de Darboux a $f$ cuando $\ell_f=u_f$. Su valor común se escribirá $I_D$. El **criterio de Darboux** es

$$\ell_f=u_f\quad\Longleftrightarrow\quad
\forall\varepsilon>0\ \exists P:\ G(f,P)<\varepsilon.$$

Para la dirección directa, la propiedad del supremo proporciona $P$ con $L(f,P)>\ell_f-\varepsilon/2$; el ínfimo da $Q$ con $U(f,Q)<u_f+\varepsilon/2$. Su refinamiento común $R$ tiene brecha menor que $\varepsilon$ cuando los extremos coinciden. Sólo se instancian dos testigos para una tolerancia fijada. Para la inversa, $0\le u_f-\ell_f\le G(f,P)$ para toda $P$; si la diferencia fuese $d>0$, pedir brecha menor que $d/2$ sería contradictorio. Por tanto es cero.

Una partición buena conserva la precisión bajo todo refinamiento. El criterio equivale también a: para cada tolerancia existe $P$ tal que todos sus refinamientos tienen brecha menor que ella; la recíproca usa el refinamiento reflexivo $P\preceq P$.

Si $f$ es integrable, $I_D$ y todas las sumas etiquetadas de $P$ están en $[L,U]$, por lo que $|S-I_D|\le G$. El punto medio numérico $A_P=(L+U)/2$ tiene certificado más fino $|A_P-I_D|\le G/2$. No afirma que $A_P$ sea una suma etiquetada ni el valor exacto. Para $x^2$, $G_n=1/n\to0$, así que el criterio recupera el valor $1/3$ de C22, aunque ninguna partición tenga brecha cero.

![En x², los intervalos \[L_n,U_n\] para n2,4,8,16 se acercan a1/3. Con n4, medio11/32 y media anchura1/8; no se afirma exactitud del medio.](../../assets/books/anm/C23/C23-F03.svg){#fig-anm-c23-f03 fig-alt="En x², los intervalos \[L_n,U_n\] para n2,4,8,16 se acercan a1/3. Con n4, medio11/32 y media anchura1/8; no se afirma exactitud del medio."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-017}

1. ¿Por qué los conjuntos de sumas son no vacíos?

[]{#MA-MIC-ANM-01-023-018}

2. ¿Qué define la integral inferior?

[]{#MA-MIC-ANM-01-023-019}

3. ¿Qué define la integral superior?

[]{#MA-MIC-ANM-01-023-020}

4. ¿Por qué $\ell_f\le u_f$?

[]{#MA-MIC-ANM-01-023-021}

5. ¿Cuál es el criterio de Darboux?

[]{#MA-MIC-ANM-01-023-022}

6. ¿Cómo se aproxima a ambos extremos a la vez?

[]{#MA-MIC-ANM-01-023-023}

7. ¿Una partición buena conserva su precisión al refinar?

[]{#MA-MIC-ANM-01-023-024}

8. ¿Qué error certifica $(L+U)/2$?

## 23.4. El puente hacia todas las sumas de Riemann

[]{#MA-SEC-ANM-01-023-004}

C22 definió Riemann por un real $I_R$ y el contrato $\forall\varepsilon>0\exists\delta>0\forall(P,\xi)$, malla menor que $\delta$ implica $|S-I_R|<\varepsilon$. Demostraremos su equivalencia con Darboux, con igualdad de valores.

Primero, ese contrato obliga acotación aun si no se añadió como hipótesis. Pedimos tolerancia1 y fijamos una uniforme $P$ de malla menor que el radio; elegimos etiquetas medias. Para cada pieza $i$, dejamos todas las otras etiquetas fijas y variamos $t\in I_i$. La suma tiene forma $f(t)\Delta_i+C_i$ y queda entre $I_R-1$ e $I_R+1$. Así $|f(t)|\le(|I_R|+1+|C_i|)/\Delta_i$. Las anchuras son positivas y hay sólo finitísimas cotas; su máximo acota $f$ en el intervalo cubierto por las piezas.

Para una partición fija y $\eta>0$, hay etiquetas $\xi^+$ y $\xi^-$ con

$$U(f,P)-\eta<S(f;P,\xi^+)\le U(f,P),\quad
L(f,P)\le S(f;P,\xi^-)<L(f,P)+\eta.$$

En cada pieza aproximamos supremo o ínfimo con error menor que $\eta/(b-a)$; sumar los errores ponderados por anchuras da menos que $\eta$. La elección de la familia finita se justifica por inducción en sus índices: añadir un testigo existencial al prefijo. No se necesitan extremos alcanzados ni elección para una familia infinita.

Si existe $I_R$, pedimos error $\varepsilon/4$ y fijamos una uniforme que cumpla el radio. El lema con $\eta=\varepsilon/4$ da $U<I_R+\varepsilon/2$ y $L>I_R-\varepsilon/2$, luego $G<\varepsilon$. Darboux existe y su valor queda entre esos extremos para cada tolerancia; si difería de $I_R$, elegir una tolerancia menor que la distancia contradice ese encierro. Por tanto $I_D=I_R$.

La vuelta requiere controlar particiones que no refinan la buena. Fijemos $P_*$ con brecha menor que $\varepsilon/2$, y sea $q$ su número de nodos interiores. Para cualquier $Q$, formamos $R=Q\cup P_*$. Sólo cambian las piezas de $Q$ cuyo interior contiene algún nodo interior de $P_*$; hay a lo sumo $q$, pues los interiores son disjuntos. En cada pieza modificada, la suma superior puede bajar como máximo $2B$ veces su anchura: tanto altura antigua como alturas hijas están en $[-B,B]$ y las anchuras hijas suman la antigua. El aumento inferior tiene la misma cota. En las demás piezas no cambia nada. Sumando,

$$G(f,Q)\le G(f,R)+4Bq\|Q\|
\le G(f,P_*)+4Bq\|Q\|.$$

Si $Bq>0$, tomamos $\delta=\varepsilon/(8Bq)$. Malla menor da brecha menor que $\varepsilon$, y el encierro común de $S$ e $I_D$ prueba el contrato de Riemann. Si $Bq=0$, el segundo término es cero y cualquier radio positivo sirve: no se divide por cero. Queda además demostrado que, para una función acotada integrable, todas las particiones de malla suficientemente pequeña tienen brecha pequeña. Conservar los cortes y reducir la malla son rutas distintas, conectadas por este conteo finito.

![P*=(0,1/2,1), Q=(0,2/5,7/10,1). Sólo la pieza\[2/5,7/10\] de Q contiene el corte1/2 en su interior. R es la unión; q1 y malla Q2/5 controlan el coste por4Bq·malla.](../../assets/books/anm/C23/C23-F04.svg){#fig-anm-c23-f04 fig-alt="P*=(0,1/2,1), Q=(0,2/5,7/10,1). Sólo la pieza\[2/5,7/10\] de Q contiene el corte1/2 en su interior. R es la unión; q1 y malla Q2/5 controlan el coste por4Bq·malla."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-025}

1. ¿El contrato de Riemann obliga acotación?

[]{#MA-MIC-ANM-01-023-026}

2. ¿Se necesitan máximos alcanzados para aproximar $U$ con etiquetas?

[]{#MA-MIC-ANM-01-023-027}

3. ¿Una familia finita de testigos exige elección infinita?

[]{#MA-MIC-ANM-01-023-028}

4. ¿Qué prueba Riemann⇒Darboux?

[]{#MA-MIC-ANM-01-023-029}

5. ¿Por qué no basta refinar sólo la partición buena?

[]{#MA-MIC-ANM-01-023-030}

6. ¿Qué cuenta $q$ en el puente inverso?

[]{#MA-MIC-ANM-01-023-031}

7. ¿Qué cota conecta las brechas?

[]{#MA-MIC-ANM-01-023-032}

8. ¿Qué se hace si $Bq=0$?

## 23.5. Clases integrables y radios útiles

[]{#MA-SEC-ANM-01-023-005}

Una función no decreciente en $[a,b]$ está acotada entre sus valores extremos. En cada pieza, $m_i=f(x_{i-1})$, $M_i=f(x_i)$, de donde

$$G(f,P)=\sum_i(f(x_i)-f(x_{i-1}))\Delta_i
\le\|P\|(f(b)-f(a)).$$

Las diferencias son no negativas y su suma telescopa. Uniformes de malla pequeña y el criterio prueban integrabilidad, sin continuidad. Si la diferencia extrema es cero, la función es constante y no se divide por ella. Para funciones no crecientes se aplica lo anterior a $-f$, o se invierten los extremos; la cota es $\|P\||f(b)-f(a)|$.

Si $f$ es Lipschitz con constante $L$, la diferencia de cualesquiera valores en una pieza es menor o igual que $L\Delta_i$. Esto implica $M_i-m_i\le L\Delta_i$: para todo $s,t$, $f(s)\le f(t)+L\Delta_i$; tomar primero supremo en $s$ y luego ínfimo en $t$ conserva la cota. Así $G\le L\|P\|(b-a)$ y obtenemos integrabilidad y un radio explícito si $L>0$.

Toda función continua en $[a,b]$ es integrable. Precisemos la herramienta heredada: C16 da compacidad del intervalo cerrado y subcubrimientos finitos; C17 conecta esa compacidad con una escala uniforme. Reconstruimos el mecanismo que necesitamos sin selección infinita. Para tolerancia1, consideramos todos los pares $(c,r)$ con $c\in[a,b]$, $r>0$ y $|f(y)-f(c)|<1$ cuando $y$ está en el dominio y $|y-c|<r$. Sus bolas de radio $r/2$ cubren el intervalo por continuidad. Un subcubrimiento finito da cota $\max_j(|f(c_j)|+1)$.

Para $\eta>0$, repetimos con error $\eta/2$ y bolas interiores de radio $r/2$. Un subcubrimiento finito proporciona $\delta=\min_j r_j/2>0$. Si $|s-t|<\delta$, elegimos una de esas bolas que contiene $s$; tanto $s$ como $t$ están a distancia menor que $r_j$ de su centro, y triangular da $|f(s)-f(t)|<\eta$. Si una pieza mide menos que $\delta$, todos sus valores difieren menos que $\eta$ y su oscilación es a lo sumo $\eta$. Pedir $\eta=\varepsilon/(2(b-a))$ produce $G\le\eta(b-a)=\varepsilon/2<\varepsilon$ en cualquier partición de esa malla. No se supone que los supremos se alcancen; el margen absorbe la desigualdad no estricta al tomarlos.

C22 ya probó integrabilidad de escalones y estabilidad por modificaciones finitas; la equivalencia les asigna también el mismo valor de Darboux. Continuidad es suficiente, no necesaria. Un salto monotónico o un valor aislado puede ser integrable. La continuidad local sola sobre un intervalo abierto no suministra la compacidad ni la acotación usadas aquí.

![h=0 para x<1/2 y h=1 para x≥1/2 es monótona con salto. En uniformes pares su brecha1/n tiende a0, controlada por malla, sin continuidad.](../../assets/books/anm/C23/C23-F05.svg){#fig-anm-c23-f05 fig-alt="h=0 para x&lt;1/2 y h=1 para x≥1/2 es monótona con salto. En uniformes pares su brecha1/n tiende a0, controlada por malla, sin continuidad."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-033}

1. ¿Por qué una monótona en un cerrado está acotada?

[]{#MA-MIC-ANM-01-023-034}

2. ¿Qué cota de brecha tiene una no decreciente?

[]{#MA-MIC-ANM-01-023-035}

3. ¿Qué cota da Lipschitz L?

[]{#MA-MIC-ANM-01-023-036}

4. ¿Qué herramienta adicional usa el caso continuo?

[]{#MA-MIC-ANM-01-023-037}

5. ¿Por qué continuidad en el cerrado da cota global?

[]{#MA-MIC-ANM-01-023-038}

6. ¿Cómo se fabrica un radio uniforme?

[]{#MA-MIC-ANM-01-023-039}

7. ¿Por qué se pide η=ε/(2(b−a))?

[]{#MA-MIC-ANM-01-023-040}

8. ¿La continuidad es necesaria para integrar?

## 23.6. Álgebra de funciones e integrales

[]{#MA-SEC-ANM-01-023-006}

Para funciones acotadas, comparar todos los pares de valores da

$$\omega(f+g,J)\le\omega(f,J)+\omega(g,J),\qquad
\omega(\alpha f,J)=|\alpha|\omega(f,J).$$

La primera sigue porque $(f+g)(s)-(f+g)(t)$ está bajo la suma de las dos oscilaciones; tomar los extremos justifica la cota. Para $\alpha<0$, supremo e ínfimo intercambian su papel, de donde el valor absoluto; para $\alpha=0$ ambos son cero. También $||f(s)|-|f(t)||\le|f(s)-f(t)|$, por lo que $\omega(|f|,J)\le\omega(f,J)$.

Si $|f|\le B_f$, $|g|\le B_g$, la identidad

$$f(s)g(s)-f(t)g(t)=f(s)(g(s)-g(t))+g(t)(f(s)-f(t))$$

da $\omega(fg,J)\le B_f\omega(g,J)+B_g\omega(f,J)$. No se multiplica una integral por otra: es una cota local del producto de funciones.

Si $f,g$ son integrables, elegimos particiones con brechas tan pequeñas como se requiera para cada una y las llevamos a un refinamiento común. Las desigualdades anteriores producen brechas arbitrariamente pequeñas para sumas, múltiplos, valor absoluto y producto. Por ejemplo, para producto basta pedir a ambas brecha menor que $\varepsilon/(B_f+B_g+1)$: el resultado es menor que $\varepsilon$, incluso si alguna constante es cero.

Los valores de sumas y múltiplos se calculan con la equivalencia de Riemann y la identidad finita de C22. Para $h=\alpha f+\beta g$, pedimos a ambos errores menores que $\varepsilon/(|\alpha|+|\beta|+1)$ y tomamos el menor de sus radios. Triangular demuestra que $S(h)$ se acerca a $\alpha I_f+\beta I_g$ con error menor que $\varepsilon$; unicidad identifica el valor. Es linealidad de la integral, no una regla de primitivas.

Si $f\le g$, entonces $I_f\le I_g$: de lo contrario su diferencia $d>0$ y una misma partición fina darían, con errores $d/3$, $S(f)>S(g)$, contradiciendo el orden de sumas con las mismas etiquetas. Como $-|f|\le f\le|f|$, el orden y la linealidad dan $|I_f|\le I_{|f|}$. Generalmente no hay igualdad. Para $f(x)=2x-1$ en $[0,1]$, C22 da $I_f=0$; dividir en $1/2$ y sumar dos triángulos mediante las fórmulas afines que justificaremos en la sección siguiente da $I_{|f|}=1/2$. El producto tampoco tiene integral $I_f I_g$: para $f=g=x$, $I_{x^2}=1/3$ frente a $I_x^2=1/4$.

![f=2x−1 tiene integral firmada0 y valor absoluto integral1/2. En el panel derecho, x² tiene integral1/3 y el cuadrado de la integral de x es1/4: el producto de funciones no da producto de integrales.](../../assets/books/anm/C23/C23-F06.svg){#fig-anm-c23-f06 fig-alt="f=2x−1 tiene integral firmada0 y valor absoluto integral1/2. En el panel derecho, x² tiene integral1/3 y el cuadrado de la integral de x es1/4: el producto de funciones no da producto de integrales."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-041}

1. ¿Qué cota tiene la oscilación de una suma?

[]{#MA-MIC-ANM-01-023-042}

2. ¿Qué sucede con un múltiplo negativo?

[]{#MA-MIC-ANM-01-023-043}

3. ¿Qué controla el valor absoluto?

[]{#MA-MIC-ANM-01-023-044}

4. ¿Qué cota controla un producto?

[]{#MA-MIC-ANM-01-023-045}

5. ¿Por qué se necesita un refinamiento común en álgebra?

[]{#MA-MIC-ANM-01-023-046}

6. ¿Cómo se identifica el valor de una combinación lineal?

[]{#MA-MIC-ANM-01-023-047}

7. ¿Siempre $I_{fg}=I_f I_g$?

[]{#MA-MIC-ANM-01-023-048}

8. ¿Qué desigualdad integral da el valor absoluto?

## 23.7. Restringir, pegar y orientar

[]{#MA-SEC-ANM-01-023-007}

Sea $a<c<b$ y $f$ acotada. Si es integrable en $[a,b]$, también lo es en cada subintervalo. Dada una partición de brecha pequeña, insertamos $c$: la brecha no aumenta y se descompone exactamente en las dos brechas de las particiones restringidas. Como ambas son no negativas, cada una es menor que la tolerancia original. El criterio prueba las dos integrabilidades.

Recíprocamente, si las restricciones son integrables, para cada tolerancia tomamos particiones de ambas con brechas menores que $\varepsilon/2$. Concatenarlas en el nodo común $c$ da una partición de $[a,b]$ cuya brecha es la suma, menor que $\varepsilon$. Aquí el valor de $f(c)$ es uno y el mismo en ambas restricciones; no se pegan dos valores incompatibles. Así $f$ es integrable en todo el intervalo.

La aditividad del valor requiere también prueba. Elijamos particiones en ambos lados con brechas menores que $\varepsilon/4$ y cualquier familia explícita de etiquetas en ellas. Sus sumas se concatenan exactamente: $S_{a,b}=S_{a,c}+S_{c,b}$. Las tres integrales quedan a distancia menor que $\varepsilon/4,\varepsilon/4,\varepsilon/2$, respectivamente, de esas sumas, pues la brecha completa es menor que $\varepsilon/2$. Triangular da

$$\left|I_{a,b}-(I_{a,c}+I_{c,b})\right|<\varepsilon.$$

Para todo $\varepsilon$ implica igualdad. Por inducción se extiende a finitísimas piezas; no una aditividad numerable sin nuevas hipótesis.

Con ello, $|2x-1|$ se integra como $1-2x$ a la izquierda de $1/2$ y $2x-1$ a la derecha. La fórmula afín de C22 da $1/4$ en cada mitad, total $1/2$. Un único punto no aporta una anchura positiva: C22 prueba que cambiar finitos valores conserva integral; el puente de este capítulo lo traslada a Darboux, aun cuando sus sumas para una partición fija cambien.

Ahora declaramos convenciones separadas: $\int_a^a f=0$ y $\int_b^a f=-\int_a^b f$ cuando la integral sobre el intervalo ordenado existe. No son particiones con anchuras negativas ni una división por longitud cero. La aditividad se extiende a cualquier orden de tres extremos cuando existe integral en el intervalo que los contiene: se ordenan los extremos, se aplica la igualdad positiva demostrada y se transponen términos con estas convenciones.

![|2x−1| se acumula con1/4 en cada mitad, total1/2. Orientación inversa da−1/2 por convención posterior, sin piezas de anchura negativa.](../../assets/books/anm/C23/C23-F07.svg){#fig-anm-c23-f07 fig-alt="|2x−1| se acumula con1/4 en cada mitad, total1/2. Orientación inversa da−1/2 por convención posterior, sin piezas de anchura negativa."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-049}

1. ¿Cómo se restringe una función integrable?

[]{#MA-MIC-ANM-01-023-050}

2. ¿Cómo se pegan dos restricciones integrables?

[]{#MA-MIC-ANM-01-023-051}

3. ¿Qué ocurre con el valor del nodo común?

[]{#MA-MIC-ANM-01-023-052}

4. ¿Cómo se prueba aditividad del valor?

[]{#MA-MIC-ANM-01-023-053}

5. ¿Se probó aditividad numerable?

[]{#MA-MIC-ANM-01-023-054}

6. ¿Cambiar valores en finitos puntos conserva la integral?

[]{#MA-MIC-ANM-01-023-055}

7. ¿Qué significa orientación inversa?

[]{#MA-MIC-ANM-01-023-056}

8. ¿Qué vale el intervalo degenerado?

## 23.8. Certificar un valor y reconocer el alcance

[]{#MA-SEC-ANM-01-023-008}

Las cotas de Darboux producen un certificado numérico cuando se conocen cotas locales universales. Si no calculamos los extremos exactos, pero tenemos $a_i\le f(t)\le b_i$ para todo $t\in I_i$, entonces

$$\sum_i a_i\Delta_i\le L(f,P)\le I_f\le U(f,P)\le\sum_i b_i\Delta_i$$

para una función cuya integrabilidad se haya demostrado. La anchura del intervalo exterior es un error certificado; una sola pareja de cotas estrechas no prueba integrabilidad para todas las tolerancias. Si se producen tales brechas exteriores arbitrariamente pequeñas, el criterio sí la prueba.

Para $x^2$ en $[0,1]$, $n=4$ uniforme da $[7/32,15/32]$. Su punto medio es $11/32$ y su certificado de error es $1/8$; el error real respecto de $1/3$ es $1/96$, menor que esa cota. La precisión garantizada por el punto medio de las cotas para uniforme general es $1/(2n)$; para error menor que $1/100$ basta $n>50$. Este certificado es de ese aproximante numérico, no de toda suma etiquetada, que con la misma partición tiene error a lo sumo $1/n$.

Un valor aislado separa integrabilidad de exactitud finita. Sea $p(1/2)=1$ y $p(x)=0$ para el resto de $[0,1]$. En la partición $(0,1/2,1)$, los dos cerrados contienen el pico: $L=0$, $U=1$. Para $0<r<1/2$, insertemos los nodos $1/2-r$ y $1/2+r$. Sólo las dos piezas vecinas al pico tienen supremo1; sus anchuras suman $2r$. Por tanto $L=0$, $U=2r$. Elegir $r<\min(1/2,\varepsilon/2)$ da el criterio y valor0. Ninguna partición tiene brecha cero porque el pico pertenece a por lo menos una pieza de anchura positiva. No se usa teoría de medida.

Una brecha persistente puede, por el contrario, impedir integrabilidad. Si una función acotada toma0 y1 en toda pieza no degenerada, todas sus sumas inferiores son0 y superiores $b-a$. Sus integrales extremas difieren. Es una condición universal sobre cada pieza, no una conclusión que se pueda extraer de unos puntos de dibujo; C25 estudiará ejemplos de discontinuidad y esa frontera con detalle.

El cierre deja habilitada una integral única por dos construcciones equivalentes, clases integrables y operaciones justificadas. El capítulo siguiente relacionará acumulación y derivada; aquí no se ha aplicado el teorema fundamental ni una regla general de antiderivadas.

![Con n4, x² está certificado entre7/32 y15/32 y su medio11/32. Para el pico p(1/2)=1, p=0 fuera, cortes1/2±r dan L0,U2r: integral0 con toda brecha finita positiva.](../../assets/books/anm/C23/C23-F08.svg){#fig-anm-c23-f08 fig-alt="Con n4, x² está certificado entre7/32 y15/32 y su medio11/32. Para el pico p(1/2)=1, p=0 fuera, cortes1/2±r dan L0,U2r: integral0 con toda brecha finita positiva."}

### Microcontroles

[]{#MA-MIC-ANM-01-023-057}

1. ¿Qué necesitan las cotas numéricas $a_i,b_i$?

[]{#MA-MIC-ANM-01-023-058}

2. ¿Una brecha pequeña una sola vez prueba integrabilidad?

[]{#MA-MIC-ANM-01-023-059}

3. ¿Cuál es el encierro de $x^2$ con n4?

[]{#MA-MIC-ANM-01-023-060}

4. ¿Cuál es su punto medio y error certificado?

[]{#MA-MIC-ANM-01-023-061}

5. ¿Qué n certifica error medio menor que1/100?

[]{#MA-MIC-ANM-01-023-062}

6. ¿Qué brecha tiene el pico con nodos1/2±r?

[]{#MA-MIC-ANM-01-023-063}

7. ¿El pico integrable tiene alguna partición de brecha cero?

[]{#MA-MIC-ANM-01-023-064}

8. ¿Qué impide integrar una función que toma0 y1 en toda pieza?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)

[← Capítulo 22](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html) · [Capítulo 24 →](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html)
