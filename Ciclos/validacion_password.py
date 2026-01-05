print('Creación y validación de un Password')

password = input('Ingrese el nuevo Password: ')

while len(password) < 6:
    print('Password invalido. Password demasiado corto, minimo 6 caracteres')
    password = input('Ingresa un nuevo valor de password: ')
else:
    print('Password válido')