def calculadora():
    print("Bienvenido a la calculadora")
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingresa el número de la operación (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print("Resultado:", sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", restar(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida.")
