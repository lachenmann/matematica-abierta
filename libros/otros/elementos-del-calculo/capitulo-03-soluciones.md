---
title: Capítulo 3 — Soluciones desarrolladas
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
source-id: EDC-C03-SOLUCIONES
source-sha256: 4783cba0441629cfcf220f136d145c0afad256f8f2d67b0f9691281ab5960463
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-03.html) · [Ejercicios](capitulo-03-ejercicios.html) · [Soluciones](capitulo-03-soluciones.html) · [Notas históricas](capitulo-03-notas.html)

Cada entrada `EDC-C03-SOL-nnn` corresponde al ejercicio `EDC-C03-EXR-nnn`. Las soluciones se apoyan exclusivamente en los capítulos 0–3. Cuando una demostración emplea el teorema del valor medio, se comprueban su continuidad y derivabilidad sobre el intervalo pertinente.

## A. Reconocimiento de hipótesis y conceptos

### Solución 3.1 (`EDC-C03-SOL-001`)

En $[0,2]$, $f(x)=x^2$ es no decreciente, pues $0\le x<y$ implica $x^2<y^2$. Tiene mínimo absoluto $f(0)=0$ y máximo absoluto $f(2)=4$. Aunque el polinomio $x^2$ se extiende a una función derivable sobre toda la recta con $f'(0)=0$, el punto $0$ es **de borde** del dominio aquí estipulado, y Fermat exige un punto interior: no se aplica formalmente por la posición del extremo. La derivada derecha en $0$ es $\lim_{h\to0^+}h^2/h=0$. La coincidencia con cero es accidental respecto del requisito lógico: por ejemplo, para $g(x)=x$ en $[0,2]$ hay un mínimo en $0$ y derivada derecha $1$.

### Solución 3.2 (`EDC-C03-SOL-002`)

Para $f(x)=x^3$, el cociente incremental en $0$ es $h^3/h=h^2\to0$, así que $f'(0)=0$. Pero $f(h)>0$ si $h>0$ y $f(h)<0$ si $h<0$. Por tanto, en cada entorno de $0$ hay valores mayores y menores que $f(0)=0$; no hay extremo local. Fermat afirma la implicación «extremo interior derivable $\Rightarrow f'=0$», no su recíproca.

### Solución 3.3 (`EDC-C03-SOL-003`)

La función valor absoluto es continua en $[-1,1]$ y satisface $f(-1)=f(1)=1$. Su derivada es $-1$ en $(-1,0)$ y $1$ en $(0,1)$; en $0$, los cocientes laterales de derivación valen respectivamente $-1$ y $1$, por lo que no existe derivada bilateral. Falla la segunda hipótesis de Rolle: derivabilidad en **todo** $(a,b)$. No hay ningún punto interior con derivada cero.

### Solución 3.4 (`EDC-C03-SOL-004`)

El seno es continuo en $[0,\pi]$ y derivable en $(0,\pi)$ por C02; además $\sin0=\sin\pi=0$. Rolle garantiza $c\in(0,\pi)$ con $\cos c=0$. Una elección es $c=\pi/2$, que pertenece al intervalo abierto indicado.

## B. Valor medio, extremos e incrementos

### Solución 3.5 (`EDC-C03-SOL-005`)

El polinomio es continuo en $[-1,2]$ y derivable en el interior. La pendiente secante vale

$$
\frac{f(2)-f(-1)}{2-(-1)}=\frac{4-1}{3}=1.
$$

Como $f'(x)=2x$, la ecuación $2c=1$ tiene la solución $c=1/2\in(-1,2)$. El valor medio identifica aquí un único punto, aunque el teorema general no promete unicidad.

### Solución 3.6 (`EDC-C03-SOL-006`)

La función $\ln$ es continua y derivable en un intervalo que contiene $[1,e]$, y $e>1$. La pendiente media es

$$
\frac{\ln e-\ln1}{e-1}=\frac1{e-1}.
$$

Como $(\ln x)'=1/x$, debe cumplirse $1/c=1/(e-1)$, luego $c=e-1$. Justificamos su pertenencia al interior sin decimales: $e>2$ porque $e=\sum_{n\ge0}1/n!>1+1=2$, y $e-1<e$. Por tanto $1<e-1<e$.

### Solución 3.7 (`EDC-C03-SOL-007`)

Tenemos $f'(x)=2x-4$, así que el único candidato estacionario interior es $x=2$. Los valores en los candidatos son

