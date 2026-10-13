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
date-modified: '2026-10-12'
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

La diferencia entre $f_n(x)=x+1/(n+1)$ y la candidata $f(x)=x$ es $1/(n+1)$ para todas las entradas de la recta. Dada $\varepsilon>0$, elegimos un natural $N>1/\varepsilon$. Para todo $n\ge N$ y todo $x\in\mathbb R$, $|f_n(x)-f(x)|=1/(n+1)\le1/(N+1)<\varepsilon$. El corte se eligió antes de examinar la entrada, así la convergencia es uniforme. Ninguna de esas funciones es acotada en la recta. Sus diferencias sí son funciones constantes acotadas, que es el control utilizado por el contrato.

**Retorno visual.** Véase [C27-F01](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.2. Negación con testigo móvil

[]{#MA-EX-ANM-01-027-002}

[]{#MA-SOL-ANM-01-027-002}

Cada entrada fija tiene $|g_n(x)|=|x|/(n+1)\to0$, con un corte $N>|x|/\varepsilon$, así hay convergencia puntual a cero. Para refutar uniformidad, fijamos $\varepsilon_0=1/2$. Ante cualquier corte $N$, elegimos $n=N$ y $x=N+1$. El error es entonces $|g_N(x)|=1\ge\varepsilon_0$. Se obtiene una infracción en cada cola con una entrada que puede depender del corte. Ésta es la negación uniforme y es compatible con el control de cada columna fija.

## 27.3. Unicidad sin nueva selección

[]{#MA-EX-ANM-01-027-003}

[]{#MA-SOL-ANM-01-027-003}

Si $f$ y $g$ son límites uniformes, también son límites puntuales, porque cada corte simultáneo sirve para una entrada fijada. Para $x\in X$, si $d=|f(x)-g(x)|>0$, los cortes de ambos contratos con error $d/3$ tienen un máximo $N$. En ese índice, $d\le|f(x)-f_N(x)|+|f_N(x)-g(x)|<2d/3$, contradicción. Así coinciden en cada entrada y son la misma función. Si $X$ es vacío, hay una única función vacía y la conclusión vale directamente, sin elegir una entrada inexistente.

## 27.4. Toda la cola, no una fila

[]{#MA-EX-ANM-01-027-004}

[]{#MA-SOL-ANM-01-027-004}

Las filas de índice par son la función constante uno, así esa subsucesión converge uniformemente a uno con error cero. Las de índice impar son la función constante menos uno. Si toda la familia convergiera uniformemente, sería puntualmente convergente en cualquier entrada del dominio no vacío. Sus dos subsucesiones numéricas constantes deberían compartir el mismo límite, pero sus valores son distintos. Por tanto no hay límite uniforme de la familia completa. Un número infinito de filas favorables no asegura que todas las etapas posteriores al corte sean favorables.

## 27.5. Cambiar el prefijo

[]{#MA-EX-ANM-01-027-005}

[]{#MA-SOL-ANM-01-027-005}

Sean $f_n\to f$ uniformemente y $g_n=f_n$ para todo $n\ge M$. Ante $\varepsilon>0$, el contrato original proporciona un corte $N$ independiente de la entrada. Tomamos $K=\max(N,M)$. Para $n\ge K$ y toda entrada, $|g_n(x)-f(x)|=|f_n(x)-f(x)|<\varepsilon$. Así la familia modificada tiene el mismo límite uniforme. Las filas del prefijo pueden cambiar de modo arbitrario, incluso perder acotación, siempre que sigan siendo funciones sobre el dominio común declarado.

## 27.6. Supremo y frontera abierta

[]{#MA-EX-ANM-01-027-006}

[]{#MA-SOL-ANM-01-027-006}

[]{#MA-SEC-ANM-01-027-002}

En $(0,1)$, todas las alturas $e(x)=x$ satisfacen $e(x)<1$, así uno es cota superior. Si $c<1$, ponemos $y=(1+\max(c,0))/2$. Esta entrada pertenece a $(0,1)$ y cumple $y>c$, de modo que $c$ no es cota superior. Por tanto $\sup e(X)=1$. Como uno no pertenece al dominio, ningún valor alcanza ese supremo. La conclusión muestra que desigualdades estrictas en todas las entradas pueden producir sólo una desigualdad no estricta al tomar supremo.

**Retorno visual.** Véase [C27-F02](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.7. Una fila sin envolvente real

[]{#MA-EX-ANM-01-027-007}

[]{#MA-SOL-ANM-01-027-007}

La candidata es cero. Para cualquier tolerancia sirve $N=1$, pues todas las filas posteriores son idénticamente cero en $(0,1]$. Hay por tanto convergencia uniforme. En la primera fila, dado $B\ge0$, la entrada $x=1/(B+1)$ pertenece al dominio y tiene error $B+1>B$. Esa imagen de errores es no acotada y no tiene supremo real. Desde el índice uno las envolventes existen y valen cero. La caracterización de uniformidad utiliza envolventes reales de una cola y no exige que el prefijo también las posea.

## 27.8. Acreditar el criterio

[]{#MA-EX-ANM-01-027-008}

[]{#MA-SOL-ANM-01-027-008}

Supongamos que desde un índice $M$ existen envolventes reales $E_n$ y que $E_n\to0$. Para $\varepsilon>0$, el límite numérico da un corte $N\ge M$ con $E_n<\varepsilon$ para todo $n\ge N$. Como el supremo acota cada error, para toda entrada $|f_n(x)-f(x)|\le E_n<\varepsilon$. El mismo corte controla todas las entradas y toda la cola, probando uniformidad. En el dominio vacío se usa la convención $E_n=0$ y el contrato se satisface vacuamente.

## 27.9. El margen al pasar al supremo

[]{#MA-EX-ANM-01-027-009}

[]{#MA-SOL-ANM-01-027-009}

Si $X\ne\varnothing$, la uniformidad con tolerancia uno entrega una cola cuyas imágenes de error son no vacías y acotadas. Completitud define allí los supremos reales $E_n$. Para $\varepsilon>0$, usamos el contrato con tolerancia $\varepsilon/2$ y reunimos su corte con el de existencia de las envolventes. Cada error posterior es menor que $\varepsilon/2$, por lo que cada supremo es a lo sumo $\varepsilon/2<\varepsilon$. Así $E_n\to0$. El factor dos conserva un margen tras el paso al supremo. Para el vacío, las envolventes se declaran cero y cumplen directamente el límite.

## 27.10. Regiones que nunca se vacían

[]{#MA-EX-ANM-01-027-010}

[]{#MA-SOL-ANM-01-027-010}

Con $k=n+3$, la condición $t_n(x)\ge1/2$ equivale a $1-|kx-2|\ge1/2$, es decir $|kx-2|\le1/2$. Por tanto $B_n(1/2)=[3/(2k),5/(2k)]$, un segmento no vacío contenido en $[0,1]$. Los extremos pertenecen porque la infracción incluye igualdad. La entrada cero queda fuera siempre. Para $x>0$ fijo, desde un corte con $n+3>3/x$ queda a la derecha de todo el soporte y no vuelve a pertenecer al conjunto infractor. Cada entrada sale eventualmente, pero ningún conjunto completo queda vacío. Ésa es la diferencia entre el contrato puntual y el uniforme en este ejemplo.

## 27.11. Supremo sin máximo de las potencias

[]{#MA-EX-ANM-01-027-011}

[]{#MA-SOL-ANM-01-027-011}

[]{#MA-SEC-ANM-01-027-003}

Para $n\ge1$, el error respecto del límite puntual es $x^n$ si $0\le x<1$ y cero en $x=1$. Todos los errores son menores que uno, así uno es una cota superior que no se alcanza. Para probar optimalidad, si $0\le c<1$ ponemos $s=(1-c)/[2(n+1)]>0$ y $x=1-s\in[0,1)$. Bernoulli da $x^n\ge1-ns>c$, porque $ns<(1-c)$. Una cota negativa ya falla ante un error cero. Por tanto $E_n=1$ para cada $n\ge1$, sin máximo, y esas envolventes refutan uniformidad.

## 27.12. Una restricción con máximo

[]{#MA-EX-ANM-01-027-012}

[]{#MA-SOL-ANM-01-027-012}

En $[0,c]$, con $0<c<1$, el límite es cero y para $n\ge1$ el orden de potencias no negativas da $0\le x^n\le c^n$. La entrada $c$ alcanza el último valor, así $E_n=c^n$ es un máximo. Escribiendo $t=1/c-1>0$, Bernoulli da $c^n\le1/(1+nt)$. Un natural $N>1/(\varepsilon t)$, reunido con el índice uno, garantiza error menor que $\varepsilon$ en toda entrada y toda la cola. La convergencia es uniforme. Si se permite $c=0$, la única columna es cero desde la etapa uno y se trata directamente.

## 27.13. Un pico que sigue siendo grande

[]{#MA-EX-ANM-01-027-013}

[]{#MA-SOL-ANM-01-027-013}

Las tiendas satisfacen $0\le t_n\le1$ y alcanzan uno en $z_n=2/(n+3)$. Como su límite puntual es cero, su envolvente de error es $E_n(t)=1$. Con $k=n+3$, la tienda normalizada $b_n=kt_n$ está entre cero y $k$ y alcanza $k$ en el mismo centro, así $E_n(b)=k$. Para tolerancia $1/2$, ante cualquier corte tomamos una etapa posterior y su centro, que sigue en $[0,1]$. Ambas familias infringen allí la tolerancia. Ninguna converge uniformemente hacia cero, aunque cada columna termine siendo exactamente cero.

## 27.14. Un máximo global decreciente

[]{#MA-EX-ANM-01-027-014}

[]{#MA-SOL-ANM-01-027-014}

Escribimos $k=n+1>0$. La desigualdad $(\sqrt{k}|x|-1)^2\ge0$ da $1+kx^2\ge2\sqrt{k}|x|$. Para $x\ne0$, dividir permite concluir $|h_n(x)|\le1/(2\sqrt{k})$; en cero la magnitud es cero. En $x=\pm1/\sqrt{k}$ el denominador vale dos y se alcanza esa cota, así $E_n=1/(2\sqrt{n+1})$ es el máximo exacto en toda la recta. Para $\varepsilon>0$, un natural $N>1/(4\varepsilon^2)$ garantiza $n+1>1/(4\varepsilon^2)$ cuando $n\ge N$, y por tanto $E_n<\varepsilon$. Queda probada uniformidad hacia cero sin restringir el dominio.

**Retorno visual.** Véase [C27-F03](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.15. La amplitud reduce el error

[]{#MA-EX-ANM-01-027-015}

[]{#MA-SOL-ANM-01-027-015}

Para $0\le x\le1$, se tiene $0\le x^{n+1}\le1$. Así $|v_n(x)|\le1/(n+1)$ y la entrada uno alcanza la cota. Es el máximo y la envolvente de error respecto de cero. Un natural $N>1/\varepsilon$ da $1/(n+1)<\varepsilon$ para todos los índices posteriores, uniformemente en la entrada. En las potencias sin ese divisor el peor error permanece cerca de uno; aquí la amplitud decreciente controla también las entradas próximas al extremo.

## 27.16. Restricción con barrera común

[]{#MA-EX-ANM-01-027-016}

[]{#MA-SOL-ANM-01-027-016}

[]{#MA-SEC-ANM-01-027-004}

Si $Y\subseteq X$, el corte uniforme elegido en $X$ sigue siendo válido para toda entrada de $Y$, así las restricciones convergen uniformemente. Si ambos conjuntos son no vacíos y existen las envolventes de la fila examinada, la imagen de errores sobre $Y$ está contenida en la de $X$. Todo número que acote la segunda acota la primera, y la minimalidad del supremo da $E_n(Y)\le E_n(X)$. Si $Y$ es vacío, su error se declara cero y no hay obligaciones de entrada. La restricción puede reducir la envolvente y no obliga a conservarla exactamente.

## 27.17. Reunión de dos contratos

[]{#MA-EX-ANM-01-027-017}

[]{#MA-SOL-ANM-01-027-017}

Para $\varepsilon>0$, las restricciones a $A$ y $B$ proporcionan cortes $N_A,N_B$. Tomamos $N=\max(N_A,N_B)$. Si $n\ge N$ y $x\in X=A\cup B$, la entrada pertenece al menos a una de las piezas y el contrato de esa pieza da $|f_n(x)-f(x)|<\varepsilon$. La misma candidata se usa en las dos restricciones, así no hay discrepancias en su intersección. El argumento incluye piezas vacías y no requiere condiciones topológicas: el máximo finito de cortes es el dato que une los contratos.

## 27.18. Una unión infinita falla

[]{#MA-EX-ANM-01-027-018}

[]{#MA-SOL-ANM-01-027-018}

La pieza $X_j$ tiene extremo $c_j=1-1/(j+2)<1$, así las potencias convergen uniformemente a cero en ella con envolvente $c_j^n$. Su unión es $[0,1)$: cada entrada $x<1$ pertenece a alguna pieza porque puede elegirse $j$ con $1/(j+2)\le1-x$. Sobre la unión, para cada $n\ge1$ el supremo del error es uno, mediante entradas arbitrariamente próximas al extremo ausente. Por tanto allí la convergencia no es uniforme. Los cortes de las piezas dependen de $j$ y no tienen una barrera común que permita repetir el argumento de unión finita.

**Retorno visual.** Véase [C27-F04](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.19. Una ruta cualquiera

[]{#MA-EX-ANM-01-027-019}

[]{#MA-SOL-ANM-01-027-019}

La ruta $x_n\in X$ está dada. Para $\varepsilon>0$, el contrato uniforme proporciona $N$ que sirve a todas las entradas de todas las filas posteriores. En particular, si $n\ge N$ sirve en la entrada $x_n$, y $|f_n(x_n)-f(x_n)|<\varepsilon$. Esto prueba que el error diagonal tiende a cero sin exigir convergencia de la ruta. Para reemplazar el valor móvil $f(x_n)$ por $f(x)$ haría falta, por ejemplo, $x_n\to x\in X$ y continuidad de $f$ en ese destino; entonces una segunda aplicación de la triangular completa la comparación.

## 27.20. Subsucesión y prefijo

[]{#MA-EX-ANM-01-027-020}

[]{#MA-SOL-ANM-01-027-020}

Sea $(n_j)$ una sucesión estrictamente creciente de naturales. La inducción da $n_j\ge j$: el primer término es no negativo y cada siguiente es al menos una unidad mayor. Si $N$ es un corte uniforme de la familia, entonces para $j\ge N$ se tiene $n_j\ge N$ y $|f_{n_j}(x)-f(x)|<\varepsilon$ para toda entrada. Así la subsucesión hereda el límite uniforme. La conversa falla en las filas constantes $(-1)^n$ sobre un dominio no vacío: la subsucesión par es idénticamente uno, mientras la completa alterna y no tiene límite puntual ni uniforme.

## 27.21. Álgebra con dos presupuestos

[]{#MA-EX-ANM-01-027-021}

[]{#MA-SOL-ANM-01-027-021}

[]{#MA-SEC-ANM-01-027-005}

Dada $\varepsilon>0$, pedimos a las dos familias errores menores que $\varepsilon/[2(|\alpha|+1)]$ y $\varepsilon/[2(|\beta|+1)]$, respectivamente. Sus cortes uniformes tienen un máximo $N$. En toda entrada de cualquier fila posterior, el error de la combinación es a lo sumo $|\alpha||f_n-f|+|\beta||g_n-g|\le(\varepsilon/2)\big(|\alpha|/(|\alpha|+1)+|\beta|/(|\beta|+1)\big)<\varepsilon$. Los coeficientes nulos están incluidos porque los denominadores siguen positivos. Por tanto $\alpha f_n+\beta g_n$ converge uniformemente a $\alpha f+\beta g$.

## 27.22. Producto con barreras declaradas

[]{#MA-EX-ANM-01-027-022}

[]{#MA-SOL-ANM-01-027-022}

Suponemos $|f|\le A$ y $|g|\le B$, con $A,B\ge0$ globales. El corte uniforme para $|f_n-f|<1$ da $|f_n|\le A+1$ en toda entrada de la cola. La identidad $f_ng_n-fg=f_n(g_n-g)+g(f_n-f)$ proporciona error a lo sumo $(A+1)|g_n-g|+B|f_n-f|$. Pedimos al error de $g_n$ una cota $\varepsilon/[2(A+2)]$ y al de $f_n$ una cota $\varepsilon/[2(B+1)]$, reuniendo sus cortes con el de la barrera. La suma resultante es menor que $\varepsilon$. Todas las constantes son independientes de la entrada, así el producto converge uniformemente a $fg$.

## 27.23. Producto sin barrera

[]{#MA-EX-ANM-01-027-023}

[]{#MA-SOL-ANM-01-027-023}

En la recta, tomamos $f_n(x)=x$ en toda etapa y $g_n(x)=1/(n+1)$. La primera familia converge uniformemente a $f(x)=x$ con error cero; la segunda converge uniformemente a $g=0$ con error constante $1/(n+1)$. El producto de filas es $x/(n+1)$ y el producto de límites es cero. Ante cualquier corte $N$, la entrada $x=N+1$ de la fila $n=N$ da error uno, refutando uniformidad con tolerancia $1/2$. La magnitud del límite $f(x)=x$ no tiene barrera global y el factor creciente amplifica el error pequeño del segundo.

**Retorno visual.** Véase [C27-F05](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.24. Cuadrar una aproximación global

[]{#MA-EX-ANM-01-027-024}

[]{#MA-SOL-ANM-01-027-024}

La familia original tiene error global $1/(n+1)$ respecto de la identidad. Al cuadrar, la diferencia es $(x+1/(n+1))^2-x^2=2x/(n+1)+1/(n+1)^2$. Para cada índice crece sin cota en magnitud al variar $x$ por la recta. Un testigo explícito es $x=n+1$, donde el error vale $2+1/(n+1)^2>1$; por tanto no hay uniformidad hacia $x^2$. Si los valores de filas y límite utilizados estuvieran todos en $[-M,M]$, se tendría $|u^2-v^2|=|u-v||u+v|\le2M|u-v|$. Esa barrera convierte el cuadrado en una operación Lipschitz sobre el rango común y sí permite transportar uniformidad.

## 27.25. Recíproco con margen

[]{#MA-EX-ANM-01-027-025}

[]{#MA-SOL-ANM-01-027-025}

El contrato uniforme para error $m/2$ proporciona una cola en la que $|g_n(x)|\ge|g(x)|-|g_n(x)-g(x)|>m/2$ para todas las entradas. Así los recíprocos de esa cola son funciones reales sobre el mismo $X$. Allí $|1/g_n-1/g|=|g_n-g|/(|g_n||g|)\le2|g_n-g|/m^2$. Para $\varepsilon>0$, reunimos el corte de dominio con el corte uniforme para error original menor que $\varepsilon m^2/2$. El error recíproco es entonces menor que $\varepsilon$. Las filas iniciales pueden tener ceros; para hablar de una familia desde el índice cero deben revisarse o reemplazarse explícitamente por funciones definidas, sin alterar esta cola.

## 27.26. Norma y salida cero

[]{#MA-EX-ANM-01-027-026}

[]{#MA-SOL-ANM-01-027-026}

[]{#MA-SEC-ANM-01-027-006}

Si $X\ne\varnothing$, cada $|u(x)|$ está entre cero y su supremo $\|u\|_\infty$. Si la norma es cero, todas esas magnitudes son cero, así $u$ coincide con la función nula. Recíprocamente, para la función nula la imagen de magnitudes es $\{0\}$ y su supremo es cero. En el dominio vacío se declaró norma cero para la única función, que también es la función nula vacía. Así la equivalencia vale en ambos casos, manteniendo separada la convención del vacío de la existencia de un supremo real.

## 27.27. Homogeneidad sin máximos

[]{#MA-EX-ANM-01-027-027}

[]{#MA-SOL-ANM-01-027-027}

Supongamos $X\ne\varnothing$ y $\alpha\ne0$. El número $|\alpha|\|u\|_\infty$ acota todas las magnitudes $|\alpha u(x)|$. Si $C$ es cualquier cota superior de éstas, dividir por $|\alpha|>0$ da una cota $C/|\alpha|$ para todas las magnitudes de $u$. La minimalidad de su supremo implica $|\alpha|\|u\|_\infty\le C$. Por tanto ese número es exactamente $\|\alpha u\|_\infty$. Si $\alpha=0$, ambos lados valen cero directamente. Si $X$ es vacío, ambas normas se definieron cero y la igualdad también es inmediata. No se usó un punto que alcanzara la norma.

## 27.28. Distancia triangular

[]{#MA-EX-ANM-01-027-028}

[]{#MA-SOL-ANM-01-027-028}

Las diferencias de funciones acotadas siguen acotadas, así las tres distancias existen. Para cada entrada, $|u(x)-w(x)|\le|u(x)-v(x)|+|v(x)-w(x)|\le d_\infty(u,v)+d_\infty(v,w)$. El último real es por tanto una cota superior de toda la imagen de magnitudes de $u-w$. Tomar su supremo da $d_\infty(u,w)\le d_\infty(u,v)+d_\infty(v,w)$. La conclusión usa cotas universales y no necesita máximos alcanzados. En el vacío, todas las distancias son cero por convención.

## 27.29. Banda y bola de frontera estricta

[]{#MA-EX-ANM-01-027-029}

[]{#MA-SOL-ANM-01-027-029}

Para $u(x)=x$ en $(0,1)$, cada entrada satisface $|u(x)-0|=x<1$. Por tanto la gráfica queda dentro de la banda abierta entre menos uno y uno alrededor de la función cero. Sin embargo el supremo de las magnitudes es uno, así $d_\infty(u,0)=1$. La condición de bola estricta pide una distancia menor que uno y no se cumple. El error nunca alcanza la frontera, pero se aproxima a ella sin un margen común positivo. Al probar equivalencias de convergencia, usar tolerancia $\varepsilon/2$ evita este problema de frontera.

**Retorno visual.** Véase [C27-F06](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.30. Clase trasladada

[]{#MA-EX-ANM-01-027-030}

[]{#MA-SOL-ANM-01-027-030}

La diferencia entre la identidad $r(x)=x$ y cero tiene magnitud $|x|$, no acotada en la recta. Por tanto no tiene supremo real y $d_\infty(r,0)$ no es una distancia real definida en esta teoría. Si $u,v$ son acotadas, en cambio, $(r+u)-(r+v)=u-v$ tiene una barrera global dada por la suma de sus cotas. Su norma existe y define la distancia entre esas dos traslaciones. La clase $r+\mathcal B(\mathbb R)$ permite medir diferencias acotadas con una base común no acotada; no extiende la distancia real a todos los pares arbitrarios de funciones.

## 27.31. De destino a pares

[]{#MA-EX-ANM-01-027-031}

[]{#MA-SOL-ANM-01-027-031}

[]{#MA-SEC-ANM-01-027-007}

Dada $\varepsilon>0$, la convergencia uniforme a $f$ entrega un corte $N$ para error $\varepsilon/3$. Para todo $m,n\ge N$ y toda entrada, la triangular da $|f_n(x)-f_m(x)|\le|f_n(x)-f(x)|+|f(x)-f_m(x)|<2\varepsilon/3<\varepsilon$. Éste es el contrato uniforme de Cauchy, con dos índices posteriores al mismo corte. La función destino ya existe por hipótesis. La prueba sólo reúne errores mediante la triangular y no usa completitud para construir ningún valor nuevo.

## 27.32. Construir primero el límite

[]{#MA-EX-ANM-01-027-032}

[]{#MA-SOL-ANM-01-027-032}

Cauchy uniforme implica Cauchy numérico en cada entrada fija. C10 proporciona un límite real único por columna y esas salidas forman una función $f:X\to\mathbb R$. Para demostrar uniformidad, fijamos $\varepsilon>0$ y elegimos un corte común $N$ de Cauchy para error $\varepsilon/3$. Fijados $n\ge N$ y $x$, para todo $m\ge N$ tenemos $|f_n(x)-f_m(x)|<\varepsilon/3$. Al llevar $m$ al límite, la continuidad del absoluto y la preservación del orden dan $|f_n(x)-f(x)|\le\varepsilon/3<\varepsilon$. El corte precedía a $n$ y a $x$, así controla todas las filas y entradas requeridas. En el vacío se obtiene directamente la función vacía.

## 27.33. Conservar el destino en funciones acotadas

[]{#MA-EX-ANM-01-027-033}

[]{#MA-SOL-ANM-01-027-033}

Una sucesión de Cauchy en $d_\infty$ cumple el contrato uniforme de Cauchy porque cada error de entrada está acotado por esa distancia. El criterio anterior construye un límite uniforme real $f$. Falta comprobar que permanece en $\mathcal B(X)$. Usamos Cauchy con tolerancia uno y fijamos la fila de referencia $f_N$. Para todos los índices $m\ge N$ y todas las entradas, $|f_m(x)-f_N(x)|<1$. Pasar $m$ al límite da $|f(x)-f_N(x)|\le1$, luego $|f(x)|\le\|f_N\|_\infty+1$. Así $f$ es acotada. La caracterización por envolventes convierte después el contrato uniforme en $d_\infty(f_n,f)\to0$. Queda probada completitud secuencial, con el vacío incluido por sus convenciones.

## 27.34. Vecinos cada vez más próximos

[]{#MA-EX-ANM-01-027-034}

[]{#MA-SOL-ANM-01-027-034}

Sobre un dominio no vacío, cada $H_n$ es una función constante y $d_\infty(H_{n+1},H_n)=1/(n+1)\to0$. Pero para $m\ge1$, $H_{2m}-H_m=\sum_{j=m+1}^{2m}1/j\ge m/(2m)=1/2$. Ante cualquier corte $N$, tomamos $m\ge\max(N,1)$; ambos índices $m,2m$ quedan en la cola y en cualquier entrada su diferencia es al menos $1/2$. La tolerancia $1/2$ refuta el error estricto pedido por Cauchy uniforme. Los incrementos vecinos pequeños no controlan la acumulación de muchos incrementos entre etapas lejanas. En un dominio vacío todas las filas serían la misma función, así ese caso no sería un contraejemplo.

**Retorno visual.** Véase [C27-F07](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.35. La completitud tiene un lugar

[]{#MA-EX-ANM-01-027-035}

[]{#MA-SOL-ANM-01-027-035}

La dirección de convergencia uniforme a Cauchy sólo usa el destino dado, la triangular y un corte común. En la dirección inversa, la completitud de los reales interviene al aplicar C10 para obtener el límite de cada columna de Cauchy. La unicidad de esas salidas construye el grafo de una función. Para recuperar uniformidad se mantiene fijo un índice y una entrada y se lleva la otra columna al límite: continuidad del absoluto y orden conservan una cota no estricta, cuyo margen $\varepsilon/3$ basta para el contrato. Si se trabaja en $\mathcal B(X)$, una fila acotada de referencia aporta después la barrera del destino. Ningún paso exige compacidad del dominio ni continuidad de las filas.

## 27.36. Presupuesto geométrico finito

[]{#MA-EX-ANM-01-027-036}

[]{#MA-SOL-ANM-01-027-036}

[]{#MA-SEC-ANM-01-027-008}

Suponemos $C\ge0$ y $0<q<1$. Para $n>m$, telescopía y triangular dan $|f_n(x)-f_m(x)|\le\sum_{j=m}^{n-1}|f_{j+1}(x)-f_j(x)|\le C\sum_{j=m}^{n-1}q^j=Cq^m(1-q^{n-m})/(1-q)\le Cq^m/(1-q)$. La suma utilizada es finita. Para $m>n$ se intercambian los índices, y para igualdad el error es cero. Como $q^j\to0$, un corte común del menor índice hace la cota menor que cualquier tolerancia, demostrando Cauchy uniforme. Su criterio produce $f$. Fijados $m,x$, pasar $n$ al límite conserva $|f(x)-f_m(x)|\le Cq^m/(1-q)$, un certificado válido en todo el dominio. Si $C=0$, las filas coinciden y se verifica directamente.

## 27.37. Destino acotado o diferencia acotada

[]{#MA-EX-ANM-01-027-037}

[]{#MA-SOL-ANM-01-027-037}

El presupuesto telescópico desde la etapa cero da $|f_n(x)-f_0(x)|\le C/(1-q)$ para todos los índices y entradas. Tras construir el límite, el mismo paso numérico conserva $|f(x)-f_0(x)|\le C/(1-q)$. Si $f_0$ es acotada, sumar su barrera da $|f_n|,|f|\le\|f_0\|_\infty+C/(1-q)$ y todos pertenecen a $\mathcal B(X)$. Si la base es arbitraria, sólo se garantiza que cada diferencia respecto de ella es acotada, así las funciones viven en $f_0+\mathcal B(X)$. Por ejemplo una base identidad en la recta puede conservar su crecimiento no acotado aunque las correcciones converjan uniformemente.

## 27.38. Un presupuesto que se alcanza

[]{#MA-EX-ANM-01-027-038}

[]{#MA-SOL-ANM-01-027-038}

La familia está definida sobre un dominio común, con $|a(x)|\le1$ y base $r$ arbitraria. Su incremento es $f_{n+1}-f_n=2^{-n-1}a$, de magnitud a lo sumo $(1/2)(1/2)^n$. El presupuesto geométrico tiene por tanto $C=q=1/2$ y certifica error a lo sumo $2^{-n}$. La cuenta directa identifica el destino $f=r+a$, pues $f_n-f=-2^{-n}a$. Así la convergencia es uniforme con la misma cota. En dominio no vacío la envolvente exacta es $2^{-n}\sup|a|$; si ese supremo es uno, la barrera $2^{-n}$ es exacta, alcanzada sólo cuando alguna magnitud de $a$ alcance uno. La base puede ser no acotada porque se cancela en la diferencia.

**Retorno visual.** Véase [C27-F08](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html#fig-anm-c27-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 27.39. Monotonía con límite continuo

[]{#MA-EX-ANM-01-027-039}

[]{#MA-SOL-ANM-01-027-039}

Los intervalos $(0,1/(n+1))$ se encogen, así $s_{n+1}(x)\le s_n(x)$ para toda entrada. En cero todas las alturas son cero. Para $x>0$ fijo, desde un corte con $n+1>1/x$ la entrada queda fuera del intervalo positivo y la columna es cero. El límite puntual es la función cero, continua. Sin embargo $x_n=1/[2(n+1)]$ pertenece al intervalo de la fila $n$ y tiene error uno respecto de ese límite. Con tolerancia $1/2$ ninguna cola es uniforme. Las filas tienen discontinuidades en sus bordes de salto, incluida la discontinuidad relativa en cero; ese dato impide omitir la regularidad de las filas en cualquier comparación con teoremas adicionales.

## 27.40. Una auditoría de condiciones

[]{#MA-EX-ANM-01-027-040}

[]{#MA-SOL-ANM-01-027-040}

Para afirmar uniformidad se necesitan un dominio común, una candidata y, para cada tolerancia, un corte que controle toda entrada en toda fila posterior. Una barrera universal de error que tienda a cero proporciona ese certificado. Para usar una distancia suprema real hay que demostrar que las diferencias medidas están acotadas y tratar el vacío por su convención; esto vale en $\mathcal B(X)$ o en una clase trasladada con base común. Para una ruta dada, uniformidad controla $f_n(x_n)-f(x_n)$ sin pedir convergencia de las entradas. Si se quiere comparar con $f(x)$, se añade $x_n\to x\in X$ y continuidad del límite en ese centro, o un control equivalente que justifique $f(x_n)\to f(x)$. Estos datos identifican exactamente qué error queda protegido en cada conclusión.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Ejercicios](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez-microcontroles.html)
