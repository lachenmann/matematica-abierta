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
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C21_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)

## 21.1. Los coeficientes no se eligen a ojo

[]{#MA-EX-ANM-01-021-001}

[]{#MA-SOL-ANM-01-021-001}

[]{#MA-SEC-ANM-01-021-001}

Derivamos cada monomio con la regla de producto finito. Si $j>k$, su derivada es cero; si $j\le k$, es $k!/(k-j)!\,(t-c)^{k-j}$. En el centro se anulan los términos con $k>j$ y el término $k=j$ vale $j!$, incluida la potencia de exponente cero definida como1. Así $P^{(j)}(c)=j!a_j$. El factorial tiene copia real positiva por inducción, luego $a_j=f^{(j)}(c)/j!$ es el único valor posible. La suma finita con esos coeficientes existe como polinomio y cumple los datos al sustituir. La unicidad se limita a grado a lo sumo$n$.

## 21.2. El cubo visto desde uno

[]{#MA-EX-ANM-01-021-002}

[]{#MA-SOL-ANM-01-021-002}

Los datos son1,3,6,6 para órdenes0 a3. Por tanto $T_1=1+3h$, $T_2=1+3h+3h^2$ y $T_3=1+3h+3h^2+h^3$. La expansión finita de $(1+h)^3$ da restos $R_1=3h^2+h^3$, $R_2=h^3$ y $R_3=0$. Cada factorial convierte derivada en coeficiente; en orden3 se divide6 por6. Los órdenes bajos conservan sus datos aunque no igualen la función fuera del centro.

**Retorno visual.** Véase [C21-F01](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 21.3. Orden mayor que el grado

[]{#MA-EX-ANM-01-021-003}

[]{#MA-SOL-ANM-01-021-003}

Las derivadas centrales son2,−3,2 y luego0 para órdenes3 y4. El Taylor es $2-3t+t^2$, pues el coeficiente cuadrático es2/2=1 y los superiores son cero. Su grado es2, menor que4. Orden4 exige conservar los datos hasta ese orden, no que el último coeficiente sea no nulo. El resto es cero porque la función ya es ese polinomio.

## 21.4. Mismos datos, salidas diferentes

[]{#MA-EX-ANM-01-021-004}

[]{#MA-SOL-ANM-01-021-004}

Cada derivada de la potencia de órdenes0 a$n$ contiene un factor positivo de grado al menos1 en$t-c$ y se anula en$c$. Así se conservan los datos. En$x\ne c$, el factor $(x-c)^{n+1}$ es no cero. Para imponer una salida$b$, tomamos $A=(b-P(x))/(x-c)^{n+1}$. La función resultante es un polinomio y tiene valor$b$ en$x$. No contradice la unicidad de Taylor porque su grado puede superar$n$.

## 21.5. Centro, dominio y factorial

[]{#MA-EX-ANM-01-021-005}

[]{#MA-SOL-ANM-01-021-005}

El centro0 pertenece al dominio declarado$t<1$; las derivadas centrales usadas deben existir, lo que aquí dan las reglas del cociente e inducción. Los denominadores$k!$ se leen como sus copias reales positivas, incluido0!=1. El polinomio puede evaluarse en cualquier real, pero el resto sólo en el dominio original. La definición únicamente iguala datos en0: para controlar el error fuera se necesita una fórmula o cota adicional. Cerca de la singularidad1, el margen del denominador puede ser arbitrariamente pequeño.

## 21.6. El invariante de Rolle repetido

[]{#MA-EX-ANM-01-021-006}

[]{#MA-SOL-ANM-01-021-006}

[]{#MA-SEC-ANM-01-021-002}

Ponemos $z_0=x$. En el paso$k$, $H_k(c)=H_k(z_k)=0$ y$z_k\ne c$. La restricción al segmento de esos extremos es continua, y su derivada existe interiormente y coincide con la original. Rolle da$z_{k+1}$ estrictamente entre ambos con$H_k\prime(z_{k+1})=0$. Si$k<n$, la cadena convierte esa igualdad en$H_{k+1}(z_{k+1})=0$, mientras$H_{k+1}(c)=0$ era dato, y permite continuar. En el paso$n$ se obtiene la derivada final nula. Hay$n+1$ pasos, de0 a$n$. La longitud es finita y fijada de antemano.

## 21.7. Una cadena de tres puntos

[]{#MA-EX-ANM-01-021-007}

[]{#MA-SOL-ANM-01-021-007}

Expandimos$H=t^3-t^4$. Sus derivadas son$H\prime=3t^2-4t^3$, $H\prime\prime=6t-12t^2$ y$H^{(3)}=6-24t$. En0, $H,H\prime,H\prime\prime$ valen0 y$H(1)=0$. Evaluar da$H\prime(3/4)=0$, $H\prime\prime(1/2)=0$ y$H^{(3)}(1/4)=0$. Se cumple$0<1/4<1/2<3/4<1$, de modo que cada punto está entre el centro y el punto anterior. La cadena realiza tres aplicaciones para$n=2$; sus valores exactos no son prescritos por el lema general.

**Retorno visual.** Véase [C21-F02](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 21.8. Un dato central que no puede perderse

[]{#MA-EX-ANM-01-021-008}

[]{#MA-SOL-ANM-01-021-008}

Tomamos$H(t)=t(1-t)$. Tiene bordes0 y0, y Rolle da un cero de$H\prime=1-2t$ en1/2. Sin embargo$H\prime(0)=1$, no cero, y$H\prime\prime=-2$ no se anula en el interior. Falta el borde central nulo del segundo miembro de la cadena, así no se puede repetir Rolle entre0 y1/2. La igualdad de valores de la función no basta para toda la cadena.

## 21.9. Rolle hacia la izquierda

[]{#MA-EX-ANM-01-021-009}

[]{#MA-SOL-ANM-01-021-009}

Tenemos$H(0)=H\prime(0)=0$ y$H(-1)=0$. La primera derivada$3t^2+2t=t(3t+2)$ se anula interiormente en$z_1=-2/3$. La segunda$6t+2$ se anula en$z_2=-1/3$, estrictamente entre−2/3 y0. La cadena cumple$-1<-2/3<-1/3<0$: se acerca al centro por la izquierda. Cada aplicación usa el segmento con extremos ordenados mediante mínimo y máximo; no se invierte una hipótesis de continuidad o interioridad.

## 21.10. Qué continuidad consume cada paso

[]{#MA-EX-ANM-01-021-010}

[]{#MA-SOL-ANM-01-021-010}

Cada$H_k$ se usa como función de un Rolle sobre un subsegmento, así necesita continuidad incluyendo sus extremos. Para$k<n$ su derivabilidad interior y la igualdad$H_k\prime=H_{k+1}$ permiten enlazar el próximo miembro. El último$H_n$ necesita derivabilidad interior, pero Rolle no exige continuidad de$H_n\prime$ ni su existencia en bordes. El proceso fija$n$ y construye sólo$n+1$ existencias, mediante inducción finita; no define un selector para todas las entradas o todos los órdenes simultáneamente.

## 21.11. El auxiliar que obliga a la igualdad

[]{#MA-EX-ANM-01-021-011}

[]{#MA-SOL-ANM-01-021-011}

[]{#MA-SEC-ANM-01-021-003}

Si$x=c$, el resto es0 por los datos centrales y no se pide testigo interior. Si$x\ne c$, definimos$A=R(x)/(x-c)^{n+1}$, con denominador no cero. Esto hace$H(x)=0$. Los datos de Taylor y la potencia de grado$n+1$ dan$H^{(k)}(c)=0$ para$k\le n$. Bajo el contrato diferencial, los primeros miembros son continuos y sus derivadas enlazan; Rolle repetido da$H^{(n+1)}(\xi)=0$. La derivada final del polinomio es0 y la de la potencia es$(n+1)!$, así$A=f^{(n+1)}(\xi)/(n+1)!$. Este factorial real es positivo, por lo que se puede despejar. Sustituimos$A$ para obtener la fórmula.

## 21.12. Un testigo que no es el medio

[]{#MA-EX-ANM-01-021-012}

[]{#MA-SOL-ANM-01-021-012}

$T_{1,0}=0$, así$R(1)=1$. La fórmula dice$1=f\prime\prime(\xi)/2=6\xi/2=3\xi$, de donde$\xi=1/3$. Pertenece estrictamente a$(0,1)$ pero no es el medio1/2. Este caso tiene un único testigo porque la segunda derivada es estrictamente creciente. No se infiere unicidad del teorema general.

**Retorno visual.** Véase [C21-F03](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 21.13. Una derivada constante deja muchos testigos

[]{#MA-EX-ANM-01-021-013}

[]{#MA-SOL-ANM-01-021-013}

La expansión exacta da$R=(x-1)^3$. La tercera derivada es6 en cada punto, de modo que$[f^{(3)}(\xi)/3!](x-1)^3=(x-1)^3$ para cualquier$\xi$ estrictamente interior. Hay infinitos puntos posibles en ese segmento y ninguna unicidad. El teorema garantiza uno; una fórmula constante puede hacer válidos todos.

## 21.14. Un centro fronterizo sin última derivada

[]{#MA-EX-ANM-01-021-014}

[]{#MA-SOL-ANM-01-021-014}

Los miembros son$f_0=t^2\sqrt t$, $f_1=(5/2)t\sqrt t$ y$f_2=(15/4)\sqrt t$, con valores0 en el borde. Son continuos sobre$[0,1]$ y las relaciones de derivación se cumplen en$(0,1)$. La derivada$f_2\prime=(15/8)/\sqrt t$ existe interiormente aunque no es finita en0. El contrato cerrado legitima Taylor de orden2 para$x>0$, usando los valores centrales dados; la derivada final se evalúa sólo en un testigo interior. No se obtiene por eso una cota uniforme de tercera derivada cerca de0.

## 21.15. El caso de orden cero

[]{#MA-EX-ANM-01-021-015}

[]{#MA-SOL-ANM-01-021-015}

El polinomio es$T_{0,c}=f(c)$ y1!=1, de modo que$f(x)-f(c)=f\prime(\xi)(x-c)$. Para$x\ne c$ esto es exactamente Lagrange sobre el segmento. Se conserva continuidad incluyendo ambos extremos y derivabilidad interior; el carácter intervalar asegura que el segmento está en el dominio. Para$x=c$ hay igualdad de valores sin testigo entre extremos coincidentes. La reducción no elimina ninguna de esas condiciones.

## 21.16. Una cota que no necesita máximo

[]{#MA-EX-ANM-01-021-016}

[]{#MA-SOL-ANM-01-021-016}

[]{#MA-SEC-ANM-01-021-004}

Para$x\ne c$, tomamos valores absolutos en$R=f^{(n+1)}(\xi)(x-c)^{n+1}/(n+1)!$ y aplicamos la cota universal en$\xi$. Resulta$|R|\le M|x-c|^{n+1}/(n+1)!$. Si$x=c$, ambos lados son0. Si$M=0$, la desigualdad fuerza$R=0$ sin dividir por$M$. Una cota suministrada controla todos los valores posibles del testigo; no se necesita obtenerla como máximo alcanzado ni presuponer continuidad de la derivada final.

## 21.17. La cancelación de Cauchy

[]{#MA-EX-ANM-01-021-017}

[]{#MA-SOL-ANM-01-021-017}

Derivamos la suma finita. La parte que deriva$f^{(k)}$ es$\sum_{k=0}^n f^{(k+1)}(t)(x-t)^k/k!$; la que deriva la potencia es$-\sum_{k=1}^n f^{(k)}(t)(x-t)^{k-1}/(k-1)!$. Tras reindexar la segunda, se cancelan todos salvo el término superior de la primera. Como$G$ es negativo de la suma más una constante,$G\prime=-f^{(n+1)}(t)(x-t)^n/n!$. Se tiene$G(x)=0$ y$G(c)=R$. Lagrange sobre$G$ da$-R=G\prime(\eta)(x-c)$; sustituir produce$R=f^{(n+1)}(\eta)(x-\eta)^n(x-c)/n!$.

**Retorno visual.** Véase [C21-F04](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 21.18. Una banda que cambia de orientación

[]{#MA-EX-ANM-01-021-018}

[]{#MA-SOL-ANM-01-021-018}

El coeficiente$R/(x-c)^3$ queda entre2/6=1/3 y6/6=1. Si$x>c$, la potencia es positiva y$(x-c)^3/3\le R\le(x-c)^3$. Si$x<c$, la potencia es negativa y se invierte el orden:$(x-c)^3\le R\le(x-c)^3/3$. En el centro$R=0$. En ambos lados la cota absoluta$|R|\le|x-c|^3$ sigue siendo válida, pero la banda firmada retiene el signo.

## 21.19. Testigos diferentes para el mismo error

[]{#MA-EX-ANM-01-021-019}

[]{#MA-SOL-ANM-01-021-019}

El resto es1. Lagrange dio$\xi=1/3$. Cauchy exige$1=6\eta(1-\eta)$; las soluciones$\eta=(1\pm1/\sqrt3)/2$ pertenecen a$(0,1)$ y ambas sirven. Ninguna es1/3. Con$M=6$, Lagrange da$|R|\le6/2=3$, mientras la estimación constante de Cauchy da$|R|\le6/1=6$. Ambas cotas son correctas aunque poco ajustadas frente al error exacto1; sus puntos y factores no se intercambian.

## 21.20. Una región antes de una entrada

[]{#MA-EX-ANM-01-021-020}

[]{#MA-SOL-ANM-01-021-020}

Para cada entrada$x$ del segmento, la prueba de Lagrange se aplica a su subsegmento con$c$. Su testigo pertenece al interior de la región completa, donde vale la misma$M$. Así$|R(x)|\le M|x-c|^{n+1}/(n+1)!\le M\rho^{n+1}/(n+1)!$. El caso central es0. La cota se eligió antes de$x$ y sirve para todas las entradas, sin seleccionar sus testigos simultáneamente. Una muestra finita sólo acota valores muestreados, no cualquier ubicación interior que puede producir el teorema.

## 21.21. Peano por Cauchy e inducción

[]{#MA-EX-ANM-01-021-021}

[]{#MA-SOL-ANM-01-021-021}

[]{#MA-SEC-ANM-01-021-005}

Los datos centrales de$H$ hasta orden$n$ son0. El resultado de orden$n-1$ aplicado a$H\prime$ da$H\prime(c+u)=o(|u|^{n-1})$. Para$\varepsilon>0$ tomamos un radio donde$|H\prime(c+u)|<n\varepsilon|u|^{n-1}$. Para$0<|h|$ dentro del radio, Cauchy en$H$ y$(t-c)^n$ da$H(c+h)/h^n=H\prime(\xi)/[n(\xi-c)^{n-1}]$. El testigo no es$c$, así la derivada del denominador no se anula; el incremento$h^n$ tampoco. La cota inductiva hace al valor absoluto del cociente menor que$\varepsilon$. Se requiere que$H\prime$ exista en el segmento, garantizado por las hipótesis inferiores para$n\ge2$.

## 21.22. Peano sin un orden cúbico de error

[]{#MA-EX-ANM-01-021-022}

[]{#MA-SOL-ANM-01-021-022}

$f(0)=0$ y$f(h)/h=\operatorname{sgn}(h)|h|^{3/2}\to0$, así$f\prime(0)=0$. Fuera de0,$f\prime(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$. Dividir por$h$ da$(5/2)\sqrt{|h|}\to0$, luego$f\prime\prime(0)=0$. El Taylor de orden2 es cero. El cociente$f(h)/|h|^2=\sqrt{|h|}$ tiende a0, pero$f(h)/|h|^3=1/\sqrt{|h|}$ excede cualquier constante finita tomando entradas suficientemente pequeñas. El resultado es Peano sin una cota uniforme del siguiente orden.

**Retorno visual.** Véase [C21-F05](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 21.23. Error absoluto y error normalizado

[]{#MA-EX-ANM-01-021-023}

[]{#MA-SOL-ANM-01-021-023}

Ambas funciones tienden a0 en valor absoluto. Pero$|r(h)|/|h|^n=1$ en todas las entradas perforadas, así no tiende a0 y$r$ no es$o(|h|^n)$. En cambio$|s(h)|/|h|^n=|h|\to0$, y$s$ sí tiene esa propiedad. Peano mide error respecto de una escala, no sólo tamaño absoluto.

## 21.24. Un modelo asintótico también es único

[]{#MA-EX-ANM-01-021-024}

[]{#MA-SOL-ANM-01-021-024}

La resta y la triangular dan$P-Q=o(|h|^n)$. Si el polinomio diferencia fuera no cero, tendría un término de menor grado$j\le n$ con coeficiente$a\ne0$: $P-Q=h^j(a+hB(h))$. Por continuidad del polinomio$B$, el factor interior tiende a$a$ y su valor absoluto es al menos$|a|/2$ en un radio. Dividir por$|h|^n$ da al menos$(|a|/2)|h|^{j-n}$, que no tiende a0: si$j=n$ es constante positiva y si$j<n$ crece sin cota. Contradicción. No se utilizó una regla de derivación para$o$.

## 21.25. Un radio para un error de raíz

[]{#MA-EX-ANM-01-021-025}

[]{#MA-SOL-ANM-01-021-025}

Como$|f(h)|/|h|^2=\sqrt{|h|}$, tomamos$\delta=\varepsilon^2$ o el mínimo con un radio de dominio. Para$0<|h|<\delta$ se cumple$\sqrt{|h|}<\varepsilon$ y la desigualdad requerida. Esto prueba Peano de orden2 con radio explícito para este ejemplo. No produce una constante cúbica: el cociente por$|h|^3$ sigue siendo$1/\sqrt{|h|}$, arbitrariamente grande.

## 21.26. Dominar el resto para decidir un signo

[]{#MA-EX-ANM-01-021-026}

[]{#MA-SOL-ANM-01-021-026}

[]{#MA-SEC-ANM-01-021-006}

Como$a\ne0$, elegimos$\varepsilon=|a|/2$ en la condición$o$. En el radio resultante el error tiene magnitud menor que la mitad del término principal. Si$m$ es par, éste tiene signo$a$ en ambos lados, y la suma conserva ese signo: mínimo estricto para$a>0$ y máximo estricto para$a<0$. Si$m$ es impar, el principal cambia de signo de un lado a otro y el error no puede invertirlo; hay salidas mayores y menores arbitrariamente próximas. El centro debe ser interior para disponer de ambos lados.

## 21.27. Cuarto poder frente a cubo

[]{#MA-EX-ANM-01-021-027}

[]{#MA-SOL-ANM-01-021-027}

Para$x^4$, las primeras tres derivadas centrales son0 y la cuarta vale24; su coeficiente es24/4!=1. El orden par positivo da mínimo local estricto, y directamente$x^4>0$ para$x\ne0$. Para$x^3$, las primeras dos son0 y la tercera6, de coeficiente1. El orden impar da ausencia de extremo interior; directamente$x^3$ es negativo a la izquierda y positivo a la derecha. Una pendiente central cero común no distingue estos casos.

**Retorno visual.** Véase [C21-F06](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 21.28. Datos nulos con tres respuestas

[]{#MA-EX-ANM-01-021-028}

[]{#MA-SOL-ANM-01-021-028}

Tomamos$p=h^{2(n+1)}$, $q=-h^{2(n+1)}$ y$r=h^{2(n+1)+1}$. Todos los exponentes superan$n$, por lo que el valor y las derivadas hasta ese orden se anulan en0. El primero es positivo en entradas no nulas y tiene mínimo estricto; el segundo negativo y tiene máximo estricto; el tercero cambia de signo y no tiene extremo interior. La falta de datos no nulos disponibles impide aplicar el criterio, no demuestra que no exista un extremo.

## 21.29. El mínimo que no gobierna toda la recta

[]{#MA-EX-ANM-01-021-029}

[]{#MA-SOL-ANM-01-021-029}

El primer orden no nulo es2, con$q\prime\prime(0)=2>0$, por lo que el criterio local da mínimo estricto. Directamente$q=h^2(1-h^2)>0$ para$0<|h|<1$. Pero$q(2)=4-16=-12<0$, así0 no es mínimo global. La segunda derivada$2-12h^2$ se vuelve negativa; no hay convexidad global que permita utilizar el soporte horizontal de C20. Un dato central positivo no reemplaza esa propiedad en todo el intervalo.

## 21.30. El orden impar en una frontera

[]{#MA-EX-ANM-01-021-030}

[]{#MA-SOL-ANM-01-021-030}

La función tiene primer coeficiente1 y orden1 impar, pero el dominio sólo ofrece incrementos$h\ge0$ desde el centro0. Para$h>0$, el término principal$h$ es positivo y no hay entradas negativas que produzcan el signo contrario. En$[0,1]$, la función alcanza mínimo único en0. Un desarrollo unilateral con error menor que la mitad del término principal certifica el signo en el lado disponible; la conclusión de ausencia de extremo del criterio impar requería centro interior y acumulación bilateral.

## 21.31. Una identidad geométrica todavía finita

[]{#MA-EX-ANM-01-021-031}

[]{#MA-SOL-ANM-01-021-031}

[]{#MA-SEC-ANM-01-021-007}

Inducción con cociente y producto da$f^{(k)}=k!/(1-h)^{k+1}$; al evaluar en0 el coeficiente de Taylor es1. Multiplicar la suma finita por$1-h$ cancela términos vecinos y deja$1-h^{n+1}$. Como$1-h\ne0$ en el dominio$h<1$, despejamos la función y obtenemos resto$h^{n+1}/(1-h)$. No se tomó un límite de sumas ni se identificó una serie infinita.

## 21.32. La raíz y su tercera derivada

[]{#MA-EX-ANM-01-021-032}

[]{#MA-SOL-ANM-01-021-032}

Por C18, $g\prime=1/(2\sqrt{1+h})$, $g\prime\prime=-1/[4(1+h)\sqrt{1+h}]$ y$g^{(3)}=3/[8(1+h)^2\sqrt{1+h}]$. En0 se obtienen1,1/2,−1/4, luego$T_2=1+h/2-h^2/8$. En el segmento$1+h\ge3/4$ y su raíz positiva es al menos3/4, pues$(3/4)^2\le3/4$. El denominador de la tercera derivada es al menos$8(3/4)^3=27/8$; el cociente queda a lo sumo8/9 y es positivo. No usamos derivación de una potencia real general.

## 21.33. Un intervalo racional para una raíz

[]{#MA-EX-ANM-01-021-033}

[]{#MA-SOL-ANM-01-021-033}

En$h=1/4$, $T_2=1+1/8-1/128=143/128$. La cota de tercera derivada8/9 da$|R_2|\le(8/9)(1/4)^3/6=1/432$. Como la tercera derivada es positiva en todo el segmento y el incremento cúbico es positivo, $R_2>0$. Así$143/128<\sqrt{5/4}\le143/128+1/432$. La primera desigualdad es estricta por signo; la segunda sólo es una cota superior no estricta. No se extrajo una raíz aproximada del dibujo.

**Retorno visual.** Véase [C21-F07](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 21.34. Un cotejo por racionalización

[]{#MA-EX-ANM-01-021-034}

[]{#MA-SOL-ANM-01-021-034}

La diferencia es$5/4-20449/16384=31/16384>0$, por lo que el aproximante es inferior a la raíz positiva. Racionalizar da error$31/[16384(\sqrt{5/4}+143/128)]$. Como la raíz es al menos1, el denominador es al menos$16384(271/128)=34688$, y el error es a lo sumo31/34688. Para comparar, $31\cdot432=13392<34688$, así31/34688<1/432. La cota algebraica es más ajustada; ambas certifican el mismo aproximante con premisas distintas.

## 21.35. La singularidad impone el margen

[]{#MA-EX-ANM-01-021-035}

[]{#MA-SOL-ANM-01-021-035}

El resto exacto es$h^{n+1}/(1-h)$. En la región declarada, $1-h\ge1-\rho>0$ y$|h|^{n+1}\le\rho^{n+1}$, así$|R|\le\rho^{n+1}/(1-\rho)$. Para$n$ fijo, si$h\uparrow1$, el numerador tiende a1 y el denominador positivo a0. Por ejemplo, para$h$ suficientemente próximo el numerador supera1/2, y tomar$1-h$ menor que$1/(2B)$ hace al resto mayor que cualquier$B>0$. El margen de dominio no puede borrarse.

## 21.36. Multiplicar modelos sin derivar errores

[]{#MA-EX-ANM-01-021-036}

[]{#MA-SOL-ANM-01-021-036}

[]{#MA-SEC-ANM-01-021-008}

El producto exacto es$PQ+Pv+Qu+uv$. Los polinomios están acotados cerca de0; por ello los cocientes normalizados de$Pv$ y$Qu$ tienden a0. También$v\to0$ y$|uv|/|h|^n=(|u|/|h|^n)|v|\to0$. Eliminar términos de grado mayor que$n$ de$PQ$ añade un error$h^{n+1}B(h)$ con$B$ polinómico acotado; normalizar deja un factor$|h|$ y tiende a0. La triangular reúne esos errores. No se derivaron$u,v$ ni se supuso que sus derivadas fueran pequeñas.

## 21.37. Sustitución con denominador protegido

[]{#MA-EX-ANM-01-021-037}

[]{#MA-SOL-ANM-01-021-037}

Pongamos$d=1-h-h^2$, que es al menos11/16 en la región. Por cociente,$F\prime=(1+2h)/d^2$, de valor1 en0; derivar da$F\prime\prime=2/d^2+2(1+2h)^2/d^3$, de valor4 en0. Así$T_2=1+h+2h^2$. La identidad$(1+h+2h^2)d=1-3h^3-2h^4$ da resto$(3h^3+2h^4)/d$. Su magnitud es a lo sumo$(3+2/4)|h|^3/(11/16)=(56/11)|h|^3$. El margen protege tanto la función como su certificado.

## 21.38. Elegir el menor grado certificado

[]{#MA-EX-ANM-01-021-038}

[]{#MA-SOL-ANM-01-021-038}

La cota exacta uniforme es$1/(3\cdot4^n)$ y se alcanza en$h=1/4$. Para$n=4$ vale1/768>1/1000; para$n=5$ vale1/3072<1/1000. Como cada aumento divide por4, ningún orden menor que4 puede servir, y4 tampoco: el mínimo es5. El polinomio en1/4 es la suma de seis términos$1+1/4+1/16+1/64+1/256+1/1024=1365/1024$. La función vale4/3; la diferencia es$(4096-4095)/3072=1/3072$.

## 21.39. Trasladar un centro conocido

[]{#MA-EX-ANM-01-021-039}

[]{#MA-SOL-ANM-01-021-039}

En centro2, con$u=t-2$, la identidad$(2+u)^3=8+12u+6u^2+u^3$ da los datos y todos los coeficientes. En centro1, con$h=t-1$, eran$1+3h+3h^2+h^3$. Se relacionan sustituyendo$h=1+u$, porque conocemos la función polinómica completa y el resto de orden3 es0. Para una función general, el modelo central finito conserva sólo datos en su centro y lleva un resto fuera de él. Trasladarlo sin controlar ese resto puede cambiar incluso el valor y las derivadas en el nuevo centro.

## 21.40. Muestras y datos que no determinan otra salida

[]{#MA-EX-ANM-01-021-040}

[]{#MA-SOL-ANM-01-021-040}

El producto es polinómico. Multiplicarlo por$h^{n+1}$ garantiza un factor de grado al menos$n+1$ en0, de modo que todas las derivadas centrales hasta$n$ se anulan. En cada$h_j$ hay un factor cero y se conserva$P(h_j)$. En$h_*$ distinto de0 y de todas las muestras, el factor$B=h_*^{n+1}\prod_j(h_*-h_j)^2$ es no cero. Para imponer salida$b$, elegimos$A=(b-P(h_*))/B$. Es una construcción finita, también con producto vacío1 si$m=0$. Conservar esos datos no certifica por sí solo un error en una región completa ni una representación infinita.

**Retorno visual.** Véase [C21-F08](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 21](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html) · [Ejercicios](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error-microcontroles.html)
