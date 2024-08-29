numero:int = int(input("Ingrese numero a operar "))
for i in range(0,6):
    resultado = i * numero
    resultadotwo = i % numero
    resultadothree = i + numero
    resultadofour = i - numero
    print(numero, " X ", i," = ",resultado)
    print(numero, " /  ", i, " = ",resultadotwo)
    print(numero, " + ", i," = ",resultadothree)
    print(numero," - ", i," = ", resultado)