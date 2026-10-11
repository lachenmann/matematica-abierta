---
title: Capítulo 17 — Computabilidad mínima para la metamatemática
status: published
draft: false
book-id: MA-BOK-0014
editorial-project: TLOG
date-modified: '2026-10-11'
license: GFDL-1.3-or-later
areas:
- fundamentos
level: avanzado
topics:
- logica
number-sections: false
content-id: MA-BCH-0219
content-type: book-chapter
source-id: TLOG-CH17-0001
prerequisites:
- MA-BCH-0202
- MA-BCH-0216
- MA-BCH-0218
related:
- MA-BOK-0014
source-sha256: 1bd49321d6bd3b3ac0746100c932c0c1b91299595a1b9ac57d27953fe95e2c9b
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 16](capitulo-16.md) · [Capítulo 18 →](capitulo-18.md)

## 17.0. De la finitud conjuntista a la efectividad operacional

La Parte III cerró la construcción de los naturales, de la recursión sobre ellos y de los conjuntos de secuencias finitas, pero **una definición conjuntista de una función no es, por sí sola, un algoritmo**. El objetivo de este capítulo es construir una semántica operacional concreta en la que la palabra «computable» posea un significado verificable. Sólo después se justificarán, en los capítulos 18–20, las codificaciones numéricas y las relaciones entre computabilidad, representabilidad y diagonalización.

**Contrato de niveles.** Toda construcción de este capítulo se desarrolla inicialmente en la metateoría externa clásica $\mathsf M_{\mathrm{ext}}=\mathsf{ZF}$, sin AC ni BPI, y estudia el sistema operacional de máquinas de registros $\mathrm{RM}$. Los resultados conjuntistas de los capítulos 14–16 suministran **patrones de demostración reconstruibles en ZF**, no axiomas que se importen retroactivamente desde $\mathsf{ZF}_{\mathrm{obj}}$. No se presupone un modelo de $\mathsf{ZF}_{\mathrm{obj}}$, ni se amplía su signatura primitiva $\tau_\in$. Los programas serán, por ahora, secuencias de instrucciones estructuradas; el **número de Gödel de un programa no está definido**.

**Procedencia.** Reconstrucción interna bajo las convenciones y recursos ya aprobados del tratado; se conservan los estados bibliográficos anteriores. Ninguna demostración se declara importada de GAS/FND ni cotejada en páginas nuevas de una fuente. La equivalencia con otras máquinas o modelos abstractos de computación es una obligación ulterior, no una consecuencia automática del nombre «máquina de registros».

## 17.1. Convenio de efectividad y niveles

### Convención 17.1.1 — Alcance de la palabra computable {#tlog-cnv-00025}

Fijamos $\omega$ y todas las operaciones conjuntistas en $\mathsf M_{\mathrm{ext}}$. La palabra **computable-RM** significará «realizada por un programa bien formado del modelo $\mathrm{RM}$ que se define a continuación»; la palabra **total** impondrá terminación sobre **todas** las entradas del dominio tipado. Un procedimiento capaz de terminar únicamente ante respuestas positivas se llamará **semidecisión-RM**. No se identifican «conjunto definible», «conjunto enumerable mediante alguna función conjuntista», «decidible-RM» y «semidecidible-RM». Esta convención se interpreta operativamente en las definiciones de §§17.13–17.16, sin adelantar sus cláusulas formales.

## 17.2. Alfabeto conjunto de instrucciones

### Definición 17.2.1 — Cuatro coordenadas y tres constructores disjuntos {#tlog-def-00107}

Definimos el **conjunto de instrucciones crudas** $\mathcal I\subseteq\omega^4$ por
$$
\begin{aligned}
\mathtt{HALT}&:=(0,0,0,0),\\
\mathtt{INC}(i,j)&:=(1,i,j,0),\\
\mathtt{DECJZ}(i,j,k)&:=(2,i,j,k),\\
\mathcal I&:=\{\mathtt{HALT}\}\cup\{\mathtt{INC}(i,j):i,j\in\omega\}
  \cup\{\mathtt{DECJZ}(i,j,k):i,j,k\in\omega\}.
\end{aligned}
$$
Los números de la primera coordenada son etiquetas sintácticas, no códigos de Gödel. La existencia de $\mathcal I$ se obtiene por separación sobre $\omega^4$ y las tres condiciones explícitas. Las familias son disjuntas por su primera coordenada; la lectura del constructor y de sus parámetros es única. Una instrucción puede contener números de registros o destinos fuera de rango: eso se prohibirá en la **formación del programa**, no mediante una noción circular de ejecución.

## 17.3. Formación de programas, aridad y saltos

### Definición 17.3.1 — Programa de $r$ registros con $n$ etiquetas {#tlog-def-00108}

Un programa estructurado es el par $P=(r,p)$, donde $r\in\omega$ y $1\leq r$, $p:n\to\mathcal I$ es una secuencia de longitud $n\in\omega$ con $1\leq n$, y **para cada** $\ell\in n$:

* Si $p(\ell)=\mathtt{HALT}$, no impone condiciones adicionales.
* Si $p(\ell)=\mathtt{INC}(i,j)$, exige $i\in r$ y $j\in n$.
* Si $p(\ell)=\mathtt{DECJZ}(i,j,k)$, exige $i\in r$ y $j,k\in n$.

El contador de instrucciones comenzará en $0\in n$. Para cada aridad $q\in\omega$, ponemos $\operatorname{Prog}_q:=\{P:\operatorname{Well}(P)\land q\leq r\}$; como $r\ge1$, existe siempre el registro de salida $0\in r$. Los $q$ valores de entrada ocuparán los registros $0,\ldots,q-1$. Los restantes se inicializarán en cero. El espacio de programas es la **familia de datos finitos con guardas**, no una sucesión de números naturales aún codificada.

## 17.4. Existencia conjuntista y programas testigo

### Proposición 17.4.1 — $\operatorname{Prog}_q$ es un conjunto no vacío {#tlog-pro-00103}

Para cada $q\in\omega$, la colección $\operatorname{Prog}_q$ existe como conjunto y contiene tanto programas con instrucción de parada como programas sin instrucción de parada.

**Demostración.** Como $\mathcal I$ es conjunto, $\mathcal I^{<\omega}$ existe mediante la construcción de secuencias finitas. Los posibles pares $(r,p)$ están acotados por $\omega\times\mathcal I^{<\omega}$. La condición $\operatorname{Well}(r,p)$ es una fórmula de conjuntos que sólo cuantifica sobre el dominio finito $n$ de $p$, sus coordenadas y $r$; por separación produce $\operatorname{Prog}_q$. Tomando $r\ge\max(1,q)$ y $p:1\to\mathcal I$ con $p(0)=\mathtt{HALT}$ obtenemos un miembro. Tomando en cambio $p(0)=\mathtt{INC}(0,0)$ obtenemos otro programa bien formado que carece de parada; el salto $0$ está dentro del segmento $1$. No se escogen simultáneamente elementos de una familia de conjuntos: ambos testimonios son explícitos. $\square$

## 17.5. Configuraciones y carga de la entrada

### Definición 17.5.1 — Estado con contador de instrucciones y registros {#tlog-def-00109}

