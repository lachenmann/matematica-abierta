---
title: Capítulo 9 — Soluciones desarrolladas
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
source-id: EDC-C09-SOLUCIONES
source-sha256: 4dc909ee2b8d9ea34bd9e078f537dcab7c2ebd59d86babc057237dc7442174c3
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-09.html) · [Ejercicios](capitulo-09-ejercicios.html) · [Soluciones](capitulo-09-soluciones.html) · [Notas históricas](capitulo-09-notas.html)

Las soluciones se escriben en correspondencia biunívoca con [los ejercicios de C09](capitulo-09-ejercicios.html). Se distingue el **resto finito** de un límite de restos cuando el orden crece. Se invocan únicamente C00–C09; el Teorema Fundamental, la integral de Darboux y las operaciones locales con series de potencias ya han sido establecidos.

## A. Binomio y series de Newton

### Solución 9.1 (`EDC-C09-SOL-001`)

Para $m=0$ tenemos $(1+x)^0=1=\binom00$. Supongamos demostrada la expansión de orden $m$. Al multiplicar por $1+x$:

$$
(1+x)^{m+1}=\sum_{k=0}^m\binom mkx^k+\sum_{k=1}^{m+1}\binom m{k-1}x^k.
$$

El coeficiente de $x^k$ para $1\le k\le m$ es $\binom mk+\binom m{k-1}=\binom{m+1}k$, por la identidad de Pascal; los coeficientes de $x^0$ y $x^{m+1}$ valen uno. Se obtiene la fórmula para $m+1$. En cada paso sólo hay $m+1$ o $m+2$ sumandos: **no** interviene un límite infinito ni un criterio de convergencia.

### Solución 9.2 (`EDC-C09-SOL-002`)

La definición de coeficientes generalizados proporciona

$$
\binom{1/2}0=1,\quad \binom{1/2}1=\tfrac12,\quad
\binom{1/2}2=-\tfrac18,\quad
\binom{1/2}3=\tfrac1{16},\quad
\binom{1/2}4=-\tfrac5{128}.
$$

Por tanto,

$$
B_4(x)=1+\frac x2-\frac{x^2}{8}+\frac{x^3}{16}-\frac{5x^4}{128}.
$$

El Teorema 9.2 justifica $\sqrt{1+x}=\lim_{N\to\infty}\sum_{n=0}^N\binom{1/2}n x^n$ **para $|x|<1$**. Los coeficientes finitos pueden calcularse para cualquier $x$, pero eso no amplía por sí solo el dominio de la igualdad con la serie.

### Solución 9.3 (`EDC-C09-SOL-003`)

Para $\alpha=-3/2$, todos los factores del numerador de $c_n=\binom\alpha n$ son no nulos. La recurrencia da $c_{n+1}/c_n=(\alpha-n)/(n+1)$, y para $x\ne0$,

$$
\left|\frac{c_{n+1}x^{n+1}}{c_nx^n}\right|
=|x|\frac{n+3/2}{n+1}\longrightarrow |x|.
$$

El criterio de razón da convergencia absoluta para $|x|<1$ y divergencia para $|x|>1$; en el centro sólo queda el término constante uno. El radio es exactamente uno.

El Teorema 9.2 identifica la suma mediante $(1+x)F'=-\frac32F$ y $F(0)=1$. Derivar $(1+x)^{3/2}F(x)$ da cero en $(-1,1)$ y el valor medio la hace constante, de valor uno. Por tanto $F(x)=(1+x)^{-3/2}$ allí.

El radio no decide por sí solo $x=-1$, pero podemos examinarlo directamente. Los módulos de los términos en ese punto son $|c_n|$ y su cociente $(n+3/2)/(n+1)$ es mayor que uno para todo $n\ge0$. Parten de $|c_0|=1$ y no disminuyen, así que no tienden a cero. La serie diverge en ese extremo, de acuerdo con que la potencia negativa tampoco tiene un valor real finito allí.

### Solución 9.4 (`EDC-C09-SOL-004`)

Para $\alpha=-2$,

$$
\binom{-2}{n}=\frac{(-2)(-3)\cdots(-(n+1))}{n!}=(-1)^n(n+1).
$$

