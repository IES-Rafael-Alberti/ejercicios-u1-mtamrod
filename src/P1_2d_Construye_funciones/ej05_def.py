def inputs():
    imp_no_iva = float(input("Introduce el importe del articulo sin IVA: "))
    imp_iva = float(0)
    iva = float(0)
    
    return imp_no_iva, imp_iva, iva

def user_menu():
    print("1. 21%")
    print("2. 10%")
    print("3. 4%")
    tipoIva = int(input("Introduce el tipo de IVA: "))

    while (tipoIva != 1 and tipoIva !=2 and tipoIva !=3):
        tipoIva = int(input("Introduce el tipo de IVA: "))

    return tipoIva

def operador():
    imp_no_iva, imp_iva, iva = inputs()
    tipoIva = user_menu()

    if (tipoIva == 1):
        iva = 0.21 * imp_no_iva 
    elif (tipoIva == 2):
        iva = 0.1 * imp_no_iva 
    else:
        iva = 0.04 * imp_no_iva 

    imp_iva = imp_no_iva + iva

    print(f"El precio final es {imp_iva}€")

def main():
    operador()


if __name__ == "__main__":
    main()


"""
def user_menu():
    print("1. 21%")
    print("2. 10%")
    print("3. 4%")

def operador(imp_no_iva, imp_iva, iva, tipoIva):
    if (tipoIva == 1):
        iva = 0.21 * imp_no_iva 
    elif (tipoIva == 2):
        iva = 0.1 * imp_no_iva 
    else:
        iva = 0.04 * imp_no_iva 

    imp_iva = imp_no_iva + iva

    print(f"El precio final es {imp_iva}€")

def main():
    imp_no_iva = float(input("Introduce el importe del articulo sin IVA: "))
    imp_iva = float(0)
    iva = float(0)
    
    user_menu()
    tipoIva = int(input("Introduce el tipo de IVA: "))
    
    operador(imp_no_iva, imp_iva, iva, tipoIva)


if __name__ == "__main__":
    main()
"""