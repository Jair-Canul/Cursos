print('*** Manejo de Listas ***')

mi_lista = [1,2,3,4,5]
print(f'{mi_lista}--> Lista original')

#Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

#Acceder a los elementos de la lista por índice
print(f'Acceder el valor del índice 4 {mi_lista[4]}')
print(f'Acceder al último índice de la lista {mi_lista[-1]}')

#mODIFICAR LSO ELEMENTOS DE UNA LISTA
mi_lista[1] = 10
print(f'Modificamos el valor del índice 1: {mi_lista[1]}')

#Agregar un nuevo elemento al fin de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agregó el elemento 6')

#Añadir un nuevo elemento en un índice especifico
mi_lista.insert(2,15)
print(f'{mi_lista} -> Se añadió el valor de 15 en el índice 2')

#Eliminar elementos de una lista
#usando el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} --> Se removió el valor 5')
#Remover por indice con el metodo pop
mi_lista.pop(1) #Remueve el elemento del índice 1
print(f'{mi_lista} --> Se eliminó el índice 1')
#Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} --> Se eliminó el índice 2')
#obtener sublistas
sublista = mi_lista[1:3] # genera una sublista del índice 1 al 2 (3 no se inlcuye)
print(f'Sublista [1:3]: {sublista}')
