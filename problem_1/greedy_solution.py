import math
from utils.problem1 import marcar_rectangulo,matriz_esta_vacia,eliminar_rectangulo,peso_rectangulo, rectangulo_borrado,rect_a_contenido,imprimir_matriz

def greedy_max_area(matriz, rectangulos: list):
    print(rectangulos)
    rectangulos.sort(key = lambda rect: ((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1)),reverse=False)
    
    print([(rect,((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1))) for rect in rectangulos])


    costo=0
    while(not matriz_esta_vacia(matriz) ):

        biggest_rect =rectangulos.pop(0)
        #si ya fue borrado totalmente por el resto se ignora
        x1,y1,x2,y2 = biggest_rect
        if rectangulo_borrado(matriz,x1,y1,x2,y2):
            continue

        #si ya hay un rectangulo que lo contiene completamente se ignora
        if any(rect_a_contenido(biggest_rect, r) for r in rectangulos):
            continue
        
        rectangulos = list(filter(lambda rect:not rectangulo_borrado(matriz,rect[0],rect[1],rect[2],rect[3]),rectangulos))
        x1,y1,x2,y2 = biggest_rect
        eliminar_rectangulo(matriz,x1,y1,x2,y2)
        costo += peso_rectangulo(x1,y1,x2,y2)
    
    print('matriz final')
    imprimir_matriz(matriz)

    return costo

