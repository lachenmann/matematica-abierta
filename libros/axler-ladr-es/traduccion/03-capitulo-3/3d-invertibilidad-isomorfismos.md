# 3D · Invertibilidad e isomorfismos

**Estado:** `COTEJADO / PRIMERA PASADA`  
**Fuente:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª ed., PDF oficial fechado 16-08-2026, pp. 82–95.  
**Procedencia:** `[TRAD]` traducción no oficial de Matemática Abierta, CC BY-NC 4.0.  
**Control textual:** la errata oficial corrige en p. 85 el intercambio de $V$ y $W$ en la última línea del enunciado 3.68 (corrección de 29-12-2023). Se sigue el PDF actual; la copia de 2024 es solo testimonio secundario.

## Aplicaciones lineales invertibles

Comenzamos con las nociones de invertibilidad e inversa para aplicaciones lineales.

### 3.59 Definición: invertible, inversa

Una aplicación lineal $T\in\mathcal L(V,W)$ es **invertible** cuando existe $S\in\mathcal L(W,V)$ tal que $ST=I_V$ y $TS=I_W$. Una aplicación $S$ con estas propiedades se denomina *una inversa* de $T$. Es importante distinguir los dos operadores identidad: el primero actúa en $V$ y el segundo, en $W$.

### 3.60 La inversa es única

Una aplicación lineal invertible tiene una única inversa.

**Demostración.** Si $S_1$ y $S_2$ son inversas de $T$, entonces

$$S_1=S_1I_W=S_1(TS_2)=(S_1T)S_2=I_VS_2=S_2.$$ 

### 3.61 Notación: $T^{-1}$

Si $T$ es invertible, $T^{-1}$ denota su única inversa: es el único elemento de $\mathcal L(W,V)$ con $T^{-1}T=I_V$ y $TT^{-1}=I_W$.

### 3.62 Ejemplo: inversa en $\mathbf R^3$

Para $T(x,y,z)=(-y,x,4z)$, una rotación antihoraria de $90^\circ$ en el plano $xy$ acompañada de una dilatación por $4$ en la dirección $z$, la transformación inversa invierte la rotación y divide la tercera coordenada por $4$:

$$T^{-1}(x,y,z)=\left(y,-x,\frac z4\right).$$

### 3.63 Invertibilidad si y solo si inyectividad y sobreyectividad

Una aplicación lineal es invertible si y solo si es inyectiva y sobreyectiva.

**Demostración.** Si $T$ tiene inversa, $Tu=Tv$ implica $u=T^{-1}Tu=T^{-1}Tv=v$; además, cada $w\in W$ es $T(T^{-1}w)$. Recíprocamente, si $T$ es biyectiva, definimos $S(w)$ como el único $v$ con $Tv=w$. Por construcción $TS=I_W$ y $ST=I_V$. Para comprobar la linealidad, la unicidad de las preimágenes de $w_1+w_2$ y de $\lambda w$ da

$$S(w_1+w_2)=S(w_1)+S(w_2),\qquad S(\lambda w)=\lambda S(w).$$

### 3.64 Ejemplo: una sola condición no basta en dimensión infinita

La aplicación $p\mapsto x^2p$ de $\mathcal P(\mathbf R)$ en sí mismo es inyectiva, pero no sobreyectiva: $1$ no está en su imagen. El desplazamiento hacia atrás en $\mathbf F^\infty$ es sobreyectivo, pero no inyectivo: $(1,0,0,\ldots)$ está en su espacio nulo. Ninguna de estas aplicaciones es invertible.

### 3.65 Inyectividad equivale a sobreyectividad en igual dimensión finita

Sean $V,W$ de dimensión finita, con $\dim V=\dim W$, y $T\in\mathcal L(V,W)$. Entonces

$$\boxed{T\text{ invertible}\iff T\text{ inyectiva}\iff T\text{ sobreyectiva}.}$$

**Demostración.** Por 3.21,

$$\tag{3.66}\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T.$$

Si $T$ es inyectiva, el espacio nulo tiene dimensión cero; la imagen tiene, por tanto, la dimensión de $W$ y es todo $W$ (2.39). Si $T$ es sobreyectiva, la igualdad anterior obliga a que el espacio nulo tenga dimensión cero, por lo que $T$ es inyectiva. Concluimos por 3.63.

### 3.67 Ejemplo: existencia de soluciones polinómicas

Dado $q\in\mathcal P(\mathbf R)$, existe $p\in\mathcal P(\mathbf R)$ tal que

$$\big((x^2+5x+7)p\big)''=q.$$

