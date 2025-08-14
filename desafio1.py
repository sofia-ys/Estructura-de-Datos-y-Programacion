from math import *
nivel = input("Nivel: ").lower()

# nivel 1
if nivel == "1":
    # 1.
    print("-----------------1.-----------------")
    texto = input("Texto: ")
    output = texto[::-1]  # entire list, starting from back
    print(output)

    # 2.
    print("-----------------2.-----------------")
    palabra = input("Palabra: ")
    vocales = ["a", "i", "u", "e", "o"]  # lista de vocales para comparar
    counter = 0
    for ch in palabra:  # pa cada character en el string palabra
        if ch in vocales:  # si el character esta en la lista
            counter += 1  # si es vocal, +1 to the counter
    print(f"Hay {counter} vocales en {palabra}")

    # 3. 
    print("-----------------3.-----------------")
    frase = input("Frase: ")
    alternadas = ""
    for i, ch in enumerate(frase):
        if i % 2 == 0:  # si es even 
            alternadas += ch.upper()  # convierte en mayuscula
        else:
            alternadas += ch.lower()  # convierte a minuscula
    print(alternadas)

# nivel 2
elif nivel == "2":
    # 4. 
    print("-----------------4.-----------------")
    frase = input("Frase: ").replace(" ", "").lower()  # quitando todos los espacios
    def pali(texto):
        for i in range(ceil(len(texto)/2)):  # solo tenemos que comparar la mitad de las letras
            if texto[i] == texto[-(i + 1)]:  # compara letra en pocision i, y la letra corresponding in opposite side
                continue  # so far so good, continue checking
            else:
                return False  # ya si uno no cuadra, we can immediately return false
        return True  # yayyy!
    print(f"La frase es un palidromo: {pali(frase)}")

    # 5. 
    frase = input("Frase: ").strip()
    espacios = 1  # nunmero de palabras = espacios + 1 
    for ch in frase:
        if ch == " ":
            espacios += 1
    print(f"Hay {espacios} palabras en la frase")

    # 6.
    desplaz = int(input("Desplazamiento: "))
    frase = input("Frase: ").lower()  # lower pq ascii de upper es diferente 
    output = ""  # initialising nuestro output 
    for ch in frase:
        if ch.isalpha():
            output += chr(ord(ch) + desplaz)  # ascii del ch + deplazamiento --> back to character
        else:
            output += ch  # deja los espacios y punctuation tranquis
    print(output)


# nivel 3
elif nivel == "3":
    # 7. 
    texto = input("Texto: ")
    for i in range(1, len(texto) + 1):  # todo length del texto
        print(texto[:i])  # from start until the i index 
    
    # 8.
    frase = input("Frase: ")
    palabras = frase.split()  # agarrando las palabras individuales
    posMasLarga = 0
    masLarga = 0
    for i, palabra in enumerate(palabras):
        if len(palabra) > masLarga:  # si encontramos una mas larga, agarramos su posicion
            posMasLarga = i  
    palabras[posMasLarga] = "*"  # la mas larga la reemplazamos
    output = " ".join(palabras)  # join todos los elementos de la lista con un espacio entre ellos
    print(output)



# # bonus
# elif nivel == "bonus":

else:
    print("No es un nivel válido.")