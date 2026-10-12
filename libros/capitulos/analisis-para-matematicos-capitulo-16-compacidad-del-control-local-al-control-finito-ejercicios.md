---
content-id: MA-BCH-0267
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-016-EJERCICIOS
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
title: Ejercicios — Capítulo 16
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C16_EJERCICIOS.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)

Las soluciones completas se encuentran en ANM-C16_SOLUCIONES.md. Declara los dominios, índices y finitud de cada subcubierta. Distingue supremo de máximo, apertura relativa de apertura real y extracción de selección. No uses continuidad uniforme ni derivadas; declara CC(R) en la recíproca secuencial general.

## 16.1. Una sola cubierta no basta

[]{#MA-EX-ANM-01-016-001}

[]{#MA-SOL-ANM-01-016-001}

[]{#MA-SEC-ANM-01-016-001}

Un argumento afirma que todo subconjunto real es compacto porque $\{\mathbb R\}$ es una cubierta finita. Explica el cambio ilegítimo de cuantificadores y refútalo con una cubierta de $\mathbb R$.

## 16.2. Subcubierta concreta

[]{#MA-EX-ANM-01-016-002}

[]{#MA-SOL-ANM-01-016-002}

Considera $K=[0,1]$ y los abiertos $U_1=(-1/4,2/5)$, $U_2=(3/10,4/5)$, $U_3=(7/10,5/4)$, $U_4=(1/5,3/5)$. Identifica una subcubierta de tres miembros y muestra que quitar cualquiera de esos tres deja algún punto sin cubrir dentro de esa subfamilia.

## 16.3. Uniones finitas desde la definición

[]{#MA-EX-ANM-01-016-003}

[]{#MA-SOL-ANM-01-016-003}

Prueba desde cubiertas que una unión finita de compactos reales es compacta, incluyendo la unión vacía. No invoques Heine–Borel.

## 16.4. El mínimo positivo tiene una hipótesis

[]{#MA-EX-ANM-01-016-004}

[]{#MA-SOL-ANM-01-016-004}

Demuestra que una familia finita no vacía de radios positivos tiene mínimo positivo. Refuta la conclusión análoga para una familia infinita.

## 16.5. Una unión infinita que escapa

[]{#MA-EX-ANM-01-016-005}

[]{#MA-SOL-ANM-01-016-005}

Sabiendo que cada segmento $[-n,n]$ será compacto por R2, explica por qué la unión de esos segmentos para $n\in\mathbb N$ refuta que toda unión de compactos sea compacta. Exhibe la cubierta responsable.

## 16.6. Registrar cobertura finita

[]{#MA-EX-ANM-01-016-006}

[]{#MA-SOL-ANM-01-016-006}

[]{#MA-SEC-ANM-01-016-002}

Para una cubierta arbitraria de $[a,b]$, $a\le b$, define $S$ como en R2 y justifica $a\in S$, existencia de su supremo y pertenencia del supremo al segmento.

## 16.7. Prolongar con un solo abierto

[]{#MA-EX-ANM-01-016-007}

[]{#MA-SOL-ANM-01-016-007}

Si $c=\sup S$, $(c-r,c+r)\subseteq U_{i_c}$ y $t\in S$ satisface $c-r/2<t\le c$, prueba que $d=\min(b,c+r/2)$ pertenece a $S$. Identifica qué índices cubren cada tramo.

## 16.8. El extremo omitido de una prueba

[]{#MA-EX-ANM-01-016-008}

[]{#MA-SOL-ANM-01-016-008}

Una prueba concluye $\sup S=b$ y afirma «por tanto $b\in S$». Refuta ese paso lógico y completa el argumento correcto de R2 para obtener la subcubierta de todo el segmento.

## 16.9. No elegir una subcubierta por segmento

[]{#MA-EX-ANM-01-016-009}

[]{#MA-SOL-ANM-01-016-009}

Explica por qué definir $S$ mediante «existe una subcubierta finita de $[a,x]$» no obliga a construir una función $x\mapsto J_x$. Enumera los testigos concretos necesarios en R2.

## 16.10. Cobertura del intervalo abierto frente al cerrado

[]{#MA-EX-ANM-01-016-010}

[]{#MA-SOL-ANM-01-016-010}

¿Puede la familia $U_n=(1/(n+2),2)$ cubrir $[0,1]$? Compara con su acción sobre $(0,1)$ y explica por qué no contradice R2.

## 16.11. Cubrir el complemento completo

[]{#MA-EX-ANM-01-016-011}

[]{#MA-SOL-ANM-01-016-011}

[]{#MA-SEC-ANM-01-016-003}

Para heredar compacidad de $A=K\cap F$, una prueba añade sólo $V=(M-1,M+1)\cap(\mathbb R\setminus F)$ cuando $K=[-M,M]$. Muestra con $M=2$, $F=\{0\}$ y una cubierta de $A$ que la familia ampliada puede no cubrir $K$. Repara el abierto añadido.

## 16.12. Cerrar dos piezas dentro de un segmento

[]{#MA-EX-ANM-01-016-012}

[]{#MA-SOL-ANM-01-016-012}

Prueba compacidad de $A=[-2,-1]\cup[1,2]$ como cerrado relativo de $K=[-2,2]$, sin usar todavía Heine–Borel. Describe el abierto añadido en la prueba de herencia.

## 16.13. Etiquetas y abiertos repetidos

[]{#MA-EX-ANM-01-016-013}

[]{#MA-SOL-ANM-01-016-013}

Desarrolla el sistema de índices al añadir un abierto $V$ a una cubierta $(U_i)_{i\in I}$ y al retirar ese miembro tras aplicar compacidad. Permite que $V$ coincida como conjunto con algún $U_i$.

## 16.14. Un subconjunto que pierde compacidad

[]{#MA-EX-ANM-01-016-014}

[]{#MA-SOL-ANM-01-016-014}

Prueba mediante una cubierta que $(0,1)$ no es compacto, aunque esté dentro del compacto $[0,1]$. Trata las subfamilias vacías y no vacías.

## 16.15. Intersección con un cerrado

[]{#MA-EX-ANM-01-016-015}

[]{#MA-SOL-ANM-01-016-015}

Prueba que $K\cap F$ es compacto cuando $K$ lo es y $F$ es cerrado real. Deduce que la intersección de toda familia no vacía de compactos reales es compacta, una vez disponible R4. Separa el caso de familia vacía.

## 16.16. Acotación desde una cubierta creciente

[]{#MA-EX-ANM-01-016-016}

[]{#MA-SOL-ANM-01-016-016}

[]{#MA-SEC-ANM-01-016-004}

Prueba que todo compacto real es acotado usando sólo la cubierta $U_n=(-(n+1),n+1)$. Incluye el vacío.

## 16.17. Un radio exterior por índices finitos

[]{#MA-EX-ANM-01-016-017}

[]{#MA-SOL-ANM-01-016-017}

Fija $p\notin K$, con $K$ compacto no vacío. Usando $V_n=\{x:|x-p|>1/(n+1)\}$, demuestra que alguna bola positiva alrededor de $p$ evita $K$.

## 16.18. Reconocer cinco dominios

[]{#MA-EX-ANM-01-016-018}

[]{#MA-SOL-ANM-01-016-018}

Usa Heine–Borel para decidir compacidad de $[0,1]$, $(0,1]$, $\mathbb R$, $\{-1,1\}$ y $\mathbb Q\cap[0,1]$. Justifica el fallo cuando corresponda.

## 16.19. La cola y el prefijo

[]{#MA-EX-ANM-01-016-019}

[]{#MA-SOL-ANM-01-016-019}

Prueba cerradura y compacidad de $K=\{0\}\cup\{1/(n+1):n\in\mathbb N\}$ sin usar la recíproca secuencial. Para un exterior positivo, construye el radio desde una cola y un prefijo finito.

## 16.20. Dos propiedades distintas

[]{#MA-EX-ANM-01-016-020}

[]{#MA-SOL-ANM-01-016-020}

Da un compacto real no conexo y un conexo real no compacto. Justifica ambas propiedades con los resultados correspondientes.

## 16.21. Acotar la ruta y retener su límite

[]{#MA-EX-ANM-01-016-021}

[]{#MA-SOL-ANM-01-016-021}

[]{#MA-SEC-ANM-01-016-005}

Demuestra que un compacto real es secuencialmente compacto usando Bolzano–Weierstrass de C08. Identifica el paso que coloca el límite en el conjunto.

## 16.22. Un límite exterior para todas las extracciones

[]{#MA-EX-ANM-01-016-022}

[]{#MA-SOL-ANM-01-016-022}

Prueba que $(0,1]$ no es secuencialmente compacto mediante una sucesión concreta. No basta decir que esa sucesión converge fuera: debes tratar todas sus subsucesiones.

## 16.23. Una fabricación que necesita permiso

[]{#MA-EX-ANM-01-016-023}

[]{#MA-SOL-ANM-01-016-023}

Un argumento dice: «Si $K$ no es acotado, para cada $n$ hay $x_n\in K$ con $|x_n|>n$; luego tenemos una sucesión». Distingue las afirmaciones y completa la contradicción bajo CC(R) explícita.

## 16.24. La ruta hacia un punto omitido

[]{#MA-EX-ANM-01-016-024}

[]{#MA-SOL-ANM-01-016-024}

Bajo CC(R), prueba que un secuencialmente compacto es cerrado. Declara la familia seleccionada y todos los límites utilizados.

## 16.25. Una enumeración dada determina testigos

[]{#MA-EX-ANM-01-016-025}

[]{#MA-SOL-ANM-01-016-025}

Sea $K\ne\varnothing$ secuencialmente compacto y sea $e:\mathbb N\to K$ una sobreyección dada. Prueba que $K$ es cerrado y acotado, y por ello compacto, sin invocar CC(R).

## 16.26. Levantar un abierto relativo

[]{#MA-EX-ANM-01-016-026}

[]{#MA-SOL-ANM-01-016-026}

[]{#MA-SEC-ANM-01-016-006}

Sea $K$ cerrado real y $A$ abierto relativo a $K$. Prueba que $W=(\mathbb R\setminus K)\cup A$ es abierto real y que $K\cap W=A$. Explica por qué esta fórmula sirve para una familia sin elegir ambientes simultáneamente.

## 16.27. Devolver los mismos índices

[]{#MA-EX-ANM-01-016-027}

[]{#MA-SOL-ANM-01-016-027}

En R6, una subfamilia finita $W_j$ cubre $K$. Prueba que los mismos índices $j$ cubren $f[K]$ con los $V_j$ originales. No supongas que $f$ tenga inversa.

## 16.28. Imagen compacta con un hueco

[]{#MA-EX-ANM-01-016-028}

[]{#MA-SOL-ANM-01-016-028}

Para $K=[-2,-1]\cup[1,2]$ y $q(x)=x^2$, calcula $q[K]$ y una cubierta de esa imagen con dos miembros abiertos. Describe las preimágenes relativas y sus levantamientos canónicos.

## 16.29. Una preimagen demasiado grande

[]{#MA-EX-ANM-01-016-029}

[]{#MA-SOL-ANM-01-016-029}

Da una continua cuya imagen sea compacta y cuyo dominio no lo sea. Usa el mismo ejemplo para refutar compacidad universal de preimágenes de compactos.

## 16.30. El ambiente importa antes de aplicar compacidad

[]{#MA-EX-ANM-01-016-030}

[]{#MA-SOL-ANM-01-016-030}

Una prueba afirma que las preimágenes $A_i\subseteq K$ de abiertos de salida son abiertos reales y aplica directamente la definición ambiental de compacidad. Da un ejemplo de preimagen no abierta real y repara la prueba.

## 16.31. Un supremo que se alcanza

[]{#MA-EX-ANM-01-016-031}

[]{#MA-SOL-ANM-01-016-031}

[]{#MA-SEC-ANM-01-016-007}

Prueba que un compacto no vacío $H\subseteq\mathbb R$ contiene su supremo y su ínfimo. No construyas una sucesión de puntos próximos a esos valores.

## 16.32. Extremos que no son ambos extremos de entrada

[]{#MA-EX-ANM-01-016-032}

[]{#MA-SOL-ANM-01-016-032}

Encuentra mínimo, máximo y todos los argumentos que los alcanzan para $f(x)=(x-1)^2$ en $[0,3]$. Justifica con desigualdades, sin derivadas.

## 16.33. Un compacto sin continuidad suficiente

[]{#MA-EX-ANM-01-016-033}

[]{#MA-SOL-ANM-01-016-033}

En $[0,1]$, define $u(x)=x$ si $x<1$ y $u(1)=0$. Calcula su imagen, decide si alcanza máximo y refuta continuidad en $1$ con un testigo para cada radio.

## 16.34. No vacuidad y no unicidad

[]{#MA-EX-ANM-01-016-034}

[]{#MA-SOL-ANM-01-016-034}

Explica por qué Weierstrass requiere dominio no vacío pero no garantiza unicidad de los extremizadores. Da un ejemplo compacto no vacío con varios mínimos y máximos.

## 16.35. Dos teoremas para describir la imagen

[]{#MA-EX-ANM-01-016-035}

[]{#MA-SOL-ANM-01-016-035}

Sea $a\le b$ y $f:[a,b]\to\mathbb R$ continua. Prueba que su imagen es $[m,M]$, identificando qué aporta C15 y qué aporta C16. Refuta que se puedan tomar siempre $m=f(a)$ y $M=f(b)$.

## 16.36. Positividad con margen

[]{#MA-EX-ANM-01-016-036}

[]{#MA-SOL-ANM-01-016-036}

[]{#MA-SEC-ANM-01-016-008}

En $K=[-2,-1]\cup[1,2]$, considera $f(x)=x^2$ y $g(x)=x+1$. Encuentra un margen positivo de $|f|$ y cotas de $|1/f|$ y $|g/f|$ válidas en todo $K$.

## 16.37. Punto más cercano y dos candidatos

[]{#MA-EX-ANM-01-016-037}

[]{#MA-SOL-ANM-01-016-037}

Prueba que cualquier compacto no vacío tiene un punto más próximo a un real fijado $p$. Para $K=\{-1,1\}$ y $p=0$, calcula todos los minimizadores y el margen.

## 16.38. Una fibra compacta que se divide

[]{#MA-EX-ANM-01-016-038}

[]{#MA-SOL-ANM-01-016-038}

Para $q(x)=x^2$ en $K=[-2,2]$, calcula la fibra de $1$ y prueba su compacidad y su desconexión. Generaliza la compacidad a la preimagen de cualquier cerrado real por una continua en compacto.

## 16.39. Inversa por transporte de cerrados

[]{#MA-EX-ANM-01-016-039}

[]{#MA-SOL-ANM-01-016-039}

Sea $K$ compacto y $f:K\to\mathbb R$ continua e inyectiva. Demuestra que la inversa $h:f[K]\to K$ es continua mediante preimágenes de cerrados relativos. Trata el vacío.

## 16.40. Homeomorfismo compacto sin monotonía global

[]{#MA-EX-ANM-01-016-040}

[]{#MA-SOL-ANM-01-016-040}

Sea $K=[0,1]\cup[2,3]$ y define $f(x)=x$ en la primera pieza, $f(x)=x-4$ en la segunda. Calcula la imagen, prueba inyectividad y continuidad, decide si es monótona en todo $K$ y justifica continuidad de su inversa.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 16](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito.html) · [Ejercicios](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-16-compacidad-del-control-local-al-control-finito-microcontroles.html)