Elegimos $m$ con $q\in\mathcal P_m(\mathbf R)$ y consideramos $T:\mathcal P_m(\mathbf R)\to\mathcal P_m(\mathbf R)$, $Tp=((x^2+5x+7)p)''$. El grado de un polinomio no nulo aumenta dos unidades al multiplicar por el cuadrático y disminuye dos al derivar dos veces, de modo que $T$ está bien definida. Si $Tp=0$, el producto cuadrático por $p$ es de grado a lo sumo uno, lo cual obliga a $p=0$. Por 3.65, $T$ es sobreyectiva y tiene una preimagen de $q$. La restricción a dimensión finita es esencial; no se aplica 3.65 directamente a $\mathcal P(\mathbf R)$.

### 3.68 $ST=I\iff TS=I$ para espacios de igual dimensión

Sean $V,W$ espacios de dimensión finita e igual, $S\in\mathcal L(W,V)$ y $T\in\mathcal L(V,W)$. Entonces

$$ST=I_V\iff TS=I_W.$$

**Demostración.** Si $ST=I_V$, la igualdad $Tv=0$ implica $v=STv=0$, luego $T$ es inyectiva. Por 3.65 es invertible. Multiplicando $ST=I_V$ por $T^{-1}$ a la derecha obtenemos $S=T^{-1}$ y por tanto $TS=I_W$. La implicación inversa se obtiene intercambiando los papeles de $V,W$ y de $S,T$.

> `[ERRATA · fuente]` El enunciado de la edición impresa intercambiaba los nombres $V$ y $W$ en su última línea. Se emplea aquí la versión corregida del PDF oficial (29-12-2023). No es una corrección conjetural de la traducción.

## Espacios vectoriales isomorfos

### 3.69 Definición: isomorfismo, isomorfos

Un **isomorfismo** es una aplicación lineal invertible. Dos espacios vectoriales son **isomorfos** si existe un isomorfismo entre ellos. La correspondencia $v\mapsto Tv$ permite entender sus elementos como reetiquetados, conservando las propiedades de espacio vectorial. «Isomorfismo» enfatiza esa identidad estructural.

### 3.70 La dimensión caracteriza el isomorfismo en dimensión finita

Dos espacios vectoriales de dimensión finita sobre $\mathbf F$ son isomorfos si y solo si tienen la misma dimensión.

**Demostración.** Un isomorfismo $T:V\to W$ tiene espacio nulo cero e imagen $W$; por 3.21, $\dim V=\dim W$. Recíprocamente, dadas bases $v_1,\ldots,v_n$ de $V$ y $w_1,\ldots,w_n$ de $W$, la aplicación

$$T\left(\sum_{j=1}^n c_jv_j\right)=\sum_{j=1}^n c_jw_j$$

es lineal y biyectiva, pues lleva una base a una base. Por 3.63 es un isomorfismo.

Así, cada espacio de dimensión finita $n$ es isomorfo a $\mathbf F^n$; en particular, $\mathcal P_m(\mathbf F)\cong\mathbf F^{m+1}$. Identificar estructuras mediante un isomorfismo no equivale a afirmar que sus conjuntos son literalmente iguales. Elegir coordenadas puede añadir complejidad cuando la estructura abstracta es más natural.

### 3.71 $\mathcal L(V,W)$ y $\mathbf F^{m,n}$ son isomorfos

Si $v_1,\ldots,v_n$ es una base de $V$ y $w_1,\ldots,w_m$ una base de $W$, la aplicación

$$\mathcal M:\mathcal L(V,W)\longrightarrow\mathbf F^{m,n},\qquad T\longmapsto\mathcal M(T)$$

es un isomorfismo.

**Demostración.** Es lineal por 3.35 y 3.38. Si $\mathcal M(T)=0$, todas las imágenes $Tv_k$ son cero y el lema 3.4 implica $T=0$: es inyectiva. Dada una matriz $A$, prescribimos sobre la base $Tv_k=\sum_{j=1}^m A_{j,k}w_j$; el lema 3.4 produce una aplicación lineal cuya matriz es $A$: es sobreyectiva.

### 3.72 Dimensión del espacio de aplicaciones lineales

Si $V,W$ son de dimensión finita,

$$\boxed{\dim\mathcal L(V,W)=(\dim V)(\dim W).}$$

**Demostración.** Combinar 3.71, 3.70 y 3.40.

## Aplicaciones lineales entendidas como multiplicación matricial

### 3.73 Definición: matriz de un vector, $\mathcal M(v)$

Para $v\in V$ y una base $v_1,\ldots,v_n$, escribimos de manera única $v=b_1v_1+\cdots+b_nv_n$. La matriz de $v$ respecto de esa base es la columna

$$\mathcal M(v)=\begin{pmatrix}b_1\\\vdots\\b_n\end{pmatrix}\in\mathbf F^{n,1}.$$

