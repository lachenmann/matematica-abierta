---
content-id: MA-BCH-0228
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-006-SOLUCIONES
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
title: Soluciones — Capítulo 6
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C06_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 6](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) · [Ejercicios](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-microcontroles.html)

Las referencias numéricas remiten al banco principal de C06. Los ejemplos elegidos son respuestas posibles; las pruebas cierran las condiciones de cada enunciado.

## §6.1

### 1. Ventanas con lados distintos

[]{#MA-EX-ANM-01-006-001}

[]{#MA-SOL-ANM-01-006-001}

[]{#MA-SEC-ANM-01-006-001}

La sucesión $a$ y el candidato real $A$ se fijan al comienzo; $n$ y $N$ son índices, mientras que $a_n,r,s$ son reales. Si $a_n\to A$, dados $r,s>0$ usamos la tolerancia $\delta=\min\{r,s\}>0$. Su umbral garantiza $-r<a_n-A<s$ en toda la cola. Recíprocamente, recibida $\varepsilon>0$, aplicamos la condición con $r=s=\varepsilon$. Entonces $A-\varepsilon<a_n<A+\varepsilon$, que equivale a $|a_n-A|<\varepsilon$. En cada dirección el umbral se elige antes de tomar un índice arbitrario de la cola; no hace falta que las ventanas iniciales sean simétricas.

### 2. Lo que un prefijo no decide

[]{#MA-EX-ANM-01-006-002}

[]{#MA-SOL-ANM-01-006-002}

Definimos $a_n=b_n=x_n$ para $n\le m$, y ponemos $a_n=0$, $b_n=2$ para $n>m$. Son funciones con dominio $\mathbb N$ y valores reales. Para cualquier $\varepsilon>0$, el umbral $m+1$ da $|a_n|=0<\varepsilon$, de modo que $a_n\to0$. Para $b$ fijamos la tolerancia 1. Ningún corte $N$ captura su cola alrededor de 0: el índice $n=\max\{N,m+1\}$ tiene $|b_n|=2\ge1$. Las gráficas comparten exactamente los puntos prescritos $(n,x_n)$ en el intervalo de índices mostrado. Ese prefijo no decide la captura de una cola ni la convergencia a 0.

### 3. Una familia con destino común

[]{#MA-EX-ANM-01-006-003}

[]{#MA-SOL-ANM-01-006-003}

Cuando $T=0$, el prefijo es vacío y la única sucesión de esta familia es la constante $A$. Para cualquier $T$ y cualquier $\varepsilon>0$, tomamos $N=T$. Todos los índices $n\ge N$ cumplen $|a^x_n-A|=0<\varepsilon$; la prueba no depende de las magnitudes del prefijo. Las funciones $a^x$ y $a^y$ tienen el mismo dominio y coinciden desde $T$. Son iguales si y sólo si $x_j=y_j$ para todos los índices $j<T$, pues ésa es la única zona en que pueden diferir. Si $T>0$, basta escoger $x_0\ne y_0$ para obtener funciones diferentes con el mismo candidato de convergencia. No se necesita aquí el teorema posterior de unicidad.

### 4. Qué familia de ventanas basta

[]{#MA-EX-ANM-01-006-004}

[]{#MA-SOL-ANM-01-006-004}

Si $a_n\to A$ y $u<A<v$, la tolerancia $\delta=\min\{A-u,v-A\}>0$ produce una cola en $(A-\delta,A+\delta)\subseteq(u,v)$. A la inversa, los intervalos $(A-\varepsilon,A+\varepsilon)$ están entre los intervalos exigidos, por lo que recuperamos la definición para cada $\varepsilon>0$. Todo intervalo abierto que contiene $A$ es una vecindad: contiene esa bola de radio $\delta$. Además, por la definición de C04, cualquier vecindad $U$ de $A$ contiene una bola $B(A,r)$ con $r>0$. Así, capturar cada vecindad implica capturar cada intervalo, y capturar cada intervalo implica capturar una bola contenida en cada vecindad. Las inclusiones transmiten la captura a $U$, aunque $U$ no sea un intervalo.

## §6.2

### 5. Un candidato elegido demasiado tarde

[]{#MA-EX-ANM-01-006-005}

[]{#MA-SOL-ANM-01-006-005}

[]{#MA-SEC-ANM-01-006-002}

La premisa controla distancias a centros elegidos después de la tolerancia; no los identifica con 0. Para la sucesión constante $a_n=5$, basta elegir $A_\varepsilon=5$ y $N_\varepsilon=0$ para cualquier tolerancia: el error es cero. Sin embargo, con candidato 0 y tolerancia 1, cada término tiene error 5, así que ningún corte funciona. Para probar $a_n\to0$ hay que fijar ese centro antes de recibir $\varepsilon$ y, para cada tolerancia, construir un umbral que controle $|a_n|$ en toda la cola. Este ejemplo refuta la conclusión propuesta; no pretende negar que la premisa pueda tener consecuencias distintas en una teoría posterior.

### 6. Negar la existencia de un destino

[]{#MA-EX-ANM-01-006-006}

[]{#MA-SOL-ANM-01-006-006}

La existencia de un destino real se expresa mediante $\exists A\in\mathbb R\ \forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N:\ n\ge N\Rightarrow |a_n-A|<\varepsilon$. Al negar sucesivamente los cuantificadores y la implicación obtenemos

$$
\forall A\in\mathbb R\ \exists\varepsilon_A>0\ \forall N\in\mathbb N\ \exists n\in\mathbb N:\quad n\ge N\ \text{y}\ |a_n-A|\ge\varepsilon_A.
$$

La sucesión queda fijada. Para cada candidato se elige una tolerancia de refutación, que puede depender de él, pero no del corte posterior. Después de cada corte se construye un índice infractor. Para refutar un solo candidato $A_0$ se exige la misma condición únicamente para ese número: desaparece el cuantificador inicial sobre todos los reales. Tal refutación deja sin decidir los demás candidatos.

### 7. Visitar sin permanecer

[]{#MA-EX-ANM-01-006-007}

[]{#MA-SOL-ANM-01-006-007}

Definimos $a_n=0$ si $n$ es par y $a_n=n+2$ si es impar. El conjunto de valores no tiene sólo dos elementos: los índices impares producen valores distintos. Dados una tolerancia $\varepsilon>0$ y un corte $N\in\mathbb N$, el índice $2N\ge N$ satisface $a_{2N}=0\in B(0,\varepsilon)$. Por tanto, cada ventana es visitada arbitrariamente tarde. En cambio, fijamos $\varepsilon_0=2$. Después de cualquier corte, el índice $2N+1$ tiene $|a_{2N+1}|=2N+3\ge2$. Ninguna cola completa queda en $B(0,2)$. Los índices de visitas e infracciones se han construido explícitamente; no se usan resultados sobre subsucesiones.

### 8. Cambiar la frontera del error

[]{#MA-EX-ANM-01-006-008}

[]{#MA-SOL-ANM-01-006-008}

Una captura con error estricto implica la misma captura con error no estricto. Recíprocamente, si tenemos la condición no estricta para toda tolerancia, recibida $\varepsilon>0$ usamos $\varepsilon/2$; el umbral correspondiente garantiza $|a_n-A|\le\varepsilon/2<\varepsilon$. Su negación es: existe $\eta>0$ tal que, después de cada corte, aparece un índice con $|a_n-A|>\eta$. Esta condición implica la refutación usual con error $\ge\eta$. Si la refutación usual proporciona $\varepsilon_0>0$ y errores $\ge\varepsilon_0$ después de cada corte, esos mismos índices tienen errores $>\varepsilon_0/2$. Así obtenemos la otra negación. La posibilidad de cambiar de tolerancia permite absorber la diferencia de frontera.

### 9. Sólo tolerancias pequeñas

[]{#MA-EX-ANM-01-006-009}

[]{#MA-SOL-ANM-01-006-009}

Para una tolerancia arbitraria $\varepsilon>0$, elegimos $\delta=\min\{\varepsilon/2,r/2\}$. Es positiva, menor que $r$ y menor que $\varepsilon$. La hipótesis proporciona un umbral para $\delta$, que sirve también para $\varepsilon$, pues $|a_n-A|<\delta<\varepsilon$. No hemos elegido un único corte para todas las tolerancias. Verificar solamente $r$ no basta: la constante $a_n=A+r/2$ satisface $|a_n-A|=r/2<r$ en todos los índices, pero no converge a $A$. La tolerancia $r/4$ falla en toda la sucesión. Una familia de exigencias pequeñas conserva la posibilidad de refinar la captura; una sola exigencia no la conserva.

## §6.3

### 10. Centro, escala y denominador

[]{#MA-EX-ANM-01-006-010}

[]{#MA-SOL-ANM-01-006-010}

[]{#MA-SEC-ANM-01-006-003}

El denominador cumple $dn+e\ge e>0$ para todo $n\in\mathbb N$, incluido 0. Si $c=0$, la sucesión es constante y $N=0$ sirve para cualquier tolerancia. Si $c\ne0$, ponemos $t=|c|/(d\varepsilon)>0$ y elegimos $N=\lfloor t\rfloor+1$. El piso usado es el construido en §6.3; por su propiedad, $N>t$. Para un índice arbitrario $n\ge N$, tenemos $dn+e>d t=|c|/\varepsilon$. Al dividir por cantidades positivas obtenemos $|a_n-A|=|c|/(dn+e)<\varepsilon$. El testigo es suficiente, aunque el término $e$ pueda permitir uno menor. No se invoca ninguna regla algebraica de límites.

### 11. Dos cortes defectuosos

[]{#MA-EX-ANM-01-006-011}

[]{#MA-SOL-ANM-01-006-011}

Tomamos $c=d=e=1$ y $\varepsilon=1/3$. Entonces $N_1=2$, pero en el índice $n=2$ el error es $1/3$, exactamente la tolerancia. La condición estricta falla, aunque $N_1$ sea un natural. Para $N_2$, con los mismos parámetros y $\varepsilon=2$, resulta $N_2=\lfloor1/2\rfloor-1=-1$, que no pertenece a $\mathbb N$ y no puede servir como umbral de la definición. En ambas fórmulas el defecto ocurre antes de acreditar toda la cola. Una reparación común es $N=\lfloor|c|/(d\varepsilon)\rfloor+1$. Es natural y mayor que $|c|/(d\varepsilon)$; el argumento del ejercicio 10 verifica el error estricto para cada $n\ge N$. Esta reparación no pretende conservar la minimalidad.

La [figura C06-F03](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.3 muestra el mismo fallo de estrictitud en n=2. No representa el segundo defecto: N₂=−1 falla por no pertenecer al dominio de índices.

### 12. Un prefijo arbitrario

[]{#MA-EX-ANM-01-006-012}

[]{#MA-SOL-ANM-01-006-012}

Los términos del prefijo son reales y los restantes están definidos porque $dn+e>0$. Si $c=0$, elegimos $N=T$ y el error es cero en toda la cola. Si $c\ne0$, dado $\varepsilon>0$ ponemos $K=\lfloor|c|/(d\varepsilon)\rfloor+1$ y $N=\max\{T,K\}$. Para cualquier $n\ge N$ se cumplen las dos obligaciones: usamos la fórmula de la cola porque $n\ge T$, y su denominador es mayor que $|c|/\varepsilon$ porque $n\ge K$. Por tanto, $|a_n-A|<\varepsilon$. Cuando $T=0$ no hay valores iniciales que controlar y la misma construcción funciona. La prueba explica directamente por qué ningún tamaño del prefijo interviene en la estimación tardía.

### 13. Un corte suficiente y el menor corte

[]{#MA-EX-ANM-01-006-013}

[]{#MA-SOL-ANM-01-006-013}

Como $n+3>0$, la condición es $n>2/\varepsilon-3$. Ponemos $m=\lfloor2/\varepsilon\rfloor$, usando sólo el piso de un real positivo. El menor umbral es

$$
N_{\min}=\max\{0,m-2\}.
$$

Si $m\le2$, entonces $2/\varepsilon<m+1\le3$, por lo que el índice 0 y todos los posteriores cumplen la condición. Si $m\ge3$, el índice $m-2$ satisface $n+3=m+1>2/\varepsilon$. Todo natural anterior tiene $n+3\le m\le2/\varepsilon$ y falla el error estricto. Esto acredita la minimalidad y el control de toda la cola. El corte $K=m+1$ del ejercicio 10 es válido pero mayor. Para $\varepsilon=2/5$, $N_{\min}=3$: el índice 2 tiene error $2/5$ y debe excluirse. Para $\varepsilon=1$, $N_{\min}=0$, mientras que $K=3$. Un testigo suficiente responde a la definición; determinar el menor requiere examinar también por qué fallan los índices anteriores.

### 14. Dos valores que no desaparecen

[]{#MA-EX-ANM-01-006-014}

[]{#MA-SOL-ANM-01-006-014}

Fijamos un candidato arbitrario $A$ y $D=|p-q|>0$. La triangular da $D\le|p-A|+|q-A|$, de modo que alguno de los dos errores es al menos $D/2$. Elegimos ese valor una vez para este candidato y fijamos $\varepsilon_A=D/2$. Después de cualquier corte usamos $i(N)$ o $j(N)$, según el valor elegido, para obtener el infractor requerido. Como el argumento vale para cada $A$, no hay destino real. Para el ejemplo, ponemos $a_{3k}=-2$, $a_{3k+1}=4$ y $a_{3k+2}=k$. Las fórmulas $i(N)=3N$ y $j(N)=3N+1$ acreditan las hipótesis. Los valores adicionales no eliminan la separación persistente que refuta cada candidato.

## §6.4

### 15. Cómo repartir una separación

[]{#MA-EX-ANM-01-006-015}

[]{#MA-SOL-ANM-01-006-015}

[]{#MA-SEC-ANM-01-006-004}

Sincronizados los umbrales, un mismo término satisface ambas capturas y la triangular da $D\le|A-a_n|+|a_n-B|<(\alpha+\beta)D$. Hay contradicción si $\alpha+\beta\le1$, incluida la igualdad, porque el error total es estricto. Si la suma es mayor que 1, esa estimación aislada no contradice $D>0$. Más aún, las ventanas pueden compartir un punto: con $A=0$, $B=D$, elegimos un real $t$ en $(\max\{0,1-\beta\},\min\{1,\alpha\})$, intervalo no vacío cuando $\alpha+\beta>1$. El punto $tD$ tiene distancias menores que $\alpha D$ y $\beta D$. Esto no permite dos límites reales distintos: para la unicidad pueden elegirse otras tolerancias cuya suma sea menor o igual que la separación. Sólo muestra que el reparto propuesto no cierra esa contradicción.

### 16. Transportar índices y cortes

[]{#MA-EX-ANM-01-006-016}

[]{#MA-SOL-ANM-01-006-016}

La función $r$ tiene dominio $\mathbb N_{\ge T}$ y codominio $\mathbb R$; $b$ tiene dominio $\mathbb N$ y el mismo codominio. La biyección $\tau_T(k)=T+k$ lleva $\mathbb N$ a $\mathbb N_{\ge T}$ y tiene inversa $n\mapsto n-T$. Se cumple $b=r\circ\tau_T$, no igualdad de las dos funciones. Si $a$ tiene umbral $N$ para la tolerancia dada, podemos usar $K=\max\{0,N-T\}$ para $b$. Cuando $k\ge K$, se tiene $T+k\ge N$, tanto si $N\le T$ como si $N>T$; de ahí $|b_k-A|<\varepsilon$. Si $b$ tiene umbral $K$, tomamos $N=T+K$ para $a$. Cada $n\ge N$ admite $k=n-T\in\mathbb N$ con $k\ge K$, y $a_n=b_k$. La correspondencia de índices transporta el control de toda la cola.

En la [figura C06-F05](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.4, la fila c ilustra la reindexación con T=3. Aquí b cumple ese papel para T general; el corte optimizado K=max{0,N−T} se justifica por las desigualdades anteriores, no por el corte suficiente de la figura.

### 17. Tres funciones y un destino

[]{#MA-EX-ANM-01-006-017}

[]{#MA-SOL-ANM-01-006-017}

Tomamos $a_n=0$ para todo $n$, $b_0=7$ y $b_n=0$ para $n\ge1$, y $c_n=1/(n+1)$. La convergencia de $a$ sigue del error cero; $b$ converge a 0 con umbral 1 para cualquier tolerancia. La convergencia de $c$ es la prueba directa de §6.3. Las tres funciones son distintas: $a_0\ne b_0$, $c_0\ne a_0$ y $c_0\ne b_0$. Además, $c_n>0=a_n=b_n$ para todo $n\ge1$. Hay coincidencia eventual entre $a$ y $b$, pero no entre éstas y $c$. Después de la unicidad de §6.4 sus límites pueden escribirse como el mismo número 0; la igualdad de esos números no implica igualdad de funciones ni coincidencia eventual.

### 18. Alguna cola y todas las colas

[]{#MA-EX-ANM-01-006-018}

[]{#MA-SOL-ANM-01-006-018}

Si $a_n\to A$, fijamos cualquier $T$. Dada una tolerancia con umbral $N$ para $a$, el mismo umbral para $k$ es suficiente, porque $T+k\ge k\ge N$. Así converge cada cola reindexada al candidato común. Que converjan todas implica que converge alguna, por ejemplo la de $T=0$. Si converge una cola con índice inicial $T$, recibimos $\varepsilon>0$ y obtenemos su corte $K$. El umbral $N=T+K$ controla $a$: para todo $n\ge N$, el natural $k=n-T\ge K$ tiene $a_n=a_{T+k}$ y error menor que $\varepsilon$. Esta última dirección explica por qué basta alguna cola. El candidato $A$ queda fijo en las tres afirmaciones; los cortes dependen de la tolerancia y pueden depender de $T$.

## §6.5

### 19. Acotar con otra tolerancia

[]{#MA-EX-ANM-01-006-019}

[]{#MA-SOL-ANM-01-006-019}

[]{#MA-SEC-ANM-01-006-005}

Definimos el conjunto finito no vacío $S_r=\{1,|A|+r\}\cup\{|a_j|:j<N_r\}$ y $M_r=\max S_r$. Para $n<N_r$ la cota está incluida en el conjunto; para $n\ge N_r$, la triangular da $|a_n|\le|A|+|a_n-A|<|A|+r\le M_r$. Por tanto, $|a_n|\le M_r$ en todos los índices, sin pretender estrictitud en el prefijo. Si $N_r=0$, el prefijo es vacío, pero $S_r$ sigue conteniendo 1. En el ejemplo $A=0$: la primera elección produce $M_1=20$ y la segunda $M_{30}=30$. Un corte anterior puede reducir el prefijo que se inspecciona, pero una tolerancia mayor aumenta la cota de cola. No hay una minimización automática por ese cambio.

La [figura C06-F06](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.5 muestra cómo reunir cola y prefijo. Su cota 4 corresponde a otro ejemplo; las cotas 20 y 30 de esta solución se calculan con sus propios datos.

### 20. Qué decide el módulo

[]{#MA-EX-ANM-01-006-020}

[]{#MA-SOL-ANM-01-006-020}

Podemos tomar $a_n=2(-1)^n$. Su módulo es la constante 2, que converge a 2. Los valores 2 y −2 reaparecen después de cada corte, y el argumento de separación del ejercicio 14 refuta todos los candidatos para $a$. Si $|b_n|\to0$, en cambio, su captura dice $||b_n|-0|<\varepsilon$ para toda cola suficientemente tardía. Esa expresión es precisamente $|b_n-0|$, por lo que el mismo umbral prueba $b_n\to0$. La sucesión $b_n=(-1)^n/(n+1)$ es un ejemplo: su módulo es $1/(n+1)$, cuya convergencia a cero ya se demostró directamente. El caso de módulo límite cero conserva toda la información de distancia al candidato 0; un módulo límite positivo no determina de qué lado están los términos.

### 21. Un coeficiente variable controlado

[]{#MA-EX-ANM-01-006-021}

[]{#MA-SOL-ANM-01-006-021}

Desde $R=\max\{T,S\}$ tenemos $|v_n|\le M|u_n|$. Si $M=0$, esto obliga a $v_n=0$ para $n\ge R$, y $R$ sirve para cualquier tolerancia positiva. Si $M>0$, recibimos $\varepsilon>0$ y escogemos un corte $K$ para $u$ con tolerancia $\varepsilon/M$. Para $n\ge N=\max\{R,K\}$ se cumple $|v_n|\le M|u_n|<\varepsilon$. Lo decisivo es una cota eventual fija que pueda usarse para elegir la tolerancia auxiliar antes de recorrer la cola. El coeficiente $C_n$ puede variar dentro de esa cota; su mera existencia sin control uniforme no permite el mismo argumento.

### 22. Una comparación intermitente

[]{#MA-EX-ANM-01-006-022}

[]{#MA-SOL-ANM-01-006-022}

Tomamos $u_n=1/(n+1)$ y $v_n=0$ en índices pares, $v_n=2$ en impares. La convergencia de $u$ ya está probada. Para cada corte $N$, el índice $2N$ satisface $|v_{2N}|=0\le3|u_{2N}|$. Pero con tolerancia 1, el índice $2N+1$ es un infractor para $v$ después de cualquier corte; no hay convergencia a cero. El argumento necesita que la comparación valga para todos los índices desde un mismo $T$, no sólo que algún índice la satisfaga después de cada corte. Bajo esa reparación, dado $\varepsilon>0$, elegimos $K$ para $u$ con tolerancia $\varepsilon/3$ y tomamos $\max\{T,K\}$. Cada índice posterior satisface $|v_n|\le3|u_n|<\varepsilon$.

### 23. Compartir destino por un error pequeño

[]{#MA-EX-ANM-01-006-023}

[]{#MA-SOL-ANM-01-006-023}

Si $a_n\to A$, recibimos $\varepsilon>0$. Elegimos $N_1$ para $|a_n-A|<\varepsilon/2$ y $N_2$ para $|a_n-b_n|<\varepsilon/2$. Para todo $n\ge\max\{N_1,N_2\}$, la triangular da $|b_n-A|\le|b_n-a_n|+|a_n-A|<\varepsilon$. Así converge $b$ al mismo candidato. Si $b_n\to A$, repetimos el control usando $|a_n-A|\le|a_n-b_n|+|b_n-A|$ y sus dos umbrales con tolerancia $\varepsilon/2$. El módulo de la diferencia es el mismo al invertir su orden; no hay que justificar una resta de límites para usarlo. La hipótesis aporta un control de la distancia entre las sucesiones, no coincidencia eventual entre sus términos.

## §6.6

### 24. Un reparto a medida

[]{#MA-EX-ANM-01-006-024}

[]{#MA-SOL-ANM-01-006-024}

[]{#MA-SEC-ANM-01-006-006}

Si $c,d\ne0$, usamos las tolerancias auxiliares $\theta\varepsilon/|c|$ y $(1-\theta)\varepsilon/|d|$. Tras sincronizar sus umbrales, la identidad del error y la triangular dan $|c(a_n-A)+d(b_n-B)|\le|c||a_n-A|+|d||b_n-B|<\theta\varepsilon+(1-\theta)\varepsilon=\varepsilon$. Si $c=0$ y $d\ne0$, sólo se requiere la segunda captura; su aporte es menor que $(1-\theta)\varepsilon<\varepsilon$. El caso $d=0,c\ne0$ se resuelve con la primera. Si ambos son cero, el error es cero desde el índice 0. El valor $\theta=1/3$ reserva un tercio al primer aporte y dos tercios al segundo. Las divisiones se realizan únicamente cuando el coeficiente correspondiente es no nulo.

La [figura C06-F07](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.6 muestra la elección de presupuestos antes de sincronizar. Aquí las fracciones son θ y 1−θ, con los coeficientes c,d; no tienen que ser las dos mitades del panel de suma.

### 25. Una cantidad finita de operaciones

[]{#MA-EX-ANM-01-006-025}

[]{#MA-SOL-ANM-01-006-025}

Para $m=1$ ambas afirmaciones son las hipótesis. Si valen para una familia de tamaño $m$, la sucesión de sumas parciales tiene límite $S_m=\sum_{j=1}^m A_j$. La regla binaria de suma, aplicada a esa sucesión y a $a^{(m+1)}$, produce límite $S_m+A_{m+1}$. Del mismo modo, la sucesión de productos parciales tiene límite $P_m=\prod_{j=1}^m A_j$ y la regla binaria del producto da $P_mA_{m+1}$. Cada paso usa convergencias ya acreditadas, incluso si algún $A_j=0$. Todas las operaciones son entre reales y definen sucesiones en $\mathbb N$. Para $m=0$, las convenciones de suma vacía 0 y producto vacío 1 dan sucesiones constantes con esos límites. La inducción sólo autoriza familias finitas; no demuestra una regla de suma o producto infinito.

### 26. Leer un producto al revés

[]{#MA-EX-ANM-01-006-026}

[]{#MA-SOL-ANM-01-006-026}

Para el producto cero tomamos $a_n=(-1)^n$ y $b_n=0$. El producto es la constante cero, pero $a$ toma 1 y −1 arbitrariamente tarde y no tiene límite real, por el argumento de separación. Para el producto no nulo elegimos $a_n=b_n=(-1)^n$. Ambos factores carecen de límite real por la misma separación, mientras que $a_nb_n=1$ para todo índice y, por tanto, el producto converge a 1. La regla del producto parte de la convergencia de cada factor para controlar dos errores; su conclusión no contiene información suficiente para recuperar esos controles. La convergencia del producto puede ocultar oscilaciones que se compensan entre los factores.

### 27. Un factor pequeño y otro acotado

[]{#MA-EX-ANM-01-006-027}

[]{#MA-SOL-ANM-01-006-027}

La identidad $|u_np_n|=|u_n||p_n|$ da $|u_np_n|\le M|u_n|$ desde $T$. Si $M=0$, el producto es cero en esa cola y converge a cero. Si $M>0$, para $\varepsilon>0$ escogemos un corte $K$ de $u$ con tolerancia $\varepsilon/M$; el umbral $\max\{T,K\}$ da $|u_np_n|<\varepsilon$ en todos los índices posteriores. Es el mecanismo de transferencia de §6.5, no la regla binaria del producto con dos límites. Por ejemplo, $u_n=1/(n+1)$ y $p_n=(-1)^n$: el segundo factor no tiene límite real, pero está acotado por 1 y el producto converge a cero. La cota eventual sustituye aquí el control de un segundo límite.

### 28. El inverso como conjunto de obligaciones

[]{#MA-EX-ANM-01-006-028}

[]{#MA-SOL-ANM-01-006-028}

El margen garantiza que $b_n\ne0$ para $n\ge T$; $B\ne0$ hace legítimo $1/B$. Por tanto, cada elección de prefijo define una función $c^x:\mathbb N\to\mathbb R$, incluso si $b$ tiene ceros anteriores. En la cola obtenemos

$$
\left|c^x_n-\frac1B\right|=\frac{|b_n-B|}{|b_n||B|}\le\frac{2}{|B|^2}|b_n-B|.
$$

El error $b_n-B$ tiende a cero por la identidad de §6.5. Su comparación con la constante positiva $2/|B|^2$ permite transferir la convergencia al error de $c^x$, sincronizando con $T$. Así $c^x_n\to1/B$. Este orden importa: estimar un inverso sin definirlo previamente dejaría abierta una obligación de dominio. Dos prefijos que difieran en alguna posición producen funciones distintas, pero las estimaciones tardías y el límite son los mismos. Si $T=0$, no hay dos prefijos distintos.

La [figura C06-F08](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.6 separa margen, definición, estimación y transferencia. La elección del prefijo forma parte de definir cˣ; ningún recíproco de cero queda implícito.

### 29. Un denominador negativo con ceros

[]{#MA-EX-ANM-01-006-029}

[]{#MA-SOL-ANM-01-006-029}

Elegimos $b_n=-2+1/(n+1)$ para $n\ge2$, además de los dos ceros prescritos. La sucesión dada por esa fórmula en todos los índices converge a −2 por las reglas lineales, y la modificación de dos términos conserva el límite. Para $n\ge2$, $b_n\le-5/3<0$, de modo que $|b_n|\ge5/3>1=|-2|/2$. Definimos $q_0=q_1=0$, $r_0=5,r_1=-7$ y $q_n=r_n=a_n/b_n$ para $n\ge2$. Ambos objetos son sucesiones reales definidas en todo $\mathbb N$ y difieren en el prefijo. Como $a_n\to3$ y $b_n\to-2\ne0$, el cociente extendido con prefijo cero converge a −3/2. La coincidencia eventual transmite ese límite a $r$. El cociente sin extensión no está definido en los índices 0 y 1.

En la [figura C06-F08](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.6, la ventana negativa muestra el mismo mecanismo de separación de cero. La fila numérica B=1 ilustra otro denominador; aquí B=−2, el margen elegido es 1 y el límite del cociente extendido es −3/2.

### 30. Tres cálculos que necesitan una auditoría

[]{#MA-EX-ANM-01-006-030}

[]{#MA-SOL-ANM-01-006-030}

En (i) las sucesiones lineales no tienen límites reales finitos: son no acotadas, mientras que toda sucesión convergente es acotada. La regla del cociente no se aplica a esos factores. Sin embargo, como $h_n>0$, la identidad $(3n+2)/(2n+5)=(3-h_n)/(2+3h_n)$ permite usar límites 3 y 2; el resultado es $3/2$, con denominador siempre positivo. En (ii), $h_n\ne0$ en todos los índices y el cociente es exactamente 1, por lo que converge a 1. La expresión $0/0$ no es un número real ni el resultado de la regla. En (iii), el numerador no converge y el límite cero del denominador tampoco habilita la regla. El cociente está definido, pero su módulo es $n+1$, que no está acotado: para cualquier cota real positiva hay un natural mayor, por C03. Así no tiene límite real finito. No se le asigna aquí un límite infinito.

### 31. Construir un cociente y revisar su margen

[]{#MA-EX-ANM-01-006-031}

[]{#MA-SOL-ANM-01-006-031}

Siempre que $(A,B)\ne(0,0)$ puede elegirse $(t,u)=(1,0)$ si $A\ne0$, o $(0,1)$ si sólo $B\ne0$; por ejemplo, tomamos $(r,s)=(1,1)$. Si $A=B=0$, ninguna elección lineal del denominador da $D\ne0$, limitación que debe declararse. Para cualquier elección válida, las reglas lineales dan numerador $P=rA+sB$ y denominador $D\ne0$. La tolerancia $|D|/2$ proporciona un corte $T$ con $|ta_n+ub_n|>|D|/2$. Asignando cero al cociente antes de $T$ y la fórmula desde $T$ definimos una sucesión real cuyo límite es $P/D$. Si $D=0$, la regla deja de decidir: con $a_n=b_n=h_n$, la expresión $a_n/b_n$ es 1; con $a_n=h_n$, $b_n=h_n^2$, es $n+1$ y no tiene límite real por no acotación. En ambos ejemplos $A=B=0$ y los denominadores son no nulos en todos los índices.

## §6.7

### 32. Llegar a la frontera de un intervalo

[]{#MA-EX-ANM-01-006-032}

[]{#MA-SOL-ANM-01-006-032}

[]{#MA-SEC-ANM-01-006-007}

Las sucesiones constantes $p$ y $q$ convergen a esos números. El paso al límite en las dos desigualdades eventuales da $p\le A\le q$. Si los términos están en $(p,q)$, también satisfacen las comparaciones no estrictas y sólo se conserva, en general, el intervalo cerrado. Para la frontera inferior elegimos $a_n=p+(q-p)/(n+2)$; para la superior, $b_n=q-(q-p)/(n+2)$. Como $0<1/(n+2)\le1/2<1$, ambos términos quedan estrictamente entre $p$ y $q$ en todos los índices. Las reglas lineales y la prueba de esa familia racional dan límites $p$ y $q$, respectivamente. La positividad de una distancia en cada índice no proporciona un margen fijo que excluya un extremo del límite.

### 33. Orden estricto y margen uniforme

[]{#MA-EX-ANM-01-006-033}

[]{#MA-SOL-ANM-01-006-033}

Tomamos $a_n=2-1/(n+2)$ y $b_n=2+1/(n+2)$; la desigualdad es estricta en todos los índices y los dos límites son 2. Para el segundo ejemplo podemos usar las constantes $c_n=0,d_n=3$ con $\delta=1$. En general, si $c_n\to C$, $d_n\to D$ y $c_n+\delta\le d_n$ eventualmente, las reglas lineales dan $c_n+\delta\to C+\delta$. El orden eventual pasa a los límites, de modo que $C+\delta\le D$. Como $\delta>0$, obtenemos $C<D$. Una desigualdad estricta sin escala positiva fija puede estrecharse hasta la igualdad; el margen uniforme impide ese estrechamiento.

La [figura C06-F10](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.7 ilustra la pérdida de estrictitud entre los límites con otro par de sucesiones que converge a 0. En nuestro primer ejemplo, los dos límites son 2; la diferencia sigue siendo positiva y no posee un margen uniforme.

### 34. Dos presupuestos de error exteriores

[]{#MA-EX-ANM-01-006-034}

[]{#MA-SOL-ANM-01-006-034}

Dada $\varepsilon>0$, elegimos cortes $N_r,N_s$ para que $r_n<\varepsilon$ y $s_n<\varepsilon$ en las respectivas colas; el valor absoluto de cada término coincide con él por no negatividad. Tomamos $N=\max\{T_1,T_2,N_r,N_s\}$. Para todo $n\ge N$ tenemos $L-\varepsilon<L-r_n\le a_n\le L+s_n<L+\varepsilon$. Las dos desigualdades exteriores son estrictas por las capturas de $r$ y $s$, aunque las comparaciones interiores no lo sean. La cadena equivale a $|a_n-L|<\varepsilon$ y establece la convergencia buscada desde la definición. Las cotas pueden decrecer de modos distintos, oscilar o alcanzar cero; únicamente importa que cada una permita responder a la misma tolerancia.

La [figura C06-F09](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) de §6.7 permite seguir los dos controles exteriores. Aquí rₙ y sₙ pueden ser distintos y se reúnen cuatro cortes; no se trasladan sin cambio el radio ni el corte numérico del ejemplo dibujado.

### 35. Una frontera conocida sólo por su módulo

[]{#MA-EX-ANM-01-006-035}

[]{#MA-SOL-ANM-01-006-035}

Ponemos $u_n=a_n=(-1)^n$ y $v_n=1$. Las comparaciones valen en todos los índices, $|u_n|=1$ converge a 1 y $v$ es constante. Sin embargo, $a$ y $u$ no tienen límite real, pues sus valores 1 y −1 reaparecen arbitrariamente tarde. La hipótesis sobre el módulo no determina el destino de la frontera inferior. Una reparación es exigir $u_n\to1$, manteniendo $v_n\to1$ y las comparaciones eventuales: ahora el sándwich sí produce $a_n\to1$. Una reparación más fuerte que basta para recuperar esa convergencia es añadir $u_n\ge0$ eventualmente a la condición original; entonces $u_n=|u_n|$ en una cola y la coincidencia eventual da $u_n\to1$.

### 36. Una caracterización por fronteras

[]{#MA-EX-ANM-01-006-036}

[]{#MA-SOL-ANM-01-006-036}

Si existen esas fronteras, el sándwich probado en §6.7 da $a_n\to L$ sin suponer la conclusión. Para la dirección inversa, partimos de $a_n\to L$ y construimos $u_n=a_n-1/(n+1)$ y $v_n=a_n+1/(n+1)$. Son funciones reales en $\mathbb N$ y satisfacen $u_n<a_n<v_n$ en todos los índices, además de $u_n\ne v_n$. La convergencia de $1/(n+1)$ a cero y las reglas lineales acreditan $u_n,v_n\to L$. No se usa el sándwich para probar aquí la convergencia de $a$, que ya es una hipótesis de esta dirección. Las dos implicaciones tienen puntos de partida distintos; confundirlos produciría una circularidad.

## §6.8

### 37. Dos recorridos para una expresión racional

[]{#MA-EX-ANM-01-006-037}

[]{#MA-SOL-ANM-01-006-037}

[]{#MA-SEC-ANM-01-006-008}

El candidato es $5/2$. Como $2n+3\ge3>0$, la sucesión está definida y la identidad $f_n-5/2=-11/[2(2n+3)]$ da $|f_n-5/2|=11/(4n+6)$. Para $\varepsilon>0$, tomamos $N=\lfloor11/(4\varepsilon)\rfloor+1$. Si $n\ge N$, $4n+6>11/\varepsilon$ y el error es menor que $\varepsilon$. El recorrido por reglas usa la identidad $f_n=(5-3h_n)/(2+h_n)$. Numerador y denominador convergen a 5 y 2; el segundo es positivo para todo índice, así que el cociente converge a $5/2$. La normalización transforma factores originalmente no acotados en sucesiones con límites finitos. La prueba directa aporta un corte explícito suficiente; la regla del cociente evita reconstruirlo, pero su validez depende de esas convergencias y del límite denominador no nulo.

### 38. Una perturbación que conserva el destino

[]{#MA-EX-ANM-01-006-038}

[]{#MA-SOL-ANM-01-006-038}

Elegimos $p_n=3(-1)^n$, que está acotada por 3 y no tiene límite real por la separación persistente de 3 y −3. La sucesión $h_n=1/(n+1)$ converge a cero; el ejercicio 27, o la transferencia de errores, da $p_nh_n\to0$ sin suponer un límite de $p$. Definimos primero $c_n=a_n+p_nh_n$ en todos los índices. La regla de suma produce $c_n\to A+0=A$. Finalmente asignamos cualquier prefijo real a $b$ antes de $T$ y ponemos $b_n=c_n$ desde $T$. La coincidencia eventual conserva la convergencia. Los tres controles usados son la cota del factor variable, la convergencia del factor pequeño y la transferencia de un prefijo finito; ninguno exige conocer un destino para $p$.

### 39. Qué puede recuperarse de las operaciones

[]{#MA-EX-ANM-01-006-039}

[]{#MA-SOL-ANM-01-006-039}

En (i), $b_n=(a_n+b_n)-a_n$; las reglas lineales prueban el destino indicado. En (ii), la convergencia de $a$ a un número no nulo garantiza un corte desde el que $a_n\ne0$. El cociente tardío $(a_nb_n)/a_n$ converge a $P/A$ al extenderlo, y coincide con $b$ en esa cola; así converge $b$, aunque $a$ tuviera ceros iniciales. En (iii), ponemos $q_n=a_n/b_n$, sucesión global por la hipótesis. La identidad $a_n=q_nb_n$ y la regla del producto dan $QB$, sin dividir por $B$. En (iv), tomamos $a_n=(-1)^n$ y $b_n=-(-1)^n$: suma cero y producto −1 convergen, pero ninguno de los factores converge. En (v), $a_n=0$ y $b_n=(-1)^n$ dan producto cero y $A=0$, sin convergencia de $b$. Recuperar un factor por división necesita el margen que aporta $A\ne0$.

### 40. Cambiar todo el orden de los índices

[]{#MA-EX-ANM-01-006-040}

[]{#MA-SOL-ANM-01-006-040}

La composición define $b:\mathbb N\to\mathbb R$. Supongamos $a_n\to A$ y recibamos $\varepsilon>0$, con umbral $K$ para $a$. El conjunto $F=\pi^{-1}(\{0,\ldots,K-1\})$ es finito: por biyectividad, cada uno de los $K$ índices tiene una sola preimagen. Si $F$ es vacío, ponemos $N=0$; en otro caso, $N=1+\max F$. Para todo $n\ge N$, el índice $n$ no pertenece a $F$, por lo que $\pi(n)\ge K$. Luego $|b_n-A|=|a_{\pi(n)}-A|<\varepsilon$. En particular, cuando $K=0$ el prefijo y su preimagen son vacíos. El corte controla posiciones de la permutación que caían en el prefijo original, no el tamaño numérico de $\pi(n)$ por una presunta monotonía.

Si $b_n\to A$, aplicamos el argumento a la biyección inversa $\pi^{-1}$: la identidad $a_n=b_{\pi^{-1}(n)}$ acredita la convergencia de $a$. La inyectividad impide repetir infinitamente un índice inicial; la sobreyectividad permite recuperar todos los índices mediante la inversa. El mecanismo es la finitud de las posiciones problemáticas, no una teoría de subsucesiones.

La figura [C06-F11](#fig-anm-c06-f11) muestra cómo elegir el corte en las posiciones nuevas. El ejemplo de biyección sólo ilustra el conjunto disperso de preimágenes; la finitud que acaba de probarse sostiene el argumento general.

### Figura [C06-F11](#fig-anm-c06-f11)

![En un ejemplo de biyección, el prefijo original 0,1,2 tiene preimágenes 8,5,2. El corte nuevo 9 queda después de todas ellas. Un recuadro separado da el argumento general por finitud, el caso vacío y la dirección inversa. Las flechas relacionan índices, no valores de la sucesión.](../../assets/books/anm/C06/C06-F11.svg){#fig-anm-c06-f11 fig-alt="En un ejemplo de biyección, el prefijo original 0,1,2 tiene preimágenes 8,5,2. El corte nuevo 9 queda después de todas ellas. Un recuadro separado da el argumento general por finitud, el caso vacío y la dirección inversa. Las flechas relacionan índices, no valores de la sucesión."}

**Figura [C06-F11](#fig-anm-c06-f11).** Las posiciones nuevas que envían al prefijo original forman un conjunto finito. Si no es vacío, un corte posterior a su máximo evita todas esas posiciones; si es vacío, basta el corte cero. La biyección no necesita conservar el orden.

Para K=3, el prefijo original es {0,1,2} y sus preimágenes en la biyección dibujada son {2,5,8}; N=9 evita todas esas posiciones. Si K=0, se elige N=0 sin tomar un máximo del conjunto vacío. En la dirección inversa se aplica la misma construcción a π⁻¹. Las flechas relacionan índices naturales; los términos reales aparecen al evaluar las funciones a y b.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 6](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n.html) · [Ejercicios](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-6-convergencia-el-juego-de-y-n-microcontroles.html)
