---
title: Capítulo 3 — Soluciones desarrolladas
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
source-id: EDC-C03-SOLUCIONES
source-sha256: 53506b4e77d814b0d72ded960267408c937e4e89e82345b95065fe9766dac092
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

La función $\ln$ es continua y derivable en un intervalo que contiene $[1,e]$, y $e>1$, de modo que podemos aplicar el valor medio. La pendiente media es

$$
\frac{\ln e-\ln1}{e-1}=\frac1{e-1}.
$$

Como $(\ln x)'=1/x$, el punto buscado debe satisfacer $1/c=1/(e-1)$, y la ecuación da $c=e-1$. Resolverla todavía exige comprobar que ese número está en el interior del intervalo. La construcción de $e$ en C02 permite hacerlo sin aproximaciones: $e=\sum_{n\ge0}1/n!>1+1=2$, porque después de los dos primeros términos quedan términos positivos. Así $e-1>1$, mientras que $e-1<e$ es inmediato. El valor encontrado pertenece a $(1,e)$ y satisface la conclusión.

### Solución 3.7 (`EDC-C03-SOL-007`)

La función es un polinomio, por lo que es continua en el intervalo compacto y tiene máximo y mínimo absolutos. Para localizar los candidatos interiores calculamos $f'(x)=2x-4$: el único punto estacionario es $x=2$, y no hay puntos de no derivabilidad. La proposición de optimización obliga a que cualquier extremo esté en ese punto o en uno de los dos bordes. Comparamos

$$
f(-1)=6,\qquad f(2)=-3,\qquad f(5)=6.
$$

El mínimo absoluto es $-3$ y se alcanza en $2$; el máximo absoluto es $6$ y se alcanza en ambos extremos $-1$ y $5$. La lista es exhaustiva porque la existencia y Fermat redujeron primero la búsqueda a esos tres puntos. Si hubiéramos comparado sólo las soluciones de $f'=0$, habríamos encontrado el mínimo y omitido los dos lugares del máximo.

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

Si $I$ consta de un único punto, la función tiene un único valor y es constante. En los demás casos, tomemos cualesquiera $x<y$ en $I$. La condición de intervalo asegura que todo el segmento $[x,y]$ pertenece al dominio. La continuidad de $f$ en todo $I$, entendida relativamente, garantiza su continuidad al restringirla a $[x,y]$, incluso cuando $x$ o $y$ sea un borde incluido de $I$. Cada punto de $(x,y)$ es interior de $I$, de modo que allí existe la derivada y vale cero.

El teorema del valor medio se aplica por tanto sobre $[x,y]$ y proporciona un $c\in(x,y)$ con

$$
f(y)-f(x)=f'(c)(y-x)=0.
$$

Así $f(x)=f(y)$ para cualquier par de puntos del dominio, incluidos sus bordes. Esta es la constancia en todo $I$ que queremos demostrar y coincide con el Corolario 3.1 aplicado a $f$ y a la función nula.

Las dos condiciones de dominio cumplen tareas distintas. Ser intervalo permite unir cualquier par por un segmento contenido en él; en un dominio formado por dos intervalos separados podemos tomar una constante distinta en cada uno y obtener derivada cero sin constancia global. La continuidad en los bordes permite comparar también con sus valores: en $[0,1]$, la función que vale cero para $0<x<1$ y uno en $x=0$ y $x=1$ tiene derivada cero en el interior, pero no es constante en todo el dominio. Falla precisamente la continuidad exigida en los extremos. La hipótesis del ejercicio excluye ese caso.

### Solución 3.12 (`EDC-C03-SOL-012`)

Para $x<y$ en $I$, la derivabilidad en $I$ implica continuidad en $[x,y]$ y derivabilidad en $(x,y)$. El valor medio produce $f(y)-f(x)=f'(c)(y-x)>0$ por $f'(c)>0$. Luego $f(y)>f(x)$. No se exige continuidad de $f'$ ni existencia de un límite de $f'$; sólo los valores puntuales positivos de esa derivada y las hipótesis del valor medio.

### Solución 3.13 (`EDC-C03-SOL-013`)

Como $f''\ge0$ en el intervalo abierto $I$, la función $f'$ es no decreciente por el criterio de monotonía. El Teorema 3.6 demuestra que, para cualesquiera $x,y\in I$,

