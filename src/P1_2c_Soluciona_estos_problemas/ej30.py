"""Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10"""

#Modelo usando listas (Antes de conseguir sacarlo sin listas)
numero_inicio = int(input("Introduce un número: "))
incremento = int(input("Introduce un incremento: "))
total_serie = int(input("Introduce un total de la serie: "))
serie = []

while incremento <= 0 or total_serie <= 0:
    print("**ERROR**")
    incremento = int(input("Introduce un incremento: "))
    total_serie = int(input("Introduce un total de la serie: "))

for i in range(numero_inicio, total_serie + 1, incremento):
    if numero_inicio == i:
        serie.append(str(i))
        serie.append("-")
    elif total_serie == i:
        serie.append("-")
        serie.append(str(i))
        del serie[-3]
    else:
        serie.append(str(i))
        serie.append("..")
if i!= total_serie:
    del serie[-3:]
    serie.append("-")
    serie.append(str(i))
    
serie = "".join(serie)
print(f"SERIE => {serie}")

#Modelo sin usar listas (Conseguí verle el sentido a la lógica y lo terminé bien)
numero_inicio = int(input("Introduce un número: "))
incremento = int(input("Introduce un incremento: "))
total_serie = int(input("Introduce un total de la serie: "))
serie = ""

while incremento <= 0 or total_serie <= 0:
    print("**ERROR**")
    incremento = int(input("Introduce un incremento: "))
    total_serie = int(input("Introduce un total de la serie: "))

for i in range(numero_inicio, total_serie + 1, incremento):
    if numero_inicio == i:
        serie += str(i) + "-"
    elif total_serie == i:
        serie = serie[:-2:] 
        serie += "-" + str(i)
    else:
        serie += str(i) + ".."
if i!= total_serie:
    cant = -4 - len(str(i))
    serie = serie[:cant:]
    serie += "-" + str(i)

print(f"SERIE => {serie}")