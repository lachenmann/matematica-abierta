---
content-id: MA-BCH-0280
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-019-SOLUCIONES
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
title: Soluciones — Capítulo 19
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C19_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html)

## 19.1. Signos en un mínimo

[]{#MA-EX-ANM-01-019-001}

[]{#MA-SOL-ANM-01-019-001}

[]{#MA-SEC-ANM-01-019-001}

En un radio del mínimo, $f(x)-f(a)\ge0$; las secantes izquierdas son no positivas y las derechas no negativas. Interioridad da una bola dentro del dominio. Si $L>0$, la tolerancia $L/2$ fuerza pendientes positivas en algún radio: elegir $x=a-\min(r,\rho,\delta)/2$ contradice el signo izquierdo. Si $L<0$, tolerancia $|L|/2$ fuerza pendientes negativas y la entrada derecha con ese mismo mínimo contradice el signo derecho. Los radios son positivos y las entradas distintas del centro. Por tricotomía sólo queda $L=0$.

Los tres radios cumplen obligaciones distintas: mantener el extremo local, permanecer dentro del dominio y controlar el error de pendiente. Su mínimo positivo proporciona una entrada válida en el lado que contradice cada signo propuesto. Así se descartan ambas posibilidades no nulas sin usar valor medio ni seleccionar una sucesión.

## 19.2. El borde no es un centro interior

[]{#MA-EX-ANM-01-019-002}

[]{#MA-SOL-ANM-01-019-002}

El orden da mínimo global en cero y máximo global en uno. En cualquier centro acumulante del segmento el cociente perforado vale uno, también en los dos bordes, así sus derivadas relativas son uno. Cada bola centrada en cero contiene entradas negativas fuera del dominio y cada bola centrada en uno contiene entradas mayores que uno, por lo que ninguno es interior. Fermat no se aplica allí; su prueba necesita ambas clases de entradas admisibles, que faltan en los bordes.

**Retorno visual.** Véase [C19-F01](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Los extremos globales también son locales relativos, pero sus centros no contienen una bola real del dominio. La derivada relativa sigue estando definida porque cada borde acumula desde su lado disponible. El ejemplo no invalida Fermat: muestra por qué su hipótesis de ambas direcciones debe mantenerse.

## 19.3. Una esquina y un punto estacionario

[]{#MA-EX-ANM-01-019-003}

[]{#MA-SOL-ANM-01-019-003}

El valor absoluto tiene mínimo global cero, pero secantes de pendientes menos uno y uno, por lo que no es derivable allí. El cuadrado tiene mínimo global y cociente centrado en cero igual a $x$, así derivada cero. El cubo tiene cociente $x^2$ y derivada cero, pero entradas positivas y negativas arbitrariamente cercanas dan valores de signos opuestos: no hay extremo local. Por tanto un extremo interior no crea derivabilidad y una derivada nula no garantiza extremo.

Los tres objetos mantienen continuidad en cero, pero sus secantes y valores vecinos responden a preguntas distintas. La esquina no tiene derivada, el cuadrado tiene mínimo y pendiente nula, y el cubo sólo tiene pendiente nula. Estos casos separan necesidad de derivabilidad para aplicar Fermat y falta de suficiencia de su conclusión.

## 19.4. Dos lados sin un intervalo completo

[]{#MA-EX-ANM-01-019-004}

[]{#MA-SOL-ANM-01-019-004}

Sea $L$ la derivada relativa. Para un mínimo, las pendientes de la izquierda son no positivas y las de la derecha no negativas dentro del radio del extremo. Si $L>0$, el radio de error $L/2$ obliga a pendientes positivas; acumulación izquierda entrega una entrada dentro del mínimo de ambos radios, contradicción. Si $L<0$, acumulación derecha y error $|L|/2$ dan la contradicción opuesta. No hace falta una bola completa del dominio, sino entradas de ambos lados en todo radio. Para máximo se aplica el resultado a $-f$. No se infiere esa acumulación sólo de que el centro sea de acumulación por uno de los lados.

Para excluir el signo positivo basta un testigo izquierdo en cada ventana, y para excluir el negativo basta uno derecho. Esa disponibilidad es más débil que contener una bola real completa. La derivada relativa debe controlar también esas entradas y el extremo aportar sus signos. Acumulación de un único lado no alcanza para las dos contradicciones.

## 19.5. Transformar el máximo

[]{#MA-EX-ANM-01-019-005}

[]{#MA-SOL-ANM-01-019-005}

Si $f$ alcanza un máximo local en $a$, la función $g=-f$ sobre el mismo dominio alcanza un mínimo local con el mismo radio. El centro sigue siendo interior y C18 da derivabilidad $g\prime(a)=-f\prime(a)$. El caso mínimo implica $g\prime(a)=0$, así $f\prime(a)=0$. La transformación conserva tipos y dominio y sólo invierte el orden de valores; no se utiliza un resultado global o valor medio.

Multiplicar por menos uno convierte la comparación superior del máximo en la inferior del mínimo. No cambia qué entradas están disponibles ni el radio del extremo. La regla de derivación conserva el signo opuesto de la pendiente y permite volver a la igualdad cero para la función original.

## 19.6. Localizar un extremo interior

[]{#MA-EX-ANM-01-019-006}

[]{#MA-SOL-ANM-01-019-006}

[]{#MA-SEC-ANM-01-019-002}

C16 entrega un máximo y un mínimo alcanzados en el segmento. Si el valor distinto es mayor que $k$, el máximo tiene valor al menos tan grande y por tanto mayor que ambos bordes; su punto no puede ser ninguno de ellos y queda en $(a,b)$. Si es menor que $k$, el mínimo queda estrictamente por debajo de ambos bordes y también es interior. Tricotomía cubre los dos casos. No se afirma que ambos extremos globales tengan esa posición ni que la función sea derivable, pues este paso sólo localiza un extremo desde continuidad.

La continuidad y compacidad se usan para alcanzar el extremo, mientras el valor distinto de los bordes se usa para ubicarlo dentro. En este paso no se necesita todavía derivabilidad. Rolle la añadirá sólo cuando aplique Fermat al extremo interior ya localizado. Separar las dos tareas evita atribuir a continuidad una conclusión sobre pendientes.

## 19.7. Una parábola que vuelve al borde

[]{#MA-EX-ANM-01-019-007}

[]{#MA-SOL-ANM-01-019-007}

El polinomio es continuo y derivable, con bordes cero. C18 da $f\prime(x)=1-2x$, que sólo se anula en $c=1/2$, interior al segmento. Su valor es $1/4$, no cero. Rolle predice existencia de un cero de la derivada entre los dos ceros de la función y en este ejemplo es único por la ecuación explícita; no predice un tercer cero de la función.

**Retorno visual.** Véase [C19-F02](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Resolver $1-2c=0$ prueba unicidad del punto estacionario en este ejemplo concreto. Evaluar la función allí responde a otra pregunta y da un cuarto. Rolle no asegura que el testigo tenga la misma altura que los bordes ni que siempre sea único. Ambas conclusiones aquí se investigan por la fórmula explícita.

## 19.8. Perder continuidad en un borde

[]{#MA-EX-ANM-01-019-008}

[]{#MA-SOL-ANM-01-019-008}

Los bordes valen cero. Cada punto interior tiene una vecindad donde $u$ es identidad, por lo que su derivada es uno y nunca cero. En uno, las entradas $1-1/(n+2)$ tienen salidas tendentes a uno, distintas del valor cero; no hay continuidad relativa. Se cumplen derivabilidad interior e igualdad de borde, pero falla precisamente continuidad del segmento cerrado. La hipótesis interior por sí sola no garantiza los extremos alcanzados necesarios para la prueba de Rolle.

La restricción interior coincide localmente con la identidad y sus pendientes permanecen en uno. El valor asignado al borde derecho hace coincidir los bordes, pero rompe continuidad relativa allí. Es una sola premisa ausente y la conclusión falla. La auditoría debe revisar todo el segmento cerrado antes de aplicar Rolle.

## 19.9. Omitir la derivabilidad

[]{#MA-EX-ANM-01-019-009}

[]{#MA-SOL-ANM-01-019-009}

La función de valor absoluto trasladada es continua y tiene valores $1/2$ en ambos bordes. A la izquierda de un medio su derivada es menos uno y a la derecha uno; en un medio no existe. Así no hay ninguna derivada interior nula y falla derivabilidad en todo el interior. Para la identidad, continuidad y derivabilidad se cumplen pero los bordes cero y uno son diferentes y su derivada siempre vale uno. Los ejemplos eliminan una sola hipótesis cada vez y muestran que no puede omitirse del enunciado universal.

La esquina interior conserva continuidad e igualdad de bordes, pero elimina la derivada exactamente en el centro que sería candidato. La identidad conserva continuidad y derivabilidad, pero pierde igualdad de bordes. Cada ejemplo conserva las demás premisas y muestra por qué la omitida es necesaria para la garantía universal.

## 19.10. Muchos puntos posibles

[]{#MA-EX-ANM-01-019-010}

[]{#MA-SOL-ANM-01-019-010}

En una constante sobre un segmento no degenerado todas las pendientes interiores son cero, por lo que cualquier punto interior sirve. La conclusión existencial no designa uno de ellos; su uso fija una función y un segmento y toma un testigo para esa instancia. Para $a=b$, el interior es vacío y no podría existir tal punto, aunque la igualdad de borde sea automática. Por eso se exige $a<b$. Ninguna de estas conclusiones construye un selector para una familia infinita de intervalos.

En un segmento no degenerado una constante tiene muchos testigos interiores. La afirmación existencial permite utilizar alguno en una aplicación, sin identificar una regla preferida global. En un singleton no hay interior y la conclusión de existencia es imposible. Eso justifica la desigualdad estricta de los extremos en el enunciado.

## 19.11. Construir el residuo de la secante

[]{#MA-EX-ANM-01-019-011}

[]{#MA-SOL-ANM-01-019-011}

[]{#MA-SEC-ANM-01-019-003}

Con $a<b$, $m=[f(b)-f(a)]/(b-a)$ es real. La recta $\ell(x)=f(a)+m(x-a)$ comparte los valores de borde y $H=f-\ell$ vive en $[a,b]$. Continuidad de $f$ y de la recta hace continua $H$ en todo el segmento; C18 da derivada $H\prime=f\prime-m$ en su interior. Ambos bordes de $H$ valen cero. Rolle entrega $c$ interior con $H\prime(c)=0$, y la identidad de derivadas implica $f\prime(c)=m$. No se ha aplicado Rolle directamente a $f$, cuyos bordes pueden ser distintos.

La auxiliar conserva dominio, continuidad y derivabilidad mediante reglas ya probadas. La secante resta exactamente el incremento total y produce dos bordes iguales. Rolle se aplica sólo después de esas comprobaciones. Su conclusión se traduce por la identidad de derivadas, sin prescribir de antemano el centro obtenido.

## 19.12. Tangente paralela en el cuadrado

[]{#MA-EX-ANM-01-019-012}

[]{#MA-SOL-ANM-01-019-012}

La pendiente secante es $(9-1)/(3-1)=4$. La recta es $\ell(x)=1+4(x-1)=4x-3$. El residuo $H(x)=x^2-4x+3=(x-1)(x-3)$ tiene ambos bordes cero y derivada $2x-4$. Se anula sólo en $c=2$, interior al segmento; allí la derivada original vale cuatro. La igualdad de pendientes se verifica exactamente, sin localizar el punto leyendo una figura.

**Retorno visual.** Véase [C19-F03](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El cuadrado produce una secante de pendiente cuatro en ese segmento y la recta correspondiente pasa por ambos bordes. Su resto factorizado verifica las dos anulaciones y su derivada lineal localiza un único centro interior. El punto medio funciona por esa expresión particular, no por una condición general de Lagrange.

## 19.13. El punto medio no es universal

[]{#MA-EX-ANM-01-019-013}

[]{#MA-SOL-ANM-01-019-013}

El incremento de valores y el de entrada son uno, así la pendiente secante es uno. La derivada del cubo es $3c^2$; en un medio vale $3/4$, por lo que no cumple la igualdad. Resolver $3c^2=1$ y exigir $c\in(0,1)$ da $c=1/\sqrt3$. El punto medio funciona para el cuadrado por su fórmula específica, sin ser un dato del teorema. Lagrange asegura existencia interior, no una localización predeterminada.

El testigo de valor medio se identifica resolviendo una ecuación de pendientes y exigiendo pertenencia al interior. La raíz positiva cumple ambas obligaciones; medio no cumple la igualdad. Pasar de un ejemplo simétrico a una regla universal de ubicación omitiría la parte existencial del teorema.

## 19.14. Restringir sin llenar un hueco

[]{#MA-EX-ANM-01-019-014}

[]{#MA-SOL-ANM-01-019-014}

Hace falta $[u,v]\subseteq D$, continuidad en ese segmento y derivabilidad en su interior. La restricción conserva continuidad y, porque cada centro interior acumula en el segmento, también las derivadas originales. En $D=[0,1]\cup[2,3]$, tomar $u=1,v=2$ sólo da dos argumentos válidos y no una función definida en $(1,2)$. La función cero en la primera pieza y uno en la segunda tiene todas sus derivadas relativas cero, mientras la secante entre esos bordes tiene pendiente uno. Lagrange no se aplica: falta su dominio intervalar completo.

La inclusión de los extremos sólo acredita dos evaluaciones, no todas las entradas del segmento. La función por piezas tiene derivadas relativas cero, pero una secante entre sus piezas de pendiente uno. Ese contraste identifica el gasto de intervalaridad. Restringir conserva derivadas donde haya acumulación, pero no rellena un hueco ausente.

## 19.15. Igualdad sin continuidad de derivada

[]{#MA-EX-ANM-01-019-015}

[]{#MA-SOL-ANM-01-019-015}

C18 demuestra que F es derivable en toda la recta y por tanto continua en cada punto. Su restricción al segmento es continua, y las derivadas de los centros interiores se conservan. Así Lagrange entrega un punto donde la derivada coincide con la pendiente secante. La discontinuidad de $F'$ en cero no elimina ninguna hipótesis del teorema, porque sólo se exige existencia de las derivadas interiores. No se afirma que el punto de valor medio sea cero o que pueda identificarse por una muestra de bultos.

La derivabilidad global de los bultos aporta continuidad de la función y todas las derivadas interiores de cualquier segmento. Son exactamente las premisas de Lagrange. La discontinuidad de la nueva función derivada en cero no interviene en la prueba. No se deduce por ello una ubicación específica del testigo de valor medio.

## 19.16. Del signo a cada par

[]{#MA-EX-ANM-01-019-016}

[]{#MA-SOL-ANM-01-019-016}

[]{#MA-SEC-ANM-01-019-004}

Fijemos $x<y$ en $I$. Intervalaridad da $[x,y]\subseteq I$, continuidad se conserva en la restricción y cada centro de $(x,y)$ pertenece al interior de $I$. Lagrange entrega $c\in(x,y)$ con $f(y)-f(x)=f\prime(c)(y-x)$. Como $f\prime(c)\ge0$ y $y-x>0$, resulta $f(x)\le f(y)$. El par era arbitrario, así la función es no decreciente. El testigo se usa sólo para ese par; no se requiere continuidad de la derivada ni seleccionarlo simultáneamente para todas las parejas.

## 19.17. Crecimiento estricto con una derivada nula

[]{#MA-EX-ANM-01-019-017}

[]{#MA-SOL-ANM-01-019-017}

Para $x<y$, $y^3-x^3=(y-x)(x^2+xy+y^2)$. El segundo factor es $(x+y/2)^2+3y^2/4$, no negativo y sólo cero si $x=y=0$, incompatible con $x<y$. Por tanto la diferencia es estrictamente positiva y el cubo es estrictamente creciente. Su derivada es $3x^2$ y vale cero en el origen. El ejemplo refuta que crecimiento estricto exija derivada positiva en cada centro; la condición necesaria donde existe derivada es sólo no negatividad.

## 19.18. Derivadas iguales, valores fijados

[]{#MA-EX-ANM-01-019-018}

[]{#MA-SOL-ANM-01-019-018}

Sea $H=f-g$ en el mismo intervalo. Es continua y derivable interiormente, con $H\prime=0$. Para un par $x<y$, Lagrange da $H(y)-H(x)=H\prime(c)(y-x)=0$; los pares iguales son triviales y los inversos se intercambian. Así todas las salidas de $H$ son iguales. Si existe $a$ con $f(a)=g(a)$, esa salida común es $H(a)=0$ y $f=g$ en todo el dominio. El argumento usa sólo diferencias y valor medio, sin introducir integrales ni primitivas.

## 19.19. Constantes distintas en un dominio roto

[]{#MA-EX-ANM-01-019-019}

[]{#MA-SOL-ANM-01-019-019}

Definimos $f=0$ en $[0,1]$ y $f=1$ en $[2,3]$. Una bola relativa de radio $1/2$ alrededor de cualquier entrada sólo toca su propia pieza, y allí las secantes perforadas valen cero. Todas las entradas, incluidos los cuatro bordes, acumulan en el dominio al menos desde un lado; por ello sus derivadas relativas existen y son cero. Sin embargo, $f(0)=0\ne1=f(2)$. El segmento entre piezas falta y no se puede aplicar Lagrange a ese par. La conclusión de constancia requiere intervalo completo, no sólo derivadas relativas nulas.

**Retorno visual.** Véase [C19-F04](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.20. Signo de una derivada existente

[]{#MA-EX-ANM-01-019-020}

[]{#MA-SOL-ANM-01-019-020}

En un centro interior $a$, toda secante de una función no decreciente es no negativa. A la derecha, numerador y denominador son no negativos y el denominador es positivo; a la izquierda, ambos son no positivos y el denominador es negativo. Si el límite $L$ fuera negativo, la tolerancia $|L|/2$ forzaría secantes menores que $L/2<0$ en algún radio. Acumulación aporta una entrada perforada allí y contradice el signo establecido. Por tanto $L\ge0$. No se deduce existencia de derivada a partir de monotonía: esa existencia era una premisa.

## 19.21. Dos cotas de incrementos

[]{#MA-EX-ANM-01-019-021}

[]{#MA-SOL-ANM-01-019-021}

[]{#MA-SEC-ANM-01-019-005}

Para $x<y$, Lagrange da $c\in(x,y)$ con $f(y)-f(x)=f\prime(c)(y-x)$. Sustituir $m\le f\prime(c)\le M$ y multiplicar por $y-x>0$ conserva el orden, obteniendo las dos cotas de incremento. Si $-L\le f\prime\le L$ con $L\ge0$, se concluye $|f(y)-f(x)|\le L(y-x)$. Para $y<x$ intercambiamos entradas y usamos simetría de magnitudes; para $x=y$ ambos lados son cero. Así la cota absoluta vale para todos los pares. Continuidad en bordes incluidos permite usar segmentos que los contengan.

## 19.22. Cubo y radio común

[]{#MA-EX-ANM-01-019-022}

[]{#MA-SOL-ANM-01-019-022}

El cubo es continuo en $[-2,2]$ y derivable en su interior. Allí $f\prime(t)=3t^2$ satisface $0\le f\prime(t)\le12$, porque $|t|\le2$. La cota de incrementos da $|y^3-x^3|\le12|y-x|$ para cualquier par del segmento. Para $\varepsilon>0$, el radio $\delta=\varepsilon/12$ convierte distancia estrictamente menor que él en error menor que $\varepsilon$. La constante controla toda la región antes de conocer el par. No se afirma esa barrera global en la recta no acotada.

**Retorno visual.** Véase [C19-F05](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.23. Una frontera rompe el certificado

[]{#MA-EX-ANM-01-019-023}

[]{#MA-SOL-ANM-01-019-023}

En cada centro interior la función $u$ coincide localmente con la identidad y $u\prime=1$. Supongamos una constante Lipschitz finita $L\ge0$ en todo $[0,1]$. Tomemos $x=(L+1)/(L+2)\in(0,1)$ y $y=1$. Como $u(y)=0$ y $u(x)=x$, tenemos $|u(y)-u(x)|=(L+1)/(L+2)>L/(L+2)=L|y-x|$, contradicción. La discontinuidad del borde invalida Lagrange en esos segmentos. Una cota interior de derivada no sustituye continuidad de la función en los bordes.

## 19.24. La raíz lejos de cero

[]{#MA-EX-ANM-01-019-024}

[]{#MA-SOL-ANM-01-019-024}

La raíz es continua en $[1/4,4]$ y tiene derivada $1/(2\sqrt t)$ en los centros interiores. Como $\sqrt t\ge1/2$, esa derivada tiene magnitud a lo sumo uno. Valor medio da $|\sqrt y-\sqrt x|\le|y-x|$, así sirve constante Lipschitz uno. En $[0,1]$, dado $L>0$, un $0<y<\min(1,1/(L+1)^2)$ cumple $\sqrt y/y=1/\sqrt y>L$, refutando la cota con el par $(0,y)$. Para $L=0$ también falla cualquier $y>0$. La raíz sigue siendo uniforme mediante el radio cuadrático de C17.

## 19.25. Una pendiente cercana en todos los centros

[]{#MA-EX-ANM-01-019-025}

[]{#MA-SOL-ANM-01-019-025}

En el segmento entre $a$ y $x$, definimos $H(t)=f(t)-f(a)-A(t-a)$. Es continua y derivable donde corresponde, con $|H\prime(t)|=|f\prime(t)-A|\le\eta$ en todo el interior. La cota de pares da $|H(x)-H(a)|\le\eta|x-a|$, y $H(a)=0$ produce el error solicitado. Si $x=a$, la igualdad de valor se verifica directamente. Saber sólo $f\prime(a)=A$ no acredita la premisa sobre las otras derivadas. El certificado utiliza ese control adicional y no Taylor.

## 19.26. Productos cruzados antes de cocientes

[]{#MA-EX-ANM-01-019-026}

[]{#MA-SOL-ANM-01-019-026}

[]{#MA-SEC-ANM-01-019-006}

Fijemos $\Delta f=f(b)-f(a)$ y $\Delta g=g(b)-g(a)$. La auxiliar $H(x)=\Delta g(f(x)-f(a))-\Delta f(g(x)-g(a))$ es continua en $[a,b]$ y derivable en $(a,b)$. Sus bordes son cero y su derivada es $H\prime=\Delta g\,f\prime-\Delta f\,g\prime$, pues los coeficientes están fijados. Rolle proporciona $c$ interior con $H\prime(c)=0$, equivalente a $\Delta f\,g\prime(c)=\Delta g\,f\prime(c)$. No se divide por incrementos ni derivadas, por lo que la identidad incluye sus posibles anulaciones.

## 19.27. Tres puntos diferentes

[]{#MA-EX-ANM-01-019-027}

[]{#MA-SOL-ANM-01-019-027}

Para $f=x^2$ y $g=x^3$ en $[0,1]$, ambos incrementos son uno. Lagrange para la primera resuelve $2c=1$ y da $c=1/2$; para la segunda resuelve $3c^2=1$ y da $c=1/\sqrt3$. Son distintos porque $1/4\ne1/3$. Cauchy exige $3c^2=2c$ y la interioridad excluye cero, dejando $c=2/3$. Allí las dos derivadas valen $4/3$. Dos existencias separadas no garantizaban un centro compartido; la auxiliar cruzada sí lo proporciona.

**Retorno visual.** Véase [C19-F06](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.28. Legitimar ambas divisiones

[]{#MA-EX-ANM-01-019-028}

[]{#MA-SOL-ANM-01-019-028}

Si $\Delta g=0$, la igualdad de bordes y las demás premisas permitirían aplicar Rolle a $g$, produciendo una derivada nula interior. Eso contradice $g\prime(t)\ne0$ para todo $t\in(a,b)$, así $\Delta g\ne0$. El testigo $c$ de Cauchy también cumple $g\prime(c)\ne0$. Ahora se divide la igualdad cruzada por $\Delta g\,g\prime(c)$ y se obtiene $f\prime(c)/g\prime(c)=\Delta f/\Delta g$. Las dos divisiones se justifican por separado: un incremento no nulo por sí solo no protege toda derivada.

## 19.29. Un incremento nulo

[]{#MA-EX-ANM-01-019-029}

[]{#MA-SOL-ANM-01-019-029}

Para $f(x)=x$ y $g(x)=x(1-x)$, se tiene $\Delta f=1$ y $\Delta g=0$. La igualdad cruzada exige $g\prime(c)=0$. Como $g\prime(c)=1-2c$, el único centro interior válido es $c=1/2$. Allí $f\prime(c)=1$ y $g\prime(c)=0$, de modo que los productos cruzados son ambos cero. Las razones por $\Delta g$ o por $g\prime(c)$ no están definidas. La forma general conserva una conclusión correcta que la división no puede expresar aquí.

## 19.30. Un testigo donde no se puede dividir

[]{#MA-EX-ANM-01-019-030}

[]{#MA-SOL-ANM-01-019-030}

Si $f=g=x^3$ en $[-1,1]$, ambos incrementos valen dos y ambas derivadas son $3c^2$. Por ello la igualdad cruzada se satisface en cualquier centro interior. En $c=0$, las dos derivadas valen cero y su razón sería $0/0$, indefinida, aunque $\Delta g=2\ne0$. Un centro interior no nulo sí permite dividir en este ejemplo, pero un testigo arbitrario no ofrece esa garantía. Para hacerlo se verifica su derivada concreta o se usa la premisa universal de no anulación.

## 19.31. Excluir los bordes de un mínimo

[]{#MA-EX-ANM-01-019-031}

[]{#MA-SOL-ANM-01-019-031}

[]{#MA-SEC-ANM-01-019-007}

El límite negativo de secantes en $u$ entrega $\delta_u>0$ con cocientes negativos. La entrada $t=u+\min(\delta_u,v-u)/2$ está dentro del segmento y cumple $H(t)<H(u)$. En $v$, el límite positivo entrega $\delta_v>0$; la entrada $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y secante positiva, así $H(s)<H(v)$. Derivabilidad implica continuidad y Weierstrass da un mínimo alcanzado en $[u,v]$. Ningún borde puede alcanzarlo, de modo que un minimizador $c$ es interior y también un mínimo local de la función original.

## 19.32. Una derivada intermedia sin suponer continuidad

[]{#MA-EX-ANM-01-019-032}

[]{#MA-SOL-ANM-01-019-032}

Sea $H(x)=f(x)-\lambda x$. Cuando $f\prime(u)<\lambda<f\prime(v)$, sus derivadas de borde cumplen $H\prime(u)<0<H\prime(v)$. El argumento anterior localiza un mínimo interior de $H$ en $[u,v]$; Fermat da $H\prime(c)=0$ y por ello $f\prime(c)=\lambda$. La continuidad usada es la de $H$, consecuencia de derivabilidad de $f$, sin suponer continuidad de $f\prime$. Si las derivadas están en orden opuesto, aplicamos el caso probado a $-f$ y $-\lambda$ y traducimos la igualdad al signo original.

## 19.33. Continuidad y ausencia de saltos

[]{#MA-EX-ANM-01-019-033}

[]{#MA-SOL-ANM-01-019-033}

La función de bultos es derivable en toda la recta, con $F\prime(0)=0$ y $F\prime(x_n)=-3/2$ para una ruta $x_n\to0$. Esta ruta refuta continuidad de $F\prime$ en cero. Sin embargo, Darboux se aplica entre cero y cada $x_n>0$: para cualquier $\lambda\in(-3/2,0)$ existe un centro estrictamente entre ambos con $F\prime=\lambda$. El testigo puede depender del nivel y del índice. Alcanzar esos valores intermedios no obliga a que las derivadas de la ruta converjan al valor central.

**Retorno visual.** Véase [C19-F07](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.34. Una derivada sin ceros tiene un signo

[]{#MA-EX-ANM-01-019-034}

[]{#MA-SOL-ANM-01-019-034}

Si hubiera una derivada positiva y otra negativa en el intervalo abierto, cero estaría estrictamente entre sus valores. Darboux produciría un centro intermedio de derivada cero, contradiciendo la premisa. Para el intervalo no vacío fijamos un centro y su signo no nulo; el opuesto queda excluido en todos los demás. Por las reglas de signo, la función es estrictamente creciente o decreciente según ese signo. No se obtiene automáticamente una separación uniforme de las magnitudes de la derivada respecto de cero.

## 19.35. Un escalón no puede ser una derivada

[]{#MA-EX-ANM-01-019-035}

[]{#MA-SOL-ANM-01-019-035}

Supongamos una función derivable en $(-1,1)$ con derivada $h$. En $u=-1/2$ su derivada sería menos uno y en $v=1/2$ sería uno. Darboux aplicado al nivel cero entregaría $c\in(-1/2,1/2)$ con derivada cero. Pero $h$ sólo toma menos uno y uno, contradicción. No se ha supuesto continuidad de $h$ ni se ha utilizado el gráfico de su salto; se infringe una propiedad necesaria de toda derivada en un intervalo.

## 19.36. Inyectividad desde Rolle

[]{#MA-EX-ANM-01-019-036}

[]{#MA-SOL-ANM-01-019-036}

[]{#MA-SEC-ANM-01-019-008}

Supongamos $f(x)=f(y)$ con $x<y$. Intervalaridad conserva todo $[x,y]$ en el dominio, continuidad se hereda y su interior dispone de derivadas. Rolle produce $c\in(x,y)$ con $f\prime(c)=0$, contradicción. Así entradas distintas no tienen la misma salida y la función es inyectiva. El valor repetido no necesitaba ser cero. La conclusión sólo garantiza a lo sumo una solución por nivel; existencia de una solución requiere otro dato.

## 19.37. Contar ceros por segmentos vecinos

[]{#MA-EX-ANM-01-019-037}

[]{#MA-SOL-ANM-01-019-037}

Si hubiera $k+2$ ceros distintos, ordenamos esa lista finita como $x_0<\cdots<x_{k+1}$. Cada segmento vecino cumple Rolle y entrega $c_j\in(x_j,x_{j+1})$ con $f\prime(c_j)=0$, para $j=0,\ldots,k$. Sus interiores son disjuntos, así los $k+1$ testigos son distintos y contradicen la cota $k$. Sólo se usan finitas aplicaciones, no una selección numerable de puntos. El recuento corresponde a raíces distintas y no a multiplicidades.

## 19.38. Existencia, unicidad y primera horquilla

[]{#MA-EX-ANM-01-019-038}

[]{#MA-SOL-ANM-01-019-038}

El polinomio $p=x^3+x-1$ es continuo, con $p(0)=-1$ y $p(1)=1$. Valor intermedio da una raíz interior. Su derivada $p\prime(x)=3x^2+1\ge1$ no se anula, así Rolle descarta dos raíces distintas y la raíz $r$ es única. Además $p(1/2)=-3/8<0$ y $p(3/4)=11/64>0$. Valor intermedio en ese subsegmento da una raíz en $(1/2,3/4)$, que por unicidad es $r$. Existencia y localización proceden de continuidad; Rolle aporta la parte de unicidad.

## 19.39. Un máximo de tres ceros que se alcanza

[]{#MA-EX-ANM-01-019-039}

[]{#MA-SOL-ANM-01-019-039}

Para $q=x^3-3x$, la derivada $q\prime=3x^2-3$ se anula exactamente en menos uno y uno. El recuento por Rolle limita a tres los ceros distintos de $q$. La factorización $q=x(x^2-3)$ muestra que $-\sqrt3,0,\sqrt3$ son esos tres ceros. La recíproca no vale: $Q=q+10$ en $[-2,2]$ conserva dos ceros interiores de derivada, pero $Q(-2)=8$, $Q(-1)=12$, $Q(1)=8$, $Q(2)=12$. Los signos de $Q\prime$ en las tres piezas y las reglas de orden aseguran $Q\ge8$ en todo ese dominio, sin ninguna raíz.

## 19.40. Residuo convertido en distancia

[]{#MA-EX-ANM-01-019-040}

[]{#MA-SOL-ANM-01-019-040}

La raíz $r$ y $x=2/3$ están en $(1/2,3/4)$. Sustituir da $p(x)=-1/27$; el crecimiento estricto y $p(r)=0$ implican $r>x$. En el segmento entre ambos, $1/4\le t^2\le9/16$, así $7/4\le p\prime(t)\le43/16$. La cota de incrementos entrega $(7/4)(r-x)\le1/27\le(43/16)(r-x)$. Dividir por las constantes positivas produce $16/1161\le r-x\le4/189$. Las barreras de derivada se probaron para todos los centros pertinentes, sin identificar el testigo de valor medio ni usar cifras de un gráfico.

**Retorno visual.** Véase [C19-F08](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html)
