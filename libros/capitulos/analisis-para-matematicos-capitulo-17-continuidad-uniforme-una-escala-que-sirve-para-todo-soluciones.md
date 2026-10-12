---
content-id: MA-BCH-0272
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-017-SOLUCIONES
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
title: Soluciones — Capítulo 17
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C17_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html)

## 17.1. El orden de los cuantificadores

[]{#MA-EX-ANM-01-017-001}

[]{#MA-SOL-ANM-01-017-001}

[]{#MA-SEC-ANM-01-017-001}

Puntual: $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$, distancia menor que $\delta$ implica error respecto de $a$ menor que $\varepsilon$. Uniforme: $\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in D$ con la implicación de R1. En la primera el radio puede depender del centro; en la segunda se fija antes de los dos puntos. Negación: existe $\varepsilon_0>0$ tal que todo $\delta>0$ admite un par con distancia menor que $\delta$ y error al menos $\varepsilon_0$. Función y dominio están fijados en los tres casos. En el vacío la uniformidad es vacía y su negación es falsa, porque no existen pares.

La negación uniforme fija una sola precisión infringida y permite que las entradas cambien después de cada radio. En continuidad puntual se fija además el centro antes de diseñar la escala. Por eso no se niegan las dos propiedades con los mismos testigos. En el vacío, la existencia de una pareja infractora es imposible y toda escala positiva satisface el control.

## 17.2. Un radio dependiente no refuta otro posible

[]{#MA-EX-ANM-01-017-002}

[]{#MA-SOL-ANM-01-017-002}

Que una construcción dependa del centro no excluye otras construcciones independientes. Para refutar uniformidad fijamos $\varepsilon_0=1$; dado $\delta>0$, sea $h=\min(\delta/2,1)>0$, $x=1/h$, $y=x+h$. Si $\delta\le2$, $h=\delta/2<\delta$; si $\delta>2$, $h=1<\delta$. El error es $h(2/h+h)=2+h^2>1$. Estos testigos sí refutan todo radio común. En $[-M,M]$, $M>0$, $|x^2-y^2|\le2M|x-y|$ y $\delta=\varepsilon/(2M)$ da uniformidad. Para $M=0$ el dominio es singleton y cualquier radio sirve.

**Retorno visual.** Véase [C17-F01](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El par construido depende del candidato $\delta$, como permite la negación, mientras la tolerancia uno permanece fija. La pequeña separación $h$ se compensa con la entrada grande $1/h$ y mantiene el error mayor que uno. En el dominio acotado esa compensación ya no puede crecer sin límite, pues $|x+y|\le2M$. El caso $M=0$ debe tratarse antes de dividir por esa barrera.

## 17.3. Una escala no lineal

[]{#MA-EX-ANM-01-017-003}

[]{#MA-SOL-ANM-01-017-003}

Para $x\ge y\ge0$, con $a=\sqrt{x}\ge b=\sqrt{y}$, $(a-b)^2\le(a-b)(a+b)=x-y$. Intercambiar los argumentos cubre el otro orden, así la diferencia de raíces es a lo sumo la raíz de la distancia. $\delta=\varepsilon^2$ sirve en todo el dominio. Si una constante $L>0$ diera control Lipschitz en $[0,1]$, tomar $x=1/(n+1)^2$, $y=0$ exigiría $1/(n+1)\le L/(n+1)^2$, es decir $n+1\le L$, falso para un índice grande. $L=0$ falla entre cero y uno.

La desigualdad de raíces compara cualquier par no negativo y no presupone un centro positivo. Por ello el radio cuadrático incluye cero y vale en todo el semieje. Para refutar Lipschitz en el segmento basta examinar parejas con una entrada cero: la razón error/distancia supera cualquier constante al escoger un índice grande. El mismo ejemplo distingue control uniforme de control lineal.

## 17.4. Restricción y regreso imposible

[]{#MA-EX-ANM-01-017-004}

[]{#MA-SOL-ANM-01-017-004}

El mismo radio uniforme sirve para todos los pares del subconjunto, porque también son pares del dominio original. La recíproca falla: $x^2$ en $\mathbb R$ no es uniforme por E002, pero en $[0,1]$ tiene constante Lipschitz dos. Incluso la restricción a un singleton sería uniforme sin informar sobre el resto.

Restringir elimina parejas que había que controlar, sin crear otras nuevas. Por eso el certificado uniforme anterior sigue siendo válido. La vuelta agregaría parejas sobre las que no hay información. El cuadrado permite comprobar ambas afirmaciones concretamente: la barrera del dominio pequeño funciona allí y los pares que escapan en el mayor refutan uniformidad global.

## 17.5. Uniformidad sin compacidad ni acotación

[]{#MA-EX-ANM-01-017-005}

[]{#MA-SOL-ANM-01-017-005}

La diferencia de salidas es $3|x-y|$, por lo que $\delta=\varepsilon/3$ sirve. El dominio es toda la recta, no acotado ni compacto por C16. La imagen también es toda la recta: $y$ tiene entrada $(y+2)/3$, así tampoco es acotada ni compacta. No refuta Heine–Cantor: éste da compacidad como condición suficiente, no necesaria para una función particular.

La traslación menos dos desaparece al restar valores y el factor tres determina la escala. La imagen se identifica por un despeje válido para cualquier salida real, no sólo observando que la función crece. La uniformidad puede coexistir con entrada y salida no acotadas. Heine–Cantor no declara que todo dominio de una uniforme deba ser compacto.

## 17.6. Proteger una cubierta concreta

[]{#MA-EX-ANM-01-017-006}

[]{#MA-SOL-ANM-01-017-006}

[]{#MA-SEC-ANM-01-017-002}

Para $z\le1/2$, $w\in K$ a distancia menor que $1/10$ satisface $w<z+1/10\le3/5$, y como $w\ge0>-1$ pertenece a $U_1$. Si $z>1/2$, $w>z-1/10>2/5$ y $w\le1<2$, luego está en $U_2$. Para $\lambda=1/5$, el centro $z=1/2$ tiene bola relativa que contiene $3/5$ y $2/5$. El primero no está en $U_1$ y el segundo no está en $U_2$; ningún miembro contiene la bola. Así ese radio falla.

**Retorno visual.** Véase [C17-F02](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El corte de centros en $1/2$ permite decidir qué abierto protege la bola relativa completa. Los extremos del dominio no molestan porque las entradas de la bola siguen en $[0,1]$. Para el radio propuesto mayor, ambos testigos están estrictamente dentro de la bola de centro medio, pero cada uno refuta un miembro distinto de la cubierta. Así se descarta toda posibilidad de que alguno contenga esa bola.

## 17.7. Familia de todos los triples

[]{#MA-EX-ANM-01-017-007}

[]{#MA-SOL-ANM-01-017-007}

$T$ contiene exactamente los triples $(a,i,r)$ con $a\in K$, $i\in I$, $r>0$ y $B(a,2r)\subseteq U_i$. Cada triple tiene componentes únicas y determina el abierto $B(a,r)$; esto es una regla funcional, no una elección entre radios. Para un $a$ arbitrario, cobertura da un $i$ y apertura un $\rho>0$; el triple $(a,i,\rho/2)$ pertenece a $T$ y su bola contiene $a$. La prueba establece cobertura punto por punto, sin definir un mapa de triples elegidos por centro.

La familia indexada por triples puede tener varias bolas con el mismo centro, y todas son admitidas si cumplen la protección doble. Para cobertura se necesita únicamente un triple para el centro fijado, obtenido de cobertura y apertura. La asignación de una bola a cada triple es una fórmula única. No es una selección de un triple preferido entre todas las posibilidades de cada centro.

## 17.8. Tomar un ínfimo demasiado pronto

[]{#MA-EX-ANM-01-017-008}

[]{#MA-SOL-ANM-01-017-008}

Positividad de todos los miembros no da ínfimo positivo: los recíprocos $1/(n+1)$ tienen ínfimo cero. Primero se aplica compacidad a las bolas pequeñas de todos los triples admisibles, obteniendo una lista finita no vacía $J$. El mínimo de sus radios es positivo por ser uno de los miembros. Si $z$ está a distancia menor que $r$ de un centro de la lista y $|w-z|<\lambda\le r$, entonces $|w-a|<2r$. La bola doble contenida en el abierto original reserva justamente ese margen; cobertura por bolas pequeñas sola no demuestra dicha inclusión.

La familia completa incluye radios arbitrariamente pequeños en muchos ejemplos y su ínfimo puede no proteger nada. La subcubierta finita conserva cobertura y permite tomar un mínimo positivo. La doble bola se utiliza después para mover la protección al centro que se está examinando. Son dos pasos distintos: reducir los datos y reservar margen para las distancias.

## 17.9. Levantar sin elegir ambientes

[]{#MA-EX-ANM-01-017-009}

[]{#MA-SOL-ANM-01-017-009}

C16 prueba que $W_i=(\mathbb R\setminus K)\cup A_i$ es abierto real y que $K\cap W_i=A_i$. La regla determina toda la familia por fórmula, y ésta cubre $K$. R2 da $\lambda>0$ para $W$. Para cada $z\in K$, algún $W_i$ contiene la bola relativa; al intersectar con $K$ se obtiene inclusión en $A_i$. No se seleccionó una familia de representantes ambientales. El vacío se resuelve con $\lambda=1$.

El levantamiento se define con la misma fórmula para todos los índices y no altera la selección de entradas dentro del compacto. Como $K$ es cerrado, esos levantamientos sí son abiertos reales. El número de Lebesgue ambiental protege bolas relativas en $K$, y la identidad de recorte las sitúa dentro de $A_i$. La prueba mantiene procedencia de índices y evita una familia de representantes elegidos.

## 17.10. Una cubierta finita sin margen

[]{#MA-EX-ANM-01-017-010}

[]{#MA-SOL-ANM-01-017-010}

Cada bola es abierta y contiene su centro; sus uniones pares e impares son abiertos y cubren $D$. Ninguna bola contiene otro $p_m$: para $m>n$, $p_n-p_m\ge p_n-p_{n+1}=1/[(n+1)(n+2)]=4r_n$; para $m<n$, la distancia al vecino anterior, cuando existe, es $1/[n(n+1)]>4r_n$. Así cada $p_n$ pertenece sólo al abierto de su paridad. Dado $\lambda>0$, elegimos $n$ con $p_n-p_{n+1}<\lambda$. La bola relativa centrada en $p_n$ contiene ambos puntos, de paridades opuestas, y no está contenida en ninguno de los dos abiertos. No hay escala positiva. El dominio omitió cero y no es compacto; finitud de una cubierta particular no sustituye compacidad.

Las bolas originales aíslan a sus propios puntos dentro de $D$. Eso hace que los dos abiertos asignen cada entrada exclusivamente según su paridad. Sin embargo, las distancias entre vecinos de distinta paridad tienden a cero. Cualquier escala positiva admite una bola relativa que contiene dos vecinos y no cabe en ninguno de los dos miembros. La cubierta es finita, pero el dominio no es compacto.

## 17.11. Las dos bolas del mismo índice

[]{#MA-EX-ANM-01-017-011}

[]{#MA-SOL-ANM-01-017-011}

[]{#MA-SEC-ANM-01-017-003}

La lista finita cubre $x$ con $B(a,r)$ y tiene $\delta\le r$. Entonces $|x-a|<r<2r$ y $|y-a|\le|y-x|+|x-a|<\delta+r\le2r$. El segundo punto puede estar fuera de $B(a,r)$, pero ambos cumplen la condición del índice en $B(a,2r)\cap K$, así sus salidas distan menos que $\varepsilon/2$ de $h(a)$. La triangular da error menor que $\varepsilon$. Afirmar pertenencia a la bola pequeña para $y$ gastaría una inclusión no probada.

**Retorno visual.** Véase [C17-F03](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La distancia de $y$ al centro de la bola se controla pasando por $x$, que sí está en la bola pequeña. El mínimo de radios aporta el margen para que ambos queden en la doble. Allí la admisibilidad controla cada salida respecto del mismo valor central. La suma de los dos presupuestos medios completa el error del par sin una inclusión adicional no demostrada.

## 17.12. Uniformizar sólo la restricción

[]{#MA-EX-ANM-01-017-012}

[]{#MA-SOL-ANM-01-017-012}

$K$ es cerrado/acotado, compacto por C16, y $f$ es continua en sus puntos relativamente a $D$. R3 hace uniforme la restricción sobre $K$, sin exigir que sea intervalo. Además $|x+y|\le4$ allí, por lo que $\delta=\varepsilon/4$ controla el error. Nada de esto uniformiza todo $D$; E002 ya refuta uniformidad del cuadrado en la recta.

Las dos piezas son cerradas y acotadas, de modo que su unión es compacta aunque no sea intervalo. El radio explícito usa una cota de $|x+y|$ válida para cualquier par de $K$, incluso si sus puntos pertenecen a piezas diferentes. La conclusión corresponde a esa restricción. Los infractores que escapan en $D$ siguen siendo posibles fuera del compacto.

## 17.13. La lectura por cubiertas de salida

[]{#MA-EX-ANM-01-017-013}

[]{#MA-SOL-ANM-01-017-013}

Cada $A_a$ es preimagen relativa de un intervalo abierto y contiene $a$, así forman cubierta. Se levantan por $W_a=(\mathbb R\setminus K)\cup A_a$ y R2 da una escala $\lambda>0$ antes de los puntos $x,y$. Para $x\in K$, R2 proporciona un índice $a$ que contiene su bola relativa. Si $|x-y|<\lambda$, tanto $x$ como $y$ están en ella y por tanto en $A_a$. Ambos errores respecto de $h(a)$ son menores que $\varepsilon/2$, y su suma controla la diferencia. No se construye un selector $x\mapsto a_x$. Para $K$ vacío sirve cualquier radio.

Las preimágenes se definen para todos los centros por una condición de salida y quedan abiertas relativas por continuidad. El número de Lebesgue se obtiene antes del par solicitado. Para ese par se fija sólo un miembro que proteja la bola de $x$, y ésta contiene también a $y$. El índice puede variar con $x$, pero el radio no, que es la conclusión uniforme.

## 17.14. Acotación sin frontera incluida

[]{#MA-EX-ANM-01-017-014}

[]{#MA-SOL-ANM-01-017-014}

Tomamos $x_n=1/(n+2)$ y $y_n=1/(n+3)$, ambos del dominio desde cero. La distancia es $1/[(n+2)(n+3)]$, tendente a cero, pero las salidas son $n+2,n+3$ y difieren uno. Para $\varepsilon_0=1$, todo radio positivo admite un índice con distancia menor, refutando uniformidad. El dominio es acotado pero no cerrado: cero es adherente y está omitido. Falta compacidad, no continuidad de la función en el dominio efectivo.

Los pares están en el dominio efectivo desde el primer término y sus diferencias se calculan exactamente. Una precisión fija uno se infringe para entradas con distancia tan pequeña como se quiera. Acotación del dominio no basta para Heine–Cantor: también hace falta cerradura para compacidad. La discontinuidad no se afirma en cero, porque cero no es una entrada del recíproco dado.

## 17.15. Vacuidad y prueba sin rutas

[]{#MA-EX-ANM-01-017-015}

[]{#MA-SOL-ANM-01-017-015}

Para $K$ no vacío, una subcubierta no puede tener conjunto de índices vacío; por ello sus radios forman conjunto finito no vacío y poseen mínimo positivo. Para $K$ vacío no se toma mínimo: $\delta=1$ satisface la condición vacía. La prueba define todos los pares admisibles, verifica cobertura con testigos individuales y usa una aplicación de compacidad seguida de datos finitos; no fabrica rutas ni selecciona radios por todos los centros. Una prueba que fabrica pares malos para cada escala necesita justificar esa selección numerable, como en la recíproca condicional de R6.

La no vacuidad de $K$ obliga a que una reducción que lo cubre contenga algún índice. Ese hecho permite el mínimo de radios positivos. Para el vacío se elige uno directamente y no se usa ese paso. La prueba por cubiertas usa existencias puntuales y un conjunto finito, mientras una ruta de pares malos exige reunir testigos para todas las escalas naturales.

## 17.16. Existencia y orden del módulo

[]{#MA-EX-ANM-01-017-016}

[]{#MA-SOL-ANM-01-017-016}

[]{#MA-SEC-ANM-01-017-004}

Si $|f|\le B$, toda diferencia está entre cero y $2B$. Para cada $t\ge0$, los pares diagonales aportan cero, por lo que el conjunto es no vacío y tiene supremo. Si $s\le t$, todos los pares admitidos a escala $s$ también lo son a escala $t$, así $\omega(s)\le\omega(t)$. A escala cero sólo hay pares iguales y el módulo vale cero. Toda diferencia admitida es a lo sumo el supremo. Para vacío se define módulo cero por convención; no se atribuye un supremo real al conjunto vacío.

La cota global produce una barrera uniforme $2B$ para errores, no sólo para un par. Los pares diagonales dan no vacuidad a cada escala. El supremo domina cada diferencia sin prometer un par maximizador. La convención para el vacío se declara aparte porque completitud real no entrega un supremo del conjunto vacío.

## 17.17. Supremo y presupuesto estricto

[]{#MA-EX-ANM-01-017-017}

[]{#MA-SOL-ANM-01-017-017}

El supremo de $[0,\varepsilon)$ es $\varepsilon$, así la estrictitud no pasa así al supremo. Se pide primero error $\varepsilon/2$ a uniformidad; para $0<t<\delta$, el supremo es a lo sumo $\varepsilon/2<\varepsilon$, lo que prueba el límite cero. Recíprocamente, dado $\varepsilon$, el límite da $\eta>0$ y $\omega(t)<\varepsilon$ para $0<t<\eta$. Fijamos $t=\eta/2$ y $\delta=t$. Todo par de distancia menor que $\delta$ tiene error a lo sumo $\omega(t)<\varepsilon$. Se conserva el orden de los cuantificadores.

La definición del módulo admite distancias menores o iguales que $t$, mientras uniformidad controla distancias estrictamente menores que $\delta$. Por eso se toma $t<\delta$ al usarla. El presupuesto medio conserva margen cuando se pasa al supremo. En la recíproca se fija una escala positiva concreta con módulo pequeño antes de verificar cualquier pareja.

## 17.18. Módulo exacto del cuadrado

[]{#MA-EX-ANM-01-017-018}

[]{#MA-SOL-ANM-01-017-018}

Si $0\le v\le u\le1$, $d=u-v\le t\le1$, la diferencia es $d(2u-d)\le d(2-d)\le t(2-t)$ porque la última diferencia es $(t-d)(2-t-d)\ge0$. El par $1,1-t$ alcanza $2t-t^2$ para $0\le t\le1$. Si $t\ge1$, la diferencia no supera uno y el par $1,0$ lo alcanza. Así el módulo es $2t-t^2$ en la primera escala y uno después. Siempre está bajo $2t$; para $0<t\le1$ la mejora exacta es $t^2$.

**Retorno visual.** Véase [C17-F04](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La cota se demuestra primero para un par arbitrario ordenado, con separación $d\le t$. El factor algebraico $(t-d)(2-t-d)$ es no negativo en la escala hasta uno, lo que compara su error con el candidato exacto. Un par explícito alcanza después la cota y acredita igualdad. Más allá del diámetro del dominio ya se admiten todos los pares y el módulo queda constante en uno.

## 17.19. Una raíz y su módulo

[]{#MA-EX-ANM-01-017-019}

[]{#MA-SOL-ANM-01-017-019}

R1 da diferencia a lo sumo $\sqrt{|x-y|}$, por tanto $\omega(t)\le\sqrt t$ para $0\le t\le1$. El par $t,0$ alcanza esa cota. Para $t\ge1$, todas las diferencias son a lo sumo uno y el par $1,0$ la alcanza. El módulo es $\sqrt t$ hasta uno y uno después. Tiende a cero, pero su cociente por $t$ es $1/\sqrt t$ cerca de cero y no admite cota lineal uniforme. El cuadrado sí tiene módulo a lo sumo $2t$.

El par que alcanza $\sqrt t$ está dentro del segmento sólo para $t\le1$, y por eso se separa la escala mayor. Allí el par de extremos ya alcanza toda la variación de salida. El módulo de la raíz tiende a cero, lo que confirma uniformidad. Su crecimiento como raíz de la escala impide una barrera lineal común cerca de cero.

## 17.20. Valores no acotados y módulo finito

[]{#MA-EX-ANM-01-017-020}

[]{#MA-SOL-ANM-01-017-020}

La identidad tiene valores que recorren toda la recta y no están acotados. A escala $t\ge0$, las diferencias admitidas están entre cero y $t$, y el par $0,t$ alcanza $t$, así el módulo es finito e igual a $t$. Directamente, $\delta=\varepsilon$ da uniformidad. La hipótesis de acotación de R4 era suficiente para construir un módulo real global sin más análisis, no necesaria en todos los ejemplos.

El módulo examina diferencias de salida a una distancia fijada, no el conjunto de salidas individuales. Para la identidad esas diferencias nunca superan $t$ y una pareja separada exactamente $t$ alcanza la cota. Así hay módulo finito a cada escala aunque las salidas no admitan cota global. El ejemplo precisa el carácter suficiente de la hipótesis de acotación en R4.

## 17.21. Radios para una suma

[]{#MA-EX-ANM-01-017-021}

[]{#MA-SOL-ANM-01-017-021}

[]{#MA-SEC-ANM-01-017-005}

Si $a\ne0$, pedimos a $f$ error menor que $\varepsilon/(2|a|)$ y obtenemos un radio; si $a=0$, el término tiene error cero y usamos radio uno para él. Hacemos lo mismo con $g,b$. El mínimo de ambos radios positivos sirve para todos los pares y la diferencia de $af+bg$ es a lo sumo la suma de los dos errores escalados, cada uno menor que $\varepsilon/2$ cuando no es cero. La suma es menor que $\varepsilon$.

Las constantes no nulas multiplican los errores y requieren dividir el presupuesto por su magnitud. Una constante cero elimina su sumando y puede recibir cualquier radio auxiliar positivo. El mínimo garantiza ambos controles antes de conocer las entradas. La triangular permite combinar los errores escalados sin suponer cotas globales de los valores de $f$ y $g$.

## 17.22. Factores que amplifican errores

[]{#MA-EX-ANM-01-017-022}

[]{#MA-SOL-ANM-01-017-022}

Pedimos errores menores que $\eta=\varepsilon/(M_f+M_g+1)$ a ambas funciones y tomamos el mínimo de sus radios. La identidad de diferencias del producto da cota $(M_f+M_g)\eta<\varepsilon$, incluidos sumandos nulos. En $\mathbb R$, ambos factores identidad son uniformes y no acotados, pero su producto cuadrado falla uniformidad. En cambio, identidad por constante uno es uniforme aunque el primer factor sea no acotado. La regla declara condiciones suficientes y el ejemplo sólo refuta una regla universal sin ellas.

La identidad de producto separa cada cambio de factor y deja un valor del otro como multiplicador. Las cotas globales y el presupuesto común impiden amplificación sin control. El uno añadido al denominador conserva positividad incluso si ambas barreras valen cero. Los dos ejemplos finales distinguen perder una garantía universal de afirmar que todo producto sin esas cotas debe fallar.

## 17.23. Un cociente sobre dos piezas

[]{#MA-EX-ANM-01-017-023}

[]{#MA-SOL-ANM-01-017-023}

En $K$, $|f|\le3$, $g\ge1$, $|f(x)-f(y)|=|x-y|$, y $|g(x)-g(y)|\le4|x-y|$. Sea $d=|x-y|$. La identidad $f(x)/g(x)-f(y)/g(y)=(f(x)-f(y))/g(x)+f(y)(1/g(x)-1/g(y))$ da error a lo sumo $d+3\cdot4d=13d$, porque los denominadores tienen magnitud al menos uno. Por tanto $\delta=\varepsilon/13$ sirve para todos los pares, incluso en piezas distintas. El cociente está definido en todo $K$.

El margen del denominador vale uno en todas las entradas, incluidas las dos piezas. La identidad de recíprocos acota su diferencia por la del cuadrado, a lo sumo cuatro veces la distancia. El numerador tiene diferencia igual a la distancia y magnitud a lo sumo tres. Reunir ambos términos da el control trece, suficiente para un radio común sin exigir que sea óptimo.

## 17.24. El orden inverso de tolerancias

[]{#MA-EX-ANM-01-017-024}

[]{#MA-SOL-ANM-01-017-024}

Primero uniformidad de $g$ para $\varepsilon$ da $\eta>0$. Después uniformidad de $f$ para $\eta$ da $\delta>0$. Distancia de entrada menor que $\delta$ produce salidas de $f$ a distancia menor que $\eta$, y por tanto error final menor que $\varepsilon$. Basta control de $g$ sobre $f[D]$. Si $D=E=\mathbb R$, $f$ identidad es uniforme, $g$ cuadrado es continua pero no uniforme, y la composición también es cuadrado no uniforme. La continuidad puntual exterior no da una tolerancia intermedia común.

**Retorno visual.** Véase [C17-F05](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La tolerancia intermedia debe servir para cualquier par de salidas de la interior. Continuidad puntual de la exterior permitiría que esa tolerancia cambiara al cambiar la salida central y no satisface ese requisito. La identidad seguida del cuadrado mantiene uniformidad de la interior y continuidad de la exterior, pero falla uniformidad de la composición. El ejemplo refuta exactamente la sustitución propuesta.

## 17.25. Inversa uniforme sin control lineal

[]{#MA-EX-ANM-01-017-025}

[]{#MA-SOL-ANM-01-017-025}

C16 hace compacta $H=f[K]$ y prueba continuidad de la inversa $h:H\to K$. Retipar su salida a $\mathbb R$ conserva continuidad, por usar la misma distancia; Heine–Cantor la hace uniforme sobre $H$. El vacío también queda incluido. Para $f(x)=x^2$ sobre $[0,1]$, la inyectividad sigue del orden no negativo, su imagen es $[0,1]$ por raíces C10 y su inversa es $\sqrt y$. R1 prueba que ésta es uniforme y no Lipschitz en ese dominio.

La continuidad inversa se obtiene primero por transporte de cerrados en C16, con dominio en la imagen. Esa imagen es compacta por continuidad de la directa. Heine–Cantor añade uniformidad de la inversa allí. La raíz sobre $[0,1]$ cumple esta conclusión con radio cuadrático aunque no disponga de una constante Lipschitz.

## 17.26. Rutas que no convergen

[]{#MA-EX-ANM-01-017-026}

[]{#MA-SOL-ANM-01-017-026}

[]{#MA-SEC-ANM-01-017-006}

La distancia de entrada es $1/(n+1)$, tendente a cero. La diferencia de cuadrados es $2+1/(n+1)^2$, que nunca baja de dos y por tanto no tiende a cero. Si el cuadrado fuera uniforme, la dirección directa R6 obligaría a que esas diferencias tendieran a cero, contradicción. Ninguna ruta de entrada converge o es acotada; la dirección directa no lo exigía. Los pares están dados por fórmula desde $n=0$, sin selección adicional.

La pequeña separación compensa exactamente la entrada creciente en el término lineal de la diferencia de cuadrados. El error queda mayor o igual que dos para todos los índices. Esto infringe la consecuencia directa necesaria de uniformidad para las rutas dadas. No se necesita convergencia individual, acotación ni seleccionar testigos de conjuntos abstractos.

## 17.27. Dos familias y dos selecciones

[]{#MA-EX-ANM-01-017-027}

[]{#MA-SOL-ANM-01-017-027}

El fallo de uniformidad fija $\varepsilon_0>0$. Para cada $n$, $A_n$ contiene entradas que tienen algún compañero a distancia menor que $1/(n+1)$ y error al menos $\varepsilon_0$; negación garantiza no vacuidad. CC(R) selecciona $x_n\in A_n$. Luego $B_n$ reúne los compañeros de ese $x_n$ con ambas propiedades y es no vacío; CC(R) selecciona $y_n\in B_n$. Estas rutas tienen distancia tendente a cero y salida separada, contradiciendo la propiedad de pares dada. Sólo esta recíproca usa las selecciones. Heine–Cantor fue demostrado directamente por una cubierta explícita y finitud, sin recurrir a la recíproca.

La primera familia contiene entradas que admiten algún compañero infractor; su selección no determina todavía quién es ese compañero. La segunda familia se define a partir de la primera ruta ya seleccionada y permite completar los pares. CC(R) respalda ambas funciones de términos. La prueba por cubiertas de Heine–Cantor es independiente y conserva su conclusión sin adoptar esta premisa adicional.

## 17.28. Una enumeración de pares malos

[]{#MA-EX-ANM-01-017-028}

[]{#MA-SOL-ANM-01-017-028}

Fijamos $\varepsilon_0$ de la negación. Para cada $n$, existe un par malo en $D$ y, por sobreyectividad, índices $j,k$ que lo representan. El conjunto de $j$ para los que existe algún $k$ malo a escala $1/(n+1)$ es no vacío; tomamos su mínimo $j_n$. Para ese índice, el conjunto de compañeros $k$ es no vacío y tiene mínimo $k_n$. Los mínimos únicos definen $x_n=e(j_n)$ y $y_n=e(k_n)$, que tienen distancia menor que $1/(n+1)$ y error al menos $\varepsilon_0$. Se usa la enumeración dada, sin inferirla para dominios arbitrarios.

La negación asegura al menos un par a cada escala, y la sobreyección representa sus dos miembros por índices. El mínimo exterior fija una primera entrada que tenga compañero y el mínimo interior fija uno para ella. No se exige que los mínimos aumenten con la escala: construyen dos rutas, no una extracción. Las cotas de distancia y error son las propiedades que esas rutas deben conservar.

## 17.29. Preservar una ruta de Cauchy

[]{#MA-EX-ANM-01-017-029}

[]{#MA-SOL-ANM-01-017-029}

Para error $\varepsilon$ elegimos el radio uniforme $\delta$. La condición Cauchy de entrada da $N$ con todas las distancias entre términos posteriores menores que $\delta$; uniformidad hace todas las diferencias de salida posteriores menores que $\varepsilon$. Para el cuadrado, cada ruta Cauchy es acotada, digamos $|x_n|\le M$ con $M>0$. Entonces $|x_n^2-x_m^2|\le2M|x_n-x_m|$, que convierte su condición Cauchy de entrada en la de salida. Sin embargo el cuadrado falla uniformidad en toda la recta, por E002/E026. No se confundió una ruta acotada particular con control sobre todo el dominio.

La condición Cauchy entrega un corte que vale para todos los pares tardíos, y el radio uniforme lo transforma en control Cauchy de salida. Para el cuadrado, la barrera $M$ pertenece a la ruta concreta y puede cambiar entre rutas diferentes. Ese control individual no ofrece un radio para toda la recta. Así preservación de rutas no equivale a uniformidad global en un dominio arbitrario.

## 17.30. Pares recíprocos y una frontera

[]{#MA-EX-ANM-01-017-030}

[]{#MA-SOL-ANM-01-017-030}

La distancia de entrada es $1/[(n+2)(n+3)]\to0$. Bajo identidad la diferencia es la misma y tiende a cero, conforme a uniformidad. Bajo recíproco la diferencia vale uno para todo $n$, refutando uniformidad por R6 directo. Las dos rutas convergen a cero, que está fuera del dominio; no se evalúa el recíproco en ese punto exterior. El test controla pares dentro del dominio efectivo.

**Retorno visual.** Véase [C17-F06](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La identidad transporta la separación exactamente y su diferencia de salida tiende a cero. El recíproco transforma los mismos argumentos en naturales consecutivos con diferencia uno. El test muestra que proximidad de entradas no se transporta uniformemente para esa función. Ambas evaluaciones se realizan dentro de $(0,1]$, sin asignar un valor a la frontera ausente.

## 17.31. Construir el corte de frontera

[]{#MA-EX-ANM-01-017-031}

[]{#MA-SOL-ANM-01-017-031}

[]{#MA-SEC-ANM-01-017-007}

Adherencia da entrada en cada bola. Fijamos el radio uniforme $\delta_0$ para error uno y $r_0=\delta_0/4$. Para este $p$, una entrada $a$ en la bola inicial acota todas las salidas allí por $f(a)\pm1$, porque la distancia entre dos entradas de ella es menor que $2r_0<\delta_0$. Todas las imágenes menores son no vacías/acotadas. Los ínfimos forman conjunto no vacío acotado superiormente por $U_{p,r_0}$, así su supremo $F(p)$ existe. Supera cada ínfimo. Para un $r$ fijado y cualquier $s$, una salida de la imagen a escala $\min(r,s)$ da $L_{p,s}\le U_{p,r}$. Por tanto ese supremo acota todo el corte y $F(p)\le U_{p,r}$. No se seleccionó entrada por todos los puntos o radios.

La cota inicial se obtiene para un punto de frontera fijado y se conserva al reducir radios. Para comparar dos escalas se usa su mínimo, cuya imagen local no es vacía y pertenece a ambas imágenes. Eso hace que cualquier supremo local sea cota de todos los ínfimos del corte. La fórmula de $F$ se define con esas cotas, sin escoger una entrada o sucesión para cada radio.

## 17.32. Anchuras que determinan un único real

[]{#MA-EX-ANM-01-017-032}

[]{#MA-SOL-ANM-01-017-032}

Para cada valor $v$, todos los valores son a lo sumo $v+\eta$, así $U\le v+\eta$. Entonces $U-\eta$ es cota inferior y no supera $L$, dando $U-L\le\eta$. Uniformidad hace arbitrariamente pequeñas estas anchuras al disminuir el radio. Dos candidatos distintos a distancia $d>0$ no caben en un intervalo de anchura a lo sumo $d/2$, por tanto el candidato es único. Si $p\in D$, $f(p)$ pertenece a cada imagen local y queda entre su ínfimo/supremo; por unicidad coincide con el corte $F(p)$.

Las diferencias estrictamente menores que $\eta$ producen una anchura sólo menor o igual que $\eta$ al pasar a extremos. Esa conclusión basta porque la uniformidad permite pedir un presupuesto más pequeño que la distancia entre dos candidatos. La coincidencia con $f$ utiliza además que la salida central pertenece a todas las imágenes cuando el centro está en $D$. Se demuestra existencia por el corte y unicidad por anchuras, en pasos distintos.

## 17.33. Uniformidad y unicidad de la extensión

[]{#MA-EX-ANM-01-017-033}

[]{#MA-SOL-ANM-01-017-033}

Para $\varepsilon>0$ tomamos radio $\delta$ de $f$ para error $\varepsilon/3$ y fijamos $\Delta=\delta/3$. Dados $p,q$ del cierre a distancia menor que $\Delta$, usamos $0<r\le\min(r_0,\delta/6)$. Todo par cruzado de entradas de sus bolas tiene distancia menor que $2r+\delta/3\le2\delta/3<\delta$. Las cotas de supremo/ínfimo dan $U_{p,r}-L_{q,r}\le\varepsilon/3$ y la desigualdad simétrica; los cortes entre esos extremos satisfacen error a lo sumo $\varepsilon/3<\varepsilon$. Para una extensión continua $G$, su radio en un $p$ para error $\varepsilon/2$ sitúa todas las salidas locales en la banda de $G(p)$. Sus ínfimos/supremos y el corte quedan en la banda cerrada, luego $|F(p)-G(p)|\le\varepsilon/2<\varepsilon$. Para todo $\varepsilon$ esto fuerza igualdad; no se usa uniformidad de $G$ para unicidad.

El radio global $\Delta$ se fija antes de $p,q$ y el radio local $r$ asegura que cualquier par cruzado de sus bolas quede en la escala original. Las cotas de supremo e ínfimo conservan el error con desigualdades no estrictas, cubiertas por el presupuesto reservado. Para unicidad basta un control puntual de la otra extensión en cada $p$. Así no se exige que una extensión continua rival sea uniforme como hipótesis.

## 17.34. Extender y no poder extender

[]{#MA-EX-ANM-01-017-034}

[]{#MA-SOL-ANM-01-017-034}

Identidad y raíz son uniformes en $(0,1]$, por R1, y sus extensiones tienen valor cero en la frontera: las funciones identidad y raíz ya son continuas en $[0,1]$ y coinciden en el dominio, así unicidad R7 las identifica. Si el recíproco tuviera extensión real continua $G$ con valor $c$ en cero, para error uno existiría $\rho>0$ con $|G(x)-c|<1$ para $0\le x<\rho$. Elegimos $n$ con $1/(n+1)<\min(\rho,1)$ y $n+1>|c|+1$. Entonces $G(1/(n+1))=n+1$ tiene diferencia respecto de $c$ mayor que uno, contradicción. Sólo se usan entradas positivas válidas y un valor finito propuesto en la frontera.

**Retorno visual.** Véase [C17-F07](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las extensiones conocidas conservan los valores originales y son continuas también en cero, por lo que la unicidad determina su valor de frontera. El recíproco, en cambio, produce valores que superan cualquier banda alrededor de un valor real propuesto. Arquimedianidad permite una entrada positiva dentro del radio de continuidad y con salida demasiado grande. La contradicción muestra imposibilidad de una extensión real continua, no sólo fracaso de una fórmula candidata.

## 17.35. Uniformidad en un dominio acotado

[]{#MA-EX-ANM-01-017-035}

[]{#MA-SOL-ANM-01-017-035}

La dirección uniforme a extensión continua es R7, incluso vacío. Recíprocamente, el cierre es cerrado y sigue acotado: si $D\subseteq[-M,M]$, su cierre está en ese cerrado. Heine–Borel lo hace compacto; una extensión continua $G$ sobre él es uniforme por R3, y su restricción $f$ lo es por R1. Para vacío sólo hay función vacía y extensión vacía. La compacidad se usa en esta recíproca sobre dominio acotado; existencia R7 no exigía acotación global del dominio.

La existencia de extensión uniforme al cierre no necesita acotación del dominio. La acotación sí se usa al volver desde una extensión meramente continua: junto con cerradura del cierre produce compacidad y habilita Heine–Cantor. Después la restricción conserva el radio uniforme. En el vacío ambas funciones y sus dominios son vacíos y la equivalencia se resuelve directamente.

## 17.36. Construir la poligonal

[]{#MA-EX-ANM-01-017-036}

[]{#MA-SOL-ANM-01-017-036}

[]{#MA-SEC-ANM-01-017-008}

Heine–Cantor para error $\varepsilon/2$ da $\delta>0$. Arquimedianidad permite un entero $n\ge1$ con $(b-a)/n<\delta$. Con $h=(b-a)/n$ y $t_j=a+jh$, definimos en cada celda $P(x)=(1-\theta)f(t_j)+\theta f(t_{j+1})$, $\theta=(x-t_j)/h$. En el extremo derecho $\theta=1$ y en el izquierdo de la siguiente celda $\theta=0$, por lo que ambas ramas dan el valor del nodo compartido. Cada rama afín es continua; las celdas forman cubierta finita por cerrados relativos y C14 da continuidad del pegado. Se usaron sólo los valores finitos en los nodos y no una capacidad computable de evaluarlos.

La escala uniforme se obtiene para un presupuesto común antes de construir nodos. Una malla suficientemente fina mantiene cada celda dentro de esa escala. Las fórmulas afines comparten valores en los nodos y por ello definen una sola función. El pegado finito sobre celdas cerradas acredita continuidad sin usar derivadas ni presuponer un algoritmo de evaluación de todas las muestras.

## 17.37. Controlar todo lo que queda entre nodos

[]{#MA-EX-ANM-01-017-037}

[]{#MA-SOL-ANM-01-017-037}

Dentro de una celda, ambos extremos distan a lo sumo $h<\delta$ de $x$; los dos errores de $f$ son menores que $\varepsilon/2$. La triangular para su combinación con pesos no negativos de suma uno da error menor que $\varepsilon/2$, también si un peso es cero porque el otro es uno. Por tanto el supremo de errores es a lo sumo $\varepsilon/2<\varepsilon$. Además $|P-f|$ es continua en compacto no vacío y alcanza máximo por C16; como es uno de los errores puntuales, ese máximo es incluso menor que $\varepsilon/2$. En el degenerado se toma constante y no se divide por cero.

Los pesos suman uno y no son negativos, así la interpolación combina dos errores bajo el mismo presupuesto. Los nodos, donde uno de los pesos es cero, siguen cumpliendo la estimación. Pasar al supremo sólo conserva una desigualdad no estricta, pero el presupuesto medio deja error global menor que $\varepsilon$. Si se usa que el error continuo alcanza máximo en el compacto, ese máximo también hereda la cota puntual estricta.

## 17.38. Certificado exacto de cuatro celdas

[]{#MA-EX-ANM-01-017-038}

[]{#MA-SOL-ANM-01-017-038}

Con $h=1/4$ y $x=t+\theta h$, expandir la interpolación de los cuadrados de los extremos y restar $(t+\theta h)^2$ da $\theta(1-\theta)h^2$. Es no negativo y a lo sumo $h^2/4=1/64$, porque $(2\theta-1)^2\ge0$. La igualdad exige $\theta=1/2$. Los cuatro medios son $1/8,3/8,5/8,7/8$, y en cada uno se alcanza $1/64$. No se emplea teoría diferencial ni convexidad futura.

**Retorno visual.** Véase [C17-F08](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html#fig-anm-c17-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La fórmula exacta cancela los términos que dependen del extremo izquierdo de la celda. Queda el mismo error según el peso $\theta$ en todas las celdas. La identidad cuadrática de $\theta(1-\theta)$ localiza la igualdad únicamente en su medio. Así se obtienen el valor máximo y todos sus argumentos, mientras en cada nodo la poligonal coincide exactamente con el cuadrado.

## 17.39. Muestras iguales y errores arbitrarios

[]{#MA-EX-ANM-01-017-039}

[]{#MA-SOL-ANM-01-017-039}

Elegimos una celda de longitud positiva $[u,v]$ entre nodos consecutivos y su medio $m=(u+v)/2$. Fuera de ella ponemos cero; en $[u,m]$ ponemos $H(x-u)/(m-u)$ y en $[m,v]$ ponemos $H(v-x)/(v-m)$. Los denominadores son positivos y las ramas coinciden en valores cero en los extremos y $H$ en el medio. El pegado finito C14 da continuidad, y todos los nodos siguen teniendo valor cero. La poligonal interpolante es cero y su error en $m$ es $H$, arbitrario. Los datos de muestras sin una escala para la función entre ellas no certifican error; Heine–Cantor da escala para cada función dada, no para toda la clase con la misma malla.

La celda de longitud positiva existe porque la malla recorre un segmento no degenerado. Sus dos mitades tienen denominadores positivos, y el acuerdo en el medio y extremos hace continua la función triangular. Ningún nodo interior de esa celda existe entre consecutivos, así todas las muestras siguen siendo cero. La altura demuestra que una malla fija no certifica el error de toda función continua que coincida en esos datos.

## 17.40. Elegir una malla a partir de tolerancia

[]{#MA-EX-ANM-01-017-040}

[]{#MA-SOL-ANM-01-017-040}

El certificado exacto da máximo $1/(4n^2)$, así basta $n>1/(2\sqrt\varepsilon)$ con $n\ge1$. La raíz de $\varepsilon$ es positiva; arquimedianidad garantiza tal entero. Si sólo usamos Lipschitz dos, para error local $\varepsilon/2$ podemos tomar $\delta=\varepsilon/4$, y R8 pide $1/n<\varepsilon/4$, es decir $n>4/\varepsilon$. Ambas condiciones son suficientes, pero la exacta aprovecha la regla algebraica del cuadrado y puede usar muchas menos celdas. No se concluye que esa mejora exista para una continua arbitraria.

El error exacto de una malla de $n$ celdas es $h^2/4=1/(4n^2)$, y la desigualdad estricta pide un entero que supere el umbral indicado. La garantía Lipschitz sólo usa una cota lineal y el presupuesto medio, por eso impone una condición más conservadora. Son dos certificados suficientes basados en información diferente. La mejora cuadrática procede de la identidad algebraica de esta función particular.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-microcontroles.html)
