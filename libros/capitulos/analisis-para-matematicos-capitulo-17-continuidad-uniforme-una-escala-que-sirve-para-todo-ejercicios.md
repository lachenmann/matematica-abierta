---
content-id: MA-BCH-0271
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-017-EJERCICIOS
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
title: Ejercicios — Capítulo 17
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C17_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html)

Las soluciones completas se encuentran en ANM-C17_SOLUCIONES.md. Declara dominios, presupuestos y orden de elección de radios. Distingue uniformidad de continuidad puntual y de acotación, supremo de cota estricta y rutas dadas de seleccionadas. No uses derivadas ni integrales; declara CC(R) en la recíproca de pares sobre dominio arbitrario.

## 17.1. El orden de los cuantificadores

[]{#MA-EX-ANM-01-017-001}

[]{#MA-SOL-ANM-01-017-001}

[]{#MA-SEC-ANM-01-017-001}

Escribe continuidad puntual, uniformidad y negación de uniformidad para $f:D\to\mathbb R$. Explica qué variables puede conocer cada radio y trata el vacío.

## 17.2. Un radio dependiente no refuta otro posible

[]{#MA-EX-ANM-01-017-002}

[]{#MA-SOL-ANM-01-017-002}

Una prueba de continuidad de $x^2$ produce radios dependientes del centro y concluye que no hay radio uniforme. Diagnostica el fallo y prueba la conclusión correcta en $\mathbb R$ con testigos para cada radio. Contrasta $[-M,M]$.

## 17.3. Una escala no lineal

[]{#MA-EX-ANM-01-017-003}

[]{#MA-SOL-ANM-01-017-003}

Prueba uniformidad de $\sqrt{x}$ en $[0,\infty)$ sin derivadas y refuta que sea Lipschitz en $[0,1]$.

## 17.4. Restricción y regreso imposible

[]{#MA-EX-ANM-01-017-004}

[]{#MA-SOL-ANM-01-017-004}

Prueba que uniformidad se hereda por restricción. Da una función cuya restricción a un subconjunto sea uniforme aunque ella no sea uniforme en el dominio mayor.

## 17.5. Uniformidad sin compacidad ni acotación

[]{#MA-EX-ANM-01-017-005}

[]{#MA-SOL-ANM-01-017-005}

Para $f(x)=3x-2$ en $\mathbb R$, da un radio uniforme y determina si la imagen y el dominio son acotados o compactos. ¿Refuta Heine–Cantor?

## 17.6. Proteger una cubierta concreta

[]{#MA-EX-ANM-01-017-006}

[]{#MA-SOL-ANM-01-017-006}

[]{#MA-SEC-ANM-01-017-002}

Para $K=[0,1]$, $U_1=(-1,3/5)$ y $U_2=(2/5,2)$, verifica que $\lambda=1/10$ es número de Lebesgue relativo. ¿Sirve $\lambda=1/5$?

## 17.7. Familia de todos los triples

[]{#MA-EX-ANM-01-017-007}

[]{#MA-SOL-ANM-01-017-007}

Reconstruye R2 mostrando por qué $T$ determina una familia abierta y cubre $K$ sin escoger un triple para cada punto.

## 17.8. Tomar un ínfimo demasiado pronto

[]{#MA-EX-ANM-01-017-008}

[]{#MA-SOL-ANM-01-017-008}

Un argumento toma el ínfimo de todos los radios locales positivos y lo declara positivo. Repara la prueba de R2 y explica el papel de la bola doble.

## 17.9. Levantar sin elegir ambientes

[]{#MA-EX-ANM-01-017-009}

[]{#MA-SOL-ANM-01-017-009}

Una cubierta de compacto se da por abiertos relativos $(A_i)$. Explica cómo obtener su número de Lebesgue sin elegir simultáneamente abiertos ambientales que representen cada $A_i$.

## 17.10. Una cubierta finita sin margen

[]{#MA-EX-ANM-01-017-010}

[]{#MA-SOL-ANM-01-017-010}

Sea $D=\{p_n=1/(n+1):n\ge0\}$. Pon $r_n=1/[4(n+1)(n+2)]$ y divide las bolas $B(p_n,r_n)$ en dos abiertos, según paridad de $n$. Prueba que cubren $D$ y que esa cubierta finita no tiene número de Lebesgue positivo.

## 17.11. Las dos bolas del mismo índice

[]{#MA-EX-ANM-01-017-011}

[]{#MA-SOL-ANM-01-017-011}

[]{#MA-SEC-ANM-01-017-003}

En R3, justifica todas las condiciones que llevan de un par $|x-y|<\delta$ al error menor que $\varepsilon$. ¿Por qué no basta decir que ambos están en la misma bola pequeña?

## 17.12. Uniformizar sólo la restricción

[]{#MA-EX-ANM-01-017-012}

[]{#MA-SOL-ANM-01-017-012}

Para $f(x)=x^2$ en $D=\mathbb R$ y $K=[-2,-1]\cup[1,2]$, aplica Heine–Cantor y da además un radio explícito. ¿Qué se puede concluir sobre todo $D$?

## 17.13. La lectura por cubiertas de salida

[]{#MA-EX-ANM-01-017-013}

[]{#MA-SOL-ANM-01-017-013}

Prueba Heine–Cantor usando los abiertos relativos $A_a=\{z\in K:|h(z)-h(a)|<\varepsilon/2\}$ y R2. Declara el orden de los testigos.

## 17.14. Acotación sin frontera incluida

[]{#MA-EX-ANM-01-017-014}

[]{#MA-SOL-ANM-01-017-014}

Refuta uniformidad de $1/x$ en $(0,1]$ con pares dados válidos desde $n=0$. Explica qué hipótesis de Heine–Cantor falta.

## 17.15. Vacuidad y prueba sin rutas

[]{#MA-EX-ANM-01-017-015}

[]{#MA-SOL-ANM-01-017-015}

Explica dónde entra no vacuidad en el mínimo de R3 y por qué la prueba no necesita CC(R). Contrasta la demostración por pares malos de una negación.

## 17.16. Existencia y orden del módulo

[]{#MA-EX-ANM-01-017-016}

[]{#MA-SOL-ANM-01-017-016}

[]{#MA-SEC-ANM-01-017-004}

Para $f:D\to\mathbb R$ acotada en un dominio no vacío, justifica existencia de $\omega_f(t)$, su monotonía, valor en cero y la cota de diferencias. Trata el dominio vacío.

## 17.17. Supremo y presupuesto estricto

[]{#MA-EX-ANM-01-017-017}

[]{#MA-SOL-ANM-01-017-017}

Una prueba dice: «todos los errores son menores que $\varepsilon$, luego su supremo también». Repara la dirección uniforme implica módulo tendente a cero y prueba la recíproca.

## 17.18. Módulo exacto del cuadrado

[]{#MA-EX-ANM-01-017-018}

[]{#MA-SOL-ANM-01-017-018}

Calcula $\omega(t)$ para $x^2$ en $[0,1]$, para todo $t\ge0$. Da los pares que alcanzan cada cota y compara con $2t$.

## 17.19. Una raíz y su módulo

[]{#MA-EX-ANM-01-017-019}

[]{#MA-SOL-ANM-01-017-019}

Calcula el módulo exacto de $\sqrt{x}$ en $[0,1]$. Contrasta la dependencia en $t$ con la del cuadrado.

## 17.20. Valores no acotados y módulo finito

[]{#MA-EX-ANM-01-017-020}

[]{#MA-SOL-ANM-01-017-020}

Explica por qué no se puede concluir que una uniforme en $\mathbb R$ tiene valores acotados. Calcula el módulo de la identidad y prueba uniformidad directamente.

## 17.21. Radios para una suma

[]{#MA-EX-ANM-01-017-021}

[]{#MA-SOL-ANM-01-017-021}

[]{#MA-SEC-ANM-01-017-005}

Prueba uniformidad de $af+bg$ si $f,g$ son uniformes en el mismo dominio y $a,b$ son constantes. Trata constantes cero.

## 17.22. Factores que amplifican errores

[]{#MA-EX-ANM-01-017-022}

[]{#MA-SOL-ANM-01-017-022}

Prueba la regla de producto bajo cotas $M_f,M_g$. Muestra que eliminar ambas cotas pierde la garantía y que no son necesarias para todo producto particular.

## 17.23. Un cociente sobre dos piezas

[]{#MA-EX-ANM-01-017-023}

[]{#MA-SOL-ANM-01-017-023}

En $K=[-2,-1]\cup[1,2]$, sean $f(x)=x+1$ y $g(x)=x^2$. Da un radio explícito uniforme para $f/g$, usando cotas de numerador, denominador y diferencias.

## 17.24. El orden inverso de tolerancias

[]{#MA-EX-ANM-01-017-024}

[]{#MA-SOL-ANM-01-017-024}

Sean $f:D\to E$ y $g:E\to\mathbb R$ uniformes. Prueba uniformidad de $g\circ f$ y refuta sustituir uniformidad de $g$ por continuidad puntual.

## 17.25. Inversa uniforme sin control lineal

[]{#MA-EX-ANM-01-017-025}

[]{#MA-SOL-ANM-01-017-025}

Justifica que una inyección continua $f:K\to\mathbb R$ sobre compacto tiene inversa uniforme en su imagen. Da un ejemplo en que esa inversa no sea Lipschitz.

## 17.26. Rutas que no convergen

[]{#MA-EX-ANM-01-017-026}

[]{#MA-SOL-ANM-01-017-026}

[]{#MA-SEC-ANM-01-017-006}

Para $x_n=n+1$ y $y_n=n+1+1/(n+1)$, calcula las distancias de entrada y salida bajo el cuadrado. Usa sólo la dirección directa de R6 para concluir.

## 17.27. Dos familias y dos selecciones

[]{#MA-EX-ANM-01-017-027}

[]{#MA-SOL-ANM-01-017-027}

Reconstruye la recíproca secuencial de R6 bajo CC(R). Identifica las dos familias reales no vacías y explica por qué Heine–Cantor no queda condicionado por esta prueba.

## 17.28. Una enumeración de pares malos

[]{#MA-EX-ANM-01-017-028}

[]{#MA-SOL-ANM-01-017-028}

Supón dada una sobreyección $e:\mathbb N\to D$ no vacío. Construye los pares malos de una negación de uniformidad mediante mínimos de índices, sin CC(R).

## 17.29. Preservar una ruta de Cauchy

[]{#MA-EX-ANM-01-017-029}

[]{#MA-SOL-ANM-01-017-029}

Prueba que una uniforme envía toda ruta de Cauchy dada a otra de Cauchy. Refuta la recíproca universal con el cuadrado en $\mathbb R$.

## 17.30. Pares recíprocos y una frontera

[]{#MA-EX-ANM-01-017-030}

[]{#MA-SOL-ANM-01-017-030}

En $(0,1]$, usa $x_n=1/(n+2)$ y $y_n=1/(n+3)$ para comparar identidad y recíproco. ¿Qué aprende el test de pares?

## 17.31. Construir el corte de frontera

[]{#MA-EX-ANM-01-017-031}

[]{#MA-SOL-ANM-01-017-031}

[]{#MA-SEC-ANM-01-017-007}

Justifica no vacuidad/acotación de $E_{p,r}$ y que el corte $F(p)$ queda entre $L_{p,r}$ y $U_{p,r}$ para todo radio admisible. No elijas sucesiones aproximantes.

## 17.32. Anchuras que determinan un único real

[]{#MA-EX-ANM-01-017-032}

[]{#MA-SOL-ANM-01-017-032}

Prueba que diferencias menores que $\eta$ entre todos los valores de una imagen no vacía/acotada implican $U-L\le\eta$. Usa esto para justificar unicidad del valor extendido y coincidencia en $D$.

## 17.33. Uniformidad y unicidad de la extensión

[]{#MA-EX-ANM-01-017-033}

[]{#MA-SOL-ANM-01-017-033}

Completa la prueba de uniformidad de $F$ sobre $\overline D$ y de unicidad entre extensiones continuas. Declara los presupuestos y radios.

## 17.34. Extender y no poder extender

[]{#MA-EX-ANM-01-017-034}

[]{#MA-SOL-ANM-01-017-034}

Determina las extensiones continuas a $[0,1]$ de identidad y raíz en $(0,1]$. Prueba que el recíproco no admite extensión real continua allí.

## 17.35. Uniformidad en un dominio acotado

[]{#MA-EX-ANM-01-017-035}

[]{#MA-SOL-ANM-01-017-035}

Para $D\subseteq\mathbb R$ acotado, prueba que $f:D\to\mathbb R$ es uniforme si y sólo si admite extensión continua al cierre. Trata vacío y explica el papel del cierre compacto.

## 17.36. Construir la poligonal

[]{#MA-EX-ANM-01-017-036}

[]{#MA-SOL-ANM-01-017-036}

[]{#MA-SEC-ANM-01-017-008}

Para una continua $f:[a,b]\to\mathbb R$, $a<b$, construye $P$ y prueba existencia de malla, coincidencia en nodos y continuidad. No uses derivadas.

## 17.37. Controlar todo lo que queda entre nodos

[]{#MA-EX-ANM-01-017-037}

[]{#MA-SOL-ANM-01-017-037}

Prueba la cota uniforme de error de R8, incluidos pesos cero y la diferencia entre error puntual, supremo y máximo.

## 17.38. Certificado exacto de cuatro celdas

[]{#MA-EX-ANM-01-017-038}

[]{#MA-SOL-ANM-01-017-038}

Para $x^2$ en $[0,1]$, interpola con cuatro celdas iguales. Calcula el error máximo y todos los puntos donde se alcanza, por álgebra.

## 17.39. Muestras iguales y errores arbitrarios

[]{#MA-EX-ANM-01-017-039}

[]{#MA-SOL-ANM-01-017-039}

Dada una malla finita en $[a,b]$ con $a<b$, construye una función continua que valga cero en todos sus nodos y alcance una altura prescrita $H>0$ entre dos de ellos. Explica qué garantía falta.

## 17.40. Elegir una malla a partir de tolerancia

[]{#MA-EX-ANM-01-017-040}

[]{#MA-SOL-ANM-01-017-040}

Para $x^2$ en $[0,1]$, da una condición en $n$ que asegure error poligonal estrictamente menor que $\varepsilon>0$. Compárala con usar sólo el control Lipschitz dos y presupuesto $\varepsilon/2$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 17](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo.html) · [Ejercicios](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-17-continuidad-uniforme-una-escala-que-sirve-para-todo-soluciones.html)
