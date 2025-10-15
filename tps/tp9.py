def f_to_c(temp_f):
    return (temp_f - 32) * (5/9)

def ejercicio2(cadena):
    return cadena[0].islower()

def esPalindromo(cadena):
    for i in range(len(cadena)):
        if cadena[i].lower() != cadena[-(i + 1)].lower():
            return False
    return True

def resursiveSumIt(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + resursiveSumIt(nums[1:])