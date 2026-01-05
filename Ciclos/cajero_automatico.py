print('*** Aplicación de cajero automático ***')

Saldo_inicial = 1200
Salir = False
while not Salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir''')

    opcion = int(input('Escoja una opción:'))
    if opcion == 1:
        print(f'Tu saldo actual es : ${Saldo_inicial}')
    elif opcion == 2:
        retiro = float(input('Saldo a retirar'))
        if retiro <= Saldo_inicial:
            Saldo_inicial -= retiro
            print(f'Tu nuevo saldo es de: {Saldo_inicial:.2f}')
        else:
            print(f'No cunetas con el saldo suficiente.\nEl saldo actual es de: ${Saldo_inicial:.2f}')
    elif opcion== 3:
        deposito = float(input('Monto a depositar: '))
        Saldo_inicial += deposito
        print(f'Deposito realizado con éxito')
        print(f'Deposito Actual: ${Saldo_inicial}')
    elif opcion == 4:
        print(f'Saliendo del cajero ATM. '
              f'Hasta pronto!')
        Salir = True
    else:
        print('Opción inválida. Seleccióne una de las opciones')
