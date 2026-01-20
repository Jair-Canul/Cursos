# Receta de Cocina
# Crear un programa para solicitar algunos 
# valores importantes para una receta de cocina
# 
# Los valores que debe introducir el usuario son:
# Nombre de la Receta
# Ingredientes
# Tiempo de preparación (en minutos)
# Dificultad("Fácil, Media, alta")#

print("*** Receta de Cocina ***")
nombre_receta = input("Ingresa el nombre: ")
ingredientes = input("Ingresa los ingredientes: ")
tiempo_preparacion = int(input("Ingresa el tiempo de preparación(min): "))
dificultad= input("Ingresa la dificultad: ")

#Imprimir los valores de la receta
print("-" * 30)
print(f'Nombre de la receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación: {tiempo_preparacion} min.')
print(f'Dificultad: {dificultad}')