Para $P=(r,p)$ de longitud $n$, una configuración es
$$
C_P:=n\times\omega^r,\qquad c=(\ell,\rho),
$$
donde $\ell\in n$ es la posición de instrucción y $\rho:r\to\omega$ es el vector de registros. Para $P\in\operatorname{Prog}_q$ y $x:q\to\omega$, la configuración inicial $\operatorname{init}_P(x)=(0,\rho_x)$ satisface
$$
\rho_x(i)=\begin{cases}x(i)&i\in q,\\0&i\in r\setminus q.\end{cases}
$$
La gráfica de $\rho_x$ se obtiene por separación sobre $r\times\omega$ y la condición por casos; es única y existe incluso si $q=0$, caso en el que $x=\varnothing$ y todos los registros comienzan en cero. El resultado del cómputo, cuando termine, será **siempre** el contenido del registro $0$. $C_P$ es un conjunto no vacío porque $n\ge1$ y hay un vector de registros nulos.

## 17.6. Guardas de decremento y salto

### Lema 17.6.1 — Cada rama no nula tiene predecesor único {#tlog-lem-00055}

Si $\rho(i)\in\omega$ es distinto de $0$, existe un único $m\in\omega$ tal que $\rho(i)=S(m)$. Toda instrucción bien formada $\mathtt{INC}(i,j)$ o $\mathtt{DECJZ}(i,j,k)$ designa un registro existente y un destino válido.

**Demostración.** Repetimos en $\mathsf M_{\mathrm{ext}}$ la inducción conjuntista que prueba que todo natural no nulo es un sucesor, y la demostración de inyectividad de $S$ desde fundamentación; esta es la prueba finita reconstruida en §16.14, no una transferencia de un modelo de $\mathsf{ZF}_{\mathrm{obj}}$. La pertenencia de los índices $i\in r$ y $j,k\in n$ es literalmente parte de $\operatorname{Well}(P)$. Se obtiene existencia de cada valor asignado al siguiente estado, y la unicidad procede de la del predecesor y de la lectura única de la instrucción. $\square$

## 17.7. Semántica de un paso

### Definición 17.7.1 — Transición totalizada con parada absorbente {#tlog-def-00110}

Sea $c=(\ell,\rho)\in C_P$. Definimos $E_P(c)$ por cláusulas disjuntas:
$$
\begin{array}{ll}
\text{HALT:}&p(\ell)=\mathtt{HALT}\Rightarrow E_P(c)=c;\\
\text{INC:}&p(\ell)=\mathtt{INC}(i,j)\Rightarrow
 E_P(c)=(j,\rho[i\mapsto S(\rho(i))]);\\
\text{DECJZ-0:}&p(\ell)=\mathtt{DECJZ}(i,j,k),\;\rho(i)=0
 \Rightarrow E_P(c)=(j,\rho);\\
\text{DECJZ-$>$0:}&p(\ell)=\mathtt{DECJZ}(i,j,k),\;\rho(i)=S(m)
 \Rightarrow E_P(c)=(k,\rho[i\mapsto m]).
\end{array}
$$
Los corchetes denotan la actualización de una función en una coordenada (Capítulo 14). La **parada es absorbente**: se representa por un estado que permanece fijo en cada paso posterior, sin declarar que la máquina haya ejecutado nuevas instrucciones reales después de detenerse. Las instrucciones no son fórmulas del lenguaje objeto $\tau_\in$; son elementos de un conjunto de sintaxis operacional metateórica.

## 17.8. Existencia y determinismo del grafo de paso

### Proposición 17.8.1 — $E_P$ es función total $C_P\to C_P$ {#tlog-pro-00104}

Para cada programa bien formado $P$ existe una única gráfica $E_P\subseteq C_P\times C_P$ que satisface las cuatro cláusulas de §17.7. La aplicación tiene dominio exacto $C_P$ y codominio $C_P$.

**Demostración.** $C_P\times C_P$ existe por producto cartesiano. Separamos los pares $(c,d)$ para los cuales una de las cuatro fórmulas definitorias establece $d=E_P(c)$, con sus testigos $i,j,k,m$ acotados por las guardas de formación. Las etiquetas 0,1,2 de instrucción son distintas, y las ramas $\rho(i)=0$ y $\rho(i)\ne0$ son excluyentes. En el segundo caso el predecesor existe y es único por §17.6. Las actualizaciones tienen dominio $r$ y valores naturales; los destinos pertenecen a $n$. Por ello para todo $c\in C_P$ hay **exactamente un** $d\in C_P$ y la relación separada es una función total. Extensionalidad concede unicidad de su grafo. La argumentación construye directamente el conjunto de transiciones, sin escoger sucesores mediante AC. $\square$

## 17.9. Ejecución determinista por recursión numérica

### Metateorema 17.9.1 — Existe una única órbita de estados {#tlog-mth-00078}

Fijados $P\in\operatorname{Prog}_q$ y $x\in\omega^q$, existe una función única
$$
\operatorname{Run}_P(x,\cdot):\omega\longrightarrow C_P
$$
que verifica
$$
\operatorname{Run}_P(x,0)=\operatorname{init}_P(x),\qquad
\operatorname{Run}_P(x,S(t))=E_P(\operatorname{Run}_P(x,t)).
$$
Más aún, existe el grafo uniforme sobre $\omega^q\times\omega$ para $P$ fijo.

**Demostración.** Reproducimos en $\mathsf M_{\mathrm{ext}}$ la construcción conjuntista de recursión sobre $\omega$: el codominio $C_P$ es un conjunto no vacío, $E_P:C_P\to C_P$ es total y el estado inicial pertenece a $C_P$. La existencia se obtiene uniendo aproximaciones funcionales compatibles, acotadas por $\mathcal P(\omega\times C_P)$; la unicidad, por inducción en $t$. Las aproximaciones y su construcción siguen el argumento explícito del Capítulo 16, aplicado ahora en la metateoría ZF. La versión uniforme utiliza el parámetro $x\in\omega^q$ y separación en $(\omega^q\times\omega)\times C_P$ más reemplazo para obtener una única gráfica de evaluación. **No** postulamos la verdad de $\mathsf{ZF}_{\mathrm{obj}}$ en $\mathsf M_{\mathrm{ext}}$ ni empleamos una familia de elecciones. $\square$

## 17.10. Certificados de ejecución acotada

### Proposición 17.10.1 — Trazas finitas existentes y verificables {#tlog-pro-00105}

Para $P,x,t$ tipados existe una única secuencia $s:S(t)\to C_P$ con
$$
s(0)=\operatorname{init}_P(x),\qquad
\forall u\in t\;s(S(u))=E_P(s(u)).
$$
Se obtiene restringiendo $\operatorname{Run}_P(x,\cdot)$ a $S(t)$. Una sucesión candidata de esa longitud puede **verificarse en un número finito de operaciones elementales**: comprobar índices, cuatro coordenadas de instrucción, igualdad de naturales, incremento y predecesor de registros, y transiciones consecutivas.

**Demostración.** La restricción del grafo uniforme existe por separación y satisface las ecuaciones. Si $s'$ es otra traza con dominio $S(t)$, se induce sobre $u\le t$ la igualdad $s(u)=s'(u)$; el paso aplica la unicidad de $E_P$. Para verificar un candidato se lee una lista finita de $t+1$ estados y se recorren sus $t$ transiciones, donde cada comprobación es una operación explícita sobre números naturales y registros finitos. Se trata de **verificación de una traza y una cota dadas**, no de un algoritmo que determine si una ejecución arbitraria terminará alguna vez. $\square$

## 17.11. Parada y salida observada

### Definición 17.11.1 — Predicado de parada en tiempo $t$ {#tlog-def-00111}

