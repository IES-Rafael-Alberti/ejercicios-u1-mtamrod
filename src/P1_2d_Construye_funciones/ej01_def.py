def input_nombre():
    nombre = input("Introduce tu nombre: ")
    return nombre

def main():
    print (f"Hola, {input_nombre()}.")


if __name__ == "__main__":
    main()