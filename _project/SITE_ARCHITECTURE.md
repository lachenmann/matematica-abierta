# Arquitectura del sitio — Matemática Abierta

## Propósito

Esta arquitectura organiza el sitio por dos ejes complementarios:

1. **forma de estudio**: teoría, problemas, cursos y libros;
2. **forma de exploración**: áreas, temas, artículos y recursos de referencia.

La estructura debe poder crecer sin exigir reorganizaciones frecuentes ni romper URLs ya publicadas.

## Navegación principal canónica

- Inicio
- Teoría
- Problemas
- Cursos
- Libros
- Explorar
- Proyecto

## 1. Inicio

La portada general del proyecto.

Debe ofrecer acceso rápido a:

- contenidos recientes;
- rutas de entrada recomendadas;
- teoría;
- problemas;
- cursos;
- libros;
- exploración por áreas.

## 2. Teoría

Portada: `teoria/index.qmd`.

Subsecciones canónicas:

### 2.1 Conceptos

Ruta pública existente: `conceptos/`.

Páginas autocontenidas dedicadas a una idea matemática concreta, con definición, interpretación, hipótesis, ejemplos, resultados básicos y conexiones.

### 2.2 Resultados y teoremas

Índice de resultados matemáticos que merezcan una entrada o referencia independiente: teoremas, proposiciones, lemas, corolarios e identidades relevantes.

### 2.3 Métodos y técnicas

Procedimientos reutilizables de resolución, demostración o cálculo: factorización, completar cuadrados, inducción, sustituciones, estimaciones, análisis de signos, etc.

### 2.4 Mapas y conexiones

Páginas de síntesis que conectan varias piezas de teoría y muestran dependencias conceptuales, equivalencias y rutas entre temas.

Estas subsecciones son vistas editoriales del corpus teórico; no obligan por sí solas a introducir nuevos prefijos de ID.

## 3. Problemas

Portada existente: `problemas/index.qmd`.

Subsecciones canónicas:

### 3.1 Todos los problemas

Banco completo de problemas publicados.

### 3.2 Por área

Agrupación por taxonomía matemática.

### 3.3 Por técnica

Agrupación por métodos principales de resolución.

### 3.4 Por dificultad

Niveles `1` a `5`.

### 3.5 Colecciones

Series editoriales de problemas, incluida la línea `PM-PRB — Problemas para matemáticos` y futuras colecciones temáticas.

Regla permanente: ningún problema puede publicarse sin `solution-status: complete`.

## 4. Cursos

Portada existente: `cursos/index.qmd`.

Subsecciones canónicas:

### 4.1 Cursos

Itinerarios sistemáticos y secuenciales organizados mediante entidades `course` y unidades `lesson`.

### 4.2 Rutas de estudio

Recorridos que combinan teoría, problemas, capítulos y artículos sin necesidad de constituir un curso formal completo.

### 4.3 Lecciones

Índice de las unidades pedagógicas publicadas, navegables también fuera de la estructura de un curso.

## 5. Libros

Portada existente: `libros/index.qmd`.

Subsecciones canónicas:

### 5.1 Colección Para matemáticos

Colección editorial principal.

- `PM-FUN` — Fundamentos para matemáticos
- `PM-CAL` — Cálculo para matemáticos
- `PM-GEO` — Geometría para matemáticos
- `PM-ANA` — Análisis para matemáticos
- `PM-TOP` — Topología para matemáticos
- `PM-EDO` — Ecuaciones diferenciales para matemáticos
- `PM-PRO` — Probabilidad para matemáticos
- `PM-DIS` — Matemática discreta para matemáticos
- `PM-NUM` — Teoría de números para matemáticos
- `PM-COM` — Análisis complejo para matemáticos
- `PM-FIS` — Física para matemáticos
- `PM-PRB` — Problemas para matemáticos

Los capítulos pueden publicarse progresivamente sin esperar al cierre del libro completo.

### 5.2 Otros libros y monografías

Espacio para futuros libros abiertos que no pertenezcan a la colección Para matemáticos.

### 5.3 Capítulos publicados

Índice transversal de capítulos disponibles, independientemente del estado global del libro padre.

## 6. Explorar

Esta sección agrupa formas transversales de recorrer el sitio.

### 6.1 Áreas

Áreas matemáticas canónicas:

