def calcula_precio(importe, iva):
    if iva < 0 or iva >100:
        iva = 21.0

    importe += (iva/100) * importe

    return f"El precio final del artículo con IVA ({iva:.1f}) es {importe:.1f}€"

def main():
    importe = float(input("Introduce el importe del artículo sin IVA: "))
    iva = float(input("Introduce el IVA del artículo: "))

    print(calcula_precio(importe, iva))


if __name__ == "__main__":
    main()