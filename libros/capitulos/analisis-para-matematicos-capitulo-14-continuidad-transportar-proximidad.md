---
content-id: MA-BCH-0258
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-014
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
title: 'Capítulo 14 — Continuidad: transportar proximidad'
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C14.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-14)

La función que vale $x^2$ fuera de $1$ y toma el valor $4$ en $1$ tiene allí un límite perfectamente determinado. Sus salidas próximas tienden a $1$, mientras su valor central es $4$. La continuidad exige que ambas informaciones sean compatibles: al acercarnos a una entrada del dominio, las salidas deben aproximarse al valor que la función asigna precisamente a esa entrada.

Ese control se expresa mediante las bolas de C04 y las imágenes y preimágenes de C12. La comparación con los límites de C13 será válida en los puntos de acumulación; en los puntos aislados podremos estudiar continuidad directamente, porque su definición incluye el centro. El dominio determina en cada caso qué entradas participan de la aproximación.

## 14.1. Hacer del valor central el destino

[]{#MA-SEC-ANM-01-014-001}

Para comparar las salidas próximas con la evaluación central necesitamos que $a$ pertenezca al dominio. En C13 podíamos preguntar por un límite sin disponer de $f(a)$; al exigir continuidad, el destino queda fijado por ese valor y la ventana de entradas puede incluir también el propio centro.

En el ejemplo $h(x)=x^2$ para $x\ne1$, $h(1)=4$, cambiar sólo el valor central por $1$ deja intactas las salidas perforadas y elimina la incompatibilidad. La definición permite distinguir exactamente qué cambia entre las dos funciones.

**Definición.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$. Decimos que $f$ es continua en $a$, relativamente a $D$, si

$$
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:
\quad |x-a|<\delta\ \Longrightarrow\ |f(x)-f(a)|<\varepsilon.
$$

La pertenencia $a\in D$ autoriza evaluar $f(a)$. Para $x=a$, tanto la distancia de entrada como el error de salida son cero, de modo que esa entrada satisface cualquier tolerancia positiva. No se requiere que $a$ sea interior del dominio ni que sea punto de acumulación: sólo se controlan las entradas de $D$ que están en la bola. Decimos que $f$ es continua en $D$ cuando lo es en cada $a\in D$.

La afirmación global tiene el orden $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$. El centro y la tolerancia se fijan antes del radio, que puede depender de ambos. Una respuesta común para todos los centros sería una exigencia adicional, estudiada en C17. Que una fórmula concreta dependa de $a$ muestra cómo trabaja esa prueba, pero por sí solo no descarta que pudiera existir otra respuesta común.

La bola relativa $D\cap B(a,\delta)$ reúne todas las entradas que debemos controlar. La continuidad equivale a pedir

$$
f[D\cap B(a,\delta)]\subseteq B(f(a),\varepsilon)
$$

para cada $\varepsilon>0$ y algún $\delta>0$. Una salida de la imagen tiene una entrada testigo en la bola relativa, y la estimación la sitúa en $B(f(a),\varepsilon)$. Recíprocamente, aplicar la inclusión a $f(x)$ recupera el error para cualquier entrada de esa bola. Por C12 también equivale a $D\cap B(a,\delta)\subseteq f^{-1}[B(f(a),\varepsilon)]$. Esta preimagen se define por pertenencia de la salida y no requiere una inversa funcional.

![C14-F01. A la izquierda, h(1)=4 es incompatible con el límite 1; la banda centrada en el valor efectivo no captura las salidas próximas. A la derecha, asignar el valor 1 repara la continuidad. El punto lleno participa del contrato; el hueco sólo representa la regla sin su valor central.](../../assets/books/anm/C14/C14-F01.svg){#fig-anm-c14-f01 fig-alt="Dos cuadráticas: una con hueco en uno uno y valor lleno en uno cuatro, y otra con valor lleno en uno uno; bandas centradas en cada valor efectivo."}

**Proposición.** Si $a\in D\cap D'$, entonces $f$ es continua en $a$ si y sólo si $\lim_{x\to a,\ x\in D}f(x)=f(a)$.

Si $f$ es continua, su radio sigue controlando las entradas distintas de $a$, y la acumulación permite formular el límite perforado de C13. Para la vuelta, el radio del límite controla cada entrada no central y, si $x=a$, el error es cero. Los dos casos cubren la bola relativa completa con el mismo radio. La hipótesis de acumulación hace posible la comparación con el límite; la continuidad en sí sólo necesita la pertenencia al dominio.

Para $h$, el destino perforado $1$ difiere de $h(1)=4$ y la proposición descarta continuidad. También podemos exhibir infractores directamente. Fijemos la tolerancia $1$ y recibamos cualquier $\delta>0$. Con $t=\min(\delta/2,1/4)$ y $x=1+t$ tenemos $0<t<\delta$, $x\ne1$ y $h(x)=x^2\le(5/4)^2=25/16$. Por tanto $|h(x)-4|\ge39/16>1$. Toda ventana contiene una entrada que mantiene un error mayor que la tolerancia fija.

### Ejercicios de la sección 14.1

[]{#ejercicios-14}

#### Ejercicio 1. Una respuesta afín centrada

[]{#MA-EX-ANM-01-014-001}

Prueba desde la definición que $f(x)=-3x+2$ es continua en cada real $a$. Trata explícitamente el centro.

[]{#MA-SOL-ANM-01-014-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

Fijemos $a$ y $\varepsilon>0$. Tomamos $\delta=\varepsilon/3>0$. Para toda entrada con $|x-a|<\delta$, el error es $|(-3x+2)-(-3a+2)|=3|x-a|<\varepsilon$. Si $x=a$, esa identidad produce cero, así que no necesitamos excluir el centro. La arbitrariedad de $a$ prueba continuidad en toda la recta.

Al restar la salida central se cancela la constante dos y queda $-3(x-a)$. Su magnitud es tres veces la distancia de entrada, por lo que el radio responde directamente a la tolerancia. El caso $x=a$ satisface la misma identidad y tiene error cero. Como el centro fue arbitrario y pertenece al dominio real, la prueba acredita continuidad en todos los puntos, no sólo una aproximación alrededor de un centro elegido.

</details>

#### Ejercicio 2. Reparar un único valor del cuadrado

[]{#MA-EX-ANM-01-014-002}

Define $h_c(x)=x^2$ si $x\ne2$ y $h_c(2)=c$. Determina para qué $c$ es continua en $2$, y prueba el resultado.

[]{#MA-SOL-ANM-01-014-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

El límite perforado es $4$ por C13 y no cambia al modificar sólo el centro. Como $2$ acumula puntos de la recta, §14.1 implica continuidad exactamente cuando $c=4$. Para ese valor, un certificado directo es $\delta=\min(1,\varepsilon/5)$: $|x+2|<5$ para $|x-2|<1$, y el error $|x^2-4|<\varepsilon$ fuera del centro; en él es cero. La necesidad procede de la unicidad del límite, no de un dibujo.

**Retorno visual.** Véase [C14-F01](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Modificar el valor central no cambia las entradas perforadas, cuyo destino sigue siendo cuatro. Si la función fuera continua, ese destino tendría que coincidir con $c$, lo que demuestra necesidad. Para suficiencia comprobamos el radio indicado en las entradas no centrales y añadimos el caso central de error cero. Así la reparación válida es única y su prueba no depende de una impresión visual del hueco.

</details>

#### Ejercicio 3. El límite existe y la continuidad falla

[]{#MA-EX-ANM-01-014-003}

Construye una función con límite finito en cero que no sea continua allí. Da un infractor explícito para cada radio de continuidad.

[]{#MA-SOL-ANM-01-014-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Sea $f(x)=0$ para $x\ne0$ y $f(0)=2$. El límite perforado es cero, con error cero para todo desafío. Para continuidad, fijamos $\varepsilon_0=1$; dado $\delta>0$, $x=\delta/2$ es distinto de cero, está en la ventana y tiene error $|f(x)-f(0)|=2\ge1$. Así la función falla en cero pese a tener límite.

El control del límite perforado usa únicamente entradas no nulas, todas con salida cero. El control de continuidad compara esas mismas salidas con el valor dos del centro. Esta diferencia produce un error fijo que no se reduce al acercarse la entrada. La tolerancia uno se mantiene para todos los radios y los testigos $\delta/2$ verifican exactamente la negación de continuidad. El límite existe, pero no coincide con la evaluación central.

</details>

#### Ejercicio 4. No intercambiar el punto y la respuesta

[]{#MA-EX-ANM-01-014-004}

Explica por qué continuidad en todo $D$ no permite escribir sin más $\forall\varepsilon>0\ \exists\delta>0\ \forall a,x\in D$ para el mismo control. Identifica la dependencia permitida y un cálculo que la haga visible.

[]{#MA-SOL-ANM-01-014-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

El contrato demostrado es $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$. Mover $a$ detrás de $\exists\delta$ exige una respuesta común para todos los centros, una condición adicional. Para $x^2$, el cálculo local de §14.8 entrega $\delta(a,\varepsilon)=\min(1,\varepsilon/(1+2|a|))$, que depende de $a$. Esa fórmula muestra la dependencia de la prueba; por sí sola no demuestra imposibilidad de algún otro radio común. Tal cuestión se estudia en C17.

En continuidad puntual el radio puede adaptarse al centro. Exigirlo antes de escoger todos los centros simultáneamente es una afirmación más fuerte. El certificado del cuadrado ilustra la dependencia porque el multiplicador $x+a$ se controla mediante una constante que crece con $|a|$. Conviene respetar el alcance: mostrar que esta fórmula depende del centro no prueba que toda fórmula alternativa deba depender de él. Una refutación del radio común requeriría otro argumento.

</details>

#### Ejercicio 5. Ventana completa, imagen y preimagen

[]{#MA-EX-ANM-01-014-005}

Demuestra que el contrato puntual equivale tanto a la inclusión de imágenes de bolas relativas como a la inclusión de la bola relativa en una preimagen. Explica por qué ninguna necesita inversa funcional.

[]{#MA-SOL-ANM-01-014-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Para $\varepsilon$ y un radio $\delta$, todo $x\in D\cap B(a,\delta)$ cumple el error exactamente cuando $f(x)\in B(f(a),\varepsilon)$. Esto equivale a que toda imagen de esa bola esté en la bola de salida, por definición de imagen con testigo; también equivale a $x\in f^{-1}[B(f(a),\varepsilon)]$ para todas esas entradas. Cuantificar sobre cada $\varepsilon$ y algún $\delta$ da las tres formulaciones. La preimagen se define por pertenencia $f(x)\in V$, aunque $f$ sea constante o no inyectiva.

La bola relativa incluye el centro y sólo las entradas que pertenecen a $D$. Cada una cumple el error si y sólo si su salida pertenece a la bola centrada en $f(a)$. Pasar a la imagen reúne esas salidas; pasar a la preimagen selecciona esas entradas. Ambas reformulaciones mantienen los mismos cuantificadores. La preimagen es una operación de pertenencia y existe aunque diferentes entradas tengan la misma salida.

</details>

## 14.2. El dominio y la reparación de un hueco

[]{#MA-SEC-ANM-01-014-002}

Al incluir el centro, la definición también tiene contenido cuando no hay otras entradas próximas. Ese caso explica por qué la continuidad puede conservarse en dominios separados y por qué restringir entradas puede eliminar una discontinuidad.

Si $a\in D$ es aislado, existe $r>0$ con $D\cap B(a,r)=\{a\}$. Para cualquier $\varepsilon>0$ usamos $\delta=r$: la única entrada permitida es $a$ y produce error cero. Toda función es por ello continua en los puntos aislados de su dominio, cualquiera que sea su valor central y cualesquiera que sean sus valores en las otras entradas.

En $D=\{0\}\cup[1,2]$, definamos $f(0)=9$ y $f(x)=x$ en el intervalo. El radio $1/2$ aísla cero y prueba continuidad allí para todas las tolerancias. Para un centro $a\in[1,2]$, el radio $\delta=\min(1/2,\varepsilon)$ excluye la entrada cero, y las restantes satisfacen $|f(x)-f(a)|=|x-a|<\varepsilon$. La prueba vale también en los extremos uno y dos, pues el cuantificador sólo considera entradas del dominio.

![C14-F02. En D={0}∪\[1,2\], la bola de radio 1/2 alrededor de cero contiene sólo esa entrada del dominio. Su salida es el valor central 9 y el error es cero para cualquier desafío. La ausencia de entradas entre las piezas no es una discontinuidad relativa.](../../assets/books/anm/C14/C14-F02.svg){#fig-anm-c14-f02 fig-alt="Gráfico con punto aislado en cero nueve y segmento entre uno uno y dos dos; ampliación de una bola relativa con sólo el punto central."}

Los puntos ausentes entre cero y uno no imponen ninguna condición a la función. La separación de las dos piezas del gráfico es compatible con continuidad relativa: en cada centro se controlan todas las entradas suficientemente próximas que realmente existen. En cero la ventana perforada queda vacía y no recibe un límite bajo la convención de C13; la ventana completa contiene el centro y demuestra continuidad con error cero.

Si $A\subseteq D$, $a\in A$ y $f$ es continua en $a$ sobre $D$, el mismo radio prueba continuidad de $f|_A$. La restricción conserva el valor $f(a)$ y toda entrada de $A$ dentro del radio era ya una entrada controlada de $D$. No se exige $a\in A'$: retirar entradas puede convertir el centro en aislado sin invalidar la prueba.

Para transportar continuidad entre dos funciones $f,g:D\to\mathbb R$ localmente iguales, la coincidencia debe incluir el centro. Si $f=g$ en $D\cap B(a,r)$, con $a\in D$ y $r>0$, entonces $f(a)=g(a)$. El mínimo de $r$ y de un radio de continuidad de $f$ asegura, para toda entrada pertinente, $|g(x)-g(a)|=|f(x)-f(a)|<\varepsilon$. Intercambiar las funciones prueba la vuelta. La igualdad sólo perforada no daría igualdad de valores centrales, como muestran $h$ y el cuadrado.

**Teorema de extensión en un punto.** Sean $a\notin D$, $a\in D'$ y $f:D\to\mathbb R$ con límite $L$ en $a$. La función $F:D\cup\{a\}\to\mathbb R$ dada por $F|_D=f$ y $F(a)=L$ es continua en $a$. Además, es la única elección del nuevo valor que permite continuidad allí.

Dado $\varepsilon>0$, usamos un radio del límite de $f$. Las entradas originales de $D$ dentro de él cumplen $|F(x)-F(a)|=|f(x)-L|<\varepsilon$, y la entrada añadida $x=a$ tiene error cero. Queda probada continuidad en el nuevo punto. Si otra extensión $G$ fuera continua allí, la comparación de §14.1 le daría límite perforado $G(a)$ en $D\cup\{a\}$. Restringir ese control a $D$ prueba $f\to G(a)$; como $a\in D'$, la unicidad de C13 obliga a $G(a)=L$.

Si además $f$ es continua en todo $D$, la extensión conserva esa continuidad en cada punto anterior. Fijados $b\in D$ y una tolerancia, reunimos un radio de continuidad de $f$ con $|b-a|/2>0$. El nuevo punto $a$ queda fuera de esa bola, donde $F$ coincide con $f$ y hereda su estimación. Junto con la prueba en $a$, esto da continuidad en $D\cup\{a\}$. La hipótesis sobre los otros puntos se ha utilizado expresamente; completar el hueco no habría corregido fallos que ya existieran en ellos.

Para cambiar un valor ya asignado en un punto de acumulación $a$, aplicamos la extensión a $D\setminus\{a\}$. Un límite finito obliga al único valor de reparación. Si hay dos límites laterales distintos, la continuidad de una extensión forzaría que ambos coincidieran con su mismo valor central, lo que es imposible. Elegir un valor intermedio no modifica ninguno de los dos destinos.

### Ejercicios de la sección 14.2

#### Ejercicio 6. Un salto entre puntos sin vecinos

[]{#MA-EX-ANM-01-014-006}

En $D=\{0\}\cup[1,2]$, define $f(0)=100$ y $f(x)=x$ en el intervalo. Prueba continuidad en todo $D$ y explica por qué la separación del gráfico no la contradice.

[]{#MA-SOL-ANM-01-014-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

En cero, radio $1/2$ confina la bola relativa al centro y da error cero para toda tolerancia. En un centro $a\in[1,2]$, tome $\delta=\min(1/2,\varepsilon)$; la entrada cero queda fuera y toda entrada pertinente pertenece al intervalo, donde el error es $|x-a|<\varepsilon$. No hay entradas entre cero y uno, así que continuidad relativa no exige conectar las dos piezas por un trazo.

**Retorno visual.** Véase [C14-F02](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

En cero no hay entradas del intervalo dentro del radio medio, así que el valor cien no necesita aproximarse a ellas. En un centro del intervalo, el mismo radio auxiliar excluye la entrada cero; las salidas de las entradas restantes obedecen a la identidad y su error es su distancia al centro. También vale en los extremos uno y dos porque la aproximación es relativa. La continuidad no exige añadir puntos ausentes entre las piezas del dominio.

</details>

#### Ejercicio 7. Restringir puede eliminar la falla

[]{#MA-EX-ANM-01-014-007}

Sea $s(x)=-1$ para $x<0$ y $s(x)=1$ para $x\ge0$. Prueba que es discontinua en cero sobre $\mathbb R$ y que su restricción a $[0,\infty)$ es continua allí.

[]{#MA-SOL-ANM-01-014-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

En el dominio real, para tolerancia $1$ y cualquier radio, $x=-\delta/2$ tiene error dos respecto de $s(0)=1$. En el dominio restringido, la función es constante uno y todo radio positivo da error cero. No contradice el teorema de restricción: éste preserva continuidad ya existente, pero no prohíbe que al retirar infractores aparezca continuidad.

La discontinuidad real usa entradas negativas que se acercan a cero, mientras su valor central es uno. Restringir al semieje no negativo elimina exactamente esos infractores y vuelve constante la función. El teorema de restricción afirma que no destruye continuidad existente; no afirma la recíproca. Una función puede adquirir continuidad al retirar rutas que provocaban el fallo en el dominio mayor.

</details>

#### Ejercicio 8. Extender un cociente con hueco

[]{#MA-EX-ANM-01-014-008}

Para $f(x)=(x^2-9)/(x-3)$ en $D=\mathbb R\setminus\{3\}$, encuentra y prueba la única extensión continua a toda la recta.

[]{#MA-SOL-ANM-01-014-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

En $D$, la factorización da $f(x)=x+3$. Su límite en tres es seis, con radio $\varepsilon$ para el error $|x-3|$. La extensión única asigna $F(3)=6$, y entonces $F(x)=x+3$ en toda la recta. El error $|F(x)-F(a)|=|x-a|$ prueba continuidad en cada centro. La unicidad se sigue del teorema de extensión; cancelar no define por sí solo el cociente original en tres.

La igualdad con $x+3$ se prueba sólo donde $x-3\ne0$, que es el dominio original. El límite en el punto excluido se calcula con esas entradas y obliga al valor seis si queremos una extensión continua. Al asignarlo obtenemos la afín completa, cuya diferencia de salidas es $x-a$. Esto prueba continuidad en todos los puntos y no sólo en el hueco reparado. La cancelación algebraica no era una evaluación del cociente en tres.

</details>

#### Ejercicio 9. Una modificación local debe incluir el centro

[]{#MA-EX-ANM-01-014-009}

Da dos funciones que coincidan en toda ventana perforada de cero y tengan continuidad distinta allí. Después prueba que la coincidencia en una ventana completa sí preserva continuidad.

[]{#MA-SOL-ANM-01-014-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

La función cero y la función con valor uno sólo en cero coinciden fuera del centro; la primera es continua y la segunda falla por la ruta $\delta/2$ con error uno. Si $f=g$ en $D\cap B(a,r)$, el centro pertenece a esa región, así que $f(a)=g(a)$. Ante un radio de continuidad $\delta_f$, el mínimo con $r$ asegura igualdad de valores y errores para toda entrada cercana. Esto prueba la ida; intercambiar las funciones prueba la vuelta.

El primer ejemplo conserva todas las salidas perforadas y cambia únicamente el destino de comparación de continuidad. Por eso igualdad fuera del centro no alcanza. En la prueba positiva, la ventana completa contiene al propio centro y obliga a igualdad de valores centrales. El mínimo de radios asegura igualdad también en cada entrada controlada. Entonces las dos diferencias de salida son idénticas, y la continuidad puede transportarse en ambas direcciones.

</details>

#### Ejercicio 10. Ningún valor repara un salto

[]{#MA-EX-ANM-01-014-010}

Sea $f(x)=-2$ para $x<0$ y $f(x)=3$ para $x>0$, sin valor en cero. Prueba que ninguna elección de $f(0)$ produce una extensión continua.

[]{#MA-SOL-ANM-01-014-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Las rutas $u_n=-1/(n+1)$ y $v_n=1/(n+1)$ tienen imágenes constantes $-2$ y $3$. Si una extensión con valor $c$ fuese continua en cero, la dirección secuencial directa obligaría ambas imágenes a converger a $c$; unicidad secuencial daría $c=-2=3$, contradicción. Las rutas explícitas no requieren selección numerable.

Las dos rutas pertenecen al dominio extendido cualquiera que sea el valor nuevo en cero y nunca evalúan ese centro. Las imágenes constantes obligarían, por continuidad, a tener como destino tanto menos dos como tres. La unicidad de límites secuenciales lo prohíbe. Ningún valor intermedio repara la incompatibilidad entre ramas. La existencia de fórmulas explícitas para las rutas evita una hipótesis de selección numerable.

</details>

## 14.3. Transportar sucesiones que sí pueden tocar el centro

[]{#MA-SEC-ANM-01-014-003}

Una sucesión del dominio puede volver al centro infinitas veces, alternar entre él y otras entradas o permanecer allí. La continuidad debe transportar todas esas aproximaciones hacia $f(a)$, y cada visita al centro aporta un término de error cero.

**Proposición.** Si $f:D\to\mathbb R$ es continua en $a\in D$ y $x_n\in D$ con $x_n\to a$, entonces $f(x_n)\to f(a)$.

Fijemos la sucesión y $\varepsilon>0$. La continuidad entrega $\delta>0$ y la convergencia de las entradas entrega después $N$ con $|x_n-a|<\delta$ para todo $n\ge N$. Cada término de esa cola pertenece a $D$, por lo que $|f(x_n)-f(a)|<\varepsilon$. También se aplica cuando $x_n=a$. El orden $\varepsilon\to\delta\to N$ transforma un control de toda la bola relativa en un control eventual de la ruta dada, sin construir una nueva sucesión.

Si $a$ es aislado, tomamos un radio $r>0$ con $D\cap B(a,r)=\{a\}$. La convergencia de $x_n$ coloca toda una cola en esa bola y la pertenencia a $D$ obliga a $x_n=a$ en la cola completa. Sus imágenes son eventualmente constantes $f(a)$ para cualquier función del dominio. Esto explica también el transporte de sucesiones en un punto de continuidad automática.

Negar continuidad en $a$ equivale a encontrar $\varepsilon_0>0$ tal que para todo $\delta>0$ existe $x\in D$ con

$$
|x-a|<\delta,\qquad |f(x)-f(a)|\ge\varepsilon_0.
$$

La tolerancia positiva impide que un infractor sea el centro, donde el error es cero. Aunque la continuidad se formule en ventanas completas, sus fallos proporcionan entradas perforadas. Usando $\eta_n=1/(n+1)$, el fracaso equivale a que todos los conjuntos

$$
E_n=\{x\in D:|x-a|<\eta_n,\ |f(x)-f(a)|\ge\varepsilon_0\}
$$

sean no vacíos para la misma $\varepsilon_0>0$. La negación de continuidad da un testigo al usar cada $\eta_n$ como radio. Recíprocamente, dado un radio positivo cualquiera, C06 permite tomar una escala menor y usar un único infractor del conjunto correspondiente. Esa entrada refuta también el radio recibido. Este paso no requiere reunir simultáneamente testigos de todos los conjuntos.

**Teorema para un dominio enumerado.** Si está dada una sobreyección $e:\mathbb N\to D$, la continuidad en $a$ equivale a que toda ruta del dominio convergente a $a$ tenga imágenes convergentes a $f(a)$.

Para la vuelta, supongamos que falla continuidad y fijemos los conjuntos $E_n$. Por sobreyectividad, $I_n=\{k:e(k)\in E_n\}$ es un subconjunto no vacío de naturales. Su mínimo único $k_n=\min I_n$ define $x_n=e(k_n)$ sin tomar un mínimo entre valores reales, que podría no existir. Se cumple $|x_n-a|<1/(n+1)$ y por tanto $x_n\to a$, mientras $|f(x_n)-f(a)|\ge\varepsilon_0$ en todos los índices contradice la convergencia de sus imágenes. La dirección directa ya probada completa la equivalencia. No necesitamos que los índices crezcan estrictamente: la cota de distancias basta, aunque la ruta no sea una subsucesión de la enumeración.

Para un dominio real arbitrario, la misma equivalencia se demuestra **bajo $\mathrm{CC}(\mathbb R)$**, el principio de selección numerable definido en C13. Se aplica exactamente a la familia de los $E_n$ no vacíos para obtener $x_n\in E_n$; las cotas anteriores dan la contradicción. Conservamos este teorema como condicional. La ida y el caso de enumeración dada no necesitan esa premisa; tampoco la necesitan las otras caracterizaciones que demostraremos con bolas.

Una ruta explícita basta para refutar continuidad sin recurrir a la recíproca. En $h$ de §14.1, la fórmula $x_n=1+1/(n+1)$ define entradas no centrales que tienden a $1$. Sus imágenes tienden a $1$ por el límite del cuadrado de C13. Si $h$ fuera continua, la dirección directa obligaría a las mismas imágenes a tender a $h(1)=4$, contra la unicidad secuencial. Los términos ya están definidos por la fórmula, de modo que no se usa selección numerable.

La refutación utiliza una consecuencia necesaria de continuidad en una ruta concreta. En cambio, para probar continuidad mediante la recíproca hay que controlar todas las rutas del dominio convergentes al centro y mantener la hipótesis que autoriza construir una ruta infractora.

### Ejercicios de la sección 14.3

#### Ejercicio 11. La ruta vuelve al centro

[]{#MA-EX-ANM-01-014-011}

Si $f$ es continua en $a$, considera $x_{2n}=a$ y $x_{2n+1}=a+1/(n+1)$, suponiendo que todos los términos estén en $D$. Prueba convergencia de entradas e imágenes.

[]{#MA-SOL-ANM-01-014-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Los términos pares tienen distancia cero y los impares distancia $1/(n+1)$, que tiende a cero. Para $\delta>0$ escoja $N$ con $1/(n+1)<\delta$ si $n\ge N$; todo índice $k\ge2N$ tiene distancia menor que $\delta$, pues en el caso impar su subíndice es al menos $N$. Luego $x_k\to a$. Continuidad y el criterio directo dan $f(x_k)\to f(a)$, incluyendo los retornos centrales.

Para los términos impares, el índice global $2n+1$ y el índice de la fórmula $n$ no son el mismo. El corte $2N$ asegura que cualquier impar tardío tenga subíndice al menos $N$. Los pares ya están en el centro y cumplen cualquier precisión. Esta verificación prueba convergencia de toda la ruta intercalada. La continuidad transporta ambas clases de términos, incluidas las visitas al centro, hacia $f(a)$.

</details>

#### Ejercicio 12. Ruta en un punto aislado

[]{#MA-EX-ANM-01-014-012}

Demuestra que si $a$ es aislado en $D$ y $x_n\in D$, $x_n\to a$, entonces $x_n=a$ eventualmente. Deduce el transporte de imágenes para cualquier $f:D\to\mathbb R$.

[]{#MA-SOL-ANM-01-014-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

Existe $r>0$ con $D\cap B(a,r)=\{a\}$. La convergencia da una cola con $|x_n-a|<r$; por pertenencia al dominio, cada término de esa cola es $a$. Las imágenes son entonces eventualmente constantes $f(a)$ y convergen a él por C06. No se necesita un límite perforado ni una hipótesis sobre $f$.

Una bola relativa aislante convierte proximidad suficiente en igualdad exacta. La convergencia coloca toda una cola dentro de ella, y la pertenencia de los términos a $D$ obliga a que sean el centro. Las salidas de esa cola son entonces constantes. La prueba no necesita continuidad como hipótesis de $f$: cualquier asignación sobre ese dominio transporta esas rutas porque éstas ya no tienen variación eventual.

</details>

#### Ejercicio 13. El infractor evita solo el centro

[]{#MA-EX-ANM-01-014-013}

Niega el contrato de continuidad y demuestra que todos los puntos del conjunto infractor para tolerancia positiva son distintos de $a$. Compara con el criterio de límite de C13.

[]{#MA-SOL-ANM-01-014-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

La negación es $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$ con $|x-a|<\delta$ y $|f(x)-f(a)|\ge\varepsilon_0$. Si $x=a$, el segundo error sería cero, contradicción. En el criterio de límite la exclusión del centro es una hipótesis explícita del dominio de control; aquí la propia infracción la implica automáticamente porque el destino es $f(a)$.

La negación invierte los cuantificadores y cambia el error estricto por un error mayor o igual que la tolerancia. Si un testigo fuera el centro, su error sería cero, contradiciendo la positividad de esa tolerancia. Así los infractores son automáticamente perforados, aunque la definición positiva de continuidad incluyera el centro. En C13 la perforación se escribía de entrada porque el destino del límite era independiente de la evaluación central.

</details>

#### Ejercicio 14. Reconstruir la recíproca enumerada

[]{#MA-EX-ANM-01-014-014}

Con $e:\mathbb N\to D$ sobreyectiva dada, prueba que preservar todas las rutas convergentes a $a$ fuerza continuidad en $a$. Indica qué objeto tiene un mínimo.

[]{#MA-SOL-ANM-01-014-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Si no hubiese continuidad, existen $\varepsilon_0$ y conjuntos $E_n$ no vacíos con $|x-a|<1/(n+1)$ y error al menos $\varepsilon_0$. Por sobreyectividad, $I_n=\{k:e(k)\in E_n\}$ es no vacío. El mínimo natural $k_n$ es único y define $x_n=e(k_n)$. Entonces $x_n\to a$ pero los errores de imagen nunca son menores que $\varepsilon_0$, contradicción. El mínimo vive en los índices; un subconjunto real no vacío puede carecer de mínimo.

Suponemos que falla continuidad y reunimos infractores con la misma tolerancia en escalas $1/(n+1)$. La enumeración hace no vacío el conjunto de índices que representan cada escala, y el menor índice define una elección única. La ruta elegida converge al centro por la cota de distancias, pero sus imágenes mantienen error grande. Esto contradice la conservación de todas las rutas. El mínimo pertenece a un subconjunto natural, no a los valores reales de los infractores.

</details>

#### Ejercicio 15. Auditar una prueba sin selector

[]{#MA-EX-ANM-01-014-015}

Un borrador dice: «Como cada $E_n$ es no vacío, elegimos $x_n\in E_n$ para todos los índices; queda probada la equivalencia secuencial en cualquier dominio». Repara su alcance sin adoptar un axioma silencioso.

[]{#MA-SOL-ANM-01-014-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

El borrador pasa de existencias individuales a una función de selección sin justificarla. Puede repararse declarando una enumeración sobreyectiva de $D$ y usando mínimos de índices, o presentando el teorema general como condicional a $\mathrm{CC}(\mathbb R)$ aplicada a los $E_n$. La dirección de continuidad a rutas ya era incondicional y no necesita reparación. No afirmamos que el borrador demuestre la recíproca universal sin esa premisa.

La frase del borrador introduce una asignación simultánea de testigos, aunque sólo había acreditado existencias individuales. Una enumeración dada permite reparar ese paso mediante mínimos de índices. Para dominios arbitrarios, el capítulo declara elección numerable para subconjuntos reales y conserva la conclusión como condicional. Las estimaciones que siguen a la selección no cambian. La dirección directa ya toma una ruta dada y no requiere ese paso adicional.

</details>

## 14.4. Preimágenes: de controles locales a conjuntos abiertos

[]{#MA-SEC-ANM-01-014-004}

Las estimaciones puntuales también permiten reconocer continuidad mediante conjuntos completos de salidas. Si una región abierta contiene $f(a)$, contiene una bola alrededor de ese valor, y la continuidad obliga a que una bola relativa alrededor de $a$ produzca salidas en esa región. La preimagen deberá contener, junto a cada una de sus entradas, todas las entradas suficientemente próximas del dominio.

Para $A\subseteq D\subseteq\mathbb R$, decimos que $A$ es abierto relativo a $D$ si $A=D\cap U$ para algún abierto $U$ de la recta. Es cerrado relativo si $D\setminus A$ es abierto relativo. Así, $[0,1/2)$ es abierto en $D=[0,1]$ aunque no lo sea en la recta: es $D\cap(-1,1/2)$. Todo $D$ es abierto y cerrado relativo a sí mismo; también lo es el vacío.

**Lema del criterio por bolas.** $A$ es abierto relativo a $D$ si y sólo si para cada $a\in A$ hay $r>0$ con $D\cap B(a,r)\subseteq A$.

Si $A=D\cap U$ con $U$ abierto, cada $a\in A$ tiene una bola contenida en $U$, cuyo recorte por $D$ queda en $A$. Para probar la vuelta formamos $U$ como unión de todas las bolas $B(a,r)$ con $a\in A$, $r>0$ y $D\cap B(a,r)\subseteq A$. La unión es abierta por C04. Cada $a\in A$ pertenece a alguna bola válida, así que $A\subseteq D\cap U$; si $x\in D\cap U$, pertenece a una bola cuyo recorte está en $A$ y por tanto $x\in A$. Obtenemos $A=D\cap U$ mediante ambas inclusiones. Al reunir todas las bolas válidas evitamos elegir una simultáneamente para cada punto.

La representación de los cerrados relativos se obtiene tomando complementos en el ambiente correcto. Si $D\setminus A=D\cap U$ para un abierto real $U$, ponemos $F=\mathbb R\setminus U$, cerrado, y resulta $A=D\cap F$. Recíprocamente, de esa última representación se sigue $D\setminus A=D\cap(\mathbb R\setminus F)$, que es abierto relativo. Así $A$ es cerrado relativo exactamente cuando se puede escribir como el recorte de un cerrado real.

**Teorema.** Para $f:D\to\mathbb R$, son equivalentes:

1. $f$ es continua en cada punto de $D$.
2. Para todo abierto $V\subseteq\mathbb R$, $f^{-1}[V]$ es abierto relativo a $D$.

Supongamos continuidad y fijemos un abierto $V$. Para cualquier $a\in f^{-1}[V]$, la salida $f(a)$ está en $V$, y su apertura da $\varepsilon>0$ con $B(f(a),\varepsilon)\subseteq V$. El radio $\delta>0$ de continuidad sitúa las salidas de $D\cap B(a,\delta)$ dentro de esa bola, luego $D\cap B(a,\delta)\subseteq f^{-1}[V]$. El criterio por bolas demuestra que la preimagen es abierta relativa. Trabajamos con una entrada arbitraria y el radio que necesita su prueba; no escogemos simultáneamente una familia de radios.

Para la implicación inversa, fijemos $a\in D$ y $\varepsilon>0$. La bola $V=B(f(a),\varepsilon)$ es un abierto real y su preimagen contiene $a$. Por hipótesis es abierta relativa, de modo que el lema entrega $\delta>0$ con $D\cap B(a,\delta)\subseteq f^{-1}[V]$. Cada entrada de esa bola relativa satisface $|f(x)-f(a)|<\varepsilon$, que es continuidad en $a$. La arbitrariedad del centro da continuidad en todo $D$.

![C14-F03. Para x² y V=(1,4), la preimagen es (−2,−1)∪(1,2). Los extremos quedan excluidos. Cada entrada de la preimagen tiene una pequeña ventana aún dentro de ella; no hace falta que el cuadrado sea invertible para obtener este conjunto.](../../assets/books/anm/C14/C14-F03.svg){#fig-anm-c14-f03 fig-alt="Cuadrática con banda de salida entre uno y cuatro y dos franjas de entrada abiertas entre menos dos menos uno y entre uno dos."}

Para $f:D\to E$ con $E\subseteq\mathbb R$, podemos usar abiertos relativos a $E$. Si $V=E\cap U$ y $U$ es abierto real, la pertenencia $f(x)\in E$ implica que $f(x)\in V$ equivale a $f(x)\in U$. Por tanto $f^{-1}[V]=f^{-1}[U]$. Cada abierto relativo tiene esta forma y cada abierto real produce uno con la misma preimagen, lo que prueba la equivalencia de los dos criterios. Ajustar el codominio a un subconjunto real que contiene la imagen no cambia las distancias ni la continuidad, aunque la función tipada conserve su codominio declarado.

Para $F\subseteq\mathbb R$, la identidad $D\setminus f^{-1}[F]=f^{-1}[\mathbb R\setminus F]$ relaciona los complementos de entrada y salida: en ambos lados se seleccionan exactamente los $x\in D$ con $f(x)\notin F$. Si todas las preimágenes de abiertos son abiertas relativas, las preimágenes de cerrados tienen complemento abierto relativo y son cerradas relativas. La vuelta aplica el mismo argumento al complemento de cada abierto. Así obtenemos también una caracterización por preimágenes de cerrados.

Para una función continua en $D$, el conjunto de ceros $f^{-1}[\{0\}]$ es cerrado relativo y el conjunto de entradas positivas $\{x\in D:f(x)>0\}=f^{-1}[(0,\infty)]$ es abierto relativo. El ambiente sigue siendo $D$: si $f$ es la función cero en $(0,1)$, su conjunto de ceros es todo $(0,1)$, cerrado respecto de sí mismo pero no en la recta. La prueba por bolas y complementos no ha utilizado la recíproca secuencial condicional.

### Ejercicios de la sección 14.4

#### Ejercicio 16. Un abierto que contiene un extremo

[]{#MA-EX-ANM-01-014-016}

Para la inclusión $f:[0,2]\to\mathbb R$, $f(x)=x$, calcula la preimagen de $(-1,1)$ y explica con radios su apertura relativa y su falta de apertura absoluta.

[]{#MA-SOL-ANM-01-014-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

La preimagen es $[0,1)$. En el ambiente $[0,2]$ es la intersección con el abierto $(-1,1)$, luego es abierta relativa. Por bolas: para $a\in[0,1)$, radio $(1-a)/2$ mantiene cualquier entrada del dominio menor que uno. En la recta, toda bola de cero contiene negativos fuera del conjunto, así que no es abierta absoluta. La inclusión es continua con radio $\varepsilon$ y no contradice el criterio correcto.

El extremo cero se incluye porque pertenece al dominio y su salida está en el intervalo abierto solicitado. Para cada $a<1$ del conjunto, el radio $(1-a)/2$ mantiene las entradas del dominio por debajo de uno; las negativas quedan descartadas por el recorte. En la recta completa esas negativas demostrarían que ninguna bola alrededor de cero cabe en la preimagen. El mismo conjunto puede ser abierto relativo y no abierto absoluto sin contradicción.

</details>

#### Ejercicio 17. La preimagen tiene dos piezas

[]{#MA-EX-ANM-01-014-017}

Para $q:\mathbb R\to\mathbb R$, $q(x)=x^2$, calcula $q^{-1}[(1,4)]$ y prueba su apertura sin confundirla con una inversa del cuadrado.

[]{#MA-SOL-ANM-01-014-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

La condición $1<x^2<4$ equivale a $1<|x|<2$, por lo que la preimagen es $(-2,-1)\cup(1,2)$, unión de dos intervalos abiertos. Es abierta por C04. No existe una inversa funcional del cuadrado sobre toda la recta porque no es inyectivo; calcular esta preimagen sólo resuelve pertenencia a un intervalo de salida.

**Retorno visual.** Véase [C14-F03](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Resolver la condición de salida produce dos ramas de entradas: sus magnitudes deben estar estrictamente entre uno y dos. Las cuatro fronteras se excluyen porque sus cuadrados están en las fronteras excluidas de $(1,4)$. Cada rama es un intervalo abierto real y su unión también. La función cuadrado no tiene inversa en toda la recta, pero eso no impide calcular su preimagen mediante una condición sobre la salida de cada entrada.

</details>

#### Ejercicio 18. Basta una base de intervalos

[]{#MA-EX-ANM-01-014-018}

Supón que para cada intervalo abierto real $I$, la preimagen $f^{-1}[I]$ es abierta relativa a $D$. Prueba continuidad de $f:D\to\mathbb R$.

[]{#MA-SOL-ANM-01-014-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Fijemos $a\in D$ y $\varepsilon>0$. El intervalo $(f(a)-\varepsilon,f(a)+\varepsilon)$ es una bola abierta y su preimagen abierta contiene $a$. El criterio por bolas da $\delta>0$ con $D\cap B(a,\delta)$ dentro de ella. Todas esas entradas tienen error menor que $\varepsilon$, que es continuidad. No es necesario seleccionar intervalos ni radios para todos los puntos a la vez.

No hace falta seleccionar una base completa de abiertos para probar cada precisión. Fijados centro y tolerancia, escogemos precisamente el intervalo centrado en su salida. La hipótesis garantiza que su preimagen es abierta relativa y contiene al centro. El criterio por bolas entrega entonces el radio de continuidad. El argumento reconstruye el control puntual directamente y vale para un centro arbitrario del dominio.

</details>

#### Ejercicio 19. Ceros cerrados en el ambiente correcto

[]{#MA-EX-ANM-01-014-019}

Sea $D=(0,1)$ y $f:D\to\mathbb R$ la función cero. Describe su conjunto de ceros y explica por qué el criterio de cerrados no afirma que sea cerrado en $\mathbb R$.

[]{#MA-SOL-ANM-01-014-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

El conjunto de ceros es todo $D=(0,1)$, cerrado relativo a sí mismo porque su complemento dentro de $D$ es vacío y abierto relativo. No es cerrado absoluto: cero es adherente y falta en él, por ejemplo mediante la ruta $1/(n+2)$. El criterio afirma cerradura en el dominio, no en otro ambiente.

Todo el dominio es cerrado respecto de sí mismo porque su complemento relativo es vacío. La preimagen de cero coincide con ese dominio. Pero en el ambiente real faltan puntos adherentes como cero y uno, de modo que no es cerrado absoluto. La continuidad no completa el dominio con sus puntos frontera. El criterio de preimágenes de cerrados conserva exactamente el ambiente en el que se ha declarado la función.

</details>

#### Ejercicio 20. Codominio restringido y preimágenes

[]{#MA-EX-ANM-01-014-020}

Sean $f:D\to E\subseteq\mathbb R$ y $V=E\cap U$, con $U$ abierto absoluto. Demuestra $f^{-1}[V]=f^{-1}[U]$ y deduce el criterio de continuidad con abiertos relativos de $E$.

[]{#MA-SOL-ANM-01-014-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Para $x\in D$, el tipo garantiza $f(x)\in E$, por lo que $f(x)\in E\cap U$ equivale a $f(x)\in U$. Esto prueba la igualdad. Si hay continuidad, el criterio absoluto da apertura de cada preimagen de $U$, por tanto de $V$. Recíprocamente, cada abierto absoluto $U$ tiene intersección $E\cap U$ abierta relativa y con la misma preimagen, así que el criterio absoluto vuelve a aplicar. Los ambientes cambian, las distancias reales no.

Aunque un abierto absoluto $U$ contenga salidas fuera de $E$, ninguna evaluación de $f$ puede producirlas. Por eso recortarlo a $E\cap U$ no cambia su selección de entradas. Esta igualdad permite expresar el criterio mediante abiertos relativos del codominio en lugar de abiertos de la recta. En la dirección inversa, cada abierto absoluto induce uno relativo con la misma preimagen, recuperando el criterio original.

</details>

## 14.5. Operar y componer sin perder el dominio

[]{#MA-SEC-ANM-01-014-005}

Las identidades algebraicas de C13 vuelven a descomponer los errores, con los destinos fijados ahora por $L=f(a)$ y $M=g(a)$. La estimación debe incluir $x=a$, donde los errores se anulan. Esto permite combinar funciones incluso si el centro es aislado y evita el problema de perforación que aparecía al componer límites.

Sean $f,g:D\to\mathbb R$ continuas en $a\in D$, y pongamos $L=f(a)$, $M=g(a)$. Para la suma, la triangular da $|(f(x)+g(x))-(L+M)|\le|f(x)-L|+|g(x)-M|$. Pedimos a cada función un error menor que $\varepsilon/2$ y reunimos los radios para obtener error total menor que $\varepsilon$. Si $\lambda\ne0$, el radio de $f$ para $\varepsilon/|\lambda|$ controla $\lambda f$; si $\lambda=0$, todos los errores son cero. La resta resulta usando $\lambda=-1$, y la triangular inversa $||f(x)|-|f(a)||\le|f(x)-f(a)|$ demuestra continuidad de $|f|$ con el mismo radio.

Para el producto, añadir y restar $f(x)M$ da $f(x)g(x)-LM=f(x)(g(x)-M)+M(f(x)-L)$. El primer multiplicador varía con la entrada y necesita una barrera común. La continuidad de $f$ para tolerancia $1$ entrega $r>0$ con $|f(x)|<A:=|L|+1$ en la bola relativa. Ponemos $B=|M|+1>0$ y pedimos errores de $g$ y $f$ menores que $\varepsilon/(2A)$ y $\varepsilon/(2B)$. En el mínimo de esos radios y de $r$, cada término de la identidad tiene magnitud menor que $\varepsilon/2$, incluso si su multiplicador es cero. Por tanto,

$$
|f(x)g(x)-LM|
\le |f(x)||g(x)-M|+|M||f(x)-L|
<\varepsilon.
$$

Los denominadores $A$ y $B$ son positivos aunque se anulen los valores centrales, y la barrera incluye $x=a$. Así quedan probadas suma, resta, producto, escala y magnitud sin recurrir a acumulación ni a una selección de entradas.

Si $g(a)=M\ne0$, la tolerancia $|M|/2$ da $|g(x)|\ge|M|-|g(x)-M|>|M|/2>0$ cerca de $a$. El dominio $D_g=\{x\in D:g(x)\ne0\}$ contiene por tanto una bola relativa del dominio original e incluye al centro. En esa bola podemos escribir

$$
\left|\frac1{g(x)}-\frac1M\right|
\le\frac{2|g(x)-M|}{|M|^2}.
$$

Al pedir además $|g(x)-M|<\varepsilon|M|^2/2$ y tomar el mínimo de los dos radios, la cota final queda estrictamente por debajo de $\varepsilon$. Esto prueba continuidad de $1/g$ en el centro considerado sobre $D_g$, y el producto con $f|_{D_g}$ prueba la de $f/g$. La desigualdad no estricta anterior admite error cero tanto en $x=a$ como en cualquier otra entrada donde $g(x)=M$; la precisión estricta se obtiene al final. En cada punto donde las funciones sean continuas y el denominador no se anule, se repite el mismo argumento.

Las constantes tienen error cero y la identidad tiene error $|x-a|$, así que sirven los radios $1$ y $\varepsilon$, respectivamente. Una inducción finita con productos y sumas construye la continuidad de todos los polinomios. Sus cocientes son continuos en el dominio donde el denominador no se anula; los puntos excluidos no son evaluaciones de la función dada.

**Teorema.** Sean $f:D\to E$, $g:E\to\mathbb R$, $a\in D$ y $b=f(a)$. Si $f$ es continua en $a$ y $g$ en $b$, entonces $g\circ f$ es continua en $a$.

Dado $\varepsilon>0$, la continuidad exterior proporciona $\eta>0$ tal que $y\in E$ y $|y-b|<\eta$ implican $|g(y)-g(b)|<\varepsilon$. Presentamos esa escala $\eta$ a la continuidad de $f$ y obtenemos $\delta>0$ con $|f(x)-b|<\eta$ para $x\in D$, $|x-a|<\delta$. Como $f:D\to E$, cada salida intermedia está admitida por $g$. Aplicando su control a $y=f(x)$ obtenemos

$$
|g(f(x))-g(f(a))|<\varepsilon.
$$

Si $f(x)=b$, la exterior evalúa su propio centro y da error cero; si $f(x)\ne b$, la misma estimación sigue siendo válida. No hacen falta evitación del punto intermedio ni acumulación de $b$ en $E$, porque la continuidad exterior controla la bola completa.

![C14-F04. La exterior responde a ε=0,6 con η=0,6; la interior responde a η con δ=0,3. Las tres ventanas incluyen su centro. La cadena de radios controla |2x| incluso cuando la salida intermedia es exactamente cero; las bandas dibujadas ilustran los contratos probados.](../../assets/books/anm/C14/C14-F04.svg){#fig-anm-c14-f04 fig-alt="Tres paneles de dos equis, valor absoluto e interior compuesto, con ventanas anidadas de precisión y centros llenos en el origen."}

Cuando sólo tenemos $f:D\to\mathbb R$ y $g:E\to\mathbb R$, la composición está definida en $T=\{x\in D:f(x)\in E\}$. Fijado $a\in T$, si $f$ es continua en $a$ y $g$ en $f(a)$, restringimos la interior a $T$ y declaramos codominio $E$. La restricción conserva continuidad y la prueba anterior da continuidad de la composición relativa a $T$. No se concluye una evaluación en $D\setminus T$. Si $T$ es vacío, no hay centros donde comprobarla.

Para continuidad global también podemos usar $(g\circ f)^{-1}[V]=f^{-1}[g^{-1}[V]]$. Si ambas funciones son continuas en sus dominios, la primera selección produce $g^{-1}[V]$ abierto relativo en $E$ y la segunda produce un abierto relativo en $D$. El criterio de §14.4 demuestra continuidad de la composición. El ambiente intermedio es $E$: no se necesita que esa preimagen sea abierta en toda la recta.

### Ejercicios de la sección 14.5

#### Ejercicio 21. Producto con un valor central nulo

[]{#MA-EX-ANM-01-014-021}

Supón $f,g:D\to\mathbb R$ continuas en $a$ con $f(a)=0$. Prueba continuidad de $fg$ usando una cota local y un único error variable.

[]{#MA-SOL-ANM-01-014-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Continuidad de $g$ para tolerancia uno da $r>0$ con $|g(x)|<B:=|g(a)|+1$ en la bola relativa. Dado $\varepsilon>0$, continuidad de $f$ da $\delta_f$ con $|f(x)|<\varepsilon/B$. En radio $\min(r,\delta_f)$, $|f(x)g(x)-f(a)g(a)|=|f(x)g(x)|<\varepsilon$. La positividad de $B$ evita dividir por un valor central nulo.

El valor central del producto es cero, así que sólo necesitamos hacer pequeño $f(x)$ mientras mantenemos $g(x)$ acotado. La continuidad de $g$ entrega una barrera positiva $B$, aunque $g(a)$ también fuera cero. La continuidad de $f$ responde a la precisión $\varepsilon/B$. El mínimo de radios proporciona ambos controles y la triangular de producto da el error requerido. No se divide por ningún valor central que pueda anularse.

</details>

#### Ejercicio 22. Cociente con dominio declarado

[]{#MA-EX-ANM-01-014-022}

Prueba continuidad de $r(x)=(x^2+1)/(x-2)$ en su dominio natural y explica qué se puede afirmar en $2$.

[]{#MA-SOL-ANM-01-014-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

El dominio es $\mathbb R\setminus\{2\}$. En cada punto de él, ambos polinomios son continuos y el denominador central es no nulo, por lo que el teorema de cocientes da continuidad relativa. En dos no hay evaluación de la expresión, así que no preguntamos por su continuidad como función dada. Un límite o una posible extensión sería una pregunta distinta; la regla de cocientes no la autoriza cuando el denominador límite es cero.

La expresión define una función sólo donde $x-2\ne0$. En cada centro de ese dominio el denominador central está definido y es no nulo, por lo que la regla de continuidad de cocientes se aplica. En dos la función dada no tiene evaluación; asignarle continuidad allí sin extenderla sería una pregunta mal formada. Investigar un límite o una extensión necesita un argumento propio y no una aplicación de la regla con denominador límite cero.

</details>

#### Ejercicio 23. Composición que toca el centro

[]{#MA-EX-ANM-01-014-023}

Prueba directamente que $h(x)=|2x|$ es continua en cero por radios anidados, permitiendo $2x=0$.

[]{#MA-SOL-ANM-01-014-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

La exterior $g(y)=|y|$ en cero responde al desafío $\varepsilon$ con $\eta=\varepsilon$, por el error $|y|$. La interior $f(x)=2x$ responde al desafío $\eta$ con $\delta=\eta/2$. Así $|x|<\delta$ implica $|2x|<\eta$ y $||2x|-0|<\varepsilon$. Si $x=0$, el error es cero y ambas etapas siguen siendo válidas.

**Retorno visual.** Véase [C14-F04](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Diseñamos primero la escala de la exterior y luego la de la interior. El valor absoluto transforma una entrada $y$ cercana a cero en una salida con error $|y|$; la multiplicación por dos hace el error intermedio $2|x|$. Así el radio final es $\varepsilon/2$. Si la interior alcanza el centro, la exterior lo evalúa con salida cero y cumple la misma estimación. Continuidad no pierde ese caso como un límite perforado exterior.

</details>

#### Ejercicio 24. Composición sólo donde existe

[]{#MA-EX-ANM-01-014-024}

Toma $f(x)=x^2$ en $\mathbb R$ y $g(y)=1/(y-1)$ en $E=\mathbb R\setminus\{1\}$. Determina el dominio efectivo de composición y prueba continuidad allí.

[]{#MA-SOL-ANM-01-014-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

$T=\{x:x^2\ne1\}=\mathbb R\setminus\{-1,1\}$. La interior es continua en cada real y la exterior en cada punto de $E$ por recíproco de una afín no nula. En cada $a\in T$, $f(a)\in E$, así que el teorema de composición da continuidad relativa a $T$. La expresión resultante es $1/(x^2-1)$, sin evaluación en los dos puntos excluidos.

Las entradas uno y menos uno producen la salida intermedia prohibida uno. Excluirlas da el dominio efectivo $T$. Allí la función interior se restringe y su codominio puede declararse $E$ para componer de manera compatible. La exterior es continua en sus entradas admitidas, y la regla de composición prueba continuidad relativa a $T$. La fórmula final no define evaluaciones en los puntos retirados.

</details>

#### Ejercicio 25. Composición por regiones de salida

[]{#MA-EX-ANM-01-014-025}

Demuestra continuidad global de la composición de $f:D\to E$ y $g:E\to\mathbb R$ continuas usando sólo el criterio de preimágenes. Justifica cada ambiente.

[]{#MA-SOL-ANM-01-014-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

Para $V$ abierto absoluto, $g^{-1}[V]$ es abierto relativo a $E$. El criterio para $f:D\to E$ da que $f^{-1}[g^{-1}[V]]$ es abierto relativo a $D$. Un punto $x$ pertenece a ese conjunto si y sólo si $g(f(x))\in V$, así que coincide con $(g\circ f)^{-1}[V]$. El criterio de abiertos concluye continuidad en $D$. Ni inyectividad ni elección numerable son necesarias.

El conjunto seleccionado en la etapa intermedia es abierto relativo a $E$, no necesariamente abierto en toda la recta. El criterio de continuidad de $f$ con codominio relativo permite seleccionarlo y obtener un abierto relativo en $D$. La identidad de preimágenes identifica esa selección con la de la composición. La prueba conserva todos los ambientes y no utiliza imágenes de abiertos, cuya apertura no estaría garantizada.

</details>

## 14.6. Lo que la continuidad no promete sobre imágenes e inversas

[]{#MA-SEC-ANM-01-014-006}

Las preimágenes describen qué entradas satisfacen una condición de salida. Las imágenes reúnen las salidas de un conjunto de entradas, y su apertura o su cierre plantean una cuestión diferente. La distinción se vuelve decisiva al intentar recuperar las entradas mediante una función inversa.

El cuadrado $q:\mathbb R\to\mathbb R$ es continuo y envía el abierto $\mathbb R$ a $[0,\infty)$. La imagen es exacta: todo cuadrado es no negativo y cada $y\ge0$ se alcanza en su raíz no negativa, cuya existencia y unicidad se demostraron en §10.7. Ninguna bola real alrededor de cero cabe en esa imagen, pues contiene negativos. Así una función continua puede enviar un abierto a un conjunto que no es abierto, sin contradecir el criterio de preimágenes.

La función $r(x)=1/(1+x^2)$ es continua en el dominio cerrado $\mathbb R$ y tiene imagen $(0,1]$. Sus salidas están en ese intervalo; para cada $0<y\le1$, la cantidad $1/y-1$ es no negativa y $x=\sqrt{1/y-1}$ produce $r(x)=y$. Esto demuestra la igualdad de imagen. Cero no se alcanza, pero cada bola de radio $\rho>0$ centrada en cero contiene la salida $\min(\rho/2,1/2)>0$. La imagen no es cerrada. La conclusión posterior sobre imágenes de compactos necesitará esa hipótesis adicional.

Sea $D=[0,1)\cup[2,3]$ y $f:D\to[0,2]$, con $f(x)=x$ en la primera pieza y $f(x)=x-1$ en la segunda. Cada regla es inyectiva y sus imágenes $[0,1)$ y $[1,2]$ son disjuntas, por lo que tampoco hay colisiones entre piezas. Como esas imágenes cubren $[0,2]$, toda salida declarada tiene una entrada única: $f$ es biyectiva.

También es continua en todo $D$. La distancia entre una entrada de la primera pieza y otra de la segunda es mayor que uno, así que la ventana de radio $\delta=\min(1/2,\varepsilon)$ alrededor de cualquier $a\in D$ sólo encuentra su propia pieza. Dentro de ella la regla es afín de pendiente uno y $|f(x)-f(a)|=|x-a|<\varepsilon$. La separación del dominio permite mantener ese control incluso en los extremos incluidos.

La inversa $h:[0,2]\to D$ vale $h(y)=y$ para $y<1$ y $h(y)=y+1$ para $y\ge1$; en particular $h(1)=2$. Recibamos cualquier $\delta>0$ y pongamos $t=\min(\delta/2,1/2)$, $y=1-t$. Tenemos $y\in[0,2]$ y $|y-1|=t<\delta$, pero la primera rama da $|h(y)-h(1)|=|1-t-2|=1+t>1$. La tolerancia fija $1/2$ falla en toda ventana, de modo que la inversa no es continua en uno.

![C14-F05. La biyección envía \[0,1) y \[2,3\] a \[0,1) y \[1,2\]. En su dominio separado es continua. Su inversa tiene valor 2 en uno, pero entradas que llegan a uno desde abajo producen salidas cercanas a uno. La inversa existe y falla en continuidad.](../../assets/books/anm/C14/C14-F05.svg){#fig-anm-c14-f05 fig-alt="Dos gráficos reflejados por intercambio de entrada y salida: dos ramas separadas en el dominio original y un salto de la inversa en uno."}

La pieza $[2,3]$ es abierta relativa a $D$, por ejemplo porque es $D\cap(3/2,4)$, mientras su imagen $[1,2]$ no es abierta relativa a $[0,2]$. Para cualquier radio alrededor de uno hay entradas del codominio ligeramente menores que uno y fuera de $[1,2]$. Como $h^{-1}[[2,3]]=[1,2]$, el criterio de preimágenes identifica el mismo fallo de continuidad inversa.

Llamamos **homeomorfismo** entre subconjuntos reales a una biyección continua cuya inversa también es continua. Esta definición describe transporte reversible de proximidad; no es una nueva conclusión sobre cualquier biyección.

Una biyección $f:D\to E$ es una aplicación abierta si $f[U]$ es abierto relativo a $E$ para todo $U$ abierto relativo a $D$. Escribamos $h=f^{-1}$. Para $U\subseteq D$, una salida $y\in E$ pertenece a $h^{-1}[U]$ exactamente cuando su entrada única $h(y)$ pertenece a $U$, es decir, cuando $y\in f[U]$. Así $h^{-1}[U]=f[U]$, o equivalentemente $(f^{-1})^{-1}[U]=f[U]$. El criterio de §14.4 dice entonces que $h$ es continua si y sólo si $f$ es abierta. En particular, una biyección continua es homeomorfismo exactamente cuando además es abierta. La equivalencia para la inversa sólo ha usado biyectividad; los dos símbolos inversos anidados expresan operaciones distintas.

### Ejercicios de la sección 14.6

#### Ejercicio 26. Imagen cerrada que pierde la cerradura

[]{#MA-EX-ANM-01-014-026}

Prueba que la función $r(x)=1/(1+x^2)$ es continua en $\mathbb R$ y tiene imagen exactamente $(0,1]$. Refuta cerradura de la imagen mediante un punto adherente.

[]{#MA-SOL-ANM-01-014-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

El denominador es un polinomio continuo y siempre positivo, de modo que el recíproco es continuo. Sus valores satisfacen $0<r(x)\le1$. Para cada $y\in(0,1]$, la entrada $\sqrt{1/y-1}$ produce $y$, luego la imagen es exactamente ese intervalo. Cero está fuera y toda bola suya contiene un punto del intervalo, por ejemplo $\min(\varepsilon/2,1/2)>0$ si el radio es $\varepsilon$. La imagen no es cerrada aunque el dominio real lo sea.

Para una salida $0<y\le1$, la cantidad $1/y-1$ es no negativa y su raíz proporciona una entrada real con la salida deseada. Esto prueba la inclusión que faltaba para la imagen exacta. Cero no se alcanza porque el denominador es positivo y finito en cada entrada. Sin embargo, cualquier bola alrededor de cero contiene alguna salida positiva del intervalo. Tener un punto adherente ausente refuta cerradura de la imagen.

</details>

#### Ejercicio 27. Auditar la biyección y su inversa

[]{#MA-EX-ANM-01-014-027}

Verifica la bijectividad y continuidad de la función por piezas de §14.6. Refuta directamente la continuidad de su inversa en uno.

[]{#MA-SOL-ANM-01-014-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Las piezas $[0,1)$ y $[2,3]$ se envían afínmente a $[0,1)$ y $[1,2]$, disjuntas y con unión $[0,2]$. Cada regla es inyectiva, y las imágenes disjuntas prueban inyectividad global; la unión prueba sobreyectividad. Un radio $\min(1/2,\varepsilon)$ evita la otra pieza y controla error $|x-a|$. La inversa vale $y$ por debajo de uno y $y+1$ desde uno. Para cada radio, $y=1-\min(\delta/2,1/2)$ tiene distancia de entrada menor que $\delta$ pero distancia de salida a $h(1)=2$ mayor que uno.

**Retorno visual.** Véase [C14-F05](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La separación entre las piezas del dominio permite controlar cada centro usando sólo su regla afín local. En las salidas, las imágenes se unen sin esa separación: valores inferiores a uno pueden acercarse a uno desde la primera pieza, aunque uno proceda de la entrada dos de la segunda. La inversa debe saltar entre esas piezas. El infractor explícito demuestra que ninguna reducción del radio exterior elimina esta separación de entradas.

</details>

#### Ejercicio 28. La identidad de un transporte reversible

[]{#MA-EX-ANM-01-014-028}

Prueba que una biyección $f:D\to E$ tiene inversa continua si y sólo si envía cada abierto relativo de $D$ a un abierto relativo de $E$.

[]{#MA-SOL-ANM-01-014-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Escriba $h=f^{-1}:E\to D$. Para $U\subseteq D$, $y\in h^{-1}[U]$ equivale a que la entrada única $h(y)$ esté en $U$, lo que equivale a $y\in f[U]$. Por tanto $h^{-1}[U]=f[U]$. El criterio de continuidad de $h$ con abiertos relativos de su codominio $D$ es exactamente la propiedad de imágenes enunciada. Ambas implicaciones se siguen de esa igualdad y del criterio, sin asumir continuidad de $f$.

Una salida pertenece a $h^{-1}[U]$ cuando su entrada recuperada está en $U$. Como $f$ es biyectiva, eso equivale a que la salida haya sido producida desde $U$. Por tanto tomar preimagen bajo la inversa es tomar imagen bajo la función original. El criterio de abiertos convierte entonces continuidad inversa en apertura de $f$. La continuidad de $f$ no se necesita para probar esta equivalencia específica.

</details>

#### Ejercicio 29. Una afín es un homeomorfismo

[]{#MA-EX-ANM-01-014-029}

Para $m\ne0$, prueba que $f:\mathbb R\to\mathbb R$, $f(x)=mx+c$, es un homeomorfismo con certificados en ambas direcciones.

[]{#MA-SOL-ANM-01-014-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Es inyectiva porque $m(x-z)=0$ implica $x=z$, y sobreyectiva porque para cada $y$ la entrada $(y-c)/m$ produce $y$. Su inversa es esa regla afín. El error directo es $|m||x-a|$, con radio $\varepsilon/|m|$. El inverso es $|y-b|/|m|$, con radio $|m|\varepsilon$. Las pruebas funcionan en cada centro y legitiman el transporte reversible.

La pendiente no nula permite despejar cada entrada de manera única y construir la inversa afín. La escala directa es $|m|$ y la inversa es su recíproco. Cada dirección tiene por ello su propio radio para la misma precisión: $\varepsilon/|m|$ al avanzar y $|m|\varepsilon$ al volver. Las constantes de traslación se cancelan al restar valores. Estas pruebas cuantitativas verifican todos los requisitos del homeomorfismo.

</details>

#### Ejercicio 30. Controles inversos sin intervalos compactos

[]{#MA-EX-ANM-01-014-030}

Sea $f:D\to E$ una biyección continua que es abierta. Prueba que la imagen por $f$ de cualquier cerrado relativo a $D$ es cerrada relativa a $E$. No uses compacidad.

[]{#MA-SOL-ANM-01-014-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Si $F\subseteq D$ es cerrado relativo, $D\setminus F$ es abierto relativo. La aplicación abierta da $f[D\setminus F]$ abierto relativo a $E$. Por bijectividad, $f[D\setminus F]=E\setminus f[F]$: una salida tiene única entrada y ésta está fuera de $F$ exactamente cuando la salida no está en $f[F]$. Por tanto $f[F]$ es cerrado relativo. La bijectividad es decisiva para la identidad de complementos de imágenes.

La apertura de la aplicación controla el complemento del cerrado relativo. La identidad de complementos de imágenes requiere biyectividad: cada salida debe tener una entrada y no puede tener entradas en ambas partes. De ahí que la imagen del complemento sea exactamente el complemento de la imagen. Como ese complemento es abierto relativo a $E$, la imagen del cerrado es cerrada allí. El argumento usa complementos y apertura, sin recurrir a compacidad.

</details>

## 14.7. Reunir definiciones locales y piezas cerradas

[]{#MA-SEC-ANM-01-014-007}

Para construir una función a partir de reglas en regiones, primero hay que comprobar que asignan el mismo valor en cada intersección. Ese acuerdo define una función única, pero aún debemos controlar entradas que se acercan a un centro desde otra región. Las propiedades de las piezas determinarán cómo reunir sus estimaciones.

Si $D=\bigcup_{i\in I}U_i$, con cada $U_i$ abierto relativo a $D$, y $f|_{U_i}$ es continua en cada $U_i$, entonces $f$ es continua en $D$.

Fijados $a\in D$ y $\varepsilon>0$, alguna pieza $U_i$ contiene $a$. Su apertura relativa proporciona $r>0$ con $D\cap B(a,r)\subseteq U_i$, y la continuidad de la restricción proporciona un radio $\delta_i>0$ para esa tolerancia. Toda entrada de $D$ dentro de $\min(r,\delta_i)$ permanece en la pieza y satisface su estimación. Esto prueba continuidad en el centro arbitrario. Aunque la cobertura sea infinita, sólo usamos una pieza que contiene el punto fijado y reunimos dos radios.

**Teorema.** Sea $D=F_1\cup\cdots\cup F_m$, con $m\ge1$ y $F_i$ cerrados relativos a $D$. Si $f:D\to\mathbb R$ tiene restricción continua en cada $F_i$, entonces es continua en $D$. Equivalentemente, podemos partir de funciones continuas en las piezas que coincidan en todas las intersecciones y pegarlas.

Una pieza cerrada que contiene $a$ puede llegar hasta él por un solo lado y no contener ninguna bola relativa alrededor de $a$. La prueba tendrá que controlar las entradas de todas las piezas que contienen el centro y excluir localmente las piezas que no lo contienen.

Fijemos $a\in D$ y $\varepsilon>0$. Si $a\in F_i$, la continuidad de la restricción entrega $\delta_i>0$ que controla sus entradas cercanas. Si $a\notin F_i$, el complemento $D\setminus F_i$ es abierto relativo y contiene $a$, por lo que hay $r_i>0$ con $D\cap B(a,r_i)\subseteq D\setminus F_i$. Cada pieza aporta así un radio de control o de exclusión. Como sólo hay finitas piezas, el mínimo de todos esos radios es positivo. Cualquier entrada del dominio dentro de él pertenece a alguna $F_j$ por la cobertura. Las piezas ausentes del centro quedaron excluidas; por tanto pertenece a una pieza que contiene $a$ y su error es menor que $\varepsilon$.

El cierre permite excluir una pieza cuando su continuidad no está centrada en $a$; la finitud asegura que las exclusiones y los controles tengan un radio positivo común. Si partimos de funciones $f_i$ en las piezas, su acuerdo en intersecciones hace único el valor pegado y garantiza $f|_{F_i}=f_i$. La prueba anterior puede entonces aplicarse a esas restricciones, sin escoger simultáneamente una pieza para cada punto.

![C14-F06. Pegado de dos reglas afines sobre semirrectas cerradas con valor común cero produce |x| continuo. En el segundo gráfico, las reglas constantes viven en (−∞,0) y \[0,∞): el acuerdo en la intersección vacía no evita la falla en cero. La primera pieza no es cerrada.](../../assets/books/anm/C14/C14-F06.svg){#fig-anm-c14-f06 fig-alt="Valor absoluto con vértice lleno en cero frente a una función escalón con círculo vacío en cero cero y punto lleno en cero uno."}

El valor absoluto se obtiene pegando $-x$ en $(-\infty,0]$ y $x$ en $[0,\infty)$. Las dos piezas son cerradas, cubren la recta y sus reglas afines continuas dan el mismo valor cero en la intersección. El teorema demuestra continuidad de $|x|$. También se aplica cuando una pieza contiene puntos aislados: la continuidad de su restricción sigue teniendo sentido en ellos.

Si usamos $D_1=(-\infty,0)$ y $D_2=[0,\infty)$, con reglas constantes cero y uno, el acuerdo en la intersección vacía asegura que la función está bien definida y ambas restricciones son continuas. Sin embargo, su valor central en cero es uno y cada entrada $-\delta/2$ tiene salida cero dentro de la ventana de radio $\delta>0$. La tolerancia $1/2$ refuta continuidad. La primera pieza no es cerrada: llega arbitrariamente cerca de cero sin contenerlo y no puede excluirse mediante ningún radio.

La continuidad también protege un signo no nulo. Si $f(a)>0$, la tolerancia $f(a)/2$ da $f(x)>f(a)/2>0$ en una bola relativa. Si $f(a)<0$, usamos $|f(a)|/2$ y obtenemos $f(x)<f(a)/2<0$. Para una función continua en todo $D$, estas estimaciones concuerdan con la apertura relativa de $f^{-1}[(0,\infty)]$ y de $f^{-1}[(-\infty,0)]$. La estabilidad cerca de un punto no prueba que existan ceros entre salidas de signos diferentes; esa cuestión necesitará en C15 un argumento sobre la estructura del dominio.

### Ejercicios de la sección 14.7

#### Ejercicio 31. Pegar un valor absoluto desplazado

[]{#MA-EX-ANM-01-014-031}

Prueba continuidad de $f(x)=2-x$ para $x\le2$ y $f(x)=x-2$ para $x\ge2$ mediante el teorema de pegado finito.

[]{#MA-SOL-ANM-01-014-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

Las piezas $(-\infty,2]$ y $[2,\infty)$ son cerradas, cubren la recta y las reglas afines son continuas en ellas. Ambas dan cero en la intersección $\{2\}$, por lo que la función está bien definida. El pegado finito prueba continuidad global; coincide con $|x-2|$, pero no es necesario usar esa identidad para aplicar el mecanismo.

**Retorno visual.** Véase [C14-F06](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las dos reglas coinciden en el único punto donde ambas se aplican, lo que asegura una asignación única. Cada una es afín continua en su semieje relativo, y las dos piezas son cerradas y finitas. El teorema de pegado proporciona la continuidad del conjunto. La identidad con un valor absoluto puede confirmar la fórmula, pero la prueba pedida muestra cómo unir controles de piezas que llegan a la misma frontera.

</details>

#### Ejercicio 32. Localizar con una cobertura abierta

[]{#MA-EX-ANM-01-014-032}

Demuestra que si una función es continua en la restricción a cada pieza de una cobertura abierta relativa de $D$, entonces es continua en $D$, aunque haya infinitas piezas.

[]{#MA-SOL-ANM-01-014-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Fijamos $a\in D$ y $\varepsilon>0$. Alguna pieza abierta relativa $U$ contiene $a$. Hay $r>0$ con $D\cap B(a,r)\subseteq U$, y la continuidad de la restricción da $\delta_U$. El mínimo de ambos radios controla toda entrada del dominio: primero la coloca en $U$ y después limita el error. La prueba sólo necesita una pieza para el punto fijado, no un mínimo de una familia infinita.

Aunque haya infinitas piezas, para un centro fijado basta una pieza que lo contenga. Su apertura relativa garantiza que todas las entradas suficientemente próximas del dominio permanezcan dentro de ella. Después usamos la continuidad de su restricción y tomamos el mínimo de esos dos radios. Nunca reunimos radios de todas las piezas simultáneamente. Esto explica por qué no hace falta finitud en una cobertura abierta.

</details>

#### Ejercicio 33. El acuerdo sin cierre no basta

[]{#MA-EX-ANM-01-014-033}

Construye una función pegada a partir de dos restricciones continuas que coincidan en su intersección y que sea discontinua. Identifica la hipótesis ausente.

[]{#MA-SOL-ANM-01-014-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

Use piezas $D_1=(-\infty,0)$ y $D_2=[0,\infty)$, con reglas constantes cero y uno. Son continuas en sus respectivos dominios y coinciden en la intersección vacía. La función global tiene valor uno en cero, pero $-\delta/2$ produce cero en cada radio; tolerancia $1/2$ refuta continuidad. $D_1$ no es cerrado relativo al dominio real, por lo que no puede excluirse cerca de un centro que no le pertenece.

El acuerdo en una intersección vacía se cumple automáticamente y asegura que no haya dos reglas incompatibles para una misma entrada. Pero no controla aproximaciones desde la pieza negativa al centro cero, que pertenece sólo a la otra pieza. Los testigos negativos mantienen error uno en cualquier ventana. La hipótesis ausente es la cerradura relativa necesaria para excluir localmente una pieza que no contiene al centro en el pegado finito.

</details>

#### Ejercicio 34. Una cobertura cerrada infinita falla

[]{#MA-EX-ANM-01-014-034}

En $D=\{0\}\cup\{1/n:n\ge1\}$, define $f(0)=0$, $f(1/n)=1$. Prueba que las piezas singleton forman una cobertura cerrada relativa con restricciones continuas, pero la función completa no es continua en cero.

[]{#MA-SOL-ANM-01-014-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Cada singleton es cerrado en la recta: desde cualquier punto distinto, la mitad de la distancia evita el singleton. Por intersección también es cerrado relativo a $D$. Las piezas cubren $D$ y cada restricción es constante, por tanto continua. En cero, para cualquier radio $\delta>0$, arquimedianidad da un entero positivo $n>1/\delta$; entonces $1/n<\delta$ y el error es uno. La tolerancia $1/2$ refuta continuidad. La cobertura es infinita; los radios que excluyen cada pieza distinta de cero no tienen una escala común positiva.

Cada singleton ofrece una prueba trivial de continuidad de su restricción, porque sólo contiene una entrada. Sin embargo, las otras piezas se acercan arbitrariamente a la pieza cero y todas sus salidas valen uno. No existe un radio que las excluya simultáneamente, aunque cada una individualmente sea cerrada. El ejemplo localiza el papel de la finitud: el mínimo de infinitos radios de exclusión puede no ser positivo.

</details>

#### Ejercicio 35. Conservar un signo cerca del centro

[]{#MA-EX-ANM-01-014-035}

Supón $f:D\to\mathbb R$ continua en $a$ y $f(a)<0$. Prueba que existe una ventana relativa en que todos sus valores son negativos. Formula también la conclusión topológica global para $f<0$.

[]{#MA-SOL-ANM-01-014-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Use tolerancia $|f(a)|/2=-f(a)/2>0$. En el radio de continuidad, $f(x)<f(a)+|f(a)|/2=f(a)/2<0$. Si $f$ es continua en todo $D$, el conjunto de valores negativos de entrada es $f^{-1}[(-\infty,0)]$ y es abierto relativo por el criterio. No se deduce existencia de un cero en otro lugar: sólo apertura y estabilidad local.

La mitad de la magnitud del valor negativo central es una tolerancia positiva. Controlar el error por ella mantiene la salida por debajo de la mitad de ese valor, que sigue siendo negativa. Si la función es continua en todo el dominio, las entradas de salida negativa forman la preimagen de un abierto y son abiertas relativas. La afirmación global sobre ese conjunto requiere esa continuidad global, además del dato puntual inicial.

</details>

## 14.8. Certificados de proximidad y límites del control lineal

[]{#MA-SEC-ANM-01-014-008}

Una estimación lineal del error ofrece una forma directa de producir radios. Es útil reconocer qué garantiza esa estimación y qué puede seguir siendo continuo cuando no dispone de ella. La raíz en el origen permitirá separar las dos propiedades sin utilizar derivadas.

Supongamos $a\in D$ y $|f(x)-f(a)|\le K|x-a|$ para $x\in D\cap B(a,r)$, con $r>0$ y $K\ge0$. Si $K>0$, tomamos $\delta=\min(r,\varepsilon/K)>0$. La primera restricción mantiene válida la cota y la segunda da $|f(x)-f(a)|\le K|x-a|<K\delta\le\varepsilon$. Si $K=0$, la cota fuerza $f(x)=f(a)$ en esa ventana y sirve $\delta=r$ para cualquier tolerancia. Ambos argumentos incluyen el centro y no necesitan acumulación.

Para el cuadrado, $|x-a|<1$ implica $|x+a|<1+2|a|$, y la factorización da $|x^2-a^2|\le(1+2|a|)|x-a|$. La cota se escribe no estricta para incluir $x=a$, donde ambos miembros son cero. Así $\delta=\min(1,\varepsilon/(1+2|a|))$ demuestra continuidad en cada real $a$. La dependencia de esta elección respecto del centro procede de la barrera para el factor variable; escribir el mismo esquema en todos los centros no equivale a haber dado un radio común a toda la recta.

Sea $s:[0,\infty)\to[0,\infty)$, $s(x)=\sqrt{x}$. La raíz no negativa está construida en §10.7; podemos usar sus propiedades algebraicas sin suponer todavía su continuidad ni deducirla de un teorema sobre inversas. Para $x,a\ge0$, pongamos $u=\sqrt{x}$ y $v=\sqrt{a}$. Si $u\ge v$, los factores son no negativos y $u-v\le u+v$, de modo que

$$
(u-v)^2\le(u-v)(u+v)=x-a=|x-a|.
$$

Si $u<v$, intercambiamos los dos valores y obtenemos también $(u-v)^2\le|x-a|$. Tomar raíces no negativas da $|\sqrt{x}-\sqrt{a}|\le\sqrt{|x-a|}$. Para cualquier $\varepsilon>0$, el radio $\delta=\varepsilon^2$ convierte $|x-a|<\delta$ en error menor que $\varepsilon$. La misma elección funciona en todos los centros $a\ge0$, incluido cero; allí sólo se cuantifica sobre entradas no negativas y el centro produce error cero.

![C14-F07. La raíz responde al desafío ε con δ=ε² en el origen. Es continua aunque no admita un control local √x≤Kx con K finito. La comparación con K=2 muestra una instancia; la prueba construye una infracción para cualquier K y radio. Sólo se consideran entradas no negativas.](../../assets/books/anm/C14/C14-F07.svg){#fig-anm-c14-f07 fig-alt="Dos gráficos de la raíz: primero una ventana de entrada cero coma cero nueve para tolerancia cero coma tres, después comparación con la recta dos equis cerca del origen."}

Pese a esa continuidad, no existen $K\ge0$ y $r>0$ con $\sqrt{x}\le Kx$ para todas las entradas $0\le x<r$. Dados $K$ y $r$, elegimos $x=\min(r/2,1/[4(K+1)^2])>0$. Está dentro de la ventana y satisface $1/\sqrt{x}\ge2(K+1)>K$. Multiplicar por $x>0$ da $\sqrt{x}>Kx$, contra la cota propuesta. El radio cuadrático en la tolerancia demuestra continuidad, mientras este infractor descarta toda barrera lineal local de ese tipo.

Sea $f:D\to E$ biyectiva y $a\in D$. Si existe $c_a>0$ tal que

$$
|f(x)-f(a)|\ge c_a|x-a|\qquad\text{para todo }x\in D,
$$

entonces $f^{-1}$ es continua en $b=f(a)$. Dado $\varepsilon>0$, elegimos $\eta=c_a\varepsilon>0$. Para cualquier $y\in E$ con $|y-b|<\eta$, la biyectividad proporciona la entrada única $x=f^{-1}(y)$. La cota se aplica a esa entrada y da $|x-a|\le|f(x)-f(a)|/c_a=|y-b|/c_a<\varepsilon$. Éste es el control de continuidad de la inversa en $b$.

La cota se exige para todo $x\in D$ porque, al recibir una salida $y$ cercana a $f(a)$, todavía no sabemos dónde está su entrada inversa. Una cota que sólo valiera cerca de $a$ no podría aplicarse antes de demostrar que esa entrada ya es cercana. En la biyección de §14.6, para $a=2$ y $|x-2|<1/2$ vale $|f(x)-f(2)|=|x-2|$, pero la primera pieza aporta entradas lejanas de dos cuyas salidas se acercan a $f(2)=1$. La inversa falla justamente allí. La cuantificación global impide ese comportamiento.

Si una biyección satisface, para constantes positivas $c,C$, las cotas $c|x-z|\le|f(x)-f(z)|\le C|x-z|$ para todos los $x,z\in D$, la superior prueba continuidad directa con radio $\varepsilon/C$ y la inferior prueba continuidad inversa con radio $c\varepsilon$. La biyectividad autoriza cada entrada recuperada y el alcance global permite aplicarle la estimación. Es una condición suficiente para disponer de los dos controles; la raíz en el origen muestra que continuidad no requiere siempre una cota lineal.

El ejemplo de la inversa obliga a mirar también las entradas que permanecen lejos del centro: sus salidas pueden acercarse a él. En cambio, para continuidad directa basta una ventana local del dominio. Esta diferencia entre los dos sentidos del transporte explica por qué una inversa algebraicamente existente necesita su propia prueba de continuidad.

### Ejercicios de la sección 14.8

#### Ejercicio 36. Un certificado directo del cuadrado

[]{#MA-EX-ANM-01-014-036}

Prueba continuidad de $x^2$ en cada centro con una cota local lineal, y trata $x=a$ sin usar una desigualdad estricta inválida.

[]{#MA-SOL-ANM-01-014-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Para $|x-a|<1$, $|x+a|<1+2|a|=:K$. Por tanto $|x^2-a^2|\le K|x-a|$, donde la desigualdad no estricta incluye $x=a$. El radio $\delta=\min(1,\varepsilon/K)$ es positivo porque $K\ge1$. Si $|x-a|<\delta$, el error es $\le K|x-a|<K\delta\le\varepsilon$. No se escribió $0<0$ en el caso central.

Cuando $x=a$, el factor $|x-a|$ es cero. Por eso la cota del producto debe escribirse no estricta antes de usar la distancia estricta de entrada: $|x^2-a^2|\le K|x-a|<\varepsilon$. Así se incluye correctamente el centro. Para entradas diferentes, la factorización y el radio auxiliar acotan el factor variable. El mismo certificado demuestra continuidad para cualquier real $a$ sin excluir evaluaciones centrales.

</details>

#### Ejercicio 37. La raíz en un extremo del dominio

[]{#MA-EX-ANM-01-014-037}

Prueba continuidad de $\sqrt{x}$ en cero sobre $[0,\infty)$ y justifica por qué no se consideran entradas negativas.

[]{#MA-SOL-ANM-01-014-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

El valor central es cero. Dado $\varepsilon>0$, tomamos $\delta=\varepsilon^2$. Para $x\in[0,\infty)$ con $|x|<\delta$, no negatividad y orden de raíces dan $|\sqrt{x}-0|=\sqrt{x}<\varepsilon$. Los negativos no pertenecen al dominio real de la función y no son entradas del cuantificador universal. La prueba incluye cero, cuyo error es cero.

**Retorno visual.** Véase [C14-F07](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La función raíz real sólo está definida para entradas no negativas. Su continuidad en cero se prueba dentro de ese dominio, sin extenderla a negativos. El radio cuadrático convierte la condición $x<\varepsilon^2$ en $\sqrt{x}<\varepsilon$. El punto central está permitido y entrega cero. Ser un extremo del dominio no obstaculiza una prueba relativa con todas las entradas que la función realmente admite.

</details>

#### Ejercicio 38. Continuidad sin barrera lineal

[]{#MA-EX-ANM-01-014-038}

Prueba que la raíz en cero no satisface $\sqrt{x}\le Kx$ en ninguna ventana positiva para ninguna constante finita $K\ge0$, pese a ser continua.

[]{#MA-SOL-ANM-01-014-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Dados $K\ge0$ y $r>0$, sea $x=\min(r/2,1/[4(K+1)^2])>0$. Entonces $x<r$ y $1/\sqrt{x}\ge2(K+1)>K$. Multiplicar por $x>0$ da $\sqrt{x}>Kx$, infracción de la cota. Continuidad ya tiene certificado $\varepsilon^2$, que no necesita esa barrera lineal. La ausencia de un certificado suficiente no significa ausencia de continuidad.

La construcción del infractor depende de la barrera $K$ y del radio propuesto. El mínimo asegura una entrada positiva dentro de la ventana y una raíz suficientemente pequeña para que su recíproco supere $K$. La desigualdad resultante contradice la cota lineal. Esto no refuta continuidad, cuyo radio ya existe y depende cuadráticamente de la tolerancia. Refuta sólo una forma particular de certificado más fuerte.

</details>

#### Ejercicio 39. Invertir el cuadrado lejos de cero

[]{#MA-EX-ANM-01-014-039}

Para $m>0$, prueba que $q:[m,\infty)\to[m^2,\infty)$, $q(x)=x^2$, es biyectiva y que su inversa tiene un certificado lineal de continuidad.

[]{#MA-SOL-ANM-01-014-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Para $x,z\ge m$, $|x^2-z^2|=(x+z)|x-z|\ge2m|x-z|$. En particular igualdad de cuadrados implica igualdad de entradas. Cada $y\ge m^2$ tiene entrada $\sqrt{y}\ge m$, lo que prueba sobreyectividad. La inversa es la raíz restringida. Para un centro $b=q(a)$ y un desafío $\varepsilon$, $|y-b|<2m\varepsilon$ implica $|q^{-1}(y)-a|\le|y-b|/(2m)<\varepsilon$. El alcance global en $x,z$ evita entradas lejanas con salidas próximas.

En el semieje desde $m>0$, la suma de dos entradas es al menos $2m$. La factorización da así una cota inferior válida para cualquier par, además de inyectividad. Las raíces de las salidas del codominio están en el dominio y prueban sobreyectividad. La misma cota global permite que una salida cercana recupere una entrada cercana sin asumirlo previamente. El radio $2m\varepsilon$ proporciona el control inverso lineal.

</details>

#### Ejercicio 40. El control inferior local no autoriza la inversa

[]{#MA-EX-ANM-01-014-040}

Construye una biyección continua y un centro no aislado $a$ donde valga localmente $|f(x)-f(a)|\ge|x-a|$, pero cuya inversa no sea continua en $f(a)$. Explica el defecto lógico de usar esa cota local para probar continuidad inversa.

[]{#MA-SOL-ANM-01-014-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Use $D=[0,1)\cup[2,3]$, $f(x)=x$ en la primera pieza y $f(x)=x-1$ en la segunda, con $a=2$. El centro no es aislado, pues $2+t\in D$ para $0<t<1$ arbitrariamente pequeño. En radio $1/2$, todas las entradas del dominio son de la segunda pieza y $|f(x)-f(2)|=|x-2|$, así que vale la cota inferior. Pero la inversa en $f(2)=1$ toma valor dos, mientras $y_n=1-1/(n+2)$ tiende a uno y su inversa es $y_n$, que tiende a uno. No puede converger también a dos. La cota local exige antes saber que la entrada inversa está cerca de dos; precisamente eso era lo que se quería probar. Las salidas cercanas que proceden de la otra pieza quedan fuera de su alcance.

**Retorno visual.** Véase [C14-F05](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La cota local sólo habla de entradas de la segunda pieza próximas a dos. No controla las entradas de la primera pieza, que están lejos de dos pero producen salidas que se acercan a uno. Aplicarla a una entrada inversa exigiría demostrar antes que esa entrada ya está en la ventana local, que es precisamente la conclusión buscada. La ruta de salidas dada exhibe este fallo circular y refuta continuidad inversa manteniendo la biyección continua hacia delante.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-14)

[← Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Capítulo 15 →](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html)