Para $P=(r,p)$, $x\in\omega^q$ y $t\in\omega$, escribimos
$$
\operatorname{Halt}(P,x,t)\iff
p\bigl(\pi_0(\operatorname{Run}_P(x,t))\bigr)=\mathtt{HALT}.
$$
Si esto ocurre, $\operatorname{Out}(P,x,t)$ es el valor $\rho(0)$ del vector de registros en $\operatorname{Run}_P(x,t)=(\ell,\rho)$. Definimos «$P$ termina en $x$» por $\exists t\in\omega\,\operatorname{Halt}(P,x,t)$. No definimos aún un tiempo de parada como término total; cuando exista al menos un testigo, su **menor** valor se legitimará por el buen orden de $\omega$.

## 17.12. Permanencia de la parada y estabilidad del resultado

### Lema 17.12.1 — Parada absorbente y tiempo mínimo {#tlog-lem-00056}

Si $\operatorname{Halt}(P,x,t)$, entonces para todo $u\ge t$ se cumplen $\operatorname{Halt}(P,x,u)$ y $\operatorname{Out}(P,x,u)=\operatorname{Out}(P,x,t)$. Cuando la ejecución termina, existe un **único menor instante** $\mu t\,\operatorname{Halt}(P,x,t)$.

**Demostración.** La instrucción de parada fija toda la configuración por la primera cláusula de $E_P$. Por inducción en el número natural de pasos posteriores, su órbita permanece constante. La totalidad del orden usual $\le$ permite escribir cada $u\ge t$ como $t+v$ (se prueba por inducción en $u$ o mediante las leyes aritméticas previamente reconstruidas), y se concluyen las dos estabilidades. El conjunto $T=\{t\in\omega:\operatorname{Halt}(P,x,t)\}$ existe por separación. Si no es vacío, el buen orden de $\omega$ proporciona un mínimo único. Ninguna operación de minimización se declara **calculable** por esta sola argumentación conjuntista. $\square$

## 17.13. Significado extensional de un programa

### Definición 17.13.1 — Gráfica calculada, posiblemente parcial {#tlog-def-00112}

Para $P\in\operatorname{Prog}_q$ definimos la relación
$$
\boxed{\ F_P^{(q)}:=\{(x,y)\in\omega^q\times\omega:\exists t\in\omega\;
[\operatorname{Halt}(P,x,t)\land\operatorname{Out}(P,x,t)=y]\}.\ }
$$
Esta es la **semántica extensional parcial** del programa. La salida $y$ aparece sólo si $P$ efectivamente alcanza una instrucción $\mathtt{HALT}$. El par $(q,P)$ forma parte del tipo: un mismo programa puede admitir varias aridades de entrada, con cargas iniciales distintas. El símbolo $F_P^{(q)}(x)$ **no** es un término definido si $P$ no termina en $x$.

## 17.14. La semántica calculada es una función parcial

### Proposición 17.14.1 — Conjunto de pares y univocidad del resultado {#tlog-pro-00106}

La relación $F_P^{(q)}$ existe como conjunto y es una función parcial con dominio incluido en $\omega^q$ e imagen incluida en $\omega$. Si $P$ alcanza la parada en $x$, produce un único $y$, independiente del testigo temporal.

**Demostración.** La clase $\omega^q\times\omega$ es un conjunto. El predicado enmarcado en §17.13 tiene parámetros conjuntistas fijos y por separación determina un subconjunto suyo; todos los cuantificadores sobre tiempos son cuantificadores ordinarios en la metateoría. Si $(x,y),(x,z)\in F_P^{(q)}$, hay instantes $t,u$ en los cuales la máquina está detenida y sus registros de salida son $y,z$. La linealidad del orden sobre naturales permite suponer $t\le u$. Por la permanencia de la parada (§17.12), el estado en $u$ coincide con el de $t$; en particular $y=z$. No se ha probado que para **todo** $x$ exista un par: la función es, en general, parcial. $\square$

## 17.15. Computabilidad parcial y total relativas al modelo

### Definición 17.15.1 — Función parcial computable-RM {#tlog-def-00113}

Sea $f\subseteq\omega^q\times\omega$ una función parcial. Diremos que $f$ es **parcial computable-RM** si existe $P\in\operatorname{Prog}_q$ con $f=F_P^{(q)}$ como grafos. Diremos que $f$ es **total computable-RM** si además $\operatorname{dom}(f)=\omega^q$. Igualdad de funciones parciales significa coincidencia de *dominio y valor*, no sólo acuerdo donde ambas están definidas. Esta es una definición exacta en $\mathsf M_{\mathrm{ext}}$ relativa a $\mathrm{RM}$; **no** se ha probado todavía la equivalencia extensional con máquinas de Turing, funciones recursivas u otros modelos.

## 17.16. Decisión, semidecisión y conjuntos c.e.

### Definición 17.16.1 — Dos nociones operacionales diferentes {#tlog-def-00114}

Para $R\subseteq\omega^q$ definimos:

* $R$ es **semidecidible-RM** (o **c.e.-RM por dominio de parada**) cuando existe $P\in\operatorname{Prog}_q$ tal que
  $$
  x\in R\iff\exists t\in\omega\,\operatorname{Halt}(P,x,t).
  $$
  Si $x\notin R$, el programa puede ejecutar infinitamente; no se exige una respuesta negativa.
* $R$ es **decidible-RM** cuando existe $P\in\operatorname{Prog}_q$ que termina para cada $x\in\omega^q$, deja el registro de salida en $\{0,1\}$, y satisface
  $$
  x\in R\iff F_P^{(q)}(x)=1,\qquad x\notin R\iff F_P^{(q)}(x)=0.
  $$

El adjetivo **computablemente enumerable** se fija por ahora en su caracterización operacional de **dominio de un cómputo parcial**. La equivalencia con la imagen de un *enumerador total que emite todos los elementos* aún no está demostrada; requiere controlar uniformemente la codificación de entradas de aridad $q$ y el entrelazado de ejecuciones. Esa obligación queda registrada para los siguientes microtramos y el capítulo 18. Tampoco se afirma que la mera definibilidad conjuntista implique una de estas dos propiedades.

## 17.17. Aproximaciones temporales a un dominio c.e.

### Proposición 17.17.1 — Reunión creciente de secciones decidibles acotadas {#tlog-pro-00107}

Fijado $P\in\operatorname{Prog}_q$, definimos para $t\in\omega$
$$
D_{P,t}:=\{x\in\omega^q:\operatorname{Halt}(P,x,t)\}.
$$
Entonces
$$
\boxed{D_{P,t}\subseteq D_{P,S(t)},\qquad
\operatorname{dom}(F_P^{(q)})=\bigcup_{t\in\omega}D_{P,t}.}
$$
Dado un triple concreto $(P,x,t)$ bien tipado, la pertenencia $x\in D_{P,t}$ puede decidirse por el cálculo finito de la traza de longitud $S(t)$. No se afirma que **$D_{P,t}$ sea finito**: un programa que se detenga inmediatamente posee $D_{P,0}=\omega^q$, posiblemente infinito.

