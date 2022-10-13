
lista_numeros = [1 ,2 ,15 ,7 ,2 ,8]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

#reducir_lista(lista_numeros)

def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio

print(promedio(reducir_lista(lista_numeros)))
