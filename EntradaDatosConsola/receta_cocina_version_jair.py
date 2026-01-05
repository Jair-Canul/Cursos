print('*** Receta de Cocina ***')
nombre_receta = input('Ingresa el nombre de la receta: ')
ingredientes = input('Ingresa los ingredientes: ')
tiempo_preparacion = int(input('Ingresa el tiempo de preparación (min): '))
dificultad = input('Ingresa la dificultad (Fácil/Media/Alta): ')

#imprimir todos los datos
print("-------------------------------------")
print(f'Nombre de la receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación: {tiempo_preparacion}min')
print(f'Dificultad: {dificultad}')