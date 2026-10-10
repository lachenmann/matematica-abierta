## Laboratorio de límites secuenciales {#sec-t1-c04-10}

Hasta aquí hemos construido las herramientas del capítulo una por una. Sabemos traducir «acercarse» a una afirmación $\varepsilon$–$N$; negar correctamente una convergencia; usar unicidad, acotación, álgebra y orden; reconocer cuándo conviene aplicar el teorema del sándwich; obtener convergencia a partir de monotonía y completitud; analizar recurrencias; y distinguir un límite real de un escape hacia $+\infty$ o $-\infty$.

Ahora cambia la tarea.

En las seis estaciones que siguen **no introduciremos teoría nueva**. El problema será decidir qué herramienta conviene usar, justificar por qué puede usarse y detectar los pasos que una solución demasiado rápida podría ocultar.

Conviene adoptar este protocolo general:

$$
\boxed{
\text{leer el objetivo}
\to
\text{identificar la estructura de la cola}
\to
\text{elegir la herramienta}
\to
\text{probar}
\to
\text{auditar hipótesis y dependencias}
}
$$

La pregunta ya no será solamente

> ¿puedo calcular este límite?,

sino también

> **¿qué teorema o definición convierte la información disponible en control de toda una cola?**

### Estación 1 — Convertir un candidato en una prueba $\varepsilon$–$N$

Consideremos

$$
a_n=\frac{4n-1}{2n+3},
\qquad n\ge0.
$$

Una manipulación informal de los términos dominantes sugiere

$$
\frac{4n-1}{2n+3}\approx\frac{4n}{2n}=2.
$$

**Problema.** Demostrar directamente desde la definición que

$$
a_n\to2,
$$

fabricando un umbral $N(\varepsilon)$ y señalando dónde aparece cada cuantificador.

#### Diagnóstico

El candidato está dado. Por tanto, la definición nos exige controlar

$$
|a_n-2|.
$$

Antes de escribir «sea $\varepsilon>0$», conviene hacer el cálculo de búsqueda: simplificar el error hasta descubrir qué condición sobre $n$ bastaría para hacerlo menor que $\varepsilon$.

#### Búsqueda del umbral

Tenemos

$$
\begin{aligned}
\left|\frac{4n-1}{2n+3}-2\right|
&=
\left|\frac{4n-1-2(2n+3)}{2n+3}\right|\\
&=
\left|\frac{-7}{2n+3}\right|\\
&=
\frac7{2n+3}.
\end{aligned}
$$

Queremos garantizar

$$
\frac7{2n+3}<\varepsilon.
$$

Sería suficiente imponer una condición un poco más fuerte y más cómoda:

$$
2n>\frac7\varepsilon,
$$

es decir,

$$
n>\frac7{2\varepsilon}.
$$

La propiedad arquimediana nos permite producir un natural que supere esa cantidad real.

#### Demostración

Sea $\varepsilon>0$ arbitrario. Por la propiedad arquimediana, elegimos $N\in\mathbb N$ tal que

$$
N>\frac7{2\varepsilon}.
$$

Sea ahora $n\ge N$. Entonces

$$
2n+3>2n\ge2N>\frac7\varepsilon.
$$

Como todas las cantidades son positivas,

$$
\frac7{2n+3}<\varepsilon.
$$

Por consiguiente,

$$
\left|\frac{4n-1}{2n+3}-2\right|<\varepsilon
$$

para todo $n\ge N$. Como $\varepsilon>0$ era arbitrario,

$$
\boxed{
\frac{4n-1}{2n+3}\to2.
}
$$

#### Lectura de la solución

La prueba contiene exactamente la arquitectura

$$
\forall\varepsilon>0
\;\exists N
\;\forall n\ge N.
$$

- El adversario lógico elige $\varepsilon$.
- Nosotros respondemos con un $N$ que puede depender de $\varepsilon$.
- Después ese mismo $N$ debe controlar **todos** los índices posteriores.

La desigualdad preliminar

