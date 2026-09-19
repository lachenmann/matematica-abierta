## 14.12. Criterio de la raíz y límite superior finito {#sec-ta-14-12}

Los criterios precedentes se formularon primero mediante un **límite ordinario** de las raíces o, sin presuponer ese límite, mediante cotas que valen a partir de cierto índice. Hay sucesiones de raíces que oscilan y no tienen límite ordinario; para ellas, la frontera superior asintótica puede contener información decisiva. El Capítulo 13 ya construyó esa frontera mediante los supremos de las colas, **pero únicamente para sucesiones acotadas**. Mantendremos exactamente esa condición de dominio.

### Teorema 14.12.1 — Criterio de la raíz mediante límite superior finito

Sea $a\in\mathbb R^{\mathbb N}$ y sea $r=R(a)$ la sucesión de raíces de Definición 14.9.4 — Sucesión de raíces asociada a una serie: $r_0=0$ y, para cada natural $n\ge1$,

$$
r_n=\sqrt[n]{|a_n|},\qquad r_n^{\,n}=|a_n|.
$$

**Supongamos que $r$ es una sucesión real acotada.** En virtud de Definición 13.12.2 — Límite inferior y límite superior existe el número real finito

$$
\boxed{L:=\limsup_{n\to\infty}r_n
=\lim_{N\to\infty}U_N(r)
=\inf\{U_N(r):N\in\mathbb N\}.}
\tag{14.12.1}
$$

Entonces $L\ge0$ y se cumplen estas afirmaciones:

1. Si $L<1$, la serie $\sum_{n=0}^{\infty}a_n$ **converge absolutamente**.
2. Si $L>1$, la serie $\sum_{n=0}^{\infty}a_n$ **diverge**, porque $a_n$ no tiende a cero.
3. Si $L=1$, no se sigue ninguna de las dos conclusiones: existen series con raíces acotadas y límite superior igual a uno que, respectivamente, convergen y divergen.

**Demostración.**

La hipótesis de acotación legitima todas las envolventes $U_N(r)=\sup T_N(r)$, y Teorema 13.12.1 — Convergencia de las envolventes de colas demuestra que convergen al número $L$ de (14.12.1). Como $r_n\ge0$ para todo $n$, sus colas tienen a cero como cota inferior; por consiguiente $U_N(r)\ge0$. La preservación del orden bajo límites (Teorema 13.6.2 — Preservación del orden en el paso al límite) da $L\ge0$.

**Caso $L<1$.** Definamos $q:=(1+L)/2$. De $0\le L<1$ obtenemos $0<q<1$ y $L<q$. La convergencia $U_N(r)\to L$ implica que existe un índice natural $N_0$ tal que

$$
U_N(r)<q\qquad(N\ge N_0).
$$

Tomemos $N\ge\max\{N_0,1\}$. Como $r_n\in T_N(r)$ para todo $n\ge N$, la definición del supremo asegura

$$
0\le r_n\le U_N(r)<q
\qquad(n\ge N).
\tag{14.12.2}
$$

Ésta es precisamente la cota eventual estrictamente subunitaria que autoriza la versión sin límite de Teorema 14.9.6 — Criterio de la raíz. Por tanto $\sum |a_n|$ converge y la serie original converge absolutamente. En particular, no ha sido necesario que $r_n$ tenga límite ordinario.

**Caso $L>1$.** Fijemos $c:=(1+L)/2$, de modo que $1<c<L$. Para todo $N\ge1$, la identidad $L=\inf\{U_M(r):M\in\mathbb N\}$ garantiza

$$
U_N(r)\ge L>c.
$$

Por la propiedad característica del supremo, existe un término de la cola $T_N(r)$ estrictamente mayor que $c$: de lo contrario, $c$ sería cota superior de esa cola y $U_N(r)\le c$, contradicción. Así,

$$
\forall N\ge1\quad\exists n\ge N:\quad r_n>c>1.
\tag{14.12.3}
$$

Para cada uno de estos índices, la identidad definitoria de la raíz y la monotonía de las potencias positivas de Lema 14.9.1 — Monotonía de las potencias positivas y cota de variación finita proporcionan

$$
|a_n|=r_n^{\,n}>c^n\ge1.
$$

La desigualdad $c^n\ge1$ se prueba por inducción a partir de $c>1$ y $c^0=1$. Si $a_n\to0$, la definición de límite con tolerancia $1$ obligaría a $|a_n|<1$ para todos los índices suficientemente grandes, contradiciendo (14.12.3). Luego $a_n\not\to0$, y el criterio de divergencia por el término general Corolario 14.2.5 — Criterio de divergencia por el término general concluye que la serie diverge. El razonamiento prueba directamente una afirmación con cuantificadores $\forall N\,\exists n$; **no se construye una sucesión de índices elegidos** ni se utiliza Choice.

**Caso $L=1$.** Proposición 14.9.9 — La frontera de ambos criterios es indecisiva construyó dos sucesiones positivas, la armónica $h$ y la telescópica $b$, cuyas respectivas series divergen y convergen, mientras sus sucesiones de raíces tienen ambas límite ordinario igual a $1$. Toda sucesión convergente de números reales es acotada (resultado del Capítulo 13), por lo que las raíces de ambos ejemplos cumplen la presente hipótesis. Para una sucesión convergente a $1$, los supremos de sus colas también convergen a $1$: dado $\varepsilon>0$, todos los términos de una cola están entre $1-\varepsilon$ y $1+\varepsilon$, luego también lo está su supremo. Así su límite superior vale $1$. Los dos ejemplos satisfacen, pues, exactamente la frontera de este teorema y tienen comportamientos opuestos. ∎

> **Lectura de los cuantificadores.** La desigualdad $\limsup r_n<1$ proporciona **una única cota $q<1$ válida eventualmente para todos los índices**. En cambio, $\limsup r_n>1$ obliga a encontrar raíces mayores que una constante $c>1$ **arbitrariamente tarde**, aunque otras raíces puedan ser pequeñas. En ambos casos la información basta; cuando el límite superior es uno, no basta.
>
> **Alcance fundacional.** Este resultado no atribuye un valor $+\infty$ a $\limsup r_n$ si $r$ no está acotada. Para sucesiones no acotadas siguen vigentes las versiones de cotas eventuales del criterio de §14.9; no extendemos aquí el dominio de Definición 13.12.2 — Límite inferior y límite superior. Los supremos de las colas son únicos: no se realiza una elección de valores, y tampoco se obtiene un procedimiento efectivo general para decidir la convergencia.

---

La teoría de series ha mostrado que el comportamiento de una sucesión de sumas depende de las cotas de sus términos, de la estructura de las colas y, en el caso de las series condicionales, también de su orden. El capítulo siguiente trasladará estas herramientas de límite y orden al estudio de los **conjuntos de puntos de la recta real**: comenzaremos por precisar, mediante el valor absoluto, qué significa que un punto esté cerca de otro.
