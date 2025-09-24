def ejercicio2(lista):
    ordenada = sorted(lista)
    listafinal = []
    i = 0
    while True:
        count = ordenada.count(ordenada[i])
        listafinal.append([ordenada[i], count])
        i += count
        if i == len(ordenada):
            break
    
    print(listafinal)
