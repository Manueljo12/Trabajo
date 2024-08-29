n = 0
x = 0
suma = 0
while n >= 0:
    n = int(input("Ingresa un numero: "))
    if n > 0:
        x = x + 1
        suma = suma + n
print("El total de numeros positivos es: ", x)
print("El promedio de los numeros es: ", suma/x)