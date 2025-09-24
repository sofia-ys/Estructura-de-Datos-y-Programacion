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