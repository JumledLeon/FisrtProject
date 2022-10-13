#PROYECTO DEL DIA 4
from random import *
name = input('¿Cual es tu nombre?: ')
intentos = 8
numero_pensado = randint(1,100)
print(f'Hola {name}, he pensado un numero entre 1 y 100. Tienes {intentos} intentos')

while intentos > 0:
    numero_elegido = int(input('¿Puedes adivinar cual es?: '))
    #print(f'\nPense en {numero_pensado}')
    intentos -= 1
    if numero_elegido < 1 or numero_elegido > 100:
        print('El numero elegido esta fuera de rango')
    elif numero_pensado > numero_elegido:
        print('El numero que elegiste es MENOR al que pense')
    elif numero_pensado < numero_elegido:
        print('El numero que elegiste es MAYOR al que pense')
    elif numero_pensado == numero_elegido:
        print(f'LE ACERTASTE!!! Y solo te tomo {8 - intentos} intentos')
        break
    else: print('ESCENARIO ERRADO')

if numero_elegido != numero_pensado:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_pensado}")
