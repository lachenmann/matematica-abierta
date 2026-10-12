---
title: Capítulo 10 — Soluciones desarrolladas
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
license: GFDL-1.3-or-later
areas:
- calculo
- analisis
- fundamentos
level: intermedio
topics:
- calculo-de-una-variable
- historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
  - role: idea
    note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra
      independiente.'
source-id: EDC-C10-SOLUCIONES
source-sha256: bea9017466aecb98f68602da83b4ccbc8b84f0c8ef1007cf98b6930b80738da1
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

[Exposición](capitulo-10.md) · [Ejercicios](capitulo-10-ejercicios.md) · [Soluciones](capitulo-10-soluciones.md) · [Notas históricas](capitulo-10-notas.md)

Las respuestas corresponden biunívocamente a [los treinta ejercicios de C10](capitulo-10-ejercicios.md). En cada resultado se explicita el intervalo o rama y se diferencia la comprobación de una fórmula de su existencia y unicidad. No se invocan C11 ni teoremas generales de existencia de EDO que no se hayan demostrado.

## A. Interpretar ecuaciones y condiciones iniciales

### Solución 10.1 (`EDC-C10-SOL-001`)

$y'=2t$ es de primer orden, lineal (coeficientes $p=0$, $q=2t$) y no autónoma porque el lado derecho depende explícitamente de $t$. $y'+3y=\cos t$ es de primer orden, lineal inhomogénea y no autónoma. $y'=y^2$ es de primer orden, autónoma y **no lineal** en $y$. $y''+4y=0$ es de segundo orden, lineal homogénea y autónoma si se entiende que no hay dependencia explícita de $t$. Para la última ecuación se requieren en general dos números, $y(t_0)$ e $y'(t_0)$, para seleccionar una solución única dentro de la familia explicitada en el Teorema 10.10. El solo orden de una ecuación no es prueba de existencia global para modelos arbitrarios.

### Solución 10.2 (`EDC-C10-SOL-002`)

Derivamos $y'=-6e^{-3t}$. Entonces $y'+3y=-6e^{-3t}+3(2e^{-3t}+1)=3$. El dato inicial es $y(0)=2+1=3$. Esta sustitución acredita que tenemos **una** solución. Para afirmar unicidad utilizamos el Teorema 10.3 con $p=3$, $q=3$ continuas en $\mathbb R$, o restamos dos soluciones y aplicamos el Teorema 10.2 a $w'=-3w$, $w(0)=0$. Sólo el segundo argumento excluye otras soluciones con el mismo dato.

### Solución 10.3 (`EDC-C10-SOL-003`)

La derivada de $t^2$ es $2t$; por el valor medio, si $y'=2t$, la diferencia $y-t^2$ tiene derivada cero y es una constante $C$ en $\mathbb R$. El dato $y(1)=5$ obliga $1+C=5$, luego $C=4$. Así $y(t)=t^2+4$ para todo real. Equivalentemente, C06 da $y(t)=5+\int_1^t 2s\,ds=5+t^2-1$. El Teorema 10.1 asegura existencia y unicidad.

### Solución 10.4 (`EDC-C10-SOL-004`)

Si $y$ **ya** es una solución $C^1$ y $F$ es continua a lo largo de su gráfica, la regla de Newton–Leibniz produce $y(t)-y(t_0)=\int_{t_0}^t y'(s)ds=\int_{t_0}^tF(s,y(s))ds$. Si una función $C^1$ satisface la identidad, derivar mediante C06 recupera la ecuación. En ambos razonamientos se comienza **suponiendo la disponibilidad de $y$**. No hemos construido $y$ para una función $F(t,y)$ arbitraria; por ello no se obtiene existencia general a partir de reescribir una ecuación en forma integral.

## B. Reconstrucción, crecimiento y coeficientes variables

### Solución 10.5 (`EDC-C10-SOL-005`)

Por el Teorema 10.1,

$$
y(t)=4+\int_0^t(3s^2-2s)ds=4+t^3-t^2.
$$