$$
n>\frac7{2\varepsilon}
$$

no es todavía la demostración: es la **búsqueda** que nos permite diseñar el testigo existencial $N$.

Podríamos obtener el mismo límite más rápidamente mediante el álgebra de límites de @prp-t1-0021. Aquí hemos evitado deliberadamente ese atajo porque el objetivo de la estación era reconstruir la lógica elemental sobre la que descansa toda la teoría.

### Estación 2 — Negar una convergencia sin cambiar el orden de los cuantificadores

Sea

$$
b_n=(-1)^n+\frac1{n+1}.
$$

Algunos términos son positivos y otros negativos, y el término adicional $1/(n+1)$ se hace pequeño. Alguien podría mirar esa pequeñez y conjeturar erróneamente que

$$
b_n\to0.
$$

**Problema.** Refutar ese candidato directamente desde la negación de la definición de convergencia.

#### Diagnóstico

Para probar

$$
b_n\not\to0
$$

no debemos demostrar que «muchos términos» quedan lejos de cero. Necesitamos una tolerancia fija $\varepsilon_0>0$ que ninguna cola consiga satisfacer por completo:

$$
\exists\varepsilon_0>0
\;\forall N
\;\exists n\ge N:
|b_n|\ge\varepsilon_0.
$$

La alternancia sugiere elegir siempre un índice par suficientemente tardío.

#### Solución

Tomemos

$$
\varepsilon_0=\frac12.
$$

Sea $N\in\mathbb N$ arbitrario. Elegimos

$$
n=2N.
$$

Entonces $n$ es par y además $n\ge N$. Por tanto,

$$
(-1)^n=1,
$$

y

$$
b_n
=
1+\frac1{2N+1}
>1.
$$

En particular,

$$
|b_n|>1>\frac12=\varepsilon_0.
$$

Así, para todo umbral $N$ encontramos un índice $n\ge N$ que queda fuera del intervalo

$$
\left(-\frac12,\frac12\right).
$$

Por la negación de la definición,

$$
\boxed{b_n\not\to0.}
$$

#### Qué demuestra y qué no demuestra

La conclusión excluye **el candidato $0$**. Por sí sola no demuestra todavía que $(b_n)$ diverja, porque podría existir otro número real como límite.

Esta separación reproduce una distinción de §4.2:

$$
\boxed{
\text{refutar un candidato}
\neq
\text{refutar todos los candidatos}.
}
$$

La estación se concentra en una habilidad lógica más básica: leer correctamente

$$
\forall N\;\exists n\ge N
$$

como «por lejos que avancemos, todavía reaparece una violación», y no confundirla con

$$
\exists N\;\forall n\ge N,
$$

que expresa estabilidad de toda una cola.

### Estación 3 — Abrir una prueba algebraica y encontrar los controles ocultos

Supongamos que

$$
x_n\to2
\qquad\text{y}\qquad
y_n\to-1.
$$

El álgebra de límites permite concluir inmediatamente

$$
x_ny_n\to-2
$$

y

$$
\frac{x_n}{y_n}\to-2.
$$

Pero ahora queremos mirar **dentro** de esas dos conclusiones.

**Problema.** Reconstruir qué controles hacen posibles las pruebas del producto y del cociente. En particular:

1. explicar por qué la prueba del producto necesita una cota para uno de los factores;
2. explicar por qué la prueba del cociente necesita separar $y_n$ de cero.

#### Primera reparación: controlar el producto

La diferencia respecto del límite esperado puede escribirse como

$$
\begin{aligned}
x_ny_n-(-2)
&=x_ny_n+2\\
&=x_n(y_n+1)-(x_n-2).
\end{aligned}
$$

Por la desigualdad triangular,

$$
|x_ny_n+2|
\le
|x_n|\,|y_n+1|+|x_n-2|.
$$

Aquí aparece el punto delicado. Sabemos que

$$
|y_n+1|\to0,
$$

pero ese factor está multiplicado por $|x_n|$. Para convertir la pequeñez de $|y_n+1|$ en pequeñez del producto necesitamos impedir que $|x_n|$ crezca sin control.

