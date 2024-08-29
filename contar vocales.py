palabra = input("Ingrese una palabra: ")
vocales = ["aeiouAEIOU"]
x = 0
for x in palabra:
    if x in vocales:
        x += 1
        x = x + 1
print(f"la palabra tiene {x} vocales")