Su derivada es $3t^2-2t$ y $y(0)=4$. El integrando es polinómico y continuo en toda la recta, de modo que la solución está definida y es única en $\mathbb R$.

### Solución 10.6 (`EDC-C10-SOL-006`)

El Teorema 10.2 con $a=-2$ da $y(t)=7e^{-2t}$. Su derivada vale $-14e^{-2t}=-2y$ y $y(0)=7$. Si $z$ fuese otra solución, $e^{2t}z$ tendría derivada $e^{2t}(z'+2z)=0$, y por el valor medio sería constante e igual a $7$. Así $z=y$ sin dividir por $z$. Como $e^{-2t}\to0$ al crecer $t$, el límite pedido es cero.

### Solución 10.7 (`EDC-C10-SOL-007`)

Integramos $a$: $\int_1^t2s\,ds=t^2-1$. Por el Teorema 10.2,

$$
y(t)=3e^{t^2-1}.
$$

Es positiva en toda la recta y su derivada es $6te^{t^2-1}$, que tiene el signo de $t$. Por tanto decrece estrictamente en $(-\infty,0)$, tiene mínimo en $0$ y crece estrictamente en $(0,\infty)$. El dato en $t=1$ vale $3$. Que $a(t)$ sea negativa antes de cero no implica que la solución sea negativa: el signo de $y$ se conserva.

### Solución 10.8 (`EDC-C10-SOL-008`)

La fórmula $y(t)=0\cdot\exp(\int_{t_0}^t a)=0$ es solución. Para cualquier otra solución $z$, el producto $e^{-A(t)}z(t)$ tiene derivada cero, por el argumento del Teorema 10.2, y en $t_0$ vale cero; de ahí $z\equiv0$. El método informal $y'/y=a(t)$ exigiría $y\ne0$ y **eliminaría precisamente** esta solución. La unicidad evita concluir por error que la rama nula está perdida.

### Solución 10.9 (`EDC-C10-SOL-009`)

La derivada de $\arctan t$ es $1/(1+t^2)$ en toda la recta, y $\arctan0=0$. Por consiguiente,

$$
y(t)=2+\arctan t.
$$

La función está definida para todo $t\in\mathbb R$, es derivable y verifica tanto la ecuación como el dato. El Teorema 10.1 prueba que es la única solución $C^1$ global para este PVI.

## C. Factor integrante y estabilidad

### Solución 10.10 (`EDC-C10-SOL-010`)

Con $p=2$, el factor integrante normalizado es $\mu(t)=e^{2t}$. Multiplicando la ecuación obtenemos $(e^{2t}y)'=3e^{2t}$. Integramos **desde $0$ hasta $t$**:

$$
e^{2t}y(t)-y(0)=3\int_0^t e^{2s}ds=\frac32(e^{2t}-1).
$$

Como $y(0)=1$, resulta $y(t)=\frac32-\frac12e^{-2t}$. Derivando, $y'=e^{-2t}$ y $y'+2y=e^{-2t}+3-e^{-2t}=3$; en cero vale $1$. Los coeficientes son continuos en toda $\mathbb R$, por lo que el Teorema 10.3 aporta unicidad global.

### Solución 10.11 (`EDC-C10-SOL-011`)

El factor es $e^t$. La identidad $(e^ty)'=te^t$ da

$$
e^t y(t)=\int_0^t s e^s ds=[(s-1)e^s]_0^t=(t-1)e^t+1.
$$

Por tanto $y(t)=t-1+e^{-t}$. Su derivada es $1-e^{-t}$; sumando $y$ se obtiene $t$. En cero vale $-1+1=0$. Al tender $t\to\infty$, el término exponencial desaparece y $y(t)=t-1+o(1)$ diverge hacia $+\infty$; no hay equilibrio constante por la fuente $q(t)=t$.

### Solución 10.12 (`EDC-C10-SOL-012`)

Trabajamos sobre $J=(0,\infty)$, donde $p(t)=1/t$ es continua. El factor integrante normalizado en $t_0=1$ es $\mu(t)=e^{\int_1^t ds/s}=e^{\ln t}=t$. Así $(ty)'=t^2$, e integrando de $1$ a $t$,

$$
ty(t)-2=\int_1^t s^2ds=\frac{t^3-1}{3}.
$$

De aquí

$$
\boxed{y(t)=\frac{t^2}{3}+\frac{5}{3t}\qquad(t>0).}
$$

La derivada es $2t/3-5/(3t^2)$, y $y'+y/t=t$. Se verifica $y(1)=1/3+5/3=2$. El coeficiente $1/t$ y la solución obtenida no están definidos en cero; el teorema garantiza unicidad **en $(0,\infty)$**, no en toda la recta.

### Solución 10.13 (`EDC-C10-SOL-013`)

Sean $y$ y $y_p$ soluciones de la misma ecuación con coeficientes continuos en $J$. Su diferencia $w=y-y_p$ satisface $w'+pw=0$. Con $P(t)=\int_{t_0}^t p$, el Teorema 10.2 aplicado a $w$ da $w(t)=w(t_0)e^{-P(t)}$. Así $y=y_p+Ce^{-P}$, con $C=y(t_0)-y_p(t_0)$. Recíprocamente, la suma satisface la ecuación porque $Ce^{-P}$ resuelve la homogénea. Si $y(t_0)=y_0$, sólo cabe $C=y_0-y_p(t_0)$: ese valor selecciona una única curva de la familia.

### Solución 10.14 (`EDC-C10-SOL-014`)

En el intervalo $[0,2]$ vale $p=1$ y $P_*=1$. El Teorema 10.4 con $\eta=1/10$, diferencia inicial a lo sumo $1/5$ y $t-t_0=2$ proporciona

$$
|y_1(2)-y_2(2)|\le e^2\left(\frac15+\frac1{10}\cdot2\right)=\frac{2e^2}{5}.
$$

Es una **cota válida**, no necesariamente óptima. En este caso, como $p=1>0$, el factor exacto también permite una estimación más fina; el ejercicio pide utilizar el teorema general con $|p|\le1$ y por eso basta la expresión anterior.

### Solución 10.15 (`EDC-C10-SOL-015`)

$P(t)=\int_0^t2s\,ds=t^2$, $\mu=e^{t^2}$. La fórmula integral es

$$
y(t)=e^{-t^2}\int_0^t2s e^{s^2}ds=e^{-t^2}(e^{t^2}-1)=1-e^{-t^2}.
$$

Derivamos $y'=2t e^{-t^2}$, mientras $2t y=2t(1-e^{-t^2})$. La suma es $2t$, y $y(0)=0$. Como $p(t)=2t$, $q(t)=2t$ son continuas en toda $\mathbb R$, el Teorema 10.3 garantiza que no hay otra solución con ese dato.

## D. Separación, equilibrios y unicidad

### Solución 10.16 (`EDC-C10-SOL-016`)

En la rama $K=(0,\infty)$ tenemos $b(y)=y^2>0$. Integrar la ecuación dividida por $y^2$ **sólo sobre esa rama** equivale a aplicar $B(y)=\int_1^y dv/v^2=1-1/y$, de modo que

$$
1-\frac1{y(t)}=\int_0^t s\,ds=\frac{t^2}{2}.
$$

Por tanto $y(t)=1/(1-t^2/2)$. La condición $y>0$ y el dato en cero seleccionan el componente $(-\sqrt2,\sqrt2)$. En ese intervalo,

$$
y'(t)=\frac{t}{(1-t^2/2)^2}=t y(t)^2.
$$

La función diverge a $+\infty$ al aproximarse a cualquiera de los dos extremos desde dentro. No admite una prolongación $C^1$ finita que atraviese esos puntos manteniendo el mismo dato y esa rama; existe, no obstante, una fórmula racional en los intervalos exteriores desconectados que **no** prolonga la trayectoria a través de la singularidad.

### Solución 10.17 (`EDC-C10-SOL-017`)

El campo es $b(y)=y(2-y)$; se anula sólo en $y=0$ y $y=2$. Son los equilibrios. Es la ecuación logística con $r=2$, $K=2$, $t_0=0$, $y_0=1$, para la cual $A=2/1-1=1$. Así

$$
y(t)=\frac{2}{1+e^{-2t}}.
$$

En cero vale uno. Derivando,

$$
y'(t)=\frac{4e^{-2t}}{(1+e^{-2t})^2}=y(t)(2-y(t)).
$$

Para $t\ge0$, el valor está entre $1$ y $2$, por lo que $y'>0$: aumenta y tiende a $2$ sin alcanzar ese valor en tiempo finito. La unicidad viene del Teorema 10.6 aplicado al campo polinómico en compactos.

### Solución 10.18 (`EDC-C10-SOL-018`)

La función $a(t)=\cos t$ es continua y su integral desde cero es $\sin t$. El Teorema 10.2 da

$$
y(t)=-2e^{\sin t}\quad(t\in\mathbb R).
$$

Su derivada es $-2e^{\sin t}\cos t=\cos t\,y(t)$ y en cero vale $-2$. La exponencial es estrictamente positiva para cualquier exponente, así que el signo de la solución es siempre negativo; los cambios de signo de $\cos t$ modifican la **dirección de variación**, no hacen cruzar $y=0$.

### Solución 10.19 (`EDC-C10-SOL-019`)

Tomemos $c=0$ y $c=1$ en la familia de la Proposición 10.3:

$$
y_0(t)=\begin{cases}0,&t\le0,\\t^2/4,&t>0,\end{cases}\qquad
 y_1(t)=\begin{cases}0,&t\le1,\\(t-1)^2/4,&t>1.\end{cases}
$$

En el tiempo de partida $c$, la derivada por la izquierda vale cero y la derivada por la derecha $(t-c)/2\to0$, de modo que existe derivada continua igual a cero. Antes de $c$, $y'=\sqrt{|y|}=0$; después, ambas expresiones valen $(t-c)/2$. Ambas cumplen $y(0)=0$, pero por ejemplo $y_0(1)=1/4$ y $y_1(1)=0$; son distintas entre sí y de la trayectoria nula.

### Solución 10.20 (`EDC-C10-SOL-020`)

Restando y factorizando,

$$
\left(u-\frac{u^2}{K}\right)-\left(v-\frac{v^2}{K}\right)
=(u-v)\left(1-\frac{u+v}{K}\right).
$$

Si $|u|,|v|\le M$, entonces $|u+v|\le2M$, y la desigualdad triangular da la cota solicitada. Multiplicando por $r>0$ obtenemos un coeficiente Lipschitz $L=r(1+2M/K)$ para $F(y)=ry(1-y/K)$ en la banda acotada. Como las imágenes de dos soluciones continuas sobre un compacto están acotadas, podemos escoger un $M$ común y aplicar el Teorema 10.6. Esto prueba **unicidad si ambas soluciones ya existen**, no existencia a partir de cualquier campo abstracto.

### Solución 10.21 (`EDC-C10-SOL-021`)

Tenemos $A=K/y_0-1=10/2-1=4$. El Teorema 10.7 da

$$
y(t)=\frac{10}{1+4e^{-2t}},\qquad t\ge0.
$$

La función es positiva, creciente porque comienza entre $0$ y $K$, y $y(t)\to10$. Para hallar el instante con $y=5$:

$$
5=\frac{10}{1+4e^{-2t}}
\iff 4e^{-2t}=1
\iff t=\frac{\ln4}{2}=\ln2.
$$

Los logaritmos están aplicados a números positivos y el tiempo es no negativo, como exige el régimen indicado.

### Solución 10.22 (`EDC-C10-SOL-022`)

Para $y_0=-5$, $K=10$ resulta $A=10/(-5)-1=-3$. La fórmula verificable es

$$
y(t)=\frac{10}{1-3e^{-2t}}.
$$

El denominador se anula cuando $e^{-2t}=1/3$, es decir, en $t_*=(\ln3)/2>0$. Sobre $[0,t_*)$ es negativo y la función satisface la ecuación y el dato $y(0)=10/(1-3)=-5$. Al aproximarse $t\uparrow t_*$, el denominador tiende a cero por valores negativos y $y(t)\to-\infty$. Una función real continua no puede tener ese límite en un tiempo interior de su dominio; no existe prolongación clásica de esa trayectoria a través de $t_*$. El Teorema 10.7 **exigía dato inicial positivo** y no debe aplicarse sin revisar la hipótesis.

## E. Modelos y segundo orden

### Solución 10.23 (`EDC-C10-SOL-023`)

Con $T_a=20$, $T_0=80$, $k=1/2\,\mathrm{h}^{-1}$ y $t_0=0$, el Teorema 10.8 da

$$
T(t)=20+60e^{-t/2}\qquad(t\ge0,\ t\text{ en horas}).
$$

$T=35$ equivale a $15=60e^{-t/2}$, de donde $e^{-t/2}=1/4$ y $t=2\ln4$ horas. El exponente es adimensional porque $(1/2\,\mathrm{h}^{-1})\cdot(t\,\mathrm h)$ carece de unidades. Las cifras son parámetros de un modelo idealizado, no una predicción validada experimentalmente.

### Solución 10.24 (`EDC-C10-SOL-024`)

La ecuación es $T'+T=10+\sin t$, con factor $\mu=e^t$. De $T(0)=0$,

$$
e^tT(t)=\int_0^t e^s(10+\sin s)ds
=10(e^t-1)+\frac{e^t}{2}(\sin t-\cos t)+\frac12.
$$

Así

$$
\boxed{T(t)=10+\frac12(\sin t-\cos t)-\frac{19}{2}e^{-t}.}
$$

En $t=0$, $10-1/2-19/2=0$. Derivando, $T'=\frac12(\cos t+\sin t)+\frac{19}{2}e^{-t}$; al sumar $T$ obtenemos $10+\sin t$. La continuidad de la fuente asegura unicidad global mediante 10.3.

### Solución 10.25 (`EDC-C10-SOL-025`)

La velocidad terminal del modelo es $v_\infty=mg/\gamma=2\cdot10/4=5$ en unidades de velocidad. Además $\gamma/m=4/2=2$ en tiempo inverso. Con $v_0=0$,

$$
v(t)=5(1-e^{-2t}),\qquad t\ge0.
$$

La mitad de la terminal se alcanza cuando $5(1-e^{-2t})=5/2$, equivalente a $e^{-2t}=1/2$, es decir, $t=(\ln2)/2$. Por derivación $v'=10e^{-2t}$ y $mv'=20e^{-2t}=20-4\cdot5(1-e^{-2t})=mg-\gamma v$, confirmando el modelo.

### Solución 10.26 (`EDC-C10-SOL-026`)

$\omega=3$, $x_0=2$ y $v_0=-3$; el Teorema 10.10 da

$$
x(t)=2\cos(3t)-\sin(3t).
$$

Su derivada es $x'=-6\sin(3t)-3\cos(3t)$ y $x''=-18\cos(3t)+9\sin(3t)=-9x$. En cero: $x(0)=2$, $x'(0)=-3$. Para unicidad, si $w$ es diferencia de dos soluciones, $w''+9w=0$ y los datos de $w,w'$ en cero son nulos. La energía $E=(w')^2+9w^2$ cumple $E'=2w'(w''+9w)=0$ y $E(0)=0$; la no negatividad fuerza $w\equiv0$.

