# 3F · Dualidad — primera unidad: funcionales, bases duales y aplicación dual

**Estado:** `BORRADOR COTEJADO EN ALCANCE 3.108–3.118 / 3F INCOMPLETA`. **Procedencia:** `[TRAD]` traducción de trabajo no oficial de Sheldon Axler, *Linear Algebra Done Right*, cuarta edición, PDF del autor fechado 16-08-2026, pp. 105–107. Licencia CC BY-NC 4.0. Se conservan la notación del autor `V'`, `T'` y las ecuaciones 3.115 y 3.117. **No** se presentan aquí los resultados 3.119 y siguientes ni los ejercicios de 3F.

## Espacio dual y aplicación dual

Las aplicaciones lineales cuyo espacio de llegada es el cuerpo de escalares desempeñan un papel especial en álgebra lineal; por ello reciben un nombre propio.

### 3.108 Definición: funcional lineal

Un **funcional lineal** sobre $V$ es una aplicación lineal de $V$ en $\mathbf F$; equivale a un elemento de $\mathcal L(V,\mathbf F)$.

### 3.109 Ejemplos: funcionales lineales

- $\varphi:\mathbf R^3\to\mathbf R$, definida por $\varphi(x,y,z)=4x-5y+2z$.
- Fijados $c_1,\ldots,c_n\in\mathbf F$, la aplicación $\varphi:\mathbf F^n\to\mathbf F$ dada por $\varphi(x_1,\ldots,x_n)=c_1x_1+\cdots+c_nx_n$.
- Sobre $\mathcal P(\mathbf R)$, el funcional $\varphi(p)=3p''(5)+7p(4)$.
- Sobre $\mathcal P(\mathbf R)$, el funcional $\varphi(p)=\int_0^1 p(x)\,dx$.

### 3.110 Definición: espacio dual, $V'$

El **espacio dual** de $V$, denotado por $V'$, es el espacio vectorial de todos los funcionales lineales sobre $V$:

$$\boxed{V'=\mathcal L(V,\mathbf F).}$$

### 3.111 Dimensión del espacio dual

Si $V$ tiene dimensión finita, también la tiene $V'$, y

$$\boxed{\dim V'=\dim V.}$$

**Demostración.** Por 3.72,

$$\dim V'=\dim\mathcal L(V,\mathbf F)=(\dim V)(\dim\mathbf F)=\dim V,$$

pues $\mathbf F$ tiene dimensión uno sobre sí mismo.

### 3.112 Definición: base dual

Si $v_1,\ldots,v_n$ es una base de $V$, su **base dual** es la lista $\varphi_1,\ldots,\varphi_n$ de elementos de $V'$ definida mediante

$$\varphi_j(v_k)=\begin{cases}1,&k=j,\\0,&k\ne j.\end{cases}$$

Cada funcional queda bien definido por el lema de la aplicación lineal 3.4, que garantiza la existencia y unicidad de una aplicación lineal con esos valores prescritos sobre una base.

### 3.113 Ejemplo: dual de la base estándar

En $\mathbf F^n$, para $n\ge1$, el funcional coordenada $\varphi_j$ viene dado por

$$\varphi_j(x_1,\ldots,x_n)=x_j.$$

Si $e_1,\ldots,e_n$ es la base estándar, entonces $\varphi_j(e_k)=1$ si $j=k$ y vale $0$ en caso contrario. Por ello $\varphi_1,\ldots,\varphi_n$ constituye su base dual.

### 3.114 La base dual proporciona los coeficientes de una combinación lineal

Sean $v_1,\ldots,v_n$ una base de $V$ y $\varphi_1,\ldots,\varphi_n$ su base dual. Para cada $v\in V$,

$$\boxed{v=\varphi_1(v)v_1+\cdots+\varphi_n(v)v_n.}$$

**Demostración.** Escribamos, de manera única,

$$\tag{3.115}v=c_1v_1+\cdots+c_nv_n.$$

Al aplicar $\varphi_j$ a ambos miembros se obtiene $\varphi_j(v)=c_j$; reemplazando cada coeficiente en 3.115 resulta la identidad buscada.

### 3.116 La base dual es una base del espacio dual

Si $V$ es de dimensión finita, la base dual de cualquier base de $V$ es una base de $V'$.

**Demostración.** Sean $v_1,\ldots,v_n$ una base de $V$ y $\varphi_1,\ldots,\varphi_n$ su base dual. Si

$$\tag{3.117}a_1\varphi_1+\cdots+a_n\varphi_n=0,$$

aplicar el funcional cero y la suma del lado izquierdo a $v_k$ produce $a_k=0$ para todo $k$. Luego la lista dual es linealmente independiente. Su longitud es $n=\dim V'$ por 3.111; el criterio 2.38 implica que constituye una base.

### 3.118 Definición: aplicación dual, $T'$

Para $T\in\mathcal L(V,W)$, la **aplicación dual** es

$$\boxed{T':W'\longrightarrow V',\qquad T'(\varphi)=\varphi\circ T.}$$

La inversión de dirección es esencial: un funcional sobre $W$, precompuesto con $T:V\to W$, se convierte en un funcional sobre $V$. Para $\varphi,\psi\in W'$ y $\lambda\in\mathbf F$,

$$T'(\varphi+\psi)=(\varphi+\psi)\circ T=T'(\varphi)+T'(\psi),$$

$$T'(\lambda\varphi)=(\lambda\varphi)\circ T=\lambda T'(\varphi).$$

Esto comprueba que $T'$ es lineal. La prima en $T'$ indica dualidad; cuando se aplique a un polinomio $p'$, indicará derivación, distinción que se hace explícita al comienzo de 3.119.

---

**Límite de publicación:** 3F no está completa; faltan 3.119 en adelante, ejercicios y soluciones, aparato, glosario y QA de sección. No contabilizar nuevos ejercicios con esta primera unidad.