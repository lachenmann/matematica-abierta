---
content-id: MA-BCH-0227
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-006-EJERCICIOS
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
title: Ejercicios — Capítulo 6
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C06_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 6](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) · [Ejercicios](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-soluciones.html)

Se conserva $\mathbb N=\{0,1,2,\ldots\}$. Cada ejercicio utiliza las herramientas disponibles hasta la sección a la que pertenece. Justifica las afirmaciones y declara los dominios cuando se construyan objetos nuevos.

## §6.1

### 1. Ventanas con lados distintos

[]{#MA-EX-ANM-01-006-001}

[]{#MA-SOL-ANM-01-006-001}

[]{#MA-SEC-ANM-01-006-001}

Fija una sucesión $a:\mathbb N\to\mathbb R$ y $A\in\mathbb R$. Compara la afirmación $a_n\to A$ con la siguiente: para cada $r,s>0$ existe $N\in\mathbb N$ tal que $A-r<a_n<A+s$ para todo $n\ge N$. Demuestra la equivalencia e identifica qué datos se fijan y cuáles se eligen.

### 2. Lo que un prefijo no decide

[]{#MA-EX-ANM-01-006-002}

[]{#MA-SOL-ANM-01-006-002}

Dados $m\in\mathbb N$ y $x_0,\ldots,x_m\in\mathbb R$, construye dos sucesiones que coincidan con esos datos: una que converja a 0 y otra que no converja a 0. Justifica ambas afirmaciones sin inferir propiedades de una cola a partir de una muestra. Explica qué comparten sus gráficas para $0\le n\le m$.

### 3. Una familia con destino común

[]{#MA-EX-ANM-01-006-003}

[]{#MA-SOL-ANM-01-006-003}

Fija $T\in\mathbb N$ y $A\in\mathbb R$. Para cada familia de reales $x=(x_0,\ldots,x_{T-1})$, define $a^x_n=x_n$ si $n<T$ y $a^x_n=A$ si $n\ge T$. Describe el caso $T=0$, demuestra directamente la convergencia a $A$ y determina cuándo $a^x=a^y$ como funciones. ¿La igualdad del candidato obliga a esa igualdad de funciones?

### 4. Qué familia de ventanas basta

[]{#MA-EX-ANM-01-006-004}

[]{#MA-SOL-ANM-01-006-004}

Demuestra que $a_n\to A$ equivale a que todo intervalo abierto $(u,v)$ con $u<A<v$ capture una cola. Compara esta condición con la captura por cada vecindad de $A$, entendiendo vecindad en el sentido de C04.

## §6.2

### 5. Un candidato elegido demasiado tarde

[]{#MA-EX-ANM-01-006-005}

[]{#MA-SOL-ANM-01-006-005}

[]{#MA-SEC-ANM-01-006-002}

Alguien escribe: «Para cada $\varepsilon>0$ puedo elegir $A_\varepsilon\in\mathbb R$ y $N_\varepsilon\in\mathbb N$ que satisfacen $|a_n-A_\varepsilon|<\varepsilon$ para todos los índices $n\ge N_\varepsilon$. Por tanto, $a_n\to0$». Localiza la falta en esa conclusión y refútala con una sucesión concreta. ¿Cuál sería la obligación correcta para acreditar el candidato 0? No se pide decidir si la premisa implica alguna otra propiedad.

### 6. Negar la existencia de un destino

[]{#MA-EX-ANM-01-006-006}

[]{#MA-SOL-ANM-01-006-006}

Escribe con todos sus dominios la afirmación «$a$ no converge a ningún número real» y deriva su forma cuantificada desde la negación de «existe $A\in\mathbb R$ al que converge». Compara el orden de elecciones con la refutación de un candidato fijo.

### 7. Visitar sin permanecer

[]{#MA-EX-ANM-01-006-007}

[]{#MA-SOL-ANM-01-006-007}

Construye una sucesión real que tome el valor 0 en índices arbitrariamente tardíos y que también tome valores de módulo al menos 2 arbitrariamente tarde, sin ser una sucesión de sólo dos valores. Verifica que visita toda bola alrededor de 0 después de cada corte y que no converge a 0.

### 8. Cambiar la frontera del error

[]{#MA-EX-ANM-01-006-008}

[]{#MA-SOL-ANM-01-006-008}

Compara la definición usual de $a_n\to A$ con la condición que exige $|a_n-A|\le\varepsilon$ eventualmente para cada $\varepsilon>0$. Demuestra su equivalencia y deriva la negación de la segunda condición. Explica por qué las distintas desigualdades en las negaciones no cambian su alcance global.

### 9. Sólo tolerancias pequeñas

[]{#MA-EX-ANM-01-006-009}

[]{#MA-SOL-ANM-01-006-009}

Sea $r>0$ fijo. Demuestra que basta verificar la captura con error estricto para todas las tolerancias $\delta$ tales que $0<\delta<r$ para acreditar $a_n\to A$. ¿Basta verificar únicamente la tolerancia $r$? Justifica la respuesta.

## §6.3

### 10. Centro, escala y denominador

[]{#MA-EX-ANM-01-006-010}

[]{#MA-SOL-ANM-01-006-010}

[]{#MA-SEC-ANM-01-006-003}

Fija $A,c\in\mathbb R$ y $d,e>0$. Para $a_n=A+c/(dn+e)$, demuestra directamente que $a_n\to A$. Da un umbral explícito para cada $\varepsilon>0$, trata $c=0$ y verifica que la sucesión está definida también en $n=0$.

### 11. Dos cortes defectuosos

[]{#MA-EX-ANM-01-006-011}

[]{#MA-SOL-ANM-01-006-011}

Para la familia del ejercicio 10 con $c\ne0$, se proponen $N_1=\max\{0,\lfloor(|c|/\varepsilon-e)/d\rfloor\}$ y $N_2=\lfloor|c|/(d\varepsilon)\rfloor-1$. Refuta cada propuesta como fórmula válida para todos los parámetros: muestra una falla de estrictitud de $N_1$ y una falla de dominio de $N_2$. Repara ambas con un testigo universal suficiente.

### 12. Un prefijo arbitrario

[]{#MA-EX-ANM-01-006-012}

[]{#MA-SOL-ANM-01-006-012}

Sea $T\in\mathbb N$. Define $a_n=x_n$ para $n<T$, con valores reales arbitrarios, y $a_n=A+c/(dn+e)$ para $n\ge T$, donde $A,c\in\mathbb R$ y $d,e>0$. Prueba $a_n\to A$ desde la definición, sin usar aún invariancia por modificaciones finitas. Cubre el prefijo vacío.

### 13. Un corte suficiente y el menor corte

[]{#MA-EX-ANM-01-006-013}

[]{#MA-SOL-ANM-01-006-013}

Considera $a_n=2/(n+3)$ y candidato 0. Para cada $\varepsilon>0$, determina el menor umbral natural que da error estricto en toda la cola. Compáralo con $K=\lfloor2/\varepsilon\rfloor+1$. Examina $\varepsilon=2/5$ y $\varepsilon=1$, e identifica el papel de la frontera.

### 14. Dos valores que no desaparecen

[]{#MA-EX-ANM-01-006-014}

[]{#MA-SOL-ANM-01-006-014}

Sean $p,q\in\mathbb R$, $p\ne q$, y una sucesión $a$. Supón que existen fórmulas $i,j:\mathbb N\to\mathbb N$ tales que $i(N),j(N)\ge N$, $a_{i(N)}=p$ y $a_{j(N)}=q$ para cada $N$. Demuestra que $a$ no converge a ningún real. Construye además un ejemplo con $p=-2$, $q=4$ y valores adicionales en otros índices.

## §6.4

### 15. Cómo repartir una separación

[]{#MA-EX-ANM-01-006-015}

[]{#MA-SOL-ANM-01-006-015}

[]{#MA-SEC-ANM-01-006-004}

En una prueba de unicidad con candidatos distintos $A,B$, escribe $D=|A-B|$. Se desean tolerancias $\alpha D$ y $\beta D$, con $\alpha,\beta>0$. Determina cuándo la triangular y las dos capturas bastan por sí solas para dar contradicción. Explica qué ocurre cuando $\alpha+\beta>1$.

### 16. Transportar índices y cortes

[]{#MA-EX-ANM-01-006-016}

[]{#MA-SOL-ANM-01-006-016}

Fija $T\in\mathbb N$, una sucesión $a$ y $A\in\mathbb R$. Compara $r=a|_{\mathbb N_{\ge T}}$ con $b_k=a_{T+k}$. Declara dominios y codominios y escribe el transporte $k\mapsto T+k$ y su inversa. Para una tolerancia, transforma un umbral de $a$ en uno de $b$, y un umbral de $b$ en uno de $a$, justificando las dos capturas.

### 17. Tres funciones y un destino

[]{#MA-EX-ANM-01-006-017}

[]{#MA-SOL-ANM-01-006-017}

Construye tres sucesiones reales distintas que converjan a 0, de modo que las dos primeras coincidan eventualmente y la tercera difiera de ambas en todos los índices suficientemente grandes. Justifica la convergencia y explica qué igualdades se conservan y cuáles no.

### 18. Alguna cola y todas las colas

[]{#MA-EX-ANM-01-006-018}

[]{#MA-SOL-ANM-01-006-018}

Para $a:\mathbb N\to\mathbb R$ y $A\in\mathbb R$, prueba la equivalencia de: $a_n\to A$; existe $T\in\mathbb N$ tal que $a_{T+k}\to A$ al recorrer $k\in\mathbb N$; para cada $T\in\mathbb N$ esa cola reindexada converge a $A$. Distingue el candidato común de los cortes, que pueden variar.

## §6.5

### 19. Acotar con otra tolerancia

[]{#MA-EX-ANM-01-006-019}

[]{#MA-SOL-ANM-01-006-019}

[]{#MA-SEC-ANM-01-006-005}

Supón $a_n\to A$. Para $r>0$, sea $N_r$ un umbral con error menor que $r$. Construye una cota global usando esa cola y el prefijo, incluido $N_r=0$. Para $a_0=20$, $a_n=0$ si $n\ge1$, compara las cotas obtenidas con $r=1,N_r=1$ y con $r=30,N_r=0$. ¿Se minimiza necesariamente la cota eligiendo una tolerancia mayor?

### 20. Qué decide el módulo

[]{#MA-EX-ANM-01-006-020}

[]{#MA-SOL-ANM-01-006-020}

Construye una sucesión $a$ cuyo módulo converja a un número positivo pero que no converja a ningún real. Demuestra, por contraste, que $|b_n|\to0$ sí obliga a $b_n\to0$. Da un ejemplo de esta segunda situación con signos alternantes.

### 21. Un coeficiente variable controlado

[]{#MA-EX-ANM-01-006-021}

[]{#MA-SOL-ANM-01-006-021}

Sean $u_n\to0$, $v:\mathbb N\to\mathbb R$ y $C:\mathbb N\to\mathbb R$. Supón que $|v_n|\le C_n|u_n|$ desde $T$ y que $0\le C_n\le M$ desde $S$, con $M\ge0$ fijo. Demuestra $v_n\to0$ y separa $M=0$ de $M>0$. Explica qué sustituye a la constancia del coeficiente.

### 22. Una comparación intermitente

[]{#MA-EX-ANM-01-006-022}

[]{#MA-SOL-ANM-01-006-022}

Examina este argumento: «$u_n\to0$ y, después de cada corte, hay un índice con $|v_n|\le3|u_n|$; luego $v_n\to0$». Construye un contraejemplo y localiza el cuantificador que falta. Formula una reparación suficiente y demuéstrala.

### 23. Compartir destino por un error pequeño

[]{#MA-EX-ANM-01-006-023}

[]{#MA-SOL-ANM-01-006-023}

Supón $a_n-b_n\to0$. Demuestra que $a_n\to A$ si y sólo si $b_n\to A$, para un candidato real fijo $A$. Usa la definición y la triangular; no invoques la regla posterior de suma de límites.

## §6.6

### 24. Un reparto a medida

[]{#MA-EX-ANM-01-006-024}

[]{#MA-SOL-ANM-01-006-024}

[]{#MA-SEC-ANM-01-006-006}

Sean $a_n\to A$, $b_n\to B$, $c,d\in\mathbb R$ y $0<\theta<1$. Construye una prueba de $ca_n+db_n\to cA+dB$ que reserve $\theta\varepsilon$ al primer error y $(1-\theta)\varepsilon$ al segundo. Trata los coeficientes nulos y da un ejemplo de reparto no simétrico.

### 25. Una cantidad finita de operaciones

[]{#MA-EX-ANM-01-006-025}

[]{#MA-SOL-ANM-01-006-025}

Para $m\ge1$, sean $a^{(1)},\ldots,a^{(m)}$ sucesiones con $a^{(j)}_n\to A_j$. Demuestra que la suma de sus términos converge a $\sum_{j=1}^m A_j$ y que su producto converge a $\prod_{j=1}^m A_j$. Usa inducción y las reglas binarias demostradas. Describe también el caso de familia vacía con las convenciones usuales.

### 26. Leer un producto al revés

[]{#MA-EX-ANM-01-006-026}

[]{#MA-SOL-ANM-01-006-026}

Se afirma: «Si $a_nb_n$ converge, ambos factores convergen». Refuta la afirmación con un producto idénticamente cero y con un producto idénticamente no nulo. En el segundo caso comprueba que ninguno de los factores tiene límite real.

### 27. Un factor pequeño y otro acotado

[]{#MA-EX-ANM-01-006-027}

[]{#MA-SOL-ANM-01-006-027}

Supón $u_n\to0$ y $|p_n|\le M$ desde $T$, con $M\ge0$ fijo. Prueba $u_np_n\to0$ sin suponer convergencia de $p$. Da un ejemplo en que esa última convergencia falle.

### 28. El inverso como conjunto de obligaciones

[]{#MA-EX-ANM-01-006-028}

[]{#MA-SOL-ANM-01-006-028}

Supón $b_n\to B\ne0$ y $|b_n|>|B|/2$ desde $T$. Para cualquier prefijo real $x_0,\ldots,x_{T-1}$, define $c^x_n=x_n$ si $n<T$ y $c^x_n=1/b_n$ si $n\ge T$. Organiza la prueba de $c^x_n\to1/B$ en cuatro obligaciones: margen, definición, estimación y transferencia. Compara dos prefijos distintos.

### 29. Un denominador negativo con ceros

[]{#MA-EX-ANM-01-006-029}

[]{#MA-SOL-ANM-01-006-029}

Construye una sucesión $b$ con $b_0=b_1=0$, límite −2 y términos no nulos desde 2. Toma $a_n=3+1/(n+1)$. Define dos sucesiones distintas que extiendan el cociente $a_n/b_n$ desde 2 y demuestra que ambas convergen a −3/2. Comprueba un margen explícito para el denominador.

### 30. Tres cálculos que necesitan una auditoría

[]{#MA-EX-ANM-01-006-030}

[]{#MA-SOL-ANM-01-006-030}

Examina las propuestas siguientes: (i) $(3n+2)/(2n+5)$ tiene límite «$\lim(3n+2)/\lim(2n+5)$»; (ii) con $h_n=1/(n+1)$, $h_n/h_n$ tiene límite «0/0»; (iii) $(-1)^n/h_n$ tiene límite «un número dividido por 0». Localiza los usos ilegítimos, resuelve los casos (i) y (ii) mediante identidades válidas y decide si (iii) tiene algún límite real sin usar límites infinitos.

### 31. Construir un cociente y revisar su margen

[]{#MA-EX-ANM-01-006-031}

[]{#MA-SOL-ANM-01-006-031}

Sean $a_n\to A$ y $b_n\to B$. Determina cuándo puedes proponer coeficientes reales $r,s,t,u$ para los que $D=tA+uB\ne0$ y estudia la expresión $(ra_n+sb_n)/(ta_n+ub_n)$. Justifica un margen eventual, define un cociente real en todo $\mathbb N$ aunque haya ceros iniciales y determina su límite. Da dos ejemplos con $D=0$ que impidan asignar una conclusión única por esa fórmula.

## §6.7

### 32. Llegar a la frontera de un intervalo

[]{#MA-EX-ANM-01-006-032}

[]{#MA-SOL-ANM-01-006-032}

[]{#MA-SEC-ANM-01-006-007}

Sean $p<q$ reales, $a_n\to A$ y $p\le a_n\le q$ eventualmente. Prueba $A\in[p,q]$. Decide si la conclusión puede sustituirse por $A\in(p,q)$ cuando todos los términos tardíos están en ese intervalo abierto. Construye un ejemplo que llegue a cada frontera.

### 33. Orden estricto y margen uniforme

[]{#MA-EX-ANM-01-006-033}

[]{#MA-SOL-ANM-01-006-033}

Construye $a,b$ con $a_n<b_n$ en todos los índices y límite común 2. Construye también $c,d$ con límites distintos y $c_n+\delta\le d_n$ para alguna constante $\delta>0$. Demuestra en general que ese margen, junto con la convergencia de ambos factores, obliga a que el primer límite sea estrictamente menor que el segundo.

### 34. Dos presupuestos de error exteriores

[]{#MA-EX-ANM-01-006-034}

[]{#MA-SOL-ANM-01-006-034}

Sean $r_n,s_n\ge0$ con $r_n\to0$, $s_n\to0$, y supón $L-r_n\le a_n$ desde $T_1$ y $a_n\le L+s_n$ desde $T_2$. Demuestra directamente $a_n\to L$ sin presuponer su convergencia ni exigir que las dos cotas de error coincidan.

### 35. Una frontera conocida sólo por su módulo

[]{#MA-EX-ANM-01-006-035}

[]{#MA-SOL-ANM-01-006-035}

Se propone: «$u_n\le a_n\le v_n$ eventualmente, $|u_n|\to1$ y $v_n\to1$; por el sándwich, $a_n\to1$». Refuta la propuesta con un ejemplo en que $u$ no tenga límite real. Formula una reparación sobre la frontera inferior y justifica el resultado.

### 36. Una caracterización por fronteras

[]{#MA-EX-ANM-01-006-036}

[]{#MA-SOL-ANM-01-006-036}

Prueba que $a_n\to L$ equivale a la existencia de sucesiones $u,v$ tales que $u_n\le a_n\le v_n$ eventualmente y $u_n,v_n\to L$. En la dirección que construye fronteras desde $a$, procura que éstas tengan fórmulas distintas y justifica la captura sin importar resultados posteriores.

## §6.8

### 37. Dos recorridos para una expresión racional

[]{#MA-EX-ANM-01-006-037}

[]{#MA-SOL-ANM-01-006-037}

[]{#MA-SEC-ANM-01-006-008}

Para $f_n=(5n+2)/(2n+3)$, demuestra su convergencia por una estimación directa del error y por normalización con $h_n=1/(n+1)$. Determina el candidato, construye un testigo suficiente y revisa los denominadores en todo $\mathbb N$.

### 38. Una perturbación que conserva el destino

[]{#MA-EX-ANM-01-006-038}

[]{#MA-SOL-ANM-01-006-038}

Sea $a_n\to A$. Diseña una sucesión $p$ sin límite real pero eventualmente acotada, y una sucesión $b$ con prefijo arbitrario que desde un corte $T$ satisfaga $b_n=a_n+p_n/(n+1)$. Demuestra $b_n\to A$ e identifica qué partes del argumento no necesitan un límite de $p$.

### 39. Qué puede recuperarse de las operaciones

[]{#MA-EX-ANM-01-006-039}

[]{#MA-SOL-ANM-01-006-039}

Para sucesiones reales $a,b$, estudia estas afirmaciones, con cocientes globalmente definidos cuando se mencionan: (i) si $a_n+b_n\to S$ y $a_n\to A$, entonces $b_n\to S-A$; (ii) si $a_nb_n\to P$ y $a_n\to A\ne0$, entonces $b_n\to P/A$; (iii) si $a_n/b_n\to Q$ y $b_n\to B$, entonces $a_n\to QB$, incluso si $B=0$; (iv) la convergencia simultánea de la suma y el producto obliga a converger a ambos factores; (v) en (ii) basta $A=0$. Justifica las inferencias o construye contraejemplos.

### 40. Cambiar todo el orden de los índices

[]{#MA-EX-ANM-01-006-040}

[]{#MA-SOL-ANM-01-006-040}

Sea $\pi:\mathbb N\to\mathbb N$ una biyección y $b_n=a_{\pi(n)}$. Demuestra que $a_n\to A$ si y sólo si $b_n\to A$, sin suponer que la permutación conserve el orden ni que $a,b$ coincidan eventualmente. Construye el corte usando la preimagen de un prefijo finito, trata el caso vacío y demuestra la dirección inversa.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 6](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) · [Ejercicios](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-soluciones.html)
