print('*** Sistema Autenticación ***')

USUARIO = 'admin'
PASSWORD = '123'

nombre_usuario = input('¿Cuál es tu usuario? ')
password_usuario = input('¿cual es tu password? ')

datos_correctos= (nombre_usuario.strip().lower() == USUARIO
                  and password_usuario.strip().lower() == PASSWORD)

print(f'¿Datos correctos? {datos_correctos}')