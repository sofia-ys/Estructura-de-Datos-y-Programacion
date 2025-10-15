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
            output += chr((ord(ch) - ord('a') + desplaz) % 26 + ord('a'))  # ascii del ch + deplazamiento --> back to character (pero con %26 pq queremos que it wraps around)
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
            masLarga = len(palabra)  # actualizar cual es la mas larga
            posMasLarga = i  
    palabras[posMasLarga] = "*"  # la mas larga la reemplazamos
    output = " ".join(palabras)  # join todos los elementos de la lista con un espacio entre ellos
    print(output)

    # 9.
    palabras = input("Palabras, separadas con un ',': ").replace(" ", "").split(",")  # dividir las por el ","
    output = ""
    masCorta = 0
    if len(palabras[1]) < len(palabras[0]):
        masCorta = 1  # si palabra en pos 1 es mascorta que palabra pos 0
    for i in range(len(palabras[masCorta])):
        output += palabras[0][i] + palabras[1][i]
    output += " " + palabras[masCorta - 1][i + 1:]  # mascorta -1 pq queremos de la maslarga
    print(output)

    # 10.
    frase = input("Frase: ")
    analisis = ""
    for ch in frase:
        if ch.isalpha():  # solo las letras queremos ver
            analisis += ch
    print(f"Numero total de letras: {len(analisis)}")
    vocales = ["a", "i", "u", "e", "o"]
    counter = 0
    for ch in analisis:
        if ch in vocales:
            counter += 1
    print(f"Porcentaje de vocales: {counter/len(analisis)*100:.1f}%")
    print(f"Porcentaje de consonantes: {(1 - counter/len(analisis))*100:.1f}%")

# bonus
elif nivel == "bonus":
    '''esto es un vignere cypher, que es parecido al ceaser cypher per utiliza una palabra como una clave, asi hay un "shift" que no es 
    constante, y es mas deficil de decifrar! es posible decifrar un texto, o tambien encryptlo'''

    def getKey(key):  # key will be an indexed version of keys (like keys[0])
        shift = []
        for ch in key:  # for each character in this one word string
            shift.append(ord(ch) - ord('a'))  # the shift is the ascii order of the number minus the capital since all keys are capslock
        return shift

    def cypher(message, key, cypherStatus):
        decryptMessage = ""  # final decrypted message
        idx = 0  # initialising our index position in the message
        key = getKey(key)  # the key we're using put into its shifts 

        if cypherStatus == "1":
            key = [-1*x for x in key]  # when descrypting we want to shift it back so we want negative shifts so just each num * -1

        for ch in message:
            if ch.isalpha():  # if we have a letter we want to decrypt it
                if ch.islower():  # checking the starting point of the alphabet for lower vs capital
                    caseShift = ord('a')
                else:
                    caseShift = ord('A')

                shift = key[idx % len(key)]  # so the actual key that applies just depends on how many letters we've gone over in the message so far
                ch = chr(((ord(ch) - caseShift + shift) % 26) + caseShift)  # converting character in message with shift 
                decryptMessage += ch  # constructing our new message
                idx = idx + 1  # whenever  we have a letter we want to make sure we're moving our index point by one
        
            else:  # if we don't have a letter we leave it as is
                decryptMessage += ch

        return decryptMessage

    clave = input("Clave: ").lower()
    message = input("Mensaje: ")  # el texto que vamos a cyper or decypher
    cypherStatus = input("Selecciona descifrar 1 o cifrar 2: ")
    decryptMessage = cypher(message, clave, cypherStatus)  # using cypher function
    if cypherStatus == "1":
        print("--------------------Mensaje decifrado:--------------------")
        print(decryptMessage)
    elif cypherStatus == "2":
        print("--------------------Mensaje cifrado:--------------------")
        print(decryptMessage)
    else:
        print("No es una opcion válida.")

else:
    print("No es un nivel válido.")