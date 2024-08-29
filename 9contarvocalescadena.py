texto = input("Ingrese una frase para contar sus vocales: ")
vocales = "aeiouAEIOU"
C = 0
for i in texto:
    if i in vocales:
        C = C + 1

print(f"La frase tiene {C} vocales")