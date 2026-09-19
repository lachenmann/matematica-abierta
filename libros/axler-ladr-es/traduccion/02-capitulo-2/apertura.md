# Capítulo 2 · Espacios vectoriales de dimensión finita

**Estado:** `COTEJADO`  
**Fuente:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª ed., PDF oficial de 16-08-2026, p. 27.  
**Licencia:** adaptación/traducción no oficial bajo CC BY-NC 4.0.  
**Control de erratas:** cotejado con la errata oficial vigente al 13-09-2026.

> [TRAD] Traducción de trabajo de Matemática Abierta. Se preservan la jerarquía conceptual, la notación y las referencias del original.

En el capítulo anterior estudiamos los espacios vectoriales. El álgebra lineal, sin embargo, centra buena parte de su atención en los **espacios vectoriales de dimensión finita**, que introduciremos en este capítulo.

Comenzaremos considerando combinaciones lineales de listas de vectores. Esto conducirá al concepto fundamental de **independencia lineal**. El **lema de dependencia lineal** se convertirá después en una de las herramientas más útiles del libro.

Una lista de vectores suficientemente pequeña como para ser linealmente independiente y suficientemente grande como para que sus combinaciones lineales llenen todo el espacio vectorial recibe el nombre de **base**. Veremos que todas las bases de un espacio vectorial tienen la misma longitud; esto permitirá definir la **dimensión** de un espacio vectorial.

El capítulo termina con una fórmula para la dimensión de la suma de dos subespacios.

## Supuestos permanentes del capítulo

- $\mathbf F$ denota $\mathbf R$ o $\mathbf C$.
- $V$ denota un espacio vectorial sobre $\mathbf F$.

> [NOTA] La fotografía que acompaña la apertura del capítulo muestra el edificio principal del Institute for Advanced Study, en Princeton. Axler recuerda allí que Paul Halmos escribió en ese edificio el primer libro moderno de álgebra lineal; su título, *Finite-Dimensional Vector Spaces*, coincide con el de este capítulo.
