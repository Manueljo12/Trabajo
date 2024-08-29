nombres = input ("Inserte varios nombres ").split()
for nombre in (nombres):
    if len(nombre) == 5:
        print(nombre.upper())