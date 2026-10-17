---
title: "Restricciones elementales y grados de libertad"
subtitle: "Física para matemáticos · Tomo I · Capítulo 11"
author: "A. Peña"
description: "Capítulo 11 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0351
source-id: FISPM-T1-C11
editorial-id: FPM-I-11
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0350"]
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

[Capítulo 10](fisica-para-matematicos-capitulo-10-fuerzas-elementales-y-diagramas-de-cuerpo-libre.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 12](fisica-para-matematicos-capitulo-12-trabajo-potencia-y-energia-cinetica.md)

[]{#fispm-c11-restricciones-elementales-y-grados-de-libertad}

[]{#restricción-geométrica-y-problema-dinámico}

[]{#fispm-t1-c11-s01}

[]{#fpm-i-11-s01}

## 11.1. Restricción geométrica y problema dinámico {#fispm-c11-restricciuxf3n-geomuxe9trica-y-problema-dinuxe1mico}

Una cuenta ensartada en un alambre puede recorrerlo sin abandonarlo. Un cuerpo unido a una cuerda tensa no puede alejarse arbitrariamente del otro extremo. Dos objetos que permanecen apoyados sobre una plataforma pueden tener movimientos relacionados con el de ésta. Tales condiciones reducen los movimientos posibles, pero no especifican por sí mismas la rapidez o las fuerzas necesarias para realizarlos.[^1]

[]{#fispm-t1-c11-d0001}

**Definición 11.1 --- Restricción activa de un modelo mecánico.** Una restricción activa es una condición que deben satisfacer las posiciones o los movimientos de los cuerpos durante el régimen considerado. Puede expresar una geometría impuesta, una conexión ideal o la permanencia de un contacto. Su forma y su intervalo de aplicación pertenecen al modelo físico.

El adjetivo «activa» recuerda que algunas relaciones sólo valen mientras persiste un régimen. Una cuerda de longitud $\ell$ impide una distancia mayor que $\ell$, pero permite distancias menores cuando está floja. La igualdad distancia $=\ell$ describe su rama tensa, no toda configuración posible de esa cuerda. Un suelo no adhesivo impide penetrar y puede dejar que el cuerpo se separe; la igualdad de alturas sólo describe contacto sostenido. El capítulo 10 mostró cómo comprobar las fuerzas que permiten mantener esas ramas.

Una guía bilateral ideal ofrece otro caso: puede obligar a una cuenta a permanecer sobre una línea, ejerciendo la reacción que sea necesaria hacia cualquiera de sus lados dentro del modelo. Para una superficie que sólo empuja, esa posibilidad no está garantizada. Escribir la misma ecuación geométrica para ambas no elimina la diferencia física de sus fuerzas admisibles.

[]{#fispm-t1-c11-p0001}

**Proposición 11.1 --- Una trayectoria geométrica no fija una historia temporal.** Para una partícula restringida a una circunferencia fija de radio $R>0$, la relación $x^2+y^2=R^2$ no determina por sí sola su velocidad ni su aceleración.

**Demostración.** Para cualquier función dos veces diferenciable $\theta(t)$,

$$\mathbf r(t)=R\cos\theta(t)\,e_x+R\sin\theta(t)\,e_y$$

satisface la relación. La velocidad tiene magnitud $R|\dot\theta|$ y la aceleración depende tanto de $\dot\theta$ como de $\ddot\theta$. Elegir funciones angulares diferentes produce historias distintas sobre la misma circunferencia. La igualdad geométrica no selecciona ninguna de esas funciones. $\square$

Para averiguar qué historia se realiza, debemos añadir fuerzas y datos compatibles. Una guía lisa, una cuerda y un motor que impone una rotación pueden conducir a esa misma circunferencia y producir balances diferentes. El dibujo de una curva no identifica automáticamente la interacción que la mantiene.

Conviene separar tres preguntas. La primera es qué posiciones permite la geometría. La segunda es qué velocidades y aceleraciones son compatibles con permanecer en ella. La tercera es qué fuerzas producen esas aceleraciones y cumplen los límites físicos del vínculo. Saltar directamente a la tercera puede ocultar una relación cinemática; responder sólo la primera deja incompleta la dinámica.

[]{#fispm-t1-c11-mp0001}

**Principio metodológico 11.1 --- Escribir el vínculo antes de usar sus consecuencias.** Declara la relación geométrica y el régimen que la activa. Deduce después sus condiciones cinemáticas y conserva las fuerzas de vínculo como incógnitas cuando corresponda. Una palabra como «unidos» no sustituye la geometría de la conexión.

[]{#ejercicios}

### 11.1.1. Ejercicios {#fispm-c11-ejercicios}

[]{#fispm-t1-c11-e0001}

[]{#fispm-t1-c11-e0011}

**Ejercicio 11.1.** Una partícula permanece en una circunferencia fija de radio $R$. Compara las historias con $\theta(t)=\omega t$ y $\theta(t)=2\omega t$, para $\omega>0$. ¿La restricción permite ambas? ¿Requieren la misma aceleración en el punto inicial?

**Solución.** Ambas satisfacen $x^2+y^2=R^2$ y comienzan en $(R,0)$. Sus velocidades iniciales son $R\omega e_y$ y $2R\omega e_y$. Sus aceleraciones iniciales son $-R\omega^2e_x$ y $-4R\omega^2e_x$. La geometría permite ambas, pero exige resultantes distintas si la masa es la misma. No son soluciones del mismo problema dinámico con los mismos datos: precisamente ilustran la información que falta al conocer sólo la curva.

[]{#fispm-t1-c11-e0002}

**Ejercicio 11.2.** Dos partículas se mueven en un plano y aún no se ha declarado ninguna conexión entre ellas. Enumera las coordenadas de posición necesarias. Un informe afirma que compartir el plano obliga a tener la misma aceleración. Evalúa la afirmación.

**Solución.** Podemos usar $(x_1,y_1,x_2,y_2)$: cuatro números describen la posición conjunta. Compartir el plano no relaciona los valores de las dos parejas ni impone aceleración común. Hace falta una conexión o una solución dinámica que justifique esa igualdad. La tercera ley, si las partículas interactúan, relacionaría sus fuerzas recíprocas; tampoco impone por sí sola igualdad de aceleraciones. Con masas distintas, incluso fuerzas opuestas de igual magnitud pueden producir aceleraciones de magnitudes diferentes.

[]{#relaciones-de-posición-fijas-y-dependientes-del-tiempo}

[]{#fispm-t1-c11-s02}

[]{#fpm-i-11-s02}

## 11.2. Relaciones de posición fijas y dependientes del tiempo {#fispm-c11-relaciones-de-posiciuxf3n-fijas-y-dependientes-del-tiempo}

Muchas restricciones elementales pueden escribirse utilizando sólo posiciones y tiempo. Una cuenta sobre una recta fija satisface $y=0$; una cuenta sobre una circunferencia fija satisface $x^2+y^2=R^2$. Un cuerpo que acompaña verticalmente una plataforma de altura prescrita $y_s(t)$ satisface $y-y_s(t)=0$ mientras mantiene contacto. La diferencia entre los tres casos aparece al derivar sus ecuaciones.[^2]

[]{#fispm-t1-c11-d0002}

**Definición 11.2 --- Restricción holónoma elemental.** Llamaremos holónoma a una restricción expresable mediante una o varias relaciones de posición

$$\Phi_\alpha(Q,t)=0,$$

donde $Q$ reúne las coordenadas de los cuerpos. Si la relación no depende explícitamente de $t$, la geometría es fija respecto del marco elegido; si lo hace, puede describir una geometría que se mueve de manera prescrita.

La definición no garantiza que cualquier lista de funciones describa un dispositivo realizable ni que sus ecuaciones sean independientes. Tampoco convierte una desigualdad unilateral en una igualdad válida siempre. Para el suelo, $y-y_s\geq0$ describe la región accesible; en la rama de contacto sostenido se añade la igualdad. Es útil mantener las dos formas y recordar cuál se está usando.

La dependencia explícita del tiempo debe distinguirse de la dependencia de posiciones desconocidas. Si una cuña tiene posición horizontal $X(t)$ que debe determinarse dinámicamente, escribir una relación con $X$ no equivale a imponer externamente su movimiento. $X$ es otra coordenada del sistema. Si un dispositivo controla y prescribe $X(t)$, se trata de información adicional: deja de ser una variable de posición que podamos elegir libremente a ese tiempo.

[]{#fispm-t1-c11-p0002}

**Proposición 11.2 --- Consecuencias de una relación afín móvil.** Si durante un intervalo

$$y(t)-\alpha x(t)-s(t)=0,$$

con $\alpha$ constante y funciones dos veces diferenciables, entonces $v_y-\alpha v_x=\dot s,\qquad a_y-\alpha a_x=\ddot s.$

**Demostración.** Diferenciar una y dos veces la igualdad produce las expresiones. La constancia de $\alpha$ evita términos adicionales. Si ésta variara con el tiempo, también habría que derivarla y conservar los términos correspondientes. $\square$

En una recta fija, $s$ es constante y las dos relaciones tienen lado derecho cero. En una recta que se traslada, $\dot s$ y $\ddot s$ pueden ser no nulos. Usar la fórmula de la recta fija después de cambiar el soporte daría una condición cinemática equivocada, incluso si el dibujo instantáneo de la línea se parece al anterior.

Proposición 11.2 expresa condiciones necesarias para una historia que cumple la relación. Si sólo se conoce la ecuación de aceleraciones, no se recupera automáticamente la posición original: al integrar quedan constantes que deben ajustarse con posición y velocidad iniciales. Esta distinción será decisiva cuando resolvamos poleas. Los términos constantes de longitud desaparecen al derivar, pero siguen siendo necesarios para comprobar la configuración inicial.

[]{#fispm-t1-c11-mp0002}

**Principio metodológico 11.2 --- Conservar el origen geométrico de las ecuaciones derivadas.** Antes de igualar aceleraciones, escribe posiciones con signos y referencias explícitos. Distingue una coordenada desconocida de una trayectoria prescrita. Cuando una constante desaparezca por diferenciación, no la borres del control de los datos iniciales.

[]{#ejercicios-1}

### 11.2.1. Ejercicios {#fispm-c11-ejercicios-1}

[]{#fispm-t1-c11-e0003}

**Ejercicio 11.3.** Una partícula permanece en una recta que satisface $y-\alpha x-ct=0$, con $\alpha$ adimensional y $c$ de dimensión velocidad. Obtén las relaciones entre componentes de velocidad y aceleración. ¿El movimiento de la recta desaparece de ambas?

**Solución.** proposición 11.2 da $v_y=\alpha v_x+c$ y $a_y=\alpha a_x$. La velocidad de traslación aparece en la primera y desaparece de la segunda porque es constante. Esto no vuelve fija la recta ni elimina $c$ del dato de velocidad compatible. Por ejemplo, una partícula con $v_x=0$ necesita $v_y=c$ para acompañarla. Imponer también $v_y=0$ sólo sería compatible si $c=0$.

[]{#fispm-t1-c11-e0004}

**Ejercicio 11.4.** Una guía circular centrada en el origen tiene radio prescrito $R(t)=R_0+ct>0$. En $t=0$, la partícula está en $(R_0,0)$. ¿Es compatible una velocidad inicial $(0,V)$ cuando $c\ne0$? Obtén la componente que debe cambiar.

**Solución.** Diferenciar $x^2+y^2=R(t)^2$ da $xv_x+yv_y=R\dot R$. En el instante inicial resulta $R_0v_x=R_0c$, por lo que $v_x=c$. La velocidad tangencial $v_y=V$ puede elegirse libremente en ese punto, pero la componente radial no puede ser cero si el radio cambia. La compatibilidad geométrica no informa aún qué fuerza expande el vínculo ni cuánto vale su reacción. El ejemplo usa el marco inercial del centro fijo, sin atribuir reposo al cuerpo respecto de toda la guía.

[]{#variables-independientes-y-grados-de-libertad}

[]{#fispm-t1-c11-s03}

[]{#fpm-i-11-s03}

## 11.3. Variables independientes y grados de libertad {#fispm-c11-variables-independientes-y-grados-de-libertad}

Contar coordenadas cartesianas es un punto de partida. Una partícula en el plano necesita dos; dos partículas en el plano necesitan cuatro. Las restricciones pueden reducir cuántos números de posición se eligen independientemente. Para hacer esa reducción de manera fiable debemos exhibir cómo los demás quedan determinados.

[]{#fispm-t1-c11-d0003}

**Definición 11.3 --- Grados de libertad de posición en una descripción local regular.** A un tiempo fijado, una familia de posiciones admisibles tiene $d$ grados de libertad si, en la región considerada, puede describirse mediante $d$ parámetros de posición independientes que determinan unívocamente las posiciones, con una parametrización regular y una recuperación local regular de esos parámetros. En los ejemplos, ambas descripciones serán explícitas y diferenciables; una variación no nula de los parámetros debe producir alguna variación de posición a primer orden.

«Regular» excluye que una parametrización pierda información local o se detenga artificialmente por una elección de variable defectuosa. No desarrollaremos aquí una teoría general de superficies de configuración. Comprobaremos directamente cada relación: qué parámetros pueden variar, cómo reconstruyen las coordenadas y cómo se recuperan de ellas. Los puntos donde esa descripción cambia se examinarán por separado.

[]{#fispm-t1-c11-p0003}

**Proposición 11.3 --- Conteo por eliminación explícita.** Si $n$ coordenadas de posición están relacionadas de modo que $k$ de ellas se expresan unívocamente como funciones regulares de las otras $n-k$, y éstas varían independientemente en una región abierta, la descripción local tiene $n-k$ grados de libertad.

**Demostración.** Elegir las $n-k$ coordenadas libres reconstruye todas las posiciones mediante las funciones declaradas. Proyectar una posición reconstruida sobre esas coordenadas recupera los parámetros sin ambigüedad. Así se obtiene exactamente la descripción local de la definición 11.3; el número de variables independientes es $n-k$. $\square$

Por ejemplo, una partícula en la recta $y=\alpha x+s$ tiene una coordenada libre $x$ y una coordenada reconstruida $y$. Dos partículas sobre una misma recta fija tienen dos posiciones libres, una por partícula, antes de declarar una relación entre ellas. Si su separación firmada es fija, una de las dos posiciones determina la otra y queda una sola variable de posición independiente.

La circunferencia requiere una descripción local cuidadosa. En una porción que no cruce el punto de corte elegido, un ángulo $\theta$ dentro de un intervalo abierto de longitud menor que $2\pi$ determina $(R\cos\theta,R\sin\theta)$ y se recupera unívocamente sobre ese arco. Tiene un grado de libertad. Que la misma circunferencia necesite varios intervalos para evitar duplicar el ángulo no aumenta ese número local.

El tiempo no se suma al conteo de posiciones a tiempo fijado. Tampoco se suma la masa ni un parámetro geométrico prescrito. Si el radio de la guía es conocido, no es una posición adicional que el cuerpo pueda elegir. Si el radio pasa a ser una coordenada dinámica independiente de un dispositivo, el sistema elegido ha cambiado y su conteo debe reconstruirse.

Grados de libertad de posición y número de datos iniciales cumplen funciones distintas. Una ecuación dinámica de segundo orden para una coordenada suele requerir posición y velocidad iniciales. Eso no significa dos grados de libertad de posición: significa dos datos para seleccionar una historia temporal de una variable de posición. Tampoco el conteo geométrico garantiza que todos los datos se permitan físicamente; la velocidad debe ser compatible con los vínculos y las fuerzas con el régimen.

[]{#fispm-t1-c11-mp0003}

**Principio metodológico 11.3 --- Mostrar las variables libres.** Justifica el conteo reconstruyendo las coordenadas dependientes desde parámetros que se puedan elegir independientemente. Indica la región donde esa reconstrucción es unívoca y separa número de coordenadas de posición, parámetros del modelo y datos iniciales.

[]{#ejercicios-2}

### 11.3.1. Ejercicios {#fispm-c11-ejercicios-2}

[]{#fispm-t1-c11-e0005}

**Ejercicio 11.5.** Dos partículas se mueven sobre una línea y permanecen unidas por una conexión de separación firmada constante $x_2-x_1=\ell>0$. Cuenta los grados de libertad de posición. ¿Qué cambia si sólo se declara que cada una permanece sobre la línea?

**Solución.** Con la conexión activa, elegir $x_1$ fija $x_2=x_1+\ell$; queda un grado de libertad. Sin la relación de separación, $x_1$ y $x_2$ se eligen independientemente y hay dos. La longitud prescrita $\ell$ no es una tercera coordenada libre. El conteo conectado exige mantener el orden y la relación indicada; una cuerda floja sólo impondría un límite de distancia y requeriría distinguir la región interior de la rama tensa.

[]{#fispm-t1-c11-e0006}

**Ejercicio 11.6.** Una partícula está restringida a una circunferencia fija y se describe localmente por $\theta$. Para determinar su historia se proporcionan $\theta_0$ y $\dot\theta_0$. Un informe cuenta dos grados de libertad porque aparecen dos números. Corrígelo y señala qué controla cada dato.

**Solución.** Hay un grado de libertad de posición: $\theta$ determina el punto del arco. $\theta_0$ fija la posición inicial y $\dot\theta_0$ la velocidad tangencial inicial, de magnitud $R|\dot\theta_0|$. Son datos de distinto orden para una historia de una sola coordenada de posición. No existe una segunda dirección de posición libre en la circunferencia. La velocidad no tiene que ser nula, pero no puede incluir una componente radial para la guía fija.

[]{#ecuaciones-redundantes-y-puntos-singulares}

[]{#fispm-t1-c11-s04}

[]{#fpm-i-11-s04}

## 11.4. Ecuaciones redundantes y puntos singulares {#fispm-c11-ecuaciones-redundantes-y-puntos-singulares}

La expresión «restar una por cada restricción» resulta peligrosa si «restricción» significa cada ecuación escrita. Podemos repetir una misma relación, multiplicarla por una constante o escribir una forma equivalente. La posición admisible no cambia y el número de variables libres tampoco. El conteo debe referirse a condiciones independientes efectivas.

[]{#fispm-t1-c11-d0004}

**Definición 11.4 --- Restricción redundante respecto de una lista.** Una ecuación añadida es redundante si toda posición que satisface las relaciones anteriores ya la satisface. En ese caso no reduce el conjunto de posiciones admisibles. Dos listas son equivalentes en una región si permiten exactamente las mismas posiciones allí.

[]{#fispm-t1-c11-p0004}

**Proposición 11.4 --- La repetición de una igualdad no reduce otra vez la libertad.** Si $\Phi(Q,t)=0$ es una relación y $\lambda\ne0$ una constante, añadir $\lambda\Phi(Q,t)=0$ no cambia las posiciones admisibles ni un conteo local válido para ellas.

**Demostración.** Toda posición con $\Phi=0$ satisface $\lambda\Phi=0$. Recíprocamente, la primera relación sigue incluida. Las dos listas permiten el mismo conjunto, de modo que los parámetros que lo describían siguen reconstruyendo todas sus posiciones. $\square$

Una dificultad distinta aparece cuando una ecuación deja de describir una reducción regular en el punto considerado. No basta con que una relación sea nueva en el papel. Por ejemplo, en el plano la igualdad $x^2+y^2=0$ parece una sola ecuación, pero permite únicamente el origen. No deja una curva sobre la cual mover una partícula.

[]{#fispm-t1-c11-p0005}

**Proposición 11.5 --- Una igualdad singular puede fijar dos coordenadas.** Sobre coordenadas reales, la relación $x^2+y^2=0$ equivale a $x=0$ y $y=0$. Su conjunto admisible tiene cero grados de libertad de posición, aunque se haya escrito una sola igualdad.

**Demostración.** Ambos cuadrados son no negativos. Si su suma es cero, cada uno debe ser cero, de donde $x=y=0$. Recíprocamente, el origen satisface la relación. No queda parámetro de posición que pueda variar en el conjunto de un solo punto. $\square$

La primera derivada de esa igualdad da $xv_x+yv_y=0$. En el origen se convierte en $0=0$ y parece no limitar ninguna velocidad. Pero una historia que permanezca en el conjunto de un solo punto tiene necesariamente velocidad cero. La condición obtenida al derivar es necesaria y, en este caso singular, insuficiente para reconocer todas las velocidades realizables. No debemos reemplazar la geometría por su primera derivada y olvidar el conjunto que describía.

Otra relación, $x^2-y^2=0$, permite dos rectas que se cruzan. Sobre una rama alejada del cruce hay una coordenada libre. En el cruce no hay una única curva regular con una dirección tangente única que describa las dos ramas a la vez. Para hablar del movimiento debemos identificar qué rama sigue la historia o examinar el encuentro. Este ejemplo no añade un formalismo nuevo; muestra el límite de usar una descripción local sin comprobar su región.

En los problemas elementales que siguen trabajaremos en ramas regulares y exhibiremos parámetros independientes. No formularemos una regla universal $n-r$ basada sólo en contar ecuaciones. Una regla general necesitaría hipótesis de independencia y regularidad precisas, además de herramientas para verificarlas; el método por eliminación de la proposición 11.3 basta para nuestros ejemplos.

[]{#fispm-t1-c11-mp0004}

**Principio metodológico 11.4 --- Contar condiciones efectivas en una región.** Retira duplicaciones lógicas antes de contar. Si una relación parece perder información al derivarla o aparecen varias ramas, vuelve al conjunto de posiciones permitido. Distingue un conteo regular de una afirmación sobre un punto singular.

[]{#ejercicios-3}

### 11.4.1. Ejercicios {#fispm-c11-ejercicios-3}

[]{#fispm-t1-c11-e0007}

**Ejercicio 11.7.** Una partícula en el plano debe satisfacer $y=0$ y $2y=0$. ¿Tiene cero grados de libertad? Compara con las condiciones $y=0$ y $x=0$.

**Solución.** Las primeras dos ecuaciones son equivalentes a $y=0$ y dejan $x$ libre: un grado de libertad. La segunda ecuación es redundante y no elimina otra coordenada. Con $y=0$ y $x=0$, sólo se permite el origen y hay cero grados de libertad. Contar el mismo número de ecuaciones en ambas listas daría el mismo resultado erróneo para conjuntos diferentes.

[]{#fispm-t1-c11-e0008}

**Ejercicio 11.8.** En el origen, un informe acepta cualquier velocidad para la restricción $x^2+y^2=0$ porque su primera derivada vale cero automáticamente. Explica el fallo y determina posición, velocidad y aceleración de una historia admisible.

**Solución.** proposición 11.5 obliga a que $x(t)=y(t)=0$ durante todo el intervalo. Por tanto, $\mathbf r=0$, $\mathbf v=0$ y $\mathbf a=0$. La primera condición derivada en un único instante no es suficiente. Incluso su segunda derivada aporta aquí información: $v_x^2+v_y^2+xa_x+ya_y=0$ implica velocidad cero en el origen, pero el argumento del conjunto completo ya determina toda la historia. Una velocidad no nula saldría inmediatamente de la única posición permitida.

[]{#compatibilidad-de-velocidades-y-aceleraciones}

[]{#fispm-t1-c11-s05}

[]{#fpm-i-11-s05}

## 11.5. Compatibilidad de velocidades y aceleraciones {#fispm-c11-compatibilidad-de-velocidades-y-aceleraciones}

Estar en una posición admisible no garantiza que cualquier velocidad permita conservar el vínculo. Una partícula situada sobre una circunferencia fija, pero con velocidad radial hacia afuera, empieza a abandonarla si no ocurre un cambio de velocidad. Para resolver una evolución regular debemos proporcionar datos compatibles con la restricción activa. Si se plantea un choque que corrige una velocidad, se trata de otro problema, no de una aceleración ordinaria que pueda borrar instantáneamente el dato.

[]{#fig:I-11-N03}

![**Figura 11.1.** En una circunferencia fija, la velocidad es tangente y la componente normal de aceleración apunta al centro. No debe imponerse aceleración normal nula. Estas flechas son cinemáticas. Véase §[11.5](#fispm-c11-compatibilidad-de-velocidades-y-aceleraciones).](/assets/books/fispm/v04/I-11-N03.svg "fig:"){.fpm-v04-figure fig-alt="Vínculo curvo y aceleración" width="340px" fig-cap=""}

[]{#fispm-t1-c11-d0005}

**Definición 11.5 --- Velocidad compatible con una restricción activa.** Una velocidad en una posición y tiempo dados es compatible si puede ser la derivada en ese instante de una historia diferenciable que satisface la restricción durante un intervalo. Diferenciar las relaciones de posición proporciona condiciones necesarias, que deben interpretarse dentro de la geometría original.

[]{#fispm-t1-c11-d0006}

**Definición 11.6 --- Aceleración compatible con una historia restringida.** Una aceleración es compatible con una posición y velocidad si puede ser la segunda derivada de una historia dos veces diferenciable que conserva la restricción. Sus condiciones se obtienen derivando dos veces las relaciones, sin omitir los términos que dependen de la velocidad o del movimiento prescrito del vínculo.

En relaciones afines fijas, las condiciones derivadas siguen siendo lineales y no contienen productos de velocidades. Una curva puede producir esos términos aunque sea fija. Este hecho explica por qué «permanecer en una trayectoria» no equivale a «tener aceleración tangente a ella».[^3]

[]{#fispm-t1-c11-p0006}

**Proposición 11.6 --- Compatibilidad en una circunferencia fija.** Si $\mathbf r\cdot\mathbf r=R^2$ durante un intervalo y $R>0$ es constante, entonces

$$\mathbf r\cdot\mathbf v=0,\qquad \mathbf r\cdot\mathbf a=-\|\mathbf v\|^2.$$

Con normal radial exterior $\mathbf n=\mathbf r/R$, la componente normal de aceleración es $a_n=-\|\mathbf v\|^2/R$.

**Demostración.** La primera derivada de $\mathbf r\cdot\mathbf r=R^2$ da $2\mathbf r\cdot\mathbf v=0$. Diferenciar esa igualdad da $\mathbf v\cdot\mathbf v+\mathbf r\cdot\mathbf a=0$. Dividir el segundo término por $R>0$ proporciona la componente respecto de la normal exterior. $\square$

La velocidad es tangente a la circunferencia, pero la aceleración tiene una componente normal hacia el centro cuando la rapidez no es cero. No se trata de una fuerza nueva: es una consecuencia cinemática que las fuerzas reales deben producir. El capítulo 8 estableció la descomposición de aceleración para trayectorias curvas; aquí la misma componente surge directamente de diferenciar el vínculo.

La igualdad deja libre, desde la geometría sola, la componente tangencial de aceleración. Ésta cambia la rapidez y se obtiene de Newton tangencial una vez declaradas las fuerzas. Confundir la componente normal necesaria con toda la aceleración conduciría a suponer rapidez constante sin justificación. Por el contrario, si la rapidez sí es constante, queda nula la componente tangencial y la normal persiste.

Las ecuaciones derivadas no deben usarse hacia atrás sin datos suficientes. Si una función cumple $\ddot y=0$, entonces $y$ es afín en el tiempo, no necesariamente constante ni nula. Para recuperar una guía fija $y=0$, también se requieren $y(t_0)=0$ y $\dot y(t_0)=0$. En ejemplos regulares afines, esas condiciones y la ecuación de aceleraciones sí preservan el vínculo por integración. En ejemplos singulares como §4, debemos volver a la geometría completa.

El control de compatibilidad precede a resolver las fuerzas. Un dato incompatible no se corrige cambiando silenciosamente la velocidad inicial. Se debe identificar el problema: o el vínculo no está activo, o se necesita un evento de cambio de régimen, o el conjunto de datos no corresponde al modelo anunciado. Esta separación evita presentar una solución de otro problema como si satisficiera el inicial.

[]{#fispm-t1-c11-mp0005}

**Principio metodológico 11.5 --- Comprobar datos de distintos órdenes.** Verifica posiciones, velocidades y aceleraciones con las relaciones correspondientes. Diferencia durante el intervalo declarado, no sólo en una instantánea. Si obtienes una ecuación de aceleraciones, conserva los datos iniciales necesarios para que su integración mantenga la geometría.

[]{#ejercicios-4}

### 11.5.1. Ejercicios {#fispm-c11-ejercicios-4}

[]{#fispm-t1-c11-e0009}

**Ejercicio 11.9.** Una partícula sobre una circunferencia fija de radio $2\,\mathrm m$ tiene posición $(2,0)\,\mathrm m$ y velocidad $(0,3)\,\mathrm{m\,s^{-1}}$. Obtén la condición sobre su aceleración. ¿Es compatible una aceleración nula? ¿Queda fijada la componente vertical?

**Solución.** La velocidad es compatible porque $\mathbf r\cdot\mathbf v=0$. Proposición 11.6 exige $2a_x=-9$, con unidades consistentes, por lo que $a_x=-4{,}5\,\mathrm{m\,s^{-2}}$. La aceleración nula no mantiene la circunferencia con esa velocidad. $a_y$ es la componente tangencial en ese punto y no queda fijada por la geometría. Para determinarla necesitamos las fuerzas tangenciales; fijarla en cero equivaldría a añadir una condición dinámica o de rapidez.

[]{#fispm-t1-c11-e0010}

**Ejercicio 11.10.** Una ecuación obtenida para una guía recta fija es $\ddot y=0$. Decide si asegura $y=0$. Da datos suficientes para que sí lo haga y un ejemplo de datos que no lo permitan.

**Solución.** La solución general es $y(t)=y_0+V(t-t_0)$. Para obtener $y=0$ en todo el intervalo se necesitan $y_0=0$ y $V=0$. Con $y_0=0$ y $V\ne0$, la partícula parte sobre la guía pero sale de ella. Con $y_0\ne0$ y $V=0$, permanece en una recta paralela distinta. La ecuación de aceleraciones sola perdió dos constantes al derivar; la posición y velocidad iniciales restituyen la información requerida.

[]{#fuerzas-de-vínculo-y-guías-lisas}

[]{#fispm-t1-c11-s06}

[]{#fpm-i-11-s06}

## 11.6. Fuerzas de vínculo y guías lisas {#fispm-c11-fuerzas-de-vuxednculo-y-guuxedas-lisas}

Una restricción activa debe coexistir con Newton. Si el cuerpo recibe una fuerza que lo desviaría de una guía, alguna interacción debe proporcionar la contribución necesaria para conservarla. A esa contribución la llamaremos fuerza de vínculo, manteniendo el receptor y el agente físico que la produce. No es una fuerza adicional sin origen: puede ser contacto de una guía o tracción de una cuerda, ya estudiados en el capítulo 10.

[]{#fig:I-11-R02}

![**Figura 11.2.** Una partícula en una guía circular fija y lisa puede tener reacción normal centrípeta, perpendicular a su velocidad. Si esa reacción es la única fuerza, su potencia es cero aunque cambie la dirección del movimiento. Véase §[11.6](#fispm-c11-fuerzas-de-vuxednculo-y-guuxedas-lisas).](/assets/books/fispm/v04/I-11-R02.svg "fig:"){.fpm-v04-figure fig-alt="La guía puede cambiar la dirección sin cambiar la rapidez" width="353px" fig-cap=""}

[]{#fispm-t1-c11-d0007}

**Definición 11.7 --- Fuerza de vínculo.** Es una fuerza incluida para representar la interacción de un dispositivo o entorno que mantiene una restricción física. En un modelo ideal puede aparecer como incógnita determinada por Newton y las condiciones cinemáticas. Su dirección y sus valores admisibles requieren hipótesis sobre esa interacción; no se deducen de una ecuación geométrica aislada.

[]{#fispm-t1-c11-d0008}

**Definición 11.8 --- Vínculo bilateral y vínculo unilateral.** Un vínculo bilateral impone una igualdad geométrica y, dentro de su idealización, puede impedir desviaciones hacia ambos lados de ella. Un vínculo unilateral limita una región accesible y puede dejar de estar activo al separarse el cuerpo. En el contacto no adhesivo, la fuerza normal sólo empuja y debe verificarse su no negatividad.

Una ranura lisa puede modelarse como una guía bilateral: si el cuerpo intenta desviarse hacia una pared o la otra, el contacto correspondiente suministra la reacción. La reacción normal neta firmada puede tener ambos signos, aunque cada pared individual sólo empuje. Una mesa sola tiene un único lado accesible y no puede producir cualquier signo. La igualdad de posiciones durante contacto no vuelve bilateral esa mesa.

Para un ejemplo plano, tomemos una guía recta fija con dirección tangente $e_t$ y normal $e_n$, ambas constantes. Sea $\mathbf F=F_te_t+F_ne_n$ la suma de otras fuerzas. La guía se declara lisa y su reacción se modela como $R_ne_n$, sin componente tangencial. Ésta es información física adicional a la geometría de la recta.

[]{#fispm-t1-c11-p0007}

**Proposición 11.7 --- Reacción de una guía recta lisa.** Mientras una partícula conserva la guía fija, su aceleración normal es cero y Newton exige

$$a_t=\frac{F_t}{m},\qquad R_n=-F_n.$$

Para una guía bilateral ideal, $R_n$ puede ser firmado. Si el mismo cálculo representa un soporte no adhesivo con $e_n$ hacia afuera, se exige además $R_n\geq0$.

**Demostración.** La posición normal constante da $a_n=0$. Proyectar Newton normal produce $0=F_n+R_n$ y proyectar tangencialmente produce $ma_t=F_t$. Las condiciones de signo proceden del tipo de interacción declarado en la definición 11.8 y en el capítulo 10, no del despeje algebraico. $\square$

La fuerza de vínculo no tiene por qué compensar toda la fuerza aplicada. Compensa aquí su componente normal; la tangencial continúa acelerando a la partícula. Si el cuerpo está en reposo instantáneo y $F_t\ne0$, comienza a moverse sobre la guía. Para equilibrio se necesitaría además $F_t=0$ bajo estas fuerzas, o una contribución tangencial que lo compense.

En una guía curva, la reacción no se obtiene imponiendo aceleración normal cero. Si se declara contacto liso bilateral con una circunferencia fija, proposición 11.6 y Newton normal dan

$$R_n=-m\frac{\|\mathbf v\|^2}{R}-F_n.$$

La reacción sigue siendo normal por la hipótesis de contacto liso, pero debe producir la aceleración normal requerida por la curvatura. Si el vínculo sólo puede tirar hacia el centro, como una cuerda, habría que escribir $R_n=-T$ y comprobar $T\geq0$. La compatibilidad geométrica y la capacidad física del dispositivo siguen siendo controles distintos.

Podemos reducir el movimiento sobre una recta a una coordenada tangencial y conservar el balance normal para calcular la reacción. Eliminar una coordenada de posición no significa eliminar una interacción física. La coordenada reducida simplifica la historia, mientras que la ecuación normal responde una pregunta sobre la fuerza que sostiene esa historia.

[]{#fispm-t1-c11-mp0006}

**Principio metodológico 11.6 --- Separar reducción y reacción.** Usa el vínculo para reducir variables de posición, pero conserva el balance necesario para encontrar su fuerza. Declara qué dirección permite la idealización y verifica sus signos. En una curva, calcula primero la aceleración normal compatible antes de resolver la reacción.

[]{#ejercicios-5}

### 11.6.1. Ejercicios {#fispm-c11-ejercicios-5}

**Ejercicio 11.11.** Una partícula de $2\,\mathrm{kg}$ está en una guía recta lisa horizontal, con datos compatibles. La suma de otras fuerzas es $(6,-8)\,\mathrm N$ en ejes horizontal y vertical. Calcula aceleración y reacción. ¿Se compensa toda esa fuerza?

**Solución.** La aceleración vertical es cero. Proposición 11.7 da $a_x=3\,\mathrm{m\,s^{-2}}$ y reacción $(0,8)\,\mathrm N$. La resultante es $(6,0)\,\mathrm N$: sólo se compensó la componente normal. La respuesta también es admisible para un soporte inferior no adhesivo si se mantiene contacto, porque la reacción apunta hacia arriba y tiene magnitud positiva. La fuerza dada ya es la suma de las otras contribuciones; no se añade un peso nuevo si estaba incluido en ella.

[]{#fispm-t1-c11-e0012}

**Ejercicio 11.12.** Repite el balance con fuerza externa total $(6,8)\,\mathrm N$. Compara una ranura bilateral ideal con un soporte inferior no adhesivo. Parte de posición apoyada y velocidad vertical nula.

**Solución.** La rama restringida exigiría reacción $(0,-8)\,\mathrm N$ y aceleración $(3,0)\,\mathrm{m\,s^{-2}}$. La ranura puede suministrar esa reacción mediante su pared superior, dentro de la idealización. El soporte inferior no puede tirar hacia abajo: se rechaza la rama de contacto. Sin esa reacción, la aceleración es $(3,4)\,\mathrm{m\,s^{-2}}$ y la separación vertical inicial aumenta como $2t^2$ metros si $t$ se expresa en segundos. El mismo vínculo algebraico de altura constante tiene capacidades físicas diferentes según el dispositivo.

[]{#cuerda-sobre-una-polea-fija}

[]{#fispm-t1-c11-s07}

[]{#fpm-i-11-s07}

## 11.7. Cuerda sobre una polea fija {#fispm-c11-cuerda-sobre-una-polea-fija}

Una cuerda tensa de longitud constante relaciona posiciones antes de relacionar aceleraciones. Para una polea fija que une dos cuerpos colgantes en ramas verticales, hay dos tramos rectos variables y un arco fijo sobre la polea. Si uno de los tramos se alarga, el otro debe acortarse en igual cantidad. Esta afirmación necesita los ejes y la geometría; no procede de la tercera ley.[^4]

[]{#fig:I-11-R01}

![**Figura 11.3.** Con $m_1>m_2$, la máquina de Atwood ideal tiene una tensión común y aceleraciones opuestas. Los diagramas corresponden a cada masa por separado: $m_1g>T>m_2g$. La polea y la cuerda no se incluyen dentro de esos cuerpos. Véase §[11.7](#fispm-c11-cuerda-sobre-una-polea-fija).](/assets/books/fispm/v04/I-11-R01.svg "fig:"){.fpm-v04-figure fig-alt="Dos DCL y una restricción" width="340px" fig-cap=""}

[]{#fig:I-11-N01}

![**Figura 11.4.** Ambas coordenadas crecen hacia abajo. La cuerda inextensible impone $y_1+y_2=\mathrm{constante}$, y por tanto $a_1+a_2=0$. Esta relación proviene de la geometría, no de la tercera ley. Véase §[11.7](#fispm-c11-cuerda-sobre-una-polea-fija).](/assets/books/fispm/v04/I-11-N01.svg "fig:"){.fpm-v04-figure fig-alt="Geometría de Atwood" width="340px" fig-cap=""}

[]{#fispm-t1-c11-d0009}

**Definición 11.9 --- Polea ideal en los ejemplos elementales.** Admitiremos una polea que mantiene la geometría declarada de la cuerda y despreciamos fricción, masa e inercia relevantes del dispositivo. La cuerda será flexible, de masa despreciable e inextensible en su rama tensa. Bajo esta idealización se transmite una magnitud de tensión común a lo largo de una misma cuerda sin otros cuerpos intermedios. No se divide por una masa nula; se adopta el balance ideal motivado por el límite de la proposición 10.8.

Una polea real puede requerir tensiones distintas para cambiar su rotación o vencer resistencia. No basta con que la cuerda sea continua para excluir esos efectos. Aquí declaramos el dispositivo ideal porque el objetivo es estudiar la longitud y los balances de partículas; la dinámica rotacional se desarrollará después.

Sea $y_1$ la longitud vertical del tramo del cuerpo 1 y $y_2$ la del cuerpo 2, ambos medidos positivos hacia abajo desde referencias fijas. Absorbiendo el arco y los otros tramos constantes en $L$, la rama tensa satisface $y_1+y_2=L$. La ubicación de cada masa también debe permanecer dentro de la región donde los tramos siguen verticales y ningún cuerpo encuentra la polea o el suelo.

[]{#fispm-t1-c11-p0008}

**Proposición 11.8 --- Relación cinemática de una polea fija.** Si $y_1+y_2=L$ con $L$ constante durante un intervalo, entonces

$$v_1+v_2=0,\qquad a_1+a_2=0.$$

Una descripción de posición tiene un grado de libertad: elegir $y_1$ fija $y_2=L-y_1$.

**Demostración.** Las relaciones de velocidad y aceleración se obtienen diferenciando la igualdad. La eliminación explícita de $y_2$ cumple proposición 11.3 en cualquier intervalo abierto de posiciones compatible con los tramos declarados. $\square$

Los signos opuestos corresponden a haber elegido ambos ejes hacia abajo. Si uno se toma hacia arriba y el otro hacia abajo, las componentes de aceleración serán iguales. Ninguna de las dos convenciones modifica el movimiento físico. Decir sólo «tienen la misma aceleración» sin indicar si se comparan magnitudes, componentes o vectores deja una ambigüedad que la ecuación de longitud evita.

[]{#fispm-t1-c11-p0009}

**Proposición 11.9 --- Máquina de Atwood elemental.** Dos masas positivas $m_1,m_2$ cuelgan de la cuerda ideal de la proposición 11.8, bajo gravedad uniforme y sin otras fuerzas sobre ellas. En los ejes descendentes declarados,

$$a_1=\frac{m_1-m_2}{m_1+m_2}g,\qquad a_2=-a_1,\qquad T=\frac{2m_1m_2}{m_1+m_2}g.$$

**Demostración.** Newton sobre cada receptor da $m_1g-T=m_1a_1$ y $m_2g-T=m_2a_2$. Sustituir $a_2=-a_1$ y restar elimina $T$ y produce $(m_1-m_2)g=(m_1+m_2)a_1$. La suma de masas es positiva y permite despejar. Sustituir en cualquiera de los balances da $T$, que es positiva para masas y $g$ positivos. La tensión calculada es admisible para la rama tensa. $\square$

Si las masas son iguales, la aceleración es cero. Eso permite reposo o movimiento uniforme con velocidades opuestas compatibles. El reposo no se deduce de igualar masas: depende de los datos iniciales. Si una masa es mayor, su aceleración apunta hacia abajo, pero podría estar subiendo inicialmente y frenarse antes de bajar. De nuevo, la resultante fija la aceleración y no impone el signo instantáneo de velocidad.

[]{#fispm-t1-c11-mp0007}

**Principio metodológico 11.7 --- Relacionar primero longitudes.** Separa los tramos variables de los constantes, define los ejes y deriva la longitud total. Justifica la tensión común mediante el dispositivo ideal y usa Newton por receptor. No reemplaces la relación geométrica por una supuesta consecuencia de acción y reacción.

[]{#ejercicios-6}

### 11.7.1. Ejercicios {#fispm-c11-ejercicios-6}

[]{#fispm-t1-c11-e0013}

**Ejercicio 11.13.** En proposición 11.9, $m_1=2\,\mathrm{kg}$, $m_2=3\,\mathrm{kg}$ y $g=10\,\mathrm{m\,s^{-2}}$. Calcula las aceleraciones firmadas y la tensión. Si el cuerpo 2 comienza subiendo, ¿contradice el signo de su aceleración?

**Solución.** $a_1=-2\,\mathrm{m\,s^{-2}}$, $a_2=+2\,\mathrm{m\,s^{-2}}$ y $T=24\,\mathrm N$. Los balances son $20-24=2(-2)$ y $30-24=3(2)$, ambos en newtons. Una velocidad inicial ascendente del cuerpo 2 significa $v_2<0$ y es compatible con aceleración positiva: inicialmente se frena. El dato del cuerpo 1 debe cumplir $v_1=-v_2$. Las fórmulas valen hasta que cambie la geometría, el régimen o las fuerzas admitidas.

[]{#fispm-t1-c11-e0014}

**Ejercicio 11.14.** Ahora la polea superior se traslada verticalmente con posición prescrita $Y(t)$. Usa un único eje positivo hacia arriba para las alturas $y_1,y_2,Y$. Los tramos siguen verticales y el arco permanece constante. Obtén la relación de aceleraciones y la tensión cuando $\ddot Y=A$ es constante. Examina su admisibilidad.

**Solución.** La longitud variable es $(Y-y_1)+(Y-y_2)$, de modo que $2Y-y_1-y_2=C$ y $a_1+a_2=2A$. Newton ascendente da $T-m_ig=m_ia_i$. Sumando las aceleraciones despejadas,

$$T\left(\frac1{m_1}+\frac1{m_2}\right)-2g=2A,$$

$$T=\frac{2m_1m_2}{m_1+m_2}(g+A),\qquad a_i=\frac{T}{m_i}-g.$$

La rama tensa requiere $A\geq-g$ y datos compatibles con la longitud y su primera derivada. Para $A<-g$, la tensión sería negativa y se rechaza esa rama. Para $A=-g$, la tensión nula es un caso marginal cuya geometría depende también de los datos y la continuación. Con masas iguales se obtiene $a_1=a_2=A$, pero no se deduce que sus velocidades relativas a la polea sean nulas: la relación inicial sólo fija su suma. Los cálculos se hicieron en el marco inercial, aunque el soporte acelere.

[]{#polea-móvil-y-factores-geométricos}

[]{#fispm-t1-c11-s08}

[]{#fpm-i-11-s08}

## 11.8. Polea móvil y factores geométricos {#fispm-c11-polea-muxf3vil-y-factores-geomuxe9tricos}

Consideremos una cuerda con un extremo fijo en el soporte superior. Desde allí baja, rodea una polea móvil, sube a una polea fija superior y baja finalmente hasta un cuerpo de masa $m_1$. La polea móvil lleva otro cuerpo de masa $m_2$; su propia masa se desprecia y su centro mantiene la misma altura que ese cuerpo salvo una distancia fija. Ambas poleas son ideales y los tramos variables son verticales.[^5]

[]{#fig:I-11-N02}

![**Figura 11.5.** En una polea móvil ideal, los dos ramales ejercen una resultante ascendente $2T$ sobre el conjunto polea--carga. Si el extremo libre se mueve con coordenada descendente $y_1$ y la polea con $y_2$, $y_1+2y_2$ es constante. Véase §[11.8](#fispm-c11-polea-muxf3vil-y-factores-geomuxe9tricos).](/assets/books/fispm/v04/I-11-N02.svg "fig:"){.fpm-v04-figure fig-alt="Dos ramales y un vínculo" width="395px" fig-cap=""}

Esta descripción permite reconstruir la longitud sin necesitar adivinar una razón de velocidades. Si el centro de la polea móvil baja, se alargan dos tramos de cuerda. Para conservar la longitud, el tramo que llega a $m_1$ debe acortarse el doble. Los arcos constantes no contribuyen a la derivada, pero las dos ramas variables de la polea móvil sí.

Sea $y_1$ la posición descendente de $m_1$ y $y_2$ la de la polea móvil y su carga, con referencias superiores fijas. La longitud toma la forma $y_1+2y_2+C_0=\ell$. Escribimos $y_1+2y_2=L$, absorbiendo las constantes geométricas en $L$.

[]{#fispm-t1-c11-p0010}

**Proposición 11.10 --- Relación de una polea móvil con dos ramas verticales.** Durante la rama tensa de esa geometría,

$$v_1+2v_2=0,\qquad a_1+2a_2=0.$$

La descripción de posición tiene un grado de libertad y no exige igualdad de magnitudes de aceleración.

**Demostración.** Diferenciar dos veces la longitud da las relaciones. Elegir $y_2$ determina $y_1=L-2y_2$, de modo que proposición 11.3 cuenta una variable libre. Si $a_2\ne0$, la relación implica $|a_1|=2|a_2|$, no igualdad. $\square$

El coeficiente dos tiene aquí dos manifestaciones relacionadas con la misma geometría. Dos tramos cambian de longitud cuando se mueve la polea y dos tracciones de magnitud $T$ tiran hacia arriba de ella. La carga móvil recibe así una fuerza ascendente total $2T$ en el modelo de polea de masa despreciable. Si se introduce un lazo corto que conecta polea y carga, su tensión sería $2T$, no $T$: es otra cuerda, cuyo balance debe distinguirse.

No sumamos una tercera tracción sobre la carga por haber mencionado ese lazo: o estudiamos el conjunto carga--polea y sus dos tracciones externas, o separamos la polea y transmitimos el resultado mediante el lazo. Mezclar ambas elecciones duplicaría fuerzas. El mismo cuidado con receptores del capítulo 10 sigue siendo necesario.

[]{#fispm-t1-c11-p0011}

**Proposición 11.11 --- Dinámica de la polea móvil cargada.** Bajo gravedad uniforme, masas positivas y las idealizaciones anteriores,

$$a_2=\frac{m_2-2m_1}{m_2+4m_1}g,\qquad a_1=-2a_2,\qquad T=\frac{3m_1m_2}{m_2+4m_1}g.$$

**Demostración.** Los balances descendentes son

$$m_1g-T=m_1a_1,\qquad m_2g-2T=m_2a_2.$$

Proposición 11.10 da $a_1=-2a_2$, por lo que el primer balance produce $T=m_1g+2m_1a_2$. Sustituir en el segundo da $(m_2-2m_1)g=(m_2+4m_1)a_2$. El denominador es positivo; despejar y sustituir proporciona las expresiones. La tensión es positiva, compatible con la tracción de la cuerda. $\square$

Las masas que producen aceleración nula no son iguales: la condición es $m_2=2m_1$. La carga móvil recibe dos tracciones y el cuerpo del extremo una. Este balance no implica una regla general que multiplique fuerza sin modificar movimiento. La longitud obliga simultáneamente a una razón de desplazamientos. No desarrollamos aquí trabajo ni potencia; basta notar que conservar sólo el factor de fuerza y olvidar la relación geométrica dejaría incompletas las ecuaciones.

También conviene evitar una regla basada únicamente en contar poleas visibles. El factor aparece al contar tramos variables de la longitud respecto de una coordenada concreta. Una polea fija puede cambiar dirección sin introducir el mismo factor. Un conjunto con otra ruta de cuerda, soportes móviles o ángulos variables requiere reconstruir la longitud. Los coeficientes constantes de este ejemplo no se transfieren automáticamente.

Los límites sirven para comprobar el resultado. Si $m_2$ es mucho mayor que $m_1$, la carga móvil tiene aceleración próxima a $g$ descendente y el extremo ligero acelera hacia arriba con magnitud próxima a $2g$. Que esa magnitud supere $g$ no viola una cota universal: el cuerpo ligero recibe tensión además de peso. La fuerza transmitida debe producir esa aceleración en su balance individual.

[]{#fispm-t1-c11-mp0008}

**Principio metodológico 11.8 --- Contar tramos y receptores, no símbolos.** Obtén el factor cinemático de los tramos que cambian de longitud y el factor de fuerza de las tracciones sobre el receptor elegido. Si hay varias cuerdas o uniones, asigna incógnitas distintas hasta que un balance justifique relacionarlas.

[]{#ejercicios-7}

### 11.8.1. Ejercicios {#fispm-c11-ejercicios-7}

[]{#fispm-t1-c11-e0015}

**Ejercicio 11.15.** En proposición 11.11, toma $m_1=m$ y $m_2=3m$. Calcula las aceleraciones y la tensión, y verifica ambos balances. Compara con la afirmación de que los dos cuerpos deben acelerar con igual magnitud porque los une una cuerda.

**Solución.** $a_2=g/7$, $a_1=-2g/7$ y $T=9mg/7$. Sobre el cuerpo del extremo,

$$mg-\frac{9mg}{7}=-\frac{2mg}{7}=ma_1.$$

Sobre la carga móvil, $3mg-2\frac{9mg}{7}=\frac{3mg}{7}=3ma_2.$ Se verifica también $a_1+2a_2=0$. La igualdad de magnitudes no es compatible con esta longitud salvo que ambas aceleraciones sean cero. Una misma tensión transmitida no produce aceleraciones iguales en geometrías ni receptores diferentes.

[]{#fispm-t1-c11-e0016}

**Ejercicio 11.16.** En la misma geometría, elige $m_2=2m_1$. Calcula tensión y aceleraciones. ¿El balance obliga al reposo? Propón datos de velocidad compatibles que produzcan movimiento uniforme mientras permanezca disponible la geometría.

**Solución.** proposición 11.11 da $a_1=a_2=0$ y $T=m_1g$, de modo que $2T=m_2g$. No obliga al reposo. Podemos elegir $v_2=V$ descendente y $v_1=-2V$ ascendente, con cualquier $V$ compatible con el intervalo físico considerado. Esas velocidades constantes preservan $y_1+2y_2=L$ si las posiciones iniciales ya lo satisfacen. El movimiento termina de ajustarse a este modelo si un cuerpo encuentra un límite geométrico o cambia alguna idealización; equilibrio de fuerzas no garantiza disponibilidad indefinida del recorrido.

Las ocho secciones fijan el método de este capítulo: expresar el vínculo, contar variables mediante una reconstrucción local, comprobar datos y deducir las relaciones de aceleración antes de resolver fuerzas. Las secciones siguientes estudian vínculos móviles, contactos curvos y varias relaciones simultáneas, y reunirá sus condiciones de validez sin anticipar el formalismo del capítulo 25.

[]{#vínculos-móviles-y-coordenadas-relativas}

[]{#fispm-t1-c11-s09}

[]{#fpm-i-11-s09}

## 11.9. Vínculos móviles y coordenadas relativas {#fispm-c11-vuxednculos-muxf3viles-y-coordenadas-relativas}

Una guía puede trasladarse sin cambiar su forma. La posición del cuerpo respecto de ella facilita la descripción geométrica, aunque las aceleraciones que entran en Newton sigan medidas en el marco inercial. Esta diferencia requiere mantener el movimiento del soporte en las ecuaciones.[^6]

[]{#fispm-t1-c11-d0010}

**Definición 11.10 --- Movimiento prescrito de un vínculo.** Una posición de soporte $\mathbf c(t)$ es prescrita cuando el modelo la proporciona como función conocida del tiempo. No se determina entonces resolviendo Newton para ese soporte. Si debe calcularse a partir de fuerzas y datos, su posición es una variable dinámica adicional del sistema elegido.

Un motor puede imponer aproximadamente una trayectoria conocida al soporte; para estudiar el movimiento de la partícula podemos usar esa trayectoria como dato. Si queremos averiguar qué fuerza necesita el motor o cómo responde un soporte libre, debemos ampliar el sistema y sus balances. La geometría no cambia al modificar la pregunta, pero sí cambia qué información está dada y qué incógnitas debemos resolver.

[]{#fispm-t1-c11-d0011}

**Definición 11.11 --- Coordenada relativa a un soporte en traslación.** Para un soporte de posición $\mathbf c(t)$ y un cuerpo de posición inercial $\mathbf r(t)$, definimos $\mathbf q=\mathbf r-\mathbf c$. En ejes de orientación fija,

$$\dot{\mathbf q}=\mathbf v-\dot{\mathbf c},\qquad \ddot{\mathbf q}=\mathbf a-\ddot{\mathbf c}.$$

La orientación fija es parte de la definición usada aquí. No estamos calculando derivadas en una base que rote con el soporte. Si éste rota, las derivadas de la base introducen términos adicionales; no se pueden trasladar sin cambios las fórmulas presentes.

[]{#fispm-t1-c11-p0012}

**Proposición 11.12 --- Circunferencia de centro móvil prescrito.** Si una partícula conserva $\|\mathbf q\|=R$, con $R>0$ constante y $\mathbf q=\mathbf r-\mathbf c(t)$, entonces

$$\mathbf q\cdot(\mathbf v-\dot{\mathbf c})=0,$$

$$\mathbf q\cdot(\mathbf a-\ddot{\mathbf c})=-\|\mathbf v-\dot{\mathbf c}\|^2.$$

A un tiempo fijado, la partícula mantiene un grado de libertad de posición sobre un arco regular si $\mathbf c(t)$ está prescrita.

**Demostración.** Diferenciar $\mathbf q\cdot\mathbf q=R^2$ una y dos veces da las relaciones de la proposición 11.6 aplicadas a $\mathbf q$. Sustituir las derivadas de la definición 11.11 produce las expresiones. A tiempo fijado, el centro es conocido y un ángulo local determina $\mathbf r=\mathbf c+R(\cos\theta,\sin\theta)$; por la proposición 11.3 queda una coordenada libre. $\square$

La velocidad relativa es tangente a la circunferencia; la velocidad inercial no tiene por qué ser perpendicular al radio instantáneo. Puede incluir la velocidad de traslación del centro. Del mismo modo, la aceleración inercial contiene la aceleración del soporte además de la requerida por el movimiento relativo. Una fotografía del círculo no permite omitir esas contribuciones.

Newton sigue siendo $m\mathbf a=\mathbf F$. Sustituir definición 11.11 lo reescribe como $m\ddot{\mathbf q}=\mathbf F-m\ddot{\mathbf c}$. En este cálculo, el término restado procede del cambio de variable: no lo añadimos al diagrama inercial como una nueva interacción física sobre el cuerpo. Así podemos usar una coordenada relativa sin confundirla con una aceleración absoluta. El tratamiento general de marcos no inerciales tendrá su lugar posterior.

Si el centro puede moverse horizontalmente con coordenada desconocida $X$, la descripción conjunta $\mathbf r=(X+R\cos\theta,R\sin\theta)$ tiene dos posiciones independientes, $X$ y $\theta$, en un arco regular. Dar después una función prescrita $X(t)$ elimina una de esas elecciones a tiempo fijado. No vuelve imposible el movimiento: sólo cambia cuáles de sus partes se determinan dentro del problema.

Una medición relativa debe indicar respecto de qué soporte se tomó. Si el laboratorio mide la velocidad del cuerpo y la del centro por separado, primero se restan para obtener la velocidad que aparece en la proposición 11.12. Si el instrumento acompaña al centro sin girar y entrega directamente esa velocidad relativa, no se vuelve a restar el movimiento del centro. Hacerlo dos veces daría una condición radial falsa. La misma regla se aplica a la aceleración: reconstruir la magnitud inercial exige sumar la aceleración prescrita del soporte una sola vez. Esta comprobación de referencias precede al uso de números y permite interpretar correctamente ejercicio 11.18.

[]{#fispm-t1-c11-mp0009}

**Principio metodológico 11.9 --- Distinguir coordenada útil y aceleración física.** Usa posiciones relativas para expresar el vínculo, conserva el movimiento del soporte al derivar y escribe Newton en el marco declarado. Indica si el soporte es una incógnita del sistema o una trayectoria externa conocida.

[]{#ejercicios-8}

### 11.9.1. Ejercicios {#fispm-c11-ejercicios-8}

[]{#fispm-t1-c11-e0017}

**Ejercicio 11.17.** Una plataforma horizontal tiene altura prescrita $y_s(t)=y_0+At^2/2$. Un cuerpo mantiene contacto con ella bajo peso y normal. Obtén sus velocidad y aceleración verticales, la normal y su condición de admisibilidad. ¿Queda fijado su movimiento horizontal?

**Solución.** El contacto sostenido impone $y=y_s$, de donde $v_y=At$ y $a_y=A$. Newton vertical exige $N=m(g+A)$, admisible sólo si $A\geq-g$ y los datos iniciales acompañan la plataforma. Si $A<-g$, la normal sería negativa y la rama se rechaza. La relación de altura no fija la coordenada horizontal: para un soporte liso infinito y sin fuerza horizontal, la velocidad horizontal será constante según sus datos, no necesariamente cero. El soporte móvil impone una parte del movimiento y no toda la historia.

[]{#fispm-t1-c11-e0018}

**Ejercicio 11.18.** El centro de una guía circular de radio $2\,\mathrm m$ tiene aceleración $(1,0)\,\mathrm{m\,s^{-2}}$. En un instante, la posición relativa del cuerpo es $(2,0)\,\mathrm m$ y su velocidad relativa $(0,3)\,\mathrm{m\,s^{-1}}$. Determina la condición sobre su aceleración inercial y compárala con la guía fija.

**Solución.** proposición 11.12 da $2(a_x-1)=-9$ y, por tanto, $a_x=-3{,}5\,\mathrm{m\,s^{-2}}$. La guía fija habría requerido $a_x=-4{,}5\,\mathrm{m\,s^{-2}}$, como en el ejercicio 11.9. La componente tangencial instantánea $a_y$ no queda fijada por esta relación normal y necesita el balance de fuerzas. El cálculo no exige conocer la velocidad absoluta del centro si ya se dio la velocidad relativa, pero ésta no debe confundirse con la velocidad del cuerpo respecto del suelo.

[]{#cuña-móvil-y-geometría-compartida}

[]{#fispm-t1-c11-s10}

[]{#fpm-i-11-s10}

## 11.10. Cuña móvil y geometría compartida {#fispm-c11-cuuxf1a-muxf3vil-y-geometruxeda-compartida}

Una cuña que desliza sobre una mesa muestra por qué una aceleración relativa no debe entrar sola en Newton. El cuerpo que baja sobre ella se mueve respecto de la cuña y ésta se mueve respecto de la mesa. Usaremos coordenadas que reconstruyan ambas posiciones, conservando ejes inerciales horizontales y verticales.[^7]

[]{#fig:I-11-N04}

![**Figura 11.6.** Si $X$ sitúa el pie izquierdo de la cuña y $s$ mide la distancia del bloque cuesta arriba, $x=X+s\cos\alpha$ e $y=s\sin\alpha$. La posición horizontal mezcla ambas coordenadas. Véase §[11.10](#fispm-c11-cuuxf1a-muxf3vil-y-geometruxeda-compartida).](/assets/books/fispm/v04/I-11-N04.svg "fig:"){.fpm-v04-figure fig-alt="Coordenadas compartidas de una cuña" width="340px" fig-cap=""}

Sea la pendiente ascendente hacia la derecha, con $0<\theta<\pi/2$. La cuña tiene masa $M>0$ y posición horizontal $X$. Un cuerpo de masa $m>0$ desliza sin fricción sobre su plano. Elegimos

$$e_t=(\cos\theta,\sin\theta),\qquad e_n=(-\sin\theta,\cos\theta).$$

[]{#fispm-t1-c11-d0012}

**Definición 11.12 --- Coordenada de deslizamiento sobre una cuña en traslación.** Mientras persiste el contacto y la cuña conserva orientación fija, describimos la posición del cuerpo mediante

$$\mathbf r=Xe_x+s e_t+\mathbf r_*,$$

con $\mathbf r_*$ constante y $s$ firmado hacia arriba de la pendiente. $X$ y $s$ son las dos coordenadas independientes de posición del conjunto en esta rama. La mesa se declara lisa y la cuña se mantiene horizontalmente orientada, sin vuelco. El modelo trata su traslación y omite la dinámica rotacional; supone además una distribución y geometría capaces de mantener el apoyo. Estas hipótesis evitan convertir un resultado de traslación en una afirmación sobre la estabilidad de cualquier cuña real.

[]{#fispm-t1-c11-p0013}

**Proposición 11.13 --- Aceleraciones de un cuerpo sobre una cuña móvil.** Con $A=\ddot X$, la aceleración del cuerpo es

$$\mathbf a=Ae_x+\ddot s e_t.$$

En componentes adaptadas al plano, $a_t=A\cos\theta+\ddot s,\qquad a_n=-A\sin\theta.$

**Demostración.** Derivar dos veces definición 11.12 produce la primera expresión porque la orientación es fija. Sus productos escalares con $e_t$ y $e_n$ dan las otras. La posición relativa normal constante elimina la aceleración normal relativa, pero no la componente normal inercial de $Ae_x$. $\square$

El último término es decisivo. Escribir $a_n=0$ para el cuerpo equivaldría a tratar el plano como fijo, aunque se haya declarado cuña móvil. La posición normal sólo es constante respecto de la cuña. El contacto debe producir también la parte de aceleración inercial que acompaña su desplazamiento.

[]{#fispm-t1-c11-p0014}

**Proposición 11.14 --- Cuña libre y cuerpo sin fricción.** Bajo gravedad uniforme, contacto liso y mesa lisa, sin otra fuerza horizontal sobre la cuña, la rama de contacto satisface

$$A=\frac{mg\sin\theta\cos\theta}{M+m\sin^2\theta},$$

$$\ddot s=-\frac{(M+m)g\sin\theta}{M+m\sin^2\theta},\qquad N=\frac{mMg\cos\theta}{M+m\sin^2\theta}.$$

**Demostración.** Sobre el cuerpo actúan peso y $Ne_n$. Newton tangencial con la proposición 11.13 da $m(A\cos\theta+\ddot s)=-mg\sin\theta$. Newton normal da $-mA\sin\theta=N-mg\cos\theta$, o $N=m(g\cos\theta-A\sin\theta)$. La cuña recibe la reacción opuesta del cuerpo, cuya componente horizontal es $N\sin\theta$; la mesa no aporta fuerza horizontal, así que $MA=N\sin\theta$. Sustituir $N$ produce $(M+m\sin^2\theta)A=mg\sin\theta\cos\theta$. El denominador es positivo. Despejar y volver a los otros balances da las fórmulas. También $N>0$ bajo las hipótesis angulares y de masas, por lo que el contacto calculado es admisible. $\square$

El cuerpo y la cuña reciben fuerzas de contacto opuestas, pero sus aceleraciones no son opuestas de igual magnitud. El cuerpo tiene movimiento vertical y relativo además de la traslación compartida. En las ecuaciones individuales aparecen esas componentes y masas diferentes. La tercera ley no reemplaza proposición 11.13 ni determina la razón de aceleraciones.

La mesa debe sostener verticalmente la cuña. La reacción del cuerpo sobre ella tiene componente vertical $-N\cos\theta$, de modo que la normal total de la mesa es $Mg+N\cos\theta>0$ en este modelo de traslación. Esto comprueba el signo del apoyo sin desarrollar el problema de momentos y vuelco, que quedó fuera de las hipótesis.

Si la cuña está sujeta, el soporte suministra además fuerza horizontal y ya no vale $MA=N\sin\theta$ para una cuña libre. La condición $A=0$ produce $\ddot s=-g\sin\theta$ y $N=mg\cos\theta$, el plano fijo del capítulo 10. Cambiar el modo de sostener la cuña modifica un balance físico, aunque su ecuación geométrica instantánea conserve la forma.

[]{#fispm-t1-c11-mp0010}

**Principio metodológico 11.10 --- Reconstruir la aceleración del receptor.** Antes de proyectar Newton, expresa la posición inercial mediante las coordenadas compartidas y derívala. Escribe por separado el balance del soporte cuando éste sea libre. Una posición relativa constante no implica una aceleración inercial nula.

[]{#ejercicios-9}

### 11.10.1. Ejercicios {#fispm-c11-ejercicios-9}

[]{#fispm-t1-c11-e0019}

**Ejercicio 11.19.** En proposición 11.14, toma $M=3\,\mathrm{kg}$, $m=1\,\mathrm{kg}$, $\theta=30^\circ$ y $g=10\,\mathrm{m\,s^{-2}}$. Calcula $A$, $\ddot s$ y $N$, y verifica el balance horizontal de la cuña.

**Solución.** El denominador es $3+1/4=13/4$ en kilogramos. Las expresiones dan

$$A=\frac{10\sqrt3}{13}\,\mathrm{m\,s^{-2}},\qquad \ddot s=-\frac{80}{13}\,\mathrm{m\,s^{-2}},\qquad N=\frac{60\sqrt3}{13}\,\mathrm N.$$

La cuña satisface $MA=30\sqrt3/13\,\mathrm N=N\sin30^\circ$. Sobre el cuerpo, $a_n=-A/2$; no es cero. Su aceleración horizontal es $A+\ddot s\cos30^\circ=-30\sqrt3/13\,\mathrm{m\,s^{-2}}$, coherente con la fuerza horizontal $-N/2$ dividida por su masa. El movimiento relativo cuesta abajo y la cuña hacia la derecha se combinan en el marco inercial.

[]{#fispm-t1-c11-e0020}

**Ejercicio 11.20.** Mantén $m$ y $\theta$ fijos y examina las expresiones de la proposición 11.14 cuando $M$ crece sin cota. Compara ese límite con una cuña sujeta. ¿Permite concluir que una cuña de masa finita está exactamente inmóvil?

**Solución.** Al dividir numeradores y denominador por $M$, se obtiene $A\to0$, $\ddot s\to-g\sin\theta$ y $N\to mg\cos\theta$. Coinciden con los resultados del soporte fijo como límite de masas. Para cualquier $M$ finita y ángulo interior, el numerador de $A$ es positivo y $A>0$: la cuña libre no está exactamente inmóvil. La cuña sujeta tiene $A=0$ porque una interacción externa modifica su balance horizontal, no porque se le haya asignado una masa grande. El límite aproxima una respuesta; no elimina una fuerza que el caso sujeto requiere.

[]{#péndulo-y-reacción-en-un-vínculo-curvo}

[]{#fispm-t1-c11-s11}

[]{#fpm-i-11-s11}

## 11.11. Péndulo y reacción en un vínculo curvo {#fispm-c11-puxe9ndulo-y-reacciuxf3n-en-un-vuxednculo-curvo}

Una cuerda tensa puede restringir una masa a una circunferencia sin imponer rapidez constante. Para estudiar el péndulo basta distinguir la ecuación tangencial que modifica esa rapidez y el balance radial que determina la tensión. No resolveremos todavía su período ni su evolución mediante energía.[^8]

[]{#fig:I-11-N05}

![**Figura 11.7.** Sobre la masa del péndulo actúan peso y tensión. La tensión apunta al soporte; la componente radial de Newton contiene $mv^2/\ell$, aunque la longitud sea constante. Véase §[11.11](#fispm-c11-puxe9ndulo-y-reacciuxf3n-en-un-vuxednculo-curvo).](/assets/books/fispm/v04/I-11-N05.svg "fig:"){.fpm-v04-figure fig-alt="Fuerzas del péndulo" width="340px" fig-cap=""}

[]{#fispm-t1-c11-d0013}

**Definición 11.13 --- Péndulo simple en la rama tensa.** El modelo consta de una masa puntual $m>0$ unida a un punto fijo por una cuerda ideal de longitud $\ell>0$, bajo gravedad uniforme. El movimiento es plano; se desprecia resistencia. La igualdad de distancia $\ell$ sólo se mantiene cuando la cuerda está tensa y la tensión calculada es admisible.

Medimos $\theta$ desde la vertical descendente y elegimos

$$\mathbf r=\ell(\sin\theta,-\cos\theta),\qquad e_r=(\sin\theta,-\cos\theta),\qquad e_\theta=(\cos\theta,\sin\theta).$$

La aceleración es $-\ell\dot\theta^2e_r+\ell\ddot\theta e_\theta$. Estos vectores de base cambian con el ángulo; la expresión procede de derivar la posición completa, como en el capítulo 8, no de tratar la base como constante.

[]{#fispm-t1-c11-p0015}

**Proposición 11.15 --- Ecuación angular y tensión del péndulo.** Durante una rama tensa regular,

$$\ddot\theta=-\frac g\ell\sin\theta,\qquad T=m\bigl(g\cos\theta+\ell\dot\theta^2\bigr).$$

**Demostración.** La fuerza de cuerda es $-Te_r$ y el peso $-mg e_y$. Sus componentes tangenciales suman $-mg\sin\theta$; Newton da $m\ell\ddot\theta=-mg\sin\theta$. Radialmente, el peso aporta $mg\cos\theta$ y Newton es $-m\ell\dot\theta^2=mg\cos\theta-T$. Despejar las dos ecuaciones produce las expresiones. $\square$

La tensión no es siempre $mg\cos\theta$. La diferencia $m\ell\dot\theta^2$ produce la aceleración hacia el centro necesaria para la curva. En el punto inferior, $T=mg+m\ell\dot\theta^2$, mayor que $mg$ si el cuerpo se mueve. En un punto de retorno con velocidad angular cero, el término cinemático desaparece, pero el balance tangencial puede seguir dando aceleración no nula.

[]{#fispm-t1-c11-p0016}

**Proposición 11.16 --- Admisibilidad de la rama tensa del péndulo.** La fórmula de la proposición 11.15 es compatible con una cuerda flexible sólo si

$$g\cos\theta+\ell\dot\theta^2\geq0.$$

En posiciones con $\cos\theta<0$, esto exige $\dot\theta^2\geq-g\cos\theta/\ell$. La condición comprueba la tensión de la rama; en igualdad, su continuación requiere examinar la evolución y no sólo ese valor instantáneo.

**Demostración.** definición 10.7 exige $T\geq0$. Como $m>0$, sustituir proposición 11.15 equivale a la desigualdad. Cuando $\cos\theta<0$, despejar el término cuadrático da el límite indicado. La igualdad permite tensión cero y no determina por sí misma las fuerzas ni la geometría posteriores. $\square$

Una varilla rígida bilateral permite una fuerza axial de ambos signos dentro del modelo. Puede sostener una masa en una posición donde la cuerda tendría que empujar. Cambiar cuerda por varilla conserva una igualdad de distancia y cambia la interacción admisible. La geometría sola no distingue esos dispositivos.

La ecuación angular tiene un resultado útil aun sin resolverla: en $0<\theta<\pi$, la aceleración angular es negativa. Esto no impone velocidad angular negativa en ese instante; puede estar frenando una velocidad positiva. Tampoco permite calcular una rapidez en otra posición sin integrar la dinámica o usar herramientas posteriores. Una condición local en el punto superior no se debe anunciar como un umbral de lanzamiento desde el punto inferior sin el cálculo que los conecte.

[]{#fispm-t1-c11-mp0011}

**Principio metodológico 11.11 --- Separar ecuación tangencial y capacidad radial.** Obtén la aceleración normal desde la curva, determina la tensión por Newton radial y comprueba su signo. Usa el balance tangencial para la evolución de la rapidez. No extrapoles un control instantáneo a todo el recorrido.

[]{#ejercicios-10}

### 11.11.1. Ejercicios {#fispm-c11-ejercicios-10}

[]{#fispm-t1-c11-e0021}

**Ejercicio 11.21.** Un péndulo tiene $\theta=\pi/3$ y velocidad angular nula en un instante de su rama tensa. Calcula tensión y aceleración angular. ¿La velocidad nula implica equilibrio?

**Solución.** proposición 11.15 da $T=mg/2>0$ y $\ddot\theta=-\sqrt3g/(2\ell)$. La rama es admisible y la aceleración tangencial no es cero. El reposo instantáneo no es equilibrio: el peso tiene una componente tangencial que inicia o cambia el movimiento. La aceleración radial sí es cero en ese instante porque la rapidez es cero; eso no elimina la aceleración completa.

[]{#fispm-t1-c11-e0022}

**Ejercicio 11.22.** La masa pasa por el punto superior con rapidez $V$. Calcula la tensión y la condición local para una rama tensa. ¿El resultado basta para fijar una rapidez mínima inicial en el punto inferior?

**Solución.** En $\theta=\pi$, $\cos\theta=-1$ y $\ell\dot\theta^2=V^2/\ell$. Por tanto, $T=m(V^2/\ell-g)$ y la rama exige $V^2\geq g\ell$. El resultado se refiere a la rapidez ya dada en el punto superior. No establece cómo se relaciona con una rapidez inicial inferior: falta resolver la evolución y controlar la tensión en el recorrido. La igualdad corresponde a tensión nula, cuyo mantenimiento no se deduce sólo del dato instantáneo.

[]{#fispm-t1-c11-e0023}

**Ejercicio 11.23.** La masa está en el punto superior con velocidad cero. Compara una cuerda flexible con una varilla bilateral ideal. Determina una continuación inicial admisible para la cuerda y la fuerza axial que requiere el reposo con varilla.

**Solución.** La rama circular de cuerda exigiría $T=-mg$ y es inadmisible. Con cuerda floja y origen en el punto de suspensión, la posición inicial es $(0,\ell)$ y la caída libre inicial da $\mathbf r(t)=(0,\ell-gt^2/2)$: para tiempos positivos suficientemente pequeños, la distancia es menor que $\ell$ y la cuerda no tracciona. La solución verifica la rama floja sin mantener artificialmente la circunferencia. La varilla puede ejercer fuerza $+mg e_r$, hacia arriba en el punto superior, y equilibrar el peso. Si se expresa como $-Se_r$, su componente axial firmada es $S=-mg$, una compresión admisible para la varilla. No se afirma aquí estabilidad de ese equilibrio.

[]{#contacto-unilateral-y-pérdida-del-vínculo}

[]{#fispm-t1-c11-s12}

[]{#fpm-i-11-s12}

## 11.12. Contacto unilateral y pérdida del vínculo {#fispm-c11-contacto-unilateral-y-puxe9rdida-del-vuxednculo}

Una guía bilateral impone su geometría mediante fuerzas de cualquiera de los dos signos. Una superficie de apoyo sólo puede empujar al cuerpo hacia la región accesible. La diferencia cambia la lectura de una solución: primero se calcula la reacción que exigiría el contacto y después se comprueba que la superficie puede ejercerla. Si el signo es imposible, la ecuación de contacto deja de describir la trayectoria.

[]{#fispm-t1-c11-d0014}

**Definición 11.14 --- Separación y rama de contacto.** Para un obstáculo circular fijo de radio $R>0$, centrado en el origen y accesible por el exterior, definimos $h=|\mathbf r|-R$. La región permitida es $h\geq0$. El contacto activo tiene $h=0$ y una reacción $Ne_r$, con $N\geq0$, dirigida hacia afuera. En una rama separada, $h>0$ y $N=0$. Estas condiciones se resumen como $h\geq0$, $N\geq0$, $Nh=0$. El producto nulo expresa que no hay fuerza de contacto a distancia; no sustituye a las ecuaciones de movimiento ni describe por sí solo un impacto.

El modelo supone superficie lisa, punto material, movimiento plano y gravedad uniforme. Se estudian ramas suaves, con posiciones y velocidades iniciales compatibles. La llegada con velocidad normal no nula requiere una ley de impacto que no se desarrolla en este capítulo. Tampoco se supone que toda solución que alcanza $N=0$ deba separarse inmediatamente: hay que estudiar la continuación.

En esta sección medimos $\theta$ desde la **vertical superior**. La convención es distinta de la del péndulo y se declara antes de proyectar:

$$e_r=(\sin\theta,\cos\theta),\qquad e_\theta=(\cos\theta,-\sin\theta).$$

Mientras hay contacto, $\mathbf r=Re_r$, $\mathbf v=R\dot\theta e_\theta$ y

$$\mathbf a=-\frac{v^2}{R}e_r+R\ddot\theta e_\theta, \qquad v^2=R^2\dot\theta^2.$$

La componente radial de la aceleración apunta hacia el centro incluso cuando la fuerza de contacto apunta hacia afuera. El peso debe aportar la diferencia. No se pueden identificar dirección de aceleración y dirección de reacción.

[]{#fispm-t1-c11-p0017}

**Proposición 11.17 --- Reacción en la cara exterior de una circunferencia.** En una rama de contacto del modelo anterior,

$$N=m\left(g\cos\theta-\frac{v^2}{R}\right),\qquad R\ddot\theta=g\sin\theta.$$

La rama exige $v^2/R\leq g\cos\theta$.

**Demostración.** El peso $(0,-mg)$ tiene componentes $-mg\cos\theta$ sobre $e_r$ y $mg\sin\theta$ sobre $e_\theta$. Newton da $-mv^2/R=N-mg\cos\theta$ y $mR\ddot\theta=mg\sin\theta$. La primera igualdad fija la reacción; la segunda fija la aceleración tangencial. La desigualdad procede de $N\geq0$, no de una nueva ecuación geométrica. En particular, si $\cos\theta<0$, ninguna rapidez permite esta rama exterior bajo las fuerzas especificadas. $\square$

Una partícula sobre una superficie curva no tiene, en general, la reacción $mg\cos\theta$ de un plano fijo. Aquí el término $mv^2/R$ es indispensable. La curvatura exige aceleración normal y modifica cuánto debe empujar la superficie. Esta distinción usa la misma cinemática radial que el péndulo, pero con otro sentido de reacción y otra región accesible.[^9]

[]{#fispm-t1-c11-p0018}

**Proposición 11.18 --- Rechazo local de una reacción negativa.** Supongamos $h=0$, $\dot h=0$ y velocidad tangencial de magnitud $v$ en un instante inicial. Si proposición 11.17 exige $N<0$, la continuación libre bajo el peso abre una separación positiva para tiempos suficientemente pequeños.

**Demostración.** Para $\rho=|\mathbf r|>0$, diferenciamos $\rho^2=\mathbf r\cdot\mathbf r$ dos veces. Resulta $\dot\rho^2+\rho\ddot\rho=|\mathbf v|^2+\mathbf r\cdot\mathbf a$. En el instante inicial, $\rho=R$, $\dot\rho=0$ y la aceleración libre es $(0,-g)$. Por tanto,

$$\ddot h=\frac{v^2}{R}-g\cos\theta.$$

La condición $N<0$ de la proposición 11.17 hace positiva esta cantidad. Con $h(0)=\dot h(0)=0$, la expansión $h(\tau)=\tfrac12\ddot h(0)\tau^2+o(\tau^2)$ implica $h(\tau)>0$ para $\tau>0$ suficientemente pequeño. La caída libre satisface entonces la región accesible y $N=0$. La trayectoria circular que exigía una superficie atractiva se descarta. $\square$

Esta prueba decide una situación local concreta. No establece toda la historia posterior ni garantiza ausencia de nuevos encuentros. Además, cuando $N=0$, el término cuadrático puede anularse: conocer aceleración normal nula de separación no basta para decidir el contacto. El ejercicio siguiente muestra una apertura de orden superior sin recurrir al trabajo ni a una integral de energía.

[]{#fispm-t1-c11-mp0012}

**Principio metodológico 11.12 --- Resolver y comprobar un contacto.** Declara la región accesible y el signo de la reacción. Resuelve Newton con la igualdad geométrica activa. Comprueba el signo de la fuerza obtenida y la compatibilidad inicial de posición y velocidad. Si la fuerza requerida es negativa, pasa a la rama sin contacto y verifica que su trayectoria entre en la región permitida. Si la fuerza es cero, estudia la continuación en lugar de decidir sólo por ese valor. Una velocidad que atraviesa la superficie requiere otro modelo, no una corrección arbitraria de signos.

[]{#ejercicios-11}

### 11.12.1. Ejercicios {#fispm-c11-ejercicios-11}

[]{#fispm-t1-c11-e0024}

**Ejercicio 11.24.** Una partícula toca la cara exterior con $\theta=\pi/3$ y $v^2/R=g/4$. Calcula la reacción y la aceleración tangencial. Decide si el signo permite la rama.

**Solución.** proposición 11.17 da $N=m(g/2-g/4)=mg/4>0$ y $a_\theta=R\ddot\theta=\sqrt3g/2$. La aceleración radial es $-g/4$ sobre $e_r$. El contacto es admisible en ese instante; por continuidad de una solución suave y del valor positivo de $N$, permanece admisible en un intervalo suficientemente pequeño si los restantes datos pertenecen a la rama. No se ha determinado el primer instante futuro de pérdida del contacto.

[]{#fispm-t1-c11-e0025}

**Ejercicio 11.25.** En el punto superior $\mathbf r(0)=(0,R)$, la velocidad es horizontal $(V,0)$. Examina la continuación libre para $V^2=2gR$ y para $V^2=gR$. ¿La igualdad $N=0$ garantiza contacto persistente?

**Solución.** En el primer caso, proposición 11.17 exige $N=m(g-2g)=-mg$. La rama circular es inadmisible y proposición 11.18 da $\ddot h=g>0$. La trayectoria libre es $\mathbf r(t)=(Vt,R-gt^2/2)$. Su norma al cuadrado vale

$$|\mathbf r(t)|^2=R^2+(V^2-gR)t^2+\frac{g^2t^4}{4}.$$

Para $V^2=2gR$, es mayor que $R^2$ en tiempos positivos y confirma la separación. Para $V^2=gR$, la reacción candidata inicial y $\ddot h(0)$ son cero, pero la misma expresión queda $R^2+g^2t^4/4>R^2$ para $t>0$. La rama libre es admisible y abre $h(t)=g^2t^4/(8R)+o(t^4)$. Por eso, el valor nulo de la reacción en un solo instante no garantiza permanencia. Se ha comprobado una continuación local separada; no se ha introducido una ley de impacto ni una regla universal para todos los contactos marginales.

[]{#sistemas-con-varias-cuerdas}

[]{#fispm-t1-c11-s13}

[]{#fpm-i-11-s13}

## 11.13. Sistemas con varias cuerdas {#fispm-c11-sistemas-con-varias-cuerdas}

Una segunda cuerda aporta su propia conservación de longitud. También aporta su propia tensión, salvo que un balance justifique una relación con la tensión de otra cuerda. Confundir ambas afirmaciones produce dos errores frecuentes: contar las mismas posiciones varias veces y transmitir una única tensión a través de cuerdas físicamente distintas.

[]{#fispm-t1-c11-d0015}

**Definición 11.15 --- Cuerdas distintas y tensiones asignadas.** En el modelo ideal, cada cuerda continua, inextensible y tensa tiene longitud fija y una magnitud de tensión común a sus tramos si las poleas correspondientes satisfacen las hipótesis ideales. A cuerdas distintas se les asignan inicialmente tensiones distintas. La igualdad o proporción entre ellas debe resultar de las ecuaciones de los cuerpos o de las poleas, no del hecho de pertenecer al mismo montaje.

Consideremos una máquina doble de Atwood. Una cuerda superior pasa por una polea fija: un extremo sostiene $m_1$ y el otro sostiene el centro de una polea inferior móvil. Una cuerda inferior pasa por esta segunda polea y sostiene $m_2$ y $m_3$. Las tres masas son positivas; las poleas y cuerdas son ideales, los tramos móviles son verticales y no hay contactos entre los cuerpos. La geometría mantiene los arcos constantes en el intervalo considerado. Denotamos por $Y$ la altura del centro inferior y por $y_1,y_2,y_3$ las alturas de las masas, todas positivas **hacia abajo**, respecto de referencias fijas.

Las longitudes constantes se escriben

$$y_1+Y=C_1,\qquad y_2+y_3-2Y=C_2.$$

En la cuerda inferior, subir o bajar el centro altera los dos tramos rectos. El signo menos procede de medir cada longitud desde ese centro hasta el cuerpo situado debajo. Las constantes recogen las partes fijas y las referencias elegidas; su valor no altera las relaciones entre velocidades o aceleraciones.[^10]

[]{#fispm-t1-c11-p0019}

**Proposición 11.19 --- Geometría y grados de libertad de la máquina doble.** El sistema tiene dos grados de libertad de posición en esta rama. Eliminando $Y$,

$$2y_1+y_2+y_3=C_3, \qquad 2\dot y_1+\dot y_2+\dot y_3=0, \qquad 2a_1+a_2+a_3=0,$$

con $C_3=C_2+2C_1$.

**Demostración.** La primera longitud da $Y=C_1-y_1$. Sustituirla en la segunda produce $y_3=C_3-2y_1-y_2$. Por tanto, elegidos $y_1$ y $y_2$ dentro de un intervalo abierto que respete la disposición física, se recuperan $Y$ y $y_3$ de modo único. Los cambios independientes de $y_1$ y $y_2$ producen cambios de posición de primer orden y no hay una tercera relación de longitud. La parametrización tiene dos parámetros regulares. Diferenciar la igualdad eliminada da las otras dos relaciones. $\square$

Se puede contar con cuatro alturas y dos ecuaciones independientes, o con tres alturas de masas y una ecuación después de eliminar el centro. Ambos procedimientos dan dos. Contar tres masas y restar dos cuerdas olvidando que la segunda polea tiene posición móvil daría uno y describiría otro sistema.

[]{#fispm-t1-c11-p0020}

**Proposición 11.20 --- Dinámica de la máquina doble ideal.** Si $T$ es la tensión inferior y $T_U$ la superior, entonces

$$T_U=2T,\qquad T=\frac{4g}{4/m_1+1/m_2+1/m_3},$$

$$a_1=g-\frac{2T}{m_1},\qquad a_2=g-\frac{T}{m_2},\qquad a_3=g-\frac{T}{m_3}.$$

**Demostración.** La polea inferior recibe dos tracciones $T$ hacia abajo y una $T_U$ hacia arriba. Su balance ideal de masa despreciable exige $T_U=2T$; se usa el balance límite del capítulo 10, sin dividir una ecuación por masa cero. Newton para las masas, con los ejes declarados, da

$$m_1g-2T=m_1a_1,\qquad m_2g-T=m_2a_2,\qquad m_3g-T=m_3a_3.$$

Al sustituir estas aceleraciones en la proposición 11.19, $0=4g-T\left(\frac4{m_1}+\frac1{m_2}+\frac1{m_3}\right).$

El coeficiente es positivo; la ecuación tiene la única solución indicada. Las otras fórmulas proceden de los tres balances. Para $g>0$, ambas tensiones son positivas, lo que permite la rama tensa mientras se mantenga la disposición geométrica. $\square$

La dimensión del denominador es inversa de masa; la de $T$ es fuerza. Los factores cuatro y dos tienen orígenes relacionados, pero no intercambiables: la longitud fija da el factor dos cinemático de $a_1$ y la polea móvil da el factor dos de fuerza sobre $m_1$. Ambos entran en el término $4/m_1$ al eliminar las aceleraciones.

Los dos grados de libertad no impiden escribir tres balances para las masas. Las aceleraciones están vinculadas y las reacciones son incógnitas adicionales; resolver el sistema completo permite recuperar las fuerzas. Una reducción puede ser útil, pero debe conservar la información necesaria para calcular tensiones y comprobar su admisibilidad. La uniformidad de tensión dentro de cada cuerda tampoco implica $T_U=T$ entre ambas: el balance de la polea demuestra aquí que esa igualdad sería incorrecta.

Es útil comprobar también la conservación de las dos longitudes originales después de eliminar el centro. Recuperamos $Y=C_1-y_1$ y sustituimos las posiciones calculadas: la longitud inferior se reduce a $2y_1+y_2+y_3-2C_1=C_2$. Si el residuo de la relación eliminada es cero, se recupera la segunda cuerda; si se verifican sólo las aceleraciones, faltan todavía las dos condiciones iniciales de esa relación. No es necesario integrar para verificar los balances de fuerza, pero sí aportar posiciones iniciales para decidir cuánto tiempo permite la disposición física. Una solución con aceleraciones constantes puede alcanzar el extremo de un recorrido finito. En ese evento cambia el problema aunque las fórmulas algebraicas sigan dando valores positivos de tensión. Por eso, positividad de las tensiones y disponibilidad de la geometría son comprobaciones distintas y ambas pertenecen a la interpretación del resultado.

[]{#fispm-t1-c11-mp0013}

**Principio metodológico 11.13 --- Separar longitudes y tensiones.** Nombra cada cuerda y escribe su longitud con todas las posiciones móviles que alteran sus tramos. Elimina posiciones auxiliares antes de contar parámetros libres. Asigna una tensión a cada cuerda ideal continua y escribe los balances de los elementos que conectan cuerdas distintas. Finalmente resuelve Newton junto con las relaciones de aceleración y comprueba los signos. No impongas igualdad de movimientos sólo porque dos masas sean iguales.

[]{#ejercicios-12}

### 11.13.1. Ejercicios {#fispm-c11-ejercicios-12}

[]{#fispm-t1-c11-e0026}

**Ejercicio 11.26.** En la máquina doble, las tres masas valen $m$. Calcula tensiones y aceleraciones, y verifica los balances.

**Solución.** El denominador de la proposición 11.20 es $6/m$, de modo que $T=2mg/3$ y $T_U=4mg/3$. Así $a_1=-g/3$ y $a_2=a_3=g/3$: la masa superior sube y las inferiores bajan. Newton para $m_1$ da $mg-4mg/3=-mg/3$; para cada masa inferior, $mg-2mg/3=mg/3$. La geometría da $2(-g/3)+g/3+g/3=0$. Además, $\ddot Y=-a_1=g/3$, compatible con el movimiento del centro inferior. Todas las fuerzas y las longitudes usan el mismo eje descendente.

[]{#fispm-t1-c11-e0027}

**Ejercicio 11.27.** Encuentra las relaciones de masas para que las tres aceleraciones sean cero. ¿Deben estar en reposo?

**Solución.** Si $a_2=a_3=0$, los balances inferiores exigen $T=m_2g=m_3g$, luego $m_2=m_3$. Si además $a_1=0$, $2T=m_1g$, de donde $m_1=2m_2$. Recíprocamente, esas relaciones sustituidas en la proposición 11.20 dan $T=m_2g$ y las tres aceleraciones nulas. Las velocidades pueden ser constantes y no nulas si satisfacen $2\dot y_1+\dot y_2+\dot y_3=0$. El reposo requiere, además, velocidades iniciales cero. La solución sólo continúa mientras las posiciones permitan los tramos y contactos supuestos.

[]{#fispm-t1-c11-e0028}

**Ejercicio 11.28.** Las tres masas son iguales. En un instante inicial compatible, $\dot y_1=0$, $\dot y_2=V$ y $\dot y_3=-V$. Decide si la simetría de masas obliga a que $y_2-y_3$ permanezca constante.

**Solución.** Los datos satisfacen la longitud diferenciada, pues $2(0)+V-V=0$. Por ejercicio 11.26, $a_2=a_3=g/3$, de modo que la segunda derivada de $y_2-y_3$ es cero. Su primera derivada inicial es $2V$, y por tanto

$$y_2(t)-y_3(t)=y_2(0)-y_3(0)+2Vt.$$

La igualdad de aceleraciones no elimina la diferencia inicial de velocidades. El centro inferior tiene $\dot Y(0)=0$ y $\ddot Y=g/3$, mientras los extremos pueden desplazarse relativamente con velocidades opuestas. Este movimiento exhibe el segundo grado de libertad. Imponer además $y_2=y_3$ requeriría posición inicial igual y $V=0$; la simetría de las ecuaciones no autoriza borrar datos compatibles.

[]{#síntesis-conteo-datos-y-admisibilidad}

[]{#fispm-t1-c11-s14}

[]{#fpm-i-11-s14}

## 11.14. Síntesis: conteo, datos y admisibilidad {#fispm-c11-suxedntesis-conteo-datos-y-admisibilidad}

El conteo geométrico responde cuántas posiciones independientes describen una rama. Newton responde cómo evoluciona con las fuerzas especificadas. Los signos de tensión y reacción responden si los elementos físicos pueden sostener esa rama. Son preguntas conectadas, pero resolver una no equivale a resolver las demás.

  Modelo y rama                                    Parámetros de posición libres            Comprobación física decisiva
  ------------------------------------------------ ---------------------------------------- ----------------------------------------------------------
  Circunferencia fija en un plano                  Un ángulo local                          Fuerza radial requerida por la rapidez
  Circunferencia con centro prescrito              Un ángulo local                          Reacción y movimiento conocido del soporte
  Cuña libre con partícula en contacto             Desplazamiento de cuña y deslizamiento   Newton de ambos cuerpos y $N\geq0$
  Péndulo de cuerda tensa                          Un ángulo local                          $T\geq0$ durante la evolución
  Partícula separada de superficie plana o curva   Dos coordenadas en el plano              Región accesible y reacción nula
  Máquina doble de Atwood                          Dos alturas independientes               Dos longitudes y dos tensiones relacionadas por la polea

El cuadro se refiere a las hipótesis de cada sección. Prescribir un movimiento que antes era incógnita reduce las posiciones libres en un instante, pero introduce datos dependientes del tiempo. Una coordenada ya conocida puede tener velocidad y aceleración no nulas. Tampoco desaparecen las fuerzas necesarias para imponerla.

Para un sistema descrito por $n$ parámetros libres con ecuaciones de segundo orden, normalmente hay que dar $n$ posiciones y $n$ velocidades iniciales compatibles. Este enunciado señala el tipo de datos que usan los modelos del capítulo; no constituye un teorema general de existencia ni cubre impactos o puntos singulares. En una representación con coordenadas redundantes, las posiciones y velocidades deben cumplir las relaciones de vínculo antes de integrar.

[]{#fispm-t1-c11-p0021}

**Proposición 11.21 --- Conservación de relaciones afines a partir de datos compatibles.** Sean, en un intervalo, relaciones $\sum_j c_{ij}q_j(t)=b_i(t)$, con coeficientes constantes y funciones dos veces diferenciables. Si se cumplen las relaciones de aceleración $\sum_j c_{ij}\ddot q_j=\ddot b_i$ y, en un instante inicial, las relaciones de posición y velocidad, entonces las relaciones de posición se mantienen en todo el intervalo.

**Demostración.** Para cada ecuación, definimos el residuo $u_i(t)=\sum_jc_{ij}q_j(t)-b_i(t)$. La hipótesis de aceleraciones da $\ddot u_i=0$, así que $u_i(t)=u_i(t_0)+\dot u_i(t_0)(t-t_0)$. Las condiciones iniciales hacen cero ambos coeficientes. Luego $u_i(t)=0$ en todo el intervalo. El argumento no presupone que las relaciones sean independientes; si alguna es redundante, su conservación no añade un grado de restricción. $\square$

Proposición 11.21 explica por qué es legítimo usar ecuaciones de aceleración para las cuerdas del capítulo una vez verificados los datos iniciales. También explica el fallo de usarlas para reparar una longitud inicial errónea: el residuo no desaparece sólo porque su segunda derivada sea cero. En relaciones no afines, hay que volver a diferenciar la geometría completa; proposición 11.6 y proposición 11.12 muestran términos de rapidez que no se pueden omitir.

Las trayectorias deben interpretarse en intervalos donde se cumplen las hipótesis. Si una cuerda pierde tensión, una partícula abandona una superficie o dos cuerpos se encuentran, no se prolonga automáticamente la misma ecuación de vínculo. Se identifican los nuevos datos de posición y velocidad y se formula la rama posterior; cuando existe choque, hace falta un modelo adicional para la discontinuidad de velocidad. Esta limitación no afecta a la validez del cálculo anterior al evento, pero sí a su extensión.

[]{#fispm-t1-c11-mp0014}

**Principio metodológico 11.14 --- Cerrar un modelo elemental de vínculos.** Revisa la secuencia completa: coordenadas y sentidos positivos; relaciones de posición con sus constantes; eliminación y parámetros libres; velocidades iniciales compatibles; relaciones de aceleración; fuerzas sobre cada cuerpo; solución; signos admisibles; intervalo de validez. Si un resultado contradice una condición unilateral, cambia la rama física. Si contradice la longitud inicial, corrige la formulación del problema antes de interpretar la integración. Conserva las reacciones cuando su valor sea parte de lo que se quiere conocer.

[]{#ejercicios-13}

### 11.14.1. Ejercicios {#fispm-c11-ejercicios-13}

[]{#fispm-t1-c11-e0029}

**Ejercicio 11.29.** Un cálculo impone $a_1+2a_2=0$ para una polea móvil, pero empieza con $y_1(0)+2y_2(0)-L=\delta$ y $\dot y_1(0)+2\dot y_2(0)=\eta$. Determina el residuo de longitud y explica cuándo el cálculo representa la cuerda original.

**Solución.** Sea $u=y_1+2y_2-L$. La ecuación de aceleración implica $\ddot u=0$. Con los datos dados,

$$u(t)=\delta+\eta t.$$

La longitud original se conserva exactamente sólo si $\delta=\eta=0$. Si $\eta=0$ y $\delta\ne0$, se conserva otra longitud, no la declarada. Si $\eta\ne0$, ni siquiera se conserva una longitud fija. Hacer cero la aceleración del residuo no lo hace cero. Cambiar las posiciones o velocidades iniciales sin una justificación física crea otro problema; un eventual tensado brusco requiere un modelo de transición que aquí no se ha supuesto.

[]{#fispm-t1-c11-e0030}

**Ejercicio 11.30.** Dos masas $m_1,m_2>0$ se desplazan en una guía horizontal lisa, con $y_1=y_2=0$. Una varilla bilateral ideal impone $x_2-x_1=\ell>0$. Cuenta los grados de libertad, examina la ecuación adicional $2(x_2-x_1)=2\ell$ y prescribe después $x_1=X_0+At^2/2$. Un actuador ejerce sobre la masa 2 una fuerza horizontal firmada $F$. Calcula $F$ y la fuerza axial firmada $S$, definida positiva hacia la derecha sobre la masa 1.

**Solución.** De cuatro coordenadas, las dos condiciones de guía fijan las alturas y la varilla permite escribir $x_2=x_1+\ell$. Queda una posición libre. La ecuación multiplicada por dos es redundante y no cambia el conteo. Prescribir $x_1=X(t)$ determina ambas posiciones: quedan cero grados de libertad de posición en cada instante, aunque ambas masas se muevan. Sus aceleraciones son $A$.

La varilla ejerce $S$ sobre la masa 1 y $-S$ sobre la masa 2, por acción y reacción. Los balances horizontales son $S=m_1A$ y $F-S=m_2A$. De aquí

$$S=m_1A,\qquad F=(m_1+m_2)A.$$

Las reacciones verticales valen $m_1g$ y $m_2g$. La varilla admite ambos signos de $S$: para $A>0$ tira de la masa 1 hacia la derecha; para $A<0$ la empuja hacia la izquierda. Una cuerda flexible no permitiría automáticamente esa segunda rama. La posición prescrita fija el movimiento y determina la fuerza del actuador; imponer simultáneamente una fuerza arbitraria distinta sobredeterminaría ese modelo. El ejemplo muestra que cero posiciones libres no significa ausencia de movimiento, aceleración o fuerzas de vínculo.

La herramienta adquirida es concreta: escribir la geometría que permanece activa, identificar las posiciones verdaderamente libres y combinar sus derivadas con Newton sin perder las condiciones físicas. El capítulo 12 estudiará trabajo, potencia y energía cinética, lo que permitirá comparar estados del movimiento mediante otra forma de organizar las mismas leyes. El formalismo general del espacio de configuración y el principio de d'Alembert se reservan para el capítulo 25.

[^1]: Daniel Kleppner y Robert Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 2, §2.4, pp. 69--70: ecuaciones de movimiento y restricciones. Las definiciones y distinciones locales se desarrollan aquí; no se atribuye a ese pasaje una teoría general de grados de libertad.

[^2]: Kleppner--Kolenkow, obra citada, cap. 2, §2.4, ejemplo 2.4, pp. 74--75: cuña, polea con soporte móvil y relación de longitudes. El conteo por eliminación, la redundancia y los ejemplos singulares de §§3--4 son desarrollos propios, con argumentos explícitos.

[^3]: Kleppner--Kolenkow, obra citada, cap. 2, §2.4, ejemplos 2.5--2.6, pp. 75--76. Se consulta la aceleración radial y la admisibilidad de la tensión. Proposición 11.6 obtiene sus condiciones directamente por diferenciación y usa la cinemática del capítulo 8 como enlace interno.

[^4]: David Morin, *Introduction to Classical Mechanics: With Problems and Solutions*, Cambridge University Press, 2008, cap. 3, §3.2, pp. 58--59: separación entre balances de Newton y conservación de longitud. La máquina fija de la proposición 11.9 se resuelve en el texto; ejercicio 11.14 desarrolla el soporte móvil a partir de la geometría del ejemplo 2.4 de Kleppner--Kolenkow, pp. 74--75.

[^5]: Morin, obra citada, cap. 3, §3.2, ejemplo de máquina de Atwood, pp. 58--59. Se adapta la convención a ejes descendentes y se conserva el factor dos de longitud y fuerza. La masa despreciable se trata mediante el balance ideal del capítulo 10, sin dividir por cero. Aceleración nula no se identifica automáticamente con reposo.

[^6]: Kleppner--Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 2, §2.4, ejemplo 2.4, pp. 74--75. El pasaje aporta geometrías con soportes móviles. Definiciones 11.10--11.11 y proposición 11.12 desarrollan explícitamente el cambio de variables con orientación fija, sin atribuir al ejemplo un tratamiento de ejes giratorios.

[^7]: Kleppner--Kolenkow, obra citada, cap. 2, §2.4, ejemplo 2.4(a), p. 74. Se usa la relación geométrica de la cuña; el sistema libre de la proposición 11.14 y sus reacciones se obtienen en el texto mediante Newton para ambos cuerpos.

[^8]: Kleppner--Kolenkow, obra citada, cap. 2, §2.4, ejemplo 2.6, p. 76: movimiento circular vertical y tensión admisible. Se declara una convención angular desde la vertical inferior y se derivan las ecuaciones exactas; no se desarrolla la aproximación de ángulo pequeño ni el periodo.

[^9]: La comparación con el vínculo circular de Kleppner--Kolenkow, ejemplo 2.6, p. 76, motiva distinguir aceleración radial y capacidad física del vínculo. El obstáculo exterior, proposiciones 11.17--11.18 y la separación de orden cuatro del ejercicio 11.25 se construyen y prueban aquí; no se atribuye ese caso completo al ejemplo bibliográfico.

[^10]: David Morin, *Introduction to Classical Mechanics: With Problems and Solutions*, Cambridge University Press, 2008, cap. 3, §3.6, problema 3.2, p. 71, y §3.8, solución 3.2, pp. 84--85. Se adapta la máquina doble a coordenadas positivas hacia abajo. El conteo por eliminación y las verificaciones de datos iniciales se explicitan localmente.
