import math
from utils.problem1 import marcar_rectangulo, matriz_esta_vacia, eliminar_rectangulo, peso_rectangulo, rectangulo_borrado, rect_a_contenido, imprimir_matriz, area_rect

def single_black_degree(matrix, rect):
    x1, y1, x2, y2 = rect
    deg = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            deg += 1 if matrix[i][j] != 0 else 0
    return deg

def greedy_max_area(matriz, rectangulos: list):
    response = []
    
    # Ordenar rectángulos primero por área de mayor a menor y luego por coste de menor a mayor en caso de empate
    rectangulos.sort(key=lambda rect: (-area_rect(matriz,rect[0], rect[1], rect[2], rect[3]), peso_rectangulo(rect[0], rect[1], rect[2], rect[3])))

    costo = 0
    while not matriz_esta_vacia(matriz):
        # Seleccionar el primer rectángulo, ya que están ordenados por área descendente y menor coste en caso de empate
        biggest_rect = rectangulos.pop(0)
        
        x1, y1, x2, y2 = biggest_rect
        
        # Ignorar rectángulos que ya han sido eliminados completamente
        if rectangulo_borrado(matriz, x1, y1, x2, y2):
            continue

        # Ignorar rectángulos que están completamente contenidos dentro de otros ya seleccionados
        if rect_a_contenido(matriz, biggest_rect, rectangulos):
            continue
        
        # Eliminar el rectángulo de la matriz y añadirlo a la solución
        eliminar_rectangulo(matriz, x1, y1, x2, y2)
        response.append(biggest_rect)
        costo += peso_rectangulo(x1, y1, x2, y2)
        rectangulos.sort(key=lambda rect: (-area_rect(matriz,rect[0], rect[1], rect[2], rect[3]), peso_rectangulo(rect[0], rect[1], rect[2], rect[3])))
    
    print('max_area_greedy_optimal solution: ', response)
    return costo
