#import os
from pathlib import Path

#Cambiar directorio
#ruta = os.chdir('C:\\Users\\Usuario\\Documents\\OneDrive\\Cursos\\4. Udemy\\3. Python\\Dia 6 - Programar Recetario')

#Crear directorios
#ruta = os.makedirs('C:\\Users\\Usuario\\Documents\\OneDrive\\Cursos\\4. Udemy\\3. Python\\Dia 6 - Programar Recetario\\Otra\\Text.txt')

#ruta = 'C:\\Users\\Usuario\\Documents\\OneDrive\\Cursos\\4. Udemy\\3. Python\\Dia 6 - Programar Recetario\\Prueba.txt'
#Obtener el nombre del archivo
#nombre_archivo = os.path.basename(ruta)
#Obtener la ruta completa del archivo
#ruta_base = os.path.dirname(ruta)
#Obtener ambas rutas separadas
#elemento = os.path.split(ruta)
#print(nombre_archivo)
#print(ruta_base)
#print(elemento)

#Eliminando directorios vacios
#os.rmdir('C:\\Users\\Usuario\\Documents\\OneDrive\\Cursos\\4. Udemy\\3. Python\\Dia 6 - Programar Recetario\\Otra')

#otro_archivo = 'Prueba.txt'

#######################################3
# Usando Pathlib
carpeta = Path('C:/Users/Usuario/Documents/OneDrive/Cursos/4. Udemy/3. Python/Dia 6 - Programar Recetario')
archivo = carpeta / 'Prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())