La recurrencia se verifica ya que $(n+1)c_{n+1}=(-2-n)c_n$. El Teorema 9.2 produce $(1+x)^{-2}=\sum_{n\ge0}(-1)^n(n+1)x^n$ para $|x|<1$. De modo equivalente, derivar la serie geométrica $\sum_{n\ge0}(-x)^n=(1+x)^{-1}$ dentro de su radio según C08, y cambiar el signo, reproduce la fórmula. Fuera del interior no se han autorizado derivaciones término a término.

### Solución 9.5 (`EDC-C09-SOL-005`)

Si $\alpha=3$, $\binom3n=0$ para $n>3$ y obtenemos $(1+x)^3=1+3x+3x^2+x^3$ para **todo** real: una suma finita no posee restricción de radio. Para $\alpha=1/2$, los coeficientes nunca se anulan y el criterio de razón fija radio uno. En $x=-1$, la base $1+x$ vale cero y la expresión $\sqrt{1+x}$ tiene sentido, pero el Teorema 9.2 sólo demostró coincidencia para $|x|<1$. Para concluir igualdad en $x=-1$ sería preciso un argumento adicional que justifique convergencia y valor en el borde, no sólo la continuidad de la raíz.

### Solución 9.6 (`EDC-C09-SOL-006`)

La recurrencia $(n+1)c_{n+1}=(\alpha-n)c_n$ permite comparar los coeficientes de $F'$ y de $xF'$. En $|x|<1$, las operaciones están justificadas por C08; para un exponente entero no negativo la serie termina y las mismas cuentas son finitas. Obtenemos

$$
\begin{aligned}
(1+x)F'&=\sum_{n\ge0}(n+1)c_{n+1}x^n
+\sum_{n\ge1}n c_nx^n\\
&=\sum_{n\ge0}\alpha c_nx^n=\alpha F.
\end{aligned}
$$

El término constante de la segunda suma es cero, y la recurrencia reúne ambos coeficientes para cada grado. La evaluación en el centro da $F(0)=c_0=1$.

Para reconocer la función sumada la comparamos con la potencia positiva $(1+x)^\alpha$, que no se anula en el intervalo. La diferencia de sus ritmos de cambio se cancela al derivar el cociente, escrito como producto:

$$
\frac{d}{dx}\left((1+x)^{-\alpha}F(x)\right)=0.
$$

El valor medio de C03 demuestra que ese producto es constante. En cero vale uno; por tanto $F(x)=(1+x)^\alpha$ en $(-1,1)$. El argumento usa una identidad de derivadas y un valor inicial, sin un teorema general de ecuaciones diferenciales de C10.

## B. Datos y polinomios locales

### Solución 9.7 (`EDC-C09-SOL-007`)

Las derivadas de $e^x$ de cualquier orden son $e^x$; en cero valen uno. En consecuencia,

$$
T_{2,0}(e^x)=1+x+\frac{x^2}{2}.
$$

El valor del polinomio en cero es $1$, su primera derivada $1+x$ vale $1$ en cero y su segunda derivada es $1$. Coinciden con los tres datos de $e^x$. Esta coincidencia no implica que $e^x$ sea el mismo polinomio para $x\ne0$.

### Solución 9.8 (`EDC-C09-SOL-008`)

Las derivadas de seno en cero, desde orden cero hasta cuatro, son $0,1,0,-1,0$. Por ello

$$
T_{4,0}(\sin x)=x-\frac{x^3}{6}.
$$

No aparece $x^4$ porque $f^{(4)}(0)=\sin0=0$. El nombre «de orden cuatro» indica que se han emparejado derivadas hasta ese orden, no que el polinomio tenga forzosamente grado cuatro.

### Solución 9.9 (`EDC-C09-SOL-009`)

Para $x>0$, $f'(x)=1/x$, $f''(x)=-1/x^2$ y $f'''(x)=2/x^3$. En $a=1$ obtenemos $f(1)=0$, $f'(1)=1$, $f''(1)=-1$, $f'''(1)=2$. Por tanto

