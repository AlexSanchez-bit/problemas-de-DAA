## Problema 1: Greedy

Un día iba Alex por su facultad cuando ve un cuadrado formado por $n \times n$ cuadraditos de color blanco. A su lado, un mensaje ponía lo siguiente: "Las siguientes tuplas de la forma $(x_1, y_1, x_2, y_2)$ son coordenadas para pintar de negro algunos rectángulos. (coordenadas de la esquina inferior derecha y superior izquierda)". Luego se veían $k$ tuplas de cuatro enteros. Finalmente decía: 
"Luego de tener el cuadrado coloreado de negro en las secciones pertinentes, su tarea es invertir el cuadrado a su estado original. En una operación puede seleccionar un rectángulo y pintar todas sus casillas de blanco. El costo de pintar de blanco un rectángulo de $h \times w$ es el mínimo entre $h$ y $w$. Encuentre el costo mínimo para pintar de blanco todo el cuadrado."

En unos 10 minutos Alex fue capaz de resolver el problema. Desgraciadamente esto no es una película y el problema de Alex no era un problema  
del milenio que lo volviera millonario. Pero, ¿sería usted capaz de resolverlo también?

#### Entrada
La primera línea consiste en dos números $n$ y $m$, el tamaño del cuadrado y la cantidad de rectángulos respectivamente. A continuación seguirán $m$ lineas, cada una con 4 números $x1$, $y1$, $x2$, $y2$, $0 \leq x1,x2,y1,y2 \leq n-1$ indicando las coordenada superior izquierda e inferior derecha del rectaguno en el cuadrado respectivamente.

#### Salida

Un número entero indicando el costo mínimo de revertir el color de todos los rectángulos a blanco.

### 1.2 Técnicas de solición

- Backtrack
- Greedy

### 1.3 Solución

Del problema tenemos un cuadrado en donde fueron pintados algunos rectángulos los cuales pueden solaparse entre ellos tanto parcial como completamente. Nuestra primera solución para atacar el problema fue crear la solución de fuerza bruta creando un backtrack para poder probar nuestras posteriores soluciones.

#### 1.3.1 Backtracking
... ALEX, TU TURNO ...
TODO: Incluir explicación del backtrack
TODO: Incluir complejidad temporal

### 1.3.2 Optimizaciones

Podemos observar que si un rectangulo es cubierto por otros rectágunos, este no es necesario pintarlo ya que pintando a los que lo cubren se pintaría este también, evitándonos así un costo innecesario.

Aquí tendríamos otro problema y es en que orden se pintan los cuadrados para asegurarnos de que siempre se pintan solo los necesarios?

Para esto definamos algúnos puntos importantes. 

- Si un rectángulo $A$ esta completamente contenido dentro de otro $B$, no es necesario pintar $A$ y sólo pintaríamos $B$. Esto es así porque aunque pintemos $A$, igual necesitaríamos pintar $B$, sin embargo si pintamos solo $B$ este cubriría $A$, por lo que solo tendríamos el costo de pintar uno solo.
- Si un rectángulo $A$ tiene al menos una casilla la cual no es cubierta por ningún otro rectangulo, entonces hay que pintar $A$ obligatioriamente. Esto es obvio ya que pintando los demas rectángulos solo pintaríamos una parte de $A$ quedando algunas casillas en negro todavía que solo serán pintadas de blanco si y solo si pintamos $A$ directamente.

Sabiendo esto entonces podemos ordenar los rectángulos por área con un costo de $O(\log n)$ y comprobando si hay alguno de los dos casos anteriores se cumplen.
- Si hay una casilla que solo es cubierta por el propio rectángulo entonces se pinta
- Si el rectangulo está cubierto completamente por otros rectángulos más grandes entonces omitimos pintar este rectangulo y simplemente esperamos a pintar los rectángulos más grandes que los cubren.

