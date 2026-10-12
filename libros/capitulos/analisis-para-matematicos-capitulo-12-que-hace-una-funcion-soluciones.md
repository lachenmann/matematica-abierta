---
content-id: MA-BCH-0252
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-012-SOLUCIONES
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
title: Soluciones — Capítulo 12
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C12_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 12](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html) · [Ejercicios](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-microcontroles.html)

## 12.1. La misma regla, tres objetos

[]{#MA-EX-ANM-01-012-001}

[]{#MA-SOL-ANM-01-012-001}

[]{#MA-SEC-ANM-01-012-001}

$g$ y $h$ tienen exactamente los pares $(x,x^2)$ con $x\ge0$, luego el mismo grafo. Sus codominios difieren, así que no son iguales. El grafo de $f$ contiene además, por ejemplo, $(-1,1)$, ausente de los otros dos. $f$ tiene distinto dominio de $g$ y $h$. Ningún par es igual como función tipada. Todas coinciden numéricamente en entradas no negativas.

## 12.2. Una relación que debe repararse

[]{#MA-EX-ANM-01-012-002}

[]{#MA-SOL-ANM-01-012-002}

La entrada $1$ tiene dos salidas distintas y la entrada $2$ no tiene ninguna. Eliminamos $(1,4)$ y añadimos $(2,4)$; quedan $(0,0),(1,1),(2,4)$. Cada entrada de $D$ tiene exactamente una salida en $E$. Sólo borrar o sólo añadir no repararía las dos deficiencias.

## 12.3. Ninguna tabla finita decide toda la función

[]{#MA-EX-ANM-01-012-003}

[]{#MA-SOL-ANM-01-012-003}

Como $A$ es finito y $\mathbb R$ infinito, existe $t\in\mathbb R\setminus A$. Por ejemplo, si $A$ no es vacío, $t=1+\sum_{a\in A}|a|$ supera todo elemento de $A$; si es vacío, sirve $t=0$. Definimos $f(x)=0$ para todo real y $g(x)=1$ cuando $x=t$, $g(x)=0$ en otro caso. Son funciones del mismo tipo, coinciden en $A$ y difieren en $t$. La tabla de $A$ no determina sus valores restantes.

## 12.4. Identidad extensional

[]{#MA-EX-ANM-01-012-004}

[]{#MA-SOL-ANM-01-012-004}

Si los grafos coinciden, $(x,f(x))\in G_g$, de modo que por unicidad de salida de $g$, $f(x)=g(x)$. Recíprocamente, igualdad de valores para toda entrada hace que cada par $(x,f(x))$ sea $(x,g(x))$ y viceversa; los grafos coinciden. Con dominio y codominio iguales, la convención tipada da $f=g$. Con codominios diferentes, la igualdad de grafos no basta, como muestran las dos versiones del cuadrado.

## 12.5. Discreto frente a real

[]{#MA-EX-ANM-01-012-005}

[]{#MA-SOL-ANM-01-012-005}

$G_a=\{(n,2n+1):n\in\mathbb N\}\subsetneq G_f$. La inclusión es estricta porque $(1/2,2)$ pertenece a $G_f$ y no a $G_a$. La sucesión tiene dominio $\mathbb N=\{0,1,\ldots\}$ y grafo discreto; la recta representa el grafo de $f$. El mismo cálculo en entradas naturales no identifica los dos objetos.

## 12.6. Imagen exacta de un intervalo

[]{#MA-EX-ANM-01-012-006}

[]{#MA-SOL-ANM-01-012-006}

[]{#MA-SEC-ANM-01-012-002}

La imagen es $[0,9]$. Toda entrada tiene $|x|\le3$, así que su cuadrado está en ese intervalo. Para $0\le y\le9$, la entrada $x=-\sqrt y\in[-3,0]\subseteq[-3,2)$ alcanza $y$. En particular $9$ se alcanza en $-3$, aunque $3$ no esté disponible; y cero se alcanza en cero.

## 12.7. Unión con dos piezas

[]{#MA-EX-ANM-01-012-007}

[]{#MA-SOL-ANM-01-012-007}

La primera pieza tiene imagen $[1,4]$: sus cuadrados están allí y $-\sqrt y$ alcanza cada $y$ de ese intervalo. La segunda tiene imagen $(0,1)$, con testigo $\sqrt y$. Por tanto la imagen de la unión es $(0,4]$. El valor $1$ sí se alcanza en $-1$, cero no se alcanza porque ninguna entrada es cero, y $4$ sí se alcanza en $-2$.

## 12.8. Imagen y cardinalidad finita

[]{#MA-EX-ANM-01-012-008}

[]{#MA-SOL-ANM-01-012-008}

Enumeramos $A=\{a_1,\ldots,a_n\}$ con entradas distintas. Su imagen consta de los $n$ valores listados, eliminando repeticiones, por lo que tiene a lo sumo $n$ elementos. Si la restricción es inyectiva, todos son distintos y hay $n$. Si no lo es, dos valores de la lista coinciden, y tras eliminar esa repetición quedan a lo sumo $n-1$. Para $A=\varnothing$, ambas cardinalidades son cero y la restricción es inyectiva de manera vacua.

## 12.9. La inclusión no estudia el orden

[]{#MA-EX-ANM-01-012-009}

[]{#MA-SOL-ANM-01-012-009}

Sirve $q(x)=x^2$. No es no decreciente porque $-2<-1$ pero $4>1$; no es no creciente porque $1<2$ pero $1<4$. Sin embargo, para $A\subseteq C$, cada salida de $q[A]$ tiene testigo $x\in A\subseteq C$, luego pertenece a $q[C]$. Son propiedades distintas: inclusión de conjuntos frente a comparación de valores.

## 12.10. Imagen de una diferencia

[]{#MA-EX-ANM-01-012-010}

[]{#MA-SOL-ANM-01-012-010}

Si $y\in f[A]\setminus f[C]$, existe $a\in A$ con $f(a)=y$. Ese $a$ no puede estar en $C$, pues entonces $y\in f[C]$. Así $a\in A\setminus C$, que prueba la inclusión. Para $q(x)=x^2$, $A=\{-1,1\}$ y $C=\{1\}$, el lado izquierdo es vacío y el derecho es $q[\{-1\}]=\{1\}$. Una entrada fuera de $C$ puede compartir salida con otra dentro de $C$.

## 12.11. Selección de dos bandas

[]{#MA-EX-ANM-01-012-011}

[]{#MA-SOL-ANM-01-012-011}

[]{#MA-SEC-ANM-01-012-003}

La condición $0\le x^2<1$ equivale a $|x|<1$, y $x^2=4$ equivale a $x=-2$ o $x=2$. Por tanto la preimagen es $(-1,1)\cup\{-2,2\}$. Se excluyen $\pm1$ por la desigualdad estricta, y se incluyen cero y las dos raíces de cuatro.

## 12.12. El dominio recorta la respuesta

[]{#MA-EX-ANM-01-012-012}

[]{#MA-SOL-ANM-01-012-012}

En toda la recta la condición da $[-2,-1)\cup(1,2]$. Intersectando con el dominio $[-1,3)$ desaparece la rama negativa, incluido $-1$ que además no cumple $x^2>1$. Queda $(1,2]$. Ambas inclusiones siguen de resolver la condición y exigir pertenencia al dominio.

## 12.13. Las fibras particionan el dominio

[]{#MA-EX-ANM-01-012-013}

[]{#MA-SOL-ANM-01-012-013}

Cada $y\in f[D]$ tiene un testigo de entrada, así que su fibra no es vacía. Si una entrada pertenece a las fibras de $y,z$, su única salida es tanto $y$ como $z$, luego $y=z$. Cada $x\in D$ pertenece a la fibra sobre $f(x)\in f[D]$, y toda fibra es subconjunto de $D$; su unión es exactamente $D$. Si $D$ es vacío, la familia es vacía y su unión también.

## 12.14. Recuperar todas las salidas solicitadas

[]{#MA-EX-ANM-01-012-014}

[]{#MA-SOL-ANM-01-012-014}

Si es sobreyectiva, $f[D]=E$ y la identidad del texto da $f[f^{-1}[B]]=B\cap E=B$. Recíprocamente, aplicamos la hipótesis a $B=E$: como $f^{-1}[E]=D$, obtenemos $f[D]=E$, que es sobreyectividad. No se necesita inyectividad: puede haber varias entradas para cada salida.

## 12.15. La preimagen conoce la función

[]{#MA-EX-ANM-01-012-015}

[]{#MA-SOL-ANM-01-012-015}

Para una entrada cualquiera $x\in D$, tomamos $B=\{f(x)\}$. Entonces $x\in f^{-1}[B]=g^{-1}[B]$, luego $g(x)\in\{f(x)\}$ y $g(x)=f(x)$. Vale para toda entrada y los tipos coinciden, así que las funciones son iguales. Si $D$ es vacío, los dos grafos son vacíos y la conclusión también vale. El conjunto de prueba puede elegirse después de fijar la entrada porque la hipótesis cubre todos los subconjuntos.

## 12.16. Álgebra de una selección

[]{#MA-EX-ANM-01-012-016}

[]{#MA-SOL-ANM-01-012-016}

[]{#MA-SEC-ANM-01-012-004}

Para $x\in D$, pertenecer al lado izquierdo significa $(f(x)\in B\text{ o }f(x)\in H)$ y $f(x)\notin K$. Esto equivale a $(x\in f^{-1}[B]\text{ o }x\in f^{-1}[H])$ y $x\notin f^{-1}[K]$, exactamente el lado derecho. Como la equivalencia vale para toda entrada, extensionalidad da igualdad. No se han supuesto inyectividad o sobreyectividad.

## 12.17. La intersección detecta inyectividad

[]{#MA-EX-ANM-01-012-017}

[]{#MA-SOL-ANM-01-012-017}

La dirección inyectiva está probada en el texto: los dos testigos de una salida común coinciden. Para la recíproca, supongamos $f(a)=f(c)$ y $a\ne c$. Tomando $A=\{a\}$, $C=\{c\}$, la imagen de su intersección es vacía, mientras que la intersección de imágenes es $\{f(a)\}$, contradicción. Luego no hay entradas distintas con igual salida.

**Retorno visual.** Véase [C12-F03](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 12.18. Saturar dos veces

[]{#MA-EX-ANM-01-012-018}

[]{#MA-SOL-ANM-01-012-018}

Cada $a\in A$ tiene salida en $f[A]$, luego está en $S(A)$. Si $A\subseteq C$, las inclusiones conservadas por imagen y preimagen dan $S(A)\subseteq S(C)$. Finalmente $f[S(A)]=f[f^{-1}[f[A]]]=f[A]\cap f[D]=f[A]$. Tomando preimagen, $S(S(A))=f^{-1}[f[S(A)]]=f^{-1}[f[A]]=S(A)$. La saturación añade fibras completas una sola vez.

## 12.19. Complementos y biyectividad

[]{#MA-EX-ANM-01-012-019}

[]{#MA-SOL-ANM-01-012-019}

Si $f$ es biyectiva, toda $y\in E$ tiene una única entrada $x$; está en la imagen de $D\setminus A$ exactamente cuando $x\notin A$, lo que equivale a $y\notin f[A]$. Para la recíproca, usar $A=\varnothing$ da $f[D]=E$, sobreyectividad. Si $a\ne c$ y $f(a)=f(c)$, tomando $A=\{a\}$, la salida común pertenece a $f[D\setminus A]$ por el testigo $c$ y también a $f[A]$, contradiciendo la igualdad con el complemento. Por tanto es inyectiva.

## 12.20. Seleccionar una partición

[]{#MA-EX-ANM-01-012-020}

[]{#MA-SOL-ANM-01-012-020}

Toda entrada tiene salida en alguna pieza, de modo que pertenece a alguna preimagen. Si pertenece a dos, su salida está en ambas piezas; la disjunción de las $B_i$ lo impide cuando los índices son distintos. Pero una pieza puede no contener salidas alcanzadas. Por ejemplo, para el cuadrado real, las piezas $(-\infty,0)$ y $[0,\infty)$ particionan $\mathbb R$ y la primera tiene preimagen vacía. Tras eliminar piezas vacías, las restantes sí particionan $D$ si éste no es vacío.

## 12.21. La última etapa se filtra primero

[]{#MA-EX-ANM-01-012-021}

[]{#MA-SOL-ANM-01-012-021}

[]{#MA-SEC-ANM-01-012-005}

Primero $1\le3-y<3$ equivale a $0<y\le2$, luego $g^{-1}[[1,3)]=(0,2]$. Después $0<x^2\le2$ da $[-\sqrt2,0)\cup(0,\sqrt2]$. Cero se excluye porque su salida compuesta es $3$; ambas raíces de dos se incluyen porque su salida es $1$.

## 12.22. Una composición sin tipo

[]{#MA-EX-ANM-01-012-022}

[]{#MA-SOL-ANM-01-012-022}

No: $f(1)=0$ no pertenece al dominio de $g$. Las entradas admisibles son $f^{-1}[\mathbb R\setminus\{0\}]=\mathbb R\setminus\{1\}$. Restringiendo $f$ a ese dominio, la composición válida es $h:\mathbb R\setminus\{1\}\to\mathbb R$, $h(x)=1/(x-1)$. Cada evaluación de la segunda etapa está ahora autorizada.

## 12.23. Dos identidades distintas

[]{#MA-EX-ANM-01-012-023}

[]{#MA-SOL-ANM-01-012-023}

Si $f(x)=f(z)$, aplicar $h$ y la primera identidad da $x=z$. Con la segunda, cada $y\in E$ tiene entrada $h(y)$ y $f(h(y))=y$. Para distinguirlas, sea $f:[0,\infty)\to\mathbb R$ la inclusión $f(x)=x$, y $h:\mathbb R\to[0,\infty)$, $h(y)=\max(y,0)$. Para $x\ge0$, $h(f(x))=x$. Pero $f(h(-1))=0\ne-1$, así que no hay segunda identidad y $f$ no es sobreyectiva.

## 12.24. Inversa sobre la imagen

[]{#MA-EX-ANM-01-012-024}

[]{#MA-SOL-ANM-01-012-024}

La asignación $\widetilde f:D\to f[D]$ es válida y mantiene inyectividad. Es sobreyectiva por definición de imagen: cada $y\in f[D]$ tiene una entrada. Luego tiene inversa $f[D]\to D$. Si hay $y\in E\setminus f[D]$, no existe entrada que alcance $y$, por lo que esa inversa no puede deshacer la asignación en tal salida. Ejemplo: inclusión $[0,\infty)\to\mathbb R$, cuya imagen es $[0,\infty)$.

## 12.25. La inversa de una composición

[]{#MA-EX-ANM-01-012-025}

[]{#MA-SOL-ANM-01-012-025}

La candidata $h=f^{-1}\circ g^{-1}:F\to D$ está tipada. Para $x\in D$, $h(g(f(x)))=f^{-1}(g^{-1}(g(f(x))))=f^{-1}(f(x))=x$. Para $z\in F$, $g(f(h(z)))=g(f(f^{-1}(g^{-1}(z))))=g(g^{-1}(z))=z$. Las dos identidades probadas en el texto garantizan biyectividad y unicidad de la inversa. El orden se invierte porque primero debe deshacerse la última etapa.

## 12.26. Imagen con orientación invertida

[]{#MA-EX-ANM-01-012-026}

[]{#MA-SOL-ANM-01-012-026}

[]{#MA-SEC-ANM-01-012-006}

De $-1\le x<2$, al multiplicar por $-3$ y sumar $2$, resulta $-4<h(x)\le5$. Para $t\in(-4,5]$, $x=(2-t)/3$ satisface $-1\le x<2$ y $h(x)=t$. La imagen es $(-4,5]$. El extremo abierto de entrada pasa a extremo inferior abierto, y el cerrado a superior cerrado.

## 12.27. Dos sentidos estrictos

[]{#MA-EX-ANM-01-012-027}

[]{#MA-SOL-ANM-01-012-027}

Para $x<y$ en $D$, $f(x)>f(y)$. Como $f(y)<f(x)$ y ambas salidas pertenecen a $E$, el decrecimiento estricto de $g$ da $g(f(y))>g(f(x))$. Así $(g\circ f)(x)<(g\circ f)(y)$. La compatibilidad de dominios permite aplicar la segunda hipótesis.

## 12.28. La inclusión de extremos puede ser propia

[]{#MA-EX-ANM-01-012-028}

[]{#MA-SOL-ANM-01-012-028}

El transporte por ramas da $[-2,0)\cup[1,3]$ y los valores extremos dan $[s(-2),s(2)]=[-2,3]$. Hay inclusión y es propia porque $1/2$ pertenece al segundo conjunto y no al primero. La prueba del crecimiento estricto en el texto incluye el caso que cruza cero; el hueco no lo contradice, pues crecimiento compara salidas existentes sin construir nuevas.

**Retorno visual.** Véase [C12-F04](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 12.29. Orden de la inversa

[]{#MA-EX-ANM-01-012-029}

[]{#MA-SOL-ANM-01-012-029}

Para $u<v$ en $E$, sean $x=f^{-1}(u)$, $y=f^{-1}(v)$. Si $x=y$, entonces $u=v$, imposible. Si $x>y$, crecimiento estricto da $u=f(x)>f(y)=v$, también imposible. Por tricotomía queda $x<y$. Así la inversa conserva el orden estricto en su propio dominio $E$.

## 12.30. Inyectividad no decide monotonía

[]{#MA-EX-ANM-01-012-030}

[]{#MA-SOL-ANM-01-012-030}

Intercambiamos $0$ y $1$ y fijamos todo otro real: $f(0)=1$, $f(1)=0$, $f(x)=x$ para $x\notin\{0,1\}$. Aplicarla dos veces devuelve cada entrada, así que es biyectiva. No es no decreciente porque $0<1$ pero $f(0)>f(1)$. No es no creciente porque $2<3$ y $f(2)<f(3)$. Reversibilidad y orden son propiedades independientes.

## 12.31. La mejor escala afín

[]{#MA-EX-ANM-01-012-031}

[]{#MA-SOL-ANM-01-012-031}

[]{#MA-SEC-ANM-01-012-007}

La identidad $|h(x)-h(y)|=|m||x-y|$ muestra que $|m|$ sirve. Si $L$ es otra cota, usamos $x=0$, $y=1$ y obtenemos $|m|\le L$. Vale también para $m=0$: la menor cota no negativa es cero. La traslación no influye en el resultado.

## 12.32. Una cota sin reversibilidad

[]{#MA-EX-ANM-01-012-032}

[]{#MA-SOL-ANM-01-012-032}

Si ambas entradas son no negativas, la distancia de salidas es $|x-y|$; si ambas son no positivas, es cero. Si $x<0<y$, es $y\le y-x=|x-y|$; el caso invertido es simétrico. Los extremos cero están incluidos en los primeros casos. Así la cota es $1$. Pero $f(-1)=f(-2)=0$, por lo que no es inyectiva.

## 12.33. La cota del cuadrado depende del radio

[]{#MA-EX-ANM-01-012-033}

[]{#MA-SOL-ANM-01-012-033}

La factorización del texto prueba la cota $2R$. Para refutar $0\le L<2R$, elegimos $t=\min(R,(2R-L)/2)>0$, $x=R$, $y=R-t\in[0,R)$. El cociente de distancias, permitido porque $t>0$, es $x+y=2R-t>L$: si $t=(2R-L)/2$, el resultado es $(2R+L)/2>L$; si $t=R$, esta rama exige $L\le0$ y, como $L\ge0$, $L=0<R$. Se viola la cota. Por tanto ninguna menor sirve.

## 12.34. Deshacer con control de distancia

[]{#MA-EX-ANM-01-012-034}

[]{#MA-SOL-ANM-01-012-034}

La cota inferior hace inyectiva a $f$, así que existe $h:f[D]\to D$. Para $u=f(x)$, $v=f(y)$, las desigualdades dan $c|h(u)-h(v)|\le|u-v|\le L|h(u)-h(v)|$. Dividiendo por constantes positivas, $(1/L)|u-v|\le|h(u)-h(v)|\le(1/c)|u-v|$. Todo par de la imagen tiene entradas únicas, así que las cotas cubren el dominio completo de $h$. No se exige sobreyectividad hacia el codominio original.

## 12.35. Cota compuesta con restricción

[]{#MA-EX-ANM-01-012-035}

[]{#MA-SOL-ANM-01-012-035}

$q$ tiene cota $4$ y $h$ tiene escala exacta $3$, luego la composición tiene cota $12$. Si $0\le L<12$, tomamos $t=\min(1,(12-L)/6)>0$, $x=2$, $y=2-t\in[1,2)$. El cociente de distancias de salidas es $3(x+y)=12-3t$. Como $t\le(12-L)/6$, ese valor es al menos $(12+L)/2>L$. Se contradice la cota $L$. Así $12$ es la menor.

## 12.36. Transportar el cuadrado entero

[]{#MA-EX-ANM-01-012-036}

[]{#MA-SOL-ANM-01-012-036}

[]{#MA-SEC-ANM-01-012-008}

La imagen es $P=\{(a,b):0\le b\le1,\ b\le a\le b+1\}$. Si $0\le u,v\le1$, entonces $b=v$ y $a=u+v$, de donde las desigualdades. Si $(a,b)\in P$, la entrada $(u,v)=(a-b,b)$ satisface $0\le u,v\le1$ y $T(u,v)=(a,b)$. Los vértices son los del paralelogramo mostrado en el texto; el argumento cubre también su interior y frontera.

**Retorno visual.** Véase [C12-F06](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 12.37. Una rejilla no es un grafo escalar

[]{#MA-EX-ANM-01-012-037}

[]{#MA-SOL-ANM-01-012-037}

Para $v=0$, $T(u,0)=(u,0)$, así que la imagen es la recta horizontal de pares $(a,0)$. Ese conjunto es el grafo de la función escalar $f:\mathbb R\to\mathbb R$, $f(a)=0$. Sin embargo, $T$ recibe pares $(u,v)$ y devuelve pares; $f$ recibe un real y devuelve cero. Su tipo, asignación y dominio difieren. Un mismo conjunto dibujado puede representar objetos en papeles distintos.

## 12.38. Ventana certificada para una afín

[]{#MA-EX-ANM-01-012-038}

[]{#MA-SOL-ANM-01-012-038}

Para $m\ne0$, la condición es $|m||x-x_0|<\rho$, por lo que la preimagen es $B(x_0,\rho/|m|)$. La inclusión de ventanas vale exactamente para $r\le\rho/|m|$: con esa condición todo punto de la bola menor satisface la desigualdad; si $r$ es mayor, la entrada $x=x_0+\rho/|m|$ está dentro de la primera bola pero su salida tiene distancia exactamente $\rho$, excluida de la segunda. Si $m=0$, la salida es siempre $c=f(x_0)$, la preimagen es toda $\mathbb R$ y cualquier $r>0$ sirve.

**Retorno visual.** Véase [C12-F07](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 12.39. Pertenencia sin vecindad

[]{#MA-EX-ANM-01-012-039}

[]{#MA-SOL-ANM-01-012-039}

$B(0,1/2)=(-1/2,1/2)$ contiene cero y no contiene uno. Por tanto la preimagen es $\{0\}$. Para cualquier $r>0$, el punto $r/2$ es distinto de cero y pertenece a $B(0,r)$, pero no a la preimagen. Ninguna bola positiva centrada en cero cabe en ella. Contener el centro no garantiza ser vecindad.

**Retorno visual.** Véase [C12-F07](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 12.40. Reconstruir imagen desde todas las selecciones

[]{#MA-EX-ANM-01-012-040}

[]{#MA-SOL-ANM-01-012-040}

Por la equivalencia del manuscrito, la segunda condición equivale a $f[A]\subseteq B$. Así $C$ y $f[A]$ tienen exactamente los mismos conjuntos que los contienen. Tomando $B=C$, la inclusión $C\subseteq C$ implica $f[A]\subseteq C$. Tomando $B=f[A]$, la inclusión $f[A]\subseteq f[A]$ implica $C\subseteq f[A]$. Las dos inclusiones dan igualdad. La caracterización recupera el transporte hacia delante a partir de su relación con todas las selecciones hacia atrás, incluidos los casos vacíos.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 12](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html) · [Ejercicios](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-microcontroles.html)
