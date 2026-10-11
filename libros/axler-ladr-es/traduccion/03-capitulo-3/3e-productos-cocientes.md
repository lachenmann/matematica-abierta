# 3E · Productos y cocientes de espacios vectoriales

**Estado:** `TRADUCCIÓN DE TRABAJO / PRIMERA PASADA; QA EDITORIAL PENDIENTE`.  
**Fuente canónica:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª ed., PDF oficial 16-08-2026, pp. 96–102.  
**Procedencia:** `[TRAD]` traducción no oficial de Matemática Abierta, CC BY-NC 4.0; los complementos propios, donde se señalan, llevan `[NOTA]`. Los ejercicios están en archivo independiente.  
**Control de erratas:** no hay entrada específica de la errata oficial para pp. 96–104 en la consulta del 16-09-2026.

## Productos de espacios vectoriales

Al trabajar simultáneamente con varios espacios vectoriales, se supone que todos están definidos sobre un mismo cuerpo.

### 3.87 Definición: producto de espacios vectoriales

Sean $V_1,\ldots,V_m$ espacios vectoriales sobre $\mathbf F$. Se llama **producto** a

$$V_1\times\cdots\times V_m=\{(v_1,\ldots,v_m):v_k\in V_k\text{ para }1\le k\le m\}.$$

En el producto, la suma y la multiplicación por escalares se calculan componente a componente:

$$(u_1,\ldots,u_m)+(v_1,\ldots,v_m)=(u_1+v_1,\ldots,u_m+v_m),$$

$$\lambda(v_1,\ldots,v_m)=(\lambda v_1,\ldots,\lambda v_m).$$

### 3.88 Ejemplo: $\mathcal P_5(\mathbf R)\times\mathbf R^3$

Los elementos son pares: la primera componente es un polinomio de grado a lo sumo cinco y la segunda es una terna real. Por ejemplo,

$$(5-6x+4x^2,(3,8,7))+(x+9x^5,(2,2,2))$$

$$=(5-5x+4x^2+9x^5,(5,10,9)).$$

Asimismo, dos veces el primer elemento es $(10-12x+8x^2,(6,16,14))$.

### 3.89 El producto es un espacio vectorial

**Resultado.** El producto $V_1\times\cdots\times V_m$, provisto de las operaciones de 3.87, es un espacio vectorial sobre $\mathbf F$.

La demostración de los axiomas se deja al lector en el original. Su vector cero es $(0,\ldots,0)$, con el cero correspondiente a cada factor, y el inverso aditivo de $(v_1,\ldots,v_m)$ es $(-v_1,\ldots,-v_m)$.

### 3.90 Ejemplo: producto e isomorfismo no son igualdad

Los elementos de $\mathbf R^2\times\mathbf R^3$ son pares de listas: $((x_1,x_2),(x_3,x_4,x_5))$. En cambio, un elemento de $\mathbf R^5$ es una única lista de longitud cinco. En consecuencia, estos espacios no son literalmente iguales. Sin embargo, la aplicación

$$((x_1,x_2),(x_3,x_4,x_5))\longmapsto(x_1,x_2,x_3,x_4,x_5)$$

es un isomorfismo: ambos espacios tienen la misma estructura lineal expresada con dos maneras de agrupar coordenadas.

### 3.91 Ejemplo: base de $\mathcal P_2(\mathbf R)\times\mathbf R^2$

Una base de este producto es

$$(1,(0,0)),\quad(x,(0,0)),\quad(x^2,(0,0)),\quad(0,(1,0)),\quad(0,(0,1)).$$

Los cinco elementos son linealmente independientes, porque anular una combinación exige anular separadamente los tres coeficientes del polinomio y las dos coordenadas; también generan todos los pares $(p,(a,b))$.

### 3.92 La dimensión de un producto es la suma de las dimensiones

**Teorema.** Si $V_1,\ldots,V_m$ tienen dimensión finita, el producto también la tiene y

$$\boxed{\dim(V_1\times\cdots\times V_m)=\dim V_1+\cdots+\dim V_m.}$$

**Demostración.** Elíjase una base de cada factor. Por cada vector de una de esas bases, fórmese el elemento del producto que lo tiene en su componente correspondiente y tiene cero en las demás. La lista formada por todos estos elementos genera el producto: cada componente se expresa en su base y luego se insertan sus sumandos en el producto. Es independiente: una combinación nula tiene todas las componentes nulas, y la independencia de la base de cada factor anula cada coeficiente. La cantidad de elementos de la base construida es la suma indicada.

