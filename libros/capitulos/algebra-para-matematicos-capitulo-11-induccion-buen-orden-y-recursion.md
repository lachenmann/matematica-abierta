---
{
  "title": "Inducción, buen orden y recursión",
  "description": "Capítulo 11 del Tomo I de Álgebra para matemáticos, con 104 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0186",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C11",
  "editorial-id": "MA-BCH-APM-01-011",
  "status": "published",
  "date-created": "2026-10-09",
  "date-modified": "2026-10-09",
  "areas": [
    "algebra",
    "fundamentos"
  ],
  "level": "fundamental",
  "topics": [
    "numeros-complejos-y-el-horizonte-de-las-ecuaciones"
  ],
  "prerequisites": [
    "MA-BCH-0185"
  ],
  "related": [
    "MA-BOK-0006"
  ],
  "provenance": {
    "type": "original",
    "sources": []
  },
  "license": "GFDL-1.3-or-later"
}
---

C10 enseñó a leer una afirmación, elegir una estrategia y construir una prueba. Sin embargo, existe una situación que merece una herramienta propia. Queremos demostrar no una proposición aislada, sino una familia

$$
P(0),P(1),P(2),\ldots
$$

o, más generalmente,

$$
P(n_0),P(n_0+1),P(n_0+2),\ldots
$$

para todos los índices de una cola de los naturales.

Comprobar cien, mil o un millón de casos sigue dejando infinitos casos sin tratar. La inducción matemática resuelve el problema usando la estructura sucesiva de $\mathbb N$.

> **La inducción no sustituye una prueba por una metáfora de dominós. Convierte una familia infinita de objetivos en un caso inicial y una implicación uniforme.**

Este capítulo conecta esa idea con el principio del buen orden y con las definiciones recursivas.

En este capítulo usamos $\mathbb N=\{0,1,2,\ldots\}$. Los rangos que empiezan en $1$ o en otro índice se declaran expresamente; incluir $0$ en el conjunto de índices no obliga a incluirlo en cada teorema.

***
## 11.1. El problema de demostrar infinitos casos {#apm-c11-s01}

Supongamos que una propiedad $P(n)$ está formulada para cada natural $n$. Verificar

$$
P(1),P(2),\ldots,P(1000)
$$

puede aportar evidencia, pero no prueba

$$
\forall n\ge1\;P(n).
$$

La dificultad es estructural: ningún número finito de verificaciones aisladas cubre una familia infinita.

Los naturales, sin embargo, están organizados por un sucesor. Si podemos demostrar un primer caso y mostrar que cada caso verdadero obliga al siguiente, la familia completa queda enlazada.

***
## 11.2. Principio de inducción matemática {#apm-c11-s02}

Sea $n_0\in\mathbb N$ y sea $P(n)$ una proposición definida para todos los enteros $n\ge n_0$.

El principio de inducción afirma que, si:

1. $P(n_0)$ es verdadera;
2. para todo $k\ge n_0$, la implicación
   $$
   P(k)\Rightarrow P(k+1)
   $$
   es verdadera,

entonces

$$
P(n)
$$

es verdadera para todo $n\ge n_0$.

La primera parte es el **caso base**. La segunda es el **paso inductivo**.

El principio no dice que $P(k)$ sea verdadera porque la supongamos. Dice que, dentro de una prueba condicional, podemos asumir $P(k)$ y demostrar que esa suposición fuerza $P(k+1)$.

***
## 11.3. Caso base e hipótesis inductiva {#apm-c11-s03}

Una prueba inductiva debe declarar con precisión su rango.

Si queremos probar $P(n)$ para todo $n\ge3$, el caso base natural es $P(3)$, no $P(1)$.

Para el paso inductivo:

> Sea $k\ge3$ arbitrario y supongamos que $P(k)$ es verdadera.

Esa suposición recibe el nombre de **hipótesis inductiva**.

Su alcance es local: se usa para demostrar $P(k+1)$. No autoriza a afirmar que todos los casos sean verdaderos antes de completar la prueba.

***
### Escribir la hipótesis y la meta antes de calcular

La expresión «por hipótesis inductiva» debe referirse a una afirmación escrita, con su índice y su rango. Sea, por ejemplo, $a_3=4$ y $a_{n+1}=a_n+2n-1$ para $n\ge3$. Queremos probar $P(n):a_n=(n-1)^2$ para $n\ge3$.

| Papel | Afirmación disponible o pendiente |
|---|---|
| Base | $a_3=4=(3-1)^2$ |
| Índice del paso | $k\ge3$, arbitrario |
| Hipótesis utilizable | $a_k=(k-1)^2$ |
| Meta | $a_{k+1}=k^2$ |
| Regla de construcción | $a_{k+1}=a_k+2k-1$ |

La cadena es $a_{k+1}=a_k+2k-1=(k-1)^2+2k-1=k^2$. La primera igualdad usa la definición recursiva; la segunda, la hipótesis; la tercera, álgebra. Ninguna usa la meta como dato. El paso y la base cubren exactamente la cola desde $3$.

**Control.** Un borrador sustituye $a_{k+1}=k^2$ al comenzar el paso y termina con la misma igualdad. ¿Qué debe cambiar?

**Solución.** Se ha asumido la meta. Hay que comenzar con la regla que define $a_{k+1}$ y sustituir sólo la expresión de $a_k$ que permite la hipótesis. Si confundes dato y objetivo, vuelve a C10, anatomía de una implicación y variables arbitrarias; después reconstruye la tabla para un índice inicial distinto.

## 11.4. Anatomía del paso inductivo {#apm-c11-s04}

El paso inductivo es una prueba ordinaria de implicación:

$$
P(k)\Rightarrow P(k+1).
$$

Por eso las técnicas de C10 siguen vigentes.

En una identidad, suele ser útil escribir la expresión correspondiente a $k+1$ y separar la parte conocida para $k$. En una desigualdad, hay que comprobar que las operaciones preservan el sentido correcto.

Un indicio de problema es escribir “por hipótesis inductiva” sin que la hipótesis aparezca realmente en el razonamiento.

También puede ocurrir que $P(k+1)$ se demuestre sin usar $P(k)$. Eso no invalida la prueba, pero indica que la inducción quizá no era necesaria.

***
### Fortalecer la afirmación para sostener el paso

Una propiedad verdadera puede aportar poca información para el argumento elegido. Considera $a_0=0$ y $a_{n+1}=(a_n+1)/(a_n+2)$. El objetivo $a_n\le1$ por sí solo no garantiza que la regla preserve esa cota: una entrada $a=-3$ cumple $a\le1$, pero produce $2$. Además, la entrada $a=-2$ hace nulo el denominador.

Probamos la afirmación más informativa $Q(n):0\le a_n\le1$. La base es $a_0=0$. Si $0\le a_k\le1$, el denominador $a_k+2$ es positivo, el numerador también y
$$
0<\frac{a_k+1}{a_k+2}<1,
$$
porque $a_k+1<a_k+2$. Así el nuevo término existe y pertenece al mismo intervalo. Por inducción, $Q(n)$ y por tanto el objetivo original valen para todos los índices.

Fortalecer no consiste en añadir la conclusión que falta como una suposición gratuita: la nueva información debe verificarse en la base y preservarse en el paso.

**Control.** ¿Los números $-3$ y $-2$ refutan el resultado sobre la sucesión que empieza en $0$?

**Solución.** No pertenecen a la órbita construida. Refutan la suficiencia de la sola condición $a\le1$ para justificar el paso propuesto. La prueba fortalecida excluye esas entradas antes de dividir. Para revisar signos y transformaciones condicionadas, vuelve a C3; para separar contraejemplo a un resultado y fallo de un argumento, vuelve a C10.

## 11.5. Cambiar el índice inicial {#apm-c11-s05}

No toda inducción comienza en $0$ o $1$.

Podemos demostrar propiedades para:

$$
n\ge2,\qquad n\ge5,\qquad n\ge n_0.
$$

La cadena que genera la inducción comienza exactamente donde se verifica el caso base.

Si el paso inductivo sólo es válido para $k\ge4$, un caso base en $n=1$ no basta para cubrir $n=2,3,4$.

Este detalle será esencial al diagnosticar pruebas defectuosas.

Si un problema fija un inicio entero negativo, se puede usar $m=n-n_0\ge0$ y $Q(m)=P(m+n_0)$. La base se convierte en $Q(0)$ y el paso conserva el incremento de uno. Esta reindexación extiende la misma herramienta a cualquier cola de los enteros sin aplicar buen orden directamente a un conjunto que incluya índices negativos.

***
## 11.6. Identidades algebraicas por inducción {#apm-c11-s06}

Consideremos

$$
1+2+\cdots+n=\frac{n(n+1)}{2}.
$$

El caso base $n=1$ es inmediato.

Para el paso, suponemos

$$
1+2+\cdots+k=\frac{k(k+1)}{2}.
$$

Entonces

$$
\begin{aligned}
1+2+\cdots+k+(k+1)
&=\frac{k(k+1)}{2}+(k+1)\\
&=(k+1)\left(\frac{k}{2}+1\right)\\
&=\frac{(k+1)(k+2)}{2}.
\end{aligned}
$$

La expresión final es precisamente la fórmula con $n=k+1$.

Aquí la inducción enseña una técnica de transformación. C12 estudiará después las sumas finitas de manera sistemática.

***
## 11.7. Desigualdades por inducción {#apm-c11-s07}

Las desigualdades requieren atención adicional.

Por ejemplo,

$$
2^n\ge n+1
$$

para todo $n\ge0$.

Base: $2^0=1\ge1$.

Hipótesis:

$$
2^k\ge k+1.
$$

Entonces

$$
2^{k+1}=2\cdot2^k\ge2(k+1)=k+2+k\ge k+2.
$$

El paso usa que los factores multiplicadores son no negativos y que $k\ge0$.

La inducción no permite multiplicar o dividir desigualdades sin controlar signos.

***
## 11.8. Más de un caso base {#apm-c11-s08}

Supongamos una sucesión definida por

$$
a_{n+2}=a_{n+1}+a_n.
$$

Una propiedad de $a_{n+2}$ puede depender simultáneamente de los dos términos anteriores. Entonces una prueba puede necesitar dos casos base.

El número de casos base no es una convención estética. Debe ser suficiente para poner en marcha la regla que conecta los índices.

Recurrencias de orden dos ofrecen el laboratorio natural para esta situación.

***
### Las bases se leen en las dependencias

Supón que una prueba permite inferir $P(n+3)$ a partir de $P(n)$ y $P(n+1)$, para $n\ge0$. Sus primeras dependencias son:

| Meta | Datos necesarios |
|---|---|
| $P(3)$ | $P(0),P(1)$ |
| $P(4)$ | $P(1),P(2)$ |
| $P(5)$ | $P(2),P(3)$ |
| $P(6)$ | $P(3),P(4)$ |