**Demostración.** Separación forma cada $D_{P,t}$ dentro de $\omega^q$. La permanencia de la parada da la inclusión. Por definición de $F_P^{(q)}$, la pertenencia de $x$ a su dominio equivale a que exista un $t$ con $\operatorname{Halt}(P,x,t)$, esto es, a $x\in\bigcup_t D_{P,t}$. La familia $t\mapsto D_{P,t}$ es funcional y existe por reemplazo, de modo que la unión es un conjunto. El algoritmo de pertenencia acotada simula exactamente $t$ pasos con la transición de §17.7 y comprueba el constructor de la instrucción actual; **termina porque $t$ es un natural dado**. Así se justifica la semidecisión por búsqueda sucesiva de cotas, sin resolver la parada ilimitada. $\square$

## 17.18. Programas básicos y programas divergentes

### Proposición 17.18.1 — Identidad, cero constante y divergencia universal {#tlog-pro-00108}

En el modelo definido existen, por construcción explícita:

1. Una máquina de aridad $1$ que calcula la identidad $n\mapsto n$: con un registro y programa de longitud $1$, $p(0)=\mathtt{HALT}$; el registro $0$ conserva la entrada.
2. Para cada aridad $q\in\omega$, una máquina que calcula la constante cero $z_q(x)=0$ en **todas** las entradas, incluso $q=0$. Tomamos $r\ge\max(q,2)$ y programa de longitud $3$:
   $$
   p(0)=\mathtt{DECJZ}(0,2,1),\qquad
   p(1)=\mathtt{INC}(1,0),\qquad
   p(2)=\mathtt{HALT}.
   $$
3. Para cada aridad $q$, una máquina que nunca termina: con $r\ge\max(q,1)$, el programa de longitud $1$ $p(0)=\mathtt{INC}(0,0)$ incrementa perpetuamente el registro $0$ y salta siempre a $0$.

**Demostración.** En (1) la instrucción inicial ya es $\mathtt{HALT}$, luego el valor de salida es la primera entrada. En (2), si el registro $0$ es cero, la primera transición salta a $2$ y detiene la máquina; si su valor es $S(m)$, decrementa a $m$ y salta a $1$, que incrementa **el registro auxiliar 1** y vuelve a $0$. Por inducción sobre el valor inicial del registro $0$, tras un número finito de vueltas se alcanza $0$ y la parada en $2$. El incremento del registro $1$ nunca altera la salida ni la condición de finitud; es válido incluso si ese registro contenía un valor de entrada. En (3) la instrucción $\mathtt{HALT}$ no aparece en el programa, de modo que toda configuración alcanzada ejecuta $\mathtt{INC}$ y ninguna satisface el predicado de parada. Los tres programas satisfacen expresamente las condiciones sobre registros y destinos. $\square$

## 17.19. Lo decidible da dos semidecisiones

### Proposición 17.19.1 — Complementos de relaciones decidibles son semidecidibles {#tlog-pro-00109}

Si $R\subseteq\omega^q$ es decidible-RM, entonces **tanto $R$ como su complemento relativo** $\omega^q\setminus R$ son semidecidibles-RM:
$$
\boxed{\operatorname{Dec}_{\rm RM}(R)\ \Longrightarrow\
\operatorname{Semi}_{\rm RM}(R)\ \land\
\operatorname{Semi}_{\rm RM}(\omega^q\setminus R).}
$$

**Demostración constructiva.** Sea $P=(r,p)$ el programa decidor de $R$, de longitud $n\ge1$, que siempre termina con contenido $0$ o $1$ en el registro $0$. Para el reconocedor de $R$ fabricamos un programa $P^+$ de igual número $r$ de registros y longitud $n+2$. Conservamos todas las instrucciones no terminales de $p$, cuyos saltos originales siguen siendo válidos. Sustituimos **cada** instrucción $\mathtt{HALT}$ en una etiqueta antigua por $\mathtt{DECJZ}(0,n+1,n)$. Añadimos $p^+(n)=\mathtt{HALT}$ y $p^+(n+1)=\mathtt{INC}(0,n+1)$. Si el decidor original llega con salida $1$, $\mathtt{DECJZ}$ decrementa el registro $0$ y salta a $n$, que es terminal; si llega con salida $0$, salta a $n+1$, que forma un bucle sin parada. La semántica hasta la **primera** visita a una instrucción originalmente terminal es idéntica a la de $P$, pues ninguna instrucción anterior fue alterada. Por ello $P^+$ se detiene exactamente cuando $x\in R$.

Para reconocer el complemento fabricamos $P^-$ conservando el mismo esquema de dos nuevas etiquetas, pero sustituyendo cada instrucción terminal antigua por $\mathtt{DECJZ}(0,n,n+1)$: acepta y se detiene en la salida cero; entra en el bucle cuando la salida es uno. Ambos programas son bien formados (todos los destinos son menores que $n+2$) y poseen semántica de parada exactamente especificada. No usamos la afirmación recíproca, que exige una construcción controlada de simulación intercalada aún no efectuada. $\square$

## 17.20. Frontera entre semántica de máquinas y aritmetización

### Corolario 17.20.1 — Infraestructura operacional mínima disponible {#tlog-cor-00024}

El sistema $\mathrm{RM}$ proporciona: (i) un **conjunto** de programas finitos por aridad; (ii) transiciones y ejecuciones deterministas como funciones entre conjuntos; (iii) una semántica extensional de funciones parciales $\omega^q\rightharpoonup\omega$; (iv) la distinción operativa entre total computable, decidible y semidecidible; (v) certificados finitos de ejecución acotada, y (vi) reconocedores explícitos para ambos lados de una relación decidible.

**Demostración.** Los apartados (i)–(v) son, respectivamente, §§17.4, 17.8–17.17. El apartado (vi) es la traducción explícita de instrucciones de §17.19. La conjunción no introduce una máquina universal, ni enumera aún los programas mediante números naturales, ni demuestra equivalencia con modelos externos, ni establece la indecidibilidad general de la parada. Tales resultados exigen pruebas adicionales; declarar aquí alguno de ellos sería una circularidad respecto de los capítulos 18–20. $\square$

## 17.21. Obligaciones heredadas del primer microtramo

Quedan para `CH17-M02`: codificación explícita o simulación uniforme de instrucciones compuestas y ejecución intercalada; clausura de las funciones computables por composición y operadores básicos; demostración de la equivalencia operativa entre semidecisión y procedimientos de enumeración una vez dispuesta una codificación efectiva de tuplas; y análisis de las condiciones bajo las que ambos semidecidibles implican decidibilidad. **No** se reclama en este microtramo una numeración efectiva de las fórmulas del lenguaje lógico ni una máquina universal. La parte IV queda `OPEN` y el Capítulo 17 permanece `PARTIAL-CLOSURE`.

## 17.22. Compilación finita y separación de niveles

### Convención 17.22.1 — Compilación finita y separación de niveles {#tlog-cnv-00026}

Fijados **programas concretos** $P,Q$ de la sintaxis de §§17.2–17.3, una *compilación finita* transforma sus listas y etiquetas en una nueva lista finita de instrucciones $\mathrm{RM}$. Los índices internos de una transformación pueden ser pares $(\ell_P,\ell_Q)$ o etiquetas simbólicas provisionales, pero sólo aparecen **durante** la construcción: el programa resultado vuelve a ser un par $(r,p)$ con $p:n\to\mathcal I$, $r,n\ge1$ y saltos dentro de $n$. Cada número de etiqueta se obtiene mediante una **enumeración finita concreta**, distinta de una numeración de Gödel de programas arbitrarios.

