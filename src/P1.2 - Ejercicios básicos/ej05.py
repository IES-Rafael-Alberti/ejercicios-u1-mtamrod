impNoIva = float(input("Introduce el importe del articulo sin IVA: "))
impIva = float(0)
iva = float(0)

print("1. 21%")
print("2. 10%")
print("3. 4%")
tipoIva = int(input("Introduce el tipo de IVA: "))

while (tipoIva != 1 and tipoIva !=2 and tipoIva !=3):
    tipoIva = int(input("Introduce el tipo de IVA: "))

if (tipoIva == 1):
    iva = 0.21 * impNoIva 
elif (tipoIva == 2):
    iva = 0.1 * impNoIva 
else:
    iva = 0.04 * impNoIva 

impIva = impNoIva + iva

print(f"El precio final es {impIva}€")