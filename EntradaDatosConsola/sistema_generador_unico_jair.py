from random import randint

print('*** Sistema Generador de ID Único')

#Nombre
nombre = input('¿Cuál es tu primer nombre?: ')
nombre_final=nombre[0:2].upper().strip()
#print(nombre)

#Apellido
apellido = input('¿Cual es tu primer Apellido?: ')
apellido_final = apellido[0:2].upper().strip()
#print(apellido)

#Año de nacimiento
anio_nacimiento =str(input('¿Cuál es tu año de nacimiento?: ' ))
anio_nacimiento_final= anio_nacimiento[2:4]
#print(anio_nacimiento)

#Números random
numeros_random1 = str(randint(0,9))
numeros_random2 = str(randint(0,9))
numeros_random3 = str(randint(0,9))
numeros_random4 = str(randint(0,9))
total_numeros_random = numeros_random1+numeros_random2+numeros_random3+numeros_random4

#Generador ID único
generador_id=nombre_final + apellido_final + anio_nacimiento_final + total_numeros_random

#Imprimimos el ID
print(f'Hola {nombre} , \n\tTu nuevo número de identificación (ID) generado por el sistema es: \n\t{generador_id} \n\t¡Felicidades!')
