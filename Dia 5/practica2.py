# PRACTICA
'''def chequear_3_cifras(lista):
    Posi = 0
    Nega = 0
    for n in lista:
        if n > 0:
            Posi += 1
        else:
            Nega += 1
    if Nega == 0:
        return True
    else:
        return False

resultado = chequear_3_cifras([1,50,502,-5000,-755,600,33,61])
print(resultado)'''
lista_numeros = [100,50,502]
def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(0,1000):
            suma = suma + n
        else:
            pass
    return suma

resultado = suma_menores(lista_numeros)
print(resultado)


def cantidad_pares(lista_numeros):
    nro_par = 0
    for n in lista_numeros:
        if n % 2 == 0:
            nro_par +=1
    return nro_par

resu2 = cantidad_pares(lista_numeros)
print(resu2)