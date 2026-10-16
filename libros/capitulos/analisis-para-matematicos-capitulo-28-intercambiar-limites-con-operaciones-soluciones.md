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
date-modified: '2026-10-13'
provenance:
  type: original
  sources:
  - ANM-C28_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html)

## 28.1. Una fila dentro de la banda

[]{#MA-EX-ANM-01-028-001}

[]{#MA-SOL-ANM-01-028-001}

[]{#MA-SEC-ANM-01-028-001}

Sea $x_0$ el centro y $\varepsilon>0$. La uniformidad permite fijar una fila $f_N$ con $|f_N(x)-f(x)|<\varepsilon/3$ para toda entrada del dominio. La continuidad de esa fila en $x_0$ proporciona $\delta>0$ tal que $|f_N(x)-f_N(x_0)|<\varepsilon/3$ si $x$ es admisible y $|x-x_0|<\delta$. Entonces $|f(x)-f(x_0)|\le|f(x)-f_N(x)|+|f_N(x)-f_N(x_0)|+|f_N(x_0)-f(x_0)|<\varepsilon$. El radio se obtuvo después de fijar la fila, y los errores de aproximación ya controlaban toda la vecindad. La prueba vale relativamente al dominio, incluidos sus bordes.

**Retorno visual.** Véase [C28-F01](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.2. Radios para todos los pares

[]{#MA-EX-ANM-01-028-002}

[]{#MA-SOL-ANM-01-028-002}

Para $\varepsilon>0$, fijamos una fila de error global menor que $\varepsilon/3$. Su continuidad uniforme proporciona un radio $\delta>0$ que sirve para todos los pares $x,y$ con $|x-y|<\delta$. En esos pares, la triangular da $|f(x)-f(y)|\le|f(x)-f_N(x)|+|f_N(x)-f_N(y)|+|f_N(y)-f(y)|<\varepsilon$. El radio es común a los pares del dominio porque pertenece a una fila uniformemente continua. Puede depender de la fila escogida para esta tolerancia; no se necesita que las otras filas compartan el mismo radio.

## 28.3. Destino continuo sin uniformidad

[]{#MA-EX-ANM-01-028-003}

[]{#MA-SOL-ANM-01-028-003}

Las potencias declaradas con fila inicial uno tienen límite cero en cada entrada fija de $[0,1)$. Esa candidata es continua. Para cada $n\ge1$, todos los errores $x^n$ son menores que uno, pero su supremo es uno: dado $0\le c<1$, una entrada $x=1-s$ con $s=(1-c)/[2(n+1)]$ satisface $x^n\ge1-ns>c$ por Bernoulli. Por tanto las envolventes no tienden a cero y no hay uniformidad. Este ejemplo refuta la recíproca: continuidad del destino de una familia puntual de filas continuas no fuerza convergencia uniforme.

## 28.4. Valores sin barrera global

[]{#MA-EX-ANM-01-028-004}

[]{#MA-SOL-ANM-01-028-004}

La diferencia entre $x+1/(n+1)$ y la identidad es la constante $1/(n+1)\to0$, así la convergencia es uniforme en toda la recta. En cada fila, $|f_n(x)-f_n(y)|=|x-y|$, y la misma identidad vale para el destino. Son por tanto Lipschitz con constante uno y uniformemente continuas. Sus valores no tienen barrera global porque aumentan sin cota al crecer la entrada. El teorema de continuidad utiliza las diferencias uniformemente pequeñas y la continuidad de una fila fija, sin requerir acotación de los valores.

## 28.5. Filas continuas arbitrariamente tardías

[]{#MA-EX-ANM-01-028-005}

[]{#MA-SOL-ANM-01-028-005}

Ante $\varepsilon>0$, el contrato uniforme entrega un corte $N$ para error $\varepsilon/3$. La hipótesis de índices continuos arbitrariamente grandes permite tomar algún $n\ge N$ cuya fila sea continua en $x_0$. Fijamos esa fila y su radio para variación menor que $\varepsilon/3$. Como está en la cola, los errores de aproximación en $x$ y $x_0$ también son menores que esa cantidad. La triangular de tres términos prueba continuidad de $f$ en el centro. Se necesita sólo una fila adecuada para la tolerancia recibida, sin construir una subsucesión infinita de ellas.

## 28.6. Construir el destino de los destinos

[]{#MA-EX-ANM-01-028-006}

[]{#MA-SOL-ANM-01-028-006}

[]{#MA-SEC-ANM-01-028-002}

Bajo R2, $f_n\to f$ uniformemente y cada fila tiene límite relativo perforado $p_n$ en el centro de acumulación $a$. Para $\eta>0$, Cauchy uniforme proporciona $N$ con $|f_n(x)-f_m(x)|<\eta/2$ para todo $m,n\ge N$ y toda entrada. Fijamos esos índices y llevamos $x\to a$ dentro del dominio perforado. El álgebra de límites y la continuidad del absoluto dan destino $|p_n-p_m|$, y la preservación del orden da $|p_n-p_m|\le\eta/2<\eta$. El corte sirve para todos los pares tardíos, así $(p_n)$ es de Cauchy. La acumulación asegura entradas efectivas y unicidad de los límites utilizados. Completitud de C10 construye su destino real $p$.

## 28.7. El límite que aún no existía

[]{#MA-EX-ANM-01-028-007}

[]{#MA-SOL-ANM-01-028-007}

Ya se construyó $p=\lim_n p_n$. Fijada $\varepsilon>0$, escogemos una fila $n$ posterior al corte uniforme para error $\varepsilon/3$ y al corte numérico para $|p_n-p|<\varepsilon/3$. Con ese índice fijo, el límite local de la fila proporciona $\delta>0$ con $|f_n(x)-p_n|<\varepsilon/3$ para toda entrada perforada a distancia menor que $\delta$ de $a$. La triangular da $|f(x)-p|\le|f(x)-f_n(x)|+|f_n(x)-p_n|+|p_n-p|<\varepsilon$. Esto prueba existencia del límite relativo de $f$ y su igualdad con $p$. El valor en $a$, si pertenece al dominio, no interviene en el contrato perforado.

## 28.8. Iterados diferentes

[]{#MA-EX-ANM-01-028-008}

[]{#MA-SOL-ANM-01-028-008}

Para $x>0$ fijo, $|r_n(x)-1|=1/[1+(n+1)x]\to0$, así el límite por índice es uno y su límite posterior por $x\to0^+$ también es uno. Para $n$ fijo, la continuidad del cociente en cero da $\lim_{x\to0^+}r_n(x)=0$; el límite por índice de esos destinos es cero. En la ruta $x_n=1/(n+1)$, el producto de escala vale uno y $r_n(x_n)=1/2$ para toda etapa. Los dos iterados y la diagonal están definidos y difieren. No hay uniformidad hacia uno en $(0,1]$: el error se aproxima a uno al acercar la entrada al origen en una fila fija, por lo que su supremo es uno.

**Retorno visual.** Véase [C28-F02](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.9. Uniformidad en una ventana fija

[]{#MA-EX-ANM-01-028-009}

[]{#MA-SOL-ANM-01-028-009}

Sea $Y=X\cap\{x:0<|x-a|<r\}$, con $r>0$ fijo. El centro sigue siendo punto de acumulación de $Y$, y cada límite de fila en $a$ se conserva al restringir porque las entradas suficientemente próximas ya pertenecen a esa ventana. La uniformidad supuesta en $Y$ permite aplicar R2 allí y obtener un destino $p$ para los límites de fila y para la función restringida. Para volver a $X$, dado un radio válido en $Y$ tomamos su mínimo con $r$. Toda entrada perforada de $X$ dentro de ese radio pertenece a $Y$ y cumple la misma desigualdad. Ventanas diferentes por fila no proporcionan este dominio común fijo.

## 28.10. Una ruta conjunta

[]{#MA-EX-ANM-01-028-010}

[]{#MA-SOL-ANM-01-028-010}

La ruta está dada con $x_n\in X\setminus\{a\}$ y $x_n\to a$. R2 ya probó que $f(x)\to p$ en el dominio perforado. Para $\varepsilon>0$, la uniformidad da un corte para $|f_n(x)-f(x)|<\varepsilon/2$ en toda entrada. El límite relativo de $f$ da un radio, y la convergencia de la ruta da otro corte desde el que $|f(x_n)-p|<\varepsilon/2$. El máximo de ambos cortes controla $|f_n(x_n)-p|\le|f_n(x_n)-f(x_n)|+|f(x_n)-p|<\varepsilon$. No se escoge una ruta por cada escala: se demuestra la afirmación para cualquier ruta admisible ya dada.

## 28.11. La cubierta creciente

[]{#MA-EX-ANM-01-028-011}

[]{#MA-SOL-ANM-01-028-011}

[]{#MA-SEC-ANM-01-028-003}

Sean las filas continuas sobre un compacto $K$, decrecientes por columnas hacia una función continua $f$. El orden al límite da $e_n=f_n-f\ge0$; los errores son continuos y decrecen puntualmente a cero. Para $\varepsilon>0$, los abiertos relativos $U_n=\{x\in K:e_n(x)<\varepsilon/2\}$ forman una cubierta creciente de $K$. Compacidad proporciona una subcubierta finita $U_{n_1},\ldots,U_{n_k}$. Tomamos $N=\max(n_1,\ldots,n_k)$. Como la cubierta es creciente, $K\subseteq U_N\subseteq U_n$ para todo $n\ge N$. Luego $|f_n(x)-f(x)|=e_n(x)<\varepsilon/2<\varepsilon$ para toda entrada de esa cola. Ésta es uniformidad. Si $K$ es vacío, el contrato es vacuo y se toma cualquier corte.

**Retorno visual.** Véase [C28-F03](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.12. Sin compacidad

[]{#MA-EX-ANM-01-028-012}

[]{#MA-SOL-ANM-01-028-012}

En $(0,1)$, cada potencia es continua, las columnas decrecen y el destino puntual es la función cero continua. Pero para cada $n\ge1$ su error supremo es uno, mediante entradas arbitrariamente próximas a uno. No hay uniformidad. La cubierta creciente de error pequeño de la prueba de Dini no tiene una subcubierta finita que alcance todo el dominio: cualquier máximo de índices deja entradas próximas a uno con error grande. El dominio abierto no es compacto, mostrando que esa hipótesis sostiene un paso necesario de la prueba.

## 28.13. Sin continuidad de las filas

[]{#MA-EX-ANM-01-028-013}

[]{#MA-SOL-ANM-01-028-013}

Los intervalos $(0,1/(n+1))$ se encogen, así $s_{n+1}\le s_n$ por columnas. En cero la altura siempre es cero; en cualquier $x>0$ fijo, desde $n+1>1/x$ la entrada queda fuera y la cola vale cero. El límite es la función cero continua sobre el compacto $[0,1]$. Sin embargo $x_n=1/[2(n+1)]$ tiene altura uno en toda etapa, así el máximo de error es uno y no hay uniformidad. Cada fila es discontinua relativamente en cero y en el otro extremo de su intervalo positivo. Falta la continuidad de las filas requerida por Dini.

## 28.14. Sin monotonía

[]{#MA-EX-ANM-01-028-014}

[]{#MA-SOL-ANM-01-028-014}

Las tiendas de C26 son continuas sobre el compacto $[0,1]$, tienen límite puntual cero continuo y conservan máximo uno en cada etapa. Para mostrar directamente la falta de monotonía decreciente, fijamos $x=2/9$. En la etapa cero, con $k=3$, la altura es cero; en la etapa seis, con $k=9$, es uno. Esa columna aumentó. Tampoco puede ser una familia creciente: en $x=2/3$ la primera altura es uno y la cola termina en cero. Así las columnas no tienen un mismo sentido de monotonía. Es la hipótesis de Dini que este ejemplo no satisface.

## 28.15. Pegar uniformidad local

[]{#MA-EX-ANM-01-028-015}

[]{#MA-SOL-ANM-01-028-015}

Sea una cubierta abierta dada de un compacto $K$, y supongamos uniformidad hacia la misma candidata en cada corte de la cubierta con $K$. Compacidad extrae finitísimos abiertos cuyos cortes todavía cubren $K$. Para $\varepsilon>0$, cada corte seleccionado entrega un índice válido; tomamos el máximo de esa lista finita. Toda entrada de $K$ pertenece a alguno y cumple el error menor que $\varepsilon$ en cualquier etapa posterior al máximo. Así hay uniformidad global. Las piezas son fijas antes de recibir los índices. Si $K$ es vacío, cualquier corte sirve sin seleccionar piezas.

## 28.16. Existencia antes de integrar

[]{#MA-EX-ANM-01-028-016}

[]{#MA-SOL-ANM-01-028-016}

[]{#MA-SEC-ANM-01-028-004}

Sea $\ell=b-a>0$. La uniformidad con tolerancia uno permite fijar una fila integrable $f_N$, acotada por algún $B_N$, con $|f-f_N|<1$ en todo el segmento. Así $|f|\le B_N+1$ y sus sumas de Darboux están definidas. Para $\varepsilon>0$, escogemos una fila con error global a lo sumo $\delta=\varepsilon/[8(\ell+1)]$, y una partición de esa fila con brecha menor que $\varepsilon/2$. La comparación de oscilaciones da $G(f,P)\le G(f_n,P)+2\delta\ell<\varepsilon/2+\varepsilon\ell/[4(\ell+1)]<3\varepsilon/4<\varepsilon$. Darboux prueba integrabilidad del destino antes de escribir su valor integral. Si $a=b$, la integral se trata por la convención degenerada y no se divide por $\ell$.

## 28.17. Error del valor integral

[]{#MA-EX-ANM-01-028-017}

[]{#MA-SOL-ANM-01-028-017}

Una vez probada la integrabilidad de $f$, la diferencia $f_n-f$ y su absoluto son integrables por C23. En la cola donde existe la envolvente real $E_n$, cada error está acotado por ella. Linealidad, desigualdad triangular integral y orden dan $|I_n-I|=|\int_a^b(f_n-f)|\le\int_a^b|f_n-f|\le\ell E_n$. La cota es universal y no necesita un máximo alcanzado. Como la uniformidad da $E_n\to0$ y $\ell$ es fija y finita, los valores integrales convergen a $I$. En el caso degenerado ambos valores son cero.

## 28.18. La cota se alcanza

[]{#MA-EX-ANM-01-028-018}

[]{#MA-SOL-ANM-01-028-018}

Las tasas $f_n(t)=t^2+1/(n+1)$ son continuas e integrables en $[0,1]$. Su límite uniforme es $f(t)=t^2$, porque el error es exactamente $E_n=1/(n+1)$ en todas las entradas. La integral del cuadrado es $1/3$ y la perturbación constante integra $1/(n+1)$ por longitud uno. Así $I_n=1/3+1/(n+1)$, $I=1/3$ y $|I_n-I|=1/(n+1)=\ell E_n$. La cota general se alcanza cuando la perturbación tiene magnitud y signo constantes.

## 28.19. Destinos existentes pero distintos

[]{#MA-EX-ANM-01-028-019}

[]{#MA-SOL-ANM-01-028-019}

Las tiendas $t_n$ son continuas y tienen integral $1/(n+3)$. Para $b_n=(n+3)t_n$, la linealidad da integral uno en cada etapa. Cada entrada fija queda finalmente fuera del soporte y la columna es cero, así el límite puntual es la función cero, integrable con valor cero. Por tanto $\lim_n\int_0^1b_n=1$ y $\int_0^1\lim_n b_n=0$. Las dos operaciones existen y dan valores distintos. La uniformidad falta porque el máximo de error de las filas normalizadas es $n+3$, alcanzado en su centro móvil.

**Retorno visual.** Véase [C28-F04](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.20. Un destino no integrable

[]{#MA-EX-ANM-01-028-020}

[]{#MA-SOL-ANM-01-028-020}

Los indicadores de los conjuntos finitos $E_{n+1}$ de racionales son integrables y tienen valor cero por modificaciones finitas. En cada racional reducido, la columna pasa definitivamente a uno cuando su denominador queda incluido; en cada irracional permanece cero. El destino puntual es Dirichlet, que tiene ínfimo cero y supremo uno en toda pieza no degenerada. Su brecha fija impide integrabilidad propia. Así el límite de valores integrales existe y vale cero, pero la integral del destino no existe. Este fallo difiere del ejemplo de tiendas normalizadas, donde ambas operaciones estaban definidas y discrepaban en valor.

## 28.21. Todas las acumulaciones

[]{#MA-EX-ANM-01-028-021}

[]{#MA-SOL-ANM-01-028-021}

[]{#MA-SEC-ANM-01-028-005}

Bajo R4, las filas y el destino son integrables y sus restricciones permiten definir las acumuladas desde $c\in[a,b]$. Por linealidad, $A_n(x)-A(x)=\int_c^x(f_n-f)$. Si $x>c$, el orden integral da magnitud a lo sumo $(x-c)E_n$. Si $x<c$, se invierte orientación y se obtiene la misma cota con $c-x$; en igualdad, la diferencia es cero. Por tanto $|A_n(x)-A(x)|\le|x-c|E_n\le\ell E_n$ para todo destino $x$. Esta barrera común tiende a cero y prueba uniformidad de las acumuladas en el segmento completo.

## 28.22. Peso integrable

[]{#MA-EX-ANM-01-028-022}

[]{#MA-SOL-ANM-01-028-022}

El peso fijo $w$, las filas y el destino son integrables, así C23 garantiza productos, diferencias y absolutos integrables. La diferencia de valores ponderados es la integral de $w(f_n-f)$. En toda entrada de la cola, $|w(f_n-f)|\le E_n|w|$. Luego $|\int wf_n-\int wf|\le\int|w(f_n-f)|\le E_n\int_a^b|w|$. El último factor es un real finito fijo, así el error tiende a cero. Si vale cero, la cota hace el error exactamente cero. Con una barrera $|w|\le M$ también se obtiene la cota $M\ell E_n$, posiblemente menos ajustada.

## 28.23. Mover los extremos

[]{#MA-EX-ANM-01-028-023}

[]{#MA-SOL-ANM-01-028-023}

Los extremos $u_n,v_n,u,v$ permanecen en $[a,b]$ y el destino integrable tiene cota $|f|\le B$. Insertamos la integral de $f$ entre los extremos móviles. Cambiar la integranda cuesta a lo sumo $|v_n-u_n|E_n\le\ell E_n$. Para los extremos, aditividad orientada da $\int_{u_n}^{v_n}f-\int_u^v f=\int_{u_n}^u f+\int_v^{v_n}f$. Las magnitudes de estas dos contribuciones no superan $B|u_n-u|$ y $B|v_n-v|$. La triangular produce $|\int_{u_n}^{v_n}f_n-\int_u^v f|\le\ell E_n+B|u_n-u|+B|v_n-v|$. Los tres términos tienden a cero. La orientación cubre cualquier orden de extremos y los intervalos degenerados.

## 28.24. El marco que crece

[]{#MA-EX-ANM-01-028-024}

[]{#MA-SOL-ANM-01-028-024}

Sobre la recta, las funciones constantes $f_n=1/(n+1)$ convergen uniformemente a cero con error $E_n=1/(n+1)$. En el intervalo de la etapa $[0,n+1]$, su integral propia es altura por longitud: $\int_0^{n+1}f_n=(1/(n+1))(n+1)=1$. La longitud creciente compensa exactamente el error pequeño. El teorema de intercambio de R4 usa un segmento fijo de longitud finita, y el de extremos móviles usa extremos convergentes dentro de ese marco. Estas hipótesis no se cumplen aquí. Cada integral del ejemplo es propia y finita; no se necesita una teoría de integrales impropias.

**Retorno visual.** Véase [C28-F05](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.25. Continuidad de la acumulada y derivada

[]{#MA-EX-ANM-01-028-025}

[]{#MA-SOL-ANM-01-028-025}

La integrabilidad basta para construir acumulaciones y hacerlas Lipschitz, por una cota absoluta de la tasa. Bajo uniformidad de las integrandas, sus acumuladas convergen uniformemente por la longitud común. Si las integrandas son además continuas, R1 hace continuo al destino y C24 identifica las derivadas de sus acumuladas con las tasas en el interior, y relativamente en los bordes. Si sólo son integrables, la recuperación de la tasa exige continuidad en el centro considerado. Un pico aislado puede cambiar la tasa sin cambiar ninguna acumulación; un salto puede producir una esquina sin derivada. La continuidad de la acumulada y la identificación de su derivada tienen por tanto hipótesis diferentes.

## 28.26. La ancla y todos los valores

[]{#MA-EX-ANM-01-028-026}

[]{#MA-SOL-ANM-01-028-026}

[]{#MA-SEC-ANM-01-028-006}

Sea $\ell=b-a$, con filas continuas en el cerrado y derivables dentro como en R6. La convergencia de $f_n(c)$ hace de Cauchy esa sucesión de anclaje. La uniformidad de $g_n=f_n'$ hace de Cauchy uniforme a las derivadas. Para $\varepsilon>0$, reunimos un corte con $|f_n(c)-f_m(c)|<\varepsilon/2$ y otro con $|g_n-g_m|<\varepsilon/[2(\ell+1)]$ en el interior. Lagrange aplicado a $f_n-f_m$ entre $c$ y cualquier $x$ da $|f_n(x)-f_m(x)|\le|f_n(c)-f_m(c)|+\varepsilon|x-c|/[2(\ell+1)]<\varepsilon/2+\varepsilon\ell/[2(\ell+1)]<\varepsilon$. El mismo corte sirve para todos los pares tardíos y todas las entradas. C27 construye el límite uniforme de valores.

## 28.27. El error de incrementos

[]{#MA-EX-ANM-01-028-027}

[]{#MA-SOL-ANM-01-028-027}

En la cola, las envolventes de derivadas dan $|g_m-g_n|\le|g_m-g|+|g-g_n|\le E_m+E_n$ en todo $(a,b)$. Lagrange aplicado a $f_m-f_n$ entre $x,y\in[a,b]$ produce $|(f_m-f_n)(y)-(f_m-f_n)(x)|\le(E_m+E_n)|y-x|$. Fijamos $n,x,y$ y llevamos $m\to\infty$. Las dos columnas de valores convergen a $f(y),f(x)$ y $E_m\to0$, así el orden conserva $|(f-f_n)(y)-(f-f_n)(x)|\le E_n|y-x|$. Para $x=y$ es inmediato. No se ha usado derivabilidad de $f$; ésta se probará a partir de la estimación ya obtenida.

## 28.28. Tres errores de cocientes

[]{#MA-EX-ANM-01-028-028}

[]{#MA-SOL-ANM-01-028-028}

Fijamos $x_0\in(a,b)$ y $\varepsilon>0$. Elegimos una fila $n$ con $E_n<\varepsilon/3$. Para $x\ne x_0$, dividir la cota de incrementos por $|x-x_0|>0$ limita la magnitud de la diferencia de los cocientes de $f$ y $f_n$ por $E_n$. La derivabilidad de esa fila fija proporciona un radio en el que su cociente difiere de $g_n(x_0)$ en menos que $\varepsilon/3$. Reducimos el radio para permanecer en el interior. Finalmente, $|g_n(x_0)-g(x_0)|\le E_n$. La triangular entre el cociente de $f$, el de la fila, su derivada y $g(x_0)$ da error menor que $\varepsilon$. Esto es la definición de $f'(x_0)=g(x_0)$ y completa la prueba sin asumir de antemano esa derivada.

## 28.29. Certificado de valores desde derivadas

[]{#MA-EX-ANM-01-028-029}

[]{#MA-SOL-ANM-01-028-029}

Tomamos $c$ como una de las entradas en la cota de incrementos del ejercicio anterior. Como la convergencia de la columna de anclaje identifica $f(c)=\lambda$, queda $|(f-f_n)(x)-(\lambda-f_n(c))|\le E_n|x-c|$. Por triangular, $|f_n(x)-f(x)|\le|f_n(c)-\lambda|+|x-c|E_n$. Reemplazar la distancia por $\ell$ da una cota uniforme de valores. El primer término mide la constante inicial y el segundo la discrepancia de variaciones. Ambos tienden a cero; si el anclaje es exacto, sólo permanece el segundo.

## 28.30. Derivadas sin continuidad

[]{#MA-EX-ANM-01-028-030}

[]{#MA-SOL-ANM-01-028-030}

Lagrange exige continuidad de las funciones comparadas en el segmento y derivabilidad en su interior, pero no continuidad de sus derivadas. R6 aplica esa herramienta a diferencias de filas y usa una cota uniforme de las diferencias de derivadas. La identificación final del destino se obtiene mediante cocientes de una fila fija y la cota proporcional de incrementos. No se integra $g$ ni se presupone que sea una tasa continua o integrable. Si las derivadas tienen extensiones continuas y convergen uniformemente, el teorema de continuidad añade esa regularidad al destino como una conclusión adicional.

## 28.31. Una esquina como límite uniforme

[]{#MA-EX-ANM-01-028-031}

[]{#MA-SOL-ANM-01-028-031}

[]{#MA-SEC-ANM-01-028-007}

Con $k=n+1>0$, la raíz de $x^2+k^{-2}$ es al menos $|x|$. Por otra parte, $(|x|+1/k)^2=x^2+2|x|/k+k^{-2}\ge x^2+k^{-2}$ y ambos lados comparados son no negativos. Así $0\le q_n(x)-|x|\le1/k$ para toda entrada, con igualdad en cero. La envolvente exacta es $1/(n+1)\to0$, probando uniformidad en toda la recta. Cada fila es derivable, porque la raíz se aplica a argumentos positivos, y $q_n'(x)=x/\sqrt{x^2+k^{-2}}$. El destino $|x|$ tiene cocientes menos uno a la izquierda de cero y uno a la derecha, así no es derivable allí. Uniformidad de valores no conserva esa propiedad.

## 28.32. Los dos destinos de derivadas existen

[]{#MA-EX-ANM-01-028-032}

[]{#MA-SOL-ANM-01-028-032}

La envolvente de valores de $h_n$ es $1/(2\sqrt{n+1})\to0$, así su límite es la función cero uniformemente. Con $k=n+1$, la regla del cociente da $h_n'(x)=(1-kx^2)/(1+kx^2)^2$. En cero vale uno para toda etapa; si $x\ne0$, su magnitud está acotada por $1/(1+kx^2)\to0$. Por tanto las derivadas tienen límite puntual $\mathbf1_{\{0\}}$. La derivada de la función límite es cero en todo centro y difiere de esa indicadora en el origen. Las derivadas, continuas, no convergen uniformemente a su destino discontinuo por R1. El ejemplo conserva la existencia de ambas operaciones y muestra que sus valores no coinciden.

**Retorno visual.** Véase [C28-F06](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.33. Sin anclaje

[]{#MA-EX-ANM-01-028-033}

[]{#MA-SOL-ANM-01-028-033}

Sobre un intervalo no vacío, las filas constantes $f_n(x)=n$ tienen derivadas cero en cada punto interior. Esa familia de derivadas es uniformemente constante cero, pero los valores crecen sin cota en cualquier anclaje y no convergen a un real. Otra familia es $f_n(x)=(-1)^n$, también con derivadas cero, cuyos valores alternan entre uno y menos uno sin límite. Ambos casos muestran que el control de derivadas deja libres las constantes aditivas. Ninguno cumple la convergencia del dato de anclaje exigida por R6.

## 28.34. Sólo uniformidad en segmentos

[]{#MA-EX-ANM-01-028-034}

[]{#MA-SOL-ANM-01-028-034}

En toda la recta, $f_n'(x)=1/(n+1)$ converge uniformemente a cero y $f_n(0)=0$ fija exactamente el anclaje. En cada segmento $[-M,M]$, el error de valores hacia cero tiene envolvente $M/(n+1)\to0$. Así se obtiene uniformidad en marcos acotados. Globalmente, cada fila $x/(n+1)$ tiene errores no acotados; además la entrada $x=n+1$ mantiene error uno en todas las etapas. El factor $|x-c|$ del certificado de R6 carece de barrera en la recta. El resultado sobre un segmento fijo no promete uniformidad global allí.

## 28.35. Una ancla por componente

[]{#MA-EX-ANM-01-028-035}

[]{#MA-SOL-ANM-01-028-035}

En $X=[0,1]\cup[2,3]$, definimos $f_n=0$ en la primera componente y $f_n=n$ en la segunda. Son continuas relativamente al dominio y derivables con derivada cero en los interiores de ambas piezas. Las derivadas convergen uniformemente a cero y el anclaje $f_n(0)=0$ es exacto. Sin embargo cualquier columna de la segunda componente diverge. El segmento que une una entrada de cada pieza atraviesa $(1,2)$, donde las funciones no están dadas, así no puede aplicarse Lagrange para transportar el dato inicial. Se necesita una ancla que fije la constante de cada componente.

## 28.36. El paquete polinómico

[]{#MA-EX-ANM-01-028-036}

[]{#MA-SOL-ANM-01-028-036}

[]{#MA-SEC-ANM-01-028-008}

La diferencia del paquete es $f_n(x)-f(x)=-2^{-n}x$. En $[-1,1]$ su magnitud máxima es $2^{-n}$, alcanzada en ambos extremos. Las derivadas son $g_n(x)=2x+1-2^{-n}$ y $g(x)=2x+1$; su diferencia es la constante $-2^{-n}$ y tiene la misma envolvente. Todas las funciones son polinomios y el anclaje en cero es exactamente cero. R6 permite identificar la derivada del destino bajo ese control. Para la norma de dos capas, $\|f_n-f\|_{C^1}=2^{-n}+2^{-n}=2^{1-n}$, que tiende a cero.

## 28.37. El error de acumulación

[]{#MA-EX-ANM-01-028-037}

[]{#MA-SOL-ANM-01-028-037}

Con anclaje de acumulación en cero, las primitivas polinómicas y Newton–Leibniz dan $A_n(x)=x^3/3+(1-2^{-n})x^2/2$ y $A(x)=x^3/3+x^2/2$. La fórmula también vale para $x<0$ por orientación. Su diferencia es $-2^{-n}x^2/2$, con envolvente exacta $2^{-n}/2$ en $[-1,1]$, alcanzada en los extremos. En cambio, el error integral de las tasas sobre todo el segmento es $\int_{-1}^1-2^{-n}x\,dx=0$. La cancelación firmada de ese tramo completo no implica igualdad de cada acumulación desde cero.

**Retorno visual.** Véase [C28-F07](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.38. Frontera estricta dyádica

[]{#MA-EX-ANM-01-028-038}

[]{#MA-SOL-ANM-01-028-038}

El error exacto de derivadas es $D_n=2^{-n}$. Para $n=3$ se tiene $D_3=1/8$, en la frontera y fuera del requisito estricto. Para $n=4$, $D_4=1/16<1/8$, y cualquier índice posterior tiene error todavía menor. Si el corte fuera menor que cuatro, su cola incluiría la etapa tres, que falla. Por tanto el corte mínimo para controlar toda la cola con error estrictamente menor que $1/8$ es $N=4$.

**Retorno visual.** Véase [C28-F08](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html#fig-anm-c28-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 28.39. Norma de dos capas

[]{#MA-EX-ANM-01-028-039}

[]{#MA-SOL-ANM-01-028-039}

La clase de R8 contiene funciones continuas en un segmento no degenerado cuya derivada interior admite extensión continua al cerrado. Esa extensión es única porque el interior es denso, y las extensiones de sumas y múltiplos son las correspondientes operaciones de las extensiones. Compacidad acota ambas capas y hace reales sus normas supremas. Su suma es no negativa. Si vale cero, la norma de valores ya obliga a que $u$ sea la función nula; la recíproca es inmediata. La linealidad de derivadas y la homogeneidad suprema dan $\|\alpha u\|_{C^1}=|\alpha|\|u\|_{C^1}$. Aplicar la triangular por separado a valores y derivadas y sumar da $\|u+v\|_{C^1}\le\|u\|_{C^1}+\|v\|_{C^1}$. Quedan verificadas las propiedades de norma sin suponer máximos alcanzados.

## 28.40. Inducción finita de órdenes

[]{#MA-EX-ANM-01-028-040}

[]{#MA-SOL-ANM-01-028-040}

Supongamos $r\ge1$, filas $C^r$ en el mismo segmento, convergencia uniforme de sus capas de orden $r$ y convergencia en un anclaje común de las capas de órdenes cero hasta $r-1$. Aplicamos R6 a las funciones de orden $r-1$, cuya derivada es la capa superior y cuyo dato inicial converge. Obtenemos un destino uniforme de ese orden y la identificación de su derivada con el destino de orden $r$. Repetimos para el orden $r-2$ usando la capa recién construida como derivada uniforme, y continuamos hasta los valores. Son sólo $r$ pasos. R1 conserva continuidad de los destinos extendidos al cerrado, y las cotas de incrementos identifican las derivadas relativas de borde. Se obtiene convergencia uniforme de todas las capas con sus relaciones de derivación. Para $r=0$ queda únicamente la convergencia uniforme de valores; no se utiliza Taylor ni una operación infinita para justificar el descenso.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html)