Aunque no aparezca $P(n+2)$ en la regla, hacen falta $P(0),P(1),P(2)$ para cubrir todos los índices con este mecanismo. Con esas bases, una hipótesis fuerte hasta $k\ge2$ da los datos $P(k-2)$ y $P(k-1)$ y produce $P(k+1)$. Los índices utilizados están dentro del rango y son anteriores a la meta.

**Control.** ¿Bastan $P(0)$ y $P(1)$ junto con esa regla?

**Solución.** No. La propiedad «$n\neq2$» cumple esas dos bases y la regla: toda conclusión de la regla tiene índice al menos $3$ y es verdadera. Sin embargo, falla $P(2)$. Este modelo demuestra que la base ausente no es una formalidad. Para recuperar la lógica del argumento, vuelve a C4, implicaciones con antecedente falso, y C10, contraejemplos; luego escribe las primeras dependencias de una regla nueva antes de escoger bases.

## 11.9. Inducción fuerte {#apm-c11-s09}

En la inducción fuerte, al demostrar $P(k+1)$ se puede suponer

$$
P(n_0),P(n_0+1),\ldots,P(k).
$$

La hipótesis es más amplia, pero la conclusión es la misma: $P(n)$ vale para todo $n\ge n_0$.

La inducción fuerte es especialmente natural cuando el nuevo caso se reduce a **algún** caso anterior, pero no sabemos de antemano que sea exactamente $k$.

“Fuerte” no significa que demuestre resultados que la inducción ordinaria no pueda demostrar. Significa que el argumento puede usar más información inductiva de forma directa.

***
## 11.10. Ordinaria y fuerte: comparación {#apm-c11-s10}

La inducción ordinaria usa el caso inmediatamente anterior. La fuerte permite utilizar todos los anteriores.

Conceptualmente son equivalentes sobre $\mathbb N$. Una forma puede simular a la otra.

Sin embargo, la elección importa para la claridad. Si un objeto de tamaño $k+1$ se descompone en partes de tamaños arbitrariamente menores, la inducción fuerte suele reflejar mejor la estructura real del argumento.

La estrategia debe seguir al problema, no al hábito.

***
### Simular una hipótesis fuerte mediante una afirmación acumulada

Supón que tenemos $P(n_0)$ y un paso que, para cada $k\ge n_0$, deduce $P(k+1)$ de todos los casos $P(j)$ con $n_0\le j\le k$. Definimos
$$
Q(n):\quad\forall j\;(n_0\le j\le n\Rightarrow P(j)),\qquad n\ge n_0.
$$
Podemos probar $Q$ por inducción ordinaria. La base $Q(n_0)$ equivale a $P(n_0)$. En el paso, $Q(k)$ proporciona todas las afirmaciones exigidas por el paso fuerte, de donde obtenemos $P(k+1)$. Para verificar $Q(k+1)$, fija $j$ con $n_0\le j\le k+1$: si $j\le k$, usamos $Q(k)$; si $j=k+1$, usamos la afirmación recién demostrada. Así la información anterior se conserva y se agrega el nuevo caso.

Una vez probados todos los $Q(n)$, fijamos $n\ge n_0$ y tomamos $j=n$ para concluir $P(n)$. La hipótesis ordinaria es una sola proposición, pero su contenido es acumulativo. No se ha supuesto la conclusión para todos los índices.

**Control.** ¿Podemos reemplazar $Q(n)$ por «$P(n_0)$ y $P(n)$» en cualquier prueba fuerte?

**Solución.** No: esa pareja no informa sobre los índices estrictamente intermedios. Por ejemplo, en un paso que necesite $P(k-1)$ con $k\ge n_0+2$, los datos $P(n_0),P(k)$ no garantizan esa afirmación. Hace falta acumular las dependencias efectivamente utilizadas. Si cuesta reconocer el alcance de $Q$, vuelve a C6, cuantificación acotada, y escribe qué valores de $j$ autoriza usar en cada paso.

## 11.11. Principio del buen orden {#apm-c11-s11}

El **principio del buen orden** afirma:

> Todo subconjunto no vacío de $\mathbb N$ tiene un elemento mínimo.

Este principio permite construir pruebas de otra forma.

Si queremos demostrar que todos los naturales de cierto rango satisfacen $P(n)$, podemos suponer lo contrario. Entonces el conjunto de contraejemplos es no vacío y posee un mínimo $m$.

La minimalidad de $m$ suele implicar que todos los índices anteriores relevantes sí satisfacen la propiedad. Esa información permite construir una contradicción.

***
## 11.12. Pruebas por menor contraejemplo {#apm-c11-s12}

El esquema es:

```text
SUPONER QUE HAY CONTRAEJEMPLOS
        ↓
FORMAR EL CONJUNTO C DE CONTRAEJEMPLOS
        ↓
TOMAR m = min C
        ↓
USAR QUE LOS ÍNDICES MENORES NO ESTÁN EN C
        ↓
CONTRADICCIÓN
```

Este método es, en muchos problemas, la traducción natural de una inducción fuerte.

La elección del menor contraejemplo sólo es legítima después de justificar que el conjunto de contraejemplos es no vacío y está contenido en $\mathbb N$.

***
## 11.13. Inducción y buen orden {#apm-c11-s13}

Inducción y buen orden expresan dos caras de la misma estructura.

Para ver cómo el buen orden conduce a la inducción, supongamos que se verifican el caso base y el paso inductivo, pero que existe algún contraejemplo. El conjunto de contraejemplos tiene un mínimo $m$.

Como el caso base es verdadero, $m>n_0$. Entonces $m-1\ge n_0$. Por minimalidad, $P(m-1)$ es verdadera. El paso inductivo obliga a $P(m)$, contradicción.

Para la dirección inversa, supongamos válido el principio de inducción y sea $S\subseteq\mathbb N$ no vacío. Supongamos, buscando contradicción, que $S$ no tiene mínimo. Probamos por inducción

$$
Q(n):\quad S\cap\{0,1,\ldots,n\}=\varnothing.
$$

La base vale: si $0\in S$, sería su mínimo, contradiciendo la suposición. Si $Q(k)$ vale y $k+1\in S$, ningún elemento de $S$ sería menor que $k+1$, de modo que éste sería mínimo. Por tanto $k+1\notin S$ y vale $Q(k+1)$.

La inducción da $Q(n)$ para todo natural $n$. Pero, como $S$ no es vacío, existe $s\in S$; entonces $Q(s)$ lo excluye de $S$, contradicción. Así $S$ tiene mínimo. Ambas direcciones de la equivalencia quedan justificadas; el ejercicio 102 ofrece otra prueba de esta dirección usando segmentos finitos.

***
## 11.14. Definiciones recursivas {#apm-c11-s14}

Una definición recursiva da:

1. uno o más valores iniciales;
2. una regla para producir nuevos valores desde valores anteriores.

Por ejemplo,

$$
a_0=2,\qquad a_{n+1}=3a_n+1.
$$

Esto no es todavía una fórmula cerrada para $a_n$. Es un procedimiento que determina los términos sucesivamente:

$$
a_0=2,\quad a_1=7,\quad a_2=22,\ldots
$$

La recursión define; una fórmula cerrada, si existe, es un teorema adicional que debe demostrarse.

***
### Definir, conjeturar y demostrar son tres tareas

Para una regla $a_{n+1}=F(a_n)$, dar $a_0\in D$ y una función total $F:D\to D$ asegura que cada etapa tiene una única salida admisible. La construcción recursiva determina la sucesión; si dos sucesiones cumplen los mismos datos, la inducción demuestra su igualdad: coinciden en $0$ y la igualdad de entradas produce igualdad de salidas en cada paso. Cuando una regla contiene divisiones, hay que justificar que nunca se llega a una entrada prohibida.

Calcular algunos términos puede sugerir una fórmula, pero esa fórmula exige base y paso. Para $a_0=2$ y $a_{n+1}=a_n/(1+a_n)$, los términos $2,2/3,2/5$ sugieren $a_n=2/(2n+1)$. La base coincide. Si la fórmula vale en $k$, su valor es positivo y
$$
a_{k+1}=\frac{2/(2k+1)}{1+2/(2k+1)}=\frac2{2k+3}.
$$
El denominador original es positivo y el resultado es la fórmula en $k+1$. La prueba justifica al mismo tiempo la existencia de todos los términos y la descripción propuesta.

**Control.** ¿La regla $b_0=1$, $b_{n+1}=1/(b_n-1)$ define una sucesión real para todos los índices?

**Solución.** No: ya $b_1$ exigiría dividir por cero. Una notación recursiva no garantiza por sí misma que el procedimiento pueda ejecutarse. Recupera en C9 los requisitos de una función y en C3 las restricciones de la división. Después distingue qué se demostró sobre la órbita y qué sólo se observó en una lista finita.

## 11.15. Probar propiedades de objetos recursivos {#apm-c11-s15}

La inducción es la herramienta natural para estudiar objetos definidos recursivamente.

Si

$$
a_0=1,\qquad a_{n+1}=2a_n+1,
$$

podemos conjeturar

$$
a_n=2^{n+1}-1.
$$

Base:

$$
a_0=1=2^1-1.
$$

Paso: si $a_k=2^{k+1}-1$, entonces

$$
a_{k+1}=2(2^{k+1}-1)+1=2^{k+2}-1.
$$

Así la fórmula queda demostrada para todo $n\ge0$.

> **Recursión construye; inducción verifica.**

***
## 11.16. Elegir entre inducción, buen orden y recursión {#apm-c11-s16}

Antes de empezar, conviene preguntar:

1. ¿la afirmación está indexada por naturales?;
2. ¿cuál es el primer índice?;
3. ¿qué debe ser exactamente $P(n)$?;
4. ¿el caso $k+1$ depende naturalmente de $k$?;
5. ¿depende de varios casos anteriores?;
6. ¿sería más limpio suponer un menor contraejemplo?;
7. ¿el objeto está definido recursivamente?;
8. ¿cuántos casos base hacen falta?;
9. ¿la hipótesis inductiva se usa realmente?;
10. ¿el paso cubre todos los índices posteriores?

C11 termina en el punto donde comienza una nueva necesidad: manipular sistemáticamente sumas y productos finitos. Ése será el trabajo de C12.

***
# Ejercicios

Los ejercicios son originales para *Álgebra para matemáticos* y se calibran con el corpus rector del capítulo. Los identificadores editoriales permanecen en comentarios internos no renderizados.

## A. Reconocer estructura inductiva


**1.** **Nivel A.** Para la afirmación $1+2+\cdots+n=n(n+1)/2$, identifica una elección natural de $P(n)$ y el índice inicial.


**2.** **Nivel A.** En «$2^n\ge n+1$ para todo $n\ge0$», ¿cuál debe ser el caso base?