$$
f(y)\ge f(x)+f'(x)(y-x).
$$

El segundo miembro es el valor de la recta tangente a la gráfica en $(x,f(x))$, evaluada en $y$. La comparación vale para todos los puntos **del mismo intervalo $I$**; no autoriza prolongar la conclusión a regiones fuera del dominio o a componentes desconectadas.

### Solución 3.14 (`EDC-C03-SOL-014`)

En $(0,\infty)$, las reglas de C02 dan $(\ln x)'=1/x$ y $(\ln x)''=-1/x^2<0$. La primera derivada es por tanto estrictamente decreciente, y el criterio de concavidad coloca la gráfica por debajo de sus tangentes. Para obtener la expresión $y-1$, elegimos el punto de contacto $x=1$: allí la altura es cero y la pendiente es uno. Resulta

$$
\ln y\le\ln1+(\ln1)'(y-1)=y-1\qquad(y>0).
$$

Para justificar la igualdad única podemos mirar la comparación que produce el valor medio. Si $y>1$, la pendiente intermedia $1/c$ es menor que uno, así que $\ln y<y-1$. Si $0<y<1$, tenemos $y<c<1$ y $1/c>1$; al multiplicar por $y-1<0$ obtenemos de nuevo $\ln y<y-1$. En $y=1$ ambos miembros son cero.

### Solución 3.15 (`EDC-C03-SOL-015`)

La cota $f'(x)\ge m>0$ asegura crecimiento estricto mediante el valor medio. La función es entonces inyectiva y tiene inversa sobre $f(I)$. Para estudiar cuánto cambia esa inversa, expresamos primero dos valores de su dominio como $u=f(x)$ y $v=f(y)$. Si $x<y$, la continuidad y derivabilidad de $f$ permiten aplicar el valor medio en $[x,y]$ y obtener

$$
v-u=f'(c)(y-x)\ge m(y-x).
$$

La separación entre imágenes es al menos $m$ veces la separación entre argumentos. Como $m>0$, podemos dividir y obtener $0<y-x\le(v-u)/m$. Reemplazando $x$ e $y$ por $f^{-1}(u)$ y $f^{-1}(v)$ resulta la desigualdad buscada para ese orden; al intercambiar los argumentos cubrimos el orden opuesto, y si coinciden ambos miembros son cero. Así $|f^{-1}(v)-f^{-1}(u)|\le|v-u|/m$, sin necesitar una fórmula explícita de la inversa.

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

Buscamos relacionar los incrementos de dos funciones en los extremos con sus derivadas en un mismo punto. Aplicar el valor medio por separado podría dar dos puntos distintos, por lo que construimos una sola función a la que podamos aplicar Rolle. Los incrementos extremos de $f$ y $g$ serán coeficientes constantes, elegidos para que los valores en $a$ y $b$ se cancelen:

$$
H(x)=(f(b)-f(a))(g(x)-g(a))-(g(b)-g(a))(f(x)-f(a)).
$$

Por las hipótesis y las reglas de combinaciones lineales, $H$ es continua en $[a,b]$ y derivable en $(a,b)$. En $a$ se anulan las dos diferencias interiores, luego $H(a)=0$. En $b$ los dos productos coinciden:

$$
H(b)=(f(b)-f(a))(g(b)-g(a))-(g(b)-g(a))(f(b)-f(a))=0.
$$

Rolle proporciona un $c\in(a,b)$ con $H'(c)=0$. Al derivar, los incrementos extremos permanecen constantes y las diferencias interiores producen $g'(c)$ y $f'(c)$, respectivamente:

$$
(f(b)-f(a))g'(c)-(g(b)-g(a))f'(c)=0,
$$

que es la igualdad pedida. La elección de una función común aseguró que ambas derivadas se evaluaran en el mismo punto. No dividimos por $g'(c)$ ni por $g(b)-g(a)$, así que la igualdad sigue teniendo sentido cuando alguno de esos números es cero.

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

Si $y>x$, aplicamos el valor medio en $[x,y]$; la continuidad necesaria se sigue de la derivabilidad. Obtenemos $f(y)-f(x)=f'(c)(y-x)$ con $x<c<y$. Como $f'$ es no decreciente, $f'(c)\ge f'(x)$, y la multiplicación por el incremento positivo da la desigualdad de soporte. Si $y<x$, aplicamos el teorema en $[y,x]$ y reordenamos la igualdad: $y<c<x$ y $f'(c)\le f'(x)$, pero el factor $y-x$ es negativo. Su signo invierte la comparación y vuelve a dar $f(y)-f(x)\ge f'(x)(y-x)$. En $y=x$ hay igualdad.

