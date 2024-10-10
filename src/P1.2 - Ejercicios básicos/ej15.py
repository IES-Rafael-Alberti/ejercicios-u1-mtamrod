año_interes = 0.04

deposito = float(input("Introduce la cantidad a ingresar: "))

for i in range (0, 3):
    deposito = round(deposito + (deposito * 0.04), 2)

    match i:
        case 0:
            print(deposito)
        case 1:
            print(deposito)
        case 2:
            print(deposito)
    
        
