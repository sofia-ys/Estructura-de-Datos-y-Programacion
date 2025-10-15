def ejercicio1():
    edad1 = int(input("Eddad de persona 1: "))
    edad2 = int(input("Eddad de persona 2: "))
    if edad1 > edad2:
        print("Persona 1 es mayor.")
    elif edad1 < edad2:
        print("Persona 2 es mayor.")
    else:
        print("Ambas personas tiene la misma edad")

def ejercicio2():
    ch = input("Caracter: ").strip()
    if ch == "(" or ch == ")":
        print("Es parentesis")

def ejercicio3():
    numero = int(input("Numero: "))
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

def ejercicio4():
    numero = int(input("Numero: "))
    if (numero/2) % 2 != 0 and (numero/2).is_integer():
        print(f"{numero} es el doble de {int(numero/2)}, que es impar")

def ejercicio5():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    if num2 == num1**2:
        print("El 2do es el cuadrado del 1ero")
    elif num2 < num1**2:
        print("El 2do es < que el cuadrado del primero")
    else:
        print("El 2do es > que el cuadrado del 1ero")

def ejercicio6():
    C = float(input("Capital: "))
    x = float(input("Interes: "))
    n = float(input("Numero de anos: "))
    if x > 0: 
        C_final = C * (1 + x/100)**n
        print(f"La capital final es {C_final:.2f} euros")

def ejercicio7():
    numero = float(input("Ingrese un numero entre 10 y 20 (inclusivo): "))
    if 10 <= numero <= 20:
        print("Gracias a usted")
    else:
        print("Respuesta incorrecta")

def ejercicio8():
    color = input("Ingrese tu color favorito: ").strip().lower()
    if color == "rojo":
        print("Me gusta el rojo tambien")
    else:
        print("No me gusta su color favorito, prefiero el rojo")

def ejercicio9():
    lluvia = input("Esta lloviendo? ").strip().lower()
    if lluvia == "si":
        viento = input("Esta ventoso? ").strip().lower()
        if viento == "si":
            print("Memaiado viento para un paraguas")
        else:
            print("Lleve un paraguas")
    else:
        print("Disfrute su dia")

def ejercicio10():
    edad = int(input("Edad: "))
    if edad >= 18:
        print("Ud puede votar")
    elif edad == 17:
        print("Ud puede aprender a manejar")
    elif edad == 16:
        print("Ud puede comprar un billete de loteria")
    else: 
        print("Ud puede jugar a verdad o consecuencia")

def ejercicio11():
    num = int(input("Tipee un numero: "))
    if num < 10:
        print("Memasiado bajo")
    elif 10 <= num <= 20:
        print("Correcto")
    else:
        print("Demasiado alto")