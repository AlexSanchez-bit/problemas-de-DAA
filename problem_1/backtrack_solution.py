from utils.problem1 import crear_matriz,peso_rectangulo,eliminar_rectangulo,restaurar_rectangulo,matriz_esta_vacia

optimal_solution=[]
min_cost = float('inf')
def backtrack(matriz, rectangulos, solution=[], solution_cost=0):
    global optimal_solution
    global min_cost
    # print('Viendo solución:', solution)
    # Caso base: si la matriz está completamente vacía, devolver el costo de la solución
    if matriz_esta_vacia(matriz):
        return sum(peso_rectangulo(rectangulos[r][0],rectangulos[r][1],rectangulos[r][2],rectangulos[r][3]) for r in solution)

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
    global optimal_solution
    global min_cost
    optimal_solution=[]
    min_cost = float('inf')
    # Inicializar el backtracking con el índice 0 y peso acumulado 0
    resp = backtrack(matriz, rectangulos,[],0 )
    print('optimal_solution backtrack: ',optimal_solution,' ',min_cost)
    return resp

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
