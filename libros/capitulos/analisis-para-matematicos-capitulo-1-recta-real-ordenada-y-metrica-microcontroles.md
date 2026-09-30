---
title: "Soluciones de microcontroles — Capítulo 1"
content-id: MA-BCH-0089
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-001-MICROCONTROLES
book-id: MA-BOK-0009
status: published
solution-status: complete
date-created: 2026-09-30
date-modified: 2026-09-30
areas: [analisis]
level: universitario
topics: [analisis-real, orden, topologia]
prerequisites: []
related: [MA-BOK-0009]
provenance:
  type: original
  sources:
    - "Manuscrito ANM C01; referencias de contraste en la portada del libro."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Capítulo 1](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica.md) · [Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Ejercicios](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-1-recta-real-ordenada-y-metrica-microcontroles.md)

# Soluciones de microcontroles — Capítulo 1

## §1.1. La misma recta, varias estructuras

[]{#MA-MSOL-ANM-01-001-001}

### 1. $x<y$

La estructura que actúa en primer plano es el **orden**. La relación $x<y$ afirma que $x$ precede a $y$ en el orden usual de $\mathbb R$; no especifica cuánto los separa ni exige realizar una operación algebraica entre ellos.

[]{#MA-MSOL-ANM-01-001-002}

### 2. «$y$ está entre $x$ y $z$»

La estructura principal vuelve a ser el **orden**. Decir que $y$ está entre $x$ y $z$ significa, sin elegir de antemano una orientación,

$$
\min\{x,z\}\le y\le\max\{x,z\}.
$$

Más adelante esta relación podrá reconocerse también mediante distancias, pero en este punto del capítulo su contenido primario es posicional: indica dónde está $y$ respecto de los extremos.

[]{#MA-MSOL-ANM-01-001-003}

### 3. «$x$ y $y$ están separados por la misma cantidad que $u$ y $v$»

Aquí la estructura relevante es la **métrica**, porque la afirmación compara separaciones. Cuando introduzcamos formalmente la distancia estándar de la recta, la frase se escribirá como

$$
d(x,y)=d(u,v),
$$

es decir,

$$
|x-y|=|u-v|.
$$

La orientación de cada par no importa: sólo se compara cuánto separa a sus puntos.

[]{#MA-MSOL-ANM-01-001-004}

### 4. $x+y=z$

La estructura que aparece en primer plano es la **algebraica**. La igualdad relaciona los tres números mediante la operación de suma. Por sí sola no afirma cuál es mayor ni menor, ni cuánto separa a un par de puntos en la recta.

[]{#MA-MSOL-ANM-01-001-005}

### 5. «Al reflejar una configuración, cambian izquierda y derecha pero no las separaciones»

En esta afirmación intervienen conjuntamente **orden** y **métrica**. La reflexión intercambia la orientación: lo que estaba a la izquierda pasa a la derecha y el orden se invierte. Al mismo tiempo, las separaciones permanecen iguales, de modo que la información métrica se conserva.

La propia reflexión puede describirse algebraicamente mediante $x\mapsto -x$, pero la afirmación que estamos leyendo compara dos efectos distintos: **cambio de orientación** y **conservación de distancias**. Ésa es precisamente la distinción estructural que §1.1 quería hacer visible.

## §1.2. Orden: izquierda, derecha y estar entre

[]{#MA-MSOL-ANM-01-001-006}

### 6. $x\in(-3,2)$

La notación de intervalo indica que $x$ queda estrictamente entre $-3$ y $2$. Como ambos extremos aparecen con paréntesis, ninguno pertenece al conjunto. Por tanto,

$$
\boxed{-3<x<2}.
$$

[]{#MA-MSOL-ANM-01-001-007}

### 7. $x\in[0,5)$

El corchete en $0$ incluye el extremo izquierdo y el paréntesis en $5$ excluye el derecho. La condición equivalente de orden es

$$
\boxed{0\le x<5}.
$$

[]{#MA-MSOL-ANM-01-001-008}

### 8. $-1<x\le4$

La desigualdad estricta en $-1$ excluye ese extremo; la desigualdad no estricta en $4$ lo incluye. En notación de intervalo,

$$
\boxed{x\in(-1,4]}.
$$

[]{#MA-MSOL-ANM-01-001-009}

### 9. $x>6$

La condición selecciona todos los reales situados estrictamente a la derecha de $6$. El punto $6$ queda excluido y no existe una frontera real superior. Por tanto,

$$
\boxed{x\in(6,\infty)}.
$$

El símbolo $\infty$ siempre aparece con paréntesis porque no es un número real que pueda pertenecer al intervalo.

[]{#MA-MSOL-ANM-01-001-010}

### 10. $x\le0$

La condición contiene todos los reales situados a la izquierda de $0$ y también al propio $0$. En consecuencia,

$$
\boxed{x\in(-\infty,0]}.
$$

De nuevo, $-\infty$ lleva paréntesis porque no es un punto de $\mathbb R$; el corchete aparece sólo en el extremo real $0$, que sí está incluido.

## §1.3. Valor absoluto: distancia al origen

[]{#MA-MSOL-ANM-01-001-011}

### 11. Si $|x|=6$, ¿qué sabemos sobre la posición de $x$?

La condición dice que $x$ está exactamente a $6$ unidades del origen. En la recta hay dos puntos con esa separación, uno a cada lado de $0$:

$$
\boxed{x=6\quad\text{o}\quad x=-6}.
$$

El valor absoluto determina la distancia al origen, pero no la orientación: saber $|x|=6$ no permite elegir entre derecha e izquierda.

[]{#MA-MSOL-ANM-01-001-012}

### 12. Si $|x|<2$, ¿en qué parte de la recta puede estar $x$?

La desigualdad pide los puntos cuya distancia al origen es menor que $2$. Por tanto, $x$ debe quedar estrictamente entre los dos puntos situados a distancia $2$ del origen:

$$
\boxed{-2<x<2}.
$$

Equivalentemente,

$$
\boxed{x\in(-2,2)}.
$$

Los extremos no pertenecen porque en $x=\pm2$ la distancia al origen vale exactamente $2$, no menos que $2$.

[]{#MA-MSOL-ANM-01-001-013}

### 13. ¿Qué diferencia de información hay entre $x-a$ y $|x-a|$?

La cantidad $x-a$ es un **desplazamiento orientado** desde $a$ hasta $x$: su signo indica de qué lado de $a$ queda $x$, y su magnitud indica cuánto se ha desplazado.

En cambio, $|x-a|$ conserva sólo el tamaño de ese desplazamiento. Es siempre no negativo y representa la **separación** entre $x$ y $a$.

Así, al pasar de $x-a$ a $|x-a|$ conservamos cuánto separa a los puntos, pero perdemos la información izquierda–derecha.

[]{#MA-MSOL-ANM-01-001-014}

### 14. Si $|x-a|=0$, ¿qué debe ocurrir?

Una distancia sólo puede ser cero cuando los dos puntos coinciden. Algebraicamente,

$$
|x-a|=0
\iff
x-a=0
\iff
\boxed{x=a}.
$$

Por tanto, el único punto situado a distancia cero del centro $a$ es el propio $a$.

## §1.4. Distancia entre dos puntos reales

[]{#MA-MSOL-ANM-01-001-015}

### 15. ¿Por qué $d(2,7)=d(7,2)$ aunque $2-7$ y $7-2$ tengan signos distintos?

Porque la distancia elimina la orientación mediante el valor absoluto:

$$
d(2,7)=|2-7|=|-5|=5,
$$

mientras que

$$
d(7,2)=|7-2|=|5|=5.
$$

Las restas tienen signos opuestos, pero el valor absoluto conserva sólo su magnitud. Por eso

$$
\boxed{d(2,7)=d(7,2)}.
$$

Ésta es la **simetría** de la distancia: cambiar el sentido del recorrido no cambia su longitud.

[]{#MA-MSOL-ANM-01-001-016}

### 16. Si $d(x,y)=0$, ¿qué podemos concluir y qué propiedad acabamos de usar?

Podemos concluir que los dos puntos coinciden:

$$
\boxed{x=y}.
$$

En efecto,

$$
d(x,y)=0\iff |x-y|=0\iff x-y=0\iff x=y.
$$

La propiedad utilizada es la **identidad de los puntos a distancia cero**: la distancia entre dos puntos vale cero si y sólo si son el mismo punto.

[]{#MA-MSOL-ANM-01-001-017}

### 17. ¿Qué afirma en palabras $d(x,z)\le d(x,y)+d(y,z)$?

Afirma que ir directamente de $x$ a $z$ nunca requiere más longitud que ir de $x$ a $z$ pasando primero por $y$.

La cantidad $d(x,z)$ mide la ruta directa, mientras que

$$
d(x,y)+d(y,z)
$$

suma las longitudes de los dos tramos de la ruta quebrada $x\to y\to z$. La **desigualdad triangular** dice, por tanto, que introducir un punto intermedio no puede acortar la distancia directa entre los extremos.

[]{#MA-MSOL-ANM-01-001-018}

### 18. ¿Qué controla la desigualdad $\bigl||x|-|y|\bigr|\le |x-y|$?

Controla cuánto pueden diferir las distancias de $x$ e $y$ al origen. La cantidad

$$
\bigl||x|-|y|\bigr|
$$

mide la diferencia entre esas dos distancias, y la desigualdad afirma que esa diferencia nunca supera la separación entre los propios puntos:

$$
\boxed{\bigl||x|-|y|\bigr|\le d(x,y)}.
$$

Así, si $x$ e $y$ están muy cerca, sus distancias al origen también deben ser cercanas. Éste es el contenido geométrico de la **desigualdad triangular inversa**.

## §1.5. La desigualdad triangular y la geometría de «estar entre»

[]{#MA-MSOL-ANM-01-001-019}

### 19. Si $x=-2$, $z=5$ y $y=1$, ¿esperamos igualdad o desigualdad estricta?

Esperamos **igualdad**, porque $1$ está entre $-2$ y $5$. En efecto,

$$
d(-2,5)=7,
$$

y

$$
d(-2,1)+d(1,5)=3+4=7.
$$

Por tanto,

$$
\boxed{d(-2,5)=d(-2,1)+d(1,5)}.
$$

La ruta que pasa por $y=1$ no contiene retroceso: recorre exactamente el mismo tramo que la ruta directa.

[]{#MA-MSOL-ANM-01-001-020}

### 20. Si $x=-2$, $z=5$ y $y=8$, ¿dónde aparece el recorrido extra?

Aquí $y=8$ queda a la derecha de $z=5$. Para pasar por $8$ desde $-2$ debemos sobrepasar el destino $5$ y después regresar desde $8$ hasta $5$.

La distancia directa es

$$
d(-2,5)=7,
$$

mientras que la ruta forzada mide

$$
d(-2,8)+d(8,5)=10+3=13.
$$

El exceso es

$$
13-7=6=2(8-5).
$$

Esos $6$ corresponden exactamente al tramo de longitud $3$ entre $5$ y $8$, recorrido una vez al sobrepasar $5$ y otra al regresar. Por eso la desigualdad es estricta.

[]{#MA-MSOL-ANM-01-001-021}

### 21. Si $d(x,z)=d(x,y)+d(y,z)$, ¿qué podemos afirmar sobre la posición de $y$ sin saber cuál de $x$ o $z$ está a la izquierda?

Podemos afirmar que $y$ está **entre** $x$ y $z$. La formulación que no presupone orientación es

$$
\boxed{\min\{x,z\}\le y\le\max\{x,z\}}.
$$

Ésta es precisamente la caracterización del caso de igualdad de la desigualdad triangular en la recta: la ruta $x\to y\to z$ no añade longitud si y sólo si $y$ pertenece al tramo cerrado determinado por los extremos.

[]{#MA-MSOL-ANM-01-001-022}

### 22. ¿Por qué los casos $y=x$ y $y=z$ deben formar parte de la caracterización?

Porque «estar entre» incluye los extremos del tramo cerrado. Si $y=x$, entonces

$$
d(x,y)=0,
\qquad
d(y,z)=d(x,z),
$$

y por tanto

$$
d(x,z)=d(x,y)+d(y,z).
$$

Si $y=z$, ocurre simétricamente:

$$
d(y,z)=0,
\qquad
d(x,y)=d(x,z).
$$

Así, en ambos extremos sigue habiendo igualdad. Excluir $y=x$ o $y=z$ haría falsa la equivalencia correcta

$$
\boxed{
d(x,z)=d(x,y)+d(y,z)
\iff
\min\{x,z\}\le y\le\max\{x,z\}
}.
$$

## §1.6. Bolas métricas: ventanas alrededor de un punto

[]{#MA-MSOL-ANM-01-001-023}

### 23. ¿Qué cambia en $B(a,r)$ si sustituimos $a$ por $a+3$ y mantenemos fijo $r$?

La bola original es

$$
B(a,r)=(a-r,a+r).
$$

Al cambiar el centro a $a+3$ obtenemos

$$
B(a+3,r)=((a+3)-r,(a+3)+r).
$$

Es decir,

$$
\boxed{B(a+3,r)=(a-r+3,a+r+3)}.
$$

Ambos extremos se desplazan $3$ unidades hacia la derecha. El radio no cambia, de modo que la anchura de la bola permanece igual: sólo se traslada toda la región.

[]{#MA-MSOL-ANM-01-001-024}

### 24. ¿Qué cambia si dejamos fijo $a$ y duplicamos $r$?

Con radio $r$ tenemos

$$
B(a,r)=(a-r,a+r).
$$

Al duplicarlo,

$$
\boxed{B(a,2r)=(a-2r,a+2r)}.
$$

El centro $a$ permanece fijo, pero cada frontera queda ahora al doble de distancia del centro. La ventana se ensancha simétricamente en ambas direcciones.

[]{#MA-MSOL-ANM-01-001-025}

### 25. ¿Por qué $a-r$ y $a+r$ quedan a la misma distancia del centro?

Calculamos sus separaciones respecto de $a$:

$$
d(a-r,a)=|(a-r)-a|=|-r|=r,
$$

y

$$
d(a+r,a)=|(a+r)-a|=|r|=r,
$$

porque $r>0$.

Por tanto,

$$
\boxed{d(a-r,a)=d(a+r,a)=r}.
$$

Los dos puntos son simétricos respecto del centro: uno está a la izquierda y el otro a la derecha, pero ambos tienen la misma separación.

[]{#MA-MSOL-ANM-01-001-026}

### 26. ¿Por qué esos dos puntos no pertenecen a $B(a,r)$?

La definición exige una desigualdad estricta:

$$
x\in B(a,r)
\iff
d(x,a)<r.
$$

Pero para los dos extremos acabamos de obtener

$$
d(a-r,a)=d(a+r,a)=r.
$$

Como $r<r$ es falso,

$$
\boxed{a-r\notin B(a,r)\qquad\text{y}\qquad a+r\notin B(a,r)}.
$$

Ésta es precisamente la razón por la que la bola abierta corresponde al intervalo abierto $(a-r,a+r)$.

[]{#MA-MSOL-ANM-01-001-027}

### 27. ¿Qué falla si intentamos usar $r=0$ como radio de una bola abierta?

Si escribiéramos $B(a,0)$ mediante la misma condición, obtendríamos

$$
B(a,0)=\{x\in\mathbb R:d(x,a)<0\}.
$$

Pero toda distancia es no negativa:

$$
d(x,a)\ge0.
$$

Por eso ningún punto puede satisfacer $d(x,a)<0$, ni siquiera el propio centro. Así,

$$
\boxed{B(a,0)=\varnothing}
$$

si se extiende formalmente la fórmula a $r=0$.

Lo que falla no es la lógica de la desigualdad, sino la interpretación que buscamos: un radio nulo no produce una región abierta de cercanía alrededor de $a$. Por eso en C01 exigimos siempre $r>0$.

## §1.7. Traducir entre orden, distancia y tolerancia

[]{#MA-MSOL-ANM-01-001-028}

### 28. Si $d(x,a)\le r$, ¿qué intervalo describe la condición?

Como

$$
d(x,a)=|x-a|,
$$

la desigualdad

$$
d(x,a)\le r
$$

significa que $x$ puede estar a lo sumo a distancia $r$ del centro $a$. Por tanto,

$$
a-r\le x\le a+r,
$$

y el conjunto correspondiente es

$$
\boxed{x\in[a-r,a+r]}.
$$

Los extremos se incluyen porque la comparación es $\le$.

[]{#MA-MSOL-ANM-01-001-029}

### 29. Si $x\in(a-r,a+r)$, ¿qué desigualdad de distancia satisface $x$?

La pertenencia al intervalo abierto equivale a

$$
a-r<x<a+r.
$$

Restando $a$,

$$
-r<x-a<r,
$$

lo que equivale a

$$
|x-a|<r.
$$

En lenguaje de distancia,

$$
\boxed{d(x,a)<r}.
$$

Así, el intervalo abierto alrededor de $a$ describe exactamente los puntos situados a menos de $r$ unidades del centro.

[]{#MA-MSOL-ANM-01-001-030}

### 30. Si $x\in(-\infty,a-r)\cup(a+r,\infty)$, ¿qué podemos afirmar sobre $|x-a|$?

La unión indica que $x$ queda fuera de las dos fronteras $a-r$ y $a+r$:

$$
x<a-r
\qquad\text{o}\qquad
x>a+r.
$$

En ambos casos, la separación respecto del centro es estrictamente mayor que $r$. Por tanto,

$$
\boxed{|x-a|>r}.
$$

Equivalentemente, $d(x,a)>r$: el punto está fuera de la región de radio $r$ alrededor de $a$.

[]{#MA-MSOL-ANM-01-001-031}

### 31. Si $|x-a|\ge r$, ¿qué ocurre con los puntos $a-r$ y $a+r$?

Ambos puntos satisfacen la condición, porque están exactamente a distancia $r$ del centro:

$$
|a-r-a|=|-r|=r,
$$

y

$$
|a+r-a|=|r|=r.
$$

Como la desigualdad permite la igualdad,

$$
\boxed{a-r\text{ y }a+r\text{ pertenecen al conjunto}}.
$$

Ésta es la diferencia precisa entre $|x-a|>r$ y $|x-a|\ge r$: la segunda incluye las dos fronteras.

[]{#MA-MSOL-ANM-01-001-032}

### 32. ¿Qué ocurre al aumentar $r$ en $d(x,a)<r$ y en $d(x,a)>r$?

Supongamos $0<r<s$.

Para la condición de cercanía,

$$
d(x,a)<r \Longrightarrow d(x,a)<s,
$$

por lo que

$$
\boxed{\{x:d(x,a)<r\}\subseteq\{x:d(x,a)<s\}}.
$$

Al aumentar el radio, la región interior **crece**: admitimos puntos más alejados del centro.

En cambio, para la condición exterior,

$$
d(x,a)>s \Longrightarrow d(x,a)>r,
$$

de modo que

$$
\boxed{\{x:d(x,a)>s\}\subseteq\{x:d(x,a)>r\}}.
$$

Al aumentar el umbral, la región exterior **se contrae**: para permanecer fuera hay que estar todavía más lejos de $a$.

Las dos familias responden de manera opuesta al mismo cambio de parámetro: aumentar $r$ ensancha la región «más cerca que $r$» y reduce la región «más lejos que $r$».

## §1.8. Qué ve el orden y qué ve la distancia

[]{#MA-MSOL-ANM-01-001-033}

### 33. Si trasladamos todos los puntos por $c$, ¿qué ocurre con el orden y con las distancias?

Ambas estructuras se preservan. Si $x<y$, entonces

$$
x+c<y+c,
$$

de modo que la orientación del orden no cambia. Además,

$$
d(x+c,y+c)=|(x+c)-(y+c)|=|x-y|=d(x,y).
$$

Por tanto, una traslación desplaza toda la configuración como un bloque rígido: **conserva el orden y conserva exactamente todas las distancias**.

[]{#MA-MSOL-ANM-01-001-034}

### 34. Si $\lambda=3$, ¿qué ocurre con una distancia de longitud $2$? ¿Y con el orden?

La ley de escala es

$$
d(\lambda x,\lambda y)=|\lambda|d(x,y).
$$

Si $\lambda=3$ y la distancia inicial vale $2$, la nueva distancia es

$$
3\cdot2=6.
$$

Como $3>0$, una desigualdad $x<y$ se transforma en

$$
3x<3y.
$$

Así, las distancias se **triplican** y el orden se **preserva**.

[]{#MA-MSOL-ANM-01-001-035}

### 35. Si $\lambda=-3$, ¿qué cambia respecto del caso anterior?

La magnitud del factor de escala sigue siendo $|-3|=3$, de modo que una distancia de longitud $2$ vuelve a convertirse en

$$
3\cdot2=6.
$$

Lo que cambia es la orientación. Si $x<y$, al multiplicar por un número negativo obtenemos

$$
-3x>-3y.
$$

Por tanto, **las distancias se triplican igual que antes, pero el orden se invierte**. La métrica registra $|\lambda|$; el orden, en cambio, distingue el signo de $\lambda$.

[]{#MA-MSOL-ANM-01-001-036}

### 36. ¿Por qué $x\mapsto -x$ preserva distancias y, sin embargo, invierte el orden?

Para la distancia,

$$
d(-x,-y)=|-x-(-y)|=|-(x-y)|=|x-y|=d(x,y).
$$

Por eso la reflexión es una isometría: no cambia ninguna separación.

Pero si $x<y$, al multiplicar por $-1$ la desigualdad cambia de sentido:

$$
-x>-y.
$$

La reflexión muestra así que **preservar distancias no equivale a preservar orientación**: la métrica permanece intacta mientras izquierda y derecha se intercambian.

[]{#MA-MSOL-ANM-01-001-037}

### 37. ¿Por qué $\lambda=0$ no debe clasificarse como una transformación que «invierte» el orden?

Porque invertir el orden exigiría que de $x<y$ resultara una desigualdad estricta opuesta entre las imágenes. Sin embargo, con $\lambda=0$ tenemos

$$
x\longmapsto0,
\qquad
y\longmapsto0.
$$

Los dos puntos distintos adquieren la misma imagen. No se cumple ni

$$
0<0
$$

ni

$$
0>0.
$$

Por tanto, $\lambda=0$ **no invierte el orden: lo colapsa**. También todas las distancias pasan a cero, pues

$$
d(0,0)=0.
$$

[]{#MA-MSOL-ANM-01-001-038}

### 38. ¿Qué información podemos perder aunque conozcamos todas las distancias de una configuración?

Podemos perder la **orientación izquierda–derecha**. Una configuración y su reflejo respecto del origen tienen exactamente las mismas distancias, porque

$$
d(-x,-y)=d(x,y)
$$

para cualquier par de puntos. Sin embargo, toda desigualdad estricta se invierte:

$$
x<y\iff -x>-y.
$$

Así, conocer todas las separaciones permite recuperar mucha información métrica —por ejemplo, qué puntos están entre otros mediante igualdades de distancias—, pero no permite distinguir una configuración de su imagen reflejada. **La métrica no determina por sí sola una orientación de la recta.**
