---
content-id: MA-BCH-0283
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-020-EJERCICIOS
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
title: Ejercicios — Capítulo 20
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C20_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Ejercicios](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html)

Las soluciones completas están en ANM-C20_SOLUCIONES.md. Declara intervalo y pesos, distingue centros interiores de bordes y controla el signo al dividir. Las pruebas tempranas de secantes y continuidad no usan derivadas. Los criterios diferenciales exigen sus hipótesis en todo el intervalo; un signo central no basta. No uses Taylor o integrales.

## 20.1. La diferencia exacta de una cuerda

[]{#MA-EX-ANM-01-020-001}

[]{#MA-SOL-ANM-01-020-001}

[]{#MA-SEC-ANM-01-020-001}

Para $f(x)=x^2$ y $z=(1-t)a+tb$, calcula la diferencia entre la altura de la cuerda y $f(z)$. Usa el resultado para decidir convexidad y sus casos de igualdad.

## 20.2. Una esquina bajo sus cuerdas

[]{#MA-EX-ANM-01-020-002}

[]{#MA-SOL-ANM-01-020-002}

Demuestra que $|x|$ es convexa y no estrictamente convexa. Identifica además por qué no admite derivada bilateral en cero.

## 20.3. Sumar sin invertir el orden

[]{#MA-EX-ANM-01-020-003}

[]{#MA-SOL-ANM-01-020-003}

Sean $f,g$ convexas sobre $I$. Demuestra convexidad de $\alpha f+\beta g$ para $\alpha,\beta\ge0$ y de $f+A+Bx$. Exhibe una falla si se permite un coeficiente negativo.

## 20.4. Una subida que no decide curvatura

[]{#MA-EX-ANM-01-020-004}

[]{#MA-SOL-ANM-01-020-004}

Compara monotonía y convexidad de $x^2$ y $x^3$ sobre $\mathbb R$ sin invocar el criterio de segunda derivada.

## 20.5. Supremo de curvas convexas

[]{#MA-EX-ANM-01-020-005}

[]{#MA-SOL-ANM-01-020-005}

Sea una familia no vacía $(f_j)$ de funciones convexas sobre el mismo intervalo. Supón que $F(x)=\sup_j f_j(x)$ es real finito para cada $x$. Prueba convexidad de $F$. Explica las condiciones de no vaciedad y finitud.

## 20.6. Reconstruir la cuerda desde pendientes

[]{#MA-EX-ANM-01-020-006}

[]{#MA-SOL-ANM-01-020-006}

[]{#MA-SEC-ANM-01-020-002}

Para $u<v<w$, demuestra algebraicamente que $S(u,v)\le S(v,w)$ equivale a la desigualdad de convexidad en $v$ entre $u,w$. Recupera también el orden de la secante larga.

## 20.7. Tres pendientes del cuadrado

[]{#MA-EX-ANM-01-020-007}

[]{#MA-SOL-ANM-01-020-007}

Calcula las pendientes de $x^2$ entre las entradas0,1,3. Comprueba su orden y relaciona cada una con la fórmula general $S(u,v)$.

## 20.8. Una igualdad que se propaga

[]{#MA-EX-ANM-01-020-008}

[]{#MA-SOL-ANM-01-020-008}

Sea $f$ convexa en $[a,b]$, y sea $\ell$ la cuerda entre sus bordes. Si $f(z)=\ell(z)$ para un $z$ interior, demuestra que $f=\ell$ en todo el segmento.

## 20.9. Cero curvatura en una pieza

[]{#MA-EX-ANM-01-020-009}

[]{#MA-SOL-ANM-01-020-009}

Construye una función convexa que no sea afín en toda $\mathbb R$ y que tenga una igualdad interior en alguna cuerda. Explica por qué no contradice E008.

## 20.10. Sin tramo recto, con desigualdad estricta

[]{#MA-EX-ANM-01-020-010}

[]{#MA-SOL-ANM-01-020-010}

Prueba que una función convexa es estrictamente convexa si y sólo si no es afín en ningún subsegmento con extremos distintos.

## 20.11. Un radio construido con secantes

[]{#MA-EX-ANM-01-020-011}

[]{#MA-SOL-ANM-01-020-011}

[]{#MA-SEC-ANM-01-020-003}

Sea $f$ convexa finita y $a<c<d<b$ en su intervalo. Construye una constante Lipschitz en $[c,d]$ y un radio de continuidad sin usar derivadas.

## 20.12. Dos pendientes laterales en una esquina

[]{#MA-EX-ANM-01-020-012}

[]{#MA-SOL-ANM-01-020-012}

Calcula las derivadas laterales de $|x|$ en cero y las constantes de secante que las definen. Decide continuidad, derivabilidad y una constante Lipschitz global.

## 20.13. Una discontinuidad convexa de borde

[]{#MA-EX-ANM-01-020-013}

[]{#MA-SOL-ANM-01-020-013}

En $[0,1]$, toma $f(0)=1$ y $f(x)=0$ para $x>0$. Prueba convexidad y falta de continuidad en cero. Explica qué afirmación de continuidad permanece válida.

## 20.14. El supremo convertido en límite

[]{#MA-EX-ANM-01-020-014}

[]{#MA-SOL-ANM-01-020-014}

Para $c$ interior de una función convexa finita, demuestra que $A=\sup_{x<c}S(x,c)$ es real y es el límite de esas secantes al acercarse desde la izquierda.

## 20.15. Ni constante global ni borde protegido

[]{#MA-EX-ANM-01-020-015}

[]{#MA-SOL-ANM-01-020-015}

Explica con $x^2$ en $\mathbb R$ por qué la convexidad no implica Lipschitz global. Da también una función convexa continua en $[0,1]$ que no sea Lipschitz allí.

## 20.16. Todas las rectas que sostienen la esquina

[]{#MA-EX-ANM-01-020-016}

[]{#MA-SOL-ANM-01-020-016}

[]{#MA-SEC-ANM-01-020-004}

Determina todos los $p$ para los que $px\le|x|$ para todo $x$. Relaciona el resultado con las dos pendientes laterales.

## 20.17. Una familia que envuelve el cuadrado

[]{#MA-EX-ANM-01-020-017}

[]{#MA-SOL-ANM-01-020-017}

Prueba $x^2=\sup_{c\in\mathbb R}(2cx-c^2)$, indicando existencia de la cota y un centro que alcance el supremo.

## 20.18. Por qué el soporte invierte un signo

[]{#MA-EX-ANM-01-020-018}

[]{#MA-SOL-ANM-01-020-018}

Sea $f$ convexa y $c$ interior. Prueba que las pendientes de una recta de soporte por $(c,f(c))$ son exactamente $[A,B]$, con $A=f\prime_-(c)$ y $B=f\prime_+(c)$.

## 20.19. Un borde sin soporte finito

[]{#MA-EX-ANM-01-020-019}

[]{#MA-SOL-ANM-01-020-019}

Para $f(x)=-\sqrt{x}$ en $[0,1]$, demuestra que no existe una recta de pendiente real finita por $(0,0)$ que quede debajo en todo el segmento. ¿Contradice la existencia interior de soportes?

## 20.20. Un segundo contacto fuerza una pieza recta

[]{#MA-EX-ANM-01-020-020}

[]{#MA-SOL-ANM-01-020-020}

Sea $f$ convexa y sea $\ell$ un soporte. Si $f(a)=\ell(a)$ y $f(b)=\ell(b)$ para $a<b$, prueba $f=\ell$ en $[a,b]$. Deduce la unicidad del contacto de una tangente de una función estrictamente convexa.

## 20.21. Dos centros en segmentos vecinos

[]{#MA-EX-ANM-01-020-021}

[]{#MA-SOL-ANM-01-020-021}

[]{#MA-SEC-ANM-01-020-005}

Demuestra que una función derivable en un intervalo abierto es convexa si su derivada es no decreciente. Declara las hipótesis de cada aplicación de Lagrange.

## 20.22. Orden de derivadas sin orden de valores

[]{#MA-EX-ANM-01-020-022}

[]{#MA-SOL-ANM-01-020-022}

Para $x^2$, explica por qué la derivada creciente certifica convexidad pero no crecimiento global de la función. Encuentra sus intervalos de monotonía.

## 20.23. Un plateau de derivadas destruye lo estricto

[]{#MA-EX-ANM-01-020-023}

[]{#MA-SOL-ANM-01-020-023}

Supón que $f$ es derivable y convexa sobre un intervalo abierto. Si $x<y$ y $f\prime(x)=f\prime(y)=k$, demuestra que $f$ es afín en $[x,y]$. Usa esto para el criterio estricto.

## 20.24. Tangentes que prueban convexidad

[]{#MA-EX-ANM-01-020-024}

[]{#MA-SOL-ANM-01-020-024}

Supón que $f$ es derivable en $I$ y que cada tangente en un centro de $I$ queda debajo de todas las salidas de $f$ en $I$. Prueba convexidad sin comparar derivadas directamente.

## 20.25. La derivada interior no arregla el borde

[]{#MA-EX-ANM-01-020-025}

[]{#MA-SOL-ANM-01-020-025}

En $[0,1]$, toma $f(0)=-1$ y $f(x)=0$ si $x>0$. Comprueba que la derivada interior es no decreciente y que la función no es convexa. Identifica la hipótesis ausente.

## 20.26. Dos derivadas, una equivalencia

[]{#MA-EX-ANM-01-020-026}

[]{#MA-SOL-ANM-01-020-026}

[]{#MA-SEC-ANM-01-020-006}

Sea $f$ dos veces derivable en un intervalo abierto. Demuestra ambas direcciones de la equivalencia entre convexidad y $f\prime\prime\ge0$, sin suponer continuidad de $f\prime\prime$.

## 20.27. Convexidad estricta con segunda derivada nula

[]{#MA-EX-ANM-01-020-027}

[]{#MA-SOL-ANM-01-020-027}

Prueba que $x^4$ es estrictamente convexa en toda la recta y que no cumple $f\prime\prime>0$ en todos los puntos.

## 20.28. Recíproco y raíz: dos direcciones

[]{#MA-EX-ANM-01-020-028}

[]{#MA-SOL-ANM-01-020-028}

Calcula las dos primeras derivadas de $1/x$ y de $\sqrt{x}$ para $x>0$. Decide monotonía y convexidad o concavidad. Justifica la extensión de concavidad de la raíz a cero.

## 20.29. Una muestra de curvatura no basta

[]{#MA-EX-ANM-01-020-029}

[]{#MA-SOL-ANM-01-020-029}

Para $q=x^2-x^4$, compara $q\prime\prime(0)$ y $q\prime\prime(1)$ y decide convexidad global. Explica además por qué $f\prime\prime(0)=0$ no identifica un cambio de convexidad.

## 20.30. Existencia, frontera y soporte horizontal

[]{#MA-EX-ANM-01-020-030}

[]{#MA-SOL-ANM-01-020-030}

Distingue las conclusiones sobre mínimos de: (i) función convexa derivable con $f\prime(c)=0$ interior; (ii) $x$ sobre $[0,1]$; (iii) $x^2$ sobre $(0,1)$. Indica cuándo hay unicidad y existencia.

## 20.31. El peso nulo en la inducción

[]{#MA-EX-ANM-01-020-031}

[]{#MA-SOL-ANM-01-020-031}

[]{#MA-SEC-ANM-01-020-007}

Prueba Jensen finito por inducción para pesos no negativos que suman1, separando las posibilidades que podrían causar una división por cero.

## 20.32. Igualdad con entradas inactivas

[]{#MA-EX-ANM-01-020-032}

[]{#MA-SOL-ANM-01-020-032}

En Jensen para una función estrictamente convexa, ¿qué condición de igualdad corresponde a pesos positivos y a pesos cero? Prueba la condición necesaria.

## 20.33. Una diferencia de diecinueve dieciseisavos

[]{#MA-EX-ANM-01-020-033}

[]{#MA-SOL-ANM-01-020-033}

Para pesos $(1/4,1/2,1/4)$ y entradas $(0,1,3)$, calcula la media, la media de cuadrados y su diferencia. Verifica la identidad de suma de desviaciones cuadráticas.

## 20.34. Una desigualdad sin logaritmos

[]{#MA-EX-ANM-01-020-034}

[]{#MA-SOL-ANM-01-020-034}

Para $x_i>0$, demuestra $(\sum_{i=1}^n x_i)(\sum_{i=1}^n1/x_i)\ge n^2$ por Jensen y da su caso de igualdad.

## 20.35. Una suma de pesos que no protege el signo

[]{#MA-EX-ANM-01-020-035}

[]{#MA-SOL-ANM-01-020-035}

Exhibe la falla de Jensen para el cuadrado con pesos2 y−1. Explica el paso de la prueba que deja de ser válido y por qué no es un contraejemplo a Jensen.

## 20.36. Restar un cuadrado para obtener una banda

[]{#MA-EX-ANM-01-020-036}

[]{#MA-SOL-ANM-01-020-036}

[]{#MA-SEC-ANM-01-020-008}

Supón $m\le f\prime\prime\le M$ en todo un intervalo abierto. Demuestra las dos cotas del error de tangente sin Taylor ni integrales.

## 20.37. La banda de una cuerda

[]{#MA-EX-ANM-01-020-037}

[]{#MA-SOL-ANM-01-020-037}

Deriva la banda del error de cuerda entre $a,b$ para $z=(1-t)a+tb$ a partir de $q_m$ y $q_M$. Incluye los pesos extremos.

## 20.38. Una banda que alcanza ambos lados

[]{#MA-EX-ANM-01-020-038}

[]{#MA-SOL-ANM-01-020-038}

Para $f(x)=x^2$ en $[0,2]$ y $m=M=2$, calcula el error de cuerda en1 y el error de tangente desde $c=1$ hasta $x=3/2$. Comprueba que las bandas son exactas.

## 20.39. Lo estricto no da un margen uniforme

[]{#MA-EX-ANM-01-020-039}

[]{#MA-SOL-ANM-01-020-039}

Para $f(x)=x^4$ cerca de cero, demuestra que la convexidad estricta no permite una cota $f\prime\prime\ge m>0$ ni una cota $|f\prime(x)|\ge m|x|$ con constante positiva uniforme.

## 20.40. De una pendiente a dos certificados

[]{#MA-EX-ANM-01-020-040}

[]{#MA-SOL-ANM-01-020-040}

Para $f(x)=x^2+x^4$ en $[-1,1]$, prueba mínimo único en0 y usa $m=2$ para certificar posición y pérdida en $x=1/4$. Calcula las cantidades exactas y compara certificado con valor real.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Ejercicios](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes-microcontroles.html)
