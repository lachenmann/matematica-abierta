---
content-id: MA-BCH-0316
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-028-SOLUCIONES
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
title: Soluciones — Capítulo 28
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C28_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html)

## 28.1. Una fila dentro de la banda

[]{#MA-EX-ANM-01-028-001}

[]{#MA-SOL-ANM-01-028-001}

[]{#MA-SEC-ANM-01-028-001}

Fijamos $\varepsilon>0$. Uniformidad da una fila $f_N$ con error menor que $\varepsilon/3$ en toda entrada. Continuidad de esa fila en $x_0$ entrega un radio para $|f_N(x)-f_N(x_0)|<\varepsilon/3$. La triangular entre $f(x),f_N(x),f_N(x_0),f(x_0)$ suma tres errores menores que $\varepsilon/3$. El mismo radio controla todas las entradas relativas próximas; no necesita controlar todas las filas.

**Retorno visual.** Véase [C28-F01](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.2. Radios para todos los pares

[]{#MA-EX-ANM-01-028-002}

[]{#MA-SOL-ANM-01-028-002}

Escogemos una fila con error uniforme menor que $\varepsilon/3$. La continuidad uniforme de esa fila produce un radio para todo par $x,y$. Sumamos error de aproximación en $x$, variación de la fila y error en $y$. El resultado es menor que $\varepsilon$ para todo par próximo. El radio depende de la tolerancia y de la fila fijada, que es suficiente.

## 28.3. Destino continuo sin uniformidad

[]{#MA-EX-ANM-01-028-003}

[]{#MA-SOL-ANM-01-028-003}

Para cada entrada $x<1$, $x^n\to0$, cuyo destino es continuo. Para cada $n\ge1$, Bernoulli produce valores de $x^n$ arbitrariamente próximos a uno desde abajo; su supremo es uno. Las envolventes no tienden a cero. Por tanto continuidad del destino no obliga uniformidad.

## 28.4. Valores sin barrera global

[]{#MA-EX-ANM-01-028-004}

[]{#MA-SOL-ANM-01-028-004}

La diferencia con la identidad es constante $1/(n+1)$ y tiende a cero uniformemente. Todas las filas y el límite satisfacen $|f(x)-f(y)|=|x-y|$, de modo que son uniformemente continuos. Sus valores son no acotados: para cualquier barrera se elige una entrada positiva suficientemente grande. R1 no necesita una barrera de valores.

## 28.5. Filas continuas arbitrariamente tardías

[]{#MA-EX-ANM-01-028-005}

[]{#MA-SOL-ANM-01-028-005}

Para la tolerancia $\varepsilon/3$, el corte uniforme es $N$. La hipótesis entrega un índice $n\ge N$ de una fila continua en $x_0$. Fijamos esa fila y su radio de continuidad. Los errores de aproximación en ambas entradas son menores que $\varepsilon/3$ por pertenecer a la cola, y la variación central también. La triangular prueba continuidad del límite; no hay que construir una subsecuencia infinita.

## 28.6. Construir el destino de los destinos

[]{#MA-EX-ANM-01-028-006}

[]{#MA-SOL-ANM-01-028-006}

[]{#MA-SEC-ANM-01-028-002}

Para $\eta>0$, Cauchy uniforme de las filas da $N$ con diferencias menores que $\eta/2$ para toda entrada y todo par posterior. Fijamos $m,n\ge N$ y pasamos la entrada al punto de acumulación. C13 conserva la cota débil: $|p_n-p_m|\le\eta/2<\eta$. El mismo corte controla todos los pares. C10 entrega el único destino real $p$.

## 28.7. El límite que aún no existía

[]{#MA-EX-ANM-01-028-007}

[]{#MA-SOL-ANM-01-028-007}

Una vez construido $p=\lim_n p_n$, fijamos una fila posterior tanto al corte uniforme para $\varepsilon/3$ como al de $|p_n-p|<\varepsilon/3$. Su límite relativo entrega un radio con $|f_n(x)-p_n|<\varepsilon/3$ en la ventana perforada. La suma de esas tres diferencias prueba $f(x)\to p$. El valor de $f(a)$ no participa.

## 28.8. Iterados diferentes

[]{#MA-EX-ANM-01-028-008}

[]{#MA-SOL-ANM-01-028-008}

Para una entrada positiva fija, el cociente tiende a uno, cuyo límite al acercarse a cero es uno. Para un índice fijo, el cociente tiende a cero cuando la entrada tiende a cero; el límite de esos destinos es cero. En la ruta indicada el numerador vale uno y el denominador dos, así el valor es $1/2$ en todas las etapas. El error respecto del límite puntual es $1/[1+(n+1)x]$, cuyo supremo es uno; no hay uniformidad.

**Retorno visual.** Véase [C28-F02](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.9. Uniformidad en una ventana fija

[]{#MA-EX-ANM-01-028-009}

[]{#MA-SOL-ANM-01-028-009}

Restringimos todas las filas a ese dominio común. Sigue acumulando en $a$, y los límites relativos originales se conservan por restricción a una ventana fija. Aplicamos R2 allí. El límite de $f$ obtenido en la ventana es también su límite en $X$ porque todo argumento suficientemente próximo y distinto del centro pertenece a ella. Ventanas distintas por índice no permiten esta reducción.

## 28.10. Una ruta conjunta

[]{#MA-EX-ANM-01-028-010}

[]{#MA-SOL-ANM-01-028-010}

La diferencia con $p$ está bajo $|f_n(x_n)-f(x_n)|+|f(x_n)-p|$. El primer término tiende a cero por el corte uniforme, independiente de la entrada elegida. El segundo lo hace por el límite relativo de $f$ y la ruta perforada dada. Cortes para $\varepsilon/2$ y su máximo completan el contrato. No se necesita seleccionar una ruta.

## 28.11. La cubierta creciente

[]{#MA-EX-ANM-01-028-011}

[]{#MA-SOL-ANM-01-028-011}

[]{#MA-SEC-ANM-01-028-003}

El error $e_n=f_n-f$ es no negativo por orden al límite y decrece a cero. Para $\varepsilon>0$, los conjuntos relativos $U_n=\{e_n<\varepsilon/2\}$ son abiertos crecientes y cubren el compacto. La familia de todas las bolas reales con cortes contenidos en algún $U_n$ es una cubierta abierta dada. Una subcubierta finita entrega un máximo de índices $N$; toda entrada está en $U_N$ y sigue estando en $U_n$ para $n\ge N$. El error es menor que $\varepsilon$. El vacío se trata vacuamente.

**Retorno visual.** Véase [C28-F03](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.12. Sin compacidad

[]{#MA-EX-ANM-01-028-012}

[]{#MA-SOL-ANM-01-028-012}

Las filas son continuas, decrecen por columnas y tienden puntualmente a cero continuo. El dominio abierto no es compacto. Para cada índice positivo la envolvente de $x^n$ es uno, aunque no se alcanza. Así no hay convergencia uniforme. Las cubiertas crecientes de error pequeño no tienen un miembro que cubra toda la pieza.

## 28.13. Sin continuidad de las filas

[]{#MA-EX-ANM-01-028-013}

[]{#MA-SOL-ANM-01-028-013}

Los soportes decrecen. En cero el valor es siempre cero; para cada entrada positiva la cola queda fuera del soporte. El límite es cero continuo. Cada fila toma el valor uno en $x_n=1/[2(n+1)]$, por lo que su envolvente es uno. Las filas tienen discontinuidad en el origen y en el otro borde interior cuando éste existe. Falta continuidad de las filas, aun con compacidad y monotonía.

## 28.14. Sin monotonía

[]{#MA-EX-ANM-01-028-014}

[]{#MA-SOL-ANM-01-028-014}

Las tiendas con $k=n+3$ son continuas, su soporte es $[1/k,3/k]$, y cada entrada positiva queda fuera de la cola; en cero siempre valen cero. El límite cero es continuo y el dominio compacto. Su máximo uno, alcanzado en $2/k$, refuta uniformidad. Si fueran decrecientes por columnas, Dini la garantizaría; tampoco son crecientes, pues una columna creciente no negativa que termina en cero sería siempre cero. Falta monotonía de la familia.

## 28.15. Pegar uniformidad local

[]{#MA-EX-ANM-01-028-015}

[]{#MA-SOL-ANM-01-028-015}

Compacidad reduce la cubierta a una subfamilia finita. Para una tolerancia fija, cada una de esas piezas entrega un corte uniforme. Tomamos el máximo finito de los cortes. Toda entrada pertenece a una pieza escogida y cumple el error posterior común. Si el compacto es vacío, cualquier corte sirve. La prueba necesita vecindades fijas con uniformidad, no sólo continuidad puntual de filas.

## 28.16. Existencia antes de integrar

[]{#MA-EX-ANM-01-028-016}

[]{#MA-SOL-ANM-01-028-016}

[]{#MA-SEC-ANM-01-028-004}

La uniformidad con tolerancia uno y una fila acotada acotan el límite. Si $|f-f_n|\le\delta$, extremos locales y suma de anchuras dan $G(f,P)\le G(f_n,P)+2\delta\ell$. Para $\varepsilon>0$ escogemos una fila con error menor que $\varepsilon/[8(\ell+1)]$ y una partición de esa fila con brecha menor que $\varepsilon/2$. La brecha de $f$ es menor que $3\varepsilon/4$. C23 acredita su integrabilidad. Para longitud cero la integral es cero por convención.

## 28.17. Error del valor integral

[]{#MA-EX-ANM-01-028-017}

[]{#MA-SOL-ANM-01-028-017}

La integrabilidad de ambos términos acredita la diferencia y su absoluto. Linealidad, triangular integral y orden dan $|I_n-I|\le\int|f_n-f|\le\ell E_n$. El supremo es real en la cola y no necesita alcanzarse. Como $E_n\to0$, también lo hace este error.

## 28.18. La cota se alcanza

[]{#MA-EX-ANM-01-028-018}

[]{#MA-SOL-ANM-01-028-018}

C23/C24 dan $I_n=1/3+1/(n+1)$ y $I=1/3$. La envolvente es $E_n=1/(n+1)$ y la longitud es uno. El error integral es exactamente $E_n$, mostrando optimalidad de la cota general para perturbaciones constantes positivas.

## 28.19. Destinos existentes pero distintos

[]{#MA-EX-ANM-01-028-019}

[]{#MA-SOL-ANM-01-028-019}

La tienda de altura uno y base de anchura $2/k$ tiene área $1/k$, con $k=n+3$. Multiplicarla por $k$ deja límite puntual cero y hace integral uno en cada etapa. La integral del destino es cero. Ambas existen y el límite de los valores integrales es uno, distinto de cero. No hay uniformidad: la altura de las filas normalizadas es $k$.

**Retorno visual.** Véase [C28-F04](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.20. Un destino no integrable

[]{#MA-EX-ANM-01-028-020}

[]{#MA-SOL-ANM-01-028-020}

Cada indicador de un conjunto finito de racionales integra cero. La sucesión que añade racionales de una enumeración tiende puntualmente a Dirichlet: uno en racionales y cero en irracionales. Cada pieza de longitud positiva tiene oscilación uno, de modo que ninguna partición da brecha menor que la longitud total. El destino no es integrable; la integral final está indefinida. Esto difiere de dos integrales existentes con valores distintos.

## 28.21. Todas las acumulaciones

[]{#MA-EX-ANM-01-028-021}

[]{#MA-SOL-ANM-01-028-021}

[]{#MA-SEC-ANM-01-028-005}

Restricción e integración orientada permiten cada acumulación. En el segmento entre $c$ y $x$, el error está bajo $|x-c|E_n\le\ell E_n$. Para $x=c$ vale cero y para $x<c$ se invierte el signo antes de aplicar orden. La cota global tendente a cero prueba uniformidad para todos los destinos $x$.

## 28.22. Peso integrable

[]{#MA-EX-ANM-01-028-022}

[]{#MA-SOL-ANM-01-028-022}

C23 acredita productos, diferencias y absolutos. La desigualdad puntual $|w(f_n-f)|\le E_n|w|$ se integra por orden, dando error a lo sumo $E_n\int|w|$. La integral de $|w|$ es finita en el marco cerrado; su producto por $E_n$ tiende a cero. Si $|w|\le M$, se obtiene la cota menos fina $M\ell E_n$.

## 28.23. Mover los extremos

[]{#MA-EX-ANM-01-028-023}

[]{#MA-SOL-ANM-01-028-023}

Insertamos la integral de $f$ con extremos $u_n,v_n$. El cambio de integranda cuesta a lo sumo $|v_n-u_n|E_n\le\ell E_n$. La aditividad orientada expresa los cambios de extremos como dos integrales de $f$; si $|f|\le B$, cuestan a lo sumo $B|u_n-u|$ y $B|v_n-v|$. Triangular suma los tres términos y todos tienden a cero. Inversiones e igualdad de extremos están cubiertas por orientación.

## 28.24. El marco que crece

[]{#MA-EX-ANM-01-028-024}

[]{#MA-SOL-ANM-01-028-024}

El error uniforme es $1/(n+1)$ y la longitud de la etapa es $n+1$. Su producto es uno, que es exactamente la integral. No hay un marco de longitud fija ni extremos con destinos finitos dentro de él. Cada integral es propia y finita; el ejemplo no necesita integrales impropias.

**Retorno visual.** Véase [C28-F05](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.25. Continuidad de la acumulada y derivada

[]{#MA-EX-ANM-01-028-025}

[]{#MA-SOL-ANM-01-028-025}

Ambos casos dan acumulaciones existentes, continuas y convergentes uniformemente por R5/C24. Si las integrandas son continuas, R1 hace continuo al destino y C24 identifica la derivada de su acumulada con él en todo punto interior. Para una integranda sólo integrable, esa identificación exige continuidad en el punto: un valor aislado puede cambiar la integranda sin cambiar la acumulada, y un salto puede impedir derivabilidad.

## 28.26. La ancla y todos los valores

[]{#MA-EX-ANM-01-028-026}

[]{#MA-SOL-ANM-01-028-026}

[]{#MA-SEC-ANM-01-028-006}

Cauchy del anclaje controla $|f_n(c)-f_m(c)|<\varepsilon/2$. Cauchy uniforme de derivadas entrega una cola con diferencia menor que $\varepsilon/[2(\ell+1)]$. C19 aplicado a $f_n-f_m$ entre $c$ y cualquier entrada da error a lo sumo el de anclaje más la cota de derivadas por $|x-c|\le\ell$. El máximo de ambos cortes sirve para todos los pares y entradas; C27 construye el límite uniforme.

## 28.27. El error de incrementos

[]{#MA-EX-ANM-01-028-027}

[]{#MA-SOL-ANM-01-028-027}

Para índices en la cola, la diferencia de derivadas $g_m-g_n$ está bajo $E_m+E_n$. C19 da la misma constante multiplicando $|y-x|$ para los incrementos de $f_m-f_n$. Fijamos $n,x,y$ y pasamos $m$ al límite. Los valores de $f_m$ convergen, $E_m\to0$, y orden conserva la desigualdad débil. Así se obtiene la cota pedida antes de derivar el destino.

## 28.28. Tres errores de cocientes

[]{#MA-EX-ANM-01-028-028}

[]{#MA-SOL-ANM-01-028-028}

En un centro interior fijo, escogemos una fila con $E_n<\varepsilon/3$. Dividir la cota de incrementos por la distancia no nula da error entre cocientes a lo sumo $E_n$. Derivabilidad de la fila fija da un radio para acercar su cociente a $g_n(x_0)$ con error menor que $\varepsilon/3$. La diferencia entre $g_n(x_0)$ y $g(x_0)$ es a lo sumo $E_n$. Triangular deja error menor que $\varepsilon$. Se restringe además el radio para permanecer dentro del segmento.

## 28.29. Certificado de valores desde derivadas

[]{#MA-EX-ANM-01-028-029}

[]{#MA-SOL-ANM-01-028-029}

En la cota de incrementos tomamos una entrada igual a $c$. La diferencia restante del error en $c$ es $f(c)-f_n(c)=\lambda-f_n(c)$. Triangular da $|f_n(x)-f(x)|\le |f_n(c)-\lambda|+|x-c|E_n$. Para una cota uniforme se reemplaza la distancia por $\ell$. Ambos términos tienden a cero; el segundo controla variaciones y el primero la constante aditiva.

## 28.30. Derivadas sin continuidad

[]{#MA-EX-ANM-01-028-030}

[]{#MA-SOL-ANM-01-028-030}

C19 sólo exige continuidad de $f_n-f_m$ en cada segmento y derivabilidad en su interior; no exige continuidad de la derivada. Las cotas de diferencias de derivadas permiten estimar incrementos. La identificación final usa derivabilidad de una fila y el presupuesto de incrementos, sin integrar $g$ ni aplicar el teorema fundamental a una función posiblemente discontinua. Si se añaden derivadas continuas, R1 sí conserva esa continuidad como conclusión adicional.

## 28.31. Una esquina como límite uniforme

[]{#MA-EX-ANM-01-028-031}

[]{#MA-SOL-ANM-01-028-031}

[]{#MA-SEC-ANM-01-028-007}

La raíz es al menos $|x|$. El cuadrado de $|x|+1/k$ es al menos $x^2+k^{-2}$, con $k=n+1$, y ambos lados son no negativos. Así el error está entre cero y $1/k$, con igualdad en cero. Cada fila deriva a $x/\sqrt{x^2+k^{-2}}$. El destino tiene cocientes laterales menos uno y uno en cero, por lo que no es derivable allí. Uniformidad de valores no conserva derivabilidad.

## 28.32. Los dos destinos de derivadas existen

[]{#MA-EX-ANM-01-028-032}

[]{#MA-SOL-ANM-01-028-032}

La envolvente de valores es $1/[2\sqrt{n+1}]$, de modo que el destino es cero uniforme. La regla de cociente da $h_n^{\prime}=(1-kx^2)/(1+kx^2)^2$. En cero vale uno; para cada entrada no nula tiende a cero por división por $k^2x^4$. Su límite puntual es la indicadora de cero. La derivada del destino es cero en toda la recta, así los valores discrepan en cero. Las derivadas no convergen uniformemente, pues son continuas y su destino no lo es.

**Retorno visual.** Véase [C28-F06](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.33. Sin anclaje

[]{#MA-EX-ANM-01-028-033}

[]{#MA-SOL-ANM-01-028-033}

Las constantes $f_n=n$ tienen derivadas cero y valores que divergen en cada entrada. Las constantes $f_n=(-1)^n$ también tienen derivadas cero y valores alternantes sin límite. Ninguna cumple convergencia en un anclaje. La derivada no detecta la constante aditiva, que R6 debe fijar por otro dato.

## 28.34. Sólo uniformidad en segmentos

[]{#MA-EX-ANM-01-028-034}

[]{#MA-SOL-ANM-01-028-034}

Las derivadas constantes $1/(n+1)$ convergen uniformemente a cero y el anclaje es siempre cero. En $[-M,M]$ el error de valores tiene envolvente $M/(n+1)$, tendente a cero. En toda la recta cada etapa tiene errores no acotados y en la entrada $n+1$ vale uno. No hay uniformidad global. La cota de R6 contiene la distancia al anclaje, que está acotada sólo en un marco finito.

## 28.35. Una ancla por componente

[]{#MA-EX-ANM-01-028-035}

[]{#MA-SOL-ANM-01-028-035}

Tomamos $f_n=0$ en la primera pieza y $f_n=n$ en la segunda. Cada restricción es constante y continua, con derivada interior cero. Las derivadas convergen uniformemente a cero en los interiores y $f_n(0)=0$. En la segunda pieza los valores divergen. El segmento entre una entrada de cada pieza atraviesa el hueco y no pertenece al dominio; C19 no puede unirlas.

## 28.36. El paquete polinómico

[]{#MA-EX-ANM-01-028-036}

[]{#MA-SOL-ANM-01-028-036}

[]{#MA-SEC-ANM-01-028-008}

La diferencia de valores es $-2^{-n}x$, así su envolvente es $2^{-n}$, alcanzada en los extremos. Las derivadas difieren por la constante $-2^{-n}$ y tienen la misma envolvente. El anclaje en cero es exacto. R6 acredita el paso de derivadas; la norma de dos capas del error es $2^{1-n}$.

## 28.37. El error de acumulación

[]{#MA-EX-ANM-01-028-037}

[]{#MA-SOL-ANM-01-028-037}

C24 y las reglas polinómicas dan $A_n=x^3/3+(1-2^{-n})x^2/2$ y $A=x^3/3+x^2/2$. Su diferencia es $-2^{-n}x^2/2$, cuya envolvente es $2^{-n}/2$, alcanzada en los extremos. En el intervalo simétrico completo, el error integral de las integrandas es cero por imparidad de la perturbación; eso no vuelve cero el error de cada acumulada.

**Retorno visual.** Véase [C28-F07](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.38. Frontera estricta dyádica

[]{#MA-EX-ANM-01-028-038}

[]{#MA-SOL-ANM-01-028-038}

El error de derivadas es $2^{-n}$. En $n=3$ es exactamente $1/8$, por lo que no cumple la desigualdad estricta. En $n=4$ es $1/16<1/8$ y toda etapa posterior disminuye. Los índices menores tampoco sirven. El corte mínimo es cuatro.

**Retorno visual.** Véase [C28-F08](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.39. Norma de dos capas

[]{#MA-EX-ANM-01-028-039}

[]{#MA-SOL-ANM-01-028-039}

Continuidad en el compacto acota ambas capas, por lo que los dos supremos existen. Positividad es suma de positivos; norma cero obliga la capa de valores cero y por tanto la función cero. Homogeneidad sigue de la linealidad de derivadas y homogeneidad de ambas normas supremas. Triangular se aplica a valores y derivadas por separado y se suma. Las extensiones continuas de derivadas son únicas y se suman y escalan junto con ellas.

## 28.40. Inducción finita de órdenes

[]{#MA-EX-ANM-01-028-040}

[]{#MA-SOL-ANM-01-028-040}

La capa de orden $r$ converge uniformemente por hipótesis y es continua. Aplicamos R6 a la de orden $r-1$, usando su valor convergente en el anclaje; obtenemos uniformidad e identificación de su derivada con la capa superior. Repetimos con el orden $r-2$ y continuamos un número finito de veces hasta los valores. R1 conserva continuidad de cada destino; en los bordes se usan extensiones y derivadas de un lado. No se intercambia una suma infinita ni se invoca Taylor.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html)
