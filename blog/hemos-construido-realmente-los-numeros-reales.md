---
title: "¿Hemos construido realmente los números reales?"
subtitle: "Wildberger y una matemática que no oculte sus fundamentos"
description: "Una lectura crítica de las objeciones de Norman J. Wildberger a los números reales, ZFC y el axioma de elección, y una propuesta constructiva para enriquecer el rigor matemático."
content-id: MA-ART-0002
content-type: article
status: published
date-created: 2026-09-15
date-modified: 2026-09-15
areas:
  - fundamentos
  - analisis
  - logica
level: intermedio
topics:
  - numeros-reales
  - dedekind
  - constructivismo
  - computabilidad
  - zfc
  - axioma-de-eleccion
  - wildberger
  - fundamentos-de-la-matematica
related:
  - Tratado de análisis
  - Tratado de álgebra
provenance:
  type: original-synthesis
  sources:
    - Norman J. Wildberger, "Real numbers: A critique and way forward" (2015)
    - Norman J. Wildberger, "Set Theory: Should You Believe?" (2015)
    - Errett Bishop, "Foundations of Constructive Analysis" (1967)
    - Stanford Encyclopedia of Philosophy, "Constructive Mathematics"
    - Stanford Encyclopedia of Philosophy, "The Axiom of Choice"
license: GFDL-1.3-or-later
---

Hay una pregunta que rara vez aparece después de una construcción rigurosa de los números reales:

$$
\boxed{\text{¿Qué significa exactamente que los hemos construido?}}
$$

Podemos definir los reales mediante cortaduras de Dedekind. Podemos obtenerlos como clases de equivalencia de sucesiones de Cauchy. Podemos definir sobre ellos suma, producto y orden, y demostrar que forman un cuerpo ordenado completo.

Todo eso constituye matemática clásica perfectamente legítima dentro de su marco formal.

Pero aún podemos preguntar:

- ¿qué clase de objeto hemos construido?;
- ¿cómo está especificado?;
- ¿puede representarse mediante información finita?;
- ¿podemos calcular con él?;
- ¿podemos decidir cuándo dos de estos objetos son iguales?;
- ¿qué principios lógicos y conjuntistas hemos utilizado para demostrar que existe?

Estas preguntas están en el centro de las críticas que Norman J. Wildberger ha dirigido contra la teoría moderna de conjuntos, los números reales y el uso del infinito actual. Su lenguaje suele ser deliberadamente provocador, y algunas de sus conclusiones van mucho más lejos de lo que la matemática estándar está dispuesta a conceder. Sin embargo, descartar por ese motivo todas sus preguntas sería un error.

En *Real numbers: A critique and way forward* (2015), Wildberger cuestiona las presentaciones habituales mediante decimales infinitos, sucesiones de Cauchy y cortaduras de Dedekind. Su preocupación recurrente es que hablamos de objetos infinitos sin prestar suficiente atención a la manera en que tales objetos pueden especificarse o manipularse mediante información finita.

No es necesario aceptar su programa finitista para reconocer que la pregunta merece una respuesta mejor que «así se hace en la matemática estándar».

La ortodoxia no constituye una demostración.

## 1. ¿Qué significa «construir»?

Supongamos que definimos

$$
\mathbb R_D
$$

como la colección de las cortaduras de Dedekind de $\mathbb Q$.

Dentro de una teoría clásica de conjuntos suficientemente fuerte podemos definir rigurosamente qué es una cortadura, definir las operaciones y el orden, y demostrar finalmente que

$$
(\mathbb R_D,+_D,\cdot_D,\le_D)
$$

es un cuerpo ordenado completo.

En un sentido formal hemos construido $\mathbb R$.

Pero la palabra *construcción* puede ocultar varias nociones diferentes:

$$
\begin{aligned}
&\text{existencia formal},\\
&\text{definibilidad},\\
&\text{especificación finita},\\
&\text{construcción efectiva},\\
&\text{computabilidad}.
\end{aligned}
$$

Estas nociones no son equivalentes.

Una demostración clásica de

$$
\exists x\,P(x)
$$

establece que existe un objeto que satisface cierta propiedad. No necesariamente proporciona un procedimiento para obtenerlo.

