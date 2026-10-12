---
content-id: MA-BCH-0300
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-024-SOLUCIONES
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
title: Soluciones — Capítulo 24
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C24_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)

## 24.1. Acumular una tasa afín

[]{#MA-EX-ANM-01-024-001}

[]{#MA-SOL-ANM-01-024-001}

[]{#MA-SEC-ANM-01-024-001}

La restricción es integrable por C23. La integral afín da $A_f(x)=x^2-x$ para $x>0$, y en cero vale cero por convención. Los valores son $0,-1/4,0$. La tasa empieza negativa y termina positiva, por lo que la acumulación firmada vuelve a su origen sin ser nula dentro.

**Retorno visual.** Véase [C24-F01](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.2. Cambiar de origen

[]{#MA-EX-ANM-01-024-002}

[]{#MA-SOL-ANM-01-024-002}

Aditividad orientada da $\int_a^x f=\int_a^c f+\int_c^x f$, cualquiera sea el orden de las entradas. Restar identifica los números; las integrales existen por restricción y orientación. Para $f=1$, $A_f(x)=x$, y la nueva función es $x-3/4$, negativa si $x<c$.

## 24.3. Grafo sin selección

[]{#MA-EX-ANM-01-024-003}

[]{#MA-SOL-ANM-01-024-003}

Para cada $x>a$ existe un único real por integrabilidad de la restricción; en $x=a$ el único valor declarado es cero. Separar los pares que cumplen cada caso en el producto $[a,b]\times\mathbb R$ forma un grafo total y univaluado. No se escoge simultáneamente una integral por entrada: la unicidad determina cada salida.

## 24.4. Incremento orientado

[]{#MA-EX-ANM-01-024-004}

[]{#MA-SOL-ANM-01-024-004}

Con $y<x$, aditividad ordenada da $A_f(x)=A_f(y)+\int_y^x f$. Restar y aplicar orientación produce $A_f(y)-A_f(x)=-\int_y^x f=\int_x^y f$. Si coinciden, la resta y la integral degenerada son cero. No se divide por anchuras nulas.

## 24.5. Acumular un escalón

[]{#MA-EX-ANM-01-024-005}

[]{#MA-SOL-ANM-01-024-005}

En $[0,x]$ con $x<1/2$ la tasa es cero. Con $x=1/2$, sólo el último punto tiene valor uno; cambios finitos conservan integral cero. Si $x>1/2$, aditividad en el corte suma cero y la integral de constante uno sobre $[1/2,x]$, de valor $x-1/2$. Las fórmulas coinciden en el corte.

## 24.6. Lipschitz de la acumulada

[]{#MA-EX-ANM-01-024-006}

[]{#MA-SOL-ANM-01-024-006}

[]{#MA-SEC-ANM-01-024-002}

Orden integral da $|A_f(y)-A_f(x)|\le3|y-x|$ para entradas ordenadas; intercambio cubre el otro orden. Para $\varepsilon>0$, $\delta=\varepsilon/4$ produce diferencia menor que $3\varepsilon/4<\varepsilon$, uniforme en ambos centros. Comparar con $-1$ da $|A_f(x)|\le3(x+1)\le9$.

**Retorno visual.** Véase [C24-F02](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.7. El caso de cota nula

[]{#MA-EX-ANM-01-024-007}

[]{#MA-SOL-ANM-01-024-007}

Su denominador siempre es positivo. Si $B=0$, la cota Lipschitz implica incrementos cero, menores que cualquier tolerancia positiva. Si $B>0$, con distancia menor que el radio la diferencia es menor que $B\varepsilon/(B+1)<\varepsilon$. No se divide por una cota nula.

## 24.8. Signo y orden

[]{#MA-EX-ANM-01-024-008}

[]{#MA-SOL-ANM-01-024-008}

Para $x<y$, orden de integrales aplicado a la constante $m$ da $A_f(y)-A_f(x)=\int_x^y f\ge m(y-x)>0$. Ambos factores finales son positivos. Si sólo $m=0$, la conclusión es débil y no prueba crecimiento estricto.

## 24.9. Positivo en un punto

[]{#MA-EX-ANM-01-024-009}

[]{#MA-SOL-ANM-01-024-009}

Tome el pico de C23: altura uno en $1/2$ y cero fuera. Es no negativo y positivo allí. Todas las restricciones difieren de la función cero en a lo sumo un punto, luego su integral es cero. La acumulada es constante y no estrictamente creciente.

## 24.10. Cociente encerrado

[]{#MA-EX-ANM-01-024-010}

[]{#MA-SOL-ANM-01-024-010}

Orden y constante dan $-2(y-x)\le A_f(y)-A_f(x)\le5(y-x)$. La anchura es positiva, por lo que dividir da cociente entre $-2$ y $5$. Las cotas son universales suficientes; no hace falta que ningún valor de $f$ sea exactamente alguna de ellas.

## 24.11. El lado negativo del cociente

[]{#MA-EX-ANM-01-024-011}

[]{#MA-SOL-ANM-01-024-011}

[]{#MA-SEC-ANM-01-024-003}

Integre las cotas $f(x)-\eta\le f(t)\le f(x)+\eta$ en $[y,x]$. Dividir por $x-y>0$ encierra $[A_f(x)-A_f(y)]/(x-y)$. Cambiar ambos signos deja idéntico el cociente $[A_f(y)-A_f(x)]/(y-x)$. Restar $f(x)$ y usar el encierro equivalente al valor absoluto da error $\le\eta$.

## 24.12. Radio puntual completo

[]{#MA-EX-ANM-01-024-012}

[]{#MA-SOL-ANM-01-024-012}

Continuidad con $\varepsilon/2$ entrega $\rho>0$. Tome $\delta=\min\{\rho,(x-a)/2,(b-x)/2\}$. Cada $y$ admisible con distancia positiva menor que ese radio encierra un tramo cuyos puntos están a distancia menor que $\rho$ del centro. Allí el error de la tasa es menor que $\varepsilon/2$, luego a lo sumo ese número. El lema encierra el error de cualquier cociente por $\varepsilon/2<\varepsilon$. Los dos lados acumulan por ser centro interior y la unicidad de C18 da la derivada.

## 24.13. Cociente exacto del cuadrado

[]{#MA-EX-ANM-01-024-013}

[]{#MA-SOL-ANM-01-024-013}

Expandir $[(1/2+h)^3-(1/2)^3]/(3h)$ da $1/4+h/2+h^2/3$. El residuo respecto de $1/4$ tiende a cero por álgebra de límites. La fórmula vale para ambos signos si la entrada está en el dominio, y confirma el valor puntual sin tomar una muestra como prueba general.

**Retorno visual.** Véase [C24-F03](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.14. Residuo cuadrático sin Taylor

[]{#MA-EX-ANM-01-024-014}

[]{#MA-SOL-ANM-01-024-014}

Para $y>x$, la resta es $\int_x^y(f(t)-f(x))\,dt$ por linealidad. Su absoluto está acotado por la integral de $L(t-x)$, igual a $L(y-x)^2/2$ por la fórmula afín. Para $y<x$, invertir orientación y usar $L(x-t)$ en $[y,x]$ da $L(x-y)^2/2$. En igualdad ambos miembros son cero; con $L=0$, el residuo es cero. No se aplicó un resto de Taylor.

## 24.15. Continuidad local y global

[]{#MA-EX-ANM-01-024-015}

[]{#MA-SOL-ANM-01-024-015}

Integrabilidad global permite definir todas las restricciones y la acumulada. Continuidad sólo en el centro controla todos los valores del tramo corto para fabricar el radio de derivación. No se requiere continuidad en otros puntos; en ellos la acumulada sigue existiendo y siendo continua por R2. La acumulación del dominio en el centro evita una condición vacía.

## 24.16. Derivada en el borde

[]{#MA-EX-ANM-01-024-016}

[]{#MA-SOL-ANM-01-024-016}

[]{#MA-SEC-ANM-01-024-004}

El borde acumula desde la derecha porque $a<b$. Continuidad para $\varepsilon/2$ da $\rho$; reduzca el radio a $\min\{\rho,(b-a)/2\}$. Si $a<y$ y $y-a$ es menor, cada $t\in[a,y]$ está dentro de la vecindad. El lema da error del cociente $\le\varepsilon/2<\varepsilon$. No se afirma ningún valor para entradas menores que $a$.

## 24.17. Dos pendientes incompatibles

[]{#MA-EX-ANM-01-024-017}

[]{#MA-SOL-ANM-01-024-017}

Sus cocientes son cero a la izquierda y uno a la derecha. Si un límite $D$ existiera, tolerancia $1/3$ daría un radio común. Tome $r=\frac12\min\{\delta,1/2\}>0$; las dos entradas $1/2\pm r$ son admisibles y producirían $|D|<1/3$ y $|1-D|<1/3$. Triangular da $1<2/3$, imposible.

## 24.18. Derivada existente, valor no recuperado

[]{#MA-EX-ANM-01-024-018}

[]{#MA-SOL-ANM-01-024-018}

Cambios finitos conservan integral cero sobre todo $[0,x]$, incluso cuando el pico es un borde de la restricción. La acumulada es la función cero y todos sus cocientes son cero, de modo que su derivada vale cero. En el pico la tasa vale uno y no es continua. Existencia de la derivada de la acumulada no basta para igualdad con la tasa.

**Retorno visual.** Véase [C24-F04](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.19. Modificar un extremo

[]{#MA-EX-ANM-01-024-019}

[]{#MA-SOL-ANM-01-024-019}

Cada restricción difiere de cero en un punto, luego todas las integrales y la acumulada son cero. El cociente derecho también es cero y su límite es cero, distinto de $f(0)=1$. La continuidad relativa de la integranda en el borde falla: sus valores cercanos son cero.

## 24.20. Corolario de tasa continua

[]{#MA-EX-ANM-01-024-020}

[]{#MA-SOL-ANM-01-024-020}

C23 da integrabilidad, que legitima R1. R2 da continuidad uniforme de la acumulada en todo el dominio. En cada centro interior se aplica R3; en los dos bordes, el argumento unilateral de R4. Son derivadas relativas al dominio original, no derivadas bilaterales de una prolongación no especificada.

## 24.21. Telescopía de una primitiva

[]{#MA-EX-ANM-01-024-021}

[]{#MA-SOL-ANM-01-024-021}

[]{#MA-SEC-ANM-01-024-005}

Fije un índice de pieza. La restricción de $H$ cumple las hipótesis de Lagrange, por lo que un testigo interior identifica el incremento con $f(c)\Delta$. Acotarlo por $m\Delta,M\Delta$ elimina el testigo. Esa desigualdad vale para todo índice; sumar finitamente cancela los nodos interiores y deja $H(b)-H(a)$. Las sumas extremas son las de Darboux; no se ha asumido integrabilidad ni se ha formado una familia de testigos.

**Retorno visual.** Véase [C24-F05](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.22. Encierro y evaluación

[]{#MA-EX-ANM-01-024-022}

[]{#MA-SOL-ANM-01-024-022}

La integral y el incremento están en el mismo intervalo de cotas para toda partición. Dado $\varepsilon>0$, el criterio entrega una brecha menor que ella, así la distancia entre ambos números es menor que $\varepsilon$. Si la distancia fuera $d>0$, elegir $d/2$ da contradicción; por ello coinciden. No se usa continuidad de la tasa ni la primera parte del fundamental.

## 24.23. Borde discontinuo de la candidata

[]{#MA-EX-ANM-01-024-023}

[]{#MA-SOL-ANM-01-024-023}

No. La derivada interior es cero, pero la integral vale cero y el incremento de borde es $-1$. Falta continuidad de $H$ en cero y Lagrange no se aplica al primer segmento. Por la definición del capítulo, esa $H$ no es una primitiva admisible en el cerrado.

## 24.24. Subintervalo y orientación

[]{#MA-EX-ANM-01-024-024}

[]{#MA-SOL-ANM-01-024-024}

Si $u<v$, restrinja ambas funciones a $[u,v]$: integrabilidad, continuidad y derivabilidad interior se conservan. R5 da $\int_u^v f=H(v)-H(u)$. Para igualdad, ambos miembros cero. Si $v<u$, aplicar la fórmula ordenada a $[v,u]$ y negar ambos lados usa orientación de C23 y da la misma identidad.

## 24.25. Hipótesis independientes

[]{#MA-EX-ANM-01-024-025}

[]{#MA-SOL-ANM-01-024-025}

La primera requiere integrabilidad global y continuidad en el centro para recuperar la tasa al derivar la acumulada. La segunda exige integrabilidad y una primitiva continua en el cerrado con igualdad de derivadas interiores; no exige continuidad de la integranda. Mera integrabilidad no construye aquí una primitiva, y mera existencia de derivadas no certifica integrabilidad.

## 24.26. Constante de primitivas

[]{#MA-EX-ANM-01-024-026}

[]{#MA-SOL-ANM-01-024-026}

[]{#MA-SEC-ANM-01-024-006}

La diferencia es continua en el cerrado, derivable dentro y de derivada cero por C18. C19 sobre cada par de entradas prueba constancia. Evaluar en $a$ da $H-K=3-(-2)=5$. Si otra constante cumpliera lo mismo, evaluar allí forzaría el mismo valor.

## 24.27. Un dato inicial

[]{#MA-EX-ANM-01-024-027}

[]{#MA-SOL-ANM-01-024-027}

R1/R4 construyen $A_f(x)=x^2-x$. La función $H(x)=2+x^2-x$ es continua en el cerrado, derivable dentro y tiene derivada $2x-1$ por C18; cumple el dato. Dos soluciones difieren en una constante por R6, que el dato fija en cero, de modo que ésta es única.

## 24.28. Potencia entera

[]{#MA-EX-ANM-01-024-028}

[]{#MA-SOL-ANM-01-024-028}

C18 da derivada de $t^4/4$ igual a $t^3$, por regla de potencias enteras. Ambas funciones son continuas en el cerrado; la tasa es integrable por C23. R5 evalúa $(2^4-(-1)^4)/4=(16-1)/4=15/4$. El valor conserva signo y no se obtuvo suponiendo la integral igual a una primitiva por definición.

## 24.29. Cancelación y absoluto

[]{#MA-EX-ANM-01-024-029}

[]{#MA-SOL-ANM-01-024-029}

La primitiva $t^2-t$ da valor total cero. Para el absoluto, parta en $1/2$: antes vale $1-2t$, con integral $1/4$; después vale $2t-1$, con integral $1/4$. Aditividad suma $1/2$. Por tanto integral cero de una tasa firmada no implica tasa cero ni absoluto integral cero.

**Retorno visual.** Véase [C24-F06](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.30. Estacionario sin extremo

[]{#MA-EX-ANM-01-024-030}

[]{#MA-SOL-ANM-01-024-030}

La primitiva $t^3$ y el origen $-1$ dan $A_f(x)=x^3+1$. Su derivada en cero es $f(0)=0$. El cubo es estrictamente creciente por C19 o su identidad de diferencias; las entradas negativas tienen valor menor que uno y las positivas mayor. Por ello cero no es máximo ni mínimo.

## 24.31. Partes desde producto

[]{#MA-EX-ANM-01-024-031}

[]{#MA-SOL-ANM-01-024-031}

[]{#MA-SEC-ANM-01-024-007}

Las continuas $p,q$ son integrables; $v,w$ lo son por hipótesis. C23 garantiza productos $pw,vq$ y suma integrables. El producto $pq$ es continuo en el cerrado y de derivada $vq+pw$ interior por C18. Es primitiva admisible de esa suma. R5 y linealidad dan $\int(vq+pw)=p(b)q(b)-p(a)q(a)$; restar $\int vq$ obtiene la identidad.

## 24.32. Comprobar una integración por partes

[]{#MA-EX-ANM-01-024-032}

[]{#MA-SOL-ANM-01-024-032}

Las funciones y derivadas $v=1,w=t$ son continuas, luego integrables. La frontera del producto es $1/2$ y $\int_0^1vq=\int_0^1t^2/2=1/6$ por R6 y escalar. Partes da $\int_0^1pw=1/2-1/6=1/3$, coincidente con la potencia calculada antes.

## 24.33. Cambio de variable decreciente

[]{#MA-EX-ANM-01-024-033}

[]{#MA-SOL-ANM-01-024-033}

La tasa es continua, $g$ continuo y derivable con extensión constante $v=-1$, integrable. El integrando es $-(1-t)$, cuya integral es $-1/2$ por la fórmula afín. Los extremos transformados son uno y cero; $\int_1^0s\,ds=-1/2$. La derivada negativa y la orientación representan el mismo cambio de sentido.

## 24.34. Ida y vuelta sin monotonía

[]{#MA-EX-ANM-01-024-034}

[]{#MA-SOL-ANM-01-024-034}

La derivada extendida $v(t)=2t$ es continua, y la composición es $t^2$. La fórmula integra $2t^3$ y da cero porque $g(-1)=g(1)=1$. Si se usa el absoluto, el integrando es $2|t|^3$ y las dos mitades dan $1/2$ cada una, total uno. Se ha quitado la cancelación, por lo que no es la misma identidad.

**Retorno visual.** Véase [C24-F07](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.35. La imagen toca un borde

[]{#MA-EX-ANM-01-024-035}

[]{#MA-SOL-ANM-01-024-035}

R4 dio derivadas relativas de $A_f$ en ambos bordes, con la tasa continua allí. Todos los centros del segmento acumulan en ese dominio. La cadena relativa de C18 admite esos centros y no divide por incrementos de $g$, que pueden ser nulos. La composición sigue siendo continua en el cerrado y su derivada interior es $f(g(t))g'(t)$; R5 se aplica con la extensión integrable declarada.

## 24.36. Error uniforme de la tasa

[]{#MA-EX-ANM-01-024-036}

[]{#MA-SOL-ANM-01-024-036}

[]{#MA-SEC-ANM-01-024-008}

Linealidad da $A_f(x)-A_g(x)=\int_0^x(f-g)$. La cota universal y orden integral implican absoluto $\le x/100\le3/100$. En $3$ queda la cota $3/100$; no se asegura igualdad ni un error menor sin más información.

**Retorno visual.** Véase [C24-F08](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.37. Dato inicial y tasa

[]{#MA-EX-ANM-01-024-037}

[]{#MA-SOL-ANM-01-024-037}

R5 sobre cada restricción expresa las salidas como dato inicial más acumulada. Triangular y la cota integral dan $|H(x)-K(x)|\le1/10+x/100\le3/25$. En $2$, $1/10+2/100=3/25$. Ambas cotas deben ser universales o datos exactos; una tabla finita no certifica el error de la tasa.

## 24.38. Misma acumulada, distintas tasas

[]{#MA-EX-ANM-01-024-038}

[]{#MA-SOL-ANM-01-024-038}

La función cero y el pico de altura uno en $1/2$ son integrables y diferentes. Todas las restricciones tienen integral cero por cambios finitos, así sus acumuladas coinciden. En el pico, la segunda tasa no es continua; allí no se cumple la hipótesis de recuperación. En los demás puntos ambas tasas y la derivada de la acumulada valen cero.

## 24.39. Promedio alcanzado

[]{#MA-EX-ANM-01-024-039}

[]{#MA-SOL-ANM-01-024-039}

C16 da mínimo y máximo alcanzados; orden integral encierra el promedio entre ambos. C15 sobre el segmento entre entradas de esos extremos entrega un valor igual al promedio. Para el escalón con corte $1/2$, la integral es $1/2$ y la longitud uno, pero sus valores son sólo cero y uno. Es integrable y no alcanza su promedio; la continuidad es una hipótesis real de esa consecuencia.

## 24.40. Dos operaciones y una constante

[]{#MA-EX-ANM-01-024-040}

[]{#MA-SOL-ANM-01-024-040}

Para continua $f$, derivar su acumulada recupera $f$ interior y relativamente en bordes. Para $H$ continua en el cerrado y derivable dentro con extensión integrable de derivada $f$, integrar recupera $H(x)-H(a)$. La constante debe reponerse como dato inicial. No se ha probado que toda derivada sea integrable ni que toda integrable tenga primitiva; los requisitos no pueden suprimirse.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-microcontroles.html)
