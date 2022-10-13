def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=2, y=4, z=5))

#EJEMPLO 2
print('\nEJEMPLO #2\n')

def prueba(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]
kwargs = {'x':'1','y':"dos",'z':'tres'}
prueba(15,20,*args,**kwargs)

#EJERCICIO 1
print('\nArgumentos Indefinidos (*kwargs) 1\n')

def cantidad_atributos(**kwargs):
    total = 0
    for clave in kwargs:
        total += 1
    return total

#EJERCICIO 2
print('\nArgumentos Indefinidos (*kwargs) 2\n')

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

print(lista_atributos(**kwargs))

#EJERCICIO 3
print('\nArgumentos Indefinidos (*kwargs) 3\n')

def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}:')
    for clave,valor in kwargs.items():
        print(f'{clave} : {valor}')

describir_persona("María", color_ojos="azules", color_pelo="rubio")