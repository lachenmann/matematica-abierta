---
content-id: MA-BCH-0296
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-023-SOLUCIONES
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: Soluciones — Capítulo 23
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C23_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)

## 23.1. Cotas sin extremos alcanzados

[]{#MA-EX-ANM-01-023-001}

[]{#MA-SOL-ANM-01-023-001}

[]{#MA-SEC-ANM-01-023-001}

Todo valor es estrictamente entre0 y1. Para cualquier η>0 hay entrada interior menor que min(η,1/2), y otra a distancia menor que min(η,1/2) de1: sus valores se aproximan a0 y1. Así ninguna cota inferior positiva o superior menor que1 sirve. Ningún valor es0 o1, por la definición nodal.

**Retorno visual.** Véase [C23-F01](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.2. Restringir disminuye oscilación

[]{#MA-EX-ANM-01-023-002}

[]{#MA-SOL-ANM-01-023-002}

La imagen f[J] está contenida en f[K]. Toda cota inferior de la grande también acota la pequeña, luego m(K)≤m(J); toda cota superior de la grande acota la pequeña, luego M(J)≤M(K). No vaciedad da m(J)≤M(J). Restar los extremos da ω(J)≤ω(K).

## 23.3. Cuadrado en una pieza

[]{#MA-EX-ANM-01-023-003}

[]{#MA-SOL-ANM-01-023-003}

Por orden del cuadrado en no negativos, m=1/16, M=9/16 y ω=1/2, alcanzados en los extremos. En un intervalo que cruza cero no bastan extremos como mínimo: por ejemplo en[−1,1] el mínimo0 está en0 y los dos extremos valen1.

## 23.4. De cotas a testigos

[]{#MA-EX-ANM-01-023-004}

[]{#MA-SOL-ANM-01-023-004}

Si todos los valores fueran≤M−η, éste sería una cota superior menor que el supremo, contradicción. Si todos fueran≥m+η, sería una cota inferior mayor que el ínfimo. Las negaciones dan los testigos; no se afirma que alcancen los extremos.

## 23.5. Dos muestras no controlan

[]{#MA-EX-ANM-01-023-005}

[]{#MA-SOL-ANM-01-023-005}

Sea f(1/2)=A>0 y f(x)=0 fuera. Las muestras de extremos son0, mientras m=0,M=A y ω=A. A es arbitrario, así que ninguna cota obtenida sólo de esas dos muestras controla la oscilación. La función sigue siendo acotada para cada A fijo.

## 23.6. Sumas del cuadrado

[]{#MA-EX-ANM-01-023-006}

[]{#MA-SOL-ANM-01-023-006}

[]{#MA-SEC-ANM-01-023-002}

Los ínfimos son0,1/16,1/4,9/16 y supremos1/16,1/4,9/16,1. Multiplicar por anchura1/4 y sumar da L=7/32,U=15/32,brecha1/4. Son cotas universales por monotonía, no meras etiquetas arbitrarias.

**Retorno visual.** Véase [C23-F02](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.7. Una inserción mejora

[]{#MA-EX-ANM-01-023-007}

[]{#MA-SOL-ANM-01-023-007}

Los hijos[u,t],[t,v] están dentro del padre: sus ínfimos≥m y supremos≤M. Multiplicar por t−u y v−t, sumar y usar que suman v−u compara los dos nuevos términos con el antiguo. Los otros términos quedan iguales. L no baja y U no sube.

## 23.8. Cruzar dos particiones

[]{#MA-EX-ANM-01-023-008}

[]{#MA-SOL-ANM-01-023-008}

Construir R con unión de nodos por C22. Monotonía da L(P)≤L(R) y U(R)≤U(Q); para R, L(R)≤U(R). La transitividad de las tres comparaciones da el resultado sin emparejar directamente piezas incompatibles.

## 23.9. Brecha cero fuerza constancia

[]{#MA-EX-ANM-01-023-009}

[]{#MA-SOL-ANM-01-023-009}

Cada ω_iΔ_i≥0 y su suma es0, por lo que cada producto es0. Δ_i>0 da ω_i=0. Todos los valores de una pieza son entonces su mismo ínfimo/supremo. Dos piezas vecinas comparten un nodo, que obliga igualdad de sus constantes; inducción finita las iguala todas.

## 23.10. Una suma no es una cota

[]{#MA-EX-ANM-01-023-010}

[]{#MA-SOL-ANM-01-023-010}

Monotonía compara L antigua con L nueva y U nueva con U antigua; no compara todas las S. En la trivial, L=0,U=1; en mitades, L=1/4,U=3/4, por lo que ambas mejoran. Las S particulares pueden ir a ambos lados de otra S.

## 23.11. Extremos de conjuntos de sumas

[]{#MA-EX-ANM-01-023-011}

[]{#MA-SOL-ANM-01-023-011}

[]{#MA-SEC-ANM-01-023-003}

Para f acotada sobre a<b, la partición trivial hace no vacías las imágenes de L y U, y cotas ±B(b−a) las acotan. Completitud proporciona supremo $\ell$ e ínfimo u. Cada U(Q) acota todas las L(P), de modo que $\ell$≤U(Q) para todo Q; por maximalidad del ínfimo, $\ell$≤u.

## 23.12. Una partición para dos aproximaciones

[]{#MA-EX-ANM-01-023-012}

[]{#MA-SOL-ANM-01-023-012}

Propiedad del supremo da P con L(P)>I−ε/2; propiedad del ínfimo da Q con U(Q)<I+ε/2. Refinamiento común R cumple L(R)≥L(P) y U(R)≤U(Q). Restar da G(R)<ε. Son dos testigos de una tolerancia fijada.

## 23.13. La recíproca del criterio

[]{#MA-EX-ANM-01-023-013}

[]{#MA-SOL-ANM-01-023-013}

Para toda P, 0≤u−$\ell$≤G(P). Si d=u−$\ell$>0, el criterio con ε=d/2 da P y d≤G(P)<d/2, contradicción. Por orden total y no negatividad, d=0.

## 23.14. Persistencia de precisión

[]{#MA-EX-ANM-01-023-014}

[]{#MA-SOL-ANM-01-023-014}

Si P tiene brecha<ε, monotonía da G(Q)≤G(P)<ε para cualquier refinamiento. En la vuelta tomar Q=P es legítimo por reflexividad y recupera el criterio original. La precisión se fija antes de Q.

## 23.15. Centro del intervalo certificado

[]{#MA-EX-ANM-01-023-015}

[]{#MA-SOL-ANM-01-023-015}

El medio es11/32; media anchura es(8/32)/2=1/8. Por encierro, el error≤1/8. El error real es11/32−1/3=(33−32)/96=1/96, positivo y menor que la cota. La cota no promete error exactamente igual a media anchura.

**Retorno visual.** Véase [C23-F03](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.16. Riemann también exige acotación

[]{#MA-EX-ANM-01-023-016}

[]{#MA-SOL-ANM-01-023-016}

[]{#MA-SEC-ANM-01-023-004}

Pedir error1 y fijar una uniforme de malla menor queδ con etiquetas medias. Para pieza i, mantener las demás fija y escribir S=f(t)Δ_i+C_i al variar t. |S|<|I|+1 y triangular dan |f(t)|≤(|I|+1+|C_i|)/Δ_i, con Δ_i>0. Máximo de las n cotas cubre todo[a,b], incluidas etiquetas de borde.

## 23.17. Etiquetas próximas a U

[]{#MA-EX-ANM-01-023-017}

[]{#MA-SOL-ANM-01-023-017}

En cada pieza hay altura f(ξ_i)>M_i−η/(b−a). Inducción finita construye la familia de n testigos. Multiplicar por Δ_i>0 y sumar da S>U−ηΣΔ_i/(b−a)=U−η. S≤U por encierro. Longitud positiva permite el denominador.

## 23.18. Un sentido del puente

[]{#MA-EX-ANM-01-023-018}

[]{#MA-SOL-ANM-01-023-018}

Elegir una uniforme de malla<radio para errorε/4. Etiquetas aproximantes con ηε/4 dan U<I_R+ε/2 y L>I_R−ε/2, luego G<ε. Criterio da I_D. El encierro entre L,U implica |I_D−I_R|<ε/2 para cada ε; distancia positiva daría contradicción al elegir ε menor, luego coinciden.

## 23.19. Cortes omitidos

[]{#MA-EX-ANM-01-023-019}

[]{#MA-SOL-ANM-01-023-019}

Refinar Q por P*. Una pieza sólo cambia si contiene un nodo de P* en su interior; los interiores disjuntos dan a lo sumo q piezas. En cada padre la superior baja≤2B·anchura y la inferior sube≤2B·anchura, porque los extremos y los de hijas están entre±B y las anchuras hijas suman la antigua. Sumar da≤4Bq·malla. G del refinamiento≤G(P*).

**Retorno visual.** Véase [C23-F04](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.20. Radio del puente y caso cero

[]{#MA-EX-ANM-01-023-020}

[]{#MA-SOL-ANM-01-023-020}

El término es24·malla, así δ=ε/48 da término<ε/2 cuando malla<δ. Brecha total<ε y el encierro prueba error<ε. Si Bq=0 el término es cero y basta cualquier radio positivo; no se usa la expresión con denominador nulo.

## 23.21. Monótona con salto

[]{#MA-EX-ANM-01-023-021}

[]{#MA-SOL-ANM-01-023-021}

[]{#MA-SEC-ANM-01-023-005}

Es no decreciente y valores extremos0,1. Los extremos de cada pieza son sus ínfimo/supremo; las diferencias son no negativas y telescopan a1, de modo que G≤malla. Uniformes de malla arbitrariamente pequeña satisfacen el criterio, aunque haya un salto.

**Retorno visual.** Véase [C23-F05](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.22. Lipschitz como certificado

[]{#MA-EX-ANM-01-023-022}

[]{#MA-SOL-ANM-01-023-022}

ω_i≤3Δ_i, por tomar extremos de diferencias universales. Entonces G≤3ΣΔ_i²≤3·malla·2=6malla. Malla<1/600 da brecha<1/100. Una muestra central de pendiente no establece Lipschitz universal.

## 23.23. Continua: de local a uniforme

[]{#MA-EX-ANM-01-023-023}

[]{#MA-SOL-ANM-01-023-023}

Se consideran todos los pares(c,r) válidos para errorη/2; sus bolas r/2 forman una cobertura. Compacidad heredada da un subcubrimiento finito. δ=min r_j/2>0. Si s está en una de esas bolas y |s−t|<δ, ambos distan<r_j del centro; triangular da diferencia<η. Sólo se usa la lista finita.

## 23.24. El margen al tomar supremos

[]{#MA-EX-ANM-01-023-024}

[]{#MA-SOL-ANM-01-023-024}

Para cada s,t, f(s)≤f(t)+η. Tomar supremo en s e ínfimo en t da M≤m+η; puede perderse la desigualdad estricta. Elegir η=ε/(2(b−a)) y malla menor que el radio uniforme da G≤ηΣΔ=ε/2<ε.

## 23.25. Un cerrado importa

[]{#MA-EX-ANM-01-023-025}

[]{#MA-SOL-ANM-01-023-025}

f(x)=1/x es continua en(0,1] y no acotada: dado M>0, tomar x positivo menor que min(1,1/(M+1)) da1/x>M. El dominio no es un cerrado compacto[a,b]; no se le aplica la prueba ni se le asigna aquí una integral impropia.

## 23.26. Signo de un múltiplo

[]{#MA-EX-ANM-01-023-026}

[]{#MA-SOL-ANM-01-023-026}

[]{#MA-SEC-ANM-01-023-006}

Para α>0, supremo e ínfimo escalan conservando orden. Para α<0, M(αf)=αm(f),m(αf)=αM(f); la diferencia es−αω(f)=|α|ω(f). Para α0 ambas cotas son0. Aproximar los extremos muestra igualdad aunque no se alcancen.

## 23.27. Producto integrable

[]{#MA-EX-ANM-01-023-027}

[]{#MA-SOL-ANM-01-023-027}

La identidad de diferencias da |f(s)g(s)−f(t)g(t)|≤Bfω(g,J)+Bgω(f,J); tomar extremos da la cota de oscilación. Pedir a ambas brechas<ε/(Bf+Bg+1), refinar común y sumar ponderadamente da G(fg)<ε; casos con constantes cero también quedan cubiertos.

## 23.28. Linealidad del valor

[]{#MA-EX-ANM-01-023-028}

[]{#MA-SOL-ANM-01-023-028}

Álgebra finita da S(αf+βg)=αSf+βSg. Para ε pedir a ambas errores<ε/(|α|+|β|+1), tomar el menor radio y triangular. El error combinado≤suma de coeficientes por ese error, menor que ε. Unicidad de Riemann y equivalencia identifican el valor.

## 23.29. Producto no multiplicativo

[]{#MA-EX-ANM-01-023-029}

[]{#MA-SOL-ANM-01-023-029}

I(fg)=I(x²)=1/3 por el certificado del cubo. IfIg=(1/2)²=1/4. Son distintos; cerrar la clase bajo producto no implica multiplicatividad de la aplicación integral.

**Retorno visual.** Véase [C23-F06](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.30. Valor absoluto y orden

[]{#MA-EX-ANM-01-023-030}

[]{#MA-SOL-ANM-01-023-030}

Triangular inversa da ω(|f|)≤ω(f), así |f| es integrable. Orden de funciones−|f|≤f≤|f| y linealidad dan−I|f|≤If≤I|f|. Para2x−1, C22 da If0; partir en1/2 y usar afines da I|f|=1/4+1/4=1/2, por lo que la desigualdad es estricta.

## 23.31. Restricción a dos lados

[]{#MA-EX-ANM-01-023-031}

[]{#MA-SOL-ANM-01-023-031}

[]{#MA-SEC-ANM-01-023-007}

Inserción conserva o mejora brecha. La nueva brecha es suma de las brechas de las listas izquierda y derecha, ambas no negativas. Una brecha total<ε fuerza cada una<ε, y como ε es arbitraria el criterio prueba las dos integrabilidades.

## 23.32. Pegar dos integrales

[]{#MA-EX-ANM-01-023-032}

[]{#MA-SOL-ANM-01-023-032}

Elegir particiones de cada lado de brecha<ε/2. Concatenar sin repetir c en la lista de nodos. Sus piezas y extremos locales son las mismas y la brecha total es su suma<ε. El criterio da integrabilidad. Si dos datos nodales fueran incompatibles, no serían restricciones de una sola función.

## 23.33. Aditividad del valor

[]{#MA-EX-ANM-01-023-033}

[]{#MA-SOL-ANM-01-023-033}

Tomar brechas izquierda/derecha<ε/4. La global es<ε/2. Cualquier etiqueta dada produce Sab=Sac+Scb; encierro da errores<ε/2,<ε/4,<ε/4. Triangular acota la diferencia de integrales por ε. Al valer para todo ε, distancia positiva es imposible y hay igualdad.

**Retorno visual.** Véase [C23-F07](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.34. Orientar sin nuevas piezas

[]{#MA-EX-ANM-01-023-034}

[]{#MA-SOL-ANM-01-023-034}

Aditividad da I0,2=2. Orientación inversa declara I2,0=−2; degenerado declara I1,1=0. No se generan anchos negativos o una partición estricta de longitud cero.

## 23.35. Cambiar un nodo

[]{#MA-EX-ANM-01-023-035}

[]{#MA-SOL-ANM-01-023-035}

C22 acota la diferencia de sumas etiquetadas por2D·malla y conserva el límite. La equivalencia transfiere misma integral a Darboux. En una partición fija el nuevo valor pertenece a piezas cerradas vecinas y puede cambiar sus supremos/ínfimos. Por ejemplo un pico1 en1/2 cambia U de0 a1 en las mitades.

## 23.36. Cotas exteriores

[]{#MA-EX-ANM-01-023-036}

[]{#MA-SOL-ANM-01-023-036}

[]{#MA-SEC-ANM-01-023-008}

Multiplicar las cotas locales por anchuras y sumar da A≤L≤I≤U≤C, con A=ΣaiΔ,C=ΣbiΔ. El medio(A+C)/2 está a distancia≤(C−A)/2 de cualquier número en[A,C]. Las cotas deben ser universales; integrabilidad no viene de una sola partición.

## 23.37. Elegir resolución de un certificado

[]{#MA-EX-ANM-01-023-037}

[]{#MA-SOL-ANM-01-023-037}

Brecha1/n, error medio certificado≤1/(2n). n51 da1/102<1/100. Las sumas etiquetadas arbitrarias tienen certificado1/n, así el mismo n no garantiza mediante esa cota el mismo umbral para todas ellas. Se distinguen los dos aproximantes.

## 23.38. El pico se encierra

[]{#MA-EX-ANM-01-023-038}

[]{#MA-SOL-ANM-01-023-038}

Todos los ínfimos son0. Sólo las piezas[1/2−r,1/2] y[1/2,1/2+r] contienen el pico y tienen supremo1; sus anchuras son r cada una. U2r,L0. Para cada ε elegir r<min(1/2,ε/2) da criterio. La integral queda entre0 y2r para r arbitrariamente pequeño, por lo que vale0.

**Retorno visual.** Véase [C23-F08](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html#fig-anm-c23-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

## 23.39. Integrable sin brecha cero

[]{#MA-EX-ANM-01-023-039}

[]{#MA-SOL-ANM-01-023-039}

El punto1/2 pertenece a al menos una pieza cerrada de anchura positiva. Esa pieza contiene además un punto distinto por no degeneración, donde p0, y el pico donde p1; su oscilación es1. Su contribución positiva impide brecha cero. Integral0 no significa que se alcance en una suma superior.

## 23.40. Brecha persistente

[]{#MA-EX-ANM-01-023-040}

[]{#MA-SOL-ANM-01-023-040}

Cada pieza tiene m0,M1, así L0,UΣΔ=b−a, cualquiera sea la partición. Entonces $\ell=0$,u=b−a>0 y no coinciden. Se necesita la hipótesis para todas las piezas; un dibujo con unas pocas muestras no la prueba.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 23](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux.html) · [Ejercicios](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-23-integral-de-riemann-y-darboux-microcontroles.html)
