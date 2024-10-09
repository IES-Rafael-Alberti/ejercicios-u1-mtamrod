"""Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10"""

numero_inicio = int(input("Introduce un número: "))
incremento = int(input("Introduce un incremento: "))
total_serie = int(input("Introduce un total de la serie: "))
serie = ""

while incremento <= 0 or total_serie <= 0:
    print("**ERROR**")
    incremento = int(input("Introduce un incremento: "))
    total_serie = int(input("Introduce un total de la serie: "))

for i in range(numero_inicio, total_serie + 1):
    if i == numero_inicio or i == total_serie -1:
        serie += str(i) + "-"
    elif i == total_serie:
        serie += str(i)
    else:
        serie += str(i) + ".."

print(f"SERIE => {serie}")