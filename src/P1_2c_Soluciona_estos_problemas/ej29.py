"""Realiza un programa en Python que solicite un nombre y una edad.

Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir"."""

nombre = input("Introduce un nombre: ")
edad = int(input("Introduce una edad: "))

if len(nombre) == 0:
    nombre = "Desconocido"

while edad < 0 or edad > 125:
    print("Edad no válida")
    edad = int(input("Introduce una edad válida: "))

diferencia_edad = 125 - edad

print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {diferencia_edad} años por cumplir")