---
title: Capítulo 1 — Soluciones desarrolladas
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-13'
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
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C01-SOLUCIONES
source-sha256: 7db738e2eaa047469cfe5a322cefe9f1c256b3ba0506307fbc76abbd6a3c2b5e
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-01.html) · [Ejercicios](capitulo-01-ejercicios.html) · [Soluciones](capitulo-01-soluciones.html) · [Notas históricas](capitulo-01-notas.html)

Estas resoluciones corresponden uno a uno a los [22 enunciados del capítulo](capitulo-01-ejercicios.html). Se usa el criterio de límite, continuidad y operaciones algebraicas de C00; no se emplean como caja negra las reglas generales de derivación de C02.

## A. Comprender la pregunta

### Solución 1.1 (`EDC-C01-SOL-001`)

Para $h\ne0$,

$$
Q_f(3,h)=\frac{(3+h)^2-3^2}h=\frac{6h+h^2}h=6+h.
$$

Por continuidad de la función $h\mapsto6+h$, el límite cuando $h\to0$ es $6$. La tangente pasa por $(3,9)$ y tiene pendiente $6$, de modo que $y=9+6(x-3)$. La expresión original no está definida en $h=0$; cancelar el factor $h$ requiere explícitamente $h\ne0$, y **sólo después** se toma el límite del resultado simplificado.

### Solución 1.2 (`EDC-C01-SOL-002`)

La diferencia de posiciones es

$$
s(t+h)-s(t)=4h-2th-h^2,
$$

así que la velocidad media es $4-2t-h$ metros por segundo. Para $t=2$ es $-h$ y su límite bilateral es $0\,\mathrm{m/s}$: el modelo tiene una detención instantánea en ese instante. Para $t=0$, sólo se permiten $h>0$; el límite de $4-h$ es $4\,\mathrm{m/s}$. Cerca de $t=2$ para tiempos mayores que $2$ la velocidad media en incrementos positivos resulta negativa: la posición del modelo comienza a disminuir. Se calculan desplazamientos con signo, no distancias totales recorridas.

### Solución 1.3 (`EDC-C01-SOL-003`)

No: el punto $1$ no pertenece al dominio $D=\mathbb R\setminus\{1\}$, así que ni $f(1)$ ni el cociente $[f(1+h)-f(1)]/h$ están definidos. Para $x\ne1$,

$$
f(x)=\frac{(x-1)(x+1)}{x-1}=x+1.
$$

La extensión continua natural es $F(x)=x+1$ para todo $x\in\mathbb R$, es decir, $F(1)=2$. Ahora $[F(1+h)-F(1)]/h=h/h=1$ cuando $h\ne0$; por tanto $F'(1)=1$. Este valor pertenece a **la extensión $F$**, no a la función incompleta $f$.

### Solución 1.4 (`EDC-C01-SOL-004`)

En el origen,

$$
Q_f(0,h)=\frac{h^3}{h}=h^2\to0.
$$

La tangente es $y=0$. Si $x<0$, entonces $x^3<0$; si $x>0$, $x^3>0$. Por tanto, la gráfica atraviesa su tangente al pasar por el origen. La definición diferencial utiliza el límite de las pendientes secantes, no la condición global de que los puntos de la gráfica permanezcan a un lado de la recta.

## B. Calcular por definición

### Solución 1.5 (`EDC-C01-SOL-005`)

Desarrollamos algebraicamente:

$$
Q_f(a,h)=\frac{(a+h)^3-a^3}{h}=3a^2+3ah+h^2.
$$

Los términos $3ah$ y $h^2$ tienden a cero, porque $a$ permanece fijo mientras varía el incremento. Resulta $f'(a)=3a^2$. Para obtener el error del modelo lineal $\ell_a(a+h)=a^3+3a^2h$, restamos al desarrollo de la cúbica su valor inicial y el término de primer grado en $h$; queda $R_a(h)=3ah^2+h^3$. Cada término contiene al menos dos factores del incremento, y al compararlo con $|h|$ obtenemos

$$
\frac{|R_a(h)|}{|h|}=|3ah+h^2|\to0,
$$

lo que demuestra que la aproximación es de primer orden.

### Solución 1.6 (`EDC-C01-SOL-006`)

Para $|h|<1$, $2+h>1$, de modo que podemos calcular el valor de la función. Tomando además $h\ne0$,

$$
Q_f(2,h)=\frac{\frac1{2+h}-\frac12}{h}
=-\frac1{2(2+h)}\longrightarrow-\frac14.
$$