$$
T_{3,1}(\ln x)=(x-1)-\frac{(x-1)^2}{2}+\frac{(x-1)^3}{3}.
$$

La función y sus derivadas están definidas y son continuas en cualquier intervalo cerrado contenido en $(0,\infty)$. Si se desea aplicar Lagrange entre $1$ y un $x>0$, el segmento debe permanecer positivo, lo cual se cumple, y la derivada cuarta existe en su interior. No se puede incluir el punto $0$ en esa aplicación.

### Solución 9.10 (`EDC-C09-SOL-010`)

Para $x>0$, $f(x)=x^{1/2}$, $f'(x)=\frac12x^{-1/2}$ y $f''(x)=-\frac14x^{-3/2}$. En el centro $a=1$:

$$
T_{2,1}(\sqrt{x})=1+\frac{x-1}{2}-\frac{(x-1)^2}{8}.
$$

Es el único polinomio cuadrático con esos datos diferenciales. Para aproximar valores distantes se necesita una cota de la tercera derivada $3/(8x^{5/2})$, que se vuelve grande cerca de cero. La igualdad de derivadas en $1$ **no** provee por sí sola una tolerancia global.

### Solución 9.11 (`EDC-C09-SOL-011`)

La derivación de $(1-x)^{-1}$ da $f^{(n)}(0)=n!$. Cada coeficiente de Taylor es uno, y

$$
T_{3,0}f(x)=1+x+x^2+x^3.
$$

Podemos calcular el error sin estimarlo primero, porque la identidad geométrica finita conserva exactamente lo que falta:

$$
f(x)-T_{3,0}f(x)=\frac{x^4}{1-x},\qquad x\ne1.
$$

En $x=1/2$, el polinomio vale $15/8$ y la función dos, con diferencia $1/8$. Una cota de Lagrange usa otra información: la derivada cuarta es $24/(1-t)^5$, cuyo módulo en $[0,1/2]$ no supera $768$. Esa elección da una cota $768(1/2)^4/24=2$, válida pero mucho mayor que el error exacto. La fórmula del resto y la cota superior cumplen trabajos distintos.

### Solución 9.12 (`EDC-C09-SOL-012`)

El polinomio requerido es

$$
P(x)=2-(x-a)+\frac4{2!}(x-a)^2+\frac0{3!}(x-a)^3
=2-(x-a)+2(x-a)^2.
$$

Sus primeras tres derivadas en $a$ son, respectivamente, $-1$, $4$ y $0$, y el valor es $2$. Si hubiera otro polinomio $Q$ de grado a lo sumo tres con los mismos cuatro datos, la diferencia $R=P-Q$ tendría $R^{(k)}(a)=0$ para $k=0,1,2,3$. Escribiendo $R=\sum_{k=0}^3c_k(x-a)^k$ se obtiene $k!c_k=0$ para cada $k$, luego $R\equiv0$: unicidad demostrada.

## C. Error finito y forma integral

### Solución 9.13 (`EDC-C09-SOL-013`)

Las derivadas de $\cos x$ en cero son $1,0,-1,0$, por lo que $T_{3,0}(\cos x)=1-x^2/2$. Con $x=1/5$, su valor es $1-1/50=49/50$. La derivada cuarta de coseno es coseno, con módulo a lo sumo uno en $[0,1/5]$. Lagrange con $n=3$ asegura

$$
\left|\cos\frac15-\frac{49}{50}\right|
\le\frac{(1/5)^4}{4!}=\frac1{15000}.
$$

Se ha usado una desigualdad sobre una derivada en un intervalo, no un desarrollo infinito supuesto.

### Solución 9.14 (`EDC-C09-SOL-014`)

Los datos de la exponencial en cero son todos uno. Su polinomio de orden tres da

$$
P_3(x)=1+x+\frac{x^2}{2}+\frac{x^3}{6};\qquad
P_3(1/10)=1+\frac1{10}+\frac1{200}+\frac1{6000}=\frac{6631}{6000}.
$$

Para acotar la derivada cuarta en el segmento usamos $e^t\le e^{1/10}<e<3$. La última desigualdad se obtiene de la serie positiva de C02: para $n\ge2$, $n!\ge2^{n-1}$, con desigualdad estricta en términos posteriores. Así $e=2+\sum_{n\ge2}1/n!<2+\sum_{n\ge2}2^{-(n-1)}=3$.

