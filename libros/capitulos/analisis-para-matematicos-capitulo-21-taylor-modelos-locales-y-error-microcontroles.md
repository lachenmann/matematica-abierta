---
content-id: MA-BCH-0289
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-021-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 21
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C21_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §21.1 — Un polinomio para los datos de un centro

### Microcontrol 001

[]{#MA-MIC-ANM-01-021-001}

[]{#MA-MSOL-ANM-01-021-001}

[]{#MA-SEC-ANM-01-021-001}

**Pregunta.** ¿Qué datos conserva el polinomio de Taylor de orden $n$?

**Solución.** El valor y las derivadas de órdenes1 a$n$ en el centro, si están definidos; orden0 significa el propio valor.

El centro y el orden se fijan antes de construir los coeficientes. Conservar esos datos significa igualdad de evaluaciones y derivadas allí, no igualdad de funciones en todo el dominio. El modelo puede tener grado menor que el orden solicitado si algunos coeficientes se anulan.

### Microcontrol 002

[]{#MA-MIC-ANM-01-021-002}

[]{#MA-MSOL-ANM-01-021-002}

**Pregunta.** ¿Cuál es el valor de $0!$ y por qué importa?

**Solución.** Es1. Su copia real positiva permite el coeficiente de orden0 y evita un denominador nulo.

La convención del factorial empieza en uno y multiplica después por naturales positivos. Todas sus copias reales son por ello positivas. En el término inicial se divide el valor central por uno, sin una singularidad artificial.

### Microcontrol 003

[]{#MA-MIC-ANM-01-021-003}

[]{#MA-MSOL-ANM-01-021-003}

**Pregunta.** ¿Qué significa $k!$ cuando aparece en un cociente real?

**Solución.** La copia real del factorial natural mediante la incrustación declarada; no se identifican tácitamente naturales y reales.

El factorial se construye como un natural y el coeficiente pertenece a un cálculo real. La incrustación lleva ese natural positivo al denominador real correspondiente. Declarar esta lectura justifica la división sin confundir los tipos de los objetos.

### Microcontrol 004

[]{#MA-MIC-ANM-01-021-004}

[]{#MA-MSOL-ANM-01-021-004}

**Pregunta.** ¿Qué coeficiente corresponde a la derivada de orden $j$?

**Solución.** $a_j=f^{(j)}(c)/j!$, porque $P^{(j)}(c)=j!a_j$.

Al derivar $j$ veces, los términos de grado menor desaparecen y los mayores conservan una potencia positiva que se anula en el centro. Sólo sobrevive el término de grado $j$ con su factorial. Dividir por ese factor positivo determina el coeficiente de manera única.

### Microcontrol 005

[]{#MA-MIC-ANM-01-021-005}

[]{#MA-MSOL-ANM-01-021-005}

**Pregunta.** ¿El orden $n$ obliga a grado exactamente $n$?

**Solución.** No. El último coeficiente puede ser cero, y el grado sólo está acotado superiormente por$n$.

El orden indica hasta qué datos se desea conservar, mientras el grado depende del último coeficiente no nulo. Un polinomio cuadrático puede coincidir con su Taylor de orden cuatro. No se agrega un término superior ficticio para alcanzar ese grado.

### Microcontrol 006

[]{#MA-MIC-ANM-01-021-006}

[]{#MA-MSOL-ANM-01-021-006}

**Pregunta.** ¿Dónde está definido el polinomio y dónde el resto?

**Solución.** El polinomio está en toda la recta; el resto $f-T_{n,c}f$ sólo en el dominio de$f$.

La fórmula polinómica sólo usa sumas y potencias enteras y admite toda entrada real. Para formar el resto también se necesita evaluar la función original. Por ello evaluar el modelo fuera del dominio no crea una salida de la función ni un error definido allí.

### Microcontrol 007

[]{#MA-MIC-ANM-01-021-007}

[]{#MA-MSOL-ANM-01-021-007}

**Pregunta.** ¿Qué resto tiene $t^3$ a orden2 y centro1?

**Solución.** Con $t=1+h$, el polinomio es $1+3h+3h^2$ y el resto exacto es$h^3$.

La expansión finita de $(1+h)^3$ separa los tres términos conservados y el término cúbico restante. No se estima un testigo desconocido para obtener esa identidad. La magnitud del resto se controla después mediante $|h|^3$, con el dominio y centro fijados.

### Microcontrol 008

[]{#MA-MIC-ANM-01-021-008}

[]{#MA-MSOL-ANM-01-021-008}

**Pregunta.** ¿Los datos centrales hasta orden $n$ determinan una función completa?

**Solución.** No. Añadir $A(t-c)^{n+1}$ conserva todos esos datos y puede cambiar la función fuera del centro.

La potencia añadida tiene un cero de orden al menos $n+1$ en el centro. Todas las derivadas hasta $n$ allí son cero, pero en una entrada distinta puede producir un cambio arbitrario mediante su coeficiente. La unicidad del modelo se refiere a polinomios de grado a lo sumo $n$.

## §21.2 — Rolle se repite sin perder sus hipótesis

### Microcontrol 009

[]{#MA-MIC-ANM-01-021-009}

[]{#MA-MSOL-ANM-01-021-009}

[]{#MA-SEC-ANM-01-021-002}

**Pregunta.** ¿Qué igualdades centrales se necesitan para Rolle repetido de orden $n$?

**Solución.** $H_k(c)=0$ para $0\le k\le n$, más $H_0(x)=0$ con $x\ne c$.

Las igualdades en el centro se utilizan una por cada miembro de la cadena. El cero adicional de la función inicia el primer segmento. Sin un dato central nulo del siguiente miembro no habría dos bordes iguales para continuar Rolle.

### Microcontrol 010

[]{#MA-MIC-ANM-01-021-010}

[]{#MA-MSOL-ANM-01-021-010}

**Pregunta.** ¿Cuántas aplicaciones de Rolle produce la última derivada nula?

**Solución.** $n+1$ aplicaciones, incluida una sola cuando$n=0$.

El primer paso parte de $H_0$ y el último de $H_n$, así los índices van de cero a $n$. La conclusión se refiere a la derivada del último miembro, de orden $n+1$ en la cadena. En orden cero no se repite nada: se realiza un solo Rolle.

### Microcontrol 011

[]{#MA-MIC-ANM-01-021-011}

[]{#MA-MSOL-ANM-01-021-011}

**Pregunta.** ¿Qué invariante permite continuar el paso $k$?

**Solución.** $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$ y continuidad/derivabilidad en el subsegmento correspondiente.

El testigo anterior aporta el segundo cero del miembro que sigue y los datos centrales aportan el primero. Su posición estrictamente interior garantiza que no coincide con el centro. Después se vuelven a verificar continuidad de bordes y derivabilidad interior en el segmento reducido.

### Microcontrol 012

[]{#MA-MIC-ANM-01-021-012}

[]{#MA-MSOL-ANM-01-021-012}

**Pregunta.** ¿Qué relación enlaza los miembros de la cadena?

**Solución.** $H_k\prime=H_{k+1}$ en el interior para $k<n$; la derivada del último miembro también debe existir interiormente.

La igualdad entre derivada de un miembro y el siguiente transmite la conclusión del paso anterior. El último paso sólo pide que exista su derivada para anularla en algún centro interior. Sin ese enlace, los ceros de funciones diferentes no formarían una inducción válida.

### Microcontrol 013

[]{#MA-MIC-ANM-01-021-013}

[]{#MA-MSOL-ANM-01-021-013}

**Pregunta.** ¿Se pide continuidad de la derivada final?

**Solución.** No. Se necesita que exista en el interior para el último Rolle; los miembros anteriores sí son continuos sobre los segmentos.

Rolle necesita continuidad de la función a la que se aplica y existencia de su derivada en el interior. No exige continuidad de esa derivada. En la última aplicación esos papeles corresponden a $H_n$ y $H_n\prime$, respectivamente.

### Microcontrol 014

[]{#MA-MIC-ANM-01-021-014}

[]{#MA-MSOL-ANM-01-021-014}

**Pregunta.** ¿Cómo se ordena el segmento si $x<c$?

**Solución.** Con extremos $\min(c,x)$ y $\max(c,x)$; los puntos sucesivos quedan entre$c$ y el punto anterior por el lado izquierdo.

Ordenar los extremos permite aplicar el mismo enunciado a izquierda o derecha sin cambiar sus hipótesis. Cada nuevo testigo está en el interior del segmento anterior y se aproxima al centro por el lado disponible. La orientación afecta después los signos de potencias, no la validez de Rolle.

### Microcontrol 015

[]{#MA-MIC-ANM-01-021-015}

[]{#MA-MSOL-ANM-01-021-015}

**Pregunta.** ¿Qué punto intermedio se afirma si $x=c$?

**Solución.** Ninguno. No hay segmento con extremos distintos y el caso se resuelve por la igualdad central.

La evaluación central de Taylor coincide con la función y el resto es cero. No hay un punto estrictamente entre dos extremos iguales ni un incremento no nulo por el que dividir. El caso se resuelve directamente antes de introducir el auxiliar con coeficiente $A$.

### Microcontrol 016

[]{#MA-MIC-ANM-01-021-016}

[]{#MA-MSOL-ANM-01-021-016}

**Pregunta.** ¿Se selecciona una familia infinita de testigos?

**Solución.** No. Para un orden y una entrada fijados, la inducción realiza sólo un número finito de pasos existenciales.

El número de aplicaciones está determinado por el orden natural fijo. Cada existencia se utiliza para el siguiente paso de esa lista finita. No se construye una asignación de testigos para todos los órdenes o entradas de una vez.

## §21.3 — Forzar el resto: la fórmula de Lagrange

### Microcontrol 017

[]{#MA-MIC-ANM-01-021-017}

[]{#MA-MSOL-ANM-01-021-017}

[]{#MA-SEC-ANM-01-021-003}

**Pregunta.** ¿Qué coeficiente fuerza la anulación del auxiliar en $x\ne c$?

**Solución.** $A=R_{n,c}(x)/(x-c)^{n+1}$; el incremento no nulo permite dividir.

El coeficiente se diseña para que el término añadido reproduzca exactamente el resto en la entrada fijada. La potencia del incremento es no nula porque $x\ne c$. La división no se formula para el centro, cuyo error se comprueba por separado.

### Microcontrol 018

[]{#MA-MIC-ANM-01-021-018}

[]{#MA-MSOL-ANM-01-021-018}

**Pregunta.** ¿Qué función auxiliar se usa en la prueba de Lagrange?

**Solución.** $H(t)=f(t)-T_{n,c}f(t)-A(t-c)^{n+1}$.

La auxiliar conserva los datos centrales nulos del resto y añade un cero en la entrada $x$. Su potencia extra no altera las derivadas centrales hasta el orden fijado. Estas son las condiciones que permiten usar Rolle repetido en vez de suponer la fórmula del resto.

### Microcontrol 019

[]{#MA-MIC-ANM-01-021-019}

[]{#MA-MSOL-ANM-01-021-019}

**Pregunta.** ¿Por qué se anulan sus datos centrales hasta orden $n$?

**Solución.** Taylor conserva los datos y la potencia adicional tiene todas esas derivadas nulas en$c$.

Cada derivada del término extra hasta orden $n$ mantiene una potencia positiva de $t-c$. En el centro se anula y el polinomio conservado cancela los otros datos de $f$. Esa verificación debe hacerse para toda la cadena, no sólo para el valor.

### Microcontrol 020

[]{#MA-MIC-ANM-01-021-020}

[]{#MA-MSOL-ANM-01-021-020}

**Pregunta.** ¿Qué igualdad deja el último Rolle?

**Solución.** $f^{(n+1)}(\xi)-A(n+1)!=0$, pues el polinomio de orden$n$ ya tiene derivada$n+1$ nula.

La derivada de orden $n+1$ del modelo es cero por su grado. La potencia añadida produce la constante factorial y Rolle fuerza la igualdad indicada. Como el factorial es positivo, se despeja $A$ y se sustituye en la definición del resto.

### Microcontrol 021

[]{#MA-MIC-ANM-01-021-021}

[]{#MA-MSOL-ANM-01-021-021}

**Pregunta.** ¿Qué posición tiene $\xi$?

**Solución.** Está estrictamente entre$c$ y$x$, para$x\ne c$; no se predetermina como punto medio.

El lema produce un testigo dentro de los segmentos sucesivamente reducidos, todos contenidos entre los extremos originales. Puede depender de la entrada y del orden y no tiene una ubicación universal. El cubo a orden uno da un ejemplo donde el testigo no es el medio.

### Microcontrol 022

[]{#MA-MIC-ANM-01-021-022}

[]{#MA-MSOL-ANM-01-021-022}

**Pregunta.** ¿De qué datos puede depender el testigo?

**Solución.** De la función, el orden, el centro y la entrada; no se conserva como una constante al variarlos.

La existencia se obtiene para los datos de una aplicación concreta. Variarlos cambia el auxiliar y los segmentos usados, por lo que también puede cambiar el testigo. Para una cota uniforme se controla cualquier ubicación posible, sin elegirlos simultáneamente.

### Microcontrol 023

[]{#MA-MIC-ANM-01-021-023}

[]{#MA-MSOL-ANM-01-021-023}

**Pregunta.** ¿Es necesaria continuidad de $f^{(n+1)}$ para la prueba por Rolle?

**Solución.** No. Basta su existencia interior y la continuidad de los miembros hasta orden$n$ sobre el segmento.

Los miembros anteriores se usan como funciones de Rolle y deben ser continuos sobre sus segmentos. La última derivada sólo se evalúa en un centro interior donde existe. No se toma un máximo suyo ni se pasa al límite de sus valores para esta fórmula.

### Microcontrol 024

[]{#MA-MIC-ANM-01-021-024}

[]{#MA-MSOL-ANM-01-021-024}

**Pregunta.** ¿Qué se usa como dato central en el contrato cerrado?

**Solución.** Los valores de las extensiones continuas dadas $f_k(c)$; no se presupone derivar en un borde.

Las extensiones continuas forman parte del contrato y proporcionan valores centrales bien definidos. Las relaciones de derivación se exigen en los interiores pertinentes. Así un centro de frontera puede tener datos extendidos sin una última derivada finita allí.

## §21.4 — Un punto desconocido, una cota verificable

### Microcontrol 025

[]{#MA-MIC-ANM-01-021-025}

[]{#MA-MSOL-ANM-01-021-025}

[]{#MA-SEC-ANM-01-021-004}

**Pregunta.** ¿Qué cota elimina el testigo de Lagrange?

**Solución.** Una cota $|f^{(n+1)}|\le M$ válida en todo el interior donde puede estar el testigo.

El testigo tiene ubicación desconocida pero pertenece a la región donde vale la barrera. Tomar magnitudes en la fórmula y sustituir esa barrera elimina la dependencia del punto. Una muestra particular de la derivada no justificaría ese paso para todos los testigos.

### Microcontrol 026

[]{#MA-MIC-ANM-01-021-026}

[]{#MA-MSOL-ANM-01-021-026}

**Pregunta.** ¿Qué hacer si $M=0$?

**Solución.** La cota obliga al resto a ser cero; no se divide por$M$.

La desigualdad absoluta del resto se vuelve $|R|\le0$ y fuerza igualdad exacta entre función y modelo en la región acreditada. El radio no debe calcularse dividiendo por una barrera nula. El caso central también cumple igualdad por los datos conservados.

### Microcontrol 027

[]{#MA-MIC-ANM-01-021-027}

[]{#MA-MSOL-ANM-01-021-027}

**Pregunta.** ¿Qué número controla todos los errores si $|x-c|\le\rho$?

**Solución.** $M\rho^{n+1}/(n+1)!$, siempre que la misma cota de derivada valga en toda la región.

La distancia máxima a $c$ domina la potencia que aparece en todos los restos de la región. La misma barrera de derivada debe proteger cada subsegmento usado. Se obtiene una cota para todas las entradas antes de conocerlas, sin identificar sus testigos.

### Microcontrol 028

[]{#MA-MIC-ANM-01-021-028}

[]{#MA-MSOL-ANM-01-021-028}

**Pregunta.** ¿Qué función permite derivar telescópicamente la forma de Cauchy?

**Solución.** $G(t)=f(x)-\sum_{k=0}^n f^{(k)}(t)(x-t)^k/k!$, con$x$ fijado.

En esta auxiliar la entrada final $x$ permanece fija y las derivadas de la función se evalúan en el argumento variable $t$. La suma es finita y puede derivarse término a término. Su estructura reserva cancelaciones entre derivadas de coeficientes y de potencias.

### Microcontrol 029

[]{#MA-MIC-ANM-01-021-029}

[]{#MA-MSOL-ANM-01-021-029}

**Pregunta.** ¿Cuál es su derivada después de cancelar términos?

**Solución.** $G\prime(t)=-f^{(n+1)}(t)(x-t)^n/n!$.

Derivar la potencia introduce un signo menos y baja un grado, cancelando el término siguiente que deriva a la función. Sólo queda el término superior sin compañero. El signo exterior de $G$ determina el signo negativo final de esa expresión.

### Microcontrol 030

[]{#MA-MIC-ANM-01-021-030}

[]{#MA-MSOL-ANM-01-021-030}

**Pregunta.** ¿Qué forma tiene el resto de Cauchy?

**Solución.** $R=f^{(n+1)}(\eta)(x-\eta)^n(x-c)/n!$, con$\eta$ estrictamente interior.

Aplicar valor medio a $G$ relaciona sus bordes, cero y resto, con su derivada interior. Sustituir el telescopaje proporciona el factor indicado. Las potencias y el factorial difieren de Lagrange, por lo que las cotas de ambas formas deben calcularse por separado.

### Microcontrol 031

[]{#MA-MIC-ANM-01-021-031}

[]{#MA-MSOL-ANM-01-021-031}

**Pregunta.** ¿Los testigos de Lagrange y Cauchy tienen que coincidir?

**Solución.** No. Son existencias obtenidas de auxiliares diferentes.

Lagrange repetido y el telescopaje de Cauchy construyen funciones auxiliares diferentes. Cada una produce su propia existencia interior. Incluso para la misma función, centro, orden y entrada pueden tener testigos distintos, como muestra el cubo.

### Microcontrol 032

[]{#MA-MIC-ANM-01-021-032}

[]{#MA-MSOL-ANM-01-021-032}

**Pregunta.** ¿Qué ocurre al multiplicar la banda de coeficientes por un incremento elevado negativo?

**Solución.** Se invierte el orden de las cotas; una banda firmada exige controlar paridad y lado del centro.

El factorial conserva signo positivo, pero la potencia del incremento puede ser negativa si su exponente es impar y la entrada está a la izquierda. Multiplicar entonces invierte el orden de la banda. La cota absoluta evita esa orientación, mientras la firmada conserva información adicional de signo.

## §21.5 — Peano: lo que desaparece al cambiar de escala

### Microcontrol 033

[]{#MA-MIC-ANM-01-021-033}

[]{#MA-MSOL-ANM-01-021-033}

[]{#MA-SEC-ANM-01-021-005}

**Pregunta.** ¿Qué significa $R(c+h)=o(|h|^n)$?

**Solución.** Para cada$\varepsilon>0$ hay un radio que hace$|R(c+h)|<\varepsilon|h|^n$ en todas las entradas perforadas de ese radio.

La comparación normalizada se formula sólo con incrementos no nulos, pues su escala debe ser positiva para dividir. El radio responde a la tolerancia y después controla todas las entradas admisibles. No se afirma una tasa fija del siguiente orden.

### Microcontrol 034

[]{#MA-MIC-ANM-01-021-034}

[]{#MA-MSOL-ANM-01-021-034}

**Pregunta.** ¿Qué caso de Peano corresponde a$n=1$?

**Solución.** La definición de derivada en el centro; no exige derivabilidad de la función en otros centros.

El resto de orden uno es la diferencia respecto del modelo afín de la derivada. Su razón por el incremento tiende a cero por definición. Una función puede cumplir esa prueba en el centro aunque no sea derivable en los otros puntos de una vecindad.

### Microcontrol 035

[]{#MA-MIC-ANM-01-021-035}

[]{#MA-MSOL-ANM-01-021-035}

**Pregunta.** ¿Dónde se exige la derivada de orden$n$ en el contrato de Peano?

**Solución.** Sólo en el centro, como derivada de$f^{(n-1)}$; las inferiores necesarias están definidas en un entorno.

Para volver a derivar se necesita que la función de orden anterior exista cerca del centro. El último límite se exige en el centro, sin pedir que exista o sea continuo en toda una vecindad. Ese contrato es más débil que el usado para una cota de resto de Lagrange de orden superior.

### Microcontrol 036

[]{#MA-MIC-ANM-01-021-036}

[]{#MA-MSOL-ANM-01-021-036}

**Pregunta.** ¿Qué herramienta recupera$H$ desde una cota para$H\prime$ en la inducción?

**Solución.** Cauchy sobre$H$ y$(t-c)^n$, cuyo cociente de derivadas divide por$n(\xi-c)^{n-1}\ne0$.

El testigo está estrictamente entre el centro y la entrada no nula. Su distancia al centro es positiva, por lo que la derivada del monomio denominador no se anula. La estimación inductiva de la derivada de $H$ controla así la razón del resto sin derivar un símbolo de error.

### Microcontrol 037

[]{#MA-MIC-ANM-01-021-037}

[]{#MA-MSOL-ANM-01-021-037}

**Pregunta.** ¿Peano proporciona una constante para$|h|^{n+1}$?

**Solución.** No. Describe un error normalizado que tiende a cero, sin garantizar una cota del siguiente orden.

La notación de error pequeño sólo promete que el cociente por $|h|^n$ tiende a cero. Una cota por $|h|^{n+1}$ exigiría además una barrera para un cociente diferente. El ejemplo con raíz en el resto separa ambas garantías.

### Microcontrol 038

[]{#MA-MIC-ANM-01-021-038}

[]{#MA-MSOL-ANM-01-021-038}

**Pregunta.** ¿Qué cociente tiende a cero para$h^2\sqrt{|h|}$ a orden2?

**Solución.** $f(h)/|h|^2=\sqrt{|h|}\to0$.

En entradas no nulas el factor cuadrático se cancela exactamente con la escala de orden dos. Queda una raíz de magnitud que tiende a cero desde ambos lados. El valor central se trata por evaluación directa y también es cero.

### Microcontrol 039

[]{#MA-MIC-ANM-01-021-039}

[]{#MA-MSOL-ANM-01-021-039}

**Pregunta.** ¿Por qué ese ejemplo no tiene una cota$C|h|^3$ en un radio?

**Solución.** Su cociente por$|h|^3$ es$1/\sqrt{|h|}$, no acotado cerca de cero.

Comparar con la escala cúbica deja un recíproco de raíz. Puede superar cualquier barrera positiva en cualquier ventana perforada suficientemente pequeña. Por ello el mismo resto cumple Peano de orden dos y refuta una tasa cúbica uniforme.

### Microcontrol 040

[]{#MA-MIC-ANM-01-021-040}

[]{#MA-MSOL-ANM-01-021-040}

**Pregunta.** ¿Puede derivarse un símbolo$o$ sin hipótesis adicionales?

**Solución.** No. Un control de valores del resto no proporciona automáticamente un control de su derivada.

Una relación asintótica de valores no declara que el resto tenga derivada ni estima esa derivada si existe. Las operaciones del capítulo usan identidades, cotas y funciones bajo contratos explícitos. Derivar la abreviatura sin esas condiciones introduciría una conclusión no demostrada.

## §21.6 — La primera derivada que no se anula

### Microcontrol 041

[]{#MA-MIC-ANM-01-021-041}

[]{#MA-MSOL-ANM-01-021-041}

[]{#MA-SEC-ANM-01-021-006}

**Pregunta.** ¿Qué término decide el criterio de la primera derivada no nula?

**Solución.** $ah^m$, con$a=f^{(m)}(c)/m!\ne0$, tras anular las derivadas anteriores.

Las derivadas previas nulas eliminan todos los términos menores del incremento de la función. El factorial positivo convierte la primera derivada no nula en el coeficiente real $a$. El resto de Peano será pequeño respecto de ese término y permitirá decidir signos.

### Microcontrol 042

[]{#MA-MIC-ANM-01-021-042}

[]{#MA-MSOL-ANM-01-021-042}

**Pregunta.** ¿Qué tolerancia evita que el resto cambie el signo principal?

**Solución.** $|r(h)|<(|a|/2)|h|^m$ en un radio perforado.

La mitad de la magnitud principal deja un margen positivo al sumar el resto. Por la triangular inversa el error no puede cancelar ni invertir ese término. La precisión se fija antes de las entradas y controla una vecindad completa perforada.

### Microcontrol 043

[]{#MA-MIC-ANM-01-021-043}

[]{#MA-MSOL-ANM-01-021-043}

**Pregunta.** ¿Qué da un primer orden no nulo par con coeficiente positivo?

**Solución.** Un mínimo local estricto en un centro interior, porque el término principal es positivo en ambos lados.

Un exponente par hace positivo $h^m$ en toda entrada no nula de ambos lados. El resto dominado deja la diferencia de valores estrictamente positiva. Así el centro es un mínimo local estricto, sin afirmar que sea mínimo global.

### Microcontrol 044

[]{#MA-MIC-ANM-01-021-044}

[]{#MA-MSOL-ANM-01-021-044}

**Pregunta.** ¿Qué da un primer orden no nulo impar?

**Solución.** No hay extremo local interior: el incremento de la función cambia de signo entre ambos lados.

Un exponente impar cambia el signo de $h^m$ entre izquierda y derecha. El presupuesto mantiene esos dos signos en la diferencia de valores. Interioridad permite encontrar entradas de ambos lados arbitrariamente cerca, lo que excluye máximos y mínimos locales.

### Microcontrol 045

[]{#MA-MIC-ANM-01-021-045}

[]{#MA-MSOL-ANM-01-021-045}

**Pregunta.** ¿Qué concluye el criterio si todas las derivadas disponibles son cero?

**Solución.** No clasifica el centro; datos de orden mayor pueden producir mínimo, máximo o ninguna de esas alternativas.

El criterio necesita un término principal no nulo para dominar el resto. Datos nulos hasta un orden finito pueden compartirse por polinomios positivos, negativos o de signo cambiante. No poder aplicar el criterio no equivale a demostrar ausencia de extremo.

### Microcontrol 046

[]{#MA-MIC-ANM-01-021-046}

[]{#MA-MSOL-ANM-01-021-046}

**Pregunta.** ¿Un mínimo local de Taylor es automáticamente global?

**Solución.** No. $h^2-h^4$ tiene mínimo local en cero y valores negativos lejos; convexidad global era una hipótesis adicional en C20.

La comparación local vale en el radio donde el término cuadrático domina al resto. Fuera de esa región el término negativo de cuarto grado puede producir salidas menores que la central. El soporte global de C20 requería convexidad en todo el intervalo, que aquí no se conserva.

### Microcontrol 047

[]{#MA-MIC-ANM-01-021-047}

[]{#MA-MSOL-ANM-01-021-047}

**Pregunta.** ¿Qué cambia al aplicar paridad en una frontera?

**Solución.** Puede faltar uno de los lados; por ejemplo la identidad tiene mínimo de borde en$[0,1]$.

La conclusión impar de ausencia de extremo utiliza dos signos y por ello dos direcciones de entrada. En una frontera puede existir sólo la dirección donde el incremento es positivo. La comparación unilateral puede entonces certificar un mínimo relativo sin contradecir el criterio interior.

### Microcontrol 048

[]{#MA-MIC-ANM-01-021-048}

[]{#MA-MSOL-ANM-01-021-048}

**Pregunta.** ¿Peano determina por sí solo el signo del resto?

**Solución.** No. Lo hace pequeño frente a un término principal no nulo; una cota firmada de Lagrange añade otra información.

Un resto normalizado pequeño puede tener cualquiera de los dos signos en diferentes entradas. El criterio de extremos controla la suma porque hay un término principal que no se anula. Un signo del resto por sí mismo requiere otra información, como el signo de la derivada de la fórmula de Lagrange.

## §21.7 — Aproximantes con certificados racionales

### Microcontrol 049

[]{#MA-MIC-ANM-01-021-049}

[]{#MA-MSOL-ANM-01-021-049}

[]{#MA-SEC-ANM-01-021-007}

**Pregunta.** ¿Qué polinomio central tiene$1/(1-h)$ a orden$n$?

**Solución.** $\sum_{k=0}^n h^k$, por$f^{(k)}(0)=k!$.

La inducción de derivadas produce un factorial que se cancela con el denominador del coeficiente central. Todos los coeficientes resultan uno. La suma termina en el orden fijado y todavía no constituye una afirmación de representación infinita.

### Microcontrol 050

[]{#MA-MIC-ANM-01-021-050}

[]{#MA-MSOL-ANM-01-021-050}

**Pregunta.** ¿Cuál es su resto exacto finito?

**Solución.** $h^{n+1}/(1-h)$, siempre que$h\ne1$ y dentro del dominio declarado.

Multiplicar la suma geométrica finita por $1-h$ cancela términos vecinos y deja $1-h^{n+1}$. El denominador no nulo permite despejar la diferencia exacta. Esa identidad acredita el resto sin pasar al límite de una sucesión de sumas.

### Microcontrol 051

[]{#MA-MIC-ANM-01-021-051}

[]{#MA-MSOL-ANM-01-021-051}

**Pregunta.** ¿Qué margen protege el denominador en$|h|\le\rho<1$?

**Solución.** $1-h\ge1-\rho>0$, que produce$|R|\le\rho^{n+1}/(1-\rho)$.

La barrera de distancia a la singularidad vale en toda la región elegida. Invertir una cantidad positiva al menos $1-\rho$ limita el denominador del resto. La potencia del incremento se controla por la misma escala $\rho$, dando una cota común.

### Microcontrol 052

[]{#MA-MIC-ANM-01-021-052}

[]{#MA-MSOL-ANM-01-021-052}

**Pregunta.** ¿Qué polinomio de orden2 aproxima$\sqrt{1+h}$ en cero?

**Solución.** $1+h/2-h^2/8$.

Los datos centrales son uno, media pendiente y segunda derivada menos un cuarto. El coeficiente cuadrático divide ese último dato por $2!=2$. La definición del modelo fija los tres coeficientes; su error fuera del centro se estudia después con la tercera derivada.

### Microcontrol 053

[]{#MA-MIC-ANM-01-021-053}

[]{#MA-MSOL-ANM-01-021-053}

**Pregunta.** ¿Qué cota racional de tercera derivada sirve en$|h|\le1/4$?

**Solución.** $0<g^{(3)}\le8/9$, usando$1+h\ge3/4$ y$\sqrt{1+h}\ge3/4$.

La raíz está definida y es positiva en toda la región. La cota racional inferior de la raíz evita necesitar su valor exacto para proteger el denominador de $g^{(3)}$. El cociente queda acotado en cualquier posible testigo interior, no sólo en el centro.

### Microcontrol 054

[]{#MA-MIC-ANM-01-021-054}

[]{#MA-MSOL-ANM-01-021-054}

**Pregunta.** ¿Qué certificado da Taylor para$\sqrt{5/4}$?

**Solución.** $143/128<\sqrt{5/4}\le143/128+1/432$; el resto es positivo y está acotado.

El incremento un cuarto está en el segmento protegido por la barrera de tercera derivada. La fórmula da un resto estrictamente positivo y su magnitud no supera la cota racional. Por eso el borde inferior se excluye y el superior se incluye; sus desigualdades responden a justificaciones distintas.

### Microcontrol 055

[]{#MA-MIC-ANM-01-021-055}

[]{#MA-MSOL-ANM-01-021-055}

**Pregunta.** ¿Qué diferencia de cuadrados permite un cotejo independiente?

**Solución.** $5/4-(143/128)^2=31/16384$; racionalizar y usar raíz al menos1 da error$\le31/34688$.

La diferencia positiva de cuadrados acredita que el aproximante está por debajo de la raíz. Al racionalizar, la suma de ambos valores protege el denominador. Una cota inferior sencilla de la raíz basta para producir el certificado, más ajustado que el de derivadas en este caso.

### Microcontrol 056

[]{#MA-MIC-ANM-01-021-056}

[]{#MA-MSOL-ANM-01-021-056}

**Pregunta.** ¿Una muestra de derivada basta para certificar el error?

**Solución.** No. La cota debe controlar todo el segmento donde puede encontrarse el testigo.

El teorema puede localizar su testigo en cualquier posición interior permitida por las hipótesis. Una barrera válida sólo en muestras no protege esas otras posiciones. El certificado necesita una desigualdad demostrada en toda la región y un dominio donde todas las evaluaciones estén definidas.

## §21.8 — Combinar modelos y elegir la resolución

### Microcontrol 057

[]{#MA-MIC-ANM-01-021-057}

[]{#MA-MSOL-ANM-01-021-057}

[]{#MA-SEC-ANM-01-021-008}

**Pregunta.** ¿Qué errores aparecen al multiplicar$P+u$ por$Q+v$?

**Solución.** $Pv+Qu+uv$, además de eliminar términos del producto polinómico que superen el orden fijado.

Expandir el producto muestra todos los errores cruzados antes de truncar. Los factores polinómicos están acotados cerca del centro y los cocientes normalizados de los errores tienden a cero. Los términos de grado superior del producto requieren además su propio control de truncación.

### Microcontrol 058

[]{#MA-MIC-ANM-01-021-058}

[]{#MA-MSOL-ANM-01-021-058}

**Pregunta.** ¿Por qué un polinomio de términos de grado mayor que$n$ es$o(|h|^n)$?

**Solución.** Se factoriza como$h^{n+1}$ por un polinomio acotado cerca de cero; tras normalizar queda un factor$|h|\to0$.

El factor polinómico restante tiene una barrera en alguna vecindad del centro. Al dividir magnitudes por $|h|^n$ queda $|h|$ multiplicado por esa barrera. Esto tiende a cero y acredita el orden del truncamiento sin derivar el resto.

### Microcontrol 059

[]{#MA-MIC-ANM-01-021-059}

[]{#MA-MSOL-ANM-01-021-059}

**Pregunta.** ¿Qué margen tiene$1-h-h^2$ en$|h|\le1/4$?

**Solución.** Al menos$11/16>0$.

La desigualdad $1-h-h^2\ge1-|h|-|h|^2$ da en la región $1-1/4-1/16=11/16$. La barrera es estrictamente positiva y protege todas las divisiones. Se utiliza tanto para definir la función en la región como para estimar el resto.

### Microcontrol 060

[]{#MA-MIC-ANM-01-021-060}

[]{#MA-MSOL-ANM-01-021-060}

**Pregunta.** ¿Qué Taylor de orden2 tiene$1/(1-h-h^2)$ en cero?

**Solución.** $1+h+2h^2$; el resto exacto es$(3h^3+2h^4)/(1-h-h^2)$.

Los datos centrales de derivadas son uno, uno y cuatro, así el último coeficiente es dos. Multiplicar el modelo por el denominador verifica el resto exacto. Su numerador empieza en grado tres y la barrera positiva convierte esa identidad en una cota cúbica.

### Microcontrol 061

[]{#MA-MIC-ANM-01-021-061}

[]{#MA-MSOL-ANM-01-021-061}

**Pregunta.** ¿Qué orden certifica error menor que$1/1000$ para$1/(1-h)$ en$|h|\le1/4$?

**Solución.** Orden5, con cota$1/3072$; orden4 tiene error$1/768$ en$h=1/4$ y falla.

La cota común geométrica se alcanza en el extremo positivo de la región. Por eso un orden cuya cota excede la tolerancia realmente falla, no sólo pierde una garantía. El siguiente orden reduce la cota por cuatro y cumple la desigualdad estricta requerida.

### Microcontrol 062

[]{#MA-MIC-ANM-01-021-062}

[]{#MA-MSOL-ANM-01-021-062}

**Pregunta.** ¿Qué dos procesos no deben confundirse?

**Solución.** Reducir el radio con un orden fijo y aumentar el grado sobre una región fija; cada uno necesita su propio control del resto.

Con un orden fijo, el radio regula qué entradas quedan cerca del centro. Con una región fija, aumentar el orden cambia el modelo y el resto que debe acotarse. Las hipótesis de un proceso no demuestran automáticamente el otro ni una suma infinita.

### Microcontrol 063

[]{#MA-MIC-ANM-01-021-063}

[]{#MA-MSOL-ANM-01-021-063}

**Pregunta.** ¿Cómo preservar datos centrales y un número finito de muestras mientras se cambia otra salida?

**Solución.** Añadiendo$A h^{n+1}\prod_j(h-h_j)^2$; su factor se anula en las muestras y hasta el orden central indicado.

El factor central anula todos los datos hasta el orden fijado y los factores de muestras conservan sus evaluaciones. En otra entrada donde no se anulan esos factores, su producto es no nulo. El coeficiente libre permite imponer allí cualquier salida, mostrando la información que los datos finitos dejan abierta.

### Microcontrol 064

[]{#MA-MIC-ANM-01-021-064}

[]{#MA-MSOL-ANM-01-021-064}

**Pregunta.** ¿Qué representación infinita se ha probado en este capítulo?

**Solución.** Ninguna. Se prueban polinomios finitos, residuos y cotas; una expansión infinita exige justificar por separado su suma y su resto.

El orden y todas las sumas del capítulo son finitos. Los controles describen sus residuos con dominios y tolerancias específicos. Para una representación infinita habría que justificar un nuevo límite y que el resto tienda a cero en el régimen correspondiente.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)

