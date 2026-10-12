---
content-id: MA-BCH-0253
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-012-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 12
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C12_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 12](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html) · [Ejercicios](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §12.1 — Una función tiene un tipo

### Microcontrol 001

[]{#MA-MIC-ANM-01-012-001}

[]{#MA-MSOL-ANM-01-012-001}

[]{#MA-SEC-ANM-01-012-001}

**Pregunta.** ¿Basta la fórmula $x^2$ para determinar una función?

**Solución.** No. Deben declararse dominio, codominio y asignación. La fórmula puede definir funciones distintas al cambiar esos conjuntos.

La asignación indica cómo calcular una salida a partir de una entrada permitida, pero no decide cuáles entradas están permitidas ni qué conjunto de salidas se declara. Por ejemplo, el cuadrado sobre todos los reales admite entradas negativas, mientras su restricción a los no negativos no las admite. Además, declarar codominio real o no negativo cambia el tipo bajo la convención del capítulo. Antes de evaluar o componer hay que conocer los tres datos: dominio, codominio y regla.

### Microcontrol 002

[]{#MA-MIC-ANM-01-012-002}

[]{#MA-MSOL-ANM-01-012-002}

**Pregunta.** ¿Qué diferencia hay entre $f$ y $f(2)$ si $f(x)=x^2$?

**Solución.** $f$ es la función; si $2$ pertenece al dominio, $f(2)=4$ es un elemento del codominio.

La función $f$ contiene una asignación completa para todas las entradas de su dominio. La expresión $f(2)$ aplica esa asignación a una entrada concreta y produce el número cuatro. No podemos sustituir $f$ por cuatro en una composición ni tratar $f(2)$ como una regla que acepta nuevas entradas. La evaluación requiere comprobar primero $2\in D$; la fórmula aislada no autoriza una entrada que el dominio excluya.

### Microcontrol 003

[]{#MA-MIC-ANM-01-012-003}

[]{#MA-MSOL-ANM-01-012-003}

**Pregunta.** ¿Incumple la definición de función que $f(-2)=f(2)$?

**Solución.** No. Entradas distintas pueden compartir salida. Se exige una única salida para cada entrada.

En una función la unicidad se refiere a la salida de una entrada fijada. Para $x=2$ hay una única salida, cuatro; para $x=-2$ también hay una única salida, cuatro. No se ha asignado más de un resultado a ninguna entrada. La propiedad que prohíbe compartir salidas es la inyectividad, que no forma parte de la definición de función. Confundirlas excluiría indebidamente funciones tan habituales como el cuadrado.

### Microcontrol 004

[]{#MA-MIC-ANM-01-012-004}

[]{#MA-MSOL-ANM-01-012-004}

**Pregunta.** ¿Qué conjunto contiene al grafo de $f:D\to E$?

**Solución.** $D\times E$, pues cada par del grafo tiene entrada en $D$ y salida en $E$.

Cada evaluación produce un par ordenado $(x,f(x))$ con $x\in D$ y $f(x)\in E$. Por definición del producto cartesiano, ese par pertenece a $D\times E$. El grafo selecciona exactamente un par para cada entrada, no todos los pares del producto. En general $G_f$ es sólo un subconjunto: si existen varias salidas posibles en $E$, la asignación elige una para cada $x$.

### Microcontrol 005

[]{#MA-MIC-ANM-01-012-005}

[]{#MA-MSOL-ANM-01-012-005}

**Pregunta.** ¿Son iguales dos funciones con el mismo grafo y codominios distintos bajo nuestra convención?

**Solución.** No. El codominio forma parte del objeto tipado, aunque coincidan todos los pares.

El grafo registra las salidas alcanzadas, pero no todas las salidas declaradas como posibles en el codominio. Las dos aplicaciones del cuadrado $\mathbb R\to\mathbb R$ y $\mathbb R\to[0,\infty)$ tienen los mismos pares $(x,x^2)$. La primera deja sin alcanzar los números negativos de su codominio; la segunda alcanza cada elemento del suyo. Bajo nuestra convención, conservar el codominio como parte del objeto permite distinguir estas propiedades sin cambiar la asignación.

### Microcontrol 006

[]{#MA-MIC-ANM-01-012-006}

[]{#MA-MSOL-ANM-01-012-006}

**Pregunta.** ¿Tres evaluaciones iguales prueban igualdad de funciones en $\mathbb R$?

**Solución.** No. Se necesita el mismo tipo e igualdad de valores para toda entrada del dominio; tres entradas no cubren $\mathbb R$.

Si las entradas observadas son $r_1,r_2,r_3$, comparemos $f(x)=0$ con $g(x)=(x-r_1)(x-r_2)(x-r_3)$, ambas de $\mathbb R$ a $\mathbb R$. En las tres entradas coinciden, porque uno de los factores se anula. En una entrada distinta de las tres, el producto no es cero y las funciones difieren. Una muestra prueba igualdades puntuales; la igualdad de funciones exige un argumento válido para toda entrada del dominio.

### Microcontrol 007

[]{#MA-MIC-ANM-01-012-007}

[]{#MA-MSOL-ANM-01-012-007}

**Pregunta.** ¿Puede evaluarse en cero $h:\mathbb R\setminus\{0\}\to\mathbb R$, $h(x)=1/x$?

**Solución.** No: cero no pertenece al dominio, por lo que $h(0)$ no es una evaluación definida.

Para evaluar una función no basta con escribir su fórmula: la entrada debe estar en el conjunto que se declaró como dominio. Aquí cero está excluido y, además, el cociente $1/0$ no es un número real. Asignar por convenio algún valor en cero produciría una extensión diferente, con nuevo dominio y nueva regla en esa entrada. No sería una evaluación de la función $h$ que ya se había definido.

### Microcontrol 008

[]{#MA-MIC-ANM-01-012-008}

[]{#MA-MSOL-ANM-01-012-008}

**Pregunta.** ¿Incluye el grafo de $a_n=n^2$ el punto $(1/2,1/4)$?

**Solución.** No. $a:\mathbb N\to\mathbb R$ sólo admite índices naturales, con $\mathbb N=\{0,1,2,\ldots\}$; $1/2$ no es un índice.

Una sucesión es una función cuyo dominio son los naturales. Su grafo contiene $(0,0),(1,1),(2,4),\ldots$, pero ningún par cuya primera coordenada sea $1/2$. La función real del cuadrado sí contiene $(1/2,1/4)$, porque su dominio admite ese valor. Dibujar una curva entre los puntos discretos puede ayudar a comparar, pero introduce evaluaciones de otra función y no amplía automáticamente el dominio de la sucesión.

## §12.2 — Imagen: transportar un conjunto

### Microcontrol 009

[]{#MA-MIC-ANM-01-012-009}

[]{#MA-MSOL-ANM-01-012-009}

[]{#MA-SEC-ANM-01-012-002}

**Pregunta.** ¿Qué testigo exige $y\in f[A]$?

**Solución.** Una entrada $x\in A$ con $f(x)=y$. Sin pertenencia a $A$, resolver la ecuación no basta.

La definición de imagen se lee como una condición existencial: $y\in f[A]$ equivale a que exista $x\in A$ con $f(x)=y$. Hay que comprobar tanto la ecuación como la pertenencia del testigo. En el cuadrado, la ecuación $x^2=4$ tiene soluciones dos y menos dos, pero si $A=\{-2\}$ sólo menos dos acredita que cuatro pertenece a la imagen. Una raíz fuera de $A$ no satisface la definición.

### Microcontrol 010

[]{#MA-MIC-ANM-01-012-010}

[]{#MA-MSOL-ANM-01-012-010}

**Pregunta.** ¿Son el mismo objeto $f(2)$ y $f[\{2\}]$?

**Solución.** No: el primero es un valor; el segundo es el conjunto unitario $\{f(2)\}$, si $2$ está en el dominio.

Evaluar actúa sobre una entrada y devuelve una salida. Tomar imagen actúa sobre un conjunto de entradas y devuelve un conjunto de salidas. Si $f(x)=x^2$, entonces $f(2)=4$ y $f[\{2\}]=\{4\}$. El número cuatro y el conjunto que lo contiene no son el mismo objeto. Las llaves y los corchetes hacen visible esta diferencia de tipos, que importa al formular inclusiones o pertenencias.

### Microcontrol 011

[]{#MA-MIC-ANM-01-012-011}

[]{#MA-MSOL-ANM-01-012-011}

**Pregunta.** Para $q(x)=x^2$, ¿cuál es $q[\{-2,2\}]$?

**Solución.** $\{4\}$. La imagen es un conjunto y no conserva dos copias del mismo valor.

Comprobamos primero que ambas entradas dan cuatro. Así cualquier elemento de la imagen tiene que ser cuatro. En sentido contrario, cuatro sí pertenece a la imagen porque, por ejemplo, menos dos es un testigo admitido. Se han probado ambas inclusiones para obtener $q[\{-2,2\}]=\{4\}$. Los conjuntos no registran multiplicidades: dos entradas que comparten salida no producen dos elementos distintos en el conjunto imagen.

### Microcontrol 012

[]{#MA-MIC-ANM-01-012-012}

[]{#MA-MSOL-ANM-01-012-012}

**Pregunta.** ¿Cuál es la imagen del conjunto vacío?

**Solución.** $f[\varnothing]=\varnothing$, porque no existe una entrada que pueda ser testigo.

Si hubiera alguna salida $y$ en $f[\varnothing]$, la definición exigiría una entrada $x\in\varnothing$ con $f(x)=y$. No existe tal entrada, de modo que ninguna salida satisface la condición. Por eso la imagen es vacía, independientemente de la regla de la función. No hay que evaluar en «el vacío»: tomar imagen del vacío significa buscar testigos entre sus elementos, y no hay ninguno.

### Microcontrol 013

[]{#MA-MIC-ANM-01-012-013}

[]{#MA-MSOL-ANM-01-012-013}

**Pregunta.** ¿Implica $A\subseteq C$ que $f[A]\subseteq f[C]$?

**Solución.** Sí, si ambos son subconjuntos del dominio. Todo testigo en $A$ también pertenece a $C$.

Tomemos un elemento arbitrario $y\in f[A]$. Existe un testigo $x\in A$ con $f(x)=y$. La inclusión $A\subseteq C$ permite usar exactamente la misma entrada como elemento de $C$, así que $y\in f[C]$. El argumento no requiere inyectividad, sobreyectividad ni orden en las entradas. Es una propiedad del transporte de conjuntos: aumentar el conjunto de entradas no elimina ninguna salida que ya se alcanzaba.

### Microcontrol 014

[]{#MA-MIC-ANM-01-012-014}

[]{#MA-MSOL-ANM-01-012-014}

**Pregunta.** ¿Tiene que coincidir $f[D]$ con el codominio $E$?

**Solución.** No. Sólo $f[D]\subseteq E$ es obligatorio. La igualdad caracteriza sobreyectividad.

La definición exige que cada salida esté en $E$, pero permite elementos de $E$ sin ninguna entrada que los alcance. Por ejemplo, para $q:\mathbb R\to\mathbb R$, los negativos pertenecen al codominio pero no a la imagen, que es $[0,\infty)$. La igualdad $f[D]=E$ añade la exigencia de alcanzar cada elemento declarado y se llama sobreyectividad. No puede deducirse simplemente de que la función esté bien definida.

### Microcontrol 015

[]{#MA-MIC-ANM-01-012-015}

[]{#MA-MSOL-ANM-01-012-015}

**Pregunta.** ¿Qué entrada de $[-2,1]$ alcanza $4$ bajo el cuadrado?

**Solución.** $-2$, pues $(-2)^2=4$ y $-2\in[-2,1]$. La otra raíz, $2$, no es un testigo en ese intervalo.

Resolver $x^2=4$ entrega las candidatas $x=-2$ y $x=2$. El intervalo incluye menos dos, porque es su extremo izquierdo cerrado, pero no incluye dos, que supera el extremo derecho uno. Sólo la primera candidata sirve para este conjunto de entradas. Comprobar los límites del dominio es parte del cálculo de la imagen; las soluciones algebraicas de la ecuación por sí solas no identifican los testigos admitidos.

### Microcontrol 016

[]{#MA-MIC-ANM-01-012-016}

[]{#MA-MSOL-ANM-01-012-016}

**Pregunta.** ¿Cuál es $q[(-2,2)]$ para $q(x)=x^2$?

**Solución.** $[0,4)$: todo cuadrado de esas entradas está allí y, para $0\le y<4$, $x=\sqrt y\in(-2,2)$ alcanza $y$.

Hay dos direcciones. Si $-2<x<2$, entonces $0\le x^2<4$, por lo que la imagen queda contenida en $[0,4)$. A la inversa, para cada $y$ con $0\le y<4$, la raíz no negativa existe y satisface $0\le\sqrt y<2$; es una entrada permitida con cuadrado $y$. Cero se alcanza en cero y cuatro sólo se alcanzaría en las entradas excluidas dos y menos dos. Esto explica los extremos abierto y cerrado de la respuesta.

## §12.3 — Preimagen: seleccionar por la salida

### Microcontrol 017

[]{#MA-MIC-ANM-01-012-017}

[]{#MA-MSOL-ANM-01-012-017}

[]{#MA-SEC-ANM-01-012-003}

**Pregunta.** ¿En qué conjunto vive $f^{-1}[B]$ si $f:D\to E$?

**Solución.** En $D$: por definición es el conjunto de entradas del dominio cuya salida pertenece a $B\subseteq E$.

La preimagen no transporta salidas hacia nuevas salidas: selecciona entradas que cumplen una condición. Su definición es $f^{-1}[B]=\{x\in D:f(x)\in B\}$. Cada elemento que devuelve está, por construcción, en $D$. El conjunto $B$ vive en el codominio, mientras su preimagen vive en el dominio. Mantener separados esos universos evita comparar objetos de tipos diferentes o tomar complementos en el conjunto equivocado.

### Microcontrol 018

[]{#MA-MIC-ANM-01-012-018}

[]{#MA-MSOL-ANM-01-012-018}

**Pregunta.** ¿Se necesita que $f$ tenga función inversa para tomar preimágenes?

**Solución.** No. La preimagen comprueba $f(x)\in B$ para $x\in D$; existe para cualquier función.

Para decidir si una entrada pertenece a la preimagen, sólo la evaluamos y comprobamos si su salida está en $B$. Ese procedimiento tiene sentido aunque varias entradas compartan salida o algunas salidas no se alcancen. La notación $f^{-1}[B]$ designa una operación sobre conjuntos; no afirma que exista una función inversa que devuelva una entrada única para cada salida. El cuadrado real permite preimágenes aunque no sea inyectivo.

### Microcontrol 019

[]{#MA-MIC-ANM-01-012-019}

[]{#MA-MSOL-ANM-01-012-019}

**Pregunta.** ¿Cuál es la fibra del cuadrado real sobre $4$?

**Solución.** $\{-2,2\}$: ambas entradas y sólo ellas satisfacen $x^2=4$.

La fibra sobre cuatro es la preimagen del conjunto unitario $\{4\}$. Resolver $x^2=4$ equivale a resolver $(x-2)(x+2)=0$, por lo que las únicas candidatas son dos y menos dos. Ambas pertenecen al dominio real y verifican la ecuación. La fibra contiene dos elementos, lo que muestra cómo una preimagen puede recuperar varias entradas de una sola salida sin que haya una inversa como función.

### Microcontrol 020

[]{#MA-MIC-ANM-01-012-020}

[]{#MA-MSOL-ANM-01-012-020}

**Pregunta.** ¿Cuál es la fibra del cuadrado real sobre $-1$?

**Solución.** $\varnothing$, porque un cuadrado real es no negativo.

Todo cuadrado real cumple $x^2\ge0$, por lo que ningún $x\in\mathbb R$ puede satisfacer $x^2=-1$. La condición que define la fibra no tiene testigos y su conjunto es vacío. La función sigue siendo válida hacia codominio real: no se exige que todos sus elementos sean alcanzados. Una fibra vacía identifica precisamente una salida del codominio que no pertenece a la imagen.

### Microcontrol 021

[]{#MA-MIC-ANM-01-012-021}

[]{#MA-MSOL-ANM-01-012-021}

**Pregunta.** ¿Cuál es $f^{-1}[E]$?

**Solución.** $D$, pues toda entrada del dominio tiene salida en el codominio.

Para cualquier $x\in D$, la definición de función garantiza $f(x)\in E$, así que $x\in f^{-1}[E]$. Esto prueba $D\subseteq f^{-1}[E]$. La inclusión contraria está incorporada en la definición de preimagen, que sólo admite entradas de $D$. Juntas dan igualdad. El resultado no necesita sobreyectividad: todas las entradas producen alguna salida permitida, aunque no se utilicen todas las salidas del codominio.

### Microcontrol 022

[]{#MA-MIC-ANM-01-012-022}

[]{#MA-MSOL-ANM-01-012-022}

**Pregunta.** ¿Cuál es $q^{-1}[(1,4]]$ para el cuadrado en $\mathbb R$?

**Solución.** $[-2,-1)\cup(1,2]$, ya que $1<x^2\le4$ equivale a $1<|x|\le2$.

La condición de pertenencia es $1<x^2\le4$. Equivale a pedir que la magnitud de la entrada sea mayor que uno y menor o igual que dos. Las entradas positivas forman $(1,2]$; las negativas forman $[-2,-1)$. Los valores dos y menos dos se incluyen porque su cuadrado cuatro está incluido; uno y menos uno se excluyen porque su cuadrado uno no lo está. El conjunto tiene dos ramas, no un intervalo único.

### Microcontrol 023

[]{#MA-MIC-ANM-01-012-023}

[]{#MA-MSOL-ANM-01-012-023}

**Pregunta.** ¿Cómo cambia esa preimagen si el dominio se restringe a $[0,\infty)$?

**Solución.** Se recorta por el nuevo dominio y queda $(1,2]$. Las entradas negativas dejan de estar disponibles.

La regla sigue siendo el cuadrado, pero la nueva función sólo admite entradas no negativas. Por tanto tomamos la preimagen real anterior y la intersectamos con $[0,\infty)$. Toda la rama negativa desaparece y queda $(1,2]$. No cambia la condición sobre la salida; cambia el conjunto en el que buscamos sus testigos. Restringir una función puede cambiar sus preimágenes aunque sus valores coincidan donde ambas están definidas.

### Microcontrol 024

[]{#MA-MIC-ANM-01-012-024}

[]{#MA-MSOL-ANM-01-012-024}

**Pregunta.** ¿Qué recupera $f[f^{-1}[B]]$?

**Solución.** $B\cap f[D]$. Recupera exactamente las salidas de $B$ que la función realmente alcanza, no las salidas imposibles.

Si $y\in f[f^{-1}[B]]$, existe una entrada cuya salida es $y$ y que cumple $f(x)\in B$. Así $y$ está tanto en $B$ como en la imagen de $D$. A la inversa, si $y\in B\cap f[D]$, un testigo $x\in D$ de $f(x)=y$ pertenece a $f^{-1}[B]$ y permite recuperar $y$ al tomar imagen. Las dos direcciones muestran por qué las salidas de $B$ que nunca se alcanzan quedan fuera del resultado.

## §12.4 — Qué operaciones sobreviven al transporte

### Microcontrol 025

[]{#MA-MIC-ANM-01-012-025}

[]{#MA-MSOL-ANM-01-012-025}

[]{#MA-SEC-ANM-01-012-004}

**Pregunta.** ¿La imagen conserva la unión de dos conjuntos de entradas?

**Solución.** Sí: $f[A\cup C]=f[A]\cup f[C]$. Un testigo en la unión pertenece a uno de los conjuntos, y recíprocamente.

Una salida en la imagen de $A\cup C$ tiene una entrada testigo en esa unión. Esa entrada pertenece a $A$ o a $C$, así que la salida está en una de sus imágenes. En la dirección inversa, un testigo en cualquiera de esos dos conjuntos también pertenece a la unión. Se conserva exactamente la alternativa lógica «o». No importa que alguna salida tenga testigos en ambos conjuntos o que los testigos sean diferentes.

### Microcontrol 026

[]{#MA-MIC-ANM-01-012-026}

[]{#MA-MSOL-ANM-01-012-026}

**Pregunta.** ¿Qué inclusión siempre vale para la imagen de una intersección?

**Solución.** $f[A\cap C]\subseteq f[A]\cap f[C]$, porque un testigo común sirve para ambas imágenes.

Si $y\in f[A\cap C]$, podemos escoger una sola entrada $x$ que está simultáneamente en $A$ y en $C$ y cuya salida es $y$. Ese mismo testigo prueba pertenencia a las dos imágenes. Pero pertenecer a $f[A]\cap f[C]$ sólo garantiza un testigo en cada conjunto, y esos testigos podrían no coincidir. Por eso siempre obtenemos la inclusión indicada y la igualdad requiere una justificación adicional.

### Microcontrol 027

[]{#MA-MIC-ANM-01-012-027}

[]{#MA-MSOL-ANM-01-012-027}

**Pregunta.** Con $q(x)=x^2$, $A=\{-1\}$ y $C=\{1\}$, ¿por qué falla la igualdad anterior?

**Solución.** $A\cap C=\varnothing$ tiene imagen vacía, pero $q[A]\cap q[C]=\{1\}$. La salida común procede de dos entradas distintas.

Los conjuntos de entradas son disjuntos, así que su intersección no ofrece ningún testigo y su imagen es vacía. En cambio, menos uno y uno producen ambos la salida uno. Cada conjunto imagen es $\{1\}$, y su intersección también es $\{1\}$. La salida compartida no proviene de una entrada compartida. Este ejemplo localiza exactamente el paso que falla al intentar invertir la inclusión de la imagen de una intersección.

### Microcontrol 028

[]{#MA-MIC-ANM-01-012-028}

[]{#MA-MSOL-ANM-01-012-028}

**Pregunta.** ¿Qué hipótesis reúne los dos testigos de una salida común?

**Solución.** Inyectividad: de $f(a)=f(c)$ se obtiene $a=c$, que pertenece entonces a ambos conjuntos.

Sea $y$ una salida común a $f[A]$ y $f[C]$. Elegimos $a\in A$ y $c\in C$ con $f(a)=y=f(c)$. Si $f$ es inyectiva, la igualdad de salidas fuerza $a=c$. Esa entrada única pertenece a $A\cap C$ y produce $y$, dando la inclusión que faltaba. La inyectividad convierte dos testigos posiblemente distintos en uno común y permite que la imagen conserve la intersección.

### Microcontrol 029

[]{#MA-MIC-ANM-01-012-029}

[]{#MA-MSOL-ANM-01-012-029}

**Pregunta.** ¿Qué preimagen tiene $B\cap H$?

**Solución.** $f^{-1}[B]\cap f^{-1}[H]$, pues una entrada cumple ambas condiciones exactamente cuando su única salida pertenece a ambos conjuntos.

Para una entrada fija $x\in D$, $x\in f^{-1}[B\cap H]$ equivale a $f(x)\in B$ y $f(x)\in H$. Cada condición equivale a pertenecer a la preimagen correspondiente. Por eso obtenemos exactamente la intersección. A diferencia de la imagen, aquí no se eligen dos entradas distintas: evaluamos la misma entrada en todas las condiciones. Esa diferencia explica que no haga falta una hipótesis de inyectividad.

### Microcontrol 030

[]{#MA-MIC-ANM-01-012-030}

[]{#MA-MSOL-ANM-01-012-030}

**Pregunta.** ¿Cuáles son los universos de los complementos en la ley de preimagen?

**Solución.** $E$ a la izquierda y $D$ a la derecha: $f^{-1}[E\setminus B]=D\setminus f^{-1}[B]$.

Para $x\in D$, su salida está en $E$ y por tanto $f(x)\in E\setminus B$ equivale a $f(x)\notin B$. Esta última condición significa $x\notin f^{-1}[B]$. Como las entradas consideradas están en $D$, el conjunto resultante es $D\setminus f^{-1}[B]$. Escribir un complemento sin indicar el universo puede incluir elementos donde la función ni siquiera se evalúa. Los dos complementos están en universos distintos pero compatibles con el tipo.

### Microcontrol 031

[]{#MA-MIC-ANM-01-012-031}

[]{#MA-MSOL-ANM-01-012-031}

**Pregunta.** ¿Siempre se cumple $A=f^{-1}[f[A]]$?

**Solución.** No. Siempre hay inclusión de $A$ en el lado derecho, pero para el cuadrado y $A=\{1\}$ el lado derecho es $\{-1,1\}$. Inyectividad garantiza igualdad.

Cualquier $a\in A$ satisface $f(a)\in f[A]$, de modo que $a$ pertenece al conjunto recuperado. Sin embargo, también se recuperan otras entradas que compartan alguna salida con $A$. Para el cuadrado, menos uno comparte con uno la salida uno y se añade a la preimagen. Si la función es inyectiva, de $f(x)=f(a)$ se obtiene $x=a\in A$, lo que impide añadir entradas nuevas y prueba la igualdad.

### Microcontrol 032

[]{#MA-MIC-ANM-01-012-032}

[]{#MA-MSOL-ANM-01-012-032}

**Pregunta.** ¿Cuál es la preimagen de $B\setminus H$?

**Solución.** $f^{-1}[B]\setminus f^{-1}[H]$: equivale a exigir $f(x)\in B$ y $f(x)\notin H$ a una entrada $x\in D$.

Fijada una entrada $x\in D$, pertenecer a la preimagen de $B\setminus H$ exige que su salida esté en $B$ y fuera de $H$. La primera condición selecciona $f^{-1}[B]$ y la segunda excluye $f^{-1}[H]$. La diferencia de esos conjuntos describe exactamente la selección. No estamos restando valores de la función; estamos excluyendo entradas según una condición sobre su única salida.

## §12.5 — Componer, restringir y deshacer

### Microcontrol 033

[]{#MA-MIC-ANM-01-012-033}

[]{#MA-MSOL-ANM-01-012-033}

[]{#MA-SEC-ANM-01-012-005}

**Pregunta.** ¿Qué tipo tiene $g\circ f$ si $f:D\to E$ y $g:E\to F$?

**Solución.** $D\to F$, con $(g\circ f)(x)=g(f(x))$; la salida de $f$ es una entrada autorizada de $g$.

El recorrido comienza con $x\in D$. La función $f$ entrega $f(x)\in E$, y ese conjunto es justamente el dominio declarado de $g$. Por eso $g$ puede evaluarse en ese resultado y entrega un elemento de $F$. La composición conserva el dominio inicial y termina en el codominio final. Si los tipos no fueran compatibles, habría que comprobar qué salidas de la primera son entradas admitidas de la segunda antes de declarar una composición en todo $D$.

### Microcontrol 034

[]{#MA-MIC-ANM-01-012-034}

[]{#MA-MSOL-ANM-01-012-034}

**Pregunta.** ¿Cómo se calcula $(g\circ f)[A]$ por etapas?

**Solución.** Como $g[f[A]]$: primero transportamos las entradas por $f$ y después sus salidas por $g$.

Para cada $x\in A$, la salida compuesta es $g(f(x))$. Todas las primeras salidas forman el conjunto $f[A]$; aplicarle $g$ reúne exactamente las segundas salidas. En sentido inverso, cualquier elemento de $g[f[A]]$ tiene un testigo intermedio $y=f(x)$ con $x\in A$, por lo que procede de la composición. Estas dos direcciones justifican la igualdad y mantienen el orden de las etapas de evaluación.

### Microcontrol 035

[]{#MA-MIC-ANM-01-012-035}

[]{#MA-MSOL-ANM-01-012-035}

**Pregunta.** ¿En qué orden se calcula $(g\circ f)^{-1}[C]$?

**Solución.** Primero $g^{-1}[C]$ en $E$, después $f^{-1}[g^{-1}[C]]$ en $D$. Es la condición $g(f(x))\in C$.

Queremos las entradas $x$ cuya salida final $g(f(x))$ esté en $C$. Primero averiguamos qué entradas intermedias $y\in E$ cumplen $g(y)\in C$, es decir, calculamos $g^{-1}[C]$. Después seleccionamos las entradas iniciales cuya salida $f(x)$ está en ese conjunto. El orden de preimágenes va hacia atrás por las etapas de la composición y no supone que ninguna de las dos funciones tenga inversa.

### Microcontrol 036

[]{#MA-MIC-ANM-01-012-036}

[]{#MA-MSOL-ANM-01-012-036}

**Pregunta.** ¿Cuál es el dominio de $f|_A$?

**Solución.** $A\subseteq D$. La restricción mantiene los valores en $A$ y el codominio $E$.

La restricción elimina del dominio las entradas que no pertenecen a $A$, pero conserva la salida original para cada entrada que permanece. Su grafo es $\{(x,f(x)):x\in A\}$ y su tipo es $A\to E$. No redefine los valores ni reduce automáticamente el codominio a las salidas alcanzadas. Una restricción puede mejorar propiedades como inyectividad al eliminar entradas que compartían salida, pero ya constituye un objeto con otro dominio.

### Microcontrol 037

[]{#MA-MIC-ANM-01-012-037}

[]{#MA-MSOL-ANM-01-012-037}

**Pregunta.** ¿Cuál es $(f|_A)^{-1}[B]$?

**Solución.** $A\cap f^{-1}[B]$, porque sólo se admiten las entradas de $A$ cuya salida está en $B$.

Una entrada pertenece a la preimagen bajo la restricción si está en su dominio $A$ y su salida original cumple la condición $f(x)\in B$. Esta segunda condición la sitúa en $f^{-1}[B]$ para la función original. Exigir ambas da la intersección. La fórmula expresa de manera precisa la idea de recortar una preimagen por el nuevo dominio, sin volver a resolver la condición sobre las salidas.

### Microcontrol 038

[]{#MA-MIC-ANM-01-012-038}

[]{#MA-MSOL-ANM-01-012-038}

**Pregunta.** ¿Qué dos propiedades permiten construir una función inversa $E\to D$?

**Solución.** Sobreyectividad, para que cada $y\in E$ tenga entrada, e inyectividad, para que esa entrada sea única; juntas forman biyectividad.

Para construir la inversa, cada salida declarada debe tener al menos una entrada que la produzca y no puede tener más de una. La primera obligación es sobreyectividad; la segunda es inyectividad. Juntas permiten asignar a cada $y\in E$ su única entrada $x\in D$. Si falta la primera, la inversa no está definida en todo $E$; si falta la segunda, habría varias candidatas y no una asignación única. Por eso la inversa de tipo $E\to D$ requiere biyectividad.

### Microcontrol 039

[]{#MA-MIC-ANM-01-012-039}

[]{#MA-MSOL-ANM-01-012-039}

**Pregunta.** ¿Cuál es la inversa de $f:\mathbb R\to\mathbb R$, $f(x)=2x+1$?

**Solución.** $h(y)=(y-1)/2$. Sustituir verifica $h(f(x))=x$ y $f(h(y))=y$ para todos los reales.

Despejamos la ecuación $y=2x+1$: restar uno y dividir por dos da $x=(y-1)/2$. Esta entrada existe para todo $y\in\mathbb R$ y es única. Las dos sustituciones verifican el resultado en ambos sentidos: $((2x+1)-1)/2=x$ y $2((y-1)/2)+1=y$. No basta comprobar una sola evaluación numérica; las identidades deben valer para todas las entradas y salidas del tipo declarado.

### Microcontrol 040

[]{#MA-MIC-ANM-01-012-040}

[]{#MA-MSOL-ANM-01-012-040}

**Pregunta.** ¿Por qué restringir el cuadrado a entradas no negativas no basta para hacerlo biyectivo hacia $\mathbb R$?

**Solución.** Porque ninguna entrada alcanza una salida negativa. Para biyectividad hay que declarar codominio $[0,\infty)$ además de restringir el dominio.

En el dominio no negativo, el cuadrado ya no identifica entradas opuestas y resulta inyectivo. Sin embargo, si mantenemos el codominio real, la salida menos uno sigue sin tener entrada. Por eso falta sobreyectividad. Al declarar codominio $[0,\infty)$, cada salida tiene la única entrada no negativa $\sqrt y$. La restricción del dominio resuelve la unicidad; ajustar el codominio resuelve la existencia para cada salida declarada.

## §12.6 — Transportar el orden no rellena los huecos

### Microcontrol 041

[]{#MA-MIC-ANM-01-012-041}

[]{#MA-MSOL-ANM-01-012-041}

[]{#MA-SEC-ANM-01-012-006}

**Pregunta.** ¿Qué significa no decreciente en un dominio $D\subseteq\mathbb R$?

**Solución.** Para todos $x,y\in D$, $x\le y$ implica $f(x)\le f(y)$. El sentido no estricto permite valores iguales.

La definición compara cualquier par de entradas del dominio, incluso si éste tiene huecos. Cuando una entrada no supera otra, su salida tampoco debe superarla. Se permiten salidas iguales: una función constante satisface la condición. La versión estrictamente creciente exige $f(x)<f(y)$ cuando $x<y$ y prohíbe esas coincidencias. Conviene distinguir ambas definiciones porque sólo la estricta garantiza por sí sola inyectividad.

### Microcontrol 042

[]{#MA-MIC-ANM-01-012-042}

[]{#MA-MSOL-ANM-01-012-042}

**Pregunta.** ¿Una función estrictamente creciente es inyectiva?

**Solución.** Sí. Entradas distintas se ordenan por tricotomía y sus salidas quedan estrictamente ordenadas, luego son distintas.

Supongamos que dos entradas distintas compartieran salida. En la recta, una sería menor que la otra. Si $x<y$, el crecimiento estricto daría $f(x)<f(y)$, contradiciendo la igualdad; si $y<x$, intercambiamos los papeles. Por tanto entradas con la misma salida deben ser iguales. La prueba usa el orden lineal del dominio y la desigualdad estricta, no necesita que el dominio sea un intervalo.

### Microcontrol 043

[]{#MA-MIC-ANM-01-012-043}

[]{#MA-MSOL-ANM-01-012-043}

**Pregunta.** ¿Una función no decreciente tiene que ser inyectiva?

**Solución.** No. Una constante en un dominio con dos entradas distintas es no decreciente y les asigna la misma salida.

Tomemos una constante $f(x)=c$ en un dominio que contenga, por ejemplo, cero y uno. Para cualquier par ordenado de entradas, las salidas son iguales y satisfacen la desigualdad no estricta. Sin embargo, $f(0)=f(1)$ con $0\ne1$, así que no es inyectiva. Exigir al menos dos entradas importa: en un dominio de un solo elemento no existe una pareja distinta que pueda refutar inyectividad.

### Microcontrol 044

[]{#MA-MIC-ANM-01-012-044}

[]{#MA-MSOL-ANM-01-012-044}

**Pregunta.** ¿Qué controla el intervalo $[f(a),f(b)]$ si $f$ es no decreciente?

**Solución.** Contiene $f[D\cap[a,b]]$, pues $a\le x\le b$ implica $f(a)\le f(x)\le f(b)$. No promete todas las salidas intermedias.

Suponiendo $a,b\in D$ y $a\le b$, para cualquier $x\in D\cap[a,b]$ aplicamos la monotonía dos veces: $a\le x$ da $f(a)\le f(x)$, y $x\le b$ da $f(x)\le f(b)$. Esto demuestra una inclusión, no una igualdad de imágenes. El intervalo entre las salidas puede contener valores que ninguna entrada alcance, como muestra la función de salto. Acotar salidas entre dos extremos no rellena los huecos de la imagen.

### Microcontrol 045

[]{#MA-MIC-ANM-01-012-045}

[]{#MA-MSOL-ANM-01-012-045}

**Pregunta.** Para la función de salto $s$ del texto, ¿se alcanza $1/2$?

**Solución.** No. Las entradas negativas dan salidas negativas y las no negativas dan salidas al menos $1$.

La función del texto vale $s(x)=x$ para $x<0$ y $s(x)=x+1$ para $x\ge0$. En la primera rama las salidas son negativas; en la segunda son al menos uno. El número $1/2$ no está en ninguna de esas regiones, por lo que su fibra es vacía. La función puede ser estrictamente creciente y aun así omitir salidas intermedias: el orden controla comparaciones, pero no garantiza que la imagen sea un intervalo.

### Microcontrol 046

[]{#MA-MIC-ANM-01-012-046}

[]{#MA-MSOL-ANM-01-012-046}

**Pregunta.** ¿Cuál es $s[[-1,1]]$?

**Solución.** $[-1,0)\cup[1,2]$, transportando cada una de las dos ramas con sus extremos correctos.

Separamos las entradas en $[-1,0)$ y $[0,1]$. La primera rama mantiene su valor y produce $[-1,0)$; el cero está excluido de esa rama. La segunda añade uno y produce $[1,2]$, incluyendo ambas fronteras. La imagen de la unión es la unión de esas imágenes. No debemos añadir el intervalo entre cero y uno: contiene salidas que el salto nunca alcanza.

### Microcontrol 047

[]{#MA-MIC-ANM-01-012-047}

[]{#MA-MSOL-ANM-01-012-047}

**Pregunta.** ¿Qué signo de $m$ hace decreciente estricta a $h(x)=mx+c$?

**Solución.** $m<0$, porque para $x<y$ el producto $m(y-x)$ es negativo, luego $h(y)<h(x)$.

Para dos entradas con $x<y$, la diferencia $h(y)-h(x)=m(y-x)$ elimina la constante $c$. Como $y-x>0$, el signo de esa diferencia es el signo de $m$. Si $m<0$, obtenemos $h(y)<h(x)$, que es decrecimiento estricto. Para $m=0$ las salidas coinciden y sólo hay constancia; para $m>0$ el sentido se invierte y hay crecimiento estricto. La traslación no cambia estas comparaciones.

### Microcontrol 048

[]{#MA-MIC-ANM-01-012-048}

[]{#MA-MSOL-ANM-01-012-048}

**Pregunta.** ¿En qué rama es creciente estricta la función cuadrado?

**Solución.** En $[0,\infty)$: si $0\le x<y$, $y^2-x^2=(y-x)(y+x)>0$. En la rama no positiva es decreciente estricta.

En la rama no negativa, $y-x>0$ y $y+x>0$ para $0\le x<y$, incluso si $x=0$. Su producto demuestra $y^2>x^2$. En la rama no positiva, si $x<y\le0$, el primer factor es positivo y el segundo negativo, por lo que $y^2<x^2$. En todo $\mathbb R$ las dos ramas no tienen el mismo sentido y el cuadrado no es monótono globalmente. El dominio declarado forma parte de la conclusión.

## §12.7 — Distancia y escala: medir la deformación

### Microcontrol 049

[]{#MA-MIC-ANM-01-012-049}

[]{#MA-MSOL-ANM-01-012-049}

[]{#MA-SEC-ANM-01-012-007}

**Pregunta.** ¿Qué factor multiplica las distancias bajo $h(x)=mx+c$?

**Solución.** $|m|$, ya que $|h(x)-h(y)|=|m||x-y|$; $c$ se cancela.

Restar salidas hace desaparecer la traslación: $h(x)-h(y)=m(x-y)$. Tomar magnitudes da un factor $|m|$, aunque $m$ sea negativo y cambie el orden de las entradas. Si $|m|=1$, todas las distancias se conservan; si es mayor que uno, se amplían; si está entre cero y uno, se reducen. Para $m=0$ todas las salidas coinciden y todas las distancias se hacen cero.

### Microcontrol 050

[]{#MA-MIC-ANM-01-012-050}

[]{#MA-MSOL-ANM-01-012-050}

**Pregunta.** ¿Puede una función invertir el orden y conservar todas las distancias?

**Solución.** Sí: $h(x)=-x$ es estrictamente decreciente y $|-x-(-y)|=|x-y|$.

Si $x<y$, entonces $-x>-y$, por lo que la reflexión invierte el orden. En cambio, la resta de salidas es $-x+y=-(x-y)$ y su magnitud coincide con la original. Este ejemplo separa dos preguntas: cómo cambia la comparación ordenada de las entradas y cómo cambia su separación. Conservar distancias no exige conservar el sentido del orden en la recta.

### Microcontrol 051

[]{#MA-MIC-ANM-01-012-051}

[]{#MA-MSOL-ANM-01-012-051}

**Pregunta.** ¿De qué puede depender una cota de expansión $L$?

**Solución.** Puede depender de la función y del dominio declarado, pero debe fijarse antes de elegir el par $x,y$ y servir para todos los pares de ese dominio.

Una cota de expansión se expresa como $\exists L\ge0\;\forall x,y\in D$, $|f(x)-f(y)|\le L|x-y|$. El factor debe fijarse antes de escoger el par y funcionar para todos ellos. Si se permitiera un factor diferente para cada par, podríamos tomar el cociente de sus distancias siempre que las entradas fueran distintas, y no habríamos probado una cota global. Restringir el dominio puede permitir un factor que no exista en un dominio mayor.

### Microcontrol 052

[]{#MA-MIC-ANM-01-012-052}

[]{#MA-MSOL-ANM-01-012-052}

**Pregunta.** ¿Qué cota de expansión tiene $x\mapsto|x|$?

**Solución.** $L=1$, por $\bigl||x|-|y|\bigr|\le|x-y|$, consecuencia de la desigualdad triangular en ambos sentidos.

La triangular da $|x|\le|x-y|+|y|$ y, al intercambiar las entradas, $|y|\le|x-y|+|x|$. Reorganizar ambas encierra $|x|-|y|$ entre $-|x-y|$ y $|x-y|$, lo que prueba la cota. El valor absoluto no aumenta distancias, aunque puede reducirlas a cero para entradas opuestas. El factor uno funciona para todos los pares reales y es óptimo, porque para entradas no negativas distintas se alcanza igualdad.

### Microcontrol 053

[]{#MA-MIC-ANM-01-012-053}

[]{#MA-MSOL-ANM-01-012-053}

**Pregunta.** ¿Qué cota da la factorización del cuadrado en $[-R,R]$ con $R>0$?

**Solución.** $2R$: $|x^2-y^2|=|x-y||x+y|\le2R|x-y|$.

En el intervalo simétrico sabemos $|x|,|y|\le R$. La triangular proporciona $|x+y|\le|x|+|y|\le2R$. Al multiplicar por $|x-y|$ en la factorización obtenemos una cota con el mismo factor $2R$ para cualquier par. No necesitamos derivadas para acreditarla. El tamaño del dominio controla el factor que aparecía libre en la fórmula y transforma una identidad algebraica en una estimación global.

### Microcontrol 054

[]{#MA-MIC-ANM-01-012-054}

[]{#MA-MSOL-ANM-01-012-054}

**Pregunta.** ¿Por qué no sirve una cota finita $L\ge0$ para el cuadrado en toda la recta?

**Solución.** El par $x=L+1$, $y=x+1$ tiene distancia $1$ y distancia de salidas $2L+3>L$, contradiciendo la cota propuesta.

Para refutar una cota propuesta hay que construir un par que dependa de ella. Con $x=L+1$ y $y=L+2$, la distancia de entradas es uno y la de salidas es $(L+2)^2-(L+1)^2=2L+3$. La estimación exigiría $2L+3\le L$, imposible para $L\ge0$. Como la construcción funciona para cualquier factor finito propuesto, ninguna cota global existe. En intervalos acotados, en cambio, el factor variable sí puede controlarse.

### Microcontrol 055

[]{#MA-MIC-ANM-01-012-055}

[]{#MA-MSOL-ANM-01-012-055}

**Pregunta.** ¿Qué garantiza una cota inferior $c|x-y|\le|f(x)-f(y)|$ con $c>0$?

**Solución.** Inyectividad: si las salidas coinciden, la desigualdad obliga a $|x-y|=0$, luego $x=y$.

Si $f(x)=f(y)$, la distancia de salidas es cero. La cota inferior obliga a $c|x-y|\le0$. Ambos factores son no negativos y $c$ es estrictamente positivo, así que $|x-y|=0$ y las entradas coinciden. La positividad estricta de $c$ es esencial: con $c=0$ la desigualdad se vuelve trivial y también la satisfacen funciones constantes que no son inyectivas.

### Microcontrol 056

[]{#MA-MIC-ANM-01-012-056}

[]{#MA-MSOL-ANM-01-012-056}

**Pregunta.** ¿Qué cota tiene una composición de funciones con cotas $L$ y $M$ compatibles?

**Solución.** $ML$, al aplicar primero $|g(f(x))-g(f(y))|\le M|f(x)-f(y)|$ y después la cota $L$.

La primera estimación se aplica a las entradas intermedias $f(x),f(y)$, por lo que éstas deben pertenecer al dominio de $g$. Después reemplazamos su distancia por la cota de $f$, obteniendo $|g(f(x))-g(f(y))|\le M L|x-y|$. Los factores se multiplican porque la segunda etapa actúa sobre una separación ya deformada por la primera. No se suman: son controles sucesivos sobre la misma distancia transportada.

## §12.8 — Representaciones y ventanas de control

### Microcontrol 057

[]{#MA-MIC-ANM-01-012-057}

[]{#MA-MSOL-ANM-01-012-057}

[]{#MA-SEC-ANM-01-012-008}

**Pregunta.** ¿Qué tipo tiene $T(u,v)=(u+v,v)$ en el texto?

**Solución.** $T:\mathbb R^2\to\mathbb R^2$; tanto entrada como salida son pares reales, no valores escalares.

La entrada es el par ordenado $(u,v)$, formado por dos números reales. La salida es otro par, cuyas coordenadas son $u+v$ y $v$. Así $T$ transforma puntos del plano en puntos del plano. No hay que interpretar las dos coordenadas de salida como dos resultados alternativos para una misma entrada: juntas constituyen un único elemento de $\mathbb R^2$. La definición sigue cumpliendo unicidad de salida.

### Microcontrol 058

[]{#MA-MIC-ANM-01-012-058}

[]{#MA-MSOL-ANM-01-012-058}

**Pregunta.** ¿Cuál es la inversa de esa transformación de rejilla?

**Solución.** $S(a,b)=(a-b,b)$, pues $S(T(u,v))=(u,v)$ y $T(S(a,b))=(a,b)$.

De las coordenadas de salida $a=u+v$ y $b=v$, recuperamos primero $v=b$ y después $u=a-b$. La candidata inversa devuelve el par $(a-b,b)$. Componer en ambos sentidos comprueba recuperación de todos los puntos: $(u+v-v,v)=(u,v)$ y $(a-b+b,b)=(a,b)$. Las identidades prueban simultáneamente que no se pierde información y que cada punto de salida tiene una entrada única.

### Microcontrol 059

[]{#MA-MIC-ANM-01-012-059}

[]{#MA-MSOL-ANM-01-012-059}

**Pregunta.** ¿En qué se transforma la recta $u=j$ bajo $T$?

**Solución.** En la recta parametrizada por $(j+v,v)$, que cumple $a-b=j$ en coordenadas de salida $(a,b)$.

En la recta inicial fijamos $u=j$ y dejamos variar libremente $v$. La salida es $(a,b)=(j+v,v)$ y cumple $a-b=j$. Para comprobar que obtenemos toda esa recta de salida, tomamos cualquier $(a,b)$ con $a-b=j$ y escogemos la entrada $(j,b)$. Su imagen es $(j+b,b)=(a,b)$. El argumento prueba las dos inclusiones y no sólo que algunos puntos enviados caen en la recta.

### Microcontrol 060

[]{#MA-MIC-ANM-01-012-060}

[]{#MA-MSOL-ANM-01-012-060}

**Pregunta.** ¿Multiplica $T$ todas las longitudes por un mismo factor?

**Solución.** No: el segmento de $(0,0)$ a $(1,0)$ conserva longitud $1$, mientras que el de $(0,0)$ a $(0,1)$ pasa a longitud $\sqrt2$.

Usamos las longitudes euclidianas del plano. El origen se mantiene fijo. El vector horizontal $(1,0)$ se transforma en $(1,0)$ y conserva longitud uno; el vertical $(0,1)$ se transforma en $(1,1)$ y su longitud es $\sqrt{1^2+1^2}=\sqrt2$. Si existiera un factor común, el primer segmento lo fijaría en uno y el segundo exigiría $\sqrt2=1$. La deformación depende de la dirección del segmento.

### Microcontrol 061

[]{#MA-MIC-ANM-01-012-061}

[]{#MA-MSOL-ANM-01-012-061}

**Pregunta.** ¿Qué inclusión de entradas equivale a $f[A]\subseteq B$?

**Solución.** $A\subseteq f^{-1}[B]$. Ambas dicen que toda entrada de $A$ tiene salida en $B$.

Si $f[A]\subseteq B$, cada $x\in A$ tiene salida en $B$, y por definición pertenece a $f^{-1}[B]$. A la inversa, si $A\subseteq f^{-1}[B]$, cualquier salida de $f[A]$ tiene un testigo $x\in A$ cuya salida está en $B$. Esto demuestra las dos direcciones. La equivalencia permite expresar el mismo control en el espacio de salidas o en el de entradas, sin suponer que la función sea invertible.

### Microcontrol 062

[]{#MA-MIC-ANM-01-012-062}

[]{#MA-MSOL-ANM-01-012-062}

**Pregunta.** ¿Por qué se recorta $B(x_0,r)$ por $D$ al usarla como ventana de entrada?

**Solución.** Porque sólo se puede transportar un subconjunto del dominio. Entradas fuera de $D$ no tienen evaluación por $f$.

Una bola alrededor de $x_0$ puede contener puntos que el dominio excluya. Por ejemplo, para una función definida sólo en $[0,\infty)$, toda bola real centrada en cero incluye puntos negativos. La ventana autorizada es $D\cap B(x_0,r)$: selecciona sólo entradas donde existe evaluación. Transportar la bola entera sin ese recorte intentaría usar valores que la función no define. La operación conserva el dominio en la formulación del control local.

### Microcontrol 063

[]{#MA-MIC-ANM-01-012-063}

[]{#MA-MSOL-ANM-01-012-063}

**Pregunta.** Para el cuadrado, ¿qué cota certifica la ventana de radio $1/4$ alrededor de $1$ hacia radio $1$ alrededor de su salida?

**Solución.** Si $|x-1|<1/4$, entonces $|x+1|<9/4$ y $|x^2-1|<9/16<1$. Así toda la ventana de entrada se transporta dentro de la de salida.

Factorizamos $x^2-1=(x-1)(x+1)$. Si $|x-1|<1/4$, la triangular da $|x+1|=|(x-1)+2|<1/4+2=9/4$. El producto queda por debajo de $(1/4)(9/4)=9/16$, que es menor que uno. Por tanto cada entrada de la ventana cumple $|x^2-1|<1$. La cota controla todos sus puntos y no sólo los extremos o algunas evaluaciones elegidas.

### Microcontrol 064

[]{#MA-MIC-ANM-01-012-064}

[]{#MA-MSOL-ANM-01-012-064}

**Pregunta.** ¿Es vecindad de cero la preimagen $s^{-1}[B(1,1/4)]=[0,1/4)$?

**Solución.** No. Contiene cero pero ninguna bola de radio positivo centrada en cero, ya que toda esa bola contiene entradas negativas.

La rama negativa produce salidas negativas y ninguna cae en $B(1,1/4)=(3/4,5/4)$. En la rama no negativa, $s(x)=x+1$ cae en esa bola exactamente cuando $0\le x<1/4$. Aunque la preimagen contiene cero, para cada $r>0$ el punto $-r/2$ pertenece a $B(0,r)$ y queda fuera de ella. Así ninguna bola real alrededor de cero está contenida en la preimagen. El universo aquí es la recta real; en un dominio restringido a los no negativos la noción relativa sería distinta.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 12](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html) · [Ejercicios](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-12-que-hace-una-funcion-microcontroles.html)
