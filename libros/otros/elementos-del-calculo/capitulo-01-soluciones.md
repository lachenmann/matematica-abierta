---
title: Capítulo 1 — Soluciones desarrolladas
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
source-id: EDC-C01-SOLUCIONES
source-sha256: 1637f02b26eab9009ddaa86e06c7aff943ab390502c8208eea9fac29b51abacb
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

Los términos $3ah$ y $h^2$ tienden a cero. Resulta $f'(a)=3a^2$. El modelo lineal es $\ell_a(a+h)=a^3+3a^2h$, y su error exacto es $R_a(h)=3ah^2+h^3$. Como

$$
\frac{|R_a(h)|}{|h|}=|3ah+h^2|\to0,
$$

la aproximación es de primer orden.

### Solución 1.6 (`EDC-C01-SOL-006`)

Para $|h|<1$, $2+h>1$, de modo que la división es lícita. Entonces

$$
Q_f(2,h)=\frac{\frac1{2+h}-\frac12}{h}
=-\frac1{2(2+h)}\longrightarrow-\frac14.
$$

La tangente por $(2,1/2)$ es $y=1/2-(x-2)/4$. La elección $|h|<1$ asegura tanto $h\ne0$ (impuesto en el cociente) como $2+h\ne0$.

### Solución 1.7 (`EDC-C01-SOL-007`)

Como $f(3)=0$, para $h>0$ el cociente es $|h|/h=1$, y para $h<0$ es $-1$. Las derivadas laterales existen pero no coinciden, por lo que $f'(3)$ no existe. Sin embargo, $|f(3+h)-f(3)|=|h|\to0$; la función sí es continua allí. La continuidad controla diferencias de valores, pero la derivabilidad exige controlar diferencias **divididas** por $h$.

### Solución 1.8 (`EDC-C01-SOL-008`)

Para $h\ne0$,

$$
Q_f(0,h)=\frac{h|h|}{h}=|h|\to0.
$$

Luego $f'(0)=0$. Que una función utilice fórmulas distintas en $x<0$ y en $x>0$ no obliga a que sus cocientes laterales den límites diferentes: aquí ambos valen cero.

### Solución 1.9 (`EDC-C01-SOL-009`)

El cociente de $f$ en cero es $Q_f(0,h)=h\sin(1/h)$. De $|\sin(1/h)|\le1$ obtenemos $|Q_f(0,h)|\le|h|$, y el encajonamiento de C00 demuestra $f'(0)=0$. Para $g$ el cociente sería $\sin(1/h)$. Con $h_n=(\pi/2+2\pi n)^{-1}$ y $k_n=(3\pi/2+2\pi n)^{-1}$ se obtienen límites parciales $1$ y $-1$ al aproximarse $h_n,k_n\to0$. Por el criterio secuencial de C00 el límite bilateral de $\sin(1/h)$ no existe; por tanto, $g'(0)$ no existe.

## C. Examinar el dominio y las uniones

### Solución 1.10 (`EDC-C01-SOL-010`)

Tenemos $f(0)=c$, mientras el límite por la izquierda vale $a$. La continuidad en cero equivale a $a=c$. Bajo esta igualdad, si $h<0$, $Q_f(0,h)=2$, y si $h>0$, $Q_f(0,h)=b$. La derivabilidad exige y basta que los límites laterales coincidan, esto es, $a=c$ y $b=2$. Entonces $f'(0)=2$. Si $a\ne c$, el cociente izquierdo es $2+(a-c)/h$ y no admite un límite finito; no puede salvarse imponiendo sólo $b=2$.

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

mientras si $h>0$ el mismo cociente es $0$. Tener una misma aproximación **lineal** no asegura una aproximación cuadrática bilateral con el mismo coeficiente.

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

Para $f(x)=x^3$ se tiene $f'(0)=0$, así que $y=0$ es tangente en el origen aunque la gráfica la **atraviese**. Además, la recta $y=-x$ comparte **sólo** el origen con la cúbica real: la igualdad $x^3=-x$ implica $x(x^2+1)=0$, cuya única solución real es $x=0$. Esa recta no es tangente diferencial, pues su pendiente es $-1$ y la derivada de la cúbica en cero es $0$. Por tanto, ni «no cruzar» ni «una sola intersección» sirve como criterio general.

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

La expresión de la derecha tiende a cero si y sólo si el cociente incremental tiende a $m$, que es exactamente $f'(a)=m$. Si dos pendientes $m,n$ satisficieran la condición, entonces por la desigualdad triangular

$$
|m-n|\le |m-Q_f(a,h)|+|Q_f(a,h)-n|\longrightarrow0,
$$

así que $m=n$.

### Solución 1.20 (`EDC-C01-SOL-020`)

Sea $m=f'(a)$. Por definición existe $\delta>0$ tal que, si $0<|h|<\delta$, entonces $|Q_f(a,h)-m|<1$. En consecuencia, $|Q_f(a,h)|\le|m|+1=:K$. Multiplicando por $|h|$, resulta $|f(a+h)-f(a)|\le K|h|$. La desigualdad también se cumple para $h=0$. La recíproca es falsa: $f(x)=|x|$ satisface $|f(h)-f(0)|=|h|$ con $K=1$, pero no es derivable en cero. La estimación es una propiedad de control puntual, no un criterio suficiente para que converjan las pendientes.

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

Esta clasificación pertenece a la parábola y a la definición local utilizada. No prueba que las tangentes a cualquier curva tengan una sola intersección con ella; ya vimos que una tangente a la cúbica atraviesa su curva.

---

**Control de dependencias.** Las soluciones se apoyan exclusivamente en límites y continuidad de C00 y en las definiciones y propiedades probadas dentro de C01. Cada inciso planteado recibe una respuesta, y los 22 IDs `EDC-C01-SOL-001--022` corresponden a los 22 `EXR-001--022`.
