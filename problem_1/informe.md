## Problema 1: Greedy

Un día iba Alex por su facultad cuando ve un cuadrado formado por $n \times n$ cuadraditos de color blanco. A su lado, un mensaje ponía lo siguiente: "Las siguientes tuplas de la forma $(x_1, y_1, x_2, y_2)$ son coordenadas para pintar de negro algunos rectángulos. (coordenadas de la esquina inferior derecha y superior izquierda)". Luego se veían $k$ tuplas de cuatro enteros. Finalmente decía: 
"Luego de tener el cuadrado coloreado de negro en las secciones pertinentes, su tarea es invertir el cuadrado a su estado original. En una operación puede seleccionar un rectángulo y pintar todas sus casillas de blanco. El costo de pintar de blanco un rectángulo de $h \times w$ es el mínimo entre $h$ y $w$. Encuentre el costo mínimo para pintar de blanco todo el cuadrado."

En unos 10 minutos Alex fue capaz de resolver el problema. Desgraciadamente esto no es una película y el problema de Alex no era un problema  
del milenio que lo volviera millonario. Pero, ¿sería usted capaz de resolverlo también?

#### Entrada
La primera línea consiste en dos números $n$ y $m$, el tamaño del cuadrado y la cantidad de rectángulos respectivamente. A continuación seguirán $m$ lineas, cada una con 4 números $x1$, $y1$, $x2$, $y2$, $0 \leq x1,x2,y1,y2 \leq n-1$ indicando las coordenada superior izquierda e inferior derecha del rectaguno en el cuadrado respectivamente.

#### Salida
Un número entero indicando el costo mínimo de revertir el color de todos los rectángulos a banco.

### 1.2 Técnicas de solición

- Backtrack
- Greedy

### 1.3 Solución

Del problema tenemos un cuadrando en donde fueron pintados algunos rectángulos los cuales pueden solaparse entre llamos tanto parcial como completamente. Nuestra primera solución para atacar el problema fue crear la solución de fuerza bruta creando un backtrack para poder probar nuestras posteriores optimizaciones.

#### 1.3.1 Backtracking
... ALEX, TU TURNO ...
TODO: Incluir explicación del backtrack
TODO: Incluir complejidad temporal

### 1.3.2 Optimizaciones

Podemos observar que si un rectangulo es cubierto por otro(s) rectáguno(s), este no es necesario pintarlo ya que pintando a los que lo cubren se pintaría este también, evitándonos así un costo innecesario.

Aquí tendríamos otro problema y es en que orden se pintan los cuadrados para asegurarnos de que siempre se pintan solo los necesarios?

Para esto definamos algúnos puntos importantes. 

- Si un rectángulo esta completamente contenido dentro de otro, este no es necesario pintarlo y sólo pintaríamos el grande. Esto es verdad porque aunque pintemos el rectángulo pequeño, igual necesitaríamos pintar el grande, sin embargo si pintamos solo el grande este cubriría el pequeño, por lo que solo tendríamos el costo de pintar el grande.
- Si un rectángulo tiene al menos una casilla la cual no es cubierta por ningún otro rectangulo, entonces este rectángulo hay que pintarlo obligatioriamente. Esto es obvio ya que pintando los demas rectángulos solo pintaríamos una parte del rectáguno quedando algunas casillas en negro todavía que solo serán pintadas de blanco si y solo si pintamos ese rectángulo.

Sabiendo esto entonces podemos ordenar los rectángulos por área con un costo de $O(\log n)$ y comprobando si hay alguno de los dos casos anteriores se cumplen.
- Si hay una casilla que solo es cubierta por el propio rectángulo entonces se pinta
- Si el rectangulo está cubierto completamente por otro(s) rectángulo(s) más grande(s) entonces omitimos pintar este rectangulo y simplemente esperamos a pintar el/los rectángulo(s) más grande(s) que lo(s) cubren.

Este método nos acerca más a la solución pero el costo computacional sigue siendo elevado, ya que estaríamos comprobando por cada rectangulo si algúnos otros lo cubren completa o parcialmente. Esto para un rectángulo tiene un costo computacional de $O(n^3)$, recorriendo cada rectángulo $O(n-1) \eq O(n)$ y por cada uno recorrer todas las casillas de ese rectángulo buscando coincidencias $O(n^2)$, dándonos un costo computacionar por cada rectángulo de $O(n^3)$. Esto, para cada rectángulo del cuadrado es $O(n^4)$

Esta solución tiene un caso que nos falla, el cual abordaremos más adelante.

TODO: Cambiar los títulos 
### 1.3.3 Usando pequeñas optimizaciones

Una mejor forma de resolver el problema es creando una matriz nueva $D$ de $n \cross n$ en donde por cada rectángulo de negro, se pasan por todos tus casillas sumando uno a cada uno. Esto al pasar por todos los rectángulos tenemos en cualquier casilla $i, j$ la cantidad de rectángulos que tienen la casilla $i, j$ de color negro. Sabiendo esto podemos reformular los dos puntos anteriores como sigue:
- Si para un rectángulo, este tiene al menos una casilla con valor $1$, indica que solo el tiene ese cuadrado pintado de negro, por lo que es necesario pintarlo.
- Si para un rectángulo, todas sus casillas tienen valores mayores a uno, indica que hay uno o mas rectángulos que cubren completamente este rectángulo, por lo que no es necesario pintarlo.

Con este enfoque, colocar estos datos en el cuadrado tiene un costo de $O(n^3)$, ya que es por cada rectángulo, recorrer todas las casillas de él.

### 1.3.4 Problemas con el enfoque hasta ahora

El enfoque planteado hasta ahora, aunque no define una solución completa, si especifica como podemos enfrentar los posibles casos al plantear la solución final. Pero este tiene un problema.

Pensemos que siguiendo este enfoque empezando del rectángulo más pequeño al más grande, si encontrarmos un rectángulo $i$ que es cubierto por un rectángulo mayor $i + k$, estaríamos delegando la tarea de pintar el rectágulo $i$ al rectángulo $i + k$, pero, cómo sabemos que el rectángulo $i + k$ es el más grande posible cubre al rectángulo mas pequeño? Como nosotros solo almacenamos la cantidad de rectángulos que cubren una casilla, entonces pasa lo siguiente:

Si el rectángulo tiene todas sus casillas mayores a uno entonces se lo delegamos a los rectángulos que vienen más a delante. Pero cuando llegemos a un rectangulo con las mismas casillas, o sea que cubre parcialmente el rectangulo anterior, como este posiblemente pueda tener todas sus casillas mayores a uno se estaría delegando la tarea de pintar a otro rectángulo, y así sucesivamente hasta el final en donde nunca se sumó este costo.

Para enfrentar esto podemos hacer lo siguente: Al recorrer los rectángulos de menor a mayor, si este tiene al menos un uno, entonces lo pintamos, sino restamos uno a todas sus casillas del rectángulo. Esto garantiza que si cuando un rectángulo mas grande pase por una casilla que previamente era mayor que uno pero para ese momento ya su valor es uno, indica que él es el ultimo rectángulo que queda que debería pintar dicha casilla, ya que los mas pequeños que él "borraron" su color de esa casilla con la seguridad que un rectángulo más ademante lo pintará por él.


TODO: DEMOSTRAR COMPLEJIDAD
TODO: VER COMO DEMUESTRO CORRECTITUD


