---
title: "Modelos, aproximaciones, escalas y linealización"
subtitle: "Física para matemáticos · Tomo I · Capítulo 6"
author: "A. Peña"
description: "Capítulo 6 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0346
source-id: FISPM-T1-C06
editorial-id: FPM-I-06
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0345"]
related: [MA-BOK-0005]
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
include-in-header:
  - ../../assets/includes/ma-math-font-ready.html
  - ../../assets/books/fispm/fispm-lightbox-focus.html
format:
  html:
    css: ../../assets/books/fispm/fispm-reader.css
    lightbox: true
number-sections: false
---

[Capítulo 5](fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 7](fisica-para-matematicos-capitulo-7-cinematica-en-una-dimension.md)

[]{#fispm-c06-modelos-aproximaciones-escalas-y-linealizaciuxf3n}

Este capítulo utiliza álgebra, geometría euclídea y cálculo de una variable: límites, derivadas, integrales y estimaciones. Importa de los capítulos 1--5 el lenguaje de los modelos físicos, las magnitudes y escalas, la medición, el espacio y las curvas. El objetivo es construir y validar simplificaciones mediante condiciones y cotas explícitas.

[]{#aproximar-es-formular-una-afirmación-con-condiciones}

[]{#fispm-t1-c06-s01}

[]{#fpm-i-06-s01}

## 6.1. Aproximar es formular una afirmación con condiciones {#fispm-c06-aproximar-es-formular-una-afirmaciuxf3n-con-condiciones}

La distancia entre dos puntos separados por una longitud horizontal $L>0$ y una altura $h$ es, dentro del modelo geométrico euclídeo, $d=\sqrt{L^2+h^2}$. Si la altura parece pequeña, suele reemplazarse esa distancia por $L$. La igualdad de Pitágoras y el reemplazo responden a operaciones diferentes: la primera es una consecuencia exacta de la geometría adoptada; el segundo pierde una parte de la distancia. Para juzgar esa pérdida hay que compararla con alguna referencia.

Dividir por $L$ permite reconocer la comparación pertinente. Si $u=h/L$, la relación exacta es $d/L=\sqrt{1+u^2}$. El valor numérico de $h$ depende de la unidad; $u$ compara la altura con la longitud del propio problema. Además, racionalizar la diferencia da $$\frac{d-L}{L} =\sqrt{1+u^2}-1 =\frac{u^2}{\sqrt{1+u^2}+1} \le\frac{u^2}{2}.$$ La última relación es una cota, no una igualdad aproximada. Por ejemplo, $|h|\le L/10$ garantiza que sustituir $d$ por $L$ pierde como máximo $0.005L$. Quien necesite conocer la distancia con error inferior a una milésima de $L$ todavía no tiene esa garantía. El mismo reemplazo puede servir para una pregunta y resultar insuficiente para otra.

[]{#una-afirmación-que-pueda-comprobarse}

### 6.1.1. Una afirmación que pueda comprobarse {#fispm-c06-una-afirmaciuxf3n-que-pueda-comprobarse}

[]{#fispm-t1-c06-d0001}

**Definición 6.1 --- Aproximación con criterio declarado.** Sean $q$ y $\widetilde q$ dos cantidades escalares del mismo tipo, definidas para los datos de un dominio $\mathcal R$. Fijada una escala positiva $S$ del mismo tipo y una tolerancia adimensional $\tau\ge0$, diremos que $\widetilde q$ aproxima a $q$ con ese criterio si, para todo dato admisible de $\mathcal R$, $$|q-\widetilde q|\le\tau S.$$ La escala puede depender de los datos, siempre que su definición y su positividad se declaren en todo el dominio.

El cuantificador «para todo» convierte una comprobación aislada en una garantía sobre un régimen. No exige que la cota sea la mejor posible. Tampoco afirma que el modelo geométrico represente cualquier situación real: si una cuerda se curva, la distancia entre extremos y la longitud de la cuerda son observables distintas. Primero se elige el modelo y la cantidad que interesa; después se aproxima su predicción.

El símbolo $\approx$ podrá abreviar una aproximación cuyo criterio ya se haya explicado. Escribir $d\approx L$ sin más información oculta tanto el cociente $h/L$ como la precisión que se pretende. Para el ejemplo anterior, una declaración completa sería: «En el modelo euclídeo, para $L>0$ y $|h|/L\le0.1$, la sustitución $d\approx L$ tiene error referido a $L$ no mayor que $0.005$».

[]{#fispm-t1-c06-mp0001}

**Principio 6.1 --- Declarar el objeto y el criterio.** Una aproximación debe identificar la cantidad objetivo, el modelo que la define, los datos admitidos y la medida con la que se juzga la pérdida de información. La corrección del cálculo dentro del modelo y la adecuación del modelo al fenómeno requieren controles distintos.

[]{#acumular-simplificaciones}

### 6.1.2. Acumular simplificaciones {#fispm-c06-acumular-simplificaciones}

Una aproximación suele construirse en varios pasos. El riesgo es que cada paso sea pequeño según una referencia distinta y que se sumen sus cifras como si fueran comparables.

[]{#fispm-t1-c06-p0001}

**Proposición 6.1 --- Composición de cotas sobre una escala común.** Sean $q_0,q_1,q_2$ cantidades del mismo tipo en un dominio $\mathcal R$, y sea $S>0$ una escala común. Si $|q_0-q_1|\le\alpha S$ y $|q_1-q_2|\le\beta S$ en todo ese dominio, con $\alpha,\beta\ge0$, entonces $$|q_0-q_2|\le(\alpha+\beta)S.$$

**Demostración.** La identidad $q_0-q_2=(q_0-q_1)+(q_1-q_2)$ permite aplicar la desigualdad triangular. Al insertar las dos cotas se obtiene $|q_0-q_2|\le|q_0-q_1|+|q_1-q_2|\le(\alpha+\beta)S$. Todas las desigualdades valen para los mismos datos. $\square$

La prueba explica por qué importa la escala común. Si las cotas fueran $\alpha S_1$ y $\beta S_2$, lo que podría sumarse serían esas cantidades, no las tolerancias solas. También importa el dominio común: dos aproximaciones válidas en regiones disjuntas no forman una cadena certificada.

[]{#ejercicios}

### 6.1.3. Ejercicios {#fispm-c06-ejercicios}

[]{#fispm-t1-c06-e0001}

[]{#fispm-t1-c06-e0006}

**Ejercicio 6.1.** Se afirma que $1/(1+x)\approx1$ «cuando $x$ es pequeño», con $x\ge0$. Repara la afirmación de dos maneras: usando error referido a la escala $1$ y usando error relativo al valor exacto. Para una tolerancia $0<\tau<1$, determina en cada caso el dominio máximo dentro de $x\ge0$.

**Solución.** La diferencia es $1-1/(1+x)=x/(1+x)$. Referida a la escala $1$, la condición es $x/(1+x)\le\tau$. Como el denominador es positivo, multiplicar no cambia el sentido de la desigualdad; queda $(1-\tau)x\le\tau$, equivalente a $0\le x\le\tau/(1-\tau)$. Para referirla al valor exacto hay que dividir por $1/(1+x)>0$, de modo que el error relativo es $x$ y el dominio es $0\le x\le\tau$. Ambas respuestas son exactas para el criterio declarado. Una tolerancia numérica idéntica produce dominios diferentes porque cambió la referencia del error.

[]{#fispm-t1-c06-e0002}

**Ejercicio 6.2.** En un dominio común se conocen $|q_0-q_1|\le0.02S$ y $|q_1-q_2|\le0.03S$. Demuestra una garantía para $q_2$. Si la segunda cota estuviera referida a $10S$, ¿qué garantía quedaría? Explica por qué ninguna de ellas demuestra que el error alcance el máximo permitido.

**Solución.** proposición 6.1 da $|q_0-q_2|\le0.05S$ en el primer caso. En el segundo, $0.03(10S)=0.30S$, por lo que la misma prueba da $0.32S$. Las cifras $0.02$ y $0.03$ sólo pueden sumarse tras expresar las cotas sobre la misma escala. Son límites superiores: si los defectos tienen signos opuestos pueden cancelarse, y si ambas aproximaciones son exactas el error es cero. La garantía no es una predicción del error efectivo.

La distancia inicial ofrece ya una aproximación controlada, pero todavía deja abierta la elección de $L$ como referencia. Esa elección pertenece al problema físico y determina qué cociente habrá que observar.

Referencia interna utilizada: [capítulo 3, §12](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md#fispm-c03-robustez-cotas-y-estimaciuxf3n-por-caminos-independientes). El ejemplo y la proposición son construcciones propias.

[]{#fispm-t1-c06-s02}

[]{#fpm-i-06-s02}

## 6.2. Escalas y variables adimensionales: interfaz con el capítulo 2 {#fispm-c06-escalas-y-variables-adimensionales-interfaz-con-fpm-i-02}

El capítulo 2 construyó las escalas características y la adimensionalización. Aquí se usan para decidir qué simplificación conviene probar. La elección de una escala reorganiza el modelo y hace visibles ciertas razones; por sí sola no elimina ningún término.

Consideremos la relación $$q+\frac{q^2}{Q}=b, \qquad Q>0,\quad b\ge0,\quad q\ge0,$$ en la que $q,Q,b$ tienen el mismo tipo de magnitud. Se adopta como modelo algebraico de una respuesta con una contribución proporcional a $q$ y otra cuadrática. No se afirma que sea una ley física universal. Su utilidad didáctica consiste en que permite seguir exactamente qué información conserva cada reducción.

Si se escoge $Q$ como escala de $q$, las variables $y=q/Q$ y $a=b/Q$ convierten la relación en $y+y^2=a$. La suma queda libre de unidades explícitas y el tamaño de la entrada se expresa mediante $a$. Si, en cambio, se escoge una escala positiva general $S$, la sustitución $q=Sy$ da $$y+\varepsilon y^2=a, \qquad \varepsilon=\frac{S}{Q},\qquad a=\frac bS.$$ Ambas formas describen el mismo modelo. La segunda separa dos números adimensionales que pueden variar de maneras diferentes cuando cambian los datos.

[]{#la-relación-normalizada}

### 6.2.1. La relación normalizada {#fispm-c06-la-relaciuxf3n-normalizada}

[]{#fispm-t1-c06-d0002}

**Definición 6.2 --- Relación de modelo en variables normalizadas.** Llamaremos relación normalizada a la expresión de un modelo obtenida sustituyendo cada cantidad por su escala positiva multiplicada por su variable adimensional y dividiendo, cuando corresponda, por una escala común no nula de los términos de la relación. Las escalas y variables son las del capítulo 2; esta definición nombra la forma de trabajo que usaremos al comparar términos.

En el ejemplo, dividir por $S$ es legítimo porque $S>0$. Las condiciones $q\ge0$ y $b\ge0$ se convierten en $y\ge0$ y $a\ge0$: adimensionalizar no autoriza a olvidar las restricciones de dominio. La variable $y$ conserva una lectura física, pues cuenta cuántas veces la respuesta contiene la escala escogida.

[]{#fispm-t1-c06-mp0002}

**Principio 6.2 --- Elegir escalas conservando su interpretación.** Una escala debe justificarse por los datos, la geometría o la pregunta. Después de normalizar se conservan sus relaciones con las cantidades originales para poder interpretar tanto el resultado como su error.

El modelo también muestra el peligro de mirar sólo el coeficiente $\varepsilon$. Aunque $\varepsilon$ sea pequeño, la razón del término cuadrático al término lineal es $\varepsilon y$ para $y>0$. Si $y$ aumenta lo suficiente, el término cuadrático deja de ser pequeño. La normalización hace visible esta dependencia; la sección siguiente fijará cómo expresar el régimen.

[]{#cambiar-la-referencia-sin-cambiar-la-exactitud}

### 6.2.2. Cambiar la referencia sin cambiar la exactitud {#fispm-c06-cambiar-la-referencia-sin-cambiar-la-exactitud}

[]{#fispm-t1-c06-p0002}

**Proposición 6.2 --- Invariancia del error relativo bajo escala común.** Sean $q\ne0$ y $\widetilde q$ cantidades del mismo tipo. Para cualquier escala $S>0$, si $y=q/S$ y $\widetilde y=\widetilde q/S$, entonces $$\frac{|y-\widetilde y|}{|y|} =\frac{|q-\widetilde q|}{|q|}.$$

**Demostración.** El numerador de la izquierda es $|q-\widetilde q|/S$ y su denominador es $|q|/S$. Dividir cancela el factor positivo $1/S$. La condición $q\ne0$ garantiza que ambos cocientes estén definidos. $\square$

La invariancia se refiere al error relativo respecto al valor exacto. El error referido a una escala elegida, $|q-\widetilde q|/S$, sí cambia al cambiar esa escala. No hay contradicción: uno compara con el valor de la cantidad y el otro con una referencia escogida. Tampoco se está afirmando que el cambio de escala altere la discrepancia física $|q-\widetilde q|$.

Para mantener separadas las operaciones, una relación normalizada se escribirá con igualdad exacta mientras sólo haya sustituciones reversibles. El signo de aproximación aparecerá cuando se omita una contribución o se sustituya una función por otra.

[]{#ejercicios-1}

### 6.2.3. Ejercicios {#fispm-c06-ejercicios-1}

[]{#fispm-t1-c06-e0003}

**Ejercicio 6.3.** Normaliza $q+q^2/Q=b$, primero mediante $Q$ y después mediante $b$ cuando $b>0$. Indica las restricciones y explica qué coeficiente permite comparar los dos términos de la segunda forma.

**Solución.** Con $y=q/Q$ y $a=b/Q$, sustituir y dividir por $Q>0$ da $y+y^2=a$, con $y,a\ge0$. Para $b>0$, ponemos $z=q/b$ y $\eta=b/Q$; dividir por $b$ da $z+\eta z^2=1$, con $z\ge0$ y $\eta>0$. Si $z>0$, la razón cuadrático/lineal es $\eta z$. El coeficiente $\eta$ es un parámetro, pero el tamaño relativo del término depende también de la solución $z$. Cuando $b=0$, la escala $b$ no está permitida; la primera normalización sigue disponible y el dominio original exige $q=0$. Las dos formas para $b>0$ se conectan mediante $y=az$ y $\eta=a$.

[]{#fispm-t1-c06-e0004}

**Ejercicio 6.4.** Sean $Q'=cQ$, $c>0$, y las coordenadas normalizadas $y=q/Q$, $y'=q/Q'$. Haz lo mismo para un candidato $\widetilde q$. Compara los errores normalizados y relativos. En este ejercicio $Q'$ cambia la referencia de representación; no se cambia el parámetro físico $Q$ del modelo anterior.

**Solución.** Las nuevas coordenadas satisfacen $y'=y/c$ y $\widetilde y'=\widetilde y/c$. Por tanto, $|y'-\widetilde y'|=|y-\widetilde y|/c$. El número que expresa el error sobre la referencia escogida cambia. Si $q\ne0$, dividir por $|y'|=|y|/c$ recupera el mismo error relativo. Si $q=0$, esa comparación relativa no está definida, aunque ambos errores referidos a escala sí lo estén. Elegir una escala mayor puede hacer pequeño el número normalizado; no mejora la aproximación.

Referencia interna utilizada: [capítulo 2, §9](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md#fispm-c02-escalas-caracteruxedsticas-y-uxf3rdenes-de-magnitud) y [capítulo 2, §10](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md#fispm-c02-adimensionalizaciuxf3n-e-inferencia-dimensional). No se reconstruye la teoría dimensional ni Buckingham.

[]{#parámetros-adimensionales-y-definición-de-régimen}

[]{#fispm-t1-c06-s03}

[]{#fpm-i-06-s03}

## 6.3. Parámetros adimensionales y definición de régimen {#fispm-c06-paruxe1metros-adimensionales-y-definiciuxf3n-de-ruxe9gimen}

En la relación $y+\varepsilon y^2=a$, decir «$\varepsilon$ es pequeño» deja una parte del problema sin especificar. Si $y$ permanece cercano a uno, la contribución cuadrática es pequeña frente a la lineal. Si $y$ se acerca a $1/\varepsilon$, ambas contribuciones tienen tamaños comparables. La misma familia puede recorrer situaciones distintas según cómo varíe $a$ y qué valores alcance la solución.

La diferencia aparece incluso antes de resolver una ecuación. Para $0<\varepsilon\le1$, la función $\varepsilon x$ tiende a cero cuando $x$ queda fijo. En el dominio $0\le x\le1$ tenemos la garantía $0\le\varepsilon x\le\varepsilon$. En el dominio creciente $0\le x\le1/\varepsilon$, el extremo $x=1/\varepsilon$ produce el valor $1$ para todo $\varepsilon$. La pequeñez del parámetro no basta para controlar una expresión en cualquier dominio.

[]{#régimen-y-límite}

### 6.3.1. Régimen y límite {#fispm-c06-ruxe9gimen-y-luxedmite}

[]{#fispm-t1-c06-d0003}

**Definición 6.3 --- Régimen de trabajo.** Un régimen es un conjunto explícito de condiciones sobre datos, variables y parámetros dentro del cual se formula una aproximación o comparación de tamaños. Si la comparación se refiere a un límite, se indica qué parámetro tiende a qué valor, qué cantidades quedan fijas y qué dominio se controla.

Un régimen puede ser finito, por ejemplo $0\le\varepsilon\le0.01$ y $0\le x\le2$. También puede describir una familia límite, como $\varepsilon\to0^+$ con $a$ fijo y positivo. No son declaraciones intercambiables: un límite dice cómo se comporta una familia; una aplicación concreta exige además escoger un umbral que garantice la tolerancia requerida.

En este capítulo $\varepsilon\ll1$ será una abreviatura interpretativa, respaldada por un límite o por una desigualdad cuantitativa. No fijaremos un número universal para «mucho menor». El umbral depende de la expresión y del error permitido. En geometría, $|h|/L\le0.1$ garantizaba una pérdida de distancia no mayor que $0.005L$; otro modelo puede necesitar un cociente más pequeño para la misma tolerancia.

[]{#fispm-t1-c06-mp0003}

**Principio 6.3 --- Declarar la familia comparada.** En un razonamiento con parámetro pequeño hay que registrar qué varía junto con él. Una cota demostrada para datos fijos no se convierte automáticamente en una cota válida para datos que aumentan cuando el parámetro disminuye.

[]{#control-puntual-y-control-sobre-un-dominio}

### 6.3.2. Control puntual y control sobre un dominio {#fispm-c06-control-puntual-y-control-sobre-un-dominio}

La diferencia entre comprobar cada valor fijo y controlar todo un dominio admite una formulación elemental. Para una función $r(\varepsilon,x)$, comprobar $r(\varepsilon,x)\to0$ para cada $x$ fijo permite que el umbral elegido dependa de ese $x$. Una garantía uniforme en un dominio $X_\varepsilon$ exige una cota válida simultáneamente para todos sus puntos, con el mismo umbral.

No hace falta introducir todavía una nueva notación para reconocer el problema. Si $|r(\varepsilon,x)|\le C\varepsilon$ para todos los $x$ admitidos, con $C$ independiente de $\varepsilon$ y $x$, entonces cualquier tolerancia $\tau>0$ queda garantizada al exigir $0<\varepsilon\le\tau/C$, cuando $C>0$. Si la supuesta constante aumenta como $1/\varepsilon$, la conclusión desaparece.

En una aplicación física, el dominio puede ser un intervalo de posiciones, alturas o tiempos. La condición de validez debe acompañar ese intervalo: una descripción local de una curva no promete representar todo el movimiento. El capítulo 5 ya separó la información local de una curva de su recorrido completo; aquí esa separación se convierte en una obligación de aproximación.

[]{#ejercicios-2}

### 6.3.3. Ejercicios {#fispm-c06-ejercicios-2}

[]{#fispm-t1-c06-e0005}

**Ejercicio 6.5.** Para $r(\varepsilon,x)=\varepsilon x$, $0<\varepsilon\le1$, determina el mayor tamaño de $|r|$ en los dominios $[0,1]$ y $[0,1/\varepsilon]$. Compara con el límite para $x$ fijo. ¿En cuál de los dos dominios puedes garantizar $|r|\le0.01$ sólo imponiendo que $\varepsilon$ sea suficientemente pequeño?

**Solución.** La función es creciente en $x\ge0$. En $[0,1]$ el máximo es $\varepsilon$, así que $\varepsilon\le0.01$ basta. En $[0,1/\varepsilon]$ el máximo es $1$, por lo que ningún umbral positivo de $\varepsilon$ garantiza la tolerancia en todo el dominio. Para cada $x$ fijo y finito, $\varepsilon x\to0$; si $x>0$, basta $\varepsilon\le0.01/x$ para ese punto. Esa elección depende de $x$ y no resuelve el segundo problema. El fallo no está en el límite puntual, sino en utilizarlo como garantía simultánea sobre un intervalo que crece.

**Ejercicio 6.6.** Para $f(\varepsilon)=1/(1+\varepsilon)$, $\varepsilon\ge0$, busca el régimen exacto que permite sustituir $f$ por $1$ con error referido a la escala $1$ no mayor que $\tau$, donde $0<\tau<1$. Interpreta el caso $\tau=0.02$ y distingue un umbral necesario y suficiente de uno meramente suficiente.

**Solución.** La diferencia es $\varepsilon/(1+\varepsilon)$. Resolver la desigualdad como en el ejercicio 6.1 da $\varepsilon\le\tau/(1-\tau)$. Para $\tau=0.02$, el umbral exacto es $1/49$, aproximadamente $0.020408$. La condición más simple $\varepsilon\le0.02$ también garantiza la tolerancia, pues $\varepsilon/(1+\varepsilon)\le\varepsilon$, pero excluye algunos valores permitidos. El primer umbral es necesario y suficiente para el criterio elegido; el segundo sólo es suficiente. En ambos se explica qué significa «pequeño».

Referencia: Hinch, *Perturbation Methods* (1991), cap. 1, §§1.1--1.2, pp. 1--7.

[]{#comparar-tamaños-órdenes-de-magnitud}

[]{#fispm-t1-c06-s04}

[]{#fpm-i-06-s04}

## 6.4. Comparar tamaños: órdenes de magnitud {#fispm-c06-comparar-tamauxf1os-uxf3rdenes-de-magnitud}

Antes de eliminar un término conviene escribir la comparación que lo autoriza. En $y+\varepsilon y^2=a$, el coeficiente $\varepsilon$ no es el objeto que se compara con $y$. Para $y>0$, el cociente pertinente es $(\varepsilon y^2)/y=\varepsilon y$. Esta operación exige comparar términos del mismo tipo de magnitud; si se comparan cantidades de dimensiones distintas, primero debe justificarse una normalización que las lleve a una misma relación.

El capítulo 2 y capítulo 3 introdujeron órdenes de magnitud como escalas numéricas. El trabajo presente necesita además saber cómo cambia una razón dentro de una familia. Dos números cercanos en una situación concreta no necesariamente conservan esa cercanía al variar el parámetro.

[]{#dos-relaciones-diferentes}

### 6.4.1. Dos relaciones diferentes {#fispm-c06-dos-relaciones-diferentes}

[]{#fispm-t1-c06-d0004}

**Definición 6.4 --- Término subdominante.** Sean $A(\varepsilon)$ y $B(\varepsilon)$ términos comparables dimensionalmente, con $B(\varepsilon)\ne0$ para $0<\varepsilon<\varepsilon_0$. Diremos que $A$ es subdominante respecto a $B$ cuando $\varepsilon\to0^+$ si $$\frac{|A(\varepsilon)|}{|B(\varepsilon)|}\longrightarrow0.$$ Si hay otras variables en un dominio declarado, una afirmación uniforme exige que la misma pequeñez se alcance simultáneamente en ese dominio.

La definición compara módulos y no signos. Un término puede ser negativo y subdominante. Tampoco afirma que $A$ tienda a cero: si $A=\varepsilon^{-1}$ y $B=\varepsilon^{-2}$, ambos crecen en módulo, pero la razón es $\varepsilon$.

[]{#fispm-t1-c06-d0005}

**Definición 6.5 --- Términos comparables en tamaño.** En un régimen, dos términos no nulos $A,B$ son comparables si existen constantes $c,C>0$, independientes de los puntos de ese régimen, tales que $$c\le\frac{|A|}{|B|}\le C.$$ Para un régimen límite, las cotas han de valer en un intervalo suficientemente pequeño del parámetro.

Comparabilidad no significa igualdad ni razón tendiendo a uno. Los términos $2\varepsilon^2$ y $\varepsilon^2$ son comparables y mantienen razón $2$. El símbolo $\sim$, cuando se emplee con significado asintótico, se reservará a una razón que tiende a uno; no se usará aquí como abreviatura de comparabilidad. Esta convención evita trasladar inadvertidamente los distintos usos de «orden» de capítulos anteriores.

[]{#una-clasificación-reutilizable}

### 6.4.2. Una clasificación reutilizable {#fispm-c06-una-clasificaciuxf3n-reutilizable}

[]{#fispm-t1-c06-p0003}

**Proposición 6.3 --- Comparación de potencias.** Sean $A=c\varepsilon^\alpha$ y $B=d\varepsilon^\beta$, con $c,d$ constantes reales no nulas, $\alpha,\beta\in\mathbb R$ y $0<\varepsilon\to0$. Entonces $A$ es subdominante respecto a $B$ si $\alpha>\beta$; son comparables si $\alpha=\beta$; y $B$ es subdominante respecto a $A$ si $\alpha<\beta$.

**Demostración.** El cociente de módulos es $|c/d|\varepsilon^{\alpha-\beta}$. Si el exponente es positivo, tiende a cero; si es cero, vale la constante positiva $|c/d|$; si es negativo, su inversa tiende a cero. Son las tres posibilidades exhaustivas para $\alpha-\beta$. $\square$

Para $0<\varepsilon\le1$, esta clasificación sitúa $\varepsilon^3$ por debajo de $\varepsilon^2$, pero no convierte $10^6\varepsilon^3$ en un término despreciable para todo valor del intervalo. Su razón a $\varepsilon^2$ es $10^6\varepsilon$; un problema con tolerancia $0.01$ exige $\varepsilon\le10^{-8}$. El límite reconoce la jerarquía eventual; la cota establece cuándo puede utilizarse.

[]{#cancelaciones-y-cantidades-objetivo}

### 6.4.3. Cancelaciones y cantidades objetivo {#fispm-c06-cancelaciones-y-cantidades-objetivo}

Comparar los sumandos no siempre basta para controlar su suma. La expresión $(1+\varepsilon)-1=\varepsilon$ contiene dos términos comparables de tamaño cercano a uno, cuya diferencia es mucho menor. Sustituir $1+\varepsilon$ por $1$ tiene un defecto pequeño frente a uno, pero destruye la diferencia completa. Si la observable que interesa es ese incremento, la aproximación debe juzgarse respecto al incremento.

[]{#fispm-t1-c06-mp0004}

**Principio 6.4 --- Comparar términos completos y revisar cancelaciones.** Una comparación debe incluir coeficientes, variables y dominio. Si el denominador elegido puede anularse, hay que separar esos puntos o usar una escala positiva distinta. Cuando la observable resulta de una cancelación, se controla el error después de formar esa observable.

La advertencia tiene una interpretación geométrica inmediata. En la distancia de §1, aproximar $d$ por $L$ puede ser adecuado para la distancia total y ser inadecuado para estudiar cuánto aumenta respecto a $L$. La pregunta decide cuál de las dos diferencias necesita conservarse.

[]{#ejercicios-3}

### 6.4.4. Ejercicios {#fispm-c06-ejercicios-3}

[]{#fispm-t1-c06-e0007}

**Ejercicio 6.7.** Clasifica $A=\varepsilon^3$, $B=\varepsilon^2$ y $C=\varepsilon^2(2+\varepsilon)$ para $0<\varepsilon\le1$ y en el límite $\varepsilon\to0^+$. Escribe una cota bilateral y dos cocientes que tiendan a cero.

**Solución.** Se tiene $C/B=2+\varepsilon$, de modo que $2<C/B\le3$; por tanto $B$ y $C$ son comparables. Además, $A/B=\varepsilon\to0$ y $A/C=\varepsilon/(2+\varepsilon)\le\varepsilon/2\to0$. En el intervalo completo los cocientes son positivos y están acotados, pero la palabra «subdominante» describe su comportamiento límite. Ninguna igualdad $B=C$ se deduce de la comparabilidad.

[]{#fispm-t1-c06-e0008}

**Ejercicio 6.8.** Un informe sustituye $1+\varepsilon$ por $1$ y concluye que el incremento $(1+\varepsilon)-1$ queda bien aproximado por cero. Calcula el error relativo del incremento para $\varepsilon>0$. Otro informe elimina $\varepsilon x^2$ frente a $x$ porque $0<\varepsilon\ll1$, sin restringir $x>0$. Encuentra valores que refuten su argumento.

**Solución.** El incremento exacto es $\varepsilon$ y el aproximado es cero. El error relativo es $|\varepsilon-0|/\varepsilon=1$, aunque el error respecto a la escala $1$ sea $\varepsilon$. La primera conclusión confunde las dos observables. En el segundo caso, la razón es $\varepsilon x$. Para $x=1/\varepsilon$ vale $1$; para $x=1/\varepsilon^2$ vale $1/\varepsilon$ y aumenta sin cota al disminuir el parámetro. El coeficiente pequeño no justifica la eliminación. Una reparación posible es declarar un dominio $0<x\le X$ con $X$ fijo y exigir $\varepsilon X$ menor que la tolerancia.

Referencias internas utilizadas: [capítulo 2, §9](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md#fispm-c02-escalas-caracteruxedsticas-y-uxf3rdenes-de-magnitud) y [capítulo 3, §10](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md#fispm-c03-estimaciuxf3n-fuxedsica-y-uxf3rdenes-de-magnitud). Las definiciones comparativas y proposición 6.3 se construyen localmente.

[]{#términos-dominantes-y-balance-dominante}

[]{#fispm-t1-c06-s05}

[]{#fpm-i-06-s05}

## 6.5. Términos dominantes y balance dominante {#fispm-c06-tuxe9rminos-dominantes-y-balance-dominante}

La relación normalizada $y+\varepsilon y^2=a$, con $a,\varepsilon>0$ y $y\ge0$, puede simplificarse de dos maneras que parecen incompatibles. Si se omite el término cuadrático, queda $y=a$. Si se omite el término lineal, queda $\varepsilon y^2=a$ y, en el dominio no negativo, $y=\sqrt{a/\varepsilon}$. Elegir una de esas respuestas por la apariencia del coeficiente deja sin resolver el problema principal: qué término es pequeño sobre la respuesta que acabamos de obtener.

[]{#fig:I-06-R03}

<figure id="fig-fpm-v04-i-06-r03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-06-R03.svg" class="lightbox" data-gallery="fpm-v04-c06"><img src="/assets/books/fispm/v04/I-06-R03.svg" alt="El término dominante puede cambiar. Diagrama del capítulo 6; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="408" height="246" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 6.1.** Los términos $u$ y $\varepsilon u^2$, con $\varepsilon=0{,}1$, son iguales en $u=10$. El segundo es pequeño respecto del primero sólo si $\varepsilon u\ll1$, aunque $\varepsilon$ sea pequeño. Véase §[6.5](#fispm-c06-tuxe9rminos-dominantes-y-balance-dominante).

</figcaption>

</figure>

Para el primer candidato, la razón cuadrático/lineal vale $\varepsilon a$. Para el segundo, la razón lineal/cuadrático vale $1/\sqrt{\varepsilon a}$. Las dos reducciones proponen regímenes diferentes de la misma relación. La combinación $\eta=\varepsilon a$ decide cuál de las comparaciones puede hacerse pequeña. Un parámetro $\varepsilon$ diminuto no impide que $\eta$ sea grande si la entrada $a$ aumenta lo suficiente.

La ecuación completa tiene una solución positiva: la función $F(y)=y+\varepsilon y^2-a$ es continua, satisface $F(0)<0$ y $F(a)>0$, y es estrictamente creciente para $y\ge0$. El teorema del valor intermedio da existencia, y el crecimiento estricto da unicidad. Este control usa cálculo de una variable; no se introduce una ecuación de evolución.

[]{#qué-se-conserva-en-un-balance}

### 6.5.1. Qué se conserva en un balance {#fispm-c06-quuxe9-se-conserva-en-un-balance}

[]{#fispm-t1-c06-d0006}

**Definición 6.6 --- Balance dominante.** Para una relación normalizada $\sum_{j=1}^n T_j=0$, un balance dominante propuesto consiste en conservar un conjunto de términos capaces de compensarse y resolver la relación reducida obtenida al omitir los demás. Se valida su jerarquía comparando, sobre el candidato obtenido y en el régimen declarado, los términos omitidos con una escala positiva del tamaño de los conservados. En un régimen límite, los cocientes omitidos deben tender a cero; para un uso cuantitativo se exige una cota explícita. Esta validación de tamaños todavía no constituye por sí sola una cota del error de la solución.

Una referencia posible es $B=\sum_{j\in J}|T_j|$, donde $J$ enumera los términos conservados y $B>0$. Esa suma de módulos no desaparece por la cancelación que la ecuación reducida necesita. Usar como denominador la suma con signos de los conservados sería inútil sobre una solución de la relación reducida: precisamente allí esa suma es cero.

En el primer candidato del ejemplo, se conservan $y$ y $-a$, cuyos módulos valen $a$. El término omitido es $\varepsilon a^2$; respecto a la escala $a$, su tamaño es $\eta$. En el segundo candidato se conservan $\varepsilon y^2$ y $-a$, y el término omitido tiene tamaño relativo $1/\sqrt\eta$. El balance incluye signos, dominio y tamaños. Una lista de términos grandes sin posibilidad de cancelación no puede satisfacer una ecuación de suma nula.

[]{#fispm-t1-c06-p0004}

**Proposición 6.4 --- Un único término dominante no puede anularse mediante términos subdominantes.** Supongamos que, para todo parámetro suficientemente pequeño, $\sum_{j=1}^n T_j(\varepsilon)=0$ y $T_k(\varepsilon)\ne0$. Es imposible que $|T_j/T_k|\to0$ para todos los $j\ne k$.

**Demostración.** Dividir la igualdad exacta por $T_k$ da $1+\sum_{j\ne k}T_j/T_k=0$. Cada cociente de la suma tiende a cero por la hipótesis sobre su módulo. Como hay un número finito de términos, tomar el límite produciría $1=0$. $\square$

La finitud interviene en el paso al límite de la suma. La proposición no dice que toda ecuación tenga exactamente dos términos principales ni que éstos deban ser iguales en módulo. Dice que un término no nulo no puede quedar solo frente a una colección finita de términos despreciables respecto a él.

[]{#fispm-t1-c06-mp0005}

**Principio 6.5 --- Proponer, resolver y comprobar.** Después de proponer un balance se resuelve su relación reducida en el dominio permitido y se insertan sus candidatos en las razones que justifican las omisiones. Un balance rechazado por signos o por tamaños no se salva porque su fórmula resulte simple.

[]{#ejercicios-4}

### 6.5.2. Ejercicios {#fispm-c06-ejercicios-4}

[]{#fispm-t1-c06-e0009}

**Ejercicio 6.9.** Para $y+\varepsilon y^2=a$, $a,\varepsilon>0$, construye los candidatos obtenidos omitiendo respectivamente el término cuadrático y el lineal. Calcula sobre cada candidato la razón del término omitido al término conservado que depende de $y$. Evalúa las razones cuando $\varepsilon=10^{-3}$ y $a$ vale $10$, $10^3$ y $10^6$. No identifiques todavía esas razones con el error relativo de la solución.

**Solución.** El candidato lineal es $y_{\mathrm L}=a$, y la razón omitido/conservado es $\varepsilon a=\eta$. El candidato cuadrático es $y_{\mathrm C}=\sqrt{a/\varepsilon}$, y la razón es $y_{\mathrm C}/(\varepsilon y_{\mathrm C}^2)=1/\sqrt\eta$. Para los tres datos se obtiene:

  $a$      $\eta$   Razón en $y_{\mathrm L}$   Razón en $y_{\mathrm C}$
  -------- -------- -------------------------- ------------------------------
  $10$     $0.01$   $0.01$                     $10$
  $10^3$   $1$      $1$                        $1$
  $10^6$   $10^3$   $10^3$                     $1/\sqrt{10^3}\approx0.0316$

El primer dato favorece el balance lineal y el tercero el cuadrático. El dato intermedio no justifica ninguna de las dos omisiones mediante una razón pequeña. Para convertir estos diagnósticos en garantías de error hará falta controlar cómo el defecto de la ecuación afecta a su solución.

[]{#fispm-t1-c06-e0010}

**Ejercicio 6.10.** Se propone buscar una raíz positiva de $\varepsilon y^2+y+1=0$, con $\varepsilon>0$, eliminando $y$ y compensando el término cuadrático con la constante. Localiza el fallo antes de comparar tamaños y demuestra que la ecuación completa tampoco tiene raíces positivas.

**Solución.** La relación reducida sería $\varepsilon y^2+1=0$. Su primer sumando es no negativo y el segundo es positivo; no pueden compensarse en los reales. Para $y>0$, los tres sumandos de la relación completa son positivos, por lo que su suma es positiva. Tampoco $y=0$ es raíz. La eliminación no falló por escoger mal un umbral: el balance contradice los signos del modelo. Una comparación de módulos por sí sola habría ocultado esa imposibilidad.

Referencia: Hinch, *Perturbation Methods* (1991), cap. 1, §§1.1--1.2, pp. 1--7.

[]{#error-residuo-y-calidad-de-una-aproximación}

[]{#fispm-t1-c06-s06}

[]{#fpm-i-06-s06}

## 6.6. Error, residuo y calidad de una aproximación {#fispm-c06-error-residuo-y-calidad-de-una-aproximaciuxf3n}

Un candidato puede satisfacer casi una ecuación y aun así estar lejos de su solución. Para reconocer esa posibilidad hay que distinguir dos defectos: el de la cantidad aproximada y el de la relación en la que se la inserta.

[]{#fig:I-06-N02}

<figure id="fig-fpm-v04-i-06-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-06-N02.svg" class="lightbox" data-gallery="fpm-v04-c06"><img src="/assets/books/fispm/v04/I-06-N02.svg" alt="Cota de un residuo. Diagrama del capítulo 6; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="408" height="253" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 6.2.** En $0\le x\le1$, $0\le x-\sin x\le x^3/6$. La curva continua es el error y la discontinua su cota; aquí ambos se calculan con el mismo argumento adimensional. Véase §[6.6](#fispm-c06-error-residuo-y-calidad-de-una-aproximaciuxf3n).

</figcaption>

</figure>

Si la distancia exacta del modelo geométrico es $d$ y se utiliza $\widetilde d$, el defecto $|\widetilde d-d|$ compara distancias. Si la relación que define $d$ se escribe como $d^2-L^2-h^2=0$, sustituir $\widetilde d$ produce $\widetilde d^2-L^2-h^2$, una cantidad con dimensiones de longitud al cuadrado. Ambos defectos pueden relacionarse, pero no tienen el mismo tipo ni se comparan directamente mediante sus valores numéricos.

[]{#medir-el-error-de-la-observable}

### 6.6.1. Medir el error de la observable {#fispm-c06-medir-el-error-de-la-observable}

[]{#fispm-t1-c06-d0007}

**Definición 6.7 --- Errores de aproximación.** Para cantidades escalares comparables $q,\widetilde q$, el error absoluto es $e_{\mathrm{abs}}=|\widetilde q-q|$. Si $q\ne0$, el error relativo al valor exacto es $e_{\mathrm{rel}}=|\widetilde q-q|/|q|$. Para una escala positiva declarada $S$, el error referido a esa escala es $e_S=|\widetilde q-q|/S$.

El error absoluto conserva el tipo de la observable; los otros dos son adimensionales. El error relativo requiere un denominador no nulo. Cerca de un cero puede crecer aunque el error absoluto sea pequeño, y en el cero no está definido. En ese caso se puede adoptar una escala positiva pertinente, sin llamar a la nueva razón «error relativo al valor exacto».

Estos errores comparan dos predicciones o una predicción completa con su reducción. La incertidumbre experimental del capítulo 3 caracteriza lo que un procedimiento de medición permite conocer. Una cota matemática de reducción no es una incertidumbre estándar ni un intervalo probabilístico. Si el modelo omite un rasgo relevante del fenómeno, disminuir el error de la reducción no corrige por sí solo esa omisión.

[]{#sustituir-en-la-relación-original}

### 6.6.2. Sustituir en la relación original {#fispm-c06-sustituir-en-la-relaciuxf3n-original}

[]{#fispm-t1-c06-d0008}

**Definición 6.8 --- Residuo.** Para una relación $F(q;\lambda)=0$ y un candidato $\widetilde q$, su residuo es $r=F(\widetilde q;\lambda)$, conservando fijos los datos $\lambda$. Si $R_F>0$ es una escala del mismo tipo que $F$, el residuo normalizado es $|r|/R_F$.

Esta definición no presupone que se conozca la solución exacta. Ésa es una ventaja práctica: puede comprobarse el residuo de un candidato antes de resolver el modelo completo. La dificultad está en interpretar qué dice esa comprobación sobre la observable. Multiplicar una ecuación por una constante pequeña multiplica su residuo y deja intactas sus raíces. Por ello el tamaño bruto del residuo depende también de cómo se escribió la relación.

En $F(y)=y+\varepsilon y^2-a$, el candidato $y=a$ tiene residuo $\varepsilon a^2$. Su valor referido a la entrada $a>0$ es $\varepsilon a$. Esa cifra coincide con una razón de tamaños de §5, pero la coincidencia no demuestra todavía que sea el error relativo de $y$. Falta estudiar la sensibilidad de la relación.

[]{#cuándo-un-residuo-controla-el-error}

### 6.6.3. Cuándo un residuo controla el error {#fispm-c06-cuuxe1ndo-un-residuo-controla-el-error}

[]{#fispm-t1-c06-p0005}

**Proposición 6.5 --- Control mediante una pendiente mínima.** Sea $F$ continua en un intervalo cerrado $I=[u,v]$, diferenciable en su interior, y supongamos $|F'(x)|\ge m>0$ en ese interior. Si $q_\ast,\widetilde q\in I$ y $F(q_\ast)=0$, entonces $$|\widetilde q-q_\ast|\le\frac{|F(\widetilde q)|}{m}.$$

**Demostración.** Si ambos puntos coinciden, la cota es inmediata. Si son distintos, el teorema del valor medio, aplicado al segmento que los une, proporciona un punto $\xi$ interior a ese segmento tal que $F(\widetilde q)-F(q_\ast)=F'(\xi)(\widetilde q-q_\ast)$. Como $F(q_\ast)=0$, tomar módulos da $|F(\widetilde q)|\ge m|\widetilde q-q_\ast|$. Dividir por $m>0$ concluye la prueba. $\square$

La proposición supone que existe una raíz en el intervalo; el residuo no establece esa existencia. También necesita una pendiente mínima defendible en todo el segmento relevante. Si $m$ es diminuto, un residuo pequeño puede permitir un error considerable. En la relación algebraica de §5, $F'(y)=1+2\varepsilon y\ge1$ para $y\ge0$; una vez encerradas raíz y candidato en un intervalo no negativo, puede usarse $m=1$.

[]{#fispm-t1-c06-mp0006}

**Principio 6.6 --- Acompañar el residuo con sensibilidad.** Un residuo pequeño sólo certifica una solución próxima cuando se dispone de una estimación que conecte ambos defectos y se cumplen sus hipótesis. La normalización del residuo ayuda a comparar escalas, pero no sustituye ese argumento.

Si se reemplaza $F$ por $\widehat F=\delta F$, con $\delta>0$, el residuo pasa a $\delta r$ y la pendiente mínima a $\delta m$. El cociente de la proposición 6.5 permanece $|r|/m$. Una ecuación puede hacerse parecer mejor satisfecha cambiando su factor global; la cota correcta no mejora por ese cambio de escritura.

[]{#ejercicios-5}

### 6.6.4. Ejercicios {#fispm-c06-ejercicios-5}

[]{#fispm-t1-c06-e0011}

**Ejercicio 6.11.** Para una escala $S>0$, una observable vale $q=0.002S$ y su aproximación es $\widetilde q=0.003S$. Calcula los tres errores de la definición 6.7. Repite con $q=0$ manteniendo la misma aproximación, y explica qué comparación deja de estar definida.

**Solución.** La diferencia es $0.001S$, de modo que $e_{\mathrm{abs}}=0.001S$, $e_S=0.001$ y $e_{\mathrm{rel}}=0.001/0.002=1/2$. Un error pequeño sobre $S$ representa aquí la mitad del valor objetivo. Si $q=0$, los errores absoluto y referido a escala son $0.003S$ y $0.003$; el relativo al valor exacto no está definido porque exigiría dividir por cero. No corresponde sustituir ese cociente por cero ni por una cifra finita elegida por convenio.

[]{#fispm-t1-c06-e0012}

**Ejercicio 6.12.** Para $\delta>0$, considera $F_\delta(y)=\delta y$, cuya raíz es $0$. Utiliza el candidato $\widetilde y=1$. Demuestra que su residuo puede ser arbitrariamente pequeño aunque el error sea unitario. Comprueba qué predice proposición 6.5.

**Solución.** El residuo es $F_\delta(1)=\delta$, que tiende a cero cuando $\delta\to0^+$. El error respecto a la raíz es $|1-0|=1$, independiente de $\delta$. La derivada vale $\delta$, por lo que proposición 6.5 utiliza $m=\delta$ y da $e_{\mathrm{abs}}\le\delta/\delta=1$. No certifica una proximidad creciente. Si se normaliza la relación por su propio factor $\delta$, queda $y=0$ y el residuo normalizado del candidato es $1$. Tanto la pendiente como la normalización revelan por qué el residuo bruto era engañoso.

[]{#fispm-t1-c06-e0013}

**Ejercicio 6.13.** Sea $F(y)=y+y^2-2$ en $[0,2]$. Verifica que hay una única raíz en ese intervalo y certifica el error del candidato $1.01$ mediante su residuo. Compara con el error exacto e indica por qué una cota puede ser correcta sin ser óptima.

**Solución.** $F(1)=0$ y $F'(y)=1+2y>0$ en el interior; la raíz es única porque $F$ es estrictamente creciente. En todo el intervalo puede emplearse la pendiente mínima $m=1$. El residuo del candidato es $1.01+(1.01)^2-2=0.0301$, así que proposición 6.5 garantiza un error no mayor que $0.0301$. El error exacto es $|1.01-1|=0.01$, que cumple la cota. La estimación usó la pendiente mínima del intervalo completo, inferior a las pendientes próximas a la raíz. Conserva una garantía más amplia a costa de precisión; no afirma que el error efectivo sea $0.0301$.

Referencias utilizadas: [capítulo 3, §12](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md#fispm-c03-robustez-cotas-y-estimaciuxf3n-por-caminos-independientes) para cotas declaradas. La cota del residuo se demuestra mediante el teorema del valor medio.

[]{#linealización-alrededor-de-un-estado-de-referencia}

[]{#fispm-t1-c06-s07}

[]{#fpm-i-06-s07}

## 6.7. Linealización alrededor de un estado de referencia {#fispm-c06-linealizaciuxf3n-alrededor-de-un-estado-de-referencia}

Una función puede resultar complicada en un intervalo amplio y tener una descripción simple cerca de un punto. Si una observable $q=f(x)$ depende de una sola variable, conocer el valor $f(x_0)$ y la pendiente $f'(x_0)$ permite predecir cómo cambia ante un incremento pequeño $h=x-x_0$. La cuestión es qué reemplazo expresa esa información y cuál es su alcance.

[]{#fig:I-06-N01}

<figure id="fig-fpm-v04-i-06-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-06-N01.svg" class="lightbox" data-gallery="fpm-v04-c06"><img src="/assets/books/fispm/v04/I-06-N01.svg" alt="Aproximación angular. Diagrama del capítulo 6; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="383" height="231" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 6.3.** La curva $\sin x$ y su tangente $x$ se comparan en $|x|\le1$, con ángulo en radianes. La proximidad es local: no convierte ambas funciones en idénticas. Véase §[6.7](#fispm-c06-linealizaciuxf3n-alrededor-de-un-estado-de-referencia).

</figcaption>

</figure>

Para la distancia $f(h)=\sqrt{L^2+h^2}$, con $L>0$, el punto base $h=0$ tiene valor $L$ y pendiente cero. Su aproximación de primer orden será constante. En cambio, cerca de una altura base $h=L$, la pendiente no es cero y la descripción local conserva una variación proporcional al incremento. La función es la misma; cambia el estado alrededor del que se pregunta.

[]{#parte-afín-y-parte-lineal}

### 6.7.1. Parte afín y parte lineal {#fispm-c06-parte-afuxedn-y-parte-lineal}

[]{#fispm-t1-c06-d0009}

**Definición 6.9 --- Linealización univariada.** Sea $f$ diferenciable en un punto interior $x_0$ de su dominio. Para $h$ tal que $x_0+h$ pertenezca al dominio, su aproximación afín de primer orden es $$L_{x_0}(h)=f(x_0)+f'(x_0)h.$$ La parte lineal del cambio es $f'(x_0)h$; la función completa de $h$ es afín y sólo es lineal cuando $f(x_0)=0$.

El término independiente conserva el estado base y el coeficiente del incremento conserva la pendiente. Si $x$ tiene dimensiones y $f$ representa una magnitud física, $f'(x_0)$ tiene el tipo de $f$ dividido por el tipo de $x$; su producto con $h$ puede sumarse a $f(x_0)$. La derivada no es necesariamente un número sin unidades.

La diferenciabilidad implica $$\frac{f(x_0+h)-L_{x_0}(h)}{h}\longrightarrow0 \qquad (h\to0,\ h\ne0).$$ En efecto, el cociente es $[f(x_0+h)-f(x_0)]/h-f'(x_0)$, que tiende a cero por la definición de derivada. Esta afirmación controla el defecto en comparación con el incremento de entrada. Todavía no da una cota cuadrática ni un radio numérico de validez.

[]{#por-qué-esa-aproximación-es-la-de-primer-orden}

### 6.7.2. Por qué esa aproximación es la de primer orden {#fispm-c06-por-quuxe9-esa-aproximaciuxf3n-es-la-de-primer-orden}

[]{#fispm-t1-c06-p0006}

**Proposición 6.6 --- Unicidad de la aproximación afín de primer orden.** Si $f$ es diferenciable en $x_0$ y una función afín $A+Bh$ satisface $$\frac{f(x_0+h)-(A+Bh)}{h}\longrightarrow0,$$ entonces $A=f(x_0)$ y $B=f'(x_0)$. Recíprocamente, esos coeficientes satisfacen el límite.

**Demostración.** Por hipótesis, el defecto dividido por $h$ tiende a cero, así que el defecto mismo también tiende a cero. La continuidad de $f$ en $x_0$, consecuencia de su diferenciabilidad, da $f(x_0)-A=0$. Con $A=f(x_0)$, el cociente de la hipótesis se convierte en el cociente incremental de $f$ menos $B$. Su límite es $f'(x_0)-B$, que debe ser cero. La recíproca es la identidad con el cociente incremental escrita antes del enunciado. $\square$

La propiedad selecciona los coeficientes por un criterio matemático, no por un ajuste arbitrario a dos valores cercanos. Una recta secante puede servir como otro modelo aproximado, pero coincide con esta aproximación de primer orden sólo si se justifican las relaciones pertinentes entre sus coeficientes y el punto base.

[]{#fispm-t1-c06-mp0007}

**Principio 6.7 --- Declarar la referencia antes de linealizar.** Se identifica la variable independiente, el punto base, el incremento y la observable cuyo cambio interesa. La aproximación resultante se interpreta respecto a ese estado; no se traslada a otro punto o a todo el dominio sin control adicional.

[]{#cuando-la-pendiente-desaparece}

### 6.7.3. Cuando la pendiente desaparece {#fispm-c06-cuando-la-pendiente-desaparece}

Si $f'(x_0)=0$, la linealización conserva el valor base y predice un cambio nulo. Puede aproximar bien el valor total mientras describe mal el primer cambio no nulo. Para $f(x)=1+x^2$ alrededor de cero, el valor aproximado es $1$ y el error absoluto es $x^2$. El incremento exacto respecto al estado base es $x^2$, mientras que el incremento linealizado es cero: su error relativo es $1$ para todo $x\ne0$.

El ejemplo no contradice proposición 6.6. El defecto $x^2$ dividido por $x$ tiende a cero, como corresponde a primer orden. Lo que falla es exigir que una aproximación de primer orden conserve un efecto cuyo primer término aparece a segundo orden. Ésta es la versión local de la advertencia sobre cancelaciones de §4.

[]{#ejercicios-6}

### 6.7.4. Ejercicios {#fispm-c06-ejercicios-6}

[]{#fispm-t1-c06-e0014}

**Ejercicio 6.14.** Para $f(h)=\sqrt{L^2+h^2}$, con $L>0$, obtén la aproximación afín alrededor de $h=0$ y alrededor de $h=L$. Usa una variable distinta para el incremento del segundo caso y comprueba las dimensiones.

**Solución.** La derivada es $f'(h)=h/\sqrt{L^2+h^2}$. En cero se obtiene $f(0)=L$ y $f'(0)=0$, por lo que $L_0(h)=L$. En el segundo caso conviene escribir $h=L+k$, para distinguir la altura total de su incremento. Entonces $f(L)=\sqrt2 L$ y $f'(L)=1/\sqrt2$, y la aproximación es $\sqrt2 L+k/\sqrt2$. Los dos términos tienen dimensiones de longitud; la pendiente es adimensional porque se deriva una longitud respecto a otra longitud. Las aproximaciones pertenecen a estados base diferentes. Sus intervalos de validez requieren el control del resto de §8.

[]{#fispm-t1-c06-e0015}

**Ejercicio 6.15.** Linealiza $f(x)=x^2$ alrededor de cero. Calcula el error absoluto, el cociente del defecto por el incremento de entrada y el error relativo del cambio de salida para $x\ne0$. Un informe afirma que «la linealización es inútil porque su error relativo es siempre uno». Evalúa esa conclusión según la observable y el criterio.

**Solución.** La parte afín es cero. El defecto absoluto es $x^2$, que tiende a cero; dividido por el incremento de entrada $x$ da $x\to0$, de acuerdo con la proposición 6.6. El cambio de salida respecto a $f(0)=0$ vale $x^2$, así que su error relativo es $x^2/x^2=1$. Si la pregunta exige resolver ese cambio con pequeña tolerancia relativa, la aproximación no sirve. Si exige un error absoluto no mayor que $\tau$ sobre una escala numérica fija, sí sirve en $|x|\le\sqrt\tau$. La conclusión del informe es demasiado amplia: juzga todos los usos mediante un único criterio.

Referencia: Riley--Hobson--Bence, *Mathematical Methods for Physics and Engineering*, 3.ª ed. (2006), §4.6, pp. 136--140.

[]{#resto-de-taylor-y-dominio-local-de-la-linealización}

[]{#fispm-t1-c06-s08}

[]{#fpm-i-06-s08}

## 6.8. Resto de Taylor y dominio local de la linealización {#fispm-c06-resto-de-taylor-y-dominio-local-de-la-linealizaciuxf3n}

La derivada seleccionó una aproximación de primer orden, pero una aplicación necesita saber cuánto puede alejarse del punto base. Decir que el defecto dividido por el incremento tiende a cero no determina, por sí solo, qué intervalo garantiza una tolerancia concreta. Para obtener ese intervalo hace falta controlar cómo varía la pendiente.

[]{#fig:I-06-R02}

<figure id="fig-fpm-v04-i-06-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-06-R02.svg" class="lightbox" data-gallery="fpm-v04-c06"><img src="/assets/books/fispm/v04/I-06-R02.svg" alt="Una cota necesita su dominio. Diagrama del capítulo 6; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="383" height="250" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 6.4.** En $|x|\le1$, el resto de $e^x\approx1+x$ satisface $|e^x-1-x|\le(e/2)x^2$. La cota discontinua usa el máximo de la segunda derivada en ese intervalo. Véase §[6.8](#fispm-c06-resto-de-taylor-y-dominio-local-de-la-linealizaciuxf3n).

</figcaption>

</figure>

Si la segunda derivada es grande, la pendiente cambia rápidamente y el intervalo certificado puede ser pequeño. Si la segunda derivada está acotada, la pérdida acumulada al reemplazar las pendientes cercanas por la pendiente base puede estimarse integrando una cota. La interpretación geométrica es la separación entre la gráfica y su recta tangente.

[]{#separar-aproximación-y-resto}

### 6.8.1. Separar aproximación y resto {#fispm-c06-separar-aproximaciuxf3n-y-resto}

[]{#fispm-t1-c06-d0010}

**Definición 6.10 --- Resto afín y radio controlado.** Para la aproximación de la definición 6.9, definimos $$R_{x_0}(h)=f(x_0+h)-f(x_0)-f'(x_0)h.$$ Así, $f(x_0+h)=L_{x_0}(h)+R_{x_0}(h)$ es una igualdad exacta. Un radio controlado para una tolerancia y una escala declaradas es un número $\rho>0$ tal que la cota requerida del resto vale para todos los incrementos $|h|\le\rho$ y el intervalo correspondiente está contenido en el dominio de $f$.

Definir el resto no lo hace pequeño. La definición identifica el defecto que hay que estimar y mantiene separada la igualdad exacta de la sustitución aproximada $f(x_0+h)\approx L_{x_0}(h)$.

[]{#fispm-t1-c06-p0007}

**Proposición 6.7 --- Cota cuadrática del resto.** Supongamos que $f$ es dos veces continuamente diferenciable en un intervalo abierto que contiene $[x_0-r,x_0+r]$, con $r>0$, y que $|f''(x)|\le M$, con $M\ge0$, en ese segmento. Entonces, para $|h|\le r$, $$|R_{x_0}(h)|\le\frac M2 h^2.$$

**Demostración.** El teorema fundamental del cálculo da $R_{x_0}(h)=\int_0^h[f'(x_0+t)-f'(x_0)]\,dt$. Aplicar el valor medio a $f'$ entre $x_0$ y $x_0+t$ proporciona $|f'(x_0+t)-f'(x_0)|\le M|t|$. Si $h\ge0$, integrar esa cota da $|R_{x_0}(h)|\le\int_0^h Mt\,dt=Mh^2/2$. Si $h<0$, invertir los límites de integración y tomar módulos da $\int_h^0 M|t|\,dt=Mh^2/2$. Ambos segmentos están dentro del intervalo donde vale la cota de $f''$. $\square$

Si se desea un error referido a una escala $S>0$ no mayor que $\tau>0$, proposición 6.7 permite imponer $Mh^2/2\le\tau S$. Para $M>0$ basta elegir $$|h|\le\rho, \qquad \rho=\min\left\{r,\sqrt{\frac{2\tau S}{M}}\right\}.$$ La escala tiene el tipo de $f$ y $M$ tiene el tipo de $f$ dividido por el cuadrado del tipo de $x$; el radio conserva el tipo de $x$. Si $M=0$, el resto es cero en todo el segmento y el radio $r$ queda disponible sin dividir por $M$.

[]{#controlar-el-cambio-observado}

### 6.8.2. Controlar el cambio observado {#fispm-c06-controlar-el-cambio-observado}

Para juzgar el cambio $\Delta f=f(x_0+h)-f(x_0)$, el denominador relativo puede ser muy distinto del valor total $f(x_0+h)$. El siguiente resultado proporciona un criterio cuando la pendiente base no se anula.

[]{#fispm-t1-c06-p0008}

**Proposición 6.8 --- Error relativo del incremento.** Bajo las hipótesis de la proposición 6.7, supongamos $a=f'(x_0)\ne0$ y $0<|h|\le r$. Si $\theta=M|h|/(2|a|)<1$, entonces $\Delta f\ne0$ y $$\frac{|\Delta f-ah|}{|\Delta f|} \le\frac{\theta}{1-\theta}.$$

**Demostración.** La identidad $\Delta f=ah+R_{x_0}(h)$ y proposición 6.7 dan $|R_{x_0}(h)|\le\theta|a||h|$. La desigualdad triangular inversa produce $|\Delta f|\ge|a||h|-|R_{x_0}(h)|\ge(1-\theta)|a||h|>0$. Dividir la cota del resto por esta cota inferior concluye el argumento. $\square$

La condición $a\ne0$ permite comparar el resto con el cambio de primer orden. Si $a=0$, esa comparación no existe; los ejemplos de §7 muestran que el error relativo del cambio puede permanecer unitario. Además, $\theta<1$ garantiza que el cambio exacto no se anule en los incrementos considerados.

[]{#fispm-t1-c06-mp0008}

**Principio 6.8 --- Convertir el resto en condiciones de uso.** La cota debe acompañarse de un dominio donde sus constantes estén justificadas y de una desigualdad que traduzca la tolerancia en un radio. Se distingue el error relativo del valor del error relativo del incremento.

[]{#ejercicios-7}

### 6.8.3. Ejercicios {#fispm-c06-ejercicios-7}

[]{#fispm-t1-c06-e0016}

**Ejercicio 6.16.** Para $f(x)=\sqrt{1+x}$, linealiza alrededor de cero y controla el resto en $|x|\le r<1$. Fija después $r=1/2$ y obtén un radio suficiente para error absoluto no mayor que $\tau>0$. Calcula el radio certificado para $\tau=0.001$.

**Solución.** La aproximación es $1+x/2$. Como $f''(x)=-1/[4(1+x)^{3/2}]$, en $|x|\le r$ se puede tomar $M=1/[4(1-r)^{3/2}]$. Proposición 6.7 da $$\left|\sqrt{1+x}-1-\frac x2\right| \le\frac{x^2}{8(1-r)^{3/2}}.$$ Para $r=1/2$, la constante es $\sqrt2/4$. Basta entonces $|x|\le\min\{1/2,\sqrt{2\sqrt2\,\tau}\}$. Para $\tau=0.001$, ese radio es aproximadamente $0.05318$. La estimación es suficiente, no se ha demostrado que sea el radio máximo posible. Mantener el radio auxiliar $1/2$ asegura que la constante utilizada no dependa del incremento concreto.

[]{#fispm-t1-c06-e0017}

**Ejercicio 6.17.** Para $f(x)=1+x+x^2$ alrededor de cero, calcula los errores relativos de la aproximación afín respecto al valor exacto y respecto al incremento exacto, en $0<|x|\le1/2$. Obtén cotas simples y explica sus diferentes ritmos de disminución.

**Solución.** La aproximación es $1+x$ y el resto es $x^2$. El valor exacto es positivo porque $1+x+x^2=(x+1/2)^2+3/4$. Por tanto, su error relativo es $x^2/(1+x+x^2)\le4x^2/3$. El incremento exacto es $x+x^2=x(1+x)$; para el dominio indicado no se anula y su error relativo es $|x|/|1+x|\le2|x|$. El mismo resto queda dividido por una cantidad de tamaño cercano a uno en el primer caso y por una de tamaño proporcional a $|x|$ en el segundo. No son dos errores absolutos distintos: son dos criterios para un defecto común. Proposición 6.8, con $a=1$ y $M=2$, da también la cota $|x|/(1-|x|)$.

[]{#fispm-t1-c06-e0018}

**Ejercicio 6.18.** Sea $f(x)=|x|^{3/2}$. Demuestra que es diferenciable en cero, identifica su aproximación afín y prueba que no existen $C>0$ y $r>0$ tales que su resto satisfaga $|R_0(x)|\le Cx^2$ para todo $|x|\le r$. Indica qué hipótesis de la proposición 6.7 no puede darse por disponible.

**Solución.** El cociente incremental en cero es $|x|^{3/2}/x$, cuyo módulo es $\sqrt{|x|}$ y tiende a cero. Así, $f'(0)=0$ y la aproximación afín es cero. El resto es $|x|^{3/2}$. Si hubiera una cota cuadrática, dividir por $x^2>0$ para $x\ne0$ daría $1/\sqrt{|x|}\le C$ cerca de cero, imposible porque ese cociente crece sin cota. Fuera de cero, la segunda derivada es $3/(4\sqrt{|x|})$ y no está acotada al acercarse a cero; la segunda derivada en cero tampoco existe. La diferenciabilidad alcanza para proposición 6.6, pero no aporta las hipótesis de la proposición 6.7.

En la geometría de §1 puede aplicarse ejercicio 6.16 a $x=(h/L)^2$. Esa sustitución produce la corrección $L+h^2/(2L)$ a la distancia. Es una aproximación afín en la variable $x$ y una corrección cuadrática en $h$; no debe confundirse con la linealización de la distancia respecto a $h$ en cero, que es constante.

Referencia: Riley--Hobson--Bence, 3.ª ed. (2006), §4.6, pp. 136--140.

[]{#parámetro-pequeño-y-primera-jerarquía-de-aproximaciones}

[]{#fispm-t1-c06-s09}

[]{#fpm-i-06-s09}

## 6.9. Parámetro pequeño y primera jerarquía de aproximaciones {#fispm-c06-paruxe1metro-pequeuxf1o-y-primera-jerarquuxeda-de-aproximaciones}

La cota del resto permite decidir si una aproximación basta para una tolerancia. Cuando varias aproximaciones se ordenan por potencias de un parámetro, interesa conservar también la dependencia de sus defectos con ese parámetro. Un número aislado, como $0.001$, no muestra qué ocurrirá al reducir a la mitad el incremento normalizado.

Para una familia de restos $R(\varepsilon,x)$, una estimación $|R(\varepsilon,x)|\le C\varepsilon^2$ contiene dos datos distintos: el exponente describe cómo disminuye la cota y la constante permite convertirla en un umbral. Si $x$ recorre un dominio, hay que saber además si la misma constante sirve en todos sus puntos. Se introduce una abreviatura para esta afirmación, con las condiciones dentro de su definición.

[]{#una-notación-para-cotas-uniformes}

### 6.9.1. Una notación para cotas uniformes {#fispm-c06-una-notaciuxf3n-para-cotas-uniformes}

[]{#fispm-t1-c06-d0011}

**Definición 6.11 --- Notación de orden uniforme elemental.** Sea $R(\varepsilon,x)$ adimensional, definido para $0<\varepsilon\le\varepsilon_0$ y $x\in X_\varepsilon$, y sea $k\in\mathbb R$. Escribiremos $$R(\varepsilon,x)=O(\varepsilon^k) \qquad (\varepsilon\to0^+,\ x\in X_\varepsilon)$$ si existen $C\ge0$ y $0<\varepsilon_1\le\varepsilon_0$ tales que $$|R(\varepsilon,x)|\le C\varepsilon^k \quad\text{para todo }0<\varepsilon\le\varepsilon_1 \text{ y todo }x\in X_\varepsilon.$$ La constante $C$ es independiente de $\varepsilon$ y de $x$; puede depender de otros datos declarados fijos. Si el resto tiene dimensiones, se normaliza mediante una escala positiva explícita antes de aplicar esta notación.

El signo igual en $R=O(\varepsilon^k)$ es una convención de notación para una propiedad de cota; no identifica $R$ con una función única llamada $O(\varepsilon^k)$. Tampoco proporciona el valor de $C$. Para una aplicación cuantitativa hay que recuperar una constante válida y el intervalo donde vale.

Por ejemplo, $R=\varepsilon^2\sin x$ cumple la definición con $C=1$ para todo $x\in\mathbb R$. En cambio, $R=\varepsilon^2x$ admite $C=2$ en $[0,2]$, pero esa misma afirmación de orden no vale en $[0,1/\varepsilon]$. La diferencia procede del dominio, no de una alteración formal de la expresión.

[]{#fispm-t1-c06-p0009}

**Proposición 6.9 --- Operaciones con cotas de orden.** Sobre dominios y datos fijos compatibles, si $R=O(\varepsilon^\alpha)$ y $S=O(\varepsilon^\beta)$, entonces $RS=O(\varepsilon^{\alpha+\beta})$. Si ambos tienen orden $O(\varepsilon^\alpha)$, entonces $R+S=O(\varepsilon^\alpha)$.

**Demostración.** Restrinjamos el parámetro al menor de los dos intervalos certificados. Las cotas $|R|\le C_R\varepsilon^\alpha$ y $|S|\le C_S\varepsilon^\beta$ dan $|RS|\le C_RC_S\varepsilon^{\alpha+\beta}$. Si los exponentes coinciden, la triangular da $|R+S|\le(C_R+C_S)\varepsilon^\alpha$. Las constantes conservan su independencia de las variables controladas. $\square$

Dividir requiere una condición adicional sobre el denominador; proposición 6.9 no autoriza a invertir una cantidad que podría anularse. También se conserva el dominio común: combinar dos estimaciones no amplía automáticamente sus regiones de validez.

[]{#orden-cero-y-primeras-correcciones}

### 6.9.2. Orden cero y primeras correcciones {#fispm-c06-orden-cero-y-primeras-correcciones}

[]{#fispm-t1-c06-d0012}

**Definición 6.12 --- Jerarquía finita en parámetro pequeño.** Para una familia adimensional $f(\varepsilon,x)$, una aproximación hasta orden entero $N\ge0$ es una expresión $$P_N(\varepsilon,x)=\sum_{j=0}^N c_j(x)\varepsilon^j$$ acompañada de una cota del resto $f-P_N=O(\varepsilon^{N+1})$ en el dominio declarado. El término $c_0$ es el orden cero y $c_1\varepsilon$ la primera corrección. Cuando se afirma que las potencias forman una jerarquía uniforme de tamaños, se comprueba además que los coeficientes relevantes permanezcan acotados en ese dominio.

Esta definición es finita. No afirma la existencia de una serie infinita, su convergencia ni que añadir indefinidamente términos mejore cualquier aproximación. Si un coeficiente se anula, el primer cambio efectivo puede aparecer más tarde; en la distancia de §8 apareció una corrección cuadrática en la altura.

[]{#fispm-t1-c06-p0010}

**Proposición 6.10 --- Jerarquía finita de una inversa.** Para todo entero $N\ge0$ y $\varepsilon\ne-1$, $$\frac1{1+\varepsilon} =\sum_{j=0}^N(-\varepsilon)^j +\frac{(-\varepsilon)^{N+1}}{1+\varepsilon}.$$ En $0\le\varepsilon\le1/2$, el resto tiene módulo no mayor que $\varepsilon^{N+1}$.

**Demostración.** Multiplicar la suma finita por $1+\varepsilon$ cancela sus términos interiores y deja $1-(-\varepsilon)^{N+1}$. Añadir el numerador del resto produce $1$, y dividir por el denominador no nulo demuestra la identidad. En el intervalo indicado, $1+\varepsilon\ge1$, por lo que el módulo del resto es $\varepsilon^{N+1}/(1+\varepsilon)\le\varepsilon^{N+1}$. $\square$

El orden cero es $1$, la primera corrección es $-\varepsilon$ y la siguiente es $\varepsilon^2$. Cada truncación tiene una cota propia. En este ejemplo la identidad puede verificarse sin usar una serie infinita.

[]{#fispm-t1-c06-mp0009}

**Principio 6.9 --- Elegir el orden por su resto.** Una truncación se justifica mediante el defecto que deja y la precisión requerida en su dominio. El nombre del orden no reemplaza la estimación de su constante ni la revisión de los coeficientes.

[]{#ejercicios-8}

### 6.9.3. Ejercicios {#fispm-c06-ejercicios-8}

[]{#fispm-t1-c06-e0019}

**Ejercicio 6.19.** Demuestra que $R(\varepsilon,x)=\varepsilon^2x$ es $O(\varepsilon^2)$ uniformemente en $[0,2]$. Demuestra que esa afirmación falla en $[0,1/\varepsilon]$, $0<\varepsilon\le1$, y determina una cota de orden que sí vale en este último dominio.

**Solución.** En el primer dominio, $|R|\le2\varepsilon^2$; sirven $C=2$ y cualquier umbral positivo dentro del intervalo permitido. Si en el segundo hubiera una constante para la cota cuadrática, evaluar en $x=1/\varepsilon$ exigiría $\varepsilon\le C\varepsilon^2$, es decir, $1/\varepsilon\le C$ para todos los parámetros suficientemente pequeños. Ninguna constante finita cumple esa condición. Allí sí se tiene $|R|\le\varepsilon$, por lo que el resto es $O(\varepsilon)$ uniformemente. El orden cambia cuando se exige una garantía sobre un dominio distinto.

[]{#fispm-t1-c06-e0020}

**Ejercicio 6.20.** Para $0\le\varepsilon\le1/2$, elige un orden suficiente de la suma de la proposición 6.10 para aproximar $1/(1+\varepsilon)$ con error absoluto no mayor que $0.001$. Indica cuántos términos conservarás y qué parte de la respuesta es una garantía uniforme.

**Solución.** proposición 6.10 proporciona $|R_N|\le(1/2)^{N+1}$. Para $N=8$ esa cota es $1/512>0.001$; para $N=9$ es $1/1024<0.001$. Por tanto, basta conservar los diez términos desde $j=0$ hasta $j=9$. La garantía vale simultáneamente para todo el intervalo, no sólo para el extremo. Se ha seleccionado un orden suficiente mediante una cota; no es necesario resolver un problema general de truncación óptima para justificarlo.

Referencia: Hinch, *Perturbation Methods* (1991), cap. 2, §§2.1--2.2, pp. 19--26.

[]{#límite-regular-y-señal-elemental-de-singularidad}

[]{#fispm-t1-c06-s10}

[]{#fpm-i-06-s10}

## 6.10. Límite regular y señal elemental de singularidad {#fispm-c06-luxedmite-regular-y-seuxf1al-elemental-de-singularidad}

Poner un parámetro igual a cero puede simplificar una relación y conservar una respuesta relevante. También puede borrar una rama de soluciones o perder el control sobre una región del dominio. Ambas posibilidades pueden detectarse mediante álgebra y límites de una variable, sin desarrollar una teoría de perturbaciones singulares.

[]{#fig:I-06-R01}

<figure id="fig-fpm-v04-i-06-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-06-R01.svg" class="lightbox" data-gallery="fpm-v04-c06"><img src="/assets/books/fispm/v04/I-06-R01.svg" alt="Un límite puede fallar cerca de una frontera. Diagrama del capítulo 6; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="246" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 6.5.** La familia $y_\varepsilon=e^{-x/\varepsilon}$ converge a cero para cada $x>0$ y conserva $y_\varepsilon(0)=1$. La gráfica usa $\varepsilon=0{,}1$: la aproximación exterior $y=0$ no es uniforme en $[0,1]$. Véase §[6.10](#fispm-c06-luxedmite-regular-y-seuxf1al-elemental-de-singularidad).

</figcaption>

</figure>

El diagnóstico debe relacionarse con la pregunta. Conservar una rama positiva cerca de un valor finito no exige preservar todas las raíces reales de la ecuación. Una aproximación uniforme en un intervalo alejado de cero tampoco necesita ser uniforme en un intervalo que lo incluye. Declarar la rama y el dominio evita convertir un éxito local en una conclusión sobre todo el modelo.

[]{#compatibilidad-respecto-a-la-información-requerida}

### 6.10.1. Compatibilidad respecto a la información requerida {#fispm-c06-compatibilidad-respecto-a-la-informaciuxf3n-requerida}

[]{#fispm-t1-c06-d0013}

**Definición 6.13 --- Diagnóstico de compatibilidad del límite.** Para una familia con parámetro $\varepsilon>0$, una rama seleccionada y un dominio declarado, llamaremos compatible al reemplazo por $\varepsilon=0$ respecto a una pregunta si conserva las respuestas requeridas y admite el control de aproximación exigido en ese dominio. Una pérdida de ramas relevantes, un cambio de dominio o el fallo de una garantía uniforme es una señal de incompatibilidad que obliga a revisar la reducción. Es un criterio de trabajo para los ejemplos elementales del capítulo, no una definición general de perturbación regular o singular.

La cláusula «respecto a una pregunta» es necesaria. Una ecuación reducida puede responder bien una pregunta concreta y perder otra información. El diagnóstico debe decir cuál de ellas interesa.

[]{#una-ecuación-que-pierde-una-raíz}

### 6.10.2. Una ecuación que pierde una raíz {#fispm-c06-una-ecuaciuxf3n-que-pierde-una-rauxedz}

Consideremos $$\varepsilon y^2+y-1=0,\qquad \varepsilon>0,$$ sin restringir inicialmente $y$ a valores positivos. Sus raíces son $$y_+(\varepsilon)=\frac{-1+\sqrt{1+4\varepsilon}}{2\varepsilon}, \qquad y_-(\varepsilon)=\frac{-1-\sqrt{1+4\varepsilon}}{2\varepsilon}.$$ La primera expresión tiene numerador y denominador tendiendo a cero. Racionalizarla da $y_+=2/(1+\sqrt{1+4\varepsilon})$, y entonces $y_+\to1$. La segunda satisface $\varepsilon y_-=-(1+\sqrt{1+4\varepsilon})/2\to-1$, por lo que diverge hacia $-\infty$.

Al poner $\varepsilon=0$, la ecuación se convierte en $y-1=0$ y conserva la raíz finita $1$. Si la pregunta seleccionaba la rama positiva, la reducción conserva su límite. Si pedía representar ambas ramas reales, la reducción pierde una de ellas. El coeficiente pequeño acompañaba un término que crece sobre esa segunda rama: $\varepsilon y^2$ no puede omitirse allí sólo porque $\varepsilon$ tienda a cero.

[]{#una-función-cuyo-límite-no-controla-todo-el-intervalo}

### 6.10.3. Una función cuyo límite no controla todo el intervalo {#fispm-c06-una-funciuxf3n-cuyo-luxedmite-no-controla-todo-el-intervalo}

Para $\varepsilon>0$ y $x\in[0,1]$, sea $f_\varepsilon(x)=x/(x+\varepsilon)$. Su límite en cada punto fijo es $$g(x)= \begin{cases} 0,&x=0,\\ 1,&0<x\le1. \end{cases}$$ Aunque ese límite existe punto por punto, el defecto respecto a $g$ no disminuye uniformemente. Para $x>0$ su módulo es $\varepsilon/(x+\varepsilon)$, que puede acercarse tanto como se quiera a $1$ escogiendo $x$ positivo suficientemente próximo a cero. En $x=0$ el defecto es cero. El supremo de los defectos en $[0,1]$ es $1$, aunque no se alcance.

Si se restringe a $[\delta,1]$ con $0<\delta\le1$ fijo, se obtiene en cambio $|f_\varepsilon-g|\le\varepsilon/(\delta+\varepsilon)\to0$. El límite puntual era correcto; la extrapolación de su control a todo el intervalo era la inferencia inválida.

[]{#fispm-t1-c06-mp0010}

**Principio 6.10 --- Revisar estructura y dominio antes de sustituir por cero.** Se comprueba qué ramas se siguen, qué variables pueden variar junto con el parámetro y qué regiones quedan cubiertas por la estimación. Si el reemplazo borra información requerida, se conserva la relación completa o se reformula una reducción con hipótesis nuevas explícitas.

No desarrollaremos métodos para reparar todos los límites incompatibles. La competencia que se busca aquí es diagnosticar cuándo el reemplazo necesita una revisión y evitar presentar la ecuación más corta como descripción universal.

[]{#ejercicios-9}

### 6.10.4. Ejercicios {#fispm-c06-ejercicios-9}

[]{#fispm-t1-c06-e0021}

**Ejercicio 6.21.** Sigue ambas raíces reales de $\varepsilon y^2+y-1=0$ cuando $\varepsilon\to0^+$. Demuestra que la raíz positiva se aproxima a $1$ con error absoluto no mayor que $\varepsilon$. Explica en qué pregunta es útil la ecuación reducida y en cuál pierde información.

**Solución.** Las fórmulas y la racionalización anteriores dan $y_+\to1$ y $y_-\to-\infty$. Además, la raíz positiva satisface $0<y_+<1$, por su expresión racionalizada. La ecuación exacta da $1-y_+=\varepsilon y_+^2\le\varepsilon$. Así, el límite de la rama positiva tiene una cota cuantitativa. La ecuación reducida $y=1$ sirve para esa rama bajo el criterio absoluto indicado; no describe las dos raíces reales ni el crecimiento de la negativa. La distinción pertenece al contenido de la pregunta, no a la validez de la fórmula cuadrática.

[]{#fispm-t1-c06-e0022}

**Ejercicio 6.22.** Para $f_\varepsilon(x)=x/(x+\varepsilon)$ en $[0,1]$, determina el límite puntual y demuestra que el supremo del defecto respecto a ese límite es $1$ para cada $\varepsilon>0$. Obtén después un umbral suficiente para defecto no mayor que $0<\tau<1$ en $[\delta,1]$, con $0<\delta\le1$ fijo.

**Solución.** En cero, todos los valores son cero; en cada punto positivo, dividir numerador y denominador por $x$ muestra el límite $1$. Para $x>0$, el defecto es $\varepsilon/(x+\varepsilon)<1$, y al tomar $x\to0^+$ se acerca a $1$; por tanto su supremo es $1$. No es un máximo, porque en cero el defecto vale cero. En el intervalo alejado de cero, la cota es $\varepsilon/(\delta+\varepsilon)$. Exigirla menor o igual que $\tau$ equivale a $\varepsilon\le\tau\delta/(1-\tau)$. Esa condición certifica el intervalo completo. Si $\delta$ varía con $\varepsilon$, debe revisarse la razón y no tratarlo como dato fijo.

Referencia: Hinch, *Perturbation Methods* (1991), cap. 1, §1.2, pp. 4--7.

[]{#coherencia-a-posteriori-de-los-términos-despreciados}

[]{#fispm-t1-c06-s11}

[]{#fpm-i-06-s11}

## 6.11. Coherencia a posteriori de los términos despreciados {#fispm-c06-coherencia-a-posteriori-de-los-tuxe9rminos-despreciados}

Una reducción puede estar bien resuelta y mal aplicada. En §5, omitir el término cuadrático de $y+\varepsilon y^2=a$ produjo $y=a$ sin error algebraico en la ecuación reducida. La cuestión pendiente era si esa respuesta hacía pequeña la contribución que se había eliminado. Al insertar el candidato, la condición se convirtió en $\eta=\varepsilon a$ pequeño.

[]{#fig:I-06-R04}

<figure id="fig-fpm-v04-i-06-r04" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-06-R04.svg" class="lightbox" data-gallery="fpm-v04-c06"><img src="/assets/books/fispm/v04/I-06-R04.svg" alt="Comprobar el tamaño después de resolver. Diagrama del capítulo 6; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="349" height="222" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 6.6.** Un residuo modelo $\varepsilon u^2$ debe compararse con una tolerancia declarada a lo largo de la solución. Aquí $\varepsilon=0{,}03$ y la línea discontinua vale $0{,}2$; el umbral se alcanza en $u=\sqrt{20/3}$. Véase §[6.11](#fispm-c06-coherencia-a-posteriori-de-los-tuxe9rminos-despreciados).

</figcaption>

</figure>

La comprobación es a posteriori porque utiliza la respuesta obtenida. No debe confundirse con elegir después una hipótesis que encubra el fallo: la comparación que se comprobará se declara antes de resolver. La respuesta puede confirmar la hipótesis, delimitarla o rechazarla.

[]{#una-obligación-que-acompaña-al-candidato}

### 6.11.1. Una obligación que acompaña al candidato {#fispm-c06-una-obligaciuxf3n-que-acompauxf1a-al-candidato}

[]{#fispm-t1-c06-d0014}

**Definición 6.14 --- Autoconsistencia de una reducción.** Una reducción es autoconsistente en un régimen si sus candidatos pertenecen al dominio del modelo y satisfacen, al sustituirlos, las condiciones de tamaño y las demás hipótesis utilizadas para construirla. Si se afirma además una precisión de la observable, se añade una estimación de error cuyas hipótesis también se verifican. Cumplir las condiciones de tamaño y demostrar una tolerancia son obligaciones relacionadas pero distintas.

Por ejemplo, insertar $y=a$ y encontrar $\varepsilon a\le0.01$ verifica una razón de omisión. Para afirmar un error relativo no mayor que $0.01$, hay que justificar que esa razón domina el error pertinente. En esta ecuación existe un argumento especialmente simple a partir de la relación exacta.

[]{#una-garantía-sin-conocer-la-fórmula-de-la-raíz}

### 6.11.2. Una garantía sin conocer la fórmula de la raíz {#fispm-c06-una-garantuxeda-sin-conocer-la-fuxf3rmula-de-la-rauxedz}

[]{#fispm-t1-c06-p0011}

**Proposición 6.11 --- Control del candidato lineal.** Para $a>0$ y $\varepsilon\ge0$, la relación $y+\varepsilon y^2=a$ tiene una única raíz positiva $y_\ast$, satisface $0<y_\ast\le a$, y el candidato $y_{\mathrm L}=a$ cumple $$\frac{a-y_\ast}{y_\ast} =\varepsilon y_\ast \le\varepsilon a.$$

**Demostración.** Si $\varepsilon=0$, la raíz es $a$ y la afirmación es inmediata. Si $\varepsilon>0$, la existencia y unicidad siguen de la continuidad y el crecimiento estricto de $F(y)=y+\varepsilon y^2-a$ en $[0,a]$, como en §5. La ecuación da $a-y_\ast=\varepsilon y_\ast^2\ge0$, lo que prueba $y_\ast\le a$. Dividir esa identidad por la raíz positiva produce el cociente del enunciado y después se usa $y_\ast\le a$. $\square$

La relación exacta convierte la razón $\eta$ calculada sobre el candidato en una garantía del error relativo respecto a la raíz verdadera. Para $\eta\le\tau$ queda certificado un error relativo no mayor que $\tau$. No se ha sustituido la raíz desconocida por el candidato dentro de una igualdad; se ha obtenido primero una cota sobre la raíz y se la ha usado en una desigualdad.

El residuo normalizado del candidato también vale $\eta$, pero esa coincidencia está justificada aquí por la proposición 6.11. En otra relación, el mismo valor de residuo puede tener consecuencias distintas sobre la observable, como mostró ejercicio 6.12.

[]{#fispm-t1-c06-mp0011}

**Principio 6.11 --- Comprobar todas las hipótesis utilizadas.** La validación revisa pertenencia al dominio, signos, denominadores y razones de omisión sobre el candidato. Las afirmaciones de precisión se respaldan con cotas que conecten el candidato con la solución del modelo completo. Una comprobación numérica favorable en un dato no demuestra validez en todo un régimen.

[]{#la-información-que-deja-un-rechazo}

### 6.11.3. La información que deja un rechazo {#fispm-c06-la-informaciuxf3n-que-deja-un-rechazo}

Si el balance cuadrático da $y_{\mathrm C}=\sqrt{a/\varepsilon}$, su hipótesis de omisión exige que $1/\sqrt{\varepsilon a}$ sea pequeño. Cuando ese cociente resulta grande, el candidato sigue resolviendo la ecuación reducida, pero no satisface la justificación que llevó a ella. El rechazo identifica qué término sigue siendo relevante y ayuda a seleccionar otro modelo.

La autoconsistencia no evalúa toda la adecuación física del modelo original. Una respuesta puede ser autoconsistente en $y+\varepsilon y^2=a$ y no representar la respuesta de un sistema real si la relación adoptada omite efectos importantes. Ese control pertenece a la comparación entre modelo y fenómeno.

[]{#ejercicios-10}

### 6.11.4. Ejercicios {#fispm-c06-ejercicios-10}

[]{#fispm-t1-c06-e0023}

**Ejercicio 6.23.** Para $y+0.01y^2=2$, certifica el candidato $y_{\mathrm L}=2$ con tolerancia relativa $2\%$ respecto a la raíz exacta. Indica qué magnitudes y condiciones utilizas y si has demostrado que el error sea exactamente $2\%$.

**Solución.** El modelo cumple las hipótesis de la proposición 6.11 con $\varepsilon=0.01$ y $a=2$. La raíz es positiva y menor que $2$. La razón de omisión sobre el candidato es $\eta=\varepsilon a=0.02$. Proposición 6.11 garantiza $(2-y_\ast)/y_\ast\le0.02$, por lo que el candidato cumple la tolerancia del $2\%$. No se afirma igualdad: el error exacto es $\varepsilon y_\ast$, estrictamente menor que $0.02$ porque $\varepsilon>0$ y $y_\ast<2$. La garantía no requirió calcular la raíz mediante radicales.

[]{#fispm-t1-c06-e0024}

**Ejercicio 6.24.** Para $y+0.01y^2=1$, se propone el candidato cuadrático $10$. Verifica su ecuación reducida, calcula la razón del término eliminado y decide si es autoconsistente. Usa una cota sobre la raíz exacta para demostrar que su error relativo supera $9$.

**Solución.** El candidato satisface $0.01(10)^2=1$. En la relación completa, el término lineal omitido vale $10$ y el cuadrático conservado vale $1$, por lo que su razón es $10$, incompatible con la pequeñez requerida. Proposición 6.11 da $0<y_\ast<1$. Como $10>y_\ast$, el error relativo es $(10-y_\ast)/y_\ast=10/y_\ast-1>9$. Resolver una ecuación reducida no valida haber despreciado el término que domina sobre su propia respuesta.

Referencias: Hinch, *Perturbation Methods* (1991), cap. 1, §§1.1--1.2, pp. 1--7, y [capítulo 3, §12](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md#fispm-c03-robustez-cotas-y-estimaciuxf3n-por-caminos-independientes).

[]{#regímenes-múltiples-cruces-y-ruptura-de-aproximaciones}

[]{#fispm-t1-c06-s12}

[]{#fpm-i-06-s12}

## 6.12. Regímenes múltiples, cruces y ruptura de aproximaciones {#fispm-c06-reguxedmenes-muxfaltiples-cruces-y-ruptura-de-aproximaciones}

Los dos candidatos de §5 responden a zonas distintas de la entrada normalizada. Para $\eta=\varepsilon a$ pequeño, $y=a$ conserva el término lineal y tiene el control relativo de la proposición 6.11. Para $\eta$ grande, el candidato $\sqrt{a/\varepsilon}$ conserva la contribución cuadrática. Entre esos regímenes puede haber una zona donde ninguno de los dos modelos cortos alcance la tolerancia pedida.

[]{#fig:I-06-N03}

<figure id="fig-fpm-v04-i-06-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-06-N03.svg" class="lightbox" data-gallery="fpm-v04-c06"><img src="/assets/books/fispm/v04/I-06-N03.svg" alt="Acumulación secular. Diagrama del capítulo 6; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="242" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 6.7.** Si el error normalizado crece como $\varepsilon u$, con $\varepsilon=0{,}05$, alcanza la tolerancia $0{,}2$ en $u=4$. Un parámetro pequeño no garantiza precisión para tiempos arbitrarios. Véase §[6.12](#fispm-c06-reguxedmenes-muxfaltiples-cruces-y-ruptura-de-aproximaciones).

</figcaption>

</figure>

El cruce no se fija por una cifra universal de $\varepsilon$. La razón que decide es $\eta$, y el criterio de precisión puede delimitar regiones más estrechas que la comparación cualitativa. Saber que dos términos son comparables no equivale a saber que una de las reducciones tenga un error de diez por ciento.

[]{#criterio-de-cruce-y-dominio-certificado}

### 6.12.1. Criterio de cruce y dominio certificado {#fispm-c06-criterio-de-cruce-y-dominio-certificado}

[]{#fispm-t1-c06-d0015}

**Definición 6.15 --- Cruce de regímenes y dominio de validez.** Un criterio de cruce identifica los datos para los que las contribuciones que compiten alcanzan tamaños comparables. El dominio certificado de una aproximación es el conjunto de datos donde una estimación demostrada garantiza la tolerancia elegida y se cumplen sus hipótesis. Salir de un dominio certificado indica que la garantía ya no está disponible; por sí solo no demuestra que la aproximación haya fallado efectivamente.

La última distinción importa cuando la cota es conservadora. Una aproximación puede seguir siendo útil fuera de la región suficiente obtenida por una prueba. Para ampliar esa región hace falta una estimación mejor o una comparación válida con la solución completa.

[]{#control-de-los-dos-modelos-reducidos}

### 6.12.2. Control de los dos modelos reducidos {#fispm-c06-control-de-los-dos-modelos-reducidos}

[]{#fispm-t1-c06-p0012}

**Proposición 6.12 --- Cotas de los candidatos lineal y cuadrático.** Sean $a,\varepsilon>0$ y $y_\ast$ la raíz positiva de $y+\varepsilon y^2=a$. Pongamos $\eta=\varepsilon a$, $y_{\mathrm L}=a$, $y_{\mathrm C}=\sqrt{a/\varepsilon}$, $\delta=1/\sqrt\eta$ y $z=y_\ast/y_{\mathrm C}$. Entonces $0<z<1$ y $$\frac{|y_{\mathrm L}-y_\ast|}{y_\ast}\le\eta, \qquad \frac{|y_{\mathrm C}-y_\ast|}{y_\ast} =\frac{\delta}{1+z}\le\delta.$$ Si además $\delta<1$, el error del candidato cuadrático admite también la cota suficiente $\delta/(1-\delta)$.

**Demostración.** La cota lineal es proposición 6.11. Dividir la ecuación exacta por $a$ e insertar $y_\ast=y_{\mathrm C}z$ da $z^2+\delta z=1$. Puesto que $z>0$ y $\delta>0$, se tiene $z^2<1$, luego $z<1$. Factorizar $1-z^2=\delta z$ da $(1-z)(1+z)=\delta z$, y por ello $$\frac{y_{\mathrm C}-y_\ast}{y_\ast} =\frac{1-z}{z} =\frac{\delta}{1+z} \le\delta.$$ La misma identidad implica $1-z=\delta z/(1+z)\le\delta$, de donde $z\ge1-\delta$. Si $\delta<1$, dividir la cota $1-z\le\delta$ por esta cota inferior positiva de $z$ da $(1-z)/z\le\delta/(1-\delta)$. $\square$

La primera cota cuadrática es más fuerte que la última. Se conserva la última porque muestra una estrategia general: obtener por separado una cota del defecto y una cota inferior del denominador. Es la misma arquitectura de la proposición 6.8. Sus dominios suficientes no son necesariamente óptimos.

Para una tolerancia relativa $\tau>0$, proposición 6.12 certifica el candidato lineal si $\eta\le\tau$ y el cuadrático si $\eta\ge1/\tau^2$. Si se utiliza la cota más conservadora, basta exigir $\eta\ge((1+\tau)/\tau)^2$. En ambos casos el umbral procede de una desigualdad demostrada.

[]{#la-zona-intermedia}

### 6.12.3. La zona intermedia {#fispm-c06-la-zona-intermedia}

Cuando $\eta=1$, la forma escalada $z=y_\ast/a$ satisface $z+z^2=1$, por lo que $z=(\sqrt5-1)/2$. Ambos candidatos coinciden con $a$, y su error relativo es $(1-z)/z=(\sqrt5-1)/2$, aproximadamente $0.618$. Una tolerancia del diez por ciento no se cumple. Aquí el diagnóstico de términos comparables se acompaña de un fallo efectivo de ambas reducciones.

Para otros datos, una región excluida por una cota suficiente puede contener puntos donde el error sí sea aceptable. Por eso un mapa de regímenes debe separar las regiones certificadas de las rechazadas mediante un cálculo efectivo, y dejar sin dictamen los datos para los que aún no tiene control.

[]{#fispm-t1-c06-mp0012}

**Principio 6.12 --- No inventar solapamientos.** Dos modelos reducidos pueden cubrir extremos distintos sin compartir un dominio certificado. Si dejan una región sin garantía, se conserva el modelo completo o se demuestra una aproximación adicional. El mapa de lectura de regímenes no debe rellenarse mediante una interpolación cuya precisión no se haya controlado.

[]{#ejercicios-11}

### 6.12.4. Ejercicios {#fispm-c06-ejercicios-11}

[]{#fispm-t1-c06-e0025}

**Ejercicio 6.25.** Para error relativo máximo $\tau>0$, demuestra que las condiciones $\eta\le\tau$ y $\eta\ge((1+\tau)/\tau)^2$ certifican respectivamente los candidatos lineal y cuadrático. En el segundo caso usa la cota conservadora de la proposición 6.12. Compara con el criterio suficiente que proporciona su cota más fuerte.

**Solución.** La primera condición se inserta directamente en la cota lineal. Para el candidato cuadrático, exigir $\delta/(1-\delta)\le\tau$ con $0<\delta<1$ equivale a $\delta\le\tau/(1+\tau)$, que implica $\delta<1$ y se traduce en $\eta\ge((1+\tau)/\tau)^2$. La cota más fuerte, error no mayor que $\delta$, sólo exige $\delta\le\tau$, o $\eta\ge1/\tau^2$. Así, dos pruebas correctas producen regiones suficientes diferentes. La mejora del umbral responde a información adicional de la identidad exacta, no a un cambio del modelo.

[]{#fispm-t1-c06-e0026}

**Ejercicio 6.26.** Para $\tau=0.1$, compara los dominios certificados por la receta conservadora del ejercicio 6.25. Determina si se solapan y qué puede concluirse de la región que queda fuera de ambos. Repite la comparación usando la cota más fuerte y da un dato donde ambos candidatos fallen efectivamente.

**Solución.** La receta conservadora da $\eta\le0.1$ para el candidato lineal y $\eta\ge121$ para el cuadrático. No hay solapamiento; $0.1<\eta<121$ queda fuera de esas garantías. La cota más fuerte amplía el dominio cuadrático a $\eta\ge100$, pero todavía deja un intervalo sin garantía entre $0.1$ y $100$. Ninguno de los intervalos excluidos constituye por sí solo una región completa de fallo. Para $\eta=1$, el cálculo desarrollado antes del ejercicio da error relativo aproximadamente $0.618$ para ambos candidatos, superior a $0.1$: ese punto sí está rechazado por comparación efectiva. La ausencia de garantía y el error demostrado se registran como conclusiones distintas.

Referencias internas: [capítulo 2, §9](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md#fispm-c02-escalas-caracteruxedsticas-y-uxf3rdenes-de-magnitud) y sus escalas normalizadas; controles propios proposiciones 6.11--6.12. No se introduce una teoría de empalme de aproximaciones.

[]{#jerarquías-de-modelos-y-descripción-efectiva}

[]{#fispm-t1-c06-s13}

[]{#fpm-i-06-s13}

## 6.13. Jerarquías de modelos y descripción efectiva {#fispm-c06-jerarquuxedas-de-modelos-y-descripciuxf3n-efectiva}

Una distancia puede describirse mediante $\sqrt{L^2+h^2}$, mediante $L+h^2/(2L)$ o mediante $L$. Las tres expresiones conservan información diferente sobre el mismo modelo geométrico. Para la distancia total y una tolerancia moderada puede bastar la última. Para estudiar el pequeño aumento causado por la altura, esa expresión elimina precisamente el efecto que interesa y conviene conservar la corrección cuadrática.

La palabra «completo» es relativa al modelo de partida. La fórmula de Pitágoras es exacta para los extremos en geometría euclídea; no describe por sí sola la forma de una cuerda curvada ni las deformaciones de un instrumento. Dentro de ese modelo podemos controlar las reducciones matemáticas. La relación entre el modelo y una situación real necesita además hipótesis y observación.

[]{#comparar-descripciones-mediante-una-observable-común}

### 6.13.1. Comparar descripciones mediante una observable común {#fispm-c06-comparar-descripciones-mediante-una-observable-comuxfan}

[]{#fispm-t1-c06-d0016}

**Definición 6.16 --- Jerarquía de modelos relativa a una pregunta.** Una jerarquía de modelos es una familia ordenada de descripciones que conservan distintos niveles de información sobre una observable común, con reglas explícitas para compararlas y dominios de validez declarados. El modelo de partida contiene la información considerada completa para esa construcción; un modelo reducido omite contribuciones bajo hipótesis; un modelo límite describe la información que se conserva al llevar un parámetro al valor límite elegido. El orden se juzga respecto a la pregunta y a la precisión requerida, no sólo por la longitud de las fórmulas.

Para comparar modelos con variables diferentes, primero se recupera la misma observable en las mismas unidades. El valor normalizado $y$ y la cantidad física $q=Sy$ no son dos predicciones que puedan restarse sin conversión. También debe existir un dominio común donde las dos descripciones y sus estimaciones estén definidas.

El modelo límite no equivale a una aproximación válida en todo el dominio. §10 mostró una raíz que desaparece y una garantía uniforme que se pierde. Si el límite conserva sólo una rama, esa elección forma parte de su descripción.

[]{#fispm-t1-c06-mp0013}

**Principio 6.13 --- Conservar la información requerida.** La selección de un modelo se hace por la observable, la escala y la precisión de la pregunta. Se registra qué contribución se elimina y qué preguntas dejan de poder responderse con esa eliminación.

En geometría, $d_0=L$ conserva la escala principal de la distancia, mientras que $d_1=L+h^2/(2L)$ conserva además su primer incremento no nulo alrededor de $h=0$. No hace falta introducir otra dimensión espacial como variable de diferenciación: $L$ se mantiene fijo y la expansión depende de una sola variable o de su parámetro normalizado.

[]{#presupuesto-de-error-entre-descripciones}

### 6.13.2. Presupuesto de error entre descripciones {#fispm-c06-presupuesto-de-error-entre-descripciones}

[]{#fispm-t1-c06-p0013}

**Proposición 6.13 --- Error acumulado entre modelos sobre una observable común.** Sean $q_{\mathrm A},q_{\mathrm B},q_{\mathrm C}$ predicciones escalares del mismo tipo en un dominio común y sea $S>0$ una escala declarada. Para $\alpha,\beta\ge0$, si $|q_{\mathrm A}-q_{\mathrm B}|\le\alpha S$ y $|q_{\mathrm B}-q_{\mathrm C}|\le\beta S$, entonces $|q_{\mathrm A}-q_{\mathrm C}|\le(\alpha+\beta)S$. La conclusión sólo compara esos tres objetos; alcanza al fenómeno físico únicamente si una de las cotas relaciona justificadamente el fenómeno con el modelo.

**Demostración.** Aplicar proposición 6.1 a las tres predicciones produce la desigualdad. La última afirmación precisa sus hipótesis: si los tres objetos son predicciones de modelos, el fenómeno no aparece en las premisas y ninguna cota sobre su diferencia puede deducirse de ellas. $\square$

Proposición 6.13 aplica un resultado conocido para hacer explícita una nueva obligación de modelización. Una reducción con error certificado de $0.01S$ puede aproximar bien al modelo de partida y aun así heredar una discrepancia mayor de ese modelo respecto a la realidad. Tampoco corresponde sumar automáticamente una incertidumbre estándar experimental a una cota determinista y dar al total una interpretación probabilística: capítulo 3 exige declarar cómo se caracteriza cada componente.

El presupuesto permite distribuir precisión cuando las contribuciones sí son cotas sobre una observable común. Si se admite una pérdida total de $0.05S$ y una parte consume $0.02S$, queda un margen de $0.03S$ para una reducción adicional. Se trata de una condición suficiente mediante la desigualdad triangular, no de una afirmación de que los defectos se sumen siempre con el mismo signo.

**Ejercicio.**

[]{#fispm-t1-c06-e0027}

**Ejercicio 6.27.** Una cantidad objetivo $q_{\mathrm{obj}}$, la predicción del modelo $q_{\mathrm M}$ y una reducción $q_{\mathrm R}$ comparten un dominio y una escala $S>0$. Se han justificado las cotas $|q_{\mathrm{obj}}-q_{\mathrm M}|\le0.02S$ y $|q_{\mathrm M}-q_{\mathrm R}|\le0.03S$. Determina la garantía total. Indica qué puede afirmarse si la primera cota no se conoce y si $0.02S$ representa únicamente una incertidumbre estándar de medición.

**Solución.** Con las dos cotas deterministas, proposición 6.13 da $|q_{\mathrm{obj}}-q_{\mathrm R}|\le0.05S$. Los modelos y el objetivo comparten dominio, escala y observable; sin esa correspondencia no sería legítimo sumar los defectos. Si falta la primera cota, sólo permanece la garantía de reducción $|q_{\mathrm M}-q_{\mathrm R}|\le0.03S$: no se obtiene una cota total respecto al objetivo. Si $0.02S$ es una incertidumbre estándar, no se ha dado la hipótesis determinista que requiere proposición 6.13. Habría que especificar el modelo de medición y la interpretación estadística apropiada antes de formular una afirmación probabilística; el número por sí solo no garantiza que toda discrepancia física sea menor que $0.02S$.

Referencias internas utilizadas: [capítulo 3, §14](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md#fispm-c03-quuxe9-puede-y-quuxe9-no-puede-decir-una-mediciuxf3n) y [capítulo 1, §11](fisica-para-matematicos-capitulo-1-teorias-fisicas-fenomenos-modelos-y-leyes.md#fispm-c01-dominio-de-validez-y-teoruxedas-efectivas). El presupuesto y la jerarquía son construcciones propias sobre los controles del capítulo.

[]{#protocolo-de-aproximación-controlada}

[]{#fispm-t1-c06-s14}

[]{#fpm-i-06-s14}

## 6.14. Protocolo de aproximación controlada {#fispm-c06-protocolo-de-aproximaciuxf3n-controlada}

Una aproximación queda defendida cuando otra persona puede recuperar la pregunta, comprobar la reducción y reconocer sus límites sin adivinar las condiciones omitidas. Una fórmula breve puede ser el resultado de ese trabajo, pero no lo sustituye. Los ejemplos del capítulo permiten reunir las obligaciones en una ficha que sirve tanto para construir una aproximación como para auditar una ya propuesta.

[]{#la-ficha-y-sus-obligaciones}

### 6.14.1. La ficha y sus obligaciones {#fispm-c06-la-ficha-y-sus-obligaciones}

[]{#fispm-t1-c06-d0017}

**Definición 6.17 --- Ficha de aproximación controlada.** Una ficha de aproximación registra el modelo de partida y su estatuto, la observable buscada, los dominios y datos, las escalas y variables normalizadas, el parámetro o las razones de control, la reducción propuesta, la medida de error y su cota, las comprobaciones de autoconsistencia y el dominio certificado resultante. Si alguna obligación no está resuelta, la ficha lo señala y restringe la conclusión a lo que sí se ha demostrado.

El registro no exige repetir toda una derivación cada vez que se usa una fórmula. Exige que las hipótesis y la evidencia sean recuperables. Para una reducción ya demostrada puede bastar citar su resultado y comprobar que los datos actuales pertenecen al régimen permitido.

El trabajo sigue una secuencia que también permite localizar dónde se produjo un fallo:

1.  **Identificar la pregunta.** Se distingue el valor total de un incremento, una raíz de todas las ramas y una observable física de una variable normalizada.

2.  **Fijar el modelo y el dominio.** Se declaran sus hipótesis y restricciones; se comprueba que las expresiones estén definidas.

3.  **Elegir escalas y parámetros.** Se usan las herramientas del capítulo 2 para expresar tamaños relativos y se registra qué queda fijo.

4.  **Proponer la reducción.** Se comparan términos completos o se identifica el punto base y la variable de una expansión univariada.

5.  **Obtener el candidato.** Se resuelve la relación reducida o se construye la expresión aproximada, conservando signos y dominios.

6.  **Controlar el defecto.** Se estima el error de la observable; si se usa residuo, se justifica la conexión mediante sensibilidad.

7.  **Validar el régimen.** Se insertan candidatos en las razones de omisión y se traduce la tolerancia en condiciones sobre los datos.

Cada paso hace una pregunta distinta. Comparar bien los términos no resuelve la ecuación; resolverla no demuestra la legitimidad de la omisión; una cota local no certifica un intervalo más amplio.

[]{#fispm-t1-c06-mp0014}

**Principio 6.14 --- Concluir con la evidencia disponible.** El informe final declara la aproximación, el criterio y el dominio donde está certificada. Diferencia una garantía suficiente, un error efectivo calculado y una región todavía sin dictamen. Si la aproximación no supera su validación, se conserva el modelo completo o se prueba otra reducción.

La cinemática en una dimensión del capítulo 7 podrá utilizar esta ficha para elegir un intervalo temporal, un estado de referencia y una precisión de posición. El método queda disponible antes de adoptar modelos particulares de movimiento: declarar una aproximación local de una curva no exige todavía masa, fuerzas ni leyes de Newton.

[]{#problemas-de-síntesis}

### 6.14.2. Problemas de síntesis {#fispm-c06-problemas-de-suxedntesis}

[]{#fispm-t1-c06-e0028}

**Ejercicio 6.28.** En el modelo geométrico $d=\sqrt{L^2+h^2}$, $L>0$, se requiere aproximar la distancia para todo $|h|\le L/5$ con error absoluto no mayor que $0.001L$. Compara los candidatos $d_0=L$ y $d_1=L+h^2/(2L)$. Construye una ficha de aproximación para uno que cumpla la tolerancia, justificando el resto sin presuponer una serie infinita.

**Solución.** La observable es la distancia total y el criterio es el error dividido por $L$. Con $u=h/L$ y $x=u^2$, el dominio es $|u|\le1/5$ y $0\le x\le1/25$. La cota de §1 para el candidato constante es $|d-d_0|/L\le u^2/2\le0.02$, que no certifica la tolerancia. Además, en $|u|=1/5$ el error efectivo es $\sqrt{1.04}-1$. Es mayor que $0.001$ porque $1.04>(1.001)^2$, de modo que ese candidato falla en el dominio pedido.

Para la corrección, racionalizar la diferencia da la identidad $$\sqrt{1+x}-1-\frac x2 =-\frac{x^2}{2(\sqrt{1+x}+1)^2}.$$ En $x\ge0$ el denominador es al menos $8$, así que $|d-d_1|/L\le u^4/8$. En el dominio pedido, la cota es $(1/5)^4/8=0.0002<0.001$. La ficha registra el modelo euclídeo, $L$ fijo, observable distancia, escala $L$, parámetro $u$, dominio $|u|\le1/5$, candidato $d_1$ y la cota uniforme $0.0002L$. El candidato constante elimina el incremento cuadrático; la corrección lo conserva. La conclusión certifica una reducción del modelo geométrico y no una longitud de cuerda deformada.

[]{#fispm-t1-c06-e0029}

**Ejercicio 6.29.** Una relación de modelo es $q+q^2/Q=b$, con $Q,b>0$ y $q\ge0$. Para $b/Q=10^{-3}$ y para $b/Q=10^3$, construye en cada caso una aproximación sencilla y certifícala con error relativo no mayor que $5\%$ respecto a la raíz positiva. Presenta el parámetro que controla cada decisión y recupera las unidades de la respuesta.

**Solución.** Escalar con $b$ da $z=q/b$ y $\eta=b/Q$, de modo que $z+\eta z^2=1$. Para $\eta=10^{-3}$, se propone omitir el término cuadrático y utilizar $z_{\mathrm L}=1$, es decir, $q_{\mathrm L}=b$. La razón de omisión sobre el candidato es $\eta=0.001$. Proposición 6.11, aplicada con entrada normalizada $a=1$ y coeficiente $\varepsilon=\eta$, garantiza error relativo no mayor que $0.001$, inferior a $0.05$.

Para $\eta=10^3$, se conserva el balance cuadrático, con $z_{\mathrm C}=1/\sqrt\eta$ y $q_{\mathrm C}=b/\sqrt{b/Q}=\sqrt{bQ}$. La razón del término lineal omitido al cuadrático conservado es $1/\sqrt\eta\approx0.03162$. Proposición 6.12 convierte esa razón en una cota de error relativo no mayor que $1/\sqrt{1000}<0.03163<0.05$. La cifra $0.03163$ se redondea hacia arriba para conservar la cota. La raíz positiva existe y es única por el argumento de §5. Tanto $b$ como $\sqrt{bQ}$ tienen el tipo de $q$. Las dos fichas corresponden a regímenes diferentes de la misma relación; la condición no se decide por el valor aislado de una magnitud con unidades.

[]{#fispm-t1-c06-e0030}

**Ejercicio 6.30.** Audita el siguiente informe, cuyas cuatro afirmaciones son deliberadamente defectuosas:

- «Como $\varepsilon=10^{-4}$, la corrección $\varepsilon x$ es menor que $0.01$ en todo $0\le x\le1/\varepsilon$».

- «El candidato $y=1$ para $F(y)=10^{-9}y=0$ tiene residuo $10^{-9}$; por ello su error respecto a una raíz es menor que $10^{-6}$».

- «Si el valor exacto es cero y la aproximación vale $10^{-6}$, su error relativo al valor exacto es cero».

- «$\sqrt{1+x}\approx1+x/2$ queda certificada en todo $x>-1$ porque proviene de Taylor».

Localiza los fallos, repara cada conclusión y redacta una ficha verificable para una de las reparaciones.

**Solución.** La primera afirmación falla en $x=1/\varepsilon=10^4$, donde la corrección vale $1$. Para garantizar $\varepsilon x\le0.01$ con ese parámetro basta restringir $0\le x\le100$; para un dominio fijo $[0,X]$ la condición general es $\varepsilon X\le0.01$. La reparación cambia el dominio y explicita la comparación.

La segunda confunde residuo con error. La única raíz es cero y el candidato tiene error $1$. La pendiente mínima es $m=10^{-9}$, por lo que proposición 6.5 da una cota de $10^{-9}/10^{-9}=1$, no $10^{-6}$. Una reparación que alcance la tolerancia solicitada sería exigir $|\widetilde y|\le10^{-6}$; entonces el error respecto a la raíz sí queda certificado. La cifra del residuo necesita interpretarse junto con la pendiente.

La tercera pide un cociente con denominador cero, de modo que el error relativo está indefinido. El error absoluto vale $10^{-6}$. Con una escala positiva $S$ declarada, puede informarse el error referido a escala $10^{-6}/S$, conservando el tipo de las cantidades; si son números adimensionales y $S=1$, ese error escalado vale $10^{-6}$.

La cuarta no declara un radio ni controla el resto. Ejercicio 6.16 certifica, por ejemplo, el error absoluto $0.001$ para $|x|\le\rho$, donde $\rho=\sqrt{2\sqrt2(0.001)}\approx0.05318$. Una ficha para esta reparación contiene el modelo funcional $f(x)=\sqrt{1+x}$ con $x>-1$, punto base cero, variable de entrada adimensional, escala de salida $1$, candidato $1+x/2$, intervalo auxiliar $|x|\le1/2$, cota del resto $(\sqrt2/4)x^2$ y dominio final $|x|\le\rho$. La cota procede de la segunda derivada en el intervalo auxiliar y garantiza la tolerancia para todos los puntos del dominio final. No se extiende al dominio completo de la raíz cuadrada.

Una fórmula aproximada expresa una decisión sobre qué información conservar. El cálculo de este capítulo permite defender esa decisión con condiciones y cotas, y reconocer los datos para los que todavía no se dispone de una defensa.

[]{#bibliografía-citada}

## 6.14. Bibliografía citada {#fispm-c06-bibliografuxeda-citada .unnumbered}

[]{#canon-interno-citado}

### 6.14.3. Canon interno citado {#fispm-c06-canon-interno-citado}

- *Física para matemáticos*, Tomo I, capítulo 1, «Teorías físicas: fenómenos, modelos y leyes». [capítulo 1](fisica-para-matematicos-capitulo-1-teorias-fisicas-fenomenos-modelos-y-leyes.md#fispm-c01-teoruxedas-fuxedsicas-fenuxf3menos-modelos-y-leyes). Localizador utilizado: §11, «Dominio de validez y teorías efectivas», citado en §13.

- *Física para matemáticos*, Tomo I, capítulo 2, «Magnitudes, unidades y análisis dimensional». [capítulo 2](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md#fispm-c02-magnitudes-unidades-y-anuxe1lisis-dimensional). Localizadores utilizados: §§9--10, citados en §§2, 4 y 12.

- *Física para matemáticos*, Tomo I, capítulo 3, «Medición, incertidumbre, estimación y órdenes de magnitud». [capítulo 3](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md#fispm-c03-mediciuxf3n-incertidumbre-estimaciuxf3n-y-uxf3rdenes-de-magnitud). Localizadores utilizados: §§10, 12 y 14, citados en §§1, 4, 6, 11 y 13.

[]{#obras-externas-citadas}

### 6.14.4. Obras externas citadas {#fispm-c06-obras-externas-citadas}

- Hinch, E. J. *Perturbation Methods*. Cambridge University Press, 1991. Localizadores utilizados: cap. 1, §§1.1--1.2, pp. 1--7, citado en §§3, 5, 10 y 11; cap. 2, §§2.1--2.2, pp. 19--26, citado en §9.

- Riley, K. F.; Hobson, M. P.; Bence, S. J. *Mathematical Methods for Physics and Engineering*. 3.ª ed. Cambridge University Press, 2006. Localizador utilizado: §4.6, «Taylor series», pp. 136--140, citado en §§7--8.
