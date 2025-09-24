'''
NIVEL 1: Trabajo de Amedeo Sandrucci, Danielle Berghege, y Sofia Yanes Sanchez
'''

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
print(f"Contrasena para nivel 2: {password_1}") 
