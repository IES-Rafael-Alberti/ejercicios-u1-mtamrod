"""Escribir un programa que pregunte el nombre de un producto, su precio 
y un número de unidades y muestre por pantalla una cadena con el nombre del 
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

producto_compra = input("Introduce el producto que quiere comprar: ")
precio_compra = float(input("Introduce el precio del producto: "))
cantidad_compra = int(input("Introduce el numero de unidades compradas: "))

precio_compra = round(precio_compra, 2)
cont_precio = len(str(precio_compra)) - 1

match (cont_precio):
    case 3:
        #0.00
        cont_precio = f"00000{precio_compra}"
    case 4:
        #00.00
        cont_precio = f"0000{precio_compra}"
    case 5:
        #000.00
        cont_precio = f"000{precio_compra}"
    case 6:
        #0000.00
        cont_precio = f"00{precio_compra}"
    case 7:
        #00000.00
        cont_precio = f"0{precio_compra}"


cont_cantidad = len(str(cantidad_compra))

match (cont_cantidad):
    case 1:
        #00X
        cont_cantidad = f"00{cantidad_compra}"
    case 2:
        #0XX
        cont_cantidad = f"00{cantidad_compra}"


precio_total = cantidad_compra * precio_compra
cont_total = len(str(precio_total)) - 1

match (cont_total):
    case 3:
        cont_total = f"0000000{precio_total}"
    case 4:
        cont_total = f"000000{precio_total}"
    case 5:
        cont_total = f"00000{precio_total}"
    case 6:
        cont_total = f"0000{precio_total}"
    case 7:
        cont_total = f"000{precio_total}"
    case 8:
        cont_total = f"00{precio_total}"
    case 9:
        cont_total = f"0{precio_total}"

print(f"{producto_compra} | {cont_precio} | {cont_cantidad} | {cont_total}")