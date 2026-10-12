---
content-id: MA-BCH-0314
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-028
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
title: Capítulo 28 — Intercambiar límites con operaciones
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C28.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html)

C27 construyó el contrato uniforme. Ahora probaremos qué operaciones conserva, construyendo cada destino antes de identificarlo: continuidad, límites relativos, integrabilidad y derivabilidad. C14/C18/C23 son centrales; C10/C13/C16/C17/C19/C24 aportan interfaces declaradas. C29 sólo se anuncia al final.

## 28.1. Fijar una fila para conservar continuidad

[]{#MA-SEC-ANM-01-028-001}

C27 permite escoger una etapa antes de conocer la entrada. Ésa es la diferencia que faltaba en el argumento de continuidad de C26. Sean $X\subseteq\mathbb R$, $f_n:X\to\mathbb R$ y $f_n\to f$ uniformemente. La continuidad se entiende relativamente a $X$, también en sus bordes y puntos aislados.

**R1 — Límite uniforme de continuas.** Si las filas son continuas en un punto $x_0\in X$, entonces $f$ es continua allí. Para $\varepsilon>0$, el contrato uniforme da un corte con error menor que $\varepsilon/3$ en toda entrada y toda fila posterior. Fijamos una sola fila $f_N$. Su continuidad en $x_0$ entrega $\delta>0$ para error menor que $\varepsilon/3$. Si $x\in X$ y $|x-x_0|<\delta$,

$$|f(x)-f(x_0)|\le |f(x)-f_N(x)|+|f_N(x)-f_N(x_0)|+|f_N(x_0)-f(x_0)|<\varepsilon.$$

El radio se obtiene **después** de fijar la fila; no debe funcionar para todas las filas. Tampoco se necesita una cota global de sus valores. Basta que haya filas continuas en el punto con índices arbitrariamente grandes: para cada tolerancia escogemos una de ellas después del corte. Si todas son continuas en $X$, la conclusión se aplica en todo $X$. En el vacío no hay puntos que comprobar.

**Continuidad uniforme es otra propiedad.** Si las filas son uniformemente continuas en $X$, la misma prueba usa el radio de una fila para todo par $x,y\in X$. Así el límite es uniformemente continuo. No se exige de antemano un radio común a la familia de filas. Si sólo sabemos continuidad ordinaria de las filas, obtenemos continuidad ordinaria; en un compacto, C17 convierte después la del límite en uniforme.

Para $f_n(x)=x+1/(n+1)$ en toda la recta, el error de aproximación es $1/(n+1)$ y el límite es la identidad, uniformemente continua y no acotada. El control de errores no es una barrera de valores.

**Una prueba que ahora sí funciona.** Las potencias de C26 en $[0,1]$ son continuas, pero su límite vale cero antes de uno y uno en uno. R1 demuestra por contraposición que no pueden converger uniformemente. La conclusión concuerda con la envolvente uno de C27. En $[0,1)$ el límite es continuo y la convergencia sigue sin ser uniforme: continuidad del destino es una consecuencia suficiente, no una caracterización del modo de convergencia.

![En la ventana \[−1,1\], la fila x+1/5 aproxima la identidad con error1/5. Los tres tramos en el segundo panel separan aproximación en ambas entradas y variación de la fila fija. Para entradas0 y1/10, el presupuesto triangular es1/2, aunque la diferencia real es1/10. La prueba general fija fila antes del radio.](../../assets/books/anm/C28/C28-F01.svg){#fig-anm-c28-f01 fig-alt="En la ventana \[−1,1\], la fila x+1/5 aproxima la identidad con error1/5. Los tres tramos en el segundo panel separan aproximación en ambas entradas y variación de la fila fija. Para entradas0 y1/10, el presupuesto triangular es1/2, aunque la diferencia real es1/10. La prueba general fija fila antes del radio."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-001}

1. ¿Qué se fija antes de obtener el radio de continuidad?

[]{#MA-MIC-ANM-01-028-002}

2. ¿Cuántos errores controla la prueba de R1?

[]{#MA-MIC-ANM-01-028-003}

3. ¿La fila fijada necesita una cota global de valores?

[]{#MA-MIC-ANM-01-028-004}

4. ¿Los radios de continuidad deben ser comunes a todas las filas?

[]{#MA-MIC-ANM-01-028-005}

5. ¿Qué hipótesis de filas conserva continuidad uniforme?

[]{#MA-MIC-ANM-01-028-006}

6. ¿Un destino continuo obliga convergencia uniforme?

[]{#MA-MIC-ANM-01-028-007}

7. ¿Qué continuidad se usa en bordes del dominio?

[]{#MA-MIC-ANM-01-028-008}

8. ¿Qué ocurre en un dominio vacío?

## 28.2. Dos límites con un presupuesto común

[]{#MA-SEC-ANM-01-028-002}

Continuidad combina dos aproximaciones: avanzar el índice y acercar la entrada. Primero construiremos los destinos antes de intercambiar el orden.

**R2 — Existencia e intercambio de límites.** Sea $a$ punto de acumulación de $X\subseteq\mathbb R$. Supongamos $f_n\to f$ uniformemente en $X$ y que existen los límites relativos perforados

$$p_n=\lim_{\substack{x\to a\\x\in X}}f_n(x)\in\mathbb R.$$

Entonces existe $p=\lim_n p_n$, existe el límite relativo de $f$ en $a$ y ambos son $p$. El centro puede pertenecer o no a $X$; su valor, si existe, no interviene en estos límites perforados.

Para construir $p$, usamos Cauchy uniforme de C27. Dada $\eta>0$, hay $N$ con $|f_n(x)-f_m(x)|<\eta/2$ para $m,n\ge N$ y toda entrada. Fijamos esos dos índices y pasamos $x\to a$. Álgebra del absoluto y orden de C13 dan

$$|p_n-p_m|\le\eta/2<\eta.$$

Hay entradas perforadas arbitrariamente cercanas porque $a\in X'$; no hemos creado un límite vacío. C10 construye el único real $p$ de esta sucesión de Cauchy.

Ahora, para $\varepsilon>0$, elegimos una fila $n$ suficientemente grande para que $|f(x)-f_n(x)|<\varepsilon/3$ en todo $X$ y $|p_n-p|<\varepsilon/3$. Con **ese índice fijo**, el límite de la fila da un radio con $|f_n(x)-p_n|<\varepsilon/3$ en la ventana perforada. Por triangular, $|f(x)-p|<\varepsilon$. Se ha probado la existencia del límite de $f$, además de la igualdad

$$\lim_{\substack{x\to a\\x\in X}}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{\substack{x\to a\\x\in X}}f_n(x).$$

Si desde el principio ya existe $\lim_{x\to a}f(x)=p$, la prueba se abrevia pasando al límite la cota uniforme con margen $\varepsilon/2$: $|p_n-p|\le\varepsilon/2<\varepsilon$. Uniformidad sólo en una vecindad perforada fija también basta: restringimos el dominio antes de aplicar R2. Una vecindad dependiente del índice no aporta ese contrato común.

**Ruta conjunta dada.** Si $x_n\in X\setminus\{a\}$ y $x_n\to a$, el presupuesto

$$|f_n(x_n)-p|\le |f_n(x_n)-f(x_n)|+|f(x_n)-p|$$

da convergencia a $p$. El corte uniforme controla el primer término y el límite recién construido controla el segundo. No se selecciona una ruta a partir de una negación.

Para $f_n(x)=x+1/(n+1)$, $a=0$, tenemos $p_n=1/(n+1)$ y $p=0$. En cambio, $r_n(x)=(n+1)x/[1+(n+1)x]$ sobre $(0,1]$ tiene límite puntual uno, pero cada fila tiende a cero cuando $x\downarrow0$. Los iterados son uno y cero; la ruta $x_n=1/(n+1)$ vale $1/2$. La falta de uniformidad explica la discrepancia, sin negar existencia de ambos iterados.

![La familia uniforme x+1/(n+1) tiene límites de fila1/(n+1) en cero y destino común0. En la familia racional r_n=(n+1)x/\[1+(n+1)x\], el límite puntual en(0,1\] es1, pero los destinos de fila en cero son0. La ruta dada1/(n+1) vale1/2. Las líneas horizontales muestran destinos calculados, no una inferencia de muestras.](../../assets/books/anm/C28/C28-F02.svg){#fig-anm-c28-f02 fig-alt="La familia uniforme x+1/(n+1) tiene límites de fila1/(n+1) en cero y destino común0. En la familia racional r_n=(n+1)x/\[1+(n+1)x\], el límite puntual en(0,1\] es1, pero los destinos de fila en cero son0. La ruta dada1/(n+1) vale1/2. Las líneas horizontales muestran destinos calculados, no una inferencia de muestras."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-009}

1. ¿Por qué el centro de R2 debe acumular?

[]{#MA-MIC-ANM-01-028-010}

2. ¿Qué se construye primero en R2?

[]{#MA-MIC-ANM-01-028-011}

3. ¿Qué cota queda al pasar una entrada al límite?

[]{#MA-MIC-ANM-01-028-012}

4. ¿Qué construye el destino de una sucesión de Cauchy real?

[]{#MA-MIC-ANM-01-028-013}

5. ¿El valor de la función en el centro participa?

[]{#MA-MIC-ANM-01-028-014}

6. ¿Basta uniformidad en una ventana fija?

[]{#MA-MIC-ANM-01-028-015}

7. ¿Qué valor conserva la ruta racional $x_n=1/(n+1)$?

[]{#MA-MIC-ANM-01-028-016}

8. ¿Se escoge una ruta por cada escala en la prueba?

## 28.3. Compacidad y monotonía: el mecanismo de Dini

[]{#MA-SEC-ANM-01-028-003}

La continuidad del límite no caracteriza uniformidad, pero en presencia de compacidad y orden de las filas sí puede producirla.

**R3 — Dini, con todas sus hipótesis.** Sea $K\subseteq\mathbb R$ compacto. Sean $f_n$ continuas relativamente a $K$, decrecientes por columnas y convergentes puntualmente a una función continua $f$. Entonces $f_n\to f$ uniformemente en $K$. Para filas crecientes aplicamos el resultado a $-f_n$.

El orden pasa al límite numérico, así $e_n(x)=f_n(x)-f(x)\ge0$; además $e_{n+1}\le e_n$ y $e_n\to0$ puntualmente. Fijamos $\varepsilon>0$ y definimos los abiertos relativos

$$U_n=\{x\in K:e_n(x)<\varepsilon/2\}.$$

Continuidad de $f_n$ y $f$ hace abiertos estos conjuntos. Son crecientes y cubren $K$ por convergencia puntual. Para conectar con la definición de cubierta de C16, podemos usar todos los pares $(n,r)$ de bolas reales cuyo corte con $K$ esté contenido en $U_n$: esa familia abierta cubre $K$ sin escoger un radio por cada punto. Compacidad entrega una subfamilia finita. Si $K\ne\varnothing$, sus índices naturales tienen máximo $N$ y todos sus cortes están en $U_N$. Por tanto $e_n(x)<\varepsilon/2<\varepsilon$ para todo $x\in K$ y $n\ge N$. Si $K$ es vacío, el contrato es vacuo.

**Dónde se gastó cada hipótesis.** Puntualidad cubre; continuidad abre; compacidad reduce a finito; monotonía convierte los índices finitos en un corte para toda la cola. No se tomó un máximo de infinitos umbrales ni se supuso una tasa geométrica. El teorema es cualitativo: no entrega una fórmula universal para $N(\varepsilon)$.

Para $f_n(x)=x/(n+1)$ en $[0,1]$, las columnas decrecen a cero y la cota explícita $1/(n+1)$ confirma el teorema. Las potencias en $[0,1]$ tienen destino discontinuo y conservan envolvente uno. En $(0,1)$ las mismas potencias tienen destino continuo, pero el dominio no es compacto y la envolvente sigue siendo uno.

Las indicadoras $s_n=\mathbf1_{(0,1/(n+1))}$ sobre $[0,1]$ decrecen puntualmente a cero continuo y tienen envolvente uno: **sus filas no son continuas**. Las tiendas $t_n$ de C26 son continuas en el compacto y tienden puntualmente a cero continuo, pero no tienen monotonía por columnas; su altura máxima uno persiste. Cada ejemplo elimina una hipótesis diferente.

**Otro uso de finitud.** Si una familia dada de abiertos cubre un compacto y la convergencia es uniforme en el corte del compacto con cada miembro, una subcubierta finita y C27 producen uniformidad en todo el compacto. «Uniforme cerca de cada punto» debe significar uniformidad en una vecindad fija del punto; continuidad local sola no lo dice. La cubierta se construye con todos los abiertos admisibles, sin elegir uno por punto.

![Para e_n=x/(n+1) en\[0,1\] y tolerancia1/4, los abiertos relativos U_n={e_n<1/8} crecen hasta cubrir todo el segmento desde n=8. En n=7 falta el extremo1. Potencias en(0,1) conservan envolvente1 pese a destino continuo: falta compacidad. Cada abierto y cada corte están definidos por la desigualdad exacta.](../../assets/books/anm/C28/C28-F03.svg){#fig-anm-c28-f03 fig-alt="Para e_n=x/(n+1) en\[0,1\] y tolerancia1/4, los abiertos relativos U_n={e_n&lt;1/8} crecen hasta cubrir todo el segmento desde n=8. En n=7 falta el extremo1. Potencias en(0,1) conservan envolvente1 pese a destino continuo: falta compacidad. Cada abierto y cada corte están definidos por la desigualdad exacta."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-017}

1. ¿Qué error es no negativo en Dini decreciente?

[]{#MA-MIC-ANM-01-028-018}

2. ¿Qué hace abiertos los conjuntos de error pequeño?

[]{#MA-MIC-ANM-01-028-019}

3. ¿Qué permite obtener una subcubierta finita?

[]{#MA-MIC-ANM-01-028-020}

4. ¿Qué convierte los índices finitos en una cola común?

[]{#MA-MIC-ANM-01-028-021}

5. ¿Dini entrega una tasa numérica general?

[]{#MA-MIC-ANM-01-028-022}

6. ¿Qué falta en las potencias sobre $(0,1)$?

[]{#MA-MIC-ANM-01-028-023}

7. ¿Qué falta en las indicadoras decrecientes del intervalo pequeño?

[]{#MA-MIC-ANM-01-028-024}

8. ¿Qué falta en las tiendas continuas de altura uno?

## 28.4. La integral soporta un error global pequeño

[]{#MA-SEC-ANM-01-028-004}

La integral de Riemann requiere existencia, no sólo una notación bajo el signo de límite. Trabajaremos en un intervalo cerrado fijo $[a,b]$, con $a<b$ y longitud $\ell=b-a$.

**R4 — Límite uniforme de integrables.** Si cada $f_n$ es integrable de Riemann en $[a,b]$ y $f_n\to f$ uniformemente, entonces $f$ es integrable y

$$\lim_n\int_a^b f_n(t)\,dt=\int_a^b f(t)\,dt.$$

Primero existe una barrera para $f$: el corte uniforme para error uno entrega una fila acotada $f_N$ y $|f|\le |f_N|+1$. Por ello las imágenes locales no vacías tienen supremo e ínfimo reales. Para cualquier función acotada $u$ con $|f-u|\le\delta$ y cualquier partición $P$, comparación de cotas en cada pieza da

$$U(f,P)\le U(u,P)+\delta\ell,\qquad L(f,P)\ge L(u,P)-\delta\ell.$$

En efecto, todo valor de $f$ queda bajo la cota superior local de $u$ más $\delta$ y sobre su cota inferior menos $\delta$. Pasar a extremos conserva desigualdades débiles; sumar anchuras produce exactamente $\ell$. Así

$$G(f,P)\le G(u,P)+2\delta\ell.$$

Dada $\varepsilon>0$, escogemos una fila con error menor que $\delta=\varepsilon/[8(\ell+1)]$ y luego una partición de esa fila con brecha menor que $\varepsilon/2$. La brecha de $f$ resulta menor que $\varepsilon/2+\varepsilon/4<\varepsilon$. El criterio de Darboux de C23 prueba integrabilidad **antes** de comparar valores integrales.

Ahora $f_n-f$ y su valor absoluto son integrables por C23. Para toda envolvente real $E_n=\sup_{[a,b]}|f_n-f|$ de la cola,

$$\left|\int_a^b f_n-\int_a^b f\right|\le\int_a^b|f_n-f|\le\ell E_n.$$

Como $E_n\to0$, el límite sigue. La desigualdad es también un certificado de error para una etapa concreta; no se necesita que el máximo se alcance. Para $a=b$, las integrales son cero por convención y no se divide por una longitud nula. Orientar al revés cambia el signo de ambos valores, conservando la cota absoluta con $|b-a|$.

Para $f_n(t)=t^2+1/(n+1)$ en $[0,1]$, la integral es $1/3+1/(n+1)$ y el error es exactamente $E_n=1/(n+1)$. La cota de longitud es óptima para errores constantes de un signo.

**Puntualidad no basta.** Las tiendas normalizadas $b_n=(n+3)t_n$ de C26 son continuas e integrables, tienden puntualmente a cero y tienen integral uno. Ambas integrales comparadas existen y difieren. Las indicadoras finitas de racionales de C25 tienden a Dirichlet, que ni siquiera es integrable: allí la comparación final no está definida. Las dos fallas son distintas.

![La perturbación constante1/(n+1) sobre t² en\[0,1\] tiene área de error igual a su envolvente. Las tiendas normalizadas de k=n+3 conservan área1 y altura k, pese a destino puntual0. Los perfiles son continuos y sus áreas se acreditan por ramas afines antes de dibujar.](../../assets/books/anm/C28/C28-F04.svg){#fig-anm-c28-f04 fig-alt="La perturbación constante1/(n+1) sobre t² en\[0,1\] tiene área de error igual a su envolvente. Las tiendas normalizadas de k=n+3 conservan área1 y altura k, pese a destino puntual0. Los perfiles son continuos y sus áreas se acreditan por ramas afines antes de dibujar."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-025}

1. ¿Qué debe probarse antes de escribir la integral del destino?

[]{#MA-MIC-ANM-01-028-026}

2. ¿Cómo cambia la brecha Darboux con error global $\delta$?

[]{#MA-MIC-ANM-01-028-027}

3. ¿Por qué aparecen dos contribuciones de error en la brecha?

[]{#MA-MIC-ANM-01-028-028}

4. ¿Qué error controla el valor integral?

[]{#MA-MIC-ANM-01-028-029}

5. ¿Debe alcanzarse la envolvente para integrar su cota?

[]{#MA-MIC-ANM-01-028-030}

6. ¿Cómo se trata un segmento de longitud cero?

[]{#MA-MIC-ANM-01-028-031}

7. ¿Qué conserva la integral de las tiendas normalizadas?

[]{#MA-MIC-ANM-01-028-032}

8. ¿Qué falla para el destino Dirichlet?

## 28.5. Acumulaciones, pesos y extremos variables

[]{#MA-SEC-ANM-01-028-005}

El presupuesto de R4 controla más que una integral final. Sea $c\in[a,b]$ fijo y definamos, por restricción y orientación de C23,

$$A_n(x)=\int_c^x f_n(t)\,dt,\qquad A(x)=\int_c^x f(t)\,dt.$$

**R5 — Acumulaciones uniformes.** Bajo R4, para todo $x\in[a,b]$,

$$|A_n(x)-A(x)|\le |x-c|E_n\le\ell E_n.$$

Si $x<c$, invertimos los límites de integración antes de aplicar orden; si $x=c$, ambos lados son cero. El mismo corte controla todos los destinos de acumulación. No es una familia infinita de cortes escogidos por separado.

Si todas las integrandas son continuas, R1 prueba continuidad de $f$. C24 entrega $A_n'=f_n$ y $A'=f$ en $(a,b)$, con derivadas relativas de un lado en los extremos cuando corresponda. Así se conservan simultáneamente acumulación y tasa. Para integrandas sólo integrables, $A$ sigue existiendo y siendo continua por C24, pero no se identifica su derivada con $f$ en un punto discontinuo sin hipótesis adicional.

**Peso fijo.** Si $w$ es integrable y $|w|\le M$, el producto $wf_n$ y $wf$ es integrable por C23 y

$$\left|\int_a^b w(t)(f_n(t)-f(t))\,dt\right|\le M\ell E_n.$$

Se puede mejorar a $E_n\int_a^b|w|$. Existencia de los productos y del absoluto precede a esta estimación. No se está multiplicando las integrales de los factores.

**Extremos móviles dentro de un marco fijo.** Sean $u_n,v_n,u,v\in[a,b]$, $u_n\to u$, $v_n\to v$. Si $|f|\le B$, la aditividad orientada da

$$\left|\int_{u_n}^{v_n}f_n-\int_u^v f\right|\le\ell E_n+B|u_n-u|+B|v_n-v|.$$

Primero cambiamos $f_n$ por $f$ manteniendo extremos; luego movemos los extremos de la integral de $f$. La cota es válida si están invertidos o coinciden. Tres errores tendentes a cero permiten el límite, porque todos los intervalos viven en el mismo marco finito.

Para $f_n(t)=t^2+1/(n+1)$, $c=0$, $A_n(x)=x^3/3+x/(n+1)$. El error de acumulación es $|x|/(n+1)$; en $[0,1]$ su envolvente es $1/(n+1)$. Si el peso es $w(t)=t$, el error integral final es $1/[2(n+1)]$.

**La longitud también es una hipótesis.** Las funciones constantes $1/(n+1)$ convergen uniformemente a cero en toda la recta. Sin embargo, su integral en $[0,n+1]$ vale uno. Los intervalos crecen y no hay una longitud fija que multiplique un error tendente a cero. No se ha definido ni utilizado aquí una integral impropia: cada etapa es una integral propia finita. Uniformidad es suficiente en el marco fijo, pero no necesaria para igualdad de un par de límites integrales: las tiendas sin normalizar tienen integral $1/(n+3)\to0$ sin converger uniformemente.

![Acumuladas de t²+1/(n+1) desde0: error x/(n+1), bajo una cota común1/(n+1) en\[0,1\]. Para constantes1/(n+1) integradas en\[0,n+1\], la altura baja y la longitud crece; el área queda1. Se representan integrales propias finitas de cada etapa, sin introducir integración impropia.](../../assets/books/anm/C28/C28-F05.svg){#fig-anm-c28-f05 fig-alt="Acumuladas de t²+1/(n+1) desde0: error x/(n+1), bajo una cota común1/(n+1) en\[0,1\]. Para constantes1/(n+1) integradas en\[0,n+1\], la altura baja y la longitud crece; el área queda1. Se representan integrales propias finitas de cada etapa, sin introducir integración impropia."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-033}

1. ¿Qué corte controla todas las acumulaciones?

[]{#MA-MIC-ANM-01-028-034}

2. ¿Qué se hace si el destino de acumulación precede al anclaje?

[]{#MA-MIC-ANM-01-028-035}

3. ¿Qué hipótesis permite identificar la derivada de toda acumulación?

[]{#MA-MIC-ANM-01-028-036}

4. ¿Qué debe acreditarse para un peso integrable fijo?

[]{#MA-MIC-ANM-01-028-037}

5. ¿Cuántos errores hay al mover ambos extremos?

[]{#MA-MIC-ANM-01-028-038}

6. ¿Dónde deben permanecer los extremos móviles?

[]{#MA-MIC-ANM-01-028-039}

7. ¿Cuánto integra $1/(n+1)$ sobre $[0,n+1]$?

[]{#MA-MIC-ANM-01-028-040}

8. ¿Uniformidad es necesaria para igualdad de límites integrales?

## 28.6. Derivadas uniformes y un valor de anclaje

[]{#MA-SEC-ANM-01-028-006}

La derivada divide incrementos por distancias pequeñas. Un error de valores uniformemente pequeño puede amplificarse sin límite tras esa división. El control adecuado actúa sobre las derivadas.

**R6 — Teorema de convergencia de derivadas.** Sean $a<b$, $f_n$ continuas en $[a,b]$ y derivables en $(a,b)$. Supongamos que $g_n=f_n'$ converge uniformemente a $g$ en $(a,b)$ y que, para un $c\in[a,b]$, $f_n(c)\to\lambda$. Entonces existe $f$ con $f_n\to f$ uniformemente en $[a,b]$, $f(c)=\lambda$ y $f'=g$ en $(a,b)$. No se supone continuidad de las derivadas.

**Construir los valores.** C27 da Cauchy uniforme para $g_n$. Para $m,n$ posteriores a un corte y $x\in[a,b]$, aplicamos C19 a $f_n-f_m$ en el segmento completo entre $c$ y $x$. Su continuidad en los extremos y derivabilidad interior están acreditadas. Si la diferencia de derivadas es menor que $\eta$ en todo $(a,b)$,

$$|f_n(x)-f_m(x)|\le |f_n(c)-f_m(c)|+\eta|x-c|.$$

El caso $x=c$ es directo. Dada $\varepsilon>0$, pedimos al anclaje error menor que $\varepsilon/2$ y a las derivadas menor que $\varepsilon/[2(\ell+1)]$, $\ell=b-a$. El máximo de ambos cortes prueba Cauchy uniforme de las filas. C27 construye el único $f$; R1 da continuidad en el cerrado y puntualidad identifica $f(c)=\lambda$.

**Controlar incrementos antes de dividir.** Sean $E_n=\sup_{(a,b)}|g_n-g|$ las envolventes reales de la cola. Para $x,y\in[a,b]$, C19 aplicado a $f_m-f_n$ y la cota $E_m+E_n$ dan

$$|(f_m-f_n)(y)-(f_m-f_n)(x)|\le(E_m+E_n)|y-x|.$$

Fijamos $n,x,y$ y pasamos $m\to\infty$. C10/C13 conservan orden y C27 da $E_m\to0$, por lo que

$$|(f-f_n)(y)-(f-f_n)(x)|\le E_n|y-x|.$$

No se afirmó que $f$ ya fuera derivable. Esta desigualdad de incrementos se obtiene antes de cualquier cociente nuevo.

**Identificar la derivada.** Fijamos $x_0\in(a,b)$ y $\varepsilon>0$. Elegimos una fila $n$ con $E_n<\varepsilon/3$. Para cualquier $x\ne x_0$ admisible, la desigualdad anterior controla en $E_n$ la diferencia de cocientes de $f$ y $f_n$. La derivabilidad de esa fila fija aporta un radio para el segundo error. Finalmente,

$$\left|\frac{f(x)-f(x_0)}{x-x_0}-g(x_0)\right|\le E_n+\left|\frac{f_n(x)-f_n(x_0)}{x-x_0}-g_n(x_0)\right|+|g_n(x_0)-g(x_0)|<\varepsilon.$$

La tercera magnitud es a lo sumo $E_n$. Se ha demostrado $f'(x_0)=g(x_0)$ por definición, sin exigir una primitiva integral de una derivada discontinua.

La misma cota de incrementos, con $x=c$, entrega el certificado

$$|f_n(x)-f(x)|\le |f_n(c)-\lambda|+|x-c|E_n.$$

En un intervalo abierto arbitrario el argumento se aplica a cada segmento cerrado contenido en él y que una el anclaje con la entrada. Produce un límite puntual y uniformidad en cada segmento acotado apropiado; en un intervalo no acotado no garantiza uniformidad global de valores. Para dominios desconectados, hace falta un anclaje por componente que se quiera construir; un valor no fija constantes en otra componente.

![Con f_n=x²+(1−2^(−n))x y ancla0, el error de valores es−2^(−n)x y la envolvente de derivadas es2^(−n). La cota de incrementos del error es D_n|y−x|; desde el anclaje queda |error(x)|≤D_n|x|. La división por distancia se hace sólo después de obtener esta cota.](../../assets/books/anm/C28/C28-F06.svg){#fig-anm-c28-f06 fig-alt="Con f_n=x²+(1−2^(−n))x y ancla0, el error de valores es−2^(−n)x y la envolvente de derivadas es2^(−n). La cota de incrementos del error es D_n|y−x|; desde el anclaje queda |error(x)|≤D_n|x|. La división por distancia se hace sólo después de obtener esta cota."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-041}

1. ¿Qué dato fija la constante aditiva en R6?

[]{#MA-MIC-ANM-01-028-042}

2. ¿En qué dominio se controlan uniformemente las derivadas?

[]{#MA-MIC-ANM-01-028-043}

3. ¿Qué herramienta convierte derivadas en cotas de incrementos?

[]{#MA-MIC-ANM-01-028-044}

4. ¿Qué se fija antes de pasar una etapa al límite en incrementos?

[]{#MA-MIC-ANM-01-028-045}

5. ¿Se supone derivabilidad del destino para obtener esa cota?

[]{#MA-MIC-ANM-01-028-046}

6. ¿Cómo se divide la cota de incrementos?

[]{#MA-MIC-ANM-01-028-047}

7. ¿R6 necesita derivadas continuas?

[]{#MA-MIC-ANM-01-028-048}

8. ¿Qué factor limita la uniformidad de valores en dominios no acotados?

## 28.7. Lo que la convergencia de valores no controla

[]{#MA-SEC-ANM-01-028-007}

La uniformidad de valores conserva continuidad, pero no derivabilidad. Tampoco basta saber que existen las derivadas puntuales de las filas y que éstas tienen un límite puntual.

**R7 — Tres pruebas de frontera.** Sea $k=n+1$ y

$$q_n(x)=\sqrt{x^2+k^{-2}}\quad(x\in\mathbb R).$$

Las herramientas de raíces y cadena de C10/C18 dan $q_n'=x/\sqrt{x^2+k^{-2}}$. Puesto que $|x|\le q_n(x)\le |x|+1/k$, se tiene $\sup_{\mathbb R}|q_n-|x||=1/k$, alcanzado en cero. La segunda desigualdad sigue al cuadrar dos cantidades no negativas. El límite $|x|$ es continuo y no derivable en cero: los cocientes laterales son menos uno y uno. Cada fila sí es derivable allí, con derivada cero. Las derivadas convergen puntualmente a la función signo, con valor cero en el origen, que es discontinua. R1 refuta su convergencia uniforme, pues las derivadas de las filas son continuas.

Ahora recuperamos

$$h_n(x)=\frac{x}{1+kx^2},\qquad h_n'(x)=\frac{1-kx^2}{(1+kx^2)^2}.$$

C27 da convergencia uniforme de valores a cero con envolvente $1/(2\sqrt k)$. En cero las derivadas valen uno; para $x\ne0$ tienden a cero. Para comprobarlo basta dividir numerador y denominador por $k^2x^4$, que es no nulo, o acotar con $1/(kx^2)+1/(k^2x^4)$. El límite puntual de derivadas es la indicadora de cero, distinta de la derivada cero del límite de valores. La igualdad deseada falla en un punto donde **ambos** destinos de derivadas existen. No es sólo una falta de existencia.

**El anclaje no es decorativo.** Las funciones constantes $f_n=n$ tienen derivadas idénticamente cero y no convergen en ningún punto. Las constantes $(-1)^n$ tampoco convergen, aunque sus derivadas sí. En $[0,1]\cup[2,3]$ podemos fijar todas las filas en cero en la primera componente y en $n$ en la segunda; una ancla en la primera no controla la segunda. No hay segmento del dominio atravesando el hueco al que aplicar C19.

**Un control local no es global.** Para $f_n(x)=x/(n+1)$ en $\mathbb R$, las derivadas convergen uniformemente a cero y $f_n(0)=0$. Los valores convergen uniformemente en cada segmento acotado, pero no en toda la recta: en $x=n+1$ el error es uno. El factor $|x-c|$ de R6 no tiene barrera global.

La operación de derivar no es continua respecto de la sola norma de valores: $h_n$ es una sucesión de errores pequeños cuyas derivadas no se acercan uniformemente a cero. La integral en un marco fijo sí tiene la cota de R4. Los operadores requieren presupuestos diferentes; no basta que sus fórmulas se parezcan a un paso al límite.

![Raíces suavizadas sqrt(x²+1/k²) convergen uniformemente a|x|, que tiene esquina en0. Para h_n=x/(1+kx²), las derivadas son(1−kx²)/(1+kx²)² y conservan valor1 en0; su destino puntual vale0 fuera de0. Se muestra la ventana\[−1,1\] de reglas definidas sobre todaR. No se concluye uniformidad de derivadas.](../../assets/books/anm/C28/C28-F07.svg){#fig-anm-c28-f07 fig-alt="Raíces suavizadas sqrt(x²+1/k²) convergen uniformemente a|x|, que tiene esquina en0. Para h_n=x/(1+kx²), las derivadas son(1−kx²)/(1+kx²)² y conservan valor1 en0; su destino puntual vale0 fuera de0. Se muestra la ventana\[−1,1\] de reglas definidas sobre todaR. No se concluye uniformidad de derivadas."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-049}

1. ¿Qué envolvente tienen las raíces suavizadas frente a $|x|$?

[]{#MA-MIC-ANM-01-028-050}

2. ¿Por qué $|x|$ no deriva en cero?

[]{#MA-MIC-ANM-01-028-051}

3. ¿Qué valor tienen $h_n^{\prime}$ en cero?

[]{#MA-MIC-ANM-01-028-052}

4. ¿Qué derivada tiene el destino cero de $h_n$?

[]{#MA-MIC-ANM-01-028-053}

5. ¿Qué no detecta la operación de derivar?

[]{#MA-MIC-ANM-01-028-054}

6. ¿Una ancla controla otra componente separada?

[]{#MA-MIC-ANM-01-028-055}

7. ¿Dónde convergen uniformemente los valores $x/(n+1)$?

[]{#MA-MIC-ANM-01-028-056}

8. ¿La sola norma de valores controla la derivada?

## 28.8. Certificar varias operaciones a la vez

[]{#MA-SEC-ANM-01-028-008}

Los teoremas anteriores permiten convertir una aproximación en una cadena de certificados, indicando para cada operación su dominio, existencia y cota.

**R8 — Un paquete explícito.** En $[-1,1]$, sean

$$f_n(x)=x^2+(1-2^{-n})x,\quad f(x)=x^2+x,\quad g_n(x)=2x+1-2^{-n},\quad g(x)=2x+1.$$

Todas las filas son polinomios, $f_n(0)=0$, y las diferencias de derivadas tienen envolvente $D_n=2^{-n}$. R6 construye e identifica el límite con derivada $g$; la cota de anclaje da $|f_n(x)-f(x)|\le |x|D_n$. La igualdad directa muestra $E_n=D_n$, alcanzada en los extremos. R1 conserva continuidad y R4 permite integrar. En todo el intervalo final $[-1,1]$, el error integral firmado es cero porque la diferencia es impar; la cota general $2E_n$ sigue siendo válida, aunque no sea exacta en ese caso.

Con anclaje de acumulación en cero, C24 da

$$A_n(x)=x^3/3+(1-2^{-n})x^2/2,\qquad A(x)=x^3/3+x^2/2.$$

Por ello $\sup|A_n-A|=D_n/2$. Se conocen simultáneamente valores, pendientes, acumulaciones y sus tasas. Un certificado para error de derivadas menor que $\varepsilon$ exige $2^{-n}<\varepsilon$, con desigualdad estricta: si $\varepsilon=1/8$, desde $n=4$ sirve, pero $n=3$ está en la frontera. No se deduce una identidad de integrales de una gráfica.

**Norma con dos capas.** Para funciones $u$ continuas en $[a,b]$ con derivada interior que admita extensión continua al cerrado, llamamos $C^1([a,b])$ a esta clase y definimos

$$\|u\|_{C^1}=\sup_{[a,b]}|u|+\sup_{[a,b]}|u'|.$$

Los extremos de $u'$ son los valores de la extensión continua; coinciden con derivadas de un lado por C19 y paso al límite. Sus imágenes son acotadas por C16. Las propiedades de norma siguen aplicando las de C27 a las dos capas; identidad usa ya la capa de valores. Si $u_n\to u$ en esta norma, convergen uniformemente valores y derivadas. A la inversa, si una sucesión de $C^1$ tiene derivadas uniformes en el cerrado y valores convergentes en un anclaje, R1 hace continuo al límite de derivadas, R6 construye $u$ y prueba convergencia en ambas capas. El límite de derivadas en los bordes es su extensión continua; la misma cota de incrementos identifica las derivadas laterales.

**Un número finito de derivadas.** Para $r\ge1$ fijo, supongamos filas $C^r$ en un mismo segmento, convergencia uniforme de sus derivadas de orden $r$ y convergencia de los valores de órdenes $0,\ldots,r-1$ en un anclaje común. Aplicamos R6 primero a las filas de orden $r-1$, después a las de orden $r-2$ y así un número finito de veces. Se construyen límites uniformes para todos los órdenes y se identifica cada derivada con el siguiente. No se usa una serie infinita ni Taylor para justificar esta inducción finita. Para $r=0$ sólo queda convergencia uniforme de valores.

**Guía de decisiones.** Para continuidad, una fila fija dentro de una banda. Para integrar, existencia por Darboux y longitud finita multiplicando el error. Para derivar, control uniforme de derivadas, segmentos admisibles y anclaje, seguido de error de incrementos proporcional a distancia. En cada caso se prueba la existencia del objeto final antes de escribir la igualdad de operaciones.

C29 usará estas herramientas sobre sucesiones de sumas parciales. Aquí sólo se trabajó con familias de funciones y con operaciones finitas: ni el criterio M de Weierstrass ni radios de convergencia han sido utilizados por anticipado.

![En el paquete polinómico dyádico sobre\[−1,1\], los errores exactos de valores y derivadas son2^(−n); el de acumulación es2^(−n)/2. Con tolerancia estricta1/8 para derivadas, n=3 es frontera y n=4 es el primer índice válido. Las curvas polinómicas y las envolventes provienen de fórmulas probadas.](../../assets/books/anm/C28/C28-F08.svg){#fig-anm-c28-f08 fig-alt="En el paquete polinómico dyádico sobre\[−1,1\], los errores exactos de valores y derivadas son2^(−n); el de acumulación es2^(−n)/2. Con tolerancia estricta1/8 para derivadas, n=3 es frontera y n=4 es el primer índice válido. Las curvas polinómicas y las envolventes provienen de fórmulas probadas."}

### Microcontroles

[]{#MA-MIC-ANM-01-028-057}

1. ¿Qué envolvente tiene la capa de derivadas del paquete polinómico?

[]{#MA-MIC-ANM-01-028-058}

2. ¿Qué anclaje del paquete es exacto?

[]{#MA-MIC-ANM-01-028-059}

3. ¿Qué envolvente tiene su error de acumulación?

[]{#MA-MIC-ANM-01-028-060}

4. ¿El error integral firmado en el segmento simétrico es igual a esa envolvente?

[]{#MA-MIC-ANM-01-028-061}

5. ¿Sirve $n=3$ para error estrictamente menor que $1/8$?

[]{#MA-MIC-ANM-01-028-062}

6. ¿Qué dos capas suma la norma $C^1$?

[]{#MA-MIC-ANM-01-028-063}

7. ¿Qué anclas se necesitan para controlar órdenes hasta $r$?

[]{#MA-MIC-ANM-01-028-064}

8. ¿Cuál es la única puerta siguiente?

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 28](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones.html) · [Ejercicios](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-28-intercambiar-limites-con-operaciones-microcontroles.html)

[← Capítulo 27](analisis-para-matematicos-capitulo-27-convergencia-uniforme-controlar-toda-la-funcion-a-la-vez.html) · [Capítulo 29 →](analisis-para-matematicos-capitulo-29-series-de-funciones-y-series-de-potencias.html)
