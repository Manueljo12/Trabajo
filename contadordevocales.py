letras:str = str(input("ingrese la palabra para contar las vocales ").lower())
vocales:str = "aeiou"
contador:int = 0
for letra in letras:
    if letra in vocales:
        contador += 1
print("el numero total de vocales son", contador)
    