Para deducir convexidad queremos comparar $f$ en un punto intermedio con la secante que une los dos extremos. Fijemos $z=(1-t)x+ty$ para $x,y\in I$ y $t\in[0,1]$. La condición de intervalo asegura $z\in I$. Usamos como base de las dos rectas de soporte el mismo punto $z$:

$$
f(x)\ge f(z)+f'(z)(x-z),\quad
f(y)\ge f(z)+f'(z)(y-z).
$$

Multiplicamos la primera desigualdad por $1-t$ y la segunda por $t$, ambas cantidades no negativas. Al sumar, los desplazamientos desde $z$ se compensan: $(1-t)(x-z)+t(y-z)=0$. El término con $f'(z)$ desaparece y queda $(1-t)f(x)+tf(y)\ge f(z)$, precisamente la definición de convexidad. Para $t=0$ o $t=1$ la comparación es una igualdad.

### Solución 3.25 (`EDC-C03-SOL-025`)

La existencia y la unicidad requieren razones distintas. Para la existencia, $f$ es continua en $[a,b]$ y sus valores extremos tienen signos opuestos; el valor intermedio de C00 proporciona un $c\in(a,b)$ con $f(c)=0$. Los signos estrictos impiden que ese cero sea uno de los bordes.

Para la unicidad, tomemos cualquier par $x<y$ en $[a,b]$. La continuidad en los extremos de ese segmento y la derivabilidad entre ellos permiten aplicar el valor medio, que da $f(y)-f(x)=f'(\xi)(y-x)\le-m(y-x)<0$. Así la función es estrictamente decreciente en todo el intervalo. Dos ceros distintos tendrían el mismo valor y contradirían esa comparación. Existe, por tanto, exactamente un cero interior.

## F. Descubrimiento y optimización

### Solución 3.26 (`EDC-C03-SOL-026`)

Si los lados son $x,y>0$ y el perímetro $P$, entonces $x+y=P/2$ y $y=P/2-x$ exige $0<x<P/2$. El área es $A(x)=x(P/2-x)$, que se extiende continuamente a $[0,P/2]$ con $A=0$ en los dos bordes. Su derivada es $A'(x)=P/2-2x$, positiva para $x<P/4$ y negativa para $x>P/4$. Por el criterio de monotonía, el máximo absoluto ocurre en $x=P/4$, y $y=P/4$: se trata de un cuadrado. El área máxima vale $P^2/16$. Los bordes degenerados de área cero no superan el área positiva del candidato.

### Solución 3.27 (`EDC-C03-SOL-027`)

Para un cilindro cerrado de radio $r>0$ y altura $h>0$, el área incluye las dos tapas circulares y la superficie lateral:

$$
S=2\pi r^2+2\pi rh,\qquad V=\pi r^2h.
$$

La restricción permite expresar la altura mediante el radio, $h=S/(2\pi r)-r$. Necesitamos conservar $h>0$: al multiplicar por $r>0$, esa condición equivale a $0<r<\sqrt{S/(2\pi)}$. Sustituimos la altura en el volumen y obtenemos una función de una sola variable,

$$
V(r)=\frac S2r-\pi r^3,
\qquad V'(r)=\frac S2-3\pi r^2.
$$

La ecuación de pendiente nula da $r_*=\sqrt{S/(6\pi)}$, que pertenece al dominio y es su único punto estacionario. La derivada es positiva antes de él y negativa después, por lo que el valor medio justifica crecimiento y decrecimiento en esos intervalos. Cada radio admisible distinto de $r_*$ tiene entonces un volumen menor que $V(r_*)$: el máximo es global.

En los bordes del dominio los límites son cero. Cuando $r\to0^+$, se ve directamente en el polinomio $V(r)\to0$, aunque la altura crezca sin límite. Cuando $r\to\sqrt{S/(2\pi)}^-$, la fórmula de la altura da $h\to0$ y el volumen vuelve a tender a cero. Para el radio óptimo, $S=6\pi r_*^2$ y

