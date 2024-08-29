def calculadora():
    while True:
        print("\nSelecciona la operacion:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Introduce el número de la operación que deseas realizar: ")

        if opcion == '5':
            print("¡Nos vemos pronto!")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Error: Debes introducir números válidos.")
                continue

            if opcion == '1':
                resultado = num1 + num2
                print(f"El resultado de {num1} + {num2} es: {resultado}")

            elif opcion == '2':
                resultado = num1 - num2
                print(f"El resultado de {num1} - {num2} es: {resultado}")

            elif opcion == '3':
                resultado = num1 * num2
                print(f"El resultado de {num1} * {num2} es: {resultado}")

            elif opcion == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"El resultado de {num1} / {num2} es: {resultado}")
                else:
                    print("Error: No se puede dividir por cero.")
        else:
            print("Opción errada. Hazlo de nuevo.")

calculadora()
