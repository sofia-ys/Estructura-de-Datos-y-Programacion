import numpy as np
import matplotlib.pyplot as plt

def ejercicio1():
    matriz = np.zeros((3, 10))
    matriz[1, :] = 1
    matriz[2, :] = 5
    print(matriz)

def ejercicio2():
    # matriz = np.zeros((15,))
    # for i in range(len(matriz)):
    #     matriz[i] = np.random.normal()
    matriz = np.random.normal(size=15)
    print(matriz)

def ejercicio3():
    matriz = np.zeros((3, 4))
    for i in range(matriz.shape[0]):  # how many rows aka 0th dimension
        print(f"Fila {i}")
        for j in range(matriz.shape[1]):  # shape[1] columns aka 1st dimension
            print(f"Elemento {i},{j}")

def ejercicio4():
    matriz = np.array([[1, 2], [3, 4]])
    inverso = np.linalg.inv(matriz)
    print(inverso)

def ejercicio5():
    ciudades = ["Bristol", "Cardiff", "Bath", "Liverpool", "Glasgow", 
                "Edinburgh", "Leeds", "Reading", "Swansea", "Manchester"]
    poblaciones = [617280, 447287, 94782, 864122, 591620, 464990, 
                   455123, 318014, 300352, 395415]
    
    plt.scatter(ciudades, poblaciones)
    plt.xticks(rotation=45)
    plt.show()
    plt.bar(ciudades, poblaciones)
    plt.xticks(rotation=45)
    plt.show()
