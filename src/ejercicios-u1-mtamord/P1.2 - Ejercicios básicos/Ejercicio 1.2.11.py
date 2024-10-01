n = int(input("Introduce un número entero positivo: "))

while (n < 0):
    print("Número no válido")
    n = int(input("Introduce un número entero positivo: "))

suma = (n * (n + 1)) / 2

print(suma)