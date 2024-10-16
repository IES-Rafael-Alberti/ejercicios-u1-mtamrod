"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
funcione cuando el día o el mes se introduzcan con un solo carácter."""

fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

fecha_nacimiento = fecha_nacimiento.split("/")

print(f"Naciste el {fecha_nacimiento[0]} de {fecha_nacimiento[1]} del {fecha_nacimiento[2]}")
