---
title: "Oscilaciones lineales"
subtitle: "Física para matemáticos · Tomo I · Capítulo 23"
author: "A. Peña"
description: "Capítulo 23 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0363
source-id: FISPM-T1-C23
editorial-id: FPM-I-23
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-15
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0362"]
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
---

[Capítulo 22](fisica-para-matematicos-capitulo-22-cuerpo-rigido-dinamica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 24](fisica-para-matematicos-capitulo-24-oscilaciones-acopladas-y-modos-normales.md)

Desplacemos una masa unida a un resorte y soltémosla. Al principio la fuerza la acelera hacia el equilibrio; al llegar allí, la fuerza se anula, pero la masa ya tiene velocidad. La inercia la lleva al otro lado. El regreso comienza cuando el resorte ha detenido ese movimiento y vuelve a acelerarla en sentido contrario. La posición de equilibrio organiza el movimiento sin convertirse por ello en su destino.

La misma alternancia aparece en un péndulo de pequeña amplitud, en una barra que gira sobre un apoyo y en las vibraciones de un instrumento. Las fuerzas y las variables pueden ser diferentes. Cerca de un equilibrio estable no degenerado, una aproximación de primer orden conduce a una ecuación común. Su sencillez permite estudiar con precisión qué información aportan la amplitud, la fase, la energía y el tiempo de decaimiento.

El modelo también muestra cómo una fuerza pequeña puede sostener un movimiento considerable. Para comprenderlo habrá que seguir el trabajo de esa fuerza durante cada ciclo. La resonancia adquiere entonces un significado concreto que depende de lo que se mida: desplazamiento, velocidad o potencia transferida.

Usaremos las leyes de Newton y el estudio de potencial y estabilidad de I10 e I13. Se presupone derivación, integración y ecuaciones diferenciales lineales elementales; las soluciones centrales se obtendrán y comprobarán aquí. Todos los modelos tendrán un solo grado de libertad. El acoplamiento entre varios osciladores corresponde a I24.

