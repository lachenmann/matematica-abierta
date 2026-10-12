---
title: Soluciones razonadas del laboratorio de investigación
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
source-id: EDC_LABORATORIO_SOLUCIONES
source-sha256: 65be8b51086b0c883cc1a84de4675728cee34cc4352dbbf9616612848292a791
---

[Índice del libro](index.qmd) · [Prefacio](prefacio.md) · [Itinerarios](itinerarios.md)

Cada solución responde al problema `INV-Cxx-nn` con el mismo código en [el laboratorio](laboratorio.md). Se conservan las hipótesis y fronteras lógicas de los capítulos originales.

## SOL-INV-C00-01 — Herón sin derivadas

Sea $s=\sqrt2$ y $x>s>0$. Por álgebra,

$$
\frac{x+2/x}{2}-s=\frac{x^2-2sx+s^2}{2x}=\frac{(x-s)^2}{2x}\ge0.
$$

Asimismo $\frac12(x+2/x)-x=(2-x^2)/(2x)<0$. El dato $x_0=2>s$ y la inducción muestran $s\le x_{n+1}<x_n$. La sucesión es monótona, acotada inferiormente y, por C00, converge a algún $\ell\ge s>0$. Pasar al límite en la identidad recursiva (denominadores no nulos) da $\ell=(\ell+2/\ell)/2$, de donde $\ell^2=2$ y $\ell=s$. La igualdad exacta del error demuestra además

$$
0\le x_{n+1}-s\le\frac{(x_n-s)^2}{2s}.
$$

Ésta no es sólo una convergencia: informa del modo en que se amplifica la precisión cuando el error ya es pequeño. No se han invocado derivadas ni el teorema de Newton.

## SOL-INV-C01-01 — Tangentes a la cúbica

Por el cociente incremental de C01, $f'(a)=3a^2$. La tangente en $(a,a^3)$ es

$$
y=a^3+3a^2(x-a)=3a^2x-2a^3.
$$

Pasa por $(0,b)$ si y sólo si $-2a^3=b$. La ecuación cúbica posee exactamente una raíz real $a=\sqrt[3]{-b/2}$, por monotonía algebraica del cubo, por lo que existe **una sola tangente diferencial** por cada punto del eje vertical. En cambio, el problema análogo para $y=x^2$ conduce a una ecuación cuadrática y puede tener 0, 1 o 2 tangentes según la posición del punto. Contar intersecciones globales no determina una tangente: en la propia cúbica, la horizontal en cero atraviesa su curva.

## SOL-INV-C02-01 — Identidad de arcotangentes

Sean $\alpha=\arctan x$ y $\beta=\arctan(1/x)$ para $x>0$. Se cumplen $0<\alpha,\beta<\pi/2$, $\tan\alpha=x$ y $\tan\beta=1/x$. La identidad trigonométrica da

$$
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta
=\cos\alpha\cos\beta(1-\tan\alpha\tan\beta)=0.
$$

Como $0<\alpha+\beta<\pi$, necesariamente $\alpha+\beta=\pi/2$. Por las reglas de C02, la derivada de la suma es

$$
\frac1{1+x^2}-\frac1{x^2(1+x^{-2})}=0.
$$

Que una derivada nula implique constancia sobre un intervalo **se probará en C03** mediante el teorema del valor medio; usar esa conclusión aquí sería anticiparla. La demostración geométrica anterior no la necesita.

## SOL-INV-C03-01 — AM–GM ponderada

La función $\ln$ es estrictamente cóncava en $(0,\infty)$ por C03, y $\exp$ es estrictamente creciente por C02. Demostraremos por inducción la desigualdad de Jensen finita

$$
\sum_{i=1}^n w_i\ln x_i\le \ln\left(\sum_{i=1}^n w_ix_i\right).
$$

Para un término es igualdad. Si $0\le w_n<1$, sea $\lambda=1-w_n>0$ y $A=\sum_{i=1}^{n-1}(w_i/\lambda)x_i$. Por inducción, $\sum_{i<n}(w_i/\lambda)\ln x_i\le\ln A$. Multiplicamos por $\lambda$ y añadimos $w_n\ln x_n$; la concavidad da $\lambda\ln A+w_n\ln x_n\le\ln(\lambda A+w_nx_n)$. Si $w_n=1$, la conclusión es trivial. Esto cierra la inducción. Aplicando la exponencial (que preserva desigualdades) obtenemos $\prod x_i^{w_i}\le\sum w_ix_i$. Por concavidad **estricta**, hay igualdad exactamente cuando todos los $x_i$ con peso estrictamente positivo son iguales. Los pesos nulos son irrelevantes.

