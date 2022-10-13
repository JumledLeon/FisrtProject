palabra = 'pyhton'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

#VAMOS A COMPRIMIR EL CODIGO
lista2 = [letra for letra in palabra]
print(lista2)

#TAMBIEN PODEMOS USAR CON NUMEROS
lista3 = [n for n in range(0,21,2)]
print(lista3)

#TAMBIEN PODEMOS REALIZAR OPERACIONES
lista4 = [n/2 for n in range(0,21,2)]
print(lista4)

lista5 = [n if n*2 > 10 else 'no' for n in range(0,21,2)]
print(lista5)

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n%2 == 0]
print(valores_pares)