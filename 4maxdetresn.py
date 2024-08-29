n1 = float(input("Ingrese el 1er numero: "))
n2 = float(input("Ingrese el 2do numero: "))
n3 = float(input("Ingrese el 3er numero: "))

if n2 < n1 > n3:
    print(" El numero mayor es el 1er numero. Numero:", n1)
elif n1 < n2 > n3:
        print(" El numero mayor es el 2do numero. Numero:", n2)
elif n1 < n3 > n2:
          print(" El numero mayor es el 3er numero. Numero:", n3)
else:
       print("Todos los numeros ingresados son iguales.")