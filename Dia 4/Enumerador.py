lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice +=1

print('\n EJEMPLO 2')
lista2 = ['a','b','c']
for indice,item in enumerate(lista2):
    print(indice,item)

print('\n EJEMPLO 3')
lista2 = ['a','b','c']
for item in enumerate(lista2):
    print(item)

print('\n EJEMPLO 4')
for item in enumerate(range(50,55)):
    print(item)

print('\n EJEMPLO 5')
lista3 = ['a','b','c']
mis_tuples = list(enumerate(lista3))
print(mis_tuples)
print(mis_tuples[1][0])

print('\n PRACTICA 1')
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for nombre,indice in list(enumerate(lista_nombres)):
    print(f'{indice} se encuentra en el índice {nombre}')

print('\n PRACTICA 2')
listax = list(enumerate("Python"))
print(listax)

print('\n PRACTICA 3')
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indicesx,nombrex in enumerate(lista_nombres):
    if nombrex.startswith('M'):
        print(indicesx)