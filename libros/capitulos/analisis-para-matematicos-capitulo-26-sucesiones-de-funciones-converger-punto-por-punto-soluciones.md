---
content-id: MA-BCH-0308
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-026-SOLUCIONES
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
title: Soluciones — Capítulo 26
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C26_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)

## 26.1. Fila y columna

[]{#MA-EX-ANM-01-026-001}

[]{#MA-SOL-ANM-01-026-001}

[]{#MA-SEC-ANM-01-026-001}

La fila de índice $n$ es la aplicación $x\mapsto(n+1)x$; la columna de entrada $x$ es $n\mapsto(n+1)x$. En cero la columna es constante0. Para $x>0$, dado $M>0$ basta $n+1>M/x$ para superar $M$; para $x<0$ los valores son menores que $-M$ cuando $n+1>M/|x|$. Una sucesión convergente sería acotada por C06, de modo que sólo converge la columna de cero. El conjunto de convergencia es $\{0\}$ y su función límite vale0.

**Retorno visual.** Véase [C26-F01](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.2. El dominio que se conserva

[]{#MA-EX-ANM-01-026-002}

[]{#MA-SOL-ANM-01-026-002}

La intersección de los dominios es $X=\mathbb R\setminus\mathbb N$. Restringidas a $X$, todas las filas están definidas. Fijado $x\in X$, elegimos $N>|x|+1/\varepsilon$. Si $n\ge N$, $|x-n|\ge n-|x|>1/\varepsilon$, luego $|1/(x-n)|<\varepsilon$. Así convergen puntualmente a cero en $X$. Los ceros de denominador excluidos no pueden recuperarse sólo porque el error sea pequeño para índices posteriores.

## 26.3. Alternancia dependiente de la entrada

[]{#MA-EX-ANM-01-026-003}

[]{#MA-SOL-ANM-01-026-003}

En $x=2$ todos los valores son0. Para otra entrada, las subsecuencias pares e impares tienen valores constantes $x-2$ y $2-x$, distintos. Si existiese límite de la columna, C06 lo transferiría a ambas y la unicidad lo identificaría con dos números distintos. Por tanto el conjunto de convergencia es $\{2\}$ y la función límite allí vale0. No se afirma convergencia en todo $\mathbb R$.

## 26.4. Grafo del límite

[]{#MA-EX-ANM-01-026-004}

[]{#MA-SOL-ANM-01-026-004}

Formamos el subconjunto $G=\{(x,y)\in X\times\mathbb R:f_n(x)\to y\}$. La hipótesis da al menos una salida en cada fibra y C06 da a lo sumo una. Por la definición de función de C12, $G$ es el grafo de una función $X\to\mathbb R$. Es una regla de salida única, no una aplicación del principio de selección entre varias salidas. Para $X$ vacío se obtiene el grafo vacío.

## 26.5. Toda entrada salvo una

[]{#MA-EX-ANM-01-026-005}

[]{#MA-SOL-ANM-01-026-005}

Para $x\notin\mathbb N$ la columna es siempre0. Si $x=m\in\mathbb N$, sólo el índice $m$ vale1; desde $N=m+1$ todos los términos son0. Por tanto el límite puntual es cero en toda la recta. Cada fila tiene un punto de altura1, pero una entrada fija encuentra como máximo uno. Una cantidad finita de gráficas no acredita las colas de todas las entradas; la clasificación anterior sí.

## 26.6. Certificado explícito

[]{#MA-EX-ANM-01-026-006}

[]{#MA-SOL-ANM-01-026-006}

[]{#MA-SEC-ANM-01-026-002}

Fijamos $x$ y $\varepsilon>0$ y elegimos un natural $N>(x^2+1)/\varepsilon$, por arquimedianidad. Para cualquier $n\ge N$, $(x^2+1)/(n+1)\le(x^2+1)/(N+1)<\varepsilon$. El numerador es positivo y el denominador también. El corte depende legítimamente de ambos desafíos y controla toda la cola.

## 26.7. Negar en el orden correcto

[]{#MA-EX-ANM-01-026-007}

[]{#MA-SOL-ANM-01-026-007}

La negación es $\exists x\in X\,\exists\varepsilon_0>0\,\forall N\,\exists n\ge N:\ |f_n(x)-f(x)|\ge\varepsilon_0$. Tomamos cualquier entrada del dominio no vacío y $\varepsilon_0=1/2$. Para cada $N$ sirve $n=N$, pues el error es1. Esa entrada no cambia con el corte. Además no hay otro límite real: las subsecuencias constantes1 y−1 lo refutarían por unicidad.

## 26.8. Un infractor móvil

[]{#MA-EX-ANM-01-026-008}

[]{#MA-SOL-ANM-01-026-008}

Dado $N$, usamos el índice $n=N$ y la entrada $x=N+1$. Entonces $f_N(x)=1$ y el error respecto del límite cero es1. Con tolerancia1/2 se refuta que exista un corte que controle simultáneamente todas las entradas. La entrada depende del corte, por lo que no se refuta la convergencia puntual, ya demostrada mediante $N(x,\varepsilon)>|x|/\varepsilon$.

**Retorno visual.** Véase [C26-F02](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.9. Reunión finita de obligaciones

[]{#MA-EX-ANM-01-026-009}

[]{#MA-SOL-ANM-01-026-009}

Un natural $N>5/\varepsilon$ funciona porque $|x|\le5$ en $A$ y $|f_n(x)|\le5/(N+1)<\varepsilon$. Para una familia puntual arbitraria en un conjunto finito, se toman los cortes de cada una de sus entradas para la misma tolerancia y su máximo finito. Ese máximo domina todas las obligaciones de cola. En el vacío sirve0. No se generaliza tomando un máximo infinito sin demostrar que existe.

## 26.10. Umbral mínimo

[]{#MA-EX-ANM-01-026-010}

[]{#MA-SOL-ANM-01-026-010}

Pongamos $r=|x|/\varepsilon\ge0$. Como los errores decrecen, un índice $N$ es válido exactamente cuando $N+1>r$. Si $r=0$, el mínimo es0. Para $r>0$, el piso de C06 satisface $\lfloor r\rfloor\le r<\lfloor r\rfloor+1$, y $N=\lfloor r\rfloor$ es válido. Un natural menor tiene $N+1\le\lfloor r\rfloor\le r$ y falla. Así $\tau=\lfloor r\rfloor$ también para $r=0$ con piso0. Cuando $r$ es entero positivo, bajar un índice deja error exactamente $\varepsilon$, que no basta.

## 26.11. Dos errores y una cota

[]{#MA-EX-ANM-01-026-011}

[]{#MA-SOL-ANM-01-026-011}

[]{#MA-SEC-ANM-01-026-003}

Fijamos $x$. La convergencia de $f_n(x)$ entrega una cola con $|f_n(x)|\le B=|f(x)|+1$. En ella el error del producto es como máximo $B|g_n(x)-g(x)|+|g(x)||f_n(x)-f(x)|$. Pedimos errores menores que $\varepsilon/[2(B+1)]$ y $\varepsilon/[2(|g(x)|+1)]$ y tomamos el máximo de esos dos cortes y el corte de acotación. La suma resultante es menor que $\varepsilon$. Cada constante fue fijada después de recibir $x$.

## 26.12. Ceros por filas

[]{#MA-EX-ANM-01-026-012}

[]{#MA-SOL-ANM-01-026-012}

El error respecto de $g(x)=x$ es $1/(n+1)$, que tiende a cero por C06. Cada columna tiene límite positivo y, desde algún corte dependiente de $x$, denominador positivo. Sin embargo, la fila $n$ se anula en $x=1/(n+1)\in X$. Por ello $1/g_n$ no es una función real sobre todo $X$. En $Y=X\setminus\{1/(n+1):n\in\mathbb N\}$ sí están definidas todas las filas y el recíproco converge a $1/x$ por la barrera $|g_n(x)|>x/2$ eventual.

## 26.13. Orden eventual

[]{#MA-EX-ANM-01-026-013}

[]{#MA-SOL-ANM-01-026-013}

Fijamos $x$. Si $d=f(x)-g(x)>0$, elegimos cortes para ambos errores menores que $d/3$ y los reunimos con el corte de orden. En una etapa posterior, $f_n(x)>f(x)-d/3$ y $g_n(x)<g(x)+d/3$, luego $f_n(x)-g_n(x)>d/3>0$, contradicción. Por tanto $f(x)\le g(x)$; la arbitrariedad de $x$ da el orden de funciones. La desigualdad estricta no se hereda necesariamente: $1/(n+1)>0$ converge a0.

## 26.14. Filas acotadas, límite sin cota

[]{#MA-EX-ANM-01-026-014}

[]{#MA-SOL-ANM-01-026-014}

Cada fila cumple $0\le u_n(x)\le n$. Para $x$ fijo, $0\le u_n(x)\le x$ y coincide con $x$ desde cualquier natural mayor que $x$. Así el límite es $u(x)=x$, sin cota superior en el dominio. No hay una barrera común para toda la familia: dado $B$, elegimos un natural $n>B$ y la entrada $x=n$, que da $u_n(n)=n>B$. Acotación fila por fila y columna por columna no producen una constante común.

**Retorno visual.** Véase [C26-F03](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.15. Componer dentro del tipo

[]{#MA-EX-ANM-01-026-015}

[]{#MA-SOL-ANM-01-026-015}

Fijamos $x$. La raíz está definida para $f_n(x)$ y $f(x)$ por no negatividad; C14 demuestra continuidad relativa de la raíz en $[0,\infty)$, incluido0. Para una tolerancia recibimos su radio en el valor $f(x)$; la convergencia puntual da un corte que coloca todos los valores posteriores dentro de ese radio. La continuidad entrega error menor que la tolerancia. Sólo se usó continuidad de la operación exterior, no la de cada fila.

## 26.16. Potencias y extremos

[]{#MA-EX-ANM-01-026-016}

[]{#MA-SOL-ANM-01-026-016}

[]{#MA-SEC-ANM-01-026-004}

En cero todos los términos posteriores al inicial son0; en uno todos son1. Si $0<x<1$, ponemos $t=1/x-1>0$ y la inducción de Bernoulli da $(1+t)^n\ge1+nt$. Por reciprocidad positiva, $x^n\le1/(1+nt)$. Un natural $N>1/(\varepsilon t)$ hace esa cota menor que $\varepsilon$ para todo $n\ge N$. El límite vale0 en $[0,1)$ y1 en el extremo1.

## 26.17. Discontinuidad relativa

[]{#MA-EX-ANM-01-026-017}

[]{#MA-SOL-ANM-01-026-017}

Fijamos tolerancia1/2. Dado $\delta>0$, definimos $d=\min(\delta/2,1/2)>0$ y $y=1-d$. Entonces $y\in[0,1)$, $0<|y-1|=d<\delta$, pero el límite toma valores0 en $y$ y1 en1. El error1 contradice cualquier radio de continuidad relativa. En cualquier centro menor que1, un radio menor que su distancia a1 deja el límite constante0, así que allí sí es continuo.

## 26.18. Una infracción en cada etapa

[]{#MA-EX-ANM-01-026-018}

[]{#MA-SOL-ANM-01-026-018}

Para $s=1/[2(n+1)]\in(0,1)$, la versión de Bernoulli $(1-s)^n\ge1-ns$ da $p_n(x_n)\ge1-n/[2(n+1)]>1/2$. En cada $x_n<1$ el límite vale0, luego hay error mayor que1/2 en todas las etapas, incluso en $n=0$ por $p_0=1$. Ante cualquier corte común, una de esas etapas lo viola. Las entradas varían con $n$; no se viola el contrato puntual.

**Retorno visual.** Véase [C26-F04](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.19. Cambiar el dominio

[]{#MA-EX-ANM-01-026-019}

[]{#MA-SOL-ANM-01-026-019}

En el primer dominio el límite es cero y $x^n\le c^n\le1/[1+n(1/c-1)]$. Un natural $N>1/[\varepsilon(1/c-1)]$ controla todas las entradas. En $[0,1)$ el límite también es cero y continuo, pero la ruta $x_n=1-1/[2(n+1)]$ permanece dentro del dominio y mantiene error mayor que1/2. Así no hay un corte simultáneo para esa tolerancia. El límite continuo no decide el control sobre todo un dominio infinito.

## 26.20. Dominio ampliado

[]{#MA-EX-ANM-01-026-020}

[]{#MA-SOL-ANM-01-026-020}

Para $|x|<1$, la prueba de Bernoulli aplicada a $|x|$ muestra $|x^n|\to0$, incluido el prefijo $p_0=1$. En1 el valor es siempre1. En−1 los valores alternan1 y−1, con subsecuencias constantes distintas; por unicidad no hay límite real. El conjunto de convergencia es $(-1,1]$, con límite0 en $(-1,1)$ y1 en1. Es indispensable revisar el nuevo extremo en lugar de reutilizar sin cambios la conclusión de $[0,1]$.

## 26.21. Capa racional

[]{#MA-EX-ANM-01-026-021}

[]{#MA-SOL-ANM-01-026-021}

[]{#MA-SEC-ANM-01-026-005}

En0 los valores son0. Para $x>0$, el error respecto de1 es $1/[1+(n+1)x]\le1/[(n+1)x]$. Un corte mayor que $1/(\varepsilon x)$ lo controla. El límite es1 para toda entrada positiva y0 en0. Dado cualquier radio $\delta>0$, $y=\min(\delta/2,1/2)>0$ queda a distancia menor que $\delta$ de0 y tiene error1 respecto del valor central. Tolerancia1/2 refuta continuidad.

## 26.22. Dos rutas, dos destinos

[]{#MA-EX-ANM-01-026-022}

[]{#MA-SOL-ANM-01-026-022}

La primera ruta hace $(n+1)x=1$ y la salida es1/2. La segunda hace $(n+1)x=1/(n+1)$ y la salida es1/(n+2), que tiende a0. Ambas entradas tienden a0 y pertenecen a $[0,1]$. No son una columna fija: el contrato puntual sólo controla $a_n(x)$ cuando $x$ permanece fijo al variar $n$. Por ello sus destinos diferentes son compatibles con el límite puntual obtenido.

**Retorno visual.** Véase [C26-F05](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.23. Una escala intermedia

[]{#MA-EX-ANM-01-026-023}

[]{#MA-SOL-ANM-01-026-023}

La raíz positiva de $n+1$ existe y es al menos1, así $w_n\in[0,1]$. Para cualquier $M>0$, elegir $n+1>M^2$ da $\sqrt{n+1}>M$; por ello $w_n\to0$. La salida es $\sqrt{n+1}/[1+\sqrt{n+1}]$, cuyo error respecto de1 es $1/[1+\sqrt{n+1}]$. Esta diferencia tiende a0 por la misma comparación. El destino es1, distinto de los de las dos rutas del ejercicio anterior.

## 26.24. Límites iterados

[]{#MA-EX-ANM-01-026-024}

[]{#MA-SOL-ANM-01-026-024}

Para una fila fija, continuidad en0 y valor0 dan $\lim_{x\to0^+}a_n(x)=0$; el límite en $n$ de esos números es0. Para una entrada positiva fija, el límite en $n$ es1; el límite por $x\to0^+$ de la función constante1 es1. Ambas operaciones iteradas existen y dan valores diferentes. La comparación es legítima porque antes se calculó la existencia de cada límite interior y exterior.

## 26.25. Reparar un prefijo fuera del dominio

[]{#MA-EX-ANM-01-026-025}

[]{#MA-SOL-ANM-01-026-025}

Definimos $x_n=\min(1,c/(n+1))$. Está en $[0,1]$ para todo índice y, desde un natural mayor que $c$, coincide con $c/(n+1)$. La ruta converge a0 por coincidencia eventual con esa sucesión numérica. En la cola, $(n+1)x_n=c$ y $a_n(x_n)=c/(1+c)$. Por transferencia de prefijos finitos, toda la sucesión de salidas converge a ese número. Si se usara la fórmula sin reparación y $c>1$, las primeras entradas podrían estar fuera del dominio.

## 26.26. Tiendas continuas

[]{#MA-EX-ANM-01-026-026}

[]{#MA-SOL-ANM-01-026-026}

[]{#MA-SEC-ANM-01-026-006}

La función afín, el valor absoluto y el máximo mediante $(u+v+|u-v|)/2$ son continuos por C14. La condición positiva equivale a $1<kx<3$, por lo que su región positiva es $(1/k,3/k)$ y en los extremos vale0. En0 es siempre0. Para $x>0$, un corte $N+3>3/x$ hace $kx>3$ en toda la cola y todos sus valores son0. Así el límite puntual es la función cero; el soporte cerrado es $[1/k,3/k]$.

## 26.27. Seguir el centro

[]{#MA-EX-ANM-01-026-027}

[]{#MA-SOL-ANM-01-026-027}

La ruta $z_n=2/(n+3)$ está en $[0,1]$ y tiende a0. En ella $kz_n=2$, por lo que $t_n(z_n)=1$. Sin embargo el límite puntual es cero, continuo, y toda fila satisface $0\le t_n\le1$. Las dos condiciones mencionadas no bastan, ni siquiera junto con continuidad de todas las filas y compactitud del dominio. El testigo es explícito para todos los índices.

## 26.28. Certificar el área

[]{#MA-EX-ANM-01-026-028}

[]{#MA-SOL-ANM-01-026-028}

La continuidad da integrabilidad por C23. El valor fuera de $[1/k,3/k]$ es0. En la primera rama la función es $kx-1$ y en la segunda $3-kx$; ambas tienen anchura $1/k$ y valores extremos0,1 o1,0. Una primitiva cuadrática, o la fórmula afín probada desde C24, da área $1/(2k)$ a cada rama. Restricción y aditividad producen integral $1/k$. Con $k=n+3$, los valores tienden a0, igual a la integral del límite.

## 26.29. Altura que compensa anchura

[]{#MA-EX-ANM-01-026-029}

[]{#MA-SOL-ANM-01-026-029}

Cada columna positiva queda exactamente en cero desde el mismo corte de $t_n$ y la columna de0 siempre vale0. Multiplicar por $n+3$ no cambia esa coincidencia eventual, así $b_n\to0$ puntualmente. Cada fila es continua e integrable. Por linealidad de C23 y el área anterior, $\int_0^1b_n=(n+3)/(n+3)=1$. El límite de esas integrales es1, mientras el límite puntual cero tiene integral0. Ambas integrales comparadas existen y difieren.

**Retorno visual.** Véase [C26-F06](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.30. Pendientes sin constante común

[]{#MA-EX-ANM-01-026-030}

[]{#MA-SOL-ANM-01-026-030}

En los puntos $u_n=1/k$ y $v_n=2/k$ tenemos salidas0 y1, mientras la distancia de entrada es1/k. Una cota común $|t_n(u)-t_n(v)|\le L|u-v|$ obligaría a $1\le L/k$, esto es $k\le L$, para todos $k=n+3$. La arquimedianidad permite elegir uno mayor que $L$, contradicción. Cada fila sí tiene constante $k$, pero esa dependencia del índice es exactamente la obstrucción.

## 26.31. Límite sin integral propia

[]{#MA-EX-ANM-01-026-031}

[]{#MA-SOL-ANM-01-026-031}

[]{#MA-SEC-ANM-01-026-007}

Cada $E_{n+1}$ es finito; su indicadora es integrable con integral0. En un irracional, toda la columna vale0. En un racional irreducible $p/q$, vale1 desde $n+1\ge q$. El límite es Dirichlet, no integrable por C25. Por tanto el límite de las integrales sí existe y vale0, pero no se puede igualar con una integral de Riemann del límite: esa integral no existe. La acotación común0≤d_n≤1 no repara la falta de existencia.

## 26.32. Calcular las derivadas

[]{#MA-EX-ANM-01-026-032}

[]{#MA-SOL-ANM-01-026-032}

Pongamos $k=n+1>0$. Cociente y potencia de C18 dan $h_n^{\prime}=(1-kx^2)/(1+kx^2)^2$. En0 los valores son0 y las derivadas1. Para $x\ne0$, $|h_n(x)|\le1/(k|x|)\to0$ y $|h_n^{\prime}(x)|\le1/(1+kx^2)\to0$. Los cortes arquimedianos para esos denominadores controlan cada cola. Así $h_n\to0$ y $h_n^{\prime}\to\mathbf1_{\{0\}}$ puntualmente. La derivada del límite cero es0 y difiere del límite de derivadas en0.

## 26.33. Un máximo exacto de error

[]{#MA-EX-ANM-01-026-033}

[]{#MA-SOL-ANM-01-026-033}

Con $k=n+1$, el cuadrado $(\sqrt{k}|x|-1)^2\ge0$ equivale a $1+kx^2\ge2\sqrt{k}|x|$. Si $x\ne0$, dividir por los factores positivos da la cota; en0 se verifica directamente. Para $x=1/\sqrt{k}$, el denominador es2 y el valor absoluto es1/(2√k), por lo que es el máximo. La cota tiende a0, pero las derivadas en0 siguen valiendo1. El control global de valores por sí solo no autoriza el intercambio de derivadas.

**Retorno visual.** Véase [C26-F07](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.34. Auditar la prueba triangular

[]{#MA-EX-ANM-01-026-034}

[]{#MA-SOL-ANM-01-026-034}

La desigualdad $|f(y)-f(x)|\le|f(y)-f_n(y)|+|f_n(y)-f_n(x)|+|f_n(x)-f(x)|$ es válida. El corte puntual en $x$ controla el último término y continuidad de la fila escogida controla el central en una ventana. Falta controlar el primero para todos los $y$ de esa ventana usando la misma fila: el corte puntual en $y$ puede depender de $y$ y ser mayor que el ya escogido. Las potencias demuestran que esa omisión puede llevar a una conclusión falsa.

## 26.35. Clasificar tres fracasos

[]{#MA-EX-ANM-01-026-035}

[]{#MA-SOL-ANM-01-026-035}

Las potencias tienen filas continuas y límite puntual existente pero discontinuo. Las tiendas normalizadas tienen filas continuas integrables y límite cero integrable; el límite de integrales1 difiere de la integral del límite0. En $d_n$, las filas son integrables con integral0, pero el límite Dirichlet no tiene integral propia; no hay dos valores integrales que comparar. El ejemplo $h_n$ aporta además derivadas puntualmente convergentes que no coinciden con la derivada del límite. Cada afirmación conserva sus hipótesis y su alcance.

## 26.36. Transportar una cota común de proximidad

[]{#MA-EX-ANM-01-026-036}

[]{#MA-SOL-ANM-01-026-036}

[]{#MA-SEC-ANM-01-026-008}

Fijamos $x,y$. Las diferencias numéricas convergen a $f(x)-f(y)$ y sus magnitudes convergen por continuidad del absoluto. El orden eventual aplicado a $|f_n(x)-f_n(y)|\le L|x-y|$ da la misma desigualdad para $f$. Para una tolerancia, $\delta=\varepsilon/(L+1)>0$ hace $L|x-y|<\varepsilon$ si $|x-y|<\delta$. En $L=0$ el error es0 para todos los pares; no se divide por $L$.

## 26.37. Diagonal con presupuesto común

[]{#MA-EX-ANM-01-026-037}

[]{#MA-SOL-ANM-01-026-037}

La desigualdad triangular y la cota común dan $|f_n(x_n)-f(x)|\le L|x_n-x|+|f_n(x)-f(x)|$. Para $\varepsilon>0$ reunimos el corte de la ruta con error menor que $\varepsilon/[2(L+1)]$ y el corte puntual en $x$ con error menor que $\varepsilon/2$. Todo índice posterior da error menor que $\varepsilon$. La constante fue común antes de recibir los índices; la ruta está dada y no requiere selección.

## 26.38. Monotonía sin barrera universal

[]{#MA-EX-ANM-01-026-038}

[]{#MA-SOL-ANM-01-026-038}

Para cada $x$, la imagen $\{f_n(x):n\in\mathbb N\}$ es no vacía y tiene cota superior real por hipótesis. C03 da su supremo $s_x$, único. Dada $\varepsilon>0$, algún $j$ cumple $f_j(x)>s_x-\varepsilon$, pues de otro modo ese número sería cota superior. Para $n\ge j$, monotonía da $s_x-\varepsilon<f_n(x)\le s_x$. Esto prueba convergencia. El grafo de los supremos únicos define la función sin elegir arbitrariamente una cota para cada entrada. No se obtiene acotación global del límite.

## 26.39. Monotonía del índice y de la variable

[]{#MA-EX-ANM-01-026-039}

[]{#MA-SOL-ANM-01-026-039}

En $X=[-1,1]$ usamos $f_n(x)=x^2-1/(n+1)$. Para toda entrada fija, el término sustraído disminuye al aumentar el índice, luego la columna aumenta y converge a $x^2$. Cada fila toma el mismo valor en−1 y1 y un valor estrictamente menor en0; por ello no es creciente ni decreciente respecto de $x$ en todo el dominio. La cota superior por columna es $x^2$ y existe además una barrera común de magnitud1. Los dos argumentos ordenados no se pueden intercambiar.

## 26.40. Un certificado y su límite de alcance

[]{#MA-EX-ANM-01-026-040}

[]{#MA-SOL-ANM-01-026-040}

El error respecto de $f(x)=x$ es $1/(n+1)$; el corte de C06 sirve para cualquier entrada. Para todo par, $|f_n(u)-f_n(v)|=|u-v|$, así $L=1$ común. Una ruta dada $x_n\to x$ cumple $|f_n(x_n)-x|\le|x_n-x|+1/(n+1)\to0$. Las tiendas también tienen límite continuo y filas continuas, pero sus pendientes exigen constantes $n+3$ sin barrera común; su ruta central mantiene salida1. La prueba positiva identifica una hipótesis concreta que el contraejemplo no satisface.

**Retorno visual.** Véase [C26-F08](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-microcontroles.html)
