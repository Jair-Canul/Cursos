print('*** Manejo de Tuplas ***')

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

#no podemos modificar una tupla
#no mi_tupla [0] = 10
#no mi_tupla.append(6)

#Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

#Crear una tupla para una coordenada x, y
coordenadas = (3,5)
#accedemos a cada elemento de la tupla
print(f'\ncoordenadas en el eje x: {coordenadas[0]}')
print(f'coordenadas en el eje x: {coordenadas[1]}')

#Crear una tupla unitaria
tupla_un_elemento = 10,

print(f'\nTupla de un elemento: {tupla_un_elemento}')

#Tupla anidada
tuplas_anidadas = (1, (2,3),(4,5))
print(f'\nSegundo elemento tupla anidada: {tuplas_anidadas[1]}')