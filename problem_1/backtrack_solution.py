from utils.problem1 import crear_matriz,peso_rectangulo,eliminar_rectangulo,restaurar_rectangulo,matriz_esta_vacia,marcar_rectangulo,imprimir_matriz

optimal_solution=[]
min_cost = float('inf')
<<<<<<< HEAD
=======

>>>>>>> dumb_ideas
def backtrack(matriz, rectangulos, solution=[], solution_cost=0):
    # Inicializamos la respuesta como infinito
    response = float('inf')


    for rect in solution:
        x1,y1,x2,y2 = rectangulos[rect]
        eliminar_rectangulo(matriz,x1,y1,x2,y2)

    if matriz_esta_vacia(matriz):
        costo_actual_solution = sum([peso_rectangulo(rectangulos[r][0],rectangulos[r][1],rectangulos[r][2],rectangulos[r][3]) for r in solution])
        response= min(response,costo_actual_solution)

    for rect in solution:
        x1,y1,x2,y2 = rectangulos[rect]
        marcar_rectangulo(matriz,x1,y1,x2,y2,rect+1)

    
    for i, rect in enumerate(rectangulos):
        if i not in solution:
            # Agregamos el índice del rectángulo actual a la solución
            solution.append(i)
            # Llamamos recursivamente con la solución actualizada
            a = backtrack(matriz, rectangulos, solution, solution_cost + peso_rectangulo(rect[0], rect[1], rect[2], rect[3]))
            # Restauramos el estado de la matriz
            solution.pop()
            # Actualizamos la respuesta con el mínimo entre la solución actual y la respuesta
            response = min(response, a)

<<<<<<< HEAD
    for rect in solution:
        x1,y1,x2,y2 = rectangulos[rect]
        eliminar_rectangulo(matriz,x1,y1,x2,y2)


    if matriz_esta_vacia(matriz):
        costo_actual_solution = sum(peso_rectangulo(rectangulos[r][0],rectangulos[r][1],rectangulos[r][2],rectangulos[r][3]) for r in solution)
        # print('subsolucion===')
        # print('costo de la solucion: ',costo_actual_solution)
        # print('rectangulos de la solucion: ',[rectangulos[r] for r in solution])
        # print('matriz resultante')
        # imprimir_matriz(matriz)
        # print('subsolucion===')
        response= min(response,costo_actual_solution)

    for rect in solution:
        x1,y1,x2,y2 = rectangulos[rect]
        marcar_rectangulo(matriz,x1,y1,x2,y2,rect)
=======
>>>>>>> dumb_ideas
    
    return response




def encontrar_peso_minimo(matriz, rectangulos):
    resp = backtrack(matriz, rectangulos,[],0 )
    return resp
<<<<<<< HEAD

=======
>>>>>>> dumb_ideas
