---
content-id: MA-BCH-0260
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-014-SOLUCIONES
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
title: Soluciones — Capítulo 14
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C14_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html)

## 14.1. Una respuesta afín centrada

[]{#MA-EX-ANM-01-014-001}

[]{#MA-SOL-ANM-01-014-001}

[]{#MA-SEC-ANM-01-014-001}

Fijemos $a$ y $\varepsilon>0$. Tomamos $\delta=\varepsilon/3>0$. Para toda entrada con $|x-a|<\delta$, el error es $|(-3x+2)-(-3a+2)|=3|x-a|<\varepsilon$. Si $x=a$, esa identidad produce cero, así que no necesitamos excluir el centro. La arbitrariedad de $a$ prueba continuidad en toda la recta.

Al restar la salida central se cancela la constante dos y queda $-3(x-a)$. Su magnitud es tres veces la distancia de entrada, por lo que el radio responde directamente a la tolerancia. El caso $x=a$ satisface la misma identidad y tiene error cero. Como el centro fue arbitrario y pertenece al dominio real, la prueba acredita continuidad en todos los puntos, no sólo una aproximación alrededor de un centro elegido.

## 14.2. Reparar un único valor del cuadrado

[]{#MA-EX-ANM-01-014-002}

[]{#MA-SOL-ANM-01-014-002}

El límite perforado es $4$ por C13 y no cambia al modificar sólo el centro. Como $2$ acumula puntos de la recta, §14.1 implica continuidad exactamente cuando $c=4$. Para ese valor, un certificado directo es $\delta=\min(1,\varepsilon/5)$: $|x+2|<5$ para $|x-2|<1$, y el error $|x^2-4|<\varepsilon$ fuera del centro; en él es cero. La necesidad procede de la unicidad del límite, no de un dibujo.

**Retorno visual.** Véase [C14-F01](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Modificar el valor central no cambia las entradas perforadas, cuyo destino sigue siendo cuatro. Si la función fuera continua, ese destino tendría que coincidir con $c$, lo que demuestra necesidad. Para suficiencia comprobamos el radio indicado en las entradas no centrales y añadimos el caso central de error cero. Así la reparación válida es única y su prueba no depende de una impresión visual del hueco.

## 14.3. El límite existe y la continuidad falla

[]{#MA-EX-ANM-01-014-003}

[]{#MA-SOL-ANM-01-014-003}

Sea $f(x)=0$ para $x\ne0$ y $f(0)=2$. El límite perforado es cero, con error cero para todo desafío. Para continuidad, fijamos $\varepsilon_0=1$; dado $\delta>0$, $x=\delta/2$ es distinto de cero, está en la ventana y tiene error $|f(x)-f(0)|=2\ge1$. Así la función falla en cero pese a tener límite.

El control del límite perforado usa únicamente entradas no nulas, todas con salida cero. El control de continuidad compara esas mismas salidas con el valor dos del centro. Esta diferencia produce un error fijo que no se reduce al acercarse la entrada. La tolerancia uno se mantiene para todos los radios y los testigos $\delta/2$ verifican exactamente la negación de continuidad. El límite existe, pero no coincide con la evaluación central.

## 14.4. No intercambiar el punto y la respuesta

[]{#MA-EX-ANM-01-014-004}

[]{#MA-SOL-ANM-01-014-004}

El contrato demostrado es $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$. Mover $a$ detrás de $\exists\delta$ exige una respuesta común para todos los centros, una condición adicional. Para $x^2$, el cálculo local de §14.8 entrega $\delta(a,\varepsilon)=\min(1,\varepsilon/(1+2|a|))$, que depende de $a$. Esa fórmula muestra la dependencia de la prueba; por sí sola no demuestra imposibilidad de algún otro radio común. Tal cuestión se estudia en C17.

En continuidad puntual el radio puede adaptarse al centro. Exigirlo antes de escoger todos los centros simultáneamente es una afirmación más fuerte. El certificado del cuadrado ilustra la dependencia porque el multiplicador $x+a$ se controla mediante una constante que crece con $|a|$. Conviene respetar el alcance: mostrar que esta fórmula depende del centro no prueba que toda fórmula alternativa deba depender de él. Una refutación del radio común requeriría otro argumento.

## 14.5. Ventana completa, imagen y preimagen

[]{#MA-EX-ANM-01-014-005}

[]{#MA-SOL-ANM-01-014-005}

Para $\varepsilon$ y un radio $\delta$, todo $x\in D\cap B(a,\delta)$ cumple el error exactamente cuando $f(x)\in B(f(a),\varepsilon)$. Esto equivale a que toda imagen de esa bola esté en la bola de salida, por definición de imagen con testigo; también equivale a $x\in f^{-1}[B(f(a),\varepsilon)]$ para todas esas entradas. Cuantificar sobre cada $\varepsilon$ y algún $\delta$ da las tres formulaciones. La preimagen se define por pertenencia $f(x)\in V$, aunque $f$ sea constante o no inyectiva.

La bola relativa incluye el centro y sólo las entradas que pertenecen a $D$. Cada una cumple el error si y sólo si su salida pertenece a la bola centrada en $f(a)$. Pasar a la imagen reúne esas salidas; pasar a la preimagen selecciona esas entradas. Ambas reformulaciones mantienen los mismos cuantificadores. La preimagen es una operación de pertenencia y existe aunque diferentes entradas tengan la misma salida.

## 14.6. Un salto entre puntos sin vecinos

[]{#MA-EX-ANM-01-014-006}

[]{#MA-SOL-ANM-01-014-006}

[]{#MA-SEC-ANM-01-014-002}

En cero, radio $1/2$ confina la bola relativa al centro y da error cero para toda tolerancia. En un centro $a\in[1,2]$, tome $\delta=\min(1/2,\varepsilon)$; la entrada cero queda fuera y toda entrada pertinente pertenece al intervalo, donde el error es $|x-a|<\varepsilon$. No hay entradas entre cero y uno, así que continuidad relativa no exige conectar las dos piezas por un trazo.

**Retorno visual.** Véase [C14-F02](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

En cero no hay entradas del intervalo dentro del radio medio, así que el valor cien no necesita aproximarse a ellas. En un centro del intervalo, el mismo radio auxiliar excluye la entrada cero; las salidas de las entradas restantes obedecen a la identidad y su error es su distancia al centro. También vale en los extremos uno y dos porque la aproximación es relativa. La continuidad no exige añadir puntos ausentes entre las piezas del dominio.

## 14.7. Restringir puede eliminar la falla

[]{#MA-EX-ANM-01-014-007}

[]{#MA-SOL-ANM-01-014-007}

En el dominio real, para tolerancia $1$ y cualquier radio, $x=-\delta/2$ tiene error dos respecto de $s(0)=1$. En el dominio restringido, la función es constante uno y todo radio positivo da error cero. No contradice el teorema de restricción: éste preserva continuidad ya existente, pero no prohíbe que al retirar infractores aparezca continuidad.

La discontinuidad real usa entradas negativas que se acercan a cero, mientras su valor central es uno. Restringir al semieje no negativo elimina exactamente esos infractores y vuelve constante la función. El teorema de restricción afirma que no destruye continuidad existente; no afirma la recíproca. Una función puede adquirir continuidad al retirar rutas que provocaban el fallo en el dominio mayor.

## 14.8. Extender un cociente con hueco

[]{#MA-EX-ANM-01-014-008}

[]{#MA-SOL-ANM-01-014-008}

En $D$, la factorización da $f(x)=x+3$. Su límite en tres es seis, con radio $\varepsilon$ para el error $|x-3|$. La extensión única asigna $F(3)=6$, y entonces $F(x)=x+3$ en toda la recta. El error $|F(x)-F(a)|=|x-a|$ prueba continuidad en cada centro. La unicidad se sigue del teorema de extensión; cancelar no define por sí solo el cociente original en tres.

La igualdad con $x+3$ se prueba sólo donde $x-3\ne0$, que es el dominio original. El límite en el punto excluido se calcula con esas entradas y obliga al valor seis si queremos una extensión continua. Al asignarlo obtenemos la afín completa, cuya diferencia de salidas es $x-a$. Esto prueba continuidad en todos los puntos y no sólo en el hueco reparado. La cancelación algebraica no era una evaluación del cociente en tres.

## 14.9. Una modificación local debe incluir el centro

[]{#MA-EX-ANM-01-014-009}

[]{#MA-SOL-ANM-01-014-009}

La función cero y la función con valor uno sólo en cero coinciden fuera del centro; la primera es continua y la segunda falla por la ruta $\delta/2$ con error uno. Si $f=g$ en $D\cap B(a,r)$, el centro pertenece a esa región, así que $f(a)=g(a)$. Ante un radio de continuidad $\delta_f$, el mínimo con $r$ asegura igualdad de valores y errores para toda entrada cercana. Esto prueba la ida; intercambiar las funciones prueba la vuelta.

El primer ejemplo conserva todas las salidas perforadas y cambia únicamente el destino de comparación de continuidad. Por eso igualdad fuera del centro no alcanza. En la prueba positiva, la ventana completa contiene al propio centro y obliga a igualdad de valores centrales. El mínimo de radios asegura igualdad también en cada entrada controlada. Entonces las dos diferencias de salida son idénticas, y la continuidad puede transportarse en ambas direcciones.

## 14.10. Ningún valor repara un salto

[]{#MA-EX-ANM-01-014-010}

[]{#MA-SOL-ANM-01-014-010}

Las rutas $u_n=-1/(n+1)$ y $v_n=1/(n+1)$ tienen imágenes constantes $-2$ y $3$. Si una extensión con valor $c$ fuese continua en cero, la dirección secuencial directa obligaría ambas imágenes a converger a $c$; unicidad secuencial daría $c=-2=3$, contradicción. Las rutas explícitas no requieren selección numerable.

Las dos rutas pertenecen al dominio extendido cualquiera que sea el valor nuevo en cero y nunca evalúan ese centro. Las imágenes constantes obligarían, por continuidad, a tener como destino tanto menos dos como tres. La unicidad de límites secuenciales lo prohíbe. Ningún valor intermedio repara la incompatibilidad entre ramas. La existencia de fórmulas explícitas para las rutas evita una hipótesis de selección numerable.

## 14.11. La ruta vuelve al centro

[]{#MA-EX-ANM-01-014-011}

[]{#MA-SOL-ANM-01-014-011}

[]{#MA-SEC-ANM-01-014-003}

Los términos pares tienen distancia cero y los impares distancia $1/(n+1)$, que tiende a cero. Para $\delta>0$ escoja $N$ con $1/(n+1)<\delta$ si $n\ge N$; todo índice $k\ge2N$ tiene distancia menor que $\delta$, pues en el caso impar su subíndice es al menos $N$. Luego $x_k\to a$. Continuidad y el criterio directo dan $f(x_k)\to f(a)$, incluyendo los retornos centrales.

Para los términos impares, el índice global $2n+1$ y el índice de la fórmula $n$ no son el mismo. El corte $2N$ asegura que cualquier impar tardío tenga subíndice al menos $N$. Los pares ya están en el centro y cumplen cualquier precisión. Esta verificación prueba convergencia de toda la ruta intercalada. La continuidad transporta ambas clases de términos, incluidas las visitas al centro, hacia $f(a)$.

## 14.12. Ruta en un punto aislado

[]{#MA-EX-ANM-01-014-012}

[]{#MA-SOL-ANM-01-014-012}

Existe $r>0$ con $D\cap B(a,r)=\{a\}$. La convergencia da una cola con $|x_n-a|<r$; por pertenencia al dominio, cada término de esa cola es $a$. Las imágenes son entonces eventualmente constantes $f(a)$ y convergen a él por C06. No se necesita un límite perforado ni una hipótesis sobre $f$.

Una bola relativa aislante convierte proximidad suficiente en igualdad exacta. La convergencia coloca toda una cola dentro de ella, y la pertenencia de los términos a $D$ obliga a que sean el centro. Las salidas de esa cola son entonces constantes. La prueba no necesita continuidad como hipótesis de $f$: cualquier asignación sobre ese dominio transporta esas rutas porque éstas ya no tienen variación eventual.

## 14.13. El infractor evita solo el centro

[]{#MA-EX-ANM-01-014-013}

[]{#MA-SOL-ANM-01-014-013}

La negación es $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$ con $|x-a|<\delta$ y $|f(x)-f(a)|\ge\varepsilon_0$. Si $x=a$, el segundo error sería cero, contradicción. En el criterio de límite la exclusión del centro es una hipótesis explícita del dominio de control; aquí la propia infracción la implica automáticamente porque el destino es $f(a)$.

La negación invierte los cuantificadores y cambia el error estricto por un error mayor o igual que la tolerancia. Si un testigo fuera el centro, su error sería cero, contradiciendo la positividad de esa tolerancia. Así los infractores son automáticamente perforados, aunque la definición positiva de continuidad incluyera el centro. En C13 la perforación se escribía de entrada porque el destino del límite era independiente de la evaluación central.

## 14.14. Reconstruir la recíproca enumerada

[]{#MA-EX-ANM-01-014-014}

[]{#MA-SOL-ANM-01-014-014}

Si no hubiese continuidad, existen $\varepsilon_0$ y conjuntos $E_n$ no vacíos con $|x-a|<1/(n+1)$ y error al menos $\varepsilon_0$. Por sobreyectividad, $I_n=\{k:e(k)\in E_n\}$ es no vacío. El mínimo natural $k_n$ es único y define $x_n=e(k_n)$. Entonces $x_n\to a$ pero los errores de imagen nunca son menores que $\varepsilon_0$, contradicción. El mínimo vive en los índices; un subconjunto real no vacío puede carecer de mínimo.

Suponemos que falla continuidad y reunimos infractores con la misma tolerancia en escalas $1/(n+1)$. La enumeración hace no vacío el conjunto de índices que representan cada escala, y el menor índice define una elección única. La ruta elegida converge al centro por la cota de distancias, pero sus imágenes mantienen error grande. Esto contradice la conservación de todas las rutas. El mínimo pertenece a un subconjunto natural, no a los valores reales de los infractores.

## 14.15. Auditar una prueba sin selector

[]{#MA-EX-ANM-01-014-015}

[]{#MA-SOL-ANM-01-014-015}

El borrador pasa de existencias individuales a una función de selección sin justificarla. Puede repararse declarando una enumeración sobreyectiva de $D$ y usando mínimos de índices, o presentando el teorema general como condicional a $\mathrm{CC}(\mathbb R)$ aplicada a los $E_n$. La dirección de continuidad a rutas ya era incondicional y no necesita reparación. No afirmamos que el borrador demuestre la recíproca universal sin esa premisa.

La frase del borrador introduce una asignación simultánea de testigos, aunque sólo había acreditado existencias individuales. Una enumeración dada permite reparar ese paso mediante mínimos de índices. Para dominios arbitrarios, el capítulo declara elección numerable para subconjuntos reales y conserva la conclusión como condicional. Las estimaciones que siguen a la selección no cambian. La dirección directa ya toma una ruta dada y no requiere ese paso adicional.

## 14.16. Un abierto que contiene un extremo

[]{#MA-EX-ANM-01-014-016}

[]{#MA-SOL-ANM-01-014-016}

[]{#MA-SEC-ANM-01-014-004}

La preimagen es $[0,1)$. En el ambiente $[0,2]$ es la intersección con el abierto $(-1,1)$, luego es abierta relativa. Por bolas: para $a\in[0,1)$, radio $(1-a)/2$ mantiene cualquier entrada del dominio menor que uno. En la recta, toda bola de cero contiene negativos fuera del conjunto, así que no es abierta absoluta. La inclusión es continua con radio $\varepsilon$ y no contradice el criterio correcto.

El extremo cero se incluye porque pertenece al dominio y su salida está en el intervalo abierto solicitado. Para cada $a<1$ del conjunto, el radio $(1-a)/2$ mantiene las entradas del dominio por debajo de uno; las negativas quedan descartadas por el recorte. En la recta completa esas negativas demostrarían que ninguna bola alrededor de cero cabe en la preimagen. El mismo conjunto puede ser abierto relativo y no abierto absoluto sin contradicción.

## 14.17. La preimagen tiene dos piezas

[]{#MA-EX-ANM-01-014-017}

[]{#MA-SOL-ANM-01-014-017}

La condición $1<x^2<4$ equivale a $1<|x|<2$, por lo que la preimagen es $(-2,-1)\cup(1,2)$, unión de dos intervalos abiertos. Es abierta por C04. No existe una inversa funcional del cuadrado sobre toda la recta porque no es inyectivo; calcular esta preimagen sólo resuelve pertenencia a un intervalo de salida.

**Retorno visual.** Véase [C14-F03](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Resolver la condición de salida produce dos ramas de entradas: sus magnitudes deben estar estrictamente entre uno y dos. Las cuatro fronteras se excluyen porque sus cuadrados están en las fronteras excluidas de $(1,4)$. Cada rama es un intervalo abierto real y su unión también. La función cuadrado no tiene inversa en toda la recta, pero eso no impide calcular su preimagen mediante una condición sobre la salida de cada entrada.

## 14.18. Basta una base de intervalos

[]{#MA-EX-ANM-01-014-018}

[]{#MA-SOL-ANM-01-014-018}

Fijemos $a\in D$ y $\varepsilon>0$. El intervalo $(f(a)-\varepsilon,f(a)+\varepsilon)$ es una bola abierta y su preimagen abierta contiene $a$. El criterio por bolas da $\delta>0$ con $D\cap B(a,\delta)$ dentro de ella. Todas esas entradas tienen error menor que $\varepsilon$, que es continuidad. No es necesario seleccionar intervalos ni radios para todos los puntos a la vez.

No hace falta seleccionar una base completa de abiertos para probar cada precisión. Fijados centro y tolerancia, escogemos precisamente el intervalo centrado en su salida. La hipótesis garantiza que su preimagen es abierta relativa y contiene al centro. El criterio por bolas entrega entonces el radio de continuidad. El argumento reconstruye el control puntual directamente y vale para un centro arbitrario del dominio.

## 14.19. Ceros cerrados en el ambiente correcto

[]{#MA-EX-ANM-01-014-019}

[]{#MA-SOL-ANM-01-014-019}

El conjunto de ceros es todo $D=(0,1)$, cerrado relativo a sí mismo porque su complemento dentro de $D$ es vacío y abierto relativo. No es cerrado absoluto: cero es adherente y falta en él, por ejemplo mediante la ruta $1/(n+2)$. El criterio afirma cerradura en el dominio, no en otro ambiente.

Todo el dominio es cerrado respecto de sí mismo porque su complemento relativo es vacío. La preimagen de cero coincide con ese dominio. Pero en el ambiente real faltan puntos adherentes como cero y uno, de modo que no es cerrado absoluto. La continuidad no completa el dominio con sus puntos frontera. El criterio de preimágenes de cerrados conserva exactamente el ambiente en el que se ha declarado la función.

## 14.20. Codominio restringido y preimágenes

[]{#MA-EX-ANM-01-014-020}

[]{#MA-SOL-ANM-01-014-020}

Para $x\in D$, el tipo garantiza $f(x)\in E$, por lo que $f(x)\in E\cap U$ equivale a $f(x)\in U$. Esto prueba la igualdad. Si hay continuidad, el criterio absoluto da apertura de cada preimagen de $U$, por tanto de $V$. Recíprocamente, cada abierto absoluto $U$ tiene intersección $E\cap U$ abierta relativa y con la misma preimagen, así que el criterio absoluto vuelve a aplicar. Los ambientes cambian, las distancias reales no.

Aunque un abierto absoluto $U$ contenga salidas fuera de $E$, ninguna evaluación de $f$ puede producirlas. Por eso recortarlo a $E\cap U$ no cambia su selección de entradas. Esta igualdad permite expresar el criterio mediante abiertos relativos del codominio en lugar de abiertos de la recta. En la dirección inversa, cada abierto absoluto induce uno relativo con la misma preimagen, recuperando el criterio original.

## 14.21. Producto con un valor central nulo

[]{#MA-EX-ANM-01-014-021}

[]{#MA-SOL-ANM-01-014-021}

[]{#MA-SEC-ANM-01-014-005}

Continuidad de $g$ para tolerancia uno da $r>0$ con $|g(x)|<B:=|g(a)|+1$ en la bola relativa. Dado $\varepsilon>0$, continuidad de $f$ da $\delta_f$ con $|f(x)|<\varepsilon/B$. En radio $\min(r,\delta_f)$, $|f(x)g(x)-f(a)g(a)|=|f(x)g(x)|<\varepsilon$. La positividad de $B$ evita dividir por un valor central nulo.

El valor central del producto es cero, así que sólo necesitamos hacer pequeño $f(x)$ mientras mantenemos $g(x)$ acotado. La continuidad de $g$ entrega una barrera positiva $B$, aunque $g(a)$ también fuera cero. La continuidad de $f$ responde a la precisión $\varepsilon/B$. El mínimo de radios proporciona ambos controles y la triangular de producto da el error requerido. No se divide por ningún valor central que pueda anularse.

## 14.22. Cociente con dominio declarado

[]{#MA-EX-ANM-01-014-022}

[]{#MA-SOL-ANM-01-014-022}

El dominio es $\mathbb R\setminus\{2\}$. En cada punto de él, ambos polinomios son continuos y el denominador central es no nulo, por lo que el teorema de cocientes da continuidad relativa. En dos no hay evaluación de la expresión, así que no preguntamos por su continuidad como función dada. Un límite o una posible extensión sería una pregunta distinta; la regla de cocientes no la autoriza cuando el denominador límite es cero.

La expresión define una función sólo donde $x-2\ne0$. En cada centro de ese dominio el denominador central está definido y es no nulo, por lo que la regla de continuidad de cocientes se aplica. En dos la función dada no tiene evaluación; asignarle continuidad allí sin extenderla sería una pregunta mal formada. Investigar un límite o una extensión necesita un argumento propio y no una aplicación de la regla con denominador límite cero.

## 14.23. Composición que toca el centro

[]{#MA-EX-ANM-01-014-023}

[]{#MA-SOL-ANM-01-014-023}

La exterior $g(y)=|y|$ en cero responde al desafío $\varepsilon$ con $\eta=\varepsilon$, por el error $|y|$. La interior $f(x)=2x$ responde al desafío $\eta$ con $\delta=\eta/2$. Así $|x|<\delta$ implica $|2x|<\eta$ y $||2x|-0|<\varepsilon$. Si $x=0$, el error es cero y ambas etapas siguen siendo válidas.

**Retorno visual.** Véase [C14-F04](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Diseñamos primero la escala de la exterior y luego la de la interior. El valor absoluto transforma una entrada $y$ cercana a cero en una salida con error $|y|$; la multiplicación por dos hace el error intermedio $2|x|$. Así el radio final es $\varepsilon/2$. Si la interior alcanza el centro, la exterior lo evalúa con salida cero y cumple la misma estimación. Continuidad no pierde ese caso como un límite perforado exterior.

## 14.24. Composición sólo donde existe

[]{#MA-EX-ANM-01-014-024}

[]{#MA-SOL-ANM-01-014-024}

$T=\{x:x^2\ne1\}=\mathbb R\setminus\{-1,1\}$. La interior es continua en cada real y la exterior en cada punto de $E$ por recíproco de una afín no nula. En cada $a\in T$, $f(a)\in E$, así que el teorema de composición da continuidad relativa a $T$. La expresión resultante es $1/(x^2-1)$, sin evaluación en los dos puntos excluidos.

Las entradas uno y menos uno producen la salida intermedia prohibida uno. Excluirlas da el dominio efectivo $T$. Allí la función interior se restringe y su codominio puede declararse $E$ para componer de manera compatible. La exterior es continua en sus entradas admitidas, y la regla de composición prueba continuidad relativa a $T$. La fórmula final no define evaluaciones en los puntos retirados.

## 14.25. Composición por regiones de salida

[]{#MA-EX-ANM-01-014-025}

[]{#MA-SOL-ANM-01-014-025}

Para $V$ abierto absoluto, $g^{-1}[V]$ es abierto relativo a $E$. El criterio para $f:D\to E$ da que $f^{-1}[g^{-1}[V]]$ es abierto relativo a $D$. Un punto $x$ pertenece a ese conjunto si y sólo si $g(f(x))\in V$, así que coincide con $(g\circ f)^{-1}[V]$. El criterio de abiertos concluye continuidad en $D$. Ni inyectividad ni elección numerable son necesarias.

El conjunto seleccionado en la etapa intermedia es abierto relativo a $E$, no necesariamente abierto en toda la recta. El criterio de continuidad de $f$ con codominio relativo permite seleccionarlo y obtener un abierto relativo en $D$. La identidad de preimágenes identifica esa selección con la de la composición. La prueba conserva todos los ambientes y no utiliza imágenes de abiertos, cuya apertura no estaría garantizada.

## 14.26. Imagen cerrada que pierde la cerradura

[]{#MA-EX-ANM-01-014-026}

[]{#MA-SOL-ANM-01-014-026}

[]{#MA-SEC-ANM-01-014-006}

El denominador es un polinomio continuo y siempre positivo, de modo que el recíproco es continuo. Sus valores satisfacen $0<r(x)\le1$. Para cada $y\in(0,1]$, la entrada $\sqrt{1/y-1}$ produce $y$, luego la imagen es exactamente ese intervalo. Cero está fuera y toda bola suya contiene un punto del intervalo, por ejemplo $\min(\varepsilon/2,1/2)>0$ si el radio es $\varepsilon$. La imagen no es cerrada aunque el dominio real lo sea.

Para una salida $0<y\le1$, la cantidad $1/y-1$ es no negativa y su raíz proporciona una entrada real con la salida deseada. Esto prueba la inclusión que faltaba para la imagen exacta. Cero no se alcanza porque el denominador es positivo y finito en cada entrada. Sin embargo, cualquier bola alrededor de cero contiene alguna salida positiva del intervalo. Tener un punto adherente ausente refuta cerradura de la imagen.

## 14.27. Auditar la biyección y su inversa

[]{#MA-EX-ANM-01-014-027}

[]{#MA-SOL-ANM-01-014-027}

Las piezas $[0,1)$ y $[2,3]$ se envían afínmente a $[0,1)$ y $[1,2]$, disjuntas y con unión $[0,2]$. Cada regla es inyectiva, y las imágenes disjuntas prueban inyectividad global; la unión prueba sobreyectividad. Un radio $\min(1/2,\varepsilon)$ evita la otra pieza y controla error $|x-a|$. La inversa vale $y$ por debajo de uno y $y+1$ desde uno. Para cada radio, $y=1-\min(\delta/2,1/2)$ tiene distancia de entrada menor que $\delta$ pero distancia de salida a $h(1)=2$ mayor que uno.

**Retorno visual.** Véase [C14-F05](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La separación entre las piezas del dominio permite controlar cada centro usando sólo su regla afín local. En las salidas, las imágenes se unen sin esa separación: valores inferiores a uno pueden acercarse a uno desde la primera pieza, aunque uno proceda de la entrada dos de la segunda. La inversa debe saltar entre esas piezas. El infractor explícito demuestra que ninguna reducción del radio exterior elimina esta separación de entradas.

## 14.28. La identidad de un transporte reversible

[]{#MA-EX-ANM-01-014-028}

[]{#MA-SOL-ANM-01-014-028}

Escriba $h=f^{-1}:E\to D$. Para $U\subseteq D$, $y\in h^{-1}[U]$ equivale a que la entrada única $h(y)$ esté en $U$, lo que equivale a $y\in f[U]$. Por tanto $h^{-1}[U]=f[U]$. El criterio de continuidad de $h$ con abiertos relativos de su codominio $D$ es exactamente la propiedad de imágenes enunciada. Ambas implicaciones se siguen de esa igualdad y del criterio, sin asumir continuidad de $f$.

Una salida pertenece a $h^{-1}[U]$ cuando su entrada recuperada está en $U$. Como $f$ es biyectiva, eso equivale a que la salida haya sido producida desde $U$. Por tanto tomar preimagen bajo la inversa es tomar imagen bajo la función original. El criterio de abiertos convierte entonces continuidad inversa en apertura de $f$. La continuidad de $f$ no se necesita para probar esta equivalencia específica.

## 14.29. Una afín es un homeomorfismo

[]{#MA-EX-ANM-01-014-029}

[]{#MA-SOL-ANM-01-014-029}

Es inyectiva porque $m(x-z)=0$ implica $x=z$, y sobreyectiva porque para cada $y$ la entrada $(y-c)/m$ produce $y$. Su inversa es esa regla afín. El error directo es $|m||x-a|$, con radio $\varepsilon/|m|$. El inverso es $|y-b|/|m|$, con radio $|m|\varepsilon$. Las pruebas funcionan en cada centro y legitiman el transporte reversible.

La pendiente no nula permite despejar cada entrada de manera única y construir la inversa afín. La escala directa es $|m|$ y la inversa es su recíproco. Cada dirección tiene por ello su propio radio para la misma precisión: $\varepsilon/|m|$ al avanzar y $|m|\varepsilon$ al volver. Las constantes de traslación se cancelan al restar valores. Estas pruebas cuantitativas verifican todos los requisitos del homeomorfismo.

## 14.30. Controles inversos sin intervalos compactos

[]{#MA-EX-ANM-01-014-030}

[]{#MA-SOL-ANM-01-014-030}

Si $F\subseteq D$ es cerrado relativo, $D\setminus F$ es abierto relativo. La aplicación abierta da $f[D\setminus F]$ abierto relativo a $E$. Por bijectividad, $f[D\setminus F]=E\setminus f[F]$: una salida tiene única entrada y ésta está fuera de $F$ exactamente cuando la salida no está en $f[F]$. Por tanto $f[F]$ es cerrado relativo. La bijectividad es decisiva para la identidad de complementos de imágenes.

La apertura de la aplicación controla el complemento del cerrado relativo. La identidad de complementos de imágenes requiere biyectividad: cada salida debe tener una entrada y no puede tener entradas en ambas partes. De ahí que la imagen del complemento sea exactamente el complemento de la imagen. Como ese complemento es abierto relativo a $E$, la imagen del cerrado es cerrada allí. El argumento usa complementos y apertura, sin recurrir a compacidad.

## 14.31. Pegar un valor absoluto desplazado

[]{#MA-EX-ANM-01-014-031}

[]{#MA-SOL-ANM-01-014-031}

[]{#MA-SEC-ANM-01-014-007}

Las piezas $(-\infty,2]$ y $[2,\infty)$ son cerradas, cubren la recta y las reglas afines son continuas en ellas. Ambas dan cero en la intersección $\{2\}$, por lo que la función está bien definida. El pegado finito prueba continuidad global; coincide con $|x-2|$, pero no es necesario usar esa identidad para aplicar el mecanismo.

**Retorno visual.** Véase [C14-F06](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las dos reglas coinciden en el único punto donde ambas se aplican, lo que asegura una asignación única. Cada una es afín continua en su semieje relativo, y las dos piezas son cerradas y finitas. El teorema de pegado proporciona la continuidad del conjunto. La identidad con un valor absoluto puede confirmar la fórmula, pero la prueba pedida muestra cómo unir controles de piezas que llegan a la misma frontera.

## 14.32. Localizar con una cobertura abierta

[]{#MA-EX-ANM-01-014-032}

[]{#MA-SOL-ANM-01-014-032}

Fijamos $a\in D$ y $\varepsilon>0$. Alguna pieza abierta relativa $U$ contiene $a$. Hay $r>0$ con $D\cap B(a,r)\subseteq U$, y la continuidad de la restricción da $\delta_U$. El mínimo de ambos radios controla toda entrada del dominio: primero la coloca en $U$ y después limita el error. La prueba sólo necesita una pieza para el punto fijado, no un mínimo de una familia infinita.

Aunque haya infinitas piezas, para un centro fijado basta una pieza que lo contenga. Su apertura relativa garantiza que todas las entradas suficientemente próximas del dominio permanezcan dentro de ella. Después usamos la continuidad de su restricción y tomamos el mínimo de esos dos radios. Nunca reunimos radios de todas las piezas simultáneamente. Esto explica por qué no hace falta finitud en una cobertura abierta.

## 14.33. El acuerdo sin cierre no basta

[]{#MA-EX-ANM-01-014-033}

[]{#MA-SOL-ANM-01-014-033}

Use piezas $D_1=(-\infty,0)$ y $D_2=[0,\infty)$, con reglas constantes cero y uno. Son continuas en sus respectivos dominios y coinciden en la intersección vacía. La función global tiene valor uno en cero, pero $-\delta/2$ produce cero en cada radio; tolerancia $1/2$ refuta continuidad. $D_1$ no es cerrado relativo al dominio real, por lo que no puede excluirse cerca de un centro que no le pertenece.

El acuerdo en una intersección vacía se cumple automáticamente y asegura que no haya dos reglas incompatibles para una misma entrada. Pero no controla aproximaciones desde la pieza negativa al centro cero, que pertenece sólo a la otra pieza. Los testigos negativos mantienen error uno en cualquier ventana. La hipótesis ausente es la cerradura relativa necesaria para excluir localmente una pieza que no contiene al centro en el pegado finito.

## 14.34. Una cobertura cerrada infinita falla

[]{#MA-EX-ANM-01-014-034}

[]{#MA-SOL-ANM-01-014-034}

Cada singleton es cerrado en la recta: desde cualquier punto distinto, la mitad de la distancia evita el singleton. Por intersección también es cerrado relativo a $D$. Las piezas cubren $D$ y cada restricción es constante, por tanto continua. En cero, para cualquier radio $\delta>0$, arquimedianidad da un entero positivo $n>1/\delta$; entonces $1/n<\delta$ y el error es uno. La tolerancia $1/2$ refuta continuidad. La cobertura es infinita; los radios que excluyen cada pieza distinta de cero no tienen una escala común positiva.

Cada singleton ofrece una prueba trivial de continuidad de su restricción, porque sólo contiene una entrada. Sin embargo, las otras piezas se acercan arbitrariamente a la pieza cero y todas sus salidas valen uno. No existe un radio que las excluya simultáneamente, aunque cada una individualmente sea cerrada. El ejemplo localiza el papel de la finitud: el mínimo de infinitos radios de exclusión puede no ser positivo.

## 14.35. Conservar un signo cerca del centro

[]{#MA-EX-ANM-01-014-035}

[]{#MA-SOL-ANM-01-014-035}

Use tolerancia $|f(a)|/2=-f(a)/2>0$. En el radio de continuidad, $f(x)<f(a)+|f(a)|/2=f(a)/2<0$. Si $f$ es continua en todo $D$, el conjunto de valores negativos de entrada es $f^{-1}[(-\infty,0)]$ y es abierto relativo por el criterio. No se deduce existencia de un cero en otro lugar: sólo apertura y estabilidad local.

La mitad de la magnitud del valor negativo central es una tolerancia positiva. Controlar el error por ella mantiene la salida por debajo de la mitad de ese valor, que sigue siendo negativa. Si la función es continua en todo el dominio, las entradas de salida negativa forman la preimagen de un abierto y son abiertas relativas. La afirmación global sobre ese conjunto requiere esa continuidad global, además del dato puntual inicial.

## 14.36. Un certificado directo del cuadrado

[]{#MA-EX-ANM-01-014-036}

[]{#MA-SOL-ANM-01-014-036}

[]{#MA-SEC-ANM-01-014-008}

Para $|x-a|<1$, $|x+a|<1+2|a|=:K$. Por tanto $|x^2-a^2|\le K|x-a|$, donde la desigualdad no estricta incluye $x=a$. El radio $\delta=\min(1,\varepsilon/K)$ es positivo porque $K\ge1$. Si $|x-a|<\delta$, el error es $\le K|x-a|<K\delta\le\varepsilon$. No se escribió $0<0$ en el caso central.

Cuando $x=a$, el factor $|x-a|$ es cero. Por eso la cota del producto debe escribirse no estricta antes de usar la distancia estricta de entrada: $|x^2-a^2|\le K|x-a|<\varepsilon$. Así se incluye correctamente el centro. Para entradas diferentes, la factorización y el radio auxiliar acotan el factor variable. El mismo certificado demuestra continuidad para cualquier real $a$ sin excluir evaluaciones centrales.

## 14.37. La raíz en un extremo del dominio

[]{#MA-EX-ANM-01-014-037}

[]{#MA-SOL-ANM-01-014-037}

El valor central es cero. Dado $\varepsilon>0$, tomamos $\delta=\varepsilon^2$. Para $x\in[0,\infty)$ con $|x|<\delta$, no negatividad y orden de raíces dan $|\sqrt{x}-0|=\sqrt{x}<\varepsilon$. Los negativos no pertenecen al dominio real de la función y no son entradas del cuantificador universal. La prueba incluye cero, cuyo error es cero.

**Retorno visual.** Véase [C14-F07](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La función raíz real sólo está definida para entradas no negativas. Su continuidad en cero se prueba dentro de ese dominio, sin extenderla a negativos. El radio cuadrático convierte la condición $x<\varepsilon^2$ en $\sqrt{x}<\varepsilon$. El punto central está permitido y entrega cero. Ser un extremo del dominio no obstaculiza una prueba relativa con todas las entradas que la función realmente admite.

## 14.38. Continuidad sin barrera lineal

[]{#MA-EX-ANM-01-014-038}

[]{#MA-SOL-ANM-01-014-038}

Dados $K\ge0$ y $r>0$, sea $x=\min(r/2,1/[4(K+1)^2])>0$. Entonces $x<r$ y $1/\sqrt{x}\ge2(K+1)>K$. Multiplicar por $x>0$ da $\sqrt{x}>Kx$, infracción de la cota. Continuidad ya tiene certificado $\varepsilon^2$, que no necesita esa barrera lineal. La ausencia de un certificado suficiente no significa ausencia de continuidad.

La construcción del infractor depende de la barrera $K$ y del radio propuesto. El mínimo asegura una entrada positiva dentro de la ventana y una raíz suficientemente pequeña para que su recíproco supere $K$. La desigualdad resultante contradice la cota lineal. Esto no refuta continuidad, cuyo radio ya existe y depende cuadráticamente de la tolerancia. Refuta sólo una forma particular de certificado más fuerte.

## 14.39. Invertir el cuadrado lejos de cero

[]{#MA-EX-ANM-01-014-039}

[]{#MA-SOL-ANM-01-014-039}

Para $x,z\ge m$, $|x^2-z^2|=(x+z)|x-z|\ge2m|x-z|$. En particular igualdad de cuadrados implica igualdad de entradas. Cada $y\ge m^2$ tiene entrada $\sqrt{y}\ge m$, lo que prueba sobreyectividad. La inversa es la raíz restringida. Para un centro $b=q(a)$ y un desafío $\varepsilon$, $|y-b|<2m\varepsilon$ implica $|q^{-1}(y)-a|\le|y-b|/(2m)<\varepsilon$. El alcance global en $x,z$ evita entradas lejanas con salidas próximas.

En el semieje desde $m>0$, la suma de dos entradas es al menos $2m$. La factorización da así una cota inferior válida para cualquier par, además de inyectividad. Las raíces de las salidas del codominio están en el dominio y prueban sobreyectividad. La misma cota global permite que una salida cercana recupere una entrada cercana sin asumirlo previamente. El radio $2m\varepsilon$ proporciona el control inverso lineal.

## 14.40. El control inferior local no autoriza la inversa

[]{#MA-EX-ANM-01-014-040}

[]{#MA-SOL-ANM-01-014-040}

Use $D=[0,1)\cup[2,3]$, $f(x)=x$ en la primera pieza y $f(x)=x-1$ en la segunda, con $a=2$. El centro no es aislado, pues $2+t\in D$ para $0<t<1$ arbitrariamente pequeño. En radio $1/2$, todas las entradas del dominio son de la segunda pieza y $|f(x)-f(2)|=|x-2|$, así que vale la cota inferior. Pero la inversa en $f(2)=1$ toma valor dos, mientras $y_n=1-1/(n+2)$ tiende a uno y su inversa es $y_n$, que tiende a uno. No puede converger también a dos. La cota local exige antes saber que la entrada inversa está cerca de dos; precisamente eso era lo que se quería probar. Las salidas cercanas que proceden de la otra pieza quedan fuera de su alcance.

**Retorno visual.** Véase [C14-F05](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La cota local sólo habla de entradas de la segunda pieza próximas a dos. No controla las entradas de la primera pieza, que están lejos de dos pero producen salidas que se acercan a uno. Aplicarla a una entrada inversa exigiría demostrar antes que esa entrada ya está en la ventana local, que es precisamente la conclusión buscada. La ruta de salidas dada exhibe este fallo circular y refuta continuidad inversa manteniendo la biyección continua hacia delante.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html)