Este método nos acerca más a la solución pero el costo computacional sigue siendo elevado, ya que estaríamos comprobando por cada rectangulo si algúnos otros lo cubren completa o parcialmente. Esto para un rectángulo tiene un costo computacional de $O(n^3)$, recorriendo cada rectángulo $O(n-1) = O(n)$ y por cada uno recorrer todas las casillas de ese rectángulo buscando coincidencias $O(n^2)$, dándonos un costo computacionar por cada rectángulo de $O(n^3)$. Esto, para cada rectángulo del cuadrado es $O(n^4)$

Esta solución tiene un caso que nos falla, el cual abordaremos más adelante.

TODO: Cambiar los títulos 
### 1.3.3 Usando pequeñas optimizaciones

Una mejor forma de resolver el problema es creando una matriz nueva $D$ de $n \times n$ en donde por cada rectángulo de negro, se pasan por todas sus casillas sumando uno a cada una. Esto al pasar por todos los rectángulos tenemos en cualquier casilla $i, j$ la cantidad de rectángulos que tienen la casilla $i, j$ de color negro. Sabiendo esto podemos reformular los dos puntos anteriores como sigue:
- Si para un rectángulo, este tiene al menos una casilla con valor $1$, indica que solo el tiene ese cuadrado pintado de negro, por lo que es necesario pintarlo.
- Si para un rectángulo, todas sus casillas tienen valores mayores a uno, indica que hay uno o mas rectángulos que cubren completamente este rectángulo, por lo que no es necesario pintarlo.

Con este enfoque, colocar estos datos en el cuadrado tiene un costo de $O(n^3)$, ya que es por cada rectángulo, recorrer todas las casillas de él.

TODO: HACER UNA TABLA COMPARATIVA DE TODAS LAS SOLUCIONES (POR COMPLEJIDAD) 

### 1.3.4 Problemas con el enfoque hasta ahora

El enfoque planteado hasta ahora, aunque no define una solución completa, si especifica como podemos enfrentar los posibles casos al plantear la solución final. Pero este tiene un problema.

Pensemos que siguiendo este enfoque empezando del rectángulo más pequeño al más grande, si encontrarmos un rectángulo $i$ que es cubierto por un rectángulo mayor $i + k$, estaríamos delegando la tarea de pintar el rectágulo $i$ al rectángulo $i + k$, pero, cómo sabemos que el rectángulo $i + k$ es el más grande posible que cubre al rectángulo más pequeño? Como nosotros solo almacenamos la cantidad de rectángulos que cubren una casilla, entonces pasa lo siguiente:

Si el rectángulo tiene todas sus casillas mayores a uno entonces se lo delegamos a los rectángulos que vienen más a delante. Pero cuando llegemos a un rectangulo con las mismas casillas, o sea que cubre parcialmente el rectangulo anterior, como este posiblemente pueda tener todas sus casillas mayores a uno se estaría delegando la tarea de pintar a otro rectángulo, y así sucesivamente hasta el final, en donde si todos los rectángulo tenían numeros mayores que uno nunca se habría sumado esos costos.

TODO: Colocar una imagen del ejemplo ese que parte la solución aquí.

Para enfrentar esto podemos hacer lo siguente: Al recorrer los rectángulos de menor a mayor, si este tiene al menos un uno, entonces lo pintamos, sino restamos uno a todas sus casillas del rectángulo. Esto garantiza que si cuando un rectángulo mas grande pase por una casilla que previamente era mayor que uno pero para ese momento ya su valor es uno, indica que él es el ultimo rectángulo que queda que debería pintar dicha casilla, ya que los mas pequeños que él "borraron" su color de esa casilla con la seguridad que un rectángulo más adelante lo pintará por él.

### 1.3.5 Análisis de correctitud

