---
title: Capítulo 7 — Soluciones desarrolladas
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
source-id: EDC-C07-SOLUCIONES
source-sha256: e744038e9a6a91565d0ee7d5009203a7ccccafca27fe5567265ca3ca1827bfdb
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-07.html) · [Ejercicios](capitulo-07-ejercicios.html) · [Soluciones](capitulo-07-soluciones.html) · [Notas históricas](capitulo-07-notas.html)

Las siguientes soluciones corresponden, una por una, a [los treinta ejercicios del capítulo](capitulo-07-ejercicios.html). Se han utilizado únicamente resultados demostrados en C00–C07. Los cálculos no se separan de sus hipótesis: las funciones racionales se integran sobre intervalos que evitan sus polos, las fórmulas de sustitución conservan extremos orientados y las integrales definidas son propias.

## A. Hipótesis, lenguaje y elecciones de método

### Solución 7.1 (`EDC-C07-SOL-001`)

(a) Si $f:[a,b]\to\mathbb R$ es continua, la integrabilidad se sigue del Teorema 5.4: las sumas de Darboux pueden aproximarse arbitrariamente. Esto **establece la existencia de un número**, sin exigir una fórmula para encontrarlo. (b) Hallar una primitiva es construir $F$ continua en $[a,b]$, derivable en $(a,b)$, tal que $F'=f$ allí. La primera parte del Teorema Fundamental (C06) garantiza existencia cuando $f$ es continua, aunque $F$ pueda quedar expresada como acumulación. (c) La segunda parte (`EDC-C06-THM-005`) demuestra que el valor de la integral es $F(b)-F(a)$. No debemos usar esta última igualdad para definir la integral y luego anunciarla como teorema: en EDC la integral ya se definió mediante Darboux.

### Solución 7.2 (`EDC-C07-SOL-002`)

La sustitución del Teorema 7.1 surge de derivar $F\circ\phi$ por la regla de la cadena. Esto no exige que $\phi$ tenga inversa ni que recorra el intervalo una sola vez. Con $\phi(t)=1-t$ y $f(u)=u$,

$$
\int_0^1 f(1-t)(-1)\,dt
=\int_1^0u\,du=-\frac12.
$$

Directamente, el integrando izquierdo es $t-1$ y su integral vale $[t^2/2-t]_0^1=-1/2$. El cambio invierte los límites $1,0$, lo cual absorbe el signo de $\phi'=-1$.

### Solución 7.3 (`EDC-C07-SOL-003`)

La función $\phi(t)=t^2$ lleva **ambos extremos** $-1$ y $1$ al mismo valor $u=1$, no a $0$ y $1$. Como $\phi' (t)=2t$,

$$
\int_{-1}^1 2te^{t^2}\,dt
=\int_{\phi(-1)}^{\phi(1)}e^u\,du
=\int_1^1e^u\,du=0.
$$

También es cero por imparidad: $2t$ es impar y $e^{t^2}$ es par. El estudiante inventó un nuevo extremo inferior y descartó el tramo decreciente de la función $t\mapsto t^2$.

### Solución 7.4 (`EDC-C07-SOL-004`)

El integrando $1/x$ **no está definido en $0$**, que pertenece a $[-1,1]$. No es una función real acotada sobre todo ese intervalo y no se le puede aplicar la definición propia de Darboux de C05. Una cancelación informal de los intervalos a ambos lados de cero no crea una integral propia. En cambio $1/x$ es continua en $[1,2]$, allí sí es integrable, y

$$
\int_1^2\frac{dx}{x}=[\ln x]_1^2=\ln2.
$$

La primitiva $\ln|x|$ existe separadamente en $(-\infty,0)$ y $(0,\infty)$; no cruza el origen.

## B. Sustitución y extremos

### Solución 7.5 (`EDC-C07-SOL-005`)

La función $1+x^3$ es positiva en $[0,2]$. Elegimos $u=1+x^3$ y $du=3x^2\,dx$ como abreviatura de $du/dx=3x^2$. Los extremos se transforman en $u(0)=1$ y $u(2)=9$. Luego

$$
\int_0^2 3x^2(1+x^3)^4\,dx
=\int_1^9u^4\,du
=\left[\frac{u^5}5\right]_1^9
=\frac{9^5-1}{5}=11809.6.
$$

El valor exacto preferible es $(9^5-1)/5=59048/5$; la igualdad decimal sólo representa ese racional.

### Solución 7.6 (`EDC-C07-SOL-006`)

Puesto que $1+x^2\ge1$ en $[0,1]$, el integrando es continuo. Poniendo $u=1+x^2$ y $du/dx=2x$,

