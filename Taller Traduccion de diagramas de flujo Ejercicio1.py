def MCD(a,b):

    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
print("El MCD es", MCD(a, b))
