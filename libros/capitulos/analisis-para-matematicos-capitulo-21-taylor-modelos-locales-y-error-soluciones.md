---
content-id: MA-BCH-0288
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-021-SOLUCIONES
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
title: Soluciones — Capítulo 21
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C21_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html)

## 21.1. Los coeficientes no se eligen a ojo

[]{#MA-EX-ANM-01-021-001}

[]{#MA-SOL-ANM-01-021-001}

[]{#MA-SEC-ANM-01-021-001}

Derivamos cada monomio con la regla de producto finito. Si $j>k$, su derivada es cero; si $j\le k$, es $k!/(k-j)!\,(t-c)^{k-j}$. En el centro se anulan los términos con $k>j$ y el término $k=j$ vale $j!$, incluida la potencia de exponente cero definida como1. Así $P^{(j)}(c)=j!a_j$. El factorial tiene copia real positiva por inducción, luego $a_j=f^{(j)}(c)/j!$ es el único valor posible. La suma finita con esos coeficientes existe como polinomio y cumple los datos al sustituir. La unicidad se limita a grado a lo sumo$n$.

La derivación de la suma es finita y se utiliza sólo en monomios enteros ya legitimados. La evaluación central selecciona un único coeficiente por cada orden. Esa relación triangular prueba existencia por construcción y unicidad dentro de la clase de grado a lo sumo $n$. Una función de grado mayor puede compartir los mismos datos.

## 21.2. El cubo visto desde uno

[]{#MA-EX-ANM-01-021-002}

[]{#MA-SOL-ANM-01-021-002}

Los datos son1,3,6,6 para órdenes0 a3. Por tanto $T_1=1+3h$, $T_2=1+3h+3h^2$ y $T_3=1+3h+3h^2+h^3$. La expansión finita de $(1+h)^3$ da restos $R_1=3h^2+h^3$, $R_2=h^3$ y $R_3=0$. Cada factorial convierte derivada en coeficiente; en orden3 se divide6 por6. Los órdenes bajos conservan sus datos aunque no igualen la función fuera del centro.

**Retorno visual.** Véase [C21-F01](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Los factoriales convierten las derivadas centrales en coeficientes de incrementos, no en los mismos números sin escala. Cada resto se obtiene restando su modelo de la expansión exacta. Aumentar el orden conserva más datos y aquí finalmente elimina el resto porque se conoce el polinomio completo.

## 21.3. Orden mayor que el grado

[]{#MA-EX-ANM-01-021-003}

[]{#MA-SOL-ANM-01-021-003}

Las derivadas centrales son2,−3,2 y luego0 para órdenes3 y4. El Taylor es $2-3t+t^2$, pues el coeficiente cuadrático es2/2=1 y los superiores son cero. Su grado es2, menor que4. Orden4 exige conservar los datos hasta ese orden, no que el último coeficiente sea no nulo. El resto es cero porque la función ya es ese polinomio.

Las derivadas superiores son datos legítimos aunque valgan cero. Los coeficientes de esos órdenes se anulan y no cambian el grado efectivo. La igualdad exacta con la función prueba resto cero sin necesitar un punto intermedio de Lagrange.

## 21.4. Mismos datos, salidas diferentes

[]{#MA-EX-ANM-01-021-004}

[]{#MA-SOL-ANM-01-021-004}

Cada derivada de la potencia de órdenes0 a$n$ contiene un factor positivo de grado al menos1 en$t-c$ y se anula en$c$. Así se conservan los datos. En$x\ne c$, el factor $(x-c)^{n+1}$ es no cero. Para imponer una salida$b$, tomamos $A=(b-P(x))/(x-c)^{n+1}$. La función resultante es un polinomio y tiene valor$b$ en$x$. No contradice la unicidad de Taylor porque su grado puede superar$n$.

La potencia adicional se anula junto con todas sus derivadas centrales hasta el orden fijado. En la entrada distinta su valor es no nulo y permite despejar el coeficiente libre. Se puede modificar cualquier salida fuera del centro manteniendo el modelo anterior, porque la clase resultante admite grados mayores.

## 21.5. Centro, dominio y factorial

[]{#MA-EX-ANM-01-021-005}

[]{#MA-SOL-ANM-01-021-005}

El centro0 pertenece al dominio declarado$t<1$; las derivadas centrales usadas deben existir, lo que aquí dan las reglas del cociente e inducción. Los denominadores$k!$ se leen como sus copias reales positivas, incluido0!=1. El polinomio puede evaluarse en cualquier real, pero el resto sólo en el dominio original. La definición únicamente iguala datos en0: para controlar el error fuera se necesita una fórmula o cota adicional. Cerca de la singularidad1, el margen del denominador puede ser arbitrariamente pequeño.

El contrato debe acreditar pertenencia del centro, existencia de los datos y lectura real de los factoriales. El polinomio definido por ellos no tiene una singularidad, pero la función sí pierde definición en uno. Una cota de error requiere controlar la región donde se comparan ambas y su distancia a esa singularidad.

## 21.6. El invariante de Rolle repetido

[]{#MA-EX-ANM-01-021-006}

[]{#MA-SOL-ANM-01-021-006}

[]{#MA-SEC-ANM-01-021-002}

Ponemos $z_0=x$. En el paso$k$, $H_k(c)=H_k(z_k)=0$ y$z_k\ne c$. La restricción al segmento de esos extremos es continua, y su derivada existe interiormente y coincide con la original. Rolle da$z_{k+1}$ estrictamente entre ambos con$H_k\prime(z_{k+1})=0$. Si$k<n$, la cadena convierte esa igualdad en$H_{k+1}(z_{k+1})=0$, mientras$H_{k+1}(c)=0$ era dato, y permite continuar. En el paso$n$ se obtiene la derivada final nula. Hay$n+1$ pasos, de0 a$n$. La longitud es finita y fijada de antemano.

En cada paso el dato central nulo pertenece al nuevo miembro y el testigo anterior aporta su otro cero. La relación de derivadas transmite la conclusión y la posición estricta conserva extremos distintos. El número finito de pasos evita una selección simultánea de testigos para una familia infinita.

## 21.7. Una cadena de tres puntos

[]{#MA-EX-ANM-01-021-007}

[]{#MA-SOL-ANM-01-021-007}

Expandimos$H=t^3-t^4$. Sus derivadas son$H\prime=3t^2-4t^3$, $H\prime\prime=6t-12t^2$ y$H^{(3)}=6-24t$. En0, $H,H\prime,H\prime\prime$ valen0 y$H(1)=0$. Evaluar da$H\prime(3/4)=0$, $H\prime\prime(1/2)=0$ y$H^{(3)}(1/4)=0$. Se cumple$0<1/4<1/2<3/4<1$, de modo que cada punto está entre el centro y el punto anterior. La cadena realiza tres aplicaciones para$n=2$; sus valores exactos no son prescritos por el lema general.

**Retorno visual.** Véase [C21-F02](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las tres anulaciones centrales preparan el orden dos y el cero en uno inicia el segmento. Los puntos explícitos satisfacen además las inclusiones estrictas requeridas por la cadena. Las cuentas verifican este ejemplo, pero el lema general sólo proporciona existencias y no prescribe esas fracciones.

## 21.8. Un dato central que no puede perderse

[]{#MA-EX-ANM-01-021-008}

[]{#MA-SOL-ANM-01-021-008}

Tomamos$H(t)=t(1-t)$. Tiene bordes0 y0, y Rolle da un cero de$H\prime=1-2t$ en1/2. Sin embargo$H\prime(0)=1$, no cero, y$H\prime\prime=-2$ no se anula en el interior. Falta el borde central nulo del segundo miembro de la cadena, así no se puede repetir Rolle entre0 y1/2. La igualdad de valores de la función no basta para toda la cadena.

La primera aplicación de Rolle se mantiene válida porque los bordes de $H$ son iguales. La segunda necesitaría igualdad de valores de $H\prime$ entre el centro y el testigo obtenido, y esa premisa falta. La segunda derivada constante no nula muestra que la conclusión no puede repararse sólo con los ceros iniciales.

## 21.9. Rolle hacia la izquierda

[]{#MA-EX-ANM-01-021-009}

[]{#MA-SOL-ANM-01-021-009}

Tenemos$H(0)=H\prime(0)=0$ y$H(-1)=0$. La primera derivada$3t^2+2t=t(3t+2)$ se anula interiormente en$z_1=-2/3$. La segunda$6t+2$ se anula en$z_2=-1/3$, estrictamente entre−2/3 y0. La cadena cumple$-1<-2/3<-1/3<0$: se acerca al centro por la izquierda. Cada aplicación usa el segmento con extremos ordenados mediante mínimo y máximo; no se invierte una hipótesis de continuidad o interioridad.

El segmento se escribe con extremos ordenados aunque el avance hacia el centro sea de izquierda a derecha. Los dos testigos permanecen interiores en sus respectivos subsegmentos. La fórmula de las derivadas confirma cada anulación y no se cambia el sentido de una hipótesis por tener incremento negativo.

## 21.10. Qué continuidad consume cada paso

[]{#MA-EX-ANM-01-021-010}

[]{#MA-SOL-ANM-01-021-010}

Cada$H_k$ se usa como función de un Rolle sobre un subsegmento, así necesita continuidad incluyendo sus extremos. Para$k<n$ su derivabilidad interior y la igualdad$H_k\prime=H_{k+1}$ permiten enlazar el próximo miembro. El último$H_n$ necesita derivabilidad interior, pero Rolle no exige continuidad de$H_n\prime$ ni su existencia en bordes. El proceso fija$n$ y construye sólo$n+1$ existencias, mediante inducción finita; no define un selector para todas las entradas o todos los órdenes simultáneamente.

Los papeles de función y derivada cambian al pasar al siguiente miembro. Cada nueva función de Rolle debe tener continuidad en sus dos bordes, pero la última derivada no necesita ese control como función de otro paso. La prueba declara un orden fijo y termina antes de exigir una continuidad adicional no prevista.

## 21.11. El auxiliar que obliga a la igualdad

[]{#MA-EX-ANM-01-021-011}

[]{#MA-SOL-ANM-01-021-011}

[]{#MA-SEC-ANM-01-021-003}

Si$x=c$, el resto es0 por los datos centrales y no se pide testigo interior. Si$x\ne c$, definimos$A=R(x)/(x-c)^{n+1}$, con denominador no cero. Esto hace$H(x)=0$. Los datos de Taylor y la potencia de grado$n+1$ dan$H^{(k)}(c)=0$ para$k\le n$. Bajo el contrato diferencial, los primeros miembros son continuos y sus derivadas enlazan; Rolle repetido da$H^{(n+1)}(\xi)=0$. La derivada final del polinomio es0 y la de la potencia es$(n+1)!$, así$A=f^{(n+1)}(\xi)/(n+1)!$. Este factorial real es positivo, por lo que se puede despejar. Sustituimos$A$ para obtener la fórmula.

El caso central se separa antes de introducir la división por el incremento. En el caso perforado, el auxiliar se diseña para conservar toda la cadena de ceros centrales y anularse en la entrada final. La última derivada nula determina su coeficiente libre. Sustituirlo produce la fórmula sin asumirla durante la construcción.

## 21.12. Un testigo que no es el medio

[]{#MA-EX-ANM-01-021-012}

[]{#MA-SOL-ANM-01-021-012}

$T_{1,0}=0$, así$R(1)=1$. La fórmula dice$1=f\prime\prime(\xi)/2=6\xi/2=3\xi$, de donde$\xi=1/3$. Pertenece estrictamente a$(0,1)$ pero no es el medio1/2. Este caso tiene un único testigo porque la segunda derivada es estrictamente creciente. No se infiere unicidad del teorema general.

**Retorno visual.** Véase [C21-F03](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La segunda derivada del cubo cambia con el testigo, por lo que la ecuación del resto identifica aquí una fracción concreta. El medio produciría un valor diferente y no satisface la igualdad. Unicidad en este ejemplo procede de esa ecuación, no de una afirmación general del teorema.

## 21.13. Una derivada constante deja muchos testigos

[]{#MA-EX-ANM-01-021-013}

[]{#MA-SOL-ANM-01-021-013}

La expansión exacta da$R=(x-1)^3$. La tercera derivada es6 en cada punto, de modo que$[f^{(3)}(\xi)/3!](x-1)^3=(x-1)^3$ para cualquier$\xi$ estrictamente interior. Hay infinitos puntos posibles en ese segmento y ninguna unicidad. El teorema garantiza uno; una fórmula constante puede hacer válidos todos.

La tercera derivada constante hace que el factor de Lagrange sea siempre uno después de dividir por el factorial. Por ello cualquier testigo interior reproduce el mismo resto cúbico. La fórmula puede ser exacta y admitir muchos testigos a la vez. Existencia no equivale a elección única.

## 21.14. Un centro fronterizo sin última derivada

[]{#MA-EX-ANM-01-021-014}

[]{#MA-SOL-ANM-01-021-014}

Los miembros son$f_0=t^2\sqrt t$, $f_1=(5/2)t\sqrt t$ y$f_2=(15/4)\sqrt t$, con valores0 en el borde. Son continuos sobre$[0,1]$ y las relaciones de derivación se cumplen en$(0,1)$. La derivada$f_2\prime=(15/8)/\sqrt t$ existe interiormente aunque no es finita en0. El contrato cerrado legitima Taylor de orden2 para$x>0$, usando los valores centrales dados; la derivada final se evalúa sólo en un testigo interior. No se obtiene por eso una cota uniforme de tercera derivada cerca de0.

Los tres miembros dados tienen límites centrales cero y proporcionan las extensiones continuas requeridas por el contrato cerrado. Sus relaciones de derivación se verifican en entradas positivas. La última derivada sólo debe existir en el testigo interior y no tiene por qué extenderse finitamente al borde. Su crecimiento cerca de cero impide una barrera uniforme allí.

## 21.15. El caso de orden cero

[]{#MA-EX-ANM-01-021-015}

[]{#MA-SOL-ANM-01-021-015}

El polinomio es$T_{0,c}=f(c)$ y1!=1, de modo que$f(x)-f(c)=f\prime(\xi)(x-c)$. Para$x\ne c$ esto es exactamente Lagrange sobre el segmento. Se conserva continuidad incluyendo ambos extremos y derivabilidad interior; el carácter intervalar asegura que el segmento está en el dominio. Para$x=c$ hay igualdad de valores sin testigo entre extremos coincidentes. La reducción no elimina ninguna de esas condiciones.

El factorial y el incremento reducen la fórmula a la igualdad de valor medio, pero conservan sus condiciones de dominio. Un segmento no degenerado necesita continuidad de bordes y derivabilidad interior. En el centro coincidente el resto se anula directamente y no se añade un testigo inexistente.

## 21.16. Una cota que no necesita máximo

[]{#MA-EX-ANM-01-021-016}

[]{#MA-SOL-ANM-01-021-016}

[]{#MA-SEC-ANM-01-021-004}

Para$x\ne c$, tomamos valores absolutos en$R=f^{(n+1)}(\xi)(x-c)^{n+1}/(n+1)!$ y aplicamos la cota universal en$\xi$. Resulta$|R|\le M|x-c|^{n+1}/(n+1)!$. Si$x=c$, ambos lados son0. Si$M=0$, la desigualdad fuerza$R=0$ sin dividir por$M$. Una cota suministrada controla todos los valores posibles del testigo; no se necesita obtenerla como máximo alcanzado ni presuponer continuidad de la derivada final.

La barrera de la derivada final se declara antes del testigo y sirve para cualquiera de sus posiciones admisibles. Tomar magnitudes produce una cota no estricta sin pedir que la barrera se alcance. Los casos central y de barrera cero se verifican directamente. Así no se usa continuidad de la última derivada para fabricar un máximo.

## 21.17. La cancelación de Cauchy

[]{#MA-EX-ANM-01-021-017}

[]{#MA-SOL-ANM-01-021-017}

Derivamos la suma finita. La parte que deriva$f^{(k)}$ es$\sum_{k=0}^n f^{(k+1)}(t)(x-t)^k/k!$; la que deriva la potencia es$-\sum_{k=1}^n f^{(k)}(t)(x-t)^{k-1}/(k-1)!$. Tras reindexar la segunda, se cancelan todos salvo el término superior de la primera. Como$G$ es negativo de la suma más una constante,$G\prime=-f^{(n+1)}(t)(x-t)^n/n!$. Se tiene$G(x)=0$ y$G(c)=R$. Lagrange sobre$G$ da$-R=G\prime(\eta)(x-c)$; sustituir produce$R=f^{(n+1)}(\eta)(x-\eta)^n(x-c)/n!$.

**Retorno visual.** Véase [C21-F04](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La entrada $x$ permanece fija al derivar respecto de $t$. La cancelación se verifica reindexando dos sumas finitas, con un único término superior restante. Después se auditan las condiciones de valor medio para $G$. Sus valores de borde permiten obtener el resto con su signo correcto.

## 21.18. Una banda que cambia de orientación

[]{#MA-EX-ANM-01-021-018}

[]{#MA-SOL-ANM-01-021-018}

El coeficiente$R/(x-c)^3$ queda entre2/6=1/3 y6/6=1. Si$x>c$, la potencia es positiva y$(x-c)^3/3\le R\le(x-c)^3$. Si$x<c$, la potencia es negativa y se invierte el orden:$(x-c)^3\le R\le(x-c)^3/3$. En el centro$R=0$. En ambos lados la cota absoluta$|R|\le|x-c|^3$ sigue siendo válida, pero la banda firmada retiene el signo.

El intervalo de coeficientes se obtiene dividiendo por el factorial positivo. La potencia cúbica conserva o invierte la orientación según el lado de la entrada. En el centro no se divide y el resto es cero. La banda firmada aporta información de signo que se pierde al tomar sólo magnitudes.

## 21.19. Testigos diferentes para el mismo error

[]{#MA-EX-ANM-01-021-019}

[]{#MA-SOL-ANM-01-021-019}

El resto es1. Lagrange dio$\xi=1/3$. Cauchy exige$1=6\eta(1-\eta)$; las soluciones$\eta=(1\pm1/\sqrt3)/2$ pertenecen a$(0,1)$ y ambas sirven. Ninguna es1/3. Con$M=6$, Lagrange da$|R|\le6/2=3$, mientras la estimación constante de Cauchy da$|R|\le6/1=6$. Ambas cotas son correctas aunque poco ajustadas frente al error exacto1; sus puntos y factores no se intercambian.

Las auxiliares distintas producen ecuaciones diferentes para sus testigos. Resolverlas y comprobar interioridad acredita sus ubicaciones en este ejemplo. Las cotas resultantes pueden ser poco ajustadas y seguir siendo válidas. No se intercambian los factores de una fórmula con los puntos de la otra.

## 21.20. Una región antes de una entrada

[]{#MA-EX-ANM-01-021-020}

[]{#MA-SOL-ANM-01-021-020}

Para cada entrada$x$ del segmento, la prueba de Lagrange se aplica a su subsegmento con$c$. Su testigo pertenece al interior de la región completa, donde vale la misma$M$. Así$|R(x)|\le M|x-c|^{n+1}/(n+1)!\le M\rho^{n+1}/(n+1)!$. El caso central es0. La cota se eligió antes de$x$ y sirve para todas las entradas, sin seleccionar sus testigos simultáneamente. Una muestra finita sólo acota valores muestreados, no cualquier ubicación interior que puede producir el teorema.

Para cada entrada el segmento que la une al centro está dentro de la región protegida. La misma barrera sirve para cualquier testigo interior de cualquiera de esos segmentos. La distancia máxima $\rho$ convierte el control puntual en uno común. No se eligen simultáneamente testigos ni se infiere la barrera de una muestra finita.

## 21.21. Peano por Cauchy e inducción

[]{#MA-EX-ANM-01-021-021}

[]{#MA-SOL-ANM-01-021-021}

[]{#MA-SEC-ANM-01-021-005}

Los datos centrales de$H$ hasta orden$n$ son0. El resultado de orden$n-1$ aplicado a$H\prime$ da$H\prime(c+u)=o(|u|^{n-1})$. Para$\varepsilon>0$ tomamos un radio donde$|H\prime(c+u)|<n\varepsilon|u|^{n-1}$. Para$0<|h|$ dentro del radio, Cauchy en$H$ y$(t-c)^n$ da$H(c+h)/h^n=H\prime(\xi)/[n(\xi-c)^{n-1}]$. El testigo no es$c$, así la derivada del denominador no se anula; el incremento$h^n$ tampoco. La cota inductiva hace al valor absoluto del cociente menor que$\varepsilon$. Se requiere que$H\prime$ exista en el segmento, garantizado por las hipótesis inferiores para$n\ge2$.

La inducción aplicada a $H\prime$ controla su error respecto de la escala de orden $n-1$. Cauchy lo relaciona con la razón del valor de $H$ por el monomio de orden $n$. El testigo distinto del centro legitima el denominador derivado. El presupuesto con factor $n$ se cancela y entrega exactamente la tolerancia requerida.

## 21.22. Peano sin un orden cúbico de error

[]{#MA-EX-ANM-01-021-022}

[]{#MA-SOL-ANM-01-021-022}

$f(0)=0$ y$f(h)/h=\operatorname{sgn}(h)|h|^{3/2}\to0$, así$f\prime(0)=0$. Fuera de0,$f\prime(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$. Dividir por$h$ da$(5/2)\sqrt{|h|}\to0$, luego$f\prime\prime(0)=0$. El Taylor de orden2 es cero. El cociente$f(h)/|h|^2=\sqrt{|h|}$ tiende a0, pero$f(h)/|h|^3=1/\sqrt{|h|}$ excede cualquier constante finita tomando entradas suficientemente pequeñas. El resultado es Peano sin una cota uniforme del siguiente orden.

**Retorno visual.** Véase [C21-F05](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las derivadas centrales se verifican mediante cocientes y no diferenciando una abreviatura asintótica. El resto cuadrático normalizado queda como raíz de magnitud y tiende a cero. Compararlo con el orden cúbico deja un recíproco que crece sin barrera. La misma función separa con precisión ambas garantías de error.

## 21.23. Error absoluto y error normalizado

[]{#MA-EX-ANM-01-021-023}

[]{#MA-SOL-ANM-01-021-023}

Ambas funciones tienden a0 en valor absoluto. Pero$|r(h)|/|h|^n=1$ en todas las entradas perforadas, así no tiende a0 y$r$ no es$o(|h|^n)$. En cambio$|s(h)|/|h|^n=|h|\to0$, y$s$ sí tiene esa propiedad. Peano mide error respecto de una escala, no sólo tamaño absoluto.

La convergencia absoluta de los dos errores sólo afirma que sus valores se hacen pequeños. La normalización pregunta si son pequeños en comparación con una escala fijada. Uno conserva razón de magnitud uno y el otro añade un factor de distancia que desaparece. Por ello sólo el segundo cumple Peano al orden solicitado.

## 21.24. Un modelo asintótico también es único

[]{#MA-EX-ANM-01-021-024}

[]{#MA-SOL-ANM-01-021-024}

La resta y la triangular dan$P-Q=o(|h|^n)$. Si el polinomio diferencia fuera no cero, tendría un término de menor grado$j\le n$ con coeficiente$a\ne0$: $P-Q=h^j(a+hB(h))$. Por continuidad del polinomio$B$, el factor interior tiende a$a$ y su valor absoluto es al menos$|a|/2$ en un radio. Dividir por$|h|^n$ da al menos$(|a|/2)|h|^{j-n}$, que no tiende a0: si$j=n$ es constante positiva y si$j<n$ crece sin cota. Contradicción. No se utilizó una regla de derivación para$o$.

El menor grado no nulo del polinomio diferencia domina sus otros términos cerca de cero. La continuidad del factor restante protege su magnitud por una constante positiva. Después de normalizar, esa barrera no desaparece para ningún grado hasta $n$. Esto contradice el error pequeño y prueba igualdad sin derivar los restos.

## 21.25. Un radio para un error de raíz

[]{#MA-EX-ANM-01-021-025}

[]{#MA-SOL-ANM-01-021-025}

Como$|f(h)|/|h|^2=\sqrt{|h|}$, tomamos$\delta=\varepsilon^2$ o el mínimo con un radio de dominio. Para$0<|h|<\delta$ se cumple$\sqrt{|h|}<\varepsilon$ y la desigualdad requerida. Esto prueba Peano de orden2 con radio explícito para este ejemplo. No produce una constante cúbica: el cociente por$|h|^3$ sigue siendo$1/\sqrt{|h|}$, arbitrariamente grande.

El radio cuadrático se diseña a partir de la precisión del error normalizado. Multiplicar la desigualdad de raíz por la escala positiva devuelve el error de valor pedido. El cociente del siguiente orden sigue sin barrera, así el mismo radio no acredita una tasa cúbica uniforme.

## 21.26. Dominar el resto para decidir un signo

[]{#MA-EX-ANM-01-021-026}

[]{#MA-SOL-ANM-01-021-026}

[]{#MA-SEC-ANM-01-021-006}

Como$a\ne0$, elegimos$\varepsilon=|a|/2$ en la condición$o$. En el radio resultante el error tiene magnitud menor que la mitad del término principal. Si$m$ es par, éste tiene signo$a$ en ambos lados, y la suma conserva ese signo: mínimo estricto para$a>0$ y máximo estricto para$a<0$. Si$m$ es impar, el principal cambia de signo de un lado a otro y el error no puede invertirlo; hay salidas mayores y menores arbitrariamente próximas. El centro debe ser interior para disponer de ambos lados.

La mitad del coeficiente principal reserva un margen para que el resto no anule su signo. La paridad decide entonces las comparaciones de valores disponibles a ambos lados. Interioridad permite usar esas dos direcciones en el caso impar. La conclusión es local en el radio proporcionado por Peano.

## 21.27. Cuarto poder frente a cubo

[]{#MA-EX-ANM-01-021-027}

[]{#MA-SOL-ANM-01-021-027}

Para$x^4$, las primeras tres derivadas centrales son0 y la cuarta vale24; su coeficiente es24/4!=1. El orden par positivo da mínimo local estricto, y directamente$x^4>0$ para$x\ne0$. Para$x^3$, las primeras dos son0 y la tercera6, de coeficiente1. El orden impar da ausencia de extremo interior; directamente$x^3$ es negativo a la izquierda y positivo a la derecha. Una pendiente central cero común no distingue estos casos.

**Retorno visual.** Véase [C21-F06](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La primera derivada no nula se convierte en coeficiente uno después de dividir por su factorial. El exponente par del cuarto poder mantiene signo positivo y el impar del cubo lo cambia. La comprobación directa de valores confirma las conclusiones y muestra por qué pendiente cero por sí sola no las distingue.

## 21.28. Datos nulos con tres respuestas

[]{#MA-EX-ANM-01-021-028}

[]{#MA-SOL-ANM-01-021-028}

Tomamos$p=h^{2(n+1)}$, $q=-h^{2(n+1)}$ y$r=h^{2(n+1)+1}$. Todos los exponentes superan$n$, por lo que el valor y las derivadas hasta ese orden se anulan en0. El primero es positivo en entradas no nulas y tiene mínimo estricto; el segundo negativo y tiene máximo estricto; el tercero cambia de signo y no tiene extremo interior. La falta de datos no nulos disponibles impide aplicar el criterio, no demuestra que no exista un extremo.

Los exponentes elegidos superan el orden de todos los datos que se desean conservar. Sus signos en entradas no nulas deciden tres comportamientos distintos. La lista finita de datos nulos es compatible con todos ellos. El criterio no clasifica cuando falta un primer término no nulo disponible.

## 21.29. El mínimo que no gobierna toda la recta

[]{#MA-EX-ANM-01-021-029}

[]{#MA-SOL-ANM-01-021-029}

El primer orden no nulo es2, con$q\prime\prime(0)=2>0$, por lo que el criterio local da mínimo estricto. Directamente$q=h^2(1-h^2)>0$ para$0<|h|<1$. Pero$q(2)=4-16=-12<0$, así0 no es mínimo global. La segunda derivada$2-12h^2$ se vuelve negativa; no hay convexidad global que permita utilizar el soporte horizontal de C20. Un dato central positivo no reemplaza esa propiedad en todo el intervalo.

La cota local se verifica mientras el factor $1-h^2$ sea positivo. Fuera de esa región hay una salida menor que la central y se refuta mínimo global. La curvatura negativa en zonas lejanas impide usar soporte convexo global. Un dato central positivo no sustituye esa hipótesis en toda la recta.

## 21.30. El orden impar en una frontera

[]{#MA-EX-ANM-01-021-030}

[]{#MA-SOL-ANM-01-021-030}

La función tiene primer coeficiente1 y orden1 impar, pero el dominio sólo ofrece incrementos$h\ge0$ desde el centro0. Para$h>0$, el término principal$h$ es positivo y no hay entradas negativas que produzcan el signo contrario. En$[0,1]$, la función alcanza mínimo único en0. Un desarrollo unilateral con error menor que la mitad del término principal certifica el signo en el lado disponible; la conclusión de ausencia de extremo del criterio impar requería centro interior y acumulación bilateral.

El dominio de frontera sólo admite el lado positivo del incremento. La comparación de término principal y resto puede preservar su signo en ese lado sin producir ninguna salida negativa. Esa versión unilateral permite un mínimo relativo. La conclusión impar interior necesitaba precisamente las entradas del lado ausente.

## 21.31. Una identidad geométrica todavía finita

[]{#MA-EX-ANM-01-021-031}

[]{#MA-SOL-ANM-01-021-031}

[]{#MA-SEC-ANM-01-021-007}

Inducción con cociente y producto da$f^{(k)}=k!/(1-h)^{k+1}$; al evaluar en0 el coeficiente de Taylor es1. Multiplicar la suma finita por$1-h$ cancela términos vecinos y deja$1-h^{n+1}$. Como$1-h\ne0$ en el dominio$h<1$, despejamos la función y obtenemos resto$h^{n+1}/(1-h)$. No se tomó un límite de sumas ni se identificó una serie infinita.

La inducción de coeficientes y la identidad geométrica usan únicamente operaciones finitas. El resto exacto conserva el denominador de la función y exige no anulación. No se ha justificado una serie infinita al escribir el modelo. Cada orden dispone de su propia identidad y región de control.

## 21.32. La raíz y su tercera derivada

[]{#MA-EX-ANM-01-021-032}

[]{#MA-SOL-ANM-01-021-032}

Por C18, $g\prime=1/(2\sqrt{1+h})$, $g\prime\prime=-1/[4(1+h)\sqrt{1+h}]$ y$g^{(3)}=3/[8(1+h)^2\sqrt{1+h}]$. En0 se obtienen1,1/2,−1/4, luego$T_2=1+h/2-h^2/8$. En el segmento$1+h\ge3/4$ y su raíz positiva es al menos3/4, pues$(3/4)^2\le3/4$. El denominador de la tercera derivada es al menos$8(3/4)^3=27/8$; el cociente queda a lo sumo8/9 y es positivo. No usamos derivación de una potencia real general.

Las reglas de raíz y recíproco se aplican en entradas mayores que menos uno, donde los denominadores son positivos. Los datos centrales dan el coeficiente cuadrático menos un octavo. Las barreras racionales inferiores del denominador producen el control de tercera derivada en toda la región, incluso sin conocer raíces exactas de sus entradas.

## 21.33. Un intervalo racional para una raíz

[]{#MA-EX-ANM-01-021-033}

[]{#MA-SOL-ANM-01-021-033}

En$h=1/4$, $T_2=1+1/8-1/128=143/128$. La cota de tercera derivada8/9 da$|R_2|\le(8/9)(1/4)^3/6=1/432$. Como la tercera derivada es positiva en todo el segmento y el incremento cúbico es positivo, $R_2>0$. Así$143/128<\sqrt{5/4}\le143/128+1/432$. La primera desigualdad es estricta por signo; la segunda sólo es una cota superior no estricta. No se extrajo una raíz aproximada del dibujo.

**Retorno visual.** Véase [C21-F07](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La entrada un cuarto queda dentro de la región controlada y el testigo es interior a su segmento con cero. La tercera derivada positiva y el incremento cúbico positivo hacen estricto el borde inferior del certificado. La cota absoluta sólo da desigualdad débil en el superior. Las fracciones proceden de sustituciones exactas.

## 21.34. Un cotejo por racionalización

[]{#MA-EX-ANM-01-021-034}

[]{#MA-SOL-ANM-01-021-034}

La diferencia es$5/4-20449/16384=31/16384>0$, por lo que el aproximante es inferior a la raíz positiva. Racionalizar da error$31/[16384(\sqrt{5/4}+143/128)]$. Como la raíz es al menos1, el denominador es al menos$16384(271/128)=34688$, y el error es a lo sumo31/34688. Para comparar, $31\cdot432=13392<34688$, así31/34688<1/432. La cota algebraica es más ajustada; ambas certifican el mismo aproximante con premisas distintas.

La diferencia positiva de cuadrados compara dos cantidades no negativas y determina el sentido del error. La racionalización lo expresa como cociente por una suma protegida. Una cota inferior sencilla de la raíz basta para obtener una barrera racional más pequeña. El cotejo es independiente del testigo de Taylor.

## 21.35. La singularidad impone el margen

[]{#MA-EX-ANM-01-021-035}

[]{#MA-SOL-ANM-01-021-035}

El resto exacto es$h^{n+1}/(1-h)$. En la región declarada, $1-h\ge1-\rho>0$ y$|h|^{n+1}\le\rho^{n+1}$, así$|R|\le\rho^{n+1}/(1-\rho)$. Para$n$ fijo, si$h\uparrow1$, el numerador tiende a1 y el denominador positivo a0. Por ejemplo, para$h$ suficientemente próximo el numerador supera1/2, y tomar$1-h$ menor que$1/(2B)$ hace al resto mayor que cualquier$B>0$. El margen de dominio no puede borrarse.

El margen $1-\rho$ limita el denominador uniformemente sólo en la región fijada. Al acercarse a la singularidad ese margen desaparece y el numerador del resto no tiende a cero para un orden fijo. Una barrera de error previa puede entonces infringirse con entradas todavía válidas. No se elimina una condición de dominio al conservar la fórmula.

## 21.36. Multiplicar modelos sin derivar errores

[]{#MA-EX-ANM-01-021-036}

[]{#MA-SOL-ANM-01-021-036}

[]{#MA-SEC-ANM-01-021-008}

El producto exacto es$PQ+Pv+Qu+uv$. Los polinomios están acotados cerca de0; por ello los cocientes normalizados de$Pv$ y$Qu$ tienden a0. También$v\to0$ y$|uv|/|h|^n=(|u|/|h|^n)|v|\to0$. Eliminar términos de grado mayor que$n$ de$PQ$ añade un error$h^{n+1}B(h)$ con$B$ polinómico acotado; normalizar deja un factor$|h|$ y tiende a0. La triangular reúne esos errores. No se derivaron$u,v$ ni se supuso que sus derivadas fueran pequeñas.

La expansión exacta del producto exhibe sus tres errores antes de estimarlos. Las barreras de polinomios y la convergencia de razones normalizadas controlan los términos cruzados. Los términos truncados tienen grado superior y aportan otro error pequeño. Ningún paso requiere derivadas de los restos.

## 21.37. Sustitución con denominador protegido

[]{#MA-EX-ANM-01-021-037}

[]{#MA-SOL-ANM-01-021-037}

Pongamos$d=1-h-h^2$, que es al menos11/16 en la región. Por cociente,$F\prime=(1+2h)/d^2$, de valor1 en0; derivar da$F\prime\prime=2/d^2+2(1+2h)^2/d^3$, de valor4 en0. Así$T_2=1+h+2h^2$. La identidad$(1+h+2h^2)d=1-3h^3-2h^4$ da resto$(3h^3+2h^4)/d$. Su magnitud es a lo sumo$(3+2/4)|h|^3/(11/16)=(56/11)|h|^3$. El margen protege tanto la función como su certificado.

El denominador se protege mediante una desigualdad en toda la región antes de aplicar reglas de cociente. Los datos centrales y la multiplicación del modelo por ese denominador verifican coeficientes y resto. La barrera once dieciseisavos permite convertir la identidad en cota cúbica. Es una garantía uniforme de región, no una cuenta aislada.

## 21.38. Elegir el menor grado certificado

[]{#MA-EX-ANM-01-021-038}

[]{#MA-SOL-ANM-01-021-038}

La cota exacta uniforme es$1/(3\cdot4^n)$ y se alcanza en$h=1/4$. Para$n=4$ vale1/768>1/1000; para$n=5$ vale1/3072<1/1000. Como cada aumento divide por4, ningún orden menor que4 puede servir, y4 tampoco: el mínimo es5. El polinomio en1/4 es la suma de seis términos$1+1/4+1/16+1/64+1/256+1/1024=1365/1024$. La función vale4/3; la diferencia es$(4096-4095)/3072=1/3072$.

La cota exacta se alcanza en la entrada positiva un cuarto. Por eso el fracaso del orden cuatro es un error real en una entrada, no sólo falta de un certificado. La reducción geométrica de las cotas descarta también todos los órdenes menores. El orden cinco cumple la tolerancia estricta y su valor se verifica con seis términos finitos.

## 21.39. Trasladar un centro conocido

[]{#MA-EX-ANM-01-021-039}

[]{#MA-SOL-ANM-01-021-039}

En centro2, con$u=t-2$, la identidad$(2+u)^3=8+12u+6u^2+u^3$ da los datos y todos los coeficientes. En centro1, con$h=t-1$, eran$1+3h+3h^2+h^3$. Se relacionan sustituyendo$h=1+u$, porque conocemos la función polinómica completa y el resto de orden3 es0. Para una función general, el modelo central finito conserva sólo datos en su centro y lleva un resto fuera de él. Trasladarlo sin controlar ese resto puede cambiar incluso el valor y las derivadas en el nuevo centro.

El traslado exacto utiliza la identidad del cubo completo, cuyo resto al orden tres es cero. Sustituir la relación entre incrementos reexpande sus términos sin perder información. En una función general el resto puede alterar incluso la evaluación en el nuevo centro. Por ello trasladar un modelo finito exige datos o control adicional.

## 21.40. Muestras y datos que no determinan otra salida

[]{#MA-EX-ANM-01-021-040}

[]{#MA-SOL-ANM-01-021-040}

El producto es polinómico. Multiplicarlo por$h^{n+1}$ garantiza un factor de grado al menos$n+1$ en0, de modo que todas las derivadas centrales hasta$n$ se anulan. En cada$h_j$ hay un factor cero y se conserva$P(h_j)$. En$h_*$ distinto de0 y de todas las muestras, el factor$B=h_*^{n+1}\prod_j(h_*-h_j)^2$ es no cero. Para imponer salida$b$, elegimos$A=(b-P(h_*))/B$. Es una construcción finita, también con producto vacío1 si$m=0$. Conservar esos datos no certifica por sí solo un error en una región completa ni una representación infinita.

**Retorno visual.** Véase [C21-F08](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Los factores de muestra conservan sus evaluaciones y la potencia central conserva las derivadas hasta el orden declarado. En una entrada distinta de todas ellas el producto es no nulo y se puede despejar el coeficiente libre. El caso de ninguna muestra adicional usa producto vacío uno. La construcción muestra los valores de región que una tabla y datos centrales finitos dejan indeterminados.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html)

