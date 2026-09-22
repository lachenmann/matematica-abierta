/** Diez ejercicios originales de Álgebra para MA-Práctica: ratings ilustrativos, no calibrados.
 * TeX explícito únicamente para presentación; claves matemáticas comprobadas en tests.
 */
export const ALGEBRA_PILOT = [
{id:'MAP-DEMO-005',area:'algebra',difficulty:2,provisionalRating:1000,title:'Ecuación con fracciones',prompt:'Resuelve \\(\\frac{x-1}{3}+\\frac{x+2}{2}=4\\).',steps:[
{question:'¿Qué igualdad resulta al multiplicar ambos miembros por 6?',options:['\\(2(x-1)+3(x+2)=24\\)','\\(3(x-1)+2(x+2)=24\\)','\\(2(x-1)+3(x+2)=4\\)'],correctIndex:0,notation:'\\(2(x-1)+3(x+2)=24\\)',explanation:'El 6 multiplica ambos miembros y cancela los dos denominadores.'},
{question:'¿Cómo queda al distribuir y reunir términos?',options:['\\(5x+8=24\\)','\\(5x+4=24\\)','\\(5x-4=24\\)'],correctIndex:1,notation:'\\(2x-2+3x+6=24\\), luego \\(5x+4=24\\).',explanation:'Los términos con x suman 5x y las constantes suman 4.'},
{question:'¿Qué igualdad resulta al aislar el término con x?',options:['\\(5x=28\\)','\\(x=20\\)','\\(5x=20\\)'],correctIndex:2,notation:'\\(5x=24-4=20\\)',explanation:'Restamos 4 en ambos miembros de la ecuación.'},
{question:'¿Cuál es la solución?',options:['\\(x=5\\)','\\(x=4\\)','\\(x=-4\\)'],correctIndex:1,notation:'\\(x=4\\)',explanation:'Dividimos por 5. Comprobación: 3/3 + 6/2 = 1+3 = 4.'}
]},
{id:'MAP-DEMO-006',area:'algebra',difficulty:1,provisionalRating:900,title:'Una identidad',prompt:'Resuelve \\(3(x+2)-3x=6\\).',steps:[
{question:'¿Cuál es la distribución correcta?',options:['\\(3x+2-3x=6\\)','\\(3x+6-3x=6\\)','\\(3x+6-x=6\\)'],correctIndex:1,notation:'\\(3x+6-3x=6\\)',explanation:'El factor 3 multiplica los dos términos del paréntesis.'},
{question:'¿Qué queda al reunir términos?',options:['\\(6=6\\)','\\(3x=0\\)','\\(0=6\\)'],correctIndex:0,notation:'\\(6=6\\)',explanation:'Los términos 3x y −3x se anulan para todo x.'},
{question:'¿Cuál es el conjunto solución?',options:['Solo \\(x=0\\)','No tiene solución','Todos los números reales'],correctIndex:2,notation:'\\(S=\\mathbb{R}\\)',explanation:'La igualdad 6=6 es verdadera para cualquier valor de x: es una identidad.'}
]},
{id:'MAP-DEMO-007',area:'algebra',difficulty:1,provisionalRating:950,title:'Ecuación incompatible',prompt:'Resuelve \\(2(x+1)=2x+5\\).',steps:[
{question:'¿Qué obtenemos al distribuir?',options:['\\(2x+1=2x+5\\)','\\(2x+2=x+5\\)','\\(2x+2=2x+5\\)'],correctIndex:2,notation:'\\(2x+2=2x+5\\)',explanation:'Distribuimos el 2 sobre ambos términos del paréntesis.'},
{question:'¿Qué sucede al restar 2x a ambos miembros?',options:['\\(2=5\\)','\\(x=3\\)','\\(0=5\\)'],correctIndex:0,notation:'\\(2=5\\)',explanation:'Se cancelan los términos 2x, dejando una afirmación falsa.'},
{question:'¿Cuál es la conclusión?',options:['Todos los reales son solución','No existe solución','La solución es \\(x=3\\)'],correctIndex:1,notation:'\\(S=\\varnothing\\)',explanation:'Ningún valor de x puede hacer que se cumpla la igualdad 2=5.'}
]},
{id:'MAP-DEMO-008',area:'algebra',difficulty:2,provisionalRating:1050,title:'Extraer factor común',prompt:'Factoriza \\(6x^2-9x\\).',steps:[
{question:'¿Cuál es el máximo factor monomial común?',options:['\\(3\\)','\\(3x\\)','\\(x^2\\)'],correctIndex:1,notation:'\\(3x\\)',explanation:'El máximo divisor común de los coeficientes es 3 y la menor potencia de x es x.'},
{question:'¿Qué expresión queda dentro del paréntesis?',options:['\\(2x-9\\)','\\(2x-6\\)','\\(2x-3\\)'],correctIndex:2,notation:'\\(6x^2=(3x)(2x)\\); \\(-9x=(3x)(-3)\\).',explanation:'Descomponemos cada término por multiplicación, sin dividir por x, de modo que también vale si x=0.'},
{question:'¿Cuál es la factorización correcta?',options:['\\(3x(2x-3)\\)','\\(3x(2x+3)\\)','\\(3(2x-3)\\)'],correctIndex:0,notation:'\\(6x^2-9x=3x(2x-3)\\)',explanation:'La propiedad distributiva recupera los términos 6x² y −9x.'}
]},
{id:'MAP-DEMO-009',area:'algebra',difficulty:2,provisionalRating:1050,title:'Diferencia de cuadrados',prompt:'Factoriza \\(x^2-25\\).',steps:[
{question:'¿Qué cuadrados aparecen?',options:['\\(x^2\\) y \\(5^2\\)','\\(x^2\\) y \\(25^2\\)','\\(x\\) y \\(5\\)'],correctIndex:0,notation:'\\(x^2-5^2\\)',explanation:'Como 25 es el cuadrado de 5, se trata de una diferencia de cuadrados.'},
{question:'¿Qué identidad resulta pertinente?',options:['\\(a^2-b^2=(a-b)^2\\)','\\(a^2-b^2=(a-b)(a+b)\\)','\\(a^2-b^2=(a+b)^2\\)'],correctIndex:1,notation:'\\(a^2-b^2=(a-b)(a+b)\\)',explanation:'Al expandir el producto, los términos cruzados se cancelan.'},
{question:'¿Cuál es el producto correcto?',options:['\\((x-5)^2\\)','\\((x+5)^2\\)','\\((x-5)(x+5)\\)'],correctIndex:2,notation:'\\(x^2-25=(x-5)(x+5)\\)',explanation:'La expansión da x²+5x−5x−25, de modo que queda x²−25.'}
]},
{id:'MAP-DEMO-010',area:'algebra',difficulty:2,provisionalRating:1100,title:'Producto igual a cero',prompt:'Resuelve \\((x-2)(x+5)=0\\).',steps:[
{question:'¿Cómo se aplica la propiedad del producto nulo?',options:['\\(x-2=0\\) y \\(x+5=0\\)','\\(x-2=0\\) o \\(x+5=0\\)','\\(x-2=x+5\\)'],correctIndex:1,notation:'\\(x-2=0\\) o \\(x+5=0\\)',explanation:'Un producto de números reales vale cero si alguno de sus factores es cero.'},
{question:'¿Qué solución aporta el primer factor?',options:['\\(x=-2\\)','\\(x=5\\)','\\(x=2\\)'],correctIndex:2,notation:'\\(x-2=0\\) implica \\(x=2\\)',explanation:'Sumar 2 a ambos miembros proporciona x=2.'},
{question:'¿Qué solución aporta el segundo factor?',options:['\\(x=-5\\)','\\(x=5\\)','\\(x=-2\\)'],correctIndex:0,notation:'\\(S=\\{-5,2\\}\\)',explanation:'De x+5=0 obtenemos −5; ambos valores anulan al menos un factor.'}
]},
{id:'MAP-DEMO-011',area:'algebra',difficulty:2,provisionalRating:1100,title:'Inecuación y signo',prompt:'Resuelve \\(-3x+6>0\\).',steps:[
{question:'¿Qué resulta al restar 6?',options:['\\(-3x>6\\)','\\(-3x<-6\\)','\\(-3x>-6\\)'],correctIndex:2,notation:'\\(-3x>-6\\)',explanation:'Restar la misma cantidad en ambos miembros preserva el sentido.'},
{question:'¿Qué ocurre al dividir por −3?',options:['\\(x<2\\)','\\(x>2\\)','\\(x<-2\\)'],correctIndex:0,notation:'\\(x<2\\)',explanation:'Dividir por un número negativo invierte el signo de la desigualdad.'},
{question:'¿Cuál es el conjunto solución?',options:['\\((2,\\infty)\\)','\\((-\\infty,2)\\)','\\((-\\infty,2]\\)'],correctIndex:1,notation:'\\(S=(-\\infty,2)\\)',explanation:'2 está excluido: el miembro izquierdo es cero y la desigualdad es estricta.'}
]},
{id:'MAP-DEMO-012',area:'algebra',difficulty:3,provisionalRating:1200,title:'Ecuación racional',prompt:'Resuelve \\(\\frac{x+1}{x-3}=2\\).',steps:[
{question:'¿Qué restricción impone el denominador?',options:['\\(x\\ne-3\\)','\\(x\\ne3\\)','Ninguna restricción'],correctIndex:1,notation:'\\(x\\ne3\\)',explanation:'El cociente de partida no está definido en x=3.'},
{question:'Para x distinto de 3, ¿qué igualdad es equivalente?',options:['\\(x+1=2(x-3)\\)','\\(x+1=2x-3\\)','\\(x+1=2(x+3)\\)'],correctIndex:0,notation:'\\(x+1=2(x-3)\\)',explanation:'Multiplicamos ambos miembros por el denominador no nulo.'},
{question:'¿Qué resulta al distribuir?',options:['\\(x+1=2x-3\\)','\\(x+1=x-6\\)','\\(x+1=2x-6\\)'],correctIndex:2,notation:'\\(x+1=2x-6\\)',explanation:'Multiplicamos por 2 cada término: 2x−6.'},
{question:'¿Cuál es la solución admisible?',options:['\\(x=3\\)','\\(x=7\\)','\\(x=-7\\)'],correctIndex:1,notation:'\\(x=7\\)',explanation:'La ecuación da x=7, cumple x≠3 y al sustituir obtenemos 8/4=2.'}
]},
{id:'MAP-DEMO-013',area:'algebra',difficulty:2,provisionalRating:1100,title:'Sistema por eliminación',prompt:'Resuelve \\(x+y=7\\), \\(x-y=1\\).',steps:[
{question:'¿Qué obtenemos al sumar ambas ecuaciones?',options:['\\(2y=8\\)','\\(2x=8\\)','\\(2x=6\\)'],correctIndex:1,notation:'\\(2x=8\\)',explanation:'Los términos y y −y se cancelan; a la derecha resulta 8.'},
{question:'¿Cuánto vale x?',options:['\\(x=4\\)','\\(x=3\\)','\\(x=8\\)'],correctIndex:0,notation:'\\(x=4\\)',explanation:'Dividimos la igualdad 2x=8 por 2.'},
{question:'¿Cuánto vale y?',options:['\\(y=4\\)','\\(y=-3\\)','\\(y=3\\)'],correctIndex:2,notation:'\\((x,y)=(4,3)\\)',explanation:'Sustituir x=4 en x+y=7 da y=3; la segunda ecuación también se cumple.'}
]},
{id:'MAP-DEMO-014',area:'algebra',difficulty:2,provisionalRating:1050,title:'Las dos raíces',prompt:'Resuelve \\(x^2=9\\) en los reales.',steps:[
{question:'¿Qué candidatos obtenemos al considerar ambos signos?',options:['Solo \\(x=3\\)','\\(x=9\\) o \\(x=-9\\)','\\(x=3\\) o \\(x=-3\\)'],correctIndex:2,notation:'\\(x=\\pm3\\)',explanation:'Tanto 3 como −3 tienen cuadrado 9, de modo que deben considerarse ambos.'},
{question:'¿Qué ocurre al comprobar el candidato negativo?',options:['\\((-3)^2=9\\)','\\((-3)^2=-9\\)','\\((-3)^2=6\\)'],correctIndex:0,notation:'\\((-3)^2=9\\)',explanation:'Multiplicar dos números negativos da un producto positivo.'},
{question:'¿Cuál es el conjunto solución?',options:['\\(S=\\{3\\}\\)','\\(S=\\{-3,3\\}\\)','\\(S=\\{-9,9\\}\\)'],correctIndex:1,notation:'\\(S=\\{-3,3\\}\\)',explanation:'Ambos candidatos satisfacen la igualdad y no existen otros reales con cuadrado 9.'}
]}
];