Lagrange con $n=3$ coloca el resto en $e^\xi(1/10)^4/24$, para $0<\xi<1/10$. Es positivo y su coeficiente es menor que tres. Por tanto

$$
0<\left|e^{1/10}-\frac{6631}{6000}\right|
<\frac{3(1/10)^4}{4!}=\frac1{80000}.
$$

La evaluación racional y la tolerancia se obtienen sin calcular previamente el valor decimal de la exponencial.

### Solución 9.15 (`EDC-C09-SOL-015`)

La identidad geométrica da

$$
\frac1{1+x}=1-x+x^2-\frac{x^3}{1+x},\qquad x\ne-1.
$$

El resto exacto es $R_2(x)=-x^3/(1+x)$. En $[0,1/2]$ tiene módulo $x^3/(1+x)\le x^3$. Por otra parte $f'''(t)=-6/(1+t)^4$, luego $|f'''(t)|\le6$ allí, y el Corolario 9.1 da $|R_2(x)|\le6x^3/3!=x^3$. En $x=1/2$ el error real vale $(1/8)/(3/2)=1/12$, mientras la cota de Lagrange calculada con $M=6$ vale $1/8$. Las cotas y el valor exacto son consistentes, pero no iguales.

### Solución 9.16 (`EDC-C09-SOL-016`)

Como seno es $C^3$ cerca del origen, el Teorema 9.6 afirma

$$
\sin x=T_{3,0}(\sin x)+o(|x|^3)
=x-\frac{x^3}{6}+o(|x|^3)\quad(x\to0).
$$

La definición de $o(|x|^3)$ expresa que **para ese orden fijo** el cociente del error por $|x|^3$ tiende a cero cuando $x\to0$. No declara que para un $x\ne0$ fijo el resto de los polinomios de órdenes $n\to\infty$ tienda a cero; este último límite requiere una cota dependiente de $n$, como la factorial en §9.7.

### Solución 9.17 (`EDC-C09-SOL-017`)

La exponencial cumple las hipótesis del resto integral en cualquier segmento finito. Con centro cero y orden uno, el Teorema 9.5 da

$$
e^x-(1+x)=\int_0^xe^t(x-t)\,dt.
$$

Para comprobar la cuenta, tratamos $x$ como extremo fijo y derivamos respecto de $t$ la expresión $e^t(x-t+1)$. El producto da $e^t(x-t+1)-e^t=e^t(x-t)$, por lo que es una primitiva del integrando. La diferencia entre sus valores en $t=x$ y $t=0$ es $e^x-(x+1)$.

Si $x>0$, el factor $x-t$ es no negativo sobre $[0,x]$. Si $x<0$, es no positivo sobre $[x,0]$, pero integrar desde cero hasta $x$ invierte el signo. En ambos casos el resto es no negativo, y es cero en $x=0$. La orientación explica el mismo signo del error a ambos lados del centro.

### Solución 9.18 (`EDC-C09-SOL-018`)

La hipótesis $C^{n+1}$ asegura que el resto integral existe sobre el segmento completo. Su fórmula es $R_n(x)=\frac1{n!}\int_a^x f^{(n+1)}(t)(x-t)^n dt$. Primero tomamos módulos y usamos la integral sobre el segmento no orientado; después aplicamos la cota de la derivada:

$$
|R_n(x)|\le\frac{M}{n!}\int_{\min(a,x)}^{\max(a,x)}|x-t|^n\,dt.
$$

En el ejercicio $x\in[a,b]$, así que podemos evaluar en $[a,x]$ por la regla de potencias y la sustitución afín de C06–C07. El valor es $(x-a)^{n+1}/(n+1)$. La escritura con módulos sirve también si consideramos un punto al otro lado del centro. Resulta

$$
|R_n(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!}.
$$

Para $x=a$, tanto el resto como la integral son cero. La potencia de la longitud mide cuánto acumula el núcleo del resto, y el factorial recoge los factores de las integraciones por partes.