$$
\int_0^1\frac{2x}{1+x^2}\,dx
=\int_1^2\frac{du}{u}=[\ln u]_1^2=\ln2.
$$

La positividad de $u$ autoriza usar el logaritmo natural sin valor absoluto.

### Solución 7.7 (`EDC-C07-SOL-007`)

Con $u=\sin x$, $du/dx=\cos x$, y extremos $0,1$,

$$
\int_0^{\pi/2}\sin x\cos x\,dx
=\int_0^1u\,du=\frac12.
$$

Como $2\sin x\cos x=\sin2x$, otra prueba es $\frac12\int_0^{\pi/2}\sin2x\,dx=[-\cos2x/4]_0^{\pi/2}=1/2$. Los senos y cosenos son continuos en el intervalo.

### Solución 7.8 (`EDC-C07-SOL-008`)

La sustitución $u=x^2$ se aplica a $\phi(x)=x^2$ **en todo** $[-1,1]$, aunque no sea monótona. Sus extremos producen $u(-1)=u(1)=1$ y

$$
\int_{-1}^1 2xe^{x^2}\,dx=\int_1^1e^u\,du=0.
$$

Si cambiamos $2x$ por $|2x|$, obtenemos una función par no negativa, cuya integral es $2\int_0^1 2xe^{x^2}\,dx=2(e-1)>0$. Ése es **otro integrando**, no una corrección de signo del primero.

### Solución 7.9 (`EDC-C07-SOL-009`)

Sea $u=3x+1$, de modo que $du/dx=3$ y $dx=du/3$ en la notación abreviada. $x=0$ da $u=1$ y $x=1$ da $u=4$. Por tanto,

$$
\int_0^1e^{3x+1}\,dx
=\frac13\int_1^4e^u\,du
=\frac{e^4-e}{3}.
$$

La función es continua en todo $\mathbb R$ y la fórmula es una aplicación del Teorema 7.1 con cambio afín.

### Solución 7.10 (`EDC-C07-SOL-010`)

En $[0,1]$ tenemos $1+x^2\in[1,2]$, de modo que la raíz es real y continua. Escribiendo $u=1+x^2$,

$$
\begin{aligned}
\int_0^1x\sqrt{1+x^2}\,dx
&=\frac12\int_1^2u^{1/2}\,du\\
&=\frac13\left[u^{3/2}\right]_1^2
=\frac{2\sqrt2-1}{3}.
\end{aligned}
$$

La comprobación por derivación de $(1+x^2)^{3/2}/3$ produce $x\sqrt{1+x^2}$.

### Solución 7.11 (`EDC-C07-SOL-011`)

El denominador $2+\sin x\ge1$ para todo $x$, luego el integrando es continuo en $[0,\pi]$. Tomando $u=2+\sin x$ se tiene $du/dx=\cos x$ y

$$
\int_0^\pi\frac{\cos x}{2+\sin x}\,dx
=\int_2^2\frac{du}{u}=0.
$$

La función $u(x)$ sube hasta $3$ y vuelve a $2$. Su falta de inyectividad no impide el teorema orientado. El resultado también se sigue de la primitiva $\ln(2+\sin x)$ evaluada en los extremos.

### Solución 7.12 (`EDC-C07-SOL-012`)

El intervalo $[1,e]$ está contenido en $(0,\infty)$; $\ln x/x$ es continuo. La sustitución $u=\ln x$, con $du/dx=1/x$, transforma los extremos en $0,1$:

$$
\int_1^e\frac{\ln x}{x}\,dx=\int_0^1u\,du=\frac12.
$$

Una primitiva sobre $(0,\infty)$ es $(\ln x)^2/2$; al derivarla se obtiene $(\ln x)/x$.

## C. Integración por partes

### Solución 7.13 (`EDC-C07-SOL-013`)

Con $u=x$, $u'=1$, $v'=e^x$, $v=e^x$, el Teorema 7.2 da

$$
\int_0^1 xe^x\,dx=[xe^x]_0^1-\int_0^1e^x\,dx=e-(e-1)=1.
$$

La función $(x-1)e^x$ tiene derivada $e^x+(x-1)e^x=xe^x$, y sus valores terminales son $0$ y $-1$, cuya diferencia es $1$.

### Solución 7.14 (`EDC-C07-SOL-014`)

Elegimos $u=x$, $u'=1$, $v'=\sin x$, $v=-\cos x$. Entonces

$$
\int_0^\pi x\sin x\,dx
=[-x\cos x]_0^\pi+\int_0^\pi\cos x\,dx
=\pi+\sin\pi-\sin0=\pi.
$$

