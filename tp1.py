from math import * 

ejercicio = int(input("Ejercicio: "))

# ejercicio 1
if ejercicio == 1:
    print(f"a) {2 + 3 + 1 + 2}")
    print(f"b) {2 + 3 * 1 + 2 }")
    print(f"c) {(2 + 3) * 1 + 2}")
    print(f"d) {(2 + 3) * (1 + 2)}")
    print(f"e) {+---6}")
    print(f"f) {-+-+6}")
    print(f"g) {-3 / 2 - 1}")
    print(f"h) {-3 // 2 - 1}")

# ejercicio 2
elif ejercicio == 2:
    print(f"a) {2 + (3 * (6/2))}")
    print(f"b) {(4 + 6)/(2 + 3)}")
    print(f"c) {(4/2)**5}")
    print(f"d) {(4/2)**(4 + 2**2)}")
    print(f"e) {(-3)**2}")
    print(f"f) {-(3**2)}")


# ejercicio 3
elif ejercicio == 3:
    print(f"a) {0xf + 0o17 + 0b1111 + 15}")  # hexadecimal 15 + octal 15 + binary 15 + base10 15
    print(f"b) {0xffff + 0b1}")  # hexadecimal 15 * (16^3 + 16^2 + 16^1 + 16^0) + binary 2^0

# ejercicio 4
elif ejercicio == 4:
    x = 10
    x = x * 10  # x = 10 * 10 = 100
    print(f"x = {x}")

# ejercicio 5
elif ejercicio == 5:
    x = 1.1
    ans = x**4 + x**3 + 2 * x**2 - x
    print(f"x = {ans}")

# ejercicio 6
elif ejercicio == 6:
    z = 2
    print(f"z = {z}")
    z += 2  # 4
    print(f"z = {z}")
    z += 2 - 2  # 4 + (2 - 2) = 4
    print(f"z = {z}")
    z *= 2  # 4 * 2 = 8
    print(f"z = {z}")
    z *= 1 + 1  # 8 * (1 + 1) = 16
    print(f"z = {z}")
    z //= 2  # 16 // 2 = 8
    print(f"z = {z}")
    z %= 3  # 8 % 3 = 2
    print(f"z = {z}")
    z /= 3 - 1  # 2 / (3 - 1) = 1
    print(f"z = {z}")
    z -= 2 + 1  # 1 - (2 + 1) = -2
    print(f"z = {z}")
    z -= 2  # -2 - 2 = -4
    print(f"z = {z}")
    z **= 3  # (-4)**3 = -64
    print(f"z = {z}")
    
# ejercicio 7
elif ejercicio == 7:
    a = "b"
    print(a + "b")  # bb
    print(a + "a")  # ba
    print(a * 2 + "b" * 3)  # bb + bbb = bbbbb
    print(2 * (a + "b"))  # 2 * bb = bbbb
    print(2 * ("a" + "b"))  # 2 * ab = abab

# ejercicio 8
elif ejercicio == 8:
    print("a" * 3 + "/*" * 5 + 2 * "abc" + "+")  # aaa/*/*/*/*/*abcabc+ 
    palindromo = "abcba"
    print((4 * "<" + palindromo + ">" * 4) * 2)  # <<<<abcba>>>><<<<abcba>>>>
    subcadena = "=" + "-" * 3 + "="  # =---=
    print("10" * 5 + 4 * subcadena)  # 1010101010=---==---==---==---=
    print(2 * "12" + "." + "3" * 3 + "e-" + 4 * "76")  # 1212.333e-76767676

# ejercicio 9
elif ejercicio == 9:
    print(f"a) {4 * "%" + 3 * "./" + 2 * "<->"}")  # %%%%%./././<-><->
    print(f"b) {2 * (3 * "(@)" + 6 * "=")}")  # (@)(@)(@)======(@)(@)(@)======
    print(f"c) {3 * "asdf" + 7 * "=-" + 7 * "?" + 2 * "asdf"}")  # asdfasdfasdf=-=-=-=-=-=-=-???????asdfasdf
    print(f"d) {2 * (9 * "." + 2 * (5 * "*" + 2 * "-"))}")  # .........*****--*****--.........*****--*****--

# ejercicio 10
elif ejercicio == 10:
    print(str(2.1) + str(1.2))  # 2.11.2 (type:str)
    print(int(str(2) + str(3)))  # 23 (type:int)
    print(str(int(12.3)) + "0")  # 12 + 0 = 120 (type:str)
    print(int("2" + "3"))  # 23 (type:int)
    print(str(2 + 3))  # 5 (type:str)
    print(str(int(2.1) + float(3)))  # 2 + 3.0 = 5.0 (type:str)

# ejercicio 11
elif ejercicio == 11:
    print(f"a) {int(exp(2 * log(3)))}")  # e^(2 * ln(3)) = e^(ln(3^2)) = e^2 = 9
    print(f"b) {round(4 * sin(3 * pi /2))}")  # 4 * (-1) = -4
    print(f"c) {abs(log10(.01) * sqrt(25))}")  # |(-2) * 5| = |-10| = 10
    print(f"d) {round(3.21123 * log10(100), 3)}")  # 3.21123 * 2 = 6.42246 = 6.422

# ejercicio 12
elif ejercicio == 12:
    nombre = input("Cual es tu nombre? ")
    nombreBinario = ""
    nombreHexa = ""
    for ch in nombre:
        nombreBinario += str(bin(ord(ch)))[2:] + " "
        nombreHexa += str(hex(ord(ch)))[2:] + " "

    print(f"Binario: {nombreBinario}")
    print(f"Hexadecimal: {nombreHexa}")

else:
    print("No es un ejercicio válido.")