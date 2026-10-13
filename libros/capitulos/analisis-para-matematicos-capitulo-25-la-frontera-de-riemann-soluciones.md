---
content-id: MA-BCH-0304
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-025-SOLUCIONES
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
title: Soluciones — Capítulo 25
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C25_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)

## 25.1. Longitud de las piezas malas

[]{#MA-EX-ANM-01-025-001}

[]{#MA-SOL-ANM-01-025-001}

[]{#MA-SEC-ANM-01-025-001}

Sea $\mathcal B=\{i:\omega_i\ge\eta\}$ y $\lambda=\sum_{i\in\mathcal B}\Delta_i$. En el grupo malo, $\omega_i\Delta_i\ge\eta\Delta_i$. Los restantes productos son no negativos, por lo que $G=\sum_i\omega_i\Delta_i\ge\eta\lambda$. Para la cota superior, las piezas buenas cumplen $\omega_i<\eta$ y las malas $\omega_i\le2B$, deducido de $-B\le f\le B$. Así $G\le\eta\sum_{i\notin\mathcal B}\Delta_i+2B\sum_{i\in\mathcal B}\Delta_i=\eta((b-a)-\lambda)+2B\lambda\le\eta(b-a)+2B\lambda$. Sólo se han usado orden, anchuras positivas y la suma finita de longitudes.

**Retorno visual.** Véase [C25-F01](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.2. Oscilación puntual y continuidad

[]{#MA-EX-ANM-01-025-002}

[]{#MA-SOL-ANM-01-025-002}

Si $f$ es continua relativamente en $x$, dado $\varepsilon>0$ existe $r>0$ con $|f(t)-f(x)|<\varepsilon/3$ para todas las entradas de $V_r(x)$. Dos alturas de esa vecindad difieren en magnitud menos que $2\varepsilon/3$, así su oscilación es a lo sumo esa cantidad. Luego $0\le\Omega_f(x)\le2\varepsilon/3$ para toda tolerancia, obligando a $\Omega_f(x)=0$. Recíprocamente, si el ínfimo es cero, su propiedad de aproximación proporciona para cada $\varepsilon>0$ un radio con $\omega(f,V_r(x))<\varepsilon$. El centro pertenece a la vecindad, así $|f(t)-f(x)|\le\omega(f,V_r(x))<\varepsilon$ para todas sus entradas. Ésta es continuidad con ese radio; no se necesita que el ínfimo se alcance.

## 25.3. Nivel cerrado

[]{#MA-EX-ANM-01-025-003}

[]{#MA-SOL-ANM-01-025-003}

Si $x\notin D_\eta$, se tiene $\Omega_f(x)<\eta$ y algún radio $r>0$ cumple $\omega(f,V_r(x))<\eta$. Para $y$ del dominio con $|y-x|<r/2$, la triangular muestra $V_{r/2}(y)\subseteq V_r(x)$. La oscilación disminuye al restringir, así $\Omega_f(y)\le\omega(f,V_{r/2}(y))\le\omega(f,V_r(x))<\eta$. Toda esa vecindad relativa de centros queda fuera del nivel. Por tanto su complemento es abierto relativo y $D_\eta$ es cerrado en $[a,b]$. Como el segmento es compacto, C16 hace compacto al nivel, incluido el caso vacío.

## 25.4. Un presupuesto numérico

[]{#MA-EX-ANM-01-025-004}

[]{#MA-SOL-ANM-01-025-004}

Sustituimos los datos en la cota $G\le\eta(b-a)+2B\lambda$. Resulta $G\le(1/10)\cdot3+2\cdot2\cdot(1/100)=3/10+1/25=17/50$. Es un certificado superior de $0,34$. No determina la brecha exacta, porque las amplitudes reales de las piezas pueden ser menores que los límites usados. En particular, la suma de anchuras malas no informa por sí sola de cuánto supera cada oscilación el nivel.

## 25.5. Nodos y oscilación

[]{#MA-EX-ANM-01-025-005}

[]{#MA-SOL-ANM-01-025-005}

Las piezas $[x_{i-1},x_i]$ y $[x_i,x_{i+1}]$ contienen el nodo compartido $x_i$. Si la tasa es cero salvo por altura uno en ese nodo, las dos piezas tienen ínfimo cero y supremo uno. Su contribución a la brecha es la suma de sus dos anchuras. No aparece un término separado por el punto: su efecto está en las imágenes de las piezas que lo incluyen. Al afinar alrededor del nodo esas anchuras pueden hacerse pequeñas, y la invariancia ante cambios finitos de C23 conserva el valor integral.

## 25.6. Collares de un conjunto finito

[]{#MA-EX-ANM-01-025-006}

[]{#MA-SOL-ANM-01-025-006}

[]{#MA-SEC-ANM-01-025-002}

Sea $E=\{e_1,\ldots,e_k\}$ y $\sigma>0$. Si $k>0$, tomamos $r=\sigma/[4(k+1)]>0$ y los intervalos abiertos $(e_j-r,e_j+r)$. Cubren todos los puntos, incluidos los extremos del dominio, aunque parte del collar quede fuera del segmento. La suma de longitudes es $2kr=\sigma k/[2(k+1)]<\sigma$. Si $k=0$, la cobertura vacía tiene longitud total cero y cumple el pedido. El denominador $k+1$ mantiene la fórmula definida sin dividir por el número de puntos.

## 25.7. Fabricar una escala común

[]{#MA-EX-ANM-01-025-007}

[]{#MA-SOL-ANM-01-025-007}

Sea $O$ la unión de los collares que cubren las excepciones. Consideramos todos los pares $(x,r)$ de dos tipos: si $x\in O$, se pide $V_r(x)\subseteq O$; si $x\notin O$, se pide $\omega(f,V_r(x))<\eta$. La apertura da pares del primer tipo y la continuidad fuera de las excepciones da pares del segundo. Las vecindades $V_{r/2}(x)$ de todos esos pares cubren $[a,b]$. Compacidad extrae finitísimos y permite tomar $\delta$ como el mínimo positivo de sus radios medios. Para una pieza de malla menor que $\delta$, escogemos un punto suyo en una de las vecindades medias. La triangular coloca todos los demás puntos en la vecindad grande. Así cada pieza está dentro de $O$ o tiene oscilación menor que $\eta$. La construcción sólo selecciona una lista finita de pares después de formar la cubierta completa.

## 25.8. El escalón y su brecha

[]{#MA-EX-ANM-01-025-008}

[]{#MA-SOL-ANM-01-025-008}

Las anchuras de la partición son $1/2-r,r,r,1/2-r$. En las dos primeras piezas los ínfimos son cero; la segunda tiene supremo uno por incluir el corte de valor uno. Las dos últimas son constantes uno. Por tanto $L=r+(1/2-r)=1/2$ y $U=r+r+(1/2-r)=1/2+r$. La brecha exacta es $r$. Las dos piezas adyacentes al corte tienen longitud total $2r$, que proporciona una cota más amplia: sólo la izquierda oscila con la convención nodal dada. La cuenta conserva la altura del corte en las dos imágenes cerradas.

**Retorno visual.** Véase [C25-F02](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.9. La hipótesis de acotación

[]{#MA-EX-ANM-01-025-009}

[]{#MA-SOL-ANM-01-025-009}

En $[0,1]$, definimos $h(0)=0$ y $h(x)=1/x$ para $x>0$. Es continua en todas las entradas positivas y sólo falla en cero. Para cualquier $B>0$, la entrada $x=1/(B+1)\in(0,1]$ tiene altura $h(x)=B+1>B$. Por tanto no es acotada. C23 probó que el contrato propio de Riemann obliga acotación, así esta tasa no es integrable en ese sentido. Tener sólo un punto de discontinuidad no permite omitir la hipótesis de amplitud global finita.

## 25.10. Gastar la tolerancia

[]{#MA-EX-ANM-01-025-010}

[]{#MA-SOL-ANM-01-025-010}

Sean $a<b$, $|f|\le B$ y $\varepsilon>0$. Con $\eta=\varepsilon/[2(b-a)]$ y $\sigma=\varepsilon/[4(B+1)]$, la clasificación de R2 da longitud mala menor que $\sigma$. La cota de R1 implica $G\le\eta(b-a)+2B\sigma=\varepsilon/2+B\varepsilon/[2(B+1)]$. Como $B/(B+1)<1$, el último número es estrictamente menor que $\varepsilon$. Las desigualdades no estrictas obtenidas al sumar no agotan el margen. Si $B=0$, la función y la brecha son cero; los mismos parámetros permanecen definidos.

## 25.11. Racionales en toda pieza

[]{#MA-EX-ANM-01-025-011}

[]{#MA-SOL-ANM-01-025-011}

[]{#MA-SEC-ANM-01-025-003}

Fijemos $u<v$. Arquimedianidad da un natural $n\ge1$ con $n(v-u)>1$. Para admitir cualquier signo de $u$, elegimos un natural $M$ con $nu+M\ge0$. El conjunto de naturales estrictamente mayores que $nu+M$ es no vacío, así tiene mínimo $j$. Como $j>0$, la minimalidad da $j-1\le nu+M$. Ponemos el entero $k=j-M$. Entonces $nu<k\le nu+1<nv$. Dividir por $n>0$ da $u<k/n<v$. El traslado por $M$ sólo permitió usar el mínimo natural; al restarlo queda un numerador entero, quizá negativo, y una fracción racional interior.

## 25.12. Irracionales en toda pieza

[]{#MA-EX-ANM-01-025-012}

[]{#MA-SOL-ANM-01-025-012}

Por densidad racional, tomamos $r\in\mathbb Q$ con $u<r<v$. El número $v-r$ es positivo, así arquimedianidad proporciona $n\ge1$ con $\sqrt2/n<v-r$. Definimos $z=r+\sqrt2/n$. Entonces $u<r<z<v$. Si $z$ fuera racional, la diferencia $z-r$ y su múltiplo entero $n(z-r)$ serían racionales. Pero ese múltiplo es $\sqrt2$, cuya irracionalidad se probó mediante reducción de una fracción y paridad. La contradicción hace a $z$ un testigo irracional dentro del intervalo.

## 25.13. La longitud correcta

[]{#MA-EX-ANM-01-025-013}

[]{#MA-SOL-ANM-01-025-013}

Cada pieza de una partición de $[-1,2]$ tiene longitud positiva y contiene racionales e irracionales. Para Dirichlet, su imagen es por tanto $\{0,1\}$, con ínfimo cero, supremo uno y oscilación uno. Resulta $L(d,P)=0$, $U(d,P)=\sum_i\Delta_i=2-(-1)=3$ y $G(d,P)=3$ para todas las particiones. Con tolerancia $\varepsilon=3/2$, ninguna brecha es menor que ella, así falla Darboux. La suma superior es la longitud tres, no uno.

**Retorno visual.** Véase [C25-F03](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.14. Etiquetas incompatibles

[]{#MA-EX-ANM-01-025-014}

[]{#MA-SOL-ANM-01-025-014}

Supongamos que existe un candidato integral $I$ sobre $[a,b]$, con $a<b$. Pedimos al contrato error $\varepsilon=(b-a)/3$ y obtenemos un radio $\delta>0$. C22 permite construir una uniforme de malla menor que $\delta$. En cada pieza, densidad da una etiqueta racional y una irracional; inducción finita forma las dos familias. La primera suma vale $b-a$ y la segunda cero. Ambas deberían estar a distancia menor que $\varepsilon$ de $I$. La triangular daría $b-a\le|b-a-I|+|I|<2(b-a)/3$, imposible. El problema persiste por fina que sea la malla.

## 25.15. Una muestra no prueba densidad

[]{#MA-EX-ANM-01-025-015}

[]{#MA-SOL-ANM-01-025-015}

Una representación de Dirichlet dibuja finitísimas entradas de cada tipo. Siempre puede elegirse un intervalo pequeño que evite todas las entradas dibujadas. El cálculo de los extremos requiere, sin embargo, una altura cero y una altura uno en cada pieza no degenerada real. Las pruebas aritméticas construyen esos testigos para un intervalo arbitrario, sin depender de una resolución gráfica. Sólo después de establecer esa densidad puede concluirse que todas las oscilaciones valen uno.

## 25.16. Contar picos de denominador pequeño

[]{#MA-EX-ANM-01-025-016}

[]{#MA-SOL-ANM-01-025-016}

[]{#MA-SEC-ANM-01-025-004}

Para un denominador $q$ con $1\le q\le N$, hay $q+1$ posibles numeradores enteros de cero a $q$. Antes de reducir y quitar duplicados hay por tanto $\sum_{q=1}^N(q+1)=N(N+1)/2+N=N(N+3)/2$ candidatos. Cada entrada de $E_N$ aparece entre ellos, así ésa es una cota cardinal. Para $N=4$, las fracciones reducidas distintas dan, en orden, $E_4=\{0,1/4,1/3,1/2,2/3,3/4,1\}$. Tiene siete entradas; la cota general es catorce, mayor porque cuenta también representaciones repetidas y no reducidas.

**Retorno visual.** Véase [C25-F04](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.17. Un irracional evita picos grandes

[]{#MA-EX-ANM-01-025-017}

[]{#MA-SOL-ANM-01-025-017}

Sea $x\in[0,1]$ irracional y $\varepsilon>0$. Elegimos $N\ge1$ con $1/(N+1)<\varepsilon$. El conjunto finito $E_N$ no contiene a $x$, así las distancias $|x-e|$, con $e\in E_N$, son positivas y tienen mínimo $d>0$. Si $|t-x|<d/2$, la entrada $t$ no pertenece a $E_N$. Allí la altura es cero si es irracional y a lo sumo $1/(N+1)$ si es racional. Como $T(x)=0$, queda $|T(t)-T(x)|\le1/(N+1)<\varepsilon$. El radio $d/2$ demuestra continuidad en $x$ con control de todos los picos omitidos.

## 25.18. Oscilación en un racional

[]{#MA-EX-ANM-01-025-018}

[]{#MA-SOL-ANM-01-025-018}

Sea $x=p/q$ en forma reducida. Cada vecindad relativa contiene al centro, con altura $1/q$, y a un irracional, con altura cero. Por tanto todas sus oscilaciones son al menos $1/q$. El conjunto $E_q\setminus\{x\}$ es finito y no contiene el centro; elegimos un radio que lo evite, mediante el mínimo de distancias positivas, o cualquier radio si es vacío. En esa vecindad las demás alturas racionales son a lo sumo $1/(q+1)$, mientras el centro conserva la mayor altura $1/q$. El ínfimo es cero por densidad irracional y el supremo $1/q$, así una oscilación vale exactamente ese número. Se concluye $\Omega_T(x)=1/q$. Los irracionales cercanos, con error $1/q$, refutan continuidad usando tolerancia $1/(2q)$.

## 25.19. Un certificado para Thomae

[]{#MA-EX-ANM-01-025-019}

[]{#MA-SOL-ANM-01-025-019}

Separamos las piezas que tocan $E_N$ de las restantes. En las primeras el supremo de $T$ es a lo sumo uno, así su suma superior aporta a lo sumo su longitud total, que no supera $\alpha$. Ninguna entrada de las otras pertenece a $E_N$, por lo que sus supremos son a lo sumo $1/(N+1)$. Sus anchuras suman a lo sumo uno, y su contribución no supera $1/(N+1)$. Así $U(T,P)\le\alpha+1/(N+1)$. Todos los ínfimos son cero por densidad irracional. Para una tolerancia elegimos primero $N$ con el segundo término menor que $\varepsilon/2$ y después collares y malla que hagan $\alpha<\varepsilon/2$. Esto prueba brechas arbitrariamente pequeñas e integral cero.

## 25.20. Discontinuidades densas, integral cero

[]{#MA-EX-ANM-01-025-020}

[]{#MA-SOL-ANM-01-025-020}

Dirichlet mantiene las alturas cero y uno en toda vecindad; su oscilación puntual es uno y su brecha en $[0,1]$ es siempre uno. Thomae vale cero en los irracionales y en los racionales tiene altura inversa al denominador reducido. Para cada nivel positivo sólo finitísimos picos lo alcanzan. Una cobertura corta de esos picos limita su aporte superior, y la cota universal de los demás limita el resto. Se obtienen sumas superiores arbitrariamente pequeñas y sumas inferiores cero, de modo que Thomae integra cero. Aunque ambas tienen discontinuidades en todos los racionales, sus amplitudes en vecindades pequeñas son diferentes. El argumento utiliza denominadores y coberturas finitas, sin un criterio de medida.

## 25.21. Cubrir los niveles desde una brecha

[]{#MA-EX-ANM-01-025-021}

[]{#MA-SOL-ANM-01-025-021}

[]{#MA-SEC-ANM-01-025-005}

Fijemos $\eta,\sigma>0$. La integrabilidad proporciona $P$ con $G(f,P)<\eta\sigma/4$. Por R1, las piezas malas de oscilación al menos $\eta$ suman longitud $\lambda<\sigma/4$. Si un punto de $D_\eta$ no es nodo, está en el interior de una pieza; una pieza buena admitiría allí una vecindad de oscilación menor que $\eta$, contradicción. Así el nivel queda cubierto por las piezas malas y los nodos. Si hay $n$ piezas, ponemos $r=\sigma/[8(n+1)]$. Ampliamos cada pieza mala en $r$ por ambos lados y cubrimos cada uno de los $n+1$ nodos con un intervalo abierto de radio $r$. Hay a lo sumo $n$ malas y la longitud total de la cobertura es a lo sumo $\lambda+2r(2n+1)<\sigma/4+\sigma/2=3\sigma/4<\sigma$. Los intervalos reales también cubren los nodos de borde. Queda probado el contenido finito nulo de cada nivel.

## 25.22. De niveles pequeños a integrabilidad

[]{#MA-EX-ANM-01-025-022}

[]{#MA-SOL-ANM-01-025-022}

Supongamos $|f|\le B$ y contenido finito nulo de cada nivel positivo. Para $\varepsilon>0$, fijamos $\eta=\varepsilon/[2(b-a)]$ y $\sigma=\varepsilon/[4(B+1)]$. Cubrimos $D_\eta$ por finitísimos abiertos de longitud total menor que $\sigma$, cuya unión llamamos $O$. Fuera de $O$ se tiene $\Omega_f(x)<\eta$, así algún radio da oscilación menor que $\eta$; dentro, la apertura da un radio cuya vecindad cabe en $O$. Los radios medios de todos los pares válidos cubren el segmento. Compacidad extrae una lista finita y su mínimo radio medio $\delta>0$. Una uniforme de malla menor que $\delta$ tiene cada pieza dentro de $O$ o en una vecindad buena. Las piezas malas deben ser del primer tipo, y la comparación finita de longitudes da $\lambda<\sigma$. R1 implica $G\le\varepsilon/2+B\varepsilon/[2(B+1)]<\varepsilon$. Darboux prueba integrabilidad; para $B=0$ la tasa es cero y la conclusión es inmediata.

## 25.23. No cubrir toda la unión

[]{#MA-EX-ANM-01-025-023}

[]{#MA-SOL-ANM-01-025-023}

En Thomae, $\Omega_T(p/q)=1/q$ para racionales y cero para irracionales. Para un $\eta>0$ fijo, el nivel $D_\eta$ sólo puede contener denominadores $q\le1/\eta$, así es finito y admite collares arbitrariamente cortos. La unión de esos niveles sobre todos los valores positivos de $\eta$ es $\mathbb Q\cap[0,1]$, porque cada racional tiene una amplitud positiva. Esa unión es densa y cualquier cobertura abierta finita suya tiene longitud total al menos uno, como se demuestra cerrando los intervalos y usando densidad. Por tanto una tasa integrable puede tener todos los niveles con contenido finito nulo y no tener esa propiedad en el conjunto completo de discontinuidades.

**Retorno visual.** Véase [C25-F05](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.24. Longitud de una cobertura del segmento

[]{#MA-EX-ANM-01-025-024}

[]{#MA-SOL-ANM-01-025-024}

Cortamos $[a,b]$ en los finitísimos extremos de los intervalos de cobertura que queden dentro del segmento, añadiendo $a,b$. En cada celda abierta entre cortes consecutivos, la pertenencia a cada intervalo de cobertura es constante, porque no hay un extremo interior que la cambie. Como la cobertura contiene todo el segmento, cada celda está en al menos uno de los intervalos. Las longitudes de las celdas suman $b-a$. Si se suman las longitudes de los intervalos, cada celda cubierta se cuenta al menos una vez, quizá más, y las partes exteriores sólo agregan longitud. Así la suma total es al menos $b-a$. Los finitísimos cortes no aportan anchura propia.

## 25.25. Los casos vacíos

[]{#MA-EX-ANM-01-025-025}

[]{#MA-SOL-ANM-01-025-025}

El vacío tiene una cobertura vacía cuya suma de longitudes es cero para cualquier tolerancia positiva. Para un conjunto de $k>0$ puntos, los collares de radio $\sigma/[4(k+1)]$ dan suma $\sigma k/[2(k+1)]<\sigma$. Así los conjuntos finitos tienen contenido finito nulo. Si la cota absoluta es $B=0$, entonces $f=0$, todas las oscilaciones puntuales son cero y todos los niveles positivos son vacíos. La brecha también es cero. En la suficiencia, el parámetro $\sigma=\varepsilon/[4(B+1)]$ sigue definido y positivo; no se requiere dividir por $B$.

## 25.26. Etapas ternarias

[]{#MA-EX-ANM-01-025-026}

[]{#MA-SOL-ANM-01-025-026}

[]{#MA-SEC-ANM-01-025-006}

La etapa cero consta de $[0,1]$, con una componente de longitud uno. Supongamos que $C_n$ tiene $2^n$ componentes de longitud $3^{-n}$. Quitar el tercio medio abierto de cada una deja dos segmentos cerrados de longitud $3^{-n}/3=3^{-(n+1)}$. Los huecos nuevos y los antiguos mantienen separadas las componentes, así hay $2\cdot2^n=2^{n+1}$. Esto prueba por inducción ambas fórmulas. La suma de longitudes en la etapa $n$ es $2^n3^{-n}=(2/3)^n$, porque las componentes no se solapan.

**Retorno visual.** Véase [C25-F06](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.27. Una cobertura abierta del conjunto final

[]{#MA-EX-ANM-01-025-027}

[]{#MA-SOL-ANM-01-025-027}

Cada $C_n$ es una unión finita de cerrados y $C=\bigcap_{n\ge0}C_n$ es cerrado. Está contenido en el compacto $[0,1]$, así es compacto por C16. Para $\sigma>0$, la convergencia geométrica permite elegir $n$ con $(2/3)^n<\sigma/2$. Cada una de las $2^n$ componentes $[u_j,v_j]$ se amplía al abierto $(u_j-r,v_j+r)$ con $r=\sigma/[8\cdot2^n]>0$. Cubren a $C$ porque $C\subseteq C_n$. La suma de longitudes es $(2/3)^n+2\cdot2^n r<\sigma/2+\sigma/4<\sigma$. Se obtiene contenido finito nulo mediante coberturas reales abiertas, también alrededor de cero y uno.

## 25.28. Interior vacío

[]{#MA-EX-ANM-01-025-028}

[]{#MA-SOL-ANM-01-025-028}

Supongamos que $C$ contiene un intervalo abierto no degenerado. Elegimos dentro de él un segmento cerrado $[u,v]$ de longitud $\ell=v-u>0$. Para $n$ suficientemente grande, $3^{-n}<\ell$. Como $C\subseteq C_n$, ese segmento debería quedar en la unión de las componentes de $C_n$. Si estuviera dentro de una sola, su longitud no podría exceder $3^{-n}$. Si tocara dos componentes distintas, contendría el hueco abierto que las separa, y por tanto algún punto fuera de $C_n$. Ambas posibilidades contradicen la inclusión. Luego $C$ tiene interior vacío. En sus bordes del dominio, una vecindad relativa completamente contenida en $C$ también contendría un intervalo abierto interior, así queda excluida.

## 25.29. Indicadora y discontinuidades

[]{#MA-EX-ANM-01-025-029}

[]{#MA-SOL-ANM-01-025-029}

Si $x\notin C$, la cerradura de $C$ da una vecindad relativa del centro disjunta de él. Allí la indicadora vale cero y es continua. Si $x\in C$, su valor es uno, pero toda vecindad relativa contiene alguna entrada fuera de $C$ por interior vacío; allí vale cero. El error uno impide continuidad con tolerancia $1/2$. Por tanto las discontinuidades son exactamente $C$, incluidos cero y uno relativamente. La función está entre cero y uno y es cero fuera del compacto $C$ de contenido finito nulo. El lema de soporte hace su integral existente y de valor cero.

## 25.30. Controlar todas las piezas que tocan el soporte

[]{#MA-EX-ANM-01-025-030}

[]{#MA-SOL-ANM-01-025-030}

Sea $E$ no vacío compacto y $O$ una unión abierta que lo cubre. Para todos los pares $(c,r)$ con $c\in E$, $r>0$ y $V_r(c)\subseteq O$, las vecindades $V_{r/2}(c)$ cubren $E$. Compacidad extrae finitísimos pares y da $\delta=\min_j r_j/2>0$. Si una pieza de malla menor que $\delta$ toca $E$ en $t$, elegimos una vecindad media que contenga a $t$. Para cualquier entrada $s$ de esa pieza, $|s-c_j|\le|s-t|+|t-c_j|<\delta+r_j/2\le r_j$, así toda la pieza está en $O$. El razonamiento funciona también cuando $t$ es un nodo de borde o compartido, y entonces controla ambas piezas que lo toquen. Sus interiores disjuntos permiten acotar la suma de anchuras por la longitud total de la cobertura. Si $E$ es vacío, no hay piezas afectadas.

## 25.31. Dos errores de salida, una oscilación

[]{#MA-EX-ANM-01-025-031}

[]{#MA-SOL-ANM-01-025-031}

[]{#MA-SEC-ANM-01-025-007}

Supongamos imágenes no vacías y acotadas y $|f(t)-g(t)|\le\delta$ para toda entrada de $I$. Para $s,t\in I$, escribimos $f(s)-f(t)=(f(s)-g(s))+(g(s)-g(t))+(g(t)-f(t))\le\omega(g,I)+2\delta$. Fijado $t$, tomar supremo en $s$ da $M_f-f(t)\le\omega(g,I)+2\delta$. Luego $M_f\le f(t)+\omega(g,I)+2\delta$ para toda $t$, y tomar ínfimo en $t$ produce $M_f\le m_f+\omega(g,I)+2\delta$. Restar $m_f$ prueba $\omega(f,I)\le\omega(g,I)+2\delta$. La optimalidad de las cotas sustituye a cualquier supuesto de extremos alcanzados.

## 25.32. Aproximantes integrables certifican existencia

[]{#MA-EX-ANM-01-025-032}

[]{#MA-SOL-ANM-01-025-032}

Sea $f$ acotada y supongamos que para toda $\delta>0$ existe una integrable $g$ con error global a lo sumo $\delta$. Dada $\varepsilon>0$, elegimos $\delta=\varepsilon/[4(b-a)]$ y una $g$ correspondiente. Darboux proporciona una partición con $G(g,P)<\varepsilon/2$. La comparación de oscilaciones ponderadas da $G(f,P)\le G(g,P)+2\delta(b-a)<\varepsilon$. Por tanto $f$ es integrable. Con su integral ya existente, para cualquier aproximante integrable de error global $\delta$, la diferencia $f-g$ es integrable y satisface $-\delta\le f-g\le\delta$. Orden y linealidad dan $|\int_a^b f-\int_a^b g|\le\delta(b-a)$. La prueba de existencia precede a esta comparación de valores.

## 25.33. Truncar alturas de Thomae

[]{#MA-EX-ANM-01-025-033}

[]{#MA-SOL-ANM-01-025-033}

Para $N\ge1$, definimos $T_N(x)=T(x)$ si $x\in E_N$ y cero en las demás entradas. Tiene soporte finito, por lo que es integrable con valor cero por cambios finitos de la tasa nula. En $E_N$ el error es cero; fuera, la altura de $T$ no supera $1/(N+1)$. Así $|T-T_N|\le1/(N+1)$ universalmente. Como esas cotas tienden a cero y $T$ está acotada, R7 prueba su integrabilidad. Después, la cota de diferencia de integrales en longitud uno da $|I_T|\le1/(N+1)$ para todo $N\ge1$. Una distancia positiva quedaría contradicha por un $N$ suficientemente grande, así $I_T=0$.

## 25.34. Estabilizar entradas no controla la familia

[]{#MA-EX-ANM-01-025-034}

[]{#MA-SOL-ANM-01-025-034}

Para un racional $x=p/q$ reducido, se tiene $x\in E_N$ desde $N\ge q$, así $d_N(x)=1$ a partir de ese índice. Para un irracional, $d_N(x)=0$ para todo $N$. Cada entrada se estabiliza en su altura de Dirichlet. Sin embargo, para cada $N\ge1$ la entrada $x_N=1/(N+1)$ tiene denominador reducido $N+1$ y queda fuera de $E_N$. Allí $d_N(x_N)=0$ y $d(x_N)=1$. El error global es por tanto al menos uno y, como ambas alturas están entre cero y uno, exactamente uno. Ningún índice controla todas las entradas con error menor que $1/2$, aunque cada entrada fija acabe estabilizada.

**Retorno visual.** Véase [C25-F07](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 25.35. Regla finita y cambios infinitos

[]{#MA-EX-ANM-01-025-035}

[]{#MA-SOL-ANM-01-025-035}

Sobre $[0,1]$, sustituimos las alturas de la tasa cero en los racionales de dos maneras. Si ponemos en cada fracción reducida $p/q$ la altura $1/q$, obtenemos Thomae, integrable con valor cero por la separación de picos grandes y alturas pequeñas. Si ponemos altura uno en todos los racionales, obtenemos Dirichlet, no integrable por su brecha fija. En ambos casos el conjunto modificado es la misma colección numerable de racionales. El resultado de cambios finitos de C23 no decide ninguna modificación infinita por sí solo; las amplitudes y su distribución requieren una prueba nueva.

## 25.36. Una cobertura de racionales

[]{#MA-EX-ANM-01-025-036}

[]{#MA-SOL-ANM-01-025-036}

[]{#MA-SEC-ANM-01-025-008}

Supongamos una cobertura de $\mathbb Q\cap[0,1]$ por los abiertos $(u_j,v_j)$, $1\le j\le k$. Su unión $O$ contiene un conjunto denso en $[0,1]$, así $[0,1]\subseteq\overline O$. Como la unión es finita, $\overline O=\bigcup_{j=1}^k[u_j,v_j]$. Los intervalos cerrados conservan las longitudes $v_j-u_j$. Cortar en sus finitísimos extremos demuestra que una cobertura del segmento tiene suma de longitudes al menos uno. Por tanto $\sum_j(v_j-u_j)\ge1$ para la cobertura abierta original. La tolerancia $\sigma=1/2$ no admite una cobertura de ese tipo, refutando el contenido finito nulo.

## 25.37. Un punto problemático no acotado

[]{#MA-EX-ANM-01-025-037}

[]{#MA-SOL-ANM-01-025-037}

La tasa $h(0)=0$, $h(x)=1/x$ para $x>0$, toma valores reales en todo $[0,1]$. Si fuera integrable propiamente, C23 daría una cota absoluta finita $B\ge0$. Elegimos $x=1/(B+2)$, que está en $(0,1]$, y obtenemos $h(x)=B+2>B$, contradicción. La tasa es continua en las entradas positivas, pero la pérdida de acotación al acercarse a cero impide el contrato propio. No se necesita investigar otro tipo de integral para esta conclusión.

## 25.38. Qué certifica una etapa de Cantor

[]{#MA-EX-ANM-01-025-038}

[]{#MA-SOL-ANM-01-025-038}

La cantidad $(2/3)^n$ es la suma de longitudes de los finitísimos componentes de $C_n$. Como $C\subseteq C_n$, ampliar esos componentes proporciona una cobertura abierta del conjunto final con longitud próxima a esa suma. El conjunto $C$ es la intersección de todas las etapas, no una de ellas. Por ejemplo $1/(2\cdot3^n)$ está en la componente izquierda de $C_n$ y se elimina al quitar su tercio medio en el paso siguiente. La etapa certifica una envolvente útil para cubrir $C$; no afirma que todos sus intervalos sobrevivan ni construye una medida de la intersección.

## 25.39. Frontera exacta y condición más fuerte

[]{#MA-EX-ANM-01-025-039}

[]{#MA-SOL-ANM-01-025-039}

Para una función acotada en un cerrado no degenerado, R5 afirma $f$ integrable si y sólo si cada $D_\eta=\{x:\Omega_f(x)\ge\eta\}$, con $\eta>0$, tiene contenido finito nulo. Si el conjunto completo de discontinuidades tuviera esa propiedad, cada nivel, al estar contenido en él, la heredaría y R5 daría integrabilidad. Es una condición suficiente más fuerte. Thomae muestra que no es necesaria: sus niveles positivos son finitos y la tasa integra cero, mientras sus discontinuidades son todos los racionales del segmento y no tienen contenido finito nulo.

## 25.40. Cerrar sin importar otra integral

[]{#MA-EX-ANM-01-025-040}

[]{#MA-SOL-ANM-01-025-040}

Dirichlet mantiene amplitud uno en toda pieza, así su brecha positiva fija impide integrabilidad. Thomae permite separar una colección finita de picos grandes y cubrirla con longitud pequeña, mientras una cota aritmética controla todos los picos restantes; integra cero. La indicadora de Cantor confina sus alturas no nulas en un compacto con coberturas finitas arbitrariamente cortas y también integra cero. Estas decisiones usan oscilación, compacidad y sumas finitas de longitudes. El capítulo no construye una medida ni una integral de Lebesgue y no asigna con ellas un valor a Dirichlet. El contraste de aproximantes deja preparada la cuestión del control de sucesiones de funciones.

**Retorno visual.** Véase [C25-F08](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html#fig-anm-c25-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 25](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann.html) · [Ejercicios](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-25-la-frontera-de-riemann-microcontroles.html)
