---
title: "Energía potencial, fuerzas conservativas y estabilidad"
subtitle: "Física para matemáticos · Tomo I · Capítulo 13"
author: "A. Peña"
description: "Capítulo 13 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
archived-content-id: MA-BCH-0353
source-id: FISPM-T1-C13
editorial-id: FPM-I-13
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0352"]
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

[Capítulo 12](fisica-para-matematicos-capitulo-12-trabajo-potencia-y-energia-cinetica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos-v04-archivo.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 14](fisica-para-matematicos-capitulo-14-momento-lineal-impulso-y-centro-de-masa.md)

[]{#fispm-c13-energuxeda-potencial-fuerzas-conservativas-y-estabilidad}

El trabajo de una fuerza puede depender del camino. Cuando admite una representación mediante diferencias de una función de posición, el potencial reúne esa información y permite formular balances de energía mecánica. Estudiaremos las condiciones matemáticas de esa representación, la influencia del dominio y sus consecuencias dinámicas. La segunda parte desarrolla el análisis de equilibrio y estabilidad.

[]{#potencial-en-una-dimensión}

[]{#fispm-t1-c13-s01}

[]{#fpm-i-13-s01}

## 1. Potencial en una dimensión {#fispm-c13-potencial-en-una-dimensiuxf3n}

En el capítulo 12 calculamos el trabajo de una fuerza y lo igualamos al cambio de energía cinética. Para una fuerza que depende sólo de la posición sobre una línea, esa integral puede almacenarse en una función de estado: basta conocer la posición para asignarle un valor. La construcción permite comparar trabajos mediante diferencias de una misma función y plantea la pregunta que organizará este capítulo: ¿cuándo sigue siendo posible en varias dimensiones?[^1]

Comencemos sobre un intervalo abierto $I\subset\mathbb R$ con una fuerza continua $F:I\to\mathbb R$. La fuerza está especificada en la coordenada física $x$ de una línea fija; no depende del tiempo ni de la velocidad. Elegimos una posición de referencia $x_0\in I$ y un número $U_0$ con unidades de energía. Que $I$ sea un intervalo garantiza que el segmento entre posiciones pertenece al dominio del modelo.

[]{#fispm-t1-c13-d0001}

**Definición 13.1 --- Energía potencial unidimensional.** La energía potencial de $F$ con referencia $(x_0,U_0)$ es

$$U(x)=U_0-\int_{x_0}^{x}F(\xi)\,d\xi.$$

El signo menos hace que un trabajo positivo de la fuerza corresponda a una disminución del potencial. La integral es orientada: si $x<x_0$, se invierten sus límites con el signo correspondiente. No se está asignando una energía al camino recorrido, sino un valor a su extremo $x$.

[]{#fispm-t1-c13-p0001}

**Proposición 13.1 --- Recuperación de fuerza y trabajo.** La función definición 13.1 es de clase $C^1$ y satisface $F(x)=-U'(x)$. Para cualquier historia $C^1$ por tramos dentro de $I$, su trabajo es $W_F=U(x_a)-U(x_b)$, aunque haya retrocesos.

**Demostración.** La continuidad de $F$ permite aplicar el teorema fundamental y obtener $U'=-F$. A lo largo de un tramo, la regla de la cadena da $dU(x(t))/dt=-F(x(t))\dot x(t)$. Integrar produce $\int F(x(t))\dot x(t)dt=U(x_a)-U(x_b)$. La suma sobre tramos cancela los valores en extremos intermedios. No se divide por velocidad, por lo que se incluyen instantes de reposo. $\square$

La construcción funciona para toda fuerza continua de posición en un intervalo. No funciona de la misma manera para la fricción cinética, porque en un mismo punto ésta puede cambiar de dirección según el movimiento. Tampoco almacena en una función $U(x)$ una fuerza con dependencia temporal arbitraria. Definir una integral sobre una historia concreta no convierte su resultado en función de posición independiente de la historia.

El potencial tiene unidades de energía y su derivada espacial unidades de fuerza. Una pendiente positiva produce fuerza hacia las $x$ negativas; una pendiente negativa produce fuerza hacia las positivas. El valor de la pendiente, y no el valor absoluto de $U$, decide la fuerza. Un potencial grande y casi plano puede ejercer una fuerza pequeña, mientras uno de valor pequeño y pendiente fuerte puede ejercer una fuerza grande.

La fórmula del trabajo incluye una información física adicional: si esta fuerza es la resultante sobre una masa constante en un marco inercial, capítulo 12 da $K_b-K_a=U_a-U_b$. Si es sólo una contribución, todavía debemos sumar los trabajos de las restantes. Introducir $U$ no cambia qué fuerzas actúan ni su jerarquía en Newton.

[]{#fispm-t1-c13-mp0001}

**Principio metodológico 13.1 --- Construir antes de interpretar.** Especifica el intervalo y la ley de fuerza, fija una referencia y construye $U$. Comprueba $-U'=F$ y el signo de la diferencia que reproduce el trabajo. Antes de interpretar el cambio cinético, identifica si esa fuerza es total o sólo una contribución.

[]{#ejercicios}

### Ejercicios {#fispm-c13-ejercicios}

[]{#fispm-t1-c13-e0001}

[]{#fispm-t1-c13-e0013}

**Ejercicio 13.1.** Una fuerza en una línea es $F(x)=A-Bx$, con $A$ de unidades de fuerza y $B>0$ de unidades de fuerza por longitud. Construye el potencial con $U(0)=0$ y calcula el trabajo entre $x=a$ y $x=b$. Comprueba el resultado integrando la fuerza.

**Solución.** definición 13.1 da $U(x)=-Ax+Bx^2/2$. Su derivada es $-A+Bx$, de modo que $-U'=A-Bx$. El trabajo es $U(a)-U(b)=A(b-a)-B(b^2-a^2)/2$, idéntico a $\int_a^b(A-Bx)dx$. La fórmula vale con $b<a$ y cambia de signo al intercambiar extremos. La posición de pendiente cero es $A/B$, pero clasificarla dinámicamente requiere precisar el modelo y el significado de estabilidad; aquí sólo se ha recuperado la fuerza.

[]{#fispm-t1-c13-e0002}

**Ejercicio 13.2.** Una fuerza sobre una línea tiene ley $F(x)=-kx$, con $k>0$. Una partícula se mueve de $a>0$ a $0$ y luego a $-a$. Obtén el trabajo de cada tramo mediante potencial y explica por qué el trabajo total cero no implica potencia cero en todo instante.

**Solución.** Con $U(0)=0$, resulta $U(x)=kx^2/2$. El primer trabajo es $ka^2/2$ y el segundo $-ka^2/2$; el total es cero porque ambos extremos tienen el mismo potencial. Durante el movimiento, la potencia es $-kx\dot x$, que en general no se anula. Si el resorte es la única fuerza tangencial, la energía cinética aumenta hacia el origen y disminuye después. La igualdad entre los extremos no determina que la rapidez permaneciera constante, ni justifica omitir el tramo intermedio.

[]{#cero-de-potencial-y-superposición}

[]{#fispm-t1-c13-s02}

[]{#fpm-i-13-s02}

## 2. Cero de potencial y superposición {#fispm-c13-cero-de-potencial-y-superposiciuxf3n}

La posición de referencia introduce una libertad de representación. Cambiar el cero del potencial no cambia la fuerza ni el trabajo entre dos posiciones. Esa libertad no autoriza a cambiar por separado valores en puntos diferentes: la diferencia debe mantenerse. También permite sumar potenciales de varias fuerzas cuando éstas comparten la misma coordenada y el mismo dominio.[^2]

[]{#fispm-t1-c13-p0002}

**Proposición 13.2 --- Unicidad salvo una constante.** Si $U$ y $V$ son potenciales $C^1$ de la misma fuerza en un intervalo $I$, existe una constante $C$ tal que $V(x)=U(x)+C$ en todo $I$.

**Demostración.** Ambas funciones satisfacen $U'=-F=V'$, por lo que $(V-U)'=0$. Para cualesquiera $a,b\in I$, el teorema del valor medio aplicado al segmento entre ellos da $(V-U)(b)=(V-U)(a)$. La diferencia es constante en el intervalo. $\square$

El argumento depende de trabajar en una componente conectada. Si la fuerza estuviera definida en dos intervalos separados por una región excluida, cada componente admitiría su propia constante. El modelo no proporciona por sí solo una comparación energética entre ellas: ninguna historia dentro de su dominio conecta los dos lados. Más adelante veremos la versión en varias dimensiones.

Para el peso uniforme en un eje vertical ascendente, $F_y=-mg$ y un potencial es $U_g(y)=mgy+C$. Elegir el suelo, una plataforma o una mesa como altura cero cambia $C$. El trabajo entre alturas permanece $-mg(y_b-y_a)$. Un valor negativo de $U_g$ sólo indica que la posición está por debajo del cero elegido; no implica rapidez negativa ni energía cinética negativa.

Para un resorte fijo horizontal, $U_s(x)=kx^2/2+C$ cuando $x$ mide la deformación con signo. La referencia habitual $U_s(0)=0$ es cómoda, pero no obligatoria. Si usamos otra coordenada $z$ y la posición sin deformación es $z_0$, la expresión pasa a $k(z-z_0)^2/2+C$. Cambiar el cero de energía y cambiar el origen de posición son operaciones distintas: la segunda modifica cómo escribimos la deformación.

[]{#fispm-t1-c13-p0003}

**Proposición 13.3 --- Superposición de potenciales.** Si $F_1,\ldots,F_n$ tienen potenciales $U_1,\ldots,U_n$ en el mismo intervalo, la fuerza $F=\sum_iF_i$ tiene potencial $U=\sum_iU_i$.

**Demostración.** La suma finita es diferenciable y $-U'=-\sum_iU_i'=\sum_iF_i$. Proposición 13.1 convierte su diferencia entre extremos en el trabajo de la suma. $\square$

En una línea vertical, un resorte anclado con posición sin deformación en $y=0$ y el peso producen $U(y)=ky^2/2+mgy+C$. Su fuerza es $-ky-mg$. Completar el cuadrado da $U(y)=\frac{k}{2}\left(y+\frac{mg}{k}\right)^2+C-\frac{m^2g^2}{2k}.$

La posición de fuerza nula queda desplazada hacia abajo. La contribución constante no modifica esa posición. El cambio de potencial sigue incluyendo ambas interacciones, y no debe añadirse nuevamente el trabajo del peso si ya se empleó el potencial total para representar su efecto.

La suma describe un modelo con parámetros fijos. Si cambia $k$, se mueve el anclaje o varía el campo gravitatorio durante la historia, no basta comparar el mismo polinomio en dos posiciones: la función puede depender explícitamente del tiempo. Separaremos ese caso en §8.

[]{#fispm-t1-c13-mp0002}

**Principio metodológico 13.2 --- Mantener una referencia coherente.** Usa un mismo potencial en los dos extremos de cada comparación. Suma contribuciones que correspondan a las fuerzas incluidas y declara qué coordenada mide cada deformación. Si representas una fuerza mediante su potencial, no agregues además su trabajo como una contribución nueva al mismo balance.

[]{#ejercicios-1}

### Ejercicios {#fispm-c13-ejercicios-1}

[]{#fispm-t1-c13-e0003}

**Ejercicio 13.3.** Para un mismo resorte se escriben $U_1(x)=kx^2/2$ y $U_2(x)=kx^2/2+C$. Una historia tiene energías cinéticas $K_a,K_b$. Compara los trabajos y las diferencias de $K+U$ con ambas referencias. ¿Qué ocurre si se cambia el cero sólo en el extremo final?

**Solución.** Los trabajos coinciden porque $U_2(a)-U_2(b)=U_1(a)-U_1(b)$. También coincide $[K_b+U_2(b)]-[K_a+U_2(a)]$ con la expresión de referencia 1: los dos $C$ se cancelan. Los valores absolutos de $K+U$ difieren en $C$. Si se usa $U_1(a)$ y $U_2(b)$, se introduce una diferencia espuria $C$ y se mezclan convenciones. Un cambio uniforme de referencia no es una fuente de trabajo físico.

[]{#fispm-t1-c13-e0004}

**Ejercicio 13.4.** Una masa $m$ cuelga de un resorte vertical fijo de constante $k$, con coordenada $y$ ascendente y deformación cero en $y=0$. Construye el potencial total con valor cero en su posición de fuerza nula y calcula el trabajo total desde esa posición hasta un desplazamiento adicional $a$.

**Solución.** La posición de fuerza nula es $y_*=-mg/k$. El potencial con la referencia pedida es $U(y)=k(y-y_*)^2/2$. Su derivada produce $-U'=-k(y-y_*)=-ky-mg$, como requiere la suma de fuerzas. Entre $y_*$ y $y_*+a$, el trabajo total es $-ka^2/2$. Es negativo para cualquier $a\ne0$. Esto no significa que una partícula soltada en reposo desde $y_*$ llegue espontáneamente allí: sin otra acción, Newton mantiene el reposo. La fórmula calcula el trabajo de las fuerzas declaradas sobre el tramo propuesto, y su realización requiere datos o agentes compatibles.

[]{#gradiente-y-fuerza-potencial}

[]{#fispm-t1-c13-s03}

[]{#fpm-i-13-s03}

## 3. Gradiente y fuerza potencial {#fispm-c13-gradiente-y-fuerza-potencial}

En varias dimensiones una posición admite desplazamientos en direcciones distintas. La derivada de una función escalar debe expresar cómo cambia al movernos en cualquiera de ellas. En el espacio euclídeo, el gradiente reúne esas derivadas direccionales en un vector. Permite representar la fuerza a partir de una sola función y calcular su trabajo mediante la regla de la cadena.[^3]

Sea $\Omega\subset\mathbb R^d$ abierto, con coordenadas cartesianas ortonormales $x_1,\ldots,x_d$. Especificar el dominio es parte de especificar el campo: una región singular o excluida no puede cruzarse sin abandonar el modelo. Trabajaremos primero con un potencial $U:\Omega\to\mathbb R$ de clase $C^1$.

[]{#fispm-t1-c13-d0002}

**Definición 13.2 --- Gradiente euclídeo.** El gradiente de $U$ es el vector

$$\nabla U=(\partial_1U,\ldots,\partial_dU),$$

que representa su diferencial mediante $DU(\mathbf x)[\mathbf h]=\nabla U(\mathbf x)\cdot\mathbf h$ para todo desplazamiento $\mathbf h$. La definición vectorial se expresa aquí en una base ortonormal; la identificación usa el producto escalar euclídeo.

[]{#fispm-t1-c13-d0003}

**Definición 13.3 --- Campo de fuerza con potencial.** Un campo de posición $\mathbf F:\Omega\to\mathbb R^d$ tiene potencial $U$ cuando $\mathbf F=-\nabla U$ en $\Omega$. La función debe estar definida como un valor único en cada punto del dominio. Una expresión que cambia al rodear un agujero no constituye todavía un potencial global.

[]{#fispm-t1-c13-p0004}

**Proposición 13.4 --- Trabajo de un campo potencial sobre una curva.** Si $\mathbf F=-\nabla U$, el trabajo a lo largo de cualquier curva $\boldsymbol\gamma:[a,b]\to\Omega$ de clase $C^1$ por tramos es

$$\int_a^b\mathbf F(\boldsymbol\gamma(s))\cdot\boldsymbol\gamma'(s)ds=U(\boldsymbol\gamma(a))-U(\boldsymbol\gamma(b)).$$

**Demostración.** En cada tramo, la regla de la cadena da $dU(\boldsymbol\gamma(s))/ds=\nabla U(\boldsymbol\gamma(s))\cdot\boldsymbol\gamma'(s)$. Sustituir $\mathbf F=-\nabla U$ e integrar produce la diferencia. Al sumar los tramos se cancelan los valores intermedios. $\square$

No se exige que la curva sea una solución de Newton para calcular esa integral. Una fuerza puede evaluarse sobre un recorrido de prueba; sólo al discutir la evolución de una partícula se requiere la ecuación dinámica. Esta separación permite comparar caminos y comprobar propiedades del campo sin introducir un agente que obligue físicamente a realizar cada recorrido.

Para un desplazamiento pequeño $\mathbf h$, la diferenciabilidad expresa $U(\mathbf x+\mathbf h)-U(\mathbf x)=\nabla U(\mathbf x)\cdot\mathbf h+o(|\mathbf h|)$. El trabajo infinitesimal del campo tiene el signo opuesto. En un punto con gradiente no nulo, la dirección de mayor aumento del potencial es $\nabla U/|\nabla U|$: el producto con un vector unitario alcanza su máximo por Cauchy--Schwarz. La fuerza apunta hacia el descenso más pronunciado del potencial.

Si una curva permanece en un nivel $U=C$, derivarla da $\nabla U\cdot\boldsymbol\gamma'=0$. Allí el campo potencial es perpendicular a sus direcciones tangentes, cuando el gradiente no se anula. Este hecho geométrico no significa que toda trayectoria dinámica siga la dirección de la fuerza ni que deba permanecer en un nivel. La velocidad tiene sus propios datos iniciales; la fuerza gobierna su aceleración.

El gradiente cartesiano tampoco se obtiene derivando respecto de cualquier parámetro sin corregir la métrica. Si describimos una curva por $q$, entonces $dU/dq=\nabla U\cdot d\mathbf r/dq$, que es una proyección ponderada por la parametrización. No es automáticamente una componente cartesiana de fuerza. Reservaremos las coordenadas generalizadas y su formulación sistemática para su lugar posterior.

[]{#fispm-t1-c13-mp0003}

**Principio metodológico 13.3 --- Comprobar todas las componentes.** Para verificar un potencial, deriva respecto de cada coordenada y compara $-\partial_iU$ con $F_i$. Para calcular trabajo sobre una curva usa la parametrización completa o la diferencia de potencial ya justificada. No conviertas la dirección de fuerza en una afirmación sobre la dirección de velocidad.

[]{#ejercicios-2}

### Ejercicios {#fispm-c13-ejercicios-2}

[]{#fispm-t1-c13-e0005}

**Ejercicio 13.5.** En el plano, sea $U(x,y)=kx^2/2+\alpha xy+ky^2/2$, con constantes de unidades adecuadas. Obtén el campo y el trabajo desde $(0,0)$ hasta $(a,b)$ por cualquier curva contenida en el plano. ¿Es necesario que ese punto sea alcanzado por una partícula inicialmente en reposo en el origen?

**Solución.** El campo es $\mathbf F=(-kx-\alpha y,-\alpha x-ky)$. Proposición 13.4 da $W=-[k(a^2+b^2)/2+\alpha ab]$. El resultado es válido para cualquier recorrido de prueba entre los extremos. La fuerza en el origen es cero. Con datos de reposo allí, Newton admite la solución constante; como el campo es lineal y localmente Lipschitz, esa solución es única. Por tanto, un extremo distinto no se alcanza desde esos datos sin otra acción. Calcular trabajo entre posiciones no suministra una trayectoria espontánea.

[]{#fispm-t1-c13-e0006}

**Ejercicio 13.6.** Sea $U(x,y)=A(x^2+y^2)$, con $A>0$. Calcula la fuerza, el trabajo sobre una vuelta circular de radio $R$ y el trabajo sobre un tramo radial de radio $R$ a radio $2R$.

**Solución.** La fuerza es $-2A(x,y)$, radial hacia el origen. Una vuelta circular mantiene $U=AR^2$ y realiza trabajo cero; también puede comprobarse porque fuerza y tangente son perpendiculares. En el tramo radial, el trabajo es $AR^2-4AR^2=-3AR^2$. La fuerza realiza trabajo negativo cuando aumenta el radio. La diferencia no exige reconstruir el tiempo, pero tampoco decide si una partícula con datos concretos llega a $2R$. Una trayectoria circular bajo esa fuerza requiere además que su aceleración normal coincida con $-2A\mathbf r/m$.

[]{#independencia-del-camino-y-circulación}

[]{#fispm-t1-c13-s04}

[]{#fpm-i-13-s04}

## 4. Independencia del camino y circulación {#fispm-c13-independencia-del-camino-y-circulaciuxf3n}

Un campo potencial realiza el mismo trabajo sobre todos los caminos que comparten extremos. La recíproca también es verdadera bajo condiciones elementales de dominio y continuidad. Probarla muestra qué significa construir un potencial a partir del trabajo: la integral elegida no puede guardar una dependencia oculta del camino.[^4]

[]{#fig:I-13-N02}

<figure id="fig-fpm-v04-i-13-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-13-N02.svg" class="lightbox" data-gallery="fpm-v04-c13"><img src="/assets/books/fispm/v04/I-13-N02.svg" alt="Dos caminos, un trabajo. Diagrama del capítulo 13; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="332" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 13.1.** Para $F=-\nabla U$, los dos caminos con extremos $a,b$ dan $W=U(a)-U(b)$. La igualdad requiere un potencial definido en el dominio considerado. Véase §[4](#fispm-c13-independencia-del-camino-y-circulaciuxf3n).

</figcaption>

</figure>

Tomemos un abierto $\Omega\subset\mathbb R^d$ conectado por caminos $C^1$ por tramos y un campo continuo $\mathbf F$. Cada curva considerada queda íntegramente dentro de $\Omega$. La integral conserva la orientación; invertirla cambia el signo, y concatenar recorridos suma sus trabajos, como se probó en el capítulo 12.

[]{#fispm-t1-c13-d0004}

**Definición 13.4 --- Campo conservativo y circulación.** El campo es conservativo en $\Omega$ si su integral entre cualesquiera dos puntos no depende del camino $C^1$ por tramos que los une. La circulación es la integral $\oint\mathbf F\cdot d\mathbf r$ sobre una curva cerrada orientada.

Aquí «conservativo» describe un campo de posición en un dominio. No se usa como sinónimo de cualquier fuerza que en una historia particular efectúe trabajo cero. Un campo puede tener circulación cero sobre un lazo y distinta de cero sobre otro. La definición exige comparar todos los caminos pertinentes.

[]{#fispm-t1-c13-p0005}

**Proposición 13.5 --- Equivalencias globales de conservatividad.** Para el campo continuo anterior, son equivalentes: independencia del camino; circulación cero sobre toda curva cerrada $C^1$ por tramos; existencia de un potencial $U\in C^1(\Omega)$ con $\mathbf F=-\nabla U$.

**Demostración.** Si el trabajo es independiente del camino, toda curva cerrada puede compararse con el recorrido constante en su punto inicial; ambas tienen los mismos extremos y éste tiene integral cero. Así se anula toda circulación.

Si toda circulación es cero, tomemos dos caminos $\gamma_1,\gamma_2$ entre los mismos extremos. Concatenar $\gamma_1$ con el inverso de $\gamma_2$ da un lazo, cuya integral es $W_1-W_2=0$. Por tanto, sus trabajos coinciden.

Con independencia del camino, fijemos $\mathbf x_0\in\Omega$ y definamos $U(\mathbf x)=U_0-\int_{\mathbf x_0}^{\mathbf x}\mathbf F\cdot d\mathbf r$. El valor está bien definido. Alrededor de cualquier $\mathbf x$ hay una bola contenida en $\Omega$. Para $h$ pequeño, podemos prolongar un camino hasta $\mathbf x$ con el segmento a $\mathbf x+h\mathbf e_i$; por independencia,

$$U(\mathbf x+h\mathbf e_i)-U(\mathbf x)=-\int_0^h F_i(\mathbf x+s\mathbf e_i)ds.$$

Dividir por $h$ y usar continuidad da $\partial_iU=-F_i$. Como esas parciales son continuas, $U$ es $C^1$ y su gradiente es $-\mathbf F$. Finalmente, un campo con potencial tiene integral determinada por sus extremos por la proposición 13.4. $\square$

La prueba no necesita que $\Omega$ sea convexo ni que no tenga agujeros: exige anulación de todas las circulaciones. La forma del dominio será decisiva cuando intentemos reemplazar esa condición global por un examen local de derivadas. No todas las curvas cerradas de una región perforada se reducen a pequeños recorridos alrededor de puntos ordinarios.

[]{#fispm-t1-c13-p0006}

**Proposición 13.6 --- Unicidad del potencial en un dominio conectado.** Dos potenciales $C^1$ del mismo campo en $\Omega$ difieren en una constante.

**Demostración.** Si $U$ y $V$ generan el mismo campo, $\nabla(V-U)=0$. Conectemos dos puntos por un camino permitido. La regla de la cadena da derivada cero de $V-U$ a lo largo de cada tramo, de modo que sus valores en los extremos coinciden. Como los puntos eran arbitrarios, la diferencia es constante. $\square$

El dominio conectado permite propagar la constante por caminos. Para un dominio desconectado, el enunciado se aplica en cada componente conectada por caminos. No hay una condición local de fuerza que fije la diferencia entre constantes de componentes separadas.

[]{#fispm-t1-c13-mp0004}

**Principio metodológico 13.4 --- Distinguir un ejemplo de una propiedad global.** Una circulación no nula basta para refutar conservatividad. Una circulación nula aislada no basta para probarla. Para afirmar que existe potencial, construye uno y verifica su gradiente, o acredita la independencia del camino con un argumento válido en todo el dominio.

[]{#ejercicios-3}

### Ejercicios {#fispm-c13-ejercicios-3}

[]{#fispm-t1-c13-e0007}

**Ejercicio 13.7.** En el plano, considera $\mathbf F(x,y)=\kappa(-y,x)$, con $\kappa\ne0$. Calcula su circulación antihoraria sobre una circunferencia de radio $R>0$ y decide si existe un potencial global.

**Solución.** Parametrizamos $\mathbf r(\theta)=R(\cos\theta,\sin\theta)$, para $0\leq\theta\leq2\pi$. Entonces $\mathbf F=\kappa R(-\sin\theta,\cos\theta)$ y $d\mathbf r/d\theta=R(-\sin\theta,\cos\theta)$. El producto vale $\kappa R^2$; integrar da $2\pi\kappa R^2\ne0$. Por proposición 13.5 no existe potencial global en el plano. Una trayectoria radial podría tener trabajo cero para este campo; eso no anula la circulación que acabamos de calcular ni rescata la propiedad global.

[]{#fispm-t1-c13-e0008}

**Ejercicio 13.8.** Un campo continuo tiene circulación cero sobre toda curva cerrada dentro de un dominio conectado. Se fija $U(\mathbf x_0)=7\,\mathrm J$ y el trabajo desde $\mathbf x_0$ a $\mathbf a$ es $3\,\mathrm J$. Desde $\mathbf a$ a $\mathbf b$ es $-2\,\mathrm J$. Calcula ambos potenciales y el trabajo directo de $\mathbf x_0$ a $\mathbf b$.

**Solución.** proposición 13.5 garantiza que la construcción es independiente del camino. Resulta $U(\mathbf a)=7-3=4\,\mathrm J$ y $U(\mathbf b)=4-(-2)=6\,\mathrm J$. Por concatenación y conservatividad, el trabajo directo es $3-2=1\,\mathrm J$, igual a $U(\mathbf x_0)-U(\mathbf b)$. El valor $7$ fija una convención; elegir $0$ desplazaría ambos potenciales en $-7\,\mathrm J$ y mantendría todos los trabajos.

[]{#integrabilidad-local-y-dominios-estrellados}

[]{#fispm-t1-c13-s05}

[]{#fpm-i-13-s05}

## 5. Integrabilidad local y dominios estrellados {#fispm-c13-integrabilidad-local-y-dominios-estrellados}

Buscar una función cuyo gradiente sea un campo dado plantea una condición de compatibilidad: las derivadas parciales cruzadas de la función deben coincidir. Esa condición produce una prueba rápida para refutar potenciales y, en dominios adecuados, permite construirlos. Mantendremos explícita la hipótesis geométrica necesaria para la construcción global.[^5]

[]{#fispm-t1-c13-p0007}

**Proposición 13.7 --- Condición necesaria de derivadas cruzadas.** Si $\mathbf F\in C^1(\Omega)$ admite un potencial $U\in C^1(\Omega)$, entonces

$$\partial_jF_i=\partial_iF_j\qquad\text{para todo }i,j.$$

**Demostración.** Puesto que $\partial_iU=-F_i$ y cada $F_i$ es $C^1$, las primeras parciales de $U$ son $C^1$ y $U$ es $C^2$. La igualdad de parciales mixtas continuas da $\partial_j\partial_iU=\partial_i\partial_jU$. Cambiar sus signos produce la identidad para el campo. $\square$

En el plano sólo hay una condición independiente: $\partial_yF_x=\partial_xF_y$. En tres dimensiones hay tres comparaciones independientes. Constituyen el contenido coordenado de rotacional nulo, pero aquí no necesitamos desarrollar ese operador ni sus teoremas integrales. La condición se formula para un campo $C^1$ en el dominio declarado; no se evalúa en un punto singular donde el campo no existe.

[]{#fispm-t1-c13-d0005}

**Definición 13.5 --- Dominio estrellado.** Un conjunto abierto $\Omega$ es estrellado respecto de $\mathbf a\in\Omega$ si, para cada $\mathbf x\in\Omega$, todo el segmento $\mathbf a+t(\mathbf x-\mathbf a)$, $0\leq t\leq1$, pertenece a $\Omega$.

Un abierto convexo es estrellado respecto de cualquiera de sus puntos. Una bola es el ejemplo local más simple. La condición no exige que todos los pares de puntos estén unidos por su segmento recto: basta un centro común desde el cual los segmentos permanezcan dentro. La geometría requerida será exactamente la que permite integrar radialmente sin atravesar zonas excluidas.

[]{#fispm-t1-c13-p0008}

**Proposición 13.8 --- Construcción de potencial en un dominio estrellado.** Sea $\Omega$ abierto y estrellado respecto de $\mathbf a$, y sea $\mathbf F\in C^1(\Omega)$ con las igualdades de la proposición 13.7. Entonces

$$U(\mathbf x)=U_0-\int_0^1\mathbf F(\mathbf a+t(\mathbf x-\mathbf a))\cdot(\mathbf x-\mathbf a)\,dt$$

es un potencial global $C^1$ de $\mathbf F$ en $\Omega$, con $U(\mathbf a)=U_0$.

**Demostración.** Pongamos $\mathbf h=\mathbf x-\mathbf a$ y $V=U_0-U$. El segmento de integración queda en el dominio. Para $\mathbf x$ fijo, ese segmento es compacto y está contenido en el abierto; un pequeño cambio de $\mathbf x$ mantiene todos los puntos de integración dentro de un entorno compacto del dominio. La continuidad de las primeras derivadas de $\mathbf F$ justifica diferenciar bajo la integral en ese entorno.

Para la coordenada $j$ obtenemos

$$\partial_jV=\int_0^1\left[F_j(\mathbf a+t\mathbf h)+t\sum_i h_i\partial_jF_i(\mathbf a+t\mathbf h)\right]dt.$$

Las igualdades cruzadas reemplazan $\partial_jF_i$ por $\partial_iF_j$. El integrando se vuelve $d[tF_j(\mathbf a+t\mathbf h)]/dt$. Integrar entre $0$ y $1$ da $\partial_jV=F_j(\mathbf x)$, porque el término en $t=0$ se anula. Así, $\partial_jU=-F_j$ para cada $j$, y las parciales son continuas. En $\mathbf x=\mathbf a$, el vector $\mathbf h$ es cero y la integral se anula, por lo que $U(\mathbf a)=U_0$. $\square$

La prueba permite una conclusión local en cualquier abierto: alrededor de cada punto hay una bola contenida en él. Si el campo es $C^1$ y cumple las igualdades cruzadas, proposición 13.8 construye un potencial en esa bola. Para que esas construcciones formen una sola función en todo el dominio, todavía debemos comprobar compatibilidad global. El próximo ejemplo mostrará por qué no basta afirmar que todas las bolas funcionan.

Una práctica habitual de integración por componentes también debe conservar las funciones aún desconocidas. Si $-\partial_xU=F_x$, integrar en $x$ deja una función de las otras coordenadas, no simplemente una constante numérica. Comparar después las componentes restantes determina esa función o revela incompatibilidad.

[]{#fispm-t1-c13-mp0005}

**Principio metodológico 13.5 --- Separar compatibilidad y dominio.** Comprueba primero regularidad e igualdades cruzadas. Si buscas suficiencia global, identifica una condición de dominio que la justifique o verifica un potencial explícito. Al integrar una componente conserva las funciones de las variables restantes hasta compararlas con las demás fuerzas.

[]{#ejercicios-4}

### Ejercicios {#fispm-c13-ejercicios-4}

[]{#fispm-t1-c13-e0009}

**Ejercicio 13.9.** En $\mathbb R^2$, sea $\mathbf F=(-2\alpha x-\beta y,-\beta x-2\gamma y)$. Comprueba la condición de integrabilidad y construye un potencial sin usar la fórmula radial completa.

**Solución.** Las parciales cruzadas valen ambas $-\beta$ y el plano es estrellado. La primera componente exige $\partial_xU=2\alpha x+\beta y$, así que $U=\alpha x^2+\beta xy+h(y)$. La segunda exige $\partial_yU=\beta x+2\gamma y$, de donde $h'(y)=2\gamma y$ y $h(y)=\gamma y^2+C$. Por tanto, $U=\alpha x^2+\beta xy+\gamma y^2+C$. Diferenciar las dos componentes verifica el campo. No se ha supuesto que $\alpha$ o $\gamma$ sean positivos: la existencia de potencial no es todavía una afirmación sobre estabilidad.

[]{#fispm-t1-c13-e0010}

**Ejercicio 13.10.** En el plano, sea $\mathbf F=(Ay,Bx)$, con $A,B$ constantes. Decide cuándo existe potencial y calcula la circulación sobre el rectángulo antihorario de vértices $(0,0),(L,0),(L,H),(0,H)$, con $L,H>0$.

**Solución.** Las derivadas cruzadas son $A$ y $B$, por lo que proposición 13.7 exige $A=B$. Si coinciden, $U=-Axy+C$ verifica ambas componentes. En el rectángulo, el tramo inferior da cero, el derecho $BLH$, el superior $-ALH$ y el izquierdo cero. La circulación es $(B-A)LH$. Si $A\ne B$, refuta el potencial por la proposición 13.5 y confirma la incompatibilidad diferencial. Si $A=B$, no usamos sólo ese lazo para probar conservatividad: la demuestra el potencial explícito o proposición 13.8 en todo el plano.

[]{#obstrucciones-globales-y-dominios-perforados}

[]{#fispm-t1-c13-s06}

[]{#fpm-i-13-s06}

## 6. Obstrucciones globales y dominios perforados {#fispm-c13-obstrucciones-globales-y-dominios-perforados}

La información diferencial describe el campo cerca de cada punto ordinario. Una integral cerrada puede explorar la forma completa del dominio y rodear una región excluida. Para entender la diferencia, estudiaremos un campo que admite potencial en cada entorno pequeño pero no en todo el plano perforado. El cálculo directo evita atribuirle una contradicción a las derivadas cruzadas.[^6]

[]{#fig:I-13-R02}

<figure id="fig-fpm-v04-i-13-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-13-R02.svg" class="lightbox" data-gallery="fpm-v04-c13"><img src="/assets/books/fispm/v04/I-13-R02.svg" alt="El dominio perforado conserva una obstrucción. Diagrama del capítulo 13; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="399" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 13.2.** En $\mathbb R^2\setminus\{0\}$, el campo $F=(-y,x)/(x^2+y^2)$ tiene rotacional nulo localmente y circulación $2\pi$ en un círculo positivo. No admite allí un potencial escalar global monovaluado. Véase §[6](#fispm-c13-obstrucciones-globales-y-dominios-perforados).

</figcaption>

</figure>

[]{#fig:I-13-N03}

<figure id="fig-fpm-v04-i-13-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-13-N03.svg" class="lightbox" data-gallery="fpm-v04-c13"><img src="/assets/books/fispm/v04/I-13-N03.svg" alt="Un dominio con agujero. Diagrama del capítulo 13; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="350" height="302" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 13.3.** El campo $F=(-y,x)/(x^2+y^2)$ tiene circulación $2\pi$ sobre un círculo orientado positivamente. Su rotacional local nulo fuera del origen no basta para producir un potencial global. Véase §[6](#fispm-c13-obstrucciones-globales-y-dominios-perforados).

</figcaption>

</figure>

[]{#fispm-t1-c13-d0006}

**Definición 13.6 --- Potencial local.** Un campo tiene potencial local alrededor de $\mathbf x$ si existe un abierto $V\subset\Omega$ que contiene $\mathbf x$ y una función $U_V\in C^1(V)$ con $\mathbf F=-\nabla U_V$ en $V$. Tiene potencial global si una única función cumple esa relación en todo $\Omega$.

La existencia global implica la local por restricción. Proposición 13.8 muestra que las igualdades cruzadas bastan para la existencia local de un campo $C^1$. La implicación inversa puede fallar, incluso en un dominio conectado donde el campo es suave en todos sus puntos. La singularidad no necesita pertenecer al dominio para afectar qué lazos están disponibles dentro de él.

[]{#fispm-t1-c13-p0009}

**Proposición 13.9 --- Campo localmente potencial sin potencial global.** En $\Omega=\mathbb R^2\setminus\{(0,0)\}$, el campo

$$\mathbf F(x,y)=A\left(-\frac{y}{x^2+y^2},\frac{x}{x^2+y^2}\right),\qquad A\ne0,$$

es suave y cumple las igualdades cruzadas, pero no admite potencial global.

**Demostración.** El denominador es positivo en $\Omega$, así que ambas componentes son suaves. Con $r^2=x^2+y^2$,

$$\partial_yF_x=A\frac{y^2-x^2}{r^4},\qquad\partial_xF_y=A\frac{y^2-x^2}{r^4}.$$

Las derivadas coinciden. Sin embargo, sobre $\mathbf r(\theta)=R(\cos\theta,\sin\theta)$, $R>0$, el campo es $(A/R)(-\sin\theta,\cos\theta)$ y la derivada de la curva es $R(-\sin\theta,\cos\theta)$. Su producto es $A$, por lo que la circulación antihoraria vale $2\pi A\ne0$. Proposición 13.5 excluye un potencial global. En una bola suficientemente pequeña alrededor de cada punto del dominio, proposición 13.8 sí produce uno local. $\square$

El campo sólo tiene sentido donde el origen está excluido. No cumple la hipótesis de un dominio estrellado respecto de un punto de $\Omega$: para cualquier centro elegido, hay un punto al otro lado del origen cuyo segmento de unión lo atraviesa. Por tanto, proposición 13.8 no prometía una construcción global allí. El cálculo de circulación detecta precisamente lo que la prueba radial no podía atravesar.

En una región donde se elige un ángulo continuo $\theta$, el campo es $A\nabla\theta$ y un potencial local es $U=-A\theta+C$. La expresión angular explica el problema: dar una vuelta modifica una determinación continua del ángulo en $2\pi$, aunque se regrese a la misma posición. Una función de estado global debe retornar al mismo valor en ese punto. Tratar el ángulo como un número real monovaluado en todo el plano perforado incumple esa exigencia.

Si retiramos del plano un semieje y elegimos una rama del ángulo, obtenemos un dominio distinto con potencial $-A\theta$. Los caminos que cruzaban el corte dejan de estar permitidos en esa representación. No se ha demostrado que el campo original sea globalmente conservativo: se ha restringido la región en la que se trabaja. Diferentes ramas pueden coincidir salvo constantes sobre componentes de intersección, pero eso no garantiza que se unan coherentemente al rodear el agujero.

No toda región perforada obliga a que todo campo falle. El campo $\mathbf G=-k(x,y)$ sigue teniendo potencial $k(x^2+y^2)/2$ al restringirlo al mismo plano perforado. El dominio hace posible una obstrucción; la circulación del campo decide si ocurre. La mera presencia de un agujero no refuta un potencial explícito bien definido.

[]{#fispm-t1-c13-mp0006}

**Principio metodológico 13.6 --- Conservar el dominio durante la prueba.** Examina qué puntos están excluidos y qué lazos siguen permitidos. No cruces una singularidad para aplicar una fórmula ni conviertas una rama angular en función global. Usa una circulación no nula para refutar el potencial, y un potencial monovaluado verificado para acreditarlo.

[]{#ejercicios-5}

### Ejercicios {#fispm-c13-ejercicios-5}

[]{#fispm-t1-c13-e0011}

**Ejercicio 13.11.** Para el campo de la proposición 13.9, calcula el trabajo desde $(R,0)$ hasta $(-R,0)$ por el semicírculo superior y por el inferior, con ambos recorridos orientados desde el primer punto al segundo. Interpreta su diferencia.

**Solución.** En el semicírculo superior, el ángulo crece de $0$ a $\pi$ y $\mathbf F\cdot d\mathbf r=A\,d\theta$, así que $W_+=A\pi$. En el inferior puede elegirse el ángulo desde $0$ hasta $-\pi$, con $W_-=-A\pi$. La diferencia es $2\pi A$. Concatenar el camino superior con el inverso del inferior da una vuelta antihoraria completa. Los dos extremos coinciden entre recorridos, pero el trabajo no: falla independencia del camino. Ningún valor único $U(-R,0)$ puede reproducir las dos diferencias desde el mismo $U(R,0)$.

[]{#fispm-t1-c13-e0012}

**Ejercicio 13.12.** Restringe el campo de la proposición 13.9 al semiplano $x>0$. Construye un potencial y verifica sus dos derivadas. Explica por qué su existencia no contradice proposición 13.9.

**Solución.** En ese semiplano puede elegirse $\theta=\arctan(y/x)$, con valores entre $-\pi/2$ y $\pi/2$. Sus derivadas son $\partial_x\theta=-y/(x^2+y^2)$ y $\partial_y\theta=x/(x^2+y^2)$. Así, $U=-A\arctan(y/x)+C$ satisface $-\nabla U=\mathbf F$. El semiplano es convexo y proposición 13.8 también garantiza la construcción. No contiene una vuelta alrededor del origen ni los dos semicírculos completos del ejercicio 13.11. La propiedad acreditada se refiere al dominio restringido, mientras proposición 13.9 excluye un potencial global en un dominio mayor con otros caminos permitidos.

[]{#conservación-de-la-energía-mecánica}

[]{#fispm-t1-c13-s07}

[]{#fpm-i-13-s07}

## 7. Conservación de la energía mecánica {#fispm-c13-conservaciuxf3n-de-la-energuxeda-mecuxe1nica}

El potencial permite reescribir el teorema trabajo--energía como una cantidad constante cuando la fuerza total proviene de él. La conservación es una consecuencia de Newton y de la forma del campo. Su uso puede reducir el cálculo de rapidez, pero conserva los límites del balance escalar establecidos en el capítulo 12: no determina por sí solo dirección, contacto ni trayectoria.[^7]

[]{#fispm-t1-c13-d0007}

**Definición 13.7 --- Energía mecánica de una partícula en un potencial.** Para una partícula de masa constante $m>0$ en un marco inercial y un potencial de posición $U$, definimos

$$E=K+U=\frac12m|\mathbf v|^2+U(\mathbf r).$$

La energía mecánica corresponde a las contribuciones representadas por ese $U$ y a la energía cinética del modelo. No incluye automáticamente temperatura, deformaciones no modeladas, energía química o cualquier reserva energética de un agente externo.

[]{#fispm-t1-c13-p0010}

**Proposición 13.10 --- Conservación con fuerza potencial y reacción sin potencia.** Supongamos que una trayectoria $C^2$ cumple Newton con fuerza total $-\nabla U(\mathbf r)+\mathbf R$, donde $U\in C^1(\Omega)$ no depende del tiempo y $\mathbf R\cdot\mathbf v=0$ a lo largo de la historia. Entonces $E$ es constante mientras esas hipótesis se mantienen.

**Demostración.** La derivada de $K$ es $m\mathbf a\cdot\mathbf v$, por la proposición 12.4. Sustituir Newton da $dK/dt=-\nabla U\cdot\mathbf v+\mathbf R\cdot\mathbf v=-\nabla U\cdot\mathbf v$. La regla de la cadena produce $dU(\mathbf r(t))/dt=\nabla U\cdot\mathbf v$. Al sumar, $dE/dt=0$; integrar mantiene el mismo valor en todo el intervalo. $\square$

El caso sin reacción se obtiene con $\mathbf R=0$. Una guía fija lisa puede satisfacer la hipótesis de potencia nula; una guía móvil requiere comprobarla y no se incluye automáticamente. El teorema tampoco afirma que la reacción sea un campo potencial. Puede variar con la rapidez y el estado de contacto, pero no aporta potencia durante el régimen probado.

Cambiar $U$ por $U+C$ cambia el valor de la constante $E$ en el mismo $C$. Las diferencias y la conservación permanecen iguales. La afirmación física no es que exista un cero absoluto de energía mecánica en esta descripción, sino que su variación es nula bajo las hipótesis.

De $E=K+U$ se deduce $K=E-U\geq0$. Una posición con $U>E$ no puede pertenecer a esa historia. En una dimensión, $v^2=2(E-U)/m$ permite calcular la rapidez donde se alcanza una posición. En varias dimensiones determina el módulo de velocidad, no sus componentes. Y aun en una dimensión un punto con $U\leq E$ puede pertenecer a otra componente permitida, o no alcanzarse en tiempo finito desde los datos iniciales.

La igualdad $U=E$ da reposo instantáneo para una partícula en este modelo. Para decidir si hay retorno o equilibrio se necesita la fuerza y la continuación de Newton. No conviene llamar a todo punto de igualdad «punto de retorno» sin esa comprobación. El segundo macrotramo analizará la estructura de regiones accesibles y las barreras con esas distinciones.

La conservación de energía y la conservatividad del campo tampoco son definiciones intercambiables. Proposición 13.5 es una propiedad de todos los caminos del dominio para un campo de posición. Proposición 13.10 es una propiedad de una historia dinámica sometida a ciertas fuerzas. Una fuerza dependiente de velocidad y perpendicular a ella puede no aportar potencia y mantener $K$ constante sin ser un campo conservativo de posición en el sentido de la definición 13.4.

[]{#fispm-t1-c13-mp0007}

**Principio metodológico 13.7 --- Derivar la cantidad conservada del modelo.** Antes de escribir $E_a=E_b$, identifica el potencial, verifica su independencia temporal y suma las fuerzas restantes. Justifica sus potencias nulas. Usa $E-U$ para rapidez y exclusiones, conservando los datos direccionales y las condiciones de alcance que el escalar no fija.

[]{#ejercicios-6}

### Ejercicios {#fispm-c13-ejercicios-6}

**Ejercicio 13.13.** Una partícula se lanza desde $y=0$ con velocidad inicial $(3,4)\,\mathrm{m/s}$ bajo gravedad uniforme, con $g=10\,\mathrm{m/s^2}$ y sin resistencia. Compara el límite de altura obtenido sólo de $K\geq0$ con la altura máxima real. ¿Por qué son distintos?

**Solución.** Con $U=mgy$, la energía inicial es $25m/2$ y el balance da $v^2=25-20y$. La no negatividad sólo exige $y\leq1{,}25\,\mathrm m$. Pero Newton horizontal da $v_x=3$ constante y la detención vertical ocurre cuando $v_y=4-10t=0$, en $t=0{,}4\,\mathrm s$. La altura es $y=4t-5t^2=0{,}8\,\mathrm m$. Allí la rapidez es $3\,\mathrm{m/s}$ y $K=9m/2$, de modo que no se anula. El límite escalar $1{,}25$ ignora la energía cinética horizontal que no puede convertirse en altura bajo este campo. Es una condición necesaria más débil, no una predicción de alcance.

[]{#fispm-t1-c13-e0014}

**Ejercicio 13.14.** Una partícula de masa $m$ permanece en una guía fija lisa del plano. Sobre ella actúan el peso y una fuerza horizontal $F_x=-kx$. La guía une $A=(0,h)$ y $B=(L,0)$, con $h,L>0$. Si en $A$ tiene rapidez $v_a$, calcula la rapidez candidata en $B$. Explica qué no queda demostrado por esa fórmula.

**Solución.** Las fuerzas tienen potencial total $U(x,y)=kx^2/2+mgy$. La reacción hace potencia cero por el carácter fijo y liso de la guía, mientras se mantiene el contacto. Proposición 13.10 da $mv_b^2/2+kL^2/2=mv_a^2/2+mgh$, de donde $v_b^2=v_a^2+2gh-kL^2/m$. No añadimos nuevamente el trabajo del peso: ya está representado por $mgy$. El radicando debe ser no negativo, pero eso no prueba que se alcance $B$. La forma intermedia de la guía puede exigir pasar por potenciales mayores que $E$, y la reacción puede tener un signo incompatible con un contacto unilateral. Tampoco se ha obtenido el tiempo de viaje ni la dirección final de velocidad; requieren la geometría y Newton.

[]{#fuerzas-adicionales-y-potenciales-temporales}

[]{#fispm-t1-c13-s08}

[]{#fpm-i-13-s08}

## 8. Fuerzas adicionales y potenciales temporales {#fispm-c13-fuerzas-adicionales-y-potenciales-temporales}

La energía mecánica deja de ser constante cuando otras fuerzas aportan potencia o cuando el potencial cambia explícitamente con el tiempo. El balance sigue siendo útil: indica qué término modifica la cantidad $K+U$. Escribirlo evita aplicar conservación en un régimen donde un agente externo, una fricción o un soporte móvil intercambia energía con la partícula.[^8]

Primero consideremos un potencial autónomo $U(\mathbf r)$ y una fuerza adicional $\mathbf f$, que puede depender del tiempo, la velocidad o la historia de contacto. Toda contribución que no se haya incluido en $-\nabla U$ debe figurar en esa fuerza adicional, salvo que su potencia se haya acreditado como cero.

[]{#fispm-t1-c13-p0011}

**Proposición 13.11 --- Balance mecánico con fuerza adicional.** Si Newton toma la forma $m\mathbf a=-\nabla U+\mathbf f$, con masa constante y $U$ independiente del tiempo, entonces

$$\frac{dE}{dt}=\mathbf f\cdot\mathbf v,\qquad E_b-E_a=\int_{t_a}^{t_b}\mathbf f\cdot\mathbf v\,dt.$$

**Demostración.** Derivar $K$ y sustituir Newton da $dK/dt=-\nabla U\cdot\mathbf v+\mathbf f\cdot\mathbf v$. La regla de la cadena da $dU/dt=\nabla U\cdot\mathbf v$. Sumarlas cancela el término potencial. Integrar la identidad restante produce la diferencia de energías. $\square$

Una resistencia viscosa $\mathbf f=-b\mathbf v$, con $b>0$, da $dE/dt=-b|\mathbf v|^2\leq0$. La energía mecánica no aumenta, aunque puede haber instantes de derivada cero cuando la velocidad se anula. El balance no describe por sí solo adónde va esa energía en un modelo ampliado: para estudiar calentamiento habría que incluir el medio y las variables internas correspondientes.

En cambio, una fuerza adicional perpendicular a la velocidad da $dE/dt=0$ durante esa historia. Tener potencia nula no equivale a admitir un potencial de posición. El cálculo del balance distingue esa condición cinemática de las equivalencias globales de la proposición 13.5.

[]{#fispm-t1-c13-d0008}

**Definición 13.8 --- Potencial con dependencia temporal explícita.** Sea $U(\mathbf r,t)$ de clase $C^1$ en una región espacial y un intervalo temporal. El campo derivado a cada tiempo es $\mathbf F_c(\mathbf r,t)=-\nabla_{\mathbf r}U(\mathbf r,t)$, donde el gradiente deriva sólo las coordenadas espaciales, manteniendo $t$ fijo.

Para cada instante puede existir independencia espacial del camino, pero una historia atraviesa valores temporales diferentes. El trabajo sobre esa historia no se reduce en general a $U(\mathbf r_a,t_a)-U(\mathbf r_b,t_b)$. Una contribución temporal aparece al derivar la función compuesta.

[]{#fispm-t1-c13-p0012}

**Proposición 13.12 --- Balance con potencial temporal.** Si $m\mathbf a=-\nabla_{\mathbf r}U(\mathbf r,t)+\mathbf f$ y $E=K+U(\mathbf r,t)$, entonces

$$\frac{dE}{dt}=\partial_tU(\mathbf r,t)+\mathbf f\cdot\mathbf v.$$

En particular, el trabajo de la contribución potencial es $W_c=U_a-U_b+\int_{t_a}^{t_b}\partial_tU(\mathbf r(t),t)\,dt.$

**Demostración.** Newton y la derivada cinética dan $dK/dt=-\nabla_{\mathbf r}U\cdot\mathbf v+\mathbf f\cdot\mathbf v$. La regla de la cadena completa es $dU/dt=\nabla_{\mathbf r}U\cdot\mathbf v+\partial_tU$. Al sumar se obtiene la primera identidad. Para la segunda, se integra $\mathbf F_c\cdot\mathbf v=-dU/dt+\partial_tU$. $\square$

Un resorte con anclaje móvil sobre una línea tiene $U(x,t)=k[x-c(t)]^2/2$. Su fuerza es $-k[x-c(t)]$ y $\partial_tU=-k[x-c(t)]\dot c(t)$. La variación del anclaje modifica el balance incluso sin fricción. El soporte fijo corresponde a $\dot c=0$ y recupera la conservación bajo las otras condiciones habituales.

Aquí hay una libertad de referencia que requiere cuidado. Sumar una constante temporal $C(t)$ a $U$ no cambia la fuerza espacial, pero aumenta $dE/dt$ en $\dot C$ y también $\partial_tU$ en $\dot C$. La identidad sigue siendo correcta. Por eso no debe interpretarse un término temporal como una transferencia física sin especificar una referencia y un modelo coherentes. Con referencia fija, el movimiento de un anclaje sí aporta una dependencia física que puede contrastarse por trabajo.

[]{#fispm-t1-c13-mp0008}

**Principio metodológico 13.8 --- Conservar la derivada temporal completa.** Al calcular $dU/dt$, distingue el cambio debido al movimiento del receptor y el cambio explícito de parámetros o soportes. Incluye todas las fuerzas adicionales y fija la convención energética antes de interpretar intercambios. No llames conservación a un balance que contiene una potencia no nula.

[]{#ejercicios-7}

### Ejercicios {#fispm-c13-ejercicios-7}

[]{#fispm-t1-c13-e0015}

**Ejercicio 13.15.** Una masa horizontal cumple $m\ddot x=-kx-b\dot x$, con $k,b>0$. Define su energía mecánica y prueba que no aumenta. ¿Puede una historia no constante conservar exactamente esa energía en todo un intervalo?

**Solución.** Tomamos $E=m\dot x^2/2+kx^2/2$. Proposición 13.11 da $\dot E=-b\dot x^2\leq0$ y $E_b-E_a=-b\int_{t_a}^{t_b}\dot x^2dt$. Si $E$ fuese constante en todo el intervalo, la integral no negativa sería cero; por continuidad, $\dot x=0$ en cada instante. La historia sería constante, y Newton exigiría $kx=0$, es decir, $x=0$. Por tanto, ninguna historia no constante mantiene exactamente esa energía bajo el modelo. Un instante de velocidad cero sólo anula la tasa en ese instante y no demuestra conservación posterior.

[]{#fispm-t1-c13-e0016}

**Ejercicio 13.16.** Un resorte horizontal tiene anclaje $c(t)=Vt$, con $V\ne0$, y fuerza sobre la masa $F_s=-k[x-c(t)]$. Un agente adicional mantiene la deformación constante $q_0\ne0$, imponiendo $x(t)=Vt+q_0$ durante $0\leq t\leq T$. Calcula las fuerzas, los trabajos y $d(K+U)/dt$ con $U=k[x-c(t)]^2/2$.

**Solución.** La aceleración es cero, así que el agente debe ejercer $F_a=kq_0$, opuesto al resorte $F_s=-kq_0$. El desplazamiento del receptor es $VT$; por tanto, $W_s=-kq_0VT$ y $W_a=kq_0VT$. Su suma es cero y $K=mV^2/2$ permanece constante. También $U=kq_0^2/2$ es constante sobre la historia. Sin embargo, su derivada parcial temporal es $\partial_tU=-kq_0V$, que no se anula. Proposición 13.12 da $\dot E=-kq_0V+F_aV=0$. La diferencia total de potencial es cero, pero el resorte efectuó trabajo no nulo: la integral temporal es indispensable. Si se elimina el agente, la historia impuesta deja de satisfacer Newton y ya no puede usarse para predecir el movimiento espontáneo.

Las ocho secciones establecen cuándo existe una función potencial, cómo depende esa existencia del dominio y qué balance mecánico resulta. Las secciones siguientes estudiarán las regiones accesibles, los equilibrios y la estabilidad. Distinguirá mínimos de energía y estabilidad dinámica, y tratará los casos en que una segunda derivada nula o una dirección plana impiden una conclusión inmediata.

[]{#paisajes-de-energía-y-regiones-accesibles}

[]{#fispm-t1-c13-s09}

[]{#fpm-i-13-s09}

## 9. Paisajes de energía y regiones accesibles {#fispm-c13-paisajes-de-energuxeda-y-regiones-accesibles}

Una vez acreditada la conservación de $E=K+U$, el potencial permite excluir posiciones y separar regiones de movimiento. En una dimensión, su gráfica también indica dónde puede anularse la velocidad. Para interpretar esos puntos necesitamos distinguir pertenencia a una región permitida, llegada en tiempo finito y continuación dinámica. Son preguntas diferentes.[^9]

[]{#fig:I-13-N01}

<figure id="fig-fpm-v04-i-13-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-13-N01.svg" class="lightbox" data-gallery="fpm-v04-c13"><img src="/assets/books/fispm/v04/I-13-N01.svg" alt="Regiones accesibles. Diagrama del capítulo 13; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="391" height="251" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 13.4.** En el ejemplo normalizado $U=(x^2-1)^2$, la energía $E=1/2$ (discontinua) deja dos regiones permitidas separadas por una barrera. Sólo donde $U\le E$ puede ser no negativa la energía cinética. Véase §[9](#fispm-c13-paisajes-de-energuxeda-y-regiones-accesibles).

</figcaption>

</figure>

[]{#fispm-t1-c13-d0009}

**Definición 13.9 --- Región permitida por una energía.** Para un potencial autónomo $U$ en un intervalo $I$ y un valor $E$, llamamos región permitida al conjunto $\mathcal A_E=\{x\in I:U(x)\leq E\}$. Su interior energético es $\{U<E\}$, donde una historia con esa energía tiene rapidez no nula. La definición expresa una condición necesaria y no una promesa de alcance desde cualquier dato inicial.

[]{#fispm-t1-c13-p0013}

**Proposición 13.13 --- Restricción a la componente permitida inicial.** Una historia continua con energía conservada $E$ permanece en $\mathcal A_E$ y en la componente conectada de ese conjunto que contiene su posición inicial.

**Demostración.** De $K=E-U\geq0$ se deduce que cada posición pertenece a $\mathcal A_E$. La imagen de cualquier intervalo temporal entre el instante inicial y un instante posterior es conectada, porque la posición es continua. Esa imagen contiene ambas posiciones y está contenida en $\mathcal A_E$; por tanto, ambas pertenecen a la misma componente conectada. $\square$

Si dos regiones permitidas están separadas por una barrera donde $U>E$, una historia no puede saltar de una a otra en el modelo clásico continuo. Que en ambas exista un punto con potencial bajo no elimina la barrera intermedia. En varias dimensiones hay que buscar caminos permitidos alrededor de barreras; una sección de la gráfica por una sola línea puede ocultarlos.

En una rama con movimiento monótono, la dirección inicial fija el signo de $\dot x$. Para una rama hacia la derecha, el tiempo entre posiciones es $t_b-t_a=\sqrt{\frac m2}\int_{x_a}^{x_b}\frac{dx}{\sqrt{E-U(x)}}.$

Se obtiene de $\dot x=+\sqrt{2(E-U)/m}$ mientras el radicando es positivo. La integral puede converger o divergir al aproximarse a una frontera; no basta resolver $U(x_b)=E$.

[]{#fispm-t1-c13-p0014}

**Proposición 13.14 --- Llegada a un cero simple y aproximación a un cero cuadrático.** Supongamos $U\in C^2$ y una rama de Newton que avanza hacia $b$, con $E-U(x)>0$ para $a\leq x<b$. Si $U(b)=E$ y $U'(b)>0$, la rama llega a $b$ en tiempo finito y retorna hacia la izquierda. Si, en cambio, $E-U(x)$ es comparable con $(b-x)^2$ cerca de $b$, el tiempo de aproximación a $b$ es infinito.

**Demostración.** En el primer caso, la diferenciabilidad da $E-U(x)=U'(b)(b-x)+o(b-x)$. El integrando temporal es comparable con $(b-x)^{-1/2}$, cuya integral converge. La solución alcanza el límite $x=b,v=0$; como el campo de estados es $C^1$ y el punto está dentro del dominio, Newton prolonga la solución. Su aceleración allí es $-U'(b)/m<0$, de modo que la velocidad se vuelve negativa inmediatamente después. En el segundo caso, existen constantes positivas que acotan $E-U(x)$ por arriba y por abajo mediante múltiplos de $(b-x)^2$. El integrando es comparable con $1/(b-x)$, cuya integral diverge. Por tanto, ninguna llegada finita ocurre en esa rama. $\square$

La prueba del retorno usa la fuerza no nula, además de la ecuación energética. Un punto crítico con $U'=0$ necesita otro análisis. Una trayectoria puede acercarse indefinidamente a un equilibrio con velocidad decreciente sin llegar a él, aunque la posición límite pertenezca a la misma componente permitida. La región permitida contiene más información geométrica que temporal.

Las dos situaciones pueden aparecer en un mismo paisaje al variar la energía. En el potencial de dos pozos $a(x^2-b^2)^2$, energías por debajo de $ab^4$ separan los pozos. En el nivel exacto $E=ab^4$, la región permitida se conecta a través del origen, pero cerca de él $E-U=2ab^2x^2-ax^4$ tiene un cero cuadrático. Una rama que se dirige al origen tarda un tiempo infinito. Por encima de la barrera, el radicando allí es positivo y ese impedimento temporal desaparece. La conexión de conjuntos permitidos en el nivel crítico no acredita un cruce dinámico finito.

[]{#fispm-t1-c13-mp0009}

**Principio metodológico 13.9 --- Examinar la rama y el tiempo de llegada.** Identifica la componente permitida de los datos iniciales y conserva el sentido del movimiento mientras no haya reposo. En una frontera $U=E$, estudia el orden del cero y la fuerza antes de afirmar que hay retorno, llegada o equilibrio.

[]{#ejercicios-8}

### Ejercicios {#fispm-c13-ejercicios-8}

[]{#fispm-t1-c13-e0017}

**Ejercicio 13.17.** Sea $U(x)=a(x^2-b^2)^2$, con $a,b>0$. Para $0<E<ab^4$, describe las componentes permitidas y decide si una partícula inicialmente en el pozo derecho puede pasar al izquierdo sin cambiar su energía.

**Solución.** La condición es $|x^2-b^2|\leq\sqrt{E/a}$. Como $\sqrt{E/a}<b^2$, definamos $r_-=\sqrt{b^2-\sqrt{E/a}}$ y $r_+=\sqrt{b^2+\sqrt{E/a}}$. La región permitida es $[-r_+,-r_-]\cup[r_-,r_+]$. El origen queda excluido porque $U(0)=ab^4>E$. Proposición 13.13 impide pasar entre componentes. Las cuatro fronteras tienen pendiente no nula y, desde una rama dirigida a ellas, son retornos de tiempo finito. La descripción energética no elimina la necesidad de fijar el signo inicial de velocidad.

[]{#fispm-t1-c13-e0018}

**Ejercicio 13.18.** Para $U(x)=kx^2/2$, una partícula de masa $m$ pasa por $x=0$ hacia la derecha con rapidez $v_0>0$. Encuentra el primer extremo derecho y calcula su tiempo de llegada mediante la integral de energía.

**Solución.** La energía es $mv_0^2/2$, así que $b=v_0\sqrt{m/k}$. La rapidez es $v_0\sqrt{1-x^2/b^2}$ sobre la rama de avance. La integral temporal da $t_*=(b/v_0)\int_0^1du/\sqrt{1-u^2}=(\pi/2)\sqrt{m/k}$. Como $U'(b)=kb>0$, proposición 13.14 garantiza el retorno. El cálculo determina este evento desde datos direccionales concretos; no usa sólo una igualdad entre energías finales.

[]{#fispm-t1-c13-e0019}

**Ejercicio 13.19.** Sea $U(x)=-cx^2$, con $c>0$, y energía $E=0$. Una partícula parte de $x_a<0$ hacia el origen. ¿Llega a $x=0$ en tiempo finito? Verifica una historia explícita.

**Solución.** Para $x<0$, la rama positiva de velocidad es $\dot x=\sqrt{2c/m}(-x)$. Si $\lambda=\sqrt{2c/m}$, su solución es $x(t)=x_a e^{-\lambda t}$ y $\dot x=-\lambda x>0$. La aceleración es $\lambda^2x$, que cumple $m\ddot x=2cx=-U'$. Su energía es cero y su límite es el origen, pero nunca lo alcanza en un tiempo finito. Aquí $E-U=cx^2$ tiene cero cuadrático. La rama pertenece a un nivel especial: este acercamiento de una historia no demuestra estabilidad del equilibrio para todos los datos próximos.

[]{#equilibrio-y-estabilidad-definiciones}

[]{#fispm-t1-c13-s10}

[]{#fpm-i-13-s10}

## 10. Equilibrio y estabilidad: definiciones {#fispm-c13-equilibrio-y-estabilidad-definiciones}

Una posición de fuerza nula no es todavía un estado de reposo si la partícula pasa por ella con velocidad no nula. Para hablar de estabilidad debemos describir el estado completo y precisar qué perturbaciones admitimos. La distinción es esencial en un sistema de segundo orden: una velocidad inicial arbitrariamente pequeña puede producir un desplazamiento grande si se espera suficiente tiempo.[^10]

Consideraremos $m\ddot{\mathbf r}=-\nabla U(\mathbf r)$, con $U\in C^2(\Omega)$ y $m>0$ constante. En variables de estado, las ecuaciones son $\dot{\mathbf r}=\mathbf v$ y $\dot{\mathbf v}=-\nabla U/m$. Su campo es $C^1$, de modo que los datos iniciales determinan una solución local única. Las conclusiones de estabilidad se referirán a este modelo autónomo en un marco inercial.

[]{#fispm-t1-c13-d0010}

**Definición 13.10 --- Estado de equilibrio.** Un estado $(\mathbf r_*,\mathbf0)$ es de equilibrio si la historia constante $\mathbf r(t)=\mathbf r_*$, $\mathbf v(t)=\mathbf0$ satisface las ecuaciones. La posición es entonces una posición de equilibrio.

[]{#fispm-t1-c13-p0015}

**Proposición 13.15 --- Equilibrios y puntos críticos.** Para el modelo anterior, $(\mathbf r_*,\mathbf0)$ es un equilibrio si y sólo si $\nabla U(\mathbf r_*)=\mathbf0$.

**Demostración.** Una historia constante tiene velocidad y aceleración cero. Sustituirla en Newton exige $\nabla U(\mathbf r_*)=0$. Recíprocamente, si el gradiente se anula, la historia constante verifica ambas ecuaciones de estado. $\square$

Para medir cercanía elegimos una escala temporal fija $\tau>0$ y usamos $d_\tau=|\mathbf r-\mathbf r_*|+\tau|\mathbf v|$. Ambos sumandos tienen unidades de longitud. Cambiar $\tau$ por otra constante positiva no cambia la noción cualitativa de estabilidad, porque las métricas resultantes se acotan mutuamente por factores constantes.

[]{#fispm-t1-c13-d0011}

**Definición 13.11 --- Estabilidad de Lyapunov del estado.** El equilibrio es estable si, para todo $\varepsilon>0$, existe $\delta>0$ tal que todo dato con $d_\tau(0)<\delta$ produce una solución para todo $t\geq0$ y satisface $d_\tau(t)<\varepsilon$. Es inestable si no cumple esa condición.

La definición exige controlar posición y velocidad, durante todo el futuro del modelo. En un dominio abierto puede tomarse primero $\varepsilon$ suficientemente pequeño para que el entorno espacial quede dentro de él. Las pruebas energéticas que siguen también justificarán la continuación temporal mediante confinamiento en un conjunto compacto del dominio.

[]{#fispm-t1-c13-d0012}

**Definición 13.12 --- Estabilidad asintótica.** Un equilibrio es asintóticamente estable si es estable y, además, existe un entorno de datos iniciales cuyas soluciones convergen a $(\mathbf r_*,\mathbf0)$ cuando $t\to\infty$.

Estabilidad significa permanecer cerca; atracción significa aproximarse al estado con el tiempo. Una oscilación pequeña puede cumplir la primera y no la segunda. Una trayectoria especial que se aproxima a un equilibrio inestable, como ejercicio 13.19, tampoco acredita atracción de un entorno completo.

[]{#fispm-t1-c13-p0016}

**Proposición 13.16 --- Obstrucción energética a la atracción de un entorno.** En el modelo conservativo anterior, ningún equilibrio es asintóticamente estable.

**Demostración.** En cualquier entorno del estado de equilibrio hay datos con posición exactamente $\mathbf r_*$ y velocidad no nula tan pequeña como se quiera. Su energía es $U(\mathbf r_*)+m|\mathbf v_0|^2/2>U(\mathbf r_*)$. Si la historia convergiera al estado, la continuidad de $K+U$ exigiría que su energía tendiera a $U(\mathbf r_*)$. Pero proposición 13.10 mantiene su valor inicial constante. Por tanto, esos datos no convergen, o no tienen una solución global; cualquiera de las dos posibilidades impide atracción del entorno exigido en la definición 13.12. $\square$

El resultado no prohíbe que existan historias particulares que converjan, ni que haya estabilidad sin atracción. Tampoco se aplica sin cambios a un sistema que pierde energía por resistencia: allí el argumento de conservación deja de estar disponible. La descripción de las fuerzas decide qué noción puede probarse.

La elección de un horizonte temporal también cambia la pregunta. En un intervalo fijo $0\leq t\leq T$, la dependencia continua de soluciones respecto de datos iniciales puede mantener cercanas historias de un equilibrio inestable si la perturbación se hace suficientemente pequeña. Definición 13.11 exige una sola elección de tamaño inicial que sirva para todos los tiempos futuros. No basta comprobar que durante diez segundos, o durante un número fijo de oscilaciones, el desplazamiento fue pequeño. El orden de los cuantificadores distingue control en una observación finita y estabilidad dinámica.

[]{#fispm-t1-c13-mp0010}

**Principio metodológico 13.10 --- Perturbar el estado completo.** Al clasificar un equilibrio, incluye perturbaciones de posición y velocidad y declara si buscas permanencia cercana o convergencia. No sustituye esa clasificación el signo de una fuerza en un dibujo ni la evolución de una única historia seleccionada.

[]{#ejercicios-9}

### Ejercicios {#fispm-c13-ejercicios-9}

[]{#fispm-t1-c13-e0020}

**Ejercicio 13.20.** Para $U(x)=a(x^2-b^2)^2$, determina los estados de equilibrio. ¿Una partícula que cruza $x=b$ con velocidad no nula está en equilibrio?

**Solución.** $U'(x)=4ax(x^2-b^2)$ se anula en $x=-b,0,b$. Los estados de equilibrio son $(-b,0),(0,0),(b,0)$, donde el segundo componente es velocidad. El estado $(b,v)$ con $v\ne0$ no es un equilibrio: aunque su aceleración instantánea sea cero, su posición cambia porque $\dot x=v$. Esta distinción no clasifica todavía los tres estados como estables o inestables; requiere los criterios y pruebas siguientes.

[]{#fispm-t1-c13-e0021}

**Ejercicio 13.21.** Una masa bajo $F=-kx$, con $k>0$, parte de $x=0$ con velocidad $\eta\ne0$ arbitrariamente pequeña. Explica por energía por qué no puede converger al equilibrio $(0,0)$.

**Solución.** Su energía inicial es $m\eta^2/2>0$, tomando $U(0)=0$. La conservación exige ese valor para todo instante. Convergencia de posición y velocidad a cero implicaría $m\dot x^2/2+kx^2/2\to0$, incompatible con la constante positiva. La amplitud puede ser muy pequeña y la historia permanecer próxima; eso es compatible con estabilidad y excluye únicamente la atracción de estos datos. Concluir inestabilidad sólo porque no hay convergencia confundiría definición 13.11 y definición 13.12.

[]{#extremos-no-degenerados-en-una-dimensión}

[]{#fispm-t1-c13-s11}

[]{#fpm-i-13-s11}

## 11. Extremos no degenerados en una dimensión {#fispm-c13-extremos-no-degenerados-en-una-dimensiuxf3n}

Un mínimo del potencial rodea el equilibrio con una barrera energética. Datos suficientemente próximos tienen energía insuficiente para cruzarla y, al mismo tiempo, velocidad pequeña. Este argumento permite probar estabilidad sin resolver la ecuación. Para un máximo con curvatura negativa, una pequeña separación inicial puede crecer hasta abandonar un entorno fijo.[^11]

[]{#fig:I-13-R01}

<figure id="fig-fpm-v04-i-13-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-13-R01.svg" class="lightbox" data-gallery="fpm-v04-c13"><img src="/assets/books/fispm/v04/I-13-R01.svg" alt="La fuerza apunta hacia un mínimo cuadrático. Diagrama del capítulo 13; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="360" height="252" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 13.5.** Para $U=2x^2/5$, la fuerza es $F=-4x/5$. A ambos lados del mínimo apunta hacia el origen. Con masa positiva, la energía conserva las perturbaciones pequeñas dentro de niveles cercanos. Véase §[11](#fispm-c13-extremos-no-degenerados-en-una-dimensiuxf3n).

</figcaption>

</figure>

Trabajaremos con $m\ddot x=-U'(x)$, $U\in C^2(I)$, en un intervalo abierto. La regularidad asegura unicidad local y permite prolongar soluciones que permanecen en un compacto del espacio de estados dentro del dominio. La masa y el marco son los usados en la definición 13.11.

[]{#fispm-t1-c13-p0017}

**Proposición 13.17 --- Mínimo local estricto y estabilidad unidimensional.** Si $x_*$ es un mínimo local estricto de $U$, el estado $(x_*,0)$ es estable en el sentido de la definición 13.11.

**Demostración.** Escribamos $U_*=U(x_*)$. Como el mínimo es interior, $U'(x_*)=0$ y proposición 13.15 da equilibrio. Fijemos $\varepsilon>0$ y elijamos $0<\rho<\varepsilon/2$ tan pequeño que $[x_*-\rho,x_*+\rho]\subset I$ y $U(x)>U_*$ para $0<|x-x_*|\leq\rho$. La barrera

$$B=\min\{U(x_*-\rho),U(x_*+\rho)\}-U_*$$

es positiva. Tomemos $e_0<\min\{B,m\varepsilon^2/(8\tau^2)\}$, con $e_0>0$. Por continuidad de $U$, hay $\delta>0$ tal que datos con $|x_0-x_*|+\tau|v_0|<\delta$ están dentro del intervalo de radio $\rho$ y tienen energía relativa $e=mv_0^2/2+U(x_0)-U_*<e_0$.

La conservación impide alcanzar cualquiera de sus dos fronteras, porque allí el potencial relativo es al menos $B>e$. Dentro, $U-U_*\geq0$ y $mv^2/2\leq e<e_0$, de modo que $\tau|v|<\varepsilon/2$. También $|x-x_*|<\rho<\varepsilon/2$, y la distancia de la definición 13.11 queda por debajo de $\varepsilon$.

El conjunto de estados en el intervalo cerrado con energía relativa a lo sumo $e_0$ es compacto y no toca sus fronteras espaciales. La solución permanece en él; la continuación de un campo $C^1$ impide un fin de existencia en tiempo finito. Por tanto, el control vale para todo $t\geq0$. $\square$

El teorema no exige curvatura positiva: exige un mínimo estricto y regularidad suficiente para el modelo. Si $U''(x_*)>0$, la condición se verifica porque Taylor da $U(x_*+q)-U_*=(U''(x_*)/2)q^2+o(q^2)>0$ para $q\ne0$ pequeño. El test de segunda derivada es así una condición suficiente cómoda, no la definición de estabilidad.

[]{#fispm-t1-c13-p0018}

**Proposición 13.18 --- Curvatura negativa e inestabilidad.** Si $U'(x_*)=0$ y $U''(x_*)<0$, el equilibrio $(x_*,0)$ es inestable.

**Demostración.** Por continuidad de $U''$ hay $\rho,c>0$ con el intervalo de radio $\rho$ dentro de $I$ y $U''\leq-c$ en él. Para $0<q\leq\rho$, integrar desde $x_*$ da $-U'(x_*+q)\geq cq$. Tomemos datos $x_0=x_*+\eta$, $v_0=0$, con $0<\eta<\rho$ tan pequeño como se quiera.

Mientras no abandone el intervalo hacia la derecha, su aceleración es positiva, su velocidad crece y $q(t)\geq\eta$. Por tanto, $\ddot q\geq c\eta/m$ y $q(t)\geq\eta+c\eta t^2/(2m)$. Esta cota obliga a alcanzar $q=\rho$ en tiempo finito. La solución puede continuarse hasta ese evento: antes, el potencial queda acotado en un compacto y la conservación acota su velocidad. Para el entorno fijo de radio $\rho$, existen así datos arbitrariamente próximos que llegan a su frontera. Esto contradice definición 13.11. $\square$

La prueba no se limita a una pendiente dibujada: exhibe perturbaciones arbitrariamente pequeñas y un entorno fijo que abandonan. El tiempo de salida puede crecer cuando $\eta$ disminuye. Una salida lenta sigue siendo inestabilidad, porque definición 13.11 exige control durante todo el futuro, no sólo durante una observación de duración fija.

En un mínimo estable, la conservación excluye atracción de un entorno por la proposición 13.16. Una fuerza disipativa puede cambiar esa conclusión, pero entonces debe analizarse su balance y su dinámica. Añadir el término «estable» no introduce espontáneamente un mecanismo de amortiguamiento.

La prueba del mínimo controla una perturbación de estado mediante energía pequeña, no mediante una fuerza pequeña aislada. La fuerza puede ser cero exactamente en el equilibrio y no confinar velocidades perturbadas si el potencial es plano. A la inversa, un mínimo muy estrecho exige una escala inicial más pequeña para una tolerancia espacial dada, pero sigue satisfaciendo la definición. Los parámetros de masa, curvatura y escala temporal intervienen en la elección de $\delta$; la clasificación cualitativa no afirma una misma tolerancia numérica para todos los modelos.

[]{#fispm-t1-c13-mp0011}

**Principio metodológico 13.11 --- Convertir el extremo en una prueba dinámica.** Para un mínimo, construye una barrera que controle posición y velocidad y justifique existencia futura. Para una curvatura negativa, muestra datos próximos que escapan de un entorno fijo. Si la segunda derivada se anula, conserva la pregunta abierta hasta examinar el potencial y la dinámica completos.

[]{#ejercicios-10}

### Ejercicios {#fispm-c13-ejercicios-10}

[]{#fispm-t1-c13-e0022}

**Ejercicio 13.22.** Clasifica los tres equilibrios de $U(x)=a(x^2-b^2)^2$ según las proposiciones 13.17--13.18. ¿Cuáles son asintóticamente estables en el modelo sin otras fuerzas?

**Solución.** $U''(x)=12ax^2-4ab^2$. En $x=\pm b$ vale $8ab^2>0$, de modo que hay mínimos locales estrictos y los estados $(\pm b,0)$ son estables. En el origen vale $-4ab^2<0$ y $(0,0)$ es inestable por la proposición 13.18. Ninguno es asintóticamente estable por la proposición 13.16. El acercamiento especial al origen en un nivel crítico no modifica esa clasificación de todos los datos próximos.

[]{#fispm-t1-c13-e0023}

**Ejercicio 13.23.** Para $U(x)=kx^2/2$, da una cota explícita de $|x(t)|+\tau|v(t)|$ en términos de la energía inicial y deduce estabilidad del origen sin resolver Newton.

**Solución.** La energía $E=mv^2/2+kx^2/2$ es no negativa y constante. Cada sumando está acotado por $E$, así que $|x|\leq\sqrt{2E/k}$ y $|v|\leq\sqrt{2E/m}$. Por tanto,

$$|x|+\tau|v|\leq\sqrt{2E}\left(\frac1{\sqrt k}+\frac{\tau}{\sqrt m}\right).$$

Si los datos tienden a $(0,0)$, $E$ tiende a cero y la cota tiende a cero uniformemente en el tiempo. El nivel de energía correspondiente es compacto, de modo que la solución existe para todo el futuro. La posición inicial sola no bastaría: mantener $x_0=0$ con velocidad grande no produce energía pequeña. El control incluye las dos componentes del estado.

[]{#equilibrios-degenerados-y-límites-del-criterio}

[]{#fispm-t1-c13-s12}

[]{#fpm-i-13-s12}

## 12. Equilibrios degenerados y límites del criterio {#fispm-c13-equilibrios-degenerados-y-luxedmites-del-criterio}

La igualdad $U''(x_*)=0$ no clasifica un equilibrio. Puede corresponder a un mínimo estricto, a un máximo, a un punto que no es extremo o a una región plana. Los términos de orden superior pueden decidir la geometría, pero no siempre existe un primer término no nulo de una expansión de Taylor. Conviene volver al potencial real y a la definición dinámica.[^12]

Para $U(x)=ax^4$, con $a>0$, el origen es un mínimo estricto aunque $U''(0)=0$. Proposición 13.17 demuestra su estabilidad sin exigir una aproximación cuadrática. El crecimiento de fuerza cerca del origen es cúbico: reemplazarlo por una fuerza lineal nula borraría el mecanismo que confina los estados de energía pequeña.

En cambio, $U(x)=-ax^4$ tiene un máximo degenerado. Aunque proposición 13.18 no se aplica porque su hipótesis de curvatura negativa falla, la fuerza $4ax^3$ empuja hacia afuera. Para datos $x_0=\eta>0,v_0=0$, mientras $x\geq\eta$ se cumple $\ddot x\geq4a\eta^3/m$. La misma integración del argumento de la proposición 13.18 obliga a abandonar cualquier entorno derecho fijo en tiempo finito. El cero de la segunda derivada no impide inestabilidad.

Si $U(x)=ax^3$, el origen es crítico pero no es un extremo. La fuerza $-3ax^2$ apunta hacia la izquierda a ambos lados. Desde $x_0=-\eta<0,v_0=0$, la posición disminuye y la aceleración satisface $\ddot x\leq-3a\eta^2/m$ mientras no salga del entorno izquierdo. Otra vez hay perturbaciones arbitrariamente pequeñas que escapan. «Punto crítico» es la condición de equilibrio, no una garantía de mínimo.

Cuando un primer término no nulo de Taylor es $cq^n$, con $q=x-x_*$, el signo y la paridad describen el extremo local: $n$ par y $c>0$ da mínimo estricto; $n$ par y $c<0$ da máximo; $n$ impar cambia de signo. Esa lectura requiere justificar que el resto sea menor que el término dominante. Si todos los coeficientes se anulan, no autoriza a afirmar que la función sea constante en un entorno.

Un ejemplo suave es $U(0)=0$ y $U(x)=E_0\exp(-\ell^2/x^2)$ para $x\ne0$, con $E_0,\ell>0$. Todas sus derivadas en el origen son cero, pero $U(x)>0$ cuando $x\ne0$, de modo que hay un mínimo estricto. La suavidad se comprueba porque cada derivada fuera del origen es un polinomio en $1/x$ multiplicado por la exponencial; esta última tiende a cero más rápido que cualquier potencia de $|x|$. Proposición 13.17 sigue probando estabilidad. El polinomio de Taylor nulo no coincide con la función en un entorno.

Una región realmente plana plantea otra distinción. Si $U$ es constante, toda posición con velocidad cero es un equilibrio. Una pequeña perturbación de posición con velocidad aún cero deja otro estado en reposo. Pero definición 13.11 también permite perturbar la velocidad, y entonces aparece una deriva indefinida.

[]{#fispm-t1-c13-p0019}

**Proposición 13.19 --- Potencial constante e inestabilidad del estado libre.** Para una partícula en $\mathbb R$ con $U$ constante, cada estado $(x_*,0)$ es inestable según la definición 13.11, aunque toda perturbación puramente posicional con velocidad cero permanezca en reposo.

**Demostración.** Newton da $\ddot x=0$. Para datos $x_0=x_*$ y $v_0=\eta>0$, la solución global es $x(t)=x_*+\eta t$, $v(t)=\eta$. La distancia inicial es $\tau\eta$, arbitrariamente pequeña. Para cualquier radio espacial fijo $\rho>0$, en $t=\rho/\eta$ la distancia posicional alcanza $\rho$, por lo que abandona el entorno de estado correspondiente. No existe el control uniforme temporal exigido por la definición 13.11. Si $v_0=0$, en cambio, la historia permanece en su posición inicial. $\square$

El lenguaje informal de «equilibrio neutro» suele referirse a la respuesta ante desplazamientos en reposo. Puede ser útil si se declara esa restricción, pero no debe sustituir la estabilidad de estado definida aquí. En varias dimensiones, una dirección plana puede producir el mismo fallo aunque las otras estén confinadas.

Tampoco se intercambian sin control el límite de perturbaciones pequeñas y el de tiempos grandes. Para la partícula libre, cada historia con velocidad $\eta$ permanece cerca en cualquier intervalo fijo cuando $\eta$ tiende a cero. Sin embargo, para cada $\eta\ne0$ el desplazamiento crece sin límite cuando aumenta el tiempo. El caso ilustra por qué una aproximación que elimina un término pequeño puede ser adecuada durante una duración finita y fallar en una afirmación de estabilidad para todo el futuro.

[]{#fispm-t1-c13-mp0012}

**Principio metodológico 13.12 --- No clasificar con una derivada nula.** Si el criterio cuadrático no decide, estudia órdenes superiores con resto controlado o usa una barrera directa. Distingue función plana de serie de Taylor nula, y respuesta a desplazamientos en reposo de estabilidad frente a todas las perturbaciones del estado.

[]{#ejercicios-11}

### Ejercicios {#fispm-c13-ejercicios-11}

[]{#fispm-t1-c13-e0024}

**Ejercicio 13.24.** Para $U(x)=ax^4$, obtén cotas de posición y velocidad en términos de la energía y decide si el equilibrio es estable o asintóticamente estable.

**Solución.** Con $E=mv^2/2+ax^4$, se tiene $|x|\leq(E/a)^{1/4}$ y $|v|\leq\sqrt{2E/m}$. Ambas cotas tienden a cero con la energía inicial y valen durante toda la historia. Los niveles de energía son compactos, lo que permite continuación global. El origen es estable; no es asintóticamente estable por la proposición 13.16. El exponente $1/4$ del control de posición refleja que el potencial es más plano que un mínimo cuadrático, pero no elimina el confinamiento.

[]{#fispm-t1-c13-e0025}

**Ejercicio 13.25.** Compara la estabilidad del origen para $U_+(x)=ax^4$, $U_-(x)=-ax^4$ y $U_0(x)=0$, con $a>0$. Todos tienen primera y segunda derivadas nulas allí. ¿Qué dato distingue las conclusiones?

**Solución.** $U_+$ tiene mínimo estricto y proposición 13.17 da estabilidad. $U_-$ empuja hacia afuera con fuerza $4ax^3$; una perturbación positiva en reposo escapa por la cota de aceleración del texto, así que es inestable. $U_0$ no ejerce fuerza y proposición 13.19 da inestabilidad frente a perturbaciones de velocidad. Coincidir en dos derivadas no decide el comportamiento. Lo distinguen la barrera positiva del primer caso, el crecimiento hacia afuera del segundo y la deriva libre del tercero. En el último, permanecer en reposo bajo desplazamientos no equivale a estabilidad del estado completo.

[]{#estabilidad-en-varias-dimensiones}

[]{#fispm-t1-c13-s13}

[]{#fpm-i-13-s13}

## 13. Estabilidad en varias dimensiones {#fispm-c13-estabilidad-en-varias-dimensiones}

En varias dimensiones el potencial puede subir en una dirección y bajar en otra. Examinar una sola sección de su paisaje no basta para demostrar confinamiento. La prueba de estabilidad exige una barrera que rodee al punto en todas las direcciones; el Hessiano ofrece una condición suficiente para construirla cerca de un punto crítico.[^13]

[]{#fispm-t1-c13-d0013}

**Definición 13.13 --- Hessiano y positividad definida.** Para $U\in C^2(\Omega)$, su Hessiano en $\mathbf r_*$ es la matriz simétrica $H_{ij}=\partial_i\partial_jU(\mathbf r_*)$. Es positivo definido si $\mathbf h^T H\mathbf h>0$ para todo vector no nulo $\mathbf h$. Es positivo semidefinido si el producto es no negativo, permitiendo direcciones no nulas donde se anula.

En coordenadas cartesianas, Taylor alrededor de un punto crítico toma la forma $U(\mathbf r_*+\mathbf h)=U_*+\mathbf h^T H\mathbf h/2+o(|\mathbf h|^2)$. La matriz representa la curvatura cuadrática local, no todo el potencial. Una dirección de curvatura cero requiere examinar el resto o una barrera directa.

[]{#fispm-t1-c13-p0020}

**Proposición 13.20 --- Mínimo estricto multidimensional y criterio del Hessiano.** Para $m\ddot{\mathbf r}=-\nabla U$, con $U\in C^2$, un mínimo local estricto interior produce un equilibrio estable. En particular, un punto crítico con Hessiano positivo definido es un mínimo local estricto y produce estabilidad.

**Demostración.** En un mínimo interior, el gradiente se anula. Tomemos una bola cerrada de radio $\rho<\varepsilon/2$ alrededor de $\mathbf r_*$, contenida en el dominio y en una región donde $U>U_*$ fuera del centro. Por compacidad de su esfera frontera,

$$B=\min_{|\mathbf r-\mathbf r_*|=\rho}(U(\mathbf r)-U_*)>0.$$

Escojamos energía relativa inicial $e$ positiva o nula, suficientemente pequeña para que $e<B$ y $e<m\varepsilon^2/(8\tau^2)$. La continuidad permite asegurar esas desigualdades mediante datos suficientemente próximos. Como $e$ se conserva, la trayectoria no alcanza la esfera. Dentro, $U-U_*\geq0$, por lo que $\tau|\mathbf v|<\varepsilon/2$, y la distancia total es menor que $\varepsilon$. El subnivel de energía dentro de la bola es compacto, no toca la esfera y acota velocidades; garantiza continuación para todo tiempo futuro.

Si $H$ es positivo definido, la función $\mathbf n\mapsto\mathbf n^TH\mathbf n$ sobre la esfera unitaria tiene mínimo $\lambda>0$. Taylor da $U-U_*\geq\lambda|\mathbf h|^2/4$ para $\mathbf h$ pequeño: el resto se acota por $\lambda|\mathbf h|^2/4$. Por tanto, hay mínimo local estricto y se aplica el primer argumento. $\square$

La prueba energética no requiere resolver cada coordenada ni diagonalizar el Hessiano. Su primera parte también cubre mínimos estrictos con curvaturas nulas, como $U=x^2+y^4$ con coeficientes positivos. El criterio matricial es suficiente, mientras que una matriz semidefinida deja información pendiente.

[]{#fispm-t1-c13-p0021}

**Proposición 13.21 --- Inestabilidad de una silla cuadrática.** Para $U(x,y)=kx^2/2-\ell y^2/2$, con $k,\ell>0$, el origen es un equilibrio inestable aunque el movimiento en la dirección $x$ esté confinado.

**Demostración.** Newton da $m\ddot x=-kx$ y $m\ddot y=\ell y$. Para datos $x_0=0,v_{x,0}=0,y_0=\eta>0,v_{y,0}=0$, la unicidad mantiene $x=0$. La solución $y(t)=\eta\cosh(\sqrt{\ell/m}\,t)$ verifica la ecuación y los datos. Para cualquier radio fijo $\rho>0$, alcanza $y=\rho$ en tiempo finito si $\eta<\rho$. Como $\eta$ puede hacerse arbitrariamente pequeña, definición 13.11 falla. $\square$

La prueba es para una silla cuadrática concreta. Un criterio general de inestabilidad de sistemas no lineales mediante el espectro de su linealización requiere herramientas adicionales; no lo damos por demostrado aquí. Los ejemplos con direcciones invariantes permiten verificar el escape directamente, y el Hessiano positivo se trata mediante una barrera sin usar ese criterio general.

Un cambio ortonormal de coordenadas no altera la positividad de la forma cuadrática: si $\mathbf h=Q\mathbf z$ con $Q^TQ=I$, entonces $\mathbf h^TH\mathbf h=\mathbf z^TQ^THQ\mathbf z$ y $|\mathbf h|=|\mathbf z|$. Las direcciones físicas no dependen de cómo orientamos los ejes. En cambio, una parametrización restringida o una coordenada curvilínea exige conservar la expresión cinética correspondiente. No se puede tomar una segunda derivada respecto de un parámetro arbitrario y tratarla, sin más, como toda la información cartesiana de fuerza y movimiento.

[]{#fispm-t1-c13-mp0013}

**Principio metodológico 13.13 --- Controlar todas las direcciones.** Para demostrar estabilidad busca una barrera cerrada alrededor del punto, o una forma cuadrática positiva con resto controlado. Si hay direcciones planas, examina los términos superiores. Para demostrar escape, comprueba que la trayectoria usada satisface todas las componentes de Newton.

[]{#ejercicios-12}

### Ejercicios {#fispm-c13-ejercicios-12}

[]{#fispm-t1-c13-e0026}

**Ejercicio 13.26.** Sea $U=k(x^2+y^2)/2+\alpha xy$, con $k>0$ y $|\alpha|<k$. Demuestra estabilidad del origen mediante una cota de energía, sin calcular autovalores.

**Solución.** Como $2|xy|\leq x^2+y^2$, se tiene $U\geq(k-|\alpha|)(x^2+y^2)/2$. El potencial es estrictamente positivo fuera del origen y tiene gradiente cero allí. Para energía $E$, resulta $|\mathbf r|\leq\sqrt{2E/(k-|\alpha|)}$ y $|\mathbf v|\leq\sqrt{2E/m}$. Ambas cotas tienden a cero con la energía inicial y confinan globalmente la historia en un compacto. El origen es estable por la definición 13.11. La condición estricta importa: cuando $|\alpha|=k$, esta cota espacial pierde una dirección y no acredita estabilidad.

[]{#fispm-t1-c13-e0027}

**Ejercicio 13.27.** Compara $U_1=kx^2/2+ay^4$, $U_2=kx^2/2$ y $U_3=kx^2/2-ay^4$, con $k,a>0$. Sus Hessianos en el origen coinciden. Clasifica el origen usando las ecuaciones y el potencial.

**Solución.** Los tres Hessianos son $\operatorname{diag}(k,0)$. En $U_1$ hay mínimo estricto y proposición 13.20 da estabilidad. En $U_2$, la coordenada $y$ es libre; datos con $x=0,v_x=0,y=0,v_y=\eta$ producen $y=\eta t$ y escape, como proposición 13.19. En $U_3$, la subhistoria $x=0,v_x=0$ es invariante y $m\ddot y=4ay^3$; iniciar $y=\eta>0,v_y=0$ produce escape por el argumento de §12. Los dos últimos son inestables. Un mismo Hessiano semidefinido admite conclusiones distintas porque no registra los términos superiores ni el control de velocidades en la dirección plana.

[]{#fispm-t1-c13-e0028}

**Ejercicio 13.28.** Para $U(x,y)=\alpha xy$, con $\alpha>0$, construye datos arbitrariamente próximos al origen que escapen. Verifica que la línea propuesta es dinámicamente invariante.

**Solución.** Newton exige $m\ddot x=-\alpha y$ y $m\ddot y=-\alpha x$. Elijamos $y=-x$, con datos $x_0=\eta,y_0=-\eta$ y ambas velocidades cero. La historia $x(t)=\eta\cosh(\sqrt{\alpha/m}\,t)$, $y(t)=-x(t)$ satisface las dos ecuaciones: $m\ddot x=\alpha x=-\alpha y$ y $m\ddot y=-\alpha x$. Su distancia espacial es $\sqrt2\eta\cosh(\sqrt{\alpha/m}\,t)$ y supera cualquier radio fijo. No bastaba elegir una dirección de potencial decreciente: se ha comprobado además una solución completa que conserva esa dirección y escapa.

[]{#síntesis-y-dominio-de-validez}

[]{#fispm-t1-c13-s14}

[]{#fpm-i-13-s14}

## 14. Síntesis y dominio de validez {#fispm-c13-suxedntesis-y-dominio-de-validez}

El capítulo ha separado tres problemas. Primero, la existencia de potencial para un campo de posición: una cuestión de integrales, derivadas y dominio. Segundo, la conservación de energía mecánica en una historia: una consecuencia de Newton y de las potencias presentes. Tercero, la estabilidad de un equilibrio: una afirmación sobre todos los datos de estado suficientemente próximos y todos los tiempos futuros. Pasar de uno al siguiente requiere hipótesis nuevas.

Un campo conservativo puede tener un equilibrio inestable, como el máximo cuadrático. Un mínimo estable puede no atraer, como cualquier mínimo en el modelo conservativo tratado. Un campo sin potencial global puede admitir potenciales locales. Y una fuerza de potencia nula en una historia puede mantener la energía sin ser un campo conservativo de posición. Mantener esas distinciones evita usar la misma palabra para resultados matemáticos distintos.

La disipación introduce una variante útil del argumento de barrera. Una energía mecánica que no aumenta puede confinar los estados cercanos a un mínimo, aunque haya dejado de ser una cantidad conservada. Esto no convierte automáticamente la monotonía en una demostración de convergencia.

[]{#fispm-t1-c13-p0022}

**Proposición 13.22 --- Estabilidad energética con resistencia viscosa.** Sea $U\in C^2(\Omega)$ con mínimo local estricto interior en $\mathbf r_*$. Para $m\ddot{\mathbf r}=-\nabla U-b\dot{\mathbf r}$, con $m,b>0$ constantes, el estado $(\mathbf r_*,\mathbf0)$ es estable.

**Demostración.** El gradiente se anula en el mínimo y la resistencia se anula en reposo, por lo que hay equilibrio. Proposición 13.11 da $\dot E=-b|\mathbf v|^2\leq0$. En la prueba de la proposición 13.20, escojamos una bola donde $U-U_*\geq0$ y una barrera $B>0$ en su esfera. Si la energía relativa inicial es menor que $B$, ninguna historia puede alcanzar la esfera: allí necesitaría energía al menos $B$, mientras $E(t)-U_*\leq E(0)-U_*<B$.

Dentro, $m|\mathbf v|^2/2\leq E(t)-U_*\leq E(0)-U_*$. Hacer suficientemente pequeña la energía inicial controla velocidad y posición como en la proposición 13.20. El campo de estados sigue siendo $C^1$ y el subnivel confinado es compacto dentro del dominio, de modo que la solución se prolonga para todo $t\geq0$. Se cumple definición 13.11. $\square$

El teorema acredita estabilidad y no necesita resolver el movimiento. Para probar atracción de un entorno habría que estudiar también qué estados pueden sostener una evolución límite de potencia disipada nula, y qué otras condiciones rigen el potencial. No invocamos sin prueba un principio general de invariancia. Que $\int_0^\infty b|\mathbf v|^2dt$ sea finita no basta, por sí solo, para concluir toda convergencia de posición.

Una guía o una región singular también puede modificar el análisis. En una guía fija, el potencial se restringe al conjunto de posiciones permitidas, y las variaciones relevantes son las compatibles con ella. El mínimo ambiente y el mínimo restringido pueden diferir. Si la guía se mueve, el potencial efectivo puede adquirir dependencia temporal y el balance de la proposición 13.12 incorpora su accionamiento. La barrera autónoma no se aplica ignorando ese término.

Las posiciones excluidas deben conservarse durante todo el razonamiento. Un equilibrio interior regular permite aplicar existencia local y las pruebas anteriores. Un supuesto mínimo en una frontera de contacto unilateral requiere verificar la reacción; una singularidad del campo no es un equilibrio ordinario aunque una representación formal de energía parezca favorable. Las desigualdades de contacto y el dominio físico siguen teniendo autoridad sobre una prolongación algebraica.

El marco elegido forma parte de ese dominio de validez. La posición de un soporte fijo y la autonomía del potencial pueden cambiar de expresión al pasar a otro observador. Para aplicar el balance se transforman campo, soporte, velocidades y argumentos temporales de manera conjunta, como en el capítulo 12. La representación puede adquirir dependencia temporal aunque el fenómeno físico sea el mismo. Las pruebas de estabilidad de este capítulo usan un equilibrio estacionario y un sistema autónomo especificado; no se trasladan literalmente a una trayectoria móvil sin reformular qué estado de referencia se compara.

[]{#fispm-t1-c13-mp0014}

**Principio metodológico 13.14 --- Identificar qué conclusión está probada.** Para potencial, comprueba campo y dominio. Para conservación, deriva el balance completo. Para estabilidad, fija el estado, el tipo de perturbación y el control temporal. Para atracción, añade una prueba de convergencia. Conserva las restricciones de contacto, regularidad y modelización en cada paso.

[]{#ejercicios-13}

### Ejercicios {#fispm-c13-ejercicios-13}

[]{#fispm-t1-c13-e0029}

**Ejercicio 13.29.** En el plano, sea $U(x,y)=-kx^2/2+ky^2/2$, con $k>0$, pero la partícula está restringida a la recta fija lisa $x=0$. Compara la estabilidad sin guía y con guía. Declara el espacio de perturbaciones de cada conclusión.

**Solución.** Sin guía, la fuerza es $(kx,-ky)$; una perturbación en la dirección $x$ crece como en la proposición 13.21 y el origen es inestable en el estado ambiente. Con la guía, las posiciones admisibles tienen $x=0$ y las velocidades admisibles $v_x=0$. El potencial restringido es $ky^2/2$ y la dinámica tangencial $m\ddot y=-ky$ tiene equilibrio estable por la proposición 13.17. La guía fija lisa no aporta potencia. La estabilidad restringida controla sólo datos compatibles $(y,v_y)$: no afirma que una partícula liberada de la guía permanezca cerca ante perturbaciones en $x$. Como el modelo restringido es conservativo, tampoco produce estabilidad asintótica.

[]{#fispm-t1-c13-e0030}

**Ejercicio 13.30.** Un bloque horizontal unido a un resorte fijo cumple $m\ddot x=-kx-b\dot x$, con $k,b>0$. Se exige que su estado permanezca dentro de $|x|+\tau|v|<\varepsilon$. Obtén una condición suficiente sobre la energía inicial y distingue lo acreditado de una prueba de convergencia.

**Solución.** La energía $E=mv^2/2+kx^2/2$ satisface $E(t)\leq E_0$. Por las cotas del ejercicio 13.23,

$$|x(t)|+\tau|v(t)|\leq\sqrt{2E_0}\left(\frac1{\sqrt k}+\frac{\tau}{\sqrt m}\right).$$

Es suficiente imponer $E_0<\varepsilon^2/[2(1/\sqrt k+\tau/\sqrt m)^2]$. El subnivel es compacto y Newton prolonga la historia globalmente, así que la condición prueba permanencia para todo tiempo. Integrar $\dot E=-bv^2$ también da $\int_0^\infty bv^2dt\leq E_0$. Estos argumentos acreditan estabilidad y disipación acumulada acotada; la convergencia de este sistema puede estudiarse por sus ecuaciones, pero no se ha demostrado únicamente con la desigualdad presentada. Esa distinción no niega una conclusión posterior: conserva el alcance de la prueba efectivamente realizada.

Con esto queda construido el puente entre trabajo, potencial y estabilidad. El dominio decide cuándo una fuerza admite representación global; el balance decide cuándo se conserva la energía mecánica; la geometría del potencial y las ecuaciones deciden qué perturbaciones quedan confinadas. El capítulo 14 estudiará momento lineal, impulso y centro de masa, y añadirá herramientas vectoriales para sistemas de partículas que el balance escalar no sustituye.

[^1]: Kleppner--Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 4, §§4.7--4.8, pp. 169--173. La construcción y su evaluación sobre historias con retrocesos se prueban aquí con el teorema fundamental y la regla de la cadena.

[^2]: Kleppner--Kolenkow, obra citada, cap. 4, §4.7, pp. 169--172: libertad del cero y suma de contribuciones. Se prueban localmente la unicidad en un intervalo y la superposición; los ejercicios distinguen una historia posible de un tramo usado para calcular trabajo.

[^3]: Morin, *Introduction to Classical Mechanics: With Problems and Solutions*, Cambridge University Press, 2008, cap. 5, §5.3, pp. 149--151, ecuaciones 5.27 y 5.30--5.32. Proposición 13.4 se demuestra mediante una parametrización única de la curva y regla de la cadena, sin dividir por componentes de velocidad.

[^4]: Morin, obra citada, cap. 5, §5.3, pp. 150--151, relaciona trabajo entre extremos y lazos. Las tres equivalencias se prueban aquí directamente para un campo continuo, usando segmentos locales y concatenación; no se presupone Stokes ni un criterio de rotacional sin condiciones de dominio.

[^5]: Morin, obra citada, cap. 5, §5.3, pp. 150--151, teorema 5.2, nota 8 y ecuaciones 5.30--5.33. Se retiene la condición necesaria y se prueba aquí una condición suficiente con dominio estrellado. No se adopta una equivalencia global basada únicamente en rotacional nulo en un abierto arbitrario.

[^6]: Morin, obra citada, cap. 5, §5.3, pp. 150--151, nota 8, advierte una limitación del criterio basado en Stokes ante singularidades. El ejemplo del plano perforado y sus integrales se desarrollan aquí para explicitar la diferencia local--global sin usar teoremas de integración de campos de capítulos posteriores.

[^7]: Kleppner--Kolenkow, obra citada, cap. 4, §4.7, pp. 169--172; Morin, obra citada, cap. 5, §5.3, p. 149, ecuación 5.28. La conservación se demuestra en tiempo con masa constante, marco inercial y potencias restantes nulas, sin identificar una guía móvil con una reacción sin trabajo.

[^8]: Kleppner--Kolenkow, obra citada, cap. 4, §4.11, pp. 182--184, presenta el balance con fuerzas adicionales. Proposición 13.12 se deduce aquí mediante la regla de la cadena para U dependiente del tiempo; el ejemplo de anclaje móvil conserva el trabajo medido con el desplazamiento de la masa y distingue la derivada parcial de la derivada sobre la historia.

[^9]: Kleppner--Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 4, §4.9, pp. 176--177, presenta regiones permitidas y diagramas energéticos. La restricción por componentes y las pruebas de llegada finita o infinita se desarrollan aquí desde continuidad e integración temporal.

[^10]: Kleppner--Kolenkow, obra citada, cap. 4, §4.8, pp. 174--175, relaciona fuerza nula y extrema del potencial. Las definiciones sobre el estado completo, la escala temporal y la obstrucción a la estabilidad asintótica se formulan y prueban aquí; no se identifica estabilidad con atracción.

[^11]: Kleppner--Kolenkow, obra citada, cap. 4, §4.8, pp. 174--175; Morin, *Introduction to Classical Mechanics*, 2008, cap. 5, §5.2, pp. 147--148. Las pruebas proposiciones 13.17--13.18 precisan estabilidad de estado, barrera energética, continuación y salida de un entorno; la aproximación oscilatoria sistemática queda para el capítulo 23.

[^12]: Kleppner--Kolenkow, obra citada, cap. 4, §4.8, p. 175, considera segundas derivadas nulas; Morin, obra citada, cap. 5, §5.2, pp. 147--148, limita la aproximación cuadrática. Aquí se distingue explícitamente serie de Taylor nula y función constante, y la respuesta «neutra» posicional de la estabilidad de Lyapunov del estado.

[^13]: El uso del paisaje y de la aproximación cuadrática enlaza con Kleppner--Kolenkow, obra citada, cap. 4, §§4.8--4.10, pp. 174--178, y Morin, obra citada, cap. 5, §5.2, pp. 147--148. El Hessiano, la barrera esférica y las pruebas multidimensionales se desarrollan aquí; no se presupone un teorema espectral de estabilidad no lineal.