$$
f(-1)=6,\qquad f(2)=-3,\qquad f(5)=6.
$$

La función es continua en el intervalo compacto, por lo que alcanza extremos. Su mínimo absoluto es $-3$ en $2$; su máximo absoluto es $6$, alcanzado en ambos extremos $-1$ y $5$. Resolver $f'=0$ y olvidar los bordes habría omitido el máximo.

### Solución 3.8 (`EDC-C03-SOL-008`)

Si $a=b$ la desigualdad es una identidad. Si $a<b$, seno es continuo en $[a,b]$ y derivable en $(a,b)$, con derivada coseno, obtenida en C02. El valor medio proporciona $c\in(a,b)$ con

$$
\sin b-\sin a=\cos c\,(b-a).
$$

Por $|\cos c|\le1$, se sigue $|\sin b-\sin a|\le b-a$. Si $b<a$, intercambiamos los extremos y el resultado vale con $|b-a|$.

### Solución 3.9 (`EDC-C03-SOL-009`)

Por C02, $f'(x)=3(x-1)(x+1)$. Es positiva en $(-2,-1)$ y $(1,2)$, y negativa en $(-1,1)$. El valor medio implica que $f$ es estrictamente creciente en los dos primeros intervalos y decreciente en el central. Los valores en $-2,-1,1,2$ son, respectivamente, $-2,2,-2,2$. El máximo absoluto es $2$, en $-1$ y $2$; el mínimo absoluto es $-2$, en $-2$ y $1$. La existencia de extremos se garantiza por continuidad en $[-2,2]$.

### Solución 3.10 (`EDC-C03-SOL-010`)

La exponencial construida en C02 es continua en $[0,1]$ y derivable en $(0,1)$, con $(e^x)'=e^x$. Por el valor medio existe $c\in(0,1)$ tal que

$$
e-1=e^1-e^0=e^c(1-0)=e^c.
$$

La exponencial es estrictamente creciente, luego $1=e^0<e^c<e^1=e$. Obtenemos $1<e-1<e$.

## C. Criterios globales y convexidad

### Solución 3.11 (`EDC-C03-SOL-011`)

Tomemos $x<y$ en el intervalo. Por continuidad de una función derivable y por el valor medio aplicado al segmento $[x,y]$ existe $c\in(x,y)$ con

$$
f(y)-f(x)=f'(c)(y-x)=0.
$$

Así $f(x)=f(y)$ para cualquier pareja, y $f$ es constante. La condición de intervalo permite unir **cualquier par de puntos** mediante un segmento contenido en el dominio. En un conjunto desconectado una función puede ser constante en cada componente con valores distintos y tener derivada cero en todos los puntos interiores.

### Solución 3.12 (`EDC-C03-SOL-012`)

Para $x<y$ en $I$, la derivabilidad en $I$ implica continuidad en $[x,y]$ y derivabilidad en $(x,y)$. El valor medio produce $f(y)-f(x)=f'(c)(y-x)>0$ por $f'(c)>0$. Luego $f(y)>f(x)$. No se exige continuidad de $f'$ ni existencia de un límite de $f'$; sólo los valores puntuales positivos de esa derivada y las hipótesis del valor medio.

### Solución 3.13 (`EDC-C03-SOL-013`)

Como $f''\ge0$ en el intervalo abierto $I$, la función $f'$ es no decreciente por el criterio de monotonía. El Teorema 3.6 demuestra que, para cualesquiera $x,y\in I$,

$$
f(y)\ge f(x)+f'(x)(y-x).
$$

El segundo miembro es el valor de la recta tangente a la gráfica en $(x,f(x))$, evaluada en $y$. La comparación vale para todos los puntos **del mismo intervalo $I$**; no autoriza prolongar la conclusión a regiones fuera del dominio o a componentes desconectadas.

### Solución 3.14 (`EDC-C03-SOL-014`)

En $(0,\infty)$, $(\ln x)'=1/x$ y $(\ln x)''=-1/x^2<0$. Así $\ln$ es estrictamente cóncava. Para una función cóncava derivable, la recta tangente queda por encima de la gráfica. Tomando el punto de contacto $x=1$ obtenemos

$$
\ln y\le\ln1+(\ln1)'(y-1)=y-1\qquad(y>0).
$$

Como $\ln$ es estrictamente cóncava, la igualdad sólo ocurre cuando $y=1$.

