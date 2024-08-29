numero = 82
binario = ""

while numero > 0:
    if numero %2 == 0:
        binario = "0" + binario
    else:
        binario = "1" + binario

    numero = numero // 2

print(binario)