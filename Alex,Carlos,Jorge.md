# Problemas

## Grid

Un día iba Alex por su facultad cuando ve un cuadrado formado por $n \times n$  
cuadraditos de color blanco. A su lado, un mensaje ponía lo siguiente: "Las  
siguientes tuplas de la forma $(x_1, y_1, x_2, y_2)$ son coordenadas para pintar de  
negro algunos rectángulos. (coordenadas de la esquina inferior derecha y superior  
izquierda)" Luego se veían $k$ tuplas de cuatro enteros. Finalmente decía:  
"Luego de tener el cuadrado coloreado de negro en las secciones pertinentes, su  
tarea es invertir el cuadrado a su estado original. En una operación puede seleccionar  
un rectángulo y pintar todas sus casillas de blanco. El costo de pintar  
de blanco un rectángulo de $h \times w$ es el mínimo entre $h$ y $w$. Encuentre el costo  
mínimo para pintar de blanco todo el cuadrado."

Solución profundizada usando Programación Dinámica (DP):

1. Característica explotada:
   La característica principal que se explota es la subestructura óptima. El costo mínimo para blanquear una región más grande puede calcularse a partir de los costos mínimos de regiones más pequeñas.

2. Subestructura óptima:
   Sea $DP[i][j]$ el costo mínimo para blanquear la submatriz desde (1,1) hasta (i,j). Entonces:
   
   $DP[i][j] = \begin{cases} 
   \min(i, j) & \text{si la celda (i,j) es negra} \\
   \min(DP[i-1][j], DP[i][j-1]) & \text{si la celda (i,j) es blanca}
   \end{cases}$

3. Demostración formal:

   Teorema: El algoritmo DP propuesto encuentra el costo mínimo para blanquear todo el cuadrado.

   Prueba (por inducción):
   
   Base: Para un cuadrado 1x1, el algoritmo es trivialmente correcto.
   
   Hipótesis inductiva: Asumamos que el algoritmo es correcto para todos los cuadrados de tamaño menor a nxn.
   
   Paso inductivo: Consideremos un cuadrado de tamaño nxn.
   - Si la celda (n,n) es blanca, no necesita ser blanqueada. El costo mínimo será el mínimo entre blanquear hasta (n-1,n) o hasta (n,n-1).
   - Si la celda (n,n) es negra, tenemos dos opciones:
     a) Blanquearla individualmente con costo min(n,n).
     b) Incluirla en un rectángulo más grande que ya estamos blanqueando.
   
   El algoritmo elige el mínimo entre estas opciones, lo cual es óptimo dado que hemos considerado todas las posibilidades.

   Por el principio de inducción, el algoritmo es correcto para todos los tamaños de cuadrado.

4. Algoritmo detallado:

   ```python
   def solve(n, black_rectangles):
       # Inicializar matriz M
       M = [[0] * (n+1) for _ in range(n+1)]
       
       # Marcar rectángulos negros
       for x1, y1, x2, y2 in black_rectangles:
           M[x1][y1] += 1
           M[x2+1][y1] -= 1
           M[x1][y2+1] -= 1
           M[x2+1][y2+1] += 1
       
       # Suma acumulativa 2D
       for i in range(1, n+1):
           for j in range(1, n+1):
               M[i][j] += M[i-1][j] + M[i][j-1] - M[i-1][j-1]
       
       # DP
       DP = [[0] * (n+1) for _ in range(n+1)]
       for i in range(1, n+1):
           for j in range(1, n+1):
               if M[i][j] > 0:  # Celda negra
                   DP[i][j] = min(i, j)
               else:  # Celda blanca
                   DP[i][j] = min(DP[i-1][j], DP[i][j-1])
       
       return DP[n][n]
   ```

5. Complejidad:
   - Tiempo: O(n^2 + k), donde k es el número de rectángulos negros.
   - Espacio: O(n^2)

Esta solución es óptima porque considera todas las posibles formas de blanquear el cuadrado, utiliza la subestructura óptima del problema, y evita recálculos almacenando resultados intermedios.

En unos 10 minutos Alex fue capaz de resolver el problema. Desgraciadamente  
esto no es una película y el problema de Alex no era un problema  
del milenio que lo volviera millonario. Pero, ¿sería usted capaz de resolverlo  
también?

Análisis del problema:

1. Programación Dinámica:
   - Posible: Sí
   - Justificación: El problema puede descomponerse en subproblemas más pequeños y las soluciones óptimas de estos subproblemas pueden combinarse para obtener la solución óptima global.
   - Hint: Considere una matriz 2D donde cada celda representa el costo mínimo para blanquear esa región del cuadrado.

2. Greedy (Voraz):
   - Posible: No
   - Justificación: La elección localmente óptima en cada paso no garantiza una solución globalmente óptima en este caso, ya que la elección de un rectángulo afecta las opciones futuras.

3. Flujo:
   - Posible: No
   - Justificación: El problema no se ajusta naturalmente a un modelo de flujo en red, ya que no hay un concepto claro de fuente, sumidero o capacidades de aristas.

4. Búsqueda Binaria:
   - Posible: No directamente
   - Justificación: Aunque la búsqueda binaria podría usarse como parte de la solución (por ejemplo, para encontrar el costo óptimo), no es la técnica principal para resolver este problema.

5. NP:
   - Posible: No parece ser NP-completo
   - Justificación: Existe un algoritmo de tiempo polinomial (programación dinámica) que puede resolver este problema eficientemente.

Hint para encontrar la respuesta:
Considere usar una técnica de barrido (sweep line) junto con programación dinámica. Ordene los eventos (bordes de los rectángulos negros) de izquierda a derecha y mantenga un estado que represente las regiones negras en cada columna. Use programación dinámica para calcular el costo mínimo de blanquear cada región a medida que avanza.