Como $x_n\to2$, existe una cola en la que

$$
|x_n-2|<1.
$$

En esa cola,

$$
|x_n|
\le
|x_n-2|+2
<3.
$$

Ya tenemos la cota que faltaba.

Sea ahora $\varepsilon>0$. Elegimos índices suficientemente grandes para que simultáneamente

$$
|x_n|<3,
$$

$$
|y_n+1|<\frac\varepsilon6,
$$

y

$$
|x_n-2|<\frac\varepsilon2.
$$

Tomando el máximo de los tres umbrales correspondientes, todas las condiciones valen en una misma cola. Entonces

$$
\begin{aligned}
|x_ny_n+2|
&\le
|x_n|\,|y_n+1|+|x_n-2|\\
&<
3\frac\varepsilon6+\frac\varepsilon2\\
&=\varepsilon.
\end{aligned}
$$

Así reaparece, desde dentro de la prueba, la razón estructural por la que la convergencia implica acotación: **un factor que tiende a cero solo puede controlar un producto si el otro factor no se escapa**.

#### Segunda reparación: controlar el cociente

Ahora examinemos

$$
\frac{x_n}{y_n}.
$$

Antes de estimar el error debemos garantizar que el denominador no se acerque a cero. Como

$$
y_n\to-1,
$$

podemos exigir

$$
|y_n+1|<\frac12.
$$

Entonces

$$
-\frac32<y_n<-\frac12,
$$

y por tanto

$$
|y_n|>\frac12.
$$

En esa cola el cociente está bien definido y además

$$
\frac1{|y_n|}<2.
$$

Ahora calculamos

$$
\begin{aligned}
\left|\frac{x_n}{y_n}+2\right|
&=
\frac{|x_n+2y_n|}{|y_n|}\\
&=
\frac{|(x_n-2)+2(y_n+1)|}{|y_n|}\\
&\le
\frac{|x_n-2|+2|y_n+1|}{|y_n|}.
\end{aligned}
$$

Sea $\varepsilon>0$. En una cola común podemos exigir

$$
|y_n+1|<\frac12,
$$

$$
|x_n-2|<\frac\varepsilon4,
$$

y

$$
|y_n+1|<\frac\varepsilon8.
$$

Entonces

$$
\begin{aligned}
\left|\frac{x_n}{y_n}+2\right|
&<
2\left(\frac\varepsilon4+2\frac\varepsilon8\right)\\
&=\varepsilon.
\end{aligned}
$$

Por tanto,

$$
\frac{x_n}{y_n}\to-2.
$$

#### Lectura de la solución

Las dos pruebas tienen obstáculos diferentes:

$$
\boxed{
\begin{array}{c}
\text{producto: controlar un factor que multiplica el error;}\\[4pt]
\text{cociente: impedir que el denominador haga explotar el error.}
\end{array}
}
$$

El teorema algebraico de @prp-t1-0021 comprime estos razonamientos para reutilizarlos. Esta estación muestra qué información permanece escondida cuando escribimos simplemente «por el álgebra de límites».

### Estación 4 — Cuando la oscilación no necesita tener límite

Consideremos

$$
u_n=\frac{2\sin n-\cos n}{n+1}.
$$

**Problema.** Determinar el límite sin suponer que las sucesiones $(\sin n)$ o $(\cos n)$ tengan límite.

#### Diagnóstico

La expresión contiene dos factores oscilantes. Intentar aplicar el álgebra de límites término a término nos obligaría a conocer primero límites para $\sin n$ y $\cos n$.

Pero no necesitamos esa información.

Lo que sí sabemos es

$$
|\sin n|\le1,
\qquad
|\cos n|\le1.
$$

La pregunta correcta no es, por tanto,

> ¿a qué número se acercan el seno y el coseno?,

sino

> ¿podemos encerrar toda la expresión entre cantidades cuya magnitud tienda a cero?

Eso apunta al teorema del sándwich.

