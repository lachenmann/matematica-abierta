---
title: "Disipación y respuesta forzada"
subtitle: "Física para matemáticos · Tomo I · Capítulo 11"
author: "A. Peña"
description: "Capítulo 11 de la edición revisada, con problemas y soluciones desarrolladas."
content-id: MA-BCH-0394
source-id: FISPM-r20261021-C11
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
edition: r20261021
canonical-edition: true
date-modified: 2026-10-21
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0363"]
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

[← 10. El oscilador armónico](fisica-para-matematicos-10-el-oscilador-armonico.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [12. Momento angular y torque →](fisica-para-matematicos-12-momento-angular-y-torque.md)

Un carro unido a un resorte vuelve cada vez menos lejos después de que lo soltamos. La primera excursión hacia la derecha llega a diez centímetros del equilibrio; la siguiente, al mismo lado, apenas supera cuatro milímetros. El resorte sigue tirando hacia el equilibrio y la masa sigue siendo la misma. ¿Qué cambió respecto del oscilador del capítulo anterior? ¿Podemos reconstruir el movimiento y averiguar qué fuerza haría falta para sostenerlo?

Consideremos un carro de masa $m=1\,\mathrm{kg}$, un resorte horizontal de constante $k=5\,\mathrm{N/m}$ y un amortiguador sujeto al laboratorio. El eje $x$ apunta hacia la derecha y su cero coincide con el equilibrio del resorte. Peso y normal se compensan. Modelaremos la fuerza del amortiguador como $-b\dot x$, con $b=2\,\mathrm{kg/s}$. Suponemos válidas ambas leyes de fuerza mientras $|x|<0{,}15\,\mathrm m$ y $|\dot x|<0{,}50\,\mathrm{m/s}$. Despreciamos masa del resorte, rotación del carro y otras resistencias. Soltamos el carro desde $x(0)=0{,}10\,\mathrm m$, con velocidad inicial nula.

La segunda ley da

$$
m\ddot x+b\dot x+kx=0.
$$

El término nuevo depende de la velocidad. Su signo cambia cuando el carro cambia de sentido: siempre se opone al movimiento relativo al laboratorio. En cambio, la fuerza del resorte cambia de signo al atravesar el equilibrio. Confundir estas dos dependencias impediría incluso dibujar correctamente las fuerzas durante un ciclo.

![El resorte y el amortiguador actúan en paralelo sobre un carro; un actuador externo puede agregar una fuerza horizontal.](/assets/books/fispm/r20261021/disipacion_modelo.svg){.fpm-v04-figure}

*Figura 11.1.* El amortiguador se refiere a un soporte fijo. La fuerza aplicada se incorpora después. Las flechas indican el eje y una fuerza aplicada positiva; la fuerza viscosa debe determinarse a partir del signo de la velocidad.

## Lo que dice la energía antes de resolver la trayectoria

La energía mecánica que seguiremos es la suma de energía cinética del carro y energía potencial elástica:

$$
E(t)=\frac12m\dot x(t)^2+\frac12kx(t)^2.
$$

El amortiguador queda fuera de esta reserva de energía mecánica. La energía que recibe puede convertirse en energía interna del fluido y de sus paredes; describir ese calentamiento exigiría ampliar el sistema. Por eso una disminución de $E$ es compatible con la conservación de energía de un sistema más amplio.

Si un actuador agrega una fuerza continua $F(t)$, la ecuación y el balance son

$$
m\ddot x+b\dot x+kx=F(t),\qquad
\frac{dE}{dt}=F(t)\dot x-b\dot x^2.
$$

**Proposición.** Sean $m,k>0$, $b\geq0$ y $x$ una solución de clase $C^2$ de la ecuación anterior para $t\geq0$. Para cualesquiera $t_2\geq t_1\geq0$,

$$
E(t_2)-E(t_1)=\int_{t_1}^{t_2}F(t)\dot x(t)\,dt
-\int_{t_1}^{t_2}b\dot x(t)^2\,dt.
$$

En particular, si $F=0$, $E$ es no creciente. Dos soluciones con la misma fuerza y los mismos datos iniciales coinciden para todo $t\geq0$ donde estén definidas.

**Demostración.** La regla de la cadena permite reunir la derivada de ambas energías como $\dot E=\dot x(m\ddot x+kx)$. La ecuación de movimiento sustituye el paréntesis por $F-b\dot x$; integrar esa identidad produce el balance. Si $F=0$, el integrando disipativo es no negativo y la energía no puede aumentar. Para la unicidad, la diferencia $d$ de dos soluciones satisface la ecuación sin fuerza, con $d(0)=\dot d(0)=0$. Su energía $E_d$ parte de cero y no crece. Puesto que $E_d\geq0$, debe seguir siendo cero, lo que obliga a $d=0$ porque $k>0$.

La prueba de unicidad justifica una estrategia útil: encontrar una fórmula que satisfaga la ecuación y los dos datos basta para identificar el movimiento. La disminución de energía, por sí sola, todavía no demuestra que la posición tienda a cero; esa conclusión se verá en las soluciones explícitas.

Para el carro inicial, $E(0)=0{,}025\,\mathrm J$. Como $E(t)\leq E(0)$, tenemos $|x(t)|\leq0{,}10\,\mathrm m$ y $|\dot x(t)|\leq\sqrt{0{,}05}\,\mathrm{m/s}<0{,}224\,\mathrm{m/s}$. Ambas cotas quedan dentro del régimen declarado. Hemos comprobado la coherencia del modelo sin conocer todavía cuándo ocurren los extremos.

## Separar la caída de la oscilación

Dividir la ecuación libre por $m$ sugiere introducir

$$
\omega_0=\sqrt{k/m},\qquad \gamma=\frac{b}{2m}.
$$

Ambas constantes tienen unidades $\mathrm{s^{-1}}$; $\omega_0$ es la frecuencia angular que tendría el mismo conjunto masa–resorte sin amortiguador. El coeficiente $b$ tiene unidades de masa dividida por tiempo, no de fuerza ni de frecuencia. El factor dos en la definición de $\gamma$ simplifica la siguiente sustitución.

Busquemos $x(t)=e^{-\gamma t}y(t)$. Las dos derivadas son

$$
\dot x=e^{-\gamma t}(\dot y-\gamma y),\qquad
\ddot x=e^{-\gamma t}(\ddot y-2\gamma\dot y+\gamma^2y).
$$

Al sustituir, los términos con $\dot y$ se cancelan y queda

$$
\ddot y+(\omega_0^2-\gamma^2)y=0.
$$

La transformación es reversible, pues la exponencial nunca se anula. Si $\gamma<\omega_0$, hemos recuperado la ecuación del capítulo anterior, con una frecuencia menor. Los datos de $y$ son $y(0)=x_0$ y $\dot y(0)=v_0+\gamma x_0$: el segundo dato cambia porque hemos extraído una exponencial que también contribuye a la velocidad.

**Definición.** Para $m,k>0$ y $b>0$, el oscilador lineal libre es *subamortiguado* si $\gamma<\omega_0$, *críticamente amortiguado* si $\gamma=\omega_0$ y *sobreamortiguado* si $\gamma>\omega_0$. En el primer caso denotaremos por $\omega_d=\sqrt{\omega_0^2-\gamma^2}$ su frecuencia angular amortiguada.

**Proposición.** En el caso subamortiguado, la solución con posición $x_0$ y velocidad $v_0$ en $t=0$ es

$$
x(t)=e^{-\gamma t}\left[x_0\cos(\omega_dt)
+\frac{v_0+\gamma x_0}{\omega_d}\sin(\omega_dt)\right].
$$

**Demostración.** La expresión entre corchetes resuelve la ecuación de $y$ y toma los datos que acabamos de calcular. La sustitución reversible produce una solución de la ecuación original con los datos pedidos. La unicidad ya demostrada descarta otras soluciones con esos datos.

Para nuestro carro, $\omega_0=\sqrt5\,\mathrm{s^{-1}}$, $\gamma=1\,\mathrm{s^{-1}}$ y $\omega_d=2\,\mathrm{s^{-1}}$. Si escribimos $u=t/(1\,\mathrm s)$, una variable adimensional, obtenemos

$$
x(t)=(0{,}10\,\mathrm m)e^{-u}\left(\cos2u+\frac12\sin2u\right),\qquad
\dot x(t)=-(0{,}25\,\mathrm{m/s})e^{-u}\sin2u.
$$

La velocidad se anula cuando $u=n\pi/2$. El primer extremo negativo ocurre en $t=\pi\,\mathrm s/2$ y vale $-(0{,}10\,\mathrm m)e^{-\pi/2}$. El siguiente extremo positivo llega en $t=\pi\,\mathrm s$ y vale $(0{,}10\,\mathrm m)e^{-\pi}\approx0{,}00432\,\mathrm m$. Ya podemos explicar los cuatro milímetros del comienzo.

![Movimiento libre del carro inicial y curvas exponenciales que lo acotan.](/assets/books/fispm/r20261021/disipacion_decaimiento.svg){.fpm-v04-figure}

*Figura 11.2.* Se representa la solución con los datos del problema de apertura. Las curvas discontinuas son cotas de la posición, no trayectorias adicionales. Se señalan extremos reales del movimiento.

La misma solución puede escribirse $x=Re^{-\gamma t}\cos(\omega_dt-\alpha)$, con $R\geq0$ constante. La cantidad $Re^{-\gamma t}$ es una envolvente: acota $|x|$. Sin embargo, cuando el coseno vale uno su derivada total es $-\gamma Re^{-\gamma t}$, que no es cero si $\gamma R>0$. Por ello los máximos de posición no se obtienen simplemente haciendo uno al coseno. La pendiente de la envolvente desplaza los extremos.

Una solución libre subamortiguada satisface $x(t+T_d)=e^{-\gamma T_d}x(t)$, donde $T_d=2\pi/\omega_d$. También lo satisface su velocidad. Los estados se repiten a escala, pero no se repiten idénticos: el movimiento amortiguado no es periódico salvo en la solución de reposo. Llamar período amortiguado a $T_d$ significa aquí el intervalo entre máximos sucesivos del mismo signo.

## Regresar sin una sucesión de oscilaciones

Si $\gamma=\omega_0$, la ecuación transformada es $\ddot y=0$. Integrarla dos veces da $y=C+Dt$, y los datos fijan

$$
x(t)=e^{-\omega_0t}\left[x_0+(v_0+\omega_0x_0)t\right].
$$

El factor $t$ no puede eliminarse: sin él sólo quedaría un parámetro para imponer dos datos iniciales. Esta solución no contiene seno ni coseno. Para $x_0>0$ y $v_0=0$, su derivada es $-\omega_0^2x_0te^{-\omega_0t}$, negativa para $t>0$; la posición se acerca a cero desde el mismo lado.

En el caso sobreamortiguado, pongamos $\lambda=\sqrt{\gamma^2-\omega_0^2}$. La ecuación transformada se resuelve con exponenciales y resulta

$$
x(t)=C e^{r_+t}+D e^{r_-t},\qquad
r_\pm=-\gamma\pm\lambda.
$$

Ambas raíces son negativas porque $0<\lambda<\gamma$. Los coeficientes se encuentran resolviendo $C+D=x_0$ y $r_+C+r_-D=v_0$; el determinante es distinto de cero. La sustitución verifica estas soluciones y la unicidad vuelve a garantizar que no faltan otras. En los tres regímenes, cuando $b>0$, posición y velocidad tienden a cero.

![Comparación de tres movimientos con los mismos datos iniciales y distintos amortiguamientos.](/assets/books/fispm/r20261021/disipacion_regimenes.svg){.fpm-v04-figure}

*Figura 11.3.* Se mantienen $m=k=1$ en unidades SI, $x_0=0{,}10\,\mathrm m$ y $v_0=0$. Se comparan $b=0{,}6$, $b=2$ y $b=4\,\mathrm{kg/s}$. La afirmación de regreso sin cruce se refiere a estos datos de liberación desde el reposo.

La clasificación de la ecuación no determina todos los detalles de una trayectoria. Un sistema crítico puede atravesar el equilibrio si se lanza hacia él con suficiente rapidez; lo que no presenta es una sucesión sostenida de cruces oscilatorios. También es incorrecto concluir que aumentar $b$ siempre acelera el retorno. En el régimen muy sobreamortiguado,

$$
r_+=-\frac{\omega_0^2}{\gamma+\sqrt{\gamma^2-\omega_0^2}}
\approx-\frac{k}{b}.
$$

La igualdad proviene de racionalizar la raíz. La aproximación requiere $\gamma\gg\omega_0$ y revela un modo lento cuya escala temporal crece como $b/k$. La fuerte resistencia puede retardar el regreso. Tampoco se alcanza exactamente el reposo en un tiempo finito en estas soluciones no triviales: cualquier tiempo de asentamiento debe especificar una tolerancia.

## Medir el amortiguamiento

Dos máximos positivos consecutivos de una oscilación subamortiguada, medidos respecto del equilibrio, permiten calcular

$$
\Lambda=\log\frac{x_n}{x_{n+1}}=\gamma T_d.
$$

Se llama *decremento logarítmico* a $\Lambda$. El cociente exige extremos del mismo signo separados por un ciclo completo; con valores absolutos de extremos consecutivos, separados por medio ciclo, aparece la mitad de ese decremento. La relación es exacta para el modelo lineal, incluso si el amortiguamiento no es pequeño dentro del régimen subamortiguado.

Con $T_d$ y $\Lambda$ podemos reconstruir $\gamma=\Lambda/T_d$, $\omega_d=2\pi/T_d$ y $\omega_0=\sqrt{\omega_d^2+\gamma^2}$. Si además conocemos $m$, obtenemos $b=2m\gamma$ y $k=m\omega_0^2$. Sin una masa conocida, esos datos sólo identifican las razones $b/m$ y $k/m$.

El ajuste no constituye una comprobación independiente de las leyes de fuerza. Después de usar dos picos para determinar parámetros, debemos predecir otros picos o cambiar la preparación. Un descenso aproximadamente constante de los picos, en lugar de un cociente constante, sugeriría revisar el modelo viscoso. El rozamiento seco del capítulo 5 y una resistencia proporcional al cuadrado de la rapidez producen otras leyes de pérdida.

También debe distinguirse la envolvente de la energía instantánea. Sustituir $x=Re^{-\gamma t}\cos\theta$, $\theta=\omega_dt-\alpha$, da exactamente

$$
E(t)=\frac{mR^2}{2}e^{-2\gamma t}
\left[(\gamma\cos\theta+\omega_d\sin\theta)^2
+\omega_0^2\cos^2\theta\right].
$$

El corchete varía con el tiempo. Aunque $E$ no aumenta, no es en general igual a $E(0)e^{-2\gamma t}$. En dos instantes separados por $T_d$, sí se cumple la relación exacta $E(t+T_d)=e^{-2\gamma T_d}E(t)$. Si $\gamma/\omega_0\ll1$, reemplazar el corchete por $\omega_0^2$ introduce correcciones relativas del orden de $\gamma/\omega_0$ y permite la descripción aproximada por una exponencial de energía. No usaremos esa aproximación para localizar un extremo ni para verificar un balance instantáneo.

## Sostener el movimiento con una fuerza periódica

Agreguemos un actuador que ejerce $F(t)=F_0\cos(\Omega t)$, con $F_0>0$ y $\Omega>0$. Suponemos que su amplitud se mantiene fija al variar la frecuencia. Esta precisión será necesaria al comparar resonancias. El movimiento completo satisface

$$
m\ddot x+b\dot x+kx=F_0\cos(\Omega t).
$$

La fuerza contiene una frecuencia, pero los datos iniciales todavía pueden agregar otras componentes al movimiento. Para encontrar una respuesta que siga al actuador ensayemos $x_s=a\cos(\Omega t)+c\sin(\Omega t)$. La sustitución y la igualdad de los coeficientes del seno y del coseno dan

$$
(k-m\Omega^2)a+b\Omega c=F_0,\qquad
(k-m\Omega^2)c-b\Omega a=0.
$$

Es un sistema de dos ecuaciones lineales. Su determinante $D=(k-m\Omega^2)^2+(b\Omega)^2$ es positivo si $b>0$. Así,

$$
a=\frac{F_0(k-m\Omega^2)}{D},\qquad
c=\frac{F_0b\Omega}{D}.
$$

Podemos reunir ambos coeficientes en $x_s=A\cos(\Omega t-\delta)$, donde

$$
A=\frac{F_0}{\sqrt{(k-m\Omega^2)^2+(b\Omega)^2}},
\qquad
\cos\delta=\frac{k-m\Omega^2}{\sqrt D},\quad
\sin\delta=\frac{b\Omega}{\sqrt D}.
$$

Elegimos $0<\delta<\pi$. La fase $\delta$ representa un retraso del desplazamiento respecto de la fuerza. Los dos cocientes fijan su cuadrante, incluso cuando $k-m\Omega^2$ cambia de signo; utilizar sólo una tangente podría convertir un retraso mayor que un cuarto de ciclo en un adelanto aparente.

**Definición.** Para una fuerza $F_0\cos(\Omega t)$ con $\Omega>0$ y $b>0$, llamaremos *respuesta estacionaria* a la solución periódica $x_s$ de período $2\pi/\Omega$. Llamaremos *transitorio* a la diferencia $h=x-x_s$ entre un movimiento completo y esa respuesta.

**Proposición.** Para $m,k,b,F_0,\Omega>0$, la respuesta estacionaria es única y tiene la amplitud y la fase anteriores. Toda solución con datos iniciales finitos se escribe $x=x_s+h$, donde $h$ resuelve la ecuación libre y $h,\dot h$ tienden a cero cuando $t\to\infty$.

**Demostración.** El sistema lineal construye una solución periódica. Al restar su ecuación de la ecuación de $x$, queda $m\ddot h+b\dot h+kh=0$; las fórmulas de los tres regímenes prueban el decaimiento de $h$ y de su derivada. Si existieran dos soluciones periódicas con el período de la fuerza, su diferencia sería también periódica y tendería a cero. Evaluarla en $t+n(2\pi/\Omega)$ y hacer $n\to\infty$ muestra que vale cero en cada $t$, por lo que ambas soluciones coinciden.

La palabra estacionaria describe una forma de respuesta sostenida, no una posición inmóvil. El tiempo que debemos esperar para observarla depende del modo libre más lento y de la tolerancia del experimento. En un sistema sobreamortiguado no basta estimarlo con $1/\gamma$.

![La solución completa se descompone en un transitorio decreciente y una respuesta periódica sostenida.](/assets/books/fispm/r20261021/disipacion_transitorio.svg){.fpm-v04-figure}

*Figura 11.4.* Para $m=1\,\mathrm{kg}$, $k=5\,\mathrm{N/m}$, $b=2\,\mathrm{kg/s}$ y $F(t)=(0{,}5\,\mathrm N)\cos(2t/\mathrm s)$, se conecta la fuerza con el carro inicialmente en reposo en el equilibrio. La respuesta estacionaria no satisface por sí sola esos datos iniciales.

En ese ejemplo, $D=17\,\mathrm{(N/m)^2}$, $a=(1/34)\,\mathrm m$ y $c=(2/17)\,\mathrm m$. La amplitud es $A=(0{,}5/\sqrt{17})\,\mathrm m\approx0{,}121\,\mathrm m$ y el retraso satisface $\tan\delta=4$, en el primer cuadrante. Pero $x_s(0)=a$ y $\dot x_s(0)=2c/\mathrm s$ no son nulos. El transitorio debe empezar en $h(0)=-a$ y $\dot h(0)=-2c/\mathrm s$ para corregir ambos datos. Aplicar mecánicamente la fórmula de amplitud al instante de conexión omitiría esa preparación.

## Qué magnitud alcanza su máximo

**Definición.** Al variar $\Omega\geq0$ manteniendo fijos $m,k,b,F_0$, llamaremos *resonancia de desplazamiento* a un máximo de $A(\Omega)$ situado en una frecuencia positiva. La resonancia de velocidad y la de potencia se referirán, respectivamente, a máximos de la amplitud de velocidad $\Omega A$ y de la potencia media absorbida. En $\Omega=0$ interpretamos $A(0)=F_0/k$ como respuesta estática.

Para maximizar $A$ podemos minimizar su denominador al cuadrado. Con $z=\Omega^2\geq0$,

$$
D(z)=(k-mz)^2+b^2z
=m^2z^2+(b^2-2mk)z+k^2.
$$

**Proposición.** Con $m,k,b,F_0>0$, existe una resonancia de desplazamiento si y sólo si $\gamma<\omega_0/\sqrt2$. En ese caso su frecuencia es

$$
\Omega_r=\sqrt{\omega_0^2-2\gamma^2}.
$$

Si $\gamma\geq\omega_0/\sqrt2$, $A(\Omega)$ disminuye para $\Omega>0$ y su máximo en $[0,\infty)$ está en cero.

**Demostración.** La derivada del polinomio $D$ respecto de $z$ se anula únicamente en $z_*=k/m-b^2/(2m^2)=\omega_0^2-2\gamma^2$. Como su coeficiente cuadrático es positivo, ese punto es el mínimo cuando pertenece al interior $z>0$. Si $z_*\leq0$, $D$ es estrictamente creciente para $z>0$, incluso cuando su derivada en cero es nula. Esto prueba ambos casos.

La condición de subamortiguamiento es más amplia. Un sistema puede oscilar al soltarlo y no presentar un pico de desplazamiento al barrer frecuencias. Cuando el pico existe y $b>0$, tenemos $\Omega_r<\omega_d<\omega_0$. Para amortiguamiento muy pequeño las diferencias pueden quedar por debajo de la resolución experimental; eso explica la utilidad de una frecuencia de resonancia aproximada, pero no convierte las tres expresiones en una identidad.

![Amplitud de desplazamiento normalizada al variar la frecuencia aplicada para varios amortiguamientos.](/assets/books/fispm/r20261021/disipacion_resonancia.svg){.fpm-v04-figure}

*Figura 11.5.* Se dibuja $kA/F_0$ en función de $\Omega/\omega_0$ para valores indicados de $\zeta=\gamma/\omega_0$. Con $\zeta=0{,}8$ la respuesta libre todavía es oscilatoria, aunque ya no existe un pico de desplazamiento a frecuencia positiva.

En el límite de baja frecuencia, $A\to F_0/k$ y $\delta\to0$: el carro sigue casi el equilibrio instantáneo. Para frecuencias muy altas, $A\sim F_0/(m\Omega^2)$ y $\delta\to\pi$: la inercia domina y la posición queda casi opuesta a la fuerza. En $\Omega=\omega_0$, $\delta=\pi/2$ y $A=F_0/(b\omega_0)$. Este último punto será especial para la transferencia de energía, aunque no maximice el desplazamiento.

## Potencia, fase y ancho de la respuesta

Para una función periódica $g$ de período $T=2\pi/\Omega$, escribiremos $\langle g\rangle=T^{-1}\int_{t_0}^{t_0+T}g(t)\,dt$. El resultado no depende de $t_0$. En la respuesta estacionaria, la energía mecánica vuelve al mismo valor después de un ciclo; promediar el balance elimina $\langle\dot E\rangle$.

**Proposición.** En la respuesta estacionaria con $m,k,b,F_0,\Omega>0$,

$$
\langle P\rangle=\langle F\dot x_s\rangle
=\frac12F_0\Omega A\sin\delta
=\frac12b\Omega^2A^2.
$$

La amplitud de velocidad y la potencia media tienen su único máximo para $\Omega>0$ en $\Omega=\omega_0$. Allí $\langle P\rangle_{\max}=F_0^2/(2b)$.

**Demostración.** Derivar $x_s$ y expandir el seno de una diferencia da

$$
\dot x_s=-\Omega A\sin(\Omega t)\cos\delta
+\Omega A\cos(\Omega t)\sin\delta.
$$

El producto con $F_0\cos(\Omega t)$ tiene promedio $F_0\Omega A\sin\delta/2$, porque el producto seno–coseno promedia cero y el cuadrado del coseno promedia $1/2$. La expresión de $\sin\delta$ da el balance con la disipación. Para localizar el máximo, dividimos numerador y denominador de $\Omega^2A^2$ por $\Omega^2$:

$$
\Omega^2A^2=\frac{F_0^2}{(k/\Omega-m\Omega)^2+b^2}.
$$

El denominador alcanza su mínimo $b^2$ únicamente cuando $k/\Omega=m\Omega$, es decir, en $\Omega=\omega_0$. La potencia es un múltiplo positivo de la misma cantidad; sustituir esa frecuencia produce el valor anunciado.

En esa frecuencia, la velocidad está en fase con la fuerza y $F\dot x_s=(F_0^2/b)\cos^2(\omega_0t)\geq0$. Fuera de ella, el actuador puede recibir energía durante parte del ciclo, aunque la transferencia media siga siendo positiva. Tampoco una amplitud constante de posición implica energía mecánica instantánea constante: la fuerza aplicada y la disipación no tienen por qué compensarse en cada instante.

![Retraso de fase y potencia media normalizada de una respuesta con amortiguamiento positivo.](/assets/books/fispm/r20261021/disipacion_fase_potencia.svg){.fpm-v04-figure}

*Figura 11.6.* Para $\zeta=0{,}25$, el retraso cruza $\pi/2$ en $\Omega/\omega_0=1$, donde la potencia media es máxima. Las dos gráficas comparten el eje de frecuencia y tienen escalas verticales diferentes.

Se define el factor de calidad por $Q=m\omega_0/b=\omega_0/(2\gamma)$. Es adimensional. Para expresar su relación con un ancho de respuesta, usemos los dos puntos donde la potencia media es la mitad de su máximo. La fórmula anterior exige $(k/\Omega-m\Omega)^2=b^2$ y da

$$
\Omega_- =\frac{\sqrt{b^2+4mk}-b}{2m},\qquad
\Omega_+ =\frac{\sqrt{b^2+4mk}+b}{2m}.
$$

Por tanto $\Omega_+-\Omega_-=b/m$ y $Q=\omega_0/(\Omega_+-\Omega_-)$. Es una identidad exacta para la potencia media de este modelo con amplitud de fuerza fija. No hemos demostrado una identidad semejante para el ancho a media altura de la curva de desplazamiento. Para $Q$ grande, los dos puntos de media potencia están cerca de $\omega_0$ y el pico es estrecho en relación con esa frecuencia.

## Qué cambia cuando se elimina la disipación

Si $b=0$, una respuesta particular para $\Omega\ne\omega_0$ es

$$
x_p(t)=\frac{F_0}{m(\omega_0^2-\Omega^2)}\cos(\Omega t).
$$

Pero la parte libre ya no decae. Con datos iniciales nulos, el movimiento completo es

$$
x(t)=\frac{F_0}{m(\omega_0^2-\Omega^2)}
\left[\cos(\Omega t)-\cos(\omega_0t)\right].
$$

Tiene dos frecuencias que persisten. En consecuencia, no podemos hablar de una respuesta atractora independiente de la preparación. Si $\Omega$ está cerca de $\omega_0$, la identidad de diferencia de cosenos muestra batimientos: una oscilación rápida modulada por una escala lenta relacionada con $|\Omega-\omega_0|$.

Cuando $\Omega=\omega_0$, el ensayo de un coseno falla porque coincide con una solución libre. Un ensayo con un factor temporal permite satisfacer la ecuación y los datos nulos:

$$
x(t)=\frac{F_0}{2m\omega_0}\,t\sin(\omega_0t).
$$

Derivar dos veces deja $\ddot x+\omega_0^2x=(F_0/m)\cos(\omega_0t)$ y en cero se anulan posición y velocidad. La envolvente crece linealmente. No hay una amplitud infinita en un instante finito: hay crecimiento sin cota cuando el tiempo crece dentro de un modelo ideal. En un aparato real, antes pueden fallar la linealidad del resorte, el control del actuador o la omisión de disipación.

![Respuesta resonante sin amortiguamiento, conectada desde datos iniciales nulos.](/assets/books/fispm/r20261021/disipacion_resonancia_ideal.svg){.fpm-v04-figure}

*Figura 11.7.* Ejemplo con $m=1\,\mathrm{kg}$, $\omega_0=2\,\mathrm{s^{-1}}$ y $F_0=0{,}2\,\mathrm N$. Las líneas discontinuas son las envolventes $\pm(0{,}05\,\mathrm{m/s})t$. El crecimiento debe contrastarse con el intervalo de validez de las leyes de fuerza.

Para $b>0$, incluso muy pequeño, la respuesta estacionaria en $\omega_0$ es finita, pero el tiempo necesario para aproximarse a ella aumenta al reducir $b$ en el régimen subamortiguado. Tomar primero un tiempo muy largo y después hacer pequeño el amortiguamiento describe una pregunta diferente de conectar una fuerza a un oscilador sin disipación y observarlo durante un tiempo fijo. La distinción entre preparación, transitorio y respuesta sostenida evita atribuir al experimento un límite que todavía no ha alcanzado.

## Ejercicios

Los datos numéricos se refieren a modelos lineales en el marco del laboratorio. Cuando se indica una respuesta estacionaria, se supone que el transitorio ha decaído por debajo de la tolerancia relevante. Las unidades SI acompañan a los parámetros aunque una ecuación auxiliar use la variable adimensional $u=t/(1\,\mathrm s)$.

### 1. Dos fuerzas que cambian de signo por razones distintas {#ejercicio-11-1}

Un carro tiene $m=2\,\mathrm{kg}$, $k=18\,\mathrm{N/m}$ y $b=4\,\mathrm{kg/s}$. En un instante está en $x=0{,}050\,\mathrm m$ con $\dot x=-0{,}20\,\mathrm{m/s}$, sin fuerza aplicada. Determine ambas fuerzas, la aceleración y la potencia disipada. Decida si el carro está aumentando su rapidez.

### 2. Clasificar antes de calcular {#ejercicio-11-2}

Para $m=1\,\mathrm{kg}$ y $k=9\,\mathrm{N/m}$ se dispone de amortiguadores con $b=2$, $6$ y $10\,\mathrm{kg/s}$. Clasifique los tres casos y determine las frecuencias o tasas exponenciales pertinentes. Explique qué ocurre si se introduce una frecuencia imaginaria en una fórmula trigonométrica sin reinterpretarla.

### 3. Lanzamiento de un oscilador subamortiguado {#ejercicio-11-3}

Con $m=1\,\mathrm{kg}$, $k=5\,\mathrm{N/m}$ y $b=2\,\mathrm{kg/s}$, prepare $x_0=0$ y $v_0=0{,}20\,\mathrm{m/s}$. Encuentre $x(t)$, el primer extremo positivo y el primer retorno al equilibrio.

### 4. Un tiempo de asentamiento garantizado {#ejercicio-11-4}

Para el carro del problema de apertura, encuentre un tiempo a partir del cual $|x(t)|<1\,\mathrm{mm}$ quede garantizado por la envolvente. Distinga esa garantía del primer instante en que el carro entra en la franja.

### 5. Reconstruir parámetros desde picos {#ejercicio-11-5}

Un carro de masa $0{,}50\,\mathrm{kg}$ presenta dos máximos positivos consecutivos de $40\,\mathrm{mm}$ y $20\,\mathrm{mm}$, separados por $2{,}0\,\mathrm s$. Bajo el modelo viscoso, calcule $\gamma$, $\omega_d$, $b$ y $k$. Prediga el tercer máximo positivo y declare qué parte del procedimiento constituye una prueba nueva del ajuste.

### 6. La energía no sigue exactamente la envolvente {#ejercicio-11-6}

Alguien propone $E(t)=E(0)e^{-2\gamma t}$ como identidad exacta para cualquier oscilación libre subamortiguada. Refútela usando una liberación desde el reposo fuera del equilibrio. Encuentre una relación exponencial de energía que sí sea exacta.

### 7. Liberación crítica {#ejercicio-11-7}

Un sistema tiene $m=1\,\mathrm{kg}$, $k=4\,\mathrm{N/m}$ y $b=4\,\mathrm{kg/s}$. Se libera desde $x_0=0{,}10\,\mathrm m$ y $v_0=0$. Encuentre la trayectoria, demuestre que no cruza el equilibrio y estime cuándo queda por debajo de $1\,\mathrm{mm}$.

### 8. Un cruce en el régimen crítico {#ejercicio-11-8}

En el mismo sistema crítico, cambie la velocidad inicial a $v_0=-0{,}50\,\mathrm{m/s}$. Determine cuándo cruza el equilibrio y explique por qué ese cruce no contradice la clasificación del régimen.

### 9. La resistencia que retrasa el regreso {#ejercicio-11-9}

Para $m=1\,\mathrm{kg}$, $k=3\,\mathrm{N/m}$ y $b=4\,\mathrm{kg/s}$, libere el carro desde $x_0=0{,}10\,\mathrm m$ con velocidad nula. Calcule las dos componentes exponenciales y la tasa que gobierna el final del retorno. Compare la expresión exacta de la raíz lenta con $-k/b$ y evalúe si la aproximación es buena.

### 10. Una cota sin resolver la ecuación {#ejercicio-11-10}

Un oscilador libre con $m=2\,\mathrm{kg}$, $k=8\,\mathrm{N/m}$ y $b>0$ parte de $x_0=0{,}10\,\mathrm m$ y $v_0=0{,}30\,\mathrm{m/s}$. Su modelo exige $|x|<0{,}20\,\mathrm m$ y $|\dot x|<0{,}50\,\mathrm{m/s}$. Compruebe su coherencia para todo $t\geq0$ sin calcular la trayectoria.

### 11. Resolver también el cuadrante {#ejercicio-11-11}

Para $m=1\,\mathrm{kg}$, $k=4\,\mathrm{N/m}$, $b=2\,\mathrm{kg/s}$ y $F(t)=(1\,\mathrm N)\cos(3t/\mathrm s)$, calcule la respuesta estacionaria mediante coeficientes reales. Determine su amplitud y el cuadrante del retraso.

### 12. Conectar desde el reposo {#ejercicio-11-12}

Obtenga la solución completa del ejemplo de la figura 11.4, con $x(0)=\dot x(0)=0$. Verifique los dos datos y señale una cota explícita para el error que se cometería al utilizar sólo la respuesta estacionaria.

### 13. Tres frecuencias de un mismo aparato {#ejercicio-11-13}

Un aparato tiene $m=1\,\mathrm{kg}$, $k=10\,\mathrm{N/m}$ y $b=2\,\mathrm{kg/s}$. Calcule $\omega_0$, $\omega_d$ y $\Omega_r$. Determine en cuál de ellas se maximiza la potencia media cuando $F_0$ se mantiene fijo.

### 14. Oscilar sin pico de desplazamiento {#ejercicio-11-14}

Construya un ejemplo con $m=k=1$ en unidades SI que sea subamortiguado y, sin embargo, carezca de resonancia de desplazamiento a frecuencia positiva. Demuestre las dos afirmaciones y decida si conserva una resonancia de potencia.

### 15. Dimensionar un actuador {#ejercicio-11-15}

Se desea sostener una amplitud de $0{,}020\,\mathrm m$ en un sistema con $m=2\,\mathrm{kg}$, $k=18\,\mathrm{N/m}$ y $b=3\,\mathrm{kg/s}$, excitado a $\Omega=3\,\mathrm{s^{-1}}$. Determine la amplitud de fuerza, su fase respecto de la velocidad y la potencia media que debe suministrar.

### 16. Una fuerza que recibe energía durante parte del ciclo {#ejercicio-11-16}

Para una respuesta con $\delta=\pi/4$, determine el signo de la potencia aplicada en los instantes de fase $\theta=\Omega t=0$ y $\theta=3\pi/8$. Compare ese signo con el de la potencia media. No confunda potencia aplicada con potencia disipada.

### 17. Ancho de media potencia y calidad {#ejercicio-11-17}

Un sistema tiene $m=1\,\mathrm{kg}$, $k=16\,\mathrm{N/m}$ y $b=2\,\mathrm{kg/s}$. Calcule $Q$, los dos puntos de media potencia y su separación. ¿Están situados exactamente a igual distancia de $\omega_0$?

### 18. Reconstruir el amortiguamiento mediante una fase {#ejercicio-11-18}

Se conocen $m=1\,\mathrm{kg}$ y $k=9\,\mathrm{N/m}$. A $\Omega=2\,\mathrm{s^{-1}}$ se mide un retraso estacionario $\delta=\pi/4$. Deduzca $b$. Explique por qué medir sólo $\delta=\pi/2$ a $\Omega=\omega_0$ no permitiría identificarlo.

### 19. Resonancia ideal durante un tiempo finito {#ejercicio-11-19}

Un carro ideal sin disipación tiene $m=1\,\mathrm{kg}$, $k=4\,\mathrm{N/m}$ y datos iniciales nulos. Se conecta $F(t)=(0{,}20\,\mathrm N)\cos(2t/\mathrm s)$. Calcule $x(t)$ y $E(t)$ en $t=\pi\,\mathrm s$. Si la ley del resorte exige $|x|<0{,}20\,\mathrm m$, dé un intervalo temporal que garantice esa condición y explique qué no puede inferirse fuera de él.

### 20. Un dato que no confirma su propio ajuste {#ejercicio-11-20}

En un primer ensayo libre, tres máximos positivos consecutivos separados por iguales intervalos valen $50$, $40$ y $30\,\mathrm{mm}$. En un segundo ensayo del mismo aparato valen $30$, $20$ y $10\,\mathrm{mm}$. Cada pico queda acotado por un intervalo determinista de semiancho $0{,}2\,\mathrm{mm}$ alrededor del valor indicado. Suponga parámetros físicos constantes. Examine el modelo viscoso ajustándolo con los dos primeros picos del primer ensayo; compare con las otras observaciones y proponga un modelo rival que merezca investigarse.

## Soluciones

### 1. Dos fuerzas que cambian de signo por razones distintas {#solucion-11-1}

El resorte ejerce $-kx=-0{,}90\,\mathrm N$, hacia la izquierda. El amortiguador ejerce $-b\dot x=+0{,}80\,\mathrm N$, hacia la derecha, porque el carro se mueve hacia la izquierda. La fuerza neta es $-0{,}10\,\mathrm N$ y la aceleración es $-0{,}050\,\mathrm{m/s^2}$. Velocidad y aceleración tienen el mismo signo; por tanto la rapidez está aumentando en ese instante.

La potencia que recibe el amortiguador es $b\dot x^2=0{,}16\,\mathrm W$, positiva. La potencia de su fuerza sobre el carro es su negativo. No hay contradicción con el aumento de rapidez: la energía potencial elástica disminuye y puede alimentar simultáneamente energía cinética y disipación. El signo de la aceleración se obtiene sumando fuerzas, mientras que el signo de la pérdida mecánica depende del producto fuerza–velocidad.

### 2. Clasificar antes de calcular {#solucion-11-2}

La frecuencia natural es $\omega_0=3\,\mathrm{s^{-1}}$ y el umbral crítico es $b_c=2\sqrt{mk}=6\,\mathrm{kg/s}$. Con $b=2$, $\gamma=1\,\mathrm{s^{-1}}<\omega_0$ y $\omega_d=\sqrt8\,\mathrm{s^{-1}}$. Con $b=6$, la raíz es doble y las soluciones son $e^{-3u}(C+D u)$, con $u=t/(1\,\mathrm s)$ y ambos coeficientes expresados en longitud.

Con $b=10$, $\gamma=5\,\mathrm{s^{-1}}$ y $\lambda=4\,\mathrm{s^{-1}}$, de modo que $r_+=-1\,\mathrm{s^{-1}}$ y $r_-=-9\,\mathrm{s^{-1}}$. La solución es una combinación de $e^{-u}$ y $e^{-9u}$. La raíz de $\omega_0^2-\gamma^2$ ya no define una frecuencia angular real; reemplazarla formalmente por una raíz imaginaria exige transformar senos y cosenos en funciones hiperbólicas o exponenciales. No describe una oscilación de frecuencia imaginaria observable. La ecuación transformada permite cambiar de régimen sin esa ambigüedad.

### 3. Lanzamiento de un oscilador subamortiguado {#solucion-11-3}

Aquí $\gamma=1\,\mathrm{s^{-1}}$ y $\omega_d=2\,\mathrm{s^{-1}}$. Como $x_0=0$, la solución se reduce a

$$
x(t)=(0{,}10\,\mathrm m)e^{-u}\sin2u,\qquad
\dot x(t)=(0{,}10\,\mathrm{m/s})e^{-u}(2\cos2u-\sin2u).
$$

El primer extremo positivo satisface $\tan2u=2$ en el primer cuadrante: $u_*=\tfrac12\arctan2\approx0{,}5536$. Su posición es $(0{,}10\,\mathrm m)e^{-u_*}(2/\sqrt5)\approx0{,}0514\,\mathrm m$. En ese extremo la aceleración es $-kx/m<0$, lo que confirma que es un máximo. El primer retorno a cero sucede cuando $2u=\pi$, es decir, $t=\pi\,\mathrm s/2$. El máximo llega antes que la cuarta parte de $T_d$: derivar la exponencial altera el instante que se obtendría mirando sólo el seno.

### 4. Un tiempo de asentamiento garantizado {#solucion-11-4}

La combinación $\cos2u+\tfrac12\sin2u$ tiene amplitud $\sqrt5/2$. Por tanto

$$
|x(t)|\leq(0{,}05\sqrt5\,\mathrm m)e^{-u}.
$$

Para que la cota sea menor que $0{,}001\,\mathrm m$ basta exigir $u>\log(50\sqrt5)\approx4{,}717$. Así, cualquier tiempo posterior a $4{,}72\,\mathrm s$ queda garantizado por esta estimación. La cota disminuye monótonamente, lo que permite afirmar que el carro permanecerá en la franja.

El primer ingreso puede suceder mucho antes, cerca del primer cruce por cero, y ser seguido por una salida. No es el tiempo solicitado. La estimación por envolvente es suficiente y puede ser conservadora; hallar el último cruce exacto de la frontera de la franja exigiría resolver una ecuación trascendente y comprobar las excursiones posteriores.

### 5. Reconstruir parámetros desde picos {#solucion-11-5}

Los picos son del mismo signo, por lo que $T_d=2{,}0\,\mathrm s$ y $\Lambda=\log2$. Resultan

$$
\gamma=\frac{\log2}{2}\,\mathrm{s^{-1}}\approx0{,}3466\,\mathrm{s^{-1}},\qquad
\omega_d=\pi\,\mathrm{s^{-1}}.
$$

Con la masa conocida, $b=2m\gamma\approx0{,}3466\,\mathrm{kg/s}$ y

$$
k=m(\omega_d^2+\gamma^2)\approx4{,}995\,\mathrm{N/m}.
$$

La frecuencia natural es aproximadamente $3{,}161\,\mathrm{s^{-1}}$. El tercer máximo positivo se predice en $10\,\mathrm{mm}$, otros dos segundos después del segundo. Los primeros dos picos se utilizaron para ajustar; reproducirlos no prueba el modelo. Medir el tercer pico, comparar su tiempo y repetir con otra amplitud sí aporta observaciones no utilizadas en ese ajuste. Las cifras calculadas no representan por sí solas una incertidumbre experimental: haría falta conocer la resolución y los errores de posición, tiempo y masa.

### 6. La energía no sigue exactamente la envolvente {#solucion-11-6}

Al soltar desde el reposo con $x_0\ne0$ y $b>0$, el balance exacto da $\dot E(0)=-b v_0^2=0$. La fórmula propuesta daría $\dot E(0)=-2\gamma E(0)<0$. Las derivadas iniciales son incompatibles y bastan para refutar la identidad.

En el caso subamortiguado, tanto $x$ como $\dot x$ se multiplican por $e^{-\gamma T_d}$ al desplazar el tiempo en un ciclo $T_d$. Como cada término de $E$ es cuadrático, sí se cumple

$$
E(t+T_d)=e^{-2\gamma T_d}E(t).
$$

Para $n$ ciclos, el factor es $e^{-2n\gamma T_d}$. Esta afirmación compara estados con la misma fase; no reemplaza la evolución continua entre ellos por una exponencial exacta. En particular, la derivada de energía se anula en cada punto de retorno, aunque la pérdida total entre dos retornos sea positiva.

### 7. Liberación crítica {#solucion-11-7}

Tenemos $\gamma=\omega_0=2\,\mathrm{s^{-1}}$. Los datos producen

$$
x(t)=(0{,}10\,\mathrm m)(1+2u)e^{-2u},\qquad
\dot x(t)=-(0{,}40\,\mathrm{m/s})u e^{-2u}.
$$

Para $u\geq0$, la posición es positiva y su derivada es negativa salvo en el instante inicial. Se aproxima al equilibrio desde la derecha y nunca lo cruza. Para localizar la tolerancia resolvemos $(1+2u)e^{-2u}=0{,}01$. La función del lado izquierdo es estrictamente decreciente para $u>0$; no hay raíces posteriores que puedan devolver el movimiento fuera de la franja.

En $u=3{,}3$ el producto vale aproximadamente $0{,}01034$ y en $u=3{,}4$ vale $0{,}00869$. Una interpolación o bisección afina el cruce a $u\approx3{,}319$. Por tanto, después de unos $3{,}32\,\mathrm s$ queda por debajo del milímetro. El equilibrio exacto sólo se alcanza en el límite temporal.

### 8. Un cruce en el régimen crítico {#solucion-11-8}

El coeficiente lineal es $v_0+\omega_0x_0=-0{,}30\,\mathrm{m/s}$. Por eso

$$
x(t)=(0{,}10\,\mathrm m-0{,}30\,\mathrm{m/s}\,t)e^{-2t/\mathrm s}.
$$

La exponencial es positiva y el cambio de signo ocurre cuando el paréntesis se anula: $t=(1/3)\,\mathrm s$. La velocidad allí es $-(0{,}30\,\mathrm{m/s})e^{-2/3}\ne0$, de modo que existe un cruce real. Después la posición permanece negativa y tiende a cero.

El amortiguamiento crítico caracteriza las raíces de la ecuación y la ausencia de una secuencia oscilatoria, no prohíbe cualquier cruce para cualquier preparación. La afirmación de retorno sin sobrepasar el equilibrio que usamos en la liberación crítica exigía $v_0=0$ y $x_0>0$. El nuevo dato inicial queda fuera de esa afirmación y proporciona un contraejemplo a su generalización indiscriminada.

### 9. La resistencia que retrasa el regreso {#solucion-11-9}

Ahora $\gamma=2\,\mathrm{s^{-1}}$, $\omega_0=\sqrt3\,\mathrm{s^{-1}}$ y $\lambda=1\,\mathrm{s^{-1}}$. Las raíces son $-1$ y $-3\,\mathrm{s^{-1}}$. Resolver $C+D=0{,}10\,\mathrm m$ y $-C-3D=0$ da $C=0{,}15\,\mathrm m$, $D=-0{,}05\,\mathrm m$. Así,

$$
x(t)=(0{,}15\,\mathrm m)e^{-u}-(0{,}05\,\mathrm m)e^{-3u}.
$$

El segundo término desaparece más deprisa y el final del retorno está gobernado por $e^{-u}$, cuya escala temporal es un segundo. La aproximación $-k/b$ predice $-0{,}75\,\mathrm{s^{-1}}$, frente al valor exacto $-1\,\mathrm{s^{-1}}$: un error relativo del $25\%$ respecto de la tasa exacta. Aquí $\omega_0/\gamma\approx0{,}866$ no es pequeño; la condición de sobreamortiguamiento se cumple, pero la condición mucho más exigente de fuerte sobreamortiguamiento no. Una clasificación cualitativa no autoriza automáticamente una aproximación asintótica.

### 10. Una cota sin resolver la ecuación {#solucion-11-10}

La energía inicial es

$$
E(0)=\tfrac12(2)(0{,}30)^2+\tfrac12(8)(0{,}10)^2
=0{,}13\,\mathrm J.
$$

Al no existir fuerza aplicada, el balance impone $E(t)\leq0{,}13\,\mathrm J$. Cada término positivo de la energía es menor o igual que esa cantidad. Se sigue que

$$
|x(t)|\leq\sqrt{\frac{2(0{,}13\,\mathrm J)}{8\,\mathrm{N/m}}}
\approx0{,}1803\,\mathrm m,
\quad
|\dot x(t)|\leq\sqrt{\frac{2(0{,}13\,\mathrm J)}{2\,\mathrm{kg}}}
\approx0{,}3606\,\mathrm{m/s}.
$$

Ambas cotas son estrictamente menores que los límites declarados. No necesitamos conocer $b$ para esta conclusión, sólo su signo no negativo. Las dos cotas no afirman que posición y rapidez alcancen simultáneamente esos valores: provienen de asignar por separado toda la energía disponible a cada término. Una cota suficiente puede ser útil aun cuando no sea alcanzable.

### 11. Resolver también el cuadrante {#solucion-11-11}

Tenemos $k-m\Omega^2=-5\,\mathrm{N/m}$, $b\Omega=6\,\mathrm{N/m}$ y $D=61\,\mathrm{(N/m)^2}$. Por tanto

$$
x_s(t)=-(5/61\,\mathrm m)\cos(3u)
+(6/61\,\mathrm m)\sin(3u).
$$

Su amplitud es $A=(1/\sqrt{61})\,\mathrm m\approx0{,}1280\,\mathrm m$. La fase cumple $\cos\delta=-5/\sqrt{61}$ y $\sin\delta=6/\sqrt{61}$; está en el segundo cuadrante y vale $\pi-\arctan(6/5)\approx2{,}266\,\mathrm{rad}$. La respuesta se retrasa más de un cuarto de ciclo respecto de la fuerza. Tomar el valor principal de $\arctan(-6/5)$ daría un ángulo negativo y no reproduciría los signos de ambos coeficientes con amplitud positiva. La comprobación por seno y coseno evita ese error.

### 12. Conectar desde el reposo {#solucion-11-12}

Escribamos $u=t/(1\,\mathrm s)$. La respuesta estacionaria es $x_s=[\cos2u+4\sin2u](1/34\,\mathrm m)$. Para anular sus datos iniciales, el transitorio subamortiguado debe tener $h(0)=-1/34\,\mathrm m$ y $\dot h(0)=-4/17\,\mathrm{m/s}$. Su coeficiente del seno resulta $-9/68\,\mathrm m$. La solución completa es

$$
\begin{aligned}
x(t)={}&(1/34\,\mathrm m)\cos2u+(2/17\,\mathrm m)\sin2u\\
&-e^{-u}\left[(1/34\,\mathrm m)\cos2u
+(9/68\,\mathrm m)\sin2u\right].
\end{aligned}
$$

En cero, las posiciones se cancelan. Derivar el transitorio da $\dot h(0)=-(4/17)\,\mathrm{m/s}$, que cancela la velocidad estacionaria. Ambas partes satisfacen sus ecuaciones, por lo que la suma es la solución pedida.

El error de posición por omitir $h$ está acotado por $(\sqrt{85}/68\,\mathrm m)e^{-u}\approx(0{,}1356\,\mathrm m)e^{-u}$. Después de $4{,}91\,\mathrm s$ queda por debajo de un milímetro. Para comprobar el régimen durante la conexión, acotaremos también la suma completa.

Pongamos $r=e^{-u}$, con $0<r\leq1$. Reunir los coeficientes de seno y coseno antes de tomar módulos conserva la compensación entre la respuesta estacionaria y el transitorio:

$$
\begin{aligned}
x(t)&=\frac{\mathrm m}{68}\big[2(1-r)\cos2u+(8-9r)\sin2u\big],\\
\dot x(t)&=\frac{\mathrm{m/s}}{68}\big[16(1-r)\cos2u+(13r-4)\sin2u\big].
\end{aligned}
$$

Para cualesquiera coeficientes $a,c$, la desigualdad de Cauchy–Schwarz da $|a\cos2u+c\sin2u|\leq\sqrt{a^2+c^2}$. Los cuadrados de las cotas que aparecen aquí son polinomios convexos de $r$. En $0\leq r\leq1$, cada valor de un polinomio convexo queda por debajo o al nivel del mayor de sus valores extremos. En este caso basta comprobarlo para un polinomio cuadrático $p(r)=ar^2+cr+d$, con $a>0$: la diferencia entre $(1-r)p(0)+rp(1)$ y $p(r)$ es $ar(1-r)\geq0$. Para la posición, esos valores son $68$ y $1$; para la velocidad, $272$ y $81$. En consecuencia,

$$
|x(t)|\leq\frac{1}{\sqrt{68}}\,\mathrm m<0{,}122\,\mathrm m,
\qquad
|\dot x(t)|\leq\frac{1}{\sqrt{17}}\,\mathrm{m/s}<0{,}243\,\mathrm{m/s}.
$$

Las cotas mantienen la posición por debajo de $0{,}15\,\mathrm m$ y la rapidez por debajo de $0{,}50\,\mathrm{m/s}$ durante toda la conexión y la evolución posterior. Por tanto, el movimiento completo permanece dentro del régimen declarado para el resorte y el amortiguador. Acotar por separado ambas partes habría perdido una cancelación útil; reunir primero sus coeficientes permitió cerrar la comprobación.

### 13. Tres frecuencias de un mismo aparato {#solucion-11-13}

Se obtiene $\gamma=1\,\mathrm{s^{-1}}$, $\omega_0=\sqrt{10}\,\mathrm{s^{-1}}\approx3{,}162\,\mathrm{s^{-1}}$ y $\omega_d=3\,\mathrm{s^{-1}}$. La condición para un pico de desplazamiento es $\omega_0^2>2\gamma^2$ y aquí se cumple. Su frecuencia es $\Omega_r=\sqrt8\,\mathrm{s^{-1}}\approx2{,}828\,\mathrm{s^{-1}}$.

Al variar la frecuencia de una fuerza de amplitud fija, el desplazamiento es máximo en $\Omega_r$. La potencia media y la amplitud de velocidad lo son en $\omega_0$. La frecuencia $\omega_d$ se mide en el movimiento libre, por ejemplo mediante el intervalo entre dos máximos positivos después de apagar el actuador. Son tres experimentos o criterios diferentes sobre el mismo aparato. La diferencia entre $\omega_d$ y $\Omega_r$ no es una corrección de unidades: ambas son frecuencias angulares reales y corresponden a preguntas físicas distintas.

### 14. Oscilar sin pico de desplazamiento {#solucion-11-14}

Elijamos $b=1{,}6\,\mathrm{kg/s}$. Entonces $\omega_0=1\,\mathrm{s^{-1}}$ y $\gamma=0{,}8\,\mathrm{s^{-1}}$. Como $\gamma<\omega_0$, la respuesta libre no trivial es subamortiguada, con $\omega_d=0{,}6\,\mathrm{s^{-1}}$. Sin embargo, $\omega_0^2-2\gamma^2=-0{,}28\,\mathrm{s^{-2}}<0$.

La amplitud estacionaria disminuye para toda frecuencia positiva y alcanza su máximo estático en cero. No existe $\Omega_r$ real y positivo. La potencia media sí tiene su máximo en $\Omega=1\,\mathrm{s^{-1}}$, porque el denominador de $\Omega^2A^2$ se minimiza allí para cualquier $b>0$. En cero la potencia media tiende a cero: una deformación estática no exige movimiento viscoso sostenido. El ejemplo separa la existencia de oscilaciones libres, de un pico de desplazamiento y de un pico de potencia.

### 15. Dimensionar un actuador {#solucion-11-15}

La frecuencia aplicada coincide con $\omega_0=\sqrt{k/m}=3\,\mathrm{s^{-1}}$. Por eso $k-m\Omega^2=0$ y $A=F_0/(b\Omega)$. Para la amplitud pedida necesitamos $F_0=b\Omega A=0{,}18\,\mathrm N$.

El retraso del desplazamiento es $\delta=\pi/2$, de modo que $x_s=A\sin(\Omega t)$ y $\dot x_s=\Omega A\cos(\Omega t)$. La velocidad está en fase con la fuerza y tiene amplitud $0{,}060\,\mathrm{m/s}$. La potencia media es

$$
\langle P\rangle=\tfrac12b(\Omega A)^2
=0{,}0054\,\mathrm W.
$$

La potencia máxima instantánea es el doble de ese promedio. Estos valores sostienen el régimen estacionario; no especifican la fuerza o energía adicional que podría requerir otra preparación del movimiento, ni las pérdidas internas del propio actuador. La comprobación dimensional $b\Omega A\sim(\mathrm{kg/s})(\mathrm{s^{-1}})\mathrm m=\mathrm N$ confirma que la amplitud de fuerza se calculó con unidades coherentes.

### 16. Una fuerza que recibe energía durante parte del ciclo {#solucion-11-16}

La potencia aplicada es $P=F_0\cos\theta[-\Omega A\sin(\theta-\delta)]$. Con $\delta=\pi/4$ y $\theta=0$, ambos factores son positivos y $P=F_0\Omega A/\sqrt2>0$. En $\theta=3\pi/8$, la fuerza sigue siendo positiva, pero $\theta-\delta=\pi/8$ y la velocidad es negativa. Por tanto $P<0$: el carro entrega energía al actuador en ese instante.

El promedio sigue siendo $F_0\Omega A/(2\sqrt2)>0$. La potencia disipada, $b\dot x_s^2$, es no negativa en todo momento y no cambia de signo cuando lo hace $P$. El balance instantáneo es $\dot E=P-b\dot x_s^2$; el promedio estacionario exige igualdad de las transferencias acumuladas en un ciclo. El signo medio no permite reemplazar ese balance por una igualdad instantánea entre fuerza aplicada y fuerza viscosa.

### 17. Ancho de media potencia y calidad {#solucion-11-17}

La frecuencia natural es $4\,\mathrm{s^{-1}}$ y $Q=m\omega_0/b=2$. La fórmula exacta proporciona

$$
\Omega_-=(\sqrt{17}-1)\,\mathrm{s^{-1}}\approx3{,}123\,\mathrm{s^{-1}},\qquad
\Omega_+=(\sqrt{17}+1)\,\mathrm{s^{-1}}\approx5{,}123\,\mathrm{s^{-1}}.
$$

La separación es $2\,\mathrm{s^{-1}}=b/m$. El cociente de $\omega_0$ por esa separación da $Q=2$. No son simétricos respecto de $4\,\mathrm{s^{-1}}$: su media aritmética es $\sqrt{17}\,\mathrm{s^{-1}}$, mayor que la frecuencia natural. En cambio, el producto es $\Omega_-\Omega_+=\omega_0^2$, así que su media geométrica coincide con $\omega_0$. Aproximarlos por $\omega_0\pm b/(2m)$ requiere un pico estrecho, es decir, $b/(m\omega_0)\ll1$. Aquí esa razón es $1/2$, y la asimetría exacta no debe ocultarse tras la aproximación.

### 18. Reconstruir el amortiguamiento mediante una fase {#solucion-11-18}

En la frecuencia medida, $k-m\Omega^2=5\,\mathrm{N/m}>0$. La fase del primer cuadrante satisface $\tan\delta=b\Omega/(k-m\Omega^2)=1$, por lo que

$$
b=\frac{k-m\Omega^2}{\Omega}=2{,}5\,\mathrm{kg/s}.
$$

El signo es positivo y coherente con disipación. Este cálculo usa una fase estacionaria; una fase medida durante el transitorio no puede sustituirse sin más en la misma relación. También sería necesario conocer la precisión temporal con que se compara fuerza y desplazamiento para asignar incertidumbre al resultado.

En $\Omega=\omega_0$, el coseno de la fase vale cero y el seno es positivo para cualquier $b>0$: siempre obtenemos $\delta=\pi/2$. Esa observación localiza la frecuencia natural bajo el modelo, pero no distingue valores de $b$. Para identificarlo allí se podría medir además la amplitud con $F_0$ conocido y utilizar $b=F_0/(\omega_0 A)$.

### 19. Resonancia ideal durante un tiempo finito {#solucion-11-19}

Tenemos $\omega_0=2\,\mathrm{s^{-1}}$. La solución resonante con datos nulos es $x(t)=(0{,}05\,\mathrm{m/s})t\sin(2t/\mathrm s)$. En $t=\pi\,\mathrm s$, la posición es cero y la velocidad vale $0{,}10\pi\,\mathrm{m/s}$. Toda la energía mecánica en ese instante es cinética:

$$
E(\pi\,\mathrm s)=0{,}005\pi^2\,\mathrm J\approx0{,}04935\,\mathrm J.
$$

La envolvente impone $|x(t)|\leq(0{,}05\,\mathrm{m/s})t$. Por tanto, $0\leq t<4\,\mathrm s$ garantiza $|x|<0{,}20\,\mathrm m$. Es un intervalo suficiente. Fuera de él, la cota deja de garantizar la condición; eso no significa que la trayectoria viole el límite en todos esos instantes. Para extender la descripción hay que comprobar el desplazamiento real y las demás hipótesis. El crecimiento secular tampoco prueba que un resorte real pueda acumular energía ilimitada manteniendo su ley lineal.

### 20. Un dato que no confirma su propio ajuste {#solucion-11-20}

Los dos primeros picos del primer ensayo fijan un factor viscoso de $40/50=0{,}8$ por ciclo. El modelo predice entonces un tercer pico de $32\,\mathrm{mm}$, frente a los $30\,\mathrm{mm}$ observados. Las cotas declaradas permiten propagar los dos picos usados en el ajuste. Como $p_2^2/p_1$ crece con $p_2>0$ y decrece con $p_1>0$, la predicción pertenece a

$$
\left[\frac{(39{,}8)^2}{50{,}2};\frac{(40{,}2)^2}{49{,}8}\right]\,\mathrm{mm}
\subset[31{,}55;32{,}46]\,\mathrm{mm}.
$$

La envolvente decimal se redondeó hacia fuera y queda separada del intervalo observado $[29{,}8;30{,}2]\,\mathrm{mm}$. La incompatibilidad se sostiene con todas las combinaciones permitidas por esas cotas. La resolución instrumental, por sí sola, requeriría un análisis adicional para convertirse en una cota del error total de cada lectura.

Con parámetros constantes e iguales intervalos entre picos, el segundo ensayo tendría que conservar el mismo cociente. Partiendo de $30\,\mathrm{mm}$, predeciría $24$ y $19{,}2\,\mathrm{mm}$, tampoco compatibles con $20$ y $10\,\mathrm{mm}$. Las observaciones muestran, en cambio, una disminución de $10\,\mathrm{mm}$ por ciclo. El rozamiento seco aproximadamente constante merece investigarse.

Para precisar esa alternativa, supongamos una fuerza de rozamiento de magnitud constante $f$ durante un recorrido desde un extremo $+A$ hasta el siguiente extremo $-B$, con $A,B>0$. Si el carro desliza todo ese tramo, el balance de energía da $k(A^2-B^2)/2=f(A+B)$. Dividir por $A+B>0$ deja $A-B=2f/k$; otro medio ciclo reduce la excursión en la misma cantidad. La disminución de $10\,\mathrm{mm}$ por ciclo correspondería a $f/k=2{,}5\,\mathrm{mm}$ mientras se conserve el deslizamiento. Cuando la fuerza restauradora ya no venza la adherencia, esta continuación por medios ciclos deja de ser válida. El modelo rival no queda probado sólo con estos picos. Habría que observar los últimos retornos, medir la dependencia de la fuerza con la velocidad y revisar cero instrumental, tiempos y estabilidad del aparato antes de escoger la explicación.

## Lecturas y conexiones

Las secciones 14.7–14.8 de Sears y Zemansky, *Física universitaria*, volumen 1, presentan el amortiguamiento, el balance energético y la respuesta forzada. Las secciones 15.6–15.7 de Serway y Jewett, *Física para ciencias e ingeniería*, volumen 1, ofrecen otro recorrido desde la pérdida de energía hasta una oscilación sostenida. Al cotejar sus descripciones de resonancia, debe precisarse qué magnitud se maximiza y cuándo se está utilizando la aproximación de amortiguamiento pequeño.

El capítulo 8 de Spivak, *Physics for Mathematicians. Mechanics I*, permite comparar los regímenes libre y forzado, el papel de las soluciones homogéneas y el uso de exponenciales complejas. Aquí los coeficientes reales permiten obtener amplitud y fase sin exigir esa herramienta como prerrequisito. Las condiciones y las frecuencias de los máximos se han deducido directamente de las fórmulas del modelo.

El balance de energía retoma los capítulos 7–8; los datos de picos vuelven al problema de medir del capítulo 0, donde una regularidad ajustada no equivale a una predicción independiente.

---

[← 10. El oscilador armónico](fisica-para-matematicos-10-el-oscilador-armonico.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [12. Momento angular y torque →](fisica-para-matematicos-12-momento-angular-y-torque.md)
