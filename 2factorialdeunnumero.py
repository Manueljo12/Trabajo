n = int(input(" Ingresa un numero:"))
if n >= 0:
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * 1
    print(f"El factorial de {n} es: {factorial}")
else:
    print("No se puede calcular el factorial")