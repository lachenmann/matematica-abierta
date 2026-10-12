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
date-modified: '2026-10-11'
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

## 19.2. El borde no es un centro interior

[]{#MA-EX-ANM-01-019-002}

[]{#MA-SOL-ANM-01-019-002}

El orden da mínimo global en cero y máximo global en uno. En cualquier centro acumulante del segmento el cociente perforado vale uno, también en los dos bordes, así sus derivadas relativas son uno. Cada bola centrada en cero contiene entradas negativas fuera del dominio y cada bola centrada en uno contiene entradas mayores que uno, por lo que ninguno es interior. Fermat no se aplica allí; su prueba necesita ambas clases de entradas admisibles, que faltan en los bordes.

**Retorno visual.** Véase [C19-F01](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.3. Una esquina y un punto estacionario

[]{#MA-EX-ANM-01-019-003}

[]{#MA-SOL-ANM-01-019-003}

El valor absoluto tiene mínimo global cero, pero secantes de pendientes menos uno y uno, por lo que no es derivable allí. El cuadrado tiene mínimo global y cociente centrado en cero igual a $x$, así derivada cero. El cubo tiene cociente $x^2$ y derivada cero, pero entradas positivas y negativas arbitrariamente cercanas dan valores de signos opuestos: no hay extremo local. Por tanto un extremo interior no crea derivabilidad y una derivada nula no garantiza extremo.

## 19.4. Dos lados sin un intervalo completo

[]{#MA-EX-ANM-01-019-004}

[]{#MA-SOL-ANM-01-019-004}

Sea $L$ la derivada relativa. Para un mínimo, las pendientes de la izquierda son no positivas y las de la derecha no negativas dentro del radio del extremo. Si $L>0$, el radio de error $L/2$ obliga a pendientes positivas; acumulación izquierda entrega una entrada dentro del mínimo de ambos radios, contradicción. Si $L<0$, acumulación derecha y error $|L|/2$ dan la contradicción opuesta. No hace falta una bola completa del dominio, sino entradas de ambos lados en todo radio. Para máximo se aplica el resultado a $-f$. No se infiere esa acumulación sólo de que el centro sea de acumulación por uno de los lados.

## 19.5. Transformar el máximo

[]{#MA-EX-ANM-01-019-005}

[]{#MA-SOL-ANM-01-019-005}

Si $f$ alcanza un máximo local en $a$, la función $g=-f$ sobre el mismo dominio alcanza un mínimo local con el mismo radio. El centro sigue siendo interior y C18 da derivabilidad $g\prime(a)=-f\prime(a)$. El caso mínimo implica $g\prime(a)=0$, así $f\prime(a)=0$. La transformación conserva tipos y dominio y sólo invierte el orden de valores; no se utiliza un resultado global o valor medio.

## 19.6. Localizar un extremo interior

[]{#MA-EX-ANM-01-019-006}

[]{#MA-SOL-ANM-01-019-006}

[]{#MA-SEC-ANM-01-019-002}

C16 entrega un máximo y un mínimo alcanzados en el segmento. Si el valor distinto es mayor que $k$, el máximo tiene valor al menos tan grande y por tanto mayor que ambos bordes; su punto no puede ser ninguno de ellos y queda en $(a,b)$. Si es menor que $k$, el mínimo queda estrictamente por debajo de ambos bordes y también es interior. Tricotomía cubre los dos casos. No se afirma que ambos extremos globales tengan esa posición ni que la función sea derivable, pues este paso sólo localiza un extremo desde continuidad.

## 19.7. Una parábola que vuelve al borde

[]{#MA-EX-ANM-01-019-007}

[]{#MA-SOL-ANM-01-019-007}

El polinomio es continuo y derivable, con bordes cero. C18 da $f\prime(x)=1-2x$, que sólo se anula en $c=1/2$, interior al segmento. Su valor es $1/4$, no cero. Rolle predice existencia de un cero de la derivada entre los dos ceros de la función y en este ejemplo es único por la ecuación explícita; no predice un tercer cero de la función.

**Retorno visual.** Véase [C19-F02](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.8. Perder continuidad en un borde

[]{#MA-EX-ANM-01-019-008}

[]{#MA-SOL-ANM-01-019-008}

Los bordes valen cero. Cada punto interior tiene una vecindad donde $u$ es identidad, por lo que su derivada es uno y nunca cero. En uno, las entradas $1-1/(n+2)$ tienen salidas tendentes a uno, distintas del valor cero; no hay continuidad relativa. Se cumplen derivabilidad interior e igualdad de borde, pero falla precisamente continuidad del segmento cerrado. La hipótesis interior por sí sola no garantiza los extremos alcanzados necesarios para la prueba de Rolle.

## 19.9. Omitir la derivabilidad

[]{#MA-EX-ANM-01-019-009}

[]{#MA-SOL-ANM-01-019-009}

La función de valor absoluto trasladada es continua y tiene valores $1/2$ en ambos bordes. A la izquierda de un medio su derivada es menos uno y a la derecha uno; en un medio no existe. Así no hay ninguna derivada interior nula y falla derivabilidad en todo el interior. Para la identidad, continuidad y derivabilidad se cumplen pero los bordes cero y uno son diferentes y su derivada siempre vale uno. Los ejemplos eliminan una sola hipótesis cada vez y muestran que no puede omitirse del enunciado universal.

## 19.10. Muchos puntos posibles

[]{#MA-EX-ANM-01-019-010}

[]{#MA-SOL-ANM-01-019-010}

En una constante sobre un segmento no degenerado todas las pendientes interiores son cero, por lo que cualquier punto interior sirve. La conclusión existencial no designa uno de ellos; su uso fija una función y un segmento y toma un testigo para esa instancia. Para $a=b$, el interior es vacío y no podría existir tal punto, aunque la igualdad de borde sea automática. Por eso se exige $a<b$. Ninguna de estas conclusiones construye un selector para una familia infinita de intervalos.

## 19.11. Construir el residuo de la secante

[]{#MA-EX-ANM-01-019-011}

[]{#MA-SOL-ANM-01-019-011}

[]{#MA-SEC-ANM-01-019-003}

Con $a<b$, $m=[f(b)-f(a)]/(b-a)$ es real. La recta $\ell(x)=f(a)+m(x-a)$ comparte los valores de borde y $H=f-\ell$ vive en $[a,b]$. Continuidad de $f$ y de la recta hace continua $H$ en todo el segmento; C18 da derivada $H\prime=f\prime-m$ en su interior. Ambos bordes de $H$ valen cero. Rolle entrega $c$ interior con $H\prime(c)=0$, y la identidad de derivadas implica $f\prime(c)=m$. No se ha aplicado Rolle directamente a $f$, cuyos bordes pueden ser distintos.

## 19.12. Tangente paralela en el cuadrado

[]{#MA-EX-ANM-01-019-012}

[]{#MA-SOL-ANM-01-019-012}

La pendiente secante es $(9-1)/(3-1)=4$. La recta es $\ell(x)=1+4(x-1)=4x-3$. El residuo $H(x)=x^2-4x+3=(x-1)(x-3)$ tiene ambos bordes cero y derivada $2x-4$. Se anula sólo en $c=2$, interior al segmento; allí la derivada original vale cuatro. La igualdad de pendientes se verifica exactamente, sin localizar el punto leyendo una figura.

**Retorno visual.** Véase [C19-F03](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.13. El punto medio no es universal

[]{#MA-EX-ANM-01-019-013}

[]{#MA-SOL-ANM-01-019-013}

El incremento de valores y el de entrada son uno, así la pendiente secante es uno. La derivada del cubo es $3c^2$; en un medio vale $3/4$, por lo que no cumple la igualdad. Resolver $3c^2=1$ y exigir $c\in(0,1)$ da $c=1/\sqrt3$. El punto medio funciona para el cuadrado por su fórmula específica, sin ser un dato del teorema. Lagrange asegura existencia interior, no una localización predeterminada.

## 19.14. Restringir sin llenar un hueco

[]{#MA-EX-ANM-01-019-014}

[]{#MA-SOL-ANM-01-019-014}

Hace falta $[u,v]\subseteq D$, continuidad en ese segmento y derivabilidad en su interior. La restricción conserva continuidad y, porque cada centro interior acumula en el segmento, también las derivadas originales. En $D=[0,1]\cup[2,3]$, tomar $u=1,v=2$ sólo da dos argumentos válidos y no una función definida en $(1,2)$. La función cero en la primera pieza y uno en la segunda tiene todas sus derivadas relativas cero, mientras la secante entre esos bordes tiene pendiente uno. Lagrange no se aplica: falta su dominio intervalar completo.

## 19.15. Igualdad sin continuidad de derivada

[]{#MA-EX-ANM-01-019-015}

[]{#MA-SOL-ANM-01-019-015}

C18 demuestra que F es derivable en toda la recta y por tanto continua en cada punto. Su restricción al segmento es continua, y las derivadas de los centros interiores se conservan. Así Lagrange entrega un punto donde la derivada coincide con la pendiente secante. La discontinuidad de $F'$ en cero no elimina ninguna hipótesis del teorema, porque sólo se exige existencia de las derivadas interiores. No se afirma que el punto de valor medio sea cero o que pueda identificarse por una muestra de bultos.

## 19.16. Del signo a cada par

[]{#MA-EX-ANM-01-019-016}

[]{#MA-SOL-ANM-01-019-016}

[]{#MA-SEC-ANM-01-019-004}

Fijamos $x<y$ de I. El intervalo contiene todo $[x,y]$ y su interior está en el de I. La restricción es continua y derivable donde corresponde. Lagrange da algún $c\in(x,y)$ con $f(y)-f(x)=f\prime(c)(y-x)$. Como la derivada es no negativa y el incremento positivo, la diferencia es no negativa. Para todo par ordenado se obtiene $f(x)\le f(y)$, sin necesitar un mismo punto c para todos los pares o continuidad de la derivada.

## 19.17. Crecimiento estricto con una derivada nula

[]{#MA-EX-ANM-01-019-017}

[]{#MA-SOL-ANM-01-019-017}

Para $x<y$, la diferencia es $(y-x)(x^2+xy+y^2)$. El primer factor es positivo y el segundo es $(x+y/2)^2+3y^2/4$, no negativo y sólo cero si $x=y=0$, imposible aquí. La diferencia es positiva. C18 da derivada $3x^2$, cero en el origen. Se refuta que crecimiento estricto implique derivada estrictamente positiva en cada punto; la conclusión necesaria donde existe es sólo no negatividad.

## 19.18. Derivadas iguales, valores fijados

[]{#MA-EX-ANM-01-019-018}

[]{#MA-SOL-ANM-01-019-018}

H=f-g es continua y derivable en el mismo dominio con $H'$=0. Para cualesquiera x<y, Lagrange en su segmento da H(y)-H(x)=$H'(c)$(y-x)=0. Los pares iguales son triviales y los inversos se intercambian, así H es constante. Si f(a)=g(a) en algún a del intervalo, H(a)=0 identifica esa constante y las funciones coinciden en todo el dominio. No se necesita integrar ni introducir una primitiva.

## 19.19. Constantes distintas en un dominio roto

[]{#MA-EX-ANM-01-019-019}

[]{#MA-SOL-ANM-01-019-019}

Ponemos f=0 en la primera pieza y f=1 en la segunda. Cada punto tiene una vecindad relativa que sólo toca su pieza y allí todos los valores son iguales, así el cociente perforado es cero. Todos los puntos, incluidos los cuatro bordes, acumulan en el dominio por al menos un lado, por lo que las derivadas relativas existen y valen cero. Sin embargo f(0)=0 y f(2)=1. El segmento entre piezas falta; la conclusión de constancia requiere el intervalo, no sólo derivabilidad en todos los puntos válidos.

**Retorno visual.** Véase [C19-F04](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.20. Signo de una derivada existente

[]{#MA-EX-ANM-01-019-020}

[]{#MA-SOL-ANM-01-019-020}

Todos los cocientes perforados centrados en a son no negativos: a la derecha numerador y denominador son no negativos; a la izquierda ambos son no positivos y el denominador es negativo. Si el límite L fuera negativo, tolerancia |L|/2 obligaría a cocientes menores que L/2<0 en un radio. Acumulación en el centro proporciona un argumento perforado dentro de él, contradicción. Sólo se usan orden y definición de derivada; no se deriva existencia de la pendiente desde monotonía.

## 19.21. Dos cotas de incrementos

[]{#MA-EX-ANM-01-019-021}

[]{#MA-SOL-ANM-01-019-021}

[]{#MA-SEC-ANM-01-019-005}

Para x<y, Lagrange proporciona c interior con diferencia $f'(c)$(y-x). Sustituir m≤$f'(c)$≤M y multiplicar por y-x>0 preserva el orden. Si las cotas son -L,L, esto equivale a magnitud a lo sumo L(y-x). Para y<x se intercambian argumentos y se usa simetría de valores absolutos; para x=y ambos lados son cero. La cota final vale para todos los pares, y la continuidad en extremos incluidos permite restringir a segmentos que los contengan.

## 19.22. Cubo y radio común

[]{#MA-EX-ANM-01-019-022}

[]{#MA-SOL-ANM-01-019-022}

La derivada es 3t², entre cero y doce para t interior. R5 da |y³-x³|≤12|y-x| para todos los pares del segmento, porque el polinomio es continuo y derivable. Para tolerancia ε>0, δ=ε/12 asegura que distancia de entrada menor que δ da error menor que ε. No se elige un radio según el centro; el mismo doce controla toda la familia de derivadas interiores. Esta prueba no afirma esa misma cota global en toda la recta.

**Retorno visual.** Véase [C19-F05](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.23. Una frontera rompe el certificado

[]{#MA-EX-ANM-01-019-023}

[]{#MA-SOL-ANM-01-019-023}

En todo el interior $u'$=1. Si un L≥0 controlara todos los pares, elegir x=(L+1)/(L+2) y y=1 daría |u(y)-u(x)|=x y |y-x|=1/(L+2). Pero x=(L+1)/(L+2)>L/(L+2)=L|y-x|, contradicción. Los dos argumentos están en el dominio y x<1. La discontinuidad en el borde impide aplicar Lagrange a esos segmentos y explica por qué la cota interior por sí sola no basta.

## 19.24. La raíz lejos de cero

[]{#MA-EX-ANM-01-019-024}

[]{#MA-SOL-ANM-01-019-024}

En centros positivos la derivada es 1/(2√t), a lo sumo uno cuando t≥1/4. La función es continua en el segmento y R5 da |√y-√x|≤|y-x|. En [0,1], cualquier constante L>0 fallaría en el par cero e y positivo tan pequeño que y<min(1,1/(L+1)²), pues √y/y=1/√y>L. Para L=0 también falla cualquier y>0. La raíz sigue siendo uniforme con control no lineal de C17; falta una cota Lipschitz, sin perder continuidad uniforme.

## 19.25. Una pendiente cercana en todos los centros

[]{#MA-EX-ANM-01-019-025}

[]{#MA-SOL-ANM-01-019-025}

La función H(t)=f(t)-f(a)-A(t-a) es continua sobre ese segmento, derivable dentro y satisface |$H'$|≤η. Aplicar la cota de pares entre a y x, con H(a)=0, da |H(x)|≤η|x-a|. Si x=a el error es cero sin aplicación de Lagrange. Saber sólo $f'(a)$=A no acota las derivadas de los otros centros ni proporciona esa premisa universal, aunque C18 garantice un resto menor que lineal alrededor de a. El certificado se apoya en la cota adicional y no usa Taylor.

## 19.26. Productos cruzados antes de cocientes

[]{#MA-EX-ANM-01-019-026}

[]{#MA-SOL-ANM-01-019-026}

[]{#MA-SEC-ANM-01-019-006}

Fijamos Δf=f(b)-f(a), Δg=g(b)-g(a), y H=Δg(f-f(a))-Δf(g-g(a)) sobre [a,b]. Sus dos bordes son cero, por cancelación de productos. Es continua y derivable donde corresponde, con $H'$=Δg $f'$-Δf $g'$, porque los coeficientes son números fijos. Rolle entrega c interior con $H'(c)$=0, que equivale a Δf $g'(c)$=Δg $f'(c)$. Cada expresión existe aunque algún incremento o derivada se anule; ningún paso dividió por ellos.

## 19.27. Tres puntos diferentes

[]{#MA-EX-ANM-01-019-027}

[]{#MA-SOL-ANM-01-019-027}

Ambos incrementos son uno. Lagrange para f resuelve 2c=1 y da 1/2; para g resuelve 3c²=1 y da 1/√3. Son distintos porque el cuadrado de 1/2 no es 1/3. Cauchy exige 3c²=2c; la interioridad c>0 elimina la solución cero y da c=2/3. En ese punto las dos derivadas valen 4/3 y su razón es uno. Aplicar dos existencias separadas no había garantizado un centro común.

**Retorno visual.** Véase [C19-F06](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.28. Legitimar ambas divisiones

[]{#MA-EX-ANM-01-019-028}

[]{#MA-SOL-ANM-01-019-028}

Si Δg=0, g tendría valores de borde iguales, continuidad en el segmento y derivabilidad dentro; Rolle daría un punto con $g'$=0, contradicción. Por tanto Δg≠0. El testigo c de Cauchy también cumple $g'(c)$≠0 por la premisa universal. Dividir la igualdad cruzada por Δg $g'(c)$, no nulo, da $f'(c)$/$g'(c)$=Δf/Δg. Se verifican las dos divisiones después de sus condiciones, sin asumir que un incremento no nulo haga no nula toda derivada.

## 19.29. Un incremento nulo

[]{#MA-EX-ANM-01-019-029}

[]{#MA-SOL-ANM-01-019-029}

Δf=1 y Δg=0. La identidad exige $g'(c)$=0; su derivada es 1-2c y el único punto interior es c=1/2. Allí $f'$=1 y $g'$=0, de modo que la igualdad cruzada es cero igual a cero. Las razones Δf/Δg y $f'$/$g'$ no existen. La forma cruzada contiene información correcta sobre la anulación, mientras la formulación por cocientes sería ilegítima en este ejemplo.

## 19.30. Un testigo donde no se puede dividir

[]{#MA-EX-ANM-01-019-030}

[]{#MA-SOL-ANM-01-019-030}

Los dos incrementos son dos y las derivadas iguales, así la igualdad cruzada es cierta para todo punto interior. En c=0 ambas derivadas valen cero. Aunque Δg=2≠0, la razón de derivadas sería 0/0 allí y no está definida. Se puede escoger otro punto no nulo en este ejemplo y obtener la razón uno, pero la sola identidad cruzada con un testigo arbitrario no garantiza esa división. Para una garantía universal se usa $g'$≠0 en todo el interior o se verifica expresamente la derivada en el testigo concreto.

## 19.31. Excluir los bordes de un mínimo

[]{#MA-EX-ANM-01-019-031}

[]{#MA-SOL-ANM-01-019-031}

[]{#MA-SEC-ANM-01-019-007}

La pendiente negativa en u fuerza cocientes negativos cerca y una entrada explícita t=u+min(δu,v-u)/2 produce H(t)<H(u). La pendiente positiva en v fuerza cocientes positivos, y s=v-min(δv,v-u)/2 tiene incremento negativo, dando H(s)<H(v). Derivabilidad da continuidad de H en todo el segmento; C16 asegura un mínimo alcanzado. Ninguno de sus bordes puede minimizar por las comparaciones, así un minimizador c está en (u,v). Una bola pequeña de c queda en el segmento y convierte ese mínimo global restringido en mínimo local de la función original.

## 19.32. Una derivada intermedia sin suponer continuidad

[]{#MA-EX-ANM-01-019-032}

[]{#MA-SOL-ANM-01-019-032}

H=f-λx tiene derivadas negativas y positivas en los dos bordes, respectivamente. E031 localiza un mínimo interior; Fermat implica $H'(c)$=0 y por tanto $f'(c)$=λ. La continuidad empleada es la de H, deducida de derivabilidad de f y de la recta, no la de $f'$. Si los valores derivados aparecen en orden opuesto, la función -f y el número -λ tienen el orden ya probado, y su conclusión se traduce de nuevo a $f'(c)$=λ. El punto está estrictamente entre u y v.

## 19.33. Continuidad y ausencia de saltos

[]{#MA-EX-ANM-01-019-033}

[]{#MA-SOL-ANM-01-019-033}

C18 prueba derivabilidad de F en toda la recta, $F'$(0)=0 y $F'$(x_n)=-3/2 con x_n→0. Por tanto $F'$ no es continua en cero. Darboux se aplica entre cero y cada x_n>0 y obliga a que cualquier λ de (-3/2,0) aparezca en algún centro interior a ese segmento. No se necesita un mismo centro para diferentes n o λ. Los valores intermedios son compatibles con las pendientes persistentes de la ruta, pues no implican convergencia al valor central.

**Retorno visual.** Véase [C19-F07](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 19.34. Una derivada sin ceros tiene un signo

[]{#MA-EX-ANM-01-019-034}

[]{#MA-SOL-ANM-01-019-034}

Si hubiera un valor positivo y otro negativo, se ordenan sus centros como u<v. El cero queda estrictamente entre las dos derivadas y Darboux da un c intermedio con $f'(c)$=0, contradicción. En un intervalo no vacío se fija un centro; tricotomía y ausencia de ceros determinan su signo y excluyen el opuesto en todos los demás. R4 hace a f estrictamente creciente o decreciente según ese signo. No se deduce una separación uniforme de la derivada respecto de cero.

## 19.35. Un escalón no puede ser una derivada

[]{#MA-EX-ANM-01-019-035}

[]{#MA-SOL-ANM-01-019-035}

Si existiera f, los centros u=-1/2 y v=1/2 tendrían derivadas menos uno y uno. Darboux con λ=0 entregaría un c∈(-1/2,1/2) donde $f'(c)$=0. Pero h sólo toma los valores -1 y 1 en todo el dominio, contradicción. El argumento usa el valor intermedio de derivadas existentes, sin asumir que h sea continua y sin discutir únicamente la apariencia de su salto en un gráfico.

## 19.36. Inyectividad desde Rolle

[]{#MA-EX-ANM-01-019-036}

[]{#MA-SOL-ANM-01-019-036}

[]{#MA-SEC-ANM-01-019-008}

Si f(x)=f(y) para x<y, el segmento está en el intervalo y su restricción cumple Rolle, que produce c∈(x,y) con $f'(c)$=0, contradicción. Por tanto dos entradas distintas no tienen el mismo valor y f es inyectiva. No es necesario que esos valores comunes sean cero: Rolle sólo requiere igualdad de borde. La ausencia de derivadas nulas no prueba existencia de ninguna solución f(x)=b; únicamente permite a lo sumo una por valor de salida.

## 19.37. Contar ceros por segmentos vecinos

[]{#MA-EX-ANM-01-019-037}

[]{#MA-SOL-ANM-01-019-037}

Supongamos k+2 ceros distintos y ordenemos esa lista finita x0<…<x(k+1). En cada segmento vecino [xj,x(j+1)], continuidad, derivabilidad e igualdad de bordes cero permiten Rolle. Se obtienen k+1 puntos c_j en sus interiores con derivada cero; son distintos porque los interiores no se solapan. Esto contradice la cota k. Las aplicaciones son finitas, no una selección numerable de testigos. La prueba se refiere a ceros distintos, sin contar multiplicidad.

## 19.38. Existencia, unicidad y primera horquilla

[]{#MA-EX-ANM-01-019-038}

[]{#MA-SOL-ANM-01-019-038}

El polinomio es continuo y tiene valores -1 y 1 en los bordes; C15 da al menos un cero interior. Su derivada 3x²+1≥1 nunca se anula, así E036 prueba inyectividad y a lo sumo un cero. Se combinan ambos resultados para una raíz única r. Los valores exactos p(1/2)=-3/8 y p(3/4)=11/64 tienen signos opuestos y el mismo argumento de continuidad en ese subsegmento sitúa el cero en (1/2,3/4); la unicidad identifica ese cero con r. Rolle no reemplaza al valor intermedio en la parte de existencia.

## 19.39. Un máximo de tres ceros que se alcanza

[]{#MA-EX-ANM-01-019-039}

[]{#MA-SOL-ANM-01-019-039}

$q'$=3x²-3 se anula exactamente en -1 y 1, así R8 limita q a tres ceros distintos. Factorizar q=x(x²-3) muestra los tres valores -√3,0,√3, que efectivamente anulan q. La cota se alcanza en este ejemplo. La recíproca general es falsa: para Q=q+10 sobre [-2,2], la derivada conserva esos dos ceros interiores, pero sus valores se controlan por R4 en las piezas: Q(-2)=8,Q(-1)=12,Q(1)=8,Q(2)=12 y los signos de 3x²-3 dan mínimos al menos ocho, sin ceros. Dos puntos estacionarios no obligan a tres raíces.

## 19.40. Residuo convertido en distancia

[]{#MA-EX-ANM-01-019-040}

[]{#MA-SOL-ANM-01-019-040}

Por E038, r∈(1/2,3/4). El aproximante también está ahí y p(x)=8/27+2/3-1=-1/27. El crecimiento estricto de p da r>x. En el segmento que contiene ambos, 1/4≤t²≤9/16, así 7/4≤$p'(t)$≤43/16. R5 produce (7/4)(r-x)≤p(r)-p(x)=1/27≤(43/16)(r-x). Dividir por las constantes positivas da r-x≤4/189 y r-x≥16/1161. Se acota el error sin conocer el punto de valor medio ni tomar una cifra decimal de la gráfica. Las cotas de derivada se probaron en todos los centros del segmento.

**Retorno visual.** Véase [C19-F08](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 19](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html) · [Ejercicios](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global-microcontroles.html)
