#Sistema Generador ID Único
#Con los datos recibidos el sistema deberá 
# realizar lo siguiente:
# 
# 1. Del valor recibido de nombre, 
# usar solo las 2 primeras letras
# y convertirlas a mayúscula
# 
# 2. Del valor de apellido, usar las 2
# primeras letras y convertirlas a mayúsculas
# 
# 3.Del valor de año, tomas los 2 últimos Dígitos
# 
# Además el sistema deberá generar 
# un valor aleatorio de 4 dígitos,
# con ayuda de la función randint() #

#Importamos randint()
from random import randint

#Input
print("*** Sistema Generador de ID Unico ***")
nombre = input("¿Cuál es tu nombre?: ")
apellido = input("¿Cuál es tu apellido?: ")
nacimiento = str(input("¿Cuál es tu año de nacimiento?(YYYY): "))

#Proceso

id_nombre = nombre[0:2].upper().strip()
id_apellido = apellido[0:2].upper().strip()
id_nacimiento = nacimiento[2:4]

#Numeros aleatorios
n1= str(randint(0,9))
n2= str(randint(0,9))
n3= str(randint(0,9))
n4= str(randint(0,9))

#ID único:
id=id_nombre+id_apellido+id_nacimiento+n1+n2+n3+n4

print("")

print(f"""Hola {nombre} {apellido},
        Tu nuevo número de identificación (ID) generado por el sistema es:
        {id}
        Felicidades!""")