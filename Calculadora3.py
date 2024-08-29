def tabla_de_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("\n")

def sumar_numero(numero1, numero2):
    return numero1 + numero2

def dividir_numero(numero1, numero2):
    if numero2 == 0:
        return "No es correcto dividir por cero"
    return numero1 / numero2

def calcular_exponencial(base, exponente):
    return base ** exponente

def calculadora():
    while True:
        try:
            # El usuario ingresa un número
            numero = float(input("Ingrese un numero: "))
            
            # Opciones de operación a realizar
            print("Elija una operacion: ")
            print("1. Crear tabla de multiplicar")
            print("2. Operacion de suma")
            print("3. Operacion de division")
            print("4. Operacion exponencial")
            opcion = input("Opcion (1/2/3/4): ").strip()
            
            if opcion == "1":
                tabla_de_multiplicar(numero)
                
            elif opcion == "2":
                otro_numero = float(input("Ingresa un numero para sumar: "))
                resultado = sumar_numero(numero, otro_numero)
                print(f"{numero} + {otro_numero} = {resultado}\n")
                
            elif opcion == "3":
                otro_numero = float(input("Ingresa un numero para dividir: "))
                resultado = dividir_numero(numero, otro_numero)
                if isinstance(resultado, str):  # Si el resultado es un mensaje de error
                    print(f"Error: {resultado}\n")
                else:
                    print(f"{numero} / {otro_numero} = {resultado}\n")
                
            elif opcion == "4":
                exponente = float(input("Ingrese el exponente: "))
                resultado = calcular_exponencial(numero, exponente)
                print(f"{numero} ^ {exponente} = {resultado}\n")
                
            else:
                print("Opcion incorrecta, elige una opcion entre 1, 2, 3 o 4.")
                
            # Aca preguntamos si desea realizar otra operacion
            continuar = input("Te gustaria realizar otra operacion? (s/n): ").lower()
            if continuar != "s":
                break
            
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número válido.\n")

calculadora()
