---
title: "Soluciones de microcontroles — Capítulo 5"
content-id: MA-BCH-0182
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-005-MICROCONTROLES
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-10-07
date-modified: 2026-10-07
areas: [analisis]
level: universitario
topics: [analisis-real, sucesiones, eventualidad]
prerequisites: [MA-BCH-0083]
related: [MA-BOK-0010]
provenance:
  type: original
  sources:
    - "ANM-C05_MICROCONTROLES_SOLUCIONES.md, fuente canónica ANM; paquete C05 cerrado."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 5](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.md) · [Ejercicios](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-microcontroles.md)

## §5.1 — Una sucesión es una función: índice y término

### Microcontrol 001

[]{#MA-MIC-ANM-01-005-001}

[]{#MA-MSOL-ANM-01-005-001}

[]{#MA-SEC-ANM-01-005-001}

1. Sea $a_n=3n-2$. Identifica el dominio, el codominio, el índice y el término cuando $n=4$.

**Solución.** La sucesión es la función $a:\mathbb N\to\mathbb R$ dada por $a(n)=3n-2$. Su dominio es $\mathbb N=\{0,1,2,\ldots\}$ y su codominio es $\mathbb R$. Al fijar $n=4$, el índice es $4\in\mathbb N$ y el término correspondiente es $a_4=3\cdot4-2=10\in\mathbb R$. La función $a$, la entrada $4$ y el valor $10$ cumplen papeles distintos.

### Microcontrol 002

[]{#MA-MIC-ANM-01-005-002}

[]{#MA-MSOL-ANM-01-005-002}

2. Escribe los primeros cinco términos de $a_n=1/(n+1)$ usando la convención $\mathbb N=\{0,1,2,\ldots\}$.

**Solución.** Los primeros cinco índices son $0,1,2,3,4$. Sustituyéndolos en la fórmula obtenemos $a_0=1$, $a_1=1/2$, $a_2=1/3$, $a_3=1/4$ y $a_4=1/5$. Por tanto, los primeros cinco términos, en su orden, son $(1,1/2,1/3,1/4,1/5)$. Comenzar en $n=1$ omitiría el primer término.

### Microcontrol 003

[]{#MA-MIC-ANM-01-005-003}

[]{#MA-MSOL-ANM-01-005-003}

3. Explica por qué las expresiones $f(x)=x^2$ con $f:\mathbb R\to\mathbb R$ y $a_n=n^2$ con $a:\mathbb N\to\mathbb R$ no definen el mismo objeto matemático.

**Solución.** Los dominios son diferentes: $f$ admite cualquier entrada real, mientras que $a$ sólo admite índices naturales; ambas tienen codominio $\mathbb R$. Por ejemplo, $f(1/2)=1/4$ está definido, pero $a_{1/2}$ no está definido porque $1/2\notin\mathbb N$. Para cada $n\in\mathbb N$ sí se cumple $a_n=f(n)$: $a$ es la restricción de $f$ a $\mathbb N$. Esa coincidencia de valores en los naturales no hace iguales las dos funciones, pues el dominio forma parte del objeto.

### Microcontrol 004

[]{#MA-MIC-ANM-01-005-004}

[]{#MA-MSOL-ANM-01-005-004}

4. Decide si la frase «$a_3$ es el tercer índice de la sucesión» es correcta. Si no lo es, reescríbela con los tipos adecuados.

**Solución.** La frase es incorrecta. La redacción adecuada es: «$a_3$ es el término de índice $3$ de la sucesión». El índice es $3\in\mathbb N$ y el término es $a_3=a(3)\in\mathbb R$. Con la indexación desde $0$, $3$ ocupa la cuarta posición entre los índices y $a_3$ es el cuarto término. Aunque en alguna sucesión se tenga $a_3=3$, esa igualdad numérica no identifica el papel de entrada con el de salida ni identifica un término con la función completa.

### Microcontrol 005

[]{#MA-MIC-ANM-01-005-005}

[]{#MA-MSOL-ANM-01-005-005}

5. Sean $a,b:\mathbb N\to\mathbb R$ tales que $a_n=b_n$ para todo $n\in\mathbb N$. Justifica, usando la definición de igualdad de funciones, por qué $a=b$.

**Solución.** Las funciones $a$ y $b$ tienen el mismo dominio $\mathbb N$ y el mismo codominio $\mathbb R$. La hipótesis dice que, para cada entrada $n\in\mathbb N$, sus valores satisfacen $a(n)=a_n=b_n=b(n)$. Como la igualdad de funciones exige precisamente el mismo dominio, el mismo codominio y la misma asignación en cada entrada, se concluye que $a=b$.

### Microcontrol 006

[]{#MA-MIC-ANM-01-005-006}

[]{#MA-MSOL-ANM-01-005-006}

6. Construye una sucesión real en la que el mismo valor aparezca en infinitos índices distintos. Explica por qué esto no contradice que una sucesión sea una función.

**Solución.** Definamos $a:\mathbb N\to\mathbb R$ por $a(n)=2$ para todo $n\in\mathbb N$. El valor $2$ aparece en todos los índices $0,1,2,\ldots$, que son infinitos y distintos. Cada índice recibe un único valor, como exige la definición de función; la definición permite que índices diferentes reciban el mismo valor.

### Microcontrol 007

[]{#MA-MIC-ANM-01-005-007}

[]{#MA-MSOL-ANM-01-005-007}

7. En una gráfica de puntos $(n,a_n)$ alguien une todos los puntos con una curva y afirma que esa curva «es la sucesión». Localiza el error.

**Solución.** La gráfica de la sucesión es la colección discreta $\{(n,a_n):n\in\mathbb N\}$. Al unir los puntos se añaden puntos cuyas primeras coordenadas pueden no ser naturales; por ejemplo, no existe un término de índice $1/2$. La curva es una representación adicional escogida por quien dibuja y no la gráfica de la función $a:\mathbb N\to\mathbb R$. Incluso los puntos originales representan la sucesión: la función queda definida por sus asignaciones en los índices naturales.

### Microcontrol 008

[]{#MA-MIC-ANM-01-005-008}

[]{#MA-MSOL-ANM-01-005-008}

8. En la notación $\{a_n:n\in\mathbb N\}$ se ha olvidado parte de la información de la sucesión. Sin desarrollar todavía §5.2, indica qué clase de información sospechas que ya no puede recuperarse.

**Solución.** El conjunto conserva qué valores aparecen, pero no registra qué valor corresponde a cada índice. Por ello se pierde el orden de aparición y la información sobre repeticiones: en qué índices se repite un valor y cuántas veces aparece. Esos datos pertenecen a la asignación $n\mapsto a_n$ y no quedan guardados al reunir los valores en un conjunto.

## §5.2 — El orden de las visitas importa

### Microcontrol 009

[]{#MA-MIC-ANM-01-005-009}

[]{#MA-MSOL-ANM-01-005-009}

[]{#MA-SEC-ANM-01-005-002}

1. Para $a_n=(-1)^n$, determina el conjunto de valores y explica qué información de la sucesión no queda registrada en ese conjunto.

**Solución.** Si $n=2k$ con $k\in\mathbb N$, entonces $a_n=1$; si $n=2k+1$, entonces $a_n=-1$. Ambos valores aparecen, por ejemplo en $n=0$ y $n=1$, y no aparece ningún otro. Por tanto, el conjunto de valores es $\{-1,1\}\subseteq\mathbb R$. Ese conjunto no registra que $1$ corresponde a los índices pares y $-1$ a los impares, ni el orden de las visitas ni sus repeticiones.

### Microcontrol 010

[]{#MA-MIC-ANM-01-005-010}

[]{#MA-MSOL-ANM-01-005-010}

2. Sean $a=(0,1,0,1,\ldots)$ y $b=(0,0,1,1,0,0,1,1,\ldots)$. Demuestra que tienen el mismo conjunto de valores pero que $a\ne b$.

**Solución.** Cada una de las dos sucesiones toma sólo los valores $0$ y $1$, y ambas toman los dos: en $a$ aparecen en los índices $0$ y $1$, y en $b$ en los índices $0$ y $2$. Sus conjuntos de valores son, por tanto, $\{0,1\}$. Sin embargo, $a_1=1$ y $b_1=0$; la diferencia en esa entrada impide la igualdad de las funciones $a,b:\mathbb N\to\mathbb R$.

### Microcontrol 011

[]{#MA-MIC-ANM-01-005-011}

[]{#MA-MSOL-ANM-01-005-011}

3. Construye dos sucesiones distintas con conjunto de valores $\{0,1,2\}$ y con órdenes de aparición diferentes.

**Solución.** Definamos $a,b:\mathbb N\to\mathbb R$ mediante $a_0=0$, $a_1=1$, $a_n=2$ para $n\ge2$, y $b_0=1$, $b_1=0$, $b_n=2$ para $n\ge2$. Así, $a=(0,1,2,2,2,\ldots)$ y $b=(1,0,2,2,2,\ldots)$. En ambas aparecen los tres valores $0,1,2$ y ningún otro. El orden de aparición de $0$ y $1$ está intercambiado, y $a_0=0\ne1=b_0$ prueba que son distintas.

### Microcontrol 012

[]{#MA-MIC-ANM-01-005-012}

[]{#MA-MSOL-ANM-01-005-012}

4. Construye dos sucesiones con el mismo conjunto de valores en las que el valor $0$ tenga patrones de repetición distintos. Describe la diferencia usando índices concretos.

**Solución.** Tomemos $a_0=0$ y $a_n=1$ para $n\ge1$. Definamos $b_{2k}=0$ y $b_{2k+1}=1$ para cada $k\in\mathbb N$. Ambas son funciones $\mathbb N\to\mathbb R$ con conjunto de valores $\{0,1\}$. En $a$, el valor $0$ aparece sólo en el índice $0$; en $b$, aparece en los índices $0,2,4,6,\ldots$. Por ejemplo, $a_2=a_4=1$, mientras que $b_2=b_4=0$. El conjunto de valores no distingue esos patrones.

### Microcontrol 013

[]{#MA-MIC-ANM-01-005-013}

[]{#MA-MSOL-ANM-01-005-013}

5. Demuestra que si $a=b$ como sucesiones, entonces $\{a_n:n\in\mathbb N\}=\{b_n:n\in\mathbb N\}$. Explica por qué el recíproco falla.

**Solución.** Sea $x\in\{a_n:n\in\mathbb N\}$. Existe un índice $m\in\mathbb N$ con $x=a_m$. Como $a=b$, se tiene $a_m=b_m$, de modo que $x$ pertenece también al conjunto de valores de $b$. Esto prueba una inclusión; intercambiando $a$ y $b$ obtenemos la otra y, por tanto, la igualdad de conjuntos. El recíproco falla: las sucesiones $(0,1,0,1,\ldots)$ y $(0,0,1,1,0,0,1,1,\ldots)$ tienen conjunto de valores $\{0,1\}$, pero sus términos de índice $1$ son diferentes.

### Microcontrol 014

[]{#MA-MIC-ANM-01-005-014}

[]{#MA-MSOL-ANM-01-005-014}

6. Sea $p_n=n$ y define $q=(1,0,2,3,4,\ldots)$. Verifica que $p$ y $q$ tienen el mismo conjunto de valores y localiza un índice que pruebe que son distintas.

**Solución.** El conjunto de valores de $p$ es $\mathbb N$, considerado como subconjunto de $\mathbb R$: cada natural $k$ aparece como $p_k=k$. Para $q$, tenemos $q_0=1$, $q_1=0$ y $q_n=n$ para $n\ge2$. Todos sus valores son naturales; además, $0$ aparece en el índice $1$, $1$ en el índice $0$ y cada $k\ge2$ en el índice $k$. Por tanto, su conjunto de valores también es $\mathbb N$. Las sucesiones son distintas porque $p_0=0\ne1=q_0$.

### Microcontrol 015

[]{#MA-MIC-ANM-01-005-015}

[]{#MA-MSOL-ANM-01-005-015}

7. Si $\sigma:\mathbb N\to\mathbb N$ es biyectiva y $b_n=a_{\sigma(n)}$, demuestra directamente que $a$ y $b$ tienen el mismo conjunto de valores. ¿Por qué eso no prueba que $a=b$?

**Solución.** Si $x$ es un valor de $b$, existe $n\in\mathbb N$ tal que $x=b_n=a_{\sigma(n)}$. Como $\sigma(n)\in\mathbb N$, $x$ es un valor de $a$. Recíprocamente, si $x=a_m$ para algún $m\in\mathbb N$, la sobreyectividad de $\sigma$ proporciona un $n\in\mathbb N$ con $\sigma(n)=m$; entonces $x=a_m=b_n$. Las dos inclusiones prueban la igualdad de conjuntos de valores. Esta prueba permite que el índice $n$ de $b$ sea distinto del índice $m$ de $a$, mientras que $a=b$ exigiría $a_n=a_{\sigma(n)}$ para cada mismo índice $n$. Por ejemplo, con $a_n=n$ y la biyección que intercambia $0$ y $1$ y deja fijos los demás índices, resulta $a_0=0$ y $b_0=1$.

### Microcontrol 016

[]{#MA-MIC-ANM-01-005-016}

[]{#MA-MSOL-ANM-01-005-016}

8. Explica con tus propias palabras qué información conserva la lista ordenada $(a_0,a_1,a_2,\ldots)$ que desaparece al pasar al conjunto $\{a_n:n\in\mathbb N\}$.

**Solución.** La lista ordenada permite recuperar el valor asignado a cada índice: la primera entrada es $a_0$, la segunda es $a_1$, y así sucesivamente. Conserva en qué posiciones aparece cada valor, el orden de las visitas y las repeticiones. El conjunto $\{a_n:n\in\mathbb N\}$ guarda únicamente qué valores aparecen al menos una vez; no indica sus posiciones ni cuántas veces se repiten.

## §5.3 — Ver una sucesión sin perder el índice

### Microcontrol 017

[]{#MA-MIC-ANM-01-005-017}

[]{#MA-MSOL-ANM-01-005-017}

[]{#MA-SEC-ANM-01-005-003}

1. Para $a_n=3-2n$, escribe los primeros cinco términos, una tabla con índices $0$ a $4$ y los cinco puntos correspondientes de la gráfica discreta.

**Solución.** Al evaluar $a_n=3-2n$ en $n=0,1,2,3,4$, obtenemos los términos $(3,1,-1,-3,-5)$ en ese orden. La tabla mantiene explícita cada entrada y su valor:

| $n$ | $a_n$ |
|---:|---:|
| $0$ | $3$ |
| $1$ | $1$ |
| $2$ | $-1$ |
| $3$ | $-3$ |
| $4$ | $-5$ |

Los cinco puntos correspondientes son $(0,3)$, $(1,1)$, $(2,-1)$, $(3,-3)$ y $(4,-5)$. Son puntos de la gráfica discreta de $a:\mathbb N\to\mathbb R$; no se añaden segmentos entre ellos.

### Microcontrol 018

[]{#MA-MIC-ANM-01-005-018}

[]{#MA-MSOL-ANM-01-005-018}

2. En la sucesión $b_n=(-1)^n$, explica por qué los puntos $(0,1)$ y $(2,1)$ contienen más información que la sola marca $1$ sobre la recta real.

**Solución.** Los puntos $(0,1)$ y $(2,1)$ registran las dos asignaciones $b_0=1$ y $b_2=1$. Tienen la misma coordenada vertical, pero son distintos porque sus primeras coordenadas son $0$ y $2$. Una sola marca en $1$ sobre la recta real indica que ese valor aparece; sin etiquetas no identifica ninguno de esos índices ni muestra que corresponda a más de una entrada.

### Microcontrol 019

[]{#MA-MIC-ANM-01-005-019}

[]{#MA-MSOL-ANM-01-005-019}

3. Un estudiante dibuja los puntos de $a_n=n^2$ y los une con la parábola $y=x^2$. Explica qué parte del dibujo representa la sucesión y qué parte es información adicional.

**Solución.** La sucesión está representada por los puntos $\{(n,n^2):n\in\mathbb N\}$, con dominio $\mathbb N=\{0,1,2,\ldots\}$ y codominio $\mathbb R$. La parábola completa es la gráfica de la función $f:\mathbb R\to\mathbb R$, $f(x)=x^2$. Contiene los puntos de la sucesión, pero también puntos como $(1/2,1/4)$, que no pertenecen a ella porque $1/2$ no es un índice natural. Toda parte de la curva ajena a los puntos de índice natural es información adicional.

### Microcontrol 020

[]{#MA-MIC-ANM-01-005-020}

[]{#MA-MSOL-ANM-01-005-020}

4. Decide si una lista ordenada puede representar correctamente una sucesión sin escribir explícitamente todos los índices. ¿Qué convención permite hacerlo?

**Solución.** Sí, si se fija la convención $\mathbb N=\{0,1,2,\ldots\}$ y se escriben los términos en ese orden: el primer lugar de $(a_0,a_1,a_2,\ldots)$ corresponde al índice $0$, el segundo al índice $1$ y el lugar $n+1$ al índice $n$. Así los índices quedan implícitos en las posiciones. Una lista de sólo unos pocos términos, acompañada de puntos suspensivos sin una regla de continuación determinada, no especifica por sí sola toda la función.

### Microcontrol 021

[]{#MA-MIC-ANM-01-005-021}

[]{#MA-MSOL-ANM-01-005-021}

5. Da un ejemplo de una representación sobre la recta real que pierda información de índice y explica cómo repararla mediante etiquetas.

**Solución.** Para $b_n=(-1)^n$, marcar únicamente $-1$ y $1$ en la recta real representa su conjunto de valores y pierde la asignación a los índices. Se repara asociando a la marca $1$ las etiquetas $n=0,2,4,\ldots$ y a la marca $-1$ las etiquetas $n=1,3,5,\ldots$, o indicando respectivamente «$n=2k$, $k\in\mathbb N$» y «$n=2k+1$, $k\in\mathbb N$». Las etiquetas permiten recuperar qué valor corresponde a cada índice, incluidas las repeticiones.

### Microcontrol 022

[]{#MA-MIC-ANM-01-005-022}

[]{#MA-MSOL-ANM-01-005-022}

6. Para $a_n=2n-1$, localiza la afirmación $a_3=5$ en la fórmula, la lista, la tabla y la gráfica discreta.

**Solución.** En la fórmula, sustituir $n=3$ da $a_3=2\cdot3-1=5$. En la lista $(-1,1,3,5,7,\ldots)$, el $5$ ocupa el cuarto lugar, que corresponde al índice $3$ porque se comienza en $0$. En la tabla, la afirmación está en la fila con entrada $3$ y valor $5$. En la gráfica discreta, está representada por el punto $(3,5)$. Los cuatro registros conservan la misma asignación $3\mapsto5$.

### Microcontrol 023

[]{#MA-MIC-ANM-01-005-023}

[]{#MA-MSOL-ANM-01-005-023}

7. Explica por qué una fórmula cerrada no forma parte de la definición de sucesión, aunque muchas sucesiones de ejemplo se presenten mediante fórmulas.

**Solución.** La definición exige una función $a:\mathbb N\to\mathbb R$: a cada índice natural debe corresponderle un único valor real. No exige que esa asignación tenga una fórmula cerrada. Una fórmula es una manera de describir la función; también la describe la colección completa de sus pares $(n,a_n)$, y dos expresiones diferentes pueden determinar la misma asignación. Por ello, usar fórmulas en muchos ejemplos no añade una condición a la definición general.

### Microcontrol 024

[]{#MA-MIC-ANM-01-005-024}

[]{#MA-MSOL-ANM-01-005-024}

8. Compara el conjunto $\{a_n:n\in\mathbb N\}$ con la gráfica $\{(n,a_n):n\in\mathbb N\}$. ¿Cuál de los dos conserva necesariamente el índice?

**Solución.** El conjunto de valores $\{a_n:n\in\mathbb N\}\subseteq\mathbb R$ conserva sólo los valores que aparecen. La gráfica $\{(n,a_n):n\in\mathbb N\}\subseteq\mathbb N\times\mathbb R$ conserva necesariamente el índice en la primera coordenada y su término en la segunda. Para cada $n$, su único punto de primera coordenada $n$ permite recuperar $a_n$. Si un valor se repite, los pares siguen siendo distintos por sus índices; el conjunto de valores reúne todas esas apariciones en un solo elemento.

## §5.4 — Colas: olvidar un comienzo finito

### Microcontrol 025

[]{#MA-MIC-ANM-01-005-025}

[]{#MA-MSOL-ANM-01-005-025}

[]{#MA-SEC-ANM-01-005-004}

1. Para $a_n=2n+1$ y $N=3$, escribe la cola restringida desde $3$ indicando su dominio y calcula sus primeros cuatro valores.

**Solución.** La cola restringida es $a|_{\mathbb N_{\ge3}}:\mathbb N_{\ge3}\to\mathbb R$, con dominio $\{3,4,5,\ldots\}$ y regla $n\mapsto2n+1$. Sus primeros cuatro valores, en los índices originales $3,4,5,6$, son $7,9,11,13$.

### Microcontrol 026

[]{#MA-MIC-ANM-01-005-026}

[]{#MA-MSOL-ANM-01-005-026}

2. Para la misma sucesión, escribe la cola reindexada $a^{\langle3\rangle}$ y verifica que $a^{\langle3\rangle}_2=a_5$.

**Solución.** La cola reindexada tiene dominio $\mathbb N$ y regla $a^{\langle3\rangle}_k=a_{3+k}=2(3+k)+1=2k+7$. Al tomar $k=2$, resulta $a^{\langle3\rangle}_2=11=a_5$. El nuevo índice $2$ corresponde al antiguo índice $5$.

### Microcontrol 027

[]{#MA-MIC-ANM-01-005-027}

[]{#MA-MSOL-ANM-01-005-027}

3. Explica por qué $a|_{\mathbb N_{\ge3}}$ y $a^{\langle3\rangle}$ contienen la misma información ordenada pero no son la misma función.

**Solución.** La restricción conserva los índices $3,4,5,\ldots$; la reindexación usa $0,1,2,\ldots$ y asigna a $k$ el antiguo valor $a_{3+k}$. El corrimiento biyectivo $k\mapsto3+k$ permite recuperar una representación desde la otra sin alterar el orden. Sus dominios son distintos, de modo que no son la misma función, aunque tengan el mismo codominio $\mathbb R$.

### Microcontrol 028

[]{#MA-MIC-ANM-01-005-028}

[]{#MA-MSOL-ANM-01-005-028}

4. Sea $a=(5,8,1,0,1,0,1,0,\ldots)$. Para $N=2$, determina la cola reindexada y el conjunto de valores tardíos. ¿Qué información pierde el segundo objeto?

**Solución.** La cola reindexada desde $2$ es $a^{\langle2\rangle}=(1,0,1,0,\ldots)$, con valor $1$ en índices nuevos pares y $0$ en impares. El conjunto de valores tardíos es $\{0,1\}$. Este conjunto olvida las posiciones originales y nuevas, el orden de alternancia y las repeticiones.

### Microcontrol 029

[]{#MA-MIC-ANM-01-005-029}

[]{#MA-MSOL-ANM-01-005-029}

5. Demuestra directamente que $\tau_N(k)=N+k$ es biyectiva de $\mathbb N$ sobre $\mathbb N_{\ge N}$.

**Solución.** Para $k\in\mathbb N$, $N+k\ge N$, por lo que $\tau_N$ toma valores en $\mathbb N_{\ge N}$. Si $N+k=N+\ell$, la cancelación da $k=\ell$, luego es inyectiva. Dado $n\in\mathbb N_{\ge N}$, el natural $k=n-N$ satisface $\tau_N(k)=n$; por tanto es sobreyectiva y, en consecuencia, biyectiva.

### Microcontrol 030

[]{#MA-MIC-ANM-01-005-030}

[]{#MA-MSOL-ANM-01-005-030}

6. Si $M\ge N$, demuestra que $\{a_n:n\ge M\}\subseteq\{a_n:n\ge N\}$.

**Solución.** Sea $x\in\{a_n:n\ge M\}$. Existe $n\in\mathbb N$ con $n\ge M$ y $x=a_n$. Como $M\ge N$, también $n\ge N$, de modo que $x\in\{a_n:n\ge N\}$. Esto prueba la inclusión.

### Microcontrol 031

[]{#MA-MIC-ANM-01-005-031}

[]{#MA-MSOL-ANM-01-005-031}

7. Verifica la identidad $a^{\langle M\rangle}=(a^{\langle N\rangle})^{\langle M-N\rangle}$ cuando $M\ge N$.

**Solución.** Como $M-N\in\mathbb N$, la reindexación de la derecha está definida. Para cada $k\in\mathbb N$, su término es $(a^{\langle N\rangle})_{M-N+k}=a_{N+(M-N+k)}=a_{M+k}=a^{\langle M\rangle}_k$. Ambas funciones tienen dominio $\mathbb N$, codominio $\mathbb R$ y valores iguales en cada índice, luego son iguales.

### Microcontrol 032

[]{#MA-MIC-ANM-01-005-032}

[]{#MA-MSOL-ANM-01-005-032}

8. Explica qué sucede cuando $N=0$: ¿cuál es el prefijo eliminado, qué es la cola restringida y qué es la cola reindexada?

**Solución.** El prefijo eliminado es vacío. Como $\mathbb N_{\ge0}=\mathbb N$, la cola restringida es $a$ misma. También $a^{\langle0\rangle}_k=a_{0+k}=a_k$ para todo $k\in\mathbb N$, así que la cola reindexada es $a$. No cambia ningún índice ni término.

## §5.5 — «A partir de cierto momento»: propiedades eventuales

### Microcontrol 033

[]{#MA-MIC-ANM-01-005-033}

[]{#MA-MSOL-ANM-01-005-033}

[]{#MA-SEC-ANM-01-005-005}

1. Sea $a_n=3n-10$. Encuentra un testigo $N$ de que $a_n>0$ eventualmente y verifica tu elección para todo $n\ge N$.

**Solución.** Elegimos $N=4$. Para cualquier $n\ge4$, $3n-10\ge12-10=2>0$, así que $a_n>0$ en toda la cola desde $4$. El índice $3$ aún da $a_3=-1$, por lo que la propiedad no vale desde $3$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-005-034}

[]{#MA-MSOL-ANM-01-005-034}

2. Explica por qué, si $N$ es un testigo de eventualidad, todo $M\ge N$ también lo es.

**Solución.** Si $\forall n\ge N:P(n)$ y $M\ge N$, cualquier índice $n\ge M$ satisface también $n\ge N$. Por tanto, $P(n)$ vale para todos los índices desde $M$, que también es un testigo.

### Microcontrol 035

[]{#MA-MIC-ANM-01-005-035}

[]{#MA-MSOL-ANM-01-005-035}

3. Construye una propiedad de una sucesión que sea eventual pero no verdadera para todos los índices.

**Solución.** Definamos $a_0=-1$ y $a_n=1$ para $n\ge1$. La propiedad $P(n):a_n>0$ vale para todos los índices desde $N=1$, pero falla en $n=0$. Es eventual y no global.

### Microcontrol 036

[]{#MA-MIC-ANM-01-005-036}

[]{#MA-MSOL-ANM-01-005-036}

4. Para $b_n=1/(n+1)$, demuestra que $b_n\in(0,1/5)$ eventualmente usando un intervalo fijo y un testigo explícito.

**Solución.** Elegimos $N=5$. Si $n\ge5$, entonces $n+1\ge6$, de modo que $0<1/(n+1)\le1/6<1/5$. Así $b_n\in(0,1/5)$ para toda la cola desde $5$. El extremo estricto importa: $b_4=1/5$ no pertenece al intervalo.

### Microcontrol 037

[]{#MA-MIC-ANM-01-005-037}

[]{#MA-MSOL-ANM-01-005-037}

5. Reescribe $\exists N\,\forall n\ge N:P(n)$ usando la cola reindexada y la variable $k$.

**Solución.** El cambio $n=N+k$ da la formulación equivalente $\exists N\in\mathbb N\,\forall k\in\mathbb N:P(N+k)$. Si $P(n)$ tiene la forma $R(a_n)$ para un predicado fijo $R$, puede escribirse $\exists N\in\mathbb N\,\forall k\in\mathbb N:R(a^{\langle N\rangle}_k)$. En un predicado general se conserva el índice original $N+k$; no se reemplaza sin más por $k$.

### Microcontrol 038

[]{#MA-MIC-ANM-01-005-038}

[]{#MA-MSOL-ANM-01-005-038}

6. Decide si comprobar $P(10),P(11),\ldots,P(1000)$ basta para demostrar que $P(n)$ ocurre eventualmente. Justifica.

**Solución.** No. Esas verificaciones no controlan los índices mayores que $1000$. Por ejemplo, $a_n=1$ para $n\le1000$ y $a_n=-1$ para $n>1000$ satisface $P(n):a_n>0$ en todos los índices comprobados. Pero dado cualquier $N$, el índice $n=N+1001$ cumple $n\ge N$ y $a_n=-1$, así que ninguna cola satisface $P$ por completo.

### Microcontrol 039

[]{#MA-MIC-ANM-01-005-039}

[]{#MA-MSOL-ANM-01-005-039}

7. Si una propiedad vale para todo $n\in\mathbb N$, ¿qué testigo de eventualidad puede elegirse inmediatamente?

**Solución.** Puede elegirse $N=0$. La cola desde $0$ contiene todo el dominio natural, y la hipótesis garantiza $P(n)$ en cada uno de sus índices.

### Microcontrol 040

[]{#MA-MIC-ANM-01-005-040}

[]{#MA-MSOL-ANM-01-005-040}

8. En la afirmación «eventualmente $a_n\in I$», explica qué objeto debe estar fijado antes de elegir $N$ y qué variable continúa recorriendo la cola.

**Solución.** El conjunto $I\subseteq\mathbb R$ debe estar fijado antes de buscar el umbral $N\in\mathbb N$. Después, $n$ recorre todos los índices naturales con $n\ge N$ y se exige que cada término $a_n$ pertenezca al mismo $I$. El umbral puede depender de $I$; $I$ no cambia al recorrer la cola.

## §5.6 — Eventualmente no significa infinitas veces

### Microcontrol 041

[]{#MA-MIC-ANM-01-005-041}

[]{#MA-MSOL-ANM-01-005-041}

[]{#MA-SEC-ANM-01-005-006}

1. Para $a_n=(-1)^n$ y $P(n):a_n=1$, demuestra desde la definición que $P$ ocurre infinitas veces y que no ocurre eventualmente.

**Solución.** Dado cualquier corte $N\in\mathbb N$, el índice par $n=2N$ cumple $n\ge N$ y $a_n=1$. Por tanto, $P$ ocurre infinitas veces. Para el mismo corte, el índice impar $m=2N+1$ cumple $m\ge N$ y $a_m=-1$, por lo que $P(m)$ falla. Ningún corte elimina todas las excepciones y $P$ no ocurre eventualmente.

### Microcontrol 042

[]{#MA-MIC-ANM-01-005-042}

[]{#MA-MSOL-ANM-01-005-042}

2. Escribe con palabras la afirmación $\forall N\in\mathbb N\,\exists n\ge N:P(n)$ sin usar la expresión «infinitas veces».

**Solución.** Para cada índice de corte $N$, se puede encontrar al menos un índice $n$ igual o posterior a ese corte en el que $P(n)$ es verdadera. El índice encontrado puede depender del corte elegido.

### Microcontrol 043

[]{#MA-MIC-ANM-01-005-043}

[]{#MA-MSOL-ANM-01-005-043}

3. Demuestra directamente que si $P$ ocurre eventualmente, entonces ocurre infinitas veces, sin usar todavía el lema de sincronización de §5.7.

**Solución.** Sea $N_0$ un testigo de eventualidad. Dado cualquier corte $M$, tomemos $n=M+N_0$. Como los dos sumandos son naturales no negativos, $n\ge M$ y $n\ge N_0$. La segunda desigualdad garantiza $P(n)$; la primera muestra una ocurrencia posterior al corte arbitrario. Esto prueba $\forall M\,\exists n\ge M:P(n)$ sin usar el lema de sincronización.

### Microcontrol 044

[]{#MA-MIC-ANM-01-005-044}

[]{#MA-MSOL-ANM-01-005-044}

4. Niega paso a paso la afirmación $\exists N\,\forall n\ge N:P(n)$ y explica por qué el resultado significa que $\neg P$ ocurre infinitas veces.

**Solución.** Negar la existencia de un testigo da $\forall N\in\mathbb N\,\neg(\forall n\in\mathbb N,\ n\ge N\Rightarrow P(n))$. Negar el universal interior produce $\forall N\in\mathbb N\,\exists n\in\mathbb N:\neg(n\ge N\Rightarrow P(n))$. La negación de la implicación es $n\ge N\land\neg P(n)$. Por tanto, la fórmula final es $\forall N\,\exists n\ge N:\neg P(n)$: después de cada corte aparece un fallo de $P$.

### Microcontrol 045

[]{#MA-MIC-ANM-01-005-045}

[]{#MA-MSOL-ANM-01-005-045}

5. Construye una propiedad $P$ tal que tanto $P$ como $\neg P$ ocurran infinitas veces.

**Solución.** Tomemos $a_n=(-1)^n$ y $P(n):a_n=1$. Para cualquier $N$, $2N\ge N$ es una ocurrencia de $P$, y $2N+1\ge N$ es una ocurrencia de $\neg P$. Ambas propiedades tienen ocurrencias posteriores a cualquier corte.

### Microcontrol 046

[]{#MA-MIC-ANM-01-005-046}

[]{#MA-MSOL-ANM-01-005-046}

6. Decide si «$P$ ocurre en cien mil índices distintos» basta para concluir que $P$ ocurre infinitas veces en el sentido de esta sección. Justifica.

**Solución.** No. Una cantidad finita de ocurrencias, por grande que sea, no garantiza una ocurrencia después de cada corte. Por ejemplo, $P(n):n<100000$ vale en cien mil índices distintos, $0,\ldots,99999$, pero no vale en ningún índice $n\ge100000$.

### Microcontrol 047

[]{#MA-MIC-ANM-01-005-047}

[]{#MA-MSOL-ANM-01-005-047}

7. Para $P(n):n$ es un cuadrado perfecto, demuestra que $P$ ocurre infinitas veces pero no eventualmente.

**Solución.** Dado $N\in\mathbb N$, el número $n=N^2$ es un cuadrado y satisface $n\ge N$: para $N=0$ es inmediato, y para $N\ge1$ se tiene $N^2\ge N$. Así $P$ ocurre infinitas veces. Para demostrar que no es eventual, tomemos $k=N+1$ y $m=k^2+1\ge N$. Como $k\ge1$, $k^2<m<(k+1)^2$, pues $1<2k+1$. No hay ningún cuadrado de un natural entre esos dos cuadrados consecutivos. Luego $m$ no es cuadrado y hay un fallo después de cada corte.

### Microcontrol 048

[]{#MA-MIC-ANM-01-005-048}

[]{#MA-MSOL-ANM-01-005-048}

8. Completa y justifica las equivalencias: «$P$ no ocurre infinitas veces» $\iff$ ______ ocurre eventualmente; «$P$ no ocurre eventualmente» $\iff$ ______ ocurre infinitas veces.

**Solución.** En ambos espacios corresponde $\neg P$. Negar $\forall N\,\exists n\ge N:P(n)$ da $\exists N\,\forall n\ge N:\neg P(n)$, es decir, $\neg P$ eventualmente. Negar $\exists N\,\forall n\ge N:P(n)$ da $\forall N\,\exists n\ge N:\neg P(n)$, es decir, $\neg P$ ocurre infinitas veces.

## §5.7 — Sincronizar colas y olvidar perturbaciones finitas

### Microcontrol 049

[]{#MA-MIC-ANM-01-005-049}

[]{#MA-MSOL-ANM-01-005-049}

[]{#MA-SEC-ANM-01-005-007}

1. Supón que $P(n)$ vale para todo $n\ge5$ y $Q(n)$ para todo $n\ge9$. Encuentra un testigo común y demuestra que $P(n)\land Q(n)$ vale desde ese índice.

**Solución.** Elegimos $N=9=\max\{5,9\}$. Si $n\ge9$, entonces $n\ge5$ y $n\ge9$, de modo que ambas hipótesis se aplican y $P(n)\land Q(n)$ es verdadera.

### Microcontrol 050

[]{#MA-MIC-ANM-01-005-050}

[]{#MA-MSOL-ANM-01-005-050}

2. Sean $P_1,P_2,P_3$ propiedades eventuales con testigos $4$, $11$ y $7$. ¿Qué umbral común produce el lema de sincronización? Justifica por qué funciona.

**Solución.** El umbral común es $N=\max\{4,11,7\}=11$. Cualquier $n\ge11$ supera o iguala los tres testigos, por lo que satisface simultáneamente $P_1(n)$, $P_2(n)$ y $P_3(n)$.

### Microcontrol 051

[]{#MA-MIC-ANM-01-005-051}

[]{#MA-MSOL-ANM-01-005-051}

3. Explica por qué el máximo de los umbrales no necesita ser el menor testigo posible para la conjunción.

**Solución.** Los testigos dados sólo garantizan validez desde sus respectivos cortes; no afirman que los cortes sean mínimos. Por ejemplo, si $P$ y $Q$ son verdaderas en todos los índices, $5$ y $9$ son testigos válidos, pero su conjunción tiene el testigo menor $0$. El máximo de los testigos suministrados garantiza un corte común sin pretender optimizarlo.

### Microcontrol 052

[]{#MA-MIC-ANM-01-005-052}

[]{#MA-MSOL-ANM-01-005-052}

4. Sean $a=(3,4,5,6,7,\ldots)$ y $b=(-100,4,5,6,7,\ldots)$. Determina desde qué índice coinciden eventualmente y explica por qué no son iguales como funciones.

**Solución.** Coinciden desde el índice $1$: para todo $n\ge1$, $a_n=b_n=n+3$. No son iguales como funciones $\mathbb N\to\mathbb R$, porque en $n=0$ se tiene $a_0=3$ y $b_0=-100$. El menor testigo de coincidencia es $1$.

### Microcontrol 053

[]{#MA-MIC-ANM-01-005-053}

[]{#MA-MSOL-ANM-01-005-053}

5. Demuestra que si $a$ y $b$ coinciden eventualmente y $a_n>0$ eventualmente, entonces $b_n>0$ eventualmente. Haz visible el umbral común que utilizas.

**Solución.** Sean $N_E$ un testigo de $a_n=b_n$ y $N_P$ un testigo de $a_n>0$. Tomemos $M=\max\{N_E,N_P\}$. Para cada $n\ge M$ se cumplen las dos condiciones, así que $b_n=a_n>0$. Por tanto, $M$ es un testigo de la positividad eventual de $b$.

### Microcontrol 054

[]{#MA-MIC-ANM-01-005-054}

[]{#MA-MSOL-ANM-01-005-054}

6. Da un contraejemplo a la frase «toda propiedad de una sucesión es invariante al modificar finitos términos» y explica qué parte de la formulación correcta falta en esa frase.

**Solución.** La sucesión constante $a_n=0$ satisface $a_0=0$. Si cambiamos sólo el primer término, definiendo $b_0=1$ y $b_n=0$ para $n\ge1$, la propiedad $b_0=0$ es falsa. La invariancia correcta se restringe a propiedades que dependen exclusivamente de una cola suficientemente tardía; la afirmación sobre el índice $0$ no cumple esa condición.

### Microcontrol 055

[]{#MA-MIC-ANM-01-005-055}

[]{#MA-MSOL-ANM-01-005-055}

7. Dos sucesiones difieren sólo en los índices $2$, $8$ y $13$. Encuentra un índice a partir del cual necesariamente coinciden y explica qué tipo de propiedades pueden transferirse desde allí.

**Solución.** Desde $N=14$ coinciden necesariamente, porque todos los índices modificados son menores que $14$. Se pueden transferir propiedades que dependen exclusivamente de una cola común suficientemente tardía. En particular, si un predicado fijo $R(a_n)$ tiene testigo $N_R$, entonces $R(b_n)$ vale desde $\max\{14,N_R\}$. No se transfieren por esta razón propiedades que miren los índices modificados.

### Microcontrol 056

[]{#MA-MIC-ANM-01-005-056}

[]{#MA-MSOL-ANM-01-005-056}

8. Sin desarrollar todavía §5.8, explica por qué disponer de un único umbral común será útil cuando una misma cola deba satisfacer simultáneamente dos condiciones de pertenencia.

**Solución.** Si una condición de pertenencia tiene testigo $N_1$ y otra tiene testigo $N_2$, el corte común $\max\{N_1,N_2\}$ permite usar ambas en cada mismo índice posterior. Así se trabaja con una única cola sobre la que las dos obligaciones están disponibles simultáneamente, sin confundir términos de índices distintos.

## §5.8 — Captura eventual: la puerta a ε–N

### Microcontrol 057

[]{#MA-MIC-ANM-01-005-057}

[]{#MA-MSOL-ANM-01-005-057}

[]{#MA-SEC-ANM-01-005-008}

1. Sea $a=(5,-2,1,1,1,\ldots)$ y $U=\{1\}$. Encuentra un testigo explícito de que $a$ está eventualmente en $U$.

**Solución.** El testigo es $N=2$. Para todo $n\ge2$ se tiene $a_n=1\in U=\{1\}$. Los valores iniciales $5$ y $-2$ no pertenecen a $U$, pero quedan fuera de esa cola.

### Microcontrol 058

[]{#MA-MIC-ANM-01-005-058}

[]{#MA-MSOL-ANM-01-005-058}

2. Reescribe «$a$ está eventualmente en $U$» usando el conjunto de valores tardíos $\{a_n:n\ge N\}$.

**Solución.** La formulación es $\exists N\in\mathbb N:\{a_n:n\in\mathbb N,\ n\ge N\}\subseteq U$. La inclusión significa que cada valor de la cola pertenece al mismo conjunto fijo $U$, y equivale a $\forall n\ge N:a_n\in U$ para ese testigo.

### Microcontrol 059

[]{#MA-MIC-ANM-01-005-059}

[]{#MA-MSOL-ANM-01-005-059}

3. Da un ejemplo de un conjunto fijo $U$ que no sea un intervalo y de una sucesión que esté eventualmente en él.

**Solución.** Tomemos $U=\{0,2\}$ y $a_0=5$, $a_n=0$ si $n\ge1$ es par, $a_n=2$ si $n$ es impar. Desde $N=1$, todos los términos pertenecen a $U$. El conjunto no es un intervalo: contiene $0$ y $2$, pero no contiene el número intermedio $1$.

### Microcontrol 060

[]{#MA-MIC-ANM-01-005-060}

[]{#MA-MSOL-ANM-01-005-060}

4. Explica por qué permitir $U_n=\{a_n\}$ para cada índice destruiría el contenido de la noción de captura eventual.

**Solución.** La elección $U_n=\{a_n\}$ asegura automáticamente $a_n\in U_n$ para cada índice de cualquier sucesión. La región se adapta al término en vez de imponerle una condición previamente fijada. Así no se exige que una cola permanezca en un mismo conjunto $U$ elegido antes del umbral.

### Microcontrol 061

[]{#MA-MIC-ANM-01-005-061}

[]{#MA-MSOL-ANM-01-005-061}

5. Supón que $a$ está eventualmente en $U$ desde $N_U=4$ y eventualmente en $V$ desde $N_V=9$. Demuestra que está eventualmente en $U\cap V$ e identifica un testigo.

**Solución.** Por el lema de sincronización, elegimos $N=\max\{4,9\}=9$. Si $n\ge9$, entonces $n\ge4$ y $n\ge9$, por lo que $a_n\in U$ y $a_n\in V$. Por definición de intersección, $a_n\in U\cap V$ en toda esa cola.

### Microcontrol 062

[]{#MA-MIC-ANM-01-005-062}

[]{#MA-MSOL-ANM-01-005-062}

6. Si $U\cap V=\varnothing$, explica por qué una sucesión no puede estar eventualmente en ambos conjuntos.

**Solución.** Si hubiera testigos $N_U$ y $N_V$, el máximo $N=\max\{N_U,N_V\}$ garantizaría $a_n\in U\cap V$ para todo $n\ge N$. En particular, $a_N$ tendría que pertenecer al conjunto vacío, lo cual es imposible. El índice $N$ existe y pertenece a la cola, así que la obligación no es vacía.

### Microcontrol 063

[]{#MA-MIC-ANM-01-005-063}

[]{#MA-MSOL-ANM-01-005-063}

7. Fija $L\in\mathbb R$ y $r>0$. Explica por qué «eventualmente $a_n\in B(L,r)$» sigue siendo sólo una captura por un conjunto fijo y no constituye todavía la definición de convergencia.

**Solución.** Al fijar $L$ y $r>0$, queda fijado el conjunto $B(L,r)=(L-r,L+r)$. La afirmación controla una sola región. Por ejemplo, la sucesión constante $a_n=L+r/2$ pertenece a esa bola en todos los índices, pero no pertenece a la bola más pequeña $B(L,r/4)$ en ningún índice. Por tanto, una captura en la primera bola no garantiza las exigencias de tolerancia más pequeñas necesarias para hablar de convergencia hacia $L$.

### Microcontrol 064

[]{#MA-MIC-ANM-01-005-064}

[]{#MA-MSOL-ANM-01-005-064}

8. Describe con palabras el cambio de arquitectura entre C05 y C06 usando el esquema «tolerancia → umbral → todos los índices posteriores», sin escribir aún la definición formal de convergencia.

**Solución.** En C05 se fija una región y se busca un umbral desde el que todos los términos permanecen en ella. En C06 la tolerancia podrá exigirse tan pequeña como se quiera: primero se elegirá esa tolerancia, después un umbral que responda a ella y, finalmente, se controlarán todos los índices posteriores. El umbral podrá cambiar con la tolerancia; una única región fija deja de ser suficiente.

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 5](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.md) · [Ejercicios](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-microcontroles.md)
