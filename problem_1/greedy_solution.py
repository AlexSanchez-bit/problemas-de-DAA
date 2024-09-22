import math
from utils.problem1 import marcar_rectangulo,matriz_esta_vacia,eliminar_rectangulo,peso_rectangulo, rectangulo_borrado,rect_a_contenido,imprimir_matriz,area_rect

def single_black_degree(matrix,rect):
    x1,y1,x2,y2 = rect
    deg=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            deg+= 1 if matrix[i][j]!=0 else 0
    return deg


def greedy_max_area(matriz, rectangulos: list):
    response=[]
    rectangulos.sort(key = lambda rect: area_rect(rect[0],rect[1],rect[2],rect[3]),reverse=True)
    
    # print([(rect,((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1))) for rect in rectangulos])


    costo=0
    while(not matriz_esta_vacia(matriz) ):
        biggest_rect =rectangulos.pop(0)
        #si ya fue borrado totalmente por el resto se ignora
        x1,y1,x2,y2 = biggest_rect
        if rectangulo_borrado(matriz,x1,y1,x2,y2):
            continue

        #si ya hay un rectangulo o varios que lo contiene completamente se ignora
        if rect_a_contenido(matriz,biggest_rect,rectangulos):
            continue
        
        x1,y1,x2,y2 = biggest_rect
        eliminar_rectangulo(matriz,x1,y1,x2,y2)
        response.append(biggest_rect)
        costo += peso_rectangulo(x1,y1,x2,y2)
    

    print('max_area_greedy_optimal solution: ',response)
    _cost =0
    return costo


