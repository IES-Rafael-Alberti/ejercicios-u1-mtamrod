payaso = 112
muñeca = 75

n_payasos = int(input("Introduce el número de payasos: "))
n_muñecas = int(input("Introduce el número de muñecas: "))

peso_pedido = (payaso * n_payasos) + (muñeca * n_muñecas)

print(f"El peso del paquete es de {peso_pedido} gramos")