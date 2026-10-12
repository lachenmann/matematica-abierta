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
date-modified: '2026-10-11'
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

$d_H(x,y)=2$, $d_H(y,z)=1$ y $d_H(x,z)=3$. Las tres desigualdades son $3\le2+1$, $2\le3+1$ y $1\le2+3$. La primera es igualdad. Este cotejo acredita ese triple; la propiedad para todas las palabras se demuestra mediante indicadores de desacuerdo en cada coordenada, no mediante esta sola muestra.

**Retorno visual.** Véase [C30-F01](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.2. Separación de una pseudométrica

[]{#MA-EX-ANM-01-030-002}

[]{#MA-SOL-ANM-01-030-002}

La simetría y la triangular son las del valor absoluto en la primera coordenada. Pero $p((0,0),(0,1))=0$ con puntos distintos. La sucesión constante $(0,0)$ tiene distancia cero tanto a $(0,0)$ como a $(0,1)$ en todos sus términos, así que satisface ambos contratos de convergencia formulados con $p$. La separación es la hipótesis que convierte distancia cero en igualdad y protege la unicidad métrica.

## 30.3. La distancia al cuadrado

[]{#MA-EX-ANM-01-030-003}

[]{#MA-SOL-ANM-01-030-003}

La propuesta cuadrática es no negativa, separa puntos y es simétrica. Falla la triangular: $s(0,2)=4> s(0,1)+s(1,2)=2$. En cambio $2|x-y|$ multiplica por un escalar positivo todas las propiedades de la métrica usual; la triangular usual multiplicada por dos sigue válida. Escalar una distancia por una constante positiva difiere de elevarla al cuadrado.

## 30.4. Un triple finito completo

[]{#MA-EX-ANM-01-030-004}

[]{#MA-SOL-ANM-01-030-004}

Para triples con alguna repetición, la triangular se reduce a igualdad o a no negatividad. Para tres puntos distintos hay sólo tres desigualdades: $t\le2+3$, $2\le3+t$ y $3\le2+t$. La segunda vale para todo $t>0$; las otras exigen $t\le5$ y $t\ge1$. Por tanto exactamente $1\le t\le5$. Positividad fuera de diagonal y simetría ya están declaradas. Aquí sí se ha agotado el universo finito de triples.

## 30.5. Triangular inversa a dos centros

[]{#MA-EX-ANM-01-030-005}

[]{#MA-SOL-ANM-01-030-005}

La triangular iterada da $d(x,y)\le d(x,a)+d(a,b)+d(b,y)$, por lo que $d(x,y)-d(a,b)\le d(x,a)+d(y,b)$. Intercambiar los dos pares da $d(a,b)-d(x,y)\le d(x,a)+d(y,b)$. Reunir ambas desigualdades prueba la cota absoluta. Se restan valores reales finitos de la métrica; no se supone una resta de puntos en $X$.

## 30.6. Bolas con dos formas

[]{#MA-EX-ANM-01-030-006}

[]{#MA-SOL-ANM-01-030-006}

[]{#MA-SEC-ANM-01-030-002}

La primera región es $|x_1-1|+|x_2+1|<2$, un rombo con frontera excluida. La segunda es $-1<x_1<3$ y $-3<x_2<1$, un cuadrado abierto. Para $(2,0)$ las distancias son $2$ y $1$: no pertenece a la primera y sí a la segunda. Para $(3,-1)$ ambas distancias son $2$, de modo que está excluido de ambas bolas abiertas y pertenece a ambas bolas cerradas del mismo radio.

**Retorno visual.** Véase [C30-F02](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.7. El radio de margen

[]{#MA-EX-ANM-01-030-007}

[]{#MA-SOL-ANM-01-030-007}

Para $d(y,z)<2/5$, la triangular da $d(a,z)\le3/5+d(y,z)<1$. Si se permite $d(y,z)=2/5$, sólo queda $d(a,z)\le1$. En la recta usual tome $a=0$, $y=3/5$ y $z=1$: está en la bola pequeña cerrada, pero no en la grande abierta. La pertenencia estricta de la ventana pequeña paga la desigualdad estricta final.

## 30.8. Clausura de una bola discreta

[]{#MA-EX-ANM-01-030-008}

[]{#MA-SOL-ANM-01-030-008}

La bola abierta contiene sólo $a$, porque los otros puntos distan exactamente uno. La cerrada contiene todo $X$. Todo singleton es cerrado, pues cada punto distinto tiene su propia bola de radio $1/2$ que evita a $a$. Así la clausura de la bola abierta es $\{a\}$, diferente de la bola cerrada. La notación de clausura no debe confundirse con una desigualdad no estricta en una definición de bola.

## 30.9. Dos ventanas separadas

[]{#MA-EX-ANM-01-030-009}

[]{#MA-SOL-ANM-01-030-009}

Una entrada común $z$ daría $D\le d(a,z)+d(z,b)<2D/3$, imposible. Para radios $r,s>0$ con $r+s\le D$, la misma entrada daría $D<r+s\le D$. No hace falta localizar un punto medio ni usar un orden de los centros; las dos pertenencias estrictas y la triangular bastan.

## 30.10. Una bola cerrada es cerrada

[]{#MA-EX-ANM-01-030-010}

[]{#MA-SOL-ANM-01-030-010}

Para $x$ fuera de la bola cerrada, $s=(d(x,a)-r)/2>0$. Si $d(x,y)<s$, la triangular inversa da $d(y,a)>d(x,a)-s>r$, así que la bola de $x$ queda en el complemento. Éste es abierto y la bola cerrada es cerrada. Como contiene a la bola abierta, contiene su clausura; la prueba sólo da esa inclusión. La métrica discreta en radio uno proporciona inclusión estricta.

## 30.11. Un borde que depende del ambiente

[]{#MA-EX-ANM-01-030-011}

[]{#MA-SOL-ANM-01-030-011}

[]{#MA-SEC-ANM-01-030-003}

En $\mathbb R$, interior $(0,1/2)$, clausura $[0,1/2]$ y frontera $\{0,1/2\}$. En $Y$, $A=Y\cap(-1,1/2)$ es abierto relativo, así que es su propio interior. La fórmula de clausura relativa deja $[0,1/2]$ y la frontera es $\{1/2\}$. El punto cero tiene una ventana relativa completa dentro de $A$, aunque no tenga una ventana de la recta dentro de $A$.

**Retorno visual.** Véase [C30-F03](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.12. Uniones e intersecciones

[]{#MA-EX-ANM-01-030-012}

[]{#MA-SOL-ANM-01-030-012}

Una entrada de una unión pertenece a un miembro y reutiliza su radio. En una intersección finita no vacía, cada punto tiene finitísimos radios positivos y su mínimo protege simultáneamente todas las condiciones. La intersección de familia vacía es el abierto $X$. En la recta, los intervalos $(-1/(n+1),1/(n+1))$ tienen intersección $\{0\}$: cero pertenece a todos, mientras para cualquier $x\ne0$ existe $n$ con $1/(n+1)<|x|$. Ninguna bola real positiva alrededor de cero cabe en el singleton, que no es abierto.

## 30.13. Todo abierto y todo cerrado

[]{#MA-EX-ANM-01-030-013}

[]{#MA-SOL-ANM-01-030-013}

Para $a\in A$, $B_D(a,1/2)=\{a\}\subset A$, así que $A$ es abierto. Su complemento satisface el mismo argumento, luego $A$ es cerrado. Interior y clausura de $A$ son ambos $A$, por lo que la frontera $\operatorname{cl}A\setminus\operatorname{int}A$ es vacía. Esto vale también para vacío y espacio completo.

## 30.14. Clausura por ventanas

[]{#MA-EX-ANM-01-030-014}

[]{#MA-SOL-ANM-01-030-014}

Contiene $A$ porque cada bola de un punto de $A$ contiene al propio punto. Si $x$ está fuera de la clausura, alguna bola $B(x,r)$ evita $A$. Para cada $y$ en ella, el margen produce una bola alrededor de $y$ contenida en $B(x,r)$, también disjunta de $A$. Así toda la bola original queda fuera de la clausura y su complemento es abierto. Si un cerrado $F$ contiene $A$, cada punto fuera de $F$ tiene una bola que evita $F$ y por ello evita $A$; no puede pertenecer a la clausura. Luego ésta está contenida en todo tal $F$.

## 30.15. Intersecar la clausura, no el interior

[]{#MA-EX-ANM-01-030-015}

[]{#MA-SOL-ANM-01-030-015}

Para $y\in Y$, la intersección $B_Y(y,r)\cap A$ es igual a $B_X(y,r)\cap A$, porque $A\subset Y$. La no vaciedad para cada radio es entonces la misma condición, con la pertenencia a $Y$ añadida. Para el interior, tome $A=Y=[0,1]$ en $X=\mathbb R$. El interior en $Y$ es todo $Y$, mientras $Y\cap\operatorname{int}_X A=(0,1)$. El ambiente cambia los puntos admisibles de la ventana, y con ellos la inclusión completa dentro de $A$.

## 30.16. Mismos términos, distinta captura

[]{#MA-EX-ANM-01-030-016}

[]{#MA-SOL-ANM-01-030-016}

[]{#MA-SEC-ANM-01-030-004}

En la usual, $|x_n|=1/(n+1)\to0$, luego converge a cero. En la discreta, converger a algún $a$ exigiría $x_n=a$ desde cierto índice por tolerancia $1/2$. Los recíprocos son todos distintos, de modo que ninguna cola es constante. No converge a ningún destino discreto, incluido cero. El conjunto de puntos es el mismo y la métrica cambia la condición efectiva.

**Retorno visual.** Véase [C30-F04](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.17. Un destino único

[]{#MA-EX-ANM-01-030-017}

[]{#MA-SOL-ANM-01-030-017}

Suponga dos límites distintos $a,b$ y escriba $D=d(a,b)>0$. Las dos convergencias con tolerancia $D/3$ dan cortes; su máximo garantiza que el mismo término de la sucesión está a distancia menor que $D/3$ de cada destino. Triangular da $D<2D/3$, contradicción. Separación transforma distancia cero en igualdad. El orden sólo se usa al comparar las distancias reales positivas, no los puntos del espacio.

## 30.18. Dos referencias acotan el mismo conjunto

[]{#MA-EX-ANM-01-030-018}

[]{#MA-SOL-ANM-01-030-018}

Por triangular $d(x,b)\le d(x,a)+d(a,b)\le R+d(a,b)$. La distancia fija de centros es real finita. Así $A$ queda dentro de la bola abierta de centro $b$ y radio $R+d(a,b)+1$, que excede la cota débil. El conjunto vacío satisface la cota de modo vacuo; disponer de los centros declarados asegura aquí que $X$ no sea vacío.

## 30.19. Un criterio secuencial con su interfaz

[]{#MA-EX-ANM-01-030-019}

[]{#MA-SOL-ANM-01-030-019}

Si $a_n\in A$ y $a_n\to a\in X$, cada bola de $a$ contiene algún término tardío de $A$, por lo que $a\in\operatorname{cl}A$, sin elección. Para la vuelta, la adherencia asegura que cada $A\cap B(a,1/(n+1))$ sea no vacío. Una selección $a_n$ en esos conjuntos, dada o garantizada por $\mathrm{CC}(X)$, satisface $d(a_n,a)<1/(n+1)$ y converge. Sin esa interfaz no se declara la existencia simultánea de los testigos arbitrarios. La caracterización secuencial inversa de cerrado tiene el mismo alcance.

## 30.20. Perturbación y dos distancias

[]{#MA-EX-ANM-01-030-020}

[]{#MA-SOL-ANM-01-030-020}

La cota de dos centros de E005 da $|d(x_n,y_n)-d(a,b)|\le d(x_n,a)+d(y_n,b)$. Para tolerancia $\varepsilon$, pedir $\varepsilon/2$ a cada convergencia y sincronizar cortes hace menor que $\varepsilon$ el error real. Si además $d(x_n,y_n)\to0$, unicidad del límite real implica $d(a,b)=0$ y separación da $a=b$. Si no se sabe aún que $y_n$ converja pero se sabe $x_n\to a$ y $d(x_n,y_n)\to0$, triangular directamente acredita $y_n\to a$.

## 30.21. Cauchy sin cero admisible

[]{#MA-EX-ANM-01-030-021}

[]{#MA-SOL-ANM-01-030-021}

[]{#MA-SEC-ANM-01-030-005}

Después de un corte $N$, todos los valores están en $(0,1/(N+2)]$ y cualquier separación es a lo sumo $1/(N+2)$. Arquimedianidad permite hacerlo menor que una tolerancia dada. En la recta, los mismos términos convergen a cero. Si hubiera un límite $a\in(0,1)$, la igualdad de distancias con la inclusión acreditaría también límite real $a$. Unicidad real lo igualaría a cero, contradiciendo la pertenencia al espacio. Cauchy sólo controla pares internos, sin imponer que el destino externo pertenezca al dominio.

**Retorno visual.** Véase [C30-F05](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.22. Cauchy y captura constante

[]{#MA-EX-ANM-01-030-022}

[]{#MA-SOL-ANM-01-030-022}

Con tolerancia $1/2$, cualquier par posterior al corte tiene distancia cero. Fijando uno de los índices en el corte, toda la cola es igual a $x_N$. Recíprocamente, una cola constante tiene todas sus distancias posteriores cero y cumple Cauchy para toda tolerancia. Esa misma cola converge a su valor constante, que pertenece al espacio. La unicidad ya probada excluye otros destinos.

## 30.23. Vecinos pequeños no bastan

[]{#MA-EX-ANM-01-030-023}

[]{#MA-SOL-ANM-01-030-023}

El salto es $h_{n+1}-h_n=1/(n+2)\to0$. Dado un corte $N$, tome $m=N+1$ y los índices $m-1=N$ y $2m-1\ge N$. La diferencia es $\sum_{j=m+1}^{2m}1/j$, con $m$ términos cada uno al menos $1/(2m)$, así que es al menos $1/2$. La tolerancia fija $1/2$ y estos pares niegan Cauchy. Los bloques crecen con el corte; controlar sólo vecinos omite precisamente esa obligación.

## 30.24. Subsucesión y cola completa

[]{#MA-EX-ANM-01-030-024}

[]{#MA-SOL-ANM-01-030-024}

Para $\varepsilon>0$, tome el corte $N$ de Cauchy con tolerancia $\varepsilon/2$, y el corte $K$ de la subsucesión convergente a $a$ con la misma tolerancia. Elija $k\ge\max\{N,K\}$; entonces $n_k\ge k\ge N$. Ese término fijo satisface $d(x_{n_k},a)<\varepsilon/2$. Para todo $n\ge N$, triangular da $d(x_n,a)\le d(x_n,x_{n_k})+d(x_{n_k},a)<\varepsilon$. No se asume existencia de una subsucesión convergente para una Cauchy arbitraria; es la hipótesis del ejercicio.

## 30.25. Saltos geométricos y tres obligaciones

[]{#MA-EX-ANM-01-030-025}

[]{#MA-SOL-ANM-01-030-025}

Para $p>q$, triangular iterada y suma geométrica finita dan $d(x_p,x_q)\le6\,2^{-q}$. Como el presupuesto tiende a cero, hay un corte común para todos los pares y la sucesión es de Cauchy. No se afirma existencia de destino en un espacio arbitrario. Si $x_p\to a\in X$, continuidad real de la distancia al punto fijo $x_q$ permite pasar $p$ al límite y da $d(x_q,a)\le6\,2^{-q}$. Para error estrictamente menor que $3/8$, basta $6\,2^{-q}<3/8$, es decir $q>4$, por lo que el primer índice certificado es $5$.

## 30.26. Preimagen de una banda

[]{#MA-EX-ANM-01-030-026}

[]{#MA-SOL-ANM-01-030-026}

[]{#MA-SEC-ANM-01-030-006}

La preimagen es $(-2,-1)\cup(1,2)$, abierta. Para todo par, $||x|-|y||\le|x-y|$ por triangular inversa real, así que en cualquier centro sirve $\delta=\varepsilon$. La desigualdad acredita continuidad de la función en todos los puntos, y el criterio de preimágenes explica la apertura de la región calculada. El mapa no necesita ser inyectivo.

**Retorno visual.** Véase [C30-F06](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.27. La equivalencia por abiertos

[]{#MA-EX-ANM-01-030-027}

[]{#MA-SOL-ANM-01-030-027}

Para continuidad→preimagen, dado abierto $V$ y $a$ con $f(a)\in V$, obtenga una bola de salida contenida en $V$ y use su radio como tolerancia de continuidad. La bola de entrada obtenida queda en la preimagen, que es abierta punto por punto. Para la vuelta, la preimagen de $B_Y(f(a),\varepsilon)$ es abierta y contiene a $a$; una bola de entrada dentro de ella entrega el radio $\delta$ de la definición. Las dos métricas intervienen en sus respectivas bolas; no se seleccionan testigos para una sucesión ni se necesita elección numerable.

## 30.28. Identidad con inversa fallida

[]{#MA-EX-ANM-01-030-028}

[]{#MA-SOL-ANM-01-030-028}

La regla es biyectiva. Para cualquier tolerancia de salida usual, tome radio discreto $1/2$: la única entrada admisible es el centro y el error de salida es cero. Para la inversa, la tolerancia discreta $1/2$ exigiría que todas las entradas de alguna ventana usual de cero fueran cero. Dado cualquier radio $\delta>0$, la entrada $\delta/2$ está en esa ventana y es distinta de cero, por lo que su distancia discreta al centro es uno. Ningún radio funciona.

## 30.29. Un fracaso secuencial condicionado

[]{#MA-EX-ANM-01-030-029}

[]{#MA-SOL-ANM-01-030-029}

Negar continuidad fija $\varepsilon_0>0$ tal que para cada radio hay una entrada cercana cuya distancia de salida a $f(a)$ es al menos $\varepsilon_0$. Para el radio $1/(n+1)$, forme su conjunto no vacío de infractores. $\mathrm{CC}(X)$ permite escoger una entrada $x_n$ de cada conjunto. Entonces $d_X(x_n,a)<1/(n+1)$ acredita convergencia, pero todas las distancias de salida son al menos $\varepsilon_0$, negando convergencia de imágenes al valor central. La selección explícita de esos testigos también basta; su existencia simultánea es el único paso que usa el supuesto.

## 30.30. Transportar el dominio de un nivel

[]{#MA-EX-ANM-01-030-030}

[]{#MA-SOL-ANM-01-030-030}

La triangular inversa da $|F(x)-F(a)|\le d(x,a)$, así que $\delta=\varepsilon$ sirve en todo centro. El conjunto de igualdad es la preimagen del singleton real cerrado $\{r\}$ y por ello es cerrado. La región estricta es la preimagen del abierto real $(-\infty,r)$ y es abierta, incluso cuando resulte vacía. Estas pruebas no necesitan que los valores de distancia recorran un intervalo continuo ni que exista algún punto a distancia $r$.

## 30.31. Un radio Lipschitz

[]{#MA-EX-ANM-01-030-031}

[]{#MA-SOL-ANM-01-030-031}

[]{#MA-SEC-ANM-01-030-007}

Si $L>0$, use $\delta=\varepsilon/L$; la desigualdad estricta de entrada da error de salida menor que $\varepsilon$. Cauchy proporciona un corte para esta tolerancia de entrada y controla todos los pares de imágenes. Si $L=0$, cualquier par tiene distancia de salida cero, así que sirve cualquier radio y cualquier sucesión de imágenes existente es constante y Cauchy. Un dominio vacío no tiene sucesiones y el transporte es vacuo.

## 30.32. Distancia cero sin pertenencia

[]{#MA-EX-ANM-01-030-032}

[]{#MA-SOL-ANM-01-030-032}

Para $x<0$, el ínfimo es $-x$ al acercar entradas a cero; para $0\le x\le1$ es cero; para $x>1$ es $x-1$ al acercar entradas a uno. El cero ocurre en $[0,1]=\operatorname{cl}A$, no sólo en $A$. El ínfimo se alcanza únicamente si $0<x<1$, tomando la propia entrada como punto de $A$. En cero y uno no se alcanza, y fuera del cerrado tampoco, pues sus extremos no están en $A$. La función es $1$-Lipschitz por el teorema general.

## 30.33. Continuidad que destruye Cauchy

[]{#MA-EX-ANM-01-030-033}

[]{#MA-SOL-ANM-01-030-033}

En un centro $a>0$, si $|x-a|<a/2$ entonces $|1/x-1/a|\le2|x-a|/a^2$. El radio $\min\{a/2,\varepsilon a^2/2\}$ sirve. Para $x_n=1/(n+2)$, $y_n=1/(n+3)$, las separaciones de entrada $1/((n+2)(n+3))$ tienden a cero y las de salida valen uno. Con tolerancia fija $1/2$ no hay radio uniforme. La primera sucesión es Cauchy por su cola recíproca, mientras las imágenes $n+2$ tienen vecinos a distancia uno y niegan Cauchy.

## 30.34. Un supremo que no se alcanza

[]{#MA-EX-ANM-01-030-034}

[]{#MA-SOL-ANM-01-030-034}

El error de $f_n$ es $t^{n+1}$ antes del extremo y cero en él. Siempre es menor que uno, pero se aproxima arbitrariamente a uno cuando $t$ se acerca a $1$ desde la izquierda, luego el supremo es exactamente uno y no se alcanza. Por ello no hay convergencia métrica, aunque cada entrada converja. Para $g_n$, el destino es cero y el máximo de error es $1/(n+1)$, alcanzado en $t=1$, de modo que sí hay convergencia en el supremo. El criterio se refiere al supremo, no sólo a errores estrictos en entradas individuales.

**Retorno visual.** Véase [C30-F07](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.35. Una distancia de funciones bien definida

[]{#MA-EX-ANM-01-030-035}

[]{#MA-SOL-ANM-01-030-035}

Las cotas de cada función hacen finitas y acotadas las magnitudes $|f(t)-g(t)|$; al ser $T$ no vacío, completitud por supremo de C3 construye un número real $D_\infty$. Si es cero, todas las magnitudes son cero y las funciones coinciden. Simetría es puntual. La triangular puntual queda bajo la suma de los dos supremos, y tomar el tercero prueba triangular. Si las distancias tienden a cero, controlan todas las entradas. A la inversa, uniformidad con tolerancia $\varepsilon/2$ da supremo a lo sumo $\varepsilon/2<\varepsilon$. Se usa completitud de los valores reales para definir supremos; no se ha demostrado aquí completitud del espacio de funciones.

## 30.36. Un par y dos métricas

[]{#MA-EX-ANM-01-030-036}

[]{#MA-SOL-ANM-01-030-036}

[]{#MA-SEC-ANM-01-030-008}

Las magnitudes de coordenadas son $3$ y $4$, por lo que $d_1=7$ y $d_\infty=4$, con $4\le7\le8$. En general, para magnitudes $u,v\ge0$, $\max\{u,v\}\le u+v\le2\max\{u,v\}$. Aplicarlo al par de coordenadas prueba $d_\infty\le d_1\le2d_\infty$ para todos los puntos. Las constantes positivas convierten bolas, cortes de convergencia y pares de Cauchy.

## 30.37. Recortar una métrica

[]{#MA-EX-ANM-01-030-037}

[]{#MA-SOL-ANM-01-030-037}

La positividad separadora y simetría son directas. La triangular se obtiene de monotonía del mínimo y $\min\{1,u+v\}\le\min\{1,u\}+\min\{1,v\}$: si algún sumando es al menos uno, la derecha domina uno; si no, es $u+v$. Para convertir un control en $e$ a $d$, use tolerancia $\eta=\min\{\varepsilon/2,1/2\}$. La distancia menor que $\eta$ es menor que uno, donde $e=d$, y menor que $\varepsilon$. La vuelta usa $e\le d$. Todo $X$ está en una bola de radio dos para $e$ si hay un centro, mientras $\mathbb R$ no es acotada en la usual.

## 30.38. Una métrica con los mismos abiertos

[]{#MA-EX-ANM-01-030-038}

[]{#MA-SOL-ANM-01-030-038}

$\phi$ es biyectiva hacia $(-1,1)$ con inversa $\psi(t)=t/(1-|t|)$, pues $1-|\phi(x)|=1/(1+|x|)$ da $\psi(\phi(x))=x$, y $1+|\psi(t)|=1/(1-|t|)$ da $\phi(\psi(t))=t$ para $|t|<1$. La separación de $e_\phi$ usa inyectividad, y simetría/triangular usan la distancia usual de las imágenes. Ambas funciones son continuas por las reglas reales y denominadores positivos. Las bolas $e_\phi$ son preimágenes de bolas relativas por $\phi$, abiertas usuales. Para un abierto usual $U$, $\phi[U]=\psi^{-1}[U]$ es abierto relativo; una bola de salida dentro de él vuelve a una bola $e_\phi$ dentro de $U$. Así cada tipo de abierto es del otro tipo, sin una cota uniforme global presupuesta.

## 30.39. Misma topología, otra Cauchy

[]{#MA-EX-ANM-01-030-039}

[]{#MA-SOL-ANM-01-030-039}

En la usual, los vecinos distan uno, luego no es Cauchy y por tanto no converge; sus valores son no acotados. En $e_\phi$, las imágenes son $n/(n+1)$ y toda cola tiene separaciones a lo sumo $1/(N+1)$, así que es Cauchy. El espacio completo queda a distancia menor que dos de cualquier centro, por lo que la sucesión es acotada. Si convergiera a un real $a$, las imágenes convergerían a $\phi(a)$ y también a uno por el cálculo numérico; unicidad obligaría $\phi(a)=1$, fuera del recorrido. No tiene destino en esa métrica. La coincidencia de abiertos no preserva Cauchy ni acotación.

**Retorno visual.** Véase [C30-F08](analisis-para-matematicos-capitulo-30-espacios-metricos.html#fig-anm-c30-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 30.40. Auditar la identidad inversa

[]{#MA-EX-ANM-01-030-040}

[]{#MA-SOL-ANM-01-030-040}

La continuidad punto a punto se sigue de la igualdad de abiertos, ya probada. Para negar uniformidad, compare $n$ y $n+1$: su distancia usual es uno y la distancia $e_\phi$ es $1/((n+1)(n+2))\to0$. Con tolerancia de salida $1/2$, estos pares impiden un radio común. En contraste, la identidad de $d_\infty$ hacia $d_1$ es $2$-Lipschitz y la inversa es $1$-Lipschitz, por las desigualdades globales entre ambas. Esos certificados sí dan radios uniformes y transportan Cauchy en los dos sentidos.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 30](analisis-para-matematicos-capitulo-30-espacios-metricos.html) · [Ejercicios](analisis-para-matematicos-capitulo-30-espacios-metricos-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-30-espacios-metricos-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-30-espacios-metricos-microcontroles.html)
