#archivo = open('prueba1.txt','a')
#lista = ['Hola','mundo','Aqui','estoy']

#for p in lista:
#    archivo.writelines(p+'\n')


registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open("prueba1.txt", 'a')
for l in registro_ultima_sesion:
    archivo.writelines(l + '\t')

archivo.close()
archivo = open('prueba1.txt', 'r')
print(archivo.read())