Las pruebas de este bloque tienen lugar en $\mathsf M_{\mathrm{ext}}=\mathsf{ZF}$, sin axioma de elección ni principio del ultrafiltro. Se distinguen: (i) ejecución simulada de un programa fijo, (ii) transformación externa **efectiva** de una lista finita, y (iii) máquina universal que interpreta una descripción numérica variable. Sólo (i)–(ii) se construirán aquí. Todas las operaciones sobre segmentos finitos se controlarán mediante los lemas siguientes.


## 17.23. Macrobloques de registros con guardas de frescura

### Definición 17.23.1 — Macrobloques de registros con guardas de frescura {#tlog-def-00115}

Un **macrobloque** consta de una cantidad finita de ubicaciones de control, entradas y salidas etiquetadas, instrucciones elementales $\mathtt{INC}$/$\mathtt{DECJZ}$ y un conjunto finito de registros utilizados. Los macros $\operatorname{Go}(j)$, $\operatorname{Clr}(a)$, $\operatorname{Move}(a,b)$, $\operatorname{Copy}(a,b;t)$ y $\operatorname{Test0}(a;j_0,j_+)$ exigen registros **distintos** cuando así se indica. $\operatorname{Move}$ incrementará $b$ tantas veces como unidades retire de $a$, sin suponer $b=0$; $\operatorname{Copy}$ exige $t=0$ y lo devolverá a cero. Las etiquetas internas y los registros auxiliares son **frescos** respecto de los bloques que se incorporen.

La lectura editorial de un macro no es una nueva instrucción primitiva de RM. Su corrección exige exhibir una lista finita de instrucciones primitivas con el mismo efecto observable y la misma condición de parada. Queda prohibida cualquier instrucción encubierta de asignación general $a:=b$, de salto indirecto o de consulta externa de un programa.


## 17.24. Saltos incondicionales, borrado y transferencia finitos

### Lema 17.24.1 — Saltos incondicionales, borrado y transferencia finitos {#tlog-lem-00057}

**Lema.** Con un registro de descarte $d$ que no será leído ni presentado como salida, y con etiquetas válidas, las siguientes plantillas implementan las operaciones indicadas:

* $\operatorname{Go}(j)$: $\mathtt{INC}(d,j)$. Cambia sólo $d$ e ingresa en $j$.
* $\operatorname{Clr}(a)$: en la etiqueta $L$ se dispone $\mathtt{DECJZ}(a,E,L)$. Si $a=0$ termina; si $a>0$ decrementa y vuelve a $L$.
* $\operatorname{Move}(a,b)$, con $a\ne b$: en $L$ se dispone $\mathtt{DECJZ}(a,E,J)$ y en $J$ se dispone $\mathtt{INC}(b,L)$; $b$ termina aumentado por el valor inicial de $a$ y $a$ termina en cero.
* $\operatorname{Test0}(a;j_0,j_+)$: en $L$ se dispone $\mathtt{DECJZ}(a,j_0,J)$; en $J$ se dispone $\mathtt{INC}(a,j_+)$. El valor final de $a$ coincide exactamente con el inicial.

**Demostración.** En $\operatorname{Clr}$ la cantidad de iteraciones decrementales es el valor inicial natural del registro. En $\operatorname{Move}$ se mantiene el invariante $a+b=a_0+b_0$ y cada paso no terminal disminuye $a$ en una unidad, por lo que se alcanzará la salida $E$. En $\operatorname{Test0}$ la rama positiva resta y a continuación restituye una unidad, sin ejecutar la rama cero. En todos los casos el contador sólo visita etiquetas explicitadas. No hay instrucciones nuevas ni búsqueda no acotada cuyo éxito se dé por supuesto. $\square$


## 17.25. Copia conservativa con auxiliar restaurado

### Lema 17.25.1 — Copia conservativa con auxiliar restaurado {#tlog-lem-00058}

**Lema.** Para registros distintos $a,b,t$, con $t=0$, existe un macrobloque finito $\operatorname{Copy}(a,b;t)$ que termina con
$$
(a,b,t)_{\mathrm{final}}=(a_0,a_0,0),
$$
sin alterar los restantes registros observables. **No** exige que $b$ esté inicialmente vacío.

