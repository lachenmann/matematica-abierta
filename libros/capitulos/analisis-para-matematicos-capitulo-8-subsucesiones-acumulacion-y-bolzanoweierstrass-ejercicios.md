---
content-id: MA-BCH-0235
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-008-EJERCICIOS
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
title: Ejercicios — Capítulo 8
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C08_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html) · [Ejercicios](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-soluciones.html)

Las soluciones completas se encuentran en ANM-C08_SOLUCIONES.md. Justifica las respuestas y declara los selectores cuando construyas una subsucesión.

## 8.1. Mapas de selección

[]{#MA-EX-ANM-01-008-001}

[]{#MA-SOL-ANM-01-008-001}

[]{#MA-SEC-ANM-01-008-001}

Para cada mapa $\mathbb N\to\mathbb N$ dado por $\varphi(k)=2k$, $\psi(k)=k^2$, $\eta(k)=\lfloor k/2\rfloor$ y $\theta(k)=k+5$, decide si es selector de subsucesión. Si lo es, calcula los tres primeros términos seleccionados de $a_n=1/(n+1)$.

## 8.2. Enumerar índices sin saltos ocultos

[]{#MA-EX-ANM-01-008-002}

[]{#MA-SOL-ANM-01-008-002}

Sea $E\subseteq\mathbb N$ infinito. Define $e_0=\min E$ y $e_{k+1}=\min\{n\in E:n>e_k\}$. Prueba que la construcción existe y que $\{e_k:k\in\mathbb N\}=E$.

## 8.3. Dos extracciones consecutivas

[]{#MA-EX-ANM-01-008-003}

[]{#MA-SOL-ANM-01-008-003}

Sea $a_n=n/(n+1)$, $b_k=a_{3k+2}$ y $c_j=b_{2j+1}$. Escribe los tres dominios de índices, el selector compuesto y una fórmula para $c_j$. ¿Conmutan los dos selectores?

## 8.4. Misma imagen, distinta selección

[]{#MA-EX-ANM-01-008-004}

[]{#MA-SOL-ANM-01-008-004}

Construye dos subsucesiones diferentes de una misma sucesión que tengan exactamente la misma imagen, y demuestra que son diferentes como funciones aunque sus imágenes coincidan.

## 8.5. Un umbral transportado y uno propio

[]{#MA-EX-ANM-01-008-005}

[]{#MA-SOL-ANM-01-008-005}

[]{#MA-SEC-ANM-01-008-002}

Para $a_n=3+1/(n+1)$ y $b_k=a_{2k+1}$, encuentra el menor umbral para la tolerancia $\varepsilon=1/10$ en cada sucesión. Compáralos con el umbral transportado de §8.2.

## 8.6. Intercalar dos límites iguales

[]{#MA-EX-ANM-01-008-006}

[]{#MA-SOL-ANM-01-008-006}

Supón que $a_{2k}\to L$ y $a_{2k+1}\to L$. Demuestra directamente que $a_n\to L$.

## 8.7. Una partición finita de índices

[]{#MA-EX-ANM-01-008-007}

[]{#MA-SOL-ANM-01-008-007}

Sea $m\ge2$ natural. Prueba que $a_n\to L$ si y sólo si $a_{mk+r}\to L$ para cada $r\in\{0,\ldots,m-1\}$.

## 8.8. Todos los términos salvo algunos

[]{#MA-EX-ANM-01-008-008}

[]{#MA-SOL-ANM-01-008-008}

Una prueba afirma: «Hay una subsucesión convergente a cero que selecciona todos los índices pares; los pares son infinitos, luego la sucesión converge a cero». Localiza el fallo, da un contraejemplo y demuestra una reparación si la selección omite sólo finitos índices.

## 8.9. Selección convergente de una monótona

[]{#MA-EX-ANM-01-008-009}

[]{#MA-SOL-ANM-01-008-009}

Sea $a$ monótona y supón que una subsucesión converge a $L\in\mathbb R$. Demuestra que $a_n\to L$ sin aplicar Bolzano–Weierstrass.

## 8.10. Una escala de radios basta

[]{#MA-EX-ANM-01-008-010}

[]{#MA-SOL-ANM-01-008-010}

[]{#MA-SEC-ANM-01-008-003}

Demuestra que $L$ es punto secuencial de $a$ si y sólo si para cada $q\in\mathbb N$ y cada $N\in\mathbb N$ hay $n\ge N$ con $|a_n-L|<1/(q+1)$.

## 8.11. Un destino prescrito con escapes

[]{#MA-EX-ANM-01-008-011}

[]{#MA-SOL-ANM-01-008-011}

Dados $L,H\in\mathbb R$ distintos, construye una sucesión acotada cuyo conjunto de puntos secuenciales sea exactamente $\{L,H\}$. Prueba que no tiene otros.

## 8.12. Alejar los índices tanto como se quiera

[]{#MA-EX-ANM-01-008-012}

[]{#MA-SOL-ANM-01-008-012}

Si $L$ es punto secuencial de $a$ y $h:\mathbb N\to\mathbb N$ es cualquier función, prueba que existe un selector $\varphi$ con $\varphi(k)\ge h(k)$ y $|a_{\varphi(k)}-L|<1/(k+1)$ para todo $k$.

## 8.13. El conjunto de destinos es cerrado

[]{#MA-EX-ANM-01-008-013}

[]{#MA-SOL-ANM-01-008-013}

Sea $C$ el conjunto de puntos de acumulación secuencial de una sucesión real $a$. Demuestra que $C$ es cerrado, sin suponer que $a$ sea acotada.

## 8.14. Destinos de una partición finita

[]{#MA-EX-ANM-01-008-014}

[]{#MA-SOL-ANM-01-008-014}

Sea $m\ge2$ natural. Prueba que el conjunto de puntos secuenciales de $a$ es la unión de los conjuntos de puntos secuenciales de las $m$ sucesiones $b^{(r)}_k=a_{mk+r}$.

## 8.15. Tres conjuntos diferentes

[]{#MA-EX-ANM-01-008-015}

[]{#MA-SOL-ANM-01-008-015}

[]{#MA-SEC-ANM-01-008-004}

Para $a_0=3$ y $a_n=1/n$ cuando $n\ge1$, determina la imagen, su clausura, su conjunto de acumulación y los puntos secuenciales de $a$. Justifica las exclusiones.

## 8.16. Cambios finitos del conjunto

[]{#MA-EX-ANM-01-008-016}

[]{#MA-SOL-ANM-01-008-016}

Sea $F\subseteq\mathbb R$ finito y $A\subseteq\mathbb R$. Demuestra que $\operatorname{Acc}(A\setminus F)=\operatorname{Acc}(A)=\operatorname{Acc}(A\cup F)$.

## 8.17. Cuando no se repiten valores

[]{#MA-EX-ANM-01-008-017}

[]{#MA-SOL-ANM-01-008-017}

Supón que cada valor real aparece sólo finitas veces en $a$. Si $A=a(\mathbb N)$, prueba que los puntos secuenciales de $a$ coinciden con $\operatorname{Acc}(A)$.

## 8.18. Misma imagen y destinos diferentes

[]{#MA-EX-ANM-01-008-018}

[]{#MA-SOL-ANM-01-008-018}

Construye dos sucesiones con imagen $A=\{1,1/2,1/3,\ldots\}$ cuyos conjuntos de puntos secuenciales sean diferentes. Determina ambos conjuntos.

## 8.19. Una elección mal justificada

[]{#MA-EX-ANM-01-008-019}

[]{#MA-SOL-ANM-01-008-019}

Audita esta frase: «Si $L$ es adherente a $A$, elegimos el menor punto de $A\cap B(L,1/(k+1))$». Da un ejemplo en que esa elección no exista y repara la prueba.

## 8.20. Caracterizar los cerrados por límites

[]{#MA-EX-ANM-01-008-020}

[]{#MA-SOL-ANM-01-008-020}

Demuestra que $F\subseteq\mathbb R$ es cerrado si y sólo si el límite de toda sucesión convergente con valores en $F$ pertenece a $F$. Trata el caso vacío.

## 8.21. Primeras mitades y reserva

[]{#MA-EX-ANM-01-008-021}

[]{#MA-SOL-ANM-01-008-021}

[]{#MA-SEC-ANM-01-008-005}

Para $a_n=(-1)^n/(n+1)$ e $I_0=[-1,1]$, aplica la regla de preferencia izquierda durante los tres primeros pasos. Explica por qué la reserva de índices es infinita en cada intervalo obtenido.

## 8.22. Un invariante demasiado débil

[]{#MA-EX-ANM-01-008-022}

[]{#MA-SOL-ANM-01-008-022}

Sea $a_0=0$ y $a_n=1$ para $n\ge1$. Los intervalos $I_k=[-2^{-k},2^{-k}]$ son cerrados, encajados, de anchura tendente a cero y contienen algún término de $a$. ¿Puede extraerse una subsucesión con $a_{n_k}\in I_k$ para todo $k$? Explica.

## 8.23. Dividir en más partes

[]{#MA-EX-ANM-01-008-023}

[]{#MA-SOL-ANM-01-008-023}

Sea $m\ge2$ natural. Adapta la construcción de §8.5 dividiendo cada intervalo en $m$ subintervalos cerrados de igual anchura. Fija una regla inequívoca de elección y prueba las propiedades necesarias para obtener un punto común único.

## 8.24. Anchuras pequeñas sin intersección

[]{#MA-EX-ANM-01-008-024}

[]{#MA-SOL-ANM-01-008-024}

Exhibe una familia de intervalos abiertos no vacíos y encajados de anchuras arbitrariamente pequeñas cuya intersección sea vacía. Explica qué paso de §8.5 deja de estar autorizado.

## 8.25. El punto común como supremo

[]{#MA-EX-ANM-01-008-025}

[]{#MA-SOL-ANM-01-008-025}

Para los intervalos $I_k=[u_k,v_k]$ de §8.5, reconstruye la existencia del punto común tomando $L=\sup\{u_k:k\in\mathbb N\}$. Verifica ambas desigualdades para cada intervalo y después la unicidad.

## 8.26. Los mínimos de la extracción

[]{#MA-EX-ANM-01-008-026}

[]{#MA-SOL-ANM-01-008-026}

[]{#MA-SEC-ANM-01-008-006}

Para el ejemplo alternante recíproco de §§8.5–8.6, verifica los seis índices $n_0,\ldots,n_5$ y demuestra que $n_k=2^{k-1}-1$ para $k\ge4$.

## 8.27. Una extracción todavía más tardía

[]{#MA-EX-ANM-01-008-027}

[]{#MA-SOL-ANM-01-008-027}

En la prueba de Bolzano–Weierstrass, sustituye la regla por $n_0=\min\{n\in E_0:n\ge h(0)\}$ y $n_{k+1}=\min\{n\in E_{k+1}:n>n_k,\ n\ge h(k+1)\}$, donde $h:\mathbb N\to\mathbb N$. Prueba que la extracción sigue convergiendo al mismo punto común.

## 8.28. Lo que no promete la existencia

[]{#MA-EX-ANM-01-008-028}

[]{#MA-SOL-ANM-01-008-028}

Construye una sucesión acotada con una subsucesión convergente y otra no convergente, ambas distintas de la sucesión original. Justifica todas las afirmaciones.

## 8.29. Extracciones simultáneas

[]{#MA-EX-ANM-01-008-029}

[]{#MA-SOL-ANM-01-008-029}

Sean $a$ y $b$ dos sucesiones reales acotadas. Prueba que existe un mismo selector $\theta$ tal que $a_{\theta(j)}$ y $b_{\theta(j)}$ convergen, posiblemente a límites diferentes. Extiende el argumento a una familia finita de sucesiones acotadas.

## 8.30. Un selector para numerables sucesiones

[]{#MA-EX-ANM-01-008-030}

[]{#MA-SOL-ANM-01-008-030}

Sea $(a^{(r)})_{r\in\mathbb N}$ una familia de sucesiones reales, cada una acotada. Demuestra que hay un selector $\theta$ tal que $a^{(r)}_{\theta(k)}$ converge para cada $r$ fijo. No se exige una cota común a toda la familia.

## 8.31. Dos hipótesis de un conjunto

[]{#MA-EX-ANM-01-008-031}

[]{#MA-SOL-ANM-01-008-031}

[]{#MA-SEC-ANM-01-008-007}

Exhibe un conjunto acotado sin puntos de acumulación y un conjunto infinito sin puntos de acumulación. Prueba ambos casos y explica por qué ninguno contradice §8.7.

## 8.32. Un cerrado que retiene el destino

[]{#MA-EX-ANM-01-008-032}

[]{#MA-SOL-ANM-01-008-032}

Sean $u\le v$ reales y $a_n\in[u,v]$. Demuestra que existe una subsucesión convergente a $L\in[u,v]$. Después muestra que la conclusión con $L\in(u,v)$ puede fallar para términos en un intervalo abierto no vacío.

## 8.33. Conjunto cerrado acotado sin acumulación

[]{#MA-EX-ANM-01-008-033}

[]{#MA-SOL-ANM-01-008-033}

Prueba que un conjunto acotado $A\subseteq\mathbb R$ sin puntos de acumulación es finito. ¿Hace falta que sea cerrado? Justifica.

## 8.34. Conjuntos de destinos acotados

[]{#MA-EX-ANM-01-008-034}

[]{#MA-SOL-ANM-01-008-034}

Sea $a$ acotada por $|a_n|\le M$. Demuestra que su conjunto $C$ de puntos secuenciales es no vacío, cerrado y contenido en $[-M,M]$.

## 8.35. Distancia positiva entre dos cerrados

[]{#MA-EX-ANM-01-008-035}

[]{#MA-SOL-ANM-01-008-035}

Sean $A,B\subseteq\mathbb R$ cerrados, no vacíos y disjuntos. Supón que $A$ es acotado. Demuestra que existe $\delta>0$ tal que $|x-y|\ge\delta$ para todo $x\in A$ y $y\in B$.

## 8.36. Toda extracción puede refinarse

[]{#MA-EX-ANM-01-008-036}

[]{#MA-SOL-ANM-01-008-036}

[]{#MA-SEC-ANM-01-008-008}

Prueba que $a_n\to L$ si y sólo si toda subsucesión de $a$ tiene a su vez una subsucesión que converge a $L$. No supongas acotación.

## 8.37. Clasificar una familia intercalada

[]{#MA-EX-ANM-01-008-037}

[]{#MA-SOL-ANM-01-008-037}

Para $p,q\in\mathbb R$, define $a_{2k}=p+1/(k+1)$ y $a_{2k+1}=q-1/(k+1)$. Determina sus puntos secuenciales y para qué parámetros converge.

## 8.38. Un radio que depende del corte

[]{#MA-EX-ANM-01-008-038}

[]{#MA-SOL-ANM-01-008-038}

Explica por qué la condición «para cada $N$ existen $n\ge N$ y $\varepsilon_N>0$ con $|a_n-L|\ge\varepsilon_N$» no niega la convergencia. Da un contraejemplo y formula la negación correcta.

## 8.39. Acercarse a un conjunto finito de destinos

[]{#MA-EX-ANM-01-008-039}

[]{#MA-SOL-ANM-01-008-039}

Supón que $a$ es acotada y que su conjunto de puntos secuenciales es el conjunto finito no vacío $\{L_1,\ldots,L_m\}$. Prueba que para todo $\varepsilon>0$, todos los términos suficientemente tardíos pertenecen a $\bigcup_{i=1}^m B(L_i,\varepsilon)$.

## 8.40. Saltos pequeños y destinos intermedios

[]{#MA-EX-ANM-01-008-040}

[]{#MA-SOL-ANM-01-008-040}

Sea $a$ una sucesión real acotada con $|a_{n+1}-a_n|\to0$. Si $p<q$ son puntos secuenciales, demuestra que todo $t\in(p,q)$ también es punto secuencial.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html) · [Ejercicios](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass-soluciones.html)
