def suma(*args):
    return sum(args)

#print(suma(3,4,5,3))

def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg**2
    return total

#print(suma_cuadrados(1,2,4))

#PRACTICA ARGUMENTOS INDEFINIDOS 2
def suma_absolutos(*args):
    total = 0
    for arg in args:
        total += abs(arg)**2
    return total
#print(suma_absolutos(2,3,5,-7))

#PRACTICA ARGUMENTOS INDEFINIDOS 3
def numeros_personas(nombre,*args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'

print(numeros_personas("Jumled",2,2,1))