/** Lote original MA-Práctica: 10 ejercicios de Álgebra.
 * IDs provisionales e inmutables, ratings ilustrativos NO calibrados.
 * Enunciados, opciones y explicaciones escritos específicamente para esta app.
 * La notación TeX explícita es editorial; no afecta al motor ni a las respuestas.
 */
export const ALGEBRA_PILOT = [
  {
    id: 'MAP-DEMO-005', area: 'algebra', difficulty: 2, provisionalRating: 1000,
    title: 'Ecuación con fracciones',
    prompt: 'Resuelve \\(\\frac{x-1}{3}+\\frac{x+2}{2}=4\\).',
    steps: [
      { question: '¿Qué igualdad resulta al multiplicar ambos miembros por 6?',
        options: ['\\(2(x-1)+3(x+2)=24\\)', '\\(3(x-1)+2(x+2)=24\\)', '\\(2(x-1)+3(x+2)=4\\)'], correctIndex: 0,
        notation: '\\(2(x-1)+3(x+2)=24\\)', explanation: 'El 6 multiplica a ambos miembros; en cada fracción cancela su denominador.' },
      { question: '¿Cómo queda la ecuación después de distribuir y reunir términos?',
        options: ['\\(5x+8=24\\)', '\\(5x+4=24\\)', '\\(5x-4=24\\)'], correctIndex: 1,
        notation: '\\(2x-2+3x+6=24\\), luego \\(5x+4=24\\).', explanation: 'Los términos en x suman 5x y las constantes suman 4.' },
      { question: '¿Qué igualdad obtenemos al aislar el término con x?',
        options: ['\\(5x=28\\)', '\\(x=20\\)', '\\(5x=20\\)'], correctIndex: 2,
        notation: '\\(5x=24-4=20\\)', explanation: 'Restar 4 a ambos miembros conserva la equivalencia.' },
      { question: '¿Cuál es la solución?', options: ['\\(x=5\\)', '\\(x=4\\)', '\\(x=-4\\)'], correctIndex: 1,
        notation: '\\(x=4\\)', explanation: 'Dividimos por 5. Comprobación: 3/3 + 6/2 = 1 + 3 = 4.' }
    ]
  },
  {
    id: 'MAP-DEMO-006', area: 'algebra', difficulty: 1, provisionalRating: 900,
    title: 'Una identidad', prompt: 'Resuelve \\(3(x+2)-3x=6\\).',
    steps: [
      { question: '¿Cuál es la distribución correcta?',
        options: ['\\(3x+2-3x=6\\)', '\\(3x+6-3x=6\\)', '\\(3x+6-x=6\\)'], correctIndex: 1,
        notation: '\\(3x+6-3x=6\\)', explanation: 'El factor 3 multiplica tanto a x como a 2.' },
      { question: '¿Qué queda al cancelar términos iguales?',
        options: ['\\(6=6\\)', '\\(3x=0\\)', '\\(0=6\\)'], correctIndex: 0,
        notation: '\\(6=6\\)', explanation: 'Los términos 3x y −3x se anulan para cualquier x.' },
      { question: '¿Cuál es el conjunto solución?',
        options: ['Solo \\(x=0\\)', 'No tiene solución', 'Todos los números reales'], correctIndex: 2,
        notation: '\\(S=\\mathbb{R}\\)', explanation: 'La igualdad 6=6 es verdadera para todo valor real de x; es una identidad.' }
    ]
  },
  {
    id: 'MAP-DEMO-007', area: 'algebra', difficulty: 1, provisionalRating: 950,
    title: 'Ecuación incompatible', prompt: 'Resuelve \\(2(x+1)=2x+5\\).',
    steps: [
      { question: '¿Qué obtenemos al distribuir?',
        options: ['\\(2x+1=2x+5\\)', '\\(2x+2=x+5\\)', '\\(2x+2=2x+5\\)'], correctIndex: 2,
        notation: '\\(2x+2=2x+5\\)', explanation: 'Multiplicamos por 2 los dos términos del paréntesis.' },
      { question: '¿Qué sucede al restar 2x de ambos miembros?',
        options: ['\\(2=5\\)', '\\(x=3\\)', '\\(0=5\\)'], correctIndex: 0,
        notation: '\\(2=5\\)', explanation: 'Se eliminan los términos 2x y aparece una igualdad falsa.' },
      { question: '¿Qué conclusión corresponde?',
        options: ['Todos los reales son solución', 'No existe solución', 'La solución es \\(x=3\\)'], correctIndex: 1,
        notation: '\\(S=\\varnothing\\)', explanation: 'Ningún valor de x puede convertir la igualdad falsa 2=5 en verdadera.' }
    ]
  },
  {
    id: 'MAP-DEMO-008', area: 'algebra', difficulty: 2, provisionalRating: 1050,
    title: 'Extraer factor común', prompt: 'Factoriza \\(6x^2-9x\\).',
    steps: [
      { question: '¿Cuál es el máximo factor monomial común?',
        options: ['\\(3\\)', '\\(3x\\)', '\\(x^2\\)'], correctIndex: 1,
        notation: '\\(3x\\)', explanation: 'El máximo divisor numérico de 6 y 9 es 3 y la menor potencia común de x es x.' },
      { question: '¿Qué expresión permanece dentro del paréntesis?',
        options: ['\\(2x-9\\)', '\\(2x-6\\)', '\\(2x-3\\)'], correctIndex: 2,
        notation: '\\(\\frac{6x^2}{3x}=2x\\), \\(\\frac{-9x}{3x}=-3\\).', explanation: 'Dividimos cada término por 3x (como identidad polinómica, el resultado también vale en x=0).' },
      { question: '¿Cuál es la factorización correcta?',
        options: ['\\(3x(2x-3)\\)', '\\(3x(2x+3)\\)', '\\(3(2x-3)\\)'], correctIndex: 0,
        notation: '\\(6x^2-9x=3x(2x-3)\\)', explanation: 'La distributividad comprueba: 3x·2x=6x² y 3x·(−3)=−9x.' }
    ]
  },
  {
    id: 'MAP-DEMO-009', area: 'algebra', difficulty: 2, provisionalRating: 1050,
    title: 'Diferencia de cuadrados', prompt: 'Factoriza \\(x^2-25\\).',
    steps: [
      { question: '¿Qué dos cuadrados aparecen?',
        options: ['\\(x^2\\) y \\(5^2\\)', '\\(x^2\\) y \\(25^2\\)', '\\(x\\) y \\(5\\)'], correctIndex: 0,
        notation: '\\(x^2-5^2\\)', explanation: '25 es el cuadrado de 5.' },
      { question: '¿Qué identidad es pertinente?',
        options: ['\\(a^2-b^2=(a-b)^2\\)', '\\(a^2-b^2=(a-b)(a+b)\\)', '\\(a^2-b^2=(a+b)^2\\)'], correctIndex: 1,
        notation: '\\(a^2-b^2=(a-b)(a+b)\\)', explanation: 'El producto elimina términos cruzados: (a−b)(a+b)=a²−b².' },
      { question: '¿Cuál es el producto correcto?',
        options: ['\\((x-5)^2\\)', '\\((x+5)^2\\)', '\\((x-5)(x+5)\\)'], correctIndex: 2,
        notation: '\\(x^2-25=(x-5)(x+5)\\)', explanation: 'Al multiplicar aparece x²+5x−5x−25=x²−25.' }
    ]
  },
  {
    id: 'MAP-DEMO-010', area: 'algebra', difficulty: 2, provisionalRating: 1100,
    title: 'Producto igual a cero', prompt: 'Resuelve \\((x-2)(x+5)=0\\).',
    steps: [
      { question: '¿Cómo se aplica la propiedad del producto nulo?',
        options: ['\\(x-2=0\\) y \\(x+5=0\\)', '\\(x-2=0\\) o \\(x+5=0\\)', '\\(x-2=x+5\\)'], correctIndex: 1,
        notation: '\\(x-2=0\\) o \\(x+5=0\\)', explanation: 'En los reales, un producto es cero si al menos uno de los factores es cero.' },
      { question: '¿Qué solución aporta el primer factor?',
        options: ['\\(x=-2\\)', '\\(x=5\\)', '\\(x=2\\)'], correctIndex: 2,
        notation: '\\(x-2=0\\Rightarrow x=2\\)', explanation: 'Sumamos 2 a ambos miembros.' },
      { question: '¿Qué otra solución aporta el segundo factor?',
        options: ['\\(x=-5\\)', '\\(x=5\\)', '\\(x=-2\\)'], correctIndex: 0,
        notation: '\\(S=\\{-5,2\\}\\)', explanation: 'x+5=0 implica x=−5; ambos valores anulan un factor.' }
    ]
  },
  {
    id: 'MAP-DEMO-011', area: 'algebra', difficulty: 2, provisionalRating: 1100,
    title: 'Inecuación y signo', prompt: 'Resuelve \\(-3x+6>0\\).',
    steps: [
      { question: '¿Qué resulta al restar 6?',
        options: ['\\(-3x>6\\)', '\\(-3x<-6\\)', '\\(-3x>-6\\)'], correctIndex: 2,
        notation: '\\(-3x>-6\\)', explanation: 'Restar la misma cantidad conserva el sentido de la desigualdad.' },
      { question: '¿Qué ocurre al dividir por −3?',
        options: ['\\(x<2\\)', '\\(x>2\\)', '\\(x<-2\\)'], correctIndex: 0,
        notation: '\\(x<2\\)', explanation: 'Dividir por un número negativo invierte el sentido de la desigualdad.' },
      { question: '¿Cómo se expresa el conjunto solución?',
        options: ['\\((2,\\infty)\\)', '\\((-\\infty,2)\\)', '\\((-\\infty,2]\\)'], correctIndex: 1,
        notation: '\\(S=(-\\infty,2)\\)', explanation: 'El 2 se excluye: en x=2 el miembro izquierdo vale 0 y la desigualdad es estricta.' }
    ]
  },
  {
    id: 'MAP-DEMO-012', area: 'algebra', difficulty: 3, provisionalRating: 1200,
    title: 'Ecuación racional', prompt: 'Resuelve \\(\\frac{x+1}{x-3}=2\\).',
    steps: [
      { question: '¿Qué restricción impone el denominador?',
        options: ['\\(x\\ne-3\\)', '\\(x\\ne3\\)', 'Ninguna restricción'], correctIndex: 1,
        notation: '\\(x\\ne3\\)', explanation: 'La expresión original no está definida en x=3.' },
      { question: 'Para x distinto de 3, ¿qué igualdad es equivalente?',
        options: ['\\(x+1=2(x-3)\\)', '\\(x+1=2x-3\\)', '\\(x+1=2(x+3)\\)'], correctIndex: 0,
        notation: '\\(x+1=2(x-3)\\)', explanation: 'Multiplicamos ambos miembros por el denominador no nulo.' },
      { question: '¿Qué resulta al distribuir el 2?',
        options: ['\\(x+1=2x-3\\)', '\\(x+1=x-6\\)', '\\(x+1=2x-6\\)'], correctIndex: 2,
        notation: '\\(x+1=2x-6\\)', explanation: 'La distributividad produce 2x−6.' },
      { question: '¿Cuál es la solución admisible?',
        options: ['\\(x=3\\)', '\\(x=7\\)', '\\(x=-7\\)'], correctIndex: 1,
        notation: '\\(x=7\\)', explanation: 'De x+1=2x−6 resulta x=7; satisface x≠3 y 8/4=2.' }
    ]
  },
  {
    id: 'MAP-DEMO-013', area: 'algebra', difficulty: 2, provisionalRating: 1100,
    title: 'Sistema por eliminación', prompt: 'Resuelve \\(x+y=7\\), \\(x-y=1\\).',
    steps: [
      { question: '¿Qué obtenemos al sumar ambas ecuaciones?',
        options: ['\\(2y=8\\)', '\\(2x=8\\)', '\\(2x=6\\)'], correctIndex: 1,
        notation: '\\(2x=8\\)', explanation: 'y y −y se cancelan; los miembros derechos suman 8.' },
      { question: '¿Cuánto vale x?',
        options: ['\\(x=4\\)', '\\(x=3\\)', '\\(x=8\\)'], correctIndex: 0,
        notation: '\\(x=4\\)', explanation: 'Dividir 2x=8 por 2 da x=4.' },
      { question: '¿Cuál es el valor correspondiente de y?',
        options: ['\\(y=4\\)', '\\(y=-3\\)', '\\(y=3\\)'], correctIndex: 2,
        notation: '\\((x,y)=(4,3)\\)', explanation: 'Sustituimos en x+y=7: y=3; la otra ecuación verifica 4−3=1.' }
    ]
  },
  {
    id: 'MAP-DEMO-014', area: 'algebra', difficulty: 2, provisionalRating: 1050,
    title: 'Las dos raíces', prompt: 'Resuelve \\(x^2=9\\) en los reales.',
    steps: [
      { question: '¿Qué candidatos obtenemos al considerar ambos signos?',
        options: ['Solo \\(x=3\\)', '\\(x=9\\) o \\(x=-9\\)', '\\(x=3\\) o \\(x=-3\\)'], correctIndex: 2,
        notation: '\\(x=\\pm3\\)', explanation: 'Tanto 3 como −3 pueden tener cuadrado 9; no debemos perder la raíz negativa.' },
      { question: '¿Qué ocurre al comprobar el candidato negativo?',
        options: ['\\((-3)^2=9\\)', '\\((-3)^2=-9\\)', '\\((-3)^2=6\\)'], correctIndex: 0,
        notation: '\\((-3)^2=9\\)', explanation: 'El producto de dos números negativos es positivo.' },
      { question: '¿Cuál es el conjunto de soluciones?',
        options: ['\\(S=\\{3\\}\\)', '\\(S=\\{-3,3\\}\\)', '\\(S=\\{-9,9\\}\\)'], correctIndex: 1,
        notation: '\\(S=\\{-3,3\\}\\)', explanation: 'Ambos candidatos satisfacen la igualdad; ningún otro real tiene valor absoluto 3.' }
    ]
  }
];
