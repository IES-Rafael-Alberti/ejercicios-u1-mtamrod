"""Escribir un programa que pregunte el nombre de un producto, su precio 
y un número de unidades y muestre por pantalla una cadena con el nombre del 
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

producto_compra = input("Introduce el producto que quiere comprar: ")
precio_compra = float(input("Introduce el precio del producto: "))
cantidad_compra = input("Introduce el numero de unidades compradas: ")

precio_compra = round(precio_compra, 2)
cont_precio = len(str(precio_compra)) - 1
cont_precio = 6 - cont_precio

for i in range (0, cont_precio):


print(cont_precio)

#print(f"{producto_compra} | {round(precio_compra, 2)} | {cantidad_compra}")