#### Solución

Por desigualdad triangular,

$$
|2\sin n-\cos n|
\le
2|\sin n|+|\cos n|
\le3.
$$

Por tanto,

$$
|u_n|
=
\frac{|2\sin n-\cos n|}{n+1}
\le
\frac3{n+1}.
$$

Ya sabemos que

$$
\frac1{n+1}\to0,
$$

así que, por multiplicación por el escalar $3$,

$$
\frac3{n+1}\to0.
$$

La forma absoluta del teorema del sándwich @prp-t1-0023 da entonces

$$
\boxed{
u_n\to0.}
$$

#### Lectura de la solución

La oscilación no fue eliminada: fue **dominada**.

$$
\boxed{
\text{factor oscilante acotado}
\times
\text{factor que tiende a }0
\longrightarrow
\text{producto que tiende a }0.
}
$$

Esta arquitectura es más importante que el ejemplo trigonométrico concreto. Cuando una parte de una expresión se resiste a tener un comportamiento simple, conviene preguntar si basta controlar su magnitud.

### Estación 5 — Detectar cuándo la completitud produce el límite

Definamos

$$
a_n=\sqrt{2-\frac1{n+1}},
\qquad n\ge0.
$$

**Problema.** Demostrar que $(a_n)$ converge y determinar su límite **sin utilizar continuidad de la raíz cuadrada**.

#### Diagnóstico

Es tentador escribir

$$
2-\frac1{n+1}\to2
$$

y después afirmar inmediatamente

$$
\sqrt{2-\frac1{n+1}}\to\sqrt2.
$$

Pero esa segunda inferencia sería precisamente una aplicación de continuidad de $x\mapsto\sqrt x$, noción que todavía no pertenece a este capítulo.

Debemos separar las dos preguntas:

1. ¿por qué existe un límite real para $(a_n)$?;
2. una vez asegurada su existencia, ¿cómo identificamos su valor usando únicamente el álgebra ya demostrada?

La forma de la sucesión sugiere que sus términos crecen y permanecen por debajo de $\sqrt2$.

#### Monotonía y cota

Para todo $n\ge0$,

$$
0<\frac1{n+1}\le1,
$$

de modo que

$$
1\le2-\frac1{n+1}<2.
$$

Por tanto,

$$
1\le a_n<\sqrt2.
$$

Así, $(a_n)$ está acotada superiormente por $\sqrt2$.

Además,

$$
\frac1{n+2}<\frac1{n+1},
$$

por lo que

$$
2-\frac1{n+2}
>
2-\frac1{n+1}.
$$

La raíz cuadrada es estrictamente creciente sobre $[0,\infty)$, de modo que

$$
a_{n+1}>a_n.
$$

La sucesión es, pues, creciente y acotada superiormente.

#### Existencia del límite

Por el teorema de convergencia monótona @thm-t1-0010, existe $L\in\mathbb R$ tal que

$$
a_n\to L.
$$

Aquí está el paso en el que actúa la completitud de $\mathbb R$: el teorema de convergencia monótona se demostró tomando el supremo de la imagen de la sucesión.

Además, como todos los términos satisfacen $a_n\ge1$, el límite producido por el teorema es no negativo; de hecho,

$$
1\le L\le\sqrt2.
$$

#### Identificación sin continuidad

La definición de $a_n$ nos da la identidad exacta

$$
a_n^2
=
2-\frac1{n+1}.
$$

Como $a_n\to L$, el álgebra de límites implica

$$
a_n^2\to L^2.
$$

Por otra parte,

$$
\frac1{n+1}\to0,
$$

y por tanto

$$
2-\frac1{n+1}\to2.
$$

Las dos sucesiones de ambos lados de la identidad son la misma término a término, así que sus límites deben coincidir. Por unicidad,

$$
L^2=2.
$$

Como $L\ge0$, la unicidad de la raíz no negativa demostrada en `T1-C02` obliga a

$$
L=\sqrt2.
$$

Concluimos

