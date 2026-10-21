# Capítulo 3 · Aplicaciones lineales

**Estado:** `COTEJADO`  
**Fuente:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª ed., PDF oficial de 16-08-2026, p. 51.  
**Licencia:** adaptación/traducción no oficial bajo CC BY-NC 4.0.  
**Control de erratas:** la errata oficial vigente no registra correcciones para la p. 51.

> [TRAD] Traducción de trabajo de Matemática Abierta. Se preservan estructura, contenido matemático y supuestos del capítulo.

Hasta ahora nuestra atención se ha centrado en los espacios vectoriales. Nadie se entusiasma con los espacios vectoriales. La parte interesante del álgebra lineal es el tema al que nos dirigimos ahora: las **aplicaciones lineales**.

Usaremos con frecuencia el poderoso **teorema fundamental de las aplicaciones lineales**, que afirma que la dimensión del dominio de una aplicación lineal es igual a la dimensión del subespacio que se envía a $0$ más la dimensión de la imagen. De él se deducirá el notable resultado de que una aplicación lineal de un espacio vectorial de dimensión finita en sí mismo es inyectiva si y sólo si su imagen es todo el espacio.

Un concepto central que introduciremos en este capítulo es la **matriz asociada a una aplicación lineal**, una vez elegidas una base del espacio de dominio y una base del espacio de llegada. Esta correspondencia entre aplicaciones lineales y matrices aporta una gran comprensión de aspectos fundamentales del álgebra lineal.

El capítulo concluye introduciendo espacios producto, espacios cociente y espacios duales.

En este capítulo necesitaremos, además de $V$, otros espacios vectoriales, que llamaremos $U$ y $W$. Por tanto, nuestros supuestos permanentes serán ahora los siguientes.

## Supuestos permanentes para este capítulo

- $\mathbf F$ denota $\mathbf R$ o $\mathbf C$.
- $U$, $V$ y $W$ denotan espacios vectoriales sobre $\mathbf F$.

> [NOTA editorial] La edición original incluye en esta página una fotografía de Dankwarderode Castle acreditada a Stefan Schäfer bajo CC BY-SA. La imagen no se reproduce en esta edición de trabajo; antes de incorporarla a una edición final deberá tratarse por separado su atribución y licencia.

---

**Atribución:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª edición. Traducción/adaptación no oficial realizada para Matemática Abierta bajo CC BY-NC 4.0. Fuente oficial: <https://linear.axler.net/>.