En buena parte de la matemática constructiva, en cambio, la afirmación de existencia está ligada a la posibilidad de producir un testigo o una construcción. La diferencia no es terminológica: cambia el contenido informativo de una prueba.

Por eso podemos reformular una de las intuiciones de Wildberger de un modo menos polémico:

$$
\boxed{\text{¿qué información contiene realmente nuestra prueba de existencia?}}
$$

Ésta sí es una pregunta matemática.

## 2. Una cortadura concreta y una cortadura arbitraria

Consideremos, por ejemplo, la cortadura asociada a $\sqrt2$:

$$
L_{\sqrt2}
=
\{q\in\mathbb Q:q<0\text{ o }q^2<2\}.
$$

Dado un racional $q$, podemos determinar mediante un cálculo finito si pertenece o no a esta cortadura.

Tenemos un procedimiento explícito.

Pero la definición clásica de número real mediante Dedekind no contiene solamente cortaduras de este tipo. Considera cortaduras arbitrarias que satisfacen determinadas propiedades estructurales.

Entonces aparece la pregunta:

$$
q\stackrel{?}{\in}L.
$$

La teoría clásica puede permitirnos hablar perfectamente bien de $L\subseteq\mathbb Q$ sin exigir que poseamos un algoritmo general que decida esa pertenencia.

Aquí Wildberger localiza una dificultad: ¿qué significa tratar esa totalidad infinita como un objeto matemático completamente dado cuando no disponemos de una especificación efectiva de su membresía?

La respuesta clásica es coherente:

> Un objeto matemático no tiene que ser computable para existir.

Pero observemos qué ha ocurrido. No hemos mostrado que la pregunta computacional carezca de sentido. Hemos adoptado un criterio de existencia más amplio.

Conviene que esta diferencia permanezca visible:

$$
\boxed{
\text{existencia clásica}
\neq
\text{decidibilidad}
\neq
\text{computabilidad}.
}
$$

## 3. Sucesiones de Cauchy: el problema reaparece

Otra construcción habitual define los reales mediante sucesiones racionales de Cauchy, identificando dos cuando su diferencia converge a cero:

$$
(a_n)\sim(b_n)
\iff
|a_n-b_n|\longrightarrow0.
$$

Un real aparece entonces como una clase de equivalencia

$$
[(a_n)].
$$

Nuevamente, la construcción clásica funciona.

Pero surgen preguntas adicionales.

¿Cómo está dada la sucesión?

¿Existe un algoritmo que produzca $a_n$ a partir de $n$?

¿Tenemos información efectiva sobre su convergencia?

Además de saber que

$$
\forall\varepsilon>0\;\exists N\;\forall m,n\ge N,
\qquad |a_m-a_n|<\varepsilon,
$$

¿podemos determinar un control explícito

$$
N=N(\varepsilon)?
$$

La diferencia es crucial.

Una sucesión puede estar bien definida y ser convergente en sentido clásico sin proporcionarnos información efectiva suficiente para calcular su límite.

El análisis computable ofrece ejemplos especialmente instructivos: existen sucesiones computables de racionales, crecientes y acotadas, cuyos límites no son reales computables. Las llamadas sucesiones de Specker muestran que

$$
\boxed{
\text{podemos calcular cada término}
\not\Rightarrow
\text{podemos calcular el límite}.
}
$$

Por eso la información efectiva de convergencia no es un detalle técnico. Forma parte del contenido computacional del teorema.

## 4. El problema empieza antes: ¿qué es una función?

La crítica de Wildberger retrocede todavía un paso más.

¿Qué es una función?

En teoría clásica de conjuntos puede definirse una función $f:A\to B$ como una relación que satisface

$$
\forall x\in A\;\exists!y\in B
\quad (x,y)\in f.
$$

Si las relaciones y los pares ordenados se representan mediante conjuntos, una función puede codificarse enteramente dentro de ZF o ZFC.

Por tanto, tomada literalmente, la afirmación «ZFC no puede definir funciones» sería demasiado fuerte. ZFC puede formalizar perfectamente funciones como objetos extensionales.

Pero la objeción interesante no termina ahí.

Consideremos

$$
f(n)=n^2+1.
$$

Podemos pensar esta función extensionalmente, como el conjunto de todos sus pares entrada-salida:

