def operador(n: int):
    while (n < 0):
        print("Número no válido")
        n = int(input("Introduce un número entero positivo: "))

    suma = (n * (n + 1)) / 2

    return int(suma)

def main():
    n = int(input("Introduce un número entero positivo: "))

    print(f"El resultado de la suma es {operador(n)}")


if __name__ == "__main__":
    main()