Hasta ahora tenemos claro que:
- Si un rectángulo $A_{w \times h}$ tiene al menos un cuadrado que solo es pintado de negro por él mismo entonces este rectángulo hay que pintarlo de completamente con un costo de $\min {(w, h)}$.
- Si un rectángulo $A_{w_1 \times h_1}$ es __cubierto completamente__ por al menos un rectángulo $B_{ w_2 \times h_2}$ tal que $w_1 \leq w_2$ y $h1 \leq h_2$, o sea, por un rectángulo mayor o igual a él que lo cubra completamente, entonces no es necesario pintar $A$ ya que pintando $B$ se cubre $A$, y el costo sería $\min{(w_2, h_2)}$.
- Si un rectángulo $A_{w \times h}$ está cubierto completamente pero por más de un rectángulo, entonces si pintamos $A$ sólo pintaríamos parcialmente los demás rectángulos, por lo que el costo total sería el costo de pintar $A$ más el costo de pintar los demás, pero si delegamos la tarea de pintar $A$ a los restantes rectángulos, el costo total solo sería el de pintar los demás.
- Se garantiza que pintando los rectángulos de menor a mayor con criterio de ordenación por área éste dará una respuesta correcta porque:
  
  - Los más pequeños solo hay que pintarlos si no están cubiertos completamente por uno mas grande.
  - Si un rectangulo grande está cubierto por varios rectángulos más pequeños y a su vez, el rectángulo grande está cubriendo a los más pequeños (vease como que el grande es una composición de rectángulos mas pequeños), entonces el coste óptimo es pintar el grande. Sea $A_{w \times h}$ el rectángulo grande y asumamos que hay $n$ rectángulos más pequeños $B^{i}_{w_i \times h_i}$, tal que $\forall B^{i}_{w_i \times h_i}, w_i = w \lor h_i = h$, o sea, que todos los rectángulos $B$ cubran a $A$ a todo los alto o a todo lo ancho. 
  
    TODO: Insertar foto para el ejemplo

    Con este emplo garantizamos que solo hallan rectángulos en horizontal o en vertial, pero que no hallan intermedios (figura de abajo). Si se cumple esto entonces el pintar los rectangulos mas pequeños entonces la suma de sus lados más pequeños $h_i$ o $w_i$, entonces $\sum{h_i} = h \land \sum{w_i} = w$. En este caso, si $\forall w_i \leq h_i$, pero $h \leq w$ entonces la solución óptima sería $w$ (porque es la suma de los lados más pequeños), sin embargo esto es un error ya que la solución optimas es $h$, por lo que es mejor pintar $A$ directamente.
    Si por el contrario, $\forall w_i \leq h_i$, y $w \leq h$ entonces la solución óptima si es $w$, entonces da igual pintar $A$ antes que los $B^{i}$ que viceversa, la solución es la misma.
  
  - Si el caso anterior no se cumple y $A$ está formado por varios rectángulos $B^{i}$ pero no todos sus lados son iguales a $w$ o a $h$ como en el caso anterior, quiere decir que hay rectángulos intermedios, (TODO: poner la foto debajo), por lo que la $\sum{w_i} \geq w \lor \sum{h_i} \geq h$, y la solución optima en estos dos casos simpre va a ser pintar $A$ primero.

- Con lo anterior y siguendo la estrategia de descontar uno cada vez que encontramos un rectángulo que es cubierto por uno o varios mas grandes aseguramos como bien dijimos anteriormente, que en cada paso que restamos uno a cada casilla es como si estubiéramos "eliminando" ese rectángulo sin ningún costo, ya que uno o varios mas grandes que él lo cubrirán.


### 1.3.6 Análisis de complejidad

Sea $n$ el tamaño del cuadrado y $m$ la cantidad de rectángulos, donde cada rectángulo tiene como tamaño máximo $n \times n$. El algoritmo consta de 3 partes:

- **Ordenar los rectángulos de menor a mayor por área**: Usando el propio algoritmo de ordenamiento del lengugaje es $O(m \log m)$.
- **Pintar los rectángulos**: Por cada uno de los rectángulos, sumar uno a todas las casillas del mismo. $O(m n^2)$.
- **Calcular la solución**: Por cada rectángulo, recorrer sus casillas buscando al menos una casilla con valor de uno, y si es así entonces despintar este rectángulo (restarle uno a cada casilla). En el caso de que ningún rectángulo cubra a otro entonces el costo es $O(m(n^2 + n^2)) = O(mn^2)$
  
Con estos tres pasos, la complejidad total es:

$$
O(m \log m) + O(mn^2) + O(mn^2) = O(m \log m) + O(mn^2) = O(mn^2)
$$