$$
h_* =\frac S{2\pi r_*}-r_*=3r_*-r_*=2r_*.
$$

La altura óptima es igual al diámetro. El cálculo utiliza el área total de un cilindro cerrado; quitar una tapa modificaría la restricción inicial y requeriría otro problema.

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

La raíz cuadrada es estrictamente creciente sobre los valores positivos, así que podemos minimizar el cuadrado de la distancia y evitar su derivación. Para el punto $(x,x^2)$ de la parábola obtenemos

$$
D(x)^2=x^2+(x^2-1)^2=x^4-x^2+1=:G(x).
$$

Antes de buscar candidatos conviene asegurar que hay un mínimo global, pues el dominio es toda la recta. El término de grado cuatro domina al de grado dos cuando $|x|$ crece, de modo que $G(x)\to+\infty$. Podemos elegir un intervalo cerrado grande, con cero en su interior, fuera del cual $G(x)>G(0)$. Dentro, la continuidad garantiza un mínimo; su valor no supera $G(0)$, así que ningún punto exterior puede mejorarlo. Ese mínimo es global.

La función es derivable en toda la recta, luego cada punto donde se alcance ese mínimo satisface Fermat. Calculamos

$$
G'(x)=4x^3-2x=2x(2x^2-1).
$$

Los únicos candidatos son $x=0$ y $x=\pm1/\sqrt2$. Sus valores son $G(0)=1$ y $G(\pm1/\sqrt2)=1/4-1/2+1=3/4$. La existencia ya asegurada y esta lista exhaustiva permiten concluir que el mínimo es $3/4$, alcanzado exactamente en los dos últimos candidatos. La distancia mínima es por tanto $\sqrt3/2$, y los puntos buscados son

$$
\left(\frac1{\sqrt2},\frac12\right)
\quad\text{y}\quad
\left(-\frac1{\sqrt2},\frac12\right).
$$

El punto estacionario $x=0$ tiene un valor mayor y no es mínimo global; además, $G''(0)=-2<0$ lo identifica como máximo local. La ecuación $G'=0$ había seleccionado los tres puntos sin clasificarlos.

## G. Desafío de síntesis

### Solución 3.30 (`EDC-C03-SOL-030`)

Si $a=b$, ambos miembros son cero. Para $a\ne b$, trabajamos sobre el segmento que los une, cualquiera que sea su orden. Como $f$ es dos veces derivable en un intervalo abierto que contiene ese segmento, $f$ y $f'$ son continuas en los segmentos cerrados donde las aplicaremos, y ambas son derivables en sus interiores.

La primera aplicación del valor medio, a $f$, produce un punto $c$ estrictamente entre $a$ y $b$ con

$$
f(b)-f(a)=f'(c)(b-a).
$$

El error frente a la recta tangente en $a$ depende entonces de la diferencia entre la pendiente en $c$ y la pendiente inicial. Restando $f'(a)(b-a)$ y tomando valores absolutos,

$$
|f(b)-f(a)-f'(a)(b-a)|=|f'(c)-f'(a)|\,|b-a|.
$$

La segunda aplicación del valor medio, a $f'$ entre $a$ y $c$, proporciona un $d$ entre esos puntos. Este segmento está contenido en el primero y la cota de $f''$ vale en él:

$$
|f'(c)-f'(a)|=|f''(d)|\,|c-a|\le M|b-a|.
$$

Usamos aquí $|c-a|\le|b-a|$, porque $c$ es intermedio. Al sustituir la cota en la igualdad anterior obtenemos $|f(b)-f(a)-f'(a)(b-a)|\le M|b-a|^2$.

La constante no tiene que ser óptima. Para $f(x)=x^2$ tenemos $|f''|=2$, pero el error exacto en torno a $a$ es $(b-a)^2$, igual a $M(b-a)^2/2$ si elegimos $M=2$. Cuando $a\ne b$, resulta estrictamente menor que la cota obtenida por las dos aplicaciones del valor medio. El resto de Taylor de C09 permitirá estudiar cotas más precisas.

---

**Control de cobertura:** treinta ejercicios `EDC-C03-EXR-001--030` desarrollados con sus treinta entradas `EDC-C03-SOL-001--030`. Los problemas se apoyan en C00–C03, sin usar integrales, el Teorema Fundamental del Cálculo ni Taylor.
