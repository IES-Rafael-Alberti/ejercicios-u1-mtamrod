"""Escribir un programa que pregunte por consola por los productos 
de una cesta de la compra, separados por comas, y muestre por pantalla 
cada uno de los productos en una línea distinta."""

lista_compra = input("Introduce los productos de tu cesta de la compra separados por comas: ")
 
lista_compra = lista_compra.split(", ")
productos_lista = lista_compra.__len__()

for i in range (0, productos_lista):
    print(f"- {lista_compra[i].capitalize()}")