print('*** Operador de asignación ***')
numero = 5
print(f'valor de número {numero}')
numero = 10
print(f'valor de número {numero}')
cadena = 'saludos desde python'
print(f'valor de la cadena: {cadena}')

#Asignación múltiple:
x, y, z = 5, 'Hola Mundo', -9.15
print(f'\nValor de x = {x}, y = {y}, z = {z}')

 #Asignación encadenada
a = b = c = 10
print(f'\nValor a = {a}, b = {b}, c = {c} ')

#intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'\nValores iniciales x = {x}, y = {y}')
#Aplicar el concepto de asignación multiple, intercambiamos valores
x, y = y, x
print(f'Invertir los valores x = {x}, y = {y}')

#recibir multiples Valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separado por coma: ').split(',') #Especificamos el separador
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')