El resultado es positivo, compatible con $x\ge0$ y $\sin x\ge0$ en el intervalo.

### Solución 7.15 (`EDC-C07-SOL-015`)

Escribimos $\ln x=(\ln x)\cdot1$. En $[1,e]$ elegimos $u=\ln x$, $u'=1/x$, $v'=1$, $v=x$, todos continuos en su dominio. Por tanto

$$
\int_1^e\ln x\,dx=[x\ln x]_1^e-\int_1^e1\,dx=e-(e-1)=1.
$$

El candidato $x\ln x-x$ es primitiva de $\ln x$ sobre el semieje positivo, pues su derivada es $\ln x+1-1=\ln x$.

### Solución 7.16 (`EDC-C07-SOL-016`)

Primero, con $u=x^2$, $v'=e^x$,

$$
\int x^2e^x\,dx=x^2e^x-2\int xe^x\,dx.
$$

Repetimos partes en la integral restante para obtener $\int xe^x\,dx=xe^x-e^x+C$. Agrupamos:

$$
\int x^2e^x\,dx=e^x(x^2-2x+2)+C.
$$

La derivada del candidato es $e^x[(x^2-2x+2)+(2x-2)]=x^2e^x$. En los extremos,

$$
\int_0^1x^2e^x\,dx=e\,(1-2+2)-2=e-2.
$$

### Solución 7.17 (`EDC-C07-SOL-017`)

Sea $I(x)=\int_0^xe^t\cos t\,dt$. Por partes con $u=\cos t$, $v'=e^t$, resulta

$$
I(x)=e^x\cos x-1+J(x),\qquad J(x)=\int_0^xe^t\sin t\,dt.
$$

Una segunda aplicación con $u=\sin t$, $v'=e^t$ da $J(x)=e^x\sin x-I(x)$ (no aparece término en $0$ porque $\sin0=0$). Así

$$
2I(x)=e^x(\sin x+\cos x)-1.
$$

La familia de primitivas es

$$
G(x)=\frac12e^x(\sin x+\cos x)+C.
$$

Su derivada es $\frac12e^x[(\sin x+\cos x)+(\cos x-\sin x)]=e^x\cos x$. El factor $1/2$ se obtiene despejando **dos veces** la integral inicial.

### Solución 7.18 (`EDC-C07-SOL-018`)

Con $u=x$, $v'=\cos(2x)$ tenemos $u'=1$ y $v=\sin(2x)/2$. Entonces

$$
\begin{aligned}
\int_0^1x\cos(2x)\,dx
&=\left[\frac{x\sin(2x)}2\right]_0^1
-\frac12\int_0^1\sin(2x)\,dx\\
&=\frac{\sin2}{2}+\left[\frac{\cos(2x)}4\right]_0^1
=\frac{\sin2}{2}+\frac{\cos2-1}{4}.
\end{aligned}
$$

La derivada de $x\sin(2x)/2+\cos(2x)/4$ es $x\cos2x$.

### Solución 7.19 (`EDC-C07-SOL-019`)

Con $u(x)=v(x)=x$ para $0\le x\le1$,

$$
\int_0^1uv\,dx=\int_0^1x^2\,dx=\frac13,
\qquad
\left(\int_0^1u\,dx\right)\left(\int_0^1v\,dx\right)=\frac14.
$$

Son distintos. La linealidad de la integral vale para sumas y múltiplos constantes, **no** convierte el producto de funciones en producto de integrales. La identidad correcta relevante es $(uv)'=u'v+uv'$, que conduce a integración por partes cuando se conocen primitivas y regularidad apropiadas.

## D. Fracciones racionales y controles de dominio

### Solución 7.20 (`EDC-C07-SOL-020`)

Para $x\notin\{0,1\}$ buscamos $A/x+B/(x-1)$. Multiplicando por $x(x-1)$ se obtiene

$$
1=A(x-1)+Bx.
$$

En $x=0$, $A=-1$; en $x=1$, $B=1$. Por tanto, en cada uno de los intervalos $(-\infty,0)$, $(0,1)$ y $(1,\infty)$,

$$
\int\frac{dx}{x(x-1)}=-\ln|x|+\ln|x-1|+C.
$$

Las constantes pueden ser distintas en los tres componentes. Derivando se recupera $-1/x+1/(x-1)=1/[x(x-1)]$.

### Solución 7.21 (`EDC-C07-SOL-021`)

Verificamos la identidad

$$
\frac1{x(x-1)^2}=\frac1x-\frac1{x-1}+\frac1{(x-1)^2}
$$

