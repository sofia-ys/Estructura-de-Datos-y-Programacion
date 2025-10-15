from datetime import datetime
import os
import csv
import random as rnd

def ejercicio1():
    nombre = input("Nombre de archivo: ").strip()
    with open(f"archivos_tp7/{nombre}.txt", "w") as archivo:
        archivo.write(f"{datetime.today()}")

def ejercicio2():
    with open("archivos_tp7/numbers.txt", "w") as archivo:
        archivo.write("5, 4, 2, 1, 3")
        print(os.path.dirname(archivo))

def ejercicio3():
    print(
        "1) Crear nuevo archivo\n" \
        "2) Mostrar el contenido del archivo\n" \
        "3) Agregar un nuevo item al archivo")
    while True: 
        while True:
            try: 
                opcion = int(input("Elija opcion 1, 2, 3: ").strip())
            except ValueError:
                print("Ingresa un numero")
            else:
                if opcion != 1 and opcion != 2 and opcion != 3:
                    print("Solo ingresa 1, 2, o 3")
                else:
                    break

        if opcion == 1:
            nombre_1 = input("Nombre de archivo: ").strip()
            archivo_1 = open(f"archivos_tp7/{nombre_1}.txt", "w")
            archivo_1.close()
        elif opcion == 2:
            nombre_2 = input("Nombre de archivo a leer: ")
            archivo_2 = open(f"archivos_tp7/{nombre_2}.txt", "r")
            archivo_2.close()
        else:
            nombre_3 = input("Nombre de archivo para agregar informacion: ")
            archivo_3 = open(f"archivos_tp7/{nombre_2}.txt", "a")
            archivo_3.close()
    
def ejercicio4():
    nombre = "cuenta"
    header = ["tipo", "transaccion", "importe"]
    tipos = ["ahorros", "corriente", "inversion"]
    transacciones = ["deposito", "extraccion"]
    filas = []

    for i in range(10):
        filas.append(f"{rnd.choice(tipos)}," + f"{rnd.choice(transacciones)}," + f"{rnd.randint(0, 1000)}" + "\n")
    
    with open(f"archivos_tp7/{nombre}.csv", "w") as archivo:
        archivo.write(",".join(header) + "\n")
        for fila in filas: 
            archivo.writelines(fila )

def ejercicio5_a():
    header = ",book,author,year released\n"
    libros = ["To Kill a Mockingbird", "A Brief History of Time", "The Great Gatsby",
              "The Man Who Mistook His Wife for a Hat", "Pride and Prejudice"]
    autores = ["Harper Lee", "Stephen Hawking", "F. Scott Fitzgerald", "Oliver Sacks", "Jane Austen"]
    anos = ["1960", "1988", "1922", "1985", "1813"]

    contenidos = []
    for i in range(5):
        contenidos.append(f"{i},{libros[i]},{autores[i]},{anos[i]}\n")

    with open(f"archivos_tp7/libros.csv", "w") as archivo:
        archivo.write(header)
        for line in contenidos:
            archivo.write(line)

def ejercicio5_b():
    agregar = input("Deseas agrergar una nueva linea de informacion? (Y/N): ").strip().lower()
    if agregar == "y":
        num = int(input("Cuantas lineas nuevas: "))
    
    lib_nuevo = []
    autor_nuevo = []
    ano_nuevo = []
    contenidos = []
    
    for i in range(num):
        print(f"----------Entrada {i + 1}----------")
        lib_nuevo.append(input("Titulo: ").strip())
        autor_nuevo.append(input("Autor: ").strip())
        ano_nuevo.append(input("Ano: ").strip())
        contenidos.append(f"{i},{lib_nuevo[i]},{autor_nuevo[i]},{ano_nuevo[i]}\n")

    with open(f"archivos_tp7/libros.csv", "a") as archivo:
        for line in contenidos:
            archivo.write(line)

def ejercicio5_c():
    ano1 = int(input("Ano de inicio: "))
    ano2 = int(input("Ano de final: "))

    datos = list(csv.reader(open("archivos_tp7/libros.csv")))[1:]
    for libro in datos:
        if ano1 <= int(libro[-1]) <= ano2:
            print(libro)

ejercicio5_c()