## SOL-INV-C04-01 — Error de generaciones

Por el valor compatible que construye C04, $A=4T/3$ y $P_n=A(1-4^{-n})$, de modo que $(A-P_n)/A=4^{-n}$. Para $n=9$ la fracción es $1/262144>10^{-6}$; para $n=10$ es $1/1048576<10^{-6}$. Así, $n=10$ es el menor entero positivo que cumple la tolerancia. Los $P_n$ son áreas **poligonales finitas**; la identificación del área parabólica requiere también demostrar el encerramiento exterior y que su holgura desaparece.

## SOL-INV-C05-01 — La función de Thomae

La función $\tau$ está acotada entre cero y uno. Cada subintervalo no degenerado contiene irracionales, así que **todas** las sumas inferiores son cero. Dado $\varepsilon>0$, elegimos un entero $N$ tal que $1/(N+1)<\varepsilon/2$. El conjunto $F_N$ de racionales de $[0,1]$ cuya fracción irreducible tiene denominador $\le N$ es **finito**: por cada $1\le q\le N$ sólo hay un número finito de numeradores $0\le p\le q$.

Rodeamos cada punto de $F_N$ mediante intervalos muy cortos, eligiendo una partición que tenga como cortes sus extremos, con **longitud total afectada menor que $\varepsilon/2$**. En los subintervalos que no contienen puntos de $F_N$, todo valor racional de $\tau$ es $\le1/(N+1)$ y en los irracionales vale cero; en los afectados, la oscilación no supera uno. Los extremos de corte compartidos que pertenezcan a $F_N$ deben incluirse entre los subintervalos afectados, lo cual se asegura escogiendo los cortes fuera de $F_N$. Por tanto

$$
U(\tau,P)-L(\tau,P)<\varepsilon/2+(b-a)\frac1{N+1}<\varepsilon,
\qquad [a,b]=[0,1].
$$

El criterio de Darboux prueba integrabilidad; como $L(\tau,P)=0$ en todas las particiones, su integral es cero. No se ha usado un criterio de discontinuidades de medida nula.

## SOL-INV-C06-01 — Igualdad de valores finales, diferencia de trayectorias

Por C06, $\int_0^1x\,dx=\int_0^1(1-x)\,dx=1/2$. Sus acumuladoras son

$$
F(t)=t^2/2,\qquad G(t)=t-t^2/2.
$$

Para $0<t<1$, $G(t)-F(t)=t(1-t)>0$, así que no coinciden interiormente, pese a que sus valores iniciales y finales sí coinciden. Además $F'=f$ y $G'=g$ por la primera parte del Teorema Fundamental: el dato de una **integral final** no determina la evolución de toda la acumulación.

## SOL-INV-C07-01 — Un logaritmo, dos caminos

La función $\ln(1+x)$ es continua en $[0,1]$, porque $1+x\ge1>0$. Por partes, $u=\ln(1+x)$ y $dv=dx$ dan

$$
I=[x\ln(1+x)]_0^1-\int_0^1\frac{x}{1+x}\,dx
=\ln2-\int_0^1\left(1-\frac1{1+x}\right)dx
=2\ln2-1.
$$

Por la vía alternativa, ponemos $t=1+x$ y comprobamos por derivación que $H(t)=t\ln t-t$ tiene derivada $\ln t$ para $t>0$. Entonces $I=H(2)-H(1)=2\ln2-1$. Ambas vías son válidas sin singularidades, pero destacan reglas distintas: producto/integración por partes frente a composición/sustitución.

## SOL-INV-C07-02 — Trayectoria no monótona

Como $\phi(-1)=\phi(1)=1$, la sustitución orientada de C07 con $f(u)=u$ produce

$$
\int_{-1}^1\phi(t)\phi'(t)\,dt
=\int_1^1u\,du=0.
$$

Directamente, $\phi(t)\phi'(t)=t^2(2t)=2t^3$, impar, y las contribuciones de $[-1,0]$ y $[0,1]$ se cancelan (o se evalúan usando $t^4/2$). La función $\phi$ decrece y luego crece: **la orientación**, no una supuesta monotonía, explica la cancelación.

## SOL-INV-C08-01 — Producto, derivación y cota

