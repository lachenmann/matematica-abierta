**69.** Un estudiante niega $\forall x\in\mathbb R\;(x^2\ge0)$ escribiendo $\forall x\in\mathbb R\;(x^2<0)$. Localiza el primer error y repara la negación.

**70.** Un estudiante traduce “para cada estudiante hay un libro que ese estudiante eligió” como $\exists b\forall e\,E(e,b)$. Explica el cambio de significado y corrige.

**71.** Sobre $\mathbb R$, decide la verdad de: (a) $\forall x\exists y\;(x+y=0)$; (b) $\exists y\forall x\;(x+y=0)$; (c) $\forall x\forall y\;(x+y=0)$; (d) $\exists x\exists y\;(x+y=0)$. Niega además la afirmación (a).

**72.** Analiza la afirmación: “Para todo real $x$ existe un único real $y$ tal que $2y+x=0$”. (a) Escríbela simbólicamente; (b) decide su verdad; (c) identifica la dependencia de $y$; (d) escribe su negación sin usar $\exists!$.

***

#### M — Problemas tipo prueba

Los siguientes ejercicios están pensados como problemas de evaluación escrita. Exigen desarrollo completo, control del alcance de los cuantificadores y justificación explícita de testigos, contraejemplos o dependencias.

**73.** Sobre $\mathbb R$, analiza las cuatro afirmaciones siguientes. Para cada una: (i) decide si es verdadera o falsa; (ii) si es verdadera, da una regla explícita para elegir el testigo; (iii) si es falsa, exhibe una contradicción o un contraejemplo; (iv) explica qué cambia al invertir el orden de los cuantificadores.

(a) $\forall x\in\mathbb R\setminus\{0\}\;\exists y\in\mathbb R\;(xy=1)$.

(b) $\exists y\in\mathbb R\;\forall x\in\mathbb R\setminus\{0\}\;(xy=1)$.

(c) $\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x)$.

(d) $\exists y\in\mathbb R\;\forall x\in\mathbb R\;(y>x)$.

**74.** Considera la afirmación

$$
\forall x\in\mathbb R\;\Big[x\ge0\Rightarrow\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big].
$$

(a) Exprésala en lenguaje natural.  
(b) Négala paso a paso hasta obtener una fórmula en la que la negación actúe sólo sobre relaciones atómicas.  
(c) Decide la verdad de la afirmación original y de su negación.  
(d) Explica por qué cambiar sólo $\forall$ por $\exists$ no produce todavía la negación correcta.

**75.** Estudia la afirmación

$$
\forall x\in\mathbb R\;\exists!y\in\mathbb R\;(3y-2=x).
$$

(a) Expande $\exists!$ usando únicamente $\exists$, $\forall$, igualdad e implicación.  
(b) Demuestra existencia y unicidad para un $x$ arbitrario.  
(c) Escribe una negación equivalente que exprese explícitamente las dos maneras en que puede fallar la unicidad existencial: inexistencia o existencia de dos testigos distintos.  
(d) Compara con $\exists!y\in\mathbb R\;\forall x\in\mathbb R\;(3y-2=x)$ y decide su valor de verdad.

**76.** Sobre $\mathbb Z$, compara

$$
A:\quad \forall m\;\exists n\;\forall k\;(k\ge n\Rightarrow k>m)
$$

y

$$
B:\quad \exists n\;\forall m\;\forall k\;(k\ge n\Rightarrow k>m).
$$

(a) Decide la verdad de $A$ y construye un testigo $n$ en función de $m$.  
(b) Decide la verdad de $B$ y da un contraejemplo que funcione para cualquier candidato $n$.  
(c) Niega $A$ empujando la negación hasta la relación atómica.  
(d) Explica en una frase qué dependencia permite $A$ y prohíbe $B$.

**77.** Para un dominio $D$, considera

$$
S(D):\quad \forall x\in D\;\exists y\in D\;(y^2=x^2+1).
$$

(a) Decide si $S(\mathbb R)$ es verdadera y justifica una elección de $y$ para cada $x$.  
(b) Decide si $S(\mathbb Z)$ es verdadera. Si es falsa, encuentra el contraejemplo más simple que puedas.  
(c) Escribe la negación de $S(\mathbb Z)$ sin dejar una negación delante de un cuantificador.  
(d) Explica por qué la misma fórmula sintáctica expresa afirmaciones diferentes al cambiar el dominio.

**78.** Sean $E$ el conjunto de estudiantes, $P$ el conjunto de problemas y $S(e,p)$ el predicado “el estudiante $e$ resolvió el problema $p$”. Formaliza la frase:

> Todo estudiante resolvió al menos un problema que ningún otro estudiante resolvió.

(a) Escribe una fórmula cuantificada completa.  
(b) Niega tu fórmula y lleva la negación hasta los predicados atómicos.  
(c) Traduce la negación obtenida nuevamente al castellano.  
(d) Explica por qué mover el cuantificador $\exists p$ delante de $\forall e$ cambia el significado.

**79.** Considera la fórmula abierta

$$
F(y,z):\quad \forall x\,[P(x,y)\Rightarrow\exists y\,Q(x,y,z)].
$$

