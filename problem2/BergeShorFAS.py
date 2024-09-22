import random

# Función para calcular in-degree y out-degree de un nodo en el grafo
def degree(graph, vertex):
    in_degree = sum([graph[u][vertex] for u in range(len(graph))])
    out_degree = sum(graph[vertex])
    return in_degree, out_degree

# Implementación de BergerShorFAS
def berger_shor_fas(graph):
    n = len(graph)
    vertices = list(range(n))
    
    # Elegimos una permutación aleatoria de los vértices
    permutation = random.sample(vertices, n)
    
    F = []  # Conjunto de arcos de retroalimentación
    
    for v in permutation:
        in_degree, out_degree = degree(graph, v)
        
        if in_degree > out_degree:
            # Añadimos los arcos entrantes al conjunto de retroalimentación
            F.extend([(u, v) for u in range(n) if graph[u][v] == 1])
        else:
            # Añadimos los arcos salientes al conjunto de retroalimentación
            F.extend([(v, u) for u in range(n) if graph[v][u] == 1])
        
        # "Eliminamos" el vértice al eliminar sus arcos del grafo
        for u in range(n):
            graph[u][v] = 0
            graph[v][u] = 0

    return F

# Grafo de ejemplo (matriz de adyacencia)
graph = [
    [0, 1, 0, 1, 0],  # Nodo 0
    [0, 0, 1, 0, 0],  # Nodo 1
    [0, 0, 0, 1, 0],  # Nodo 2
    [0, 0, 0, 0, 1],  # Nodo 3
    [1, 0, 0, 0, 0]   # Nodo 4
]

# Ejecutamos el algoritmo BergerShorFAS
feedback_arc_set = berger_shor_fas(graph)

# Imprimimos el resultado
print(f"Conjunto de arcos de retroalimentación: {feedback_arc_set}")
