from utils.problem1 import crear_matriz,peso_rectangulo,eliminar_rectangulo,restaurar_rectangulo,matriz_esta_vacia

def backtrack(matriz, rectangulos, solution=[], solution_cost=0):
    print('Viendo solución:', solution)
    
    # Caso base: si la matriz está completamente vacía, devolver el costo de la solución
    if matriz_esta_vacia(matriz):
        return solution_cost

    # Inicializamos la respuesta como infinito
    response = float('inf')
    
    for i, rect in enumerate(rectangulos):
        if i not in solution:
            # Agregamos el índice del rectángulo actual a la solución
            solution.append(i)
            
            # Eliminamos el rectángulo actual de la matriz
            eliminar_rectangulo(matriz, rect[0], rect[1], rect[2], rect[3])
            
            # Llamamos recursivamente con la solución actualizada
            a = backtrack(matriz, rectangulos, solution, solution_cost + peso_rectangulo(rect[0], rect[1], rect[2], rect[3]))
            
            # Restauramos el estado de la matriz
            restaurar_rectangulo(matriz, rect[0], rect[1], rect[2], rect[3])
            
            # Eliminamos el índice del rectángulo actual de la solución
            solution.pop()
            
            # Actualizamos la respuesta con el mínimo entre la solución actual y la respuesta
            response = min(response, a)
    
    return response



def encontrar_peso_minimo(matriz, rectangulos):
    # Inicializar el backtracking con el índice 0 y peso acumulado 0
    return backtrack(matriz, rectangulos )

def backtrack_max(list):
    length = len(list)
    result = []

    for i in range(length):
        for j in range(length):
            for k in range(length):
                result.append(list[i:j] + [list[k]])
            k = 0
        j = 0
    

    return result

print('max estuvo aqui: ',backtrack_max([1,2,3]))