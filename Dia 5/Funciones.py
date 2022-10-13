def saludar_persona(nombre):
    '''Aqui vamos a saludar
    a una persona'''
    print(f'Hola {nombre}')

saludar_persona('Juan')

#OTRO EJEMPLO
def bienvenida():
    nombre_persona = 'Jum'
    print(f'¡Bienvenido {nombre_persona}!')
bienvenida()

#OTRO EJEMPLO
print('OTRO EJEMPLO')
def cuadrado(un_numero):
    #un_numero = 3
    print(un_numero**2)
cuadrado(5)

#USANDO 'RETURN' EN VEZ DE PRINT
print("\nUSANDO 'RETURN' EN VEZ DE PRINT")

def multiplicador(num1,num2):
    return num1*num2

resultado = multiplicador(4,50)
print(resultado)

#ejemplo 2
def multiplicador2(num3,num4):
    total2 = num3*num4
    print(total2)
    return total2

multiplicador2(2,10)