llevando el lado derecho al denominador común: su numerador es $(x-1)^2-x(x-1)+x=x^2-2x+1-x^2+x+x=1$. La primitiva, para $x\ne0,1$ y en cada intervalo conexo del dominio, es

$$
\ln|x|-\ln|x-1|-\frac1{x-1}+C.
$$

La última derivada vale $(x-1)^{-2}$, porque $( - (x-1)^{-1})'=(x-1)^{-2}$. No se integran a través de los polos.

### Solución 7.22 (`EDC-C07-SOL-022`)

Completamos el cuadrado: $x^2+2x+2=(x+1)^2+1>0$ para todo $x$. El numerador se divide como $(2x+2)+1$. Entonces

$$
\begin{aligned}
\int\frac{2x+3}{x^2+2x+2}\,dx
&=\int\frac{2x+2}{(x+1)^2+1}\,dx
+\int\frac{dx}{(x+1)^2+1}\\
&=\ln((x+1)^2+1)+\arctan(x+1)+C.
\end{aligned}
$$

La primera derivada es $(2x+2)/Q(x)$ y la segunda $1/Q(x)$; suman el integrando. No hay restricciones de dominio adicionales.

### Solución 7.23 (`EDC-C07-SOL-023`)

La división euclídea da $x^3+1=x(x^2-1)+(x+1)$, por lo que, para $x\ne-1,1$,

$$
\frac{x^3+1}{x^2-1}=x+\frac{x+1}{(x-1)(x+1)}=x+\frac1{x-1}.
$$

En $[2,3]$ la función es continua y $x-1>0$. Aplicando el Teorema Fundamental,

$$
\int_2^3\frac{x^3+1}{x^2-1}\,dx
=\left[\frac{x^2}{2}+\ln(x-1)\right]_2^3
=\frac52+\ln2.
$$

La fórmula cancelada existe en $x=-1$, pero el cociente original es $0/0$ allí; ese punto sigue excluido de su dominio original y no queda restituido por la simplificación.

### Solución 7.24 (`EDC-C07-SOL-024`)

Sea $Q(x)=(x-1)(x-2)(x-3)$. Para raíces distintas, el Teorema 7.3 da $A_i=1/Q'(r_i)$. Tenemos

$$
Q'(1)=(1-2)(1-3)=2,\quad
Q'(2)=(2-1)(2-3)=-1,\quad
Q'(3)=(3-1)(3-2)=2.
$$

Así,

$$
\frac1{(x-1)(x-2)(x-3)}
=\frac{1/2}{x-1}-\frac1{x-2}+\frac{1/2}{x-3}.
$$

Las primitivas en cada componente de $\mathbb R\setminus\{1,2,3\}$ son

$$
\frac12\ln|x-1|-\ln|x-2|+\frac12\ln|x-3|+C.
$$

La identidad se verifica multiplicando por $Q$ o usando los coeficientes en las raíces y comparando grados, como en la prueba del Teorema 7.3.

## E. Aplicaciones y significado de la integral

### Solución 7.25 (`EDC-C07-SOL-025`)

En $0\le x\le2$, $2x-x^2=x(2-x)\ge0$, por lo que $y=2x$ está encima de $y=x^2$. El área es

$$
A=\int_0^2(2x-x^2)\,dx
=\left[x^2-\frac{x^3}{3}\right]_0^2
=4-\frac83=\frac43.
$$

La continuidad de la diferencia garantiza la existencia de la integral; su no negatividad justifica leerla como área geométrica.

### Solución 7.26 (`EDC-C07-SOL-026`)

La diferencia $x-x^2=x(1-x)$ se anula en $0$ y $1$. Es negativa en $[-1,0]$, positiva en $[0,1]$ y negativa en $[1,2]$. Por tanto,

$$
\begin{aligned}
A&=\int_{-1}^0(x^2-x)\,dx
+\int_0^1(x-x^2)\,dx
+\int_1^2(x^2-x)\,dx\\
&=\frac56+\frac16+\frac56=\boxed{\frac{11}{6}}.
\end{aligned}
$$

En cambio,

$$
\int_{-1}^{2}(x-x^2)\,dx
=\left[\frac{x^2}2-\frac{x^3}3\right]_{-1}^{2}
=-\frac32,
$$

cuyo valor absoluto es $3/2\ne11/6$. Las contribuciones orientadas pueden cancelarse y el área total no.

### Solución 7.27 (`EDC-C07-SOL-027`)

El trabajo de la fuerza externa en el desplazamiento positivo es

