def input_nombre():
    nombre = input("Escribe tu nombre: ")
    return nombre

def main():
    print (f"Hola, {input_nombre()}.")


if __name__ == "__main__":
    main()