---
title: "Los números reales: axiomas de cuerpo, orden y completitud"
description: "Capítulo 1 de Cálculo para matemáticos, Tomo I; 40 ejercicios con soluciones."
content-id: MA-BCH-0003
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas: [calculo, analisis]
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: 2026-09-09
date-modified: 2026-10-16
prerequisites:
  []
number-sections: true
number-depth: 2
number-offset: [0]
crossref:
  chapters: true
format:
  html:
    css: calculo-para-matematicos.css
    html-math-method:
      method: mathjax
      url: https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js
---

# Los números reales: axiomas de cuerpo, orden y completitud {#sec-t1-c02}

En los cálculos elementales usamos los números reales con la familiaridad de quien conoce el terreno: sumamos, comparamos y escribimos raíces confiando en que cada operación permitida dará un número y en que los números que necesitamos estarán disponibles. El cálculo nos obligará a examinar esa confianza. Afirmar que una sucesión tiene un límite o que una función continua alcanza cierto valor exige una razón para asegurar la existencia de ese número.

La imagen de una recta sin agujeros sugiere lo que buscamos, pero todavía debemos darle un significado que pueda utilizarse en una demostración. Los racionales servirán para reconocer la dificultad: permiten las operaciones aritméticas habituales y admiten un orden compatible con ellas, aunque dejan sin solución algunas ecuaciones muy sencillas.

La comparación entre ambos sistemas nos lleva a preguntar

$$
\boxed{\text{¿qué posee }\mathbb R\text{ que no posee }\mathbb Q\text{ y que hace posible el cálculo?}}
$$

Tomaremos las propiedades de los números reales como punto de partida axiomático. Las operaciones y el orden describirán primero una estructura que también poseen los racionales; la **completitud** añadirá la condición de existencia que esa estructura deja abierta. Construir los reales a partir de objetos más elementales es otra manera de justificar estas propiedades, propia del estudio de sus fundamentos.

La ecuación que pondrá a prueba esa estructura es conocida desde la aritmética escolar,

$$
x^2=2,
$$

y, sin embargo, su resolución exige distinguir dos cuestiones: qué operaciones podemos hacer con un número y qué garantiza que exista un número con la propiedad buscada. Para formular la segunda cuestión necesitaremos las nociones de cota y supremo; la completitud permitirá después demostrar la existencia de la raíz real.

Como este es el primer capítulo, fijamos una convención mínima de lectura. La escritura $x\in A$ significa que $x$ pertenece al conjunto $A$; $A\subseteq B$ indica que todo elemento de $A$ pertenece a $B$. Las expresiones $\forall x\in A$ y $\exists x\in A$ se leen, respectivamente, «para todo elemento de $A$» y «existe al menos uno». El símbolo $\exists!$ exigirá, cuando aparezca, existencia **y** unicidad. Estas convenciones sirven para leer los axiomas y las pruebas; las operaciones con conjuntos necesarias para estudiar funciones se presentarán en el capítulo siguiente.

[Índice del Tomo I](../para-matematicos/calculo-para-matematicos.md) · [Capítulo 2 →](funciones-reales-estructura-composicion-inversas-y-graficas.md)

## Lectura por secciones {.unnumbered}

Cada sección se carga en una página independiente. Los ejercicios y sus soluciones se pueden abrir por separado.

- [1.1 — Axiomas de cuerpo y estructura de orden](cpm-c01-01.md)
- [1.2 — Valor absoluto, distancia y desigualdades](cpm-c01-02.md)
- [1.3 — Cotas, máximos, mínimos, supremos e ínfimos](cpm-c01-03.md)
- [1.4 — Por qué los racionales no bastan: el ejemplo de Rudin](cpm-c01-04.md)
- [1.5 — Completitud: la propiedad que falta en $\mathbb Q$](cpm-c01-05.md)
- [1.6 — Completitud en acción: existencia de raíces](cpm-c01-06.md)
- [1.7 — La propiedad arquimediana](cpm-c01-07.md)
- [1.8 — Entre dos reales siempre hay más números](cpm-c01-08.md)
- [1.9 — Intervalos encajados y bisección](cpm-c01-09.md)
- [1.10 — Laboratorio de completitud](cpm-c01-10.md)
- [1.11 — Ejercicios](cpm-c01-11.md)
- [Soluciones](cpm-c01-soluciones.md)