[]{#fispm-t1-c23-s01}

[]{#fpm-i-23-s01}

## §1. La fuerza cerca del equilibrio

Sea $q$ una coordenada cartesiana para una partícula de masa constante $m>0$. En ausencia de otras fuerzas, su ecuación es $m\ddot q=-U'(q)$. Un equilibrio $q_*$ satisface $U'(q_*)=0$. Escribir $x=q-q_*$ permite medir las desviaciones desde ese punto.

Supongamos que $U$ es tres veces continuamente diferenciable en un entorno del equilibrio y que $k=U''(q_*)>0$. Taylor da

$$
U'(q_*+x)=kx+R(x),\qquad |R(x)|\le C|x|^2
$$

en un intervalo suficientemente pequeño. La fuerza principal es proporcional al desplazamiento y tiene signo opuesto. Si se retiene ese término, queda

$$
m\ddot x+kx=0.
$$

[]{#fispm-t1-c23-d0001}

**Definición FPM-I-23-D01 — Oscilador armónico y frecuencia natural.** Un oscilador armónico de un grado de libertad satisface la ecuación anterior, con $m,k>0$ constantes. Su frecuencia angular natural es $\omega_0=\sqrt{k/m}$, su período es $T_0=2\pi/\omega_0$ y su frecuencia ordinaria es $f_0=1/T_0$. Los radianes se consideran adimensionales; $\omega_0$ se expresa en $\mathrm{s}^{-1}$ y $f_0$ en hertz.

[]{#fispm-t1-c23-p0001}

**Proposición FPM-I-23-P01 — Orden del error de fuerza.** Bajo las hipótesis anteriores, la diferencia entre la aceleración exacta y la aceleración armónica, evaluadas en una misma posición $x$, tiene módulo a lo sumo $(C/m)|x|^2$. Para $x\ne0$, el cociente entre el error de fuerza y $k|x|$ es a lo sumo $C|x|/k$.

**Demostración.** La ecuación exacta es $\ddot x=-kx/m-R(x)/m$. Restar $-kx/m$ y aplicar la cota del resto prueba la primera afirmación. Dividir $|R(x)|\le C|x|^2$ por $k|x|$ prueba la segunda. $\square$

La cota compara fuerzas en una posición. Para deducir una aproximación de trayectorias en un intervalo temporal hay que controlar también la acumulación del error. Dos movimientos muy próximos durante varios períodos pueden perder sincronía mucho después. Esa distinción será especialmente importante para el péndulo.

Cuando $U''(q_*)=0$, el argumento no produce un resorte de rigidez positiva. El potencial $U(x)=\lambda x^4/4$, con $\lambda>0$, tiene un mínimo estricto y movimientos oscilatorios, pero la ecuación $m\ddot x=-\lambda x^3$ conserva su carácter no lineal por pequeña que sea la amplitud. La estabilidad de I13 admite más casos que el oscilador armónico.

[]{#fispm-t1-c23-s02}

[]{#fpm-i-23-s02}

## §2. Resolver el problema inicial

La ecuación normalizada es $\ddot x+\omega_0^2x=0$. Derivar dos veces un seno o un coseno devuelve la misma función multiplicada por $-\omega_0^2$. Esto sugiere buscar la solución en el espacio generado por ambas funciones.

[]{#fispm-t1-c23-p0002}

**Proposición FPM-I-23-P02 — Solución inicial única.** Para cualesquiera datos reales $x(0)=x_0$ y $\dot x(0)=v_0$, la solución es

$$
x(t)=x_0\cos(\omega_0t)+\frac{v_0}{\omega_0}\sin(\omega_0t).
$$

**Demostración.** La sustitución verifica la ecuación y los datos. Para probar unicidad sin dar por completa nuestra búsqueda trigonométrica, restemos dos soluciones con esos mismos datos. Su diferencia $z$ satisface $\ddot z+\omega_0^2z=0$ y $z(0)=\dot z(0)=0$. Al derivar,

$$
\frac{d}{dt}(\dot z^2+\omega_0^2z^2)
=2\dot z(\ddot z+\omega_0^2z)=0.
$$

La expresión es constante e inicialmente nula. Sus dos sumandos son no negativos, de modo que $z=\dot z=0$ para todo $t$. $\square$

El dato de velocidad tiene tanta importancia como el de posición. Una masa situada en el equilibrio puede permanecer allí o atravesarlo con cualquier rapidez inicial. La ecuación de segundo orden necesita ambos datos porque describe un estado formado por posición y velocidad.

Por ejemplo, para $m=0{,}50\,\mathrm{kg}$ y $k=8\,\mathrm{N/m}$ resulta $\omega_0=4\,\mathrm{s}^{-1}$. Con $x_0=0{,}03\,\mathrm m$ y $v_0=0{,}16\,\mathrm{m/s}$,

$$
x(t)=0{,}03\cos(4t)+0{,}04\sin(4t)\quad\text{metros},
$$

donde el valor numérico de $t$ se introduce en segundos. La rapidez inicial positiva hace crecer la posición durante un primer intervalo, aunque el resorte ya tire hacia el equilibrio.

[]{#fispm-t1-c23-s03}

[]{#fpm-i-23-s03}

## §3. Amplitud y fase

Los dos coeficientes de la solución contienen información que puede reorganizarse geométricamente. Pongamos

$$
A=\sqrt{x_0^2+(v_0/\omega_0)^2}.
$$

Para $A>0$ existe un ángulo $\phi$, determinado módulo $2\pi$, tal que $x_0=A\cos\phi$ y $v_0=-A\omega_0\sin\phi$. La fórmula de adición del coseno transforma la solución en $x(t)=A\cos(\omega_0t+\phi)$.

[]{#fispm-t1-c23-d0002}

**Definición FPM-I-23-D02 — Amplitud y fase.** En una solución armónica no nula escrita como $x(t)=A\cos(\omega_0t+\phi)$, con $A>0$, la amplitud es $A$ y la fase es $\omega_0t+\phi$ módulo $2\pi$. Para la solución nula fijamos $A=0$; su fase carece de determinación física.

La fase inicial se calcula con los dos signos,

$$
\phi=\operatorname{atan2}(-v_0/\omega_0,x_0).
$$

La función $\operatorname{atan2}(y,x)$ designa el argumento del vector $(x,y)$ en un intervalo de longitud $2\pi$. Usar únicamente la tangente pierde la distinción entre cuadrantes y puede invertir el sentido inicial del movimiento.

[]{#fispm-t1-c23-p0003}

**Proposición FPM-I-23-P03 — Cambio del origen temporal.** Si $t=t'+t_*$, la amplitud y la frecuencia permanecen iguales y la fase inicial pasa de $\phi$ a $\phi+\omega_0t_*$, módulo $2\pi$.

**Demostración.** Sustituir $t'+t_*$ en $A\cos(\omega_0t+\phi)$ produce directamente la expresión indicada. $\square$

Por tanto, una fase aislada depende del reloj elegido. La diferencia de fase entre dos movimientos de la misma frecuencia, observados con el mismo reloj, permanece constante. Una diferencia de $\pi$ corresponde a desplazamientos opuestos; una diferencia de $\pi/2$ sitúa el máximo de uno en un cruce por el equilibrio del otro.

[]{#fispm-t1-c23-s04}

[]{#fpm-i-23-s04}

## §4. Energía y geometría del estado

La energía del oscilador, tomando cero de potencial en el equilibrio, es

$$
E=\frac12m\dot x^2+\frac12kx^2.
$$

[]{#fispm-t1-c23-p0004}

**Proposición FPM-I-23-P04 — Conservación y amplitud energética.** La energía permanece constante y vale $E=kA^2/2$. Si $A>0$, la curva recorrida en el plano $(x,v)$ es la elipse

$$
\frac{x^2}{A^2}+\frac{v^2}{\omega_0^2A^2}=1.
$$

**Demostración.** Derivar $E$ da $\dot E=\dot x(m\ddot x+kx)=0$. Sustituir $x=A\cos\theta$ y $v=-A\omega_0\sin\theta$, con $\theta=\omega_0t+\phi$, da $E=kA^2(\cos^2\theta+\sin^2\theta)/2=kA^2/2$. Dividir la identidad energética por ese valor produce la ecuación de la elipse. $\square$

En un extremo $x=\pm A$ la velocidad es cero. En el equilibrio $x=0$ la rapidez es máxima: $|v|=\omega_0A$. La energía permite obtener esos valores sin averiguar en qué instante se alcanzan.

[]{#fispm-t1-c23-p0005}

**Proposición FPM-I-23-P05 — Promedios en un ciclo.** En cualquier intervalo de longitud $T_0$, las energías cinética y potencial medias son ambas $E/2$.

**Demostración.** Las dos energías son $E\sin^2\theta$ y $E\cos^2\theta$. Durante un ciclo, $\theta$ recorre un intervalo de longitud $2\pi$. Las identidades $\sin^2\theta=(1-\cos2\theta)/2$ y $\cos^2\theta=(1+\cos2\theta)/2$ muestran que ambas medias valen $1/2$. $\square$

En las coordenadas $(x,v/\omega_0)$ la elipse se convierte en un círculo. El punto de estado gira uniformemente en sentido horario, pues en $(A,0)$ la aceleración es negativa. Un único valor de posición, en cambio, suele corresponder a dos estados: uno que avanza y otro que regresa.

[]{#fispm-t1-c23-s05}

[]{#fpm-i-23-s05}

## §5. Qué conserva la aproximación armónica

En un resorte vertical ideal, con eje positivo hacia abajo, la ecuación es $m\ddot q=mg-kq$, donde $q$ mide el alargamiento desde la longitud natural. El equilibrio se encuentra en $q_*=mg/k$. Al escribir $x=q-q_*$ queda exactamente $m\ddot x=-kx$. La gravedad uniforme desplaza el equilibrio; el coeficiente de la desviación sigue siendo $k$.

Para un péndulo simple de longitud $\ell$, el balance tangencial da

$$
\ddot\theta+\frac g\ell\sin\theta=0.
$$

Como $|\sin\theta-\theta|\le |\theta|^3/6$, la aproximación de pequeña amplitud es $\ddot\theta+(g/\ell)\theta=0$, con frecuencia $\sqrt{g/\ell}$. La variable es angular; el papel de masa inercial lo cumple $m\ell^2$ si escribimos el balance de torque, y la rigidez angular vale $mg\ell$.

[]{#fispm-t1-c23-p0006}

**Proposición FPM-I-23-P06 — Período exacto del péndulo y primer error.** Para una oscilación del péndulo ideal con amplitud $0<\alpha<\pi$,

$$
T(\alpha)=4\sqrt{\frac\ell g}\int_0^{\pi/2}
\frac{d\psi}{\sqrt{1-\sin^2(\alpha/2)\sin^2\psi}}.
$$

Cuando $\alpha\to0$, $T(\alpha)=T_0[1+\alpha^2/16+O(\alpha^4)]$, donde $T_0=2\pi\sqrt{\ell/g}$ y $\alpha$ se mide en radianes.

**Demostración.** La energía en el extremo es $mg\ell(1-\cos\alpha)$. Igualarla a $m\ell^2\dot\theta^2/2+mg\ell(1-\cos\theta)$ da

$$
\dot\theta^2=\frac{2g}{\ell}(\cos\theta-\cos\alpha).
$$

Un cuarto del período es la integral temporal entre $0$ y $\alpha$. La sustitución $\sin(\theta/2)=s\sin\psi$, con $s=\sin(\alpha/2)$, transforma esa integral en la anunciada. Para $s$ pequeño, Taylor, uniformemente para $0\le\psi\le\pi/2$, da $(1-s^2\sin^2\psi)^{-1/2}=1+s^2\sin^2\psi/2+O(s^4)$. Integrar y usar $s^2=\alpha^2/4+O(\alpha^4)$ produce el coeficiente $1/16$. $\square$

El período real es mayor que $T_0$: el integrando exacto es mayor que uno en el interior. La diferencia de período es pequeña para amplitudes pequeñas, pero se repite en cada ciclo y termina produciendo un desfase apreciable. La aproximación de fuerza y su duración útil son dos cuestiones relacionadas que conviene medir por separado.

[]{#fispm-t1-c23-s06}

[]{#fpm-i-23-s06}

## §6. Una fuerza que disipa energía

Un movimiento real suele perder energía mecánica. En un régimen en que la fuerza resistente es aproximadamente proporcional a la velocidad respecto del medio, escribimos $F_d=-b\dot x$, con $b\ge0$. El medio y el soporte del resorte se suponen en reposo en el marco usado. La ecuación libre es

$$
m\ddot x+b\dot x+kx=0.
$$

[]{#fispm-t1-c23-d0003}

**Definición FPM-I-23-D03 — Parámetros de amortiguamiento.** Definimos $\beta=b/(2m)$ y $\omega_0=\sqrt{k/m}$. El sistema es subamortiguado si $0<\beta<\omega_0$, críticamente amortiguado si $\beta=\omega_0$ y sobreamortiguado si $\beta>\omega_0$. El caso $\beta=0$ es el oscilador conservativo.

[]{#fispm-t1-c23-p0007}

**Proposición FPM-I-23-P07 — Balance disipativo.** Para el oscilador libre con resistencia viscosa,

$$
\dot E=-b\dot x^2,\qquad
E(t)+\int_0^t b\dot x(s)^2\,ds=E(0)\quad(t\ge0).
$$

**Demostración.** Derivar $E$ y sustituir la ecuación deja $\dot x(-b\dot x)$. Integrar entre $0$ y $t$ prueba el balance. $\square$

La energía es no creciente. Eso todavía no demuestra por sí solo que $x$ tienda al equilibrio: una función no creciente puede tender a un valor positivo. Las soluciones explícitas permitirán resolver esa pregunta. También conviene observar que $\dot E=0$ en cada instante de retorno, donde $\dot x=0$. La energía no necesita decrecer a una tasa estrictamente negativa en todos los instantes para perderse a lo largo del movimiento.

La ley viscosa es una hipótesis de modelo. El rozamiento seco depende del signo de la velocidad y requiere otro tratamiento cerca del reposo. Sustituir uno por otro cambia tanto las soluciones como la manera en que se detiene el sistema.

[]{#fispm-t1-c23-s07}

[]{#fpm-i-23-s07}

## §7. Los tres regímenes de retorno

Buscamos soluciones $x=e^{rt}$. Al sustituir, aparece $r^2+2\beta r+\omega_0^2=0$. El discriminante decide la forma del movimiento.

[]{#fispm-t1-c23-p0008}

**Proposición FPM-I-23-P08 — Soluciones libres amortiguadas.** Con datos iniciales $x_0,v_0$:

Si $0\le\beta<\omega_0$ y $\omega_d=\sqrt{\omega_0^2-\beta^2}$,

$$
x(t)=e^{-\beta t}\left[x_0\cos(\omega_dt)
+\frac{v_0+\beta x_0}{\omega_d}\sin(\omega_dt)\right].
$$

Si $\beta=\omega_0$,

$$
x(t)=e^{-\beta t}[x_0+(v_0+\beta x_0)t].
$$

Si $\beta>\omega_0$ y $\gamma=\sqrt{\beta^2-\omega_0^2}$,

$$
x(t)=e^{-\beta t}\left[x_0\cosh(\gamma t)
+\frac{v_0+\beta x_0}{\gamma}\sinh(\gamma t)\right].
$$

**Demostración.** La sustitución $x=e^{-\beta t}y$ reduce la ecuación a $\ddot y+(\omega_0^2-\beta^2)y=0$, con $y(0)=x_0$ y $\dot y(0)=v_0+\beta x_0$. Según el signo del coeficiente, se resuelve con senos y cosenos, funciones afines o exponenciales reales. Las expresiones satisfacen los datos. La unicidad se prueba con el balance energético aplicado a la diferencia de dos soluciones de datos iguales: su energía empieza en cero y no puede aumentar ni hacerse negativa. $\square$

En el caso subamortiguado, cualquier solución no nula cambia de signo repetidamente. Su parte trigonométrica conserva un período $T_d=2\pi/\omega_d$, aunque la solución completa ya no es periódica.

En los casos crítico y sobreamortiguado puede haber un cruce por el equilibrio, según los datos iniciales. Lo que desaparece es la sucesión indefinida de cruces. Para comprobarlo, en el caso crítico basta estudiar el signo del factor afín. En el sobreamortiguado, escribir $x=c_+e^{r_+t}+c_-e^{r_-t}$, con $r_+>r_-$, muestra que la ecuación $x=0$ equivale a $c_+e^{(r_+-r_-)t}+c_-=0$, con a lo sumo una solución si el movimiento no es nulo.

[]{#fispm-t1-c23-p0009}

**Proposición FPM-I-23-P09 — Atracción del equilibrio y cola lenta.** Si $\beta>0$, todas las soluciones libres satisfacen $(x(t),\dot x(t))\to(0,0)$ cuando $t\to\infty$. En el régimen sobreamortiguado, la tasa exponencial más lenta es

$$
r_+=-\beta+\sqrt{\beta^2-\omega_0^2}
=-\frac{\omega_0^2}{\beta+\sqrt{\beta^2-\omega_0^2}}.
$$

**Demostración.** En el régimen subamortiguado, la exponencial decreciente multiplica funciones acotadas. En el crítico, tanto $e^{-\beta t}$ como $te^{-\beta t}$ y sus derivadas tienden a cero. En el sobreamortiguado las dos raíces son negativas porque $\sqrt{\beta^2-\omega_0^2}<\beta$. La identidad para $r_+$ se obtiene racionalizando. $\square$

Cuando $\beta$ es muy grande, $r_+\sim-\omega_0^2/(2\beta)=-k/b$. Una resistencia enorme puede hacer muy lento el retorno. La frase «más amortiguamiento, retorno más rápido» falla en ese régimen. La tasa lenta aparece salvo que los datos anulen exactamente su coeficiente.

[]{#fispm-t1-c23-s08}

[]{#fpm-i-23-s08}

## §8. Medir el decaimiento

En el régimen subamortiguado podemos escribir $x=A_de^{-\beta t}\cos(\omega_dt+\phi_d)$. El factor $A_de^{-\beta t}$ es una envolvente: la curva permanece entre sus valores positivo y negativo. Los extremos reales no ocurren exactamente cuando el coseno vale $\pm1$, porque también varía la exponencial.

Al derivar, la condición de extremo es $\beta\cos\theta+\omega_d\sin\theta=0$. Los máximos positivos consecutivos tienen la misma fase módulo $2\pi$, por lo que están separados por $T_d$.

[]{#fispm-t1-c23-d0004}

**Definición FPM-I-23-D04 — Decremento logarítmico y factor de calidad.** Para máximos positivos consecutivos $X_n,X_{n+1}$, definimos $\delta=\log(X_n/X_{n+1})$. Para $\beta>0$, adoptamos el factor de calidad del modelo $Q=\omega_0/(2\beta)=m\omega_0/b$.

[]{#fispm-t1-c23-p0010}

**Proposición FPM-I-23-P10 — Medición por máximos.** En el régimen subamortiguado,

$$
\delta=\beta T_d,\qquad
\omega_0=\sqrt{\omega_d^2+\beta^2},\qquad
Q=\frac{\sqrt{4\pi^2+\delta^2}}{2\delta}.
$$

**Demostración.** La parte trigonométrica toma el mismo valor en dos máximos positivos consecutivos. Su cociente es por ello $e^{\beta T_d}$, y el logaritmo da la primera igualdad. La definición de $\omega_d$ da la segunda. Sustituir $\omega_d=2\pi/T_d$ y $\beta=\delta/T_d$ en $Q$ prueba la tercera. $\square$

Para $\delta\ll1$, $Q\simeq\pi/\delta$. Esta última relación es aproximada. Tampoco la energía instantánea es, en general, una exponencial pura: $E$ contiene factores periódicos además de $e^{-2\beta t}$. Sí se cumple exactamente

$$
E(t+T_d)=e^{-2\beta T_d}E(t),
$$

pues tanto posición como velocidad se multiplican por $e^{-\beta T_d}$ al avanzar un ciclo de la parte oscilatoria.

[]{#fispm-t1-c23-s09}

[]{#fpm-i-23-s09}

## §9. Una fuerza aplicada y la respuesta causal

Incorporemos una fuerza exterior prescrita $F(t)$:

$$
m\ddot x+b\dot x+kx=F(t).
$$

La ecuación es lineal. Si $x_1,x_2$ responden a $F_1,F_2$, entonces $a_1x_1+a_2x_2$ responde a $a_1F_1+a_2F_2$. Para sumar respuestas con condiciones iniciales hay que sumar también esos datos. Cuando se busca la respuesta de reposo, todas las contribuciones se toman con datos nulos.

[]{#fispm-t1-c23-p0011}

**Proposición FPM-I-23-P11 — Fórmula de respuesta para datos nulos.** Sea $F$ continua y $h$ la solución homogénea con $h(0)=0$, $\dot h(0)=1$. Entonces

$$
x(t)=\frac1m\int_0^t h(t-s)F(s)\,ds
$$

es la solución con $x(0)=\dot x(0)=0$. En el régimen subamortiguado, $h(t)=e^{-\beta t}\sin(\omega_dt)/\omega_d$ para $t\ge0$.

**Demostración.** Derivar la integral una vez no añade término de borde porque $h(0)=0$. Derivarla otra vez añade $\dot h(0)F(t)/m=F(t)/m$. En $\ddot x+2\beta\dot x+\omega_0^2x$, los términos integrales se anulan por la ecuación de $h$. Los datos iniciales son nulos. La unicidad ya probada para diferencias homogéneas completa el argumento. $\square$

La integral acumula respuestas a fuerzas pasadas. En el instante $t$ sólo usa valores de $F(s)$ con $s\le t$. Esta causalidad resulta especialmente útil para una fuerza que se enciende, se apaga o actúa durante un intervalo corto. En los regímenes crítico y sobreamortiguado, las mismas ideas se aplican con $h(t)=te^{-\beta t}$ y $h(t)=e^{-\beta t}\sinh(\gamma t)/\gamma$, respectivamente.

Una fuerza continua por tramos también admite esta fórmula, interpretando las derivadas en cada tramo y manteniendo continuas posición y velocidad en los saltos finitos de la fuerza.

[]{#fispm-t1-c23-s10}

[]{#fpm-i-23-s10}

## §10. Fuerza sinusoidal y desfase

Supongamos $F(t)=F_0\cos(\Omega t)$, con $F_0>0$, $\Omega>0$ y $b>0$. Buscamos una solución particular de la misma frecuencia,

$$
x_s(t)=a\cos(\Omega t)+c\sin(\Omega t).
$$

Sustituir y agrupar senos y cosenos da, poniendo $d=k-m\Omega^2$,

$$
da+b\Omega c=F_0,\qquad dc-b\Omega a=0.
$$

El determinante $D=d^2+b^2\Omega^2$ es positivo. Así,

$$
a=\frac{F_0d}{D},\qquad c=\frac{F_0b\Omega}{D}.
$$

[]{#fispm-t1-c23-d0005}

**Definición FPM-I-23-D05 — Respuesta estacionaria y susceptibilidad.** La respuesta sinusoidal estacionaria es $x_s=A(\Omega)\cos(\Omega t-\vartheta)$, donde

$$
A(\Omega)=\frac{F_0}{\sqrt{(k-m\Omega^2)^2+b^2\Omega^2}},
\qquad
\vartheta=\operatorname{atan2}(b\Omega,k-m\Omega^2)\in(0,\pi).
$$

Con la convención compleja $F(t)=\operatorname{Re}(F_0e^{i\Omega t})$, la susceptibilidad es $\chi(\Omega)=(k-m\Omega^2+ib\Omega)^{-1}$, de modo que $x_s=\operatorname{Re}(\chi F_0e^{i\Omega t})$.

[]{#fispm-t1-c23-p0012}

**Proposición FPM-I-23-P12 — Pérdida de memoria inicial.** Para $b>0$, toda solución con la fuerza sinusoidal indicada satisface $x(t)-x_s(t)\to0$ y $\dot x(t)-\dot x_s(t)\to0$.

**Demostración.** La diferencia satisface la ecuación homogénea amortiguada. P09 asegura su decaimiento para cualesquiera datos iniciales. $\square$

«Estacionaria» significa aquí que el patrón de respuesta se repite y ya no depende de cómo se inició el movimiento. La masa continúa moviéndose y disipando energía.

Cuando $\Omega$ es pequeña, $A\to F_0/k$ y $\vartheta\to0$: el resorte sigue casi estáticamente la fuerza. Cuando $\Omega$ es muy grande, $A\sim F_0/(m\Omega^2)$ y $\vartheta\to\pi$: domina la aceleración. En $\Omega=\omega_0$, la fase es $\pi/2$. Entonces la velocidad, derivada de $A\sin(\omega_0t)$, está en fase con la fuerza.

[]{#fispm-t1-c23-s11}

[]{#fpm-i-23-s11}

## §11. Qué frecuencia maximiza el desplazamiento

La amplitud depende de $\Omega$. Para compararla entre frecuencias fijaremos $m,k,b$ y la amplitud de fuerza $F_0$. Esta última condición importa: si el mecanismo cambia la fuerza al variar la frecuencia, cambia también el problema de optimización.

[]{#fispm-t1-c23-p0013}

**Proposición FPM-I-23-P13 — Pico de desplazamiento.** Si $0<\beta<\omega_0/\sqrt2$, la amplitud estacionaria tiene un máximo único para $\Omega>0$ en

$$
\Omega_r=\sqrt{\omega_0^2-2\beta^2},\qquad
A(\Omega_r)=\frac{F_0}{2m\beta\sqrt{\omega_0^2-\beta^2}}.
$$

Si $\beta\ge\omega_0/\sqrt2$, la amplitud decrece estrictamente para $\Omega>0$ y su supremo es el valor estático $F_0/k$ cuando $\Omega\to0$.

**Demostración.** Maximizar $A$ equivale a minimizar

$$
H(\Omega)=(\omega_0^2-\Omega^2)^2+4\beta^2\Omega^2.
$$

Con $u=\Omega^2\ge0$,

$$
H=u^2+(4\beta^2-2\omega_0^2)u+\omega_0^4.
$$

Es una parábola estrictamente convexa cuyo vértice está en $u=\omega_0^2-2\beta^2$. Si ese valor es positivo, da el mínimo interior; sustituirlo produce $H=4\beta^2(\omega_0^2-\beta^2)$ y la amplitud anunciada. Si es no positivo, $H$ aumenta estrictamente con $u>0$. $\square$

La frecuencia natural $\omega_0$, la frecuencia libre amortiguada $\omega_d$ y la frecuencia del pico $\Omega_r$ son distintas. Para amortiguamiento débil se aproximan, lo que explica que una descripción poco precisa pueda confundirlas sin que un experimento elemental lo revele. Hay incluso sistemas subamortiguados, con $\omega_0/\sqrt2\le\beta<\omega_0$, cuya respuesta libre oscila y cuya curva de desplazamiento carece de un pico interior.

[]{#fispm-t1-c23-s12}

[]{#fpm-i-23-s12}

## §12. Trabajo por ciclo y resonancia de potencia

El balance energético con fuerza exterior es

$$
\dot E=F(t)\dot x-b\dot x^2.
$$

En régimen estacionario, la energía recupera su valor después de un período $T_\Omega=2\pi/\Omega$. Promediar el balance da $\langle F\dot x_s\rangle=b\langle\dot x_s^2\rangle$. La potencia que entrega la fuerza compensa exactamente la disipación media.

[]{#fispm-t1-c23-p0014}

**Proposición FPM-I-23-P14 — Potencia media y máximo.** Con $b>0$ y $F_0$ fijo,

$$
\overline P(\Omega)
=\frac12b\Omega^2 A(\Omega)^2
=\frac{F_0^2b\Omega^2}{2[(k-m\Omega^2)^2+b^2\Omega^2]}.
$$

Para $\Omega>0$ su máximo único se alcanza en $\Omega=\omega_0$ y vale $F_0^2/(2b)$.

**Demostración.** La media de $\dot x_s^2=\Omega^2 A^2\sin^2(\Omega t-\vartheta)$ es $\Omega^2A^2/2$. Para localizar el máximo, divídase numerador y denominador por $\Omega^2$:

$$
\overline P=\frac{F_0^2b}{2[(k/\Omega-m\Omega)^2+b^2]}.
$$

El denominador es mínimo exactamente cuando $k/\Omega=m\Omega$, es decir, cuando $\Omega=\sqrt{k/m}$. $\square$

[]{#fispm-t1-c23-d0006}

**Definición FPM-I-23-D06 — Anchura de media potencia.** Sean $\Omega_-<\omega_0<\Omega_+$ las frecuencias positivas donde $\overline P$ es la mitad de su máximo. Definimos $\Delta\Omega=\Omega_+-\Omega_-$.

[]{#fispm-t1-c23-p0015}

**Proposición FPM-I-23-P15 — Anchura exacta del modelo viscoso.** Se cumple

$$
\Omega_\pm=\sqrt{\omega_0^2+\beta^2}\pm\beta,
\qquad \Delta\Omega=2\beta,
\qquad Q=\frac{\omega_0}{\Delta\Omega}.
$$

**Demostración.** La condición de media potencia equivale a $(k-m\Omega^2)^2=b^2\Omega^2$, o $|\omega_0^2-\Omega^2|=2\beta\Omega$. Resolver las dos cuadráticas y tomar sus raíces positivas da los valores indicados. Restarlos produce $2\beta$ y la definición de $Q$ completa la prueba. $\square$

La igualdad para la anchura es exacta para esta potencia, este amortiguamiento viscoso y esta fuerza de amplitud fija. Si se usa el cuadrado del desplazamiento para definir otra anchura, hay que repetir el cálculo. En un oscilador de calidad alta las curvas se parecen mucho cerca del pico, pero ese parecido no vuelve intercambiables sus definiciones.

[]{#fispm-t1-c23-s13}

[]{#fpm-i-23-s13}

## §13. Resonancia sin disipación y batidos

Para $b=0$ desaparece el mecanismo que borra las condiciones iniciales. Si $\Omega\ne\omega_0$, todavía existe una solución particular sinusoidal, pero el movimiento libre que se le añade permanece indefinidamente. Ya no se obtiene una respuesta única atrayente.

[]{#fispm-t1-c23-p0016}

**Proposición FPM-I-23-P16 — Forzamiento sin disipación desde el reposo.** Con $b=0$, $x(0)=\dot x(0)=0$ y $F=F_0\cos(\Omega t)$,

$$
x(t)=\frac{F_0}{m(\omega_0^2-\Omega^2)}
[\cos(\Omega t)-\cos(\omega_0t)]\quad(\Omega\ne\omega_0).
$$

En resonancia exacta,

$$
x(t)=\frac{F_0}{2m\omega_0}t\sin(\omega_0t).
$$

**Demostración.** Fuera de resonancia, el primer coseno, con su coeficiente, resuelve la ecuación forzada; el segundo cancela la posición inicial sin alterar la fuerza y ambas derivadas iniciales son cero. En resonancia, derivar dos veces $t\sin(\omega_0t)$ da

$$
\left(\frac{d^2}{dt^2}+\omega_0^2\right)
[t\sin(\omega_0t)]=2\omega_0\cos(\omega_0t).
$$

La expresión propuesta satisface la ecuación y los datos. La unicidad prueba ambas fórmulas. $\square$

Para frecuencias cercanas, la identidad

$$
\cos(\Omega t)-\cos(\omega_0t)
=-2\sin\left(\frac{\Omega+\omega_0}{2}t\right)
\sin\left(\frac{\Omega-\omega_0}{2}t\right)
$$

separa una oscilación rápida de una modulación lenta. Los máximos del módulo de la envolvente están separados por $2\pi/|\Omega-\omega_0|$: ése es el período de batido. El signo de la envolvente alterna, lo que equivale a un cambio de fase de $\pi$ de la oscilación rápida.

La fórmula resonante también se recupera tomando $\Omega\to\omega_0$ en la solución de reposo para cada tiempo fijo. Su crecimiento proporcional a $t$ permanece dentro de un modelo ideal de resorte lineal y fuerza prescrita. Un aparato físico termina encontrando disipación, no linealidad, límites del actuador o una amplitud incompatible con la aproximación inicial.

[]{#fispm-t1-c23-s14}

[]{#fpm-i-23-s14}

## §14. Reconstruir el modelo y reconocer sus límites

Un registro de posición puede revelar varios parámetros. La oscilación libre permite medir $T_d$ y $\delta$; de ellos se obtienen $\beta$ y $\omega_0$. Todavía falta una escala de masa para separar $m$, $k$ y $b$: multiplicar los tres por una misma constante deja inalterada la ecuación libre normalizada.

Una fuerza estática conocida aporta otra observación. Si produce un desplazamiento de equilibrio $x_s\ne0$, entonces $k=F_s/x_s$. Después $m=k/\omega_0^2$ y $b=2m\beta$. Cada medición resuelve una indeterminación distinta. Ajustar una curva sin examinar qué parámetros pueden identificarse puede dar una precisión numérica engañosa.

También la excitación necesita una descripción correcta. Si el extremo del resorte se mueve con posición prescrita $y(t)$ y la resistencia viscosa actúa respecto de ese mismo soporte, el balance es

$$
m\ddot x=-k(x-y)-b(\dot x-\dot y).
$$

Con la coordenada relativa $z=x-y$,

$$
m\ddot z+b\dot z+kz=-m\ddot y.
$$

Para $y=Y\cos(\Omega t)$, la amplitud de la fuerza equivalente es $m\Omega^2Y$. Aunque la amplitud del soporte permanezca fija, la fuerza equivalente crece con la frecuencia. Las conclusiones de P13, formuladas con $F_0$ fijo, deben adaptarse antes de usarse en este experimento.

La energía proporciona un control transversal: una resistencia viscosa pasiva siempre aporta $-b\dot x^2$ en el marco en que se ha definido esa resistencia. Un signo contrario señalaría un mecanismo activo o un error en el balance. La fase ofrece otro control: la velocidad estacionaria está en fase con la fuerza en la frecuencia de máxima potencia. Un ajuste que contradiga simultáneamente estos balances exige revisar convenciones y modelo.

En I24, cada masa sentirá fuerzas que dependen también de las posiciones de las otras. Encontrar movimientos en que todas oscilen con una frecuencia común permitirá recuperar ecuaciones escalares como las de este capítulo. La amplitud y la fase pasarán a describir la organización del movimiento colectivo.

## Ejercicios

[]{#fispm-t1-c23-e0001}

### FPM-I-23-E01 — Del resorte al período

Una masa de $2\,\mathrm{kg}$ está unida a un resorte de $18\,\mathrm{N/m}$. Halla frecuencia angular, frecuencia ordinaria y período. Explica qué cambia si la amplitud se duplica en el modelo ideal.

[]{#fispm-t1-c23-e0002}

### FPM-I-23-E02 — Datos con velocidad

Resuelve $\ddot x+9x=0$ con $x(0)=2$ y $\dot x(0)=-3$. Da amplitud y fase con la convención del capítulo.

[]{#fispm-t1-c23-e0003}

### FPM-I-23-E03 — La posición no determina el estado

Construye dos soluciones armónicas de frecuencia $\omega_0$ que pasen por $x=0$ en $t=0$ con velocidades opuestas no nulas. Compara sus energías y fases.

[]{#fispm-t1-c23-e0004}

### FPM-I-23-E04 — Cambiar de reloj

Para $x(t)=A\cos(\omega_0t+\phi)$, con $A>0$, escoge un nuevo origen temporal en un máximo positivo. Escribe la solución con el nuevo reloj.

[]{#fispm-t1-c23-e0005}

### FPM-I-23-E05 — Energía y extremos

Un oscilador tiene $m=1\,\mathrm{kg}$, $k=25\,\mathrm{N/m}$ y $E=0{,}50\,\mathrm J$. Halla su amplitud y su rapidez máxima.

[]{#fispm-t1-c23-e0006}

### FPM-I-23-E06 — Un cociente que exige cuidado

Un argumento divide $m\ddot x=-kx$ por $\dot x$ para obtener una ecuación energética. Diagnostica el problema y construye una prueba válida incluso en los extremos.

[]{#fispm-t1-c23-e0007}

### FPM-I-23-E07 — Cambio del equilibrio vertical

Un resorte vertical ideal soporta una masa $m$ y después otra de masa $4m$. Compara los alargamientos de equilibrio y los períodos, suponiendo que sigue siendo válida la ley de Hooke.

[]{#fispm-t1-c23-e0008}

### FPM-I-23-E08 — Equilibrio degenerado

Para $m\ddot x=-\lambda x^3$, con $\lambda>0$, una oscilación tiene amplitud $A>0$. Deduce mediante energía que su período es proporcional a $1/A$.

[]{#fispm-t1-c23-e0009}

### FPM-I-23-E09 — Error del período del péndulo

Usa P06 para estimar la corrección relativa del período a una amplitud de $0{,}20$ radianes. Distingue estimación asintótica y cota rigurosa.

[]{#fispm-t1-c23-e0010}

### FPM-I-23-E10 — Clasificación dimensional

Sean $m=1\,\mathrm{kg}$ y $k=9\,\mathrm{N/m}$. Clasifica los casos $b=2$, $6$ y $10\,\mathrm{kg/s}$ y calcula las frecuencias o raíces relevantes.

[]{#fispm-t1-c23-e0011}

### FPM-I-23-E11 — Subamortiguado desde un extremo

Resuelve $\ddot x+2\dot x+5x=0$ con $x(0)=1$, $\dot x(0)=0$. Explica por qué el coeficiente del seno no es cero.

[]{#fispm-t1-c23-e0012}

### FPM-I-23-E12 — Cruce en el régimen crítico

Para $\ddot x+4\dot x+4x=0$, $x(0)=1$, determina qué velocidades iniciales producen un cruce por el equilibrio en un tiempo positivo.

[]{#fispm-t1-c23-e0013}

### FPM-I-23-E13 — Modo lento ausente

En $\ddot x+6\dot x+5x=0$, encuentra la relación entre $x_0$ y $v_0$ que elimina el modo más lento. Resuelve para $x_0=1$ bajo esa condición.

[]{#fispm-t1-c23-e0014}

### FPM-I-23-E14 — Inferir amortiguamiento

Los máximos positivos de una oscilación están separados por $2\,\mathrm s$ y cada uno vale el $80\%$ del anterior. Calcula $\beta$, $\omega_d$, $\omega_0$ y $Q$.

[]{#fispm-t1-c23-e0015}

### FPM-I-23-E15 — ¿Energía exponencial exacta?

Refuta la afirmación de que toda energía libre subamortiguada satisface $E(t)=E(0)e^{-2\beta t}$. Usa datos de reposo con desplazamiento no nulo.

[]{#fispm-t1-c23-e0016}

### FPM-I-23-E16 — Encendido de una fuerza constante

Un oscilador subamortiguado parte del reposo en el equilibrio. A partir de $t=0$ actúa una fuerza constante $F_s$. Halla $x(t)$ y su límite.

[]{#fispm-t1-c23-e0017}

### FPM-I-23-E17 — Impulso ideal

Un impulso de magnitud algebraica $J$ actúa en $t=0$ sobre un oscilador en reposo. Modela su efecto como un salto de velocidad $J/m$ y escribe la respuesta subamortiguada posterior. Calcula la energía inmediatamente después.

[]{#fispm-t1-c23-e0018}

### FPM-I-23-E18 — Pulso de duración finita

Con los datos de E16, la fuerza se apaga en $t=\tau>0$. Expresa la respuesta completa usando la respuesta al escalón unitario de fuerza y justifica la continuidad en $\tau$.

[]{#fispm-t1-c23-e0019}

### FPM-I-23-E19 — Resolver amplitud y fase

Para $m=1$, $k=9$, $b=2$, $F_0=4$ y $\Omega=2$ en unidades coherentes, calcula la respuesta estacionaria y su desfase.

[]{#fispm-t1-c23-e0020}

### FPM-I-23-E20 — Una tangente insuficiente

En el sistema de E19 usa $\Omega=4$. Explica qué error produce escoger la fase con la función $\arctan$ de un solo argumento.

[]{#fispm-t1-c23-e0021}

### FPM-I-23-E21 — Oscilar sin pico de desplazamiento

Construye un sistema libre subamortiguado cuya amplitud estacionaria decrezca para toda $\Omega>0$ con $F_0$ fijo. Justifica ambas propiedades.

[]{#fispm-t1-c23-e0022}

### FPM-I-23-E22 — Tres frecuencias

Para $\omega_0=5\,\mathrm{s}^{-1}$ y $\beta=1\,\mathrm{s}^{-1}$, ordena y calcula la frecuencia libre amortiguada, la de máximo desplazamiento y la de máxima potencia.

[]{#fispm-t1-c23-e0023}

### FPM-I-23-E23 — Energía por ciclo

Demuestra que el trabajo de la fuerza en un ciclo estacionario es $W=\pi b\Omega A^2$. Calcula su valor en $\Omega=\omega_0$.

[]{#fispm-t1-c23-e0024}

### FPM-I-23-E24 — Frecuencias de media potencia

Para $\omega_0=10$ y $\beta=1$ en unidades coherentes, calcula $\Omega_-$, $\Omega_+$ y su media geométrica. ¿Está $\omega_0$ en el punto medio aritmético?

[]{#fispm-t1-c23-e0025}

### FPM-I-23-E25 — Resonancia de reposo

Comprueba directamente la solución resonante de P16 y calcula su energía en los instantes $t_n=n\pi/\omega_0$, para enteros $n\ge0$.

[]{#fispm-t1-c23-e0026}

### FPM-I-23-E26 — Batidos audibles

Dos oscilaciones de igual amplitud tienen frecuencias ordinarias $440$ y $442\,\mathrm{Hz}$. Escribe su suma como producto y determina la frecuencia de los máximos del módulo de la envolvente.

[]{#fispm-t1-c23-e0027}

### FPM-I-23-E27 — Identificación incompleta

Demuestra que observar una trayectoria libre, aun exactamente y durante un intervalo arbitrariamente largo, no basta en general para identificar por separado $m$, $b$ y $k$.

[]{#fispm-t1-c23-e0028}

### FPM-I-23-E28 — Identificación con dato estático

Se miden $\beta=0{,}5\,\mathrm{s}^{-1}$ y $\omega_d=\sqrt{15{,}75}\,\mathrm{s}^{-1}$. Una fuerza estática de $8\,\mathrm N$ desplaza el equilibrio $0{,}02\,\mathrm m$. Halla $m$, $k$, $b$ y $Q$.

[]{#fispm-t1-c23-e0029}

### FPM-I-23-E29 — Excitación por el soporte

Para el modelo de soporte móvil de §14, con $y=Y\cos(\Omega t)$ y $b>0$, encuentra la amplitud estacionaria relativa $Z$ y sus límites cuando $\Omega\to0$ y $\Omega\to\infty$.

[]{#fispm-t1-c23-e0030}

### FPM-I-23-E30 — Estabilidad sin pérdida de energía

Demuestra que el equilibrio del oscilador libre sin disipación es estable en el plano posición-velocidad, pero no es asintóticamente estable. Usa la distancia escalada $r(x,v)=\sqrt{x^2+(v/\omega_0)^2}$ y explica su relación con la distancia euclídea.

## Soluciones

### FPM-I-23-E01

Dividir la rigidez por la masa da $\omega_0^2=9\,\mathrm{s}^{-2}$. Por tanto $\omega_0=3\,\mathrm{s}^{-1}$, $T_0=2\pi/3\,\mathrm s$ y $f_0=3/(2\pi)\,\mathrm{Hz}$. La ecuación lineal no contiene la amplitud en su frecuencia. Duplicar $A$ deja $T_0$ igual y multiplica por cuatro la energía $kA^2/2$. Esta conclusión exige conservar el modelo de resorte ideal.

### FPM-I-23-E02

P02 da $x=2\cos3t-\sin3t$. Comparando con $A\cos(3t+\phi)$, obtenemos $A=\sqrt5$, $\cos\phi=2/\sqrt5$ y $\sin\phi=1/\sqrt5$. Puede elegirse $\phi=\arctan(1/2)$, en el primer cuadrante. La derivada inicial es $-3A\sin\phi=-3$, lo que verifica el signo.

### FPM-I-23-E03

Para cualquier $V>0$, tomemos $x_\pm(t)=\pm(V/\omega_0)\sin(\omega_0t)$. Sus velocidades iniciales son $\pm V$ y ambas energías valen $mV^2/2$. Con amplitudes positivas, las fases son $-\pi/2$ y $\pi/2$ módulo $2\pi$. Los estados son distintos aunque compartan posición y energía; sus puntos en la elipse energética están en lados opuestos del eje de posición.

### FPM-I-23-E04

Escogemos $t_*=(2\pi n-\phi)/\omega_0$ para algún entero $n$. Con $t'=t-t_*$ resulta $x=A\cos(\omega_0t'+2\pi n)=A\cos(\omega_0t')$. La velocidad en $t'=0$ es cero y la aceleración es negativa, de modo que se trata de un máximo positivo. La elección de $n$ sólo selecciona cuál de esos máximos inicia el reloj.

### FPM-I-23-E05

En el extremo toda la energía es potencial: $A=\sqrt{2E/k}=0{,}20\,\mathrm m$. En el equilibrio toda es cinética: $v_{\max}=\sqrt{2E/m}=1\,\mathrm{m/s}$. Coincide con $\omega_0A=5\cdot0{,}20$. Las dos vías sirven como comprobación mutua.

### FPM-I-23-E06

La división no está definida en los puntos donde $\dot x=0$, incluidos los extremos de toda oscilación no trivial. La prueba global consiste en multiplicar la ecuación por $\dot x$, sin dividir: $m\ddot x\dot x+kx\dot x=0$. El lado izquierdo es la derivada de $m\dot x^2/2+kx^2/2$. Así la energía se conserva en todo el intervalo, también donde ambos productos se anulan.

### FPM-I-23-E07

El equilibrio satisface $kq_*=mg$, por lo que cuadruplicar la masa cuadruplica el alargamiento. La frecuencia pasa de $\sqrt{k/m}$ a $\sqrt{k/(4m)}=\omega_0/2$; el período se duplica. La gravedad no cambia la frecuencia para una masa dada en este modelo, pero cambiar la masa modifica tanto equilibrio como inercia.

### FPM-I-23-E08

La energía es $m\dot x^2/2+\lambda x^4/4=\lambda A^4/4$. En un cuarto del ciclo,

$$
\frac T4=\sqrt{\frac{2m}{\lambda}}\int_0^A
\frac{dx}{\sqrt{A^4-x^4}}
=\frac1A\sqrt{\frac{2m}{\lambda}}\int_0^1\frac{du}{\sqrt{1-u^4}}.
$$

La sustitución fue $x=Au$. La integral es finita: cerca de $u=1$, $1-u^4$ tiene un cero simple, por lo que la singularidad es del tipo $(1-u)^{-1/2}$, integrable. El factor restante no depende de $A$. Por tanto $T$ es proporcional a $1/A$ y diverge cuando la amplitud tiende a cero. Un mínimo estable degenerado puede tener una dependencia de amplitud muy distinta de la armónica.

### FPM-I-23-E09

El primer término relativo es $\alpha^2/16=0{,}04/16=0{,}0025$, es decir, aproximadamente $0{,}25\%$. P06 deja un resto $O(\alpha^4)$ sin dar una constante numérica explícita. Por ello el resultado es una estimación asintótica; no autoriza afirmar que el error exacto sea menor que $0{,}25\%$. De hecho, los términos positivos de orden superior hacen que la corrección exacta supere ligeramente ese primer término.

### FPM-I-23-E10

La frecuencia natural es $3\,\mathrm{s}^{-1}$. Para $b=2$, $\beta=1$ y $\omega_d=\sqrt8\,\mathrm{s}^{-1}$: caso subamortiguado. Para $b=6$, $\beta=3=\omega_0$: caso crítico y raíz doble $-3\,\mathrm{s}^{-1}$. Para $b=10$, $\beta=5$ y $\gamma=4$: caso sobreamortiguado con raíces $-1$ y $-9\,\mathrm{s}^{-1}$. El parámetro que se compara con $\omega_0$ es $b/(2m)$; comparar directamente $b$ con una frecuencia sería dimensionalmente incorrecto.

### FPM-I-23-E11

Aquí $\beta=1$, $\omega_0=\sqrt5$ y $\omega_d=2$. La solución es $x=e^{-t}(\cos2t+\tfrac12\sin2t)$. Al derivarla en cero aparece $-1+2(1/2)=0$. Si se omitiera el seno, la derivada de la envolvente produciría una velocidad inicial $-1$. La condición de reposo debe imponerse a la solución completa.

### FPM-I-23-E12

La solución crítica es $x=e^{-2t}[1+(v_0+2)t]$. La exponencial siempre es positiva, de modo que un cero positivo exige $v_0+2<0$. Por tanto el cruce ocurre exactamente para $v_0<-2$, en $t_*=-1/(v_0+2)$. Si $v_0=-2$, el movimiento es $e^{-2t}>0$; si $v_0>-2$, el factor afín permanece positivo para $t\ge0$.

### FPM-I-23-E13

Las raíces son $-1$ y $-5$, por lo que $x=ce^{-t}+de^{-5t}$. Los datos satisfacen $c+d=x_0$ y $-c-5d=v_0$. Para eliminar el modo lento se requiere $c=0$, equivalente a $v_0=-5x_0$. Con $x_0=1$, resulta $x=e^{-5t}$. Una perturbación de esa relación reintroduce el modo $e^{-t}$ y cambia el comportamiento dominante a tiempos largos.

### FPM-I-23-E14

El decremento es $\delta=\log(1/0{,}8)=\log1{,}25\approx0{,}22314$. Entonces $\beta=\delta/2\approx0{,}11157\,\mathrm{s}^{-1}$ y $\omega_d=2\pi/2=\pi\,\mathrm{s}^{-1}$. Reconstruimos $\omega_0=\sqrt{\pi^2+\beta^2}\approx3{,}14357\,\mathrm{s}^{-1}$. Finalmente $Q=\omega_0/(2\beta)\approx14{,}09$. La medición usa máximos del mismo signo; tomar extremos alternos cambiaría el intervalo y el decremento.

### FPM-I-23-E15

Con $x_0\ne0$ y $v_0=0$, la energía inicial es positiva y el balance exacto da $\dot E(0)=-bv_0^2=0$. La fórmula propuesta implicaría $\dot E(0)=-2\beta E(0)<0$ si $\beta>0$, contradicción. La relación exponencial es exacta al comparar estados separados por $T_d$ y sirve como descripción de envolvente; no es la ley instantánea general de la energía.

### FPM-I-23-E16

El nuevo equilibrio es $x_s=F_s/k$. La desviación $u=x-x_s$ satisface la ecuación homogénea con $u(0)=-x_s$ y $\dot u(0)=0$. Por P08,

$$
x(t)=\frac{F_s}{k}\left[1-e^{-\beta t}
\left(\cos\omega_dt+\frac\beta{\omega_d}\sin\omega_dt\right)\right].
$$

Si $\beta>0$, el término transitorio tiende a cero y $x\to F_s/k$. Para $\beta=0$, la misma fórmula da $x=(F_s/k)(1-\cos\omega_0t)$, que no converge: el equilibrio se desplaza, pero no hay disipación que atraiga el movimiento hacia él.

### FPM-I-23-E17

Integrar el balance de momento durante un impulso ideal da $m[v(0^+)-v(0^-)]=J$. La posición sigue siendo cero y $v(0^+)=J/m$. Por P08,

$$
x(t)=\frac{J}{m\omega_d}e^{-\beta t}\sin(\omega_dt),\qquad t>0.
$$

La energía inicial posterior es $J^2/(2m)$. Este modelo concentra el impulso en un intervalo cuya duración se desprecia frente al período y al tiempo de amortiguamiento; la evolución posterior vuelve a ser libre.

### FPM-I-23-E18

Sea $S(t)$ la expresión de E16 con $F_s=1$, para $t\ge0$, y fijemos $S(t)=0$ para $t<0$. Entonces $x(t)=F_s[S(t)-S(t-\tau)]$. El primer término enciende la fuerza; el segundo añade un escalón opuesto cuando se apaga. Como $S(0)=S'(0)=0$, introducir el segundo término en $\tau$ no genera saltos de posición ni de velocidad. La aceleración sí cambia en una cantidad $-F_s/m$, coherente con el salto de la fuerza.

### FPM-I-23-E19

Tenemos $d=9-4=5$, $b\Omega=4$ y $D=41$. Así

$$
x_s=\frac{20}{41}\cos2t+\frac{16}{41}\sin2t,
\qquad A=\frac4{\sqrt{41}},\quad
\vartheta=\arctan(4/5)\approx0{,}67474.
$$

La fase está en el primer cuadrante porque ambos componentes que la definen son positivos. Reagrupar como $A\cos(2t-\vartheta)$ reproduce los dos coeficientes y verifica la convención de retraso.

### FPM-I-23-E20

Con $\Omega=4$, $d=9-16=-7$ y $b\Omega=8$. La fase correcta es $\vartheta=\operatorname{atan2}(8,-7)\approx2{,}28963$ radianes, en el segundo cuadrante. Usar $\arctan(8/(-7))$ devuelve un ángulo negativo, separado del correcto por $\pi$. Con amplitud positiva invertiría el signo de toda la respuesta particular. Debe usarse la información de los dos componentes, no sólo su cociente.

### FPM-I-23-E21

Tomemos $m=k=1$ y $b=\sqrt3$, de modo que $\omega_0=1$ y $\beta=\sqrt3/2$. Como $\beta<1$, la frecuencia libre amortiguada es $\omega_d=1/2$ y las soluciones libres no nulas oscilan. Pero $\beta>1/\sqrt2$, así que P13 prueba que la amplitud forzada decrece para toda frecuencia positiva. La oscilación libre y el pico de desplazamiento son propiedades diferentes.

### FPM-I-23-E22

La frecuencia del pico de desplazamiento es $\sqrt{25-2}=\sqrt{23}\approx4{,}79583$. La frecuencia libre amortiguada es $\sqrt{25-1}=\sqrt{24}\approx4{,}89898$. La de máxima potencia es $\omega_0=5$, todas en $\mathrm{s}^{-1}$. Por tanto $\Omega_r<\omega_d<\omega_0$. Las tres se acercan cuando $\beta/\omega_0$ tiende a cero.

### FPM-I-23-E23

En régimen estacionario, el trabajo por ciclo es la potencia media multiplicada por $T_\Omega$. P14 da $W=(b\Omega^2A^2/2)(2\pi/\Omega)=\pi b\Omega A^2$. En $\Omega=\omega_0$, la amplitud es $F_0/(b\omega_0)$ y por tanto $W=\pi F_0^2/(b\omega_0)$. Coincide con la energía disipada durante ese ciclo, porque la energía almacenada vuelve al mismo valor.

### FPM-I-23-E24

Las frecuencias son $\sqrt{101}-1\approx9{,}04988$ y $\sqrt{101}+1\approx11{,}04988$. Su producto es $101-1=100$, de modo que su media geométrica es $10=\omega_0$. Su media aritmética es $\sqrt{101}>10$. Los extremos de media potencia tienen separación exacta $2\beta$, pero no están dispuestos simétricamente alrededor de $\omega_0$ en una escala lineal.

### FPM-I-23-E25

Sea $c=F_0/(2m\omega_0)$. Derivar $x=ct\sin\omega_0t$ da $\dot x=c\sin\omega_0t+c\omega_0t\cos\omega_0t$ y $\ddot x=2c\omega_0\cos\omega_0t-c\omega_0^2t\sin\omega_0t$. Así $m\ddot x+kx=F_0\cos\omega_0t$ y los datos son cero. En $t_n$, $x=0$ y $\dot x=c\omega_0t_n(-1)^n$, por lo que

$$
E(t_n)=\frac{F_0^2t_n^2}{8m}.
$$

Esta sucesión exhibe el crecimiento cuadrático energético del modelo resonante sin disipación.

### FPM-I-23-E26

La suma es

$$
A\cos(2\pi440t)+A\cos(2\pi442t)
=2A\cos(2\pi t)\cos(2\pi441t).
$$

El módulo de la envolvente $2A|\cos2\pi t|$ tiene máximos separados por $0{,}5\,\mathrm s$, por lo que la frecuencia de batido es $2\,\mathrm{Hz}$. El factor firmado $\cos2\pi t$ tiene período de un segundo; su signo negativo representa una inversión de fase de la oscilación rápida, no una amplitud física negativa.

### FPM-I-23-E27

Si $m\ddot x+b\dot x+kx=0$, entonces para todo $c>0$ también $(cm)\ddot x+(cb)\dot x+(ck)x=0$. Los mismos datos iniciales producen la misma trayectoria en una familia infinita de ternas físicas. En el mejor caso la observación determina las razones $b/m$ y $k/m$, pero no una escala común. Algunas trayectorias especiales pueden ofrecer aún menos información; la solución nula, por ejemplo, es compatible con cualquier terna positiva.

### FPM-I-23-E28

Se obtiene $\omega_0^2=\omega_d^2+\beta^2=15{,}75+0{,}25=16\,\mathrm{s}^{-2}$. El dato estático da $k=8/0{,}02=400\,\mathrm{N/m}$. Después $m=k/\omega_0^2=25\,\mathrm{kg}$ y $b=2m\beta=25\,\mathrm{kg/s}$. Por último $Q=\omega_0/(2\beta)=4$. La fuerza estática proporciona la escala de rigidez que faltaba en E27.

### FPM-I-23-E29

La fuerza equivalente de la ecuación relativa es $m\Omega^2Y\cos\Omega t$. Aplicando §10,

$$
\frac ZY=\frac{m\Omega^2}{\sqrt{(k-m\Omega^2)^2+b^2\Omega^2}}.
$$

Para $\Omega\to0$, $Z/Y\sim m\Omega^2/k\to0$: el desplazamiento relativo es pequeño y la masa sigue aproximadamente al soporte. Para $\Omega\to\infty$, dividir por $m\Omega^2$ muestra que $Z/Y\to1$. En ese límite la coordenada relativa tiene fase próxima a $\pi$ respecto de $y$, de modo que $z\simeq-y$ y la posición absoluta $x=y+z$ es pequeña. Las amplitudes relativas y absolutas expresan observaciones distintas.

### FPM-I-23-E30

P04 implica que $r(x(t),v(t))$ es constante. Para cualquier $\varepsilon>0$, un estado con $r(x_0,v_0)<\varepsilon$ permanece dentro de esa misma bola escalada para todo tiempo: el equilibrio es estable. Pero un estado inicial no nulo tiene $r>0$ constante y no converge al origen, de modo que falta atracción y el equilibrio no es asintóticamente estable. Después de fijar unidades para ambos ejes, la norma escalada y la euclídea satisfacen cotas de la forma $c\|(x,v)\|\le r(x,v)\le C\|(x,v)\|$, con $c,C>0$, porque el cambio $(x,v)\mapsto(x,v/\omega_0)$ es lineal e invertible. Por ello expresan la misma noción local de estabilidad. La conservación energética justifica permanencia cerca del equilibrio; la disipación de P09 añade convergencia.

## Notas y lecturas

1. La distinción entre fuerza de rozamiento seco y resistencia proporcional a la velocidad puede contrastarse en David Tong, *Dynamics and Relativity*, §§2.5.1–2.5.3, pp. impresas 31–34. En §2.5.3, su coeficiente de fuerza resistente se denota por $\gamma$ y su tasa de amortiguamiento por $\alpha$. Aquí corresponden a $b$ y $\beta$. [Texto del autor, University of Cambridge](https://www.damtp.cam.ac.uk/user/tong/relativity/dynrel.pdf).
2. Para acompañar el estudio de transitorios y respuesta sinusoidal, el curso de Yen-Jie Lee, *Physics III: Vibrations and Waves*, MIT OpenCourseWare, otoño de 2016, ofrece la lección 3, «Driven Oscillators, Transient Phenomena, Resonance», con materiales de lectura y demostraciones. [Página de la lección](https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/part-i-mechanical-vibrations-and-waves/lecture-3/). Las demostraciones, la secuencia y los ejercicios de este capítulo se desarrollan en el propio texto; estas lecturas permiten ampliar el estudio.
3. El factor $Q$ se ha definido aquí mediante los coeficientes de la ecuación. Su identificación con $\omega_0/\Delta\Omega$ se demuestra en P15 para la potencia media y fuerza de amplitud fija. Las interpretaciones mediante pérdida relativa de energía por ciclo requieren distinguir una pérdida finita de su aproximación de amortiguamiento débil.

---

[Capítulo 22](fisica-para-matematicos-capitulo-22-cuerpo-rigido-dinamica.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 24](fisica-para-matematicos-capitulo-24-oscilaciones-acopladas-y-modos-normales.md)
