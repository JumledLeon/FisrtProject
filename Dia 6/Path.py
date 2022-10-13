from pathlib import Path

base = Path.home()
guia = Path(base,'Europa','Espana',Path('Barcelona','Sagrada_familia.txt'))
#print(base)
#print(guia)
guia2 = guia.with_name('La_Pedrera.txt')
#print(guia2)

#print(guia.parent)
#print(guia.parent.parent)

#Enumerar archivos en una ruta
guia = Path(Path.home(),'Europa')

for txt in Path(guia).glob('**/*.txt'):
    print(txt)

guia4 = Path('Europa','Espana','Barcelona','Sagrada_familia.txt')
en_europa = guia4.relative_to(Path('Europa'))
en_espana = guia4.relative_to(Path('Europa','Espana'))
print(en_europa)
print(en_espana)