```{=html}
<script id="cpm-c01-anchor-routes" type="application/json">{"sec-t1-c02-02": "cpm-c01-01.html", "def-t1-0012": "cpm-c01-01.html", "prp-t1-0025": "cpm-c01-01.html", "exm-t1-0040": "cpm-c01-01.html", "prp-t1-0026": "cpm-c01-01.html", "prp-t1-0027": "cpm-c01-01.html", "thm-t1-0011": "cpm-c01-01.html", "def-t1-0032": "cpm-c01-01.html", "prp-t1-0028": "cpm-c01-01.html", "exm-t1-0041": "cpm-c01-01.html", "prp-t1-0007": "cpm-c01-01.html", "def-t1-0013": "cpm-c01-01.html", "sec-t1-c02-03": "cpm-c01-02.html", "def-t1-0014": "cpm-c01-02.html", "prp-t1-0008": "cpm-c01-02.html", "thm-t1-0001": "cpm-c01-02.html", "cor-t1-0001": "cpm-c01-02.html", "prp-t1-0009": "cpm-c01-02.html", "fig-t1-c02-01": "cpm-c01-02.html", "exm-t1-0013": "cpm-c01-02.html", "sec-t1-c02-04": "cpm-c01-03.html", "def-t1-0015": "cpm-c01-03.html", "def-t1-0016": "cpm-c01-03.html", "exm-t1-0014": "cpm-c01-03.html", "def-t1-0017": "cpm-c01-03.html", "prp-t1-0010": "cpm-c01-03.html", "exm-t1-0015": "cpm-c01-03.html", "sec-t1-c02-01": "cpm-c01-04.html", "prp-t1-0006": "cpm-c01-04.html", "exm-t1-0012": "cpm-c01-04.html", "sec-t1-c02-05": "cpm-c01-05.html", "sec-t1-c02-completeness-axiom": "cpm-c01-05.html", "prp-t1-0011": "cpm-c01-05.html", "prp-t1-0012": "cpm-c01-05.html", "exm-t1-0016": "cpm-c01-05.html", "sec-t1-c02-06": "cpm-c01-06.html", "thm-t1-0002": "cpm-c01-06.html", "sec-t1-c02-07": "cpm-c01-07.html", "thm-t1-0003": "cpm-c01-07.html", "cor-t1-0002": "cpm-c01-07.html", "cor-t1-0003": "cpm-c01-07.html", "lem-t1-0001": "cpm-c01-07.html", "sec-t1-c02-08": "cpm-c01-08.html", "def-t1-0018": "cpm-c01-08.html", "thm-t1-0004": "cpm-c01-08.html", "exm-t1-0017": "cpm-c01-08.html", "thm-t1-0005": "cpm-c01-08.html", "sec-t1-c02-09": "cpm-c01-09.html", "thm-t1-0006": "cpm-c01-09.html", "exm-t1-0018": "cpm-c01-09.html", "cor-t1-0004": "cpm-c01-09.html", "exm-t1-0019": "cpm-c01-09.html", "sec-t1-c02-10": "cpm-c01-10.html", "sec-t1-c02-11": "cpm-c01-11.html", "exr-t1-0036": "cpm-c01-11.html", "exr-t1-0037": "cpm-c01-11.html", "exr-t1-0038": "cpm-c01-11.html", "exr-t1-0039": "cpm-c01-11.html", "exr-t1-0040": "cpm-c01-11.html", "exr-t1-0041": "cpm-c01-11.html", "exr-t1-0042": "cpm-c01-11.html", "exr-t1-0043": "cpm-c01-11.html", "exr-t1-0044": "cpm-c01-11.html", "exr-t1-0045": "cpm-c01-11.html", "exr-t1-0046": "cpm-c01-11.html", "exr-t1-0047": "cpm-c01-11.html", "exr-t1-0048": "cpm-c01-11.html", "exr-t1-0049": "cpm-c01-11.html", "exr-t1-0050": "cpm-c01-11.html", "exr-t1-0051": "cpm-c01-11.html", "exr-t1-0052": "cpm-c01-11.html", "exr-t1-0053": "cpm-c01-11.html", "exr-t1-0054": "cpm-c01-11.html", "exr-t1-0055": "cpm-c01-11.html", "exr-t1-0056": "cpm-c01-11.html", "exr-t1-0057": "cpm-c01-11.html", "exr-t1-0058": "cpm-c01-11.html", "exr-t1-0059": "cpm-c01-11.html", "exr-t1-0060": "cpm-c01-11.html", "exr-t1-0061": "cpm-c01-11.html", "exr-t1-0062": "cpm-c01-11.html", "exr-t1-0063": "cpm-c01-11.html", "exr-t1-0064": "cpm-c01-11.html", "exr-t1-0065": "cpm-c01-11.html", "exr-t1-0066": "cpm-c01-11.html", "exr-t1-0067": "cpm-c01-11.html", "exr-t1-0068": "cpm-c01-11.html", "exr-t1-0069": "cpm-c01-11.html", "exr-t1-0070": "cpm-c01-11.html", "exr-t1-0071": "cpm-c01-11.html", "exr-t1-0072": "cpm-c01-11.html", "exr-t1-0073": "cpm-c01-11.html", "exr-t1-0074": "cpm-c01-11.html", "exr-t1-0075": "cpm-c01-11.html", "cpm-c01-soluciones": "cpm-c01-soluciones.html", "sol-t1-0036": "cpm-c01-soluciones.html", "sol-t1-0037": "cpm-c01-soluciones.html", "sol-t1-0038": "cpm-c01-soluciones.html", "sol-t1-0039": "cpm-c01-soluciones.html", "sol-t1-0040": "cpm-c01-soluciones.html", "sol-t1-0041": "cpm-c01-soluciones.html", "sol-t1-0042": "cpm-c01-soluciones.html", "sol-t1-0043": "cpm-c01-soluciones.html", "sol-t1-0044": "cpm-c01-soluciones.html", "sol-t1-0045": "cpm-c01-soluciones.html", "sol-t1-0046": "cpm-c01-soluciones.html", "sol-t1-0047": "cpm-c01-soluciones.html", "sol-t1-0048": "cpm-c01-soluciones.html", "sol-t1-0049": "cpm-c01-soluciones.html", "sol-t1-0050": "cpm-c01-soluciones.html", "sol-t1-0051": "cpm-c01-soluciones.html", "sol-t1-0052": "cpm-c01-soluciones.html", "sol-t1-0053": "cpm-c01-soluciones.html", "sol-t1-0054": "cpm-c01-soluciones.html", "sol-t1-0055": "cpm-c01-soluciones.html", "sol-t1-0056": "cpm-c01-soluciones.html", "sol-t1-0057": "cpm-c01-soluciones.html", "sol-t1-0058": "cpm-c01-soluciones.html", "sol-t1-0059": "cpm-c01-soluciones.html", "sol-t1-0060": "cpm-c01-soluciones.html", "sol-t1-0061": "cpm-c01-soluciones.html", "sol-t1-0062": "cpm-c01-soluciones.html", "sol-t1-0063": "cpm-c01-soluciones.html", "sol-t1-0064": "cpm-c01-soluciones.html", "sol-t1-0065": "cpm-c01-soluciones.html", "sol-t1-0066": "cpm-c01-soluciones.html", "sol-t1-0067": "cpm-c01-soluciones.html", "sol-t1-0068": "cpm-c01-soluciones.html", "sol-t1-0069": "cpm-c01-soluciones.html", "sol-t1-0070": "cpm-c01-soluciones.html", "sol-t1-0071": "cpm-c01-soluciones.html", "sol-t1-0072": "cpm-c01-soluciones.html", "sol-t1-0073": "cpm-c01-soluciones.html", "sol-t1-0074": "cpm-c01-soluciones.html", "sol-t1-0075": "cpm-c01-soluciones.html"}</script>
<script>
(function () {
  function followAnchor() {
    const anchor = decodeURIComponent(location.hash.slice(1));
    const routes = JSON.parse(document.getElementById("cpm-c01-anchor-routes").textContent);
    if (Object.hasOwn(routes, anchor)) location.replace(routes[anchor] + location.hash);
  }
  followAnchor();
  window.addEventListener("hashchange", followAnchor);
})();
</script>
```

[Índice del Tomo I](../para-matematicos/calculo-para-matematicos.md) · [Capítulo 2 →](funciones-reales-estructura-composicion-inversas-y-graficas.md)