## El Laberinto

En tiempos antiguos, esos cuando los edificios se derrumbaban por mal tiempo y la conexión mágica era muy lenta, los héroes del reino se aventuraban en el legendario laberinto, un intrincado entramado de pasillos, cada uno custodiado por una bestia mágica. Los pasillos sólo podían caminarse en un sentido pues un viento muy fuerte no te dejaba regresar. Se decía que las criaturas del laberinto, uniendo sus fuerzas mágicas (garras y eso), habían creado ciclos dentro de este, atrapando a cualquiera que entrara a ellos en una especie de montaña rusa sin final en la que un monstruo se reía de ti cada vez que le pasabas por al lado, una locura.

El joven héroe Carlos, se enfrentaba a una prueba única: desmantelar los ciclos eternos y liberar los pasillos del laberinto para que su gente pudiera cruzarlo sin caer en los bucles infinitos de burla y depravación.

Cada vez que el héroe asesinaba cruelmente (no importa porque somos los buenos) a la criatura que cuidaba una un camino, este se rompía y desaparecía. Orión era fuerte, pero no tanto, debía optimizar bien a cuántos monstruos enfrentarse. Ayude al héroe encontrando la mínima cantidad de monstruos que debe matar para eliminar todas las montañas rusas de burla y depravación.

Análisis del problema:

1. Programación Dinámica:
   - Posible: No
   - Justificación: Este problema no presenta una estructura de subproblemas superpuestos o subestructura óptima clara que se pueda aprovechar con programación dinámica.

2. Greedy (Voraz):
   - Posible: No
   - Justificación: Las decisiones localmente óptimas no garantizan una solución globalmente óptima en este caso, ya que eliminar un ciclo puede afectar a otros de manera compleja.

3. Flujo:
   - Posible: No directamente
   - Justificación: Aunque el problema involucra un grafo dirigido, no se ajusta naturalmente a un problema de flujo máximo o mínimo.

4. Búsqueda Binaria:
   - Posible: No
   - Justificación: El problema no implica buscar un valor específico en un rango ordenado, que es donde la búsqueda binaria sería aplicable.

5. NP:
   - Posible: Sí, es un problema NP-difícil
   - Justificación: Este problema es una variante del problema del conjunto de retroalimentación de arcos (Feedback Arc Set), que es conocido por ser NP-difícil.

Hint para encontrar la respuesta:
El problema se puede modelar como un grafo dirigido donde los vértices son las intersecciones del laberinto y las aristas son los pasillos custodiados por monstruos. El objetivo es encontrar el conjunto mínimo de aristas cuya eliminación hace que el grafo sea acíclico. Esto es equivalente al problema del conjunto de retroalimentación de arcos mínimo (Minimum Feedback Arc Set). 

Aunque el problema es NP-difícil, para instancias pequeñas o medianas, se pueden usar técnicas como:
1. Programación lineal entera (ILP)
2. Algoritmos de aproximación
3. Heurísticas basadas en DFS para identificar y romper ciclos
4. Algoritmos de fuerza bruta con poda para instancias muy pequeñas

Para instancias grandes, se recomienda usar algoritmos de aproximación o heurísticas que, aunque no garanticen la solución óptima, puedan proporcionar una buena solución en un tiempo razonable.

## El profe

Jorge es profesor de programación. En sus ratos libres, le gusta divertirse con las estadísticas de sus pobres estudiantes reprobados. Los estudiantes están separados en $n$ grupos. Casualmente, este año, todos los estudiantes reprobaron alguno de los dos exámenes finales: $P$ (POO) y $R$ (Recursividad).

Esta tarde, Jorge decide entretenerse separando a los estudiantes suspensos en conjuntos de tamaño $k$ que cumplan lo siguiente: En un mismo conjunto, todos los estudiantes son del mismo grupo $i$ ($1 \leq i \leq n$) o suspendieron por el mismo examen $P$ o $R$.

Conociendo el grupo y la prueba suspendida de cada estudiante, y el tamaño de los conjuntos, ayude a Jorge a saber cuántos conjuntos de estudiantes suspensos puede formar.

Análisis del problema:

1. Programación Dinámica:
   - Posible: Sí
   - Justificación: Este problema puede resolverse utilizando programación dinámica, ya que podemos construir la solución a partir de subproblemas más pequeños (por ejemplo, calculando el número de conjuntos para subconjuntos de estudiantes).

2. Greedy (Voraz):
   - Posible: No
   - Justificación: Un enfoque voraz no garantizaría la solución óptima, ya que las decisiones locales podrían no llevar al máximo número de conjuntos posibles.

3. Flujo:
   - Posible: No
   - Justificación: Este problema no se ajusta naturalmente a un modelo de flujo en red, ya que no estamos buscando un flujo máximo o mínimo entre nodos.

4. Búsqueda Binaria:
   - Posible: No directamente
   - Justificación: Aunque la búsqueda binaria podría usarse como parte de la solución (por ejemplo, para encontrar el número óptimo de conjuntos), no es la técnica principal para resolver este problema.

5. NP:
   - Posible: No parece ser NP-completo
   - Justificación: Existe un algoritmo de tiempo polinomial (programación dinámica) que puede resolver este problema eficientemente.

Hint para encontrar la respuesta:
Considere usar programación dinámica. Puede crear una tabla DP donde DP[i][j][l] representa el número de conjuntos que se pueden formar usando los primeros i estudiantes, j conjuntos del mismo grupo, y l conjuntos del mismo examen. Actualice esta tabla iterativamente, considerando para cada estudiante si formará parte de un conjunto existente o iniciará uno nuevo, ya sea por grupo o por examen suspendido.
