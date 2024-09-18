import random

def crear_matriz(N):
    # Crear una matriz NxN inicializada en 0
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    return matriz

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

def marcar_rectangulo(matriz, x1, y1, x2, y2,num=1):
    # Marcar el rectángulo con 1s
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            matriz[i][j] = num

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

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





import copy

def peso_rectangulo(x1, y1, x2, y2):
    # Calcula el peso del rectángulo (mínimo entre ancho y alto)
    alto = x2 - x1 + 1
    ancho = y2 - y1 + 1
    return min(alto, ancho)

def eliminar_rectangulo(matriz, x1, y1, x2, y2):
    # Elimina el rectángulo de la matriz (cambia de 1 a 0 en las posiciones ocupadas)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            matriz[i][j] = 0

def restaurar_rectangulo(matriz, x1, y1, x2, y2):
    # Restaura el rectángulo en la matriz (cambia de 0 a 1 en las posiciones ocupadas)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            matriz[i][j] = 1

def matriz_esta_vacia(matriz):
    # Verifica si la matriz está completamente vacía (llena de ceros)
    for fila in matriz:
        if any(fila):  # Si hay algún 1 en la fila, la matriz no está vacía
            return False
    return True

def backtrack(matriz, rectangulos, idx, peso_acumulado):
    # Caso base: si la matriz está completamente vacía, devolver el peso acumulado
    if matriz_esta_vacia(matriz):
        return peso_acumulado

    # Si hemos procesado todos los rectángulos y no vaciamos la matriz, devolvemos un valor grande (invalido)
    if idx >= len(rectangulos):
        return float('inf')

    # Obtener el rectángulo actual
    x1, y1, x2, y2 = rectangulos[idx]
    
    # Opción 1: No usar este rectángulo (ir al siguiente rectángulo)
    peso_no_usar = backtrack(matriz, rectangulos, idx + 1, peso_acumulado)

    # Opción 2: Usar este rectángulo (eliminarlo de la matriz)
    # Primero, calculamos el peso del rectángulo actual
    peso_actual = peso_rectangulo(x1, y1, x2, y2)

    # Luego, eliminamos el rectángulo de la matriz
    eliminar_rectangulo(matriz, x1, y1, x2, y2)
    # Realizamos la llamada recursiva para procesar el siguiente rectángulo
    peso_usar = backtrack(matriz, rectangulos, idx + 1, peso_acumulado + peso_actual)

    # Finalmente, restauramos el rectángulo (backtracking: restaurar el estado original de la matriz)
    restaurar_rectangulo(matriz, x1, y1, x2, y2)

    # Retornamos el mínimo entre usar y no usar el rectángulo actual
    return min(peso_no_usar, peso_usar)

def encontrar_peso_minimo(matriz, rectangulos):
    # Inicializar el backtracking con el índice 0 y peso acumulado 0
    return backtrack(matriz, rectangulos, 0, 0)

# Definir el tamaño de la matriz N y la cantidad de rectángulos a generar
N = 10
cantidad_arrays = random.randint(1,N)

matriz,rectangulos = main(N, cantidad_arrays)
print('matriz inicial')

for i,rect in enumerate(rectangulos):
    print(i+1,'---',rect,'----',peso_rectangulo(rect[0],rect[1],rect[2],rect[3]))
# Encontrar el peso mínimo para vaciar la matriz
peso_minimo = encontrar_peso_minimo(matriz, rectangulos)

print(f"El peso mínimo para vaciar la matriz es: {peso_minimo}")

# 