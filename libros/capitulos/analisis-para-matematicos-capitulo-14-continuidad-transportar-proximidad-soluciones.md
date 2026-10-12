---
content-id: MA-BCH-0260
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-014-SOLUCIONES
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
title: Soluciones — Capítulo 14
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C14_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html)

## 14.1. Una respuesta afín centrada

[]{#MA-EX-ANM-01-014-001}

[]{#MA-SOL-ANM-01-014-001}

[]{#MA-SEC-ANM-01-014-001}

Fijemos $a$ y $\varepsilon>0$. Tomamos $\delta=\varepsilon/3>0$. Para toda entrada con $|x-a|<\delta$, el error es $|(-3x+2)-(-3a+2)|=3|x-a|<\varepsilon$. Si $x=a$, esa identidad produce cero, así que no necesitamos excluir el centro. La arbitrariedad de $a$ prueba continuidad en toda la recta.

## 14.2. Reparar un único valor del cuadrado

[]{#MA-EX-ANM-01-014-002}

[]{#MA-SOL-ANM-01-014-002}

El límite perforado es $4$ por C13 y no cambia al modificar sólo el centro. Como $2$ acumula puntos de la recta, §14.1 implica continuidad exactamente cuando $c=4$. Para ese valor, un certificado directo es $\delta=\min(1,\varepsilon/5)$: $|x+2|<5$ para $|x-2|<1$, y el error $|x^2-4|<\varepsilon$ fuera del centro; en él es cero. La necesidad procede de la unicidad del límite, no de un dibujo.

**Retorno visual.** Véase [C14-F01](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 14.3. El límite existe y la continuidad falla

[]{#MA-EX-ANM-01-014-003}

[]{#MA-SOL-ANM-01-014-003}

Sea $f(x)=0$ para $x\ne0$ y $f(0)=2$. El límite perforado es cero, con error cero para todo desafío. Para continuidad, fijamos $\varepsilon_0=1$; dado $\delta>0$, $x=\delta/2$ es distinto de cero, está en la ventana y tiene error $|f(x)-f(0)|=2\ge1$. Así la función falla en cero pese a tener límite.

## 14.4. No intercambiar el punto y la respuesta

[]{#MA-EX-ANM-01-014-004}

[]{#MA-SOL-ANM-01-014-004}

El contrato demostrado es $\forall a\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D$. Mover $a$ detrás de $\exists\delta$ exige una respuesta común para todos los centros, una condición adicional. Para $x^2$, el cálculo local de §14.8 entrega $\delta(a,\varepsilon)=\min(1,\varepsilon/(1+2|a|))$, que depende de $a$. Esa fórmula muestra la dependencia de la prueba; por sí sola no demuestra imposibilidad de algún otro radio común. Tal cuestión se estudia en C17.

## 14.5. Ventana completa, imagen y preimagen

[]{#MA-EX-ANM-01-014-005}

[]{#MA-SOL-ANM-01-014-005}

Para $\varepsilon$ y un radio $\delta$, todo $x\in D\cap B(a,\delta)$ cumple el error exactamente cuando $f(x)\in B(f(a),\varepsilon)$. Esto equivale a que toda imagen de esa bola esté en la bola de salida, por definición de imagen con testigo; también equivale a $x\in f^{-1}[B(f(a),\varepsilon)]$ para todas esas entradas. Cuantificar sobre cada $\varepsilon$ y algún $\delta$ da las tres formulaciones. La preimagen se define por pertenencia $f(x)\in V$, aunque $f$ sea constante o no inyectiva.

## 14.6. Un salto entre puntos sin vecinos

[]{#MA-EX-ANM-01-014-006}

[]{#MA-SOL-ANM-01-014-006}

[]{#MA-SEC-ANM-01-014-002}

En cero, radio $1/2$ confina la bola relativa al centro y da error cero para toda tolerancia. En un centro $a\in[1,2]$, tome $\delta=\min(1/2,\varepsilon)$; la entrada cero queda fuera y toda entrada pertinente pertenece al intervalo, donde el error es $|x-a|<\varepsilon$. No hay entradas entre cero y uno, así que continuidad relativa no exige conectar las dos piezas por un trazo.

**Retorno visual.** Véase [C14-F02](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 14.7. Restringir puede eliminar la falla

[]{#MA-EX-ANM-01-014-007}

[]{#MA-SOL-ANM-01-014-007}

En el dominio real, para tolerancia $1$ y cualquier radio, $x=-\delta/2$ tiene error dos respecto de $s(0)=1$. En el dominio restringido, la función es constante uno y todo radio positivo da error cero. No contradice el teorema de restricción: éste preserva continuidad ya existente, pero no prohíbe que al retirar infractores aparezca continuidad.

## 14.8. Extender un cociente con hueco

[]{#MA-EX-ANM-01-014-008}

[]{#MA-SOL-ANM-01-014-008}

En $D$, la factorización da $f(x)=x+3$. Su límite en tres es seis, con radio $\varepsilon$ para el error $|x-3|$. La extensión única asigna $F(3)=6$, y entonces $F(x)=x+3$ en toda la recta. El error $|F(x)-F(a)|=|x-a|$ prueba continuidad en cada centro. La unicidad se sigue del teorema de extensión; cancelar no define por sí solo el cociente original en tres.

## 14.9. Una modificación local debe incluir el centro

[]{#MA-EX-ANM-01-014-009}

[]{#MA-SOL-ANM-01-014-009}

La función cero y la función con valor uno sólo en cero coinciden fuera del centro; la primera es continua y la segunda falla por la ruta $\delta/2$ con error uno. Si $f=g$ en $D\cap B(a,r)$, el centro pertenece a esa región, así que $f(a)=g(a)$. Ante un radio de continuidad $\delta_f$, el mínimo con $r$ asegura igualdad de valores y errores para toda entrada cercana. Esto prueba la ida; intercambiar las funciones prueba la vuelta.

## 14.10. Ningún valor repara un salto

[]{#MA-EX-ANM-01-014-010}

[]{#MA-SOL-ANM-01-014-010}

Las rutas $u_n=-1/(n+1)$ y $v_n=1/(n+1)$ tienen imágenes constantes $-2$ y $3$. Si una extensión con valor $c$ fuese continua en cero, la dirección secuencial directa obligaría ambas imágenes a converger a $c$; unicidad secuencial daría $c=-2=3$, contradicción. Las rutas explícitas no requieren selección numerable.

## 14.11. La ruta vuelve al centro

[]{#MA-EX-ANM-01-014-011}

[]{#MA-SOL-ANM-01-014-011}

[]{#MA-SEC-ANM-01-014-003}

Los términos pares tienen distancia cero y los impares distancia $1/(n+1)$, que tiende a cero. Para $\delta>0$ escoja $N$ con $1/(n+1)<\delta$ si $n\ge N$; todo índice $k\ge2N$ tiene distancia menor que $\delta$, pues en el caso impar su subíndice es al menos $N$. Luego $x_k\to a$. Continuidad y el criterio directo dan $f(x_k)\to f(a)$, incluyendo los retornos centrales.

## 14.12. Ruta en un punto aislado

[]{#MA-EX-ANM-01-014-012}

[]{#MA-SOL-ANM-01-014-012}

Existe $r>0$ con $D\cap B(a,r)=\{a\}$. La convergencia da una cola con $|x_n-a|<r$; por pertenencia al dominio, cada término de esa cola es $a$. Las imágenes son entonces eventualmente constantes $f(a)$ y convergen a él por C06. No se necesita un límite perforado ni una hipótesis sobre $f$.

## 14.13. El infractor evita solo el centro

[]{#MA-EX-ANM-01-014-013}

[]{#MA-SOL-ANM-01-014-013}

La negación es $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D$ con $|x-a|<\delta$ y $|f(x)-f(a)|\ge\varepsilon_0$. Si $x=a$, el segundo error sería cero, contradicción. En el criterio de límite la exclusión del centro es una hipótesis explícita del dominio de control; aquí la propia infracción la implica automáticamente porque el destino es $f(a)$.

## 14.14. Reconstruir la recíproca enumerada

[]{#MA-EX-ANM-01-014-014}

[]{#MA-SOL-ANM-01-014-014}

Si no hubiese continuidad, existen $\varepsilon_0$ y conjuntos $E_n$ no vacíos con $|x-a|<1/(n+1)$ y error al menos $\varepsilon_0$. Por sobreyectividad, $I_n=\{k:e(k)\in E_n\}$ es no vacío. El mínimo natural $k_n$ es único y define $x_n=e(k_n)$. Entonces $x_n\to a$ pero los errores de imagen nunca son menores que $\varepsilon_0$, contradicción. El mínimo vive en los índices; un subconjunto real no vacío puede carecer de mínimo.

## 14.15. Auditar una prueba sin selector

[]{#MA-EX-ANM-01-014-015}

[]{#MA-SOL-ANM-01-014-015}

El borrador pasa de existencias individuales a una función de selección sin justificarla. Puede repararse declarando una enumeración sobreyectiva de $D$ y usando mínimos de índices, o presentando el teorema general como condicional a $\mathrm{CC}(\mathbb R)$ aplicada a los $E_n$. La dirección de continuidad a rutas ya era incondicional y no necesita reparación. No afirmamos que el borrador demuestre la recíproca universal sin esa premisa.

## 14.16. Un abierto que contiene un extremo

[]{#MA-EX-ANM-01-014-016}

[]{#MA-SOL-ANM-01-014-016}

[]{#MA-SEC-ANM-01-014-004}

La preimagen es $[0,1)$. En el ambiente $[0,2]$ es la intersección con el abierto $(-1,1)$, luego es abierta relativa. Por bolas: para $a\in[0,1)$, radio $(1-a)/2$ mantiene cualquier entrada del dominio menor que uno. En la recta, toda bola de cero contiene negativos fuera del conjunto, así que no es abierta absoluta. La inclusión es continua con radio $\varepsilon$ y no contradice el criterio correcto.

## 14.17. La preimagen tiene dos piezas

[]{#MA-EX-ANM-01-014-017}

[]{#MA-SOL-ANM-01-014-017}

La condición $1<x^2<4$ equivale a $1<|x|<2$, por lo que la preimagen es $(-2,-1)\cup(1,2)$, unión de dos intervalos abiertos. Es abierta por C04. No existe una inversa funcional del cuadrado sobre toda la recta porque no es inyectivo; calcular esta preimagen sólo resuelve pertenencia a un intervalo de salida.

**Retorno visual.** Véase [C14-F03](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 14.18. Basta una base de intervalos

[]{#MA-EX-ANM-01-014-018}

[]{#MA-SOL-ANM-01-014-018}

Fijemos $a\in D$ y $\varepsilon>0$. El intervalo $(f(a)-\varepsilon,f(a)+\varepsilon)$ es una bola abierta y su preimagen abierta contiene $a$. El criterio por bolas da $\delta>0$ con $D\cap B(a,\delta)$ dentro de ella. Todas esas entradas tienen error menor que $\varepsilon$, que es continuidad. No es necesario seleccionar intervalos ni radios para todos los puntos a la vez.

## 14.19. Ceros cerrados en el ambiente correcto

[]{#MA-EX-ANM-01-014-019}

[]{#MA-SOL-ANM-01-014-019}

El conjunto de ceros es todo $D=(0,1)$, cerrado relativo a sí mismo porque su complemento dentro de $D$ es vacío y abierto relativo. No es cerrado absoluto: cero es adherente y falta en él, por ejemplo mediante la ruta $1/(n+2)$. El criterio afirma cerradura en el dominio, no en otro ambiente.

## 14.20. Codominio restringido y preimágenes

[]{#MA-EX-ANM-01-014-020}

[]{#MA-SOL-ANM-01-014-020}

Para $x\in D$, el tipo garantiza $f(x)\in E$, por lo que $f(x)\in E\cap U$ equivale a $f(x)\in U$. Esto prueba la igualdad. Si hay continuidad, el criterio absoluto da apertura de cada preimagen de $U$, por tanto de $V$. Recíprocamente, cada abierto absoluto $U$ tiene intersección $E\cap U$ abierta relativa y con la misma preimagen, así que el criterio absoluto vuelve a aplicar. Los ambientes cambian, las distancias reales no.

## 14.21. Producto con un valor central nulo

[]{#MA-EX-ANM-01-014-021}

[]{#MA-SOL-ANM-01-014-021}

[]{#MA-SEC-ANM-01-014-005}

Continuidad de $g$ para tolerancia uno da $r>0$ con $|g(x)|<B:=|g(a)|+1$ en la bola relativa. Dado $\varepsilon>0$, continuidad de $f$ da $\delta_f$ con $|f(x)|<\varepsilon/B$. En radio $\min(r,\delta_f)$, $|f(x)g(x)-f(a)g(a)|=|f(x)g(x)|<\varepsilon$. La positividad de $B$ evita dividir por un valor central nulo.

## 14.22. Cociente con dominio declarado

[]{#MA-EX-ANM-01-014-022}

[]{#MA-SOL-ANM-01-014-022}

El dominio es $\mathbb R\setminus\{2\}$. En cada punto de él, ambos polinomios son continuos y el denominador central es no nulo, por lo que el teorema de cocientes da continuidad relativa. En dos no hay evaluación de la expresión, así que no preguntamos por su continuidad como función dada. Un límite o una posible extensión sería una pregunta distinta; la regla de cocientes no la autoriza cuando el denominador límite es cero.

## 14.23. Composición que toca el centro

[]{#MA-EX-ANM-01-014-023}

[]{#MA-SOL-ANM-01-014-023}

La exterior $g(y)=|y|$ en cero responde al desafío $\varepsilon$ con $\eta=\varepsilon$, por el error $|y|$. La interior $f(x)=2x$ responde al desafío $\eta$ con $\delta=\eta/2$. Así $|x|<\delta$ implica $|2x|<\eta$ y $||2x|-0|<\varepsilon$. Si $x=0$, el error es cero y ambas etapas siguen siendo válidas.

**Retorno visual.** Véase [C14-F04](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 14.24. Composición sólo donde existe

[]{#MA-EX-ANM-01-014-024}

[]{#MA-SOL-ANM-01-014-024}

$T=\{x:x^2\ne1\}=\mathbb R\setminus\{-1,1\}$. La interior es continua en cada real y la exterior en cada punto de $E$ por recíproco de una afín no nula. En cada $a\in T$, $f(a)\in E$, así que el teorema de composición da continuidad relativa a $T$. La expresión resultante es $1/(x^2-1)$, sin evaluación en los dos puntos excluidos.

## 14.25. Composición por regiones de salida

[]{#MA-EX-ANM-01-014-025}

[]{#MA-SOL-ANM-01-014-025}

Para $V$ abierto absoluto, $g^{-1}[V]$ es abierto relativo a $E$. El criterio para $f:D\to E$ da que $f^{-1}[g^{-1}[V]]$ es abierto relativo a $D$. Un punto $x$ pertenece a ese conjunto si y sólo si $g(f(x))\in V$, así que coincide con $(g\circ f)^{-1}[V]$. El criterio de abiertos concluye continuidad en $D$. Ni inyectividad ni elección numerable son necesarias.

## 14.26. Imagen cerrada que pierde la cerradura

[]{#MA-EX-ANM-01-014-026}

[]{#MA-SOL-ANM-01-014-026}

[]{#MA-SEC-ANM-01-014-006}

El denominador es un polinomio continuo y siempre positivo, de modo que el recíproco es continuo. Sus valores satisfacen $0<r(x)\le1$. Para cada $y\in(0,1]$, la entrada $\sqrt{1/y-1}$ produce $y$, luego la imagen es exactamente ese intervalo. Cero está fuera y toda bola suya contiene un punto del intervalo, por ejemplo $\min(\varepsilon/2,1/2)>0$ si el radio es $\varepsilon$. La imagen no es cerrada aunque el dominio real lo sea.

## 14.27. Auditar la biyección y su inversa

[]{#MA-EX-ANM-01-014-027}

[]{#MA-SOL-ANM-01-014-027}

Las piezas $[0,1)$ y $[2,3]$ se envían afínmente a $[0,1)$ y $[1,2]$, disjuntas y con unión $[0,2]$. Cada regla es inyectiva, y las imágenes disjuntas prueban inyectividad global; la unión prueba sobreyectividad. Un radio $\min(1/2,\varepsilon)$ evita la otra pieza y controla error $|x-a|$. La inversa vale $y$ por debajo de uno y $y+1$ desde uno. Para cada radio, $y=1-\min(\delta/2,1/2)$ tiene distancia de entrada menor que $\delta$ pero distancia de salida a $h(1)=2$ mayor que uno.

**Retorno visual.** Véase [C14-F05](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 14.28. La identidad de un transporte reversible

[]{#MA-EX-ANM-01-014-028}

[]{#MA-SOL-ANM-01-014-028}

Escriba $h=f^{-1}:E\to D$. Para $U\subseteq D$, $y\in h^{-1}[U]$ equivale a que la entrada única $h(y)$ esté en $U$, lo que equivale a $y\in f[U]$. Por tanto $h^{-1}[U]=f[U]$. El criterio de continuidad de $h$ con abiertos relativos de su codominio $D$ es exactamente la propiedad de imágenes enunciada. Ambas implicaciones se siguen de esa igualdad y del criterio, sin asumir continuidad de $f$.

## 14.29. Una afín es un homeomorfismo

[]{#MA-EX-ANM-01-014-029}

[]{#MA-SOL-ANM-01-014-029}

Es inyectiva porque $m(x-z)=0$ implica $x=z$, y sobreyectiva porque para cada $y$ la entrada $(y-c)/m$ produce $y$. Su inversa es esa regla afín. El error directo es $|m||x-a|$, con radio $\varepsilon/|m|$. El inverso es $|y-b|/|m|$, con radio $|m|\varepsilon$. Las pruebas funcionan en cada centro y legitiman el transporte reversible.

## 14.30. Controles inversos sin intervalos compactos

[]{#MA-EX-ANM-01-014-030}

[]{#MA-SOL-ANM-01-014-030}

Si $F\subseteq D$ es cerrado relativo, $D\setminus F$ es abierto relativo. La aplicación abierta da $f[D\setminus F]$ abierto relativo a $E$. Por bijectividad, $f[D\setminus F]=E\setminus f[F]$: una salida tiene única entrada y ésta está fuera de $F$ exactamente cuando la salida no está en $f[F]$. Por tanto $f[F]$ es cerrado relativo. La bijectividad es decisiva para la identidad de complementos de imágenes.

## 14.31. Pegar un valor absoluto desplazado

[]{#MA-EX-ANM-01-014-031}

[]{#MA-SOL-ANM-01-014-031}

[]{#MA-SEC-ANM-01-014-007}

Las piezas $(-\infty,2]$ y $[2,\infty)$ son cerradas, cubren la recta y las reglas afines son continuas en ellas. Ambas dan cero en la intersección $\{2\}$, por lo que la función está bien definida. El pegado finito prueba continuidad global; coincide con $|x-2|$, pero no es necesario usar esa identidad para aplicar el mecanismo.

**Retorno visual.** Véase [C14-F06](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 14.32. Localizar con una cobertura abierta

[]{#MA-EX-ANM-01-014-032}

[]{#MA-SOL-ANM-01-014-032}

Fijamos $a\in D$ y $\varepsilon>0$. Alguna pieza abierta relativa $U$ contiene $a$. Hay $r>0$ con $D\cap B(a,r)\subseteq U$, y la continuidad de la restricción da $\delta_U$. El mínimo de ambos radios controla toda entrada del dominio: primero la coloca en $U$ y después limita el error. La prueba sólo necesita una pieza para el punto fijado, no un mínimo de una familia infinita.

## 14.33. El acuerdo sin cierre no basta

[]{#MA-EX-ANM-01-014-033}

[]{#MA-SOL-ANM-01-014-033}

Use piezas $D_1=(-\infty,0)$ y $D_2=[0,\infty)$, con reglas constantes cero y uno. Son continuas en sus respectivos dominios y coinciden en la intersección vacía. La función global tiene valor uno en cero, pero $-\delta/2$ produce cero en cada radio; tolerancia $1/2$ refuta continuidad. $D_1$ no es cerrado relativo al dominio real, por lo que no puede excluirse cerca de un centro que no le pertenece.

## 14.34. Una cobertura cerrada infinita falla

[]{#MA-EX-ANM-01-014-034}

[]{#MA-SOL-ANM-01-014-034}

Cada singleton es cerrado en la recta: desde cualquier punto distinto, la mitad de la distancia evita el singleton. Por intersección también es cerrado relativo a $D$. Las piezas cubren $D$ y cada restricción es constante, por tanto continua. En cero, para cualquier radio $\delta>0$, arquimedianidad da un entero positivo $n>1/\delta$; entonces $1/n<\delta$ y el error es uno. La tolerancia $1/2$ refuta continuidad. La cobertura es infinita; los radios que excluyen cada pieza distinta de cero no tienen una escala común positiva.

## 14.35. Conservar un signo cerca del centro

[]{#MA-EX-ANM-01-014-035}

[]{#MA-SOL-ANM-01-014-035}

Use tolerancia $|f(a)|/2=-f(a)/2>0$. En el radio de continuidad, $f(x)<f(a)+|f(a)|/2=f(a)/2<0$. Si $f$ es continua en todo $D$, el conjunto de valores negativos de entrada es $f^{-1}[(-\infty,0)]$ y es abierto relativo por el criterio. No se deduce existencia de un cero en otro lugar: sólo apertura y estabilidad local.

## 14.36. Un certificado directo del cuadrado

[]{#MA-EX-ANM-01-014-036}

[]{#MA-SOL-ANM-01-014-036}

[]{#MA-SEC-ANM-01-014-008}

Para $|x-a|<1$, $|x+a|<1+2|a|=:K$. Por tanto $|x^2-a^2|\le K|x-a|$, donde la desigualdad no estricta incluye $x=a$. El radio $\delta=\min(1,\varepsilon/K)$ es positivo porque $K\ge1$. Si $|x-a|<\delta$, el error es $\le K|x-a|<K\delta\le\varepsilon$. No se escribió $0<0$ en el caso central.

## 14.37. La raíz en un extremo del dominio

[]{#MA-EX-ANM-01-014-037}

[]{#MA-SOL-ANM-01-014-037}

El valor central es cero. Dado $\varepsilon>0$, tomamos $\delta=\varepsilon^2$. Para $x\in[0,\infty)$ con $|x|<\delta$, no negatividad y orden de raíces dan $|\sqrt{x}-0|=\sqrt{x}<\varepsilon$. Los negativos no pertenecen al dominio real de la función y no son entradas del cuantificador universal. La prueba incluye cero, cuyo error es cero.

**Retorno visual.** Véase [C14-F07](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 14.38. Continuidad sin barrera lineal

[]{#MA-EX-ANM-01-014-038}

[]{#MA-SOL-ANM-01-014-038}

Dados $K\ge0$ y $r>0$, sea $x=\min(r/2,1/[4(K+1)^2])>0$. Entonces $x<r$ y $1/\sqrt{x}\ge2(K+1)>K$. Multiplicar por $x>0$ da $\sqrt{x}>Kx$, infracción de la cota. Continuidad ya tiene certificado $\varepsilon^2$, que no necesita esa barrera lineal. La ausencia de un certificado suficiente no significa ausencia de continuidad.

## 14.39. Invertir el cuadrado lejos de cero

[]{#MA-EX-ANM-01-014-039}

[]{#MA-SOL-ANM-01-014-039}

Para $x,z\ge m$, $|x^2-z^2|=(x+z)|x-z|\ge2m|x-z|$. En particular igualdad de cuadrados implica igualdad de entradas. Cada $y\ge m^2$ tiene entrada $\sqrt{y}\ge m$, lo que prueba sobreyectividad. La inversa es la raíz restringida. Para un centro $b=q(a)$ y un desafío $\varepsilon$, $|y-b|<2m\varepsilon$ implica $|q^{-1}(y)-a|\le|y-b|/(2m)<\varepsilon$. El alcance global en $x,z$ evita entradas lejanas con salidas próximas.

## 14.40. El control inferior local no autoriza la inversa

[]{#MA-EX-ANM-01-014-040}

[]{#MA-SOL-ANM-01-014-040}

Use $D=[0,1)\cup[2,3]$, $f(x)=x$ en la primera pieza y $f(x)=x-1$ en la segunda, con $a=2$. El centro no es aislado, pues $2+t\in D$ para $0<t<1$ arbitrariamente pequeño. En radio $1/2$, todas las entradas del dominio son de la segunda pieza y $|f(x)-f(2)|=|x-2|$, así que vale la cota inferior. Pero la inversa en $f(2)=1$ toma valor dos, mientras $y_n=1-1/(n+2)$ tiende a uno y su inversa es $y_n$, que tiende a uno. No puede converger también a dos. La cota local exige antes saber que la entrada inversa está cerca de dos; precisamente eso era lo que se quería probar. Las salidas cercanas que proceden de la otra pieza quedan fuera de su alcance.

**Retorno visual.** Véase [C14-F05](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html#fig-anm-c14-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 14](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad.html) · [Ejercicios](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-14-continuidad-transportar-proximidad-microcontroles.html)
