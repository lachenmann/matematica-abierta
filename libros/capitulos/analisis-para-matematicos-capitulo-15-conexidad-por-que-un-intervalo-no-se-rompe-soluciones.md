---
content-id: MA-BCH-0264
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-015-SOLUCIONES
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: Soluciones — Capítulo 15
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C15_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Ejercicios](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-microcontroles.html)

## 15.1. Una separación relativa verificable

[]{#MA-EX-ANM-01-015-001}

[]{#MA-SOL-ANM-01-015-001}

[]{#MA-SEC-ANM-01-015-001}

Tomamos $A=E\cap(-\infty,0)=[-3,-1]$ y $B=E\cap(0,\infty)=[2,4]$. Los rayos son abiertos reales, así las partes son abiertas relativas a $E$. $-2\in A$ y $3\in B$ prueban no vacuidad. Las desigualdades $x<0$ y $x>0$ son incompatibles, dando disjunción; todo punto de $E$ está en uno de los segmentos y por ello en una parte, dando cobertura. Ninguno de los segmentos es abierto real: cualquier bola alrededor de su extremo exterior contiene puntos que no pertenecen al segmento. El ambiente relativo es indispensable.

**Retorno visual.** Véase [C15-F01](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.2. Una partición que no rompe el intervalo

[]{#MA-EX-ANM-01-015-002}

[]{#MA-SOL-ANM-01-015-002}

Ambas partes son no vacías, disjuntas y cubren $E$. Además $A=E\cap(-\infty,1)$ es abierta relativa. $B$ no lo es en $1$: dado $r>0$, ponemos $h=\min(r/2,1/2)>0$, $t=1-h$. Entonces $t\in[0,1)\subseteq E$, $|t-1|=h<r$ y $t\notin B$. Ningún radio de $1$ dentro de $E$ queda en $B$. Por eso la partición no es separación.

**Retorno visual.** Véase [C15-F01](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.3. Equivalencia por complemento

[]{#MA-EX-ANM-01-015-003}

[]{#MA-SOL-ANM-01-015-003}

Si $E$ es conexo y $A$ es abierto y cerrado relativo, $E\setminus A$ es abierto relativo. Si $A$ no fuese vacío ni todo $E$, las dos partes serían no vacías, disjuntas y exhaustivas, separando $E$. Luego $A=\varnothing$ o $A=E$. Recíprocamente, una separación $A,B$ da $B=E\setminus A$; la apertura de $B$ hace a $A$ cerrado relativo y la de $A$ ya está dada. Por no vacuidad de ambas partes $A$ es no vacío y propio, contradiciendo el criterio. Si $E$ es vacío, su único subconjunto es vacío y no puede existir separación; ambas afirmaciones se cumplen.

## 15.4. Separar un conjunto finito

[]{#MA-EX-ANM-01-015-004}

[]{#MA-SOL-ANM-01-015-004}

Vacío y singleton no pueden dividirse en dos partes disjuntas no vacías, luego son conexos. Si el conjunto finito tiene al menos dos puntos, se puede ordenar como $t_1<\cdots<t_m$ con $m\ge2$, usando repetidamente el menor de una lista finita por comparación. Sea $c=(t_1+t_2)/2$. No pertenece al conjunto porque está entre sus dos primeros puntos. Las partes $E\cap(-\infty,c)=\{t_1\}$ y $E\cap(c,\infty)$ son abiertas relativas, disjuntas y exhaustivas; contienen $t_1$ y $t_2$. Son una separación. Sólo se usó una lista finita y el orden real.

## 15.5. Ambientes anidados

[]{#MA-EX-ANM-01-015-005}

[]{#MA-SOL-ANM-01-015-005}

Escribimos $A=E\cap U$ con $U$ abierto real. Como $F\subseteq E$, $F\cap A=F\cap U$, abierto relativo a $F$. Para una separación $A,B$ de $E$, sus intersecciones con $F$ siguen siendo abiertas relativas, disjuntas y exhaustivas. Pero alguna puede ser vacía: con $E=[-2,-1]\cup[1,2]$, sus dos segmentos como partes y $F=[1,2]$, la intersección de la primera parte con $F$ es vacía. Por ello no queda una separación de $F$.

## 15.6. Preparar un supremo legítimo

[]{#MA-EX-ANM-01-015-006}

[]{#MA-SOL-ANM-01-015-006}

[]{#MA-SEC-ANM-01-015-002}

$S=A\cap[a,b]$ contiene $a$ y todos sus elementos son menores o iguales que $b$. Completitud da $c=\sup S$. Como $a\in S$, $a\le c$; como $b$ es cota, $c\le b$. La hipótesis intervalar da $[a,b]\subseteq I$, luego $c\in I=A\cup B$. La cobertura asigna una parte y la disjunción impide que pertenezca a ambas. Sin intervalaridad, $c$ podría faltar en el dominio y no habría esa dicotomía.

## 15.7. Reparar un avance fuera del dominio

[]{#MA-EX-ANM-01-015-007}

[]{#MA-SOL-ANM-01-015-007}

La apertura relativa sólo garantiza pertenencia a $A$ de puntos de $I$ próximos a $c$. El punto $c+r/2$ puede superar $b$ y hasta salir de $I$; por ejemplo $c=0.9$, $b=1$, $r=1$ da $d=1.4$. En el argumento correcto, $c<b$ porque $b\in B$ y $c\in A$. Ponemos $h=\min((b-c)/2,r/2)>0$, $d=c+h$. Entonces $c<d<b$, $d\in[a,b]\subseteq I$ y $|d-c|<r$. La apertura da $d\in A$, luego $d\in S$, en contradicción con $d>\sup S$. La reparación usa por separado dominio y radio.

**Retorno visual.** Véase [C15-F02](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.8. La propiedad aproximante necesaria

[]{#MA-EX-ANM-01-015-008}

[]{#MA-SOL-ANM-01-015-008}

$c-s/2<c$ no es cota superior de $S$, porque sería una cota menor que la menor cota superior $c$. Por negación de la condición de cota existe $t\in S$ con $t>c-s/2$. Además $t\le c$ pues $c$ sí es cota. Como $S\subseteq A$ y $c\in B$, la disjunción da $t\ne c$. Así $0<c-t<s/2<s$, y $t\in I$ pertenece a la vecindad de $c$ dentro de $I$, que está en $B$. Queda $t\in A\cap B$, contradicción. Sólo se usó un testigo para este radio.

## 15.9. La completitud en el paso correcto

[]{#MA-EX-ANM-01-015-009}

[]{#MA-SOL-ANM-01-015-009}

El orden racional no garantiza un supremo racional para todo subconjunto racional no vacío acotado. Si se toma el supremo en $\mathbb R$, puede quedar fuera del dominio racional y la dicotomía «pertenece a una parte» falla. El corte $c=\sqrt2\notin\mathbb Q$ da las partes racionales menores y mayores que $c$. Son abiertas relativas, disjuntas, exhaustivas y no vacías por los testigos $1$ y $2$. La densidad racional no incorpora a $c$ ni subsana el gasto de completitud y pertenencia.

## 15.10. Intervalos no acotados y degenerados

[]{#MA-EX-ANM-01-015-010}

[]{#MA-SOL-ANM-01-015-010}

En la semirrecta, si $u\le v$ son miembros, todo $t\in[u,v]$ satisface $t\ge u>a$, así también pertenece. La recta contiene todos sus segmentos. Singleton y vacío satisfacen el predicado intervalar vacíamente o con segmentos degenerados. R2 los hace conexos. Su prueba acota sólo $S=A\cap[u,v]$ después de fijar dos puntos de una supuesta separación; no necesita acotar todo el intervalo. En vacío y singleton no hay dos puntos de partes disjuntas no vacías, de modo que la separación ya es imposible.

## 15.11. Un punto omitido suficiente

[]{#MA-EX-ANM-01-015-011}

[]{#MA-SOL-ANM-01-015-011}

[]{#MA-SEC-ANM-01-015-003}

La unión anterior a quitar $2$ es $[0,3]$, pues $1$ está en la primera pieza. Por tanto $E=[0,3]\setminus\{2\}$. Tomamos $A=E\cap(-\infty,2)=[0,2)$ y $B=E\cap(2,\infty)=(2,3]$. Son abiertas relativas por los rayos, disjuntas y cubren $E$ porque $2$ fue omitido. Son no vacías por $0$ y $3$. $1$ no es hueco: pertenece a $E$. Las modalidades de extremos de cada pieza no deben leerse aisladas de la unión.

## 15.12. Densidad y ruptura

[]{#MA-EX-ANM-01-015-012}

[]{#MA-SOL-ANM-01-015-012}

Usamos $c=\sqrt2$, real irracional, y $A=\mathbb Q\cap(-\infty,c)$, $B=\mathbb Q\cap(c,\infty)$. Las partes son abiertas relativas, disjuntas y cubren los racionales por $c\notin\mathbb Q$. $1\in A$, $2\in B$. Para todo $r>0$, densidad racional da un punto en $(c-r,c)$ y otro en $(c,c+r)$, pertenecientes a las partes respectivas. Aproximación arbitraria al corte es compatible con separación: el punto límite común está fuera del ambiente racional.

**Retorno visual.** Véase [C15-F03](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.13. Intersecciones y uniones

[]{#MA-EX-ANM-01-015-013}

[]{#MA-SOL-ANM-01-015-013}

Si $x,y$ pertenecen a la intersección, están en cada intervalo de la familia, y el segmento entre ellos está en cada miembro, luego en la intersección. Es intervalo y R2 da conexidad. Para una familia sin miembros, la intersección relativa a $\mathbb R$ es toda $\mathbb R$, también intervalo. La unión falla para $(0,1)\cup(2,3)$: $1/2$ y $5/2$ pertenecen pero $3/2$ no; R3 da desconexión o se exhibe el corte por $3/2$.

## 15.14. Una familia con punto común

[]{#MA-EX-ANM-01-015-014}

[]{#MA-SOL-ANM-01-015-014}

Supongamos una separación $H=A\cup B$ y, intercambiando nombres, $p\in A$. Para cada índice fijo $i$, las partes $E_i\cap A$ y $E_i\cap B$ son abiertas relativas a $E_i$, disjuntas y exhaustivas. La primera contiene el punto común $p$. Si la segunda fuese no vacía, separaría $E_i$; por conexidad es vacía. Se ha probado para todo $i$ que $E_i\subseteq A$. Por definición de unión, $H\subseteq A$, luego $B=\varnothing$, contradicción. El punto $p$ es único testigo compartido fijado desde la hipótesis; no se produce una familia de elecciones.

## 15.15. Cerrar un intervalo sin romperlo

[]{#MA-EX-ANM-01-015-015}

[]{#MA-SOL-ANM-01-015-015}

Para $I=\varnothing$, ninguna vecindad toca $I$ y su adherencia es vacía. En el resto, tomemos $u<v$ en $\overline I$ y $u<t<v$. La vecindad de $u$ de radio $(t-u)/2$ toca $I$, dando $a\in I$ con $a<t$. La de $v$ de radio $(v-t)/2$ da $b\in I$ con $t<b$. Intervalaridad implica $t\in[a,b]\subseteq I\subseteq\overline I$. Los extremos $u,v$ ya están en la adherencia. Así todo segmento entre miembros está en ella, y es intervalo. R2 prueba conexidad. Sólo se fijaron dos testigos de vecindades para el punto $t$ considerado.

## 15.16. Separación de valores a entradas

[]{#MA-EX-ANM-01-015-016}

[]{#MA-SOL-ANM-01-015-016}

[]{#MA-SEC-ANM-01-015-004}

Sea $h=f\upharpoonright E$, continua. Si $H=f[E]$ se separara como $A=H\cap V$, $B=H\cap W$ con $V,W$ abiertos reales, tomamos $P=\{x\in E:h(x)\in A\}=h^{-1}[V]$ y $Q=h^{-1}[W]$. Son abiertos relativos a $E$, mientras $A,B$ lo eran a $H$. Disjunción y cobertura se trasladan porque toda salida de $h$ está en $H=A\cup B$. Para un valor concreto en cada parte, pertenecer a $H$ da una entrada en $E$ con esa salida; ambas preimágenes son no vacías. Así separan $E$, contradicción. Si $E$ es vacío, su imagen es vacía y ya es conexa. No se usa inversa funcional ni selector de todas las fibras.

## 15.17. La preimagen que se divide

[]{#MA-EX-ANM-01-015-017}

[]{#MA-SOL-ANM-01-015-017}

La ecuación $x^2=1$ equivale a $(x-1)(x+1)=0$, luego la preimagen es $\{-1,1\}$. Sus dos singletons se obtienen cortando por cero; son abiertos relativos, disjuntos y no vacíos, y cubren la preimagen. No es conexa. $q$ es continua por C14, su dominio $[-2,2]$ es conexo y $\{1\}$ también. Nada contradice R4: el teorema preserva conexidad por imagen directa, no por preimagen.

## 15.18. Una imagen global intervalar no certifica continuidad

[]{#MA-EX-ANM-01-015-018}

[]{#MA-SOL-ANM-01-015-018}

La primera rama tiene imagen $[-1,0)$ y la segunda $[-1,0]$, luego la imagen total es $[-1,0]$, intervalo. Pero $f(0)=-1$. Dado $\delta>0$, ponemos $t=\min(\delta/2,1/4)>0$, $x=-t\in[-1,0)$. Entonces $|x|<\delta$ y $|f(x)-f(0)|=1-t\ge3/4>1/2$. La tolerancia $1/2$ refuta continuidad en cero. El resultado de preservación es una implicación con continuidad como premisa; que la imagen total sea intervalar no prueba controles locales ni el valor intermedio en cada subsegmento.

## 15.19. El criterio de dos valores

[]{#MA-EX-ANM-01-015-019}

[]{#MA-SOL-ANM-01-015-019}

Si $E$ es conexo, R4 da imagen conexa de $u$ como subconjunto real. Una imagen que contuviera $0$ y $1$ sería exactamente $\{0,1\}$, que omite $1/2$ y no es intervalo; contradicción con R3. Así no hay dos entradas con salidas distintas, que es constancia. Si $E$ tuviera separación $A,B$, definimos $u=0$ en $A$, $u=1$ en $B$. Cobertura/disjunción hacen válida la función. Para cada entrada, una bola relativa contenida en su parte hace el error cero, dando continuidad para todo $\varepsilon>0$. Las dos partes no vacías dan salidas diferentes, contradicción con el criterio. En vacío la condición de constancia es universal vacía y no se exige valor alcanzado.

## 15.20. Conexidad preservada por homeomorfismo

[]{#MA-EX-ANM-01-015-020}

[]{#MA-SOL-ANM-01-015-020}

Si $E$ es conexo, continuidad de $f$ y sobreyectividad dan $F=f[E]$ conexo por R4. Si $F$ es conexo, la inversa $h:F\to E$ es continua y sobreyectiva sobre $E$, luego $E=h[F]$ es conexo. Para una continua sobreyectiva sin inversa continua sólo está garantizada la primera dirección. La constante $\{-1,1\}\to\{0\}$ es continua y sobreyectiva; el codominio es conexo y el dominio no. No hay inversa funcional en ese ejemplo, lo cual ya basta para refutar la recíproca general.

## 15.21. Localización con orientación invertida

[]{#MA-EX-ANM-01-015-021}

[]{#MA-SOL-ANM-01-015-021}

[]{#MA-SEC-ANM-01-015-005}

$[v,u]\subseteq I$ por intervalaridad. La restricción continua a ese segmento tiene imagen intervalar que contiene $f(u)$ y $f(v)$, por R4 y R3. Contiene el valor intermedio $y$, así existe $c\in[v,u]$ con $f(c)=y$. Las desigualdades estrictas hacen $y$ distinto de las dos salidas extremas, luego $c\ne u,v$ y $c\in(v,u)$. El orden de las salidas no tiene que coincidir con el de los argumentos.

## 15.22. Existencia y unicidad por pruebas distintas

[]{#MA-EX-ANM-01-015-022}

[]{#MA-SOL-ANM-01-015-022}

$F$ es continua por álgebra polinomial de C14. $F(0)=-1<0$ y $F(1)=1>0$, así R5 da una raíz interior. Para $0\le x<z\le1$, $F(z)-F(x)=(z-x)(z^2+zx+x^2+1)>0$, porque el primer factor es positivo y el segundo al menos $1$. Por tanto es estrictamente creciente en el segmento y no puede tener dos ceros. Existencia e interioridad vienen del valor intermedio; unicidad viene de la desigualdad algebraica independiente.

**Retorno visual.** Véase [C15-F04](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.23. Una coincidencia de dos continuas

[]{#MA-EX-ANM-01-015-023}

[]{#MA-SOL-ANM-01-015-023}

$h=f-g$ es continua por C14. En cero es negativa y en uno positiva, luego R5 da $c\in(0,1)$ con $h(c)=0$, es decir $f(c)=g(c)$. No se garantiza unicidad. Por ejemplo $f(x)=(x-1/4)(x-1/2)(x-3/4)$ y $g(x)=0$ cumplen $f(0)=-3/32<0$, $f(1)=3/32>0$ y coinciden en tres entradas interiores distintas. Todas las funciones indicadas son polinomiales o constantes y por ello continuas.

## 15.24. Sin ceros, un signo

[]{#MA-EX-ANM-01-015-024}

[]{#MA-SOL-ANM-01-015-024}

Fijamos $a\in I$. Como $f(a)\ne0$, es positivo o negativo. Si fuese positivo y hubiera $b$ con $f(b)<0$, R5 produciría cero entre $a,b$, contradicción. Todos los valores son no negativos y, al no haber ceros, positivos. El caso $f(a)<0$ es simétrico. Sin intervalaridad, $f(x)=1/x$ en $\mathbb R\setminus\{0\}$ es continua por C14, no tiene ceros y toma $-1$ y $1$. El punto omitido impide aplicar R5 entre esos argumentos.

## 15.25. Inclusión no es descripción de toda la imagen

[]{#MA-EX-ANM-01-015-025}

[]{#MA-SOL-ANM-01-015-025}

Para $f(x)=x^2$ en $[-2,2]$, ambos extremos valen $4$, pero $f(0)=0$. La fórmula propuesta daría sólo $\{4\}$, y es falsa. La imagen es de hecho $[0,4]$: todo cuadrado del dominio está ahí, y para cada $y\in[0,4]$ la raíz positiva $\sqrt y\in[0,2]$ da la preimagen. R5 garantiza la inclusión del segmento entre las dos salidas extremas dentro de la imagen. No garantiza que no haya otros valores; identificar extremos globales alcanzados requiere argumentos adicionales.

## 15.26. Tres actualizaciones exactas

[]{#MA-EX-ANM-01-015-026}

[]{#MA-SOL-ANM-01-015-026}

[]{#MA-SEC-ANM-01-015-006}

$M_0=1/2$ y $F(M_0)=1/8+1/2-1=-3/8<0$, así $[L_1,U_1]=[1/2,1]$. $M_1=3/4$ y $F(M_1)=27/64+48/64-64/64=11/64>0$, así $[L_2,U_2]=[1/2,3/4]$. $M_2=5/8$ y $F(M_2)=125/512+320/512-512/512=-67/512<0$, así $[L_3,U_3]=[5/8,3/4]$. Su medio es $M_3=11/16$. La raíz encerrada $c$ satisface $|M_3-c|\le(3/4-5/8)/2=1/16$. Se usaron tres evaluaciones/actualizaciones; no se evaluó $M_3$ para obtener esta cota.

**Retorno visual.** Véase [C15-F05](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.27. Número de actualizaciones

[]{#MA-EX-ANM-01-015-027}

[]{#MA-SOL-ANM-01-015-027}

Después de $n$ actualizaciones, el error es a lo sumo $3/2^{n+1}$. Buscamos que esa cota sea estrictamente menor que $1/1000$, equivalente a $2^{n+1}>3000$. Para $n=11$, $2^{12}=4096>3000$, así sirve; $n=10$ no lo garantiza pues $2048<3000$. En general se elige $n\in\mathbb N$ con $2^{n+1}>(b-a)/\tau$. Una cota igual a $\tau$ sólo garantiza error menor o igual, no estricto. Si hubo cero exacto antes, se dispone de error cero.

## 15.28. El cero límite sin compacidad

[]{#MA-EX-ANM-01-015-028}

[]{#MA-SOL-ANM-01-015-028}

Los $L_n$ están acotados por $b$ y el conjunto no vacío tiene supremo $c$. Para un $n$ fijo, si $k\le n$, $L_k\le L_n\le U_n$; si $k>n$, anidamiento da $L_k\le U_k\le U_n$. Así $U_n$ es cota de todos los inferiores y $L_n\le c\le U_n$. En particular $c\in[a,b]$. De $0\le c-L_n\le(b-a)/2^n$ y $0\le U_n-c\le(b-a)/2^n$ resultan ambas convergencias a $c$. Continuidad directa da $g(L_n),g(U_n)\to g(c)$. Una sucesión negativa no puede converger a un real positivo, pues una tolerancia de la mitad de ese real haría los términos positivos; análogamente la positiva no converge a negativo. Así $g(c)\le0$ y $g(c)\ge0$, luego vale cero. No se usó selección de rutas ni recíproca secuencial.

## 15.29. Longitud frente a residual

[]{#MA-EX-ANM-01-015-029}

[]{#MA-SOL-ANM-01-015-029}

Para $A>0$ definimos $g_A(x)=A(x-\ell/4)$ en $[0,\ell]$. Es continua, $g_A(0)=-A\ell/4<0$, $g_A(\ell)=3A\ell/4>0$, y su raíz es $\ell/4$. El medio $\ell/2$ tiene error posicional $\ell/4$, compatible con la cota $\ell/2$, pero residual $|g_A(\ell/2)|=A\ell/4$. Dado cualquier candidato finito $B\ge0$ para esa longitud, elegimos $A>4B/\ell$, y el residual supera $B$. La longitud no controla la escala vertical; haría falta información cuantitativa adicional de la función.

## 15.30. Una evaluación incierta

[]{#MA-EX-ANM-01-015-030}

[]{#MA-SOL-ANM-01-015-030}

La inclusión permite valores negativos, cero y positivos, por lo que no certifica $g(M)<0$. Sustituir el extremo inferior puede destruir el invariante si el valor es positivo. Un certificado contenido estrictamente en $(-\infty,0)$ autoriza reemplazar el inferior; uno contenido estrictamente en $(0,\infty)$ autoriza reemplazar el superior. Una igualdad exacta certificada $g(M)=0$ autoriza detener con raíz exacta. Si el intervalo de evaluación contiene cero, se requiere refinar o conservar el encierro anterior y declarar que no se decidió el signo; no se deduce igualdad de una tolerancia pequeña. La recurrencia clásica no proporciona por sí sola esos certificados computacionales.

## 15.31. Excluir un pico por dos fibras

[]{#MA-EX-ANM-01-015-031}

[]{#MA-SOL-ANM-01-015-031}

[]{#MA-SEC-ANM-01-015-007}

Inyectividad hace distintos los tres valores. Si $f(y)>\max(f(x),f(z))$, tomamos $w=(f(y)+\max(f(x),f(z)))/2$. Es estrictamente intermedio en cada par de salidas de $[x,y]$ y $[y,z]$. R5 entrega $s\in(x,y)$ y $t\in(y,z)$ con $f(s)=w=f(t)$; como $s<t$, contradice inyectividad. Si $f(y)<\min(f(x),f(z))$, usamos el punto medio entre esas dos cantidades y repetimos. Las posibilidades restantes son precisamente $f(x)<f(y)<f(z)$ o $f(z)<f(y)<f(x)$.

## 15.32. Propagar una orientación

[]{#MA-EX-ANM-01-015-032}

[]{#MA-SOL-ANM-01-015-032}

Ordenamos los puntos distintos de $\{a,b,x,y\}$ como $t_1<\cdots<t_m$, con $2\le m\le4$. Si $m=2$, ambos pares son el mismo y la conclusión está dada. Si $m\ge3$, para cada triple consecutivo la propiedad implica que las diferencias adyacentes $f(t_{i+1})-f(t_i)$ y $f(t_{i+2})-f(t_{i+1})$ tienen igual signo estricto. Por propagación a lo largo de la lista todas tienen el mismo signo. Si fuese negativo, sumando las diferencias entre las posiciones de $a$ y $b$ resultaría $f(b)<f(a)$, contradicción. Todas son positivas; sumando entre $x$ e $y$ obtenemos $f(y)>f(x)$. El procedimiento trata puntos exteriores al par fijado y no se limita a un subintervalo.

## 15.33. Barrera en un extremo del dominio

[]{#MA-EX-ANM-01-015-033}

[]{#MA-SOL-ANM-01-015-033}

La imagen es $J=[0,1)$: los cuadrados pertenecen a ese intervalo y cada $y\in J$ tiene raíz no negativa menor que $1$. La función es inyectiva creciente ahí, pues para $0\le x<z<1$, $z^2-x^2=(z-x)(z+x)>0$. Su inversa $h$ está definida. Si $0<\varepsilon<1$, tomamos el punto barrera $r=\varepsilon/2\in[0,1)$ y $\eta=r^2=\varepsilon^2/4$. Si $y\in J$ y $|y|<\eta$, su preimagen no puede ser $x\ge\varepsilon$, pues entonces $x>r$ y $y=x^2>r^2=\eta$. Así $|h(y)-h(0)|=x<\varepsilon$. Si $\varepsilon\ge1$, toda preimagen satisface $0\le x<1\le\varepsilon$, por lo que sirve $\eta=1$. No hay barrera izquierda porque todas las entradas son no negativas.

**Retorno visual.** Véase [C15-F06](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.34. Crecimiento con salto

[]{#MA-EX-ANM-01-015-034}

[]{#MA-SOL-ANM-01-015-034}

En cada rama la diferencia entre salidas es la diferencia entre entradas y es positiva. Si $x<0\le z$, $k(x)=x<0<1\le z+1=k(z)$, así también crece entre ramas. Pero $k(0)=1$; dado $\delta>0$, $x=-\min(\delta/2,1/2)$ tiene $|x|<\delta$ y $|k(x)-k(0)|=1-x>1$, refutando continuidad con tolerancia $1$. La imagen es $(-\infty,0)\cup[1,\infty)$, no intervalo. Falta continuidad en la premisa de R7; estricto crecimiento solo no la garantiza.

## 15.35. Por qué el dominio intervalar importa para la inversa

[]{#MA-EX-ANM-01-015-035}

[]{#MA-SOL-ANM-01-015-035}

Las imágenes de las piezas son $[0,1)$ y $[1,2]$, disjuntas y exhaustivas de $[0,2]$; cada rama es inyectiva, de modo que $f$ es biyección. En cualquier centro de $D$, el radio $\delta=\min(1/2,\varepsilon)$ evita la otra pieza y dentro de la misma rama el error de salida es la distancia de entradas, menor que $\varepsilon$. Así $f$ es continua relativa. La inversa vale $h(y)=y$ para $y<1$ y $h(y)=y+1$ para $y\ge1$, luego $h(1)=2$. Dado $\eta>0$, $t=\min(\eta/2,1/2)>0$ da $y=1-t\in[0,1)$ con $|y-1|<\eta$ y $|h(y)-2|=1+t>1$. Falla continuidad con tolerancia $1$. $D$ omite puntos entre $0$ y $2$ y no es intervalo; ésa es la premisa faltante de R7.

## 15.36. Relación por segmentos

[]{#MA-EX-ANM-01-015-036}

[]{#MA-SOL-ANM-01-015-036}

[]{#MA-SEC-ANM-01-015-008}

Reflexividad usa $[x,x]=\{x\}\subseteq D$; simetría usa que min/max no cambian al permutar. Si $x\sim y$ y $y\sim z$, los dos segmentos comparten $y$ y su unión es intervalo contenido en $D$, por §15.3; contiene $x,z$, luego también el segmento entre ellos. Así $x\sim z$. Si $u,v$ están en $C_x$, transitividad da $u\sim v$. Todo $t$ entre ellos está en $D$ y satisface $u\sim t$ porque su segmento con $u$ queda en el de $u,v$. De $x\sim u$ resulta $x\sim t$, así $t\in C_x$. Es intervalo.

## 15.37. Un dominio con tres componentes

[]{#MA-EX-ANM-01-015-037}

[]{#MA-SOL-ANM-01-015-037}

Las tres piezas son intervalos, luego conexas. Ningún conexo de $D$ puede tocar dos piezas: si tocara la izquierda y otra, omitiría un punto entre $-1$ y $0$, como $-1/2$; si tocara cero y la derecha, omitiría $1/2$. Por R3 no sería conexo. Cada pieza es por tanto máxima y es componente. Son todas abiertas relativas: la izquierda es $D\cap(-\infty,-1/2)$, el singleton $D\cap(-1/2,1/2)$ y la derecha $D\cap(1/2,\infty)$. También son cerradas relativas por R8 o porque el complemento de cada una es unión de las otras dos abiertas relativas. No todas son cerradas reales, pues los extremos $-2$ y $3$ faltan.

## 15.38. Componentes acumuladas sin apertura

[]{#MA-EX-ANM-01-015-038}

[]{#MA-SOL-ANM-01-015-038}

Todos los puntos de $D$ son racionales. Entre dos distintos hay un irracional por densidad de irracionales; éste no pertenece a $D$. El segmento entre los puntos no queda en $D$, así ninguna clase contiene dos puntos. Para $t_n=1/(n+1)$ con $n\ge1$, las distancias a sus vecinos $t_{n-1}$ y $t_{n+1}$ son positivas; la mitad del menor de ellas da una bola relativa que sólo contiene $t_n$. Para $n=0$, basta la mitad de $t_0-t_1=1/2$, es decir $1/4$, pues todos los otros positivos son a lo sumo $1/2$. Así los singletons positivos son abiertos relativos. $\{0\}$ no lo es: para cada $r>0$, arquimedianidad da $n$ con $0<t_n<r$. Todos los singletons son cerrados reales y por ello relativos, pero sólo la apertura de una vecindad determina aislamiento. La componente de cero es cerrada sin ser abierta relativa.

**Retorno visual.** Véase [C15-F07](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html#fig-anm-c15-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 15.39. Cerradura relativa desde la adherencia

[]{#MA-EX-ANM-01-015-039}

[]{#MA-SOL-ANM-01-015-039}

Si $z=x$, ya está en $C_x$. Si $x<z$, para todo $x<t<z$ la adherencia da $w\in C_x$ con $|w-z|<(z-t)/2$, así $w>t$. Como el segmento entre $x,w$ está en $D$, $t\in D$. Los extremos $x,z$ pertenecen a $D$, así $[x,z]\subseteq D$ y $z\in C_x$. Si $z<x$, para $z<t<x$ usamos radio $(t-z)/2$ alrededor de $z$, obteniendo $w<t$ en $C_x$; el segmento entre $w,x$ contiene $t$ y está en $D$. De nuevo $[z,x]\subseteq D$, luego $z\in C_x$. Todos los puntos adherentes que están en $D$ quedan en la clase, criterio de cierre relativo. En $D=(0,1)$ hay una componente única $(0,1)$, cerrada relativa a sí misma pero no cerrada real porque cero es adherente exterior.

## 15.40. Transportar o fusionar componentes

[]{#MA-EX-ANM-01-015-040}

[]{#MA-SOL-ANM-01-015-040}

Sea $f:D\to H$ homeomorfismo, $C$ componente de $x$. R4 hace conexo $f[C]$, que contiene $f(x)$ y queda en la componente $K$ de ese punto por maximalidad. La inversa continua hace conexo $f^{-1}[K]$, que contiene $x$ y por maximalidad está en $C$. Aplicando la biyección $f$ obtenemos $K\subseteq f[C]$, y las dos inclusiones dan igualdad. La constante $\{-1,1\}\to\{0\}$ es continua en el dominio relativo y fusiona sus dos componentes singleton en una sola. No existe inversa funcional, mucho menos continua, por lo que no puede transportarse $K$ hacia atrás para aplicar maximalidad. Una continua general sólo garantiza imagen conexa dentro de una componente.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 15](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe.html) · [Ejercicios](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-15-conexidad-por-que-un-intervalo-no-se-rompe-microcontroles.html)
