# Guion hablado — MA-CLS-C13-P01

Este archivo fija **exactamente lo que se pronuncia**. Las expresiones matemáticas están expandidas a forma oral para que la medición de voz sea reproducible.

## 01 — opening

El problema de partida parece geométrico: queremos asignar un número a una región limitada por una curva. Pero el cálculo integral no comienza suponiendo que ya sabemos qué significa ese número. Comienza por encerrar, sumar y comprobar qué permanece estable al refinar.

## 02 — block-1

Para una función no negativa podemos comparar la región con rectángulos. Una suma queda por debajo y otra por arriba. En el ejemplo de equis al cuadrado sobre el intervalo de cero a uno, la diferencia entre ambas cotas es exactamente uno sobre ene para estas particiones uniformes. Al aumentar ene, esa brecha puede hacerse arbitrariamente pequeña. La imagen importa, pero lo decisivo es el control cuantitativo de la incertidumbre.

## 03 — bridge-1

Refinar nos dice cómo estrechar el encierro. Ahora debemos mirar qué contiene cada suma.

## 04 — block-2

En cada subintervalo elegimos una etiqueta xi sub i. La altura es efe de xi sub i y la anchura es delta equis sub i. Su producto es la contribución de una franja. Al reunir todas las franjas aparece la suma desde i igual uno hasta ene de efe de xi sub i por delta equis sub i. Aquí reconocemos la estructura de una suma de Riemann. Todavía no estamos usando esto como definición general de integral.

## 05 — bridge-2

Y hay una dificultad adicional: las alturas no tienen por qué ser siempre positivas.

## 06 — block-3

El capítulo ya permite integrar funciones escalonadas. Si una franja tiene altura uno y otra altura menos uno, sus contribuciones con signo se cancelan: la integral de cero a dos de ese de equis, diferencial de equis, es cero. Pero el área geométrica de ambas franjas no se cancela. Al pasar al valor absoluto de ese, las dos contribuciones son positivas y obtenemos dos. Por eso una integral con signo no es, en general, lo mismo que el área geométrica total.

## 07 — closing

El recorrido deja tres ideas separadas. Primero, una región curva puede encerrarse mediante sumas finitas. Segundo, cada suma se construye con contribuciones de la forma efe de xi sub i por delta equis sub i. Tercero, esas contribuciones llevan signo. Con este lenguaje preparado, ya podemos avanzar hacia una definición general sin confundir la intuición geométrica con la teoría que debe justificarla.
