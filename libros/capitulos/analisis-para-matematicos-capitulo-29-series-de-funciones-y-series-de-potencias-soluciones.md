---
content-id: MA-BCH-0320
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-029-SOLUCIONES
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
title: Soluciones — Capítulo 29
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C29_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)

## 29.1. La geométrica en dos dominios

[]{#MA-EX-ANM-01-029-001}

[]{#MA-SOL-ANM-01-029-001}

[]{#MA-SEC-ANM-01-029-001}

La identidad finita da $S_n=(1-x^{n+1})/(1-x)$ cuando $x\ne1$. Para $|x|<1$ su límite es $1/(1-x)$ y el resto $x^{n+1}/(1-x)$ tiene magnitud a lo sumo $r^{n+1}/(1-r)$ en la ventana. Si $|x|\ge1$, los términos no tienden a cero, así que el dominio es exactamente $(-1,1)$. Para cada $n$, el resto crece sin cota al aproximarse $x$ a $1$ desde la izquierda; no puede existir un corte uniforme en todo el dominio.

**Retorno visual.** Véase [C29-F01](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.2. Un término necesario

[]{#MA-EX-ANM-01-029-002}

[]{#MA-SOL-ANM-01-029-002}

Dado $\varepsilon>0$, escoja $N$ con $|S_n-S|<\varepsilon/2$ para $n\ge N$ y toda entrada. Si $j\ge N+1$, ambos $j,j-1$ superan el corte; la triangular da $|u_j|=|S_j-S_{j-1}|<\varepsilon$. La serie de funciones constantes $1/(j+1)$ tiene términos uniformemente nulos pero sumas parciales armónicas divergentes. El control de un término no controla bloques de longitud arbitraria.

## 29.3. Cortes dependientes de la entrada

[]{#MA-EX-ANM-01-029-003}

[]{#MA-SOL-ANM-01-029-003}

Se ha intercambiado $\forall x\exists N_x$ por $\exists N\forall x$. Para un índice dado $n$, tome $x_n=1-1/(2(n+1))$. Por la desigualdad finita de Bernoulli, $x_n^{n+1}\ge1/2$. Por tanto el resto geométrico es al menos $(n+1)$; en particular no es menor que $1$. Cada columna converge, pero estas entradas cambiantes impiden cualquier corte común.

## 29.4. Prefijo no acotado

[]{#MA-EX-ANM-01-029-004}

[]{#MA-SOL-ANM-01-029-004}

Para $n\ge0$, $S_n(x)=x^2+1-2^{-n}$ y $S=x^2+1$, de modo que el error es exactamente $2^{-n}$ en toda la recta. Sin embargo $x^2$ no está acotado globalmente y ningún $M_0$ finito lo domina. La cola uniforme no exige una barrera de valores para el prefijo común.

## 29.5. Cauchy sin suma conocida

[]{#MA-EX-ANM-01-029-005}

[]{#MA-SOL-ANM-01-029-005}

Fijada cada entrada, la cota y la simetría de diferencias hacen Cauchy la sucesión $S_n(x)$; completitud real entrega $S(x)$. Para $n,x$ fijos, pasar $m$ al límite conserva $|S-S_n|\le\eta_n$. Dado $\varepsilon>0$, un corte con toda la cola de $\eta_n$ menor que $\varepsilon$ funciona para todas las entradas. La existencia del destino procede de Cauchy, y la uniformidad del mismo presupuesto.

## 29.6. Mayorante dyádico

[]{#MA-EX-ANM-01-029-006}

[]{#MA-SOL-ANM-01-029-006}

[]{#MA-SEC-ANM-01-029-002}

La suma del mayorante es $6$, así que $|S(x)|\le6$. La cola desde $n+1$ es $3\,2^{-n}$. La desigualdad $3\,2^{-n}<3/8$ equivale a $n>3$, luego el primer índice garantizado es $4$. En $n=3$ la cota iguala la tolerancia; no acredita una desigualdad estricta.

## 29.7. La serie de magnitudes

[]{#MA-EX-ANM-01-029-007}

[]{#MA-SOL-ANM-01-029-007}

Para parciales positivos $A_n(x)=\sum_{j=0}^n|u_j(x)|$, la diferencia $A_m-A_n$ es una cola positiva dominada por la cola del mayorante, común a todas las entradas. Cauchy uniforme produce $A(x)$ y el error a lo sumo $T_n$. Las desigualdades finitas $A_n\le\sum_{j=0}^n M_j$ pasan al límite y dan $A\le\sum M_j$. Ésta es una prueba sobre otra serie, no una identificación de $A$ con $|S|$.

## 29.8. Uniformidad sin criterio M

[]{#MA-EX-ANM-01-029-008}

[]{#MA-SOL-ANM-01-029-008}

En $x=k$ hay exactamente un término no nulo y la suma vale $1/(k+1)$. El resto es cero si $k\le n$ y $1/(k+1)$ si $k>n$; su máximo es $1/(n+2)$, alcanzado en $k=n+1$. Las magnitudes son las mismas funciones, así que su serie también es uniforme. Cualquier $M_j$ común debe dominar la entrada $x=j$ y satisface $M_j\ge1/(j+1)$; comparación con la armónica impide sumabilidad.

**Retorno visual.** Véase [C29-F02](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.9. Cancelación uniforme

[]{#MA-EX-ANM-01-029-009}

[]{#MA-SOL-ANM-01-029-009}

Todos los parciales son constantes. C11 da un destino numérico y resto de magnitud a lo sumo $1/(n+2)$; la misma cota vale para todo $X$, luego hay uniformidad. Las magnitudes forman la armónica divergente en cada entrada. Por tanto no hay convergencia absoluta ni mayorante M sumable, pues éste tendría que dominar cada magnitud armónica.

## 29.10. Cambio de parámetro

[]{#MA-EX-ANM-01-029-010}

[]{#MA-SOL-ANM-01-029-010}

Es geométrica de razón $x/3$, así que $S=1/(1-x/3)$ y $R_n=(x/3)^{n+1}/(1-x/3)$. M usa $M_j=3^{-j}$ y cola $3^{-n}/2$. Para $0\le x\le1$, el resto no negativo crece con $x$ porque crecen numerador y recíproco del denominador; en $x=1$ vale precisamente $3^{-n}/2$. Aquí el certificado M es la envolvente exacta, no sólo una cota suficiente.

## 29.11. Integrales y orientación

[]{#MA-EX-ANM-01-029-011}

[]{#MA-SOL-ANM-01-029-011}

[]{#MA-SEC-ANM-01-029-003}

La uniformidad acredita integrabilidad del destino por C28. La longitud completa es $5$, por lo que el error de integral es a lo sumo $5\,2^{-n}$. Para cada $x$, la acumulada orientada desde $1$ tiene error a lo sumo $|x-1|2^{-n}$, y sobre todo el marco $|x-1|\le3$. El error uniforme de acumuladas es a lo sumo $3\,2^{-n}$, tanto a la izquierda como a la derecha del ancla.

## 29.12. Serie derivada con ancla

[]{#MA-EX-ANM-01-029-012}

[]{#MA-SOL-ANM-01-029-012}

Sean los términos continuos en $[a,b]$ y derivables en $(a,b)$; supongamos la serie de derivadas uniforme a $g$ y la serie de valores en $c\in[a,b]$ convergente a $\lambda$. Las sumas finitas $S_n$ son continuas y derivables, $S_n^{\prime}$ son los parciales de la serie derivada y $S_n(c)\to\lambda$. Cumplen exactamente C28: derivadas uniformes más ancla convergente. Allí se construye el límite uniforme $S$ de valores y se demuestra $S^{\prime}=g$ mediante incrementos. La identidad de series es esa conclusión, no una derivación formal previa.

## 29.13. Telescopio suave con esquina

[]{#MA-EX-ANM-01-029-013}

[]{#MA-SOL-ANM-01-029-013}

Los parciales telescópicos son $h_n$. Con $a=1/(n+1)$, $0\le\sqrt{x^2+a^2}-|x|=a^2/(\sqrt{x^2+a^2}+|x|)\le a$, con igualdad en cero. Por tanto el error uniforme es $a$. Cada fila es derivable y $h_n^{\prime}(0)=0$, pero el límite $|x|$ tiene cocientes $1$ desde la derecha y $-1$ desde la izquierda. Su derivada en cero no existe; el límite de derivadas en ese punto no permite intercambiarlas.

**Retorno visual.** Véase [C29-F03](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.14. Constantes invisibles

[]{#MA-EX-ANM-01-029-014}

[]{#MA-SOL-ANM-01-029-014}

Tome $u_j(x)=1$ en $[0,1]$. Las derivadas son cero y su serie converge uniformemente a cero. Los parciales de valores son $n+1$, divergentes en toda entrada. Falta convergencia de la serie de valores en una ancla. Uniformidad de pendientes sólo controla diferencias espaciales; no controla el nivel absoluto de los parciales.

## 29.15. Serie polinómica integrada

[]{#MA-EX-ANM-01-029-015}

[]{#MA-SOL-ANM-01-029-015}

Los coeficientes suman $2$, luego $S=2x^2$, $S_n=(2-2^{-n})x^2$. Las derivadas tienen mayorantes $2\,2^{-j}$ y el ancla cero es exacta, así que el intercambio es válido y $S^{\prime}=4x$. La integral es $2x^3/3$. Los errores uniformes de valores, derivadas y acumuladas son respectivamente $2^{-n}$, $2^{1-n}$ y $2^{-n}/3$, alcanzados en los extremos. La integración orientada da el signo correcto cuando $x<0$.

## 29.16. Convergencia en una entrada

[]{#MA-EX-ANM-01-029-016}

[]{#MA-SOL-ANM-01-029-016}

[]{#MA-SEC-ANM-01-029-004}

La distancia convergente es $3$, mientras $[0,4]$ tiene radio $2$ respecto del centro. El lema interior usa $\rho=2/3$, da convergencia absoluta y uniforme, y cota $5(2/3)^{n+1}/(1-2/3)=15(2/3)^{n+1}$. También asegura toda distancia estrictamente menor que $3$, sin decidir $5$, el extremo opuesto a $-1$.

**Retorno visual.** Véase [C29-F04](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.17. Supremo sin pertenencia

[]{#MA-EX-ANM-01-029-017}

[]{#MA-SOL-ANM-01-029-017}

$H$ contiene cero. Si está acotado tiene supremo $R$; si no, se usa el caso infinito. Para cualquier $0<r<R$ existe una distancia convergente $d>r$, porque de otro modo $r$ sería cota superior de $H$. El lema interior controla el segmento de radio $r$. El centro converge por separado. Una entrada convergente de distancia mayor que un $R$ finito pondría en $H$ un número superior a su cota, contradicción. Ningún paso necesita una entrada convergente de distancia exactamente $R$.

## 29.18. El término constante

[]{#MA-EX-ANM-01-029-018}

[]{#MA-SOL-ANM-01-029-018}

El monomio de orden cero es constante $1$; todos los monomios de orden positivo se anulan en el centro. La suma vale $a_0$. Por ejemplo $7+\sum_{j\ge1}j!(x-c)^j$ sólo converge en $c$, y allí vale $7$. El radio cero describe un dominio de un punto, no el valor de la función. La notación del monomio constante evita una evaluación ambigua de $0^0$.

## 29.19. Compactos interiores

[]{#MA-EX-ANM-01-029-019}

[]{#MA-SOL-ANM-01-029-019}

Si $K$ es vacío, la condición es vacua. En caso contrario, continuidad de $|x-c|$ y compacidad entregan un máximo $d$. Cada punto está en el intervalo abierto, luego el punto que alcanza el máximo tiene $d<R$. Escoja $r$ con $d<r<R$ (si $R=\infty$, cualquier $r>d$). El segmento cerrado de radio $r$ tiene uniformidad por el lema; restringir a $K$ conserva el corte común.

## 29.20. Radios iguales no dan cortes iguales

[]{#MA-EX-ANM-01-029-020}

[]{#MA-SOL-ANM-01-029-020}

La geométrica no converge en los extremos y no es uniforme en todo el abierto, pues su resto no está acotado cerca de $1$. Para la segunda, $|x^j|/(j+1)^2\le1/(j+1)^2$ en el cerrado, y la serie de estos mayorantes converge por comparación telescópica. M acredita uniformidad en todo el cerrado, y por restricción en el abierto. El radio describe la región interior de convergencia absoluta, pero no una tasa ni uniformidad hasta su frontera.

## 29.21. Cocientes acreditados

[]{#MA-EX-ANM-01-029-021}

[]{#MA-SOL-ANM-01-029-021}

[]{#MA-SEC-ANM-01-029-005}

Suponga términos eventualmente no nulos. Si el límite $L<1$, elija $L<q<1$ y un índice $N$ después del cual cada cociente es a lo sumo $q$. Inducción da $|b_{N+k}|\le|b_N|q^k$; la cola converge absolutamente por comparación geométrica y el prefijo finito no altera ello. Si $L>1$, elija $1<q<L$ y un índice con cocientes al menos $q$. Entonces $|b_{N+k}|\ge|b_N|q^k$, con $|b_N|>0$; los términos no tienden a cero. El límite $1$ no proporciona ninguna de esas dos barreras.

## 29.22. Trasladar y escalar

[]{#MA-EX-ANM-01-029-022}

[]{#MA-SOL-ANM-01-029-022}

El centro es $2$ y los cocientes de coeficientes en potencias de $x-2$ tienden a $1/3$, así que el radio es $3$. En $x=-1$, la razón normalizada es $-1$ y la alternada converge condicionalmente. En $x=5$ es $1$ y diverge la armónica. El dominio es $[-1,5)$. Los puntos exteriores divergen por el radio; los interiores convergen absolutamente.

## 29.23. Ceros en los coeficientes

[]{#MA-EX-ANM-01-029-023}

[]{#MA-SOL-ANM-01-029-023}

La serie es geométrica de razón $(x-1)^2$. Converge si esa razón es menor que $1$, es decir $|x-1|<1$, y diverge en los extremos y fuera porque los términos no desaparecen. Tiene radio $1$ y dominio $(0,2)$. Los coeficientes de grados impares son cero, de modo que hay cocientes indefinidos infinitamente a menudo; no se cumplen las hipótesis del método consecutivo.

## 29.24. Raíz sin cociente

[]{#MA-EX-ANM-01-029-024}

[]{#MA-SOL-ANM-01-029-024}

Para los índices pares la raíz es $2$; para los impares es $2/(j+1)^{1/j}$. Para probar $(j+1)^{1/j}\to1$, fijado $q>1$, la sucesión $(j+1)/q^j$ tiene cociente tendente a $1/q<1$, luego tiende a cero por barrera geométrica; eventualmente $j+1<q^j$. Así $1\le(j+1)^{1/j}<q$, y el límite es $1$. Las raíces de $a_j$ tienden a $2$, así que $R=1/2$. Los cocientes consecutivos alternan entre valores tendentes a cero e infinito, por lo que ese método no decide.

## 29.25. Todos los extremos

[]{#MA-EX-ANM-01-029-025}

[]{#MA-SOL-ANM-01-029-025}

Use $z=(x+3)/2$. La geométrica en $z$ tiene dominio $(-5,-1)$. La serie $\sum_{j\ge1}z^j/j$ tiene dominio $[-5,-1)$, y $\sum_{j\ge1}(-1)^jz^j/j$ tiene $(-5,-1]$. La serie $\sum_{j\ge0}z^j/(j+1)^2$ tiene $[-5,-1]$. En todos los casos el radio es $2$ por los cocientes de los coeficientes escalados. Las evaluaciones $z=\pm1$ se justifican respectivamente por término no nulo, alternada, armónica y comparación positiva telescópica.

**Retorno visual.** Véase [C29-F05](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.26. La cola derivada

[]{#MA-EX-ANM-01-029-026}

[]{#MA-SOL-ANM-01-029-026}

[]{#MA-SEC-ANM-01-029-006}

Derive la identidad polinómica finita $\sum_{j=0}^n\rho^j=(1-\rho^{n+1})/(1-\rho)$. Resulta $\sum_{j=1}^n j\rho^{j-1}=[1-(n+1)\rho^n+n\rho^{n+1}]/(1-\rho)^2$. La comparación de cocientes hace $n\rho^n\to0$, así que la suma total es $1/(1-\rho)^2$. Restar el parcial da $\rho^n[(n+1)-n\rho]/(1-\rho)^2$. El orden lógico acredita el mayorante antes de intercambiar derivadas y límites.

**Retorno visual.** Véase [C29-F06](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.27. Presupuesto derivativo concreto

[]{#MA-EX-ANM-01-029-027}

[]{#MA-SOL-ANM-01-029-027}

Los términos derivados están dominados por $3j\,2^{-j}$. La cola desde $j=n+1$ es $(3/2)\sum_{j>n}j(1/2)^{j-1}$. Con la fórmula anterior resulta $3(n+2)2^{-n}$. Para $n=4$ es $18/16=9/8$. Esta cota puede ser grande aunque el resto de valores sea $3\,2^{-n}$: el factor de índice consume parte del margen geométrico. El ancla constante y la sumabilidad derivada acreditan el intercambio en cualquier ventana estrictamente interior a radio $2$.

## 29.28. Una frontera no derivable por la serie

[]{#MA-EX-ANM-01-029-028}

[]{#MA-SOL-ANM-01-029-028}

La serie de valores converge condicionalmente en $-1$ por C11. Dentro del radio su derivada es $\sum_{j\ge1}x^{j-1}=1/(1-x)$. En $x=-1$ los términos de esa serie derivada alternan entre $1$ y $-1$ y no tienden a cero; diverge. El teorema de potencias declara sólo entradas estrictamente interiores. Incluso si la función interior admitiera una extensión derivable al borde, no sería lícito igualar esa derivada con una serie divergente.

## 29.29. Integral y radio

[]{#MA-EX-ANM-01-029-029}

[]{#MA-SOL-ANM-01-029-029}

La integrada ya converge en el interior por comparación y el teorema de integración. Si converge en una distancia $d>0$, existe $B$ con $|a_j|d^{j+1}/(j+1)\le B$. Para $0<r<d$, $|a_j|r^j\le(B/d)(j+1)(r/d)^j$, cuya serie converge por cociente. El radio original es al menos todos esos $r$. Si el radio de la integrada fuese mayor, escoger una distancia convergente y luego un $r$ entre el radio original y esa distancia contradiría lo anterior. La misma prueba cubre un supuesto radio integrado infinito frente a uno original finito.

## 29.30. Orden finito y ancla

[]{#MA-EX-ANM-01-029-030}

[]{#MA-SOL-ANM-01-029-030}

Iterar tres veces el teorema derivativo, con igualdad de radios en cada paso, da $F^{(3)}(x)=\sum_{j\ge3}j(j-1)(j-2)a_j(x-c)^{j-3}$ en $|x-c|<R$. En el centro sólo sobrevive $j=3$, luego $F^{(3)}(c)=6a_3$ y $a_3=F^{(3)}(c)/6$. Cada derivación usa uniformidad en una ventana interior y el ancla de su serie. No se hace una afirmación en la frontera ni para órdenes que cambien con el corte.

## 29.31. Certificado factorial

[]{#MA-EX-ANM-01-029-031}

[]{#MA-SOL-ANM-01-029-031}

[]{#MA-SEC-ANM-01-029-007}

El primer término omitido tiene magnitud a lo sumo $1/5!=1/120$. Desde allí los cocientes son a lo sumo $1/6$, de modo que la cola está dominada por $(1/120)/(1-1/6)=1/100$. Puesto que $1/100<1/50$, el mismo parcial de grado cuatro satisface la tolerancia en todas las entradas de la ventana. No se usa una aproximación decimal de la suma.

**Retorno visual.** Véase [C29-F07](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.32. Ecuación y positividad

[]{#MA-EX-ANM-01-029-032}

[]{#MA-SOL-ANM-01-029-032}

Radio infinito y derivación término a término dan $E^{\prime}=\sum_{j\ge1}x^{j-1}/(j-1)!=E$, por reindexación finita y límite. Producto y cadena dan derivada cero a $E(x)E(-x)$; valor medio sobre el segmento entre cero y cualquier $x$ lo identifica con el valor inicial $1$. Por tanto $E$ no se anula. Es continua y vale $1$ en cero; si tomara un valor negativo, valor intermedio en el segmento correspondiente produciría un cero, contradicción. Luego siempre es positiva.

## 29.33. Unicidad de coeficientes

[]{#MA-EX-ANM-01-029-033}

[]{#MA-SOL-ANM-01-029-033}

Para cada entero fijo $k$, la derivación iterada acreditada entrega en el centro $k!a_k$ para la primera representación y $k!b_k$ para la segunda. Las funciones coinciden en una vecindad abierta, luego por definición de derivadas y su iteración sus derivadas de orden $k$ allí coinciden. Como $k!\ne0$, $a_k=b_k$. El argumento requiere representaciones convergentes previamente existentes; no construye una representación para cualquier función suave.

## 29.34. Integral geométrica

[]{#MA-EX-ANM-01-029-034}

[]{#MA-SOL-ANM-01-029-034}

Cada segmento que une cero con $x$ está estrictamente dentro de $(-1,1)$ y la geométrica converge uniformemente allí. Integración término a término da $L(x)=\sum_{j\ge0}x^{j+1}/(j+1)=\sum_{j\ge1}x^j/j$. El integrando es continuo, así que el TFC de C24 da $L^{\prime}(x)=1/(1-x)$ en el interior y $L(0)=0$. Las cotas de error son longitud por resto geométrico. El resultado no asigna valores al integral en la singularidad $1$.

## 29.35. Ley de adición y unicidad concreta

[]{#MA-EX-ANM-01-029-035}

[]{#MA-SOL-ANM-01-029-035}

Para $a$ fijo, la derivada de $E(a+t)E(-t)$ es cero por $E^{\prime}=E$, producto y cadena; valor medio lo hace constante igual a $E(a)$. Multiplicar por $E(t)$, usando el producto recíproco, da $E(a+t)=E(a)E(t)$. Para otra solución $y$, la misma regla da derivada cero a $y(t)E(-t)$. En cada segmento desde cero dentro del intervalo el valor medio la hace igual a $1$, por la condición inicial. Multiplicar por $E(t)$ entrega $y(t)=E(t)$. Es una prueba para esta ecuación, no la invocación de una teoría general.

## 29.36. Triángulo de coeficientes

[]{#MA-EX-ANM-01-029-036}

[]{#MA-SOL-ANM-01-029-036}

[]{#MA-SEC-ANM-01-029-008}

Cada coeficiente es $d_n=\sum_{j=0}^n1=n+1$. La absoluta interior y el producto de Cauchy probado entregan $\sum_{n\ge0}(n+1)x^n=(1-x)^{-2}$ para $|x|<1$. Sus cocientes de coeficientes tienden a $1$, luego su radio es $1$. En ambos extremos los términos tienen magnitudes $n+1$, así que diverge allí. La cuenta finita de pares del triángulo explica el factor $n+1$.

**Retorno visual.** Véase [C29-F08](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html#fig-anm-c29-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 29.37. Colas del producto

[]{#MA-EX-ANM-01-029-037}

[]{#MA-SOL-ANM-01-029-037}

En el cuadrado de índice $m\ge N$, el triángulo de suma de índices a lo sumo $N$ está incluido. Para cualquier par excluido, al menos un índice excede $h=\lfloor N/2\rfloor$. La suma finita de magnitudes excluidas está entonces dominada por $B_*T_\alpha(h)+A_*T_\beta(h)$; contar dos veces algunos pares sólo aumenta la cota. Con $N$ fijo, pasar $m$ al límite hace converger el producto de parciales a $AB$. La cota pasa con desigualdad débil. Después $N\to\infty$ hace desaparecer las colas y demuestra que los parciales triangulares tienden a $AB$.

## 29.38. El radio del producto puede crecer

[]{#MA-EX-ANM-01-029-038}

[]{#MA-SOL-ANM-01-029-038}

La geométrica tiene coeficientes $a_n=1$ y radio $1$. El polinomio $1-x$ tiene $b_0=1$, $b_1=-1$, los demás cero y radio infinito. Los coeficientes del producto son $d_0=1$ y, para $n\ge1$, $d_n=a_n-a_{n-1}=0$. Su serie es constante y tiene radio infinito, mayor que el mínimo $1$. La igualdad entre el producto de las funciones originales y esa serie se acredita en $(-1,1)$; la geométrica original sigue divergente fuera.

## 29.39. Uniformidad del producto funcional

[]{#MA-EX-ANM-01-029-039}

[]{#MA-SOL-ANM-01-029-039}

En cada entrada son absolutamente convergentes y el producto numérico identifica el destino. Las colas de magnitudes tienen envolventes comunes $t_\alpha(h),t_\beta(h)\to0$ por la uniformidad supuesta. La cota triangular vale simultáneamente: el resto del producto de Cauchy es a lo sumo $B_*t_\alpha(\lfloor N/2\rfloor)+A_*t_\beta(\lfloor N/2\rfloor)$. Este presupuesto tiende a cero con un corte independiente de la entrada. Las barreras comunes se usan para que los factores no amplifiquen arbitrariamente las colas.

## 29.40. Un certificado reutilizable y su alcance

[]{#MA-EX-ANM-01-029-040}

[]{#MA-SOL-ANM-01-029-040}

Cada serie de magnitudes está acotada por $2$, con cola desde $h+1$ a lo sumo $2^{-h}$. El método triangular da cota $4\,2^{-\lfloor N/2\rfloor}$. Por la identidad ponderada geométrica, la cola de coeficientes $(n+1)x^n$ tiene envolvente exacta en $x=1/2$: $\sum_{n>N}(n+1)2^{-n}=(N+3)2^{-N}$. La primera es suficiente y suele ser menos ajustada; ambas tienden a cero. El argumento usa magnitudes, triangular y regiones interiores, mecanismos que se trasladarán a discos complejos. No acredita por sí solo diferenciabilidad compleja ni valores en toda la frontera.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 29](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html) · [Ejercicios](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias-microcontroles.html)
