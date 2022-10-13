from random import *

# Lanzar datos
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    #print(dado1, dado2)
    return dado1, dado2


suma_dados = 0

def evaluar_jugada():
    dado1, dado2 = lanzar_dados()
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

evaluar_jugada()
'''
import random


def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"'''