- Fundamentos
- Álgebra
- Cálculo
- Geometría
- Análisis
- Topología
- Ecuaciones diferenciales
- Probabilidad
- Matemática discreta
- Teoría de números
- Análisis complejo
- Física matemática

Cada página de área debe agregar teoría, problemas, cursos, libros y artículos relacionados.

### 6.2 Índice temático

Índice por `topics`, más específico que las áreas.

Ejemplos: números reales, desigualdades, valor absoluto, límites, continuidad, espacios métricos.

### 6.3 Artículos

La carpeta pública existente `blog/` se conserva para preservar URLs, pero su función editorial será **Artículos**.

Los artículos son piezas independientes que no pertenecen necesariamente a una secuencia de curso o libro. Pueden incluir:

- ensayos matemáticos;
- historia de las matemáticas;
- conexiones amplias;
- estrategias de estudio;
- notas editoriales de interés público.

No deben duplicar páginas conceptuales cuya función natural pertenezca a Teoría.

### 6.4 Bibliografía

Vista pública de la bibliografía maestra `references.bib`, con posibilidad futura de navegación por autores, obras y áreas.

### 6.5 Notación y convenciones

Convenciones matemáticas y editoriales utilizadas transversalmente en Matemática Abierta.

### 6.6 Glosario

Definiciones breves y referencias cruzadas para términos que no justifican por sí solos una página teórica completa.

## 7. Proyecto

Subsecciones canónicas:

### 7.1 Acerca de Matemática Abierta

Propósito, historia y filosofía del proyecto.

Ruta pública existente: `acerca-de.qmd`.

### 7.2 Política editorial

Versión pública de los principios de trabajo: estudio privado, reconstrucción, reescritura, procedencia, revisión y publicación.

### 7.3 Procedencia y derechos

Explicación pública de cómo se registran fuentes, adaptaciones, traducciones, figuras y materiales de terceros.

### 7.4 Licencia

Ruta pública existente: `licencia.qmd`.

Contenido textual original: `GFDL-1.3-or-later` salvo indicación en contrario.

### 7.5 Cómo citar Matemática Abierta

Convenciones recomendadas para citar páginas, problemas, capítulos, libros y versiones del sitio.

### 7.6 Estado y hoja de ruta

Información pública de alto nivel sobre desarrollo, colecciones activas y próximos hitos, sin exponer documentación privada de trabajo.

## Navegación secundaria y filtros

Las siguientes dimensiones son filtros transversales y no deben competir como secciones primarias:

- área;
- nivel;
- dificultad;
- técnica;
- tema;
- colección;
- estado editorial;
- procedencia.

## Elementos fuera de la navegación pública principal

### Laboratorio visual

`laboratorio-visual.qmd` es una página de QA del sistema visual. Una vez congelado WEB-0003, no debe ocupar un lugar permanente en la navegación pública principal. Puede conservarse como recurso interno o página no enlazada.

### `_project/`

Toda la carpeta `_project/` es documentación editorial interna del repositorio y no forma parte del contenido público del sitio.

## Política de URLs

- No mover páginas ya publicadas sólo para reflejar la jerarquía visual.
- Preservar `/conceptos/`, `/problemas/`, `/cursos/`, `/libros/` y `/blog/` cuando ya existan enlaces públicos.
- La jerarquía del menú y la jerarquía del sistema de archivos no tienen que ser idénticas.
- Toda migración futura de rutas debe contemplar redirecciones antes de retirar una URL pública.

## Navegación principal objetivo

```text
Inicio
Teoría
  Portada de Teoría
  Conceptos
  Resultados y teoremas
  Métodos y técnicas
  Mapas y conexiones
Problemas
  Todos los problemas
  Por área
  Por técnica
  Por dificultad
  Colecciones
Cursos
  Cursos
  Rutas de estudio
  Lecciones
Libros
  Para matemáticos
  Otros libros y monografías
  Capítulos publicados
Explorar
  Áreas
  Índice temático
  Artículos
  Bibliografía
  Notación y convenciones
  Glosario
Proyecto
  Acerca de
  Política editorial
  Procedencia y derechos
  Licencia
  Cómo citar
  Estado y hoja de ruta
```

## Estado

Esta es la arquitectura de información v1 de Matemática Abierta. Debe considerarse estable y sólo modificarse cuando exista una razón editorial clara, no por crecimiento incremental ordinario.
