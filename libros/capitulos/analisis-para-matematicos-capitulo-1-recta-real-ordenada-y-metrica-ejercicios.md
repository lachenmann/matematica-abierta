---
title: "Ejercicios — Capítulo 1"
content-id: MA-BCH-0087
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-001-EJERCICIOS
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-09-30
date-modified: 2026-09-30
areas: [analisis]
level: universitario
topics: [analisis-real, orden, topologia]
prerequisites: []
related: [MA-BOK-0010]
provenance:
  type: original
  sources:
    - "Manuscrito ANM C01; referencias de contraste en la portada del libro."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Capítulo 1](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica.md) · [Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Ejercicios](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-microcontroles.md)

# Ejercicios — Capítulo 1

## §1.1. La misma recta, varias estructuras

[]{#MA-EX-ANM-01-001-001}

### 1. Lo que el orden no dice

Un estudiante afirma:

> Si $x<y<z$, entonces $y$ está a la misma distancia de $x$ que de $z$.

Decide si la afirmación es correcta. Si es falsa, da dos ternas numéricas con el mismo patrón de orden $x<y<z$: una en la que las dos separaciones sean iguales y otra en la que no lo sean. Explica qué información proporciona realmente el orden.

[]{#MA-EX-ANM-01-001-002}

### 2. Reflejar no destruye toda la información

Considera los tres puntos $-2$, $1$ y $5$ sobre la recta real y después su imagen al reflejarlos respecto del origen.

1. Escribe los tres puntos reflejados y ordénalos de menor a mayor.
2. Compara, antes y después de la reflexión, las separaciones entre cada par de puntos.
3. Un estudiante concluye: «Como cambió el orden izquierda–derecha, cambió también toda la información geométrica». Diagnostica con precisión qué parte de esa conclusión es falsa.

No basta con responder «la reflexión conserva distancias»: muestra la comparación numérica que sostiene tu diagnóstico.

[]{#MA-EX-ANM-01-001-003}

### 3. Un orden fijo, separaciones variables

Fija los extremos $0$ y $1$, y coloca entre ellos un punto $t$ con $0<t<1$.

1. Explica por qué el patrón de orden $0<t<1$ no cambia al variar $t$ dentro de $(0,1)$.
2. Compara la separación de $t$ respecto de $0$ con su separación respecto de $1$ en los tres casos $0<t<\tfrac12$, $t=\tfrac12$ y $\tfrac12<t<1$.
3. Resume qué permanece y qué cambia cuando $t$ recorre el intervalo $(0,1)$.

El objetivo no es resolver una desigualdad aislada, sino usar una familia completa para distinguir información de orden e información métrica.

[]{#MA-EX-ANM-01-001-004}

### 4. Tres capas sobre los mismos números

Supón que tres números reales $a,b,c$ satisfacen simultáneamente

$$
a+b=c
$$

y

$$
a<b.
$$

Alguien sostiene que esos dos datos bastan para decidir cuál de $a$ o $b$ está más cerca de $c$.

1. Construye un ejemplo que satisfaga las dos condiciones y en el que $b$ esté más cerca de $c$ que $a$.
2. Construye otro ejemplo que satisfaga las mismas dos condiciones y en el que $a$ esté más cerca de $c$ que $b$.
3. Identifica qué parte de la información usada en el problema es algebraica, cuál pertenece al orden y cuál es métrica.
4. Explica por qué los dos primeros datos, aun tomados conjuntamente, no determinan por sí solos la tercera clase de información.

## §1.2. Orden: izquierda, derecha y estar entre

[]{#MA-EX-ANM-01-001-005}

### 5. Una condición, tres escrituras

Sea

$$
-4\le x<3.
$$

1. Escribe el conjunto de valores posibles de $x$ en notación de intervalo.
2. Describe la misma región con palabras, indicando qué ocurre en cada extremo.
3. Decide si cada uno de los puntos $-4$, $0$ y $3$ pertenece al conjunto y justifica tu respuesta a partir de la desigualdad original, no sólo de la notación del intervalo.

[]{#MA-EX-ANM-01-001-006}

### 6. Dos fronteras, cuatro regiones

Fija números reales $a<b$. Para cada una de las condiciones siguientes:

1. escríbela como pertenencia a un intervalo;
2. indica qué extremos quedan incluidos;
3. explica qué cambia —y qué no cambia— al pasar de una línea a la siguiente.

$$
a<x<b,
$$

$$
a\le x<b,
$$

$$
a<x\le b,
$$

$$
a\le x\le b.
$$

No trates los cuatro casos como reglas independientes: organiza tu respuesta a partir de la información que codifican $<$ y $\le$ en cada frontera.

[]{#MA-EX-ANM-01-001-007}

### 7. ¿Puede incluirse el infinito?

Un estudiante escribe

$$
[2,\infty]
$$

para representar todos los números reales $x$ tales que $x\ge2$, y explica: «Uso corchete en $\infty$ porque quiero incluir todos los valores hacia la derecha».

1. Diagnostica el error.
2. Escribe la notación correcta.
3. Explica por qué el símbolo $\infty$ no se comporta como un extremo real ordinario del intervalo.
4. Da la notación correcta para la condición $x<2$ y compárala con la anterior.

[]{#MA-EX-ANM-01-001-008}

### 8. El mismo tramo sin elegir orientación

Sean $p,q\in\mathbb R$, sin suponer cuál de los dos es menor, y considera la condición

$$
\min\{p,q\}\le x\le\max\{p,q\}.
$$

1. Describe verbalmente qué región de la recta selecciona.
2. Escribe esa región como intervalo usando sólo $\min\{p,q\}$ y $\max\{p,q\}$.
3. Reescribe la condición en los dos casos posibles: $p\le q$ y $q\le p$.
4. Explica por qué la formulación con mínimo y máximo permite hablar del tramo entre $p$ y $q$ sin decidir de antemano cuál está a la izquierda.

[]{#MA-EX-ANM-01-001-009}

### 9. Dos formas equivalentes de «estar entre»

Sean $x,y,z\in\mathbb R$. Demuestra que

$$
\min\{x,z\}\le y\le\max\{x,z\}
$$

si y sólo si se cumple al menos una de las dos cadenas

$$
x\le y\le z
$$

o

$$
z\le y\le x.
$$

Tu demostración debe cubrir explícitamente los dos órdenes posibles entre $x$ y $z$ y explicar por qué no hace falta una tercera posibilidad.

## §1.3. Valor absoluto: distancia al origen

[]{#MA-EX-ANM-01-001-010}

### 10. Una distancia con centro desplazado

Interpreta geométricamente la ecuación

$$
|x-3|=5.
$$

1. Exprésala en palabras como una condición de distancia respecto de un centro.
2. Determina todos los valores de $x$.
3. Explica por qué aparecen exactamente dos soluciones y qué relación geométrica tienen con el centro $3$.

No empieces resolviendo por casos: comienza identificando qué está midiendo $|x-3|$.

[]{#MA-EX-ANM-01-001-011}

### 11. Del valor absoluto a una región de la recta

Considera la condición

$$
|x+2|<4.
$$

1. Identifica el centro respecto del cual se está midiendo la separación.
2. Describe la condición en palabras.
3. Determina la región de la recta que satisface la desigualdad y escríbela mediante desigualdades de orden.
4. Comprueba directamente si $x=-6$, $x=-2$ y $x=2$ satisfacen la condición original.

La verificación final debe hacerse sustituyendo en $|x+2|<4$, no sólo mirando la región obtenida.

[]{#MA-EX-ANM-01-001-012}

### 12. Desplazamiento no es lo mismo que distancia

Un estudiante afirma:

> Como $|x-a|$ es la distancia entre $x$ y $a$, podemos quitar siempre las barras y escribir $|x-a|=x-a$.

1. Explica qué confusión conceptual contiene la afirmación.
2. Da un ejemplo con $x<a$ en el que la igualdad propuesta falle.
3. Indica qué información conserva $x-a$ que desaparece al pasar a $|x-a|$.
4. Formula una condición precisa bajo la cual sí se cumple $|x-a|=x-a$.

[]{#MA-EX-ANM-01-001-013}

### 13. Dos puntos simétricos respecto de un centro

Fija un centro $a\in\mathbb R$ y un número $t>0$. Considera los puntos

$$
x_+=a+t,
\qquad
x_-=a-t.
$$

1. Calcula $x_+-a$ y $x_--a$.
2. Calcula $|x_+-a|$ y $|x_--a|$.
3. Explica qué cambia y qué permanece al sustituir $t$ por otro número positivo.
4. Explica por qué conocer sólo la distancia al centro no permite decidir a qué lado de $a$ se encuentra el punto.

Tu respuesta debe distinguir explícitamente **desplazamiento orientado** y **separación**.

[]{#MA-EX-ANM-01-001-014}

### 14. Un centro común para dos puntos equidistantes

Sean $x,y,a\in\mathbb R$ y supón que

$$
|x-a|=|y-a|.
$$

1. Muestra que necesariamente ocurre una de estas dos posibilidades:

$$
x=y
$$

o

$$
x+y=2a.
$$

2. Si además $x\ne y$, concluye que

$$
a=\frac{x+y}{2}.
$$

3. Interpreta geométricamente el resultado: ¿qué papel desempeña $a$ cuando dos puntos distintos están a la misma distancia de él?

No uses resultados posteriores del capítulo: basta trabajar con la definición del valor absoluto y álgebra elemental.

## §1.4. Distancia entre dos puntos reales

[]{#MA-EX-ANM-01-001-015}

### 15. Tres propiedades que salen de la definición

Sea

$$
d(x,y)=|x-y|.
$$

Demuestra directamente, para cualesquiera $x,y\in\mathbb R$, las tres propiedades siguientes:

1. $d(x,y)\ge0$;
2. $d(x,y)=0\iff x=y$;
3. $d(x,y)=d(y,x)$.

En cada caso indica qué propiedad elemental del valor absoluto estás usando. No cites estas afirmaciones como propiedades ya conocidas de una métrica: el objetivo es recuperarlas desde la definición concreta de $d$.

[]{#MA-EX-ANM-01-001-016}

### 16. Reconstruir la desigualdad triangular

Sean $x,y,z\in\mathbb R$. Sin comenzar citando la desigualdad triangular para $d$, demuestra

$$
d(x,z)\le d(x,y)+d(y,z).
$$

Puedes usar el hecho elemental

$$
-|u|\le u\le |u|
$$

para todo $u\in\mathbb R$.

Tu argumento debe mostrar explícitamente:

1. cómo obtener $|u+v|\le |u|+|v|$;
2. qué elecciones de $u$ y $v$ producen $x-z$;
3. cómo se traduce el resultado final al lenguaje de $d$.

[]{#MA-EX-ANM-01-001-017}

### 17. De la desigualdad triangular a una cota inversa

Demuestra que, para cualesquiera $x,y\in\mathbb R$,

$$
\bigl||x|-|y|\bigr|\le d(x,y).
$$

No uses la desigualdad triangular inversa como un resultado ya disponible. Parte de la desigualdad triangular ordinaria y obtén primero dos desigualdades de una sola dirección. Después explica por qué ambas pueden condensarse en una sola expresión con valor absoluto.

[]{#MA-EX-ANM-01-001-018}

### 18. Una igualdad demasiado fuerte

Un estudiante razona así:

$$
x-z=(x-y)+(y-z),
$$

por lo tanto

$$
|x-z|=|x-y|+|y-z|,
$$

y concluye que

$$
d(x,z)=d(x,y)+d(y,z)
$$

para todos los reales $x,y,z$.

1. Identifica exactamente qué paso no está justificado.
2. Sustituye la igualdad falsa por la afirmación correcta que sí vale siempre.
3. Da un contraejemplo numérico a la igualdad propuesta y verifica ambos lados.
4. Explica por qué el contraejemplo no contradice la desigualdad correcta.

No intentes todavía caracterizar cuándo sí hay igualdad; esa pregunta pertenece a la sección siguiente.

[]{#MA-EX-ANM-01-001-019}

### 19. Mover el punto de referencia en la desigualdad inversa

Fija $x,y,a\in\mathbb R$.

1. Aplica la desigualdad triangular inversa a los números $x-a$ e $y-a$ y demuestra

$$
\bigl||x-a|-|y-a|\bigr|\le |x-y|.
$$

2. Toma ahora $x=1$ y $y=5$. Calcula el lado izquierdo para $a=-2$, $a=3$ y $a=8$.
3. Compara los tres resultados con $|x-y|$.
4. Explica qué cantidad cambia al mover $a$ y qué cota permanece inalterada.

El objetivo es ver que cambiar el punto de referencia modifica las dos distancias individuales, pero no la cota universal que controla cuánto pueden diferir.

[]{#MA-EX-ANM-01-001-020}

### 20. Encadenar estimaciones de distancia

Sean $x,y,z,w\in\mathbb R$. Demuestra que

$$
d(x,w)\le d(x,y)+d(y,z)+d(z,w).
$$

Tu prueba debe usar la desigualdad triangular dos veces y mostrar con claridad dónde se aplica cada vez.

Después deduce que, si para cierto $r\ge0$ se cumplen

$$
d(x,y)\le r,
\qquad
d(y,z)\le r,
\qquad
d(z,w)\le r,
$$

entonces

$$
d(x,w)\le3r.
$$

Explica qué enseña este resultado sobre la acumulación de varios errores o desplazamientos pequeños.

[]{#MA-EX-ANM-01-001-021}

### 21. Transportar una cota a un punto cercano

Sean $m,M,\varepsilon\ge0$ con $m\le M$. Supón que dos números reales $x$ e $y$ satisfacen

$$
m\le |x|\le M
$$

y

$$
d(x,y)\le\varepsilon.
$$

Demuestra que

$$
\max\{0,m-\varepsilon\}\le |y|\le M+\varepsilon.
$$

Tu argumento debe indicar qué parte proviene de la desigualdad triangular y qué parte de la desigualdad triangular inversa.

Después analiza si las dos cotas pueden alcanzarse exactamente:

1. construye un ejemplo que alcance la cota superior;
2. si $m\ge\varepsilon$, construye un ejemplo que alcance $m-\varepsilon$;
3. si $m<\varepsilon$, explica por qué la cota inferior se convierte en $0$ y da un ejemplo que la alcance.

Interpreta el resultado como una regla de propagación de error: conocer cuánto puede cambiar un punto permite controlar cuánto puede cambiar su distancia al origen.

## §1.5. La desigualdad triangular y la geometría de «estar entre»

[]{#MA-EX-ANM-01-001-022}

### 22. Igualdad sin retroceso

Sean $x,y,z\in\mathbb R$. Demuestra directamente que, si $y$ está entre $x$ y $z$, entonces

$$
d(x,z)=d(x,y)+d(y,z).
$$

Tu prueba debe cubrir explícitamente los dos órdenes posibles

$$
x\le y\le z
$$

y

$$
z\le y\le x,
$$

incluyendo los casos en que $y$ coincide con uno de los extremos. Explica al final por qué la suma de las dos distancias parciales no contiene recorrido redundante.

[]{#MA-EX-ANM-01-001-023}

### 23. La igualdad obliga al punto intermedio

Supón que $x,y,z\in\mathbb R$ satisfacen

$$
d(x,z)=d(x,y)+d(y,z).
$$

Demuestra que

$$
\min\{x,z\}\le y\le\max\{x,z\}.
$$

Organiza la prueba suponiendo primero $x\le z$ y examinando las tres regiones posibles para $y$: $y<x$, $x\le y\le z$ y $y>z$. En los dos casos exteriores debes exhibir explícitamente la longitud extra que hace imposible la igualdad.

[]{#MA-EX-ANM-01-001-024}

### 24. Estar entre no significa ser el punto medio

Un estudiante afirma:

> Si $d(x,z)=d(x,y)+d(y,z)$, entonces $y$ es necesariamente el punto medio entre $x$ y $z$.

1. Diagnostica el error y da un contraejemplo numérico.
2. Formula la conclusión correcta que sí se deduce de la igualdad triangular en $\mathbb R$.
3. Añade una condición métrica que, junto con la igualdad triangular, sí obligue a que $y$ sea el punto medio de $x$ y $z$.
4. Justifica esa afirmación sin usar resultados posteriores del capítulo.

[]{#MA-EX-ANM-01-001-025}

### 25. Medir exactamente el retroceso

Fija dos puntos $x<z$ y define, para $y\in\mathbb R$,

$$
E(y)=d(x,y)+d(y,z)-d(x,z).
$$

1. Demuestra que

$$
E(y)=
\begin{cases}
2(x-y),&y<x,\\
0,&x\le y\le z,\\
2(y-z),&y>z.
\end{cases}
$$

2. Explica por qué $E(y)\ge0$ para todo $y$.
3. Determina exactamente para qué valores de $y$ se cumple $E(y)=0$.
4. Interpreta geométricamente el factor $2$ que aparece cuando $y$ queda fuera del segmento $[x,z]$.

[]{#MA-EX-ANM-01-001-026}

### 26. Cuatro puntos y una ruta sin retroceso

Supón que $x,z\in\mathbb R$ satisfacen $x\le z$. Demuestra que

$$
d(x,z)=d(x,y)+d(y,w)+d(w,z)
$$

si y sólo si

$$
x\le y\le w\le z.
$$

Tu prueba debe explicar por qué, si la igualdad total se cumple, las dos desigualdades

$$
d(x,z)\le d(x,y)+d(y,z)
$$

y

$$
d(y,z)\le d(y,w)+d(w,z)
$$

han de convertirse simultáneamente en igualdades. Interpreta el resultado como una extensión del principio «igualdad triangular = ausencia de retroceso».

[]{#MA-EX-ANM-01-001-027}

### 27. Lo que las distancias revelan —y lo que no

Sean $a,b,c\in\mathbb R$ tres puntos distintos. Supón que sólo conocemos las tres distancias

$$
d(a,b),\qquad d(b,c),\qquad d(a,c).
$$

1. Demuestra que uno de los tres puntos está entre los otros dos y que la distancia entre los dos extremos es la suma de las otras dos distancias.
2. Explica cómo determinar, a partir de las tres distancias etiquetadas, cuál de $a,b,c$ es el punto intermedio.
3. Para

$$
d(a,b)=2,\qquad d(a,c)=3,\qquad d(b,c)=5,
$$

identifica el punto intermedio y justifica la respuesta.
4. Demuestra que, aun conociendo las tres distancias, no podemos decidir qué extremo está a la izquierda y cuál a la derecha: construye a partir de una realización cualquiera otra realización con las mismas distancias y orientación opuesta.

El objetivo es precisar hasta dónde la información métrica permite recuperar la estructura de orden y qué parte de la orientación sigue perdiéndose.

## §1.6. Bolas métricas: ventanas alrededor de un punto

[]{#MA-EX-ANM-01-001-028}

### 28. Leer una bola en cuatro lenguajes

Considera la bola

$$
B(2,3).
$$

1. Escríbela usando la definición $d(x,2)<3$.
2. Reescribe la condición mediante valor absoluto.
3. Exprésala como una doble desigualdad de orden.
4. Escríbela como intervalo.
5. Decide si pertenecen a la bola los puntos $-1$, $2$ y $5$, justificando cada caso desde la condición de distancia.

El objetivo es seguir una misma región a través de varias representaciones, no memorizar el intervalo final.

[]{#MA-EX-ANM-01-001-029}

### 29. Recuperar centro y radio desde un intervalo

Sea $u<v$. Demuestra que el intervalo abierto

$$
(u,v)
$$

puede escribirse como una bola $B(a,r)$ con

$$
a=\frac{u+v}{2},
\qquad
r=\frac{v-u}{2}.
$$

Después:

1. verifica la fórmula para el intervalo $(-5,1)$;
2. explica geométricamente por qué $a$ es el centro del intervalo;
3. explica por qué $r>0$ se deduce de $u<v$.

No basta con sustituir en una fórmula: muestra que $a-r=u$ y $a+r=v$.

[]{#MA-EX-ANM-01-001-030}

### 30. Mismo centro, radios distintos

Fija $a\in\mathbb R$ y números $0<r<s$.

1. Demuestra que

$$
B(a,r)\subset B(a,s).
$$

2. Prueba que la inclusión es estricta construyendo explícitamente un punto que pertenezca a $B(a,s)$ pero no a $B(a,r)$.
3. Interpreta el resultado usando la imagen de una ventana centrada en $a$: ¿qué permanece y qué cambia cuando aumenta el radio?

Tu prueba de la inclusión debe partir de la condición de distancia, no sólo de un dibujo.

[]{#MA-EX-ANM-01-001-031}

### 31. Mover el centro: cuándo dos bolas se encuentran

Fija $r>0$ y sean $a,b\in\mathbb R$. Considera las dos bolas de igual radio

$$
B(a,r)
\qquad\text{y}\qquad
B(b,r).
$$

Demuestra que

$$
B(a,r)\cap B(b,r)\ne\varnothing
\iff
d(a,b)<2r.
$$

Después analiza por separado los casos

$$
d(a,b)=2r
$$

y

$$
d(a,b)>2r.
$$

Explica qué ocurre geométricamente con los dos intervalos cuando desplazamos uno de los centros alejándolo del otro, manteniendo fijo el radio.

[]{#MA-EX-ANM-01-001-032}

### 32. Cuándo una bola cabe dentro de otra

Sean $a,b\in\mathbb R$ y $r,s>0$. Demuestra que

$$
B(a,r)\subseteq B(b,s)
\iff
d(a,b)+r\le s.
$$

Tu prueba debe conectar dos perspectivas:

1. la representación por intervalos

$$
B(a,r)=(a-r,a+r),
\qquad
B(b,s)=(b-s,b+s);
$$

2. la interpretación métrica de $d(a,b)$ como separación entre los centros.

Explica al final por qué la condición dice exactamente que el radio de la bola grande debe alcanzar desde $b$ hasta el punto más lejano de la bola pequeña.

No uses conceptos topológicos posteriores: trabaja sólo con distancia, valor absoluto, orden e intervalos.

## §1.7. Traducir entre orden, distancia y tolerancia

[]{#MA-EX-ANM-01-001-033}

### 33. Una tolerancia escondida dentro de una expresión lineal

Considera la condición

$$
|2x-5|<3.
$$

1. Reescríbela en la forma $|x-a|<r$, identificando el centro $a$ y el radio $r$.
2. Exprésala como una desigualdad de distancia $d(x,a)<r$.
3. Tradúcela a una doble desigualdad de orden.
4. Escribe el conjunto solución como intervalo.
5. Explica por qué dividir toda la desigualdad por $2$ no cambia el sentido de la comparación.

El objetivo es reconocer primero la estructura de tolerancia y sólo después resolver la desigualdad.

[]{#MA-EX-ANM-01-001-034}

### 34. Estar lejos de un centro

Traduce completamente la condición

$$
|3x+6|\ge 9
$$

hasta obtener:

1. una condición de distancia respecto de un centro;
2. una disyunción de desigualdades de orden;
3. una unión de regiones de la recta.

Después decide si los puntos $-5$, $-2$ y $1$ pertenecen al conjunto solución, justificando cada respuesta desde la condición original.

[]{#MA-EX-ANM-01-001-035}

### 35. Una rama desaparecida

Un estudiante afirma que, para $r>0$,

$$
|x-a|>r
\iff
x>a+r.
$$

1. Explica qué parte de la región solución ha desaparecido.
2. Da un contraejemplo numérico a la equivalencia propuesta.
3. Escribe la equivalencia correcta en lenguaje de orden.
4. Exprésala como unión de intervalos.
5. Explica por qué el error es fácil de cometer si se piensa en $x-a$ como desplazamiento orientado y no en $|x-a|$ como distancia.

[]{#MA-EX-ANM-01-001-036}

### 36. Entre dos umbrales de distancia

Sean $a\in\mathbb R$ y $0<r<s$. Considera la condición

$$
r<d(x,a)\le s.
$$

1. Reescríbela mediante valor absoluto.
2. Traduce la condición a desigualdades de orden.
3. Describe el conjunto solución como unión de intervalos.
4. Indica cuáles de los cuatro puntos $a-s$, $a-r$, $a+r$ y $a+s$ pertenecen al conjunto.
5. Explica por qué la región obtenida tiene dos componentes separadas por una zona central excluida.

[]{#MA-EX-ANM-01-001-037}

### 37. Dos tolerancias simultáneas

Sean $a,b\in\mathbb R$ y $r,s>0$. Estudia el conjunto de puntos que satisfacen simultáneamente

$$
d(x,a)\le r
$$

y

$$
d(x,b)\le s.
$$

1. Traduce ambas condiciones a intervalos cerrados.
2. Escribe su intersección usando $\max$ y $\min$.
3. Demuestra que existe al menos un punto que satisface ambas tolerancias si y sólo si

$$
d(a,b)\le r+s.
$$

4. Interpreta la condición final como comparación entre la separación de los centros y los márgenes de tolerancia disponibles.

*Pista conceptual.* Antes de manipular valores absolutos, piensa qué significa que dos intervalos cerrados centrados en $a$ y $b$ tengan un punto común.

[]{#MA-EX-ANM-01-001-038}

### 38. Una familia que no crece por inclusión

Fija $a\in\mathbb R$ y, para cada $t>0$, define

$$
A_t=\{x\in\mathbb R:t<d(x,a)\le 2t\}.
$$

1. Traduce $A_t$ a una unión de intervalos.
2. Sean $0<t<s$. Demuestra que, en general, ni $A_t\subseteq A_s$ ni $A_s\subseteq A_t$.
3. Caracteriza exactamente cuándo $A_t\cap A_s$ es vacío y cuándo no lo es.
4. Si la intersección es no vacía, descríbela mediante una condición sobre $d(x,a)$.
5. Explica por qué aquí «aumentar el parámetro» no produce una familia anidada como ocurría con las bolas $B(a,r)$.

*Pista conceptual.* En vez de mirar primero los puntos $x$, mira los valores posibles de la distancia $d(x,a)$. Para $A_t$ esos valores forman un intervalo de tolerancias, no una región del tipo $d(x,a)<t$.

## §1.8. Qué ve el orden y qué ve la distancia

[]{#MA-EX-ANM-01-001-039}

### 39. Preservar distancias no significa preservar orientación

Sea $F:\mathbb R\to\mathbb R$ una aplicación que preserva todas las distancias:

$$
d(F(x),F(y))=d(x,y)
$$

para cualesquiera $x,y\in\mathbb R$.

Un estudiante concluye:

> Si $x<y$, entonces necesariamente $F(x)<F(y)$, porque una aplicación que preserva distancias conserva toda la geometría de la recta.

1. Diagnostica la afirmación mediante un contraejemplo explícito.
2. Demuestra, sin embargo, que $F$ sí preserva la relación «estar entre»: si $y$ está entre $x$ y $z$, entonces $F(y)$ está entre $F(x)$ y $F(z)$.
3. Explica con precisión qué información métrica se conserva y qué información de orientación puede perderse.

No supongas que $F$ es lineal o afín.

[]{#MA-EX-ANM-01-001-040}

### 40. Trasladar y escalar en una sola transformación

Para $\lambda,c\in\mathbb R$, define

$$
T_{\lambda,c}(x)=\lambda x+c.
$$

1. Demuestra que

$$
d(T_{\lambda,c}(x),T_{\lambda,c}(y))=|\lambda|\,d(x,y).
$$

2. Clasifica completamente los valores de $\lambda$ para los cuales $T_{\lambda,c}$:
   - preserva exactamente todas las distancias;
   - preserva el orden estricto;
   - invierte el orden estricto;
   - colapsa puntos distintos.
3. Determina todas las transformaciones de esta familia que preservan simultáneamente todas las distancias y el orden.
4. Determina todas las que preservan todas las distancias e invierten el orden.
5. Explica por qué el parámetro $c$ no interviene ni en el factor de escala de las distancias ni en el sentido de la orientación.

*Pista conceptual.* Separa el efecto de sumar $c$ del efecto de multiplicar por $\lambda$.

[]{#MA-EX-ANM-01-001-041}

### 41. Componer transformaciones: escala y orientación

Sean

$$
S(x)=\lambda x+c,
\qquad
T(x)=\mu x+d,
$$

con $\lambda,\mu\ne0$.

1. Calcula $T\circ S$ y demuestra que su factor de escala métrica es $|\mu\lambda|$.
2. Prueba que $T\circ S$ preserva el orden si $\mu\lambda>0$ y lo invierte si $\mu\lambda<0$.
3. Explica por qué dos transformaciones que invierten la orientación producen, al componerse, una transformación que la preserva.
4. Para $p\in\mathbb R$, define la reflexión respecto del punto $p$ por

$$
R_p(x)=2p-x.
$$

Demuestra que

$$
R_q\circ R_p(x)=x+2(q-p).
$$

5. Interpreta el resultado: ¿por qué la composición de dos reflexiones de la recta es una traslación? ¿Qué ocurre cuando $p=q$?

*Pista conceptual.* En la composición, los factores de escala se multiplican y los signos registran cuántas inversiones de orientación se han acumulado.

[]{#MA-EX-ANM-01-001-042}

### 42. Clasificar todas las isometrías de la recta

Sea $F:\mathbb R\to\mathbb R$ una aplicación que preserva todas las distancias:

$$
d(F(x),F(y))=d(x,y)
$$

para cualesquiera $x,y\in\mathbb R$.

Demuestra que existe un número $c\in\mathbb R$ tal que necesariamente ocurre exactamente una de las dos formas

$$
F(x)=x+c
$$

para todo $x$, o bien

$$
F(x)=-x+c
$$

para todo $x$.

En otras palabras: demuestra que **toda isometría de la recta es una traslación o una reflexión seguida de una traslación**.

Después deduce que toda isometría de $\mathbb R$ o bien preserva todas las desigualdades estrictas, o bien las invierte todas.

*Pista conceptual.* Empieza eliminando $F(0)$ mediante una traslación. Si consigues una isometría $G$ con $G(0)=0$, entonces $|G(x)|=|x|$ para todo $x$. El paso difícil es demostrar que la elección del signo no puede cambiar de un punto a otro.