La tangente por $(2,1/2)$ es $y=1/2-(x-2)/4$. La condición $|h|<1$ mantiene $2+h\ne0$; además imponemos $h\ne0$ al formar el cociente incremental. Son condiciones distintas: la primera protege el denominador de la función y la segunda permite dividir por el incremento.

### Solución 1.7 (`EDC-C01-SOL-007`)

Como $f(3)=0$, para $h>0$ el cociente es $|h|/h=1$, y para $h<0$ es $-1$. Las derivadas laterales existen pero no coinciden, por lo que $f'(3)$ no existe. Sin embargo, $|f(3+h)-f(3)|=|h|\to0$; la función sí es continua allí. La continuidad controla diferencias de valores, pero la derivabilidad exige controlar diferencias **divididas** por $h$.

### Solución 1.8 (`EDC-C01-SOL-008`)

Para $h\ne0$,

$$
Q_f(0,h)=\frac{h|h|}{h}=|h|\to0.
$$

Luego $f'(0)=0$. Que una función utilice fórmulas distintas en $x<0$ y en $x>0$ no obliga a que sus cocientes laterales den límites diferentes: aquí ambos valen cero.

### Solución 1.9 (`EDC-C01-SOL-009`)

El cociente de $f$ en cero es $Q_f(0,h)=h\sin(1/h)$. Aunque el seno siga oscilando cuando $h$ se acerca a cero, su magnitud permanece acotada: de $|\sin(1/h)|\le1$ obtenemos $|Q_f(0,h)|\le|h|$. El encajonamiento de C00 demuestra por tanto $f'(0)=0$.

Para $g$ se cancela el único factor $h$ y el cociente queda igual a $\sin(1/h)$. Podemos escoger incrementos que obliguen al argumento del seno a tomar siempre uno de dos tipos de ángulos: con $h_n=(\pi/2+2\pi n)^{-1}$ y $k_n=(3\pi/2+2\pi n)^{-1}$ obtenemos valores $1$ y $-1$, respectivamente, mientras $h_n,k_n\to0$. Si el límite del cociente existiera, las dos sucesiones de valores tendrían que converger al mismo número por el criterio secuencial de C00. Como eso es imposible, $g'(0)$ no existe.

## C. Examinar el dominio y las uniones

### Solución 1.10 (`EDC-C01-SOL-010`)

El valor del empalme lo determina la rama derecha: $f(0)=c$. Desde la izquierda los valores se aproximan a $a$, y desde la derecha a $c$, de modo que la continuidad equivale a $a=c$. Esa igualdad elimina el salto al calcular las diferencias: para $h<0$, $Q_f(0,h)=2$, y para $h>0$, $Q_f(0,h)=b$. Los dos límites coinciden si y sólo si $b=2$; junto con $a=c$, son las condiciones de derivabilidad, y entonces $f'(0)=2$.

Si $a\ne c$, el cociente izquierdo conserva el término $2+(a-c)/h$. La parte $(a-c)/h$ no tiene límite finito, porque su numerador es fijo y no nulo mientras el denominador se aproxima a cero. Igualar las pendientes de las dos fórmulas no elimina ese salto.

### Solución 1.11 (`EDC-C01-SOL-011`)

Se cumple $f(0)=0$. Tanto $x^2$ cuando $x\to0^-$ como $kx$ cuando $x\to0^+$ convergen a cero para cualquier $k$; la continuidad es automática. Los cocientes incrementales son $Q_f(0,h)=h$ para $h<0$ y $Q_f(0,h)=k$ para $h>0$. Por tanto, $f'_-(0)=0$ y $f'_+(0)=k$. Existe derivada bilateral si y sólo si $k=0$, caso en que $f'(0)=0$.

### Solución 1.12 (`EDC-C01-SOL-012`)

En el punto de unión, $f(1)=1$. Las expresiones izquierda y derecha tienen límite $1$ cuando $x\to1$, por lo que hay continuidad. Para $h<0$,

$$
Q_f(1,h)=\frac{(1+h)^2-1}{h}=2+h\to2;
$$

para $h>0$, $Q_f(1,h)=[2(1+h)-1-1]/h=2$. Coinciden las derivadas laterales y $f'(1)=2$. Pero el error cuadrático cambia: si $h<0$,

$$
\frac{f(1+h)-f(1)-2h}{h^2}=\frac{h^2}{h^2}=1,
$$

