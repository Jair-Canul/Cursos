#Version con entrada de datos

print('*** Generador de Email Actualizado (Versión Jair) ***')

#Nombre
nombre_user = input('Nombre(s):  ')
nombre_user=nombre_user.strip().lower().replace(' ', '.')
#print(nombre_user)

#Apellidos
apellidos_user = input('Apellidos: ')
apellidos_user=apellidos_user.strip().lower().replace(' ','.')
#print(apellidos_user)

#Nombre compleo
nombre_completo=nombre_user+'.'+apellidos_user
#print(nombre_completo)

#Nombre de la empresa
nombre_empresa = input('Nombre de la empresa: ')
nombre_empresa=nombre_empresa.lower().replace(' ','')
#extensión del dominio
extension_dominio = input('Ingrese la extensión del dominio: ')

#correo completo
correo_completo = nombre_completo + '@' + nombre_empresa + extension_dominio

print(f''' 
Tu nuevo Email generado por el sistema es:
        {correo_completo}
        !Felicidades¡''')