Para $|x|<1$, la serie geométrica converge absolutamente. El producto de Cauchy de dos copias tiene coeficiente $c_n=\sum_{j=0}^n1=n+1$ y suma $(1-x)^{-2}$. Por otro lado, el Teorema 8.9 autoriza derivar $\sum_{n=0}^{\infty}x^{n+1}=x/(1-x)$, lo que da exactamente $\sum_{n=0}^{\infty}(n+1)x^n=(1-x)^{-2}$. Para $|x|\le r<1$,

$$
\left|\sum_{n=N+1}^{\infty}(n+1)x^n\right|\le\sum_{n=N+1}^{\infty}(n+1)r^n
=\frac{r^{N+1}((N+2)-(N+1)r)}{(1-r)^2}.
$$

La última igualdad resulta al derivar dentro de $0\le r<1$ la identidad geométrica de cola $\sum_{n=N+1}^{\infty}r^{n+1}=r^{N+2}/(1-r)$, o por manipulación de sumas finitas y paso al límite. La cota vale simultáneamente en $[-r,r]$.

## SOL-INV-C09-01 — Newton y Herón

Para $f(x)=x^2-2$, el método de Newton de C09 da $N_f(x)=x-(x^2-2)/(2x)=(x+2/x)/2$, siempre que $x>0$. Es exactamente Herón. Si $s=\sqrt2$, álgebra elemental proporciona

$$
N_f(x)-s=\frac{(x-s)^2}{2x}.
$$

Para $x\ge s$, se obtiene $0\le e_{n+1}\le e_n^2/(2s)$, y la convergencia desde $x_0=2$ ya fue probada en INV-C00-01. El Teorema 9.10 generaliza el control cuadrático a raíces simples de funciones $C^2$ con $|f'|$ acotada inferiormente y $|f''|$ superiormente, aunque ya no exista una identidad exacta tan sencilla.

## SOL-INV-C10-01 — Mitad de la capacidad

Por el Teorema 10.7, $y(t)=K/(1+A e^{-r(t-t_0)})$ con $A=K/y_0-1$. La hipótesis $0<y_0<K/2$ implica $A>1$ y la solución es creciente. La ecuación $y(t)=K/2$ equivale a $A e^{-r(t-t_0)}=1$, de donde

$$
t_{1/2}=t_0+\frac1r\ln\left(\frac K{y_0}-1\right).
$$

Es futuro porque el logaritmo es positivo; la monotonía estricta garantiza **unicidad**. Si $y_0=K/2$, el instante es el inicial; si $y_0>K/2$, la trayectoria positiva tiende a $K$ desde arriba o desde abajo según el dato, pero no alcanza $K/2$ en un instante **posterior**. El factor $r$ tiene unidades inversas del tiempo, de modo que $1/r$ es una duración.

## SOL-INV-C10-02 — Unicidad por energía

Sea $w=x_1-x_2$. Satisface $w''+\omega^2w=0$. La cantidad

$$
E(t)=(w'(t))^2+\omega^2(w(t))^2\ge0
$$

es derivable y $E'(t)=2w'(t)(w''(t)+\omega^2w(t))=0$. Por el teorema del valor medio, es constante. Si las posiciones y velocidades coinciden en $t_0$, $E(t_0)=0$. De $E\equiv0$ y la positividad de los cuadrados concluimos $w'=w=0$ en todo el intervalo. Verificar una fórmula explícita es una prueba de existencia; la energía elimina todas las demás soluciones con los mismos dos datos.

## SOL-INV-C11-01 — Certificados cruzados

El Teorema Fundamental da $I=1-e^{-1}$. Como $|y'(t)|=e^{-t}\le1$ en $[0,1]$, el Teorema 11.3 certifica para cualquier suma etiquetada de $n$ intervalos iguales $|S_n-I|\le1/(2n)$. Taylor–Lagrange en torno a cero, aplicado a $e^x$ en $x=-1$, tiene resto para grado $N$ acotado por $1/(N+1)!$: en el segmento $[-1,0]$, $e^t\le1$. Por tanto $|e^{-1}-T_N|\le1/(N+1)!$. Con $A_N=1-T_N$ se sigue la segunda cota; la tercera procede de la desigualdad triangular:

$$
|S_n-A_N|\le|S_n-I|+|I-A_N|\le\frac1{2n}+\frac1{(N+1)!}.
$$

La comparación no utiliza evaluaciones decimales ni supone que dos aproximaciones convergen sólo porque visualmente parecen acercarse.

---

**Correspondencia:** catorce problemas `INV-Cxx-nn` ↔ catorce soluciones `SOL-INV-Cxx-nn`, con pruebas por las herramientas anteriores a cada problema.
