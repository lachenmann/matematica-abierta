# Ejercicios de 3D · Invertibilidad e isomorfismos

**Estado:** `BORRADOR COTEJADO` · **Procedencia:** `[TRAD]`, Axler 4.ª edición, PDF oficial 16-08-2026, pp. 93–95. Traducción no oficial CC BY-NC 4.0. La numeración y las hipótesis se conservan; soluciones originales en [`3d.md`](../../soluciones/03-capitulo-3/3d.md).

**1.** Supongamos que $T\in\mathcal L(V,W)$ es invertible. Demuestra que $T^{-1}$ es invertible y que $(T^{-1})^{-1}=T$.

**2.** Supongamos que $T\in\mathcal L(U,V)$ y $S\in\mathcal L(V,W)$ son invertibles. Demuestra que $ST\in\mathcal L(U,W)$ es invertible y que $(ST)^{-1}=T^{-1}S^{-1}$.

**3.** Supongamos que $V$ tiene dimensión finita y $T\in\mathcal L(V)$. Demuestra la equivalencia de: (a) $T$ es invertible; (b) $Tv_1,\ldots,Tv_n$ es una base de $V$ para **toda** base $v_1,\ldots,v_n$ de $V$; (c) $Tv_1,\ldots,Tv_n$ es una base de $V$ para **alguna** base $v_1,\ldots,v_n$ de $V$.

**4.** Sean $V$ de dimensión finita y $\dim V>1$. Demuestra que el conjunto de aplicaciones lineales no invertibles de $V$ en sí mismo no es un subespacio de $\mathcal L(V)$.

**5.** Sean $V$ de dimensión finita, $U$ un subespacio de $V$ y $S\in\mathcal L(U,V)$. Demuestra que existe una aplicación lineal invertible $T:V\to V$ con $Tu=Su$ para cada $u\in U$ si y solo si $S$ es inyectiva.

**6.** Sean $W$ de dimensión finita y $S,T\in\mathcal L(V,W)$. Demuestra que $\operatorname{null}S=\operatorname{null}T$ si y solo si existe un operador invertible $E\in\mathcal L(W)$ tal que $S=ET$.

**7.** Sean $V$ de dimensión finita y $S,T\in\mathcal L(V,W)$. Demuestra que $\operatorname{range}S=\operatorname{range}T$ si y solo si existe un operador invertible $E\in\mathcal L(V)$ tal que $S=TE$.

**8.** Sean $V,W$ de dimensión finita y $S,T\in\mathcal L(V,W)$. Demuestra que existen operadores invertibles $E_1\in\mathcal L(V)$ y $E_2\in\mathcal L(W)$ tales que $S=E_2TE_1$ si y solo si $\dim\operatorname{null}S=\dim\operatorname{null}T$.

**9.** Supongamos que $V$ tiene dimensión finita y que $T:V\to W$ es lineal y sobreyectiva. Demuestra que existe un subespacio $U$ de $V$ tal que la restricción $T|_U:U\to W$ es un isomorfismo. Aquí $T|_U(u)=Tu$ para todo $u\in U$.

**10.** Sean $V,W$ de dimensión finita y $U\subseteq V$ un subespacio. Sea

$$\mathcal E=\{T\in\mathcal L(V,W):U\subseteq\operatorname{null}T\}.$$

(a) Demuestra que $\mathcal E$ es un subespacio de $\mathcal L(V,W)$. (b) Obtén una fórmula para $\dim\mathcal E$ en función de $\dim V$, $\dim W$ y $\dim U$. **Pista del autor:** define $\Phi:\mathcal L(V,W)\to\mathcal L(U,W)$ por $\Phi(T)=T|_U$; determina su espacio nulo y su imagen.

**11.** Sean $V$ de dimensión finita y $S,T\in\mathcal L(V)$. Demuestra que $ST$ es invertible si y solo si tanto $S$ como $T$ son invertibles.

