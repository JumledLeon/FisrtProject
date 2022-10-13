nombre = input("¿Cual es tu nombre?: ")
ventas = input("¿Cuanto vendiste?: ")
ventas = float(ventas)
print(type(ventas))
comision = round(ventas * 0.13,2)

print(f"Ok {nombre}. Este mes ganaste {comision}")