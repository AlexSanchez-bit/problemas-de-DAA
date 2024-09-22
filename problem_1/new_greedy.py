from utils.problem1 import marcar_rectangulo,matriz_esta_vacia,eliminar_rectangulo,peso_rectangulo, rectangulo_borrado,rect_a_contenido,imprimir_matriz

def cuantos_negros(matriz, rectangulo):
    negros = 0
    for x in range(rectangulo[0], rectangulo[2] + 1):
        for y in range(rectangulo[1], rectangulo[3] + 1):
            if not matriz[x][y] == 0:
                negros += 1
    return negros

def greedy_max_area_upgrade(matriz, rectangulos: list):
    response=[]
    # rectangulos.sort(key = lambda rect: ((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1)),reverse=True)
    
    rectangulos_with_area = [(rect, ((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1))) for rect in rectangulos]
    rectangulos_with_area.sort(key = lambda rect: rect[1], reverse=True)
    # print([(rect,((abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1))) for rect in rectangulos])

    costo=0
    while(not matriz_esta_vacia(matriz) ):
        biggest_rect =rectangulos_with_area.pop(0)[0]
        #si ya fue borrado totalmente por el resto se ignora
        x1,y1,x2,y2 = biggest_rect
        if rectangulo_borrado(matriz,x1,y1,x2,y2):
            continue

        
        x1,y1,x2,y2 = biggest_rect
        eliminar_rectangulo(matriz,x1,y1,x2,y2)
        new_rectangulos_with_area = []
        for (rect, area) in rectangulos_with_area:
            negros = cuantos_negros(matriz, rect)
            new_rectangulos_with_area.append((rect, negros))
        new_rectangulos_with_area.sort(key = lambda rect: rect[1], reverse=True)
        rectangulos_with_area = new_rectangulos_with_area
        response.append(biggest_rect)
        costo += peso_rectangulo(x1,y1,x2,y2)
    
    print(response)
    return costo