### 3.93 Productos y sumas directas

Sean $V_1,\ldots,V_m$ subespacios de $V$. Definamos la aplicación lineal

$$\Gamma:V_1\times\cdots\times V_m\longrightarrow V_1+\cdots+V_m,\qquad\Gamma(v_1,\ldots,v_m)=v_1+\cdots+v_m.$$

**Resultado.** La suma $V_1+\cdots+V_m$ es directa si y solo si $\Gamma$ es inyectiva.

**Demostración.** Por el criterio de inyectividad 3.15, $\Gamma$ es inyectiva exactamente cuando su espacio nulo contiene solo la tupla cero; es decir, cuando la única representación de $0$ como $v_1+\cdots+v_m$, con $v_k\in V_k$, tiene todos los sumandos nulos. Esta es la condición de 1.45. Además, $\Gamma$ es sobreyectiva por la definición misma de suma de subespacios, de modo que «inyectiva» puede sustituirse por «invertible».

### 3.94 Criterio dimensional de suma directa

**Teorema.** Si $V$ tiene dimensión finita y $V_1,\ldots,V_m$ son subespacios suyos, entonces

$$V_1+\cdots+V_m\text{ es suma directa}\iff\dim(V_1+\cdots+V_m)=\sum_{k=1}^{m}\dim V_k.$$

**Demostración.** La aplicación $\Gamma$ de 3.93 es sobreyectiva. Por 3.21, es inyectiva si y solo si su dominio y su imagen tienen la misma dimensión. Sustituyendo la dimensión de su dominio por la fórmula 3.92 y aplicando 3.93 se obtiene la equivalencia. Cuando $m=2$, también puede combinarse 1.46 con 2.43.

## Espacios cociente

### 3.95 Notación: $v+U$

Si $v\in V$ y $U\subseteq V$, denotamos por

$$v+U=\{v+u:u\in U\}$$

el conjunto obtenido al sumar $v$ a cada elemento de $U$.

### 3.96 Ejemplo: trasladar una recta de $\mathbf R^2$

Para $U=\{(x,2x):x\in\mathbf R\}$, la recta $(17,20)+U$ tiene pendiente $2$ y pasa por $(17,20)$. Como $(10,20)\in U$, puede describirse como el desplazamiento de $U$ siete unidades a la derecha. `[NOTA · accesibilidad]` Equivalente textual del diagrama del original: dos rectas paralelas de pendiente 2; una pasa por el origen y $(10,20)$, la otra por $(17,20)$.

### 3.97 Definición: trasladado

El conjunto $v+U$ se denomina un **trasladado** de $U$.

### 3.98 Ejemplos: trasladados

Los trasladados de una recta por el origen en $\mathbf R^2$ son las rectas paralelas a ella; en particular, los de $U=\{(x,2x)\}$ son las rectas de pendiente $2$. Si $U=\{(x,y,0):x,y\in\mathbf R\}$, sus trasladados son los planos paralelos al plano $xy$ en $\mathbf R^3$. De manera general, trasladar un plano por el origen produce todos los planos paralelos a él.

### 3.99 Definición: espacio cociente $V/U$

Si $U$ es un subespacio de $V$, el **espacio cociente** se define, en primer término, como el conjunto de todos los trasladados de $U$:

$$\boxed{V/U=\{v+U:v\in V\}.}$$

### 3.100 Ejemplos: espacios cociente

Si $U$ es la recta de pendiente $2$ por el origen en $\mathbf R^2$, entonces $\mathbf R^2/U$ consiste en todas las rectas de esa pendiente. Si $U$ es una recta por el origen en $\mathbf R^3$, el cociente consiste en las rectas paralelas a ella; cuando $U$ es un plano por el origen en $\mathbf R^3$, consiste en los planos paralelos correspondientes.

### 3.101 Dos trasladados de un subespacio son iguales o disjuntos

**Proposición.** Sean $U\le V$ y $v,w\in V$. Entonces son equivalentes las tres condiciones

$$\boxed{v-w\in U\iff v+U=w+U\iff(v+U)\cap(w+U)\ne\varnothing.}$$

