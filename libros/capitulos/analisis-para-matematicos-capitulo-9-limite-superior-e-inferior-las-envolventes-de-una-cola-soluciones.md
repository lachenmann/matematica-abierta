---
content-id: MA-BCH-0240
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-009-SOLUCIONES
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
title: Soluciones — Capítulo 9
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C09_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 9](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html) · [Ejercicios](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-microcontroles.html)

## 9.1. Un extremo inicial

[]{#MA-EX-ANM-01-009-001}

[]{#MA-SOL-ANM-01-009-001}

[]{#MA-SEC-ANM-01-009-001}

$T_0=\{-4,1,7\}$, $T_1=\{-4,1\}$ y $T_N=\{1\}$ para $N\ge2$. Así $(\ell_0,u_0)=(-4,7)$, $(\ell_1,u_1)=(-4,1)$ y $(\ell_N,u_N)=(1,1)$ desde el corte dos. Se distinguen los conjuntos de valores de los infinitos conjuntos de índices.

Después de la prueba, puede retomarse la [figura 9.1](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f01) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.2. Una frontera ausente

[]{#MA-EX-ANM-01-009-002}

[]{#MA-SOL-ANM-01-009-002}

Los términos crecen desde $a_N$, así $\ell_N=2-1/(N+1)$ y se alcanza en $N$. Todos son menores que dos. Para $\eta>0$, escoger $n\ge N$ con $1/(n+1)<\eta$ da $a_n>2-\eta$, por lo que $u_N=2$ y no se alcanza.

## 9.3. Aproximación bilateral

[]{#MA-EX-ANM-01-009-003}

[]{#MA-SOL-ANM-01-009-003}

Si todo término posterior fuera a lo sumo $u_N-\eta$, ese real sería cota superior estrictamente menor que $u_N$. Si todo término fuera al menos $\ell_N+\eta$, sería cota inferior estrictamente mayor que $\ell_N$. Ambas conclusiones contradicen la optimalidad respectiva. Los valores que evitan esas contradicciones pertenecen a $T_N$ y por tanto tienen índices posteriores al corte.

## 9.4. Cuándo se retira una altura

[]{#MA-EX-ANM-01-009-004}

[]{#MA-SOL-ANM-01-009-004}

Cada índice al menos $N$ es $N$ o es al menos $N+1$, lo que prueba la igualdad; la inclusión inversa se sigue de los mismos índices. La inclusión es estricta exactamente cuando $a_N$ no reaparece en ningún índice posterior. Que se retire un índice no obliga a retirar su valor.

## 9.5. Acotación eventual

[]{#MA-EX-ANM-01-009-005}

[]{#MA-SOL-ANM-01-009-005}

Si $N_0=0$, sirve $M$. Si $N_0>0$, el prefijo contiene finitos términos y $B=\max\{M,|a_0|,\ldots,|a_{N_0-1}|\}$ es una cota de todas las magnitudes. Por tanto cada cola es no vacía y acotada y la construcción de ambos extremos finitos queda autorizada.

## 9.6. Alternancia con margen decreciente

[]{#MA-EX-ANM-01-009-006}

[]{#MA-SOL-ANM-01-009-006}

[]{#MA-SEC-ANM-01-009-002}

Con $e(N)$ par y $o(N)$ impar mínimos posteriores, $u_N=5+1/(e(N)+1)$ y $\ell_N=1-1/(o(N)+1)$. Los pares positivos relativos a tres disminuyen y los impares aumentan; los primeros disponibles dan los extremos. Las correcciones tienden a cero porque sus índices son al menos $N$. Así $\alpha=1$, $\beta=5$.

Después de la prueba, puede retomarse la [figura 9.2](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.7. Orden en dos niveles

[]{#MA-EX-ANM-01-009-007}

[]{#MA-SOL-ANM-01-009-007}

Cada cola está dentro de $T_0$, de modo que $\inf T_0\le\ell_N\le u_N\le\sup T_0$. El paso al límite conserva orden y da la cadena. Completitud da primero sup/inf reales de cada cola y después, mediante C07, los límites reales de las envolventes monótonas acotadas.

## 9.8. Invertir operaciones

[]{#MA-EX-ANM-01-009-008}

[]{#MA-SOL-ANM-01-009-008}

Cada cola contiene cero y uno. La primera expresión vale uno y la segunda cero. Son $\beta$ y $\alpha$, respectivamente; no se intercambian en general.

Después de la prueba, puede retomarse la [figura 9.2](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.9. Monotonía original

[]{#MA-EX-ANM-01-009-009}

[]{#MA-SOL-ANM-01-009-009}

$\ell_N=a_N$ porque es el menor término posterior. Sea $s=\sup T_0$. Es también supremo de cada cola: cualquier cota de una cola acota los términos anteriores porque son a lo sumo $a_N$. Así $u_N=s$ para todo $N$. C07 da $a_N\to s$, y por tanto $\alpha=\beta=s$.

## 9.10. Igualdad de límites, desigualdad de objetos

[]{#MA-EX-ANM-01-009-010}

[]{#MA-SOL-ANM-01-009-010}

La alternancia $a_n=0$ para pares y uno para impares, y la alternancia inversa $b_n=1-a_n$, son distintas en cada índice. Cada cola de ambas contiene cero y uno, por lo que sus envolventes son idénticas: $\ell_N=0,u_N=1$. Igualdad de envolventes no implica igualdad de las funciones originales.

Después de la prueba, puede retomarse la [figura 9.2](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.11. Umbral persistente

[]{#MA-EX-ANM-01-009-011}

[]{#MA-SOL-ANM-01-009-011}

[]{#MA-SEC-ANM-01-009-003}

Una cota inferior global $m$ hace que $m-1\in A$, por lo que es no vacío. Una cota superior global $M$ acota a $A$. Si $t>\beta$, sólo hay finitas visitas sobre $t$, luego $t\notin A$; así $\beta$ acota $A$. Todo $t<\beta$ pertenece a $A$ por §9.3; en particular $\beta-\varepsilon\in A$ para toda tolerancia. Ninguna cota menor que $\beta$ puede acotar a $A$, por lo que su supremo es $\beta$.

## 9.12. Umbral eventual

[]{#MA-EX-ANM-01-009-012}

[]{#MA-SOL-ANM-01-009-012}

$B$ contiene una cota superior global y es no vacío. Ningún $t<\beta$ pertenece a $B$, pues hay infinitas visitas sobre él; así $\beta$ es cota inferior. Todo $t>\beta$ pertenece a $B$, luego hay elementos arbitrariamente próximos por arriba y $\inf B=\beta$. Para la constante uno, $\beta=1\in B$ porque no hay términos mayores que uno. Para $1+1/(n+1)$, $\beta=1\notin B$ porque todos los términos son mayores.

## 9.13. Probar una frontera candidata

[]{#MA-EX-ANM-01-009-013}

[]{#MA-SOL-ANM-01-009-013}

La cota eventual implica $u_N\le4+\varepsilon$ para algún corte, y por tanto $\beta\le4+\varepsilon$. Las visitas implican $u_K>4-\varepsilon$ para cada corte y por límite $\beta\ge4-\varepsilon$. Si $\beta$ difiriera de cuatro, elegir la mitad de la distancia como tolerancia contradiría una desigualdad. Por tanto $\beta=4$, sin control sobre un posible extremo inferior distinto.

Después de la prueba, puede retomarse la [figura 9.3](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f03) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.14. Visitas con una sola tolerancia

[]{#MA-EX-ANM-01-009-014}

[]{#MA-SOL-ANM-01-009-014}

No. La constante $a_n=7/4$ satisface la visita con esa tolerancia y tiene $\beta=7/4$. Falta exigir todas las tolerancias y la cota eventual superior. Incluso todas las visitas por abajo sólo darían $\beta\ge2$.

Después de la prueba, puede retomarse la [figura 9.3](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f03) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.15. Versión inferior por umbrales

[]{#MA-EX-ANM-01-009-015}

[]{#MA-SOL-ANM-01-009-015}

El conjunto es no vacío: si $M$ acota superiormente a $a$, $M+1$ pertenece a él. Está acotado inferiormente por una cota inferior global. Si $t<\alpha$, las visitas por debajo de $t$ son finitas por la cota inferior eventual con tolerancia $(\alpha-t)/2$. Si $t>\alpha$, la condición de visitas con tolerancia $t-\alpha$ da infinitos términos menores que $t$. Por ello $\alpha$ es cota inferior y hay elementos arbitrariamente próximos por arriba, lo que identifica el ínfimo.

## 9.16. Un selector explícito

[]{#MA-EX-ANM-01-009-016}

[]{#MA-SOL-ANM-01-009-016}

[]{#MA-SEC-ANM-01-009-004}

Las selecciones $\varphi(k)=2k$ y $\psi(k)=2k+1$ son estrictamente crecientes en $\mathbb N$. Sus términos son $1+1/(2k+1)$ y $-1+1/(2k+2)$, que convergen a uno y menos uno. Para cada ε>0, una cola cumple −1−ε<a_n<1+ε, por la pequeñez del recíproco; así todos sus destinos están en [−1,1]. Como las dos selecciones alcanzan los extremos de ese intervalo, el carácter mínimo/máximo de §9.4 identifica α=−1 y β=1. La convergencia recíproca se verifica por arquimedianidad.

Después de la prueba, puede retomarse la [figura 9.4](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.17. Construcción sin elección arbitraria

[]{#MA-EX-ANM-01-009-017}

[]{#MA-SOL-ANM-01-009-017}

Para cualquier $\delta,K$, la cota superior eventual fija $H$ y las visitas por abajo después de $\max\{H,K\}$ dan un índice con $|a_n-\beta|<\delta$. Por ello existen los mínimos $n_0=\min\{n:|a_n-\beta|<1\}$ y $n_k=\min\{n\ge n_{k-1}+1:|a_n-\beta|<1/(k+1)\}$ para $k\ge1$. La recursión da aumento estricto. Para $\varepsilon>0$, elegir $K$ con $1/(K+1)<\varepsilon$; todo $k\ge K$ tiene error menor, luego la extracción converge a $\beta$.

Después de la prueba, puede retomarse la [figura 9.4](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.18. Extracción de una extracción

[]{#MA-EX-ANM-01-009-018}

[]{#MA-SOL-ANM-01-009-018}

$b$ es acotada. Sus extremos son límites de subsucesiones $b_{\psi(j)}$ por §9.4. La composición $\varphi\circ\psi$ es estrictamente creciente, de modo que ambos son destinos de $a$ y quedan en $[\alpha_a,\beta_a]$. Además $\alpha_b\le\beta_b$ por §9.2. Esto reúne toda la cadena; una extracción puede estrechar la banda.

## 9.19. Un punto intermedio ausente

[]{#MA-EX-ANM-01-009-019}

[]{#MA-SOL-ANM-01-009-019}

Cada término de cualquier extracción vale cero o uno y está a distancia exactamente $1/2$ de $1/2$. La tolerancia $1/4$ impide convergencia a ese candidato. Los destinos cero y uno se obtienen por paridad; así el confinamiento no es una caracterización de todos los puntos interiores.

Después de la prueba, puede retomarse la [figura 9.4](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f04) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.20. Destinos extremos y conjunto

[]{#MA-EX-ANM-01-009-020}

[]{#MA-SOL-ANM-01-009-020}

El conjunto contiene límites, no necesariamente términos. Las extracciones probadas llevan $\alpha,\beta$ a él y el confinamiento los compara con todos sus elementos, dando mínimo y máximo. Para $a_n=1/(n+1)$ ambos extremos son cero y el conjunto de destinos es $\{0\}$, aunque ningún término valga cero.

## 9.21. La igualdad captura toda la cola

[]{#MA-EX-ANM-01-009-021}

[]{#MA-SOL-ANM-01-009-021}

[]{#MA-SEC-ANM-01-009-005}

Fijar $\varepsilon>0$. Elegir $N_1$ con $\ell_n>L-\varepsilon$ para $n\ge N_1$ y $N_2$ con $u_n<L+\varepsilon$ para $n\ge N_2$. Con $N=\max\{N_1,N_2\}$, el encierro $\ell_n\le a_n\le u_n$ prueba $|a_n-L|<\varepsilon$ para todo $n\ge N$. No basta tomar sólo uno de los cortes.

Después de la prueba, puede retomarse la [figura 9.5](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f05) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.22. Dos amplitudes

[]{#MA-EX-ANM-01-009-022}

[]{#MA-SOL-ANM-01-009-022}

Para $a$, las correcciones recíprocas van a cero y ambos extremos son cinco, luego $\omega(a)=0$. Para $b$, toda cola contiene cuatro y seis, luego $\alpha_b=4$, $\beta_b=6$ y $\omega(b)=2$. La primera converge aunque alterna; la segunda no.

Después de la prueba, puede retomarse la [figura 9.5](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f05) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.23. Supremo de distancias

[]{#MA-EX-ANM-01-009-023}

[]{#MA-SOL-ANM-01-009-023}

Todas las distancias son a lo sumo $u_N-\ell_N$. Para $\eta>0$ escoger términos con $a_p>u_N-\eta/2$ y $a_q<\ell_N+\eta/2$ por aproximación. Su distancia es al menos $a_p-a_q>u_N-\ell_N-\eta$. El conjunto de distancias contiene cero y es acotado; la cota y su aproximación identifican su supremo.

## 9.24. Único destino

[]{#MA-EX-ANM-01-009-024}

[]{#MA-SOL-ANM-01-009-024}

Si el conjunto de destinos es $\{L\}$, sus mínimo y máximo probados en §9.4 son ambos $L$, luego $\omega=0$. Si $\omega=0$, $\alpha=\beta=L$; el confinamiento fuerza a todos los destinos a ser $L$ y la extracción extrema garantiza que existe. No se omite la no vacuidad.

## 9.25. Cuánto ve una tolerancia fija

[]{#MA-EX-ANM-01-009-025}

[]{#MA-SOL-ANM-01-009-025}

El supremo de esas distancias da $d_N\le\varepsilon$, sin garantizar desigualdad estricta. Una sola tolerancia no prueba convergencia: la alternancia cero–uno tiene todas sus distancias menores que dos y no converge. Si la condición existiera para cada tolerancia positiva, entonces $0\le\omega\le\varepsilon$ para toda $\varepsilon$ y el criterio de §9.5 daría convergencia.

Después de la prueba, puede retomarse la [figura 9.5](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f05) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.26. Modificar y desplazar

[]{#MA-EX-ANM-01-009-026}

[]{#MA-SOL-ANM-01-009-026}

[]{#MA-SEC-ANM-01-009-006}

Ambas operaciones conservan los extremos menos uno y uno. La primera cambia un valor del prefijo y deja idénticas las colas desde uno. La segunda invierte la paridad y reindexa; sus colas son las de $a$ con corte desplazado. Son funciones diferentes y operaciones diferentes.

Después de la prueba, puede retomarse la [figura 9.2](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.27. Perturbación que desaparece

[]{#MA-EX-ANM-01-009-027}

[]{#MA-SOL-ANM-01-009-027}

$r$ es acotada, luego $a+r$ lo es. Para $\varepsilon>0$, en colas suficientemente tardías $a_n-\varepsilon<a_n+r_n<a_n+\varepsilon$. Comparando supremos e ínfimos en ambas direcciones, sus extremos difieren a lo sumo en $\varepsilon$. Como vale para toda tolerancia, coinciden los dos extremos. Al restarlos coincide la oscilación.

Después de la prueba, puede retomarse la [figura 9.2](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f02) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.28. Estabilidad con margen

[]{#MA-EX-ANM-01-009-028}

[]{#MA-SOL-ANM-01-009-028}

En colas posteriores, $b_n\le a_n+\delta$ y $a_n\le b_n+\delta$, por lo que ambos supremos difieren a lo sumo en $\delta$. Las desigualdades inferiores hacen lo mismo con los ínfimos. Pasar al límite conserva todas las desigualdades. Finalmente la desigualdad triangular aplicada a $(\beta_a-\beta_b)-(\alpha_a-\alpha_b)$ da el margen $2\delta$.

## 9.29. El margen puede alcanzarse

[]{#MA-EX-ANM-01-009-029}

[]{#MA-SOL-ANM-01-009-029}

Tomar $a_n=(-1)^n\delta$ y $b_n=0$. La distancia término a término es $\delta$, los extremos de $a$ son $-\delta,\delta$ y los de $b$ son cero; así sus oscilaciones difieren en $2\delta$. La cota anterior es óptima.

## 9.30. Error persistente

[]{#MA-EX-ANM-01-009-030}

[]{#MA-SOL-ANM-01-009-030}

No. Si $a_n=0$, la suma es la alternancia menos uno–uno. Los extremos cambian de cero y cero a menos uno y uno. El error es acotado pero no tiende a cero; acotación sola no da invariancia.

## 9.31. Escala negativa

[]{#MA-EX-ANM-01-009-031}

[]{#MA-SOL-ANM-01-009-031}

[]{#MA-SEC-ANM-01-009-007}

La escala negativa intercambia los extremos: $\alpha(-4a)=-12$ y $\beta(-4a)=8$. Al trasladar por uno resultan $-11$ y nueve; la oscilación es veinte, también igual a $4(3-(-2))$.

## 9.32. Suma con desacuerdo temporal

[]{#MA-EX-ANM-01-009-032}

[]{#MA-SOL-ANM-01-009-032}

La suma es cero, por lo que ambos extremos de la suma son cero. Las fronteras superiores separadas suman dos y las inferiores menos dos. Ambas desigualdades generales son estrictas, porque las alturas extremas de los sumandos aparecen en paridades opuestas.

Después de la prueba, puede retomarse la [figura 9.6](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f06) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.33. Intervalo más preciso para la suma

[]{#MA-EX-ANM-01-009-033}

[]{#MA-SOL-ANM-01-009-033}

Escoger una extracción $a_{n_k}\to\beta_a$. Para $\varepsilon>0$, eventualmente $a_{n_k}>\beta_a-\varepsilon$ y $b_{n_k}>\alpha_b-\varepsilon$. Son visitas arbitrariamente tardías de la suma sobre $\beta_a+\alpha_b-2\varepsilon$, luego $\beta(a+b)\ge\beta_a+\alpha_b-2\varepsilon$ por la caracterización de visitas o por los supremos de cola. Dejar $\varepsilon$ arbitraria da la primera cota; intercambiar $a,b$ da la otra. Para la inferior usar la extracción $a_{m_k}\to\alpha_a$ y la cota eventual $b_n<\beta_b+\varepsilon$: da visitas tardías de la suma por debajo de $\alpha_a+\beta_b+2\varepsilon$, luego $\alpha(a+b)\le\alpha_a+\beta_b$. Intercambiar los sumandos da la última cota.

## 9.34. Producto y signo

[]{#MA-EX-ANM-01-009-034}

[]{#MA-SOL-ANM-01-009-034}

En cada cola los extremos son no negativos y $\ell_N(a)\ell_N(b)\le a_nb_n\le u_N(a)u_N(b)$. El producto es acotado; tomar extremos y límites da $\alpha(ab)\ge\alpha_a\alpha_b$ y $\beta(ab)\le\beta_a\beta_b$. Si $a_n=b_n$ alternan entre menos dos y menos uno, los extremos superiores son menos uno y su producto es uno, pero $\beta(ab)=4$. La cota superior falla sin control de signo.

## 9.35. Un sumando convergente

[]{#MA-EX-ANM-01-009-035}

[]{#MA-SOL-ANM-01-009-035}

La suma es acotada porque ambos sumandos lo son. Escribir $a_n+b_n=(a_n+B)+(b_n-B)$, donde el segundo término tiende a cero. La estabilidad y la traslación dan $\alpha(a+b)=\alpha_a+B$ y $\beta(a+b)=\beta_a+B$. Al restar, $\omega(a+b)=\omega(a)$: el sumando convergente traslada las fronteras y conserva su distancia.

Después de la prueba, puede retomarse la [figura 9.6](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html#fig-anm-c09-f06) para contrastar el mecanismo con el ejemplo del capítulo.

## 9.36. Picos cada vez más separados

[]{#MA-EX-ANM-01-009-036}

[]{#MA-SOL-ANM-01-009-036}

[]{#MA-SEC-ANM-01-009-008}

Las potencias superan cualquier corte porque $2^j\ge j+1$. Los índices $2^j+1$ para $j\ge1$ crecen y están estrictamente entre $2^j$ y $2^{j+1}$, por lo que no son potencias. Cada cola contiene cero y uno, y sus extremos son cero y uno. Ambos son destinos por selecciones crecientes de esos índices; ningún otro real puede ser destino porque la imagen es el conjunto finito $\{0,1\}$.

## 9.37. Todos los puntos de un intervalo

[]{#MA-EX-ANM-01-009-037}

[]{#MA-SOL-ANM-01-009-037}

Todos los términos están en $[0,1]$ y cada bloque contiene ambos extremos, por lo que cada cola contiene cero y uno y $\alpha=0,\beta=1$. Para $x\in[0,1]$, en cada bloque escoger el menor entero $j_m\in\{0,\ldots,m\}$ con $j_m/m\ge x$. Existe porque $m/m=1$. Si $j_m>0$, minimalidad da $(j_m-1)/m<x$, luego $0\le j_m/m-x<1/m$; si $j_m=0$, $x=0$ y el error es cero. Los índices originales aumentan porque se toma un término de cada bloque consecutivo. La extracción converge a $x$ por arquimedianidad. Ningún destino queda fuera del intervalo por confinamiento.

## 9.38. Misma banda, distintos destinos

[]{#MA-EX-ANM-01-009-038}

[]{#MA-SOL-ANM-01-009-038}

La alternancia menos dos–tres tiene destinos exactamente $\{-2,3\}$. El patrón periódico menos dos–cero–tres tiene destinos exactamente $\{-2,0,3\}$. Cada valor del patrón aparece en una clase de índices y produce una subsucesión constante. Ningún real externo a la imagen finita puede ser destino porque su distancia mínima a esa imagen es positiva. Las colas contienen todos los valores del patrón, luego ambas bandas son $[-2,3]$.

## 9.39. Un destino sin acotación

[]{#MA-EX-ANM-01-009-039}

[]{#MA-SOL-ANM-01-009-039}

Los pares dan una extracción constante cero. Si una subsucesión convergente incluyera infinitos términos impares, éstos formarían una extracción con índices $2k+1$ crecientes y valores $k+1$ sin cota; eso contradice que toda convergente y sus subsucesiones son acotadas. Por tanto toda extracción convergente es eventualmente par y su límite es cero. La sucesión original no es acotada, así que no converge en $\mathbb R$. Sus colas carecen de supremo real; los extremos finitos del capítulo y el criterio que los usa requieren acotación.

## 9.40. Saltos pequeños llenan la banda

[]{#MA-EX-ANM-01-009-040}

[]{#MA-SOL-ANM-01-009-040}

Fijar $L$ interior y $\varepsilon>0$. Las visitas de §9.3 proporcionan términos menores que $L$ arbitrariamente tarde, porque escoger tolerancia $(L-\alpha)/2$ los mantiene debajo. También hay términos mayores que $L$ después de cualquier corte por tolerancia $(\beta-L)/2$. Elegir $H$ con saltos menores que $\varepsilon$ para $n\ge H$. Dado cualquier corte $K$, escoger $p\ge\max\{H,K\}$ con $a_p<L$ y después $q>p$ con $a_q>L$. Sea $r$ el primer índice de $\{p+1,\ldots,q\}$ con $a_r\ge L$. Entonces $a_{r-1}<L\le a_r$ y $0\le a_r-L\le a_r-a_{r-1}<\varepsilon$. Se obtienen visitas a la bola de $L$ después de cualquier corte; C08 o la construcción de mínimos de §9.4 produce una extracción convergente a $L$. Los extremos ya son destinos y todos los destinos están confinados en la banda. La condición de saltos se usa en el primer cruce, y la acotación en la existencia de las fronteras.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 9](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html) · [Ejercicios](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-microcontroles.html)
