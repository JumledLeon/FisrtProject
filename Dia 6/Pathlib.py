from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/Usuario/Documents/OneDrive/Cursos/4. Udemy/3. Python/Dia 6 - Programar Recetario/Prueba.txt')
carpeta2 = Path('C:/Users/Usuario/Documents/OneDrive/Cursos/4. Udemy/3. Python/Dia 6 - Programar Recetario/Pruebas.txt')
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
#print(carpeta.read_text())
#Nombre del archivo
print(carpeta.name)
#Devuelve tipo de archivo
print(carpeta.suffix)
#Devuelve nombre sin terminacion
print(carpeta.stem)
#Validar si archivo existe
if not carpeta2.exists():
    print('Archivo no este')
else:
    print('Genial!, existe')