**3.** **Nivel B.** Explica por qué comprobar $P(1),\ldots,P(100)$ no demuestra $\forall n\ge1\,P(n)$.


**4.** **Nivel B.** Si una afirmación se quiere demostrar sólo para $n\ge5$, ¿es obligatorio comprobar $P(1)$?


**5.** **Nivel B.** ¿Qué debe demostrar exactamente el paso inductivo de una inducción ordinaria iniciada en $n_0$?


**6.** **Nivel C.** Una prueba verifica $P(1)$ y demuestra $P(k)\Rightarrow P(k+2)$. ¿Qué índices quedan cubiertos automáticamente?

## B. Caso base y paso inductivo


**7.** **Nivel A.** Verifica el caso base de $1+3+\cdots+(2n-1)=n^2$ para $n=1$.


**8.** **Nivel B.** Suponiendo $1+3+\cdots+(2k-1)=k^2$, calcula la suma hasta el siguiente impar y obtén la fórmula para $k+1$.


**9.** **Nivel B.** En una prueba inductiva, ¿por qué es legítimo suponer $P(k)$ durante el paso?


**10.** **Nivel B.** Diagnostica: «Supongamos que $P(k+1)$ es verdadera. Entonces... por tanto $P(k+1)$».


**11.** **Nivel C.** Demuestra por inducción que $3^n\ge1+2n$ para todo $n\ge0$.


**12.** **Nivel C.** Demuestra por inducción que $5^n-1$ es múltiplo de $4$ para todo $n\ge0$.


**13.** **Nivel C.** Una prueba del paso $P(k)\Rightarrow P(k+1)$ no usa $P(k)$. ¿Es necesariamente incorrecta?


**14.** **Nivel D.** Explica por qué un caso base correcto no compensa un paso inductivo que sólo se ha demostrado para algunos valores de $k$.

## C. Identidades elementales


**15.** **Nivel B.** Demuestra por inducción $1+3+\cdots+(2n-1)=n^2$ para $n\ge1$.


**16.** **Nivel B.** Demuestra por inducción $2+4+\cdots+2n=n(n+1)$.


**17.** **Nivel C.** Demuestra $1+2+\cdots+n=n(n+1)/2$ por inducción.


**18.** **Nivel C.** Demuestra $1+2+\cdots+n+(n+1)=(n+1)(n+2)/2$ partiendo de la hipótesis inductiva para $n$.


**19.** **Nivel C.** Demuestra por inducción $1+2+\cdots+n+(n+1)+(n+2)=(n+2)(n+3)/2$ si ya conoces la fórmula hasta $n$.


**20.** **Nivel C.** Demuestra por inducción que $1+2+\cdots+(n-1)=n(n-1)/2$ para $n\ge1$.


**21.** **Nivel D.** Demuestra por inducción $1\cdot2+2\cdot3+\cdots+n(n+1)=n(n+1)(n+2)/3$.


**22.** **Nivel D.** Demuestra por inducción $1^2+3^2+\cdots+(2n-1)^2=n(4n^2-1)/3$.

## D. Desigualdades


**23.** **Nivel B.** Demuestra $2^n\ge n+1$ para $n\ge0$.


**24.** **Nivel C.** Demuestra $3^n\ge n^2$ para todo $n\ge1$; separa explícitamente los casos iniciales que necesita el paso.


**25.** **Nivel C.** Demuestra $n!\ge2^{n-1}$ para $n\ge1$.


**26.** **Nivel C.** Demuestra $1+n\le2^n$ para $n\ge0$.


**27.** **Nivel D.** Demuestra $n^2\le2^n$ para todo $n\ge4$.


**28.** **Nivel D.** Explica por qué al multiplicar una desigualdad inductiva por una cantidad cuyo signo no se conoce hay que detenerse.

## E. Índice inicial y reindexación


**29.** **Nivel B.** Demuestra por inducción que $2^n>n$ para todo $n\ge1$.


**30.** **Nivel C.** Demuestra $n^2\ge2n+3$ para todo $n\ge3$.


**31.** **Nivel C.** Una prueba pretende establecer $2^n\ge n^2$ para $n\ge4$ pero usa caso base $n=1$. ¿Qué debe corregirse?


**32.** **Nivel C.** Reindexa una afirmación $P(n)$ válida para $n\ge5$ mediante $m=n-5$.


**33.** **Nivel D.** Demuestra que $2^n\ge n^2$ para $n=4$ y para todo $n\ge4$ usando el paso del ejercicio 27.


**34.** **Nivel D.** Explica por qué el teorema «si base en $n_0$ y paso para $k\ge n_0+2$» deja un hueco.

## F. Varios casos base y recurrencias


**35.** **Nivel B.** Sea $a_0=1$, $a_1=1$ y $a_{n+2}=a_{n+1}+a_n$. Calcula $a_2,a_3,a_4$.


**36.** **Nivel C.** Explica por qué una propiedad de la sucesión anterior suele requerir dos casos base.


**37.** **Nivel C.** Para $a_0=2$, $a_1=3$, $a_{n+2}=3a_{n+1}-2a_n$, demuestra que $a_n=2^n+1$.


**38.** **Nivel C.** Sea $b_0=0$, $b_1=1$, $b_{n+2}=b_{n+1}+2b_n$. Demuestra que $b_n\ge0$ para todo $n$.


**39.** **Nivel D.** En una recurrencia de orden dos, ¿basta suponer sólo $P(k+1)$ para demostrar $P(k+2)$?


**40.** **Nivel D.** Da un ejemplo de una propiedad cuyo paso pueda usar dos casos consecutivos.

## G. Inducción fuerte


**41.** **Nivel C.** Formula el paso inductivo fuerte para una propiedad $P(n)$ iniciada en $n=2$.


**42.** **Nivel C.** Explica por qué la inducción fuerte no produce una conclusión más fuerte que la ordinaria.


**43.** **Nivel C.** Demuestra por inducción fuerte que todo entero $n\ge2$ puede escribirse como suma de términos iguales a $2$ o $3$.


**44.** **Nivel D.** Demuestra que todo entero $n\ge8$ puede escribirse como $3a+5b$ con $a,b\in\mathbb N\cup\{0\}$.


**45.** **Nivel D.** ¿Por qué el ejercicio anterior necesita tres casos base si el paso reduce $n$ en $3$?


**46.** **Nivel D.** Demuestra por inducción fuerte que una sucesión definida por $a_0=1$, $a_1=2$, $a_n=a_{n-1}+a_{n-2}$ satisface $a_n\le2^n$ para $n\ge1$.


**47.** **Nivel E.** Supón que todos los objetos de tamaño $1$ poseen $P$, que cada objeto de tamaño $n\ge2$ puede descomponerse en dos objetos de tamaños positivos menores que $n$, y que $P$ se preserva al combinar dos objetos que la poseen. Demuestra mediante inducción fuerte que todos los objetos de tamaño positivo poseen $P$.


**48.** **Nivel E.** Convierte conceptualmente una prueba por inducción fuerte en una prueba ordinaria definiendo $Q(n)=P(n_0)\land\cdots\land P(n)$.

## H. Buen orden


**49.** **Nivel B.** Enuncia el principio del buen orden para $\mathbb N$.


**50.** **Nivel C.** ¿Qué debe comprobarse antes de escribir «sea $m$ el menor contraejemplo»?


**51.** **Nivel C.** Usa menor contraejemplo para demostrar que $2^n\ge n+1$ para todo $n\ge0$.


**52.** **Nivel D.** Usa buen orden para demostrar que todo $n\ge8$ puede escribirse como $3a+5b$.


**53.** **Nivel D.** Explica por qué el método del menor contraejemplo se parece a la inducción fuerte.


**54.** **Nivel E.** Demuestra, usando buen orden, que si $S\subseteq\mathbb N$ es no vacío y cerrado bajo «si $n\in S$, entonces $n+1\in S$», y contiene $0$, entonces $S=\mathbb N$.

## I. Comparación de principios


**55.** **Nivel C.** Resume cómo el buen orden demuestra el principio de inducción.


**56.** **Nivel D.** ¿Qué información proporciona un menor contraejemplo $m$ que se corresponde con la hipótesis fuerte?


**57.** **Nivel D.** Explica cuándo preferirías buen orden en lugar de escribir una inducción fuerte explícita.


**58.** **Nivel E.** Explica por qué la equivalencia entre inducción y buen orden no significa que todas las pruebas tengan la misma claridad en ambos formatos.

## J. Definiciones recursivas


**59.** **Nivel A.** Para $a_0=2$, $a_{n+1}=3a_n+1$, calcula $a_1,a_2,a_3$.


**60.** **Nivel B.** Explica la diferencia entre una definición recursiva y una fórmula cerrada.


**61.** **Nivel B.** Define recursivamente la sucesión constante $a_n=5$.


**62.** **Nivel C.** Define recursivamente $a_n=2n+1$.


**63.** **Nivel C.** Una recurrencia $a_{n+2}=a_{n+1}+a_n$ sin valores iniciales, ¿determina una única sucesión?


**64.** **Nivel D.** Si $a_0=c$ y $a_{n+1}=F(a_n)$, explica por qué la regla determina sucesivamente a lo sumo una secuencia de valores.

## K. Propiedades de objetos recursivos


**65.** **Nivel B.** Para $a_0=1$, $a_{n+1}=2a_n+1$, demuestra $a_n=2^{n+1}-1$.


**66.** **Nivel C.** Para $b_0=2$, $b_{n+1}=b_n+3$, demuestra $b_n=2+3n$.


**67.** **Nivel C.** Para $c_0=1$, $c_{n+1}=c_n+2n+1$, demuestra $c_n=n^2+1$.


**68.** **Nivel C.** Si $a_0>0$ y $a_{n+1}=a_n+1/a_n$, demuestra $a_n>0$ para todo $n$.


**69.** **Nivel D.** Para $a_0=0$, $a_{n+1}=2a_n+2$, demuestra que $a_n=2^{n+1}-2$.


**70.** **Nivel D.** Sea $a_0=1$ y $a_{n+1}=a_n/(1+a_n)$. Demuestra que $a_n=1/(n+1)$.

## L. Diagnóstico y síntesis


**71.** **Nivel D.** Diagnostica: una prueba establece el caso base $P(1)$ y luego demuestra $P(k-1)\Rightarrow P(k+1)$ para $k\ge2$.


**72.** **Nivel D.** Una prueba de $P(n)$ usa inducción fuerte aunque $P(k+1)$ sólo depende de $P(k)$. ¿Es inválida?

## M. Problemas avanzados tipo prueba


