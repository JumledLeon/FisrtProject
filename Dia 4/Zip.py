nombres = ['Ana','Hugo','Valeria','Leo']
edades = [65,29,42,55]
ciudades = ['Lima','Madrid','Mexico']
combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nmb, edad, ciudad in combinados:
    print(f'{nmb} tiene {edad} y vive en {ciudad}')

print('\nPRACTICA 1')
marcas = ['Adida','Rebook','Nike']
productos = ['Zapatilla','bolso','Reloj']
mi_zip = list(zip(marcas,productos))
print(mi_zip)
print(zip(marcas,productos))