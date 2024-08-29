n = int(input("ingrese el numero deseado para sumar sus digitos: "))
suma = 0
while n > 0:
    suma = suma + (n % 10)
    n = n // 10
print("La suma de los digitos es: ",suma)