**73.** **Nivel E.** Demuestra por inducción
$$
1\cdot2+2\cdot3+\cdots+n(n+1)=\frac{n(n+1)(n+2)}{3}
$$
para todo $n\ge1$. Presenta el paso inductivo como una cadena algebraica completa y explica dónde se usa exactamente la hipótesis inductiva.


**74.** **Nivel F.** Sea $a_1=1$ y
$$
a_{n+1}=\frac{2a_n}{1+a_n}.
$$
Demuestra que $0<a_n\le1$ para todo $n\ge1$. Explica por qué conviene fortalecer el objetivo «$a_n\le1$» añadiendo positividad.


**75.** **Nivel F.** Sea
$$
a_0=2,\qquad a_1=3,\qquad a_{n+2}=3a_{n+1}-2a_n.
$$
Demuestra que $a_n=2^n+1$ para todo $n\ge0$ y explica por qué se necesitan dos casos base.


**76.** **Nivel F.** Demuestra por inducción fuerte que todo entero $n\ge8$ puede escribirse como
$$
n=3a+5b
$$
con $a,b$ enteros no negativos. Justifica el número de casos base y evita usar teoría de congruencias.


**77.** **Nivel G.** Demuestra el resultado del ejercicio anterior mediante el principio del buen orden y un menor contraejemplo. Después compara línea por línea qué papel desempeña la minimalidad frente a la hipótesis inductiva fuerte.


**78.** **Nivel G.** Demuestra que el principio de buen orden implica el principio de inducción ordinaria para afirmaciones $P(n)$ con $n\ge n_0$. La prueba debe definir explícitamente el conjunto de contraejemplos y justificar cada paso.


**79.** **Nivel G.** Sea
$$
a_0=1,\qquad a_{n+1}=2a_n+1.
$$
(a) calcula los primeros cinco términos y formula una conjetura cerrada;  
(b) demuéstrala por inducción;  
(c) deduce un invariante cualitativo de la sucesión;  
(d) explica la frase «recursión construye; inducción verifica» en este ejemplo.


**80.** **Nivel G.** Se propone la siguiente prueba de «$2^n>n^2$ para todo $n\ge1$»:

> Base: $n=1$, pues $2>1$.  
> Supongamos $2^k>k^2$. Entonces
> $2^{k+1}>2k^2>(k+1)^2$,
> y termina la inducción.

(a) localiza todos los errores;  
(b) determina un enunciado verdadero cercano;  
(c) reconstruye una prueba inductiva completa.

***
## N. Elegir el índice inicial y justificar el rango


**81.** **Nivel C.** Determina el menor entero $n_0\ge0$ tal que $2^n\ge3n$ para todo $n\ge n_0$ y prueba ese rango por inducción. Explica por qué el caso verdadero $n=0$ no permite iniciar automáticamente una prueba de la misma desigualdad para todos los naturales.


**82.** **Nivel C.** Interpreta la suma $4+5+\cdots+n$ como vacía cuando $n=3$. Demuestra $4+5+\cdots+n=n(n+1)/2-6$ para $n\ge3$ y reescribe la prueba mediante $m=n-3\ge0$. Indica qué suma y qué igualdad corresponden a la nueva base.


**83.** **Nivel D.** Una sucesión empieza en el índice $5$: $a_5=7$ y $a_{n+1}=2a_n-3$ para $n\ge5$. Demuestra $a_n=4\cdot2^{n-5}+3$ en su rango completo. Escribe por separado $P(k)$, $P(k+1)$ y la regla disponible. Decide si estos datos determinan $a_0,\ldots,a_4$.


**84.** **Nivel D.** Con el producto vacío igual a $1$, demuestra
$$
\prod_{j=2}^n\frac{j-1}{j}=\frac1n\qquad(n\ge1).
$$
Da una prueba inductiva y otra por cancelación de factores. Justifica el índice inicial, cada denominador y la relación entre ambas pruebas.


**85.** **Nivel D.** Determina el menor índice $n_0\ge0$ para el cual $n(n-1)\ge3n+4$ vale en todos los enteros $n\ge n_0$. Prueba la cola por inducción y reindexa desde $0$. Comprueba que no elegiste el índice sólo porque el paso funcionaba allí.


**86.** **Nivel E.** Para $t\in\mathbb R$, define $x_0=t$ y $x_{n+1}=-x_n$. Demuestra $x_n=(-1)^nt$ y clasifica los valores de $t$ para los que existe una cola de índices en la cual $x_n\ge0$ siempre. Si tal cola existe, determina su menor índice inicial. Justifica por qué comprobar un término no negativo no basta.

## O. Dependencias y casos sin cubrir


**87.** **Nivel C.** Una prueba verifica $P(0)$ y $P(k)\Rightarrow P(k+1)$ para todo $k\ge1$. ¿Prueba todos los casos $n\ge0$? Construye una propiedad concreta que cumpla exactamente esos datos y falle en un índice. Indica una base adicional suficiente y prueba que repara la cobertura.


**88.** **Nivel D.** Se conocen $P(0),P(2)$ y $P(k)\Rightarrow P(k+3)$ para $k\ge0$. Describe sin usar congruencias qué índices quedan cubiertos y cuáles no. Construye un modelo en que todos los índices no cubiertos fallen. Repara la prueba con una sola base y justifica la cobertura de todos los naturales.


**89.** **Nivel D.** Se dan $u_0=u_1=1$ y $u_{n+3}=u_{n+1}+u_n$ para $n\ge0$. Un texto asegura que esto determina una sucesión positiva. Detecta el valor inicial ausente, exhibe una elección que refute positividad y demuestra que añadir un valor positivo en ese índice sí determina una sucesión positiva completa.


**90.** **Nivel E.** Una regla de prueba dice $P(n)\land P(n+2)\Rightarrow P(n+3)$ para $n\ge0$. Se verifican sólo $P(0)$ y $P(1)$. Explica por qué ni siquiera el primer uso de la regla está autorizado. Determina las bases necesarias entre los índices $0,1,2$ para cubrir todo el rango usando exclusivamente esa regla, y demuestra que bastan.


**91.** **Nivel E.** Se intenta probar que cualquier conjunto finito no vacío de objetos tiene un único color común. La base de un objeto es verdadera. Para $n+1$ objetos se toman dos grupos de $n$, uno omitiendo el primero y otro el último; se afirma que comparten un objeto que iguala los colores. Localiza el índice donde falla el paso, construye el contraejemplo y explica por qué un paso correcto desde $n\ge2$ no rescata la prueba.


**92.** **Nivel E.** Un texto define $x_0=1$, $x_{n+1}=1/(2-x_n)$ y afirma que los denominadores son no nulos «porque están escritos en la definición». Repara el argumento demostrando la existencia de todos los términos y su valor exacto. Contrasta con la misma regla y valor inicial $y_0=2$. ¿Toda regla parcial es necesariamente inválida en cualquier órbita?

## P. Fortalecer la afirmación antes de probar


**93.** **Nivel D.** Sea $0\le a_0\le1$ y $a_{n+1}=a_n^2/2$. Queremos probar $a_n\le1$. Explica por qué la sola hipótesis $a_k\le1$ no basta para el paso. Elige una afirmación fortalecida, demuestra que se preserva y deduce además una cota para todos los términos de índice positivo.


**94.** **Nivel E.** Define $u_0=0,v_0=1$ y $u_{n+1}=u_n+2v_n$, $v_{n+1}=2u_n+v_n$. Para probar una fórmula de $u_n$, fortalece el trabajo a dos identidades para $u_n+v_n$ y $v_n-u_n$. Demuéstralas simultáneamente y deduce fórmulas cerradas de ambas sucesiones.


**95.** **Nivel E.** Sean $a_0=1,a_1=2$ y $a_{n+2}=2a_{n+1}-a_n$. Demuestra $a_n\ge1$ fortaleciendo la prueba con una afirmación sobre las diferencias consecutivas. Explica por qué dos cotas inferiores aisladas no permiten restar en la recurrencia y deduce la fórmula exacta.


**96.** **Nivel E.** Define $S_0=\varnothing$ y $S_{n+1}=S_n\cup\{n\}$. Queremos probar $n\notin S_n$ para todo $n\ge0$. Explica por qué conocer sólo $k\notin S_k$ no excluye $k+1$ de $S_k$. Fortalece la afirmación a una descripción exacta de $S_n$ y cierra el objetivo.


**97.** **Nivel F.** Sea $f:A\to A$ con $f\circ f=f$. Define $f^0=\operatorname{id}_A$ y $f^{n+1}=f\circ f^n$. Demuestra que $f^{n+1}=f^n$ para $n\ge1$ mediante la afirmación más precisa $f^n=f$. Determina exactamente cuándo la igualdad se extiende también al índice $0$ y trata $A=\varnothing$.


**98.** **Nivel F.** Sean $x_1,x_2,\ldots$ reales en $[0,1]$, y define $t_0=1,t_{n+1}=t_nx_{n+1}$. Demuestra simultáneamente $0\le t_n\le1$ y $t_n\le x_j$ para cada $1\le j\le n$. Deduce que $t_{n+1}\le t_n$. Explica qué información se necesita para preservar las cotas y da un fallo si se admiten factores negativos.

## Q. Comparar métodos en problemas nuevos


**99.** **Nivel E.** Demuestra $n^3-n\ge0$ para enteros $n\ge1$ de tres formas: directamente, por inducción ordinaria y por menor contraejemplo. En cada una declara los datos de orden usados. Después compara cuál introduce menos información adicional.


**100.** **Nivel F.** Construye expresiones a partir del símbolo $x$ y de la regla: si $E,F$ son expresiones, también lo es $(E+F)$. Define $L(x)=1,I(x)=0$, $L((E+F))=L(E)+L(F)$ e $I((E+F))=1+I(E)+I(F)$. Demuestra $L(E)=I(E)+1$ para toda expresión, por inducción fuerte sobre $I(E)$ y por menor contraejemplo. Indica la base que necesita el argumento y por qué cada subexpresión tiene índice menor.


**101.** **Nivel F.** Sea $b_0,b_1,\ldots,b_r$ una lista de enteros no negativos estrictamente decreciente. Demuestra $b_j\le b_0-j$ por inducción y deduce $r\le b_0$. Después demuestra mediante buen orden que no existe una sucesión infinita estrictamente decreciente de enteros no negativos. Explica la diferencia entre una cota numérica y una contradicción obtenida de un mínimo.


**102.** **Nivel G.** Usando sólo inducción ordinaria, demuestra que todo subconjunto no vacío $S$ de los enteros no negativos tiene mínimo. No invoques buen orden al escogerlo. Puedes estudiar $S\cap\{0,1,\ldots,n\}$, pero debes justificar el paso y por qué un mínimo de una parte acotada acaba siendo mínimo de todo $S$.