**Demostración.** Se ejecuta primero $\operatorname{Clr}(b)$. Después, mientras $a>0$, una instrucción $\mathtt{DECJZ}(a,E,J)$ disminuye $a$ y la ruta positiva ejecuta $\mathtt{INC}(b,J')$, $\mathtt{INC}(t,L)$, con retorno a la prueba en $L$. Se ha establecido, después de $k$ iteraciones, $a=a_0-k$, $b=k$, $t=k$. Tras $a_0$ iteraciones se llega a $(0,a_0,a_0)$. Finalmente $\operatorname{Move}(t,a)$ proporciona $(a_0,a_0,0)$. La inducción sobre $a_0\in\omega$ prueba terminación y exactitud. Todas las etiquetas y los registros satisfacen las guardas de §17.3. $\square$


## 17.26. Relocalización de registros y de etiquetas sin colisiones

### Proposición 17.26.1 — Relocalización de registros y de etiquetas sin colisiones {#tlog-pro-00110}

**Proposición.** Para cualesquiera listas finitas de instrucciones bien formadas y cualesquiera conjuntos finitos de registros y etiquetas prohibidos, existen asignaciones explícitas de nuevos registros/etiquetas disjuntas de los prohibidos. Se puede trasladar cada programa a un banco propio, y traducir cada destino a la nueva etiqueta que le corresponde, preservando el valor de los registros simulados.

**Demostración.** Dado un conjunto finito $F\subseteq\omega$, el menor natural mayor que todos sus elementos existe ($0$ si $F=\varnothing$); desde allí se asignan sucesivamente $r$ nombres. El control finito se ordena por el orden natural de los pares de números originales y, cuando haya más de dos coordenadas, por orden lexicográfico; se numera $0,\dots,N-1$. Cada $\mathtt{INC}(i,j)$ se transforma en $\mathtt{INC}(\widehat i,\widehat j)$ y cada $\mathtt{DECJZ}(i,j,k)$ en su versión con tres coordenadas relocalizadas. La inversa sobre cada imagen finita existe y permite recuperar exactamente las direcciones antiguas. Si las etiquetas finales se ampliarán con bloques auxiliares, se fija primero la lista de **todas** las etiquetas simbólicas del montaje y se resuelven conjuntamente los destinos. No se necesita escoger elementos de una familia infinita; las asignaciones se calculan a partir de conjuntos finitos explícitos. $\square$


## 17.27. Compilación de diagramas de control finito a programas RM

### Metateorema 17.27.1 — Compilación de diagramas de control finito a programas RM {#tlog-mth-00079}

**Metateorema (compilación).** Sea $G$ un diagrama **finito y no vacío** con entrada distinguida, vértices etiquetados por instrucciones $\mathtt{INC}$, $\mathtt{DECJZ}$ o las plantillas de §§17.24–17.25, y arcos hacia vértices del mismo diagrama; permite vértices terminales $\mathtt{HALT}$ y vértices de retorno o aviso al bloque llamador. Si cada macro cumple sus guardas de frescura, existe un programa bien formado $\operatorname{Compile}(G)$ cuya ejecución coincide con las transiciones abstractas entre entradas y salidas de bloques sobre todos los registros observables. Si el diagrama no llega nunca al vértice terminal, tampoco llega a una instrucción $\mathtt{HALT}$ del programa compilado.

**Demostración.** Se reemplaza cada llamada macro por una **copia textual finita** de su plantilla, con etiquetas internas y auxiliares disjuntos; los ciclos de ejecución permanecen como arcos, no como recursión de expansión de macros. Al ser finito $G$ y finitas las plantillas, el conjunto expandido de vértices es finito. Se ordena y numera canónicamente con su entrada original como etiqueta $0$, obteniendo un segmento $n$; se traduce cada arco a su índice en $n$. Se elige $r$ mayor que cada índice de registro utilizado y mayor o igual que la aridad de entrada. Las guardas $i<r$ y $j,k<n$ se satisfacen **por construcción**. Los casos de cuatro cláusulas de transición de §17.7 dan, por inspección de instrucciones, una simulación de cada arco primitivo; los lemas 17.24–17.25 justifican el paso por un macro completo. Concatenando los tramos finitos de ejecución se obtiene una simulación de todo recorrido. La instrucción terminal sólo se coloca en vértices terminales declarados: ninguna rama no terminal genera una parada espuria. El argumento entrega un **compilador de dos datos finitos fijos**, no un intérprete universal sobre códigos numéricos de programas. $\square$


## 17.28. Bloque de un paso de programa fijo con retorno

### Definición 17.28.1 — Bloque de un paso de programa fijo con retorno {#tlog-def-00116}

Fijado $P=(r,p)$ de longitud $n$, construimos una familia de bloques $\operatorname{Step}_P(\ell)$, uno por cada $\ell\in n$, actuando sobre un banco propio de $r$ registros. Si $p(\ell)$ es $\mathtt{INC}(i,j)$, incrementa el registro simulado $i$ y retorna señalando el índice $j$; si es $\mathtt{DECJZ}(i,j,k)$, ejecuta la prueba con decremento indicada y retorna $j$ o $k$ según el valor; si es $\mathtt{HALT}$, devuelve la **señal terminal**, sin ejecutar una parada nativa del programa anfitrión.

Los índices de retorno son **etiquetas de control finito** externas al banco de registros. En una composición de bloques, cada salida se conecta directamente con la entrada correspondiente al control siguiente. En particular, $\operatorname{Step}_P$ no recibe $P$ codificado como un natural ni lee una cinta de instrucciones variable: $P$ ya está fijado cuando se construye la familia finita.


## 17.29. Exactitud de la simulación de un paso y detección de HALT

### Lema 17.29.1 — Exactitud de la simulación de un paso y detección de HALT {#tlog-lem-00059}

**Lema.** Supongamos que el banco reservado a $P$ codifica el vector $\rho$ y el vértice de control externo es $\ell$. Entonces completar $\operatorname{Step}_P(\ell)$ produce exactamente la nueva configuración $E_P(\ell,\rho)$ si la instrucción no es terminal; en el caso terminal produce una señal de parada y conserva $\rho$. Nunca produce una señal terminal en un vértice que no contiene $\mathtt{HALT}$.

**Demostración.** Por lectura única de la primera coordenada de cada instrucción existen sólo tres casos. $\mathtt{INC}$ modifica una única coordenada y selecciona su destino explícito. $\mathtt{DECJZ}$ separa exhaustivamente el caso cero y el caso sucesor; la rama positiva decrementa una unidad y salta al segundo destino, de acuerdo con $E_P$. Para $\mathtt{HALT}$, la semántica absorbente de §17.7 deja los registros invariantes y el bloque señala la finalización del cálculo simulado. Los destinos pertenecen a $n$ por la buena formación. Todos los otros registros pertenecen a bancos disjuntos y son invariantes, salvo los registros de descarte ignorados. De aquí el resultado y la ausencia de falsos positivos. $\square$


## 17.30. Simuladores finitos de un programa individual

### Proposición 17.30.1 — Simuladores finitos de un programa individual {#tlog-pro-00111}

**Proposición.** Fijado $P\in\operatorname{Prog}_q$, existe una familia finita de bloques de control que simula tantos pasos de $P$ como sean necesarios, copia y conserva los $q$ registros iniciales en un banco disjunto, y alcanza una señal terminal **si y sólo si** $P$ termina en esa entrada. Si alcanza la señal, el registro designado como salida simulada coincide con $F_P^{(q)}(x)$.

**Demostración.** Se copian las entradas mediante §17.25 a los primeros $q$ registros del banco inicialmente vacío. Se enlazan los $n$ bloques $\operatorname{Step}_P(\ell)$ con sus destinos por §17.28. Por inducción en el número de pasos simulados, el control y los valores del banco representan $\operatorname{Run}_P(x,t)$; en una visita a $\mathtt{HALT}$ la señal aparece por §17.29. Si el original nunca alcanza un terminal, la simulación sólo visita bloques de instrucciones no terminales y por el teorema de compilación nunca llega a $\mathtt{HALT}$ de aceptación. Si se detiene, la lectura estable de §17.12 identifica su valor de salida. Los pasos auxiliares de cada bloque son finitos, pero no se supone una cota **uniforme en $x$** para el tiempo total. $\square$


## 17.31. Clausura bajo sustitución general de funciones parciales computables

### Metateorema 17.31.1 — Clausura bajo sustitución general de funciones parciales computables {#tlog-mth-00080}

**Metateorema (composición parcial, con todas las aridades).** Sean $q,m\in\omega$, $g:\omega^m\rightharpoonup\omega$ y $f_i:\omega^q\rightharpoonup\omega$ ($i<m$), todas parciales computables-RM. Entonces la función parcial
$$
 h(x)=g\bigl(f_0(x),\ldots,f_{m-1}(x)\bigr)
$$
es computable-RM, con dominio **exactamente**
$$
 \boxed{\operatorname{dom}(h)=\{x\in\omega^q:\forall i<m\ x\in\operatorname{dom}(f_i),\ (f_i(x))_{i<m}\in\operatorname{dom}(g)\}.}
$$
Se admite $m=0$ (ejecución de una función nularia) y $q=0$ (una única entrada vacía).

**Demostración.** Fijamos los programas testigo $P_i$ y $Q$; no hay familia arbitraria de decisiones, pues $m$ es finito. Se conserva $x$ en los registros iniciales del programa anfitrión, y se destinan bancos disjuntos a cada $P_i$ y a $Q$; la copia de cada coordenada se realiza mediante §17.25. Se simulan, **secuencialmente**, $P_0,\dots,P_{m-1}$. Si alguno no llega a su primera instrucción de parada, la simulación permanece en sus bloques y el anfitrión no termina. Al acabar $P_i$, su salida se copia a un registro fresco de resultados sin destruir el banco; concluida la lista, los $m$ valores se copian a los registros de entrada $0,\dots,m-1$ del banco $Q$, con los auxiliares de $Q$ a cero. Se simula $Q$; si termina, se borra el registro $0$ anfitrión y se copia allí la salida del banco $Q$, seguida de una única instrucción $\mathtt{HALT}$ real. La compilación finita de §17.27 garantiza que todos los saltos y bancos son válidos. Por inducción en los segmentos de ejecución, el anfitrión se detiene exactamente cuando las $m$ aplicaciones internas y la aplicación externa están definidas; su valor es $g((f_i(x))_{i<m})$. Para $m=0$ se omite la fase de $P_i$ y se carga la entrada nularia de $Q$; para $q=0$ se omite la copia de entradas originales. No se aplica en ningún punto una «regla de composición computable» sin construir el programa. $\square$


## 17.32. Proyecciones, sucesor y constantes son computables-RM

### Proposición 17.32.1 — Proyecciones, sucesor y constantes son computables-RM {#tlog-pro-00112}

**Proposición.** Para $q\ge1$ e $i<q$, la proyección $\pi_i^q(x)=x(i)$ es total computable-RM; también lo son la función sucesor $S:\omega\to\omega$ y cada constante $c_q:\omega^q\to\omega$, $c_q(x)=c$ para $c\in\omega$, incluso $q=0$.

**Demostración.** Si $i=0$, el programa $\mathtt{HALT}$ inmediato deja la primera entrada como salida. Para $i>0$ se mantiene el registro $i$, se borra el registro $0$ y se copia $i\to0$ con un auxiliar fresco, devolviéndolo a cero. El sucesor usa $\mathtt{INC}(0,1)$ seguido de $\mathtt{HALT}$. Para una constante se borra el registro $0$ y se encadenan exactamente $c$ incrementos de su contenido antes de detenerse (con $c=0$, ninguno). Las macros se expanden por §17.27 y terminan sobre todos los naturales porque sus ciclos disminuyen un registro fuente. Las entradas nularias tienen un único vector vacío; la instrucción de salida siempre se refiere al registro $0$, disponible porque $r\ge1$. $\square$


## 17.33. Suma y multiplicación son computables-RM

### Proposición 17.33.1 — Suma y multiplicación son computables-RM {#tlog-pro-00113}

**Proposición.** Las funciones $+:\omega^2\to\omega$ y $\cdot:\omega^2\to\omega$ son totales computables-RM.

**Demostración de la suma.** El anfitrión recibe $a$ en el registro $0$ y $b$ en $1$. El macro $\operatorname{Move}(1,0)$ decrementa $b$ veces el registro $1$ e incrementa simultáneamente el $0$; la salida es $a+b$ y el programa termina por inducción sobre $b$.

**Demostración del producto.** Se copian inicialmente $a$ a un registro $A$ y $b$ a un contador $B$, mientras un acumulador $T$ se inicializa en cero. Por cada unidad retirada de $B$, se copia $A$ a un registro temporal $U$ y se ejecuta $\operatorname{Move}(U,T)$, que suma $a$ al acumulador y deja $U$ vacío. El invariante después de $k\le b$ vueltas es $T=k\cdot a$ y $B=b-k$; tras $b$ vueltas $T=a\cdot b$. Se borra el registro anfitrión $0$ y se mueve $T$ a él. Cada bucle interno termina tras $a$ pasos y el externo tras $b$; sus auxiliares se inicializan en cero y los saltos quedan guardados por §17.27. Este razonamiento prueba **terminación efectiva** y no solamente existencia conjuntista de $a+b$ y $a\cdot b$. $\square$


## 17.34. Producto de controles finitos y planificación alternada

### Definición 17.34.1 — Producto de controles finitos y planificación alternada {#tlog-def-00117}

Sean $P=(r_P,p)$ y $Q=(r_Q,q')$ **programas fijos de la misma aridad de entrada** $a$, con longitudes $n_P,n_Q\ge1$. Reservamos bancos de registros disjuntos, inicialmente copiados desde la misma entrada $x\in\omega^a$. El conjunto de vértices de planificación es finito:
$$
 \mathcal D_{P,Q}=n_P\times n_Q\times\{0,1\}.
$$
En $v=(i,j,0)$ se ejecuta un solo paso simulado de $P$ y se pasa a $(i',j,1)$; en $(i,j,1)$ se ejecuta un paso de $Q$ y se pasa a $(i,j',0)$. Si la instrucción examinada es $\mathtt{HALT}$, el bloque no altera su banco y emite la señal $H_P$ o $H_Q$. Para verificar intersecciones se pueden añadir **dos indicadores finitos** $\sigma_P,\sigma_Q\in\{0,1\}$ al control, suprimiendo toda simulación de un programa ya detenido. Estas señales son arcos del programa **compilado**, no salidas de un oráculo.

Con las plantillas del §17.27 todo este diagrama se convierte en un programa RM bien formado. El nombre $\operatorname{Dovetail}(P,Q)$ designa sólo el **esquema finito de construcción de un programa desde dos programas ya fijados**, nunca una máquina universal que reciba las instrucciones de $P,Q$ como datos numéricos.


## 17.35. Justicia de la planificación e identidad de las dos órbitas

### Lema 17.35.1 — Justicia de la planificación e identidad de las dos órbitas {#tlog-lem-00060}

**Lema.** Antes de una señal terminal, después de $k$ ciclos completos de la planificación alternada, los dos bancos simulan las configuraciones $\operatorname{Run}_P(x,k)$ y $\operatorname{Run}_Q(x,k)$, respectivamente (salvo un desplazamiento finito de las instrucciones auxiliares del anfitrión). Por consiguiente, si uno de los dos programas alcanza $\mathtt{HALT}$ tras $t$ pasos, su señal aparece durante los primeros $t+1$ turnos propios; el otro programa no puede impedirla mediante divergencia.

**Demostración.** La base $k=0$ es la carga común de las entradas y los controles $(0,0,0)$. El paso alterna una ejecución exacta de $\operatorname{Step}_P(i)$ con una de $\operatorname{Step}_Q(j)$; por §17.29 sólo cambia el banco correspondiente y su control, de modo que las dos proyecciones reproducen las órbitas originales. Si cualquiera llega a instrucción terminal, la construcción emite su señal antes del paso siguiente. En la variante con indicadores, un banco que ya ha terminado se deja fijo y los turnos del otro prosiguen; esto conserva la justicia para toda rama no terminada. La propiedad no presupone un límite computable para $t$; sólo afirma que cualquier $t$ finito acaba siendo inspeccionado. $\square$


## 17.36. Doble semidecisión implica decidibilidad

### Metateorema 17.36.1 — Doble semidecisión implica decidibilidad {#tlog-mth-00081}

**Metateorema.** Para todo $a\in\omega$ y $R\subseteq\omega^a$,
$$
\boxed{\operatorname{Semi}_{\mathrm{RM}}(R)\land\operatorname{Semi}_{\mathrm{RM}}(\omega^a\setminus R)\Longrightarrow\operatorname{Dec}_{\mathrm{RM}}(R).}
$$

**Demostración constructiva.** Se fijan un reconocedor $P$ de $R$ y otro $Q$ de su complemento, ambos de aridad $a$. Compilamos el producto finito de §17.34 sobre bancos privados y copiamos allí la entrada. En una señal $H_P$ se ejecuta $\operatorname{Clr}(0)$, un único incremento del registro anfitrión de salida $0$ y $\mathtt{HALT}$; en una señal $H_Q$ se borra el registro $0$ y se ejecuta $\mathtt{HALT}$. En ambas ramas la salida final pertenece a $\{0,1\}$. Para cada $x\in\omega^a$, la ley del tercero excluido da $x\in R$ o $x\in\omega^a\setminus R$. En el primer caso $P$ se detiene en algún tiempo finito, por la propiedad de justicia aparece $H_P$; $Q$ no llega a $H_Q$ por exactitud de su dominio de parada. En el segundo caso las funciones se intercambian. Así el programa **siempre** termina, con salida característica correcta. No se infiere terminación de una consulta omnisciente a ambos programas: se obtiene mediante una planificación RM finita que permite progresar a los dos. El caso $a=0$ funciona porque la entrada es la secuencia vacía única y se copian cero coordenadas. $\square$


## 17.37. Caracterización de decisión por doble semidecisión

### Corolario 17.37.1 — Caracterización de decisión por doble semidecisión {#tlog-cor-00025}

**Corolario.** Para toda aridad $a$ y conjunto $R\subseteq\omega^a$,
$$
\boxed{\operatorname{Dec}_{\mathrm{RM}}(R)\iff\operatorname{Semi}_{\mathrm{RM}}(R)\land\operatorname{Semi}_{\mathrm{RM}}(\omega^a\setminus R).}
$$
**Demostración.** La implicación directa es la construcción explícita de dos reconocedores desde un decidor de §17.19 ([TLOG-PRO-00109](#tlog-pro-00109)). La inversa es el programa entrelazado de §17.36. Ambas direcciones son relativas al modelo RM concretamente construido y no dependen de una tesis de equivalencia de modelos. $\square$


## 17.38. Unión e intersección de relaciones semidecidibles

### Proposición 17.38.1 — Unión e intersección de relaciones semidecidibles {#tlog-pro-00114}

**Proposición.** Si $R,S\subseteq\omega^a$ son semidecidibles-RM, también lo son $R\cup S$ y $R\cap S$; el vacío y $\omega^a$ son semidecidibles-RM para toda aridad $a$.

**Demostración.** Para $R\cup S$ se compilan los reconocedores mediante §17.34, conectando **cualquiera** de las señales $H_P,H_Q$ a una instrucción terminal real. Por §17.35, termina exactamente si al menos uno de los programas termina. Para $R\cap S$ se amplía el control finito con dos indicadores de parada: al llegar $H_P$ se fija $\sigma_P=1$ y se deja de avanzar su banco; análogamente para $Q$. La instrucción terminal real se ejecuta solamente al tener $\sigma_P=\sigma_Q=1$. Si ambos programas paran, la planificación eventualmente ve ambos eventos; si uno no para, su indicador queda $0$ para siempre. Los estados de indicadores son cuatro vértices adicionales de tipo finito (replicados por las etiquetas de control), no una memoria infinita. $\varnothing$ es dominio de parada del programa divergente de §17.18; $\omega^a$ lo es del programa de parada inmediata. Se respetan aridad común y salida no relevante de los reconocedores. $\square$


## 17.39. Clausura booleana de las relaciones decidibles

### Proposición 17.39.1 — Clausura booleana de las relaciones decidibles {#tlog-pro-00115}

**Proposición.** Para $R,S\subseteq\omega^a$ decidibles-RM son decidibles-RM $R\cup S$, $R\cap S$, $\omega^a\setminus R$, $R\setminus S$ y $R\triangle S$.

**Demostración.** Por §17.37, los dos lados de cada relación decidible son semidecidibles. §17.38 prueba la clausura de semidecidibles por unión/intersección; además, $\omega^a\setminus(R\cup S)=R^c\cap S^c$ y $\omega^a\setminus(R\cap S)=R^c\cup S^c$. Los dos lados de las uniones e intersecciones son por tanto semidecidibles; la equivalencia de §17.37 devuelve decidibilidad. El complemento intercambia los dos reconocedores y es decidible; diferencia y diferencia simétrica se expresan mediante un número **finito** de uniones, intersecciones y complementos. Las igualdades de conjuntos son puramente conjuntistas y no introducen decisiones externas. $\square$


## 17.40. Preimágenes semidecidibles y decidibles por mapas computables

### Metateorema 17.40.1 — Preimágenes semidecidibles y decidibles por mapas computables {#tlog-mth-00082}

**Metateorema.** Si $f:\omega^a\rightharpoonup\omega$ es parcial computable-RM y $R\subseteq\omega$ semidecidible-RM, entonces
$$
 S_f(R):=\{x\in\operatorname{dom}(f):f(x)\in R\}
$$
es semidecidible-RM. Si $f$ es **total** y $R$ decidible-RM, entonces $f^{-1}[R]$ es decidible-RM.

**Demostración.** Sea $P$ un programa para $f$ y $Q$ un reconocedor cuyo dominio de parada es $R$. Se ejecuta la composición secuencial $Q\circ P$ de §17.31, permitiendo que $Q$ reciba como única entrada el resultado de $P$. Su parada ocurre exactamente cuando $P$ termina y $Q$ se detiene en $f(x)$, lo que equivale a la pertenencia a $S_f(R)$. Para la segunda afirmación se sustituye $Q$ por un **decidor total** de $R$, conservando su resultado característico $0$ o $1$. Puesto que $f$ es total, la composición es total y reproduce la función característica de $f^{-1}[R]$. Si $f$ fuese parcial, la misma construcción sería parcial y **no** justificaría la decidibilidad de una preimagen sobre todo $\omega^a$ sin una condición adicional de dominio. $\square$


## 17.41. Cierre operativo del capítulo y frontera de aritmetización

### Corolario 17.41.1 — Cierre operativo del capítulo y frontera de aritmetización {#tlog-cor-00026}

**Corolario de salida arquitectónica.** El sistema RM está construido sobre conjuntos y configuraciones finitos dentro de $\mathsf M_{\mathrm{ext}}$; posee compilación finita de programas fijos, clausura bajo composición general de funciones parciales, programas totales de proyección, constantes, sucesor, suma y producto, simulación intercalada de dos programas fijos, equivalencia exacta de decidibilidad con doble semidecisión y clausuras booleanas elementales. La distinción «definible en ZF» $\not\Rightarrow$ «computable-RM» queda intacta.

**Demostración.** Cada componente se apoya en resultados anteriores del propio capítulo, sin importar pruebas de otros tratados. El programa compilado obtenido en cada punto usa exclusivamente $\mathtt{HALT}$, $\mathtt{INC}$ y $\mathtt{DECJZ}$ con registros y destinos guardados. No se ha establecido todavía: (a) numeración efectiva $P\mapsto\ulcorner P\urcorner$; (b) máquina universal que procese una descripción variable; (c) equivalencia entre c.e.-RM por dominio y enumeración de imágenes de una función **total** en una codificación de tuplas; (d) equivalencia con máquinas de Turing; (e) indecidibilidad de la parada; (f) representabilidad de relaciones computables dentro de una teoría aritmética. La construcción de códigos numéricos y predicados sintácticos pertenece al Capítulo 18, la representabilidad al 19 y la diagonalización al 20. **Ninguna** de estas obligaciones queda disfrazada de teorema cerrado. $\square$


## 17.42. Cierre matemático, editorial y fronteras de transferencia

El capítulo contiene **40 resultados cerrados** (20 de M01 y 20 de M02). Queda demostrada la salida aprobada de computabilidad **mínima** para la metamatemática. No se ha producido codificación numérica de programas ni de expresiones, ni un simulador universal, ni equivalencia con modelos alternativos. Estos puntos se distinguen como obligaciones independientes de los siguientes capítulos; no son hipótesis ocultas de las pruebas de M02. El argumento de simulación finita utiliza etiquetas de control **incrustadas en un programa ya compilado**, no análisis por un programa de una descripción variable recibida como dato.

La auditoría del DAG y la persistencia de la versión definitiva se registran separadamente en `TLOG_CH17_M02_AUDIT_v01.md`, `TLOG_CH17_CLOSURE_AUDIT_v01.md` y el certificado de readback. No se activan interfaces con GAS/FND ni se declara formalización Lean o publicación web.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 16](capitulo-16.md) · [Capítulo 18 →](capitulo-18.md)

