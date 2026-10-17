---
title: "Dispersión clásica y reducción efectiva"
subtitle: "Física para matemáticos · Tomo I · Capítulo 19"
author: "A. Peña"
description: "Capítulo 19 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0359
source-id: FISPM-T1-C19
editorial-id: FPM-I-19
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0358"]
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

[Capítulo 18](fisica-para-matematicos-capitulo-18-orbitas-de-kepler.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 20](fisica-para-matematicos-capitulo-20-movimiento-en-marcos-no-inerciales.md)

[]{#fispm-c19-dispersiuxf3n-cluxe1sica-y-reducciuxf3n-efectiva}

Una órbita abierta describe un encuentro: dos cuerpos se aproximan, interactúan y vuelven a separarse. Para comparar encuentros diferentes, necesitamos datos que puedan prepararse lejos de la interacción y resultados que puedan medirse después. La rapidez de entrada y el desplazamiento lateral de la aproximación fijan el estado relativo; el cambio de dirección de salida ofrece una primera medida del efecto de la fuerza.

El movimiento de una sola trayectoria todavía no responde cuántas partículas llegará a ver un detector. Un haz contiene muchos desplazamientos laterales distintos. La sección eficaz conecta esa distribución de preparaciones con una distribución de resultados. Su cálculo reúne dinámica, geometría y una transformación de variables cuya orientación y ramas deben controlarse.

Trabajaremos con interacciones centrales conservativas y un potencial de energía relativa $U(r)$ que tiende a cero en el infinito. Las masas son positivas constantes y la masa reducida es $\mu$. Supondremos que existen velocidades asintóticas de entrada y salida cuando hablemos de dispersión. Los encuentros capturados, los contactos y las singularidades se tratarán por separado. La dinámica principal será clásica y no relativista; la relación posterior con dispersión cuántica conservará su propio régimen.

[]{#preparar-un-encuentro-y-medir-su-resultado}

[]{#fispm-t1-c19-s01}

[]{#fpm-i-19-s01}

## 19.1. Preparar un encuentro y medir su resultado {#fispm-c19-preparar-un-encuentro-y-medir-su-resultado}

Desde lejos, el encuentro puede caracterizarse por una rapidez relativa $v_\infty>0$ y por cuánto se aparta la aproximación de una colisión frontal. El punto de referencia es el origen de la coordenada relativa, no necesariamente un cuerpo inmóvil en el laboratorio.

[]{#fig:I-19-N01}

<figure id="fig-fpm-v04-i-19-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-19-N01.svg" class="lightbox" data-gallery="fpm-v04-c19"><img src="/assets/books/fispm/v04/I-19-N01.svg" alt="Parámetro de impacto. Diagrama del capítulo 19; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="434" height="252" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 19.1.** El parámetro $b$ es la separación perpendicular entre la recta asintótica incidente y el centro. La curva de salida es un esquema de desviación repulsiva; no pretende ser una solución cuantitativa. Véase §[19.1](#fispm-c19-preparar-un-encuentro-y-medir-su-resultado).

</figcaption>

</figure>

[]{#fispm-t1-c19-d0001}

**Definición 19.1 --- Datos asintóticos y parámetro de impacto.** Para un encuentro relativo conservativo, sean $\mathbf w_-$ y $\mathbf w_+$ los límites de la velocidad antes y después, de magnitud $v_\infty$. Definimos

$$E=\frac12\mu v_\infty^2>0,\qquad b=\frac{L}{\mu v_\infty}\geq0,$$

donde $L=|\mathbf q\times\mu\dot{\mathbf q}|$. Cuando hay una línea asintótica entrante bien definida, $b$ es su distancia perpendicular al origen. La definición mediante $L$ evita exigir una aproximación temporal demasiado fuerte. En interacciones de largo alcance, la posición puede acumular una corrección longitudinal que crece lentamente, aunque la velocidad tenga límite y la trayectoria posea una dirección asintótica. No supondremos automáticamente $\mathbf q(t)=\mathbf w_-t+\mathbf b+o(1)$ en todos los potenciales.

[]{#fispm-t1-c19-p0001}

**Proposición 19.1 --- Igualdad de rapideces asintóticas.** Si el encuentro retorna al infinito bajo un potencial autónomo con $U(\infty)=0$, sus rapideces relativas de entrada y salida son iguales.

**Demostración.** La energía conservada es $E=\mu|\mathbf w|^2/2+U(r)$. En cada extremo con $r\to\infty$, el potencial tiende a cero y deja $E=\mu|\mathbf w_\pm|^2/2$. Ambas magnitudes son $\sqrt{2E/\mu}$. $\square$

[]{#fispm-t1-c19-d0002}

**Definición 19.2 --- Ángulo observado de dispersión.**

$$\chi=\arccos\left(\frac{\mathbf w_-\cdot\mathbf w_+}{v_\infty^2}\right), \qquad 0\leq\chi\leq\pi.$$

Es el ángulo entre velocidades, no entre los vectores posición lejanos. No conserva por sí solo el sentido lateral de la desviación ni el número de vueltas durante la interacción.

[]{#fispm-t1-c19-mp0001}

**Principio metodológico 19.1.** Declara qué velocidades son relativas y qué dirección mide el ángulo. Separa rapidez asintótica, parámetro de impacto y orientación lateral.

[]{#ejercicios}

### 19.1.1. Ejercicios {#fispm-c19-ejercicios}

[]{#fispm-t1-c19-e0001}

[]{#fispm-t1-c19-e0019}

**Ejercicio 19.1.** En un movimiento libre, $\mathbf q(t)=vt\,\mathbf e_x+b\,\mathbf e_y$, con $v,b>0$. Calcula $E,L$ y el ángulo de dispersión.

**Solución.** La velocidad es $v\mathbf e_x$ y $E=\mu v^2/2$. El momento angular es $-\mu bv\,\mathbf e_z$, así que su magnitud es $L=\mu bv$ y definición 19.1 recupera el parámetro $b$. La velocidad de salida coincide con la de entrada, por lo que $\chi=0$. Los vectores posición al principio y al final apuntan en sentidos aproximadamente opuestos; usar su ángulo habría dado un resultado incorrecto.

[]{#fispm-t1-c19-e0002}

**Ejercicio 19.2.** Un encuentro conserva $E$ y termina con rapidez relativa de salida distinta de $\sqrt{2E/\mu}$ a un radio finito $R$. ¿Eso contradice proposición 19.1?

**Solución.** No necesariamente. A radio finito, $|\mathbf w(R)|^2=2[E-U(R)]/\mu$. Proposición 19.1 compara los límites donde $U$ tiende a cero. Si el detector mide antes de que el potencial sea despreciable, hay que incluir esa diferencia. Una desigualdad entre las rapideces realmente asintóticas requeriría revisar conservación, potencial o canales de energía adicionales.

[]{#reducción-radial-y-ángulo-de-salida}

[]{#fispm-t1-c19-s02}

[]{#fpm-i-19-s02}

## 19.2. Reducción radial y ángulo de salida {#fispm-c19-reducciuxf3n-radial-y-uxe1ngulo-de-salida}

El potencial efectivo del capítulo 17 permite encontrar hasta dónde se acerca una trayectoria entrante. Luego una integral angular determina cuánto gira el vector separación durante el encuentro.

[]{#fispm-t1-c19-d0003}

**Definición 19.3 --- Función radial normalizada.** Para $b>0$,

$$Q(r)=1-\frac{b^2}{r^2}-\frac{U(r)}{E}.$$

La ecuación energética da $\dot r^2=v_\infty^2Q(r)$. Llamamos $r_{\min}>0$ al primer radio de retorno accesible desde el infinito; bajo las hipótesis siguientes es la mayor raíz relevante que limita la componente exterior admisible.

[]{#fispm-t1-c19-p0002}

**Proposición 19.2 --- Integral de medio encuentro.** Supongamos una raíz simple $Q(r_{\min})=0$, con $Q(r)>0$ para todo $r>r_{\min}$, y un potencial regular en ese intervalo que tiende a cero. El ángulo entre el periastro y cada dirección radial asintótica es

$$\Phi(b)=\int_{r_{\min}}^\infty \frac{b\,dr}{r^2\sqrt{Q(r)}}.$$

El vector separación gira un ángulo total $2\Phi$.

**Demostración.** La velocidad angular positiva en el plano orientado es $\dot\theta=L/(\mu r^2)=bv_\infty/r^2$. Dividirla por la rapidez radial saliente $v_\infty\sqrt Q$ da el integrando. La fuerza autónoma conserva el mismo problema radial en entrada y salida, de modo que ambos tramos aportan igual ángulo. La raíz simple hace integrable el extremo inferior, como se mostró en el capítulo 17; en el infinito, $Q\to1$ y el integrando es comparable a $b/r^2$. $\square$

[]{#fispm-t1-c19-p0003}

**Proposición 19.3 --- De giro radial a desviación.** Definamos el ángulo de desviación con signo por la convención

$$\delta=\pi-2\Phi.$$

El ángulo principal observado es $\chi=\arccos(\cos\delta)$. Cuando $-\pi\leq\delta\leq\pi$, se reduce a $\chi=|\delta|$.

**Demostración.** En la entrada lejana, la velocidad apunta en sentido opuesto al vector radial; en la salida, en el mismo sentido. Por tanto el cambio de dirección entre velocidades difiere en $\pi$ del giro radial total. La convención indicada escoge su signo opuesto. El producto de las direcciones depende del coseno de esa diferencia y definición 19.2 da la expresión principal. En el intervalo de una desviación sin vueltas adicionales, el ángulo principal es el valor absoluto. $\square$

Una desviación repulsiva simple tiene $\Phi<\pi/2$ y $\delta>0$; una atractiva simple puede tener $\Phi>\pi/2$ y $\delta<0$. Cuando hay giro adicional o acercamiento a una órbita inestable, el ángulo sin reducir puede salir de ese intervalo. El ángulo del detector sigue entre cero y $\pi$ y pierde información de vueltas.

[]{#fispm-t1-c19-mp0002}

**Principio metodológico 19.2.** Selecciona la raíz accesible desde el infinito y conserva el ángulo con signo antes de reducirlo al ángulo observado. Las otras raíces pueden pertenecer a regiones que la trayectoria no visita.

[]{#ejercicios-1}

### 19.2.1. Ejercicios {#fispm-c19-ejercicios-1}

[]{#fispm-t1-c19-e0003}

**Ejercicio 19.3.** Para $U=0$ y $b>0$, evalúa $\Phi$ y verifica el resultado libre.

**Solución.** La raíz exterior es $r_{\min}=b$. La sustitución $s=b/r$ da $\Phi=\int_0^1 ds/\sqrt{1-s^2}=\pi/2$. Entonces $\delta=0$ y $\chi=0$. El radio mínimo es el parámetro de impacto sólo en este caso libre.

[]{#fispm-t1-c19-e0004}

**Ejercicio 19.4.** Un cálculo produce $\Phi=5\pi/4$. Encuentra $\delta$ y $\chi$. ¿El detector conserva todo el giro calculado?

**Solución.** $\delta=\pi-2(5\pi/4)=-3\pi/2$. El ángulo principal es $\arccos(\cos(-3\pi/2))=\pi/2$. El giro radial total fue $5\pi/2$; el detector que sólo registra el ángulo entre velocidades entrega $90^\circ$ y no distingue por sí mismo el giro adicional.

[]{#controlar-una-integral-con-un-extremo-singular}

[]{#fispm-t1-c19-s03}

[]{#fpm-i-19-s03}

## 19.3. Controlar una integral con un extremo singular {#fispm-c19-controlar-una-integral-con-un-extremo-singular}

El integrando de la proposición 19.2 diverge en el radio de retorno, aunque su integral sea finita. Esa diferencia importa para un cálculo numérico: evaluar directamente muy cerca de la raíz puede amplificar errores de redondeo o de localización.

[]{#fispm-t1-c19-p0004}

**Proposición 19.4 --- Regularización de una raíz simple.** Si $Q'(r_{\min})>0$ y $Q$ es diferenciable allí, la sustitución $r=r_{\min}+s^2$ transforma la integral cercana en un integrando con límite finito

$$\lim_{s\to0^+} \frac{2bs}{(r_{\min}+s^2)^2\sqrt{Q(r_{\min}+s^2)}} =\frac{2b}{r_{\min}^2\sqrt{Q'(r_{\min})}}.$$

**Demostración.** Diferenciabilidad da $Q(r_{\min}+s^2)=Q'(r_{\min})s^2+o(s^2)$. Para $s>0$, la raíz del denominador es $s\sqrt{Q'(r_{\min})+o(1)}$. El factor $s$ se cancela con el jacobiano $dr=2s\,ds$, dejando el límite. $\square$

[]{#fispm-t1-c19-p0005}

**Proposición 19.5 --- Cota del tramo lejano.** Si $Q(r)\geq c>0$ para $r\geq R$, el ángulo omitido al truncar la integral allí satisface

$$0\leq\int_R^\infty\frac{b\,dr}{r^2\sqrt{Q(r)}} \leq\frac{b}{R\sqrt c}.$$

**Demostración.** Sustituir la cota inferior de $Q$ acota el integrando por $b/(r^2\sqrt c)$. Su integral de $R$ al infinito vale $b/(R\sqrt c)$. $\square$

Esta cota es para $\Phi$; el correspondiente error en $\delta$ es como máximo el doble. Se suma al error de la raíz y de la integración. Si el retorno es doble o se acerca a serlo, proposición 19.4 deja de ofrecer un límite finito uniforme y pueden aparecer tiempos y ángulos muy grandes. En ese caso hay que revisar la estructura del potencial, no sólo aumentar una malla.

[]{#fispm-t1-c19-mp0003}

**Principio metodológico 19.3.** Separa error de localización del retorno, error de cuadratura y cola lejana. Usa una transformación que respete el orden de la raíz.

[]{#ejercicios-2}

### 19.3.1. Ejercicios {#fispm-c19-ejercicios-2}

[]{#fispm-t1-c19-e0005}

**Ejercicio 19.5.** Una integración se corta en $R=100b$ y se ha demostrado $Q\geq1/2$ desde allí. Acota el error en $\Phi$ y en $\delta$ debido sólo al corte.

**Solución.** proposición 19.5 da error de $\Phi$ no mayor que $1/(100\sqrt{1/2})=\sqrt2/100\simeq0,01414$ radianes. Para $\delta=\pi-2\Phi$, la cota es aproximadamente $0,02828$ radianes. Es una cota absoluta de la cola; no incluye los otros errores del cálculo.

[]{#fispm-t1-c19-e0006}

**Ejercicio 19.6.** Cerca de una raíz, $Q(r)$ se comporta como $C(r-r_*)^2$ en el lado exterior, con $C>0$. ¿La sustitución de la proposición 19.4 produce un extremo regular?

**Solución.** Con $r-r_*=s^2$, $\sqrt Q$ se comporta como $\sqrt C\,s^2$. El jacobiano sólo aporta $2s$, de modo que el integrando se comporta como una constante por $1/s$ y la integral diverge. La raíz doble puede representar aproximación asintótica con giro creciente. No es el mismo caso que una raíz simple de retorno.

[]{#la-ley-inversa-del-radio-como-ejemplo-exacto}

[]{#fispm-t1-c19-s04}

[]{#fpm-i-19-s04}

## 19.4. La ley inversa del radio como ejemplo exacto {#fispm-c19-la-ley-inversa-del-radio-como-ejemplo-exacto}

El potencial $U=\pm\kappa/r$, con $\kappa>0$, ofrece un encuentro cuya desviación puede obtenerse sin integrar numéricamente. El signo positivo es repulsivo y el negativo atractivo. El caso atractivo incluye la gravitación del par con $\kappa=Gm_1m_2$; el repulsivo puede modelar una interacción electrostática entre cargas de igual signo.

[]{#fig:I-19-R01}

<figure id="fig-fpm-v04-i-19-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-19-R01.svg" class="lightbox" data-gallery="fpm-v04-c19"><img src="/assets/books/fispm/v04/I-19-R01.svg" alt="Ángulo y parámetro de impacto. Diagrama del capítulo 19; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="438" height="253" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 19.2.** En dispersión por una fuerza inversa del cuadrado, $b=a\cot(\chi/2)$, con $a>0$ fijado por el acoplamiento y la energía lejana. Los encuentros de mayor parámetro de impacto producen menor desviación, bajo las hipótesis de esa ley. Véase §[19.4](#fispm-c19-la-ley-inversa-del-radio-como-ejemplo-exacto).

</figcaption>

</figure>

[]{#fig:I-19-N03}

<figure id="fig-fpm-v04-i-19-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-19-N03.svg" class="lightbox" data-gallery="fpm-v04-c19"><img src="/assets/books/fispm/v04/I-19-N03.svg" alt="Ángulo y parámetro de impacto. Diagrama del capítulo 19; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="432" height="246" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 19.3.** Para la dispersión coulombiana repulsiva, en unidades con $\kappa/(\mu v_\infty^2)=1$, $\chi=2\arctan(1/b)$. Los encuentros más lejanos se desvían menos. Véase §[19.4](#fispm-c19-la-ley-inversa-del-radio-como-ejemplo-exacto).

</figcaption>

</figure>

[]{#fispm-t1-c19-d0004}

**Definición 19.4 --- Longitud de interacción.**

$$\ell=\frac{\kappa}{\mu v_\infty^2} =\frac{\kappa}{2E}>0.$$

Su comparación con $b$ mide la intensidad de la desviación del encuentro.

[]{#fispm-t1-c19-p0006}

**Proposición 19.6 --- Desviación inversa del radio.** Para $b>0$, ambos signos del potencial dan

$$\chi=2\arctan\left(\frac{\ell}{b}\right), \qquad b=\ell\cot(\chi/2).$$

Con la convención de la proposición 19.3, $\delta=+\chi$ para repulsión y $\delta=-\chi$ para atracción.

**Demostración.** La órbita tiene excentricidad $e=\sqrt{1+b^2/\ell^2}>1$. Para atracción, la hipérbola del capítulo 18 tiene $\Phi=\arccos(-1/e)$. Para repulsión, Binet da $r=p/(e\cos\theta-1)$, con $p=L^2/(\mu\kappa)$ y raíz angular lejana $\Phi=\arccos(1/e)$. La relación de $e$ procede de energía y momento, o de sustituir la solución de Binet en la energía. Proposición 19.3 produce respectivamente desviaciones de magnitud $2\arcsin(1/e)$. Como $1/e=\ell/\sqrt{b^2+\ell^2}$, ese ángulo es $2\arctan(\ell/b)$ para valores positivos. $\square$

[]{#fispm-t1-c19-p0007}

**Proposición 19.7 --- Cambio de momento relativo.**

$$|\Delta\mathbf p_{\mathrm{rel}}| =2\mu v_\infty\sin(\chi/2) =\frac{2\mu v_\infty\ell}{\sqrt{b^2+\ell^2}}.$$

**Demostración.** Los momentos de entrada y salida tienen igual magnitud $\mu v_\infty$ y forman ángulo $\chi$. El cuadrado de su diferencia es $2\mu^2v_\infty^2(1-\cos\chi)=4\mu^2v_\infty^2\sin^2(\chi/2)$. La ley de la proposición 19.6 da la segunda expresión. $\square$

Las magnitudes de desviación coinciden para ambas interacciones, pero los lados de salida son diferentes. Una distribución angular que no registre orientación respecto del desplazamiento lateral puede ocultar el signo de la fuerza. En adelante ese hecho reaparecerá al calcular secciones eficaces.[^1]

[]{#fispm-t1-c19-mp0004}

**Principio metodológico 19.4.** Conserva el signo de la interacción y distingue desviación lateral de su magnitud. El mismo ángulo principal no prueba el mismo mecanismo físico.

[]{#ejercicios-3}

### 19.4.1. Ejercicios {#fispm-c19-ejercicios-3}

[]{#fispm-t1-c19-e0007}

**Ejercicio 19.7.** Para un encuentro inverso del radio con $b=\ell$, calcula la desviación y el cambio de momento relativo.

**Solución.** $\chi=2\arctan1=\pi/2$. Proposición 19.7 da $|\Delta\mathbf p_{\mathrm{rel}}|=\sqrt2\,\mu v_\infty$. La desviación con signo es positiva en repulsión y negativa en atracción bajo la convención fijada.

[]{#fispm-t1-c19-e0008}

**Ejercicio 19.8.** Mantén $b,\kappa,\mu$ y duplica $v_\infty$. ¿La desviación se divide exactamente por cuatro?

**Solución.** La longitud $\ell$ se divide por cuatro y la nueva desviación es $\chi_{\mathrm{nueva}}=2\arctan[\ell/(4b)]$. No es en general la cuarta parte de $2\arctan(\ell/b)$. La proporcionalidad aparece como aproximación cuando $\ell/b\ll1$, porque entonces $\arctan x\simeq x$. El cambio de escala de la fuerza no debe confundirse con una linealidad exacta del ángulo.

[]{#máxima-aproximación-y-encuentro-con-una-superficie}

[]{#fispm-t1-c19-s05}

[]{#fpm-i-19-s05}

## 19.5. Máxima aproximación y encuentro con una superficie {#fispm-c19-muxe1xima-aproximaciuxf3n-y-encuentro-con-una-superficie}

El parámetro de impacto se define lejos del encuentro. La fuerza puede acercar la trayectoria a la región central o alejarla de ella. Por eso no se identifica en general con la distancia mínima ni con la condición geométrica de contacto.

[]{#fispm-t1-c19-p0008}

**Proposición 19.8 --- Radios mínimos inversos del radio.** Para $b>0$,

$$r_{\min}^{\mathrm{rep}}=\ell+\sqrt{\ell^2+b^2}, \qquad r_{\min}^{\mathrm{atr}}=-\ell+\sqrt{\ell^2+b^2}.$$

**Demostración.** En el retorno, $E=L^2/(2\mu r^2)\pm\kappa/r$. Usar $L=\mu v_\infty b$ y $E=\mu v_\infty^2/2$ da $r^2\mp2\ell r-b^2=0$. La raíz positiva es la indicada para cada signo. $\square$

La repulsión aumenta la máxima distancia de acercamiento respecto de $b$, mientras la atracción la reduce. En el límite $b\to0$, la repulsión tiene retorno radial en $2\ell$; la atracción puntual lleva hacia la singularidad. La fórmula angular del encuentro no debe convertir esa coincidencia singular en una dispersión saliente bien definida.

[]{#fispm-t1-c19-p0009}

**Proposición 19.9 --- Condición para alcanzar un radio absorbente.** Supongamos que una trayectoria que llega a $r=R>0$ se absorbe o cambia de canal por un mecanismo declarado. Para el potencial atractivo $-\kappa/r$, los impactos que alcanzan ese radio cumplen

$$b^2\leq R^2+2\ell R.$$

Para el repulsivo $+\kappa/r$, cumplen $b^2\leq R^2-2\ell R$, si el miembro derecho es no negativo; si es negativo, ninguno llega.

**Demostración.** Las expresiones de la proposición 19.8 son crecientes en $b$. Imponer $r_{\min}\leq R$ y despejar produce cada desigualdad. Equivale a que el estado exterior alcance $R$ con velocidad radial real, sin un retorno previo. El caso radial se interpreta directamente con la energía, no mediante un plano orbital indeterminado. $\square$

La ley central conservativa, por sí sola, no captura una trayectoria que llega del infinito y vuelve a salir bajo sus hipótesis. Para llamar captura a alcanzar $R$ hace falta el mecanismo que absorbe o disipa allí. En un encuentro de cuerpos extensos, $R$ puede ser la suma de sus radios de contacto; la dinámica posterior pertenece a otro modelo.

[]{#fispm-t1-c19-mp0005}

**Principio metodológico 19.5.** Separa la aproximación determinada por la fuerza del mecanismo de contacto o captura. Declara el radio y el cambio de modelo al alcanzarlo.

[]{#ejercicios-4}

### 19.5.1. Ejercicios {#fispm-c19-ejercicios-4}

[]{#fispm-t1-c19-e0009}

**Ejercicio 19.9.** Para $b=2\ell$, compara los radios mínimos atractivo, repulsivo y libre.

**Solución.** Los valores son $(\sqrt5-1)\ell$, $(\sqrt5+1)\ell$ y $2\ell$. Aproximadamente son $1,236\ell$, $3,236\ell$ y $2\ell$. La misma preparación lejana puede alcanzar distancias centrales muy distintas bajo fuerzas de sentidos opuestos, aunque sus ángulos principales de dispersión coincidan en el ejemplo inverso del radio.

[]{#fispm-t1-c19-e0010}

**Ejercicio 19.10.** Para una interacción atractiva con $\ell=R$, encuentra el radio máximo de impacto que alcanza la superficie $R$. Compara con el límite geométrico sin fuerza.

**Solución.** proposición 19.9 da $b_{\max}=\sqrt{R^2+2R^2}=\sqrt3\,R$. Sin interacción, sólo llegan los impactos con $b\leq R$. La atracción enfoca también preparaciones que pasarían fuera de la superficie en un movimiento libre.

[]{#sección-eficaz-como-área-de-preparación}

[]{#fispm-t1-c19-s06}

[]{#fpm-i-19-s06}

## 19.6. Sección eficaz como área de preparación {#fispm-c19-secciuxf3n-eficaz-como-uxe1rea-de-preparaciuxf3n}

Un haz uniforme prepara distintos parámetros de impacto con una distribución proporcional al área transversal. La sección eficaz de un resultado cuenta cuánta área de esa preparación lo produce. No tiene por qué coincidir con el tamaño geométrico del objeto: una fuerza puede enfocar trayectorias o desviarlas antes del contacto.

[]{#fig:I-19-N02}

<figure id="fig-fpm-v04-i-19-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-19-N02.svg" class="lightbox" data-gallery="fpm-v04-c19"><img src="/assets/books/fispm/v04/I-19-N02.svg" alt="Área de preparación. Diagrama del capítulo 19; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="425" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 19.4.** En una preparación axialmente simétrica, un anillo de radios $b,b+db$ tiene área diferencial $d\sigma=2\pi b\,db$. Es un área del haz incidente, no una superficie de la trayectoria. Véase §[19.6](#fispm-c19-secciuxf3n-eficaz-como-uxe1rea-de-preparaciuxf3n).

</figcaption>

</figure>

[]{#fispm-t1-c19-d0005}

**Definición 19.5 --- Sección eficaz de un conjunto de resultados.** Para un haz uniforme de rapidez fijada y una interacción dada, sea $\mathcal B$ el conjunto de vectores de impacto que producen el resultado seleccionado. Definimos

$$\sigma(\mathcal B)=\int_{\mathcal B}d^2b.$$

Tiene unidades de área. Si la selección es simétrica alrededor del eje entrante y corresponde a impactos entre $b_a$ y $b_b$, su sección es $\pi(b_b^2-b_a^2)$. El elemento anular es $d\sigma=2\pi b\,db$.

[]{#fispm-t1-c19-p0010}

**Proposición 19.10 --- Flujo y tasa de eventos.** Para un blanco aislado ideal y flujo incidente uniforme $j$ de partículas por área y tiempo, la tasa esperada del resultado es $\dot N=j\sigma$. Si un haz finito uniforme de área $A$ contiene íntegramente la región de impactos del resultado, la fracción de partículas que lo producen es $\sigma/A$.

**Demostración.** Un área transversal $d^2b$ recibe $j\,d^2b$ partículas por tiempo. Integrar sobre la región seleccionada da $j\sigma$. El haz completo recibe $jA$, por lo que dividir ambas tasas produce la fracción. $\square$

La hipótesis de inclusión importa. Para un haz estrecho que no cubre toda la región seleccionada, se integra sólo la intersección. Si el flujo varía con la posición, la tasa es $\int_{\mathcal B}j(\mathbf b)\,d^2b$ y no un producto con un único valor arbitrario de flujo.

Proposición 19.9 y definición 19.5 dan, para una superficie absorbente en el campo atractivo, $\sigma_{\mathrm{cap}}=\pi R^2(1+2\ell/R)$. El área excede $\pi R^2$ por enfoque. Para repulsión es $\pi\max(R^2-2\ell R,0)$. Estas secciones pertenecen al canal de alcanzar la superficie, no al de salida elástica desde ella.

[]{#fispm-t1-c19-mp0006}

**Principio metodológico 19.6.** Define el resultado contado y la distribución de preparación. Convierte áreas en probabilidades sólo después de normalizar el haz pertinente.

[]{#ejercicios-5}

### 19.6.1. Ejercicios {#fispm-c19-ejercicios-5}

[]{#fispm-t1-c19-e0011}

**Ejercicio 19.11.** Un haz uniforme de área $100\,\mathrm{mm^2}$ cubre una región de impactos seleccionados de sección $5\,\mathrm{mm^2}$. Calcula la fracción de eventos. ¿Qué cambia si esa región queda parcialmente fuera del haz?

**Solución.** Bajo inclusión completa, la fracción es $5/100=0,05$, un $5\%$. Si parte de la región queda fuera, el numerador es su área de intersección con el haz y la fracción disminuye. La sección propia de la interacción sigue siendo $5\,\mathrm{mm^2}$; cambió la preparación experimental que la ilumina.

[]{#fispm-t1-c19-e0012}

**Ejercicio 19.12.** En un modelo de blanco aislado, $j=10^4\,\mathrm{m^{-2}s^{-1}}$ y la sección del resultado es $2\times10^{-6}\,\mathrm{m^2}$. Calcula la tasa y el número esperado durante $100\,\mathrm s$.

**Solución.** La tasa es $j\sigma=0,02\,\mathrm{s^{-1}}$. Durante el intervalo, el número esperado es $2$. Es una media del modelo de preparación, no la afirmación de que cada repetición del experimento arroje exactamente dos eventos.

[]{#la-distribución-angular-y-sus-ramas}

[]{#fispm-t1-c19-s07}

[]{#fpm-i-19-s07}

## 19.7. La distribución angular y sus ramas {#fispm-c19-la-distribuciuxf3n-angular-y-sus-ramas}

Para calcular cuántas partículas salen por un ángulo dado, transformamos el área de impactos en un área de direcciones. El ángulo sólido mide esa segunda área en la esfera unitaria.

[]{#fispm-t1-c19-d0006}

**Definición 19.6 --- Ángulo sólido y sección diferencial.** En coordenadas de dirección $\chi,\varphi$,

$$d\Omega=\sin\chi\,d\chi\,d\varphi.$$

La sección diferencial $d\sigma/d\Omega$ se define de modo que $d\sigma=(d\sigma/d\Omega)\,d\Omega$. Usamos esta normalización estándar, sin un factor adicional $4\pi$. Su unidad es área por estereorradián.

La fórmula del ángulo sólido procede de una franja sobre la esfera unitaria: el arco meridiano tiene longitud $d\chi$ y el arco paralelo $\sin\chi\,d\varphi$. La simetría central hace uniforme el azimut de salida para un haz sin preferencia azimutal.

[]{#fispm-t1-c19-p0011}

**Proposición 19.11 --- Una rama angular regular.** Si $b\mapsto\chi(b)$ es invertible y diferenciable en una rama con $0<\chi<\pi$ y derivada no nula,

$$\frac{d\sigma}{d\Omega} =\frac{b}{\sin\chi}\left|\frac{db}{d\chi}\right|.$$

**Demostración.** El anillo de impactos aporta $2\pi b\,|db|$. Las direcciones de salida en la franja aportan $2\pi\sin\chi\,|d\chi|$. Dividir y usar el cambio de variable da la expresión. El valor absoluto conserva el área cuando el ángulo decrece al aumentar el impacto. $\square$

[]{#fispm-t1-c19-p0012}

**Proposición 19.12 --- Suma de ramas.** Si un mismo ángulo regular recibe contribuciones de varias ramas disjuntas de impacto, entonces

$$\frac{d\sigma}{d\Omega} =\sum_j\frac{b_j(\chi)}{\sin\chi} \left|\frac{db_j}{d\chi}\right|.$$

**Demostración.** Cada rama representa una región distinta de preparación y aporta el área de la proposición 19.11. Las áreas de regiones disjuntas se suman, aunque sus direcciones de salida coincidan. $\square$

En los ejes $\chi=0,\pi$, o en puntos donde la derivada angular se anula, la fórmula requiere límites o una integración por intervalos. También puede existir una contribución concentrada exactamente en la dirección de entrada, como ocurre con impactos libres fuera de una interacción de alcance finito. Esa contribución no se representa mediante una densidad ordinaria finita.

[]{#fispm-t1-c19-mp0007}

**Principio metodológico 19.7.** Mantén valores absolutos, suma ramas y calcula intervalos finitos cerca de singularidades. Una densidad angular no reemplaza una medida concentrada en una dirección.

[]{#ejercicios-6}

### 19.7.1. Ejercicios {#fispm-c19-ejercicios-6}

[]{#fispm-t1-c19-e0013}

**Ejercicio 19.13.** Una rama tiene $b(\chi)=\ell\cot(\chi/2)$. Calcula $db/d\chi$ y explica por qué no puede usarse su signo directamente como sección.

**Solución.** La derivada es $-(\ell/2)\csc^2(\chi/2)$, negativa. Un ángulo mayor corresponde a un impacto menor. El elemento de área debe ser no negativo; proposición 19.11 usa el valor absoluto. Sin él se obtendría una sección diferencial negativa, que no puede contar una región de preparación.

[]{#fispm-t1-c19-e0014}

**Ejercicio 19.14.** En una franja angular interior, dos ramas disjuntas tienen $b_1=a\chi$ y $b_2=c+a\chi$, con $a,c>0$. Calcula la sección diferencial de esa franja. La relación es un ejemplo local de cambio de variables, sin atribuirle una ley de fuerza específica.

**Solución.** Ambas derivadas tienen magnitud $a$. Proposición 19.12 da $d\sigma/d\Omega=[a(a\chi)+a(c+a\chi)]/\sin\chi =(ac+2a^2\chi)/\sin\chi$. Las dos áreas suman, no se cancelan. Que las ramas sean disjuntas significa que los intervalos de impacto seleccionados no se superponen en el dominio local considerado.

[]{#sección-inversa-del-radio-y-resolución-angular}

[]{#fispm-t1-c19-s08}

[]{#fpm-i-19-s08}

## 19.8. Sección inversa del radio y resolución angular {#fispm-c19-secciuxf3n-inversa-del-radio-y-resoluciuxf3n-angular}

La ley exacta de §4 permite calcular una distribución angular completa. El resultado muestra cómo un alcance largo afecta a los eventos de desviación pequeña.

[]{#fispm-t1-c19-p0013}

**Proposición 19.13 --- Sección diferencial inversa del radio.** Para $U=\pm\kappa/r$ sin canal absorbente y $0<\chi<\pi$,

$$\frac{d\sigma}{d\Omega} =\frac{\ell^2}{4\sin^4(\chi/2)} =\left(\frac{\kappa}{4E}\right)^2 \frac1{\sin^4(\chi/2)}.$$

**Demostración.** proposición 19.6 da $b=\ell\cot(\chi/2)$ y ejercicio 19.13 su derivada. Sustituir en la proposición 19.11 y usar $\sin\chi=2\sin(\chi/2)\cos(\chi/2)$ cancela el coseno y deja $\ell^2/[4\sin^4(\chi/2)]$. Definición 19.4 da la segunda expresión. El posible caso puntual $b=0$ no cambia una sección como área. $\square$

En el modelo electrostático repulsivo, esta forma es la ley de Rutherford con el coeficiente de interacción pertinente. Aquí se ha derivado como una ley clásica de un potencial, con energía relativa y masa reducida explícitas. No se presupone que un blanco móvil pueda tratarse siempre como inmóvil.[^2]

[]{#fispm-t1-c19-p0014}

**Proposición 19.14 --- Sección por encima de un umbral angular.** Para $0<\chi_0<\pi$,

$$\sigma(\chi\geq\chi_0) =\pi\ell^2\cot^2(\chi_0/2).$$

Tiende a infinito cuando $\chi_0\to0^+$.

**Demostración.** La ley de la proposición 19.6 es decreciente: la condición angular equivale al disco de impactos $b\leq\ell\cot(\chi_0/2)$. Su área da la expresión. Como $\cot(\chi_0/2)\sim2/\chi_0$, el área crece como $4\pi\ell^2/\chi_0^2$. $\square$

La divergencia significa que el modelo de alcance infinito desvía, aunque muy poco, preparaciones a impactos arbitrariamente grandes. Un detector con umbral positivo mide una sección finita. Una interacción apantallada o un haz finito exige otra selección de eventos y puede modificar el comportamiento frontal.

[]{#fispm-t1-c19-mp0008}

**Principio metodológico 19.8.** Declara la resolución angular y el canal antes de integrar una sección. Una divergencia frontal del modelo no implica un número infinito de eventos en un haz finito.

[]{#ejercicios-7}

### 19.8.1. Ejercicios {#fispm-c19-ejercicios-7}

[]{#fispm-t1-c19-e0015}

**Ejercicio 19.15.** Encuentra la sección de eventos con $\chi\geq\pi/2$ en el potencial inverso del radio y compara con $\chi\geq\pi/3$.

**Solución.** Para el primer umbral, $\cot(\pi/4)=1$ y la sección es $\pi\ell^2$. Para el segundo, $\cot(\pi/6)=\sqrt3$ y la sección es $3\pi\ell^2$. Bajar el umbral incluye más impactos lejanos.

[]{#fispm-t1-c19-e0016}

**Ejercicio 19.16.** Mantén $\kappa$ y el ángulo de observación, pero duplica la energía relativa $E$. Compara las secciones diferenciales.

**Solución.** proposición 19.13 es proporcional a $E^{-2}$, por lo que la nueva sección es la cuarta parte. Esta proporcionalidad es exacta en el modelo inverso del radio a ángulo fijo. No equivale a afirmar que el ángulo a impacto fijo dependa linealmente de la energía.

[]{#una-esfera-que-devuelve-la-partícula}

[]{#fispm-t1-c19-s09}

[]{#fpm-i-19-s09}

## 19.9. Una esfera que devuelve la partícula {#fispm-c19-una-esfera-que-devuelve-la-partuxedcula}

Hasta ahora el acercamiento terminaba en un punto de retorno suave o en una superficie absorbente. Una superficie rígida plantea otra regla. Consideremos el movimiento relativo alrededor de una esfera impenetrable de radio $a$. Fuera de ella no hay fuerza; en el contacto la velocidad se refleja de manera especular. Este modelo describe una esfera fija o una interacción relativa elástica entre dos cuerpos cuyo radio de contacto es $a$.

[]{#fispm-t1-c19-d0007}

**Definición 19.7 --- Reflexión especular.** Si $\mathbf n$ es la normal exterior unitaria en el contacto, la regla es

$$\mathbf w_+=\mathbf w_--2(\mathbf w_-\cdot\mathbf n)\mathbf n.$$

Conserva la componente tangencial, invierte la normal y conserva la rapidez. La superficie suministra un impulso; la ecuación diferencial libre solo describe los tramos anterior y posterior.

[]{#fispm-t1-c19-p0015}

**Proposición 19.15 --- Ley angular de la esfera rígida.** Para $0\leq b\leq a$, el ángulo de dispersión satisface

$$\chi=\pi-2\arcsin(b/a),\qquad b=a\cos(\chi/2).$$

**Demostración.** Tomemos $\mathbf w_-=v_\infty\mathbf e_x$ y la recta incidente $y=b$. El contacto ocurre en $(-\sqrt{a^2-b^2},b)$, de modo que $\mathbf n=(-\sqrt{1-b^2/a^2},b/a)$. La regla de reflexión da $\mathbf w_-\cdot\mathbf w_+/v_\infty^2=2b^2/a^2-1$. En el intervalo $0\leq b/a\leq1$, esta cantidad es $\cos(\pi-2\arcsin(b/a))$. La definición del ángulo principal prueba ambas expresiones. El contacto rasante puede entenderse como límite; su conjunto tiene área nula. $\square$

[]{#fispm-t1-c19-p0016}

**Proposición 19.16 --- Sección diferencial constante.** Para $0<\chi<\pi$, la esfera rígida tiene

$$\frac{d\sigma}{d\Omega}=\frac{a^2}{4},\qquad \sigma_{\mathrm{contacto}}=\pi a^2.$$

**Demostración.** Derivar $b=a\cos(\chi/2)$ da $|db/d\chi|=(a/2)\sin(\chi/2)$. Proposición 19.11 y la identidad del seno doble dan $a^2/4$. Su integral sobre la esfera de direcciones es $(a^2/4)4\pi=\pi a^2$, igual al área del disco de impactos que toca la superficie. $\square$

Una densidad constante por unidad de ángulo sólido produce más eventos por unidad de $\chi$ cerca del ecuador angular, porque allí $2\pi\sin\chi$ es mayor. La palabra «uniforme» requiere especificar la medida. Para $b>a$ la dirección no cambia. Si un haz finito incluye esos impactos, el canal transmitido contiene una contribución concentrada en la dirección frontal. Esa contribución no se obtiene prolongando la densidad constante hasta describir todo el haz.

[]{#fispm-t1-c19-mp0009}

**Principio metodológico 19.9.** Una condición de contacto pertenece al modelo. Escríbela antes de calcular la trayectoria o la sección del canal que produce.

[]{#ejercicios-8}

### 19.9.1. Ejercicios {#fispm-c19-ejercicios-8}

[]{#fispm-t1-c19-e0017}

**Ejercicio 19.17.** Calcula la fracción de contactos con $\chi\geq\pi/2$ para un haz uniforme.

**Solución.** La condición equivale a $b\leq a/\sqrt2$. Su área es $\pi a^2/2$, y dividir por $\pi a^2$ da $1/2$. También se obtiene integrando la densidad constante sobre un hemisferio de direcciones, de área angular $2\pi$.

[]{#fispm-t1-c19-e0018}

**Ejercicio 19.18.** Un haz uniforme ocupa un disco de radio $B>a$. Describe la probabilidad de transmisión sin cambio de dirección y la densidad angular de los eventos reflejados.

**Solución.** El anillo $a<b\leq B$ tiene probabilidad $1-a^2/B^2$ y se concentra en la dirección incidente. Los contactos tienen probabilidad $a^2/B^2$. Su densidad de probabilidad por unidad de ángulo sólido es $a^2/(4\pi B^2)$; al integrarla se recupera $a^2/B^2$. Condicionada a que haya contacto, la densidad es $1/(4\pi)$. Las tres cantidades tienen normalizaciones distintas y responden a preguntas distintas.

[]{#varias-preparaciones-una-dirección}

[]{#fispm-t1-c19-s10}

[]{#fpm-i-19-s10}

## 19.10. Varias preparaciones, una dirección {#fispm-c19-varias-preparaciones-una-direcciuxf3n}

La ley inversa del radio es monótona. Una interacción con zonas atractivas y repulsivas puede producir una función angular que primero crezca y después decrezca. Entonces una dirección recibe eventos procedentes de impactos distintos. Proposición 19.12 permite sumarlos cuando las ramas son regulares. Falta examinar el punto donde dejan de serlo.

[]{#fispm-t1-c19-d0008}

**Definición 19.8 --- Punto crítico angular simple.** Sea $\chi(b)$ una función de clase $C^3$ cerca de $b_c>0$, con $0<\chi_c=\chi(b_c)<\pi$. Llamaremos crítico simple al caso $\chi'(b_c)=0$ y $\chi''(b_c)=c\ne0$.

[]{#fispm-t1-c19-p0017}

**Proposición 19.17 --- Concentración integrable cerca de un extremo angular.** En el lado angular donde existen las dos ramas próximas a $b_c$, su contribución conjunta satisface

$$\frac{d\sigma}{d\Omega}\sim \frac{\sqrt2\,b_c}{\sin\chi_c\sqrt{|c|}} \frac1{\sqrt{|\chi-\chi_c|}}.$$

La sección de un intervalo angular finito alrededor de ese extremo es finita.

**Demostración.** Taylor da $\chi-\chi_c=(c/2)(b-b_c)^2+O((b-b_c)^3)$. En el lado con $c(\chi-\chi_c)>0$ hay dos soluciones locales, con $b-b_c\sim\pm\sqrt{2|\chi-\chi_c|/|c|}$. Además $\chi'(b)=c(b-b_c)+O((b-b_c)^2)$, de donde cada $|db/d\chi|\sim[2|c||\chi-\chi_c|]^{-1/2}$. Cada rama aporta $b_c/\sin\chi_c$ por ese factor; sumar las dos prueba el coeficiente. Para integrar en dirección se multiplica por $2\pi\sin\chi\,d\chi$. El seno permanece acotado y separado de cero localmente, y $\int_0^\varepsilon x^{-1/2}dx=2\sqrt\varepsilon$. $\square$

Esta concentración recibe habitualmente el nombre de arcoíris clásico. El término describe una acumulación de preparaciones en direcciones vecinas. La densidad ideal puede divergir mientras cada detector de apertura finita registra una cantidad finita. La proposición es local: otras ramas, si las hay, deben añadirse.

Hay otra singularidad distinta. Si la raíz radial accesible se vuelve doble, la integral de $\Phi$ puede crecer sin límite. Cerca de la raíz, un factor $Q(r)\sim C(r-r_c)^2$, con $C>0$, produce una integral proporcional a $\int dr/|r-r_c|$. La trayectoria se demora cerca de una órbita circular inestable y puede dar muchas vueltas. El ángulo principal sigue perteneciendo a $[0,\pi]$, aunque $\pi-2\Phi$ ya no esté entre $-\pi$ y $\pi$. La demora y las vueltas no establecen por sí solas captura; hay que examinar el canal y la continuación del movimiento.

[]{#fispm-t1-c19-mp0010}

**Principio metodológico 19.10.** Ante una densidad singular, vuelve al área de preparaciones y calcula un intervalo observable. Distingue un extremo de la función angular de una raíz múltiple en la dinámica radial.

[]{#ejercicios-9}

### 19.10.1. Ejercicios {#fispm-c19-ejercicios-9}

**Ejercicio 19.19.** Supón localmente $\chi=\chi_c+A(b-b_c)^2$, con $A>0$. Calcula la sección del intervalo $\chi_c\leq\chi\leq\chi_c+\varepsilon$, contando ambas ramas y suponiendo $\sqrt{\varepsilon/A}<b_c$.

**Solución.** El conjunto de impactos es $b_c-d\leq b\leq b_c+d$, donde $d=\sqrt{\varepsilon/A}$. Su área es $\pi[(b_c+d)^2-(b_c-d)^2]=4\pi b_c\sqrt{\varepsilon/A}$. El crecimiento es proporcional a $\sqrt\varepsilon$. Derivar esta sección respecto del límite superior produce una densidad angular integrada en azimut proporcional a $\varepsilon^{-1/2}$, coherente con la proposición 19.17 porque $c=2A$.

[]{#fispm-t1-c19-e0020}

**Ejercicio 19.20.** Una trayectoria tiene $\Phi=5\pi/3$. Calcula el ángulo observado y decide si puede usarse $\chi=|\pi-2\Phi|$.

**Solución.** El giro firmado definido en §2 es $\delta=-7\pi/3$. Por tanto $\cos\delta=1/2$ y $\chi=\arccos(1/2)=\pi/3$. El valor absoluto sería $7\pi/3$, fuera del intervalo de los ángulos principales. Para recuperar una dirección hay que conservar la periodicidad, además de la información dinámica sobre las vueltas.

[]{#cuánto-basta-con-integrar-sobre-una-recta}

[]{#fispm-t1-c19-s11}

[]{#fpm-i-19-s11}

## 19.11. Cuánto basta con integrar sobre una recta {#fispm-c19-cuuxe1nto-basta-con-integrar-sobre-una-recta}

Para impactos grandes, la interacción puede cambiar poco la velocidad. En ese régimen se intenta calcular el impulso sobre la trayectoria libre. La propuesta necesita una comprobación posterior: si la corrección resulta grande, la trayectoria usada para calcularla deja de ser una referencia adecuada.

[]{#fispm-t1-c19-p0018}

**Proposición 19.18 --- Impulso transversal en la aproximación rectilínea.** Sea una fuerza relativa central $\mathbf F=f(r)\mathbf q/r$, donde $f>0$ significa repulsión. Al sustituir $\mathbf q_0(t)=(v_\infty t,b,0)$, con $b>0$, el impulso transversal por unidad de masa reducida es

$$\Delta w_y^{(0)}=\frac b\mu\int_{-\infty}^{\infty} \frac{f(\sqrt{v_\infty^2t^2+b^2})}{\sqrt{v_\infty^2t^2+b^2}}\,dt,$$

si la integral converge. Para $f(r)=\pm\kappa/r^2$ vale $\Delta w_y^{(0)}/v_\infty=\pm2\ell/b$.

**Demostración.** La componente transversal de $\mu\dot{\mathbf w}=\mathbf F$ evaluada sobre $\mathbf q_0$ es $b f(r)/(\mu r)$. Integrar da la primera fórmula. Para la fuerza inversa del cuadrado, sustituir $u=v_\infty t/b$ deja $\pm\kappa/(\mu b v_\infty)\int_{-\infty}^{\infty}(1+u^2)^{-3/2}du$. Una primitiva es $u/\sqrt{1+u^2}$, cuyos límites difieren en dos. Dividir por $v_\infty$ y usar la definición de $\ell$ prueba el resultado. $\square$

Esta proposición calcula exactamente una integral sobre una recta elegida. La identificación de su resultado con la desviación real es una aproximación adicional. Para desviaciones pequeñas, el cambio transversal dividido por la rapidez coincide con el ángulo firmado al primer orden. En el ejemplo inverso del radio podemos contrastarlo con la respuesta exacta.

[]{#fispm-t1-c19-p0019}

**Proposición 19.19 --- Error angular del primer término.** Para $x=\ell/b\geq0$, el ángulo exacto $\chi=2\arctan x$ cumple

$$0\leq2x-\chi\leq\frac23x^3.$$

**Demostración.** La diferencia es $2\int_0^x[1-(1+u^2)^{-1}]du=2\int_0^x u^2/(1+u^2)du$. El integrando está entre cero y $u^2$. Integrar esas cotas prueba el enunciado. $\square$

En particular, cuando $x$ es pequeño, el error relativo respecto de la predicción $2x$ es a lo sumo $x^2/3$. Esa cota corresponde a este potencial y a esta fórmula angular; no proporciona automáticamente una cota de error para cualquier fuerza o para toda la trayectoria.

[]{#fispm-t1-c19-mp0011}

**Principio metodológico 19.11.** Expresa el parámetro pequeño como una razón adimensional y contrasta la aproximación con una cantidad observable. Indica qué error se ha acotado.

[]{#ejercicios-10}

### 19.11.1. Ejercicios {#fispm-c19-ejercicios-10}

[]{#fispm-t1-c19-e0021}

**Ejercicio 19.21.** Si $b=10\ell$, acota el error de la aproximación $\chi\approx2\ell/b$.

**Solución.** Aquí $x=0.1$. La predicción es $0.2$ radianes y su exceso sobre el valor exacto está entre cero y $2(0.1)^3/3=1/1500$ radianes. Respecto de $0.2$, el error es como máximo $1/300$, aproximadamente $0.33\%$.

[]{#fispm-t1-c19-e0022}

**Ejercicio 19.22.** Evalúa el impulso rectilíneo para $f(r)=C/r^3$ y formula una condición de pequeña desviación.

**Solución.** proposición 19.18 da $\Delta w_y^{(0)}=Cb\mu^{-1}\int dt/(v_\infty^2t^2+b^2)^2$. Con $u=v_\infty t/b$, resulta $C/(\mu v_\infty b^2)\int du/(1+u^2)^2$. La sustitución $u=\tan s$ transforma la integral en $\int_{-\pi/2}^{\pi/2}\cos^2s\,ds=\pi/2$. Por tanto $\Delta w_y^{(0)}/v_\infty=\pi C/(2\mu v_\infty^2b^2)$. Su magnitud debe ser mucho menor que uno. Es una comprobación necesaria para la aproximación propuesta; por sí sola no demuestra una estimación uniforme del error de trayectoria.

[]{#el-detector-vive-en-el-laboratorio}

[]{#fispm-t1-c19-s12}

[]{#fpm-i-19-s12}

## 19.12. El detector vive en el laboratorio {#fispm-c19-el-detector-vive-en-el-laboratorio}

La reducción radial usa la velocidad relativa. Un detector puede medir la velocidad de un solo cuerpo en un marco donde el otro estaba inicialmente en reposo. Traducir ambas descripciones es parte del problema físico.

Tomemos masas $m_1,m_2>0$, $M=m_1+m_2$, proyectil incidente con velocidad $v\mathbf e_x$ y blanco inicialmente quieto. Supondremos un encuentro elástico, con energía potencial tendiendo al mismo valor cero antes y después. Entonces $\mathbf V=(m_1/M)v\mathbf e_x$, $\mathbf w_-=v\mathbf e_x$ y, eligiendo el lado positivo del plano de dispersión, $\mathbf w_+=v(\cos\chi\mathbf e_x+\sin\chi\mathbf e_y)$.

[]{#fispm-t1-c19-p0020}

**Proposición 19.20 --- Transformación cinemática al laboratorio.** Las velocidades finales son

$$\mathbf v_{1+}=\frac vM[(m_1+m_2\cos\chi)\mathbf e_x+m_2\sin\chi\mathbf e_y],$$

$$\mathbf v_{2+}=\frac{m_1v}{M}[(1-\cos\chi)\mathbf e_x-\sin\chi\mathbf e_y].$$

Si la velocidad del proyectil no se anula, su ángulo de laboratorio es $\theta=\operatorname{atan2}(m_2\sin\chi,m_1+m_2\cos\chi)\in[0,\pi].$

**Demostración.** La descomposición de dos cuerpos es $\mathbf v_1=\mathbf V+(m_2/M)\mathbf w$ y $\mathbf v_2=\mathbf V-(m_1/M)\mathbf w$. Sustituir $\mathbf w_+$ da las fórmulas. El ángulo se determina por ambas componentes, que es precisamente la información preservada por $\operatorname{atan2}$. $\square$

[]{#fispm-t1-c19-p0021}

**Proposición 19.21 --- Reparto de energía y masas iguales.** Respecto de la energía incidente $K_{\mathrm{in}}=m_1v^2/2$, la energía final del blanco satisface

$$\frac{K_{2+}}{K_{\mathrm{in}}}=\frac{4m_1m_2}{M^2}\sin^2(\chi/2).$$

Para $m_1=m_2$ y $0\leq\chi<\pi$, se cumple $\theta=\chi/2$ y $|\mathbf v_{1+}|=v\cos(\chi/2)$. Si $\chi=\pi$, el proyectil queda quieto y su dirección final no está definida.

**Demostración.** La norma al cuadrado de la velocidad del blanco en la proposición 19.20 es $(m_1v/M)^2[(1-\cos\chi)^2+\sin^2\chi]=4(m_1v/M)^2\sin^2(\chi/2)$. Multiplicar por $m_2/2$ y dividir por $K_{\mathrm{in}}$ prueba la fracción. Para masas iguales, la velocidad del proyectil es $v\cos(\chi/2)[\cos(\chi/2)\mathbf e_x+\sin(\chi/2)\mathbf e_y]$. Sus consecuencias incluyen la excepción en $\chi=\pi$. $\square$

[]{#fispm-t1-c19-p0022}

**Proposición 19.22 --- Límite angular para un proyectil más pesado.** Si $m_1>m_2$, el ángulo de laboratorio alcanza un máximo

$$\theta_{\max}=\arcsin(m_2/m_1).$$

Cada ángulo estrictamente entre cero y ese máximo proviene de dos ángulos relativos distintos.

**Demostración.** La componente longitudinal es siempre positiva. Derivar el ángulo de la proposición 19.20 da

$$\frac{d\theta}{d\chi}= \frac{m_2(m_1\cos\chi+m_2)}{m_1^2+m_2^2+2m_1m_2\cos\chi}.$$

El denominador es positivo y el numerador se anula una sola vez, en $\cos\chi=-m_2/m_1$. Antes es positivo y después negativo. La función comienza y termina en cero, así que cada valor interior tiene una preimagen en cada tramo monótono. Sustituir el coseno crítico en las componentes de la proposición 19.20 da $\sin\theta_{\max}=m_2/m_1$. $\square$

Si $m_1<m_2$, el proyectil puede salir hacia atrás: en $\chi=\pi$ su componente longitudinal es negativa. Escribir solamente una tangente borraría esa información. También hay que transformar la medida angular cuando se transforma una sección. En una rama regular axial, $\sin\chi\,d\chi\,d\varphi$ pasa a $\sin\theta\,d\theta\,d\varphi$; las distintas preimágenes deben sumarse. La conservación de energía relativa no hace coincidir los ángulos de ambos marcos.

[]{#fispm-t1-c19-mp0012}

**Principio metodológico 19.12.** Identifica el cuerpo observado y el marco del detector. Transforma primero velocidades; después transforma ángulos y medidas, manteniendo las ramas.

[]{#ejercicios-11}

### 19.12.1. Ejercicios {#fispm-c19-ejercicios-11}

[]{#fispm-t1-c19-e0023}

**Ejercicio 19.23.** Para masas iguales, expresa la sección diferencial de la esfera rígida en el laboratorio para el proyectil.

**Solución.** proposición 19.21 da $\chi=2\theta$, con $0<\theta<\pi/2$. El azimut se conserva y el cociente angular es $\sin(2\theta)2/\sin\theta=4\cos\theta$. Multiplicar la densidad relativa $a^2/4$ da $d\sigma/d\Omega_{\mathrm{lab}}=a^2\cos\theta$. Su integral es $2\pi a^2\int_0^{\pi/2}\cos\theta\sin\theta\,d\theta=\pi a^2$. El evento extremo de proyectil quieto tiene área nula y no recibe una dirección artificial.

[]{#fispm-t1-c19-e0024}

**Ejercicio 19.24.** Sea $m_1=3m_2$. Calcula el máximo ángulo del proyectil y la mayor fracción de energía transferible al blanco.

**Solución.** proposición 19.22 da $\theta_{\max}=\arcsin(1/3)$, aproximadamente $19.47^\circ$. Proposición 19.21 da un coeficiente máximo $4(3)/(4^2)=3/4$, alcanzado en $\chi=\pi$. En ese encuentro frontal el proyectil sigue hacia delante y el blanco recibe el $75\%$ de la energía incidente. El máximo de transferencia y el máximo angular corresponden a preparaciones diferentes.

[]{#de-un-área-a-una-cuenta-de-eventos}

[]{#fispm-t1-c19-s13}

[]{#fpm-i-19-s13}

## 19.13. De un área a una cuenta de eventos {#fispm-c19-de-un-uxe1rea-a-una-cuenta-de-eventos}

Una sección es una propiedad del encuentro y del evento seleccionado. Una cuenta experimental combina esa sección con un flujo, una cantidad de centros y una respuesta instrumental. Mezclar esas cantidades dificulta comparar experimentos.

[]{#fispm-t1-c19-p0023}

**Proposición 19.23 --- Cuenta con aceptación angular.** Sean $N$ centros independientes expuestos al mismo flujo uniforme $j$, sin atenuación ni encuentros múltiples relevantes. Sea $0\leq\eta(\Omega)\leq1$ la probabilidad de registrar un evento en la dirección $\Omega$, y sea $D$ la región angular aceptada. Si el canal tiene densidad angular, la tasa media registrada es

$$\dot N_{\mathrm{reg}}=jN\int_D\eta(\Omega)\frac{d\sigma}{d\Omega}\,d\Omega.$$

**Demostración.** Para un centro, el área de preparaciones que llega a un elemento angular tiene medida $d\sigma$. El flujo produce tasa $j\,d\sigma$. Registrar cada evento con probabilidad $\eta$ multiplica su tasa media por ese factor. Integrar sobre $D$ y sumar las $N$ contribuciones independientes da la expresión. Si existe una contribución concentrada, se integra respecto de la medida $d\sigma$ completa en lugar de usar solo su densidad. $\square$

Un blanco de densidad superficial $n_s$ se aproxima a ese régimen cuando la probabilidad de interacción pertinente es pequeña. La combinación $n_s\sigma$ es adimensional; exigir $n_s\sigma\ll1$ sirve como criterio de dilución para un canal de sección finita. Con fuerzas de largo alcance hace falta especificar qué interacción cuenta y cómo se controla la acumulación de desviaciones pequeñas. Un umbral de detección no elimina automáticamente las otras interacciones del movimiento real.

La física cuántica retomará estas preguntas con otra descripción del estado incidente y de la amplitud de salida. La escala $\hbar/(\mu v_\infty)$ tiene dimensiones de longitud; compararla con las escalas espaciales de la interacción ayuda a plantear cuándo cabe esperar una descripción clásica. Esa comparación es orientativa y no constituye una garantía universal: la coherencia, las condiciones de preparación y la resolución también importan. En el modelo clásico sumamos áreas de preparaciones disjuntas. Más adelante habrá que examinar cuándo las alternativas cuánticas exigen sumar amplitudes antes de obtener probabilidades. El presente capítulo proporciona las magnitudes geométricas con las que se hará esa comparación.

[]{#fispm-t1-c19-mp0013}

**Principio metodológico 19.13.** Separa sección, flujo y eficiencia. Expresa el dominio angular aceptado y las hipótesis de encuentro único antes de convertir una ley de dispersión en una cuenta.

[]{#ejercicios-12}

### 19.13.1. Ejercicios {#fispm-c19-ejercicios-12}

[]{#fispm-t1-c19-e0025}

**Ejercicio 19.25.** Para una esfera rígida, un detector cubre $\chi_1\leq\chi\leq\chi_2$, todo el azimut, y tiene eficiencia constante $\eta_0$. Calcula su tasa para $N$ centros.

**Solución.** La integral angular es $(a^2/4)2\pi\int_{\chi_1}^{\chi_2}\sin\chi\,d\chi=(\pi a^2/2)(\cos\chi_1-\cos\chi_2)$. Por tanto la tasa es $jN\eta_0(\pi a^2/2)(\cos\chi_1-\cos\chi_2)$. Para el intervalo completo y eficiencia uno se recupera $jN\pi a^2$. La fórmula supone el marco relativo o un blanco fijo; para un detector de laboratorio con blanco móvil se requiere §12.

[]{#fispm-t1-c19-e0026}

**Ejercicio 19.26.** Comprueba las dimensiones de la proposición 19.23 y determina qué producto puede medirse si solo se conoce la cuenta y la apertura, pero se desconocen $j$ y $N$.

**Solución.** $d\Omega$ es adimensional, $d\sigma/d\Omega$ tiene dimensión de área, $j$ de inversa de área y tiempo, y $N,\eta$ son adimensionales. La tasa tiene dimensión $T^{-1}$. Si la forma angular de la sección es conocida salvo un coeficiente $C$, la cuenta determina $jNC$ multiplicado por la aceptación y eficiencia conocidas. No determina separadamente $C$, $j$ y $N$. Hace falta una calibración independiente para inferir una sección absoluta.

[]{#qué-puede-recuperarse-de-la-dispersión}

[]{#fispm-t1-c19-s14}

[]{#fpm-i-19-s14}

## 19.14. Qué puede recuperarse de la dispersión {#fispm-c19-quuxe9-puede-recuperarse-de-la-dispersiuxf3n}

Empezamos preparando una distancia transversal y terminamos midiendo una dirección. Entre ambas hay una dinámica radial, un cambio de variables y una selección instrumental. Se puede recorrer parte de ese camino en sentido inverso, siempre que la estructura de las ramas sea conocida.

[]{#fispm-t1-c19-p0024}

**Proposición 19.24 --- Recuperación de una ley monótona desde su sección.** Supongamos que $\chi(b)$ es estrictamente decreciente, que su imagen es $(0,\pi)$, que $b(\chi)\to0$ cuando $\chi\to\pi$, y que hay una sola rama regular. Entonces

$$b(\chi)^2=2\int_\chi^\pi \frac{d\sigma}{d\Omega}(u)\sin u\,du.$$

**Demostración.** proposición 19.11 y $b'<0$ dan $d\sigma/d\Omega=-bb'/\sin\chi$. Así $(b^2)'=-2(d\sigma/d\Omega)\sin\chi$. Integrar de $\chi$ a $\pi$ y usar el límite nulo prueba la fórmula, también como integral impropia cuando sea necesario. $\square$

Recuperar $b(\chi)$ no equivale todavía a recuperar un potencial único. Esa segunda pregunta requiere hipótesis sobre la interacción, datos de energía y un análisis inverso adicional. Si se suman varias ramas, la sección sola tampoco indica cuál contribución pertenece a cada una.

[]{#fispm-t1-c19-p0025}

**Proposición 19.25 --- Intercambio de energía en un marco inercial general.** En un encuentro elástico de dos cuerpos, sea $\Delta\mathbf w=\mathbf w_+-\mathbf w_-$ y sea $\mathbf V$ la velocidad constante del centro de masas en el marco elegido. Entonces

$$\Delta K_1=\mu\mathbf V\cdot\Delta\mathbf w, \qquad \Delta K_2=-\mu\mathbf V\cdot\Delta\mathbf w.$$

**Demostración.** Escribamos $\mathbf v_1=\mathbf V+(m_2/M)\mathbf w$. Al restar las normas al cuadrado antes y después, el término $|\mathbf V|^2$ se cancela y el término proporcional a $|\mathbf w|^2$ también, porque el encuentro es elástico. Queda $\Delta K_1=m_1(m_2/M)\mathbf V\cdot\Delta\mathbf w=\mu\mathbf V\cdot\Delta\mathbf w$. La descomposición del segundo cuerpo cambia el signo del término cruzado y da la segunda igualdad. $\square$

En el marco del centro de masas, $\mathbf V=0$ y cada rapidez asintótica permanece igual. En otros marcos puede haber transferencia entre las energías cinéticas individuales. La suma se conserva en todos ellos. El mismo encuentro ofrece así un ángulo relativo útil para reducir la dinámica y unas energías de laboratorio útiles para describir lo que recibe cada cuerpo.

[]{#fispm-t1-c19-mp0014}

**Principio metodológico 19.14.** Al interpretar datos, explicita qué información se pierde en cada paso: orientación, número de vueltas, identidad de rama, eficiencia o marco. Una inversión solo puede recuperar lo que sus hipótesis vuelven identificable.

[]{#problemas-de-integración}

### 19.14.1. Problemas de integración {#fispm-c19-problemas-de-integraciuxf3n}

[]{#fispm-t1-c19-e0027}

**Ejercicio 19.27.** Aplica proposición 19.24 a una sección constante $C>0$ y determina la ley angular y el radio de contacto equivalente.

**Solución.** La integral da $b^2=2C(1+\cos\chi)=4C\cos^2(\chi/2)$. Como $b\geq0$, $b=2\sqrt C\cos(\chi/2)$. Coincide con la esfera rígida de radio $a=2\sqrt C$. La sección total es $4\pi C=\pi a^2$. Esto recupera una ley de preparación y salida dentro de las hipótesis de la proposición 19.24; no prueba que cualquier sistema con esa sección deba tener una superficie material rígida.

[]{#fispm-t1-c19-e0028}

**Ejercicio 19.28.** Para atracción $U=-\kappa/r$ y superficie absorbente de radio $R$, calcula la sección de trayectorias que regresan al infinito con $\chi\geq\chi_0$, donde $0<\chi_0<\pi$. Define $B=\ell\cot(\chi_0/2)$ y $b_c=\sqrt{R^2+2\ell R}$.

**Solución.** La condición angular de las trayectorias conservativas es $b\leq B$. La superficie absorbe los impactos $b\leq b_c$, con la convención de incluir el contacto. Las trayectorias de regreso aceptadas forman $b_c<b\leq B$ si $B>b_c$. Por tanto $\sigma_{\mathrm{regreso}}=\pi\max(B^2-b_c^2,0)$. No se puede asignar la ley de salida de la hipérbola a una trayectoria truncada por absorción. Los extremos puntuales no alteran el área.

[]{#fispm-t1-c19-e0029}

**Ejercicio 19.29.** Un blanco inicialmente quieto tiene masa $m_2=2m_1$. En un encuentro de ángulo relativo $\chi=2\pi/3$, calcula ambas velocidades finales, el ángulo del proyectil y las fracciones de energía.

**Solución.** proposición 19.20 da $\mathbf v_{1+}=(v/\sqrt3)\mathbf e_y$ y $\mathbf v_{2+}=(v/2)\mathbf e_x-(v\sqrt3/6)\mathbf e_y$. El proyectil sale a $\theta=\pi/2$ y conserva la fracción $1/3$ de su energía inicial. La norma al cuadrado de la velocidad del blanco es $v^2/3$, pero su masa es doble; recibe la fracción $2/3$. El momento final es $m_1\mathbf v_{1+}+2m_1\mathbf v_{2+}=m_1v\mathbf e_x$, y ambas energías suman la incidente. Usar la energía relativa como si fuera toda la energía del laboratorio habría omitido el movimiento del centro de masas.

[]{#fispm-t1-c19-e0030}

**Ejercicio 19.30.** Considera dos encuentros elásticos con el mismo $\Delta\mathbf w$ en marcos relacionados por una velocidad constante $\mathbf u$, de modo que $\mathbf V'=\mathbf V-\mathbf u$. Determina el cambio de la transferencia cinética del primer cuerpo y relaciónalo con su cambio de momento.

**Solución.** proposición 19.25 da $\Delta K_1'=\Delta K_1-\mu\mathbf u\cdot\Delta\mathbf w$. La descomposición de velocidades implica $\Delta\mathbf p_1=m_1(m_2/M)\Delta\mathbf w=\mu\Delta\mathbf w$. Por tanto $\Delta K_1'=\Delta K_1-\mathbf u\cdot\Delta\mathbf p_1$. Para el segundo cuerpo el cambio es opuesto, porque $\Delta\mathbf p_2=-\Delta\mathbf p_1$. La transferencia individual depende del marco; la conservación de la suma es consistente con esa transformación.

La preparación de un encuentro ha permitido enlazar conservación, reducción radial y geometría de medidas. Para pasar al siguiente capítulo cambiaremos una hipótesis que aquí sostuvo toda la descripción: el marco desde el que escribimos las ecuaciones. Un observador acelerado o en rotación introduce términos que deben derivarse de la transformación cinemática antes de interpretarse como fuerzas.

[]{#fispm-c19-notas-y-referencias label="fispm-c19-notas-y-referencias"}

[^1]: La derivación de la dispersión inversa del radio se desarrolla aquí a partir de la reducción de dos cuerpos y la ecuación de Binet del capítulo capítulo 18. Como contraste de convenciones físicas: MIT OpenCourseWare, *Introduction to Applied Nuclear Physics*, capítulo 8, apartado de dispersión de Rutherford, https://ocw.mit.edu/courses/22-02-introduction-to-applied-nuclear-physics-spring-2012/f06e26889dd2332f1664a2df42e00ed4_MIT22_02S12_lec_ch8.pdf . Se emplean en este capítulo la energía relativa y la medida geométrica ordinaria de ángulo sólido.

[^2]: MIT OpenCourseWare, *Experimental Physics I & II*, guía experimental de dispersión de Rutherford, https://ocw.mit.edu/courses/8-13-14-experimental-physics-i-ii-junior-lab-fall-2016-spring-2017/f83bb6ada6c56da065d372126fff731c_MIT8_13-14F16-S17exp15.pdf . Las demostraciones y ejercicios presentes son desarrollos propios; la referencia proporciona contexto experimental para distinguir ley angular, aceptación y cuenta.