$$
\{(0,1),(1,2),(2,5),(3,10),\ldots\},
$$

o intensionalmente, mediante la regla:

$$
\boxed{\text{dado }n,\text{ elevarlo al cuadrado y sumar }1.}
$$

La primera descripción registra qué valores tiene la función.

La segunda proporciona un procedimiento para obtenerlos.

En matemática clásica, dos funciones con los mismos valores son la misma función extensional. En computación, teoría de tipos y otras perspectivas intensionales, puede ser relevante conservar también la forma de producir esos valores.

Así aparece una distinción fundamental:

$$
\boxed{
\text{función extensional}
\neq
\text{algoritmo que la realiza}.
}
$$

ZFC responde con precisión a la primera noción. Una crítica constructiva o computacional pregunta además por la segunda.

## 5. ZFC y el lenguaje en que hablamos de sus axiomas

Wildberger también critica la manera en que suelen presentarse los axiomas de la teoría de conjuntos. En *Set Theory: Should You Believe?* pregunta por nociones como «propiedad», «función» o «familia» cuando éstas aparecen informalmente al explicar los axiomas.

Aquí es importante no confundir la presentación pedagógica de ZFC con su formulación formal.

El lenguaje de primer orden de la teoría de conjuntos puede tomarse con una estructura extremadamente austera: esencialmente igualdad y la relación de pertenencia $\in$. Los esquemas de separación y reemplazo no necesitan introducir «propiedades» o «funciones» como nuevos objetos primitivos del lenguaje; se formulan mediante fórmulas de ese lenguaje.

Por ejemplo, reemplazo puede trabajar con una fórmula funcional $\varphi(x,y)$ que satisfaga una condición de unicidad apropiada. Ésta es una noción metalingüística de fórmula funcional, distinta de una función que ya sea un conjunto interno al universo.

Esa distinción muestra que varias críticas populares a ZFC confunden niveles formales diferentes.

Pero también revela algo que merece explicarse: la frase informal

> «una función es simplemente un conjunto de pares ordenados»

no cuenta toda la historia de cómo razonamos, definimos y presentamos funciones en la práctica matemática.

Precisar estos niveles no debilita la teoría de conjuntos. La hace más transparente.

## 6. El axioma de elección: existencia sin selección explícita

El axioma de elección hace todavía más visible la tensión entre existencia y construcción.

En una de sus formulaciones, permite afirmar la existencia de una función de elección para una familia apropiada de conjuntos no vacíos aun cuando no se haya especificado una regla uniforme concreta que realice las selecciones.

Su fuerza matemática es profunda. Entre los resultados equivalentes al axioma de elección completo, trabajando sobre ZF, está el enunciado:

$$
\boxed{\text{Todo espacio vectorial posee una base.}}
$$

La afirmación es perfectamente precisa dentro de la matemática clásica.

Pero desde una perspectiva constructiva podemos hacer una pregunta adicional. Cuando afirmamos que un espacio vectorial arbitrario $V$ posee una base $B$,

$$
\exists B\subseteq V,
$$

¿hemos construido efectivamente esa base?

No necesariamente.

Una vez más,

$$
\boxed{
\text{existencia clásica}
\neq
\text{procedimiento de construcción}.
}
$$

Esto no convierte al axioma de elección en incorrecto. Significa que una exposición rigurosa puede ganar mucho haciendo visible cuándo una conclusión depende de un principio de elección.

La regla metodológica adecuada no tiene por qué ser

$$
\text{«no usar elección»}.
$$

Puede ser algo más útil:

$$
\boxed{\text{no usar elección inadvertidamente}.}
$$

## 7. Lo que ZFC responde —y lo que no pretende responder

Debemos ser igualmente rigurosos con la matemática clásica y con Wildberger.

ZFC permite formalizar conjuntos, relaciones, funciones, sucesiones, cortaduras y las construcciones usuales de los reales. Si aceptamos ese marco, una cortadura infinita no constituye por sí misma una contradicción.

Por tanto, las objeciones de Wildberger no son normalmente refutaciones internas de ZFC.

Con frecuencia son objeciones al criterio de legitimidad matemática que ZFC permite adoptar.

De manera semejante,

