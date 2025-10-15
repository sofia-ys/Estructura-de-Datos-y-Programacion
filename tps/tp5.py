import numpy as np
import random as rand

def ejercicio1():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[-1, 0], [0, 1], [1, 1]])
    print(A @ B)

def ejercicio2():
    A = np.array([[1, 2, 3], [5, 5, 6]])
    row_sums = []
    col_sums = []

    for row in A:
        row_sums.append(sum(row))
    for i in range(len(A[0])):
        col_sums.append(sum(A[:, i]))

    comun = set(row_sums).intersection(set(col_sums))

    if comun != 0:
        print("La suma de una(s) fila(s) es igual a una(s) columna(s)")

def ejercicio3():
    dim = int(input("Dimension de matriz: "))
    matriz = np.zeros((dim, dim))

    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            matriz[i, j] += rand.randint(-100, 100)
    print(matriz)

def ejercicio4():
    precios = [50, 75, 46, 22, 80, 65, 8]
    print(f"Precio menor: {min(precios)}")
    print(f"Precio mayor: {max(precios)}")