### Solución 3.15 (`EDC-C03-SOL-015`)

Dado que $f'(x)\ge m>0$, el valor medio muestra que $f$ es estrictamente creciente e inyectiva, por lo cual existe inversa sobre $f(I)$. Sean $u=f(x)$ y $v=f(y)$; si $x<y$, el valor medio aplicado a $[x,y]$ da

$$
v-u=f'(c)(y-x)\ge m(y-x).
$$

Por tanto $0<y-x\le(v-u)/m$. Intercambiando los argumentos cuando sea necesario resulta $|f^{-1}(v)-f^{-1}(u)|\le|v-u|/m$. Este argumento no necesita que exista una fórmula explícita de la inversa.

## D. Contraejemplos y diagnóstico de errores

### Solución 3.16 (`EDC-C03-SOL-016`)

La función polinómica $f(x)=x^3$ satisface $f'(0)=3\cdot0^2=0$. Sin embargo, para todo $\delta>0$ existen $h\in(0,\delta)$ y $-h\in(-\delta,0)$ con $f(-h)<f(0)<f(h)$. No existe ni máximo ni mínimo local en $0$. Se ha confundido una condición necesaria con una suficiente.

### Solución 3.17 (`EDC-C03-SOL-017`)

Sea $f(x)=|x|$ sobre $[-1,1]$. Es continua y $f(-1)=f(1)=1$, pero $f'=-1$ para $x<0$, $f'=1$ para $x>0$ y $f'(0)$ no existe. No hay punto interior con derivada cero. La conclusión de Rolle requiere además **derivabilidad en todo el intervalo abierto**.

### Solución 3.18 (`EDC-C03-SOL-018`)

Definamos $f(x)=0$ para $x\le0$ y $f(x)=x^2$ para $x>0$. Es continua en toda la recta. En $0$,

$$
\frac{f(h)-f(0)}h=
\begin{cases}0,&h<0,\\ h,&h>0,\end{cases}
\longrightarrow0.
$$

Así es derivable con $f'(0)=0$. Para $x<0$, $f'(x)=0$, y para $x>0$, $f'(x)=2x>0$. Por tanto $f'\ge0$ en toda $\mathbb R$, pero $f$ es constante en $(-\infty,0]$ y no es estrictamente creciente.

### Solución 3.19 (`EDC-C03-SOL-019`)

Tomemos $f(x)=x-x^3$. Su derivada es $f'(x)=1-3x^2$, de modo que $f'(0)=1>0$, mientras $f'(1)=-2<0$. No es creciente en toda la recta: en el intervalo $[1,2]$ la derivada es negativa en cada punto, así que $f$ decrece estrictamente allí. La información legítima de $f'(0)>0$ es local: por la definición de límite, para incrementos $h>0$ pequeños, $f(h)>f(0)$, y para $h<0$ pequeños, $f(h)<f(0)$. No se sigue un criterio global de monotonía sin conocer el signo de la derivada en el intervalo completo.

### Solución 3.20 (`EDC-C03-SOL-020`)

La función $f(x)=|x|^{2/3}$ es continua en $[-1,1]$ y no negativa; su mínimo absoluto es $f(0)=0$. Para $h\ne0$,

$$
\frac{f(h)-f(0)}h=\frac{|h|^{2/3}}h
=\operatorname{sgn}(h)|h|^{-1/3},
$$

que no tiene límite real finito al acercarse a cero (tiende a $+\infty$ por la derecha y $-\infty$ por la izquierda). Fermat no se contradice: exige que en el extremo interior exista derivada.

## E. Demostraciones estructurales

### Solución 3.21 (`EDC-C03-SOL-021`)

Definamos

$$
H(x)=(f(b)-f(a))(g(x)-g(a))-(g(b)-g(a))(f(x)-f(a)).
$$

Por las hipótesis, $H$ es continua en $[a,b]$ y derivable en $(a,b)$. Claramente $H(a)=0$; además,

$$
H(b)=(f(b)-f(a))(g(b)-g(a))-(g(b)-g(a))(f(b)-f(a))=0.
$$

Rolle da $c\in(a,b)$ tal que $H'(c)=0$. Derivando con los incrementos extremos como constantes,

$$
(f(b)-f(a))g'(c)-(g(b)-g(a))f'(c)=0,
$$

que es la igualdad pedida. No hemos dividido por $g'(c)$ ni por $g(b)-g(a)$; la formulación conserva sentido aunque alguno sea cero.