**103.** **Nivel G.** Sea $F:D\to D$ y $S\subseteq D$. Demuestra que las dos condiciones son equivalentes: (i) $F(S)\subseteq S$; (ii) para toda entrada inicial $x_0\in S$, la órbita $x_{n+1}=F(x_n)$ permanece en $S$ para todos los índices. Trata $S=\varnothing$. Refuta la versión que sólo exige que una órbita particular permanezca en $S$ y explica dónde se necesita la cuantificación sobre las entradas iniciales.


**104.** **Nivel G.** Define $h(0)=0$. Para un índice positivo par $m=2r$, define $h(m)=h(r)$; para uno impar $m=2r+1$, define $h(m)=1-h(r)$. Justifica que cada referencia es a un índice menor y que la regla determina un único valor en todos los enteros no negativos. Calcula $h(0),\ldots,h(7)$ y prueba $h(m)\in\{0,1\}$. Presenta la prueba por inducción fuerte y explica cómo convertirla en ordinaria sin suponer sólo $h(k)\in\{0,1\}$.

# Soluciones razonadas

## A. Reconocer estructura inductiva


### 1

Toma $P(n)$ como la igualdad $1+2+\cdots+n=n(n+1)/2$. El índice inicial natural es $n=1$.


### 2

El caso base es $n=0$: se verifica $2^0=1\ge1$.


### 3

Porque quedan infinitos índices sin verificar. Una afirmación universal no se sigue de un número finito de casos, salvo que haya una razón estructural adicional.


### 4

No. La cadena inductiva puede comenzar en $5$. El caso base apropiado es $P(5)$, siempre que el paso inductivo sea válido para todo $k\ge5$.


### 5

Debe demostrar que para todo $k\ge n_0$, si $P(k)$ es verdadera, entonces $P(k+1)$ también lo es.


### 6

Partiendo sólo de $P(1)$, quedan cubiertos $1,3,5,\ldots$. Para cubrir también los pares haría falta, por ejemplo, un segundo caso base $P(2)$.

## B. Caso base y paso inductivo


### 7

El lado izquierdo es $1$ y el derecho $1^2=1$. Por tanto el caso base vale.


### 8

Se añade $2(k+1)-1=2k+1$: $k^2+(2k+1)=(k+1)^2$. Éste es el paso inductivo.


### 9

Porque el paso inductivo es una prueba de la implicación $P(k)\Rightarrow P(k+1)$. Para demostrar una implicación se supone temporalmente su antecedente.


### 10

Es circular: se ha asumido directamente la conclusión del paso. La hipótesis permitida es $P(k)$, no $P(k+1)$.


### 11

Base: $1\ge1$. Supón $3^k\ge1+2k$. Entonces $3^{k+1}=3\cdot3^k\ge3+6k$. Como $3+6k\ge3+2k=1+2(k+1)$ para $k\ge0$, queda el paso.


### 12

Base: $5^0-1=0$. Supón $5^k-1=4m$. Entonces $5^{k+1}-1=5(5^k-1)+4=20m+4=4(5m+1)$.


### 13

No. Si $P(k+1)$ se demuestra sin la hipótesis, el paso sigue siendo válido. Pero suele indicar que existe una prueba directa de todos los casos y que la inducción quizá es innecesaria.


### 14

La inducción necesita la implicación para todos los $k$ del rango. Si hay un hueco, la cadena puede detenerse allí y los índices posteriores no quedan justificados.

## C. Identidades elementales


### 15

Base $n=1$: $1=1$. Supón la fórmula para $k$. Entonces al añadir $2k+1$ se obtiene $k^2+2k+1=(k+1)^2$.


### 16

Base: $2=1\cdot2$. Supón $2+\cdots+2k=k(k+1)$. Añadiendo $2(k+1)$: $k(k+1)+2(k+1)=(k+1)(k+2)$.


### 17

Base $1=1$. Supón la fórmula para $k$. Entonces $k(k+1)/2+(k+1)=(k+1)(k+2)/2$.


### 18

Es exactamente el paso: sustituye $1+\cdots+n$ por $n(n+1)/2$ y factoriza $n+1$.


### 19

Desde $n(n+1)/2$ se añaden $n+1$ y $n+2$. El resultado es $[n(n+1)+2(n+1)+2(n+2)]/2=(n^2+5n+6)/2=(n+2)(n+3)/2$.


### 20

Base $n=1$: suma vacía $0=0$. Supón la fórmula para $k$. Para $k+1$ se añade $k$: $k(k-1)/2+k=k(k+1)/2$.


### 21

Base: $2=1\cdot2\cdot3/3$. Supón la fórmula para $k$. Añade $(k+1)(k+2)$ y factoriza $(k+1)(k+2)$: $k(k+1)(k+2)/3+(k+1)(k+2)=(k+1)(k+2)(k+3)/3$.


### 22

Base $n=1$: $1=1$. Supón la fórmula para $k$. Añade $(2k+1)^2$ y lleva a denominador $3$: $[k(4k^2-1)+3(4k^2+4k+1)]/3=(k+1)(4(k+1)^2-1)/3$.

## D. Desigualdades


### 23

Base: $1\ge1$. Si $2^k\ge k+1$, entonces $2^{k+1}\ge2k+2\ge k+2$ porque $k\ge0$.


### 24

Verificamos primero $n=1$ y $n=2$: $3\ge1$ y $9\ge4$. Ahora sea $k\ge2$ y supón $3^k\ge k^2$. Entonces $3^{k+1}\ge3k^2$. Basta $3k^2\ge(k+1)^2$, equivalente a $2k^2-2k-1\ge0$, que vale para $k\ge2$. Así el paso cubre todos los índices desde $2$ en adelante.


### 25

Base: $1=1$. Supón $k!\ge2^{k-1}$. Entonces $(k+1)!=(k+1)k!\ge2k!\ge2^k$, pues $k+1\ge2$.


### 26

Es la misma desigualdad que $2^n\ge n+1$. Base $0$. Paso: $2^{k+1}\ge2(k+1)\ge k+2$.


### 27

Base: $16=16$. Supón $k^2\le2^k$ con $k\ge4$. Entonces $2^{k+1}\ge2k^2$. Como $2k^2-(k+1)^2=k^2-2k-1\ge0$ para $k\ge3$, se obtiene $(k+1)^2\le2^{k+1}$.


### 28

Porque multiplicar por un número negativo invierte el sentido de la desigualdad. Una prueba válida debe establecer el signo del factor antes de usar la operación.

## E. Índice inicial y reindexación


### 29

Base: $2>1$. Supón $2^k>k$. Entonces $2^{k+1}>2k\ge k+1$ para $k\ge1$.


### 30

Base: $9\ge9$. Supón $k^2\ge2k+3$. Entonces $(k+1)^2=k^2+2k+1\ge4k+4$. Como $4k+4\ge2k+5=2(k+1)+3$ para $k\ge1$, queda el paso.


### 31

Debe verificar la base $n=4$ y un paso uniforme para $k\ge4$. Aunque $n=1$ también satisface la desigualdad, $n=3$ la refuta: $8<9$. Por ello no puede construirse una cadena válida de todos los casos desde $1$. El caso verdadero aislado no reemplaza la base del rango pedido.


### 32

Define $Q(m)=P(m+5)$ para $m\ge0$. Probar $Q(m)$ para todo $m\ge0$ equivale a probar $P(n)$ para todo $n\ge5$.


### 33

Base $n=4$: $16=16$. El paso ya mostró que $k^2\le2^k$ implica $(k+1)^2\le2^{k+1}$ para $k\ge4$. Por inducción, vale para todo $n\ge4$.


### 34

No hay mecanismo que produzca $P(n_0+1)$ ni $P(n_0+2)$ desde la base. Para iniciar el paso en $k\ge n_0+2$ deben verificarse por separado los casos necesarios hasta alcanzar ese índice.

## F. Varios casos base y recurrencias


### 35

$a_2=2$, $a_3=3$, $a_4=5$.


### 36

Porque el término $a_{n+2}$ depende de dos términos anteriores. Para iniciar el mecanismo hay que conocer la propiedad al menos en los dos valores iniciales.


### 37

Base: $a_0=2=1+1$ y $a_1=3=2+1$. Supón las fórmulas para $k$ y $k+1$. Entonces $a_{k+2}=3(2^{k+1}+1)-2(2^k+1)=2^{k+2}+1$.


### 38

Base: $b_0,b_1\ge0$. Si $b_k,b_{k+1}\ge0$, entonces $b_{k+2}=b_{k+1}+2b_k\ge0$.


### 39

No necesariamente. Si la fórmula para el nuevo término usa también el término $k$, puede ser necesario disponer de $P(k)$ y $P(k+1)$.


### 40

Para Fibonacci, la positividad usa que si $a_k>0$ y $a_{k+1}>0$, entonces $a_{k+2}=a_{k+1}+a_k>0$. Dos casos consecutivos alimentan el siguiente.

## G. Inducción fuerte


### 41

Fijado $k\ge2$, se supone que $P(2),P(3),\ldots,P(k)$ son verdaderas y, usando todas las necesarias, se demuestra $P(k+1)$.


### 42

Ambas concluyen exactamente que $P(n)$ vale para todos los índices del rango. Lo que cambia es la información permitida dentro del paso inductivo.


### 43

Base: $2=2$, $3=3$. Para $n\ge4$, suponiendo representables todos los enteros entre $2$ y $n-1$, escribimos $n=2+(n-2)$; como $n-2\ge2$ cuando $n\ge4$, el término $n-2$ es representable.


### 44

Base: $8=3+5$, $9=3+3+3$, $10=5+5$. Para $n\ge11$, $n-3\ge8$; por hipótesis fuerte $n-3=3a+5b$, luego $n=3(a+1)+5b$.


### 45

Porque las cadenas de índices se separan según el residuo al restar repetidamente $3$. Los casos $8,9,10$ inician las tres cadenas que luego cubre el paso.


### 46

Base $n=1$: $2=2$. Para $n=2$, $a_2=3\le4$. Si todos los casos hasta $k$ cumplen la cota, entonces $a_{k+1}=a_k+a_{k-1}\le2^k+2^{k-1}<2^{k+1}$.


### 47

Base: todos los objetos de tamaño $1$ poseen $P$ por la hipótesis explícita. Supón que todos los objetos de tamaños entre $1$ y $k$ poseen $P$. Un objeto de tamaño $k+1\ge2$ se descompone, por hipótesis, en dos objetos de tamaños positivos $r,s<k+1$. La hipótesis fuerte se aplica a ambos, y la preservación al combinarlos da $P$ para el objeto original. Así todos los objetos de tamaño positivo poseen $P$. Sin la hipótesis base, el enunciado no sería válido: la propiedad siempre falsa se preserva condicionalmente al combinar dos objetos que la poseen, porque ese antecedente nunca ocurre, pero no se cumple en ningún objeto de tamaño $1$.


### 48

