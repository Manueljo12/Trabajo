def tablademultiplicar(numero1, numero2):
    return str(numero1) + " x " + str(numero2) + " = " + str(numero1*numero2)

n = int(input("Ingrese el numero que desea hallar su tabla de multiplicar: "))

for x in range(0, 6):
    print(tablademultiplicar(n,x))