## D. Taylor infinito: representaciones y excepciones

### Solución 9.19 (`EDC-C09-SOL-019`)

Las derivadas del seno en cero alternan $0,1,0,-1$; las del coseno, $1,0,-1,0$. Por tanto, para $n$ sucesivos, los únicos coeficientes no nulos producen

$$
\sin x=\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k+1}}{(2k+1)!},\qquad
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k}}{(2k)!}.
$$

No son meramente series formales: por Lagrange los restos de **todos** los polinomios de grado $n$ tienen módulo a lo sumo $|x|^{n+1}/(n+1)!$, ya que todas las derivadas trigonométricas están acotadas por uno en la recta. Para cada $x$ fijo, esa expresión tiende a cero por el criterio de razón. Se demuestra la representación para cualquier real $x$.

### Solución 9.20 (`EDC-C09-SOL-020`)

En $x=-1$, el polinomio de grado cuatro de Maclaurin de $e^x$ da

$$
T_{4,0}e^{-1}=1-1+\frac12-\frac16+\frac1{24}
=\frac38.
$$

Para $t\in[-1,0]$, $e^t\le1$. Taylor–Lagrange con $n=4$ y $a=0$, $x=-1$, produce

$$
\left|e^{-1}-\frac38\right|\le\frac1{5!}=\frac1{120}.
$$

El verdadero valor de $e^{-1}$ es algo menor que $3/8$, pero la cota no exige calcularlo decimalmente.

### Solución 9.21 (`EDC-C09-SOL-021`)

La derivación sucesiva de C02 da, para $k\ge1$, $\frac{d^k}{dx^k}\ln(1+x)=(-1)^{k-1}(k-1)!/(1+x)^k$. Al evaluar en cero y dividir por $k!$, el coeficiente es $(-1)^{k-1}/k$; el constante es $\ln1=0$.

La igualdad con la serie para $|x|<1$ fue demostrada en C08 mediante integración de la geométrica. En $x=1/2$, sus términos alternan y las magnitudes $b_k=1/(k2^k)$ disminuyen hacia cero: el cociente $b_{k+1}/b_k=k/[2(k+1)]$ es menor que uno. El criterio alternante acota el error tras los primeros $N$ términos por la magnitud del siguiente:

$$
\left|\ln\frac32-\sum_{k=1}^{N}\frac{(-1)^{k-1}}{k2^k}\right|
\le\frac{1}{(N+1)2^{N+1}}.
$$

La comparación de derivadas determina los coeficientes; la representación ya probada identifica la suma, y la alternancia proporciona la tolerancia numérica. El punto elegido está dentro del radio.

### Solución 9.22 (`EDC-C09-SOL-022`)

Para $f(x)=(1+x)^{-1}$, $f^{(n)}(0)=(-1)^nn!$, de modo que su Taylor en cero es $\sum_{n\ge0}(-1)^nx^n$ y tiene radio $1$ por el Teorema 8.2. Para $g(x)=(1+x)^3$, las derivadas de orden $n\ge4$ son cero; su Taylor consta sólo de $1+3x+3x^2+x^3$, que converge (por ser polinomio) para todo $x$, con radio infinito. El radio exactamente uno del Teorema 9.2 se afirma **sólo** cuando $\alpha$ no es un entero no negativo; la terminación algebraica es la excepción.

### Solución 9.23 (`EDC-C09-SOL-023`)

Comenzamos con la derivada en el origen. Para $h\ne0$,

$$
\frac{g(h)-g(0)}h=\frac{e^{-1/h^2}}h\longrightarrow0
$$

por el Lema 9.1 aplicado al módulo con $m=1$. Así $g'(0)=0$. Fuera de cero, la cadena da $g'(x)=2x^{-3}e^{-1/x^2}$. Su cociente incremental en el origen es

$$
\lim_{h\to0}\frac{g'(h)-g'(0)}h
=\lim_{h\to0}2h^{-4}e^{-1/h^2}=0
$$

por el mismo lema con $m=4$, y obtenemos $g''(0)=0$.