Base: $Q(n_0)$ es $P(n_0)$. Si $Q(k)$ vale, entonces están disponibles todos los casos $P(n_0),\ldots,P(k)$; el paso fuerte produce $P(k+1)$, y junto con $Q(k)$ obtenemos $Q(k+1)$. De $Q(n)$ se sigue $P(n)$.

## H. Buen orden


### 49

Todo subconjunto no vacío de $\mathbb N$ posee un elemento mínimo.


### 50

Hay que suponer que existen contraejemplos y definir su conjunto como un subconjunto no vacío de $\mathbb N$. Sólo entonces el buen orden garantiza un mínimo.


### 51

Supón que hay fallos y sea $m$ el menor. Como $n=0$ cumple, $m\ge1$. Por minimalidad, $2^{m-1}\ge m$. Entonces $2^m=2\cdot2^{m-1}\ge2m\ge m+1$, contradicción.


### 52

Supón contraejemplos y sea $m\ge8$ el menor. Los casos $8,9,10$ son representables, así $m\ge11$. Entonces $m-3\ge8$ y, por minimalidad, $m-3=3a+5b$. Luego $m=3(a+1)+5b$, contradicción.


### 53

La minimalidad del contraejemplo garantiza que todos los índices menores relevantes sí satisfacen la propiedad, exactamente la información que una hipótesis inductiva fuerte permite usar.


### 54

Si $\mathbb N\setminus S$ fuera no vacío, tendría mínimo $m$. Como $0\in S$, $m>0$, así $m-1\in S$ por minimalidad. El cierre da $m\in S$, contradicción.

## I. Comparación de principios


### 55

Si base y paso valen pero existe un contraejemplo, toma el menor $m$. No es el caso base, así $m-1$ está en el rango y no es contraejemplo. Por tanto $P(m-1)$ vale y el paso da $P(m)$, contradicción.


### 56

Que todos los índices del rango estrictamente menores que $m$ satisfacen la propiedad.


### 57

Cuando la negación del resultado produce naturalmente un objeto mínimo y el argumento reduce ese objeto a uno menor. El lenguaje de minimalidad puede reflejar mejor la estructura.


### 58

La equivalencia es lógica: ambos principios permiten establecer los mismos tipos de afirmaciones sobre $\mathbb N$. Pero la forma de un problema puede encajar mejor con una cadena sucesiva o con una reducción al menor contraejemplo.

## J. Definiciones recursivas


### 59

$a_1=7$, $a_2=22$, $a_3=67$.


### 60

La definición recursiva produce cada término a partir de anteriores. Una fórmula cerrada expresa $a_n$ directamente en función de $n$ y, si se propone, debe demostrarse.


### 61

Puede definirse por $a_0=5$ y $a_{n+1}=a_n$.


### 62

Toma $a_0=1$ y $a_{n+1}=a_n+2$.


### 63

No. Se necesitan al menos dos valores iniciales para fijar una sucesión concreta; distintas elecciones producen sucesiones distintas.


### 64

Una vez fijado $a_0$, la regla determina un único $a_1=F(a_0)$; éste determina un único $a_2$, etc. La unicidad se propaga sucesivamente.

## K. Propiedades de objetos recursivos


### 65

Base $n=0$: $1=2-1$. Si $a_k=2^{k+1}-1$, entonces $a_{k+1}=2^{k+2}-1$.


### 66

Base $2=2$. Si $b_k=2+3k$, entonces $b_{k+1}=2+3k+3=2+3(k+1)$.


### 67

Base $1=0^2+1$. Si $c_k=k^2+1$, entonces $c_{k+1}=k^2+1+2k+1=(k+1)^2+1$.


### 68

Base positiva por hipótesis. Si $a_k>0$, entonces $1/a_k>0$, así $a_{k+1}=a_k+1/a_k>0$.


### 69

Base: $0=2-2$. Si $a_k=2^{k+1}-2$, entonces $a_{k+1}=2^{k+2}-4+2=2^{k+2}-2$.


### 70

Base: $1=1/(0+1)$. Si $a_k=1/(k+1)$, entonces $a_{k+1}=[1/(k+1)]/[1+1/(k+1)]=1/(k+2)$.

## L. Diagnóstico y síntesis


### 71

Al escribir $j=k-1$, el paso disponible es $P(j)\Rightarrow P(j+2)$ para $j\ge1$. Desde $P(1)$ sólo cubre $1,3,5,\ldots$. Para producir $P(2)$ mediante la escritura original haría falta $k=1$, fuera del rango autorizado, además de $P(0)$; no hay un paso disponible hacia ese índice. Añadir $P(2)$ inicia la cadena $2,4,6,\ldots$ y, con la cadena impar, cubre todos los índices desde $1$. El modelo «$n$ es impar» cumple la base y todos los pasos dados, pero falla en los pares, de modo que los datos originales no bastan.


### 72

No. La hipótesis fuerte incluye $P(k)$, así que el argumento puede ser válido. Simplemente es más información de la necesaria y la inducción ordinaria sería más económica.

## M. Problemas avanzados tipo prueba


### 73

Sea
$$
P(n):\quad \sum_{j=1}^{n}j(j+1)=\frac{n(n+1)(n+2)}{3}.
$$

**Base.** Para $n=1$, el lado izquierdo es $2$ y el derecho $1\cdot2\cdot3/3=2$.

**Paso.** Sea $k\ge1$ y supón
$$
1\cdot2+\cdots+k(k+1)=\frac{k(k+1)(k+2)}{3}.
$$
Entonces
$$
\begin{aligned}
1\cdot2+\cdots+k(k+1)+(k+1)(k+2)
&=\frac{k(k+1)(k+2)}{3}+(k+1)(k+2)\\
&=(k+1)(k+2)\left(\frac{k}{3}+1\right)\\
&=\frac{(k+1)(k+2)(k+3)}{3}.
\end{aligned}
$$
La primera igualdad del paso es exactamente donde se sustituye la suma anterior usando la hipótesis inductiva. La expresión final es la fórmula para $k+1$. Por inducción, el resultado vale para todo $n\ge1$.


### 74

Probamos simultáneamente
$$
P(n):\quad 0<a_n\le1.
$$

**Base.** $a_1=1$, luego $0<a_1\le1$.

**Paso.** Supón $0<a_k\le1$. Como $a_k>0$, el denominador $1+a_k$ es positivo, y por tanto
$$
a_{k+1}=\frac{2a_k}{1+a_k}>0.
$$
Para la cota superior, como el denominador es positivo,
$$
\frac{2a_k}{1+a_k}\le1
\iff
2a_k\le1+a_k
\iff
a_k\le1,
$$
que es la hipótesis.

Así $0<a_{k+1}\le1$.

La positividad no es decoración: permite controlar el signo del denominador y justificar la equivalencia usada en la desigualdad. Probar sólo $a_n\le1$ dejaría ese punto sin apoyo.


### 75

Sea $P(n): a_n=2^n+1$.

**Bases.**
$$
a_0=2=2^0+1,\qquad a_1=3=2^1+1.
$$

**Paso.** Supón
$$
a_k=2^k+1,\qquad a_{k+1}=2^{k+1}+1.
$$
Entonces
$$
\begin{aligned}
a_{k+2}
&=3a_{k+1}-2a_k\\
&=3(2^{k+1}+1)-2(2^k+1)\\
&=6\cdot2^k+3-2\cdot2^k-2\\
&=4\cdot2^k+1\\
&=2^{k+2}+1.
\end{aligned}
$$

Se requieren dos casos base porque la regla que produce $a_{k+2}$ utiliza simultáneamente los dos términos anteriores. Un único caso no pone en marcha la recurrencia.


### 76

Verificamos tres bases:
$$
8=3+5,\qquad 9=3+3+3,\qquad 10=5+5.
$$

Supón ahora que todo entero $m$ con $8\le m\le k$ es representable, donde $k\ge10$. Queremos representar $k+1$.

Como
$$
k+1-3=k-2\ge8,
$$
la hipótesis fuerte se aplica a $k-2$. Existen $a,b\ge0$ con
$$
k-2=3a+5b.
$$
Entonces
$$
k+1=3(a+1)+5b.
$$

Los tres casos base son naturales porque el paso incrementa en $3$: desde $8,9,10$ se generan sucesivamente todos los índices posteriores sin necesidad de hablar de residuos módulo $3$.


### 77

Supón que existe al menos un entero $n\ge8$ que no puede escribirse como $3a+5b$. Sea
$$
C=\{n\in\mathbb N:n\ge8\text{ y }n\text{ no es representable}\}.
$$
Por hipótesis $C$ es no vacío. Por buen orden, sea $m=\min C$.

Los enteros $8,9,10$ son representables, así $m\ge11$. Entonces $m-3\ge8$ y $m-3<m$. Por minimalidad de $m$, el entero $m-3$ no está en $C$; por tanto
$$
m-3=3a+5b
$$
para algunos $a,b\ge0$. Luego
$$
m=3(a+1)+5b,
$$
contradicción con $m\in C$.

Comparación: en inducción fuerte suponemos explícitamente que todos los enteros previos del rango son representables. En buen orden, esa misma información se obtiene de la minimalidad de $m$: ningún entero menor que el primer contraejemplo puede ser contraejemplo.


### 78

Supón que se cumplen:

1. $P(n_0)$;
2. para todo $k\ge n_0$, $P(k)\Rightarrow P(k+1)$.

Queremos probar $P(n)$ para todo $n\ge n_0$.

Supón lo contrario. Entonces el conjunto
$$
C=\{n\in\mathbb N:n\ge n_0\text{ y }\neg P(n)\}
$$
es no vacío. Por buen orden, posee un mínimo $m$.

Como $P(n_0)$ es verdadera, $m\ne n_0$, luego $m>n_0$. Por tanto $m-1\ge n_0$.

Por minimalidad de $m$, $m-1\notin C$, de modo que $P(m-1)$ es verdadera. Aplicando el paso inductivo con $k=m-1$, obtenemos $P(m)$, contradicción con $m\in C$.

Así $C$ debe ser vacío y $P(n)$ vale para todo $n\ge n_0$.


### 79

Los primeros términos son
$$
1,3,7,15,31.
$$
La conjetura es
$$
a_n=2^{n+1}-1.
$$

Base:
$$
a_0=1=2^1-1.
$$

Paso: si $a_k=2^{k+1}-1$, entonces
$$
a_{k+1}=2(2^{k+1}-1)+1=2^{k+2}-1.
$$
Por inducción, la fórmula vale para todo $n\ge0$.

Como $2^{n+1}$ es par para todo $n\ge0$, $a_n$ es siempre impar. También es positivo y estrictamente creciente.

La recurrencia especifica cómo generar cada término a partir del anterior: construye la sucesión. La inducción demuestra que todos los términos generados satisfacen una descripción global que la recurrencia no muestra de forma inmediata.