$$
\text{no computable}
$$

no significa

$$
\text{inconsistente}.
$$

Cuando alguien exige que todo objeto matemático admita una especificación finita efectiva, está imponiendo una condición adicional que la teoría clásica no adopta en general.

Pero tampoco debemos pedirle a ZFC que responda preguntas que pertenecen a otro nivel.

ZFC puede responder:

> ¿puede formalizarse este objeto dentro de la teoría?

La teoría de la computabilidad pregunta además:

> ¿podemos calcularlo?

La matemática constructiva pregunta:

> ¿qué construcción contiene la prueba de existencia?

La teoría de la decisión pregunta:

> ¿podemos decidir esta propiedad mediante un procedimiento general?

La complejidad pregunta:

> aun cuando podamos calcularlo, ¿con qué recursos?

Son preguntas distintas.

Una exposición rigurosa debe evitar colapsarlas en una sola.

## 8. No necesitamos elegir entre Wildberger y la matemática clásica

Existe una falsa dicotomía frecuente:

$$
\text{matemática clásica}
\qquad\text{vs.}\qquad
\text{finitismo radical}.
$$

La tradición constructiva muestra que existe un territorio enorme entre ambos extremos.

Errett Bishop desarrolló una parte sustancial del análisis desde una orientación constructiva. La teoría de tipos, el análisis computable y distintas formas de matemática constructiva han profundizado después la relación entre existencia, información y cálculo.

Esto sugiere una actitud metodológica especialmente fértil:

$$
\boxed{
\text{construir cuando podamos; declarar con precisión cuándo no lo hacemos.}
}
$$

No necesitamos renunciar automáticamente a un teorema porque su prueba clásica sea no constructiva.

Podemos hacer algo más informativo:

1. demostrar el resultado clásico;
2. identificar sus dependencias lógicas y conjuntistas relevantes;
3. determinar qué información efectiva proporciona la demostración;
4. buscar, cuando tenga sentido, una versión constructiva o computable;
5. comparar exactamente qué se gana y qué se pierde.

Entonces las diferencias fundacionales dejan de ser únicamente una disputa filosófica y se convierten en información matemática.

## 9. Un principio editorial: no ocultar

Podemos resumir esta posición en una regla:

$$
\boxed{
\text{No prohibir la matemática no constructiva;}
\quad
\text{prohibir que su carácter no constructivo permanezca invisible.}
}
$$

Lo mismo vale para el infinito y para el axioma de elección.

No proponemos:

$$
\text{«Sólo existen números computables».}
$$

Preguntamos:

$$
\boxed{\text{¿este número es computable y, si lo es, mediante qué representación?}}
$$

No proponemos abandonar la completitud clásica.

Distinguimos:

$$
\text{completitud clásica}
$$

de

$$
\text{completitud efectiva}.
$$

No rechazamos una demostración porque use elección.

Registramos qué forma de elección utiliza, si puede evitarse y si el propio teorema necesita realmente esa fuerza o sólo la necesita la prueba elegida.

Esta diferencia enriquece los resultados. No los empobrece.

## 10. Un decálogo crítico para las construcciones matemáticas

De esta discusión emerge un protocolo que puede aplicarse a prácticamente cualquier construcción matemática.

### 1. ¿Qué objeto estamos introduciendo?

Precisar su naturaleza matemática y no esconderla detrás de una notación conveniente.

### 2. ¿Qué significa que esté definido?

Distinguir definición formal, descripción finita, especificación efectiva y mera caracterización existencial.

### 3. ¿Cómo sabemos que existe?

Identificar el argumento exacto de existencia y los principios sobre los que descansa.

### 4. ¿Podemos construirlo?

Preguntar si la demostración proporciona el objeto cuya existencia afirma.

### 5. ¿Podemos calcular con él?

No confundir operaciones formalmente definidas con operaciones efectivamente computables.

### 6. ¿Podemos decidir cuándo dos objetos son iguales?

Una relación de igualdad puede estar perfectamente definida aunque no exista un algoritmo general que la decida.

### 7. ¿Podemos decidir sus propiedades básicas?

Para una cortadura $L\subseteq\mathbb Q$, por ejemplo:

$$
q\in L\;?
$$

