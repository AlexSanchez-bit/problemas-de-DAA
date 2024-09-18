import copy

def crear_matriz(N):
    # Crear una matriz NxN inicializada en 0
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    return matriz

def peso_rectangulo(x1, y1, x2, y2):
    # Calcula el peso del rectángulo (mínimo entre ancho y alto)
    alto = (x2 - x1) + 1
    ancho = (y2 - y1) + 1
    return min(alto, ancho)

def eliminar_rectangulo(matriz, x1, y1, x2, y2):
    # Elimina el rectángulo de la matriz (cambia de 1 a 0 en las posiciones ocupadas)
    all_zeroes=True
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            matriz[i][j] = 0
    
def rectangulo_borrado(matrix,x1,y1,x2,y2):
    all_zeroes=True
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if matrix[i][j] != 0:
                all_zeroes=False
    return all_zeroes


def restaurar_rectangulo(matriz, x1, y1, x2, y2):
    # Restaura el rectángulo en la matriz (cambia de 0 a 1 en las posiciones ocupadas)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            matriz[i][j] = 1

def rect_a_contenido(rect1, rect2):
    x1, y1, x2, y2 = rect1
    a1, b1, a2, b2 = rect2
    
    # Verificar que las esquinas de rect1 están dentro de rect2
    return a1 <= x1 and b1 <= y1 and a2 >= x2 and b2 >= y2



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