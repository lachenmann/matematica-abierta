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
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C24_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html)

## 24.1. Acumular una tasa afín

[]{#MA-EX-ANM-01-024-001}

[]{#MA-SOL-ANM-01-024-001}

[]{#MA-SEC-ANM-01-024-001}

La tasa afín es integrable y sus restricciones también. Para $x>0$, la fórmula de C22 calcula la integral de una afín como la longitud por el promedio de sus alturas extremas. Por tanto $A_f(x)=x\big((-1)+(2x-1)\big)/2=x^2-x$. En $x=0$, la convención degenerada da cero y coincide con la fórmula. Así $A_f(0)=0$, $A_f(1/2)=-1/4$ y $A_f(1)=0$. En el interior, $x(x-1)<0$. La acumulación baja mientras la tasa es negativa y vuelve al valor inicial cuando la contribución positiva completa la compensación.

**Retorno visual.** Véase [C24-F01](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.2. Cambiar de origen

[]{#MA-EX-ANM-01-024-002}

[]{#MA-SOL-ANM-01-024-002}

Definimos $A_{f,c}(x)=\int_c^x f$ mediante restricción y orientación. Si $c\le x$, aditividad da $A_f(x)=A_f(c)+\int_c^x f$. Si $x<c$, da $A_f(c)=A_f(x)+\int_x^c f$; al restar y negar la integral se obtiene la misma igualdad $A_{f,c}(x)=A_f(x)-A_f(c)$. Para $x=c$ ambos lados son cero. Con $f=1$ en $[0,1]$, $A_f(x)=x$ y el nuevo origen $c=3/4$ da $A_{f,c}(x)=x-3/4$. Sus valores negativos antes de $c$ reflejan la orientación de esos tramos.

## 24.3. Grafo sin selección

[]{#MA-EX-ANM-01-024-003}

[]{#MA-SOL-ANM-01-024-003}

Para $a<x\le b$, C23 garantiza la integrabilidad de $f|_{[a,x]}$ y la unicidad de su valor integral. En $x=a$ declaramos la única salida cero. Dentro de $[a,b]\times\mathbb R$, consideramos la relación que contiene $(a,0)$ y los pares $(x,r)$ con $a<x\le b$ y $r=\int_a^x f$. Cada entrada del intervalo tiene exactamente una salida real, y ninguna entrada exterior pertenece al producto. La relación es por tanto el grafo de una función con dominio exacto $[a,b]$. La unicidad determina las salidas, sin una selección simultánea de testigos de integración.

## 24.4. Incremento orientado

[]{#MA-EX-ANM-01-024-004}

[]{#MA-SOL-ANM-01-024-004}

Si $x<y$, aditividad sobre los intervalos contiguos da $\int_a^y f=\int_a^x f+\int_x^y f$, incluyendo el caso $x=a$ por la convención degenerada. Así $A_f(y)-A_f(x)=\int_x^y f$. Si $y<x$, la identidad ordenada da $A_f(x)-A_f(y)=\int_y^x f$. Al negar se obtiene $A_f(y)-A_f(x)=-\int_y^x f=\int_x^y f$. Con $x=y$, tanto la diferencia como la integral degenerada valen cero. Las integrales existen por restricción; la inversión de extremos modifica su signo.

## 24.5. Acumular un escalón

[]{#MA-EX-ANM-01-024-005}

[]{#MA-SOL-ANM-01-024-005}

Sea $h(t)=0$ para $t<1/2$ y $h(t)=1$ para $t\ge1/2$. Si $0<x<1/2$, la restricción a $[0,x]$ es cero y su integral vale cero. Si $x=1/2$, difiere de la función cero sólo en su último punto; C23 conserva la integral cero. Si $x>1/2$, aditividad da $A_h(x)=\int_0^{1/2}h+\int_{1/2}^x h=0+(x-1/2)$. Junto con $A_h(0)=0$, queda $A_h(x)=0$ para $x\le1/2$ y $A_h(x)=x-1/2$ para $x\ge1/2$. Las dos fórmulas tienen el mismo valor en el corte, por lo que no hay salto en la acumulada.

## 24.6. Lipschitz de la acumulada

[]{#MA-EX-ANM-01-024-006}

[]{#MA-SOL-ANM-01-024-006}

[]{#MA-SEC-ANM-01-024-002}

El origen es $a=-1$. Para $x<y$, el orden integral aplicado a $-3\le f\le3$ da $-3(y-x)\le\int_x^y f\le3(y-x)$. La identidad de incrementos implica $|A_f(y)-A_f(x)|\le3|y-x|$; intercambiar entradas prueba el mismo resultado si $y<x$, y la igualdad es inmediata. Dada $\varepsilon>0$, el radio $\delta=\varepsilon/4$ sirve para todos los centros: si $|y-x|<\delta$, el incremento tiene magnitud menor que $3\varepsilon/4<\varepsilon$. Esto prueba continuidad uniforme. Como $A_f(-1)=0$, también $|A_f(x)|\le3(x+1)\le9$ en todo el intervalo.

**Retorno visual.** Véase [C24-F02](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.7. El caso de cota nula

[]{#MA-EX-ANM-01-024-007}

[]{#MA-SOL-ANM-01-024-007}

La cota absoluta tiene $B\ge0$, así $B+1>0$ y $\delta=\varepsilon/(B+1)$ es un radio positivo para toda tolerancia positiva. Si $B>0$ y $|y-x|<\delta$, se obtiene $|A_f(y)-A_f(x)|\le B|y-x|<B\varepsilon/(B+1)<\varepsilon$. Si $B=0$, la desigualdad $|f|\le0$ hace la tasa idénticamente cero y todos los incrementos de la acumulada son cero. El mismo radio sirve en ese caso. Como no depende del centro, demuestra continuidad uniforme.

## 24.8. Signo y orden

[]{#MA-EX-ANM-01-024-008}

[]{#MA-SOL-ANM-01-024-008}

Sean $x<y$. La restricción de $f$ es integrable y la constante $m$ tiene integral $m(y-x)$. El orden $f\ge m$ implica $A_f(y)-A_f(x)=\int_x^y f\ge m(y-x)$. Tanto $m$ como $y-x$ son positivos, así el incremento es estrictamente positivo. Por tanto $A_f$ es estrictamente creciente y satisface la cota cuantitativa $A_f(y)-A_f(x)\ge m(y-x)$ en todo par ordenado. Esta cota también impide que un tramo de longitud positiva tenga acumulación nula.

## 24.9. Positivo en un punto

[]{#MA-EX-ANM-01-024-009}

[]{#MA-SOL-ANM-01-024-009}

Definimos $p(1/2)=1$ y $p(t)=0$ para las demás entradas de $[0,1]$. Es integrable por el argumento del pico de C23, no negativa y positiva en $1/2$. En cada $[0,x]$ difiere de la función cero en a lo sumo un punto, por lo que $\int_0^x p=0$. Su acumulada es idénticamente cero y tiene iguales valores en cualesquiera dos entradas. Esto refuta el crecimiento estricto bajo la sola hipótesis de positividad en algún punto.

## 24.10. Cociente encerrado

[]{#MA-EX-ANM-01-024-010}

[]{#MA-SOL-ANM-01-024-010}

La integral de las constantes en $[x,y]$ vale, respectivamente, $-2(y-x)$ y $5(y-x)$. Al integrar las cotas universales resulta $-2(y-x)\le\int_x^y f=A_f(y)-A_f(x)\le5(y-x)$. Como $y-x>0$, dividir conserva el orden y da $-2\le(A_f(y)-A_f(x))/(y-x)\le5$. La conclusión sólo requiere que las cotas valgan para todas las entradas del tramo. No necesita que alguna altura sea exactamente menos dos o cinco, ni que esas cotas sean los extremos óptimos de la imagen.

## 24.11. El lado negativo del cociente

[]{#MA-EX-ANM-01-024-011}

[]{#MA-SOL-ANM-01-024-011}

[]{#MA-SEC-ANM-01-024-003}

Suponemos $y<x$ y $|f(t)-f(x)|\le\eta$ para todo $t\in[y,x]$. Integramos $f(x)-\eta\le f(t)\le f(x)+\eta$ sobre ese segmento ordenado. Su longitud positiva permite dividir y obtener $f(x)-\eta\le\big(\int_y^x f\big)/(x-y)\le f(x)+\eta$. Por aditividad, el cociente central es $(A_f(x)-A_f(y))/(x-y)$, igual a $(A_f(y)-A_f(x))/(y-x)$ al cambiar los dos signos. Restar $f(x)$ da un error entre $-\eta$ y $\eta$, equivalente a magnitud a lo sumo $\eta$. Así el lado negativo queda cubierto sin dividir una desigualdad por un número negativo.

## 24.12. Radio puntual completo

[]{#MA-EX-ANM-01-024-012}

[]{#MA-SOL-ANM-01-024-012}

Sea $x\in(a,b)$ y $\varepsilon>0$. La continuidad de $f$ en $x$ proporciona $\rho>0$ tal que $|f(t)-f(x)|<\varepsilon/2$ para toda entrada del dominio con $|t-x|<\rho$. Tomamos $\delta=\min\{\rho,(x-a)/2,(b-x)/2\}>0$. Para cualquier $y$ con $0<|y-x|<\delta$, todo punto del segmento entre $x$ e $y$ dista de $x$ a lo sumo $|y-x|<\rho$. El error de la tasa en todo ese tramo está acotado por $\varepsilon/2$. El lema del promedio, válido para los dos órdenes, da $\left|(A_f(y)-A_f(x))/(y-x)-f(x)\right|\le\varepsilon/2<\varepsilon$. El radio precede a toda $y$ y ambos lados contienen entradas cercanas al centro, así esta es la prueba completa de $A_f'(x)=f(x)$.

## 24.13. Cociente exacto del cuadrado

[]{#MA-EX-ANM-01-024-013}

[]{#MA-SOL-ANM-01-024-013}

Los incrementos admisibles satisfacen $-1/2\le h\le1/2$ y $h\ne0$. La fórmula por sumas de C22 da $A_f(x)=x^3/3$. Por tanto el cociente en $1/2$ es $\big((1/2+h)^3-(1/2)^3\big)/(3h)$. Expandir el cubo produce numerador $3h/4+3h^2/2+h^3$ y dividir da $1/4+h/2+h^2/3$. Su diferencia respecto de $1/4$ tiene magnitud a lo sumo $|h|/2+h^2/3$. Para $|h|\le1/2$, esto no supera $2|h|/3$, que tiende a cero. La misma cuenta cubre ambos signos y confirma la derivada $1/4$.

**Retorno visual.** Véase [C24-F03](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.14. Residuo cuadrático sin Taylor

[]{#MA-EX-ANM-01-024-014}

[]{#MA-SOL-ANM-01-024-014}

Por linealidad e incrementos, el residuo $R=A_f(y)-A_f(x)-f(x)(y-x)$ es $\int_x^y(f(t)-f(x))\,dt$. Si $x<y$, la triangular integral y Lipschitz dan $|R|\le\int_x^y|f(t)-f(x)|\,dt\le\int_x^y L(t-x)\,dt=L(y-x)^2/2$. La última evaluación es la fórmula afín de C22. Si $y<x$, invertimos orientación para trabajar en $[y,x]$, donde $|f(t)-f(x)|\le L(x-t)$; su integral vale $L(x-y)^2/2$. Si $x=y$, el residuo es cero. Así $|R|\le L|y-x|^2/2$ en todos los casos, también con $L=0$, sin usar Taylor.

## 24.15. Continuidad local y global

[]{#MA-EX-ANM-01-024-015}

[]{#MA-SOL-ANM-01-024-015}

La integrabilidad en todo $[a,b]$ permite restringir la tasa, construir cada valor de $A_f$ y escribir los incrementos como integrales. Además aporta una cota absoluta que demuestra continuidad de la acumulada. Para derivarla en una entrada interior fija $x$, sólo se necesita continuidad de $f$ en $x$: el radio puntual controla todas las alturas del segmento entre $x$ y una entrada cercana. El promedio local fuerza entonces el límite del cociente a $f(x)$. No interviene continuidad de la tasa en el resto del intervalo. El carácter interior del centro permite acercamientos por ambos lados; en los bordes la misma prueba produce derivadas relativas.

## 24.16. Derivada en el borde

[]{#MA-EX-ANM-01-024-016}

[]{#MA-SOL-ANM-01-024-016}

[]{#MA-SEC-ANM-01-024-004}

Sea $\varepsilon>0$. La continuidad relativa de $f$ en $a$ proporciona $\rho>0$ con $|f(t)-f(a)|<\varepsilon/2$ para las entradas del dominio a distancia menor que $\rho$ de $a$. Ponemos $\delta=\min\{\rho,(b-a)/2\}>0$. Si $a<y\le b$ y $y-a<\delta$, todos los puntos de $[a,y]$ están en esa vecindad. Integrar las cotas y dividir por $y-a>0$ da $\left|(A_f(y)-A_f(a))/(y-a)-f(a)\right|\le\varepsilon/2<\varepsilon$. Como $a<b$, existen entradas derechas arbitrariamente próximas. El límite derecho, que es la derivada relativa al cerrado en $a$, vale $f(a)$.

## 24.17. Dos pendientes incompatibles

[]{#MA-EX-ANM-01-024-017}

[]{#MA-SOL-ANM-01-024-017}

La acumulada del escalón es cero hasta $c=1/2$ y $x-c$ después. Sus cocientes en $c$ valen cero para incrementos negativos y uno para positivos. Supongamos que tuviera derivada $D$. Con tolerancia $1/3$ existiría $\delta>0$ tal que todos los cocientes de entradas a distancia positiva menor que $\delta$ estuvieran a distancia menor que $1/3$ de $D$. Elegimos $r=\frac12\min\{\delta,1/2\}>0$. Las entradas $c-r,c+r$ pertenecen al dominio y cumplen la escala pedida. Sus cocientes dan $|D|<1/3$ y $|1-D|<1/3$. La triangular implicaría $1\le|D|+|1-D|<2/3$, contradicción. La acumulada es continua en el corte y carece de derivada allí.

## 24.18. Derivada existente, valor no recuperado

[]{#MA-EX-ANM-01-024-018}

[]{#MA-SOL-ANM-01-024-018}

Para el pico $p(1/2)=1$, $p=0$ fuera, cada restricción a $[0,x]$ difiere de la tasa cero en a lo sumo una entrada. C23 conserva sus integrales, incluso si el punto excepcional coincide con el extremo $x$. Por ello $A_p(x)=0$ para toda entrada. En el centro $c=1/2$, todos sus cocientes son cero y $A_p'(c)=0$. En cambio $p(c)=1$. La tasa no es continua en $c$: cualquier vecindad contiene entradas distintas donde vale cero. Falla precisamente la hipótesis que permite recuperar el valor puntual de la tasa.

**Retorno visual.** Véase [C24-F04](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.19. Modificar un extremo

[]{#MA-EX-ANM-01-024-019}

[]{#MA-SOL-ANM-01-024-019}

La función dada difiere de cero sólo en el extremo izquierdo. Sobre cada $[0,x]$ de longitud positiva, el cambio finito conserva la integral cero; en $x=0$ la convención da también cero. Así $A_f$ es la función cero. Para $y>0$, $(A_f(y)-A_f(0))/y=0$, por lo que su derivada derecha en cero vale cero. Este valor difiere de $f(0)=1$. La continuidad relativa de la tasa falla allí, pues todas las entradas positivas próximas tienen altura cero. El ejemplo muestra que también en un borde un valor aislado puede perderse al acumular.

## 24.20. Corolario de tasa continua

[]{#MA-EX-ANM-01-024-020}

[]{#MA-SOL-ANM-01-024-020}

Una función continua sobre $[a,b]$, con $a<b$, está acotada y es integrable por C23. Sus restricciones construyen $A_f$, y la cota absoluta prueba que esa acumulada es Lipschitz y continua en todo el cerrado. En cada punto de $(a,b)$, la continuidad puntual de la tasa permite aplicar la primera parte del fundamental y obtener $A_f'=f$. En $a$ se usa el argumento derecho; en $b$, el izquierdo. Ambos recuperan los valores de la tasa por continuidad relativa. Se obtiene una primitiva normalizada, con derivadas de borde referidas al dominio original.

## 24.21. Telescopía de una primitiva

[]{#MA-EX-ANM-01-024-021}

[]{#MA-SOL-ANM-01-024-021}

[]{#MA-SEC-ANM-01-024-005}

Fijemos una pieza $[x_{i-1},x_i]$ de $P$. La continuidad de $H$ en el cerrado y su derivabilidad interior permiten aplicar Lagrange en esa pieza. Existe $c$ en su interior con $H(x_i)-H(x_{i-1})=H'(c)\Delta_i=f(c)\Delta_i$. Como $m_i\le f(c)\le M_i$ y $\Delta_i>0$, queda $m_i\Delta_i\le H(x_i)-H(x_{i-1})\le M_i\Delta_i$. El testigo ha desaparecido de esta conclusión, que vale para cualquier índice. Sumamos las desigualdades finitas; los valores de $H$ en nodos interiores se cancelan y obtenemos $L(f,P)\le H(b)-H(a)\le U(f,P)$. La acotación de $f$ garantiza extremos reales, y no se necesitó formar una familia de etiquetas ni suponer integrabilidad.

**Retorno visual.** Véase [C24-F05](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.22. Encierro y evaluación

[]{#MA-EX-ANM-01-024-022}

[]{#MA-SOL-ANM-01-024-022}

Sea $I=\int_a^b f$, cuya existencia se añade como hipótesis. Para toda partición, el encierro del ejercicio anterior y el de la integral sitúan $H(b)-H(a)$ e $I$ en el mismo intervalo $[L(f,P),U(f,P)]$. Por tanto $|H(b)-H(a)-I|\le G(f,P)$. Dada $\varepsilon>0$, el criterio de Darboux produce una partición de brecha menor que $\varepsilon$, dando distancia menor que ella. Si la distancia fuera $d>0$, aplicar el criterio con $d/2$ produciría $d<d/2$, imposible. Luego $I=H(b)-H(a)$. La prueba usa Lagrange e integrabilidad; no requiere continuidad de $f$.

## 24.23. Borde discontinuo de la candidata

[]{#MA-EX-ANM-01-024-023}

[]{#MA-SOL-ANM-01-024-023}

Para $x\in(0,1)$, la función $H$ es localmente constante cero, así $H'(x)=0=f(x)$. La tasa cero es integrable y $\int_0^1f=0$. Sin embargo, $H(1)-H(0)=0-1=-1$, así la igualdad de evaluación falla. La candidata es discontinua en cero, porque sus valores derechos son cero y su valor inicial es uno. Por tanto no es una primitiva admisible según la definición del capítulo. En cualquier primera pieza que empiece en cero, falta la continuidad requerida por Lagrange, que era el paso que conectaba la derivada interior con el incremento nodal.

## 24.24. Subintervalo y orientación

[]{#MA-EX-ANM-01-024-024}

[]{#MA-SOL-ANM-01-024-024}

Si $u<v$, la tasa restringida a $[u,v]$ es integrable. La restricción de $H$ es continua en ese cerrado y derivable en su interior, con derivada igual a la tasa allí. Newton–Leibniz da $\int_u^v f=H(v)-H(u)$. Si $u=v$, la integral degenerada y la diferencia valen cero. Si $v<u$, aplicamos la fórmula ordenada sobre $[v,u]$ y negamos: $\int_u^v f=-\int_v^u f=-(H(u)-H(v))=H(v)-H(u)$. Así la evaluación vale para todos los pares del dominio, con la orientación correspondiente.

## 24.25. Hipótesis independientes

[]{#MA-EX-ANM-01-024-025}

[]{#MA-SOL-ANM-01-024-025}

La primera parte empieza con una tasa integrable y construye su acumulada. Para recuperar la tasa al derivar en una entrada se añade continuidad en esa entrada; si es un borde, la continuidad y la derivada son relativas. La segunda parte empieza con una tasa integrable y una primitiva $H$ ya dada, continua en el cerrado y derivable dentro, con $H'=f$ en el interior. Evalúa la integral por incrementos de $H$ sin exigir continuidad de $f$. La primera dirección construye una primitiva cuando la tasa es continua; la segunda evalúa mediante una primitiva admisible existente. Ambas conservan la hipótesis de integrabilidad que legitima sus valores integrales.

## 24.26. Constante de primitivas

[]{#MA-EX-ANM-01-024-026}

[]{#MA-SOL-ANM-01-024-026}

[]{#MA-SEC-ANM-01-024-006}

La diferencia $D=H-K$ es continua en $[a,b]$, derivable en $(a,b)$ y tiene derivada $D'=H'-K'=0$. Para cualesquiera $u<v$ del dominio, Lagrange sobre $[u,v]$ da $D(v)-D(u)=D'(c)(v-u)=0$. Por tanto $D$ es constante en todo el intervalo, incluidos los bordes. Evaluar en $a$ fija $D(a)=3-(-2)=5$, así $H(x)=K(x)+5$ para toda entrada. La misma evaluación muestra que ninguna otra constante podría satisfacer esos datos.

## 24.27. Un dato inicial

[]{#MA-EX-ANM-01-024-027}

[]{#MA-SOL-ANM-01-024-027}

La acumulada de la tasa afín es $A_f(x)=x^2-x$. Por tanto proponemos $H(x)=2+x^2-x$. Es continua en $[0,1]$, derivable dentro, tiene $H'(x)=2x-1$ por las reglas de C18 y cumple $H(0)=2$. Si $K$ es otra solución admisible, $K-H$ es continua en el cerrado y tiene derivada cero en el interior. Lagrange la hace constante, y el dato inicial da $K(0)-H(0)=0$. Así $K=H$ y la solución es única entre las primitivas con la regularidad declarada.

## 24.28. Potencia entera

[]{#MA-EX-ANM-01-024-028}

[]{#MA-SOL-ANM-01-024-028}

La tasa $t^3$ es continua en $[-1,2]$ y por tanto integrable. La regla de potencias enteras de C18 da $\big(t^4/4\big)'=t^3$, y la función $H(t)=t^4/4$ es continua en el cerrado y derivable dentro. Es una primitiva admisible. Newton–Leibniz permite evaluar $\int_{-1}^2t^3\,dt=H(2)-H(-1)=(16-1)/4=15/4$. Por aditividad, el tramo negativo aporta $-1/4$ y el positivo aporta cuatro, dando la misma suma firmada.

## 24.29. Cancelación y absoluto

[]{#MA-EX-ANM-01-024-029}

[]{#MA-SOL-ANM-01-024-029}

Para $2t-1$, la primitiva $H(t)=t^2-t$ da $\int_0^1(2t-1)\,dt=H(1)-H(0)=0$. Para el absoluto, partimos en $1/2$. Sobre $[0,1/2]$ vale $1-2t$ y la primitiva $t-t^2$ da $1/2-1/4=1/4$. Sobre $[1/2,1]$ vale $2t-1$ y su integral es $0-(-1/4)=1/4$. Las funciones son continuas e integrables en los segmentos usados. Aditividad produce $\int_0^1|2t-1|\,dt=1/2$. En la integral firmada los aportes son $-1/4$ y $1/4$; al tomar el absoluto se suman sus magnitudes.

**Retorno visual.** Véase [C24-F06](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.30. Estacionario sin extremo

[]{#MA-EX-ANM-01-024-030}

[]{#MA-SOL-ANM-01-024-030}

La tasa continua $3t^2$ tiene primitiva $t^3$. Con origen en menos uno, Newton–Leibniz da $A_f(x)=x^3-(-1)^3=x^3+1$. Su derivada en cero es $3\cdot0^2=0$, así el punto es estacionario. Sin embargo, $A_f(x)<1=A_f(0)$ para $x<0$ y $A_f(x)>1$ para $x>0$, con entradas de ambos tipos en toda vecindad de cero. Esto excluye tanto un máximo como un mínimo local. Además el cubo es estrictamente creciente: si $u<v$, $v^3-u^3=(v-u)(v^2+uv+u^2)>0$, pues el segundo factor sólo podría ser cero con $u=v=0$.

## 24.31. Partes desde producto

[]{#MA-EX-ANM-01-024-031}

[]{#MA-SOL-ANM-01-024-031}

[]{#MA-SEC-ANM-01-024-007}

Suponemos $p,q$ continuas en $[a,b]$ y derivables dentro, con extensiones integrables $v,w$ de sus derivadas interiores. C23 hace integrables a $p,q$ por continuidad y a los productos $pw,vq$ y su suma por el álgebra de integrables. La función $H=pq$ es continua en el cerrado y la regla del producto da $H'=vq+pw$ en el interior. Es una primitiva admisible de esa suma. Newton–Leibniz da $\int_a^b(vq+pw)=p(b)q(b)-p(a)q(a)$. Por linealidad y existencia de ambas integrales, podemos restar $\int_a^b vq$ y obtener $\int_a^b pw=p(b)q(b)-p(a)q(a)-\int_a^b vq$. Los valores escogidos para $v,w$ en los bordes no cambian los valores integrales, por invariancia ante modificaciones finitas.

## 24.32. Comprobar una integración por partes

[]{#MA-EX-ANM-01-024-032}

[]{#MA-SOL-ANM-01-024-032}

Para $p(t)=t$ y $q(t)=t^2/2$, las extensiones de derivadas $v(t)=1$ y $w(t)=t$ son continuas en $[0,1]$, por tanto integrables. Los productos también lo son. La contribución de borde es $p(1)q(1)-p(0)q(0)=1/2$. La regla de potencias ya permite evaluar $\int_0^1vq=\int_0^1t^2/2=1/6$ mediante la primitiva $t^3/6$. La fórmula de partes da $\int_0^1pw=1/2-1/6=1/3$. Como $pw=t^2$, coincide con la evaluación directa por $t^3/3$. Esta comprobación utiliza valores de potencias previamente justificados.

## 24.33. Cambio de variable decreciente

[]{#MA-EX-ANM-01-024-033}

[]{#MA-SOL-ANM-01-024-033}

La tasa $f(s)=s$ es continua en $[0,1]$. La función $g(t)=1-t$ lleva $[0,1]$ a ese intervalo, es continua y tiene derivada extendida $v(t)=-1$, integrable. Así la integranda transformada es $f(g(t))v(t)=-(1-t)=t-1$. Su integral vale $[t^2/2-t]_0^1=-1/2$. Las imágenes extremas son $g(0)=1$ y $g(1)=0$, por lo que el lado derecho es $\int_1^0s\,ds=-\int_0^1s\,ds=-1/2$. El signo negativo de la derivada registra el recorrido decreciente y coincide con la orientación de los extremos transformados.

## 24.34. Ida y vuelta sin monotonía

[]{#MA-EX-ANM-01-024-034}

[]{#MA-SOL-ANM-01-024-034}

La función $g(t)=t^2$ lleva $[-1,1]$ a $[0,1]$ y tiene extensión continua de derivada $v(t)=2t$. Para la tasa continua $f(s)=s$, la integranda $f(g(t))v(t)=2t^3$ es integrable. Su primitiva $t^4/2$ da integral cero, igual a $\int_{g(-1)}^{g(1)}s\,ds=\int_1^1s\,ds=0$. Por separado, los aportes son $-1/2$ en $[-1,0]$ y $1/2$ en $[0,1]$. Si se sustituye $v$ por $|v|$, la integranda pasa a $2|t|^3$. En cada mitad su integral es $1/2$, así el total es uno. El recorrido de ida y vuelta, sin monotonía global, se cancela sólo en la fórmula con signo.

**Retorno visual.** Véase [C24-F07](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.35. La imagen toca un borde

[]{#MA-EX-ANM-01-024-035}

[]{#MA-SOL-ANM-01-024-035}

Sea $F=A_f$, con $f$ continua en $[a,b]$. La primera parte del fundamental da a $F$ derivadas relativas también en los extremos, con valores $f(a),f(b)$. Por tanto, si un centro interior $t$ de $g$ tiene imagen $c=g(t)$ en un borde, la aproximación de $F$ sigue siendo válida para los incrementos de imagen que permanecen en $[a,b]$. Escribimos $F(c+k)-F(c)=f(c)k+r(k)$, con $r(k)/|k|\to0$ para incrementos admisibles no nulos y $r(0)=0$. Tomando $k=g(t+h)-g(t)$, la derivabilidad de $g$ limita $|k|/|h|$ cerca de cero. Así $r(k)/h\to0$, y para $k=0$ el residuo es exactamente cero. Queda $(F\circ g)'(t)=f(g(t))g'(t)$ sin dividir por $k$. La composición es continua en el cerrado; la extensión integrable de $g'$ y el álgebra de C23 hacen integrable su tasa transformada, permitiendo Newton–Leibniz.

## 24.36. Error uniforme de la tasa

[]{#MA-EX-ANM-01-024-036}

[]{#MA-SOL-ANM-01-024-036}

[]{#MA-SEC-ANM-01-024-008}

La diferencia $f-g$ es integrable por el álgebra de C23. Para $0<x\le3$, linealidad da $A_f(x)-A_g(x)=\int_0^x(f-g)$. La cota universal $|f-g|\le1/100$ y el orden integral implican $|A_f(x)-A_g(x)|\le x/100\le3/100$. En $x=0$ la diferencia es cero y cumple la fórmula. En $x=3$ el error certificado es a lo sumo $3/100$. La cota es alcanzable, por ejemplo si $f-g$ es constantemente $1/100$, pero para tasas generales no afirma que el error efectivo alcance ese máximo.

**Retorno visual.** Véase [C24-F08](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html#fig-anm-c24-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 24.37. Dato inicial y tasa

[]{#MA-EX-ANM-01-024-037}

[]{#MA-SOL-ANM-01-024-037}

Sean $c_0=H(0)$ y $d_0=K(0)$, con $|c_0-d_0|=1/10$. Newton–Leibniz sobre cada restricción da $H(x)=c_0+\int_0^x f$ y $K(x)=d_0+\int_0^x g$, donde las tasas integrables satisfacen $|f-g|\le1/100$. La triangular y la cota integral producen $|H(x)-K(x)|\le1/10+x/100$ para $0\le x\le2$. En todo el dominio esto no supera $1/10+2/100=3/25$. El dato inicial aporta una diferencia fija y la discrepancia de las tasas aporta una cantidad proporcional a la longitud recorrida. Si ambas tienen el mismo signo, la cota puede alcanzarse.

## 24.38. Misma acumulada, distintas tasas

[]{#MA-EX-ANM-01-024-038}

[]{#MA-SOL-ANM-01-024-038}

Tomamos $f(t)=0$ en $[0,1]$ y $g(1/2)=1$, $g(t)=0$ en las demás entradas. La segunda tasa es integrable por modificación finita de la primera, y ambas son diferentes en $1/2$. Sobre cada $[0,x]$ sus integrales coinciden, así $A_f=A_g=0$ en todo el dominio. En el punto excepcional, $g$ es discontinua y la primera parte del fundamental no afirma recuperar su altura. En las demás entradas ambas tasas valen cero y son continuas relativamente, por lo que la derivada de la acumulada sí coincide con ellas. El ejemplo muestra por qué el requisito de continuidad puntual importa para identificar la tasa a partir de su acumulada.

## 24.39. Promedio alcanzado

[]{#MA-EX-ANM-01-024-039}

[]{#MA-SOL-ANM-01-024-039}

Sea $f$ continua en $[u,v]$, con $u<v$. Por C16, tiene mínimo $m$ y máximo $M$ alcanzados en entradas $s,t$. Integrar $m\le f\le M$ y dividir por $v-u>0$ da $m\le\mu\le M$, donde $\mu=(v-u)^{-1}\int_u^v f$. Si $m=M$, la función es constante y todas las entradas realizan el promedio. Si $m<M$, los puntos de los extremos son distintos; el valor intermedio en el segmento ordenado que los une entrega $c$ con $f(c)=\mu$, incluyendo los casos en que el promedio sea uno de los extremos. Para el escalón de corte $1/2$ en $[0,1]$, la integral y el promedio valen $1/2$, pero la imagen es $\{0,1\}$. Es una tasa integrable que no alcanza su promedio, así la conclusión no se extiende a toda integrable.

## 24.40. Dos operaciones y una constante

[]{#MA-EX-ANM-01-024-040}

[]{#MA-SOL-ANM-01-024-040}

Para una tasa continua $f$ en $[a,b]$, integrar desde $a$ produce $A_f$ y derivarla recupera $f$ en los puntos interiores y mediante derivadas relativas en los bordes. Para una función $H$ continua en el cerrado, derivable dentro y con extensión integrable $f$ de su derivada, integrar esa tasa produce $A_f(x)=H(x)-H(a)$. El valor inicial debe reponerse para reconstruir $H$. En la primera composición se conserva cada altura por continuidad; en la segunda se pierde una constante al derivar. El capítulo no demuestra que toda derivada sea integrable ni que toda tasa integrable tenga una primitiva: las hipótesis de los dos contratos siguen siendo necesarias para aplicar las fórmulas aquí probadas.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 24](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo.html) · [Ejercicios](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-24-el-teorema-fundamental-del-calculo-soluciones.html)
