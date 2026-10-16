---
content-id: MA-BCH-0259
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-014-EJERCICIOS
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
title: Ejercicios — Capítulo 14
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C14_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html)

Las soluciones completas se encuentran en ANM-C14_SOLUCIONES.md. Justifica las respuestas y declara los dominios y puntos de acumulación. Distingue continuidad de límite perforado, preimagen de imagen y control inverso de existencia de inversa. Declara cualquier hipótesis de selección al usar la recíproca secuencial.

## 14.1. Una respuesta afín centrada

[]{#MA-EX-ANM-01-014-001}

[]{#MA-SOL-ANM-01-014-001}

[]{#MA-SEC-ANM-01-014-001}

Prueba desde la definición que $f(x)=-3x+2$ es continua en cada real $a$. Trata explícitamente el centro.

## 14.2. Reparar un único valor del cuadrado

[]{#MA-EX-ANM-01-014-002}

[]{#MA-SOL-ANM-01-014-002}

Define $h_c(x)=x^2$ si $x\ne2$ y $h_c(2)=c$. Determina para qué $c$ es continua en $2$, y prueba el resultado.

## 14.3. El límite existe y la continuidad falla

[]{#MA-EX-ANM-01-014-003}

[]{#MA-SOL-ANM-01-014-003}

Construye una función con límite finito en cero que no sea continua allí. Da un infractor explícito para cada radio de continuidad.

## 14.4. No intercambiar el punto y la respuesta

[]{#MA-EX-ANM-01-014-004}

[]{#MA-SOL-ANM-01-014-004}

Explica por qué continuidad en todo $D$ no permite escribir sin más $\forall\varepsilon>0\ \exists\delta>0\ \forall a,x\in D$ para el mismo control. Identifica la dependencia permitida y un cálculo que la haga visible.

## 14.5. Ventana completa, imagen y preimagen

[]{#MA-EX-ANM-01-014-005}

[]{#MA-SOL-ANM-01-014-005}

Demuestra que el contrato puntual equivale tanto a la inclusión de imágenes de bolas relativas como a la inclusión de la bola relativa en una preimagen. Explica por qué ninguna necesita inversa funcional.

## 14.6. Un salto entre puntos sin vecinos

[]{#MA-EX-ANM-01-014-006}

[]{#MA-SOL-ANM-01-014-006}

[]{#MA-SEC-ANM-01-014-002}

En $D=\{0\}\cup[1,2]$, define $f(0)=100$ y $f(x)=x$ en el intervalo. Prueba continuidad en todo $D$ y explica por qué la separación del gráfico no la contradice.

## 14.7. Restringir puede eliminar la falla

[]{#MA-EX-ANM-01-014-007}

[]{#MA-SOL-ANM-01-014-007}

Sea $s(x)=-1$ para $x<0$ y $s(x)=1$ para $x\ge0$. Prueba que es discontinua en cero sobre $\mathbb R$ y que su restricción a $[0,\infty)$ es continua allí.

## 14.8. Extender un cociente con hueco

[]{#MA-EX-ANM-01-014-008}

[]{#MA-SOL-ANM-01-014-008}

Para $f(x)=(x^2-9)/(x-3)$ en $D=\mathbb R\setminus\{3\}$, encuentra y prueba la única extensión continua a toda la recta.

## 14.9. Una modificación local debe incluir el centro

[]{#MA-EX-ANM-01-014-009}

[]{#MA-SOL-ANM-01-014-009}

Da dos funciones que coincidan en toda ventana perforada de cero y tengan continuidad distinta allí. Después prueba que la coincidencia en una ventana completa sí preserva continuidad.

## 14.10. Ningún valor repara un salto

[]{#MA-EX-ANM-01-014-010}

[]{#MA-SOL-ANM-01-014-010}

Sea $f(x)=-2$ para $x<0$ y $f(x)=3$ para $x>0$, sin valor en cero. Prueba que ninguna elección de $f(0)$ produce una extensión continua.

## 14.11. La ruta vuelve al centro

[]{#MA-EX-ANM-01-014-011}

[]{#MA-SOL-ANM-01-014-011}

[]{#MA-SEC-ANM-01-014-003}

Si $f$ es continua en $a$, considera $x_{2n}=a$ y $x_{2n+1}=a+1/(n+1)$, suponiendo que todos los términos estén en $D$. Prueba convergencia de entradas e imágenes.

## 14.12. Ruta en un punto aislado

[]{#MA-EX-ANM-01-014-012}

[]{#MA-SOL-ANM-01-014-012}

Demuestra que si $a$ es aislado en $D$ y $x_n\in D$, $x_n\to a$, entonces $x_n=a$ eventualmente. Deduce el transporte de imágenes para cualquier $f:D\to\mathbb R$.

## 14.13. El infractor evita solo el centro

[]{#MA-EX-ANM-01-014-013}

[]{#MA-SOL-ANM-01-014-013}

Niega el contrato de continuidad y demuestra que todos los puntos del conjunto infractor para tolerancia positiva son distintos de $a$. Compara con el criterio de límite de C13.

## 14.14. Reconstruir la recíproca enumerada

[]{#MA-EX-ANM-01-014-014}

[]{#MA-SOL-ANM-01-014-014}

Con $e:\mathbb N\to D$ sobreyectiva dada, prueba que preservar todas las rutas convergentes a $a$ fuerza continuidad en $a$. Indica qué objeto tiene un mínimo.

## 14.15. Auditar una prueba sin selector

[]{#MA-EX-ANM-01-014-015}

[]{#MA-SOL-ANM-01-014-015}

Un borrador dice: «Como cada $E_n$ es no vacío, elegimos $x_n\in E_n$ para todos los índices; queda probada la equivalencia secuencial en cualquier dominio». Repara su alcance sin adoptar un axioma silencioso.

## 14.16. Un abierto que contiene un extremo

[]{#MA-EX-ANM-01-014-016}

[]{#MA-SOL-ANM-01-014-016}

[]{#MA-SEC-ANM-01-014-004}

Para la inclusión $f:[0,2]\to\mathbb R$, $f(x)=x$, calcula la preimagen de $(-1,1)$ y explica con radios su apertura relativa y su falta de apertura absoluta.

## 14.17. La preimagen tiene dos piezas

[]{#MA-EX-ANM-01-014-017}

[]{#MA-SOL-ANM-01-014-017}

Para $q:\mathbb R\to\mathbb R$, $q(x)=x^2$, calcula $q^{-1}[(1,4)]$ y prueba su apertura sin confundirla con una inversa del cuadrado.

## 14.18. Basta una base de intervalos

[]{#MA-EX-ANM-01-014-018}

[]{#MA-SOL-ANM-01-014-018}

Supón que para cada intervalo abierto real $I$, la preimagen $f^{-1}[I]$ es abierta relativa a $D$. Prueba continuidad de $f:D\to\mathbb R$.

## 14.19. Ceros cerrados en el ambiente correcto

[]{#MA-EX-ANM-01-014-019}

[]{#MA-SOL-ANM-01-014-019}

Sea $D=(0,1)$ y $f:D\to\mathbb R$ la función cero. Describe su conjunto de ceros y explica por qué el criterio de cerrados no afirma que sea cerrado en $\mathbb R$.

## 14.20. Codominio restringido y preimágenes

[]{#MA-EX-ANM-01-014-020}

[]{#MA-SOL-ANM-01-014-020}

Sean $f:D\to E\subseteq\mathbb R$ y $V=E\cap U$, con $U$ abierto absoluto. Demuestra $f^{-1}[V]=f^{-1}[U]$ y deduce el criterio de continuidad con abiertos relativos de $E$.

## 14.21. Producto con un valor central nulo

[]{#MA-EX-ANM-01-014-021}

[]{#MA-SOL-ANM-01-014-021}

[]{#MA-SEC-ANM-01-014-005}

Supón $f,g:D\to\mathbb R$ continuas en $a$ con $f(a)=0$. Prueba continuidad de $fg$ usando una cota local y un único error variable.

## 14.22. Cociente con dominio declarado

[]{#MA-EX-ANM-01-014-022}

[]{#MA-SOL-ANM-01-014-022}

Prueba continuidad de $r(x)=(x^2+1)/(x-2)$ en su dominio natural y explica qué se puede afirmar en $2$.

## 14.23. Composición que toca el centro

[]{#MA-EX-ANM-01-014-023}

[]{#MA-SOL-ANM-01-014-023}

Prueba directamente que $h(x)=|2x|$ es continua en cero por radios anidados, permitiendo $2x=0$.

## 14.24. Composición sólo donde existe

[]{#MA-EX-ANM-01-014-024}

[]{#MA-SOL-ANM-01-014-024}

Toma $f(x)=x^2$ en $\mathbb R$ y $g(y)=1/(y-1)$ en $E=\mathbb R\setminus\{1\}$. Determina el dominio efectivo de composición y prueba continuidad allí.

## 14.25. Composición por regiones de salida

[]{#MA-EX-ANM-01-014-025}

[]{#MA-SOL-ANM-01-014-025}

Demuestra continuidad global de la composición de $f:D\to E$ y $g:E\to\mathbb R$ continuas usando sólo el criterio de preimágenes. Justifica cada ambiente.

## 14.26. Imagen cerrada que pierde la cerradura

[]{#MA-EX-ANM-01-014-026}

[]{#MA-SOL-ANM-01-014-026}

[]{#MA-SEC-ANM-01-014-006}

Prueba que la función $r(x)=1/(1+x^2)$ es continua en $\mathbb R$ y tiene imagen exactamente $(0,1]$. Refuta cerradura de la imagen mediante un punto adherente.

## 14.27. Auditar la biyección y su inversa

[]{#MA-EX-ANM-01-014-027}

[]{#MA-SOL-ANM-01-014-027}

Verifica la bijectividad y continuidad de la función por piezas de §14.6. Refuta directamente la continuidad de su inversa en uno.

## 14.28. La identidad de un transporte reversible

[]{#MA-EX-ANM-01-014-028}

[]{#MA-SOL-ANM-01-014-028}

Prueba que una biyección $f:D\to E$ tiene inversa continua si y sólo si envía cada abierto relativo de $D$ a un abierto relativo de $E$.

## 14.29. Una afín es un homeomorfismo

[]{#MA-EX-ANM-01-014-029}

[]{#MA-SOL-ANM-01-014-029}

Para $m\ne0$, prueba que $f:\mathbb R\to\mathbb R$, $f(x)=mx+c$, es un homeomorfismo con certificados en ambas direcciones.

## 14.30. Controles inversos sin intervalos compactos

[]{#MA-EX-ANM-01-014-030}

[]{#MA-SOL-ANM-01-014-030}

Sea $f:D\to E$ una biyección continua que es abierta. Prueba que la imagen por $f$ de cualquier cerrado relativo a $D$ es cerrada relativa a $E$. No uses compacidad.

## 14.31. Pegar un valor absoluto desplazado

[]{#MA-EX-ANM-01-014-031}

[]{#MA-SOL-ANM-01-014-031}

[]{#MA-SEC-ANM-01-014-007}

Prueba continuidad de $f(x)=2-x$ para $x\le2$ y $f(x)=x-2$ para $x\ge2$ mediante el teorema de pegado finito.

## 14.32. Localizar con una cobertura abierta

[]{#MA-EX-ANM-01-014-032}

[]{#MA-SOL-ANM-01-014-032}

Demuestra que si una función es continua en la restricción a cada pieza de una cobertura abierta relativa de $D$, entonces es continua en $D$, aunque haya infinitas piezas.

## 14.33. El acuerdo sin cierre no basta

[]{#MA-EX-ANM-01-014-033}

[]{#MA-SOL-ANM-01-014-033}

Construye una función pegada a partir de dos restricciones continuas que coincidan en su intersección y que sea discontinua. Identifica la hipótesis ausente.

## 14.34. Una cobertura cerrada infinita falla

[]{#MA-EX-ANM-01-014-034}

[]{#MA-SOL-ANM-01-014-034}

En $D=\{0\}\cup\{1/n:n\ge1\}$, define $f(0)=0$, $f(1/n)=1$. Prueba que las piezas singleton forman una cobertura cerrada relativa con restricciones continuas, pero la función completa no es continua en cero.

## 14.35. Conservar un signo cerca del centro

[]{#MA-EX-ANM-01-014-035}

[]{#MA-SOL-ANM-01-014-035}

Supón $f:D\to\mathbb R$ continua en $a$ y $f(a)<0$. Prueba que existe una ventana relativa en que todos sus valores son negativos. Formula también la conclusión topológica global para $f<0$.

## 14.36. Un certificado directo del cuadrado

[]{#MA-EX-ANM-01-014-036}

[]{#MA-SOL-ANM-01-014-036}

[]{#MA-SEC-ANM-01-014-008}

Prueba continuidad de $x^2$ en cada centro con una cota local lineal, y trata $x=a$ sin usar una desigualdad estricta inválida.

## 14.37. La raíz en un extremo del dominio

[]{#MA-EX-ANM-01-014-037}

[]{#MA-SOL-ANM-01-014-037}

Prueba continuidad de $\sqrt{x}$ en cero sobre $[0,\infty)$ y justifica por qué no se consideran entradas negativas.

## 14.38. Continuidad sin barrera lineal

[]{#MA-EX-ANM-01-014-038}

[]{#MA-SOL-ANM-01-014-038}

Prueba que la raíz en cero no satisface $\sqrt{x}\le Kx$ en ninguna ventana positiva para ninguna constante finita $K\ge0$, pese a ser continua.

## 14.39. Invertir el cuadrado lejos de cero

[]{#MA-EX-ANM-01-014-039}

[]{#MA-SOL-ANM-01-014-039}

Para $m>0$, prueba que $q:[m,\infty)\to[m^2,\infty)$, $q(x)=x^2$, es biyectiva y que su inversa tiene un certificado lineal de continuidad.

## 14.40. El control inferior local no autoriza la inversa

[]{#MA-EX-ANM-01-014-040}

[]{#MA-SOL-ANM-01-014-040}

Construye una biyección continua y un centro no aislado $a$ donde valga localmente $|f(x)-f(a)|\ge|x-a|$, pero cuya inversa no sea continua en $f(a)$. Explica el defecto lógico de usar esa cota local para probar continuidad inversa.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html)