mientras si $h>0$ el mismo cociente es $0$. Los errores de ambos lados son pequeños frente a $|h|$, y por eso producen la misma aproximación **lineal**. Al dividir en cambio por $h^2$, el lado izquierdo conserva un error relativo igual a uno y el derecho da cero. La comparación en una escala más fina revela una diferencia que la aproximación de primer orden no tenía que controlar.

### Solución 1.13 (`EDC-C01-SOL-013`)

Para $x>0$, $f(x)=1$; para $x<0$, $f(x)=-1$, mientras $f(0)=0$. Los límites laterales de la función en cero difieren de $f(0)$, así que no hay continuidad. Además, para $h\ne0$,

$$
\frac{f(h)-f(0)}h=\frac{\operatorname{sgn}(h)}h=\frac1{|h|}.
$$

Esta cantidad no tiene límite real finito cuando $h\to0$. Por el Teorema 1.3, la falta de continuidad ya excluye la derivabilidad. No se atribuye ningún valor al cociente $|x|/x$ en $x=0$.

### Solución 1.14 (`EDC-C01-SOL-014`)

Como $f(0)=0$, el cociente derecho es $\sqrt h/h=1/\sqrt h$ para $h>0$. Elijamos $h_n=1/n^2\to0^+$: entonces $Q_f(0,h_n)=n\to+\infty$. Si existiera un límite lateral finito $L$, por el criterio secuencial todos los cocientes a lo largo de sucesiones $h_n\to0^+$ deberían converger a $L$, contradicción. La función no está definida para incrementos negativos desde cero, por lo que no satisface la hipótesis de punto **interior** exigida a la derivada bilateral.

## D. Detectar afirmaciones falsas

### Solución 1.15 (`EDC-C01-SOL-015`)

Para $f(x)=x^3$ se tiene $f'(0)=0$, así que $y=0$ es tangente en el origen aunque la gráfica la **atraviese**. Además, la recta $y=-x$ comparte **sólo** el origen con la cúbica real: la igualdad $x^3=-x$ implica $x(x^2+1)=0$, cuya única solución real es $x=0$. Esa recta no es tangente diferencial, pues su pendiente es $-1$ y la derivada de la cúbica en cero es $0$. La recta con una sola intersección puede por tanto tener una pendiente equivocada.

También una tangente correcta puede encontrar la curva en otro punto: para $q(x)=x^2(x-1)$, el cociente en cero es $q(h)/h=h(h-1)\to0$, así que $y=0$ es tangente allí, aunque la gráfica vuelve a encontrarla en $x=1$. La pendiente y el error cerca del punto de tangencia se deciden localmente, con independencia de esas otras intersecciones.

### Solución 1.16 (`EDC-C01-SOL-016`)

Tomemos $f(x)=|x|$, continua en todo $\mathbb R$; en particular $|f(h)-f(0)|=|h|\to0$. No obstante, $Q_f(0,h)$ vale $1$ para $h>0$ y $-1$ para $h<0$. Los límites laterales no coinciden, de modo que $f'(0)$ no existe.

### Solución 1.17 (`EDC-C01-SOL-017`)

Sea $f(x)=x^3$. Su derivada en cero es $0$ porque $h^3/h=h^2\to0$. Para todo $h<0$, $f(h)=h^3<0=f(0)$; para todo $h>0$, $f(h)=h^3>0=f(0)$. Por tanto, en cualquier entorno del origen hay valores mayores y menores que el central: cero no es máximo ni mínimo local.

### Solución 1.18 (`EDC-C01-SOL-018`)

Tomemos $f(x)=x-x^2$ y $a=0$. Directamente,

$$
Q_f(0,h)=\frac{h-h^2}{h}=1-h\to1>0.
$$

Pero $f(2)=2-4=-2<0=f(0)$, a pesar de que $2>0$. La afirmación verdadera sólo vale **suficientemente cerca** de $a$: por la Proposición 1.3 existe $\delta>0$ tal que $f(a+h)>f(a)$ para $0<h<\delta$, y $f(a+h)<f(a)$ para $-\delta<h<0$ cuando $f'(a)>0$. En este ejemplo basta $\delta=1$, pues $h(1-h)>0$ cuando $0<h<1$.

## E. Demostrar con precisión

### Solución 1.19 (`EDC-C01-SOL-019`)

Para cada $h\ne0$ suficientemente pequeño,

