print('*** Playlist de Canciones ***')

#Creamos la lista vacía
lista_reproduccion = []

numero_canciones = int(input('¿Cuántas canciones deseas agregar?'))

#iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'proporcione la canción {indice + 1}: ')
    lista_reproduccion.append(cancion)

#Empezamos a agregar canciones
lista_reproduccion.append('Hotel Californai - Eagles')
lista_reproduccion.append('Insane in the brain - Cypress Hill')
lista_reproduccion.append('Árboles de la barranca - El coyote')

#Ordenar la lista en orden alfabetico . sort
#lista_reproduccion.sort(reverse = True)
lista_reproduccion.sort()

#Mostrar la lista de canciones
print(f'\n Lista de reproducción en orden alfabético: ')
print(lista_reproduccion)

#Mostrar la lista iterando sus elementos
print()
for cancion in lista_reproduccion:
    print(f'- {cancion}')