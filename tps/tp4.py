import numpy as np

def ejercicio1():
    num = int(input("Numero: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)

def ejercicio2():
    num = int(input("Numero: "))
    for i in range(13):
        print(f"{num} x {i} = {num * i}")

# opcion 1
def ejercicio3_1():
    billetes = [20000, 10000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2]
    cantidad = int(input("Cantidad: "))

    def scan(num, billetes):
        for bill in billetes:
            if num >= bill:  # encontrar el starting point
                rest = num - bill
                return rest, bill

    while cantidad >= billetes[-1]:
        cantidad, bill = scan(cantidad, billetes)
        print(f"1 billete de {bill}")

# opcion 2
def ejercicio3_2():
    billetes = [20000, 10000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2]
    cantidad = int(input("Cantidad: "))

    for bill in billetes:  # solo tenemos q pasar por la lista una vez
        if cantidad >= bill:
            num_bill = cantidad // bill  # cuantos billetes de este tamano necesitamos
            cantidad = cantidad - bill * num_bill 
            if num_bill == 1:
                print(f"{num_bill} billete de {bill}")
            else:
                print(f"{num_bill} billetes de {bill}")

def ejercicio4():
    num = int(input("Numero: "))

    def primo(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(np.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    i = 0
    while True:
        if primo(num + i):
            print(f"El numero primo mas cercano es {num + i}")
            break
        if primo(num - i):
            print(f"El numero primo mas cercano es {num - i}")
            break
        else:
            i += 1

def ejercicio5(n=100):
    secuencia = [0, 1]
    while secuencia[-1] < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    print(secuencia)

def ejercicio6():
    lista = input("Lista: ").split(", ")
    print(lista[-1::-1])

def ejercicio7():
    for i in range(4):
        print(" "*i + "*"*(10-3*i))
    
    print(10*"+")
    for i in range(4):
        print("+" + 8*" " + "+")
    print(10*"+")

def ejercicio8():
    adviniar = 17
    while True:  
        num = int(input("Numero entre 10 y 20: "))
        if num == adviniar:
            print("Ganaste!")
            break
        elif num > adviniar:
            print("Muy alto")
        else:
            print("Muy bajo")