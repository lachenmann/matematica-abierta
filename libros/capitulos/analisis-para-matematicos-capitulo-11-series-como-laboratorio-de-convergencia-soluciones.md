---
content-id: MA-BCH-0248
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-011-SOLUCIONES
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
title: Soluciones — Capítulo 11
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C11_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html)

## 11.1. Aportes y totales

[]{#MA-EX-ANM-01-011-001}

[]{#MA-SOL-ANM-01-011-001}

[]{#MA-SEC-ANM-01-011-001}

Los términos son $1,1/2,1/4,1/8$ y los totales $1,3/2,7/4,15/8$. $a$ y $s$ son sucesiones reales distintas; $s_n$ acumula $n+1$ valores de $a$.

Después del argumento, la [figura 11.1](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f01) permite contrastar el mecanismo con el ejemplo del capítulo.

Calculemos acumulando un aporte cada vez: $s_0=1$, $s_1=1+1/2=3/2$, $s_2=3/2+1/4=7/4$ y $s_3=7/4+1/8=15/8$. La fórmula de los aportes indica lo que se añade; la de los totales indica lo que ya se ha reunido. Así, aunque $a_3=1/8$ sea pequeño, $s_3=15/8$ no lo es. La convergencia de la serie pregunta por el destino de los totales, no por el de los aportes.

## 11.2. Recuperar una serie

[]{#MA-EX-ANM-01-011-002}

[]{#MA-SOL-ANM-01-011-002}

$a_0=s_0=1/2$. Para $n\ge1$, $a_n=s_n-s_{n-1}=(n+1)/(n+2)-n/(n+1)=1/((n+1)(n+2))$. La recursión verifica los totales, y su recuperación demuestra unicidad. Como $s_n=1-1/(n+2)\to1$, la serie tiene suma uno. La misma fórmula también da el término inicial si se evalúa en cero.

Al restar los dos cocientes, el numerador común es $(n+1)^2-n(n+2)=1$. Eso justifica la fórmula, en vez de limitarse a anunciarla. Para comprobar existencia, sumamos los términos recuperados: los recíprocos consecutivos se cancelan y dejan $1-1/(n+2)$, exactamente el total prescrito. Para comprobar unicidad, cualquier sucesión que produzca esos mismos totales debe tener el mismo primer aporte y las mismas diferencias posteriores. El límite de los totales es uno, aunque cada aporte tienda a cero.

## 11.3. Misma suma, distinto proceso

[]{#MA-EX-ANM-01-011-003}

[]{#MA-SOL-ANM-01-011-003}

Tomemos $a=(1,0,0,\ldots)$ y $b=(0,1,0,\ldots)$. Sus totales son $s_n=1$ en todo índice y $t_0=0$, $t_n=1$ para $n\ge1$. Ambas sumas valen uno, pero $a_0\ne b_0$ y $s_0\ne t_0$. Igualdad numérica de sumas no implica igualdad de funciones.

Después del argumento, la [figura 11.1](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f01) permite contrastar el mecanismo con el ejemplo del capítulo.

El soporte de cada sucesión es finito: sólo tiene un índice con aporte distinto de cero. Por eso, tras incorporar ese aporte, los totales permanecen iguales a uno y convergen a uno. Sin embargo, basta comparar el índice cero para mostrar que tanto los aportes como sus procesos son diferentes. La suma conserva un número final, pero no indica en qué momento se incorporó cada aporte. Conocer todos los totales contiene más información que conocer únicamente su límite.

## 11.4. Una transformación reversible

[]{#MA-EX-ANM-01-011-004}

[]{#MA-SOL-ANM-01-011-004}

Definamos $a_0=s_0$ y $a_{n+1}=s_{n+1}-s_n$. Si $u=\operatorname{PS}(a)$, entonces $u_0=s_0$. Suponiendo $u_n=s_n$, la recursión da $u_{n+1}=s_n+s_{n+1}-s_n=s_{n+1}$. Inducción prueba $u=s$. Si otro $b$ produce $s$, la recuperación de §11.1 fuerza $b_0=a_0$ y $b_{n+1}=a_{n+1}$. Es una correspondencia entre sucesiones, sin exigir convergencia.

Después del argumento, la [figura 11.1](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f01) permite contrastar el mecanismo con el ejemplo del capítulo.

La prueba tiene dos obligaciones. Para existencia, construimos $a$ y demostramos por inducción que su proceso de sumación coincide con $s$ en cada índice. Para unicidad, partimos de cualquier otra candidata y usamos las identidades $a_0=s_0$ y $a_{n+1}=s_{n+1}-s_n$, que son forzadas por los totales. No se necesita que $s$ tenga límite: la transformación entre aportes y totales es reversible incluso cuando la serie diverge.

## 11.5. Totales acotados y término nulo

[]{#MA-EX-ANM-01-011-005}

[]{#MA-SOL-ANM-01-011-005}

Prescribamos bloques: para cada $m\ge1$, $m$ términos $1/m$ seguidos de $m$ términos $-1/m$. El bloque ocupa $m(m-1)\le n\le m(m+1)-1$; sus extremos consecutivos cubren todos los naturales. Los totales van de cero a uno y regresan a cero, así que están en $[0,1]$. Dada $\varepsilon>0$, tomar $M$ con $1/M<\varepsilon$ hace $|a_n|\le1/M<\varepsilon$ desde el comienzo del bloque $M$. Los totales de mitad y final de cada bloque son uno y cero en índices arbitrariamente grandes; falla Cauchy con tolerancia $1/2$.

Después del argumento, la [figura 11.5](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f05) permite contrastar el mecanismo con el ejemplo del capítulo.

El primer bloque tiene dos aportes; los primeros $m-1$ bloques contienen $2(1+\cdots+(m-1))=m(m-1)$ aportes, lo que explica la posición inicial del bloque $m$. Su mitad positiva eleva el total a uno y su mitad negativa lo devuelve a cero. Para negar Cauchy, recibido un corte escogemos un bloque posterior completo y comparamos sus totales de mitad y final. Su separación es uno. Los saltos individuales se hacen pequeños, pero el número creciente de aportes permite mantener una excursión de tamaño fijo.

## 11.6. Identidad de bloques

[]{#MA-EX-ANM-01-011-006}

[]{#MA-SOL-ANM-01-011-006}

[]{#MA-SEC-ANM-01-011-002}

Fijemos $q$. Para $p=q+1$, la recursión da la identidad. Si vale para $p$, entonces $s_{p+1}-s_q=(s_p-s_q)+a_{p+1}=\sum_{j=q+1}^{p+1}a_j$. La inducción sobre $p-q\ge1$ cubre todos los extremos; no interviene una suma infinita.

El índice $q$ permanece fijo durante la inducción y la variable es la longitud $p-q$. La base tiene un solo aporte nuevo: $s_{q+1}-s_q=a_{q+1}$. En el paso inductivo, incorporar $a_{p+1}$ prolonga el bloque y el total exactamente de la misma manera. Así la identidad vale para cada $q$ y todos los extremos posteriores. La suma comienza en $q+1$ porque $a_q$ ya estaba incluido en el total que se resta.

## 11.7. La longitud no puede elegir el corte

[]{#MA-EX-ANM-01-011-007}

[]{#MA-SOL-ANM-01-011-007}

Para un natural fijo $r\ge1$, $0\le\sum_{j=q+1}^{q+r}1/(j+1)\le r/(q+2)\to0$. El corte de esta estimación depende de $r$. Cauchy exige uno solo para todas las longitudes. Tomando $q=m-1$, $p=2m-1$, se obtiene un bloque al menos $1/2$ después de cualquier corte, así que no converge.

Después del argumento, la [figura 11.2](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f02) permite contrastar el mecanismo con el ejemplo del capítulo.

Para una longitud fijada $r$ y una tolerancia positiva, basta escoger $N$ con $N+2>r/\varepsilon$. Entonces todo bloque de longitud $r$ iniciado después de $N$ tiene suma menor que $\varepsilon$. Pero la negación de Cauchy permite escoger la longitud después del corte: con $m=N+1$, el bloque de denominadores $m+1,\ldots,2m$ tiene $m$ aportes de tamaño al menos $1/(2m)$. Su suma no baja de $1/2$. La dependencia del corte respecto de la longitud es precisamente lo que impide el criterio completo.

## 11.8. Términos que no desaparecen

[]{#MA-EX-ANM-01-011-008}

[]{#MA-SOL-ANM-01-011-008}

En la primera, $|a_n|=1$ en cada índice; en la segunda, $b_n\ge1/2$. Ninguna sucesión de términos tiende a cero, y la condición necesaria de §11.2 descarta ambas convergencias. No hace falta calcular sus totales para aplicar esa condición.

Si una serie convergiera, la diferencia de dos totales consecutivos tendría que tender a cero, por lo que sus aportes desaparecerían. Aquí la primera sucesión mantiene magnitud uno. La segunda mantiene una cota inferior $1/2$, así que ninguna cola puede satisfacer, por ejemplo, la tolerancia $1/4$ respecto de cero. Hemos hecho fallar una condición necesaria. Eso basta para descartar ambas series, aunque sus comportamientos de totales sean distintos.

## 11.9. Acumulación en potencias de dos

[]{#MA-EX-ANM-01-011-009}

[]{#MA-SOL-ANM-01-011-009}

En la notación de denominadores, $s_{2^m-1}=\sum_{j=1}^{2^m}1/j$. Para cada $i=1,\ldots,m$, el bloque $j=2^{i-1}+1,\ldots,2^i$ tiene $2^{i-1}$ términos, cada uno al menos $1/2^i$, de modo que aporta al menos $1/2$. Añadiendo el término $j=1$ resulta la cota, también válida para $m=0$. Es una partición finita; prueba que los totales carecen de barrera superior.

Después del argumento, la [figura 11.2](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f02) permite contrastar el mecanismo con el ejemplo del capítulo.

Los bloques duplican sus extremos: después del aporte inicial uno, reunimos denominadores $2$, luego $3,4$, después $5,\ldots,8$, y así sucesivamente. Cada grupo aporta al menos medio, porque duplica su cantidad de sumandos mientras divide por dos la cota inferior de cada uno. Para cualquier barrera $B$, arquimedianidad permite escoger $m$ con $1+m/2>B$. El total correspondiente la supera. No estamos asignando un valor a una suma infinita: todos los bloques y totales usados son finitos.

## 11.10. Reparar una falsa prueba

[]{#MA-EX-ANM-01-011-010}

[]{#MA-SOL-ANM-01-011-010}

Una suma de muchos términos puede exceder $\varepsilon$, y los signos tampoco autorizan ignorar magnitudes. Si la longitud está acotada por $M$, basta hacer $|a_j|<\varepsilon/M$ en la cola. La triangular finita da magnitud del bloque menor que $r\varepsilon/M\le\varepsilon$ para $1\le r\le M$; el bloque vacío vale cero. Esto controla sólo bloques de esas longitudes, no el criterio completo sin otra hipótesis.

Después del argumento, la [figura 11.2](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f02) permite contrastar el mecanismo con el ejemplo del capítulo.

La reparación debe pedir control del valor absoluto, porque «menor que $\varepsilon$» como desigualdad firmada no controla aportes negativos grandes. Si un bloque tiene $r\le M$ términos, hacemos cada magnitud menor que $\varepsilon/M$. La triangular da una suma de magnitudes estrictamente menor que $r\varepsilon/M\le\varepsilon$. El factor $M$ reparte el presupuesto entre el máximo número de errores permitidos. Si las longitudes no están acotadas, esta elección no controla todos los bloques.

## 11.11. Telescopaje y corte

[]{#MA-EX-ANM-01-011-011}

[]{#MA-SOL-ANM-01-011-011}

[]{#MA-SEC-ANM-01-011-003}

La descomposición $a_n=1/(n+1)-1/(n+2)$ da $s_n=1-1/(n+2)$. La suma es uno y el resto $1/(n+2)$. Error estrictamente menor que $1/100$ equivale a $n+2>100$; basta $n=99$ y todos los cortes posteriores. $n=98$ sólo da igualdad con la tolerancia.

Después del argumento, la [figura 11.3](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f03) permite contrastar el mecanismo con el ejemplo del capítulo.

La identidad telescópica se obtiene restando recíprocos: $1/(n+1)-1/(n+2)=1/((n+1)(n+2))$. Después de sumar hasta $n$, sobreviven el primer recíproco uno y el último $-1/(n+2)$. Para el error estricto, $n+2>100$ equivale a $n>98$. El primer natural posible es 99 y el total usa cien aportes, desde el índice cero hasta el 99. Con 99 aportes, el índice final sería 98 y el error sería exactamente $1/100$.

## 11.12. Razón negativa

[]{#MA-EX-ANM-01-011-012}

[]{#MA-SOL-ANM-01-011-012}

Por §11.3, $S=2/3$ y $R_n=(2/3)(-1/2)^{n+1}$. Su magnitud es $1/(3\cdot2^n)$. Para $n=6$ vale $1/192<1/100$, y para $n=5$ vale $1/96>1/100$; por ello seis es el primer corte suficiente en la cota exacta. Hasta él se suman siete términos.

Después del argumento, la [figura 11.3](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f03) permite contrastar el mecanismo con el ejemplo del capítulo.

La fórmula finita da $s_n=(1-(-1/2)^{n+1})/(1+1/2)$. Al tomar el límite obtenemos $S=2/3$ y, al restar, el resto firmado. Su magnitud vale $(2/3)2^{-(n+1)}=1/(3\cdot2^n)$. Comparar los índices cinco y seis decide el primer corte porque esta magnitud disminuye al aumentar el índice. El signo del resto cambia con la paridad; ese cambio no modifica la certificación del error absoluto.

## 11.13. Todos los casos geométricos

[]{#MA-EX-ANM-01-011-013}

[]{#MA-SOL-ANM-01-011-013}

Si $|r|<1$, la identidad finita y $r^{n+1}\to0$ dan suma $1/(1-r)$. En cero se usa $r^0=1$: suma uno. Para $|r|\ge1$, $|r^n|\ge1$, por lo que falla el término nulo. En particular $r=1$ tiene totales $n+1$, y $r=-1$ totales uno/cero; ambas divergen.

Después del argumento, la [figura 11.3](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f03) permite contrastar el mecanismo con el ejemplo del capítulo.

Dentro de $(-1,1)$ las potencias tienden a cero y la identidad finita determina el límite de los totales. La razón cero se comprueba directamente: el aporte de exponente cero es uno y todos los posteriores son cero. Fuera del intervalo, incluida su frontera, las magnitudes de los aportes son al menos uno. Esto descarta convergencia antes de intentar dividir o calcular un destino. En particular, la fórmula con denominador $1-r$ no puede usarse para $r=1$.

## 11.14. La diferencia puede sumar sin magnitudes

[]{#MA-EX-ANM-01-011-014}

[]{#MA-SOL-ANM-01-011-014}

$c_n\to0$, así que por telescopaje $s_n=1-c_{n+1}\to1$. Además $a_n=(-1)^n[1/(n+1)+1/(n+2)]$, luego $|a_n|\ge1/(n+1)$. Si sus magnitudes tuvieran totales acotados, los armónicos quedarían acotados por comparación finita, contradiciendo 11.9. La serie original converge y la de magnitudes diverge. La prueba sólo usa telescopaje y la acumulación armónica ya establecida; no necesita el criterio alternado ni el de convergencia absoluta.

Los signos de $c_n$ y $c_{n+1}$ son opuestos; restarlos suma sus magnitudes y mantiene el signo de $c_n$. Por eso $|a_n|=1/(n+1)+1/(n+2)$. La cancelación telescópica controla los totales originales mediante $c_{n+1}\to0$, pero al tomar magnitudes esa cancelación desaparece. Las sumas de magnitudes dominan las armónicas y no pueden permanecer acotadas. Este ejemplo permite separar los dos tipos de convergencia sin utilizar un criterio que se presenta más adelante.

## 11.15. Telescopar no crea destino

[]{#MA-EX-ANM-01-011-015}

[]{#MA-SOL-ANM-01-011-015}

Siempre $s_n=c_0-c_{n+1}$. Si $c_n\to C$, la serie tiene suma $c_0-C$. Si $s_n\to S$, entonces $c_{n+1}=c_0-s_n\to c_0-S$; para $n\ge1$ se traslada el corte en una unidad, y el término $c_0$ no afecta el límite. Así $c_n\to c_0-S$. El telescopaje proporciona una equivalencia, no convergencia automática.

Para la vuelta, conocer $s_n\to S$ da el límite de $c_{n+1}$ por la identidad $c_{n+1}=c_0-s_n$. Si ese control funciona desde $n\ge N$, el control de $c_j$ funciona desde $j\ge N+1$. El valor inicial no afecta la convergencia porque queda fuera de una cola suficientemente tardía. El telescopaje reduce el problema a otra sucesión; si ésta oscila o carece de destino, la cancelación algebraica por sí sola no lo remedia.

## 11.16. Dónde se usa la barrera

[]{#MA-EX-ANM-01-011-016}

[]{#MA-SOL-ANM-01-011-016}

[]{#MA-SEC-ANM-01-011-004}

Sea $S=\sup\{s_n\}$, real por no vacuidad y cota. Dada $\varepsilon>0$, existe $N$ con $s_N>S-\varepsilon$ por optimalidad del supremo. La no negatividad hace $s_N\le s_n\le S$ para todo $n\ge N$, así que $|s_n-S|<\varepsilon$. Completitud construye $S$ y el signo mantiene cerca toda la cola.

El conjunto de totales contiene $s_0$ y tiene una cota superior común, así que la completitud permite tomar su supremo real. La optimalidad asegura un total por encima de $S-\varepsilon$: de lo contrario, esa cantidad menor que $S$ sería otra cota superior. Después, la monotonía conserva el acercamiento y la cota $S$ impide sobrepasar la barrera. Ambas hipótesis cumplen funciones diferentes: una construye el destino y la otra retiene la cola dentro de la franja de precisión.

## 11.17. Comparar y estimar

[]{#MA-EX-ANM-01-011-017}

[]{#MA-SOL-ANM-01-011-017}

Para todo $n$, $0\le1/(n+2)^2\le1/((n+1)(n+2))$. Sus totales están entre cero y los telescópicos, por tanto entre cero y uno. La barrera positiva prueba existencia de $S$. Para $p>n$, comparar sólo la cola da $0\le s_p-s_n\le1/(n+2)-1/(p+2)$. Al tomar $p\to\infty$, $0\le S-s_n\le1/(n+2)$.

La comparación término a término vale porque $(n+2)^2\ge(n+1)(n+2)>0$, y al invertir denominadores positivos se invierte el orden. La serie telescópica ofrece una barrera uno para los totales, lo que demuestra primero la existencia de la suma buscada. Sólo después podemos dejar el extremo posterior $p$ tender a infinito en la comparación de bloques. Así obtenemos un resto certificado sin conocer una fórmula para $S$. La misma cota sirve para todos los cortes con $n+2>1/\varepsilon$.

## 11.18. Comparación eventual

[]{#MA-EX-ANM-01-011-018}

[]{#MA-SOL-ANM-01-011-018}

Coinciden desde uno y difieren en $a_0-b_0=99$. La geométrica de $b$ tiene suma dos, así que los totales de $a$ son los de $b$ más 99 y su suma es 101. La comparación eventual no da $S_a\le S_b$; conserva convergencia pero debe incorporar el prefijo.

Los prefijos iniciales difieren en cien menos uno, es decir, 99. Desde el segundo aporte las dos sucesiones son idénticas, por lo que cada total de $a$ es el correspondiente total geométrico de $b$ más esa constante. Al pasar al límite, la diferencia 99 se conserva: las sumas son 101 y dos. Comparar únicamente la cola no compara el total acumulado antes de ella. Una modificación finita conserva convergencia, pero puede cambiar la suma en una cantidad arbitraria.

## 11.19. Una barrera para series con signos

[]{#MA-EX-ANM-01-011-019}

[]{#MA-SOL-ANM-01-011-019}

El supremo puede existir, pero tras encontrar un total cercano no sabemos que los posteriores sean mayores. Para $a_n=(-1)^n$, el supremo de los totales es uno y éstos alternan uno/cero; no se conserva cercanía al supremo. Falta la no negatividad de los incrementos.

Después del argumento, la [figura 11.1](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f01) permite contrastar el mecanismo con el ejemplo del capítulo.

Tener un supremo de los totales sólo dice que existe una menor cota superior. Para identificarlo con el límite hace falta que, después de aproximarse a él, los totales no retrocedan. La serie alternada de unos produce un total igual al supremo en cada índice par y un total cero en cada índice impar. Así ningún corte asegura cercanía permanente a uno. La no negatividad de los aportes es la hipótesis que proporcionaba monotonía en la prueba positiva.

## 11.20. Barrera sin fórmula de suma

[]{#MA-EX-ANM-01-011-020}

[]{#MA-SOL-ANM-01-011-020}

La comparación finita con $b_n=1/((n+1)(n+2))$ acota todos los totales por uno y prueba convergencia por §11.4. Comparando bloques y tomando el límite del extremo posterior resulta $0\le S-s_n\le1/(n+2)$. Se conserva uniformidad en la elección de $\theta$, pero no se afirma que las diferentes sucesiones tengan la misma suma.

Después del argumento, la [figura 11.1](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f01) permite contrastar el mecanismo con el ejemplo del capítulo.

Multiplicar el aporte telescópico positivo por una cantidad entre cero y uno lo mantiene entre cero y ese aporte original. Por eso todos los totales son crecientes y no superan uno. La comparación de bloques da una cota de resto independiente de las elecciones de $\theta_n$. No obstante, esas elecciones cambian la suma: si todas valen cero, la suma es cero; si todas valen uno, es uno. Una garantía uniforme de error no implica que los destinos coincidan.

## 11.21. Triangular finita

[]{#MA-EX-ANM-01-011-021}

[]{#MA-SOL-ANM-01-011-021}

[]{#MA-SEC-ANM-01-011-005}

Para longitud uno es igualdad. Si vale hasta $p$, la triangular da $|\sum_{j=q+1}^{p+1}a_j|\le|\sum_{j=q+1}^pa_j|+|a_{p+1}|\le\sum_{j=q+1}^{p+1}|a_j|$. Inducción sobre la longitud cubre todos los bloques finitos.

En el paso inductivo, distinguimos la suma ya controlada del aporte que se añade. La triangular para esos dos números da la primera desigualdad; la hipótesis inductiva da la segunda. El bloque inicial de un término satisface igualdad, así que la inducción empieza sin ninguna condición adicional. Como todas las operaciones son finitas, la conclusión se aplica incluso a aportes cuyas series divergen. La convergencia será una aplicación posterior del control, no una hipótesis de esta desigualdad.

## 11.22. Signos libres

[]{#MA-EX-ANM-01-011-022}

[]{#MA-SOL-ANM-01-011-022}

Las magnitudes son $2^{-n}$ y su serie geométrica tiene suma dos. Por §11.5, la original converge absolutamente. La cola de magnitudes posterior a $n$ tiene suma $2^{-n}$, por tanto $|S-s_n|\le2^{-n}$. La estimación es independiente de cómo cambian los signos.

Después del argumento, la [figura 11.4](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f04) permite contrastar el mecanismo con el ejemplo del capítulo.

Tomar magnitudes elimina exactamente los signos libres: $|\sigma_n2^{-n}|=2^{-n}$. Los totales de magnitudes tienen suma dos y el bloque posterior al índice $n$ tiene suma geométrica $2^{-n}$. El criterio absoluto prueba existencia de $S$ y domina su resto por esa cola. La cota no supone regularidad en los signos; permite incluso elegirlos de manera completamente irregular. Para asegurar precisión $\varepsilon$ basta hacer $2^{-n}<\varepsilon$.

## 11.23. Orden de las hipótesis

[]{#MA-EX-ANM-01-011-023}

[]{#MA-SOL-ANM-01-011-023}

Una cota de valores sólo da acotación. Para reparar, usar $|s_p-s_q|\le u_p-u_q$. Si $u$ converge, es Cauchy; para $p>q$ tardíos, su incremento no negativo es menor que la tolerancia. El mismo corte controla los bloques originales y C10 produce un límite real de $s$.

Después del argumento, la [figura 11.4](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f04) permite contrastar el mecanismo con el ejemplo del capítulo.

Una sucesión puede permanecer dentro de una barrera y oscilar indefinidamente: estar acotada no es converger. Lo que caracteriza Cauchy es la distancia entre dos totales tardíos, no la magnitud de cada total. La desigualdad correcta compara esa distancia con el incremento de los totales de magnitudes. Convergencia de estos últimos proporciona un corte que sirve para todos los pares. La completitud produce luego el límite original, evitando asumirlo al comienzo de la prueba.

## 11.24. Sumas y restos

[]{#MA-EX-ANM-01-011-024}

[]{#MA-SOL-ANM-01-011-024}

La triangular finita da $|s_p|\le u_p$; la desigualdad inversa de valor absoluto y C06 permiten pasar al límite, dando $|S|\le A$. Fijado $n$, para todos $p>n$ vale $|s_p-s_n|\le u_p-u_n$; al tomar el límite de $p$, el lado izquierdo tiende a $|S-s_n|$ y el derecho a $A-u_n$. El orden de límites da la cota solicitada.

La continuidad del valor absoluto puede justificarse sin un teorema adicional: $\bigl||s_p|-|S|\bigr|\le|s_p-S|\to0$. Para el resto, mantenemos el corte $n$ fijo y sólo dejamos variar $p$. Así $s_n$ y $u_n$ son constantes en ese paso al límite. La comparación finita conserva el orden en el límite y produce una cota no estricta. Como $A-u_n\to0$, esa cota permite certificar precisiones cada vez menores.

## 11.25. Localizar igualdad

[]{#MA-EX-ANM-01-011-025}

[]{#MA-SOL-ANM-01-011-025}

Si todos son no negativos, $S=A$; si todos son no positivos, $S=-A$, por identidades finitas y límites. Para la recíproca definamos $p_n=(|a_n|+a_n)/2\ge0$ y $m_n=(|a_n|-a_n)/2\ge0$. Sus totales convergen a $P=(A+S)/2$ y $M=(A-S)/2$ por álgebra de límites; $P,M\ge0$. La igualdad $|S|=A$ fuerza $M=0$ si $S\ge0$, o $P=0$ si $S\le0$. Una serie no negativa de suma cero tiene cada término cero, pues cada término es menor o igual a un total posterior, que es a lo sumo cero. Así en el primer caso $m_n=0$ y $a_n\ge0$; en el segundo $p_n=0$ y $a_n\le0$. Si $A=0$, todos los términos son cero y ambas descripciones sirven.

Las sucesiones $p_n$ y $m_n$ separan los aportes positivos y las magnitudes de los negativos: $a_n=p_n-m_n$ y $|a_n|=p_n+m_n$. Si ambas partes acumuladas fueran positivas, la resta tendría magnitud estrictamente menor que su suma. La igualdad obliga a que una parte acumule cero. Como sus aportes son no negativos, ni uno solo puede ser positivo si la suma es cero. Por eso todos los aportes originales tienen un mismo signo débil, y los ceros son compatibles con cualquiera de las dos descripciones.

## 11.26. Lema alternado

[]{#MA-EX-ANM-01-011-026}

[]{#MA-SOL-ANM-01-011-026}

[]{#MA-SEC-ANM-01-011-006}

Para la cota inferior agrupar pares $c_0-c_1$, $c_2-c_3$, etc., dejando el último término positivo si sobra. Todos los sumandos son no negativos. Para la superior, escribir $c_0-(c_1-c_2)-(c_3-c_4)-\cdots$ y restar el último término si el índice final es impar. Las cantidades restadas son no negativas. Ambas escrituras provienen de la misma suma finita.

Después del argumento, la [figura 11.4](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f04) permite contrastar el mecanismo con el ejemplo del capítulo.

Las dos agrupaciones sirven a fines distintos. Agrupar desde el primer aporte muestra que el resultado no es negativo; dejar el primero fuera y agrupar desde el segundo muestra que no supera ese primer aporte. Hay que comprobar la paridad del número de sumandos para tratar el aporte que queda sin pareja. Si termina con signo positivo, se añade en la prueba inferior; si termina con signo negativo, se resta en la superior. Todas las diferencias emparejadas son no negativas por el decrecimiento.

## 11.27. Un corte alternado

[]{#MA-EX-ANM-01-011-027}

[]{#MA-SOL-ANM-01-011-027}

Las magnitudes decrecen y tienden a cero, así que el criterio probado en §11.6 aporta un real $S$. Su resto satisface $|S-s_n|\le1/(n+2)$. Tomar $n=99$ hace esta cota $1/101<1/100$ y controla todo corte posterior. No se calcula $S$ para certificar esa precisión.

Después del argumento, la [figura 11.4](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f04) permite contrastar el mecanismo con el ejemplo del capítulo.

El criterio de alternancia se aplica porque $b_n=1/(n+1)$ es no negativo, no creciente y tiende a cero. El resto se domina por la siguiente magnitud $b_{n+1}=1/(n+2)$. La elección 99 garantiza el requisito estricto mediante $1/101<1/100$. Este corte es suficiente según la cota del criterio; no se afirma que sea el primer índice cuyo error real cumpla la tolerancia. Esa afirmación exigiría información adicional sobre el error exacto, no sólo una cota superior.

## 11.28. El signo del resto

[]{#MA-EX-ANM-01-011-028}

[]{#MA-SOL-ANM-01-011-028}

El control finito $0\le(-1)^{n+1}(s_p-s_n)\le b_{n+1}$ pasa al límite con $n$ fijo. Para $n$ par, $0\le-(S-s_n)$, así que $S\le s_n$; para $n$ impar, $0\le S-s_n$, así que $s_n\le S$. Las desigualdades son débiles: puede haber igualdad si desaparece el resto.

Después del argumento, la [figura 11.4](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f04) permite contrastar el mecanismo con el ejemplo del capítulo.

La suma del bloque posterior comienza con el signo $(-1)^{n+1}$. Multiplicar por ese signo permite usar el lema con primer aporte positivo. Al pasar al límite obtenemos el resto firmado, y la paridad decide de qué lado de $S$ queda el total. Si las magnitudes posteriores son cero, el resto es cero y el total coincide con $S$. Por eso «por encima» y «por debajo» deben entenderse con desigualdades no estrictas.

## 11.29. Borrar el decrecimiento

[]{#MA-EX-ANM-01-011-029}

[]{#MA-SOL-ANM-01-011-029}

Tomemos $a_{2k}=2/(k+1)$ y $a_{2k+1}=-1/(k+1)$. Ambas paridades de magnitudes tienden a cero, así que $a_n\to0$ por un corte común. Cada pareja suma $1/(k+1)$, y los totales $s_{2m+1}$ son armónicos no acotados. Por tanto la serie diverge. Las magnitudes no decrecen: para $k\ge1$, $2/(k+2)>1/(k+1)$. La desigualdad de parejas del lema no puede aplicarse.

Después del argumento, la [figura 11.4](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f04) permite contrastar el mecanismo con el ejemplo del capítulo.

Cada pareja aporta $2/(k+1)-1/(k+1)=1/(k+1)$. La subsecuencia de totales al final de las parejas es entonces la armónica y no puede converger. En cambio, los aportes individuales sí tienden a cero: basta un corte común para las dos subsecuencias de magnitudes. Entre parejas, el paso de $1/(k+1)$ a $2/(k+2)$ aumenta para $k>0$, así que falla el decrecimiento global. Alternar signos y tener término nulo no bastan para aplicar el criterio alternado.

## 11.30. Alternancia eventual

[]{#MA-EX-ANM-01-011-030}

[]{#MA-SOL-ANM-01-011-030}

Aplique §11.6 a la cola reindexada, con un signo global $\eta$ que no altera las magnitudes de bloques. La serie de términos $(-1)^kb_k$ tiene suma $T$; la cola con el signo global tiene suma $\eta T$, y añadir el prefijo finito $P_m$ da $S=P_m+\eta T$. En el corte original $n\ge m$, la siguiente magnitud es $b_{n-m+1}$, por lo que $|S-s_n|\le b_{n-m+1}$. El resto tiene el signo de $\eta(-1)^{n-m+1}$ salvo cero. No se exige comportamiento alternado del prefijo.

La reindexación hace que el aporte de índice original $n$ corresponda a $k=n-m$. Tras incorporarlo, el siguiente aporte de la cola tiene magnitud $b_{n-m+1}$, lo que explica el desplazamiento del resto. El prefijo $P_m$ se suma tanto al total como al destino y se cancela al calcular su diferencia. El signo global $\eta$ cambia la orientación del encierro, pero no la cota de error absoluto. Para $m=0$ el prefijo es vacío y se recupera el caso inicial.

## 11.31. Extremos de grupos

[]{#MA-EX-ANM-01-011-031}

[]{#MA-SOL-ANM-01-011-031}

[]{#MA-SEC-ANM-01-011-007}

Para $k=0$, $t_0=g_0=s_{\phi(0)}$. Si vale para $k-1$, sumar el bloque desde $\phi(k-1)+1$ hasta $\phi(k)$ da $t_k=s_{\phi(k-1)}+[s_{\phi(k)}-s_{\phi(k-1)}]=s_{\phi(k)}$. Inducción prueba la identidad sin reordenar términos.

Después del argumento, la [figura 11.5](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f05) permite contrastar el mecanismo con el ejemplo del capítulo.

El primer grupo debe incorporar todos los aportes desde cero hasta $\phi(0)$. Cada grupo posterior comienza justo una posición después del extremo previo y termina en el nuevo extremo. Por eso sumar grupos consecutivos no duplica ni omite ningún aporte del prefijo. La identidad de bloques expresa exactamente ese hecho y hace funcionar el paso inductivo. Estamos cambiando la frecuencia con que observamos los totales; no estamos cambiando el orden original de los términos.

## 11.32. Una agrupación engañosa

[]{#MA-EX-ANM-01-011-032}

[]{#MA-SOL-ANM-01-011-032}

Con $\phi(k)=2k+1$, cada grupo es $1-1=0$, así que la serie agrupada tiene suma cero. La original tiene totales par uno e impar cero y no es Cauchy. La agrupación sólo conserva una extracción de sus totales y no suministra control de los índices pares omitidos.

Después del argumento, la [figura 11.5](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f05) permite contrastar el mecanismo con el ejemplo del capítulo.

Los extremos elegidos son los índices impares $1,3,5,\ldots$, donde los totales originales valen cero. La agrupación los observa y no registra los totales pares, iguales a uno. Por eso todos los grupos pueden sumar cero sin que el recorrido completo converja. El ejemplo no contradice que agrupar una serie convergente conserve su suma: la serie de partida no cumple esa hipótesis. Una subsucesión convergente no demuestra por sí sola convergencia de toda la sucesión.

## 11.33. Grupos de longitud acotada

[]{#MA-EX-ANM-01-011-033}

[]{#MA-SOL-ANM-01-011-033}

Escojamos $J$ con $|a_j|<\varepsilon/(2M)$ para $j\ge J$ y un corte $K\ge\max\{1,J\}$ de grupos con $|t_k-S|<\varepsilon/2$. Para $k\ge K$, todo índice del grupo es al menos $\phi(k-1)+1\ge k\ge J$. La diferencia de un total interior al extremo suma a lo sumo $M$ magnitudes, luego es menor que $\varepsilon/2$ o cero. Todo $n\ge\phi(K-1)+1$ pertenece a esos grupos, así que $|s_n-S|\le|s_n-t_k|+|t_k-S|<\varepsilon$.

Después del argumento, la [figura 11.5](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f05) permite contrastar el mecanismo con el ejemplo del capítulo.

Para cada índice original tardío existe un grupo que lo contiene, porque los extremos crecen y los grupos cubren los índices sin huecos. Su distancia al total del extremo se controla por a lo sumo $M$ aportes pequeños. La triangular reparte el error en esa separación interior y la distancia del extremo a $S$, con presupuestos de $\varepsilon/2$. El corte original se fija en el comienzo del grupo $K$: desde allí todos los índices están cubiertos por ambos controles. Los totales anteriores a ese corte no afectan la conclusión.

## 11.34. Longitud no necesaria

[]{#MA-EX-ANM-01-011-034}

[]{#MA-SOL-ANM-01-011-034}

La geométrica $a_n=2^{-n}$ converge a dos. Tomemos $\phi(k)=(k+1)^2-1$: el grupo inicial tiene un término y el grupo $k\ge1$ tiene longitud $2k+1$, no acotada. Por la dirección directa de §11.7, la agrupada conserva suma dos. La cota de longitud es suficiente para recuperar convergencia a partir de extremos y término nulo, no necesaria para toda agrupación de una serie ya convergente.

La longitud del grupo $k\ge1$ es $\phi(k)-\phi(k-1)=(k+1)^2-k^2=2k+1$, que crece sin cota. Aun así, sus totales son $s_{\phi(k)}$ y forman una subsecuencia de una sucesión ya convergente a dos. Una condición suficiente describe una vía para probar una conclusión bajo ciertas hipótesis; no afirma que la conclusión falle siempre que alguna de ellas falte. Aquí la convergencia completa está establecida antes de elegir la agrupación.

## 11.35. Excursiones que se reducen

[]{#MA-EX-ANM-01-011-035}

[]{#MA-SOL-ANM-01-011-035}

El bloque ocupa $m(m-1)\le n\le m(m+1)-1$. Sus totales empiezan en cero, suben a $h_m$ y vuelven a cero. Si $h_m\to0$, todo total de los bloques tardíos está entre cero y $h_m$, así que converge a cero por un corte en el comienzo de un bloque. Si la serie converge, los totales finales cero fuerzan suma cero por una extracción con índices crecientes; los totales de mitad son $h_m$ y deben tender también a cero. Por tanto la equivalencia y suma quedan establecidas. Además $|a_n|\le1/m\to0$ en todo caso: ese control por sí solo no decide el resultado.

Después del argumento, la [figura 11.5](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f05) permite contrastar el mecanismo con el ejemplo del capítulo.

Después de cada bloque completo el total es cero, porque las dos mitades se compensan exactamente. Dentro del bloque, todos los totales están entre cero y $h_m$, y la cima alcanza $h_m$. Si esas alturas tienden a cero, el encierro controla todos los índices posteriores, no sólo los finales. Si la serie converge, los finales fuerzan límite cero y las cimas deben acercarse a ese mismo límite. La serie converge exactamente cuando desaparecen las excursiones interiores, aunque las longitudes crezcan.

## 11.36. Una tolerancia estricta

[]{#MA-EX-ANM-01-011-036}

[]{#MA-SOL-ANM-01-011-036}

[]{#MA-SEC-ANM-01-011-008}

El resto exacto es $2^{-n}$. Se necesita $2^{-n}<1/16=2^{-4}$, así que el primer índice es $n=5$ y se suman seis términos. En $n=4$ el error es exactamente la tolerancia.

Después del argumento, la [figura 11.3](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f03) permite contrastar el mecanismo con el ejemplo del capítulo.

Para razón $1/2$, $s_n=2(1-2^{-(n+1)})=2-2^{-n}$, así que $S-s_n=2^{-n}$. La función del índice disminuye estrictamente; en cuatro vale $1/16$ y en cinco vale $1/32$. Todos los índices menores tienen un error mayor o igual que $1/16$, lo que demuestra que cinco es realmente el primero. Contar desde cero da seis aportes. Aquí podemos afirmar minimalidad porque conocemos el error exacto, no sólo una estimación.

## 11.37. Certificado sin suma conocida

[]{#MA-EX-ANM-01-011-037}

[]{#MA-SOL-ANM-01-011-037}

La prueba de §11.6 da $s_5\le S\le s_4$. Sumando finitamente, $s_4=47/60$ y $s_5=37/60$. El punto medio es $7/10$ y el semiancho $1/12<1/10$. Por tanto $|S-7/10|\le1/12$; no se identifica $S$ con ese punto medio.

Después del argumento, la [figura 11.6](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f06) permite contrastar el mecanismo con el ejemplo del capítulo.

La alternancia proporciona primero un encierro válido: el total par $s_4$ está arriba y el impar $s_5$ abajo. Luego hacemos el cálculo finito con denominador común 60. La anchura es $10/60=1/6$, y el punto medio reduce el peor error a $1/12$. Como $1/12<1/10$, satisface la precisión solicitada. El promedio no se presenta como valor exacto ni requiere una expresión cerrada para la suma de la serie.

## 11.38. Linealidad con dominio de validez

[]{#MA-EX-ANM-01-011-038}

[]{#MA-SOL-ANM-01-011-038}

La identidad finita de §11.8 da totales $\alpha s_n+\beta t_n$. C06, con $s_n\to A$ y $t_n\to B$, prueba suma $\alpha A+\beta B$. Las hipótesis no se borran: las series de términos uno y menos uno divergen, pero su suma término a término es la serie cero convergente. No existen dos sumas reales previas que puedan sumarse en ese ejemplo.

La identidad para totales se verifica antes de tomar límites: sumar hasta $n$ los aportes $\alpha a_j+\beta b_j$ da $\alpha s_n+\beta t_n$. El álgebra de límites sólo puede usarse cuando $s_n\to A$ y $t_n\to B$ son hipótesis demostradas. La cancelación de los aportes uno y menos uno produce una serie cero, pero los dos procesos originales carecen de sumas reales. Una combinación puede converger sin que esté permitido atribuir sumas a sus componentes divergentes.

## 11.39. Cambiar sólo un prefijo

[]{#MA-EX-ANM-01-011-039}

[]{#MA-SOL-ANM-01-011-039}

Para todo $n\ge m$, sus totales difieren en $D=\sum_{j=0}^{m-1}(a_j-b_j)$; en $m=0$ la suma vacía es cero. Si un proceso converge, el otro converge sumando o restando la constante $D$ en su cola. Cuando ambas sumas existen, $S_a-S_b=D$. Los términos pueden ser distintos y tener convergencia equivalente sin igualdad de sumas.

Para $n\ge m$, la diferencia de los totales contiene un prefijo de diferencias y una cola de ceros. Por eso queda la constante $D$ y ya no depende de $n$. Si $s_n^b\to S_b$, entonces $s_n^a=s_n^b+D\to S_b+D$; la dirección inversa usa $-D$. Para $m=0$ no hay prefijo, $D=0$, y las sucesiones coinciden desde el inicio. Convergencia equivalente no significa suma idéntica cuando el prefijo sí cambia.

## 11.40. Dos mecanismos en una sola serie

[]{#MA-EX-ANM-01-011-040}

[]{#MA-SOL-ANM-01-011-040}

La alternada tiene suma $B$ y error a lo sumo $1/(n+2)$. La perturbación geométricamente dominada converge absolutamente a $E$, con error a lo sumo $2^{-n}$. Linealidad da suma $S=B+E$, y triangular da $|S-s_n|\le1/(n+2)+2^{-n}$. Para demostrar que no es absoluta, la triangular implica $1/(n+1)\le|a_n|+|e_n|$. Si la serie de $|a_n|$ convergiera, sus totales y los de $|e_n|$ estarían acotados; sumando esta desigualdad, los totales armónicos quedarían acotados, contradicción. La original converge y sus magnitudes no, de modo que es condicional.

Después del argumento, la [figura 11.4](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html#fig-anm-c11-f04) permite contrastar el mecanismo con el ejemplo del capítulo.

La suma combina dos controles compatibles: cancelación alternada para el componente armónico y control absoluto para la perturbación. La triangular suma sus restos y proporciona un certificado que tiende a cero. Para excluir convergencia absoluta de la mezcla, escribimos el componente armónico como $a_n-e_n$ y tomamos magnitudes. La comparación obliga a que una hipotética suma absoluta de la mezcla, junto con la suma absoluta de la perturbación, acote la armónica. Como eso es imposible, la perturbación no puede eliminar su carácter condicional.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Ejercicios](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia-soluciones.html)
