Lista=[]
Numeros = int(input("¿Cuantos numeros desea ingresar?"))
i=1
while i <= Numeros:
    n = int(input(f"{i}Ingrese numero: "))
    Lista.append(n)
    i+=1
print("Numero mayor es ",max(Lista))