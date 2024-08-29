n = int(input("Ingrese un numero para identificar si es primo: "))
x = 1
y = 0
while x <= n:
    if n % x == 0:
        y = y + 1
    x = x + 1
if y == 2:
    print("El numero ",n,"es primo")
else:
    print("El numero ",n,"no es primo")