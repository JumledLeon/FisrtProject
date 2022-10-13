print('\nEJEMPLO #INTEGER RANDOM')
from random import *
#aleatorio = randint(1,50)
#aleatorio = round(uniform(1,5),1)
#aleatorio = random()
colores = ['azul','rojo','verde','amarillo']
#aleatorio = choice(colores)
numeros = list(range(5,50,5))
print(numeros)
#SHUFFLE no se puede almacenar en una lista
shuffle(numeros)
print(numeros)