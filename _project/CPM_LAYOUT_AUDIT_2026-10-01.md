# Auditoría de maquetación y ayudas visuales — Tomo I

Fecha: 2026-10-01. Alcance: los 20 capítulos publicados de Cálculo para matemáticos. Esta auditoría examina la estructura de fuentes, el comportamiento del HTML y una muestra visual de expresiones complejas; no sustituye una revisión matemática ni la lectura visual completa del libro.

## Hallazgos y correcciones

- Antes de esta intervención había 64 figuras repartidas entre 7 capítulos; 13 capítulos carecían de figuras. Se añaden 16 diagramas reproducibles, con fuentes SVG y PNG, hasta alcanzar 80 figuras y una ayuda visual central como mínimo en cada capítulo. Tener una figura no equivale a una cobertura visual suficiente de todos sus temas.
- El capítulo visible 13 pasa de 8 a 11 figuras. Las tres nuevas representan área bajo una parábola, rectángulos inferiores y superiores para un borde curvo y contribuciones positivas y negativas de una cúbica. El texto distingue motivación geométrica, construcción mediante sumas y teoría posterior con signo.
- Las expresiones complejas tenían márgenes estrechos. La hoja compartida del libro amplía el espacio entre texto y fórmulas, concede más aire a fracciones y sistemas, y protege el borde inferior dentro del contenedor desplazable de MathJax.
- Se unifican márgenes, anchura y pies de figuras. Los bloques identificados como definiciones, teoremas, lemas, proposiciones y corolarios reciben una presentación común cuando no usan ya un callout.
- Las tablas y fórmulas en línea demasiado anchas tienen desplazamiento local también en tabletas. La cuadrícula principal puede encogerse sin ampliar toda la página.

## Inventario por capítulo

Los recuentos de fórmulas proceden de bloques delimitados por doble dólar en las fuentes. La columna «complejas» es una clasificación estructural que detecta fracciones, sumas, integrales y entornos de varias líneas; no mide dificultad matemática.

| Capítulo | Título | Figuras antes → después | Fórmulas separadas | Complejas | Siguiente ayuda visual prioritaria |
|---|---|---:|---:|---:|---|
| 1 | Los números reales: axiomas de cuerpo, orden y completitud | 0 → 1 | 1759 | 329 | Supremo e ínfimo; huecos racionales y completitud. |
| 2 | Funciones reales: estructura, composición, inversas y gráficas | 0 → 1 | 1098 | 92 | Imagen y preimagen; inyectividad, sobreyectividad y ramas. |
| 3 | Sucesiones y la primera noción rigurosa de límite | 0 → 1 | 1168 | 364 | Oscilación, subsucesiones y sucesiones de Cauchy. |
| 4 | Límites de funciones | 0 → 1 | 1204 | 293 | Límites laterales, agujeros y límites en infinito. |
| 5 | Continuidad en la recta: intervalos, compacidad y teoremas fundamentales | 0 → 1 | 1213 | 186 | Valor intermedio, bisección y compacidad. |
| 6 | La derivada y la aproximación lineal local | 0 → 1 | 851 | 269 | No diferenciabilidad y aproximación afín local. |
| 7 | Álgebra de derivadas y regla de la cadena | 0 → 1 | 233 | 137 | Producto como variación de dos factores; cadena en puntos interiores. |
| 8 | Derivación de funciones elementales, inversas e implícitas | 0 → 1 | 199 | 115 | Ramas inversas y curvas implícitas. |
| 9 | Teoremas de Rolle y del valor medio | 0 → 1 | 161 | 62 | Contraejemplos al retirar hipótesis de Rolle y valor medio. |
| 10 | Monotonía, extremos, convexidad y forma de las gráficas | 0 → 1 | 126 | 48 | Cambios de signo, extremos e inflexión. |
| 11 | Derivadas superiores y fórmula de Taylor con resto | 0 → 1 | 331 | 123 | Restos de Taylor y diferencia entre polinomio y serie. |
| 12 | Aproximación, método de Newton y problemas de optimización | 0 → 1 | 588 | 303 | Intervalos certificados y comportamiento de Newton fuera de sus hipótesis. |
| 13 | Del área y las sumas a la integral | 8 → 11 | 691 | 356 | Lectura conjunta de particiones, oscilación y contribuciones con signo. |
| 14 | Integral de Riemann: definición, integrabilidad y propiedades | 14 → 14 | 625 | 282 | Integrabilidad y brecha entre sumas; conservar el juego de 14 figuras. |
| 15 | Teoremas de valor medio para integrales | 10 → 10 | 343 | 198 | Comparación visual de medias y ponderaciones; conservar las 10 figuras. |
| 16 | Teorema fundamental del cálculo | 9 → 9 | 532 | 255 | Acumulación y derivación; conservar las 9 figuras. |
| 17 | Logaritmo, exponencial y funciones relacionadas desde el cálculo | 10 → 10 | 837 | 280 | Construcción de logaritmo y exponencial; conservar las 10 figuras. |
| 18 | Técnicas de integración | 8 → 8 | 832 | 526 | Elección del método de integración; conservar las 8 figuras. |
| 19 | Aplicaciones geométricas y cuantitativas de la integral | 0 → 1 | 825 | 346 | Cruce de curvas, arandelas, cascarones y longitud de arco. |
| 20 | Ecuaciones diferenciales elementales y síntesis Newton–Leibniz | 5 → 5 | 121 | 61 | Campos de pendientes y condiciones iniciales; conservar las 5 figuras. |

## Evidencia y validación

- Línea base: ejecución de navegador 36810437685, con 20 capítulos en anchuras 320, 390, 600, 768 y 1440 px. Pasaron 98 de las 100 comprobaciones. Los fallos fueron desbordamientos globales a 768 px en los capítulos visibles 5 y 10; las comprobaciones no registraron errores de MathJax, imágenes rotas, referencias sin resolver ni identificadores duplicados.
- Reproducción local con MathJax 3.2.2 y Chrome: los capítulos 5 y 10 desbordaban a 835 y 779 px, respectivamente. Con la hoja corregida ambos miden 768 px, igual a la ventana. La diferencia con los 824 y 805 px de la línea base refleja el navegador y el entorno tipográfico; ambos ensayos detectan el mismo defecto.
- Revisión de los 16 diagramas en hojas de contacto y comprobación geométrica de las cajas de texto: ningún rótulo sale del lienzo. Las figuras usan funciones y valores explícitos y se generan desde código; las fuentes SVG permiten futuras correcciones.
- Integridad de fuentes: 20 capítulos, 800 pares de ejercicios y soluciones, 2462 anclas únicas, 80 archivos PNG referenciados y destinos internos conservados.
- La nueva ejecución completa de Quarto y navegador en CI acompaña la solicitud de integración. Sus resultados y capturas son la evidencia final del HTML regenerado; el ensayo local usa el HTML de la línea base con la hoja CSS nueva.

## Límites y revisión siguiente

Las correcciones de esta ronda afectan al HTML. PDF, EPUB y los estilos de lectura de Obsidian requieren controles separados. Las nuevas ilustraciones sí pertenecen a las fuentes canónicas y pueden reutilizarse en esas salidas.

La revisión visual posterior debe recorrer las fórmulas más largas, comprobar el ritmo de lectura alrededor de demostraciones extensas y valorar la densidad de figuras por sección. Conviene revisar también la repetición del título del capítulo entre la cabecera de página y el encabezado del manuscrito antes de decidir un cambio editorial uniforme. Las prioridades de la tabla son trabajo pendiente explícito, no un certificado de cobertura completa.
