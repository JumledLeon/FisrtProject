#EJERCICIO 1
print('Ejercicio # 1')

def devolver_distintos(a,b,c):
    suma = a+b+c
    lista = [a,b,c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(1,2,0))

#EJERCICIO 2
print('\nEjercicio # 2')

def ordena_palabra(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)
    #print(mi_set)

    lista = list(mi_set)
    lista.sort()
    return  lista

print(ordena_palabra('arrebatarse'))

#EJERCICIO 3
print('\nEjercicio # 3')

def validador(*args):
    contador = 0
    for arg in args:
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else :
            contador += 1
    return False

print(validador(0,1,0,0,3,4,0,1))

#EJERCICIO 4
print('\nEjercicio # 4')

def contar_primos(num):
    primos = []
    iteracion = 3

    if num < 2:
        return 0

    while iteracion <= num:
        for n in range(3,iteracion,2):
            if iteracion %n == 0:
                iteracion +=2
                break
        else:
                primos.append(iteracion)
                iteracion +=2
    print(primos)
    return len(primos)

print(f'Longitud es {contar_primos(20)}')

