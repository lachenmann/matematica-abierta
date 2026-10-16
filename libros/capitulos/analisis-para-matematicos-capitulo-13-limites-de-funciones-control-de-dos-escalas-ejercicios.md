---
content-id: MA-BCH-0255
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-013-EJERCICIOS
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
title: Ejercicios — Capítulo 13
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C13_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html)

Las soluciones completas se encuentran en ANM-C13_SOLUCIONES.md. Justifica las respuestas y declara los dominios y puntos de acumulación. Distingue un candidato refutado de la inexistencia de cualquier límite, y una ruta dada de una selección de infractores.

## 13.1. El agujero no decide el destino

[]{#MA-EX-ANM-01-013-001}

[]{#MA-SOL-ANM-01-013-001}

[]{#MA-SEC-ANM-01-013-001}

Define $f:\mathbb R\to\mathbb R$ por $f(x)=2x+5$ si $x\ne-1$ y $f(-1)=100$. Prueba desde la definición el límite en $-1$ y explica qué dato se excluye.

## 13.2. Una pregunta sin entradas

[]{#MA-EX-ANM-01-013-002}

[]{#MA-SOL-ANM-01-013-002}

Para $D=\{0\}\cup[2,3]$ y cualquier $f:D\to\mathbb R$, analiza la fórmula perforada en $a=0$. ¿Hay un límite bajo la convención del capítulo?

## 13.3. Dos lenguajes del mismo control

[]{#MA-EX-ANM-01-013-003}

[]{#MA-SOL-ANM-01-013-003}

Prueba directamente que $f[U_D(a,\delta)]\subseteq B(L,\varepsilon)$ equivale a $U_D(a,\delta)\subseteq f^{-1}[B(L,\varepsilon)]$. Mantén separados valores y conjuntos.

## 13.4. Igualdad en un germen perforado

[]{#MA-EX-ANM-01-013-004}

[]{#MA-SOL-ANM-01-013-004}

Sean $f,g:D\to\mathbb R$ iguales siempre que $0<|x-a|<r$, con $r>0$ y $a\in D^{\prime}$. Prueba que tienen exactamente los mismos candidatos de límite.

## 13.5. Cambiar valores en infinitos puntos lejanos

[]{#MA-EX-ANM-01-013-005}

[]{#MA-SOL-ANM-01-013-005}

Construye dos funciones reales que difieran en infinitos puntos, una no acotada globalmente, y que tengan límite cero en cero por coincidencia local. Prueba las afirmaciones.

## 13.6. Diseñar el radio de una afín decreciente

[]{#MA-EX-ANM-01-013-006}

[]{#MA-SOL-ANM-01-013-006}

[]{#MA-SEC-ANM-01-013-002}

Prueba desde la definición que $-4x+7$ tiene límite $-1$ en $a=2$. Determina el mayor radio simétrico válido para un desafío $\varepsilon>0$.

## 13.7. Un radio conservador para un cuadrado

[]{#MA-EX-ANM-01-013-007}

[]{#MA-SOL-ANM-01-013-007}

Prueba desde la definición $x^2\to4$ en $2$ y da un radio explícito que no necesite resolver una desigualdad cuadrática.

## 13.8. Radio óptimo del cuadrado en uno

[]{#MA-EX-ANM-01-013-008}

[]{#MA-SOL-ANM-01-013-008}

Para $0<\varepsilon<1$, demuestra que el mayor radio simétrico para $|x^2-1|<\varepsilon$ alrededor de $1$ es $\delta_*=\sqrt{1+\varepsilon}-1$.

## 13.9. Reparar una respuesta que depende de la entrada

[]{#MA-EX-ANM-01-013-009}

[]{#MA-SOL-ANM-01-013-009}

Un borrador afirma: «Para probar $x^2\to1$, tomo $\delta=\varepsilon/(|x+1|+1)$; así el error será pequeño». Localiza el defecto y escribe una prueba válida.

## 13.10. Proteger un recíproco desplazado

[]{#MA-EX-ANM-01-013-010}

[]{#MA-SOL-ANM-01-013-010}

Prueba desde la definición que $1/(x-3)$ tiene límite $-1/2$ en $a=1$.

## 13.11. Una cota que incluye el centro

[]{#MA-EX-ANM-01-013-011}

[]{#MA-SOL-ANM-01-013-011}

[]{#MA-SEC-ANM-01-013-003}

Si $a\in D$, $a\in D^{\prime}$ y $f\to L$, prueba que $f$ está acotada en alguna ventana no perforada $D\cap B(a,r)$, sin suponer $f(a)=L$.

## 13.12. Encierro sin existencia supuesta

[]{#MA-EX-ANM-01-013-012}

[]{#MA-SOL-ANM-01-013-012}

Sea $f:\mathbb R\to\mathbb R$ y supongamos $-x^2\le f(x)\le2x^2$ para $0<|x|<1$. Prueba $f\to0$ sin usar reglas algebraicas posteriores.

## 13.13. Oscilar y aun así converger

[]{#MA-EX-ANM-01-013-013}

[]{#MA-SOL-ANM-01-013-013}

Sea $b(x)=1$ para $x$ racional y $b(x)=-1$ para $x$ irracional. Prueba que $h(x)=xb(x)$ tiene límite cero en cero, sin decidir si $b$ tiene límite.

## 13.14. El orden no conserva separación estricta

[]{#MA-EX-ANM-01-013-014}

[]{#MA-SOL-ANM-01-013-014}

Construye $f<g$ en una ventana perforada con el mismo límite, y prueba que en general sí se conserva el orden no estricto de límites.

## 13.15. Dos destinos no caben en una misma ventana

[]{#MA-EX-ANM-01-013-015}

[]{#MA-SOL-ANM-01-013-015}

Reconstruye la unicidad usando tolerancia $|L-M|/2$ en vez de un tercio. Explica por qué las desigualdades estrictas siguen bastando.

## 13.16. La frontera ya es infracción

[]{#MA-EX-ANM-01-013-016}

[]{#MA-SOL-ANM-01-013-016}

[]{#MA-SEC-ANM-01-013-004}

Para $f(x)=x$ en cero y candidato $L=1$, da una tolerancia fija y un infractor explícito para cada radio.

## 13.17. Una escala basta para todos los radios

[]{#MA-EX-ANM-01-013-017}

[]{#MA-SOL-ANM-01-013-017}

Sean $r_n>0$ tales que para cada $\delta>0$ existe $n$ con $r_n<\delta$. Prueba que la negación del límite equivale a no vaciedad de los infractores en cada escala $r_n$, para una misma tolerancia.

## 13.18. Todos los reales quedan descartados

[]{#MA-EX-ANM-01-013-018}

[]{#MA-SOL-ANM-01-013-018}

Prueba directamente, sin sucesiones, que $f(x)=1/|x|$ en $\mathbb R\setminus\{0\}$ no tiene límite real finito en cero.

## 13.19. Cada entrada favorable no es un límite

[]{#MA-EX-ANM-01-013-019}

[]{#MA-SOL-ANM-01-013-019}

Prueba que la condición «para todo $\varepsilon,\delta>0$ existe $x$ con $0<|x|<\delta$ y $|f(x)|<\varepsilon$» no garantiza $f\to0$.

## 13.20. Fallo sin magnitud infinita

[]{#MA-EX-ANM-01-013-020}

[]{#MA-SOL-ANM-01-013-020}

Construye una función globalmente acotada sin límite en cero y refútala para todo candidato mediante una tolerancia fija.

## 13.21. Una ruta favorable engaña

[]{#MA-EX-ANM-01-013-021}

[]{#MA-SOL-ANM-01-013-021}

[]{#MA-SEC-ANM-01-013-005}

Sea $f(x)=0$ si $x=1/(n+1)$ para algún $n\in\mathbb N$ y $f(x)=1$ en las demás entradas reales. Encuentra dos rutas admisibles en cero que descarten un límite.

## 13.22. Un prefijo puede tocar el centro

[]{#MA-EX-ANM-01-013-022}

[]{#MA-SOL-ANM-01-013-022}

Supón $f\to L$ en $a$, $x_n\in D$ y $x_n\to a$, con $x_n\ne a$ para todos los índices a partir de cierto $N_0$. Prueba $f(x_n)\to L$ si $f$ está definida en todos los términos.

## 13.23. El mínimo vive en los índices

[]{#MA-EX-ANM-01-013-023}

[]{#MA-SOL-ANM-01-013-023}

En un dominio enumerado, justifica la existencia del selector $x_n=e(\min I_n)$ y explica por qué no se toma el mínimo de $E_n\subseteq\mathbb R$.

## 13.24. La ruta de infracciones prueba la recíproca

[]{#MA-EX-ANM-01-013-024}

[]{#MA-SOL-ANM-01-013-024}

Bajo $\mathrm{CC}(\mathbb R)$, prueba la recíproca secuencial y localiza exactamente el uso de la hipótesis.

## 13.25. No hace falta una ruta distinta en cada paso

[]{#MA-EX-ANM-01-013-025}

[]{#MA-SOL-ANM-01-013-025}

Para el selector de infractores, demuestra que los términos no necesitan ser distintos entre sí, pero ningún punto fijo distinto de $a$ puede aparecer en índices arbitrariamente grandes.

## 13.26. Cancelar antes de usar un cociente

[]{#MA-EX-ANM-01-013-026}

[]{#MA-SOL-ANM-01-013-026}

[]{#MA-SEC-ANM-01-013-006}

Calcula y prueba el límite en $2$ de $(x^2-4)/(x-2)$ en su dominio natural. ¿Por qué no se usa directamente la regla de cociente?

## 13.27. Un denominador con ceros lejanos

[]{#MA-EX-ANM-01-013-027}

[]{#MA-SOL-ANM-01-013-027}

Sean $f(x)=x+1$, $g(x)=x^2-4$. Prueba el límite de $f/g$ en cero y declara el dominio.

## 13.28. Producto desde una identidad diferente

[]{#MA-EX-ANM-01-013-028}

[]{#MA-SOL-ANM-01-013-028}

Prueba la regla de producto utilizando $fg-LM=(f-L)(g-M)+L(g-M)+M(f-L)$ y un solo presupuesto para ambos errores.

## 13.29. Norma y diferencia de normas

[]{#MA-EX-ANM-01-013-029}

[]{#MA-SOL-ANM-01-013-029}

Si $f\to L$ y $g\to M$, prueba $\bigl||f|-|g|\bigr|\to\bigl||L|-|M|\bigr|$ y da un control directo del error con los dos errores originales.

## 13.30. Un producto converge sin límites de los factores

[]{#MA-EX-ANM-01-013-030}

[]{#MA-SOL-ANM-01-013-030}

Construye funciones $f,g$ sin límite en cero cuyo producto sí tenga límite. Prueba todas las afirmaciones.

## 13.31. El único lado disponible

[]{#MA-EX-ANM-01-013-031}

[]{#MA-SOL-ANM-01-013-031}

[]{#MA-SEC-ANM-01-013-007}

Sea $D=\{0\}\cup(0,2)$ y $f(x)=x^2$ para $x>0$, $f(0)=9$. Prueba el límite en cero a través de $D$ y analiza los límites laterales.

## 13.32. Reunir piezas finitas

[]{#MA-EX-ANM-01-013-032}

[]{#MA-SOL-ANM-01-013-032}

Sea $D=D_1\cup D_2$, $a\in D_1^{\prime}\cap D_2^{\prime}$, y supón que las dos restricciones de $f$ tienen el mismo límite $L$. Prueba el límite en $D$ y la recíproca.

## 13.33. Infinitas piezas no garantizan reunión

[]{#MA-EX-ANM-01-013-033}

[]{#MA-SOL-ANM-01-013-033}

Sea $D=(0,\infty)$ y $D_k=\{1/k\}\cup((0,\infty)\setminus\{1/j:j\in\mathbb N,\ j\ge1\})$ para $k\ge1$. Para $f(x)=1$ en los puntos $1/j$ y $f(x)=0$ en las demás entradas, prueba que cada restricción tiene límite cero y su unión no.

## 13.34. Una prueba densa puede omitir todo el problema

[]{#MA-EX-ANM-01-013-034}

[]{#MA-SOL-ANM-01-013-034}

Para el indicador de irracionales, prueba el límite restringido a los racionales en cero y refuta cualquier límite en el dominio real usando rutas explícitas.

## 13.35. Al menos un lado acumula

[]{#MA-EX-ANM-01-013-035}

[]{#MA-SOL-ANM-01-013-035}

Si $a\in D^{\prime}$, demuestra que acumula al menos uno de $D\cap(-\infty,a)$ y $D\cap(a,\infty)$. Si exactamente uno acumula, prueba que ese lado decide el límite completo.

## 13.36. La composición pierde el centro perforado

[]{#MA-EX-ANM-01-013-036}

[]{#MA-SOL-ANM-01-013-036}

[]{#MA-SEC-ANM-01-013-008}

Construye $f,g:\mathbb R\to\mathbb R$ con $\lim_{x\to0}f(x)=0$ y $\lim_{y\to0}g(y)=0$ pero $\lim_{x\to0}g(f(x))=2$. Explica la falla del argumento usual.

## 13.37. Componer dos cuadrados con certificados

[]{#MA-EX-ANM-01-013-037}

[]{#MA-SOL-ANM-01-013-037}

Prueba directamente mediante radios anidados que $x^4\to1$ en $1$, usando el certificado del cuadrado y la alternativa central para la segunda etapa.

## 13.38. La alternativa central sin límites conocidos

[]{#MA-EX-ANM-01-013-038}

[]{#MA-SOL-ANM-01-013-038}

Sean $f:D\to E$, $g:E\to\mathbb R$, $a\in D^{\prime}$. Supón que $f(x)=b\in E$ en alguna ventana perforada. Determina y prueba el límite de la composición sin suponer que exista un límite de $g$ en $b$.

## 13.39. Composición a través de un subconjunto de salidas

[]{#MA-EX-ANM-01-013-039}

[]{#MA-SOL-ANM-01-013-039}

Sean $f:D\to E$, $a\in D^{\prime}$, $b\in A^{\prime}$ para $A\subseteq E$, y $g:E\to\mathbb R$. Supón $f\to b$, $g|_A\to L$ y que $f(x)\in A\setminus\{b\}$ cerca de $a$. Prueba el límite de $g\circ f$ aunque $g$ no tenga límite en todo $E$.

## 13.40. Un criterio exacto para tocar una salida defectuosa

[]{#MA-EX-ANM-01-013-040}

[]{#MA-SOL-ANM-01-013-040}

Sean $f:D\to E$, $a\in D^{\prime}$, $b\in E\cap E^{\prime}$, $g:E\to\mathbb R$, $f\to b$ y $g\to L$ en $b$, con $g(b)\ne L$. Prueba que $g\circ f\to L$ si y sólo si $f(x)\ne b$ en alguna ventana perforada de $a$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 13](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html) · [Ejercicios](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas-soluciones.html)
