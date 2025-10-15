'''
NIVEL 2: Trabajo de Amedeo Sandrucci, Danielle Berghege, y Sofia Yanes Sanchez
'''

lista = [45, 12, 78, 3, 56, 91, 18]  # contenidos del archivo
with open("parcial_g17\datos.txt", "w") as archivo:  # creando un archivo llamado datos.txt q podemos modificar
    for num in lista:  # para cada elemento de la lista
        archivo.write(str(num) + "\n")  # anadimos el elemento y un caracter \n para tenerlos en lineas separadas

def procesar_archivo(nombre_archivo):
    contenidos = []  # creando una lista vacia para guardar el contenido del archivo
    with open(nombre_archivo, "r") as archivo:  # abriendo el archivo en modo read
        lines = archivo.readlines()  # lines es una lista con el contenido de cada linea de archivo como elemento
        for line in lines:  # para cada elemento (basicamente, cada numero del archivo)
            contenidos.append(int(line[:-1]))  # anadimos el numero del archivo como int y quitamos el \n pq descartamos el caracter final

    mayores = []  # creando una lista vacia para guardar los valores > 50
    for el in contenidos:  # para cada numero en nuestra lista con los contenidos del archivo
        if el > 50:  # si el numero cumple con esta condicion
            mayores.append(el)  # la ajuntamos a la lista

    return mayores

mayores = procesar_archivo("parcial_g17\datos.txt")  # la funcion devuelve la lista de numeros >50
promedio = sum(mayores)/len(mayores)  # tomamos los elementos de esta lista y encontramos su promedio suma/#elementos, tmb se puede hacer con np.mean(mayores)
print(f"El promedio es {promedio}")

password_2 = str(promedio)[::-1]  # convertiendo en string y despues invertiendo la cadena pq tomamos un paso en la direccion al revez con el -1
print(f"Contrasena para nivel 3: {password_2}") 