$$
\frac{|f(a+h)-f(a)-mh|}{|h|}
=\left|\frac{f(a+h)-f(a)}h-m\right|.
$$

El numerador es el error de la recta de pendiente $m$ que pasa por $(a,f(a))$. Dividir su magnitud por $|h|$ equivale, como muestra la igualdad, a medir la distancia entre la pendiente secante y $m$. La expresión de la derecha tiende a cero si y sólo si el cociente incremental tiende a $m$, es decir, si $f'(a)=m$. Para comprobar la unicidad directamente, supongamos que dos pendientes $m,n$ satisfacen la condición. La distancia entre ellas puede controlarse usando una misma pendiente secante como valor intermedio:

$$
|m-n|\le |m-Q_f(a,h)|+|Q_f(a,h)-n|\longrightarrow0,
$$

así que $m=n$.

### Solución 1.20 (`EDC-C01-SOL-020`)

Sea $m=f'(a)$. Las pendientes que se aproximan a un número finito tienen que permanecer acotadas cerca del punto; podemos obtener una cota concreta pidiendo tolerancia uno en la definición. Existe así $\delta>0$, elegida dentro del radio permitido por el dominio, tal que $0<|h|<\delta$ implica $|Q_f(a,h)-m|<1$. La desigualdad triangular da $|Q_f(a,h)|\le|m|+1=:K$. Multiplicamos por $|h|$ y obtenemos $|f(a+h)-f(a)|\le K|h|$, que también vale en $h=0$ porque ambos miembros se anulan.

La cota controla cuánto se separan los valores de $f(a)$, pero sólo exige que las pendientes estén acotadas. La función $f(x)=|x|$ satisface $|f(h)-f(0)|=|h|$ con $K=1$, mientras que sus cocientes toman los valores $1$ y $-1$ a cada lado del origen. Esas pendientes acotadas no convergen a un número común, de modo que la recíproca es falsa.

### Solución 1.21 (`EDC-C01-SOL-021`)

Para cualquier $a,h\in\mathbb R$, $1+a^2\ge1$ y $1+(a+h)^2\ge1$, así que ambos denominadores son estrictamente positivos. Restamos:

$$
\begin{aligned}
\frac{f(a+h)-f(a)}h
&=\frac{1}{h}\left(\frac1{1+(a+h)^2}-\frac1{1+a^2}\right)\\
&=-\frac{(a+h)^2-a^2}{h[1+(a+h)^2](1+a^2)}\\
&=-\frac{2a+h}{[1+(a+h)^2](1+a^2)}.
\end{aligned}
$$

Para $h\ne0$ la cancelación es válida. Al tomar $h\to0$ se obtiene $f'(a)=-2a/(1+a^2)^2$, sin usar la regla del cociente.

## F. Investigar y generalizar

### Solución 1.22 (`EDC-C01-SOL-022`)

La tangente diferencial a $y=x^2$ en el punto de abscisa $a$ es

$$
y=a^2+2a(x-a)=2ax-a^2.
$$

Para que pase por $P=(b,c)$ debe verificarse $c=2ab-a^2$, equivalentemente

$$
a^2-2ba+c=0
\quad\Longleftrightarrow\quad
(a-b)^2=b^2-c.
$$

- Si $c>b^2$, el segundo miembro es negativo: no existe abscisa de tangencia real, luego no hay tangentes por $P$.
- Si $c=b^2$, sólo existe $a=b$, y hay exactamente una tangente, la que pasa por el propio punto de la parábola.
- Si $c<b^2$, hay dos soluciones reales distintas $a=b\pm\sqrt{b^2-c}$ y, por tener pendientes distintas $2a$, dos rectas tangentes diferentes.

El parámetro que buscamos era la abscisa de tangencia, y cada solución determina una recta por su pendiente $2a$. Completar el cuadrado convirtió el número de posibles tangentes en el problema de contar números cuyo cuadrado es $b^2-c$. La clasificación depende de la parábola: la distancia vertical entre su gráfica y la tangente en $a$ es $(x-a)^2$, que sólo se anula en ese punto. Otras curvas pueden atravesar su tangente o volver a encontrarla lejos del punto, como muestran los ejemplos de la solución 1.15.

---

**Control de dependencias.** Las soluciones se apoyan exclusivamente en límites y continuidad de C00 y en las definiciones y propiedades probadas dentro de C01. Cada inciso planteado recibe una respuesta, y los 22 IDs `EDC-C01-SOL-001--022` corresponden a los 22 `EXR-001--022`.
