print('*** Promedio de Calificaciones ***')

total_calificaciones = int(input('Proporciona el numero de calificaciones:'))
calificaciones = []

for i in range(total_calificaciones):
    calificacion = float(input(f'Calificación {i}: '))
    calificaciones.append(calificacion)

print(f'\nLas calificaciones que se proporcionaron son: {calificaciones}')

#Sum() se usa para sumar los valores de...
suma_calif = sum(calificaciones)
prom = suma_calif/total_calificaciones
print(f'Promedio de las calificaciones {prom:.2f}')