**Demostración.** Si $v-w\in U$, para todo $u\in U$ tenemos $v+u=w+((v-w)+u)\in w+U$; esto da una inclusión, y la otra es simétrica. La igualdad de trasladados implica inmediatamente una intersección no vacía. Por último, un elemento común puede escribirse $v+u_1=w+u_2$ con $u_1,u_2\in U$; de ahí $v-w=u_2-u_1\in U$.

### 3.102 Definición: operaciones en el cociente

Para $U\le V$, $v,w\in V$ y $\lambda\in\mathbf F$, se proponen las operaciones

$$(v+U)+(w+U)=(v+w)+U,\qquad\lambda(v+U)=(\lambda v)+U.$$

Es necesario probar que no dependen de los representantes escogidos.

### 3.103 El cociente es un espacio vectorial

**Teorema.** Con las operaciones de 3.102, $V/U$ es un espacio vectorial.

**Demostración.** Si $v_1+U=v_2+U$ y $w_1+U=w_2+U$, 3.101 garantiza que $v_1-v_2$ y $w_1-w_2$ pertenecen a $U$. Por cierre bajo la suma, $(v_1+w_1)-(v_2+w_2)\in U$; de nuevo por 3.101, la suma de clases es independiente de sus representantes. Análogamente, $\lambda(v_1-v_2)\in U$ implica $(\lambda v_1)+U=(\lambda v_2)+U$: la multiplicación por escalares también está bien definida. Las restantes leyes vectoriales se heredan de $V$ al operar con representantes, ahora legítimamente. El cero es $0+U=U$ y el inverso aditivo de $v+U$ es $(-v)+U$.

### 3.104 Definición: aplicación cociente $\pi$

Para $U\le V$, la **aplicación cociente** es

$$\pi:V\longrightarrow V/U,\qquad\pi(v)=v+U.$$

Es lineal por 3.102; depende del subespacio $U$, que se omite de la notación cuando no hay ambigüedad. Es sobreyectiva por 3.99.

### 3.105 Dimensión de un espacio cociente

**Teorema.** Si $V$ tiene dimensión finita y $U\le V$, entonces

$$\boxed{\dim(V/U)=\dim V-\dim U.}$$

**Demostración.** Como $v+U=0+U$ si y solo si $v\in U$ (3.101), se tiene $\operatorname{null}\pi=U$. Además, $\operatorname{range}\pi=V/U$. Aplicar 3.21 a $\pi$ da $\dim V=\dim U+\dim(V/U)$, y basta despejar.

### 3.106 Notación: $\widetilde T$

Dada $T\in\mathcal L(V,W)$, definimos la aplicación inducida

$$\widetilde T:V/(\operatorname{null}T)\longrightarrow W,\qquad\widetilde T(v+\operatorname{null}T)=Tv.$$

Está **bien definida**: si $u+\operatorname{null}T=v+\operatorname{null}T$, 3.101 implica $u-v\in\operatorname{null}T$, por lo que $Tu=Tv$. La linealidad se verifica usando 3.102 y la linealidad de $T$.

### 3.107 Espacio nulo e imagen de $\widetilde T$

**Teorema.** Para $T\in\mathcal L(V,W)$ y la proyección cociente $\pi:V\to V/(\operatorname{null}T)$:

(a) $\widetilde T\circ\pi=T$; (b) $\widetilde T$ es inyectiva; (c) $\operatorname{range}\widetilde T=\operatorname{range}T$; (d) $V/(\operatorname{null}T)$ es isomorfo a $\operatorname{range}T$.

**Demostración.** Para (a), $(\widetilde T\circ\pi)(v)=\widetilde T(v+\operatorname{null}T)=Tv$. Para (b), si $\widetilde T(v+\operatorname{null}T)=0$, entonces $v\in\operatorname{null}T$, de modo que $v+\operatorname{null}T$ es el cero del cociente; su espacio nulo es trivial. La definición da (c) directamente: ambas imágenes están formadas por los vectores $Tv$. En (d), considérense las mismas asignaciones con espacio de llegada restringido a $\operatorname{range}T$: por (b) y (c) constituyen un isomorfismo.

**Relación de dependencia:** (d) también es válido sin suponer dimensión finita. No debe confundirse la identificación por isomorfismo con la igualdad literal del cociente y la imagen.

---

**Próximo control:** cotejo tipográfico final de la figura 3.96, referencias, 19 ejercicios y soluciones propias; no promover a `CERRADO` antes del QA.