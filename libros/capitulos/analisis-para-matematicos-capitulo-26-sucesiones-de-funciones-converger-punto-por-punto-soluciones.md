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
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C26_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html)

## 26.1. Fila y columna

[]{#MA-EX-ANM-01-026-001}

[]{#MA-SOL-ANM-01-026-001}

[]{#MA-SEC-ANM-01-026-001}

La fila $n$ es $f_n:x\mapsto(n+1)x$ sobre $\mathbb R$; la columna $x$ es la sucesión $((n+1)x)_{n\ge0}$. En $x=0$ todos los valores son cero. Si $x\ne0$, sus magnitudes $(n+1)|x|$ exceden cualquier $M>0$ desde un índice con $n+1>M/|x|$. La columna es entonces no acotada y no puede converger a un real, pues C06 hace acotada toda sucesión convergente. Para $x>0$ crece sin cota superior y para $x<0$ decrece sin cota inferior. El conjunto de convergencia real es exactamente $\{0\}$ y la función límite sobre él vale cero.

**Retorno visual.** Véase [C26-F01](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.2. El dominio que se conserva

[]{#MA-EX-ANM-01-026-002}

[]{#MA-SOL-ANM-01-026-002}

Como los índices son $\mathbb N=\{0,1,2,\ldots\}$, la intersección de los dominios es $X=\mathbb R\setminus\mathbb N$. En ese conjunto cada denominador $x-n$ es no nulo para todo índice. Fijados $x\in X$ y $\varepsilon>0$, elegimos un natural $N>|x|+1/\varepsilon$. Para $n\ge N$, la triangular inversa da $|x-n|\ge n-|x|>1/\varepsilon$, así $|1/(x-n)|<\varepsilon$. Las restricciones convergen puntualmente a cero en $X$. Éste es el mayor dominio común de las fórmulas dadas; podrían elegirse subconjuntos suyos, pero incluir un natural exigiría declarar cómo se repara su fila singular.

## 26.3. Alternancia dependiente de la entrada

[]{#MA-EX-ANM-01-026-003}

[]{#MA-SOL-ANM-01-026-003}

En $x=2$ todos los valores de la columna son cero. Para $x\ne2$, los índices pares tienen altura $x-2$ y los impares altura $2-x$. Si hubiera un límite real, ambas subsucesiones deberían converger a él por C06. Son constantes y sus valores son distintos, de modo que la unicidad lo hace imposible. El conjunto de convergencia es $\{2\}$ y la función límite allí vale cero. La alternancia no depende de una etapa inicial excepcional: sigue produciendo ambos valores en índices arbitrariamente tardíos.

## 26.4. Grafo del límite

[]{#MA-EX-ANM-01-026-004}

[]{#MA-SOL-ANM-01-026-004}

Definimos $G=\{(x,y)\in X\times\mathbb R:f_n(x)\to y\}$. La hipótesis de convergencia de cada columna proporciona al menos un $y$ para cada entrada. La unicidad del límite numérico proporciona a lo sumo uno. Por tanto $G$ es total y univaluada sobre $X$, y define una función $f:X\to\mathbb R$. La salida está determinada por una propiedad que tiene un único valor, sin elegir entre alternativas por entrada. Si $X$ es vacío, el mismo procedimiento produce el único grafo vacío.

## 26.5. Toda entrada salvo una

[]{#MA-EX-ANM-01-026-005}

[]{#MA-SOL-ANM-01-026-005}

Si $x\notin\mathbb N$, ninguna fila tiene su pico en esa entrada y la columna es cero desde el inicio. Si $x=m\in\mathbb N$, el único término de altura uno es el de índice $m$; desde $N=m+1$ toda la cola es cero. Así $f_n(x)\to0$ para cada $x\in\mathbb R$. Cada fila contiene un pico de altura uno, pero éste aparece en una entrada diferente al aumentar el índice. El argumento clasifica una entrada arbitraria y controla su cola completa; unas pocas gráficas no certificarían esa afirmación universal.

## 26.6. Certificado explícito

[]{#MA-EX-ANM-01-026-006}

[]{#MA-SOL-ANM-01-026-006}

[]{#MA-SEC-ANM-01-026-002}

Fijamos $x\in\mathbb R$ y $\varepsilon>0$. El numerador $x^2+1$ es positivo. Por arquimedianidad elegimos un natural $N>(x^2+1)/\varepsilon$. Para cualquier $n\ge N$, se tiene $0<(x^2+1)/(n+1)\le(x^2+1)/(N+1)<\varepsilon$. El corte sirve para toda la cola y depende sólo de los desafíos recibidos, la entrada y la tolerancia. Se obtiene convergencia puntual a cero en toda la recta.

## 26.7. Negar en el orden correcto

[]{#MA-EX-ANM-01-026-007}

[]{#MA-SOL-ANM-01-026-007}

La negación hacia una candidata fija $f$ es $\exists x\in X\ \exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists n\ge N:\ |f_n(x)-f(x)|\ge\varepsilon_0$. Para la candidata cero y $f_n(x)=(-1)^n$, fijamos cualquier entrada del dominio no vacío y $\varepsilon_0=1/2$. Ante cada corte $N$, el índice $n=N$ tiene error uno, así infringe la obligación. La entrada permanece fija y la refutación sí es puntual. La familia tampoco converge a otra candidata real en esa entrada, porque las subsucesiones constantes uno y menos uno no podrían compartir un límite.

## 26.8. Un infractor móvil

[]{#MA-EX-ANM-01-026-008}

[]{#MA-SOL-ANM-01-026-008}

El límite puntual es cero: para cada entrada fija, un corte $N>|x|/\varepsilon$ controla $|x|/(n+1)$ en toda la cola. Para refutar un corte simultáneo, fijamos tolerancia $1/2$. Ante cualquier $N$, tomamos $n=N$ y $x=N+1$, obteniendo $|f_N(x)|=1$. Se demuestra $\forall N\ \exists x\ \exists n\ge N$ con error grande. La entrada se elige después del corte, de modo que esa afirmación no es la negación del contrato puntual, cuyo infractor tendría que ser una misma entrada para todos los cortes.

**Retorno visual.** Véase [C26-F02](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.9. Reunión finita de obligaciones

[]{#MA-EX-ANM-01-026-009}

[]{#MA-SOL-ANM-01-026-009}

En $A=\{-3,0,5\}$, todas las magnitudes de entrada están acotadas por cinco. Un natural $N>5/\varepsilon$ da, para todo $n\ge N$ y todo $x\in A$, $|f_n(x)|\le5/(N+1)<\varepsilon$. Para una familia puntualmente convergente cualquiera sobre un conjunto finito, la tolerancia fija proporciona un corte por cada entrada. Se construye esa lista finita de cortes y se toma su máximo; cualquier índice posterior cumple todas las obligaciones. En el vacío sirve cero. La extensión a infinitas entradas necesitaría demostrar que sus umbrales tienen una barrera natural común.

## 26.10. Umbral mínimo

[]{#MA-EX-ANM-01-026-010}

[]{#MA-SOL-ANM-01-026-010}

Sea $r=|x|/\varepsilon\ge0$. Como el error $|x|/(n+1)$ no aumenta con $n$, un corte $N$ es válido exactamente cuando $N+1>r$. Ponemos $m=\lfloor r\rfloor$, caracterizado por $m\le r<m+1$. El corte $N=m$ cumple la desigualdad estricta. Si un natural $N<m$, entonces $N+1\le m\le r$, de modo que ya el error en ese índice es al menos $\varepsilon$ y falla. Por tanto $\tau(x,\varepsilon)=\lfloor|x|/\varepsilon\rfloor$, incluido $x=0$, donde el mínimo es cero. Cuando $r$ es un entero positivo, el índice anterior da error exactamente igual a $\varepsilon$, que no satisface el contrato estricto.

## 26.11. Dos errores y una cota

[]{#MA-EX-ANM-01-026-011}

[]{#MA-SOL-ANM-01-026-011}

[]{#MA-SEC-ANM-01-026-003}

Fijamos una entrada $x$ y abreviamos $f(x)=a$, $g(x)=b$. La convergencia de la primera columna da un corte de acotación con $|f_n(x)|\le B=|a|+1$. Usamos la identidad $f_ng_n-ab=f_n(g_n-b)+b(f_n-a)$. Su magnitud no supera $B|g_n-b|+|b||f_n-a|$. Pedimos a la segunda columna error menor que $\varepsilon/[2(B+1)]$ y a la primera menor que $\varepsilon/[2(|b|+1)]$. El máximo de esos dos cortes y el de acotación garantiza que la suma anterior es menor que $\varepsilon$, pues cada coeficiente sobre su denominador más uno es menor que uno. La entrada era arbitraria, así el producto converge puntualmente a $fg$. No se necesitó una cota global de las familias.

## 26.12. Ceros por filas

[]{#MA-EX-ANM-01-026-012}

[]{#MA-SOL-ANM-01-026-012}

Para $x\in(0,1]$, $|g_n(x)-x|=1/(n+1)\to0$, así el límite puntual es $g(x)=x>0$. Sin embargo, cada fila se anula en $x_n=1/(n+1)$, que pertenece al dominio. Por eso $1/g_n$ no define una función real en todo $X$ en ninguna etapa. Un dominio común posible para los recíprocos es $Y=X\setminus\{1/(n+1):n\in\mathbb N\}$. En una entrada fija de $Y$, desde un corte con $1/(n+1)<x/2$ tenemos $g_n(x)>x/2$. Entonces $|1/g_n(x)-1/x|=|x-g_n(x)|/(x|g_n(x)|)\le2/[x^2(n+1)]\to0$. La barrera eventual justifica el límite, mientras la restricción común justifica la existencia de todas las filas.

## 26.13. Orden eventual

[]{#MA-EX-ANM-01-026-013}

[]{#MA-SOL-ANM-01-026-013}

Fijemos $x$ y supongamos por contradicción que $d=f(x)-g(x)>0$. Reunimos los cortes para errores menores que $d/3$ de ambas columnas y el corte a partir del que se cumple su orden. En cualquier índice posterior, $f_n(x)>f(x)-d/3$ y $g_n(x)<g(x)+d/3$, así $f_n(x)-g_n(x)>d-2d/3=d/3>0$. Esto contradice $f_n(x)\le g_n(x)$. Por tanto $f(x)\le g(x)$ para toda entrada. La estrictitud no pasa automáticamente: las columnas $1/(n+1)>0$ y cero tienen el mismo límite cero.

## 26.14. Filas acotadas, límite sin cota

[]{#MA-EX-ANM-01-026-014}

[]{#MA-SOL-ANM-01-026-014}

Para cada $n$, la fila $u_n$ satisface $0\le u_n(x)\le n$ en todo $[0,\infty)$, así está acotada. Para cada entrada fija $x$, su columna satisface $0\le u_n(x)\le x$ y desde cualquier natural $N>x$ coincide con $x$. Por tanto su límite es $u(x)=x$. Esta función no tiene cota superior en todo el dominio. Tampoco hay una barrera común para toda la familia: dado $B\ge0$, elegimos un natural $n>B$ y tomamos $x=n$, obteniendo $u_n(n)=n>B$. Las cotas por filas y por columnas son válidas, pero dependen de argumentos diferentes y ninguna proporciona esa barrera global.

**Retorno visual.** Véase [C26-F03](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.15. Componer dentro del tipo

[]{#MA-EX-ANM-01-026-015}

[]{#MA-SOL-ANM-01-026-015}

Para una entrada fija, escribimos $u_n=f_n(x)\ge0$ y $u=f(x)\ge0$. Sus raíces reales están definidas. Si $u_n\ge u$, la diferencia de raíces es no negativa y $u_n-u=(\sqrt{u_n}-\sqrt u)(\sqrt{u_n}+\sqrt u)\ge(\sqrt{u_n}-\sqrt u)^2$. Intercambiar los dos valores cubre el orden inverso, así $|\sqrt{u_n}-\sqrt u|^2\le|u_n-u|$. Para $\varepsilon>0$, la convergencia de la columna da una cola con $|u_n-u|<\varepsilon^2$, luego el error de raíces es menor que $\varepsilon$. Esto también cubre $u=0$. Sólo se usa el control de la columna y la operación raíz, sin continuidad de las filas.

## 26.16. Potencias y extremos

[]{#MA-EX-ANM-01-026-016}

[]{#MA-SOL-ANM-01-026-016}

[]{#MA-SEC-ANM-01-026-004}

La recurrencia declara $p_0=1$. En cero, $p_n(0)=0$ para $n\ge1$, así el límite es cero; en uno, todos los términos son uno. Si $0<x<1$, ponemos $t=1/x-1>0$. Bernoulli, probado por inducción, da $(1+t)^n\ge1+nt$, luego $0<p_n(x)=x^n\le1/(1+nt)$. Para $\varepsilon>0$, un natural $N>1/(\varepsilon t)$ hace esta cota menor que $\varepsilon$ para todos los índices posteriores. Por tanto el límite puntual vale cero en $[0,1)$ y uno en el extremo uno. La prueba mantiene la entrada fija y no usa logaritmos.

## 26.17. Discontinuidad relativa

[]{#MA-EX-ANM-01-026-017}

[]{#MA-SOL-ANM-01-026-017}

Sea $p$ el límite, con $p(1)=1$ y $p(y)=0$ para $y<1$. Fijamos tolerancia $1/2$. Para cualquier $\delta>0$, tomamos $d=\min(\delta/2,1/2)>0$ y $y=1-d$. Entonces $y\in[0,1)$ y $0<|y-1|=d<\delta$, pero $|p(y)-p(1)|=1$. Ningún radio cumple continuidad relativa en uno. En un centro $x<1$, en cambio, un radio menor que $1-x$ evita el punto excepcional y deja la función constante cero. La discontinuidad nueva está exactamente en el extremo uno.

## 26.18. Una infracción en cada etapa

[]{#MA-EX-ANM-01-026-018}

[]{#MA-SOL-ANM-01-026-018}

Para cada $n\ge0$, la entrada $x_n=1-1/[2(n+1)]$ está entre cero y uno. La versión de Bernoulli $(1-s)^n\ge1-ns$ para $0\le s\le1$ da $p_n(x_n)\ge1-n/[2(n+1)]=(n+2)/[2(n+1)]>1/2$; para $n=0$ la fila inicial vale uno. Como el límite en $x_n<1$ es cero, el error supera $1/2$ en cada etapa. Ante cualquier corte común sirve la infracción de esa misma etapa. Sin embargo, las entradas varían con el índice y se aproximan a uno. El resultado refuta control simultáneo en todo el dominio, conservando la convergencia de cada columna fija.

**Retorno visual.** Véase [C26-F04](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.19. Cambiar el dominio

[]{#MA-EX-ANM-01-026-019}

[]{#MA-SOL-ANM-01-026-019}

En $[0,c]$, con $0<c<1$, el límite puntual es cero. Para $n\ge1$ y todas las entradas de ese segmento, $p_n(x)\le c^n\le1/[1+n(1/c-1)]$. Un natural $N>1/[\varepsilon(1/c-1)]$, también positivo, controla toda la cola y todas las entradas a la vez. En $[0,1)$, el límite sigue siendo cero, pero las entradas $x_n=1-1/[2(n+1)]$ pertenecen al dominio y tienen error mayor que $1/2$ en cada etapa. Allí no existe un corte simultáneo para esa tolerancia. La candidata es continua en ambos dominios; la pérdida de separación respecto del borde uno cambia el control global.

## 26.20. Dominio ampliado

[]{#MA-EX-ANM-01-026-020}

[]{#MA-SOL-ANM-01-026-020}

Si $|x|<1$, para $n\ge1$ tenemos $|p_n(x)|=|x|^n$. La prueba geométrica anterior aplicada a $|x|$ da límite cero, con el caso $x=0$ tratado por la recurrencia. En $x=1$, todos los valores son uno. En $x=-1$, las subsucesiones pares e impares son constantes uno y menos uno, así la columna no tiene límite real. Por tanto el conjunto de convergencia en $[-1,1]$ es $(-1,1]$. La función límite sobre él vale cero en $(-1,1)$ y uno en el extremo uno. La familia no converge puntualmente en todo el dominio ampliado porque falla la nueva columna de menos uno.

## 26.21. Capa racional

[]{#MA-EX-ANM-01-026-021}

[]{#MA-SOL-ANM-01-026-021}

[]{#MA-SEC-ANM-01-026-005}

Los denominadores son al menos uno en $[0,1]$, así cada fila está definida y es continua. En cero, $a_n(0)=0$ para todo $n$. Para una entrada fija $x>0$, $|a_n(x)-1|=1/[1+(n+1)x]\le1/[(n+1)x]$. Un natural $N>1/(\varepsilon x)$ controla este error en toda la cola. El límite $a$ vale cero en cero y uno en las entradas positivas. Con tolerancia $1/2$, ante cualquier $\delta>0$ tomamos $y=\min(\delta/2,1/2)>0$; pertenece al dominio, queda a distancia menor que $\delta$ del origen y tiene $|a(y)-a(0)|=1$. Así el límite no es continuo relativamente en cero.

## 26.22. Dos rutas, dos destinos

[]{#MA-EX-ANM-01-026-022}

[]{#MA-SOL-ANM-01-026-022}

Ambas rutas permanecen en $[0,1]$ y tienden a cero. En la primera, $(n+1)/(n+1)=1$, así $a_n(1/(n+1))=1/2$ para todo índice. En la segunda, el producto de escala es $1/(n+1)$ y $a_n(1/(n+1)^2)=[1/(n+1)]/[1+1/(n+1)]=1/(n+2)\to0$. Sus destinos de salida son, por tanto, distintos. El límite puntual fija $x$ antes de variar $n$; ninguna de estas rutas es una columna fija. Sus resultados muestran cómo la elección simultánea de entrada e índice puede retener comportamientos que el contrato puntual no controla.

**Retorno visual.** Véase [C26-F05](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.23. Una escala intermedia

[]{#MA-EX-ANM-01-026-023}

[]{#MA-SOL-ANM-01-026-023}

Como $n+1\ge1$, existe su raíz positiva y satisface $\sqrt{n+1}\ge1$, así $w_n=1/\sqrt{n+1}\in(0,1]$. Para cualquier $\varepsilon>0$, desde $n+1>1/\varepsilon^2$ se tiene $w_n<\varepsilon$, por lo que la ruta tiende a cero. Usando $n+1=(\sqrt{n+1})^2$, el producto $(n+1)w_n$ es $\sqrt{n+1}$. Entonces $a_n(w_n)=\sqrt{n+1}/(1+\sqrt{n+1})$ y su error respecto de uno es $1/(1+\sqrt{n+1})\le w_n\to0$. El destino de esta escala intermedia es uno.

## 26.24. Límites iterados

[]{#MA-EX-ANM-01-026-024}

[]{#MA-SOL-ANM-01-026-024}

Fijado $n$, la fila es continua en cero y su valor allí es cero. Por tanto $\lim_{x\to0^+}a_n(x)=0$, y el límite en $n$ de esa sucesión constante es cero. En el orden contrario, para cada entrada positiva fija ya se probó $\lim_{n\to\infty}a_n(x)=1$. La función resultante sobre $(0,1]$ es constante uno, así su límite por $x\to0^+$ es uno. Las dos operaciones iteradas existen y dan $\lim_n\lim_{x\to0^+}a_n(x)=0$ y $\lim_{x\to0^+}\lim_n a_n(x)=1$. Su diferencia muestra que el orden de operaciones no puede intercambiarse con la sola convergencia puntual.

## 26.25. Reparar un prefijo fuera del dominio

[]{#MA-EX-ANM-01-026-025}

[]{#MA-SOL-ANM-01-026-025}

Para $c>0$, definimos $x_n=\min(1,c/(n+1))$. Cada entrada pertenece a $(0,1]$. Elegimos un natural $N>c$; para $n\ge N$, se tiene $c/(n+1)<1$ y la ruta coincide con la fórmula requerida. Esa cola tiende a cero, así toda la ruta también. En ella $(n+1)x_n=c$ y $a_n(x_n)=c/(1+c)$ exactamente. Las salidas iniciales pueden ser distintas, pero su prefijo finito no cambia el límite $c/(1+c)$. La reparación permite evaluar todas las etapas aunque $c>1$.

## 26.26. Tiendas continuas

[]{#MA-EX-ANM-01-026-026}

[]{#MA-SOL-ANM-01-026-026}

[]{#MA-SEC-ANM-01-026-006}

Con $k=n+3\ge3$, la composición afín $kx-2$, su valor absoluto y el máximo con cero son continuos, por las reglas de C14. Por tanto $t_n$ es continua en $[0,1]$. Su altura es positiva si y sólo si $|kx-2|<1$, equivalente a $1/k<x<3/k$; en los dos extremos vale cero y fuera también. El soporte cerrado es $[1/k,3/k]\subseteq[0,1]$. En cero toda columna vale cero. Para $x>0$ fijo, elegimos $N$ con $N+3>3/x$; desde ese corte $(n+3)x>3$ y todos los términos son cero. Así $t_n\to0$ puntualmente, por coincidencia eventual exacta en cada entrada.

## 26.27. Seguir el centro

[]{#MA-EX-ANM-01-026-027}

[]{#MA-SOL-ANM-01-026-027}

Tomamos $z_n=2/(n+3)$, que pertenece a $[0,1]$ y tiende al origen. En esa entrada, $(n+3)z_n=2$, así $t_n(z_n)=\max(0,1-0)=1$ para toda etapa. El límite puntual es la función cero y es continuo; todas las filas son continuas y comparten la cota $0\le t_n\le1$ en el dominio compacto. Aun así, la ruta central mantiene salidas uno, distintas de la salida cero del límite en su destino de entrada. Las condiciones mencionadas no aportan un control común de cómo varían las filas con la entrada.

## 26.28. Certificar el área

[]{#MA-EX-ANM-01-026-028}

[]{#MA-SOL-ANM-01-026-028}

La continuidad de $t_n$ en el cerrado prueba primero su integrabilidad por C23. Fuera del soporte su integral es cero. En $[1/k,2/k]$ vale $kx-1$, y en $[2/k,3/k]$ vale $3-kx$. Ambas ramas tienen anchura $1/k$ y alturas extremas cero y uno en orden inverso. La fórmula afín por sumas de C22 da integral $1/(2k)$ en cada rama. Restricción y aditividad producen $\int_0^1t_n=1/k=1/(n+3)$. Estos valores tienden a cero, coincidiendo en este ejemplo con la integral del límite puntual nulo. La igualdad se ha calculado para la familia dada, sin asumir un teorema general de intercambio.

## 26.29. Altura que compensa anchura

[]{#MA-EX-ANM-01-026-029}

[]{#MA-SOL-ANM-01-026-029}

Definimos $b_n=(n+3)t_n=kt_n$. Cada columna de $t_n$ es exactamente cero en una cola; multiplicar su altura por $k$ conserva ese hecho, así $b_n\to0$ puntualmente. Cada fila es continua e integrable. Por linealidad y la cuenta anterior, $\int_0^1b_n=k\int_0^1t_n=k/k=1$. La sucesión de integrales tiene límite uno, mientras la función límite cero es integrable con valor cero. Existen las dos operaciones comparadas y dan valores distintos. Aquí el aumento de altura compensa la contracción del soporte.

**Retorno visual.** Véase [C26-F06](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.30. Pendientes sin constante común

[]{#MA-EX-ANM-01-026-030}

[]{#MA-SOL-ANM-01-026-030}

Para cualquier índice, ponemos $u_n=1/k$ y $v_n=2/k$, con $k=n+3$. Ambas entradas pertenecen al dominio y sus alturas son $t_n(u_n)=0$ y $t_n(v_n)=1$. Si existiera una constante Lipschitz común $L\ge0$, tendría que cumplirse $1=|t_n(v_n)-t_n(u_n)|\le L|v_n-u_n|=L/k$, luego $k\le L$ para todo índice. Arquimedianidad proporciona $n$ con $n+3>L$, contradicción. Cada fila sí tiene constante $k$, pues el absoluto y el máximo con cero no aumentan diferencias y la función afín tiene pendiente $k$. Lo que falta es una barrera independiente de la etapa.

## 26.31. Límite sin integral propia

[]{#MA-EX-ANM-01-026-031}

[]{#MA-SOL-ANM-01-026-031}

[]{#MA-SEC-ANM-01-026-007}

El conjunto $E_{n+1}$ es finito y su indicadora es una modificación finita de la tasa cero. Por tanto cada $d_n$ es integrable con valor cero. En los irracionales todas sus columnas son cero; en un racional reducido de denominador $q$ la columna vale uno desde $n+1\ge q$. El límite puntual es Dirichlet, que C25 probó no integrable. Así $\lim_n\int_0^1d_n=0$ existe, pero $\int_0^1\lim_n d_n$ no es un valor real definido como integral propia de Riemann. No hay dos valores integrales que comparar en ese caso. La cota común entre cero y uno no asegura la integrabilidad del límite.

## 26.32. Calcular las derivadas

[]{#MA-EX-ANM-01-026-032}

[]{#MA-SOL-ANM-01-026-032}

Escribimos $k=n+1>0$. El denominador $1+kx^2$ es positivo en toda la recta, y la regla del cociente da $h_n'(x)=[(1+kx^2)-x(2kx)]/(1+kx^2)^2=(1-kx^2)/(1+kx^2)^2$. En cero, $h_n(0)=0$ y $h_n'(0)=1$. Si $x\ne0$, $|h_n(x)|\le1/(k|x|)\to0$. Además $|1-kx^2|\le1+kx^2$, así $|h_n'(x)|\le1/(1+kx^2)\to0$. Cada cota ofrece un corte arquimediano para la entrada fija. Por tanto $h_n\to h=0$ y $h_n'\to g=\mathbf1_{\{0\}}$ puntualmente. La derivada de $h$ es cero y difiere de $g$ en el origen, donde ambas operaciones existen.

## 26.33. Un máximo exacto de error

[]{#MA-EX-ANM-01-026-033}

[]{#MA-SOL-ANM-01-026-033}

Sea $k=n+1$ y $r=\sqrt{k}>0$. El cuadrado $(r|x|-1)^2\ge0$ equivale a $1+kx^2\ge2r|x|$. Para $x\ne0$, dividir por los denominadores positivos da $|h_n(x)|=|x|/(1+kx^2)\le1/(2r)$. En cero el valor es cero y cumple la misma cota. En $x=\pm1/r$, el denominador es dos y la magnitud $1/(2r)$, así la cota se alcanza y es el máximo exacto. Tiende a cero al aumentar el índice y controla todos los valores simultáneamente. Sin embargo $h_n'(0)=1$ para toda etapa, por lo que esa cota global de valores no basta para intercambiar derivadas.

**Retorno visual.** Véase [C26-F07](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 26.34. Auditar la prueba triangular

[]{#MA-EX-ANM-01-026-034}

[]{#MA-SOL-ANM-01-026-034}

La triangular $|f(y)-f(x)|\le|f(y)-f_n(y)|+|f_n(y)-f_n(x)|+|f_n(x)-f(x)|$ es válida. El error puntual en $x$ permite escoger un índice para el último término. La continuidad de esa fila permite elegir un radio que controle el término central para entradas cercanas. El primer término requiere ahora controlar $|f(y)-f_n(y)|$ para todas esas entradas con el mismo índice ya escogido. La convergencia puntual sólo da cortes que pueden depender de $y$ y no proporciona ese control de ventana. Las potencias en $[0,1]$, con filas continuas y límite discontinuo en uno, prueban que la conclusión pretendida puede ser falsa.

## 26.35. Clasificar tres fracasos

[]{#MA-EX-ANM-01-026-035}

[]{#MA-SOL-ANM-01-026-035}

En las potencias sobre $[0,1]$ todas las filas son continuas y el límite puntual existe, pero es discontinuo en uno. En las tiendas normalizadas $b_n$ existen las integrales de todas las filas y del límite nulo; el límite de las primeras es uno y la segunda vale cero. En $d_n=\mathbf1_{E_{n+1}}$, las filas tienen integral cero y límite puntual Dirichlet, pero éste carece de integral propia. Los dos ejemplos integrales fallan de formas distintas: uno da valores desiguales y el otro deja inexistente una operación. Cada afirmación debe conservar esa diferencia de alcance.

## 26.36. Transportar una cota común de proximidad

[]{#MA-EX-ANM-01-026-036}

[]{#MA-SOL-ANM-01-026-036}

[]{#MA-SEC-ANM-01-026-008}

Fijamos $x,y\in X$. La convergencia de sus dos columnas y el álgebra numérica dan $f_n(x)-f_n(y)\to f(x)-f(y)$. La continuidad del absoluto da convergencia de sus magnitudes. Como todas están acotadas por el mismo $L|x-y|$, la preservación del orden produce $|f(x)-f(y)|\le L|x-y|$. Esto vale para todo par, así $f$ es Lipschitz con la misma constante. Para $\varepsilon>0$, tomamos $\delta=\varepsilon/(L+1)>0$. Si $L>0$ y la distancia es menor que $\delta$, el error es menor que $L\varepsilon/(L+1)<\varepsilon$; si $L=0$, es cero. Se obtiene continuidad relativa, incluso uniforme en el dominio.

## 26.37. Diagonal con presupuesto común

[]{#MA-EX-ANM-01-026-037}

[]{#MA-SOL-ANM-01-026-037}

La ruta está dada con $x_n\in X$ y $x_n\to x\in X$. La triangular y la cota común dan $|f_n(x_n)-f(x)|\le|f_n(x_n)-f_n(x)|+|f_n(x)-f(x)|\le L|x_n-x|+|f_n(x)-f(x)|$. Dada $\varepsilon>0$, tomamos el corte de la ruta para error menor que $\varepsilon/[2(L+1)]$ y el corte puntual en $x$ para error menor que $\varepsilon/2$. Su máximo garantiza que la expresión anterior es menor que $\varepsilon$. Para $L=0$ el primer término es cero y el mismo argumento sirve. La constante común controla el cambio de entrada que la convergencia puntual sola dejaba sin resolver.

## 26.38. Monotonía sin barrera universal

[]{#MA-EX-ANM-01-026-038}

[]{#MA-SOL-ANM-01-026-038}

Para cada entrada fija $x$, la imagen de su columna es no vacía y tiene una cota superior real por hipótesis. Completitud proporciona el supremo único $s_x$. Para $\varepsilon>0$, algún índice $j$ satisface $f_j(x)>s_x-\varepsilon$; de otro modo ese número menor sería cota superior. La monotonía por índice mantiene, para $n\ge j$, $s_x-\varepsilon<f_j(x)\le f_n(x)\le s_x$. Por tanto $|f_n(x)-s_x|<\varepsilon$ en toda la cola. Los supremos únicos forman el grafo de la función límite sin seleccionar una cota arbitraria por entrada. No se requiere una barrera común sobre todo $X$, ni se concluye que el límite esté globalmente acotado.

## 26.39. Monotonía del índice y de la variable

[]{#MA-EX-ANM-01-026-039}

[]{#MA-SOL-ANM-01-026-039}

En $X=[-1,1]$, definimos $f_n(x)=x^2-1/(n+1)$. Para cada entrada, $f_{n+1}(x)-f_n(x)=1/[(n+1)(n+2)]>0$, así las columnas son estrictamente crecientes y convergen a $x^2$. Sin embargo, en una fila fija se tiene $f_n(-1)=f_n(1)=1-1/(n+1)$ y $f_n(0)=-1/(n+1)$, estrictamente menor. El orden $-1<0$ refuta que esa fila sea no decreciente, y $0<1$ refuta que sea no creciente. La monotonía por columnas compara etapas distintas; la monotonía respecto de la variable compara entradas distintas de una misma etapa.

## 26.40. Un certificado y su límite de alcance

[]{#MA-EX-ANM-01-026-040}

[]{#MA-SOL-ANM-01-026-040}

Para cualquier entrada $x$, $|f_n(x)-x|=1/(n+1)\to0$, así el límite puntual es la identidad. Para todo par $u,v$, $|f_n(u)-f_n(v)|=|u-v|$, dando constante Lipschitz común uno. Si $x_n\to x$ es una ruta dada, la triangular ofrece $|f_n(x_n)-x|\le|x_n-x|+1/(n+1)\to0$, reuniendo sus dos cortes. En las tiendas, las filas y el límite también son continuos, pero sus constantes Lipschitz crecen como $n+3$. La ruta central mantiene salida uno, así esas condiciones de continuidad no reemplazan la cota común que hace funcionar la prueba positiva.

**Retorno visual.** Véase [C26-F08](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html#fig-anm-c26-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 26](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto.html) · [Ejercicios](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-26-sucesiones-de-funciones-converger-punto-por-punto-soluciones.html)
