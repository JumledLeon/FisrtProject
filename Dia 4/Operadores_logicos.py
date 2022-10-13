mi_bool2 = 4 < 5 and 5 > 6
mi_bool3 = 4 < 5 or 5 > 6
texto1 = 'esta frase es breve'
mi_bool4 = ('frase' in texto1) or ('python' in texto1)
mi_bool5 = not 'a' != 'a'

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = (palabra1 not in frase) and (palabra2 not in frase)
print(mi_bool)
