---
title: "Cinemática en varias dimensiones"
subtitle: "Física para matemáticos · Tomo I · Capítulo 8"
author: "A. Peña"
description: "Capítulo 8 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0348
source-id: FISPM-T1-C08
editorial-id: FPM-I-08
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0347"]
related: [MA-BOK-0005]
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
include-in-header:
  - ../../assets/includes/ma-math-font-ready.html
  - ../../assets/books/fispm/fispm-lightbox-focus.html
format:
  html:
    css: ../../assets/books/fispm/fispm-reader.css
    lightbox: true
number-sections: false
---

[Capítulo 7](fisica-para-matematicos-capitulo-7-cinematica-en-una-dimension.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 9](fisica-para-matematicos-capitulo-9-leyes-de-newton-y-estructura-de-la-dinamica.md)

[]{#fispm-c08-cinemuxe1tica-en-varias-dimensiones}

[]{#prerrequisitos-y-propósito}

## 8.0. Prerrequisitos y propósito {#fispm-c08-prerrequisitos-y-propuxf3sito .unnumbered}

Se utilizan la geometría afín euclídea del capítulo 4, las derivadas y la longitud de curvas del capítulo 5, el control de aproximaciones del capítulo 6 y las reconstrucciones y eventos del capítulo 7. La matemática requerida es M2--M3: vectores, producto escalar, trigonometría, derivadas e integrales de una variable. Las aceleraciones se prescriben como datos del modelo; su explicación mediante fuerzas pertenece al capítulo 9.

El capítulo estudia historias vectoriales, reconstrucción con datos iniciales, rapidez y dirección, proyectiles, coordenadas polares, movimiento circular, marcos móviles, composición y control de aproximaciones. La traslación y las cotas vectoriales se formulan en dos y tres dimensiones; el giro de ejes se desarrolla en el plano. Se conserva un reloj físico común y se explicitan dominios y restricciones de eventos.

[]{#historia-vectorial-y-componentes-en-un-marco-fijo}

[]{#fispm-t1-c08-s01}

[]{#fpm-i-08-s01}

## 8.1. Historia vectorial y componentes en un marco fijo {#fispm-c08-historia-vectorial-y-componentes-en-un-marco-fijo}

Una cámara registra el recorrido de un objeto sobre una mesa. Cada imagen proporciona dos coordenadas, pero ninguna de las dos series por separado describe el movimiento completo. Si la coordenada horizontal crece mientras la vertical disminuye, el objeto se desplaza en una dirección oblicua; si ambas regresan a sus valores iniciales, vuelve al punto de partida. Las coordenadas deben leerse juntas y en el mismo instante.

El capítulo 7 convirtió un movimiento sobre una recta fija en una función escalar. Aquí recuperamos la estructura del capítulo 5 y la usamos para resolver problemas con varias componentes. La diferencia no consiste en reemplazar cada número por una lista sin cambiar el razonamiento: una velocidad puede variar por su dirección aunque su norma permanezca constante.

[]{#representar-una-historia}

### 8.1.1. Representar una historia {#fispm-c08-representar-una-historia}

Sea $\mathcal E$ un espacio afín euclídeo de dimensión $d=2$ o $3$, con espacio vectorial de desplazamientos $V$. Fijamos un origen $O$ y una base ortonormal $B=(e_1,\ldots,e_d)$. El reloj es común a todas las componentes; su lectura $t$ pertenece a un intervalo no degenerado $I$. El marco $F=(O,B)$ permanece fijo durante esta primera parte.

[]{#fispm-t1-c08-d0001}

**Definición 8.1 --- Representación cartesiana de una historia.** Una historia continua $P:I\to\mathcal E$ se representa en $F$ por funciones continuas $x_i:I\to\mathbb R$ mediante $$P(t)=O+\mathbf r(t),\qquad \mathbf r(t)=\sum_{i=1}^d x_i(t)e_i.$$ El vector $\mathbf r(t)=\overrightarrow{OP(t)}$ es la posición relativa a $O$. Cuando las componentes son diferenciables, la velocidad es $\mathbf v=\mathbf r'$; cuando son dos veces diferenciables, la aceleración es $\mathbf a=\mathbf r''$.

La definición conserva el tipado del capítulo 4: $P(t)$ es un punto, $\mathbf r(t)$ es un vector y $x_i(t)$ es una componente escalar de longitud. El desplazamiento entre dos instantes es $\mathbf r(t_2)-\mathbf r(t_1)$, independiente de haber elegido otro origen fijo. La norma de ese desplazamiento no determina la distancia recorrida durante el intervalo.

[]{#fispm-t1-c08-p0001}

**Proposición 8.1 --- Derivación en una base fija.** Si todas las componentes $x_i$ son diferenciables en un instante interior $t$, entonces $$\mathbf v(t)=\sum_{i=1}^d x_i'(t)e_i.$$ Si son dos veces diferenciables allí, entonces $\mathbf a(t)=\sum_i x_i''(t)e_i$. En particular, la rapidez es $\|\mathbf v(t)\|=\sqrt{\sum_i(x_i'(t))^2}$.

**Demostración.** El cociente incremental de $\mathbf r$ es la suma finita $\sum_i((x_i(t+h)-x_i(t))/h)e_i$. Cada coeficiente converge a $x_i'(t)$ y cada $e_i$ es constante. La continuidad de las operaciones vectoriales permite pasar al límite en la suma. Una segunda derivación aplica el mismo argumento a las componentes $x_i'$. La fórmula de la norma resulta de la ortonormalidad, pues $e_i\cdot e_j$ es cero para $i\ne j$ y uno para $i=j$. $\square$

La hipótesis de base fija merece conservarse en la memoria. Si $e_i$ dependiera del tiempo, la regla del producto añadiría $x_i e_i'$; §§7--8 harán visible ese término en una situación concreta.

[]{#dos-gráficas-temporales-y-una-trayectoria}

### 8.1.2. Dos gráficas temporales y una trayectoria {#fispm-c08-dos-gruxe1ficas-temporales-y-una-trayectoria}

En un plano, las gráficas de $x(t)$ y $y(t)$ viven en planos tiempo--coordenada. La trayectoria, en cambio, es la imagen del mapa $t\mapsto(x(t),y(t))$ en el plano espacial. La pendiente $dy/dx$ de esa imagen, cuando se puede definir mediante $x'(t)\ne0$, es $y'(t)/x'(t)$: no es ninguna de las dos componentes de velocidad. Es un cociente adimensional que informa una dirección local.

[]{#fispm-t1-c08-mp0001}

**Principio metodológico 8.1 --- Conservar la sincronización.** Toda pareja o terna de componentes debe referirse al mismo reloj y al mismo instante. Eliminar el parámetro puede recuperar una relación espacial, pero no conserva automáticamente la rapidez, el sentido, las repeticiones ni el dominio temporal.

Para escribir ejemplos con dimensiones compatibles, elegimos $L>0$ y $T>0$, y ponemos $u=(t-t_0)/T$. Una ley $\mathbf r(t)=L\mathbf R(u)$, con $\mathbf R$ adimensional, produce $\mathbf v=(L/T)\mathbf R'$ y $\mathbf a=(L/T^2)\mathbf R''$. Las primas de $\mathbf R$ se refieren a $u$. En los ejercicios usaremos esta convención salvo indicación contraria.

[]{#ejercicios}

### 8.1.3. Ejercicios {#fispm-c08-ejercicios}

[]{#fispm-t1-c08-e0001}

[]{#fispm-t1-c08-e0008}

**Ejercicio 8.1.** En una base ortonormal fija $(e_1,e_2)$, sea $\mathbf R(u)=u e_1+(1-u^2)e_2$ para $-1\le u\le1$. Calcula velocidad, aceleración, rapidez y desplazamiento entre extremos. Encuentra la ecuación espacial de la trayectoria e indica su parte efectivamente recorrida.

**Solución.** proposición 8.1 da $\mathbf v=(L/T)(e_1-2u e_2)$, $\mathbf a=-(2L/T^2)e_2$ y rapidez $(L/T)\sqrt{1+4u^2}$. Los extremos son $-e_1$ y $e_1$ en coordenadas normalizadas; el desplazamiento físico es $2Le_1$. Si $X=u$ y $Y=1-u^2$, la imagen satisface $Y=1-X^2$ con $-1\le X\le1$. La ecuación sin la restricción de $X$ incluiría puntos que esta historia no visita. La rapidez nunca se anula, aunque la componente vertical sí lo hace en $u=0$.

[]{#fispm-t1-c08-e0002}

**Ejercicio 8.2.** Dos historias en $0\le u\le1$ tienen $\mathbf R_A(u)=u e_1+u^2 e_2$ y $\mathbf R_B(u)=u^2e_1+u^4e_2$. ¿Comparten trayectoria, velocidad y reposo instantáneo?

**Solución.** Ambas imágenes son el arco $Y=X^2$, $0\le X\le1$. En A, $X=u$; en B, $X=u^2$, que recorre el mismo intervalo. Sus velocidades normalizadas son $e_1+2u e_2$ y $2u e_1+4u^3e_2$, diferentes en general. En $u=0$, A tiene velocidad $e_1$ y B velocidad nula, entendiendo en el extremo la derivada unilateral o la extensión suave de la ley. Compartir imagen no equivale a compartir historia temporal. En cada instante hay que comparar las componentes simultáneas, no sólo su relación espacial.

La estructura se apoya en [capítulo 4](#fispm-c04-espacio-eucluxeddeo-vectores-y-marcos-de-referencia) y [capítulo 5](#fispm-c05-tiempo-movimiento-y-curvas), §§3--8. Shankar, cap. 2, §§2.2--2.5, sirve de contraste para la diferencia entre trayectoria espacial y gráficas temporales.[^1]

[]{#reconstrucción-desde-velocidad-y-aceleración}

[]{#fispm-t1-c08-s02}

[]{#fpm-i-08-s02}

## 8.2. Reconstrucción desde velocidad y aceleración {#fispm-c08-reconstrucciuxf3n-desde-velocidad-y-aceleraciuxf3n}

Supongamos que un instrumento proporciona las dos componentes de velocidad en función del tiempo. Podemos integrar cada registro, pero la integración deja dos constantes: una por coordenada. Juntas forman un vector inicial. Una velocidad prescribe desplazamientos entre instantes y deja abierta la posición de la historia en el espacio.

La reconstrucción no exige una teoría nueva de integración vectorial. En dimensión finita definimos la integral componente a componente en una base fija. Su resultado es independiente de la base: un cambio constante de coordenadas es una transformación lineal que conmuta con las sumas y con la integral de funciones continuas.

[]{#fispm-t1-c08-d0002}

**Definición 8.2 --- Integral vectorial de una función continua.** Para $\mathbf f:[a,b]\to V$ continua y $\mathbf f=\sum_i f_i e_i$, ponemos $$\int_a^b\mathbf f(s)\,ds =\sum_i\left(\int_a^b f_i(s)\,ds\right)e_i.$$ Usamos integrales orientadas: $\int_b^a\mathbf f=-\int_a^b\mathbf f$ y $\int_a^a\mathbf f=0$.

[]{#fispm-t1-c08-p0002}

**Proposición 8.2 --- Reconstrucción vectorial con datos iniciales.** Sean $I$ un intervalo, $t_0\in I$, $P_0\in\mathcal E$ y $\mathbf v_0\in V$. Si $\mathbf a:I\to V$ es continua, existe una única historia de clase $C^2$, con derivadas unilaterales en los extremos incluidos, que cumple $P(t_0)=P_0$, $\mathbf v(t_0)=\mathbf v_0$ y aceleración $\mathbf a$. Está dada por $$\mathbf v(t)=\mathbf v_0+\int_{t_0}^t\mathbf a(s)\,ds,$$ $$P(t)=P_0+(t-t_0)\mathbf v_0+ \int_{t_0}^t(t-s)\mathbf a(s)\,ds.$$ Si se prescribe sólo una velocidad continua, el dato $P_0$ determina de modo único la historia $P(t)=P_0+\int_{t_0}^t\mathbf v(s)\,ds$.

**Demostración.** Para cada $t\in I$, el segmento cerrado entre $t_0$ y $t$ está contenido en $I$; por continuidad, las integrales están definidas allí, aunque $I$ sea abierto o no acotado. El teorema fundamental del cálculo aplicado a cada componente demuestra que la primera fórmula tiene derivada $\mathbf a$ y valor $\mathbf v_0$ en $t_0$.

Para la segunda fórmula escribimos su integral como $t\int_{t_0}^t\mathbf a(s)\,ds-\int_{t_0}^t s\mathbf a(s)\,ds$. Al derivar, los términos $t\mathbf a(t)$ se cancelan y queda $\int_{t_0}^t\mathbf a(s)\,ds$. Por tanto, la derivada de la posición relativa es la velocidad anunciada; una derivada más da la aceleración. En $t=t_0$ se cumplen ambos datos iniciales.

Para la unicidad, la diferencia de dos velocidades con igual aceleración tiene derivada nula en todas sus componentes y valor cero en $t_0$; es el vector nulo en todo el intervalo. La diferencia de las posiciones relativas tiene entonces derivada cero y valor cero, y también se anula. El caso de velocidad prescrita repite este último paso. $\square$

La prueba muestra dos tareas diferentes: construir una historia que cumple las condiciones y descartar otras. Omitir el segundo paso dejaría sin demostrar la unicidad. También muestra por qué la continuidad de la aceleración basta: la segunda derivada se obtiene sin derivar $\mathbf a$.

[]{#el-caso-constante-y-el-plano-que-contiene-la-historia}

### 8.2.1. El caso constante y el plano que contiene la historia {#fispm-c08-el-caso-constante-y-el-plano-que-contiene-la-historia}

Si $\mathbf a(t)=\mathbf a_0$, la integral del núcleo $t-s$ da $$P(t)=P_0+\tau\mathbf v_0+\tfrac12\tau^2\mathbf a_0, \qquad \mathbf v(t)=\mathbf v_0+\tau\mathbf a_0, \qquad \tau=t-t_0.$$ La historia permanece en el subespacio afín $P_0+\operatorname{span}\{\mathbf v_0,\mathbf a_0\}$. En tres dimensiones, por tanto, una aceleración vectorial constante no produce una curva espacial arbitraria: la imagen está en un plano, una recta o un punto según el rango de los datos. Si los dos vectores son linealmente independientes, la imagen es una parábola en ese plano; si son dependientes, el movimiento es rectilíneo. La componente perpendicular a ambos nunca aparece en la fórmula.

[]{#fispm-t1-c08-mp0002}

**Principio metodológico 8.2 --- Contar datos vectoriales.** Aceleración conocida, posición inicial y velocidad inicial forman un problema de reconstrucción completo. Una coordenada inicial o una rapidez inicial sin dirección dejan información faltante; la cantidad de datos escalares debe interpretarse mediante los vectores que pretende determinar.

[]{#ejercicios-1}

### 8.2.2. Ejercicios {#fispm-c08-ejercicios-1}

[]{#fispm-t1-c08-e0003}

**Ejercicio 8.3.** En tiempo normalizado, $\mathbf R''(u)=2e_1+6u e_2$, con $\mathbf R(0)=e_2$ y $\mathbf R'(0)=e_1-e_2$. Reconstruye la historia y verifica los tres datos.

**Solución.** Integrar desde cero da $\mathbf R'(u)=(1+2u)e_1+(-1+3u^2)e_2$. Integrar otra vez y añadir la posición inicial produce $\mathbf R(u)=(u+u^2)e_1+(1-u+u^3)e_2$. En cero los valores son $e_2$ y $e_1-e_2$, y derivar dos veces recupera $2e_1+6u e_2$. Las magnitudes físicas son $L\mathbf R$, $(L/T)\mathbf R'$ y $(L/T^2)\mathbf R''$; las funciones del enunciado son adimensionales.

[]{#fispm-t1-c08-e0004}

**Ejercicio 8.4.** Se conocen $\mathbf a\equiv0$, $P(0)=P_0$ y la rapidez inicial $c>0$, pero no su dirección. Describe todas las historias compatibles en un plano y decide qué cambia si $c=0$.

**Solución.** Para cada vector unitario $n$, proposición 8.2 produce $P(t)=P_0+ctn$. Todos esos movimientos cumplen la misma rapidez inicial y aceleración nula. Recíprocamente, cualquier historia compatible tiene velocidad constante $\mathbf v_0$ de norma $c$, por lo que puede escribirse $cn$ con $n$ unitario. La familia está parametrizada por las direcciones del círculo unitario. Si $c=0$, el único vector de norma cero es el nulo y la historia queda determinada: $P(t)=P_0$. La insuficiencia de una rapidez como dato desaparece en este caso particular.

La reconstrucción extiende [capítulo 7](#fispm-c07-cinemuxe1tica-en-una-dimensiuxf3n), §§6--9. Kleppner--Kolenkow §1.7 controla la integración temporal; la existencia y unicidad se prueban aquí por componentes.[^2]

[]{#rapidez-dirección-y-geometría-del-movimiento}

[]{#fispm-t1-c08-s03}

[]{#fpm-i-08-s03}

## 8.3. Rapidez, dirección y geometría del movimiento {#fispm-c08-rapidez-direcciuxf3n-y-geometruxeda-del-movimiento}

En una curva cerrada, un objeto puede avanzar a rapidez constante y regresar al inicio. Su velocidad no permanece constante: apunta en direcciones distintas durante el recorrido. La idea escalar del capítulo 7, según la cual el cambio se reconoce en una componente firmada, necesita ahora separar la norma y la dirección del vector.

[]{#fispm-t1-c08-d0003}

**Definición 8.3 --- Rapidez y dirección instantánea.** En un instante con velocidad $\mathbf v(t)$, la rapidez es $q(t)=\|\mathbf v(t)\|$. Si $q(t)>0$, la dirección unitaria del movimiento es $\mathbf n(t)=\mathbf v(t)/q(t)$. En un instante de reposo, $\mathbf n$ no queda definida por esta fórmula.

La restricción $q>0$ evita atribuir una dirección al vector nulo. Puede existir una dirección límite al acercarse a un instante de reposo, pero requiere estudiar esa historia particular; no la incluye la definición.

[]{#fispm-t1-c08-p0003}

**Proposición 8.3 --- Cambio de rapidez y cambio de dirección.** Si $\mathbf r\in C^2(I,V)$ y $q>0$ en un intervalo abierto $J\subset I$, entonces $$q'=\frac{\mathbf v\cdot\mathbf a}{q},\qquad \mathbf a=q'\mathbf n+q\mathbf n',\qquad \mathbf n\cdot\mathbf n'=0.$$ La rapidez es constante en $J$ si y sólo si $\mathbf v\cdot\mathbf a=0$ en todo $J$.

**Demostración.** Como $q^2=\mathbf v\cdot\mathbf v$, la regla del producto da $2qq'=2\mathbf v\cdot\mathbf a$; la división está permitida por $q>0$. Derivar $\mathbf v=q\mathbf n$ produce la descomposición de $\mathbf a$. Por último, $\mathbf n\cdot\mathbf n=1$ implica $2\mathbf n\cdot\mathbf n'=0$. Si $q$ es constante, la primera identidad da producto escalar nulo. Si el producto escalar se anula en todo $J$, entonces $q'=0$ allí y el teorema del valor medio asegura que $q$ es constante en ese intervalo. $\square$

La equivalencia exige un intervalo, no un instante aislado. Que $\mathbf v\cdot\mathbf a$ se anule en $t_*$ sólo informa $q'(t_*)=0$ cuando $q(t_*)>0$. Tampoco $q$ constante exige $\mathbf a=0$: permite un cambio de dirección. La componente $q'\mathbf n$ es paralela a la velocidad; la componente $q\mathbf n'$ es perpendicular a ella.

Si deseamos medir cuánto gira la dirección por longitud recorrida, capítulo 5 permite usar $ds/dt=q$. Definimos aquí, sólo en un tramo regular, $\kappa=\|\mathbf n'\|/q$. Entonces la magnitud de la parte perpendicular de la aceleración es $q^2\kappa$. No necesitamos un marco de Frenet ni derivadas de varias variables: la fórmula surge de dividir el cambio temporal de una dirección por la rapidez. No se extiende mediante esta definición a $q=0$.

[]{#fispm-t1-c08-mp0003}

**Principio metodológico 8.3 --- Separar las preguntas sobre norma y vector.** Rapidez constante significa $\|\mathbf v\|$ constante; velocidad constante significa $\mathbf v$ constante. Sólo la segunda condición obliga a aceleración nula. La primera debe analizarse mediante el producto escalar o la evolución de la dirección.

[]{#longitud-y-desplazamiento}

### 8.3.1. Longitud y desplazamiento {#fispm-c08-longitud-y-desplazamiento}

Para $\mathbf r\in C^1([a,b],V)$, la distancia recorrida es $\ell=\int_a^b q(t)\,dt$, por la fórmula de longitud del capítulo 5. Como $\mathbf r(b)-\mathbf r(a)=\int_a^b\mathbf v(t)\,dt$, se tiene $\|\mathbf r(b)-\mathbf r(a)\|\le\ell$. Podemos ver esta desigualdad sin suponer una dirección fija: si el desplazamiento $D$ no es nulo, su vector unitario $m=D/\|D\|$ cumple $\|D\|=\int m\cdot\mathbf v\le\int\|\mathbf v\|$. Si $D=0$, la desigualdad es inmediata.

En el caso $D\ne0$, la igualdad exige que la función continua no negativa $q-m\cdot\mathbf v$ tenga integral cero, y por ello sea cero en cada instante. La igualdad en Cauchy--Schwarz obliga entonces a $\mathbf v(t)=\lambda(t)m$ con $\lambda(t)\ge0$. Así la igualdad entre longitud y módulo del desplazamiento caracteriza un avance por la dirección fija de los extremos sin retrocesos, permitiendo instantes de reposo. Si $D=0$, igualdad significa longitud cero y, por continuidad, reposo durante todo el intervalo.

[]{#ejercicios-2}

### 8.3.2. Ejercicios {#fispm-c08-ejercicios-2}

[]{#fispm-t1-c08-e0005}

**Ejercicio 8.5.** Sea $\mathbf R(u)=\cos u\,e_1+\sin u\,e_2$ en $0\le u\le2\pi$. Calcula rapidez, aceleración, longitud y desplazamiento, e interpreta proposición 8.3.

**Solución.** La velocidad es $(L/T)(-\sin u\,e_1+\cos u\,e_2)$, de norma $L/T$. La aceleración es $-(L/T^2)(\cos u\,e_1+\sin u\,e_2)$, no nula y perpendicular a la velocidad. La longitud es $(L/T)(2\pi T)=2\pi L$; el desplazamiento es cero. Proposición 8.3 permite aceleración no nula con rapidez constante porque toda la variación ocurre en la dirección. El círculo proporciona el contraejemplo a la afirmación de que rapidez constante implicaría movimiento rectilíneo uniforme.

[]{#fispm-t1-c08-e0006}

**Ejercicio 8.6.** En $-1\le u\le1$, sea $\mathbf R(u)=u e_1+u^2e_2$. Comprueba que la rapidez tiene derivada cero en $u=0$, y decide si es constante en algún intervalo abierto alrededor de ese instante.

**Solución.** La rapidez física es $q=(L/T)\sqrt{1+4u^2}$. Su derivada respecto del tiempo es $(4L/T^2)u/\sqrt{1+4u^2}$, que se anula en cero. Para cualquier $u\ne0$ la rapidez es mayor que $L/T$, así que no es constante en ningún intervalo abierto alrededor de cero. El producto $\mathbf v\cdot\mathbf a=(4L^2/T^3)u$ confirma la anulación sólo en ese instante. Una propiedad diferencial puntual no se convierte por sí sola en una propiedad de toda la historia.

La distinción está anticipada por Shankar §2.6 y Kleppner--Kolenkow §1.8. Aquí se expresa mediante proposición 8.3, que también permite tratar movimientos no circulares.[^3]

[]{#tiro-parabólico-como-modelo-cinemático}

[]{#fispm-t1-c08-s04}

[]{#fpm-i-08-s04}

## 8.4. Tiro parabólico como modelo cinemático {#fispm-c08-tiro-parabuxf3lico-como-modelo-cinemuxe1tico}

Una pelota sale de una plataforma y avanza mientras cambia su altura. La pregunta puede ser dónde tocará un suelo horizontal, cuánto tiempo estará en vuelo o qué velocidad debe tener para pasar por un punto. Antes de integrar debemos especificar qué descripción adoptamos: la fórmula parabólica no se obtiene de la palabra «pelota».

[]{#fig:I-08-R01}

![**Figura 8.1.** En el tiro ideal $r(t)=(t,2t-t^2/2)$, la altura máxima es $2$ en $t=2$. El retorno al nivel inicial ocurre en $t=4$, con alcance $4$. El segmento discontinuo mide altura y las coordenadas están normalizadas. Véase §[8.4](#fispm-c08-tiro-parabuxf3lico-como-modelo-cinemuxe1tico).](/assets/books/fispm/v04/I-08-R01.svg "fig:"){.fpm-v04-figure fig-alt="La aceleración permanece vertical" width="340px" fig-cap=""}

[]{#fig:I-08-N01}

![**Figura 8.2.** Sin resistencia, $X=u$ y $Y=2u-u^2/2$ entre lanzamiento y retorno al nivel inicial. En el ápice $u=2$, la velocidad es horizontal y la aceleración sigue apuntando hacia abajo. Las flechas son cinemáticas. Véase §[8.4](#fispm-c08-tiro-parabuxf3lico-como-modelo-cinemuxe1tico).](/assets/books/fispm/v04/I-08-N01.svg "fig:"){.fpm-v04-figure fig-alt="Proyectil y aceleración" width="368px" fig-cap=""}

[]{#fispm-t1-c08-d0004}

**Definición 8.4 --- Modelo local de proyectil.** En un marco cartesiano fijo del plano vertical, con $e_x$ horizontal y $e_y$ hacia arriba, el modelo prescribe $$\mathbf a(t)=-g e_y,\qquad g>0,$$ con condiciones iniciales $P(t_0)=O+x_0e_x+y_0e_y$ y $\mathbf v(t_0)=v_{0x}e_x+v_{0y}e_y$. Se aplica durante el intervalo de vuelo que se declare.

La aceleración es una hipótesis del modelo `[``MOD``]`; las condiciones iniciales son datos `[``IC``]`. Al usarlo para un proyectil próximo a la superficie terrestre se omiten, entre otros efectos, la resistencia del medio, la variación espacial de la aceleración y la curvatura del suelo. Un objeto pequeño para la pregunta se representa por un punto, sin describir su giro ni deformación. Esas idealizaciones permiten una predicción cinemática; no afirman que la aceleración de cualquier objeto lanzado sea exactamente la misma.

Un régimen razonable exige que la extensión espacial de la historia permita tratar como constante la aceleración, que la desviación por el medio sea pequeña para la tolerancia deseada y que el marco fijo sea adecuado durante el tiempo de vuelo. Estas condiciones no tienen un umbral numérico universal: el proyecto concreto debe aportar escalas y tolerancia. Una discrepancia horizontal sistemática o una curvatura incompatible con la parábola puede exigir revisar esas premisas. El capítulo 6 enseña a convertir diferencias de aceleración en cotas de posición; §13 retomará ese control vectorial.

[]{#fispm-t1-c08-p0004}

**Proposición 8.4 --- Historia del proyectil y eliminación del tiempo.** Para $\tau=t-t_0$, la historia de la definición 8.4 es $$x(t)=x_0+v_{0x}\tau,\qquad y(t)=y_0+v_{0y}\tau-\tfrac12 g\tau^2,$$ con $\mathbf v(t)=v_{0x}e_x+(v_{0y}-g\tau)e_y$. Si $v_{0x}\ne0$, su imagen satisface $$y=y_0+\frac{v_{0y}}{v_{0x}}(x-x_0) -\frac{g}{2v_{0x}^2}(x-x_0)^2,$$ restringida a los valores de $x$ correspondientes al intervalo temporal. Si $v_{0x}=0$, la imagen está en la recta $x=x_0$.

**Demostración.** proposición 8.2 aplicado a la aceleración constante da las dos componentes y la velocidad. Cuando $v_{0x}\ne0$, la primera igualdad tiene inversa $\tau=(x-x_0)/v_{0x}$. Sustituir en la segunda produce la ecuación espacial. La sustitución es reversible en los valores admitidos por el dominio. Si $v_{0x}=0$, la primera componente es constante y no se puede realizar esa división; la segunda describe directamente el movimiento vertical. $\square$

La ecuación parabólica es una consecuencia matemática exacta `[``MATH``]` de la definición 8.4. Su exactitud dentro del modelo no elimina los efectos físicos omitidos. También importa el caso degenerado: un lanzamiento vertical pertenece al modelo y no exige forzar una fórmula con denominador cero.

[]{#qué-significa-separar-las-componentes}

### 8.4.1. Qué significa separar las componentes {#fispm-c08-quuxe9-significa-separar-las-componentes}

La ecuación horizontal tiene aceleración cero y la vertical tiene aceleración $-g$. Esa separación es matemática porque el modelo prescribe componentes desacopladas. Ambas comparten el tiempo; cuando ocurre un evento vertical, la posición horizontal debe evaluarse en ese mismo instante. La frase «el movimiento horizontal no influye en el vertical» está limitada a estas premisas. Una aceleración que dependiera de la velocidad completa o de la posición podría destruir esa separación.

[]{#fispm-t1-c08-mp0004}

**Principio metodológico 8.4 --- Declarar la aceleración antes de integrar.** En cinemática, una aceleración prescrita es un dato o una hipótesis. Integrar demuestra qué historia resulta de esa premisa; la explicación dinámica y la comprobación empírica son obligaciones diferentes.

[]{#ejercicios-3}

### 8.4.2. Ejercicios {#fispm-c08-ejercicios-3}

[]{#fispm-t1-c08-e0007}

**Ejercicio 8.7.** Toma $g=2L/T^2$, $x_0=0$, $y_0=2L$, $v_{0x}=3L/T$ y $v_{0y}=L/T$. Encuentra las componentes normalizadas y la relación espacial. Mantén inicialmente el dominio $u\ge0$ sin imponer todavía el suelo.

**Solución.** proposición 8.4 da $X(u)=3u$ y $Y(u)=2+u-u^2$. La velocidad es $(L/T)(3e_x+(1-2u)e_y)$ y la aceleración $-(2L/T^2)e_y$. Como $u=X/3$, la relación espacial es $Y=2+X/3-X^2/9$ con $X\ge0$. La condición $u\ge0$ ya excluye la rama temporal anterior al lanzamiento; el evento de contacto reducirá aún más el intervalo. La ecuación sin dominio no describe por sí sola el vuelo físico.

**Ejercicio 8.8.** Bajo definición 8.4, dos objetos parten simultáneamente de la misma altura y con la misma componente vertical inicial, pero diferentes componentes horizontales. Explica qué eventos de altura comparten. ¿Basta ese resultado para afirmar que chocarán entre sí?

**Solución.** Ambos tienen exactamente la misma función $y(\tau)$, de modo que los conjuntos de tiempos en que alcanzan cualquier altura prescrita coinciden dentro del dominio común. Sus funciones horizontales son $x_{A0}+v_{Ax}\tau$ y $x_{B0}+v_{Bx}\tau$, y un encuentro exige además su igualdad en uno de esos instantes. Si parten también de la misma abscisa pero con $v_{Ax}\ne v_{Bx}$, la igualdad horizontal sólo ocurre en $\tau=0$. Coincidencia de alturas no es coincidencia de puntos; el encuentro es una condición vectorial simultánea.

Shankar, cap. 2, §2.7, pp. 32--35, controla la separación de componentes y el lanzamiento a igual altura. La exposición usa datos propios y mantiene explícitos los casos degenerados.[^4]

[]{#eventos-altura-y-alcance}

[]{#fispm-t1-c08-s05}

[]{#fpm-i-08-s05}

## 8.5. Eventos, altura y alcance {#fispm-c08-eventos-altura-y-alcance}

La prolongación algebraica de una parábola sigue existiendo después de tocar el suelo. El modelo de vuelo termina allí: la colisión modifica la historia y requiere otro tratamiento. Por eso encontrar una raíz no basta; debemos decidir qué raíz corresponde al evento y qué intervalo queda físicamente admitido.

Tomamos $t_0=0$, suelo $y=0$, altura inicial $h\ge0$ y componentes iniciales $p=v_{0x}$, $w=v_{0y}$. La ley vertical es $y(\tau)=h+w\tau-g\tau^2/2$. Para un lanzamiento desde el suelo que produzca un intervalo de vuelo positivo exigimos $w>0$; para $h>0$, cualquier $w\in\mathbb R$ deja una primera raíz futura.

[]{#fispm-t1-c08-d0005}

**Definición 8.5 --- Intervalo de vuelo hasta el suelo.** Bajo las condiciones anteriores, el tiempo de llegada es la primera raíz estrictamente positiva $\tau_f$ de $y(\tau)=0$. El intervalo de vuelo es $[0,\tau_f]$ y cumple $y(\tau)>0$ para $0<\tau<\tau_f$. El desplazamiento horizontal al llegar es $\Delta x_f=p\tau_f$; si se fija $p>0$, lo llamaremos alcance $R$.

La condición de raíz positiva evita contar el instante de salida como llegada en un lanzamiento desde el suelo. Si $h=0$ y $w\le0$, esta convención no proporciona un vuelo positivo sobre el suelo; el modelo necesitaría otro dominio o una descripción de contacto. Si $p<0$, $\Delta x_f$ es negativo respecto de la orientación elegida, y su módulo puede emplearse como distancia horizontal entre extremos. No cambiamos de significado sin avisarlo.

[]{#fispm-t1-c08-p0005}

**Proposición 8.5 --- Tiempo de llegada y altura máxima.** Si $h>0$, o si $h=0$ y $w>0$, entonces $$\tau_f=\frac{w+\sqrt{w^2+2gh}}{g}.$$ La altura máxima en $[0,\tau_f]$ es $h+w^2/(2g)$ si $w>0$, alcanzada en $\tau=w/g$; si $w\le0$ y $h>0$, es $h$, alcanzada en la salida. Cuando $h=0$ y $w>0$, $\tau_f=2w/g$.

**Demostración.** Resolver la ecuación cuadrática da las raíces $(w\pm\sqrt{w^2+2gh})/g$. Para $h>0$, la raíz con signo menos es negativa y la otra positiva, pues la raíz cuadrada es mayor que $|w|$. Para $h=0$, $w>0$, las raíces son cero y $2w/g$. El coeficiente cuadrático es negativo, de modo que $y$ es positivo entre las raíces; en ambos casos lo es durante el interior del vuelo definido.

La derivada vertical es $y'=w-g\tau$. Si $w>0$, se anula en $w/g$, que está dentro del vuelo porque $\tau_f>w/g$, y cambia de positiva a negativa. Sustituir ese instante en $y$ da $h+w^2/(2g)$. Si $w\le0$, la función disminuye para todo $\tau>0$, por lo que el máximo del intervalo cerrado es el valor inicial. $\square$

El vértice de la parábola prolongada podría estar en tiempo negativo cuando $w<0$. Incluirlo como «altura máxima del vuelo» sería optimizar sobre el dominio equivocado. El evento y el dominio forman parte de la pregunta.

[]{#alcance-a-igual-altura}

### 8.5.1. Alcance a igual altura {#fispm-c08-alcance-a-igual-altura}

[]{#fispm-t1-c08-p0006}

**Proposición 8.6 --- Alcance con rapidez inicial fija a igual altura.** Para $h=0$, rapidez inicial $c>0$ y ángulo $0<\alpha<\pi/2$, con $p=c\cos\alpha$ y $w=c\sin\alpha$, el alcance es $$R(\alpha)=\frac{c^2}{g}\sin(2\alpha).$$ Su máximo es $c^2/g$, alcanzado únicamente en $\alpha=\pi/4$ dentro de ese intervalo.

**Demostración.** proposición 8.5 da $\tau_f=2c\sin\alpha/g$. Multiplicar por $p=c\cos\alpha$ y usar $2\sin\alpha\cos\alpha=\sin(2\alpha)$ produce la fórmula. Para $2\alpha\in(0,\pi)$, el seno no supera uno y es uno sólo en $2\alpha=\pi/2$. La condición equivalente es $\alpha=\pi/4$. $\square$

El ángulo de cuarenta y cinco grados depende de comparar alcances con la misma rapidez, salida y llegada a igual altura, y aceleración de la definición 8.4. Si cambia la altura final, la duración deja de ser $2w/g$; si cambia la rapidez con el ángulo, la función que se optimiza cambia. No hay un ángulo universal desligado de esas condiciones.

[]{#fispm-t1-c08-mp0005}

**Principio metodológico 8.5 --- Resolver eventos dentro de la historia admitida.** Una ecuación de evento determina candidatos. Se conserva cada candidato sólo después de comprobar tiempo, posición y régimen. Las extremizaciones también deben hacerse en ese dominio, incluidos sus extremos.

[]{#ejercicios-4}

### 8.5.2. Ejercicios {#fispm-c08-ejercicios-4}

[]{#fispm-t1-c08-e0009}

**Ejercicio 8.9.** Para ejercicio 8.7, termina el vuelo en el suelo. Encuentra tiempo de llegada, posición, altura máxima y velocidad de llegada. Comprueba qué raíz se descarta.

**Solución.** $2+u-u^2=0$ tiene raíces $u=-1$ y $u=2$. La primera pertenece al pasado de la ley prolongada y no al vuelo desde $u=0$; la segunda da $\tau_f=2T$ y $P_f=O+6Le_x$. La altura máxima ocurre en $u=1/2$ y vale $9L/4$. La velocidad final es $(L/T)(3e_x-3e_y)$, de rapidez $3\sqrt2L/T$. En el interior $0<u<2$, $Y=(2-u)(u+1)>0$, lo que confirma la admisibilidad. El vuelo termina en $u=2$, aunque la expresión polinómica permita seguir calculando.

[]{#fispm-t1-c08-e0010}

**Ejercicio 8.10.** Se lanza desde $h>0$ con rapidez fija $c>0$. Demuestra que $\alpha=\pi/4$ no maximiza el alcance entre ángulos ascendentes $0<\alpha<\pi/2$. No necesitas encontrar el máximo.

**Solución.** proposición 8.5 da $R(\alpha)=(c/g)\cos\alpha\,[c\sin\alpha+S(\alpha)]$, donde $S(\alpha)=\sqrt{c^2\sin^2\alpha+2gh}$. La función es diferenciable en el intervalo y $S'=c^2\sin\alpha\cos\alpha/S$. Para $b=c/\sqrt2$ y $S_*=\sqrt{b^2+2gh}$, la derivada en $\pi/4$ es $$R'(\pi/4)=\frac{c}{g\sqrt2}\left(-S_*+\frac{b^2}{S_*}\right) =-\frac{2ch}{\sqrt2S_*}<0.$$ En un entorno de ese ángulo la función disminuye, así que un ángulo ligeramente menor da mayor alcance. El caso $h=0$ anula esta derivada y recupera proposición 8.6. La fórmula familiar fallaba aquí porque la altura de salida modifica el tiempo de vuelo.

[]{#diseñar-un-lanzamiento-y-reconocer-información-faltante}

[]{#fispm-t1-c08-s06}

[]{#fpm-i-08-s06}

## 8.6. Diseñar un lanzamiento y reconocer información faltante {#fispm-c08-diseuxf1ar-un-lanzamiento-y-reconocer-informaciuxf3n-faltante}

Hasta ahora fijamos la velocidad inicial y calculamos lo que ocurriría. El problema inverso pide qué velocidad permitiría un evento deseado. La inversión tiene que conservar los datos que se conocen: alcanzar un punto no determina por sí solo la duración ni la rapidez del lanzamiento.

Tomamos la salida en $(0,0)$ y el objetivo en $(d,H)$, con $d>0$. Si el tiempo de llegada $\tau>0$ se prescribe, proposición 8.4 determina inmediatamente $$p=\frac d\tau,\qquad w=\frac H\tau+\frac{g\tau}{2}.$$ Esta pareja es única para ese tiempo. Si no se prescribe $\tau$, las parejas forman una familia de un parámetro. La fórmula responde al evento de paso por el objetivo; si hay suelo, obstáculos u otro final de vuelo, hay que verificar adicionalmente el segmento temporal anterior. Un objetivo alcanzado por una prolongación posterior a una colisión no constituye un lanzamiento admisible.

[]{#fispm-t1-c08-p0007}

**Proposición 8.7 --- Rapidez mínima para pasar por un objetivo.** Bajo definición 8.4, sin restricciones adicionales durante el recorrido y con $\tau>0$ libre, la menor rapidez inicial capaz de pasar por $(d,H)$ satisface $$c_{\min}^2=g\left(H+\sqrt{d^2+H^2}\right).$$ Se alcanza en un único tiempo, determinado por $\tau^2=2\sqrt{d^2+H^2}/g$, y la pareja $(p,w)$ anterior determina una única velocidad para ese tiempo.

**Demostración.** El cuadrado de la rapidez requerida es $$c^2(\tau)=p^2+w^2 =\frac{d^2+H^2}{\tau^2}+gH+\frac{g^2\tau^2}{4}.$$ Sea $A=d^2+H^2>0$ y $z=\tau^2>0$. Los términos que dependen de $z$ cumplen $$\frac A z+\frac{g^2z}{4}-g\sqrt A =\left(\frac{\sqrt A}{\sqrt z}-\frac{g\sqrt z}{2}\right)^2\ge0.$$ La igualdad ocurre si y sólo si $z=2\sqrt A/g$. Por tanto, el mínimo de $c^2$ es $gH+g\sqrt A$, positivo porque $d>0$ implica $\sqrt A>|H|$. La rapidez tiene el mismo minimizador, pues la raíz cuadrada es estrictamente creciente en números positivos. La unicidad del tiempo positivo y de las componentes ya calculadas concluye la prueba. $\square$

La prueba transforma una búsqueda de velocidades en una búsqueda de tiempos. No necesita diferenciar una expresión trigonométrica ni suponer de antemano que el mejor lanzamiento tenga cierto ángulo. Tampoco convierte todos los objetivos en físicamente accesibles: la cláusula sin restricciones adicionales es parte sustantiva del enunciado.

[]{#rapidez-fijada-y-dos-posibilidades}

### 8.6.1. Rapidez fijada y dos posibilidades {#fispm-c08-rapidez-fijada-y-dos-posibilidades}

Si la rapidez disponible es $c$, la igualdad anterior produce una ecuación para $z=\tau^2$: $$\frac{g^2}{4}z^2+(gH-c^2)z+(d^2+H^2)=0.$$ Para $c=c_{\min}$ hay una raíz positiva doble y un lanzamiento. Para $c>c_{\min}$ hay dos raíces positivas distintas: el discriminante es positivo porque $c^2-gH>g\sqrt{d^2+H^2}$; la suma y el producto de las raíces son positivos. Sus raíces cuadradas proporcionan dos tiempos y dos velocidades iniciales. Para $c<c_{\min}$ no hay tiempo admisible, por la proposición 8.7. Esta clasificación incluye objetivos altos y bajos, sin dividir por una componente vertical que pudiera anularse.

[]{#fispm-t1-c08-mp0006}

**Principio metodológico 8.6 --- Declarar el dato libre en una inversión.** Un punto objetivo, un tiempo objetivo y una rapidez inicial son restricciones diferentes. Antes de resolver, se debe identificar cuál se fija, cuál se busca y cuáles quedan libres. La multiplicidad de soluciones puede ser una propiedad del problema y no un error algebraico.

[]{#ejercicios-5}

### 8.6.2. Ejercicios {#fispm-c08-ejercicios-5}

[]{#fispm-t1-c08-e0011}

**Ejercicio 8.11.** Un objetivo está en $(d,0)$ con $d>0$. Encuentra la rapidez mínima y la velocidad inicial que la alcanza. Relaciona el resultado con la proposición 8.6.

**Solución.** proposición 8.7 da $c_{\min}=\sqrt{gd}$ y $\tau_* =\sqrt{2d/g}$. Las componentes son $p=d/\tau_* =\sqrt{gd/2}$ y $w=g\tau_*/2=\sqrt{gd/2}$. La velocidad apunta a $\pi/4$ y tiene norma $\sqrt{gd}$. Proposición 8.6 afirma que a rapidez $c$ el mayor alcance a igual altura es $c^2/g$; exigir que ese alcance sea $d$ produce el mismo umbral. Las dos formulaciones invierten qué magnitud se fija y cuál se optimiza.

[]{#fispm-t1-c08-e0012}

**Ejercicio 8.12.** Usa unidades normalizadas con $g=2L/T^2$ y objetivo $(L,0)$. Para rapidez $c=2L/T$, encuentra ambos tiempos de llegada y sus velocidades iniciales. Verifica el paso por el objetivo y el dominio sobre el suelo.

**Solución.** Si $u=\tau/T$, las componentes iniciales normalizadas son $P=1/u$ y $W=u$. La condición de rapidez es $u^{-2}+u^2=4$. Con $z=u^2$ obtenemos $z^2-4z+1=0$, por lo que $z_\pm=2\pm\sqrt3>0$ y $u_\pm=\sqrt{2\pm\sqrt3}$. Las velocidades son $(L/T)(u_\pm^{-1}e_x+u_\pm e_y)$; ambas tienen norma $2L/T$.

Para cada elección, $X(s)=s/u_\pm$ y $Y(s)=u_\pm s-s^2$ en tiempo normalizado $s$. En $s=u_\pm$ se cumple $(X,Y)=(1,0)$ y en $0<s<u_\pm$ se tiene $Y=s(u_\pm-s)>0$. Ambas historias alcanzan el objetivo en su primera llegada positiva al suelo. El lanzamiento de mayor tiempo tiene mayor componente vertical y menor componente horizontal. La ecuación inversa conserva esas dos posibilidades.

[]{#coordenadas-polares-y-direcciones-variables}

[]{#fispm-t1-c08-s07}

[]{#fpm-i-08-s07}

## 8.7. Coordenadas polares y direcciones variables {#fispm-c08-coordenadas-polares-y-direcciones-variables}

Un movimiento próximo a un centro fijo puede resultar más sencillo si registramos distancia al centro y ángulo. Para una circunferencia centrada en ese punto, la distancia no cambia y el ángulo contiene toda la evolución. Sin embargo, que una coordenada sea constante no significa que el vector de posición lo sea: su dirección puede variar.

[]{#fig:I-08-R02}

![**Figura 8.3.** La base ortonormal polar gira con el ángulo: $\dot e_r=\dot\theta e_\theta$ y $\dot e_\theta=-\dot\theta e_r$. Las flechas muestran sus direcciones; su longitud es esquemática. Véase §[8.7](#fispm-c08-coordenadas-polares-y-direcciones-variables).](/assets/books/fispm/v04/I-08-R02.svg "fig:"){.fpm-v04-figure fig-alt="La base polar también se deriva" width="340px" fig-cap=""}

[]{#fig:I-08-N02}

![**Figura 8.4.** En el punto de ángulo $\theta$, $e_r$ es radial y $e_\theta$ apunta hacia el incremento de $\theta$. Las dos direcciones giran con el punto; sus derivadas aportan términos a la aceleración. Véase §[8.7](#fispm-c08-coordenadas-polares-y-direcciones-variables).](/assets/books/fispm/v04/I-08-N02.svg "fig:"){.fpm-v04-figure fig-alt="Base polar local" width="340px" fig-cap=""}

Fijamos un plano orientado con origen $O$ y base ortonormal $(e_x,e_y)$. Para un punto distinto de $O$, la distancia $\rho>0$ es única, mientras que el ángulo representa una dirección y se determina módulo $2\pi$.

[]{#fispm-t1-c08-d0006}

**Definición 8.6 --- Representación polar de una historia que evita el origen.** Una representación polar diferenciable de $P$ en un intervalo $J$ consta de funciones diferenciables $\rho:J\to(0,\infty)$ y $\theta:J\to\mathbb R$ tales que $$\mathbf r(t)=\rho(t)e_r(t),\qquad e_r(t)=\cos\theta(t)e_x+\sin\theta(t)e_y.$$ La dirección angular positiva se representa por $$e_\theta(t)=-\sin\theta(t)e_x+\cos\theta(t)e_y.$$ La función $\theta$ es una elección continua del ángulo a lo largo del tramo, no una coordenada principal obligada a permanecer entre dos valores fijos. La regularidad de estas funciones se exige explícitamente cuando se derivan.

El cambio de coordenadas es $x=\rho\cos\theta$, $y=\rho\sin\theta$. La distancia se recupera por $\rho=\sqrt{x^2+y^2}$; el ángulo requiere conservar el cuadrante. La receta $\theta=\arctan(y/x)$ falla si $x=0$ y confunde direcciones opuestas cuando sólo se usa el cociente. Se puede elegir una rama del ángulo en un entorno espacial que evite un corte; al seguir una historia que cruza ese corte hay que continuar el ángulo de manera coherente. No utilizaremos sin prueba un teorema global de levantamiento: nuestros cálculos se hacen en tramos con una representación polar regular declarada, o en leyes polares dadas desde el comienzo.

[]{#una-base-ligada-a-la-posición}

### 8.7.1. Una base ligada a la posición {#fispm-c08-una-base-ligada-a-la-posiciuxf3n}

En cada instante, $(e_r,e_\theta)$ es una base ortonormal del mismo plano. Directamente, $e_r\cdot e_r=e_\theta\cdot e_\theta=1$ y $e_r\cdot e_\theta=0$, por las identidades trigonométricas. Las componentes de un vector $\mathbf b$ en esa base son $b_r=\mathbf b\cdot e_r$ y $b_\theta=\mathbf b\cdot e_\theta$. Para comparar componentes tomadas en instantes diferentes, debemos recordar que sus direcciones pueden ser diferentes.

[]{#fispm-t1-c08-p0008}

**Proposición 8.8 --- Derivadas de las direcciones polares.** En una representación definición 8.6, si $\theta$ es diferenciable, entonces $$e_r'=\theta'e_\theta, \qquad e_\theta'=-\theta'e_r.$$ Dos elecciones continuas del ángulo para la misma dirección, en el mismo intervalo conectado, difieren en una constante múltiplo entero de $2\pi$; por tanto, si son diferenciables tienen la misma derivada.

**Demostración.** Derivar las componentes de $e_r$ en la base fija da $\theta'(-\sin\theta e_x+\cos\theta e_y)=\theta'e_\theta$. Derivar las de $e_\theta$ da $-\theta'(\cos\theta e_x+\sin\theta e_y)=-\theta'e_r$.

Si $\theta_1$ y $\theta_2$ representan la misma dirección, sus senos y cosenos coinciden. Por la periodicidad de la parametrización del círculo, $(\theta_1-\theta_2)/(2\pi)$ toma valores enteros. Es una función continua en un intervalo: si tomara dos enteros distintos, el teorema del valor intermedio la obligaría a tomar un valor no entero entre ellos. Es, por ello, constante. Su derivada es cero cuando ambas elecciones son diferenciables. $\square$

La primera identidad expresa que el cambio de un vector unitario es perpendicular al propio vector. Proposición 8.3 ya había mostrado esa estructura de forma general. La segunda identidad fija el signo de la rotación: cuando $\theta$ crece, $e_\theta$ gira hacia $-e_r$.

[]{#fispm-t1-c08-mp0007}

**Principio metodológico 8.7 --- Derivar coeficientes y direcciones.** Una base ortonormal puede cambiar con el tiempo. Su ortonormalidad permite calcular normas y proyecciones en cada instante, pero no autoriza tratar sus vectores como constantes al derivar.

[]{#el-origen-y-el-corte-angular}

### 8.7.2. El origen y el corte angular {#fispm-c08-el-origen-y-el-corte-angular}

En $\rho=0$ cualquier ángulo produce el mismo punto. La dirección radial deja de estar determinada por la posición; no es una singularidad necesaria del movimiento físico. Por ejemplo, la ley cartesiana $\mathbf r(t)=ct e_x$, con $c>0$, atraviesa el origen suavemente. Su distancia es $c|t|$, no diferenciable en cero, y la dirección radial cambia de $-e_x$ a $e_x$. La descripción cartesiana sigue siendo regular mientras la descripción polar ligada a la posición pierde regularidad.

Un salto de $2\pi$ en una lectura principal del ángulo tampoco prueba un salto del punto. En una circunferencia, $\theta(t)$ puede crecer continuamente a través de $\pi$, aunque un instrumento que devuelve ángulos en $(-\pi,\pi]$ cambie de rama. Se debe distinguir el registro angular, su continuación temporal y la posición que representan.

[]{#ejercicios-6}

### 8.7.3. Ejercicios {#fispm-c08-ejercicios-6}

[]{#fispm-t1-c08-e0013}

**Ejercicio 8.13.** En tiempo normalizado, $\rho=L$ y $\theta(u)=3\pi/4+u$ para $0\le u\le\pi/2$. Describe el registro principal en $(-\pi,\pi]$ y decide si la posición o la dirección $e_r$ tienen un salto.

**Solución.** Hasta $u=\pi/4$ el ángulo principal es $3\pi/4+u$; en el cruce toma $\pi$ y después puede escribirse $3\pi/4+u-2\pi$. El registro principal salta de valores próximos a $\pi$ a valores próximos a $-\pi$. Sin embargo, seno y coseno son continuos y periódicos: $\mathbf r=L(\cos\theta e_x+\sin\theta e_y)$ y $e_r$ no tienen salto. Para derivar se conserva la función continua $3\pi/4+u$, cuya derivada temporal es $1/T$. Derivar una lectura con salto como si fuera la dirección física confundiría el corte con el movimiento.

[]{#fispm-t1-c08-e0014}

**Ejercicio 8.14.** Explica por qué los puntos con coordenadas $(x,y)=(-L,L)$ y $(L,-L)$ tienen el mismo cociente $y/x$ pero distintas direcciones polares. Encuentra $\rho$ y una elección de $\theta$ para cada uno.

**Solución.** Ambos cocientes son $-1$ y ambas distancias son $\sqrt2L$. Para el primero podemos elegir $\theta=3\pi/4$ y para el segundo $\theta=-\pi/4$. Sus direcciones son opuestas y difieren en $\pi$, no en un múltiplo entero de $2\pi$. Usar sólo $\arctan(-1)=-\pi/4$ representaría correctamente el segundo punto y colocaría el primero en el cuadrante equivocado. Las igualdades $\cos\theta=x/\rho$ y $\sin\theta=y/\rho$ controlan simultáneamente el cuadrante.

Kleppner--Kolenkow §1.9, pp. 27--33, controla el cambio a direcciones polares. Aquí se añade explícitamente la separación entre el ángulo continuado, el corte de una rama y el origen.[^5]

[]{#velocidad-y-aceleración-en-coordenadas-polares}

[]{#fispm-t1-c08-s08}

[]{#fpm-i-08-s08}

## 8.8. Velocidad y aceleración en coordenadas polares {#fispm-c08-velocidad-y-aceleraciuxf3n-en-coordenadas-polares}

En una historia polar, $\rho'$ informa cuánto cambia la distancia al origen. No mide toda la rapidez: un objeto puede mantener esa distancia y moverse alrededor del origen. El término que falta debe proceder de la dirección $e_r$, que ahora cambia con el ángulo.

[]{#fispm-t1-c08-p0009}

**Proposición 8.9 --- Fórmulas cinemáticas polares.** Si $\rho>0$ y $\rho,\theta\in C^2(J)$ en una representación definición 8.6, entonces $$\mathbf v=\rho'e_r+\rho\theta'e_\theta,$$ $$\mathbf a=(\rho''-\rho(\theta')^2)e_r +(\rho\theta''+2\rho'\theta')e_\theta.$$ La rapidez es $q=\sqrt{(\rho')^2+\rho^2(\theta')^2}$.

**Demostración.** Derivar $\mathbf r=\rho e_r$ con la regla del producto y proposición 8.8 da $\mathbf v=\rho'e_r+\rho\theta'e_\theta$. Para la aceleración derivamos ambos sumandos: $$\mathbf a=\rho''e_r+\rho'\theta'e_\theta +(\rho'\theta'+\rho\theta'')e_\theta -\rho(\theta')^2e_r.$$ Agrupar las direcciones $e_r$ y $e_\theta$ produce la fórmula. Los dos términos $\rho'\theta'$ tienen procedencias distintas: uno deriva la dirección de la velocidad radial y el otro deriva el coeficiente de la velocidad angular. La norma de $\mathbf v$ se obtiene por ortonormalidad. $\square$

La componente radial de la aceleración es $a_r=\rho''-\rho(\theta')^2$, y la angular es $a_\theta=\rho\theta''+2\rho'\theta'$. No son, en general, las segundas derivadas de las coordenadas. Además, $\theta'$ tiene dimensión $T^{-1}$ y $\theta''$ dimensión $T^{-2}$, al medir el ángulo en radianes como cantidad adimensional. Multiplicar por $\rho$ proporciona las dimensiones de velocidad y aceleración. Una supuesta componente lineal $\theta'$ sin factor de longitud tendría dimensiones incorrectas.

[]{#interpretar-los-términos-sin-introducir-fuerzas}

### 8.8.1. Interpretar los términos sin introducir fuerzas {#fispm-c08-interpretar-los-tuxe9rminos-sin-introducir-fuerzas}

Si $\theta$ es constante, la dirección radial también lo es y el movimiento se reduce a una recta: $\mathbf v=\rho'e_r$, $\mathbf a=\rho''e_r$. Si $\rho=b>0$ es constante, la velocidad es $b\theta'e_\theta$ y la aceleración $-b(\theta')^2e_r+b\theta''e_\theta$. El primer término apunta hacia el centro y mide el cambio de dirección; el segundo responde al cambio de velocidad angular. Estos son resultados cinemáticos, sin identificar una fuerza que los produzca.

La dirección $e_\theta$ es perpendicular a la radial. Sólo en un movimiento de radio constante la velocidad queda enteramente en esa dirección y es tangente a la circunferencia. Para una espiral, la tangente a la trayectoria contiene en general las dos direcciones. Llamar «tangencial» a la componente angular puede ocultar esta diferencia si no se indica a qué curva se refiere.

[]{#fispm-t1-c08-mp0008}

**Principio metodológico 8.8 --- Distinguir componente y derivada de coordenada.** Las componentes polares de velocidad son $(\rho',\rho\theta')$ y las de aceleración son $(\rho''-\rho(\theta')^2,\rho\theta''+2\rho'\theta')$. El cálculo debe reconstruir el vector completo antes de interpretar un coeficiente como aceleración física.

[]{#una-recta-vista-desde-coordenadas-polares}

### 8.8.2. Una recta vista desde coordenadas polares {#fispm-c08-una-recta-vista-desde-coordenadas-polares}

La ley cartesiana $\mathbf r(t)=ct e_x+b e_y$, con $b,c>0$, tiene velocidad constante $ce_x$ y aceleración cero. En tiempo $t\in\mathbb R$, su distancia es $\rho=\sqrt{c^2t^2+b^2}$. Una elección continua de ángulo en $(0,\pi)$ cumple $\theta'=-bc/(c^2t^2+b^2)$. Así, $\rho''=b^2c^2/\rho^3>0$, aunque el vector aceleración sea nulo.

Proposición 8.9 resuelve la aparente contradicción: $\rho(\theta')^2=b^2c^2/\rho^3$, exactamente igual a $\rho''$, y la componente radial se cancela. Asimismo, $\rho'=c^2t/\rho$ y $\theta''=2bc^3t/\rho^4$ dan $\rho\theta''+2\rho'\theta'=0$. La curvatura de las coordenadas puede producir derivadas no nulas incluso cuando la historia tiene aceleración nula. No hemos cambiado el movimiento; hemos cambiado su representación.

[]{#ejercicios-7}

### 8.8.3. Ejercicios {#fispm-c08-ejercicios-7}

[]{#fispm-t1-c08-e0015}

**Ejercicio 8.15.** Se da $\rho(t)=L(1+u^2)$ y $\theta(t)=2u$, con $u=(t-t_0)/T\in[-1,1]$. Encuentra velocidad, aceleración y rapidez. Evalúa los vectores en $u=0$ y verifica mediante coordenadas cartesianas la aceleración en ese instante.

**Solución.** Las derivadas son $\rho'=2Lu/T$, $\rho''=2L/T^2$, $\theta'=2/T$ y $\theta''=0$. Proposición 8.9 da $$\mathbf v=\frac LT\,[2u e_r+2(1+u^2)e_\theta],$$ $$\mathbf a=\frac L{T^2}\,[(-2-4u^2)e_r+8u e_\theta], \qquad q=\frac{2L}{T}\sqrt{u^2+(1+u^2)^2}.$$ En cero, $e_r=e_x$, $e_\theta=e_y$, por lo que $\mathbf v=2Le_y/T$ y $\mathbf a=-2Le_x/T^2$. El radio tiene allí un mínimo, pues $\rho''>0$, pero la aceleración radial es negativa: la rotación aporta un término mayor.

Para comprobarlo en cartesianas, $X=(1+u^2)\cos(2u)$ y $Y=(1+u^2)\sin(2u)$. La segunda derivada de $X$ en cero es $2-4=-2$, y la de $Y$ es cero por su imparidad y regularidad. Multiplicar por $L/T^2$ recupera la aceleración encontrada. Esta comparación verifica una cancelación estructural que la sola segunda derivada del radio no permite ver.

[]{#fispm-t1-c08-e0016}

**Ejercicio 8.16.** Un razonamiento afirma: «Si $\rho(t)=b$ y $\theta(t)=\omega t$, ambas coordenadas tienen segunda derivada cero, luego $\mathbf a=0$». Para $b>0$ y $\omega\ne0$, localiza la falla y redacta una corrección completa.

**Solución.** La afirmación trata las direcciones polares como si fueran vectores fijos. En realidad, $\mathbf r=b e_r(t)$ y proposición 8.8 da $e_r'=\omega e_\theta$, $e_\theta'=-\omega e_r$. Por ello, $\mathbf v=b\omega e_\theta$ y $\mathbf a=-b\omega^2e_r$, no nula. Las segundas derivadas escalares $\rho''$ y $\theta''$ son cero, pero proposición 8.9 incluye $-\rho(\theta')^2$. La rapidez es $b|\omega|$ constante y la aceleración cambia la dirección de la velocidad, de acuerdo con la proposición 8.3. La corrección debe conservar ambos pasos de la regla del producto; añadir sólo la conclusión correcta no explica el error.

Proposición 8.9 reorganiza el cálculo de una historia: primero derivamos en el espacio vectorial fijo, después expresamos el resultado en direcciones polares instantáneas. Esta disciplina será la entrada a los marcos móviles. Una base que depende de la posición del objeto y un marco físico cuyos ejes giran no son todavía la misma construcción, aunque en ambos casos haya que derivar direcciones variables.

La fórmula y sus términos se contrastaron con Kleppner--Kolenkow §1.9, pp. 33--38; los ejemplos y las demostraciones de este macrotramo son propios.[^6]

[]{#movimiento-circular-uniforme-y-no-uniforme}

[]{#fispm-t1-c08-s09}

[]{#fpm-i-08-s09}

## 8.9. Movimiento circular uniforme y no uniforme {#fispm-c08-movimiento-circular-uniforme-y-no-uniforme}

Un objeto recorre una pista circular. Conocer el radio y el tiempo de una vuelta no indica, por sí solo, cómo se distribuye su rapidez durante esa vuelta. Puede avanzar lentamente en un sector y más rápido en otro; también puede detenerse o cambiar de sentido. La circunferencia describe la imagen espacial, mientras que la función angular conserva la historia temporal.

[]{#fig:I-08-N03}

![**Figura 8.5.** En el movimiento circular uniforme, la velocidad es tangente y la aceleración es centrípeta. Las flechas representan $v$ y $a$, no un diagrama de fuerzas. Véase §[8.9](#fispm-c08-movimiento-circular-uniforme-y-no-uniforme).](/assets/books/fispm/v04/I-08-N03.svg "fig:"){.fpm-v04-figure fig-alt="Rapidez constante y aceleración" width="340px" fig-cap=""}

[]{#fispm-t1-c08-d0007}

**Definición 8.7 --- Historia circular respecto de un centro fijo.** Una historia circular de radio $b>0$ y centro $C$ se escribe $$P(t)=C+b\bigl(\cos\theta(t)e_x+\sin\theta(t)e_y\bigr),$$ con $\theta$ de la regularidad exigida en el intervalo considerado. Su velocidad angular escalar firmada es $\omega(t)=\theta'(t)$. Llamaremos uniforme a la historia con $\theta(t)=\theta_0+\omega_0(t-t_0)$ y $\omega_0\ne0$ constante.

El centro es fijo y $b$ tiene dimensión de longitud. La velocidad angular tiene dimensión $T^{-1}$ y su signo depende de la orientación del plano. En una ley uniforme completa, la imagen es toda la circunferencia; en un intervalo corto puede ser sólo un arco. La historia constante, con $\omega_0=0$, describe reposo y no tiene un período fundamental positivo de revolución.

[]{#fispm-t1-c08-p0010}

**Proposición 8.10 --- Cinemática de una historia circular.** Si $\theta\in C^2$, entonces $$\mathbf v=b\omega e_\theta,\qquad \mathbf a=-b\omega^2e_r+b\omega'e_\theta,\qquad q=b|\omega|.$$ En cada instante con $\omega\ne0$, la componente de aceleración paralela a la dirección del movimiento es $q'=b\operatorname{sgn}(\omega)\omega'$, y la magnitud de la componente perpendicular es $q^2/b$. Para una ley uniforme definida en todo $\mathbb R$, el período fundamental de la posición es $\mathcal T=2\pi/|\omega_0|$.

**Demostración.** Tomamos el origen polar en $C$ y aplicamos proposición 8.9 con $\rho=b$ constante. Desaparecen $\rho'$ y $\rho''$, y quedan las fórmulas de velocidad y aceleración. La norma de $\mathbf v$ es $b|\omega|$. Cuando $\omega\ne0$, la dirección del movimiento es $\operatorname{sgn}(\omega)e_\theta$, por lo que proyectar $\mathbf a$ en ella da $b\operatorname{sgn}(\omega)\omega'$. La parte radial es perpendicular a la velocidad y tiene norma $b\omega^2=q^2/b$.

En la ley uniforme, $P(t+s)=P(t)$ para todo $t$ si y sólo si $\omega_0s$ es múltiplo entero de $2\pi$. Entre los valores positivos de $s$, el menor es $2\pi/|\omega_0|$. Es el período fundamental, no sólo un tiempo de retorno encontrado en un instante. $\square$

La rapidez puede ser constante aunque el vector aceleración gire durante el recorrido. En una ley uniforme, su norma $b\omega_0^2$ es constante y su dirección apunta siempre hacia el centro. La denominación *centrípeta* describe esa dirección; no identifica aún una interacción física que mantenga el movimiento.

Si $\omega$ se anula en un instante, las fórmulas vectoriales siguen siendo válidas. La expresión $q'$ puede requerir cuidado: $|\omega|$ no tiene por qué ser diferenciable en un cero donde $\omega$ cambia de signo. Proposición 8.3 exigía rapidez positiva precisamente para evitar ese problema. Una aceleración angular no nula en el instante de reposo puede poner al objeto en movimiento inmediatamente después.

[]{#fispm-t1-c08-mp0009}

**Principio metodológico 8.9 --- Distinguir una vuelta de un período.** Un retorno al punto inicial ocurre cuando cambia el ángulo en un múltiplo de $2\pi$. Un período de toda la historia exige que el mismo desplazamiento temporal reproduzca la posición en cada instante del dominio pertinente. Un retorno aislado no prueba periodicidad.

[]{#ejercicios-8}

### 8.9.1. Ejercicios {#fispm-c08-ejercicios-8}

[]{#fispm-t1-c08-e0017}

**Ejercicio 8.17.** Sea $b=3L$ y $\theta(u)=u^2$ para $u\ge0$. Calcula velocidad, aceleración y rapidez. Compara el tiempo de la primera vuelta con la duración de la segunda. ¿Hay reposo inicial con aceleración no nula?

**Solución.** La velocidad angular es $2u/T$ y su derivada temporal es $2/T^2$. Proposición 8.10 da $$\mathbf v=\frac{6L}{T}u e_\theta, \qquad \mathbf a=\frac{L}{T^2}(-12u^2e_r+6e_\theta), \qquad q=\frac{6L}{T}u.$$ La primera vuelta termina en $u_1=\sqrt{2\pi}$ y la segunda en $u_2=\sqrt{4\pi}$. Sus duraciones son $T\sqrt{2\pi}$ y $T(\sqrt{4\pi}-\sqrt{2\pi})$, diferentes. Tampoco existe un desplazamiento temporal positivo $s$ que reproduzca toda la historia: la diferencia angular normalizada $(u+s)^2-u^2=2us+s^2$ varía continuamente con $u$ y no puede tomar sólo múltiplos enteros de $2\pi$. En cero la velocidad es nula, pero la aceleración es $6Le_\theta/T^2$, usando la extensión suave o la derivada unilateral. Reposo instantáneo no implica ausencia de cambio de velocidad.

[]{#fispm-t1-c08-e0018}

**Ejercicio 8.18.** Una historia tiene centro fijo $C$, radio $2L$ y ángulo $\theta(u)=\pi/2-3u$. Encuentra sentido, rapidez, aceleración y período. Explica por qué cambiar el signo de la velocidad angular no cambia la dirección radial de la aceleración.

**Solución.** La velocidad angular es $-3/T$: el movimiento sigue el sentido angular negativo. La velocidad es $-6Le_\theta/T$, la rapidez $6L/T$ y la aceleración $-18Le_r/T^2$. El período es $2\pi T/3$. La parte radial contiene el cuadrado de la velocidad angular; al invertir el sentido, sigue apuntando hacia $C$. Las posiciones en un mismo tiempo pueden cambiar por esa inversión, pero en cada una la aceleración uniforme es radial hacia dentro.

El tratamiento usa la interfaz polar ya demostrada. Shankar §2.6 y Kleppner--Kolenkow §1.9 sirven de contraste para el caso uniforme y la separación entre cambio de dirección y cambio de rapidez.[^7]

[]{#marcos-con-origen-en-traslación}

[]{#fispm-t1-c08-s10}

[]{#fpm-i-08-s10}

## 8.10. Marcos con origen en traslación {#fispm-c08-marcos-con-origen-en-traslaciuxf3n}

Una persona observa un objeto desde una plataforma que se desplaza. Aunque sus ejes permanezcan paralelos a los del suelo, la coordenada que registra es una posición respecto de un origen móvil. Derivar esa coordenada mide el cambio relativo a la plataforma, y no necesariamente la velocidad descrita desde el origen fijo.

Mantendremos un único reloj y las mismas unidades de longitud. Es una elección del modelo cinemático clásico que permite comparar simultáneamente posiciones en los dos marcos. No estamos deduciendo una transformación de relojes a partir de la geometría espacial.

[]{#fispm-t1-c08-d0008}

**Definición 8.8 --- Marco en traslación y posición relativa.** En un espacio de dimensión $2$ o $3$, sean $O$ y $B$ un origen y una base ortonormal fijos. Un marco en traslación tiene origen $O'(t)=O+\mathbf c(t)$ y conserva la base $B$. Si $P(t)=O+\mathbf r(t)$, su posición relativa al origen móvil es $$\mathbf y(t)=\mathbf r(t)-\mathbf c(t).$$ Llamaremos velocidad y aceleración relativas a las derivadas $\mathbf y'$ y $\mathbf y''$ cuando existan. Su significado depende del origen móvil declarado.

La identidad $P=O'+\mathbf y$ compara un punto con dos representaciones de origen. El vector $\mathbf y$ existe en el espacio de desplazamientos, pero su derivada pierde la invariancia frente a un cambio temporal del origen: el vector $\mathbf c$ ya no es constante.

[]{#fispm-t1-c08-p0011}

**Proposición 8.11 --- Composición bajo traslación.** Si $\mathbf c$ y $\mathbf y$ son de clase $C^2$, entonces $$\mathbf v=\mathbf c'+\mathbf y',\qquad \mathbf a=\mathbf c''+\mathbf y''.$$ Si $\mathbf c(t)=\mathbf c_0+\mathbf U(t-t_0)$ con $\mathbf U$ constante, la velocidad relativa es $\mathbf v-\mathbf U$ y la aceleración relativa coincide con $\mathbf a$. Las dos aceleraciones coinciden en todo un intervalo si y sólo si $\mathbf c''=0$ allí.

**Demostración.** definición 8.8 da $\mathbf r=\mathbf c+\mathbf y$. Derivar una vez y luego otra produce las dos identidades. Para una traslación uniforme, $\mathbf c'=\mathbf U$ y $\mathbf c''=0$, lo que da las fórmulas particulares. En general, $\mathbf a-\mathbf y''=\mathbf c''$; por tanto, la igualdad de aceleraciones en cada instante equivale a $\mathbf c''=0$ en cada instante del intervalo. $\square$

El resultado es cinemático. La igualdad de aceleraciones bajo traslación uniforme no demuestra aquí que ambos marcos sean inerciales ni cómo se transforman las leyes dinámicas. La transformación espacial $\mathbf y=\mathbf r-\mathbf c_0-\mathbf U(t-t_0)$, acompañada por el reloj común, es la parte de la transformación galileana que necesitamos. Su uso como descripción física se mantiene dentro del régimen clásico elegido.

[]{#reposo-y-rapidez-en-dos-descripciones}

### 8.10.1. Reposo y rapidez en dos descripciones {#fispm-c08-reposo-y-rapidez-en-dos-descripciones}

Si $\mathbf y$ es constante, el objeto permanece fijo respecto de la plataforma y su velocidad en el marco fijo es $\mathbf c'$. Si $\mathbf r$ es constante, su velocidad relativa es $-\mathbf c'$. La palabra «reposo» necesita un marco. Lo mismo ocurre con la rapidez: $\|\mathbf v-\mathbf U\|$ no suele ser $\|\mathbf v\|-\|\mathbf U\|$, pues la norma depende de la dirección de ambos vectores.

La aceleración puede coincidir y las velocidades diferir. Por ejemplo, un objeto con aceleración prescrita $-ge_y$ mantiene esa misma aceleración en una plataforma que se traslada uniformemente, pero sus componentes iniciales de velocidad cambian por la sustracción de $\mathbf U$. La parábola descrita desde la plataforma puede tener otra componente horizontal o degenerar en una recta vertical. La trayectoria espacial relativa al origen móvil es una representación distinta de la imagen del movimiento en el marco fijo.

[]{#fispm-t1-c08-mp0010}

**Principio metodológico 8.10 --- Nombrar el marco de una derivada.** Toda velocidad o aceleración relativa debe indicar respecto de qué origen y ejes se obtiene. Para ejes paralelos fijos, las derivadas se relacionan por la proposición 8.11. Una igualdad de aceleraciones no autoriza una igualdad de velocidades ni de trayectorias.

[]{#ejercicios-9}

### 8.10.2. Ejercicios {#fispm-c08-ejercicios-9}

[]{#fispm-t1-c08-e0019}

**Ejercicio 8.19.** En variables normalizadas, el origen móvil tiene $\mathbf C(u)=u^2e_x-u e_y$ y el objeto tiene posición relativa $\mathbf Y(u)=(1+u)e_x+2e_y$. Reconstruye posición, velocidad y aceleración en el marco fijo, y compara las aceleraciones.

**Solución.** La posición relativa al origen fijo es $\mathbf R=\mathbf C+\mathbf Y=(1+u+u^2)e_x+(2-u)e_y$. La velocidad física es $(L/T)((1+2u)e_x-e_y)$ y la aceleración es $2Le_x/T^2$. En el marco móvil, $\mathbf y'=Le_x/T$ y $\mathbf y''=0$. La diferencia de aceleraciones es $\mathbf c''=2Le_x/T^2$, exactamente la aceleración del origen móvil. La historia es uniforme respecto de esa plataforma, pero no respecto del marco fijo.

[]{#fispm-t1-c08-e0020}

**Ejercicio 8.20.** Un proyectil tiene $\mathbf r(\tau)=p\tau e_x+(h+w\tau-g\tau^2/2)e_y$, con $p>0$, $h>0$ y $g>0$. El origen de una plataforma sigue $\mathbf c(\tau)=p\tau e_x$. Describe el vuelo desde la plataforma y determina si cambia el tiempo de contacto con el suelo.

**Solución.** definición 8.8 da $\mathbf y=(h+w\tau-g\tau^2/2)e_y$. El proyectil permanece sobre la vertical del origen móvil: su componente horizontal relativa es cero. Su aceleración relativa es $-ge_y$, pues la plataforma tiene aceleración nula. El suelo $y=0$ mantiene la misma altura en esta traslación horizontal; el tiempo de contacto sigue siendo $(w+\sqrt{w^2+2gh})/g$. En ese instante el punto de llegada, expresado en el marco fijo, tiene abscisa $p\tau_f$; desde la plataforma tiene abscisa relativa cero. El evento físico no ha cambiado, aunque sí su representación.

Kleppner--Kolenkow §8.2 permite contrastar la resta de velocidades y aceleraciones y la hipótesis de reloj común. Se utiliza únicamente su relación cinemática de posiciones y derivadas.[^8]

[]{#marcos-planos-con-ejes-en-rotación}

[]{#fispm-t1-c08-s11}

[]{#fpm-i-08-s11}

## 8.11. Marcos planos con ejes en rotación {#fispm-c08-marcos-planos-con-ejes-en-rotaciuxf3n}

Una cámara puede desplazarse y girar al mismo tiempo. Ahora un objeto que conserva sus coordenadas en la imagen no mantiene necesariamente un vector constante respecto del suelo: los ejes de la cámara cambian de dirección. La composición de velocidades necesita reconocer ese giro además del movimiento del origen.

Trabajamos en un plano orientado con base fija $(e_x,e_y)$. Introducimos el operador $J$, que gira noventa grados en el sentido positivo: $Je_x=e_y$ y $Je_y=-e_x$. Así, $J^2=-\operatorname{Id}$, $\|Jz\|=\|z\|$ y $z\cdot Jz=0$. Sólo usamos un operador lineal del plano, sin introducir un eje angular tridimensional.

[]{#fispm-t1-c08-d0009}

**Definición 8.9 --- Marco plano en traslación y rotación.** Sean $\mathbf c(t)$ de clase $C^2$ y $\varphi(t)$ de clase $C^2$. Definimos $Q(t)$ como la rotación de ángulo $\varphi(t)$, con $$Qe_x=\cos\varphi\,e_x+\sin\varphi\,e_y, \qquad Qe_y=-\sin\varphi\,e_x+\cos\varphi\,e_y.$$ El marco tiene origen $O+\mathbf c$ y base $(Qe_x,Qe_y)$. Las coordenadas móviles $\xi_1,\xi_2$ se reúnen en el vector auxiliar $\mathbf y=\xi_1e_x+\xi_2e_y$ y representan la posición mediante $$\mathbf r=\mathbf c+Q\mathbf y.$$ Denotamos $\omega=\varphi'$. El vector relativo de velocidad expresado en direcciones móviles es $Q\mathbf y'$; no se identifica con $(Q\mathbf y)'$.

El vector auxiliar $\mathbf y$ conserva los números registrados en el marco móvil, colocados en una copia con direcciones fijas para poder diferenciarlos. Aplicar $Q$ devuelve su interpretación espacial instantánea. Esta separación permite escribir una fórmula breve sin confundir las componentes con el vector físico que representan.

[]{#fispm-t1-c08-p0012}

**Proposición 8.12 --- Derivadas en un marco plano móvil.** Bajo definición 8.9, si $\mathbf y\in C^2$, entonces $$\mathbf v=\mathbf c'+Q\bigl(\mathbf y'+\omega J\mathbf y\bigr),$$ $$\mathbf a=\mathbf c''+Q\bigl(\mathbf y''+2\omega J\mathbf y' +\omega'J\mathbf y-\omega^2\mathbf y\bigr).$$

**Demostración.** Derivar las dos columnas de $Q$ muestra que $Q'=\omega QJ$. Además, $QJ=JQ$, como se comprueba aplicando ambos operadores a $e_x$ y $e_y$. Derivar $\mathbf r=\mathbf c+Q\mathbf y$ da $\mathbf v=\mathbf c'+Q(\mathbf y'+\omega J\mathbf y)$.

Para la segunda derivada, ponemos $z=\mathbf y'+\omega J\mathbf y$. La regla del producto da $(Qz)'=Q(\omega Jz+z')$. Como $z'=\mathbf y''+\omega'J\mathbf y+\omega J\mathbf y'$, sustituir y usar $J^2=-\operatorname{Id}$ produce $$\omega Jz+z' =\mathbf y''+2\omega J\mathbf y'+\omega'J\mathbf y-\omega^2\mathbf y.$$ Añadir $\mathbf c''$ completa la fórmula. $\square$

La aceleración tiene cinco contribuciones: movimiento del origen, segunda derivada de las coordenadas, término mixto entre giro y movimiento relativo, cambio de velocidad angular y giro de un punto con coordenadas fijas. Cada término se obtiene de la relación de posiciones. No se añaden por analogía con una fuerza ni se deducen de una imagen.

El término $2\omega QJ\mathbf y'$ suele denominarse aceleración de Coriolis en esta descomposición. El término $-\omega^2Q\mathbf y$ apunta hacia el origen móvil cuando se interpreta aisladamente. La fórmula relaciona descripciones de aceleración; identificar términos de una ecuación dinámica requerirá declarar un marco y leyes físicas. No convertimos aquí estos sumandos en interacciones.

[]{#qué-cambia-respecto-de-las-coordenadas-polares}

### 8.11.1. Qué cambia respecto de las coordenadas polares {#fispm-c08-quuxe9-cambia-respecto-de-las-coordenadas-polares}

En §8, la dirección radial se eligió desde la posición del objeto y el ángulo era el de esa posición. En definición 8.9, el ángulo $\varphi$ pertenece al marco y se prescribe independientemente de dónde esté el objeto. Las coordenadas $\xi_1,\xi_2$ pueden cambiar ambas, y el objeto puede cruzar el origen del marco sin singularidad de esta representación cartesiana móvil.

Proposición 8.9 se recupera como una elección particular: si $\mathbf c=0$, $\varphi=\theta$ y $\mathbf y=\rho e_x$, proposición 8.12 da $\mathbf v=\rho'e_r+\rho\theta'e_\theta$ y la aceleración polar. Esa comprobación explica por qué aparece el mismo factor dos, sin confundir dos construcciones que cumplen funciones diferentes.

[]{#fispm-t1-c08-mp0011}

**Principio metodológico 8.11 --- Reconstruir antes de derivar.** Para un marco giratorio, la relación básica es $\mathbf r=\mathbf c+Q\mathbf y$. La velocidad y aceleración se obtienen derivándola con todos sus factores. La suma $\mathbf c'+Q\mathbf y'$ sólo es suficiente si desaparece el término de giro por una condición comprobada.

[]{#ejercicios-10}

### 8.11.2. Ejercicios {#fispm-c08-ejercicios-10}

[]{#fispm-t1-c08-e0021}

**Ejercicio 8.21.** El origen móvil coincide con el fijo, $\varphi(u)=u$ y $\mathbf Y(u)=2e_x+e_y$ es constante. Encuentra velocidad, aceleración y rapidez en el marco fijo. ¿Qué observa la cámara en sus coordenadas?

**Solución.** Aquí $\omega=1/T$ y $\mathbf y'=\mathbf y''=0$. Proposición 8.12 da $\mathbf v=(L/T)Q(-e_x+2e_y)$ y $\mathbf a=-(L/T^2)Q(2e_x+e_y)$. La rapidez es $\sqrt5L/T$. La cámara registra coordenadas constantes $(2L,L)$ y reposo relativo. El punto describe en el marco fijo una circunferencia de radio $\sqrt5L$. El giro del marco basta para producir movimiento respecto de las direcciones fijas, aun cuando las derivadas de sus coordenadas sean cero.

[]{#fispm-t1-c08-e0022}

**Ejercicio 8.22.** Sea $\mathbf c=0$, $\varphi(u)=u^2/2$ y $\mathbf Y(u)=(1+u)e_x$, con $0\le u\le1$. Calcula las contribuciones de aceleración de la proposición 8.12 y verifica el resultado derivando la posición cartesiana.

**Solución.** En unidades normalizadas, $\varphi_u'=u$, $\varphi_u''=1$, $\mathbf Y'=e_x$ y $\mathbf Y''=0$. Las contribuciones dentro de $Q$ son cero, $2u e_y$, $(1+u)e_y$ y $-u^2(1+u)e_x$. Por tanto, $$\mathbf a=\frac{L}{T^2}Q\bigl(-u^2(1+u)e_x+(1+3u)e_y\bigr).$$ Para verificarlo, escribimos $X=(1+u)\cos(u^2/2)$ y $Y=(1+u)\sin(u^2/2)$. La primera derivada es $Q(e_x+u(1+u)e_y)$; derivar esa expresión con $Q_u'=uQJ$ recupera exactamente las dos componentes anteriores. En $u=0$ la velocidad angular es cero, pero su derivada no, y la aceleración vale $Le_y/T^2$. Omitir el término angular de cambio de giro perdería ese resultado.

[]{#fispm-t1-c08-e0023}

**Ejercicio 8.23.** Una historia está fija en el marco cartesiano: $\mathbf r=Le_x$. El origen móvil es cero y sus ejes giran con $\varphi(u)=u$. Encuentra las coordenadas móviles y comprueba con la proposición 8.12 que velocidad y aceleración en el marco fijo son nulas.

**Solución.** La inversión de la definición 8.9 es $\mathbf y=Q^{-1}\mathbf r$, de modo que $\mathbf Y=\cos u\,e_x-\sin u\,e_y$. Derivar respecto de $u$ da $\mathbf Y'=-J\mathbf Y$ y $\mathbf Y''=-\mathbf Y$. La fórmula normalizada de velocidad tiene $\mathbf Y'+J\mathbf Y=0$. La de aceleración tiene $$\mathbf Y''+2J\mathbf Y'-\mathbf Y =-\mathbf Y+2\mathbf Y-\mathbf Y=0.$$ La cámara registra una rotación en sentido contrario, aunque el objeto no se mueve en el marco fijo. Sus coordenadas tienen derivadas no nulas que se cancelan con los términos debidos al giro. El cálculo evita atribuir al objeto una aceleración sólo por la curvatura de ese registro relativo.

Kleppner--Kolenkow §8.5, pp. 356--359, controla las derivadas de direcciones giratorias y el término mixto para giro uniforme. Proposición 8.12 incorpora además traslación y velocidad angular variable mediante una derivación planar propia.[^9]

[]{#composición-de-movimientos-y-encuentros}

[]{#fispm-t1-c08-s12}

[]{#fpm-i-08-s12}

## 8.12. Composición de movimientos y encuentros {#fispm-c08-composiciuxf3n-de-movimientos-y-encuentros}

Una persona camina sobre una plataforma que, a su vez, se mueve respecto del suelo. La descripción combina dos relaciones de posición. Si una de ellas utiliza ejes giratorios, sus números deben transformarse antes de sumarlos: una componente horizontal de la plataforma no es automáticamente una componente horizontal del suelo.

[]{#fispm-t1-c08-p0013}

**Proposición 8.13 --- Composición de dos marcos planos.** Supongamos que $\mathbf r=\mathbf c_1+Q_1\mathbf y$ y $\mathbf y=\mathbf c_2+Q_2\mathbf z$, con funciones de clase $C^2$ y rotaciones planas $Q_1,Q_2$. Entonces $$\mathbf r=\mathbf c+Q\mathbf z, \qquad \mathbf c=\mathbf c_1+Q_1\mathbf c_2, \qquad Q=Q_1Q_2.$$ Si $Q_i$ tiene ángulo continuado $\varphi_i$, podemos usar $\varphi=\varphi_1+\varphi_2$ para $Q$. La velocidad angular total es $\omega_1+\omega_2$, pero la velocidad del origen compuesto es $$\mathbf c'=\mathbf c_1'+Q_1(\mathbf c_2'+\omega_1J\mathbf c_2).$$

**Demostración.** Sustituir la segunda relación en la primera produce $\mathbf c_1+Q_1\mathbf c_2+Q_1Q_2\mathbf z$, lo que prueba la fórmula de posición. Las identidades de suma del seno y del coseno dan $Q_1Q_2=Q_{\varphi_1+\varphi_2}$. Derivar el ángulo produce la suma de velocidades angulares. Derivar $\mathbf c=\mathbf c_1+Q_1\mathbf c_2$ y usar $Q_1'=\omega_1Q_1J$ da la última identidad. $\square$

La suma angular usa que ambas rotaciones actúan en el mismo plano orientado. No se presenta como regla para rotaciones espaciales generales. En tres dimensiones, las traslaciones con ejes paralelos se componen por suma de sus vectores; el caso giratorio espacial requiere una construcción que no necesitamos aquí.

Para dos traslaciones sin giro, proposición 8.13 reduce a $\mathbf r=\mathbf c_1+\mathbf c_2+\mathbf z$. Derivar permite sumar las tres velocidades vectoriales. Las rapidez no se suman salvo condiciones particulares de dirección. Por ejemplo, una componente transversal respecto de una plataforma puede ser necesaria para cancelar el avance de la plataforma en otra dirección.

[]{#encuentros-como-igualdades-simultáneas}

### 8.12.1. Encuentros como igualdades simultáneas {#fispm-c08-encuentros-como-igualdades-simultuxe1neas}

Sean $P_A,P_B$ dos historias en un dominio temporal común $I$. El conjunto de tiempos de encuentro es $E=\{t\in I:P_A(t)=P_B(t)\}$. Dos curvas espaciales pueden cruzarse en un punto y no tener un encuentro, si cada objeto pasa por allí en tiempos distintos.

[]{#fispm-t1-c08-p0014}

**Proposición 8.14 --- Invariancia del encuentro bajo un marco común.** Si ambas historias se representan en el mismo marco móvil $\mathbf r_A=\mathbf c+Q\mathbf y_A$ y $\mathbf r_B=\mathbf c+Q\mathbf y_B$, con $Q$ invertible en cada instante, entonces $$\{t\in I:P_A(t)=P_B(t)\} =\{t\in I:\mathbf y_A(t)=\mathbf y_B(t)\}.$$ Si $Q$ es ortogonal, también $\|\mathbf r_A(t)-\mathbf r_B(t)\|=\|\mathbf y_A(t)-\mathbf y_B(t)\|$ para cada instante.

**Demostración.** Restar las posiciones elimina el origen común y da $\mathbf r_A-\mathbf r_B=Q(\mathbf y_A-\mathbf y_B)$. Por invertibilidad de $Q$, el primer vector es cero si y sólo si lo es el segundo. Esa equivalencia puntual, para cada $t\in I$, prueba ambas inclusiones entre los conjuntos de tiempos. La igualdad de normas se sigue de la ortogonalidad. $\square$

El encuentro es el mismo evento físico en ambas descripciones. La conclusión necesita el mismo marco y reloj para los dos objetos. Restar coordenadas de cámaras diferentes sin transformar sus orígenes y ejes no permite usar proposición 8.14. Tampoco la distancia instantánea entre objetos debe confundirse con la longitud de una trayectoria relativa: derivar una rotación temporal introduce términos nuevos.

[]{#fispm-t1-c08-mp0012}

**Principio metodológico 8.12 --- Componer posiciones antes de componer eventos.** Se expresan las historias en un marco común, se conserva el reloj y después se resuelve la igualdad de posiciones. La coincidencia de una coordenada, la intersección de imágenes o la igualdad de rapidez no reemplazan esa condición.

[]{#ejercicios-11}

### 8.12.2. Ejercicios {#fispm-c08-ejercicios-11}

[]{#fispm-t1-c08-e0024}

**Ejercicio 8.24.** En tiempo normalizado, $\mathbf c_1=0$, $Q_1=Q_u$, $\mathbf C_2=e_x$ y $Q_2=Q_{-u}$. Un objeto tiene coordenadas constantes $\mathbf Z=2e_y$ en el segundo marco. Encuentra su historia en el marco fijo. ¿La cancelación de ángulos implica reposo de todo el marco compuesto?

**Solución.** proposición 8.13 da $Q=Q_uQ_{-u}=\operatorname{Id}$, pero $\mathbf C=Q_u e_x$. La posición normalizada es $\mathbf R=Q_u e_x+2e_y$. Su velocidad es $(L/T)Q_u e_y$ y su aceleración $-(L/T^2)Q_u e_x$. La orientación total permanece fija mientras el origen recorre una circunferencia. Cancelar los giros de ejes no cancela la traslación que el primer giro induce en un origen situado fuera del centro.

[]{#fispm-t1-c08-e0025}

**Ejercicio 8.25.** En $0\le u\le3$, dos historias tienen $\mathbf R_A=(u,1)$ y $\mathbf R_B=(2,u)$ en coordenadas normalizadas fijas. Sus imágenes se cruzan. Determina si hay encuentro y verifica el resultado en el marco $\mathbf C=(u,0)$, $Q=Q_u$.

**Solución.** La imagen de A contiene el punto $(2,1)$ en $u=2$; la de B lo contiene en $u=1$. Para un encuentro simultáneo se exige $(u,1)=(2,u)$, que requeriría $u=2$ y $u=1$ a la vez. No existe tal tiempo. En el marco móvil, la diferencia de coordenadas es $Q_{-u}(\mathbf R_A-\mathbf R_B)=Q_{-u}(u-2,1-u)$. Por invertibilidad, sólo podría anularse si ambas componentes originales se anularan simultáneamente; ya comprobamos que eso no ocurre. El cambio de marco conserva la ausencia de encuentro.

[]{#aproximaciones-vectoriales-y-horizonte-de-validez}

[]{#fispm-t1-c08-s13}

[]{#fpm-i-08-s13}

## 8.13. Aproximaciones vectoriales y horizonte de validez {#fispm-c08-aproximaciones-vectoriales-y-horizonte-de-validez}

Una ley cinemática puede omitir una pequeña contribución a la aceleración y aun así acumular un defecto de posición apreciable durante un vuelo largo. La evaluación de la reducción necesita la observable y el intervalo: un error pequeño en aceleración no es directamente un error pequeño en posición.

[]{#fispm-t1-c08-d0010}

**Definición 8.10 --- Errores vectoriales comparables.** Para dos historias expresadas en el mismo marco fijo y reloj, definimos el error de posición $e_r(t)=\|\mathbf r(t)-\widetilde{\mathbf r}(t)\|$ y el de velocidad $e_v(t)=\|\mathbf v(t)-\widetilde{\mathbf v}(t)\|$. Un error referido a una escala $S>0$ del mismo tipo es el cociente correspondiente dividido por $S$.

El error de posición tiene dimensión $L$ y el de velocidad $L/T$. El error relativo a la norma de una predicción no se define cuando esa norma es cero. Una escala física positiva evita esa división, siempre que se explique qué comparación mide. No se interpreta una cota determinista como una probabilidad o incertidumbre estadística de la observación.

[]{#fispm-t1-c08-p0015}

**Proposición 8.15 --- Acumulación de un defecto de aceleración.** Sean dos historias $C^2$ en $[t_0,t_0+H]$, con $H>0$. Supongamos $$e_r(t_0)\le\delta_r,\qquad e_v(t_0)\le\delta_v, \qquad \|\mathbf a(t)-\widetilde{\mathbf a}(t)\|\le A,$$ para todo el intervalo, donde $\delta_r,\delta_v,A\ge0$. Para $0\le\tau\le H$, entonces $$e_v(t_0+\tau)\le\delta_v+A\tau,$$ $$e_r(t_0+\tau)\le\delta_r+\delta_v\tau+\tfrac12 A\tau^2.$$

**Demostración.** Primero justificamos que, para una función vectorial continua $f$ en $[a,b]$, $\|\int_a^b f\|\le\int_a^b\|f\|$. Si la integral es nula, la desigualdad es inmediata. Si es un vector no nulo $D$, tomamos $m=D/\|D\|$ y usamos Cauchy--Schwarz para obtener $\|D\|=\int m\cdot f\le\int\|f\|$.

Restar las reconstrucciones de velocidad de la proposición 8.2 da una diferencia inicial más la integral del defecto de aceleración. La desigualdad triangular y la cota integral anterior producen $e_v\le\delta_v+A\tau$. Restar las reconstrucciones de posición da, exactamente, $$\Delta\mathbf r(t_0+\tau) =\Delta\mathbf r(t_0)+\tau\Delta\mathbf v(t_0) +\int_{t_0}^{t_0+\tau}(t_0+\tau-s)\Delta\mathbf a(s)\,ds.$$ El núcleo de la integral es no negativo en el segmento. Tomar normas y aplicar la cota $A$ da $\delta_r+\delta_v\tau+A\int_{t_0}^{t_0+\tau}(t_0+\tau-s)ds$, que es la expresión anunciada. $\square$

La cota funciona en dos y tres dimensiones y no supone que el defecto conserve una dirección. Puede ser conservadora: cambios de dirección del defecto pueden cancelarse parcialmente al integrar, pero la norma no descuenta una cancelación que aún no se conoce. Con datos iniciales exactos, el defecto máximo de posición garantizado crece como $A\tau^2/2$.

[]{#fispm-t1-c08-d0011}

**Definición 8.11 --- Horizonte certificado de una reducción.** Para una tolerancia de posición $\varepsilon S$ con $S>0$ y $\varepsilon>0$, un horizonte certificado es un $H>0$ dentro del dominio común de los modelos tal que la cota probada garantiza $e_r(t_0+\tau)\le\varepsilon S$ para todo $0\le\tau\le H$. Es una garantía suficiente, no necesariamente el último tiempo en que el error real cumple la tolerancia.

Con proposición 8.15 basta imponer $\delta_r+\delta_vH+AH^2/2\le\varepsilon S$. Esa condición controla todos los tiempos anteriores porque sus coeficientes son no negativos. Si $A=0$ y los datos iniciales coinciden, no hay defecto de estas historias; eso no demuestra que el modelo sea adecuado para un fenómeno durante un tiempo ilimitado. La comparación se refiere a los dos modelos y al dominio declarados.

[]{#errores-de-representación-del-marco}

### 8.13.1. Errores de representación del marco {#fispm-c08-errores-de-representaciuxf3n-del-marco}

Un instrumento puede conocer imperfectamente su origen y orientación. Entonces hay que separar el defecto de las coordenadas del defecto de la transformación que las coloca en el espacio.

[]{#fispm-t1-c08-p0016}

**Proposición 8.16 --- Cota de posición con un marco aproximado.** En un mismo instante, sean $\mathbf r=\mathbf c+Q_\varphi\mathbf y$ y $\widetilde{\mathbf r}=\widetilde{\mathbf c}+Q_{\widetilde\varphi}\widetilde{\mathbf y}$ dos representaciones planas. Entonces $$\|\mathbf r-\widetilde{\mathbf r}\| \le\|\mathbf c-\widetilde{\mathbf c}\| +\|\mathbf y-\widetilde{\mathbf y}\| +2\left|\sin\frac{\varphi-\widetilde\varphi}{2}\right| \|\widetilde{\mathbf y}\|.$$ El último término es a lo sumo $|\varphi-\widetilde\varphi|\,\|\widetilde{\mathbf y}\|$. Si el marco es exactamente el mismo, el error de posición es precisamente $\|\mathbf y-\widetilde{\mathbf y}\|$.

**Demostración.** Restar ambas expresiones y añadir y sustraer $Q_\varphi\widetilde{\mathbf y}$ da una suma de tres vectores: defecto del origen, $Q_\varphi(\mathbf y-\widetilde{\mathbf y})$ y $(Q_\varphi-Q_{\widetilde\varphi})\widetilde{\mathbf y}$. La norma del segundo coincide con la del defecto de coordenadas.

Para cualquier vector $z$, la ortogonalidad y el producto escalar entre dos giros del mismo vector dan $$\|(Q_\varphi-Q_{\widetilde\varphi})z\|^2 =2\|z\|^2(1-\cos(\varphi-\widetilde\varphi)) =4\|z\|^2\sin^2\frac{\varphi-\widetilde\varphi}{2}.$$ Tomar raíces y aplicar la desigualdad triangular prueba la cota. La desigualdad $|\sin x|\le|x|$ da la versión lineal. Si origen y rotación coinciden, sólo permanece el segundo vector y su norma es exactamente $\|\mathbf y-\widetilde{\mathbf y}\|$. $\square$

Un mismo defecto angular puede producir un defecto de longitud mayor para objetos más alejados del origen. Además, una diferencia de ángulo de $2\pi$ no produce defecto de orientación: la cota trigonométrica lo reconoce exactamente, mientras que la lineal es más conservadora. Para una comparación local de ángulos conviene elegir continuaciones o representantes que hagan significativo el defecto declarado.

[]{#fispm-t1-c08-mp0013}

**Principio metodológico 8.13 --- Controlar una observable durante un intervalo.** Una reducción registra qué término omite, cómo lo acota, qué datos iniciales conserva, qué observable controla y durante cuánto tiempo. Si también aproxima el marco, debe incluir ese defecto en la comparación espacial. La señal de salida del régimen no se sustituye por una afirmación de exactitud global.

[]{#ejercicios-12}

### 8.13.2. Ejercicios {#fispm-c08-ejercicios-12}

[]{#fispm-t1-c08-e0026}

**Ejercicio 8.26.** Dos modelos parten con los mismos datos iniciales y su defecto de aceleración cumple $\|\Delta\mathbf a\|\le0{,}02L/T^2$. Se exige error de posición a lo sumo $0{,}01L$ durante todo el intervalo. Encuentra un horizonte garantizado por la proposición 8.15 y un defecto constante que alcance la cota.

**Solución.** proposición 8.15 da $e_r\le0{,}01L(\tau/T)^2$. La tolerancia se garantiza para $0\le\tau\le T$, siempre que la cota de aceleración valga en ese intervalo. Un defecto constante $\Delta\mathbf a=0{,}02Le_x/T^2$ produce $\Delta\mathbf r=0{,}01L(\tau/T)^2e_x$ y alcanza la cota en cada instante. Sin conocer la dirección o estructura del defecto, no podemos certificar un horizonte mayor con esa misma información. Un caso con cancelaciones podría cumplir la tolerancia más tiempo.

[]{#fispm-t1-c08-e0027}

**Ejercicio 8.27.** El marco se conoce con defecto de origen a lo sumo $0{,}001L$, defecto angular a lo sumo $0{,}002$ radianes y defecto de coordenadas a lo sumo $0{,}003L$. Para $\|\widetilde{\mathbf y}\|\le4L$, encuentra una garantía de error espacial. ¿Qué parte de la cota cambia si se observa un objeto al doble de distancia?

**Solución.** La versión lineal de la proposición 8.16 da $e_r\le0{,}001L+0{,}003L+0{,}002(4L)=0{,}012L$. La tolerancia espacial debe ser al menos esa cota para quedar certificada por la información disponible. Al duplicar el límite de distancia a $8L$, sólo el término angular se duplica, y la cota pasa a $0{,}020L$. El cálculo muestra que calibrar el giro puede resultar decisivo para observaciones lejanas, incluso con el mismo defecto angular pequeño.

[]{#fispm-t1-c08-e0028}

**Ejercicio 8.28.** En un marco plano móvil se aproxima la velocidad fija por $\widetilde{\mathbf v}=\mathbf c'+Q\mathbf y'$, omitiendo el giro. Supón $|\omega|\le\Omega$ y $\|\mathbf y\|\le B$ en todo un intervalo. Acota el defecto de velocidad y el de una posición aproximada reconstruida integrando esa velocidad desde la posición inicial exacta. Indica qué no permite afirmar esta información sobre el defecto de aceleración.

**Solución.** proposición 8.12 da $\mathbf v-\widetilde{\mathbf v}=\omega QJ\mathbf y$, cuya norma es $|\omega|\|\mathbf y\|\le\Omega B$. Si $\widetilde{\mathbf r}(t_0)=\mathbf r(t_0)$ y se define $\widetilde{\mathbf r}'=\widetilde{\mathbf v}$, integrar el defecto produce $e_r(t_0+\tau)\le\Omega B\tau$. Para tolerancia $\varepsilon S$ y $\Omega B>0$, basta $H\le\varepsilon S/(\Omega B)$ dentro del dominio de las cotas.

El cálculo controla una posición reconstruida por integración; no declara que sea idéntica a una expresión obtenida simplemente congelando los ejes. Tampoco una cota de la función defecto controla su derivada: para acotar el defecto de aceleración se necesitan límites sobre $\omega'$, $\mathbf y'$ y los demás factores al derivar. Una función pequeña puede cambiar rápidamente. La reducción queda justificada sólo para las observables que efectivamente se acotaron.

Las nociones de error, resto y dominio certificado proceden de [capítulo 6](#fispm-c06-modelos-aproximaciones-escalas-y-linealizaciuxf3n), §§6, 8 y 14. Proposición 8.15 y proposición 8.16 construyen aquí las extensiones vectoriales y de marco necesarias.

[]{#reconstrucción-y-auditoría-de-una-historia-completa}

[]{#fispm-t1-c08-s14}

[]{#fpm-i-08-s14}

## 8.14. Reconstrucción y auditoría de una historia completa {#fispm-c08-reconstrucciuxf3n-y-auditoruxeda-de-una-historia-completa}

La descripción de un movimiento debe permitir pasar de los datos al evento sin cambiar inadvertidamente de marco, reloj o modelo. El capítulo ofrece tres representaciones con funciones diferentes: coordenadas cartesianas fijas, coordenadas polares ligadas a un centro y coordenadas cartesianas de un marco móvil. La elección depende de la pregunta; ninguna representación releva de conservar sus condiciones.

[]{#cómo-organizar-una-reconstrucción}

### 8.14.1. Cómo organizar una reconstrucción {#fispm-c08-cuxf3mo-organizar-una-reconstrucciuxf3n}

Primero se identifica qué se conoce. Una posición temporal completa permite derivar; una velocidad necesita una posición inicial para reconstruir; una aceleración necesita posición y velocidad iniciales. Una rapidez inicial sin dirección suele dejar una familia. Un punto objetivo puede seleccionar varias historias, dependiendo de si se fija también rapidez o tiempo.

Después se elige un marco en el que las hipótesis sean claras. Una aceleración constante en direcciones fijas no tiene por qué tener componentes constantes en ejes giratorios. Para transformar la historia se reconstruye primero la relación de posiciones. Proposición 8.11 y proposición 8.12 son consecuencias de esa relación, y sus términos se auditan comprobando qué factores dependen del tiempo.

Los eventos se resuelven en el dominio de la historia. Una raíz de una prolongación posterior al contacto con el suelo puede carecer de significado en el vuelo. Un cruce de imágenes no prueba un encuentro. Si se usa un marco común, proposición 8.14 permite comparar directamente las coordenadas móviles en un mismo instante; si se usan dos marcos distintos, primero hay que componer o transformar las posiciones.

Finalmente se interpreta la precisión. Una fórmula exacta del modelo puede omitir efectos físicos, y una reducción de esa fórmula puede añadir otro defecto. Proposición 8.15 controla la acumulación temporal de una discrepancia de aceleración; proposición 8.16 controla la transformación espacial de registros imperfectos. La tolerancia y el intervalo deben responder a la observable solicitada, sin mezclarse con una incertidumbre estadística que no se ha modelado.

[]{#fispm-t1-c08-mp0014}

**Principio metodológico 8.14 --- Cerrar el recorrido desde los datos hasta la observación.** Una historia reconstruida se devuelve a su pregunta: se verifican datos iniciales, aceleración o velocidad prescrita, representación, dimensiones, eventos admitidos y tolerancia. La interpretación final declara qué ha quedado determinado, qué sigue libre y qué premisas habría que revisar si el contraste falla.

[]{#ejercicios-de-integración}

### 8.14.2. Ejercicios de integración {#fispm-c08-ejercicios-de-integraciuxf3n}

[]{#fispm-t1-c08-e0029}

**Ejercicio 8.29.** En $0\le u\le2$, una cámara tiene origen normalizado $\mathbf C(u)=u e_x+u^2e_y$ y ejes giratorios de ángulo $\varphi(u)=u$. Un objeto se registra con coordenadas móviles $\mathbf Y(u)=(2-u)e_x+e_y$. Otro punto permanece fijo respecto de la cámara, con coordenadas $\mathbf Z=e_x+e_y$.

Reconstruye la posición, velocidad y aceleración del primer objeto en el marco fijo. Comprueba sus datos en $u=0$ y encuentra el encuentro con el punto fijo de la cámara, indicando la posición y ambas velocidades en ese evento. Explica si coincidir en posición obliga a compartir velocidad.

**Solución.** La relación fundamental es $\mathbf R=\mathbf C+Q_u\mathbf Y$, por lo que $$\mathbf R=u e_x+u^2e_y+Q_u((2-u)e_x+e_y).$$ La fórmula de la proposición 8.12, expresada en derivadas respecto de $u$, da $$\mathbf v=\frac LT\left[e_x+2u e_y+Q_u(-2e_x+(2-u)e_y)\right],$$ $$\mathbf a=\frac L{T^2}\left[2e_y+Q_u((u-2)e_x-3e_y)\right].$$ Dentro de $Q$, la velocidad procede de $\mathbf Y'+J\mathbf Y=-e_x+((2-u)e_y-e_x)$; la aceleración procede de $2J\mathbf Y'-\mathbf Y=-2e_y-(2-u)e_x-e_y$. Esta derivación conserva el término mixto y el radial.

En $u=0$, $\mathbf R=2e_x+e_y$, $\mathbf v=(L/T)(-e_x+2e_y)$ y $\mathbf a=(L/T^2)(-2e_x-e_y)$. La rapidez inicial es $\sqrt5L/T$, aunque la rapidez relativa de las coordenadas es $L/T$. El movimiento del marco contribuye a la diferencia.

Por proposición 8.14, el encuentro equivale a $\mathbf Y(u)=\mathbf Z$. La segunda componente ya coincide; la primera exige $2-u=1$, de modo que el único tiempo admitido es $u=1$, o $t=t_0+T$. La posición común es $$P_*=O+L\left[(1+\cos1-\sin1)e_x+(1+\sin1+\cos1)e_y\right].$$ La velocidad del primer objeto allí es $(L/T)(e_x+2e_y+Q_1(-2e_x+e_y))$. La del punto ligado a la cámara es $(L/T)(e_x+2e_y+Q_1(-e_x+e_y))$, porque su derivada de coordenadas es cero. La diferencia es $-(L/T)Q_1e_x$, no nula. El objeto pasa por ese punto de la cámara sin quedar unido a él. Un encuentro sólo iguala posiciones en el instante; no impone igualdad de las derivadas.

[]{#fispm-t1-c08-e0030}

**Ejercicio 8.30.** Un proyectil ideal parte de $(0,2L)$ con componentes iniciales $(3L/T,L/T)$ y $g=2L/T^2$. Se desea predecir el contacto con el suelo. La historia con el defecto tiene los mismos datos iniciales y aceleración $-ge_y+\boldsymbol\eta(t)$, continua, con $\|\boldsymbol\eta(t)\|\le0{,}02L/T^2$ para $0\le t\le3T$. Su posición se reconstruye de ese dato y se prolonga matemáticamente en el intervalo para localizar la primera llegada al suelo; la descripción física de vuelo termina en ese evento. Un análisis usa el instante ideal $2T$ como si fuera también el instante real de llegada y afirma que el error de alcance es a lo sumo $0{,}04L$.

Encuentra la predicción ideal, comprueba qué garantiza realmente proposición 8.15 en $2T$ y explica la falla del análisis. Después certifica una ventana para el primer contacto real y una cota para el error de su abscisa, usando únicamente la información suministrada. Escribe una conclusión que distinga posición en un tiempo fijado de posición en un evento.

**Solución.** La historia ideal tiene $X_0(u)=3u$ y $Y_0(u)=2+u-u^2$. Su primer contacto positivo es $u=2$ y la abscisa es $6L$. Proposición 8.15, con $A=0{,}02L/T^2$ y datos iniciales coincidentes, da $$\|\mathbf r(t)-\mathbf r_0(t)\|\le0{,}01Lu^2, \qquad \|\mathbf v(t)-\mathbf v_0(t)\|\le0{,}02(L/T)u.$$ En $u=2$, el defecto de posición no supera $0{,}04L$. Ésa es una comparación a tiempo fijo. La altura real puede ser positiva o negativa en ese instante; no se ha probado que el evento real ocurra allí. La diferencia de alcance incluye también el movimiento horizontal durante el defecto de tiempo de llegada.

Para controlar ese evento, usamos $|Y-Y_0|\le0{,}01u^2$. La altura real satisface $$2+u-1{,}01u^2\le Y(u)\le2+u-0{,}99u^2.$$ Las raíces positivas de los dos extremos son $$u_- =\frac{1+\sqrt{9{,}08}}{2{,}02}, \qquad u_+ =\frac{1+\sqrt{8{,}92}}{1{,}98}.$$ Para $0\le u<u_-$, el extremo inferior es positivo, así que no hay contacto. En $u_+$, el extremo superior es cero, por lo que $Y(u_+)\le0$. La continuidad y la altura inicial positiva garantizan una raíz en $[u_-,u_+]$, y el conjunto de raíces de ese segmento compacto tiene un menor elemento. Es el primer contacto: cualquier raíz anterior quedaba excluida por la cota inferior. La ventana está dentro de $[0,3]$.

Podemos usar un intervalo algo más amplio con números sencillos, sin depender de redondear raíces: en $u=1{,}98$ el extremo inferior vale $0{,}020396>0$ y es positivo en todo $[0,1{,}98]$, por concavidad y positividad en ambos extremos; en $u=2{,}02$ el extremo superior vale $-0{,}019596<0$. Por tanto, $1{,}98<u_f<2{,}02$. Cerca de esa ventana, la velocidad vertical real es negativa, pues su componente normalizada no supera $1-2u+0{,}02u=1-1{,}98u<0$. El contacto es único dentro de la ventana.

En el evento real, $|X(u_f)-3u_f|\le0{,}01u_f^2$ y $|u_f-2|<0{,}02$. La desigualdad triangular proporciona $$|x_f-6L| \le L\bigl(0{,}01u_f^2+3|u_f-2|\bigr) <L\bigl(0{,}01(2{,}02)^2+0{,}06\bigr) =0{,}100804L.$$ Si se exige error de alcance no mayor que $0{,}1L$, esa cota sencilla todavía no lo certifica. Podemos afinarla con la misma información: el extremo inferior en $u=1{,}986$ vale $0{,}00236204>0$ y el extremo superior en $u=2{,}014$ vale $-0{,}00163404<0$. Por el mismo argumento, $1{,}986<u_f<2{,}014$. Entonces $$|x_f-6L|<L\bigl(0{,}01(2{,}014)^2+3(0{,}014)\bigr) =0{,}08256196L<0{,}1L.$$ La tolerancia queda certificada, junto con la ventana temporal más estrecha. La cota $0{,}04L$ continúa siendo válida para comparar las dos posiciones en el tiempo ideal; la cota de alcance se obtuvo controlando además el evento real. Mejorar una garantía suficiente no requiere suponer que el error verdadero alcance ninguno de esos límites.

[]{#lo-que-queda-preparado-para-la-dinámica}

### 8.14.3. Lo que queda preparado para la dinámica {#fispm-c08-lo-que-queda-preparado-para-la-dinuxe1mica}

La cinemática ha establecido cómo describir una historia, reconstruirla de datos prescritos, transformarla entre marcos y controlar determinadas reducciones. Los términos de aceleración que aparecen en una base móvil ya tienen una explicación geométrica. La pregunta siguiente será qué interacciones y principios físicos determinan la aceleración, y en qué marcos se formulan esas leyes. Esa nueva tarea necesita las distinciones construidas aquí, pero no estaba contenida en derivar dos veces una posición.

[]{#fispm-c08-notas-y-referencias-del-capuxedtulo label="fispm-c08-notas-y-referencias-del-capuxedtulo"}

[^1]: R. Shankar, *Fundamentals of Physics I*, Expanded Edition, Yale University Press, 2019, cap. 2, §§2.2--2.5, pp. 16--29. Control de representaciones vectoriales y derivadas en base fija; no se reproducen sus ejemplos.

[^2]: D. Kleppner y R. Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, cap. 1, §1.7, pp. 19--21. Se usa la edición concreta disponible, sin atribuirle otra numeración de edición.

[^3]: Shankar, obra citada, cap. 2, §2.6, pp. 29--32; Kleppner--Kolenkow, obra citada, cap. 1, §1.8, pp. 24--27. Control del cambio de dirección y de la derivación vectorial.

[^4]: Shankar, obra citada, cap. 2, §2.7, pp. 32--35. Control del modelo parabólico y del alcance a igual altura; las hipótesis y restricciones se explicitan en el desarrollo propio.

[^5]: Kleppner--Kolenkow, obra citada, cap. 1, §1.9, pp. 27--33. Control de base polar y derivadas de sus vectores unitarios.

[^6]: Kleppner--Kolenkow, obra citada, cap. 1, §1.9, pp. 33--38. Control de componentes polares de velocidad y aceleración. No se introduce su tratamiento dinámico de fuerzas en marcos giratorios.

[^7]: R. Shankar, *Fundamentals of Physics I*, Expanded Edition, Yale University Press, 2019, cap. 2, §2.6, pp. 29--32; D. Kleppner y R. Kolenkow, *An Introduction to Mechanics*, copia Cambridge University Press, 2010, §1.9. Control de la cinemática circular; se reconstruyen los resultados con la proposición 8.9.

[^8]: Kleppner--Kolenkow, obra citada, §8.2, pp. 340--343. Se extraen la relación de posiciones, sus derivadas y la hipótesis de tiempo común. Los argumentos sobre fuerzas e inercialidad de la fuente no se incorporan en este capítulo.

[^9]: Kleppner--Kolenkow, obra citada, §8.5, pp. 356--359, pasajes sobre derivadas temporales y aceleración relativa a ejes giratorios. Se usan como control cinemático del caso uniforme; la deducción planar con giro variable es propia.
