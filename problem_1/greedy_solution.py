import math
from utils.problem1 import marcar_rectangulo,matriz_esta_vacia,eliminar_rectangulo,peso_rectangulo

def greedy_max_area(matriz, rectangulos: list):
    print(rectangulos)
    rectangulos.sort(key = lambda rect: ((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1)),reverse=True)
    
    print([(rect,((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1))) for rect in rectangulos])


    costo=0
    while(not matriz_esta_vacia(matriz)):
        biggest_rect =rectangulos.pop(0)
        x1,y1,x2,y2 = biggest_rect
        eliminar_rectangulo(matriz,x1,y1,x2,y2)
        costo += peso_rectangulo(x1,y1,x2,y2)
    return costo