Depende de la base, aunque se omita esta de la notación cuando el contexto sea inequívoco.

### 3.74 Ejemplos: matriz de un vector

Respecto de la base estándar de $\mathcal P_4(\mathbf R)$,

$$\mathcal M(2-7x+5x^3+x^4)=\begin{pmatrix}2\\-7\\0\\5\\1\end{pmatrix}.$$

Respecto de la base estándar de $\mathbf F^n$, la matriz de $(x_1,\ldots,x_n)$ es la columna cuyas entradas son $x_1,\ldots,x_n$. Fijar una base hace que $v\mapsto\mathcal M(v)$ sea un isomorfismo $V\to\mathbf F^{n,1}$.

### 3.75 Columna $k$ de $\mathcal M(T)$

Para $T\in\mathcal L(V,W)$ y bases $v_1,\ldots,v_n$ y $w_1,\ldots,w_m$,

$$\mathcal M(T)_{\cdot,k}=\mathcal M(Tv_k),\quad 1\le k\le n,$$

con las coordenadas del lado derecho tomadas en la base de $W$. Se sigue directamente de 3.31 y 3.73.

### 3.76 Las aplicaciones lineales actúan como multiplicaciones de matrices

Bajo las mismas hipótesis y para cada $v\in V$,

$$\boxed{\mathcal M(Tv)=\mathcal M(T)\mathcal M(v).}$$

**Demostración.** Si $v=\sum_{k=1}^n b_kv_k$, entonces

$$\tag{3.77}Tv=\sum_{k=1}^n b_kTv_k.$$

Tomando coordenadas y usando 3.75 y 3.50,

$$\mathcal M(Tv)=\sum_{k=1}^n b_k\mathcal M(Tv_k)
=\sum_{k=1}^n b_k\mathcal M(T)_{\cdot,k}
=\mathcal M(T)\mathcal M(v).$$

Cada matriz $A\in\mathbf F^{m,n}$ define, a su vez, una aplicación lineal $x\mapsto Ax$ entre espacios de columnas. Toda aplicación entre espacios de dimensión finita puede representarse así después de elegir bases, aunque la matriz particular depende de esas elecciones.

### 3.78 La dimensión de la imagen es el rango columna de la matriz

Si $V,W$ son de dimensión finita y $T\in\mathcal L(V,W)$, entonces

$$\boxed{\dim\operatorname{range}T=\operatorname{rank}\mathcal M(T).}$$

**Demostración.** La aplicación de coordenadas en $W$ restringida a $\operatorname{range}T$ es un isomorfismo hacia el subespacio generado por $\mathcal M(Tv_1),\ldots,\mathcal M(Tv_n)$, que por 3.75 son justamente las columnas de $\mathcal M(T)$. Las dimensiones coinciden por 3.70. El rango columna coincide con el rango por 3.57–3.58.

## Cambio de base

Para un operador $T\in\mathcal L(V)$ suele emplearse la misma base en el dominio y en el espacio de llegada; abreviamos $\mathcal M(T,(v_1,\ldots,v_n))$ cuando ambas bases coinciden.

### 3.79 Definición: matriz identidad $I$

Para $n\ge1$, la matriz identidad $I$ de tamaño $n\times n$ tiene unos en la diagonal y ceros fuera de ella:

$$I_{j,k}=\begin{cases}1&j=k,\\0&j\ne k.\end{cases}$$

Respecto de cualquier base, la matriz del operador identidad es la matriz identidad: $\mathcal M(I)=I$. El símbolo denota objetos distintos a ambos lados, según el contexto. Para cada matriz cuadrada $A$ de tamaño $n$, $AI=IA=A$.

### 3.80 Definición: matriz invertible e inversa $A^{-1}$

Una matriz cuadrada $A$ es invertible si existe una matriz $B$ del mismo tamaño con $AB=BA=I$. Tal $B$ es única, se llama inversa y se denota $A^{-1}$. También se emplean «no singular» y «singular» para invertible y no invertible. Las identidades algebraicas de los inversos incluyen

$$(A^{-1})^{-1}=A,\qquad (AC)^{-1}=C^{-1}A^{-1}$$

cuando $A,C$ son invertibles y del mismo tamaño: se comprueba multiplicando a ambos lados, con el orden indicado.

### 3.81 Matriz del producto de aplicaciones lineales

Para $T\in\mathcal L(U,V)$, $S\in\mathcal L(V,W)$, una base $u_1,\ldots,u_m$ de $U$, una base $v_1,\ldots,v_n$ de $V$ y una base $w_1,\ldots,w_p$ de $W$,

$$\mathcal M(ST,(u_j),(w_j))=\mathcal M(S,(v_j),(w_j))\,\mathcal M(T,(u_j),(v_j)).$$

