'''utilizando lista'''
# contactos = ["Danielle", "Amedeo", "Sofia", "Victoria", "Agnes"]

# def agregar_contacto(nombre):
#     contactos.append(nombre)
#     return contactos

# def ver_contactos():
#     print(contactos)

# def buscar_contacto(nombre):
#     return nombre in contactos

'''utilizando un archivo'''
def agregar_contacto(nombre):
    with open("contactos.txt", "a") as fout:
        fout.write(f"\n{nombre}")    

def ver_contactos():
    with open("contactos.txt", "r") as fin:
        for line in fin.readlines():
            print(line)

def buscar_contacto(nombre):
    with open("contactos.txt", "r") as fin:
        for line in fin.readlines():
            if line.strip() == nombre:
                return True
            else:
                continue
    return False

print("Menu:\n 1: Agregar contacto\n 2. Ver contactos\n 3. Buscar contacto\n 4. Salir")

while True:
    opcion = input("Opcion: ").strip()
    if opcion == "1":
        agregar = input("Nombre: ").strip()
        agregar_contacto(agregar)
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        buscar = input("Nombre: ").strip()
        print(buscar_contacto(buscar))
    elif opcion == "4":
        break
    else:
        print("Ingresa un numero de 1-4")