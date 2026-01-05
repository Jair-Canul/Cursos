print('*** Aplicación Calculadora ***')

salir = False
while not salir:
    print('''Opciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        numero1= float(input('Dame el valor 1: '))
        numero2= float(input('Dame el valor 2: '))
        suma = numero1 + numero2
        print(f'El resultado de la suma es: {suma:.2f}\n')
    elif opcion == 2:
        numero1 = float(input('Dame el valor 1: '))
        numero2 = float(input('Dame el valor 2: '))
        resta = numero1 - numero2
        print(f'El resultado de la resta es: {resta:.2f}\n')
    elif opcion == 3:
        numero1 = float(input('Dame el valor 1: '))
        numero2 = float(input('Dame el valor 2: '))
        multiplicacion = numero1 * numero2
        print(f'El resultado de la multiplicación es: {multiplicacion:.2f}\n')
    elif opcion == 4:
        numero1 = float(input('Dame el valor 1: '))
        numero2 = float(input('Dame el valor 2: '))
        division = numero1 / numero2
        print(f'El resultado de la división es: {division:.2f}\n')
    elif opcion == 5:
        print('Saliendo del programa de Calculadora. Hasta Pronto!')
        salir = True
    else:
        print('Opción invalida, seleccione otra opción...\n')