### Solución 10.27 (`EDC-C10-SOL-027`)

Sea $E=(x')^2+\omega^2x^2$. Como $x\in C^2$,

$$
E'=2x'x''+2\omega^2xx'=2x'(x''+\omega^2x)=0.
$$

Por el valor medio, $E$ es constante. Si $x(t_0)=x'(t_0)=0$, entonces $E(t_0)=0$, y los dos cuadrados no negativos implican $x(t)=x'(t)=0$ para todo tiempo del intervalo; la solución es nula. Esta prueba explota **una identidad de energía específica** y el signo positivo de $\omega^2$; no proporciona por sí misma un teorema de existencia o unicidad para cualquier EDO de segundo orden.

## F. Diagnóstico fundacional y aproximación

### Solución 10.28 (`EDC-C10-SOL-028`)

Para $y'+2y=3$, $y(0)=1$, la fórmula $y=3/2-(1/2)e^{-2t}$ demuestra existencia sobre toda $\mathbb R$, y el factor integrante prueba unicidad: se verifican las **tres** propiedades. Para $y'=\sqrt{|y|}$, $y(0)=0$, hay soluciones, pero la Proposición 10.3 produce infinitas con el mismo dato; algunas incluso están definidas globalmente. Para $y'=t y^2$, $y(0)=1$, la solución positiva $1/(1-t^2/2)$ existe y es única en su rama sobre $(-\sqrt2,\sqrt2)$, pero su fórmula posee polos en los extremos y no se prolonga como función clásica real finita a través de ellos. La existencia local, la unicidad y la globalidad son propiedades **lógicamente distintas**, no sinónimos.

### Solución 10.29 (`EDC-C10-SOL-029`)

La solución exacta es $y(t)=e^t$ (Teorema 10.2). El paso de Euler desde la posición exacta $y(0)=1$ es $y_E(h)=1+h F(0,1)=1+h$. El error es $e^h-(1+h)$. Taylor–Lagrange de orden uno, entre $0$ y $h>0$, da $e^h=1+h+\frac12e^{\xi}h^2$ para $0<\xi<h$. De aquí

$$
0\le e^h-(1+h)\le\frac12e^h h^2.
$$

El Lema 10.2 también asegura esta cota con $M=e^h$. Pero en un segundo paso el método numérico arranca desde $1+h$, **no** desde el verdadero $e^h$; el error anterior se transmite. Para $N$ pasos sería necesaria una estimación adicional de propagación de errores, ausente de la mera cota local.

### Solución 10.30 (`EDC-C10-SOL-030`)

(a) La ecuación lineal tiene $p=2$ y $q(t)=1+t$. El factor es $e^{2t}$. La fórmula del Teorema 10.3 produce

$$
y(t)=e^{-2t}\left(1+\int_0^t e^{2s}(1+s)ds\right).
$$

Por integración por partes de C07, una primitiva de $e^{2s}(1+s)$ es $e^{2s}(s/2+1/4)$; derivándola se verifica $e^{2s}(1+s)$. Por tanto

$$
\begin{aligned}
\int_0^t e^{2s}(1+s)ds&=e^{2t}(t/2+1/4)-1/4,\\
y(t)&=\boxed{\frac t2+\frac14+\frac34e^{-2t}}.
\end{aligned}
$$

(b) En cero, $y(0)=1/4+3/4=1$. Además $y'=1/2-(3/2)e^{-2t}$ y $y'+2y=[1/2-(3/2)e^{-2t}]+[t+1/2+(3/2)e^{-2t}]=1+t$. Los coeficientes de la EDO son continuos en $\mathbb R$; el Teorema 10.3 da **unicidad global**, no sólo verificación algebraica.

(c) De la expresión exacta, $y'(0)=1/2-3/2=-1$, $y''(t)=3e^{-2t}$ y $y''(0)=3$. Por ello

$$
T_{2,0}y(t)=1-t+\frac32t^2.
$$

(d) La tercera derivada es $y'''(t)=-6e^{-2t}$. Para $0\le t\le1$, $|y'''(t)|\le6$. El Teorema 9.4 de Taylor–Lagrange, aplicado con $n=2$ sobre $[0,t]$, asegura

$$
\left|\frac t2+\frac14+\frac34e^{-2t}-\left(1-t+\frac32t^2\right)\right|
\le\frac{6t^3}{3!}=t^3.
$$

La reconstrucción viene del factor integrante (10.3), la antiderivada y la comprobación de C07 y C02, la unicidad de 10.3, y la cota de C09. No se ha supuesto ninguna teoría general de existencia o unicidad fuera de esta clase lineal.

---

**Control de cobertura:** `EDC-C10-SOL-001--030` corresponde exactamente a `EDC-C10-EXR-001--030`, con intervalos, ramas y pruebas de sustitución cuando proceden.
