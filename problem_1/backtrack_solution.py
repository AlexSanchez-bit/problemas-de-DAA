from utils.problem1 import crear_matriz,peso_rectangulo,eliminar_rectangulo,restaurar_rectangulo,matriz_esta_vacia

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