### Solución 3.22 (`EDC-C03-SOL-022`)

Para cualesquiera $x,y\in[a,b]$, si $x=y$ la desigualdad es trivial. Si $x<y$, la continuidad en el intervalo cerrado y derivabilidad interior permiten aplicar el valor medio a $[x,y]$:

$$
|f(y)-f(x)|=|f'(c)|\,|y-x|\le K|y-x|.
$$

Si $y<x$ intercambiamos los argumentos. Así se cumple la condición Lipschitz para todo par del intervalo. Es esencial que la cota $K$ sirva en **todos** los puntos interiores, no sólo en alguno.

### Solución 3.23 (`EDC-C03-SOL-023`)

Como $f'(x)\le-m<0$, el valor medio aplicado a cualquier par $x<y$ da $f(y)-f(x)=f'(c)(y-x)\le-m(y-x)<0$. Así $f$ es estrictamente decreciente y posee inversa sobre su imagen. Si $u=f(x)$ y $v=f(y)$, el mismo cálculo produce

$$
|u-v|=|f'(c)|\,|x-y|\ge m|x-y|,
$$

por lo que $|f^{-1}(u)-f^{-1}(v)|\le|u-v|/m$. No importa que $f'$ no sea continua.

### Solución 3.24 (`EDC-C03-SOL-024`)

Si $y>x$, el valor medio da $f(y)-f(x)=f'(c)(y-x)$ con $x<c<y$. Puesto que $f'$ es no decreciente, $f'(c)\ge f'(x)$, y se obtiene la desigualdad de soporte. Si $y<x$, el valor medio da $y<c<x$, con $f'(c)\le f'(x)$; al multiplicar por $y-x<0$, vuelve a salir $f(y)-f(x)\ge f'(x)(y-x)$.

Para $x,y\in I$ y $t\in[0,1]$, fijemos $z=(1-t)x+ty$. Aplicando la desigualdad de soporte desde $z$ hacia ambos extremos,

$$
f(x)\ge f(z)+f'(z)(x-z),\quad
f(y)\ge f(z)+f'(z)(y-z).
$$

Al ponderar la primera por $1-t$ y la segunda por $t$ y sumar, el término lineal desaparece porque $(1-t)(x-z)+t(y-z)=0$. Queda $(1-t)f(x)+tf(y)\ge f(z)$, la convexidad requerida.

### Solución 3.25 (`EDC-C03-SOL-025`)

Por continuidad de $f$ y signos opuestos de $f(a),f(b)$, el teorema del valor intermedio de C00 produce $c\in(a,b)$ con $f(c)=0$. Para $x<y$ en $[a,b]$, el valor medio da $f(y)-f(x)=f'(\xi)(y-x)\le-m(y-x)<0$. La función es estrictamente decreciente y, por ello, inyectiva: dos ceros distintos serían imposibles. Existe **exactamente uno**.

## F. Descubrimiento y optimización

### Solución 3.26 (`EDC-C03-SOL-026`)

Si los lados son $x,y>0$ y el perímetro $P$, entonces $x+y=P/2$ y $y=P/2-x$ exige $0<x<P/2$. El área es $A(x)=x(P/2-x)$, que se extiende continuamente a $[0,P/2]$ con $A=0$ en los dos bordes. Su derivada es $A'(x)=P/2-2x$, positiva para $x<P/4$ y negativa para $x>P/4$. Por el criterio de monotonía, el máximo absoluto ocurre en $x=P/4$, y $y=P/4$: se trata de un cuadrado. El área máxima vale $P^2/16$. Los bordes degenerados de área cero no superan el área positiva del candidato.

### Solución 3.27 (`EDC-C03-SOL-027`)

Para un cilindro cerrado de radio $r>0$ y altura $h>0$,

$$
S=2\pi r^2+2\pi rh,\qquad V=\pi r^2h.
$$

Despejando $h$ obtenemos $h=S/(2\pi r)-r$. La restricción $h>0$ equivale a $0<r<\sqrt{S/(2\pi)}$. Sustituyendo en el volumen,

$$
V(r)=\frac S2r-\pi r^3,
\qquad V'(r)=\frac S2-3\pi r^2.
$$

La derivada cambia de positiva a negativa en $r_*=\sqrt{S/(6\pi)}$, único punto estacionario del dominio. Cuando $r\to0^+$, $V(r)\to0$; cuando $r\to\sqrt{S/(2\pi)}^-$, $V(r)\to0$ porque $h\to0$. El criterio de monotonía demuestra que $r_*$ es el máximo global. Como $S=6\pi r_*^2$,

