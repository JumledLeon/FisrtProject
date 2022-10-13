monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -=1
else: print('No tengo mas monedas')

print('\nEJEMPLO 2')
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for num in lista_numeros:
    if num >=0:
        print(num)
    else: break

