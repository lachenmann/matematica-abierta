---
title: Capítulo 1 — Ejercicios
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
source-id: EDC-C01-EJERCICIOS
source-sha256: 037c8444e589768ba4ec1c512afa77439b1334b4493316b78da1bbcd88ee725d
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-01.html) · [Ejercicios](capitulo-01-ejercicios.html) · [Soluciones](capitulo-01-soluciones.html)

Los enunciados son independientes de sus desarrollos, reunidos en [Soluciones del capítulo 1](capitulo-01-soluciones.html). Los cálculos se resuelven desde los cocientes incrementales: se pide justificar cada límite y comprobar el dominio en el que las operaciones están permitidas. Los identificadores `EXR` y `SOL` se corresponden por los tres dígitos finales.

## A. Comprender la pregunta

**Ejercicio 1.1 (`EDC-C01-EXR-001`).** Para $f(x)=x^2$, escriba la pendiente de la secante entre los puntos de abscisas $3$ y $3+h$, con $h\ne0$. Determine su límite y la ecuación de la recta tangente en $x=3$. Indique en qué operación sería ilegítimo sustituir $h=0$.

**Ejercicio 1.2 (`EDC-C01-EXR-002`).** Una posición medida en metros, en función del tiempo en segundos, está dada por $s(t)=10+4t-t^2$, $t\ge0$. Calcule la velocidad media entre $t=2$ y $t=2+h$, cuando ambos tiempos pertenecen al dominio. Halle la velocidad instantánea en $t=2$ y la velocidad lateral derecha en $t=0$. Indique sus unidades e interprete el signo.

**Ejercicio 1.3 (`EDC-C01-EXR-003`).** La función $f(x)=(x^2-1)/(x-1)$ está definida para $x\ne1$. ¿Tiene sentido preguntar por $f'(1)$ en ese dominio? Construya una extensión continua $F:\mathbb R\to\mathbb R$ de $f$ y calcule $F'(1)$ mediante la definición. Distinga la función inicial y su extensión.

**Ejercicio 1.4 (`EDC-C01-EXR-004`).** La curva $y=x^3$ pasa por el origen. Determine por definición la pendiente de su tangente allí. Compruebe que la curva tiene puntos a ambos lados de su recta tangente. Explique por qué «no cruzar la curva» no es una definición válida de tangencia diferencial.

## B. Calcular por definición

**Ejercicio 1.5 (`EDC-C01-EXR-005`).** Para $f(x)=x^3$, desarrolle el cociente incremental en un punto real arbitrario $a$ y obtenga $f'(a)$. Escriba explícitamente el término de error del modelo lineal en $a$.

**Ejercicio 1.6 (`EDC-C01-EXR-006`).** Determine la derivada de $f(x)=1/x$ en $a=2$ directamente desde el cociente incremental. Obtenga la recta tangente y compruebe que todos los denominadores empleados son no nulos en un entorno apropiado de $h=0$.

**Ejercicio 1.7 (`EDC-C01-EXR-007`).** Para $f(x)=|x-3|$, calcule las razones de cambio por derecha e izquierda en $a=3$. Determine la continuidad y la derivabilidad en ese punto, explicando por qué son propiedades diferentes.

**Ejercicio 1.8 (`EDC-C01-EXR-008`).** Sea $f(x)=x|x|$ en $\mathbb R$. Determine $f'(0)$ directamente. ¿Es posible que una función definida mediante expresiones distintas a cada lado tenga derivada en el punto de unión?

**Ejercicio 1.9 (`EDC-C01-EXR-009`).** Para

$$
f(x)=\begin{cases}x^2\sin(1/x),&x\ne0,\\0,&x=0,\end{cases}
$$

calcule $f'(0)$ y justifique el límite por encajonamiento. Compare con $g(x)=x\sin(1/x)$, $g(0)=0$: ¿tiene $g'(0)$?

## C. Examinar el dominio y las uniones

**Ejercicio 1.10 (`EDC-C01-EXR-010`).** Sean $a,b,c\in\mathbb R$ y

$$
f(x)=\begin{cases}2x+a,&x<0,\\bx+c,&x\ge0.\end{cases}
$$

Encuentre las condiciones necesarias y suficientes de continuidad y derivabilidad en cero. Cuando exista, indique la derivada.

**Ejercicio 1.11 (`EDC-C01-EXR-011`).** Sea $k\in\mathbb R$ y

