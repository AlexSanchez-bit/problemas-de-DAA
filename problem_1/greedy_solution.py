import math

def greedy_max_area(matriz, rectangulos: list):
    print(rectangulos)
    rectangulos.sort(key = lambda rect: ((abs(rect[0] - rect[3]) + 1) * (abs(rect[1] - rect[2]) + 1)))

    print(rectangulos)