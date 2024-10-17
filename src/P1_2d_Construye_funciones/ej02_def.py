def inputs():
    horas = int(input("Escribe las horas de trabajo: "))
    precio = float(input("Escribe el precio por hora: "))

    return horas, precio

def operador():
    horas, precio = inputs()
    

    return horas * precio

def main():
    print(f"Importe total: {operador()}€")


if __name__ == "__main__":
    main()