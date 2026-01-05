print('*** Sistema de administración de cuentas ***')

salir = False
while not salir: #Mientras la variable de salir no sea verdadera
    print(f'''Menú:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Escoge una opción: '))
    if opcion == 1:
        print('\nCreando cuenta...\n')
    elif opcion == 2:
        print('Eliminado cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema...')
        print('Hasta pronto!\n')
        salir = True
    else:
        print('Opción invalida, proporciona otra opción...\n')
else:#El ciclo while permite igual trabajar con else, enviando algo al momento de terminar el programa
    print('Terminando el sistema de Administración de cuentas')