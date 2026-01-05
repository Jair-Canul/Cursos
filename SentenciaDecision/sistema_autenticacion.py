print('*** Sistema de autenticación ***')

USER = 'admin'
PASSWORD = '123'

introduce_usuario = input('Introduce nombre de Usuario ')
introduce_usuario = introduce_usuario.strip().lower()
introduce_password = input('introduce password ')
introduce_password = introduce_password.strip().lower()

if introduce_usuario == USER and introduce_password == PASSWORD:
    print('WELCOM TO THE SISTEM!')

elif introduce_usuario == USER:
    print('Password invalido')
elif introduce_password == PASSWORD:
    print('Usuario inválido')
else:
    print('Usuario y Password inválido')