¿existe un procedimiento efectivo que determine la respuesta?

### 8. ¿Qué infinitud estamos utilizando?

Distinguir un proceso potencialmente indefinido de una totalidad infinita tratada como objeto completo.

### 9. ¿Qué principios lógicos o de elección intervienen?

Cuando sean relevantes, hacer visibles lógica clásica, tercero excluido, elección numerable, elección dependiente, principios de ideales primos, Zorn o elección completa.

### 10. ¿Qué sobrevive bajo exigencias constructivas o efectivas?

Después del resultado clásico, preguntar:

$$
\boxed{
\text{¿cuál es la versión constructiva o computable más fuerte que podemos conservar?}
}
$$

## 11. Wildberger como prueba de estrés

Wildberger puede estar equivocado en una objeción determinada.

Puede ocurrir que una respuesta formal resuelva otra completamente.

También puede ocurrir que una objeción sólo tenga fuerza si aceptamos previamente su criterio finitista de legitimidad matemática.

Pero la peor respuesta sería ignorar la pregunta porque procede de una posición minoritaria.

Una matemática segura de sus fundamentos debería poder enfrentarse a sus adversarios más incómodos.

Por eso resulta útil tratar a Wildberger no necesariamente como un guía, sino como una **prueba de estrés**.

Ante una construcción podemos preguntar:

$$
\begin{aligned}
&\text{¿qué acabamos de introducir?}\\
&\text{¿cómo se especifica?}\\
&\text{¿cómo demostramos que existe?}\\
&\text{¿podemos construirlo?}\\
&\text{¿podemos calcular con él?}\\
&\text{¿podemos decidir igualdad?}\\
&\text{¿qué axiomas estamos utilizando?}
\end{aligned}
$$

Si la teoría puede responder satisfactoriamente, la objeción habrá servido para fortalecerla.

Si no puede hacerlo, entonces hemos descubierto algo que merecía hacerse visible.

## Conclusión

La discusión sobre los números reales no debería reducirse a decidir si Dedekind tenía razón o si Wildberger está equivocado.

La cuestión más fértil es otra:

> ¿qué podemos aprender sobre nuestra propia matemática cuando tomamos en serio las preguntas del crítico?

Una construcción clásica puede ser correcta y, al mismo tiempo, no ser efectiva.

Una función puede estar formalmente definida y no venir acompañada de un algoritmo.

Una existencia puede estar demostrada sin que podamos exhibir un testigo.

Un teorema puede depender de un principio de elección que permanece invisible en su formulación cotidiana.

Nada de esto invalida automáticamente la matemática clásica.

Pero todo ello pertenece al contenido matemático del resultado.

Por eso adoptamos una orientación deliberadamente constructiva sin convertirla en dogma:

$$
\boxed{
\begin{gathered}
\text{construir siempre que sea razonablemente posible,}\\
\text{hacer explícitas las dependencias cuando no lo sea,}\\
\text{y utilizar las objeciones para aumentar, no disminuir, el rigor.}
\end{gathered}
}
$$

Quizá ésta sea una respuesta más interesante a Wildberger que aceptarlo o descartarlo en bloque.

No ignorarlo.

No seguirlo ciegamente.

Sino permitir que sus preguntas nos obliguen a precisar mejor qué queremos decir cuando afirmamos que algo **existe**, que algo está **construido** o que una operación está **definida** en matemáticas.

---

## Referencias y lecturas

- Bishop, Errett. *Foundations of Constructive Analysis*. McGraw-Hill, 1967.
- Bridges, Douglas; Richman, Fred. *Varieties of Constructive Mathematics*. Cambridge University Press, 1987.
- Stanford Encyclopedia of Philosophy. “[Constructive Mathematics](https://plato.stanford.edu/entries/mathematics-constructive/)”.
- Stanford Encyclopedia of Philosophy. “[The Axiom of Choice](https://plato.stanford.edu/entries/axiom-choice/)”.
- Wildberger, Norman J. “Real numbers: A critique and way forward”. 2015. DOI: 10.13140/RG.2.1.3673.8406.
- Wildberger, Norman J. “[Set Theory: Should You Believe?](https://web.maths.unsw.edu.au/~norman/papers/SetTheory.pdf)”. 2015.