$$
\boxed{
\sqrt{2-\frac1{n+1}}
\to
\sqrt2.
}
$$

#### Dónde estaba la completitud

La prueba tiene dos capas claramente separadas:

$$
\boxed{
\text{monotonía + cota + completitud}
\to
\text{existencia de }L
\to
\text{álgebra}
\to
\text{identificación de }L.
}
$$

No hemos pasado una raíz cuadrada a través del símbolo de límite. Primero obtuvimos **existencia** mediante el orden completo de $\mathbb R$ y solo después utilizamos una identidad algebraica para averiguar quién era el límite.

### Estación 6 — Auditar una recurrencia antes de resolver su ecuación de punto fijo

Sea

$$
u_0=0,
\qquad
u_{n+1}=\frac{u_n+3}{2}.
$$

Una solución apresurada podría decir:

> «Si $u_n\to L$, entonces $L=(L+3)/2$, de donde $L=3$. Por tanto, $u_n\to3$.»

**Problema.** Localizar el fallo lógico y reparar completamente la demostración sin utilizar continuidad.

#### Diagnóstico del argumento defectuoso

La primera frase comienza con una hipótesis condicional:

$$
\text{si }u_n\to L.
$$

La ecuación

$$
L=\frac{L+3}{2}
$$

solo puede servir para **identificar un candidato después de saber que el límite existe**. Resolverla no demuestra que la sucesión converja.

La prueba correcta debe seguir el protocolo de §4.8:

$$
\boxed{
\text{bien definida}
\to
\text{región invariante}
\to
\text{monotonía}
\to
\text{existencia}
\to
\text{identificación}.
}
$$

#### Paso 1: la recurrencia está bien definida y preserva una región

Demostraremos por inducción que

$$
0\le u_n<3
$$

para todo $n\ge0$.

Para $n=0$,

$$
u_0=0,
$$

de modo que la afirmación es verdadera.

Supongamos ahora

$$
0\le u_n<3.
$$

Entonces

$$
3\le u_n+3<6,
$$

y al dividir por $2$,

$$
\frac32\le u_{n+1}<3.
$$

En particular,

$$
0\le u_{n+1}<3.
$$

Por inducción, la región $[0,3)$ es invariante bajo la recurrencia.

#### Paso 2: monotonía

Para todo $n$,

$$
\begin{aligned}
u_{n+1}-u_n
&=\frac{u_n+3}{2}-u_n\\
&=\frac{3-u_n}{2}.
\end{aligned}
$$

Como $u_n<3$,

$$
u_{n+1}-u_n>0.
$$

Así, $(u_n)$ es estrictamente creciente.

Además, la región invariante ya nos dio la cota superior

$$
u_n<3.
$$

#### Paso 3: existencia por completitud

La sucesión es creciente y acotada superiormente. Por @thm-t1-0010,

$$
u_n\to L
$$

para algún $L\in\mathbb R$.

Solo ahora tenemos derecho a buscar una ecuación para $L$.

#### Paso 4: identificación mediante desplazamiento y álgebra

Por la estabilidad bajo desplazamiento de índices @prp-t1-0019,

$$
u_{n+1}\to L.
$$

La recurrencia satisface

$$
2u_{n+1}=u_n+3.
$$

Aplicando únicamente el álgebra de límites,

$$
2L=L+3.
$$

Por tanto,

$$
L=3.
$$

Concluimos

$$
\boxed{u_n\to3.}
$$

#### Lectura de la solución

La ecuación de punto fijo era correcta; lo incorrecto era su **posición lógica** dentro del argumento.

$$
\boxed{
\text{ecuación del candidato}
\not\Longrightarrow
\text{existencia del límite}.
}
$$

El orden correcto es

$$
\boxed{
\text{probar que el límite existe}
\longrightarrow
\text{usar la recurrencia para identificarlo}.
}
$$

Esta distinción será especialmente importante más adelante, cuando las recurrencias sean suficientemente complejas como para poseer varios puntos fijos o para no converger a ninguno de ellos.

