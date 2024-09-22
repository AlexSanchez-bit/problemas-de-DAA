
from collections import defaultdict, deque

def greedyFAS(graph):
    # Inicialización de las secuencias
    s1 = deque()  # Secuencia para las fuentes
    s2 = deque()  # Secuencia para los sumideros

    # Definir los grados de entrada y salida
    outdegree = defaultdict(int)
    indegree = defaultdict(int)

    # Calcular los grados de entrada y salida para cada nodo
    for u in graph:
        for v in graph[u]:
            outdegree[u] += 1
            indegree[v] += 1

    def get_delta(u):
        return outdegree[u] - indegree[u]

    # Lista de nodos en el grafo
    nodes = set(graph.keys())

    # Mientras queden nodos en el grafo
    while nodes:
        # Eliminar sumideros
        sinks = {u for u in nodes if outdegree[u] == 0}
        while sinks:
            u = sinks.pop()
            s2.appendleft(u)  # Prependemos a s2
            nodes.remove(u)
            # Actualizar grados de entrada y salida
            for v in graph[u]:
                indegree[v] -= 1
                if outdegree[v] == 0:
                    sinks.add(v)

        # Eliminar fuentes
        sources = {u for u in nodes if indegree[u] == 0}
        while sources:
            u = sources.pop()
            s1.append(u)  # Añadimos a s1
            nodes.remove(u)
            # Actualizar grados de entrada y salida
            for v in graph[u]:
                outdegree[v] -= 1
                if indegree[v] == 0:
                    sources.add(v)

        # Si no hay fuentes ni sumideros, eliminar el nodo con mayor δ(u)
        if nodes:
            u = max(nodes, key=get_delta)
            s1.append(u)
            nodes.remove(u)
            # Actualizar grados de entrada y salida
            for v in graph[u]:
                indegree[v] -= 1

    # Retornar la secuencia s = s1 + s2
    return list(s1) + list(s2)

# Ejemplo de uso
graph = {
    1: [2],
    2: [3],
    3: [4],
    4: [],
    5: [6],
    6: [7],
    7: [8],
    8: [5]
}

result = greedyFAS(graph)
print("Secuencia resultante:", result)
