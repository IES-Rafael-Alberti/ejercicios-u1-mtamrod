precio_producto = input("Introduce el precio del producto con 2 decimales: ")

lista_precio = []
pos_producto = precio_producto.find(".")
lista_precio.append(precio_producto[0:pos_producto])
lista_precio.append(precio_producto[pos_producto+1:])

print(f"Son {lista_precio[0]} euros y {lista_precio[1]} centimos")

