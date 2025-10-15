from math import *
ejercicio = int(input("Ejercicio: "))

# ejercicio 1
if ejercicio == 1:
    print(f"a) {int(exp(2 * log(3)))}")  # e^(2 * ln(3)) = e^(ln(3^2)) = e^2 = 9
    print(f"b) {round(4 * sin(3 * pi /2))}")  # 4 * (-1) = -4
    print(f"c) {abs(log10(.01) * sqrt(25))}")  # |(-2) * 5| = |-10| = 10
    print(f"d) {round(3.21123 * log10(100), 3)}")  # 3.21123 * 2 = 6.42246 = 6.422

# ejercicio 2
elif ejercicio == 2:
    r = 1
    perimetro = 2 * pi * r
    print(f"Perimetro: {perimetro}")

# ejercicio 3
elif ejercicio == 3:
    s = float(input("Lado del cuadrado: "))
    perimetro = 4 * s
    area = s**2
    print(f"Perimetro: {perimetro}")
    print(f"Area : {area:.2f}")  # redondando a 2 decimos

# ejercicio 4
elif ejercicio == 4:
    s1 = float(input("Lado 1 del rectangulo: "))
    s2 = float(input("Lado 2 del rectangulo: "))
    perimetro = 2 * s1 + 2 * s2
    area = s1 * s2
    print(f"Perimetro: {perimetro}")
    print(f"Area : {area:.2f}") 

# ejercicio 5
elif ejercicio == 5:
    b = float(input("Base del triangulo: "))
    h = float(input("Altura del triangulo: "))
    area = 0.5 * b * h
    print(f"Area : {area:.2f}") 

# ejercicio 6
elif ejercicio == 6:
    C = float(input("Cantidad de euros: "))
    x = float(input("Tasa de interes: "))
    n = float(input("Numero de años: "))
    valor = C * (1 + x/100)**n
    print(f"Valor: {valor:.2f}")

# ejercicio 7
elif ejercicio == 7:
    nombre = input("Cual es tu nombre? ")
    nombreBinario = ""
    nombreHexa = ""
    nombreOctal = ""
    for ch in nombre:
        nombreBinario += str(bin(ord(ch)))[2:] + " "
        nombreOctal += str(oct(ord(ch)))[2:] + " "
        nombreHexa += str(hex(ord(ch)))[2:] + " "

    print(f"Binario: {nombreBinario}")
    print(f"Octal: {nombreOctal}")
    print(f"Hexadecimal: {nombreHexa}")

# ejercicio 8
elif ejercicio == 8:
    tasa = {"chelines":8.56 / 100, "dracmas":0.35 / 100, "francos belgas":2.94 / 100, 
            "francos frances": 0.18, "libra":1.38}
    
    cantidadChelines = float(input("Cantidad en chelines: "))
    dolares = cantidadChelines * tasa["chelines"]
    print(f"Cantidad en dolares = {dolares:.2f}")

    cantidadDracmas = float(input("Cantidad en dracmas: "))
    francosFranceses = cantidadDracmas * tasa["dracmas"] / tasa["francos frances"]
    print(f"Cantidad en francos franceses = {francosFranceses:.2f}")

    cantidadDolares = float(input("Cantidad en dolares: "))
    esterlina = cantidadDolares / tasa["libra"]
    francosBelgas = cantidadDolares / tasa["francos belgas"]
    print(f"Cantidad en libra esterlina = {esterlina:.2f}")
    print(f"Cantidad en francos belgas = {francosBelgas:.2f}")

# ejercicio 9
elif ejercicio == 9:
    x = int(input("x: "))
    y = int(input("y: "))
    a = int(input("a: "))
    d = int(input("d: "))
    
    try: 
        ans = (x + y - a) / (d - 1)
    except ZeroDivisionError:
        print("Solucion no existe.") 
    else:
        print(f"x = {ans}")

else:
    print("No es un ejercicio válido.")