### 80

**(a)** Hay dos problemas.

Primero, el enunciado original es falso: para $n=2$ se tiene $2^2=2^2$, no desigualdad estricta; para $n=3$, $8<9$.

Segundo, el paso usa
$$
2k^2>(k+1)^2,
$$
que no vale para todos los $k\ge1$. Es equivalente a
$$
k^2-2k-1>0,
$$
que sólo vale desde cierto índice.

**(b)** Un enunciado verdadero y natural es
$$
2^n\ge n^2\qquad\text{para todo }n\ge4.
$$

**(c) Base.**
$$
2^4=16=4^2.
$$

**Paso.** Sea $k\ge4$ y supón $2^k\ge k^2$. Entonces
$$
2^{k+1}\ge2k^2.
$$
Basta probar
$$
2k^2\ge(k+1)^2.
$$
La diferencia es
$$
2k^2-(k+1)^2=k^2-2k-1.
$$
Para $k\ge4$,
$$
k^2-2k-1=(k-1)^2-2\ge9-2=7>0.
$$
Así
$$
2^{k+1}\ge(k+1)^2.
$$

Por inducción, $2^n\ge n^2$ para todo $n\ge4$.

La lección es que el rango de validez del paso y el caso base deben estar coordinados; un caso base aislado no atraviesa huecos donde el paso falla.

## N. Elegir el índice inicial y justificar el rango


### 81

Los casos $1,2,3$ fallan: $2<3$, $4<6$, $8<9$. En $4$, $16\ge12$. Sea $k\ge4$ y supongamos $2^k\ge3k$. Entonces $2^{k+1}\ge6k\ge3k+3=3(k+1)$, pues $3k\ge3$. Por inducción, la desigualdad vale en la cola desde $4$. Toda cola iniciada antes incluiría el caso falso $3$, así que $n_0=4$ es mínimo. Aunque $2^0\ge0$, la implicación del paso en $k=0$ sería verdadera en su antecedente y falsa en su conclusión. Una base aislada no reemplaza el paso uniforme.


### 82

En $n=3$ la suma es $0$ y $3\cdot4/2-6=0$. Si la fórmula vale para $k\ge3$, al agregar $k+1$ obtenemos $k(k+1)/2-6+(k+1)=(k+1)(k+2)/2-6$, que es la meta en $k+1$.

Con $m=n-3$, sea $Q(m):4+\cdots+(m+3)=(m+3)(m+4)/2-6$. En $m=0$ la suma vuelve a ser vacía y el lado derecho es $0$. El paso agrega $m+4$ y lleva el lado derecho a $(m+4)(m+5)/2-6$. La correspondencia entre índices $m\ge0$ y $n\ge3$ es biyectiva por $n=m+3$; no se altera el contenido ni se introduce un término $3$ en la suma.


### 83

La base es $a_5=7=4\cdot2^0+3$. Fijado $k\ge5$, la hipótesis $P(k)$ es $a_k=4\cdot2^{k-5}+3$; la meta $P(k+1)$ es $a_{k+1}=4\cdot2^{k-4}+3$. La regla da
$$
a_{k+1}=2a_k-3=2(4\cdot2^{k-5}+3)-3=4\cdot2^{k-4}+3.
$$
Así la fórmula vale para todos los índices $n\ge5$. Los datos no definen términos anteriores: la regla sólo se impone para $n\ge5$. Si se desea extender la sucesión hacia atrás, se necesita una nueva condición; no se puede aplicar una regla fuera de su rango declarado.


### 84

En $n=1$, el producto es vacío y vale $1=1/1$. Si la fórmula vale para $k\ge1$, el producto para $k+1$ es el anterior multiplicado por $k/(k+1)$, y por tanto vale $(1/k)\,k/(k+1)=1/(k+1)$. Todos los denominadores son enteros positivos.

Para $n\ge2$, escribir los factores da $(1/2)(2/3)\cdots((n-1)/n)$. Los números $2,\ldots,n-1$ aparecen en numerador y denominador y son no nulos; se cancelan dejando $1/n$. El caso $n=1$ ya se verificó aparte. La prueba inductiva realiza una cancelación al añadir cada factor, mientras la directa las organiza todas juntas. El índice $0$ no es admisible para el lado derecho $1/n$.


### 85

La diferencia entre los miembros es $d(n)=n^2-4n-4$. Para $n=0,1,2,3,4$ sus valores son $-4,-7,-8,-7,-4$, y $d(5)=1$. Por tanto la base válida es $5$. Si $d(k)\ge0$ con $k\ge5$, entonces $d(k+1)=d(k)+2k-3\ge0+7>0$. Esto prueba todos los índices posteriores. Como $4$ falla, ninguna cola iniciada antes sirve. El paso preserva no negatividad desde $k\ge2$, pero eso no da una base verdadera en $2$.

La versión reindexada es $Q(m):(m+5)(m+4)\ge3(m+5)+4$ para $m\ge0$. Su base corresponde a $n=5$ y el incremento de la diferencia es $2m+7>0$.


### 86

Base: $x_0=t=(-1)^0t$. Si la fórmula vale en $k$, entonces $x_{k+1}=-(-1)^kt=(-1)^{k+1}t$. Por inducción vale en todos los índices.

Si $t=0$, todos los términos son cero y la menor cola comienza en $0$. Si $t>0$, cada índice impar produce $-t<0$; cualquier cola contiene un impar, por ejemplo su primer índice si es impar o el siguiente si es par. Si $t<0$, cada índice par produce $t<0$, y cualquier cola contiene un par por el mismo razonamiento. Así sólo $t=0$ admite esa cola. Un término no negativo puede ser seguido por uno negativo: el paso no preserva el signo salvo que el término sea cero.

## O. Dependencias y casos sin cubrir


### 87

No. Toma $P(n):n\neq1$. La base $P(0)$ es verdadera. Para $k\ge1$, la conclusión $k+1\neq1$ siempre es verdadera, por lo que cada implicación exigida vale, incluso cuando su antecedente $P(1)$ es falso. Sin embargo, $P(1)$ falla.

Añadir $P(1)$ como dato para una propiedad general repara la cobertura: esa base y el paso para $k\ge1$ prueban por inducción todos los casos desde $1$; con $P(0)$ se cubre el rango completo. El contraejemplo no puede cumplir la base adicional, lo cual muestra que era información ausente.


### 88

Quedan cubiertas las cadenas $0,3,6,\ldots$ y $2,5,8,\ldots$; falta $1,4,7,\ldots$. Todo natural pertenece a una de esas tres cadenas: restar $3$ mientras el resultado siga siendo al menos $3$ termina en $0,1$ o $2$, pues los naturales disminuyen en cada resta.

Un modelo es declarar $P(n)$ verdadera exactamente en las dos cadenas cubiertas. Ambas bases son verdaderas y sumar $3$ mantiene esas cadenas; si el antecedente falla, la implicación sigue siendo verdadera. Añadir $P(1)$ inicia la tercera cadena. Repetir el paso en cada una, o usar inducción fuerte con las tres bases y reducir una meta $n\ge3$ a $n-3$, prueba todos los casos. No se usó teoría de congruencias.


### 89

Falta $u_2$. Los términos $u_3,u_4,u_5,\ldots$ se pueden producir sucesivamente una vez conocido ese valor, pero la regla nunca lo define. Elegir $u_2=-1$ ya refuta positividad y aun así permite construir una sucesión que satisface la regla.

Si añadimos $u_2=c>0$, cada término nuevo queda determinado de manera única por términos anteriores. Las bases $u_0,u_1,u_2$ son positivas. Para $m\ge3$, la hipótesis fuerte proporciona positividad de $u_{m-2}$ y $u_{m-3}$, y la regla $u_m=u_{m-2}+u_{m-3}$ da positividad de $u_m$. Así todos los términos son positivos. Construcción y prueba requieren conocer el tercer valor, aunque la regla no use el término inmediatamente anterior.


### 90

Para obtener $P(3)$ con $n=0$ se necesitan $P(0)$ y $P(2)$; la segunda no está disponible. Además, ninguna conclusión de la regla tiene índice menor que $3$, así que ninguno de los casos $0,1,2$ puede obtenerse de ella. Deben establecerse los tres por separado si no se usa otro mecanismo.

Con las tres bases, para una meta $m\ge3$ la hipótesis fuerte hasta $m-1$ da $P(m-3)$ y $P(m-1)$. Aplicar la regla con $n=m-3$ produce $P(m)$. Ambos índices están en el rango. Para mostrar que $P(2)$ no estaba implícita, el modelo $P(n):n\neq2$ cumple las dos bases y toda regla, cuya conclusión es siempre verdadera, pero falla precisamente en $2$.


### 91

Cuando $n=1$, los dos grupos son los dos objetos por separado y su intersección es vacía. No hay un objeto común que permita comparar sus colores. Un conjunto de dos objetos, uno rojo y otro azul, cumple la base de los grupos unitarios y refuta la conclusión para la pareja.

Para $n\ge2$, los grupos descritos comparten $n-1\ge1$ objetos. Si realmente ambos grupos fueran de color uniforme, uno común sí obligaría a que sus colores coincidan y cubrirían juntos el conjunto entero. Esto hace válida esa implicación condicional desde $n=2$, pero no establece la base de dos objetos, que es falsa. La base de un objeto y un paso desde $2$ dejan sin justificar precisamente el enlace $1\to2$.


### 92

La escritura no garantiza un denominador no nulo. Para $x$, probamos por inducción que los términos se pueden construir y $x_n=1$. La base vale. Si $x_k=1$ existe, $2-x_k=1\neq0$, así que el siguiente término existe y es $1$. Esto justifica cada etapa y todos los valores.

Para $y_0=2$, el primer paso divide por cero y no hay sucesión real completa con esos datos. La regla es parcial como función de una entrada real cualquiera, pero la órbita iniciada en $1$ permanece en el conjunto seguro $\{1\}$. Una regla parcial puede definir una órbita válida si se demuestra que ésta nunca llega a las entradas prohibidas; no basta declararlo ni rechazarla sin analizar la órbita.

## P. Fortalecer la afirmación antes de probar


### 93

La entrada $a_k=-3$ cumple $a_k\le1$ pero produce $9/2>1$; por tanto esa sola condición no justifica el paso. No es un contraejemplo a la órbita dada, que empieza en el intervalo indicado.

Fortalecemos a $0\le a_n\le1$. La base está dada. Si $0\le a_k\le1$, entonces $0\le a_k^2\le1$, por lo que $0\le a_{k+1}\le1/2\le1$. La inducción prueba el intervalo y el objetivo inicial. Además, cada término positivo es resultado de algún paso, de modo que $0\le a_n\le1/2$ para $n\ge1$. Esta cota no se impone a $a_0$, que puede ser $1$.