La inducción conserva dos datos: la derivada de orden $n$ tiene valor cero en el origen y, fuera de él, es $P_n(1/x)e^{-1/x^2}$. Derivar esa expresión sólo añade potencias de $1/x$ y deja otra forma polinómica por exponencial. Para derivar en cero, dividir por $h$ añade una potencia inversa a cada uno de sus monomios; el lema hace tender todos esos términos a cero. La nueva derivada exterior también tiende a cero, por lo que se une continuamente al valor cero del origen. La inducción justifica tanto la existencia de todas las derivadas como su continuidad.

### Solución 9.24 (`EDC-C09-SOL-024`)

Los datos $g^{(n)}(0)=0$ hacen nulos todos los coeficientes de Maclaurin. Cada suma parcial es cero para cualquier $x$, y su límite también es cero en toda la recta. Para $x\ne0$, sin embargo, $g(x)=e^{-1/x^2}>0$, de modo que la serie converge pero no representa a la función allí.

Peano fija primero un orden $n$ y hace acercarse $x$ al centro: para cualquier tolerancia, el cociente $|g(x)|/|x|^n$ queda pequeño en un entorno suficientemente estrecho, que puede depender de $n$. La representación por la serie fija en cambio un $x\ne0$ y hace crecer el orden. Aquí $g(x)-T_{n,0}g(x)=g(x)$ para todo $n$, así que permanece positivo. Un límite controla la aproximación al centro y el otro pediría mejorar la aproximación en un punto ya elegido; no son intercambiables.

## E. Newton y diagnósticos de teoremas

### Solución 9.25 (`EDC-C09-SOL-025`)

Para $f(x)=x^2-2$, la derivada es $2x$. El paso de Newton se escribe

$$
N_f(x)=x-\frac{x^2-2}{2x}=\frac12\left(x+\frac2x\right)
$$

si $x\ne0$. Con $x_0=3/2$, la primera media da $x_1=(3/2+4/3)/2=17/12$. La segunda es

$$
x_2=\frac12\left(\frac{17}{12}+\frac{24}{17}\right)
=\frac{577}{408}.
$$

Para justificar el control local usamos $r=\sqrt2$. Las desigualdades $7/5<r<8/5$ se comprueban elevando al cuadrado números positivos. Por tanto $[r-2/5,r+2/5]$ queda en $[1,2]$, donde $|f'|=2x\ge2$ y $|f''|=2$. Podemos tomar $m=2$ y $M=2$. El Teorema 9.10 da

$$
|x_{k+1}-r|\le\frac{M}{2m}|x_k-r|^2=\frac12|x_k-r|^2.
$$

El factor de conservación del entorno es $q=(M/2m)(2/5)=1/5<1$. La semilla $3/2$ pertenece a ese entorno, así que los iterados permanecen en él y convergen a $r$. Las cuentas exactas de los primeros pasos se realizan bajo esas hipótesis, sin deducir convergencia general sólo porque se aproximen visualmente a una raíz.

### Solución 9.26 (`EDC-C09-SOL-026`)

Para $f(x)=x^3-1$ tenemos $f'(x)=3x^2$, de modo que $f'(0)=0$. La expresión

