'''def chequear_3_cifras(num):
    return num in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)'''

# EJEMPLO DINAMICO
print('\nEJEMPLO DINAMICO')

def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras([55,9,600])
print(resultado)