$$
h_* =\frac S{2\pi r_*}-r_*=3r_*-r_*=2r_*.
$$

La altura óptima es, por tanto, igual al diámetro. El razonamiento utiliza área **total** con las dos tapas; sin tapas, la restricción y la solución serían diferentes.

### Solución 3.28 (`EDC-C03-SOL-028`)

Para $x>0$, la regla del producto y las derivadas de C02 dan

$$
F'(x)=\alpha x^{\alpha-1}e^{-\lambda x}-\lambda x^\alpha e^{-\lambda x}
=x^{\alpha-1}e^{-\lambda x}(\alpha-\lambda x).
$$

El primer factor y la exponencial son positivos; por tanto $F'>0$ para $0<x<\alpha/\lambda$ y $F'<0$ para $x>\alpha/\lambda$. El teorema del valor medio implica crecimiento estricto antes y decrecimiento estricto después del único punto $x_*=\alpha/\lambda$. Es, pues, máximo global de $F$ en $(0,\infty)$, con valor

$$
F(x_*)=\left(\frac\alpha\lambda\right)^\alpha e^{-\alpha}.
$$

No es necesario derivar un límite en infinito para garantizar el máximo: la comparación por monotonía contra $x_*$ cubre ya todo el dominio.

### Solución 3.29 (`EDC-C03-SOL-029`)

El cuadrado de la distancia entre $(0,1)$ y $(x,x^2)$ es

$$
D(x)^2=x^2+(x^2-1)^2=x^4-x^2+1=:G(x).
$$

Minimizar distancia positiva equivale a minimizar $G$. Como $G(x)\to+\infty$ cuando $|x|\to\infty$, existe un mínimo global (por ejemplo, fuera de un intervalo cerrado grande $G(x)>G(0)$, y dentro se aplica valores extremos). Derivando,

$$
G'(x)=4x^3-2x=2x(2x^2-1).
$$

Los puntos estacionarios son $x=0$ y $x=\pm1/\sqrt2$. Sus valores son $G(0)=1$ y $G(\pm1/\sqrt2)=1/4-1/2+1=3/4$. Por tanto la distancia mínima es $\sqrt3/2$, alcanzada exactamente en los puntos

$$
\left(\frac1{\sqrt2},\frac12\right)
\quad\text{y}\quad
\left(-\frac1{\sqrt2},\frac12\right).
$$

El punto estacionario $x=0$ no es mínimo global (de hecho, $G''(0)=-2<0$): una ecuación $G'=0$ no clasifica por sí sola sus raíces.

## G. Desafío de síntesis

### Solución 3.30 (`EDC-C03-SOL-030`)

Si $a=b$, ambos miembros de la desigualdad valen cero. Supongamos $a\ne b$ y, sin perder generalidad en el argumento de valor absoluto, consideremos el segmento con extremos $a$ y $b$. La primera aplicación del valor medio a $f$ da un $c$ estrictamente entre ambos con

$$
f(b)-f(a)=f'(c)(b-a).
$$

Restando $f'(a)(b-a)$ y tomando valores absolutos,

$$
|f(b)-f(a)-f'(a)(b-a)|=|f'(c)-f'(a)|\,|b-a|.
$$

La segunda aplicación del valor medio, esta vez a $f'$ entre $a$ y $c$, da $d$ entre ambos con

$$
|f'(c)-f'(a)|=|f''(d)|\,|c-a|\le M|b-a|.
$$

Al combinar las cotas queda $|f(b)-f(a)-f'(a)(b-a)|\le M|b-a|^2$. No afirmamos que la constante $M$ sea óptima: para $f(x)=x^2$ se tiene $|f''|=2$, pero el error exacto en torno a $a$ es $(b-a)^2$, igual a $M(b-a)^2/2$, estrictamente menor que la cota del ejercicio cuando $a\ne b$. Una estimación óptima sistemática aparecerá al estudiar el resto de Taylor en C09.

---

**Control de cobertura:** treinta ejercicios `EDC-C03-EXR-001--030` desarrollados con sus treinta entradas `EDC-C03-SOL-001--030`. Los problemas se apoyan en C00–C03, sin usar integrales, el Teorema Fundamental del Cálculo ni Taylor.
