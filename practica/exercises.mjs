/** Ejercicios originales demostrativos. No reutilizan identificadores MA-PRB ni establecen ratings calibrados. */
import { validateBank } from './engine.mjs';

export const EXERCISES = [
  { id:'MAP-DEMO-001', area:'aritmetica', difficulty:1, provisionalRating:800, title:'Sumar fracciones', prompt:'Calcula 1/2 + 1/3.', steps:[
    {question:'¿Cuál es un denominador común conveniente?',options:['5','6','3'],correctIndex:1,notation:'m.c.m.(2, 3) = 6',explanation:'6 es múltiplo tanto de 2 como de 3.'},
    {question:'¿Cómo expresamos ambas fracciones con denominador 6?',options:['3/6 + 2/6','2/6 + 2/6','1/6 + 1/6'],correctIndex:0,notation:'1/2 = 3/6; 1/3 = 2/6',explanation:'Multiplicamos numerador y denominador por 3 y 2, respectivamente.'},
    {question:'¿Cuál es la suma?',options:['5/12','2/5','5/6'],correctIndex:2,notation:'3/6 + 2/6 = 5/6',explanation:'Sumamos numeradores y conservamos el denominador común.'}
  ]},
  { id:'MAP-DEMO-002', area:'algebra', difficulty:2, provisionalRating:1050, title:'Resolver una ecuación', prompt:'Resuelve 2(x − 3) = x + 5.', steps:[
    {question:'¿Qué transformación es válida primero?',options:['Distribuir el 2','Dividir solo el lado izquierdo por 2','Sumar 3 únicamente al lado derecho'],correctIndex:0,notation:'2x − 6 = x + 5',explanation:'La propiedad distributiva transforma 2(x − 3) en 2x − 6.'},
    {question:'¿Cómo agrupamos términos con x?',options:['Restar x a ambos lados','Restar x solo a la izquierda','Multiplicar ambos lados por x'],correctIndex:0,notation:'x − 6 = 5',explanation:'Restar x a ambos miembros conserva la equivalencia.'},
    {question:'¿Cuál es la solución?',options:['x = −1','x = 11','x = 5'],correctIndex:1,notation:'x = 11',explanation:'Sumar 6 a ambos miembros da x = 11; comprobación: 2(11−3)=16 y 11+5=16.'}
  ]},
  { id:'MAP-DEMO-003', area:'calculo', difficulty:3, provisionalRating:1250, title:'Regla de la cadena', prompt:'Deriva f(x) = (x² + 1)³.', steps:[
    {question:'¿Qué estrategia conviene utilizar primero?',options:['Regla del producto','Regla de la cadena','Regla del cociente'],correctIndex:1,notation:'Estrategia: regla de la cadena.',explanation:'Se trata de una composición de funciones: cubo de una expresión interior.'},
    {question:'¿Cuál es la función interior?',options:['u(x) = x² + 1','u(x) = 3x²','u(x) = (x² + 1)³'],correctIndex:0,notation:'u(x) = x² + 1',explanation:'La función exterior es g(u)=u³.'},
    {question:'¿Cuál es la derivada de u?',options:['2x + 1','2x','x'],correctIndex:1,notation:"u′(x) = 2x",explanation:'La derivada de x² es 2x y la de la constante 1 es cero.'},
    {question:'¿Qué resultado produce la regla de la cadena?',options:['3(x² + 1)²','6x(x² + 1)²','6x(x² + 1)³'],correctIndex:1,notation:"f′(x) = 3(x² + 1)² · 2x = 6x(x² + 1)²",explanation:'Se multiplica la derivada de la función exterior evaluada en u por u′.'}
  ]},
  { id:'MAP-DEMO-004', area:'demostraciones', difficulty:3, provisionalRating:1300, title:'Una prueba por contraposición', prompt:'Demuestra: si n² es impar, entonces n es impar (n entero).', steps:[
    {question:'¿Qué proposición contrapositiva debemos probar?',options:['Si n es par, n² es par','Si n es impar, n² es impar','Si n² es par, n es par'],correctIndex:0,notation:'Contrapositiva: n par ⇒ n² par.',explanation:'La proposición P⇒Q es equivalente a ¬Q⇒¬P.'},
    {question:'Si n es par, ¿cómo lo representamos?',options:['n = 2k + 1 para algún k entero','n = 2k para algún k entero','n = k/2 para algún k entero'],correctIndex:1,notation:'n = 2k, con k ∈ ℤ.',explanation:'Esta es la definición de entero par.'},
    {question:'¿Cómo se expresa n² a partir de n = 2k?',options:['n² = 2k²','n² = 4k² = 2(2k²)','n² = 4k + 2'],correctIndex:1,notation:'n² = 4k² = 2(2k²).',explanation:'Como 2k² es entero, n² es par.'},
    {question:'¿Qué conclusión es válida?',options:['La recíproca quedó demostrada','Probamos la contrapositiva y, por equivalencia, la proposición original','La prueba requiere suponer que n es positivo'],correctIndex:1,notation:'n² impar ⇒ n impar. ∎',explanation:'Hemos probado la contrapositiva sobre todos los enteros, sin requerir positividad.'}
  ]}
];
validateBank(EXERCISES);
