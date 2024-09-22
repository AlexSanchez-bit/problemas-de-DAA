# Implementación de SimpleFAS
def simple_fas(graph, permutation):
    L = []  # Arcos donde u < v según la permutación
    R = []  # Arcos donde u > v según la permutación
    n = len(permutation)
    
    # Construcción de los subgrafos L y R
    for u in range(n):
        for v in range(n):
            if u != v and graph[u][v] == 1:  # Si hay arco de u a v
                if permutation.index(u) < permutation.index(v):
                    L.append((u, v))
                else:
                    R.append((u, v))
    
    # Devolvemos el tamaño del conjunto de arcos de retroalimentación
    return len(graph) - max(len(L), len(R))

# Grafo de ejemplo
graph = [
    [0, 1, 0, 1],  # Nodo 0
    [0, 0, 1, 0],  # Nodo 1
    [0, 0, 0, 1],  # Nodo 2
    [0, 0, 0, 0]   # Nodo 3
]

# Permutación de ejemplo (similar a la entrada del texto)
permutation = [0, 1, 2, 3]

# Ejecutamos el algoritmo SimpleFAS
result = simple_fas(graph, permutation)

# Imprimimos el resultado
print(f"Tamaño del conjunto de arcos de retroalimentación: {result}")