$$
W_{\mathrm{ext}}=\int_0^L kx\,dx=\frac{kL^2}{2}.
$$

Para la fuerza de restitución, que se opone al desplazamiento, obtenemos

$$
W_{\mathrm{res}}=\int_0^L(-kx)\,dx=-\frac{kL^2}{2}.
$$

Si $k$ se mide en $\mathrm{N}/\mathrm m$ y $L$ en $\mathrm m$, $kL^2$ tiene unidades $\mathrm{N\,m}=\mathrm J$. No se deben intercambiar los signos de fuerzas físicamente opuestas.

### Solución 7.28 (`EDC-C07-SOL-028`)

Por el Teorema Fundamental aplicado a $Q'=r$,

$$
Q(4)-Q(1)=\int_1^4(2t+3)\,dt
=\left[t^2+3t\right]_1^4
=(16+12)-(1+3)=24.
$$

Para hallar $Q(4)$ como número absoluto necesitamos una condición inicial, por ejemplo el valor $Q(1)$. La derivada sólo determina $Q$ hasta una constante; en el modelo habría que especificar además las unidades de $t$ y $Q$ para atribuir unidades coherentes a los coeficientes $2$ y $3$.

## F. Demostraciones y desafío de síntesis

### Solución 7.29 (`EDC-C07-SOL-029`)

Sea $\phi(t)=-t$ en $[-b,-a]$ con $a<b$. Entonces $\phi(-b)=b$, $\phi(-a)=a$ y $\phi'(t)=-1$. Por la sustitución orientada,

$$
-\int_{-b}^{-a}f(-t)\,dt
=\int_b^a f(u)\,du
=-\int_a^b f(u)\,du.
$$

Multiplicando por $-1$ en ambos lados,

$$
\boxed{\int_{-b}^{-a}f(-t)\,dt=\int_a^b f(u)\,du.}
$$

La primera minusvalía proviene de la derivada del cambio; la segunda, de la orientación invertida de los extremos. Se compensan. La continuidad de $f$ garantiza integrabilidad de todas las expresiones.

### Solución 7.30 (`EDC-C07-SOL-030`)

Cada sumando es continuo en $[0,1]$: $e^{x^2}$ es continua, $1+x^2>0$ asegura que $\ln(1+x^2)$ existe, y $(x+1)(x+2)>0$ evita los polos racionales.

**Primer sumando.** La sustitución $u=x^2$ transforma $x\in[0,1]$ en $u\in[0,1]$ y da

$$
\int_0^12xe^{x^2}\,dx=\int_0^1e^u\,du=e-1.
$$

**Segundo sumando.** Con $u=1+x^2$, los extremos son $u=1$ y $u=2$ y

$$
\begin{aligned}
\int_0^1x\ln(1+x^2)\,dx
&=\frac12\int_1^2\ln u\,du\\
&=\frac12[\,u\ln u-u\,]_1^2
=\ln2-\frac12,
\end{aligned}
$$

usando la primitiva de $\ln u$ obtenida por partes.

**Tercer sumando.** La identidad

$$
\frac1{(x+1)(x+2)}=\frac1{x+1}-\frac1{x+2}
$$

proviene de resolver la descomposición lineal. Por tanto,

$$
\begin{aligned}
\int_0^1\frac{dx}{(x+1)(x+2)}
&=[\ln(x+1)-\ln(x+2)]_0^1\\
&=\ln\left(\frac23\right)-\ln\left(\frac12\right)
=\ln\frac43.
\end{aligned}
$$

Sumando los tres resultados obtenemos

$$
\boxed{\int_0^1\left(2xe^{x^2}+x\ln(1+x^2)+\frac1{(x+1)(x+2)}\right)dx
=e-\frac32+\ln\frac83.}
$$

Para el control por derivación, definimos

$$
G(x)=e^{x^2}+\frac12\bigl[(1+x^2)\ln(1+x^2)-(1+x^2)\bigr]
+\ln(x+1)-\ln(x+2).
$$

Por la cadena y el producto, $G'=2xe^{x^2}+x\ln(1+x^2)+1/(x+1)-1/(x+2)$, idéntico al integrando. La diferencia $G(1)-G(0)$ reproduce exactamente el valor anterior, completando una segunda verificación sin utilizar capítulos posteriores.

---

**Control de cobertura:** `EDC-C07-SOL-001--030` responde uno a uno a `EDC-C07-EXR-001--030`, incluidos los incisos conceptuales, los dominios, la orientación y las demostraciones. Los tres procedimientos se justifican desde C00–C07, sin apelar a series de potencias, Taylor o integrales impropias.
