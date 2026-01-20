#Sistema De Empleados
#Crear un progrma para solicitar la información de un empleado,
# introduciendo los datos por consola
# Los datos a solicitar son:
# Nombre Empleado
# Edad Del Empleado
# Salario del Empleado
# Es jefe de departamento (Si/No)

print("*** Sistema de Empleados *** ")
nombre_empleado = input("Nombre del empleado: ")
edad_empleado= int(input("Edad del empleado: "))
salario_empleado = float(input("Salario del empleado: "))
es_jefe_departamento = input("Es jefe departamento(Si/No): ")

#Vamos a convertir a un tipo boll la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si" #Lo compara y nos muestra True o False

#Imprimir los valores del empleado
print("\n*** Datos del Empleado ***")
print(f'Nombre: {nombre_empleado}')
print(f"Edad: {edad_empleado} años")
print(f'Salario: ${salario_empleado:.2f}') #:.2f para mostrar dos decimales
print(f'¿Es jefe de departamento?: {es_jefe_departamento}')