(a) Identifica todas las apariciones libres y ligadas de variables.  
(b) Renombra la variable ligada del cuantificador existencial para eliminar la reutilización del símbolo $y$ sin cambiar el significado.  
(c) Explica por qué renombrar ingenuamente el $\forall x$ como $\forall y$ puede capturar una variable que antes era libre.  
(d) Forma la clausura universal de la fórmula corregida.  
(e) Niega esa clausura universal hasta obtener una fórmula donde la negación actúe sólo sobre $Q$.

**80.** Analiza la afirmación

$$
\forall x\in\mathbb R\;\exists!y\in\mathbb R\;
\Big[y>x\land\forall z\in\mathbb R\,(z>x\Rightarrow y\le z)\Big].
$$

(a) Traduce cuidadosamente la afirmación al castellano.  
(b) Decide si es verdadera o falsa.  
(c) Si suponemos que un $y$ satisface la condición para cierto $x$, construye explícitamente un real $z$ que destruya esa posibilidad.  
(d) Explica si el fracaso está en la existencia, en la unicidad o en ambas.  
(e) Escribe en lenguaje natural una negación exacta de la afirmación original.

# Soluciones razonadas

Las soluciones forman parte del capítulo canónico. En los ejercicios de traducción puede haber variantes lingüísticas equivalentes; lo esencial es conservar dominio, cuantificadores, alcance y dependencia.

### Soluciones — A — Predicados y dominios

**Solución 1.** (a) $x+1$ es una expresión: representa un número una vez fijado $x$. (b) $x+1=5$ es un predicado abierto porque su verdad depende de $x$. (c) $4+1=5$ es una proposición y es verdadera. (d) “$n$ es par” es un predicado abierto. (e) “$6$ es par” es una proposición verdadera.

**Solución 2.** En $\mathbb Z$ no existe entero con cuadrado $2$, así que es falsa. En $\mathbb Q$ también es falsa: $\sqrt2$ no es racional. En $\mathbb R$ es verdadera, con testigos $\sqrt2$ y $-\sqrt2$. El ejercicio muestra que el dominio forma parte del significado.

**Solución 3.** Sobre $\{0,1\}$ es verdadera: hay sólo dos casos y ambos dan igualdad. Sobre $\mathbb Z$ también es verdadera, pues $x^2-x=x(x-1)$ y para todo entero $x$ el producto es no negativo: si $x\le0$, ambos factores son no positivos; si $x\ge1$, ambos son no negativos. Sobre $\mathbb R$ es falsa: $x=1/2$ produce $1/4<1/2$.

**Solución 4.** La expresión $1/x$ no está definida en $x=0$. Por tanto, si queremos usar $Q$ como predicado numérico debemos restringir el dominio a valores donde tenga sentido, por ejemplo $\mathbb R\setminus\{0\}$. No es correcto declarar simplemente $Q(0)$ falsa: la fórmula ni siquiera está definida allí.

**Solución 5.** Una elección es $D=\{-1,1\}$: ambos elementos satisfacen $x^2=1$. Para que sea falsa basta incluir un contraejemplo; por ejemplo $E=\{-1,0,1\}$, porque $0^2\ne1$.

**Solución 6.** Sobre $\mathbb Z$, el universal es falso porque $x=2$ da $4<4$, falso; el existencial es verdadero, por ejemplo con $x=0$. Sobre $\mathbb R$, el universal también es falso, por ejemplo con $x=3$, y el existencial es verdadero con $x=0$. Las dos afirmaciones conservan aquí su valor de verdad al cambiar de dominio, aunque sus conjuntos de testigos y contraejemplos cambian.

### Soluciones — B — Variables libres y ligadas

**Solución 7.** El cuantificador $\forall x$ liga a $x$ dentro de $P(x,y)$. La variable $y$ no tiene cuantificador y queda libre. Por ello la fórmula completa sigue siendo abierta respecto de $y$.

**Solución 8.** $y$ está ligada por $\exists y$ en todo el alcance entre corchetes. Las variables $x$ y $z$ quedan libres.

**Solución 9.** La primera es cerrada: todas las variables que aparecen, $x$ e $y$, están ligadas. La segunda no es cerrada porque $z$ queda libre. Su valor de verdad puede depender del valor o interpretación de $z$.

**Solución 10.** (a) Por ejemplo, sustituyendo $x=3$ obtenemos $3^2=9$, verdadera. (b) $\exists x\in\mathbb R\;(x^2=9)$, verdadera. (c) $\forall x\in\mathbb R\;(x^2=9)$, falsa. Las tres operaciones cierran la variable, pero producen proposiciones diferentes.

**Solución 11.** $x$ está ligada por el cuantificador universal y su alcance incluye tanto $P(x,y)$ como $R(x,z)$. $z$ está ligada por $\exists z$ dentro del consecuente. $y$ queda libre porque no aparece cuantificada.

**Solución 12.** Podemos escribir $\forall t\,P(t,y)$: $t$ reemplaza coherentemente a la variable ligada $x$, mientras $y$ permanece libre. En cambio, $\forall y\,P(y,y)$ hace que el cuantificador ligue también la posición que antes correspondía a la $y$ libre. Se produce captura de variable y el significado puede cambiar.

### Soluciones — C — Universales y contraejemplos