$$
N_f(0)=0-\frac{f(0)}{f'(0)}
$$

intenta dividir $-1$ por cero y **no está definida**. El Teorema 9.10 exige $|f'|\ge m>0$ en un entorno de la raíz y, por tanto, no permite concluir nada sobre una semilla donde la derivada se anula. Esto no prueba que Newton falle desde todas las semillas: cerca de la raíz $r=1$, la derivada vale $3\ne0$ y puede elegirse un entorno compacto pequeño donde esté separada de cero.

### Solución 9.27 (`EDC-C09-SOL-027`)

(a) La función plana $g(x)=e^{-1/x^2}$ para $x\ne0$, $g(0)=0$, es $C^\infty$, pero su Taylor en cero es cero y $g(x)>0$ fuera del centro. (b) La función $f(x)=1/(1-x)$ tiene valor en $x=-2$, pero su Taylor en cero es la geométrica $\sum x^n$, divergente en $-2$ por el término general. (c) $T_{4,0}(\sin x)=x-x^3/6$ tiene **grado tres**, porque su cuarta derivada en cero es cero. Cada contraejemplo señala la inferencia equivocada y no altera los teoremas positivos existentes.

### Solución 9.28 (`EDC-C09-SOL-028`)

Si la serie de potencias $F(x)=\sum_{n\ge0}a_n(x-c)^n$ tiene radio $R>0$, el Teorema 8.9 justifica derivarla en intervalos cerrados interiores, y la Proposición 8.3 permite repetir la operación cualquier número finito de veces. En el centro,

$$
F^{(n)}(c)=n!a_n
\qquad\Longrightarrow\qquad a_n=\frac{F^{(n)}(c)}{n!}.
$$

Por tanto, si dos series representan la misma $F$ cerca del centro, cada coeficiente coincide. El enunciado tiene la premisa «**si** hay una representación por serie con radio positivo»; no construye tal serie para una función $C^\infty$ cualquiera. El ejemplo plano de 9.24 muestra que esa conversión de una necesidad en una suficiencia es inválida.

## F. Desafíos de síntesis

### Solución 9.29 (`EDC-C09-SOL-029`)

La raíz es suave sobre un intervalo abierto que contiene $[0,1/4]$. Los datos en cero son $f(0)=1$, $f'(0)=1/2$ y $f''(0)=-1/4$, y el polinomio evaluado da

$$
T_{2,0}f(x)=1+\frac x2-\frac{x^2}{8},\qquad
T_{2,0}f(1/4)=1+\frac18-\frac1{128}=\frac{143}{128}.
$$

La derivada siguiente es $f^{(3)}(t)=\frac38(1+t)^{-5/2}$, positiva y a lo sumo $3/8$ en el segmento. Lagrange expresa el resto como esa derivada en un punto interior por $(1/4)^3/3!$. Conserva el signo positivo y proporciona

$$
0<\sqrt{\frac54}-\frac{143}{128}
\le\frac{(3/8)(1/4)^3}{3!}
=\frac1{1024}.
$$

La serie binomial completa representa la misma raíz en $|x|<1$ por el Teorema 9.2, incluido $x=1/4$. Esa representación identifica un límite de todos los polinomios; la tolerancia pedida para el polinomio de orden dos procede de la cota finita de Lagrange.

### Solución 9.30 (`EDC-C09-SOL-030`)

(a) Para obtener los datos en cero derivamos por el producto y reunimos los términos que aparecen en cada paso:

$$
\begin{aligned}
f'(x)&=e^x(\cos x-\sin x),\\
f''(x)&=-2e^x\sin x,\\
f'''(x)&=-2e^x(\sin x+\cos x),\\
f^{(4)}(x)&=-4e^x\cos x.
\end{aligned}
$$

Los datos necesarios son $f(0)=1$, $f'(0)=1$, $f''(0)=0$ y $f'''(0)=-2$. Dividir cada uno por su factorial produce

$$
\boxed{T_{3,0}f(x)=1+x-\frac{x^3}{3}.}
$$

(b) En el segmento de cero a $x$, con $0\le x\le1/2$, tenemos $|f^{(4)}(t)|=4e^t|\cos t|\le4e^{1/2}$. Esa cota común permite aplicar Lagrange sin conocer el punto intermedio. El error satisface

$$
\left|e^x\cos x-\left(1+x-\frac{x^3}{3}\right)\right|
\le\frac{4e^{1/2}}{4!}x^4=\frac{e^{1/2}x^4}{6}.
$$

(c) La estimación controla el orden tres en todo el segmento. Para representar una función mediante su serie necesitamos controlar la sucesión de restos al aumentar el orden en cada punto fijado. El Teorema 9.7 aporta esa condición: $R_n(x)\to0$ cuando $n\to\infty$. La existencia de una sola cota finita no decide el límite, y la función plana muestra que incluso tener todas las derivadas y buenas aproximaciones cerca del centro para cada orden puede dejar un resto fijo positivo fuera de él.

---

**Cobertura:** `EDC-C09-SOL-001--030` responde uno a uno a `EDC-C09-EXR-001--030`. Se verifican dominios, justificación de series, hipótesis del resto y orientación de las integrales, sin invocar resultados de C10 ni C11.
