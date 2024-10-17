BARRA_PAN = float(3.49)
descuento = float(0.6)

barra_no_dia = int(input("Introduce las barras vendidas que no son del día: "))
coste_no_fresco = BARRA_PAN + (BARRA_PAN * descuento)
print(f"Barra de pan: {BARRA_PAN}€\nDescuento por no fresco: 60%\nCoste de barras no frescas: {round(coste_no_fresco, 2)}€")