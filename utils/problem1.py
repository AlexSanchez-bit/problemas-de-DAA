import copy

def crear_matriz(N):
    # Crear una matriz NxN inicializada en 0
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    return matriz

def peso_rectangulo(x1, y1, x2, y2):
    # Calcula el peso del rectángulo (mínimo entre ancho y alto)
    alto = abs(x2 - x1) + 1
    ancho = abs(y2 - y1) + 1
    return min(alto, ancho)

def eliminar_rectangulo(matriz, x1, y1, x2, y2):
    # Elimina el rectángulo de la matriz (cambia de 1 a 0 en las posiciones ocupadas)
    todos_ceros = True
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

def rect_a_contenido(matrix, rect1, rectangles):
    x1, y1, x2, y2 = rect1
    
    # Recorremos las posiciones dentro de rect1
    black_tiles=0
    covered_black_tiles=0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            # Verificamos si la posición en la matriz tiene valor 1
            if matrix[i][j] != 0:
                black_tiles+=1
                # Verificamos si está dentro de los límites de rect2
                for rect2 in rectangles:
                    a1,b1,a2,b2 = rect2
                    if  (a1 <= i <= a2 and b1 <= j <= b2):
                        covered_black_tiles+=1
                        break  # Si alguna posición no está contenida, retornamos False
    
    return black_tiles == covered_black_tiles  # Si todas las posiciones con 1 están contenidas, retornamos True

def covered_area(matriz,x1,y1,x2,y2):
    marks=0
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if(matriz[x][y]!=0):
                marks+=1
    return marks


def area_rect(matriz,rectangulos,x1,y1,x2,y2):
    marks=0#calculando la cantidad de espacios seleccionables solo por el rectangulo
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if(matriz[x][y]!=0):
                contained=False
                for x_1,y_1,x_2,y_2 in rectangulos:
                    if x1 == x_1 and x2 == x_2 and y1== y_1 and y2== y_2:
                        continue
                    if x_1<= x <= x_2 and y_1<=y<=y_2   :
                        contained=True
                        break
                if not contained:
                    marks+=1

    return marks




def matriz_esta_vacia(matriz):
    # Verifica si la matriz está completamente vacía (llena de ceros)
    for fila in matriz:
        if any([elem != 0 for elem in fila]):
            return False
    return True


def marcar_rectangulo(matriz, x1, y1, x2, y2,num=1):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            matriz[i][j] = num

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))