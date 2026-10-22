---
title: "Cinemática en una dimensión"
subtitle: "Física para matemáticos · Tomo I · Capítulo 7"
author: "A. Peña"
description: "Capítulo 7 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0347
source-id: FISPM-T1-C07
editorial-id: FPM-I-07
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0346"]
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
archive: true
edition: v04
search: false
sitemap: false
listing: false
---

::: {.callout-note}
## Edición archivada · v04

Esta página conserva la edición de 17 de octubre de 2026. La [edición canónica revisada](/libros/para-matematicos/fisica-para-matematicos.html) reúne los capítulos 0–27 y sus soluciones.
:::

[Capítulo 6](fisica-para-matematicos-capitulo-6-modelos-aproximaciones-escalas-y-linealizacion.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 8](fisica-para-matematicos-capitulo-8-cinematica-en-varias-dimensiones.md)

[]{#fispm-c07-cinemuxe1tica-en-una-dimensiuxf3n}

[]{#prerrequisitos-y-propósito}

## Prerrequisitos y propósito {#fispm-c07-prerrequisitos-y-propuxf3sito .unnumbered}

Se utilizan derivadas e integrales de una variable de M3 y la representación geométrica de M2 disponible en el capítulo 5. El capítulo 5 aporta posición, velocidad, aceleración y longitud; capítulo 6, las cotas para controlar aproximaciones. El capítulo estudia historias sobre una recta fija, reconstrucciones con datos iniciales, eventos e identificación a partir de posiciones. Las aceleraciones se prescriben como datos cinemáticos; su explicación dinámica se estudiará después.

[]{#una-recta-orientada-y-una-historia-temporal}

[]{#fispm-t1-c07-s01}

[]{#fpm-i-07-s01}

## 1. Una recta orientada y una historia temporal {#fispm-c07-una-recta-orientada-y-una-historia-temporal}

Un móvil se desplaza a lo largo de un riel recto. Para describirlo podemos registrar una sucesión de posiciones, pero una lista de números sólo adquiere significado después de fijar dónde está el origen, qué sentido se considera positivo y qué instante corresponde a cada registro. La cifra $2$ no identifica por sí sola una posición; tampoco indica si el móvil está avanzando o regresando. El problema cinemático comienza con una representación que permita interpretar esos datos.

El capítulo 5 construyó la posición como un punto del espacio y la velocidad como un vector. Aquí especializamos esa construcción a una recta espacial fija. Ganamos una función real de tiempo, sin perder la diferencia entre el punto físico, el vector de desplazamiento y su componente.

[]{#la-coordenada-que-representa-una-posición}

### La coordenada que representa una posición {#fispm-c07-la-coordenada-que-representa-una-posiciuxf3n}

Sean $O$ un punto fijo y $e$ un vector unitario fijo, con $\|e\|=1$. La recta orientada correspondiente es $\ell=\{O+\xi e:\xi\in\mathbb R\}$. El signo de $\xi$ identifica uno de sus dos sentidos; su módulo mide la distancia al origen en la unidad de longitud elegida. El símbolo $O+\xi e$ expresa la traslación de un punto por un vector, no una suma de dos puntos.

[]{#fispm-t1-c07-d0001}

**Definición 7.1 --- Historia rectilínea en una coordenada fija.** Una historia rectilínea sobre $\ell$, durante un intervalo temporal no degenerado $I$, es una aplicación $P:I\to\ell$ representada por una función continua $x:I\to\mathbb R$ mediante $$P(t)=O+x(t)e,\qquad t\in I.$$ El punto $O$, la orientación $e$ y la interpretación física del parámetro $t$ se mantienen fijos durante la historia. Cuando se requiera velocidad, se exigirá la diferenciabilidad correspondiente de $x$; cuando se requiera aceleración continua, se trabajará con $x\in C^2$ en el intervalo considerado.

La continuidad forma parte de la clase de historias que adoptamos: excluye saltos instantáneos de posición. No afirmamos que cualquier aplicación continua tenga velocidad o aceleración. Esas cantidades requieren hipótesis adicionales, y se pueden estudiar sólo en una parte del dominio.

La coordenada $x(t)$ es una magnitud firmada de longitud. Un valor negativo señala una posición al otro lado del origen, sin afirmar nada sobre el sentido del movimiento. Ese sentido depende de cómo cambia la coordenada con el tiempo. Si $t_1<t_2$, el desplazamiento entre ambos instantes es el vector $$\overrightarrow{P(t_1)P(t_2)}=\bigl(x(t_2)-x(t_1)\bigr)e.$$ Su componente puede ser positiva, negativa o nula. Una componente nula sólo informa que los extremos coinciden; el móvil pudo desplazarse durante el intervalo.

[]{#fispm-t1-c07-mp0001}

**Principio metodológico 7.1 --- Fijar representación y reloj antes de calcular.** Toda ley rectilínea debe acompañarse de su intervalo temporal, origen, orientación y significado del reloj. Una modificación de la coordenada debe interpretarse respecto de esos datos antes de atribuirla a un movimiento diferente.

Cambiar un origen fijo u orientar el eje en el sentido opuesto modifica la representación. Cambiar físicamente el reloj o mover el marco plantea otra cuestión, que no necesitamos para este capítulo. Los marcos móviles quedan reservados para el capítulo 8.

[]{#de-la-componente-al-vector}

### De la componente al vector {#fispm-c07-de-la-componente-al-vector}

Usaremos $v(t)$ y $a(t)$ para las componentes escalares firmadas de velocidad y aceleración. Los vectores completos se escribirán $\mathbf v(t)$ y $\mathbf a(t)$. Esta convención importa: el signo de $v$ depende de la orientación, mientras que la rapidez es una magnitud no negativa.

[]{#fispm-t1-c07-p0001}

**Proposición 7.1 --- Especialización escalar en una recta fija.** Si $x$ es diferenciable en un instante interior $t$, entonces $$\mathbf v(t)=x'(t)e=v(t)e,\qquad v(t)=x'(t).$$ Si $x$ es dos veces diferenciable en ese instante, entonces $\mathbf a(t)=x''(t)e=a(t)e$, con $a(t)=x''(t)$. La rapidez es $\|\mathbf v(t)\|=|v(t)|$.

**Demostración.** Para $h\ne0$ tal que $t+h\in I$, el cociente vectorial que define la velocidad es $$\frac{\overrightarrow{P(t)P(t+h)}}{h} =\frac{x(t+h)-x(t)}{h}\,e.$$ El vector $e$ es constante. El límite del coeficiente existe por diferenciabilidad de $x$, y da $x'(t)e$. Derivar una segunda vez, manteniendo $e$ fijo, produce $x''(t)e$. Finalmente, la homogeneidad de la norma y $\|e\|=1$ dan $\|x'(t)e\|=|x'(t)|$. $\square$

La constancia de $e$ autoriza los pasos. Si la dirección dependiera del tiempo, derivar únicamente el coeficiente perdería parte del cambio del vector; no estamos en esa situación.

Las dimensiones de las componentes son $[x]=L$, $[v]=L/T$ y $[a]=L/T^2$. Derivar no convierte una coordenada de longitud en otra longitud. Un resultado como $v=2$ necesita una unidad de longitud dividida por una unidad de tiempo para ser una afirmación física completa.

[]{#escalas-para-escribir-leyes-y-ejercicios}

### Escalas para escribir leyes y ejercicios {#fispm-c07-escalas-para-escribir-leyes-y-ejercicios}

Los polinomios son útiles para explorar movimientos, pero sus términos deben tener dimensiones compatibles. Para evitar expresiones como una suma de tiempo y tiempo al cuadrado sin coeficientes apropiados, elegimos escalas $T>0$ y $L>0$, y referencias fijas $t_0,x_*$. Escribimos $u=(t-t_0)/T$ y $x(t)=x_*+LX(u)$, donde $u$ y $X$ son adimensionales. Así se reutiliza la adimensionalización del capítulo 2, sin volver a desarrollar su teoría.

La regla de la cadena da $v(t)=(L/T)X'(u)$ y $a(t)=(L/T^2)X''(u)$. Denotaremos $V(u)=X'(u)$ y $A(u)=V'(u)$ a las componentes normalizadas. Las primas en $X,V$ se refieren a $u$; las primas en $x$ se refieren a $t$. Las escalas permiten recuperar las magnitudes físicas después del cálculo. La interfaz dimensional procede de [capítulo 2](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md#fispm-c02-magnitudes-unidades-y-anuxe1lisis-dimensional), §§9--10.

Por ejemplo, la ley $X(u)=1+u^2$ representa $x(t)=x_*+L\bigl(1+((t-t_0)/T)^2\bigr)$. Su velocidad es $(2L/T)u$, no simplemente $2u$ con unidades de velocidad omitidas. Para $u<0$ el móvil se desplaza en el sentido negativo; para $u>0$, en el positivo. La posición puede permanecer al lado positivo del origen durante ambos tramos: posición positiva y velocidad positiva son afirmaciones distintas.

En los ejercicios, salvo indicación contraria, se toma $x_*=0$, de modo que $P(t)=O+LX(u)e$. El instante $t_0$ es la referencia del reloj; un valor $u<0$ pertenece a la historia si así lo permite su dominio.

[]{#ejercicios}

### Ejercicios {#fispm-c07-ejercicios}

[]{#fispm-t1-c07-e0001}

[]{#fispm-t1-c07-e0007}

**Ejercicio 7.1.** Una historia tiene $X(u)=2+u$ para $0\le u\le2$. Manteniendo el mismo reloj, cambia al origen $O'=O+3Le$ y a la orientación $e'=-e$. Encuentra la coordenada normalizada $Y(u)$ respecto de esos nuevos datos, sus componentes de velocidad y aceleración, y comprueba si se ha modificado la posición física.

**Solución.** La misma posición debe satisfacer $O+LX(u)e=O'+LY(u)e'$. Sustituyendo los nuevos datos, el segundo miembro es $O+3Le-LY(u)e$. Comparar los coeficientes de $e$ da $X(u)=3-Y(u)$, por lo que $Y(u)=1-u$.

La componente física nueva de velocidad es $(L/T)Y'(u)=-L/T$ y la de aceleración es $(L/T^2)Y''(u)=0$. En la representación inicial la velocidad era $L/T$ y la aceleración cero. Sin embargo, el vector nuevo de velocidad es $(-L/T)e'=(L/T)e$, igual al anterior. Además, $O'+LY(u)e'=O+L(2+u)e$ para todo $u$ del intervalo. Cambiaron la coordenada y su signo, mientras que posición y vector velocidad se conservaron.

[]{#fispm-t1-c07-e0002}

**Ejercicio 7.2.** Para $X(u)=1-u^2$ en $[-1,1]$, reconstruye la posición, los vectores velocidad y aceleración, y la rapidez. Calcula el desplazamiento entre los dos extremos temporales y explica qué permite concluir.

**Solución.** La posición es $P(t)=O+L(1-u^2)e$, donde $t=t_0+Tu$. Proposición 7.1 y la regla de la cadena dan $\mathbf v(t)=-(2L/T)u\,e$ y $\mathbf a(t)=-(2L/T^2)e$. La rapidez vale $(2L/T)|u|$, de modo que se anula en $u=0$ y es positiva en los demás instantes.

En $u=-1$ y $u=1$ la coordenada es cero, por lo que el desplazamiento entre extremos es el vector nulo. Durante la historia, en cambio, $X(0)=1$: el móvil alcanza una posición distinta antes de regresar. La coincidencia de extremos no prueba reposo durante el intervalo. El sentido de ida y regreso se reconoce en el signo de $V(u)=-2u$.

La representación en una recta fija importa las distinciones geométricas de [capítulo 5, §3](fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md#fispm-c05-posiciuxf3n-relativa-y-coordenadas-de-una-curva) y su derivación de velocidad y aceleración en §§5--7. Una vez fijados los datos que dan significado a $x(t)$, podemos leer su gráfica temporal.

[]{#leer-la-gráfica-de-posición}

[]{#fispm-t1-c07-s02}

[]{#fpm-i-07-s02}

## 2. Leer la gráfica de posición {#fispm-c07-leer-la-gruxe1fica-de-posiciuxf3n}

Una curva dibujada en un plano puede sugerir que el móvil sube, baja o gira. Si los ejes del dibujo son tiempo y posición, esas impresiones deben reinterpretarse: el móvil sigue en una recta espacial. La curva muestra cómo cambia su coordenada con el reloj, no la forma de un camino en un espacio de dos dimensiones.

Esta diferencia también explica por qué una gráfica descendente no describe necesariamente una posición negativa. Puede representar un móvil que todavía está a la derecha del origen, pero se acerca a él. Para leerla hay que distinguir la altura de la curva de su pendiente.

[]{#dos-conjuntos-con-información-diferente}

### Dos conjuntos con información diferente {#fispm-c07-dos-conjuntos-con-informaciuxf3n-diferente}

[]{#fispm-t1-c07-d0002}

**Definición 7.2 --- Gráfica temporal y escalas de sus ejes.** La gráfica temporal de una coordenada $x:I\to\mathbb R$ es el conjunto $G_x=\{(t,x(t)):t\in I\}$ en el plano de tiempo y coordenada. Sus ejes representan magnitudes de tipos diferentes y deben llevar unidades o escalas declaradas. Con las referencias y escalas de §1, su representación normalizada es $G_X=\{(u,X(u)):u\in J\}$, donde $J=\{(t-t_0)/T:t\in I\}$.

La trayectoria espacial es otro conjunto: $\Gamma=\{O+x(t)e:t\in I\}\subseteq\ell$. En $G_x$ se conserva el tiempo asociado a cada posición. En $\Gamma$ sólo aparecen las posiciones alcanzadas. Dos historias pueden recorrer la misma parte de la recta con tiempos diferentes y tener gráficas temporales distintas.

Si $t_1<t_2$, la pendiente de la secante que une los puntos de la gráfica es $\bigl(x(t_2)-x(t_1)\bigr)/(t_2-t_1)$. Es la componente de velocidad media ya definida en el capítulo 5. Su signo informa el sentido del desplazamiento neto, pero no garantiza que el móvil se haya desplazado en ese mismo sentido durante todo el intervalo.

Cuando $x$ es diferenciable en un instante interior, las pendientes de las secantes con un extremo fijo convergen a $x'(t)=v(t)$. La pendiente tangente es por ello una lectura local de velocidad. La altura $x(t)$ y la pendiente $v(t)$ pueden tener signos diferentes; se refieren a posición y cambio de posición, respectivamente.

[]{#fispm-t1-c07-mp0002}

**Principio metodológico 7.2 --- Leer pendientes con unidades y escalas.** Una pendiente debe calcularse como cociente de incrementos de las magnitudes representadas. El ángulo aparente de una recta en el papel no determina una velocidad hasta declarar la relación entre las escalas de los ejes.

Para ver el papel de esas escalas, sean $h=k_t(t-t_0)$ y $z=k_x(x-x_*)$ las distancias horizontal y vertical en el papel, con $k_t,k_x>0$. Entonces $dz/dh=(k_x/k_t)v$. Los factores tienen unidades de longitud del papel por tiempo y por longitud física, respectivamente. Si se duplica $k_x$ manteniendo $k_t$, se duplica la pendiente dibujada aunque la historia sea la misma.

En las coordenadas normalizadas, la regla es $v=(L/T)X'$. La derivada $X'$ mide una pendiente adimensional; el factor $L/T$ la convierte en componente de velocidad. Esta distinción evita asignar un significado físico universal a una inclinación de $45$ grados.

[]{#qué-autoriza-el-signo-de-la-derivada}

### Qué autoriza el signo de la derivada {#fispm-c07-quuxe9-autoriza-el-signo-de-la-derivada}

[]{#fispm-t1-c07-p0002}

**Proposición 7.2 --- Signo de la pendiente y monotonía.** Sea $x$ continua en $[\alpha,\beta]$, con $\alpha<\beta$, y diferenciable en su interior. Si $x'(t)>0$ para todo $t\in(\alpha,\beta)$, entonces $x$ es estrictamente creciente. Si $x'(t)\ge0$ en ese interior, entonces $x$ es no decreciente. Las versiones con signo negativo dan decrecimiento estricto o no crecimiento. Además, si $x$ tiene un extremo local en un instante interior $t_c$ donde es diferenciable, entonces $x'(t_c)=0$.

**Demostración.** Para dos instantes $s<t$ del intervalo, el teorema del valor medio proporciona $c\in(s,t)$ con $x(t)-x(s)=x'(c)(t-s)$. El factor $t-s$ es positivo, por lo que una derivada positiva produce una diferencia positiva, y una derivada no negativa produce una diferencia no negativa. Los otros signos se tratan mediante la misma igualdad.

Para la afirmación sobre extremos, supongamos primero un máximo local en $t_c$. Para incrementos positivos suficientemente pequeños, el cociente $\bigl(x(t_c+h)-x(t_c)\bigr)/h$ es no positivo; para incrementos negativos, es no negativo. Si ambos cocientes convergen a una misma derivada, ésta debe ser simultáneamente no positiva y no negativa, luego es cero. En un mínimo se invierten las desigualdades y se obtiene la misma conclusión. $\square$

El resultado separa un criterio suficiente de una condición necesaria. Una derivada positiva en todo un intervalo basta para crecimiento estricto. Que una función sea estrictamente creciente no obliga a que su derivada sea positiva en cada instante: $X(u)=u^3$ crece estrictamente, pero $X'(0)=0$. Del mismo modo, la condición $v(t_c)=0$ es necesaria para un extremo local interior diferenciable, pero no lo garantiza.

Tampoco se aplica esa condición sin revisar la posición temporal del punto. Un máximo en el extremo de un intervalo cerrado puede tener pendiente no nula. Las hipótesis «interior» y «diferenciable» forman parte de la afirmación, no son detalles que se puedan omitir al mirar un dibujo.

[]{#una-lectura-con-signos-separados}

### Una lectura con signos separados {#fispm-c07-una-lectura-con-signos-separados}

Consideremos $X(u)=2-u+u^2$ en $[0,1]$. La coordenada normalizada es positiva en todo el intervalo, porque $X(u)=(u-1/2)^2+7/4$. La velocidad normalizada es $V(u)=-1+2u$, que es negativa antes de $u=1/2$, nula allí y positiva después. El móvil primero se desplaza hacia coordenadas menores y luego hacia coordenadas mayores, sin cruzar el origen.

La gráfica permite organizar esa información:

  Intervalo o instante   Signo de $V$   Lectura de $X$
  ---------------------- -------------- ----------------
  $0<u<1/2$              negativo       decrece
  $u=1/2$                cero           mínimo local
  $1/2<u<1$              positivo       crece

El mínimo se confirma por los signos de la derivada a ambos lados. No se ha deducido exclusivamente de una tangente horizontal. El siguiente ejercicio exige repetir esa lectura cuando hay dos puntos estacionarios.

[]{#ejercicios-1}

### Ejercicios {#fispm-c07-ejercicios-1}

[]{#fispm-t1-c07-e0003}

**Ejercicio 7.3.** Analiza $X(u)=u^3-u$ en $[-1,1]$. Determina puntos estacionarios, intervalos de crecimiento y decrecimiento, extremos locales interiores y extremos globales del intervalo. Explica qué información corresponde a la gráfica temporal.

**Solución.** La derivada es $V(u)=3u^2-1$, cuyos ceros son $u_-=-1/\sqrt3$ y $u_+=1/\sqrt3$. El signo de $V$ es positivo para $|u|>1/\sqrt3$ y negativo para $|u|<1/\sqrt3$. Proposición 7.2 da crecimiento en $[-1,u_-]$, decrecimiento en $[u_-,u_+]$ y crecimiento en $[u_+,1]$.

En $u_-$ el signo pasa de positivo a negativo: allí hay un máximo local. En $u_+$ pasa de negativo a positivo: allí hay un mínimo local. Sus valores son $X(u_-)=2/(3\sqrt3)$ y $X(u_+)=-2/(3\sqrt3)$. Los extremos temporales tienen $X(-1)=X(1)=0$. Comparar estos cuatro valores muestra que el máximo y mínimo locales encontrados también son el máximo y mínimo globales.

Las posiciones físicas son $x=LX$ con la convención de §1, y los tiempos son $t=t_0+Tu$. La curva que sube y baja en el plano $(u,X)$ representa cambios de sentido sobre una sola recta espacial. No describe una trayectoria espacial cúbica en un plano.

[]{#fispm-t1-c07-e0004}

**Ejercicio 7.4.** La misma ley $X(u)=2u$ se dibuja con dos escalas verticales distintas y la misma escala horizontal. Explica qué cambia en el dibujo. Si $L=3\,\mathrm m$ y $T=2\,\mathrm s$, calcula la velocidad física y decide si cambia al redibujar la gráfica.

**Solución.** La pendiente normalizada es $X'=2$, de modo que $v=(L/T)2=3\,\mathrm{m/s}$. Si la escala vertical del papel se duplica, la altura dibujada de cada punto respecto de la referencia y la pendiente dibujada se duplican. El ángulo que forma la recta con la horizontal cambia.

El cociente entre incrementos físicos sigue siendo $\Delta x/\Delta t=3\,\mathrm{m/s}$. No cambian $L,T$ ni la ley temporal; cambió la representación sobre el papel. Calcular una velocidad directamente desde un ángulo sin consultar los ejes confundiría ambas situaciones.

La lectura de pendientes recupera las cantidades medias e instantáneas discutidas por Shankar, *Fundamentals of Physics I*, edición ampliada de 2019, cap. 1 §1.3, pp. 4--6. Las gráficas y ejercicios de esta sección se construyen aquí a partir de esas distinciones. La gráfica de velocidad hará visible por separado la información que en la de posición aparece como pendiente.

[]{#leer-la-gráfica-de-velocidad}

[]{#fispm-t1-c07-s03}

[]{#fpm-i-07-s03}

## 3. Leer la gráfica de velocidad {#fispm-c07-leer-la-gruxe1fica-de-velocidad}

Dos móviles pueden pasar por la misma posición con velocidades distintas. Una gráfica de posición permite reconocer esa diferencia a través de sus pendientes; la gráfica de velocidad la presenta directamente como una altura firmada. Sin embargo, esa altura ya no es una posición. Estar por debajo del eje horizontal significa tener componente negativa de velocidad, no estar necesariamente al lado negativo del origen espacial.

La gráfica $G_v=\{(t,v(t)):t\in I\}$ tiene tiempo en su eje horizontal y velocidad en el vertical. En la representación normalizada usamos $(u,V(u))$, con $v=(L/T)V$. Como $L/T>0$, $v$ y $V$ tienen el mismo signo. Podemos estudiar el signo con $V$ y restaurar las unidades cuando se pida una magnitud física.

[]{#altura-pendiente-y-sentido}

### Altura, pendiente y sentido {#fispm-c07-altura-pendiente-y-sentido}

Si $v$ es positiva durante un intervalo, proposición 7.2 asegura que la coordenada crece. Si es negativa, la coordenada decrece. La altura de $G_v$ informa el sentido de recorrido respecto de $e$ y su módulo informa la rapidez. Dos valores $v=3\,\mathrm{m/s}$ y $v=-3\,\mathrm{m/s}$ representan velocidades opuestas con la misma rapidez.

La pendiente de $G_v$ informa otra cosa. Una secante entre $t_1<t_2$ tiene pendiente $\bigl(v(t_2)-v(t_1)\bigr)/(t_2-t_1)$: es la componente de aceleración media durante ese intervalo. Si $v$ es diferenciable en un instante interior, la pendiente tangente es $v'(t)=a(t)$. Una gráfica de velocidad horizontal describe componente constante de velocidad, no necesariamente reposo. El reposo corresponde a la altura cero.

Por ejemplo, para $V(u)=2-u$ en $[0,3]$, la gráfica de velocidad es una recta descendente. Hasta $u=2$, su altura es positiva y la coordenada crece, aunque la velocidad se haga cada vez menor. Después de $u=2$, la altura es negativa y la coordenada decrece. La pendiente normalizada es $-1$ a ambos lados, de modo que la componente física de aceleración es $-L/T^2$ durante todo el intervalo. La pendiente constante no evita el cambio de sentido.

No hemos reconstruido una coordenada específica a partir de esa velocidad. Distintas posiciones iniciales pueden compartir la misma gráfica de velocidad; esa información faltante se estudiará sistemáticamente en §6.

[]{#lo-que-ocurre-en-un-cero}

### Lo que ocurre en un cero {#fispm-c07-lo-que-ocurre-en-un-cero}

En un instante interior $t_c$ con $v(t_c)=0$, el móvil está en reposo instantáneo. Para saber si invierte su sentido necesitamos información a ambos lados. Un valor de una función en un punto no contiene los signos de sus valores vecinos.

[]{#fispm-t1-c07-d0003}

**Definición 7.3 --- Cambio de sentido local.** Sea $x$ de clase $C^1$ en un entorno de un instante interior $t_c$. Diremos que presenta un cambio de sentido local aislado en $t_c$ si $v(t_c)=0$ y existe $\rho>0$, con $(t_c-\rho,t_c+\rho)\subseteq I$, tal que se cumple una de estas dos alternativas: $v>0$ en $(t_c-\rho,t_c)$ y $v<0$ en $(t_c,t_c+\rho)$, o los signos son los opuestos.

La definición fija el caso elemental que usaremos. Pide signos estrictos en cada semientorno y un cero aislado entre ellos. No pretende clasificar historias con infinitos ceros acumulados ni sustituye una discusión de posiciones no diferenciables. Al pedir un instante interior evitamos inferir un «antes» que no pertenece al dominio declarado.

Por proposición 7.2, la primera alternativa describe coordenada creciente antes de $t_c$ y decreciente después, por lo que $t_c$ es un máximo local estricto. La segunda describe un mínimo local estricto. La continuidad de $v$ también explica por qué los signos opuestos no pueden mantenerse hasta el instante central con una velocidad allí positiva o negativa.

[]{#fispm-t1-c07-mp0003}

**Principio metodológico 7.3 --- Auditar el signo a ambos lados de un cero.** Para interpretar un cero de velocidad se debe distinguir reposo instantáneo, cambio de sentido y reposo durante un intervalo. Una inversión local se certifica con los signos vecinos; la igualdad $v(t_c)=0$ por sí sola no la certifica.

Hay tres situaciones elementales. Si $V(u)=u$, el signo cambia de negativo a positivo en cero. Si $V(u)=u^2$, el signo es positivo a ambos lados: la velocidad se anula, pero la coordenada sigue creciendo. Si $V$ es idénticamente cero en un intervalo, la coordenada es constante allí, por el teorema del valor medio. En el último caso no existe un único instante aislado que caracterice el reposo.

[]{#eventos-que-no-deben-confundirse}

### Eventos que no deben confundirse {#fispm-c07-eventos-que-no-deben-confundirse}

La ley $X(u)=1+u$ en $[-2,0]$ cruza el origen en $u=-1$. Su velocidad normalizada es $1$ durante todo el intervalo, de modo que ese cruce ocurre sin reposo ni inversión. Estar en el origen no obliga a tener velocidad cero.

La ley $X(u)=2-u^2$ en $[-1,1]$ ofrece otro patrón. Su velocidad normalizada $-2u$ pasa de positiva a negativa en cero. Allí hay reposo e inversión, pero la coordenada vale $2$, lejos del origen elegido. El evento de inversión puede ocurrir en una posición cualquiera.

Estas leyes separan las preguntas «estar en el origen», «tener velocidad cero» e «invertir el sentido». La gráfica de velocidad responde a las dos últimas sólo con las condiciones correspondientes. El ejercicio siguiente muestra que también reposo e inversión deben distinguirse entre sí.

[]{#ejercicios-2}

### Ejercicios {#fispm-c07-ejercicios-2}

[]{#fispm-t1-c07-e0005}

**Ejercicio 7.5.** Compara $X_1(u)=u^2$ y $X_2(u)=u^3$ en un entorno de $u=0$. Calcula sus velocidades normalizadas, clasifica el reposo central y decide si la afirmación «velocidad cero implica inversión» es válida.

**Solución.** Para la primera historia, $V_1(u)=2u$ es negativa a la izquierda y positiva a la derecha. En cero es nula. Definición 7.3 certifica una inversión local del sentido negativo al positivo; $X_1$ tiene allí un mínimo.

Para la segunda, $V_2(u)=3u^2$ es positiva para todo $u\ne0$ del entorno y se anula en cero. Hay reposo instantáneo, pero no inversión. También puede verificarse el crecimiento estricto de $u^3$ comparando directamente sus valores en dos argumentos ordenados.

La segunda historia es un contraejemplo a la afirmación propuesta. Ambas tienen velocidad cero en el mismo instante normalizado, mientras que sus signos vecinos determinan comportamientos diferentes. Multiplicar las velocidades normalizadas por $L/T>0$ no altera esa clasificación.

[]{#fispm-t1-c07-e0006}

**Ejercicio 7.6.** Una historia diferenciable tiene componente de velocidad normalizada $V(u)=1-u^2$ en $[-2,2]$. Determina todos sus ceros, signos y cambios de sentido. Contrasta el resultado con una historia cuya velocidad es idénticamente cero en un intervalo.

**Solución.** La ecuación $1-u^2=0$ tiene soluciones $u=-1$ y $u=1$, ambas interiores al dominio. La función es negativa en $[-2,-1)$, positiva en $(-1,1)$ y negativa en $(1,2]$. En $u=-1$ pasa de negativo a positivo, por lo que hay un cambio de sentido asociado a un mínimo de coordenada. En $u=1$ pasa de positivo a negativo, asociado a un máximo. En los dos instantes hay reposo instantáneo.

Si $V\equiv0$ en un intervalo, también $v\equiv0$ allí. Para dos instantes $s<t$, el valor medio aplicado a la coordenada da $x(t)-x(s)=v(c)(t-s)=0$ para algún $c\in(s,t)$. La coordenada es constante en todo ese intervalo. No se presenta la situación de la definición 7.3, que exige velocidades no nulas en los semientornos de un instante aislado.

Conocer la gráfica de velocidad permite clasificar sentidos y reposos sin fijar todavía una posición inicial. La lectura de su pendiente nos lleva a la gráfica de aceleración, donde habrá que conservar esa información de signos para interpretar la rapidez.

[]{#leer-la-gráfica-de-aceleración}

[]{#fispm-t1-c07-s04}

[]{#fpm-i-07-s04}

## 4. Leer la gráfica de aceleración {#fispm-c07-leer-la-gruxe1fica-de-aceleraciuxf3n}

Un móvil que se desplaza hacia coordenadas negativas puede tener aceleración negativa y aumentar su rapidez. La palabra «negativa» indica una orientación de la componente, mientras que «aumentar la rapidez» compara módulos. Confundir ambas operaciones conduce a interpretar una misma gráfica de dos maneras incompatibles.

La aceleración describe cómo varía la velocidad. Su gráfica tiene tiempo en el eje horizontal y una componente de tipo $L/T^2$ en el vertical. No expresa la causa de esa variación. Aquí la estudiamos como una cantidad cinemática, siguiendo la separación entre descripción y dinámica establecida en el capítulo 5.

[]{#la-altura-de-la-gráfica-de-aceleración}

### La altura de la gráfica de aceleración {#fispm-c07-la-altura-de-la-gruxe1fica-de-aceleraciuxf3n}

Si $a(t)>0$ durante un intervalo, la componente $v(t)$ es estrictamente creciente bajo las hipótesis del valor medio. Puede pasar, por ejemplo, de $-4\,\mathrm{m/s}$ a $-2\,\mathrm{m/s}$: aumenta como número firmado, pero disminuye su módulo. También puede pasar de $2\,\mathrm{m/s}$ a $4\,\mathrm{m/s}$: ahora aumentan componente y rapidez.

Si $a(t)<0$, la componente de velocidad decrece. Pasar de $4$ a $2\,\mathrm{m/s}$ disminuye la rapidez; pasar de $-2$ a $-4\,\mathrm{m/s}$ la aumenta. La altura de la gráfica de aceleración, por sí sola, no distingue esos casos.

Con $u=(t-t_0)/T$ y las escalas de §1, la aceleración es $a(t)=(L/T^2)A(u)$. La relación $A=V'$ ayuda a leer la variación de $V$, pero las unidades físicas se recuperan mediante $L/T^2$. Una recta horizontal en la gráfica de $a$ describe aceleración constante; no describe velocidad constante salvo que esa altura sea cero.

Para $A=0$ en un intervalo, el valor medio implica que $v$ es constante en él. Todavía puede haber desplazamiento si esa constante es no nula. El cálculo no dice por qué el móvil conserva su velocidad: una afirmación sobre fuerzas o inercia sería adicional y pertenece a capítulos posteriores.

[]{#derivar-la-rapidez-con-sus-hipótesis}

### Derivar la rapidez con sus hipótesis {#fispm-c07-derivar-la-rapidez-con-sus-hipuxf3tesis}

La rapidez es $r(t)=|v(t)|$. El valor absoluto cambia de fórmula en cero. Antes de derivarlo debemos comprobar que la velocidad no se anula en el punto considerado.

[]{#fispm-t1-c07-p0003}

**Proposición 7.3 --- Variación de la rapidez fuera de reposo.** Sea $v$ diferenciable en un instante interior $t$ y supongamos $v(t)\ne0$. Entonces la rapidez es diferenciable en ese instante y satisface $$r'(t)=\operatorname{sgn}(v(t))\,a(t),$$ donde $\operatorname{sgn}(z)=1$ si $z>0$ y $\operatorname{sgn}(z)=-1$ si $z<0$. En particular, el signo de $r'(t)$ es el signo del producto $v(t)a(t)$.

**Demostración.** La diferenciabilidad de $v$ implica su continuidad en $t$. Si $v(t)>0$, la continuidad asegura que $v$ sigue siendo positiva en un entorno de $t$: basta restringirlo hasta que $|v(s)-v(t)|<v(t)/2$. En ese entorno $|v(s)|=v(s)$, y derivar en $t$ da $r'(t)=v'(t)=a(t)$.

Si $v(t)<0$, se escoge análogamente un entorno donde $v(s)<0$. Allí $|v(s)|=-v(s)$ y $r'(t)=-a(t)$. Son las dos alternativas de la fórmula. Puesto que $v(t)=\operatorname{sgn}(v(t))|v(t)|$ con $|v(t)|>0$, los números $r'(t)=\operatorname{sgn}(v(t))a(t)$ y $v(t)a(t)$ tienen el mismo signo. $\square$

La continuidad mantiene el signo cerca del instante y autoriza elegir una rama del valor absoluto. No se ha derivado una función de signo a través de un cero; ése habría sido un paso ilegítimo.

En un intervalo donde $v$ no se anula y el producto $va$ es positivo en todos sus instantes interiores, la rapidez es estrictamente creciente por el valor medio. Si el producto es negativo, es estrictamente decreciente. Un signo de $r'$ en un único instante expresa una tasa local; para concluir monotonía durante un intervalo se necesita una condición sobre todo ese intervalo.

[]{#fispm-t1-c07-mp0004}

**Principio metodológico 7.4 --- Relacionar aceleración con velocidad al interpretar la rapidez.** Fuera de reposo, se deben comparar los signos de $v$ y $a$. Componentes con el mismo signo aumentan localmente la rapidez; componentes de signos opuestos la disminuyen. En un cero de velocidad se revisa directamente $|v|$, porque proposición 7.3 no se aplica allí.

La comparación queda organizada en cuatro casos:

  Signo de $v$   Signo de $a$   Signo de $r'$
  -------------- -------------- ---------------
  positivo       positivo       positivo
  positivo       negativo       negativo
  negativo       positivo       negativo
  negativo       negativo       positivo

Ninguna fila supone una fuerza. La tabla sólo traduce el cálculo del valor absoluto y conserva la distinción entre orientación y módulo.

[]{#el-instante-que-exige-otra-lectura}

### El instante que exige otra lectura {#fispm-c07-el-instante-que-exige-otra-lectura}

Para $V(u)=u^2$, la rapidez normalizada es $R(u)=u^2$ también en cero, porque la componente nunca es negativa. Su derivada existe allí y vale cero, aunque la hipótesis $v\ne0$ de la proposición 7.3 no se cumpla. La conclusión se obtiene de la fórmula explícita de $R$, no de una aplicación de la proposición 7.3 fuera de su alcance.

[]{#fispm-t1-c07-e0008}

Una velocidad que cambie de signo puede producir otra regularidad para su módulo. El valor absoluto se debe entonces escribir por separado a ambos lados del cero y se deben comparar los cocientes incrementales. Ejercicio 7.8 realiza ese control para una componente suave con signo cambiante.

La aceleración y la tasa de cambio de rapidez son cantidades distintas: la primera deriva $v$, mientras que la segunda deriva $|v|$ donde ese cálculo existe. Que falte una hipótesis de la proposición 7.3 obliga a buscar otro argumento; no prueba por sí solo que la rapidez sea no diferenciable.

[]{#ejercicios-3}

### Ejercicios {#fispm-c07-ejercicios-3}

**Ejercicio 7.7.** Para $V(u)=-2-u$ en $[0,1]$, determina la aceleración física, el sentido de movimiento y la variación de la rapidez. Audita la frase «una aceleración negativa siempre frena».

**Solución.** Derivar respecto de $u$ da $A=-1$, de modo que $a=-L/T^2$. La componente física de velocidad es $v=-(L/T)(2+u)$, negativa durante todo el intervalo; la coordenada decrece respecto de la orientación elegida.

La rapidez es $r=(L/T)(2+u)$. Al derivar respecto del tiempo, usando $du/dt=1/T$, se obtiene $r'=L/T^2>0$. La rapidez aumenta. Proposición 7.3 confirma el resultado: $v$ y $a$ son negativos, por lo que $va>0$.

Esta historia contradice la frase propuesta. La aceleración negativa describe decrecimiento de la componente firmada; sólo se interpreta como frenado, en el sentido de disminución de rapidez, cuando la velocidad es positiva durante el intervalo considerado.

**Ejercicio 7.8.** Para $V(u)=u$ en $[-1,1]$, calcula la rapidez normalizada y sus derivadas laterales en cero. Decide si proposición 7.3 permite calcular allí la derivada de la rapidez y compara con la aceleración.

**Solución.** La rapidez normalizada es $R(u)=|u|$. Como $R(0)=0$, su cociente incremental en cero es $|h|/h$: vale $-1$ para $h<0$ y $1$ para $h>0$. Los límites laterales son distintos, por lo que $R'(0)$ no existe.

En magnitudes físicas, $r(t)=(L/T)|(t-t_0)/T|=(L/T^2)|t-t_0|$. Las tasas laterales son $-L/T^2$ y $L/T^2$. La componente de velocidad, en cambio, es $v(t)=(L/T^2)(t-t_0)$ y tiene derivada $a=L/T^2$ también en $t_0$.

Proposición 7.3 no permite sustituir $t=t_0$ en su conclusión porque allí $v=0$. La falta de derivada de la rapidez se demuestra con el cociente incremental; no se deduce simplemente de que falte una hipótesis. Las cantidades están bien definidas como funciones en todo el intervalo, aunque una de ellas carezca de derivada bilateral en un instante.

Las gráficas de $x,v,a$ permiten así distinguir posición, sentido, rapidez y variación de velocidad. Esa lectura local deja una pregunta de intervalo: cuánto desplazamiento y cuánto recorrido acumula la historia. Para responderla, §5 utilizará las áreas de velocidad con signo y con valor absoluto.

[]{#desplazamiento-distancia-y-áreas-firmadas}

[]{#fispm-t1-c07-s05}

[]{#fpm-i-07-s05}

## 5. Desplazamiento, distancia y áreas firmadas {#fispm-c07-desplazamiento-distancia-y-uxe1reas-firmadas}

Un móvil sale de una marca del riel, alcanza otra y regresa a la primera. El desplazamiento total es cero, pero el recorrido no lo es. Las gráficas de §3 permiten reconocer el cambio de sentido; para medir cuánto se acumula durante cada parte necesitamos integrar la velocidad. El signo que distingue ida y regreso debe conservarse para el desplazamiento y eliminarse para sumar recorrido.

[]{#fig:I-07-N02}

<figure id="fig-fpm-v04-i-07-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-07-N02.svg" class="lightbox" data-gallery="fpm-v04-c07"><img src="/assets/books/fispm/v04/I-07-N02.svg" alt="Área firmada bajo la velocidad. Diagrama del capítulo 7; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="232" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 7.1.** Con $V=1-u$ entre $u=0$ y $2$, las áreas positiva y negativa se cancelan: $\Delta X=0$. La distancia normalizada suma sus módulos y vale uno. Véase §[5](#fispm-c07-desplazamiento-distancia-y-uxe1reas-firmadas).

</figcaption>

</figure>

En esta sección $x$ es de clase $C^1$ sobre $[\alpha,\beta]$, con $\alpha<\beta$. En un intervalo cerrado, esta regularidad significa que la derivada interior se extiende continuamente hasta los extremos, donde se interpreta lateralmente. Es la convención del capítulo 5. Escribimos $v=x'$ y mantenemos fijos $O,e$ en $P(t)=O+x(t)e$.

[]{#dos-cantidades-sobre-el-mismo-intervalo}

### Dos cantidades sobre el mismo intervalo {#fispm-c07-dos-cantidades-sobre-el-mismo-intervalo}

La componente del desplazamiento es $\Delta x=x(\beta)-x(\alpha)$; el vector completo es $\Delta x\,e$. La distancia recorrida es la longitud geométrica de esta historia temporal, no sólo la distancia entre sus extremos. Denotaremos ese recorrido por $d_{\mathrm{rec}}$. Su definición y su fórmula integral ya están disponibles en [capítulo 5, §13](fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md#fispm-c05-fuxf3rmula-de-longitud-de-arco-y-paruxe1metro-natural), proposición 7.28.

Una suma de términos $v(t_i)\Delta t_i$ conserva el signo de cada contribución. Si en lugar de $v$ usamos $|v|$, todas las contribuciones son no negativas. Bajo la hipótesis de continuidad, ambas sumas tienen límites integrales; la diferencia entre ellas persiste por mucho que se refine la partición.

[]{#fispm-t1-c07-p0004}

**Proposición 7.4 --- Áreas de velocidad, desplazamiento y distancia.** Bajo las hipótesis anteriores, $$\Delta x=\int_\alpha^\beta v(t)\,dt,\qquad d_{\mathrm{rec}}=\int_\alpha^\beta |v(t)|\,dt,$$ y se cumple $d_{\mathrm{rec}}\ge|\Delta x|$. Hay igualdad si y sólo si $v\ge0$ en todo $[\alpha,\beta]$ o $v\le0$ en todo ese intervalo. Se permite que $v$ se anule en puntos o subintervalos.

**Demostración.** El teorema fundamental del cálculo aplicado a $x$ da $x(\beta)-x(\alpha)=\int_\alpha^\beta x'(t)\,dt$. Por proposición 7.1, la norma del vector velocidad es $|v|$. La fórmula de longitud del capítulo 5 da entonces $d_{\mathrm{rec}}=\int_\alpha^\beta |v|$; no la estamos tomando como una definición nueva de longitud.

Las desigualdades $-|v(t)|\le v(t)\le|v(t)|$, integradas, producen $-d_{\mathrm{rec}}\le\Delta x\le d_{\mathrm{rec}}$, equivalentes a la cota anunciada.

Si $v\ge0$, ambas integrales coinciden y $\Delta x\ge0$. Si $v\le0$, la integral de $|v|$ es el opuesto de la de $v$, luego coincide con $|\Delta x|$. Para probar la necesidad, supongamos primero $\Delta x\ge0$ y $d_{\mathrm{rec}}=|\Delta x|=\Delta x$. Entonces $$\int_\alpha^\beta \bigl(|v(t)|-v(t)\bigr)\,dt=0.$$ El integrando es continuo y no negativo. Si fuera positivo en algún punto, la continuidad lo mantendría por encima de una constante positiva en un pequeño intervalo de longitud positiva, y su integral sería positiva. El mismo argumento funciona con un intervalo lateral si el punto es un extremo. Por tanto, $|v|-v$ es idénticamente cero: $v\ge0$. Si $\Delta x<0$, se aplica ese argumento a $|v|+v$ y se obtiene $v\le0$. $\square$

La continuidad permite pasar de una integral nula a una afirmación en cada punto. La condición de igualdad se refiere a no tomar ambos signos; no exige velocidad estrictamente positiva o negativa. Un reposo intermedio no añade recorrido, pero tampoco produce cancelación.

[]{#leer-un-área-con-unidades}

### Leer un área con unidades {#fispm-c07-leer-un-uxe1rea-con-unidades}

El área firmada entre la gráfica de $v$ y el eje temporal representa $\Delta x$: la parte bajo el eje aporta signo negativo. El área geométrica total representa $d_{\mathrm{rec}}$. En ambos casos las unidades son $(\mathrm{m/s})\mathrm s=\mathrm m$. Una superficie medida en centímetros cuadrados del papel necesita las escalas de ambos ejes para convertirse en una longitud física.

[]{#fispm-t1-c07-mp0005}

**Principio metodológico 7.5 --- Conservar el signo para desplazamiento y el módulo para recorrido.** Antes de integrar una gráfica de velocidad, debe precisarse si se busca una componente de desplazamiento o distancia recorrida. Cuando la velocidad cambia de signo, el cálculo del recorrido se divide en intervalos de signo conocido.

La división es una técnica de cálculo, no una hipótesis adicional del teorema. Proposición 7.4 también vale si los ceros son numerosos y no hay una partición finita cómoda; lo que puede fallar es un procedimiento particular para evaluar la integral.

En la notación normalizada de §1, si $u_\alpha=(\alpha-t_0)/T$ y $u_\beta=(\beta-t_0)/T$, el cambio de variable $t=t_0+Tu$ da $$\Delta x=L\int_{u_\alpha}^{u_\beta}V(u)\,du,\qquad d_{\mathrm{rec}}=L\int_{u_\alpha}^{u_\beta}|V(u)|\,du.$$ El factor $T$ de $dt$ cancela el denominador temporal de $v=(L/T)V$. Una integral adimensional de $V$ no debe presentarse directamente como metros.

[]{#un-regreso-que-no-cancela-todo}

### Un regreso que no cancela todo {#fispm-c07-un-regreso-que-no-cancela-todo}

Para $V(u)=1-u$ en $[0,3]$, la contribución positiva entre $0$ y $1$ es $1/2$; el módulo de la contribución negativa entre $1$ y $3$ es $2$. Así, $\Delta x=-3L/2$ y $d_{\mathrm{rec}}=5L/2$. El móvil termina del lado negativo respecto de su posición inicial, pero recorrió también un tramo en el sentido positivo. El exceso de recorrido sobre $|\Delta x|$ registra esa ida que luego fue deshecha.

[]{#ejercicios-4}

### Ejercicios {#fispm-c07-ejercicios-4}

[]{#fispm-t1-c07-e0009}

**Ejercicio 7.9.** Una historia tiene $V(u)=2-u$ en $[0,4]$. Calcula su desplazamiento y distancia recorrida. Explica el papel del cero de velocidad en el cálculo.

**Solución.** El único cero es $u=2$. La velocidad es positiva antes y negativa después; dividir allí permite escribir correctamente su módulo. Una primitiva de $2-u$ es $2u-u^2/2$, y por tanto $$\Delta x=L[2u-u^2/2]_0^4=0.$$ La contribución positiva vale $\int_0^2(2-u)\,du=2$. En el segundo tramo, $\int_2^4(2-u)\,du=-2$. Para el recorrido se suma el módulo de ambas contribuciones: $$d_{\mathrm{rec}}=L(2+2)=4L.$$ El vector desplazamiento es nulo. Se recorrieron $2L$ en cada sentido, de modo que no hubo reposo durante toda la historia. El cero de velocidad señala la división entre los dos tramos, no una pérdida de la distancia acumulada.

[]{#fispm-t1-c07-e0010}

**Ejercicio 7.10.** Reconstruye la condición de igualdad de la proposición 7.4 separando las contribuciones positivas y negativas. Aplícala a $V(u)=u^2$ en $[-1,1]$ y explica por qué un cero de velocidad no impide la igualdad.

**Solución.** Sean $v_+(t)=\max\{v(t),0\}$ y $v_-(t)=\max\{-v(t),0\}$. Son continuas, no negativas, y satisfacen $v=v_+-v_-$ y $|v|=v_++v_-$. Definamos $J_+=\int_\alpha^\beta v_+$ y $J_-=\int_\alpha^\beta v_-$. Entonces $\Delta x=J_+-J_-$ y $d_{\mathrm{rec}}=J_++J_-$. Si $J_+\ge J_-$, la diferencia $d_{\mathrm{rec}}-|\Delta x|$ es $2J_-$. Si $J_- > J_+$, es $2J_+$. En conjunto, $$d_{\mathrm{rec}}-|\Delta x|=2\min\{J_+,J_-\}.$$ La igualdad requiere $J_+=0$ o $J_-=0$. Una función continua no negativa con integral cero es idénticamente cero, como se justificó en la proposición 7.4. La primera alternativa implica $v\le0$; la segunda, $v\ge0$. Esto prueba ambas direcciones del criterio.

Para $V=u^2$, no hay contribución negativa y $\int_{-1}^1u^2\,du=2/3$. Por las escalas de §1, $\Delta x=d_{\mathrm{rec}}=2L/3$. La velocidad se anula en cero, pero mantiene el signo no negativo: no aparece ningún recorrido de vuelta que deba cancelarse.

Las integrales de esta sección determinan diferencias de posición. Para determinar una posición concreta falta saber dónde comienza la historia.

[]{#reconstruir-posición-desde-velocidad}

[]{#fispm-t1-c07-s06}

[]{#fpm-i-07-s06}

## 6. Reconstruir posición desde velocidad {#fispm-c07-reconstruir-posiciuxf3n-desde-velocidad}

Dos móviles separados sobre un riel pueden tener la misma velocidad en cada instante. Si sus gráficas de velocidad coinciden, ambos acumulan el mismo desplazamiento entre dos tiempos, pero eso no obliga a que ocupen la misma posición. Integrar la velocidad selecciona diferencias; una posición conocida fija la referencia que falta.

La dificultad aparece incluso con una velocidad constante de $1\,\mathrm{m/s}$. Las leyes $x_1(t)=t\,\mathrm{m/s}$ y $x_2(t)=5\,\mathrm m+t\,\mathrm{m/s}$, con $t$ medido como magnitud temporal, tienen la misma derivada. El sumando de longitud desaparece al derivar y reaparece como información que la velocidad no proporciona.

[]{#el-dato-que-selecciona-una-historia}

### El dato que selecciona una historia {#fispm-c07-el-dato-que-selecciona-una-historia}

[]{#fispm-t1-c07-d0004}

**Definición 7.4 --- Datos iniciales de una reconstrucción cinemática.** Fijado un instante $t_0$ del dominio, una posición inicial es una condición $x(t_0)=x_0$. Si la reconstrucción prescribe aceleración, se considera además una velocidad inicial $v(t_0)=v_0$. Los valores $x_0,v_0$ se refieren al mismo marco fijo, orientación y reloj que las funciones temporales.

«Inicial» designa aquí el instante de referencia de los datos. No obliga a que $t_0$ sea el primer instante del intervalo ni a que su valor numérico sea cero. Para reconstruir desde velocidad se necesita $x_0$; desde aceleración necesitaremos también $v_0$. Cada afirmación requiere demostrar que esos datos bastan.

Sea $I=[\alpha,\beta]$, con $\alpha<\beta$, y $t_0\in I$. Si $v$ es continua, podemos acumular su integral desde $t_0$ hasta cualquier $t\in I$. Para $t<t_0$ usamos la integral orientada, $\int_{t_0}^t v=-\int_t^{t_0}v$. El signo de esa inversión de límites es independiente del signo que pueda tener la velocidad.

[]{#fispm-t1-c07-p0005}

**Proposición 7.5 --- Reconstrucción única desde velocidad continua.** Dados $v\in C(I)$ y $x_0\in\mathbb R$, existe una única función $x\in C^1(I)$ tal que $x'=v$ y $x(t_0)=x_0$. Es $$x(t)=x_0+\int_{t_0}^t v(s)\,ds,\qquad t\in I.$$ Las derivadas en los extremos se interpretan con la convención lateral de §5.

**Demostración.** Definimos $x$ por la fórmula. La continuidad de $v$ permite aplicar el teorema fundamental: la función integral es de clase $C^1$ y su derivada es $v(t)$. Además, $\int_{t_0}^{t_0}v=0$, luego $x(t_0)=x_0$. Esto prueba existencia y regularidad.

Para unicidad, sean $x_1,x_2$ dos funciones que cumplen las condiciones y escribamos $z=x_1-x_2$. Entonces $z'=0$ y $z(t_0)=0$. Para cualquier $t\ne t_0$, el valor medio sobre el intervalo entre $t$ y $t_0$ da $z(t)-z(t_0)=z'(c)(t-t_0)=0$ para algún $c$ entre ellos. Por tanto, $z(t)=0$ para todo $t\in I$. $\square$

La prueba tiene dos obligaciones distintas. Integrar construye una candidata y verificar su derivada demuestra que funciona; comparar dos candidatas demuestra que no existe otra. Una fórmula comprobada, por sí sola, no habría probado unicidad.

La hipótesis de continuidad garantiza una posición $C^1$. Una función meramente integrable admite una función integral, pero no necesariamente una derivada clásica igual al dato en cada punto. Esa ampliación exige otros enunciados y no se atribuye a proposición 7.5.

[]{#una-primitiva-no-es-todavía-una-posición-seleccionada}

### Una primitiva no es todavía una posición seleccionada {#fispm-c07-una-primitiva-no-es-todavuxeda-una-posiciuxf3n-seleccionada}

Si $F'=v$ en $I$, proposición 7.5 puede escribirse como $x(t)=F(t)+x_0-F(t_0)$. El valor $F(t_0)$ no debe omitirse salvo que sea cero. La familia $F+C$ reúne todas las posiciones con esa velocidad; el dato inicial fija $C=x_0-F(t_0)$.

Por ejemplo, consideremos $V(u)=u$ en $[-1,2]$ y el dato $X(1)=3$. Una primitiva es $u^2/2$. La historia seleccionada es $X(u)=3+\int_1^u q\,dq=(5+u^2)/2$. Derivar confirma $X'=u$ y evaluar en $1$ confirma $X=3$. Elegir $X=3+u^2/2$ conservaría la velocidad, pero daría $X(1)=7/2$: añadir el valor inicial a una primitiva arbitraria no es una regla válida.

En términos de gráficas, la velocidad fija las pendientes de la gráfica de posición. Cambiar la constante desplaza verticalmente esa gráfica y, en el riel, traslada todas las posiciones por la misma cantidad fija. Conserva velocidades y desplazamientos, no los puntos ocupados.

El procedimiento de reconstrucción por integrales se coteja con Kleppner y Kolenkow, *An Introduction to Mechanics*, copia Cambridge 2010, cap. 1 §1.7, pp. 19--21. Aquí la existencia y unicidad se justifican con resultados de una variable y aceleración no interviene aún.

[]{#ejercicios-5}

### Ejercicios {#fispm-c07-ejercicios-5}

[]{#fispm-t1-c07-e0011}

**Ejercicio 7.11.** Para $V(u)=1+2u$ en $[0,2]$ y $X(0)=-1$, reconstruye la coordenada normalizada. Verifica velocidad y dato inicial, y recupera la posición física.

**Solución.** Usando $q$ como variable de integración para distinguirla del límite $u$, $$X(u)=-1+\int_0^u(1+2q)\,dq=-1+u+u^2.$$ La derivada es $X'(u)=1+2u=V(u)$ y $X(0)=-1$. Las escalas de §1 dan $x(t)=L(-1+u+u^2)$, $u=(t-t_0)/T$, en $[t_0,t_0+2T]$. Así $x(t_0)=-L$ y $x'(t)=(L/T)(1+2u)$, la velocidad física prescrita.

Proposición 7.5 asegura que no hay otra historia $C^1$ con esos datos. El término $-1$ fija la posición; los términos dependientes del tiempo acumulan su cambio.

[]{#fispm-t1-c07-e0012}

**Ejercicio 7.12.** En un intervalo no degenerado que contiene $0$, describe todas las historias con $V(u)=3u^2-1$. Demuestra qué cambia al imponer $X(0)=2$.

**Solución.** Una primitiva es $F(u)=u^3-u$. Si $X'=V$, la diferencia $X-F$ tiene derivada cero. El valor medio sobre cualquier subintervalo entre dos puntos demuestra que esa diferencia es constante. Por tanto, todas las historias, y no sólo algunas candidatas, son $X(u)=u^3-u+C$, con $C\in\mathbb R$.

Como $F(0)=0$, la condición $X(0)=2$ obliga a $C=2$. La historia única es $X=u^3-u+2$. Cambiar $C$ desplaza la posición física por una longitud $L\Delta C$; no cambia $V$, sus ceros ni el desplazamiento entre dos tiempos. Sin el dato de posición quedaba una familia entera de historias posibles.

La reconstrucción desde velocidad queda determinada por un solo valor de posición. Cuando el dato sea aceleración, la primera integral reconstruirá una velocidad y habrá que seleccionar también esa primera constante.

[]{#reconstruir-movimiento-desde-aceleración}

[]{#fispm-t1-c07-s07}

[]{#fpm-i-07-s07}

## 7. Reconstruir movimiento desde aceleración {#fispm-c07-reconstruir-movimiento-desde-aceleraciuxf3n}

Una gráfica de aceleración informa cuánto cambia la velocidad entre dos instantes. No indica por sí sola qué velocidad tenía el móvil al comienzo, ni dónde estaba. Un mismo cambio de velocidad puede superponerse a velocidades iniciales distintas; incluso después de seleccionar la velocidad, queda la libertad de trasladar la posición.

La reconstrucción sigue las dos relaciones ya establecidas: $v'=a$ y $x'=v$. Integramos primero el dato de aceleración para obtener velocidad y después la velocidad para obtener posición. Ambas operaciones son integrales de una variable. La segunda no autoriza a olvidar la constante que apareció en la primera.

[]{#dos-integraciones-con-datos-en-un-mismo-instante}

### Dos integraciones con datos en un mismo instante {#fispm-c07-dos-integraciones-con-datos-en-un-mismo-instante}

Sea $I=[\alpha,\beta]$, con $\alpha<\beta$, y $t_0\in I$. La regularidad que adoptamos para el dato es $a\in C(I)$. La velocidad construida será $C^1$ y la posición será $C^2$, con derivadas laterales en extremos según la convención de §5.

[]{#fispm-t1-c07-p0006}

**Proposición 7.6 --- Reconstrucción única desde aceleración continua.** Dados $a\in C(I)$ y dos valores $x_0,v_0\in\mathbb R$, existe una única historia $x\in C^2(I)$ tal que $x''=a$, $x(t_0)=x_0$ y $x'(t_0)=v_0$. Su velocidad y posición son $$v(t)=v_0+\int_{t_0}^t a(s)\,ds$$ y $$x(t)=x_0+\int_{t_0}^t v(q)\,dq =x_0+v_0(t-t_0)+\int_{t_0}^t\left(\int_{t_0}^q a(s)\,ds\right)dq.$$

Antes de demostrarla, se pueden leer las tres contribuciones de la última fórmula. $x_0$ fija una posición, $v_0(t-t_0)$ acumula el aporte de la velocidad inicial y la integral iterada acumula el cambio producido por el dato de aceleración. La variable $q$ recorre los tiempos de la segunda integración; $s$ recorre los de la primera. Las dos letras evitan confundir un límite variable con la variable que se integra.

**Demostración.** Aplicamos proposición 7.5 a la función continua $a$, interpretándola como derivada de $v$, y al dato $v(t_0)=v_0$. Obtenemos una única función $v\in C^1(I)$ con $v'=a$. Aplicamos proposición 7.5 de nuevo, ahora a esta velocidad y a $x(t_0)=x_0$. Se obtiene una única $x\in C^1(I)$ con $x'=v$. Como $v$ es $C^1$, esa posición es $C^2$ y $x''=a$. Sustituir la expresión de $v$ en su integral y separar el término constante produce la fórmula iterada.

Para comprobar la unicidad dentro de la clase anunciada, sea $y\in C^2(I)$ otra candidata. Las funciones $y'$ y $v$ tienen la misma derivada $a$ y el mismo valor $v_0$ en $t_0$; la unicidad de la primera aplicación de la proposición 7.5 implica $y'=v$. Las funciones $y$ y $x$ tienen entonces la misma derivada $v$ y el mismo valor $x_0$ en $t_0$; la segunda aplicación implica $y=x$. $\square$

No intercambiamos el orden de las integraciones ni usamos un teorema de integración multivariable. El intervalo hasta $q$ pertenece al dominio original porque $I$ es un intervalo. Si $t<t_0$, ambas integrales se interpretan con sus límites orientados.

Las unidades también se acumulan por etapas. La integral de aceleración tiene tipo $(L/T^2)T=L/T$ y puede sumarse a $v_0$. Integrar esa velocidad produce longitud. En las convenciones de §1, con referencia inicial $u=0$, las mismas relaciones son $$V(u)=V_0+\int_0^u A(s)\,ds,\qquad X(u)=X_0+\int_0^u V(q)\,dq,$$ donde $v_0=(L/T)V_0$ y $x_0=LX_0$ si $x_*=0$.

[]{#qué-se-pierde-al-omitir-un-dato}

### Qué se pierde al omitir un dato {#fispm-c07-quuxe9-se-pierde-al-omitir-un-dato}

Si $x$ es una historia con aceleración $a$, las funciones $$y(t)=x(t)+c+b(t-t_0)$$ tienen la misma aceleración, para cualesquiera constantes $c$ de longitud y $b$ de velocidad. Su posición inicial cambia en $c$ y su velocidad inicial en $b$. Recíprocamente, si $y''=x''$, el valor medio aplicado primero a $y'-x'$ muestra que esa diferencia es una constante $b$; aplicado después a $y-x-b(t-t_0)$ muestra que la diferencia restante es una constante $c$. Ésa es toda la libertad disponible, no sólo una familia de ejemplos.

Fijar $x_0$ elimina $c$, pero deja $b$. Fijar únicamente $v_0$ elimina $b$, pero permite una traslación de posición. La aceleración y ambos datos, tomados en un mismo instante, eliminan las dos libertades.

[]{#fispm-t1-c07-mp0006}

**Principio metodológico 7.6 --- Cerrar la reconstrucción con los datos iniciales necesarios.** Al integrar una aceleración prescrita, se deben seleccionar tanto la velocidad inicial como la posición inicial. Una familia de primitivas no es una historia física determinada. Cada dato se verifica en el instante donde fue impuesto.

Esta lectura de las constantes concuerda con Shankar, *Fundamentals of Physics I*, edición ampliada de 2019, cap. 1 §1.4, pp. 6--8, y con Kleppner--Kolenkow, copia Cambridge 2010, cap. 1 §1.7, pp. 19--21. Aquí el argumento vale para aceleración continua variable; no utiliza la hipótesis de aceleración constante de algunos pasajes de esas obras.

[]{#un-dato-de-aceleración-variable}

### Un dato de aceleración variable {#fispm-c07-un-dato-de-aceleraciuxf3n-variable}

Consideremos $A(u)=1-u$ en $[0,2]$, con $V(0)=2$ y $X(0)=-1$. Integrar primero da $V(u)=2+u-u^2/2$. Integrar esa función da $X(u)=-1+2u+u^2/2-u^3/6$. Las derivadas $X'=V$ y $V'=A$ verifican la reconstrucción, junto con los dos datos en cero.

La gráfica de aceleración cruza el eje en $u=1$. Allí la velocidad pasa de crecer a decrecer, pero no se anula: $V(1)=5/2$. Un cero de aceleración no es un reposo instantáneo. La reconstrucción deja visible por qué esa información no podía obtenerse de la altura de $A$ sin conocer también la velocidad inicial.

[]{#ejercicios-6}

### Ejercicios {#fispm-c07-ejercicios-6}

[]{#fispm-t1-c07-e0013}

**Ejercicio 7.13.** Para $A(u)=2u$ en $[0,2]$, con $V(0)=-1$ y $X(0)=0$, reconstruye velocidad y posición. Verifica los datos y determina si el móvil cambia de sentido dentro del intervalo.

**Solución.** La primera integración debe conservar la velocidad inicial: $$V(u)=-1+\int_0^u2s\,ds=-1+u^2.$$ La segunda debe conservar la posición inicial: $$X(u)=\int_0^u(-1+q^2)\,dq=-u+\frac{u^3}{3}.$$ Se comprueba $X'=V$, $V'=2u=A$, $X(0)=0$ y $V(0)=-1$. En magnitudes físicas, $x=L(-u+u^3/3)$, $v=(L/T)(-1+u^2)$ y $a=(L/T^2)2u$.

El único cero de $V$ en el dominio es $u=1$. La componente es negativa en $[0,1)$ y positiva en $(1,2]$, por lo que definición 7.3 certifica una inversión local. La posición alcanza allí un mínimo, $X(1)=-2/3$. La aceleración es positiva en ese instante y durante el movimiento posterior; ese signo se interpreta junto al de la velocidad, como en §4.

[]{#fispm-t1-c07-e0014}

**Ejercicio 7.14.** En un intervalo no degenerado que contiene $0$, compara la información de $A\equiv0$ sola, de $A\equiv0$ más $X(0)=X_0$, y de esos datos más $V(0)=V_0$. Describe todas las historias compatibles y justifica la cantidad de información que falta.

**Solución.** Si $A=V'=0$, el valor medio implica que $V$ es una constante $c_1$. Integrar $X'=c_1$, o aplicar proposición 7.5, da $X(u)=c_0+c_1u$. Por tanto, la aceleración sola deja dos constantes independientes. Por ejemplo, $X=0$, $X=1$ y $X=u$ cumplen $A=0$ y son historias diferentes.

La posición en cero es $c_0$, de modo que $X(0)=X_0$ fija $c_0=X_0$ pero permite cualquier $c_1$. Todas esas historias pasan por la misma posición al inicio y pueden tener velocidades distintas. Finalmente, $V(0)=V_0$ fija $c_1=V_0$. La única historia es $X=X_0+V_0u$, con velocidad física $(L/T)V_0$.

La prueba mediante valor medio muestra que no quedan soluciones adicionales fuera de la familia afín dentro de la regularidad considerada. Tampoco afirma por qué la aceleración es cero: ese dato fue prescrito.

Las dos constantes que seleccionan una historia tienen significados diferentes y comprobables. Cuando la velocidad no varía, esa reconstrucción adopta la forma afín que acabamos de obtener.

[]{#movimiento-uniforme}

[]{#fispm-t1-c07-s08}

[]{#fpm-i-07-s08}

## 8. Movimiento uniforme {#fispm-c07-movimiento-uniforme}

Un registro muestra que la coordenada de un móvil aumenta la misma cantidad en cada segundo. Otro muestra que disminuye la misma cantidad. Ambos pueden describirse mediante una velocidad constante; el signo distingue el sentido y el módulo fija cuánto recorrido se acumula por unidad de tiempo. Si la cantidad por segundo es cero, la misma familia incluye el reposo.

Hay que distinguir una hipótesis válida durante un intervalo de una coincidencia entre unas pocas observaciones. Dos posiciones siempre permiten calcular una velocidad media; no demuestran que esa velocidad se mantuviera entre ellas.

[]{#la-condición-y-su-ley-temporal}

### La condición y su ley temporal {#fispm-c07-la-condiciuxf3n-y-su-ley-temporal}

[]{#fispm-t1-c07-d0005}

**Definición 7.5 --- Movimiento uniforme, incluido el reposo.** Una historia rectilínea $x\in C^1(I)$, sobre un intervalo temporal no degenerado y en la representación fija de §1, es uniforme si existe una constante $v_0$ tal que $v(t)=v_0$ en todo $I$. Si $v_0=0$, la historia es de reposo.

La definición fija una componente constante respecto de una orientación fija. No se define el movimiento uniforme mediante una velocidad media ni sólo mediante rapidez constante. El reposo es el caso cero de la misma condición, no una excepción a sus fórmulas.

[]{#fispm-t1-c07-p0007}

**Proposición 7.7 --- Caracterización del movimiento uniforme.** Sea $x\in C^1(I)$ y $t_0\in I$, con $x_0=x(t_0)$. La historia es uniforme con componente $v_0$ si y sólo si $$x(t)=x_0+v_0(t-t_0)\qquad\text{para todo }t\in I.$$ Si además $x\in C^2(I)$, el movimiento es uniforme si y sólo si $a(t)=0$ en todo el intervalo.

**Demostración.** En $t=t_0$, la igualdad de posición es el dato $x(t_0)=x_0$. Si $v=v_0$ y $t\ne t_0$, el intervalo cerrado entre ambos instantes es no degenerado y está contenido en $I$; proposición 7.5 da $$x(t)=x_0+\int_{t_0}^t v_0\,ds=x_0+v_0(t-t_0).$$ El resultado se conserva para $t<t_0$ por la orientación de la integral. Recíprocamente, derivar la ley afín da $x'=v_0$, que es la condición de la definición 7.5.

Bajo la regularidad $C^2$, una velocidad constante tiene derivada $a=0$. Para la conversa, si $a=v'=0$, el valor medio aplicado a $v$ entre dos instantes cualesquiera da igualdad de sus valores. Así $v$ es constante en $I$. $\square$

Cada dirección tiene una tarea propia: la integral produce la ley a partir de la condición; la derivada recupera la condición a partir de la ley. Una aceleración nula no obliga a posición constante: permite cualquier velocidad constante. El reposo requiere además que el valor seleccionado de esa velocidad sea cero.

[]{#representaciones-de-la-misma-historia}

### Representaciones de la misma historia {#fispm-c07-representaciones-de-la-misma-historia}

Para un movimiento uniforme, la gráfica temporal de posición es un segmento de recta o parte de una recta, según el dominio; la gráfica de velocidad es horizontal y la de aceleración, cuando se considera, está sobre el eje temporal. Esas gráficas se relacionan mediante derivadas, aunque sus alturas representen magnitudes diferentes.

Para $s<t$ en $I$, proposición 7.4 y proposición 7.7 dan $$\Delta x=v_0(t-s),\qquad d_{\mathrm{rec}}=|v_0|(t-s).$$ La distancia entre las posiciones extremas coincide con el recorrido porque no hay aportes de signos opuestos. Las cantidades son cero si $v_0=0$.

Por ejemplo, en $[0,4\,\mathrm s]$, la ley $x(t)=3\,\mathrm m-(2\,\mathrm{m/s})t$ representa movimiento uniforme hacia coordenadas menores. Entre los extremos, el desplazamiento tiene componente $-8\,\mathrm m$ y el recorrido es $8\,\mathrm m$. En cambio, $x(t)=3\,\mathrm m$ sobre el mismo intervalo representa reposo y produce cero en ambas cantidades. La pendiente horizontal de esta última gráfica de posición se distingue de la gráfica horizontal de velocidad del primer caso.

[]{#seleccionar-una-ley-no-verifica-la-hipótesis}

### Seleccionar una ley no verifica la hipótesis {#fispm-c07-seleccionar-una-ley-no-verifica-la-hipuxf3tesis}

Si se sabe de antemano que una historia es uniforme y se conocen $x(t_1)=x_1$, $x(t_2)=x_2$ para $t_1<t_2$, proposición 7.7 obliga a $$v_0=\frac{x_2-x_1}{t_2-t_1},\qquad x(t)=x_1+v_0(t-t_1).$$ Dentro de esa familia hay una historia única. Sin la hipótesis de uniformidad, el cociente sigue siendo una velocidad media, pero deja abierta la forma de la función entre las observaciones.

La condición cinemática tampoco determina una causa física. No hemos deducido una ley de inercia ni identificado fuerzas: describimos la consecuencia de prescribir una velocidad constante. La reconstrucción integral utilizada se coteja con Kleppner--Kolenkow, copia Cambridge 2010, cap. 1 §1.7, pp. 19--21; el caso constante es una especialización de esa operación.

**Ejercicio.**

[]{#fispm-t1-c07-e0015}

**Ejercicio 7.15.** Una historia suave sobre $[0,1]$ satisface $X(0)=0$ y $X(1)=1$. Decide si los datos prueban movimiento uniforme. Construye una historia uniforme y una familia de historias no uniformes compatibles con ellos.

**Solución.** La ley $X_{\mathrm{unif}}(u)=u$ cumple ambos datos y tiene $V=1$ constante. Para construir alternativas, necesitamos un término que se anule en los dos tiempos observados. El producto $u(1-u)$ cumple esa condición. Por tanto, para cada constante adimensional $c\ne0$, $$X_c(u)=u+c\,u(1-u)$$ conserva $X_c(0)=0$ y $X_c(1)=1$, pero su velocidad es $V_c(u)=1+c(1-2u)$. Esa función no es constante porque $V_c'=-2c\ne0$. Todas las historias son polinomiales y suaves, de modo que la falta de uniformidad no depende de irregularidades ocultas.

La velocidad media normalizada entre los extremos es $1$ en todos los casos; la física es $L/T$. Por ejemplo, para $c=1/2$, la componente normalizada pasa de $3/2$ a $1/2$ y permanece positiva: puede fallar la uniformidad incluso sin un regreso. Las dos observaciones no controlan las velocidades intermedias.

Si se añade la hipótesis de la definición 7.5, proposición 7.7 obliga a una ley $X=X_0+V_0u$. Los datos fijan $X_0=0$ y $V_0=1$, seleccionando $X=u$. La conclusión de unicidad es relativa a esa clase declarada; no convierte dos muestras en una demostración de la hipótesis física.

El movimiento uniforme queda caracterizado por una condición temporal, una ley afín y un criterio de aceleración nula bajo regularidad suficiente. La reconstrucción permite probar esas equivalencias y mantener separado lo que se supone durante el intervalo de lo que muestran sus extremos.

[]{#aceleración-constante}

[]{#fispm-t1-c07-s09}

[]{#fpm-i-07-s09}

## 9. Aceleración constante {#fispm-c07-aceleraciuxf3n-constante}

Un móvil puede aumentar su componente de velocidad en la misma cantidad durante cada segundo, o disminuirla a un ritmo constante. La condición se refiere al cambio de velocidad, no al cambio de posición. Si se conoce además una posición y una velocidad en un instante, las dos integraciones de §7 seleccionan una historia cuadrática.

[]{#fig:I-07-N01}

<figure id="fig-fpm-v04-i-07-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-07-N01.svg" class="lightbox" data-gallery="fpm-v04-c07"><img src="/assets/books/fispm/v04/I-07-N01.svg" alt="Tres lecturas de una historia. Diagrama del capítulo 7; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="404" height="252" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 7.2.** Para $X=u^2/2$ en $0\le u\le2$, la línea continua representa $X$, la discontinua $V=u$ y la punteada $A=1$. Son magnitudes normalizadas distintas, ligadas por derivación. Véase §[9](#fispm-c07-aceleraciuxf3n-constante).

</figcaption>

</figure>

Esa forma temporal es una consecuencia de la aceleración prescrita. No explica qué la produce ni garantiza que el dato constante continúe siendo válido fuera del intervalo considerado. Mantendremos separados el cálculo bajo la hipótesis y el dominio donde se adopta esa hipótesis.

[]{#de-la-condición-a-las-leyes-temporales}

### De la condición a las leyes temporales {#fispm-c07-de-la-condiciuxf3n-a-las-leyes-temporales}

[]{#fispm-t1-c07-d0006}

**Definición 7.6 --- Movimiento de aceleración constante.** Una historia rectilínea $x\in C^2(I)$, en la representación fija de §1 y sobre un intervalo no degenerado $I$, tiene aceleración constante si existe una constante $a_0$ tal que $x''(t)=a_0$ para todo $t\in I$. Para seleccionar una historia se prescriben $x(t_0)=x_0$ y $x'(t_0)=v_0$ en un mismo $t_0\in I$.

El caso $a_0=0$ está incluido y corresponde a la familia uniforme de §8. Si $a_0\ne0$, la velocidad varía, pero su signo depende también de $v_0$ y del tiempo. Aceleración constante no significa rapidez creciente durante toda la historia.

[]{#fispm-t1-c07-p0008}

**Proposición 7.8 --- Leyes de aceleración constante e identidad sin tiempo.** Bajo definición 7.6 y sus datos iniciales, la historia única satisface, para todo $t\in I$, $$v(t)=v_0+a_0(t-t_0),\qquad x(t)=x_0+v_0(t-t_0)+\frac{a_0}{2}(t-t_0)^2.$$ También se cumple $$v(t)^2-v_0^2=2a_0\bigl(x(t)-x_0\bigr),$$ incluido el caso $a_0=0$. La diferencia de posición es desplazamiento firmado, no distancia recorrida.

**Demostración.** En $t=t_0$, las dos leyes temporales recuperan los datos iniciales. Para $t\ne t_0$, el intervalo cerrado entre ambos instantes es no degenerado y está contenido en $I$; proposición 7.6 da $$v(t)=v_0+\int_{t_0}^t a_0\,ds=v_0+a_0(t-t_0).$$ Integrar esa velocidad produce $$x(t)=x_0+\int_{t_0}^t\bigl(v_0+a_0(q-t_0)\bigr)\,dq =x_0+v_0(t-t_0)+\frac{a_0}{2}(t-t_0)^2.$$ La unicidad es la ya probada en la proposición 7.6. Para la identidad, escribamos $h=t-t_0$. Al expandir el cuadrado se obtiene $$(v_0+a_0h)^2-v_0^2=2a_0v_0h+a_0^2h^2 =2a_0\left(v_0h+\frac{a_0}{2}h^2\right).$$ El último paréntesis es $x(t)-x_0$. No se ha dividido por $a_0$ ni por la velocidad, de modo que el argumento conserva sus ceros. $\square$

La identidad relaciona valores tomados en un mismo instante. Al elevar al cuadrado se pierde información de signo: un valor de $v^2$ no permite decidir por sí solo entre dos componentes opuestas. Las leyes temporales conservan esa información y permiten filtrar cuál ocurre en el dominio de la historia.

Las unidades de cada término de posición son longitud: $v_0(t-t_0)$ y $a_0(t-t_0)^2/2$ pueden sumarse a $x_0$. En la identidad, ambos miembros tienen tipo $L^2/T^2$. El análisis dimensional controla la coherencia, pero no demuestra la fórmula.

[]{#inversión-recorrido-y-dominio}

### Inversión, recorrido y dominio {#fispm-c07-inversiuxf3n-recorrido-y-dominio}

Para $a_0\ne0$, la única candidata a un cero de velocidad es $t_c=t_0-v_0/a_0$. Si está en el interior de $I$, la función afín $v$ tiene signos opuestos a ambos lados y definición 7.3 certifica una inversión. Si cae fuera del dominio, la historia declarada no contiene ese evento. Un cero en un extremo no proporciona por sí solo los dos semientornos que exige definición 7.3.

Por ejemplo, $X(u)=4-u+u^2/2$ en $[0,3]$ tiene $V=-1+u$ y $A=1$. Antes de $u=1$, la componente negativa aumenta hacia cero y la rapidez disminuye. Después, la componente y la rapidez aumentan. La aceleración positiva no cambia en el proceso; cambia su relación con el signo de la velocidad.

Para evaluar distancia se vuelve a proposición 7.4 y se integra $|v|$, separando en las inversiones que pertenezcan al dominio. Sustituir distancia por desplazamiento en la identidad cuadrática puede dar una respuesta incorrecta cuando hay regreso.

[]{#fispm-t1-c07-mp0007}

**Principio metodológico 7.7 --- Usar las fórmulas sólo en el dominio de la hipótesis.** Las leyes de la proposición 7.8 se aplican en el intervalo donde se prescribe aceleración constante y con los datos iniciales que las seleccionan. La posibilidad algebraica de evaluar un polinomio fuera de ese intervalo no autoriza a prolongar la historia física.

El control de estas fórmulas se coteja con Shankar, *Fundamentals of Physics I*, edición ampliada de 2019, cap. 1 §1.4, pp. 6--10, y Kleppner--Kolenkow, copia Cambridge 2010, cap. 1 §1.7, p. 21. La demostración propia conserva aceleración cero y el carácter firmado del desplazamiento.

[]{#ejercicios-7}

### Ejercicios {#fispm-c07-ejercicios-7}

[]{#fispm-t1-c07-e0016}

**Ejercicio 7.16.** En $[0,5]$ se prescribe $A=-1$, con $X(0)=1$ y $V(0)=2$. Calcula posición, velocidad, inversión, desplazamiento y distancia recorrida entre los extremos.

**Solución.** Integrar con ambos datos da $V(u)=2-u$ y $X(u)=1+2u-u^2/2$. El cero $u=2$ es interior; el signo pasa de positivo a negativo y hay inversión. Allí $X(2)=3$. En el extremo final, $X(5)=-3/2$, de modo que $\Delta x=L(-3/2-1)=-5L/2$.

El recorrido anterior a la inversión es $L(X(2)-X(0))=2L$. Después se recorren $L(X(2)-X(5))=9L/2$. Por tanto, $d_{\mathrm{rec}}=13L/2$, mayor que $|\Delta x|=5L/2$. Las componentes físicas son $v=(L/T)(2-u)$ y $a=-L/T^2$; la posición es $x=LX$. El cálculo verifica también $X'=V$ y $V'=A$.

[]{#fispm-t1-c07-e0017}

**Ejercicio 7.17.** Demuestra la identidad $V^2-V_0^2=2A_0(X-X_0)$ desde las leyes temporales normalizadas. Trata $A_0=0$ y explica qué información no recupera la identidad por sí sola.

**Solución.** Sea $h=u-u_0$ la diferencia respecto del instante normalizado de los datos. Las leyes son $V=V_0+A_0h$ y $X-X_0=V_0h+A_0h^2/2$. Entonces $$V^2-V_0^2=2V_0A_0h+A_0^2h^2 =2A_0(X-X_0).$$ Si $A_0=0$, ambos miembros valen cero; no aparece una división inválida. La identidad queda $V^2=V_0^2$ y no contiene $X$. Para reconstruir posición seguimos necesitando la ley temporal y el dato inicial. Si $A_0\ne0$, tampoco el cuadrado distingue las dos orientaciones posibles de velocidad.

El atajo $h=(V-V_0)/A_0$ sólo es admisible cuando $A_0\ne0$. La expansión trabaja directamente con las leyes y evita perder el caso cero.

[]{#fispm-t1-c07-e0018}

**Ejercicio 7.18.** Para $A(u)=u$ en $[0,2]$, con $V(0)=X(0)=0$, audita la propuesta $X_{\mathrm{pret}}(u)=A(u)u^2/2$. Reconstruye la historia correcta y calcula el residuo de aceleración de la propuesta.

**Solución.** La aceleración varía, por lo que proposición 7.8 no permite sustituir una constante por $A(u)$. Proposición 7.6 da $V(u)=\int_0^u s\,ds=u^2/2$ y $X(u)=\int_0^u q^2/2\,dq=u^3/6$. Ambas derivadas y ambos datos iniciales quedan verificados.

La propuesta es $X_{\mathrm{pret}}=u^3/2$, con segunda derivada $3u$. Su residuo respecto del dato prescrito es $R_A(u)=X_{\mathrm{pret}}''(u)-A(u)=2u$. Los datos iniciales de posición y velocidad sí son correctos, pero la aceleración falla en cada $u>0$. En unidades físicas, el residuo es $(L/T^2)2u$. Verificar dos datos no sustituye verificar la ley durante el intervalo.

La forma cuadrática queda vinculada a una hipótesis temporal concreta. Cuando esa hipótesis cambia en un instante conocido, cada tramo debe reconstruirse con los valores que hereda de su unión.

[]{#historias-definidas-por-tramos}

[]{#fispm-t1-c07-s10}

[]{#fpm-i-07-s10}

## 10. Historias definidas por tramos {#fispm-c07-historias-definidas-por-tramos}

Una descripción puede prescribir aceleración constante durante una parte del recorrido y otra aceleración después. Integrar cada expresión por separado produce fórmulas, pero todavía falta comprobar si representan una sola historia: al llegar al instante de cambio, ambas deben asignar la misma posición. Si además se pretende una velocidad clásica en ese instante, las pendientes también deben coincidir.

[]{#fig:I-07-R01}

<figure id="fig-fpm-v04-i-07-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-07-R01.svg" class="lightbox" data-gallery="fpm-v04-c07"><img src="/assets/books/fispm/v04/I-07-R01.svg" alt="Una velocidad continua con cambio de aceleración. Diagrama del capítulo 7; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="407" height="227" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 7.3.** La ley $v=1$ hasta $t=1$ y $v=2-t$ después es continua. La aceleración cambia de $0$ a $-1$ en el empalme y no tiene allí un valor clásico único. No hay salto de posición ni impulso requerido por un salto de velocidad. Véase §[10](#fispm-c07-historias-definidas-por-tramos).

</figcaption>

</figure>

Los valores finales de un tramo se convierten en datos del siguiente. Esa transferencia evita reiniciar artificialmente posición y reloj cada vez que cambia la fórmula.

[]{#una-función-construida-con-varios-intervalos}

### Una función construida con varios intervalos {#fispm-c07-una-funciuxf3n-construida-con-varios-intervalos}

[]{#fispm-t1-c07-d0007}

**Definición 7.7 --- Historia admisible por tramos.** Sea una partición finita $\alpha=\tau_0<\tau_1<\cdots<\tau_n=\beta$. Para cada $j$, sea $x_j\in C^1([\tau_{j-1},\tau_j])$, con la convención lateral en extremos. Si los valores coinciden en cada unión, $$x_j(\tau_j)=x_{j+1}(\tau_j)\qquad (1\le j<n),$$ las funciones definen una única historia continua $x$ sobre $[\alpha,\beta]$, que coincide con $x_j$ en cada tramo. Diremos que es admisible por tramos en este sentido. Cuando se necesite aceleración dentro de un tramo, se exigirá allí la diferenciabilidad adicional correspondiente, por ejemplo $x_j\in C^2$.

La coincidencia de valores hace que la ley sea inequívoca en los nodos $\tau_j$ y excluye saltos de posición. La definición no exige todavía que la historia completa sea $C^1$: admite pendientes laterales distintas. «Admisible» nombra esta clase cinemática declarada, sin afirmar que toda unión tenga una explicación dinámica dentro del modelo.

Una fórmula del segundo tramo suele escribirse con tiempo local $w=t-\tau_j$. El mismo reloj físico sigue vigente; $w=0$ identifica la unión. Cambiar la variable en una fórmula no pone a cero la posición ni la velocidad.

[]{#qué-exige-una-velocidad-en-la-unión}

### Qué exige una velocidad en la unión {#fispm-c07-quuxe9-exige-una-velocidad-en-la-uniuxf3n}

[]{#fispm-t1-c07-p0009}

**Proposición 7.9 --- Criterio de empalme $C^1$.** Bajo definición 7.7, la historia completa es de clase $C^1$ en $[\alpha,\beta]$ si y sólo si, en cada nodo interior, coinciden las derivadas de los dos tramos: $$x_j'(\tau_j)=x_{j+1}'(\tau_j)\qquad (1\le j<n).$$

**Demostración.** Fijemos un nodo $c=\tau_j$ y usemos el valor común de posición $x(c)$. Para $h>0$ suficientemente pequeño, el cociente $\bigl(x(c+h)-x(c)\bigr)/h$ pertenece al tramo derecho. Por el valor medio es $x_{j+1}'(\xi_h)$, con $\xi_h\in(c,c+h)$. La continuidad de la derivada hasta el extremo derecho de la unión da límite $x_{j+1}'(c)$ cuando $h\to0^+$. Para $h<0$, el argumento sobre el tramo izquierdo da límite $x_j'(c)$ cuando $h\to0^-$.

La derivada bilateral existe si y sólo si esos límites coinciden. Si coinciden en todos los nodos, la derivada global reúne las derivadas continuas de cada tramo y sus valores comunes; es continua también en las uniones. Así la historia es $C^1$. Recíprocamente, si la historia es $C^1$, su derivada en cada nodo coincide con ambas derivadas laterales, que por tanto son iguales. $\square$

La hipótesis de continuidad de las derivadas hasta los extremos de cada tramo permite identificar los límites de los cocientes. No se deduce el criterio sólo de mirar pendientes de un dibujo ni de asignar a mano un valor de velocidad en el nodo.

Conservar posición y velocidad tampoco asegura aceleración. Si cada tramo es $C^2$, para decidir si existe $x''(c)$ se revisan los cocientes de la velocidad a ambos lados. Límites laterales distintos impiden una aceleración clásica en ese instante, aunque posición y velocidad sean continuas.

[]{#fispm-t1-c07-mp0008}

**Principio metodológico 7.8 --- Auditar cada unión antes de atribuir una derivada.** En un nodo se comprueban primero valores de posición, después cocientes laterales de posición y, si corresponde, cocientes laterales de velocidad. Una fórmula por tramos no autoriza a usar sus derivadas interiores en el nodo sin ese control.

No se introduce una aceleración generalizada para reparar una esquina ni se interpreta un salto mediante impulsos. Si falta una derivada clásica, se declara su ausencia y se limita el uso de las fórmulas a los tramos donde esa derivada existe.

[]{#transferir-datos-en-lugar-de-reiniciar}

### Transferir datos en lugar de reiniciar {#fispm-c07-transferir-datos-en-lugar-de-reiniciar}

Consideremos, en tiempo normalizado, $X(u)=2+u$ para $0\le u\le1$. Al llegar a la unión, $X(1)=3$ y $V(1)=1$. Si el segundo tramo prescribe $A=2$, escribir $w=u-1$ y usar esos datos da $X=3+w+w^2$ y $V=1+2w$. La nueva fórmula conserva posición y velocidad en $w=0$. Elegir en cambio $X=w^2$ produciría un salto de posición; elegir $X=3+w^2$ conservaría posición, pero cambiaría la pendiente de $1$ a $0$.

La reconstrucción de la proposición 7.6 se aplica a cada tramo con sus propios datos. Si la aceleración tiene valores laterales distintos, cada extensión del dato hasta la unión pertenece a su tramo y no determina una aceleración global allí.

Para el recorrido, una historia $C^1$ ya está cubierta por la proposición 7.4. Si sólo es $C^1$ por tramos, se calcula la longitud de cada restricción y se suman sus contribuciones. Esta suma concuerda con la definición geométrica: añadir los nodos a una partición no acorta su longitud poligonal, y las particiones de cada tramo pueden reunirse en una partición del intervalo completo. No se aplica una fórmula que exija $C^1$ global sin verificar esa hipótesis.

[]{#ejercicios-8}

### Ejercicios {#fispm-c07-ejercicios-8}

[]{#fispm-t1-c07-e0019}

**Ejercicio 7.19.** En $[0,2]$, sea $X(u)=u^2$ para $u\le1$ y $X(u)=1+2(u-1)+3(u-1)^2$ para $u\ge1$. Audita continuidad, velocidad y aceleración en la unión.

**Solución.** Ambas expresiones dan $X(1)=1$. Las derivadas de los tramos son $2u$ y $2+6(u-1)$; sus valores laterales en $1$ son ambos $2$. Proposición 7.9 implica que $X$ es $C^1$ y que $V(1)=2$.

Para la aceleración, las derivadas de velocidad en los dos tramos son $2$ y $6$. El cociente de $V(u)-V(1)$ entre $u-1$ tiende a $2$ por la izquierda y a $6$ por la derecha. Por tanto, $V'(1)$ no existe. La posición y la velocidad tienen valores clásicos en el nodo, pero la aceleración no. En magnitudes físicas, $v=(L/T)V$ sigue siendo continua y las aceleraciones laterales son $2L/T^2$ y $6L/T^2$.

[]{#fispm-t1-c07-e0020}

**Ejercicio 7.20.** En $[0,2]$, sea $X(u)=u$ para $u\le1$ y $X(u)=1+2(u-1)$ para $u\ge1$. Determina si hay velocidad y rapidez instantáneas clásicas en $u=1$.

**Solución.** Los valores de posición coinciden en $1$, así que la función es continua. Para $h<0$, $\bigl(X(1+h)-X(1)\bigr)/h=1$; para $h>0$, ese cociente vale $2$. Los límites son diferentes y no existe $X'(1)$.

Dentro de los tramos, las componentes normalizadas son $1$ y $2$, y las rapideces físicas son $L/T$ y $2L/T$. En el nodo no hay vector velocidad clásico del cual tomar la norma; tampoco hay rapidez instantánea clásica según la definición usada en el capítulo. Asignar una de las dos cifras al nodo no crea la derivada que falta. La historia pertenece a definición 7.7, pero no es $C^1$ global.

[]{#fispm-t1-c07-e0021}

**Ejercicio 7.21.** En tiempo normalizado, prescribe $A=1$ para $0\le u<1$ y $A=-1$ para $1<u\le3$, sin asignar aceleración clásica en $u=1$. Con $X(0)=V(0)=0$, construye un empalme $C^1$ y calcula la distancia total. Audita la aceleración en la unión.

**Solución.** En el primer tramo, integrar da $V(u)=u$ y $X(u)=u^2/2$. Sus valores finales son $V(1)=1$ y $X(1)=1/2$. Esos valores seleccionan el segundo tramo. Con $w=u-1$, la aceleración $-1$ da $$V(u)=1-w,\qquad X(u)=\frac12+w-\frac{w^2}{2},\qquad 1\le u\le3.$$ En $w=0$ coinciden posición y pendiente, luego proposición 7.9 certifica el empalme $C^1$. Las derivadas laterales de velocidad son $1$ y $-1$, por lo que no existe aceleración clásica en el nodo. Las fórmulas de aceleración cumplen el dato en los intervalos donde fue prescrito.

La velocidad es positiva hasta $u=2$, se anula allí y es negativa después. Se tienen $X(0)=0$, $X(2)=1$ y $X(3)=1/2$. El recorrido es por tanto $L(1-0)+L(1-1/2)=3L/2$. El desplazamiento es sólo $L/2$, porque parte del recorrido se deshace en el último tramo.

La exclusión de $u=1$ en el dato de aceleración es necesaria: asignarle el valor $1$ o $-1$ no alteraría una integral, pero ninguno sería la segunda derivada de esta posición en el nodo. El problema distingue una asignación aislada de un dato integral de la existencia de una derivada clásica.

Una historia por tramos queda determinada por sus leyes, sus dominios y sus uniones. Con esos datos ya se pueden buscar instantes donde alcanza una marca o coincide con otra historia, sin extender una fórmula fuera del tramo que la define.

[]{#eventos-encuentros-y-admisibilidad}

[]{#fispm-t1-c07-s11}

[]{#fpm-i-07-s11}

## 11. Eventos, encuentros y admisibilidad {#fispm-c07-eventos-encuentros-y-admisibilidad}

Conocer una ley temporal permite preguntar cuándo el móvil alcanza una marca del riel. La incógnita pasa a ser el tiempo: se resuelve una ecuación de posición. Pero las raíces algebraicas sólo son candidatas. Cada una debe pertenecer al dominio de la historia y al tramo cuya fórmula se utilizó.

[]{#fig:I-07-N03}

<figure id="fig-fpm-v04-i-07-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-07-N03.svg" class="lightbox" data-gallery="fpm-v04-c07"><img src="/assets/books/fispm/v04/I-07-N03.svg" alt="Evento de detención. Diagrama del capítulo 7; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="247" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 7.4.** La ley $X=2u-u^2/2$ alcanza un máximo en $u=2$, donde $V=0$ y $A=-1$. La continuación después del evento invierte el sentido; imponer detención permanente sería otro modelo. Véase §[11](#fispm-c07-eventos-encuentros-y-admisibilidad).

</figcaption>

</figure>

Un encuentro requiere además comparar dos posiciones en un mismo instante, marco y reloj. Que dos móviles recorran alguna vez la misma marca no significa que se encuentren: pueden llegar en tiempos diferentes.

[]{#instantes-de-un-evento-de-posición}

### Instantes de un evento de posición {#fispm-c07-instantes-de-un-evento-de-posiciuxf3n}

[]{#fispm-t1-c07-d0008}

**Definición 7.8 --- Conjunto de tiempos de un evento de posición.** Para una historia $x:I\to\mathbb R$ y una coordenada fija $\xi$, definimos $$\mathcal T_\xi(x)=\{t\in I:x(t)=\xi\}.$$ El conjunto reúne todos los instantes de la historia en que se ocupa el punto $O+\xi e$.

La definición incluye el dominio dentro de la condición. El resultado puede ser vacío, contener un tiempo, varios tiempos o un intervalo entero. Una historia en reposo sobre la marca durante un intervalo hace que cada instante de ese intervalo sea un evento; no existe entonces una única «hora de llegada» sin una condición adicional.

Por ejemplo, $X(u)=(u-1)^2$ en $[0,2]$ alcanza $X=0$ sólo en $u=1$, mientras que alcanza $X=1$ en $u=0$ y $u=2$. El cero de $(u-1)^2$ es una raíz doble, pero corresponde a un solo instante. La multiplicidad algebraica no cuenta eventos distintos. Aquí $V=2(u-1)$ cambia de signo en el evento central; la historia toca la marca y regresa. Resolver $X=0$ no describe por sí solo ese comportamiento: se usó también el signo de la velocidad.

Si la ley está definida por tramos, se resuelve $x_j(t)=\xi$ en cada dominio $[\tau_{j-1},\tau_j]$. Las raíces que no pertenecen a ese dominio se descartan. Los nodos que aparezcan en dos tramos se reúnen como un mismo instante, porque el resultado es un conjunto y definición 7.7 asegura un único valor de posición allí.

[]{#encuentros-en-una-descripción-común}

### Encuentros en una descripción común {#fispm-c07-encuentros-en-una-descripciuxf3n-comuxfan}

[]{#fispm-t1-c07-d0009}

**Definición 7.9 --- Encuentro en un marco y reloj comunes.** Sean dos historias rectilíneas $x_A:I_A\to\mathbb R$ y $x_B:I_B\to\mathbb R$, expresadas respecto del mismo origen, orientación, unidad de longitud y reloj. Su conjunto de encuentros es $$\mathcal C(x_A,x_B)=\{t\in I_A\cap I_B:x_A(t)=x_B(t)\}.$$

La intersección de dominios fija los tiempos en que ambas historias están disponibles. Puede ser un intervalo, un solo punto o el conjunto vacío. Si es vacía, no hay un encuentro definido por esas dos historias. Una raíz de una ecuación prolongada no añade un instante a esa intersección.

La igualdad de coordenadas representa igualdad de puntos porque el marco es común. Comparar cifras medidas desde orígenes distintos, sin traducirlas a una representación común, no demostraría encuentro. Tampoco estamos cambiando a un observador móvil: se mantienen los datos fijos de §1.

Para dos leyes afines, la ecuación de encuentro se reduce a una igualdad lineal. Si las velocidades son distintas, hay como máximo una candidata; si son iguales y las posiciones iniciales difieren, no hay ninguna; si las leyes coinciden, todo el dominio común pertenece al conjunto. Las tres alternativas deben considerarse antes de dividir por una diferencia de velocidades que puede ser cero.

[]{#la-raíz-y-el-dominio-tienen-funciones-distintas}

### La raíz y el dominio tienen funciones distintas {#fispm-c07-la-rauxedz-y-el-dominio-tienen-funciones-distintas}

Supongamos que una ley cuadrática se adopta sólo hasta un tiempo final conocido. El polinomio puede tener otra raíz más allá de ese tiempo; esa raíz pertenece a su prolongación algebraica, no al conjunto de eventos de la historia declarada. Del mismo modo, un tiempo negativo es admisible si está dentro del intervalo elegido: el origen del reloj no impone una prohibición física a todo tiempo anterior.

Esta distinción se coteja con Shankar, edición ampliada de 2019, cap. 1 §1.5, pp. 10--12. Se usa el control del intervalo y de raíces adicionales; la situación y los cálculos de los ejercicios siguientes son propios y no reproducen su problema de caída.

Una igualdad de posición en un nodo tampoco garantiza velocidades iguales. El evento puede estar definido por continuidad, aunque la derivada falte allí. Para informar cómo ocurre el evento, la regularidad y los signos se auditan por separado.

[]{#ejercicios-9}

### Ejercicios {#fispm-c07-ejercicios-9}

[]{#fispm-t1-c07-e0022}

**Ejercicio 7.22.** En $[0,2]$, sean $X_A(u)=u$ y $X_B(u)=2-u$. Halla sus encuentros. Compara con el caso $X_B=X_A$ y con una tercera historia $X_C(u)=u+1$ sobre el mismo dominio.

**Solución.** Resolver $u=2-u$ da $u=1$, que pertenece a $[0,2]$. El conjunto de encuentros normalizado es $\{1\}$, y la posición común es $X=1$. En magnitudes físicas, el encuentro ocurre en $t=t_0+T$ y en $P=O+Le$.

Si $X_B=X_A$, la igualdad se cumple para cada $u\in[0,2]$. El conjunto es todo el intervalo; hablar de un único encuentro omitiría la coincidencia continua. Para $X_C=u+1$, la ecuación $u=u+1$ equivale a $0=1$ y no tiene solución. Ambos móviles tienen la misma velocidad normalizada, pero sus posiciones difieren siempre en $1$. La separación física es $L$, y el conjunto de encuentros es vacío. No se divide por la diferencia nula de velocidades.

[]{#fispm-t1-c07-e0023}

**Ejercicio 7.23.** La historia $X(u)=2+u-u^2$ está declarada en $[0,2]$. Encuentra todos los tiempos en que $X=0$ y juzga las raíces de la ecuación. Explica qué cambiaría si el dominio declarado fuese $[-1,2]$.

**Solución.** La ecuación es $u^2-u-2=0$, que factoriza como $(u-2)(u+1)=0$. Las raíces del polinomio son $2$ y $-1$. Al intersectarlas con $[0,2]$, queda sólo $u=2$. El conjunto físico de eventos es $\{t_0+2T\}$.

Se descarta $u=-1$ porque no pertenece al dominio dado, no porque todo tiempo negativo sea inadmisible. Si la misma ley se declarase y fuese válida en $[-1,2]$, ambos extremos serían eventos: el conjunto sería $\{t_0-T,t_0+2T\}$. Eso sería otra declaración de dominio, que no se obtiene automáticamente al resolver la ecuación de la historia original.

Como $V(u)=1-2u$, los signos de velocidad en las dos raíces prolongadas serían diferentes. Esa información puede interpretar los eventos cuando pertenecen al dominio, pero no convierte una raíz excluida en un evento real de la historia inicial.

La búsqueda de eventos entrega conjuntos de tiempos acompañados de dominio y, cuando se pide, de posición y regularidad. Las ecuaciones aportan candidatas; la historia declarada determina cuáles son admisibles.

[]{#problemas-inversos-e-información-faltante}

[]{#fispm-t1-c07-s12}

[]{#fpm-i-07-s12}

## 12. Problemas inversos e información faltante {#fispm-c07-problemas-inversos-e-informaciuxf3n-faltante}

Hasta aquí hemos partido de una ley de velocidad o aceleración y de los datos iniciales que seleccionan una historia. Otra situación comienza con posiciones registradas en algunos instantes. Se desea recuperar la ley que las produjo. La pregunta cambia: ya no integramos una función temporal conocida, sino que examinamos qué información permiten determinar unas condiciones finitas.

[]{#fig:I-07-R02}

<figure id="fig-fpm-v04-i-07-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-07-R02.svg" class="lightbox" data-gallery="fpm-v04-c07"><img src="/assets/books/fispm/v04/I-07-R02.svg" alt="La velocidad no determina el origen de posición. Diagrama del capítulo 7; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="399" height="242" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 7.5.** Las historias $x=t$ y $x=1+t$ comparten velocidad y aceleración. Para seleccionar una de ellas hace falta un dato de posición. Todas las variables del ejemplo están normalizadas. Véase §[12](#fispm-c07-problemas-inversos-e-informaciuxf3n-faltante).

</figcaption>

</figure>

Tres posiciones pueden fijar los coeficientes de un polinomio cuadrático. Sin embargo, entre las marcas temporales hay una infinidad de historias suaves que pasan por los mismos puntos. Para distinguir ambas afirmaciones hace falta declarar primero la clase de historias admisibles.

[]{#identificar-dentro-de-una-familia}

### Identificar dentro de una familia {#fispm-c07-identificar-dentro-de-una-familia}

Trabajamos con las escalas de §1: $u=(t-t_0)/T$ y $x=x_*+LX(u)$, con $L,T>0$. Los datos son pares $(u_j,y_j)$, donde $y_j$ es una posición normalizada. No sumamos potencias de tiempo físico a una longitud: los coeficientes y la variable de los polinomios siguientes son adimensionales.

[]{#fispm-t1-c07-d0010}

**Definición 7.10 --- Identificación dentro de una clase cinemática.** Sea una familia declarada de historias $X_\theta:J\to\mathbb R$, parametrizada por $\theta\in\Theta$, y sean los datos finitos $X_\theta(u_j)=y_j$, con $u_j\in J$. El conjunto de parámetros compatibles es $$\Theta_{\mathrm{datos}}=\{\theta\in\Theta:X_\theta(u_j)=y_j\text{ para todo }j\}.$$ Hay existencia si ese conjunto no es vacío; los parámetros quedan identificados de manera única si contiene un solo elemento.

La unicidad se refiere a la parametrización elegida. Si dos parámetros distintos describen la misma historia, la historia podría quedar determinada sin que lo estuvieran los parámetros. En la familia $X(u)=c_0+c_1u+c_2u^2$ sobre un intervalo no degenerado, los coeficientes sí representan la historia de manera única: un polinomio nulo en todo ese intervalo tiene todos sus coeficientes nulos.

Una incompatibilidad puede aparecer antes de intentar un ajuste. Dos posiciones distintas atribuidas al mismo instante no pueden ser valores de una función. Si los datos son compatibles, todavía queda por examinar si las restricciones bastan dentro de la familia elegida.

[]{#tres-tiempos-distintos-y-una-ley-cuadrática}

### Tres tiempos distintos y una ley cuadrática {#fispm-c07-tres-tiempos-distintos-y-una-ley-cuadruxe1tica}

[]{#fispm-t1-c07-p0010}

**Proposición 7.10 --- Identificación cuadrática a partir de tres tiempos distintos.** Sean $u_1,u_2,u_3$ tres números reales distintos de un intervalo no degenerado $J$, y $y_1,y_2,y_3$ tres valores reales. Existe un único polinomio de grado a lo sumo dos que satisface $X(u_i)=y_i$ para $i=1,2,3$.

**Demostración.** Para construir el polinomio, buscamos tres piezas: la pieza asociada a $u_i$ debe valer uno allí y cero en los otros dos tiempos. Si $\{i,j,k\}=\{1,2,3\}$, la expresión $$\ell_i(u)=\frac{(u-u_j)(u-u_k)}{(u_i-u_j)(u_i-u_k)}$$ tiene esas propiedades. El denominador no es cero porque los tiempos son distintos. Cada $\ell_i$ es cuadrática y satisface $\ell_i(u_i)=1$, mientras que $\ell_i(u_j)=\ell_i(u_k)=0$. Por tanto, $$X(u)=y_1\ell_1(u)+y_2\ell_2(u)+y_3\ell_3(u)$$ tiene grado a lo sumo dos y toma los tres valores pedidos. Esto prueba existencia sin resolver un sistema mediante matrices.

Para probar unicidad, sean $X$ e $Y$ dos candidatos. Su diferencia $Q=X-Y$ tiene grado a lo sumo dos y se anula en los tres tiempos. Si fuese un polinomio no nulo, el teorema del factor obligaría a que $(u-u_1)(u-u_2)(u-u_3)$ lo dividiera: se extrae sucesivamente cada factor, y los otros ceros siguen siendo ceros del cociente porque los tiempos son distintos. Un polinomio no nulo de grado a lo sumo dos no puede tener un divisor de grado tres. Así, $Q$ es el polinomio nulo y $X=Y$. $\square$

La familia incluye polinomios afines y constantes; «grado a lo sumo dos» no exige un término cuadrático no nulo. Por proposición 7.8, una ley cuadrática corresponde a una aceleración constante en su dominio, con $A=2c_2$ y $a=2c_2L/T^2$. El resultado permite identificar esa aceleración **bajo la hipótesis de la familia**. Las tres posiciones no demuestran que tal hipótesis describa el movimiento entre las observaciones.

[]{#qué-no-determina-una-lista-finita-de-posiciones}

### Qué no determina una lista finita de posiciones {#fispm-c07-quuxe9-no-determina-una-lista-finita-de-posiciones}

[]{#fispm-t1-c07-p0011}

**Proposición 7.11 --- Subdeterminación por posiciones finitas.** Sea $J$ un intervalo no degenerado y sea $X_0\in C^2(J)$ una historia compatible con posiciones prescritas en un conjunto finito de tiempos distintos $u_1,\ldots,u_n\in J$, con $n\ge1$. Para cada $C\in\mathbb R$, la historia $$X_C(u)=X_0(u)+C\prod_{j=1}^{n}(u-u_j)$$ pertenece a $C^2(J)$ y conserva todas esas posiciones. Dos valores distintos de $C$ producen historias distintas.

**Demostración.** El producto es un polinomio; sumarlo a una función $C^2$ conserva esa regularidad. En cada tiempo $u_i$ uno de sus factores se anula, de modo que $X_C(u_i)=X_0(u_i)$.

Si $C\ne C'$, la diferencia de las historias es $(C-C')\prod_j(u-u_j)$. Un intervalo no degenerado contiene algún punto diferente de los finitísimos tiempos de la lista. En ese punto todos los factores son no nulos y la diferencia no es cero. Las historias son, por tanto, distintas, aunque sus muestras coincidan. $\square$

Si un tiempo aparece repetido con el mismo valor, basta conservarlo una vez. Si aparece con valores diferentes, no existe una historia compatible desde la cual iniciar la construcción. La restricción a un intervalo no degenerado asegura que hay tiempos sin muestrear; sobre un dominio reducido a un único instante esa conclusión no tendría sentido.

El contraejemplo deja libres sólo condiciones de posición. Si se conocen además velocidades, aceleraciones o restricciones de régimen, hay que auditarlas por separado: la familia construida no pretende conservar datos que no se impusieron. Tampoco garantiza que todas sus historias sean físicamente apropiadas para una situación concreta. Su función es demostrar que las posiciones finitas, por sí solas, no seleccionan una historia general.

[]{#fispm-t1-c07-mp0009}

**Principio metodológico 7.9 --- Declarar la familia antes de inferir unicidad desde datos.** Un informe de identificación expresa la clase elegida, las condiciones disponibles y la conclusión de existencia o unicidad dentro de esa clase. Distingue la identificación de parámetros de la justificación de la hipótesis cinemática.

[]{#ejercicios-10}

### Ejercicios {#fispm-c07-ejercicios-10}

[]{#fispm-t1-c07-e0024}

**Ejercicio 7.24.** En $0\le u\le2$, se adopta la familia $X(u)=c_0+c_1u+c_2u^2$. Los datos son $X(0)=1$, $X(1)=2$ y $X(2)=1$. Identifica los coeficientes, calcula $V(0)$ y $A$, y recupera las unidades físicas de velocidad y aceleración. Indica qué papel cumple la hipótesis cuadrática.

**Solución.** La condición en cero entrega $c_0=1$. Las otras dos condiciones se convierten en $$c_1+c_2=1,\qquad 2c_1+4c_2=0.$$ Restar el doble de la primera a la segunda da $2c_2=-2$. Así, $c_2=-1$ y $c_1=2$, y la historia identificada es $X(u)=1+2u-u^2$. Sustituir $u=0,1,2$ recupera los valores $1,2,1$, respectivamente.

La derivación entrega $V=2-2u$ y $A=-2$. Por tanto, $V(0)=2$, la velocidad inicial física es $v(t_0)=2L/T$ y la aceleración es $a=-2L/T^2$ en todo el dominio adoptado. La constancia se concluye de la ley cuadrática supuesta e identificada; no queda probada empíricamente a partir de las tres posiciones.

[]{#fispm-t1-c07-e0025}

**Ejercicio 7.25.** Con los mismos datos y dominio del ejercicio 7.24, construye una familia de historias suaves que conserve las tres muestras y que, salvo un miembro, no tenga aceleración constante. Verifica que los miembros son distintos.

**Solución.** El producto que se anula en los tiempos de la muestra es $u(u-1)(u-2)$. Definimos $$X_\lambda(u)=1+2u-u^2+\lambda u(u-1)(u-2),\qquad \lambda\in\mathbb R.$$ Todos los miembros son polinomios y conservan las muestras. En $u=1/2$, el producto vale $3/8$, por lo que $$X_\lambda(1/2)=\frac74+\frac{3\lambda}{8}.$$ Ese valor distingue cualquier par de parámetros diferentes.

Al expandir el producto como $u^3-3u^2+2u$ y derivar dos veces, obtenemos $A_\lambda(u)=-2+\lambda(6u-6)$. Para $\lambda\ne0$ cambia con $u$; para $\lambda=0$ recupera ejercicio 7.24. La aceleración física es $(L/T^2)A_\lambda$. Las posiciones muestreadas admiten tanto la historia de aceleración constante como estas historias de aceleración variable.

[]{#fispm-t1-c07-e0026}

**Ejercicio 7.26.** Audita primero los datos $(0,0),(0,1),(1,2)$. Audita después $(0,0),(0,0),(1,2)$ dentro de la familia cuadrática sobre $[0,1]$. Decide en cada caso si hay existencia y unicidad.

**Solución.** La primera lista exige a la vez $X(0)=0$ y $X(0)=1$. No existe una función que cumpla ambas condiciones; el fallo precede a la elección de familia.

En la segunda lista, repetir $X(0)=0$ no añade una restricción independiente. En la familia cuadrática quedan $c_0=0$ y $c_1+c_2=2$, de donde $$X(u)=(2-c_2)u+c_2u^2,\qquad c_2\in\mathbb R.$$ Hay existencia y una familia infinita de parámetros compatibles. Para distinguir sus historias, basta evaluar en $u=1/2$: se obtiene $1-c_2/4$. Proposición 7.10 requería tres tiempos distintos; esta lista contiene sólo dos.

La información faltante puede proceder de una hipótesis de modelo todavía no justificada o de condiciones insuficientes dentro de la familia. Al pasar a una ley aproximada aparece otra obligación: controlar cómo se acumula la discrepancia a lo largo del tiempo.

[]{#aproximación-cinemática-y-horizonte-de-validez}

[]{#fispm-t1-c07-s13}

[]{#fpm-i-07-s13}

## 13. Aproximación cinemática y horizonte de validez {#fispm-c07-aproximaciuxf3n-cinemuxe1tica-y-horizonte-de-validez}

Una ley simplificada puede describir bien la posición durante un intervalo breve y perder precisión al prolongarla. Una diferencia pequeña de velocidad, mantenida durante mucho tiempo, acumula desplazamiento; una diferencia de aceleración altera primero la velocidad y después la posición. La pregunta útil es cuánto tiempo garantiza la información disponible que el error permanezca bajo la tolerancia elegida.

El capítulo 6 §6 separó error y residuo, y §§7--8 construyeron la linealización univariada con control del resto. Aplicaremos ese criterio a la variable temporal. Comparamos dos historias expresadas en el mismo marco fijo y reloj: una historia de referencia $x$ y una candidata $\widetilde x$. La referencia puede ser un modelo más completo; la comparación no convierte por sí sola a ninguno de los dos en descripción exacta del fenómeno.

[]{#presupuesto-y-horizonte}

### Presupuesto y horizonte {#fispm-c07-presupuesto-y-horizonte}

[]{#fispm-t1-c07-d0011}

**Definición 7.11 --- Presupuesto determinista y horizonte certificado.** Sean dos historias definidas desde $t_0$ hasta $t_0+H_0$, con $H_0>0$, y una tolerancia absoluta de posición $\varepsilon_x\ge0$. Un presupuesto de error es una función $B:[0,H_0]\to[0,\infty)$, con unidades de longitud, para la que se ha demostrado $$|x(t_0+h)-\widetilde x(t_0+h)|\le B(h) \quad\text{para todo }0\le h\le H_0.$$ Un horizonte certificado mediante ese presupuesto es un número $H\in[0,H_0]$ tal que $B(h)\le\varepsilon_x$ para todo $h\in[0,H]$, manteniéndose allí las hipótesis usadas para obtener la cota.

Si la tolerancia se refiere a una escala de longitud $L>0$, se escribe $\varepsilon_x=\tau L$, con $\tau\ge0$ adimensional. El presupuesto normalizado es $B/L$. Esa elección permite comparar errores aun cuando la posición de referencia sea cero, donde un error relativo a su valor sería indefinido.

La certificación es uniforme sobre el intervalo: no basta comprobar un instante arbitrario. Para los presupuestos crecientes que construiremos, controlar el extremo final sí será suficiente. La definición admite $H=0$ si sólo queda certificada la condición inicial; ello no concede información sobre un intervalo de duración positiva.

Estas son cotas deterministas entre historias. No constituyen incertidumbres experimentales ni presuponen distribuciones estadísticas. Si un presupuesto supera la tolerancia, se pierde esa garantía; el error efectivo puede seguir siendo menor.

[]{#integrar-una-diferencia-de-velocidad}

### Integrar una diferencia de velocidad {#fispm-c07-integrar-una-diferencia-de-velocidad}

[]{#fispm-t1-c07-p0012}

**Proposición 7.12 --- Cota integrada de error de velocidad.** Sean $x,\widetilde x\in C^1([t_0,t_0+H_0])$, con $H_0>0$, y $0\le H\le H_0$. Supongamos que $$|x(t_0)-\widetilde x(t_0)|\le\delta_x,\qquad |v(t)-\widetilde v(t)|\le\delta_v \quad(t_0\le t\le t_0+H),$$ donde $\delta_x,\delta_v\ge0$, $v=x'$ y $\widetilde v=\widetilde x'$. Entonces, para todo $0\le h\le H$, $$|x(t_0+h)-\widetilde x(t_0+h)|\le\delta_x+\delta_v h.$$

**Demostración.** La reconstrucción de la proposición 7.5, aplicada a ambas historias, da la igualdad $$x(t_0+h)-\widetilde x(t_0+h) =x(t_0)-\widetilde x(t_0) +\int_{t_0}^{t_0+h}[v(s)-\widetilde v(s)]\,ds.$$ Tomar módulos, usar la desigualdad triangular y acotar el integrando por $\delta_v$ entrega $$|x(t_0+h)-\widetilde x(t_0+h)| \le\delta_x+\int_{t_0}^{t_0+h}\delta_v\,ds =\delta_x+\delta_v h.$$ Si $H=0$, sólo se evalúa $h=0$ y la conclusión es la cota inicial. $\square$

La cota permite errores con signos variables. No depende de que se acumulen efectivamente en un mismo sentido; contempla el caso desfavorable en que no hay cancelación. Las unidades lo reflejan: $\delta_v h$ tiene unidades de longitud y puede sumarse a $\delta_x$.

Si $\delta_v>0$ y $\varepsilon_x\ge\delta_x$, basta elegir $$H\le\min\left\{H_0,\frac{\varepsilon_x-\delta_x}{\delta_v}\right\},$$ siempre que la cota de velocidad esté justificada en ese intervalo. Si $\delta_v=0$, el presupuesto es constante y no se divide por ella. Si $\varepsilon_x<\delta_x$, este presupuesto no certifica ni siquiera el instante inicial, aunque la cota inicial disponible podría ser más grande que el error efectivo.

[]{#integrar-dos-veces-una-diferencia-de-aceleración}

### Integrar dos veces una diferencia de aceleración {#fispm-c07-integrar-dos-veces-una-diferencia-de-aceleraciuxf3n}

[]{#fispm-t1-c07-p0013}

**Proposición 7.13 --- Cota integrada de error de aceleración.** Sean $x,\widetilde x\in C^2([t_0,t_0+H_0])$, con $H_0>0$, y $0\le H\le H_0$. Supongamos cotas no negativas $$|x(t_0)-\widetilde x(t_0)|\le\delta_x,\qquad |v(t_0)-\widetilde v(t_0)|\le\delta_v,$$ y $|a(t)-\widetilde a(t)|\le\delta_a$ para todo $t\in[t_0,t_0+H]$. Para $0\le h\le H$ se cumplen $$|v(t_0+h)-\widetilde v(t_0+h)|\le\delta_v+\delta_a h$$ y $$|x(t_0+h)-\widetilde x(t_0+h)| \le\delta_x+\delta_v h+\frac{\delta_a}{2}h^2.$$

**Demostración.** La primera integración de la proposición 7.6 entrega $$v(t_0+r)-\widetilde v(t_0+r) =v(t_0)-\widetilde v(t_0)+ \int_0^r[a(t_0+s)-\widetilde a(t_0+s)]\,ds.$$ Para cada $r\in[0,H]$, el mismo argumento triangular de la proposición 7.12 da $|v(t_0+r)-\widetilde v(t_0+r)|\le\delta_v+\delta_a r$. Esta cota depende del tiempo transcurrido: conservaremos esa dependencia al integrar la diferencia de posiciones. Así, $$|x(t_0+h)-\widetilde x(t_0+h)| \le\delta_x+\int_0^h(\delta_v+\delta_a r)\,dr =\delta_x+\delta_v h+\frac{\delta_a}{2}h^2.$$ Se han utilizado sucesivamente dos integrales de una variable. Para $H=0$, las conclusiones son las cotas iniciales. $\square$

Reemplazar prematuramente la cota de velocidad por su máximo $\delta_v+\delta_a H$ daría el presupuesto más grande $\delta_x+\delta_v h+\delta_a Hh$. La integración de su dependencia en $r$ explica el factor $1/2$ de la proposición 7.13.

Los tres términos del presupuesto tienen unidades de longitud. Para coeficientes no negativos, el presupuesto crece o permanece constante en $h\ge0$, pues su derivada es $\delta_v+\delta_a h\ge0$. Por ello basta resolver la desigualdad en $h=H$ y mantener $H\le H_0$. No se prolonga una cota de aceleración más allá del dominio donde fue demostrada.

[]{#la-recta-tangente-como-historia-aproximada}

### La recta tangente como historia aproximada {#fispm-c07-la-recta-tangente-como-historia-aproximada}

Tomemos la candidata $\widetilde x(t_0+h)=x(t_0)+v(t_0)h$. Tiene los mismos datos iniciales y aceleración cero. Si $x\in C^2$ y $|a(t)|\le M$ en el intervalo de control, proposición 7.13 da $$|x(t_0+h)-x(t_0)-v(t_0)h|\le\frac M2 h^2.$$ Es la aplicación temporal de la cota del resto del capítulo 6 §8, obtenida aquí por dos integraciones. La posición base y la velocidad base quedan conservadas; se controla lo que se pierde al mantener fija la velocidad.

Para $M>0$ y tolerancia $\tau L$, el intervalo suficiente tiene duración no mayor que $\sqrt{2\tau L/M}$, además de la restricción de dominio. Para $M=0$, la historia de referencia es afín en ese intervalo y la candidata coincide con ella. Una velocidad inicial nula tampoco invalida la cota absoluta: sólo advierte que la recta tangente no conserva un cambio de posición cuyo primer término sea cuadrático.

Controlar posición no certifica automáticamente los tiempos de todos sus eventos. Una perturbación pequeña puede eliminar una raíz tangencial: $X(u)=u^2$ alcanza cero en $[-1,1]$, mientras que $\widetilde X(u)=u^2+\eta$, con $\eta>0$, no lo alcanza, aunque su error uniforme de posición sea $\eta$. Una conclusión sobre eventos requiere condiciones adicionales; los presupuestos presentes responden a una tolerancia de posición.

Referencia interna: [capítulo 6](fisica-para-matematicos-capitulo-6-modelos-aproximaciones-escalas-y-linealizacion.md#fispm-c06-modelos-aproximaciones-escalas-y-linealizaciuxf3n), §6, error frente a residuo; §§7--8, aproximación afín y cota cuadrática del resto.

[]{#ejercicios-11}

### Ejercicios {#fispm-c07-ejercicios-11}

[]{#fispm-t1-c07-e0027}

**Ejercicio 7.27.** Dos historias $C^1$ están disponibles en $0\le u\le H_0$, con $H_0>0$. En ese intervalo se sabe que $|X(0)-\widetilde X(0)|\le0.02$ y $|V(u)-\widetilde V(u)|\le0.03$. Certifica un horizonte con tolerancia normalizada de posición $0.10$. Explica qué concluyes si se desea prolongarlo más allá.

**Solución.** Aplicamos proposición 7.12 a las variables normalizadas. El presupuesto es $B_X(u)=0.02+0.03u$, una función creciente. Para que no exceda $0.10$ hasta $H$ basta exigir $$0.02+0.03H\le0.10,$$ que equivale a $H\le0.08/0.03=8/3$. El horizonte mayor certificado por este presupuesto y el dominio disponible es $\min\{H_0,8/3\}$.

En magnitudes físicas, la tolerancia es $0.10L$, las cotas inicial y de velocidad son $0.02L$ y $0.03L/T$, y la duración certificada es $T\min\{H_0,8/3\}$. El presupuesto dimensional produce la misma conclusión.

Si $H_0>8/3$, superar $8/3$ pierde la garantía de este presupuesto, sin demostrar que las historias concretas se separen más de la tolerancia. Si se supera $H_0$, tampoco están disponibles las hipótesis de la cota. En cualquiera de los dos casos hace falta información adicional para certificar la prolongación.

[]{#fispm-t1-c07-e0028}

**Ejercicio 7.28.** Dos historias $C^2$ tienen la misma posición y velocidad iniciales en $u=0$, y satisfacen $|A(u)-\widetilde A(u)|\le0.04$ en $[0,3]$. Certifica una tolerancia de posición $0.02$. Construye un par que sature el presupuesto y otro que muestre por qué la pérdida de garantía no demuestra un fallo efectivo. Relaciona el resultado con el resto de una linealización.

**Solución.** En proposición 7.13 los errores iniciales son cero. El presupuesto normalizado es $B_X(u)=0.04u^2/2=0.02u^2$. La desigualdad $0.02H^2\le0.02$, con $H\ge0$, equivale a $H\le1$. El dominio de control llega hasta $3$, así que $H=1$ es el horizonte mayor certificado por este presupuesto. La duración física es $T$ y la tolerancia es $0.02L$.

Para mostrar saturación, tomamos $\widetilde X(u)=0$ y $X(u)=0.02u^2$ sobre $[0,3]$. Ambas historias tienen posición y velocidad iniciales nulas, y $A-\widetilde A=0.04$. Su error es exactamente $0.02u^2$, de modo que sí supera la tolerancia para $u>1$.

En cambio, las historias $X=\widetilde X=0$ satisfacen las mismas cotas disponibles y tienen error cero hasta $u=3$. La cota no obliga a que se realice el peor caso. Si la candidata fuese la recta tangente de una historia con $|A|\le0.04$, el presupuesto obtenido sería el mismo control cuadrático de su resto. La validez local procede de la cota de segunda derivada y del dominio, no de la apariencia recta de un dibujo.

[]{#reconstruir-y-auditar-una-historia-completa}

[]{#fispm-t1-c07-s14}

[]{#fpm-i-07-s14}

## 14. Reconstruir y auditar una historia completa {#fispm-c07-reconstruir-y-auditar-una-historia-completa}

Una reconstrucción reúne decisiones que pueden comprobarse por separado. El origen y el reloj permiten interpretar una coordenada; la regularidad autoriza las derivadas; los datos iniciales seleccionan una historia dentro de la clase prescrita. Después vienen las preguntas sobre eventos y recorrido. Si se usa una aproximación, su dominio puede ser menor que el de la historia de referencia.

Para cerrar el trabajo hace falta conservar la relación entre esas decisiones. Una fórmula de posición sin dominio no permite filtrar una raíz; una velocidad sin escala no proporciona una magnitud física; una cota sin hipótesis no certifica un intervalo.

[]{#una-ficha-que-permita-recuperar-el-razonamiento}

### Una ficha que permita recuperar el razonamiento {#fispm-c07-una-ficha-que-permita-recuperar-el-razonamiento}

[]{#fispm-t1-c07-d0012}

**Definición 7.12 --- Ficha de reconstrucción cinemática controlada.** Una ficha reúne el marco espacial fijo y el reloj, el dominio temporal y las escalas, los datos disponibles, la clase o ley cinemática adoptada y su estatuto, la historia reconstruida con su regularidad, los eventos y observables solicitados, y el control de cualquier aproximación utilizada. Este último declara la candidata, la tolerancia, las cotas justificadas y el régimen temporal certificado.

La ficha especializa la de aproximación controlada del capítulo 6 §14. Si la aceleración se prescribe como una función del tiempo, se identifica como dato del modelo. No se atribuye esa prescripción a una explicación dinámica todavía no estudiada. Si falta información para una conclusión solicitada, se registra la conclusión que sigue abierta.

No es necesario recalcular una derivación ya probada. Proposición 7.6 puede justificar una reconstrucción al comprobar sus hipótesis y los datos iniciales; proposición 7.13 puede justificar un presupuesto al declarar las cotas. La ficha debe permitir distinguir qué se tomó como dato, qué se supuso y qué se obtuvo por cálculo.

[]{#fispm-t1-c07-mp0010}

**Principio metodológico 7.10 --- Entregar una historia con hipótesis y control.** La conclusión cinemática acompaña la ley temporal con su dominio, datos y condiciones de uso. Una aproximación se entrega con la observable controlada y la evidencia que certifica su intervalo.

Referencia interna: [capítulo 6](fisica-para-matematicos-capitulo-6-modelos-aproximaciones-escalas-y-linealizacion.md#fispm-c06-modelos-aproximaciones-escalas-y-linealizaciuxf3n), §14, ficha de aproximación controlada. Las siguientes síntesis y sus soluciones son propias.

[]{#ejercicios-de-síntesis}

### Ejercicios de síntesis {#fispm-c07-ejercicios-de-suxedntesis}

[]{#fispm-t1-c07-e0029}

**Ejercicio 7.29.** En una recta fija, con $x_*=0$, se prescribe $A(u)=-2u$ sobre $[0,3]$, junto con $X(0)=1$ y $V(0)=3$. Construye una ficha que reconstruya la historia y determine las inversiones, el regreso a $X=1$, el desplazamiento y la distancia total. Audita después la candidata $\widetilde X(u)=1+3u$ con tolerancia de posición $0.01$: obtén el horizonte a partir del resto exacto y compáralo con el que se obtiene usando únicamente una cota uniforme de aceleración en el intervalo elegido.

**Solución.** La ficha fija $P(t)=O+LX(u)e$, $u=(t-t_0)/T$, con $L,T>0$, $O$ y $e$ constantes. El dominio físico es $[t_0,t_0+3T]$. La aceleración prescrita es $a(t)=-(2L/T^2)u$; se toma como hipótesis cinemática, sin derivarla de fuerzas. Los datos iniciales son $x(t_0)=L$ y $v(t_0)=3L/T$.

La reconstrucción de la proposición 7.6 exige integrar primero aceleración y después velocidad: $$V(u)=3+\int_0^u(-2s)\,ds=3-u^2,$$ $$X(u)=1+\int_0^u(3-s^2)\,ds=1+3u-\frac{u^3}{3}.$$ Estas funciones son polinomios, de modo que la historia es $C^2$ en todo el dominio, con derivadas laterales en sus extremos. Derivar $X$ y $V$ verifica la aceleración y los datos iniciales. Proposición 7.6 asegura unicidad bajo esa prescripción.

El signo de $V$ organiza el movimiento. La ecuación $3-u^2=0$ da $u=\pm\sqrt3$, y sólo $\sqrt3$ pertenece a $[0,3]$. En $[0,\sqrt3)$ la velocidad es positiva; en $(\sqrt3,3]$ es negativa. Por definición 7.3 hay una inversión interior en $u=\sqrt3$, que corresponde a $t=t_0+\sqrt3\,T$. La posición alcanza allí su máximo: $$X(\sqrt3)=1+3\sqrt3-\frac{3\sqrt3}{3}=1+2\sqrt3.$$ El móvil avanza hacia el sentido de $e$ y luego regresa. La aceleración es negativa para $u>0$: antes de la inversión disminuye la rapidez y después la aumenta, de acuerdo con el signo de $va$.

Para localizar los eventos en $X=1$, conservamos la ecuación y el dominio: $$1+3u-\frac{u^3}{3}=1 \quad\Longleftrightarrow\quad u(9-u^2)=0.$$ Las candidatas son $0,3,-3$. Su intersección con $[0,3]$ es $\{0,3\}$: el instante inicial es una ocupación de la marca, y el regreso posterior ocurre en $u=3$. Los eventos físicos son $t_0$ y $t_0+3T$.

Ambos extremos tienen $X=1$, por lo que el desplazamiento total es cero. La distancia exige separar los sentidos: $$\frac dL= \int_0^{\sqrt3}(3-u^2)\,du+ \int_{\sqrt3}^{3}(u^2-3)\,du =2\sqrt3+2\sqrt3=4\sqrt3.$$ Así, $d=4\sqrt3\,L$, aunque el desplazamiento sea nulo. La posición máxima permite comprobar el mismo resultado: el tramo de ida y el de vuelta recorren cada uno $2\sqrt3\,L$.

La candidata $\widetilde X=1+3u$ conserva posición y velocidad iniciales, pero adopta aceleración cero. El resto de posición es una igualdad exacta: $$X(u)-\widetilde X(u)=-\frac{u^3}{3}.$$ En $u\ge0$, su módulo crece con $u$. La tolerancia $0.01$ se cumple para todos los tiempos hasta $H$ si y sólo si $$0\le H\le3,\qquad \frac{H^3}{3}\le0.01.$$ El horizonte máximo efectivo de esta candidata para el criterio declarado es $$H_{\mathrm{exacto}}=(0.03)^{1/3}\approx0.31072.$$ Se usa el valor exacto para la certificación; la cifra decimal sólo lo representa. La duración física es $T(0.03)^{1/3}$ y la tolerancia absoluta es $0.01L$. Para cualquier $u$ mayor que ese horizonte dentro de $[0,3]$, el error efectivo sí supera la tolerancia.

También puede recuperarse el resto integrando la cota variable. Como $|A(s)-\widetilde A(s)|=2s$ para $s\ge0$, el error de velocidad queda acotado por $\int_0^r2s\,ds=r^2$. Integrarlo hasta $u$ da $\int_0^ur^2\,dr=u^3/3$. En esta historia ambas cotas se alcanzan.

Si se conserva sólo la cota uniforme $|A-\widetilde A|\le2H$ sobre $[0,H]$, proposición 7.13 da en cada $u\le H$ el presupuesto $$|X(u)-\widetilde X(u)|\le\frac{2H}{2}u^2=Hu^2.$$ Su máximo es $H^3$. Por esta vía basta exigir $H^3\le0.01$, lo que certifica $$H_{\mathrm{uniforme}}=(0.01)^{1/3}\approx0.21544.$$ Elegir este $H$ es autoconsistente: en todo el intervalo elegido se cumple $2u\le2H$. La garantía es más conservadora porque sustituye una aceleración de error que crece desde cero por su máximo en todo el intervalo. El horizonte exacto no puede atribuirse a ese presupuesto uniforme.

La ficha concluye que la historia completa está reconstruida en $[0,3]$ bajo la aceleración prescrita. La candidata afín controla posición sólo en el intervalo certificado elegido. No reproduce la inversión ni el regreso: su velocidad normalizada es siempre $3$ y alcanza $X=1$ únicamente en $u=0$. La certificación local de posición no permite utilizarla para esos eventos lejanos.

[]{#fispm-t1-c07-e0030}

**Ejercicio 7.30.** Audita las cuatro frases de este informe:

- «La tangente forma un ángulo de $45^\circ$ en el dibujo; por eso la velocidad es $1$».

- «Si la velocidad es cero en un instante, el móvil invierte allí su sentido».

- «Una aceleración negativa siempre frena al móvil».

- «Tres posiciones en tiempos distintos demuestran que la aceleración es constante».

Repara cada afirmación con una condición o un contraejemplo ya disponible. Construye después una ficha completa para una reparación, incluyendo una aproximación con tolerancia de posición declarada.

**Solución.** La primera frase omite las unidades y las escalas. Si un dibujo usa coordenadas de papel $p=(t-t_0)/\alpha$ y $q=(x-x_*)/\beta$, con $\alpha>0$ una escala temporal y $\beta>0$ una escala de longitud, entonces su pendiente es $dq/dp=(\alpha/\beta)v$. Un ángulo de $45^\circ$ en ejes perpendiculares con la misma unidad de papel significa pendiente gráfica uno; la velocidad física vale $\beta/\alpha$, con unidades de longitud por tiempo. Cambiar la razón de escalas cambia el ángulo dibujado aunque la historia física sea la misma. La reparación exige convertir la pendiente mediante las escalas, como en el ejercicio 7.4.

La segunda frase confunde una condición necesaria de la inversión suave con una conclusión suficiente. Cerca de cero, $X=u^2$ tiene $V=2u$ y cambia de sentido; $X=u^3$ tiene $V=3u^2$ y mantiene el sentido a ambos lados. Ambos tienen $V(0)=0$. La reparación consiste en verificar los signos en semientornos del instante, conforme a definición 7.3 y ejercicio 7.5.

La tercera frase falla cuando velocidad y aceleración son negativas. En ejercicio 7.7, $V=-2-u$ sobre $[0,1]$ y $A=-1$, mientras que la rapidez normalizada $|V|=2+u$ crece. Fuera de los ceros de velocidad, proposición 7.3 determina su variación mediante el signo de $va$. «Frenar», entendido como disminuir rapidez, requiere ese análisis; en $v=0$ no se aplica la fórmula derivativa sin examinar el punto.

La cuarta frase omite la clase de modelos. Proposición 7.10 identifica una ley de grado a lo sumo dos bajo esa hipótesis. Proposición 7.11 y ejercicio 7.25 producen historias distintas con las mismas posiciones finitas. La conclusión reparada es unicidad de los coeficientes dentro de la familia cuadrática, no demostración de la aceleración constante del fenómeno.

Construimos una ficha para la tercera reparación. Se fija $P(t)=O+LX(u)e$, $u=(t-t_0)/T$, sobre $[0,1]$, con $L,T>0$. El modelo prescribe $A=-1$, $X(0)=1$ y $V(0)=-2$. Proposición 7.6 entrega $$V(u)=-2-u,\qquad X(u)=1-2u-\frac{u^2}{2}.$$ La historia es $C^2$ en el dominio; su aceleración física es $-L/T^2$ y su velocidad es $(L/T)(-2-u)$. Como $V<0$ en todo el intervalo, no hay reposo ni inversión. La rapidez física es $(L/T)(2+u)$ y crece a pesar de la aceleración negativa.

Como evento de posición, la ocupación de $X=0$ exige $u^2+4u-2=0$. Las candidatas son $-2\pm\sqrt6$ y sólo $-2+\sqrt6\in[0,1]$ es admisible. El evento ocurre en $t=t_0+(-2+\sqrt6)T$. Los extremos tienen $X(0)=1$ y $X(1)=-3/2$, de modo que el desplazamiento es $-5L/2$ y, al conservarse el sentido, la distancia es $5L/2$.

Para aproximar posición se adopta $\widetilde X=1-2u$, con tolerancia absoluta $L/8$. Su error normalizado es $u^2/2$, que coincide con el presupuesto de la proposición 7.13 para datos iniciales iguales y diferencia de aceleración de módulo uno. Exigir $u^2/2\le1/8$ en $u\ge0$ certifica $0\le u\le1/2$. La duración certificada es $T/2$; la historia de referencia conserva su dominio $[0,1]$. El evento en $u=-2+\sqrt6$ pertenece al intervalo de posición certificado, pero no se ha certificado un error en su tiempo mediante esa sola cota.

La ficha permite comprobar cada conclusión desde el modelo declarado: derivar verifica las componentes, sus signos determinan el sentido y la rapidez, la ecuación de posición entrega un evento filtrado por dominio y el resto limita la aproximación. La hipótesis de aceleración constante está expuesta desde el inicio; no se deduce de un dibujo ni de una lista de muestras.

[]{#bibliografía-citada}

## Bibliografía citada {#fispm-c07-bibliografuxeda-citada .unnumbered}

[]{#canon-interno-citado}

### Canon interno citado {#fispm-c07-canon-interno-citado}

- *Física para matemáticos*, Tomo I, capítulo 2, «Magnitudes, unidades y análisis dimensional». [capítulo 2](fisica-para-matematicos-capitulo-2-magnitudes-unidades-y-analisis-dimensional.md#fispm-c02-magnitudes-unidades-y-anuxe1lisis-dimensional). Localizadores usados: §§9--10, interfaz de escalas y adimensionalización citada en §1.

- *Física para matemáticos*, Tomo I, capítulo 5, «Tiempo, movimiento y curvas». [capítulo 5](fisica-para-matematicos-capitulo-5-tiempo-movimiento-y-curvas.md#fispm-c05-tiempo-movimiento-y-curvas). Localizadores usados: §3, representación de posición y coordenadas, y §§5--7, velocidad, regularidad/reposo y aceleración, citados en §1 y aplicados en §§2--4; §13 proposición 7.28, fórmula de longitud citada y aplicada en §5.

- *Física para matemáticos*, Tomo I, capítulo 6, «Modelos, aproximaciones, escalas y linealización». [capítulo 6](fisica-para-matematicos-capitulo-6-modelos-aproximaciones-escalas-y-linealizacion.md#fispm-c06-modelos-aproximaciones-escalas-y-linealizaciuxf3n). Localizadores usados: §6, diferencia entre error y residuo, y §§7--8, linealización univariada y cota del resto, citados en §13; §14, ficha de aproximación controlada, citada y especializada en §14.

[]{#obra-externa-citada}

### Obra externa citada {#fispm-c07-obra-externa-citada}

- Shankar, R. *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*. Expanded Edition. Yale University Press, 2019. Cap. 1, §1.3, pp. 4--6, cantidades medias e instantáneas, citado en §2; cap. 1 §1.4, pp. 6--8, significado de las dos constantes de integración y datos iniciales, citado en §7; pp. 6--10, leyes de aceleración constante, citadas en §9; cap. 1 §1.5, pp. 10--12, dominio y raíces adicionales, citado en §11.

- Kleppner, Daniel, y Robert J. Kolenkow. *An Introduction to Mechanics*. Copia publicada por Cambridge University Press, 2010; publicación previa McGraw-Hill, 1973. Cap. 1 §1.7, pp. 19--21, reconstrucción por integrales y datos iniciales; citado en §§6--8 y p. 21 en §9.