**12.** Sean $V$ de dimensión finita, $S,T,U\in\mathcal L(V)$ y $STU=I$. Demuestra que $T$ es invertible y que $T^{-1}=US$.

**13.** Demuestra que el resultado del ejercicio 12 puede fallar si se suprime la hipótesis de dimensión finita de $V$.

**14.** Demuestra o proporciona un contraejemplo: si $V$ es de dimensión finita y $R,S,T\in\mathcal L(V)$ satisfacen que $RST$ es sobreyectiva, entonces $S$ es inyectiva.

**15.** Sean $T\in\mathcal L(V)$ y $v_1,\ldots,v_m$ una lista de $V$ tal que $Tv_1,\ldots,Tv_m$ genera $V$. Demuestra que $v_1,\ldots,v_m$ genera $V$.

**16.** Demuestra que toda aplicación lineal $T:\mathbf F^{n,1}\to\mathbf F^{m,1}$ se obtiene mediante multiplicación por una matriz: existe $A\in\mathbf F^{m,n}$ tal que $Tx=Ax$ para todo $x\in\mathbf F^{n,1}$.

**17.** Sean $V$ de dimensión finita, $S\in\mathcal L(V)$ y $\mathcal A\in\mathcal L(\mathcal L(V))$ definida por $\mathcal A(T)=ST$. Demuestra: (a) $\dim\operatorname{null}\mathcal A=(\dim V)(\dim\operatorname{null}S)$; (b) $\dim\operatorname{range}\mathcal A=(\dim V)(\dim\operatorname{range}S)$.

**18.** Demuestra que $V$ y $\mathcal L(\mathbf F,V)$ son espacios vectoriales isomorfos.

**19.** Sean $V$ de dimensión finita y $T\in\mathcal L(V)$. Demuestra que $T$ tiene la misma matriz respecto de toda base de $V$ si y solo si es un múltiplo escalar del operador identidad.

**20.** Sea $q\in\mathcal P(\mathbf R)$. Demuestra que existe $p\in\mathcal P(\mathbf R)$ tal que, para todo $x\in\mathbf R$,

$$q(x)=(x^2+x)p''(x)+2xp'(x)+p(3).$$

**21.** Sea $n$ un entero positivo y sean $A_{j,k}\in\mathbf F$ para $j,k=1,\ldots,n$. Demuestra la equivalencia de: (a) el sistema homogéneo $\sum_{k=1}^n A_{j,k}x_k=0$ para $j=1,\ldots,n$ tiene únicamente la solución trivial $x_1=\cdots=x_n=0$; (b) para cada elección de $c_1,\ldots,c_n\in\mathbf F$, el sistema $\sum_{k=1}^n A_{j,k}x_k=c_j$ para $j=1,\ldots,n$ posee una solución. En ambos casos, el número de ecuaciones coincide con el de incógnitas.

**22.** Sean $T\in\mathcal L(V)$ y $v_1,\ldots,v_n$ una base de $V$. Demuestra que $\mathcal M(T,(v_1,\ldots,v_n))$ es invertible si y solo si $T$ es invertible.

**23.** Sean $u_1,\ldots,u_n$ y $v_1,\ldots,v_n$ bases de $V$, y $T\in\mathcal L(V)$ tal que $Tv_k=u_k$ para $k=1,\ldots,n$. Demuestra que

$$\mathcal M(T,(v_1,\ldots,v_n))=\mathcal M(I,(u_1,\ldots,u_n),(v_1,\ldots,v_n)).$$

**24.** Sean $A$ y $B$ matrices cuadradas del mismo tamaño con $AB=I$. Demuestra que $BA=I$.

---

**Nota editorial:** la notación $\operatorname{null}$ y $\operatorname{range}$ se conserva para cotejo con Axler; en prosa, «espacio nulo» e «imagen». El ejercicio 20 contiene la evaluación $p(3)$, no una derivada. La convención para matrices $0\times0$ en los ejercicios sobre bases vacías requiere una decisión editorial explícita, porque 3.79 define la matriz identidad para $n\ge1$.
