---
content-id: MA-BCH-0284
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-020-SOLUCIONES
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
title: Soluciones — Capítulo 20
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C20_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Ejercicios](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html)

## 20.1. La diferencia exacta de una cuerda

[]{#MA-EX-ANM-01-020-001}

[]{#MA-SOL-ANM-01-020-001}

[]{#MA-SEC-ANM-01-020-001}

Expandimos $z^2=(1-t)^2a^2+2t(1-t)ab+t^2b^2$. Restar de $(1-t)a^2+tb^2$ deja $t(1-t)(a^2-2ab+b^2)=t(1-t)(b-a)^2$. En $0\le t\le1$ es no negativa y prueba convexidad en toda la recta. Se anula exactamente si $t=0$, $t=1$ o $a=b$. Cuando $0<t<1$ y $a\ne b$ es positiva, por lo que la convexidad es estricta.

El cálculo da una identidad para todos los pesos de la definición, no sólo una comparación en el punto medio. La positividad de cada factor determina estrictitud y la anulación identifica los casos triviales. Así la misma expansión acredita convexidad débil, estricta y sus igualdades sin utilizar derivadas.

## 20.2. Una esquina bajo sus cuerdas

[]{#MA-EX-ANM-01-020-002}

[]{#MA-SOL-ANM-01-020-002}

Para pesos no negativos, la triangular da $|(1-t)a+tb|\le|(1-t)a|+|tb|=(1-t)|a|+t|b|$. Vale para todas las entradas y pesos de la definición. Entre $a=1$ y $b=2$, la función es $x$, de modo que cualquier peso interior da igualdad; falla convexidad estricta. En cero, el cociente $|h|/h$ es1 para $h>0$ y−1 para $h<0$. Sus límites laterales distintos excluyen derivada bilateral. Es una función convexa continua con esquina, no una excepción a la definición.

**Retorno visual.** Véase [C20-F01](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Los pesos no negativos permiten sacar sus factores de los valores absolutos sin cambiar signo. El tramo positivo afín proporciona un par que refuta estrictitud, mientras las secantes de ambos lados de cero refutan derivabilidad. Son dos fallos distintos que no afectan la desigualdad convexa ya demostrada.

## 20.3. Sumar sin invertir el orden

[]{#MA-EX-ANM-01-020-003}

[]{#MA-SOL-ANM-01-020-003}

Aplicamos convexidad de cada función en $z=(1-t)a+tb$, multiplicamos por $\alpha,\beta$ no negativos y sumamos. La salida queda acotada por la combinación de salidas de $\alpha f+\beta g$. La recta satisface igualdad en cada combinación, por lo que sumarla conserva la diferencia de convexidad de $f$. Un coeficiente negativo invierte la comparación: con $f=x^2$ y $\alpha=-1$, en $a=-1$, $b=1$, $t=1/2$ la salida de $-f$ es0 y la media de salidas es−1. La desigualdad $0\le-1$ es falsa.

La suma de desigualdades conserva el control porque sus coeficientes no invierten el orden. Agregar una afín contribuye con igualdad y deja intacta la diferencia convexa. El ejemplo negativo elimina exactamente esa condición de signo. No demuestra que ninguna combinación con coeficiente negativo pueda ser convexa, sino que se pierde la garantía universal.

## 20.4. Una subida que no decide curvatura

[]{#MA-EX-ANM-01-020-004}

[]{#MA-SOL-ANM-01-020-004}

El cuadrado es estrictamente convexo por E001. No es no decreciente en toda la recta: $-2<-1$ pero4>1. El cubo es estrictamente creciente porque, para $x<y$, $y^3-x^3=(y-x)(x^2+xy+y^2)>0$; el segundo factor sólo podría ser cero si ambos fueran cero, imposible con $x<y$. No es convexo en toda la recta: para entradas−2 y0 y peso1/2, la salida en−1 es−1, mayor que la media−4. Monotonía ordena dos salidas; convexidad compara una salida intermedia con una altura interpolada.

En el cuadrado, alturas decrecientes del lado negativo conviven con convexidad estricta. En el cubo, el crecimiento de todos los pares convive con una comparación de cuerda que falla. Las identidades y el contraejemplo de valores bastan para separar propiedades, sin usar un criterio diferencial futuro.

## 20.5. Supremo de curvas convexas

[]{#MA-EX-ANM-01-020-005}

[]{#MA-SOL-ANM-01-020-005}

Para cada $j$, $f_j(z)\le(1-t)f_j(a)+tf_j(b)\le(1-t)F(a)+tF(b)$, porque los pesos son no negativos. El lado derecho es una cota superior real común; tomar el supremo de los valores en $z$ produce $F(z)\le(1-t)F(a)+tF(b)$. La familia no vacía permite el supremo real de un conjunto de valores no vacío y la hipótesis de finitud evita un valor infinito fuera del codominio declarado. No se exige que un índice alcance el supremo. Las rectas son un caso particular.

Para cada índice se obtiene la misma cota superior en la entrada combinada, formada con los dos supremos de borde. El supremo de valores allí no puede superar esa cota. La prueba no supone un índice que maximice cada altura ni reúne elecciones de índices para las entradas. La finitud declarada mantiene la función resultante con valores reales.

## 20.6. Reconstruir la cuerda desde pendientes

[]{#MA-EX-ANM-01-020-006}

[]{#MA-SOL-ANM-01-020-006}

[]{#MA-SEC-ANM-01-020-002}

Multiplicamos por $(v-u)(w-v)>0$: $(w-v)(f(v)-f(u))\le(v-u)(f(w)-f(v))$. Agrupar $f(v)$ da $(w-u)f(v)\le(w-v)f(u)+(v-u)f(w)$. Dividir por $w-u$ da la cuerda en $v$, con pesos positivos que suman1. A su vez $S(u,w)=[(v-u)S(u,v)+(w-v)S(v,w)]/(w-u)$; una media con pesos positivos de dos valores ordenados está entre ellos. Por ello $S(u,v)\le S(u,w)\le S(v,w)$.

Las longitudes de los dos tramos son estrictamente positivas y legitiman todas las multiplicaciones y divisiones. El reordenamiento produce exactamente los pesos de la entrada intermedia. La secante larga es una media de las cortas y conserva su banda. Esta equivalencia es algebraica y no requiere derivadas.

## 20.7. Tres pendientes del cuadrado

[]{#MA-EX-ANM-01-020-007}

[]{#MA-SOL-ANM-01-020-007}

Para el cuadrado, $(v^2-u^2)/(v-u)=u+v$ cuando $u<v$. Las pendientes cortas son $S(0,1)=1$ y $S(1,3)=4$; la larga es $S(0,3)=3$. Se obtiene1<3<4. La media ponderada es $(1/3)1+(2/3)4=3$. La desigualdad estricta concuerda con convexidad estricta; una secante larga no toma por definición la pendiente de una de sus piezas.

**Retorno visual.** Véase [C20-F02](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Cancelar la diferencia de entradas exige extremos distintos, cumplido en las tres secantes. Las longitudes uno y dos se convierten en pesos un tercio y dos tercios para la larga. El resultado tres queda estrictamente entre uno y cuatro. Esa cuenta muestra por qué una secante larga no coincide necesariamente con ninguna de sus partes.

## 20.8. Una igualdad que se propaga

[]{#MA-EX-ANM-01-020-008}

[]{#MA-SOL-ANM-01-020-008}

Ponemos $h=\ell-f$. Es cóncava, no negativa por la cuerda y nula en $a,z,b$. Para $a<x<z$, escribimos $z=\theta x+(1-\theta)b$, con $\theta=(b-z)/(b-x)>0$. Concavidad da $0=h(z)\ge\theta h(x)$, así $h(x)=0$. Para $z<x<b$, escribimos $z=(1-\eta)a+\eta x$, con $\eta=(z-a)/(x-a)>0$ y obtenemos $0\ge\eta h(x)$, de nuevo $h(x)=0$. La no negatividad descarta valores negativos y los puntos restantes ya eran ceros. La igualdad interior ha forzado un tramo afín completo.

La cuerda ya aporta $h\ge0$ y la concavidad proporciona la desigualdad que propaga el contacto. Cada punto no central se relaciona con el contacto mediante el borde opuesto. Como su peso es positivo, una altura positiva sería incompatible con el cero de la combinación. Se concluye igualdad en todo el segmento, no fuera de él.

## 20.9. Cero curvatura en una pieza

[]{#MA-EX-ANM-01-020-009}

[]{#MA-SOL-ANM-01-020-009}

Tomamos $f(x)=\max\{0,x\}$. Es convexa como supremo finito de las rectas0 y $x$ por E005. En $[1,3]$ coincide con $x$, y en2 hay igualdad con la cuerda. No es afín en toda la recta: es0 para entradas negativas y $x$ para positivas. E008 fuerza afinidad sólo en el segmento cuyos bordes e igualdad se fijaron, aquí $[1,3]$. No propaga la recta fuera de ese segmento.

Las dos rectas son una familia finita no vacía con supremo real en cada entrada. En la pieza positiva su máximo es la identidad y produce las igualdades pedidas. En la negativa es la constante cero, incompatible con una única regla afín global. La rigidez de una cuerda sólo utiliza el segmento cuyos datos se han fijado.

## 20.10. Sin tramo recto, con desigualdad estricta

[]{#MA-EX-ANM-01-020-010}

[]{#MA-SOL-ANM-01-020-010}

Si es estrictamente convexa, una afinidad en un segmento no degenerado daría igualdad en cualquier combinación interior de sus bordes, contradicción. Para la otra dirección, si falla convexidad estricta, existen $a\ne b$ y un peso interior con igualdad: la convexidad débil ya excluye que el signo sea el contrario. Ordenamos $a,b$; la entrada combinada queda interior. E008 hace afín todo ese subsegmento. Contradice la ausencia de tramos afines. Las combinaciones triviales no intervienen.

La dirección recíproca parte de convexidad débil, que impide una desigualdad contraria. Un fallo de estrictitud interior debe por ello ser igualdad, y la rigidez la convierte en afinidad del tramo. La ausencia de tramos afines descarta ese caso. Los pesos extremos y entradas repetidas se excluyen porque siempre producen igualdad.

## 20.11. Un radio construido con secantes

[]{#MA-EX-ANM-01-020-011}

[]{#MA-SOL-ANM-01-020-011}

[]{#MA-SEC-ANM-01-020-003}

Para $c\le x<y\le d$, la regla de triples da $S(a,c)\le S(a,x)\le S(x,y)\le S(y,b)\le S(d,b)$. Con $L=\max\{|S(a,c)|,|S(d,b)|\}$ resulta $|S(x,y)|\le L$, luego $|f(y)-f(x)|\le L|y-x|$. Entradas iguales dan incremento cero y entradas invertidas se cubren por simetría. Si $L>0$, tomamos $\delta=\varepsilon/L$; si $L=0$, la función es constante en el segmento y cualquier radio positivo sirve. Los puntos exteriores son la hipótesis que mantiene finitas las cotas.

La cadena de secantes usa centros exteriores a la región que se controla y conserva sus barreras al mover $x,y$. Si algún centro coincide con $c$ o $d$, la comparación correspondiente es igualdad y se omite el triple degenerado. La banda finita da un control para todos los pares y su radio uniforme. No se utiliza una cota de derivadas para fabricar continuidad.

## 20.12. Dos pendientes laterales en una esquina

[]{#MA-EX-ANM-01-020-012}

[]{#MA-SOL-ANM-01-020-012}

Para $x<0$, $S(x,0)=(0-|x|)/(0-x)=-1$, así el supremo izquierdo es−1. Para $y>0$, $S(0,y)=1$, así el ínfimo derecho es1. Las pendientes laterales difieren y no existe derivada bilateral. La triangular aplicada a $x=(x-y)+y$ y luego con $x,y$ intercambiados da $||x|-|y||\le|x-y|$. Es Lipschitz con constante1 en toda la recta, y por ello continua incluso en la esquina.

**Retorno visual.** Véase [C20-F03](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las dos familias laterales son constantes y sus cotas óptimas se alcanzan en toda entrada de su lado. Sus valores diferentes impiden un único límite bilateral. La desigualdad triangular inversa controla en cambio todas las diferencias de valores, incluida la esquina. Esto distingue continuidad y Lipschitz de existencia de derivada.

## 20.13. Una discontinuidad convexa de borde

[]{#MA-EX-ANM-01-020-013}

[]{#MA-SOL-ANM-01-020-013}

Para cualquier combinación de dos entradas no negativas, si la entrada combinada es positiva la salida es0 y la media de salidas es no negativa. Si la combinación es cero, todas las entradas con peso positivo son cero y la media de salidas vale1, igual que la salida. Esto prueba convexidad para todos los pesos. La sucesión positiva $1/(n+1)$ tiene salidas0 y converge a cero, cuya salida es1; no hay continuidad en ese borde. En cada punto interior la función es constante en un radio pequeño y continua. La continuidad interior de una función convexa finita no incluye automáticamente la frontera.

Una combinación no negativa sólo puede ser cero si todas sus entradas activas son cero. Ese caso preserva exactamente la altura excepcional del borde. Las entradas positivas próximas refutan continuidad allí sin alterar convexidad. La conclusión de continuidad para convexas finitas se mantiene en los centros interiores que tienen margen por ambos lados.

## 20.14. El supremo convertido en límite

[]{#MA-EX-ANM-01-020-014}

[]{#MA-SOL-ANM-01-020-014}

Hay entradas a ambos lados de $c$. Una secante derecha fija acota todas las secantes izquierdas por la regla de triples, y una secante izquierda fija muestra que el conjunto no es vacío y da una cota inferior a su supremo. La completitud proporciona $A\in\mathbb R$. Para $\varepsilon>0$, elegimos $x_0<c$ con $A-\varepsilon<S(x_0,c)\le A$. Si $x_0<x<c$, la monotonía de secantes con extremo fijo da $A-\varepsilon<S(x_0,c)\le S(x,c)\le A$. El radio $c-x_0$ produce la condición de límite izquierdo. El cociente de derivada para incremento negativo es precisamente $S(x,c)$.

La secante derecha fija aporta una cota superior a todo el conjunto izquierdo, y un miembro izquierdo acredita no vacuidad. El supremo real existe por completitud. Su propiedad aproximante y el orden de secantes permiten diseñar un radio a partir de un solo testigo. No se supone que el supremo sea una pendiente alcanzada ni se selecciona una ruta.

## 20.15. Ni constante global ni borde protegido

[]{#MA-EX-ANM-01-020-015}

[]{#MA-SOL-ANM-01-020-015}

Si el cuadrado tuviera constante global $L$, comparar0 y $x>0$ daría $x^2\le Lx$ y por tanto $x\le L$ para todos los positivos, imposible tomando $x>L$. Para el borde, $f(x)=-\sqrt{x}$ es convexa continua en $[0,1]$: sobre el interior su segunda derivada es positiva según20.6, y continuidad permite extender convexidad a los bordes por20.5. Si fuera Lipschitz con constante $L$, comparar0 con $x>0$ daría $1/\sqrt{x}\le L$, imposible cerca de cero. No se usa este ejemplo como premisa de la prueba temprana de continuidad; se verifica con herramientas ya disponibles.

El control local interior puede cambiar de constante al cambiar la región y no da una constante para toda la recta. Cerca de un borde, incluso continuidad no asegura una banda de secantes finita. Los dos ejemplos infringen barreras propuestas con pares válidos. Usar después criterios diferenciales para verificar el segundo ejemplo no los convierte en premisas de la prueba temprana.

## 20.16. Todas las rectas que sostienen la esquina

[]{#MA-EX-ANM-01-020-016}

[]{#MA-SOL-ANM-01-020-016}

[]{#MA-SEC-ANM-01-020-004}

Para $x>0$, dividir por $x$ exige $p\le1$. Para $x<0$, la desigualdad $px\le-x$ y la división negativa exigen $p\ge-1$. En cero siempre hay igualdad. A la inversa, si $-1\le p\le1$, estas dos condiciones prueban el soporte en ambas mitades. Las pendientes laterales son−1 y1, así se recupera exactamente su intervalo cerrado. Las rectas pasan por el centro y son soportes, aunque no haya derivada bilateral.

Dividir por entradas negativas invierte el orden y produce la restricción inferior de pendiente. En las positivas la división conserva el orden y produce la superior. El centro cero tiene igualdad sin formar un cociente. Ambas condiciones reunidas dan exactamente el intervalo de soportes, aunque no exista tangente bilateral.

## 20.17. Una familia que envuelve el cuadrado

[]{#MA-EX-ANM-01-020-017}

[]{#MA-SOL-ANM-01-020-017}

La identidad $x^2-2cx+c^2=(x-c)^2\ge0$ da $2cx-c^2\le x^2$ para todo $c$. La familia es no vacía y está acotada superiormente por el real $x^2$, así tiene supremo real. El centro $c=x$ produce el valor $2x^2-x^2=x^2$. Por tanto el supremo coincide con $x^2$. Las rectas son las tangentes y soportes globales del cuadrado. La igualdad se prueba para cada $x$, no a partir de una colección finita dibujada.

**Retorno visual.** Véase [C20-F04](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La diferencia cuadrática prueba una cota común para toda la familia de rectas. Luego una recta del propio centro $c=x$ alcanza esa cota y acredita la igualdad del supremo. Un dibujo con algunas tangentes sólo representaría parte de la familia. La fórmula verifica el resultado para todas las entradas y centros reales.

## 20.18. Por qué el soporte invierte un signo

[]{#MA-EX-ANM-01-020-018}

[]{#MA-SOL-ANM-01-020-018}

Si $A\le p\le B$, para $x>c$ usamos $S(c,x)\ge B\ge p$ y multiplicamos por $x-c>0$. Para $x<c$, usamos $S(x,c)\le A\le p$ y multiplicamos por $x-c<0$, invirtiendo el orden. En ambos casos $f(x)\ge f(c)+p(x-c)$; en el centro hay igualdad. Recíprocamente, el soporte dividido a la derecha obliga a $p\le S(c,x)$ para todos los $x>c$, luego $p\le B$. A la izquierda obliga a $S(x,c)\le p$ para todos los $x<c$, luego $A\le p$. Ambas orientaciones son necesarias.

El lado izquierdo y el derecho exigen orientaciones distintas al pasar de pendientes a alturas. El supremo izquierdo es la menor cota superior y el ínfimo derecho la mayor cota inferior de sus familias. Por ello las comparaciones para todas las entradas equivalen a $A\le p\le B$. La prueba verifica necesidad y suficiencia, con igualdad directa en el centro.

## 20.19. Un borde sin soporte finito

[]{#MA-EX-ANM-01-020-019}

[]{#MA-SOL-ANM-01-020-019}

Una recta por el origen sería $px$. El soporte exigiría $px\le-\sqrt{x}$ para cada $x>0$, y al dividir por $x$ daría $p\le-1/\sqrt{x}$. Dado un real $p$, podemos tomar $x>0$ suficientemente pequeño para que $-1/\sqrt{x}<p$, contradicción. La función es convexa y continua por E015. La construcción de soportes con pendientes finitas requería un centro interior con entradas por ambos lados; cero es frontera y queda fuera de esa conclusión.

Para cualquier pendiente candidata, las secantes desde el borde toman valores arbitrariamente negativos. Por tanto ninguna recta finita puede mantenerse por debajo cerca de cero. La continuidad de valores no limita esa razón por la distancia de entrada. El teorema de soportes finitos se formuló para centros interiores y no incluye esa frontera.

## 20.20. Un segundo contacto fuerza una pieza recta

[]{#MA-EX-ANM-01-020-020}

[]{#MA-SOL-ANM-01-020-020}

En una entrada $z=(1-t)a+tb$, convexidad da $f(z)\le(1-t)f(a)+tf(b)=(1-t)\ell(a)+t\ell(b)=\ell(z)$. El soporte da la desigualdad opuesta, de modo que hay igualdad en cada entrada del segmento. Para una función estrictamente convexa, dos contactos distintos crearían un tramo afín no degenerado, imposible por E010. La tangente en un centro derivable ya es soporte y tiene al menos su contacto central; no puede tener otro.

El soporte aporta una cota inferior en la entrada combinada y la cuerda una superior con la misma recta, pues comparten sus bordes. Ambas obligan a igualdad. Dos contactos de una convexa estricta crearían así un tramo afín prohibido. En el caso derivable, la tangente ya tiene su contacto central y sólo puede tener ése.

## 20.21. Dos centros en segmentos vecinos

[]{#MA-EX-ANM-01-020-021}

[]{#MA-SOL-ANM-01-020-021}

[]{#MA-SEC-ANM-01-020-005}

Fijamos $u<v<w$. Ambos segmentos $[u,v]$ y $[v,w]$ están en el dominio por carácter intervalar. La función es derivable en sus interiores y continua en sus bordes por derivabilidad en el intervalo abierto. Lagrange da $c\in(u,v)$ y $d\in(v,w)$ con $S(u,v)=f\prime(c)$ y $S(v,w)=f\prime(d)$. Como $c<d$, el orden de $f\prime$ da $S(u,v)\le S(v,w)$. E006 recupera convexidad en cada entrada intermedia. No pedimos continuidad de $f\prime$ ni un mismo testigo para las dos instancias.

La derivabilidad en el intervalo abierto garantiza continuidad en los extremos de ambos subsegmentos, además de sus derivadas interiores. La ubicación de los testigos, uno antes y otro después de $v$, permite aplicar el orden de la derivada. Así se recupera la comparación de secantes que caracteriza convexidad. No se necesita continuidad de la función derivada.

## 20.22. Orden de derivadas sin orden de valores

[]{#MA-EX-ANM-01-020-022}

[]{#MA-SOL-ANM-01-020-022}

La derivada es $2x$, estrictamente creciente en toda la recta.20.5 certifica convexidad estricta. Sus valores son negativos para $x<0$ y positivos para $x>0$, así C19 hace decreciente al cuadrado en $(-\infty,0]$ y creciente en $[0,\infty)$, estrictamente en pares distintos de cada tramo. Por ejemplo, $f(-2)=4>f(-1)=1$. El orden de la derivada compara pendientes entre centros; su signo decide dirección de los incrementos de la función.

**Retorno visual.** Véase [C20-F05](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La pendiente $2x$ tiene orden estricto entre centros, pero su signo cambia en cero. El primer hecho prueba convexidad estricta y el segundo determina las dos zonas de monotonía. Para pares que incluyen cero se utiliza valor medio con centro interior de signo estricto en su tramo. No hay crecimiento global del cuadrado.

## 20.23. Un plateau de derivadas destruye lo estricto

[]{#MA-EX-ANM-01-020-023}

[]{#MA-SOL-ANM-01-020-023}

Por20.5 la derivada no decrece, por lo que $k=f\prime(x)\le f\prime(t)\le f\prime(y)=k$ para cada $x<t<y$. Así $f\prime(t)=k$. La función $f(t)-kt$ es continua sobre el segmento y tiene derivada interior cero; la constancia de C19 la hace constante allí. Resulta $f(t)=kt+A$ en $[x,y]$. Si $f$ fuera estrictamente convexa, este tramo afín sería imposible. Por ello la derivada de una función estrictamente convexa derivable debe ser estrictamente creciente; la recíproca se prueba con los dos centros ordenados de E021.

El orden de la derivada encierra sus valores intermedios entre dos iguales y los fija en $k$. Restar la recta de pendiente $k$ produce derivada cero y permite aplicar constancia sobre el segmento. La pieza afín contradice estrictitud. El criterio recíproco usa centros de Lagrange estrictamente ordenados y conserva la desigualdad estricta de secantes.

## 20.24. Tangentes que prueban convexidad

[]{#MA-EX-ANM-01-020-024}

[]{#MA-SOL-ANM-01-020-024}

Para $a<b$ y $0<t<1$, sea $z=(1-t)a+tb\in I$. El soporte en $z$ da $f(a)\ge f(z)+f\prime(z)(a-z)$ y $f(b)\ge f(z)+f\prime(z)(b-z)$. Multiplicamos por $1-t$ y $t$ y sumamos. El término de pendiente es $f\prime(z)((1-t)(a-z)+t(b-z))=0$. Entonces $(1-t)f(a)+tf(b)\ge f(z)$. Para pesos extremos o entradas coincidentes hay igualdad. Se gastó el soporte en todas las entradas, no sólo en un radio vecinal.

El soporte se utiliza en el centro combinado $z$ y se evalúa en ambos bordes. Al sumar con pesos positivos desaparecen los incrementos dirigidos porque su combinación es cero. La conclusión es exactamente la comparación de cuerda. Un control sólo local de tangentes no proporcionaría necesariamente esas dos evaluaciones de soporte global.

## 20.25. La derivada interior no arregla el borde

[]{#MA-EX-ANM-01-020-025}

[]{#MA-SOL-ANM-01-020-025}

En cualquier centro interior hay un radio donde $f=0$, así $f\prime=0$ en todo $(0,1)$ y no decrece. Pero la cuerda entre0 y1 tiene altura−1/2 en1/2, mientras $f(1/2)=0$. La desigualdad convexa $0\le-1/2$ falla. Falta continuidad en el borde0. El criterio sobre un intervalo abierto no incluía ese borde; su extensión a un segmento cerrado exigía continuidad de $f$ en ambos extremos.

Modificar el borde no afecta las derivadas en centros interiores, que siguen siendo cero. Pero cambia la cuerda que incluye ese borde y su altura cae por debajo del valor interior. La falta de continuidad impide extender el criterio abierto al segmento cerrado. El ejemplo conserva orden de derivadas y muestra el gasto de la hipótesis de borde.

## 20.26. Dos derivadas, una equivalencia

[]{#MA-EX-ANM-01-020-026}

[]{#MA-SOL-ANM-01-020-026}

[]{#MA-SEC-ANM-01-020-006}

Si $f\prime\prime\ge0$, aplicamos C19 a $f\prime$: es derivable y por ello continua en cada segmento interior. El signo de su derivada hace a $f\prime$ no decreciente y20.5 hace convexa a $f$. Si $f$ es convexa,20.5 hace a $f\prime$ no decreciente. En un centro donde es derivable, el cociente de $f\prime$ es no negativo para incrementos positivos; también para negativos, pues numerador y denominador son no positivos. El límite $f\prime\prime$ es no negativo. Ninguna dirección utiliza continuidad de $f\prime\prime$.

La segunda derivada se entiende como derivada de la primera en todos los centros del intervalo. Eso permite aplicar el resultado de signo a la primera función y después el criterio convexo. En la dirección opuesta, el orden de una primera derivada convexa obliga a que su derivada existente sea no negativa. Ningún paso requiere continuidad de la segunda derivada.

## 20.27. Convexidad estricta con segunda derivada nula

[]{#MA-EX-ANM-01-020-027}

[]{#MA-SOL-ANM-01-020-027}

Las reglas de C18 dan $f\prime=4x^3$ y $f\prime\prime=12x^2$. El cubo es estrictamente creciente por la identidad de E004, de modo que $4x^3$ también lo es.20.5 da convexidad estricta. Sin embargo $f\prime\prime(0)=0$. La condición positiva en todos los centros es suficiente, pero no necesaria; el criterio débil sigue verificándose en toda la recta.

**Retorno visual.** Véase [C20-F06](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La estrictitud procede del orden estricto de $4x^3$, probado con pares y no de una segunda derivada positiva en cada punto. La segunda derivada $12x^2$ mantiene el signo débil y se anula en cero. Ese centro no produce un tramo afín. Por ello la anulación puntual no destruye convexidad estricta.

## 20.28. Recíproco y raíz: dos direcciones

[]{#MA-EX-ANM-01-020-028}

[]{#MA-SOL-ANM-01-020-028}

Para el recíproco, las reglas de cociente dan $f\prime=-1/x^2<0$ y $f\prime\prime=2/x^3>0$: es estrictamente decreciente y estrictamente convexa en $(0,\infty)$. Para la raíz, C18 da $g\prime=1/(2\sqrt{x})>0$. Derivamos el recíproco de $2\sqrt{x}$: $g\prime\prime=-(1/\sqrt{x})/(4x)=-1/(4x^{3/2})<0$. Es creciente y estrictamente cóncava en el interior. La raíz es continua en cero por C10/C14. Aplicamos el criterio de borde para $-g$ sobre cada $[0,b]$, o pasamos al límite en desigualdades interiores. No afirmamos una segunda derivada finita en cero.

Todas las divisiones se realizan en centros positivos, donde las raíces y potencias de denominador son no nulas. El signo de la primera derivada decide monotonía y el de la segunda orden de pendientes. La continuidad de la raíz en cero permite pasar a la comparación de borde. No se aplica allí una fórmula de segunda derivada que carecería de valor finito.

## 20.29. Una muestra de curvatura no basta

[]{#MA-EX-ANM-01-020-029}

[]{#MA-SOL-ANM-01-020-029}

Tenemos $q\prime\prime(x)=2-12x^2$, así $q\prime\prime(0)=2>0$ y $q\prime\prime(1)=-10<0$. Como es dos veces derivable en toda la recta, la necesidad de20.6 excluye convexidad global. Un signo central no reemplaza el signo en todos los puntos. Para la segunda pregunta, $x^4$ tiene segunda derivada0 en el origen y conserva convexidad a ambos lados; $x^3$ también tiene segunda derivada0 allí pero $6x$ cambia de signo y sus dos lados tienen concavidades opuestas. El valor nulo por sí solo no decide el fenómeno.

El criterio requiere el signo de curvatura en todo el intervalo y el valor negativo en uno basta para refutar esa premisa global. Una evaluación positiva en cero no la repone. Para curvatura nula, los dos polinomios comparados muestran comportamientos vecinos diferentes. El fenómeno de cambio de convexidad necesita información a ambos lados y no una cifra aislada.

## 20.30. Existencia, frontera y soporte horizontal

[]{#MA-EX-ANM-01-020-030}

[]{#MA-SOL-ANM-01-020-030}

(i) El soporte en $c$ es horizontal, de modo que $f(x)\ge f(c)$ para todas las entradas: el mínimo existe porque ya tenemos $c$. Si la convexidad es estricta, la desigualdad es estricta para toda entrada distinta y el mínimo es único. (ii) La identidad es afín y su mínimo único está en el borde0; tiene derivada relativa1, así la condición necesaria de Fermat interior no aplica. (iii) El cuadrado es estrictamente convexo y todas sus salidas son positivas; para cualquier entrada $x$ la entrada $x/2$ tiene menor salida. No hay mínimo alcanzado, aunque el ínfimo sea0. La convexidad no fabrica una entrada estacionaria.

Un centro estacionario interior ya proporciona una entrada y su soporte horizontal acredita el mínimo global. Estrictitud asegura unicidad si ese mínimo existe. En una frontera puede haber mínimo sin pendiente relativa cero, y en un intervalo abierto puede faltar por completo el minimizador. Existencia, ubicación y unicidad responden a hipótesis diferentes.

## 20.31. El peso nulo en la inducción

[]{#MA-EX-ANM-01-020-031}

[]{#MA-SOL-ANM-01-020-031}

[]{#MA-SEC-ANM-01-020-007}

Para una entrada hay igualdad. En el paso, sea $s=1-\lambda_n$. Si $s=0$, todos los pesos anteriores son cero y sólo se evalúa $x_n$. Si $\lambda_n=0$, aplicamos la hipótesis inductiva a los primeros pesos, que ya suman1. Si $0<s<1$, la media $y=\sum_{i<n}(\lambda_i/s)x_i$ pertenece al intervalo por inducción de combinaciones y $f(y)\le\sum_{i<n}(\lambda_i/s)f(x_i)$. Convexidad entre $y$ y $x_n$ con pesos $s,1-s$ y multiplicación de la cota por $s>0$ dan la desigualdad de $n$ entradas. No se normaliza un grupo de peso cero.

La inducción tiene un caso base no vacío y separa los pesos extremos antes de normalizar. Con un grupo de peso positivo, sus proporciones suman uno y su media permanece en el intervalo. La combinación final utiliza convexidad de dos entradas y el control inductivo del grupo. La finitud asegura que el procedimiento reduce efectivamente la lista.

## 20.32. Igualdad con entradas inactivas

[]{#MA-EX-ANM-01-020-032}

[]{#MA-SOL-ANM-01-020-032}

Los pesos cero se eliminan sin cambiar media ni salida. Si todas las entradas restantes coinciden, hay igualdad. Si difieren, agrupamos las entradas activas de valor mínimo con peso total $\theta$. Hay al menos una entrada mayor, por lo que $0<\theta<1$, y la media $y$ de las restantes es estrictamente mayor que el mínimo. La convexidad estricta entre ambos valores da una desigualdad estricta; Jensen en los grupos acota las salidas sin cambiar ese signo. Por tanto la desigualdad total es estricta. La igualdad exige que las entradas con peso positivo sean iguales; las inactivas son libres.

Retirar los pesos nulos deja exactamente la misma media y combinación de salidas. Si las entradas activas difieren, el grupo de valor mínimo y el resto tienen pesos totales estrictamente entre cero y uno. La media del resto es mayor y la comparación estricta entre ambos valores se conserva al usar Jensen dentro del grupo. Esto demuestra necesidad de coincidencia de todas las entradas activas.

## 20.33. Una diferencia de diecinueve dieciseisavos

[]{#MA-EX-ANM-01-020-033}

[]{#MA-SOL-ANM-01-020-033}

La media es $\mu=0+1/2+3/4=5/4$. La media de cuadrados es $0+1/2+9/4=11/4$. Restar $\mu^2=25/16$ deja $44/16-25/16=19/16$. La suma de desviaciones es $(1/4)(25/16)+(1/2)(1/16)+(1/4)(49/16)=25/64+2/64+49/64=76/64=19/16$. La identidad proviene de expandir los cuadrados y usar las dos relaciones de pesos y media; la cuenta ejemplifica una prueba universal.

**Retorno visual.** Véase [C20-F07](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La identidad general se obtiene expandiendo $(x_i-\mu)^2$ y usando $\sum\lambda_i=1$ y $\sum\lambda_i x_i=\mu$. La cuenta exacta muestra que los dos modos de evaluar dan alturas diferentes. Su diferencia es una suma no negativa de desviaciones y aquí es positiva porque hay entradas activas distintas.

## 20.34. Una desigualdad sin logaritmos

[]{#MA-EX-ANM-01-020-034}

[]{#MA-SOL-ANM-01-020-034}

La función $1/x$ es estrictamente convexa en $(0,\infty)$ por E028. Con pesos iguales $1/n$, la media $\mu=(\sum_i x_i)/n$ es positiva y Jensen da $1/\mu\le(1/n)\sum_i1/x_i$. Como $1/\mu=n/\sum_i x_i$, multiplicamos por $n\sum_i x_i>0$ y obtenemos $n^2\le(\sum_i x_i)(\sum_i1/x_i)$. Todos los pesos son positivos, así E032 dice que la igualdad ocurre exactamente cuando las entradas son todas iguales. Para $n=1$ esa condición es automática.

La media positiva pertenece al dominio del recíproco y todas las multiplicaciones usadas para despejar conservan el orden. Los pesos iguales son positivos, así la igualdad estrictamente convexa obliga a igualdad de todas las entradas. El caso de una sola entrada cumple la condición automáticamente. No se utiliza logaritmo ni una regla ajena a Jensen.

## 20.35. Una suma de pesos que no protege el signo

[]{#MA-EX-ANM-01-020-035}

[]{#MA-SOL-ANM-01-020-035}

Con entradas0 y1, la combinación es−1 y su cuadrado vale1. La media de cuadrados es $2\cdot0-1\cdot1=-1$, así la desigualdad pedida sería $1\le-1$, falsa. Los pesos suman1 pero uno es negativo. El paso de convexidad de dos entradas sólo admite pesos entre0 y1; además multiplicar cotas por un peso negativo invierte el orden. Jensen requería pesos no negativos, de modo que la construcción muestra necesidad de esa condición, no una falla del teorema.

El contraejemplo mantiene suma uno pero pierde no negatividad. La entrada combinada puede salir del segmento entre las muestras y ponderar una desigualdad con signo negativo invierte su sentido. Esas son las obligaciones que dejan de estar disponibles en la prueba. La conclusión falsa no contradice el teorema con sus premisas completas.

## 20.36. Restar un cuadrado para obtener una banda

[]{#MA-EX-ANM-01-020-036}

[]{#MA-SOL-ANM-01-020-036}

[]{#MA-SEC-ANM-01-020-008}

La función $q_m=f-(m/2)x^2$ tiene segunda derivada $f\prime\prime-m\ge0$, así es convexa. Su soporte en $c$ da $f(x)-(m/2)x^2\ge f(c)-(m/2)c^2+(f\prime(c)-mc)(x-c)$. Reorganizar deja el error de tangente al menos $(m/2)(x-c)^2$. La función $q_M=f-(M/2)x^2$ tiene segunda derivada no positiva, por lo que es cóncava y su tangente queda arriba; el mismo álgebra da la cota superior $(M/2)(x-c)^2$. No se requiere que $m$ sea positivo ni que $f\prime\prime$ sea continua.

Las auxiliares desplazan la curvatura por constantes conocidas y permiten aplicar criterios ya probados. Sus tangentes se comparan globalmente en el intervalo. Al reorganizar términos aparece el cuadrado de distancia al centro y las dos bandas firmadas. Esta ruta no necesita un desarrollo de Taylor ni continuidad de la segunda derivada.

## 20.37. La banda de una cuerda

[]{#MA-EX-ANM-01-020-037}

[]{#MA-SOL-ANM-01-020-037}

Convexidad de $q_m$ da $q_m(z)\le(1-t)q_m(a)+tq_m(b)$. Sustituimos y trasladamos el cuadrado: la diferencia de cuerda de $f$ es al menos $(m/2)((1-t)a^2+tb^2-z^2)=(m/2)t(1-t)(b-a)^2$. Concavidad de $q_M$ da la comparación opuesta y la cota superior con $M$. Para $t=0$ o1, tanto diferencia de cuerda como factor son cero, sin división. Si los bordes pertenecen a un segmento cerrado, continuidad de $f$ en ellos y el criterio extendido legitiman el mismo razonamiento.

La desigualdad convexa de la auxiliar inferior y la cóncava de la superior se evalúan con los mismos pesos. La diferencia de cuadrados produce el factor exacto de cuerda. Los pesos extremos se verifican por igualdad, sin dividir por un factor nulo. Para bordes incluidos se conserva la continuidad necesaria del criterio extendido.

## 20.38. Una banda que alcanza ambos lados

[]{#MA-EX-ANM-01-020-038}

[]{#MA-SOL-ANM-01-020-038}

La cuerda entre0 y2 tiene altura2 en1, mientras $f(1)=1$; el error es1. El factor $(m/2)t(1-t)(b-a)^2$ con $t=1/2$ es $1\cdot(1/4)\cdot4=1$, tanto inferior como superior. La tangente en1 es $1+2(x-1)$. En $x=3/2$ vale2 y $f(x)=9/4$, así el error es1/4. La banda de tangente da $(2/2)(1/2)^2=1/4$ en ambos lados. La función tiene segunda derivada constante2 y bordes continuos, por lo que cumple todas las condiciones.

La curvatura constante dos hace coincidir las barreras inferior y superior. Por eso ambos certificados determinan exactamente los errores, no sólo intervalos que los contienen. La diferencia de cuerda y la de tangente se calculan en centros y distancias distintos. Comprobar las dos cuentas mantiene separadas sus fórmulas.

## 20.39. Lo estricto no da un margen uniforme

[]{#MA-EX-ANM-01-020-039}

[]{#MA-SOL-ANM-01-020-039}

La convexidad estricta fue demostrada en E027. Pero $f\prime\prime(0)=0$, que impide cualquier cota positiva que incluya cero. Incluso excluyendo el centro, $f\prime\prime(x)=12x^2$ puede hacerse menor que todo $m>0$ acercándose a cero. Para la otra cota, si $x\ne0$, $|f\prime(x)|/|x|=4x^2$, también arbitrariamente pequeño. No existe una constante positiva uniforme en un radio completo alrededor de cero. El certificado con división por $m$ gasta convexidad fuerte cuantitativa y no sólo convexidad estricta.

La anulación en cero refuta una barrera de curvatura positiva que incluya el centro. Incluso al quitarlo, las magnitudes próximas pueden hacerse menores que cualquier barrera propuesta. El mismo argumento vale para la razón pendiente/distancia. La estrictitud cualitativa no legitima una división por una constante positiva que no se ha demostrado.

## 20.40. De una pendiente a dos certificados

[]{#MA-EX-ANM-01-020-040}

[]{#MA-SOL-ANM-01-020-040}

La segunda derivada $2+12x^2$ está entre2 y14 en el segmento, y la función es continua en sus bordes. En el interior es fuertemente convexa, con extensión de las bandas al segmento. La derivada $2x+4x^3$ se anula en0; el soporte horizontal y la banda positiva muestran que0 es el mínimo único, también frente a los bordes. En $x=1/4$, $f\prime(x)=1/2+1/16=9/16$. C19 aplicado a $f\prime$ y la cota $m=2$ dan $|x|\le(9/16)/2=9/32$. La banda inferior con centro $x$ y entrada0, seguida de completar el cuadrado, da $f(x)-f(0)\le(9/16)^2/4=81/1024$. El valor exacto es $1/16+1/256=17/256=68/1024$. Así $1/4=8/32\le9/32$ y $68/1024\le81/1024$. Se distinguen las desigualdades universales probadas de su comprobación particular.

**Retorno visual.** Véase [C20-F08](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html#fig-anm-c20-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El margen dos se demuestra para todas las segundas derivadas, no sólo en el aproximante. El centro cero es estacionario y su soporte horizontal, reforzado por la banda positiva, da mínimo único. Los certificados de posición y pérdida usan ese margen y una pendiente residual exacta. Sus cotas se comparan después con los valores exactos, distinguiendo una garantía universal de la precisión efectiva de este ejemplo.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Ejercicios](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html)
