#ABRIENDO ARCHIVOS
mi_file = open('prueba.txt')

#Ejemplo 1:
una_linea = mi_file.readline()
print(una_linea.rstrip())
una_linea = mi_file.readline()
print(una_linea.rstrip())

#Ejemplo 2: Recorriendo linea por linea
#for l in mi_file:
#    print('Aqui dice:' + l)

#Ejemplo 3: Creando una LISTA de lineas
#todas = mi_file.readlines()
#todas = todas.pop() > Me quedo con la ultima linea
#print(todas)

#Siempre cerrar el archivo al final
mi_file.close()