---
content-id: MA-BCH-0296
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-023-SOLUCIONES
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
title: Soluciones — Capítulo 23
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C23_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html)

## 23.1. Cotas sin extremos alcanzados

[]{#MA-EX-ANM-01-023-001}

[]{#MA-SOL-ANM-01-023-001}

[]{#MA-SEC-ANM-01-023-001}

La imagen de $g$ está contenida en $(0,1)$: en el interior $g(x)=x$, y los dos extremos del dominio tienen altura $1/2$. Por tanto cero es cota inferior y uno cota superior, y ninguno pertenece a la imagen. Para $\eta>0$ tomamos $t=\min(\eta/2,1/4)$. Entonces $t$ y $1-t$ son interiores, $g(t)=t<\eta$ y $g(1-t)=1-t>1-\eta$. Una cota inferior positiva se contradice tomando $\eta$ igual a ella; una cota superior menor que uno se contradice tomando $\eta$ igual a su distancia a uno. En consecuencia $\inf g=0$ y $\sup g=1$, sin extremos alcanzados.

**Retorno visual.** Véase [C23-F01](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.2. Restringir disminuye oscilación

[]{#MA-EX-ANM-01-023-002}

[]{#MA-SOL-ANM-01-023-002}

Escribimos $m_J=\inf f[J]$, $M_J=\sup f[J]$ y análogamente para $K$. Se requiere que las imágenes sean no vacías y acotadas. La inclusión $J\subseteq K$ implica $f[J]\subseteq f[K]$. Toda cota inferior de $f[K]$ acota también $f[J]$, de donde $m_K\le m_J$; toda cota superior de $f[K]$ acota $f[J]$, de donde $M_J\le M_K$. Una entrada de $J$ da además $m_J\le M_J$. Así $m_K\le m_J\le M_J\le M_K$, y al restar $0\le M_J-m_J\le M_K-m_K$. La conclusión depende de la inclusión de imágenes, sin continuidad.

## 23.3. Cuadrado en una pieza

[]{#MA-EX-ANM-01-023-003}

[]{#MA-SOL-ANM-01-023-003}

Para $1/4\le x\le3/4$, la monotonía del cuadrado sobre los no negativos da $1/16\le x^2\le9/16$. Los valores extremos se alcanzan en los bordes, así $m=1/16$, $M=9/16$ y $\omega=9/16-1/16=1/2$. La condición de no negatividad justifica esa monotonía: si $0\le s<t$, entonces $t^2-s^2=(t-s)(t+s)>0$. En $[-1,1]$ los dos bordes tienen altura uno, pero el mínimo del cuadrado es cero en el interior. Allí no sirve la misma regla de tomar el borde izquierdo como ínfimo.

## 23.4. De cotas a testigos

[]{#MA-EX-ANM-01-023-004}

[]{#MA-SOL-ANM-01-023-004}

Sean $M=\sup f[J]$ y $m=\inf f[J]$, con imagen no vacía y acotada. Si no existiera $s\in J$ con $f(s)>M-\eta$, tendríamos $f(s)\le M-\eta$ para todas las entradas. El real $M-\eta<M$ sería entonces una cota superior, contradiciendo que $M$ sea la menor. De igual forma, la ausencia de un $t$ con $f(t)<m+\eta$ haría de $m+\eta>m$ una cota inferior, contra la maximalidad de $m$. Estos dos argumentos dan testigos para cada $\eta>0$, aunque las alturas extremas no se alcancen.

## 23.5. Dos muestras no controlan

[]{#MA-EX-ANM-01-023-005}

[]{#MA-SOL-ANM-01-023-005}

Dado un tamaño deseado $R>0$, elegimos $H=R+1$ y definimos $f(1/2)=H$, $f(x)=0$ para las demás entradas de $[0,1]$. Las muestras en cero y uno son ambas cero. Sin embargo, la imagen es $\{0,H\}$, así $m=0$, $M=H$ y $\omega=H>R$. Para cada $H$ fijo la función está acotada. Esta familia muestra que conservar las dos muestras no limita la altura de una entrada distinta y, por tanto, no limita la oscilación.

## 23.6. Sumas del cuadrado

[]{#MA-EX-ANM-01-023-006}

[]{#MA-SOL-ANM-01-023-006}

[]{#MA-SEC-ANM-01-023-002}

Los nodos son $0,1/4,1/2,3/4,1$ y las cuatro anchuras valen $1/4$. Como el cuadrado es creciente allí, las alturas inferiores son $0,1/16,4/16,9/16$ y las superiores $1/16,4/16,9/16,16/16$. Por tanto $L=(0+1+4+9)/64=14/64=7/32$ y $U=(1+4+9+16)/64=30/64=15/32$. La brecha es $U-L=8/32=1/4$. Las alturas usadas son extremos de la imagen completa de cada pieza; por eso las dos sumas encierran cualquier suma etiquetada de esta partición.

**Retorno visual.** Véase [C23-F02](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.7. Una inserción mejora

[]{#MA-EX-ANM-01-023-007}

[]{#MA-SOL-ANM-01-023-007}

Sean $u<t<v$, $m=\inf f([u,v])$ y $M=\sup f([u,v])$. Para las hijas ponemos $m_1,m_2,M_1,M_2$. La inclusión de cada hija en el padre da $m\le m_1,m_2$ y $M_1,M_2\le M$. Como las anchuras son positivas, $m(v-u)\le m_1(t-u)+m_2(v-t)$ y $M_1(t-u)+M_2(v-t)\le M(v-u)$. Se usó $(t-u)+(v-t)=v-u$. Las demás piezas aportan los mismos términos antes y después de insertar el corte. Así la suma inferior no baja y la superior no sube. Una sucesión finita de inserciones prueba lo mismo para cualquier refinamiento.

## 23.8. Cruzar dos particiones

[]{#MA-EX-ANM-01-023-008}

[]{#MA-SOL-ANM-01-023-008}

Formamos $R$ ordenando la unión finita de los nodos de $P$ y $Q$ y eliminando repeticiones. Tiene los mismos extremos y refina ambas particiones. La monotonía respecto de $P$ da $L(f,P)\le L(f,R)$; el orden en la partición $R$ da $L(f,R)\le U(f,R)$; la monotonía respecto de $Q$ da $U(f,R)\le U(f,Q)$. Concatenar las tres comparaciones prueba $L(f,P)\le U(f,Q)$. No es preciso que las listas originales tengan igual número de piezas o compartan los cortes interiores.

## 23.9. Brecha cero fuerza constancia

[]{#MA-EX-ANM-01-023-009}

[]{#MA-SOL-ANM-01-023-009}

La igualdad $G(f,P)=\sum_i\omega_i\Delta_i=0$ es una suma finita de reales no negativos. Si alguno fuera positivo, la suma también lo sería; por tanto todos son cero. Como $\Delta_i>0$, cada $\omega_i=0$ y $m_i=M_i$. Toda altura de la pieza queda entre esos dos extremos iguales, así $f$ es constante allí. Las piezas $I_i$ e $I_{i+1}$ contienen el nodo $x_i$, donde ambas constantes deben valer $f(x_i)$. Por inducción sobre los índices, todas coinciden. El uso de piezas cerradas hace posible esa propagación de igualdad.

## 23.10. Una suma no es una cota

[]{#MA-EX-ANM-01-023-010}

[]{#MA-SOL-ANM-01-023-010}

Para $f(x)=x$, la partición trivial tiene $L=0$ y $U=1$, y su etiqueta media da $S=1/2$. En las mitades, las etiquetas izquierdas dan $S=(0+1/2)/2=1/4$ y las derechas $S=(1/2+1)/2=3/4$. Son, respectivamente, $L$ y $U$ de la partición refinada. La monotonía de Darboux se verifica en $0\le1/4$ y $3/4\le1$: mejoran las dos barreras. Comparar esas dos sumas etiquetadas con $1/2$ da movimientos opuestos, porque las etiquetas se han cambiado. Ninguna de esas comparaciones contradice la monotonía de las barreras.

## 23.11. Extremos de conjuntos de sumas

[]{#MA-EX-ANM-01-023-011}

[]{#MA-SOL-ANM-01-023-011}

[]{#MA-SEC-ANM-01-023-003}

Suponemos $a<b$ y $f:[a,b]\to\mathbb R$ acotada, con $|f|\le B$. La partición trivial prueba que los conjuntos $\mathcal L_f$ y $\mathcal U_f$ son no vacíos. Todas sus sumas satisfacen $-B(b-a)\le L(f,P)\le U(f,P)\le B(b-a)$, por las cotas de alturas y la identidad de longitudes. Completitud proporciona $\ell_f=\sup\mathcal L_f$ y $u_f=\inf\mathcal U_f$. Para cualquier $Q$, la comparación por refinamiento común da $L(f,P)\le U(f,Q)$ para toda $P$. Por tanto $\ell_f\le U(f,Q)$ para toda $Q$, y al tomar ínfimo queda $\ell_f\le u_f$.

## 23.12. Una partición para dos aproximaciones

[]{#MA-EX-ANM-01-023-012}

[]{#MA-SOL-ANM-01-023-012}

Sea $\varepsilon>0$. Como $I$ es el supremo de las sumas inferiores, existe $P$ con $L(f,P)>I-\varepsilon/2$; de otro modo ese real menor sería una cota superior del conjunto. Como $I$ es el ínfimo de las superiores, existe $Q$ con $U(f,Q)<I+\varepsilon/2$. Tomamos el refinamiento común $R$. La monotonía da $L(f,R)\ge L(f,P)>I-\varepsilon/2$ y $U(f,R)\le U(f,Q)<I+\varepsilon/2$. Restar prueba $G(f,R)<\varepsilon$. Las particiones aproximan los extremos; no necesitan realizarlos exactamente.

## 23.13. La recíproca del criterio

[]{#MA-EX-ANM-01-023-013}

[]{#MA-SOL-ANM-01-023-013}

Por definición de los dos extremos, para cada partición $P$ se tiene $L(f,P)\le\ell_f\le u_f\le U(f,P)$. De ahí $0\le u_f-\ell_f\le G(f,P)$. Supongamos que $d=u_f-\ell_f>0$. La hipótesis de brechas arbitrariamente pequeñas aplicada a $\varepsilon=d/2$ produce $P$ con $G(f,P)<d/2$. Esto daría $d\le G(f,P)<d/2$, imposible. Por no negatividad queda $d=0$ y las integrales inferior y superior coinciden.

## 23.14. Persistencia de precisión

[]{#MA-EX-ANM-01-023-014}

[]{#MA-SOL-ANM-01-023-014}

Fijada $\varepsilon>0$, si existe $P_*$ con $G(f,P_*)<\varepsilon$, toda $Q$ que la refina satisface $L(f,P_*)\le L(f,Q)$ y $U(f,Q)\le U(f,P_*)$. Restar da $G(f,Q)\le G(f,P_*)<\varepsilon$. Esto prueba la persistencia con los cuantificadores $\forall\varepsilon>0\ \exists P_*\ \forall Q\succeq P_*$. En la dirección inversa se toma $Q=P_*$: una partición se refina a sí misma. Así la condición persistente entrega una partición de brecha menor que cada tolerancia y recupera el criterio de Darboux.

## 23.15. Centro del intervalo certificado

[]{#MA-EX-ANM-01-023-015}

[]{#MA-SOL-ANM-01-023-015}

El centro de las cotas es $A=(7/32+15/32)/2=11/32$. La longitud del intervalo certificado es $15/32-7/32=1/4$, así su semilongitud es $1/8$. Como $I$ está en ese intervalo, $|A-I|\le1/8$. Con el dato $I=1/3$, el error efectivo es $|11/32-1/3|=|33/96-32/96|=1/96$. El centro sobreestima el valor en $1/96$ y cumple la cota. Esta operación promedia las dos sumas de Darboux; no es la suma con etiquetas en los puntos medios, que para estas piezas vale $21/64$.

**Retorno visual.** Véase [C23-F03](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.16. Riemann también exige acotación

[]{#MA-EX-ANM-01-023-016}

[]{#MA-SOL-ANM-01-023-016}

[]{#MA-SEC-ANM-01-023-004}

Aplicamos el contrato de Riemann con tolerancia uno y obtenemos $\delta>0$. Elegimos una partición uniforme con malla menor que $\delta$ y fijamos etiquetas de referencia. Para cada pieza $I_i$, mantenemos esas etiquetas en las demás y dejamos variar $t\in I_i$. La suma resultante es $S=f(t)\Delta_i+C_i$, donde $C_i$ es una suma finita fija. El contrato implica $|S-I|<1$, luego $|S|<|I|+1$ y $|f(t)|\Delta_i=|S-C_i|\le|S|+|C_i|<|I|+1+|C_i|$. Dividir por $\Delta_i>0$ da una cota en toda $I_i$. El máximo finito de esas cotas limita $|f|$ en el intervalo, porque las piezas lo cubren, incluidos sus bordes.

## 23.17. Etiquetas próximas a U

[]{#MA-EX-ANM-01-023-017}

[]{#MA-SOL-ANM-01-023-017}

Sean $M_i=\sup f[I_i]$ y $\eta>0$. Como $b-a>0$, el número $\eta/(b-a)$ es positivo. En cada pieza existe $\xi_i$ con $f(\xi_i)>M_i-\eta/(b-a)$. Construimos la familia por inducción finita sobre sus $n$ piezas. Al multiplicar por $\Delta_i>0$ y sumar, $S>\sum_i M_i\Delta_i-\eta\sum_i\Delta_i/(b-a)=U-\eta$. Además $S\le U$ por la cota superior de cada altura. Por tanto $U-\eta<S\le U$. La misma construcción con ínfimos proporciona $L\le S^-<L+\eta$.

## 23.18. Un sentido del puente

[]{#MA-EX-ANM-01-023-018}

[]{#MA-SOL-ANM-01-023-018}

La acotación ya se deduce del contrato de Riemann, así las sumas de Darboux están definidas. Para $\varepsilon>0$, tomamos una partición uniforme de malla menor que el radio que garantiza error $\varepsilon/4$ respecto de $I_R$. Aproximamos sus extremos con etiquetas para obtener $U-\varepsilon/4<S^+$ y $S^-<L+\varepsilon/4$. El contrato da $S^+<I_R+\varepsilon/4$ y $S^->I_R-\varepsilon/4$. Así $U<I_R+\varepsilon/2$ y $L>I_R-\varepsilon/2$, de donde $G<\varepsilon$. Darboux produce una integral $I_D$, que queda entre $L$ y $U$. Estas mismas desigualdades dan $|I_D-I_R|<\varepsilon/2$ para cada $\varepsilon>0$; una distancia positiva sería incompatible con una tolerancia menor. Por tanto los valores coinciden.

## 23.19. Cortes omitidos

[]{#MA-EX-ANM-01-023-019}

[]{#MA-SOL-ANM-01-023-019}

Sea $|f|\le B$ y formemos $R=P_*\cup Q$. Una pieza de $Q$ se divide sólo cuando contiene un nodo interior de $P_*$ en su interior. Como los interiores de las piezas son disjuntos, hay a lo sumo $q$ padres afectados; sus anchuras suman a lo sumo $q\|Q\|$. En un padre de anchura $\Delta$, el supremo antiguo y los de sus hijas están entre $-B$ y $B$. La disminución de la contribución superior es no negativa y no supera $2B\Delta$, porque las anchuras hijas suman $\Delta$. Igualmente el aumento de la contribución inferior no supera $2B\Delta$. Por tanto $G(f,Q)-G(f,R)\le4Bq\|Q\|$. Como $R$ refina $P_*$, $G(f,R)\le G(f,P_*)$. Sumando las desigualdades obtenemos $G(f,Q)\le G(f,P_*)+4Bq\|Q\|$.

**Retorno visual.** Véase [C23-F04](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.20. Radio del puente y caso cero

[]{#MA-EX-ANM-01-023-020}

[]{#MA-SOL-ANM-01-023-020}

Con $B=2$ y $q=3$, la corrección del puente es $4Bq\|Q\|=24\|Q\|$. Si $G(f,P_*)<\varepsilon/2$, elegimos $\delta=\varepsilon/48>0$. Toda $Q$ de malla menor que $\delta$ cumple $G(f,Q)<\varepsilon/2+24\delta=\varepsilon$. Una suma etiquetada de $Q$ y la integral de Darboux están ambas entre $L(f,Q)$ y $U(f,Q)$, así su distancia es menor que $\varepsilon$: queda probado el contrato de Riemann. Para $Bq=0$ la corrección es cero y cualquier radio positivo sirve. Si $B=0$, la función es cero; si $q=0$, la partición buena es la trivial y todas las particiones la refinan.

## 23.21. Monótona con salto

[]{#MA-EX-ANM-01-023-021}

[]{#MA-SOL-ANM-01-023-021}

[]{#MA-SEC-ANM-01-023-005}

La función $h$ es no decreciente y sus extremos son $h(0)=0$, $h(1)=1$. En cualquier partición, $G(h,P)=\sum_i(h(x_i)-h(x_{i-1}))\Delta_i\le\|P\|\sum_i(h(x_i)-h(x_{i-1}))=\|P\|$. Para una tolerancia $\varepsilon>0$, una uniforme de malla menor que $\varepsilon$ tiene brecha menor que ella. El criterio prueba integrabilidad a pesar del salto. Para identificar el valor, insertamos $1/2$ en una uniforme cada vez más fina. La suma inferior en esa partición vale $1/2$, mientras la superior vale $1/2+d$, siendo $d$ la anchura de la pieza inmediatamente izquierda al salto. Esa pieza incluye el nodo de altura uno y aporta $d$ a la suma superior. Como $d$ puede hacerse arbitrariamente pequeño, la integral es $1/2$.

**Retorno visual.** Véase [C23-F05](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.22. Lipschitz como certificado

[]{#MA-EX-ANM-01-023-022}

[]{#MA-SOL-ANM-01-023-022}

En cada pieza de anchura $\Delta_i$, la hipótesis Lipschitz con constante tres da $|f(s)-f(t)|\le3\Delta_i$ para toda pareja de entradas. De ahí $\omega_i\le3\Delta_i$. Al ponderar y sumar, $G\le3\sum_i\Delta_i^2\le3\|P\|\sum_i\Delta_i=6\|P\|$, porque la longitud total es dos. Por tanto $\|P\|<1/600$ garantiza $G<6/600=1/100$. Una uniforme de $1201$ piezas tiene malla $2/1201<1/600$ y cumple el pedido. La hipótesis Lipschitz se usa sobre todas las parejas de cada pieza.

## 23.23. Continua: de local a uniforme

[]{#MA-EX-ANM-01-023-023}

[]{#MA-SOL-ANM-01-023-023}

Fijemos un error de alturas $\eta>0$. Consideramos el conjunto de todos los pares $(c,r)$ con $c\in[a,b]$, $r>0$ y $|f(x)-f(c)|<\eta/2$ para las entradas del dominio a distancia menor que $r$ de $c$. La continuidad garantiza al menos un par por centro, así las bolas relativas de radio $r/2$ forman una cobertura abierta del cerrado. Compacidad da un subcubrimiento finito con pares $(c_j,r_j)$. Ponemos $\delta=\min_j r_j/2>0$. Si $s,t$ están en el dominio y $|s-t|<\delta$, elegimos una bola reducida que contenga a $s$. Entonces $|s-c_j|<r_j/2$ y $|t-c_j|\le|t-s|+|s-c_j|<r_j$. Los dos errores respecto del centro son menores que $\eta/2$, por lo que $|f(s)-f(t)|<\eta$. La construcción sólo extrae una lista finita de pares de la cobertura completa.

## 23.24. El margen al tomar supremos

[]{#MA-EX-ANM-01-023-024}

[]{#MA-SOL-ANM-01-023-024}

Si $|f(s)-f(t)|<\eta$ para toda pareja de una pieza, fijar $t$ da $f(s)<f(t)+\eta$ para todo $s$. Al tomar supremo, $M\le f(t)+\eta$; al tomar ínfimo en $t$, $M\le m+\eta$. Así $\omega\le\eta$, con posible pérdida de estrictitud. Por ejemplo, para $f(x)=x$ en $(0,\eta)$, todas las diferencias son menores que $\eta$ pero la oscilación es exactamente $\eta$. Para el intervalo de longitud positiva $b-a$, pedimos la escala uniforme correspondiente a $\eta=\varepsilon/(2(b-a))$. Una partición de malla menor que esa escala cumple $G\le\eta(b-a)=\varepsilon/2<\varepsilon$.

## 23.25. Un cerrado importa

[]{#MA-EX-ANM-01-023-025}

[]{#MA-SOL-ANM-01-023-025}

La función $f(x)=1/x$ es continua en $(0,1]$. Para cualquier $M>0$ tomamos $x=1/(M+1)$, que pertenece al dominio y satisface $f(x)=M+1>M$. Por tanto no existe cota superior global. El dominio no es compacto: la sucesión $1/(n+1)$ tiende a cero, que queda fuera de él. La construcción por subcubrimiento finito de este capítulo exige un cerrado $[a,b]$; en este ejemplo no entrega la cota necesaria para las sumas de Darboux del intervalo completo.

## 23.26. Signo de un múltiplo

[]{#MA-EX-ANM-01-023-026}

[]{#MA-SOL-ANM-01-023-026}

[]{#MA-SEC-ANM-01-023-006}

Si $\alpha>0$, $\alpha m$ y $\alpha M$ son, respectivamente, el ínfimo y el supremo de $\alpha f[J]$: las desigualdades escalan y los testigos próximos a los extremos prueban su optimalidad. Por ello la oscilación es $\alpha(M-m)$. Si $\alpha<0$, las desigualdades se invierten, y los mismos testigos dan $m(\alpha f,J)=\alpha M$ y $M(\alpha f,J)=\alpha m$. La diferencia es $\alpha m-\alpha M=-\alpha(M-m)=|\alpha|\omega(f,J)$. Para $\alpha=0$ la imagen es $\{0\}$ y ambas oscilaciones son cero. Quedan cubiertos los tres signos sin suponer extremos alcanzados.

## 23.27. Producto integrable

[]{#MA-EX-ANM-01-023-027}

[]{#MA-SOL-ANM-01-023-027}

Sean $|f|\le B_f$ y $|g|\le B_g$. Para $s,t$ en una pieza, la identidad $f(s)g(s)-f(t)g(t)=f(s)(g(s)-g(t))+g(t)(f(s)-f(t))$ da $\omega(fg,J)\le B_f\omega(g,J)+B_g\omega(f,J)$ al tomar extremos. El producto está acotado por $B_fB_g$. Dado $\varepsilon>0$, elegimos particiones para ambas funciones con brechas menores que $\eta=\varepsilon/(B_f+B_g+1)$ y tomamos su refinamiento común $R$. Las brechas de $f$ y $g$ conservan esa cota. Al ponderar la desigualdad local resulta $G(fg,R)\le B_fG(g,R)+B_gG(f,R)\le(B_f+B_g)\eta<\varepsilon$. La última desigualdad también cubre $B_f+B_g=0$. El criterio prueba integrabilidad del producto.

## 23.28. Linealidad del valor

[]{#MA-EX-ANM-01-023-028}

[]{#MA-SOL-ANM-01-023-028}

Para cualquier partición y las mismas etiquetas, la distributividad finita da $S(\alpha f+\beta g)=\alpha S(f)+\beta S(g)$. Dado $\varepsilon>0$, ponemos $\eta=\varepsilon/(|\alpha|+|\beta|+1)$ y tomamos los radios de ambos contratos de Riemann para ese error. Con $\delta$ igual al mínimo, toda partición de malla menor que $\delta$ satisface $|S(\alpha f+\beta g)-(\alpha I_f+\beta I_g)|\le|\alpha||S(f)-I_f|+|\beta||S(g)-I_g|\le(|\alpha|+|\beta|)\eta<\varepsilon$. Esto prueba el contrato con candidato $\alpha I_f+\beta I_g$, incluidos coeficientes cero. La equivalencia y unicidad identifican ese real con la integral de Darboux.

## 23.29. Producto no multiplicativo

[]{#MA-EX-ANM-01-023-029}

[]{#MA-SOL-ANM-01-023-029}

En $[0,1]$, los certificados de sumas de C22 prueban $I_x=1/2$ e $I_{x^2}=1/3$ sin antiderivadas. Como $f=g=x$, su producto es $fg=x^2$. Por tanto $I(fg)=1/3$ y $I_fI_g=(1/2)(1/2)=1/4$. La diferencia es $1/12>0$. El teorema sobre productos garantiza la integrabilidad de $fg$; este cálculo muestra que el valor de su integral no se obtiene multiplicando los dos valores integrales.

**Retorno visual.** Véase [C23-F06](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.30. Valor absoluto y orden

[]{#MA-EX-ANM-01-023-030}

[]{#MA-SOL-ANM-01-023-030}

La triangular inversa implica $\omega(|f|,J)\le\omega(f,J)$ en cada pieza. Toda partición de brecha pequeña para $f$ tiene brecha al menos tan pequeña para $|f|$, así ésta es integrable. El orden $-|f|\le f\le|f|$, junto con linealidad, da $-I_{|f|}\le I_f\le I_{|f|}$, luego $|I_f|\le I_{|f|}$. Para $f(x)=2x-1$ en $[0,1]$, linealidad da $I_f=2(1/2)-1=0$. Una vez probada aditividad, partimos en $1/2$: $|f|=1-2x$ a la izquierda y $|f|=2x-1$ a la derecha. El certificado afín de C22 da $I_{[0,1/2]}x=1/8$ e $I_{[1/2,1]}x=3/8$. Las dos contribuciones son $1/2-2(1/8)=1/4$ y $2(3/8)-1/2=1/4$. Por tanto $0=|I_f|<I_{|f|}=1/2$.

## 23.31. Restricción a dos lados

[]{#MA-EX-ANM-01-023-031}

[]{#MA-SOL-ANM-01-023-031}

[]{#MA-SEC-ANM-01-023-007}

Sea $a<c<b$ y $f$ integrable en $[a,b]$. Para $\varepsilon>0$, elegimos $P$ con $G(f,P)<\varepsilon$ e insertamos $c$ si todavía no es nodo. La nueva partición $R$ tiene brecha no mayor. Sus piezas se separan en dos listas que forman particiones de $[a,c]$ y $[c,b]$. Las alturas de cada pieza son las mismas para la función y su restricción correspondiente, por lo que $G(f,R)=G(f|_{[a,c]},R_1)+G(f|_{[c,b]},R_2)$. Ambas cantidades son no negativas y cada una es menor que $\varepsilon$. Las restricciones conservan la acotación de $f$ y cumplen el criterio para toda tolerancia.

## 23.32. Pegar dos integrales

[]{#MA-EX-ANM-01-023-032}

[]{#MA-SOL-ANM-01-023-032}

Suponemos que ambas restricciones son integrables y que comparten la altura $f(c)$, con $a<c<b$. Cada lado está acotado; el máximo de sus dos cotas absolutas acota la función global. Para $\varepsilon>0$, tomamos particiones de cada lado con brechas menores que $\varepsilon/2$. Concatenamos sus nodos omitiendo la segunda copia de $c$. La lista global es estrictamente creciente y sus piezas son exactamente las de las dos listas. Como los extremos locales incluyen el mismo valor en $c$, la brecha global es la suma de las dos brechas, menor que $\varepsilon$. El criterio prueba la integrabilidad de la función en $[a,b]$.

## 23.33. Aditividad del valor

[]{#MA-EX-ANM-01-023-033}

[]{#MA-SOL-ANM-01-023-033}

Ya se sabe que las tres integrales existen. Para $\varepsilon>0$, tomamos particiones de los lados con brechas $G_1,G_2<\varepsilon/4$ y las concatenamos en $R$. La brecha global es $G_1+G_2<\varepsilon/2$. Elegimos cualquier familia de etiquetas en los lados y la concatenamos. Sus sumas satisfacen exactamente $S_{ab}=S_{ac}+S_{cb}$. El encierro de cada suma y su integral da $|I_{ab}-S_{ab}|\le G_1+G_2$, $|I_{ac}-S_{ac}|\le G_1$ y $|I_{cb}-S_{cb}|\le G_2$. Así $|I_{ab}-I_{ac}-I_{cb}|\le2(G_1+G_2)<\varepsilon$. Como esto vale para toda tolerancia positiva, la distancia es cero y $I_{ab}=I_{ac}+I_{cb}$.

**Retorno visual.** Véase [C23-F07](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.34. Orientar sin nuevas piezas

[]{#MA-EX-ANM-01-023-034}

[]{#MA-SOL-ANM-01-023-034}

La aditividad en intervalos ordenados da $I_{0,2}(x)=I_{0,1}(x)+I_{1,2}(x)=1/2+3/2=2$. La convención de orientación inversa define $I_{2,0}(x)=-I_{0,2}(x)=-2$. La convención para un intervalo degenerado define $I_{1,1}(x)=0$. Estas dos extensiones actúan sobre los valores integrales; la construcción de las sumas sigue usando piezas de anchura positiva cuando los extremos son distintos y están ordenados.

## 23.35. Cambiar un nodo

[]{#MA-EX-ANM-01-023-035}

[]{#MA-SOL-ANM-01-023-035}

Sean $f$ y $g$ iguales excepto en $c$, con $D=|f(c)-g(c)|$. Una etiqueta igual a $c$ puede aparecer en a lo sumo dos piezas cerradas. Por tanto $|S_f-S_g|\le2D\|P\|$. Para una tolerancia $\varepsilon$, el contrato de $f$ con error $\varepsilon/2$ y una malla además menor que $\varepsilon/(4D)$, si $D>0$, dan el mismo contrato para $g$ y el mismo valor por triangular. Si $D=0$, las funciones coinciden. La equivalencia transfiere la conclusión a Darboux. En una partición fija, el valor de $c$ sí puede alterar un extremo local: la función cero tiene $L=U=0$, mientras al poner altura uno en $c=1/2$, sobre las mitades queda $L=0$ y $U=1$. Las dos funciones tienen integral cero.

## 23.36. Cotas exteriores

[]{#MA-EX-ANM-01-023-036}

[]{#MA-SOL-ANM-01-023-036}

[]{#MA-SEC-ANM-01-023-008}

Sean $A=\sum_i a_i\Delta_i$ y $C=\sum_i b_i\Delta_i$. La hipótesis universal en la pieza da $a_i\le m_i\le M_i\le b_i$. Ponderar por anchuras positivas y sumar produce $A\le L(f,P)\le I_f\le U(f,P)\le C$, usando que la integral ya existe. Para $H=(A+C)/2$, cualquier real en $[A,C]$ está a distancia a lo sumo $(C-A)/2$ de $H$. En particular $|H-I_f|\le(C-A)/2$. El certificado puede ser menos ajustado que el de Darboux si las cotas exteriores no son los extremos exactos.

## 23.37. Elegir resolución de un certificado

[]{#MA-EX-ANM-01-023-037}

[]{#MA-SOL-ANM-01-023-037}

Para la uniforme de $n\ge1$ piezas, las sumas del cuadrado son $L_n=1/3-1/(2n)+1/(6n^2)$ y $U_n=1/3+1/(2n)+1/(6n^2)$, obtenidas de las identidades finitas de C22. Su brecha es $1/n$ y su centro $H_n=1/3+1/(6n^2)$. El certificado de encierro da $|H_n-I|\le1/(2n)$. Tomando $n=51$, se obtiene $1/102<1/100$, por lo que cumple la resolución pedida. La fórmula permite además ver que el error real es $1/(6\cdot51^2)=1/15606$. Una suma etiquetada arbitraria recibe la cota $1/n$; para certificar el mismo umbral a todas ellas mediante esa cota haría falta $n>100$.

## 23.38. El pico se encierra

[]{#MA-EX-ANM-01-023-038}

[]{#MA-SOL-ANM-01-023-038}

Para $0<r<1/2$, los cinco nodos dados son estrictamente crecientes. Cada pieza contiene entradas diferentes de $1/2$, donde $p=0$, así todos los ínfimos son cero y $L=0$. Sólo $[1/2-r,1/2]$ y $[1/2,1/2+r]$ contienen el pico; sus supremos son uno y cada anchura vale $r$. Por tanto $U=2r$ y $G=2r$. Dado $\varepsilon>0$, elegimos $r=\min(1/4,\varepsilon/4)$; cumple $0<r<1/2$ y $2r\le\varepsilon/2<\varepsilon$. Darboux prueba integrabilidad. Todas las sumas inferiores valen cero, así $\ell_p=0$; la coincidencia de extremos da $I_p=0$.

**Retorno visual.** Véase [C23-F08](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.39. Integrable sin brecha cero

[]{#MA-EX-ANM-01-023-039}

[]{#MA-SOL-ANM-01-023-039}

Sea $P$ cualquier partición de $[0,1]$. Como sus piezas cubren el intervalo, alguna contiene $1/2$. Esa pieza tiene anchura positiva, por lo que contiene otra entrada distinta de $1/2$. La imagen sobre ella contiene cero y uno y sólo esas alturas, así su oscilación es uno. Su contribución a la brecha es su anchura, estrictamente positiva; las demás contribuciones son no negativas. Luego $G(p,P)>0$ para toda partición. El ejercicio anterior proporciona brechas arbitrariamente pequeñas y prueba integral cero. Así el ínfimo de las brechas puede ser cero aunque ninguna brecha lo alcance.

## 23.40. Brecha persistente

[]{#MA-EX-ANM-01-023-040}

[]{#MA-SOL-ANM-01-023-040}

Suponemos $a<b$ y que la función sólo toma cero y uno, alcanzando ambas alturas en toda pieza no degenerada. Cada pieza de cualquier partición tiene anchura positiva y por hipótesis su ínfimo es cero y su supremo uno. Por tanto $L(f,P)=0$ y $U(f,P)=\sum_i\Delta_i=b-a$. Los conjuntos de sumas son $\mathcal L_f=\{0\}$ y $\mathcal U_f=\{b-a\}$, así $\ell_f=0$ y $u_f=b-a>0$. También el criterio falla con $\varepsilon=(b-a)/2$, pues ninguna brecha es menor que ella. La hipótesis sobre todas las piezas sostiene el argumento; una colección finita de muestras no demostraría esa distribución de alturas.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html)
