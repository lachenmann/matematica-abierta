---
{
  "title": "Identidades, productos notables y factorización",
  "description": "Capítulo 19 del Tomo I de Álgebra para matemáticos, con 92 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0194",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C19",
  "editorial-id": "MA-BCH-APM-01-024",
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
    "MA-BCH-0193"
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

En capítulos anteriores hemos aprendido a transformar expresiones sin perder de vista las propiedades que justifican cada paso. Ahora aparece una habilidad diferente. Ya no basta con saber **cómo** distribuir, multiplicar o combinar términos: debemos aprender a decidir **qué forma de una expresión conviene mirar**.

Considere

$$
x^2-9
$$

y

$$
(x-3)(x+3).
$$

Son expresiones iguales para todo $x\in\mathbb R$, pero no muestran la misma información. La primera hace visible una diferencia de cuadrados. La segunda exhibe dos factores. Si expandimos,

$$
(x-3)(x+3)=x^2-9.
$$

Si leemos la misma identidad en sentido inverso,

$$
x^2-9=(x-3)(x+3).
$$

La primera dirección se llama **expansión**. La segunda, **factorización**.

El punto decisivo de este capítulo es que ninguna de las dos formas es universalmente “mejor”. Una forma puede ser más útil para comparar términos; otra, para reconocer factores; otra, para preparar una transformación posterior. La fluidez algebraica madura consiste en poder cambiar de representación **con un propósito**.

La idea rectora será:

> **Factorizar no es adivinar una fórmula. Es reconstruir una estructura multiplicativa cuya expansión reproduce exactamente la expresión inicial.**

Por eso no estudiaremos los llamados “casos de factorización” como una colección de recetas aisladas. Los derivaremos de unas pocas ideas: distributividad, reconocimiento de forma, agrupación y verificación.

## 19.1. Expandir y factorizar son dos lecturas de la distributividad {#apm-c19-s01}

La identidad fundamental es

$$
a(b+c)=ab+ac.
$$

Leída de izquierda a derecha, distribuye el factor $a$ sobre una suma. Leída de derecha a izquierda, extrae el factor común $a$:

$$
ab+ac=a(b+c).
$$

No son dos leyes diferentes. Son la misma igualdad recorrida en direcciones opuestas.

### Dos formas, una misma expresión

Por ejemplo,

$$
3x(x+4)=3x^2+12x.
$$

La forma $3x(x+4)$ hace visible que toda la expresión es un producto y que $3x$ es factor. La forma $3x^2+12x$ hace visibles dos términos y sus coeficientes. La igualdad permite pasar de una descripción a la otra.

### Factorizar como reconstrucción

Supongamos que encontramos

$$
6x^2+9x.
$$

Los dos términos contienen $3x$:

$$
6x^2+9x
=
3x(2x)+3x(3)
=
3x(2x+3).
$$

La factorización no apareció por reconocimiento mágico. Reconstruimos un producto a partir de la distributividad.

### Verificar en sentido contrario

Toda factorización propuesta puede someterse a una prueba simple:

```text
FORMA FACTORIZADA
      ↓ expandir
FORMA OBTENIDA
      ↓ comparar
EXPRESIÓN ORIGINAL
```

Si proponemos

$$
x^2+5x+6=(x+2)(x+3),
$$

expandimos:

$$
(x+2)(x+3)
=
x^2+3x+2x+6
=
x^2+5x+6.
$$

La verificación confirma la identidad. Factorizar produce una conjetura estructural; expandir permite auditarla.

### Pregunta de lectura

Ante una expresión, antes de operar, pregunte:

> ¿Estoy mirando una suma que oculta un producto, o un producto que conviene desarrollar?

## 19.2. Expansión controlada: distribuir sin destruir información {#apm-c19-s02}

Expandir significa eliminar productos sobre sumas mediante distributividad. Pero no toda expansión debe hacerse de inmediato ni hasta el final.

Considere

$$
(2x-3)(x+5).
$$

Aplicando distributividad:

$$
(2x-3)(x+5)
=
2x(x+5)-3(x+5)
$$

y luego

$$
=
2x^2+10x-3x-15
=
2x^2+7x-15.
$$

### La estructura general

Para cualesquiera $a,b,c,d$,

$$
(a+b)(c+d)
=
ac+ad+bc+bd.
$$

La justificación no depende de una mnemotecnia:

$$
(a+b)(c+d)
=
a(c+d)+b(c+d)
=
ac+ad+bc+bd.
$$

### El signo negativo entra en la distribución

Por ejemplo,

$$
(x-4)(x-7)
=
x(x-7)-4(x-7)
=
x^2-11x+28.
$$

El $+28$ proviene de $(-4)(-7)$.

### No expandir por reflejo

Considere

$$
(x-1)(x+1)+(x-1)(x+4).
$$

La forma dada ya muestra un factor común:

$$
(x-1)\big((x+1)+(x+4)\big)
=
(x-1)(2x+5).
$$

Expandir todo al comienzo habría ocultado temporalmente la estructura útil.

### Expansión parcial

En

$$
(x+2)\big((x-1)(x+1)+3\big),
$$

puede ser útil expandir sólo el producto interior:

$$
(x-1)(x+1)=x^2-1,
$$

obteniendo

$$
(x+2)(x^2+2).
$$

No existe obligación de expandir el producto exterior si la forma obtenida ya cumple el propósito.

## 19.3. Factor común: la primera pregunta {#apm-c19-s03}

Cuando una expresión es una suma de términos, la primera inspección debería buscar factores comunes.

En

$$
12x^3y-18x^2y^2,
$$

ambos términos contienen $6x^2y$. Por tanto,

$$
12x^3y-18x^2y^2
=
6x^2y(2x-3y).
$$

### El factor común más informativo

Podríamos extraer sólo $2x$, pero la expresión interior seguiría teniendo factor común. En problemas de factorización suele convenir extraer de una vez el mayor factor común visible.

No estamos desarrollando aquí una teoría general del MCD de polinomios.

### El coeficiente residual $1$

$$
x^4+x^2
=
x^2(x^2+1).
$$

El $1$ es esencial porque $x^2=x^2\cdot1$.

### Extraer un factor negativo

A veces conviene elegir deliberadamente $-1$:

$$
3-x=-(x-3),
$$

y en general

$$
a-b=-(b-a).
$$

Esto puede hacer visible otra estructura.

### Protocolo inicial

```text
1. LEER LOS TÉRMINOS.
2. BUSCAR FACTORES NUMÉRICOS COMUNES.
3. BUSCAR POTENCIAS COMUNES.
4. BUSCAR BLOQUES ALGEBRAICOS COMUNES.
5. DECIDIR SI CONVIENE EXTRAER UN SIGNO NEGATIVO.
6. VOLVER A LEER LA EXPRESIÓN RESULTANTE.
```

El último paso es crucial: una factorización puede revelar inmediatamente otra.

## 19.4. El cuadrado de una suma y de una diferencia {#apm-c19-s04}

La identidad

$$
(a+b)^2=a^2+2ab+b^2
$$

se deriva de

$$
(a+b)^2=(a+b)(a+b).
$$

Distribuyendo:

$$
(a+b)(a+b)
=
a^2+ab+ab+b^2
=
a^2+2ab+b^2.
$$

Por tanto,

$$
\boxed{(a+b)^2=a^2+2ab+b^2.}
$$

Análogamente,

$$
\boxed{(a-b)^2=a^2-2ab+b^2.}
$$

### El término cruzado no es opcional

La igualdad

$$
(a+b)^2=a^2+b^2
$$

es falsa en general. Con $a=b=1$:

$$
4\neq2.
$$

El error consiste en perder los dos términos cruzados $ab$.

### Lectura inversa

$$
a^2+2ab+b^2=(a+b)^2,
$$

$$
a^2-2ab+b^2=(a-b)^2.
$$

Esto permite reconocer trinomios cuadrados perfectos.

Por ejemplo,

$$
x^2+10x+25=(x+5)^2.
$$

Los extremos son $x^2$ y $5^2$, y el término medio coincide con $2(x)(5)$.

### Conexión con C13

Los coeficientes $1,2,1$ son los coeficientes binomiales de la expansión de segundo grado. La identidad forma parte de la estructura general del binomio.

## 19.5. Diferencia de cuadrados: una identidad con dos direcciones {#apm-c19-s05}

Multipliquemos

$$
(a+b)(a-b).
$$

Entonces

$$
(a+b)(a-b)
=
a^2-ab+ab-b^2
=
a^2-b^2.
$$

Así,

$$
\boxed{a^2-b^2=(a-b)(a+b).}
$$

### Reconocimiento

$$
9x^2-25=(3x)^2-5^2,
$$

de modo que

$$
9x^2-25=(3x-5)(3x+5).
$$

### Factorización iterada

$$
x^4-16
=
(x^2-4)(x^2+4)
=
(x-2)(x+2)(x^2+4).
$$

En el marco actual no afirmaremos formalmente que $x^2+4$ sea irreducible. Sólo observamos que las estructuras elementales estudiadas aquí no producen otra factorización real del mismo tipo. La irreducibilidad pertenece a C25.

### No confundir suma y diferencia

La identidad no autoriza

$$
a^2+b^2=(a+b)(a-b).
$$

La semejanza visual no basta: hay que verificar la estructura.

## 19.6. Cubos: expansión y factorización {#apm-c19-s06}

Por C13,

$$
(a+b)^3
=
a^3+3a^2b+3ab^2+b^3,
$$

y

$$
(a-b)^3
=
a^3-3a^2b+3ab^2-b^3.
$$

### Diferencia de cubos

$$
\boxed{
a^3-b^3
=
(a-b)(a^2+ab+b^2).
}
$$

Al expandir,

$$
(a-b)(a^2+ab+b^2)
=
a^3-b^3.
$$

Los términos intermedios se cancelan.

### Suma de cubos

$$
\boxed{
a^3+b^3
=
(a+b)(a^2-ab+b^2).
}
$$

El signo negativo del término central es precisamente el que permite cancelar los términos mixtos.

### Ejemplo

$$
8x^3+27
=
(2x)^3+3^3
=
(2x+3)(4x^2-6x+9).
$$

La expansión verifica el resultado.

## 19.7. Diferencias de potencias y sumas de potencias impares {#apm-c19-s07}

Sea $n\ge1$. Considere

$$
(a-b)
\left(
\sum_{j=0}^{n-1}a^{n-1-j}b^j
\right).
$$

Al distribuir, todos los términos intermedios aparecen una vez con signo positivo y una vez con signo negativo. Se cancelan y queda

$$
a^n-b^n.
$$


**Precisión de lectura.** Cuando $n=1$, el paréntesis de esta identidad contiene un único sumando $1$. Para todos los índices, los monomios de las sumas finitas omiten los factores de exponente cero, como producto vacío de valor uno: no requiere evaluar $0^0$ cuando $a=0$ o $b=0$.

Por tanto,

$$
\boxed{
a^n-b^n
=
(a-b)
\left(
\sum_{j=0}^{n-1}a^{n-1-j}b^j
\right).
}
$$

Para $n=5$,

$$
a^5-b^5
=
(a-b)(a^4+a^3b+a^2b^2+ab^3+b^4).
$$

### Suma de potencias impares

Si $n$ es impar,

$$
\boxed{
a^n+b^n
=
(a+b)
\left(
\sum_{j=0}^{n-1}(-1)^j a^{n-1-j}b^j
\right).
}
$$

Los signos alternan y la expansión vuelve a cancelar los términos intermedios.

Para $n=5$:

$$
a^5+b^5
=
(a+b)(a^4-a^3b+a^2b^2-ab^3+b^4).
$$

No apelamos al teorema del factor. Estas identidades se justifican por distributividad y cancelación finita.

### Varias estructuras simultáneas

$$
x^{12}-y^{12}
$$

puede verse como diferencia de cuadrados, de cubos o de potencias. La mejor lectura depende del objetivo.

## 19.8. Factorización por agrupación {#apm-c19-s08}

Hay expresiones sin factor común global evidente que pueden reorganizarse para producirlo.

Considere

$$
ax+ay+bx+by.
$$

Agrupamos:

$$
(ax+ay)+(bx+by).
$$

Entonces

$$
a(x+y)+b(x+y)
=
(a+b)(x+y).
$$

### La agrupación tiene un objetivo

En

$$
2x^2+6x+x+3,
$$

podemos escribir

$$
(2x^2+6x)+(x+3)
=
2x(x+3)+(x+3)
=
(2x+1)(x+3).
$$

Agrupar sirve porque después aparece un factor común compuesto.

### Reordenar antes de agrupar

$$
x^3+3x^2-4x-12
=
(x^3+3x^2)+(-4x-12)
$$

$$
=
x^2(x+3)-4(x+3)
$$

$$
=
(x+3)(x^2-4)
$$

$$
=
(x+3)(x-2)(x+2).
$$

La agrupación puede ser sólo el primer nivel de una factorización.


## 19.9. Trinomios mónicos: reconstruir suma y producto {#apm-c19-s09}

Partamos de

$$
(x+r)(x+s)
=
x^2+sx+rx+rs
=
x^2+(r+s)x+rs.
$$

Por tanto, factorizar

$$
x^2+bx+c
$$

como producto de dos binomios significa encontrar $r,s$ tales que

$$
r+s=b
$$

y

$$
rs=c.
$$

### Ejemplo

Para

$$
x^2+7x+12,
$$

buscamos dos números cuyo producto sea $12$ y cuya suma sea $7$:

$$
3\cdot4=12,
\qquad
3+4=7.
$$

Así,

$$
x^2+7x+12=(x+3)(x+4).
$$

### Los signos salen de suma y producto

En

$$
x^2-x-12
$$

necesitamos

$$
r+s=-1,
\qquad
rs=-12.
$$

Una pareja adecuada es $r=3$, $s=-4$. Entonces

$$
x^2-x-12=(x+3)(x-4).
$$

No hace falta una tabla de signos separada: las condiciones de suma y producto contienen toda la información.

### Cuando no aparece una pareja

Si dentro del conjunto de coeficientes que estamos explorando no encontramos $r,s$ adecuados, no concluimos todavía una irreducibilidad formal.

Diremos simplemente:

> Con las estructuras elementales y el tipo de coeficientes buscados en este contexto no hemos obtenido una factorización adicional.

La noción precisa de irreducibilidad pertenece a C25.



### Reconstruir suma y producto con un centro

Si buscamos $r+s=S$ y $rs=P$, escribamos $h=S/2$, $r=h+d$ y $s=h-d$. Su producto es $h^2-d^2$. Por tanto, una pareja real exige $P\le h^2$ y se reconstruye con $d=\sqrt{h^2-P}$. La justificación inversa es $(r-s)^2=S^2-4P\ge0$. No estamos aplicando una receta sin comprobarla: la suma y el producto de la pareja obtenida certifican la reconstrucción. Con $S=6$ y $P=5$, $h=3$ y $d=2$, obtenemos $1,5$ y $x^2+6x+5=(x+1)(x+5)$. **Control resuelto:** $S=4$, $P=5$ es imposible en los reales, porque $h^2-P=-1$. No encontrar enteros era insuficiente; la no negatividad del cuadrado descarta aquí toda pareja real.

## 19.10. Trinomios generales: fabricar una agrupación {#apm-c19-s10}

Consideremos

$$
ax^2+bx+c,
\qquad
a\neq0.
$$

Cuando $a\neq1$, una estrategia útil consiste en buscar dos números $m,n$ que satisfagan

$$
m+n=b
$$

y

$$
mn=ac.
$$

Después descomponemos el término medio:

$$
bx=mx+nx,
$$

y usamos agrupación.

### Ejemplo

Factoricemos

$$
6x^2+11x+3.
$$

Tenemos

$$
ac=18.
$$

Buscamos dos números que multipliquen $18$ y sumen $11$:

$$
9+2=11,
\qquad
9\cdot2=18.
$$

Entonces

$$
6x^2+11x+3
=
6x^2+9x+2x+3.
$$

Agrupamos:

$$
(6x^2+9x)+(2x+3)
$$

y obtenemos

$$
3x(2x+3)+1(2x+3).
$$

Por tanto,

$$
\boxed{
6x^2+11x+3=(3x+1)(2x+3).
}
$$

### Por qué aparece el producto $ac$

Si

$$
ax^2+bx+c=(px+q)(rx+s),
$$

entonces

$$
pr=a,
\qquad
qs=c,
$$

y el término medio es

$$
(ps+qr)x.
$$

Los dos productos cruzados son los que descomponen el coeficiente $b$. Su producto es

$$
(ps)(qr)=pr\cdot qs=ac.
$$

Por eso la condición $mn=ac$ organiza la búsqueda de una descomposición compatible con agrupación.

### Inspección o procedimiento

En un caso sencillo como

$$
2x^2+5x+2,
$$

puede verse directamente

$$
(2x+1)(x+2).
$$

Pero cuando la inspección no es inmediata, descomponer el término medio ofrece una ruta sistemática.

En ambos casos, el control final es el mismo:

> Expandir el producto obtenido y comparar término a término con la expresión original.

## 19.11. Cuadrados perfectos y patrones casi correctos {#apm-c19-s11}

Reconocer una forma no consiste en mirar sólo los términos extremos.

Considere

$$
x^2+12x+36.
$$

Los extremos son

$$
x^2
\qquad\text{y}\qquad
6^2.
$$

Para que la expresión sea

$$
(x+6)^2,
$$

el término medio debe ser

$$
2(x)(6)=12x.
$$

Como coincide,

$$
x^2+12x+36=(x+6)^2.
$$

### Un patrón casi correcto

Ahora considere

$$
x^2+10x+36.
$$

Los extremos siguen siendo $x^2$ y $6^2$, pero el término medio correcto para $(x+6)^2$ sería $12x$.

Por tanto,

$$
x^2+10x+36-(x+6)^2=-2x.
$$

No es una identidad de igualdad: los miembros coinciden en $x=0$ y difieren cuando $x\ne0$. La semejanza visual no basta.

### Reconstruir un término faltante

Si deseamos que

$$
x^2+kx+49
$$

sea el cuadrado de $(x+7)$, entonces

$$
(x+7)^2=x^2+14x+49.
$$

Por tanto el término lineal debe ser $14x$.

No estamos resolviendo aquí una ecuación en el sentido de C21. Estamos reconstruyendo una identidad bajo una condición estructural.

### Prueba de estrés

Ante un supuesto cuadrado perfecto:

```text
1. IDENTIFICAR LOS DOS CUADRADOS.
2. TOMAR SUS RAÍCES.
3. CALCULAR EL DOBLE PRODUCTO.
4. COMPARAR CON EL TÉRMINO MEDIO.
5. SÓLO ENTONCES FACTORIZAR.
```

## 19.12. Sustitución auxiliar: nombrar una estructura repetida {#apm-c19-s12}

Algunas expresiones parecen complicadas porque una misma subestructura aparece varias veces.

Considere

$$
x^4-5x^2+4.
$$

Si escribimos

$$
u=x^2,
$$

la expresión se convierte temporalmente en

$$
u^2-5u+4.
$$

Ahora reconocemos un trinomio mónico:

$$
u^2-5u+4=(u-1)(u-4).
$$

Deshacemos la sustitución:

$$
(x^2-1)(x^2-4).
$$

Y volvemos a leer:

$$
x^2-1=(x-1)(x+1),
$$

$$
x^2-4=(x-2)(x+2).
$$

Por tanto,

$$
x^4-5x^2+4
=
(x-1)(x+1)(x-2)(x+2).
$$

### La sustitución no cambia el problema

La letra $u$ no crea un objeto nuevo; nombra temporalmente un bloque para hacer visible una forma conocida.

### Sustituir un bloque compuesto

En

$$
(x+1)^4-5(x+1)^2+4
$$

tomamos

$$
u=(x+1)^2.
$$

Entonces

$$
u^2-5u+4=(u-1)(u-4),
$$

y al regresar:

$$
\big((x+1)^2-1\big)\big((x+1)^2-4\big).
$$

Cada factor puede analizarse de nuevo como diferencia de cuadrados.

### Transferencia desde C18

En el dominio real apropiado puede aparecer

$$
x-5\sqrt{x}+4.
$$

Si $x\ge0$, tomamos

$$
u=\sqrt{x}.
$$

Entonces $x=u^2$ y la expresión queda

$$
u^2-5u+4.
$$

La sustitución no elimina el dominio original $x\ge0$.



### Una sustitución no borra los términos que quedan fuera

En $E=x^4-5x^2+4+x(x^2-1)$, poner $u=x^2$ produce $(u-1)(u-4)+x(u-1)$. La letra $x$ sigue presente: no podemos sustituirla por $u$. Agrupamos y regresamos a la variable original: $E=(x^2-1)(x^2+x-4)$. Expandir devuelve $x^4+x^3-5x^2-x+4$. **Diagnóstico resuelto:** afirmar que toda la expresión depende solo de $u$ pierde información. En $x=2$ y $x=-2$ tenemos el mismo $u=4$, pero $E$ vale $6$ y $-6$. La sustitución auxiliar puede organizar parte de una expresión sin convertirla entera en una expresión de una sola nueva variable. Conservar las dependencias residuales evita reconstrucciones falsas.

## 19.13. Factorizaciones encadenadas {#apm-c19-s13}

En problemas de varias etapas, después de cada transformación debemos volver a leer la nueva forma.

Considere

$$
2x^5-18x.
$$

### Paso 1: factor común

$$
2x^5-18x
=
2x(x^4-9).
$$

### Paso 2: diferencia de cuadrados

$$
x^4-9
=
(x^2)^2-3^2
=
(x^2-3)(x^2+3).
$$

Por tanto,

$$
2x^5-18x
=
2x(x^2-3)(x^2+3).
$$

La forma $2x(x^2-3)(x^2+3)$ cumple el objetivo de hacer visibles estos bloques. Si se pide continuar con factores reales, C18 permite escribir $x^2-3=(x-\sqrt3)(x+\sqrt3)$. Detenerse depende del objetivo declarado; no afirma que todos los factores sean irreducibles.

### Agrupación que revela una nueva identidad

Considere

$$
x^3+2x^2-9x-18.
$$

Agrupamos:

$$
(x^3+2x^2)+(-9x-18).
$$

Luego,

$$
x^2(x+2)-9(x+2)
=
(x+2)(x^2-9)
$$

y finalmente

$$
\boxed{
x^3+2x^2-9x-18
=
(x+2)(x-3)(x+3).
}
$$

### Estrategia recursiva

```text
FACTOR COMÚN
    ↓
VOLVER A LEER
    ↓
IDENTIDAD / AGRUPACIÓN / SUSTITUCIÓN
    ↓
VOLVER A LEER
    ↓
NUEVA FACTORIZACIÓN SI PROCEDE
    ↓
VERIFICAR
```

No debemos “seguir factorizando” por inercia. Nos detenemos cuando el objetivo está cumplido y ninguna estructura del marco actual ofrece una continuación justificada.

## 19.14. Elegir entre forma expandida y forma factorizada {#apm-c19-s14}

Considere

$$
(x-2)(x+5)
=
x^2+3x-10.
$$

Las dos formas son equivalentes, pero hacen visible información diferente.

### Forma expandida

$$
x^2+3x-10
$$

muestra con claridad:

- los términos;
- los coeficientes;
- la contribución lineal;
- la facilidad para sumar con otra expresión expandida.

### Forma factorizada

$$
(x-2)(x+5)
$$

muestra:

- dos factores;
- una estructura multiplicativa;
- una forma que será útil en capítulos posteriores.

### Elegir forma por función

Si debemos sumar esta expresión con

$$
-x^2+4x+1,
$$

puede convenir expandir.

Si debemos compararla con otra expresión que contiene $(x-2)$, puede convenir conservar la factorización.

Si una expresión ya aparece como

$$
(x+3)(x^2-4),
$$

expandir de inmediato oculta que

$$
x^2-4=(x-2)(x+2).
$$

### Previsión algebraica

La pregunta experta no es:

> ¿Qué operación puedo hacer ahora?

sino:

> ¿Qué forma quiero obtener y qué información necesito que quede visible?

En C20, la forma factorizada ayudará a leer expresiones racionales. En C21, ayudará a estudiar ecuaciones. Aquí sólo preparamos esas representaciones: todavía no cancelamos factores en cocientes ni resolvemos ecuaciones por producto nulo.



### Comparar rutas sin dividir por un parámetro

Para $E=(x+a)(x+b)-(x+a)(x+c)$, extraer el bloque compartido da $E=(x+a)[(x+b)-(x+c)]=(b-c)(x+a)$. Expandir primero da $(b-c)x+a(b-c)$, que verifica la misma identidad. La primera ruta conserva un factor y reduce la resta a una constante; la segunda facilita comparar coeficientes. **Control resuelto:** si $b=c$, ambas representaciones dan cero para todo $x$. Dividir por $b-c$ para «comprobar» habría eliminado precisamente ese caso. Una identidad paramétrica debe verificarse también donde algún factor se anula; la distributividad funciona allí sin divisiones. La forma final se elige por su propósito, no por una preferencia automática por productos.

## 19.15. Laboratorio P3: localizar el primer patrón falso {#apm-c19-s15}

Las cadenas largas plantean un peligro especial: un error temprano puede quedar oculto por pasos posteriores que, considerados aisladamente, parecen familiares.

Considere

$$
(x+3)^2
=
x^2+9
=
(x-3)(x+3).
$$

El primer error ocurre en

$$
(x+3)^2=x^2+9.
$$

La expansión correcta es

$$
(x+3)^2=x^2+6x+9.
$$

La cadena queda rota desde esa primera igualdad falsa.

### Segundo ejemplo

$$
x^2-6x+9
=
(x-3)^2
=
x^2-9.
$$

El primer paso es correcto. El segundo es falso:

$$
(x-3)^2-(x^2-9)=18-6x.
$$

No es una identidad, aunque los dos miembros coinciden en $x=3$. Se confundió el cuadrado de una diferencia con una diferencia de cuadrados.

### Agrupación aparente

La cadena

$$
2x^2+5x+3
=
(2x^2+2x)+(3x+3)
$$

$$
=
2x(x+1)+3(x+1)
$$

$$
=
(2x+3)(x+1)
$$

es correcta.

En cambio, si escribimos

$$
2x^2+5x+3
=
(2x^2+x)+(4x+3),
$$

la primera igualdad sigue siendo válida, pero

$$
x(2x+1)+(4x+3)
$$

no posee el factor común $(2x+1)$. El error sería inventar después una factorización que la expresión no contiene.

### Protocolo de auditoría

```text
1. LEER SIN CORREGIR.
2. LOCALIZAR LA PRIMERA IGUALDAD FALSA.
3. IDENTIFICAR LA LEY QUE SE INTENTÓ USAR.
4. EXPLICAR QUÉ ESTRUCTURA FALTABA.
5. VOLVER AL ÚLTIMO PASO VÁLIDO.
6. RECONSTRUIR LA CADENA.
7. VERIFICAR POR UNA RUTA INDEPENDIENTE.
```

### Por qué los errores son plausibles

La falsa igualdad

$$
(a+b)^2=a^2+b^2
$$

imita una ley verdadera:

$$
(ab)^2=a^2b^2.
$$

Por eso la corrección no debe limitarse a “eso está mal”. Hay que identificar si tenemos:

- potencia de un producto;
- potencia de una suma;
- diferencia de cuadrados;
- cuadrado de una diferencia.

Aprender álgebra implica clasificar la forma antes de elegir la ley.

## 19.16. Cierre: un protocolo de reconocimiento y factorización {#apm-c19-s16}

A lo largo del capítulo hemos usado varias identidades, pero el objetivo no era acumular fórmulas.

Todo el trabajo puede organizarse alrededor de tres movimientos:

$$
\boxed{
\text{leer}
\longrightarrow
\text{reconstruir}
\longrightarrow
\text{verificar}
}
$$

### Leer

Antes de transformar:

- ¿cuántos términos hay?;
- ¿hay factor común?;
- ¿veo cuadrados, cubos o potencias repetidas?;
- ¿hay un bloque que aparece varias veces?;
- ¿una agrupación podría crear un factor común?;
- ¿la expresión hereda restricciones de dominio desde C18?

### Reconstruir

Elegimos la herramienta según la forma:

- distributividad inversa;
- diferencia de cuadrados;
- cuadrados perfectos;
- suma o diferencia de cubos;
- diferencia general de potencias;
- agrupación;
- trinomios;
- sustitución auxiliar.

### Volver a leer

Después de cada paso preguntamos:

> ¿La nueva forma revela otra estructura?

Una factorización puede abrir la puerta a otra.

### Verificar

Cuando haya riesgo de error:

$$
\text{factorización propuesta}
\longrightarrow
\text{expansión}
\longrightarrow
\text{comparación}.
$$

### Elegir la forma final

No existe una forma universalmente superior.

La forma expandida puede ser mejor para comparar y combinar términos. La forma factorizada puede revelar estructura. Una sustitución puede hacer visible un patrón.

### Protocolo final

```text
1. ¿HAY FACTOR COMÚN?
2. ¿QUÉ FORMA GLOBAL TIENE LA EXPRESIÓN?
3. ¿HAY DOS TÉRMINOS, TRES, CUATRO O UN BLOQUE REPETIDO?
4. ¿RECONOZCO CUADRADOS, CUBOS O DIFERENCIAS DE POTENCIAS?
5. ¿UNA AGRUPACIÓN CREA UN FACTOR COMÚN?
6. ¿UN TRINOMIO PUEDE LEERSE COMO PRODUCTO DE BINOMIOS?
7. ¿CONVIENE UNA SUSTITUCIÓN AUXILIAR?
8. ¿LA NUEVA FORMA ADMITE OTRA ETAPA?
9. ¿CÓMO VERIFICO LA IDENTIDAD?
10. ¿QUÉ FORMA SIRVE MEJOR PARA LA TAREA SIGUIENTE?
```

### La idea que debe permanecer

Factorizar no consiste en reconocer dibujos familiares de manera automática. Consiste en **hacer visible una estructura multiplicativa y justificar que realmente estaba allí**.

En el próximo capítulo esa habilidad adquirirá una responsabilidad nueva. Cuando las expresiones aparezcan en cocientes, ya no bastará con reconocer factores: habrá que controlar también qué valores estaban excluidos antes de cualquier simplificación.

La forma seguirá importando, pero el dominio volverá al primer plano.

***
# Ejercicios

Los 80 ejercicios iniciales conservan su procedencia y organización por función cognitiva. El suplemento añade 12 tareas con soluciones y procedencia interna explícita; el banco completo contiene 92 ejercicios. Los problemas de reconocimiento exigen leer antes de transformar; los de fluidez técnica deben verificarse cuando la expansión sea útil; los de justificación y diagnóstico requieren argumentar, y los problemas avanzados combinan varias decisiones. **No se solicita resolver ecuaciones ni simplificar fracciones algebraicas:** esas tareas pertenecen a capítulos posteriores.

## A. Reconocimiento y lectura estructural


**1.** **Nivel A.** Sin efectuar cálculos completos, clasifique cada tarea como **expansión**, **factorización** o **verificación de una identidad**: (a) transformar $(x+2)(x-5)$ en suma; (b) transformar $6x^2+9x$ en producto; (c) comprobar que $x^2-16=(x-4)(x+4)$; (d) recuperar un producto a partir de $a^2+2ab+b^2$. Explique qué información revelaría la forma buscada.


**2.** **Nivel A.** En $18x^3y^2-12x^2y^3+6xy$, identifique el factor numérico, las potencias de variables comunes y el factor común conjunto. Escriba **sólo la forma que espera obtener**, indicando cómo verificaría después su elección.


**3.** **Nivel A.** Asocie cada expresión con una identidad candidata, sin factorizar todavía: (a) $p^2-49$; (b) $p^2+14p+49$; (c) $8p^3+27$; (d) $p^2+49$; (e) $p^4-16$. Señale cuál no comparte el patrón elemental de diferencia de cuadrados y cuál admite más de una lectura.


**4.** **Nivel A.** Examine $9x^2-25$, $9x^2+25$, $9x^2+30x+25$ y $9x^2-30x+25$. Para cada una, decida si reconoce diferencia de cuadrados, cuadrado perfecto u otra forma; justifique en una frase el papel del signo y del término medio.


**5.** **Nivel A.** Explique, sin desarrollar un producto largo, por qué $(-a)^2$, $-a^2$, $(a-b)^2$ y $a^2-b^2$ no representan en general el mismo objeto algebraico. Para las dos últimas, indique qué identidad habría que consultar.


**6.** **Nivel A.** Para cada trinomio $x^2+7x+10$, $x^2-x-12$ y $x^2-8x+15$, indique qué suma y qué producto deben satisfacer dos números $r,s$ para obtener $(x+r)(x+s)$. Todavía no complete la factorización.


**7.** **Nivel A.** En $x^3+4x^2-9x-36$, proponga dos agrupaciones de términos que merezca examinar. Anticipe qué factor compuesto debería aparecer para que una de ellas resulte útil; no es necesario desarrollar toda la factorización.


**8.** **Nivel A.** Indique una sustitución auxiliar natural para (a) $x^6-7x^3+10$ y (b) $(2x-1)^4-5(2x-1)^2+4$. Explique qué patrón aparecería y cómo habría que regresar a la variable original.


**9.** **Nivel A.** Elija **expandir**, **factorizar** o **conservar** para cada propósito: (a) leer coeficientes de $(x-3)(2x+1)$; (b) mostrar factores de $x^2-9$; (c) detectar rápidamente un factor común en $(x+1)(x-2)+4(x+1)$; (d) comparar términos de dos expresiones ya desarrolladas. Justifique cada elección.


**10.** **Nivel A.** En el dominio real de $x^{3/2}-x^{1/2}$, identifique el factor visible y la condición sobre $x$ que debe examinarse antes de manipular exponentes. Explique por qué una factorización posterior debe conservar esa información.

## B. Fluidez técnica


**11.** **Nivel B.** Expanda y reúna términos semejantes: $(3x-2)(2x+5)$. Anote al lado de cada término su procedencia en la distributividad.


**12.** **Nivel B.** Expanda $(x-2y)(x+3y)$ y explique qué dos productos originan el coeficiente de $xy$.


**13.** **Nivel B.** Expanda y simplifique $(2x-y+3)(x+2y)$. Organice el cálculo para evitar perder los signos.


**14.** **Nivel B.** Extraiga primero el mayor factor común evidente de $24x^4y^2-36x^3y^3+12x^2y^2$. Compruebe por expansión la expresión obtenida.


**15.** **Nivel B.** Extraiga deliberadamente un factor común **negativo** de $-4x^3+12x^2-8x$ para que el primer término del paréntesis sea positivo. Justifique los tres signos interiores.


**16.** **Nivel B.** Desarrolle $(3a-2b)^2$ y $(x+4)^2$ desde productos de binomios, no mediante la cita aislada de una fórmula.


**17.** **Nivel B.** Factorice $16x^2-81y^2$ y verifique el resultado multiplicando los factores.


**18.** **Nivel B.** Factorice $x^8-1$ aplicando sucesivamente diferencias de cuadrados mientras encuentre un nuevo patrón estudiado; escriba las etapas y compruebe al menos la primera multiplicación.


**19.** **Nivel B.** Factorice $27a^3+8b^3$ usando una identidad cúbica. Reconstruya los signos del segundo factor por expansión.


**20.** **Nivel B.** Factorice $64x^3-125$ y verifique que los términos mixtos se cancelan.


**21.** **Nivel B.** Factorice $x^3+4x^2-9x-36$ por agrupación y examine si el segundo factor admite otra identidad.


**22.** **Nivel B.** Factorice $6xy-9x+4y-6$ mediante una agrupación que produzca el mismo binomio dos veces.


**23.** **Nivel B.** Factorice $x^2-9x+20$ reconstruyendo dos números mediante su suma y su producto.


**24.** **Nivel B.** Factorice $x^2+2x-35$ y verifique por expansión que los signos son correctos.


**25.** **Nivel B.** Factorice $6x^2+13x+6$ descomponiendo el término medio y agrupando. Indique la pareja elegida y por qué su producto es $6\cdot6$.


**26.** **Nivel B.** Factorice $12x^2-7x-10$ por el método $ac$. Compruebe explícitamente tanto el coeficiente lineal como el término constante.

## C. Justificación y reconstrucción


**27.** **Nivel C.** Demuestre $(a+b)(c+d)=ac+ad+bc+bd$ mediante dos aplicaciones de distributividad. Lea después su igualdad en sentido inverso e indique qué información debe reconocerse para factorizar.


**28.** **Nivel C.** Reconstruya desde $(a-b)(a-b)$ la identidad del cuadrado de una diferencia. Señale los dos términos cruzados y construya un contraejemplo a $(a-b)^2=a^2-b^2$.


**29.** **Nivel C.** Obtenga $(a+b)^3$ por distributividad y explique por qué sus coeficientes son $1,3,3,1$. Compare el mecanismo con el teorema del binomio ya disponible en C13.


**30.** **Nivel C.** Derive $a^2-b^2=(a-b)(a+b)$ mediante expansión. Explique por qué la misma operación no justifica $a^2+b^2=(a-b)(a+b)$ y exhiba un contraejemplo numérico.


**31.** **Nivel C.** Demuestre por expansión tanto $a^3-b^3=(a-b)(a^2+ab+b^2)$ como $a^3+b^3=(a+b)(a^2-ab+b^2)$. Identifique exactamente qué pares de términos se cancelan.


**32.** **Nivel C.** Para cada entero $n\ge1$, demuestre mediante distributividad y cancelación telescópica la identidad $a^n-b^n=(a-b)\sum_{j=0}^{n-1}a^{n-1-j}b^j$. Incluya explícitamente el caso $n=1$ y explique el papel de los índices extremos.


**33.** **Nivel C.** Sea $n=2k+1$ impar positivo. Sustituya $b$ por $-b$ en la identidad del ejercicio anterior para derivar $a^n+b^n$. Justifique la alternancia de signos y compruebe la fórmula para $n=3$ y $n=5$.


**34.** **Nivel C.** Demuestre en ambos sentidos: $x^2+bx+c=(x+r)(x+s)$ **si y sólo si** $b=r+s$ y $c=rs$, suponiendo igualdad de expresiones en $x$ para todos los reales. Justifique la comparación de coeficientes usando valores adecuados de $x$ o expansión y una identidad elemental.


**35.** **Nivel C.** Explique por qué, si $a\neq0$, $m+n=b$ y $mn=ac$, se obtiene $ax^2+bx+c=\frac1a(ax+m)(ax+n)$. Derive de esta identidad el método de descomposición del término medio y agrupe un ejemplo original.


**36.** **Nivel C.** Verifique por **dos rutas** la identidad $x^3+5x^2-4x-20=(x+5)(x-2)(x+2)$: primero por agrupación y luego expandiendo el producto propuesto. Indique qué controla cada ruta.


**37.** **Nivel C.** Muestre que $2x(x+1)=x(2x+2)=2x^2+2x$ para todo real $x$. ¿En qué difieren las tres formas y qué enseña el ejemplo acerca de la elección de representación?


**38.** **Nivel C.** Factorice $x^{3/2}-x^{1/2}$ como $\sqrt{x}(x-1)$ en su dominio real $x\ge0$: justifique la identidad para $x>0$ mediante leyes de potencias y verifique $x=0$ por separado. Explique por qué no debe perderse la información de dominio.

## D. Diagnóstico del primer paso inválido


**39.** **Nivel D.** Audite la cadena $(a+b)^2=a^2+b^2=(a-b)(a+b)$. Localice **la primera** igualdad inválida, nombre la ley que se intentó usar, corrija desde el último punto válido y dé un contraejemplo.


**40.** **Nivel D.** Audite $(x-4)^2=x^2-16=(x-4)(x+4)$. Determine el primer paso inválido, distinga cuadrado de diferencia de diferencia de cuadrados y reconstruya una identidad verdadera.


**41.** **Nivel D.** Audite $a^2+b^2=(a+b)(a-b)=a^2-b^2$. Identifique el primer paso inválido y explique por qué la segunda igualdad, tomada aisladamente, sí es correcta.


**42.** **Nivel D.** Audite $(a+b)^3=a^3+b^3=(a+b)(a^2-ab+b^2)$. Señale el primer error y explique cómo una igualdad posterior correcta puede ocultarlo.


**43.** **Nivel D.** En la cadena $x^3+8=(x+2)(x^2+2x+4)=x^3+8$, identifique el primer patrón falso. Reconstruya la identidad correcta de suma de cubos y compruébela expandiendo.


**44.** **Nivel D.** En $x^3-8=(x-2)(x^2-2x+4)=x^3-8$, detecte el primer error de signo y escriba la factorización corregida con comprobación.


**45.** **Nivel D.** Un estudiante escribe $6x^2+9x=3x(2x+9)=6x^2+27x$. Localice la primera ruptura, explique el papel del coeficiente residual y repare la cadena.


**46.** **Nivel D.** Examine $-x^2+5x-6=-(x^2+5x-6)=-(x+2)(x+3)$. Determine la primera igualdad falsa y reconstruya una extracción correcta del factor $-1$, sin resolver ninguna ecuación.


**47.** **Nivel D.** La cadena $x^2+7x+10=(x+2)(x+5)=(x+2)(x-5)$ contiene un paso correcto seguido por uno falso. Localice el primero que falla, nombre el cambio de estructura y verifique la reparación.


**48.** **Nivel D.** Audite $6x^2+11x+3=6x^2+6x+5x+3=6x(x+1)+(5x+3)=(x+1)(6x+3)$. Identifique la primera igualdad inválida y elija una descomposición del término medio que sí produzca agrupación útil.


**49.** **Nivel D.** Un estudiante declara $x^4-5x^2+4=u^2-5u+4$ con $u=x$ y concluye $(u-1)(u-4)$. Determine el primer error en la sustitución, elija el bloque correcto y regrese a $x$ sin resolver ecuaciones.


**50.** **Nivel D.** Audite, en el dominio $x\ge0$, $x^{3/2}-x^{1/2}=x^{1/2}(x+1)=\sqrt{x}(x+1)$. Localice el primer error, compárelo con la distributividad verdadera y explique cómo verificar la reparación en $x=0$.

## E. Estrategia y elección de representación


**51.** **Nivel E.** En $(x+2)(x-3)+(x+2)(2x+1)$, decida entre expandir ambos productos o extraer primero un factor compuesto. Ejecute la ruta elegida, compare con la otra y explique qué estrategia evita más trabajo.


**52.** **Nivel E.** Compare $x^4-16$ con $x^4+16$. Identifique las diferencias estructurales que justifican o impiden aplicar directamente la diferencia de cuadrados, y describa hasta dónde llega una factorización elemental sin declarar irreducibilidad.


**53.** **Nivel E.** Factorice $6x^2+11x+3$ de dos maneras: (i) inspección del producto de binomios; (ii) método $ac$ y agrupación. Compare qué pista ofrece cada procedimiento y verifique expandiendo.


**54.** **Nivel E.** Elija y justifique el orden de técnicas para $8x^3+12x^2+4x$: factor común, trinomio o expansión. Factorice por etapas y explique por qué conviene volver a leer después del primer paso.


**55.** **Nivel E.** Para comparar $x^2+2x+1$ con $(x-1)(x+1)+2x+2$, elija una forma común y establezca por una cadena de identidades si son iguales. ¿Por qué esa representación es mejor para esta tarea?


**56.** **Nivel E.** Construya un trinomio con extremos $x^2$ y $16$ que **no** sea cuadrado perfecto y explique cómo corregir su término medio para obtener $(x+4)^2$. Distinga reconocer extremos de verificar el doble producto.


**57.** **Nivel E.** Factorice $x^3-2x^2+3x-6$ por dos agrupaciones distintas. Argumente qué factor común pretende fabricar cada una y por qué ambas conducen a la misma identidad.


**58.** **Nivel E.** Determine una sustitución conveniente para $(x-2)^4-5(x-2)^2+4$. Factorice, deshaga la sustitución y explique en qué momento debe revisarse una nueva diferencia de cuadrados.


**59.** **Nivel E.** Proponga dos rutas para comenzar la factorización de $a^6-b^6$ —como diferencia de cuadrados y como diferencia de cubos—. Desarrolle ambas hasta obtener productos equivalentes y compruebe la equivalencia por identidades, sin usar el teorema del factor.


**60.** **Nivel E.** Para $(x^2+9)(x^2-9)+3(x^2+9)$, decida si conviene expandir o factorizar primero. Obtenga una forma estructuralmente útil y compruebe por expansión sin sostener que una representación sea superior para toda tarea.

## F. Transferencia acumulativa


**61.** **Nivel F.** En el dominio $x\ge0$, factorice $x^{5/2}-4x^{3/2}+3x^{1/2}$ mediante factor común y un trinomio. Justifique para $x>0$ las leyes de potencias y controle por separado $x=0$.


**62.** **Nivel F.** Con $x>0$, use la sustitución $u=x^{2/3}$ para factorizar $x^{4/3}-5x^{2/3}+4$. Regrese a exponentes racionales y explique qué hipótesis permiten esas transformaciones.


**63.** **Nivel F.** Para $x\ge0$, factorice $\sqrt{x}(x-4)+2\sqrt{x}(x+1)$ por factor común compuesto. Verifique por distributividad y declare el dominio original.


**64.** **Nivel F.** Derive una forma factorizada de $(u+v)^3+(u-v)^3$ por expansión controlada; compárela con una ruta que extraiga primero un factor común después de reagrupar. Verifique ambas para cualesquiera $u,v\in\mathbb R$.


**65.** **Nivel F.** Factorice $x^6-1$ por dos rutas: (i) empiece con la diferencia de cuadrados $(x^3)^2-1^2$ y después use suma y diferencia de cubos; (ii) empiece con la diferencia de cubos $(x^2)^3-1^3$ y reconstruya las identidades restantes. Compare los productos por expansión.


**66.** **Nivel F.** Deduzca la factorización de $x^7+2^7$ usando la suma de potencias impares. Escriba todos los signos, compruebe los dos términos extremos y explique por qué se cancelan los intermedios.


**67.** **Nivel F.** Use $u=x^2$ para factorizar $x^4-10x^2+9$. Deshaga la sustitución y aplique las diferencias de cuadrados restantes. Verifique por expansión.


**68.** **Nivel F.** Factorice $(x+1)^4-10(x+1)^2+9$ mediante una sustitución para el bloque repetido. Deshaga la sustitución con cuidado y explique por qué expandir de entrada sería más costoso.


**69.** **Nivel F.** Reconozca un cuadrado perfecto dentro de $9x^2-6xy+y^2-25z^2$; convierta luego la expresión en diferencia de cuadrados. Verifique el producto obtenido mediante una ruta independiente.


**70.** **Nivel F.** Sea $k\in\mathbb R$. Verifique para todo $x$ la identidad $x^3+(k+2)x^2+(2k-3)x-3k=(x+k)(x+3)(x-1)$. Reconstruya una factorización por agrupación y explique qué papel desempeña el parámetro.


**71.** **Nivel F.** Factorice $12x^3-27x$ por al menos dos rutas: (i) factor común seguido de identidad; (ii) reconocimiento de la diferencia de cuadrados dentro de un factor común alternativo. Compare y verifique.


**72.** **Nivel F.** Compare las factorizaciones de $4x^4-20x^2+16$ obtenidas por (i) extracción inicial de $4$ y sustitución $u=x^2$, y (ii) agrupación de una diferencia de cuadrados construida. Justifique cada paso sin apelar a raíces de ecuaciones.

## G. Síntesis avanzada


**73.** **Nivel G.** **Auditoría de cuatro etapas.** Factorice $2x^4+6x^3-18x^2-54x$ empezando por factor común, continuando por agrupación, identificando una diferencia de cuadrados y releyendo los factores resultantes. Escriba la razón de cada paso, verifique la forma final por expansión y compare con una ruta que agrupe antes de extraer todo el factor común.


**74.** **Nivel G.** **Identidad paramétrica.** Para $a,b\in\mathbb R$, demuestre $(a+b)^4-(a-b)^4=8ab(a^2+b^2)$ mediante (i) dos diferencias de cuadrados encadenadas y (ii) expansión binomial. Explique qué cancelaciones producen el resultado y compare las dos arquitecturas de prueba.


**75.** **Nivel G.** **Diferencia general de potencias.** Demuestre la identidad de $a^n-b^n$ para todo $n\ge1$ mediante una suma finita explícita. Aplíquela a $x^{10}-1$ de dos maneras (exponente $10$ y diferencia de quintas potencias de $x^2$ y $1$); compare los factores obtenidos sin invocar teorema del factor ni irreducibilidad.


**76.** **Nivel G.** **Suma de potencias impares.** Sea $n=2k+1$. Derive la identidad general desde la diferencia de potencias y aplíquela a $x^7+1$. Justifique los signos de los siete términos del segundo factor y verifique la factorización mediante cancelación telescópica.


**77.** **Nivel G.** **Trinomio general de alta carga.** Factorice $18x^2-21x-15$ (i) extrayendo primero el factor numérico y usando el método $ac$ y (ii) descomponiendo directamente el término medio antes de agrupar. Compare el número de pasos, explique la selección de sumandos y verifique por expansión.


**78.** **Nivel G.** **Sustitución estructural.** Factorice $\big(x^2+2x\big)^2-2\big(x^2+2x\big)-3$ sin resolver ecuaciones: nombre el bloque repetido, factorice el trinomio auxiliar, deshaga la sustitución y examine cada factor nuevamente. Construya una segunda verificación por expansión.


**79.** **Nivel G.** **Auditoría extensa de cadena.** Examine línea por línea la cadena siguiente. Localice **la primera igualdad falsa**, aunque las transformaciones posteriores sean correctas a partir de la expresión equivocada. Explique por qué el error era plausible y reconstruya desde el último paso válido una factorización verdadera; compruebe ambos productos por expansión.

$$
\begin{aligned}
\text{(1)}\quad E&=x^4+5x^3-4x^2-20x,\\
\text{(2)}\quad &=x(x^3+5x^2-4x-20),\\
\text{(3)}\quad &=x\big[(x^3+5x^2)+(-4x-20)\big],\\
\text{(4)}\quad &=x\big[x^2(x+5)-4(x+5)\big],\\
\text{(5)}\quad &=x(x+5)(x^2-4),\\
\text{(6)}\quad &=x(x+5)(x-2)(x+2),\\
\text{(7)}\quad &=x(x+5)(x-2)^2,\\
\text{(8)}\quad &=(x^2+5x)(x-2)^2,\\
\text{(9)}\quad &=(x^2+5x)(x^2-4x+4),\\
\text{(10)}\quad &=x^4+x^3-16x^2+20x,\\
\text{(11)}\quad &=x(x^3+x^2-16x+20),\\
\text{(12)}\quad &=x\big[(x^3+x^2)+(-16x+20)\big],\\
\text{(13)}\quad &=x\big[x^2(x+1)-4(4x-5)\big].
\end{aligned}
$$


**80.** **Nivel G.** **Síntesis MA-PED completa.** Considere, para $x\in\mathbb R$,

$$
E(x)=(x+1)^4-5(x+1)^2+4+3(x+1)\big((x+1)^2-1\big).
$$

Redacte una solución que distinga expresamente: **(1)** lectura de bloques y objetivo; **(2)** estrategia de sustitución $u=x+1$ frente a expansión inmediata; **(3)** identidad que revela el factor común; **(4)** mecanismo de reconstrucción del trinomio y de sus diferencias de cuadrados; **(5)** ejecución técnica de una factorización de varias etapas; **(6)** verificación independiente mediante expansión; **(7)** comparación con una segunda ruta que expanda primero; **(8)** cierre sobre qué información hace visible cada forma. No resuelva la ecuación $E(x)=0$ ni emplee teoría posterior.

***
## H. Profundización y reconstrucción

Intente cada tarea antes de consultar su solución. Los parámetros son reales salvo indicación distinta.



#### Ejercicio 081. Factorización paramétrica por reconstrucción

Para cada $t\in\mathbb R$, factorice $x^4+(t-1)x^2-t$ y explique qué ocurre en $t=-1$ y $t=0$. Verifique sin dividir por $t$.



#### Ejercicio 082. Un parámetro que anula toda una identidad

Simplifique $(tx+1)^2-(x+t)^2$ y determine todos los $t$ para los que es cero para todo real $x$.



#### Ejercicio 083. Una diferencia de productos que no depende de la variable

Pruebe que $(x+a)(x+b)-(x+a+h)(x+b-h)$ es constante en $x$. Clasifique cuándo es idénticamente cero.



#### Ejercicio 084. Construir factores enteros consecutivos

Caracterice todos los trinomios $x^2+Bx+C$ que se escriben $(x+r)(x+r+1)$ con $r\in\mathbb Z$.



#### Ejercicio 085. Diseñar un producto simétrico

Determine para qué $A\in\mathbb R$ existe $u\in\mathbb R$ tal que $x^4+Ax^2+1=(x^2+ux+1)(x^2-ux+1)$ para todo $x$; dé todos los $u$.



#### Ejercicio 086. Una familia cúbica diseñada por sus factores

Construya todos los productos $(x+a)^2(x+b)$ cuyo término en $x^2$ sea cero. Expanda y conserve el caso $a=0$.



#### Ejercicio 087. Expandir para certificar una propiedad aritmética

Para $n\in\mathbb Z$, simplifique $(n+1)^4-2n^4+(n-1)^4$. Pruebe que siempre es positivo y par, pero nunca múltiplo de $4$.



#### Ejercicio 088. Paridad visible en una diferencia de cuadrados

Para enteros $x,a,b$, estudie la paridad de $(x+a)^2-(x+b)^2$. Pruebe que es múltiplo de $4$ si $a,b$ tienen igual paridad y que es impar si tienen paridad distinta.



#### Ejercicio 089. Un cuadrado oculto entre cuatro consecutivos

Pruebe para todo entero $n$ que $n(n+1)(n+2)(n+3)+1$ es un cuadrado entero. Compare una agrupación y una expansión.



#### Ejercicio 090. Reparar un patrón casi cuadrado

Compare $x^4+(a^2+b^2)x^2+a^2b^2$ con $(x^2+ab)^2$. Halle su diferencia y determine cuándo coinciden para todo $x$ real.



#### Ejercicio 091. Certificar una identidad cúbica sin suponer los coeficientes

Determine $b,c$ en función de $a$ para que $(x-a)(x^2+bx+c)=x^3-a^3$ para todo real $x$. Justifique también la necesidad.



#### Ejercicio 092. Reparar y especializar una identidad de tres variables

Determine $\lambda$ para que $a^3+b^3+c^3+\lambda abc=(a+b+c)(a^2+b^2+c^2-ab-ac-bc)$ para todos los reales. Factorice después la especialización $c=b$.

# Soluciones razonadas

En cada solución distinguimos la estructura reconocida de la ley que permite transformarla. Cuando se propone una factorización, la expansión proporciona un control independiente; cuando intervienen radicales o exponentes racionales, se conserva el dominio original. Una identidad no se convierte aquí en un problema de resolución de ecuaciones.

## A. Reconocimiento y lectura estructural


### Solución 1

(a) **Expansión**: $(x+2)(x-5)$ debe pasar de producto a suma para mostrar términos y coeficientes. (b) **Factorización**: $6x^2+9x$ debe pasar de suma a producto para exhibir el factor $3x$. (c) **Verificación**: se multiplica $(x-4)(x+4)$ y se compara con $x^2-16$. (d) **Factorización por cuadrado perfecto**: $a^2+2ab+b^2=(a+b)^2$ muestra una sola estructura cuadrada. La clasificación depende de la *tarea*, no de la apariencia aislada de los símbolos.


### Solución 2

El factor numérico común es $6$. Las menores potencias de las variables presentes en los tres términos son $x^1$ e $y^1$; el factor conjunto es, por tanto, $6xy$. La forma anticipada es

$$
18x^3y^2-12x^2y^3+6xy=6xy(3x^2y-2xy^2+1).
$$

Para verificarla, se distribuye $6xy$ sobre los tres sumandos: deben reaparecer exactamente los tres términos originales. El último sumando interior es $1$, no $0$.


### Solución 3

(a) $p^2-49=p^2-7^2$: diferencia de cuadrados. (b) $p^2+14p+49$: candidato a $(p+7)^2$, porque $14p=2p\cdot7$. (c) $8p^3+27=(2p)^3+3^3$: suma de cubos. (d) $p^2+49$: **suma**, no diferencia, de cuadrados; no admite directamente la identidad de (a). (e) $p^4-16=(p^2)^2-4^2$: diferencia de cuadrados; también puede verse como $(p^4)-(2^4)$, diferencia de cuartas potencias. El caso (e) admite varias lecturas y una segunda diferencia de cuadrados tras el primer paso.


### Solución 4

$9x^2-25=(3x)^2-5^2$ es diferencia de cuadrados. $9x^2+25$ es suma de cuadrados, sin la misma identidad directa. $9x^2+30x+25=(3x+5)^2$: el término medio coincide con $2(3x)(5)$. Finalmente $9x^2-30x+25=(3x-5)^2$: el signo negativo corresponde a $-2(3x)(5)$. La presencia de extremos cuadrados **no basta** para reconocer un cuadrado perfecto: es necesario comprobar el término medio.


### Solución 5

$(-a)^2=a^2$, mientras que $-a^2=-(a^2)$; por ejemplo, para $a=2$ son $4$ y $-4$. Además,

$$
(a-b)^2=a^2-2ab+b^2,
\qquad a^2-b^2=(a-b)(a+b).
$$

La primera es el **cuadrado de una diferencia**; la segunda, una **diferencia de cuadrados**. Para $a=3,b=1$ valen $4$ y $8$, respectivamente. La posición de los paréntesis y el término cruzado deciden qué identidad consultar.


### Solución 6

La regla de lectura es $(x+r)(x+s)=x^2+(r+s)x+rs$. Para $x^2+7x+10$ se requiere $r+s=7$ y $rs=10$; para $x^2-x-12$, $r+s=-1$ y $rs=-12$; para $x^2-8x+15$, $r+s=-8$ y $rs=15$. Son las condiciones buscadas; no se necesita completar las factorizaciones en esta etapa de reconocimiento.


### Solución 7

Una agrupación es $(x^3+4x^2)+(-9x-36)$: se anticipa $x^2(x+4)-9(x+4)$, de modo que aparece $(x+4)$. Otra es $(x^3-9x)+(4x^2-36)$: se anticipa $x(x^2-9)+4(x^2-9)$, que produce $(x^2-9)$. Ambas agrupaciones son legítimas; anticipar *qué factor aparecerá* hace que la selección sea estratégica.


### Solución 8

(a) Sea $u=x^3$. Entonces $x^6-7x^3+10$ se lee como $u^2-7u+10$: un trinomio mónico. (b) Sea $u=(2x-1)^2$. Entonces aparece $u^2-5u+4$. Primero se analiza el trinomio en $u$; después se sustituye de vuelta el bloque exacto, $x^3$ o $(2x-1)^2$, y se inspeccionan los factores resultantes por si esconden diferencias de cuadrados. La sustitución sólo *nombra* una estructura; no autoriza olvidar su definición.


### Solución 9

(a) **Expandir** $(x-3)(2x+1)$ para leer los coeficientes de $2x^2-5x-3$. (b) **Factorizar** $x^2-9$ como $(x-3)(x+3)$ para exhibir los factores. (c) **Conservar la estructura y extraer** $(x+1)$: $(x+1)[(x-2)+4]=(x+1)(x+2)$; expandir primero sería trabajo innecesario. (d) **Conservar las formas desarrolladas** para comparar término a término, tras reunir los términos semejantes si hace falta. La finalidad decide la representación.


### Solución 10

En $\mathbb R$, $x^{1/2}=\sqrt x$ exige $x\ge0$; ése es también el dominio de $x^{3/2}$. Para $x>0$, $x^{3/2}=x\,x^{1/2}$, por lo que el factor esperado es $x^{1/2}$ y la forma $\sqrt x(x-1)$. En $x=0$ ambas expresiones valen $0$, de modo que la identidad se extiende al dominio original. La forma factorizada debe seguir interpretándose en $x\ge0$: la manipulación no asigna valores reales a la expresión original para $x<0$.

## B. Fluidez técnica


### Solución 11

Cada término procede de un producto distinto:

$$
(3x-2)(2x+5)
=\underbrace{6x^2}_{(3x)(2x)}
+\underbrace{15x}_{(3x)(5)}
-\underbrace{4x}_{(-2)(2x)}
-\underbrace{10}_{(-2)(5)}
=6x^2+11x-10.
$$

La reunión $15x-4x=11x$ ocurre *después* de distribuir.


### Solución 12

$$
(x-2y)(x+3y)
=x^2+3xy-2xy-6y^2
=x^2+xy-6y^2.
$$

Los dos productos que forman el coeficiente de $xy$ son $x\cdot3y=3xy$ y $(-2y)\cdot x=-2xy$; juntos dan $xy$.


### Solución 13

Distribuimos cada sumando del primer factor:

$$
\begin{aligned}
(2x-y+3)(x+2y)
&=2x^2+4xy-xy-2y^2+3x+6y\\
&=2x^2+3xy-2y^2+3x+6y.
\end{aligned}
$$

El signo $-2y^2$ procede de $(-y)(2y)$; organizar el cálculo por sumando previene la omisión de productos.


### Solución 14

El factor numérico común máximo visible es $12$; las potencias comunes son $x^2y^2$. Entonces

$$
24x^4y^2-36x^3y^3+12x^2y^2
=12x^2y^2(2x^2-3xy+1).
$$

La expansión de la derecha devuelve $24x^4y^2-36x^3y^3+12x^2y^2$. El coeficiente final del paréntesis es $1$ porque se ha extraído el tercer término entero.


### Solución 15

Elegimos $-4x$, que deja positivo el primer coeficiente interior:

$$
-4x^3+12x^2-8x
=-4x(x^2-3x+2).
$$

Los signos interiores son $+$, $-$ y $+$: multiplicados por $-4x$ producen, respectivamente, $-4x^3$, $+12x^2$ y $-8x$. Además $x^2-3x+2=(x-1)(x-2)$, por lo que puede escribirse $-4x(x-1)(x-2)$; la verificación por expansión recupera el original.


### Solución 16

$$
\begin{aligned}
(3a-2b)^2&=(3a-2b)(3a-2b)\\
&=9a^2-6ab-6ab+4b^2\\
&=9a^2-12ab+4b^2.
\end{aligned}
$$

Análogamente,

$$
(x+4)^2=(x+4)(x+4)=x^2+4x+4x+16=x^2+8x+16.
$$

Los términos cruzados se obtienen de dos productos diferentes.


### Solución 17

$$
16x^2-81y^2=(4x)^2-(9y)^2=(4x-9y)(4x+9y).
$$

La comprobación es $(4x-9y)(4x+9y)=16x^2-81y^2$ porque $36xy-36xy=0$.


### Solución 18

Repetimos la misma identidad donde aparece una nueva diferencia de cuadrados:

$$
\begin{aligned}
x^8-1&=(x^4-1)(x^4+1)\\
&=(x^2-1)(x^2+1)(x^4+1)\\
&=(x-1)(x+1)(x^2+1)(x^4+1).
\end{aligned}
$$

La primera comprobación: $(x^4-1)(x^4+1)=x^8-1$. No declaramos irreducibles los otros factores; simplemente detenemos esta ruta de *diferencias de cuadrados visibles*.


### Solución 19

Es suma de cubos de $3a$ y $2b$:

$$
27a^3+8b^3=(3a+2b)(9a^2-6ab+4b^2).
$$

Al expandir, los términos mixtos son $-18a^2b+18a^2b$ y $12ab^2-12ab^2$: ambos pares se cancelan y quedan $27a^3+8b^3$. El signo central negativo es indispensable.


### Solución 20

$$
64x^3-125=(4x)^3-5^3
=(4x-5)(16x^2+20x+25).
$$

La expansión produce $64x^3+80x^2+100x-80x^2-100x-125=64x^3-125$. Son precisamente los términos mixtos los que se cancelan.


### Solución 21

Agrupamos:

$$
\begin{aligned}
x^3+4x^2-9x-36
&=x^2(x+4)-9(x+4)\\
&=(x+4)(x^2-9)\\
&=(x+4)(x-3)(x+3).
\end{aligned}
$$

El nuevo factor $x^2-9$ es una diferencia de cuadrados, motivo para volver a inspeccionar después de agrupar.


### Solución 22

$$
6xy-9x+4y-6
=3x(2y-3)+2(2y-3)
=(3x+2)(2y-3).
$$

El binomio $2y-3$ aparece dos veces; distribuir el producto final devuelve los cuatro términos iniciales.


### Solución 23

Buscamos $r+s=-9$ y $rs=20$. La pareja $-4,-5$ satisface ambas condiciones, por lo que

$$
x^2-9x+20=(x-4)(x-5).
$$

Expandir devuelve $x^2-(4+5)x+20$.


### Solución 24

Las condiciones son $r+s=2$ y $rs=-35$, satisfechas por $7,-5$. Por tanto,

$$
x^2+2x-35=(x+7)(x-5).
$$

La comprobación da $x^2-5x+7x-35=x^2+2x-35$: el producto negativo exige signos opuestos, pero la suma decide cuál es positivo.


### Solución 25

Aquí $ac=6\cdot6=36$. Elegimos $9,4$, pues $9+4=13$ y $9\cdot4=36$:

$$
\begin{aligned}
6x^2+13x+6
&=6x^2+9x+4x+6\\
&=3x(2x+3)+2(2x+3)\\
&=(3x+2)(2x+3).
\end{aligned}
$$

El producto $ac$ organiza la partición del término medio para que surja un binomio común.


### Solución 26

$ac=12(-10)=-120$. La pareja $-15,8$ tiene suma $-7$ y producto $-120$:

$$
\begin{aligned}
12x^2-7x-10
&=12x^2-15x+8x-10\\
&=3x(4x-5)+2(4x-5)\\
&=(3x+2)(4x-5).
\end{aligned}
$$

La expansión muestra coeficiente lineal $-15+8=-7$ y constante $2(-5)=-10$, además del término principal $3\cdot4x^2=12x^2$.

## C. Justificación y reconstrucción


### Solución 27

La primera distributividad respecto del factor izquierdo da

$$
(a+b)(c+d)=a(c+d)+b(c+d).
$$

La segunda, aplicada en ambos sumandos, da $ac+ad+bc+bd$. Para leer la igualdad al revés, primero identificamos los pares $ac+ad=a(c+d)$ y $bc+bd=b(c+d)$; al reconstruir el bloque compartido $c+d$ obtenemos $(a+b)(c+d)$. No basta observar cuatro términos: debemos reconocer una organización que produzca el mismo factor compuesto.


### Solución 28

$$
\begin{aligned}
(a-b)(a-b)&=a^2-ab-ba+b^2\\
&=a^2-2ab+b^2.
\end{aligned}
$$

Los términos cruzados son $a(-b)=-ab$ y $(-b)a=-ab$. Por ejemplo, $a=3,b=1$ refuta la falsa identidad: $(3-1)^2=4$, mientras $3^2-1^2=8$. La fórmula correcta para la última expresión es $a^2-b^2=(a-b)(a+b)$.


### Solución 29

Comenzamos con el cuadrado ya demostrado:

$$
\begin{aligned}
(a+b)^3
&=(a^2+2ab+b^2)(a+b)\\
&=a^3+a^2b+2a^2b+2ab^2+ab^2+b^3\\
&=a^3+3a^2b+3ab^2+b^3.
\end{aligned}
$$

Los tres aportes a $a^2b$ y los tres a $ab^2$ explican los coeficientes $3$. Desde C13, el teorema del binomio proporciona la misma secuencia $\binom30,\binom31,\binom32,\binom33=1,3,3,1$. La expansión muestra el mecanismo; el teorema revela su estructura combinatoria general.


### Solución 30

$$
(a-b)(a+b)=a^2+ab-ab-b^2=a^2-b^2.
$$

La cancelación de $ab$ con $-ab$ produce una **diferencia**, nunca una suma de cuadrados. Con $a=b=1$, el supuesto $a^2+b^2=(a-b)(a+b)$ afirmaría $2=0$, lo que la refuta. La expansión es simultáneamente demostración de la identidad verdadera y diagnóstico de la falsa.


### Solución 31

Para la diferencia,

$$
\begin{aligned}
(a-b)(a^2+ab+b^2)
&=a^3+\underbrace{a^2b}_{+}-\underbrace{a^2b}_{-}
 +\underbrace{ab^2}_{+}-\underbrace{ab^2}_{-}-b^3\\
&=a^3-b^3.
\end{aligned}
$$

De manera análoga,

$$
\begin{aligned}
(a+b)(a^2-ab+b^2)
&=a^3-\underbrace{a^2b}_{-}+\underbrace{a^2b}_{+}
 +\underbrace{ab^2}_{+}-\underbrace{ab^2}_{-}+b^3\\
&=a^3+b^3.
\end{aligned}
$$

En ambos casos se anulan exactamente un par de términos de tipo $a^2b$ y otro de tipo $ab^2$; los signos interiores son los necesarios para esa cancelación.


### Solución 32

Sea $S=\sum_{j=0}^{n-1}a^{n-1-j}b^j$, para $n\ge1$. Distribuimos y cambiamos sólo el índice de la segunda suma:

$$
\begin{aligned}
(a-b)S
&=\sum_{j=0}^{n-1}a^{n-j}b^j
 -\sum_{j=0}^{n-1}a^{n-1-j}b^{j+1}\\
&=\sum_{j=0}^{n-1}a^{n-j}b^j
 -\sum_{j=1}^{n}a^{n-j}b^j\\
&=a^n-b^n.
\end{aligned}
$$

Cada índice $1\le j\le n-1$ se cancela. El extremo $j=0$ de la primera suma deja $a^n$ y el extremo $j=n$ de la segunda deja $-b^n$. Para $n=1$, definimos la suma de un único término como $S=1$, y la identidad se reduce a $(a-b)\cdot1=a-b$. En las sumas generales, un factor de exponente cero se **omite** como factor vacío; en particular no estamos evaluando $0^0$ cuando alguna base vale cero. Todo se obtiene mediante operaciones finitas.


### Solución 33

En la identidad anterior reemplazamos $b$ por $-b$. Como $n=2k+1$ es impar, $(-b)^n=-b^n$ y

$$
a^n+b^n
=(a+b)\sum_{j=0}^{n-1}(-1)^j a^{n-1-j}b^j.
$$

Los signos alternan porque cada término lleva $(-b)^j$; el último es positivo, pues $n-1=2k$ es par. Para $n=3$, resulta $(a+b)(a^2-ab+b^2)$; para $n=5$, $(a+b)(a^4-a^3b+a^2b^2-ab^3+b^4)$. Expandir cualquiera de ellos anula los términos intermedios y conserva $a^n+b^n$.


### Solución 34

**Suficiencia.** Si $r+s=b$ y $rs=c$, entonces

$$
(x+r)(x+s)=x^2+(r+s)x+rs=x^2+bx+c.
$$

**Necesidad.** Si esta igualdad vale para *todo* $x$, al expandir y restar $x^2$ tenemos

$$
[b-(r+s)]x+[c-rs]=0\quad\text{para todo }x.
$$

Al elegir $x=0$ deducimos $c-rs=0$. Con $x=1$ queda $b-(r+s)=0$. Por tanto $c=rs$ y $b=r+s$. El argumento justifica la comparación de coeficientes sin presuponer todavía una teoría formal de polinomios.


### Solución 35

Como $a\ne0$, la expresión propuesta está definida. Al expandir,

$$
\begin{aligned}
\frac1a(ax+m)(ax+n)
&=\frac1a\big(a^2x^2+a(m+n)x+mn\big)\\
&=ax^2+bx+c,
\end{aligned}
$$

porque $m+n=b$ y $mn=ac$. Esta fórmula explica el método: dividir $bx$ como $mx+nx$ permite reagrupar $ax^2+mx+nx+c$ hasta construir los factores. Ejemplo propio, distinto del desarrollado en la teoría: $8x^2+14x+3$ tiene $ac=24$; elegimos $m=12$ y $n=2$, pues $12+2=14$ y $12\cdot2=24$. Por agrupación,

$$
8x^2+14x+3=8x^2+12x+2x+3=4x(2x+3)+(2x+3)=(4x+1)(2x+3).
$$

La factorización se comprueba expandiendo. El método no presupone que cualquier pareja exista dentro de una clase de coeficientes fijada.


### Solución 36

**Ruta por agrupación:**

$$
\begin{aligned}
x^3+5x^2-4x-20
&=x^2(x+5)-4(x+5)\\
&=(x+5)(x^2-4)\\
&=(x+5)(x-2)(x+2).
\end{aligned}
$$

**Ruta inversa de verificación:** $(x-2)(x+2)=x^2-4$ y

$$
(x+5)(x^2-4)=x^3+5x^2-4x-20.
$$

La primera ruta *descubre* una estructura común; la segunda comprueba independientemente que la expresión propuesta reproduce todos los términos.


### Solución 37

Por asociatividad y conmutatividad, $2x(x+1)=x[2(x+1)]$, y por distributividad $2(x+1)=2x+2$. Luego

$$
2x(x+1)=x(2x+2)=2x^2+2x.
$$

La primera forma destaca el factor $2x$ y el bloque $x+1$; la segunda, el factor $x$ y el bloque $2x+2$; la tercera, dos términos y sus coeficientes. Las tres son iguales para todo $x$, pero su utilidad depende de qué información se necesite.


### Solución 38

El dominio real de $x^{3/2}-x^{1/2}$ es $x\ge0$. Para $x>0$, la ley de potencias da $x^{3/2}=x^{1/2}x$, así que

$$
x^{3/2}-x^{1/2}=x^{1/2}(x-1)=\sqrt x(x-1).
$$

En el extremo $x=0$, la expresión original y la factorizada valen $0$ directamente, por lo que también allí coinciden. La expresión factorizada debe conservar la restricción $x\ge0$; no se infiere una extensión real a valores negativos de $x$.

## D. Diagnóstico del primer paso inválido


### Solución 39

La **primera** igualdad es falsa: $(a+b)^2$ se ha tratado como si el cuadrado distribuyera sobre una suma. En realidad,

$$
(a+b)^2=(a+b)(a+b)=a^2+2ab+b^2.
$$

Además, la última expresión propuesta $(a-b)(a+b)$ vale $a^2-b^2$, no $a^2+b^2$. Con $a=b=1$, la primera igualdad falsa da $4=2$. Se reconstruye desde $(a+b)^2$, sin considerar verdaderas las igualdades posteriores por el mero hecho de que forman una cadena.


### Solución 40

El primer error es $(x-4)^2=x^2-16$: se confundió el cuadrado de una diferencia con una diferencia de cuadrados. La reparación es

$$
(x-4)^2=x^2-8x+16.
$$

La identidad diferente $x^2-16=(x-4)(x+4)$ sí es válida, pero **no** demuestra la cadena propuesta. Para $x=0$, por ejemplo, $(x-4)^2=16$ y $x^2-16=-16$.


### Solución 41

La primera igualdad es inválida: $a^2+b^2$ no es, en general, $(a+b)(a-b)$. La segunda igualdad es correcta si se la aísla:

$$
(a+b)(a-b)=a^2-b^2.
$$

Con $a=b=1$ se ve $2\ne0$. La corrección consiste en sustituir el miembro inicial por $a^2-b^2$, no en presentar una falsa factorización de la suma de cuadrados.


### Solución 42

El primer error es $(a+b)^3=a^3+b^3$: se perdieron $3a^2b+3ab^2$. La expansión correcta es

$$
(a+b)^3=a^3+3a^2b+3ab^2+b^3.
$$

En cambio, $a^3+b^3=(a+b)(a^2-ab+b^2)$ es una identidad verdadera aislada. Esa coincidencia posterior no repara el primer salto falso ni valida la cadena completa.


### Solución 43

La primera igualdad ya falla por el signo central: la propuesta $(x+2)(x^2+2x+4)$ expande a $x^3+4x^2+8x+8$, no a $x^3+8$. La suma de cubos correcta es

$$
x^3+8=x^3+2^3=(x+2)(x^2-2x+4).
$$

Al expandir aparecen $+2x^2-2x^2$ y $+4x-4x$, que se cancelan. La segunda igualdad de la cadena original también es falsa; la primera falla antes.


### Solución 44

La primera igualdad cambia el signo equivocado: $(x-2)(x^2-2x+4)$ contiene $-4x^2+8x$, que no están en $x^3-8$. La identidad de diferencia de cubos da

$$
x^3-8=(x-2)(x^2+2x+4).
$$

Comprobación: $x^3+2x^2+4x-2x^2-4x-8=x^3-8$. El término central del factor cuadrático debe ser $+2x$.


### Solución 45

La primera ruptura aparece al escribir $6x^2+9x=3x(2x+9)$. Distribuir el supuesto resultado da $6x^2+27x$, como la propia cadena reconoce; el factor de $9x$ por $3x$ deja coeficiente residual $3$, **no $9$**. La reparación es

$$
6x^2+9x=3x(2x+3).
$$

Expandir verifica exactamente la expresión inicial.


### Solución 46

La primera igualdad es falsa porque extraer $-1$ debe invertir **todos** los signos:

$$
-x^2+5x-6=-(x^2-5x+6).
$$

Ahora $x^2-5x+6=(x-2)(x-3)$, pues $(-2)+(-3)=-5$ y $(-2)(-3)=6$. En consecuencia,

$$
-x^2+5x-6=-(x-2)(x-3).
$$

No estamos resolviendo una ecuación: comprobamos una identidad multiplicando.


### Solución 47

La primera igualdad es correcta: $(x+2)(x+5)=x^2+7x+10$. La **segunda** es falsa porque cambiar $x+5$ por $x-5$ altera tanto el término lineal como el constante. La reparación es conservar

$$
x^2+7x+10=(x+2)(x+5).
$$

Al expandir de nuevo se obtiene $x^2+(2+5)x+10$. Para $x=0$, el producto correcto vale $10$ y el alterado vale $-10$.


### Solución 48

La primera descomposición $11x=6x+5x$ es correcta; también lo es $6x^2+6x=6x(x+1)$. La **primera igualdad falsa** es la última: $6x(x+1)+(5x+3)$ no tiene el binomio $(x+1)$ como factor común, y $(x+1)(6x+3)=6x^2+9x+3$, no la expresión anterior.

Para fabricar una agrupación útil, elegimos $9+2=11$ y $9\cdot2=6\cdot3=18$:

$$
\begin{aligned}
6x^2+11x+3
&=6x^2+9x+2x+3\\
&=3x(2x+3)+(2x+3)\\
&=(3x+1)(2x+3).
\end{aligned}
$$

La expansión confirma el término medio $9x+2x=11x$.


### Solución 49

La primera sustitución ya falla: con $u=x$, $u^2=x^2$, no $x^4$. Debe elegirse $u=x^2$ para obtener $u^2-5u+4$. Éste factoriza como $(u-1)(u-4)$; al regresar,

$$
\begin{aligned}
x^4-5x^2+4
&=(x^2-1)(x^2-4)\\
&=(x-1)(x+1)(x-2)(x+2).
\end{aligned}
$$

No se resolvió ninguna ecuación; se reconstruyó una identidad y puede comprobarse expandiendo.


### Solución 50

El dominio original es $x\ge0$. El primer error está en $x^{3/2}-x^{1/2}=x^{1/2}(x+1)$: por distributividad, la expresión de la derecha vale $x^{3/2}+x^{1/2}$, con signo **positivo** en el segundo término. La forma corregida es

$$
x^{3/2}-x^{1/2}=\sqrt x(x-1),\qquad x\ge0.
$$

Para $x>0$ se usa $x^{3/2}=x\sqrt x$; para $x=0$ se evalúan directamente ambos lados y se obtiene $0=0$. La igualdad falsa coincide fortuitamente en $0$, lo que demuestra que una comprobación en un solo punto no acredita una identidad.

## E. Estrategia y elección de representación


### Solución 51

Los dos productos comparten el bloque $(x+2)$: conservarlo ahorra una expansión y una refactorización. Por distributividad inversa,

$$
\begin{aligned}
(x+2)(x-3)+(x+2)(2x+1)
&=(x+2)[(x-3)+(2x+1)]\\
&=(x+2)(3x-2).
\end{aligned}
$$

La ruta alternativa desarrolla: $(x^2-x-6)+(2x^2+5x+2)=3x^2+4x-4$, que al expandir $(x+2)(3x-2)$ resulta igual. Extraer primero el factor compuesto evita producir seis términos para recuperar un producto ya visible.


### Solución 52

$x^4-16=(x^2)^2-4^2$ es una diferencia de cuadrados directa:

$$
x^4-16=(x^2-4)(x^2+4)=(x-2)(x+2)(x^2+4).
$$

En cambio, $x^4+16$ es inicialmente una **suma** de cuadrados y no admite aplicar a sus dos términos la misma fórmula. No debemos concluir de ello que sea imposible factorizarla de otra manera. Podemos *construir* una diferencia de cuadrados usando identidades ya estudiadas y $\sqrt2$ de C18:

$$
\begin{aligned}
x^4+16
&=(x^2+4)^2-(2\sqrt2\,x)^2\\
&=(x^2+4-2\sqrt2\,x)(x^2+4+2\sqrt2\,x).
\end{aligned}
$$

La expansión confirma que los $8x^2$ añadidos y sustraídos se cancelan. En C19 no se emite un juicio formal de irreducibilidad ni se exige una clasificación completa sobre distintos cuerpos; se precisa qué identidad se usa y por qué la aplicación directa inicial era incorrecta.


### Solución 53

**Inspección:** buscamos factores principales $3x$ y $2x$ y constantes $1$ y $3$; $(3x+1)(2x+3)$ produce término cruzado $9x+2x=11x$. **Método $ac$:** $ac=18$, pareja $9,2$; por tanto,

$$
6x^2+11x+3=6x^2+9x+2x+3
=3x(2x+3)+(2x+3)
=(3x+1)(2x+3).
$$

La inspección utiliza la estructura esperada del producto; el método $ac$ fabrica sistemáticamente una agrupación. Expandir $(3x+1)(2x+3)=6x^2+11x+3$ verifica ambas rutas.


### Solución 54

Antes de buscar un patrón especial, observamos el factor común $4x$:

$$
8x^3+12x^2+4x=4x(2x^2+3x+1).
$$

La nueva forma revela un trinomio que puede reconstruirse como $(2x+1)(x+1)$, pues su expansión es $2x^2+3x+1$. Concluimos

$$
4x(2x+1)(x+1).
$$

No había un producto que expandir al inicio. El primer paso reduce el número de factores y **hace aparecer** una estructura distinta; por eso es preciso volver a leer después de extraer el factor común.


### Solución 55

Elegimos la forma desarrollada como representación común, porque el objetivo es comparar dos expresiones:

$$
(x-1)(x+1)+2x+2=x^2-1+2x+2=x^2+2x+1.
$$

Es idéntica a la primera. Alternativamente, ambas expresiones se reconstruyen como $(x+1)^2$; en efecto, la segunda es $(x+1)[(x-1)+2]=(x+1)^2$. La forma desarrollada facilita la comparación término a término; la factorizada muestra el cuadrado oculto.


### Solución 56

Un ejemplo original es $x^2+5x+16$. Sus extremos son $x^2$ y $4^2$, pero para que sea $(x+4)^2$ necesita el término central $2x\cdot4=8x$. Con $5x$ no es ese cuadrado perfecto. Corrigiendo el término medio obtenemos

$$
x^2+8x+16=(x+4)^2.
$$

La identificación de los extremos sólo sugiere un candidato: el doble producto debe comprobarse antes de declararlo identidad.


### Solución 57

Una primera agrupación produce

$$
x^3-2x^2+3x-6=x^2(x-2)+3(x-2)=(x-2)(x^2+3).
$$

Reordenando los términos obtenemos una segunda:

$$
(x^3+3x)+(-2x^2-6)=x(x^2+3)-2(x^2+3)
=(x-2)(x^2+3).
$$

La primera intenta fabricar $(x-2)$ y la segunda $(x^2+3)$. Al extraer el factor común final, el mismo producto aparece con el orden de los factores intercambiado. Su expansión reproduce el enunciado.


### Solución 58

El bloque repetido es $(x-2)^2$. Si $u=(x-2)^2$, entonces

$$
u^2-5u+4=(u-1)(u-4).
$$

Al regresar,

$$
[(x-2)^2-1][(x-2)^2-4].
$$

**Aquí** hay que volver a inspeccionar: cada corchete es diferencia de cuadrados. Así,

$$
[(x-3)(x-1)][(x-4)x]
=x(x-1)(x-3)(x-4).
$$

La sustitución sirve para ver el trinomio y deshacerla revela los factores adicionales; expandir en sentido inverso confirma la identidad.


### Solución 59

**Diferencia de cuadrados:**

$$
\begin{aligned}
a^6-b^6
&=(a^3-b^3)(a^3+b^3)\\
&=(a-b)(a^2+ab+b^2)(a+b)(a^2-ab+b^2).
\end{aligned}
$$

**Diferencia de cubos:**

$$
\begin{aligned}
a^6-b^6
&=(a^2-b^2)(a^4+a^2b^2+b^4)\\
&=(a-b)(a+b)[(a^2+b^2)^2-(ab)^2]\\
&=(a-b)(a+b)(a^2+ab+b^2)(a^2-ab+b^2).
\end{aligned}
$$

Los productos finales son iguales por conmutatividad de los factores. En la segunda ruta, la identidad intermedia se verifica expandiendo $(a^2+b^2)^2-a^2b^2=a^4+a^2b^2+b^4$. No necesitamos teorema del factor.


### Solución 60

La suma presenta el bloque común $(x^2+9)$; extraerlo primero conserva la estructura:

$$
\begin{aligned}
(x^2+9)(x^2-9)+3(x^2+9)
&=(x^2+9)[(x^2-9)+3]\\
&=(x^2+9)(x^2-6).
\end{aligned}
$$

Al expandir la expresión original: $(x^4-81)+3x^2+27=x^4+3x^2-54$. Expandir $(x^2+9)(x^2-6)$ da el mismo resultado. La forma producto conserva los factores; la desarrollada permite leer coeficientes. Ninguna es superior para *todas* las tareas.

## F. Transferencia acumulativa


### Solución 61

El dominio original es $x\ge0$. Para $x>0$, las leyes de C18 permiten extraer $x^{1/2}$:

$$
\begin{aligned}
x^{5/2}-4x^{3/2}+3x^{1/2}
&=x^{1/2}(x^2-4x+3)\\
&=\sqrt x(x-1)(x-3).
\end{aligned}
$$

La pareja $-1,-3$ tiene suma $-4$ y producto $3$. En $x=0$ todos los términos originales y el producto final valen $0$, de modo que la identidad también es válida allí. Mantener $x\ge0$ es parte de la respuesta.


### Solución 62

La hipótesis $x>0$ asegura que los exponentes racionales y sus leyes pueden utilizarse de forma sistemática. Tomando $u=x^{2/3}$,

$$
x^{4/3}-5x^{2/3}+4=u^2-5u+4=(u-1)(u-4).
$$

Al regresar,

$$
(x^{2/3}-1)(x^{2/3}-4),\qquad x>0.
$$

Si se desea continuar, con $v=x^{1/3}>0$ los factores son diferencias de cuadrados: $(v-1)(v+1)(v-2)(v+2)$. Cada sustitución debe revertirse de manera completa y la hipótesis original $x>0$ permanece; no se amplía el dominio al simplificar.


### Solución 63

El dominio original es $x\ge0$. El factor compuesto común es $\sqrt x$:

$$
\sqrt x(x-4)+2\sqrt x(x+1)
=\sqrt x[(x-4)+2(x+1)]
=\sqrt x(3x-2).
$$

Distribuyendo el producto final obtenemos $3x\sqrt x-2\sqrt x$, y en el original $x\sqrt x-4\sqrt x+2x\sqrt x+2\sqrt x$ produce lo mismo. La comprobación incluye $x=0$ porque ninguna expresión contiene divisiones por $\sqrt x$.


### Solución 64

**Ruta por expansión:**

$$
\begin{aligned}
(u+v)^3+(u-v)^3
&=(u^3+3u^2v+3uv^2+v^3)\\
&\quad +(u^3-3u^2v+3uv^2-v^3)\\
&=2u^3+6uv^2\\
&=2u(u^2+3v^2).
\end{aligned}
$$

Las contribuciones impares en $v$ se cancelan por parejas. **Ruta de reagrupación estructural:** sean $A=u+v$, $B=u-v$. La suma de cubos produce $(A+B)(A^2-AB+B^2)$; aquí $A+B=2u$ y

$$
A^2-AB+B^2=(u+v)^2-(u^2-v^2)+(u-v)^2=u^2+3v^2.
$$

Extraemos así inmediatamente el factor $2u$ y obtenemos el mismo producto. No se requiere restricción de dominio: son identidades para todos los reales $u,v$.


### Solución 65

**Ruta (i), cuadrados primero:**

$$
\begin{aligned}
x^6-1
&=(x^3-1)(x^3+1)\\
&=(x-1)(x^2+x+1)(x+1)(x^2-x+1).
\end{aligned}
$$

Los dos factores cúbicos se tratan mediante diferencia y suma de cubos. **Ruta (ii), cubos primero:**

$$
\begin{aligned}
x^6-1
&=(x^2-1)(x^4+x^2+1)\\
&=(x-1)(x+1)[(x^2+1)^2-x^2]\\
&=(x-1)(x+1)(x^2-x+1)(x^2+x+1).
\end{aligned}
$$

Son los mismos cuatro factores, salvo el orden. La identidad $(x^2+x+1)(x^2-x+1)=(x^2+1)^2-x^2=x^4+x^2+1$ verifica la equivalencia por expansión.


### Solución 66

Como $7$ es impar, aplicamos la suma de potencias con $a=x$, $b=2$:

$$
\boxed{x^7+2^7=(x+2)(x^6-2x^5+4x^4-8x^3+16x^2-32x+64).}
$$

Los siete términos del segundo factor alternan signos $+,-,+,-,+,-,+$. Al distribuir $x$ y $2$, cada término intermedio $\pm2^j x^{7-j}$ aparece con el signo opuesto de la otra distribución; se cancelan. Sólo quedan $x^7$ del primer extremo y $2\cdot64=128=2^7$ del último extremo. La comprobación es algebraica y no usa raíces de polinomios.


### Solución 67

Pongamos $u=x^2$. El trinomio auxiliar factoriza como

$$
u^2-10u+9=(u-1)(u-9)
$$

porque $-1-9=-10$ y $(-1)(-9)=9$. Al regresar,

$$
x^4-10x^2+9=(x^2-1)(x^2-9)
=(x-1)(x+1)(x-3)(x+3).
$$

La expansión de los dos factores cuadráticos produce $(x^2)^2-10x^2+9$, verificando la expresión inicial.


### Solución 68

El bloque repetido es $u=(x+1)^2$. Por tanto,

$$
\begin{aligned}
(x+1)^4-10(x+1)^2+9
&=u^2-10u+9\\
&=(u-1)(u-9)\\
&=[(x+1)^2-1][(x+1)^2-9]\\
&=x(x+2)(x-2)(x+4).
\end{aligned}
$$

Ambos corchetes son diferencias de cuadrados, pues $1=1^2$ y $9=3^2$. Expandir desde el inicio un binomio a la cuarta potencia y luego volver a factorizar generaría más términos intermedios; la sustitución conserva visible la estructura cuadrática del bloque.


### Solución 69

Los primeros tres términos forman el cuadrado perfecto

$$
9x^2-6xy+y^2=(3x-y)^2.
$$

Luego

$$
\begin{aligned}
9x^2-6xy+y^2-25z^2
&=(3x-y)^2-(5z)^2\\
&=(3x-y-5z)(3x-y+5z).
\end{aligned}
$$

Verificación independiente: multiplique los dos factores como conjugados, obteniendo $(3x-y)^2-25z^2$, y expanda el cuadrado para recuperar los cuatro términos. El término cruzado $-6xy$ es indispensable.


### Solución 70

Descomponemos los coeficientes que contienen $k$ para fabricar el bloque $x+k$:

$$
\begin{aligned}
&x^3+(k+2)x^2+(2k-3)x-3k\\
&=x^3+kx^2+2x^2+2kx-3x-3k\\
&=x^2(x+k)+2x(x+k)-3(x+k)\\
&=(x+k)(x^2+2x-3)\\
&=(x+k)(x+3)(x-1).
\end{aligned}
$$

Para el último paso, $(x+3)(x-1)=x^2+2x-3$. El parámetro $k$ se trata como un real arbitrario: no hace falta dividir por él ni imponer $k\ne0$. La expansión del producto final da exactamente $x^3+(k+2)x^2+(2k-3)x-3k$ para todo $x,k\in\mathbb R$.


### Solución 71

**Ruta (i):** extraemos $3x$ y aplicamos diferencia de cuadrados:

$$
12x^3-27x=3x(4x^2-9)=3x(2x-3)(2x+3).
$$

**Ruta (ii):** extraemos sólo $x$ y luego reorganizamos el coeficiente:

$$
x(12x^2-27)=x\cdot3[(2x)^2-3^2]=3x(2x-3)(2x+3).
$$

La primera reconoce de entrada un factor común más grande; la segunda lo descubre después. Expandir los conjugados da $4x^2-9$, y multiplicar por $3x$ produce $12x^3-27x$.


### Solución 72

**Ruta (i):** primero extraemos $4$ y luego usamos $u=x^2$:

$$
\begin{aligned}
4x^4-20x^2+16
&=4(x^4-5x^2+4)\\
&=4(u^2-5u+4)\\
&=4(u-1)(u-4)\\
&=4(x-1)(x+1)(x-2)(x+2).
\end{aligned}
$$

**Ruta (ii):** fabricamos una diferencia de cuadrados dentro del mismo factor común:

$$
\begin{aligned}
4(x^4-5x^2+4)
&=4[(x^2+2)^2-(3x)^2]\\
&=4(x^2-3x+2)(x^2+3x+2)\\
&=4(x-1)(x-2)(x+1)(x+2).
\end{aligned}
$$

La construcción funciona porque $(x^2+2)^2-9x^2=x^4-5x^2+4$. Ambas rutas son identidades de expresiones, no resolución de ecuaciones, y sus productos sólo difieren por el orden de los factores.

## G. Síntesis avanzada


### Solución 73

**Lectura y plan.** La expresión $2x^4+6x^3-18x^2-54x$ tiene factor común $2x$. Después quedarán cuatro términos: convendrá agruparlos y volver a buscar un patrón.

**Ruta principal, cuatro etapas:**

$$
\begin{aligned}
E&=2x(x^3+3x^2-9x-27) &&\text{factor común},\\
 &=2x\big[x^2(x+3)-9(x+3)\big] &&\text{agrupación},\\
 &=2x(x+3)(x^2-9) &&\text{factor compuesto},\\
 &=2x(x+3)(x-3)(x+3) &&\text{diferencia de cuadrados}\\
 &=\boxed{2x(x+3)^2(x-3)}.&&\text{relectura}
\end{aligned}
$$

**Verificación independiente.** $(x+3)^2(x-3)=(x+3)(x^2-9)=x^3+3x^2-9x-27$; al multiplicar por $2x$ se recuperan exactamente los cuatro términos del enunciado.

**Ruta alternativa, agrupación primero:**

$$
\begin{aligned}
E&=(2x^4+6x^3)+(-18x^2-54x)\\
 &=2x^3(x+3)-18x(x+3)\\
 &=(x+3)(2x^3-18x)\\
 &=2x(x+3)(x^2-9)\\
 &=2x(x+3)^2(x-3).
\end{aligned}
$$

Las rutas difieren en el momento de extraer $2x$, no en la identidad final. En ninguna etapa se divide por $x$ o $x+3$, por lo que las igualdades valen para todo real $x$.


### Solución 74

**Arquitectura 1: dos diferencias de cuadrados.** Identificamos $A=(a+b)^2$ y $B=(a-b)^2$:

$$
\begin{aligned}
(a+b)^4-(a-b)^4
&=[(a+b)^2-(a-b)^2][(a+b)^2+(a-b)^2]\\
&=[(2b)(2a)]\,[2(a^2+b^2)]\\
&=\boxed{8ab(a^2+b^2)}.
\end{aligned}
$$

La primera diferencia de cuadrados interna se obtiene con $(a+b)-(a-b)=2b$ y $(a+b)+(a-b)=2a$; la suma de cuadrados de los binomios vale $2a^2+2b^2$ porque $+2ab$ y $-2ab$ se cancelan.

**Arquitectura 2: expansión binomial.**

$$
\begin{aligned}
(a+b)^4&=a^4+4a^3b+6a^2b^2+4ab^3+b^4,\\
(a-b)^4&=a^4-4a^3b+6a^2b^2-4ab^3+b^4.
\end{aligned}
$$

Al restar se cancelan $a^4$, $6a^2b^2$ y $b^4$; los términos de grados impares en $b$ se duplican: $8a^3b+8ab^3=8ab(a^2+b^2)$. La primera prueba explota la forma antes de expandir; la segunda identifica explícitamente la cancelación entre coeficientes binomiales. Ambas son válidas para todos los reales $a,b$.


### Solución 75

**Demostración general.** Definimos para $n\ge1$ la suma finita

$$
S_n=\sum_{j=0}^{n-1}a^{n-1-j}b^j.
$$

Entonces

$$
\begin{aligned}
(a-b)S_n
&=\sum_{j=0}^{n-1}a^{n-j}b^j-
  \sum_{j=1}^{n}a^{n-j}b^j\\
&=a^n-b^n,
\end{aligned}
$$

pues los términos de índices $1,\dots,n-1$ se anulan por parejas. En $n=1$, $S_1$ es por definición la suma de un único término $1$, y se recupera $a-b=(a-b)\cdot1$. En los extremos de las sumas se omiten los factores de exponente cero (producto vacío); no se evalúa $0^0$ si una base vale cero. La prueba no utiliza división por $a-b$ ni el teorema del factor.

**Aplicación con exponente $10$.** Directamente,

$$
x^{10}-1=(x-1)(x^9+x^8+x^7+x^6+x^5+x^4+x^3+x^2+x+1).
$$

**Aplicación como diferencia de quintas potencias.** Sustituyendo $a=x^2$, $b=1$, $n=5$:

$$
\begin{aligned}
x^{10}-1
&=(x^2-1)(x^8+x^6+x^4+x^2+1)\\
&=(x-1)(x+1)(x^8+x^6+x^4+x^2+1).
\end{aligned}
$$

**Comparación.** Multiplicar $(x+1)(x^8+x^6+x^4+x^2+1)$ produce exactamente los diez sumandos $x^9+x^8+\cdots+x+1$. Por tanto, los factores de ambas rutas son compatibles: la segunda revela un factor $x+1$ que la primera todavía no había hecho visible. No declaramos que alguna expresión sea irreducible ni empleamos teoría de raíces.


### Solución 76

Sea $n=2k+1\ge1$. Partimos de la diferencia de potencias y reemplazamos $b$ por $-b$:

$$
\begin{aligned}
a^n+b^n
&=a^n-(-b)^n\\
&=(a+b)\sum_{j=0}^{n-1}a^{n-1-j}(-b)^j\\
&=(a+b)\sum_{j=0}^{n-1}(-1)^j a^{n-1-j}b^j.
\end{aligned}
$$

La sustitución es válida porque $(-b)^n=-b^n$ para $n$ impar. Para $a=x$, $b=1$ y $n=7$:

$$
\boxed{x^7+1=(x+1)(x^6-x^5+x^4-x^3+x^2-x+1).}
$$

Los siete signos del segundo factor son $+,-,+,-,+,-,+$. Si $S=x^6-x^5+x^4-x^3+x^2-x+1$, entonces $xS$ y $S$ aportan términos iguales y opuestos en grados $1$ a $6$; sólo permanecen $x^7$ y $1$. Esto demuestra por expansión telescópica que el producto reproduce $x^7+1$, incluso para $x=-1$ sin realizar ninguna división.


### Solución 77

**Ruta (i), factor numérico inicial.** Como los tres coeficientes son múltiplos de $3$,

$$
18x^2-21x-15=3(6x^2-7x-5).
$$

En el trinomio interior, $ac=6(-5)=-30$. Buscamos sumandos $-10$ y $3$, cuyo producto es $-30$ y suma $-7$:

$$
\begin{aligned}
6x^2-7x-5
&=6x^2-10x+3x-5\\
&=2x(3x-5)+(3x-5)\\
&=(2x+1)(3x-5).
\end{aligned}
$$

La forma final es $\boxed{3(2x+1)(3x-5)}$.

**Ruta (ii), descomposición directa.** Sin sacar el $3$, usamos $ac=18(-15)=-270$. La pareja $-30,9$ suma $-21$ y tiene producto $-270$:

$$
\begin{aligned}
18x^2-21x-15
&=18x^2-30x+9x-15\\
&=6x(3x-5)+3(3x-5)\\
&=(6x+3)(3x-5)\\
&=3(2x+1)(3x-5).
\end{aligned}
$$

La primera ruta reduce los coeficientes antes de buscar la pareja y suele facilitar la aritmética; la segunda muestra que el procedimiento también funciona directamente. **Verificación:** $(2x+1)(3x-5)=6x^2-7x-5$ y el factor $3$ devuelve $18x^2-21x-15$.


### Solución 78

**Bloque y estrategia.** Escribimos $u=x^2+2x$. El enunciado se convierte en un trinomio mónico:

$$
u^2-2u-3=(u-3)(u+1),
$$

pues $-3+1=-2$ y $(-3)(1)=-3$.

**Regreso a $x$ y nueva lectura:**

$$
\begin{aligned}
E(x)
&=(x^2+2x-3)(x^2+2x+1)\\
&=(x+3)(x-1)(x+1)^2.
\end{aligned}
$$

El primer factor es un trinomio mónico; el segundo es un cuadrado perfecto. **Segunda verificación:** desarrollar directamente la expresión original da

$$
(x^2+2x)^2-2(x^2+2x)-3=x^4+4x^3+2x^2-4x-3.
$$

Expandir $(x^2+2x-3)(x^2+2x+1)$ produce ese mismo polinomio. La sustitución sólo facilita una identidad; no hemos resuelto la ecuación $E(x)=0$.


### Solución 79

**Lectura secuencial.** Las líneas (1)–(6) son correctas. La línea (2) extrae $x$; (3) reagrupa; (4) extrae respectivamente $x^2$ y $-4$; (5) extrae $(x+5)$; y (6) usa la diferencia de cuadrados $x^2-4=(x-2)(x+2)$.

La **primera igualdad falsa es (6) $\longrightarrow$ (7)**:

$$
(x-2)(x+2)\neq(x-2)^2
$$

como identidad, pues el primero vale $x^2-4$ y el segundo $x^2-4x+4$. Es plausible confundir los dos productos porque ambos contienen $x-2$ y dos factores lineales, pero un par de conjugados no forma un cuadrado. Por ejemplo, para $x=0$ esos dos factores cuadráticos valen $-4$ y $4$, pero ese valor no refuta la igualdad completa de las líneas (6) y (7), porque su factor exterior $x$ vale cero. Para comprobar la ruptura de la cadena completa, usamos $x=1$: la línea (6) vale $1\cdot6\cdot(-1)\cdot3=-18$ y la línea (7) vale $1\cdot6\cdot(-1)^2=6$.

**No confundir error temprano y pasos posteriores.** Las líneas (7)–(13), tomadas como transformaciones sucesivas *de la expresión equivocada*, son algebraicamente correctas: (8) agrupa $x(x+5)=x^2+5x$, (9) desarrolla $(x-2)^2$, (10) expande, (11) extrae $x$, (12) reagrupa y (13) factoriza dos grupos. Su corrección local no las reconecta con $E$ después de la ruptura en (7).

**Reconstrucción desde el último paso válido:** conservamos la línea (6) sin alterar ninguno de sus dos conjugados; la factorización verdadera es

$$
\boxed{E=x(x+5)(x-2)(x+2).}
$$

**Control de ambos productos.** El producto correcto expande así:

$$
x(x+5)(x^2-4)=x^4+5x^3-4x^2-20x.
$$

El producto introducido erróneamente en (7), en cambio, es

$$
x(x+5)(x-2)^2=x^4+x^3-16x^2+20x.
$$

Las dos expansiones son diferentes. Esto identifica exactamente dónde dejó de conservarse la expresión original y por qué una larga cadena posterior no proporciona una demostración.


### Solución 80

**(1) Lectura estructural y objetivo.** Toda la expresión está definida para $x\in\mathbb R$. Aparecen reiteradamente $x+1$ y su cuadrado. Buscamos una forma multiplicativa que permita ver factores sin resolver la ecuación $E(x)=0$.

**(2) Estrategia y sustitución.** Tomamos $u=x+1$. A diferencia de expandir de inmediato las potencias de $x+1$, esto conserva los bloques:

$$
E=u^4-5u^2+4+3u(u^2-1).
$$

**(3) Identidad que revela el factor común.** La parte par es cuadrática en $u^2$:

$$
u^4-5u^2+4=(u^2-1)(u^2-4).
$$

El sumando restante ya contiene $u^2-1$. Lo extraemos:

$$
E=(u^2-1)[(u^2-4)+3u]=(u^2-1)(u^2+3u-4).
$$

**(4) Mecanismo de reconstrucción.** El trinomio $u^2+3u-4$ procede de la pareja $4,-1$, cuya suma es $3$ y producto $-4$:

$$
u^2+3u-4=(u+4)(u-1).
$$

Por diferencia de cuadrados, $u^2-1=(u-1)(u+1)$.

**(5) Ejecución técnica y regreso a la variable original.**

$$
\begin{aligned}
E&=(u-1)(u+1)(u+4)(u-1)\\
 &= (u-1)^2(u+1)(u+4)\\
 &=\boxed{x^2(x+2)(x+5)},\qquad u=x+1.
\end{aligned}
$$

No se ha dividido por ningún factor; la identidad es válida para todo real $x$.

**(6) Verificación independiente.** Expandimos directamente en $u$:

$$
E=u^4+3u^3-5u^2-3u+4.
$$

Al sustituir $u=x+1$ y desarrollar se obtiene $E=x^4+7x^3+10x^2$. Expandir el producto propuesto da igualmente $x^2(x^2+7x+10)=x^4+7x^3+10x^2$.

**(7) Segunda ruta: expansión primero.** Sin introducir $u$ podemos expandir $\big((x+1)^2\big)^2$, $-5(x+1)^2$ y $3(x+1)((x+1)^2-1)$, reunir términos y obtener $x^4+7x^3+10x^2$. Extrayendo $x^2$ y reconstruyendo el trinomio, llegamos a $x^2(x+2)(x+5)$. Es válida, pero genera más términos y exige controlar más cancelaciones.

**(8) Cierre: forma y función.** La representación en $u$ hace visible la estructura cuadrática y el factor compartido $u^2-1$; la desarrollada hace visibles los coeficientes; la factorizada muestra $x^2$, $(x+2)$ y $(x+5)$. Las tres representan la misma expresión en $\mathbb R$. La elección de forma respondió al propósito de factorizar y verificar, no a la idea de que un producto sea siempre preferible.

## H. Soluciones de profundización y reconstrucción



#### Solución 081

Con $u=x^2$, buscamos suma $t-1$ y producto $-t$: los factores son $(u-1)(u+t)$. Así, $E=(x-1)(x+1)(x^2+t)$. Expandir $(x^2-1)(x^2+t)$ devuelve los tres términos originales para todo $t$. Si $t=-1$, queda $(x^2-1)^2=(x-1)^2(x+1)^2$; si $t=0$, queda $x^2(x-1)(x+1)$. La identidad no exige que los factores sean no nulos y conserva ambos valores excepcionales.



#### Solución 082

La diferencia de cuadrados da $[(t-1)(x-1)][(t+1)(x+1)]=(t^2-1)(x^2-1)$. Si $t=\pm1$, se anula para todo $x$. Recíprocamente, evaluar en $x=0$ exige $1-t^2=0$, luego $t=\pm1$. Expandir los cuadrados da $(t^2-1)x^2+1-t^2$, verificando el resultado. Evaluar en $x=1$ solamente no habría restringido $t$.



#### Solución 083

Escribamos $A=x+a$, $B=x+b$. El segundo producto es $(A+h)(B-h)=AB+hB-hA-h^2$. La diferencia es $h(A-B)+h^2=h(a-b+h)$. Desapareció $x$ porque $A-B=a-b$. Por el producto nulo, la constante es cero exactamente si $h=0$ o $h=b-a$. En el segundo caso se intercambian los dos factores originales; en el primero no cambian. No se ha dividido por un parámetro potencialmente nulo.



#### Solución 084

Expandir exige $B=2r+1$ y $C=r(r+1)$. Por tanto, $B$ es impar y $C=(B^2-1)/4$. Estas condiciones también bastan: si $B$ es un entero impar, $r=(B-1)/2$ es entero y $r(r+1)=(B^2-1)/4=C$. La expansión comprueba el trinomio. No basta que $B$ sea impar: el término constante está fijado por esa misma elección.



#### Solución 085

El producto es $(x^2+1)^2-u^2x^2=x^4+(2-u^2)x^2+1$. La igualdad equivale a $A=2-u^2$: la necesidad se obtiene también evaluando la diferencia en $x=1$. Existe $u$ real exactamente si $A\le2$. Todos son $u=\pm\sqrt{2-A}$, con una sola elección $u=0$ cuando $A=2$. Sustituir esos valores demuestra la suficiencia; no se afirma irreducibilidad de los factores.



#### Solución 086

La expansión es $x^3+(2a+b)x^2+(a^2+2ab)x+a^2b$. El requisito fuerza $b=-2a$ y produce $x^3-3a^2x-2a^3$. Recíprocamente, cada real $a$ y $b=-2a$ satisfacen el requisito, por la misma expansión. Si $a=0$, también $b=0$ y el producto es $x^3$. Esta parametrización describe los productos con la forma impuesta, no todos los cúbicos posibles sin término cuadrático.



#### Solución 087

Las expansiones son $n^4\pm4n^3+6n^2\pm4n+1$. Al sumarlas y restar $2n^4$, queda $12n^2+2$. Como $n^2\ge0$, es al menos $2$; es $2(6n^2+1)$ y por tanto par. También es $4(3n^2)+2$, cuyo resto al dividir por $4$ es $2$. La demostración incluye negativos y cero; comprobar unos pocos enteros no sustituye este certificado.



#### Solución 088

La factorización es $(a-b)(2x+a+b)$. Con igual paridad, $a-b$ y $a+b$ son pares; ambos factores son pares, de modo que el producto es múltiplo de $4$. Con paridad distinta, $a-b$ y $a+b$ son impares; añadir $2x$ conserva la imparidad del segundo factor y el producto es impar. La identidad procede de la diferencia de cuadrados, así que no requiere suponer signos positivos.



#### Solución 089

Agrupemos $n(n+3)=u=n^2+3n$ y $(n+1)(n+2)=u+2$. La expresión es $u(u+2)+1=(u+1)^2=(n^2+3n+1)^2$. El número entre paréntesis es entero. Como verificación independiente, ambas expansiones dan $n^4+6n^3+11n^2+6n+1$. La agrupación revela el cuadrado con menos términos; la expansión certifica la identidad. El argumento vale incluso si alguno de los consecutivos es cero o negativo.



#### Solución 090

El segundo es $x^4+2abx^2+a^2b^2$. La diferencia es $(a^2+b^2-2ab)x^2=(a-b)^2x^2$. Por tanto, el primero se reconstruye sumando ese defecto al supuesto cuadrado. Coinciden para todo $x$ si $a=b$; si coinciden, evaluar en $x=1$ fuerza $(a-b)^2=0$, luego $a=b$. La igualdad en $x=0$ no prueba nada sobre los parámetros, porque el defecto se anula allí siempre.



#### Solución 091

La diferencia entre ambos miembros es $(b-a)x^2+(c-ab)x+a^3-ac$. Evaluar en $0$ anula el término constante. Evaluar después en $1$ y $-1$ da la suma y diferencia de los otros dos coeficientes; ambos deben ser cero. Así $b=a$ y $c=ab=a^2$, también cuando $a=0$. Sustituir da $(x-a)(x^2+ax+a^2)=x^3-a^3$, cuya expansión verifica la suficiencia. Se usaron tres evaluaciones de una diferencia cuadrática, sin presuponer una factorización.



#### Solución 092

En $a=b=c=1$, el segundo miembro es cero y el primero $3+\lambda$, así que $\lambda=-3$ es necesario. Al distribuir el segundo miembro, los seis términos mixtos de la forma $a^2b$ se cancelan y quedan los tres cubos y $-3abc$; esto prueba la suficiencia. Si $c=b$, el factor cuadrático es $a^2+b^2-2ab=(a-b)^2$, por lo que $a^3+2b^3-3ab^2=(a+2b)(a-b)^2$. Expandir esta última expresión recupera sus tres términos. La identidad es clásica; la tarea consiste en reconstruir su coeficiente y usarla.

***

[← Capítulo 18](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 20 →](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md)
