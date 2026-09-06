# Guía visual de Matemática Abierta

## Objetivo

El sistema visual debe mejorar la lectura matemática, especialmente en sesiones largas y en pantallas móviles. La semántica vive en Markdown; la apariencia vive en `styles.scss`.

## Principios

- ancho de lectura relativamente estrecho;
- tipografía aireada;
- fórmulas centradas y legibles;
- desplazamiento horizontal de expresiones largas en móvil;
- modo claro y oscuro;
- bloques pedagógicos con identidad visual estable;
- colores con función semántica, no decorativa.

## Bloques pedagógicos canónicos

- `ma-intuicion` — intuición conceptual;
- `ma-dominio` — dominio, hipótesis o restricciones;
- `ma-enunciado` — enunciado o material fuente;
- `ma-definicion` — definición formal;
- `ma-metodo` — estrategia reusable;
- `ma-error` — error frecuente o advertencia conceptual;
- `ma-comprobacion` — comprobación, control o verificación;
- `ma-fuente` — fuente o procedencia bibliográfica;
- `ma-observacion` — observación complementaria.

Todos se usan junto con la clase base `ma-block`.

Ejemplo:

```markdown
::: {.ma-block .ma-intuicion}
**Intuición**

Texto explicativo.
:::
```

## Convención editorial

Los colores e iconos deben conservar su función en todo el sitio. No cambiar el significado visual de un bloque entre cursos, problemas o libros.

## Responsive

La versión móvil es un objetivo de primer nivel. Ningún bloque debe desbordar el viewport y las fórmulas largas deben poder desplazarse horizontalmente sin romper la página.

## Estado

Este documento describe la primera versión aprobada del lenguaje visual de Matemática Abierta, desarrollada en WEB-0003.
