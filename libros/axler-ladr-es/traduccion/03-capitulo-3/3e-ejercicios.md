# Ejercicios 3E · Productos y cocientes de espacios vectoriales

**Estado:** `TRAD / PRIMERA PASADA COTEJADA; QA FINAL PENDIENTE` · **Fuente:** Axler, 4.ª ed., PDF oficial 16-08-2026, pp. 103–104. Traducción no oficial CC BY-NC 4.0. **19 ejercicios**; conservar la numeración del autor. Las soluciones propias aparecen en [`3e.md`](../../soluciones/03-capitulo-3/3e.md).

**1.** Sea $T:V\to W$ una función. Su **gráfica** es $G(T)=\{(v,Tv):v\in V\}\subseteq V\times W$. Demuestra que $T$ es lineal si y solo si su gráfica es un subespacio de $V\times W$. [El original añade que, desde un punto de vista conjuntista formal, una función puede identificarse con su gráfica: un subconjunto de $V\times W$ que contiene exactamente un par con primera componente $v$ para cada $v\in V$.]

**2.** Supón que $V_1\times\cdots\times V_m$ tiene dimensión finita. Demuestra que cada $V_k$ tiene dimensión finita.

**3.** Demuestra que $\mathcal L(V_1\times\cdots\times V_m,W)$ es isomorfo a $\mathcal L(V_1,W)\times\cdots\times\mathcal L(V_m,W)$. **No se supone dimensión finita** (tampoco en los ejercicios 4 y 5).

**4.** Demuestra que $\mathcal L(V,W_1\times\cdots\times W_m)$ es isomorfo a $\mathcal L(V,W_1)\times\cdots\times\mathcal L(V,W_m)$.

**5.** Para $m\ge1$ define $V^m=V\times\cdots\times V$ ($m$ factores). Demuestra que $V^m$ y $\mathcal L(\mathbf F^m,V)$ son isomorfos.

**6.** Sean $v,x\in V$ y $U,W$ subespacios de $V$. Si $v+U=x+W$, demuestra que $U=W$.

**7.** Sea $U=\{(x,y,z)\in\mathbf R^3:2x+3y+5z=0\}$ y $A\subseteq\mathbf R^3$. Demuestra que $A$ es un trasladado de $U$ si y solo si, para algún $c\in\mathbf R$, $A=\{(x,y,z)\in\mathbf R^3:2x+3y+5z=c\}$.

**8.** (a) Para $T\in\mathcal L(V,W)$ y $c\in W$, prueba que $\{x\in V:Tx=c\}$ es vacío o es un trasladado de $\operatorname{null}T$. (b) Explica por qué las soluciones de un sistema de ecuaciones lineales como 3.27 son vacías o forman un trasladado de un subespacio de $\mathbf F^n$.

**9.** Demuestra que $A\subseteq V$ no vacío es un trasladado de algún subespacio de $V$ si y solo si $\lambda v+(1-\lambda)w\in A$ para cualesquiera $v,w\in A$ y $\lambda\in\mathbf F$.

**10.** Si $A_1=v+U_1$ y $A_2=w+U_2$, con $U_1,U_2\le V$ y $v,w\in V$, demuestra que $A_1\cap A_2$ es vacío o es un trasladado de algún subespacio de $V$.

**11.** Sea $U=\{(x_1,x_2,\ldots)\in\mathbf F^\infty:x_k\ne0\text{ solo para un número finito de }k\}$. (a) Demuestra que $U$ es un subespacio de $\mathbf F^\infty$. (b) Demuestra que $\mathbf F^\infty/U$ tiene dimensión infinita.

**12.** Sean $v_1,\ldots,v_m\in V$ y $A=\{\lambda_1v_1+\cdots+\lambda_mv_m:\lambda_k\in\mathbf F,\;\lambda_1+\cdots+\lambda_m=1\}$. (a) Demuestra que $A$ es un trasladado de un subespacio. (b) Si $B$ es un trasladado de un subespacio y contiene $\{v_1,\ldots,v_m\}$, demuestra que $A\subseteq B$. (c) Demuestra que $A$ es un trasladado de un subespacio de dimensión menor que $m$.

**13.** Si $U\le V$ y $V/U$ tiene dimensión finita, demuestra que $V$ es isomorfo a $U\times(V/U)$.

**14.** Si $V=U\oplus W$ y $w_1,\ldots,w_m$ es una base de $W$, demuestra que $w_1+U,\ldots,w_m+U$ es una base de $V/U$.

**15.** Si $v_1+U,\ldots,v_m+U$ es una base de $V/U$ y $u_1,\ldots,u_n$ es una base de $U$, demuestra que $v_1,\ldots,v_m,u_1,\ldots,u_n$ es una base de $V$.

**16.** Si $\varphi\in\mathcal L(V,\mathbf F)$ y $\varphi\ne0$, demuestra que $\dim(V/\operatorname{null}\varphi)=1$.

**17.** Si $U\le V$ y $\dim(V/U)=1$, demuestra que existe $\varphi\in\mathcal L(V,\mathbf F)$ tal que $\operatorname{null}\varphi=U$.

**18.** Supón que $U\le V$ y $V/U$ tiene dimensión finita. (a) Si $W\le V$ es de dimensión finita y $V=U+W$, demuestra que $\dim W\ge\dim(V/U)$. (b) Demuestra que existe $W\le V$ de dimensión finita con $\dim W=\dim(V/U)$ y $V=U\oplus W$.

**19.** Sea $T\in\mathcal L(V,W)$, $U\le V$ y $\pi:V\to V/U$ la aplicación cociente. Demuestra que existe $S\in\mathcal L(V/U,W)$ con $T=S\circ\pi$ si y solo si $U\subseteq\operatorname{null}T$.

**Control editorial:** en los ejercicios 3–5 y 13–19 no introducir hipótesis de dimensión finita adicionales a las que figuran expresamente en cada enunciado.