$$
f(x)=\begin{cases}x^2,&x<0,\\kx,&x\ge0.\end{cases}
$$

Pruebe que $f$ es continua en cero para todo $k$. ¿Para qué valores de $k$ es derivable allí?

**Ejercicio 1.12 (`EDC-C01-EXR-012`).** Sea

$$
f(x)=\begin{cases}x^2,&x\le1,\\2x-1,&x>1.\end{cases}
$$

Compruebe la continuidad en $x=1$ y calcule las derivadas laterales desde la definición. ¿Existe la derivada bilateral? ¿Qué sucede con la segunda diferencia $[f(1+h)-f(1)-2h]/h^2$ desde cada lado?

**Ejercicio 1.13 (`EDC-C01-EXR-013`).** Defina $f(0)=0$ y $f(x)=|x|/x$ para $x\ne0$. Estudie la continuidad y la derivabilidad en cero. Evite asignar un valor al cociente $|x|/x$ en el origen.

**Ejercicio 1.14 (`EDC-C01-EXR-014`).** Para $f:[0,\infty)\to\mathbb R$, $f(x)=\sqrt x$, determine si existe una derivada **lateral derecha finita** en $0$. Utilice los incrementos $h_n=1/n^2$ y explique por qué no corresponde preguntar por una derivada bilateral según nuestra definición interior.

## D. Detectar afirmaciones falsas

**Ejercicio 1.15 (`EDC-C01-EXR-015`).** «Toda tangente a una curva la toca en un solo punto y no la atraviesa». Refute ambos supuestos como criterio general de tangencia diferencial: basta un ejemplo para refutar la prohibición de atravesarla y explicar por qué contar intersecciones globales no establece una propiedad local.

**Ejercicio 1.16 (`EDC-C01-EXR-016`).** «Si $f$ es continua en $a$, entonces existe $f'(a)$». Dé un contraejemplo continuo en toda la recta y muestre el fallo de los límites laterales.

**Ejercicio 1.17 (`EDC-C01-EXR-017`).** «Si $f'(a)=0$, entonces $a$ es máximo o mínimo local». Dé un contraejemplo y demuestre las dos desigualdades que descartan ambos tipos de extremo.

**Ejercicio 1.18 (`EDC-C01-EXR-018`).** «Si $f'(a)>0$, entonces $f(x)>f(a)$ para **todo** $x>a$ del dominio». Construya un polinomio que refute el alcance global de esta frase. Formule la afirmación **local** que sí se probó en el capítulo.

## E. Demostrar con precisión

**Ejercicio 1.19 (`EDC-C01-EXR-019`).** Demuestre directamente, sin usar una regla de derivación, que $f'(a)=m$ equivale a

$$
\lim_{h\to0}\frac{|f(a+h)-f(a)-mh|}{|h|}=0
$$

para $a$ interior al dominio. Explique por qué $m$ es único.

**Ejercicio 1.20 (`EDC-C01-EXR-020`).** Pruebe que, si $f$ es derivable en un punto interior $a$, existen $\delta>0$ y $K>0$ tales que

$$
|f(a+h)-f(a)|\le K|h|\qquad(|h|<\delta).
$$

¿Es cierta la recíproca? Justifique la respuesta con una función concreta.

**Ejercicio 1.21 (`EDC-C01-EXR-021`).** Sean $a\in\mathbb R$ y $f(x)=1/(1+x^2)$. Partiendo de la diferencia $f(a+h)-f(a)$, y sin invocar la regla del cociente de C02, demuestre que

$$
f'(a)=-\frac{2a}{(1+a^2)^2}.
$$

Indique por qué los denominadores nunca se anulan.

## F. Investigar y generalizar

**Ejercicio 1.22 (`EDC-C01-EXR-022`).** Dada la parábola $y=x^2$ y un punto fijo $P=(b,c)$ del plano, determine cuántas **rectas tangentes diferenciales** a esa parábola pasan por $P$. Clasifique los casos según la comparación entre $c$ y $b^2$. Justifique algebraicamente la respuesta y explique por qué una tangente puede cortar de nuevo la curva en otros problemas, aunque aquí no lo haga.

---

**Protocolo de resolución.** Todas las soluciones están desarrolladas en [EDC-C01-SOLUCIONES](capitulo-01-soluciones.html). Ningún ejercicio precisa Rolle, el teorema del valor medio, las reglas generales de C02 ni un teorema del cálculo integral. Si un paso utiliza límites, debe poder justificarse con el capítulo 0.