### Un mapa de decisiones para problemas de sucesiones

Las seis estaciones muestran que «calcular un límite» no designa una única técnica. Antes de hacer álgebra conviene diagnosticar qué tipo de información tenemos.

Un primer mapa puede organizarse así:

$$
\boxed{
\begin{array}{c}
\text{¿definición directa?}\\
\downarrow\\
\text{¿álgebra?}\quad\text{¿sándwich?}\quad\text{¿monotonía + cota?}\\
\downarrow\\
\text{¿recurrencia?}\quad\text{¿límite infinito?}
\end{array}
}
$$

Podemos convertirlo en preguntas operativas.

**Si nos dan un candidato real $L$**, preguntamos primero si podemos estimar directamente

$$
|a_n-L|.
$$

Cuando el error se reduce a una expresión elemental en $n$, una prueba $\varepsilon$–$N$ puede ser la ruta más transparente.

**Si la sucesión está construida a partir de otras cuyos límites ya conocemos**, el álgebra de @prp-t1-0021 puede comprimir el trabajo. Pero debemos auditar sus hipótesis: en productos aparece acotación y en cocientes el denominador debe quedar eventualmente separado de cero.

**Si aparece una oscilación acotada multiplicada por algo pequeño**, conviene buscar una desigualdad en valor absoluto y aplicar el sándwich en vez de intentar asignar un límite a cada factor.

**Si no conocemos el candidato pero la sucesión tiene una dirección de movimiento**, preguntamos si es monótona y está acotada en la dirección adecuada. Si ambas respuestas son afirmativas, la completitud puede producir el límite mediante @thm-t1-0010.

**Si la sucesión está dada por recurrencia**, no comenzamos resolviendo una ecuación de punto fijo. Primero debemos demostrar que la regla está bien definida, encontrar una región invariante o cotas, estudiar monotonía y obtener existencia. Solo después usamos desplazamiento de índices y álgebra para identificar el límite.

**Si los términos parecen crecer sin cota**, debemos distinguir no acotación de límite infinito. Para probar

$$
a_n\to+\infty
$$

o

$$
a_n\to-\infty,
$$

la definición exige superar o descender cualquier barrera con **toda una cola**, no solo con términos arbitrariamente grandes en magnitud.

**Si queremos refutar una convergencia**, buscamos una tolerancia fija que reaparezca violada arbitrariamente lejos. La estructura correcta es

$$
\exists\varepsilon_0>0
\;\forall N
\;\exists n\ge N.
$$

### Qué debe poder hacer ahora el lector

Al terminar este laboratorio, una solución completa ya no debería consistir únicamente en una cadena de manipulaciones simbólicas. Antes de calcular, debemos ser capaces de decir:

- qué afirmación cuantificada intentamos probar o negar;
- qué información pertenece solo a un prefijo y qué información controla una cola;
- si estamos usando una definición o un teorema ya demostrado;
- cuáles son las hipótesis delicadas de ese teorema;
- si la existencia del límite está demostrada o solo hemos encontrado un candidato;
- dónde entra la completitud, cuando entra;
- y qué herramientas posteriores estamos evitando para no razonar circularmente.

El capítulo comenzó preguntando cómo expresar rigurosamente lo que ocurre «a partir de algún momento y para siempre después». Después de estas seis estaciones, esa pregunta ya dispone de un repertorio de respuestas diferentes pero coordinadas:

$$
\boxed{
\begin{array}{c}
\varepsilon\text{–}N,\\
\text{álgebra y orden},\\
\text{sándwich},\\
\text{monotonía + completitud},\\
\text{recurrencias},\\
M\text{–}N\text{ para límites infinitos}.
\end{array}
}
$$

En §4.11 ese repertorio dejará de estar organizado por estaciones. El banco final mezclará reconocimiento, prueba directa, diagnóstico, contraejemplos, descubrimiento guiado y desafíos de síntesis. La tarea será elegir la herramienta adecuada sin que el enunciado anuncie de antemano cuál es.

