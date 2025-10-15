'''
Trabajo de Amedeo Sandrucci, Danielle Berghege, y Sofia Yanes Sanchez
'''

# nivel 1
personas = [("Ana", "Martínez"), ("Juan", "Pérez"), ("Sofía", "Gómez"), ("Luis", "Fernández")]

def generar_password(personas):
    resultados = []  # creando lista vacia 
    for persona in personas:
        # concetanando: persona[0][0] es el primer elemento del tuple y el primer caracter de la lista, persona[1] es el segundo el del tuple (el apellido)
        resultados.append(persona[0][0].lower() + persona[1].upper())  
    return resultados
print(generar_password(personas))

password_1 = ""  # una cadena vacia para poder modificarla
for el in generar_password(personas):
    password_1 += el  # concatenando todos los elementos de la lista generada para obtener la contrasena
# print(password_1) 


# nivel 2
lista = [45, 12, 78, 3, 56, 91, 18]  # contenidos del archivo
with open("datos.txt", "w") as archivo:  # creando un archivo llamado datos.txt q podemos modificar
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

mayores = procesar_archivo("datos.txt")  # la funcion devuelve la lista de numeros >50
promedio = sum(mayores)/len(mayores)  # tomamos los elementos de esta lista y encontramos su promedio suma/#elementos, tmb se puede hacer con np.mean(mayores)
print(f"El promedio es {promedio}")

cadena_promedio = str(promedio)
password_2 = cadena_promedio[::-1]
# print(password_2)


# nivel 3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(17)  # para q cada vez q se corre el codigo tenemos la misma lista (para el punto 4)

arreglo = np.zeros((100,))  # creando un array vacio con 100 elementos
for i in range(len(arreglo)):  
    arreglo[i] = np.random.randint(0, 11)  # randint genera numeros [,) entonces ponemos hasta 11

masq5 = []  # creando una lista vacia para guardar los valores
for el in arreglo:  # para cada numero en el arreglo
    if el >= 5:  # si este numero >= lo anadimos a la lista q creamos masq5
        masq5.append(el)

# creando el hisograma
plt.hist(masq5, bins=10)  # con 10 intervalos
plt.xlabel("Numeros entre 5 y 10")  # dandole titulos al grafico
plt.ylabel("Frecuencia de numeros")
plt.title("Distribucion de numeros aleatorios")
plt.show()

def clave_final(valores):
    valor_max = str(np.max(valores))  # como valores es una lista, podemos encontrar el valor maximo con max() y lo convertimos en string
    num_el = str(len(valores))  # el numero de elementos filtrados es lo largo de la lista q los contiene (valores)
    return valor_max + "-" + num_el  # concatenamos el valor maximo con un guion medio y el numero de elementos filtrados
password_3 = clave_final(masq5)  # como entrada a la funcion utilizamos la lista de valores filtrados >=5
print(f"La contrasena final es {password_3}")