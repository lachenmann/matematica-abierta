# Política editorial de Matemática Abierta

## 1. Flujo canónico

1. estudio privado en Obsidian / Drive;
2. comprensión matemática;
3. extracción y reconstrucción;
4. reescritura editorial propia;
5. registro de procedencia;
6. revisión matemática, pedagógica, bibliográfica, jurídica y técnica;
7. publicación en el repositorio público y la web.

## 2. Privado no significa `draft`

El repositorio público no es depósito de notas privadas.

No introducir allí:

- transcripciones extensas de libros protegidos;
- notas privadas demasiado cercanas a una fuente;
- scans protegidos;
- material cuya publicación todavía no sea jurídicamente clara.

`draft: true` sólo controla la publicación normal de una página por Quarto; no vuelve privado el archivo en GitHub.

## 3. Reescritura y procedencia

Matemática Abierta estudia fuentes con rigor, pero no publica copias de apuntes o libros ajenos. La secuencia editorial es:

`fuente → comprensión → reconstrucción → texto propio → procedencia explícita`.

Una cita bibliográfica identifica procedencia, pero no concede derechos de reproducción.

## 4. Problemas

Todo problema publicado debe incluir una solución completamente desarrollada.

No puede pasar a `status: published` mientras `solution-status` no sea `complete`.

## 5. Publicación progresiva

Cursos, conceptos, problemas, artículos, libros y la colección «Para matemáticos» pueden publicarse por unidades a medida que alcancen estado editorial suficiente. No es necesario esperar a que un libro completo esté terminado.

## 6. Filosofía pedagógica

El contenido debe aspirar a combinar:

- clase explicativa;
- rigor completo;
- autonomía del autodidacta;
- transiciones fundamentales explícitas;
- ejercicios con solución desarrollada;
- QA explícito;
- procedencia bibliográfica registrada.

## 7. Markdown y Obsidian

Para nuevo contenido matemático editorial, preferir `.md` cuando no haga falta una función exclusiva de `.qmd`, para mantener compatibilidad directa con Obsidian. Los archivos técnicos y landings existentes pueden seguir en `.qmd`; no hacer migraciones masivas sólo por uniformidad.

## 8. Licencias

El contenido textual y educativo original se publica bajo GNU Free Documentation License 1.3 o posterior (`GFDL-1.3-or-later`).

El código o los scripts propios pueden usar GNU GPLv3 o posterior de forma separada cuando corresponda.

El material de terceros conserva sus derechos y licencias y no se relicencia por aparecer citado en el proyecto.
