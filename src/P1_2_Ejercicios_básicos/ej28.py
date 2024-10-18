def calculo_area(lado1, lado2, lado3):
    # Semiperímetro
    perimetro = (lado1 + lado2 + lado3) / 2
    
    # Formula de Herón
    area = float((perimetro * (perimetro - lado1) * (perimetro - lado2) * (perimetro - lado3)))
    
    return area

def main():
    lado1 = float(input("Introduce el primer lado: "))
    lado2 = float(input("Introduce el segundo lado: "))
    lado3 = float(input("Introduce el tercer lado: "))

    print(f"{calculo_area(lado1, lado2, lado3):.2f}")

if __name__ == "__main__":
    main()