---
content-id: MA-BCH-0229
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-006-MICROCONTROLES
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
title: Soluciones de microcontroles — Capítulo 6
date-modified: '2026-10-14'
provenance:
  type: original
  sources:
  - ANM-C06_MICROCONTROLES_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 6](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) · [Ejercicios](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-microcontroles.html)

Las soluciones corresponden, en orden, a las ocho preguntas de «Antes de seguir» de cada sección. Los enunciados permanecen en el manuscrito. Se conserva $\mathbb N=\{0,1,2,\ldots\}$.

## §6.1

### 001. Pregunta 1

[]{#MA-MIC-ANM-01-006-001}

[]{#MA-MSOL-ANM-01-006-001}

[]{#MA-SEC-ANM-01-006-001}

$a$ es una función $\mathbb N\to\mathbb R$; $n\in\mathbb N$ es un índice y $a_n\in\mathbb R$ su término. El candidato $A\in\mathbb R$ es otro número real, $\varepsilon>0$ una tolerancia real y $N\in\mathbb N$ un umbral. Primero se fijan la sucesión $a$ y el candidato $A$. Después se recibe $\varepsilon$, se elige $N$ y se toma un índice arbitrario $n\ge N$.

### 002. Pregunta 2

[]{#MA-MIC-ANM-01-006-002}

[]{#MA-MSOL-ANM-01-006-002}

La sucesión $a$ converge al candidato $A$ si, para cada tolerancia real positiva, existe un umbral natural desde el que todos los términos tienen distancia a $A$ estrictamente menor que esa tolerancia. Simbólicamente,

$$
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N:\quad n\ge N\Longrightarrow |a_n-A|<\varepsilon.
$$

La sucesión y el candidato están fijados antes de esa cuantificación.

### 003. Pregunta 3

[]{#MA-MIC-ANM-01-006-003}

[]{#MA-MSOL-ANM-01-006-003}

En $B(0,2)$ sirve $N=0$, pues los dos valores posibles, 0 y 1, tienen módulo menor que 2. En $B(0,1/2)$ no sirve ningún umbral: para cualquier $N$, el índice impar $2N+1\ge N$ tiene valor 1 y error $1\ge1/2$. Por tanto, $r$ no converge al candidato 0. Esta comprobación, por sí sola, refuta ese candidato; no formula todavía una refutación de todos los reales.

### 004. Pregunta 4

[]{#MA-MIC-ANM-01-006-004}

[]{#MA-MSOL-ANM-01-006-004}

Si $n\ge K\ge N$, entonces $n\ge N$ y se aplica la estimación acreditada por el corte original. Así $K$ controla la misma tolerancia en toda su cola. La definición exige algún testigo natural suficiente, no el menor. La posibilidad de aumentar el umbral permite sincronizar controles sin tener que minimizar cada corte.

### 005. Pregunta 5

[]{#MA-MIC-ANM-01-006-005}

[]{#MA-MSOL-ANM-01-006-005}

El valor 2 es interior, con error 0. Los valores $5/3$ y $7/3$ están en la frontera de $B(2,1/3)$, porque sus errores respecto de 2 son exactamente $1/3$. Sólo el valor 2 cumple el error estricto. Estar en el intervalo cerrado correspondiente no equivale a estar en la bola abierta.

### 006. Pregunta 6

[]{#MA-MIC-ANM-01-006-006}

[]{#MA-MSOL-ANM-01-006-006}

Con la convención de índice inicial 0, tenemos $b_0=9$, $b_1=-4$ y $b_n=1$ desde $n=2$. Para cualquier $\varepsilon>0$, elegimos $N=2$. Si $n\ge N$, entonces $|b_n-1|=0<\varepsilon$. Los dos términos anteriores no pertenecen a la cola que debe controlarse; sus errores no invalidan el testigo.

### 007. Pregunta 7

[]{#MA-MIC-ANM-01-006-007}

[]{#MA-MSOL-ANM-01-006-007}

La tabla sólo muestra un número finito de índices, mientras que una captura exige controlar todos los índices posteriores al corte. Además, sólo comprueba las tolerancias que aparecen en ella, mientras que la definición exige responder a cualquier real positivo. Una fórmula de error y una estimación general pueden cerrar ambas obligaciones; la inspección de esas filas no las cierra.

### 008. Pregunta 8

[]{#MA-MIC-ANM-01-006-008}

[]{#MA-MSOL-ANM-01-006-008}

Si $a_n\to A$ y $U$ es una vecindad de $A$, existe $r>0$ con $B(A,r)\subseteq U$. La convergencia captura una cola en esa bola, y la inclusión la sitúa en $U$. Recíprocamente, si cada vecindad captura una cola, para una tolerancia arbitraria $\varepsilon>0$ usamos la vecindad concreta $U=B(A,\varepsilon)$. Su captura significa $|a_n-A|<\varepsilon$ eventualmente, que recupera la definición.

## §6.2

### 009. Pregunta 1

[]{#MA-MIC-ANM-01-006-009}

[]{#MA-MSOL-ANM-01-006-009}

[]{#MA-SEC-ANM-01-006-002}

Se fijan $a$ y $A$, se recibe $\varepsilon>0$, se construye $N\in\mathbb N$ y se verifica el error para un $n\ge N$ arbitrario. El umbral puede depender de $a,A,\varepsilon$, pero no del índice posterior que recorre la cola. Elegirlo después de conocer ese índice cambiaría la obligación: no se habría construido un corte común para todos los términos tardíos.

### 010. Pregunta 2

[]{#MA-MIC-ANM-01-006-010}

[]{#MA-MSOL-ANM-01-006-010}

Si un mismo $N$ funciona para todas las tolerancias y algún $n\ge N$ tiene error $d=|a_n-A|>0$, elegimos $\varepsilon=d/2$. La captura exigiría $d<d/2$, contradicción. Luego $a_n=A$ para todos los índices desde $N$. A la inversa, si la sucesión es constante de valor $A$ desde un corte, el error cero hace que ese corte sirva para cualquier tolerancia positiva.

### 011. Pregunta 3

[]{#MA-MIC-ANM-01-006-011}

[]{#MA-MSOL-ANM-01-006-011}

Las cantidades $\varepsilon_n=|a_n-A|+1$ se adaptan al error de cada término y garantizan una desigualdad automática. No responden a una tolerancia arbitraria recibida previamente ni producen un corte que la controle. Por ejemplo, para $a_n=1$ y candidato 0 esas elecciones siempre dan 2, pero la tolerancia $1/2$ no captura ningún término. El procedimiento elude las exigencias pequeñas en lugar de acreditarlas.

### 012. Pregunta 4

[]{#MA-MIC-ANM-01-006-012}

[]{#MA-MSOL-ANM-01-006-012}

Tras recibir $\varepsilon$ y escoger $n$, se puede poner $N=n+1$. Entonces $n\ge N$ es falso y la implicación resulta verdadera, cualquiera que sea el error. Se perdió el control de todos los índices posteriores a un único umbral: la elección depende del término que se quería comprobar y lo deja fuera de su propia cola.

### 013. Pregunta 5

[]{#MA-MIC-ANM-01-006-013}

[]{#MA-MSOL-ANM-01-006-013}

Negar sucesivamente los cuantificadores y la implicación da

$$
\exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists n\in\mathbb N:\quad n\ge N\ \text{y}\ |a_n-A|\ge\varepsilon_0.
$$

El candidato permanece fijo. La negación de $P\Rightarrow Q$ es $P\land\neg Q$: el índice debe pertenecer a la cola y fallar la estimación. Una implicación permitiría que un índice anterior al corte acreditase vacíamente la condición, sin producir ningún infractor tardío.

### 014. Pregunta 6

[]{#MA-MIC-ANM-01-006-014}

[]{#MA-MSOL-ANM-01-006-014}

El índice $2N\ge N$ es interior: su valor es 0 y su error es cero. El índice $2N+1\ge N$ es infractor: su valor es 1 y el error es al menos $1/2$. El segundo acredita la refutación, pues impide que todos los términos de la cola estén en la ventana. La existencia simultánea de visitas interiores no elimina la infracción que sobrevive a cada corte.

### 015. Pregunta 7

[]{#MA-MIC-ANM-01-006-015}

[]{#MA-MSOL-ANM-01-006-015}

El error respecto de 1 es $|3-1|=2$ en todo índice. Fijamos $\varepsilon_0=2$ y, después de cualquier corte $N$, elegimos $n=N$. El error cae en la frontera y falla la desigualdad estricta. Esto refuta el candidato 1, pero la sucesión converge a 3: con ese candidato el error es cero desde el índice 0. Refutar un número no refuta los demás.

### 016. Pregunta 8

[]{#MA-MIC-ANM-01-006-016}

[]{#MA-MSOL-ANM-01-006-016}

Con el corte 0 y condición $n>0$, sólo se inspeccionan términos nulos, así que el error es menor que $1/2$. Con $n\ge0$ se incluye $d_0=1$ y ese corte falla; bajo nuestra convención sirve $N=1$. En general, un umbral $K$ para $n>K$ se transforma en $K+1$ para $n\ge K+1$, porque los índices son naturales. Si un umbral $N$ funciona para $n\ge N$, también sirve para $n>N$, ya que se reduce la cola exigida.

## §6.3

### 017. Pregunta 1

[]{#MA-MIC-ANM-01-006-017}

[]{#MA-MSOL-ANM-01-006-017}

[]{#MA-SEC-ANM-01-006-003}

Por la propiedad arquimediana de C03, elegimos $m\in\mathbb N$ con $m>t$. El conjunto finito $F=\{j\in\{0,\ldots,m\}:j\le t\}$ contiene 0 y tiene máximo $K$. Como $m>t$, el índice $m$ no pertenece a $F$, luego $K<m$ y $K+1\le m$. Si $K+1\le t$, su sucesor pertenecería a $F$, contradiciendo la maximalidad. Así $K\le t<K+1$.

### 018. Pregunta 2

[]{#MA-MIC-ANM-01-006-018}

[]{#MA-MSOL-ANM-01-006-018}

Si $K$ y $J$ cumplen las dos desigualdades y $K<J$, el orden natural da $K+1\le J\le t$, contradiciendo $t<K+1$. Si $J<K$, se obtiene la contradicción simétrica. Por tanto, $K=J$. Toda elección de $m>t$ que produzca esa propiedad conduce al mismo natural, pues la unicidad depende sólo de $t$ y no del conjunto auxiliar elegido.

### 019. Pregunta 3

[]{#MA-MIC-ANM-01-006-019}

[]{#MA-MSOL-ANM-01-006-019}

Para $\varepsilon=2/5$, $N=\lfloor5/2\rfloor=2$. Si $n\ge2$, entonces $n+1\ge3>5/2$ y, al invertir cantidades positivas, $|a_n|=1/(n+1)\le1/3<2/5$. El paso $n+1\ge N+1>1/\varepsilon$ vale para cualquier índice posterior, no sólo para el primero; por eso controla toda la cola.

### 020. Pregunta 4

[]{#MA-MIC-ANM-01-006-020}

[]{#MA-MSOL-ANM-01-006-020}

Con $\varepsilon=1/3$, la propuesta da $N'=2$ y el índice 2 tiene error $1/3$, de frontera, que no satisface la condición estricta. Con $\varepsilon=2$, da $N'=-1$, que no es un natural. La reparación $N=\lfloor1/\varepsilon\rfloor$ funciona para cualquier tolerancia positiva: $n\ge N$ implica $n+1\ge N+1>1/\varepsilon$, luego $1/(n+1)<\varepsilon$. Cierra tanto el dominio del testigo como la estrictitud.

### 021. Pregunta 5

[]{#MA-MIC-ANM-01-006-021}

[]{#MA-MSOL-ANM-01-006-021}

Si $\varepsilon>1$, entonces $0<1/\varepsilon<1$ y su piso es 0. La sucesión está definida en el índice 0, donde $a_0=1<\varepsilon$; además, para todos los naturales $n$, $a_n\le1<\varepsilon$. Así el corte 0 controla incluso el primer término. Cambia el umbral suficiente para esa tolerancia, no el dominio $\mathbb N$ de la sucesión.

### 022. Pregunta 6

[]{#MA-MIC-ANM-01-006-022}

[]{#MA-MSOL-ANM-01-006-022}

Para todo natural $n$, $|(-1)^n|=1$ y $n+1>0$, de modo que $|s_n-0|=1/(n+1)$. Dado $\varepsilon>0$, reutilizamos $N=\lfloor1/\varepsilon\rfloor$ y la estimación de la primera prueba: si $n\ge N$, ese error es menor que $\varepsilon$. La identidad del módulo elimina el signo alternante; la construcción del corte y su verificación permanecen iguales.

### 023. Pregunta 7

[]{#MA-MIC-ANM-01-006-023}

[]{#MA-MSOL-ANM-01-006-023}

El error es $|u_n-3|=2/(n+1)$. Para $\varepsilon>0$ elegimos $N=\lfloor2/\varepsilon\rfloor$; si $n\ge N$, $n+1\ge N+1>2/\varepsilon$, luego el error es menor que $\varepsilon$. Si el coeficiente se sustituye por 0, la sucesión es constante de valor 3 y basta $N=0$ para todas las tolerancias. No hay que aplicar el piso construido para argumentos positivos a un argumento cero.

### 024. Pregunta 8

[]{#MA-MIC-ANM-01-006-024}

[]{#MA-MSOL-ANM-01-006-024}

Fijamos un candidato arbitrario $A$. La triangular da $2\le|1-A|+|-1-A|$, así que alguno de esos errores es al menos 1. Fijamos la tolerancia 1 y elegimos el valor separado de $A$. Después de cualquier corte $N$, usamos $2N$ si ese valor es 1, o $2N+1$ si es −1; el índice elegido es tardío y su error es al menos 1. El argumento vale para cada real $A$, por lo que excluye todo límite real, no sólo el candidato 0.

## §6.4

### 025. Pregunta 1

[]{#MA-MIC-ANM-01-006-025}

[]{#MA-MSOL-ANM-01-006-025}

[]{#MA-SEC-ANM-01-006-004}

Si $a_n\to A$ y $a_n\to B$ con $A\ne B$, ponemos $d=|A-B|>0$. Las capturas con tolerancia $d/3$ proporcionan cortes $N_A,N_B$. En un mismo índice $n\ge\max\{N_A,N_B\}$, la triangular da $d\le|A-a_n|+|a_n-B|<2d/3$, contradicción. El máximo asegura que ambos controles recaigan en ese mismo término, necesario para enlazar las dos distancias. Así $A=B$.

### 026. Pregunta 2

[]{#MA-MIC-ANM-01-006-026}

[]{#MA-MSOL-ANM-01-006-026}

Con tolerancia $d/3$ para cada candidato, la estimación da $d<2d/3$, imposible para $d>0$. Si usamos $d$ para ambos, sólo obtenemos $d<2d$, que no contradice la separación. Las capturas pueden ajustarse porque la convergencia responde a todas las tolerancias; el reparto debe mantener el error total por debajo de la distancia entre los candidatos.

### 027. Pregunta 3

[]{#MA-MIC-ANM-01-006-027}

[]{#MA-MSOL-ANM-01-006-027}

Si las dos pruebas fueran válidas, la unicidad aplicada a $u$ obligaría a $B=3$. Cuando $B\ne3$, sus conclusiones no pueden acreditarse simultáneamente para la misma sucesión. El teorema garantiza a lo sumo un destino real; no garantiza que exista alguno. La sucesión $(-1)^n$, cuya ausencia de todo límite ya se demostró, muestra esa diferencia.

### 028. Pregunta 4

[]{#MA-MIC-ANM-01-006-028}

[]{#MA-MSOL-ANM-01-006-028}

Tomamos $N_b=\max\{5,9\}=9$. Para cualquier $n\ge9$, está disponible tanto la igualdad $b_n=a_n$ como la captura de $a$ respecto de $A$. Por tanto, $|b_n-A|=|a_n-A|<\varepsilon$ para la tolerancia considerada. Un corte que sólo controlase una de esas dos obligaciones no justificaría la transferencia.

### 029. Pregunta 5

[]{#MA-MIC-ANM-01-006-029}

[]{#MA-MSOL-ANM-01-006-029}

Podemos tomar $a_n=0$ y $b_n=1/(n+1)$. Ambas convergen a cero por pruebas ya disponibles y, como $b_n>0$, nunca coinciden en un índice común. Los límites son números reales iguales; las sucesiones son funciones distintas, pues sus valores difieren en cada índice. Tener igual límite no significa igualdad de funciones ni coincidencia eventual.

### 030. Pregunta 6

[]{#MA-MIC-ANM-01-006-030}

[]{#MA-MSOL-ANM-01-006-030}

Si el corte de $b$ es $K=5$, tomamos $N=3+5=8$ para $a$: para todo $n\ge8$, el natural $k=n-3\ge5$ satisface $a_n=b_k$. Si el corte de $a$ es $N=8$, sirve $K=5$ para $b$, pues $k\ge5$ implica $3+k\ge8$. También serviría el corte suficiente $K=8$. En cada dirección se transportan índices de funciones con dominio $\mathbb N$ mediante la relación $n=3+k$.

### 031. Pregunta 7

[]{#MA-MIC-ANM-01-006-031}

[]{#MA-MSOL-ANM-01-006-031}

La restricción $a|_{\mathbb N_{\ge T}}$ es una función $\mathbb N_{\ge T}\to\mathbb R$. La cola reindexada $b_k=a_{T+k}$ es una función $\mathbb N\to\mathbb R$. El conjunto $\{a_n:n\ge T\}$ es un subconjunto de $\mathbb R$ y no conserva posiciones ni repeticiones como información indexada. Nuestra definición se aplica literalmente a $b$. Si $T=0$, la restricción también tiene dominio $\mathbb N$ y coincide con $a$; para $T>0$ tiene otro dominio.

### 032. Pregunta 8

[]{#MA-MIC-ANM-01-006-032}

[]{#MA-MSOL-ANM-01-006-032}

Si $b$ coincidiese eventualmente con $a$ y convergiese a algún $B$, la equivalencia por coincidencia eventual transmitiría esa convergencia a $a$, contra la hipótesis. Por tanto, $b$ no tiene límite real. Si $b_k=a_{T+k}$ es una cola reindexada, una supuesta convergencia de $b$ se transmite a $a$ usando, para cada corte $K$ de $b$, el corte $T+K$ en los índices originales. La misma contradicción excluye su convergencia.

## §6.5

### 033. Pregunta 1

[]{#MA-MIC-ANM-01-006-033}

[]{#MA-MSOL-ANM-01-006-033}

[]{#MA-SEC-ANM-01-006-005}

La convergencia proporciona un corte $N$ para la tolerancia 1. Desde él, $|a_n|\le|A|+|a_n-A|<|A|+1$. El conjunto finito $S=\{1,|A|+1\}\cup\{|a_j|:j<N\}$ tiene máximo $M$, que cubre el prefijo y la cola, con $|a_n|\le M$ para todos los índices. Esa sola tolerancia basta para obtener una cota; la convergencia exige capturas para todas las tolerancias positivas y no se deduce de esta única banda.

### 034. Pregunta 2

[]{#MA-MIC-ANM-01-006-034}

[]{#MA-MSOL-ANM-01-006-034}

Si $N=0$, no hay índices naturales $j<N$ y el prefijo es vacío. Pero $S=\{1,|A|+1\}$ permanece finito y no vacío; su máximo existe y controla la cola, que en ese caso comprende todos los índices. Se ha incluido una cota explícita antes de formar el máximo, en lugar de intentar tomar el máximo del prefijo vacío.

### 035. Pregunta 3

[]{#MA-MIC-ANM-01-006-035}

[]{#MA-MSOL-ANM-01-006-035}

El candidato es 0 y, desde $N=1$, $0<c_n\le1/2<1$. La construcción da $S=\{1,|0|+1\}\cup\{|c_0|\}=\{1,4\}$ y $M=4$. En todos los índices vale $|c_n|\le4$, pero no puede reemplazarse por $|c_n|<4$: el término inicial tiene módulo exactamente 4. La desigualdad estricta disponible para la cola no convierte el máximo del prefijo en una cota estricta.

### 036. Pregunta 4

[]{#MA-MIC-ANM-01-006-036}

[]{#MA-MSOL-ANM-01-006-036}

La sucesión tiene módulo 1 en todos los índices y está acotada por 1. Para cualquier candidato $A$, la triangular da $2\le|1-A|+|-1-A|$; al menos un error es mayor o igual que 1. Ese valor se obtiene después de cualquier corte $N$ en $2N$ o $2N+1$. La tolerancia 1 refuta cada candidato, luego no hay límite real. Refutar sólo un $A$ dejaría abiertos los demás; aquí $A$ fue arbitrario.

### 037. Pregunta 5

[]{#MA-MIC-ANM-01-006-037}

[]{#MA-MSOL-ANM-01-006-037}

La sucesión de error es $e_n=a_n-3=-2/(n+1)$, función real con el mismo dominio $\mathbb N$. En cada índice $|e_n-0|=|a_n-3|=2/(n+1)$. Por tanto, los mismos umbrales para todas las tolerancias acreditan $a_n\to3$ y $e_n\to0$, en ambas direcciones. La equivalencia procede de una identidad de errores, sin usar una regla de resta de límites.

### 038. Pregunta 6

[]{#MA-MIC-ANM-01-006-038}

[]{#MA-MSOL-ANM-01-006-038}

Para $C=3$ tomamos $N=\max\{4,7\}=7$. Si $n\ge7$, ambas obligaciones están disponibles y $|v_n|\le3|u_n|<3(\varepsilon/3)=\varepsilon$. Si $C=0$, la comparación desde $T$ da $|v_n|\le0$, luego $v_n=0$ en esa cola. El corte $T$ sirve para todas las tolerancias positivas; no se divide por cero.

### 039. Pregunta 7

[]{#MA-MIC-ANM-01-006-039}

[]{#MA-MSOL-ANM-01-006-039}

Definimos $u_n=a_n-A$ y $v_n=|a_n|-|A|$. La identidad de errores da $u_n\to0$. La triangular inversa asegura $|v_n|\le|u_n|$ para todo índice, así que usamos $C=1$ y $T=0$. La transferencia produce $v_n\to0$, equivalente a $|a_n|\to|A|$. La comparación puede ser una igualdad; la estrictitud final viene de $|u_n|<\varepsilon$ en la cola, no de una mejora estricta en la triangular inversa.

### 040. Pregunta 8

[]{#MA-MIC-ANM-01-006-040}

[]{#MA-MSOL-ANM-01-006-040}

Para $a_n=(-1)^n$, los módulos son la constante 1 y convergen, pero $a$ no tiene límite real. Para la segunda afirmación tomamos $u_n=1/(n+1)$, $v_n=1$ y $C_n=n+1$. Entonces $|v_n|=C_n|u_n|$ en todos los índices y $u_n\to0$, mientras que $v$ no converge a cero. Los coeficientes variables sin una cota fija pueden compensar por completo el error pequeño. El lema requiere una constante fija, o un control que permita reducirse a ella.

## §6.6

### 041. Pregunta 1

[]{#MA-MIC-ANM-01-006-041}

[]{#MA-MSOL-ANM-01-006-041}

[]{#MA-SEC-ANM-01-006-006}

Con $a_n\to A$ y $b_n\to B$, primero se recibe $\varepsilon>0$, luego se eligen tolerancias auxiliares $\varepsilon/2$ para cada sucesión, después sus cortes $N_a,N_b$ y finalmente $N=\max\{N_a,N_b\}$. Para todo $n\ge N$, la triangular da $|(a_n+b_n)-(A+B)|\le|a_n-A|+|b_n-B|<\varepsilon$. También sirve el reparto $\varepsilon/3$ y $2\varepsilon/3$: ambos son positivos y su suma es la tolerancia de salida.

### 042. Pregunta 2

[]{#MA-MIC-ANM-01-006-042}

[]{#MA-MSOL-ANM-01-006-042}

Si $a_n\to A$ y $c=0$, el error de $ca_n$ respecto de $cA$ es cero y basta el corte 0. Si $c\ne0$, dado $\varepsilon>0$ pedimos a $a$ la tolerancia $\varepsilon/|c|$; entonces $|ca_n-cA|=|c||a_n-A|<\varepsilon$ en la cola. Para la diferencia suponemos además $b_n\to B$. El escalar −1 da $-b_n\to-B$, y la regla de suma aplicada a $a$ y $-b$ acredita $a_n-b_n\to A-B$.

### 043. Pregunta 3

[]{#MA-MIC-ANM-01-006-043}

[]{#MA-MSOL-ANM-01-006-043}

La identidad $a_nb_n-AB=a_n(b_n-B)+B(a_n-A)$ se obtiene al sumar y restar $a_nB$. La acotación de $a$, consecuencia de su convergencia, permite elegir $|a_n|\le M$ con $M\ge1$. Usamos tolerancias $\varepsilon/(2M)$ para $b$ y $\varepsilon/[2(|B|+1)]$ para $a$, y reunimos sus cortes. Entonces el error es a lo sumo $M|b_n-B|+|B||a_n-A|$. El primer aporte es menor que $\varepsilon/2$ y el segundo es menor o igual que $\varepsilon/2$, por lo que el total es menor que $\varepsilon$. La convergencia de $a$ se gasta tanto en su cota fija como en su captura de error.

### 044. Pregunta 4

[]{#MA-MIC-ANM-01-006-044}

[]{#MA-MSOL-ANM-01-006-044}

Si $B=0$, el segundo aporte $|B||a_n-A|$ es exactamente cero. No se puede conservar una desigualdad estricta al multiplicar por cero: se usa $0\le\varepsilon/2$. El primer aporte cumple $M|b_n-B|<\varepsilon/2$, porque $M\ge1$ es positivo y se pidió la tolerancia $\varepsilon/(2M)$. Ese aporte basta para cerrar el error total estrictamente por debajo de $\varepsilon$, sin dividir por $B$.

### 045. Pregunta 5

[]{#MA-MIC-ANM-01-006-045}

[]{#MA-MSOL-ANM-01-006-045}

Como $B\ne0$, $|B|/2>0$ es una tolerancia legítima. La convergencia da un corte $T$ con $|b_n-B|<|B|/2$ desde él. Por la triangular, $|b_n|\ge|B|-|b_n-B|>|B|/2>0$. La hipótesis autoriza esa escala positiva y la no anulación tardía necesaria para invertir los términos. La prueba sólo usa módulos y también cubre $B<0$.

### 046. Pregunta 6

[]{#MA-MIC-ANM-01-006-046}

[]{#MA-MSOL-ANM-01-006-046}

La sucesión $s_n=(-1)^n/(n+1)$ converge a cero. Por suma con la constante 1, $1+s_n\to1$; cambiar los dos términos iniciales conserva ese límite, así que $b_n\to1$. Para $n\ge2$, $|s_n|\le1/3$ y $b_n\ge2/3>1/2$, margen válido desde $T=2$. Definimos $c_0=c_1=0$ y $c_n=1/b_n$ para $n\ge2$. Es una función $\mathbb N\to\mathbb R$ y la regla del inverso extendido da $c_n\to1$. Cambiar efectivamente algún valor del prefijo cambia la función; la coincidencia eventual conserva el límite. No se toman recíprocos de los ceros iniciales.

### 047. Pregunta 7

[]{#MA-MIC-ANM-01-006-047}

[]{#MA-MSOL-ANM-01-006-047}

Si todos los $b_n$ son no nulos, $q_n=a_n/b_n$ es una función $\mathbb N\to\mathbb R$ y la regla del cociente global da $A/B$. Si sólo se garantiza no anulación desde $T$, definimos $z_n=0$ antes de $T$ y $z_n=a_n/b_n$ desde él: la extensión tiene dominio $\mathbb N$ y converge por inverso extendido y producto. La función $y_k=a_{T+k}/b_{T+k}$ también tiene dominio $\mathbb N$, pero sus índices son reindexados; es la cola reindexada de $z$ y converge a $A/B$ por la equivalencia de colas. La restricción a los índices originales desde $T$ tiene dominio $\mathbb N_{\ge T}$ y es otro objeto.

### 048. Pregunta 8

[]{#MA-MIC-ANM-01-006-048}

[]{#MA-MSOL-ANM-01-006-048}

Si $B=0$, ni $1/B$ ni $A/B$ son números reales, y la regla no proporciona un límite. Eso no decide todos los cocientes: para $h_n=1/(n+1)>0$, las identidades $h_n/h_n=1$ y $h_n^2/h_n=h_n$ acreditan límites 1 y 0, respectivamente, pese a que el denominador tiende a cero. Una suma convergente tampoco obliga a converger a sus sumandos: $a_n=(-1)^n$ y $b_n=-(-1)^n$ no tienen límite real, pero su suma es la constante cero.

## §6.7

### 049. Pregunta 1

[]{#MA-MIC-ANM-01-006-049}

[]{#MA-MSOL-ANM-01-006-049}

[]{#MA-SEC-ANM-01-006-007}

Si $a_n\to A$, $b_n\to B$ y $a_n\le b_n$ desde $T$, suponemos $A>B$ y ponemos $d=A-B>0$. Elegimos tolerancia $d/3$ para las dos convergencias y cortes $N_a,N_b$. Desde $N=\max\{T,N_a,N_b\}$ valen las dos capturas y la comparación eventual. Pero $a_n>A-d/3=B+2d/3>B+d/3>b_n$, contradiciendo $a_n\le b_n$. Luego $A\le B$. El máximo reúne tres controles, incluido el corte de comparación.

### 050. Pregunta 2

[]{#MA-MIC-ANM-01-006-050}

[]{#MA-MSOL-ANM-01-006-050}

La sucesión constante cero converge a 0 y satisface $0\le x_n$ en la cola indicada. El paso al límite en el orden, aplicado a esa constante y a $x_n\to X$, da $0\le X$. La sola positividad eventual no construye un límite: por ejemplo, $x_n=2+(-1)^n$ es positiva y toma los valores $3$ en los pares y $1$ en los impares. Para cualquier candidato $X$, la triangular da $2\le|3-X|+|1-X|$, de modo que uno de esos errores es al menos $1$. Elegido ese valor, después de cada corte $N$ aparece en $2N$ o en $2N+1$. La tolerancia $1$ refuta así todo candidato, aunque todos los términos sean positivos.

### 051. Pregunta 3

[]{#MA-MIC-ANM-01-006-051}

[]{#MA-MSOL-ANM-01-006-051}

Para todo $n\in\mathbb N$, $n+1>0$ y por tanto $0<1/(n+1)$. La constante cero converge a cero y la primera prueba de §6.3 acredita el mismo destino para $1/(n+1)$. Sus términos están estrictamente ordenados y nunca son iguales; las funciones son distintas. Sus límites son dos números iguales a 0. La comparación estricta entre términos no obliga a una separación estricta de esos números.

### 052. Pregunta 4

[]{#MA-MIC-ANM-01-006-052}

[]{#MA-MSOL-ANM-01-006-052}

La regla de suma da $a_n+\delta\to A+\delta$. Como $a_n+\delta\le b_n$ eventualmente y ambas sucesiones convergen, el paso al límite en el orden produce $A+\delta\le B$. Al ser $\delta>0$, resulta $A<B$. La hipótesis adicional es un margen positivo fijo entre las sucesiones; la sola diferencia positiva en cada índice podría tender a cero y permitir límites iguales.

### 053. Pregunta 5

[]{#MA-MIC-ANM-01-006-053}

[]{#MA-MSOL-ANM-01-006-053}

Dada $\varepsilon>0$, las convergencias de $u,v$ hacia el mismo $L$ proporcionan cortes $N_u,N_v$. Reunimos éstos con el corte $T$ de $u_n\le a_n\le v_n$. Para todo $n\ge\max\{T,N_u,N_v\}$, la parte inferior de la captura de $u$ y la parte superior de la de $v$ dan $L-\varepsilon<u_n\le a_n\le v_n<L+\varepsilon$. Así $|a_n-L|<\varepsilon$. La estrictitud procede de las capturas exteriores; no se supone convergencia previa de $a$.

### 054. Pregunta 6

[]{#MA-MIC-ANM-01-006-054}

[]{#MA-MSOL-ANM-01-006-054}

Tomamos $N=\max\{3,8,5,6\}=8$. Si $n\ge8$, ambas comparaciones y ambas capturas están disponibles. Para el destino exterior común $L$ y la tolerancia considerada, se obtiene $L-\varepsilon<u_n\le a_n\le v_n<L+\varepsilon$. Por tanto, el error del término intermedio respecto de $L$ es menor que $\varepsilon$ en toda la cola desde 8.

### 055. Pregunta 7

[]{#MA-MIC-ANM-01-006-055}

[]{#MA-MSOL-ANM-01-006-055}

Como $n+1\ge1$, $|w_n|=1/(n+1)^2\le1/(n+1)$, de donde $-1/(n+1)\le w_n\le1/(n+1)$. Las fronteras convergen a cero por la primera prueba y la regla del escalar −1. El sándwich da $w_n\to0$. En $n=0$, $w_0=1$ coincide con la frontera superior; desde $n=1$, su módulo es estrictamente menor que $1/(n+1)$. El teorema admite comparaciones no estrictas y no requiere monotonía de la intermedia: las capturas exteriores son las que aseguran el error estricto.

### 056. Pregunta 8

[]{#MA-MIC-ANM-01-006-056}

[]{#MA-MSOL-ANM-01-006-056}

En $-1\le q_n=(-1)^n\le1$, las fronteras convergen pero a destinos distintos; falta el candidato exterior común. La separación de los valores de $q$ impide su convergencia. Para $r_n=0$ en índices pares y 1 en impares, las fronteras cero sí tienen destino común, pero sólo en los pares se cumple $0\le r_n\le0$. No existe un corte desde el que esa comparación valga para todos los índices. Los impares arbitrariamente tardíos refutan el candidato 0. Cada una de las dos hipótesis ausentes es necesaria para aplicar el sándwich.

## §6.8

### 057. Pregunta 1

[]{#MA-MIC-ANM-01-006-057}

[]{#MA-MSOL-ANM-01-006-057}

[]{#MA-SEC-ANM-01-006-008}

Acreditar $a_n\to A$ exige $\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\ge N:\ |a_n-A|<\varepsilon$. Refutar ese candidato exige $\exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists n\ge N:\ |a_n-A|\ge\varepsilon_0$. Para excluir todo límite real se antepone $\forall A\in\mathbb R$ a esta última obligación. La tolerancia puede depender de la sucesión fijada y de $A$, pero debe quedar elegida antes del corte $N$ y del índice infractor posterior.

### 058. Pregunta 2

[]{#MA-MIC-ANM-01-006-058}

[]{#MA-MSOL-ANM-01-006-058}

Como $n+2>0$, la identidad $f_n=2-3/(n+2)$ da error $3/(n+2)$. Para $\varepsilon>0$, tomamos $N=\lfloor3/\varepsilon\rfloor$; si $n\ge N$, $n+2\ge N+2>3/\varepsilon$, luego el error es menor que $\varepsilon$. Con $\varepsilon=1/2$, el testigo es 6 y, para cualquier $n\ge6$, el error es a lo sumo $3/8<1/2$. La desigualdad se verificó para un índice arbitrario posterior al corte; no sólo en el índice 6.

### 059. Pregunta 3

[]{#MA-MIC-ANM-01-006-059}

[]{#MA-MSOL-ANM-01-006-059}

Con $h_n=1/(n+1)\to0$, se tiene $f_n=(2-h_n)/(1+h_n)$: multiplicar numerador y denominador por $n+1>0$ recupera $(2n+1)/(n+2)$. Las reglas lineales dan límites 2 y 1 para las nuevas sucesiones. Además, $1+h_n>0$ en todo índice, así que el cociente global está definido y converge a 2. Aplicar directamente la regla a $2n+1$ y $n+2$ exigiría convergencias reales finitas de ambos factores, que no están disponibles: ambas sucesiones son no acotadas y no pueden tener tales límites.

### 060. Pregunta 4

[]{#MA-MIC-ANM-01-006-060}

[]{#MA-MSOL-ANM-01-006-060}

La identidad $f_n=2-3/(n+2)<2$ vale en todos los índices. Luego $|f_n-3|=3-f_n=1+3/(n+2)>1$. Fijamos la tolerancia 1 y, para cualquier corte $N$, elegimos el infractor $n=N$. Se refuta el candidato 3, mientras que las pruebas anteriores acreditan el candidato 2. Las afirmaciones son compatibles: la refutación de un destino incorrecto no niega la convergencia a otro.

### 061. Pregunta 5

[]{#MA-MIC-ANM-01-006-061}

[]{#MA-MSOL-ANM-01-006-061}

Sea $h_n=1/(n+1)\to0$ y $v_n=x_n-3=p_n/(n+1)$. Desde $T$, $|v_n|\le5h_n$, así que la transferencia con $C=5$ da $v_n\to0$ y la identidad de errores da $x_n\to3$. Para $\varepsilon>0$, podemos usar $N=\max\{T,\lfloor5/\varepsilon\rfloor\}$: reúne la cota de $p$ con la captura de $h$ para $\varepsilon/5$. Sólo se necesita la magnitud eventual de $p$, no una convergencia suya.

### 062. Pregunta 6

[]{#MA-MIC-ANM-01-006-062}

[]{#MA-MSOL-ANM-01-006-062}

Desde $T$, la cota $|p_n|\le5$ y el denominador positivo dan $3-5/(n+1)\le x_n\le3+5/(n+1)$. Las fronteras $u_n=3-5h_n$ y $v_n=3+5h_n$ convergen a 3 por reglas lineales. El sándwich acredita $x_n\to3$ sin suponer su convergencia. Sería circular pasar al límite en las dos comparaciones atribuyendo previamente un límite a $x$, pues justamente su existencia y su candidato deben producirse mediante la captura exterior.

### 063. Pregunta 7

[]{#MA-MIC-ANM-01-006-063}

[]{#MA-MSOL-ANM-01-006-063}

Si $b_n\ne0$ sólo desde $T$, una extensión $z:\mathbb N\to\mathbb R$ asigna valores reales antes de $T$ y pone $z_n=a_n/b_n$ desde él. La cola reindexada $y_k=a_{T+k}/b_{T+k}$ también tiene dominio $\mathbb N$, pero elimina el prefijo y usa otra correspondencia de índices. Antes de calcular se comprueba no anulación en cada evaluación y se identifica cuál función está definida. Para aplicar la regla del cociente se requieren además $a_n\to A$, $b_n\to B\ne0$. Bajo esas hipótesis, extensión y reindexación tienen límite $A/B$. Una modificación del prefijo conserva el límite, aunque pueda cambiar la función.

### 064. Pregunta 8

[]{#MA-MIC-ANM-01-006-064}

[]{#MA-MSOL-ANM-01-006-064}

Elegimos las dos primeras afirmaciones. La sucesión $(-1)^n$ es acotada por 1, pero no tiene límite real: la triangular separa alguno de sus valores persistentes de cada candidato. La conclusión válida que queda es que convergencia implica acotación, no su conversa. Para el orden, las sucesiones $a_n=0$ y $b_n=1/(n+1)$ satisfacen $a_n<b_n$ en todos los índices y ambas convergen a 0. Con convergencias acreditadas y orden eventual se conserva la conclusión no estricta $A\le B$; obtener $A<B$ necesita información adicional, como un margen positivo uniforme.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 6](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) · [Ejercicios](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-microcontroles.html)
