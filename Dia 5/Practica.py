#PRACTICA

palabra = '12345'
def invertir_palabra(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida.upper()
plb = invertir_palabra('Hola')
print(plb)


