import copy

def crear_matriz(N):
    # Crear una matriz NxN inicializada en 0
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    return matriz

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
        if any([elem != 0 for elem in fila]):  # Si hay algún 1 en la fila, la matriz no está vacía
            return False
    return True


def marcar_rectangulo(matriz, x1, y1, x2, y2,num=1):
    # Marcar el rectángulo con 1s
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            matriz[i][j] = num

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))