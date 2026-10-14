---
content-id: MA-BCH-0324
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-030-SOLUCIONES
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
title: Soluciones — Capítulo 30
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C30_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)

## 30.1. Tres distancias de Hamming

[]{#MA-EX-ANM-01-030-001}

[]{#MA-SOL-ANM-01-030-001}

[]{#MA-SEC-ANM-01-030-001}

Entre $000$ y $101$ cambian la primera y la tercera coordenada, así que $d_H(x,y)=2$. Entre $101$ y $111$ sólo cambia la segunda, y $d_H(y,z)=1$. Entre $000$ y $111$ cambian las tres, dando $d_H(x,z)=3$.

Las tres triangulares del triple son $3\le2+1$, $2\le3+1$ y $1\le2+3$. La primera es igualdad: los dos pasos distribuyen los tres desacuerdos sin añadir otros. Esto comprueba el triple solicitado. Para acreditar la propiedad en todas las palabras, se usa por coordenada $\mathbf1_{\{x_i\ne z_i\}}\le\mathbf1_{\{x_i\ne y_i\}}+\mathbf1_{\{y_i\ne z_i\}}$ y se suman las desigualdades.

**Retorno visual.** Véase [C30-F01](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.2. Separación de una pseudométrica

[]{#MA-EX-ANM-01-030-002}

[]{#MA-SOL-ANM-01-030-002}

Para $x=(a,b)$, $y=(c,e)$ y $z=(u,v)$, la simetría es $|a-c|=|c-a|$, y la triangular real da $p(x,z)=|a-u|\le|a-c|+|c-u|=p(x,y)+p(y,z)$. Los valores son no negativos y la diagonal vale cero.

Falla la separación: $p((0,0),(0,1))=0$, aunque esos puntos sean distintos. Para la sucesión constante $x_n=(0,0)$, tanto $p(x_n,(0,0))$ como $p(x_n,(0,1))$ valen cero en todo índice. Satisface la condición de convergencia formulada con $p$ para ambos destinos.

La función es una pseudométrica. La prueba de unicidad que usa triangular sólo puede concluir distancia cero entre los destinos; la separación es necesaria para convertir esa conclusión en igualdad de puntos.

## 30.3. La distancia al cuadrado

[]{#MA-EX-ANM-01-030-003}

[]{#MA-SOL-ANM-01-030-003}

La función $s(x,y)=|x-y|^2$ es no negativa, simétrica y vale cero exactamente cuando $x=y$. El axioma que falla es la triangular: con puntos $0,1,2$, $s(0,2)=4$, mientras $s(0,1)+s(1,2)=2$. Este único triple refuta la afirmación universal.

Para $e(x,y)=2|x-y|$, todas las propiedades de la distancia usual se conservan al multiplicarlas por dos. En particular, $2|x-z|\le2|x-y|+2|y-z|$. El factor positivo conserva también separación. Por tanto $e$ sí es métrica: el contraejemplo anterior afecta al cuadrado, no al escalamiento por una constante positiva.

## 30.4. Un triple finito completo

[]{#MA-EX-ANM-01-030-004}

[]{#MA-SOL-ANM-01-030-004}

No negatividad, separación y simetría están aseguradas por la diagonal cero y las distancias positivas declaradas. Queda comprobar todas las triangulares. Cuando algún punto del triple se repite, la desigualdad tiene lado izquierdo cero o se reduce a una igualdad.

Para triples de tres puntos distintos, simetría reduce los casos a $t\le2+3$, $2\le3+t$ y $3\le2+t$. La primera exige $t\le5$; la tercera, $t\ge1$; la segunda vale para todo $t>0$.

Así los valores exactos son $1\le t\le5$. Los extremos están incluidos porque la triangular permite igualdad. Si $t<1$ falla la ruta de longitud $3$ por los otros dos lados; si $t>5$ falla la ruta directa de longitud $t$. Se han cubierto todos los triples del conjunto finito.

## 30.5. Triangular inversa a dos centros

[]{#MA-EX-ANM-01-030-005}

[]{#MA-SOL-ANM-01-030-005}

Aplique triangular dos veces para pasar por $a$ y $b$: $d(x,y)\le d(x,a)+d(a,b)+d(b,y)$. Restar $d(a,b)$ y usar simetría da $d(x,y)-d(a,b)\le d(x,a)+d(y,b)$.

En la ruta inversa, $d(a,b)\le d(a,x)+d(x,y)+d(y,b)$, luego $d(a,b)-d(x,y)\le d(x,a)+d(y,b)$. Ambas diferencias opuestas quedan bajo la misma cota; por ello $|d(x,y)-d(a,b)|\le d(x,a)+d(y,b)$.

Los objetos restados son valores reales finitos de la métrica. Ninguna operación de resta entre puntos de $X$ interviene en la prueba.

## 30.6. Bolas con dos formas

[]{#MA-EX-ANM-01-030-006}

[]{#MA-SOL-ANM-01-030-006}

[]{#MA-SEC-ANM-01-030-002}

Con centro $a=(1,-1)$, la bola para $d_1$ es $\{(x_1,x_2):|x_1-1|+|x_2+1|<2\}$. Es un rombo abierto con vértices de frontera $(-1,-1)$, $(3,-1)$, $(1,-3)$ y $(1,1)$.

Para $d_\infty$, la condición es $|x_1-1|<2$ y $|x_2+1|<2$, es decir $(-1,3)\times(-3,1)$. Es un cuadrado abierto.

En $(2,0)$, las diferencias de coordenadas tienen magnitud uno y uno: $d_1=2$, que excluye el punto de su bola abierta, y $d_\infty=1$, que lo incluye. En $(3,-1)$, las magnitudes son dos y cero, de modo que ambas distancias son dos; el punto queda excluido de ambas bolas abiertas. Sí pertenece a las dos bolas cerradas del mismo radio.

**Retorno visual.** Véase [C30-F02](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.7. El radio de margen

[]{#MA-EX-ANM-01-030-007}

[]{#MA-SOL-ANM-01-030-007}

Si $z\in B(y,2/5)$, la triangular da $d(a,z)\le d(a,y)+d(y,z)<3/5+2/5=1$. Ésta es precisamente la pertenencia a $B(a,1)$, por lo que la inclusión está acreditada.

En el borde de la bola pequeña sólo se sabe $d(y,z)=2/5$, y la estimación da $d(a,z)\le1$. La igualdad puede ocurrir: en la recta usual, tome $a=0$, $y=3/5$ y $z=1$. Cumple la condición de borde y queda fuera de la bola grande abierta. Por ello no se puede incluir todo el borde sin información adicional.

## 30.8. Clausura de una bola discreta

[]{#MA-EX-ANM-01-030-008}

[]{#MA-SOL-ANM-01-030-008}

En la métrica discreta, todo punto distinto de $a$ está a distancia uno. Por la desigualdad estricta, $B_D(a,1)=\{a\}$; por la desigualdad no estricta, $C_D(a,1)=X$.

Para cada $x\ne a$, $B_D(x,1/2)=\{x\}$ evita a $a$. El complemento del singleton es abierto, y el singleton es cerrado. Así $\operatorname{cl}_X B_D(a,1)=\{a\}$. Como hay al menos dos puntos, esta clausura es estrictamente menor que $C_D(a,1)$. La operación de clausura y la definición de bola cerrada no coinciden en general.

## 30.9. Dos ventanas separadas

[]{#MA-EX-ANM-01-030-009}

[]{#MA-SOL-ANM-01-030-009}

Si $z$ perteneciera a ambas bolas de radio $D/3$, la triangular daría $D=d(a,b)\le d(a,z)+d(z,b)<2D/3$, imposible para $D>0$. Por tanto son disjuntas.

Más generalmente, si $r,s>0$ y $r+s\le D$, una entrada común a $B(a,r)$ y $B(b,s)$ daría $D\le d(a,z)+d(z,b)<r+s\le D$. La contradicción persiste en el caso $r+s=D$ porque las pertenencias a bolas abiertas son estrictas. La prueba no necesita un punto medio ni una estructura lineal.

## 30.10. Una bola cerrada es cerrada

[]{#MA-EX-ANM-01-030-010}

[]{#MA-SOL-ANM-01-030-010}

Sea $x\notin C_d(a,r)$, de modo que $d(x,a)>r$. Elija $s=[d(x,a)-r]/2>0$. Si $d(x,y)<s$, la triangular inversa da $d(y,a)\ge d(x,a)-d(x,y)>d(x,a)-s=[d(x,a)+r]/2>r$. Así $B_d(x,s)$ está en el complemento de la bola cerrada.

El complemento es abierto y $C_d(a,r)$ es cerrado. Puesto que contiene a $B_d(a,r)$, contiene también su clausura. Este argumento acredita $\operatorname{cl}_X B_d(a,r)\subseteq C_d(a,r)$.

La inclusión opuesta no se ha probado y puede fallar: en la métrica discreta, con al menos dos puntos y radio uno, la clausura de la bola abierta es $\{a\}$ y la bola cerrada es todo $X$.

## 30.11. Un borde que depende del ambiente

[]{#MA-EX-ANM-01-030-011}

[]{#MA-SOL-ANM-01-030-011}

[]{#MA-SEC-ANM-01-030-003}

En $\mathbb R$, cada punto de $(0,1/2)$ tiene una bola pequeña dentro de $A$. Cero no la tiene porque sus bolas contienen negativos, y $1/2$ no pertenece a $A$. Por ello $\operatorname{int}_{\mathbb R}A=(0,1/2)$. Cada bola de los extremos cero y $1/2$ encuentra a $A$, y los puntos fuera de $[0,1/2]$ tienen una bola que lo evita. Así la clausura es $[0,1/2]$ y la frontera es $\{0,1/2\}$.

En $Y=[0,1]$, el conjunto $A=Y\cap(-1,1/2)$ es abierto relativo, luego $\operatorname{int}_Y A=A$. En particular, $B_Y(0,1/2)=[0,1/2)$ cabe en $A$. La clausura relativa es $Y\cap[0,1/2]=[0,1/2]$, y su diferencia con el interior deja la frontera $\{1/2\}$. Cero pierde su condición de frontera porque ya no hay entradas negativas en el ambiente.

**Retorno visual.** Véase [C30-F03](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.12. Uniones e intersecciones

[]{#MA-EX-ANM-01-030-012}

[]{#MA-SOL-ANM-01-030-012}

Sea $U=\bigcup_iU_i$ una unión de abiertos. Si $x\in U$, existe un miembro $U_i$ que lo contiene y un radio $r>0$ con $B(x,r)\subseteq U_i\subseteq U$. Así $U$ es abierto; la unión vacía también lo es.

Para una intersección de $k\ge1$ abiertos y un punto común $x$, cada miembro da un radio $r_i>0$. El mínimo $r=\min_i r_i$ es positivo y su bola está dentro de todos los miembros. La intersección de familia vacía es $X$, también abierto. Sólo se combinan aquí finitísimos radios.

En la recta, $\bigcap_{n\ge0}(-1/(n+1),1/(n+1))=\{0\}$. Cero pertenece a todos; para $x\ne0$, arquimedianidad proporciona $n$ con $1/(n+1)<|x|$, excluyéndolo de ese miembro. Ninguna bola real positiva de cero cabe en $\{0\}$, así que esta intersección infinita no es abierta.

## 30.13. Todo abierto y todo cerrado

[]{#MA-EX-ANM-01-030-013}

[]{#MA-SOL-ANM-01-030-013}

Para cualquier $A\subseteq X$ y $a\in A$, la bola discreta $B_D(a,1/2)=\{a\}$ está incluida en $A$. Luego $A$ es abierto. El mismo razonamiento aplicado a $X\setminus A$ prueba que el complemento es abierto y $A$ es cerrado.

En consecuencia, $\operatorname{int}_X A=A$ y $\operatorname{cl}_X A=A$. Su frontera, la diferencia entre clausura e interior, es vacía. También se ve directamente: en cada punto la bola singleton encuentra sólo uno de $A$ y su complemento, nunca ambos. El argumento incluye el conjunto vacío y el espacio completo.

## 30.14. Clausura por ventanas

[]{#MA-EX-ANM-01-030-014}

[]{#MA-SOL-ANM-01-030-014}

Todo punto de $A$ pertenece a $\operatorname{cl}_X A$, porque cada bola suya contiene al propio punto. Si $x$ está fuera de la clausura, existe $r>0$ con $B(x,r)\cap A=\varnothing$.

Para $y\in B(x,r)$, el margen $r-d(x,y)>0$ proporciona una bola de $y$ contenida en $B(x,r)$; también evita a $A$. Por tanto $y$ está fuera de la clausura. Toda la bola $B(x,r)$ queda en su complemento, que es abierto; la clausura es cerrada.

Sea ahora $F$ cualquier cerrado que contiene a $A$. Cada $x\notin F$ tiene una bola dentro de $X\setminus F$, y esa bola evita a $A$. Por ello no pertenece a $\operatorname{cl}_X A$. Se sigue $\operatorname{cl}_X A\subseteq F$, acreditando que es el menor cerrado que contiene a $A$ directamente por bolas.

## 30.15. Intersecar la clausura, no el interior

[]{#MA-EX-ANM-01-030-015}

[]{#MA-SOL-ANM-01-030-015}

Para $y\in Y$ y todo $r>0$, $B_Y(y,r)\cap A=[Y\cap B_X(y,r)]\cap A=B_X(y,r)\cap A$, pues $A\subseteq Y$. Ambas intersecciones son no vacías simultáneamente. Por la definición de clausura, $y\in\operatorname{cl}_Y A$ equivale a $y\in\operatorname{cl}_X A$ con $y\in Y$, luego $\operatorname{cl}_Y A=Y\cap\operatorname{cl}_X A$.

Para refutar la fórmula de interiores, tome $A=Y=[0,1]$ dentro de $X=\mathbb R$. El interior de $A$ en $Y$ es todo $Y$, pero $Y\cap\operatorname{int}_X A=(0,1)$. En los extremos, las bolas relativas omiten los puntos exteriores que impiden el interior absoluto.

## 30.16. Mismos términos, distinta captura

[]{#MA-EX-ANM-01-030-016}

[]{#MA-SOL-ANM-01-030-016}

[]{#MA-SEC-ANM-01-030-004}

En la usual, $d(x_n,0)=1/(n+1)\to0$. Dada una tolerancia positiva, arquimedianidad permite elegir $N$ con $1/(N+1)<\varepsilon$, y todos los posteriores cumplen la misma desigualdad. Así $x_n\to0$.

En la discreta, converger a cualquier $a\in\mathbb R$ exigiría, con tolerancia $1/2$, $d_D(x_n,a)=0$ para toda una cola. Esto obliga a $x_n=a$ desde algún índice. Los valores $1/(n+1)$ son todos distintos, por lo que ninguna cola es constante. No converge a cero ni a ningún otro destino discreto. Cambiar la métrica ha cambiado las bolas que la sucesión debe ocupar.

**Retorno visual.** Véase [C30-F04](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.17. Un destino único

[]{#MA-EX-ANM-01-030-017}

[]{#MA-SOL-ANM-01-030-017}

Suponga que $x_n$ converge a $a$ y a $b$. Si fueran distintos, separación daría $D=d(a,b)>0$. Para tolerancia $D/3$, cada convergencia proporciona un corte; tome el máximo de los dos.

En cualquier índice posterior, $d(a,x_n)<D/3$ y $d(x_n,b)<D/3$. Por triangular, $D\le d(a,x_n)+d(x_n,b)<2D/3$, contradicción. Por tanto $a=b$.

El orden se usa sólo para comparar números reales de distancia. No se han usado coordenadas, un orden entre puntos ni la existencia de límites para sucesiones arbitrarias; la completitud no interviene.

## 30.18. Dos referencias acotan el mismo conjunto

[]{#MA-EX-ANM-01-030-018}

[]{#MA-SOL-ANM-01-030-018}

Para $x\in A$, la triangular da $d(x,b)\le d(x,a)+d(a,b)\le R+d(a,b)$. La distancia fija entre los centros es finita, por lo que ésta es una cota común respecto de $b$.

Para obtener inclusión en una bola abierta, aumente la cota: $A\subseteq B_d(b,R+d(a,b)+1)$, tomando $R\ge0$ como cota de distancias. La unidad añadida garantiza radio positivo y desigualdad estricta aun cuando se alcance la cota anterior. Si $A$ es vacío, cualquier bola de centro $b$ lo contiene. La elección de los centros declarados ya asegura que $X$ no es vacío.

## 30.19. Un criterio secuencial con su interfaz

[]{#MA-EX-ANM-01-030-019}

[]{#MA-SOL-ANM-01-030-019}

La dirección incondicional es: si existe una sucesión $a_n\in A$ con $a_n\to a\in X$, entonces $a\in\operatorname{cl}_X A$. Para cada radio $r>0$, la convergencia coloca un término tardío en $B(a,r)$; ese término pertenece a $A$ y acredita la intersección no vacía.

Para la vuelta, si $a\in\operatorname{cl}_X A$, cada conjunto $W_n=A\cap B(a,1/(n+1))$ es no vacío. Bajo $\mathrm{CC}(X)$ se elige $a_n\in W_n$ simultáneamente, o se utiliza una selección suministrada. Entonces $d(a_n,a)<1/(n+1)\to0$, por lo que $a_n\to a$.

La propiedad de clausura da un testigo para cada radio; la interfaz de elección o la selección explícita permite reunirlos en una sucesión. Sin esa interfaz sólo se afirma la primera dirección de manera general.

## 30.20. Perturbación y dos distancias

[]{#MA-EX-ANM-01-030-020}

[]{#MA-SOL-ANM-01-030-020}

La desigualdad de dos centros da $|d(x_n,y_n)-d(a,b)|\le d(x_n,a)+d(y_n,b)$. Para una tolerancia $\varepsilon>0$, pida $\varepsilon/2$ a ambas convergencias y tome el máximo de sus cortes. Toda la cola tiene error menor que $\varepsilon$, de modo que $d(x_n,y_n)\to d(a,b)$ como sucesión real.

Si además $d(x_n,y_n)\to0$, la unicidad del límite real da $d(a,b)=0$; separación implica $a=b$. Si todavía no se ha supuesto convergencia de $y_n$, basta saber $x_n\to a$ y $d(x_n,y_n)\to0$: triangular da $d(y_n,a)\le d(y_n,x_n)+d(x_n,a)\to0$, construyendo su convergencia al mismo destino.

## 30.21. Cauchy sin cero admisible

[]{#MA-EX-ANM-01-030-021}

[]{#MA-SOL-ANM-01-030-021}

[]{#MA-SEC-ANM-01-030-005}

Todos los términos pertenecen a $(0,1)$. Para $m,n\ge N$, están en $(0,1/(N+2)]$, luego $|x_m-x_n|\le1/(N+2)$. Escoger $N$ con esa barrera menor que $\varepsilon$ controla todos los pares de la cola y prueba Cauchy.

Los mismos términos convergen a cero en $\mathbb R$. Si convergieran a algún $a\in(0,1)$ con la métrica restringida, la igualdad de distancias acreditaría también convergencia real a $a$. Unicidad obligaría a $a=0$, que está fuera del espacio. Por tanto no tienen ningún destino en $(0,1)$; la condición Cauchy queda satisfecha sin asegurar que el límite externo sea admisible.

**Retorno visual.** Véase [C30-F05](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.22. Cauchy y captura constante

[]{#MA-EX-ANM-01-030-022}

[]{#MA-SOL-ANM-01-030-022}

Si una sucesión es Cauchy en la discreta, tome tolerancia $1/2$. Existe $N$ con $d_D(x_m,x_n)<1/2$ para todos $m,n\ge N$. Las únicas distancias posibles son cero y uno, por lo que todas esas distancias son cero. Fijar $m=N$ da $x_n=x_N$ para toda la cola.

Recíprocamente, una cola constante tiene distancia cero entre todos sus pares posteriores y cumple Cauchy para cualquier tolerancia. Converge al valor constante $x_N$, que pertenece al espacio, pues su error es cero desde ese corte. La separación y unicidad excluyen otro destino. Así las sucesiones de Cauchy discretas son exactamente las eventualmente constantes.

## 30.23. Vecinos pequeños no bastan

[]{#MA-EX-ANM-01-030-023}

[]{#MA-SOL-ANM-01-030-023}

El salto vecino es $h_{n+1}-h_n=1/(n+2)\to0$. Para negar Cauchy hay que exhibir una tolerancia fija y pares tardíos separados por ella.

Dado cualquier corte $N\ge0$, ponga $m=N+1$ y tome los índices $p=m-1=N$, $q=2m-1$. Ambos son posteriores al corte. Sus valores difieren en $h_q-h_p=\sum_{j=m+1}^{2m}1/j$. Hay $m$ términos y cada uno es al menos $1/(2m)$, luego la diferencia es $\ge1/2$.

La tolerancia $\varepsilon_0=1/2$ falla después de todo corte, con esos pares dados explícitamente. Aunque cada salto se haga pequeño, los bloques de longitud creciente mantienen una separación fija. No se ha necesitado seleccionar infractores mediante elección.

## 30.24. Subsucesión y cola completa

[]{#MA-EX-ANM-01-030-024}

[]{#MA-SOL-ANM-01-030-024}

Suponga que $x_n$ es Cauchy y que una subsucesión $x_{n_k}$ converge a $a\in X$. Dado $\varepsilon>0$, elija $N$ de Cauchy para $\varepsilon/2$, y $K$ de la subsucesión para la misma tolerancia.

Escoja un índice $k\ge\max\{N,K\}$. Como los índices de la subsucesión son estrictamente crecientes, $n_k\ge k\ge N$, y $d(x_{n_k},a)<\varepsilon/2$. Mantenga fijo este término como referencia. Para todo $n\ge N$, la triangular da $d(x_n,a)\le d(x_n,x_{n_k})+d(x_{n_k},a)<\varepsilon$.

Así converge la sucesión completa a $a$. La existencia de una subsucesión convergente pertenece a las hipótesis: no se ha deducido que toda Cauchy disponga de ella en un espacio arbitrario.

## 30.25. Saltos geométricos y tres obligaciones

[]{#MA-EX-ANM-01-030-025}

[]{#MA-SOL-ANM-01-030-025}

Para $p>q$, la triangular iterada compara los extremos por todos los saltos intermedios: $d(x_p,x_q)\le\sum_{j=q}^{p-1}3\,2^{-j}=6\,2^{-q}(1-2^{-(p-q)})\le6\,2^{-q}$. El primer salto es el de índice $q$, lo que determina el factor seis.

Para ambos índices $\ge N$, intercambiarlos si hace falta deja una distancia $\le6\,2^{-N}$. Esta barrera tiende a cero y prueba Cauchy. En un espacio arbitrario no basta para afirmar existencia de un destino.

Si ya se sabe $x_p\to a\in X$, la triangular inversa da $|d(x_q,x_p)-d(x_q,a)|\le d(x_p,a)\to0$. Con $q$ fijo se puede pasar al límite en la cota y obtener $d(x_q,a)\le6\,2^{-q}$. Para tolerancia estricta $3/8$, se pide $6\,2^{-q}<3/8$, equivalente a $q>4$. El primer corte certificado es cinco; en cuatro la barrera sólo da $\le3/8$. La sucesión real $x_q=6\,2^{-q}$ alcanza el error al destino cero y muestra que cuatro no garantiza la desigualdad estricta.

## 30.26. Preimagen de una banda

[]{#MA-EX-ANM-01-030-026}

[]{#MA-SOL-ANM-01-030-026}

[]{#MA-SEC-ANM-01-030-006}

La condición $1<|x|<2$ se cumple exactamente en $(-2,-1)\cup(1,2)$. Por ello $f^{-1}[(1,2)]$ es esa unión de dos intervalos abiertos.

La triangular inversa real da $||x|-|a||\le|x-a|$ para cualquier centro $a$. Con $\delta=\varepsilon$, toda entrada a distancia menor que $\delta$ tiene error de salida menor que $\varepsilon$. Así $f$ es continua en toda la recta, e incluso $1$-Lipschitz. Su falta de inyectividad no afecta a este control ni al criterio por preimágenes.

**Retorno visual.** Véase [C30-F06](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.27. La equivalencia por abiertos

[]{#MA-EX-ANM-01-030-027}

[]{#MA-SOL-ANM-01-030-027}

Sean $(X,d_X)$ y $(Y,d_Y)$ espacios métricos, y $f:X\to Y$. Suponga primero que $f$ es continua. Si $V\subseteq Y$ es abierto y $a\in f^{-1}[V]$, existe $\varepsilon>0$ con $B_Y(f(a),\varepsilon)\subseteq V$. Continuidad en $a$ proporciona $\delta>0$ que envía $B_X(a,\delta)$ dentro de esa bola. Luego la preimagen es abierta en $X$.

Recíprocamente, suponga que toda preimagen de un abierto de $Y$ es abierta en $X$. Para $a\in X$ y $\varepsilon>0$, la preimagen de $B_Y(f(a),\varepsilon)$ es abierta y contiene a $a$. Existe $\delta>0$ con $B_X(a,\delta)$ incluida en ella. Esto significa exactamente que $d_X(x,a)<\delta$ implica $d_Y(f(x),f(a))<\varepsilon$, acreditando continuidad en cada centro.

Las bolas de entrada y salida usan sus métricas respectivas. La prueba trabaja punto a punto con radios; no construye sucesiones ni utiliza elección numerable. El dominio vacío satisface ambas condiciones de modo vacuo.

## 30.28. Identidad con inversa fallida

[]{#MA-EX-ANM-01-030-028}

[]{#MA-SOL-ANM-01-030-028}

La identidad $i:(\mathbb R,d_D)\to(\mathbb R,|\cdot|)$ es biyectiva por su regla de valores. Para cualquier centro $a$ y tolerancia de salida $\varepsilon>0$, el radio discreto $\delta=1/2$ admite únicamente $x=a$. Su error de salida es cero, luego $i$ es continua.

Para la inversa $j$ en cero, fije tolerancia discreta $1/2$. Dado cualquier radio usual $\delta>0$, tome $x=\delta/2$. Está a distancia usual menor que $\delta$ de cero y es distinto de cero, por lo que $d_D(j(x),j(0))=1$. Ningún radio cumple la tolerancia. La biyección continua tiene, por tanto, una inversa discontinua.

## 30.29. Un fracaso secuencial condicionado

[]{#MA-EX-ANM-01-030-029}

[]{#MA-SOL-ANM-01-030-029}

Negar continuidad en $a$ da $\varepsilon_0>0$ tal que para cada $\delta>0$ existe $x\in X$ con $d_X(x,a)<\delta$ y $d_Y(f(x),f(a))\ge\varepsilon_0$. Para $n\ge0$, forme $W_n=\{x\in X:d_X(x,a)<1/(n+1),\ d_Y(f(x),f(a))\ge\varepsilon_0\}$. Cada $W_n$ es no vacío.

Bajo $\mathrm{CC}(X)$, se selecciona simultáneamente $x_n\in W_n$. Entonces $d_X(x_n,a)<1/(n+1)\to0$, pero las imágenes quedan a distancia al menos $\varepsilon_0$ de $f(a)$ en todos los índices. Así $x_n\to a$ y $f(x_n)$ no converge al valor central.

La elección se usa exclusivamente para reunir los testigos de la familia $W_n$ en una sucesión. Si esos testigos ya están dados explícitamente, basta utilizarlos. La sucesión infractora niega convergencia al valor central; podría tener otro destino en el codominio.

## 30.30. Transportar el dominio de un nivel

[]{#MA-EX-ANM-01-030-030}

[]{#MA-SOL-ANM-01-030-030}

Con $F(x)=d(x,b)$, la triangular inversa da $|F(x)-F(a)|\le d(x,a)$ para todos los puntos. Por tanto $\delta=\varepsilon$ acredita continuidad en cualquier centro, y también continuidad uniforme.

Para cualquier $r\in\mathbb R$, el nivel $\{x:d(x,b)=r\}$ es $F^{-1}[\{r\}]$. El singleton real es cerrado y la preimagen por una función continua es cerrada, como se obtiene aplicando el criterio de abiertos al complemento. La región $\{x:d(x,b)<r\}=F^{-1}[(-\infty,r)]$ es abierta.

Estas conclusiones incluyen niveles vacíos y la región vacía cuando $r\le0$. No se exige que exista algún punto a distancia exactamente $r$ ni que la distancia recorra todos los valores de un intervalo.

## 30.31. Un radio Lipschitz

[]{#MA-EX-ANM-01-030-031}

[]{#MA-SOL-ANM-01-030-031}

[]{#MA-SEC-ANM-01-030-007}

Suponga $d_Y(f(x),f(y))\le Ld_X(x,y)$ para todo par. Si $L>0$, el radio común $\delta=\varepsilon/L$ da error de salida menor que $\varepsilon$ cuando la distancia de entrada es menor que $\delta$.

Para una sucesión Cauchy $x_n$, elija su corte correspondiente a $\delta$. Todo par posterior cumple $d_X(x_m,x_n)<\delta$ y por ello $d_Y(f(x_m),f(x_n))<\varepsilon$. Así la sucesión de imágenes es Cauchy sin necesitar un destino en ninguno de los espacios.

Si $L=0$, todas las distancias de imágenes son cero; por separación, en un dominio no vacío la función es constante. Cualquier radio positivo sirve, y las imágenes de cualquier sucesión son constantes y Cauchy. Si el dominio es vacío, las condiciones universales son vacuas y no hay sucesiones que transportar.

## 30.32. Distancia cero sin pertenencia

[]{#MA-EX-ANM-01-030-032}

[]{#MA-SOL-ANM-01-030-032}

Para $x<0$ y $a\in(0,1)$, $|x-a|=a-x>-x$. Hacer $a\to0^+$ aproxima ese valor a $-x$, luego el ínfimo es $-x$ y no se alcanza. Para $x>1$, $|x-a|=x-a>x-1$; al hacer $a\to1^-$, el ínfimo es $x-1$, tampoco alcanzado.

Si $0<x<1$, tomar $a=x$ da distancia cero, el mínimo. En $x=0$ o $x=1$, las distancias positivas a entradas que se acercan al extremo tienden a cero; su ínfimo es cero pero no hay punto del intervalo que lo alcance.

Así $\operatorname{dist}(x,A)=-x$ para $x<0$, cero para $0\le x\le1$, y $x-1$ para $x>1$. El conjunto de ceros es $[0,1]=\operatorname{cl}A$. El ínfimo se alcanza exactamente cuando $x\in(0,1)$, lo que distingue distancia cero, pertenencia a la clausura y existencia de un punto minimizante.

## 30.33. Continuidad que destruye Cauchy

[]{#MA-EX-ANM-01-030-033}

[]{#MA-SOL-ANM-01-030-033}

En un centro $a\in(0,1)$, si $|x-a|<a/2$ entonces $x>a/2$ y $|1/x-1/a|=|x-a|/(ax)\le2|x-a|/a^2$. Para $\varepsilon>0$ sirve $\delta=\min\{a/2,\varepsilon a^2/2\}$, que acredita continuidad en $a$.

Para negar uniformidad, use $x_n=1/(n+2)$, $y_n=1/(n+3)$. Su separación es $1/[(n+2)(n+3)]\to0$, mientras la separación de imágenes es uno. Con tolerancia de salida $1/2$, cualquier radio queda incumplido por alguno de esos pares.

La sucesión $x_n$ es Cauchy en $(0,1)$: los términos posteriores a $N$ están entre cero y $1/(N+2)$. Sus imágenes son $n+2$, cuyos vecinos tienen distancia uno y niegan Cauchy con tolerancia $1/2$. El centro problemático cero está fuera del dominio; el ejemplo respeta continuidad en todos sus puntos.

## 30.34. Un supremo que no se alcanza

[]{#MA-EX-ANM-01-030-034}

[]{#MA-SOL-ANM-01-030-034}

Para $t<1$, $f_n(t)\to0$, y en $t=1$ todos los valores son uno; ésas son las evaluaciones del destino puntual $f$. Su error es $t^{n+1}$ en $[0,1)$ y cero en uno. Es menor que uno en todas las entradas.

Sin embargo, para $n$ fijo y $t\to1^-$, $t^{n+1}\to1$. Por ello uno es la menor cota superior y $D_\infty(f_n,f)=1$ en cada índice. El supremo no se alcanza, y las distancias no tienden a cero: no hay convergencia uniforme a $f$.

Para $g_n(t)=t/(n+1)$, el destino es cero y $D_\infty(g_n,0)=1/(n+1)$, alcanzado en $t=1$. Éste sí tiende a cero. La primera familia muestra por qué errores individualmente estrictos no permiten concluir que su supremo sea estricto.

**Retorno visual.** Véase [C30-F07](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.35. Una distancia de funciones bien definida

[]{#MA-EX-ANM-01-030-035}

[]{#MA-SOL-ANM-01-030-035}

Sean $f,g\in\mathcal B(T)$, con $T\ne\varnothing$. Si sus magnitudes están acotadas por $M_f,M_g$, entonces $0\le|f(t)-g(t)|\le M_f+M_g$. El conjunto de errores es no vacío y acotado; la completitud real por supremos construye el número finito $D_\infty(f,g)$.

Si $f=g$, el supremo es cero. Si el supremo es cero, cada error es cero, luego $f(t)=g(t)$ para todo $t$ y $f=g$. La simetría procede del valor absoluto. Para $h\in\mathcal B(T)$, la triangular puntual da $|f(t)-g(t)|\le D_\infty(f,h)+D_\infty(h,g)$ en toda entrada; tomar supremo acredita la triangular de $D_\infty$.

Si $D_\infty(f_n,f)\to0$, una distancia menor que $\varepsilon$ controla todos los errores y da uniformidad. Recíprocamente, uniformidad con tolerancia $\varepsilon/2$ deja $D_\infty(f_n,f)\le\varepsilon/2<\varepsilon$ en toda la cola. El destino pertenece aquí a $\mathcal B(T)$; si sólo se sabe que es límite uniforme de funciones acotadas, un parcial con error menor que uno prueba su acotación. La completitud real se usa para formar los supremos, sin haber probado todavía completitud del espacio de funciones.

## 30.36. Un par y dos métricas

[]{#MA-EX-ANM-01-030-036}

[]{#MA-SOL-ANM-01-030-036}

[]{#MA-SEC-ANM-01-030-008}

Para $x=(1,2)$, $y=(4,-2)$, las magnitudes de las diferencias de coordenadas son tres y cuatro. Por ello $d_1(x,y)=7$ y $d_\infty(x,y)=4$, cumpliendo $4\le7\le8$.

En general, con $u=|x_1-y_1|$ y $v=|x_2-y_2|$, el máximo es menor o igual que $u+v$, y ambos sumandos son menores o iguales que el máximo. Luego $\max\{u,v\}\le u+v\le2\max\{u,v\}$, que prueba $d_\infty\le d_1\le2d_\infty$ para todos los pares.

La identidad de $d_\infty$ a $d_1$ es $2$-Lipschitz y la inversa es $1$-Lipschitz. Esas cotas convierten radios de bolas y tolerancias de convergencia y Cauchy en los dos sentidos.

## 30.37. Recortar una métrica

[]{#MA-EX-ANM-01-030-037}

[]{#MA-SOL-ANM-01-030-037}

La función $e(x,y)=\min\{1,d(x,y)\}$ es no negativa, separa puntos y es simétrica. Para $u,v\ge0$, $\min\{1,u+v\}\le\min\{1,u\}+\min\{1,v\}$: si alguno es al menos uno, el lado derecho domina uno; si ambos son menores que uno, el lado derecho es $u+v$. Monotonía del mínimo y triangular de $d$ dan $e(x,z)\le e(x,y)+e(y,z)$.

Como $e\le d$, un corte que controle distancias en $d$ controla las de $e$. Para el sentido inverso, dada $\varepsilon>0$, pida en $e$ la tolerancia $\eta=\min\{\varepsilon/2,1/2\}$. Una distancia $e(x,y)<\eta$ fuerza $d(x,y)<1$, donde $e=d$, y además $d(x,y)<\varepsilon$. Aplicar este control a distancias al destino o a todos los pares de una cola conserva, respectivamente, convergencia y Cauchy.

La acotación puede cambiar: en $e$ todas las distancias son $\le1$, y un espacio no vacío entero cabe en una bola de radio dos. La recta con distancia usual no es acotada. El acuerdo en controles pequeños no produce una comparación global de las distancias grandes.

## 30.38. Una métrica con los mismos abiertos

[]{#MA-EX-ANM-01-030-038}

[]{#MA-SOL-ANM-01-030-038}

Para todo $x\in\mathbb R$, $|\phi(x)|=|x|/(1+|x|)<1$. Defina $\psi(t)=t/(1-|t|)$ en $(-1,1)$. Se tiene $1-|\phi(x)|=1/(1+|x|)$ y, por tanto, $\psi(\phi(x))=x$. Para $|t|<1$, $1+|\psi(t)|=1/(1-|t|)$, y de igual modo $\phi(\psi(t))=t$. Así $\phi$ es una biyección con inversa $\psi$.

La separación de $e_\phi$ procede de la inyectividad de $\phi$; no negatividad, simetría y triangular son las propiedades del valor absoluto entre las imágenes. Luego $e_\phi$ es métrica. Ambas funciones $\phi$ y $\psi$ son continuas con las métricas usuales por las reglas reales de valor absoluto y cociente, cuyos denominadores son positivos en sus dominios.

Cada bola $B_{e_\phi}(a,r)$ es $\phi^{-1}[B_{(-1,1)}(\phi(a),r)]$, abierta usual por continuidad. Una unión de tales bolas prueba que todo abierto de $e_\phi$ es usual. Para la otra dirección, si $U$ es abierto usual, $\phi[U]=\psi^{-1}[U]$ es abierto relativo en $(-1,1)$. En cada $a\in U$ hay una bola relativa de $\phi(a)$ dentro de esa imagen; su preimagen es una bola de $e_\phi$ dentro de $U$. Así tienen exactamente los mismos abiertos, mediante radios locales.

## 30.39. Misma topología, otra Cauchy

[]{#MA-EX-ANM-01-030-039}

[]{#MA-SOL-ANM-01-030-039}

En la usual, $|x_{n+1}-x_n|=1$. La tolerancia $1/2$ queda incumplida por vecinos posteriores a cualquier corte, de modo que $x_n=n$ no es Cauchy. Tampoco converge, pues toda convergente es Cauchy; además no es acotada, por arquimedianidad.

En $e_\phi$, las imágenes son $n/(n+1)=1-1/(n+1)$. Para $m,n\ge N$, su separación es $\le1/(N+1)$, lo que prueba Cauchy. Como todas las imágenes pertenecen a $(-1,1)$, todas las distancias $e_\phi$ son menores que dos; una bola de radio dos alrededor de cualquier centro contiene la sucesión, que sí es acotada.

Si convergiera a algún real $a$ en $e_\phi$, por definición las imágenes convergerían usualmente a $\phi(a)$. También convergen a uno por la fórmula explícita, y unicidad obligaría $\phi(a)=1$, fuera del recorrido. No existe destino en ese espacio. La misma topología conserva convergencia a sus puntos, pero no necesariamente Cauchy ni acotación.

**Retorno visual.** Véase [C30-F08](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.40. Auditar la identidad inversa

[]{#MA-EX-ANM-01-030-040}

[]{#MA-SOL-ANM-01-030-040}

La identidad $i:(\mathbb R,e_\phi)\to(\mathbb R,|\cdot|)$ es continua, pues ambos espacios tienen los mismos abiertos y las preimágenes por identidad coinciden con ellos. También puede darse un radio local: para $a\in\mathbb R$, continuidad de $\psi$ en $\phi(a)$ convierte una tolerancia usual en un radio de imágenes, y $e_\phi(x,a)<\delta$ sitúa a $\phi(x)$ en ese radio, dando $|x-a|<\varepsilon$.

Para negar uniformidad, tome los pares $n,n+1$. Su distancia de entrada es $e_\phi(n,n+1)=1/[(n+1)(n+2)]\to0$, pero su distancia de salida usual es uno. Con tolerancia $1/2$, cualquier radio común falla para algún par posterior. La continuidad de la inversa $\psi$ es local y no proporciona ese radio común cerca de la frontera del intervalo de imágenes.

Entre $d_\infty$ y $d_1$ en el plano, las desigualdades globales dan identidades $2$-Lipschitz y $1$-Lipschitz. Sirven, respectivamente, los radios uniformes $\varepsilon/2$ y $\varepsilon$, y ambas identidades transportan Cauchy. Las cotas comunes de ese ejemplo acreditan una propiedad adicional al acuerdo de abiertos.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)
