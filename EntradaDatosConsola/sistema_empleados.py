print('*** Sistema de Empleados ***')
nombre_empleado = input('Nombre del Empleado:')
edad_empleado = int(input('Edad del empleado:'))
salario_empleado = float(input('Salario del empleado: $'))
es_jefe_departamento = input('¿Es jefe de departamento?(Si/No)')

#Convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento=es_jefe_departamento.lower() == 'si'

#Imprimimos todos
print('\nDatos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: ${salario_empleado:.2f}')
print(f'¿Es Jefe de Departamento? {es_jefe_departamento}')
