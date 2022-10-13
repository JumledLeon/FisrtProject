nombres = ['Juan','Ana','Carlos','Belen','Fran']
for elem in nombres:
    num_letra = nombres.index(elem) + 1
    print(f"Letra {num_letra}: {elem}")

nums = [1,2,3,4,5]
mi_valor = 0
for num in nums:
    mi_valor = mi_valor + num
    print(mi_valor)

palabra = 'Python'
for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print('\nPROBANDO CON DICCIONARIOS')
dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.values():
    print(item)

print('\nTEST')
print(4%2)