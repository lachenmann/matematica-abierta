---
content-id: MA-BCH-0312
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-027-SOLUCIONES
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
title: Soluciones — Capítulo 27
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C27_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)

## 27.1. Banda sobre una función no acotada

[]{#MA-EX-ANM-01-027-001}

[]{#MA-SOL-ANM-01-027-001}

[]{#MA-SEC-ANM-01-027-001}

Fijada $\varepsilon>0$, elegimos un natural $N>1/\varepsilon$. Para todos $n\ge N$ y $x\in\mathbb R$, el error es1/(n+1)≤1/(N+1)<ε. El corte no depende de la entrada, así la convergencia es uniforme. Los valores de cada fila y del límite son no acotados en la recta, pero sus diferencias tienen magnitud constante1/(n+1). La cota relevante para el contrato es la del error.

**Retorno visual.** Véase [C27-F01](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.2. Negación con testigo móvil

[]{#MA-EX-ANM-01-027-002}

[]{#MA-SOL-ANM-01-027-002}

Usamos tolerancia $\varepsilon_0=1/2$. Dado cualquier corte $N$, tomamos $n=N$ y $x=N+1$. El error es1≥ε0. Se cumple la negación uniforme con entrada dependiente del corte. Para una entrada fija, en cambio, un natural mayor que |x|/ε controla toda la cola y prueba límite puntual cero. Los dos alcances son distintos.

## 27.3. Unicidad sin nueva selección

[]{#MA-EX-ANM-01-027-003}

[]{#MA-SOL-ANM-01-027-003}

Dos límites uniformes son también límites puntuales: cada corte simultáneo funciona en una entrada fija. Por unicidad numérica de C26, ambos valores coinciden en toda entrada; igualdad de funciones da un solo límite. Si el dominio es vacío, existe una única función vacía, así la conclusión también vale sin producir ninguna entrada. No se selecciona un punto de una colección vacía.

## 27.4. Toda la cola, no una fila

[]{#MA-EX-ANM-01-027-004}

[]{#MA-SOL-ANM-01-027-004}

Las filas pares son exactamente1, así esa subsucesión converge uniformemente a1. Las impares son exactamente−1. Si toda la familia tuviera límite uniforme, lo tendría puntual en cualquier entrada y las subsecuencias numéricas constantes compartirían ese destino, contradiciendo unicidad. Una fila favorable o infinitas filas favorables no controlan todas las filas de una cola.

## 27.5. Cambiar el prefijo

[]{#MA-EX-ANM-01-027-005}

[]{#MA-SOL-ANM-01-027-005}

Supongamos que la nueva familia coincide con la anterior para todo índice n≥M. Para una tolerancia, la familia original entrega un corte N independiente de la entrada. El corte máximo(N,M) controla todas las filas nuevas posteriores, pues coinciden con las antiguas y tienen error menor que ε en todas las entradas. Los valores del prefijo modificado no intervienen, aunque sean no acotados.

## 27.6. Supremo y frontera abierta

[]{#MA-EX-ANM-01-027-006}

[]{#MA-SOL-ANM-01-027-006}

[]{#MA-SEC-ANM-01-027-002}

El número1 acota la imagen. Si c<1, el punto y=(1+máx(c,0))/2 pertenece a(0,1) y es mayor que c, por lo que c no acota todos los errores. Así el supremo es1. Ningún punto lo alcanza porque todas las entradas son menores que1. El error estricto en cada punto sólo da supremo≤1; para obtener supremo<ε se requiere usar un margen como ε/2.

**Retorno visual.** Véase [C27-F02](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.7. Una fila sin envolvente real

[]{#MA-EX-ANM-01-027-007}

[]{#MA-SOL-ANM-01-027-007}

La candidata es cero. Para toda ε>0 sirve N=1, pues cada fila posterior coincide con ella, de modo que hay uniformidad. En la primera fila, dado B≥0, x=1/(B+1) pertenece al dominio y da errorB+1>B. No existe supremo real de ese conjunto de errores. Las envolventes existen desde el índice1 y valen0; la caracterización se formula sobre esa cola.

## 27.8. Acreditar el criterio

[]{#MA-EX-ANM-01-027-008}

[]{#MA-SOL-ANM-01-027-008}

Para ε>0, el límite numérico entrega un corte N dentro de la cola con E_n<ε para todos n≥N. Por definición de supremo, para cualquier entrada |f_n(x)−f(x)|≤E_n<ε. El mismo N sirve para todos x y todos los índices posteriores. En el vacío se usa la convención de error0 y el contrato es vacuo.

## 27.9. El margen al pasar al supremo

[]{#MA-EX-ANM-01-027-009}

[]{#MA-SOL-ANM-01-027-009}

Uniformidad con tolerancia1 da una cola de conjuntos de error no vacíos acotados cuando X no es vacío, por lo que C03 produce sus supremos. Para ε>0, recibimos un corte uniforme para ε/2 y lo reunimos con el de existencia. Cada supremo de esa cola es≤ε/2<ε. Esto prueba el límite0. No se cambia una desigualdad estricta punto a punto por una estricta del supremo sin el margen.

## 27.10. Regiones que nunca se vacían

[]{#MA-EX-ANM-01-027-010}

[]{#MA-SOL-ANM-01-027-010}

Con k=n+3, la condición es |kx−2|≤1/2, luego B_n(1/2)=[3/(2k),5/(2k)], no vacío para toda etapa y dentro de[0,1]. La entrada0 no pertenece a ninguno. Para x>0 fijo, desde k>3/x queda fuera del soporte y también de B_n. Así cada entrada sale eventualmente, pero ningún conjunto de infracción queda vacío. Esto distingue puntualidad de uniformidad.

## 27.11. Supremo sin máximo de las potencias

[]{#MA-EX-ANM-01-027-011}

[]{#MA-SOL-ANM-01-027-011}

[]{#MA-SEC-ANM-01-027-003}

En1 el error es0 y para x<1 es x^n<1, así1 es cota y no se alcanza. Dada cualquier cota propuesta0≤c<1, tomamos0<s<(1−c)/(n+1) y x=1−s. Bernoulli da x^n≥1−ns>c, así c falla. Cotas negativas fallan ante el error0. Por tanto E_n=1 sin máximo; no hay uniformidad.

## 27.12. Una restricción con máximo

[]{#MA-EX-ANM-01-027-012}

[]{#MA-SOL-ANM-01-027-012}

Para n≥1 y0≤x≤c se tiene x^n≤c^n, y la igualdad se alcanza en c. Así E_n=c^n. Poniendo t=1/c−1>0, Bernoulli produce c^n≤1/(1+nt). Un natural N>1/(εt), reunido con1, da E_n<ε en toda la cola. Para c=0 la familia tiene error0 desde la etapa1.

## 27.13. Un pico que sigue siendo grande

[]{#MA-EX-ANM-01-027-013}

[]{#MA-SOL-ANM-01-027-013}

Con k=n+3, las tiendas tienen cota1 y alcanzan1 en2/k, así E_n(t)=1. Las normalizadas tienen cota k y alcanzan k en el mismo centro, así E_n(b)=k. Para tolerancia1/2, en cualquier índice posterior al corte ese centro es infractor. Los centros están en el dominio. Ninguna envolvente tiende a cero aunque los límites puntuales sean cero.

## 27.14. Un máximo global decreciente

[]{#MA-EX-ANM-01-027-014}

[]{#MA-SOL-ANM-01-027-014}

Con k=n+1, el cuadrado(√k|x|−1)^2≥0 da1+kx²≥2√k|x|. Para x≠0, dividir por factores positivos implica |h_n(x)|≤1/(2√k), y en0 el error es0. En x=±1/√k se alcanza la cota, por lo que es el máximo exacto. Un natural N>1/(4ε²) hace ese máximo menor que ε en toda la cola. No se necesita acotar el dominio.

**Retorno visual.** Véase [C27-F03](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.15. La amplitud reduce el error

[]{#MA-EX-ANM-01-027-015}

[]{#MA-SOL-ANM-01-027-015}

En el dominio,0≤x^(n+1)≤1, así el error es≤1/(n+1). En x=1 se alcanza esa cota; es el máximo y la envolvente. Un natural N>1/ε da error menor que ε para todos n≥N y x del segmento. A diferencia de x^n, la amplitud1/(n+1) reduce también la peor discrepancia del extremo, no sólo las columnas interiores.

## 27.16. Restricción con barrera común

[]{#MA-EX-ANM-01-027-016}

[]{#MA-SOL-ANM-01-027-016}

[]{#MA-SEC-ANM-01-027-004}

El corte uniforme en X ya controla todas las entradas de Y, así funciona sin cambios. Para conjuntos no vacíos, la imagen de errores de Y es subconjunto de la de X; cada cota de la mayor acota la menor y C02 da E_n(Y)≤E_n(X). En una pieza vacía se adopta error0 y no hay obligaciones. No se deduce igualdad de envolventes.

## 27.17. Reunión de dos contratos

[]{#MA-EX-ANM-01-027-017}

[]{#MA-SOL-ANM-01-027-017}

Para ε>0, tomamos los cortes N_A y N_B y su máximo N. Si n≥N y x∈X, pertenece a A o B y el contrato de esa pieza entrega error<ε. Los cortes son independientes de la entrada. Si alguna pieza es vacía basta el corte de la otra. El argumento no necesita topología de las piezas, sólo una unión finita.

## 27.18. Una unión infinita falla

[]{#MA-EX-ANM-01-027-018}

[]{#MA-SOL-ANM-01-027-018}

La unión es[0,1): para cualquier x<1, la arquimedianidad permite1/(j+2)≤1−x. En cada pieza la envolvente de las potencias es c_j^n→0, así hay uniformidad hacia cero. En la unión el supremo del error es1 para todo n≥1, como en §27.3, y no hay uniformidad. Los cortes dependientes de j no tienen una barrera común que permita tomar un máximo infinito.

**Retorno visual.** Véase [C27-F04](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.19. Una ruta cualquiera

[]{#MA-EX-ANM-01-027-019}

[]{#MA-SOL-ANM-01-027-019}

Para una tolerancia, el contrato entrega un corte que controla toda entrada en toda fila posterior. En particular, controla la entrada x_n de la fila n. Por ello el error diagonal respecto del valor f(x_n) es menor que ε para n≥N. No se exige convergencia de x_n. Para cambiar el destino a f(x), se necesitarían además x_n→x y un dato como continuidad de f en x.

## 27.20. Subsucesión y prefijo

[]{#MA-EX-ANM-01-027-020}

[]{#MA-SOL-ANM-01-027-020}

Por inducción, índices naturales estrictamente crecientes n_j cumplen n_j≥j. El corte uniforme N de la familia completa sirve desde j≥N, pues n_j≥N y controla todas las entradas. La conversa falla para filas constantes(−1)^n: la subsucesión par es igual a1 en todo el dominio pero la completa alterna dos destinos distintos en cada entrada. Una cola completa tiene más obligaciones que una subsucesión.

## 27.21. Álgebra con dos presupuestos

[]{#MA-EX-ANM-01-027-021}

[]{#MA-SOL-ANM-01-027-021}

[]{#MA-SEC-ANM-01-027-005}

Para ε>0 pedimos los errores de f_n y g_n menores que ε/[2(|α|+1)] y ε/[2(|β|+1)], respectivamente. Sus cortes no dependen de la entrada; tomamos el máximo. En cualquier fila posterior y entrada, la triangular da error≤|α||f_n−f|+|β||g_n−g|<ε. Los denominadores positivos incluyen coeficientes cero sin dividir por ellos.

## 27.22. Producto con barreras declaradas

[]{#MA-EX-ANM-01-027-022}

[]{#MA-SOL-ANM-01-027-022}

El corte para |f_n−f|<1 produce |f_n|≤A+1 en toda entrada de la cola. Allí el error de producto es≤(A+1)|g_n−g|+B|f_n−f|. Pedimos los dos errores menores que ε/[2(A+2)] y ε/[2(B+1)] y reunimos ambos cortes con el de la barrera. La suma es<ε. Las constantes A,B son globales, por lo que el corte no depende de x.

## 27.23. Producto sin barrera

[]{#MA-EX-ANM-01-027-023}

[]{#MA-SOL-ANM-01-027-023}

Tomamos f_n(x)=x, con error0 hacia x, y g_n(x)=1/(n+1), con error independiente de x tendente a cero. El producto de límites es0 y el producto de filas es x/(n+1). Para cada N, la entrada x=N+1 en la fila n=N da error1; tolerancia1/2 refuta uniformidad. La barrera de f(x)=x falta en todo el dominio.

**Retorno visual.** Véase [C27-F05](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.24. Cuadrar una aproximación global

[]{#MA-EX-ANM-01-027-024}

[]{#MA-SOL-ANM-01-027-024}

La familia original converge uniformemente a x. El error de los cuadrados es |2x/(n+1)+1/(n+1)^2|, no acotado para ningún n, así no hay uniformidad hacia x². Para una refutación explícita basta x=n+1: el error es2+1/(n+1)²>1. Si todos los valores de filas y límite estuvieran en[−M,M], el cuadrado tendría cota Lipschitz2M por |u²−v²|=|u−v||u+v|, que sí transportaría el contrato.

## 27.25. Recíproco con margen

[]{#MA-EX-ANM-01-027-025}

[]{#MA-SOL-ANM-01-027-025}

Un corte uniforme para error<m/2 da |g_n(x)|>m/2 en todas las entradas de la cola. Así esa cola de recíprocos está definida en X. El error es |g_n−g|/(|g_n||g|)≤2|g_n−g|/m². Un corte para error de g_n menor que εm²/2, reunido con el de dominio, hace el error recíproco<ε. Las primeras filas pueden tener ceros; para una familia desde cero deben revisarse o repararse explícitamente.

## 27.26. Norma y salida cero

[]{#MA-EX-ANM-01-027-026}

[]{#MA-SOL-ANM-01-027-026}

[]{#MA-SEC-ANM-01-027-006}

Para X no vacío, cada |u(x)| está entre0 y su supremo. Si el supremo es0, todos los valores son0, así u es la función cero. Si u es cero, la imagen de magnitudes es{0} y tiene supremo0. Para el vacío se declaró norma0; la única función es la función cero vacía, por lo que la equivalencia también vale sin fingir un supremo del conjunto vacío.

## 27.27. Homogeneidad sin máximos

[]{#MA-EX-ANM-01-027-027}

[]{#MA-SOL-ANM-01-027-027}

Para α≠0, el número |α|‖u‖∞ acota todas las magnitudes de αu. Si C es cualquier cota de éstas, C/|α| acota las magnitudes de u; la minimalidad del supremo da |α|‖u‖∞≤C. Por tanto ese número es el supremo buscado. Para α=0 se verifican directamente ambos lados0. En el dominio vacío ambas normas fueron definidas0 y la igualdad es inmediata.

## 27.28. Distancia triangular

[]{#MA-EX-ANM-01-027-028}

[]{#MA-SOL-ANM-01-027-028}

Para cualquier entrada, |u(x)−w(x)|≤|u(x)−v(x)|+|v(x)−w(x)|≤d∞(u,v)+d∞(v,w). El miembro derecho es una cota superior real de todas las diferencias u−w. Tomando su supremo obtenemos d∞(u,w)≤d∞(u,v)+d∞(v,w). Las tres diferencias están acotadas porque las funciones lo están. En el vacío todas las distancias son0.

## 27.29. Banda y bola de frontera estricta

[]{#MA-EX-ANM-01-027-029}

[]{#MA-SOL-ANM-01-027-029}

Para todas las entradas, |u(x)|=x<1, así la gráfica queda en la banda abierta de radio1 alrededor de cero. Pero d∞(u,0)=sup(0,1)=1, y u no pertenece a la bola estricta de radio1. No hay contradicción: pertenencia punto a punto a una banda abierta permite supremo en la frontera. Al usar radios menores en un contrato de convergencia, esa diferencia se resuelve con ε/2.

**Retorno visual.** Véase [C27-F06](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.30. Clase trasladada

[]{#MA-EX-ANM-01-027-030}

[]{#MA-SOL-ANM-01-027-030}

La magnitud |x| no tiene cota real en toda la recta, de modo que no hay supremo real para la diferencia entre x y0. En cambio,(x+u)−(x+v)=u−v es acotada por la suma de barreras de u y v. Su supremo real existe por C03 y define una distancia en la clase x+$\mathcal B(\mathbb R)$. La parte no acotada común se cancela; no se extiende la distancia real a pares arbitrarios de funciones.

## 27.31. De destino a pares

[]{#MA-EX-ANM-01-027-031}

[]{#MA-SOL-ANM-01-027-031}

[]{#MA-SEC-ANM-01-027-007}

Para $\varepsilon>0$ recibimos un corte uniforme para $\varepsilon/3$. Si $m,n\ge N$ y $x\in X$, la triangular da

$$|f_n(x)-f_m(x)|\le |f_n(x)-f(x)|+|f(x)-f_m(x)|<2\varepsilon/3<\varepsilon.$$

El mismo corte controla los dos índices y toda entrada. Esta dirección sólo usa el destino ya dado y la triangular; no necesita completitud.

## 27.32. Construir primero el límite

[]{#MA-EX-ANM-01-027-032}

[]{#MA-SOL-ANM-01-027-032}

Cada columna es de Cauchy real, así C10 da un límite único y C26 reúne los límites en una función f. Para ε>0 elegimos un corte común de Cauchy con ε/3. Fijados n≥N y x, todos m≥N satisfacen |f_n(x)−f_m(x)|<ε/3. Al llevar m al límite, álgebra y orden dan |f_n(x)−f(x)|≤ε/3<ε. El corte se eligió antes de n y x, así controla toda la función. La desigualdad tras el límite es≤, no≥.

## 27.33. Conservar el destino en funciones acotadas

[]{#MA-EX-ANM-01-027-033}

[]{#MA-SOL-ANM-01-027-033}

Una sucesión de Cauchy en d∞ cumple el contrato uniforme de Cauchy y tiene límite uniforme real f por el criterio. Con tolerancia1 tomamos una fila de referencia f_N; pasar m al límite en |f_m(x)−f_N(x)|<1 da |f(x)|≤‖f_N‖∞+1 para toda entrada. Así f pertenece a$\mathcal B(X)$. El criterio de envolventes identifica la convergencia uniforme con d∞(f_n,f)→0. La existencia numérica usa C10; la barrera común conserva el espacio.

## 27.34. Vecinos cada vez más próximos

[]{#MA-EX-ANM-01-027-034}

[]{#MA-SOL-ANM-01-027-034}

En un dominio no vacío, d∞(H_(n+1),H_n)=1/(n+1)→0. Pero para m≥1, H_(2m)−H_m suma m términos, cada uno≥1/(2m), así la diferencia es≥1/2. Ante un corte N elegimos m≥máx(N,1); ambos índices son posteriores y cualquier entrada muestra separación≥1/2. Tolerancia1/2 refuta Cauchy uniforme. El contrato controla todos los pares tardíos, no sólo vecinos.

**Retorno visual.** Véase [C27-F07](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.35. La completitud tiene un lugar

[]{#MA-EX-ANM-01-027-035}

[]{#MA-SOL-ANM-01-027-035}

Convergencia uniforme⇒Cauchy usa únicamente triangular y un corte común. En la vuelta, C10 usa completitud de ℝ para obtener el destino de cada columna; unicidad construye el grafo. Una vez existente la función límite, el paso de m→∞ conserva la cota no estricta por orden, y el margen ε/3 entrega el contrato uniforme. La permanencia en$\mathcal B(X)$ usa una fila acotada de referencia. No se supone compacidad ni continuidad de las filas.

## 27.36. Presupuesto geométrico finito

[]{#MA-EX-ANM-01-027-036}

[]{#MA-SOL-ANM-01-027-036}

[]{#MA-SEC-ANM-01-027-008}

Para $n>m$, telescopar y sumar una cantidad finita de errores da, para toda entrada,

$$|f_n(x)-f_m(x)|\le C\sum_{j=m}^{n-1}q^j=Cq^m\frac{1-q^{n-m}}{1-q}\le\frac{Cq^m}{1-q}.$$

Intercambiamos índices si $m>n$; si coinciden, el error es cero. Como $q^m\to0$, hay un corte común para todos los pares, y el criterio produce $f$. Fijando $m$ y pasando $n$ al límite, obtenemos $|f(x)-f_m(x)|\le Cq^m/(1-q)$ en todo $X$.

## 27.37. Destino acotado o diferencia acotada

[]{#MA-EX-ANM-01-027-037}

[]{#MA-SOL-ANM-01-027-037}

Telescopar desde0 da |f_n(x)−f_0(x)|≤C/(1−q). Al pasar al límite se conserva la misma barrera para f−f_0. Si f_0 está acotada, entonces |f_n| y |f| están acotados por ‖f_0‖∞+C/(1−q), y todos viven en$\mathcal B(X)$. Si f_0 no está acotada, sólo se garantiza pertenencia a f_0+$\mathcal B(X)$. No se concluye acotación de f sin esa premisa.

## 27.38. Un presupuesto que se alcanza

[]{#MA-EX-ANM-01-027-038}

[]{#MA-SOL-ANM-01-027-038}

El incremento es2^(−n−1)a, de magnitud≤(1/2)(1/2)^n. El presupuesto geométrico sirve con C=1/2,q=1/2 y da cota2^(−n). Directamente f_n−(r+a)=−2^(−n)a, cuya magnitud es≤2^(−n); por ello el límite uniforme es r+a. Si |a| alcanza1, la cota es el máximo exacto. Si sólo tiene supremo1, es la envolvente exacta sin exigir máximo. La base r puede ser no acotada.

**Retorno visual.** Véase [C27-F08](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.39. Monotonía con límite continuo

[]{#MA-EX-ANM-01-027-039}

[]{#MA-SOL-ANM-01-027-039}

Los intervalos positivos se encogen, así s_(n+1)≤s_n entrada por entrada. En0 todas las filas valen0. Para x>0 fijo, desde n+1>1/x queda fuera y la columna vale0. El límite puntual es cero, continuo. Sin embargo x_n=1/[2(n+1)] pertenece al intervalo positivo y da error1 en toda etapa; no hay uniformidad. Las filas son discontinuas, por lo que no se puede usar un resultado que requiera continuidad de ellas omitiendo esa hipótesis.

## 27.40. Una auditoría de condiciones

[]{#MA-EX-ANM-01-027-040}

[]{#MA-SOL-ANM-01-027-040}

Uniformidad requiere un corte por tolerancia que controle todas las entradas y todas las filas posteriores; una barrera universal tendente a cero basta. La distancia suprema real requiere diferencias acotadas en la clase utilizada, con convención explícita para el vacío; no vale sobre todas las funciones arbitrarias. Para una ruta dada, uniformidad controla f_n(x_n)−f(x_n). Si x_n→x y f es continua en x, C14 y la triangular permiten compararla con f(x). La continuidad del límite no se deduce aquí sin prueba: su preservación se trata en C28.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)
