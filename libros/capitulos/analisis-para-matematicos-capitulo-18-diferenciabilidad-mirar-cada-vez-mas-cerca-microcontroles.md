---
content-id: MA-BCH-0277
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-018-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 18
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C18_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)

Las preguntas se reproducen literalmente para facilitar el cotejo; sus IDs y huellas vinculan cada solución con el manuscrito.

## §18.1 — Pendientes con un centro fijo

### Microcontrol 001

[]{#MA-MIC-ANM-01-018-001}

[]{#MA-MSOL-ANM-01-018-001}

[]{#MA-SEC-ANM-01-018-001}

**Pregunta.** ¿Dónde vive el cociente incremental centrado en $a$?

**Solución.** En $D\setminus\{a\}$; $f(a)$ debe existir, pero $q_{f,a}(a)$ no está definido.

La diferencia de valores utiliza la evaluación central $f(a)$, por lo que $a$ debe ser una entrada. La división utiliza $x-a$ y sólo se permite cuando $x\ne a$. Así el centro pertenece al dominio de la función, pero no al del cociente. La derivada estudia un límite de ese nuevo objeto sin evaluarlo en su centro.

### Microcontrol 002

[]{#MA-MIC-ANM-01-018-002}

[]{#MA-MSOL-ANM-01-018-002}

**Pregunta.** ¿Por qué se exige $a\in\operatorname{Acc}(D)$?

**Solución.** Para disponer de entradas distintas del centro en todo radio y garantizar unicidad del límite; en un aislado la condición sería vacía para cualquier pendiente.

La acumulación permite encontrar una entrada perforada en cualquier ventana positiva. Sin ella, elegir una ventana vacía haría válidas todas las pendientes candidatas y no habría un valor único que llamar derivada. El capítulo excluye ese caso mediante una condición sobre el dominio antes de investigar el límite.

### Microcontrol 003

[]{#MA-MIC-ANM-01-018-003}

[]{#MA-MSOL-ANM-01-018-003}

**Pregunta.** ¿Qué variables están fijadas antes de elegir el radio de derivabilidad?

**Solución.** La función, su dominio, el centro y la tolerancia para el error de pendiente. El radio se fija antes de la entrada variable.

El centro permanece fijo en todas las secantes de esa prueba. El radio puede responder al centro y a la precisión, pero no adaptarse después a cada entrada. Para verificarlo se consideran todas las entradas admisibles con distancia positiva menor que él. Una tabla de algunas secantes no cumple esa obligación universal.

### Microcontrol 004

[]{#MA-MIC-ANM-01-018-004}

[]{#MA-MSOL-ANM-01-018-004}

**Pregunta.** ¿Cuál es la derivada de $x^2$ en $a$ y qué identidad la prueba?

**Solución.** Es $2a$, porque el cociente en $a+h$ es $2a+h$ para $h\ne0$ y su diferencia respecto de $2a$ vale $h$.

La factorización del numerador cancela $h$ sólo porque se ha excluido $h=0$. El error de pendiente tiene magnitud $|h|$ y por ello el radio igual a la tolerancia lo controla directamente. La evaluación central del cuadrado ya está definida. Ninguna secante individual tiene que coincidir con el valor límite para que la prueba funcione.

### Microcontrol 005

[]{#MA-MIC-ANM-01-018-005}

[]{#MA-MSOL-ANM-01-018-005}

**Pregunta.** ¿Una pendiente secante muy grande equivale a una derivada real?

**Solución.** No. La derivada definida aquí exige un límite finito único de todas las secantes suficientemente cercanas.

El tamaño de una secante concreta no determina el límite del conjunto de secantes próximas. Puede variar según la escala o según el lado de aproximación. Aquí la definición pide un real finito y control de todas las entradas admitidas. Una tendencia sin cota tampoco produce una derivada real finita bajo esta convención.

### Microcontrol 006

[]{#MA-MIC-ANM-01-018-006}

[]{#MA-MSOL-ANM-01-018-006}

**Pregunta.** ¿Qué debe conservar una restricción para heredar la derivada?

**Solución.** El centro y su acumulación en el dominio restringido; luego los mismos radios controlan sus argumentos perforados.

La restricción conserva el valor central y los cocientes de las entradas que mantiene. Los radios originales siguen controlando esos cocientes. Pero la restricción podría aislar el centro, y entonces faltaría una premisa de la definición. Conservar acumulación asegura que la nueva derivada exista en el sentido adoptado y tenga el mismo valor.

### Microcontrol 007

[]{#MA-MIC-ANM-01-018-007}

[]{#MA-MSOL-ANM-01-018-007}

**Pregunta.** ¿Qué derivada relativa tiene $|x|$ en cero sobre $[0,\infty)$?

**Solución.** Uno: todos los cocientes relativos perforados valen uno. Esto no afirma derivabilidad bilateral sobre toda la recta.

En ese dominio sólo hay entradas positivas distintas del centro y allí $|x|=x$. El cociente vale exactamente uno y su error respecto de uno es cero. En la recta se añaden entradas negativas con cociente menos uno, que cambian la pregunta de límite. Una conclusión relativa no se transporta al dominio mayor sin revisar esas nuevas entradas.

### Microcontrol 008

[]{#MA-MIC-ANM-01-018-008}

[]{#MA-MSOL-ANM-01-018-008}

**Pregunta.** ¿Tiene derivada según R1 una función en un singleton?

**Solución.** No en su único punto, porque ese punto no es de acumulación del dominio.

Su única entrada es aislada y no hay secantes admitidas en ninguna escala. La continuidad sí puede verificarse allí porque compara el valor central consigo mismo. La derivada, en cambio, exige acumulación para identificar una pendiente a partir de otras entradas. Son condiciones diferentes sobre el mismo punto.

## §18.2 — El error que desaparece al ampliar

### Microcontrol 009

[]{#MA-MIC-ANM-01-018-009}

[]{#MA-MSOL-ANM-01-018-009}

[]{#MA-SEC-ANM-01-018-002}

**Pregunta.** ¿Qué error identifica la pendiente correcta?

**Solución.** El resto dividido por el incremento, que debe tender a cero; equivalentemente, $|r_L(x)|<\eta|x-a|$ para toda tolerancia en algún radio.

La identidad $r_L(x)/(x-a)=q_{f,a}(x)-L$ convierte error normalizado en error de pendiente. Multiplicar las magnitudes por $|x-a|>0$ da la versión con presupuestos lineales. La equivalencia sólo se formula en entradas perforadas. En el centro el resto vale cero, pero la razón no se define.

### Microcontrol 010

[]{#MA-MIC-ANM-01-018-010}

[]{#MA-MSOL-ANM-01-018-010}

**Pregunta.** ¿Por qué error absoluto tendente a cero no identifica $L$?

**Solución.** Para una función continua, restar cualquier recta por el centro sigue dando error tendente a cero. La normalización por $x-a$ distingue las pendientes.

Todas las rectas que pasan por el punto central tienen el mismo valor allí. Si la función es continua, su diferencia con cualquiera de ellas tiende a cero en magnitud absoluta. Dividir por el incremento pregunta algo más preciso: si el error desaparece en comparación con la distancia de entrada. Esa condición distingue el modelo de primer orden.

### Microcontrol 011

[]{#MA-MIC-ANM-01-018-011}

[]{#MA-MSOL-ANM-01-018-011}

**Pregunta.** ¿Cuánto vale el resto del cuadrado con pendiente $2a$?

**Solución.** $r_{2a}(a+h)=h^2$, por expansión exacta.

La expansión da $(a+h)^2=a^2+2ah+h^2$. Los dos primeros términos son exactamente el modelo afín con pendiente $2a$ y el tercero es el resto. Al normalizar por $h\ne0$ queda $h$, que tiende a cero. Este ejemplo tiene un resto cuadrático demostrado, aunque no toda función derivable deba tenerlo.

### Microcontrol 012

[]{#MA-MIC-ANM-01-018-012}

[]{#MA-MSOL-ANM-01-018-012}

**Pregunta.** ¿Qué papel cumple la acumulación en la unicidad del modelo?

**Solución.** Proporciona una entrada perforada dentro del mínimo de dos radios; al dividir allí, dos pendientes distintas contradicen ambos presupuestos de error.

Si dos pendientes distaran $d>0$, sus presupuestos de resto se pedirían con una fracción de $d$. Una entrada perforada dentro de ambos radios permite restar las identidades y dividir por su distancia positiva. La suma de los errores sería menor que la distancia entre las pendientes. La acumulación justifica esa entrada concreta, sin seleccionar una ruta.

### Microcontrol 013

[]{#MA-MIC-ANM-01-018-013}

[]{#MA-MSOL-ANM-01-018-013}

**Pregunta.** ¿Qué entradas admite $G_t(u)$?

**Solución.** Sólo las que cumplen $a+tu\in D$; si el dominio está roto no puede suponerse que todo un marco de $u$ sea admisible.

El zoom transforma una coordenada $u$ en la entrada original $a+tu$. Su evaluación sólo existe si esa entrada pertenece a $D$, y se usa una escala $t\ne0$ para dividir. En un dominio con huecos, el conjunto admisible de coordenadas puede depender de $t$. Dibujar un marco completo no autoriza llenar esos huecos.

### Microcontrol 014

[]{#MA-MIC-ANM-01-018-014}

[]{#MA-MSOL-ANM-01-018-014}

**Pregunta.** ¿Por qué se limita el marco de zoom a $|u|\le R$?

**Solución.** La cota $\eta|u|$ se convierte en una cota común $\eta R$. Sin limitar $u$, ese presupuesto no protege toda la recta.

La estimación de derivabilidad se multiplica por la magnitud de la coordenada ampliada. Un marco acotado permite sustituirla por una barrera común y diseñar una escala válida para todas sus entradas admitidas. Si $R=0$, sólo hay la coordenada central y su error es cero. Sin una barrera del marco, la misma estimación no produce control uniforme sobre todas las coordenadas.

### Microcontrol 015

[]{#MA-MIC-ANM-01-018-015}

[]{#MA-MSOL-ANM-01-018-015}

**Pregunta.** ¿Qué significa $o(|x-a|)$ en este capítulo?

**Solución.** Una abreviatura del límite cero del error normalizado sobre el dominio perforado, sin imponer una tasa cuadrática.

El símbolo resume una obligación de tolerancias: el cociente de magnitudes del resto por $|x-a|$ puede hacerse menor que cualquier positivo. No añade una constante $B$ con resto menor que $B|x-a|^2$. Las dos tasas son distintas y el ejemplo $|x|\sqrt{|x|}$ las separa. La notación conserva el dominio relativo de aproximación.

### Microcontrol 016

[]{#MA-MIC-ANM-01-018-016}

[]{#MA-MSOL-ANM-01-018-016}

**Pregunta.** ¿La recta de R2 minimiza necesariamente todo error a distancia finita?

**Solución.** No. Su propiedad es el error de orden menor que $|x-a|$ al acercarse al centro.

La propiedad se refiere a cómo cambia el error al reducir la distancia al centro. No compara todas las rectas mediante un criterio de ajuste en un intervalo fijo. Una recta distinta podría aproximar mejor alguna entrada lejana sin ser el modelo de primer orden. La unicidad demostrada corresponde al error normalizado tendente a cero.

## §18.3 — Continuidad, esquinas y alcance del control

### Microcontrol 017

[]{#MA-MIC-ANM-01-018-017}

[]{#MA-MSOL-ANM-01-018-017}

[]{#MA-SEC-ANM-01-018-003}

**Pregunta.** ¿Qué tolerancia inicial produce una cota de pendientes?

**Solución.** La tolerancia uno respecto de $L$; resulta $|q|<|L|+1$ cerca del centro.

El límite finito de pendientes implica que dentro de alguna ventana su distancia a $L$ es menor que uno. La triangular da entonces $|q|<|L|+1$, una constante estrictamente positiva. Multiplicar por la distancia de entrada controla el error de valores. La barrera se obtiene del límite antes de elegir la precisión de continuidad.

### Microcontrol 018

[]{#MA-MIC-ANM-01-018-018}

[]{#MA-MSOL-ANM-01-018-018}

**Pregunta.** ¿Cómo se trata el argumento $x=a$ al demostrar continuidad?

**Solución.** Se comprueba aparte: el error de salida es cero. No se evalúa allí el cociente perforado.

La continuidad incluye la entrada central y allí la diferencia $f(a)-f(a)$ vale cero. Para entradas distintas se usa la cota de secantes y se multiplica por $|x-a|$. Separar estos dos casos verifica toda la bola relativa. Así se evita introducir una evaluación de $q$ que no pertenece a su dominio.

### Microcontrol 019

[]{#MA-MIC-ANM-01-018-019}

[]{#MA-MSOL-ANM-01-018-019}

**Pregunta.** ¿Qué radio transforma la cota $C|x-a|$ en error menor que $\varepsilon$?

**Solución.** $\min(r,\varepsilon/C)$ con $C>0$, usando el radio $r$ donde la cota está probada.

El primer radio conserva la región donde la estimación es válida; el segundo convierte distancia en precisión de salida. Su mínimo positivo cumple ambas condiciones a la vez. La distancia de entrada estricta da error final estricto, incluso si la cota inicial es no estricta. La positividad de $C$ legitima la división.

### Microcontrol 020

[]{#MA-MIC-ANM-01-018-020}

[]{#MA-MSOL-ANM-01-018-020}

**Pregunta.** ¿Por qué falla la derivada bilateral de $|x|$ en cero?

**Solución.** Las pendientes de las entradas positivas y negativas son uno y menos uno; no pueden acercarse al mismo real con error menor que $1/2$.

Dentro de cualquier radio positivo se pueden tomar entradas de signos opuestos. Sus pendientes difieren en dos y, si ambas estuvieran a distancia menor que medio de un candidato, la triangular las separaría menos que uno. Esa contradicción descarta cualquier candidato real. La refutación utiliza secantes válidas, no sólo la forma visible de la esquina.

### Microcontrol 021

[]{#MA-MIC-ANM-01-018-021}

[]{#MA-MSOL-ANM-01-018-021}

**Pregunta.** ¿Pendiente nula en un punto implica constancia cerca?

**Solución.** No. $x^3$ tiene derivada cero en cero y cambia de valor y de signo arbitrariamente cerca.

El cociente centrado de $x^3$ es $x^2$ y tiende a cero. Sin embargo, entradas positivas y negativas tienen salidas de signos opuestos respecto del valor central. Por eso tampoco hay máximo ni mínimo local en cero. Una pendiente nula sólo identifica el término lineal del modelo y no decide el comportamiento restante.

### Microcontrol 022

[]{#MA-MIC-ANM-01-018-022}

[]{#MA-MSOL-ANM-01-018-022}

**Pregunta.** ¿Qué centro queda fijo en la cota de R3?

**Solución.** $a$. El resultado compara $f(x)$ con $f(a)$, sin controlar todos los pares $x,y$ próximos.

La estimación tiene forma $|f(x)-f(a)|\le C|x-a|$ con una evaluación central fija. Una condición Lipschitz vecina pediría una cota para $|f(x)-f(y)|$ de cualquier par en la región. Ese nuevo centro $y$ no está controlado por la primera afirmación. El ejemplo racional/irracional muestra que la diferencia de alcance es efectiva.

### Microcontrol 023

[]{#MA-MIC-ANM-01-018-023}

[]{#MA-MSOL-ANM-01-018-023}

**Pregunta.** ¿Qué derivada tiene en cero la función racional/irracional de R3?

**Solución.** Cero, pues su cociente tiene magnitud a lo sumo $|x|$ aunque sea discontinua en todos los otros puntos.

En el centro cero la función vale cero y satisface $|F(x)|\le x^2$ para todas las entradas. Por ello su cociente tiene error a lo sumo $|x|$ respecto de cero. La densidad de ambas clases de entradas provoca discontinuidad en cada centro no nulo. La derivabilidad puntual no convierte ese control centrado en regularidad de todo el entorno.

### Microcontrol 024

[]{#MA-MIC-ANM-01-018-024}

[]{#MA-MSOL-ANM-01-018-024}

**Pregunta.** ¿Qué comparación local permite $f\prime(a)>0$?

**Solución.** Cerca del centro, las entradas mayores que $a$ tienen salida mayor que $f(a)$ y las menores tienen salida menor. No es aún monotonía entre todos los pares.

La tolerancia $f\prime(a)/2$ mantiene positivas las secantes suficientemente cercanas. El signo del incremento $x-a$ decide entonces el de la diferencia $f(x)-f(a)$. Esto compara cada entrada con el mismo centro. No se han controlado secantes centradas en otros puntos y por ello no se deduce crecimiento de toda una vecindad.

## §18.4 — Operaciones sobre incrementos

### Microcontrol 025

[]{#MA-MIC-ANM-01-018-025}

[]{#MA-MSOL-ANM-01-018-025}

[]{#MA-SEC-ANM-01-018-004}

**Pregunta.** ¿Qué factor requiere continuidad en la prueba del producto?

**Solución.** El factor $f(x)$ en $f(x)q_g(x)+g(a)q_f(x)$; R3 da su límite $f(a)$.

La identidad del producto mezcla cocientes centrados con un valor variable de la función. Los límites de los cocientes no bastan para ese factor. Derivabilidad de $f$ implica continuidad y proporciona $f(x)\to f(a)$. Sólo después se aplica la regla de producto de límites y se obtiene la fórmula solicitada.

### Microcontrol 026

[]{#MA-MIC-ANM-01-018-026}

[]{#MA-MSOL-ANM-01-018-026}

**Pregunta.** ¿Qué dominio comparte la regla de suma?

**Solución.** Un mismo dominio $D$ para ambos sumandos, con $a\in D\cap\operatorname{Acc}(D)$ y ambas derivadas existentes allí.

Para sumar los cocientes se necesitan ambas evaluaciones en cada entrada considerada y el mismo denominador $x-a$. Si los dominios fueran distintos, habría que restringirlos a su intersección y comprobar acumulación allí. La mera acumulación de cada dominio separado no garantiza esa premisa común. El dominio declarado evita esa omisión.

### Microcontrol 027

[]{#MA-MIC-ANM-01-018-027}

[]{#MA-MSOL-ANM-01-018-027}

**Pregunta.** ¿Qué margen da $g(a)\ne0$ junto con continuidad?

**Solución.** En una vecindad relativa, $|g(x)|>|g(a)|/2>0$, por lo que el recíproco está definido cerca.

La triangular inversa da $|g(x)|\ge|g(a)|-|g(x)-g(a)|$. Pedir a continuidad error menor que la mitad de $|g(a)|$ entrega la separación requerida. Ese margen asegura definición del recíproco y control del denominador de su secante. La hipótesis $g(a)\ne0$ también protege la propia evaluación central.

### Microcontrol 028

[]{#MA-MIC-ANM-01-018-028}

[]{#MA-MSOL-ANM-01-018-028}

**Pregunta.** ¿Cuál es el dominio efectivo de $f/g$?

**Solución.** $E=\{x\in D:g(x)\ne0\}$, con numerador restringido expresamente a ese dominio.

El cociente sólo tiene valor donde su denominador no se anula. Tanto el numerador como el denominador se consideran allí restringidos y conservan sus evaluaciones originales. En un centro con $g(a)\ne0$, el margen local protege una ventana completa relativa. No se asigna derivada del cociente en los ceros excluidos de su dominio.

### Microcontrol 029

[]{#MA-MIC-ANM-01-018-029}

[]{#MA-MSOL-ANM-01-018-029}

**Pregunta.** ¿Por qué ese dominio efectivo acumula en $a$?

**Solución.** Contiene toda una vecindad relativa de $a$ en $D$ y $a$ ya era de acumulación en $D$.

Para cualquier ventana deseada se toma el mínimo de su radio y el radio donde el denominador está protegido. La acumulación de $D$ proporciona dentro una entrada distinta de $a$. Esa entrada pertenece también a $E$ porque allí $g$ no se anula. Así se acredita acumulación del dominio efectivo con un testigo para cada ventana.

### Microcontrol 030

[]{#MA-MIC-ANM-01-018-030}

[]{#MA-MSOL-ANM-01-018-030}

**Pregunta.** ¿Qué signo aparece en la derivada de $1/g$?

**Solución.** El negativo: $-(g\prime(a))/g(a)^2$, procedente de la diferencia de recíprocos.

Al restar recíprocos, el numerador es $g(a)-g(x)$ y por ello introduce el signo menos respecto del cociente de $g$. El denominador es $g(x)g(a)$ y tiende a $g(a)^2>0$. La protección local permite aplicar la regla de límite del cociente. El signo proviene de una identidad, no de una regla memorizada sin dominio.

### Microcontrol 031

[]{#MA-MIC-ANM-01-018-031}

[]{#MA-MSOL-ANM-01-018-031}

**Pregunta.** ¿Cómo se trata la potencia cero en el origen?

**Solución.** Como la constante uno, con derivada cero; no se escribe una fórmula que contenga $0a^{-1}$ en $a=0$.

La función potencia cero se define como uno también en el origen en esta convención. Su numerador incremental es cero y su derivada vale cero. La fórmula para potencias positivas se demuestra con exponentes no negativos. Escribir formalmente $0a^{-1}$ en el origen introduciría una expresión indefinida que no representa esa constante.

### Microcontrol 032

[]{#MA-MIC-ANM-01-018-032}

[]{#MA-MSOL-ANM-01-018-032}

**Pregunta.** ¿Cancelar $x/x$ añade cero al dominio original?

**Solución.** No. Vale uno y deriva a cero sólo en $\mathbb R\setminus\{0\}$. Incluir cero requiere una extensión distinta.

La cancelación es una igualdad válida sólo cuando el divisor no es cero. Allí la función original es constante y sus secantes valen cero. En cero no dispone de evaluación, que es una premisa de derivabilidad. Añadir un valor en el hueco define otro objeto cuyo comportamiento debe comprobarse como extensión.

## §18.5 — La cadena cuando el incremento interior se anula

### Microcontrol 033

[]{#MA-MIC-ANM-01-018-033}

[]{#MA-MSOL-ANM-01-018-033}

[]{#MA-SEC-ANM-01-018-005}

**Pregunta.** ¿Qué división falla si $g(x)=g(a)$?

**Solución.** La división por $g(x)-g(a)$ en la factorización habitual de secantes; el cociente de la composición sí está definido si $x\ne a$.

Puede ocurrir que $x\ne a$ pero la función interior repita su salida central. El cociente compuesto sigue teniendo denominador $x-a\ne0$, mientras la secante exterior escrita con $g(x)-g(a)$ no está definida. La prueba debe incluir esas entradas. Rellenar el factor exterior en su centro evita excluirlas silenciosamente.

### Microcontrol 034

[]{#MA-MIC-ANM-01-018-034}

[]{#MA-MSOL-ANM-01-018-034}

**Pregunta.** ¿Qué valor se asigna al factor exterior $A$ en $b$?

**Solución.** $f\prime(b)$, como valor de una nueva función, sin efectuar la división exterior en el centro.

El factor exterior es una función nueva que coincide con las secantes fuera de $b$ y declara un valor en $b$. Ese valor es el límite ya demostrado de las secantes exteriores. No se afirma que el cociente original tuviera evaluación central. La nueva definición permite usar composición continua cuando la interior alcanza exactamente $b$.

### Microcontrol 035

[]{#MA-MIC-ANM-01-018-035}

[]{#MA-MSOL-ANM-01-018-035}

**Pregunta.** ¿Por qué $A$ es continua en $b$?

**Solución.** Fuera del centro sus valores convergen a $f\prime(b)$ por derivabilidad, y en el centro su diferencia respecto de ese valor es cero.

La derivada exterior controla todas las entradas perforadas de $E$ próximas a $b$. El valor añadido en el centro coincide con el destino de ese límite y tiene error cero. Ambos casos cumplen el mismo radio de continuidad relativa. Así $A$ transporta aproximaciones que pueden visitar el centro, no sólo las que lo evitan.

### Microcontrol 036

[]{#MA-MIC-ANM-01-018-036}

[]{#MA-MSOL-ANM-01-018-036}

**Pregunta.** ¿Qué identidad admite incremento interior cero?

**Solución.** $q_{f\circ g,a}(x)=A(g(x))q_{g,a}(x)$; ambos incrementos de salida son cero cuando $g(x)=b$.

Si $g(x)\ne b$, la identidad proviene de multiplicar secantes y cancelar un incremento no nulo. Si $g(x)=b$, el cociente compuesto y el interior valen cero, por lo que la igualdad también vale con $A(b)$ finito. Separar los casos acredita todas las entradas perforadas del dominio inicial. No se efectúa una división exterior en su centro.

### Microcontrol 037

[]{#MA-MIC-ANM-01-018-037}

[]{#MA-MSOL-ANM-01-018-037}

**Pregunta.** ¿Exige la cadena una derivada interior no nula?

**Solución.** No. El producto de límites sigue siendo válido si $g\prime(a)=0$.

La secante interior puede tender a cero y seguirá estando acotada cerca del centro porque su límite es finito. La secante exterior rellenada tiende a la derivada exterior por continuidad compuesta. El producto tiende entonces al producto de derivadas, que puede ser cero. No hay ninguna división por la derivada interior en esta regla.

### Microcontrol 038

[]{#MA-MIC-ANM-01-018-038}

[]{#MA-MSOL-ANM-01-018-038}

**Pregunta.** ¿Qué inclusión de tipos simplifica la composición?

**Solución.** $g:D\to E$ y $f:E\to\mathbb R$, de modo que toda imagen interior es entrada admisible exterior.

La inclusión de tipos asegura que cada evaluación intermedia pueda usarse como entrada de $f$. Así el dominio compuesto coincide con $D$ y su acumulación ya está declarada. Si sólo hay compatibilidad parcial, debe definirse la preimagen efectiva de $E$ y revisarla antes de aplicar la cadena. La proximidad numérica no sustituye pertenencia.

### Microcontrol 039

[]{#MA-MIC-ANM-01-018-039}

[]{#MA-MSOL-ANM-01-018-039}

**Pregunta.** ¿Qué condición adicional hay que verificar sobre un dominio efectivo $T$?

**Solución.** $a\in T\cap\operatorname{Acc}(T)$. La acumulación del dominio original y del exterior no la garantiza.

La función compuesta sólo se evalúa en las entradas que la interior envía al dominio exterior. Ese conjunto puede reducirse a un punto aislado aunque los dominios de ambos factores acumulen en sus respectivos centros. La definición de derivada debe aplicarse al dominio compuesto real. El ejemplo con cuadrado y semieje negativo muestra exactamente esa pérdida.

### Microcontrol 040

[]{#MA-MIC-ANM-01-018-040}

[]{#MA-MSOL-ANM-01-018-040}

**Pregunta.** ¿La imagen de una función interior constante acumula en su valor?

**Solución.** No, es un singleton. Aun así la cadena funciona si la función exterior es derivable en su propio dominio acumulante.

Las salidas de la interior pueden permanecer siempre en $b$ sin visitar otras entradas exteriores. La función $A$ está definida y es continua también en ese punto. La derivada exterior se ha establecido respecto de $E$, no de la imagen singleton de la interior. Así el cociente compuesto puede ser cero en todas las entradas perforadas y cumplir la cadena.

## §18.6 — Invertir la pendiente exige volver al punto

### Microcontrol 041

[]{#MA-MIC-ANM-01-018-041}

[]{#MA-MSOL-ANM-01-018-041}

[]{#MA-SEC-ANM-01-018-006}

**Pregunta.** ¿Qué hipótesis construye una inversa única sobre la imagen?

**Solución.** Inyectividad de $f$; cada $y\in f[D]$ tiene un único antecedente en $D$.

Pertenecer a la imagen asegura existencia de antecedente y la inyectividad asegura unicidad. De ambos datos se define $h:f[D]\to D$. No se garantiza continuidad de ese retorno sólo por construirlo. Esa propiedad adicional tiene una función propia en la prueba de derivabilidad inversa.

### Microcontrol 042

[]{#MA-MIC-ANM-01-018-042}

[]{#MA-MSOL-ANM-01-018-042}

**Pregunta.** ¿Qué asegura la acumulación de la imagen en $f(a)$?

**Solución.** Continuidad de $f$ en el centro, acumulación de $D$ e inyectividad para que un antecedente distinto produzca un valor distinto.

La continuidad lleva una entrada próxima a $a$ a una salida próxima a $b$. La acumulación proporciona una entrada distinta dentro del radio que responda al desafío de salida. La inyectividad hace que su salida también sea distinta de $b$. Así se obtiene un miembro perforado de la imagen en cada ventana sin seleccionar una sucesión.

### Microcontrol 043

[]{#MA-MIC-ANM-01-018-043}

[]{#MA-MSOL-ANM-01-018-043}

**Pregunta.** ¿Qué hipótesis aproxima $h(y)$ a $a$ cuando $y$ se acerca a $b$?

**Solución.** Continuidad de la inversa $h$ en $b$; no basta saber que la inversa existe.

El cociente inverso se escribe usando $x=h(y)$ y el límite original sólo controla entradas cercanas a $a$. La continuidad de $h$ convierte una ventana en salidas en esa cercanía de antecedentes. La existencia de la inversa sólo identifica $x$, no acredita que esté próximo. El ejemplo de la inversa que salta separa ambas obligaciones.

### Microcontrol 044

[]{#MA-MIC-ANM-01-018-044}

[]{#MA-MSOL-ANM-01-018-044}

**Pregunta.** ¿Para qué se exige $L\ne0$?

**Solución.** Para separar las pendientes originales de cero y controlar sus recíprocos mediante el margen $|L|/2$.

La tolerancia $|L|/2$ en el límite de secantes asegura $|q_f|>|L|/2>0$ cerca de $a$. Esto permite invertir y acotar el error del recíproco por el error original. Si $L=0$, no hay ese margen y la inversa puede tener cocientes sin límite real finito. La raíz en cero ejemplifica tal fallo.

### Microcontrol 045

[]{#MA-MIC-ANM-01-018-045}

[]{#MA-MSOL-ANM-01-018-045}

**Pregunta.** ¿Por qué $y\ne b$ implica $h(y)\ne a$?

**Solución.** Porque $h(y)=a$ daría $y=f(h(y))=f(a)=b$, contradicción.

La identidad $f(h(y))=y$ vale en todo el dominio de la inversa. Si el antecedente fuera $a$, obligaría a que la salida fuese $b$. Por contradicción, las entradas perforadas de la inversa se convierten en entradas perforadas para el cociente original. Esa evitación legitima la identidad de secantes recíprocas.

### Microcontrol 046

[]{#MA-MIC-ANM-01-018-046}

[]{#MA-MSOL-ANM-01-018-046}

**Pregunta.** ¿Cuál es la derivada de la raíz en $b>0$?

**Solución.** $1/(2\sqrt b)$, aplicando la inversa del cuadrado en $a=\sqrt b>0$.

Para $b>0$ su antecedente $a=\sqrt b$ es positivo y la pendiente del cuadrado $2a$ no es cero. La raíz es continua allí y la identidad de secantes recíprocas entrega $1/(2a)$. Sustituir $a$ por su expresión da la fórmula. El centro cero requiere otra pregunta porque allí falla la pendiente no nula.

### Microcontrol 047

[]{#MA-MIC-ANM-01-018-047}

[]{#MA-MSOL-ANM-01-018-047}

**Pregunta.** ¿Por qué no se deriva primero $f\circ h=\mathrm{id}$ para probar R6?

**Solución.** Eso aplicaría la cadena suponiendo ya la derivabilidad de $h$, precisamente lo que falta demostrar.

La regla de la cadena tiene como premisa derivabilidad de sus dos factores en los centros correspondientes. Aplicarla con $h$ antes de demostrar esa premisa sólo despeja un valor hipotético, sin acreditar existencia. La identidad directa de secantes sí puede establecer un límite sin presuponer derivabilidad inversa. Esa es la reparación del argumento circular.

### Microcontrol 048

[]{#MA-MIC-ANM-01-018-048}

[]{#MA-MSOL-ANM-01-018-048}

**Pregunta.** ¿Qué falla para la raíz en cero?

**Solución.** Su cociente relativo es $1/\sqrt y$, sin límite real finito. La pendiente del cuadrado que se invertiría vale cero.

La raíz sí es continua y tiene centro acumulante en su dominio no negativo. Pero sus secantes desde cero superan cualquier barrera al tomar entradas positivas suficientemente pequeñas. Un límite real finito implicaría acotación local de esas secantes, contradicción. La regla de inversa no se aplica con pendiente original cero.

## §18.7 — Una derivada es otra función

### Microcontrol 049

[]{#MA-MIC-ANM-01-018-049}

[]{#MA-MSOL-ANM-01-018-049}

[]{#MA-SEC-ANM-01-018-007}

**Pregunta.** ¿Cuál es el dominio de $f\prime$?

**Solución.** $\operatorname{Diff}(f)$: centros del dominio que son de acumulación y donde el límite de pendientes existe finito.

Cada valor de $f\prime$ se asigna después de comprobar pertenencia del centro, acumulación y límite real finito de su cociente. El conjunto de centros que cumplen esas condiciones es su dominio propio. Puede ser todo el dominio original, un subconjunto pequeño o incluso vacío. La función derivada no hereda automáticamente todas las entradas de $f$.

### Microcontrol 050

[]{#MA-MIC-ANM-01-018-050}

[]{#MA-MSOL-ANM-01-018-050}

**Pregunta.** ¿Puede preguntarse continuidad de $f\prime$ en un punto donde no está definida?

**Solución.** No. Puede preguntarse un límite si el punto acumula en su dominio, pero continuidad requiere un valor en el punto.

La continuidad puntual compara otras evaluaciones con un valor central existente. Si ese valor falta, la pregunta no satisface la definición. Un límite perforado puede formularse en un punto exterior que acumule en el dominio de la derivada. Distinguir ambas preguntas evita rellenar un valor sin una extensión declarada.

### Microcontrol 051

[]{#MA-MIC-ANM-01-018-051}

[]{#MA-MSOL-ANM-01-018-051}

**Pregunta.** ¿Qué impide solapamiento de los intervalos $I_n$?

**Solución.** La suma de semianchos vecinos $5c_n^2/32$ es menor que la distancia entre centros $c_n/2$; los intervalos ordenados quedan separados.

Cada centro siguiente vale la mitad del anterior y su semiancho la cuarta parte. La suma de los semianchos es menor que la distancia entre centros, dejando un hueco positivo entre vecinos. Ese orden de vecinos separa también intervalos no consecutivos. La comprobación utiliza las fórmulas para todo índice, no sólo los bultos dibujados.

### Microcontrol 052

[]{#MA-MIC-ANM-01-018-052}

[]{#MA-MSOL-ANM-01-018-052}

**Pregunta.** ¿Qué cota prueba $F\prime(0)=0$?

**Solución.** $0\le F(x)\le x^2/2$, por lo que el cociente centrado en cero tiene magnitud a lo sumo $|x|/2$.

La función vale cero en el centro y fuera de los intervalos, y dentro de ellos la barrera cuadrática controla todas sus salidas. Para $x\ne0$, dividir por $|x|$ da error de pendiente a lo sumo $|x|/2$. Un radio, por ejemplo $2\eta$, lo hace menor que $\eta$. La prueba en cero es directa y no usa un pegado infinito.

### Microcontrol 053

[]{#MA-MIC-ANM-01-018-053}

[]{#MA-MSOL-ANM-01-018-053}

**Pregunta.** ¿Por qué coinciden las derivadas en los extremos de cada bulto?

**Solución.** La rama interior se anula con orden al menos dos y da cociente tendente a cero; la rama exterior es cero.

En el extremo el valor de la rama interior también es cero. La cota cuadrática respecto de la distancia a ese extremo, dividida por el incremento no nulo, da una cantidad tendente a cero. Del lado exterior la función permanece cero. Así ambas partes cumplen el mismo límite de secantes, dentro de una vecindad que aísla ese bulto.

### Microcontrol 054

[]{#MA-MIC-ANM-01-018-054}

[]{#MA-MSOL-ANM-01-018-054}

**Pregunta.** ¿Qué puntos refutan continuidad de $F\prime$ en cero?

**Solución.** $x_n=c_n+w_n/2\to0$, con $F\prime(x_n)=-3/2$ para todo $n$, frente a $F\prime(0)=0$.

Los puntos elegidos están en el interior de sus propios bultos y tienden a cero porque centros y semianchos tienden a cero. La fórmula derivada interior produce el valor fijo menos tres medios en todos ellos. Su distancia a $F\prime(0)=0$ no baja de uno. La dirección directa de continuidad para esta ruta explícita refuta continuidad de la derivada.

### Microcontrol 055

[]{#MA-MIC-ANM-01-018-055}

[]{#MA-MSOL-ANM-01-018-055}

**Pregunta.** ¿Cómo se evita usar un pegado infinito sin justificación?

**Solución.** Fuera de cero sólo hay finitos intervalos en una vecindad; cero se trata directamente con la cota global del cociente.

En un punto positivo no nulo, la cola de intervalos acaba por quedar por debajo de una vecindad del punto. Sólo quedan finitos bultos que revisar allí y se puede usar su separación. En un punto negativo una vecindad no toca ninguno. En cero esas exclusiones no funcionan, por lo que se usa la cota global de secantes.

### Microcontrol 056

[]{#MA-MIC-ANM-01-018-056}

[]{#MA-MSOL-ANM-01-018-056}

**Pregunta.** ¿La figura con varios bultos prueba el caso infinito?

**Solución.** No. La prueba usa fórmulas y cotas para todo $n$; la imagen representa una muestra finita.

Una figura finita puede orientar sobre amplitudes y anchuras, pero no comprueba todos los índices de la cola. Las desigualdades simbólicas justifican separación, finitud local y aproximación a cero para la familia completa. La ruta de puntos con derivada fija también está definida para todos los naturales. Esa evidencia algebraica sostiene el caso infinito.

## §18.8 — Certificar una aproximación local

### Microcontrol 057

[]{#MA-MIC-ANM-01-018-057}

[]{#MA-MSOL-ANM-01-018-057}

[]{#MA-SEC-ANM-01-018-008}

**Pregunta.** ¿Qué dato convierte una recta local en certificado cuadrático?

**Solución.** Una cota demostrada $|r(a+h)|\le Bh^2$ en una vecindad especificada, adicional a la mera existencia de la derivada.

La derivada garantiza un error pequeño comparado con $|h|$, pero no una tasa específica más rápida. Para certificar una cota cuadrática hay que demostrar la desigualdad y nombrar la vecindad donde vale. Con esos datos se pueden calcular radios de error de valor y de pendiente. No se introduce Taylor como justificación de una cota aún no probada.

### Microcontrol 058

[]{#MA-MIC-ANM-01-018-058}

[]{#MA-MSOL-ANM-01-018-058}

**Pregunta.** ¿Cuánto vale el modelo de $\sqrt{1+h}$ en $h=1/100$?

**Solución.** $1+h/2=201/200$; el error absoluto está acotado por $1/20000$.

El modelo afín tiene valor central uno y pendiente media. Al sustituir el incremento $1/100$ se obtiene exactamente $1+1/200=201/200$. La cota cuadrática con constante media da $h^2/2=1/20000$. Se trata de un certificado de error absoluto para una entrada dentro de la vecindad declarada.

### Microcontrol 059

[]{#MA-MIC-ANM-01-018-059}

[]{#MA-MSOL-ANM-01-018-059}

**Pregunta.** ¿En qué lado del valor exacto queda ese modelo de raíz?

**Solución.** Por encima: el resto exacto es $-h^2/[2(\sqrt{1+h}+1)^2]\le0$.

El denominador de la identidad es positivo y el numerador negativo o cero. Por ello el valor exacto menos el modelo es no positivo. El modelo sobreestima la raíz y coincide con ella cuando $h=0$. Este signo se obtiene por racionalización, sin usar concavidad ni un teorema posterior.

### Microcontrol 060

[]{#MA-MIC-ANM-01-018-060}

[]{#MA-MSOL-ANM-01-018-060}

**Pregunta.** ¿Qué diferencia hay entre error de valor y error de pendiente secante?

**Solución.** El segundo es el resto dividido por $h\ne0$; con cota $Bh^2$, sus magnitudes son a lo sumo $Bh^2$ y $B|h|$, respectivamente.

El error de valor es la diferencia entre evaluación exacta y modelo afín. El error de secante divide esa diferencia por el incremento perforado. En magnitudes, la cota cuadrática se transforma en una lineal al dividir por $|h|$. En el centro el error de valor es cero, pero no se define una secante allí.

### Microcontrol 061

[]{#MA-MIC-ANM-01-018-061}

[]{#MA-MSOL-ANM-01-018-061}

**Pregunta.** ¿La derivabilidad garantiza resto cuadrático?

**Solución.** No. $|x|\sqrt{|x|}$ tiene derivada cero en cero, pero el cociente de su resto por $x^2$ es $1/\sqrt{|x|}$ y no está acotado.

El cociente centrado tiene magnitud $\sqrt{|x|}$ y tiende a cero, acreditando derivada nula. La razón del resto respecto de $x^2$ crece sin cota, así ninguna constante cuadrática sirve en toda una ventana. La misma función cumple el modelo de primer orden y refuta esa tasa adicional. Esto precisa el alcance de la notación de resto pequeño.

### Microcontrol 062

[]{#MA-MIC-ANM-01-018-062}

[]{#MA-MSOL-ANM-01-018-062}

**Pregunta.** ¿Qué significa el producto vacío en $p_c$?

**Solución.** Uno. Si las únicas muestras son el centro, la construcción da simplemente $p_c(x)=cx$.

Cuando no hay nodos distintos de cero, no hay factores de anulación adicionales. La convención de producto vacío permite usar la misma fórmula y deja una función afín. Su valor en cero es cero y su cociente perforado es exactamente $c$. No se inventan divisores correspondientes a una lista vacía.

### Microcontrol 063

[]{#MA-MIC-ANM-01-018-063}

[]{#MA-MSOL-ANM-01-018-063}

**Pregunta.** ¿Qué derivada en cero tiene $p_c$ aunque sus muestras sean cero?

**Solución.** $c$, pues su cociente es $c$ por un producto finito de factores que tienden a uno.

Para cada nodo no nulo, el factor $(x-s)/(-s)$ tiende a uno al acercarse a cero. El producto es finito y su límite también es uno. Multiplicar por $c$ da el límite de la secante, mientras cada factor anula el polinomio en su nodo. Así una misma tabla finita de ceros permite cualquier pendiente prescrita.

### Microcontrol 064

[]{#MA-MIC-ANM-01-018-064}

[]{#MA-MSOL-ANM-01-018-064}

**Pregunta.** ¿Qué controla un certificado de derivada que no controla una tabla finita?

**Solución.** Todas las entradas admisibles dentro de un radio para cada tolerancia, no sólo los puntos muestreados.

Un certificado proporciona para cada precisión un radio que controla todas las secantes admitidas dentro de él. Una tabla sólo acredita valores en puntos particulares y puede omitir entradas mucho más próximas. Los polinomios construidos con pendientes arbitrarias mantienen la misma tabla. Por eso las muestras no determinan por sí solas una derivada.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Ejercicios](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca-microcontroles.html)
