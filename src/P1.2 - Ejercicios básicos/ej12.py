peso = float(input("Introduce tu peso(Kg): "))
estatura = float(input("Introduce tu estatura(Mts): "))

imc = round(peso / (estatura * estatura), 2)

print(f"Tu índice de masa corporal es {imc}")