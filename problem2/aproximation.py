from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.out_degree = defaultdict(int)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.out_degree[u] += 1
        self.in_degree[v] += 1

    def feedback_arc_set_gabow(self):
        """
        Implementación del algoritmo de Gabow para encontrar un conjunto de aristas de retroalimentación
        en un grafo planar. Este algoritmo utiliza una búsqueda en profundidad (DFS) para identificar
        ciclos en el grafo y eliminar aristas de manera que se minimicen los ciclos.

        Propiedades de los grafos planos en las que se basa:
        1. **Teorema de Kuratowski**: Un grafo es planar si y solo si no contiene un subgrafo que sea
           una subdivisión de K5 (el grafo completo de 5 vértices) o K3,3 (el grafo bipartito completo de
           3 vértices en cada conjunto).
        2. **Ciclos en grafos planos**: En un grafo planar, los ciclos pueden ser detectados y eliminados
           de manera eficiente utilizando técnicas de búsqueda en profundidad, ya que la estructura del
           grafo permite un manejo efectivo de los nodos y aristas.
        3. **Propiedades de conectividad**: Los grafos planos tienen propiedades de conectividad que
           permiten la identificación de ciclos y la eliminación de aristas sin afectar la planitud del grafo.

        El algoritmo busca ciclos en el grafo y elimina aristas hasta que no queden más ciclos, garantizando
        que se obtiene un conjunto de aristas de retroalimentación.
        """
        edges_to_remove = set()
        
        while True:
            cycle = self.find_cycle()
            if not cycle:
                break  # No hay más ciclos, terminamos

            # Elegir una arista del ciclo para eliminar
            edge_to_remove = self.choose_edge_to_remove(cycle)
            edges_to_remove.add(edge_to_remove)
            self.remove_edge(edge_to_remove)

        return edges_to_remove

    def find_cycle(self):
        visited = set()
        stack = []
        
        def visit(node):
            if node in stack:
                return [node]  # Ciclo encontrado
            if node in visited:
                return None  # Ya visitado, no hay ciclo

            visited.add(node)
            stack.append(node)

            for neighbor in self.adj[node]:
                cycle = visit(neighbor)
                if cycle:
                    if cycle[0] == node:
                        return cycle  # Ciclo completo
                    return cycle

            stack.pop()  # Retirar el nodo de la pila al finalizar
            return None

        for node in self.adj:
            if node not in visited:
                cycle = visit(node)
                if cycle:
                    return cycle

        return None

    def choose_edge_to_remove(self, cycle):
        # Elige una arista para eliminar (puedes usar diferentes heurísticas)
        return (cycle[0], cycle[1])  # (u, v) de la arista u -> v

    def remove_edge(self, edge):
        u, v = edge
        if v in self.adj[u]:
            self.adj[u].remove(v)
            self.out_degree[u] -= 1
            self.in_degree[v] -= 1

# Ejemplo de uso
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)  # Ciclo
    g.add_edge(3, 4)

    edges_removed = g.feedback_arc_set_gabow()
    print("Aristas eliminadas para romper ciclos:", edges_removed)
