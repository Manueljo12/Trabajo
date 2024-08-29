numero.int = int(input("por favor ingresar un numero: "))
resultado:int = (numero % 2)

if resultado == 0:
    print(f"El numero{numero}es par")
else:
    print("El numero es impar",numero)
