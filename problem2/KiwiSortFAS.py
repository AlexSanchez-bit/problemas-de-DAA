import random

def has_arc(graph, start_vertex, end_vertex):
    """Verifica si hay un arco de start_vertex a end_vertex en el grafo."""
    return end_vertex in graph[start_vertex]

def kwik_sort_fas(graph, vertex_arrangement, low_index, high_index):
    """Implementa el algoritmo KwikSortFAS."""
    if low_index < high_index:
        less_than_pivot, greater_than_pivot, current_index = low_index, high_index, low_index
        pivot_vertex = vertex_arrangement[random.randint(low_index, high_index)]

        while current_index <= greater_than_pivot:
            if has_arc(graph, vertex_arrangement[current_index], pivot_vertex):
                vertex_arrangement[less_than_pivot], vertex_arrangement[current_index] = vertex_arrangement[current_index], vertex_arrangement[less_than_pivot]
                less_than_pivot += 1
                current_index += 1
            elif has_arc(graph, pivot_vertex, vertex_arrangement[current_index]):
                vertex_arrangement[current_index], vertex_arrangement[greater_than_pivot] = vertex_arrangement[greater_than_pivot], vertex_arrangement[current_index]
                greater_than_pivot -= 1
            else:
                current_index += 1

        kwik_sort_fas(graph, vertex_arrangement, low_index, less_than_pivot - 1)
        if less_than_pivot < greater_than_pivot:
            kwik_sort_fas(graph, vertex_arrangement, less_than_pivot, greater_than_pivot)
        kwik_sort_fas(graph, vertex_arrangement, greater_than_pivot + 1, high_index)

def extract_feedback_arc_set(graph, vertex_arrangement):
    """Extrae un conjunto de arcos de retroalimentación a partir de un arreglo lineal."""
    feedback_arcs = []
    for i in range(len(vertex_arrangement) - 1):
        for j in range(i + 1, len(vertex_arrangement)):
            if has_arc(graph, vertex_arrangement[j], vertex_arrangement[i]):
                feedback_arcs.append((vertex_arrangement[j], vertex_arrangement[i]))
    return feedback_arcs

# Caso de uso
if __name__ == "__main__":
    # Definimos un grafo dirigido como un diccionario
    directed_graph = {
        1: [2, 3],
        2: [3],
        3: [4],
        4: [],
        5: [3, 4],
        6: [5],
        7: [6, 8],
        8: []
    }
    
    # Arreglo inicial de vértices
    initial_vertex_arrangement = list(directed_graph.keys())
    
    # Ejecutamos KwikSortFAS
    random.shuffle(initial_vertex_arrangement)  # Mezclamos el arreglo inicial
    kwik_sort_fas(directed_graph, initial_vertex_arrangement, 0, len(initial_vertex_arrangement) - 1)
    
    # Extraemos el conjunto de arcos de retroalimentación
    feedback_arcs = extract_feedback_arc_set(directed_graph, initial_vertex_arrangement)
    
    print("Arreglo lineal después de KwikSortFAS:", initial_vertex_arrangement)
    print("Conjunto de arcos de retroalimentación:", feedback_arcs)