### 94

Probamos $u_n+v_n=3^n$ y $v_n-u_n=(-1)^n$. En $0$, ambas sumas indicadas valen $1$. Si las identidades valen en $k$, entonces
$$
u_{k+1}+v_{k+1}=3(u_k+v_k)=3^{k+1},
$$
$$
v_{k+1}-u_{k+1}=u_k-v_k=-(-1)^k=(-1)^{k+1}.
$$
Así se preservan conjuntamente. Sumar las identidades da $2v_n=3^n+(-1)^n$, y restarlas da $2u_n=3^n-(-1)^n$. Por tanto
$$
u_n=\frac{3^n-(-1)^n}{2},\qquad v_n=\frac{3^n+(-1)^n}{2}.
$$
La fórmula de $u_k$ sola no proporciona directamente $v_k$, que aparece en su regla; las dos identidades suministran exactamente la información acoplada necesaria.


### 95

De $a_n,a_{n+1}\ge1$ no se deduce $2a_{n+1}-a_n\ge1$: los valores $a_n=10,a_{n+1}=1$ refutan esa inferencia. En la sucesión dada, probamos $a_{n+1}-a_n=1$. La base es $2-1=1$. Si la diferencia vale en $k$, entonces
$$
a_{k+2}-a_{k+1}=(2a_{k+1}-a_k)-a_{k+1}=a_{k+1}-a_k=1.
$$
Todas las diferencias son $1$. Ahora la base $a_0=1$ y el paso $a_{k+1}=a_k+1$ prueban por inducción $a_n=n+1$, que da la cota para $n\ge0$. La información sobre diferencias controla la resta; las cotas inferiores por separado no lo hacen.


### 96

Un conjunto puede excluir $k$ e incluir $k+1$, por ejemplo $\{k+1\}$. Por tanto la sola ausencia de $k$ no controla todas las entradas previas del paso. Probamos
$$
S_n=\{j\in\mathbb Z:0\le j<n\}.
$$
La base es el conjunto vacío, porque no hay entero $j$ con $0\le j<0$. Si vale en $k$, entonces $S_{k+1}=\{j:0\le j<k\}\cup\{k\}$. Un entero está en esta unión exactamente cuando $0\le j<k+1$: si está por debajo de $k$, pertenece a la primera parte; si no, la condición entera lo obliga a ser $k$. Así obtenemos la fórmula en $k+1$. Como $n<n$ es falso, $n\notin S_n$. La descripción exacta controla todas las entradas, no sólo una ausencia.


### 97

Las composiciones están tipadas porque $f$ lleva $A$ en $A$. Para $n=1$, $f^1=f\circ\operatorname{id}_A=f$. Si $f^k=f$ con $k\ge1$, entonces $f^{k+1}=f\circ f^k=f\circ f=f$. Por inducción, cada iteración positiva es $f$; en particular $f^{n+1}=f^n$ desde $1$.

En $0$, la igualdad pide $f^1=f^0$, es decir, $f=\operatorname{id}_A$, condición necesaria y suficiente. Si $A$ es vacío, sólo hay una función $A\to A$, que es la identidad, así todas las igualdades valen también en $0$. La precisión del fortalecimiento permite leer cada iteración; no autoriza cambiar su rango.


### 98

En $0$, $t_0=1$ pertenece al intervalo y no hay índices $j$ que comprobar. Supongamos las dos partes en $k$. Como $t_k\ge0$ y $0\le x_{k+1}\le1$, se tiene $0\le t_{k+1}=t_kx_{k+1}\le t_k\le1$. Para $j\le k$, esta cadena y $t_k\le x_j$ dan $t_{k+1}\le x_j$. Para el nuevo índice, $t_k\le1$ y $x_{k+1}\ge0$ dan $t_{k+1}\le x_{k+1}$. Así se preservan todos los datos y se prueba también la monotonía.

El signo de $t_k$ justifica comparar el producto con $t_k$; el del factor justifica multiplicar la cota $t_k\le1$. Si $x_1=x_2=-1$, entonces $t_1=-1,t_2=1$, por lo que falla $t_2\le t_1$ y también $t_2\le x_1$.

## Q. Comparar métodos en problemas nuevos


### 99

Directamente, $n^3-n=n(n-1)(n+1)$ y los tres factores son no negativos para $n\ge1$.

Por inducción, la base en $1$ vale $0$. Si $k^3-k\ge0$, entonces $(k+1)^3-(k+1)=(k^3-k)+3k^2+3k\ge0$, porque $k\ge1$. Esto cierra la cola.

Por menor contraejemplo, supongamos no vacío $C=\{n\ge1:n^3-n<0\}$. Es un subconjunto de los naturales, así posee mínimo $m$. La base excluye $m=1$; por tanto $m\ge2$ y $m-1\ge1$. Minimalidad da $(m-1)^3-(m-1)\ge0$. Agregar $3(m-1)^2+3(m-1)\ge0$ produce $m^3-m\ge0$, contradicción. La prueba directa sólo requiere factorizar y controlar signos; las otras añaden un mecanismo de índices que aquí resulta válido pero innecesario.


### 100

Una expresión con $I=0$ no puede ser compuesta, porque una compuesta tiene $I=1+I(E)+I(F)\ge1$. Por tanto es $x$ y cumple $L=1=I+1$.

Para la inducción fuerte, considera una expresión compuesta $G=(E+F)$ con $I(G)=m\ge1$. Sus subexpresiones tienen índices no negativos estrictamente menores que $m$, porque $I(G)=1+I(E)+I(F)$. La hipótesis da $L(E)=I(E)+1$ y $L(F)=I(F)+1$. Entonces $L(G)=I(E)+I(F)+2=I(G)+1$. La base y el paso prueban la afirmación para todas las expresiones.

Para menor contraejemplo, si existen expresiones que fallan, los valores de $I$ de esas expresiones forman un subconjunto no vacío de naturales. Toma su mínimo $m$ y una expresión fallida de ese tamaño. No es $x$ por la base. Es compuesta y ambas subexpresiones cumplen la fórmula por sus índices menores. La misma cuenta la demuestra para la expresión fallida, contradicción. La base debe cubrir todos los objetos del primer tamaño; no basta declarar una propiedad sólo para tamaños compuestos.


### 101

En $j=0$ hay igualdad. Si $j<r$, como los términos son enteros y $b_{j+1}<b_j$, se tiene $b_{j+1}\le b_j-1$. Bajo la hipótesis $b_j\le b_0-j$, obtenemos $b_{j+1}\le b_0-(j+1)$. Así vale la cota hasta $r$. Como $b_r\ge0$, resulta $0\le b_0-r$ y $r\le b_0$.

Si existiera una sucesión infinita de ese tipo, el conjunto de sus valores sería no vacío y estaría contenido en los naturales no negativos. Su mínimo se alcanza en algún término $b_m$. Pero el término siguiente existe y satisface $b_{m+1}<b_m$, contradiciendo minimalidad. El primer argumento cuantifica cuántas disminuciones admite un valor inicial; el segundo descarta infinitud sin calcular su longitud. La no negatividad es esencial: $0,-1,-2,\ldots$ es infinita y estrictamente decreciente en los enteros.


### 102

Probamos por inducción que $S_n=S\cap\{0,\ldots,n\}$ es vacío o tiene mínimo. Para $n=0$ sólo puede ser vacío o $\{0\}$. Supongamos la afirmación en $k$. Si $S_k$ tiene mínimo $m$, éste sigue siendo mínimo al agregar eventualmente $k+1$, pues $m\le k<k+1$. Si $S_k$ es vacío, $S_{k+1}$ es vacío cuando $k+1\notin S$ y es $\{k+1\}$ cuando $k+1\in S$. Los casos cubren el paso.

Como $S$ no es vacío, toma algún $s\in S$, sin afirmar que sea mínimo. La parte $S_s$ contiene $s$, luego tiene mínimo $m$ por la afirmación probada. Para cualquier $t\in S$, si $t\le s$, pertenece a $S_s$ y satisface $m\le t$; si $t>s$, se tiene $m\le s<t$. Así $m$ es mínimo de todo $S$. La existencia de $s$ viene de no vacuidad y la del mínimo finito de inducción; no se usó el principio que se quería demostrar.


### 103

Si $F(S)\subseteq S$ y fijamos $x_0\in S$, la base está dada. Si $x_k\in S$, entonces $x_{k+1}=F(x_k)\in F(S)\subseteq S$. La inducción prueba toda la órbita; existe en todos los índices porque $F$ es total y lleva $D$ en $D$.

Recíprocamente, fija $s\in S$ arbitrario y aplica (ii) a la órbita que empieza en $x_0=s$. Su término de índice $1$ es $F(s)$ y pertenece a $S$. Así toda imagen de un elemento de $S$ está en $S$. Si $S$ es vacío, la imagen es vacía y (ii) no tiene entradas iniciales que comprobar: ambas condiciones valen.

Una órbita particular no basta. Toma $D=\{0,1,2\}$, $S=\{0,1\}$ y $F(0)=0,F(1)=2,F(2)=2$. La órbita desde $0$ permanece en $S$, pero $F(1)=2\notin S$. En la vuelta se necesita poder iniciar la órbita en cada $s\in S$, no sólo en uno favorable.


### 104

Cada entero positivo es par o impar y esas posibilidades son excluyentes. En el caso par, $r\ge1$ y $r<2r=m$. En el impar, $r\ge0$ y $r<2r+1=m$. Cada representación determina un único $r$, por cancelación en $2r=2s$ o $2r+1=2s+1$. Así, al construir los valores en orden creciente, la regla usa un valor anterior único y aplica una operación determinada. Ningún índice queda sin cubrir ni recibe reglas contradictorias.

Los primeros valores son $0,1,1,0,1,0,0,1$. Para la prueba fuerte, la base $h(0)=0$ está en $\{0,1\}$. Si todos los valores anteriores a $m\ge1$ están en ese conjunto, el índice $r<m$ de su regla también. En el caso par se conserva $h(r)$; en el impar, $1-h(r)$ intercambia $0$ y $1$. Por tanto $h(m)$ está en el conjunto y el resultado vale en todos los índices.

Para inducción ordinaria usamos $Q(k):h(j)\in\{0,1\}$ para todo $0\le j\le k$. Su base vale. Desde $Q(k)$ se obtiene la información sobre el índice reducido de $k+1$, que es a lo sumo $k$, y se prueba el nuevo valor; junto con los anteriores esto da $Q(k+1)$. Conocer sólo $h(k)$ no proporcionaría en general el valor $h(r)$ que necesita la regla.

***

[← Capítulo 10](algebra-para-matematicos-capitulo-10-como-se-demuestra.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 12 →](algebra-para-matematicos-capitulo-12-sumas-productos-e-identidades-finitas.md)
