#floyd warshall cicles verification 
def has_cycle_floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] < graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    if i == j and graph[i][j] >= 0:
                        return True
    return False



#verificando ciclos con DFS
def has_cycle_dfs(graph):
    n = len(graph)
    visited = [False] * n
    stack = []

    def dfs(node):
        visited[node] = True
        stack.append(node)
        for neighbor in range(n):
            if graph[node][neighbor]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif neighbor in stack:
                    return True
        stack.pop()
        return False

    for node in range(n):
        if not visited[node]:
            if dfs(node):
                return True
    return False