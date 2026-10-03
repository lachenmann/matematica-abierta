# Narración — MA-CLS-C13-P01

**Duración objetivo:** 2:45–3:20.  
**Función:** unir las tres visualizaciones aprobadas sin añadir teoría nueva.

## Apertura

> El problema de partida parece geométrico: queremos asignar un número a una región limitada por una curva. Pero el cálculo integral no comienza suponiendo que ya sabemos qué significa ese número. Comienza por encerrar, sumar y comprobar qué permanece estable al refinar.

## Bloque 1 — MA-VIZ-C13-002

> Para una función no negativa podemos comparar la región con rectángulos. Una suma queda por debajo y otra por arriba. En el ejemplo de \(x^2\) sobre \([0,1]\), la diferencia entre ambas cotas es exactamente \(1/n\) para estas particiones uniformes. Al aumentar \(n\), esa brecha puede hacerse arbitrariamente pequeña. La imagen importa, pero lo decisivo es el control cuantitativo de la incertidumbre.

## Puente 1

> Refinar nos dice cómo estrechar el encierro. Ahora debemos mirar qué contiene cada suma.

## Bloque 2 — MA-VIZ-C13-003

> En cada subintervalo elegimos una etiqueta \(\xi_i\). La altura es \(f(\xi_i)\) y la anchura es \(\Delta x_i\). Su producto es la contribución de una franja. Al reunir todas las franjas aparece la suma
>
> \[
> \sum_{i=1}^{n} f(\xi_i)\,\Delta x_i.
> \]
>
> Aquí reconocemos la estructura de una suma de Riemann. Todavía no estamos usando esto como definición general de integral.

## Puente 2

> Y hay una dificultad adicional: las alturas no tienen por qué ser siempre positivas.

## Bloque 3 — MA-VIZ-C13-004

> El capítulo ya permite integrar funciones escalonadas. Si una franja tiene altura \(1\) y otra altura \(-1\), sus contribuciones con signo se cancelan:
>
> \[
> \int_0^2 s(x)\,dx=0.
> \]
>
> Pero el área geométrica de ambas franjas no se cancela. Al pasar a \(|s|\), las dos contribuciones son positivas y obtenemos \(2\). Por eso una integral con signo no es, en general, lo mismo que el área geométrica total.

## Cierre

> El recorrido deja tres ideas separadas. Primero, una región curva puede encerrarse mediante sumas finitas. Segundo, cada suma se construye con contribuciones de la forma \(f(\xi_i)\Delta x_i\). Tercero, esas contribuciones llevan signo. Con este lenguaje preparado, ya podemos avanzar hacia una definición general sin confundir la intuición geométrica con la teoría que debe justificarla.
