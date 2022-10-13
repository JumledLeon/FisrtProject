if  10 > 11 :
    print('es correcto')
else:
    print('no es correcto')

mascota = 'loro'
if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
else:
    print('no se que animal tienes')

edad2 = 16
nota = 9
if edad2 < 18:
    print('eres mocoso')
    if nota >= 7:
        print('Aprobado')
    else:
        print('no aprobado')
else:
    print('eres adulto')

edad = 16
tiene_licencia = False
if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad >= 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")