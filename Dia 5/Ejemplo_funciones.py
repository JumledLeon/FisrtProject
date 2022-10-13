precios_cafe = [('capuchino',3.5),('Expreso',3.2),('Moka',2.9)]
print('\nEJEMPLO ##')
for elemento in precios_cafe:
    print(elemento)

print('\nEJEMPLO ##')
for cafe,precio in precios_cafe:
    print(precio*0.45)

print('\nEJEMPLO ##')
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return(cafe_mas_caro,precio_mayor)
cafe, precio = cafe_mas_caro(precios_cafe)
print(cafe_mas_caro(precios_cafe))
print(f'El cafe mas caro es {cafe} cuyo precio es {precio}')