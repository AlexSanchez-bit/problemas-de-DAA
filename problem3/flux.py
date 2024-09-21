from collections import defaultdict, deque

class Grafo:
    def __init__(self):
        self.adj = defaultdict(list)
        self.caps = {}

    def agregar_arista(self, u, v, cap):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Añadir arista inversa para el flujo
        self.caps[(u, v)] = cap
        self.caps[(v, u)] = 0  # La capacidad de la arista inversa es 0

    def bfs(self, s, t, parent):
        visited = set()
        queue = deque([s])
        while queue:
            u = queue.popleft()
            if u == t:
                return True
            for v in self.adj[u]:
                if v not in visited and self.caps[(u, v)] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
                    if v == t:
                        return True
        return False

    def flujo_maximo(self, s, t):
        parent = {}
        max_flow = 0
        
        # Busca caminos aumentantes usando BFS
        while self.bfs(s, t, parent):
            path_flow = float('Inf')
            v = t
            
            # Encuentra el flujo mínimo en el camino encontrado
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.caps[(u, v)])
                v = parent[v]
            
            # Actualiza las capacidades de las aristas y el flujo inverso
            v = t
            while v != s:
                u = parent[v]
                self.caps[(u, v)] -= path_flow
                self.caps[(v, u)] += path_flow
                v = parent[v]
            
            max_flow += path_flow
        
        return max_flow
# Inicia la variable global antes de llamar a la solución