Esta es la formulación con bases explícitas de 3.43. No es lícito cambiar arbitrariamente la base intermedia de una de las matrices.

### 3.82 La matriz de la identidad entre dos bases

Si $\mathcal U=(u_1,\ldots,u_n)$ y $\mathcal V=(v_1,\ldots,v_n)$ son bases de $V$, las matrices $\mathcal M(I,\mathcal U,\mathcal V)$ y $\mathcal M(I,\mathcal V,\mathcal U)$ son inversas. En efecto, las dos aplicaciones de 3.81 a $I\circ I=I$ dan en ambos órdenes el producto identidad.

### 3.83 Ejemplo: dos bases de $\mathbf F^2$

Para $\mathcal U=((4,2),(5,3))$ y la base estándar $\mathcal E=((1,0),(0,1))$,

$$C=\mathcal M(I,\mathcal U,\mathcal E)=\begin{pmatrix}4&5\\2&3\end{pmatrix},\qquad C^{-1}=\begin{pmatrix}\frac32&-\frac52\\-1&2\end{pmatrix}.$$

Así, $\mathcal M(I,\mathcal E,\mathcal U)=C^{-1}$.

### 3.84 Fórmula de cambio de base

Sean $T\in\mathcal L(V)$ y dos bases $\mathcal U=(u_1,\ldots,u_n)$ y $\mathcal V=(v_1,\ldots,v_n)$. Definamos

$$A=\mathcal M(T,\mathcal U),\quad B=\mathcal M(T,\mathcal V),\quad C=\mathcal M(I,\mathcal U,\mathcal V).$$

Entonces

$$\boxed{A=C^{-1}BC.}$$

**Demostración.** Por 3.81, la matriz de $T$ entre la base $\mathcal U$ de entrada y $\mathcal V$ de salida es $BC$. La conversión de coordenadas de salida desde $\mathcal V$ a $\mathcal U$ es $C^{-1}$, de modo que

$$\tag{3.85}A=C^{-1}\mathcal M(T,\mathcal U,\mathcal V)=C^{-1}BC.$$

### 3.86 Matriz de la inversa

Si $v_1,\ldots,v_n$ es una base de $V$ y $T\in\mathcal L(V)$ es invertible, entonces

$$\boxed{\mathcal M(T^{-1})=(\mathcal M(T))^{-1}.}$$

La demostración se solicita en los ejercicios y se incorpora separadamente como `[SOL]`.

## Ejercicios 3D · Registro fiel de objetivos

1. Invertibilidad de $T^{-1}$ y doble inversa.  
2. Inversa de la composición de dos aplicaciones invertibles.  
3. Equivalencia entre invertibilidad y transformación de alguna/toda base en base.  
4. Mostrar que las aplicaciones no invertibles de $\mathcal L(V)$ no forman subespacio si $\dim V>1$.  
5. Criterio para extender $S:U\to V$ a un automorfismo de $V$.  
6. Igualdad de espacios nulos y equivalencia por automorfismo del codominio.  
7. Igualdad de imágenes y equivalencia por automorfismo del dominio.  
8. Clasificación por dimensión del espacio nulo bajo automorfismos a ambos lados.  
9. Restricción isomorfa de una aplicación sobreyectiva.  
10. Subespacio de aplicaciones que anulan $U$ y cálculo de su dimensión.  
11. Invertibilidad de un producto de operadores en dimensión finita.  
12. De $STU=I$ deducir la inversa de $T$.  
13. Contraejemplo a la conclusión anterior en dimensión infinita.  
14. Relación entre la sobreyectividad de $RST$ y la inyectividad de $S$.  
15. Una lista cuyas imágenes generan $V$ genera también $V$.  
16. Toda aplicación entre espacios de columnas es multiplicación por una matriz.  
17. Dimensiones del espacio nulo y la imagen de la multiplicación izquierda $\mathcal A(T)=ST$.  
18. Isomorfismo $V\cong\mathcal L(\mathbf F,V)$.  
19. Caracterización de los operadores con la misma matriz en cualquier base.  
20. Existencia de solución polinómica para $q=(x^2+x)p''+2xp'+p(3)$.  
21. Equivalencia entre unicidad de solución homogénea y existencia de solución para todo término independiente en sistemas cuadrados.  
22. Invertibilidad de $T$ si y solo si invertibilidad de su matriz en una base.  
23. Identidad entre matrices de $T$ y del operador identidad respecto de las bases indicadas.  
24. Para matrices cuadradas, $AB=I\Rightarrow BA=I$.

Los enunciados íntegros se consultan en la fuente oficial, pp. 93–95; las soluciones originales se publican en `soluciones/03-capitulo-3/3d.md`. No se altera la numeración ni se atribuyen esas soluciones a Axler.
