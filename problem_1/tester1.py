import random

from problem_1.backtrack_solution import encontrar_peso_minimo
from utils.problem1 import imprimir_matriz,crear_matriz,marcar_rectangulo,peso_rectangulo
from problem_1.greedy_solution import greedy_max_area
from problem_1.new_solition import solution


def generar_array_unico(N, lista_existente):
    while True:
        # Generar coordenadas para la esquina superior izquierda (x1, y1)
        x1, y1 = random.randint(0, N-2), random.randint(0, N-2)
        
        # Generar coordenadas para la esquina inferior derecha (x2, y2)
        # Aseguramos que x2 > x1 (al menos dos filas) y y2 > y1 (al menos dos columnas)
        x2 = random.randint(x1 , N-1)  # Garantiza al menos 2 filas
        y2 = random.randint(y1 , N-1)  # Garantiza al menos 2 columnas
        
        array = (x1, y1, x2, y2)
        
        # Verificar si el array es único en la lista
        if array not in lista_existente:
            return array


def main(N, cantidad_arrays):
    # Crear la matriz NxN inicializada en 0
    matriz = crear_matriz(N)
    
    # Lista donde almacenaremos los arrays
    lista_rectangulos = []
    
    # Generar arrays únicos y añadirlos a la lista
    for _ in range(cantidad_arrays):
        array = generar_array_unico(N, lista_rectangulos)
        lista_rectangulos.append(array)
    
    # Para cada array en la lista de rectángulos, marcar la matriz
    i=1
    for (x1, y1, x2, y2) in lista_rectangulos:
        marcar_rectangulo(matriz, x1, y1, x2, y2,i)
        i+=1
    
    # Imprimir la matriz resultante
    imprimir_matriz(matriz)
    return matriz,lista_rectangulos







# Definir el tamaño de la matriz N y la cantidad de rectángulos a generar
N = 10
import time

test_count=1000
count=0
time_passed=time.time()
algo_mean_time = 0
for _ in range(0,test_count):
    cantidad_arrays = random.randint(1,N)

    matriz,rectangulos = main(N, cantidad_arrays)
    print('matriz inicial')

    rect_copy=rectangulos.copy()
    peso_minimo = encontrar_peso_minimo(matriz,rect_copy )

    rect_copy2= rectangulos.copy()
    auxtime=time.time()
    min_greedy=solution(N, rect_copy2)
    algo_mean_time+=time.time() - auxtime
    print('minimo carlos solution: ',min_greedy)
    print(f"minimo backtrack: {peso_minimo}")

    if min_greedy == peso_minimo:
        count+=1
time_passed = time.time() - time_passed
print('porcentaje de casos pasados: ',count/test_count)
print('tiempo medio de ejecucion (en segundos): ',algo_mean_time/time_passed)


# print('backtrack   ',rect_copy)
# print('greedy   ',rect_copy2)

# for i,rect in enumerate(rectangulos):
#     print(i+1,'---',rect,'----',peso_rectangulo(rect[0],rect[1],rect[2],rect[3]))
# # Encontrar el peso mínimo para vaciar la matriz



# 