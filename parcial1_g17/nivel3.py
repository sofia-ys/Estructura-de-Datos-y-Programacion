'''
NIVEL 3: Trabajo de Amedeo Sandrucci, Danielle Berghege, y Sofia Yanes Sanchez
'''

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