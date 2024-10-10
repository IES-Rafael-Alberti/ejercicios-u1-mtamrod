"""Escribir un programa que pregunte el nombre de un producto, su precio 
y un número de unidades y muestre por pantalla una cadena con el nombre del 
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

producto_compra = input("Introduce el producto que quiere comprar: ")
precio_compra = float(input("Introduce el precio del producto: "))
cantidad_compra = int(input("Introduce el numero de unidades compradas: "))

precio_total = cantidad_compra * precio_compra

print(f"{producto_compra} | {precio_compra:09.2f} | {cantidad_compra:03} | {precio_total:011.2f}")